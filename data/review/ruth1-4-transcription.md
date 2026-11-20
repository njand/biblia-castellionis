# Ruth 1–4, phase 1: the transcription

*2026-11-19. The first book on decision 85's route (PLAN.md §4, phase 1). Gate: the printed text
`text/orig/draft/RUT.usfm` approved → `text/orig/RUT.usfm`. The readers' own notes: `ruth1-4-transcription-readers.md`.*

**Decision:** approved for now (Nathan, 2026-11-19: "Approve for now"); moved to `text/orig/RUT.usfm`, never
rewritten by code. Phase 2 next.

## How the lines were read

- **Leaves**: 1738 (archive.org `bibliasacraexseb01cast`) leaves **318–321**, found with `lines --heads`. Leaf 318
  opens with Judges 21:19–25 (not Ruth's); leaf 322 begins 1 Samuel.
- **Voted** with `python -m pipeline lines Ruth 1-4 --leaves 318-321`: 349 rows, words from 1738's OCR 1,572,
  1750 45, Wikisource 15, 1726 1, unknown 98; 36 doubts (`Ruth1-4.doubts.tsv`). **Two fixes to `ocrdraft.classify`**
  were needed first, both for leaf 318, where Ruth begins mid-page under Judges: the heading OCR'd as `cApvT i.`
  (a looser chapter pattern, taken only when a numeral alone follows it, so a line opening with *caput* is not caught),
  and the short title *RVTHA.* across the page's middle (narrower than the earlier rule's half page). Without them,
  chapter 1 was lost entirely. Tests pass (210).
- **Read** on the page by two readers (Reader A leaves 318–319, rows 2–154; Reader B leaves 320–321, rows 155–349),
  every line on its crop (sheets `Ruth1-4.voted-001` … `-025`), the whole pages for margins, indents and footnotes,
  doubtful places zoomed. Claude merged their rows and checked the open points on the page (below).
- **Result**: `data/witnesses/read-1738/Ruth1-4.tsv`, 320 text lines and 6 `%` rows (4 footnotes, 2 catchwords),
  1,720 words; `Ruth1-4.corrections.tsv`, 259 rows changed by the reading; **307 words** differ from the vote
  (beside the spacing and punctuation the OCR set wrong). One line the OCR lost was added (leaf 320, *imposuit.*,
  3:15); two rows that were halves of footnote lines were folded into their notes; one row, *ita,* under leaf 318's
  right column, is the catchword (leaf 319 opens *ita, meæ filiæ*) and is now a `%` row.
- **Verse numbers**: the vote's were wrong from 1:7 on (it had the KJV's) and throughout chapters 2–4; every number
  was placed again from 1738's margins. 1738 numbers chapter 1 **1–23** (the KJV 22); 2, 3 and 4 have the KJV's counts
  but cut differently. Wikisource's Ruth has 1738's numbering and agrees everywhere but 2:6 (below). One number placed by
  sense: 4:8 *Erat autem mos* (the margin lost in the gutter; 1750 and Wikisource agree).

## Checked by Claude on the page

- **2:6** (leaf 319, right column): 1738's "6" stands beside the line *adsit vobis Ioua. Cui illi: et tibi*, so 1738's
  2:6 begins at *Cui illi*; Wikisource begins it a line later at *Et Boozus*. The printed text follows the margin. It
  makes no difference to the edition: both land in the KJV's 2:4 and 2:5 after versifying.
- **1:14** *hærebat,etNoe-*: printed run together (no space after the comma or after *et*); kept as printed.
- **3:2** *pu-* / *ll is fuisti*: the hOCR and the page agree, a misprint for *puellis*; kept as printed (decision 58).
- **3:16**: an asterisk after *venit:* (*nit: \* quærentique*), but no footnote stands at the foot of leaf 320 or 321
  (the hOCR shows none either; 1750 has no mark). A mark without a note: taken out of the text like the other note
  marks, and listed here for phase 2.
- **Paragraphs**: `orig --read-lines` takes 1738's indents from the hOCR; against the readers' lists, two were missed
  (2:3 *Ita rus profecta*, 3:16 *Illa in oppidum*, each a column's first line, seen indented) and one was false (3:1
  *requiem tibi*, a line beside the drop capital). Recorded as `¶` / `¶-` rows in `data/decisions/Ruth.orig.tsv`.
  The printed text's paragraphs now match every indent the readers saw (15, with the chapter openings). For a book not
  yet settled `orig.verse_paragraph_rows` had no first word to check a `¶` row against (it reads the gold); it now
  falls back to the verse's first word as built.

