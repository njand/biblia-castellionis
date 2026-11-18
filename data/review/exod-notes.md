# Exodus: light notes (Old Testament search)

Built 2026-11-18 by the process in `ot-notes-process.md` (decisions 1A–4A), as `gen-notes.md` was for Genesis: kind A
when the NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio keeps it; kinds B and C where his
reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew agreeing, and nobody calls the
passage uncertain. Formulas as in `notes-audit.md` §A and the Genesis notes.

**Sources read:**
- `exod-notes-candidates.md` (`python -m pipeline notes Exod`): 11 BSB version notes, 60 numbers, 17 short verses, and
  Castellio's own marks (3), a section the tool gained for this pass (`gen-notes.md` §F).
- The NRSVue (Bible Gateway, read 2026-11-18) for all 40 chapters with its footnotes, by four readers (1–10, 11–20,
  21–30, 31–40), each reading the Latin verse by verse against the WLC, the BSB with its footnotes and the KJV, with
  the Vulgate and Brenton's LXX where a verse looked odd. Each find was checked here against the files. The NET notes
  could not be loaded (netbible.org returned the wrong passage) and were not needed: no proposal below is disputed.
- The printings: 1738 as printed (`text/orig/EXO.usfm`) and its raw OCR, the 1750 raw OCR (`sources/archive/`), and
  for items 4, 6 and 7 the 1573 OCR through the MDZ search (canvases 81 for 28:24; the others by search hit; no 1573
  page image read). 1551 (Google Books BrlIAAAAcAAJ) for items 4–8, read by Nathan on 2026-11-18 (Claude's own search
  met a CAPTCHA and stopped).
- Castellio's 1554 annotations (`gen-exod-notes-1554.md`): nothing on any item below.

The yield is 8 notes in 40 chapters (0.2 a chapter), against 6 in Genesis's 50.

## A. Modern Bibles follow the versions (kind A)

None. Where both the NRSVue and the BSB leave the Hebrew (1:22 "to the Hebrews", 8:23 "distinction", 39:24 the
linen), Castellio already goes their way (*Hebræōrum marēs*, *discrīmen*, *byssō bilīce*).

## B. Readings Castellio marked as taken from the Greek (kind C)

The edition doesn't print Castellio's *G.* … *H.* marks, so where modern Bibles keep the Hebrew the note gives the reader
what the mark told him. Each stands in 1738 and 1750 with the mark.

**Decision:** accept all except 3 (Nathan, 2026-11-18: "Drop #3, which you said yourself was weak", then "Apply both")

1. **2:22** *Item alterum, quem Eliezerem nōmināvit … līberāsset*: the Hebrew has Gershom only (וַתֵּלֶד בֵּן וַיִּקְרָא
   אֶת־שְׁמוֹ גֵּרְשֹׁם …); Eliezer is first named at 18:4. The NRSVue and the BSB have Gershom only, without a note on a second son;
   so do the KJV and Brenton's LXX. The Clementine Vulgate has the addition (*Alterum vero peperit, quem vocavit
   Eliezer …*). 1738 *extranea. G\ Item alterum … liberasset. h.* (OCR, lines 10477–10482), 1750 *G. Item alterum …
   fet. H.* (lines 8462–8466).
   **Apply:** `Exod.2.22` la: `injūriā līberāsset.` → `injūriā līberāsset\f + \fr 2:22 \ft ‘Item alterum … līberāsset’ Castelliō ex Græcō addit; Eliezer Hebraicē prīmum 18:4 nōminātur.\f*.`
