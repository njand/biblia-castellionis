"""Stage 1: aligning OCR witnesses to verse ids, word by word, against a versified base text.

A witness is an OCR text with no reliable verse division: an archive.org scan (sources/archive/<key>/text.txt,
a whole Testament or Bible) or the 1726–27 Google Books OCR in TXT/1. It is cleaned (`clean`), each chapter of
the base is located in it by shared word triples, and the words in that window are aligned to the base's words.
Every witness word then carries the base verse id it falls in, which gives one row per verse.

The base is the gold text for settled chapters (to measure the witnesses) and Wikisource elsewhere.

Folding for alignment: lower case, no accents or macrons, æ/œ → ae/oe, j → i, v → u, ſ → s. The OCRs also
confuse long s with f (TXT/1 writes every ſ as f), so the f/s-blind fold maps f → s as well; scores are given
both ways."""

import collections
import difflib
import re
import statistics
import unicodedata
from dataclasses import dataclass, field

from pipeline import tsv

TOKEN = re.compile(r"[^\W\d_]+|\d+|[^\w\s]")
TILDE = {"ã": "a", "ẽ": "e", "ĩ": "i", "õ": "o", "ũ": "u"}


def clean(text):
    """OCR text → plain text: hyphenated line ends joined, ſ → s, & → et, q; → que, ã → am (ãn mid-word)."""
    text = unicodedata.normalize("NFC", text)
    text = re.sub(r"(\w)[-¬]\s*\n\s*(\w)", r"\1\2", text)          # conſi-\nderet → conſideret
    text = text.replace("ſ", "s").replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ß", "ss")
    text = re.sub(r"(?<!\w)(&|8c)(?!\w)", "et", text)
    text = re.sub(r"(\w)q ?;", r"\1que", text)                      # the hOCR may read atq; as "atq ;"
    text = re.sub(r"([ãẽĩõũ])(?=\W|$)", lambda m: TILDE[m.group(1)] + "m", text)
    text = re.sub(r"[ãẽĩõũ]", lambda m: TILDE[m.group()] + "n", text)
    return text


def fold(word, fs=False):
    """The comparison form of a word; fs=True also maps f → s (long-s confusion)."""
    decomposed = unicodedata.normalize("NFD", word.lower().replace("æ", "ae").replace("œ", "oe"))
    word = "".join(c for c in decomposed if unicodedata.category(c) != "Mn").replace("j", "i").replace("v", "u")
    return word.replace("f", "s") if fs else word


def words(text):
    """[(token, is_word)] of a cleaned text, in order (numbers and punctuation are not words)."""
    return [(t, t[0].isalpha()) for t in TOKEN.findall(text)]


# Castellio sets words that follow the Latin (Vulgate) between an italic L. and G. (docs/editions.md): 1573 Luke
# 11:7 "& tibi dare L. si ille pulsare perseuerauerit G.". The OCRs read the marks as L./I./J. and G./C.
L_MARKS, G_MARKS, MARK_SPAN = {"L", "I", "J"}, {"G", "C"}, 40


def lg_marks(tokens):
    """{index of an L mark: index of its G mark} in [(token, is_word)]: an L-like capital followed by . or ,
    and, within MARK_SPAN tokens, a G-like capital followed by . or , (or a bare G), with words between."""
    pairs, i = {}, 0
    punct = lambda k: k < len(tokens) and tokens[k][0] in (".", ",")
    while i < len(tokens):
        if tokens[i][0] in L_MARKS and punct(i + 1):
            for k in range(i + 2, min(len(tokens), i + MARK_SPAN)):
                if tokens[k][0] in L_MARKS and punct(k + 1):
                    break
                if tokens[k][0] in G_MARKS and (punct(k + 1) or tokens[k][0] == "G"):
                    if any(tokens[j][0][:1].isalpha() for j in range(i + 2, k)):
                        pairs[i] = k
                        i = k
                    break
        i += 1
    return pairs


