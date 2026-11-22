# 1 Kings 1–22, phase 1: the readers' notes

The fifteen readers' notes as written (2026-11-21/22), three leaves each, for `1kgs1-22-transcription.md`. Row
numbers are those of `data/witnesses/read-1738/1Kgs1-22.voted.tsv` (and of the `row` column of
`1Kgs1-22.corrections.tsv`); verse numbers are 1738's. Image names in readers 02–14's notes written before the
image-offset fix (`STATUS.md`) may be the old ones; the rows were read from the right pages. The readers' rows, the
brief, `STATUS.md` and `merge.py` are in `data/review/1kgs1-22-readers/`.

## Settled by Claude at the merge (2026-11-22)

- **Pages 324–325 read twice** (reader 01 from leaves 386–387, readers 02/03 from 390–391): the 1049 words agree
  but one, row 486 (1:44): leaf 391 prints *cumque eo misit*; 03's *eumque* corrected.
- **18:18 at *Cui ille*** (row 3119): the wide space on the margin-*18* line stands before *Cui*, not before *non*
  (leaf 419 col. 1, looked at); `#18` moved, as readers 13's 19:10 and 19:14 *Cui* (KJV *And he answered*).
- **22:5 at *Sed tibi censeo*** (row 3875; margin lost in the gutter): wide spaces stand before both *Cui
  Iosaphatus* and *Sed tibi* (leaf 427 col. 0, looked at); kept at *Sed tibi*, where the KJV and the Hebrew begin 5
  (Jehoshaphat's *Enquire*).
- **Row 4057 *Iou mque*** (22:50): the *a* did not print (reader 15); kept as printed (decision 58, as Ruth 3:2
  *ll is*); the edited text has *Iouamque* (1750).
- **Row 1300 *fuit.*** moved to the foot of leaf 399 col. 1 (reader 05).
- **Signatures and catchwords** are kept as `%` rows, as every reader wrote them.
- Readers 09–10 removed rows 2466–2468 (marks above the running head), against the brief's rule to keep an
  unmatched line; they are not text.

---

## reader-01 (`reader-01.partial.md`)

## Reader 01: rows 2–226 (1 Kgs 1:1 – 2:5, to *balteum*), plus the two last lines of leaf 387

Written as `reader-01.partial.tsv` at the coordinator's request. Every row is read on the matching page image, so this
"partial" file in fact covers the **whole range**: the last good row is **226**, and the rows after it (`+` 914–916)
are the two lines of p. 325 the vote does not have under leaf 387.

### Which images match which voted leaves

I checked the running head, page number and text of each image against the rows:

| Image | Printed page | Voted leaf | Match |
|---|---|---|---|
| `1738-page-0385.jpg` | 323 (end of 2 Sam.; *REGVM LIBER III.*, *CAPVT I.*, 1:1–9) | 385 (rows 2–38) | yes |
| `1738-page-0386.jpg` | 324 (*Cap. I.*, 1:9–37) | 386 (rows 39–145) | yes: same text, but the OCR is poor and interleaves col. 0 (labelled column 1, lines 7–57) with col. 1 (lines 59–110) |
| `1738-page-0387.jpg` | 325 (*Cap. I. 2.*, 1:37 – 2:5) | 387 (rows 146–226) | yes: same page, but the OCR is mostly garbage, and col. 1's ch. 2 lines (OCR lines 68–93) are labelled column 0 |
| `1738-page-0388.jpg` | 326 (2:5–) | **392** (row 556 *ntauit. Tu pro tua prudentia*) | **no**: voted leaves 388–391 are OCR of pp. 324–325 again (388: 324 partly; 389: 325 partly; 390: 324, row 355 *fratres suos*; 391: 325, rows 459–555, ending *X 3 enta-*) |
| `1738-page-0391.jpg` | 329 (*Cap. 4. 5.*) | about 395 | no |

So from voted leaf 388 on, image = voted leaf − 4 (at least to 392 → 388); rows 227–555 duplicate my pages and
should **not** be read again as text (they would repeat 1:9 – 2:5). The reading sheets for leaf 387 (e.g. sheet 012)
cut the wrong lines under each row (the OCR boxes don't sit on the text), so I read leaves 385–387 from the whole
page images, zoomed with ffmpeg (1.4× per column chunk, 2.5–4× at doubtful spots), with 1750 (`text.txt` lines
46530–46900, which follows 1738's line breaks almost line for line) as a check on the wording.

### Leaves and what is on them

- **385** (p. 323): end of 2 Samuel above the rule (not in the vote); title *REGVM LIBER III.*, *CAPVT I.* and its
  italic summary (*Dauidis ætas decrepita … Fugiens Adonias.*) → rows 3–5 (the summary) removed. 1:1–1:9 *eoque*:
  col. 0 rows 6–19, col. 1 rows 20–38. Signature *X 2* and catchword *fratres* not in the vote (not added).
- **386** (p. 324): 1:9 *fratres* – 1:37 *eiusque solium*. Col. 0 = 51 lines, col. 1 = 51 lines. Rows put back in
  page order and col. 0's rows (44–143, labelled column 1) given column 0. Row 40 *orationem complebo.* is col. 0's
  line 21 (between rows 82 and 85). Catchword *etiam* (row 145, vote *eri*) → `% etiam`.
- **387** (p. 325): 1:37 *etiam supra* – 2:5 *cru-*; *CAPVT II.* and summary (*Moribundi Dauidis … necatus.*) in
  col. 1, not in the vote as rows (row 167 `- JM — '` is junk → removed). Rows of col. 1 (164–226 that the vote
  labels column 0) given column 1.

### Removed rows (9)

3, 4, 5 (ch. 1 summary); 39 *ULm*, 41 *jucfiET* (junk); 42 *REGVM LIBER III.*, 43 *Ca* (running head of 386);
146 *REGVM LIBER ffi.* (running head of 387); 167 `- JM — '` (junk, beside ch. 2's drop capital).

### Added rows (17, all leaf 387, lines lost by the OCR)

Col. 0: 900 *hoc Adonias, et omnes eius conui-* (after row 161); 901 *contatus est, quid sibi vellet tu-*, 902
*multus ille ciuium. #42 Adhuc eo*, 903 *loquente, ecce aderat Ionathan Ab-* (after row 163); 904 *#49 Tum perterriti
omnes, qui ab A-* (after 202); 905 *alius alio discedunt. #50 Ipse Adon-* (after 205).
Col. 1: 906 *aram sese recipit, eiusque cornua* (first line); 907 *gis Solomonis metu, aræ cornua* (after 209); 908
*quod in eo scelus deprehensum fu-* (after 214); 909 *uisset; #54 ille eum domum iussit*, 910 *discedere.* (after
218); 911 *cepit in hunc modum: #2 ego* (after 220); 912 *quam defore, qui ex meo genere* (after 192); 913 *vero tu
scis, quid in me commise-* (after 195); 914 *quo cincta latera, et calceos, qui-*, 915 *bus indutos pedes habebat,
cru-*, 916 `% enta-` (catchword; signature *X 3*) at the foot of col. 1.
No chapter heading was missing in my range: `\c 1` (row 2) and `\c 2` (row 164, moved to its place before *DAuid*,
col. 1) copied unchanged.

### Verse numbers (1738's margins)

- **ch. 1 runs 1–54** (KJV 53). Leaf 385 col. 0 margins legible (1, 2, 3, 4); col. 1 right margin legible (5–9).
  Leaf 386 both margins legible (10–23 left; 24–37 right). Leaf 387 col. 0: 38–43 legible, 44–50 cut by the gutter to
  fragments (on the lines *cumque*, *giæ*, *auditis*, *regii*, *tius*, *Tum*, *alius*), placed by those, the wide
  spaces and 1750 (same lines, numbers printed); col. 1 51–54 legible.
- Placed within the line by the wide space and sense: 2 *suaserunt* (row 9); 4 *puella in primis* (row 17; vote had
  it after *regem adducitur*, KJV 4 "the damsel was very fair"); 5 *Adonias* (20); 7 *Cum* (27); 8 *Sadocus* (30);
  9 *Igitur* (35); 11 *ad-|monuit* (53); 13 *Adi* (68); 16 *Eum* (91); 18 *Atqui* (106); 19 *bouesque* (109); 20 *In
  te* (123); 22 *Ea* (135); 23 *quod postquam* (139, KJV 23 "they told the king"); 24 *domine rex* (45); 25 *Nam*
  (51); 26 *quum* (62); 27 *Fitne* (71); 28 *Tum rex* (76); 29 *Per Iouam* (83); 30 *quemadmodum* (86); 31 *Hic* (95);
  33 *adsumite* (112); 36 *Tum Banaias* (136); 37 *eiusque solium* (144, wide space after *Solomoni,*); 39 *et, sumta*
  (154); 40 *eumque* (158); 41 *Audiuit* (161); 42 *Adhuc* (902); 43 *Atqui* (169); 45 *regem-|que* (178, wide
  space); 46 *Quin* (187); 47 *eiusque Deum* (193; margin fragment on the *regii* line, 1750 the same); 48 *Et rex*
  (197); 50 *Ipse* (905); 51 *Quod* (208); 53 *Deinde* (215); 54 *ille* (909).
- **1:34** at the line's start *eumque ibi* (row 120; no wider space in the line; *ibi … vngitote* is KJV 34 "anoint
  him there"; the vote had it at *tu Sadoce*). A choice by sense: check.
- **ch. 2, in this range 1–5**: 1 *DAuid* (219), 2 *ego* (911), 3 *Tu te* (221), 4 *vt Ioua* (224), 5 *Iam vero* (195).

### Misprints and odd forms, kept as printed

- Row 32 **et Reis** (1750 *et Regis*): clearly *Reis* on 1738 (the Hebrew *Rei*). Wording doubt, 1738 kept.
- Row 38 **Enrogel**: heavy ink, read *Enrogel* (1750 *Enrogel*).
- Row 26 *pulcritudine* (1750 *pulchritudine*). Row 37 *Zoheleth*. Row 147 *dauidicum*; row 225 *israeliticorum* and
  row 223 *mosaicæ* lower-case as printed.
- Row 34 *Dauidis*: a stray acute-like mark stands above the final *s* (zoomed 2.5×); taken as a blot, not written.
- Row 207 *Solomonem*: the second *n* is a damaged sort (looks like *p*/a broken *n*, zoomed 2.5×); written *Solomonem*.
  Check if the edition wants it noted as *Solomopem*.
- Commas without a following space, kept: row 65 **tuum,neque** (and *nequeSado-* set tight, written *neque Sado-*),
  row 67 **pontificem,neque**, row 83 **tit,sic**. Set tight, written with the space: row 83 *PerIouam*. Rows 113
  *epulas, quum* and 127 *significes, ecquis* have a thin space (zoomed 3×), written with it.
- Drop capitals: row 6 **QVVM** (Q + *VVM*); row 219 **DAuid** (D + *Auid*).

### Paragraph indents

Row 6 (1:1, drop capital Q, four lines beside it, rows 6–9); row 85 *Tum Bethsaba* (1:15); row 105 *Tum Dauid iubet*
(1:32); row 149 *Deinde Sadocus* (1:38); row 219 (2:1, drop capital D, rows 219–220 and 911 beside it). No other line
of the three leaves is indented.

### Footnotes, marks, asterisks

No footnotes on leaves 385–387. Marks: row 33 *L.* (before *et Cerethæi*) and *H.* (after *Phelethæi*), kept. No
asterisks.

### Wording doubts (1738 vs 1750)

- 1:8 row 32 *Reis* (1738) / *Regis* (1750): kept *Reis*.
- 1:6 row 26 *pulcritudine* / *pulchritudine*: spelling only.
- Otherwise 1750 agrees with every line read (its *Nathani*, *vixerunt*, *veniet* are its own OCR errors).

### Omission check (against the BSB, 1:1 – 2:5)

Every KJV verse 1:1–53 and 2:1–5a has its matter on the page; the seventeen lines the OCR lost are restored above
(1:41–42, 49–51, 52, 53, 2:1, 4, 5). Nothing the Hebrew has is missing from the page itself.

### Summary

Rows written: 233 (225 rows of the range, minus 9 removed, plus 17 added). Rows changed from the vote: nearly all
(the vote's text for leaves 386–387 is unusable OCR; every line re-read; only a handful of leaf 385 rows were right as
voted apart from s for ſ). `reader-01.tsv` / `.md` not yet written; this partial file holds the complete reading.

---

## reader-02 (`reader-02.partial.md`)

# Reader 02: rows 227–458 (leaves 388–390) — partial file, but the range is in fact read to its end

Paused on the coordinator's request. **Last row finished: 458** (the end of the range). Every row of the range is
accounted for in `reader-02.partial.tsv` (103 rows: 102 from the vote plus 1 added catchword; 130 rows removed,
see below). Rows changed from the vote: 71. Nothing is left to resume in this range; what needs Claude's attention
is the **leaf/crop mismatch** below.

## The leaf numbering is out of step here (must be checked before any reader goes on)

- The archive scan photographed pp. 324–325 three times. In the OCR (`1Kgs1-22.voted.tsv`): leaf 386 = p. 324
  (blurred/partial shot), 387 = p. 325 (garbled), **388 = p. 324 again (column fragments only), 389 = p. 325 again
  (fragments, incl. a second `\c 2` at row 345 and pieces of the ch. 2 summary, rows 348–354)**, **390 = p. 324
  (clean)**, 391 = p. 325 (clean; its own `\c 2` is row 526).
- The page crops do **not** have the duplicate shots: `1738-page-0386.jpg` = p. 324, `0387` = p. 325, `0388` = p. 326
  (2:6–30), `0389` = p. 327, `0390` = p. 328. So from leaf 390 on, **OCR leaf N = crop file N−4** (checked: OCR 391 =
  crop 0387 *etiam supra dauidicum*; OCR 392 = p. 326 *[c]entauit. Tu pro tua prudentia*, = crop 0388; OCR 393 =
  p. 327 *cit. Quod Ioabi*; OCR 394 = p. 328 *in tuo populo*). Leaf 385 = crop 0385 (p. 323) agrees.
- Consequence: **the reading sheets 017–033 (and later sheets, from leaf 388 on) crop the wrong pages** (e.g. sheet
  017's row 228 shows p. 326's *tum non fines*); they cannot be used. I read rows 355–458 from crop `0386` (p. 324)
  directly, zoomed (1.6×, and 3× at doubtful stops). Readers of later leaves must use crop N−4.
- Reader 01's range (leaves 385–387) also contains the duplicate shots 386–387: if Reader 01 reads them as p. 324–325,
  p. 324 will be doubled with my rows 355–458, and p. 325 with leaf 391. Also, leaf 385 (37 rows) stops at *tes
  tuebantur. Sadocus aute[m]*: p. 323 col. 1 goes on (*pontifex, et Banaias Ioiadæ filius, … L. et Cerethæi et
  Phelethæi H. he-|roesque Dauidis, … Igitur quum is Adonias* (9) *… immolasset, eoque*, catchword *fratres*), lines
  not in leaf 385's OCR, so must be added from crop 0385.

## Removed rows (130)

- **Rows 227–354** (all of OCR leaves 388 and 389): the duplicate, fragmentary shots of pp. 324–325, superseded by
  leaves 390 (my rows 355–458) and 391. This includes `\c 2` at row 345 (a duplicate: the real `\c 2` is row 526 on
  leaf 391) and the ch. 2 summary fragments (rows 348–354). Claude: confirm this removal.
- Rows 406 *REGVM LIBER III.* and 407 *Cap. f,*: running head.

## Added rows

- `+ 390 1 900 % etiam`: catchword at the foot of col. 1 (not in the vote).

## Leaf 390 (= crop 0386, p. 324, running head *324 REGVM LIBER III. Cap. I.*): 1 Kings 1:9 (end) – 1:37

Col. 0 (rows 355–405): *fratres suos omnes* (end of 1:9) to *eo submisse sa-*; col. 1 (rows 408–458): *lutato, sic
inquit* to *eiusque solium*, catchword *etiam*. No footnotes, no G./L./H. marks, no asterisks on this page.

### Verse numbers (margins all legible: col. 0 left margin 10–23, col. 1 right margin 24–37; no misprints)

10 *Nathanem autem vatem* (row 357; the vote's *o* was the margin's 0, no `#` in the vote); 11 *ad-|monuit* (359,
by sense, margin beside the line); 12 *Quamobrem* (365); 13 *Adi re-|gem* (367, after *consulas.* and a wide space);
14 *Ego* (373); 15 *Tum Bethsaba* (376); 16 *Eum submisse* (379); 17 *domine, tu mihi* (382); 18 *Atqui scito*
(386); 19 *bouesque et* (388, by sense: KJV 19 "he has sacrificed oxen"); 20 *In te autem* (395); 21 *Te quidem*
(399); 22 *Ea ad-|huc* (401); 23 *quod postquam* (403); 24 *domine rex* (408); 25 *Nam is* (411); 26 *quum* (417);
27 *Fitne* (421); 28 *Tum rex iussit* (424); 29 *Per Iouam* (427); 30 *quemadmodum* (429); 31 *Hic Bethsaba* (434);
32 *Tum Dauid* (439); 33 *adsumite* (442); **34 *eumque ibi* (446)**: the margin 34 stands beside this line; no wide
space inside it, and by sense (KJV 34 "there let Zadok … anoint him") the verse starts with the line; the vote had it
at *et* (line end). **37 *eiusque solium* (458)**: wide space after *Solomoni,*; 1750 has 37 at the same line.
The vote's numbers (#2 … #21) were the running count; all replaced.

### Paragraph indents

Row 376 *Tum Bethsaba regem adit* (1:15) and row 439 *Tum Dauid iubet* (1:32). All other lines flush.

### Forms kept as printed / tight setting

- Row 418 *tuum,neque* and row 419 *pontificem,neque*: no space after the comma, kept; *nequeSado-* set tight,
  written *neque Sado-*. Row 427 *tit,sic*: no space after comma, kept; *PerIouam* tight, written *Per Iouam*.
  Row 369 *tuumSo-* tight, written *tuum So-*.
- Row 421–422 *au-|ctore* (ct ligature; vote *6\ore*). Row 427–428 *viuen-|tem* (vote *viue-|ntem*).
- Row 386–387 *Adon-|iam* hyphenation as printed. Row 409 *iussistine*. Row 442 *adsumite*. Row 457 *adfuit*.

### Main corrections of the vote (wording)

365 *da be* → *dabo*; 368 *Dauidero* → *Dauidem*; 370 *port* → *post*; 372 *Adonias I* → *Adonias?*; 381 *bere! ?* →
*beret?*; **382 *alibi* → *mihi*** (clear on the page; 1750 *mihi*); 393 *ioabum* → *Ioabum*; 394 *tuuin* → *tuum*;
421 *inuitauerit haec* → *Fitne hæc* (vote had repeated the word); 441 *ioiadae* → *Ioiadæ*; 450 *fessum* →
*sessum*; 452–453 *inls-|raelitas, tum in lucteos iraperium* → *in Is-|raelitas, tum in Iudæos imperium*; 458
*folium* → *solium*; æ restored throughout (*Iudæos, thæ, tuæ, quære, Abisagæ, iadæ, hæc, Quæ, præstabo, præbuit,
mulæ meæ*); ſ/f confusions (*sit, so-, sup-, ste-, Bethsaba*) settled on the page.

### Wording doubts

None. 1750 (`sources/archive/1750/text.txt` ll. 46600–46720) agrees in wording throughout 1:11–37. (Outside my
range: crop 0387 and 1750 read *ex-|tollat* where the vote's row 460 has *tollet*: for the next reader.)

### Omission check (BSB 1:9–37)

Every verse's clauses present on the page and in the read lines; 1:36 "Amen" is rendered by *faxit Ioua Deus tuus*
(Castellio's wording), not lost.

### Summary

Range rows 227–458 (232). Written 103 (102 vote rows + 1 added). Removed 130 (128 duplicate-leaf rows 227–354, 2
running-head rows). Changed from the vote: 71.

---

## reader-03 (`reader-03.md`)

## Reader 03: rows 459–755 (1 Kgs 1:37 *…supra dauidicum solium ex-* – 3:8 *…res administrare scio, et*)

Read in two sittings: rows 459–671 by the first reader (paused; `reader-03.partial.tsv` / `.partial.md`, kept as
they are), rows 672–755 by the second. `reader-03.tsv` = the partial's 212 rows unchanged, then rows 672–755.

**Images.** The first sitting read from the old, misnamed images (OCR leaf = image + 4 then: leaf 391 was
`1738-page-0387.jpg`); since the fix (STATUS.md) leaf N is `sources/archive/crops/1738-page-0N.jpg`, and the names below
are the new ones. The first sitting matched each page by running head and text, so its rows stand. The second sitting
read leaf 393 on `1738-page-0393.jpg` (running head *Cap. 2. 3. | REGVM LIBER III. | 327*), in crops at 1.5× per
quarter column and 2.5–4× on doubtful letters and stops; the redrawn sheets 048–054 cover rows 660–757.

1750 (`sources/archive/1750/text.txt`, around lines 46700–47140) is a line-for-line reprint of these pages with the
same margin numbers; used only to confirm margin numbers and to quote in the wording doubts.

Leaf 391 (rows 459–555) shows pages that reader 01 also read from leaf 387 (expected; see STATUS.md).

### Leaves
- Leaf 391 (`1738-page-0391.jpg`, page 325): col. 0 = 1:37 end – 1:50 (*ad*); col. 1 = 1:50 – 1:54, *CAPVT II.* and
  summary, 2:1 – 2:5 (*cru-*); foot: signature *X 3*, catchword *enta-* (row 555).
- Leaf 392 (`1738-page-0392.jpg`, page 326): col. 0 = 2:5 *entauit* – 2:19; col. 1 = 2:19 – 2:30 *…moriturum di-*;
  catchword *cit.* at the foot of col. 1 is not a row in the vote (not added).
- Leaf 393 (`1738-page-0393.jpg`, page 327): col. 0 (lines 4–54) = 2:30 *cit.* – 2:43 *cur Iouæ iusiu-*; col. 1
  (lines 55–103) = 2:43 *randum* – 2:46, rule, *CAPVT III.* and its two-line italic summary (*Solomo Pharaonis gener.
  Illius pietas et sapientia, de scortis iudicium.*: not in the vote, nothing to remove), 3:1 – 3:8 *et*; foot:
  signature *X 4* (under col. 0) and catchword *in* (col. 1), neither a row in the vote (not added). No footnotes.

### Verse numbers (1738's margins)
- **ch. 1 (this range 38–54; 1738 has 54 against the KJV's 53)**: 38 *Deinde* (461), 39 *et, sumta* (466), 40 *eumque*
  (470), 41 *Audiuit* (473), 42 *Adhuc* (478), 43 *Atqui* (483), 44 *eumque eo misit* (486, the vote's *cumque* is
  *eumque*), 45 *regem-|que vnxerunt* (490), 46 *Quin etiam* (495), 47 *eiusque Deum* (498), 48 *Et rex ipse* (501),
  49 *Tum perterriti* (506), 50 *Ipse Adonias* (508), 51 *Quod postquam* (511), 52 *respondit* (517), 53 *Deinde misit*
  (520), 54 *ille eum domum* (524). By sense 1–52 = KJV; 53 = KJV 53a, 54 = KJV 53b.
- Col. 0's numbers 45–50 on leaf 391 are lost in the gutter (only fragments beside rows 490, 495, 498, 501, 506, 508);
  placed by the fragments, the sense, and 1750's margin (same numbers beside the same lines).
- **47 (row 498)**: the fragment (and 1750's *47*) is beside *regii, eiusque Deum comprecati*; KJV 47 would begin at
  *dominoque* (row 496). Placed at *eiusque* (the line's only clause start). **Doubt**: could be *dominoque*.
- **52 (row 517)**: the 52 stands beside *respondit, si vir frugi fuerit, ni-*; placed at *respondit* (the line's first
  word; the vote had it at *nihil*). **Doubt**: could be *si vir*.
- **ch. 2 (1–46, = the KJV's count)**: 1 *DAuid* (528), 2 *ego* (530), 3 *Tu te fortem* (532), 4 *vt Ioua præstet*
  (540; vote had *quæ*), 5 *Iam vero* (545), 6 *Tu pro tua* (556), 7 *At Berzellæi* (558), 8 *Habes Semeim* (563), 9
  *Tu eum impuni-* (570), 10 *Tum obdormiuit* (575), 11 *Regnauit* (577), 12 *At Solomo* (580), 13 *Adonias autem*
  (584), 14 *Vo-|lebam* (587), 15 *Et ille* (589), 16 *Nunc ego* (595), 17 *Vt cum Solomone* (598), 18 *Tum Bethsaba*
  (601), 19 *Cui rex venienti* (605), 20 *paruum ego* (609), 21 *Et illa* (612), 22 *At rex Solomo* (615), 23 *At, ne
  mihi* (621), 24 *Itaque per Iouam* (624), 25 *Hæc locutus* (629), 26 *Abiathari autem* (633), 27 *Ita Abiathari*
  (642), 28 *Horum fama* (645), 29 *Quod vbi* (649), 30 *Banaias in Iouæ* (654), 31 *Quod Ioabi* (658), 32 *vt factam*
  (664), 33 *quorum sanguis* (671), 34 *Tum Banaias* (676), 35 *rex* (678), 36 *Deinde euocato* (682), 37 *Quod si
  exierit* (685), 38 *Semeis regi* (688), 39 *Sed præterito* (692), 40 *instrato* (696), 41 *Quod* (698), 42 *Quum
  ego* (703), 43 *cur Iouæ* (708), 44 *Tu scis* (710), 45 *quod scelus* (713), 46 *Tum Banaias* (718).
  All legible in the margins (13–19 with a worn first digit; 39 printed like *3ꝯ*, 41 and 42 with a small raised
  second digit, all clear by sequence). The vote's numbers were the running count and all replaced (the vote's 25–38
  for 2:34–46, and the stray *6* in row 682 *#27 6 Deinde*, the margin's 36, taken out).
- Within-line placements by the stop and the wider space: 35 at *rex* after *sepulto;* (678; KJV 35 begins with the
  king's appointment), 41 *Quod* (698), 42 *Quum ego* (703), 43 *cur* (708), 44 *Tu scis* (710), 45 *quod scelus*
  (713). Where 1738 divides differently from the KJV: 2:2b *be strong and show yourself a man* is in 1738's 3 (*Tu te
  fortem virumque præbeto*); 2:19a sits in 18 (*Deinde regem adit*); 2:42a *the king summoned Shimei* is in 41's
  lines (*eum ad se curat arcessendum, atque ita adloquitur*); **45 (row 713)**: the margin *45* stands beside *bi sis
  conscius; quod scelus Ioua*, so 45 begins at *quod scelus Ioua in tuum caput retorquet*, which the KJV has as 44b
  (KJV 45 = *quum interim et rex Solomo felix*); placed by the margin (the line has no later start), 1750 the same.
  2:46b *Thus the kingdom was established in the hand of Solomon* is Castellio's 3:1 *Confirmato regno*.
- **ch. 3 (this range 1–8)**: 1 *COnfirmato* (722), 2 *Qui-|bus* (728), 3 *Ipse Solomo* (732), 4 *Quumque* (735), 5
  *ad-|paruit* (740), 6 *Cui* (743), 7 *Quamobrem* (751), 8 *et* (755). The vote had *#2 Ipse*, *#3 vitam*: 1738's 2
  is beside *cum Hierosolymam muros. Qui* (728) and 3 beside *erat. Ipse Solomo* (732); row 734 *vitam agebat.* has no
  number. KJV 3:3b (*only he sacrificed … in high places*) begins 1738's 4 (*Quumque in sacellis sacrificia facere
  atque adolere solitus*); otherwise = KJV.

### Letters lost in the gutter
- Leaf 391 col. 0 margin numbers 45–50 (above). On leaf 393 nothing is lost: both columns and margins are whole.

### Misprints and odd forms, kept as printed
- Row 460 *tollat.* (vote *tollet.*). Row 459, 500, 545 *solium* (vote *folium*: long s).
- Row 474–475 *conui-|uæ* (vote *cónui-|vae*). Row 476 *tubæ*: the u is worn and looks like *n* (*tnbæ*); read *tubæ*.
- Row 509 *Solomonem*: the second n is broken (looks like *ŋ*); read *n*.
- Row 562 *Ab-|salomum* as printed. Row 644 *Silunte*. Row 643 *confieret*.
- **Row 726 *intera*** (3:1 *dum intera domum suam exædificat*): a misprint for *interea*, clear at 3× (1750 *interca*
  = *interea*). Kept.
- **Row 728–729 *Qui|bus***: *Quibus* divided at the line end with no hyphen (zoomed at 4×: *Qui* then the margin 2;
  1750 has *Qui-*). Kept as printed, without a hyphen.
- Row 740 *ad-|paruit*: the hyphen after *ad* is faint and small but there (4×); 1750 *apparuit*.
- Row 708 *iusiu-* is printed with a short round s mid-word (not ſ); written s either way.
- No space after a comma, as printed: row 625 *stabiliuit,et*; row 628 *promiserat,exstruxit,ho-*; row 652
  *gisse,et*; row 662 *sanguine,quem*; row 704 *obtestatus,et tibi*.
- Tight settings written with the space: 549 *Abneri Neris*, 553 *et calceos*, 584 *Adonias autem Hagithæ*, 586 *et ab
  ea*, 601 *Tum Beth-*, 608 *dextra adsedit*, 681 *in Abiatharis* (printed *inAbiatharis*), 727 *et cir-* (nearly
  *etcir-*), 747 *quum aliis*. Parentheses printed with an inner space (*( scis*, *( inquit*, *maior )*) written
  closed up.
- Row 647 *G. L.* printed with a space between.
- Worn letters, read by the word: 716 *sta-* (s–t ligature worn), 731 *exædificata* (the last a broken, looks like
  *exædificat a*), 749 *potissimum* (final m broken), 753 *Dauidis* (i faint), 755 *et* (t worn, looks like *e!*).

### Paragraph indents and drop capitals
- Row 461 *Deinde Sadocus* (1:38); row 528 drop capital **D** + *Auid* (2:1, *DAuid*, three lines beside it);
  row 575 *Tum obdormiuit* (2:10); row 584 *Adonias autem* (2:13); row 633 *Abiathari autem* (2:26); row 682 *Deinde
  euocato Semei* (2:36); row 722 drop capital **C** + *Onfirmato* (3:1, *COnfirmato*, three lines 722–724 beside it);
  row 735 *Quumque in sacellis* (3:4).
- Checked flush: 506, 589, 598, 642, 658, 664, 676, 685, 688, 692, 696, 698, 703, 708, 710, 718 (2:46 *Tum Banaias*
  flush, not a paragraph), 732, 743, 751.

### Footnotes, marks, asterisks
- No footnotes on leaves 391–393. No asterisks.
- **G. … H.** row 581–582: *consedit, G. natus annos duodecim, H. estque* (2:12). **G. L. … H.** row 647: *ad G. L.
  Solomonem H. inclinasset* (2:28). Kept as printed (italic). None in rows 672–755.

### Removed / added / catchwords
- **Row 527 removed**: `#1 digresjin, necatus.`, the last line of the italic summary of ch. 2 (*…digressus, necatus.*).
- Rows 526 `\c 2` and 721 `\c 3` copied unchanged. Ch. 3's heading and summary (leaf 393 col. 1 lines 68–69) are not
  in the vote.
- Row 555 `X 3 enta-` → `% X 3 enta-` (signature and catchword).
- Catchword *cit.* at the foot of leaf 392 col. 1, and signature *X 4* / catchword *in* at the foot of leaf 393: no
  rows in the vote; not added. No rows added.

### Wording doubts / vote losses (the page is the reading)
- Row 577 *sepultus est* (vote lost *sepultus*); row 580 *At Solomo in solio* (vote lost *Solomo*); row 611 *Cui rex*
  (vote lost *Cui*); row 662 *a sanguine,quem* (vote lost *sanguine*); row 567 *veni: cui ego* (vote *cui : cui ego*);
  row 609 *paruum* (vote *panium*). All confirmed on the page and in 1750 where checked.
- Rows 672–755, the vote's misreadings put right from the page (besides spaces before stops, *ae* → *æ*, lower-case
  *iouam* / *ioiadae* → *Iouam* / *Ioiadæ*, and the verse numbers): 674 *so-* (vote *fo-*), 677 *illum* (*ilium*), 678
  *suæ* (*fox*), 679 *illo ex-* (*illoex-*), 680 *ercitui* (*crcitui*), 685 *exierit* (*exieris*), 686 *transierit*
  (*transient*), 695 *fugissent … nuntiatum* (*fugisfent … ntuitiatum*), 701 *eum* (*cum*), 704 *obtestatus*
  (*obteftatus*), 709 *et meum* (*etmeum*), 710 *scis,* (comma lost), 713 *sis* (*fis*), 714 the vote's *#37* before
  *quum in-* (no margin number there) taken out, 716 *solium … beneficio sta-* (*folium … beneficiofta-*), 717 *sit*
  (*fit*), 719 *illumque* (*illuraque*), 720 *sus* (*fus*), 725 *filia* (*tilia*), 726 *intera* (*intere*), 733 *sui*
  (*fui*), 737 *fectus … sacri-* (*fec~his … facri-*), 740 *illa … ad-* (*ilia … ad*), 742 *vt postularet*
  (*vtpoftularet*), 744 *modum* (*molum*), 747 *quum aliis* (*quumaliis*), 752 **tuus** (vote *tum*; 1750 *qui tuus*),
  754 *tris mei creauisti, qui nec tum per* (*trii>meicreauifti, qui nee tamper*), 755 *administrare … et*
  (*adminiitrare … el*).
- 1738 against 1750 in more than spelling: 726 *intera* (1750 *interea*; misprint, above); 732 *Ipse Solomo, Iouam
  amans,* (1750 no comma after *Solomo*); 733 *parentis sui Dauidis* (1750 *sui, Dauidis*); 751 *Quamobrem, Ioua mi*
  (1750 no comma). Stops only; the page is the reading.

### Omission check (1 Kgs 1:37 end – 3:8, against the BSB)
Every verse read against the BSB; no clause the page has is lost in the reading, and the page lacks nothing the
Hebrew has beyond Castellio's usual paraphrase. Points of note, none an omission:
- 1:47–48 the king *bowed in worship on his bed* is in 1738's 48 (*in lecto … submisse gratias egit*); 1:52 *not a hair
  will fall to the ground* rendered *nihil prorsus ei nocitum iri*.
- 2:28 *but not with Absalom*: Castellio has *non ad G. L. Solomonem H.* (his marked reading, not a loss).
- 2:30b Benaiah's report to the king is in 1738's 31 (*Quod Ioabi responsum postquam regi Banaias retulit*).
- 2:37 *your blood will be on your own head* rendered *sua culpa pereundum*; 2:39b *Look, your slaves are in Gath*
  rendered *idque ei nuntiatum esset*; 2:42 *Did I not make you swear … and warn you* = *Quum ego te per Iouam
  obtestatus, et tibi contestatus fuerim*.
- 2:46b *the kingdom was firmly established* opens 3:1 (*Confirmato regno*).
- 3:7b *I am only a little child, not knowing how to go out or come in* rendered *qui nec tum per ætatem res
  administrare scio*.

### Uncertain readings to check
- 1:47 and 1:52 verse-start placements (above); 2:45 placed by the margin at *quod scelus* against the KJV's division.
- *tubæ* (476), *Solomonem* (509) worn letters. *conui-* (474) the hyphen sits a little high (could be read as a stop;
  read as hyphen by the word).
- 740 *ad-* (faint hyphen) and 728 *Qui* (no hyphen): both looked at 4×.

### Counts
- Rows written: **296** (rows 459–755 less row 527 removed): 212 from the first sitting, 84 from the second.
- Changed from the vote: **238** (179 + 59). Removed: **1** (527). Added: **0**.

- **Row 486 corrected at the merge (2026-11-22)**: *cumque eo misit* (1:44), not *eumque*: read on leaf 391 when reader 01's second reading of p. 324 (leaf 387) differed; this was the only word of pp. 324–325 on which the two readings differed.

---

## reader-04 (`reader-04.md`)

## Reader 04: rows 756–1048 (1 Kgs 3:8 *in tuo populo …* – 6:7 *…Templum saxo integro, vt adue-*)

Read in two sittings: rows 756–876 by the first reader (paused; `reader-04.partial.tsv` / `.partial.md`, kept as
they are), rows 877–1048 by the second. `reader-04.tsv` = the partial's 120 rows unchanged, then rows 877–1048 in page
order. No partial row was found wrong on the page (row 856's verse 9 is still a doubt, below).

**Images.** The first sitting read from the old, misnamed images (then leaf = image + 4: leaf 394 was
`1738-page-0390.jpg`), matched by running head and text; the names below are the new ones (leaf N =
`sources/archive/crops/1738-page-0N.jpg`). The first sitting found the old sheets unusable and read the pages
directly. The second sitting read leaves 395–396 on `1738-page-0395.jpg` (head *Cap. 4. 5. | REGVM LIBER III. | 329*)
and `1738-page-0396.jpg` (*330 | REGVM LIBER III. | Cap. 5. 6.*), in crops at 1.5× per quarter column and 3–5× on
doubtful letters and stops.

1750 (`sources/archive/1750/text.txt`, lines ~47120–47560) has the same text and margin numbers but from 4:19 on breaks
its lines differently; used only to confirm numbers and to quote in the doubts.

### Leaves
- Leaf 394 (`1738-page-0394.jpg`, p. 328, *REGVM LIBER III. Cap. 3.4*): col. 0 = 3:8b–21 (rows 756–806); col. 1 =
  3:21–28, *CAPVT IIII.* with its italic summary (*Solomonis ministri. Populi requies. Regis imperium, victus, aula,
  copiæ, præsidium, sapientia.*; not in the vote), then 4:1–7 (rows 807–852). Catchword *rum* at the foot of col. 1,
  not in the vote (not added).
- Leaf 395 (`1738-page-0395.jpg`, p. 329): col. 0 (lines 4–53) = 4:8–24 *…reges sunt,* (rows 853–903), footnote *b)*
  (row 904); col. 1 (lines 55–102) = 4:24 *cumque* – 4:34, rule, *CAPVT V.* and its three-line italic summary (*Ad
  Hiramum regis literæ. Illius ad Solomonem responsio suauis. Ad templum adparatus.*; not in the vote), 5:1–3 *tu scis,*
  (rows 905–948). Foot of col. 1: signature *X 5* and catchword *Da-*, not rows in the vote (not added).
- Leaf 396 (`1738-page-0396.jpg`, p. 330): col. 0 (lines 3–52) = 5:3 *Dauidem* – 5:13 *omni-* (rows 949–998); col. 1
  (lines 54–102) = 5:13 *bus Israelitis* – 5:18, rule, *CAPVT VI.* and summary, 6:1–7 *vt adue-* (rows 1002–1048);
  catchword *ctum* under col. 1, not in the vote (not added). Footnote *c)* set across the foot of the page under
  both columns (vote row 999, placed by the vote in col. 0): its letter stands in col. 1 (row 1048), so the row is put
  after col. 1's last text row.

### Verse numbers (1738's margins)
The vote's numbers were wrong throughout (a running count); every one placed again from the margin. All margin
numbers in the range are legible; none cut by the gutter.
- **ch. 3 (9–28)**: 9 *da mihi* (759, after *sit:*); 10 *Hac re* (764); 11 *Quoniam* (766); 12 *scito* (770); 13 *sed
  etiam* (775); 14 *Quod si* (779); 15 *Tum expergefactus* (784); 16 *Tum ad regem* (790); 17 *o domine* (793); 18
  *Tertio* (796); 19 *hæc,* (799); 20 *et filium* (802; the vote had it at *dormi-*); 21 *Mane* (805); 22 *Tum altera*
  (809); 23 *Ad hunc* (812); 24 *Adlatoque* (818); 25 *Hic mulier* (821); 26 *quæso* (824); 27 *Tum rex* (827; vote at
  *de-*); 28 *Hanc* (829). The vote's `#12` on row 783 and `#13` on 784 were wrong; 783 has no verse start.
- **ch. 4 (1–34; = the KJV's count overall, but 9–15 run one ahead of the KJV)**: 1 *TEnuit* (835); 2 *Aza-* (837,
  margin beside *fuerunt eius proceres: Aza-*; vote on 838); 3 *Eli-* (838); 4 *Banaias* (841); 5 *Azarias* (843); 6
  *Achisar* (846); 7 *Habebat* (848); 8 *Benhur* (853, margin on the first line of leaf 395; the sentence *quo-|rum
  nomina sunt* begins on 852 with no number there); **9 *Elonemque* (856), placed by sense: doubt** (margin 9 beside
  *Bethsamem,  Elonemque et Beth-*, wide space after *Bethsamem,*; could be at *Bethsamem*; 9 covers part of KJV 9 and
  KJV 10); 10 *Benabinada-* (859, = KJV 11); 11 *Is* (861, = KJV 11b); 12 *Baana* (862); 13 *Bengeber* (868); 14
  *Achinadabus* (875); 15 *Achimaas* (876); 16 *Baana Chusæi* (879); 17 *Io-|saphatus* (880); 18 *Semeis* (882); 19
  *Gaber* (883); 20 *Erant* (887); 21 *imperi-|um* (889, margin beside *voluptatibus fruebantur, imperi-*); 22 *Eius*
  (895); 23 *boues* (897, beside *sexaginta,  boues altiles*, wide space); 24 *Nam* (900); 25 *Vulgoque* (906); 26
  *Habebat* (910); 27 *Solomonem* (913); 28 *et equis* (917, wide space after *trahebant,*); 29 *Fuit* (920); 30 *vt non
  solum* (923, wide space after *ditus,*); 31 *ipsumque* (926); 32 *Dixit* (930); 33 *Disseruit* (933); 34 *con-|ueniebant*
  (937). From 16 on 1738 = KJV.
- **ch. 5 (1–18 = KJV)**: 1 *MIsit* (943); 2 *Cui* (947); 3 *tu scis* (948; the vote had it as 2); 4 *Nunc scito* (954);
  5 *in animo* (957, beside *habentem,  inanimo habere*, wide space; vote at *no-|mini*); 6 *Quamobrem* (963); 7 *His
  Solomonis* (971); 8 *Audiui* (977); 9 *Obsequar* (978); 10 *eamque* (983, beside *significaueris,  eamque, ibi a*,
  wide space; vote at *ibi*); 11 *Ita* (986); 12 *estque* (993); 13 *Imperauit* (998); 14 *quos* (1003); 15 *His
  præerat* (1007); **16 *præter* (1011)** placed by sense: the margin 16 stands beside *præter præfectos, operi ab eo
  præ-*; *præter præfectos … tria millia trecentos* is the whole of KJV 16 (vote had it at *operi*); 17 *Iussit*
  (1013); 18 *quæ saxa* (1016).
- **ch. 6 (1–7 in this range)**: 1 *IGitur* (1022); 2 *Fuit autem* (1027); 3 *Vestibulum* (1031; the vote had it
  before *triginta*); 4 *Templum fene-* (1036); 5 *Templi parieti* (1038); 6 *Aedicularum* (1042); 7 *Templum saxo*
  (1048).

### Letters lost in the gutter
None: both leaves' text is whole at the gutter.

### Misprints and odd forms, kept as printed
- Row 768 *diuitias,non*, 810 *est,qui*, 815 *adfirmat,alterius*, 909 *Bersabam,toto*, 977 *Audiui,quæ* (no space
  after the comma).
- Set tight, written with the space: 860 *tenebat Nephathdoram*; 933 *Disseruit de*, *a cedro*; 957 *in animo*;
  1017 *et Hirami*; 1019 *ac præpararunt*; 1040 *et penetrale*.
- Row 800–801 *(quod … incubuerat)*: spaces inside the parentheses dropped.
- Row 875 *Addo-|nis* (double d; 1750 *Ado-|nis*). Row 865 *est* with a broken t.
- Row 891 *palæstinæ* with a lower-case p (1750 *Palaestinae*).
- Row 893 *quas omnes gentes* (as printed; 1750 the same).
- Row 967 *quantam tu dixeris* (1750 *quantum*): kept, see doubts.
- Row 985 *subministrando*: the m is broken into a dotless stroke and an n (*subıninistrando* to the eye, zoomed 4×;
  the OCR read *fubininiftrando*); read as *subministrando*, a damaged letter, not a misprint.
- Row 972 *tis,*: a smudge between *s* and the comma (zoomed 5×), not a stop.
- Row 1033 *in fronte*: a thin rule runs from the e's bar to the right (zoomed 5×); not the thick hyphen of this
  type and no word is divided, so read as an inked space or lead, no hyphen (the vote had *fronte-*).
- Row 902 *tenebat,*: the comma sits low under the t (zoomed 3×); 903 *qui citra*: a speck at the foot of *i* after
  *qui*, read as a blot, not a stop.
- Row 999 (footnote c) *aducherentur*: read as printed, the letter after *du* has no visible bar (zoomed 4×);
  *adueherentur* is meant. **Check on the page** (it may be a worn e).

### Paragraph indents and drop capitals
- Drop capitals: row 835 **TEnuit** (4:1), row 943 **MIsit** (5:1; rows 944–945 set beside it), row 1022 **IGitur**
  (6:1; rows 1023–1024 beside it).
- Indented: 784 (3:15 *Tum expergefactus*), 790 (3:16 *Tum ad regem*), 887 (4:20 *Erant*), 920 (4:29 *Fuit autem*),
  971 (5:7 *His Solomonis*), 977 (5:8 *Audiui*), 998 (5:13 *Imperauit*), and 1048 (6:7 *Templum saxo*: the footnote
  letter *c* stands in the indent). Row 796 (3:18) is not indented; nor are 895 (4:22 *Eius*), 954 (5:4), 978 (5:9).

### Footnotes, marks, asterisks
- **b)** row 904, leaf 395 col. 0: *b) Gaulonim vocat Iosephus.* Hangs on *Argobiæ* (row 872, letter between
  *tractum* and *Ar-*, taken out of the text by the first sitting). The letter is faint in the text; in the note it
  is a clear italic *b* with its parenthesis (zoomed 4×), and the next note in the book is *c)* (row 999), so *b)*.
  No note *a)* in rows 756–1048 (it must be earlier in 1 Kings, or the letters do not restart with the book).
- **c)** row 999, leaf 396, set under both columns: *c) quadrabantur in lapicidinis lapides, quo minores
  aducherentur.* Hangs on *Templum* (row 1048, 6:7; letter before the word, taken out). Moved from col. 0 (the vote)
  to after col. 1's last row, line 900.