2. **6:20** *et Marīam eōrum sorōrem*: Hebrew וַתֵּלֶד לוֹ אֶת־אַהֲרֹן וְאֶת־מֹשֶׁה, Aaron and Moses (the NRSVue, the BSB, the KJV
   and the Vulgate, none with a note). Brenton's LXX adds καὶ Μαριὰμ τὴν ἀδελφὴν αὐτῶν; Castellio keeps the Hebrew's 137
   years, not the LXX's 132. 1738 *G.L.* at the foot of the page, *G L. et Mariam eorum sororem, H.* over it (OCR lines
   10973–10982); 1750 *G. L. et Mariam eorum fororem, H.* (lines 9046–9047).
   **Apply:** `Exod.6.20` la: `Mōsem et Marīam eōrum sorōrem, vīxitque` → `Mōsem et Marīam eōrum sorōrem\f + \fr 6:20 \ft Hebraicē וַתֵּלֶד לוֹ אֶת־אַהֲרֹן וְאֶת־מֹשֶׁה, ‘peperit eī Aharōnem et Mōsem’; ‘et Marīam eōrum sorōrem’ Castelliō ex Græcō addit.\f*, vīxitque`
3. **28:34** *et byssō bilīce*: the pomegranates of 28:33 are רִמֹּנֵי תְּכֵלֶת וְאַרְגָּמָן וְתוֹלַעַת שָׁנִי, without linen (the NRSVue
   and the BSB, without a note; the Vulgate). Brenton's LXX 28:33 adds καὶ βύσσου κεκλωσμένης. 1738 *G. L. et bysso bilice H.*
   (OCR *bysfo*), 1750 *G.* at the same place. The weakest of the three: at 39:24 the NRSVue (note "Sam Gk Syr Vg: MT
   lacks fine linen") and the BSB add the linen, so Castellio has made 28:33 agree with 39:24 from the Greek, and the
   change of sense is small. It passes on Gen 32:29's precedent (a mark of his own). Leave it out if the bar is held
   strictly.
   **Apply:** `Exod.28.34` la: `et byssō bilīce, et iīs` → `et byssō bilīce\f + \fr 28:34 \ft Hebraicē 28:33 רִמֹּנֵי תְּכֵלֶת וְאַרְגָּמָן וְתוֹלַעַת שָׁנִי, ‘māla pūnica ex hyacinthō, purpurā et coccō iterātō’; ‘et byssō bilīce’ Castelliō ex Græcō addit.\f*, et iīs`

## C. Castellio's text departs from the Hebrew (kind C)

Each stands in 1551 (read by Nathan), 1738 and 1750, and items 4, 6 and 7 in 1573 too: Castellio's own text from the
first edition, so noted as Gen 44:2's golden cup was, not corrected. Items 5–7 are contradicted by his own wording
elsewhere, but no printing corrects them.

**Decision:** accept (Nathan, 2026-11-18: "Apply both")

4. **23:6** *Inimīcī tuī jūs in līte nē dēprāvātō*: Hebrew לֹא תַטֶּה מִשְׁפַּט אֶבְיֹנְךָ בְּרִיבוֹ, "the justice due to your poor"
   (the NRSVue, the BSB, without a note; the Vulgate *pauperis*, the LXX πένητος). No version has "enemy"; it seems carried
   from 23:4–5. 1738 *Inimici tui ius in lite* (`text/orig` line 739), 1750 the same (line 11555), 1573 the same (OCR), 1551 *Inimici tui ius*.
   **Apply:** `Exod.23.6` la: `Inimīcī tuī jūs` → `Inimīcī tuī\f + \fr 23:6 \ft Hebraicē אֶבְיֹנְךָ, ‘pauperis tuī’.\f* jūs`
5. **28:24** *duās illās argenteās catēnulās*: Hebrew שְׁתֵּי עֲבֹתֹת הַזָּהָב, the two cords of gold (the NRSVue, the BSB, without a
   note; the Vulgate *catenas aureas*), the chains Castellio himself makes *ex aurō pūrō* at 28:14 and 28:22. 1738
   (`text/orig` line 928), 1750 (line 12221) and 1573 (canvas 81, OCR) all *argenteas*, and 1551.
   **Apply:** `Exod.28.24` la: `argenteās catēnulās ibīdem` → `argenteās catēnulās\f + \fr 28:24 \ft Hebraicē עֲבֹתֹת הַזָּהָב, ‘catēnulās aureās’.\f* ibīdem`
6. **34:26** *Hædum in sanguine mātris suæ nē coquitō*: Hebrew בַּחֲלֵב אִמּוֹ, in its mother's milk (the NRSVue, the BSB, the KJV,
   the Vulgate *in lacte*), and Castellio's own *in lacte mātris suæ* at 23:19 and Deut 14:21 (1573, whose margin there
   cites 34:26). 1738 (`text/orig` line 1160), 1750 (*fanguine matris*, line 13284) and 1573 (OCR) all *sanguine*, and 1551.
   **Apply:** `Exod.34.26` la: `in sanguine mātris suæ nē coquitō` → `in sanguine mātris suæ\f + \fr 34:26 \ft Hebraicē בַּחֲלֵב אִמּוֹ, ‘in lacte mātris suæ’.\f* nē coquitō`
