"""Stage 2: collating a chapter's text against the printings, verse by verse (PLAN.md §4, stage 2).

The text collated is the drafted chapter (text/draft/<USFM>.usfm) or, where there is none, Wikisource. Every
witness is aligned to it (pipeline.align) and its verse row compared with the verse word by word on the
spelling-blind reading form (align.reading: case, macrons, i/j, u/v, æ, h-, double letters and the editions'
spelling habits aside), so what is left is a different word, a word more or a word less.

Each difference is a *place*: a span of the text's words (empty for a word the text lacks) and what each
witness reads there. A witness that reads the text's words there supports the text; a witness whose row does
not reach the place says nothing. Places are classified:

  correct     the base (1573 for the NT, 1738 for the OT) and at least one other witness agree against the text
  base-only   the base alone against the text (often its OCR; read on the page image)
  others      the base agrees with the text, or says nothing, while two or more others agree against it
  variant     1556 (the NT reference) differs from 1573 where 1573 is read
Noise (a reading of one OCR alone) is counted, not listed.

The witnesses: for the NT, 1573 (MDZ hOCR, the base), 1556 (e-rara OCR, the reference; reads poorly), 1758, 1681,
1715, 1747, 1750 (archive.org OCR), your 1726–27 text (TXT/2 - Post-Corrected where it has the book, Acts;
otherwise the uncorrected Google Books OCR of TXT/1) and Wikisource; for the OT, 1738 (archive.org OCR, the base; Wikisource
transcribes it), 1750, your 1726–27 text (TXT/3 - Edited, Google Books OCR corrected by hand) and Wikisource."""

import collections
import difflib
import re
from dataclasses import dataclass, field

from pipeline import align, books, gold, latex, mdz, paths, tsv

PRINTINGS = [("1556", None), ("1758", ("1758-1", "1758-2")), ("1681", ("1681",)), ("1715", ("1715",)),
             ("1747", ("1747",)), ("1750", ("1750",))]
OT_PRINTINGS = [("1738", ("1738",)), ("1750", ("1750",))]
# Witnesses whose text keeps f and long s apart: the 1573 hOCR (which reads ſ as ſ, though often as f too) and
# Wikisource. The archive.org OCRs and your 1726 text (TXT/1 and TXT/2 alike) write ſ as f.
FS_DISTINCT = ("1573", "ws")
FS_MARK = "f/s:"
EDGE = 6                                              # words on each side of a verse boundary, for `edges`
MACRON_TO_TILDE = {"ā": "ã", "ē": "ẽ", "ī": "ĩ", "ō": "õ", "ū": "ũ"}


def text_1556():
    """The e-rara 1556 OCR (sources/erara-1556/), e caudata as ae, nasal bars as tildes (align.clean expands)."""
    pages = sorted((paths.SOURCES / "erara-1556").glob("1028*.txt"), key=lambda p: int(p.stem))
    text = "\n".join(p.read_text(encoding="utf-8") for p in pages).replace("ę", "ae").replace("Ę", "Ae")
    return "".join(MACRON_TO_TILDE.get(c, c) for c in text)


def base_key(osis):
    """The base edition's witness key: 1573 for the New Testament, 1738 for the Old (decisions 1 and 24)."""
    return "1738" if books.select([osis])[0].testament == "vetus" else "1573"