- No *G.*, *L.*, *H.* marks in the range.
- **Asterisks** (no footnote), taken out: row 979 *materiam \* mei* (5:9); row 1031 *triginta.\** (6:2); row 1038
  *illustrabat.\** (6:4, the vote had it after `#5`); row 1039 *ædi-|culas \** (6:5).
- Row 806: a small speck above *ra natum*, read as a blot, not an asterisk (no footnote in that column). Worth a look.

### Removed / added / catchwords
- **Row 869 removed** (`395 0 70 ea.`): OCR junk between lines 19 and 20; no such line on the page.
- **Rows 1000–1001 removed**: the running head (*REGVM LIBER III.*, *Cap. 5.6*) of leaf 396.
- **Row 1021 removed** (`#1 Fani absolutio.`): the last line of ch. 6's italic summary.
- **Row added**: `+ 395 1 901 erat.` after row 919 (4:28 *vbi rex | erat.*), the line the OCR lost (vote line 70).
- Rows 942 `\c 5` and 1020 `\c 6` copied unchanged.
- Row 904 (footnote b) given line 900; row 999 (footnote c) moved to col. 1, line 900.
- Catchwords *rum* (leaf 394), *X 5* / *Da-* (395), *ctum* (396): no rows in the vote; not added.

### Wording doubts / vote losses (the page is the reading)
- Rows 756–876: row 815–816 the OCR moved *alterius* and lost *mortuum* (page: 815 *lium suum viuum
  adfirmat,alterius*, 816 *mortuum; altera contra illius mor-*); 763 *popu-* / 764 *lum?* (vote *pop-*/*ulum?*); 764
  *delectatus* (vote *delegatus*); 865 *nam* (vote *nem*), 866 *Bethsana* (vote *Bethsane*).
- Rows 877–1048, the vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops, the
  verse numbers and stray margin digits): 883 **Gaber** (vote *Geber*; 1750 *Gaber*); 885 *terram* (*ren an»*); 890
  *um tenente … in omnia* (*«mtenentc … omnia*); 891 *flumine palæstinæ terræ*; 894 *vitam* (lost); 895 *victus*
  (*victis*); 902 *tum tenebat, a Tipsa* (*tumteriebat. aTipfaadGazam*); 918 *hordeum* (*Uordeum*); 919 *in eum*
  (*in emu*); 922 **nita** (vote *nite*); 924 **mnes** (vote *Omnes*: the word is *o-|mnes*); 927 *Ethanem … Hemanem*
  (*Ethariem … Hemancm*); 931–932 *car-|mina* (vote *mine*); 936 *quadrupedibus*; 943–945 the drop-capital lines
  (*•\ /flfit*, *\j\ rex*, *-^'■^•quum*); 949 *patrem* (*patrere*); 957 *in animo* (*inanirao*); 960 *eius* (*ehrs*);
  963 *mihi* (*mi hi*); 964 *sic* (*sie*); 965 *serui cum tuis adsint: ego tibi ser-* (*feruicum … egotibifer-*); 973
  *tum* (*turn*); 977 *Audiui,quæ* (*Audini,qii3e*); 983 *eamque,* (*eamqtic,*); 985 *vicissim in subministrando*;
  995 **ab illo** (vote *billo*); 996–997 *inter-|cedente* (*inter-|edente*); 1009 *rum* (*rura*); 1010 *octoginta
  millia:* (colon lost); 1013 **rex** (vote *re*); 1024 *qui se-* (hyphen lost); 1029 *construxit*; 1033 *in fronte*
  (no hyphen, above); 1045 *retractiones*; 1046 *ne æ-*; 1047 *diculæ*.
- 1738 against 1750 in more than spelling: 967 *quantam tu dixeris* (1750 *quantum*; *quantam* agrees with
  *mercedem*, so probably not a misprint); 961–962 1750 has no comma after *filius* and *collocatus* (1738
  *filius, a se … col-|locatus, Iouæ*); 902 1750 *a/T'ipfa* (noise). Stops only otherwise. The page is the reading.

### Omission check (1 Kgs 3:8b – 6:7a, against the BSB)
Every verse read against the BSB; no clause the page has is lost in the reading, and the page lacks nothing the
Hebrew has beyond Castellio's usual paraphrase. Points of note, none an omission:
- 3:8b–4:12 (first sitting): every clause present.
- 4:20 *eating, drinking and rejoicing* = *epulisque et voluptatibus fruebantur*; 4:21 *from the Euphrates* = *a flumine*.
- 4:23 *fattened poultry* = *viuaria*.
- 4:29 *breadth of understanding as the sand on the seashore* = *tamque infinita ingenii vbertate*.
- 5:11 *twenty cors of pressed oil*: 1738 *expressi olei viginti coros* follows the Hebrew (the BSB, after the LXX,
  has 20,000 baths).
- 5:18 *the Gebalites* = *fabrique* (Castellio's rendering, not a loss).
- 6:1 *over Israel* not rendered (*anno regni Solomonis quarto*): Castellio's paraphrase.
- 6:7 runs on to leaf 397 (*-ctum*).

### Uncertain readings to check
- Row 856: verse 9 at *Elonemque* or *Bethsamem*.
- Row 1011: verse 16 at *præter* (sense) or *operi* (the vote).
- Row 999 *aducherentur* (c or worn e).
- Row 904 / 872: the letter *b)* (faint in the text, clear in the note).
- Row 1033 *fronte* (thin rule, read as no hyphen); row 1048 indented or only the note letter in the indent.
- Row 806 speck above *ra natum*.

### Counts
- Rows written: **290** (rows 756–1048 = 293, less 4 removed: 869, 1000, 1001, 1021; plus 1 added): 120 from the first
  sitting, 170 from the second (169 vote rows + 1 added).
- Changed from the vote: **235** (103 + 132). Removed: **4**. Added: **1** (*erat.*, leaf 395 col. 1).

---

## reader-05 (`reader-05.md`)

## Reader 05: rows 1049–1349 (1 Kgs 6:7 *-ctum erat, sic ædificabatur* – 7:51 *…ibique repo-|fuit.*)

Read in two sittings: rows 1049–1099 by the first reader (paused; `reader-05.partial.tsv` / `.partial.md`, kept as
they are), rows 1100–1349 by the second. `reader-05.tsv` = the partial's 51 rows, then rows 1100–1349 in page order.
One partial row was found wrong on the page and corrected: **row 1080** `lis, qua parietes` → **`lis,qua parietes`**
(no space after the comma, zoomed 2×). The partial's row 1099 *præcludebat,* (comma) was looked at again (3×): a comma
with a tail, kept (1750 has a full stop there).

**Images.** The first sitting read from the old, misnamed images (then leaf = image + 4: leaf 397 was
`1738-page-0393.jpg`), matched by running head and text; the names below are the new ones (leaf N =
`sources/archive/crops/1738-page-0N.jpg`). The second sitting read on the redrawn sheets
`sources/archive/crops/sheets/lines/1Kgs1-22.voted-078.jpg` to `-096.jpg` (rows 1088–1355; checked by their row
labels) and the whole pages `1738-page-0397.jpg` (head *Cap. 6. | REGVM LIBER III. | 331*), `1738-page-0398.jpg`
(*332 | REGVM LIBER III. | Cap. 7.*) and `1738-page-0399.jpg` (*Cap. 7. | REGVM LIBER III. | 333*), with 2–4× zooms
on doubtful letters and stops.

1750 (`sources/archive/1750/text.txt`, lines ~47640–47960) has the same text and the same margin numbers (22–38 in
ch. 6, 1–52 in ch. 7) with its own line breaks; used to confirm numbers and quoted in the doubts.

### Leaves
- Leaf 397 (`1738-page-0397.jpg`, p. 331): col. 0 (lines 4–54) = 6:7 *-ctum erat* – 6:21 *præcludebat,* (rows
  1049–1099); col. 1 (lines 55–101) = 6:22–38 (rows 1100–1146), then a rule, *CAPVT VII.* and its italic summary
  (*Regia domus. Hiramus ad varia facienda vocatus*; not in the vote), and the catchword *At* (not in the vote; not
  added). Row 1147 `\c 7` copied unchanged.
- Leaf 398 (`1738-page-0398.jpg`, p. 332): col. 0 (lines 4–54) = 7:1–13 *…Hiramum quemdam,* (rows 1148–1198); col. 1
  (lines 55–105) = 7:13 *ex matre vidua* – 7:25 *posteriora to-* (rows 1199–1249); catchword *ta* under col. 1, not in
  the vote (not added).
- Leaf 399 (`1738-page-0399.jpg`, p. 333): col. 0 (lines 4–53) = 7:25 *-ta intus* – 7:40 *quæ decem* (rows 1250–1299);
  col. 1 (lines 54–103) = 7:40 *basibus* – 7:52 *repo-|fuit.* (rows 1301–1349, then 1300); catchword *CAPVT* at the foot
  (not in the vote; not added). No running-head rows in the vote for these leaves.

### Verse numbers (1738's margins)
The vote's numbers were wrong throughout (a running count); every one placed again from the margin.
- **ch. 6 (7–38)**, col. 0 left margin, all legible: the vote's `#7` at *vt in eo* (row 1049) removed (6:7 begins on
  row 1048); 8 *lanuas* (1052); 9 *Templum exædificans* (1056); 10 *et super vniuersum* (1058, within the line after
  *tegebat,* and a wide space); 11 *Ac tum Ioua* (1062); 12 *quod ad istud* (1064); 13 *atque inter meos* (1070); 14
  *Igitur* (1071); 15 *Eius parietes* (1073); 16 *et viginti* (1078); 17 *reliquos quadraginta* (1083); 18 *Interiorem*
  (1085); 19 *Penetrale* (1090); 20 *idque penetrale* (1093); 21 *Aedem intus* (1097). Col. 1 right margin, all
  legible: 22 *Idque* (1100); 23 *In pe-|netrali* (1102); 24 *Vtriusque* (1105); **25 *eadem* (1109)**, margin beside
  *eadem vtriusque mensura atque*, placed at the line start (the line before ends *distaret,*); 26 *Hos in medio* (1111);
  27 *Hos auro tegebat.* (1116); 28 *Templi parietes* (1117); 29 *ipsumque* (1121); 30 *In pene-|tralis* (1122); 31 *quas
  fores* (1125); 32 *Itidem* (1129); 33 *val-|uas* (1131); 34 *insculptis* (1133); 35 *Atrium* (1136); 36 *Hoc Iouæ*
  (1139); 37 *anno vndecimo* (1141); 38 *at|que ita* (1144). 1738's 26–37 run one ahead of the KJV (26 = KJV 27 … 37 =
  KJV 38a; 38 = KJV 38b): Castellio joins KJV 25–26 in his 25. For `versify`.
- **ch. 7 (1–52; the KJV has 51)**: col. 0 left margin of 398, all legible: 1 *AT* (1148); **2 *Qua* (1149)**, margin
  beside *lomo tredecim annis:  Qua*, wide space after the colon (KJV 2 begins with *nemorensem*, row 1150); **3
  *tabulata* (1157)**, margin beside *na transtra incumbebant,  tabulata*, wide space (= KJV 3); 4 *Luminum* (1161); 5
  *quarum fe-* (1163); 6 *Fecit et columnatam* (1167); 7 *Fecit et iudicialem* (1173); 8 *cuiusmodi* (1176); 9 *Atque
  hæc* (1181); 10 *Fundamentum* (1186); 11 *Insuper* (1189); 12 *Atrium maius* (1191; the margin *12* has a blot on the
  1); 13 *Curauit* (1197). Col. 1 right margin of 398: **14 *summæ* (1200)**, beside *tre Tyrio, metallicum,  summæ*,
  wide space; 15 *Duas* (1205); 16 *Tum duo* (1209); 17 *Præter columnas* (1215); 18 *Itemque* (1219); 19 *In
  capitulis* (1223); 20 *Has colu-|mnas* (1228); 21 *Columnarum opere* (1234); 22 *cuius labra* (1236, wide space after
  *vndique,*); 23 *Subter labium* (1239); 24 *et singulorum* (1242, wide space after *bant,*); 25 *la-|cus* (1244).
  Col. 0 of 399 (left margin, the first digit cut by the gutter on most: *ı6*, *7*, *8*, *9*, *o*, *1*, *2*, *3*,
  *4*, *5*, *6*, *7*, *8*, *9*, *o*; placed by the visible digit and the sequence): 26 *Crassitudo* (1250, within
  the line after *habebant.*); 27 *Faciebat et bases* (1255); 28 *Areolas* (1260); 29 *Clausu-|lis* (1262); 30
  *Habebant* (1265); 31 *Lauacri* (1270); 32 *Erant au-|tem* (1274); 33 *Areolis* (1276); 34 *Rotæ* (1278); 35
  *Quatuor autem humeri* (1282); 36 *In summa* (1284); 37 *et in eiusdem* (1287); 38 *Impresserat* (1289); 39 *Ad hunc*
  (1293); 40 *Deinde faciebat* (1297). Col. 1 of 399 (right margin, legible): 41 *Bases* (1302); 42 *lacum in dex-*
  (1304); 43 *Deinde cacabos* (1306); 44 *vi-|delicet columnas* (1309); **45 *videlicet binos* (1315)**, margin beside
  *gas,  videlicet binos malogranato-*, wide space (the vote had it at *gas*); 46 *Item bases* (1318); 47 *breuiter*
  (1323); 48 *Atque hæc* (1326); 49 *Fecit etiam* (1332); 50 *can-|delabra* (1335); 51 *tum cardines* (1342); 52 *Hoc
  omne* (1345). 1738 = KJV to 16; from 17 it runs one ahead (17 = KJV 18 …), with further splits (28/29 = KJV 28–29,
  31/32 = KJV 31, 41/42 = KJV 39, 46 = KJV 43–45a, 47 = KJV 45b, 48 = KJV 46–47); 52 = KJV 51. 1750 has the same 52.
  For `versify`.

### Letters lost in the gutter
None in the text: only the first digits of the margin numbers on leaf 399 col. 0 (above). Row 1207 *bitorum*: a stain
over *bi* (the letters are under it, read through it; 1750 *cubitorum*).

### Misprints and odd forms, kept as printed
- **Row 1052 *lanuas*** (for *Ianuas*): a lower-case *l* (first sitting, zoomed 5×; 1750's OCR also *lanuas*).
- **Row 1115 *in templa*** (for *in templo*): the *a* is clear on the sheet and the page; 1750 *in templo.* Kept; see
  doubts.
- Row 1144 *at* at the line end with **no hyphen** (*at|que ita*; 1750 *at-*): nothing after *at* but the margin 38.
- Row 1143 *omnibus-*: the hyphen is printed as a short raised dot (zoomed 3×); the word runs on (*omnibus-|que*), and
  1750 has *omnibus-*. Written as a hyphen.
- Row 1100 *templum,*: a small raised comma before the margin 22 (zoomed 3×; the vote had a full stop; 1750
  *templum,*).
- Row 1265 *opere simo* (as printed; 1750 the same).
- Row 1335 *adposititii* (1750 *appofititii*); row 1273 *sesquicubitale* (1750 *fexquicubitale*); row 1090 *adparente*
  (1750 *apparente*).
- Row 1171 *coassatione* (printed *coaſſatione*). Row 1328 *Sochot*, 1328–1329 *Sar-|than*, 1142 *Bul*, 1141 *Zif*.
- Row 1049 *ctum* (ct ligature; *ex|actum* split from row 1048); 1097 *Aedem* (A and e separate).
- No space after the comma: 1080 *lis,qua*; 1159 *columnis,singulorum*; 1184 *intus,tum foris,et*; 1202
  *peritiæ,ingenii*; 1213 *imposita,singula*; 1243 *deni,duplici*; 1282 *humeri,qui*; 1309 *fecit,absoluit*; 1312
  *imposita,et*; 1341 *turibula,ex*.
- Set tight, written with the space: 1100 *totum denique*; 1139 *nibus exstruebat*; 1180 *fecit et*; 1182 *et ad*; 1192
  *et vno*; 1262 *boues et cherubi*; 1274 *erant etiam*; 1292 *cum leonibus et palmis*; 1312 *fastigiis imposita*; 1339
  *et capides, et in-*.
- Row 1176 *quear cedro*: the *r* has a long tail touching the *c* (zoomed 3×), not a hyphen (the vote *quear-cedro*;
  1750 *quear cedro*).
- Row 1148 *ædificauit*: the *f* is worn (it looks *ædiricauit*, zoomed 2×); a damaged letter, not a misprint.
  Row 1236 *cuius*: the second *u* and the *s* are smudged together (zoomed 2×). Row 1308 *omne*: a broken *n*.
- Specks, not stops: 1172 a dot well after *obiaceret.* (zoomed 3×); 1238 an orange stain above the comma after
  *cubitorum* (zoomed 4×; a comma, not a semicolon); 1344 a small mark between *templi,* and *aureos.* (on the sheet).

### Paragraph indents and drop capitals
- Drop capital: row 1148 **AT** (7:1, *A* drop capital, *T* small capital; rows 1149–1150 set beside it).
- Indented: 1173 (7:7 *Fecit et iudicialem*), 1197 (7:13 *Curauit*), 1205 (7:15 *Duas columnas*), 1234 (7:21
  *Columnarum opere*), 1255 (7:27 *Faciebat et bases*), 1297 (7:40 *Deinde faciebat*). Each follows a short last line
  (1172 *obiaceret.*, 1196 *ticu fiebat.*, 1204 *que opera fecit omnia.*, 1233 *opus.*, 1254 *rum.*, 1296 *gura.*).
- No indent in ch. 6 within the range (col. 0 of 397 and col. 1: 1117 *Templi parietes*, 1100 *Idque* start flush).
  Not indented: 1345 (7:52 *Hoc omne*, flush after *aureos.*), 1326 (7:48).

### Footnotes, marks, asterisks
- **No footnotes** on leaves 397–399. The last footnote was *c)* (leaf 396, reader 04); the next lettered note
  should be *d)*.
- No *G.*, *L.*, *H.* marks in the range.
- **Asterisks** (no footnote), taken out: row 1104 *materia,\* in altitudinem* (6:23); 1125 *quinaria:\* quas* (6:31);
  1151 *domum \* construxit* (7:2); 1208 *duodecim.\** (7:15, at the line end); 1235 *faciebat, \* rotun-* (7:21);
  1261 *interiectas,\* quibus* (7:28); 1265 *tori,\* opere* (7:29); 1267 *asseres, \* et in* (7:30); 1268 *humeros \*
  subter* (7:30); 1270 *intus \* supra* (7:31).

### Removed / added / moved
- None removed, none added.
- **Row 1300 moved**: `fuit.` (the vote's leaf 399 col. 0 line 103) is the last line of col. 1 (*ibique repo-|fuit.*);
  given col. 1, line 103, after row 1349. Row 1296 was the vote's `c.`: the page has *gura.* (*ac fi-|gura.*).
- Row 1147 `\c 7` copied unchanged.
- Catchwords *At* (397), *ta* (398), *CAPVT* (399): no rows in the vote; not added.

### Wording doubts / vote losses (the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, & → ct, spaces before stops, the verse
  numbers and stray margin digits): 1100 *totum denique templum,*; 1118 **cheruborum** (vote *chetuborum*); 1127
  **cælabat** (vote *cadebat*; 1750 *caelabat*); 1131 *iecturam* (*iechiram*); 1131–1132 **val-|uas** (vote *ve|uas*);
  1139–1141 *tem-|plum … quar-|to mense Zif fundatum, anno* (*rem|pium … qu-|arto se Zif ftmdanim, anu*); 1142
  *vndecimo … Bul* (*vndecirao … Bui*); 1148–1151 the drop-capital lines (*#1 1 ,4 1 domumfuam xdiricauic*, *a /A
  lomo*, *•\*- ■\*- ad finem*, *fern*); 1152 *longitudinem … cubito-* (*loniiuidinem … cubiio-*); 1156 *columnis*
  (*cohuimis*); 1157 *na* (margin *3* in the text); 1169 *quinquaginta* (*quinquagima*); 1175 *eamque* (*eamqvie*);
  1177–1178 *alterum ædi-|um* (*alteriun aedi-|11111*); 1182–1184 *lapidibus, et ad|regulam … serraque defe-|ctis, tum
  intus,tum* (*laoidibus, etad|re^nla.n … (ercaque … cts, turn intuSjtum*); 1186 *iactum* (*iaaum*); 1195–1196 *Iouæ …
  ticu fiebat* (*ioua: … tku tiebat*); 1198 *Hiramum* (*Hiraiuun;*); 1199–1200 **pa-|tre Tyrio** (vote *pa|tre mej*);
  1201 *faciendo* (*faciend*); 1202 *peritiæ … Is* (*periti.?, … I*); 1203 *eius-* (hyphen lost); 1205 *formauit*
  (*formaui*); 1206 *octonum … cu-* (*odronum … cu*); 1207 *bitorum … circui-* (*J9$orum … circui*); 1209–1210 *colu-|
  mnarum, … ex* (*colu|mtiarum … e*); 1211 *ære* (*acre*); 1215 *columnas* (*columna*); 1219 *in vtro-* (*in*: *vtro-*
  lost); 1227 *rum* (*rtini*); 1229 *cellæ* (*celbe*); 1230 *erectamque* (*eredtamque*); 1236 *de-* (hyphen lost);
  1247 *ctabant* (*<5tabant*); 1250 **ta intus** (vote *te*); 1252 *in poculis opus est* (*inpoculisopuseft*); 1260
  *ratio.* (margin *8* in the text); 1262 *leones* (*>leones*); 1263 *tam* (*tara*); 1271 *cubitum, id-* (*cur i'um,
  id.*); 1274 *erant etiam sculpturæ* (*crantetiam fculpturar*); 1277 *rotæ … basibus* (*roue … bad bus*); 1281 *fusi-*
  (*full-*); 1285 *basi capitulum erat* (*beli capitulumeratdimidii*); 1290 *processuum* (*procesfimm*); 1292 *cum
  leonibus et palmis* (*cumleonibusetpalmis*); 1293 *mo-* (*mo.*); 1295–1296 **ac fi-|gura.** (vote *a-|c.*); 1301
  *singulis* (*finglilis*); 1304 *dex-* (*deæ*); 1322 *phialas:* (colon lost); 1325 *ex ære* (*ex xre*); 1326 *hæc*
  (*bate*); 1335 *can-* (*caH-*); 1341 *ex auro* (*exa\iro*); 1344 *aureos.* (stop lost); 1347 *parente* (*pa rente*).
- 1738 against 1750 in more than spelling: **1115 1738 *in templa mutuo se*, 1750 *in templo. mutuo fe***: 1738
  misprinted against the sense (*medio in templo*); kept as printed. 1099 1738 *præcludebat,* (comma), 1750
  *praecludebat.*. 1144 1738 *at* without hyphen, 1750 *at-*. Otherwise stops only (e.g. 1750 *Solomo;* for 1738
  *Solomo,* in 1346; 1750 no comma after *globi* in 1240). The page is the reading.

### Omission check (1 Kgs 6:7b – 7:51, against the BSB)
Every verse read against the BSB; no clause the page has is lost in the reading (every printed line of the three
leaves has its row: 51 + 47 + 51 + 51 + 50 + 50 lines), and the page lacks nothing the Hebrew has beyond Castellio's
paraphrase. Points of note, none an omission:
- 6:7b–6:21 (first sitting): every clause present.
- 6:22 *until everything was completely finished* = *nulla omissa parte*.
- 6:23 *olive wood* = *cupressina materia* (Castellio's rendering; likewise *cupressinas fores* 6:31, *cupressinos*
  6:33; the doors of 6:34 *pineas*).
- 6:25–26: KJV 26 (*the height of each cherub was ten cubits*) = *vtroque in denos adsurgente cubitos*.
- 6:29 *in both the inner and outer sanctuaries* = *intus forisque*.
- 7:1 *his entire palace* = *domum suam … Qua ad finem perducta*.
- 7:6 *a portico in front of it and a canopy with pillars* = *quæ cum suis columnis et coassatione, ante illas posita,
  eis obiaceret*.
- 7:14 *a craftsman in bronze* = *metallicum*; *skill, understanding, and knowledge* = *peritiæ, ingenii atque
  scientiæ*.
- 7:24 *ornamental buds* = *globi, cucurbitarum siluestrium similes*.
- 7:29 *wreaths of beveled work* = *superadditi tori, opere simo*.
- 7:41–45 the inventory: every item present (*columnas duas … rotunda capitula … plagas duas … malogranata
  quadringenta … bases decem … lauacra … lacum vnum … boues duodecim … pelues, fuscinas, phialas*).
- 7:47 *left all these articles unweighed* = *omissa tot vasorum ponderis disquisitione*.
- 7:50 *the Most Holy Place* = *sanctioris sacrarii*; *doors of the main hall* = *ostiorum cellæ templi*.

### Uncertain readings to check
- Row 1115 *templa* (misprint for *templo*; clear on the page).
- Row 1100 *templum,* (a small raised comma) and row 1099 *præcludebat,* (comma, 1750 full stop).
- Row 1143 *omnibus-* (hyphen printed as a dot) and row 1144 *at* (no hyphen).
- Row 1149 verse 2 at *Qua* (margin and space) rather than *nemoren-* (the KJV's start); row 1315 verse 45 at
  *videlicet* rather than *gas*.
- Row 1052 *lanuas* (l or I).

### Counts
- Rows written: **301** (rows 1049–1349, none removed, none added): 51 from the first sitting, 250 from the second.
- Changed from the vote: **220** (36 in rows 1049–1099, of which row 1080 was corrected in this sitting; 184 in rows
  1100–1349, including row 1300 moved to col. 1). Removed: **0**. Added: **0**. Moved: **1** (row 1300).

---

## reader-06 (`reader-06.md`)

## Reader 06: rows 1350–1650 (1 Kgs 8:1 *TVm senatores* – 9:3 *…istam a te constructam æ-*)

Read in two sittings: rows 1350–1418 by the first reader (paused; `reader-06.partial.tsv` / `.partial.md`, kept as
they are), rows 1419–1650 by the second. `reader-06.tsv` = the partial's 68 rows unchanged (`\c 8`, 66 voted rows,
1 added), then rows 1419–1650 in page order, with one added row. **No partial row was found wrong on the
page**; the partial's open point (verse 8 at row 1383 or 1384) is settled below: **row 1383, at *atque***, as written.

**Images.** The first sitting read from the old, misnamed images (then leaf = image + 4: leaf 400 was
`1738-page-0396.jpg`), matched by running head and text; the names below are the new ones (leaf N =
`sources/archive/crops/1738-page-0N.jpg`). The second sitting read the whole pages `1738-page-0400.jpg` (head
*334 | REGVM LIBER III. | Cap. 8.*), `1738-page-0401.jpg` (*Cap. 8. | REGVM LIBER III. | 335*) and
`1738-page-0402.jpg` (*336 | REGVM LIBER III. | Cap. 8.9.*) in strips at 1.6×, with 3–4× zooms on doubtful letters
and stops (scratch folder `scratchpad\r06b\`). The redrawn sheets were not needed.

1750 (`sources/archive/1750/text.txt`, lines ~48000–48340) has the same text and the same margin numbers (ch. 8:
1–66; ch. 9: 1–3 in range) with its own line breaks; used to confirm numbers and quoted in the doubts.

### Leaves
- Leaf 400 (`1738-page-0400.jpg`, p. 334): col. 0 = *CAPVT VIII.*, its italic summary (*Arca in templum Dei. Regis
  Solomonis hymnus.*), then 8:1 *TVm* – 8:12 *Deinde ita locutus / est:* (rows 1350, 1353–1400, + added *est:*);
  col. 1 (lines 58–108) = 8:13 *Grates ago* – 8:26 *Nunc, Deus* (rows 1401–1451); catchword *Israe-* under col. 1,
  not in the vote (not added).
- Leaf 401 (`1738-page-0401.jpg`, p. 335): col. 0 (lines 4–53) = 8:26 *Israelitarum, confirmetur* – 8:36 *possiden-*
  (rows 1452–1501), then the last line *dam.*, lost by the OCR (added); col. 1 (lines 55–105) = 8:37 *Fames* – 8:47
  *impietatemque con-* (rows 1502–1552); catchword *fiten-*, not in the vote (not added).
- Leaf 402 (`1738-page-0402.jpg`, p. 336): col. 0 (lines 4–54) = 8:47 *fitentes* – 8:59 *quibus Iouæ supplica-*
  (rows 1553–1603); col. 1 (lines 55–104) = 8:59 *ui,præsto* – 8:66 *cerat.* (rows 1604–1641), a rule, *CAPVT IX.* and
  its italic summary (*Ad regem Deus. Hiramus fictor. Regis tributa. Aegyptia regina. Regia sacrificia, classis.*;
  not in the vote), row 1642 `\c 9` copied unchanged, then 9:1 *POstquam* – 9:3 *constructam æ-* (rows 1643–1650);
  catchword *dem*, not in the vote (not added).

### Verse numbers (1738's margins)
The vote's numbers were a running count and wrong throughout; every one placed again from the margin.
- **ch. 8, leaf 400 col. 0** (left margin, first sitting): 1 *TVm* (1353, drop capital); 2 *Ita conuocatis* (1359);
  3 *coactisque* (1362); 4 *vna cum* (1365); 5 *quibus* (1367); 6 *Igitur* (1373); 7 *Nam cheru-* (1377);
  **8 *atque illic adhuc sunt* (1383)**; 9 *Deinde egressis* (1388); 10 *Tum Solomo* (1393); 11 *Tum conuersus*
  (1398); 12 *Deinde ita locutus* (1400).
  - **Verse 8 settled (the partial's open point): row 1383, at *atque***. Zoomed (1.6×) on `1738-page-0400.jpg`: the
    numeral *8* stands squarely beside *adparerent:  atque illic adhuc sunt:* (row 1383), not beside *neque
    quidquam* (1384), and there is a wide space after *adparerent:*; a verse beginning at the start of 1384 would put
    the numeral beside 1384. 1750 also prints its 8 beside the *apparerent* line. Castellio's 8 is thus KJV 8b–9
    (*and there they are unto this day* + *nothing in the ark*); the KJV's own boundary (9 at *neque*) is for
    `versify`, not the reading.
- **Leaf 400 col. 1** (right margin, all legible): 13 *Grates ago* (1401); 14 *Dixerat* (1404); 15 *sed Dauidem*
  (1409); 16 *Quumque* (1411); 17 *Ioua ei demon-* (1414); 18 *sed tamen non ipsum* (1418); 19 *sed eius fi-*
  (1419, after *ædem;* and a wide space; vote #13); 20 *Hoc suum* (1422; vote none); 21 *et ibi* (1427; vote #14);
  22 *Hic Solomo* (1431; vote none); 23 *Ioua De-|us* (1434; vote #15); 24 *qui quidem* (1440); 25 *Quare* (1444);
  26 *Nunc, Deus* (1451).
- **Leaf 401 col. 0** (left margin; the first digit cut by the gutter on most: *7*, *8*, *9*, *o*, *1*, *2*, *3*,
  *4*, *5*, *6*; placed by the visible digit, the sequence and the sense): 27 *Enimuero* (1454; vote #19); 28
  *Verumtamen* (1458); 29 *vt oculos* (1462); 30 *Igitur quod* (1467; vote none); 31 *Si quis* (1472; vote `I`);
  **32 *exaudito tu de cælis* (1476)**, margin *2* beside *tum fuerit: exaudito*, placed by sense (KJV 32 *then hear
  thou in heaven*; 1750 the same line); 33 *Quum victi* (1482; vote `3`); 34 *exaudito de cælis* (1487, line start;
  vote #21); 35 *Quum clauso* (1491; vote `5`); **36 *audito de cælis* (1496)**, margin *6* beside *recedent:  audito
  de cælis, tuo-*, wide space after the colon (KJV 36 *then hear thou in heaven*; vote none).
- **Leaf 401 col. 1** (right margin, legible; *41* and *42* blotted): 37 *Fames* (1502; vote #22 at the line end);
  38 *omnes pre-* (1507); 39 *igno-|scitoque* (1513); 40 *vt te me-|tuant* (1518; vote #25 at the line start); 41
  *Quinetiam* (1521); 42 *audito de cælo* (1527); 43 *vt omnes terrarum* (1530); 44 *Si tui ad bellum* (1535); 45
  *exaudito de cælis eorum* (1540); 46 *Si, quum* (1543); 47 *et in ea* (1548).
- **Leaf 402 col. 0** (left margin, legible): 48 *atque ad te* (1553); 49 *audito de tuæ* (1561); 50 *et tuis
  commissum* (1564); 51 *(nam tuus* (1569); 52 *vt oculos* (1572); 53 *Nam tu* (1576); 54 *Finitis* (1583; vote `a`);
  55 *et stans* (1587; vote #38); 56 *grates ago* (1590; vote `6` in the text); 57 *Adsit* (1595; vote `7` in the
  text); **58 *vt mentes* (1597)**, margin *58* beside *ne nos desertos relinquat,  vt*: placed at *vt*, not at the
  line start, by sense (KJV 57 ends *let him not leave us*, 58 *that he may incline our hearts*) and by 1750, which
  sets *ne nos defertos rclinquat,* without a number and prints *58* beside the next line *vt mentes noftras*; 59
  *vtque mea* (1602).
- **Leaf 402 col. 1** (right margin, legible): 60 *vt sciant* (1608); 61 *et vos* (1610); 62 *Deinde apud Iouam*
  (1614); 63 *immola-|uitque* (1616); 64 *Eodem die* (1621); 65 *Atque eo* (1628); 66 *Octauo die* (1635).
- **ch. 9** (right margin): 1 *POstquam* (1643, drop capital); **2 *Ioua ei iterum* (1646)**, margin *2* beside
  *uit:  Ioua ei iterum adparuit,* (wide space; vote had no #2 here); 3 *ego tuas ad* (1648; the vote's #2).
- Castellio's numbering: ch. 8 1–7 = KJV 1–7 (KJV 8a inside his 7), 8 = KJV 8b–9, 9 = KJV 10–11, 10 = KJV 12–13,
  11 = KJV 14, 12 = KJV 15a, 13 = KJV 15b, 14 = KJV 16a, 15 = KJV 16b, 16 = KJV 17, 17 = KJV 18, 18 = KJV 19a,
  19 = KJV 19b; from 20 to 66 = KJV 20–66. Ch. 9 1–3 = KJV 1–3. For `versify`. 1750 has the same numbers.

### Letters lost in the gutter
None in the text; only the first digits of the margin numbers on leaf 401 col. 0 (above).

### Misprints and odd forms, kept as printed
- No misprint against the sense found in rows 1419–1650.
- No space after the comma: 1379 *superne,et* and *vectes,tege-*; 1415 *strauit,quod* and *esset,ipsius*; 1430
  *nostris,a se*; 1500 *dirigens,pluuiaque*; 1604 *ui,præsto* (printed *ui ,præsto*: the space stands before the
  comma, zoomed 4×; space dropped by the rule); 1624 *sacrificio,fertoque*.
- Set tight, written with the space: 1418 *ipsum esse*; 1478 *et nocentem*; 1570 *lus et* and *a te*; 1595 *Deus
  no-*; 1620 *rex et o-*.
- Lower case as printed: 1355 *israeliticarum*, 1406 *isra-|eliticarum*, 1497 *israeli-|tici*, 1573 *israelitici*;
  1590 *grates* (after *hæc verba:*); 1648 *ego*.
- œ in *fœderis* (1358, 1374), *fœdus* (1388), *cœtui* (1399), *fœ-|dus* (1428).
- *adparerent* (1383), *adparuit*, *adparuerat* (1646–1647), *adliciat* (1598), *adposita* (1626), *adfligente*
  (1495), *adfe-|cerat* (1640); 1750 *apparerent*, *apparuit*, *alliciat*, *appofita*.
- *caussam* (1542, 1563, 1607), *quatuor-|decim* (1634), *Hemathæ* (1631), *Gabaonem* (1647), *tuus sunt popu-|lus*
  (1569, as printed; 1750 the same).
- 1643 *POstquam*: drop capital P, two lines deep (rows 1644–1645 set in beside it), *O* a capital, the rest lower
  case.
- Specks, not stops: 1368 a speck between *ea* and *gestantibus* (first sitting); 1437 a faint inked space-mark before
  *qui* (zoomed 4×; not a bracket or stop); 1504 a dot **below the baseline** between *si* and *locustæ* (zoomed 4×;
  lower than any full stop on the page, and no stop is wanted there; 1750 *fi locuftae*): written *si locustæ*,
  flagged below; 1463 a speck after *nomi-*; 1514 a smudge above the comma after *scitoque*.
- Damaged letters: 1369 *simul* (blotted *u*); 1387 *Ioua* (worn *I*); 1432 *Iouæ* (broken *u*); 1533 *hanc* (the *h*
  looks *b* at 1.6×; at 4× the shoulder of an *h*).

### Paragraph indents and drop capitals
- Drop capitals: 1353 **TVm** (8:1); 1643 **POstquam** (9:1).
- Indented: 1401 (8:13 *Grates ago*), 1472 (8:31 *Si quis*), 1482 (8:33 *Quum victi*), 1491 (8:35 *Quum clauso*),
  1502 (8:37 *Fames*, the first line of leaf 401 col. 1; the line before, *dam.*, is short), 1521 (8:41
  *Quinetiam*), 1535 (8:44 *Si tui*), 1543 (8:46 *Si, quum*), 1583 (8:54 *Finitis*). Each follows a short last line
  (*est:*, *propitieris.*, *rependas.*, *reducito.*, *dam.*, *data.*, *censeri.*, *agito.*, *Ioua.*).
- Not indented: 1530 (8:43 *vt omnes*, flush after the full line *concedito:*); every other line of the range starts
  flush.

### Footnotes, marks, asterisks
- **No footnotes** on leaves 400–402. The last lettered note is still *c)* (leaf 396); the next should be *d)*.
- No *G.*, *L.*, *H.* marks. No asterisks.

### Removed / added
- Removed: 1351 `#1 Reg-.r Solomoni*` and 1352 `hymn in.` (the italic summary of ch. 8). None in rows 1419–1650 (the
  summary of ch. 9 was already off the vote).
- Added: `+ 400 0 900 est:` (after row 1400, the last line of leaf 400 col. 0); `+ 401 0 900 dam.` (after row 1501,
  the last line of leaf 401 col. 0, *possiden-|dam.*).
- Catchwords *Israe-* (400), *fiten-* (401), *dem* (402): no rows in the vote; not added.
- Rows 1350 `\c 8` and 1642 `\c 9` copied unchanged.

### Wording doubts / vote losses (the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, & → et, spaces before stops, the verse
  numbers and stray margin digits): 1419 *constructurum* (*conftrudiurum*); 1422 *cturum* (*tSrurum*); 1431 *cussit*
  (*cusfit*); 1456 *cælorumque cæli* (*cxlorumque cali*); 1460 **Ioua mi** (*Ionami*); 1464 *noctes* (*nodes*); 1466
  **ad hunc** (*ad nunc*); 1471 **quum audiueris, propitieris** (vote *quum, propitieris*: *audiueris* lost); 1482
  *victi* (*vi<Sli*); 1487 *cælis* (*cariis*); 1489 *que in terram* (*queinterram*); 1491 *Quum clauso cælo,
  desiderataque* (*Qiiumclaufocxlojdefiderataque*); 1501 **rigato** (vote *rigate*); 1503 *si ardores* (*d ardores*);
  1504 *si locustæ* (*si . locustæ*); 1510 *suæ* (*fuse*); 1513 *domicilio* (*doaiicilio*); 1524 *forti* (*sorti*);
  1533 *constructam* (*conftruciam*); 1538 *delectam* (*dele&am*); 1549 *erunt* (*«runt*); 1551 *dum sese conuerterint*
  (*dumfefeconuerterint*); 1554–1555 *hosti-|um* (*host-|ium*); 1559 **versus ædem** (vote *versus sedem*); 1561
  *tuæ sedis statione* (*tuse sedis lhtione*); 1565 **eorum** (vote *certim*); 1566 *licta* (*licto*); 1568–1569 *sic
  … vt eorum mise-* (*sie … vteorummife-*); 1570 *lus et patrimonium, a te* (*lusetpatrimonium, ere*); 1576
  *inuocaberis* (*rnuocaberis*); 1586
  *passisque* (*pasrisque*); 1587 *cælum* (*j cælum*); 1594–1595 **promise-|rat** (vote *promifc-|tat*); 1602 *cuit*
  (*r,cuit*); 1610 *nec* (*nee*); 1612 *rectas* (*rectos*); 1617–1618 *bo-|um … balan-|tum* (*bo-|urn … bala-|ntum*);
  1620 **caueruntque ædem Iouæ, rex et o-** (*cauefuntque ædem Iou£,rexeto-*); 1623 *Iouæ templum positi. Nam*
  (*lou.e templumpofiti. .Nam*); 1624 *sacrificio* (*facrifkio*); 1627 **et ferta, et adipes** (vote *et ferta
  adipes*: the second *et* lost); 1635–1636 *di-|misit* (*di|misit*); 1636 *actis* (*adus*); 1643 *POstquam … tem-*
  (*POftquara … rem*); 1644 *plum* (*pium*); 1645 *quæ ei* (*qiueei*); 1648 **ad** (vote *a*; zoomed 4×, 1750 *ad*);
  1650 *constructam* (*conftructom*).
- 1738 against 1750 in more than spelling: none. Stops only: 1430 1738 *nostris,a se … eductis, per-*, 1750 *noflris
  a fe … edutis per-*; 1451 1738 *emplo, probauissent*, 1750 no comma; 1569 1738 *reantur,*, 1750 *reantur;*; 1647
  1738 *adparuerat, i-*, 1750 *apparverat; i-*; 1646 1738 *uit:*, 1750 *vit;*; 1636 1738 *illi, actis*, 1750 no comma.
  1504 1738 has the low dot after *si* (above), 1750 none. The page is the reading.

### Omission check (1 Kgs 8:1 – 9:3a, against the BSB)
Every verse read against the BSB; no clause the page has is lost in the reading (every printed text line of the three
leaves has its row, the two lines the OCR lost added), and the
page lacks nothing the Hebrew has beyond Castellio's paraphrase. Points of note, none an omission:
- 8:1–19a (first sitting): every clause present.
- 8:21 *the covenant of the LORD … with our fathers* = *fœdus … Iouæ, quod cum maioribus nostris … percussit*.
- 8:27 *the highest heavens* = *cæli cælorumque cæli*.
- 8:28–30: *the cry and the prayer* = *preces atque supplicationem … obsecrationes atque preces*; *when You hear,
  may You forgive* = *quum audiueris, propitieris* (the vote had lost *audiueris*).
- 8:31–32: *condemning the wicked … justifying the righteous* = *nocentem condemnando, et innocentem absoluendo*.
- 8:37: famine, plague, blight, mildew, locusts, grasshoppers, siege, plague or sickness = *Fames … pestilentia …
  ardores … rubigo … locustæ … eruca … ab hoste … obsidebuntur … clades aut morbus* (all present).
- 8:39 *for You alone know the hearts of all men* = the parenthesis *(nam tu solus … perspicis)*.
- 8:42 *Your mighty hand and outstretched arm* = *manuque forti, et extento brachio*.
- 8:46–50: every clause present, including 8:47 *we have sinned … acted wickedly* = *suum peccatum, culpam
  impietatemque confitentes*, and 8:50 *grant them compassion* = *misericordiam sic in eos moueto*.
- 8:51 *the iron furnace* = *ergastulo ferreo*; 8:53 *O Lord GOD* = *domine Ioua*.
- 8:63 22,000 oxen and 120,000 sheep = *boum viginti duo millia, et balantum centum viginti millia*.
- 8:64 *burnt offerings, grain offerings, and the fat* = *solido sacrificio, fertoque, et adipibus*; 8:65 *from
  Lebo-hamath to the Brook of Egypt … fourteen days* = *ab vsque Hemathæ confinio, ad fluuium Aegypti … bis septem
  dies, id est, quatuordecim*.
- 8:66 the BSB *On the fifteenth day*, Castellio *Octauo die* (the Hebrew's *on the eighth day*): a rendering, not a
  loss.
- 9:1–3a: every clause present to the end of the range.

### Uncertain readings to check
- Row 1504 *si locustæ*: a dot below the baseline after *si* (`1738-page-0401.jpg`, col. 1, about x 790–1040,
  y 185–255); read as a speck, not a full stop.
- Row 1597 verse 58 at *vt* (margin beside the line *ne nos … vt*; placed by sense and by 1750's line).
- Row 1476 verse 32 at *exaudito* and row 1496 verse 36 at *audito* (within the line, by the margin and the sense).
- Row 1604 *ui,præsto* (the space stands before the comma, none after).

### Counts
- Rows written: **301** (rows 1350–1650 less 2 removed, plus 2 added): 68 from the first sitting (`\c 8`, 66 voted
  rows, 1 added), 233 from the second (232 voted rows including `\c 9`, 1 added). Removed: **2** (1351, 1352). Added: **2**.
- Changed from the vote: **209** (49 in rows 1350–1418, counted now against the vote; 160 in rows 1419–1650). No
  partial row changed in this sitting.

---

## reader-07 (`reader-07.md`)

## Reader 07: rows 1651–1949 (1 Kgs 9:3 *dem consecraui* – 11:16 *(nam sex menses*)

Read in two sittings: rows 1651–1752 (leaf 403) by the first reader (paused; `reader-07.partial.tsv` / `.partial.md`,
kept as they are), rows 1753–1949 (leaves 404–405) by the second. `reader-07.tsv` = the partial's 102 rows unchanged,
then rows 1753–1949 in page order, with the CAPVT XI heading and summary removed and two rows added (`\c 11`, footnote
*a)*). **No partial row was found wrong**; the second sitting did not re-read leaf 403 line by line (its last line,
*ongabre, apud Elotha, in litore*, runs on correctly into leaf 404's *maris rubri*).

**Images.** The first sitting read from the old, misnamed images (then leaf = image + 4: leaf 403 was
`1738-page-0399.jpg`), matched by running head and text; the names below are the new ones (leaf N =
`sources/archive/crops/1738-page-0N.jpg`). The second sitting read the whole pages `1738-page-0404.jpg` (head
*338 | REGVM LIBER III. | Cap. 10.*) and `1738-page-0405.jpg` (*Cap. 10. 11. | REGVM LIBER III. | 339*) in column
strips at 1.5× (column 1 recropped from x 770 so that no first letter was cut), with 3–6× zooms on doubtful letters
and stops (scratch folder `scratchpad\r07b\`). The redrawn sheets were not needed.

1750 (`sources/archive/1750/text.txt`, lines ~48480–48715) has the same text and the same margin numbers with its own
line breaks; used to confirm numbers and quoted in the doubts.

### Leaves
- Leaf 403 (`1738-page-0403.jpg`, p. 337, *Cap. 9.*): col. 0 and col. 1 = 9:3 *dem consecraui* – 9:26 *ongabre, apud
  Elotha, in litore* (rows 1651–1752; first sitting). Signature **Y** and catchword **maris** under col. 1, not in the
  vote (not added).
- Leaf 404 (`1738-page-0404.jpg`, p. 338): col. 0 (lines 4–52) = 9:26 *maris rubri* – 9:28 *retulerunt.* (rows
  1753–1760), a rule, *CAPVT X.* and its italic summary (*Austri regina ad Solomonem. Huius opulentia.*; not in the
  vote), row 1761 `\c 10` copied unchanged, then 10:1 *ET Sabæ* – 10:9 *qui ius æquumque* (rows 1762–1799); col. 1
  (lines 53–103) = 10:9 *faceres.* – 10:22 *tertio quo-* (rows 1800–1850); catchword *que* under col. 1, not in the
  vote (not added).
- Leaf 405 (`1738-page-0405.jpg`, p. 339): col. 0 (lines 4–52) = 10:22 *que anno* – 10:29 *adducebantur.* (rows
  1851–1883), a rule, *CAPVT XI.* and its six-line italic summary (rows 1884–1890, **removed**), the added `\c 11`, then
  11:1 *SEd amauit* – 11:2 *pellicerentur* (rows 1891–1899), and footnote *a)* at the column's foot (added); col. 1
  (lines 54–103) = 11:2 *deos.* – 11:16 *(nam sex menses* (rows 1900–1949); signature **Y 2** and catchword **man-**
  under col. 1, not in the vote (not added).

### Verse numbers (1738's margins)
The vote's numbers were a running count and wrong throughout; every one placed again from the margin.
- **ch. 9** (first sitting, leaf 403): 4 *Quod si tu* (1654), 5 (1659), 6 (1664), 7 (1669), 8 (1675), 9 *Quibus* (1680),
  10 *Præteritis* (1687), 11 (1690), 12 (1695), 13 (1698), 14 (1702), 15 (1704), 16 (1709), 17 (1714), 18 (1716),
  **19 *tum omnia* (1718; margin beside the line, placed at the line's start by sense, KJV 19)**, 20 (1723), 21 (1726),
  22 (1732), 23 (1737), 24 (1742), 25 (1745), 26 *Itemque abso-|luto* (1750); all legible.
- **ch. 9, leaf 404 col. 0** (left margin): 27 *qua in classe* (1754; vote #19); 28 *qui Ophir* (1757; vote #20), both
  within the line after a wide space.
- **ch. 10, leaf 404 col. 0** (left margin, all legible): 1 *ET Sabæ* (1762, drop capital); 2 *ingressa-|que* (1765);
  3 *Cui rex* (1771); 4 *Tum* (1774); **5 *tum eius mensæ* (1777)**, margin *5* beside *structam domum,  tum eius
  mensæ*: placed at *tum* by sense (KJV 5 *the food of his table*) and the wide space, as the vote and 1750;
  6 *vtique* (1783, line start; the vote had the numeral as a stray *6* in the text); **7 *quibus re-|bus* (1785)**,
  margin beside *sapientia audiueram:  quibus re-*, placed at *quibus* (KJV 7 *But I did not believe*; 1750 the same
  line); 8 *Felices* (1792); 9 *Grates* (1795).
- **Leaf 404 col. 1** (right margin, all legible): 10 *Tum regi* (1800); 11 *Præterea Hira-|mi* (1804); 12 *quibus ex
  piceæ* (1808); 13 *Solomo quoque* (1813); 14 *Erat au-|tem* (1818); 15 *Præ-|ter ea* (1821); 16 *Fecit* (1825);
  17 *trecen-|tosque* (1828); 18 *Fecit* (1832); 19 *cuius* (1834); **20 *et ibi duodecim* (1839)**, margin *20* (the
  *0* blotted) beside *leones, et ibi duodecim leones in*: placed at *et ibi* by sense (KJV 20 *Twelve lions stood*)
  and the vote; 21 *Atque omnia* (1843, indented line); 22 *Nam cilica* (1849).
- **Leaf 405 col. 0** (left margin, first digit partly in the gutter but legible: *23*–*29*): 23 *Ita tantum* (1853);
  24 *vt totus* (1855); 25 *vtque ei* (1859); 26 *Itaque* (1862); 27 *fecit-|que* (1868); 28 *Ex Aegy-|pto* (1872);
  29 *Addicebatur* (1877). The vote's `#21` at the start of 1883 (*tores adducebantur.*) is a stray: no number in the
  margin there; removed.
- **ch. 11, leaf 405 col. 0**: 1 *SEd* (1891, drop capital); 2 *de quibus* (1895, after *hettæas:* and a wide space).
- **Leaf 405 col. 1** (right margin, all legible; *3* looks like *5*): 3 *Illis amore* (1900); 4 *et sub tempus* (1904,
  after *mus,* and a wide space); 5 *sed etiam* (1909, line start); 6 *Adeoque* (1912); 7 *vt* (1915, end of line);
  8 *idem-|que* (1919); 9 *Itaque* (1922); 10 *atque hoc* (1926, after *adparuerat,* and a wide space; KJV 10 *had
  warned*); 11 *quoniam tu* (1930); 12 *Quamquam* (1934); 13 *Non tamen* (1937); 14 *Igitur* (1942, indented);
  15 *Hic Adadus* (1944).
  - **16 *(nam sex menses* (1949): the margin *16* stands one line high, beside 1948 *occisis ab ipso Ioabo omnibus
    Idu-*, with nothing beside 1949.** Placed at *(nam* by sense: *occisis … Idumææ maribus* is KJV 15 (*had struck
    down every male in Edom*), *(nam sex menses mansit ibi Ioabus* is KJV 16; 1750 prints its *16* beside *mææ
    maribus: (nam sex menses*. The vote had #32 at the start of 1948.
- Castellio's numbering in this range = the KJV's (ch. 9 to 28, ch. 10 1–29, ch. 11 1–16). 1750 has the same numbers.

### Letters lost in the gutter
None in the text. On leaf 405 col. 0 the first digits of *23*–*29* are partly in the gutter but readable.

### Misprints and odd forms, kept as printed
- No misprint against the sense found in rows 1753–1949. *campestrium* (1872) is printed with worn type (the *u* and
  first stroke of *m* broken, looking *campestriiun* at 1.5×; at 6× six stems after *tr*: *i u m*); read
  *campestrium* (1750 *campeftrium*).
- No space after the comma: 1770 *proponit,quidquid*; 1778 *victum,et*; 1861 *equos,mulos*; 1864 *parauit,vt*;
  1867 *oppidis,partim*; 1908 *esset,vt*; 1914 *præstitit,sicut*; 1921 *alienigenis,quæ*; 1939 *concedam,propter*.
  (1770 *adit, eique*, 1861 *arma, aromata* and 1901 *mo, vxores* have a thin space after the comma, zoomed 2.5–5×.)
- Set tight, written with the space: 1840 *sex gradibus*; 1874 *erat ratio*; 1908 *pater Dauid*; 1939 *propter
  Dauidem*; 1909 *sed etiam* (with an inked speck at x-height between them, not a stop).
- Lower case as printed: 1849 *cilica*, 1850 *hiramica* (1750 *Cilica*, *Hiramica*); 1893–1895 *moabitidas,
  ammonitidas, idumæas, sidonias, hettæas*; 1944 *idumæi* (1750 *Idumaei*); 1783 *vtique* after *adloquitur:*.
- *Sabæ* (1762, 1775, 1802, 1814; the vote *Sebæ*); *adseclæ* (1793; 1750 *affeclae*); *adportabat* (1853),
  *adferrent* (1862), *adparuerat* (1926), *adpellatur* (footnote); *caussa* (1858); *insumtis* (1827); *Idumæo-|rum*
  (1753–1754: the line ends *Idumæo-*, the vote broke *Idumæ-|orum*); *mææ* (1949, *Idu-|mææ*); *fœdus* (1931);
  *Astorethum*, *Chamosum*, *Chamoso*, *Melcomum*, *Molocho* (1909–1918).
- 1762 **ET**: drop capital E, two lines deep (1763–1764 set in beside it), *T* a capital. 1891 **SEd**: drop capital
  S, two lines deep (1892–1893 set in), *E* a capital, *d* lower case.

### Paragraph indents and drop capitals
- Drop capitals: 1762 **ET** (10:1); 1891 **SEd** (11:1). (Leaf 403: none.)
- Indented: 1687 (9:10 *Præteritis*, first sitting); 1843 (10:21 *Atque omnia*, after the short line *vllo regno
  factum est.*); 1942 (11:14 *Igitur*, after the short line *lymam.*). Every other line of leaves 404–405 starts
  flush (1783 *vtique*, 6, is flush).

### Footnotes, marks, asterisks
- **Footnote *a)*** (leaf 405, at the foot of col. 0, under 11:2): `% a) idem mox Molochus adpellatur.`, added as
  `+ 405 0 900` after row 1899. It hangs on **Melcomum** (row 1911, 11:5, col. 1: *deum, et ᵃMelcomum
  Ammonita-*; the superior italic *a* before the word, zoomed 3×, taken out of the text row). The page prints the
  letter **a)**, not *d)*: the series that reached *c)* on leaf 396 starts again here (or the letters run per page);
  written as printed.
- **L. … H.** (row 1910): *L. et Chamosum Moabitarum H.* (11:5), italic capitals, kept as printed. *Chamosum* (Chemosh)
  is not in the Hebrew of 11:5 (the BSB names Ashtoreth and Milcom only), nor in the Clementine Vulgate's 11:5
  (*Astarthen deam Sidoniorum, et Moloch idolum Ammonitarum*); Brenton's LXX 11:5 has *τῷ Χαμὼς εἰδώλῳ Μωὰβ*. So the
  marks enclose words the Hebrew lacks. 1750 has the same marks.
- **Asterisk** (row 1807): *piceæ lignorum \* multitudinem* (10:11), no footnote on the page; taken out. 1750 has none.
- No *G.* marks.

### Removed / added
- Removed: **1884–1890**, the heading *CAPVT XI.* (vote *CAPVT XL*) and the six lines of its italic summary
  (*Solomonis effeminatio. Concubinarum numerus: in istum Ioua: in eumdem Idumæus. Razon hostis. In Solomonem
  conspiratio. Eius mors. Liber gestorum Solomonis. Regni anni, sepultura. Roboamus heres.*). Confirmed on the page.
  (Ch. 10's heading and summary were already off the vote.)
- Added: `+ 405 0 37 \c 11` (between rows 1883 and 1891, where the heading stood; line number 37 = the removed
  heading's); `+ 405 0 900 % a) idem mox Molochus adpellatur.` (after row 1899).
- No text line lost by the OCR on leaves 404–405.
- Catchwords and signatures *Y* / *maris* (403), *que* (404), *Y 2* / *man-* (405): no rows in the vote; not added.
- Row 1761 `\c 10` copied unchanged.

### Wording doubts / vote losses (the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops, the verse numbers
  and stray margin digits): 1762–1764 *ET Sabæ … monis … venit* (*y^T Sebæ … t\ monis … •\*-^ venit*); 1766
  *Hierosolymam cum* (*Hierolblymamcum*); 1770 *eique proponit* (*eiquc propoiiit*); 1772 *omnes eius quæstiones*
  (*opines eiusquxftiones*); 1774 *illi non* (*il]inon*); 1777 *structam domum, tum eius* (*ftru6tamdomum, tumeius*);
  1778 *victum,et regiorum accubationem* (*vi£him,ct regiorum acuibationem*); 1781 *sacrificia* (*faci iiicia*); 1785
  *sapientia* (*plentia*); 1790 *tu famam* (*tufamam*); 1792 *virtute.* (*virtute'.*); 1793 **adseclæ** (vote
  *adfectæ*); 1797 *tanto semper* (*tau to Temper*); 1805–1806 **Ophire** (vote *Ophite*, twice); 1810 *et nabla*
  (*etnablacan-*); 1817 *illa* (*ilia*); 1826–1827 **scu-|ta** (vote *sen-|ta*); 1827 *ductili, insumtis* (*dudtili ,
  infumtis*); 1831–1832 *nemo-|rensi* (*nerao-|renfi*); 1833 *solium* (*folium*); 1835 *solii* (*folii*); 1839
  *leones, et ibi* (*leor.es, et*); 1850 *hiramica* (*hiraroica*); 1853 *simiasque … Ita tantum* (*1imiasque …
  Itatantum*); 1856 *conspectum* (*confpedrum*); 1858 *illius prædita* (*iliiuspr?editadi-*); 1859 *uinitus* (*5
  uinitus*); 1864 *parauit,vt … quadringentas* (*parauif,vt … quadringenfas*); 1871 *lapidum: et cedrorum, quam
  syco-* (*lapidumtetccdrorum, quamfyco-*); 1872 *campestrium* (*campeftrimn*); 1874 *hæc erat* (*hæce tat*); 1877
  *raret* (*rarer*); 1901 *septin-* (*feptin-*); 1909 *sed etiam* (*fedetiam*); 1910 *L. et … H.* (*L.tt … //.*); 1913
  *offendit* (*ofFendit*).
- 1738 against 1750 in more than spelling: **none**. Stops and capitals only: 1770 1738 *proponit,quidquid*, 1750
  *proponit quidquid*; 1812 1738 *erat, neque*, 1750 no comma; 1814 1738 *Sabæ, quidquid*, 1750 no comma; 1836 1750
  *rotundum ,'*; 1861 1738 *aromata, equos,mulos*, 1750 *aromata,equos mulos,*; 1878 1738 *quadriga vna*, 1750
  *quadriga vna,*; 1912 1738 *sequeretur.*, 1750 *sequeretur,*; 1849–1850 and 1944 capitals (above). The page is the
  reading.
- **10:27 *auri***: 1738 (1869) *vt et auri Hierosolymæ non minor foret copia, quam lapidum*, where the Hebrew and the
  BSB have **silver** (*The king made silver as common in Jerusalem as stones*). 1750 the same (*vt ct auri
  Hierofoly-*). Castellio's reading or an old misprint carried by both; kept as printed, for the notes.

### Omission check (1 Kgs 9:3 – 11:16a, against the BSB)
Every verse read against the BSB; no clause the page has is lost in the reading (every printed text line of the three
leaves has its row; the OCR lost none on 404–405), and the page lacks nothing the Hebrew has beyond Castellio's
paraphrase. Points of note, none an omission:
- 9:3–26a (first sitting): every clause present (9:25 *So he completed the temple* = 9:26 *absoluto templo*).
- 9:26–28: *Ezion-geber … Eloth … Red Sea* = *Asiongabre, apud Elotha, in litore maris rubri in finibus Idumæorum*;
  420 talents = *quadringenta viginti talenta*.
- 10:1–9: every clause present; 10:5 *the service and attire of his attendants and cupbearers* = *administratorum
  statum atque vestitum, eiusque potionem*; *it took her breath away* = *attonita*; 10:6 *She said to the king* =
  *regem sic adloquitur* (end of Castellio's 5).
- 10:10 *Never again was such an abundance of spices* = *quanta adhuc non prouenerat* (Castellio's *not yet*).
- 10:11–12 almug wood = *piceæ ligna*; *steps* = *fulcra*; *lyres and harps* = *citharas, et nabla*; *nor has such been
  seen* = *neque visa*.
- 10:13 *out of his royal bounty* = *vt rege Solomone dignum erat, vltro*.
- 10:15 *merchants, traders … Arabian kings and governors* = *a mercatoribus, ab institoribus aromatariis, omnibusque
  Arabiæ regulis, et regionis prætoribus*.
- 10:16–20: 200 shields × 600 shekels, 300 × 3 minas, the throne, six steps, rounded back, armrests, two lions, twelve
  lions: all present.
- 10:22 *ships of Tarshish … once every three years … gold, silver, ivory, apes, and peacocks* = *cilica classis regia,
  vna cum hiramica, tertio quoque anno … aurum, argentum, ebora, pauos, simiasque*.
- 10:25 *articles of silver and gold, clothing, weapons, spices, horses, and mules* = all six present.
- 10:26 1,400 chariots, 12,000 horsemen = *mille quadringentas quadrigas … equitum millia duodecim*.
- 10:27 *silver* rendered *auri* (above); *cedar as abundant as sycamore in the foothills* = *cedrorum, quam
  sycomororum campestrium*.
- 10:28 *from Egypt and Kue* = *Ex Aegypto*; *Kue* is not rendered (Castellio reads the word as *societas*, *the royal
  merchants' company*): a rendering, not a loss.
- 10:29 600 shekels, 150; *Hittites … Aram* = *Hettæorum et Syriæ regibus*.
- 11:1–2: every clause present; 11:2 *Yet Solomon clung to these women in love* = *Illis amore iunctus Solomo*, which
  opens Castellio's 3 (it stands after the margin *3*; the KJV's 2 ends there).
- 11:3–13: every clause present; 11:5 adds *L. et Chamosum Moabitarum H. deum* (marked); 11:7 *on a hill east of
  Jerusalem* = *in monte Hierosolymis obiacente*; 11:9 *twice* = *semel atque iterum*.
- 11:14–16a: present to the end of the range.

### Uncertain readings to check
- Row 1949 / 1948: verse 16 placed at *(nam* (1949), though 1738's margin *16* stands beside 1948 (by sense and by
  1750's margin); `1738-page-0405.jpg`, col. 1, foot.
- Footnote letter *a)* (not *d)*) on leaf 405: as printed, both at the note and at *Melcomum*.
- Row 1872 *campestrium* (worn type; `1738-page-0405.jpg`, about x 300–520, y 1155–1210).
- Row 1869 *auri* for the Hebrew's silver (10:27), as printed and as 1750.

### Counts
- Rows written: **294** (rows 1651–1949 less 7 removed, plus 2 added): 102 from the first sitting (all voted rows,
  none added or removed), 192 from the second (190 voted rows including `\c 10`, plus `\c 11` and footnote *a)*).
- Removed: **7** (1884–1890). Added: **2** (`\c 11`, footnote *a)*).
- Changed from the vote: **227** (83 in rows 1651–1752; 144 in rows 1753–1949). No partial row changed.

---

## reader-08 (`reader-08.md`)

## Reader 08: rows 1950–2246 (1 Kgs 11:16 *mansit ibi Ioabus* – 13:6 [1738's 13:6] *ora, quæso, in-*)

Read in two sittings: rows 1950–1999 (leaf 406 col. 0) and the footnote *b)* by the first reader (paused;
`reader-08.partial.tsv` / `.partial.md`, kept as they are), rows 2000–2246 (rest of leaf 406, leaves 407–408) by the
second. `reader-08.tsv` = the partial's 51 rows unchanged, then rows 2000–2246 in page order, with six rows removed
(running heads, one italic summary) and two footnote rows added. **No partial row was found wrong**: the second
sitting checked the two marks the partial left open (rows 1981, 1999) and the footnote *b)* on the page (below), and
read the partial's last lines into leaf 406 col. 1 (*cuius conspira-|tionis*), which run on correctly.

**Images.** The first sitting read from the old, misnamed images (then leaf = image + 4; its notes say
`1738-page-0402.jpg` for leaf 406); the names here are the new ones, leaf N = `sources/archive/crops/1738-page-0N.jpg`,
matched by running head: leaf 406 = `1738-page-0406.jpg` (*340 | REGVM LIBER III. | Cap. 11.*), 407 =
`1738-page-0407.jpg` (*Cap. 11. 12. | REGVM LIBER III. | 341*), 408 = `1738-page-0408.jpg` (*342 | REGVM LIBER III. |
Cap. 12. 13.*). The second sitting read the whole pages in column strips at 1.4× with 4–6× zooms on doubtful letters,
stops and the gutter (scratch folder `scratchpad\r08b\`); the redrawn sheets were not needed. 1750
(`sources/archive/1750/text.txt`, lines ~48755–49075) has the same text and, where its OCR kept them, the same margin
numbers; used to confirm numbers and quoted in the doubts. No rows of the doubts file fall on these leaves.

### Leaves
- Leaf 406 (`1738-page-0406.jpg`, p. 340): col. 0 (lines 4–53) = 11:16 *mansit ibi Ioabus* – 11:28 *cuius conspira-*
  (rows 1950–1999; first sitting), footnote *b)* at its foot (added by the first sitting); col. 1 (lines 55–104) =
  11:28 *tionis caussa* – 11:38 *adero tibi,* (rows 2002–2051). Catchword **et** under col. 1, not in the vote (not
  added). Rows 2000–2001 (*REGVM LIBER III.*, *Cap. II.*) are the running head: **removed**.
- Leaf 407 (`1738-page-0407.jpg`, p. 341): col. 0 (lines 4–50) = 11:38 *et domum tibi* – 11:43 *eius filius.* (rows
  2053–2073), a rule, *CAPVT XII.* and its two-line italic summary (*Populus ad nouum regem. Huius crudelitas. Populi
  defectio. Ieroboamus rex, idololatra.*), row 2074 `\c 12` copied unchanged, then 12:1 *IS Roboamus* – 12:7 *Cui
  illi* (rows 2076–2098), and footnote *c)* (added); col. 1 (lines 53–102) = 12:7 *respondent* – 12:17 [Castellio]
  *lapidibus* (rows 2099–2147), then signature and catchword row 2148 (`% Y 3 ob-`) and footnote *d)* (added). Row 2052
  (*Gap. ii. is.*, the head *Cap. 11. 12.*) and row 2075 (the summary's second line, *Populi defectio …*, with a stray
  `#1`) **removed**.
- Leaf 408 (`1738-page-0408.jpg`, p. 342): col. 0 (lines 4–54) = 12:17 *obrutum necarunt* – 12:30 *quum vulgo alte-*
  (rows 2150–2200); col. 1 (lines 55–103) = 12:30 *rius visendi* – 12:33 *collocauit.* (rows 2202–2213), a rule,
  *CAPVT XIII.* and its four-line italic summary (*Ieroboami manus tabida. Vates laceratus a leone. Ad illum alius
  vates. Mortui sepultura. Ieroboami malitia maior: eiusdem familiæ exstinctio.*; not in the vote), row 2214 (below),
  then 13:1 *QVum autem* – 13:6 *ora, quæso, in-* (rows 2215–2246). Catchword **quit,** under col. 1, not in the vote
  (not added; leaf 409 begins *quit, Iouam*). Rows 2149 (*REGVM LIBER III.*) and 2201 (*Cap. 12. i$.*) are running
  heads: **removed**.

### Chapter 13 (row 2214)
The vote's row 2214 `\c 10` stands where 1738 prints **CAPVT XIII.** (`1738-page-0408.jpg`, col. 1, below *ctos,
collocauit.*; the running head reads *Cap. 12. 13.*; 1750 also prints *CAPVT XIII* there). **Written `\c 13`** (the only
`\c` row changed). 1738's ch. 13 begins *QVum autem ad aram, quam Bethele fecerat* = KJV 12:33 (second half); its 13:2
*superuenit* = KJV 13:1.

### Verse numbers (1738's margins)
The vote's numbers were a running count (#38–#51, #1–#20, #1–#4) and wrong throughout; every one placed again.
- **ch. 11, leaf 406 col. 0** (first sitting; left margin, all legible): 17 *fugerat* (1952), 18 *Hi* (1956), 19
  *tantamque* (1963), 20 *Ex hac* (1967), 21 *Igitur* (1972), 22 *quærentique* (1977), 23 *Præterea* (1981), 24
  *factaque* (1985), 25 *captaque* (1988), 26 *Is* (1989), 27 *toto* (1992), 28 *Ad hæc* (1995).
- **ch. 11, leaf 406 col. 1** (right margin, all legible): 29 *Mellonem* (2002, after *fuit:* and a wide space);
  30 *Quodam* (2009); 31 *Hic quum* (2013); 32 *Vnam* (2022); 33 *quoniam* (2026); 34 *Ab illo* (2033); 35 *Sed aufe-*
  (2038); 36 *concessa* (2040); 37 *Tibi* (2044); 38 *Quod si* (2047, line start, not indented).
- **ch. 11, leaf 407 col. 0** (left margin, the first digit in the gutter): 39 *Atque* (2055, margin *39* beside
  *Israelitasque tib tribuam. Atque*; placed at *Atque* by sense, KJV 39 *I will humble David's descendants*; the vote's
  stray *P* before *Israelitasque* is the margin); 40 *Hanc* (2058; *4* cut); 41 *De* (2063, line end; margin *·1*,
  KJV 41 *the rest of the acts*); 42 *Regnauit* (2067; only *2* visible); 43 *Deinde* (2069; only *3* visible). The vote's
  #50 at the start of 2066 (*stat in libro*) is a stray.
- **ch. 12, leaf 407 col. 0** (left margin, **cut by the gutter**: only slivers of the right edges show, beside 2079
  (*2*-like), 2081, 2082 (faint), 2085 (a dot), 2086, 2088, 2092 and 2095; none legible as a digit). 1 *IS* (2076, drop
  capital); the rest **placed by sense** (KJV/BSB) and the sentence breaks: **2 *Ieroboamus* (2079)** (sliver beside
  that line; KJV 2 *When Jeroboam heard*); **3 *arcessitus* (2083)** (KJV 3 *they sent for Jeroboam*; a faint sliver
  stands beside 2082 *gerat) degebat, postquam id*, so 3 could stand at *postquam* instead); **4 *vt, quoniam* (2086)**
  (KJV 4 *Your father put a heavy yoke*; sliver beside the line; *Atque hi a Roboamo postularunt*, 2085, is KJV 3's
  *and said*); **5 *Quibus* (2091)** (1750's OCR has *5* beside this line); **6 *Atque* (2093, line end)** (KJV 6
  *consulted with the elders*); **7 *Cui illi* (2098)** (KJV 7 *They replied*). To check against another copy of 1738.
- **ch. 12, leaf 407 col. 1** (right margin, all legible): 8 *At ille* (2103, line start; flush); 9 *quidnam* (2106);
  10 *Cui* (2109); 11 *quod si* (2116); 12 *Die tertio* (2120); **13 *meus* (2125)**, margin *13* beside *consilium
  secutus, ita dixit: meus*, the speech (KJV 14); 14 *Non est* (2129; KJV 15); 15 *Tum omnes* (2134, indented; KJV 16);
  16 *At-|que ita* (2140; KJV 16b–17); 17 *Quumque* (2144; KJV 18a).
- **ch. 12, leaf 408 col. 0** (left margin, all legible): **18 *Itaque* (2150)**, margin *18* beside *obrutum necarunt.
  Itaque occu-*: placed after the stop and the wide space (*obrutum necarunt* ends 17; 1750 has *18* beside *necarunt.
  Itaque*; KJV 18b *mounted his chariot*); 19 *Atque ita* (2153); 20 *Quumque* (2155); 21 *At Roboamus* (2161); 22 *Sed
  mandauit* (2169); 23 *ne proficisce-* (2173); 24 *Ita illi* (2177); 25 *Instaurauit* (2180, indented); 26 *Deinde*
  (2183, line end); 27 *Si homines* (2186); 28 *Igitur* (2191); 29 *Atque vnum* (2197); 30 *quæ res* (2199).
- **ch. 12, leaf 408 col. 1** (right margin, legible): 31 *Fecit* (2204, indented); 32 *Itemque* (2206); 33 *idque
  Bethele* (2210).
- **ch. 13, leaf 408 col. 1**: 1 *QVum* (2215, drop capital); 2 *superuenit* (2221); 3 *cuius* (2231); 4 *His* (2235);
  5 *Tum diffissa* (2242); 6 *Hic rex* (2245).
- Castellio's numbering against the KJV: ch. 11 from 32 = KJV (his 29–31 cover KJV 27–31: 29 *Mellonem* = KJV 27b–28,
  30 *Quodam* = KJV 29, 31 *Hic* = KJV 29b–31); ch. 12 = KJV to 12, then one ahead (13 = KJV 14 … 16 = KJV 16b–17,
  17–18 = KJV 18), the same again from 19; his 13:1 = KJV 12:33, his 13:2 = KJV 13:1–2, from 3 = KJV.

### Letters lost in the gutter
None in the text. Leaf 407 col. 0: the first digits of *39*–*43* are cut (sequence and the visible last digits settle
them); **ch. 12's numbers 2–7 are lost** (above).

### Misprints and odd forms, kept as printed
- **2055 *tib tribuam*** (11:38): *tib* without the *i*, clear at 4× (`1738-page-0407.jpg`, about x 300–400,
  y 225–260); 1750 *tibi tribuam*. A misprint, kept.
- **2029 *Mclcomum*** (11:33): the second letter is a *c* (no crossbar, zoomed 4×, against the clear *e* of *neque* in
  the next lines); 1750 *Melcomum*, and leaf 405 (row 1911) prints *Melcomum*. Kept as printed; possibly a broken *e*:
  check (`1738-page-0406.jpg`, about x 880–1000, y 1500–1540).
- No space after the comma: 2049 *gradiens,mihi … fueris,mea*; 2078 *Israelitæ,eius*; 2097 *gauitque,quid*; 2123
  *durius,et*; 2128 *animaduertit,ego*; 2131 *Ioua,vt*; 2152 *dere,Hierosolymamque*; 2205 *vulgo,a*; 2216
  *fecerat,accessisset*; 2223 *qui,Ieroboamo*; 2228 *nomine,qui*. (2028 *rum, Chamosum* has a thin space, zoomed 4×.)
- Set tight, written with the space: 2088 *eis ab*; 2205 *a Leui* (*aLeui*).
- Lower case as printed: 2162–2163 *iu-|dæam*, 2160 *dauidicam*, 2164 *beniamiticam*. *Isæida* (2137; vote *Isaeida*;
  1750 *Ifacida*). *Sesacum* (2061; vote *Sesaeum*). *Ahiæ*, *Ahias*, *Ahiam* (2011, 2014, 2133; vote *Abiae*, *Abias*,
  *Abiam*). *viventi* with *v* (2096). *cœpit* with the ligature (2184). *extorsurus* (2021). *Astorethum*, *Chamosum*
  (2027–2028). *caussa* throughout. *Iudææ*, *Iudæ*, *Iudæa* (2143, 2171, 2189, 2208, 2222).
- Drop capitals: 2076 **IS** (I two lines deep, 2077–2078 set in beside it; *S* a capital); 2215 **QVum** (Q two lines
  deep, *V* a capital).
- First sitting: row 1954 *idumæis* lower case; 1998 *minabatur* with a broken *t*.

### The partial's open marks (settled on the page)
- **Row 1981 *Solo-***: at 6× the line end is a plain hyphen with a short raised stroke above it (a stray or a damaged
  sort), not a letter or accent: read as the hyphen; the row stands.
- **Row 1999 *conspira-***: at 5× the mark is a round blob at mid x-height, the same height as the hyphens of *So-*,
  *no-* two lines above (not on the baseline like a full stop), and the word runs on as *tionis* (2002): the hyphen; the
  row stands.

### Paragraph indents and drop capitals
- Drop capitals: 2076 **IS** (12:1); 2215 **QVum** (13:1).
- Indented: **1995** (11:28 *Ad hæc Ieroboamus*, first sitting); **2134** (12:15 *Tum omnes*, after the short line
  *Ahiam Silonium prædixerat.*); **2180** (12:25 *Instaurauit*, after the short line *tum expeditionem omiserunt.*);
  **2204** (12:31 *Fecit et ædem*, after the short line *commearent.*). Every other line of the range starts flush
  (2047 *Quod si*, 2058 *Hanc*, 2067 *Regnauit*, 2103 *At ille*, 2186 *Si homines* are flush; 2073 *eius filius.* and 2213
  *ctos, collocauit.* end chapters).

### Footnotes, marks, asterisks
- **b)** (leaf 406, under col. 0): `% b) posteritatem.`, added by the first sitting as `+ 406 0 900` after row 1999.
  The letter at the note is an italic *b* with a heavy bowl (5×), the same form as the letter in the text. It hangs on
  **lucernam** (row 2041, 11:36, col. 1: *vt ᵇlucernam habeat*; italic *b* before the word, zoomed 5×), taken out of the
  text row. The note stands at the foot of col. 0 only (col. 1's foot has the catchword *et*), so it stays after
  col. 0's rows.
- **c)** (leaf 407): `% c) in rege, sicut Cæsares a primo nomen habent.`, added as `+ 407 0 900` after row 2098: the
  note begins at the foot of col. 0 and runs on under col. 1. It hangs on **in Dauide** (row 2136, 12:16: *nihil iam
  sibi iuris ᶜin Dauide*; italic *c* before *in*), taken out.
- **d)** (leaf 407): `% d) scilicet ante Israelitarum discessum.`, added as `+ 407 1 901` after row 2148 (its first line
  begins under col. 1 after *c)*, the second, *discessum.*, under col. 0). It hangs on **misisset** (row 2145, 12:18:
  *Quumque ᵈmisisset Roboamus*; italic *d* at the line's start), taken out.
- Letters as printed: *b)* on leaf 406, *c)*, *d)* on leaf 407, after *a)* on leaf 405: the series runs on here.
- No *G.*, *L.*, *H.* marks and no asterisks in rows 2000–2246 (none in 1950–1999 either).

### Removed / added
- Removed (6): **2000, 2001** (running head of leaf 406 col. 1); **2052** (*Gap. ii. is.* = *Cap. 11. 12.*); **2075**
  (the second line of ch. 12's italic summary; the heading and first line were already off); **2149** (*REGVM LIBER
  III.*); **2201** (*Cap. 12. i$.*). All confirmed on the page.
- Added (2 here, 3 in all): `+ 407 0 900 % c) …`, `+ 407 1 901 % d) …`; the partial's `+ 406 0 900 % b) …`.
- Row 2148 `Y 3 ob-` made `% Y 3 ob-` (signature and catchword of leaf 407).
- No text line lost by the OCR on leaves 406–408 (line numbers run on in every column, gaps only at the headings).
- Catchwords *et* (406) and *quit,* (408): no rows in the vote; not added.
- Row 2074 `\c 12` copied unchanged; row 2214 `\c 10` → **`\c 13`**.

### Wording doubts / vote losses (the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops, verse numbers and
  margin debris): 2002 *tionis caussa hæc fuit:* (*caussa haec ruit*); 2003 *ædificante Solomone* (*sdificanteSolomone*);
  2011–2014 *Ahiæ*, *Ahias* (*Abiae*, *Abias*); 2029 *Mclcomum* as the vote; 2041 the footnote letter out; 2047 *quæ
  tibi præci-* (*quae tibipneci-*); 2051 *meus: adero tibi,* (*meusiaderotibi,*); 2055 *Israelitasque tib* (*PIsraelitasque
  tib*); 2061 *Sesacum*; 2065 *et gestis, et sapientia, scriptum* (*etgeftis, etfapientia, fcriptumex-*); 2073 *filius*
  (*dims*); 2078 *nerant omnes Israelitæ,eius* (*nerantomnes Israelitx,eius*); 2088 *eis ab*; 2098 *respondendum? Cui
  illi* (*respondendum I Cui ilii*); 2099 *si … illis* (*st … ilJis*); 2103–2109, 2116 the line ends cut in the vote
  (*f*, *e*, *censu*, *Cu*, *iu*) read whole: *se-*, *eo*, *et*, *consu-*, *a se*, *Cui*, *iu-*; 2122 *iussi* (*iusfifiierant*);
  2125, 2127 *meus* (*mens*, *metis*); 2133 *Ahiam* (*Abiam*); 2136 *iuris in* (*iuris c in*); 2137 *Isæida*; 2140 *At-*
  (*At-I*); 2142 *sic tamen, vt Israelitæ* (*fictamen, vtlsraelitx*); 2145 *misisset* (*</misisset*); 2150 *obrutum
  necarunt. Itaque occu-* (*obmfum necarunf. Itaqueoccu-*); 2154 *domo* (*dorae*); 2159 *tantum Iu-* (*tantumlu-*); 2164
  *miticam* (*rniticam*); 2165 *octoginta* (*o&oginta*); 2170 *fi-* (*ri-*); 2171 *Iudææ* (*lud eae*); 2176, 2180, 2197,
  2199 stray margin digits *1*, *j*, *9*, *0* dropped; 2178–2179 *et ad … tum expeditionem* (*etad … tumexpeditionem*);
  2184 *sic … cœpit* (*sie … coepit*); 2191 *illum* (*ilium*, also 2239–2240); 2193 *monuit* (*mOnuit*); 2196 *educti ex Ae-*
  (*edu&i exAe-*); 2200 *offensam attulit, quum vulgo* (*offenfamattulit, quum vulgoalte-*); 2204 *sa-* (*fa»*); 2205
  *vulgo,a Leui*; 2206 *festum* (*testum*); 2212–2213 *a se fa-|ctos* (*afefa-|6tos*); 2217 *octaui* (*oifraui*); 2221
  *adscendisset* (*adfeendisfet*); 2224 *clamauit ad* (*clamauitad*); 2229 *mactabit* (*ma&abit*); 2242 *diffissa*
  (*diffisf*).
- 1738 against 1750 in more than spelling:
  - **2117 *onerauit*, 2119 *aduertit*** (12:11): 1738 *quod si pater eos graui iugo onerauit … si pater in eos scuticis
    animaduertit* (both clear on the page); 1750 *onerauerit … animaduerterit*. Kept as printed.
  - **2055 *tib*** (1750 *tibi*) and **2029 *Mclcomum*** (1750 *Melcomum*): above.
  - Stops only: 2101 1738 *fore, vt*, 1750 *fore vt*; 2011 1750 *roboamus, in via*; 2223 1738 *qui,Ieroboamo*, 1750
    *qui Ieroboamo*; 2133 1750 *filonium*. The page is the reading.

### Omission check (1 Kgs 11:16 – 13:6, against the BSB)
Every verse read against the BSB; every printed text line of the three leaves has its row, and the page lacks nothing
the Hebrew has beyond Castellio's paraphrase. Points of note, none an omission:
- 11:16–28 (first sitting): every clause present (the vote had lost *seruus*, 1997; restored).
- 11:27–28 *the reason he rebelled … Solomon had built the Millo … Jeroboam was a mighty man of valor … put him in charge
  of the whole labor force of the house of Joseph* = *conspirationis caussa … Mellonem ædificante … vir robustus …
  vniuerso Iosepheorum tributo præposuit*.
- 11:29–31 *Ahijah the Shilonite … a new cloak … twelve pieces … ten pieces … ten tribes*: all present.
- 11:33 *Ashtoreth … Chemosh … Milcom … nor done what is right in My eyes, nor kept My statutes and judgments* = *vt
  mihi obtemperent, mea placita, instituta, sententias exsequuntur*.
- 11:34 *all the days of his life* = *quamdiu viuet*; 11:36 *a lamp* = *lucernam* (note *b) posteritatem*).
- 11:37 *you shall reign over all that your heart desires* = *imperabisque Israelitis tuo arbitratu*.
- 11:38 *I will be with you. I will build you a lasting dynasty … and I will give Israel to you* = *adero tibi, et domum
  tibi firmam construam … Israelitasque tib tribuam*.
- 11:40–43: Shishak = *Sesacum*; forty years; *Rehoboam reigned in his place*: present.
- 12:1–7: every clause present; 12:3 *So they sent for Jeroboam* = *arcessitus aduocatusque*; 12:5 *So the people
  departed* = *Atque illis digressis*; 12:7 *If you will be a servant to these people and serve them this day* = *si in
  præsentia illis obsequatur*.
- 12:10 *who had grown up with him* is not repeated in Castellio's 10 (said in his 8, *qui cum eo educati*); *waist* =
  *medium corporis truncum*. A rendering.
- 12:12 *since the king had said, Come back to me on the third day* = *sicut ab eo iussi fuerant*.
- 12:16 *son of Jesse* = *in Isæida*; *To your tents, O Israel* = *domum discedendum Israelitis esse*.
- 12:18 *in charge of the forced labor* = *tributi præfectum*; 12:21 180,000 = *centum octoginta millia*.
- 12:22–24 *Shemaiah the man of God* = *Semeiæ diuino*; *this word is from Me* = *se enim illius esse auctorem rei*.
- 12:25–33: Shechem, Penuel; two golden calves; *too much for you* = *nihil iam opus esse*; Bethel and Dan; *this became
  a sin* = *offensam attulit*; *priests who were not Levites* = *a Leui non ortos*; *fifteenth day of the eighth month*
  (twice: 2207–2208, 2216–2217); *a month of his own choosing* = *quem mensem ad suam libidinem commentus erat*; *burned
  incense* = *adolendi caussa*.
- 13:1–6a: *by the word of the LORD* (*iussu Iouæ*, twice); Josiah; *priests of the high places* = *sacellanos
  sacerdotes*; *That day the man of God gave a sign* = *tum prodigium dans*; the withered hand; the altar split; 13:6
  begins *Hic rex diuinum adloquitur: ora, quæso, in-|quit* (to the end of the range).

### Uncertain readings to check
- **Ch. 12:2–7 verse numbers** (rows 2079, 2083, 2086, 2091, 2093, 2098): the margin is lost in the gutter of
  `1738-page-0407.jpg` (x 0–40, y 1500–2500); placed by sense; 3 may stand at *postquam* (2082) rather than *arcessitus*.
- **Row 2029 *Mclcomum***: *c* or a broken *e* (`1738-page-0406.jpg`, col. 1).
- **Row 2055 *tib***: misprint as printed (`1738-page-0407.jpg`, col. 0, line 6).
- Row 2125 verse 13 at *meus* (the margin number beside the line; KJV 14 begins at *iuuenum consilium secutus*).

### Counts
- Rows written: **294** (rows 1950–2246 less 6 removed, plus 3 added): 51 from the first sitting (50 voted rows and the
  footnote *b)*), 243 from the second (241 voted rows including `\c 12` and `\c 13`, plus footnotes *c)*, *d)*).
- Removed: **6** (2000, 2001, 2052, 2075, 2149, 2201). Added: **3** (footnotes *b)*, *c)*, *d)*).
- Changed from the vote: **214** (34 in rows 1950–1999; 180 in rows 2002–2246, including 2148 → `% Y 3 ob-` and
  2214 → `\c 13`). No partial row changed.

---

## reader-09-10 (`reader-09-10.md`)

## Readers 09–10: rows 2247–2658 (1 Kgs 13:4 [1738's numbering] *quit, Iouam* – 14:20 *Nadabus eius filius.*)

Read in one sitting after the pause (`reader-09.partial.*`, `reader-10.partial.*` kept as they are; they read no row).
`reader-09.tsv` = leaf 409's rows (2247–2348); `reader-10.tsv` = leaf 414's rows (2559–2658). Rows 2349–2558 (the
vote's leaves 410–413) are archive.org's second shots of pages printed on leaves 414 and 415: removed, block by block
below. Leaves 409 and 414 are consecutive printed pages (343, 344): 409 ends *non re-|cessit Ieroboamus a suis malis
mo-* with the catchword *ribus,* and 414 begins *ribus, sed etiam iterum*, so nothing printed falls between them.

**Images.** Named by leaf (the fixed names; the partial notes' image names are the old, wrong ones): leaf 409 =
`sources/archive/crops/1738-page-0409.jpg` (head *Cap. 13. | REGVM LIBER III. | 343*), leaf 414 = `1738-page-0414.jpg`
(*344 | REGVM LIBER III. | Cap. 14.*); leaf 415 = `1738-page-0415.jpg` (p. 345, *Cap. 14. 15.*) looked at only for the
duplicate check and its foot. Read from whole-column strips at 1.3× with 3–8× zooms on doubtful letters, line-end
hyphens and spacing (scratch `scratchpad\r0910\`); the sheets were not needed. 1750 (`sources/archive/1750/text.txt`,
lines 49072–49320) read alongside for the numbers and the wording. The doubts file has no rows on these leaves.

### Leaves
- **Leaf 409** (p. 343): col. 0 (lines 4–54) = 13:4 *quit, Iouam Deum tuum* – 13:20 *Ioua cum di-* (rows 2247–2297);
  col. 1 (lines 55–105) = 13:20 *uino vate* – 13:33 *a suis malis mo-* (rows 2298–2348). Signature **Y 4** and catchword
  **ribus,** at the foot: not in the vote, not added (as reader 08). Running head not in the vote. No footnotes.
- **Leaves 410–413**: no image (`archive.skipped_leaves`); their rows are duplicate shots, all removed (below).
- **Leaf 414** (p. 344): col. 0 (lines 4–54) = 13:33 *ribus, sed etiam* – 13:34, rule, *CAPVT XIIII.*, its six-line
  italic summary (*Regia coniux ad vatem. Huius solertia, in regem comminationes. Reginæ digressio. Annales
  Israelitarum. Roboami imperium in Iudæis. Iudæi idololatræ. Aegyptiorum in Hierosolymam expeditio. Roboami, et
  Ierobami bella. Illius mors.*), then 14:1 *PEr id tempus* – 14:9 *vt mei* (rows 2559–2607 less the summary rows);
  col. 1 (lines 55–105) = 14:9 *irritandi caussa* – 14:20 *Nadabus eius filius.* (rows 2608–2658). Catchword **At**
  under col. 1 (p. 345 begins *At Roboamus*): not in the vote, not added. No footnotes, no signature.

### Chapter 14
The vote **has** `\c 14` (row 2566, line 11) where 1738 prints *CAPVT XIIII.* below the rule after *euerteretur.*;
copied unchanged, so **no `\c 14` row was added** (the brief to me said the OCR missed it; it did not miss the `\c`,
only the drop capital *P* and the summary's first two lines, which are not text). The summary's last four lines
(rows 2567–2570, *Annates Israelitarum … Illius mors.*, with a stray `#1`) **removed**. 1738 prints the heading
*XIIII* (four I's).

### Verse numbers (1738's margins; all legible, none cut)
The vote's numbers were a running count (#5–#27 on 409, #32 and #1–#16 on 414) and wrong throughout; every one placed
again. Castellio's ch. 13 = KJV from 3 (reader 08), so 7–34 here = KJV 13:7–34.
- **ch. 13, leaf 409 col. 0** (left margin): 7 *Atque* (2251, margin beside *et in priorem statum redit. Atque*; placed
  after the stop and wide space; KJV 7 *the king said*); 8 *Cui ille* (2254); 9 *Nam a Ioua* (2258); 10 *Hoc edicto*
  (2261); 11 *Erat Bethele* (2264, line start, indented); 12 *Tum pater* (2268); 13 *mandat* (2273, line start);
  **14 *et eum* (2275)**, margin *14* beside *dit, diuinumque subsequitur: et*: placed at *et* after the colon and the
  wider space (1750's OCR also has *14* after *et*); by sense (KJV 14 *and went after the man of God*) it could stand at
  *diuinumque* (see Uncertain); 15 *Quum-|que* (2278); 16 *Cui ille* (2281); 17 *propterea* (2285, after *esse,* and a
  wide space); 18 *At il-|le* (2288); 19 *Ita* (2294); 20 *His* (2297, line start, flush).
- **ch. 13, leaf 409 col. 1** (right margin): 21 *hæc est* (2300, after *clamat:* and a wide space); 22 *sed* (2303);
  23 *Igitur* (2308); 24 *Quumque* (2312); 25 *accidit* (2314, line start); 26 *Hac re* (2319); 27 *Deinde* (2325, line
  start, flush); 28 *eoque* (2326); 29 *Tum vates* (2331); 30 *eumque* (2336, line start); 31 *Illo* (2337); 32 *Etenim*
  (2342); 33 *Post* (2347, line start, flush).
- **ch. 13, leaf 414 col. 0**: 34 *Quæ res* (2562; margin *34*).
- **ch. 14, leaf 414 col. 0** (left margin): 1 *PEr* (2571, drop capital; margin *1*); **2 *Illic enim* (2575)** (margin
  beside *Siluntem se conferat. Illic enim*; Castellio's 1 = KJV 1–2a, his 2 = KJV 2b *For Ahijah the prophet is
  there*); 3 *Igitur* (2577); 4 *Vxor* (2581); 5 *Eum autem* (2584); 6 *Igitur illa* (2588); 7 *I sic* (2594, line start,
  flush); **8 *ere-|ptoque* (2598)** (margin beside *litarum imperio præfeci, ere-*, after the comma and a wide space;
  KJV 8 *I tore the kingdom*); 9 *vt etiam* (2605, line start; the vote's #6 after *omnes,* was wrong).
- **ch. 14, leaf 414 col. 1** (right margin): 10 *propterea* (2609); 11 *eius-|que* (2616; Castellio's 11 = KJV 10b–11,
  *I will burn up the house … dogs … birds*); 12 *Itaque* (2622); 13 *Nam hic* (2626); 14 *Suscitabitque* (2631); 15 *Nec*
  (2633); 16 *eosque* (2640); 17 *Tum* (2644, line start, flush); 18 *et a cunctis* (2647); 19 *De* (2650); 20 *Regnauit*
  (2654). From 12 = KJV.

### Letters lost in the gutter
None (both pages' margins and line ends whole).

### Misprints and odd forms, kept as printed
- **2599 *ptoque*** (14:8, *ere-|ptoque*): the *o* is weak on its right side and at 8× could be taken for a *c* (the
  vote and its leaf-412 duplicate read *ptcque*); its bowl is round and closed-looking against the open, hooked *c* of
  *dauidicæ* on the same line: read *ptoque*. To check (`1738-page-0414.jpg`, about x 100–190, y 2198–2248).
- No space after the comma: 2561 *cit,et … fuit,ad*; 2579 *guttum,et*; 2607 *deueneris,vt* (zoomed 3×).
- Set tight, written with the spaces: 2252 *eum sic*; 2299 *ille retraxerat*; 2313 *asinus et leo* (looks *asinuset*).
- *sumsisti* (2305, as printed, not *sumpsisti*); *comminctorem* (2616, *ct* ligature; vote *comminctorem*, the leaf-412
  shot *comminclorem*); *caussa* / *causſa* (2563, 2608); *dauidicæ* lower case (2599); *Ahiam*, *Ahiæ*, *Ahias* (2576,
  2582, 2589, 2650; vote *Ablata*, *Abiæ*, *Abias*); *Abia* the son (2572); *Siluntem* (2575, 2582); *Thersam* (2645);
  *ædium* (2646); *aeris* with *ae* (2621, not *æ*, as printed).
- 2293 *pòtionemque*: a dot above the *o* (4×), round, not an accent stroke: a speck; written *potionemque*.
- *( qui* (2601) has a thin space after the parenthesis: written *(qui*.
- Drop capital: 2571 **PEr** (P three lines deep, 2572–2573 set in beside it; *E* a capital).

### Paragraph indents and drop capitals
- Indented: **2264** (13:11 *Erat Bethele*, after the short line *qua Bethel venerat.*).
- Drop capital: **2571** (14:1 *PEr*), with 2572–2573 set in beside it.
- Every other line starts flush (2297 *His*, 2314 *accidit*, 2325 *Deinde*, 2336 *eumque*, 2347 *Post*, 2594 *I sic*,
  2605 *vt etiam*, 2644 *Tum* are flush).

### Footnotes, marks, asterisks
- No footnotes on leaves 409 and 414; no *G.*, *L.*, *H.* marks; no asterisks.

### Removed duplicate blocks (rows 2349–2558, 210 rows) and what each repeats
Checked word by word against the voted rows of leaves 414 and 415 (and against page 415's foot for one line). Every
row is a piece of a line printed on p. 344 (leaf 414) or p. 345 (leaf 415), or noise outside the text block.
- **Leaf 410 (rows 2349–2366, 18 rows)**: a part-shot of p. 344's top. 2349 = 2562 (*dotia inaugurauit. Quæ res in*);
  2350 = 2565; 2351 = 2604 (*hi accepta forent) similis*; this shot has the line the vote had lost on 414, see below);
  2352–2353 = p. 344's running head (*REGVM LIBER III.*, *Cap. 14.*, with a stray `#28`); 2354 = 2559; 2355 = 2608
  (*… caussa deos alienos et c*, its start garbled to *hominum*); 2356 = 2560; 2357 = 2609; 2358 = 2610; 2359 = 2561; 2360
  = 2611; 2361 = 2563; 2362 = 2612; 2363 = 2564; 2364 = 2613; 2365 = 2614; 2366 = 2615.
- **Leaf 411 (rows 2367–2413, 47 rows)**: a part-shot of p. 345's foot and col. 1 (= leaf 415). 2367 `\c 15` = 2701;
  2368 = 2749 (*et vasa in ædem Iouæ intulit.*); 2369 (*Jflrwrx. IirseS&SM*) = the italic summary of *CAPVT XV*
  (hOCR box just below the `\c 15` line, x 650–1076, y 3229); 2370–2371 = 2702–2703 (*HVic in regnum … Abia-|mus*);
  2372 = 2753 (*Baasa expeditionem fecisset in*); **2373 (*«) pofieriotem. /) H. Re bean am. j) me.*) = p. 345's
  footnote line** *e) posteritatem. f) H. Roboamum. g) auia.* (seen on `1738-page-0415.jpg`; the vote has **no row** for
  it under leaf 415, so reader 11 must add these three notes); 2374–2390 = 2704–2720 (15:1–5); 2391 (*#6 Abia*) = the
  right end of 2725 (*… Hic Abi-*); 2392 (*Is*) and 2393 (*H;;A;:.*) = pieces of 2726 (hOCR boxes on the same line, y
  2023); 2394–2397 = 2727–2730; 2398 = 2731; 2399–2406 = 2733–2740; 2407–2409 = 2743–2745; 2410 = 2747; 2411–2413 =
  2750–2752.
- **Leaf 412 (rows 2414–2498, 85 rows)**: a shot of p. 344 with the right part of col. 0 and the foot of col. 1 cut
  (the partial's reader 10 saw the same). 2414 (*m m m mm jm.mm-h.*) = noise along the image's top edge (hOCR box y
  0–82, above the page); 2415–2421 = 2559–2565 (left parts); 2422 (*capvt :*) = *CAPVT XIIII.*; 2423–2428 = the six
  lines of the ch. 14 summary (the first two not in the vote's leaf 414 either; the last four = 2567–2570); 2429–2465 =
  2571–2607, line for line (left parts; 2462 *hi ecce* = 2604 *hi accepta*); 2466 (*si)*), 2467 (*st*), 2468 (*Vt*):
  **three one-to-three-letter marks with hOCR boxes above the page's running head** (x 2133–2167, y 304–740; the head
  *LIBER III. Cap. 14.* is at y 824): outside the text block, matching no printed line; removed as noise, since p. 343
  runs on to p. 344 with nothing between (flagged in case Claude wants them kept); 2469–2471 = p. 344's running head
  (*LIBER III.*, *REGV[M]*, *Cap. 14.*); 2472–2495 = 2608–2631 (2492–2495 right-cut); 2496 (*is*), 2497 (*CO*), 2498
  (*At*) = the right ends of 2656 *suis* and 2657 *loco* and the catchword **At** (hOCR boxes at the foot of col. 1, y
  3280, 3330, 3415, the gap before *At* where *filius.* would be).
- **Leaf 413 (rows 2499–2558, 60 rows)**: a shot of p. 345 with both columns cut and interleaved. 2499–2500 = p. 345's
  running head (*Cap. 14. 15.*, *[REG]VM LIBER III.*); the col.-0 lines 11–39 (2502, 2504, 2506, 2508, 2510, 2511,
  2513, 2516, 2518, 2520, 2522, 2524, 2526, 2528, 2529, 2531, 2533, 2535, 2537, 2539, 2542–2550) = 2659–2687 (14:21–27,
  left parts); the lines 40–62 (2501, 2503, 2505, 2507, 2509, 2512, 2514, 2515, 2517, 2519, 2521, 2523, 2525, 2527,
  2530, 2532, 2534, 2536, 2538, 2540, 2541) = 2704–2724 (15:1–6, with p. 345's margin numbers and gutter letters of
  col. 0 at their starts: *1a-*, *it,*, *y-*, *:x*, *e-*, *o-*, *m*, *is*, *n*, *t*, … and *3*, *4*, *5*, *7* at their ends);
  col. 1 lines 63–70 (2551–2558) = 2725–2732 (right parts).
- So **every** row 2349–2558 repeats text printed on leaf 414 or 415 (or is noise with no text), and none carries a
  line missing from leaves 409/414/415 except the two the vote had lost: p. 344's *hi accepta forent) similis fueris,*
  (read here on the page, row 2604) and p. 345's footnote line (for reader 11).

### Lost / added / removed
- **Line the vote merged on leaf 414**: col. 0 lines 50–51. The vote had 2603 *obsecutus, ea demum fecit, quae a-* and
  2604 *ccepta forent) similis fueris,*; the page prints **2603 *obsecutus, ea demum fecit, quæ mi-*** and **2604 *hi
  accepta forent) similis fueris,*** (zoomed; 1750 *quae mi-|hi accepta forent*; leaf 410's shot *hi accepta forent*):
  the vote had dropped *mi-|hi*. No row added (the two rows carry the two lines).
- Removed: **214** rows: 2349–2558 (210, the duplicate shots) and 2567–2570 (4, the ch. 14 summary).
- Added: none. `\c 14` (2566) copied unchanged.
- No text line lost on leaves 409 and 414 (line numbers run on: 409 col. 0 4–54, col. 1 55–105; 414 col. 0 4–11,
  18–54, col. 1 55–105; 12–17 the heading and summary).

### Wording doubts (1738 against 1750; the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops and the numbers): 2250
  *et sua regi manus restituitur* (*etfua … reftifuitur*); 2252 *rex eum sic* (*cum sie*); 2256 *non te comitarer, aut*
  (*autci-*); 2257 *hoc in loco cape-* (*hocinlococape-*); 2261 *edicto profectus* (*edi&o profestus*); 2264 *quidam
  senex* (*qiiidam fewer*, a stray *1*); 2265 *veniunt ipsius filii* (*veniimtipfiusfilii*); 2266 *narrant* (*n errant*);
  2269–2270 *disces-|serit*; 2273 *sibi asinum*; 2274 *inscen-*; 2277 *num sit* (*nam fit*); 2288 *At il-* (*At d-*, a
  stray *6*); 2290–2291 *illum*, *Iouæ* (*ilium*, *iouæ*); 2294, 2297 stray margin digits *9*, *o* dropped; 2299 *ille
  retraxerat … eum* (*illeretraxerat … cum*); 2300 *sic clamat* (*ile clamat*), *Iouæ*; 2303 *exsecutus es*
  (*exfecutuses*); 2305 *sumsisti*; 2313 *asinus et*; 2314–2316 *homi-|nes … pro-|iectum* (*ne» … jec"him*); 2320
  *illum*; 2323 *a quo laceratus* (*aquolaceratus*); 2324 *ei minatus* (*eiminatus*); 2332–2334 *asi-|noque … su-|um ad
  luctum* (*ail-|noque … Al-|um ad ludum*); 2337 *luctu*; 2338 *præcipit, vt se* (*praxipit, vrse*); 2340 *condant*
  (*condantr*); 2343 *Iouæ*; 2559 *ribus* (*ubus*); 2571 *PEr* (*er*); 2573 *suæ mandat*; 2575 *Illic* (*IUle*); 2576
  *Ahiam* (*Ablata*); 2577 *se fore eius regem populi* (*fefbreeius regempopuli*); 2579 *illum*; 2582 *Ahiæ*; 2583
  *cæcutientis* (*excutientis*); 2586 *eum* (*etim*); 2588 *illa* (*ilJa*); 2589 *Ahias simul ac* (*Abias simulac*); 2591
  *dientis audiuit, sic* (*dientisaudiuit, sie*); 2594 *I sic … hæc* (*1 sie … bate*); 2597 *delectum* (*deledhmi*); 2598
  *litarum* (*litai -utu*); 2599 *ptoque dauidicæ*; 2603–2604 *mi-|hi accepta* (above); 2605 *omnes, qui*; 2606 *meque
  post*; 2607 *vt* (*v t*); 2610 *sic*; 2621 *aeris* (*acris*); 2636 *in*; 2640 *uam* (*11 am*); 2646 *ædium limen*
  (*xdiumlimen*); 2647 *et a cunctis* (*eta cundiis*); 2650 *prædixerat*; 2652 *regnauerit*.
- 1738 against 1750 in more than spelling: **none**. Stops only: 1750 *quo instrato infcendit* (1738 *instrato,*); 1750
  *omnes qui* (1738 *omnes, qui*, 2605); 1750 *percussos in modum* (1738 *percussos,*, 2635); 1750 *Vxor, digressa* (1738
  *vxor digressa,*, 2644); 1750 *atque ea* (1738 *atque, ea*, 2645); 1750 *eoque instrato profectus* (1738 *in-|strato,
  profectus*). 1750's *Abja* (14:1) and *iuffit* (13:18) are its OCR.

### Omission check (1 Kgs 13:6b–14:20 against the BSB)
Every verse read against the BSB; every printed line of the two leaves has its row. Points of note, none an omission
by the reading:
- 13:6b–10: the hand restored *as it was before* = *in priorem statum redit*; *half your possessions* = *dimidiam domum
  tuam*; *bread … water … return by the way you came* (9 and 17) present each time.
- 13:11–19: the sons' report of *the deeds* and *the words*; *Saddle the donkey*; the oak; *I am* = *se esse
  respondisset*; *an angel … by the word of the LORD* = *ab angelo iussu Iouæ*; *The old prophet was lying to him* = *hæc
  mentiens dicebat*.
- 13:20–26: all present; 13:21 *have defied the word of the LORD* = *in Iouam Deum tuum contumax*; 13:26 *it has mauled
  him and killed him* = *a quo laceratus necatusque sit*.
- 13:27–34: all present; 13:30 *Oh, my brother!* = *vt fratrem lamentabili luctu*; 13:32 *shrines on the high places in
  the cities of Samaria* = *omnia collina sacella, apud oppida Samariæ posita*; 13:33 *He ordained anyone who desired* =
  *quos ei visum fuit, ad ea sacerdotia inaugurauit*; 13:34 = *Quæ res in caussa fuit …*.
- 14:1–6: present; 14:5 *because when she arrives, she will be disguised* is carried by 6 *seque dissimulante* (a
  rendering).
- 14:7–11: present; 14:10 *every male, both slave and free* is rendered by *nihil neque tam abstrusum … neque tam
  obuium* and *ad comminctorem parietis*; *as one burns up dung* = *quam simus … abstergi solet*.
- **14:14b *This is the day—yes, even today!***: not on the page (Castellio's 14 ends *aliquando eruat.*); the page
  lacks it, not the reading.
- 14:15–20: present (*Asherah poles* = *lucis*; *beyond the Euphrates* = *transque flumen*; Tirzah = *Thersam*;
  twenty-two years; Nadab).

### Uncertain readings to check on the page
- **13:14's number** (row 2275): margin *14* beside *dit, diuinumque subsequitur: et*; placed at *et* (wide space after
  the colon, as 1750's OCR); by sense it may belong at *diuinumque* (`1738-page-0409.jpg`, col. 0, about y 1460–1500).
- **Row 2599 *ptoque*** (or *ptcque*): `1738-page-0414.jpg`, col. 0, about x 100–190, y 2198–2248.
- **Rows 2466–2468** (leaf 412, *si)*, *st*, *Vt*): removed as noise above the running head; no image exists to confirm.

### Counts
- Rows written: **198** (102 in `reader-09.tsv`, leaf 409; 96 in `reader-10.tsv`, leaf 414), including `\c 14`.
- Removed: **214** (rows 2349–2558, 210; rows 2567–2570, 4). Added: **0**.
- Changed from the vote: **131** (72 on leaf 409, 59 on leaf 414).

---

## reader-11 (`reader-11.md`)

## Reader 11: rows 2659–2953 (1 Kgs 14:21 *At Roboamus* – 16:31 *in matrimonium duxit, et eo*)

Read in one sitting after the pause (`reader-11.partial.*` kept as they are; they read no row). Every line read on the
page images, named by the voted leaf (the fixed names): leaf 415 = `sources/archive/crops/1738-page-0415.jpg` (head
*Cap. 14. 15. | REGVM LIBER III. | 345*), leaf 416 = `1738-page-0416.jpg` (p. 346, *Cap. 15. 16.*), leaf 417 =
`1738-page-0417.jpg` (*Cap. 16. | REGVM LIBER III. | 347*). Each column read in four native-resolution strips, with 2–3×
zooms on doubtful letters, stops and spacing (scratch `scratchpad\r11\`); the sheets were not needed. 1750
(`sources/archive/1750/text.txt`, lines 48968–49760) read alongside for numbers and wording. The doubts file has no rows
on these leaves. The partial's working draft was not used.

### Leaves
- **Leaf 415** (p. 345): col. 0 (lines 4–52) = 14:21 *At Roboamus* – 14:31 *Ammo-|nitis.* (rows 2659–2700), rule,
  *CAPVT XV*, four-line italic summary (not in the vote: nothing to remove), `\c 15` (2701, copied unchanged), 15:1
  *HVic … qui anno duo-* (2702–2703); col. 1 (lines 54–104) = 15:1 *devicesimo* – 15:17 *fecisset in Iu-* (2704–2753),
  then the signature and catchword line **Y 5 … dæam,** (2754, made `% Y 5 dæam,`). Foot: the footnote line
  *e) posteritatem. f) H. Roboamum.* under col. 0 and *g) auia.* under col. 1 (below the signature line); the vote had
  no row for any of them (added, below).
- **Leaf 416** (p. 346): col. 0 (lines 4–54) = 15:17 *dæam, Ramamque muniret* – 15:27 *thonem Palæstinorum omnibus*
  (2755–2805); col. 1 (lines 55–109) = 15:27 *Israelitarum copiis* – 15:34 *garat.* (2806–2831), rule, *CAPVT XVI.*,
  five-line italic summary, `\c 16` (2832), 16:1 *ITaque* – 16:5 *Israelita-* (2835–2851), then a lost line **rum.**
  (added) and the catchword **Post-** (not in the vote, not added). No footnotes, no signature.
- **Leaf 417** (p. 347): col. 0 (lines 4–54) = 16:6 *Postquam* – 16:18 *vrbem expu-* (2852–2902); col. 1 (lines 55–105)
  = 16:18 *gnari* – 16:31 *et eo* (2903–2953); catchword **venit,** under col. 1 (not in the vote, not added). No
  footnotes, no signature.

### Chapters
- `\c 15` (2701) and `\c 16` (2832) copied unchanged. *CAPVT XV* (p. 345 col. 0) and *CAPVT XVI.* (p. 346 col. 1).
- Removed: **2833–2834** (`Ambr'u rex. Samaria adificatio. Rex` / `Achabttt. Hiericbuntis injlauratio.`), the last two
  lines of ch. 16's italic summary (*Ambris rex. Samariæ ædificatio. Rex Achabus. Hierichuntis instauratio.*), with the
  vote's stray `#1`.

### Verse numbers (1738's margins; all legible, none cut)
The vote's numbers were a running count and wrong throughout (#17–#22 on ch. 14, etc.); every one placed again. Col. 0
numbers stand in the left margin, col. 1 numbers in the right.
- **ch. 14** (= KJV): 21 *At* (2659; the vote's `I` was the margin *21*); 22 *Offenderunt* (2667); 23 *sibique* (2670,
  after *irritauerant:* and a wide space); 24 *Quin-|etiam* (2673); 25 *Hoc* (2678, indented); 26 *templique* (2681,
  line start); 27 *pro quibus* (2684); 28 *qui eos* (2688, after *misit,* and a wide space); 29 *Reli-|quæ* (2690); 30
  *Fuit* (2693); 31 *Roboamus* (2695).
- **ch. 15**: 1 *HVic* (2702, drop capital); 2 *Regnauit* (2706); 3 *Is omnia* (2708); 4 *Quam-|quam* (2712); **5
  *quoniam* (2717)**: margin *5* at the right end of *quoniam Iouæ obsecutus Dauid, a*; no break inside the line, the
  verse (KJV 5 *For David had done what was right*) begins at its start; 6 *Intercessit* (2720); 7 *De reliquis* (2723);
  **8 *Huic* (2729)** (margin beside *Dauidis. Huic in regnum suc-*; Castellio's 7 runs on through *Hic Abiamus … sepultus
  est in vrbe Dauidis*, KJV 7b–8a; his 8 = KJV 8b–9); **9 *Regnauit* (2732)** (= KJV 10a); **10 *Eius* (2734)** (= KJV
  10b, *mater*/*auia*); 11 *Hic A-|sa* (2735); from 11 = KJV: 12 *effemi-|natos* (2737); 13 *Maacham* (2740); 14
  *Quamquam* (2744); 15 *Patris* (2747); 16 *Inter* (2750, indented); 17 *Quumque* (2752); 18 *cepit* (2757); 19 *fœdus*
  (2764); 20 *Tum Benadadus* (2770); 21 *Quibus* (2776); 22 *Tum rex* (2778); 23 *De reliquis* (2784); 24 *Postquam*
  (2790); 25 *Nadabus* (2794); 26 *In hunc* (2798); 27 *coniura-* (2802); 28 *anno Asæ* (2807, after *terfecit,* and a
  wide space); 29 *quo regno* (2809, line start); **30 *quæ non solum* (2815)**: the margin *30* stands beside this line
  (line start), not beside *xerat, propter Ieroboami scelera:* above it, where KJV 30 (*because of the sins of Jeroboam*)
  begins; placed by the margin (1750 also has *30* at *quae non solum*); 31 *De reliquis* (2819); 32 *Fuit* (2821); 33
  *Anno tertio* (2824); 34 *et contra* (2828).
