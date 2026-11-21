# 1 Samuel 16–31: light notes (Old Testament search), reader B

Built 2026-11-20 in phase 2 of decision 85 (PLAN.md §4), beside `propose`, by the process in `ot-notes-process.md`
(decisions 1A–4A), as Ruth's (`ruth-notes.md`), Judges' (`judg-notes.md`) and Joshua's (`josh-notes.md`), with the bar
as it now stands (Nathan, 2026-11-19: no note for a departure without plot or theological significance; `num-notes.md`
§F: a construal the context sets right is left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an
ancient version and Castellio keeps it; kinds B and C where his reading or his text departs from the Hebrew against the
NRSVue, the BSB and the Hebrew agreeing, and nobody calls the passage uncertain. Reader A has chapters 1–15 (and 13:1).
Castellio's 1554 annotations on 1 Samuel 16–31 and the 1554 text's margins, read on the page in this pass, are in
`1sam-notes-1554-b.md`.

**Sources read:**
- `1sam-notes-candidates.md` (`python -m pipeline notes 1Sam`), every candidate in 16–31: the *G.* … *H.* marks at
  17:43, 17:49, 22:10 (= 22:9, *pontificem*) and 28:10 (not 1 Samuel's: §D); the BSB version notes 17:4, 17:12, 17:52,
  20:25, 20:41, 22:3, 25:1, 25:22, 30:2; the numerals 17:18–29:5.
- The NRSVue (Bible Gateway, read 2026-11-20) for chapters 16–31 with every footnote (not stored; one fetch per chapter,
  29–31 together); 28:17 read again for its first clause.
- Every verse of the preview (`text/draft/1SA.preview.usfm`) 16:1–31:13 read against the BSB (`sources/parallel/bsb/1Sam.tsv`),
  with the WLC, Brenton's LXX and the Vulgate where a verse looked odd (17:43, 17:49, 22:9, 25:22, 28:17, 30:2).
- 1738 as printed (`text/orig/1SA.usfm`) and its footnotes and asterisks from phase 1 (`data/witnesses/read-1738/1Sam1-31.tsv`,
  `1sam1-31-transcription-readers.md`); the 1750 raw OCR (`sources/archive/1750/text.txt`); **1554** (MDZ bsb10196330,
  canvases 161–171 and the annotations on canvases 825–826) and **1573** (MDZ bsb10141277, search API snippets only,
  canvases 199, 201, 205) for the places below (`1sam-notes-1554-b.md`).

The yield is 1 note proposed in 16 chapters (0.06 a chapter), with two more near the bar recommended left out (items 2,
3) and one place where the 1554 annotation shows the base text has lost Castellio's reading (item 4, a text question,
not a note).

## A. Modern Bibles follow the versions (kind A)

None proposed. Both Bibles leave the Hebrew for the Greek at 17:12, 17:52, 25:22 and 30:2: at 17:12 and 30:2 Castellio
already reads with them (his 1554 annotations say so, `1sam-notes-1554-b.md`); 17:52 is below the bar (§G); 25:22 is
item 3.

## B. A reading Castellio marked as taken from the Greek (kind C)

**Decision:** accept 1; item 2 (17:49) left out (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

1. **17:43** *Num ego sum canis (inquit) ut tū mē baculō, et lapidibus adgrediāre? Nōn, inquit Dāvīd, sed cane
   dēterior.* 1738 prints Castellio's marks: *vt tu me baculo, G. et lapidibus H. adgrediare? G Non, inquit Dauid, sed
   cane deterior. H.* (`text/orig/1SA.usfm` line 541; the second *G* without its stop, as read on the page), and 1750
   the same (OCR line 40257, *et lapidibus H. adgrediare? G. / Non, inquit Dauid, fed cane dete-*). So did **1554**
   (canvas 163, column 301: *me baculo? G. & lapidibus H. aggrediare? G. Non, inquit Dauid, sed cane deterior. H.*) and
   **1573** (canvas 199, MDZ search: *vt tu me baculo, G. & lapidibus H. aggrediare? G.*). The Hebrew has only the
   Philistine's question: הֲכֶלֶב אָנֹכִי כִּי־אַתָּה בָא־אֵלַי בַּמַּקְלוֹת, "Am I a dog, that you come to me with sticks?"; the
   Vulgate the same (*cum baculo*). The words are Brenton's LXX: ἐν ῥάβδῳ καὶ λίθοις; καὶ εἶπε Δαυὶδ, οὐχί, ἀλλʼ ἢ
   χείρων κυνός. The NRSVue ("Am I a dog, that you come to me with sticks?", no footnote) and the BSB (the same, no
   note) keep the Hebrew. Kind C, a version followed where modern Bibles keep the Hebrew: the form of the accepted
   Exod 2:22, Exod 6:20 and Josh 16:10 notes (*‘…’ Castelliō ex Græcō addit*).

   **Why it passes the bar**: it gives David a line he does not speak in the Hebrew, in the most read exchange of the
   book: his insult "No, worse than a dog" answers the Philistine before 17:45's speech. A reader with a modern Bible
   finds the Philistine's question go unanswered until 17:45. The stones (*et lapidibus*) are small, but they are the
   same marked passage and cost nothing to name. Near the bar only in being a single retort that changes no outcome;
   Exod 6:20 (Miriam named) and Josh 16:10 (Pharaoh's capture of Gezer) were accepted for less.

   Words checked with `pipeline latin macron` (lapidibus, dēterior, addit; *Castelliō*, *Græcō* as in the settled
   notes); the quoted words as the preview has them.
   **Recommendation (Claude): accept.**
   **Apply:** `1Sam.17.43` la: `sed cane dēterior.” Tum` → `sed cane dēterior\f + \fr 17:43 \ft ‘et lapidibus’ et ‘Nōn, inquit Dāvīd, sed cane dēterior’ Castelliō ex Græcō addit.\f*.” Tum`

2. **17:49** *ut ille transadacta galea, et adfīxō frontī saxō, prōnus humī conciderit*, **near the bar**. 1738 marks
   *G. transadacta galea, et H.* (line 547), as 1554 (canvas 163, column 301, *ut ille G. transadacta galea, & H. affixo
   fronti saxo*) and 1573 (canvas 199, *vt ille G. tranſadacta galea, & H. affixo fronti ſaxo*). Brenton's LXX: διέδυ ὁ
   λίθος διὰ τῆς περικεφαλαίας εἰς τὸ μέτωπον αὐτοῦ ("the stone went through the helmet into his forehead"); the Hebrew
   וַתִּטְבַּע הָאֶבֶן בְּמִצְחוֹ, "the stone sank into his forehead", as the NRSVue and the BSB (no notes). Only the helmet is
   added: the stone, the forehead and the fall are the Hebrew's, and nothing in the story turns on the helmet (a
   furnishing detail, brief.md). **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Sam.17.49` la: `ut ille trānsadāctā galeā,` → `ut ille trānsadāctā galeā\f + \fr 17:49 \ft ‘trānsadāctā galeā’ Castelliō ex Græcō addit.\f*,`

## C. Near the bar, recommended left out

**Decision:** left out (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

3. **25:22** *At ita perdat Deus hostēs Dāvīdis*: Hebrew כֹּה־יַעֲשֶׂה אֱלֹהִים לְאֹיְבֵי דָוִד, "so may God do to the enemies
   of David", as Castellio and the Vulgate (*Hæc faciat Deus inimicis David*). The NRSVue "God do so to David" (note
   "Gk Compare Syr: Heb *the enemies of David*"), the BSB "May God punish David" (note "Some LXX manuscripts; MT David's
   enemies"; Brenton's LXX τῷ Δαυὶδ). So kind A by the test. But the oath is David's self-curse either way (the Hebrew's
   "enemies of David" is read as a scribe's softening), what David swears and does is the same, and the reader of the
   Latin sees an oath. Only the oath's wording changes, as Judg 9:29 and Josh 12:4 (the frame only) were left out.
   1738 *At ita perdat Deus hostes Dauidis* (`text/orig/1SA.usfm`), 1554 (canvas 167, column 310, *At ita perdat Deus
   hostes Dauidis*) the same. **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Sam.25.22` la: `At ita perdat Deus hostēs Dāvīdis,` → `At ita perdat Deus hostēs Dāvīdis\f + \fr 25:22 \ft Versiōnēs antīquæ habent ‘ita perdat Deus Dāvīdem’.\f*,`

## D. The 1554 annotation shows the base text lost Castellio's reading (a text question, not a note)

**Decision:** applied to the draft (`1sam1-31-draft-fixes.md` §3, read on 1554 canvas 165 by Claude), confirmed with the book (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later); the Apply line below is superseded

4. **20:30** *ō improbē, inquit, contumācisque mātris prōgeniēs*. 1738 prints *o improbe* (line 658), and 1750 (OCR
   line 40822) and Wikisource the same, so Saul calls Jonathan "wicked". But **1554** prints *O' improbæ, inquit,
   contumacisq; matris progenies* (canvas 165, column 305, zoom `n165-20_30.jpg`), "O son of a wicked, contumacious
   mother", and so does **1573** (canvas 201, MDZ search: *O c improbæ, inquit, contumacisq; matris progenies*).
   Castellio's own margin there, which 1738 prints as its footnote l) on this very word, explains *improbæ*: *ut hominis
   filium uocant Hebræi hominẽ, ita Saulus improbæ filium uocat improbum: sed à matre, ne se ipse damnet* ("Saul calls a
   wicked man the son of a wicked woman, naming the mother so as not to condemn himself"). The Hebrew בֶּן־נַעֲוַת הַמַּרְדּוּת is
   "son of a perverse, rebellious (woman)" (the NRSVue footnote: "Cn Compare Q ms Gk: Meaning of MT uncertain"; the BSB
   "You son of a perverse and rebellious woman"). So *improbe* is a later printer's change, between 1573 and 1738, and
   1738's footnote no longer fits its text. The edition follows 1738, but this is a misprint against the author's
   evident sense and his own note: the verse readers should consider *improbæ* (no macron: feminine genitive, with
   *contumācis … mātris*). The printed text (`text/orig/1SA.usfm`) keeps *improbe*, as printed.
   **Apply (for the verse review, if accepted; not a note):** `1Sam.20.30` la: `ō improbē, inquit,` → `ō improbæ, inquit,`

## E. 1738's footnotes in 16–31 (recommended: none printed)

**Decision:** none printed, as Joshua, Judges, Ruth (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

1738 prints twelve lettered footnotes in these chapters. **All twelve are Castellio's 1554 lettered margins**, with only
the spelling of a later printing changed (`1sam-notes-1554-b.md`, table). None marks a departure from the Hebrew that the
text needs noted; all are glosses on the sense, and the edition prints no glosses (brief.md: "No marginal notes or
commentary"; Joshua, Judges and Ruth printed none of 1738's, `josh-notes.md` §E, `judg-notes.md` §D, `ruth-notes.md` §C).

- **19:19** *h) eadem modo Rama, modo Ramatha (vt paullo ante) dicitur.* on *apud Ramam* (the task's "20:? h)": it is
  KJV 19:19). A name's two forms.
- **20:3** *i) Iurare vocat religiose adfirmare, quod facit sequentibus his verbis: Quam certum est, etc.* on *jūrāvit*;
  the verse's own oath follows.
- **20:11** *k) scilicet vt cælum intuens Iouam iuraret.* on *sub dīum*. Commentary.
- **20:30** *l) vt hominis filium vocant Hebræi hominem, ita Saulus improbæ filium vocat improbum: sed a matre, ne se
  ipse damnet.* on *improbē*: see item 4; once the text reads *improbæ* the gloss is a comment on the idiom.
- **21:2** *m) scil. vbi me præstolentur: ne sciant, quo ego profectus sim.* on *certum quendam locum*. Commentary.
- **21:5** *n) si forte mei famuli … lustrandis corporibus est destinatum.* on *Quod sī*: a paraphrase of Castellio's
  reading of a verse the NRSVue and the BSB render differently ("the vessels of the young men are holy"); Castellio
  reads כְּלֵי as their bodies (*corpora*). The sense (the men are clean) stands, and the bread is given as in the Hebrew.
  No note. (The NET was not read.)
