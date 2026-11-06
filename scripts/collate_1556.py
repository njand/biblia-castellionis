"""Collate Wikisource's NT against the 1556 Basel edition (e-rara OCR), with other printings as corroboration.

For every Wikisource word, the 1556 OCR word aligned to it is compared in reading (spelling habits aside).
Where 1556 differs, the other OCR witnesses decide what kind of difference it is:
  wikisource-slip  every other witness found agrees with 1556 (Wikisource alone differs)
  edition          the witnesses split; 1556 sides with some of them
  1556-only        no other witness reads as 1556 does: OCR noise in 1556, or a reading only 1556 has
Writes <out>/nt1556.tsv (every difference) and prints per-book counts.
"""
import collections
import pathlib
import re
import sys

REPO = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
sys.path.insert(0, str(REPO))
from pipeline import align, books, paths, tsv  # noqa: E402

MACRON_TO_TILDE = {"ā": "ã", "ē": "ẽ", "ī": "ĩ", "ō": "õ", "ū": "ũ"}


def text_1556():
    folder = REPO / "sources" / "erara-1556"
    pages = sorted(folder.glob("1028*.txt"), key=lambda p: int(p.stem))
    text = "\n".join(p.read_text(encoding="utf-8") for p in pages)
    text = text.replace("ę", "ae").replace("Ę", "Ae")                  # e caudata
    return "".join(MACRON_TO_TILDE.get(c, c) for c in text)         # nasal bars: ū → ũ (clean expands)


def main():
    witnesses = {"1556": [align.Witness(text_1556())]}
    for key, files in [("1758", ["1758-1", "1758-2"]), ("1681", ["1681"]), ("1747", ["1747"]), ("1750", ["1750"])]:
        witnesses[key] = [align.Witness((paths.SOURCES / "archive" / f / "text.txt").read_text(encoding="utf-8"))
                          for f in files]
    rows, summary = [], []
    for book in [b for b in books.BOOKS if b.testament == "novum"]:
        path = paths.WITNESSES / "wikisource" / f"{book.osis}.tsv"
        if not path.exists():
            continue
        base = [(r["id"], r["text"]) for r in tsv.read(path) if r["text"]]
        aligned = {k: align.align_book(ws, base) for k, ws in witnesses.items()}
        counts = collections.Counter()
        for c_index, chapter in enumerate(aligned["1556"]):
            others = {k: aligned[k][c_index] for k in aligned if k != "1556"}
            for i, (vid, ws_word, w1556) in enumerate(chapter.matches):
                counts["words"] += 1
                if w1556 is None or i in chapter.joined:
                    continue
                counts["found"] += 1
                r1556, rws = align.reading(w1556), align.reading(ws_word)
                if r1556 == rws:
                    counts["same"] += 1
                    continue
                readings = {k: o.matches[i][2] for k, o in others.items()
                            if i < len(o.matches) and o.matches[i][2] and i not in o.joined}
                with_1556 = sorted(k for k, w in readings.items() if align.reading(w) == r1556)
                with_ws = sorted(k for k, w in readings.items() if align.reading(w) == rws)
                if with_1556 and not with_ws:
                    kind = "wikisource-slip"
                elif with_1556:
                    kind = "edition"
                else:
                    kind = "1556-only"
                counts[kind] += 1
                rows.append((vid, ws_word, w1556, kind, ",".join(with_1556), ",".join(with_ws),
                             " | ".join(f"{k}:{w}" for k, w in sorted(readings.items()))))
        summary.append((book.osis, counts))
        print(f"{book.osis:6} words {counts['words']:6}  found {counts['found'] / max(1, counts['words']):6.1%}  "
              f"same {counts['same'] / max(1, counts['found']):6.2%}  edition {counts['edition']:4}  "
              f"ws-slip {counts['wikisource-slip']:4}  1556-only {counts['1556-only']:5}", flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    tsv.write(OUT / "nt1556.tsv", rows, header=("id", "wikisource", "1556", "kind", "with_1556", "with_wikisource",
                                                 "witnesses"))
    tsv.write(OUT / "nt1556-books.tsv",
              [(osis, c["words"], c["found"], c["same"], c["edition"], c["wikisource-slip"], c["1556-only"])
               for osis, c in summary],
              header=("book", "words", "found", "same", "edition", "wikisource_slip", "only_1556"))


main()