- **ch. 16** (= KJV): 1 *ITaque* (2835, drop capital); **2 *quoniam* (2837)**: the margin *2* stands at the right end of
  the line *filium, cum Baasa locutus ita est:*, which has no break; the speech (KJV 2) begins with the next line,
  *quoniam*: placed there; 3 *propterea* (2842); 4 *ita vt* (2846); 5 *De reliquis* (2849); 6 *Postquam* (2852,
  indented; the vote's `J` was the margin *6*); 7 *Igitur* (2855); 8 *quum an-|no* (2862, after *iri:* and a wide
  space); 9 *coniurauit* (2866); **10 *vulneribus* (2872)**: margin *10* beside *vulneribus interfecit, anno Asæ*; no
  wider space inside the line, so placed at its start (KJV 10 *Zimri went in and struck him*; *adgressus* ends the line
  above); 11 *eo-|que* (2874); 12 *vniuersamque* (2878, line start, flush); 13 *propter tot* (2881); 14 *De reliquis*
  (2887); 15 *Anno* (2890, line start, flush); 16 *Nam* (2893, flush); 17 *Cumque* (2899); 18 *At Zambris* (2902,
  flush); 19 *At-|que* (2904); 20 *De reliquis* (2909); 21 *Tunc* (2913, indented); 22 *Sed* (2917); 23 *quod regnum*
  (2920); 24 *quorum* (2922); 25 *Adeo* (2928); 26 *omnesque* (2931); 27 *De reliquis* (2936); 28 *Ambri* (2941,
  indented); 29 *quod regnum* (2944, line start); 30 *Hic Achabus* (2947, line start); 31 *etiam* (2951).

