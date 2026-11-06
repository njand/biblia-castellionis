"""The gold set: the settled chapters of the USFM master (text/<USFM code>.usfm), one row per verse.

data/gold/<osis>.tsv has the parallel texts' columns (see parallel.py), so every stage can be scored against it:

  id      OSIS id, numbered as the master numbers it (Genesis still follows the 1726–27 numbering in places)
  text    the reading text: macrons, æ/œ, “…” ‘…’ and punctuation as printed; no markup
  marks   layout markers before the verse: p, m, q1/q2/q3, b
  layout  the text with the markers inside the verse kept inline, and \\qt …\\qt* around quoted Scripture

The file is rebuilt from the USFM by `python -m pipeline gold`; edit the USFM, never this."""

from pipeline import books, latex, parallel, paths, tsv

GOLD = paths.DATA / "gold"
HEADER = ("id", "text", "marks", "layout")


def rows(usfm, osis):
    """[(id, text, marks, layout)] for a USFM book."""
    _, verses = parallel.parse_usfm(usfm.replace(latex.SOFT_HYPHEN, ""), keep=("qt",))
    return [(tsv.verse_id(osis, c, v), text, marks, layout) for c, v, text, marks, layout in verses]


def build(names=()):
    """Write data/gold/<osis>.tsv for every book that has a USFM master. Returns {osis: rows}."""
    built = {}
    for book in books.select(names):
        path = latex.usfm_path(book)
        if not path.exists():
            continue
        built[book.osis] = rows(path.read_text(encoding="utf-8"), book.osis)
        tsv.write(GOLD / f"{book.osis}.tsv", built[book.osis], header=HEADER)
    return built


def load(osis):
    """{id: row} from data/gold/<osis>.tsv ({} if the book has no gold text)."""
    path = GOLD / f"{osis}.tsv"
    return {row["id"]: row for row in tsv.read(path)} if path.exists() else {}
