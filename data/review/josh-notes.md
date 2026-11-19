# Joshua: light notes (Old Testament search)

Built 2026-11-19 by the process in `ot-notes-process.md` (decisions 1A–4A), as Judges' (`judg-notes.md`), with the bar
as the Numbers pass left it (`num-notes.md` §F: a construal the context sets right is left out). Nathan: "Start the notes
for Joshua, the same way". Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio
keeps it; kinds B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew
agreeing, and nobody calls the passage uncertain. Castellio's 1554 annotations on Joshua, read on the page in this pass,
are in `josh-notes-1554.md`: none proposes a note.

**Sources read:**
- `josh-notes-candidates.md` (`python -m pipeline notes Josh`): 10 BSB version notes, 12 numbers, 3 short verses, and
  Castellio's *G.* … *H.* at 16:10 (§C).
- The NRSVue (Bible Gateway, read 2026-11-19) for all 24 chapters with its footnotes, one chapter per fetch, by three
  readers (1–7, 8–14, 15–24), each reading the Latin verse by verse against the KJV and the BSB with its footnotes, with
  the WLC, the Vulgate and Brenton's LXX where a verse looked odd; the NET for 23:4–5. Their notes:
  `josh-notes-readers.md`. Each item below was checked here against the files (the settled text, the WLC, the Vulgate,
  the BSB).
- The printings: 1738 as printed (`text/orig/JOS.usfm`) and its raw OCR, the 1750 raw OCR (`sources/archive/`), 1573
  through the MDZ search API and hOCR, and **page images read by Claude** for 16:10 (1554 canvas 132, 1573 canvas 166) and
  23:5 (1554 canvas 136). Every reading noted is Castellio's own text, not a printer's slip.

The yield is 2 notes proposed in 24 chapters (0.08 a chapter), 6:23 and 16:10; 13:3 left out on Nathan's standard of
2026-11-19 (no plot or theological significance), and one more place near the bar recommended left out (23:5).

## A. Modern Bibles follow the versions (kind A)

None proposed. The two places where both Bibles leave the Hebrew are border details (§E: 12:4, 18:18).

## B. Castellio's reading or text departs from the Hebrew (kinds B and C)

**Decision:** accept item 1; item 2 left out (Nathan, 2026-11-19: "Apply all", after "Minor notes … can be dropped")

