"""Parallel Bibles: downloads, USFM parsing and the KJV versification table.

USFM texts (ebible.org) are parsed into sources/parallel/<key>/<osis>.tsv with columns `id  text  marks`:
`marks` lists the layout markers met since the previous verse (p, m, q1, q2, b, s1:<heading>…), which stage 5
uses to transfer paragraphs and poetry. The Greek and Hebrew (SBLGNT, OSHB) are only downloaded for now.
data/versification/kjv.tsv (book, chapter, verses) is committed: it is the target numbering of this edition."""

import re
import zipfile
from dataclasses import dataclass

from pipeline import books, net, paths, tsv


@dataclass(frozen=True)
class Text:
    key: str
    url: str
    usfm: bool
    note: str


TEXTS = [
    Text("kjv", "https://ebible.org/Scriptures/eng-kjv2006_usfm.zip", True, "King James Version (with Apocrypha); public domain"),
    Text("bsb", "https://ebible.org/Scriptures/engbsb_usfm.zip", True, "Berean Standard Bible; public domain; paragraphs, poetry, quotation marks"),
    Text("web", "https://ebible.org/Scriptures/eng-web_usfm.zip", True, "World English Bible; public domain"),
    Text("vulgate", "https://ebible.org/Scriptures/latVUC_usfm.zip", True, "Vulgata Clementina; public domain"),
    Text("wlc", "https://ebible.org/Scriptures/hboWLC_usfm.zip", True, "Westminster Leningrad Codex (Hebrew OT); text public domain (its lemma/morphology attributes, CC BY-SA, are dropped)"),
    Text("tr", "https://ebible.org/Scriptures/grctr_usfm.zip", True, "Greek Textus Receptus (Stephanus 1550, Elzevir 1624, Scrivener 1881 collated); public domain"),
    Text("lxx", "https://ebible.org/Scriptures/grcbrent_usfm.zip", True, "Septuagint, the Greek text of Brenton's edition (1851); public domain"),
    Text("sblgnt", "https://github.com/LogosBible/SBLGNT/archive/refs/heads/master.zip", False, "SBL Greek New Testament; CC BY 4.0"),
    Text("oshb", "https://github.com/openscriptures/morphhb/archive/refs/heads/master.zip", False, "Open Scriptures Hebrew Bible (WLC + morphology); CC BY 4.0"),
]

BY_KEY = {text.key: text for text in TEXTS}
_ORDER = {book.osis: n for n, book in enumerate(books.BOOKS)}

LAYOUT = {"p", "m", "pi", "pi1", "pi2", "mi", "nb", "pc", "q", "q1", "q2", "q3", "qc", "qr", "qm", "b", "li", "li1", "li2", "d"}
LAYOUT_SPLIT = re.compile(r"\s*\\(" + "|".join(sorted(LAYOUT, key=len, reverse=True)) + r")\b\s*")
HEADINGS = {"s", "s1", "s2", "ms", "mr", "r", "sp"}
# Notes and cross-references are dropped with their content; other character markers keep their text.
DROP = re.compile(r"\\(f|x|fe)\s.*?\\\1\*", re.DOTALL)
WORD = re.compile(r"\\\+?w\s+([^|\\]*)(?:\|[^\\]*)?\\\+?w\*")
CHAR = re.compile(r"\\\+?[a-z]+\d?(?:\*|\s?)")     # a space after an opening marker belongs to it; after \x* it is text


