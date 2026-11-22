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
