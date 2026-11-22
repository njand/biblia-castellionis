# Reader 09 (partial, paused): leaves 409–411, rows 2247–2413

**No row was read on the page.** The pause came before any line was checked, so `reader-09.partial.tsv` holds
only the header. A later reader resumes from **row 2247**.

## What I found before pausing: the page images do not match the vote's leaves here

- The vote's rows for leaves 409–411 hold 1 Kgs 13:4 – 13:27 (leaf 409), fragments of 13:27 – 14:10 (leaf 410,
  18 rows) and fragments of 15:1 – 15:15 (leaf 411, 47 rows, with `\c 15` at row 2367).
- The page images `sources/archive/crops/1738-page-0409.jpg`, `-0410.jpg` and `-0411.jpg` (drawn 2026-11-21 20:49–20:50)
  show **printed pages 347, 348 and 349**: running heads *Cap. 16.*, *Cap. 17.*, *Cap. 18.*; 1 Kgs 16:6 – 16:31,
  16:31 – 17:23 (with *CAPVT XVII.*), 17:23 – 18:23 (with *CAPVT XVIII.* and footnotes h–k).
- The running heads of the images just before (checked, top strip only): 0405 = p. 343 *Cap. 13.*; 0406 = p. 344
  *Cap. 14.*; 0407 = p. 345 *Cap. 14. 15.*; 0408 = p. 346 *Cap. 15. 16.*
- So the text of my rows is on the images numbered about **0404–0407**, not 0409–0411 (13:4 is probably on p. 342 or
  343; not yet looked at). Either the hOCR leaves are misassigned in this stretch (the vote's leaf 410 and 411, with
  only 18 and 47 rows of broken text, look like OCR of a different or damaged image), or the image numbering is
  offset. `archive.page_image` fetches archive.org image `leaf - 1`; the offset here is about 4–5 leaves.
- Consequence: the reading sheets for these rows (about 161–173) crop `1738-page-0409…0411` by the vote's hOCR boxes,
  so their crops will show the wrong text (chs. 16–18) and cannot be used. Readers 08 and 10 should check the same
  thing in their ranges (where the vote's leaf and the image stop matching).
- Also: the vote has no `\c 14` row in this range (ch. 14 begins on printed p. 343/344, which the vote's leaf 410
  covers only in fragments); `\c 14` must be added when the range is read.

## For the resumer

Find the images that print 13:4 *quit, Iouam Deum tuum* through 15:15 (start with 0404–0407 and their neighbours),
read rows 2247–2413 on those, and record in the notes which image each row was read on. 1750's text of 13:4–15:3 is at
`sources/archive/1750/text.txt` lines ≈49060–49400 (for wording doubts only).
