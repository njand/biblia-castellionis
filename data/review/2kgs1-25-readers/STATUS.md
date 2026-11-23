# 2 Kings readers: where each range stands

*Begun 2026-11-22 on Nathan's "Start transcribing the next book".* `pipeline lines 2Kgs 1-25 --leaves 429-460`:
3086 lines (rows 2–3087), voted with 1750 only; 0 doubts; the vote found no `\c 23`. Eleven readers, three leaves
each, run **one at a time** with the quota checked before each (`BRIEF.md`).

| Reader | Leaves | Rows | State |
|---|---|---|---|
| 01 | 429–431 | 2–259 (sheets 001–019) | done (263 rows: 5 added; four points to check on the page, `reader-01.md`) |
| 02 | 432–434 | 260–556 (019–040) | done (298 rows: 1 removed, 2 added; ch. 3 has 28 verses in 1738, `reader-02.md`) |
| 03 | 435–437 | 557–854 (040–061) | done (298 rows: 3 removed, 3 added; ch. 6 has 34 verses in 1738, `reader-03.md`) |
| 04 | 438–440 | 855–1147 (061–082) | done (297 rows: 4 added; ch. 8 has 30 verses in 1738, ch. 9 numbered differently at 19–21, `reader-04.md`) |
| 05 | 441–443 | 1148–1443 (082–103) | done (295 rows: 4 removed, 3 added; ch. 10 divided differently, ch. 11 has 20 verses (KJV 11:21 = 1738 12:1), `reader-05.md`) |
| 06 | 444–446 | 1444–1736 (103–123) | done (292 rows: 3 removed, 2 added; 13:2–24 margins lost in the gutters, placed by sense, `reader-06.md`) |
| 07 | 447–449 | 1737–2033 (123–144) | done (296 rows: 3 removed, 2 added; ch. 15 has 37 verses (KJV 15:38 = 1738 16:1), ch. 17 runs four behind from 15, `reader-07.md`) |
| 08 | 450–452 | 2034–2326 (144–165) | done (295 rows: 5 removed, 7 added; ch. 17 catches up to the KJV by splitting verses, ends 19:15; `reader-08.md`) |
| 09 | 453–455 | 2327–2617 (165–186) | done (294 rows: 2 removed, 5 added; ch. 20 has 20 verses (KJV 20:21 = 1738 21:1), ch. 21 has 25 (KJV 21:26 = 1738 22:1); ends 22:3, `reader-09.md`) |
| 10 | 456–458 | 2618–2916 (186–207) | done (298 rows: 4 removed, 3 added; `\c 23` found at row 2699 (the vote had `\c 21`); ch. 22–24 divided differently; ends 24:8, `reader-10.md`) |
| 11 | 459–460 | 2917–3087 (207–219) | done (167 rows: 6 removed, 2 added; ch. 24 and 25 have the KJV's counts, divided differently at 24:12–16, 25:16–17, 25:21–22; ends 25:30 *diu vixit.*, `reader-11.md`) |

Merged 2026-11-22 (`merge.py`: 3093 rows, 2305 changed, 38 added, 31 removed; two of Claude's corrections after
looking at the readers' doubts on the page, `FIXES`); notes compiled in `../2kgs1-25-transcription-readers.md`;
`draft --from-ocr` and `orig --read-lines` built. Versification by three aligners, one at a time (`ALIGN.md`):

| Aligner | Chapters | State |
|---|---|---|
| 1 | 1–8 | done (73 edits: 35 split, 38 merge; `align-1.md`) |
| 2 | 9–17 | done (76 edits: 37 split, 37 merge, 2 chapter; `align-2.md`) |
| 3 | 18–25 | done (58 edits: 26 split, 28 merge, 4 chapter; `align-3.md`) |

Applied 2026-11-22 (`versify 2Kgs --draft --apply`: 207 edits, checks passed; the file renamed
`2Kgs1-25.draft.edits.tsv`; 11:16's printed anchor corrected to *Illi,iniectis*); printed text rebuilt on the KJV's
numbering; paragraphs checked (`data/decisions/2Kgs.orig.tsv`, 41); a third correction (row 253 *conuocàuerit*) in
`FIXES`. Summary for Nathan: `../2kgs1-25-transcription.md`.
