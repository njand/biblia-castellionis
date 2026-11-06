# For Nathan

## Now

- **2026-11-05: all nine plan decisions taken** (below); `brief.md`, `PLAN.md` and `CLAUDE.md` updated to match.
  Decision 9 makes USFM the master copy: LaTeX becomes a generated print output and Overleaf editing ends.
- **M0 (groundwork) is done** (commit 3badc59). `python -m pipeline` fetches every witness and keeps the chapter
  ledger.
- **M1 (calibration) is in progress** in its own session. It starts by migrating the finished LaTeX chapters to
  USFM (shown lossless by converting back), then learns the spelling and macron rules, aligns the OCR witnesses
  and builds the test harness. Then the Matthew 14–28 pilot, reviewed in full.

## Decisions waiting

- None. (README and `LICENSE` brought in line with the decisions on 2026-11-05.)

## Decided

| # | Date | Decision |
|---|---|---|
| 1 | 2026-11-05 | **Base edition: the editions Wikisource follows** (1760 NT, 1738 OT). Other printings' differing readings are recorded as variants. Wording in the finished chapters (from 1726–27) that differs is proposed for review, never changed automatically. |
| 2 | 2026-11-05 | **Apocrypha: in scope, after the 66 books** (M7). Placement decided then. |
| 3 | 2026-11-05 | **Chapter summaries: included** as small italic headings under each chapter number, normalized and macronized like the text. |
| 4 | 2026-11-05 | **Quotation marks: “…” for direct speech, ‘…’ only for quotes within it; reported discourse unmarked.** About 33 reported passages in the finished chapters lose their ‘…’ (proposed for review). |
| 5 | 2026-11-05 | **Versification: KJV everywhere**, mappings recorded; Psalm titles unnumbered above verse 1. |
| 6 | 2026-11-05 | **Review: strict pilot, then relax.** Every change is reviewed during Matthew 14–28. The auto-apply policy (sources agree on audible macrons, two-scan corrections, approved spelling rules, with a 1-in-10 full read) starts once the measured error rate is acceptable. |
| 7 | 2026-11-05 | **License: CC BY-SA 4.0**, crediting Wikisource and the scan libraries. |
| 8 | 2026-11-05 | **Latin databases used in place** from `../fur-fulminis/data` (`LATIN_REF_HOME` to move them). |
| 9 | 2026-11-05 | **USFM is the master copy** (`text/<book>.usfm`). The website, EPUBs, print PDF (generated LaTeX in your current layout), TXT and an ebible.org submission are all built from it (PLAN.md §4a). Overleaf editing ends; the old LaTeX/HTML/EPUB/TXT folders retire once the migration is verified (removal is your call). |

## How to run

```
python -m pipeline fetch all        # once; downloads are cached in sources/ (≈260 MB)
python -m pipeline status
python -m pipeline status Matt --chapters
```
