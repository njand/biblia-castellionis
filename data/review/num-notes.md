# Numbers: light notes (Old Testament search)

Built 2026-11-18 by the process in `ot-notes-process.md` (decisions 1A–4A), as `gen-notes.md`, `exod-notes.md` and
`lev-notes.md` were: kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio keeps
it; kinds B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew
agreeing, and nobody calls the passage uncertain. Formulas as in `notes-audit.md` §A and the earlier books.

**Sources read:**
- `num-notes-candidates.md` (`python -m pipeline notes Num`): 14 BSB version notes, 39 numbers, 6 short verses, and
  Castellio's one *G.* … *H.* mark (10:6).
- The NRSVue (Bible Gateway, read 2026-11-18) for all 36 chapters with its footnotes, by three readers (1–12, 13–24,
  25–36), each reading the Latin verse by verse against the WLC, the BSB with its footnotes and the KJV, with the
  Vulgate and Brenton's LXX where a verse looked odd. For 13–24 the fetch returned the NRSVue's text and notes
  summarised rather than in full; the wording cited for item 5 was checked against the BSB, the KJV and the versions,
  which agree with it. Each item below was checked here against the files. The NET notes were not read.
- The printings: 1738 as printed (`text/orig/NUM.usfm`, from the lines read on the page) and its raw OCR
  (`sources/archive/1738/text.txt`), the 1750 raw OCR (`sources/archive/1750/text.txt`), for item 6 the 1573 OCR
  through the MDZ search (canvas 124), and for §D 1738 leaf 225 read on the page.
- Castellio's 1554 annotations (`num-notes-1554.md`): nothing on any item below (they begin at chapter 13; those on
  27:19, 30:5, 30:15, 33:3 and 34:6 are class c).

The yield is 5 notes in 36 chapters (0.14 a chapter) once item 5 was withdrawn (§F), with the note at 21:24 already there.

## A. Modern Bibles follow the versions (kind A)

None. Where both the NRSVue and the BSB leave the Hebrew, Castellio already goes their way: 2:14 *Dūēlis* (Deuel, with
Hebrew manuscripts, the SP and the Vulgate; so 1:14, 7:42, 7:47, 10:20), 9:16 *interdiū* ("by day", with the LXX, the
Syriac and the Vulgate). 33:8 (Pi-hahiroth for the Hebrew's Hahiroth) is a name only; Castellio has *faucēs Ahīrōtha*
at 33:7.

## B. A reading Castellio marked as taken from the Greek (kind C)

As Exod 2:22 and 6:20: the edition doesn't print his *G.* … *H.* marks, so where modern Bibles keep the Hebrew the note
gives the reader what the mark told him.

**Decision:** accept (Nathan, 2026-11-18: "Apply all")

1. **10:6** *cum tertium; quī ad occidentem: cum quārtum; quī ad septentriōnēs*: the Hebrew names only the second alarm
   (the camps on the south), then "an alarm they shall blow for their journeys" (וּתְקַעְתֶּם תְּרוּעָה שֵׁנִית … תֵּימָנָה תְּרוּעָה
   יִתְקְעוּ לְמַסְעֵיהֶם). The NRSVue, the BSB and the KJV, without a note, have the second alarm only; the Vulgate *et juxta
   hunc modum reliqui facient*. Brenton's LXX adds σημασίαν τρίτην … παρὰ θάλασσαν … σημασίαν τετάρτην … πρὸς Βοῤῥᾶν, the
   third alarm for the camps by the sea (west) and the fourth for the north: Castellio's addition. 1738 *mouento, G. L.
   Quum tertium; qui ad occidentem: quum quartum; qui ad septemtriones: H. eisque* (`text/orig` line 353; OCR lines
   21367–21369), 1750 *G. L. Quum tertium … feptemtriones: H.* (lines 19984–19987).
   **Apply:** `Num.10.6` la: `quī ad septentriōnēs: iīsque` → `quī ad septentriōnēs\f + \fr 10:6 \ft ‘cum tertium … septentriōnēs’ Castelliō ex Græcō addit; Hebraicē secundus tantum clangor nōminātur.\f*: iīsque`

## C. Castellio's reading or text departs from the Hebrew (kinds B and C)

Each stands in 1738 and 1750 (item 6 in 1573 too): Castellio's own text, so noted, not corrected.

**Decision:** accept (Nathan, 2026-11-18: "Apply all")

2. **5:18** *ejusque caput tondētō*: Hebrew וּפָרַע אֶת־רֹאשׁ הָאִשָּׁה, "and he shall loosen the woman's hair" (the NRSVue
   "dishevel the woman's hair", the BSB "let down her hair", neither with a note; the KJV "uncover the woman's head",
   the Vulgate *discooperiet caput ejus*, the LXX ἀποκαλύψει τὴν κεφαλήν). No version has shearing; the rite gains a
   shaving of the suspected wife's head. Castellio gives פָּרַע as *tondēre* each time (Lev 10:6, 13:45, 21:10), but there
   the gesture is mourning, where cutting the hair was a sign too, and they are left out (`lev-notes.md` §D); here it
   changes the rite. 1738 *caput tondeto* (`text/orig` line 217; OCR line 20750), 1750 the same (line 19325).
   **Apply:** `Num.5.18` la: `ejusque caput tondētō,` → `ejusque caput tondētō\f + \fr 5:18 \ft Hebraicē וּפָרַע אֶת־רֹאשׁ הָאִשָּׁה, ‘et crīnēs mulieris solvitō’.\f*,`
3. **11:25** *tum sine intermissiōne vāticinābantur*: Hebrew וַיִּתְנַבְּאוּ וְלֹא יָסָפוּ, "they prophesied, but did not do so
   again" (the NRSVue, the BSB "but they never did so again", neither with a note; Brenton's LXX καὶ οὐκ ἔτι
   προσέθεντο). Castellio has the opposite, with the Vulgate (*nec ultra cessaverunt*) and the KJV ("and did not
   cease"), the old reading of יָסָפוּ as from סוּף, "cease". 1738's own footnote here (OCR line 21717: *ad verbum: Ita
   vaticinabantur, vt nihil adderent: hoc est, vt id vnum continenter agerent*) argues for it; it is one of the
   Leipzig editor's lettered glosses, which `num-notes-1554.md` traced to Castellio's annotations only in two places,
   not this one. Unlike Exod 32:25 (left out, a rare word read with the Vulgate and the
   KJV), the sense here is reversed and the modern Bibles agree with the Greek. 1738 *tum, sine intermissione
   vaticinabantur* (`text/orig` line 415; OCR lines 21616–21617), 1750 the same (lines 20252–20253).
   **Apply:** `Num.11.25` la: `sine intermissiōne vāticinābantur.` → `sine intermissiōne vāticinābantur\f + \fr 11:25 \ft Hebraicē וְלֹא יָסָפוּ, ‘neque id posteā iterāvērunt’.\f*.`
