# 1 Kings 1–22, phase 1: the transcription

*2026-11-22. Decision 85's phase 1 (PLAN.md §4), on Nathan's "Start transcribing the next book". Gate: the printed
text `text/orig/draft/1KI.usfm` approved → `text/orig/1KI.usfm`. The readers' own notes, with Claude's settlements at
their head: `1kgs1-22-transcription-readers.md`; their rows, the readers' and aligners' briefs and reports, `STATUS.md`
and the merge script: `1kgs1-22-readers/`.*

**Decision:** approved for now (Nathan, 2026-11-22: "Approve for now", after the paragraphs were checked on his "Check the paragraphs"); `text/orig/draft/1KI.usfm` moved to `text/orig/1KI.usfm`. Phase 2 next.

## For you

1. **Approve the printed text for now?** `text/orig/draft/1KI.usfm`: every word from the lines read on the page, on
   the KJV's numbering, 816 verse ids (the KJV's 816), 15,024 words, the same as the draft's verse for verse; 73
   paragraphs (each chapter's start and 51 indents, checked against the readers' lists, below). Castellio's *G.*, *L.*, *H.* marks are printed as 1738 has
   them; the footnotes are not.
2. **The versification** (196 edits, `data/versification/1Kgs1-22.draft.edits.tsv`: 95 split, 98 merge, 3 chapter;
   applied to the draft and the printed text; decision 30's standing rule). Made by three aligners one after another
   (1–8, 9–15, 16–22; reports `1kgs1-22-readers/align-1.md` … `align-3.md`), each tested on both texts; the checks
   pass (the same words, the KJV's verse counts). Calls you may want to see:
   - **Three chapter breaks moved**, each where 1738's chapter opens with the end of the KJV's last verse before:
     2/3 (*Confirmato regno,* = KJV 2:46b; ch. 3 now opens *Solomo adfinitatem*), 12/13 (1738's 13:1 *Quum autem ad
     aram … adscendisset:* = KJV 12:33; ch. 13 opens *supervenit*), 14/15 (*Huic in regnum successit Abiamus ejus
     filius,* = KJV 14:31b; ch. 15 opens with the relative clause *qui anno duodevicesimo …*, in lower case). The
     draft sets `\p` after each new `\c`, though each falls mid-sentence: phase 2's layout to settle.
   - **Ch. 22 from 44**: 1738 follows the Hebrew's numbering (one ahead of the KJV); its 44 *quamquam sacella* joins
     the KJV's 43.
   - **22:22** opens at *Quo pacto?* (KJV *Wherewith?*), not at 1738's margin (*Ibo*).
   - Left as Castellio divides, one Latin sentence across two KJV verses with no clear place for the second: 1:47–48,
     6:21–22, 8:12–13, 8:41–42, 16:9–10, 16:15–16, 17:8–9; speech introductions ending a verse stay there.
3. Nothing else waits on you in phase 1. Phase 2 has the slips, the footnotes and asterisks, and Castellio's marks.

## How the lines were read

- **Leaves**: 1738 (archive.org `bibliasacraexseb01cast`) leaves **385–429** (pp. 323–357). The book begins on leaf
  385 under *REGVM LIBER III.* and ends at the top of leaf 429 (*patris exemplo læsit.*), above *REGVM LIBER IIII.*
  Wikisource has no 1 Kings; 1750 was the only other voter.
- **Voted** with `python -m pipeline lines 1Kgs 1-22 --leaves 385-429`: 4,062 lines, among them the hOCR's second
  shots of pages archive.org photographed twice (below).
- **Read** on the page by fifteen readers, three leaves each. All fifteen started at once to use a quota window
  (2026-11-21); the window was missed, the readers saved what they had (`reader-NN.partial.*`) and the ranges were
  finished one reader at a time. The three aligners ran one after another, the rest was done here.
- **Result**: `data/witnesses/read-1738/1Kgs1-22.tsv`, 3,309 rows: 22 chapter rows, 15 lettered footnotes and 6
  signatures or catchwords as `%` rows. `1Kgs1-22.corrections.tsv`: 2,450 changed lines, 19 added, 772 removed (732
  of them the second shots; the rest running heads, the OCR's second readings of line ends, an ornamental rule). The
  vote's verse numbers were placed again from 1738's margins.

## The image offset (fixed) and the twice-photographed pages

archive.org photographed some 1738 pages again; its page images leave out those hOCR leaves (386–389, 410–413,
424–425, also 830–831), but `archive.page_image` took image = leaf − 1, so from leaf 386 on every cached image and
reading sheet showed a page four, eight or ten leaves on. Readers 05, 09, 10, 14 found it. **Fix**:
`archive.skipped_leaves` reads the gaps in `page_numbers.json`, `page_image` counts only the kept leaves and returns
None for a skipped one, `sheet` passes over those; the wrong images and sheets were set aside in
`sources/archive/crops/misnamed-2026-11-21/` and redrawn (heads checked on images 0394, 0414, 0426). Tests pass (218).

The skipped leaves' rows repeat pages printed on other leaves and were removed after the readers compared them:
rows 39–354 except leaf 385's, 2349–2558, 3539–3744. Pages 324–325 were read on both shots (reader 01 on leaves
386–387, readers 02/03 on 390–391): the 1,049 words agree but one, 1:44, where leaf 391 prints *cumque eo misit*
(03's *eumque* corrected; Claude, on the page).

## Checked by Claude on the page

- **1:44 *cumque*** (above). **18:18**: the wide space on the margin-*18* line stands before *Cui ille*, so the verse
  opens there (leaf 419 col. 1), as 19:10 and 19:14 *Cui*. **22:5**: margin lost in the gutter; wide spaces before
  both *Cui Iosaphatus* and *Sed tibi censeo* (leaf 427 col. 0); kept at *Sed tibi*, where the KJV and the Hebrew
  begin 5. **22:52 *Iou mque*** (KJV numbering): the *a* did not print (reader 15, at 5×); kept as printed, as Ruth 3:2 *ll is*.
- **Readers 09–10 removed rows 2466–2468**, specks above a running head, against the brief's rule to keep an
  unmatched line: not text.

## Paragraphs (checked 2026-11-22, on Nathan's "Check the paragraphs")

`orig --read-lines` took 65 paragraphs from the hOCR's indents; the readers list 73 (the 22 chapter openings and
51 indents, every line of the book looked at). Every difference was seen on the page:
- **Ten indents the hOCR missed**, each set in beside its margin number after a short line, or at the head of a
  page: 1:15 *Tum Bethsaba*, 1:38 *Deinde Sadocus*, 3:15 *Tum expergefactus*, 4:29 *Fuit autem*, 6:7 *Templum saxo*
  (the footnote letter *c* stands in the indent), 7:7 *Fecit et iudicialem*, 7:13 *Curauit*, 13:11 *Erat Bethele*,
  14:21 *At Roboamus* (top of p. 345), 16:6 *Postquam Baasa* (top of p. 347).
- **Two false**: 7:35 *et in eiusdem* starts flush (the *7* before it is the margin's *37*); 16:2 *quoniam tu* is set
  in beside the drop capital *I* of 16:1, as 2 Samuel's 21:1.
- Recorded in `data/decisions/1Kgs.orig.tsv` (¶ and ¶-), the printed text rebuilt: 73 paragraphs, the words
  unchanged (the same as the draft's, verse for verse). Tests pass.
- The three moved chapter breaks open their paragraphs where the KJV's chapter now begins (3:1 *Solomo*, 13:1
  *superuenit*, 15:1 *qui anno*), not at 1738's drop capitals (*COnfirmato*, *Quum autem ad aram*, *Huic in regnum*),
  as 2 Samuel's printed text does at 14:1 and 20:1.

## Footnotes and Castellio's marks (inputs for phase 2's notes)

- **15 lettered footnotes**, each a `%` row with its printed text, its letter taken out of the text row; the word each
  hangs on is in the readers' notes. 1738 restarts its letters: *b)*, *c)* (4:13, 5:17; no *a)* found before them),
  *a)*–*k)* (11:5 *Melcomum*: *idem mox Molochus adpellatur.* … 18:21 *ambigua sententia nutatis?*), *a)*–*c)*
  (20:34 *vbi publicanos colloces …*, 21:7, 22:34 *simpliciter*: *in incertum.*). Glosses mostly; 4:13 *Argobiæ*:
  *Gaulonim vocat Iosephus.*; 15:6 *f) H. Roboamum.* gives the Hebrew's name beside *L. Abiamum H.*