def load_witnesses(osis):
    """{key: [align.Witness]}: for a New Testament book 1573, 1556, the archive.org printings and Wikisource; for an
    Old Testament book 1738, 1750, the 1726–27 text of TXT/3 and Wikisource."""
    book = books.select([osis])[0]
    if book.testament == "vetus":
        out = {}
        for key, files in OT_PRINTINGS:
            out[key] = [align.Witness((paths.SOURCES / "archive" / f / "text.txt").read_text(encoding="utf-8"))
                        for f in files if (paths.SOURCES / "archive" / f / "text.txt").exists()]
        txt = paths.TXT / "3 - Edited" / "Vetus Fœdus" / f"{book.slug}.txt"
        if txt.exists():
            out["1726"] = [align.Witness(txt.read_text(encoding="utf-8"))]
        out["ws"] = tsv.read(paths.WITNESSES / "wikisource" / f"{osis}.tsv")
        return out
    out = {"1573": [mdz.witness()]}
    for key, files in PRINTINGS:
        if files is None:
            out[key] = [align.Witness(text_1556())]
        else:
            out[key] = [align.Witness((paths.SOURCES / "archive" / f / "text.txt").read_text(encoding="utf-8"))
                        for f in files if (paths.SOURCES / "archive" / f / "text.txt").exists()]
    txt = paths.TXT / "2 - Post-Corrected" / "Novum Fœdus" / f"{book.slug}.txt"
    ocr = paths.TXT / "1 - OCR" / "Novum Fœdus" / f"{book.slug}.txt"
    if txt.exists():                                  # your 1726–27 text, OCR corrected by hand (Acts)
        out["1726"] = [align.Witness(txt.read_text(encoding="utf-8"))]
    elif ocr.exists():                                # its Google Books OCR, uncorrected (every ſ read as f)
        out["1726"] = [align.Witness(ocr.read_text(encoding="utf-8"))]
    path = paths.WITNESSES / "wikisource" / f"{osis}.tsv"
    rows = tsv.read(path)
    out["ws"] = rows                                  # versified already: rows, not an OCR to align
    return out


def base_rows(osis, chapters, source="draft"):
    """[(verse id, text)] of the text to collate: the draft USFM, the settled USFM, Wikisource, or a USFM file (a
    working copy)."""
    book = books.select([osis])[0]
    if not isinstance(source, str):
        rows = [(vid, text) for vid, text, *_ in gold.rows(source.read_text(encoding="utf-8"), osis)]
    elif source == "wikisource":
        rows = [(r["id"], r["text"]) for r in tsv.read(paths.WITNESSES / "wikisource" / f"{osis}.tsv")]
    else:
        path = latex.usfm_path(book, draft=source == "draft")
        rows = [(vid, text) for vid, text, *_ in gold.rows(path.read_text(encoding="utf-8"), osis)]
    return [(vid, text) for vid, text in rows if tsv.parse_id(vid)[1] in chapters and text]


def draft_usfm(osis, chapters):
    """Stage 1's working text as USFM: Wikisource's verses for these chapters, a paragraph (\\p) wherever the BSB
    opens one, the header of the book's settled USFM. No macrons, quotation marks or poetry yet (stages 3–5),
    and no chapter summaries (the USFM reader has no \\cd yet)."""
    from pipeline import structure
    book = books.select([osis])[0]
    master = latex.usfm_path(book)
    header = [line for line in master.read_text(encoding="utf-8").splitlines() if line.startswith(("\\id", "\\usfm",
              "\\ide", "\\h", "\\toc", "\\mt"))] if master.exists() else [f"\\id {book.usfm}", "\\usfm 3.0", "\\ide UTF-8"]
    bsb = structure.bsb_rows(osis)
    out, chapter = header + [""], None
    for row in tsv.read(paths.WITNESSES / "wikisource" / f"{osis}.tsv"):
        _, c, v = tsv.parse_id(row["id"])
        if c not in chapters or v == 0:
            continue
        if c != chapter:
            out += ([""] if chapter else []) + [f"\\c {c}"]
            chapter = c
        if v == 1 or structure.starts(bsb.get(row["id"], {}).get("marks", "")):
            out.append("\\p")
        out.append(f"\\v {v} {row['text']}")
    return "\n".join(out) + "\n"


@dataclass
class Place:
    vid: str
    start: int                  # index of the first text word in the verse
    end: int                    # one past the last (start == end: the text lacks words here)
    text: str                   # the text's words there
    readings: dict = field(default_factory=dict)      # {folded reading: {witness: as printed}}
    support: list = field(default_factory=list)       # witnesses that read the text here
    kind: str = ""
    sort: str = ""              # division, spelling, form or reading (sort_kind)
    base: str = "1573"          # the base edition's witness key (base_key)
    context: str = ""

    def against(self):
        """(folded reading, {witness: as printed}) with the most witnesses against the text."""
        return max(self.readings.items(), key=lambda kv: ((self.base in kv[1]) + len(kv[1]), len(kv[0])))


