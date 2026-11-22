# 1 Kings readers: where each range stands (2026-11-21)

Fifteen readers were started at once to use a quota window before a reset; the window was missed, so readers
02–15 were paused and saved what they had read in `reader-NN.partial.tsv` / `.partial.md`. The ranges are
finished one reader at a time from the resume row below.

**Image offset (fixed 2026-11-21).** archive.org photographed some 1738 pages again; its page images skip those
leaves (hOCR leaves 386–389, 410–413, 424–425; also 830–831), but `archive.page_image` assumed image = leaf − 1, so
from leaf 386 on every cached page image and reading sheet showed a page four (later eight, ten) leaves on. Now
`archive.skipped_leaves` counts only the kept leaves. The wrong images and sheets were set aside in
`sources/archive/crops/misnamed-2026-11-21/` and redrawn. **Image names in the partial notes are the old ones**:
where a reader writes "page-0390 = leaf 394", the page now is `1738-page-0394.jpg`. The readers who read did so from
the right page (matched by running head and text), so their rows stand.

**The skipped leaves' rows are duplicates** (or fragments) of pages printed on other leaves and are removed in the
reading: rows 39–354 except leaf 385's (leaves 386–389; reader 02 removed 227–354), rows 2349–2558 (leaves 410–413),
rows 3539–3744 (leaves 424–425), to be confirmed on the pages by the readers of those ranges.

| Reader | Leaves | Rows | State (2026-11-21, evening) |
|---|---|---|---|
| 01 | 385–387 | 2–226 | done (`reader-01.partial.*`, the whole range; leaves 386–387 are first shots of pp. 324–325, see below) |
| 02 | 388–390 | 227–458 | done (`reader-02.partial.*`; 227–354 removed as duplicates) |
| 03–08 | 391–408 | 459–2246 | done (`reader-NN.tsv/.md`, the partial's rows plus the rest) |
| 09–10 | 409–414 | 2247–2658 | done (`reader-09.tsv`, `reader-10.tsv`, `reader-09-10.md`; 410–413 removed as duplicates) |
| 11–13 | 415–423 | 2659–3538 | done |
| 14 | 424–426 | 3539–3842 | done (424–425 removed as duplicates) |
| 15 | 427–429 | 3843–4063 | done (2026-11-22; `reader-15.tsv/.md`; 1 Kings ends at row 4063 on leaf 429, 2 Kings follows below the rule) |

Then: merge (a `merge.py` like 2 Samuel's, reading the `.partial` files for 01–02 and the combined files for 09–10),
compare reader 01's pp. 324–325 with 02/03's, make the verse placement around *Cui …* consistent (readers 12/13
differ), and write `1kgs1-22-transcription-readers.md`.

**Pages 324–325 were read twice.** Reader 01 read them from leaves 386–387 (the first shots; the OCR unusable,
nearly every row retyped), readers 02 and 03 from leaves 390–391 (the clean shots, rows 355–555). archive.org keeps
390–391, so the merge takes 02/03's rows and removes 386–387's (rows 39–226 less leaf 385's); reader 01's reading
of the same pages is then a second reading to compare word for word, every difference looked at on the page.
Reader 01 notes that 387 col. 1 ends *quo cincta latera … cru-* (2:5), lines the vote has only under leaf 391.

Points raised for checking on the page are in each `.partial.md` (e.g. reader 08: row 2214 `\c 10` is really
`\c 13`; reader 02: the rest of p. 323 col. 1, 1:8–9, is missing from the vote; reader 15: leaf 429 col. 1 is cut
at the right in the OCR).

**Merged 2026-11-22** (`merge.py --write`): `data/witnesses/read-1738/1Kgs1-22.tsv` (3309 rows) and `.corrections.tsv` (2450 changed, 19 added, 772 removed). Reader 01's second reading of pp. 324–325 agreed with 02/03's in every word but one, row 486 (1:44): the page prints *cumque*, so 03's *eumque* was corrected. Still to do: the verse placement around *Cui …* (readers 12/13), reader 15's *Iou mque* (4057, a letter that did not print), and `1kgs1-22-transcription-readers.md`.
