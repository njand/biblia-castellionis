# Leviticus 12–27, stages 1–2: 1738 read on the page, line by line (no Wikisource text)

Proposed 2026-11-15 (decision 68's route, as Exodus 31–40: `data/review/exod31-40-stage2.md`; decision 30's standing
rule). Nathan: "Yes, read 12–27"; versified to the KJV on his "Yes, versify Leviticus". **Stages 3–5 come next and were not run.**

- **Base**: the 1738 Leipzig edition (decision 1), leaves 167–187 of its hOCR (archive.org bibliasacraexseb01cast;
  the archive.org image is one lower). Wikisource has no Leviticus after chapter 11, so the text is 1738's own.
- **Stage 1** (`ocrdraft.make_lines`, leaves 167–187): 1738's OCR line by line, voted with 1750 and the 1726 OCR →
  `data/witnesses/read-1738/Lev12-27.voted.tsv` (1,914 rows). The OCR's *CAPVT XXVIL* had come out as chapter 24;
  set to 27.
- **Stage 2**: **every line read on the page images** (`ocrdraft.reading_sheets`, 136 sheets of 14 lines, each
  line's crop under its text), by four readers in parallel (12:1–15:18, 15:19–20:5, 20:5–24:21, 24:21–27:34), words
  and punctuation as 1738 prints them (s for ſ, æ/œ, u/v and i/j as printed; footnote letters and asterisks dropped;
  running heads, chapter summaries, catchwords and footnotes kept as `%` rows, not text) →
  `data/witnesses/read-1738/Lev12-27.tsv`, every changed row in `Lev12-27.corrections.tsv`. Verse starts set where
  1738's margin numbers stand, with the KJV beside them.
- **Checked by Claude after the merge**: two sheets read again independently (rows 271–284 and 1683–1696, 28
  lines): no difference. The lines the OCR had lost or misfiled, read on the page:
  - 13:17 (leaf 168, col. 0, line 55) *eſt.* at the column's foot, not in the OCR lines: joined to row 99.
  - 17:3 (leaf 174, col. 0) *Hæc præcipit Ioua. Quicumque de* (margin 3), filed by the OCR inside 17:14 (row 734):
    the reader restored it to row 684 from 1750; read on 1738's page since, the same.
  - 16:33 *expiato, et pro sacerdotibus pro-*, filed by the OCR in row 718: restored to row 670 by the reader.
  - 13:47 *veſtis laneæ aut lineæ, aut exterio-*, glued by the OCR to row 185: put back after row 235.
  - 21:8 *ſacros facio.* (leaf 178, col. 0, line 52), no row: joined to row 1073.
  - 25:42 *tote.* and 26:41 *rim.*, line ends of column 1 filed under column 0 (rows 1548, 1730): joined to the
    lines they end (*timetote.*, *deportauerim.*).
  - 27:33–34 (leaf 187, col. 1, lines 11–16), missing from the OCR lines: read and added (*permutatum fuerit, et id,
    quod erit … te Sina tradidit.*; margin 34 at *Hæc ſunt præcepta*).
- **The draft** (`ocrdraft.draft_from_ocr`, as `pipeline draft Lev 12-27 --from-ocr`, appended after 1–11 since
  the file exists): `text/draft/LEV.usfm`, the read lines joined into verses in Wikisource's conventions, the BSB's
  paragraphs. `ocrdraft.modern` now writes the enclitic *-ue* as *-ve* (*ouemue* → *ovemve*, *malumue*, *pedemue*,
  *redimitorue*; tested).
- **Printed text (stage 2b)**: `pipeline orig Lev 12-27 --read-lines` → `text/orig/draft/LEV.usfm` (1–11 kept).
  Paragraphs are 1738's indents; three look like the drop capital's indented lines, not paragraphs (12:1 before
  *hæc Israelitis*, 13:2 *homo, cuius*, 16:29 *Mensis septimi*): to check on the page with the 2b review.

## The numbers

| | |
|---|---:|
| printed lines read (leaves 167–187) | 1,903 body rows + 6 added |
| rows changed by the reading | 1,342 |
| verses (1738's numbering) | 12: 8, 13: 59, 14: 57, 15: 33, 16: 34, 17: **17**, 18: **32**, 19: 37, 20: 27, 21: 24, 22: 33, 23: 44, 24: 23, 25: **56**, 26: **47**, 27: 34 |

## 1738's verse numbers against the KJV's (decision 5): versified

1738's margins differ from the KJV in these chapters (the readers' notes; 1750 has the same numbers). Moved to the
KJV's numbering by 23 edits in `data/versification/Lev12-27.draft.edits.tsv` (`pipeline versify Lev --draft --apply`,
decision 30's standing rule: only verse markers move; checks passed, same words, the KJV's count in all 27 chapters,
859 verses), and the printed text rebuilt on them (`orig Lev 12-27 --read-lines`). Where the KJV has *And the LORD
spake unto Moses, saying* and Castellio only *inquit*, the clause up to *inquit* stays as that verse, as at Exod 30:17
(22:17 *Tum hæc, inquit,*; 22:26 *Bos autem, inquit,*; 23:26 *Decimus autem dies mensis septimi, inquit,*; 23:33
*Item sic Israelitas adloquere, inquit Ioua Mosi:*; 24:13 *Quod Mosi datum est huiusmodi:*). Anchors are cut to letters
both spellings share (*tum femin*, *et o*, *educito*), since the same file moves the printed text. 1738's numbers, by
chapter:

