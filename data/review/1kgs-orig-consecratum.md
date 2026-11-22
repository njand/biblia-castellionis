# 1 Kings 7:51 and 22:34 in the printed text: two phase-1 misreadings

*2026-11-22.* Found by verse reader r3 in phase 2 (`1kgs1-22-phase2/r3.md`), after the printed text was approved for
now. The phase-1 reader read *confe-|cratum* and *repo-|fuit.* (`data/witnesses/read-1738/1Kgs1-22.tsv`, leaf 399,
column 1, lines 99–103; reader 05's rows 1346 and 1300). The page prints **conse-|cratum** and **repo-|suit.**: seen
by Claude on the crop of the five lines, both letters are the long *ſ* with no crossbar, as *abſoluit*, *ſuo*, *vaſa*,
*fiſcum* in the same lines, against the barred *f* of *fiſcum*. Neither *confecratum* nor *repofuit* is a Latin word.
The read lines are corrected with it (reader 05's rows, merged again), and the draft (`1kgs1-22-draft-fixes.md` §3).

1. **1 Kgs 7:51** *confecratum* → *consecratum*, *repofuit* → *reposuit* (`text/orig/1KI.usfm`).
    **Apply:** `1Kgs.7.51` la: `Solomo, confecratum a` → `Solomo, consecratum a`
    **Apply:** `1Kgs.7.51` la: `ibique repofuit.` → `ibique reposuit.`
    **Decision:** accept (Nathan, 2026-11-22)

2. **1 Kgs 22:34** *lorieam* → *loricam* (`text/orig/1KI.usfm`). Found by verse reader r9 (`1kgs1-22-phase2/r9.md`).
   The phase-1 reader read *lori-|eam* (leaf 428, column 0 line 53 and column 1 line 55, a footnote between; reader 15's
   row 3993). The page prints **cam** at the head of column 1 line 55: seen by Claude on the crop, a *c* with no bar,
   as the *c* of *flectat* below it. *lorīcam*, the breastplate (Hebrew הַשִּׁרְיֹן). The read line is corrected and
   merged again, and the draft (`1kgs1-22-draft-fixes.md` §3).
    **Apply:** `1Kgs.22.34` la: `et lorieam vulnerauit` → `et loricam vulnerauit`
    **Decision:** accept (Nathan, 2026-11-22)

To apply once accepted: `python -m pipeline review apply data/review/1kgs-orig-consecratum.md --items 1 2 --to
text/orig/1KI.usfm --write`.