- **Castellio's marks**, printed in the text: *L. … H.* 1:8 (*et Cerethæi et Phelethæi*), 11:5 (*et Chamosum
  Moabitarum*), 15:6 (*Abiamum*, with footnote *f)*); *G. … H.* 2:12 (*natus annos duodecim*); *G. L. … H.* 2:28
  (*Solomonem*), 18:22 (*G. L. lucanique vates quadringenti. H.*).
- **Asterisks with no footnote** (5:9; 6:2, 6:4, 6:5, 6:23, 6:31; 7:2, 7:15, 7:21, 7:28–30 and more in ch. 7; 10:11;
  15:13; 19:3; 21:24; 22:30), taken out and listed in the readers' notes, by 1738's numbering. As in 1–2 Samuel,
  phase 2 checks them against Castellio's 1554 annotations *IN LIBROS REGVM*.

## Wording doubts (the printed text keeps 1738; the edition's choice is phase 2's)

- **10:27 *auri*** where the Hebrew has silver; 1750 the same: Castellio's, perhaps, for a note.
- Misprints kept: 3:1 *intera*; 6:8 *lanuas* (*Ianuas*); 6:27 *in templa* (*templo*); 11:38 *tib*; 17:1 *adparco*;
  18:17 *est tune*; 20:14 *promitit*; 22:52 *Iou mque* (KJV numbering). Otherwise 1738 and 1750 differ mostly in spelling and stops (readers'
  notes, by row).

## Corrected after approval (2026-11-22)

Two phase-1 misreadings found by phase 2's verse readers, checked by Claude on the page and accepted by Nathan
(`1kgs-orig-consecratum.md`): 7:51 *confecratum*, *repofuit* → *consecratum*, *reposuit* (long ſ read as f); 22:34
*lorieam* → *loricam*. Applied to `text/orig/1KI.usfm`; the read lines were corrected with them.