4. **12:8** *cōramque ac sine ænigmatis aut simulācrō Jōvam aspiciet*: Hebrew וּמַרְאֶה וְלֹא בְחִידֹת וּתְמֻנַת יְהוָה יַבִּיט,
   "plainly and not in riddles, and he beholds the form of the LORD" (the NRSVue, the BSB, neither with a note; the KJV
   "the similitude of the LORD shall he behold"). Castellio, with the Vulgate (*non per ænigmata et figuras Dominum
   videt*), puts the form under the negative: Moses sees God without any likeness, where a modern Bible says he sees
   his form. The LXX has τὴν δόξαν Κυρίου εἶδε, not Castellio's source. 1738 *coramque ac sine ænigmatis aut simulacro
   Iouam adspiciet* (`text/orig` line 436; OCR lines 21690–21692), 1750 the same (lines 20329–20331).
   **Apply:** `Num.12.8` la: `aut simulācrō Jōvam aspiciet.` → `aut simulācrō Jōvam aspiciet\f + \fr 12:8 \ft Hebraicē וּתְמֻנַת יְהוָה יַבִּיט, ‘et speciem Jōvæ aspiciet’.\f*.`
5. **14:24–25** *eamque ejus prōgeniēs, nec nōn Amālēchītās et Chananæōs vallis incolās, occupābit*: Hebrew 14:25
   וְהָעֲמָלֵקִי וְהַכְּנַעֲנִי יוֹשֵׁב בָּעֵמֶק, "and the Amalekites and the Canaanites live in the valley": a clause of its own, the
   reason Israel must turn back the next day (and 14:43–45 has those peoples rout Israel). Castellio makes them a second
   object of *occupābit*, a promise that Caleb's descendants will conquer them too. The NRSVue ("Now, since the
   Amalekites and the Canaanites live in the valleys"; its one note on the verse is on the Red Sea) and the BSB ("Now
   since …", no note) agree; so do the KJV (the clause in parentheses), the Vulgate (*Quoniam Amalecites et Chananæus
   habitant*) and the LXX. 1738 *nec non Amalechitas et Chananæos vallis incolas, occupabit* (`text/orig` line 511; OCR
   lines 22019–22021), 1750 the same (lines 20654–20657). **Near the bar:** a construal, in a secondary clause, which the
   next verses set right. Leave it out if the bar is held strictly. **Withdrawn** after it was applied (Nathan,
   2026-11-18: "Yes, drop 14:25"): item 9 removes it.
   **Apply:** `Num.14.25` la: `vallis incolās, occupābit.` → `vallis incolās, occupābit\f + \fr 14:25 \ft Hebraicē וְהָעֲמָלֵקִי וְהַכְּנַעֲנִי יוֹשֵׁב בָּעֵמֶק, ‘Amālēchītæ autem et Chananæī in valle habitant’.\f*.`
