# Joshua 1–24, stages 1–2: 1738 read on the page, line by line, with Wikisource as a witness

Proposed 2026-11-18 (decision 68's route, as Deuteronomy: `data/review/deut1-34-stage2.md`; decision 30's standing
rule). Nathan: "Pull, then start work on Joshua", then "Go all the way through stage 5 before stopping to ask for my
input".

## The route, and why

Wikisource has all 24 chapters of Joshua (its 5 verses missing aside: 15:1, 15:23, 18:24, 24:17, 24:28), so the book
was first drafted from it, the Leviticus 1–11 way (`pipeline draft Josh 1-24`). Collated with 1738's OCR, that draft
showed **80 verses the OCR covers under 60%**, and Wikisource's Joshua turned out **not to be a faithful copy of
1738**: besides its typos (*trajectururos, vestari, digressism, antirent, infgendes, exterminanarunt*), it respells
throughout (*allocutus, quicquid, loquutus, persequuti, haereditatem, Moyses, unquam, sylvestris*) where 1738 prints
*adlocutus, quidquid, locutus, persecuti, hereditatem, Moses, vmquam, siluestris*, and differs in wording (2:7
*insequebantur* for 1738's *insecuti sunt*, 4:14 *fecerant* for *timuerant*, 7:12 *sacrilegum* for *sacrilegium*, 10:19
*Ipsius* for *Ipsis*). So every printed line of 1738 was read on the page (decision 68's route, which also gives the
printed text, stage 2b, with every word read), and **Wikisource served as an independent witness** to catch the readers'
slips. The Wikisource draft was set aside (`pipeline draft Josh 1-24 --from-ocr` builds `text/draft/JOS.usfm` from
the read lines). Wikisource supplied no text of the edition, only this check.

## Stage 1

- **Base**: the 1738 Leipzig edition (decision 1), **leaves 267 (col. 0, line 42: *CAPVT I.*, below Deuteronomy 34's
  left column) – 292 (col. 1, line 52, *ephraimitico.*, above Judges' title)** of its hOCR (archive.org
  bibliasacraexseb01cast). Running head *IOSVA*.
- `ocrdraft.make_lines` (1738's OCR line by line, voted with 1750 and the 1726 OCR `TXT/1 - OCR/Vetus Fœdus/josua.txt`)
  → `data/witnesses/read-1738/Josh1-24.voted.tsv` (2,455 rows: 2,431 printed lines and 24 `\c` rows).
- **Set right by hand**, each seen in the OCR's leaf and the page:
  - **Six chapter numerals misread**: *CAPVT 1III.* had come out as chapter 3 (row 270/0/16, set to **4**), *XL* as 40
    (278/0/36 → **11**), *xir.* as 41 (279/0/30 → **12**), *XXL* as 30 (287/1/7 → **21**), *XXIL* as 29 (288/1/77 →
    **22**), *XXIIL* as 28 (290/0/37 → **23**). With them wrong, `make_lines` had dropped chapters 11, 12 and 21–23 and
    taken in Judges 1; it was run again unfiltered and cut by hand.
  - **Leaf 267**: the right column's lines 23–40 (Deuteronomy 34:7–12, *nos natus centum et viginti* … *edidit
    Israelitis.*) dropped; Joshua 1:1–6 is the left column's lines 45–65, 1:6–7 the right column's 66–89.
  - **Leaf 292**: Joshua 24:24–33 is col. 0 lines 4–28 and col. 1 lines 29–52; Judges' title (col. 1, 53) and Judges
    1 (col. 0 from 55, col. 1 from 71) dropped.
  - **Row 1170** (*ginta.*, the last word of 12:24, *tri-|ginta*): the OCR listed it among column 0's lines; it is the
    last line of column 1 on leaf 279, so it was moved after row 1220 (reader 4).
- **Verse starts** found in the margins by the OCR: few, and mostly wrong (chapter 10 four behind, chapter 15 tagged
  1–12 for 1–63, 19:32–51 read as 21–37): the readers set every one again.

## Stage 2: every line read on the page (2026-11-18)

- **Read** on the page images (`ocrdraft.reading_sheets`, 174 sheets of 14 lines, each line's crop under its OCR
  text; the labels drawn with Deuteronomy's `-gravity NorthWest` fix, `archive.py` not touched) by eight readers in
  parallel (sheets 1–22, 23–44 … 155–174; rows 3–313, 314–624, 625–935, 936–1246, 1247–1556, 1557–1868, 1869–2179,
  2180–2456), under Deuteronomy's conventions: words and punctuation as 1738 prints them (s for ſ, & and q; expanded,
  æ/œ, u/v and i/j as printed, no accents; footnote letters and asterisks dropped; running heads, catchwords,
  signatures and footnotes kept as `%` rows), verse starts where the margin number and the sense put them; where the
  margin is cut or in the gutter, by Wikisource's verse openings (only its first four words were shown, so its
  wording stayed an independent check), the KJV and 1750. → `data/witnesses/read-1738/Josh1-24.tsv`, every changed
  row in `Josh1-24.corrections.tsv`. The readers' notes: `josh1-24-stage2-readers.md`.