7. **36:18** *uncōs aureōs quīnquāgintā*: Hebrew קַרְסֵי נְחֹשֶׁת חֲמִשִּׁים, fifty bronze clasps (the NRSVue, the BSB, the Vulgate
   *fibulas æneas*), Castellio's own *factōs ex ære uncōs* at 26:11; the gold clasps are those of 36:13, a few lines up.
   1738 (`text/orig` line 1230), 1750 (line 13566) and 1573 (OCR) all *aureos*, and 1551.
   **Apply:** `Exod.36.18` la: `uncōs aureōs quīnquāgintā` → `uncōs aureōs\f + \fr 36:18 \ft Hebraicē קַרְסֵי נְחֹשֶׁת, ‘uncōs ex ære’.\f* quīnquāgintā`
8. **40:3** *et propitiātōriō tegitō*: Hebrew וְסַכֹּתָ עַל־הָאָרֹן אֶת־הַפָּרֹכֶת, "screen the ark with the veil" (the NRSVue "curtain",
   the BSB "veil", without a note; the KJV and the Vulgate *velum*). Castellio puts the mercy seat for the veil, perhaps
   from 40:20; the veil comes back at 40:21 (*sīpariō obvēlāvit*). 1738 (`text/orig` line 1376), 1750
   (*propitiatoriotegito*, line 14135) and 1573 (OCR). 1551 words it otherwise with the same sense: *Ibi arcam
   oraculi propitiatorio tectam collocato* (Nathan); the later *collocato, et propitiatorio tegito* is Castellio's
   revision.
   **Apply:** `Exod.40.3` la: `et propitiātōriō tegitō.` → `et propitiātōriō tegitō\f + \fr 40:3 \ft Hebraicē וְסַכֹּתָ עַל־הָאָרֹן אֶת־הַפָּרֹכֶת, ‘et arcam sīpariō tegitō’.\f*.`

## D. Considered and left out

