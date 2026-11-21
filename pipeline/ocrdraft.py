"""Stage 1 without Wikisource: a base text read from 1738's own OCR (decision 68; data/review/exod31-40-plan.md).

Wikisource has no text for Exodus 31–40 (nor for most of M6). This builds the working text from 1738's hOCR
(archive.org bibliasacraexseb01cast), in three steps:

1. `page_lines`: each leaf's body lines, column by column, without the running head, the chapter heading (CAPVT …,
   kept as the chapter's start), the italic chapter summary under it (decision 67: no summaries anywhere), the
   signature mark and the catchword at the page's foot; the verse numbers in the margins are taken off the line and
   kept as its `margin` (the OCR often glues a number to the line's first or last word: "7arcam", "cæspitium24").
2. `vote`: each word, or a repair of it (long s read as f, rn for m, x for æ, cl for ct …), kept where it is a known
   Latin form (the settled text's, Wikisource's, 1738's printed forms, the `latin macron` lexicon); else 1750's,
   Wikisource's or 1726's word at the same place (each aligned to 1738 word by word), in that order, repaired the
   same way (Wikisource's in 1738's letters where a repair of the OCR word gives it); else the OCR's word. Where two
   or more of the others agree with each other against the voted word, the place is listed for the readers
   (`doubts`). 1738 is never outvoted: 1750 and Wikisource share readings 1738 lacks (Judg 1:12 *Calebus*).
3. `lines_tsv`: the result as one row per printed line (`leaf column line text`), the verse starts marked `#N`
   before their word and chapters as `\\c N` rows: the file the page reading corrects (stage 2), every column read
   on the page images. `to_usfm` turns the read lines into the draft (hyphens joined, u/v and i/j and ae as
   Wikisource writes them, the BSB's paragraphs).

Verse numbers: 1738 prints them in the margin beside the line where a verse begins, not before its word, so the
word is placed after the line's sentence stop (or at the line's start when the line before ends one), and 1726
(whose OCR prints the number inline, before its word) decides where it can. Every placement is checked when the
column is read, with the KJV beside it."""

import collections
import difflib
import html
import json
import re
from dataclasses import dataclass, field

from pipeline import paths

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
CHAPTER = re.compile(r"^C\s*A\s*P\s*[VU]\s*T\s*(.*)$")
# The heading with its capitals misread as small letters (1738 leaf 318, Ruth: "cApvT i."): only with a numeral
# alone after it, so that a text line opening with *caput* is not taken for one.
CHAPTER_LOOSE = re.compile(r"^[Cc]\s*[Aa]\s*[Pp]\s*[VvUu]\s*[Tt]\s*([IVXLivxl]+)\s*\.?$")
# The heading with specks read into it (1738 leaf 347, 1 Sam 23: "~~ i Ca Tp VT _ XXIII.-"): its letters squashed
# together and capitalized, a stray letter allowed between those of CAPVT, on a short line.
CHAPTER_SPECKED = re.compile(r"C.?A.?P.?[VU].?T([IVXL]+)$")
# A chapter's first line, opening with its drop capital: two capitals then small letters (PAlæstini), or the capital
# read apart from its word (T Dauid).
DROP_START = re.compile(r"^(?:[A-Z]{2}[a-zæœ]|[A-Z]\s+[A-Z]?[a-zæœ])")
# What a margin number looks like in the OCR: digits and the letters and marks it reads them as.
NUMBERISH = re.compile(r"^[0-9IlOoSgq|%^*<>&;:{}()\[\]?\-'.,\"’`~\\/zZ]+$")
LEAD = re.compile(r"^(?:&lt;|&amp;|[0-9|%^*<>&;:{}()\[\]?'\"’`~\\/])+")
TRAIL = re.compile(r"(?:[0-9|%^*<>&;:{}()\[\]?'\"’`~\\/-]|(?<=[a-z,.;:])[IlOoSg]{1,2})+$")


@dataclass
class Line:
    leaf: int
    column: int                      # 0 left, 1 right
    number: int                      # the hOCR's line number on the leaf
    y: int
    words: list                      # [(text, (x0, y0, x1, y1))]
    margin: str = ""                 # the margin number's OCR text, if any
    kind: str = "body"               # body, head, title, chapter, summary, catch, signature, footnote, margin
    chapter: int | None = None       # for a chapter heading: its number

    @property
    def text(self):
        return " ".join(t for t, _ in self.words)


def chapter_number(line, previous):
    """A heading's chapter number, read in sequence. The OCR reads the numeral's last I as L, and an I inside it as
    1 (1738 leaf 322, 1 Sam 1 "CAPVT L"; 333 "XIL"; 335 "XI1IL"): where the number read is not the next one and the
    numeral with those read as I is, the next one is taken."""
    if line.chapter == previous + 1:
        return line.chapter
    m = re.search(r"[IVXLl1]+[.,]?\s*$", line.text)
    if m:
        alt = re.sub(r"L(?=[.,]?\s*$)", "I", m.group().replace("1", "I").replace("l", "I"))
        if roman(alt) == previous + 1:
            return previous + 1
    return line.chapter or previous + 1


