"""Stage 2: collating a chapter's text against the printings, verse by verse (PLAN.md §4, stage 2).

The text collated is the drafted chapter (text/draft/<USFM>.usfm) or, where there is none, Wikisource. Every
witness is aligned to it (pipeline.align) and its verse row compared with the verse word by word on the
spelling-blind reading form (align.reading: case, macrons, i/j, u/v, æ, h-, double letters and the editions'
spelling habits aside), so what is left is a different word, a word more or a word less.

Each difference is a *place*: a span of the text's words (empty for a word the text lacks) and what each
witness reads there. A witness that reads the text's words there supports the text; a witness whose row does
not reach the place says nothing. Places are classified:

  correct     1573 (the base) and at least one other printing or Wikisource agree against the text
  base-only   1573 alone against the text (often its OCR; read on the page image)
  others      1573 agrees with the text, or says nothing, while two or more others agree against it
  variant     1556 (the reference) differs from 1573 where 1573 is read
Noise (a reading of one OCR alone) is counted, not listed.

The witnesses: 1573 (MDZ hOCR, the NT base), 1556 (e-rara OCR, the reference; reads poorly), 1758, 1681, 1715,
1747, 1750 (archive.org OCR) and Wikisource."""

import collections
import difflib
import re
from dataclasses import dataclass, field

from pipeline import align, books, gold, latex, mdz, paths, tsv

PRINTINGS = [("1556", None), ("1758", ("1758-1", "1758-2")), ("1681", ("1681",)), ("1715", ("1715",)),
             ("1747", ("1747",)), ("1750", ("1750",))]
MACRON_TO_TILDE = {"ā": "ã", "ē": "ẽ", "ī": "ĩ", "ō": "õ", "ū": "ũ"}


def text_1556():
    """The e-rara 1556 OCR (sources/erara-1556/), e caudata as ae, nasal bars as tildes (align.clean expands)."""
    pages = sorted((paths.SOURCES / "erara-1556").glob("1028*.txt"), key=lambda p: int(p.stem))
    text = "\n".join(p.read_text(encoding="utf-8") for p in pages).replace("ę", "ae").replace("Ę", "Ae")
    return "".join(MACRON_TO_TILDE.get(c, c) for c in text)


def load_witnesses(osis):
    """{key: [align.Witness]} for a New Testament book: 1573, 1556, the archive.org printings, Wikisource."""
    out = {"1573": [mdz.witness()]}
    for key, files in PRINTINGS:
        if files is None:
            out[key] = [align.Witness(text_1556())]
        else:
            out[key] = [align.Witness((paths.SOURCES / "archive" / f / "text.txt").read_text(encoding="utf-8"))
                        for f in files if (paths.SOURCES / "archive" / f / "text.txt").exists()]
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
    context: str = ""

    def against(self):
        """(folded reading, {witness: as printed}) with the most witnesses against the text."""
        return max(self.readings.items(), key=lambda kv: (("1573" in kv[1]) + len(kv[1]), len(kv[0])))


def keys(words):
    return [align.reading(w) for w in words]


def word_list(text):
    return [t for t, is_word in align.words(align.clean(text)) if is_word]


def compare(vid, base_text, rows):
    """[Place] for one verse. rows: {witness: its verse row text, or None where it has none}."""
    base = word_list(base_text)
    bk = keys(base)
    places = {}
    for witness, row in rows.items():
        if not row:
            continue
        wit = word_list(row)
        wk = keys(wit)
        matcher = difflib.SequenceMatcher(None, bk, wk, autojunk=False)
        blocks = matcher.get_matching_blocks()
        if sum(b.size for b in blocks) < 0.5 * len(bk):
            continue                                  # a row that is mostly something else: no evidence
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
    for (i1, i2), place in places.items():
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
        place.context = (" ".join(base[max(0, i1 - 5):i1]) + " ⟦" + place.text + "⟧ " + " ".join(base[i2:i2 + 5])).strip()
    return sorted(places.values(), key=lambda p: (p.start, p.end))


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
    """division (same letters), spelling, form, or reading (a different word, or words more or fewer)."""
    reading, who = place.against()
    printed = next(iter(who.values()))
    if reading.replace(" ", "") == "".join(align.reading(w) for w in place.text.split()):
        return "division"
    if spelling_key(printed) == spelling_key(place.text):
        return "spelling"
    if form_key(printed) == form_key(place.text):
        return "form"
    return "reading"


def classify(place):
    reading, who = place.against()
    others = [w for w in who if w not in ("1573", "1556")]
    if "1573" in who and others:
        return "correct"
    if "1573" in who:
        return "base-only"
    if len(others) >= 2 and "1573" not in place.support:
        return "others"
    if len(others) >= 2:
        return "others-1573-agrees"
    return "noise"


def collate(osis, chapters, source="draft", witnesses=None):
    """{chapter: [Place]} with each place classified, and the rows of every witness ({key: {vid: row}})."""
    witnesses = witnesses or load_witnesses(osis)
    base = base_rows(osis, chapters, source)
    ws = {r["id"]: r["text"] for r in witnesses["ws"]}
    by_chapter = collections.defaultdict(list)
    for vid, text in base:
        by_chapter[tsv.parse_id(vid)[1]].append((vid, text))
    out, all_rows, canvases = {}, collections.defaultdict(dict), {}
    for number in sorted(by_chapter):
        rows = by_chapter[number]
        chapter_rows = {}
        for key, ws_list in witnesses.items():
            if key == "ws":
                chapter_rows[key] = {vid: ws.get(vid) for vid, _ in rows}
                continue
            tries = [align.align_chapter(w, rows, number) for w in ws_list]
            best = max(tries, key=lambda c: sum(1 for m in c.matches if m[2] is not None))
            chapter_rows[key] = dict(best.verses)
            if key == "1573":
                canvases.update(best.pages)
                for vid, marked in best.marked.items():
                    all_rows["1573-marks"][vid] = marked
        places = []
        for vid, text in rows:
            verse_rows = {key: chapter_rows[key].get(vid) for key in chapter_rows}
            for key in chapter_rows:
                all_rows[key][vid] = chapter_rows[key].get(vid)
            for place in compare(vid, text, verse_rows):
                place.kind = classify(place)
                place.sort = sort_kind(place)
                places.append(place)
        out[number] = places
    all_rows["canvas"] = canvases
    return out, all_rows