### Letters lost in the gutter
None (margins and line ends whole on all three pages).

### Misprints and odd forms, kept as printed
- **2704 *devicesimo*** with a *v* inside the word (zoomed 3×; 1750 *deuigesimo*).
- **2679 *Sesacus;Aegypti***: a semicolon (dot above, tail below, slightly broken) set tight, no space after it
  (zoomed 3×); 1750 has no stop. Kept; a misprint for a space or comma, probably.
- No space after the comma: 2660 *regnauit,vnum*; 2666 *Ammonitis,no-*; 2719 *recesserat,præterquam*; 2758
  *aurumque,quod*.
- Set tight, written with the spaces: 2666 *Eius mater*; 2683 *mnes clipeos aureos*; 2804 *sacharianus genere*; 2810
  *sic interfecit*; 2882 *tum Baasæ*; 2927 *vrbem a Semere*.
- *( quibus* (2801), *( qui* (2869) with a thin space after the parenthesis, *strinxerat )* (2802), *erat )* (2870): written
  without the spaces, as readers 09–10.
- *offendunt* (2936, 16:26; 1750 the same), *Ahiam* (2813), *Ahiæ* (2803, 2825), *Silonium*, *Thebnim*, *Thebni*,
  *Ambrim*/*Ambris*/*Ambri*, *Arsæ*, *Ethbaalis*, *Iezabe-|lem*, *Iosaphatus*, *baasanam* (lower case, 2878),
  *israeliticis* (2664), *israeliticum* (2919, lower case), *tricesimo* (2921; vote *trigesimo*, 1750 *trigesimo*),
  *vicesimo* (2863, 2873, 2890; 1750 *vigesimo* once), *caussa* (2817), *aeris* with *ae* (2848, as 14:11's *aeris*), *Hettæi*,
  *quatuor*, *pædore*, *Hananis* (2856) beside *Ananis* (2835), *Baasa* / *Baasæ*, *Asæ* / *Asa*.
- *auctor*, *recto*, *facta*, *profecti*, *exstructa*, *factis*, *defuncto* printed with the *ct* ligature.
- 2694 *Ieroboamum*: a thin slanting stroke over the second *o* (looks like an acute, *Ierobóamum*); 2695 *bellum*: a small
  mark over the *b*. Both read as specks (no reason for an accent; neither in 1750): written plain. To check.
- 2923 *Thersæ*: the *T* has a stray ink stroke through it (the vote `"Thersae`); the letter is a *T*.
- 2926 *occupauit*: the *u* before *p* is blotted; read *occupauit* (1750 the same).
- Drop capitals: 2702 **HVic** (H two lines deep, 2703 set in beside it); 2835 **ITaque** (I three lines deep, 2836–2837
  set in).

### Paragraph indents and drop capitals
- Indented: **2659** (14:21 *At Roboamus*, top of p. 345, after 14:20's *Nadabus eius filius.* at the foot of p. 344),
  **2678** (14:25 *Hoc Roboamo*), **2750** (15:16 *Inter hunc*), **2852** (16:6 *Postquam*, top of p. 347, after the
  short line *rum.*), **2913** (16:21 *Tunc diuisus*), **2941** (16:28 *Ambri vita*).
- Drop capitals: **2702** (15:1), **2835** (16:1).
- Every other line starts flush (2681 *templique*, 2717 *quoniam*, 2809 *quo regno*, 2815 *quæ non*, 2819 *De
  reliquis*, 2872 *vulneribus*, 2878, 2890, 2893, 2902, 2944, 2947 are flush).

### Footnotes, marks, asterisks
- Footnotes (p. 345; all hang on words in col. 1, so all three rows are put after col. 1's last text row 2753, before the
  signature row 2754, as 2 Samuel's footnote and signature rows; on the page *e)* and *f)* are printed under col. 0 and
  *g)* under col. 1, below the signature line):
  - **e) posteritatem.** (line 900): hangs on *lucernam*, 2714 *eius ei e lucernam concessit* (15:4); letter removed.
  - **f) H. Roboamum.** (line 901): hangs on *Abiamum*, 2721 *inter L. f Abiamum H.* (15:6); letter removed.
  - **g) auia.** (line 902): hangs on *mater*, 2734 *Eius g mater fuit* (15:10); letter removed (the vote `Eius^`).