- **25:22** *a) ne canem quidem.* on *nē parietis quidem commictōrem*. A gloss on the idiom (1554 *ne canẽ quidem.*).
- **25:29** *a) apud Iouam esse dicuntur, qui hac vita (quam curat Ioua) fruuntur. vide Esa. 38. et Ps. 116.* on *anima
  tua apud Jōvam*. Commentary, with cross-references (which the notes never carry, brief.md).
- **25:29** *b) tuos hostes male perdat ac profliget.* on *Jōva tuōrum hostium animam*. Paraphrase.
- **25:31** *c) quod fieret, si Nabalem interfecisses.* on *hoc tē nūlla cōnscientiæ lābe*. Paraphrase.
- **28:6** *d) per Pontificem, qui hæc verba, Claritas et Integritas, gestabat in monili,* on *per clāritātem*. Printed
  ending in a comma, but **complete**: 1554's margin ends *gestabat in monili.* (canvas 169, column 314, zoom
  `n169-28_6.jpg`), so the comma is 1738's slip, not a lost continuation. It explains that *clāritās* is the Urim, which
  the settled Exod 28:30 and Lev 8:8 set out (*CLĀRITĀS ET INTEGRITĀS* on the breastpiece). Castellio's vocabulary; the
  NRSVue and the BSB have "Urim". A reader of this edition has met it in Exodus. Not printed. (Aside for the verse
  readers: 1554 prints *per Claritatem* with a capital, canvas 169; 1738 and 1750 *claritatem*.)