def keys(words):
    return [align.reading(w) for w in words]


def word_list(text):
    return [t for t, is_word in align.words(align.clean(text)) if is_word]


COVERED = 0.6                                         # the share of a verse's words the base witness must show


def uncovered(base, rows, threshold=COVERED):
    """[(verse id, share)] of the verses the base witness does not cover: no aligned text, or fewer than `threshold`
    of the verse's words found in it (folded, f/s blind). Its OCR may read a page's columns out of order (1573 at
    2 Cor 2:9–13), and a verse it does not cover is compared with nothing: read those by hand."""
    out = []
    for vid, text in base:
        want = [align.fold(w, fs=True) for w in word_list(text)]
        if not want:
            continue
        got = collections.Counter(align.fold(w, fs=True) for w in word_list(rows.get(vid) or ""))
        found = 0
        for w in want:
            if got[w]:
                got[w] -= 1
                found += 1
        share = found / len(want)
        if share < threshold:
            out.append((vid, round(share, 2)))
    return out


def fs_only(a, b):
    """True when two words differ only in f against s (long s, which the f/s-blind fold sets alike)."""
    fa, fb = align.fold(a), align.fold(b)
    return fa != fb and len(fa) == len(fb) and all(x == y or {x, y} == {"f", "s"} for x, y in zip(fa, fb))


def compare(vid, base_text, rows, fs_distinct=FS_DISTINCT):
    """[Place] for one verse. rows: {witness: its verse row text, or None where it has none}. Words read alike
    but for f against s (sani/fani) are a place too, in the witnesses whose text keeps the two apart
    (fs_distinct: the 1573 hOCR, which reads long s as ſ, and Wikisource)."""
    base = word_list(base_text)
    bk = keys(base)
    places = {}
    fs_agree = collections.defaultdict(list)          # base word index → fs_distinct witnesses reading it alike
    for witness, row in rows.items():
        if not row:
            continue
        wit = word_list(row)
        wk = keys(wit)
        matcher = difflib.SequenceMatcher(None, bk, wk, autojunk=False)
        blocks = matcher.get_matching_blocks()
        if sum(b.size for b in blocks) < 0.5 * len(bk):
            continue                                  # a row that is mostly something else: no evidence
        if witness in fs_distinct:
            for b in blocks:
                for k in range(b.size):
                    i, j = b.a + k, b.b + k
                    if fs_only(base[i], wit[j]):
                        place = places.setdefault((i, i + 1, "fs"), Place(vid, i, i + 1, base[i]))
                        place.readings.setdefault(FS_MARK + align.fold(wit[j]), {})[witness] = wit[j]
                    elif "f" in align.fold(base[i]) or "s" in align.fold(base[i]):
                        fs_agree[i].append(witness)
        covered = (blocks[0].a if blocks[0].size else len(bk), max((b.a + b.size for b in blocks if b.size), default=0))
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == "equal":
                continue
            # Words a row adds before its first or after its last match are the row's edges, not the verse's.
            if tag == "insert" and (i1 <= covered[0] and j1 == 0 or i1 >= covered[1] and j2 == len(wk)):
                continue
            if tag == "delete" and (i2 <= covered[0] or i1 >= covered[1]):
                continue
            place = places.setdefault((i1, i2), Place(vid, i1, i2, " ".join(base[i1:i2])))
            place.readings.setdefault(" ".join(wk[j1:j2]), {})[witness] = " ".join(wit[j1:j2])
    # Who reads the text at each place: a witness whose row has the text's words there, unchanged.
    for (i1, i2, *fs), place in places.items():
        place.context = (" ".join(base[max(0, i1 - 5):i1]) + " ⟦" + place.text + "⟧ " + " ".join(base[i2:i2 + 5])).strip()
        if fs:                                        # f/s: only the witnesses that keep them apart can say
            place.support = list(fs_agree[i1])
            continue
        for witness, row in rows.items():
            if not row or any(witness in r for r in place.readings.values()):
                continue
            blocks = [b for b in difflib.SequenceMatcher(None, bk, keys(word_list(row)), autojunk=False)
                      .get_matching_blocks() if b.size]
            if i1 == i2:                              # nothing inserted between two words read in one run
                ok = any(b.a < i1 < b.a + b.size or (i1 == len(bk) and b.a + b.size == i1) for b in blocks)
            else:
                ok = any(b.a <= i1 and i2 <= b.a + b.size for b in blocks)
            if ok:
                place.support.append(witness)
    return sorted(places.values(), key=lambda p: (p.start, p.end))