def strip_inline(text, keep=()):
    """The text without notes, word attributes or character markers (except the markers named in `keep`)."""
    text = DROP.sub("", text)
    text = WORD.sub(r"\1", text)
    text = CHAR.sub(lambda m: m.group(0) if m.group(0).strip("\\+* ") in keep else "", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_usfm(source, keep=()):
    """Return (usfm book code, [(chapter, verse, text, marks, layout)]).

    `marks` are the markers met between the previous verse and this one (paragraph, poetry, headings);
    `layout` is the verse text with the layout markers that fall inside it kept inline ("… wicked, \\q2 or …"),
    and the character markers named in `keep` (e.g. "qt" keeps \\qt …\\qt*)."""
    code, chapter, rows, marks = None, 0, [], []
    # A verse can start mid-line ("\q1 \v 2 …"), so each \v begins a line of its own.
    lines = [piece for line in source.splitlines() for piece in re.split(r"(?=\\v\s)", line)]
    for line in lines:
        match = re.match(r"\\(\w+)\s?(.*)", line.strip())
        if not match:
            if rows and line.strip():
                rows[-1][2] += " " + line.strip()
            continue
        marker, rest = match.groups()
        if marker == "id":
            code = rest.split()[0]
        elif marker == "c":
            chapter = int(rest.split()[0])
            marks = []
        elif marker == "v":
            number, _, text = rest.partition(" ")
            rows.append([chapter, int(re.match(r"\d+", number).group()), text, marks])
            marks = []
        elif marker in LAYOUT:
            if rest.strip() and rows:
                # a new line inside the current verse; a bare marker just before it (\b) belongs there too
                rows[-1][2] += "".join(f" \\{m}" for m in marks) + f" \\{marker} {rest}"
                marks = []
            else:
                marks.append(marker)                     # layout before the next verse
        elif marker in HEADINGS:
            marks.append(f"{marker}:{strip_inline(rest)}")
        elif rows and marker not in ("toc1", "toc2", "toc3", "h", "mt", "mt1", "mt2", "ide", "rem", "cl", "cp", "cls"):
            rows[-1][2] += " " + line.strip()
    out = []
    for c, v, raw, m in rows:
        # parts = [text, marker, text, marker, text, …]
        parts = LAYOUT_SPLIT.split(raw)
        texts = [strip_inline(part) for part in parts[0::2]]
        kept = [strip_inline(part, keep) for part in parts[0::2]] if keep else texts
        layout = kept[0] + "".join(f" \\{marker} {text}" for marker, text in zip(parts[1::2], kept[1:]))
        out.append((c, v, " ".join(t for t in texts if t), " ".join(m), layout.strip()))
    return code, out


def fetch(text: Text, refresh=False):
    """Download and unpack one text; parse USFM into per-book TSVs. Returns the number of books parsed."""
    folder = paths.SOURCES / "parallel" / text.key
    archive = net.download(text.url, folder / "download.zip", refresh)
    unpacked = folder / "files"
    if refresh or not unpacked.exists():
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(unpacked)
    if not text.usfm:
        return 0
    count = 0
    for usfm_file in sorted(unpacked.rglob("*.usfm")) + sorted(unpacked.rglob("*.SFM")):
        code, rows = parse_usfm(usfm_file.read_text(encoding="utf-8-sig"))
        book = books.BY_USFM.get(code)
        if not book or not rows:
            continue
        tsv.write(folder / f"{book.osis}.tsv", [(tsv.verse_id(book.osis, c, v), t, m, layout)
                                               for c, v, t, m, layout in rows], header=("id", "text", "marks", "layout"))
        count += 1
    return count


def write_kjv_versification():
    """data/versification/kjv.tsv from the parsed KJV: one row per chapter with its verse count."""
    folder = paths.SOURCES / "parallel" / "kjv"
    out = []
    for book in books.BOOKS:
        path = folder / f"{book.osis}.tsv"
        if not path.exists():
            continue
        counts = {}
        for row in tsv.read(path):
            _, chapter, verse = tsv.parse_id(row["id"])
            counts[chapter] = max(counts.get(chapter, 0), verse)
        out += [(book.osis, chapter, verses) for chapter, verses in sorted(counts.items())]
    tsv.write(paths.VERSIFICATION / "kjv.tsv", out, header=("book", "chapter", "verses"))
    return out


# ---------------------------------------------------------------- other numberings → the KJV's

def write_wlc_map():
    """data/versification/wlc.map.tsv from the OSHB's wlc/VerseMap.xml (the WLC's verses that the KJV numbers
    differently), runs of the same shift written as one range. Returns the rows, or [] without the OSHB."""
    import xml.etree.ElementTree as ET
    found = sorted((paths.SOURCES / "parallel" / "oshb" / "files").rglob("VerseMap.xml"))
    if not found:
        return []
    # a verse divided between two ("Ps.13.6!a") goes whole to the KJV verse its first part is in
    pairs = {}
    for book in ET.parse(found[0]).getroot():
        for v in book:
            pairs.setdefault(tsv.parse_id(v.get("wlc").split("!")[0]), tsv.parse_id(v.get("kjv").split("!")[0]))
    pairs = sorted(pairs.items(), key=lambda pair: (_ORDER.get(pair[0][0], 999),) + pair[0][1:])
    rows, run = [], None
    for (book, c, v), (kbook, kc, kv) in pairs:
        if run and [book, c, kbook, kc, kv - v] == run[:2] + run[4:7] and v == run[3] + 1:
            run[3] = v
            continue
        if run:
            rows.append(run)
        run = [book, c, v, v, kbook, kc, kv - v]
    if run:
        rows.append(run)
    out = [(f"{b}.{c}.{v1}" + (f"-{v2}" if v2 != v1 else ""), f"{kb}.{kc}.{v1 + shift}",
            "OSHB VerseMap (CC BY 4.0)") for b, c, v1, v2, kb, kc, shift in rows]
    books_seen = list(dict.fromkeys(b.osis for b in books.BOOKS if b.testament == "vetus" and not b.apocrypha))
    header = [(b, "=", "numbering as the KJV except the rows below") for b in books_seen]
    tsv.write(paths.VERSIFICATION / "wlc.map.tsv", header + out, header=("source", "target", "note"))
    return out


def _parse_ref(text):
    """'Mark.9.1-49' → ('Mark', 9, 1, 49); 'Exod.36-39' → ('Exod', 36, None, 39) (whole chapters)."""
    book, _, rest = text.partition(".")
    if rest.count(".") == 0:
        first, _, last = rest.partition("-")
        return book, int(first), None, int(last or first)
    chapter, _, verses = rest.partition(".")
    first, _, last = verses.partition("-")
    return book, int(chapter), int(first), int(last or first)


def verse_map(key):
    """The rows of data/versification/<key>.map.tsv as ({book: note} of books checked against the KJV,
    [(book, chapter, first, last, target book, target chapter, target first)], {(book, chapter): (note, first verse,
    last verse)} of the verses that cannot be aligned: a target `-`; `Exod.37-39` names whole chapters, `Exod.36.8-38`
    verses). None when the text has no map (it is numbered as the KJV throughout)."""
    path = paths.VERSIFICATION / f"{key}.map.tsv"
    if not path.exists():
        return None
    checked, shifts, unaligned = {}, [], {}
    for row in tsv.read(path):
        source, target = row["source"], row["target"]
        if target == "=":
            checked[source] = row["note"]
            continue
        book, chapter, first, last = _parse_ref(source)
        if target == "-":
            if first is None:
                for c in range(chapter, last + 1):
                    unaligned[(book, c)] = (row["note"], 1, 999)
            else:
                unaligned[(book, chapter)] = (row["note"], first, last)
            continue
        tbook, tchapter, tfirst, _ = _parse_ref(target)
        shifts.append((book, chapter, first, last, tbook, tchapter, tfirst))
    return checked, shifts, unaligned


def aligned(key, osis, sources=None):
    """A parallel text's verses of one book in the KJV's numbering: ({kjv id: text}, {chapter: note} where verses are
    left out as not aligned), or None when the text is not at hand or its numbering is unchecked for this book."""
    path = (sources or paths.SOURCES) / "parallel" / key / f"{osis}.tsv"
    if not path.exists():
        return None
    rows = [(row["id"], row["text"]) for row in tsv.read(path)]
    mapping = verse_map(key)
    if mapping is None:
        return dict(rows), {}
    checked, shifts, unaligned = mapping
    if osis not in checked:
        return None
    out = {}
    for vid, text in rows:
        book, chapter, verse = tsv.parse_id(vid)
        gap = unaligned.get((book, chapter))
        if gap and gap[1] <= verse <= gap[2]:
            continue
        for sbook, sc, first, last, tbook, tc, tfirst in shifts:
            if (sbook, sc) == (book, chapter) and first <= verse <= last:
                vid = tsv.verse_id(tbook, tc, tfirst + verse - first)
                break
        out[vid] = f"{out[vid]} {text}" if vid in out else text       # two verses joined in the KJV
    gaps = {c: note for (book, c), (note, _, _) in unaligned.items() if book == osis}
    return out, gaps


def kjv_counts():
    """{(osis, chapter): verses} from data/versification/kjv.tsv."""
    path = paths.VERSIFICATION / "kjv.tsv"
    if not path.exists():
        return {}
    return {(row["book"], int(row["chapter"])): int(row["verses"]) for row in tsv.read(path)}