| | |
|---|---:|
| printed lines read (leaves 267–292) | 2,431 |
| rows changed by the reading | 1,883 |
| `%` rows (heads, signatures, catchwords, two footnotes, one summary line) | 11 |
| verses (1738's numbering) | 656 (the KJV: 658) |

Every chapter's numbers run 1… in order, none missing or doubled. 1738's counts against the KJV's: **6: 28/27**, **21:
42/45**, the rest the KJV's count (clause-level differences listed in the readers' notes).

**Placed by sense where the margin is cut or in the gutter** (each row in the readers' notes): 1:2–6; 2:17–24 (the
units digit only); 3:2–3; 4:10–24; 5:2–12; 6:22–28; 7:3–14; 8:11–35; 10:21; 11:5–23; 12:2–4; 13:15–33; 14:1–8;
15:15–43 and the digit fragments of 15:44–63; 16:2–4; 17:16–18; 18:8–18; 20:1–9; 21:37–42; 22:1–18; 23:4–16;
24:2–8 and 24:28–33. **15:20–23**: Wikisource runs its 15:20 through *Iagur* and has no 23; the page begins each town
of the list on a new line or after a wide gap, and with the KJV gives 21 *quorum*, 22 *Cina*, 23 *Cedes*, 24 *Ziph*.

