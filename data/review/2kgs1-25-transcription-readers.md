# 2 Kings 1–25, phase 1: the readers' notes

The eleven readers' notes as written (2026-11-22), three leaves each (two for reader 11), for
`2kgs1-25-transcription.md`. Row numbers are those of `data/witnesses/read-1738/2Kgs1-25.voted.tsv` (and of the `row`
column of `2Kgs1-25.corrections.tsv`); verse numbers are 1738's. The readers' rows, the brief, `STATUS.md` and
`merge.py` are in `data/review/2kgs1-25-readers/`.

## Settled by Claude at the merge (2026-11-22)

Each looked at on the page image (the line with one either side, the column's full width with its margin numerals,
cut from `sources/archive/crops/1738-page-0LLL.jpg`).

- **Row 2292 *Ezechiani*** (leaf 452 col. 1, ch. 19): the page prints *Ezechiani* (dot on the last stroke), a misprint
  for *Ezechiam*; reader 08's *Ezechiam* corrected to the page (decision 58). The edited text will have *Ezechiam*.
- **25:29 at *muta-*** (row 3082): the margin *29* stands beside row 3083, which begins mid-word (*-tis eius carceris
  vestimentis*); as at 5:20 and 7:19, where the numeral's line opens inside a word, the verse begins on the line
  above at the sense break, *mutatis* (KJV *And changed his prison garments*). Reader 11's `#29` at *eumque* moved.
- **Row 253 *conuocàuerit*** (3:13, leaf 431 col. 1): a grave stands over the *a*, a clean stroke, as reader 01
  described; kept as printed, like 1738's other accents (the settled printed texts keep them, decision 67).
- **Readers' other asks, looked at and kept**: row 875 *indîci* (circumflex printed), 1555 *eouites* (the *q* without
  its tail), 1556 *cepi.,* (a low dot, then the comma), 1:1 *Moabi-/bitæ* (the syllable printed twice).
  The three corrections are in `merge.py` (`FIXES`), the readers' files left as they read.
- **Kept as the readers placed them** (looked at): 2:2 at *vt ibi maneret* (row 96; the margin *2* stands beside the
  *batur,* line, whose only starts are *vt* and *sese*); 2:4 at *Quibus* (row 104; the line's only start); 4:26 at
  *eamque* (row 409; the *26* heads col. 1, though col. 0's margin beside *vt aduenienti* was free: the printer's
  start, though the KJV's 26 begins at *vt aduenienti*, for `versify`); 5:20 at *cœpit* (row 584) and 7:19 at
  *respondit* (row 862), the numerals a line lower beside lines that open mid-word; 10:28 at *Ita* (row 1288); 10:29
  at *videlicet* (row 1292; the *29* stands beside *-strinxerat*, three lines below the KJV's start at *quamquam*, for
  `versify`); 17:19 at *eousque* (row 2028; the numeral beside that line); 17:29 at *Hemathenses* (row 2066; numeral
  at the line's start); 20:19 at *Et Ezechias* (row 2496; wide space); 21:15 at *quoniam me* (row 2571; wide
  space); 25:28 at *eumque* (row 3079).
- **Readings kept** (looked at): row 1574 *cecidisses* (the gutter takes the first letter; *e* stands second, so
  not *cæcidisses*); row 1391 *Et* (11:17) lost in the gutter but for a sliver, restored like the other gutter
  letters; row 1593 *Ioas* (13:25, *I* and the numeral lost in the gutter); row 2201 *aram* (a fibre crosses the
  *r*); row 3021 *eubitus* (printed so, a misprint for *cubitus*; the vote had silently corrected it); row 364
  *quær eret* (the gap printed).
- **Chapter 23**: the vote had *CAPVT XXIII* at row 2699 as `\c 21`; reader 10 corrected it on the page.
- **Signatures and catchwords** are kept as `%` rows, as every reader wrote them.

---

## reader-01 (`reader-01.md`)

# Reader 01: rows 2–259 (2 Kgs 1:1 – 3:15 *Sed arcessatur*), leaves 429–431

Every row was read on the whole page images (`1738-page-0429/0430/0431.jpg`), zoomed column by column with ffmpeg
(1.4–1.5×, 4–5× at doubtful letters and stops). The reading sheets were not needed: the vote's leaf/column/line labels
match the pages line for line (line counts checked per column: 429 col. 0 = 31 lines, col. 1 = 36; 430 col. 0 = 21 +
24, col. 1 = 50; 431 col. 0 = 35 + 8, col. 1 = 50). 1750 (`sources/archive/1750/text.txt` lines 50922–51230) was used
only as a check on wording and on the margin numbers the gutter cut.

## Leaves and what is on them

- **429** (p. 357, *Cap. 1.*): end of 1 Kings above the rule (not mine), title *REGVM LIBER IIII.*, *CAPVT I.* and its
  italic summary (not in the vote; nothing removed). 1:1 *MORTVO* – 1:15 *Tum*: col. 0 rows 3–33 (line 22 = `\c 1`),
  col. 1 rows 34–69. Foot: signature *Z 3*, catchword *Elias* → added `+ 429 1 900 % Z 3 Elias`.
- **430** (p. 358, *Cap. 1. 2.*): col. 0 rows 70–90 (1:15 *Elias* – 1:18), rule, *CAPVT II.* and summary (not in the
  vote), rows 92–115 (2:1 – 2:5 *Quibus*); col. 1 rows 116–165 (2:5 *ille respondet* – 2:16 *in ali-*). Foot: footnote
  *d)* (set across the page foot under col. 0, but its call is in col. 1) and catchword *quem* → added
  `+ 430 1 900 % d) columen atque præsidium.` and `+ 430 1 901 % quem`. No signature (verso).
- **431** (p. 359, *Cap. 2. 3.*): col. 0 rows 166–200 (2:16 *quem* – 2:25), rule, *CAPVT III.* and summary (not in the
  vote), rows 202–209 (3:1 – 3:3 *Sed*); col. 1 rows 210–259 (3:3 *Ieroboami* – 3:15 *Sed arcessatur*). Foot: footnote
  *e)* (again under col. 0, call in col. 1), signature *Z 4* (a dot after Z, *Z· 4*, probably a stray), catchword
  *mihi* → added `+ 431 1 900 % e) administro.` and `+ 431 1 901 % Z 4 mihi`.

The `\c 1`, `\c 2`, `\c 3` rows (2, 91, 201) stand where the page's *CAPVT I./II./III.* stand; kept unchanged.

## Verse numbers

The vote's numbers were wrong almost everywhere after 1:1 (it numbered ch. 1 from 2 at *misit-*, ch. 2 and 3 with a
growing lag); every `#N` placed again from the margin.

- **Ch. 1.** Leaf 429 col. 0's numbers (2–7) stand in the gutter and are cut away entirely (only ink traces at the edge),
  so 2–7 are placed by sense, the wide spaces, the sequence and 1750's margin (which follows 1738's lines and has *5* at
  *His ad nuntios*, *5*[=6] on the *respondent: occurrit* line, *7* at *Tum ille*): **2** *Ochozias autem* (row 5),
  **3** *At Iouæ angelus* (12), **4** *Itaque hoc* (18), **5** *His ad nuntios* (21), **6** *occurrit nobis* (24; the
  number would stand by the line *respondent: occurrit*, which begins mid-clause *ita / respondent*, so the start in it is
  *occurrit*, after the wide space; KJV's 6 begins with "And they said"), **7** *Tum ille* (33). Col. 1 margin, all
  legible: **8** *Homo hir-* (35), **9** *misit-* (38), **10** *Si diuinus* (43), **11** *At* (48), **12** *Atque ignis
  diuinus* (56), **13** *Sed rex* (58), **14** *Quumque* (65), **15** *Tum* (69). Leaf 430: **16** margin by the line
  *eique ita locutus est: [wide] hæc est* (73): placed at *eique* (line start; KJV 16 "And he said unto him"); the wide
  space before *hæc* is the usual one before speech. **17** *Atque ille* (81), **18** *De re-* (87).
- **Ch. 2.** **1** *CEterum* (92). **2**: the margin *2* stands by the line *batur, vt ibi maneret: [wide] sese enim*
  (96), whose first word ends *horta-/batur*; placed at **`vt ibi maneret`** (KJV 2 "Tarry here"). Please check: one
  could also put it at *Elisæum* (row 95, line start, "And Elijah said unto Elisha") a line above the numeral. **3**
  *Deinde illis* (100). **4**: the margin *4* is clearly by the line *caput tuum raptum iri? [wide] Quibus* (104), so
  1738 starts 4 at **`Quibus`** ("Yea, I know it; hold ye your peace", which KJV ends verse 3 with); KJV's 4 begins at
  *Tum Elias* (row 106). 1750 has its *4* on the same line. Kept as printed; flag for the edited text's versification.
  **5** *Deinde* (110, margin on the left of col. 0: *5 vt ego te non relinquam. Deinde*). Col. 1 (right margin
  legible): **6** *Hortantique* (117), **7** *Atque vbi* (122), **8** *cepit* (125; the vote had none), **9** *Post*
  (128), **10** *Rem* (134, numeral printed *1c*, the 0 damaged), **11** *His* (137), **12** *o pater* (143, numeral
  half-cut), **13** *et, sublata* (147; the wide space stands before *et,*; numeral half-cut *1;*), **14** *Atque vbi ad
  Iordanis* (149), **15** *Eum* (156), **16** *hortaban-* (161). Leaf 431 col. 0 (left margin legible): **17** *Ille*
  (167), **18** *Quibus* (173), **19** *Deinde* (175), **20** *Quo* (181), **21** *sic dicit* (184), **22** *Ita
  salubris* (187), **23** *Inde* (189), **24** *Quos* (193), **25** *Illinc* (198).
- **Ch. 3.** **1** *IOramus* (202), **2** *fuitque* (206, after the wide space), **3** *Sed* (209), **4** *Ce-* (212),
  **5** *Itaque* (218), **6** *mi-* (220; *mi-/sitque*: the vote's `#6` and `#7` both moved/removed), **7** *Ille re-*
  (225), **8** *Cui ille* (229), **9** *Igitur* (231), **10** *Atque hic* (235), **11** *At Iosaphatus* (238), **12** *Et
  Iosaphatus* (244), **13** *Tum Elisæus* (248), **14** *Et Eli-* (254), **15** *Sed arcessatur* (259).

## Letters lost in the gutter (read from the traces and the sense)

- Leaf 429 col. 0, line starts faint/cut: rows 26 *a quo*, 27 *eo*, 29 *vt*, 30 *dei*, 31 *lecto* (vote *celo*),
  32 *quam*, 33 *turum* (the *t* lost).
- Leaf 431 col. 0, top lines worn: row 166 *quem montem* (*m* of *montem* faint), 167 *esset.*, 168 *garet* (*ar*
  faint), 169 *victus*, 170 *nes*. All agree with 1750.

## Misprints and odd forms kept as printed

- Row 210 *filii* is set in **italic** type in a roman line (wrong-fount; written plainly).
- Row 253 *conuocauerit*: a mark like a grave accent stands over the second *a* (*conuocàuerit*); I take it for a
  damaged sort or ink, and wrote *conuocauerit*. Please look (leaf 431 col. 1 line 98).
- Row 143 *mante:* the colon's lower dot is sunk below the line (looks like *mante .*); read as a colon.
- Commas set without a following space, kept: row 25 *quidam,qui*, 51 *misit,qui*, 52 *rex,vt*, 136 *minus,non*.
- Row 44 is printed *( inquit ille respondens )* with spaces inside the parentheses; written *(inquit ille
  respondens)*.
- Tight settings given their space: *mo quidam* (25), *Elia perlatis* (22), *et ex eis* (15), *ita adlocutus* (42),
  *de cælo*, *qui te* (45), *Eli-/sæus* etc.
- Row 188 *Elisæi* (vote *Elisei*); row 49 *alterum* (vote *alteram*); row 11–12 the page has *morbo con- / ualiturus*
  (vote *mor- / bo tutus*); row 31 *lecto* (vote *celo*); row 214 *Israelitarum* without diaeresis (vote *Israélitarum*).
- Row 101 *bethelenses* and 112 *hierichuntii*, 158 *elianum* in lower case, as printed.

## Paragraph indents and drop capitals

No indented line in rows 2–259: every line starts flush at its column's edge. Drop capitals: row 3 *MORTVO* (M over
three lines; the rest in capitals), row 92 *CEterum*, row 202 *IOramus*.

## Footnotes

- **d)** *columen atque præsidium.* — hangs on *currus* (row 144, *tarum ᵈ currus et equites*, the italic *d* taken out;
  2:12 "the chariot of Israel"). Printed across the foot of leaf 430 under col. 0, placed after col. 1's text.
- **e)** *administro.* — hangs on *adpareo* (row 256, *cui ego ᵉ adpareo*, the *e* taken out; 3:14 "before whom I
  stand"). Printed at the foot of leaf 431 under col. 0, placed after col. 1's text.

## G./L./H. marks and asterisks

No *G.*, *L.* or *H.* in my range. One asterisk with no footnote: row 221 *Iosaphatum \* Iudææ* (taken out). The vote's
asterisk at row 210 *scelera\** is not on the page (zoomed: a faint blemish by the comma, no asterisk); the vote's `<*`
at row 117 is OCR noise. Row 171 *neque* has a speck above, not a mark.

## Rows lost, added, removed

- Added (5): `+ 429 1 900 % Z 3 Elias`, `+ 430 1 900 % d) …`, `+ 430 1 901 % quem`, `+ 431 1 900 % e) administro.`,
  `+ 431 1 901 % Z 4 mihi`.
- Removed: none. No text line lost by the OCR.

## Wording doubts (1738 against 1750)

None beyond spelling and OCR noise: 1750 reads the same words line for line in all three chapters (checked e.g. 1:2
*conualiturus*, 1:6 *lecto*, 2:2–4, 2:10 *Si me a te*, 2:19 *verum et aquam*, 3:4 *arietum pensitabat*, 3:6
*Iosaphatum*). Nothing looks misprinted against the sense.

## Omission check (against the BSB/KJV)

Each verse 1:1–3:15 read against the BSB. Castellio condenses throughout (e.g. 1:2 gives the messengers' errand in
indirect speech; 1:15's angel's words in indirect speech; 2:3/2:5 the prophets' question indirect), but no clause of
the Hebrew is missing from the page that my reading lost, and every printed line is in the rows (line counts above). 3:7
has Jehoshaphat's answer only in indirect form (*seque et suos homines equosque in illius arbitrio futuros*), without
"I am as thou art, my people as thy people" spelled out — Castellio's condensing, not a lost line.

## Uncertain readings and how settled

- 2:2 placement (row 96) and 2:4 at *Quibus* (row 104): see above; want Claude's call.
- Row 253 the accent-like mark on *conuocauerit*.
- Row 61 *peruenit;* — zoomed: semicolon (1750 also *;*).
- Ch. 1 verses 2–7 placed by sense with 1750's margin, since 1738's are cut.

## Summary

258 rows of the vote read (2–259), 192 changed from the vote, 0 removed, 5 added (2 footnotes, 2 signature/catchword
rows, 1 catchword); 263 rows written.

## reader-02 (`reader-02.md`)

# Reader 02: rows 260–556 (2 Kgs 3:15 *mihi fidicen* – 5:14 *in tantam cor-*), leaves 432–434

Every row was read on the whole page images (`1738-page-0432/0433/0434.jpg`), each column zoomed in four bands at 2×,
and at 4–6× for doubtful stops and marks. The reading sheets were not needed: the vote's leaf/column/line labels match
the pages line for line (432 col. 0 = lines 4–54, 51 lines; col. 1 = 55–57, rule, *CAPVT IIII.* and summary, 63–104;
433 col. 0 = 4–52 + two footnote lines; col. 1 = 55–103 + signature/catchword; 434 col. 0 = 4–34, rule, *CAPVT V.* and
summary, 38–52; col. 1 = 53–103 + catchword). 1750 (`sources/archive/1750/text.txt` lines ~51290–51700) used only as a
check on wording and margin numbers.

## Leaves and what is on them

- **432** (p. 360, *Cap. 3. 4.*): col. 0 rows 260–310 (3:15 *mihi fidicen* – 3:28 *Hac tanta atro-*); col. 1 rows
  311–313 (end of ch. 3), rule, *CAPVT IIII.* and italic summary, rows 316–357 (4:1 – 4:10 *quandocumque ad eos
  veniet,*). Foot: catchword *ibi*, no signature (verso) → added `+ 432 1 900 % ibi`.
- **433** (p. 361, *Cap. 4.*): col. 0 rows 358–406 (4:10 *ibi diuersetur* – 4:25 *aduenienti Sunamiti*); footnotes *f)*
  and *g)* set across the page foot (both calls in col. 0) → rows 407, 408 (the vote's garbled OCR of the footnotes,
  re-used for the notes, kept in col. 0); col. 1 rows 409–457 (4:26 *illi curreret* – 4:38 *puero iussit,*); foot:
  signature *Z 5*, catchword *vt* → row 458 (the vote's line 105, which held the middle of the footnote line
  *interprece fjreulo. g) nihil foris cum*) re-used as `% Z 5 vt`.
- **434** (p. 362, *Cap. 4. 5.*): col. 0 rows 459–489 (4:38 *vt ollam* – 4:44 *fuerat.*), rule, *CAPVT V.* and
  summary (not in the vote), rows 491–505 (5:1 – 5:3 *illo discussum iri.*); col. 1 rows 506–556 (5:4 *Hæc
  Israelitidis* – 5:14 *in tantam cor-*). Foot: catchword *poris*, no signature → added `+ 434 1 900 % poris`.

`\c 4` (row 314) and `\c 5` (row 490) stand where the page's *CAPVT IIII.* and *CAPVT V.* stand: kept.

## Verse numbers

All margins legible on these three leaves (no gutter loss). The vote's numbers were placed wrongly almost
everywhere; every `#N` placed again from 1738's margin.

- **Ch. 3** (continuing reader 01): **16** *iubet Ioua* (262, line start), **17** *namque* (263), **18** *Atque hoc*
  (268), **19** *expugnabitisque* (270), **20** *Igitur* (276), **21** *Et omnes* (279), **22** *simulac* (284, line
  start; vote at *vident*), **23** *ratique* (287), **24** *Sed exciti* (291), **25** *oppida* (294), **26** *Quam
  quum* (300), **27** *Moabitarum rex* (303), **28** *Sed post-* (306).
  **Flag: 1738 numbers ch. 3 to 28 verses, KJV 27.** It splits KJV 25 at *Quam quum funditoribus* (the slingers =
  KJV 25b), so its 26 = KJV 25b, 27 = KJV 26, 28 = KJV 27. The margin numerals are clear and in sequence (1750 has the
  same 26/27/28 on the same lines). Kept as printed; for the edited text's versification.
