# Biblia Sacra ex Sebastiani Castellionis Interpretatione

A reader's edition of Sebastian Castellio's Latin Bible: Gaffiot 2016 orthography, full macrons, modern
paragraphs, poetry and quotation marks, KJV versification. `PLAN.md` describes the automated pipeline being
built; `brief.md` holds the editorial rules; `HUMAN.md` lists what waits on Nathan.

## Rules

- **USFM is the master copy** (`text/<USFM code>.usfm`, one file per book; decided 2026-11-05). Every published
  format (website, EPUB, PDF via generated LaTeX, TXT) is generated from it; nothing generated is edited by hand.
  Until M1 migrates them, the finished chapters still live in `LaTeX/biblia/**/*.tex`.
- **Finished chapters are never rewritten by code.** A settled chapter (in `text/*.usfm`, or live in the LaTeX
  until the migration) may be checked and changes proposed, never written to. Nathan edits the USFM by hand.
- **Propose, don't silently change.** Every judgment (a reading, a spelling, a macron, a quotation boundary)
  goes into a reviewable file with its evidence. Only rules Nathan has approved are applied without review.
- **Cite only evidence actually seen** (a witness's reading, a tool's output, a page image). If a tool returns
  nothing, say so.
- **Gaffiot 2016 is CC BY-NC-ND.** Use its answers (via `python -m pipeline latin macron`) to decide; never copy
  its text into this repo.
- **Wikisource text is CC BY-SA 4.0.** Keep `data/witnesses/wikisource/MANIFEST.tsv` (page and revision) current;
  the edition must credit Wikisource.
- **The fur-fulminis databases are read-only**, reached only through `python -m pipeline latin …`.
- Commit only when Nathan asks.

## Layout

| Path | What |
|---|---|
| `text/<USFM code>.usfm` | **The master copy**, one file per book (created by the M1 migration); markers in PLAN.md §3 |
| `build/` | Generated outputs (website, EPUBs, PDF, TXT/TSV); git-ignored; published via GitHub releases and Pages |
| `LaTeX/main.tex`, `LaTeX/biblia/{vetus,novum} foedus/<slug>.tex` | *Legacy* master, until the migration is verified; `main.tex`'s preamble is reused for the generated PDF |
| `scripts/latex_converter.py`, `HTML/`, `EPUB/`, `TXT/3`, `TXT/4` | *Legacy* outputs of the LaTeX; retired after the migration (removal is Nathan's call) |
| `TXT/1 - OCR`, `TXT/2 - Post-Corrected` | Earlier manual stages (Google Books OCR of the 1726–27 edition); now witnesses |
| `pipeline/` | The pipeline package: `python -m pipeline --help` |
| `data/witnesses/<source>/<osis>.tsv` | Parsed witnesses, one row per verse: `id  text  flags` (committed) |
| `data/witnesses/archive.tsv` | The archive.org editions and their OCR files |
| `data/versification/kjv.tsv` | KJV verses per chapter: the target numbering |
| `data/status.tsv` | The chapter ledger (stage, earlier repo work, witness coverage) |
| `sources/` | Raw downloads, cached; git-ignored; rebuilt by `python -m pipeline fetch all` |

## Conventions

- Verse ids are OSIS: `Matt.14.3`. Verse 0 is a chapter's summary (argumentum) or a psalm title.
  Books are listed in `pipeline/books.py` (OSIS code, USFM code, repo slug, Wikisource page, WordPress slug).
- Chapter stages: pending → fetched → aligned → corrected → normalized → macronized → structured →
  in-review → approved → settled. Move a chapter with `python -m pipeline ledger set Matt.14 --stage aligned`.
- Python 3.12, standard library only. Tests: `python -m unittest discover -s pipeline/tests -t .`
- UTF-8 throughout, with precomposed macron vowels (ā, not a + ◌̄). In USFM, quotation marks are the characters
  themselves (“…”, ‘…’), not LaTeX's ``…''.

## Commands

```
python -m pipeline fetch all                 # Wikisource, WordPress, parallel Bibles, archive.org OCR
python -m pipeline fetch archive --hocr      # also the hOCR word boxes (14–40 MB per volume)
python -m pipeline status [BOOK…] [--chapters]
python -m pipeline latin macron vēnit        # W/M/G macron lookup (fur-fulminis)
python -m pipeline latin macron-check --text FILE
cd scripts && python latex_converter.py      # legacy: LaTeX → TXT/HTML (until the USFM builds replace it)
```

## Sources at a glance

- **Wikisource** (base text): NT complete; much of the OT. NT from the 1760 edition, OT from 1738; some books
  from other printings (Song of Songs keeps u for v; Obadiah has stress accents).
- **WordPress (2019)**: Gospels and Genesis 1–35, macronized: Nathan's earlier macron decisions.
- **archive.org OCR**: 1681, 1715, 1747, 1758 NT; 1738 OT; 1750 Bible.
- **Parallel**: KJV (versification), BSB (paragraphs, poetry `\q1/\q2`, quotation marks; see the `layout` column),
  WEB, Clementine Vulgate, SBLGNT, OSHB — parsed into `sources/parallel/<key>/<osis>.tsv`.