- *G.*/*L.*/*H.* marks: **2721 *inter L. Abiamum H.*** (italic *L.* and *H.*, kept; 1750 *inter L, Abiamum H.*).
- Asterisk: **2742 *in luco:* eumque*** (15:13), after the colon, with no footnote on the page: taken out. (The partial's
  doubt about 2734 *Eius^* was footnote *g*.)

### Lost / added / removed
- Added (4): **three footnote rows** on leaf 415 col. 1, lines 900–902 (above); **+ 416 1 900 *rum.*** after 2851: the
  short last line of 16:5 (*Israelita-|rum.*), printed above the catchword *Post-*, missing from the vote.
- Removed (2): 2833–2834 (ch. 16 summary).
- Changed: 2754 (`am 5 dacam,`) is the signature line *Y 5* with the catchword *dæam,*: made `% Y 5 dæam,`; the next
  page begins *dæam, Ramamque muniret, vt exi-* (2755; the vote `daeatn, vt, exit-` had lost *Ramamque muniret*) and
  2756 *tum aditumque* (the vote `um adituraquc`): the partial's line-break doubt is settled; no line was lost.
- No other line lost: line numbers run on (415 col. 0 4–52, col. 1 54–104; 416 col. 0 4–54, col. 1 55–109 + *rum.*; 417
  col. 0 4–54, col. 1 55–105).

