"""Verse TSV files: a header row, then one row per verse, keyed by OSIS id (`Matt.14.3`).

Verse 0 (`Matt.14.0`) holds a chapter's summary (argumentum) where a source has one."""

import csv
from pathlib import Path


class Verse(int):
    """A verse number, or a range of KJV verses that one verse of Castellio's stands for (USFM `\\v 12-83`: Num 7,
    where he gives the princes' offering once and the KJV twelve times). It is its first number wherever a number
    is compared, sorted or counted from; `last` is the last, and it prints as `12-83` (ids, USFM) or with
    `display` as `12–83`."""

    def __new__(cls, first, last=None):
        self = super().__new__(cls, first)
        self.last = int(first) if last is None else int(last)
        if self.last < self:
            raise ValueError(f"verse range {first}-{last} runs backwards")
        return self

    @property
    def is_range(self):
        return self.last > self

    def __str__(self):
        return f"{int(self)}-{self.last}" if self.is_range else str(int(self))

    __repr__ = __str__

    def __format__(self, spec):
        return format(str(self), spec) if not spec or spec[-1] not in "dnxXobeEfFgG%c" else format(int(self), spec)

    def display(self):
        return f"{int(self)}–{self.last}" if self.is_range else str(int(self))

    def numbers(self):
        return range(int(self), self.last + 1)


def parse_number(text):
    """`12` or `12-83` (a USFM verse range) → Verse."""
    first, _, last = str(text).partition("-")
    return Verse(int(first), int(last) if last else None)


def verse_id(osis, chapter, verse):
    return f"{osis}.{chapter}.{verse}"


def parse_id(vid):
    osis, chapter, verse = vid.rsplit(".", 2)
    return osis, int(chapter), parse_number(verse)


def write(path: Path, rows, header=("id", "text")):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, escapechar="\\")
        writer.writerow(header)
        for row in rows:
            writer.writerow([str(cell).replace("\t", " ").replace("\n", " ") for cell in row])


def read(path: Path):
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle, delimiter="\t", quoting=csv.QUOTE_NONE, escapechar="\\")
        header = next(reader)
        return [dict(zip(header, row)) for row in reader]