def edges(a, b, windows):
    """[Place] for the words added or lost at a verse boundary, which `compare` cannot see (a row is cut where the
    witness's words stop matching, so a word only one side has at a verse's start or end falls between rows).

    a, b: (verse id, text) of the verses before and after the boundary; either may be None at a chapter's start or
    end. windows: {witness: (its row for a, the words it prints between the two rows, its row for b)}, a row None
    where it has none. The last EDGE words of a and the first of b are compared with the witness's words there;
    only differences that touch the boundary are kept (an addition or loss at it, or a change running over it). At
    a chapter's end only words the witness lacks count. A chapter's opening is not compared: the printings set its
    first letters as a decorated initial the OCRs misread or drop (1573 *Væ nam* for *Quænam*), and what comes
    before verse 1 is a heading or a summary; a word added or lost there is still a blind spot."""
    if a is None:
        return []
    ta = word_list(a[1])[-EDGE:] if a else []
    tb = word_list(b[1])[:EDGE] if b else []
    na, cut = (len(word_list(a[1])) if a else 0), len(ta)
    text = ta + tb
    tk = keys(text)
    places, readers = {}, []
    for witness, (row_a, gap, row_b) in windows.items():
        if (a and not row_a) or (b and not row_b):
            continue
        wa = word_list(row_a)[-(EDGE + 2):] if a else []
        wb = word_list(row_b)[:EDGE + 2] if b else []
        gap_words = [w for w in word_list(gap or "") if not (len(w) == 1 and w.isupper())] if a and b else []
        wit = wa + gap_words + wb
        wk = keys(wit)
        touched = False
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, tk, wk, autojunk=False).get_opcodes():
            if tag == "equal":
                continue
            at_cut = i1 <= cut <= i2
            if tag == "insert" and not (a and b and i1 == cut):
                continue
            if tag == "delete" and not at_cut:
                continue
            if tag == "replace" and not (i1 < cut < i2 or at_cut and i2 - i1 != j2 - j1):
                continue
            if (i1 == 0 and a) or (i2 == len(tk) and b and i1 < i2 and tag != "delete"):
                continue                                # the outer edge of the window: the rows' own business
            touched = True
            if i1 < cut:                                # starts in verse a (a change running over the cut stays there)
                vid, start, end = a[0], na - cut + i1, na - cut + min(i2, cut)
            else:
                vid, start, end = b[0], i1 - cut, i2 - cut
            place = places.setdefault((vid, start, end), Place(vid, start, end, " ".join(text[i1:i2])))
            place.readings.setdefault(" ".join(wk[j1:j2]), {})[witness] = " ".join(wit[j1:j2])
        if not touched:
            readers.append(witness)
    for (vid, start, end), place in places.items():
        place.support = [w for w in readers if not any(w in r for r in place.readings.values())]
        i1 = start + (cut - na if a and vid == a[0] else cut)
        i2 = i1 + len(place.text.split()) if place.text else i1
        place.context = (" ".join(text[max(0, i1 - 5):i1]) + " ⟦" + place.text + "⟧ " + " ".join(text[i2:i2 + 5])).strip()
        place.sort = "edge"
    return list(places.values())