def strip_marks(pieces):
    """(text, [marked words]) from a verse row's tokens: the L./G. marks and their points removed, the words
    between them kept."""
    pairs = lg_marks([(t, t[:1].isalpha()) for t in pieces])
    drop, marked = set(), []
    for i, k in pairs.items():
        drop.update({i, i + 1, k})
        if k + 1 < len(pieces) and pieces[k + 1] in (".", ","):
            drop.add(k + 1)
        marked.append(" ".join(t for t in pieces[i + 2:k] if t[:1].isalpha()))
    kept = [t for j, t in enumerate(pieces) if j not in drop]
    return re.sub(r"\s+([,.;:?!)])", r"\1", " ".join(kept)), marked


@dataclass
class Chapter:
    """The alignment of one base chapter: for each base word, the witness word (or None) and where it is."""
    chapter: str
    found: bool
    matches: list = field(default_factory=list)      # [(base verse id, base word, witness word or None)]
    verses: dict = field(default_factory=dict)       # {verse id: witness text}
    numbers: list = field(default_factory=list)      # [(number printed, base verse id it introduces)]
    joined: set = field(default_factory=set)         # indices of base words the OCR ran together or split
    marked: dict = field(default_factory=dict)       # {verse id: [words set between L. and G.]}
    pages: dict = field(default_factory=dict)        # {verse id: canvas or page label}, where the witness has them
    spans: dict = field(default_factory=dict)        # {verse id: (first, last) token indices of its row}
    at: dict = field(default_factory=dict)           # {base word index: (first, last) witness token indices}