**First letters lost in the gutter**, completed from the sense and 1750 (each in the readers' notes): leaf 267 col. 0
(rows 7–23), 271 col. 0 (367–390), 273 col. 0 (569–585), 275 col. 0 (755–786), 279 col. 0 (1163–1178), 281 col. 0
(1329–1375), 285 col. 0 (1735–1769), 287 col. 0, 288 col. 1, 289 col. 0, 291 col. 0 (2310–2355). Leaf 290's right
column is cut at the line ends (rows 2268–2284, from 1750).

**Lost lines**: none. Each reader checked its columns for printed text lines without a row; what has none is chapter
headings and summaries, running heads, catchwords and signatures.

## Checked by Claude against Wikisource and 1750

The read lines were compared with Wikisource word by word (u/v, i/j, æ/ae and case folded), and each difference with
1750's OCR aligned to the same verse: **352 differences**. 128 are Wikisource's respellings (above); 140 have 1750
with the reading; Wikisource's five missing verses are on the page. **The 84 where 1750 sides with Wikisource or is
silent or garbled were looked at on the page** (crops of each line, the doubtful letters enlarged), with 13 spellings
1750 does not confirm. **Two readers' slips found and set right** in the read lines and the corrections file:

- **9:4 *resartos*** (row 807; reader: *refartos*): long s, no crossbar, enlarged (leaf 275); *resarciō*, patched.
- **14:9 *su-|um*** (row 1381; reader: *fu-*): long s, enlarged (leaf 281).
- And **1:1 *in hunc modum*** (row 7; reader *In*, from the OCR): the first letter is lost in the gutter; 1750 has
  *in hunc modum*, and the sense runs on (*adlocutus est in hunc modum:*).

The rest stand as read, among them against Wikisource and 1750: 4:14 ***timuerant*** (both *fecerant*; *sicut antea
Mosem timuerant*, leaf 270), 13:30 *regni* (both *regi*), 18:4 *hereditatum*, 18:16 *gigantium*, 19:9 *ducta*, 15:35
*Azeca*, 15:57 *Gabaa*, 15:59 *Bethanoth*, 16:10 *Gazerenses*, 19:22 and 21:16 *Bethsemem*, 21:14 *Lebnam*,
*Estemoam*, 24:23 *adpellite*; against Wikisource: 1:3 *Mosi*, 2:7 *insecuti sunt*, 2:8 *tectum adscendit*, 4:15
*oracu-|li arcam*, 7:12 *sacrilegium*, 10:19 *Ipsis*, 12:2 *Sehon*, 12:22 *Iacha-|nanæ*, 15:9 *Nephtoæ*, 15:54 *Sior*, 15:55
*Iota.*, 19:43 *Thamnatha*, 19:50 *Thamnathsa-|ram*, 21:12 *Chale-|bo*, 24:30 *Thannathseræ*, and *submœnia*, *immo*,
*litorea*, *prœlio*, *Gazæ* (all seen). Every *f* where Wikisource has *s* checked: 8:21 *fumo*, 17:14 *sortis*, 19:1
*sors* are Wikisource's slips.

**Misprints, seen on the page** (kept in the read lines and the printed text, decision 58; corrected below for the
reading edition): 7:21 *auimaduertisset* (a turned n), 8:10 *antem*, 13:25 *eorumqne*, 15:31 *Scſenna* (an open c,
no bar, beside the barred e's of *Medemena*, enlarged), 18:1 *terrra*, 18:20 *circumſeripta* (an e with its bar,
unlike the word's two c's, enlarged), 22:3 *manda-|datum*, 22:5 *to-|que* (for *totoque*: the syllable lost at the line
break; 1750 *to que*).

**Printed spellings to keep in mind** (the printed text has them; the edited text's stage 3 decides): *submœnia*
(2:15; Gaffiot has neither *submœnia* nor *summœnia*), *quessitis* (24:32, Wikisource *quaesitis*), *Thannathseræ*
(24:30) beside *Thamnathsaram* (19:50), *Chalebo* (21:12) beside *Calebo*, *Iota.* (15:55), *Sior* (15:54).

**Castellio's marks**: 16:10 ***G.** donec Pharao Aegypti rex expeditionem fecit, urbemque cepit ac igni cremavit, et
Chananaeos et Pherezaeos Gazerensesque confodit, urbemque filiae suae dotis nomine dedit. **H.***: the Septuagint's
addition (Brenton's text, `sources/parallel/lxx`: *ἕως ἀνέβη Φαραὼ βασιλεὺς Αἰγύπτου, καὶ ἔλαβεν αὐτὴν … καὶ ἔδωκεν
αὐτὴν Φαραὼ ἐν φερνῇ τῇ θυγατρὶ αὐτοῦ*), between his *G.* (Greek) and *H.* (back to the Hebrew), as Gen 44:6. Kept in the printed
text; in the edited text the marks are dropped and the words kept, as the settled Gen 44:6 and Lev 18:17 (below). A
light footnote (decision 56) is a candidate for the notes pass.

**1738's footnotes** (rows kept as `%`, not text): 7:1 *a) idem Achor et Achan est.* (leaf 273) and 22:34 *a) hoc est,
testis.* (leaf 290, the altar *Ed*). Candidates for the notes pass.

## Versified (decision 5; decision 30's standing rule), 2026-11-18

29 edits in `data/versification/Josh1-24.draft.edits.tsv` (14 merges, 14 splits, one range), made by Claude chapter by
chapter beside the KJV from the readers' mappings, each boundary read in the Latin; applied to the draft (`versify
Josh --draft --apply`, run on `Josh.draft.edits.tsv`, then renamed by its span, as Deuteronomy's) and to the printed
text (`orig Josh 1-24 --read-lines` reads the same file). Only verse markers move. Checked: the words unchanged in both
files, every chapter at the KJV's count (658 verses; 656 rows, 4:15–17 one), the draft and the printed text with the
same verse ids and the same words in every verse (15:31 aside, the misprint corrected below).

Deuteronomy's principles: the count is fixed, not every boundary; a drift is fixed at both ends by a split and a merge;
where 1738 begins a verse a clause off the KJV and the numbering holds, Castellio's division stands (1:10–11, 2:8–9,
2:22–24, 7:2–3, 8:16, 8:30–31, 9:19, 10:23–24, 11:1–2, 11:7–9, 13:2–3, 13:6–7, 13:12–13, 14:10–11, 15:2–6,
21:13–14, 21:21–22, 22:1–2, 22:7–8).

- **4**: split 1 (KJV 2 at *ut homines duodecim*), merge 3 (KJV 3); **4:15–17 a verse range**: Castellio's *Igitur
  Josua ex Jovae mandato sacerdotibus oraculi arcam ferentibus jussit, ut ex Jordane exirent:* condenses the KJV's
  15 (the LORD spake), 16 (Command the priests) and 17 (Joshua commanded) into one clause, which no split divides;
  numbered `15-17`, as Deut 14:16–17. Merges 22 (KJV 23) and 24 (KJV 24).
- **5**: split 2 (KJV 3 at *factis cultris*: KJV 2 'the LORD said unto Joshua' is *Eo tempore Josua, ex Jovae
  mandato,*), merge 6 (KJV 6).
- **6**: merge 27 (KJV 26, the curse on Jericho's builder in two of Castellio's verses).
- **7**: merge 22 (KJV 21, Achan's confession), split 23 (KJV 23 at *ea inde capiunt*).
- **10**: split 7 (KJV 8 at *et a Jova admonitus*), merge 11 (KJV 11, the hailstones).
- **19**: merge 10 (KJV 9), split 11 (KJV 11 at *Inde ad mare*).
- **21** (the Levites' cities; 1738 groups them by tribe, 42 verses for the KJV's 45): splits 23, 28, 29, 34, 35,
  36, 38, 39, 42 and merges 25, 31, 34, 38, 39, 42 cut the list where the KJV's verses begin (*Ajalonem*, *Jerimoth*,
  *Helcath*, *Damna*, *Cedemotha*, *Hesebon*, *Levitarum oppida*, *eaque omnia*, *nulla prorsus*). Castellio has
  Reuben's cities (KJV 21:36–37, which some Hebrew manuscripts lack) at his 35.

## Stage 2b: the printed text

`python -m pipeline orig Josh 1-24 --read-lines` → `text/orig/draft/JOS.usfm` (every word from the read lines, in the
KJV's numbering) and `data/orig/Josh.pages.tsv` (each verse's leaf, for the site's link). The book's first word stays
in capitals as printed (*POSTQVAM*, as Deuteronomy's *ORATIO*); the chapters' drop-capital words are normal words
(decision 76). Paragraphs: 1738's indents as `archive.indents` reads them (33), **not yet checked on the page**, as
Numbers' and Deuteronomy's. The title is the edited text's *Jōsua* in both files (1738's running head *IOSVA*;
the settled *Jōsua* 30 times). **Approved for now** 2026-11-19 (Nathan: "Approve it for now"): rebuilt, identical to
the draft, moved to `text/orig/JOS.usfm` (`data/review/josh-orig.md`).

## Corrections for the reading edition (stage 2)

Kept as printed in the read lines and the printed text (decision 58); corrected in the draft for the reading edition.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-18)

1. **Josh 1:15** *servoMose … cisIordanem*: printed without spaces (tight justification, leaf 268); two words each,
   and *Jordanem* in the draft's j (the u/v and i/j step skips a word run on to another).
    **Apply:** `Josh.1.15` la: `a Jovae servoMose tributam cisIordanem ad` → `a Jovae servo Mose tributam cis Jordanem ad`
2. **Josh 7:21** *auimaduertisset* → *animadvertisset* (1738's turned n, leaf 273; Wikisource *animadvertisset*).
    **Apply:** `Josh.7.21` la: `in praeda avimaduertisset egregiam` → `in praeda animadvertisset egregiam`
3. **Josh 8:10** *antem* → *autem* (leaf 274; 1750 and Wikisource *autem*).
    **Apply:** `Josh.8.10` la: `Josua antem, illa nocte` → `Josua autem, illa nocte`
4. **Josh 13:25** *eorumqne* → *eorumque* (leaf 280; 1750 *eorumque*).
    **Apply:** `Josh.13.25` la: `eorumqne fines` → `eorumque fines`
5. **Josh 15:31** *Scsenna* → *Sesenna* (leaf 282; 1750 *Sefenna*, Wikisource *Sesenna*; Hebrew סַנְסַנָּה). The
   names reader decides the form in stage 3–5.
    **Apply:** `Josh.15.31` la: `Medemena, Scsenna,` → `Medemena, Sesenna,`
6. **Josh 16:10** Castellio's *G. … H.* marks dropped, the words kept, as the settled Gen 44:6 and Lev 18:17; the
   stop before *G.* a comma, since *donec* runs on from *sed tributarii*.
    **Apply:** `Josh.16.10` la: `sed tributarii. G. donec Pharao` → `sed tributarii, donec Pharao`
    **Apply:** `Josh.16.10` la: `dotis nomine dedit. H.` → `dotis nomine dedit.`
7. **Josh 18:1** *terrra* → *terra* (leaf 284).
    **Apply:** `Josh.18.1` la: `ab eis terrra, oraculi` → `ab eis terra, oraculi`
8. **Josh 18:20** *circumseripta* → *circumscripta* (leaf 285, enlarged).
    **Apply:** `Josh.18.20` la: `terminis circumseripta.` → `terminis circumscripta.`
9. **Josh 22:3** *mandadatum* → *mandatum* (leaf 288, *manda-|datum*; 1750 *man-|datum*).
    **Apply:** `Josh.22.3` la: `vestri mandadatum curastis` → `vestri mandatum curastis`
10. **Josh 22:5** *toque* → *totoque* (leaf 288–289, *to-|que*: *hunc toto corde totoque animo colatis*, Hebrew
    בְּכָל־לְבַבְכֶם וּבְכָל־נַפְשְׁכֶם; Wikisource *totoque*).
    **Apply:** `Josh.22.5` la: `toto corde toque animo` → `toto corde totoque animo`
11. **Josh 21:2** *inChananæa*: printed without a space (read line 287/1, row 1971; found by the stage 3–5 reader of
    18–21); two words (Wikisource *in Chananaea*).
    **Apply:** `Josh.21.2` la: `apud Siluntem inChananaea demonstrarunt` → `apud Siluntem in Chananaea demonstrarunt`
12. **Josh 22:11** *exaduersum* → *exadversum*: 1738 prints *exaduersum* (the read line has it); the draft's u/v step
    missed a consonantal u after the prefix *ex-ad-* (as Deut 4:9 *aduertite*). Found by the stage 3–5 reader of 22–24.
    **Apply:** `Josh.22.11` la: `Jordanis exaduersum Israelitis` → `Jordanis exadversum Israelitis`

## Names: one spelling per person, place and people (stage 3–5, 2026-11-19)

From the names readers (`josh1-24-names.md`): one form per person, place and people (decision 46), the settled
spelling first, else Joshua's own commoner spelling; 1738's misprinted names corrected. The printed text keeps
1738's. Kept as Castellio spells them, though one place: Jokneam (12:22 *Jachananæ*, 19:11 *Jeconam*), Taanach
(12:21 *Thenaci*, 21:25 *Thanach*, 17:11 *Tanacenses*): his transliterations differ, and one spelling would need
case forms he never prints (hard calls in `josh1-24-stages3-5.md`).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

13. **Josh 2:1** *Setimo* → *Sittimo*: Shittim (הַשִּׁטִּים): the settled spelling, Num 25:1 *Sittīmō*, 33:49 *Sittīmōrum*; 1738 *Setimo* follows the Vulgate's *Setim* (hard call 1) (Claude, 2026-11-19)
    **Apply:** `Josh.2.1` la: `Setimo` → `Sittimo`
14. **Josh 3:1** *Setimo* → *Sittimo*: Shittim: as 2:1 (Claude, 2026-11-19)
    **Apply:** `Josh.3.1` la: `Setimo` → `Sittimo`
15. **Josh 11:1** *Someronis* → *Semeronis*: Shimron (שִׁמְרוֹן): Joshua's own *Semeron* (19:15, the same town of Zebulun) and *Semeromeronis* (12:20) (hard call 7) (Claude, 2026-11-19)
    **Apply:** `Josh.11.1` la: `Someronis` → `Semeronis`
16. **Josh 12:5** *Salecham* → *Salcham*: Salecah (סַלְכָה): the settled spelling, Deut 3:10 *Salcham* (Claude, 2026-11-19)
    **Apply:** `Josh.12.5` la: `Salecham` → `Salcham`
17. **Josh 12:5** *maachathaeos* → *maachataeos*: Maacathites: the settled Deut 3:14 *Maachātis* (t, not th) (hard call 4) (Claude, 2026-11-19)
    **Apply:** `Josh.12.5` la: `maachathaeos` → `maachataeos`
18. **Josh 12:17** *Thaphuae* → *Taphuae*: Tappuah (תַּפּוּחַ, the town whose king Joshua took), one spelling within Joshua, as 16:8 and 17:8 *Taphua*, 15:53 *Bethtaphua* (T, not Th) (Claude, 2026-11-19)
    **Apply:** `Josh.12.17` la: `Thaphuae` → `Taphuae`
19. **Josh 12:22** *Cadis* → *Cedis*: Kedesh (קֶדֶשׁ): Joshua's own *Cedes* (15:23, 19:37, 21:32; *Cedesam* 20:7), genitive; *Cadis* reads as Kadesh (קָדֵשׁ, the settled *Cadēs*), another place (hard call 3) (Claude, 2026-11-19)
    **Apply:** `Josh.12.22` la: `Cadis` → `Cedis`
20. **Josh 13:3** *Acharonis* → *Accaronis*: Ekron (עֶקְרוֹן): Joshua's own *Accaron* (15:11, 15:45, 15:46, 19:43) and *accaronensis* in this verse (hard call 2) (Claude, 2026-11-19)
    **Apply:** `Josh.13.3` la: `Acharonis` → `Accaronis`
21. **Josh 13:11** *Salecham* → *Salcham*: Salecah: as 12:5 (Claude, 2026-11-19)
    **Apply:** `Josh.13.11` la: `Salecham` → `Salcham`
22. **Josh 13:11** *maachathaeosque* → *maachataeosque*: Maacathites: as 12:5 (Claude, 2026-11-19)
    **Apply:** `Josh.13.11` la: `maachathaeosque` → `maachataeosque`
23. **Josh 13:13** *Maachathaeisque* → *Maachataeisque*: Maacathites: as 12:5 (Claude, 2026-11-19)
    **Apply:** `Josh.13.13` la: `Maachathaeisque` → `Maachataeisque`
24. **Josh 13:18** *Jassa* → *Jasa*: Jahaz (יַהְצָה): the settled *Jāsam* (Num 21:23), *Jāsā* (Deut 2:32), and Joshua's own 21:36 *Jasa* (Claude, 2026-11-19)
    **Apply:** `Josh.13.18` la: `Jassa` → `Jasa`
25. **Josh 13:18** *Cedemothia* → *Cedemotha*: Kedemoth (קְדֵמֹת): Joshua's own 21:37 *Cedemotha*, the settled Deut 2:26 *Cedēmōthis*; the extra i a misprint or a stray form (hard call 5) (Claude, 2026-11-19)
    **Apply:** `Josh.13.18` la: `Cedemothia` → `Cedemotha`
26. **Josh 13:20** *Bethphogor* → *Bethphegor*: Beth-peor (בֵּית פְּעוֹר): the settled Deut 34:6 *Bēthphegōr* (and *Phegōr-*, *Baalphegōre*); 1738's *phogor* follows the Greek Βαιθφογώρ (hard call 6) (Claude, 2026-11-19)
    **Apply:** `Josh.13.20` la: `Bethphogor` → `Bethphegor`
27. **Josh 15:4** *Asemonem* → *Asmonem*: Azmon (עַצְמוֹנָה), one place two spellings: the settled Num 34:4 *Asmōnem* (Claude, 2026-11-19)
    **Apply:** `Josh.15.4` la: `Asemonem` → `Asmonem`
28. **Josh 15:7** *Adumim* → *Adommim*: Adummim (אֲדֻמִּים), one spelling within Joshua, as 18:17 *Adommim* (the Hebrew's doubled m; Vulgate *Adommim* both times) (Claude, 2026-11-19)
    **Apply:** `Josh.15.7` la: `Adumim` → `Adommim`
29. **Josh 15:14** *Sesaim* → *Sesaeum*: Sheshai (שֵׁשַׁי), one person: the settled Num 13:22 *Sēsæus*, in the accusative (Claude, 2026-11-19)
    **Apply:** `Josh.15.14` la: `Sesaim` → `Sesaeum`
30. **Josh 15:14** *Tholmaim* → *Thalmaeum*: Talmai (תַּלְמַי), one person: the settled Num 13:22 *Thalmæus*, in the accusative (Claude, 2026-11-19)
    **Apply:** `Josh.15.14` la: `Tholmaim` → `Thalmaeum`
31. **Josh 15:28** *Hazersual* → *Hasersual*: Hazar-shual (חֲצַר שׁוּעָל), one spelling within Joshua, as 19:3 *Hasersual* (s for tsade as *Hasergadda*, *Hasersusa*) (Claude, 2026-11-19)
    **Apply:** `Josh.15.28` la: `Hazersual` → `Hasersual`
32. **Josh 15:29** *Ezem* → *Asem*: Azem (עָצֶם, the same town of Simeon), one spelling within Joshua, as 19:3 *Asem* (s for tsade as *Hasor*) (Claude, 2026-11-19)
    **Apply:** `Josh.15.29` la: `Ezem` → `Asem`
33. **Josh 15:30** *Harma* → *Horma*: Hormah (חָרְמָה), one place two spellings: the settled Num 14:45 *Hormam*, as 19:4 *Horma* (Claude, 2026-11-19)
    **Apply:** `Josh.15.30` la: `Harma` → `Horma`
34. **Josh 15:32** *Aen* → *Ain*: Ain (עַיִן, the same town of Simeon), one spelling within Joshua, as 19:7, 21:16 *Ain* and the settled Num 34:11 *Ainis* (Claude, 2026-11-19)
    **Apply:** `Josh.15.32` la: `Aen` → `Ain`
35. **Josh 15:33** *Sarea* → *Saraa*: Zorah (צָרְעָה), one spelling within Joshua, as 19:41 *Saraa* (Claude, 2026-11-19)
    **Apply:** `Josh.15.33` la: `Sarea` → `Saraa`
36. **Josh 15:34** *Taphna* → *Taphua*: Tappuah (תַּפּוּחַ: patah, doubled p, shureq), a turned letter: 1738 prints *Taphna* (leaf 282, col. 1, line 94, seen), as 1554 (canvas 132), 1573 (canvas 165, both seen) and 1750, but no source seen has an n, and Castellio spells the same Hebrew name with u in all six other places (*Taphua* 12:17, 16:8, 17:8 twice; *Bethtaphua* 15:53; *Entaphua* 17:7); the Vulgate *Taphua*. The printings descend one from another, so their agreement shows only that the letter was never corrected. The printed text keeps *Taphna* (decision 58). First withdrawn (the page's n, and Judah's Tappuah not Ephraim's: but Judah's Beth-tappuah, 15:53, is *Bethtaphua*); restored on reconsideration (Nathan, 2026-11-19: "Are you sure it holds up?", then "Yes, Taphūa"; `josh1-24-names.md` §"Evidence re-checked", 4) (Claude, 2026-11-19)
    **Apply:** `Josh.15.34` la: `Taphna` → `Taphua`
37. **Josh 15:41** *Macceda* → *Maceda*: Makkedah (מַקֵּדָה), one place two spellings within Joshua: as 10:10, 10:16–29, 12:16 *Maceda*, *Macedam* (seven times) (Claude, 2026-11-19)
    **Apply:** `Josh.15.41` la: `Macceda` → `Maceda`
38. **Josh 15:42** *Assan* → *Asan*: Ashan (עָשָׁן, the same town given to Simeon), one spelling within Joshua, as 19:7 *Asan* (Claude, 2026-11-19)
    **Apply:** `Josh.15.42` la: `Assan` → `Asan`
39. **Josh 15:48** *Jatthir* → *Jattir*: Jattir (יַתִּיר, the same town given to the Levites), one spelling within Joshua, as 21:14 *Jattir* (Claude, 2026-11-19)
    **Apply:** `Josh.15.48` la: `Jatthir` → `Jattir`
40. **Josh 15:60** *Cariathiarim* → *Cariathjarim*: Kirjath-jearim: j for the consonant, as 15:9 *Cariathjarimum*, 18:14, 18:15 (Claude, 2026-11-19)
    **Apply:** `Josh.15.60` la: `Cariathiarim` → `Cariathjarim`
41. **Josh 16:5** *Atarothaddar* → *Atarothadar*: Ataroth-addar (עַטְרוֹת אַדָּר), one spelling within Joshua, as 18:13 *Atarothadar* (and 15:3 *Adar*, the settled Num 34:4 *Hazaradār*) (Claude, 2026-11-19)
    **Apply:** `Josh.16.5` la: `Atarothaddar` → `Atarothadar`
42. **Josh 17:2** *Esriele* → *Asriele*: Asriel (אַשְׂרִיאֵל), one person: the settled Num 26:31 *Asrīēl* (Claude, 2026-11-19)
    **Apply:** `Josh.17.2` la: `Esriele` → `Asriele`
43. **Josh 17:3** *Salphadus* → *Salphaadus*: Zelophehad (צְלָפְחָד), one person: the settled Num 26:33 *Salphaādus* (Claude, 2026-11-19)
    **Apply:** `Josh.17.3` la: `Salphadus` → `Salphaadus`
44. **Josh 17:3** *Melcha* → *Melca*: Milcah (מִלְכָּה), one person: the settled Num 26:33, 27:1 *Melca* (Claude, 2026-11-19)
    **Apply:** `Josh.17.3` la: `Melcha` → `Melca`
45. **Josh 17:7** *Machmatam* → *Machmetam*: Michmethah (הַמִּכְמְתָת), one spelling within Joshua, as 16:6 *Machmetam* (Claude, 2026-11-19)
    **Apply:** `Josh.17.7` la: `Machmatam` → `Machmetam`
46. **Josh 17:11** *Magedonenses* → *Mageddonenses*: Megiddo (מְגִדּוֹ, the Hebrew's dagesh), one place two spellings within Joshua: as 12:21 *Mageddonis* (Claude, 2026-11-19)
    **Apply:** `Josh.17.11` la: `Magedonenses` → `Mageddonenses`
47. **Josh 18:13** *Lusae* → *Luzae*: Luz (לוּזָה), one place two spellings: the settled Gen 48:3 *Lūzæ*, as 16:2 *Luzam* (Claude, 2026-11-19)
    **Apply:** `Josh.18.13` la: `Lusae` → `Luzae`
48. **Josh 18:25** *Beerota* → *Berotha*: Beeroth (בְּאֵרוֹת, the Gibeonite town), one place two spellings within Joshua: as 9:17 *Berotha* (N1's *Bērōtha*; the settled *Bērōthīs*, Deut 10:6) (Claude, 2026-11-19)
    **Apply:** `Josh.18.25` la: `Beerota` → `Berotha`
49. **Josh 18:26** *Caphara* → *Caphira*: Chephirah (כְּפִירָה), one place two spellings within Joshua: as 9:17 *Caphira* (the Hebrew's hireq-yod) (Claude, 2026-11-19)
    **Apply:** `Josh.18.26` la: `Caphara` → `Caphira`
50. **Josh 19:25** *Halcath* → *Helcath*: Helkath (חֶלְקַת, the same town given to the Levites), one spelling within Joshua, as 21:31 *Helcath* (Claude, 2026-11-19)
    **Apply:** `Josh.19.25` la: `Halcath` → `Helcath`
51. **Josh 19:27** *Jephthaelis* → *Jephthahelis*: Jiphthah-el (יִפְתַּח־אֵל), one spelling within Joshua, as 19:14 *Jephthahelis* (Claude, 2026-11-19)
    **Apply:** `Josh.19.27` la: `Jephthaelis` → `Jephthahelis`
52. **Josh 20:8** *Bosor* → *Beser*: Bezer (בֶּצֶר), the city of refuge: the settled Deut 4:43 *Beser* (the same verse's list) (Claude, 2026-11-19)
    **Apply:** `Josh.20.8` la: `Bosor` → `Beser`
53. **Josh 21:12** *Chalebo* → *Calebo*: Caleb, one person: the settled *Calebō* (Num 14:30), as 15:13, 15:18 *Calebo* (Claude, 2026-11-19)
    **Apply:** `Josh.21.12` la: `Chalebo` → `Calebo`
54. **Josh 21:23** *Gabathonem* → *Gebbethonem*: Gibbethon (גִּבְּתוֹן, the same town of Dan), one spelling within Joshua, as 19:44 *Gebbethon* (Claude, 2026-11-19)
    **Apply:** `Josh.21.23` la: `Gabathonem` → `Gebbethonem`
55. **Josh 21:34** *Jecanam* → *Jeconam*: Jokneam (יָקְנְעָם, the same town of Zebulun), one spelling within my chapters, as 19:11 *Jeconam* (12:22 has *Jachananae*: see the notes) (Claude, 2026-11-19)
    **Apply:** `Josh.21.34` la: `Jecanam` → `Jeconam`
56. **Josh 21:36** *Bosor* → *Beser*: Bezer: as 20:8, the settled Deut 4:43 *Beser* (Claude, 2026-11-19)
    **Apply:** `Josh.21.36` la: `Bosor` → `Beser`
57. **Josh 21:39** *Jaser* → *Jazer*: Jazer (יַעְזֵר), one place two spellings: the settled Num 21:32, 32:3, 32:35 *Jazēr* (Claude, 2026-11-19)
    **Apply:** `Josh.21.39` la: `Jaser` → `Jazer`
58. **Josh 24:30** *Thannathserae* → *Thamnathserae*: Timnath-serah (תִּמְנַת־סֶרַח, the same Hebrew as 19:50), one spelling within Joshua: the Hebrew's mem (*Thamn-*, as 19:50) and segol (*-ser-*, as 1738 here and 1573's *Thānathserę*, canvas 171, seen). First proposed as *Thamnathsarae* after 19:50; revised with item 65 (Nathan, 2026-11-19: "Apply all seven") (Claude, 2026-11-19)
    **Apply:** `Josh.24.30` la: `Thannathserae` → `Thamnathserae`
59. **Josh 24:32** *Josephaeis* → *Josepheis*: Josephites, one people two spellings: the settled Deut 27:12 *Jōsēphēī* (as 18:11 *Josepheos*) (Claude, 2026-11-19)
    **Apply:** `Josh.24.32` la: `Josephaeis` → `Josepheis`

## Names revised after the evidence was re-checked (2026-11-19)

From `josh1-24-names.md` §"Evidence re-checked" (Nathan asked for the evidence point by point, then "Apply all seven").
The printed text keeps 1738's spellings.

**Decision:** accept (Nathan, 2026-11-19: "Apply all seven")

62. **Josh 12:22** *Jachananae* → *Jeconam*: Jokneam (יָקְנֳעָם). 1738's *Iacha-|nanæ* is a misprint for Castellio's
    *Iachanamæ* (1573 canvas 164, seen; 1554 canvas 130, OCR; Wikisource *Jachanama*: the Hebrew's final m); and one
    spelling for one town, as 19:11 and 21:34 *Jeconam*, indeclinable here (*rēx Jeconām*): the Hebrew's o (qamets
    hatuf) and final qamets (Claude, 2026-11-19)
    **Apply:** `Josh.12.22` la: `Jachananae` → `Jeconam`
63. **Josh 12:21** *Thenaci* → *Thanach*: Taanach (תַּעְנַךְ patah, patah, final soft k), one spelling within Joshua, as
    21:25 *Thanach* (1554, 1573, 1738), indeclinable as there (the Vulgate *rex Thanach*); *Thenaci* is Castellio's
    in every printing (Claude, 2026-11-19)
    **Apply:** `Josh.12.21` la: `Thenaci` → `Thanach`
64. **Josh 17:11** *Tanacenses* → *Thanachenses*: the men of Taanach: as 21:25 *Thanach*, -ēnsis (Claude, 2026-11-19)
    **Apply:** `Josh.17.11` la: `Tanacenses` → `Thanachenses`
65. **Josh 19:50** *Thamnathsaram* → *Thamnathseram*: Timnath-serah: the Hebrew's segol (סֶרַח), as 24:30 (item 58)
    (Claude, 2026-11-19)
    **Apply:** `Josh.19.50` la: `Thamnathsaram` → `Thamnathseram`

## Found in stages 3–5 (2026-11-19)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

60. **Josh 22:16, 22:17** *respublica* → *res publica*: two words, as the settled text (*rēs pūblica*) and Gaffiot
    write it (found by the proofreader of 18–24); the printed text keeps 1738's one word.
    **Apply:** `Josh.22.16` la: `universa Jovana respublica.` → `universa Jovana res publica.`
    **Apply:** `Josh.22.17` la: `Jovana respublica vulnus` → `Jovana res publica vulnus`

61. **Josh 7:12, 7:13** *sacrilegium* → *sacrilegum* (the guilty man, not the sacrilege): 1738 prints *ſacrilegium*
    in both verses (leaf 273, rows 576, 580, seen; 1750 the same), but 7:13 *sacrilegium esse inter Israelitas, ante
    quem … sublatum* leaves *quem* nothing to agree with. **1573** (MDZ bsb10141277, canvas 160, OCR) prints
    *nisi de medio vestri ſacrilegum ſustulerits* (7:12) and *ſacrilegum eſſe inter Iſraelitas, ante quem de ſuorum
    numero ſublatum, non poterunt* (7:13), with the margin note *Sacrilegum puniri*; Wikisource *sacrilegum* in both.
    Castellio's word restored in both verses for the reading edition; the printed text keeps 1738's. A call for
    Nathan (`josh1-24-stages3-5.md`).
    **Apply:** `Josh.7.12` la: `vestri sacrilegium sustuleritis` → `vestri sacrilegum sustuleritis`
    **Apply:** `Josh.7.13` la: `dicere, sacrilegium esse` → `dicere, sacrilegum esse`

**Kept as 1738 prints it**, though 1573 differs: **4:14** *sicut antea Mosem timuerant* (1573 canvas 158 *fecerant*,
1750 and Wikisource the same): 1738's verb reads well (they feared him as they had feared Moses) and the base edition's
reading stands (decision 1); recorded in `docs/editions.md`.