- **28:13** *e) diuinum virum, et humana forma augustiorem.* on *dīvum*. Castellio's *dīvum* is the Hebrew's אֱלֹהִים, "a
  divine being" (the NRSVue, note "Or *a god* or *gods*"; the BSB "a god"): no departure.

**Recommendation (Claude):** print none of them, as in Joshua, Judges and Ruth.

## F. 1738's asterisks in 16–31: Castellio's 1554 annotations

The seven asterisks 1738 prints with no footnote in these chapters stand, each, **exactly where the lemma of one of
Castellio's 1554 annotations ends** (annotations read on canvases 825–826, `1sam-notes-1554-b.md`):

| 1738 (phase 1 reader's row) | Verse (KJV) | 1554 annotation lemma (canvas, column) |
|---|---|---|
| *immanis \* ex castris* (row 1720) | 17:4 | *Vir quidam immanis.)* (825, 346) |
| *prouecta.\* Eius* (row 1753) | 17:12 | *Iam senex & ætate prouecta.)* (825, 346) |
| *ad summum ter \* in locum* (row 2213; 1738's 20:18) | 20:19 | *Descendes autem ad summum ter.)* (825, 346–826, 347) |
| *[descenden]ti, \* atque ita dicenti* (row 2765) | 25:20 | *Cum suis aduersus eam descendenti.)* (826, 347) |
| *qui te comitantur, \* dari* (row 2799) | 25:27 | *Qui te comitantur.)* (826, 347) |
| *Faciet Ioua tibi, \* quod per me prædixit* (row 3108) | 28:17 | *Faciet Ioua tibi.)* (826, 347) |
| *tum mulieres \* captiuos ceperant* (row 3208) | 30:2 | *Omnes omnium ætatum tum uiros, tum mulieres.)* (826, 347) |