class Witness:
    """A cleaned OCR text, indexed by folded word triples for locating chapters.

    The L./G. marks are not words: they take no part in the alignment. anchors=True (an edition that prints
    every verse number and reads cleanly: 1573) lets a verse row run from its printed number to the next one,
    so words the base lacks at a verse's edges are kept."""

    def __init__(self, text, anchors=False):
        self.anchors = anchors
        self.tokens = words(clean(text))
        self.lg = lg_marks(self.tokens)                  # {L mark index: G mark index}
        for i, k in self.lg.items():
            self.tokens[i] = (self.tokens[i][0], False)
            self.tokens[k] = (self.tokens[k][0], False)
        self.word_at = [i for i, (_, is_word) in enumerate(self.tokens) if is_word]
        self.folded = [fold(self.tokens[i][0], fs=True) for i in self.word_at]
        self.index = collections.defaultdict(list)
        for n in range(len(self.folded) - 2):
            self.index[tuple(self.folded[n:n + 3])].append(n)

    def locate(self, base_words, margin=80):
        """(start, end) in witness word positions of the window holding these base words, or None."""
        folded = [fold(w, fs=True) for w in base_words]
        offsets = []
        for n in range(len(folded) - 2):
            hits = self.index.get(tuple(folded[n:n + 3]), [])
            if 0 < len(hits) <= 3:                       # common triples point everywhere; skip them
                offsets.extend(hit - n for hit in hits)
        if len(offsets) < max(3, len(folded) // 50):
            return None
        # The densest cluster of offsets, then its median: robust to stray hits elsewhere in the book.
        offsets.sort()
        width = max(40, len(folded) // 4)
        best = max(range(len(offsets)), key=lambda i: sum(1 for o in offsets[i:i + 400] if o - offsets[i] <= width))
        cluster = [o for o in offsets[best:] if o - offsets[best] <= width]
        start = int(statistics.median(cluster))
        return max(0, start - margin), min(len(self.folded), start + len(folded) + margin)


def align_chapter(witness, base_rows, chapter):
    """Align one base chapter ([(verse id, text)] in order) with the witness."""
    base = [(vid, w) for vid, text in base_rows for w, is_word in words(text) if is_word]
    window = witness.locate([w for _, w in base])
    result = Chapter(chapter, window is not None)
    if window is None:
        result.matches = [(vid, w, None) for vid, w in base]
        return result
    start, end = window
    a = [fold(w, fs=True) for _, w in base]
    b = witness.folded[start:end]
    owner = {}                                           # witness word position → base verse id
    paired = {}                                          # base word index → witness word text
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal" or (tag == "replace" and i2 - i1 == j2 - j1):
            for k in range(i2 - i1):
                # A short substitution is a misreading or a variant; in a long one (OCR columns read out of
                # order) only words that still look alike are paired.
                if tag == "replace" and i2 - i1 > 3 and \
                        difflib.SequenceMatcher(None, a[i1 + k], b[j1 + k]).ratio() < 0.5:
                    continue
                paired[i1 + k] = witness.tokens[witness.word_at[start + j1 + k]][0]
                owner[start + j1 + k] = base[i1 + k][0]
                position = witness.word_at[start + j1 + k]
                result.at[i1 + k] = (position, position)
        elif tag == "replace" and "".join(a[i1:i2]) == "".join(b[j1:j2]):
            joined = " ".join(witness.tokens[witness.word_at[start + j]][0] for j in range(j1, j2))
            for k in range(i1, i2):                      # words run together or split in the OCR: same letters
                paired[k] = joined if k == i1 else ""
                result.joined.add(k)
                result.at[k] = (witness.word_at[start + j1], witness.word_at[start + j2 - 1])
            for j in range(j1, j2):
                owner[start + j] = base[i1][0]
    result.matches = [(vid, w, paired.get(i)) for i, (vid, w) in enumerate(base)]
    # Verse rows: every witness token from the first to the last word paired with the verse (so numbers,
    # punctuation and anything misread between them come along); a printed number just before is noted.
    spans = collections.defaultdict(list)
    for position, vid in owner.items():
        spans[vid].append(witness.word_at[position])
    owned = {witness.word_at[position] for position in owner}
    verse_words = collections.Counter(vid for vid, _ in base)
    for vid, positions in spans.items():
        # The densest run of the verse's words: a stray match far away (a common word in a column read out of
        # order) must not stretch the row over other verses.
        positions.sort()
        gap = 2 * verse_words[vid] + 10
        runs, run = [], [positions[0]]
        for position in positions[1:]:
            if position - run[-1] > gap:
                runs.append(run)
                run = []
            run.append(position)
        runs.append(run)
        best = max(runs, key=len)
        if len(best) < max(2, 0.3 * verse_words[vid]):
            continue                                     # a few common words matched by chance: no row
        first, last = _edges(witness, best[0], best[-1], vid, owned)
        result.spans[vid] = (first, last)
        pieces = [token for token, _ in witness.tokens[first:last + 1]]
        result.verses[vid], marked = strip_marks(pieces)
        if marked:
            result.marked[vid] = marked
        if getattr(witness, "canvas_at", None):
            pages = sorted({witness.canvas_at[min(first, len(witness.canvas_at) - 1)],
                            witness.canvas_at[min(last, len(witness.canvas_at) - 1)]})
            result.pages[vid] = "–".join(map(str, pages))
        before = [token for token, _ in witness.tokens[max(0, first - 3):first] if token.isdecimal() and token.isascii()]
        if before:
            result.numbers.append((int(before[-1]), vid))
    return result


def _edges(witness, first, last, vid, owned):
    """Widen a verse row (token indices) to words of the verse that matched no base word: an L. … G. passage
    just after it and, in an anchored witness, everything from its printed number to the next verse's."""
    tokens = witness.tokens
    verse = tsv.parse_id(vid)[2]
    if witness.anchors:
        for k in range(first - 1, max(-1, first - MARK_SPAN), -1):
            if tokens[k][0].isdigit() or k in owned:
                if tokens[k][0] == str(verse):
                    first = k + 1
                break
        for k in range(last + 1, min(len(tokens), last + MARK_SPAN)):
            if tokens[k][0].isdigit() or k in owned:
                if tokens[k][0] == str(verse + 1):
                    last = k - 1
                    while last > first and not tokens[last][1] and tokens[last][0] not in (".", ",", ";", ":", "?", "!"):
                        last -= 1
                break
    for i, k in getattr(witness, "lg", {}).items():
        # An L. … G. passage that starts inside the row (or just after it) and closes after it: the base lacks
        # its last words, or the OCR misread them.
        if first <= i <= last + 3 and k > last and not any(j in owned for j in range(last + 1, k)):
            last = k
    while last + 1 < len(tokens) and not tokens[last + 1][1] and not tokens[last + 1][0].isdigit() \
            and tokens[last + 1][0] not in L_MARKS | G_MARKS:
        last += 1                                        # the verse's closing punctuation
    return first, last


SPELLINGS = [("quum", "cum"), ("eis", "iis"), ("eisque", "iisque"), ("ioann", "iohann"), ("oe", "ae")]


def reading(word):
    """The f/s-blind fold with the editions' spelling habits also set aside (quum/cum, eīs/iīs, coelum/cælum,
    Joannes/Johannēs, h-, -mpt-, double letters): what is left is a misreading or a different word."""
    from pipeline import rules
    w = fold(word, fs=True)
    for old, new in SPELLINGS:
        w = w.replace(old, new) if old in ("oe", "ioann") else (new if w == old else w)
    return rules.variant_key(w)


def score(chapters):
    """Counts over aligned chapters: base words, words found, and agreements three ways (exact, f/s-blind, and
    reading: spelling habits aside)."""
    total = found = exact = fs = read = 0
    for chapter in chapters:
        for index, (_, base_word, witness_word) in enumerate(chapter.matches):
            total += 1
            if witness_word is None:
                continue
            found += 1
            if index in chapter.joined or fold(witness_word) == fold(base_word):
                exact, fs, read = exact + 1, fs + 1, read + 1
            elif fold(witness_word, fs=True) == fold(base_word, fs=True):
                fs, read = fs + 1, read + 1
            elif reading(witness_word) == reading(base_word):
                read += 1
    return {"words": total, "found": found, "exact": exact, "fs": fs, "reading": read}


def number_agreement(chapters):
    """(printed verse numbers seen at a verse start, how many equal that verse's number in the base)."""
    seen = agree = 0
    for chapter in chapters:
        for number, vid in chapter.numbers:
            seen += 1
            agree += number == tsv.parse_id(vid)[2]
    return seen, agree


# ---------------------------------------------------------------- the witnesses and their measurement

@dataclass(frozen=True)
class Source:
    key: str            # data/witnesses/<key>/
    label: str
    files: tuple        # archive keys, or "txt1"


SOURCES = [
    Source("ocr-1681", "1681 NT (KB, ABBYY)", ("1681",)),
    Source("ocr-1715", "1715 NT (Tesseract)", ("1715",)),
    Source("ocr-1726", "1726–27 Bible (Google Books OCR, TXT/1)", ("txt1",)),
    Source("ocr-1738", "1738 OT vol. 1 (ABBYY)", ("1738",)),
    Source("ocr-1747", "1747 NT (Tesseract)", ("1747",)),
    Source("ocr-1750", "1750 Bible (Tesseract)", ("1750",)),
    Source("ocr-1758", "1758 NT, 2 vols (Tesseract, long s)", ("1758-1", "1758-2")),
    Source("ocr-1573", "1573 Bible, NT (Basel, Perna; MDZ hOCR): the NT base", ("mdz-1573",)),
]
BY_SOURCE = {source.key: source for source in SOURCES}


def texts(source, book, paths):
    """The raw texts that may hold this book for a source (each file is one Witness)."""
    out = []
    for name in source.files:
        if name == "mdz-1573":
            if book.testament == "novum" and (paths.SOURCES / "mdz-1573").exists():
                out.append(name)                         # pages, read by pipeline.mdz
            continue
        if name == "txt1":
            folder = {"vetus": "Vetus Fœdus", "novum": "Novum Fœdus"}[book.testament]
            path = paths.TXT / "1 - OCR" / folder / f"{book.slug}.txt"
        else:
            path = paths.SOURCES / "archive" / name / "text.txt"
        if path.exists():
            out.append(path)
    return out


def align_book(witnesses, base_rows):
    """[Chapter] for a book's base rows ([(verse id, text)]), taking for each chapter the witness file that
    holds it best (the 1758 New Testament is in two volumes)."""
    chapters = collections.defaultdict(list)
    for vid, text in base_rows:
        chapters[tsv.parse_id(vid)[1]].append((vid, text))
    out = []
    for number in sorted(chapters):
        tries = [align_chapter(w, chapters[number], number) for w in witnesses]
        out.append(max(tries, key=lambda c: sum(1 for m in c.matches if m[2] is not None)))
    return out


def disagreements(chapters, limit=12):
    """The commonest (base word, witness word) pairs that disagree even in reading (spelling habits aside)."""
    pairs = collections.Counter()
    for chapter in chapters:
        for index, (_, base_word, witness_word) in enumerate(chapter.matches):
            if witness_word and index not in chapter.joined and reading(witness_word) != reading(base_word):
                pairs[(fold(base_word), fold(witness_word))] += 1
    return pairs.most_common(limit)


def write_report(summary, paths):
    """data/calibration/witnesses.tsv (one row per witness and book) and witnesses.md (the readable report)."""
    folder = paths.DATA / "calibration"
    tsv.write(folder / "witnesses.tsv",
              [(key, osis, s["words"], s["found"], s["exact"], s["fs"], s["reading"], agree, seen)
               for key, _, osis, s, seen, agree, _ in summary],
              header=("witness", "book", "gold_words", "found", "agree", "agree_fs", "agree_reading", "numbers_agree",
                      "numbers_seen"))
    totals = {}
    for key, label, osis, s, seen, agree, pairs in summary:
        t = totals.setdefault(key, {"label": label, "books": [], "words": 0, "found": 0, "exact": 0, "fs": 0, "reading": 0,
                                    "seen": 0, "agree": 0, "pairs": collections.Counter()})
        t["books"].append(osis)
        for name in ("words", "found", "exact", "fs", "reading"):
            t[name] += s[name]
        t["seen"] += seen
        t["agree"] += agree
        t["pairs"].update(dict(pairs))
    pct = lambda a, b: f"{100 * a / b:.1f}%" if b else "–"
    lines = ["# Witnesses against the gold text", "",
             "Each witness aligned word by word to the settled chapters (`python -m pipeline align`). **Found**: share "
             "of gold words the witness has at all (OCR that lost lines, columns read out of order, or the book "
             "missing). **Agree**: of the words found, how many read the same once case, accents and macrons, "
             "i/j, u/v and æ/ae are set aside. **f/s-blind**: the same, also counting f for long s as agreement. "
             "**Reading**: the editions' spelling habits also set aside (*quum/cum, eīs/iīs, coelum/cælum, "
             "Joannes/Johannēs*, h-, double letters): what is left is a misreading, or a different word in that "
             "edition (your text follows 1726–27). **Verse numbers**: printed numbers just before a verse that "
             "equal its number (numbers the OCR lost or misread don't count).", "",
             "The verse rows (`data/witnesses/ocr-*/<osis>.tsv`) flag a verse *missing* or *partial* (under 80% of "
             "its words found), give the words Castellio sets between an italic *L.* and *G.* (words from the Latin, "
             "`docs/editions.md`) as `L…G: …` with the marks removed from the text, and for 1573 the MDZ canvas. "
             "1573 prints every verse number, so its rows run from one printed number to the next.", "",
             "| Witness | Books | Gold words | Found | Agree | f/s-blind | Reading | Verse numbers |",
             "|---|---|---:|---:|---:|---:|---:|---:|"]
    for key, t in sorted(totals.items(), key=lambda kv: -kv[1]["reading"] / max(1, kv[1]["found"])):
        lines.append(f"| {t['label']} | {', '.join(t['books'])} | {t['words']:,} | {pct(t['found'], t['words'])} | "
                     f"{pct(t['exact'], t['found'])} | {pct(t['fs'], t['found'])} | {pct(t['reading'], t['found'])} | "
                     f"{t['agree']}/{t['seen']} |")
    lines += ["", "## By book", "", "| Witness | Book | Found | Agree | f/s-blind | Reading |",
              "|---|---|---:|---:|---:|---:|"]
    for key, label, osis, s, seen, agree, _ in summary:
        lines.append(f"| {key} | {osis} | {pct(s['found'], s['words'])} | {pct(s['exact'], s['found'])} | "
                     f"{pct(s['fs'], s['found'])} | {pct(s['reading'], s['found'])} |")
    lines += ["", "## Commonest disagreements in reading (gold → witness, folded)", ""]
    for key, t in totals.items():
        lines.append(f"- **{key}**: " + ", ".join(f"{a}→{b} {n}×" for (a, b), n in t["pairs"].most_common(10)))
    path = folder / "witnesses.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return path


def row_flags(chapter, vid, found, total):
    """The flags of a witness's verse row: missing/partial, the L. … G. words, the canvas."""
    flags = ["missing" if not found else "partial" if found < 0.8 * total else ""]
    flags += [f"L…G: {words}" for words in chapter.marked.get(vid, [])]
    if vid in chapter.pages:
        flags.append(f"canvas {chapter.pages[vid]}")
    return "; ".join(f for f in flags if f)