- **The existing notes all pass and stay:** 19:23 (*populum* read for *the mountain*; the NRSVue and the BSB with the
  Hebrew, no note), 23:15 (his coinages), 25:5 (cedar for acacia; the NRSVue's "uncertain" there is on the hides),
  30:24 (*Īris*, after Josephus), 40:20 (*vectēs āræ* for the ark's poles; 1738 and 1750).
- **Old readings of Castellio's, near the bar** (as Gen 33:18 was left out):
  - 32:25 *populum … spoliātum ōrnāmentīs (spoliāverat enim Aharōn …)* for פָרֻעַ, "out of control" (the NRSVue,
    the BSB), with the Vulgate (*nudatus … spoliaverat*) and the KJV ("naked"). 1738 the same; 1750 not looked at.
  - 22:28 *Magistrātuī nē maledīcitō* for אֱלֹהִים (the NRSVue "God", the BSB "God"): the judges reading is the
    Targum's and the KJV margin's, and consistent with his *recuperātōrēs* at 21:6 and 22:8–9.
  - 21:8 *nec is eam dēsponderit*, the Ketiv (the BSB gives it as an alternative).
  - 32:29 *Expiāte hodiē manūs vestrās*, the imperative as the Masoretes point it (the KJV).
  - 34:33 the veil put on before the speaking ended (the KJV's "till Moses had done speaking").
- **Only one of the NRSVue and the BSB leaves the Hebrew** (no consensus): 3:1, 5:5, 5:9, 5:13, 5:16, 8:3, 14:25 (the
  NRSVue "clogged" with the versions; the BSB "wobble" with "Or … come off" as an alternative; Castellio *dētractīs*
  with the Hebrew and the KJV), 23:2, 23:25, 24:11, 27:15.
- **Castellio already goes the versions' way:** 1:22, 8:23, 13:16, 17:16 (*signō*, the NRSVue's banner), 19:13
  (*sagittīs*), 20:18 (*perterritī*, the NRSVue "were afraid" with the versions), 39:24.
- **Kept with the Hebrew where the BSB only reports a version:** 1:5 seventy (the LXX and a scroll 75), 2:14, 9:16,
  12:40 the 430 years in Egypt (the SP and LXX add Canaan), 13:18 *prōcīnctī* (the LXX "fifth generation"), 14:20.
- **Small slips that leave the sense:** 29:22 *quia agnus initiātōrius est* for אֵיל מִלֻּאִים, a ram, named as *ariete* in
  the same verse (1573, 1738 and 1750 all *agnus*); 34:24 *quotannīs*, the *Ter quotannīs* of 34:23 understood.
- **His own harmonising, defended in 1554:** 9:6 *mortuō omnis generis pecore* (`gen-exod-notes-1554.md`, class c).
- **Paraphrase, vocabulary, materials:** 18:17–18 *stultum … īnstitūtum* for "you will wear yourselves out" (with the
  Vulgate's *stulto labore*; the sense of 18:18 kept), 21:13 *forte fortūnā*, 21:22 *abortum* (the NRSVue's
  miscarriage), 14:2 *faucēs Ahīrōtha*, 14:8 *cum ingentī manū*, 20:5 *Deus impatiēns sociī*, 34:7, 34:13 *lūcōs*,
  the officers of 18:21, the stones of 28:17–20 and 39:10, 30:34 *crocum*, 30:35 *temperātum*, 9:31 *in herbā*, the
  skins and vestments the NRSVue calls uncertain (31:10, 35:7, 35:19, 35:23, 36:19, 39:23, 39:34, 39:41).
- **Numbers:** every numeral the readers checked matches the Hebrew; the tool's other hits are counts on one side only
  (*totidem*, *ambō*, *quīna*, *utrimque*) or words moved across verses in the tabernacle chapters, where the totals agree
  (36:24–32, 38:11–17, 38:24–29).
- **Short verses:** paraphrase or words carried into the next verse (6:29, 18:18, 36:5–31).
- **The settled text against 1738:** read word by word for 1–20 by the readers; every difference is an approved spelling
  or already in `data/decisions/Exod.orig.tsv` (15:6 *fortissimē*, 18:5 *Cum hīs*). No slip to correct.

## E. A paragraph at 34:27 (layout, found by Nathan)

**Decision:** accept (Nathan, 2026-11-18: "Apply both")

9. **34:26–27**: God's speech (34:10–26) closes at 34:26, and 34:27 opens a new one with its own *inquit*, so the
   quotation marks close and reopen side by side in one paragraph (Nathan: "why do we close the quote at the end of
   this verse, to immediately reopen it?"). The marks are right; a new paragraph at 34:27, as the BSB has, separates
   the two speeches.
   **Apply:** `Exod.34.27` la: `\v 27 “Hæc tū verba,”` → `\p \v 27 “Hæc tū verba,”`

## F. For the next books

- The mark search found **Num 10:6** (*G. L. Quum tertium … quum quartum …*: the third and fourth blasts, from the
  LXX): a candidate for the Numbers pass.
- Bünemann's preface lists the places he restored from 1551 (`docs/editions.md`, "The Leipzig editions and their
  prefaces"); his Deuteronomy, Kings and Chronicles places are worth checking when those books are settled.