1. **6:23** *cumque omnī suā propinquitāte forās in castra Isrāēlītārum ēdūxērunt, et ibi relīquērunt*: Hebrew
   וַיַּנִּיחוּם מִחוּץ לְמַחֲנֵה יִשְׂרָאֵל, "and they left them **outside** the camp of Israel" (the NRSVue "set them outside
   the camp of Israel", the BSB "settled them outside the camp of Israel", neither with a note; the KJV "without the
   camp"; the Vulgate *extra castra Israël manere fecerunt*; Brenton's LXX ἔξω τῆς παρεμβολῆς). Castellio brings Rahab's
   family out of the city *in castra* and leaves them there: inside the camp, where every witness puts them outside it
   (her living *inter Isrāēlītās* comes at 6:25). A plain phrase turned to its opposite; it bears on the story (the
   unclean outsiders kept outside the camp until they are received, 6:25), so it passes the standard of 2026-11-19.
   1738 *foras in castra Israelitarum eduxerunt, et ibi reliquerunt* (`text/orig` line
   146), 1750 (OCR lines 30605–30607), 1573 *forâs in castra Israelitarum eduxerunt* (canvas 159, OCR) the same.
   **Recommendation (Claude): note.**
   **Apply:** `Josh.6.23` la: `forās in castra Isrāēlītārum ēdūxērunt,` → `forās in castra Isrāēlītārum\f + \fr 6:23 \ft Hebraicē מִחוּץ לְמַחֲנֵה יִשְׂרָאֵל, ‘extrā castra Isrāēlītārum’.\f* ēdūxērunt,`
2. **13:3** *quīnque Palæstīnōrum præfectūræ, Gazēa, Azōtēnsis, Ascalōnēnsis, Gethēnsis, Accarōnēnsis et Hevæēnsis*,
   **near the bar**: Hebrew … וְהָעֶקְרוֹנִי וְהָעַוִּים, "the Ekronites; and the Avvim" (the NRSVue "and those of the Avvim",
   the BSB "as well as that of the Avvites", neither with a note; the KJV "the Avites"). Castellio follows Brenton's
   LXX καὶ τῷ Εὐαίῳ and makes the Avvim into the Hivites: *Hevæ-* is his stem for the Hivites (חִוִּי) of Gibeon and
   Hermon (9:1, 9:7, 11:3, 11:19), while the Avvim are *Aviōs* in the settled Deut 2:23 (the same people, in the same
   corner, "as far as Gaza") and their town *Avīm* at 18:23. So his reader meets a Hivite district among the Philistine
   cities, a people his own text keeps apart. The Vulgate has no Avvim in 13:3. 1738 *accaronensis et heuæensis*
   (`text/orig` line 352), 1750 (OCR lines 31703–31704), 1573 *Accaronenſis, & Heuæenſis* (canvas 164, OCR) the same;
   the names reader saw it in stage 5 (`josh1-24-names.md` call 13) and kept it as his rendering. Against a note: it is
   a name in a list. **Left out** (Nathan, 2026-11-19: "Minor notes (e.g. rare names in lists) that don't really have
   any plot or theological significance can be dropped"; Claude had recommended it on the Judg 4:5 precedent, which
   goes too, `notes-minor.md`).
   **Apply (only if accepted against the decision):** `Josh.13.3` la: `Accarōnēnsis et Hevæēnsis:` → `Accarōnēnsis et Hevæēnsis\f + \fr 13:3 \ft Hebraicē הָעַוִּים, ‘Aviī’.\f*:`

## C. A reading Castellio marked as taken from the Greek (kind C)

As Exod 2:22 and Num 10:6: the edition doesn't print his *G.* … *H.* marks, so where the modern Bibles keep the Hebrew
the note tells the reader what the marks told him.

**Decision:** accept (Nathan, 2026-11-19: "Apply all")

3. **16:10** *…sed tribūtāriī, dōnec Pharaō Ægyptī rēx expedītiōnem fēcit, urbemque cēpit ac ignī cremāvit, et
   Chananæōs et Pherezæōs Gazerēnsēsque cōnfōdit, urbemque fīliæ suæ dōtis nōmine dedit.* The Hebrew ends at
   וַיְהִי לְמַס־עֹבֵד, "and they became forced labourers"; the NRSVue ("but have been made to do forced labor") and the BSB
   ("but they are forced laborers") end there, with no note, as the KJV and the Vulgate do. The clause is the
   Septuagint's (Brenton: ἕως ἀνέβη Φαραὼ βασιλεὺς Αἰγύπτου … καὶ ἔδωκεν αὐτὴν Φαραὼ ἐν φερνῇ τῇ θυγατρὶ αὐτοῦ), the event
   the Hebrew tells only at 1 Kgs 9:16. A reader with a modern Bible meets a whole event (Pharaoh burns Gezer and gives it
   as a dowry) that neither prints, and "to this day" becomes "until Pharaoh …". Unlike Judg 16:13–14, the modern Bibles
   do not add it.
   - **1554** (Castellio's lifetime, MDZ bsb10196330 canvas 132, column 240, image read): *ſed tributarij, G. donec
     Pharao Aegypti rex expeditionem fecit, urbemq; cæpit, ac igni cremauit, & Chananæos & Pherezęos Gazerenſeſque
     confodit, urbemq; filiæ ſuæ dotis nomine dedit. H.*: the clause with both marks.
   - **1738** the same, with the marks (`text/orig` line 479; leaf 283).
   - **1573** (bsb10141277 canvas 166, column 288, image read): *10 Quanquam Gazerenſes Chananæos non eiecerunt,
     habitantq; adhuc Chananęi inter Ephraimitas, ſed tributarij.*, then CAPVT XVII: **the clause is not there.**
   - **1750**: not there either (raw OCR line 32230, then CAPVT XVII; OCR only).
   So the marked reading is Castellio's own, and 1573 drops it; whether he dropped it in his last revision or his
   posthumous editor did cannot be told from the print (as with 1573's other changes, `docs/editions.md`). The edited
   text follows the base edition, 1738 (decision 1), and keeps it; the note says what it is. If Nathan prefers 1573's
   shorter verse, that is a change to the settled text, not a note, and would need its own proposal.
   **Recommendation (Claude): note.**
   **Apply:** `Josh.16.10` la: `urbemque fīliæ suæ dōtis nōmine dedit.` → `urbemque fīliæ suæ dōtis nōmine dedit\f + \fr 16:10 \ft ‘dōnec Pharaō … dedit’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*.`

## D. Near the bar, recommended left out

**Decision:** left out, as recommended (Nathan, 2026-11-19: "Apply all")

4. **23:5** *Cēterum ipse Jōva Deus vester eās vōbīs fugāvit extermināvitque, et vōs eārum terram occupāstis*: Castellio
   puts in the past what the Hebrew promises (יֶהְדֳּפֵם … וְהוֹרִישׁ … וִירִשְׁתֶּם, "he will push them back … drive them out …
   you shall possess"; the NRSVue, the BSB, the KJV, the Vulgate *disperdet … possidebitis* and the LXX, all future).
   His own, in 1554 too (canvas 136, column 247, image read: *eas uobis fugauit, exterminauitq;, & uos earū terrā
   occupaſtis*), 1573 (canvas 170, OCR), 1738, 1750. But his context sets the sense right (23:4 *reliquārum adhūc hārum
   nātiōnum*, 23:7, 23:12–13: nations remain), 23:4's joining of the remaining and the conquered nations is itself hard
   (the NET's note), and it is a tense in a secondary clause, the kind left out at Num 14:25. **Recommendation (Claude):
   leave out.**
   **Apply (only if accepted against the recommendation):** `Josh.23.5` la: `eās vōbīs fugāvit extermināvitque,` → `eās vōbīs fugāvit extermināvitque\f + \fr 23:5 \ft Hebraicē יֶהְדֳּפֵם … וְהוֹרִישׁ … וִירִשְׁתֶּם, ‘expellet … exterminābit … et possidēbitis’.\f*,`

## E. Considered and left out (the readers' full lists: `josh-notes-readers.md`)

- **The tool's candidates**: 7:1 *Zabdis* (the Hebrew, with both Bibles); 12:4 (both Bibles follow the Greek, "Og"
  for "the territory of Og": only the list's frame changes, as Judg 9:29); 12:23 Gilgal (only the NRSVue has Galilee);
  13:26 *Dabīris* (Castellio already with both Bibles); 15:4 (a pronoun, only the BSB); 15:18 (the Hebrew, as Judg 1:14);
  16:2 (only the BSB leaves the Hebrew); 18:18 (both Bibles follow the Greek, Castellio the Hebrew; one point on a border
  moves, as Judg 20:33 and Deut 11:30); 18:28 *Cariathaim* (the Hebrew's name is itself defective, both Bibles emend it;
  a name in a list); 19:34 (the Hebrew, with both). Every numeral matches the Hebrew (the dual and the ordinals, numbers
  carried across verses at 5:2–3, 14:10–11), and every town count in 15–21. The short verses 5:2, 8:17 and 22:13 are
  words moved.
- **The NRSVue's expected additions**: 15:59 (no added passage on Bible Gateway's NRSVue; Castellio, the BSB and the KJV
  have none) and 21:36–37 (present in all, no note). Nothing to note.
- **Below the bar**: 1:14 (the livestock left out of a list); 5:6 *majōribus nostrīs* (a pronoun); 6:9, 6:13 *vulgō* for
  the rear guard (the Vulgate's construal); 13:17 *Bēthbaal, Meōn* (one town divided, 1738 prints the comma); 17:8
  (Tappuah's owner compressed, near the Vulgate); 24:11 (the Hivites missing from the list of seven nations, in 1573
  canvas 170, 1738 and 1750: one name in a stock list).
- **Construals the context sets right, and names translated** (`num-notes.md` §F): 8:15 *fūsī* (8:6 has told the reader
  the flight is feigned); 9:21; 11:13; Misrephoth-maim (*aquārum incendia*), Halak (*mōns glaber*), Mearah, the book of
  Jashar (*liber rēctī*); 19:13 *Methōār*; 22:10–11 Geliloth (the two Bibles differ).
- **Only one of the two Bibles leaves the Hebrew** (Castellio with the Hebrew): 2:4, 5:1, 6:18, 6:25, 7:17, 8:17, 9:14,
  10:2, 12:23, 15:4, 16:2, 19:29.
- **Disputed or uncertain Hebrew**: 9:4 (*Simulātā lēgātiōne*), 17:11, 18:15, 24:12.
- **1738's footnotes** (both Castellio's 1554 margins, `josh-notes-1554.md`): **7:24** *idem Achor et Achan est* (the
  mark after *Achoris*; `docs/editions.md` and HUMAN.md had placed it at 7:1) and **22:34** *hoc est,
  testis* (the altar *Ēd*, which the settled verse already explains: *quod ea testis esset*). Glosses, not departures.
