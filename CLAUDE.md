# Biblia Sacra ex Sebastiani Castellionis Interpretatione

A reader's edition of Sebastian Castellio's Latin Bible: Gaffiot 2016 orthography, full macrons, modern
paragraphs, poetry and quotation marks, KJV versification. `PLAN.md` describes the automated pipeline being
built; `brief.md` holds the editorial rules; `HUMAN.md` lists what waits on Nathan.

## Rules

- **Finished chapters are never rewritten by code.** A chapter that is live (not commented out) in
  `LaTeX/biblia/**/*.tex` is `settled` in `data/status.tsv`. The pipeline may check it and propose changes, never
  write to it. Nathan edits the LaTeX by hand (sometimes via Overleaf).
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
| `LaTeX/main.tex`, `LaTeX/biblia/{vetus,novum} foedus/<slug>.tex` | The published master (one file per book) |
| `scripts/latex_converter.py` | LaTeX → `TXT/3`, `TXT/4`, `HTML/`; keeps TXT chapters not yet in LaTeX |
| `EPUB/` | Built from the HTML chapter files (see the EPUB rebuild in git history, ca2f013) |
| `TXT/1 - OCR`, `TXT/2 - Post-Corrected` | Earlier manual stages (Google Books OCR of the 1726–27 edition) |
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
- UTF-8 throughout; the TXT and LaTeX files use precomposed macron vowels (ā, not a + ◌̄).

## Commands

```
python -m pipeline fetch all                 # Wikisource, WordPress, parallel Bibles, archive.org OCR
python -m pipeline fetch archive --hocr      # also the hOCR word boxes (14–40 MB per volume)
python -m pipeline status [BOOK…] [--chapters]
python -m pipeline latin macron vēnit        # W/M/G macron lookup (fur-fulminis)
python -m pipeline latin macron-check --text FILE
cd scripts && python latex_converter.py      # LaTeX → TXT/HTML
```

## Sources at a glance

- **Wikisource** (base text): NT complete; much of the OT. NT from the 1760 edition, OT from 1738; some books
  from other printings (Song of Songs keeps u for v; Obadiah has stress accents).
- **WordPress (2019)**: Gospels and Genesis 1–35, macronized: Nathan's earlier macron decisions.
- **archive.org OCR**: 1681, 1715, 1747, 1758 NT; 1738 OT; 1750 Bible.
- **Parallel**: KJV (versification), BSB (paragraphs, poetry `\q1/\q2`, quotation marks; see the `layout` column),
  WEB, Clementine Vulgate, SBLGNT, OSHB — parsed into `sources/parallel/<key>/<osis>.tsv`.
