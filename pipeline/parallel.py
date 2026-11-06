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
    Text("sblgnt", "https://github.com/LogosBible/SBLGNT/archive/refs/heads/master.zip", False, "SBL Greek New Testament; CC BY 4.0"),
    Text("oshb", "https://github.com/openscriptures/morphhb/archive/refs/heads/master.zip", False, "Open Scriptures Hebrew Bible (WLC + morphology); CC BY 4.0"),
]

BY_KEY = {text.key: text for text in TEXTS}

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
        elif rows and marker not in ("toc1", "toc2", "toc3", "h", "mt", "mt1", "mt2", "ide", "rem", "cl", "cp"):
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


def kjv_counts():
    """{(osis, chapter): verses} from data/versification/kjv.tsv."""
    path = paths.VERSIFICATION / "kjv.tsv"
    if not path.exists():
        return {}
    return {(row["book"], int(row["chapter"])): int(row["verses"]) for row in tsv.read(path)}
