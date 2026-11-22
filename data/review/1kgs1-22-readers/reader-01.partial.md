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
