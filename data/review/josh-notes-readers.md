# Joshua notes: the readers' reports

Three readers (1–7, 8–14, 15–24), 2026-11-19, under the brief summarized in `josh-notes.md`. Kept as written (internal notes); `josh-notes.md` says what was proposed from them, and corrects one placing: 1738's Achor footnote is at 7:24.

## Joshua 1–7: light notes (reader 1)

Read 2026-11-19 by the process in `ot-notes-process.md` (§§1–3, 5), with the bar as `judg-notes.md` and `num-notes.md` §F
leave it. Every verse of 1–7 in `text/JOS.usfm` was read against the KJV and the BSB with all its footnotes (from
`sources/parallel/bsb/files/07-JOSengbsb.usfm`), with the WLC, the Vulgate and Brenton's LXX where a verse looked odd
(1:14, 5:6, 6:18, 6:23, 7:17). The NRSVue (Bible Gateway, read 2026-11-19) was fetched one chapter per fetch for all
seven chapters, with its textual footnotes (none stored). The NET was not read: no item below rests on a disputed
reading. 1738 checked as printed (`text/orig/JOS.usfm`) and in its raw OCR (`sources/archive/1738/text.txt`), 1750 in
its raw OCR, 1573 through the MDZ search API (OCR snippet; no page image read).

The NRSVue's textual footnotes in 1–7, all seen: 2:4 "Gk: Heb *him*"; 2:10 and 4:23 "Or *Sea of Reeds*"; 3:16 "Heb
*Salt Sea*"; 5:1 "Q ms places 8.30–35 before 5.1"; 5:3 and 5:9 (name meanings); 6:18 "Gk: Heb *devote to destruction*";
6:25 "Heb *She*"; 7:17 "Heb mss Syr: MT *one by one*"; 7:26 (name meaning). Chapter 1 has cross references only.

The yield is 1 note in 7 chapters (0.14 a chapter), near the bar.

### B. Castellio's text departs from the Hebrew (kind B/C)

1. **6:23** *cumque omnī suā propinquitāte forās in castra Isrāēlītārum ēdūxērunt, et ibi relīquērunt*: Hebrew
   וַיַּנִּיחוּם מִחוּץ לְמַחֲנֵה יִשְׂרָאֵל, "and they left them **outside** the camp of Israel". The NRSVue "and set them outside the
   camp of Israel" (no note), the BSB "and settled them outside the camp of Israel" (no note), the KJV "without the
   camp of Israel", the Vulgate *extra castra Israël manere fecerunt*, Brenton's LXX ἔξω τῆς παρεμβολῆς (the verse's
   end; the LXX file's opening seen, the Vulgate's in full). No version and no modern Bible reads "into the camp".
   Castellio brings Rahab's family *forās* (out of the city) *in castra* and leaves them there: inside the camp, where
   every witness puts them outside it, the place of foreigners not yet received (her living *inter Isrāēlītās* comes
   only at 6:25). A reader with a modern Bible would find the opposite location. Not a printer's slip: 1738 *foras in
   castra Israelitarum eduxerunt, et ibi reliquerunt* (`text/orig/JOS.usfm` line 146; OCR lines 31102–31103), 1750
   *[f]oras in castra Israëlitarum eduxerunt* (OCR lines 30605–30607), 1573 *forâs in castra Israelitarum eduxerunt,
   & ibi reliquerunt* (MDZ canvas 159). Castellio's own.
   **Near the bar**: a detail of place, not of the event; but it is a plain Hebrew phrase turned to its opposite, on
   the scale of Judg 4:5 (Hormah for Ramah), which was accepted. **Recommendation: note.** Latin words checked with
   `pipeline latin macron` (*extrā*, *castra*, *Isrāēlītārum*; *Hebraicē* as in the existing notes). The old text occurs
   once in `text/JOS.usfm`.
   **Apply:** `Josh.6.23` la: `forās in castra Isrāēlītārum ēdūxērunt,` → `forās in castra Isrāēlītārum\f + \fr 6:23 \ft Hebraicē מִחוּץ לְמַחֲנֵה יִשְׂרָאֵל, ‘extrā castra Isrāēlītārum’.\f* ēdūxērunt,`

### C. Considered and left out

