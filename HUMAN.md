# For Nathan

## Now

- **2026-11-05: all eight plan decisions taken** (below); `brief.md` and `PLAN.md` updated to match.
- **M0 (groundwork) is done** (commit 3badc59). `python -m pipeline` fetches every witness and keeps the chapter
  ledger.
- **Next: M1 (calibration).** Learn the spelling and macron rules from the finished chapters, align the OCR
  witnesses to verses, and build the test harness that scores the pipeline against your finished chapters.
  Then the Matthew 14–28 pilot, reviewed in full.

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

## How to run

```
python -m pipeline fetch all        # once; downloads are cached in sources/ (≈260 MB)
python -m pipeline status
python -m pipeline status Matt --chapters
```
