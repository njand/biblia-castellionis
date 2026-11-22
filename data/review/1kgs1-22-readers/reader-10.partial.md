# Reader 10 (1 Kings, leaves 412–414, rows 2414–2658): paused before reading

**Rows checked on the page: none.** `reader-10.partial.tsv` holds only the header. The next reader starts at
**row 2414**.

## What was found before the pause

1. **The page images do not match these leaves.** `sources/archive/crops/1738-page-0412.jpg`, `-0413.jpg` and
   `-0414.jpg` (downloaded 2026-11-21 20:50) show printed pages **350, 351 and 352** (*Cap. 18.19.*, *Cap. 19.20.*,
   *Cap. 20.*: 1 Kgs 18:24 – 20:26). The voted rows for those leaves are 1 Kgs 13:33 – 14:21 and the start of 15.
   `page_numbers.json` gives leaf 414 = page 344, which matches neither. So `archive.page_image`'s offset (hOCR leaf − 1)
   or the cached files are wrong here, and **no reading sheet for this range can be trusted until it is checked**
   (sheets 173–190 were not drawn yet when I stopped). Find the image that actually shows 13:33 – 14:21 before
   reading.
2. **Leaves 412 and 413 in the vote look like fragments.** Leaf 412 col. 0 (rows 2414–2465) repeats the left part
   of leaf 414 col. 0 (13:33–14:7, *ubus, sed etiatn iterum* … *tergun*), and leaf 412 col. 1 (rows 2466–2498) repeats
   the left part of leaf 414 col. 1 (14:7–14:13), lines cut short. Leaf 413 (rows 2499–2558) interleaves two
   fragments: lines 11–39 are the left part of 14:21–28 (the text leaf 415 col. 0 has in full), and lines 40–70 are
   15:1–8 (Abiam: *…us, duodevicesimo regni Ieroboami, Nabati filii…* to *…cesfit Asa*). Leaf 411 col. 1 (reader 9)
   likewise carries 15:2–13. These look like partial or overlapping scans (a folded or shifted leaf), not separate
   printed pages; they probably should be removed as duplicates once the real pages are seen. Leaf 414 (rows
   2559–2658) is the full text of 13:33 – 14:20 (*…Nadabus eius filius.*).
3. **Ch. 14 heading**: row 2566 `\c 14` is present; rows 2567–2570 (*Annates Israelitarum … Illius mors.*) are the
   end of the italic chapter summary and should be removed; row 2422 *capvt :* and rows 2423–2428 on leaf 412 are
   the same summary (fragment). Row 2567's `#1` belongs on row 2571 (*er id tempus*, drop capital P lost: 1750 reads
   *Per id tempus*).
4. 1750's text for this stretch is at `sources/archive/1750/text.txt` lines 49190–49340 (13:33 – 14:24), useful for
   the wording check.