- **Ch. 4** (agrees with KJV throughout, 44 verses): **1** *MVlier* (316), **2** *Quærentique* (322), **3** *Tum ille*
  (327), **4** *dein-/de ingressa* (329), **5** *Illa ab eo* (333), **6** *Vasis* (336), **7** *Ita cohibito* (339,
  line start), **8** *Item* (343), **9** *Igitur* (349), **10** *persuadetque* (353, after the wide space), **11**
  *Quodam die* (358), **12** *iussit Gihezi* (361), **13** *eaque vocata* (362), **14** *Illique* (369), **15** *Tum
  illi* (373), **16** *tu hac* (375), **17** *Concepit* (379), **18** *Is puer* (382), **19** *Et pater* (385), **20**
  *ad quam* (387), **21** *Illa ad lectum* (390), **22** *et vocato* (392), **23** *Quærenti* (396), **24** *Ita
  instrata* (399), **25** *Atque ita* (402), **26** *eamque interrogaret* (409: the margin *26* is by the line *illi
  curreret obuiam, [wide] eamque in-*; placed at the wide space. KJV 26 begins "Run now" = *illi curreret*, a line
  start; please check which you prefer), **27** *et diuinum* (412), **28** *Et illa* (418), **29** *Hic il-* (420),
  **30** *Sed pueri* (426), **31** *Tum ille surgit* (429), **32** *Tum Elisæus* (435), **33** *precatusque* (439),
  **34** *Hoc* (442), **35** *Tum puer* (446), **36** *Quæ postquam* (450), **37** *Illa ei* (452), **38** *Elisæus
  Galgala* (455), **39** *Et quidam* (461), **40** *Deinde* (466), **41** *Ille* (470), **42** *Item a Baalsalisa*
  (476), **43** *Cui minister* (482), **44** *Tum ille ad-* (486).
- **Ch. 5**: **1** *ERat* (491), **2** *Apud* (497), **3** *Hæc* (501), **4** *Hæc Israelitidis* (506; vote had it on
  row 505), **5** *iussit rex* (508), **6** *simulac* (516), **7** *Hac lecta* (519), **8** *Postquam* (527), **9**
  *Venit* (533), **10** *et ei illic* (535), **11** *Sed indignatus* (539), **12** *Quasi vero* (544), **13** *Quum*
  (547), **14** *Ita ille* (554).

## Letters lost in the gutter

None: all three leaves are clean at the inner edge on these columns.

## Misprints and odd forms kept as printed

- Row 277 *fertum* (Castellio's word for the meal offering, as elsewhere in 1750 Leviticus/Numbers): not *sertum*.
- Row 299 *Harasetham* (long s, read on the zoom; vote *Harafetham*).
- Row 305 *Idumææ*; 304 *prœlio*; 309 *mœ-/nibus*; 384 *cœpit* (but 307 *cepit*, both as printed).
- Row 525 *sultis* (= *si vultis*), as printed (1750 the same).
- Row 545 *damasceni* in lower case, as printed.
- Commas set without a following space, kept: 368 *respondet,se*, 382 *educatus,quodam*, 492 *Syriæ,vir*, 528
  *nus,regem*, 530 *dum,cur*, 543 *et,admota*.
- Tight settings given their space: 479 *in glumis* (vote *inglumis*; the page has a thin space), 543 *admota loco*,
  302 *vt iam*, 363 *iussit illi*.
- Row 364 *quæreret* is printed with a gap inside it (*quær eret*), a loose sort; written as one word.
- Row 378 *imponere.*: the stop is damaged (a full stop with a smudge beside it, at the column edge); read as a full
  stop (1750 *imponere.*; next sentence begins *Concepit*).
- Row 268 *vtamini.*: zoomed at 6×, a full stop slightly tilted, not a comma.
- Row 379 *peperit-* the hyphen is a heavy dot-like sort; a hyphen.

## Paragraph indents and drop capitals

Indented lines: rows **382** (*Is puer*, 4:18), **455** (*Elisæus Galgala*, 4:38), **476** (*Item a Baalsalisa*,
4:42), **506** (*Hæc Israelitidis*, 5:4), **527** (*Postquam accepit*, 5:8). Drop capitals: row 316 *MVlier* (M over
three lines; the rest of the word in capitals as *V*), row 491 *ERat*. No other indent.

## Footnotes

- **f)** *Elisæus eius linguæ ignarus, vtebatur interprete famulo.* — hangs on *iussit illi* (row 363, *adstante, ᶠ
  iussit illi*; 4:13, Elisha speaking to the woman through Gehazi). The italic *f* taken out of the text.
- **g)** *nihil foris cum quoquam negotii habere.* — hangs on *inter suos se continere* (row 368, *se ᵍ inter suos
  se*; 4:13 "I dwell among mine own people"). The *g* taken out. Note *g)* begins at the right of the foot line
  after *f)* and runs on under col. 0 (*quoquam negotii habere.*; the *a* of *habere* damaged).

Both are written as `%` rows 407, 408 after col. 0's last text row (406).

## G./L./H. marks and asterisks

No *G.*, *L.* or *H.* in my range. One asterisk with no footnote: row 452 *accidit, \* et eum* (4:37), taken out.

## Rows lost, added, removed

- Removed: row 315 (432/1/62, `#1 multipltifltio fer Eiiftum.`), the last line of ch. 4's italic summary
  (*multiplicatio per Elisæum.*).
- Re-used: 407, 408 (footnote OCR) for the footnotes; 458 (footnote OCR fragment) for signature/catchword.
- Added (2): `+ 432 1 900 % ibi`, `+ 434 1 900 % poris`.
- No text line lost by the OCR, but several garbled lines rebuilt from the page: 393–394 (*ali-/quem mittat* — the vote
  lost *mittat*), 433 (*cem ederet* — vote lost *ederet*), 412 (*Illa re-/spondit*), 539–540 (*reuersurum. Sed
  indignatus Na-/aman, discedebat.* — vote *reuersurum. ama-/n , discedebat.*), 491–496 (drop capital and *(nam per
  eum Syris Ioua victoriam dederat)*).

## Wording doubts (1738 against 1750)

None beyond spelling and OCR noise. 1750 reads the same words line for line (checked 3:20 *fertum*, 3:25–28, 4:2
*habe-/ret?*, 4:13 *se inter suos se continere*, 4:16 *imponere*, 4:22 *aliquem mittat*, 4:31 *vocem ederet*, 4:42
*primitiarum panes hordeaceos*, 5:5, 5:7 *sultis*, 5:11 *Sed indignatus Naaman, discedebat*). Nothing looks
misprinted against the sense.

## Omission check (against BSB/KJV)

Each verse 3:15b–5:14a read against the KJV/BSB. Castellio condenses (indirect speech in 4:1–2, 4:13–14, 5:3, 5:8),
but no clause of the Hebrew is missing that the page has and my reading lost. 3:27 "there was great indignation
against Israel" is rendered *Hac tanta atrocitate permoti Israelitæ* (Castellio's reading, not a loss). 4:13 Elisha's
speech to the woman goes through Gehazi as interpreter (*iussit illi, vt ex ea quæreret*), with note *f)*.

## Uncertain readings and how settled