That is every 1554 annotation on 1 Samuel 16–31, and no asterisk lacks one. The same holds for reader A's seven (1:3
*bellipotentem*, 6:8 *simulachra*, 6:17–18 *saxum*, 8:12 *centuriones*, 12:17 *tonabit*, 13:1 *Iniuit autem Saulus
regnum*, 14:36 *perimerent*: the fourteen 1554 annotations on the book, canvas 825, match 1738's fourteen asterisks one
for one, by my reading of the column; A reports on them). So **1738's footnote-less asterisks mark the places of
Castellio's 1554 annotations**, which 1738 does not print. This settles Ruth's open question (`ruth-notes.md` item 7,
"not proved"): the 3:16 asterisk is the same mark.

None of the seven in 16–31 needs a note: 17:4 explains *immānis* (from בנים as "of men", i.e. excellent; the modern
"champion"; a construal of one word); 17:12 emends בא באנשים to בשנים, "advanced in years", **as the NRSVue ("Gk Syr: Heb
*among men*") and the BSB do**; 20:19, 25:20, 25:27 explain his Latin; 28:17 reads לך, "to you", with the margin, Jerome
and the Greek, **as the NRSVue does** ("The LORD has done to you just as he spoke by me", no footnote; WLC לוֹ); 30:2
follows the Greek's "and all who were in it", **as the NRSVue ("Gk: Heb lacks *and all*") and the BSB do**.

## G. Considered and left out

- **The tool's candidates**: **17:4** *sex cubitōs* (the Hebrew and the BSB; only the NRSVue has "four", note "Q ms Gk:
  MT *six*": not both, and a number); **17:12** (Castellio with both Bibles, §F); **17:52** *usque ad vallem* (the Hebrew
  גַּיְא; both Bibles "Gath" with the Greek, NRSVue "Gk Syr: Heb *a valley*"): only the end point of a pursuit, as Judg
  20:33 and Deut 11:30; **20:25** *Jonathān surrēxisset* (the Hebrew; the BSB "opposite Jonathan" with the LXX; the NRSVue's
  footnote "Q ms Gk: MT *rose*" was reported for 20:34 by the fetch, so whether it leaves the Hebrew here is not
  settled): a seating, below the bar either way; **20:41** *ā merīdiānā parte* (the Hebrew, as the BSB); **22:3** (the
  BSB "stay" with the Syriac and Vulgate; Castellio's *ad eōs sē recipere* gives the sense); **25:1** *Pharanem* (the
  Hebrew, with both Bibles); **25:22** item 3; **30:2** (§F); **22:9** (the candidates' 22:10) *Achitobi fīlium,
  pontificem*: 1738 marks *G. L. pontificem, H.* (1554 canvas 166, column 307, *G. L. pontificẽ, H.*), the Greek's τὸν
  ἱερέα; a title of a man the story calls the priest throughout (21:1): nothing to note; **28:10** (the candidates'
  *G. L. Ioua H. tibi benigne adiit. / At Ettaeus*) is 2 Sam 15:21, Ittai, misplaced by the tool. **Numbers**: every
  numeral in 16–31 matches the Hebrew (*tribūnus* for שַׂר־הָאֶלֶף and *centēnī et mīllēnī* are his vocabulary; *Saulus
  mīlle, decem superāvit mīllia Dāvīd* the song's thousands and ten thousands; 21:5 *tertium diem* for כִּתְמוֹל שִׁלְשֹׁם,
  §E); 18:27 *ducentīs* is the Hebrew (the NRSVue "one hundred", Gk).
- **The passages the Septuagint lacks** (Brenton's LXX has no 17:12–31, 17:55–18:5, 18:10–11, 18:17, 18:30, among others):
  Castellio prints them all, as 1554 does (canvases 162–163), and the NRSVue prints them without brackets or notes, as
  the BSB. Nothing to note.
- **Only the NRSVue leaves the Hebrew** (Castellio with the Hebrew and the BSB): 17:4, 18:27, 23:11, 23:14, 23:16,
  24:10, 27:8, 27:10, 29:10 (the NRSVue adds the Greek's "and go to the place … done well before me").
- **Disputed or uncertain Hebrew** (the NRSVue "Meaning of Heb uncertain"): 17:8, 19:13, 19:16, 19:20, 20:14–15, 20:19,
  20:30, 20:41, 21:2, 21:5, 22:14 (*tuō jussū profectō* for "captain over your bodyguard", NRSVue "Heb *and turns
  aside*"), 22:22, 23:28.
- **His vocabulary, or a construal the context sets right**: *tribūnus*, *centuriōnēs*, *satrapæ*; *bacchārī* for
  prophesying (18:10, 19:20–24); 28:6 *per clāritātem* (the Urim, §E); 28:7–8 *fēminam Phœbō præditam*, *dīvīnā mihi
  per Apollinem* (the medium and her spirit: his classical names, the sense kept); 28:13 *dīvum*; 17:1 *in fīnibus
  Daniōrum* (Ephes-dammim); 17:29 *num injussus fēcī?*; 18:21 *ex alterā fīliā* (בִּשְׁתַּיִם); 23:15–19 *in silvā* (Horesh);
  23:28 *Rūpēs diremtōria*; 26:19 *precor, ut tū eī lītēs*; 26:10 and 28:17 a tense (*faciet*, with the Vulgate) where
  the Hebrew has the perfect, the sense kept.
- **Words moved or condensed**: 16:4–5, 17:13–15, 17:19–22, 20:14–16 (the vengeance on David's enemies in 20:14), 23:24–25.