## Footnotes and Castellio's marks (inputs for phase 2's notes)

1738's four footnotes, written as `%` rows with their exact printed text:

| Where | Letter | Hangs on | Note |
|---|---|---|---|
| 1:8 (leaf 318) | m) | *tum erga* ᵐ *mortuos* | *me, propter vestros maritos.* |
| 1:10 (leaf 318) | n) | *esse* ⁿ *reuersuras* | *hoc est, ituras cum ea reuertente. Nec enim reuertebantur ipsæ in Iudæam, quum in Iudæa numquam fuissent.* |
| 1:13 (leaf 319; 1738's 1:14) | a) | *Equidem* ᵃ *valde vestra caussa doleo* | *Inuita a vobis diuellor, sed cogit Ioua, qui me vestris maritis priuauerit.* |
| 1:20 (leaf 319; 1738's 1:21) | b) | ᵇ *Noemim vocare, vocate me Maram* | *Noemis ab amœnitate et iucunditate: Mara ab acerbitate et mœrore dicitur.* |

And the asterisk at 3:16 with no note (above). No *L.* … *H.* or *G.* … *H.* marks in Ruth. Whether these notes are
Castellio's (his 1554 annotations or margins, as Joshua's two were) is for phase 2's notes pass.

## Wording doubts (the printed text keeps 1738; the edition's choice is phase 2's)

Verses in the KJV's numbering, as the printed text now has them.

- 1:19 *ad quarum aduentum* (1750 *ad*); Wikisource *At quarum*.
- 2:10 *submisse* (1750 *submiffe*); Wikisource *sumisse*.
- 2:23 *famulas* (Wikisource too); 1750's OCR *famulos* (not checked on 1750's page).
- 3:3 *homini*; 1750's OCR *homine* (not checked on 1750's page).
- 4:4 *Tum ille: ego redimam* (1750 the same); Wikisource *Tum illa*, its own slip.
- 4:18 *Hezronem*, clearly printed; the vote and Wikisource *Hezeronem*.
- Forms kept as printed that phase 2 will normalize: *promsit*, *sumserit*, *redemturus* (twice), *exspecta*,
  *caussa*, *paullum*, *QuumqueBoozus* (no space), *Isæi*, *Isæum*, *Isæus*. Row by row in the readers' notes.

## Versification

`data/versification/Ruth1-4.draft.edits.tsv`: **59 edits, applied** to `text/draft/RUT.usfm` and the printed text
(decision 30's standing rule, each with the KJV's words that place it). Castellio recasts Ruth's sentences more freely
than the Pentateuch's, so many of the KJV's boundaries fall inside his verses: the edits move 1738's numbers to the
words where each KJV verse begins (1:3 *moritur Elimelechus*, 1:20 *dicebat*, 2:9 *et videto*, 4:10 *nec non Rutham*
…), join the verses he split (1:14 *Non ita* into the KJV's 1:13), and re-cut the genealogy (4:18–22, which 1738
numbers half a clause off the KJV's). The checks pass: the same words, the KJV's 22, 23, 18 and 22 verses.

## What was made

- `data/witnesses/read-1738/Ruth1-4.voted.tsv`, `.doubts.tsv`, `.tsv`, `.corrections.tsv`.
- `text/draft/RUT.usfm`: the draft in Wikisource's conventions, on the KJV's numbering, with the BSB's paragraphs
  (for phase 2).
- **`text/orig/draft/RUT.usfm`**: the printed text, every word from the read lines, 85 verses; its word counts match
  the draft's verse for verse. Each verse's leaf in `data/orig/Ruth.pages.tsv`.
- `data/decisions/Ruth.orig.tsv`: the three paragraph rows.
- The ledger: Ruth 1–4 `corrected`.

## On approval

Move `text/orig/draft/RUT.usfm` to `text/orig/RUT.usfm` (never rewritten by code after that), then phase 2:
`propose Ruth 1-4` and the notes search side by side.
