# Numbers 1–36, stages 1–2: 1738 read on the page, line by line (no Wikisource text)

Proposed 2026-11-16 (decision 68's route, as Leviticus 12–27: `data/review/lev12-27-stage2.md`; decision 30's
standing rule). Nathan: "Start Numbers", "Yes, read 1–36", "Yes, versify Numbers", "Add verse ranges".
**Versified to the KJV, chapter 7 with a verse range (below); stages 3–5 not run.**

- **Base**: the 1738 Leipzig edition (decision 1), leaves 187 (col. 1) – 227 (col. 0) of its hOCR (archive.org
  bibliasacraexseb01cast). Wikisource's *Numeri* page has only 1:0–1:1, so the whole book is 1738's own.
- **Stage 1** (`ocrdraft.make_lines`, leaves 187–227, chapters 1–36): 1738's OCR line by line, voted with 1750 and
  the 1726 OCR → `data/witnesses/read-1738/Num1-36.voted.tsv` (3,885 rows). Set right by hand: *CAPVT XXV 111.* had
  come out as a second chapter 25 (row 3002, set to 28); Deuteronomy 1's opening on leaf 227 (*\c 1* and after)
  cut off.
- **Stage 2**: **every line read on the page images** (`ocrdraft.reading_sheets`, 275 sheets of 14 lines, each line's
  crop under its text), by eight readers in parallel (sheets 1–35, 36–70 … 246–275; rows 3–496, 497–991, 992–1485,
  1486–1979, 1980–2473, 2474–2968, 2969–3463, 3464–3886), words and punctuation as 1738 prints them (s for ſ, æ/œ,
  u/v and i/j as printed, no accents; footnote letters and asterisks dropped; running heads, chapter summaries,
  catchwords and footnotes kept as `%` rows) → `data/witnesses/read-1738/Num1-36.tsv`, every changed, moved or added
  row in `Num1-36.corrections.tsv`. The readers' own notes, verse by verse where 1738's numbers differ from the
  KJV: `num1-36-stage2-readers.md`.