6. **25:2** *iīsdem eārum diīs epulābantur, et pōtābant*: Hebrew וַיֹּאכַל הָעָם וַיִּשְׁתַּחֲוּוּ לֵאלֹהֵיהֶן, "the people ate and
   bowed down to their gods" (the NRSVue, the BSB, neither with a note; the KJV "bowed down", the Vulgate *adoraverunt*,
   the LXX προσεκύνησαν). The worship, the sin the chapter is about (25:3 "joined himself to Baal-peor"), becomes
   drinking, as if וַיִּשְׁתַּחֲוּוּ were from שָׁתָה, "drink". 1738 *epulabantur, et potabant* (`text/orig` line 904; OCR line
   23684), 1750 (line 22498) and 1573 (*epulabantur, & potabant*, canvas 124, OCR) the same.
   **Apply:** `Num.25.2` la: `epulābantur, et pōtābant.` → `epulābantur, et pōtābant\f + \fr 25:2 \ft Hebraicē וַיִּשְׁתַּחֲוּוּ לֵאלֹהֵיהֶן, ‘et deōs eārum adōrābant’.\f*.`

## D. A misreading to correct: *salsī lacūs*, 34:3 and 34:12 (not a note)

The settled text has *ab extrēmō falsī lacūs* (34:3) and *falsō lacū terminābitur* (34:12), "the false lake", from the
lines read on 1738's leaf 225 (`data/witnesses/read-1738/Num1-36.tsv` lines 3744 and 3769), and `text/orig/NUM.usfm`
has *falsi* and *falso* (lines 1338, 1348). The sense needs *salsus*, the Salt Sea (יָם הַמֶּלַח), as Castellio has it at
Gen 14:3 *lacus salsus* and Deut 3:17 *lacum salsum* (where the Deuteronomy reading corrected the same slip,
`Deut1-34.corrections.tsv` line 310). Read on the page (leaf 225, the crops checked here): both words begin with a long
ſ without a crossbar, unlike the crossed *fi* of *fines* on the line above. 1738 prints *ſalſi* and *ſalſo*: *salsi*,
*salso*. The 1750 OCR (*falífi*, *falfo*, lines 23956, 23986) and the 1573 OCR (*falſi*, canvas 131) agree with ſ.

**Decision:** accept (Nathan, 2026-11-18: "Apply all")

7. The edited text.
   **Apply:** `Num.34.3` la: `ab extrēmō falsī lacūs` → `ab extrēmō salsī lacūs`
   **Apply:** `Num.34.12` la: `falsō lacū terminābitur` → `salsō lacū terminābitur`
8. The printed text, applied with `python -m pipeline review apply data/review/num-notes.md --items 8 --to
   text/orig/NUM.usfm --write`; on approval the read lines' corrections (`Num1-36.corrections.tsv`) get the same two
   readings, as Deuteronomy's did.
   **Apply:** `Num.34.3` la: `extremo falsi lacus` → `extremo salsi lacus`
   **Apply:** `Num.34.12` la: `falso lacu terminabitur` → `salso lacu terminabitur`

## E. Considered and left out

- **The existing note at 21:24 passes** (*Ār*, Castellio's emendation from 1554, against the Hebrew, the LXX, the
  Vulgate and the KJV; the NRSVue and the BSB keep the Hebrew without a note).
- **Small omissions that leave the sense (as Exod 34:24):** 14:38 (the Hebrew's חָיוּ, "lived", not translated; the
  survival is implied by *autem* against 14:37; the next candidate after item 5), 13:33 (the last clause, "and so we
  were in their sight", left out), 9:20 *aliquam multōs diēs* for "a few days" (the contrast with 9:19 blurred; not
  checked in the printings), 14:18 (paraphrased).