### Wording doubts (1738 against 1750; the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops and the numbers), among
  them: 2663 *mæ regnauit* (*ymae*); 2666–2667 *Eius … no-|mine* (*Ems … n-|omine*); 2671 *lucos* (*Incos*); 2673–2674
  *Quin-|etiam … effemi-* (*Qirin- … eftemi-*); 2680 *Hierosolymam* (*Hierolblymam*); 2689 *et in stipa-*
  (*etinftipa-*); 2695 *bellum* (*bellutn*), *post-* (*port-*); 2702–2703 *HVic … Abia-|mus* (*T "I Vie … Abi-|a~| mus*);
  2705 *filii* (*lilii*); 2714 *ei lucernam* (*ei f lucernam*); 2715 *filio* (*lilio*); 2721 *inter L. Abiamum H.*
  (*inter Z. /AbiamumJf.*); 2723 *Abia-|mi* (*Ara-|mi*); 2725 *Iudææ.* (*Iudaea? .*); 2739 *facta* (*facia*); 2742 (the
  asterisk); 2757 *intercluderet* (*tnterchideret*); 2761 *ta misit Benadado Tabremmonis* (*ta it Eenadado
  Tabremraonis*); 2765 *interque meum et tuum patrem*; 2771 *sæ regi morem* (*ix. regi raorem*; 1750 *Asae regi*);
  2772 *suorum* (*sitorum*); 2774 *et Abelmaacham, totaque* (*erAheimaacham, totaqne*); 2777 *Ramæ* (*Rem\**); 2779 *Iudæos
  omnes, nullo immuni* (*Indvces otanes, nullo imnuini*); 2786 *quæ gesserit, et quæ* (*qu.tgesferit, etquaccon-*);
  2794 *Iosaphatus, eius filius* (*Icuaphatus, eiusfiiius*); 2802 *imitantem* (*imiiantem*); 2803 *Ahiæ* (*Abi«*); 2811
  *in vita relin-* (*invitarelin-*); 2813 *Ahiam* (*Abiam*); 2825 *Ahiæ* (*Abiae*); 2835 *ITaque* (*Teque*); 2842
  *sceleribus offendar* (*feeler ibus ostendar*); 2844 *sic adfici-* (*sie adrlci-*); 2848 *is ab aeris* (*isabaeris*);
  2859 *offenderat* (*ostenderat*); 2861 *Ieroboami* (*Ieroboarai*); 2864 *Baasæ* (*Baafc*); 2871 *ebrium*
  (*ebriura*); 2875 *solii* (*folii*); 2893 *Nam* (*6Nam*); 2899 *gem in castris* (*7gemincaftris*); 2902 *At* (*&At*);
  2905 *ita* (*lea*); 2911 *annalibus* (*annalibuj*); 2915 *Thebnim* (*1 htbnim*); 2921 *tricesimo* (*trigesimo*); 2926
  *exstructa* (*exftrucla*); 2931 *antecesserit* (*anlecesferit*); 2952 *Ethbaalis Sidoniorum* (*Etlibaalis
  Sidonicrnm*).
- 1738 against 1750 in more than spelling: **none**. Stops only: 1750 *Sesacus Aegypti* (1738 *Sesacus;Aegypti*); 1750
  *Ioua Deus eius, ei lucernam* (1738 *Ioua, Deus eius ei*); 1750 *Iehum Ananis* / *Iehum Hananis filium vatem Ioua*
  (1738 *Iehum, Ananis*; *Iehum, Hananis filium vatem, Ioua*); 1750 *Ela Baasae filius* (1738 *Ela, Baasæ filius,*);
  1750 *videns vrbem expugnari,* (1738 *videns, vrbem expu-|gnari:*); 1750 *milites ad* (1738 *milites, ad*); 1750
  *gestis, scriptum* (1738 *gestis scriptum*, 2820, 2888). 1750 *vigesimo sexto*, *trigesimo* are spellings.

### Omission check (1 Kgs 14:21–16:31a against the BSB)
Every verse read against the BSB; every printed line of the three leaves has its row. Points of note, none an omission
by the reading:
- 14:21–31: all present (Naamah the Ammonite twice, 21 and 31, as the Hebrew; Shishak; the bronze shields and the
  guardroom; *war … all their days* = *perpetuum bellum*). 14:31 *And his son Abijam reigned in his place* is not in
  Castellio's 14:31: it opens 15:1 (*HVic in regnum successit Abiamus eius filius*), a rendering, not a loss.
- 15:1–8: present; 15:2 *Maacah daughter of Abishalom* = *Maacha, Absalomi filia*; 15:4 *a lamp* = *lucernam* (note
  *e*); 15:6 *Rehoboam* = *L. Abiamum H.* with note *f* (*H. Roboamum*); 15:8 *Abijam rested … Asa his son reigned*
  = *Hic Abiamus … sepultus est … Huic in regnum successit Asa*, with KJV 7b's *war between Abijam and Jeroboam*
  (*Hic Abiamus bellum gessit cum Ieroboamo*).
- 15:9–24: present; 15:10 *grandmother* = *mater* with note *g* (*auia*); 15:13 *obscene image … Kidron* = *Pana …
  Cedronem*; 15:17 *fortified Ramah* = *Ramamque muniret*; 15:20 the towns *Ijon, Dan, Abel-beth-maacah, all
  Chinnereth … Naphtali*; 15:22 *no one was exempt* = *nullo immuni*; *Geba … Mizpah* = *Gabaam … Maspham*; 15:23
  *diseased in his feet*.
- 15:25–34: present; 15:27 *of the house of Issachar* = *Issacharianus genere*; Gibbethon twice; 15:29 *not leaving
  … anyone that breathed* = *nullum prorsus in vita*.
- 16:1–7: present; 16:7 *and also because he struck it down* is given as *eumque occisum iri* (a rendering).
- 16:8–20: present (Arza the steward; *not even a male … kinsmen or friends* = *cognatos, amicos funditus ad vnum*;
  *the citadel of the king's house* = *regiæ palatium*).
- 16:21–31a: present (Tibni son of Ginath; two talents; Shemer; Ethbaal king of the Sidonians). The range ends at *et
  eo* (16:31b *venit, vt …* is on leaf 418).

### Uncertain readings to check on the page
- **15:30's number** (row 2815): margin *30* beside *quæ non solum*; KJV 30 begins at *propter Ieroboami scelera* on the
  line above (`1738-page-0416.jpg`, col. 1, about y 560–620). Placed by the margin.
- **16:10's number** (row 2872): placed at the line start *vulneribus*; by sense it could stand at *anno Asæ*
  (`1738-page-0417.jpg`, col. 0, about y 1150).
- **16:2's number** (row 2837): margin *2* at the end of the line above; placed at *quoniam*.
- **2694 *Ieroboamum*, 2695 *bellum***: stray strokes read as specks (`1738-page-0415.jpg`, col. 0, about y 1850–1910).
- **Footnote row order**: footnotes put before the signature row (2 Samuel's order), though on the page *g) auia.* is
  printed below the signature line *Y 5 … dæam,*.

### Counts
- Rows written: **297** (leaf 415: 99, incl. `\c 15`, the 3 footnotes and the signature row; leaf 416: 96, incl.
  `\c 16` and the added *rum.*; leaf 417: 102), from the range's 295 rows.
- Removed: **2** (2833–2834). Added: **4** (three footnotes, *rum.*).
- Changed from the vote: **218** (66 on leaf 415, 79 on leaf 416, 73 on leaf 417).

---

## reader-12 (`reader-12.md`)

## Reader 12: rows 2954–3243 (1 Kgs 16:31b *venit,vt Baalem* – 19:2 *Iezabel Eliæ per nunti-*)

Read in one sitting after the pause (`reader-12.partial.*` kept as they are; they read no row). Every line read on the
page images, named by the voted leaf (the fixed names): leaf 418 = `sources/archive/crops/1738-page-0418.jpg` (head
*348 | REGVM LIBER III. | Cap. 17.*), leaf 419 = `1738-page-0419.jpg` (*Cap. 18. | REGVM LIBER III. | 349*), leaf 420 =
`1738-page-0420.jpg` (*350 | REGVM LIBER III. | Cap. 18.19.*). Each line read on the reading sheets
`sources/archive/crops/sheets/lines/1Kgs1-22.voted-210.jpg` … `-231.jpg` (labels 2946–3256), with the whole pages for
margins, indents, the chapter openings and the feet, and 2–6× zooms on doubtful letters, stops and spacing (scratch
`scratchpad\r12\`). 1750 (`sources/archive/1750/text.txt`, lines ~49740–50100) read alongside for numbers and wording.
The doubts file has no rows on these leaves.

### Leaves
- **Leaf 418** (p. 348): col. 0 (lines 4–52) = 16:31b *venit,vt Baalem* – 16:34 *dixerat.* (2954–2969), rule, *CAPVT
  XVII.*, two-line italic summary (*Elias de siccitate. … Mulieris confessio pia.*), `\c 17` (2970), 17:1 *ELias* – 17:10
  *eique clamat,* (2972–3001); col. 1 (lines 53–103) = 17:10 *vt sibi paullum aquæ* – 17:23 *domum ex cubiculo depor-*
  (3002–3052). Catchword **tatum,** under col. 1 (not in the vote, not added). No footnotes, no signature.
- **Leaf 419** (p. 349): col. 0 (lines 5–52) = 17:23 *tatum, matri reddidit* – 17:24 *nuntium.* (3053–3057), rule,
  *CAPVT XVIII.*, four-line italic summary (*Ad Achabum Elias. … interfecti. Pluuiæ restitutio.*), `\c 18` (3058), 18:1
  *LOngo* – 18:12 *Qui postquam a* (3060–3097); col. 1 (lines 55–103) = 18:12 *te digressus fuero* – 18:23 *superque
  lignis constituam,* (3098–3146); catchword **ne-** under col. 1 (not in the vote, not added). Foot: one footnote line
  across both columns, *h) scilicet per Deum, vt dicerent, an tu illic esses,   i) lucorum.   k) ambigua* / *sententia
  nutatis?*; the vote had no row for it (added, below).
- **Leaf 420** (p. 350): col. 0 (lines 4–54) = 18:24 *neque ignem supponam* – 18:36 *accedit E-* (3147–3197); col. 1
  (lines 55–103) = 18:36 *lias vates* – 18:46 *zrael ventum est.* (3198–3238), rule, *CAPVT XIX.*, three-line italic
  summary (not in the vote: nothing to remove), `\c 19` (3239), 19:1 *POstquam* – 19:2 *nunti-* (3240–3243); catchword
  **um** under col. 1 (it is reader 13's row 3244 *ium*: the vote's *ium* has a stray *i*; the page has *nunti-|um*).
  No footnotes, no signature.

### Chapters
- `\c 17` (2970), `\c 18` (3058), `\c 19` (3239) copied unchanged.
- Removed: **2971** (`#1 Mulieru confessio pia.`, the last line of ch. 17's italic summary, *Mulieris confessio pia.*) and
  **3059** (`#1 interfefli. Pluui* rtftitutio.`, the last line of ch. 18's, *interfecti. Pluuiæ restitutio.*), with the
  vote's stray `#1`s (moved to the chapters' first text rows).

### Verse numbers (1738's margins; col. 0 numbers left, col. 1 right)
The vote's numbers were a running count and wrong throughout; every one placed again.
- **ch. 16**: 32 *et ei aram* (2955, line start; the vote's `%` was the margin *32*); 33 *Præ-|terea* (2956, after
  *erigeret.* and a wide space; the vote's `3` was the margin *33*); 34 *Eius* (2961, line start; the vote's `4`).
- **ch. 17** (= KJV): 1 *ELias* (2972, drop capital); 2 *Sic autem* (2978, after *meum.* and a wide space); 3 *discede*
  (2979); 4 *Ego* (2983); 5 *Ita ille* (2984); 6 *ibi* (2987); 7 *Sed quum* (2991); 8 *iussit* (2993); 9 *sese enim*
  (2995); **10 *Tum ille* (2997)**: margin *10* at the start of *daturum esse,vt eum aleret. Tum*; the verse (KJV 10 *So he
  arose*) begins at *Tum* after a wide space; 11 *Quumque illa* (3003); 12 *Sed illa ita* (3005); 13 *Cui Elias:*
  (3013); 14 *Nam* (3019, line start, flush); 15 *Tum illa* (3023); 16 *quum in-|terea* (3026); 17 *Post eas* (3031,
  indented); 18 *Itaque* (3033); 19 *Tum Elias* (3037); 20 *De-|inde* (3040); 21 *Tum sese* (3045, line start, flush);
  22 *Hac* (3048); 23 *atque* (3050); 24 *Cui mulier* (3054, after *inquit.* and a wide space).
- **ch. 18** (= KJV in count; the verse divisions are Castellio's): 1 *LOngo* (3060, drop capital); **2 *Igitur Elias*
  (3064)**: the margin *2* stands two lines higher, beside *chabo ostensum eat: sese plu-* (3062) at the foot of the drop
  capital, a line with no break; placed at *Igitur* (line start; KJV 2 *So Elijah went*; 1750 also has *2* at *Igitur*);
  3 *Quum autem fame* (3065; = KJV 2b, the famine); 4 *quumque Iezabel* (3069); 5 *eique* (3074, after *tauerat )*); 6
  *Quumque* (3079, indented); 7 *Ab-|dias* (3081); **8 *Cui ille* (3085)**: margin *8* at the line start *Elias? inquit.*;
  placed at *Cui ille: sum.* after a wide space (KJV 8 *Yes, he replied*); 9 *At ille* (3087, margin at *liam.*); 10 *Ita
  viuat* (3089); 11 *Et tu* (3095); 12 *Qui postquam* (3097); 13 *nisi forte* (3103); 14 *Et tu* (3109, flush); 15 *At
  Eli-|as* (3111); 16 *Tum Abdias* (3114); 17 *Et Achabus* (3116); **18 *non e-|go* (3119)**: margin *18* at the line end
  beside *non e-*; placed there (*Cui ille:* is the lead-in; KJV 18 *And he answered, I have not troubled Israel*: by
  KJV it could stand at *Cui*); 19 *Verum* (3123); 20 *Igitur* (3128); 21 *Et Elias* (3131); 22 *Quumque* (3136); **23
  *Dentur* (3142)**: margin *23* at the end of the line above (*lucanique … H.*); placed at *Dentur*, line start; 24 *Tum
  vos* (3147, after *supponam.*); 25 *Et Elias* (3153); 26 *Tum illi* (3158); 27 *Sub meridiem* (3165); 28 *At illi*
  (3170, margin at *pergefaciendus.*); 29 *Deinde* (3174); 30 *ius-|sit* (3178, after *attenderet:*); 31 *et saxa* (3182);
  32 *Ex his* (3186); 33 *compositaque* (3189); **34 *Deinde iubet* (3191)** (= KJV 33b *Fill four jars*: Castellio's 33
  is KJV 33a, his 34 KJV 33b–34); 35 *ita vt* (3194); 36 *Post-|ea* (3196); 37 *Exaudi* (3203); 38 *Tum dela-|psus*
  (3206); 39 *Quo vi-|so* (3209); 40 *Tum Elias* (3212); 41 *De-|inde* (3215); 42 *Achabo* (3219); 43 *famulum* (3222);
  44 *Septimo* (3226); 45 *deinde* (3231); 46 *Achabus* (3234).
- **ch. 19**: 1 *POstquam* (3240, drop capital, margin *1*); 2 *Iezabel* (3243, margin *2* at the line end; after
  *cidasset:* and a wide space).

### Letters lost in the gutter
- Leaf 419 col. 0: the first digit of *10*, *11*, *12* (3089, 3095, 3097) cut by the gutter (*o*, *1*, *2* visible);
  placed by sequence and sense. No text letters lost.

### Misprints and odd forms, kept as printed
- **2976 *adparco*** (17:1; zoomed 4×: a clear *c* for *e*; 1750 *appareo*). Kept, a misprint.
- **3118 *cutus est tune is es*** (18:17): no stop after *est*, only a wide space (zoomed 4×; 1750 *est:*). Kept. The
  *is* is printed heavier (looks like a broken capital); read *is*.
- **3061 *Ioua*** (18:1): the first letter rises like an *l* (vote `ioua`); read as the capital *I*, but see the checks.
- No space after the comma: 2954 *venit,vt*; 2997 *esse,vt*; 3035 *stud,diuine?* (zoomed 3×); 3037 *iussit,sibi*; 3094
  *obtestabatur,quod*; 3096 *bes,vt*; 3099 *spiritus,nescio*; 3111 *eam,quo*; 3117 *vidit,sic*; 3126
  *quinquaginta,et*; 3152 *respondit,conditionem*; 3215 *ducit,ibique*; 3240 *Iezabeli,quæ*.
- Set tight, written with the spaces: 2972 *ex inco-*; 2997 *daturum esse*; 3007 *tuum testor*; 3041 *inde eo*; 3048
  *anima in*; 3052 *domum ex cubiculo*; 3101 *ab eo*; 3117 *sic adlo-*; 3187 *et circum*; 3189 *nis caperet*; 3205 *qui
  eorum ani-*; 3219 *epulatum profecto*.
- *tauerat )* (3074) with a space before the parenthesis: written without it, as readers 09–11.
- **Hyphens printed faint or apart**: 3128 *arces-* (a faint short dash set well clear of the word, zoomed 3×); 3184
  *Io-* (only a faint raised dot after *Io*, zoomed 2×); both written as hyphens.
- Forms: *Sarephtham* (2994) beside *Sarephtam* (2998); *Carithum* (2981, 2986); *depsititium* (3016); *consumtum*
  (3021), *absumsit* (3208); *seriæ*, *seria* (3021, 3028; long s, the jar); *sit* (3169, long s without the bar,
  zoomed 4×); *fer-|tum* (3175, f with the bar, zoomed 4×); *sata* (3188); *adpellate*, *adpellabo*, *adnuerit*;
  *Iezabele* (3105); *baalensi* (2955), *baalenses* (3139, 3212) lower case; *quatuor* (3191); *cælo* (3232);
  *dela-|psus* (3206); *Iezrael* (3235), *Ie-|zrael* (3237).
- *factum*, *cocti*, *collecto*, *constructo*, *pectus*, *profectus*, *conuictores*, *dissectum*, *subiecto*,
  *instinctus*, *succinctis*, *iunctis*, *spectatum* printed with the *ct* ligature.
- Drop capitals: **2972 ELias** (E three lines deep, 2972–2974 set in); **3060 LOngo** (L three lines, 3060–3062); **3240
  POstquam** (P three lines, 3240–3242).
- 3014: a small mark (a smudge or pointing sign) in the right margin beside *i factum,*: not a numeral or text; ignored.

### Paragraph indents and drop capitals
- Indented: **3031** (17:17 *Post eas res*), **3079** (18:6 *Quumque sibi obeundam*).
- Drop capitals: **2972** (17:1), **3060** (18:1), **3240** (19:1).
- Every other line starts flush (2954, 2955, 2961, 3019, 3045, 3064, 3109, 3142, 3147, 3158, 3174, 3186, 3191, 3212
  are flush).

### Footnotes, marks, asterisks
- Footnotes (p. 349; one line across both columns at the foot, *k* running onto a second line under col. 0). Each row
  is put after the last text row of the column whose word it hangs on (as reader 11):
  - **h) scilicet per Deum, vt dicerent, an tu illic esses,** (leaf 419 col. 0, line 900, after 3097): hangs on
    *obtestabatur*, 3094 *et gentes h obtestabatur,quod* (18:10); the italic *h* removed. The note ends with a comma
    (zoomed 6×), as printed.
  - **i) lucorum.** (col. 1, line 901, after 3146): hangs on *lucanos*, 3126 *quinquaginta,et i lu-|canos* (18:19);
    letter removed (the vote's `»`).
  - **k) ambigua sententia nutatis?** (col. 1, line 902): hangs on *quousque*, 3133 *quousque k in vtrumque* (18:21);
    letter removed (the vote's asterisk: it is the footnote letter, not an asterisk).
- *G.*/*L.*/*H.* marks: **3140–3141 *quinquaginta, G. L. | lucanique vates quadringenti. H.*** (18:22; italic, kept;
  1750 the same).
- Asterisks: none.

### Lost / added / removed
- Added (3): the footnote rows *h*, *i*, *k* on leaf 419 (lines 900–902).
- Removed (2): 2971, 3059 (chapter summaries).
- No text line lost: line numbers run on (418 col. 0 4–52 with the summary lines 20–22, col. 1 53–103; 419 col. 0 5–52,
  col. 1 55–103; 420 col. 0 4–54, col. 1 55–103 with the summary 96–100). Catchwords *tatum,*, *ne-*, *um* not in the
  vote, not added.

### Wording doubts (1738 against 1750; the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops and the numbers), among
  them: 2958–2959 *uam … suis factis | offendit* (*uani … fuisfaclis | ostendit*); 2964 *primogenitum* (*priraogenitum*);
  2966 *natu* (*nam*); 2972–2974 (the drop capital, *inco-|lis … sic*); 2975 *cui* (*cur*); 2981/2986 *Carithum*
  (*Canthum*); 2997 *daturum esse,vt eum* (*ic daturumesfe,vteum*); 3003/3023 *illa* (*ili*); 3005 *illa ita* (*ilia
  it*); 3009–3010 *se-|ria* (*se|ne*); 3012 *sum* (*Anu*); 3013 *Elias:* (colon lost); 3014 *factum,* (comma lost); 3022
  *defecturum*; 3027 *exhaurire-*; 3034–3035 *Elia sic agere … i-|stud,diuine? … mea* (*Eliaficagere … i-|ftudjdiuine …
  raca*); 3041 *collocato, sic* (*collocate , sie*); 3042 *viduæ* (*vidua»*); 3054 *uum* (*1111m*); 3061–3062 *Ioua …
  ostensum eat: sese* ; 3092 *Quum-* (*Qiium-*); 3094 (footnote *h*); 3105 *Iezabele* (*Iezabcle*); 3112 *sic … Ioua*
  (*He … ioua*); 3119 *Israelitas?* (*Israeli res?*); 3127–3129 *Ieza-|belis conuictores. Igitur arces-|siuit*; 3133
  (footnote *k*); 3141 *lucanique* (*lucemque*); 3142 *Dentur* (*Dentur-*); 3152 *do respondit,conditionem* (*de …
  condiuonem*); 3153 *Baalis vatibus* (*Baaiisvatibus*); 3155 *et priores* (*etpiiores*); 3165 *sic* (*ile*); 3170
  *pergefaciendus* (*pei -gefaciendus*); 3174 *meridie* (*meririie*); 3178/3180/3183 hyphens (*ius.*, *accesse.*, *la.*);
  3185 *ua, … nominari* (*ne, … nonjinari*); 3188–3189 *ducit, … sata semi-|nis* (*ducic … fata femi-|n is*); 3200
  *effice* (*eflke*); 3206 *dela-* (*dele*); 3209 *Quo vi-* (*Qyovi*); 3215 *fluuium* (*Amman*); 3217 *dat* (*det*); 3228
  *mæ* (*mx*); 3230 *ctis … ne a plu-* (*clis … neaplu-*); 3234–3237 *conscen-|so … Iezrael … succin-|ctis … præcurrit …
  Ie-|zrael*; 3240 *quæ* (*qua*); 3241 *narrauit,* (*narraui*); 3243 *nunti-* (*nunt-*).
- 1738 against 1750 in more than spelling: **2976 *adparco*** (1750 *appareo*: 1738's misprint); **3118 *est tune*** (1750
  *est: tune*, a stop only). Otherwise stops only: 1750 *ad Carithum fluuium e regione* (1738
  *fluuium, e regione*); 1750 *quod collecto* (1738 *quod, collecto*); 1750 *negarent te adesse* (1738 *negarent, te
  adesse,*); 1750 *nescio quo* (1738
  *spiritus,nescio quo*); 1750 *centum videlicet* (1738 *centum, videli-|cet*); 1750 *domine relatum* (1738 *domine,*);
  1750 *hic populus te* (1738 *populus, te*); 1750 *Achabus autem conscenso* (1738 *autem, conscen-|so*).

### Omission check (1 Kgs 16:31b–19:2a against the BSB)
Every verse read against the BSB; every printed line of the three leaves has its row. None lost by the reading:
- 16:31b–34: Baal worship, the altar in the temple of Baal in Samaria, the Asherah (*lucum*), Hiel of Bethel, Abiram the
  firstborn, Segub the youngest, *the word of the LORD spoken through Joshua son of Nun*: all present.
- 17:1–24: all present (the brook Cherith *east of the Jordan*; ravens morning and evening; the widow of Zarephath; *a
  handful of flour … a little oil … two sticks*; *make me a small cake first*; the jar and jug until rain; the son's
  illness; *stretched himself out over the boy three times*; *the word of the LORD in your mouth is truth* rendered *vere
  Iouæ internuntium*).
- 18:1–46: all present (the third year; Obadiah over the household, the hundred prophets in two caves of fifty; horses
  and mules; *swore an oath* = *regna et gentes obtestabatur*; the 450 prophets of Baal and 400 of Asherah *who eat at
  Jezebel's table* = *lucanos … Iezabelis conuictores*; *waver between two opinions* = *in vtrumque crus claudicatis*;
  the two bulls; *limped around the altar* = *altare factum prætergrediebantur*; the taunt; cutting themselves; the
  evening offering; the twelve stones, *Israel shall be your name*; the trench of two seahs; four jars three times;
  the fire; the Kishon; the cloud like a man's hand; Elijah running before Ahab to Jezreel).
- 19:1–2a: present to *per nunti-* (the rest of 19:2 is on leaf 421).

### Uncertain readings to check on the page
- **3061 *Ioua*** (`1738-page-0419.jpg`, col. 0, about y 730, x 300): the first letter looks like a lower-case *l*;
  written *Ioua*.
- **18:2's number** (row 3064): margin *2* stands at 3062 beside the drop capital; placed at *Igitur*.
- **18:18's number** (row 3119): placed at *non e-|go* by the margin; KJV would start at *Cui ille*.
- **3118** *cutus est tune*: no stop (col. 1, about y 1090).
- **3184 *Io-*** and **3128 *arces-***: faint hyphens (`1738-page-0420.jpg` col. 0 about y 1960; `-0419` col. 1 about y
  1610).
- **Footnote *h*'s closing comma** (*esses,*; `1738-page-0419.jpg` about y 2590, x 800–1000).

### Counts
- Rows written: **291** (leaf 418: 98, incl. `\c 17`; leaf 419: 96, incl. `\c 18` and the 3 footnotes; leaf 420: 97,
  incl. `\c 19`), from the range's 290 rows.
- Removed: **2** (2971, 3059). Added: **3** (footnotes *h*, *i*, *k*).
- Changed from the vote: **221** (77 on leaf 418, 73 on leaf 419, 71 on leaf 420).

---

## reader-13 (`reader-13.md`)

## Reader 13: rows 3244–3538 (1 Kgs 19:2 *-um significat* – 21:2 *sese ei*)

Read in one sitting after the pause (`reader-13.partial.*` kept as they are; they read no row). Every line read on the
reading sheets `sources/archive/crops/sheets/lines/1Kgs1-22.voted-231.jpg` … `-251.jpg` (labels 3243–3538), with the
whole pages for margins, indents, chapter openings and the feet, and 2–5× zooms on doubtful letters, stops and the
footnote (scratch `scratchpad\r13\`). Pages, named by the voted leaf (the fixed names): leaf 421 =
`sources/archive/crops/1738-page-0421.jpg` (head *Cap. 19. 20. | REGVM LIBER III. | 351*), leaf 422 = `1738-page-0422.jpg`
(*352 | REGVM LIBER III. | Cap. 20.*), leaf 423 = `1738-page-0423.jpg` (*Cap. 20. 21. | REGVM LIBER III. | 353*). 1750
(`sources/archive/1750/text.txt`, lines ~50090–50530) read alongside for numbers and wording. The doubts file has no rows
here.

### Leaves
- **Leaf 421** (p. 351): col. 0 (lines 4–54) = 19:2 *um significat* – 19:13 *Elias: læna* (3244–3294); col. 1 (lines
  55–104) = 19:13 *sua faciem* – 19:21 *eique administrat.* (3295–3334), rule, *CAPVT XX.*, four-line italic summary (not
  in the vote: nothing to remove), `\c 20` (3335), 20:1 *BEnadadus* – *obsedit atque* (3336–3340). Catchword **oppu-**
  under col. 1 (not in the vote, not added). No footnotes, no signature.
- **Leaf 422** (p. 352): col. 0 (lines 4–54) = 20:2 *oppugnauit.* – 20:13 *videsne tantam istam,* (3341–3391); col. 1
  (lines 55–105) = 20:13 *tam ingentem* – 20:26 *ad Aphec profi-* (3392–3442). Catchword **ciscitur,** under col. 1 (not
  in the vote). No footnotes, no signature.
- **Leaf 423** (p. 353): col. 0 (lines 4–53) = 20:26 *ciscitur* – 20:34 *facto fœde-* (3443–3492), then footnote *a)*
  (3493, made line 900); col. 1 (lines 54–101) = 20:34 *re te dimittam* – 20:43 *peruenit.* (3494–3529), rule, *CAPVT
  XXI.*, three-line italic summary (not in the vote), `\c 21` (3530), 21:1 *HIs* – 21:2 *sese ei* (3531–3538). Signature
  **Z** and catchword **aliam** under col. 1 (not in the vote, not added).

### Chapters
- `\c 20` (3335), `\c 21` (3530) copied unchanged. No row removed.

### Verse numbers (1738's margins; col. 0 numbers left, col. 1 right)
The vote's numbers were a running count and wrong throughout; every one placed again. 1750's margin numbers agree with
every placing below except where noted.
- **ch. 19** (from 3): 3 *Quibus* (3248, line start); 4 *ibique* (3251); 5 *Deinde* (3257, after *maiores.* and a wide
  space); 6 *Quumque* (3261); 7 *Iterumque* (3265); 8 *Tum ille* (3268); **9 *vbi* (3272)**: margin at the line start
  *diuinum montem Horebum:*; placed at *vbi* after a wide space (KJV 9 *And he came thither unto a cave*); **10 *Cui*
  (3275)**: margin at *tus est:*; placed at *Cui* after *Elia?* and a wide space (KJV 10 *And he said, I have been very
  jealous*); 11 *Tum ille ei iubet* (3282, line start; only *1* visible, the gutter cut the first digit); **12 *Ven-|tum*
  (3288)**: margin *2* (first digit cut) at the line start *vento Ioua non erat.*; placed at *Ventum* after a wide space
  (Castellio's 12 begins with the earthquake; KJV 11 runs to the earthquake); 13 *Hanc simulac* (3294); **14 *Cui ille*
  (3298)**: margin at the line end beside *ego me*; placed at *Cui* as in 10; 15 *Tum Ioua* (3304); 16 *Iehum* (3308);
  17 *vt qui* (3312); 18 *Ego* (3315); 19 *Igitur* (3319, indented); 20 *Tum ille, reli-* (3324); 21 *Ita reuersus*
  (3329).
- **ch. 20** (43 verses, = KJV in count; some divisions differ): 1 *BEnadadus* (3336, drop capital); 2 *Missisque*
  (3341); 3 *sic dicit* (3343); **4 *Ad hæc* (3346)**: margin at the line start *mosique*; placed at *Ad* after a wide
  space; **5 *Hæc est* (3351)**: margin at the line start *cum huiusmodi mandatis.*; placed at *Hæc* after a wide space
  (*redierunt legati*, KJV 5a, stays in Castellio's 4); 6 *me crastino* (3355); 7 *Tum rex* (3359); 8 *Cui omnes*
  (3367); 9 *Itaque* (3369); 10 *Hanc rem* (3374); 11 *Cui rex* (3381); 12 *Hac audita* (3384); 13 *Tum accedit*
  (3388); 14 *Per quos?* (3395); 15 *Tum ille* (3398); 16 *Hi sub* (3402); 17 *Qui, egressis* (3406, line start, margin
  at the line end); **18 *At illi* (3411)**: Castellio's 17 covers KJV 17–18, his 18 = KJV 19; **19 *quos deinde*
  (3415)**: margin at the line end beside *quos*; **20 *Benadadus* (3417)**: margin at the end of the line that begins
  with *Benadadus*; placed at the line start (KJV 20b); 21 *Israelitarum rex* (3418); 22 *Tum vates* (3421, indented);
  23 *Igi-|tur* (3426); 24 *Ita-|que* (3431); 25 *exercitumque* (3434, after a wide space); 26 *Horum* (3440, flush);
  27 *Israelitæ* (3444; *7* visible, the *2* half cut); 28 *Ac tum* (3448; *8* visible); 29 *Igitur* (3456; *9*
  visible); 30 *Reliqui* (3461; only a trace in the gutter); 31 *Tum sui* (3467; a trace); **32 *Igitur centonibus*
  (3473)**, **33 *Viuit tuus frater* (3480)**, **34 *Et Bena-|dadus* (3485)**: these three margin numbers are lost in the
  gutter (only specks at 3473, 3480 and beside 3484 *dadum arcessi*); placed by sequence and sense, as 1750 (32 at
  *Igitur centonibus*, 33 at *Viuit*, 34 at *Et Bena-*); 35 *Tum quidam* (3496, indented); 36 *Itaque* (3502); 37
  *Vates* (3504); 38 *Ab eoque* (3505); **39 *quum in acie* (3510)**: line start; *regem clamat in hunc modum:* stays in
  38; 40 *In-|terea* (3515); 41 *Tum ille,abster-* (3518); 42 *hoc tibi* (3521); 43 *Tum rex* (3526).
- **ch. 21**: 1 *HIs* (3531, drop capital, margin *1*); 2 *contendit* (3534, after *palatium:* and a wide space).

### Letters lost in the gutter
- Leaf 421 col. 0: the first digit of *11*, *12*, *13*; leaf 423 col. 0: 27–34 cut (see above). No text letters lost.

### Misprints and odd forms, kept as printed
- **3397 *promitit*** (20:14; zoomed 3×: one *t*; 1750 *promittit*). Kept, a misprint.
- **3308 *Nansis*** (19:16, Nimshi; zoomed 3×: long s with the left nub only, no bar through; 1750 OCR *Nanfis*).
- **3468 *israelitici*** lower case (20:31). Kept.
- **3312 *cedat*** (vote *cedet*); **3263 *depsititium***; *sumsit* (3270); *caussa* (3517, long s + s); *Hazae-|lis*
  (3312, a and e separate); *Saphati* (3310, 3320; the vote's *Sephati* at 3310 is wrong).
- No space after the comma: **3336 *rex,con-***; **3497 *Iouæ,vt***; **3514 *fuisset,ego*** (zoomed 3×); **3518
  *ille,abster-***.
- Set tight, written with the spaces: 3264 *vbi comedit et bi-*; 3284 *Ioua transibat … adeo in-*; 3298 *hic agis*;
  3320 *um Saphati*; 3321 *et duodecim*; 3324 *in eum coniecit*; 3336 *autem Syriæ*; 3345 *aurum meum est*; 3360
  *conuocatis omni-*; 3407 *qui rem*; 3457 *dies alteri*; 3463 *hominum vi-*; 3494 *icto cum illo*; 3502 *ab eo*; 3507
  *rex erat*.
- **3435 *pa-***: the hyphen is a short raised dot-like dash (zoomed 3×; vote *pa.*); written as a hyphen.
- Stops checked: 3328 *reuertatur;* (semicolon, zoomed 3×); 3391 *Ioua;*; 3455 *concessurum;*; 3537 *vteretur;*.
- *ct* ligatures (relicto, nocte-, ctauit, mactatque, cocta, accincto, discincto, facturum, victos, delectu, victoriam,
  micti, icto, dicto, nactus, ictus, recte, coniuncta) noted, written *ct*.
- Drop capitals: **3336 BEnadadus** (B three lines deep, 3336–3338 set in); **3531 HIs** (H three lines, 3531–3533).

### Paragraph indents and drop capitals
- Indented: **3319** (19:19 *Igitur ille inde*), **3421** (20:22 *Tum vates*), **3496** (20:35 *Tum quidam*).
- Drop capitals: **3336** (20:1), **3531** (21:1).
- Every other line flush (checked 3248, 3282, 3294, 3367, 3374, 3406, 3440, 3467, 3480 in particular).

### Footnotes, marks, asterisks
- **a) vbi publicanos colloces et vectigalia exigas,** (leaf 423 col. 0, row 3493 kept, line 104 → 900, after 3492):
  hangs on *fora*, 3489 *tibique a fora statues* (20:34); the letter (the vote's `"`) removed. 1738 restarts its letters
  on this page (*a*, after *k* on leaf 419). The type is worn: *publicanos* looks like *publieanos* (the *c* filled with
  ink, zoomed 5×); read *c*. The note ends with a comma (zoomed 5×), as printed.
- *G.*/*L.*/*H.* marks: none.
- **Asterisk**: 3248 *territus, \* vt vitæ* (19:3): no footnote on leaf 421 (foot checked, zoomed); taken out, stands
  before *vt*. 1750 has none.

### Lost / added / removed
- None added, none removed. Line numbers run on (421 col. 0 4–54, col. 1 55–104 with the chapter heading 96–99; 422 col.
  0 4–54, col. 1 55–105; 423 col. 0 4–53, col. 1 54–101 with the heading 90–93). The footnote row 3493 kept, its line made
  900. Catchwords *oppu-*, *ciscitur,*, *aliam* and signature *Z* not in the vote, not added.

### Wording doubts (1738 against 1750; the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops and the numbers), among
  them: 3244 *um* (*ium*, see reader 12: the page has *nunti-|um*); 3246 *postridie ita*; 3247 *fuisset*; 3248
  *Quibus*; 3249 *consuleret, discessit, et*; 3261–3262 *Quumque ille adspexis-|set* (*Qiiuraque ille se-|t*); 3263 *et
  aquæ*; 3274 *ctauit* (*&auit*); 3288 *erat* (*ciat*); 3292 *nec*; 3294 *læna* (*lama*); 3305 *istud iter*; 3308
  *Nansis* (*Nanfisi*); 3314 *qui Iehu ensem euaserit*; 3315 *interficiat*; 3318 *derunt, nec*; 3326 *petitque*
  (*peritque*); 3331 *mactatque*; 3336 *BEnadadus* (drop capital lost); 3337 *tractis* (*tradis*); 3343 *tarum … sic*;
  3353 *misi* (*mili*); 3359 *piant*; 3383 *cto*; 3384 *dum*; 3402 *Hi sub*; 3407 *postquam*; 3412 *eos* (*cos*); 3420
  *adficit* (*adficir*); 3422 *se* (*sc*); 3426 *facturum* (*fachirum*); 3427 *sui* (*fui*); 3433 *eorum* (*cor*); 3443
  *bellum* (*helium*); 3444 *rat. Israelitæ* (the vote's `7` is the margin); 3445 *eunt* (*emit*); 3447 *quasi*; 3448 the
  vote's `8` is the margin; 3456 *eum* (*cura*); 3458–3459 *castra … septi-|mo*; 3462 *fuga … collapso* (*ruga …
  collapib*); 3467 *sui … illi*; 3472 *vitam* (*vitatu*); 3474 *micti … restesque*; 3477 *tuus Benadadus* (*tune
  Eenadadus*); 3478 *ille*; 3479 *frater* (*fracet*); 3483 *stim*; 3484 *arcessi*; 3486 *sic*; 3487 *meus* (*incus*);
  3492 *facto fœde-*; 3493 the footnote; 3494 *re te dimittam. Ita, icto cum illo* (*rete diroittam. Ita, iclocumilb*);
  3499 *dicto*; 3500 *a se* (*ese*); 3507 *rex erat* (*rexerat*); 3515–3516 *In-|terea*; 3521–3522 *signi-|ficari*
  (*signi!|ricari*); 3528 *Samariamque*; 3531 *haberet* (*habere*); 3534 *contendit* (*contendi*).
- 1738 against 1750 in more than spelling: **3397 *promitit*** (1750 *promittit*: 1738's misprint). Otherwise 1750
  agrees in wording; stops only (1750 *hic agis Elia?*, *iubet vt se*, *vt si amissus*, *ibique ignota*).

### Omission check (1 Kgs 19:2b–21:2a against the BSB)
Every verse read against the BSB; every printed line of the three leaves has its row. None lost by the reading:
- 19:2b–21: all present (Jezebel's oath; Beersheba *which belongs to Judah*; the day's journey, the broom tree; the
  angel twice, the cake and jar of water; forty days to Horeb; the cave; the two complaints; wind, earthquake, fire,
  *a still small voice*; the mantle over the face; anoint Hazael, Jehu son of Nimshi, Elisha son of Shaphat of
  Abel-meholah; the seven thousand who have not bowed or kissed Baal; Elisha with twelve yoke of oxen, the cloak; the
  farewell, the oxen boiled with the yoke's gear).
- 20:1–43: all present (thirty-two kings, horses and chariots; the two embassies; the elders' counsel; *the dust of
  Samaria … handfuls*; *Let not him that girdeth on his harness boast*; drinking in the booths; the young men of the
  district governors, 232, and 7,000; the Syrians' *gods of the hills*; replacing the kings with governors; Aphek, the
  two little flocks of goats; 100,000 slain, the wall falling on 27,000; sackcloth and ropes; *he is my brother*; the
  cities restored and the streets (bazaars) in Damascus, with footnote *a*; the covenant; the prophet struck, the lion,
  the second man; the disguise, the talent of silver; *your life for his life, your people for his people*; *sullen
  and displeased*).
- 21:1–2a: present to *sese ei* (the rest of 21:2 on leaf 426).

### Uncertain readings to check on the page
- **20:32–34 numbers** (rows 3473, 3480, 3485; `1738-page-0423.jpg` col. 0 left margin, about y 1950–2230): lost in the
  gutter; placed as 1750.
- **19:10 and 19:14 at *Cui*** (3275, 3298): margins beside the lines; KJV 10/14 *And he said* agrees.
- **3308 *Nansis*** (long s or f; `-0421` col. 1 about y 775).
- **Footnote *a***: *publicanos* (worn *c*) and its closing comma (`-0423` about y 2650).

### Counts
- Rows written: **295** (leaf 421: 97 incl. `\c 20`; leaf 422: 102; leaf 423: 96 incl. `\c 21` and the footnote), from
  the range's 295 rows.
- Removed: **0**. Added: **0** (the footnote is the vote's row 3493, its line made 900).
- Changed from the vote: **212**.

---

## reader-14 (`reader-14.md`)

## Reader 14: rows 3539–3842 (1 Kgs 21:2 *aliam vineam* – 21:25 *erat æque Iouæ lædendo deditus,*)

Read in one sitting after the pause (`reader-14.partial.*` kept as they are; they read no row). `reader-14.tsv` =
leaf 426's rows (3745–3842) plus one footnote row. Rows 3539–3744 (the vote's leaves 424–425) are archive.org's second
shots of pp. 354–355, printed on leaves 426 and 427: removed, block by block below. Leaf 423 (p. 353) ends 21:2 *sese
ei* with the catchword *aliam* (reader 13); leaf 426 (p. 354) begins *aliam vineam*: nothing printed falls between.

**Images.** Named by leaf (the fixed names): leaf 426 = `sources/archive/crops/1738-page-0426.jpg` (head *354 | REGVM
LIBER III. | Cap. 21.*); leaf 427 = `1738-page-0427.jpg` (*Cap. 22. | REGVM LIBER III. | 355*), looked at for the
duplicate check and its foot. Read from column bands at 1× with 2–8× zooms on doubtful letters, stops, the right
margin of col. 1 and the footnote (scratch `scratchpad\r14\`); the sheets were not needed. 1750
(`sources/archive/1750/text.txt`, lines 50503–50620) read alongside for the numbers and the wording. hOCR word boxes
of leaves 424–425 (`archive.pages('1738')`) used to place the noise rows. The doubts file has no rows on these leaves.

### Leaves
- **Leaves 424–425**: no image (`archive.skipped_leaves`); their rows are duplicate shots, all removed (below).
- **Leaf 426** (p. 354): col. 0 (lines 4–52) = 21:2 *aliam vineam* – 21:13 *Nabothum Deo regique* (3745–3793), then
  footnote *b)* (added, line 900); col. 1 (lines 55–103) = 21:13 *maledixisse.* – 21:25 *erat æque Iouæ lædendo
  deditus,* (3794–3842). Catchword **vt** under col. 1 (p. 355 begins *vt Achabus*): not in the vote, not added. No
  signature. Running head not in the vote.

### Chapters
- No chapter starts on leaf 426. The vote's `\c 22` at **row 3677** lies in a duplicate block (leaf 425 = a shot of p.
  355) and is **removed** with it. Chapter 22 really begins on **leaf 427 col. 0**: *CAPVT XXII.* below the rule after
  21:29 *psius temporibus, sed eius filii.*, its four-line italic summary (*Iosaphatus rex ad Israelitas. Pseudouates
  Sedeciæ. Achabi mors. Ochozias heres. Iosaphatus Iudææ rex. Ochoziæ prauitas. Baalicolæ.*), then 22:1 *TRiennio
  peracto* (drop capital). The vote already has that `\c 22` at **row 3860** (leaf 427, line 19), with *TRiennio* at
  3861: reader 15's range, nothing to add.

### Verse numbers (1738's margins; col. 0 left, col. 1 right)
The vote's numbers were a running count (#7–#16) and wrong throughout; every one placed again. Col. 0's numbers all
legible; col. 1's right margin is half in the gutter (first digits or fragments visible: *1* at 14–18, a speck at 19,
*2* at 20–25), placed by the line, the sequence and the wider space. 21:1–2 begin on leaf 423 (reader 13).
- **col. 0**: 3 *Sed Nabothus* (3748, after *rum.* and a wide space); 4 *Acha-|bus* (3750); 5 *Venientique* (3756);
  **6 *narrat* (3759)**: margin beside *bum non capiat, narrat, se cum*; a wide space stands before *narrat* (zoomed
  2×), not before *se cum* where the vote and 1750's line put it; by sense KJV 6 *And he said unto her* = *narrat*;
  7 *At Iezabel* (3765, line start, flush); 8 *Hæc locuta* (3771, indented); **9 *indi-|cite* (3776)**, after
  *sententiam:* and a wide space; **10 *qui pro testimo-|nio* (3780)**: margin beside *ditos statuite, qui pro
  testimo-*, a wide space after *statuite,* (1750's OCR has a dash there); so Castellio's 9 holds *et contra eum duos
  homines perditos statuite* (KJV 10a) and his 10 begins at *qui*; 11 *Ad harum* (3783); **12 *in-|dictoque* (3787)**,
  after *faciunt,* and a wide space; 13 *Deinde* (3790, line start, flush).
- **col. 1**: 14 *Ita educitur* (3794); 15 *Iezabel audita* (3799, line start, flush); 16 *Achabus* (3805); 17 *Tum
  Elias* (3809); **18 *cum eo ex Iouæ man-|dato* (3814)**, after *caperet)* and a wide space (Castellio's 17 carries
  KJV 17–18 as narrative, his 18 = KJV 19a); **19 *At hoc* (3816)**, margin fragment beside *possideas? At hoc sic a
  Ioua ha-*; after *possideas?* and a wide space (= KJV 19b, the second *Thus says the LORD*); 20 *Hic Achabus*
  (3820); **21 *et quia tu* (3822)**: margin *2* beside *ctus sum, inquit ille: et quia tu*, a wide space after
  *ille:*; Castellio's 21 thus begins with KJV 20b *because you have sold yourself* (1750's line also begins *ctus
  sum*, its *21* standing at the line start); 22 *tuamque do-|mum* (3830, after *parietis,* and a wide space); 23 *De
  Ieza-|bele* (3835); 24 *Ac qui* (3838); 25 *Hic quamquam* (3841).

### Letters lost in the gutter
- Col. 1's right-margin numbers, half cut (above). No text letters lost; every line end of both columns whole.

### Misprints and odd forms, kept as printed
- **3756 *abstinuit***: the *st* is a ligature whose *ſ*-top hooks over a short *t* (8×; the vote and leaf 424's shot
  read *absfinuit*); the same glyph is in *esto* (3768, vote *beto*): read *abstinuit*, no misprint.
- 3757 *quanam*: a speck above the first *n* (2×), not a letter; 3824 *mala*: a speck above the last *a*, not an
  accent. Both written plain.
- 3766 *israeliticum* lower case (as printed; the vote's *israéliticum* has no accent on the page); 3837
  *iezraelensi* lower case (as printed; 3760, 3769, 3802 *Iezraelensi(s)* capital).
- *Nabathi* (3832, Nebat), *Baasæ Achiæ* (3833), *Thesbita* (3809), *commincto-|rem* (3829–3830, *ct* ligature),
  *degressus* (3813), *aereæ* (3840), *comesum* (3838), *lincturos* (3820).
- Parentheses with thin spaces inside (*( si illi ita videretur )*, *( si ita placeret )*, *( qui tum*): written
  without them, *(si illi ita videretur)* etc., as reader 09–10.
- Set tight, written with the spaces: 3749 *Ioua volente*; 3754 *lecto suo*; 3759 *se cum*; 3760 *vt sibi*; 3762 *ita
  placeret*; 3765 *o te hominem*; 3781 *regique ma-*; 3790 *Deinde duo superueniunt*; 3796 *Deinde ad Iezabelem*; 3799
  *Nabothi lapidatione*; 3810 *a Ioua*; 3815 *locutus est … occideris et*; 3816 *hoc sic a Ioua*; 3818 *re canes
  Nabothi cruorem*; 3822 *ctus sum … quia tu*; 3823 *totus addictus*; 3828 *stirpitus ex-*; 3833 *filii domum*; 3834
  *quia tu et Iouam … et Israeli-*; 3841 *quamquam nemo*. No comma without its space on this page.
- *ct* ligatures (lecto, eductum, dictoque, interfectumque, intellecta, lincturos, nactus/ctus, addictus, comminctorem)
  written *ct*.
- Line-end hyphens set as a raised dot in places (3776 *indi-*, 3803 *renuis-*, 3829 *commin-*, 3830 *do-*): written
  as hyphens.

### Paragraph indents and drop capitals
- Indented: **3771** (21:8 *Hæc locuta*, after the short line *tradam.*).
- Every other line starts flush (3765 *At Iezabel*, 3790 *Deinde*, 3799 *Iezabel* are flush). No drop capitals.

### Footnotes, marks, asterisks
- **b) qui vnius vineæ comparandæ rationem non inuenias, quo pacto regnum, si esset opus, tibi parares?** (leaf 426,
  col. 0, line 900, after 3793): set full width across both columns' foot in two lines (*… si es-|set opus, tibi
  parares?*), joined in one row with *esset*. Hangs on *o te hominem idoneum*, 3765 *At Iezabel: b o te hominem
  idone-* (21:7); the italic *b* removed (the vote's `^`). Letter as printed (the note on leaf 423 was *a*).
- **Asterisk**: 3838 *comesum iri.* Ac qui* (21:24): no footnote for it on the page; taken out.
- No *G.*, *L.*, *H.* marks.

### Removed duplicate blocks (rows 3539–3744, 206 rows) and what each repeats
Checked word by word against the voted rows of leaves 426 and 427, and placed with the hOCR boxes. Every row is a piece
of a line printed on p. 354 (leaf 426) or p. 355 (leaf 427), or noise outside the text block. Nothing on leaf 428 is
repeated.
- **Leaf 424 (rows 3539–3643, 105 rows) = a shot of p. 354 (leaf 426)**, the two columns interleaved line by line
  (hOCR lines 10–58 = col. 0, 59–121 = col. 1, the col.-1 lines cut at the right).
  - 3539 (*.«-■•…*), 3540 (*X teji c>*), 3541 (*st r r,*), 3542 (*rjor c*): noise at the image's top left (hOCR boxes x
    38–954, y 0–404, above the running head at y 852 and left of the text at x 1224): no printed line.
  - 3543 *tradam.* = 3770; 3544 *REGVM LIBER HI.* and 3545 *Cap. it* = p. 354's running head (*REGVM LIBER III.*,
    *Cap. 21.*).
  - col. 0 lines: 3546 = 3745; 3549–3550 = 3746–3747; 3552 = 3748; 3554 = 3749; 3556 = 3750; 3558 = 3751; 3560 = 3752;
    3562 = 3753; 3564 = 3754; 3566 = 3755; 3568 = 3756; 3571–3572 = 3757–3758; 3574 = 3759; 3576 = 3760; 3578 = 3761;
    3580 = 3762; 3582 = 3763; 3584 = 3764; 3586 = 3765; 3588 = 3766; 3591 = 3767; 3593–3594 = 3768–3769; 3599–3600 =
    3771–3772; 3603 = 3773; 3605–3606 = 3774–3775; 3608 = 3776; 3610 = 3777; 3612 = 3778; 3615 = 3779; 3617 = 3780;
    3619–3620 = 3781–3782; 3623 = 3783; 3625 = 3784; 3627 = 3785; 3629–3630 = 3786–3787; 3633 = 3788; 3635–3636 =
    3789–3790; 3638 = 3791; 3640 = 3792; 3643 = 3793.
  - col. 1 lines: 3547–3548 = 3794–3795; 3551 = 3796; 3553 = 3797; 3555 = 3798; 3557 = 3799; 3559 = 3800; 3561 = 3801;
    3563 = 3802; 3565 = 3803; 3567 = 3804; 3569–3570 = 3805–3806; 3573 = 3807; 3575 = 3808; 3577 = 3809; 3579 = 3810;
    3581 = 3811; 3583 = 3812; 3585 = 3813; 3587 = 3814; 3589–3590 = 3815–3816; 3592 = 3817; 3595 = 3818; 3596–3597 =
    3819 (split: *tuum quoque cruorem es* and *canes*); 3598 = 3820; 3601–3602 = 3821–3822; 3604 = 3823; 3607 = 3824;
    3609 = 3825; 3611 = 3826; 3613–3614 = 3827–3828; 3616 = 3829; 3618 = 3830; 3621–3622 = 3831–3832; 3624 = 3833;
    3626 = 3834; 3628 = 3835; 3631–3632 = 3836–3837; 3634 = 3838; 3637 = 3839; 3639 = 3840; 3641–3642 = 3841–3842.
  - So all 98 lines of p. 354 are there once each, and nothing else.
- **Leaf 425 (rows 3644–3744, 101 rows) = a shot of p. 355 (leaf 427)**, the columns interleaved (hOCR lines 15–64 =
  col. 0, left letters cut from line 16 on; 66–117 = col. 1).
  - 3644 *REGVM LIBER III.* = p. 355's running head.
  - col. 0, 21:25–29: 3646 = 3845 (*[vt Ac]habus, qui, instigante Ieza-*); 3648 = 3846; 3650 = 3847; 3652 = 3848; 3654
    = 3849; 3656 = 3850; 3658 = 3851; 3660 = 3852; 3662 = 3853; 3664 = 3854; 3666 = 3855; 3668 = 3856; 3670 = 3857;
    3672 = 3858; 3674 = 3859.
  - **3677 `\c 22`** = the heading *CAPVT XXII.* (hOCR line 30, y 1843) = 3860, the vote's `\c 22` on leaf 427.
  - 3679 (*[Sed]eciiu. Acbabi mors. Ocboziat betes.*), 3681 (*[Ios]apbatKA lud\*\* rex. Ochozig praui-*), 3682
    (*[tus.] Baaiicolt.*) = lines 2–4 of the ch. 22 italic summary (not text; the vote's leaf 427 has no rows for it).
  - col. 0, 22:1–6: 3684 = 3861 (*[TRi]ennio peracto*); 3686 = 3862; 3688 = 3863; 3690 = 3864; 3692 = 3865; 3694 =
    3866; 3696 = 3867; 3698 = 3868; 3700 = 3869; 3702 = 3870; 3704 = 3871; 3706 = 3872; 3708 = 3873; 3710 = 3874; 3712
    = 3875; 3714 = 3876; 3716 = 3877; 3718 = 3878; 3720 = 3879; 3722 = 3880; 3724 = 3881; 3726 = 3882; 3728 = 3883;
    3730 = 3884; 3732 = 3885; 3734 = 3886; 3736 = 3887; 3738 = 3888; 3740 = 3889; 3742 = 3890.
  - col. 1, 22:7–20 (with p. 355's margin numbers 9–20 at the line ends): 3645 = 3891; 3647 = 3892; 3649 = 3893; 3651
    = 3894; 3653 = 3895; 3655 = 3896; 3657 = 3897; 3659 = 3898; 3661 = 3899; 3663 = 3900; 3665 = 3901; 3667 = 3902;
    3669 = 3903; 3671 = 3904; 3673 = 3905; 3675 = 3906; 3676 = 3907; 3678 = 3909 (the shot lacks 3908's line, *tes:
    adgrederetur rex feliciter Ra-*, which leaf 427's vote has); 3680 = 3910; 3683 = 3911; 3685 = 3912; 3687 = 3913;
    3689 = 3914; 3691 = 3915; 3693 = 3916; 3695 = 3917; 3697 = 3918; 3699 = 3919; 3701 = 3920; 3703 = 3921; 3705 =
    3922; 3707 = 3923; 3709 = 3924; 3711 = 3925; 3713 = 3926; 3715 = 3927; 3717 = 3928; 3719 = 3929; 3721 = 3930; 3723
    = 3931; 3725 = 3932; 3727 = 3933; 3729 = 3934; 3731 = 3935; 3733 = 3936; 3735 = 3937; 3737 = 3938; 3739 = 3939;
    3741 = 3940; 3743 = 3941.
  - **3744 (*Z % Ua-*)** = p. 355's foot: signature **Z 2** and catchword **laa-** (seen on `1738-page-0427.jpg`; p. 356
    begins *laaditarum*). The vote's leaf 427 has **no row** for it; for reader 15 to decide (the brief adds a
    catchword row only where the vote has one; readers 09–13 added none).
- So **every** row 3539–3744 repeats text printed on leaf 426 or 427, or is noise or heading/summary; none carries a
  line missing from leaves 426–427.

### Lost / added / removed
- Removed: **206** rows (3539–3744, the duplicate shots, including `\c 22` at 3677).
- Added: **1** (the footnote *b)*, leaf 426 col. 0 line 900).
- No text line lost on leaf 426 (line numbers run on: col. 0 4–52, col. 1 55–103).

### Wording doubts (1738 against 1750; the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces before stops and the numbers): 3746
  *si illi ita* (*fiilliita*); 3749 *Ioua volente, commissurum* (*commisfunmi*); 3754 *lecto suo* (*leftofuo*); 3755
  *auerso* (*auerib*); 3756 *abstinuit* (*absfinuit*); 3765 *o te* (*^ote*); 3766 *israeliticum* (*israéliticum*); 3768
  *esto læto* (*beto*); 3787 *eo* (*,eo*); 3788 *dictoque* (*di&oque*); 3789 *constituunt* (*conftituunr*); 3798
  *interfectumque* (*interfechimque*); 3806 *intellecta* (*intellect*); 3809 *Tum Elias* (*TumEIias*); 3810 *Israelitarum*
  (*Israelitarum.*); 3815 *locutus est: et occideris et* (*locutuseft: et occiderise*); 3816 *possideas?* (*possideas \*);
  3822–3823 *ctus sum … et quia tu | Iouæ offendendo totus addictus es,* (*Ctusfum … etquiatuJ | otFendendo
  totusaddic\uses*); 3826 *abdi-* (*abdi*); 3830 *do-* (*do-3'*); 3832 *filii* (*tali*); 3833 *Baasæ* (*ftaafae*); 3834
  *Iouam … Israeli-* (*iouam … Israeli*); 3835 *tas* (*res*), *De Ieza-* (*De*); 3837 *iezraelensi* (the vote's
  lower case is right); 3838 *Achabi-*; 3840 *aereæ volucres* (*aereae volucre*); 3842 *Iouæ* (*Ioua;*).
- 1738 against 1750 in more than spelling:
  - **3746 1738 *(si illi ita videretur)***, 1750 OCR *(fi ita illi videretur)*: word order. 1738 checked on the page
    (*ſi illi ita*).
  - **3763 1738 *Illum vero***, 1750 OCR *Illam vero*: 1738 clearly *Illum* (Naboth, the subject of *negasse*); 1750's
    *Illam* may be its OCR.
  - Stops only: 1750 *Ioua volente commissurum* (1738 *volente,*); 1750 *negasse sibi* (1738 *negasse,*); 1750 *et
    auerso vultu* (1738 *et, auerso*); 1750 *Hæc locuta litteras* (1738 *locuta,*); 1750 *interfectumque esse,* (1738
    *esse.*); 1750 *degressus vt* (1738 *degressus,*); 1750 *beto;* (1738 *beto,*); 1750 *scito fore* (1738 *scito,
    fore*); 1750 *exscindat;* (1738 *exscindat,*).

### Omission check (1 Kgs 21:2–25 against the BSB)
Every verse read against the BSB; every printed line of the leaf has its row. Points of note, none an omission by the
reading:
- 21:2–6: *better vineyard … its value in silver* present; 21:4 Naboth's words reported as *hac Nabothi voce*; 21:6
  Ahab's answer in indirect speech; *I will not give you my vineyard* = *negasse, sibi daturum esse vineam*.
- 21:7: *Do you not reign over Israel?* rendered ironically, *o te hominem idoneum … qui israeliticum regnum pares?*,
  with footnote *b)* explaining it.
- 21:8–14: all present; *among the people* = *in editissimo omnium loco*; *scoundrels* = *homines perditi*; 21:13 *took
  him outside the city* = *educitur ex oppido*; 21:14 the message to Jezebel present.
- 21:15–19: present; 21:17 *the word of the LORD came to Elijah* is carried by *iussus a Ioua*; 21:18 *who is in
  Samaria* = *apud Samariam*; 21:19 *yes, yours!* has no separate word (a rendering).
- 21:20: *When Elijah arrived* is not on the page (Castellio has *Hic Achabus: ergo me nactus es*); a rendering.
- 21:21–24: present; *every male, both slave and free* = *nihil neque tam abditum neque tam obuium … vsque ad
  comminctorem parietis*; 21:23 *by the wall of Jezreel* = *in agro iezraelensi* (Castellio's field, not the wall:
  the page's reading).
- 21:25 begins *Hic quamquam nemo erat æque Iouæ lædendo deditus,* and runs on to leaf 427 (*vt Achabus …*).

### Uncertain readings to check on the page
- **21:6's number** (3759): placed at *narrat* by the wide space (`1738-page-0426.jpg`, col. 0, about y 790–820); the
  vote and 1750 have *se cum*.
- **21:10's number** (3780) at *qui pro testimonio* and **21:21's** (3822) at *et quia tu*: by the wide spaces, against
  the KJV's division.
- **3756 *abstinuit*** (*st* ligature; col. 0, about x 250–360, y 665–725).

### Counts
- Rows written: **99** in `reader-14.tsv` (98 from leaf 426, rows 3745–3842, plus 1 footnote row).
- Changed from the vote: **63**. Removed: **206** (rows 3539–3744). Added: **1**.

---

## reader-15 (`reader-15.md`)

## Reader 15: rows 3843–4063 (1 Kgs 21:25 *vt Achabus* – 22:54 end of the book)

Read in one sitting after the pause (`reader-15.partial.md` kept as it is; it read no row). `reader-15.tsv` = leaves
427–429's rows less 7 removed, plus 2 added rows (signature/catchword lines).

**Images.** Named by leaf (the fixed names): leaf 427 = `1738-page-0427.jpg` (head *Cap. 22. | REGVM LIBER III. |
355*), leaf 428 = `1738-page-0428.jpg` (*356 | REGVM LIBER III. | Cap. 22.*), leaf 429 = `1738-page-0429.jpg` (*Cap. 1.
| REGVM LIBER IIII. | 357*). Read from column strips at 1× with 2–5× zooms on doubtful letters, margins and stops
(scratch `scratchpad\r15\`); the sheets were not needed. 1750 (`sources/archive/1750/text.txt`, lines ~50620–50900)
read alongside for the numbers and the wording; its line breaks match 1738's through 22:21–54. No `doubts.tsv` rows on
these leaves.

### Leaves
- **Leaf 427** (p. 355): col. 0 (lines 4–53) = 21:25 *vt Achabus* – 21:28 *sed eius filii.* (3845–3859), rule, *CAPVT
  XXII.* and its italic summary (not in the vote), `\c 22` (3860), 22:1 *TRiennio* – 22:8 *quod mihi nihil faustum, sed*
  (3861–3890); col. 1 (lines 54–104) = 22:8 *tantum infausta* – 22:20 *vt Ramotha Ga-* (3891–3941). Foot: signature
  **Z 2** and catchword **laa-** (the vote's 3744, a duplicate shot, removed by reader 14): **added** as `% Z 2 laa-`
  (427/1/900).
- **Leaf 428** (p. 356): col. 0 (lines 4–53) = 22:20 *laaditarum* – 22:34 *inter commissuras et lori-* (3942–3991), then
  footnote *c)* (3992); col. 1 (lines 55–104) = 22:34 *cam vulnerauit* – 22:50 *suos Iosa-* (3993–4046). Catchword
  **phato,** under col. 1 (no signature): not in the vote, **added** as `% phato,` (428/1/900).
- **Leaf 429** (p. 357): col. 0 lines 1–8 = 22:50 *phato, qui cum* – 22:52 *anno decimo septimo* (4047–4054); col. 1
  lines 12–19 = 22:52 *Iosaphati Iudææ regis.* – 22:54 *patris exemplo læsit.* (4056–4063).
  **1 Kings ends here, at row 4063** (*patris exemplo læsit.*, the last line of col. 1's eight-line block). Below
  both columns: a full-width ornamental rule, then the title **REGVM LIBER IIII.**, *CAPVT I.*, its italic summary and
  2 Kgs 1:1 *MORTVO Achabo* (drop capital) to 1:15 on the rest of the page. **The vote has no 2 Kings rows** (it stops at
  4063); the only row from the 2 Kings part of the page is **4055** (col. 0 line 20, `zm:`), the OCR of the
  ornamental rule: removed. No row of the output belongs to 2 Kings.

### Chapters
- `\c 22` at **row 3860** confirmed: *CAPVT XXII.* below the rule after 21:28 *sed eius filii.* (leaf 427 col. 0),
  summary *Iosaphatus rex ad Israelitas. Pseudouates Sedecias. Achabi mors. Ochozias heres. Iosaphatus Iudææ rex.
  Ochoziæ prauitas. Baalicolæ.* (four italic lines, not text), then 22:1 *TRiennio* with a three-line drop *T*.

### Verse numbers (1738's margins: leaf 427 col. 0 left = gutter; col. 1 right; leaf 428 col. 0 left, col. 1 right =
gutter; leaf 429 col. 0 left = gutter, col. 1 right)
The vote's numbers (#17–#19, #1–#34) were a running count and wrong throughout; every one placed again.
- **Ch. 21 (end)**: 1738 has **28** verses here (its 25, *Hic quamquam*, holds KJV 25–26): **26 *tamen auditis* (3850)**,
  margin shows only the second digit *6*, the *2* lost in the gutter, after *sustulerat:* and a wide space (= KJV 27);
  **27 *Tum Ioua cum E-|lia* (3854)**, margin *7* beside *calceatus incessit. Tum Ioua*; **28 *Quoni-|am* (3856)**,
  margin *8*, after *submittat?* and a wide space.
- **Ch. 22, leaf 427 col. 0 (vv. 1–8): the margin numbers are lost** (the gutter, with the facing leaf's edge over the
  first letters of the lower lines). Placed by the wide spaces and the sequence (col. 1 resumes at 9, and 1738's
  numbers follow the Hebrew/KJV through ch. 22): 1 *TRiennio* (3861); 2 *anno tertio* (3863, after *fuit,* and a wide
  space); 3 *et rex Israelitarum* (3865, after *Israelitarum:* and a wide space); 4 *Deinde a Iosaphato* (3869); **5
  *Sed tibi censeo* (3875)**, after *vti.* and a wide space (= KJV 5); a similar wide space stands before *Cui
  Iosaphatus* (3872, KJV 4b), not numbered; 6 *Igitur* (3877, line start); 7 *Sed Iosaphatus* (3884, line start); 8
  *Cui rex Israeli-|tarum* (3886, after *interrogemus?* and a wide space).
- **col. 1 (right margin, all legible)**: 9 *Tum rex* (3894); 10 *Quumque* (3897); 11 *Se-|decias* (3902); 12 *Idemque*
  (3907, line start); 13 *Ceterum* (3910); 14 *Sed* (3915); 15 *Deinde* (3919, line start); **16 *Et rex: ego* (3924)**
  (the vote had it at *ego*; the wide space is before *Et*); **17 *Tum ille: vidi* (3927)** (vote at *vidi*); 18 *Hic
  rex* (3932); **19 *Et Michæas: ergo* (3936)** (vote at *ergo*); **20 *ecquis* (3940)**, after *dicentem:* and a wide
  space.
- **Leaf 428 col. 0 (left margin, legible)**: 21 *Atque alio* (3943, line start); **22 *Ibo* (3946)**: margin *22*
  beside *inquit Ioua. Ibo, inquit ille*, the wide space before *Ibo*; so 1738's 21 ends *Quo pacto? inquit Ioua.*
  (KJV 22 begins at *Wherewith?*; 1750 has 22 at the same line); 23 *Quamobrem* (3950); 24 *Hic Sedecias* (3953); 25
  *Tum scies* (3957); 26 *Et rex* (3959); **27 *et mandato* (3963)**, after *deducito:* and a wide space; 28 *Cui
  Michæas* (3967); 29 *Igitur* (3970); 30 *monuit* (3973); 31 *Imperauerat* (3979, line start); 32 *Ita-|que* (3983);
  33 *Sed ex-|clamante* (3986); 34 *At quidam* (3989).
- **Leaf 428 col. 1 (right margin, last digit partly in the gutter)**: 35 *Atque eo die* (3996); 36 *Sub occasum*
  (4000); 37 *Rex mortuus* (4003); 38 *Quumque* (4005, line start); 39 *De omnibus* (4009); 40 *Achabo* (4014); 41
  *Iosaphatus autem* (4016); 42 *annos tum natus* (4019, after *quarto,* and a wide space); 43 *Is omnes* (4023); **44
  *quamquam sacella* (4026)**: 1738 numbers by the Hebrew here (KJV 43b *nevertheless the high places…*), so from here
  1738 = KJV + 1: 45 *Fuit* (4029); 46 *De reliquis* (4031); 47 *Reli-|quias* (4037); 48 *In Idumæa* (4040, margin
  *4[8]*); 49 *Fecit* (4041, *4[9]*); 50 *obtulit* (4045, *5[0]*).
- **Leaf 429**: **51 *Defuncto* (4049)** and **52 *Ochozias* (4052)**: col. 0's left margin shows only *1* and *2*
  (the *5* lost in the gutter; a speck of it beside the *1*); 1750 has 51, 52 on the same lines. The vote's `1
  Defuncto)` and `* eius filius` were these digits: no asterisk on 4052. Col. 1: 53 *Regnauit* (4056), 54 *Baalem*
  (4061). The vote's #33 at *Iosaphati* (4056) was wrong: no verse begins there. **Ch. 22 has 54 verses in 1738**
  (Hebrew numbering; KJV 53).

### Letters lost in the gutter
- Leaf 427 col. 0, lines 43–53 (3880–3890): the facing leaf's edge lies over the first letter of each line, partly
  hiding *n*(e), *a*(doriatur), *d*(ent), *v*(rbe), *S*(ed), *p*(ræterea), *i*(nterrogemus), *t*(arum: the *t* hidden
  entirely; read *Israeli-|tarum*, the vote's *Isra-|ëli* was wrong), *q*(uem), *c*(ontari), *o*(di): all restored by
  the visible remainder and the word. Margin numbers of 22:1–8 lost (above).
- Col. 1 margins of leaves 427–428: first or last digits half cut, as listed. No text letters lost at line ends; leaf
  429 col. 1's line ends are **whole on the page** (the OCR's *Regnau*, *Ion mqu*, *imi*, *fu* were its cut): read
  *Regnauit*, *Iou mque* (below), *imi-*, *sui*.

### Misprints and odd forms, kept as printed
- **4057 *Iou mque***: the *a* of *Iouamque* **did not print**: a blank the width of a letter between *Iou* and
  *mque*, no trace of ink at 5× with contrast raised (`1738-page-0429.jpg`, col. 1 line 2, about x 1310–1510, y
  160–215). Written as printed, *Iou mque*; 1750 *Iouamque*. **For Claude/Nathan to decide** how a dropped sort is
  written (no precedent found in the earlier readers' notes).
- 3867 *Ramotha Galaa-|ditidis* (sic; elsewhere *Galaaditarum*); 3963 *Ioam* (Joash; the vote's *leam*); 4023 *Salis*
  (Shilhi); 4045 *Asiongaber*; 4043 *Ophire*; 3892, 3896 *Iemlæ*; 3903, 3954 *Chanaanæ*; 3921 *Ramothis*; 4059 *Nabati*.
- *Michæas/Michæam/Michææ/Michæa* with æ throughout (3892, 3896, 3911, 3916, 3920, 3936, 3954, 3958, 3961, 3967);
  *Iudææ* (3864, 3972, 4017, 4037, 4056), *Iudæorum* (3898); *prœlium* with œ (3974, 3978).
- Specks over letters, not accents: 3847 *nefandos* (spot above the *o*), 3868 *ctandum* (stroke over *u*, the
  descender of the line above), 3943 *aliud* (stroke over *u*), 3898 *Iosaphatus* (speck before *s*), 3910 *Io-|ua
  volente* (speck between). 3852 *indutus*: broken type (*ndtitus*-looking), read *indutus*.
- 3873 *licet*: covered by a brown stain (*l…et*); the *c* hidden; read *licet* by the remains and 1750.
- Comma without its space, kept: 3874 *equis,perinde*; 3918 *foret,id*; 3949 *Vade,atque*; 3969 *hoc,inquit*; 4044
  *successisset,facto*.
- 3881 *nec ne*: set with a thin space (zoomed 2×), written as two words; 3940 *ecquis* (the vote's *ecqui*).
- Parentheses with thin spaces inside (*( inquit Iosa-*, *( inquit Michæas )*): written without them.
- *ct* ligatures (peracto, cunctandum, dicturum, victoriam, flectat, adfectum, edictum, constructis, defuncto, factis,
  facto, Defuncto, auctoris) written *ct*.

### Paragraph indents and drop capitals
- Drop capital: **3861 *TRiennio*** (three lines; 3862–3863 stand beside it).
- No indented line on leaves 427–429: every other line starts flush (3877 *Igitur*, 3907 *Idemque*, 3919 *Deinde*,
  3979 *Imperauerat*, 4005 *Quumque* are flush). On leaf 427 col. 0, 3880–3890 the left edge is hidden by the
  facing leaf, but the visible letters line up with the lines above: no indent.

### Footnotes, marks, asterisks
- **c) in incertum.** (leaf 428, col. 0 foot, row 3992 kept as `% c) in incertum.`): hangs on **simpliciter** (3990,
  22:34): the small italic *c* stands at the end of 3989 *At quidam c* before *simpliciter*; removed from the text row.
- **Asterisk**: 3977 *dueret.* Ipse* (22:30): no footnote for it on the page; taken out.
- The vote's `*` on 4052 is the margin digit *2* (above), not an asterisk.
- No *G.*, *L.*, *H.* marks.

### Lost / added / removed
- Removed (7): **3843** running head *REGVM LIBER III.*; **3844** *Cap. 12.* (= the head's *Cap. 22.*); **4030, 4032,
  4034, 4036** (lines 106–109: `#30 cum`, `#31 liquis`, `'a6tis,`, `tat in`), the OCR's second reading of the line ends
  of 4029, 4031, 4033, 4035 (*cum*, *reliquis*, *factis,*, *exstat in*, with the margin 45–46): duplicates; **4055**
  `zm:` = the ornamental rule between the books (2 Kings part of the page).
- Added (2): `% Z 2 laa-` (427/1/900, p. 355's signature and catchword); `% phato,` (428/1/900, p. 356's catchword).
  Earlier readers added no catchword rows (reader 14 left *vt* out); drop these in the merge if that is the rule.
- No text line lost: leaf 427 col. 0 4–53, col. 1 54–104; leaf 428 col. 0 4–53, col. 1 55–104 (less the four
  fragments); leaf 429 col. 0 1–8, col. 1 12–19.

### Wording doubts (1738 against 1750; the page is the reading)
- The vote's misreadings put right from the page (besides ſ/f, *ae* → *æ*, spaces and numbers), among them: 3852
  *indutus* (*indutus»*), 3858 *illa* (*ilia*), 3859 *sed eius* (*fedeius*), 3867–3868 *proinde cun-|ctandum*
  (*proindecun-|6tandum*), 3869 *eriperent* (*eripeient*), 3873 *licet tibi me* (*ifcettibime*), 3875 *censeo*
  (*cenfto*), 3879 *quærit ex eis* (*quaeritexeis*), 3881 *adoriatur, nec ne* (*(idoriatur , nee ne*), 3886–3887
  *Israeli-|tarum* (*Isra-|ëli*), 3888 *quem liceat de* (*mem liceatde*), 3892, 3896 *Iemlæ* (*Iemlar*, *Iemlac*), 3898
  *Iosaphatus* (*lolaphatus*), 3910 *ua volente* (*uaVoIente*), 3922 *ferimus* (*ftrimus*), 3939 *læuaque*
  (*Ixuaque*), 3945–3946 *Quo pacto? | inquit* (*pacta» ? | 2 inquit*), 3957 *locutus sit? Tum scies* (*loeutusfit?
  Tumfcies*), 3961 *eumque* (*cumque*), 3963 *Ioam* (*leam*), 3982 *magnumue* (*niagnumue*), 3986 *verterunt*
  (*vertertint*), 3987 *non* (*nun*), 3991 *commissuras* (*coramisfuras*), 4005 *currus ad Samariæ pisci-*
  (*currusad Saroarixpifci*), 4014 *regum* (*rerum*), 4023 *Salis filiam* (*Salisriliam*), 4041 *nullus erat … Fecit*
  (*nulluserat … Fecit 4*), 4047 *seruis* (*feriiis*), 4053 *Israelitarum regnum apud Sa-* (*Israelifarum … ^-a-*),
  4056–4063 (leaf 429 col. 1, the OCR cut at the right): read in full.
- 1738 against 1750 in more than spelling: none. Stops only: 1750 *licet tibi me meisque et* (1738 *me, meisque,
  et*); 1750 *Decipies ( sub-* (1738 *Decipies, (sub-*); 1750 *Tum scies* (1738 *scies,*).

### Omission check (1 Kgs 21:25–22:53 KJV against the BSB)
Every verse read against the BSB; every printed line has its row.
- 21:25–29: present; KJV 26 (*abominably … idols … Amorites*) is in 1738's 25.
- 22:1–14: present; 22:4 *I am as you are, my people as your people, my horses as your horses* = *licet tibi me,
  meisque, et hominibus, et equis, perinde ac tuis, vti*; 22:7 *a prophet of the LORD … that we may inquire of him*
  present.
- 22:15–28: present; 22:19 *on His right and on His left* = *dextra læuaque*; 22:24 *Which way did the Spirit…*
  rendered *quando … emigrauit*; 22:28 *Mark my words, all you people!* = *Atque hoc … audite vniuersi.*
- 22:29–40: present; 22:34 *at random* = *simpliciter* with note c) *in incertum*; 22:35 *the blood … ran into the
  bottom of the chariot* = *in capsum currus*; 22:38 *and the prostitutes bathed* = *lauantibus scortis*.
- 22:41–53: present; 22:46 (Heb. 47) *male shrine prostitutes* = *Reliquias mollium*; 22:48 (Heb. 49) *ships of
  Tarshish* = *naues Cilicas*; 22:53 *provoked … as his father had done* = *sui patris exemplo læsit*. Nothing lost.

### Uncertain readings to check on the page
- **4057 *Iou mque*** (the unprinted *a*): how to write it.
- **22:1–8's numbers** (leaf 427 col. 0, margins lost): placed by the wide spaces; 5 at *Sed tibi censeo* (3875) rather
  than *Cui Iosaphatus* (3872).
- **21:26** (3850): only the *6* visible (`1738-page-0427.jpg`, col. 0, x 0–20, y 430–470).
- **22:22 at *Ibo*** (3946), against the KJV's division (1750 agrees with 1738's line).
- **3873 *licet*** under the stain (col. 0, about x 230–330, y 1900–1950).
- The two added catchword/signature rows: keep or drop by the merge's rule.

### Counts
- Rows written: **216** in `reader-15.tsv` (214 voted rows, 2 added).
- Changed from the vote: **161**. Removed: **7** (3843, 3844, 4030, 4032, 4034, 4036, 4055). Added: **2**.