- 3:26–28 (1738's extra verse): kept as printed; flag for versification.
- 4:26 at *eamque* (wide space) vs *illi* (line start): want Claude's call.
- Row 378 damaged stop after *imponere*: read as full stop.
- Row 364 *quær eret* gap: written *quæreret*.

## Summary

296 rows of the vote read (260–556), 1 removed (315), 209 changed from the vote, 2 added (catchwords *ibi*, *poris*);
298 rows written.

## reader-03 (`reader-03.md`)

# Reader 03: rows 557–854 (2 Kgs 5:14 *poris puritatem* – 7:17 *a rege præposi-*), leaves 435–437

Every row was read on the whole page images (`1738-page-0435/0436/0437.jpg`), each column zoomed in four bands at 1.6×,
and at 3–4× for doubtful letters and stops. The vote's leaf/column/line labels match the pages line for line. 1750
(`sources/archive/1750/text.txt` lines ~51655–52060) used only as a check on wording and margin numbers.

## Leaves and what is on them

- **435** (p. 363, *Cap. 5. 6.*): col. 0 rows 557–607 (5:14 *poris puritatem* – 5:24 *Hæc*); col. 1 rows 608–624
  (end of ch. 5), rule, *CAPVT VI.* and italic summary, rows 627–653 (6:1 – 6:9 *misit diuinus signifi-*). Foot:
  catchword *catum*, no signature → added `+ 435 1 900 % catum`.
- **436** (p. 364, *Cap. 6.*): col. 0 rows 654–704 (6:9 *catum Israelitarum* – 6:21 *His*); col. 1 rows 705–755
  (6:21 *conspectis* – 6:33 *eum-*). Foot: catchword *que*, no signature → added `+ 436 1 900 % que`.
- **437** (p. 365, *Cap. 7.*): col. 0 rows 756–763 (end of ch. 6), rule, *CAPVT VII.* and italic summary, rows
  767–803 (7:1 – 7:8 *vbi*); col. 1 rows 804–854 (7:8 *ad extrema castra* – 7:17 *a rege præposi-*). Foot: catchword
  *tus,* (leaf 438 begins *tus, a turba oppressus*), no signature → added `+ 437 1 900 % tus,`.

`\c 6` (row 625) and `\c 7` (row 764) stand where the page's *CAPVT VI.* and *CAPVT VII.* stand: kept.

## Verse numbers

Margins: on 435 col. 0 and 436 col. 0 the numbers stand on the left, clear; on 435–437 col. 1 on the right, clear;
on 437 col. 0 they stand in the gutter, partly cut (see below). The vote's numbers were mostly a line or a word off;
every `#N` placed again from 1738's margin.

- **Ch. 5** (27 verses, as KJV): **15** *De-/inde* (558, after the wide space), **16** *Sed ille* (565), **17** *Tum
  Naaman* (569), **18** *Hanc quidem* (574), **19** *Cui vates* (581), **20** *cœpit Gihezis* (584, placed by sense:
  **the margin *20* stands one line lower**, beside 585 *ni famulus sic secum loqui: hem,*, where no sentence begins;
  1750 has its *20* on the same line. KJV 20 "But Gehazi … said" = *cœpit Gihezis*; 19b "so he departed" =
  *Quumque … processisset*. Please confirm), **21** *Hæc lo-/cutus* (590), **22** *Salua, inquit ille* (595), **23**
  *Cui Naaman* (602, line start), **24** *Hæc* (607, last word of col. 0), **25** *et quæ-/renti* (611), **26** *At
  ille* (614, line start), **27** *Er-/go* (620).
- **Ch. 6: 1738 numbers 34 verses, KJV 33.** **1** *PEtierunt* (627), **2** *irent* (630), **3** *Atque illo
  permit-/tente* (633), **4** *Vbi ad Iordanem* (637), **5** *Qui quum* (641), **6** *interrogauit* (644, line start),
  **7** *Atque ille* (648), **8** *Item* (649), **9** *misit diuinus* (653), **10** *Itaque* (657), **11** *Qua re*
  (661), **12** *Cui suorum* (666), **13** *Tum ille imperat* (671), **14** *Atque vbi* (673), **15** *Mane* (677),
  **16** *Cui ille* (682), **17** *Deinde* (684), **18** *Postquam* (691), **19** *Quod postquam* (694), **20** *Ita
  eos* (699; margin *20* printed hard against *rant.*), **21** *His* (704, last word of col. 0), **22** *Noli
  occidere* (707), **23** *Tum ille* (712), **24** *Postea* (717), **25** *qua obsidione* (719), **26** *Ac, rege*
  (724), **27** *Cui ille* (727), **28** *Sed tamen* (730), **29** *Ita fi-/lium* (735), **30** *Hac audita* (740),
  **31** *Deus me* (745), **32** *Hæc locutus* (747), **33** *sciendum* (752, line start), **34** *Eo adhuc* (758).
  1738 splits KJV 32 at *sciendum vobis est* (Elisha's words, "See ye how this son of a murderer…"): 1738 32 = KJV
  32a, 33 = KJV 32b, 34 = KJV 33. Numerals clear and in sequence (1750 has the same 33/34). For the edited text's
  versification.
  Within-verse boundaries that differ slightly from KJV (no change in count): 1738 3 begins *Atque illo permittente*
  (KJV 2b "And he answered, Go ye"); 1738 4 runs to *decideret* (KJV 5a "as one was felling a beam"), 5 begins *Qui
  quum vociferaretur*; 1738 7 begins *Atque ille, porrecta manu* (KJV 7 "Take it up"); 1738 14 begins *Atque vbi ei
  nuntiatum est* (KJV 13b "it was told him … Dothan").
- **Ch. 7** (to v. 17; agrees with KJV in count): **1** *AT* (767), **2** *Tum triumuir* (772), **3** *Erant* (778),
  **4** *Siue* (782), **5** *Ita sub crepusculum* (788; vote had it before *moriamur*, which ends v. 4), **6**
  *Fecerat* (792), **7** *Ita-/que* (798), **8** *Igitur* (803), **9** *Deinde in-/ter* (811), **10** *Ita ianitorem*
  (818), **11** *Tum ille* (824), **12** *At rex* (827), **13** *Tum quidam* (834), **14** *Ita sumtis* (840), **15**
  *qui illos* (843), **16** *Quod postquam* (847; KJV puts "the messengers returned, and told the king" at the end of
  15), **17** *Triumuir* (852).

## Letters lost in the gutter

No text letters lost. Leaf 437 col. 0's margin numbers are in the gutter and partly cut: *34* shows only its *4*
(row 758), *8* only its right half (row 803); 1–7 legible. Placed by the fragments and the sequence.

## Misprints and odd forms kept as printed

- Row 589 *talem*: the *l* is a broken sort (looks like *taiem*, a dot above a short stroke); read *talem* (1750
  *talem*).
- Row 775 *istud*: the long s is damaged (looks *iltud*); read *istud*.
- Row 729–730 *ab are-/ane?* as printed (1750 the same *abare-/ane*); Castellio's form for "from the barnfloor".
- Row 792 *Fecerat enim Dominus*: *Dominus*, not *Ioua*, as printed (1750 the same).
- Row 796 *Aegypti-*: *A* and *e* separate, not *Æ*.
- Row 603 *coegit* with plain *oe*; 780, 812 *cœperunt* and 584 *cœpit* with the ligature, as printed.
- Row 723 *columbini*; 734 *comessemus*; 735 *comesuræ*; 845 *supellectile*; 850 *væ-/niitque*; 837 *israelitico-*
  lower case: all as printed.
- Commas set without a following space, kept: 619 *oleas,vineas,balan-*, 620 *tes,boues*, 719 *inuasit,obseditque*,
  720 *incessit,vt*, 829 *Sciunt,nos*.
- Tight settings given their space: 621 *go Naamanis* (page *goNaamanis*), 784 *est. Quam-*.
- Row 845 *plenam ,*: comma set after a space; written *plenam,*. Row 742 *( in*: written *(in*.
- Stops checked at 3–4×: 607 *illi.* (full stop), 778 *comedes.* (a damaged full stop), 816 *subituros.* (full stop),
  777 *ille;* (semicolon).

## Paragraph indents and drop capitals

Indented line: row **717** (*Postea Benadadus*, 6:24). No other indent on the three leaves. Drop capitals: row 627
*PEtierunt* (P over three lines), row 767 *AT* (A over three lines; the *T* in capitals, so written *AT*).

## Footnotes

None on these leaves.

## G./L./H. marks and asterisks

- Row 619 *G. L. vt emas H.* (5:26), italic, kept as printed.
- Asterisks with no footnote, taken out: row 723 *columbini \* quinque* (6:25); row 761 *rex, \* ita loquitur* (6:33).

## Rows lost, added, removed

- Removed: row 626 (435/1/77, `#1 efiu. In Etiftum regis rabies.`), the last line of ch. 6's summary (*esus. In
  Elisæum regis rabies.*); rows 765–766 (437/0/14–15), the last two lines of ch. 7's summary (*Leprosorum præda.
  Triumuiri a multitudine oppressio.*).
- Added (3): catchwords `+ 435 1 900 % catum`, `+ 436 1 900 % que`, `+ 437 1 900 % tus,`.
- No text line lost by the OCR. Garbled lines rebuilt from the page: 655–657 (*progrede-/retur … Itaque*), 671–672
  (*visant, vbi / sit, vt mittat*; the vote lost *mittat*), 694 (*ret. Quod postquam ille ad Eli-*), 699–700
  (*perdu-/xit*), 705–707 (*rex ita Eli-/sæum adloquitur … inquit il-/le*: the vote lost *Eli-/sæum* and *il-*), 733
  (*ego darem*), 767 (drop capital *AT*), 772, 781–782 (*operi-/mur?*), 801–803 (*equis … con-/suluerant*), 804 (*in*).

## Wording doubts (1738 against 1750)

None beyond spelling, punctuation and OCR noise. Checked: 5:16 *acciperet.* (1750 *acciperet:*), 5:20 *parsit*,
6:13 *vt visant, vbi sit, vt mittat*, 6:21 *rex ita Elisæum adloquitur*, 6:27 *ab are-/ane*, 6:30 *interius
vestitum*, 7:2 *panderet* (1750 OCR *ponderet*, noise; 1738 clear *panderet*), 7:6 *Dominus*, 7:13 *ex regiis ei*.
Nothing looks misprinted against the sense.

## Omission check (against BSB/KJV)

Each verse 5:14b–7:17a read against the KJV/BSB. Castellio condenses (5:26–27, 6:13 "Go and spy where he is",
7:13 "they are as all the multitude of Israel that are left … consumed" → the parenthesis *totidem enim superesse
…*), and 6:21 "shall I smite them? shall I smite them?" is given once (*occidamne pater?*): his rendering, not a loss.
No clause the page has is missing from my reading.

## Uncertain readings and how settled

- 5:20 placed at *cœpit* though the margin numeral is one line lower (above): want Claude's call.
- 6:34 (1738's extra verse): kept as printed; flag for versification.
- Row 589 *talem* (broken l), 775 *istud* (damaged ſ): read as the words.

## Summary

298 rows of the vote read (557–854), 3 removed (626, 765, 766), 209 changed from the vote, 3 added (catchwords
*catum*, *que*, *tus,*); 298 rows written.

## reader-04 (`reader-04.md`)

# Reader 04: rows 855–1147 (2 Kgs 7:17 *tus, a turba oppressus* – 9:35 *Sed qui ad eam se-*), leaves 438–440

Every row read on the whole page images (`1738-page-0438/0439/0440.jpg`), each column zoomed in four bands at 1.5×,
and at 3–7× for doubtful letters, stops and margin numerals. The vote's leaf/column/line labels match the pages line
for line. 1750 (`sources/archive/1750/text.txt` lines ~52077–52520) used only as a check on wording and margin numbers.

## Leaves and what is on them

- **438** (p. 366, *Cap. 8.*): col. 0 rows 855–869 (7:17 *tus, a turba* – 7:20 end), rule, *CAPVT VIII.* and italic
  summary (not in the vote's rows), `\c 8` (870), rows 871–899 (8:1 – 8:7 *vt mulieri*); col. 1 rows 900–950 (8:7
  *omnia sua restitueret* – 8:19 *qui erant ex Achabi*). Foot: catchword *fami-*, no signature → added
  `+ 438 1 900 % fami-`.
- **439** (p. 367, *Cap. 8. 9.*): col. 0 rows 951–994 (8:19 *familia* – 8:30 end of ch. 8), rule, *CAPVT IX.* and
  italic summary (not in the vote's rows), `\c 9` (995), and at the column's foot the footnote *b) insanus.* → added
  `+ 439 0 900 % b) insanus.` after row 995; col. 1 rows 996–1045 (9:1 *TVm* – 9:12 *postulantibus: il-*). Foot:
  catchword *lius*, no signature → added `+ 439 1 900 % lius`.
- **440** (p. 368, *Cap. 9.*): col. 0 rows 1046–1096 (9:12 *lius dicta refert* – 9:22 *Iehu? Cui*); col. 1 rows
  1097–1147 (9:22 *ille: quid* – 9:35 *Sed qui ad eam se-*). Foot: catchword *pelien-* (leaf 441 begins *peliendum
  iuerunt*), no signature → added `+ 440 1 900 % pelien-`.

`\c 8` (row 870) and `\c 9` (row 995) stand where the page's *CAPVT VIII.* and *CAPVT IX.* stand: kept.

## Verse numbers

Margins: 438 col. 0 left, clear; 438 col. 1 right, the last three (17, 18, 19) cut by the gutter to *1* and a
fragment; 439 col. 0 in the gutter, cut (20 shows *o*, 21 *I*, 22 *2*, 23–30 the units digit only); 439 col. 1 and
440 both columns clear. All placed by fragment, sequence and sense; the vote's numbers were mostly wrong and all
were placed again.

- **Ch. 7 (end)**: **18** *tum, quum diuino* (858, after the wide space), **19** *respondit triumuir* (862, placed by
  sense: **the margin *19* stands one line lower**, beside 863 *uir ille, etiamsi*, where no verse can begin
  mid-word; 1750 has its 19 on the same line. KJV 19 "And that lord answered" = *respondit triumuir ille*. Like
  reader 03's 5:20; please confirm), **20** *Id quod ei* (867).
- **Ch. 8: 1738 numbers 30 verses, KJV 29.** **1** *MOnuit* (871), **2** *His* (877), **3** *Præteritis* (881),
  **4** *Rex autem* (884), **5** *Atque* (888, line start), **6** *Tum rex* (896), **7** *vt mulieri* (899, after the
  wide space; margin *7* beside *dedit, cum mandato,*), **8** *Quum venisset* (903, indented), **9** *iussit rex*
  (906), **10** *Hazael illi* (910), **11** *Cui Eli-/sæus* (918), **12** *Hæc locutus* (922, line start), **13** *et*
  (923, last word), **14** *Et* (930, last word), **15** *Ita digressus* (935), **16** *Postri-/die* (938), **17**
  *Anno autem* (942, line start), **18** *Regnauit* (947), **19** *regumque* (948), **20** *Quamquam* (953), **21**
  *Huius* (957), **22** *Itaque* (959), **23** *At-/que ea* (964), **24** *Reli-/quæ* (967), **25** *Ioramo* (971,
  indented), **26** *idque* (974), **27** *Regnauit* (977), **28** *Achabi stirpis* (980), **29** *et* (982, last
  word), **30** *vbi quum* (986). 1738 splits KJV 6 at *vt mulieri omnia sua restitueret* ("saying, Restore all that
  was hers"): 1738 7 = KJV 6b, and 1738 8–30 = KJV 7–29. 1750's margins agree (its 18–29 are legible, the same
  places). For the edited text's versification.
- **Ch. 9** (to v. 35; same count as KJV, but numbered differently between 18 and 22): **1** *TVm* (996), **2** *eo
  postquam* (1001), **3** *sumtaque* (1005), **4** *Igitur* (1010), **5** *quo vbi* (1013, line start), **6** *Tum
  Iehus* (1017), **7** *vt Achabi* (1023, line start), **8** *faciam-/que* (1026), **9** *Achabique* (1032), **10**
  *Quin etiam* (1036, line start), **11** *Iehus autem* (1039), **12** *Negantibus* (1044), **13** *Tum illi* (1048),
  **14** *Igitur* (1052), **15** *reuersus erat* (1058), **16** *Ipse* (1064), **17** *Quum-/que* (1067), **18**
  *Eques* (1073), **19** *Quum speculator* (1077; margin beside *recede pone me.*, which ends Jehu's answer in 18:
  placed after the stop and wide space), **20** *Qui vbi* (1080), **21** *Hoc quum* (1085, line start), **22** *At-/que,
  illo viso* (1094), **23** *Hic Ioramus* (1100), **24** *At Iehus* (1102), **25** *Eoque* (1105), **26** *quo
  oraculo* (1113), **27** *Hæc videns* (1119), **28** *Ille ad Mageddonem* (1124), **29** *Cœperat* (1128), **30**
  *Iehus vero* (1130), **31** *an impune* (1135, after *dixit:* and the wide space; KJV 31 begins "And as Jehu
  entered in at the gate", which is *Iehu prætereunte portam, dixit:* on the line before), **32** *At ille* (1136),
  **33** *præcipitate* (1140, after *nes:* and the wide space), **34** *Deinde* (1144), **35** *Sed qui* (1147).
  1738 against KJV: 1738 19 = KJV 18b ("And the watchman told…"), 20 = KJV 19, 21 = KJV 20–21 (*Hoc quum speculator*
  … *in fundo Nabothi*), 22 = KJV 22; in step from 22 on. Also 1738 33 runs on through *iuit ad sumendum cibum* (KJV
  34a "when he was come in, he did eat"); 34 begins *Deinde nefariam* (KJV 34b).

## Letters lost in the gutter

No text letters lost; only margin numerals (above).

## Misprints and odd forms kept as printed

- Row 875 *indîci*: a circumflex-like mark over the second *i* (zoomed 6–7×: a clear angled stroke, unlike the
  specks earlier readers set aside; the final *i* has its ordinary dot). Written *indîci* as printed (1750 *indici*);
  it marks *indīcī* (passive infinitive of *indīcō*). **Please check** whether the project keeps such accents in the
  OT printed text.
- Row 970 *dææ* (*Iu-/dææ*, genitive), as printed.
- Row 907 *Ha-/zaeli* with plain *ae* (not *æ*), as printed (zoomed).
- Row 1066 *decubabat* (for *decumbebat*?), as printed (1750 the same).
- Row 1123–1124 *Iebla-/am*; 1107 *Badacari*; 1123 *Gure*; 1133 *comsit*; 1031–1032 *commin-/ctorem*; 1042
  *limphatus*; 982 *achabicæ* and 1037 *iezraelensi* lower case (zoomed); 1094, 1108 *Iezraelensis* capital: all as
  printed.
- Row 990 *prœlio* with the ligature; 1128 *Cœperat*.
- Commas (and a paren) set without a following space, kept: 893 *Gihezis,do-*, 902 *reliquerat,ad*, 913
  *Atque,vbi*, 951 *familia,(nam*, 1009 *Deinde,aperto*, 1066 *decubabat,ad*, 1070 *bum,seque*, 1106 *eum,(inquit*,
  1120 *Ochozias,fugam*.
- Tight settings given their space: 867 *quod ei*, 891 *filium a*, 930 *et grauidas*, 1048 *illi ei*, 1073 *Eques
  illi*, 1104 *vt telum*, 1107 *Badacari) et in* (page *Badacari)etin*), 1138 *a me*, 1143 *iuit ad*.
- Spaces inside parentheses dropped: 890 *( cuius* → *(cuius*, 891 *reuocauerat )*, 952 *matrimonio )*, 1007 *( qui*,
  1008 *iubeat )*.
- Row 1142 *eius · murum*: a low speck between the words (zoomed 2.5×), no stop the sense allows: written *eius
  murum*.
- Stops checked at 3–4×: 921 *moriturum.*, 1022 *Israelitarum,* (comma), 1140 *inquit.* (a small, slightly raised
  full stop; 1750 *inquit,*), 1146 *iussit;* (semicolon), 1070 *dixisset;*, 897 *interrogauit;*.
- Row 1010 *iuuenis*: the first *i* is a damaged sort (heavy, dropped), read *iuuenis*. Row 1078 *nuntium* (damaged
  *t*), 1141 *Tum* (damaged *m*), 1146 *re-* (damaged *r*): read as the words.

## Paragraph indents and drop capitals

Indented lines: row **903** (*Quum venisset autem Elisæus*, 8:8 = KJV 8:7) and row **971** (*Ioramo vita defuncto*,
8:25 = KJV 8:24). No other indent on the three leaves. Drop capitals: row 871 *MOnuit* (M over three lines), row 996
*TVm* (T over three lines; the *V* in capitals, so written *TVm*).

## Footnotes

- **b)** *insanus.* (439 col. 0 foot, below *CAPVT IX.* and its summary), hanging on row 1042 *limphatus* (9:11,
  *venisset ᵇ limphatus ille*; letter taken out of the text row). The note stands at the foot of column 0 though its
  word is in column 1; placed as `+ 439 0 900` after `\c 9` (row 995), the last row of that column. (No note *a)* on
  these leaves.)

## G./L./H. marks and asterisks

None on these leaves.

## Rows lost, added, removed

- Removed: none (the chapter summaries of 8 and 9 were already off the vote).
- Added (4): catchwords `+ 438 1 900 % fami-`, `+ 439 1 900 % lius`, `+ 440 1 900 % pelien-`; footnote
  `+ 439 0 900 % b) insanus.`
- No text line lost by the OCR. Rows heavily rebuilt from the page: 862–867, 871–875 (drop capital), 916–927, 944,
  947–950, 959–970, 996–998 (drop capital), 1042, 1046–1053, 1061–1072, 1075–1090, 1100–1147 (the vote's 1105–1147
  are badly garbled: *teque in curru* → *Eoque in curru*, *fiadacari>etin* → *Badacari) et in*, *Iczradeniis* →
  *Iezraelensis*, *memmi* → *memini*, *:remur* → *sequeremur*, *loli£ iert* → *Iouæ fert*, *iussi* → *iussit*,
  *vedhis* → *vectus*, *remi Achabi sibi* → *rami Achabi filii*, *mini fiuim* → *num suum*, *nefa nam* → *nefa-
  riam*, etc.).

## Wording doubts (1738 against 1750)

None beyond spelling, punctuation and OCR noise. Checked: 7:18 *tum, quum diuino, regi pollicito* (1750 *tum quum
diuino regi pollicito*), 7:19 *aperiret*, 8:1 *indici*, 8:9 *Hazaeli* (1750 *Hazaéli*), 8:10 *ad sciscitandum*, 8:30
*Ramotha a Syris*, 9:10 *iezraelensi*, 9:17 *decubabat* (both), 9:25 *Badacari*, 9:26 *quem pridie vidisset*, 9:27
*in cliuo Gure, apud Ieblaam*, 9:33 *inquit.* (1750 *inquit,*). Nothing looks misprinted against the sense.

## Omission check (against BSB/KJV)

Each verse 7:17b–9:35a read against the KJV/BSB. Castellio condenses (8:5 "this is her son, whom Elisha restored to
life" kept; 8:11 "until he was ashamed" not rendered: *vultum aliquamdiu fixum flens tenuit*; 8:21 "and smote the
Edomites … and the captains of the chariots" → *Idumæos … adortus vicit, curruumque principes*; 9:17 "Take an
horseman" folded into the command; 9:33 "and he trode her under foot" → *Ille, ea conculcata*), his rendering, not a
loss. 9:31 "Had Zimri peace" → *an impune Zambris*. No clause the page has is missing from my reading.

## Uncertain readings and how settled

- 7:19 placed at *respondit* though the margin numeral is one line lower (above): want Claude's call.
- 8:7 placed at *vt mulieri* (margin beside *dedit, cum mandato,*); 9:19 at *Quum speculator*, 9:31 at *an impune*,
  9:33 at *præcipitate*: each after a stop and the wide space in the numbered line.
- Ch. 8 has 30 verses in 1738 (KJV 29); ch. 9's 19–21 differ from KJV within the chapter: flag for versification.
- Row 875 *indîci* (accent kept as printed): want Claude's call.
- Footnote *b)* placed at column 0's foot (where printed), though its word is in column 1.

## Summary

293 rows of the vote read (855–1147), 0 removed, 226 changed from the vote, 4 added (3 catchwords, 1 footnote);
297 rows written.

## reader-05 (`reader-05.md`)

# Reader 05: rows 1148–1443 (2 Kgs 9:35 *peliendum iuerunt* – 12:9 *perforato eius oper-*), leaves 441–443

Every row read on the whole page images (`1738-page-0441/0442/0443.jpg`), each column zoomed in five bands at 1.5×,
and at 2–4× for the gutter strips, doubtful stops, the blot in *fiscellis* and the catchwords. The vote's
leaf/column/line labels match the pages line for line. 1750 (`sources/archive/1750/text.txt` lines ~52540–52990)
used only as a check on wording and on margin numbers where 1738's are lost in the gutter.

## Leaves and what is on them

- **441** (p. 369, *Cap. 10.*): running head (vote rows 1148–1149, removed); col. 0 rows 1150–1160 (9:35 *peliendum
  iuerunt* – 9:37 end), rule, *CAPVT X.* and italic summary (not in the vote's rows), `\c 10` (1161), rows 1162–1195
  (10:1 *QVum* – 10:7 *filios regios, eosque iugularunt,*); col. 1 rows 1196–1246 (10:7 *homines septuaginta* – 10:19
  *Qua-*). Foot: signature *A a* and catchword *pro-* → added `+ 441 1 900 % A a pro-`.
- **442** (p. 370, *Cap. 10. 11.*): running head not in the vote's rows; col. 0 rows 1247–1297 (10:19 *propter* –
  10:30 *sententia tra-*); col. 1 rows 1298–1321 (10:30 *ctasset* – 10:36 end), rule, *CAPVT XI.* and italic summary
  (not in the rows), `\c 11` (1322), rows 1323–1343 (11:1 *CEterum* – 11:5 *aderit sabbato, et*). Foot: catchword
  *re-*, no signature → added `+ 442 1 900 % re-`.
- **443** (p. 371, *Cap. 11. 12.*): running head (vote rows 1344–1345, removed); col. 0 rows 1346–1396 (11:5 *regiæ
  custodiam aget* – 11:18 *et imagines*); col. 1 rows 1397–1408 (11:18 *probe perfringunt* – 11:20 end), rule, *CAPVT
  XII.* and italic summary (not in the rows), `\c 12` (1409), rows 1410–1443 (12:1 *AGebat* – 12:9 *perforato eius
  oper-*). Foot: signature *A a 2* and catchword *culo,* → added `+ 443 1 900 % A a 2 culo,` (the stop after *culo* sits
  at the image's lower edge: comma or full stop; read as a comma, the sense *operculo, foramen*).

`\c 10` (1161), `\c 11` (1322) and `\c 12` (1409) stand where the page's *CAPVT X.*, *XI.* and *XII.* stand: kept.

## Verse numbers

Margins: 441 col. 0 is in the gutter and its numbers are **lost** (only fragments of 36 *5*, 37 *7* and 10:7 *7*);
441 col. 1 clear; 442 col. 0 clear (left margin); 442 col. 1 in the gutter, cut to the tens digit *3* (31–36) and
11:1–5 clear; 443 col. 0 in the gutter, lost or cut (fragments of 10 *1(*, 11 *1.*, 12, 13 *3*, 14 *4*, 15 *5*, 16
*6*, 17 *7*, 18 *8*); 443 col. 1 clear. Where lost, placed by sequence, sense, the wide space before the verse and
1750's margins (which agree wherever both are legible). The vote's numbers were all wrong (off by up to eleven) and
all were placed again.

- **Ch. 9 (end)**: **36** *Quod postquam* (1152), **37** *Iacuit* (1157). Same as KJV.
- **Ch. 10** (36 verses, as KJV, but divided differently inside): **1** *QVum* (1162), **2** *simulac* (1167, after
  *verba:* and the wide space), **3** *dispicite* (1171), **4** *Illi* (1175, last word), **5** *miseruntque* (1179),
  **6** *Ad hæc* (1186), **7** *Igitur* (1193; fragment *7*), **8** *Ad quem* (1198), **9** *Po-/stridie* (1202), **10**
  *Iamiam* (1208), **11** *Tum Iehus* (1213, line start), **12** *Atque* (1219, indented), **13** *Quumque* (1222),
  **14** *iussit* (1225), **15** *Illinc* (1230, indented), **16** *Atque illum* (1235), **17** *Illo in currum* (1239,
  line start), **18** *Deinde* (1243), **19** *Qua-/propter* (1246), **20** *Hæc autem* (1253), **21** *Iussitque*
  (1255), **22** *Qui postquam* (1259), **23** *iisque prolatis* (1264), **24** *Atque illis* (1270), **25** *Atque vbi*
  (1276), **26** *Deinde in oppidum* (1282), **27** *tum ipsius* (1285, line start), **28** *Ita exterminauit* (1288),
  **29** *vide-/licet* (1292; see below), **30** *Tum Ioua* (1294), **31** *Sed non* (1300), **32** *Per ea* (1305), **33**
  *et* (1309, last word; fragment *3*), **34** *qua Galaaditis* (1311, after the wide space), **35** *De re-/liquis*
  (1313), **36** *Regnauit* (1319).
  Against the KJV: 1738 17 begins *Illo in currum euecto* (KJV 16's end "So they made him ride in his chariot"); 19 =
  KJV 19a, **20 = KJV 19b** (*Hæc autem callide* "But Jehu did it in subtilty"), 21 = KJV 20–21a, 22 = KJV 21b–22, 23–25
  = KJV 23–25 (25 to *triumuiri*), **26** *Deinde in oppidum templi Baalis profecti* = KJV 25's end ("and went to the
  city of the house of Baal") + 26, 27 = 27; **28 = KJV 28 + 29a** (*quamquam … non abstinuit*), **29 = KJV 29b**
  (*videlicet ab aureis vitulis*); 30–31 = 30–31; 32 = KJV 32 + 33a (*a Iordane … Galaaditarum*), **33** = KJV 33b
  (*et Gadinorum … Manassensium*), **34** = KJV 33c (*qua Galaaditis … patent*), **35 = KJV 34–35** (no number at
  *Ie-/hu vita defuncto*), 36 = 36. 1750's margins agree (its 28, 29 and 31 legible on the same lines).
- **Ch. 11: 1738 numbers 20 verses, KJV 21** (KJV 11:21 "Seven years old was Jehoash" is 1738's 12:1 *AGebat Ioas
  annum septimum*, as in the Hebrew's 12:1). **1** *CEterum* (1323), **2** *Sed Io-/saba* (1326), **3** *eumque ex*
  (1331), **4** *Anno se-/ptimo* (1335), **5** *eisque regis* (1340, after *paciscitur:* and the wide space), **6**
  *Altera* (1346), **7** *Duæ autem* (1350, line start), **8** *Atque ita* (1353), **9** *Hæc* (1357), **10** *Pontifex*
  (1363, line start), **11** *stan-/tibusque* (1365), **12** *filium regis* (1369), **13** *Athalia* (1373), **14** *et
  regem* (1375), **15** *At Ioiada* (1382), **16** *Nolebat* (1386, after *trucident.* and the wide space; fragment *6*
  beside this line), **17** *Et Ioiada* (1391, line start), **18** *Deinde totius* (1394), **19** *Pontifex Iouæ
  templo* (1399), **20** *atque ita otium* (1406). 6–9 have no visible fragment: placed by sense and 1750 (6 *Altera*,
  7 *Duæ*, 8 *agent. Atque*, 9 *stipabitis. Hæc*, all on the same lines in 1750). Against the KJV: 5 = KJV 4b–5 (*eisque
  regis filium ostendit* "and shewed them the king's son"), 6–14 = 6–14, 15 = KJV 15a, 16 = KJV 15b–16, 17–18 = 17–18,
  19 = KJV 18b–20a, 20 = KJV 20b.
- **Ch. 12** (to v. 9): **1** *AGebat* (1410) = KJV 11:21 + 12:1, **2** *Is Ioas* (1415), **3** *tam-/etsi* (1417),
  **4** *Iussit autem* (1420), **5** *sumerent a* (1427), **6** *Sed anno* (1430), **7** *vocauit* (1433), **8** *Sed quum*
  (1439), **9** *cepit Ioiada* (1442). From 2 on, as KJV.

**10:29 placed at *vide-/licet***: the margin *29* stands beside 1292 *strinxerat, non abstinuit, vide-*, two lines
below *quam-/quam* (where KJV 29 "Howbeit" begins), and the line has a wide space after *abstinuit,* before *vide-*,
the printer's usual verse break; 1750 also has its 29 on this line. So 1738's 29 is *videlicet ab aureis vitulis, qui
Bethele et Dane erant*, against the KJV's division. Please confirm (alternative: *quam-/quam*, row 1288).

## Letters lost in the gutter

- **441 col. 0**, rows 1176–1195: the first letter(s) of each line cut by the fold, all supplied by the sense and 1750
  and written whole: 1176 *[v]ero*, 1177 *[q]uippe*, 1178 *[d]em*, 1179 *[i]psi*, 1180 *[p]ræfectus*, 1181 *[n]us*,
  1182 *[a]d*, 1183 *[t]estate*, 1184 *[r]os*, 1185 *[c]reaturos*, 1186 *[A]d* (part of A), 1187 *[p]sit*, 1188
  *[e]stis*, 1189 *[i]storum*, 1190 *[p]ita*, 1191 *[I]ezrael*, 1192 *[t]a*, 1193 *[b]us*, 1194 *[a]d*, 1195
  *[fi]lios*.
- **443 col. 0**, rows 1359–1396: one to three letters lost at each line's start: 1359 *[f]aciunt*, 1360 *[s]uis*,
  1361 *[b]us*, 1362 *[s]abbato*, 1363 *[P]ontifex*, 1364 *[r]etrasque*, 1365 *[t]emplo*, 1366 *[t]ibusque*, 1367
  *[p]li*, 1368 *[t]emplum*, 1369 *[v]ndique*, 1370 *[e]ducit*, 1371 *[im]ponit*, 1372 *[v]ngunt*, 1373 *[g]em*, 1374
  *[cu]rsus*, 1375 *[Io]uæ*, 1376 *[co]nspicata*, 1377 *[e]rat*, 1378 *[tu]bas*, 1379 *[ta]les*, 1380 *[ve]stimenta*,
  1381 *[ti]onem*, 1382 *[cl]amat*, 1383 *[ri]onibus*, 1384 *[ra]t*, 1385 *[ed]ucant*, 1386 *[ri]t*, 1387 *[en]im*,
  1388 *[int]erire*, 1389 *[in] viam*, 1390 *[adi]tus* (only *s est* whole), 1391 **[Et] Ioiada**, 1392 *[po]pulumque*,
  1393 *[se]nt*, 1394 *[pa]ctionem*, 1395 *[reg]ionis*, 1396 *[or]ti*.
- **1391 *Et Ioiada***: only a dark stroke (the foot of a *t*) shows before *Ioiada*; the line starts at the same x as
  its neighbours, which have lost two or three letters, so a word stood there; 1750 reads *Et Ioiada tum*; KJV "And
  Jehoiada made a covenant". Written *Et Ioiada*. **Please check** on the page (or another 1738 copy).
- The vote had dropped *Iouæ* at 1365 (*emplo erant tradidit*): the page has *templo Iouæ erant,tradidit:*.

## Misprints and odd forms kept as printed

- 1150 *iuerunt* (= iverunt). 1442 *cepit* (for *cœpit*; 1305 has *cœpit*). 1356 *moriatur*: the *i* is a damaged
  sort (dot printed, stem not), read *moriatur*.
- Lower case as printed: 1156, 1159 *iezraelensi*; 1165 *iezraelen-/ses*; 1257 *israeliticis*; 1347 *suriam* (1750
  *Suriam*); 1167 *simulac* after the colon.
- 1220 *Iudææ* (genitive, two æ). 1349 *Messæ*. 1431 *Ioæ*. 1428 *diœcesi*, 1437 *diœcesibus*. 1232 *es ne*, 1178
  *ne dum* two words.
- 1410 *AGebat*: drop capital A; the *G* after it looks italic (zoomed). Written *AGebat*.
- 1197 *fiscellis*: an ink blot over *ce* (zoomed 4×; the OCR read an asterisk); no asterisk, no note.
- Commas set without a following space, kept: 1221 *consanguineos,interrogat,qui*, 1230 *digressus,incidit*, 1245
  *seruiuisse,Iehum*, 1312 *Aroere,apud*, 1365 *erant,tradidit*, 1388 *Illi,iniectis manibus,eam*; and two with the
  space before instead of after (space dropped): 1279 *gressi ,illos* → *gressi,illos*, 1379 *lætantes ,tubisque* →
  *lætantes,tubisque*.
- Spaces before punctuation dropped throughout (*Samariæ :*, *habetis ;*, *creaturos :*, *obeditis ;*, *interfecit ?*,
  *sint ?*, *te ?*, *edici :*, *iungerentur :*, *promeret ;*, *Baalem :*, *viueret :*, *aduocat :*, *sunt :*, *diœcesi
  ,*, *staurassent :*, *resarcire :*, etc.).
- Stops checked at 3×: 1249 *desit;* (semicolon; 1750 *desit:*), 1238 *iussit.*, 1171 *habetis;*, 1188 *obeditis;*,
  1375 *venit;*, 1264 *promeret;*.
- 1394: a brown stain between *fecit.* and *Deinde* (the OCR read *&*): not a mark.
- No accents over letters on these leaves.

## Paragraph indents and drop capitals

Indented lines: rows **1219** (*Atque in itinere*, 10:12) and **1230** (*Illinc digressus*, 10:15), both in 441 col. 1.
No other indent on 441, 442, or 443 col. 1; 443 col. 0's left edge is in the gutter, so an indent there cannot be
seen (none expected: its line starts align with the cut). Drop capitals: 1162 *QVum* (Q over three lines, *V* in
capitals), 1323 *CEterum* (C over three lines, *E* capital), 1410 *AGebat* (A over three lines).

## Footnotes

None on these leaves.

## G./L./H. marks and asterisks

None.

## Rows lost, added, removed

- Removed (4): 1148–1149 (441's running head *REGVM LIBER IIII.* / *Cap. 10.*), 1344–1345 (443's running head
  *REGVM LIBER IIII.* / *Cap. 11. 12.*).
- Added (3): `+ 441 1 900 % A a pro-`, `+ 442 1 900 % re-`, `+ 443 1 900 % A a 2 culo,`.
- No text line lost by the OCR. Rows heavily rebuilt: 1162–1164 (drop capital), 1176–1195 and 1346–1396 (gutter),
  1285–1297, 1305–1321, 1323–1343, 1365, 1410.

## Wording doubts (1738 against 1750)

None beyond spelling, capitals, punctuation and OCR noise. Checked: 9:35 *iuerunt*; 10:1 *iezraelenses senatores et
Achabi educatores* (both); 10:5 *præfectus domus et prætor vrbanus*; 10:19 *desit;* (1750 *desit:*); 10:25 *vitam vita
perdendam*; 11:6 *suriam* (1750 *Suriam*); 11:10 *templo Iouæ erant*; 11:17 *Et Ioiada* (1738 in the gutter, see
above); 12:9 *cepit*. Nothing looks misprinted against the sense.

## Omission check (against BSB/KJV)

Each verse 9:35b–12:9a read against the KJV/BSB. Castellio condenses (10:1 "to the rulers of Jezreel, to the elders,
and to them that brought up Ahab's children" → *ad principes iezraelenses senatores et Achabi educatores*; 10:25 "cast
them out" → *prosternuntque*; 11:12 "the testimony" → *oraculum*; 12:2 "all his days wherein Jehoiada the priest
instructed him" → *tamdiu … quamdiu doctorem Ioiadam … habuit*), his rendering, not a loss. No clause the page has is
missing from my reading.

## Uncertain readings and how settled

- 10:29 at *vide-/licet* (margin and wide space; 1750 same line) rather than *quam-/quam*: want Claude's call.
- 11:17 *Et* restored in the gutter from the fragment, the line width and 1750: want a check.
- 11:16 at *Nolebat* (wide space; margin fragment *6* on that line).
- Ch. 10's internal division differs from KJV (20 = KJV 19b, 26, 28/29, 33/34, 35 = KJV 34–35); ch. 11 has 20 verses
  (KJV 21, its 21 = 1738 12:1): flag for versification.
- Catchword *culo,* (stop at the image's edge).

## Summary

296 rows of the vote in range (1148–1443): 4 removed, 292 kept, 234 changed from the vote, 3 added (catchword and
signature rows); 295 rows written.

## reader-06 (`reader-06.md`)

# Reader 06: rows 1444–1736 (2 Kgs 12:9 *culo, apud aram* – 15:8 *Anno duodequadrage-*), leaves 444–446

Every row read on the whole page images (`1738-page-0444/0445/0446.jpg`), each column zoomed in four bands at 1.5×,
the gutter strips and outer margins separately, and doubtful letters and stops at 3–4× (*eouites*, *cepi.*,
*ternecionem*, *cecidisses*, *Iouæ paruit*). The vote's leaf/column/line labels match the pages line for line. 1750
(`sources/archive/1750/text.txt` lines ~53020–53420) used only as a check on wording and, where 1738's margin is lost,
on verse numbers (its margins are mostly lost in its OCR too for ch. 13).

## Leaves and what is on them

- **444** (p. 372, verso, *Cap. 12. 13.*): running head not in the rows of col. 0; col. 0 rows 1444–1494 (12:9 *culo,
  apud aram* – 12:20 *occisus est apud Mel-*); col. 1 running head (vote rows 1495–1496, removed), rows 1497–1500
  (12:20 *lonem domum* – 12:21 end), rule, *CAPVT XIII.* and italic summary (not in the rows), `\c 13` (1501), rows
  1502–1542 (13:1 *ANno* – 13:11 *inque eis viuendo.*). Foot: catchword *De*, no signature → added `+ 444 1 900 % De`.
- **445** (p. 373, recto, *Cap. 13. 14.*): running head not in the rows; col. 0 rows 1543–1593 (13:12 *De ceteris* –
  13:25 *Ioas Ioachazi filius oppida rursum*); col. 1 rows 1594–1597 (13:25 *eripuit* – end), rule, *CAPVT XIIII.* and
  italic summary (not in the rows), `\c 14` (1598), rows 1599–1638 (14:1 *ANno* – 14:11 *profectus est*). Foot:
  signature *A a 3* and catchword *Ioas*: the vote has them as text row 1639 (*A a 3 Ioas*) → kept as `1639 … % A a 3
  Ioas`.
- **446** (p. 374, verso, *Cap. 14. 15.*): running head not in the rows; col. 0 rows 1640–1690 (14:11 *Ioas
  Israelitarum rex* – 14:25 *vt habebatur in*); col. 1 rows 1691–1711 (14:25 *Iouæ Dei* – 14:29 end), rule, *CAPVT
  XV.*, italic summary (its last line is vote row 1713 *Atfyriw. In inJtos Syri.* = *Assyriis. In Iudæos Syri.*,
  removed), `\c 15` (1712), rows 1714–1736 (15:1 *ANno* – 15:8 *Anno duodequadrage-*). Foot: catchword *simo*, no
  signature → added `+ 446 1 900 % simo`.

`\c 13` (1501), `\c 14` (1598) and `\c 15` (1712) stand where the page's *CAPVT XIII.*, *XIIII.* and *XV.* stand: kept.

## Verse numbers

Margins: 444 col. 0 clear (left, outer); 444 col. 1 in the gutter (right), **lost** except *1* at 13:1, a cut *2* at
1498 and small fragments at 1507, 1511, 1513, 1517, 1520, 1525, 1533 (the marks the vote read as *;* *,* *'*); 445
col. 0 in the gutter (left), **all lost**; 445 col. 1 clear (right); 446 col. 0 clear (left); 446 col. 1 right margin
cut to the tens digit *2* (26–29), ch. 15 clear. The vote's numbers were nearly all wrong (ch. 12 off by three; ch. 13
missing most; ch. 14 off by up to five) and all were placed again.

- **Ch. 12 (from 9)**: **10** *Ac postquam* (1449), **11** *inque* (1453, after *numerabant:* and the wide space),
  **12** *in cæmentarios* (1459, line start), **13** *Neque ex illa* (1464), **14** *Sed ea* (1469), **15** *Neque
  illis* (1471), **16** *verum* (1475, line start), **17** *Quum au-/tem* (1477), **18** *cepit* (1480, after the
  wide space), **19** *De reliquis* (1489), **20** *Hic Ioas* (1492, line start), **21** *Eoque* (1498; margin cut to
  *2*). 21 verses, as KJV; 1738 20 = KJV 20 + 21a (*Hic Ioas a suis Iozabaro … occisus est … ad Sillam*), 21 = KJV 21b
  (*Eoque … sepulto, successit … Amasias*). 10–19 as KJV.
- **Ch. 13** (25 verses, as KJV; numbers 2–24 lost in the gutters, placed by sense, the gutter fragments on 444 and
  the wide spaces the printer leaves at a verse start): **1** *ANno* (1502), **2** *Hic quum* (1507), **3** *iratus*
  (1511), **4** *Sed* (1513, last word), **5** *et Israelitas, defen-/sore dato* (1517), **6** *Neque* (1520, last
  word), **7** *quum quidem Ioachazo* (1525), **8** *De reli-/quis* (1530), **9** *Io-/achazo* (1533, fragment),
  **10** *anno tri-/cesimo* (1536, after a wide space; KJV 10 "In the thirty and seventh year"), **11** *Offendit*
  (1539), **12** *De ceteris* (1543, line start), **13** *Ioa vita* (1547), **14** *Quum labora-/ret* (1550), **15**
  *Tum Elisæus* (1555), **16** *Quumque ille arcum* (1557, line start), **17** *et,eum orien-/talem* (1561, after the
  wide space), **18** *Itemque re-/gem* (1567), **19** *Qua re* (1571), **20** *Mortuo sepultoque* (1575), **21**
  *quidam, qui ho-/minem* (1578, wide space), **22** *Hazael autem* (1583), **23** *quamquam* (1585, wide space), **24**
  *Mortuo Hazaele* (1590), **25** *Ioas Ioachazi filius* (1593, line start).
  - **13:25**: the only *25* on the page stands in 445 col. 1's right margin beside **1595** *quæ ille a Ioachazo patre
    suo armis*, two lines into the column; the verse (KJV 25 "And Jehoash the son of Jehoahaz took again") begins at
    1593 *Ioas Ioachazi filius* at the foot of col. 0, whose margin is lost. Placed at 1593 by sense; *quæ* (after a
    comma, inside the relative clause) cannot start a verse. **Please check.**
  - **13:16** (line start *Quumque ille arcum*, KJV 15b "And he took unto him bow and arrows") and **13:17** (*et,eum
    orientalem*, KJV 17 "Open the window eastward") placed by sense and spacing; no margin survives. Alternatives:
    16 at *iussit* (1558), 17 at *Quam postquam* (1559).
- **Ch. 14** (29 verses, all as KJV): **1** *ANno* (1599), **2** *Regnauit Hiero-* (1603), **3** *Hic* (1605), **4**
  *non sublatis* (1609, after *est,* and the wide space), **5** *Is, postquam* (1611), **6** *neque* (1614), **7**
  *Occidit et* (1620), **8** *Tum,* (1624), **9** *Cui Ioas* (1628), **10** *Tu quoni-* (1633), **11** *His quum* (1637),
  **12** *victique* (1643, after *sus est:* and the wide space), **13** *Amasiam* (1645), **14** *ablato-/que* (1651),
  **15** *De ceteris* (1656, line start), **16** *Ioæ vita* (1660), **17** *Vixit au-/tem* (1663), **18** *De reliquis*
  (1667), **19** *Aduersus* (1669), **20** *sublatusque* (1673, line start), **21** *Eius deinde* (1675), **22** *Is,
  rege* (1678), **23** *Anno decimo-/quinto* (1680), **24** *Is Iouam* (1685, line start), **25** *Recuperauit* (1688),
  **26** *Respexit* (1694; cut *2*), **27** *Quumque nul-/lus* (1697; cut *2*), **28** *De reliquis* (1702; cut *2*),
  **29** *Postquam* (1708; cut *2*). 1750's margins agree where its OCR has them (10, 11, …).
- **Ch. 15** (to 8, as KJV): **1** *ANno* (1714), **2** *Regnauit Hie-* (1718), **3** *Is Iouæ* (1721), **4** *non
  sublatis* (1723), **5** *Hic rex* (1726, line start), **6** *De re-/liquis* (1730), **7** *Azaria vita* (1733), **8**
  *Anno duodequadrage-/simo* (1736).

So 1738 runs with the KJV through 12:10–15:8 except the internal division at 12:20–21.

## Letters lost in the gutter

- **445 col. 0** (rows 1554–1593): about one letter lost at each line's start, written whole from the sense and
  1750: 1554 *[o]* (part of an *o*, x-height, so lower case *o pater*), 1556 *[c]epi*, 1557 *[Q]uumque*, 1558
  *[p]isset*, 1559 *[m]oueret*, 1560 *[m]ouit*, 1561 *[m]anibus*, 1562 *[t]alem*, 1563 *[q]ue*, 1564 *[c]ulato*, 1565
  *[I]ouæ*, 1566 *[s]agitta*, 1567 *[t]ernecionem*, 1568 *[g]em*, 1569 *[Q]uumque*, 1570 *[r]am*, 1571 *[d]esinit*, 1572
  *[u]inus*, 1573 *[p]ulsasses*, 1574 *[c]ecidisses* (see doubts), 1575 *[e]s*, 1576 *[q]uum*, 1577 *[a]bitæ*, 1578
  *[n]em*, 1579 *[m]inem*, 1580 *[e]um*, 1581 *[r]unt*, 1582 *[g]it*, 1583 *[s]us*, 1584 *[I]sraelitas*, 1585
  *[c]rudeliter*, 1586 *[e]orum*, 1587 *[o]b*, 1588 *[I]saaco*, 1589 *[q]ue*, 1590 *[t]enus*, 1591 *[H]azaele*, 1592
  *[e]ius*, 1593 *[I]oas*. Rows 1543–1553 whole.
- **1572 *uinus***: *di-/[u]inus*: only the right stem of the first letter shows; written *u* (word-internal after the
  hyphen, 1738's habit); 1750 *vinus*.
- **1567 *ternecionem***: the vote (and 1750's OCR) read *térnecionem*; on the page the *t* is in the gutter and the
  *e* after it has **no accent** (4× zoom; the only dot is the *i*'s). Written *ternecionem*.
- **1584 *Israelitas***: the vote's *Israélitas* has no accent on the page (3× zoom): none written.

## Misprints and odd forms kept as printed

- **1555 *eouites*** (for *equites*): the letter is an *o* with no tail at 3× (a broken *q* or a wrong sort); 1750
  *equites*. Kept as seen; **please check**.
- **1556 *cepi.,*** (*præ-/cepi., vt*): after *cepi* a low dot, then a space and a comma; probably *cepit,* with the *t*
  not printed (1750 *cepit,*). Written *cepi.,* (space before the comma dropped); **please check**.
- 1479/1480 *cepisset*, *cepit* (no œ, as in reader 05's 12:9 *cepit*); 1682 *cœpit*.
- Lower case as printed: 1596–1597 *israe-/liticas*, 1699 *israeliticum*, 1554 *o pater*.
- Capitals: 1605 *Hierosolymitana* (vote *hierosolymitana*).
- 1540 *Ieroboami,Nabati*: a comma after *Ieroboami*, no space (1750 none); 1547 *defuncto,sedit*; 1561 *et,eum*;
  1645–1646 *Amasiam,Ioæ filium,Iudææ / regem,Ioachazi*; 1686 *sceleribus,qui-*: commas without a following space,
  kept.
- 1623 *Iectheel* (vote *Ieftheel*; 1750 *Iectheel*). 1693 *Amittæi*. 1461 *sarciendas*. 1478 *Getham*. 1492
  *Semaæ*. 1641 *Amasia* is followed by a short raised stroke (a space quad inked): not a mark, not written.
  1680 *restituit.* with a stray short stroke after the stop: not written.
- 1606 *Iouæ*: a faint thin oblique stroke above the *o* (3×), much fainter than the type; read as a speck, not an
  accent. **Please check** (would be *Ióuæ*).
- 1585 *quamquam*: an ink blot over the *q*; lower case.
- 1513 *Sed* with no comma: the mark after it (vote *Sed,*) is a fragment of the gutter margin number, like those at
  1507 *et*, 1511 *eos*, 1520 *Neque*, 1525 *Ioachazo*.
- Spaces before punctuation dropped throughout (*culo ,*, *pecuniæ :*, *relatam ,*, *agentibus :*, *est :*,
  *Hierosolymis ;*, *regnante :*, etc.).
- Stops checked at 3×: 1525 *lucus;* (semicolon), 1560 *mouit;*, 1570 *ferit;*, 1671 *profugisset;*, 1580/1581
  *abiece-/runt.*
- No accents over letters on these leaves (see *ternecionem*, *Israelitas*, *Iouæ* above).

## Paragraph indents and drop capitals

No indented line on 444, 445 or 446 (445 col. 0's left edge is in the gutter; its line starts are cut evenly, so
none can be seen). Drop capitals: 1502 *ANno* (13:1), 1599 *ANno* (14:1), 1714 *ANno* (15:1), each an A over three
lines with *N* in capitals.

## Footnotes

None on these leaves.

## G./L./H. marks and asterisks

None.

## Rows lost, added, removed

- Removed (3): 1495–1496 (444 col. 1's running head *REGVM LIBER IIII.* / *Cap. 12.13.*), 1713 (the last line of
  ch. 15's italic summary, *Assyriis. In Iudæos Syri.*).
- Added (2): `+ 444 1 900 % De`, `+ 446 1 900 % simo`. Row 1639 (*A a 3 Ioas*, signature and catchword) kept as a
  `%` row.
- Words the vote lost: 1539 *Offendit* (*cim. autem Iouam* → *cim. Offendit autem Iouam*). No whole line lost.
- Rows heavily rebuilt: 1451–1452, 1493–1494, 1497, 1500, 1518, 1543–1597 (gutter and noise), 1599, 1645, 1663,
  1685–1686, 1713.

## Wording doubts (1738 against 1750)

- **13:19 1574 *cecidisses*** (1738, only *ecidisses* visible, one letter lost as on the lines around it) against
  1750 *cæcidisses* (OCR *caecidiffes*). The sense wants *cæcidisses* (from *cædo*, "you would have smitten"; cf. 1567
  *cædes*); *cecidisses* (from *cado*) would be a misprint. The visible *e* is whole with no ligature to its left, so
  read *cecidisses*; but an *æ* whose *a* fell in the gutter cannot be ruled out. **Please check** on another 1738
  copy.
- 13:14 *eouites* (1750 *equites*) and 13:15 *cepi.,* (1750 *cepit,*): see misprints.
- Otherwise none beyond spelling, punctuation and OCR noise. Checked: 12:11 *quæ in templo Iouæ inueniebatur*; 12:20
  *Iozabaro Semaæ filio, et Iozabado Someris filio* (both); 13:7 *quasi in trituræ puluerem*; 13:17 *ista est (inquit
  ille) victrix Iouæ sagitta*; 14:7 *Iectheel*; 14:10 *gloriare domi tuæ manens* (1750 same); 14:20 *sublatusque in
  equo* (1750 same); 14:25 *Gethephrensem*; 15:1 *annum tum agens decimum sextum*.

## Omission check (against BSB/KJV)

Each verse 12:9b–15:8a read against the KJV. Castellio condenses and subordinates (13:2–5 run as one period; 13:6 "the
grove" → *lucus*; 13:15–18 the bow and arrows; 14:9 "a wild beast" → *fera*; 14:26 "shut up … left" → *neque abditum
neque abiectum*; 15:5 "the king's son was over the house, judging" → *Iothamo … domum procurante, populoque ius
dicente*), his rendering, not a loss. 13:14 "wept over his face" → *apud eum flens* (no "face"); 13:23 "and was
gracious unto them, and had compassion" → *eorum misertus Ioua, eos respexit*. No clause the page has is missing
from my reading (1539 *Offendit* restored).

## Uncertain readings and how settled

- 13:25 placed at 1593 *Ioas* against the margin *25* beside 1595 (want Claude's call).
- 13:2–24 placed without margins (gutter): by sense, wide spaces and fragments; 13:16 and 13:17 the least sure.
- 13:19 *cecidisses* / *cæcidisses*; 13:14 *eouites*; 13:15 *cepi.,*; 14:3 *Iouæ* faint stroke.
- 12:21 at *Eoque* (margin cut to *2*).

## Summary

293 rows of the vote in range (1444–1736): 3 removed, 290 kept, 204 changed from the vote, 2 added (catchword rows);
292 rows written.

## reader-07 (`reader-07.md`)

# Reader 07: rows 1737–2033 (2 Kgs 15:8 *simo Azariæ* – 17:23 *transferen-/dos*), leaves 447–449

Every row read on the whole page images (`1738-page-0447/0448/0449.jpg`), each column zoomed in four bands at 1.4×,
doubtful letters and marks at 3–5× (*Iabis filius :-eoque*, *basium*, *regi-*, *offendit*, *filium*, *patria*,
*addicti*). The vote's leaf/column/line labels match the pages line for line. 1750 (`sources/archive/1750/text.txt`
lines ~53490–53900) used only as a check on wording.

## Leaves and what is on them

- **447** (p. 375, recto, *Cap. 15.*): running head not in the rows; col. 0 rows 1737–1787 (15:8 *simo Azariæ* – 15:20
  *Ita reuersus Assyriæ*); col. 1 rows 1788–1838 (15:20 *rex, in ea regione* – 15:34 *exemplo ad Io-*). Foot: signature
  *Aa 4* and catchword *uæ* → added `+ 447 1 900 % A a 4 uæ`.
- **448** (p. 376, verso, *Cap. 16.*): running head not in the rows; col. 0 rows 1839–1849 (15:34 *uæ voluntatem* –
  15:37 end), rule, *CAPVT XVI.* and italic summary (five lines; the vote kept its last three as rows 1851–1853,
  *Ad Syriæ regem obsessus Achazus sup-/plex cum donis, eiusdem mors, heres E-/zechias.*, removed), `\c 16` (1850),
  rows 1854–1885 (16:1 *IOthamo* – 16:7 *et Israelitarum*); col. 1 rows 1886–1936 (16:7 *regis iniuria* – 16:19
  *in annalibus regum*). Foot: catchword *Iu-*, no signature → added `+ 448 1 900 % Iu-`.
- **449** (p. 377, recto, *Cap. 17.*): running head not in the rows; col. 0 rows 1937–1940 (16:19 *Iudææ.* – 16:20
  end), rule, *CAPVT XVII.* and italic summary (not in the rows), `\c 17` (1941), rows 1942–1981 (17:1 *ANno* – 17:11
  *eorum caus-*); col. 1 rows 1982–2032 (17:11 *sa exactarum* – 17:19 *transferen-*). Foot: signature *Aa 5* and
  catchword *dos*: the vote has them as row 2033 (*A a 5 dos*) → kept as `2033 … % A a 5 dos`.

`\c 16` (1850) and `\c 17` (1941) stand where *CAPVT XVI.* and *XVII.* stand: kept. (No chapter is lost on these
leaves; the missing `\c 23` is not in my range.)

## Verse numbers

Margins all legible: 447 col. 0 left, 447 col. 1 right (34 cut to *3*), 448 col. 0 left, 448 col. 1 right in the
gutter (10, 12, 13 cut to *1*, *1:*, *1:*; read by sequence), 449 col. 0 left, 449 col. 1 right. The vote's numbers
were wrong throughout ch. 15 (off by six to eight) and one ahead in ch. 16; all placed again from the margins.

- **Ch. 15 (from 9)**: **9** *In hunc* (1740), **10** *coniurationem* (1745, after *cedentem,* and the wide space),
  **11** *De reliquis* (1748), **12** *Hoc est* (1750), **13** *Sellumus* (1754), **14** *Manahemus* (1758), **15** *De
  reliquis Sellumi* (1761), **16** *Deinde* (1764), **17** *Anno tricesimo* (1770), **18** *Is contra* (1774), **19**
  *Quumque* (1778), **20** *quod quidem* (1783, line start), **21** *De reliquis omnibus* (1789), **22** *Manahemo*
  (1792), **23** *Re-/gnauit* (1795), **24** *Eum* (1796), **25** *Phaca Ro-* (1800), **26** *De ceteris* (1806), **27**
  *Anno quinquagesimo* (1809), **28** *Is Iouam* (1813), **29** *Huius* (1816), **30** *Phacam* (1824), **31** *De
  reliquis* (1828), **32** *Anno secundo* (1831), **33** *Regnauit Hie-* (1835), **34** *Is Oziæ* (1838; margin cut to
  *3*), **35** *non sub-* (1839, after *vixit,* and the wide space), **36** *De reliquis* (1843), **37** *Per ea* (1846).
  **1738's ch. 15 has 37 verses, the KJV's 38.** Differences from the KJV:
  - 15:23: 1738 begins at *Regnauit Samariæ biennium*; *anno Azariæ … quinquagesimo* (KJV 23a) stays in 1738 22.
  - 15:33: 1738 begins at *Regnauit Hierosolymis*; *annos tum natus viginti quinque* (KJV 33a) stays in 1738 32.
  - KJV 15:38 (*Jotham slept with his fathers*) is 1738 **16:1** (*IOthamo vita defuncto … sepulto,*).
- **Ch. 16** (20 verses in both): **1** *IOthamo* (1854; = KJV 15:38), **2** *Iudææ regnum* (1857; = KJV 16:1 + 2a,
  through *annos sexdecim*), **3** *Is tan-/tum* (1861; = KJV 2b–3), **4** *sacrificaretque* (1869), **5** *Tum Razin*
  (1872), **6** *Eo tem-/pore* (1876), **7** *Misit* (1881), **8** *eidemque* (1887), **9** *His* (1890), **10** *Achazus
  autem* (1894; cut *1*), **11** *isque* (1899), **12** *Rex Damasco* (1902; cut *1:*), **13** *solidamque* (1904; cut
  *1:*), **14** *Altare* (1908), **15** *Vriæque* (1912), **16** *His omnibus* (1924), **17** *Truncauit* (1926), **18**
  *Tapetem* (1931), **19** *De* (1934), **20** *Achazo* (1937). From 4 on as KJV. 16:13 at *solidamque* by sense (KJV
  13 "he burnt his burnt offering"; *ad eam rem diuinam fecit* = KJV 12 "offered thereon"), the margin beside that
  line.
- **Ch. 17 (to 19)**: **1** *ANno* (1942), **2** *Regnauit* (1945), **3** *Hunc* (1948), **4** *postea* (1951, after
  *egisset:* and the wide space), **5** *Quum enim* (1957), **6** *eaque* (1959), **7** *Et quia* (1964), **8** *et
  instituta* (1969), **9** *sacellaque* (1975), **10** *statuas* (1977), **11** *et ibi* (1980), **12** *colendo* (1984),
  **13** *quumque* (1986), **14** *sed eadem* (1995), **15** *omissisque* (2004), **16** *ob hæc* (2012), **17** *Ac
  Iudæis* (2015), **18** *Nam* (2021), **19** *eousque* (2028). Differences from the KJV:
  - 17:1–2: 1738 2 begins at *Regnauit Samariæ annos nouem* (KJV 1b).
  - 17:14: 1738 begins at *sed eadem ceruicis duritate*; *non obtemperauerant* (KJV 14a) stays in 1738 13; 1738 14
    also holds KJV 15 (*repudiatis illius institutis, atque fœdere … vetuerat*).
  - So 1738 15 = KJV 16–17 (*omissisque … addicti*), 16 = KJV 18 (*ob hæc … tribu*), 17 = KJV 19–20 (*Ac Iudæis …
    abiiceret*), 18 = KJV 21–22 (*Nam separati … non recedentes*), 19 = KJV 23 (*eousque, vt Ioua … transferendos*, to
    leaf 450). 1738 runs four behind the KJV from here.
  - **17:19 placed at *eousque*** (KJV 23 "Until the LORD removed"), the *19* stands beside line 2028 *non recedentes,
    eousque, vt*; the alternative is *vt Ioua* (the vote had it at *vt*). **Please check.**

## Letters lost in the gutter

None: all line starts and ends whole. Only the margin numbers of 448 col. 1 (10, 12, 13) and 447 col. 1 (34) are cut.

## Misprints and odd forms kept as printed

- 1746, 1754 *Iabis* (capital I; vote *labis*); 1754 *Iabis filius anno* with no comma after *filius*.
- 1746 *filius: eoque*: after the colon a faint thin hairline (4×) reaching to *eoque*, much lighter than type; not a
  hyphen or dash, not written.
- 1768 *thapsen-/sesque* lower case; 1865 *israeliticorum* lower case.
- 1775 *luntatem*: the *t* is broken (only its top shows, the vote's *lun'atem*); written whole.
- 1803 *Arie* (vote *Aue*; 1750 *Arie*). 1837 *Ierusa*. 1820–1821 *Ianoam*, *Ca-/dem*, *Hasor*. 1847 *Razinem* (1750
  *Rezinem*: a 1750 change or OCR; 1738 clearly *Razinem*). 1893 *Cirenem*. 1961 *Habore* (vote *Habere*; 1750
  *Habore*). 1948 *Salmanasar*. 1953, 1965–1966 *Aegypti*, *Aegypto* (A e, not Æ).
- Commas with no following space, kept: 1740 *hunc,contra*, 1772 *Manahemus,Gadis*, 2007 *adorabant,Baalem*.
- Tight settings written with the space: 1880 *ducta est* (*ductaeſt*), 1903 *visa ara*, 1911 *ad aræ*, 1932 *et
  aditum*, 1983 *facinora ad*, 1993 *missa ad*.
- 1878, 1952: a space inside the opening parenthesis (*( exactis*, *( quod*), dropped: *(exactis inde Iudæis)*, *(quod
  et legatos … mittebat)*.
- 1784 *potentis-/simis*: the line-end *im.* in the vote is the hyphen (*im-*).
- 1927 *basium*: an ink blot covers the letter after *basi* (3×); the shape and width fit *u*; 1750 *basium*.
- 1932 *regi-*: a tiny hollow ring above the *i* (4×), the same height as the dots; read as a damaged dot, not an
  accent. **Please check.**
- 1946 *offendit,*: a small raised mark between *t* and the comma (5×), like a risen space quad (cf. reader 06's 1641
  *Amasia*); not an asterisk (no note on the page), not written.
- 2011 *addicti*: an ink blot before the *a* (the vote's *-addicti*); not a mark, not written.
- 2015 *bu.*: underscored by an ink stroke (the vote's *JtiiU*); text *bu.*
- 2023 *filium*: the second *i*'s dot is a tilted short stroke (3×), slightly more slanted than the others; read as a
  dot, not a grave (*filìum*). **Please check.**
- 2032 *patria*: a long thin light stroke crosses the *p* and *a* from upper left (3×), a fibre or scratch, not an
  accent.
- Stops checked: 1756 *iniit:*, 1959 *obsedit;*, 1986 *vetuerat;*, 1994 *mandata;*, 2004 *rat;* (semicolons), 1887
  *defenderet:*, 1899 *pontificem:*. Spaces before punctuation dropped throughout.
- **Accents**: none printed over a letter on these leaves (the vote had none either).

## Paragraph indents and drop capitals

No indented line on 447, 448 or 449 (every column's left edge checked). Drop capitals: 1854 *IOthamo* (16:1, I over
three lines, the vote's *TOthamo* / *I maiores* / *-•-auctoris*), 1942 *ANno* (17:1, A over three lines, the vote's
*I A Nuo* / *r\ dacae* / *■*■ ■*■ res*).

## Footnotes

None on these leaves.

## G./L./H. marks and asterisks

None (1741's *ir\** and 1946's raised mark are not asterisks; see above).

## Rows lost, added, removed

- Removed (3): 1851–1853 (the last three lines of ch. 16's italic summary).
- Added (2): `+ 447 1 900 % A a 4 uæ`, `+ 448 1 900 % Iu-`. Row 2033 (*A a 5 dos*) kept as a `%` row.
- Words the vote lost: 2031 *minatus erat,* (*suos vates eosque, ex* → *suos vates minatus erat, eosque ex*); 1828
  *reliquis* (vote *reliqui*). No whole line lost.
- Vote misreadings of substance corrected: 1995 *sed eadem ceruicis* (vote *sed cadere*), 1980 *erant* (vote
  *erent*), 1931 *qui in* (*qui i*), 1925–1926 *est pon-/tifex Vrias* (vote *est t.* / *pontifex*), 2004 *Iouæ* (vote
  *Ioua*), 1849 *filium* (*ilium*), 1937 *Iudææ* (*°Iudaeae*).

## Wording doubts (1738 against 1750)

None beyond spelling, punctuation and OCR noise. Checked against 1750: 15:25 *cum Argobo,et Arie* (1750 comma tight
too); 15:34–37 (1750 same wording, *Rezinem* for *Razinem*); 16:17 *areas basium*; 16:18 *Tapetem quoque sabbati*;
17:6 *Halæque et Habore*; 17:14 *sed eadem ceruicis duritate*; 17:15–18 (1750 same wording).

## Omission check (against BSB/KJV)

Each verse 15:8b–17:23a read against the KJV. Castellio condenses: 15:12 the oracle given as *Hoc est oraculum Iouæ,
quo Iehu promiserat fore …*; 15:16 "from Tirzah" *vsque a Thersa*; 15:25 "Argob and Arieh" *cum Argobo, et Arie* and
"in the palace of the king's house" *in arce regiæ*; 16:3 "according to the abominations of the heathen" *qualia sunt
gentium flagitia*; 16:10–16 the altar paraphrased (*totius operis rationem*); 16:18 "the covert for the sabbath"
*Tapetem … sabbati*; 17:9 "did secretly those things that were not right" *res designauerant illicitas*; 17:13 "by
all the prophets, and by all the seers" *per tot vates futura præuidentes*; 17:22 "walked in all the sins" *per omnia
… flagitia grassabantur*. His rendering, not a loss. No clause the page has is missing from my reading (2031 *minatus
erat* restored).

## Uncertain readings and how settled

- 17:19 at *eousque* vs *vt* (want Claude's call).
- 1932 *regi-* ring over the i; 2023 *filium* tilted dot; 1927 *basium* blotted letter.
- 16:13 at *solidamque* (margin cut to *1:*, beside that line; sense).

## Summary

297 rows of the vote in range (1737–2033): 3 removed, 294 kept, 223 changed from the vote, 2 added (signature and
catchword rows); 296 rows written.

## reader-08 (`reader-08.md`)

# Reader 08: rows 2034–2326 (2 Kgs 17:19 *dos curauerit* – 19:15 *qui solus omnium*), leaves 450–452

Every row read on the whole page images (`1738-page-0450/0451/0452.jpg`), each column zoomed in four bands at 1.4×,
doubtful letters, marks and margin numerals at 3–5× (*Ezechiam/Ezechiani*, *aram*, *Ezechiæ:*, *ne deos,*, margin
*13*). 1750 (`sources/archive/1750/text.txt` lines ~53925–54400 and 109100–109300) used only as a check on wording.
Leaf 452 was badly voted: two lines of col. 1 (*tuere verba … / Assyriæ regis famuli …*) were fused into col. 0's
rows 2250–2251, and the vote's line labels jump there (col. 0 19 → 36; col. 1 starts at 20 and jumps 35 → 67). The
rows' leaf/column/line labels are kept as the vote gave them.

## Leaves and what is on them

- **450** (p. 378, verso, head *Cap. 17. 18.*): running head not in the rows; col. 0 rows 2034–2084 (17:19 *dos
  curauerit* – 17:34 *feriendoque cum eis*); col. 1 rows 2085–2106 (17:34 *fœdere* – 17:41 end), rule, *CAPVT XVIII.*
  and italic summary (three lines; the vote kept the last as row 2108 *#1 Rabfacit oratio superba.*, removed),
  `\c 18` (2107), rows 2109–2131 (18:1 *ANno* – 18:7 *Con-*). Foot: catchword *tra*, no signature → added
  `+ 450 1 900 % tra`.
- **451** (p. 379, recto, head *Cap. 19.*, sic: the page holds only ch. 18): the vote's rows 2132 *REGVM LIBER III!.*
  and 2133 *Cap. 19.* are the running head → removed. Col. 0 rows 2134–2183 (18:7 *tra regem* – 18:18 *apud eos hu-*),
  footnote *a)* at its foot → added `+ 451 0 900`; col. 1 rows 2184–2233 (18:18 *iusmodi* – 18:30 *vt Iouæ con-*).
  Foot: catchword *fida-*, no signature → added `+ 451 1 900 % fida-`.
- **452** (p. 380, verso, head *Cap. 18. 19.*): running head not in the rows; col. 0 rows 2234–2268 (18:30
  *fidatis* – 18:37 end), rule, *CAPVT XIX.* and italic summary (three lines; the vote kept the last two as rows
  2270–2271 *#1 Ad loimm Ezecbiiu. De Senacberibo va-* / *les. Angehi\* in Senacberibi copias,*, removed), `\c 19`
  (2269), rows 2272–2279 (19:1 *HIs* – 19:2 *qui ei ita*); col. 1 rows 2280–2326 with two added lines (19:2
  *dicerent* – 19:15 *qui solus omnium*). Foot: footnote *b)* (two lines across the page's width) → added
  `+ 452 1 902`; catchword *orbis* → added `+ 452 1 903 % orbis`. No signature.

`\c 18` (2107) and `\c 19` (2269) stand where *CAPVT XVIII.* and *XIX.* stand: kept. No `\c 23` in my leaves.

## Verse numbers

Margins: 450 col. 0 left, col. 1 right; 451 col. 0 left, col. 1 right; 452 col. 0 left, col. 1 right. All legible,
none cut. The vote's numbers were wrong throughout ch. 17 (it ran on from 16) and one ahead in ch. 18–19; all placed
again from the margins.

- **Ch. 17** (continuing reader 07's 19): **20** *Deduxit* (2036), **21** *occupataque* (2040, line start), **22**
  *Sed vt primum* (2041), **23** *Itaque* (2045), **24** *Tum rex* (2050), **25** *Ita profectus* (2055), **26** *Sed
  illi* (2059), **27** *prout* (2062), **28** *Babylonii* (2064), **29** *Hemathenses* (2066, line start; see below),
  **30** *Sephar-/uaimenses* (2067), **31** *Ita quum* (2070), **32** *fa-/ctum est* (2074), **33** *Atque ad hunc*
  (2078), **34** *feriendoque* (2084), **35** *sed tantum* (2088), **36** *ab hoc* (2091), **37** *neue deos* (2094),
  **38** *ne deos, inquam* (2097, line start), **39** *qui eos* (2099), **40** *Sed non* (2101), **41** *et Iouæ
  religionem* (2103).
  **1738's ch. 17 has 41 verses, as the KJV**, but numbered differently from KJV 15 to 40: reader 07 found 1738 four
  behind at 19 (= KJV 23). 1738 catches up by dividing verses the KJV does not: 20 = KJV 24a (*Deduxit … Israelitarum*),
  21 = KJV 24b (*occupataque … oppida*), 22 = KJV 25, 23 = 26, 24 = 27, 25 = 28, 26 = KJV 29a (*Sed illi … posuerant*),
  27 = KJV 29b (*prout quæque natio*), 28 = KJV 30a (Babylon, Cuth), 29 = KJV 30b–31a (Hamath, Avites), 30 = KJV 31b
  (Sepharvites), 31 = KJV 32, 32 = 33, 33 = 34, 34 = 35, 35 = 36, 36 = 37, 37 = 38, 38 = KJV 39a (*ne deos, inquam …
  vererentur*), 39 = KJV 39b (*qui eos esset … vindicaturus*), 40 = KJV 40, 41 = KJV 41.
  - **17:29 placed at *Hemathenses*** (the line start, beside the numeral); the alternative is *Auani* (KJV 31 begins
    with the Avites). No stop or wide space before *Auani* (only a comma), and 21 likewise starts a line after a comma.
    1750 sets the same line (*29 Hemathenses Asimam, Auani Ne-*), so it does not settle it. **Please check.**
- **Ch. 18** (37 verses in both; same division as the KJV): **1** *ANno* (2109), **2** *Regnauit* (2113), **3** *Is*
  (2115), **4** *sacella* (2118), **5** *Iouæ Deo* (2123), **6** *Iouæ sine* (2127), **7** *Ioua secundo* (2129), **8**
  *Palæstinos* (2135), **9** *Huius* (2138), **10** *atque ea* (2143, line start), **11** *Israelitas* (2146), **12**
  *quando-/quidem* (2149), **13** *Anno autem* (2155), **14** *Tum* (2159), **15** *Quumque* (2164), **16** *Ac tum*
  (2168), **17** *At rex* (2171), **18** *vocauere regem* (2179, line start), **19** *vos hæc* (2184), **20**
  *verbisne* (2187), **21** *An videlicet* (2190), **22** *Quod si* (2196), **23** *Age iam* (2202), **24** *Tune*
  (2207), **25** *An porro* (2211), **26** *Hic Eliacimus* (2215), **27** *At Rabsaces* (2221), **28** *Audite* (2227),
  **29** *Hæc di-/cit* (2229), **30** *neue ab eo* (2232), **31** *Nolite* (2236), **32** *donec* (2242), **33** *neue
  Ezechi-/am* (2247), **34** *Vbi sunt* (2252), **35** *Quis* (2256), **36** *Ad hæc* (2260), **37** *Tum Eliacimus*
  (2264). Small differences of division only: 1738 20 begins at *verbisne* (KJV 20 "Thou sayest"), within the speech.
- **Ch. 19** (to verse 15 here): **1** *HIs* (2272), **2** *misitque* (2275), **3** *dies* (2280; KJV 3 "Thus saith
  Hezekiah" stays in 1738 2: *sic dicit Ezechias:*), **4** *Mirum* (2285), **5** *quæ quum Ioua* (2289; KJV 4b "lift
  up thy prayer" falls in 1738 5, and KJV 5 *Hæc postquam … retulerunt* too), **6** *hæc dicetis* (2294; KJV 6 begins
  at *Esaias illis respondit*), **7** *Nam ego* (2296), **8** *Rabsaces autem* (2299), **9** *Qui* (2302), **10** *ne
  tibi* (2307), **11** *Tutemet* (2311), **12** *Numquid* (2314), **13** *Vbi sunt rex* (2317; the margin *13*'s 3 has a
  flat top like a 5, zoomed: 3), **14** *Has* (2320), **15** *Ioua Deus* (2325).

## Letters lost in the gutter

None: all line starts and ends whole, all margin numerals whole.

## Misprints and odd forms kept as printed

- Running head of leaf 451 *Cap. 19.* though the page is all ch. 18 (not text; noted only).
- 2292 *Ezechiam* (*Hæc postquam Ezechiam Esaiæ retulerunt*): at 4× the word looks like *Ezechiani*, but the last
  stroke has no dot and the space is a loose *m* (1750's OCR also reads *ezechiani*, at the same place, and at 18:37
  *Ezechiani* where 1738 clearly prints *Ezechiam*). Written *Ezechiam*. **Please check.**
- 2201 *aram*: a fibre crosses the *r* (5×); the letter's stem shows; 1750 *aram*.
- 2186 *Ezechiæ:*: beside the colon a faint smudge (4×), a risen space, not a second stop.
- 2193 *tatur*: a short stroke stands in the column's left margin before it; outside the text, not written.
- Lower case as printed: 2039, 2047 *samaritana*; 2148 *medicæ* (1750 *Medicae*); 2252–2254 *hemathenses*,
  *arphadenses*, *sepharuaimenses*, *henenses*, *auani* (1750 capitals); 2069 *sepharuaimensibus*; 2312 *assyrii*.
- Forms: 2037 *Aua* (vote *Ana*), 2147 *Habore* (vote *Habere*), 2141 *Salmanasar*, 2066 *Asimam*, 2122 *Nehostan*,
  2317 *Thelassarianos* (printed *Thelaſſarianos*; vote *Thelasfarianos*), 2319 *Henæ* (vote *Heuae*), 2303 *Tharacam*,
  2131 *gessit*.
- Commas with no following space, kept: 2047 *deductos,quoni-*, 2090 *reuererentur,hunc*, 2177 *superioris,positum*,
  2234 *fidatis,quasi*.
- Tight settings written with the space: 2036 *rex Assyriæ* (*rexAsſyriæ*), 2160 *ad Lachim* (*adLachim*).
- Spaces inside parentheses dropped: 2088 *(a quo*, 2120 *(quoniam*, 2121 *adolebant)*, 2147 *(quæ*, 2149 *positæ)*,
  2083 *(cui … Israelis)*, 2218 *(sese enim scire)*.
- 2075 *religio-*: the hyphen is a raised point, as elsewhere; written as a hyphen.
- 2153 *Iouæ*: the I is broken (looks like *[*); written *Iouæ*. 2042 *Iouæ*: the æ is faint; whole.
- Stops checked: 2087, 2094, 2096 semicolons; 2232 *defendere;* (semicolon); 2062 *posuerant:*; question marks at
  2187, 2190, 2194, 2202, 2206, 2209, 2210, 2212, 2251, 2253–2259, 2313–2320.
- **Accents**: none printed on these leaves (the vote invented none).

## Paragraph indents and drop capitals

Indented lines: **2036** *Deduxit* (17:20), **2155** *Anno autem* (18:13), **2325** *Ioua Deus Israelitarum* (19:15,
the prayer). No others (every column's left edge checked). Drop capitals: 2109 *ANno* (18:1, A over three lines;
vote already *ANno*), 2272 *HIs* (19:1, H over three lines; vote *y "ilsauditis*).

## Footnotes

- *a)* on leaf 451 col. 0, hangs on 2176 *et a) apud aquæ ductum* (18:17, between *et* and *apud*): `% a) scilicet
  extra vrbem.`
- *b)* on leaf 452 (two full-width lines at the page foot; placed after col. 1, where its mark is), hangs on 2282
  *hodiernus dies est, b) iam fetu* (19:3, after *est,*): `% b) tantus est noster dolor, quantus parturientis feminæ,
  quæ ad eiiciendum fetum iam ad vuluæ fauces progressum, vires non habet.` (the note's *fe-/tum* joined).
Both letters taken out of the text rows.

## G./L./H. marks and asterisks

None. The vote's *\** at 2242 (*\* donec*) and in 2271 are OCR noise: nothing on the page.

## Rows lost, added, removed

- Removed (5): 2108 (last line of ch. 18's summary), 2132–2133 (leaf 451's running head), 2270–2271 (ch. 19's summary).
- Added (7): `+ 450 1 900 % tra`; `+ 451 0 900 % a) …`; `+ 451 1 900 % fida-`; `+ 452 1 900` *tuere verba, quæ
  audiuisti, quibus* and `+ 452 1 901` *Assyriæ regis famuli in me inuecti* (19:6: the vote had fused these col. 1
  lines onto col. 0's 2250–2251, *rum gentium … ter- tuere verba …* / *tam ab Assyriæ … Assyriae regis famuli in me
  inuecti*; their col. 0 halves kept in 2250–2251, the col. 1 halves added in place after 2295); `+ 452 1 902 % b) …`;
  `+ 452 1 903 % orbis`.
- Words the vote lost: 2036 *Assyriæ* (*rex ex Ba-*); 2055 *sacer-* (*vnu-*); 2066 *Auani* (*Anam*);
  2234 *Ioua sit* (garbled); 2251 *ram* (*tam*); 2280 *dies* (*die*). Many lines on leaf 452 col. 1 had their last
  letters or words lost (2281 *contu-*, 2282 *iam fetu*, 2283 *suppe-*, 2285 *tuus*, 2286 *As-*, 2287 *conui-*,
  2288 *petu-*, 2289 *Io-*, 2294 *domi-*): restored from the page.
- Vote misreadings of substance corrected: 2056 *vnus sacer-/dotum* (vote *vnu-/s*), 2165 *triginta* (*rngin te*),
  2200 *certam* (*certain*), 2201 *aram* (*a^am*), 2223 *meus* (*mens*), 2215 *Helciæ fi-/lius*, 2290 *Deus tuus
  audiuerit*, 2295 *noli me-*.

## Wording doubts (1738 against 1750)

- 19:13 (2319): 1738 *rex vrbis Sepharuaimi*, 1750 *rex ciuitatis Sepharuaimi*: a 1750 change; 1738 clear.
- 18:30 (2234): 1738 *quasi vos Ioua sit defensurus*; 1750's OCR *quasi vos Ioua defehfurus* (no *sit*: likely OCR
  loss, the 1750 line is not checked on its page). 1738 clear.
- Otherwise spelling, capitals and punctuation only (1750 *quartodecimo,*; *Medicae*; capitalized gentilics; *Rezinem*
  not here).

## Omission check (against BSB/KJV)

Each verse 17:23b–19:15a read against the KJV. Castellio condenses: 17:24 "Babylon, Cuthah, Ava, Hamath, Sepharvaim"
all present; 17:29 "every nation made gods of their own" *cuiusque nationis homines, deos gentiles fecerant*; 17:34
"the statutes, or after their ordinances" *instituta, iura, legem, disciplinam*; 18:4 "brake in pieces the brasen
serpent" *contriuit*; 18:17 "came and stood by the conduit of the upper pool" present; 18:26 "for we understand it"
*sese enim scire*; 18:32 "that ye may live, and not die" given as *vt ita vestræ saluti prospiciatur*; 18:34 "Hena,
and Ivah" *henenses, et auani*; 19:3 "for the children are come to the birth" *iam fetu in arctum progresso* (with note
b); 19:12 "Gozan, Haran, Rezeph, Eden … Thelasar" present. His rendering, not a loss. No clause the page has is
missing from my reading (the two fused col. 1 lines restored).

## Uncertain readings (want Claude's check on the page)

- 17:29 at *Hemathenses* (line start) vs *Auani*.
- 2292 *Ezechiam* vs *Ezechiani* (leaf 452 col. 1, line 13).
- 2201 *aram* under a fibre.

## Summary

295 rows written (rows 2034–2326: 293, less 5 removed, plus 7 added); 236 of the 288 kept rows changed from the vote
(mostly ſ→s, æ, spacing, verse numbers). Text ends at 2 Kings 19:15 *rubis insidens, qui solus omnium* (catchword
*orbis*).

## reader-09 (`reader-09.md`)

# Reader 09: rows 2327–2617 (2 Kgs 19:15 *orbis regnorum* – 22:3 *nec ad dextram nec ad*), leaves 453–455

Every row read on the whole page images (`1738-page-0453/0454/0455.jpg`), each column zoomed in four bands at 1.4×,
doubtful letters and marks at 3–4× (*efficiente*, *surum?*, *conualuit*, *abhinc*, *res ad*, the asterisk at 20:13,
the catchword *fecit;*, *Nis-/Adra-*, the foot of leaf 453). 1750 (`sources/archive/1750/text.txt` lines
54480–54860) used only as a check on wording. The text continues reader 08's *rubis insidens, qui solus omnium*
(2326) with *orbis* (2328), as its catchword says.

## Leaves and what is on them

- **453** (p. 381, recto, head *Cap. 19.*): the vote's row 2327 *Cap. 19.* is the running head → removed. Col. 0
  rows 2328–2377 (19:15 *orbis* – 19:26 end); foot: footnotes *c)* and *d)* on one line under col. 0 → added
  `+ 453 0 900`, `+ 453 0 901`. Col. 1 rows 2378–2421 (19:27 – 19:37 end), rule, *CAPVT XX.* and italic summary
  (four lines, not in the vote's rows), `\c 20` (2422). Foot: catchword *Per* → added `+ 453 1 900 % Per`. No
  signature.
- **454** (p. 382, verso, head *Cap. 20. 21.*): running head not in the rows. Col. 0 rows 2423–2473 (20:1 *PEr* –
  20:13 *armarium:*); col. 1 rows 2474–2505 (20:13 *denique* – 20:20 end), rule, *CAPVT XXI.* and italic summary (four
  lines, not in the rows), `\c 21` (2506), rows 2507–2519 (21:1 *POstquam* – 21:4 *regis*). Foot: catchword *fecit;*
  → added `+ 454 1 900 % fecit;` (the catchword has a semicolon; the next page's first word is *fecit:* with a colon:
  both as printed). No signature, no footnotes.
- **455** (p. 383, recto, head *Cap. 21. 22.*): running head not in the rows. Col. 0 rows 2520–2569 (21:4 *fecit:* –
  21:14 *prædæ*); footnote *e)* at its foot: the vote's own row 2570 (*0 sie Hierosolymam punUtn 1 vecec.*) kept and
  read as `% e) …`. Col. 1 rows 2571–2606 (21:14 *sint* – 21:25 end), rule, *CAPVT XXII.* and italic summary (two
  lines; the vote kept the second as row 2608 *#1 Muiteru Hold\* vathiniim.* = *Mulieris Holdæ vaticinium.* →
  removed), `\c 22` (2607), rows 2609–2617 (22:1 *AMone* – 22:3 *nec ad*). Foot: catchword *sini-* → added
  `+ 455 1 900 % sini-` (the next reader's first line should begin *nistram*). No signature.

`\c 20` (2422), `\c 21` (2506), `\c 22` (2607) stand where *CAPVT XX.*, *XXI.*, *XXII.* stand: kept. **No `\c 23`
in my leaves** (ch. 22 begins at the foot of 455 col. 1 and runs on).

## Verse numbers

Margins: 453 col. 0 left (the *1* of 16, 17, 18 cut in the gutter: only *.6*, *:7*, *:8* show; 19–26 whole), col. 1
right; 454 col. 0 left, col. 1 right; 455 col. 0 left, col. 1 right. The vote's numbers were three behind in ch. 19
and wrong through ch. 20–22; all placed again from the margins.

- **Ch. 19** (continuing reader 08's 15): **16** *aperi Ioua* (2330), **17** *Sane* (2334), **18** *earumque* (2335),
  **19** *Quapropter* (2340), **20** *Tum Esaias* (2344, line start), **21** *Atque hoc est* (2348), **22** *In quem*
  (2352), **23** *ego tot meis* (2357), **24** *Ego effodi* (2363), **25** *Numquamne* (2366), **26** *earumque incolas*
  (2372), **27** *Tuas* (2378, line start), **28** *Quoniam* (2380), **29** *Tu vero* (2385), **30** *Ac quod* (2392),
  **31** *Nam a* (2395), **32** *Quare* (2398), **33** *Qua venit* (2403), **34** *me eam* (2405), **35** *Igitur*
  (2408), **36** *Itaque* (2413), **37** *Vbi postquam* (2415).
  **1738's ch. 19 has 37 verses, as the KJV.** In my part the division differs only slightly: 1738 15 holds KJV 16a
  (*præbe Ioua aurem tuam, et audi*; KJV 16 "LORD, bow down thine ear"), 16 begins at *aperi* (KJV 16b); KJV 23a "By
  thy messengers thou hast reproached the Lord" (*per nuntios … maledixisti atque ita dixisti*) stays in 1738 22, and
  1738 23 begins at *ego tot meis* (KJV 23b). From 24 on, the same as the KJV.
- **Ch. 20** (20 verses; KJV 21): **1** *PEr* (2423), **2** *Ille* (2429), **3** *vt recordaretur* (2430, by the
  wide space and the sense; the numeral stands beside the line *Iouam precatus, vt recordare-*; KJV 3 "Remember
  now"), **4** *Tum Ioua* (2435), **5** *reuertere* (2437), **6** *addamque* (2443), **7** *Igitur* (2448), **8**
  *Quærenti* (2451), **9** *hoc tibi* (2454), **10** *Facile* (2458), **11** *Tum Ioua oratus* (2462), **12** *Sub id*
  (2466, indented), **13** *Quibus* (2469), **14** *Tum Esaias* (2477), **15** *Quid autem* (2482), **16** *Et Esaias*
  (2486), **17** *Scito* (2488), **18** *Quin et* (2493), **19** *Et Ezechias* (2496; the numeral is beside the line
  *spadones. Et Ezechias: non re-*: placed after the stop and wide space, at *Et Ezechias*, as KJV 19 "Then said
  Hezekiah"; the vote had it at *non recuso*), **20** *De reliquis* (2500).
  Same division as the KJV for 1–20; **KJV 20:21** ("And Hezekiah slept with his fathers: and Manasseh his son
  reigned") is in 1738 **21:1** (*POstquam ad maiorum suorum manes migrauit Ezechias, regnum pro eo obtinuit
  Manasses*).
- **Ch. 21** (25 verses; KJV 26): **1** *POstquam* (2507), **2** *Regnauit annos* (2511), **3** *Is Iouam* (2513),
  **4** *Sacella* (2516), **5** *altaria cunctis* (2524), **6** *Simulacrum* (2531), **7** *effecturumque* (2537),
  **8** *modo omnia* (2541, line start), **9** *At illi* (2544), **10** *Ergo Ioua* (2548), **11** *quandoquidem*
  (2550), **12** *propterea* (2556), **13** *et e) in Hierosolymam* (2561), **14** *adspernatusque* (2566), **15**
  *quoniam me* (2571; the numeral beside *sint et direptioni: quoniam me*, placed after the colon and wide space; the
  vote had it at the line start), **16** *Præterea* (2576, indented), **17** *De ceteris* (2581), **18** *Manassi*
  (2584), **19** *Regnauit Hierosolymis* (2589), **20** *Is Iouam* (2592), **21** *eademque* (2594), **22** *et
  Iouam* (2596), **23** *Hic rex Amon* (2599), **24** *Omnibusque* (2601), **25** *De reliquis* (2604).
  Against the KJV: 1738 1 = KJV 20:21 + 21:1a (*annos tum natus duodecim*); 2 = KJV 1b (*Regnauit annos
  quinquaginta quinque … Haphsiba*); 3 = KJV 2; 4 = KJV 3–4 (*Sacella … adorauit coluitque: aras in æde Iouæ
  ædificauit … collocaturum*); 5 = KJV 5–6 (*altaria cunctis … Iouam irritauit*); 6 = KJV 7 (*Simulacrum … in
  perpetuum*); 7 = KJV 8a (*effecturumque … non mouerent*); 8 = KJV 8b (*modo omnia … curarent*, KJV "only if they
  will observe"); 9–25 = KJV 9–25. **KJV 21:26** (Amon buried in the garden of Uzza, Josiah reigns) is in 1738
  **22:1**.
- **Ch. 22** (to verse 3 here): **1** *AMone* (2609; = KJV 21:26 + 22:1a), **2** *Regnauit Hierosolymis* (2612; =
  KJV 22:1b), **3** *Is Iouæ paruit* (2615; = KJV 22:2).

## Letters lost in the gutter

Only the margin numerals 16, 17, 18 on leaf 453 col. 0 (their *1* cut; read by the visible *6/7/8* and the
sequence). No text letters lost.

## Misprints and odd forms kept as printed

- 2418 *Sarasar* (printed *Saraſar*; vote *Serafar*; 1750 *Sarafar*).
- 2591 *Messalemethan* (printed *Meſſalemethan*; 1750's OCR *Maflale-*: not checked on its page), *Harusi*,
  *Iote-/banam*.
- 2513 *Haphsiba*; 2614 *Basecha-/tensi*; 2421 *Esaraddon*; 2416 *Nis-/rochi*.
- 2335 *assyrii* lower case (as 19:11 at 2312).
- 2555 *Iudæos*, 2551 *Iudææ*: æ printed throughout these leaves (the vote's *ae* written æ where the page has the
  ligature: *cæli*, *ædificauit*, *Iouæ*, *Iudææ*, *prædæ*, *Ozæ*, *Adaiæ*, *ætatis*).
- 2579 *Israelitas* (vote *Israelites*): the page has *Israelitas*.
- Commas with no following space, kept: 2473 *mata,vnguenta*, 2522 *dixisset,se*, 2595 *satus,cultos*.
- Spaces inside parentheses dropped: 2459 *(inquit Ezechias)* (printed *( inquit Ezechias )*).
- 2454 *surum?*: the question mark has a faint upper stroke (4×); a question mark, not a footnote letter (1750
  *furum?*).
- 2481 *terrarum*: the second *r* is broken (looks like *F*); *terrarum*.
- Hyphens at line end printed as low points in places (2416 *Nis-*, 2417 *Adra-*, 2591 *Iote-*, 2598 *ingres-*):
  written as hyphens.
- The catchword at the foot of 454 is *fecit;* while 455 begins *fecit:*; both written as printed.

## Accents

None printed on these leaves; the vote invented none. Checked at 4×: 2397 *efficiente* (a brown stain over the *e*,
not an accent), 2442 *abhinc* (a stain over the *a*), 2575 *res ad* (a faint speck over the *a*, no accent's shape;
1750 *ad*). **Please check 2575 *ad***, if you want certainty.

## Paragraph indents and drop capitals

Indented lines: **2466** *Sub id tempus* (20:12), **2576** *Præterea* (21:16). No others (every column's left edge
checked; 2344 *Tum Esaias* and 2435 *Tum Ioua* and 2541 *modo omnia* start lines flush). Drop capitals: 2423 *PEr*
(20:1, P over three lines; vote *f~|Er*), 2507 *POstquam* (21:1, P over three lines), 2609 *AMone* (22:1, A over three
lines); the lines beside each (2424–2425, 2508–2509, 2610–2611) are set in by the capital, not indents.

## Footnotes

- *c)* (leaf 453, under col. 0), hangs on 2365 *omnia c) aggeribus* (19:24): `% c) magna.`
- *d)* (same line), hangs on 2367 *me d) hoc olim* (19:25): `% d) istarum vastitatum auctorem esse, de quibus tu te
  iactas.`
- *e)* (leaf 455, col. 0 foot), hangs on 2561 *et e) in Hierosolymam* (21:13): `% e) sic Hierosolymam puniam, vt etc.`
  (the vote's row 2570, kept as the footnote row).
All letters taken out of the text rows.

## G./L./H. marks and asterisks

No G./L./H. marks. **Asterisk** at 2470 *Ezechias, \* ostendit* (20:13), clear at 3×, with no footnote on the page:
taken out (1750 has none). The vote's *\** in 2420 (*Armenian\**), 2608 and *<■'* in 2365 are noise / the note letter.

## Rows lost, added, removed

- Removed (2): 2327 (running head *Cap. 19.*), 2608 (last line of ch. 22's summary).
- Added (5): `+ 453 0 900 % c)`, `+ 453 0 901 % d)`, `+ 453 1 900 % Per`, `+ 454 1 900 % fecit;`, `+ 455 1 900 % sini-`.
- No text line lost. Vote misreadings of substance corrected: 2345 *Ezechiæ* (vote *Ezechias*), 2349 *illum* (vote
  *ilium*), 2401 *stuc* (vote *rtisc*), 2407 *meum* (vote *menta*), 2416 *Nis-* (vote *Nis.*),
  2418 *Sarasar*, 2427 *etenim moritu-* (vote *denim raoritu-*), 2428 *reualiturum*, 2437 *est* (vote *en*), 2455
  *erit a Ioua, eum factu-* (vote *ente Ioua, eumfactu-*), 2492 *tur* (vote *tnr*), 2522 *dixisset,se*, 2531 *luci*
  (vote *Inci*), 2532 *facti* (vote *fasti*), 2537–2538 *effe-/cturumque*, 2566 *tersa*, 2586 *sepulto* (vote
  *sepulro*), 2600–2601 *interfe-/ctus*, 2614 *matre Idida*.

## Wording doubts (1738 against 1750)

None of substance. 1750 agrees word for word where its OCR is legible; differences are punctuation (1750
*turum;* at 21:4 vs 1738 *turum:*; 1750 *Facile est (inquit* without the comma) and 1750's spelling of the
mother's name (*Maflale-*, OCR). 1738 clear throughout.

## Omission check (against BSB/KJV)

Each verse 19:15b–22:2 read against the KJV. Castellio condenses but nothing is missing: 19:24 "with the sole of my
feet have I dried up all the rivers of besieged places" *pedum vestigiis omnia aggeribus munita flumina siccaui*;
19:26 "as the grass on the housetops, and as corn blasted before it be grown up" *gramini tectorum, quod ante iustum
arescit incrementum*; 19:28 "hook in thy nose, bridle in thy lips" present; 19:37 Nisroch, Adrammelech, Sharezer,
Armenia, Esarhaddon present; 20:8–11 the shadow on the dial of Ahaz present; 20:13 "the silver, and the gold, and the
spices, and the precious ointment, and all the house of his armour" present; 21:3 "as did Ahab king of Israel"
*exemplo Achabi Israelitarum regis*; 21:6 "observed times, and used enchantments, and dealt with familiar spirits and
wizards" *auguriis et hariolatione … ventriloquos et magos*; 21:13 "the line of Samaria, and the plummet of the house
of Ahab" *amussi … libra*; 21:19 "Meshullemeth, the daughter of Haruz of Jotbah" *Messalemethan, Harusi filiam,
Iotebanam*; 21:26 and 22:1 (Josiah eight years old, 31 years, Jedidah daughter of Adaiah of Boscath) present. No
clause the page has is missing from my reading.

## Uncertain readings (want Claude's check on the page)

- 20:19 placed at *Et Ezechias* (2496), not the vote's *non recuso*; 21:15 at *quoniam me* (2571), not the line start.
- 2575 *ad* (speck above the *a*: not an accent, I judge).
- 2454 *surum?* (faint question mark).

## Summary

Rows written 294 (289 of the vote's rows + 5 added); changed from the vote 215 (including verse numbers moved);
removed 2 (2327, 2608); added 5. Ends at 2 Kings 22:3 *sui secutus, nec ad dextram nec ad* (catchword *sini-*).

## reader-10 (`reader-10.md`)

# 2 Kings, reader 10: leaves 456–458 (rows 2618–2916)

Read on the page images `1738-page-0456/0457/0458.jpg`, every column zoomed (ffmpeg, 1.5–5×); the vote's rows used
only for row numbers and as a first draft. 1750's OCR (`sources/archive/1750/text.txt`, lines ~54880–55215) grepped for
the doubtful words.

## Leaves

- **456** (p. 384, head *REGVM LIBER IIII.* / *Cap. 22. 23.*): col. 0 = 22:3 end (*sinistram deflexit*) to 22:14
  (*Hierosolymis*); col. 1 = 22:14 end – 22:20, then the rule, **CAPVT XXIII** and its italic summary (5 lines), then
  23:1–3 (*… monita, de-*). Catchword *creta,* at the foot of col. 1.
- **457** (p. 385, head *Cap. 23.* / *REGVM LIBER IIII.*): col. 0 = 23:3 *creta* – 23:12 *earumque pul-*; col. 1 =
  23:12 *uerem* – 23:22 *præsi-*. Foot: signature *B b* and catchword *dum,*.
- **458** (p. 386, head *REGVM LIBER IIII.* / *Cap. 23.24.*): col. 0 = 23:22 *dum* – 23:34 *et gentem cen-*; col. 1 =
  23:34 *tum argenti* – 23:37, rule, **CAPVT XXIIII** and its summary (4 lines), 24:1–8 (*… matre Ne-*). Catchword
  *hosta,* (reader 11's first row should begin *hosta*; the vote's row 2919 has *oste*).

No footnotes on these leaves.

## Chapter rows

- **Row 2699: the vote's `\c 21` corrected to `\c 23`.** It stands where the page prints **CAPVT XXIII** (leaf 456 col.
  1, after *illaturus.*). This is the chapter heading the vote "lost": it had found it but numbered it 21. Its summary
  lines were already gone from the vote.
- Row 2887 `\c 24`: right; **CAPVT XXIIII** stands there (leaf 458 col. 1).

## Verse numbers (1738's margin numbering)

Margins: 456 col. 0 left, col. 1 right (all the col. 1 numerals partly cut at the outer edge: *1* of 15–19 shows,
and *2* of 20; read by the sequence); 457 col. 0 left (4, 5, 6, 7, 8 visible; 9–12 lost in the gutter, only a
stroke beside *Etenim*; placed by sense and wide spaces), col. 1 right (13–22 whole); 458 col. 0 left (23–34, 30
and 32–34 partly cut), col. 1 right (35–37 show only *3*; 24:1–8 whole). The vote's numbers were wrong almost
everywhere (one to three behind in ch. 22–23, and 24:1 had been put on a summary line); all placed again.

- **Ch. 22** (continuing reader 09's 3): **4** *Hic Iosias* (2618), **5** *vt summam* (2623), **6** *vtque ea* (2626),
  **7** *neque illis* (2634), **8** *Tum Helcias* (2637), **9** *Eum vbi* (2641, line start), **10** *hoc quoque*
  (2646), **11** *Rex, auditis* (2650, line start), **12** *imperauit* (2651; numeral beside *cerptis suis vestimentis,
  impera-*: placed at *impera-*, KJV 12 "And the king commanded"), **13** *vt Iouæ oraculum* (2655), **14**
  *Adiuerunt* (2663), **15** *illa eis* (2670), **16** *sic dicit Ioua:* (2673, the second *sic dicit*), **17** *quoniam
  relicto* (2677), **18** *Regi autem* (2682), **19** *Quod ad ea* (2685), **20** *Itaque te tuis* (2693).
  **1738's ch. 22 has 20 verses, as the KJV, but divided differently:** 1 = KJV 21:26 + 22:1a, 2 = 22:1b, 3 = 22:2,
  4 = 22:3, 5 = 22:4, **6 = KJV 22:5–6** (*vtque ea curatoribus … quibus templum resarciretur*), and 7–20 = KJV 7–20.
- **Ch. 23**: **1** *HAec* (2700), **2** *cumque omnibus* (2703), **3** *et pro suggestu* (2711), **4** *iussitque*
  (2719), **5** *flaminesque* (2728), **6** *et lucum* (2734, line start), **7** *et ganeas* (2739), **8**
  *abductisque* (2742), **9** *Etenim* (2749, line start; numeral cut), **10** *Polluit* (2753, line start; cut),
  **11** *equos sustulit* (2756, by the wide space; cut), **12** *Aras in* (2761, by the wide space; cut), **13**
  *Sacella in* (2767), **14** *statuas* (2774), **15** *A-ram* (2776), **16** *Quumque* (2783), **17** *Deinde quum*
  (2791), **18** *iussit illum* (2798), **19** *Præterea* (2802), **20** *eademque* (2806), **21** *Deinde
  Hierosolymam* (2811), **22** *Nullum* (2815), **23** *quale id* (2819), **24** *Ad hæc* (2821), **25** *Sed
  quamquam* (2829), **26** *non tamen* (2835), **27** *quin decreuerit* (2839), **28** *De reliquis* (2845), **29**
  *Hic Iosias* (2847), **30** *et a suis* (2854), **31** *Eius in locum* (2857, line start, indented), **32**
  *Regnauit* (2860), **33** *Is maiores* (2862), **34** *et gentem* (2867), **35** *Ioachazum* (2874, line start),
  **36** *Argentum* (2876), **37** *Regnum iniit* (2881).
  **37 verses, as the KJV**; 1–30 the same division as the KJV. Then: 1738 **31** = KJV 30b + 31a (*Eius in locum
  Ioachazus … vnctus, rexque … factus est, anno ætatis suæ vicesimo tertio*; KJV 30b "the people of the land took
  Jehoahaz … made him king"), **32** = KJV 31b (*Regnauit … Lebnensi*), **33** = KJV 32 + 33a (*Is maiores … regno
  hierosolymitano priuauit*), **34** = KJV 33b + 34a (*et gentem centum … in Ioacimum*), **35** = KJV 34b
  (*Ioachazum … mortuus est*), **36** = KJV 35, **37** = KJV 36–37 (*Regnum iniit … Rumensi. Is in Iouam fuit
  impius …*).
- **Ch. 24** (to verse 8 here): **1** *HVius* (2889), **2** *cui quum* (2891), **3** *qui Iudæam* (2896), **4** *vt eos
  propter* (2899), **5** *De reliquis* (2905, line start), **6** *Ioacimo vita* (2907), **7** *Nec deinceps* (2909),
  **8** *Duodeuicesimum* (2914, line start). Against the KJV: 1738 1–2 = KJV 1 (*cui quum … fecisset* = "Jehoiakim
  became his servant three years: then he turned and rebelled"), 2 continues with KJV 2a (*immisit … Ammonitas*), 3 =
  KJV 2b–3a (*qui Iudæam … accidit*), 4 = KJV 3b–4; 5–8 = KJV 5–8.

## Letters lost in the gutter

Only margin numerals (above). No text letters lost.

## Misprints and odd forms kept as printed

- 2633 *latumiis* (1750 the same).
- 2667 *Harami* (vote *Hararai*; 1750 *Harami*).
- 2766 *cucurrit in torrentem* (sense "cast"/"scattered"; 1750 also *cucurrit*): kept.
- 2770 *Solomo*; 2771 *Chamoso*; 2759 *Nathanmelechi*; 2760 *Pharuarim*; 2754 *Hennomi*; 2745 *a Gaba ad Bersabam*;
  2884 *Zebuda Phadaiæ … Rumensi*; 2862 *Lebnensi*.
- Lower case: 2797 *bethelensem*, 2866 *hemathensi* (1750 *Hemathensi*), *hierosolymitano*, 2913 *ægyptii*.
- 2795 *Iudæa* (æ), 2683 *Iudææ*; æ/œ printed throughout (*Iouæ*, *fœderis*, *cœnaculi*, *fœdauit*).
- Commas with no space after, kept: 2653 *filio,et*, 2734 *lucum,ex*, 2808 *sacerdotes,qui*, 2838 *flagitia,quibus*.
- Tight words given their space: 2665 *etSaphan*, 2850 *expeditionemad*, 2867 *mitanopriuauit*, 2639 *selibrum*.
- Spaces before punctuation dropped (*referetis :*, *Iosias :*, *mam , et ædem*, *multauit :*, *quinque :* etc.).

## Paragraph indents and drop capitals

- 2700 *HAec* (drop capital H, 3 lines deep) and 2889 *HVius* (drop capital H): chapter openings.
- **2857** *Eius in locum Ioachazus* (23:31): indented, a new paragraph.
- No other indented lines (each column's left edge checked).

## Footnotes, G./L./H. marks, asterisks

None on these leaves. (A blot before *plo Iouæ* at 2630, leaf 456 col. 0, is ink, not a mark.)

## Rows removed, added, changed

- Removed: **2714** (*Cap. Z3.*, the running head of 457), **2868** (*REGVM LIBER IIH.*) and **2869** (*Cap. 13.24.*),
  the running head of 458, and **2888** (*Jm I ul.11 Sedcci<e. In hi.Uos ioan.*, the last line of ch. 24's summary
  *Impietas Sedeciæ. In Iudæos Ioua.*; the vote had put `#1` on it).
- Added: `+ 456 1 900 % creta,` (catchword), `+ 457 1 900 % B b dum,` (signature and catchword), `+ 458 1 900 % hosta,`
  (catchword).
- Corrected: 2699 `\c 21` → `\c 23`.
- Text: 2791 the vote's *ediderat. quum* lacked **Deinde** (printed *ediderat. Deinde quum*); 2703 the vote's *eumque*
  is printed *cumque*; 2862 *lilia* → *filia*; 2864 *esse-/nt* → *offen-/dit*; 2839 *dccreuait* → *decreuerit*; 2817
  the vote's *Israélitis* had an invented accent: printed *Israelitis*.

## Accents

None printed in these rows. The vote's *Israélitis* (2817) dropped. Two doubtful marks kept plain: 2647 *quoque*
(a hairline above the first o, zoomed at 5×: looks like a damaged sort or a speck, not a clear grave) and 2715
*mente* (specks over m, e and e alike: dirt, not accents). Please check 2647 on the page if in doubt.

## Wording doubts (1738 against 1750)

None beyond spelling and punctuation in the places grepped (*Harami*, *latumiis*, *cucurrit*, *a Gaba*,
*Nathanmelechi*, *Pharuarim*, *tota mente*, *quoque nuntiauit*, *Deinde quum*, *decreuerit*, *offendit*,
*expeditionem ad*, *Is in Iouam*): 1750 agrees word for word. 1750 adds a comma in 23:2 *populo, in Iouæ* (1738
*populo in Iouæ*).

## Omission check (against the BSB/KJV)

Every verse 22:3–24:8 checked clause by clause: nothing the page has is lost in the reading, and the page has every
clause of the English (22:14 Shallum's line *Sellumi Thecuæ filii, Harami nepotis, vestium custodis*; 23:4 Baal,
Asherah *luco*, host of heaven; 23:8 the gate of Joshua the governor; 23:16 the man of God's word; 23:24 mediums,
teraphim *lares*, idols *stercoreos deos*; 24:4 the innocent blood). The only missing words were the vote's
(*Deinde* at 2791).

## Summary

- Rows written: 298 (295 of the range's 299, plus 3 added); header + 298 lines.
- Changed from the vote: 219 rows (mostly s for ſ, æ, verse numbers and OCR repairs).
- Removed: 4 (2714, 2868, 2869, 2888). Added: 3 (`%` catchword/signature rows).
- Text ends at **2 Kings 24:8** (1738 = KJV), *rosolymis menses tres, matre Ne-* (catchword *hosta,*).

## reader-11 (`reader-11.md`)

# 2 Kings, reader 11: leaves 459–460 (rows 2917–3087)

Read on the page images `1738-page-0459.jpg` and `1738-page-0460.jpg`, every column zoomed (ffmpeg, 1.5–5×); the
vote's rows used only for row numbers and as a first draft. 1750's OCR (`sources/archive/1750/text.txt`, lines
~55250–55480) read beside the whole range for wording doubts.

## Leaves

- **459** (p. 387, head *Cap. 24. 25.* / *REGVM LIBER IIII.*): col. 0 = 24:8 end (*hosta, Elnathanis filia*) to
  24:20, the rule, **CAPVT XXV** and its italic summary (4 lines: *Sedeciæ defectio a rege Babyloniæ.
  Hierosolymæ expugnatio, incensio, excisio. Ioachinis carcer. In eumdem regis Babyloniæ benignitas.*), then 25:1
  (drop capital Q, *QVum hic Sedecias … men-*); col. 1 = 25:1 *sis decimi* – 25:16 *ad Iouæ*. Foot: signature
  *B b 2* (its lower half cut by the image edge) and catchword *tem-*.
- **460** (p. 388, head *REGVM LIBER IIII.* / *Cap. 25.*): col. 0 = 25:16 *templum* – 25:23 *Ioannes*; col. 1 = 25:23
  *Careæ* – 25:30 *diu vixit.* (line 70). **2 Kings ends there.** Below it: a large woodcut ornament (a putto with
  two drumsticks between two kettledrums, with foliage) and the catchword *PARA-* (for *PARALIPOMENON*, leaf 461).
  No *FINIS*, no text of 1 Chronicles on this leaf. The ornament is not in the vote; the catchword is kept as a `%`
  row (as reader 10's catchwords).

No footnotes on these leaves.

## Chapter rows

- Row 2962 `\c 25`: right; **CAPVT XXV** stands there (leaf 459 col. 0, after *tolleret.*).
- No CAPVT on leaf 460.

## Verse numbers (1738's margin numbering)

Margins: 459 col. 0 left (the gutter cuts the first figure of 10–20: *o*, *.1*, *ɪ2*, *ɪ3*, *ɪ4*, *ɪ5*, *6*, *7*, *8*,
*9*, *o* show; read by the sequence, all placed by wide spaces), col. 1 right (2–16 whole); 460 col. 0 left (17–23
whole), col. 1 right (24–30, the right edge slightly cut, *3c* for 30). The vote's numbers were wrong throughout
(it numbered ch. 24 from 6, and ch. 25 one or two behind from 5 on, losing 28); all placed again.

- **Ch. 24** (continuing reader 10's 8): **9** *Is patrem* (2920), **10** *Per id tempus* (2922, line start), **11**
  *quumque vrbs* (2925), **12** *dedidit* (2928), **13** *quo capto* (2931), **14** *Et totam* (2938), **15** *et
  Ioachine rege* (2942), **16** *omnibus denique* (2947; numeral beside *mille, omnibus denique*, wide space after
  *mille,*), **17** *Mattaniam* (2950), **18** *qui Sedecias* (2953, line start), **19** *Fuit* (2957), **20** *Ioua
  tanta* (2959).
  **1738's ch. 24 has 20 verses, as the KJV.** 9–11 = KJV 9–11; **12** = KJV 12a (*dedidit se Ioachin … spadonibusque*);
  **13** = KJV 12b + 13 (*quo capto, Babyloniæ rex anno sui regni octauo abstulit …*, KJV 12b "the king of Babylon
  took him in the eighth year"); 14 = KJV 14; **15** = KJV 15 + 16a (*et Ioachine rege … fabrisque et opificibus
  mille*, the seven thousand men of might and the thousand craftsmen of KJV 16); **16** = KJV 16b (*omnibus denique,
  quorum vires erant ad bellum idoneæ … abductis*); 17–20 = KJV 17–20. (With reader 10's 1–4: the chapter's
  divisions differ from the KJV at 1–4 and 12–16.)
- **Ch. 25**: **1** *QVum* (2964), **2** *Quæ postquam* (2971), **3** *nono die* (2973), **4** *et rex Sedecias*
  (2976), **5** *Sed eum* (2981), **6** *et Reblatham* (2985, line start), **7** *eiusque filiis* (2987), **8**
  *Quinti autem* (2990), **9** *Iouæ templum* (2995), **10** *Muros au-tem* (2998), **11** *Re-liquias* (3000), **12**
  *relictis* (3006, line start), **13** *Columnas* (3007), **14** *Ollas* (3011), **15** *Acerras* (3014, line start),
  **16** *columnas duas* (3016, line start), **17** *quorum tot vasorum* (3019), **18** *Comprehendit* (3027), **19**
  *ac ex vrbe* (3031), **20** *hos, inquam* (3038), **21** *qui illic* (3041), **22** *Abductis* (3043, line start),
  **23** *Quod postquam* (3047), **24** *quibus quorum-que* (3057), **25** *Sed accidit* (3063), **26** *Tum vniuersus*
  (3069), **27** *Anno autem* (3072), **28** *eumque comiter* (3079, line start; see below), **29** *eum-que per
  omnem vitam* (3083), **30** *et quotidiano* (3085).
  **1738's ch. 25 has 30 verses, as the KJV**, divided the same except: **16** = KJV 16a (*columnas duas, lacum vnum,
  bases quas Solomo rex fecerat ad Iouæ templum*), **17** = KJV 16b + 17 (*quorum tot vasorum immensum æris pondus
  erat* = "the brass of all these vessels was without weight", then the pillar's height); **21** = KJV 21a (*qui illic
  eos … interfecit*), **22** = KJV 21b + 22 (*Abductis autem ex sua patria Iudæis* = "So Judah was carried away out of
  their land", then Gedaliah set over them).
- **Placed by sense** (no wide space on a tightly set line): **28** and **29**. The numeral 28 stands beside *eumque
  comiter adlocutus, eius*; the spaces in that line are even, so 28 could stand before *eumque* (line start) or before
  *eius solium*. Placed at *eumque* (KJV and Vulgate 28 begin with the kind words: "And he spake kindly to him";
  *et locutus est ei benigna*). 29 stands beside *tis eius carceris vestimentis, eum-*: placed at *eum-que per omnem
  vitam* (KJV 29 "and changed his prison garments" belongs with the clause *mutatis … vestimentis* already in 28's
  sentence, but no other start fits the line: *tis eius …* is a word's end). Please check 28 if in doubt; 1750 puts
  its 28 beside the same line.

## Letters lost in the gutter

Only margin numerals (above). No text letters lost.

## Misprints and odd forms kept as printed

- **3021 *eubitus*** (*duodeuiginti eubitus in altitudinem*): printed *eubitus*, zoomed at 4×, the first letter an e
  with its bar (cf. *cubitos* two lines below, a clear c). 1750 *cubitos*. Misprint kept.
- 3046 *Ahichami* (vote *Ahicliami*; 1750 *Achicami*): kept.
- 3035 *Sophrem* (1750 the same); 3055 *Careæ*, *Thanehumethi*; 3065 *Elisamæ*; 3042 *Hemathensium*; 2957
  *Lebnensem*; 3075 *Euilme-rodachus*; 2935 *Solomo*, 3017 *Solomo* (a speck in the o).
- Lower case: 2982 *chaldæi*, 2983 *hierichuntio* (1750 the same).
- Commas with no space after, kept: 2927 *obsessam,ve-*, 2935 *vasa,quæ*, 2942 *rege,eius-*, 2944 *nibus,et* and
  *primatibus,omni-*, 2947 *denique,quorum*, 3069 *populus,ma-*.
- Tight words given their space: 2926 *nem venisset* (vote *nemvenisfet*), 2985 *et Reblatham*, 2987 *supplicio est*,
  2988 *ipse ex-*, 3086 *penu aluit*, 2961 *eos e suo*.
- Spaces before punctuation dropped (*runt :*, *nisset :*, *busque :*, *decima :*, *templum :*, *esse :* etc.).
- 2919 *hosta,* (vote *oste ,*), as reader 10's catchword.

## Paragraph indents and drop capitals

- 2964 *QVum* (drop capital Q, 3 lines deep): the chapter opening.
- No indented lines (each column's left edge checked on both leaves).

## Footnotes, G./L./H. marks, asterisks

None on these leaves.

## Accents

None printed in these rows; the vote invented none. Three marks looked at and kept plain:
- 2920 *patrem*: a faint hairline over the e (5×); detached, as faint as the paper's specks: not an accent.
- 2943 *matre*: a thin stroke well above the e, not touching it (4×): a hair or speck, not a grave (an ablative would
  not take one). The stroke between *et* and *proceribus* in the same line is a flaw: printed *et proceribus*.
- 3044 *dæis* (*Iudæis*): the i's dot is a little elongated and slanted (5×); read as a damaged dot, not an accent.
  Please check on the page if in doubt.
- 3073 *Ioachinis*: an ink blot on the second i, not an accent.

## Rows removed, added, changed

- Removed: **2917** (*REGVM LIBER HIT.*) and **2918** (*ap. 24.15.*), the running head of 459; **2963** (*#1
  benignitiM.*, the last line of ch. 25's summary *… benignitas.*; the vote had put `#1` on it); **3018** (*\iS*, the
  page number 388 of 460's head); **3053** (*REGVM LIBER IIIL*) and **3054** (*Cap. a$.*), the rest of 460's head
  (the vote had put them in mid-column 1).
- Added: `+ 459 1 900 % B b 2 tem-` (signature and catchword), `+ 460 1 900 % PARA-` (catchword for 1 Chronicles).
- No text line lost by the OCR.
- Text corrections beyond s for ſ, æ and spacing: 2925–28 *obsidionem venisset … obsessam,ve-nisset* (vote
  *obfidionemvenisfet … obfesfam,ve-nisfet*); 2921 *Iouam impie vixit* (vote *iouam impievixit*); 2933 *inde omnes tum*
  (vote *indeomnestmn*); 2938 *dictum* (vote *4di£him*); 2940 *millia, omnesque* (vote *millia,-omnesque*); 2943 *et
  proceribus* (vote *et/proceribus*); 2946 *fabrisque* (vote *febris*); 2948 *bellum* (*belluni*); 2950 *tem* (*7
  rem*); 2957 *Ieremiæ filiam* (*jIeremiaeHiiam*); 2958 *Iouam* (*iouam*); 2986 *de*
  (*d«*); 3006 *vineas* (*vinea*); 3007 *Columnas* (*Columna*); 3008 *lacum* (*Iacum*); 3009 *æde* (*ede*); 3016
  *columnas … bases* (*base*); 3020 *immensum* (*iramenfura*); 3021 *eubitus* (*cubitus*: the vote had corrected the
  misprint); 3022 *capitello æ-* (*ae-*); 3033 *ctus* (*dhis*); 3035 *parebant* (*parcbant*); 3041 *regem* (*i-egem*);
  3042 *Hemathensium* (*Hemathcnfium*); 3044 *eo-* (*co-*); 3045 *reliquerat, Godoliam* (*reliquerat,GodoIiam*); 3046
  *Ahichami … Saphanis* (*Ahicliami … Saphani»*); 3051 *eum* (*cum*); 3052 *Nathaniæ* (*Nathani.e*); 3055 *Careæ*
  (*Cereae*); 3064 *Nathaniæ* (*Nathaniac*); 3065 *samæ* (*faraae*); 3068–69 *occide-ret* (*occide-rer*), *ma-*
  (*ma-a*); 3079 *eumque* (*cumque*); 3080 *solium* (*folium*); 3081–82 *so-lia* (*fo-lia*); 3083 *eius* (*cius*); 3084
  *que … conuicto-* (*one … conuidto-*; the q's tail is faint on the page, but it is *que*); 3085 *rem* (*rein*); 3086
  *menso … penu aluit* (*menfo … penualuit*). 3072 *autem*: the e is under an ink blot on the page; read by the sense
  and 1750.

## Wording doubts (1738 against 1750)

- **24:15–16 (2946–47)**: 1738 *fabrisque et opificibus mille, omnibus denique, quorum vires …*; 1750 *fabris et
  opificibus mille, omnibusque denique, quorum vires …* (the *-que* moved). The page is clear: 1738 kept.
- **25:16 (3021)**: 1738 *eubitus* (misprint), 1750 *cubitos*.
- **25:22 (3046)**: 1738 *Ahichami*, 1750 *Achicami*.
- Smaller: 1750 *hos inquam* (1738 *hos, inquam,*); 1750 *Ismaël* twice (1738 *Ismael*, no diaeresis, zoomed both);
  1750 *âc ex*, *à*, *ità* (1738 *ac*, *a*, *ita*, unaccented); 1750 *vt eos e suo*. Otherwise 1750 agrees word for
  word.

## Omission check (against the BSB/KJV)

Every verse 24:9–25:30 checked clause by clause: nothing the page has is lost in the reading, and the page has every
clause of the English (24:13 the gold vessels cut in pieces *confregit aurea vasa*, "as the LORD had said"; 24:14 ten
thousand captives, craftsmen and smiths, "none remained, except the poorest" *relicta sola plebe*; 24:16 the seven
thousand and the thousand; 25:4 the gate between the two walls by the king's garden; 25:13 pillars, stands, the sea;
25:14–15 pots, shovels, snuffers, spoons, firepans, bowls; 25:17 the capital three cubits, network and
pomegranates; 25:19 the officer, five men of the king's presence, the scribe of the host, sixty men; 25:23 all four
captains with their fathers' names; 25:27 the year, month and day). 25:3 has *nono die mensis* with no month: the
Hebrew names none here either (the KJV's "fourth" is supplied in italics); 25:14 *instrumenta musica* for the
Hebrew's snuffers is Castellio's rendering. The only missing or wrong words were the vote's.

## Summary

- Rows written: 167 (165 of the range's 171, plus 2 added); header + 167 lines.
- Changed from the vote: 138 rows (mostly s for ſ, æ, verse numbers, spacing and OCR repairs).
- Removed: 6 (2917, 2918, 2963, 3018, 3053, 3054). Added: 2 (`%` signature/catchword rows).
- Text ends at **2 Kings 25:30** (1738 = KJV), leaf 460 col. 1 line 70, *diu vixit.*; then an ornament and the
  catchword *PARA-*.