- **Checked by Claude after the merge**: two sheets read again independently (88: rows 1232–1245, 12:9–14; 232:
  rows 3266–3280, 30:16–31:6; 28 lines): no difference in words or marks (31:6, a margin in the gutter, placed by
  the sense as the reader did). The merged text compared with 1750's OCR word by word: no run of 1750's words
  missing (what differs is 1750's summaries, running heads and OCR noise).

## The numbers

| | |
|---|---:|
| printed lines read (leaves 187–227) | 3,849 rows + 91 added |
| rows changed by the reading | 2,993, and 2 moved |
| verses (1738's numbering) | 1,221 (the KJV: 1,288) |

## Lines the OCR lost, read on the page by Claude (91 rows added)

The OCR had glued these lines onto other rows (the readers took the strays out) or not seen them at all; none was
on a sheet. Read on 1738's page from crops of the column (`archive.sheet`), and added after the row named:

- 3:42 (after row 304, leaf 190): *vt erat a Ioua iussus, omnium Is- / raelitarum primogenitorum cen-*. The first
  letter is a *u* shape, its left stroke not inked; read *vt*, 1738's form at a line's start (*vt* 65 times, *ut* once
  in Leviticus 12–27's read lines).
- 7:36 *rietes sexaginta, capri sexaginta,* (after 777); 8:2 *quum lucernas accenderet,* (after 790); 8:18
  *Israelitarum primogenitis desumsi,* (after 838); 8:19 *raelitis attribui, qui Israelitarum* (after 839).
- 20:26 *eius filio induito, Aharone illic* (after 2187); 21:3, six lines from *funditus euersuros. Quibus a Io-* to
  *runt.* (after 2209); 21:5–6 *vilem fastidire. Quapropter im- / misit in populum Ioua presteres ser- / pentes,
  quibus homines mordenti-* (after 2218); 22:19 *cte manerent : se autem sciscitatu- / rum, ecquid sibi iterum Ioua
  dice-* (after 2399).
- **28:1–8**, all of leaf 218 col. 0 above row 3003 (23 lines, from *ITem Mosem Ioua adfatus est in* to
  *deliniatur.*, with the summary *Offerenda quæ, quo tempore …* as `%other`); 28:31's end *iusque fertum.*
  (after 3077).
- **31:1–2**, leaf 220 col. 1's foot (after the `\c 31` row): the summary (4 lines, `%other`), *ITem Mosi Ioua
  mandauit, vt / Madianitas Israelitarum nomine / vlcisceretur, postea ad suos*, catchword *popu-*.
- 32:42's end *nominauit.* (after 3572); 34:29 *Hi sunt, quibus Ioua præcepit, vt* (after 3750); 35:4–5 *le pateant
  cubitos, vt quum ex-* and catchword *tra* (after 3766).
- **35:14–20** (leaf 226 col. 0's foot, after 3798, 18 lines, *in Chananæa attribuetis, quibus* … *cito. Quod si eum
  per odium*) and **35:30–35** (leaf 226 col. 1's foot, after 3830, 17 lines, *ore testium occiditor homicida.* …
  *Israelitas habito.*).

Moved: row 1777 *clade.* (16:50's last line) after row 1827; row 2751 *genti.* (26:22) after row 2801. Spaced: row
1036 *cumHobaboRaguelis*, row 1236 *dixitMosi;* (type set tight, not word division). Rows 38–43 are Leviticus
27:33–34, misfiled by the OCR: kept as `%other`. Chapter summaries the OCR lost (2–5, 23–27, 29, 32–36) are not text
and were not added.

## Versified (decision 5; decision 30's standing rule)

138 edits in `data/versification/Num1-36.draft.edits.tsv` (first 55 for 1–12, 25 for 13–24, 35 for 25–36, by
three readers working chapter by chapter beside the KJV, and two by Claude at 5:20–21; then chapter 7's 24 and the
census ranges below, which took the place of 15 splits), applied to the draft and to the
printed text (`orig Num 1-36 --read-lines` reads the same file). Only verse and chapter markers move; checked: the
words are unchanged in both files, no verse is empty, and every chapter has the KJV's count (1,288 verses). The principles are Leviticus's: the count is fixed, not every boundary
(Castellio's division stands where his verse starts a few words off the KJV's: 5:12–13, 6:20, 8:20–26, 9:6–7,
11:1–5, 12:5, 12:9–10, 13:17–18, 15:19, 16:47–49, 21:14–16, 22:11, 22:24, 22:37, 24:2, 32:10–11, 34:16–19,
35:20–23, 4:20–22); a drift is fixed at both ends by a merge and a split; where the KJV has 'And the LORD spake
unto Moses, saying' the clause up to *inquit* or the verb of speaking is that verse (3:44, 4:17, 8:23, 16:23,
16:36, 20:7, 26:52, 31:25). **1738's 23:1 is the KJV's 22:41** (*Postridie vero Balaamum deduxit*): merge 23:2,
then the chapter break moved to *Tum Balaamus*; the draft's paragraph marks there set by hand (22:40 *misit,* runs
on into 41; \\p after \\c 23).

`versify.py` now takes an anchor in both spellings (`ut moneret|vt moneret`, tested), since the draft and the
printed text differ at the first letter in places (*ut/vt*, *unum/vnum*, *Jova/Ioua*, *quae/quæ*); used at 1:41,
3:45, 4:18, 5:21, 16:24, 16:37, 26:53, 31:26, 31:53.

**Condensed census, as verse ranges** (Nathan, 2026-11-16: "Yes, use ranges"): where Castellio gives in one clause what
the KJV has as two or more verses, a split would leave a one-word verse and a bare number. Those are ranges instead
(versify's `range`, below): the ten tribes of **1:22–43** (* 22-23 Simeonis quinquaginta novem millia trecenti.*,
24–25 Gad … 42–43 Naphtali; 1738's own *Josephi, | Ephraimitarum …* at 32–33 stays as it numbers it), **4:38–41**
(*Gersoniorum eadem ratione recensitorum summa fuit duo millia sexcenti triginta*) and **4:42–44** (*Merarensium item
tria millia ducenti. Haec summa est stirpis Merarensium,*). 15 splits gave way to 12 `range` rows (138 rows in the
file). Chapter 2's splits at *militum* / *milites* / *militibus* stay: 1738 sets the muster as its own verse itself
(2:4 *militum autem numerus recensitorum 74600.*), as the KJV does, and so 4:47–48 (*summa fuit octo millia …*).

### Chapter 7: a verse range, 12–83 (Nathan, 2026-11-16: "Add verse ranges")

Castellio gives the princes' offering once (his 12–17), *Haec, inquam, singuli obtulerunt* (18), then the twelve
princes one line each, day by day (19–30), and the totals (31–39). The KJV repeats the offering for each prince
(12–83, six verses a day). The words are in another order, so no moving of markers reaches the KJV's 89: his 19
(Nahshon, the first day) is the KJV's 12, his 12–17 the KJV's 13–17, his 20–30 the KJV's 18, 24, 30 … 78.

So 1738's 12–30 are one verse numbered **12–83** (USFM `\v 12-83`), and 31–39 go on as the KJV's 84–89: 31 = 84
(with 32's *scutellae argenteae duodecim … lances aureae totidem,*), 85 from *scutellae quidem centenariae* (with
33), 34–36 = 86–88 (37 *Haec fuit altaris jam inuncti dedicatio* joins 88), 38–39 = 89. 24 edits in the same file
(18 merges, `range Num.7.12 83`, a split and three merges). Numbers now has the KJV's 1,288 verses in every
chapter, in the draft and the printed text.

The pipeline reads a range everywhere (2026-11-16): `tsv.Verse`, a verse number that is its first number wherever
one is compared or counted, with `last`, printing `12-83` in ids and USFM and `12–83` on the page; versify's
`range` op; the parsers of `latex`, `publish`, `gold` (`parallel.parse_usfm(ranges=True)`; the parallel texts'
own ranges still read as their first verse), `orig`, `verses`, `normalize`, `collate`, `review`. Shown: the site's
number *12–83* and its parallel column with the KJV's 12–83 joined; the text files' ¹²–⁸³; the PDF's
`\VersusUsque{83}` (numbered 12–83, the running head marking 12); the citation *Num 7,12–83*. Tests added
(`test_versify`, `test_publish`). Built from the draft into a scratch folder (site, EPUB, TXT, PDF) to check.

### 1738's own numbers, before versifying

1738's margins differ from the KJV in most chapters; 1750 has the same numbers wherever its margin could be read.
Counts by chapter (1738 / KJV), the differing ones in bold:

**1: 51/54**, **2: 29/34**, **3: 50/51**, **4: 43/49**, 5–6 as the KJV (breaks differ at 5:12–13, 19–21; 6:20, 24–25),
**7: 39/89** (Castellio gives the twelve princes' offerings once, not twelve times), 8–12 as the KJV (breaks differ
in 8:24–26, 9:7, 9:19, 11:2–20, 12:5, 12:11), **13: 34/33** (splits KJV 3 at *viros scilicet omnes*), 14 (26–29 one
behind), 15 (16–19 one ahead), **16: 49/50**, 17 (11–13), **18: 32/32** but 27–30 one ahead, 19–21 (breaks differ),
**22: 40/41** and **23: 30/30** (1738's 23:1 is the KJV's 22:41, *POstridie*), 24–25, **26: 64/65**, 27, **28: 30/31**,
**29: 39/40**, **30: 17/16**, 31 (splits and merges), 32–34, **35: 35/34**, 36.

**Settled by Claude on the page**: 18:27–30, where two readers' ranges met and both wrote 27: 27 at *quum ab
Israelitis*, 28 at *Quod exceptitium*, 29 at *Ita excipietis*, 30 at *quæ maxime opima* (margins in the gutter;
the marks seen on leaf 207 col. 0 and 1750's margins 27, 28, 29, 30 agree; no number at *atque ex omnibus donariis*).

**Placed by sense where the margin is cut, in the gutter or a line off** (the readers' notes list each): 1:2,
2:10–29, 3:9–17, 3:40, 3:50, 4:12–21, 4:42; 5:27–6:10; 7:34–38 (7:37–38 by count only); 10 (most); 10:27–28
(printed a line low); 15:9–10; 16:29–40; 18:18–24; 20:10–24; 21:22; 22:4–9; 23:11–23 (the merge at 23:14 a guess);
25:8–18; 26:1–3, 26:32, 26:62–64; 27:7; 29:1–14, 29:25; 30:4–5; 31:3–17; 32:11–25; 36:1–5.

## Readings to note

Row numbers are the voted file's; verse numbers 1738's.

- 5:14 (rows 530, 532) *adfletur* twice, as printed (row 590 *adflatus*): **not a misprint**, the present subjunctive
  passive of *adflō* (*adflētur*, 'be breathed upon' by the spirit of jealousy), as 5:30's *adflatus*. Kept.
- 6:3 (row 602) *bibtto;*, a damaged *bibito*, and 30:17 (row 3264) *Atquæ*, a misprint for *Atque*: corrected for
  the reading edition below; the printed text keeps them (decision 58).
- 21:6 *presteres* (*prēstēr*, a fiery serpent), as printed; 34:8 (row 3705) *Hematham* (1750's OCR *Hemathan*).
- Castellio's *G. L. … H.* marks (rows 972, 974, 10:6) kept as printed in the read lines.
- Footnote rows (1202, 1252, 2181–2182, 2559–2561, 3228) read only as far as the crop shows; not text.

## Built from the read lines

- **The draft**: `pipeline draft Num 1-36 --from-ocr` → `text/draft/NUM.usfm` (1,221 verses, 1738's numbering, in
  Wikisource's conventions, the BSB's paragraphs).
- **Printed text (stage 2b)**: `pipeline orig Num 1-36 --read-lines` → `text/orig/draft/NUM.usfm`, with
  `data/orig/Num.pages.tsv`.

Both now in the KJV's numbering (above). **Next**: stages 3–5.

## Corrections for the reading edition, found in stages 3–5

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-16)

Kept as printed in the read lines and the printed text (decision 58); corrected in the draft for the reading edition.

1. **Num 6:3** *bibtto* → *bibito* (row 602; the i damaged on the page).
    **Apply:** `Num.6.3` la: `acetum ne bibtto;` → `acetum ne bibito;`
2. **Num 30:16** (1738's 30:17) *Atquae* → *Atque* (row 3264; 1738 *Atquæ*, a misprint).
    **Apply:** `Num.30.16` la: `Atquae haec quidem` → `Atque haec quidem`
3. **Num 10:6** *movento, G. L. Quum tertium; … ad septemtriones: H. eisque*: Castellio's *G. L. … H.* marks (the Greek's
   and the Latin's addition against the Hebrew: 1738 prints them in the text, rows 972, 974) dropped, the words kept,
   as Lev 18:17 and the settled Exod 28:34.
    **Apply:** `Num.10.6` la: `movento, G. L. Quum tertium` → `movento, Quum tertium`
    **Apply:** `Num.10.6` la: `ad septemtriones: H. eisque` → `ad septemtriones: eisque`
4. **Num 3:30** *Elisaphane* → *Elsaphane*: Elizaphan son of Uzziel, the same man as the settled Exod 6:22 *Elsāphān*
   and Lev 10:4 *Elsāphānem* (decision 46, one form per person; Nathan's "Yes, Elsāphānem" for Lev 10:4). 1738 prints
   *Elisa-|phane* (row 262, leaf 189); the printed text keeps it.
    **Apply:** `Num.3.30` la: `gentilitatum Elisaphane Ozielis` → `gentilitatum Elsaphane Ozielis`
5. **Num 16:47** *in quo iam clades ceperat* → *coeperat* ('where the plague had begun'; the verse before has *iamque
   clades incipit*). 1554 prints *clades cœpe-|rat* (MDZ bsb10196330, canvas 91) and 1726 *coeperat*; 1738 (leaf 205,
   col. 1, read enlarged 2026-11-16) and 1750 *ceperat*: a later printing's slip. Nathan, 2026-11-16: "correct clear
   errors in the edited edition"; the printed text keeps 1738's *ceperat*.
    **Apply:** `Num.16.47` la: `clades ceperat` → `clades coeperat`
6. **Num 28:7** *ut in sacro temetum Jova libetur* → *Jovae* (the dative: 'that the strong wine be poured to the
   LORD'). 1554 prints *temetum | Iouæ libetur* (canvas 98); 1738 (leaf 218, col. 0, read on the page) and 1750
   *Ioua*: a misprint the later printings share. Corrected as Nathan asked (2026-11-16), as Lev 10:1 *coram Jova*;
   the printed text keeps *Ioua*.
    **Apply:** `Num.28.7` la: `temetum Jova libetur` → `temetum Jovae libetur`

## Names: one form per person (decision 46)

**Decision:** accept (Nathan, 2026-11-16: "Decide 1 form for each person. If Gaffiot or L&S do not have that name (or a
similar analog), look at the Hebrew (and maybe Greek) to determine which form is best")

Corrected in the draft for the reading edition; the printed text keeps 1738's spellings (decision 58). Where 1738
prints one man two ways, one spelling (the Hebrew decides); where a person or clan is already settled (Gen 46, Exod 6,
14), the settled spelling. The full table, with the markings: `data/review/num1-36-names.md`.

1. **Num 1:6** *Surisadaei* → *Surisaddaei*: Zurishaddai: one spelling, -sadd- (Hebrew dagesh; as 7:12, 10:19) (Claude, 2026-11-16)
    **Apply:** `Num.1.6` la: `Surisadaei` → `Surisaddaei`
2. **Num 1:7** *Aminadabi* → *Amminadabi*: Amminadab: one form: settled Exod 6:23 *Ammīnādābī* (decision 46; Luke 3:33, Matt 1:4 have *Amīnādāb-*) (Claude, 2026-11-16)
    **Apply:** `Num.1.7` la: `Aminadabi` → `Amminadabi`
3. **Num 1:11** *Abidam* → *Abidan*: Abidan son of Gideoni (Benjamin): one spelling, *Abidan* as 2:22, 7:12, 10:24 (Hebrew nun; *Abidam* is Abida, Gen 25:4) (Claude, 2026-11-16)
    **Apply:** `Num.1.11` la: `Abidam` → `Abidan`
4. **Num 1:15** *Nepthaliana* → *Nephthaliana*: Naphtalite (tribe adjective): one spelling, as 13:14 *Nephthaliana* and the settled *Nephthālis* (Claude, 2026-11-16)
    **Apply:** `Num.1.15` la: `Nepthaliana` → `Nephthaliana`
5. **Num 1:15** *Ahira* → *Achira*: Ahira son of Enan (Naphtali): one spelling, *Achira* as 2:29, 7:12, 10:27 (Claude, 2026-11-16)
    **Apply:** `Num.1.15` la: `Ahira` → `Achira`
6. **Num 2:3** *Aminadabi* → *Amminadabi*: Amminadab: one form: settled Exod 6:23 *Ammīnādābī* (decision 46; Luke 3:33, Matt 1:4 have *Amīnādāb-*) (Claude, 2026-11-16)
    **Apply:** `Num.2.3` la: `Aminadabi` → `Amminadabi`
7. **Num 2:12** *Surisadaei* → *Surisaddaei*: Zurishaddai: one spelling, -sadd- (Hebrew dagesh; as 7:12, 10:19) (Claude, 2026-11-16)
    **Apply:** `Num.2.12` la: `Surisadaei` → `Surisaddaei`
8. **Num 2:20** *Phadassuris* → *Phadasuris*: Pedahzur: one spelling, *Phadasur* as 1:10, 10:23 (Hebrew single ṣade; the Greek Φαδασσούρ doubles it) (Claude, 2026-11-16)
    **Apply:** `Num.2.20` la: `Phadassuris` → `Phadasuris`
9. **Num 2:25** *Ammisadaei* → *Ammisaddaei*: Ammishaddai: one spelling, -sadd- as 1:12, 7:12, 10:25 (Claude, 2026-11-16)
    **Apply:** `Num.2.25` la: `Ammisadaei` → `Ammisaddaei`
10. **Num 3:18** *Semeis* → *Simeis*: Shimei son of Gershon: one spelling, the settled *Simeīm* (Exod 6:17) (Claude, 2026-11-16)
    **Apply:** `Num.3.18` la: `Semeis` → `Simeis`
11. **Num 3:19** *Jesaar* → *Isaar*: Izhar son of Kohath: one spelling, the settled *Isaār* (Exod 6:18, 21) as Num 16:1 *Isaāris* (Claude, 2026-11-16)
    **Apply:** `Num.3.19` la: `Jesaar` → `Isaar`
12. **Num 3:20** *Moolis* → *Moholis*: Mahli son of Merari: one spelling, the settled *Moholīm* (Exod 6:19) (Claude, 2026-11-16)
    **Apply:** `Num.3.20` la: `Moolis` → `Moholis`
13. **Num 3:21** *Semejana* → *Simejana*: Shimeite: founder settled *Simeī* (Exod 6:17 *Simeīm*); -ānus; the vowel before j unmarked (Claude, 2026-11-16)
    **Apply:** `Num.3.21` la: `Semejana` → `Simejana`
14. **Num 3:27** *Jesaariana* → *Isaariana*: Izharite: founder settled *Isaār* (Exod 6:18, 21; Num 16:1); -iānus (Claude, 2026-11-16)
    **Apply:** `Num.3.27` la: `Jesaariana` → `Isaariana`
15. **Num 3:33** *Mooliana* → *Moholiana*: Mahlite: founder settled *Moholī* (Exod 6:19 *Moholīm*); -iānus (Claude, 2026-11-16)
    **Apply:** `Num.3.33` la: `Mooliana` → `Moholiana`
16. **Num 7:12** *Elisaphus* → *Eliasaphus*: Eliasaph son of Deuel (Gad): one spelling, *Eliasaphus* as 1:14, 2:14, 10:20 (Hebrew אֶלְיָסָף) (Claude, 2026-11-16)
    **Apply:** `Num.7.12-83` la: `Elisaphus` → `Eliasaphus`
17. **Num 7:12** *Phadassuris* → *Phadasuris*: Pedahzur: one spelling, *Phadasur* as 1:10, 10:23 (Hebrew single ṣade; the Greek Φαδασσούρ doubles it) (Claude, 2026-11-16)
    **Apply:** `Num.7.12-83` la: `Phadassuris` → `Phadasuris`
18. **Num 7:12** *Achieser* → *Achiezer*: Ahiezer son of Ammishaddai (Dan): one spelling, *Achiezer* as 1:12, 2:25 (zayin, as the settled *Eliezer*) (Claude, 2026-11-16)
    **Apply:** `Num.7.12-83` la: `Achieser` → `Achiezer`
19. **Num 7:12** *Asserianorum* → *Aserianorum*: Asherite (tribe adjective): one spelling, the settled *Āsēr* (1:13, 2:27, 34:27 *Aseriana*) (Claude, 2026-11-16)
    **Apply:** `Num.7.12-83` la: `Asserianorum` → `Aserianorum`
20. **Num 10:18** *Elizur* → *Elisur*: Elizur son of Shedeur (Reuben): one spelling, as 1:5, 2:10, 7:12 *Elisur* (Claude, 2026-11-16)
    **Apply:** `Num.10.18` la: `Elizur` → `Elisur`
21. **Num 10:25** *Achieser* → *Achiezer*: Ahiezer son of Ammishaddai (Dan): one spelling, *Achiezer* as 1:12, 2:25 (zayin, as the settled *Eliezer*) (Claude, 2026-11-16)
    **Apply:** `Num.10.25` la: `Achieser` → `Achiezer`
22. **Num 10:26** *Asserianae* → *Aserianae*: Asherite (tribe adjective): one spelling, the settled *Āsēr* (1:13, 2:27, 34:27 *Aseriana*) (Claude, 2026-11-16)
    **Apply:** `Num.10.26` la: `Asserianae` → `Aserianae`
23. **Num 13:13** *Asseriana* → *Aseriana*: Asherite (tribe adjective): one spelling, the settled *Āsēr* (1:13, 2:27, 34:27 *Aseriana*) (Claude, 2026-11-16)
    **Apply:** `Num.13.13` la: `Asseriana` → `Aseriana`
24. **Num 21:32** *Jaser* → *Jazer*: Jazer: one spelling, *Jazer* as 32:1, 3, 35 (Hebrew zayin); Greek Ἰαζήρ η (Claude, 2026-11-16)
    **Apply:** `Num.21.32` la: `Jaser` → `Jazer`
25. **Num 26:15** *Haggi* → *Hagi*: Haggi son of Gad: one form, the settled Gen 46:16 *Hagīm* (Hebrew חַגִּי in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.15` la: `ab Haggi` → `ab Hagi`
26. **Num 26:15** *Haggia* → *Hagia*: Haggite: founder Haggi as settled Gen 46:16 *Hagīm*; -ius (Claude, 2026-11-16)
    **Apply:** `Num.26.15` la: `Haggia` → `Hagia`
27. **Num 26:17** *Arieli* → *Areeli*: Areli son of Gad: one form, the settled Gen 46:16 *Areēlīm* (Hebrew אַרְאֵלִי in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.17` la: `ab Arieli` → `ab Areeli`
28. **Num 26:17** *Arielia* → *Areelia*: Arelite: founder Areli as settled Gen 46:16 *Areēlīm* (Claude, 2026-11-16)
    **Apply:** `Num.26.17` la: `Arielia` → `Areelia`
29. **Num 26:23** *Phua* → *Phuva*: Puvah son of Issachar: one form, the settled Gen 46:13 *Phuvam* (Hebrew פֻּוָּה in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.23` la: `a Phua` → `a Phuva`
30. **Num 26:23** *Phuana* → *Phuvana*: Punite: founder Puvah as settled Gen 46:13 *Phuvam*; -ānus (Claude, 2026-11-16)
    **Apply:** `Num.26.23` la: `Phuana` → `Phuvana`
31. **Num 26:24** *Simbrone* → *Simerone*: Shimron son of Issachar: one form, the settled Gen 46:13 *Simerōnem* (Hebrew שִׁמְרֹן in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.24` la: `Simbrone` → `Simerone`
32. **Num 26:24** *Simbronia* → *Simeronia*: Shimronite: founder Shimron as settled Gen 46:13 *Simerōnem* (Claude, 2026-11-16)
    **Apply:** `Num.26.24` la: `Simbronia` → `Simeronia`
33. **Num 26:26** *Saredo* → *Seredo*: Sered son of Zebulun: one form, the settled Gen 46:14 *Seredum* (Hebrew סֶרֶד in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.26` la: `Saredo` → `Seredo`
34. **Num 26:26** *Saredina* → *Seredina*: Seredite: founder Sered as settled Gen 46:14 *Seredum*; -īnus (Nathan) (Claude, 2026-11-16)
    **Apply:** `Num.26.26` la: `Saredina` → `Seredina`
35. **Num 26:26** *Jalele* → *Jahele*: Jahleel son of Zebulun: one form, the settled Gen 46:14 *Jahēlem* (Hebrew יַחְלְאֵל in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.26` la: `Jalele` → `Jahele`
36. **Num 26:26** *Jalelina* → *Jahelina*: Jahleelite: founder Jahleel as settled Gen 46:14 *Jahēlem*; -īnus (Nathan) (Claude, 2026-11-16)
    **Apply:** `Num.26.26` la: `Jalelina` → `Jahelina`
37. **Num 26:38** *Bala* → *Bela*: Bela son of Benjamin: one form, the settled Gen 46:21 *Belam* (Hebrew בֶּלַע in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.38` la: `a Bala` → `a Bela`
38. **Num 26:38** *Balana* → *Belana*: Belaite: founder Bela as settled Gen 46:21 *Belam*; -ānus (Claude, 2026-11-16)
    **Apply:** `Num.26.38` la: `Balana` → `Belana`
39. **Num 26:38** *Azbele* → *Asbele*: Ashbel son of Benjamin: one form, the settled Gen 46:21 *Asbēlem* (Hebrew אַשְׁבֵּל in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.38` la: `Azbele` → `Asbele`
40. **Num 26:38** *Azbelina* → *Asbelina*: Ashbelite: founder Ashbel as settled Gen 46:21 *Asbēlem*; -īnus (Nathan) (Claude, 2026-11-16)
    **Apply:** `Num.26.38` la: `Azbelina` → `Asbelina`
41. **Num 26:40** *Balae* → *Belae*: Bela son of Benjamin: one form, the settled Gen 46:21 *Belam* (Claude, 2026-11-16)
    **Apply:** `Num.26.40` la: `Balae` → `Belae`
42. **Num 26:40** *Ardes* → *Aredus*: Ard son of Bela: one form, the settled Gen 46:21 *Aredum* (Hebrew אַרְדְּ in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.40` la: `Ardes` → `Aredus`
43. **Num 26:40** *Ardiana* → *Arediana*: Ardite: founder Ard as settled Gen 46:21 *Aredum*; -iānus (Claude, 2026-11-16)
    **Apply:** `Num.26.40` la: `Ardiana` → `Arediana`
44. **Num 26:44** *Jemna* → *Imma*: Imnah son of Asher: one form, the settled Gen 46:17 *Immam* (Hebrew יִמְנָה in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.44` la: `a Jemna` → `a Imma`
45. **Num 26:44** *Jemnana* → *Immana*: Imnite: founder Imnah as settled Gen 46:17 *Immam*; -ānus (Claude, 2026-11-16)
    **Apply:** `Num.26.44` la: `Jemnana` → `Immana`
46. **Num 26:44** *Jessui* → *Isvi*: Ishvi son of Asher: one form, the settled Gen 46:17 *Isvīm* (Hebrew יִשְׁוִי in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.44` la: `a Jessui ` → `a Isvi `
47. **Num 26:44** *Jessujana* → *Isviana*: Ishvite: founder Ishvi as settled Gen 46:17 *Isvīm*; -ānus (Claude, 2026-11-16)
    **Apply:** `Num.26.44` la: `Jessujana` → `Isviana`
48. **Num 26:44** *Bria* → *Beria*: Beriah son of Asher: one form, the settled Gen 46:17 *Berīa*, *Berīam* (Hebrew בְּרִיעָה in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.44` la: `a Bria` → `a Beria`
49. **Num 26:44** *Briana* → *Beriana*: Beriite: founder Beriah as settled Gen 46:17 *Berīa*; -ānus (Claude, 2026-11-16)
    **Apply:** `Num.26.44` la: `Briana` → `Beriana`
50. **Num 26:45** *Briae* → *Beriae*: Beriah son of Asher: one form, the settled Gen 46:17 *Berīa*, *Berīam* (Hebrew בְּרִיעָה in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.45` la: `Briae` → `Beriae`
51. **Num 26:46** *Saram* → *Seram*: Serah daughter of Asher: one form, the settled Gen 46:17 *Seram* (Hebrew שָׂרַח in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.46` la: `Saram` → `Seram`
52. **Num 26:48** *Jessiele* → *Jaseele*: Jahzeel son of Naphtali: one form, the settled Gen 46:24 *Jaseēlem* (Hebrew יַחְצְאֵל in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.48` la: `Jessiele` → `Jaseele`
53. **Num 26:48** *Jessielina* → *Jaseelina*: Jahzeelite: founder Jahzeel as settled Gen 46:24 *Jaseēlem*; -īnus (Nathan) (Claude, 2026-11-16)
    **Apply:** `Num.26.48` la: `Jessielina` → `Jaseelina`
54. **Num 26:48** *Guni* → *Cuni*: Guni son of Naphtali: one form, the settled Gen 46:24 *Cūnīm* (Hebrew גּוּנִי in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.48` la: `a Guni` → `a Cuni`
55. **Num 26:48** *Guniana* → *Cuniana*: Gunite: founder Guni as settled Gen 46:24 *Cūnīm*; -iānus (Claude, 2026-11-16)
    **Apply:** `Num.26.48` la: `Guniana` → `Cuniana`
56. **Num 26:49** *Sellemo* → *Sillemo*: Shillem son of Naphtali: one form, the settled Gen 46:24 *Sillēmum* (Hebrew שִׁלֵּם in both) (Claude, 2026-11-16)
    **Apply:** `Num.26.49` la: `Sellemo` → `Sillemo`
57. **Num 26:49** *Sellemina* → *Sillemina*: Shillemite: founder Shillem as settled Gen 46:24 *Sillēmum*; -īnus (Nathan) (Claude, 2026-11-16)
    **Apply:** `Num.26.49` la: `Sellemina` → `Sillemina`
58. **Num 26:58** *Libnia* → *Lebnia*: Libnite: founder settled *Lebnī* (Exod 6:17 *Lebnīm*; Num 3:18, 21 *Lebn-*) (Claude, 2026-11-16)
    **Apply:** `Num.26.58` la: `Libnia` → `Lebnia`
59. **Num 26:58** *Moolia* → *Moholia*: Mahlite: founder settled *Moholī* (Exod 6:19 *Moholīm*) (Claude, 2026-11-16)
    **Apply:** `Num.26.58` la: `Moolia` → `Moholia`
60. **Num 26:59** *Jochabedam* → *Jacobedam*: Jochebed: one form, the settled Exod 6:20 *Jacobedam* (unmarked there by decision) (Claude, 2026-11-16)
    **Apply:** `Num.26.59` la: `Jochabedam` → `Jacobedam`
61. **Num 26:59** *Jochabeda* → *Jacobeda*: Jochebed: one form, the settled Exod 6:20 *Jacobedam* (unmarked there by decision) (Claude, 2026-11-16)
    **Apply:** `Num.26.59` la: `qua Jochabeda` → `qua Jacobeda`
62. **Num 27:1** *Melcha* → *Melca*: Milcah daughter of Zelophehad: one spelling, *Melca* as 26:33 and the settled *Melca* (Gen 22, same Hebrew מִלְכָּה, kaf with dagesh) (Claude, 2026-11-16)
    **Apply:** `Num.27.1` la: `Melcha` → `Melca`
63. **Num 33:7** *Magdal* → *Magdol*: Migdol: one form, the settled Exod 14:2 *Magdōl* (Claude, 2026-11-16)
    **Apply:** `Num.33.7` la: `Magdal` → `Magdol`
64. **Num 33:17** *Hazerothis* → *Haserothis*: Hazeroth: one spelling, *Haseroth* as 11:35, 12:1, 12:16 (Claude, 2026-11-16)
    **Apply:** `Num.33.17` la: `Hazerothis` → `Haserothis`
65. **Num 34:19** *Chalebus* → *Calebus*: Caleb son of Jephunneh: one spelling, *Calebus* as 13:6, 14:6 … (Hebrew כָּלֵב, kaf with dagesh) (Claude, 2026-11-16)
    **Apply:** `Num.34.19` la: `Chalebus` → `Calebus`
66. **Num 36:11** *Melcha* → *Melca*: Milcah daughter of Zelophehad: one spelling, *Melca* as 26:33 and the settled *Melca* (Gen 22, same Hebrew מִלְכָּה, kaf with dagesh) (Claude, 2026-11-16)
    **Apply:** `Num.36.11` la: `Melcha` → `Melca`
67. **Num 25:1** *in Cittimo* → *in Sittimo*: Shittim (Hebrew שִׁטִּים), where Israel abode; not Kittim (24:24). Castellio's
   1554 prints *in Sittimo commorantibus* (MDZ bsb10196330, canvas 96), and 1738 itself *Sittimorum* at 33:49: 1738's
   *Cittimo* here is a later printing's slip. Corrected in the edited text (Nathan accepted it, 2026-11-16); the printed
   text keeps *Cittimo*.
    **Apply:** `Num.25.1` la: `in Cittimo` → `in Sittimo`