- **Old readings of Castellio's, below the bar:** 5:16 (*Id* for "her"; she is set before the LORD in 5:18 all the same),
  21:1 *rēx Aradus* (the KJV's "king Arad") and *explōrātōrum viā* (with the KJV and the Vulgate), 21:18 *imperātōre*
  (the KJV's "lawgiver"; poetry), 24:6 *tabernācula* for the aloes (with the LXX and the Vulgate; a plant word in a
  simile), 31:6 *sacra tēla* for "the vessels of the sanctuary" (what they are is disputed), 35:11 *cōnstrūxeritis* for
  "select", 23:21, 23:23.
- **Disputed:** 9:22 *annum tōtum* (the KJV "a year", the NRSVue "a longer time"), 11:28 (the NRSVue's own "Or … from his
  youth"), 24:17 *optimātēs* (the BSB against the Hebrew; the NRSVue gives alternatives), 10:36, 21:14–15, 21:30, 22:32
  (his 1554 note, after Josephus), 24:3, 24:8, 24:15, 24:23 (the NRSVue: uncertain, or alternatives).
- **Only one of the NRSVue and the BSB leaves the Hebrew:** 16:1, 16:6, 21:13, 21:28, 22:11, 23:2, 26:1, 26:4, 27:14,
  31:6, 32:17, 34:6; Castellio with the Hebrew or the sense unchanged.
- **Kept with the Hebrew where the BSB only reports a version, or names:** 3:9, 3:28 (8,600), 3:34, 16:5 (the LXX's
  "other", cited in 2 Tim 2:19), 26:17, 26:23, 26:39, 26:40, 27:12, 32:3.
- **Paraphrase, vocabulary, words moved, names translated:** the speech formulas turned to *inquit* (3:11–12, 4:17–18,
  4:21), 5:16–17, 12:2, 12:4, 12:9–10, 2:2, 4:20, 9:15, 10:34; 11:32 *modiōs*, 11:34 *busta cupiditātis*, 22:39, 33:49
  *plānitiem Sittīmōrum*; 13:21 *Sinæ* (Zin), 13:23–24 *Escōlem*, 22:5 *conterrāneōrum*, 25:8 *in prōstibulum*, 27:18
  *hominem cordātum*, 30:16, 31:32, 31:53; 21:13 and 22:1 *cis*; 10:29 (*socerī suī*, as the BSB); 26:9–10, 31:23–24,
  32:10–11, 34:1–2, 34:14–15, 35:9–10, 35:20–23 (words across verses); the skins and cloths of ch. 4, bdellium,
  *cichorēīs*.
- **Numbers:** every numeral matches the Hebrew: the census of 1 and 26 (603,550; 601,730), the camps of 2, the Levites
  of 3–4 (22,000, 22,273, 273, 8,580), the offerings of 7 and 28–29 (Tabernacles 13 down to 7 bulls), 16:35 and 16:48
  (the 14,700, the Hebrew's 17:14), the spoil of 31 (675,000 … 16,750 shekels), the stations of 33, the cities and cubits
  of 35. The tool's hits are numbers carried across verses (1:32, 4:22–23, 4:29–30, 4:46–47, 14:22–23, 16:48–49,
  32:10–11, 34:14–15), distributives and *duo mīllia* for the dual (3:47, 4:36, 7:85, 35:5), the tenth understood in
  *singulās* (28:21, 28:29, 29:4, 29:10), *triente* (15:6–7), *tribūnī et centuriōnēs* (1:16, 10:4, 31:14, 31:48, 31:54),
  or a number the tool missed (23:14 *septemque*).
- **Short verses:** the census and leader verses condensed (1:32, 3:21, 4:23, 10:16, 10:27), 14:27.
- **Names of persons:** every leader, clan and daughter matches the Hebrew; only Castellio's spellings differ.

## F. Item 5 withdrawn

Asked whether any of the weaker notes should go, Claude recommended dropping 14:25 alone: a construal of a secondary
clause, not a misread word, which the story itself sets right at 14:43–45, below the bar Exod 32:25 was held to. 27:28
(Leviticus), 5:18 and 11:25 stay: a wrong legal term, a rite changed, a sense reversed.

**Decision:** accept (Nathan, 2026-11-18: "Yes, drop 14:25")

9. **14:25**: the note of item 5 removed; the verse as it was settled.
   **Apply:** `Num.14.25` la: `vallis incolās, occupābit\f + \fr 14:25 \ft Hebraicē וְהָעֲמָלֵקִי וְהַכְּנַעֲנִי יוֹשֵׁב בָּעֵמֶק, ‘Amālēchītæ autem et Chananæī in valle habitant’.\f*.` → `vallis incolās, occupābit.`