def roman(text):
    """CAPVT XXXI. → 31 (None if no numeral)."""
    m = re.search(r"[IVXLC]+", text.replace("l", "I"))
    if not m:
        return None
    total, last = 0, 0
    for ch in reversed(m.group()):
        v = ROMAN[ch]
        total, last = (total - v, last) if v < last else (total + v, v)
    return total


def _median(values):
    values = sorted(values)
    return values[len(values) // 2] if values else 0


def classify(words, size):
    """[Line] of one page: words [(text, box, line number)] in reading order, size (width, height). Pure (no files),
    so it can be tested on a made-up page."""
    width, height = size
    grouped = collections.OrderedDict()
    for text, box, n in words:
        if text.strip():
            grouped.setdefault(n, []).append((html.unescape(text.strip()), box))
    lines = []
    for n, ws in grouped.items():
        x0, y0 = min(b[0] for _, b in ws), min(b[1] for _, b in ws)
        x1 = max(b[2] for _, b in ws)
        column = 0 if (x0 + x1) / 2 < width / 2 else 1
        line = Line(0, column, n, y0, ws)
        bare = re.sub(r"^[^A-Za-z]+", "", line.text)
        # The running head: the book's name in spaced capitals, Cap. 35. 36., the page number (a text line can also
        # stand that high, at a column's top: Exod 147 "gintabulis exarata").
        if y0 < 60 and (re.search(r"Cap|[A-Z]\s?[A-Z]\s?[A-Z]\s?[A-Z]|^\W*\d|\d\.\s?\d", line.text)
                        or all(len(t) <= 3 for t, _ in ws)):
            line.kind = "head"
        elif CHAPTER.match(bare):
            line.kind, line.chapter = "chapter", roman(CHAPTER.match(bare).group(1))
        elif CHAPTER_LOOSE.match(bare):
            line.kind, line.chapter = "chapter", roman(CHAPTER_LOOSE.match(bare).group(1).upper())
        elif len(ws) <= 8 and len(squashed := re.sub(r"[^A-Za-z]", "", line.text)) <= 16 \
                and (m := CHAPTER_SPECKED.search(squashed.upper())):
            line.kind, line.chapter = "chapter", roman(m.group(1))
        lines.append(line)
    # A book's title across both columns in mid-page (1738 leaf 156: LEVITICVS. under Exodus's last lines): the
    # columns above it are read before those below it, and the title is not the text.
    titles = [l.y for l in lines if l.kind == "body" and l.y > 0.1 * height
              # wider than a column, or a short title standing across the page's middle (1738 leaf 318: RVTHA.)
              and (max(b[2] for _, b in l.words) - min(b[0] for _, b in l.words) > 0.5 * width
                   or min(b[0] for _, b in l.words) < 0.45 * width < 0.55 * width < max(b[2] for _, b in l.words))
              and re.fullmatch(r"[A-Z][A-Z\s]{3,}\.?", l.text.strip())]
    for line in lines:
        if line.y in titles:
            line.kind = "title"
    # The page's lines band by band (above and below a title), column by column, top to bottom (the OCR's own order
    # can set a line out of place: 1738 leaf 146, a chapter summary's last line after the text's first lines).
    lines.sort(key=lambda l: (l.kind != "head", sum(t <= l.y for t in titles), l.column, l.y))
    # A heading whose numeral the OCR set as a line of its own (CAPVT | XXXVI.)
    for k, line in enumerate(lines[:-1]):
        nxt = lines[k + 1]
        if line.kind == "chapter" and line.chapter is None and abs(nxt.y - line.y) < 25 \
                and re.fullmatch(r"[IVXLl.\s]+", nxt.text):
            line.chapter, nxt.kind = roman(nxt.text), "head"
    body = [l for l in lines if l.kind == "body"]
    usual = _median([_median([b[3] - b[1] for _, b in l.words]) for l in body]) or 36
    # The foot: a signature mark (F 3) and the catchword, the next page's first word, under the last line.
    for line in body:
        if line.y > 0.93 * height and (len(line.words) <= 2 or line.words[0][1][0] > 0.6 * width
                                       and len(line.words) <= 3):
            line.kind = "catch"
    # A catchword that is the next chapter's heading (CAPVT alone, at the foot): not a chapter here.
    for line in lines:
        if line.kind == "chapter" and line.chapter is None and line.y > 0.8 * height:
            line.kind = "catch"
    # Footnotes under the columns: from the first line at the foot that opens with a note's letter (h) scilicet …),
    # every line as low or lower, in either column.
    starts = [l.y for l in lines if l.kind == "body" and l.y > 0.6 * height and l.words
              and re.match(r"^[a-zA-Z*]{1,2}\)", l.words[0][0])]
    if starts:
        for line in lines:
            if line.kind == "body" and line.y >= min(starts) - 10:
                line.kind = "footnote"
    body = [l for l in lines if l.kind == "body"]
    # The summary under a chapter heading: the lines after it, up to and including the first that ends a sentence
    # and stands before the chapter's text (a line of the usual height, or one indented beside a drop capital).
    for i, line in enumerate(lines):
        if line.kind != "chapter":
            continue
        k = i + 1
        while k < len(lines) and lines[k].kind != "body":
            k += 1
        while k < len(lines) and lines[k].column == line.column and lines[k].kind == "body":
            current = lines[k]
            h = _median([b[3] - b[1] for _, b in current.words])
            # The text's first line, under a summary whose last stop the OCR lost: it opens with the drop capital,
            # read as two capitals (1738 leaf 339, 1 Sam 17 "PAlxftini") or a capital standing apart (344, 1 Sam 20
            # "T DauidaNaiotho")
            if k > i + 1 and DROP_START.match(re.sub(r"^[^A-Za-z]+", "", current.text)):
                break
            current.kind = "summary"
            nxt = lines[k + 1] if k + 1 < len(lines) else None
            ends = current.text.rstrip().endswith(".")
            nh = _median([b[3] - b[1] for _, b in nxt.words]) if nxt else usual
            if ends and (nxt is None or nh >= 0.9 * usual or h >= 0.9 * usual):
                break
            # A summary whose last stop the OCR lost (1738 leaf 342, 1 Sam 18: "nupta re?;,;"): the next line is in
            # the text's larger type, this one in the summary's smaller.
            # (Not when this line breaks a word: the summary runs on, 1738 leaf 346, 1 Sam 21 "D.mid. Sa-" / "cri panes.")
            if nxt is not None and h < 0.85 * usual and nh >= 0.95 * usual \
                    and not current.text.rstrip().endswith("-"):
                break
            k += 1
    # Margins: each column's text edges, from its body lines; a word outside them is the margin's number.
    for column in (0, 1):
        col = [l for l in lines if l.column == column and l.kind == "body"]
        if not col:
            continue
        # The text's edges: where each line's first (last) real word starts (ends), a word of three letters or more.
        left = _median([next((b[0] for t, b in l.words if sum(c.isalpha() for c in t) >= 3), l.words[0][1][0])
                        for l in col])
        right = _median([next((b[2] for t, b in reversed(l.words) if sum(c.isalpha() for c in t) >= 3),
                              l.words[-1][1][2]) for l in col])
        for l in col:
            strip_margin(l, column, left, right)
            # A line of margin only (numbers, a drop capital's box, the gutter's specks): not the text.
            if not any(sum(c.isalpha() for c in t) >= 2 for t, _ in l.words):
                l.kind = "margin"
    return lines


def _cut(text, box, pixels, lead):
    """How many characters of a word lie `pixels` into the margin (by the word's mean letter width)."""
    width = max(1, box[2] - box[0]) / max(1, len(text))
    n = int(round(max(0, pixels - 8) / width))
    return max(0, min(n, len(text) - 1))


def strip_margin(line, column, left, right):
    """Take the margin number off a line: a whole word in the margin, or the characters of the first word (left
    column) or the last (right column) that lie in the margin, by their place on the page."""
    words = list(line.words)
    if column == 0:
        while len(words) > 1 and words[0][1][2] < left + 6:
            line.margin += words.pop(0)[0]
        if words and words[0][1][0] < left - 18:
            text, box = words[0]
            n = _cut(text, box, left - box[0], True)
            m = LEAD.match(text)
            n = max(n, m.end() if m and m.end() < len(text) else 0)
            if n:
                line.margin += text[:n]
                words[0] = (text[n:], box)
    else:
        while len(words) > 1 and words[-1][1][0] > right - 4:
            line.margin = words.pop()[0] + line.margin
        if words and words[-1][1][2] > right + 18:
            text, box = words[-1]
            n = _cut(text, box, box[2] - right, False)
            m = TRAIL.search(text)
            n = max(n, len(text) - m.start() if m and m.start() > 0 else 0)
            if n:
                line.margin = text[-n:] + line.margin
                words[-1] = (text[:-n], box)
    line.words = words


def page_lines(key, leaf):
    """[Line] of one leaf of an edition's hOCR."""
    from pipeline import archive
    _, words, size = archive.pages(key)[leaf]
    out = classify([(w.text, w.box, w.line) for w in words], size)
    for line in out:
        line.leaf = leaf
    return out


# ---------------------------------------------------------------- repair and vote

REPAIRS = [("rn", "m"), ("x", "æ"), ("cl", "ct"), ("ch", "ct"), ("fl", "st"), ("ft", "st"), ("lh", "li"), ("ni", "m"),
           ("in", "m"), ("ri", "n"), ("h", "b"), ("e", "c"), ("c", "e"), ("l", "i"), ("i", "l"), ("n", "u"),
           ("u", "n"), ("f", "s"), ("r", "t"), ("t", "r"), ("a", "e"), ("o", "e")]
KNOWN_CACHE = paths.SOURCES / "cache" / "ocrdraft-known.json"


def known_forms():
    """(settled, all): folded forms the settled text has, and every known form (Wikisource's words, the settled
    text's, 1738's printed forms read across the Old Testament)."""
    from pipeline import align, books, gold, rules, tsv
    settled, every = set(), set()
    for book in books.BOOKS:
        for row in gold.load(book.osis).values():
            for w, is_word in align.words(row["text"]):
                if is_word:
                    settled.add(align.fold(rules.unmacron(w)))
        path = paths.WITNESSES / "wikisource" / f"{book.osis}.tsv"
        if path.exists():
            for row in tsv.read(path):
                for w, is_word in align.words(align.clean(row["text"])):
                    if is_word:
                        every.add(align.fold(w))
    return settled, every | settled


def looked_up(candidates):
    """The candidates `latin macron` knows (cached in sources/cache/ocrdraft-known.json)."""
    from pipeline import latin
    cache = json.loads(KNOWN_CACHE.read_text(encoding="utf-8")) if KNOWN_CACHE.exists() else {}
    todo = sorted({c for c in candidates if c not in cache})
    for i in range(0, len(todo), 200):
        _, out = latin.run(["macron", *todo[i:i + 200]], capture=True)
        unknown = set(re.findall(r"^(\S+): no source knows", out.replace("\r", ""), re.M))
        cache.update({c: c not in unknown for c in todo[i:i + 200]})
    KNOWN_CACHE.parent.mkdir(parents=True, exist_ok=True)
    KNOWN_CACHE.write_text(json.dumps(cache), encoding="utf-8")
    return {c for c in candidates if cache.get(c)}


def candidates(word):
    """The OCR word and its repairs, most likely first."""
    from pipeline import orig
    w = word.replace("ſ", "s")
    out = orig.long_s(w, w.replace("f", "s"))[:8]
    for old, new in REPAIRS:
        for c in list(out[:4]):
            i = c.find(old)
            while i >= 0:
                out.append(c[:i] + new + c[i + len(old):])
                i = c.find(old, i + 1)
    return list(dict.fromkeys(out))


@dataclass
class Voter:
    settled: set
    known: set
    how: collections.Counter = field(default_factory=collections.Counter)
    doubts: list = field(default_factory=list)      # [(line index, word index, OCR word, voted, the others' word)]

    def fix(self, word):
        """A known form of the word (the OCR's, or a repair), settled forms first; None if none."""
        from pipeline import align
        from pipeline import orig
        w = word.replace("ſ", "s")
        own = list(dict.fromkeys(orig.long_s(w, w.replace("f", "s"))[:8]))   # the word, its f put back to s
        cands = candidates(word)
        # The word or its long s first (settled forms before others: fex/sex, fine/sine, fi/si), then the repairs.
        for group in (own, cands):
            for pool in (self.settled, self.known):
                for c in group:
                    if align.fold(c) in pool:
                        return c
        return None

    def vote(self, word, others, names=None):
        """The voted word: the OCR's (or a repair) if known, else the first other witness's known word (`names`
        label them in `how`; Wikisource's word is put in 1738's letters, `in_print_letters`)."""
        fixed = self.fix(word)
        if fixed:
            self.how["1738"] += 1
            return fixed
        names = names or ["other"] * len(others)
        for other, name in zip(others, names):
            if other and (fixed := self.fix(other)):
                if name == "Wikisource":
                    fixed = in_print_letters(word, fixed)
                self.how[name] += 1
                return fixed
        self.how["unknown"] += 1
        return word


def in_print_letters(ocr, modern):
    """Wikisource's word written as 1738 would print it: the repair of the OCR word that folds to it (keeping 1738's
    u/v, i/j and æ), else the word with j as i (1738 prints no j)."""
    from pipeline import align
    target = align.fold(modern, fs=True)
    for c in candidates(ocr):
        if align.fold(c, fs=True) == target:
            return c
    return modern.replace("j", "i").replace("J", "I")


def doubts(voted, others):
    """[(index, the others' word)] where two or more other witnesses have a word at this place, all the same
    (folded: case, u/v, i/j, æ, long s), and the voted word is another: places for the readers to look at first.
    `others` are {index: word} maps (`paired`)."""
    from pipeline import align
    out = []
    for i, v in enumerate(voted):
        there = [m[i] for m in others if m.get(i)]
        if len(there) < 2:
            continue
        folded = {align.fold(w, fs=True) for w in there}
        if len(folded) == 1 and folded != {align.fold(v, fs=True)}:
            out.append((i, there[0]))
    return out


def paired(witness, words):
    """{index in words: the witness's word there}: the witness aligned word by word to the token list."""
    from pipeline import align
    folded = [align.fold(t, fs=True) for t in words]
    out = {}
    step = 400
    for start in range(0, len(words), step):
        chunk = words[start:start + step]
        win = witness.locate(chunk)
        if not win:
            continue
        b = witness.folded[win[0]:win[1]]
        sm = difflib.SequenceMatcher(None, folded[start:start + step], b, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag in ("equal", "replace") and i2 - i1 == j2 - j1:
                for k in range(i2 - i1):
                    out[start + i1 + k] = witness.tokens[witness.word_at[win[0] + j1 + k]][0]
    return out


# ---------------------------------------------------------------- the whole: lines with verses

STOP = re.compile(r"[.:;?!]$")


def build(key, leaves, voter=None, others=()):
    """(order, out): the body and chapter lines of the leaves in order, and {(line index, word index): voted word}.
    A word broken at a line's end (ma-|numittitor) is voted whole and cut again where the print cut it."""
    lines = [l for leaf in leaves for l in page_lines(key, leaf)]
    order = [l for l in lines if l.kind in ("body", "chapter")]
    units = []                                  # [(word, [(li, wi, letters)])]
    carry = None
    for li, line in enumerate(order):
        if line.kind != "body":
            continue
        for wi, (text, _) in enumerate(line.words):
            core = re.sub(r"^\W+|\W+$", "", text)
            if not core or not core[0].isalpha():
                continue
            if carry is not None and wi == 0:
                word, places = carry
                units.append((word + core, places + [(li, wi, len(core))]))
                carry = None
                continue
            if carry is not None:                 # the next line did not start with a word: keep the fragment
                units.append(carry)
                carry = None
            if wi == len(line.words) - 1 and text.endswith("-"):
                carry = (core, [(li, wi, len(core))])
            else:
                units.append((core, [(li, wi, len(core))]))
    if carry is not None:
        units.append(carry)
    out = {}
    words = [u[0] for u in units]
    voted = list(words)
    if voter is not None:
        names = [getattr(w, "name", "other") for w in others]
        pair_maps = [paired(w, words) for w in others]
        for i, w in enumerate(words):
            voted[i] = voter.vote(w, [m.get(i) for m in pair_maps], names)
        for i, other in doubts(voted, pair_maps):
            li, wi, _ = units[i][1][0]
            voter.doubts.append((li, wi, words[i], voted[i], other))
    for (word, places), v in zip(units, voted):
        if len(places) == 1:
            out[places[0][:2]] = v
        else:
            first = places[0][2]
            cut = max(1, min(len(v) - 1, round(first * len(v) / len(word))))
            out[places[0][:2]] = v[:cut]
            out[places[1][:2]] = v[cut:]
    return order, out


NUMBER_1750 = re.compile(r"^([0-9IlTtvłoO$§]{0,2}[0-9][0-9IlTtvłoO]{0,2})\s?(?=[A-Za-z]|$)"
                         r"|\s([0-9IlTtvłoO]{0,2}[0-9][0-9IlTtvłoO]{0,2})\s*$")


def numbered_1750(order):
    """{line index: True} for the 1738 lines whose line in 1750 (a reprint, line for line) carries a verse number:
    1750's margins survive where 1738's scan cuts them off."""
    from pipeline import align
    raw = [l for l in (paths.SOURCES / "archive" / "1750" / "text.txt").read_text(encoding="utf-8").splitlines()
           if l.strip()]

    def key(s):
        return " ".join(align.fold(w, fs=True) for w in re.findall(r"[^\W\d_]{2,}", s))
    keys = [key(l) for l in raw]
    body = [(li, key(l.text)) for li, l in enumerate(order) if l.kind == "body"]
    if not body:
        return {}
    # Where the leaves begin in 1750: the first of the opening lines found there (two of its long words in one
    # 1750 line, the lines alike), less its place among the lines.
    at = 0
    for count, (_, anchor) in enumerate(body[:30]):
        words = [w for w in anchor.split() if len(w) >= 5]
        if len(words) < 3:
            continue
        found = [(difflib.SequenceMatcher(None, anchor, k).ratio(), n) for n, k in enumerate(keys)
                 if sum(w in k.split() for w in words) >= 2]
        found = [f for f in found if f[0] >= 0.6]
        if found:
            at = max(found)[1] - count
            break
    out, p = {}, max(0, at - 3)
    for li, k in body:
        scored = [(difflib.SequenceMatcher(None, k, keys[n]).ratio(), n) for n in range(p, min(len(keys), p + 14))]
        if not scored:
            break
        r, n = max(scored)
        if r >= 0.55:
            if NUMBER_1750.search(raw[n].strip()):
                out[li] = True
            p = n + 1
    return out


def place_verses(order, extra=None):
    """{line index: word index}: lines where a verse begins (a number in 1738's margin, or in 1750's), and the word
    it begins with: the line's start when the line before ends a sentence; else after the line's last sentence stop
    (not at its end); else after its last comma; else its start."""
    extra = extra or {}
    starts = {}
    for li, line in enumerate(order):
        if line.kind != "body" or not line.words:
            continue
        if not (any(ch.isdigit() for ch in line.margin) or extra.get(li)):
            continue
        texts = [t for t, _ in line.words]
        prev = next((order[k] for k in range(li - 1, -1, -1) if order[k].kind == "body" and order[k].words), None)
        prev_ends = prev is None or bool(STOP.search(prev.words[-1][0])) or order[li - 1].kind == "chapter"
        stops = [k + 1 for k, t in enumerate(texts[:-1]) if STOP.search(t)]
        commas = [k + 1 for k, t in enumerate(texts[:-1]) if t.endswith(",")]
        starts[li] = 0 if prev_ends else (stops[-1] if stops else commas[-1] if commas else 0)
    return starts


def lines_tsv(order, out, starts):
    """The lines file: header `leaf column line text`; `\\c N` rows for chapters; verse starts as `#N` before the
    word, numbered in sequence within each chapter (the margin digits are unreliable); a chapter's first word #1."""
    rows = ["leaf\tcolumn\tline\ttext"]
    chapter, verse, fresh = 0, 0, False
    for li, line in enumerate(order):
        if line.kind == "chapter":
            chapter = chapter_number(line, chapter)
            verse, fresh = 0, True
            rows.append(f"{line.leaf}\t{line.column}\t{line.number}\t\\c {chapter}")
            continue
        parts = []
        for wi, (text, _) in enumerate(line.words):
            if (fresh and wi == 0) or starts.get(li) == wi:
                verse += 1
                parts.append(f"#{verse}")
                fresh = False
            v = out.get((li, wi))
            if v is not None:
                lead = re.match(r"^\W*", text).group()
                tail = re.search(r"\W*$", text).group()
                parts.append(lead + v + tail)
            else:
                parts.append(text)
        rows.append(f"{line.leaf}\t{line.column}\t{line.number}\t{' '.join(parts)}")
    return "\n".join(rows) + "\n"


# ---------------------------------------------------------------- read lines → USFM

def read_lines(path):
    """[(leaf, column, line, text)] of a lines file."""
    out = []
    for row in path.read_text(encoding="utf-8").splitlines()[1:]:
        if row.strip():
            leaf, column, line, text = row.split("\t")
            out.append((int(leaf), int(column), int(line), text))
    return out


def verses_of(lines):
    """{(chapter, verse): text as printed (hyphens joined)} from read lines; also the leaf of each verse's start."""
    out, leaf_of = collections.OrderedDict(), {}
    chapter, verse, buf = None, None, ""

    def flush():
        if chapter is not None and verse is not None:
            out[(chapter, verse)] = re.sub(r"\s+", " ", buf).strip()

    for leaf, _, _, text in lines:
        if text.strip().startswith("%"):          # a catchword, footnote or margin read as a line: not the text
            continue
        if m := re.match(r"\\c (\d+)$", text.strip()):
            flush()
            chapter, verse, buf = int(m.group(1)), None, ""
            continue
        text = text.strip()
        for piece in re.split(r"(#\d+)", text):
            if m := re.match(r"#(\d+)$", piece):
                flush()
                verse, buf = int(m.group(1)), ""
                leaf_of[(chapter, verse)] = leaf
            else:
                buf += piece
        # a line ending in a hyphen joins the next line's first word
        if re.search(r"\w-$", buf):
            buf = buf[:-1]
        else:
            buf += " "
    flush()
    return out, leaf_of


def modern(word, forms):
    """A printed word in Wikisource's conventions: the spelling Wikisource or the settled text gives the same folded
    word (u/v, i/j; ae and oe for æ, œ), else by rule (u for v before a consonant at a word's start, then
    `macronize.jv`: consonantal i and u as j and v at a word's start and between vowels). A word in capitals (1738's
    Exod 34:6–7, IOVA DEVS MISERICORS) is set the same way and kept in capitals (Wikisource's SANCTUS, JESUS)."""
    from pipeline import align, macronize
    caps = len(word) > 1 and word.isupper()
    plain = (word.replace("æ", "ae").replace("Æ", "AE" if caps else "Ae").replace("œ", "oe")
             .replace("Œ", "OE" if caps else "Oe"))
    if caps:
        return modern(plain.lower(), forms).upper()
    found = forms.get(align.fold(plain))
    if found:
        # a book that keeps u and i (Malachi's Iacobeis; ouatu): j/v as everywhere, coeō's i kept (coierunt)
        found = re.sub(r"^([Cc]o)j(?=[ei])", r"\1i", macronize.jv(found))
        return (found[0].upper() + found[1:]) if plain[:1].isupper() else found
    # the enclitic -ue (Lev 11:3 ouemue, 27:33 malumue): a known word, or an accusative or -tor imperative, + ve
    stem = plain[:-2]
    if re.search(r"[^qg]ue$", plain) and (align.fold(stem) in forms or re.search(r"(m|tor)$", stem)):
        return modern(stem, forms) + "ve"
    w = re.sub(r"^([Vv])(?=[^aeiouAEIOU]|$)", lambda m: "U" if m.group(1) == "V" else "u", plain)
    w = re.sub(r"(?<=.)v", "u", w)
    # u after a prefix or in a stem where it is always a consonant: ob|uelauit, sub|uehebat, super|uacaneas,
    # con|seruanto, ab|soluere, ceruix, paruus (the forms Wikisource lacks; jv reaches only u between vowels)
    w = re.sub(r"^(ab|ad|animad|circum|con|in|ob|per|sub|super|trans)u(?=[aeiou])", r"\1v", w, flags=re.I)
    # (not pāreō's perfect: Lev 26:15 paru|eritis, paruit)
    w = re.sub(r"(ser|cer|ner|par|sal|sil|sol|cal|ful)u(?=[aeiou])(?!(?<=paru)(?:er|it\b|isse|imus|istis))", r"\1v",
               w, flags=re.I)
    w = re.sub(r"^([iI])uu(?=[aeiou])", r"\1uv", w)              # iuuatote (Lev 25:35): ju|v, not jvv
    # eō's perfect and its compounds: iuissent (Num 14:7), co|iuistis (16:11), ex|iuit: i|v, not jv
    w = re.sub(r"^((?:ab|ad|co|ex|in|ob|per|prae|red|sub|trans)?[iI])u(?=[ie])", r"\1v", w)
    w = re.sub(r"(?<=[vV])j", "i", macronize.jv(w))          # sæuies: jv reads the i after u as between vowels
    w = re.sub(r"^([Cc]o)j(?=[ei])", r"\1i", w)                   # coeō's coierit (Lev 20:12), not cojerit
    return re.sub(r"^([Ss]ub)iug", r"\1jug", w)                    # subiugiis (Lev 26:13): sub|jug-


def wikisource_forms():
    """{folded word: Wikisource's or the settled text's spelling (unmacronized, ae and oe)}, the commonest."""
    from pipeline import align, books, gold, rules, tsv
    counts = collections.defaultdict(collections.Counter)
    for book in books.BOOKS:
        path = paths.WITNESSES / "wikisource" / f"{book.osis}.tsv"
        if path.exists():
            for row in tsv.read(path):
                for w, is_word in align.words(align.clean(row["text"])):
                    if is_word:
                        counts[align.fold(w)][rules.unmacron(w).lower()] += 1     # a stray macron (rumperētur)
        for row in gold.load(book.osis).values():
            for w, is_word in align.words(row["text"]):
                if is_word:
                    w = rules.unmacron(w).lower().replace("æ", "ae").replace("œ", "oe")
                    counts[align.fold(w)][w] += 1
    return {k: c.most_common(1)[0][0] for k, c in counts.items()}


def modern_text(text, forms):
    """A verse as printed, in Wikisource's conventions: & and q; written out, spaces before punctuation (the OCR's)
    dropped and one after it, each word by `modern`."""
    text = re.sub(r"(?<=\w)q;", "que", text.replace("&", "et"))
    text = re.sub(r"\s+([,.;:?!)])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"([,;:?!])(?=[^\W\d_])", r"\1 ", text)
    out = []
    for t in re.findall(r"[^\W\d_]+|[^\w\s]+|\d+|\s+", text):
        out.append(modern(t, forms) if t[0].isalpha() else t)
    return re.sub(r"\s+", " ", "".join(out)).strip()


def drop_capital(text):
    """A chapter's first word as 1738 prints it beside a drop capital (INterea, HAec, EX) in lower case after its
    first letter."""
    return re.sub(r"^([A-Z])([A-Z]+)(?=[a-z]|\b)", lambda m: m.group(1) + m.group(2).lower(), text)


def to_usfm(lines, header, forms, bsb, osis):
    r"""The draft from read lines: the header lines, then each chapter with its verses in Wikisource's conventions
    (`modern_text`; hyphens joined by `verses_of`), a \p at each chapter's start and wherever the BSB opens a
    paragraph, as `collate.draft_usfm` sets a Wikisource draft."""
    from pipeline import structure
    verses, _ = verses_of(lines)
    out, chapter = list(header) + [""], None
    for (c, v), text in verses.items():
        if c != chapter:
            out += ([""] if chapter else []) + [rf"\c {c}"]
            chapter = c
        if v == 1:
            text = drop_capital(text)
        if v == 1 or structure.starts(bsb.get(f"{osis}.{c}.{v}", {}).get("marks", "")):
            out.append(r"\p")
        out.append(rf"\v {v} {modern_text(text, forms)}")
    return "\n".join(out) + "\n"


def draft_from_ocr(osis, chapters):
    """(USFM, source): `pipeline draft BOOK CH --from-ocr`, the draft of the read lines in
    data/witnesses/read-1738/<osis><first>-<last>.tsv, with the header of the book's settled USFM."""
    from pipeline import books, latex, structure
    book = books.select([osis])[0]
    span = f"{chapters.start}-{chapters.stop - 1}" if len(chapters) > 1 else str(chapters.start)
    source = paths.WITNESSES / "read-1738" / f"{osis}{span}.tsv"
    if not source.exists():
        raise SystemExit(f"no {source.relative_to(paths.ROOT).as_posix()}: the lines are read on the page first")
    master = latex.usfm_path(book)
    heads = (r"\id", r"\usfm", r"\ide", r"\h", r"\toc", r"\mt")
    header = ([line for line in master.read_text(encoding="utf-8").splitlines() if line.startswith(heads)]
              if master.exists() else books.usfm_header(book))
    keep, on = [], False
    for row in read_lines(source):
        if m := re.match(r"\\c (\d+)$", row[3].strip()):
            on = int(m.group(1)) in chapters
        if on:
            keep.append(row)
    return to_usfm(keep, header, wikisource_forms(), structure.bsb_rows(osis), osis), source


def wikisource_witness(osis, chapters):
    """An align.Witness of Wikisource's text of these chapters (chapter summaries left out, as 1738's lines leave
    them out), or None where Wikisource has fewer than ten verses of them."""
    from pipeline import align, tsv
    path = paths.WITNESSES / "wikisource" / f"{osis}.tsv"
    if not path.exists():
        return None
    rows = [r for r in tsv.read(path)
            if int(r["id"].split(".")[1]) in chapters and int(r["id"].split(".")[2]) > 0]
    if len(rows) < 10:
        return None
    w = align.Witness("\n".join(r["text"] for r in rows))
    w.name = "Wikisource"
    return w


def make_lines(osis, leaves, chapters, vote=True):
    """(text, how, doubts): the lines file's text for these chapters of a book, from 1738's leaves, voted with 1750,
    Wikisource and 1726 (where each has the book); `how` counts where each voted word came from, and `doubts` lists
    the places the others agree against it, as rows (leaf, column, line, OCR word, voted, the others' word)."""
    from pipeline import align, books
    voter, others = None, ()
    if vote:
        settled, known = known_forms()
        order, out0 = build("1738", leaves)
        extra = set()
        for t in out0.values():
            for c in candidates(t)[:12]:
                f = align.fold(c)
                if f not in known and re.fullmatch("[a-z]+", f):
                    extra.add(f)
        known |= looked_up(extra)
        voter = Voter(settled, known)
        book = books.select([osis])[0]
        others = [align.Witness((paths.SOURCES / "archive" / "1750" / "text.txt").read_text(encoding="utf-8"))]
        others[0].name = "1750"
        if (ws := wikisource_witness(osis, chapters)) is not None:
            others.append(ws)
        old = paths.ROOT / "TXT" / "1 - OCR" / "Vetus Fœdus" / f"{book.slug}.txt"
        if old.exists():
            others.append(align.Witness(old.read_text(encoding="utf-8")))
            others[-1].name = "1726"
    order, out = build("1738", leaves, voter, others)
    text = lines_tsv(order, out, place_verses(order, numbered_1750(order)))
    rows = text.splitlines()
    keep, on, ended = [rows[0]], False, False
    for row in rows[1:]:
        if m := re.search(r"\\c (\d+)$", row):
            # a chapter 1 after the book's rows: the next book has begun (1738 leaf 357, 2 Samuel under 1 Samuel 31)
            ended = ended or (int(m.group(1)) == 1 and len(keep) > 1)
            on = int(m.group(1)) in chapters and not ended
        if on:
            keep.append(row)
    kept = {tuple(r.split("\t")[:3]) for r in keep[1:]}
    found = []
    for li, wi, ocr, voted, other in (voter.doubts if voter else []):
        line = order[li]
        place = (str(line.leaf), str(line.column), str(line.number))
        if place in kept:
            found.append((*place, ocr, voted, other))
    return "\n".join(keep) + "\n", (voter.how if voter else None), found


def heads(leaves):
    """[(leaf, running head, book title, [chapter numbers])] of 1738's leaves, for finding a book's leaves."""
    out = []
    for leaf in leaves:
        lines = page_lines("1738", leaf)
        out.append((leaf, " ".join(l.text for l in lines if l.kind == "head"),
                    " ".join(l.text for l in lines if l.kind == "title"),
                    [l.chapter for l in lines if l.kind == "chapter"]))
    return out


def reading_sheets(lines_path, folder, per=14, key="1738"):
    """Sheets for reading a lines file on the page: each printed line's crop under the draft's text of that line
    (archive.sheet), `per` lines a sheet, in the file's order. Returns [(sheet path, [row numbers])]."""
    from pipeline import archive
    rows = read_lines(lines_path)
    body = [(n, r) for n, r in enumerate(rows, 2) if not r[3].strip().startswith("\\c ")]
    out = []
    for k in range(0, len(body), per):
        chunk = body[k:k + per]
        items = []
        for n, (leaf, column, line, text) in chunk:
            try:
                box = archive.line_box(key, leaf, line, pad=(40, 6))
            except ValueError:
                continue
            # the column's whole width, margins included, so the margin's verse number is on the crop
            _, words, (width, _) = archive.pages(key)[leaf]
            side = [w for w in words if (w.box[0] + w.box[2]) / 2 < width / 2] if column == 0 else \
                   [w for w in words if (w.box[0] + w.box[2]) / 2 >= width / 2]
            if side:
                xs0 = sorted(w.box[0] for w in side)
                xs1 = sorted(w.box[2] for w in side)
                box = (max(0, xs0[len(xs0) // 50] - 30), box[1], min(width, xs1[-len(xs1) // 50 - 1] + 50), box[3])
            items.append((f"{n}: {text}", leaf, box))
        path = folder / f"{lines_path.stem}-{k // per + 1:03d}.jpg"
        archive.sheet(key, items, path, 900)
        out.append((path, [n for n, _ in chunk]))
    return out
