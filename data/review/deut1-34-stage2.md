# Deuteronomy 1–34, stages 1–2: 1738 read on the page, line by line (no Wikisource text)

Proposed 2026-11-17 (decision 68's route, as Numbers: `data/review/num1-36-stage2.md`; decision 30's standing rule).
Nathan: "Start Deuteronomy, the way Numbers was done" (stage 1 only, then stop and report), "Yes, read 1–34",
"Yes, versify Deuteronomy", "Yes, run stages 3–5".
**Stages 1 and 2 done; the draft and the printed text built and versified to the KJV (below); stages 3–5 run, with the corrections and names they found (below); settled for now 2026-11-18 (`text/DEU.usfm`).**

- **Base**: the 1738 Leipzig edition (decision 1), leaves 227 (col. 0, below Numbers 36) – 264 and 267 (cols. 0–1,
  above Joshua's title) of its hOCR (archive.org bibliasacraexseb01cast). Leaf 265 is a map (*MARE MAGNVM*, *EPHRAIM* in its OCR), 266
  blank. Wikisource's *Deuteronomium* page has only 1:1, so the whole book is 1738's own.
- **Stage 1** (`ocrdraft.make_lines`, leaves 227–264 and 267, chapters 1–34): 1738's OCR line by line, voted with
  1750 and the 1726 OCR (`TXT/1 - OCR/Vetus Fœdus/deuteronomium.txt`) → `data/witnesses/read-1738/Deut1-34.voted.tsv`
  (3,692 rows: 3,658 printed lines and 34 `\c` rows). Set right by hand, each read on the page (below).

## The numbers

| | |
|---|---:|
| printed lines (leaves 227–264, 267) | 3,658 |
| chapters | 34, in order |
| verse starts found in the margins (1738's or 1750's) | 573 of the KJV's 959 |

Verse starts found, by chapter (found / KJV): 1: 39/46, 2: 32/37, 3: 25/29, 4: 32/49, 5: 28/33, 6: 20/25, 7: 14/26,
8: 14/20, 9: 18/29, 10: 18/22, 11: 24/32, 12: 17/32, 13: 10/18, 14: 17/29, 15: 12/23, 16: 13/22, 17: 15/20, 18: 13/22,
19: 13/21, 20: 13/20, 21: 8/23, 22: 13/30, 23: 13/25, 24: 5/22, 25: 9/19, 26: 7/19, 27: 10/26, 28: 40/68, 29: 15/29,
30: 12/20, 31: 12/30, 32: 19/52, 33: 19/29, 34: 4/12. The readers set the rest in stage 2 (Numbers: 739 of 1,288).

## Leaf 227: Deuteronomy's opening, read on the page

Numbers ends at the top of leaf 227 (col. 1, *danem hierichuntium.*); under a rule comes the title
*DEVTERONOMIVM.*, then *CAPVT I.*, its summary (*Mosis ad populum concio. Præterita itinera, magistratus,
exploratores, facinora, clades.*: not text), and 1:1–7 in two columns: 11 lines on the left (the drop capital *O*
beside the first four) and 15 on the right, catchword *ca*, signature *L 4*. **Every one of the 26 lines is in the OCR
and in the voted file** (rows 227/0/67–77, 227/1/78–92); the Numbers rows above the title are not. The OCR had lost
or misplaced four things, set right by hand from the page:

- 1:1 *RATIO* → ***ORATIO***: the drop capital, which the OCR does not read (written with its word, as the readers do).
- 1:3: the margin's *3* had been read into the line (*3 Igitur*), and the verse start set a line early, at
  *Cadesbarneam.*: now `#3` before *Igitur*.
- 1:6–7: the margins put 6 beside *planare huiusmodi verbis: Ioua* and 7 beside *mansisse: iussitque*; the OCR had
  lost the 6 and set its `#6` at *iussitque*. Now `#6` before *Ioua Deus noster*, `#7` before *iussitque*
  (KJV 6 'The LORD our God spake unto us in Horeb', 7 'Turn you, and take your journey').

Chapter 1's verse numbers were then renumbered in sequence (the file's rule: `lines_tsv`).