# Spellings the editions alternate that align.reading keeps apart; a place that differs only in these is a
# spelling (stage 3), not a reading.
SPELLING = [("intellig", "intelleg"), ("exsp", "exp"), ("exst", "ext"), ("exs", "ex"), ("cunque", "cumque"),
            ("nqu", "mqu"), ("quoti", "coti"), ("monim", "monum"), ("dexter", "dextr"), ("decum", "decim"),
            ("accers", "arcess"), ("accerf", "arcess"), ("charis", "caris"), ("ichunt", "icunt"), ("sumps", "sums"),
            ("quend", "quemd"), ("quand", "quamd"), ("andiu", "amdiu"), ("quum", "cum"), ("auth", "auct"), ("leth", "let"), ("thars", "tars"),
            ("ll", "l"), ("rr", "r"), ("bb", "b"), ("ss", "s"), ("ff", "f"), ("cc", "c"), ("gg", "g"), ("y", "i"),
            ("ae", "e"), ("oe", "e")]
# ad- assimilated or not before a consonant (adscendit/ascendit, adlevavit/allevavit), per word.
ASSIMILATED = re.compile(r"^ad(?=[cfglprst])")
# Forms the editions alternate (perfects with and without -v-, the participle of misereor, …): a form
# difference, also for stage 3.
FORMS = [(r"iuer", "ier"), (r"iuit$", "iit"), (r"iuiss", "iiss"), (r"iiss", "iss"), (r"asti", "auisti"),
         (r"misert", "miserit"), (r"ulans", "uclans"), (r"ulant", "uclant"), (r"accubat", "accubit"), (r"sere$", "serunt")]


def spelling_key(words):
    w = "".join(ASSIMILATED.sub("a", align.reading(x)) for x in words.split())
    for old, new in SPELLING:
        w = w.replace(old, new)
    return w


def form_key(words):
    w = spelling_key(words)
    for old, new in FORMS:
        w = re.sub(old, new, w)
    return w


def sort_kind(place):
    """f/s (f against long s), division (same letters), spelling, form, or reading (a different word, or words more
    or fewer)."""
    reading, who = place.against()
    printed = next(iter(who.values()))
    if reading.startswith(FS_MARK):
        return "f/s"
    if reading.replace(" ", "") == "".join(align.reading(w) for w in place.text.split()):
        return "division"
    if spelling_key(printed) == spelling_key(place.text):
        return "spelling"
    if form_key(printed) == form_key(place.text):
        return "form"
    return "reading"


def classify(place):
    reading, who = place.against()
    others = [w for w in who if w not in (place.base, "1556")]
    if place.base in who and others:
        return "correct"
    if place.base in who:
        return "base-only"
    if len(others) >= 2 and place.base not in place.support:
        return "others"
    if len(others) >= 2:
        return f"others-{place.base}-agrees"
    return "noise"


def between(chapter, witness, vids, limit=40):
    """{verse id: the witness's text between the previous verse's row and this one's}, where both rows exist, come
    in order and lie within `limit` tokens of each other."""
    out = {}
    for prev, vid in zip(vids, vids[1:]):
        if prev in chapter.spans and vid in chapter.spans:
            last, first = chapter.spans[prev][1], chapter.spans[vid][0]
            if 0 <= first - last - 1 <= limit:
                out[vid] = " ".join(t for t, _ in witness.tokens[last + 1:first])
    return out


# Scripture references printed in the margins (Gen., Luc., Matth. …) that an OCR runs into the text.
REFERENCES = {"gen", "exod", "exo", "leu", "leuit", "num", "deut", "deu", "psal", "psalm", "esa", "isa", "iesa", "iere",
              "ier", "ezec", "ezech", "dan", "ose", "osee", "ioel", "mich", "hab", "abac", "mal", "matth", "mat",
              "marc", "mar", "luc", "ioan", "ioh", "act", "rom", "cor", "gal", "eph", "ephe", "phil", "col", "thes",
              "tim", "tit", "heb", "hebr", "iac", "pet", "apoc", "cap"}


def known(words):
    """{word: True if the lexicon knows it} (pipeline.macronize's cached lookups)."""
    from pipeline import macronize
    words = {w for w in words if w}
    entries = macronize.lookup(words)
    return {w: bool(entries[macronize.key(w)].candidates) for w in words}


