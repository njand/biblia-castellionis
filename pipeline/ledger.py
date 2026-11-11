"""The chapter ledger, data/status.tsv: one row per chapter (KJV numbering) with its stage and the material
available for it.

stage    where the chapter is in the pipeline. `settled` = finished in the USFM master, text/<USFM>.usfm; never
         rewritten by the pipeline;
         otherwise pending → fetched → aligned → corrected → normalized → macronized → structured →
         in-review → approved (approved chapters become settled). Only `ledger set` moves a chapter past
         `fetched`; `ledger refresh` recomputes everything else and keeps those stages and the notes.
repo     the furthest earlier work in this repo: usfm, usfm-draft (text/draft/), txt-edited, txt-corrected, ocr, or -
wikisource, wordpress   verses each witness has for the chapter (- if none)
flags    verses the Wikisource parser flagged for review (joined, gap, repeat)"""

import re

from pipeline import books, latex, parallel, paths, tsv, wikisource

STAGES = ["pending", "fetched", "aligned", "corrected", "normalized", "macronized", "structured",
          "in-review", "approved", "settled"]
REPO_ORDER = ["usfm", "usfm-draft", "txt-edited", "txt-corrected", "ocr"]
HEADER = ("chapter", "verses", "stage", "repo", "wikisource", "wordpress", "flags", "note")

TESTAMENT_DIR = {"vetus": "Vetus Fœdus", "novum": "Novum Fœdus"}
TXT_STAGES = [("txt-edited", "3 - Edited"), ("txt-corrected", "2 - Post-Corrected")]


def usfm_chapters(book):
    """(settled chapter numbers, draft chapter numbers) in the USFM master, or None if the book has none yet."""
    path = latex.usfm_path(book)
    if not path.exists():
        return None
    chapters = lambda p: {int(n) for n in re.findall(r"^\\c\s+(\d+)", p.read_text(encoding="utf-8"), re.MULTILINE)} \
        if p.exists() else set()
    return chapters(path), chapters(latex.usfm_path(book, draft=True))


def txt_chapters(book, stage_dir):
    path = paths.TXT / stage_dir / TESTAMENT_DIR[book.testament] / f"{book.slug}.txt"
    if not path.exists():
        return set()
    numerals = re.findall(r"^\s*CAPUT\s+([IVXLC]+)\b", path.read_text(encoding="utf-8"), flags=re.MULTILINE)
    return {wikisource.roman(numeral) for numeral in numerals}


def has_ocr(book):
    return (paths.TXT / "1 - OCR" / TESTAMENT_DIR[book.testament] / f"{book.slug}.txt").exists()


def witness_counts(source, book):
    """({chapter: verses}, {chapter: flagged verses}) for a witness TSV."""
    path = paths.WITNESSES / source / f"{book.osis}.tsv"
    counts, flagged = {}, {}
    if not path.exists():
        return counts, flagged
    for row in tsv.read(path):
        _, chapter, verse = tsv.parse_id(row["id"])
        if verse == 0:
            continue
        counts[chapter] = counts.get(chapter, 0) + 1
        if row.get("flags") and wikisource.needs_review(row["flags"]):
            flagged[chapter] = flagged.get(chapter, 0) + 1
    return counts, flagged


def load():
    if not paths.LEDGER.exists():
        return {}
    return {row["chapter"]: row for row in tsv.read(paths.LEDGER)}


def save(rows):
    tsv.write(paths.LEDGER, [[row[column] for column in HEADER] for row in rows], header=HEADER)


def refresh():
    """Rebuild data/status.tsv from the repo and the witnesses, keeping manual stages and notes."""
    previous = load()
    kjv = parallel.kjv_counts()
    if not kjv:
        raise SystemExit("ledger: data/versification/kjv.tsv missing; run `python -m pipeline fetch parallel` first")
    rows = []
    for book in books.BOOKS:
        master = usfm_chapters(book)
        live, draft = master or (set(), set())
        kind = "usfm"
        txt = {name: txt_chapters(book, folder) for name, folder in TXT_STAGES}
        ocr = has_ocr(book)
        ws, ws_flags = witness_counts("wikisource", book)
        wp, _ = witness_counts("wordpress", book)
        chapters = sorted(c for (osis, c) in kjv if osis == book.osis) or sorted(set(ws) | set(wp))
        for chapter in chapters:
            key = f"{book.osis}.{chapter}"
            repo = (kind if chapter in live else f"{kind}-draft" if chapter in draft
                    else next((name for name, found in txt.items() if chapter in found), "ocr" if ocr else "-"))
            stage = "settled" if repo == kind else "fetched" if chapter in ws or chapter in wp else "pending"
            old = previous.get(key, {})
            if stage != "settled" and STAGES.index(old.get("stage", "pending")) > STAGES.index("fetched"):
                stage = old["stage"]
            rows.append({"chapter": key, "verses": kjv.get((book.osis, chapter), ""), "stage": stage, "repo": repo,
                         "wikisource": ws.get(chapter, "-"), "wordpress": wp.get(chapter, "-"),
                         "flags": ws_flags.get(chapter, 0) or "", "note": old.get("note", "")})
    save(rows)
    return rows


def set_stage(chapters, stage, note=None):
    if stage not in STAGES:
        raise SystemExit(f"ledger: unknown stage {stage!r}; one of {', '.join(STAGES)}")
    rows = load()
    for chapter in chapters:
        if chapter not in rows:
            raise SystemExit(f"ledger: no chapter {chapter!r} (use OSIS.chapter, e.g. Matt.14)")
        rows[chapter]["stage"] = stage
        if note is not None:
            rows[chapter]["note"] = note
    save(rows.values())


def summary(rows, book_filter=None):
    """Lines describing each book: chapters, stages, and coverage by the witnesses."""
    lines = []
    for book in books.BOOKS:
        if book_filter and book.osis not in book_filter:
            continue
        mine = [row for row in rows if row["chapter"].rsplit(".", 1)[0] == book.osis]
        if not mine:
            continue
        stages = {}
        for row in mine:
            stages[row["stage"]] = stages.get(row["stage"], 0) + 1
        repo = {}
        for row in mine:
            if row["repo"] not in ("-", "ocr"):
                repo[row["repo"]] = repo.get(row["repo"], 0) + 1
        complete = lambda column: sum(1 for row in mine if row[column] != "-" and str(row[column]) == str(row["verses"]))
        partial = lambda column: sum(1 for row in mine if row[column] != "-")
        lines.append(
            f"{book.osis:7} {len(mine):4} ch  "
            + " ".join(f"{name}:{count}" for name, count in sorted(stages.items(), key=lambda kv: STAGES.index(kv[0])))
            + f"  | wikisource {partial('wikisource')} ch ({complete('wikisource')} full)"
            + f"  wordpress {partial('wordpress')} ch"
            + ("  | repo " + " ".join(f"{k}:{v}" for k, v in repo.items()) if repo else ""))
    return lines
