# Biblia Sacra ex Sebastiani Castellionis Interpretatione

A reader's edition of Sebastian Castellio's Latin Bible: Gaffiot 2016 orthography, full macrons, modern
paragraphs, poetry and quotation marks, KJV versification. `PLAN.md` describes the automated pipeline being
built; `brief.md` holds the editorial rules; `HUMAN.md` lists what waits on Nathan.

## Rules

- **USFM is the master copy** (`text/<USFM code>.usfm`, one file per book; decided 2026-11-05). Every published
  format (website, EPUB, PDF via generated LaTeX, TXT) is generated from it; nothing generated is edited by hand.
  Until M1 migrates them, the finished chapters still live in `LaTeX/biblia/**/*.tex`.
- **Finished chapters are never rewritten by code.** A settled chapter (in `text/*.usfm`, or live in the LaTeX
  until the migration) may be checked and changes proposed, never written to, except to apply
  proposals Nathan has accepted, exactly as their `Apply` lines say (each checked to match once). Otherwise Nathan
  edits the USFM by hand.
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
| `text/draft/<USFM code>.usfm` | Drafted, unchecked chapters (Wikisource via `pipeline draft`; none at present; a draft in review has its `.preview.usfm` beside it); not settled. Once approved, a draft's chapters move into `text/<USFM code>.usfm` and the draft file goes (Matthew 14–28 settled 2026-11-07, Mark 6–16, Luke 14–24, John 5–21 and Genesis 28–50 2026-11-08, Romans 1–16, Acts 1–28 and Exodus 1–20 2026-11-09, 1 Corinthians 1–16 and 2 Corinthians 1–13 2026-11-10) |
| `data/review/*.md` | Proposals with exact **Apply** lines and **Decision** lines; applied by `python -m pipeline review apply` |
| `data/decisions/<osis>.layout.tsv`, `.forms.tsv` | Calls made by reading a verse, for `pipeline propose`: its quotation marks, `\qt`, poetry, paragraphs, capitals and punctuation over the draft's own words (`marks` `=` keeps the draft's, `-` none), and macrons decided in context, each with its reason |
| `data/rules/orthography.tsv` | Spelling rules (`old new scope status note`); only `approved` rows are applied. `REVIEW.md` beside it is the latest proposal for Nathan; `distinct.tsv` lists look-alike words decided to be different |
| `data/witnesses/ocr-<year>/<osis>.tsv` | OCR witnesses aligned to verse ids (`python -m pipeline align`): 1573 (MDZ hOCR, `pipeline/mdz.py`), 1681, 1715, 1726 (= `TXT/1`), 1738, 1747, 1750, 1758; flags `partial`/`missing`, `L…G: words` (Castellio's L. … G. marks), `canvas N` (1573) |
| `data/calibration/witnesses.md` | Each witness scored against the gold (found, agreement exact / f-s-blind / reading); `witnesses.tsv` holds the counts |
| `data/calibration/harness.md` | Stages 3–4 from Wikisource scored against the gold (`python -m pipeline harness`; leave-one-out) |
| `docs/editions.md` | The editions of Castellio's Bible (lifetime vs posthumous, purposes, what he changed vs later editors), for the README and front matter; keep it current as editions are examined |
| `data/calibration/nt1556.tsv` | Wikisource NT against the 1556 OCR (`scripts/collate_1556.py`; 1556 pages cached in `sources/erara-1556/`): differences confirmed by another printing |
| `data/calibration/nt1573.tsv` | 1573 against 1556, both OCRs aligned to Wikisource (`scripts/collate_1573.py`; 1573 hOCR pages cached in `sources/mdz-1573/<canvas>.hocr`, NT = canvases 747–960): every difference, with the printings that share each side; `nt1573-books.tsv` has the counts per book |
| `data/calibration/scans.md` | The editions compared (1551, 1554, 1556, 1573, 1745, 1758, 1760) and where their scans are; the evidence for the 1573 NT base |
| `data/calibration/wikisource.tsv` | Every difference between Wikisource and the gold, sorted by kind (`python -m pipeline rules`) |
| `data/gold/<osis>.tsv` | The settled chapters per verse (`id text marks layout`), rebuilt from `text/` by `python -m pipeline gold`; the harness's answer key |
| `build/` | Generated outputs (website, EPUBs, PDF, TXT/TSV); git-ignored; published via GitHub releases and Pages (`.github/workflows/`: `pages.yml` on every push to main, `release.yml` on a tag `v*`, notes in `RELEASE.md`) |
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
python -m pipeline migrate [BOOK…]           # LaTeX → text/*.usfm where none exists yet; always checks the round trip
python -m pipeline gold [BOOK…]              # text/*.usfm → data/gold/<osis>.tsv
python -m pipeline rules [BOOK…]             # learn spelling rules (keeps approved/rejected statuses)
python -m pipeline align [WITNESS…]          # OCR witnesses → verse ids, scored against the gold
python -m pipeline harness [BOOK…]           # normalize + macronize from Wikisource, scored (lexicon cached in sources/cache)
python -m pipeline versify Gen [--apply]     # KJV renumbering from data/versification/Gen.edits.tsv (apply: all approved)
python -m pipeline versify Matt --draft [--to COPY]   # the same for text/draft/ (Matt.draft.edits.tsv)
python -m pipeline review check|apply FILE… [--write] [--items N…] [--all] [--to COPY]   # Apply lines of data/review/*.md
python -m pipeline draft Mark 6-16            # stage 1: Wikisource → text/draft/MRK.usfm (never overwrites)
python -m pipeline collate Matt 14-28 [--base draft|settled|wikisource|FILE]   # stage 2 → data/calibration/<osis><CH>-collation.tsv
python -m pipeline propose Mark 6-16 [--rates] # stages 3–5 on an unmarked draft: one review item per verse → data/review/mark6-16-chNN.md + text/draft/MRK.preview.usfm
python -m pipeline build Matt Mark Luke John --version v1.0   # stage 7: text/ → build/ (site, EPUBs, PDF LaTeX, TXT/TSV/JSON)
cd scripts && python latex_converter.py      # legacy: LaTeX → TXT/HTML (until the USFM builds replace it)
```

## Sources at a glance

- **Base editions** (decisions 15 and 24): NT = the 1573 Basel edition (Perna, *ex postrema recognitione*; MDZ
  bsb10141277), the 1556 text revised further; 1556 (e-rara 10281656), Castellio's last lifetime edition, is the
  reference, its differing readings recorded as variants. OT = 1738 Leipzig. 1573 numbers the verses and its OCR
  is good: search `api.digitale-sammlungen.de/iiif/services/search/v1/bsb10141277?q=<word>`, hOCR
  `api.digitale-sammlungen.de/ocr/bsb10141277/<n>`, images
  `api.digitale-sammlungen.de/iiif/image/v2/bsb10141277_<00801>/<x,y,w,h>/800,/0/default.jpg` (Git Bash `curl`
  fails TLS to MDZ here; use PowerShell `Invoke-WebRequest` or the web-fetch tool).
- **Wikisource** (working text): NT complete; much of the OT. Cites 1760 for the NT, but its Gospels follow the
  1573/1758 line, its Acts–Revelation the early line (`data/calibration/scans.md`); OT from 1738; some books
  from other printings (Song of Songs keeps u for v; Obadiah has stress accents).
- **WordPress (2019)**: Gospels and Genesis 1–35, macronized: Nathan's earlier macron decisions.
- **archive.org OCR**: 1681, 1715, 1747, 1758 NT; 1738 OT; 1750 Bible.
- **Parallel**: KJV (versification), BSB (paragraphs, poetry `\q1/\q2`, quotation marks; see the `layout` column),
  WEB, Clementine Vulgate, SBLGNT, OSHB — parsed into `sources/parallel/<key>/<osis>.tsv`.
