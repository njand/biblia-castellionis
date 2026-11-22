# 1 Kings 1–11: light notes (Old Testament search), reader A

Built 2026-11-22 in phase 2 of decision 85 (PLAN.md §4), beside `propose`, by the process in `ot-notes-process.md`
(decisions 1A–4A), as 2 Samuel's (`../2sam1-24-phase2/notes-a.md`, `notes-b.md`, settled 2026-11-21), with the bar as it
now stands (Nathan, 2026-11-19: no note for a departure without plot or theological significance, a name, place or
number included; 2026-11-21: a name that changes who did or suffered what, or makes the book contradict itself, with
the modern Bibles agreeing against Castellio, does get one; `num-notes.md` §F: a construal the context sets right is
left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio keeps it;
kinds B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew
agreeing, and nobody calls the passage uncertain. Chapters 12–22 are reader B's. Castellio's 1554 annotations on these
chapters and the 1554 text's margins, read on the page in this pass, are in `notes-1554-a.md`. Names in note text as
the preview has them after `names.md` (*Absālōmum* as settled in `text/2SA.usfm`; *Chamōssum*, *Cerēthæī*,
*Phelethæī*, *Mōabītārum* as `text/draft/1KI.preview.usfm`).

**Sources read:**
- `../1kgs-notes-candidates.md` (`python -m pipeline notes 1Kgs`), its entries for chapters 1–11: Castellio's marks at
  2:12, 2:28 and 8:55 (8:55 is a false placement: the 1750 OCR line *exfecutumiuit. G. Deumque tot eius opera
  recordans* is Esther's Greek addition, `sources/archive/1750/text.txt` line 77178, not 1 Kings); 7 BSB *against MT*
  (4:19, 4:26, 5:11, 6:8, 7:7, 7:40, 9:8), 7 *with MT* (1:25, 2:5, 5:16, 6:1, 7:17, 11:33), 5 *other* (1:48, 7:26,
  8:12, 9:26, 10:8), 22 numbers, 1 short (6:25). Also 1:8's and 11:5's *L. … H.*, which the tool does not list
  (`../1kgs1-22-transcription.md` § Footnotes and Castellio's marks).
- The NRSVue (Bible Gateway, read 2026-11-22) for chapters 1–11 with all its footnotes (not stored). The NET was not
  read. The verses below read in the preview (`text/draft/1KI.preview.usfm`) and the printed text
  (`text/orig/1KI.usfm`) against the BSB, the WLC, the Clementine Vulgate, Brenton's LXX and the KJV
  (`sources/parallel/`); the verse readers' reports `r1.md`–`r5.md` (r5 left 10:27 *aurī* for the notes; none flagged
  anything else for them).
- 1738's 4 footnotes and 15 asterisks in these chapters, from phase 1 (`data/witnesses/read-1738/1Kgs1-22.tsv`,
  `../1kgs1-22-transcription-readers.md`, readers 04, 05, 07).
- The printings: 1738 as printed (`text/orig/1KI.usfm`), the 1750 raw OCR (`sources/archive/1750/text.txt`), **1554**
  (canvases 186–195, 827–833) on page images read here (`notes-1554-a.md`), **1573** through the MDZ search API only.

The yield is **2 notes proposed in 11 chapters** (0.18 a chapter), both Castellio's own *G.* … *H.* passages, whose
marks the edition no longer prints: Solomon's age at 2:12, which the Hebrew never gives and which makes the book
contradict itself, and *Solomōnem* for Absalom at 2:28, which changes what Joab is said to have done. No kind A passes.
Three more of his marked or odd readings are near the bar and recommended left out (11:5, 1:8, 10:27), with 9:8 and
6:8 (kind A by the letter).

## A. Modern Bibles follow the versions (kind A)

None proposed. The places where both the NRSVue and the BSB leave the Hebrew are 6:8 ("lowest/bottom" for "middle":
§C item 7), 7:7 ("to the rafters/ceiling", with the Syriac and the Vulgate: Castellio's *ā pavīmentō ad laquear* is
theirs) and 9:8 ("a heap of ruins/rubble": §C item 6). Everywhere else one of the two keeps the Hebrew (§E).

## B. Castellio's text departs from the Hebrew (kind C)

**Decision:** accept (Nathan, 2026-11-22: "Approve all as recommended")

1. **2:12** *At Solomō in soliō Dāvīdis patris suī cōnsēdit, nātus annōs duodecim, estque ejus rēgnum probē
   cōnfirmātum*: Castellio's **G. … H.** words *natus annos duodecim*, "being twelve years old", which neither the
   Hebrew (וּשְׁלֹמֹה יָשַׁב עַל־כִּסֵּא דָּוִד אָבִיו וַתִּכֹּן מַלְכֻתוֹ מְאֹד, "Solomon sat on the throne of David his father, and his kingdom was
   firmly established") nor the NRSVue nor the BSB has (no note in either), nor the Clementine Vulgate, nor Brenton's
   LXX (*Καὶ Σαλωμὼν ἐκάθισεν ἐπὶ θρόνου Δαυὶδ τοῦ πατρὸς αὐτοῦ, καὶ ἡτοιμάσθη ἡ βασιλεία αὐτοῦ σφόδρα*): his mark
   says it is the Greek's, but the Greek text he read was not seen here.
   **Why it passes the bar**: it gives the king's age at his accession, a fact the Hebrew of Kings never states, and
   it **makes the book contradict itself** (the 2026-11-21 rule, 2 Sam 21:8): with 11:42 (*per annōs quadrāgintā*) and
   14:21 (Rehoboam *ūnum et quadrāgintā annōs nātus*), both the Hebrew's, Castellio's Solomon fathered his heir at
   eleven, a tension the Hebrew does not have. It also colours 3:7 (*quī nec tum per ætātem rēs administrāre sciō*). The
   mark that told Castellio's reader it was the Greek's is gone from the edition (`../1kgs1-22-draft-fixes.md`), as at
   2 Sam 8:7 (accepted 2026-11-21). **Near the bar** in being a number; it is not a number in a list. 1554 (canvas 187,
   column 350, zoom `z187-2_12.jpg`: *At Solomo in ſolio Dauidis patris ſui | cõſedit, G.natus annos 12, H. eſtq; eius
   regnum*), 1738 (`text/orig/1KI.usfm`: *consedit, G. natus annos duodecim, H. estque*), 1750 (OCR, the candidates
   file: *confedit, G. / natus annos duodecim ,H.*) the same; 1573 not found by the search API (queried *duodecim*:
   no hit placed here).
   The form of 2 Sam 8:7. Words checked with `pipeline latin macron-check` (*Hebraicē* as the settled notes have it).
   **Recommendation (Claude): accept.**
   **Apply:** `1Kgs.2.12` la: `nātus annōs duodecim,` → `nātus annōs duodecim\f + \fr 2:12 \ft ‘nātus annōs duodecim’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*,`

2. **2:28** *Hōrum fāmā ad Jōābum perlātā, quī ad Adōniam, nōn ad Solomōnem inclīnāsset, cōnfūgit in Jōvæ
   tabernāculum*: Castellio's **G. L. … H.** word *Solomonem* where the Hebrew has Absalom: כִּי יוֹאָב נָטָה אַחֲרֵי אֲדֹנִיָּה
   וְאַחֲרֵי אַבְשָׁלוֹם לֹא נָטָה, "for Joab had turned after Adonijah, though he had not turned after Absalom". The NRSVue ("had
   not supported Absalom") and the BSB ("but not with Absalom") the Hebrew, with no note in either; the KJV the same.
   Castellio follows the Greek (Brenton's LXX *καὶ ὀπίσω Σαλωμὼν οὐκ ἔκλινε*) and the Vulgate (*et post Salomonem non
   declinasset*), as his *G. L.* says.
   **Why it passes the bar**: a name that **changes what is said of who did what** (the 2026-11-21 rule, 2 Sam 12:31),
   with the modern Bibles agreeing against him. In the Hebrew the narrator sets Joab's support of Adonijah against his
   loyalty in Absalom's revolt; in Castellio he had simply not backed Solomon, which is why he flees. A reader comparing
   a modern Bible meets "Absalom" and nothing to say why the Latin differs. 1554 (canvas 188, column 351, zoom
   `z188-2_28.jpg`: *qui ad A-|donaim, non ad G.L Solomonẽ H.inclinaſſet*), 1573 (canvas 227, search API: *non ad G. L.
   Solomonem H. inclinaſſet*), 1738 (*non ad G. L. Solomonem H. inclinasset*), 1750 (OCR: *ad G. L. SolomonemH.
   inclinaffet*) the same.
   The note's form is Deut's *Castelliō Septuāgintā sequitur* with 1 Sam 5:6's *ut Vulgāta*; *Absālōmum* as
   `text/2SA.usfm`. Words checked with `pipeline latin macron-check`.
   **Recommendation (Claude): accept.**
   **Apply:** `1Kgs.2.28` la: `nōn ad Solomōnem inclīnāsset,` → `nōn ad Solomōnem\f + \fr 2:28 \ft Hebraicē וְאַחֲרֵי אַבְשָׁלוֹם, ‘ad Absālōmum’; Castelliō Septuāgintā sequitur, ut Vulgāta.\f* inclīnāsset,`

## C. Places near the bar (recommended left out)

**Decision:** reject 3, 4, 5, 6, 7 (as recommended, under Nathan, 2026-11-22: "Approve all as recommended")

3. **11:5** *sed etiam Astōrethum Sīdōniōrum, et Chamōssum Mōabītārum deum, et Melcōmum Ammonītārum nefās,
   sequerētur*: Castellio's **L. … H.** words *et Chamosum Moabitarum*, Chemosh named among the gods Solomon followed.
   The Hebrew names Ashtoreth and Milcom only (אַחֲרֵי עַשְׁתֹּרֶת אֱלֹהֵי צִדֹנִים וְאַחֲרֵי מִלְכֹּם שִׁקֻּץ עַמֹּנִים); so the NRSVue and the BSB, with
   no note, and the Clementine Vulgate (*Astarthen … et Moloch*). Brenton's LXX 11:5 has Chemosh (*τῷ Χαμὼς εἰδώλῳ
   Μωὰβ*, of the high place built); Castellio's *L.* source was not found. 1554 (canvas 194, column 364, zoom
   `z194-11_5.jpg`: *ſed etiã Aſtorethum Sidoniorũ, L. & Cha-|moſum Moabitarũ H. deum, & ᵃ Melcomum*), 1573 (the
   search API finds 11:33 only, canvas 239), 1738, 1750 (reader 07: the same marks) alike. A god Solomon worshipped is
   theological matter; but **the chapter says it anyway**: 11:7 (Solomon builds a high place for Chemosh) and 11:33
   (*Chamōssum Mōabītārum*) are the Hebrew's, so the reader is told nothing the Hebrew does not tell two verses later.
   The case of 2 Sam 1:19 (accepted, "adding no new matter") cuts the other way, but that line opened the best-known
   poem of the book; this is a list. **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Kgs.11.5` la: `et Chamōssum Mōabītārum deum,` → `et Chamōssum Mōabītārum\f + \fr 11:5 \ft ‘et Chamōssum Mōabītārum’ Castelliō addit; Hebraicē nōn est.\f* deum,`

4. **1:8** *et Semeis, et Rēis et Cerēthæī et Phelethæī hērōēsque Dāvīdis, ab Adōnia nōn stābant*: Castellio's **L. …
   H.** words *et Cerethæi et Phelethæi*, David's guard added to those who did not side with Adonijah. Not in the Hebrew
   (וְשִׁמְעִי וְרֵעִי וְהַגִּבּוֹרִים אֲשֶׁר לְדָוִד), the NRSVue (which changes *Shimei* and *Rei* to "Shammah and his companions",
   "Lucianic"), the BSB, Brenton's LXX or the Clementine Vulgate (*et robur exercitus David*): source not found. 1554
   (canvas 186, column 348: *& Se-|meis, & Reis, L. & Cerethæi & Phelethæi H. | heroesq; Dauidis*), 1573 (canvas 225,
   search API: *& Reis; L. & Cerethæi & Phelethæi H. heroesque*), 1738 (reader 01) the same. A group's name in a list,
   and it changes nothing that happens: the Cherethites and Pelethites go with Solomon at 1:38 and 1:44 in the Hebrew
   too. Dropped by the rule of 2026-11-19, as 2 Sam 8:13. **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Kgs.1.8` la: `et Cerēthæī et Phelethæī hērōēsque` → `et Cerēthæī et Phelethæī\f + \fr 1:8 \ft ‘et Cerēthæī et Phelethæī’ Castelliō addit; Hebraicē nōn est.\f* hērōēsque`

5. **10:27** *fēcitque rēx, ut et aurī Hierosolymæ nōn minor foret cōpia, quam lapidum*: Hebrew אֶת־הַכֶּסֶף, "the
   silver", as stones in Jerusalem; the NRSVue, the BSB, the KJV and the Vulgate (*abundantia argenti*) silver, no note;
   Brenton's LXX *τὸ χρυσίον καὶ τὸ ἀργύριον*, "the gold and the silver". Castellio's own, not 1738's: 1554 (canvas 194,
   column 364, zoom `z194-10_27.jpg`: *fecitq; rex, ut & auri Hie-|roſolymę non minor foret copia*), 1573 (canvas 238,
   search API: *fecitq; rex, vt & auri Hierofolymæ non minor foret copia*), 1738 and 1750 alike (the transcription's
   wording doubts). Perhaps the Greek's gold, half taken (his *et*, "even gold"). His own 2 Chr 9:27 has silver (1573,
   canvas 289, search API: *tantam Hierofolymis argenti cedrorumq; copiam*), so his Bible differs from itself between
   the parallels; but within Kings 10:21 (*sine argentō, quippe quod … nūllīus habēbātur pretiī*) still stands, and the
   point, Solomon's wealth, is the same. A material, dropped by the rule of 2026-11-19 (Exod 25:5's cedar is the old
   exception, a reading rather than a slip). **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Kgs.10.27` la: `ut et aurī Hierosolymæ` → `ut et aurī\f + \fr 10:27 \ft Hebraicē הַכֶּסֶף, ‘argentī’.\f* Hierosolymæ`

6. **9:8** *et templum istud ostentuī sit, ut prætereuntēs omnēs attonitī sībilent*: kind A by the letter. Hebrew
   וְהַבַּיִת הַזֶּה יִהְיֶה עֶלְיוֹן, "this house shall be high" (the KJV "which is high"); the NRSVue "This house will become a heap
   of ruins" (note "Syr OL: Heb *will become high*"), the BSB "when this temple has become a heap of rubble" (note
   "Some LXX manuscripts, Syriac, and Arabic"). Castellio keeps neither: *ostentuī sit*, "be a spectacle", as the
   Vulgate's *erit in exemplum*; 1554 the same (canvas 193, column 362, *tem-|plum iſtud oſtentui ſit*). The sense the
   modern Bibles recover stands in his Latin: the temple that God casts off (9:7) becomes a sight that passers-by hiss
   at, and they ask why the LORD has done this to it; "ruins" only names how. A construal the context sets right, as
   2 Sam 7:23. **Recommendation (Claude): leave out.**

7. **6:8** *Jānuās habēbant media tabulāta, ā templī dextrō latere*: kind A by the letter: the Hebrew הַצֵּלָע הַתִּיכֹנָה, "the
   middle side-chamber"; the NRSVue "the lower story" ("Gk Tg: Heb *middle*"), the BSB "the bottom floor" ("LXX and
   Targum; Hebrew middle"). Castellio keeps the Hebrew on purpose: his 1554 annotation on 6:5 explains *Harum
   ædicularum media tabulata … ianuas habebant à templi dextro latere* (canvas 827, column 350; `notes-1554-a.md` §1).
   A detail of the building, which way the stair entered: dropped by the rule of 2026-11-19. **Recommendation (Claude):
   leave out.**

## D. 1738's footnotes (recommended: none printed)

**Decision:** none printed (Nathan, 2026-11-22: "Approve all as recommended")

1738 prints 4 lettered footnotes in chapters 1–11 (`%` rows of `data/witnesses/read-1738/1Kgs1-22.tsv`; readers 04, 07).
**All four are Castellio's 1554 margins**, changed only in spelling and letter (`notes-1554-a.md` §3). As in Joshua,
Judges, Ruth and 1–2 Samuel (`../2sam1-24-phase2/notes-a.md` §D), the edition prints no glosses (brief.md: "No marginal
notes or commentary"). Each, with what it glosses:

- **4:13** *b) Gaulonim vocat Iosephus.* (on *Argōbiæ*, the region of Argob: Josephus' name for it).
- **6:7** *c) quadrabantur in lapicidinis lapides, quo minores aducherentur.* (on *Templum*: the stones were squared in
  the quarry; 1738's *aducherentur* is a misprint of 1554's *aduehe-|rentur*, kept as printed in `text/orig/`).
- **11:5** *a) idem mox Molochus adpellatur.* (on *Melcōmum*: the same god is called Moloch at 11:7).
- **11:36** *b) posteritatem.* (on *lucernam*, David's lamp: his line; the NRSVue and the BSB "a lamp").

None marks a departure from the Hebrew. **Recommendation (Claude):** print none.

## E. 1738's asterisks

1738's fifteen asterisks in these chapters (5:9; 6:2, 6:4, 6:5, 6:23, 6:31; 7:2, 7:15, 7:23, 7:28, 7:29, 7:30 twice, 7:31;
10:11, on the KJV's numbering; readers 04, 05, 07) **each stand at the place of one of Castellio's 1554 annotations
*IN III. REGVM*** (canvases 827–833; `notes-1554-a.md` §2), as in Ruth and 1–2 Samuel. The edition prints no asterisks.
The annotations are on the timber, the temple's measures and the furnishings of Hiram's bronze work (ch. 5–7, with
woodcuts), and the almug wood of 10:11: commentary on words where no reader comparing a modern Bible is misled, or
choices of a tree or a furnishing the rule of 2026-11-19 leaves out (6:23's and 6:31–33's *cupressina* for the
Hebrew's "olive wood", taken from the Greek, as his annotation says; 10:11 *piceæ*, the Hebrew's almug, from the Greek
and Josephus). None meets the bar. The 6:8 reading his annotation defends is item 7.

## F. Considered and left out

- **The tool's candidates**, besides the items above: **4:19** *ūnā præfectūrā comprehēnsam* (the BSB alone, with some
  LXX manuscripts, "one governor in the land of Judah"; the NRSVue no note); **4:26** *quadrāgintā præsēpiōrum mīllia*
  (the BSB alone 4,000; a number, with the Hebrew); **5:11** *expressī oleī vīgintī corōs* (the BSB alone 20,000 baths;
  a number, with the Hebrew); **7:40** *cacabōs* (the BSB's "pots" with many manuscripts: Castellio with it); **1:25,
  2:5, 5:16, 6:1, 7:17, 11:33** (with MT: the BSB keeps the Hebrew; Castellio too: 2:5 *quō cīncta latera … pedēs
  habēbat*, his own, the NRSVue alone "my"; 11:33 *colunt*, the Hebrew's plural, the NRSVue alone "he has"); **1:48**
  (the Hebrew's "one to sit"); **7:26** (*duōrum mīllium batōrum*, the Hebrew's); **8:12** *ego tibi Jōva, quī tenebrās
  inhabitāre statuistī* (spoken to God, the Hebrew's "The LORD has said he would dwell in thick darkness": a construal,
  the same matter; 1554 the same, canvas 192); **9:26** *Elōtha* (a place); **10:8** *hominēs tuī* (the Hebrew's "men";
  the NRSVue alone "wives"). The numbers of 5:12, 5:14, 6:1, 6:6, 6:24–26 (6:25 *eadem utriusque mēnsūra*, the short
  verse, gives the second cherub's ten cubits by 6:24 and 6:26), 6:31, 6:32, 7:2, 7:16, 7:17, 7:23, 7:30, 7:32, 7:34,
  8:65 (*bis septem diēs, id est, quattuordecim*, the Hebrew's), 9:2, 10:17: each the Hebrew's, or a number on one
  side only.
- **The NRSVue alone**: 1:8 "Shammah and his companions" (Lucianic), 1:25 "Joab the commander", 1:48 "one of my
  offspring", 2:5 "innocent blood … my waist … my feet" (Gk), 4:24 (Gk lacks "from Tiphsah to Gaza"; Castellio has it,
  *ā Tipsā ad Gazam*), 5:3 "he" and "his feet" (Gk Tg Vg), 6:6 "story" (Gk), 8:16 (adds "nor did I choose anyone …
  Jerusalem", Cn after 2 Chr 6:5–6; the BSB and Castellio the Hebrew), 8:37 "any of their cities", 8:65 "seven days",
  9:25 (Gk), 10:8 "wives", 11:15 "destroying Edom" (Gk Syr; the BSB and Castellio *cum esset Dāvīd apud Idūmæōs*, the
  Hebrew), 11:33 "he has": none with the BSB's agreement.
- **The Hebrew uncertain** (the NRSVue's notes): 6:4, 6:20, 6:31, 7:24 (twice), 10:1. At 6:31 Castellio says so himself
  (*Hunc locum non intelligo … ne quem hoc loco fallat mea translatio*, canvas 828).
- **His vocabulary or a construal the context sets right**: *lacus* for the bronze "Sea" (7:23; his annotation: *Mare
  est in Hebræo, sed mare pro lacu dicitur*); *Jōva* and the classical names of offices (4:2–6); 7:7 *ā pavīmentō ad
  laquear* (with the modern Bibles).
- **Castellio's other marks**: 1:8 and 11:5 *L. … H.* (items 4 and 3).
- **Not 1 Kings**: the candidates' 8:55 (above).

**For the edition summary (not a note):** 3:7 *quī nec tum per ætātem rēs administrāre sciō* (1738 as printed, 1750
OCR line 47133 *qui nec tum per*): **1554 prints *necdum*** (canvas 188, column 352, zoom `z188-3_7.jpg`: *qui necdum
per ætatem res adminiſtrare | ſcio*), "who am not yet of an age to …", the Hebrew's "I am but a little child". *nec tum*
may be a later printer's division of *necdum*; 1573 was not found by the search API. A wording choice for Nathan
(the edited text keeps 1738 unless he takes 1554's *necdum*).