**The tool's candidates in 1–7:**
- **7:1** (BSB: Zabdi a variant of Zimri, LXX, 1 Chr 2:6): Castellio *Zabdis nepōs* (also 7:17–18 *Zabdī*, *Zabdis*)
  keeps the Hebrew, as both Bibles do. Nothing to note.
- **Numbers 3:4** (*bis mīlle cubitōs*, the Hebrew's dual אַלְפַּיִם, "two thousand"), **4:19** (*decimō diē*, the Hebrew's
  בֶּעָשׂוֹר written as a word), **6:14** (*semel diē secundō … sex diēbus*: all there), **7:3** (*duo aut tria … mīllia*, the
  Hebrew's dual): every numeral matches the Hebrew; the tool's differences are the dual and ordinals. **5:2**'s
  "second time" is in 5:3 *iterātō*.
- **Short 5:2**: the command "make flint knives and circumcise again" is carried into 5:3 (*factīs cultrīs lapideīs,
  Isrāēlītās iterātō circumcīdit*). Words moved.

**Only the NRSVue leaves the Hebrew** (the BSB with it, or not naming a version):
- **2:4** (NRSVue "Gk: Heb *him*"): Castellio *ambōs occuluisset*, the sense both Bibles print ("hid them"). Nothing.
- **6:18** (NRSVue "covet", Gk; the BSB "lest you yourself be set apart for destruction", the Hebrew): Castellio *nē, sī
  quid inde cēperitis* has neither clause; a condensation, the sense (taking the devoted things brings ruin) kept.
- **6:25** (NRSVue "Her family", "Heb *She*"): Castellio *eaque inter Isrāēlītās … mānsit*, the Hebrew, with the BSB.
- **7:17** (NRSVue "by households", "Heb mss Syr: MT *one by one*"; the BSB "come forward", no note): Castellio
  *sortītus est in virōs*, the Hebrew לַגְּבָרִים (and the LXX κατʼ ἄνδρα). Not kind A.
- **5:1** (NRSVue: a Qumran manuscript's order of chapters): no reading; and 5:1's Ketiv "until we had crossed"
  (BSB note "Or until we had crossed over"): Castellio *ad Isrāēlītārum trānsmissiōnem*, the Qere, with both Bibles.

**Weighed and left out:**
- **1:14** *vestrīs mulieribus et parvulīs*: the Hebrew's third item וּמִקְנֵיכֶם "and your livestock" is missing (1738
  line 25 the same). A list shortened; no reader is misled about the event. Below the bar.
- **5:6** *majōribus nostrīs* for לַאֲבוֹתָם "to their fathers" (both Bibles "their"): a pronoun; the sense (the land sworn
  to the fathers, given to "us") stands. Left out, as pronoun slips are elsewhere.
- **5:14** *Immō ego dux exercitūs Jōvæ* for לֹא (both Bibles "Neither"; some versions read "to him"): Castellio's
  *Immō* is the Hebrew's "No". Nothing.
- **6:9, 6:13** *prōmiscuō vulgō*, *vulgō* for הַמְאַסֵּף "the rear guard" (both Bibles "rear guard"; the Vulgate *reliquum
  vulgus*): the Vulgate's construal; who walks behind the ark (the rest of the people or a rear guard) barely
  changes the procession. Left out by `num-notes.md` §F.
- **7:5** *ad Sabārīm*: a name, with the NRSVue ("as far as Shebarim") and the BSB's own note ("Or as far as Shebarim").
- **7:14** *sortīminī*: the Hebrew's "the tribe which the LORD takes" understood as by lot, as 7:16 *sortēs jēcit* and
  the common reading; vocabulary of the procedure.
- **7:21** *aureamque linguam*: the Hebrew's לְשׁוֹן זָהָב literally ("a tongue of gold"; both Bibles "a bar"); the KJV
  "wedge". Literal, not a departure.
- **Paraphrase, words moved or condensed**: 1:10–11 (the order to the people moved into 1:10), 2:15 (*submœnia* for
  "she dwelt on the wall"), 2:22–23, 3:15–16, 4:10–13 (*cōram Jōvā* and the plains of Jericho moved into 4:12), 4:15–17
  (one verse in Castellio, *\v 15-17*), 5:4–7, 6:3–4, 7:2–3 (the spies' report begun in 7:2), 7:20, 7:25.
- **Vocabulary**: *magistrātūs* (1:10, 3:2), *sacrātī* / *sacrilegium* for חֵרֶם (6:17–18, 7:1–15), *ōrāculī arcam* (4:15–17),
  *tubās buccinās* (6:4–13), *senātōribus* (7:6).
- **1738's footnotes and Castellio's 1554 annotations**: not read here (the other reader's).
- **Misreadings of 1738**: none found at the places checked.

## Joshua 8–14: light notes (reader 2)

Read 2026-11-19 by the process in `ot-notes-process.md` (§1–3, §5), with the bar `judg-notes.md` and `num-notes.md` §F
left. Every verse of 8–14 in `text/JOS.usfm` (via `data/gold/Josh.tsv`) was read against the KJV and the BSB, with the
WLC wherever a verse looked odd (8:15–17, 9:4, 9:21, 12:4, 12:23, 13:3, 13:17, 13:26), the Vulgate and Brenton's LXX at
13:3–4. Chapters 12–14 read for numbers and places changed, not spellings. The NRSVue (Bible Gateway, read 2026-11-19)
fetched one chapter per fetch for all seven chapters, its textual footnotes taken from each page (none stored); for
chapter 11 the fetch returned only cross references, i.e. no textual footnote on the page. The NET was not read: no item
rests on a disputed reading. 1738 checked as printed (`text/orig/JOS.usfm`) and in its raw OCR, 1750 in its raw OCR, 1573
through the MDZ search API (OCR snippet only, no page image). The stage reviews (`josh1-24-ch13.md`,
`josh1-24-names.md`, `josh1-24-stages3-5.md`) were read where they touch an item.

The yield is 1 note in 7 chapters (0.14 a chapter), near the bar.

### B. Castellio's text departs from the Hebrew (kind C)

1. **13:3** *quīnque Palæstīnōrum præfectūræ, Gazēa, Azōtēnsis, Ascalōnēnsis, Gethēnsis, Accarōnēnsis et Hevæēnsis*:
   Hebrew … וְהָעֶקְרוֹנִי וְהָעַוִּים, "and the Ekronites; and the Avvim". The NRSVue "and those of the Avvim" (no note on
   it; its only notes in the chapter are at 13:8, 13:9, 13:14, 13:26), the BSB "as well as that of the Avvites" (no
   note), the KJV "also the Avites". Castellio makes the Avvim into the Hivites: *Hevæ-* is his stem for the Hivites
   (חִוִּי) throughout, at 9:1 *Hevæī*, 9:7 *Hevæīs*, 11:3 *Hevæōs*, 11:19 *Hevæōs Gabaōnītās*, the people of Gibeon and
   of Hermon in the north; while for the Avvim themselves he writes *Aviōs* (settled Deut 2:23, the same people in the
   same southwest corner, "as far as Gaza") and the town *Avīm* (Josh 18:23). The form comes from the Greek, Brenton's
   LXX καὶ τῷ Εὐαίῳ (the LXX's spelling of the Hivites too); the Vulgate has no Avvim in 13:3 and puts *Hevæi* at the head
   of 13:4 (*Ad meridiem vero sunt Hevæi*). So a reader of Castellio meets a sixth "prefecture" of Hivites among the
   Philistine cities, where the Hebrew and both modern Bibles have the Avvim, a different people: a people changed into
   another, as Judg 4:5 *Hormam* for Ramah (a place Castellio names elsewhere for itself). Not a printer's slip: 1738
   *accaronensis et heuæensis* (`text/orig/JOS.usfm` line 352; OCR line 32051–32053), 1750 *Accaronenfis et Heuacenfis*
   (OCR lines 31703–31704), 1573 *Accaronenſis, & Heuæenſis* (MDZ canvas 164). The stage review already saw it
   (`josh1-24-names.md` call 13: "follows the Greek Εὐαίῳ (the Hivites), against the settled Deut 2:23 *Aviōs*"; kept
   as his rendering).
   **Near the bar**: it is a name in a list, and could be read as the Greek's spelling of a name (left out by the rule
   on names); against that, Castellio's own text distinguishes the two peoples, so his reader is told something the
   Hebrew does not say. **Recommendation: accept**, on the Judg 4:5 precedent; leave out if names in lists are to stay
   below the bar. Latin: *Hebraicē* (Gaffiot *Hĕbrăĭcē*, the lookup gives *hebraice*); *Aviī* nominative plural of the
   settled *Aviōs* (Deut 2:23; the lookup knows only the common noun *avius*, no macron on the i).
   **Apply:** `Josh.13.3` la: `Accarōnēnsis et Hevæēnsis:` → `Accarōnēnsis et Hevæēnsis\f + \fr 13:3 \ft Hebraicē הָעַוִּים, ‘Aviī’.\f*:`

### C. Considered and left out

**The tool's candidates in 8–14:**
- **12:4** (kind A in form: the NRSVue "and King Og of Bashan", note "Gk: Heb *the boundary of King Og*"; the BSB "And Og
  king of Bashan", note "LXX; Hebrew And the territory of Og"): Castellio *tum fīnēs Ōgī Bāsānæ rēgis … quī Astarōtha et
  Edreīm incolēbat* keeps the Hebrew, but only the list's frame changes (Og's territory or Og), as Judg 9:29 and Deut
  31:1. Left out.
- **12:23** *rēx Gojōrum in Galgalīs*: the Hebrew; the BSB with it ("Goiim in Gilgal", note "Hebrew; LXX Goyim in
  Galilee"); only the NRSVue follows the Greek ("Galilee", "Gk: Heb *Gilgal*"). One Bible only.
- **13:26** *ad fīnēs Dabīris*: Castellio goes with the versions and with both Bibles (NRSVue "Debir", "Gk Syr Vg: Heb
  *Lidebir*"; BSB the same with note). Nothing to note (Gen 4:8 principle).
- **14:10–11** (numerals): 45 years and 85 years both present; the 85 moved from 14:10 into 14:11 (words moved).
- **8:17** (short verse): its opening is in 8:16 *ita, ut nēmine Hāī aut Bēthēle relictō*; words moved. Castellio keeps
  the Hebrew's "or Bethel" with the BSB; only the NRSVue drops it ("Gk: Heb adds *or Bethel*").

**Numbers checked against the Hebrew**: 8:3 30,000; 8:12 5,000; 8:25 12,000; 12:24 thirty-one kings (Castellio's list
in 12:9–24 counts 31); 13:30 sixty towns; 14:7 forty; 14:10–11 forty-five, eighty-five. All match.

**Only one of the two Bibles leaves the Hebrew** (Castellio with the Hebrew and the BSB): 8:17 (above); 9:14 (NRSVue
"the leaders", "Gk: Heb *men*"; Castellio *hominēs*); 10:2 (NRSVue "he", "Heb ms Syr ms Vg: MT *they*"; Castellio's
singular *perculsus est* at the end of 10:1, a construal either way); 12:23 (above).

**Disputed or uncertain Hebrew**: 9:4 *Simulātā enim lēgātiōne* (the Hebrew's "made as if envoys", with the BSB and the
KJV; the NRSVue "prepared provisions", "Heb mss Gk Syr: Meaning of MT uncertain").

**Construals the context sets right, or names translated** (`num-notes.md` §F; Deut 1:1, Judg 8:13):
- 8:15 *ab iīs fūsī in silvam fugerent* (the Hebrew: they let themselves be beaten, feigning; 1738 line 197 *fusi in
  siluam*): 8:6 *nōbīs enim fugam simulantibus* has already told the reader the flight is a feint. *silva* for the
  wilderness also at 8:20–21, 8:24: vocabulary.
- 9:21 *Igitur hoc cīvitās prīmōribus concessit* for "as the leaders had said to them": the outcome (the Gibeonites
  spared as servants) stands.
- 11:8, 13:6 *ad aquārum incendia* (Misrephoth-maim, "burnings of waters", the KJV margin's sense); 11:17, 12:7 *monte
  glabrō* (Halak, "smooth"); 13:4 *Sīdōnius recessus* (Mearah, "cave"); 10:13 *in librō rēctī* (Jashar): names
  translated, as Deut 1:1.
- 11:13 *oppidōrum, quæ in integrō mānsērunt* for the towns on their mounds (NRSVue "stood on mounds"): the old reading
  (KJV "stood still in their strength"); the sense (Israel burned none but Hazor) stands.
- 13:17 *Bēthbaal, Meōn* for one town Beth-baal-meon (1738 line 366, 1750 OCR line 31781 print the comma; flagged in
  `josh1-24-stages3-5.md`): a name divided in a list; nothing in the story turns on it. Below the bar.

**Vocabulary**: 8:29, 10:26–27 *crux*, *patibulum* for the tree; 9:23, 9:27 *fānum*, *lixæ*; 13:14 *rēs dīvīna* for the
fire offerings; 13:21 *satrapæ*; 8:33 *senātōrēs*, *magistrātūs*.

**Paraphrase or words moved**: 8:1–2 (in indirect speech), 8:9–13, 8:16–17, 8:18 (the LORD's command condensed into
*mandante Jōvā*), 8:30–35 (Moses' command moved from 8:31 to 8:30; 8:33's blessing moved into 8:34), 9:7–8, 9:16–19,
10:7–10, 10:15–17, 10:23–24, 10:36–39, 11:1–2, 11:6–9, 11:17–18, 11:21–22, 12:7–8, 13:2–3 (Shihor moved up), 13:6–7
(the lot moved into 13:7), 13:12–13 (Moses' conquest moved into 13:13), 14:1–2 (the lot in 14:1).

**1738's footnotes and Castellio's 1554 annotations**: not read here (the other reader's); none bears on 13:3 as far as
the stage files show.

## Joshua 15–24: light notes (reader 3)

Read 2026-11-19 by the process in `ot-notes-process.md` (§§1–3, 5), with the bar as `judg-notes.md` and `num-notes.md` §F
leave it. Every verse of 15–24 in `text/JOS.usfm` (via `data/gold/Josh.tsv`) was read against the KJV and the BSB, with
the WLC, the Vulgate and Brenton's LXX wherever a verse looked odd (15:4, 15:18, 16:2, 16:10, 17:8, 18:18, 18:28, 23:5).
The BSB's footnotes were taken from `josh-notes-candidates.md`. The NRSVue (Bible Gateway, read 2026-11-19) was fetched
one chapter per fetch for all ten chapters with its footnotes. None of it was stored. I re-fetched 15:47–63 and 15:59–60
on their own to check the expected Greek passage. The NET (Bible Gateway) was read for 23:4–5 only. The lists in 15–21
were read for numbers, for passages added or missing, and for one place changed into another. 1738 was checked as
printed (`text/orig/JOS.usfm`) and in its raw OCR, 1750 in its raw OCR, 1573 through the MDZ search API and the hOCR of
canvas 166, and 1554 (MDZ bsb10196330) through its search API and the hOCR of canvas 132. No page image was read.

**Two things the brief expected that the NRSVue on Bible Gateway does not have:**
- **15:59:** the NRSVue there has no added passage. It reads only "Maarath, Beth-anoth, and Eltekon: six towns with their
  villages." I searched the page for "Tekoa", "Ephrathah" and "Bether" and found none of them, and the verse has no
  footnote. The BSB and the KJV lack the passage too, and so does Castellio (*Marēth, Bēthanōth et Eltecōn, oppida sex
  cum suīs pāgīs*). Nothing to note.
- **21:36–37:** the verses are present in the NRSVue (Bezer, Jahzah, Kedemoth, Mephaath: four towns), with no footnote.
  The BSB, the KJV and Castellio (*Beser, Jāsa, Cedēmōtha et Mēphāath, oppida quattuor*) have them as well. Nothing to note.

The yield is 1 note proposed in 10 chapters (0.1 a chapter), plus one place near the bar (23:5) that I recommend leaving out.

### C. A reading Castellio marked as taken from the Greek (kind C)

1. **16:10** *…sed tribūtāriī, dōnec Pharaō Ægyptī rēx expedītiōnem fēcit, urbemque cēpit ac ignī cremāvit, et Chananæōs
   et Pherezæōs Gazerēnsēsque cōnfōdit, urbemque fīliæ suæ dōtis nōmine dedit.*
   - **Hebrew:** the verse ends at וַיְהִי לְמַס־עֹבֵד, "and they became forced labourers".
   - **The modern Bibles:** the NRSVue "…have lived within Ephraim to this day but have been made to do forced labor"
     (no footnote; only a cross-reference "Josh 17.12; Judg 1.29; 1 Kings 9.16"). The BSB "…to this day, but they are
     forced laborers" (no note). The KJV and the Vulgate (*usque in diem hanc tributarius*) end there too.
   - **Castellio's source:** Brenton's LXX adds ἕως ἀνέβη Φαραὼ βασιλεὺς Αἰγύπτου, καὶ ἔλαβεν αὐτὴν, καὶ ἐνέπρησεν αὐτὴν ἐν
     πυρί· καὶ τοὺς Χαναναίους, καὶ τοὺς Φερεζαίους, καὶ τοὺς κατοικοῦντας ἐν Γαζὲρ, ἐξεκέντησαν· καὶ ἔδωκεν αὐτὴν Φαραὼ ἐν
     φερνῇ τῇ θυγατρὶ αὐτοῦ. Castellio's clause renders it word for word. It is the event the Hebrew tells only at
     1 Kgs 9:16, which 1573 renders in its place (canvas 237, *Pharao rex Egypti fecit expeditionem … filiæ suæ Solomonis
     vxori dotis nomine dedit*).
   - **Marked by Castellio:** 1738 prints *sed tributarii. G. donec Pharao … dotis nomine dedit. H.* (`text/orig/JOS.usfm`
     line 479; raw OCR lines 32496–32503, *G. donee Pharao Aegypti* … *nomine dedit. H.*). The *H.* closes the passage at
     the end of 16:10, so the whole of the addition lies in this verse.
   - **The printings differ, which bears on the edition history.**
     - **1554** (Castellio's lifetime, MDZ bsb10196330, hOCR canvas 132) has it with both marks: *sed tributarij, G. donec
       Pharao Aegypti rex expeditionem fecit, … urbemque filiæ suæ dotis nomine dedit. H.* This is the comma the settled
       text has.
     - **1573** omits it. The hOCR of canvas 166 ends the verse *ſed tributarij.* and goes straight to CAPVT XVII; neither
       "Pharao" nor "dotis" is on the page.
     - **1750** omits it as well (raw OCR line 32230 *fed tri-|butarii:*, then CAPVT XVII). "confodit" occurs nowhere in
       its Joshua.
   - **Why it is a note:** the reading is Castellio's own (1554) and the base edition's (1738). A reader with the NRSVue
     or the BSB meets a whole event (Pharaoh burns Gezer and gives it as a dowry) that neither prints. It also turns the
     Hebrew's "to this day" into "until Pharaoh…". This is the case of Num 10:6 and Exod 2:22: a marked addition the
     modern Bibles do not print. It is not the case of Judg 16:13–14, where the modern Bibles add the marked words too.
     Judg 1:29 *sed tribūtum pendentēs* was left out as small, but this addition is a full narrative clause. The Hebrew is
     not disputed: the NRSVue has no footnote and no "uncertain".
   - **Recommendation (reader 3): propose.** The form is that of Exod 2:22 and Num 10:6. Every Latin word was checked
     with `latin macron`: *dōnec*, *Pharaō*, *Græcō*, *addit*, *Hebraicē*, *nōn*, *est*; *Castelliō* is as in the existing
     notes. The old text occurs once in the file (`text/JOS.usfm` line 547).
   - **For `docs/editions.md`:** that 1554 has the passage and 1573 and 1750 do not is a fact for it. The 1738 entry there
     records only 1738.

   **Apply:** `Josh.16.10` la: `urbemque fīliæ suæ dōtis nōmine dedit.` → `urbemque fīliæ suæ dōtis nōmine dedit\f + \fr 16:10 \ft ‘dōnec Pharaō … dedit’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*.`

### B. Castellio's reading departs from the Hebrew (kind B), near the bar

2. **23:5** *Cēterum ipse Jōva Deus vester eās vōbīs fugāvit extermināvitque, et vōs eārum terram occupāstis*
   - **What Castellio does:** he puts in the past what the Hebrew promises for the future. The Hebrew has
     יֶהְדֳּפֵם … וְהוֹרִישׁ אֹתָם … וִירִשְׁתֶּם אֶת־אַרְצָם (yiqtol, then weqatal). The NRSVue reads "The Lord your God will push
     them back before you and drive them out of your sight, and you shall possess their land" (no footnote). The BSB "will
     push them out … so that you can take possession", the KJV "he shall expel them … ye shall possess", the Vulgate
     *disperdet … auferet … possidebitis*, and Brenton's LXX ἐξολοθρεύσει … κατακληρονομήσετε are all future. The NET is
     also future, with no note on the tense.
   - **Not a printer's slip:** 1738 *fugauit exterminauitque … occupastis* (`text/orig` line 692; raw OCR line 33372),
     1750 the same (raw OCR line 33202), 1573 *fugauit, exterminauit, & vos earum terram occupaſtis* (canvas 170).
   - **Why it matters:** in the Hebrew the nations left over (23:4) are still to be driven out, and that promise is what
     23:12–13 makes conditional.
   - **Against a note:**
     - Castellio's own context sets it right: 23:4 *reliquārum adhūc hārum nātiōnum*, 23:7 *istīs reliquīs apud vōs
       nātiōnibus*, 23:12–13 *nōn jam vōbīs istās omnēs nātiōnēs expulsūrum esse*.
     - 23:4 itself joins "these remaining nations" to "all the nations I have cut off". The NET's note on 23:4 calls that
       relationship "difficult to understand", and Castellio's past tense reads *eās* as the nations already conquered.
     - It is a tense in a secondary clause, the kind of construal `num-notes.md` §F left out (Num 14:25).
   - **Recommendation (reader 3): leave out.**

   **Apply (only if accepted against the recommendation):** `Josh.23.5` la: `eās vōbīs fugāvit extermināvitque,` → `eās vōbīs fugāvit extermināvitque\f + \fr 23:5 \ft Hebraicē יֶהְדֳּפֵם … וְהוֹרִישׁ … וִירִשְׁתֶּם, ‘expellet … exterminābit … et possidēbitis’.\f*,`

   I checked the Latin words with `latin macron`: *expellet*, *exterminābit*, *possidēbitis*. I have not run this line
   through `review check`; the old text occurs once (line 787).

### Considered and left out

**The tool's candidates in 15–24:**
- **15:4** (BSB: LXX "their"; Hebrew "your"): Castellio *eōrum terminus* goes the BSB's way. The NRSVue keeps "your south
  boundary". Only one of the two Bibles leaves the Hebrew, and it is a pronoun with the same sense.
- **15:18** (BSB: Hebrew "she urged him"; other LXX mss "he urged her"): Castellio *cum ā marītō impetrāsset, ut ā patre
  suō agrum peteret* keeps the Hebrew, as the NRSVue does ("she urged him to ask her father"). *gemēbat ex asinō* (the
  Vulgate's *suspiravit*, for the rare וַתִּצְנַח "dismounted") is the same as Judg 1:14, which was left out. It is a rare
  word, and the bride's request is the same.
- **16:2** (BSB: LXX "Bethel (that is, Luz)"): Castellio *inde ad Lūzam* (from Bethel, named at the end of 16:1, to Luz)
  is the Hebrew. The NRSVue keeps the Hebrew too ("from Bethel to Luz"), so only the BSB leaves it.
- **16:10:** proposed above.
- **18:18** (BSB: LXX "northern slope of Beth-arabah"; NRSVue "Gk: Heb *to the slope over against the Arabah*"): this is
  kind A by the test. Both Bibles leave the Hebrew, and Castellio keeps it (*ad latus positum in fronte septentriōnālis
  campī*; 1738 `text/orig` line 522). Only one point on a border line changes, so it is left out as Judg 20:33 and
  Deut 11:30 were. His *prōgressumque ad septentriōnāle Bēthaglæ latus* is 18:19's opening, moved.
- **18:28** (BSB and NRSVue: Gk Syr Vg "Jebus", Heb "the Jebusite"; Gk "Kiriath-jearim", Heb "Kiriath"):
  - *Jebūsī, aliās Hierosolyma* is the Hebrew with the same sense.
  - *Cariathaim* (1738 the same) is neither the Hebrew's bare קִרְיַת nor the versions' Kiriath-jearim. Castellio spells
    Reuben's Kiriathaim the same way (Num 32:37 *Cariāthaim*, Josh 13:19 *Cariāthaimum*).
  - Near the Judg 4:5 kind (a place changed into another), but the Hebrew name itself is defective and both modern Bibles
    emend it. In a town list nothing turns on it, and Kiriath-jearim is Judah's (15:60, 18:14) on their reading anyway.
    Left out as a name.
- **19:34** (BSB: Hebrew "Judah at the Jordan"; LXX differs): Castellio *Jūdæīs Jordāne orientālī* is the Hebrew. The
  NRSVue keeps it too and has no note.
- **Numbers** 22:14, 22:21, 22:30, 23:10, 24:31: every numeral matches. The "thousands of Israel" become *cōpiārum
  Isrāēlīticārum* (his vocabulary), *mīllēnōs* is 23:10's thousand, and 24:31 has no number on either side (the tool read
  *senum* as a numeral).
- **Short 22:13**: the three tribes named in the Hebrew are *eōs* (22:12–13 continue 22:11's sentence). Words carried, not
  lost.

**The town counts in 15–21:** all match the Hebrew and the NRSVue: 15:32 (29), 36 (14), 41 (16), 44 (9), 51 (11; *præter
eōrum pāgōs*, the same sense), 54 (9), 57 (10), 59 (6), 60 (2), 62 (6); 18:24 (12), 28 (14); 19:6 (13), 7 (4), 15 (12),
22 (16), 30 (22), 38 (19); 21:4–7 (13, 10, 13, 12), 16 (9), 18 (4), 19 (13), 22, 24 (4), 25 (2), 26 (10), 27 (2), 29, 31
(4), 32 (3), 33 (13), 35, 37, 39 (4), 40 (12), 41 (48). 19:2–6 lists Saba beside Bersaba as the Hebrew does (fourteen
names for "thirteen"), with the NRSVue.

**Other places weighed:**
- **24:11:** Castellio's list of the nations lacks the Hivites. He has six (*Amorræōs, Pherezæōs, Chananæōs, Hettæōs,
  Gergesæōs et Jebūsæōs*); the Hebrew, the NRSVue and the BSB have seven. It is not a slip of one printing: 1573 canvas
  170, 1738 `text/orig` line 719 and 1750 raw OCR line 33345 all have the six. One name dropped from a stock list changes
  nothing in the story, so it is below the bar.
- **17:8:** *cujus Taphūæ terra est Manassēnsium, Ephrāimītīs fīnitima* leaves out that the town of Tappuah itself was
  Ephraim's (the Hebrew's וְתַפּוּחַ … לִבְנֵי אֶפְרָיִם). This is close to the Vulgate's construal (*quæ est juxta terminos
  Manasse filiorum Ephraim*), and 16:8–9 and 17:9 give the reader the Ephraimite towns inside Manasseh. Below the bar.
- **15:61** *In silvīs* for בַּמִּדְבָּר: Castellio's regular word for this (Josh 8:15, 8:24, 12:8; Judg 20:42), so it is
  vocabulary.
- **19:13** *Remmōnem, Methōār et Nēam*: the Hebrew's הַמְּתֹאָר ("curving") taken as a town, as the KJV's "Remmon-methoar".
  A name.
- **22:34** *āram Ēd*: Castellio names the altar, as the NRSVue ("Witness"; "Heb mss Syr: MT lacks *Witness*"), the BSB and
  the KJV do. Nothing to note. 1738's footnote there is the other reader's.
- **22:10–11** *ad rīpam Jordānis* for גְּלִילוֹת: the NRSVue "region" ("Or *to Geliloth*"), the BSB "Geliloth". The two
  Bibles disagree, so no note. 22:11 *exadversum Isrāēlītīs* for אֶל־עֵבֶר בְּנֵי יִשְׂרָאֵל keeps the sense.
- **Disputed Hebrew** (the NRSVue "Meaning of Heb uncertain"): 17:11 *trēs tractūs*, 18:15, 24:12 (the hornets).
- **Words moved or condensed:** 15:2–3 (Akrabbim and Zin in 15:2), 18:18–19, 19:8–9, 19:49–50 (*ex Jōvæ præceptō*), 21:21–22
  (Gezer), 22:22–23, 24:6–8 (the years in the wilderness in 24:8).
- **The NRSVue's other footnotes in 15–24:** 15:2, 15:5, 18:19 "Heb *Salt Sea*"; 15:13 "Heb *he*"; 19:29 "Cn Compare Gk:
  Heb *Mehebel*" (the NRSVue alone; Castellio's *ā sorte Axībæ* reads מֵחֶבֶל as a common noun, as the BSB's "in the region of Achzib" does); 22:19 "Or *make rebels of us*"; 24:6 "Or
  *Sea of Reeds*"; 24:32 "Heb *one hundred qesitah*" (Castellio *centum quessitis*, a measure). Chapters 16, 20, 21 and 23
  have cross-references only. None of these bears on a note.