## Set right by hand elsewhere

- **Two chapter numerals misread**: *C A P V T XXL* had come out as chapter 30 (row 250/0/4, set to **21**) and
  *CAPVT XXVIL* as 24 (row 255/0/22, set to **27**). *CAPVT xxxir.* (262/0/9) had no number and was counted to 32
  as it should be.
- **Deuteronomy 34:1–12's end is on leaf 267**, past the map: left column lines 4–22 (*ostendit Ioua totam
  Galaaditidem* … *Mortuus est an-*) and right column 23–40 (*nos natus centum et viginti* … *edidit Israelitis.*),
  then Joshua's title. The OCR orders the leaf column by column, so Joshua 1 (left column, 45–65) came between the two:
  Joshua's rows dropped, the right column's Deuteronomy lines put after the left's; row 267/0/1 (*rap. f .*, the
  running head *Cap. 1.*) dropped. **The gutter cuts the left column on this leaf**: the first letter or two of lines
  4–22 are partly lost on the image (*>stendit*, *lephthalcnfeni* for *Nephthalensem*, *nanasfenfem* for
  *Manassensem*, *njftraleni* for *australem* …), and the margin numbers 2–7 with them. For stage 2: read those lines
  with 1750 beside them (*ostendit*, *Nephthalensem* … are whole there) and set 34:2–7 by the sense and the KJV.
- **Lines glued across the columns** (the OCR read the two columns' lines as one; read on the page and split at the
  gutter, the halves put in their columns):
  - leaf 244, lines 46–53: the left column's 14:8–10 (*quoque, quoniam quum bisulcus sit,* … *rum esu abstinetote,
    eaque in im-*) glued onto the right column's 14:27–29 (*Leuitas quoque vestrates, qui par-* … *tem et hereditatem
    habent, peregri-*); line 48 had the right column's *non sunt, ne omittito.* glued onto the left's *Horum neque
    carne vescimini, ne-*. 16 rows now. The left column's margins 9 and 10 (*Aquatilium*, *At quæ*) and the right's
    28–29 were lost in the gluing: for stage 2.
  - leaf 254, line 77: the left column's 26:2 *sionem Deus vester Ioua dat,* (after the drop capital *Q* of *QVum*)
    glued onto the right column's 26:13 *abstuli, idque Leuitæ, peregrino,*. 2 rows now.

## Checked by Claude for lost lines (stage 1)

- **Gaps between lines**: every column of leaves 227–264 scanned for a space of a line or more between OCR lines.
  Besides the glued lines above, only footnotes (239/0/54, 242/0/105, 262/0/52: 1738's lettered notes, kept as rows
  for the readers to mark `%`, as in Numbers) and the heading on leaf 227.
- **Short column feet**: the nine columns whose text ends high (229/0, 230/1, 235/0, 237/0, 240/0, 243/1, 247/0,
  257/0, 259/0) seen on the page: a chapter heading and its summary (chapters 2, 3, 6, 8, 11, 14, 18) or footnotes
  (257, 259) below the last line. Nothing lost.
- **Against 1750's OCR**, word by word over the whole book: no run of 1750's text missing from the voted lines. What
  1750 has and 1738's lines do not is its chapter summaries, running heads and OCR noise; the places checked by hand
  (8:19 *hoc apud vos hodie testor*, 12:29–31, 33:11 *manuum operi faue: sic elumba*, 3:2–3 *et eum et omnes eius homines*) are
  all in the voted file, misread or in another line order in 1750's OCR.

