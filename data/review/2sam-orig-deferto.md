# 2 Samuel 14:10 in the printed text: *deferto*, not *deserto*

*2026-11-21.* Found by proofreader p3 in phase 2 (`2sam1-24-phase2/p3.md`), after the printed text was approved for
now. The phase-1 reader read *deserto* (`data/witnesses/read-1738/2Sam1-24.tsv` row 1392, leaf 371, column 1, line 58).
The page prints **deferto**: seen by Claude on the crop of the line, the letter has the *f*'s full crossbar, as *faxo*
in the same line, against the long *ſ* of *ſolio* and *ſi* in the line above. The hOCR reads *deferto* (1726's OCR
*deferco*), and the sense needs *dēfertō ad mē*, "bring him to me" (Hebrew וַהֲבֵאתוֹ אֵלַי; Vulgate *adduc eum ad
me*). The read line is corrected with it, and the draft (`2sam1-24-draft-fixes.md` §1.9).

1. **2 Sam 14:10** *deserto* → *deferto* (`text/orig/2SA.usfm`).
    **Apply:** `2Sam.14.10` la: `mutiat, deserto ad me` → `mutiat, deferto ad me`
    **Decision:** accept (Nathan, 2026-11-21: "Approve all")

To apply once accepted: `python -m pipeline review apply data/review/2sam-orig-deferto.md --items 1 --to
text/orig/2SA.usfm --write`.
