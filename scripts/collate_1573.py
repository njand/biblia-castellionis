"""Collate the 1573 Basel edition (Perna, "ex postrema recognitione"; MDZ bsb10141277 hOCR) against 1556.

Both OCRs are aligned to Wikisource's NT, so each Wikisource word has a 1573 word and a 1556 word. Where both are
found and read differently (spelling habits aside), the other printings say whether each side is a real reading:
  change    1573's reading is also in a later printing (1681, 1715, 1747, 1750, 1758) or Wikisource, and 1556's
            is also in one of them or in Wikisource: two real readings, so a change between 1556 and 1573
  1573-ocr  1573's reading is in no other text: most likely OCR noise in 1573
  1556-ocr  1556's reading is in no other text (and 1573's is): most likely OCR noise in 1556
Writes <out>/nt1573.tsv (every difference) and <out>/nt1573-books.tsv, and prints per-book counts.
The hOCR pages are cached in sources/mdz-1573/<canvas>.hocr and read by pipeline.mdz (canvases 747–960 hold the NT).
"""
import collections
import pathlib
import sys

REPO = pathlib.Path(sys.argv[1])
OUT = pathlib.Path(sys.argv[2])
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "scripts"))
from pipeline import align, books, mdz, paths, tsv  # noqa: E402

LATER = [("1758", ["1758-1", "1758-2"]), ("1681", ["1681"]), ("1715", ["1715"]), ("1747", ["1747"]),
         ("1750", ["1750"])]


def text_1556():
    folder = REPO / "sources" / "erara-1556"
    pages = sorted(folder.glob("1028*.txt"), key=lambda p: int(p.stem))
    text = "\n".join(p.read_text(encoding="utf-8") for p in pages).replace("ę", "ae").replace("Ę", "Ae")
    return "".join({"ā": "ã", "ē": "ẽ", "ī": "ĩ", "ō": "õ", "ū": "ũ"}.get(c, c) for c in text)


def main():
    witnesses = {"1573": [mdz.witness()], "1556": [align.Witness(text_1556())]}
    for key, files in LATER:
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
        for c, chapter in enumerate(aligned["1573"]):
            ch56 = aligned["1556"][c]
            for i, (vid, ws_word, w73) in enumerate(chapter.matches):
                counts["words"] += 1
                if w73 is not None and i not in chapter.joined:
                    counts["found_1573"] += 1
                    if align.reading(w73) == align.reading(ws_word):
                        counts["1573_eq_ws"] += 1
                w56 = ch56.matches[i][2] if i < len(ch56.matches) else None
                if w73 is None or w56 is None or i in chapter.joined or i in ch56.joined:
                    continue
                counts["both"] += 1
                r73, r56 = align.reading(w73), align.reading(w56)
                if r73 == r56:
                    counts["same"] += 1
                    continue
                others = {"ws": ws_word}
                for key, _ in LATER:
                    o = aligned[key][c]
                    if i < len(o.matches) and o.matches[i][2] and i not in o.joined:
                        others[key] = o.matches[i][2]
                with73 = sorted(k for k, w in others.items() if align.reading(w) == r73)
                with56 = sorted(k for k, w in others.items() if align.reading(w) == r56)
                kind = "change" if with73 and with56 else "1573-ocr" if not with73 else "1556-ocr"
                counts[kind] += 1
                rows.append((vid, ws_word, w56, w73, kind, ",".join(with56), ",".join(with73),
                             " | ".join(f"{k}:{w}" for k, w in sorted(others.items()))))
        summary.append((book.osis, counts))
        print(f"{book.osis:6} words {counts['words']:6}  1573 found {counts['found_1573'] / max(1, counts['words']):6.1%}"
              f"  =ws {counts['1573_eq_ws'] / max(1, counts['found_1573']):6.2%}  both {counts['both']:6}"
              f"  same {counts['same'] / max(1, counts['both']):6.2%}  change {counts['change']:4}"
              f"  1573-ocr {counts['1573-ocr']:5}  1556-ocr {counts['1556-ocr']:5}", flush=True)
    OUT.mkdir(parents=True, exist_ok=True)
    tsv.write(OUT / "nt1573.tsv", rows, header=("id", "wikisource", "1556", "1573", "kind", "with_1556", "with_1573",
                                                 "witnesses"))
    tsv.write(OUT / "nt1573-books.tsv",
              [(osis, c["words"], c["found_1573"], c["1573_eq_ws"], c["both"], c["same"], c["change"], c["1573-ocr"],
                c["1556-ocr"]) for osis, c in summary],
              header=("book", "words", "found_1573", "1573_eq_wikisource", "both_found", "same", "change",
                      "ocr_1573", "ocr_1556"))


main()