Still for stage 2: the drop capitals of the other chapters (the OCR drops them or reads noise: *^"~x Vum* at 26:1),
every word (the voter's slips stand: 1:3 *eiulo* for *anno*, 1:2 *Scirem* for *Seirem*, 33:11 *sane … elumbe*), the
verse starts, and the footnote rows.

## Stage 2: every line read on the page (2026-11-17)

- **Read** on the page images (`ocrdraft.reading_sheets`, 262 sheets of 14 lines, each line's crop under its text), by
  eight readers in parallel (sheets 1–33, 34–66 … 232–262; rows 3–467, 468–932, 933–1399, 1400–1865, 1866–2333,
  2334–2801, 2802–3266, 3267–3693), words and punctuation as 1738 prints them (s for ſ, & and q; expanded, æ/œ, u/v
  and i/j as printed, no accents; footnote letters and asterisks dropped; running heads, chapter summaries, catchwords
  and footnotes kept as `%` rows), verse starts where the margin number and the sense put them →
  `data/witnesses/read-1738/Deut1-34.tsv`, every changed or added row in `Deut1-34.corrections.tsv`. The readers'
  notes, with 1738's numbers against the KJV chapter by chapter: `deut1-34-stage2-readers.md`.
- **The sheets** were made with ImageMagick through a copy of `archive._magick_sheet` that draws each label under an
  explicit `-gravity NorthWest` (`+4+5`): in ImageMagick 6 a `-gravity` set inside parentheses carries on, so from the
  second crop on the repo's version drew each label 21 px low, under the crop. The fix in `pipeline/archive.py` is
  left to Nathan (only Deuteronomy's files touched in this pass).
- **Checked by Claude after the merge**: two sheets read again independently (180: rows 2532–2545, 24:17–21; 240:
  rows 3380–3393, 32:2–6; 28 lines): no difference in words, marks or verse starts. The merged text compared with
  1750's OCR word by word: no run of 1750's words missing (what differs is 1750's summaries, running heads and OCR
  noise; 28:35 *ad verticem* found in row 2908). Every chapter's verse numbers run 1… in sequence, none doubled.

| | |
|---|---:|
| printed lines read (leaves 227–264, 267) | 3,658 rows + 1 added |
| rows changed by the reading | 2,869 |
| `%` rows (summaries, heads, catchwords, footnotes) | 26 |
| verses (1738's numbering) | 964 (the KJV: 959) |

**1738's counts against the KJV's** (the readers' notes give each chapter's mapping): **1: 47/46** (1738's chapter ends before the KJV's 1:46, which falls in its 2:1; 1:41–47 divided differently), 2: 37/37, **3: 30/29**, 4: 49/49, **5: 34/33** (1738 starts a verse
at *Locutus est autem*, KJV 5b), 6–15 as the KJV in count (breaks differ at 6:19, 7:3, 8:3–6, 8:20, 9:25–27, 11:3,
12:27, 13:13–15, 14:16–21, 14:25, 15:2), **16: 21/22** (1738's 21 *Lucum vllarum* is the KJV's 21–22; seen on leaf 246:
no 22 in the margin), 17–20 as the KJV, **21: 24/23**, 22–26 as the KJV in count (breaks differ at 22:19, 23:2–4,
25:17–19, 26:4–14), **27: 27/26**, 28: 68/68 (one or two ahead, KJV 68 split), 29: 29/29, **30: 21/20**, 31–34 as the
KJV (31:10, 31:15, 32:21, 32:33, 33:3 a few words off).

**Placed by sense where the margin is cut or in the gutter** (the readers' notes list each row): leaf 228 and 230 right
columns; 229 left (1:34–47; 1:42–46 least certain); 231 left (3:2–13); 232 right, 233 both, 236 right, 237 left (7:18–26);
parts of 239–241; 247 and 249 left (20:2–7 from 1750 and the sense); 251 and 253 left; 255 left (26:16–27:7, no digit
showing: from 1750 and the 1726 OCR's numbers); 256 right; 257 left; 259 left; 260 right; 261 left (31:8–18); 263 left
(32:28–43; 32:33 at *quibus vuæ felleæ*, with 1750); 267 left (34:2–7, by the sense and the KJV). Doubtful
placements: 4:49 (*qui idem*), 6:19, 11:3 (*extentum brachium*), 18:11 (*Pythii*), 29:26 (*eisque*; 1726 has it at
the line's start).

**First letters lost in the gutter, completed from the sense and 1750** (each listed in the readers' notes): leaf 233
left (rows 561–577, 15 lines), 255 left (rows 2712–2730), 257 left (rows 2902–2928; 2924 *stirpabitur*, 2928
*ærugo* doubtful), 267 left (rows 3657–3675, 19 letters; 3670 *uus*, the stem showing u, where 1750 has *vus*).

## Lines the OCR lost, read on the page by Claude (1 row added)

- **32:43's end, *cabitur.*** (leaf 263, col. 0, line 54; after row 3515): the column's last line, *suorum terræ pla- /
  cabitur.*, which the OCR had taken for a catchword (a short line at the column's foot), so stage 1 left it out. The
  right column's *tur,* below *prosternun-* is the catchword (leaf 264 begins *tur, eo de tuis dictis*).

The readers found no other text line without a row. What they list as lost is chapter headings and summaries, running
heads, catchwords and footnotes, not text (as in Numbers, not added). The hand splits of stage 1 checked on the whole
page by the readers: leaf 244 (rows 1636–1643, 1687–1694) and leaf 254 (rows 2622, 2672) each have their own
column's line.

**Joined in the read lines** (as Numbers 21:8–9): 1738 breaks four words at a line's end with no hyphen; a hyphen
written so that the draft and the printed text join them: rows 139–140 *Ca-|lebo* (1:35), 143–144 *Io-|uæ* (1:36),
2985–2986 *mol-|lis* (28:55), 3211–3212 *ve-|stro* (30:14).

## Readings to note

Row numbers are the voted file's, verse numbers 1738's; all kept as printed in the read lines and the printed text (decision 58), and read
enlarged on the page by Claude (2026-11-17); for the reading edition, stages 3–5:

- 980 *haberitis* (8:3, for *haberetis*); 1078 *iustititiam* (9:6); 1831 *collocandc* (16:11, for *collocando*: the
  last letter open like a c); 2016 *cis* (18:18, for *eis*); 2333 *calumnietnr* (22:16, a turned u); 2406
  *abhorrerote* (23:7, for *abhorretote*); 2438 *mrcedem* (23:18, for *mercedem*).
- Spellings as printed, not misprints: *prœlium* (rows 306, 330), *requietem* (409), *aerem* in two letters (528),
  *Sigorim* (34:3), lower-case *amorræo*, *hesebonium*, *ægyptiæ*; 33:28 *rore* (1750 the same).
- Footnote rows (1170, 1469, 3415 …) and the 26 `%` rows: not text.

## Built from the read lines

- **The draft**: `pipeline draft Deut 1-34 --from-ocr` → `text/draft/DEU.usfm` (964 verses, 1738's numbering, in
  Wikisource's conventions, the BSB's paragraphs).
- **Printed text (stage 2b)**: `pipeline orig Deut 1-34 --read-lines` → `text/orig/draft/DEU.usfm`, with
  `data/orig/Deut.pages.tsv`.

## Versified (decision 5; decision 30's standing rule), 2026-11-18

45 edits in `data/versification/Deut1-34.draft.edits.tsv` (21 merges, 22 splits, one chapter break, one range), made
by Claude chapter by chapter beside the KJV from the readers' mappings (`deut1-34-stage2-readers.md`, "1738's verse
numbers vs the KJV"), each boundary read in the Latin; applied to the draft (`versify Deut --draft --apply`, run on
`Deut.draft.edits.tsv`, then renamed by its span as Numbers') and to the printed text (`orig Deut 1-34 --read-lines`
reads the same file). Only verse and chapter markers move. Checked: the words unchanged in both files, no verse empty,
every chapter at the KJV's count (959 verses), the draft and the printed text with the same verse ids and the same
number of words in every verse. The anchor at 28:4 gives both spellings (*advenientes|aduenientes*), as do 2:1,
2:2, 3:25, 8:6, 16:21, 25:17 and 26:7.

The principles are Numbers' and Leviticus's: the count is fixed, not every boundary. A drift is fixed at both ends by
a split and a merge; where 1738 begins a verse a clause off the KJV and the numbering holds, Castellio's division
stands: 2:5 (*Sese enim*, after *ne eos infestaretis*), 2:18 (ends with *et propius ad Ammonitas accessurus*),
2:22, 2:25, 3:22, 6:19, 7:3, 7:19, 8:20, 11:3, 12:27, 13:13–15, 14:25, 15:2, 16:17, 17:3, 18:11, 19:18, 19:21,
20:17, 21:4, 21:22–23, 22:14–19, 26:10–11, 26:13–14, 27:10, 28:10, 28:52, 28:64–67, 29:26, 30:10, 30:19–20, 31:10,
31:15, 32:21, 32:33, 33:3. Where the KJV has 'And the LORD spake unto me, saying', the clause up to the verb of
speaking is that verse (2:2 *Tum Jova me monuit,*; 2:17 *adlocutus est me Jova.*; 3:23 *Tunc etiam Jovam Dominum
oravi,*), as Numbers 3:11.

- **1:41–2:1**: 1738's 42 and 44 join 41 and 43 (KJV 41–42); **KJV 1:46 'So ye abode in Kadesh many days' is the
  opening clause of 1738's 2:1** (*Quumque multo maximam vestrae morae partem fuissetis apud Cadem:*): the chapter
  break moved to *reversi contendimus*, mid-sentence, so `\nb` follows `\c 2` in the draft (set by hand after
  versify relayed the BSB's `\p` there; Exodus 7:1 and 8:1 are settled the same way).
- **2**: split 2 (KJV 3 at *ut quoniam*), merge 4 (KJV 4), split 16 (KJV 17), merge 19 (KJV 19).
- **3**: merges 14 (KJV 13 *totam scilicet Argobiam*) and 22 (KJV 20 *tum demum*), split 25 (KJV 24 at *ut
  (postquam*).
- **4**: split 3 at *quum vos, qui* (KJV 4; no number on the page), merge 6 (KJV 6). **5**: merge 6 (*Locutus est
  autem in hunc modum:* ends KJV 5).
- **8**: merge 3 (KJV 2), split 6 at *Quare ejus* (KJV 6). **9**: split 25 at *eumque his verbis* (KJV 26), merge 27.
- **14:16–17, a verse range** (as Numbers 1:22–43, Nathan's "Yes, use ranges"): Castellio's 16–17 name the ten birds
  of the KJV's 16–18, not one for one (*cuculo, bubone, noctua, ibi, pelicano* | *mergo, ciconia, ardeolarum
  generibus, pico, et vespertilione*). The KJV's 17 would begin at *pelicano*, the last word of his 16, a one-word
  verse; so his 16 is numbered **16-17** and his 17 is the KJV's 18 ('the stork … and the bat'). His 20–21 join
  (KJV 21, *Morticino … Haedum in lacte*). **A call for you to check.**
- **16:21**: split at *neve statuam* (KJV 22; 1738 has no 22). **21**: merge 18 (*Quum sit enim ejus virium
  principium*, KJV 17).
- **23**: split 2 at *Ammonita aut* (KJV 3), merge 4 (KJV 4). **25**: split 17 at *ut vobis in itinere* (KJV 18),
  merge 19 (KJV 19).
- **26:3–8**: 1738 cuts these at the speeches' openings, half a verse off, so that the KJV's 4 and 6 would have fallen
  whole in his 5 and 7: merge 4 (KJV 3), split 5 at *et tu coram* and merge 6 (KJV 5), split 7 at *Jovam Deum
  majorum* (KJV 7), split 8 at *eduxit nos* and merge 8 (KJV 8). His 10–11 and 13–14, a clause off, stand.
- **27**: split 7 at *atque in saxis* (KJV 8), merges 15 (*Et universus populus respondens dicito, amen*) and 21
  (*qui paternum gremium detexerit*).
- **28**: splits 3 at *felices erunt* (KJV 4), 4 at *felices eritis advenientes* (KJV 6), 16 at *infelicia vestra
  canistra* (KJV 17) and 48 at *gentem ita crudelem* (KJV 50); merges 11 and 13 (KJV 12–13), 51 (KJV 52) and 68.
- **30**: split 17 at *hoc vobis hodie confirmo* (KJV 18); merges 19 (*Eligite ergo vitam* with *Caelos … testor*,
  KJV 19) and 21 (KJV 20). KJV 20's opening 'That thou mayest love the LORD thy God … obey … cleave unto him' is in
  19, where Castellio joins it to *vivatis*.

## Corrections for the reading edition, found in stages 3–5

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-18; as Nathan's "correct clear errors in the edited edition", 2026-11-16)

Kept as printed in the read lines and the printed text (decision 58); corrected in the draft for the reading edition.
Each was read enlarged on 1738's page in stage 2 (§"Readings to note"); verses in the KJV's numbering.

1. **Deut 8:2** (1738's 8:3) *haberitis* → *haberetis* (row 980; *quid in animo haberetis*, imperfect subjunctive
   beside *servaturi essetis*).
    **Apply:** `Deut.8.2` la: `in animo haberitis` → `in animo haberetis`
2. **Deut 9:6** *justititiam* → *justitiam* (row 1078; a syllable doubled at the line's turn).
    **Apply:** `Deut.9.6` la: `propter justititiam vestram` → `propter justitiam vestram`
3. **Deut 16:11** *collocandc* → *collocando* (row 1831; *suo nomini collocando*, as 12:5, 12:11, 14:23, 16:2).
    **Apply:** `Deut.16.11` la: `nomini collocandc destinaverit` → `nomini collocando destinaverit`
4. **Deut 18:18** *cis* → *eis* (row 2016; *itaque eis eloquetur*, 'he shall speak unto them').
    **Apply:** `Deut.18.18` la: `itaque cis eloquetur` → `itaque eis eloquetur`
5. **Deut 22:16** *calumnietnr* → *calumnietur* (row 2333; a turned u).
    **Apply:** `Deut.22.16` la: `exosus calumnietnr` → `exosus calumnietur`
6. **Deut 23:7** *abhorrerote* → *abhorretote* (row 2406; the future imperative, as *ne abhorretote* in the same
   verse's second clause).
    **Apply:** `Deut.23.7` la: `Idumaeo ne abhorrerote` → `Idumaeo ne abhorretote`
7. **Deut 23:18** *mrcedem* → *mercedem* (row 2438).
    **Apply:** `Deut.23.18` la: `Meretricis mrcedem` → `Meretricis mercedem`
8. **Deut 4:14** *possessinem* → *possessionem* (rows 516–517: 1738 prints *posses-|si-|nem*, seen on the sheet again
   2026-11-18; a syllable dropped at the line's turn).
    **Apply:** `Deut.4.14` la: `in possessinem essetis` → `in possessionem essetis`
9. **Deut 33:29** *conferuate* → *conservate* ('O people saved by the LORD'): not a misprint but a reading slip in stage
   2. 1738 prints *conſer-|uate* (row 3648, leaf 264 col. 1, seen on the sheet 2026-11-18); the long s was read as f.
   Set right in the read lines (`Deut1-34.tsv` row 3648, `Deut1-34.corrections.tsv`) and so in the printed text, rebuilt.
    **Apply:** `Deut.33.29` la: `o popule conferuate per Jovam` → `o popule conservate per Jovam`
10. **Deut 4:9** *aduertite* → *advertite* and **Deut 32:21** *peruersa* → *perversa*: not 1738's errors but the draft's
   conversion to j/v, which missed a consonantal u after a prefix (found by reader 2 in stages 3–5; the whole draft then
   searched for the same: these two, and *aluorum* (11)). The printed text keeps 1738's *u*.
    **Apply:** `Deut.4.9` la: `aduertite` → `advertite`
    **Apply:** `Deut.32.21` la: `peruersa` → `perversa`
11. **Deut 7:13** *aluorum* → *alvorum* (*alvus*, 'the fruit of thy womb'): the same conversion slip (reader 3); the
   draft then searched again for every consonant + u + vowel, and no other found. The printed text keeps 1738's *u*.
    **Apply:** `Deut.7.13` la: `aluorum` → `alvorum`
12. **Deut 23:25** *introjeris* → *introieris* (*introeō*'s future perfect, the i a vowel): the draft's conversion
   made it j (reader 6); 1738 prints *introieris* (leaf 252, col. 1). Every other *-j-* after a prefix in the draft is
   a consonant (*abjeci, adjiciet, subjicio* …).
    **Apply:** `Deut.23.25` la: `introjeris` → `introieris`
13. **Deut 32:30** *fieri ne posset* → *fierine posset*: a question ('How should one chase a thousand …?', ending
   with 1738's own question mark), so the enclitic *-ne*, not *nē* 'lest' (reader 8). 1738 prints two words (leaf
   263, col. 0, line 8); the printed text keeps them (decision 58: word division as printed).
    **Apply:** `Deut.32.30` la: `fieri ne posset` → `fierine posset`
14. **Deut 11:10** *conferebatis* → *conserebatis* ('where thou sowedst thy seed') and **Deut 28:30, 28:39** *vineas
   conferetis* → *conseretis* ('thou shalt plant vineyards'): three more long s read as f in stage 2, as 33:29. 1738
   prints *conſerebatis* (row 1310, leaf 240 col. 1), *con-|ſeretis* (rows 2887–2888, leaf 257 col. 0) and *conſe-|retis*
   (rows 2918–2919), each seen on its sheet 2026-11-18 beside an ſ in the same crop (*veſtris*, *Veſtri*, *ſed*). Found by
   proofreader 2 (11:10); the draft's every *f*-word then compared with the settled text and read in context, and
   these two found. Set right in the read lines (`Deut1-34.tsv`, `Deut1-34.corrections.tsv`) and so in the printed text.
    **Apply:** `Deut.11.10` la: `conferebatis` → `conserebatis`
    **Apply:** `Deut.28.30` la: `vineas conferetis` → `vineas conseretis`
    **Apply:** `Deut.28.39` la: `Vineas conferetis` → `Vineas conseretis`

## Names: one form per person (decision 46)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-18; as Nathan's "Decide 1 form for each person" for Numbers, 2026-11-16)

Corrected in the draft for the reading edition; the printed text keeps 1738's spellings (decision 58). The names reader's
table, with every marking and the hard calls: `data/review/deut1-34-names.md`. Items 1–2 (*Emenses*), 10 (*Jaacanensium*), 11–12
(*Hebraeus*), 13 (*Beoris*) and 14 (*Seboimorum*) are hard calls there (each can be dropped); 4, 7 and 8 are the draft's
j-conversion, which missed the consonant after *cis-/trans-*.

1. **Deut 2:10** *Emes* → *Emenses*: the Emim (הָאֵמִים): one form for the people, the settled Gen 14:5 *Emēnsēs* (Hebrew הָאֵימִים, the same people) (decision 46; see names.md, hard call 2) (Claude, 2026-11-18)
    **Apply:** `Deut.2.10` la: `Emes` → `Emenses`
2. **Deut 2:11** *Emes* → *Emenses*: the Emim: one form, the settled Gen 14:5 *Emēnsēs* (decision 46; names.md, hard call 2) (Claude, 2026-11-18)
    **Apply:** `Deut.2.11` la: `Emes` → `Emenses`
3. **Deut 2:37** *Jabboqui* → *Jabboci*: the Jabbok (יַבֹּק): one form, the settled Gen 32:22 *Jabbocī*, Num 21:24 *Jabbōcum* (decision 46) (Claude, 2026-11-18)
    **Apply:** `Deut.2.37` la: `Jabboqui` → `Jabboci`
4. **Deut 3:8** *cisiordaninam* → *cisjordaninam*: i/j: the consonant after *cis-* (as *Jordanem*, 4:48 *cisjordanini*); the j-conversion missed it (Claude, 2026-11-18)
    **Apply:** `Deut.3.8` la: `cisiordaninam` → `cisjordaninam`
5. **Deut 3:16** *Jabboquum* → *Jabbocum*: the Jabbok: one form, the settled Num 21:24 *Jabbōcum* (decision 46) (Claude, 2026-11-18)
    **Apply:** `Deut.3.16` la: `Jabboquum` → `Jabbocum`
6. **Deut 3:17** *Cenneretho* → *Ceneretho*: Chinnereth (כִּנֶּרֶת): one form, the settled Num 34:11 *Cenerethī* (decision 46) (Claude, 2026-11-18)
    **Apply:** `Deut.3.17` la: `Cenneretho` → `Ceneretho`
7. **Deut 3:25** *transiordaninam* → *transjordaninam*: i/j: the consonant after *trans-* (as *Jordanem* and the settled Matt 4:25 *Trānsjordānīnā*) (Claude, 2026-11-18)
    **Apply:** `Deut.3.25` la: `transiordaninam` → `transjordaninam`
8. **Deut 4:49** *cisiordaninum* → *cisjordaninum*: i/j: the consonant after *cis-* (as *Jordanem*, 4:48 *cisjordanini*) (Claude, 2026-11-18)
    **Apply:** `Deut.4.49` la: `cisiordaninum` → `cisjordaninum`
9. **Deut 7:1** *Pheresaeos* → *Pherezaeos*: the Perizzites: one spelling, as 20:17 *Pherezaeos* and the settled *Pherezæōs* (Gen 15:20, Exod 23:23; Hebrew zayin) (Claude, 2026-11-18)
    **Apply:** `Deut.7.1` la: `Pheresaeos` → `Pherezaeos`
10. **Deut 10:6** *Jaquanensium* → *Jaacanensium*: Bene-jaakan (בְּנֵי־יַעֲקָן): one form for Jaakan, the settled Num 33:31 *Benējaacāne* (decision 46; names.md, hard call 4) (Claude, 2026-11-18)
    **Apply:** `Deut.10.6` la: `Jaquanensium` → `Jaacanensium`
11. **Deut 15:12** *Ebraeus* → *Hebraeus*: Hebrew (עִבְרִי): one spelling, the settled Exod 21:2 *Hebræum* (the same law), Exod 1–2, Gen 10:21, 14:13 *Hebr-*, and Wiktionary's *hebraeus* (names.md, hard call 3) (Claude, 2026-11-18)
    **Apply:** `Deut.15.12` la: `Ebraeus` → `Hebraeus`
12. **Deut 15:12** *Ebraea* → *Hebraea*: Hebrew woman: one spelling, as *Hebraeus* (the settled Exod 1:19 *Hebræās*) (names.md, hard call 3) (Claude, 2026-11-18)
    **Apply:** `Deut.15.12` la: `Ebraea` → `Hebraea`
13. **Deut 23:4** *Phegoris* → *Beoris*: Beor, Balaam's father (בְּעוֹר, LXX Βεώρ; not Peor, פְּעוֹר): one form for the person, the settled Num 22:5, 31:8 *Beōris*; 1738 and 1726 both print *Phegoris* (Castellio's own; the printed text keeps it) (names.md, hard call 6) (Claude, 2026-11-18)
    **Apply:** `Deut.23.4` la: `Phegoris` → `Beoris`
14. **Deut 29:23** *Sebojum* → *Seboimorum*: Zeboiim (צְבוֹיִם): one form, the settled Gen 14:2 *Seboimōrum* (genitive plural as here) (decision 46; names.md, hard call 5) (Claude, 2026-11-18)
    **Apply:** `Deut.29.23` la: `Sebojum` → `Seboimorum`
15. **Deut 34:1** *Phasge* → *Phasgae*: Pisgah, genitive: one spelling, as 3:27 *in jugum Phasgae* and the settled Num 21:20, 23:14 *Phasgæ* (1738 prints *Phasge*; the printed text keeps it) (Claude, 2026-11-18)
    **Apply:** `Deut.34.1` la: `Phasge` → `Phasgae`

## Next

Castellio's 1554 annotations (`deut-notes-1554.md`). The printed text was approved for now 2026-11-18
(`text/orig/DEU.usfm`, `deut-orig.md`).