- **15**: from 1738's 11 (*Qui ea tulerit*, inside the KJV's 10) one ahead; the count comes back at 33.
- **17**: 17 verses against 16: 1738's 16 at *et aqua lauator*, 17 at *Quod si vestimenta* (KJV 16).
- **18**: 32 against 30; the same as the KJV to 18.
- **22**: 17 at *Tum hæc*, 18 at *qui vel Israelita*, 19 at *qualecumque*; 26 at *Bos autem*, 27 at *Vaccam*.
- **23**: 26 at *Decimus*, 27 at *conuentum sacrum*, 33 at *Vespere*.
- **24**: 12 at *Hic quum*, 14 at *Tum hæc Israelitis*.
- **25**: 56 against 55: 1738's 40 is the KJV's 40–41, its 41–45 the KJV's 42–46, its 46 inside the KJV's 46; its 56
  ends the KJV's 55.
- **26**: 47 against 46: 1738's 43 at *Recordabor et terræ* (still KJV 42), 46 inside the KJV's 45, 47 = KJV 46.
- **27**: 2 at *Si qui*, where the margin number stands (*hæc Israelitis edissere* stays in verse 1).
- Margins cut at the gutter, numbers placed by the sense, the KJV and 1750's margins: 13:32, 36, 41–48, 54; 14:30–31;
  16:2–14; 17:5–15; 18:2–15; 19:30–34; 22:2–8, 19; 23:26–36, 40–41; 25:19–32; 26:21–36.

## Readings to note

Verse numbers are 1738's.

- 13:32 (row 151) *neqne* (an inverted u on the page; 1750 *neque*): kept in the read line for the printed text;
  the draft's *neqne* is to be set right in stage 3.