def sift(places):
    """Places worth reading, of the two kinds an OCR fills with noise. f/s: the witness's word must be a Latin
    word (1573's OCR reads ſ as f often: *Apoftoli*, *fuum*), as *fani* for *sani*. Words a witness prints between
    two verses: Latin words, not a running head in capitals, a margin reference (*Gen.*, *Luc.*) or a fragment."""
    is_fs = lambda p: any(r.startswith(FS_MARK) for r in p.readings)
    check = {w for p in places if is_fs(p) or p.sort == "edge" for who in p.readings.values() for v in who.values()
             for w in v.split()}
    lexicon = known(check)
    word_ok = lambda w: lexicon.get(w) and not (w.isupper() and len(w) > 1) and align.fold(w) not in REFERENCES
    out = []
    for place in places:
        if is_fs(place):
            place.readings = {r: who for r, who in place.readings.items() if any(word_ok(v) for v in who.values())}
        elif place.sort == "edge" and not place.text:
            place.readings = {r: who for r, who in place.readings.items()
                              if all(word_ok(w) for v in who.values() for w in v.split())}
        if place.readings:
            out.append(place)
    return out


def collate(osis, chapters, source="draft", witnesses=None):
    """{chapter: [Place]} with each place classified, and the rows of every witness ({key: {vid: row}})."""
    witnesses = witnesses or load_witnesses(osis)
    base = base_rows(osis, chapters, source)
    base_witness = base_key(osis)
    ws = {r["id"]: r["text"] for r in witnesses["ws"]}
    by_chapter = collections.defaultdict(list)
    for vid, text in base:
        by_chapter[tsv.parse_id(vid)[1]].append((vid, text))
    out, all_rows, canvases = {}, collections.defaultdict(dict), {}
    fs_distinct = FS_DISTINCT                         # f against long s means something only in these
    for number in sorted(by_chapter):
        rows = by_chapter[number]
        chapter_rows, gaps = {}, {}
        for key, ws_list in witnesses.items():
            if key == "ws":
                chapter_rows[key] = {vid: ws.get(vid) for vid, _ in rows}
                continue
            tries = [(align.align_chapter(w, rows, number), w) for w in ws_list]
            best, source = max(tries, key=lambda t: sum(1 for m in t[0].matches if m[2] is not None))
            chapter_rows[key] = dict(best.verses)
            gaps[key] = between(best, source, [vid for vid, _ in rows])
            if key == "1573":
                canvases.update(best.pages)
                for vid, marked in best.marked.items():
                    all_rows["1573-marks"][vid] = marked
        places = []
        for vid, text in rows:
            verse_rows = {key: chapter_rows[key].get(vid) for key in chapter_rows}
            for key in chapter_rows:
                all_rows[key][vid] = chapter_rows[key].get(vid)
            places.extend(compare(vid, text, verse_rows, fs_distinct))
        # Words added or lost at each verse boundary (and at the chapter's two ends).
        found = {(p.vid, p.start, p.end, p.sort): p for p in places}
        for a, b in zip([None] + rows, rows + [None]):
            windows = {key: (chapter_rows[key].get(a[0]) if a else None,
                             gaps.get(key, {}).get(b[0], "") if a and b else "",
                             chapter_rows[key].get(b[0]) if b else None) for key in chapter_rows}
            for place in edges(a, b, windows):
                same = found.get((place.vid, place.start, place.end, ""))
                if same:                              # the verse's own comparison saw it too: one place
                    for reading, who in place.readings.items():
                        same.readings.setdefault(reading, {}).update(who)
                    continue
                places.append(place)
        places = sift(places)
        for place in places:
            place.base = base_witness
            place.kind = classify(place)
            place.sort = place.sort or sort_kind(place)
        out[number] = sorted(places, key=lambda p: (tsv.parse_id(p.vid)[2], p.start, p.end))
    all_rows["canvas"] = canvases
    all_rows["uncovered"] = uncovered(base, all_rows[base_witness])
    return out, all_rows
