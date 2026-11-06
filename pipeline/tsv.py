"""Verse TSV files: a header row, then one row per verse, keyed by OSIS id (`Matt.14.3`).

Verse 0 (`Matt.14.0`) holds a chapter's summary (argumentum) where a source has one."""

import csv
from pathlib import Path


def verse_id(osis, chapter, verse):
    return f"{osis}.{chapter}.{verse}"


def parse_id(vid):
    osis, chapter, verse = vid.rsplit(".", 2)
    return osis, int(chapter), int(verse)


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