- 22:29 (row 1223) *re iquum*, the l not inked: *reliquum* (1750 the same).
- 19:12 (row 868) *nom ne*: *nomine* (1750 the same).
- 18:17 (row 791) *nam L. eius H. con-*: the italic *L.* and *H.* (Castellio's marks) kept as printed.
- 17:15–16 (rows 744–746) *vestimenta sua perluito, #16 et aqua lauator, impurusque ad vesperam esto, et aqua
  lauator.*: *et aqua lauator* twice, and *vesperam* (elsewhere *vesperum*), as printed; for stage 3 (the KJV ends
  'then shall he be clean').
- 25:33 (row 1564) *quique. a Leuita* and 27:29 (row 1903) *si homo est. ne redimitor*: points as printed (1750
  the same).

## Corrections for the reading edition, found in stages 3–5 (7)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-15)

Kept as printed in the read lines and the printed text (decision 58); corrected in the draft for the reading edition.

1. **Lev 13:32** *neqne* → *neque* (row 151; 1738's inverted u, leaf 169; 1750 *neque*).
    **Apply:** `Lev.13.32` la: `crevisse, neqne flavos` → `crevisse, neque flavos`
2. **Lev 18:17** *nam L. ejus H. consanguineae sunt*: Castellio's *L. … H.* marks (*Latine … Hebraice*, his
   literal-rendering signs) dropped, the words kept, as the settled Exod 28:34 (`data/review/exod21-30-stage2.md`).
    **Apply:** `Lev.18.17` la: `nam L. ejus H. consanguineae` → `nam ejus consanguineae`
3. **Lev 19:20** *animaduertitor* → *animadvertitor*; **Lev 25:35** *jvvatote* → *juvatote*; **Lev 26:15**
   *parveritis* → *parueritis* (*pāreō*); **Lev 20:12** *cojerit* → *coierit* (*coeō*); **Lev 26:13** *subiugiis* →
   *subjugiis*. Not the page's: `ocrdraft.modern` had set 1738's *animaduertitor*, *iuuatote*, *parueritis*,
   *coierit* and *subiugiis* wrongly (u/v, i/j). Fixed there, with tests; the read lines rebuilt with the fix differ
   from the draft in these five words only.
    **Apply:** `Lev.19.20` la: `animaduertitor` → `animadvertitor`
    **Apply:** `Lev.25.35` la: `inquilinum jvvatote` → `inquilinum juvatote`
    **Apply:** `Lev.26.15` la: `non parveritis` → `non parueritis`
    **Apply:** `Lev.20.12` la: `nuru cojerit` → `nuru coierit`
    **Apply:** `Lev.26.13` la: `vestrarum subiugiis` → `vestrarum subjugiis`
4. **Lev 13:19** *albo rubricans macula* → *rubicans*. 1738 prints *rubricans* (leaf 168, col. 0, line 59; read
   enlarged here 2026-11-16) but *rubicantem* at 13:24 (line 76). Castellio's 1554 has *albo rubicãs macula* here and
   *albo rubican-|tem* at 13:24 (MDZ bsb10196330, canvases 70–71, read by the side session Nathan forked). Gaffiot has
   *rŭbĭcō, āre*; *rubrīcō* is only in Lewis & Short (late, very rare). So *rubricans* is the later printings' change,
   and 13:24 stays. Nathan, 2026-11-16: "Apply all of your recommendations".
    **Apply:** `Lev.13.19` la: `albo rubricans macula` → `albo rubicans macula`
5. **Lev 17:15** *impurusque ad vesperam esto, et aqua lavator.* → *impurusque ad vesperum esto, et ita purgator.*
   1738 repeats *et aqua lauator* (leaf 175, col. 0, lines 5–7, as read), and so does 1750. 1554 (canvas 74, read by
   the side session) prints *& aqua lauator, impuruſq; ad ueſperum eſto, & ita pur-|gator.*: the later printings lost
   *et ita purgator* and repeated the earlier phrase. Taken from 1554 as Exod 37:9 *obtegerent* was from 1554/1573. The
   Hebrew ends 'and he shall be clean'. Nathan, 2026-11-16: "Apply all of your recommendations".
    **Apply:** `Lev.17.15` la: `ad vesperam esto, et aqua lavator.` → `ad vesperum esto, et ita purgator.`

**Applied to the draft** under decision 30's standing rule.

## Readings for you (not changed)

Printed so by 1738 **and** 1750 (the only witnesses for 12–27); the draft keeps them until you decide.

1. **Lev 13:24** *maculam albo rubicantem* (row 141): no Latin *rubicō*; 13:19 has *albo rubricans macula* (*rubrīcō*,
   to redden). *rubricantem*?
2. **Lev 17:15** *vestimenta sua perluito, et aqua lavator, impurusque ad vesperam esto, et aqua lavator.* (rows
   744–746; 1750 line 16749 the same): the KJV and the Hebrew end *וְטָהֵר*, 'then shall he be clean'. Castellio may mean
   a second washing at evening, or the printer repeated the phrase for something like *et purus esto*. *vesperam*
   (Gaffiot has *vespera*) beside the usual *vesperum* is a variant, not a slip.
3. **Lev 23:24** *sabbatum monetum clangoris* (row 1315, *mone-|tum*; 1750 line 17658 *monetum*): not a Latin word.
   Reader G proposes *monitum* ('reminder', Hebrew *zikhrôn*, LXX μνημόσυνον): a conjecture.
