# Deuteronomy: light notes (Old Testament search)

Built 2026-11-18 by the process in `ot-notes-process.md` (decisions 1A–4A), as the notes for Genesis–Numbers were,
with the bar as the Leviticus and Numbers passes left it (`num-notes.md` §F: a construal the context sets right is
left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio keeps it; kinds
B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew agreeing, and
nobody calls the passage uncertain. Castellio's 1554 annotations on Deuteronomy, read for the first time in this pass,
are in `deut-notes-1554.md`, with one note proposed there (33:8).

**Sources read:**
- `deut-notes-candidates.md` (`python -m pipeline notes Deut`): 19 BSB version notes, 21 numbers, no short verses, and
  one *G.* … *H.* mark, which is not Deuteronomy's (§D).
- The NRSVue (Bible Gateway, read 2026-11-18) for all 34 chapters with its footnotes, one chapter per fetch, by three
  readers (1–11, 12–24, 25–34), each reading the Latin verse by verse against the WLC, the BSB with its footnotes and the
  KJV, with the Vulgate and Brenton's LXX where a verse looked odd. The fetches gave the footnotes verbatim; the verse
  wording was fetched apart where an item needed it. Each item below was checked here against the files. The NET notes
  were not read.
- The printings: 1738 as printed (`text/orig/DEU.usfm`, from the lines read on the page) and its raw OCR, the 1750 raw
  OCR (`sources/archive/`), and the 1573 OCR through the MDZ search for items 2–5 and 7 (no 1573 page image read).

The yield is 6 notes in 34 chapters (0.18 a chapter), and 1 from the 1554 annotations.

## A. Modern Bibles follow the versions (kind A)

The first notes of this kind since Gen 47:21: both are lines of the Song of Moses where the NRSVue and the BSB follow the
Greek and a Hebrew scroll from Qumran.

**Decision:** accept (Nathan, 2026-11-18: "As recommended")

1. **32:8** *cēterīs nātiōnibus fīnēs prō numerō Isrāēlītārum assignāsse*: Hebrew לְמִסְפַּר בְּנֵי יִשְׂרָאֵל, "according to
   the number of the sons of Israel" (the Vulgate *filiorum Israël*, the KJV). The NRSVue has "according to the number
   of the gods" (note "Q ms Compare Gk Tg: MT *the Israelites*"), the BSB "according to the number of the sons of God"
   (note "DSS; LXX … angels of God; MT … sons of Israel"); Brenton's LXX κατὰ ἀριθμὸν ἀγγέλων Θεοῦ. The nations' boundaries
   follow the number of Israel in Castellio, of the sons of God in both modern Bibles. 1738 *pro numero Israelitarum
   adsignasse* (`text/orig` line 1014; OCR lines 29931–29935), 1750 (lines 29366–29368) and 1573 (canvas 153) the same.
   The chief witness for "sons of God" is a Hebrew scroll, not a version, so the note names it beside the Greek (*cōdex
   Hebræus antīquior*, as the New Testament notes say *cōdicēs antīquiōrēs*); the front matter's gloss needs no change.
   **Apply:** `Deut.32.8` la: `prō numerō Isrāēlītārum assignāsse.` → `prō numerō Isrāēlītārum\f + \fr 32:8 \ft Versiōnēs antīquæ habent ‘prō numerō angelōrum Deī’, cōdex Hebræus antīquior ‘fīliōrum Deī’.\f* assignāsse.`
2. **32:43** *Dēcantāte, ō gentēs, ejus populum*: the Hebrew has four lines (הַרְנִינוּ גוֹיִם עַמּוֹ …), as Castellio,
   the Vulgate and the KJV. The NRSVue and the BSB both add, from the Greek and the Qumran scroll, "worship him, all you
   gods" / "let all God's angels worship Him" (the NRSVue "Q ms Gk: MT lacks this line"; the BSB "MT lacks … Cited in
   Hebrews 1:6"), and "repay those who hate him" (the NRSVue "Q ms Gk: MT lacks this line"; the BSB "LXX and Vulgate";
   the Vulgate here has *et vindictam retribuet in hostes eorum*, which is the Hebrew's line). Brenton's LXX opens
   Εὐφράνθητε οὐρανοὶ ἅμα αὐτῷ, καὶ προσκυνησάτωσαν αὐτῷ πάντες ἄγγελοι Θεοῦ. The note gives the line Hebrews 1:6 quotes,
   the one a reader most needs; the rest are smaller (the opening "heavens" for "nations" is the NRSVue's alone). 1738
   *Decantate, o gentes, eius populum* (`text/orig` line 1049; OCR lines 30062–30068), 1750 (lines 29513–29518) and 1573
   (canvas 154) the same.
   **Apply:** `Deut.32.43` la: `Dēcantāte, ō gentēs, ejus populum,` → `Dēcantāte, ō gentēs, ejus populum\f + \fr 32:43 \ft Versiōnēs antīquæ addunt ‘Lætāminī, cælī, cum eō, et adōrent eum omnēs angelī Deī’.\f*,`

## B. Castellio's reading or text departs from the Hebrew (kinds B and C)

Each stands in 1738 and 1750, and in 1573 where looked up: Castellio's own text, so noted, not corrected.

**Decision:** accept (Nathan, 2026-11-18: "As recommended")

3. **10:3** *Itaque arcam cedrinam fēcī*: Hebrew אֲרוֹן עֲצֵי שִׁטִּים, an ark of acacia wood (the NRSVue, the BSB, neither with
   a note; the KJV "shittim wood", the Vulgate *de lignis setim*). The same ark and the same reading as Exodus, whose
   note at 25:5 (*Hebraicē hīc et passim עֲצֵי שִׁטִּים, ‘ligna acaciæ’*) covers Exodus only; a reader of Deuteronomy
   never sees it. 1738 *arcam cedrinam feci* (`text/orig` line 347; OCR line 26986), 1750 the same (line 25998).
   **Apply:** `Deut.10.3` la: `Itaque arcam cedrinam fēcī,` → `Itaque arcam cedrinam\f + \fr 10:3 \ft Hebraicē עֲצֵי שִׁטִּים, ‘ligna acaciæ’.\f* fēcī,`
4. **24:18** *vōs fuisse in Ægyptō peregrīnōs*: Hebrew כִּי עֶבֶד הָיִיתָ בְּמִצְרַיִם, "that you were a slave in Egypt" (the
   NRSVue, the BSB, neither with a note; the KJV "bondman", the Vulgate *servieris*, the LXX οἰκέτης). Castellio gives the
   formula as slavery everywhere else (15:15 and 5:15 *tē servum fuisse*, 16:12, and four verses on, 24:22 *vōs fuisse
   servōs in Ægyptō*, the same Hebrew); "strangers" seems carried from *Peregrīnī* in 24:17, or from the other formula
   of 10:19 and 23:7. 1738 *vos fuisse in Aegypto peregrinos* (`text/orig` line 764; OCR lines 28799–28800), 1750 (lines
   28083–28084) and 1573 (canvas 148) the same. **Near the bar:** the motive of the law (remember your hardship in
   Egypt) stands, and "strangers in Egypt" is itself a formula of Deuteronomy; but it is a word changed, like Exod 36:18,
   and his own 24:22 contradicts it. Leave it out if the bar is held strictly.
   **Apply:** `Deut.24.18` la: `vōs fuisse in Ægyptō peregrīnōs,` → `vōs fuisse in Ægyptō peregrīnōs\f + \fr 24:18 \ft Hebraicē עֶבֶד הָיִיתָ, ‘servus fuistī’.\f*,`
5. **26:5** *Majōrēs nostrī, Syrīs eōs opprimentibus, dēscendērunt in Ægyptum*: Hebrew אֲרַמִּי אֹבֵד אָבִי, "a wandering
   (or perishing) Aramean was my father" (the NRSVue "A wandering Aramean was my ancestor", the BSB "My father was a
   wandering Aramean", neither with a note; the KJV "A Syrian ready to perish was my father"). Castellio follows the
   Vulgate (*Syrus persequebatur patrem meum*), the Targum's and the rabbis' reading (Laban the oppressor): the ancestor
   is no longer the Aramean, and the Syrians become his oppressors. אבד is a common word, so this is not Exod 32:25's
   case of a rare word; Num 12:8, shared with the Vulgate, was accepted. The LXX (Συρίαν ἀπέβαλεν ὁ πατήρ μου) is not his
   source. 1738 *maiores nostri, Syris eos opprimentibus* (`text/orig` line 798; OCR lines 28926–28927), 1750 (lines
   28225–28226) and 1573 (canvas 149) the same. His 1554 annotations say nothing on it.
   **Apply:** `Deut.26.5` la: `Syrīs eōs opprimentibus,` → `Syrīs eōs opprimentibus\f + \fr 26:5 \ft Hebraicē אֲרַמִּי אֹבֵד אָבִי, ‘Syrus vagus erat pater meus’.\f*,`
6. **31:23** *ductūrum enim Isrāēlītās in terram, quam Deus illīs jūrejūrandō prōmīsisset, ipsumque Deum eī adfutūrum*:
   Hebrew אֲשֶׁר־נִשְׁבַּעְתִּי לָהֶם וְאָנֹכִי אֶהְיֶה עִמָּךְ, "which I swore to them, and I will be with you": the LORD speaks, and
   it is he who commissions Joshua (the NRSVue "Then the Lord commissioned Joshua", note "Heb *he*"; the BSB the same, no
   note; the KJV "which I sware … I will be with thee", the Vulgate *quam pollicitus sum, et ego ero tecum*). Castellio
   has the third person of Brenton's LXX (ἣν ὤμοσεν αὐτοῖς Κύριος, καὶ αὐτὸς ἔσται μετὰ σοῦ), which after 31:22 *Scrīpsit ergō
   Mōsēs* makes Moses the speaker. No *G.* … *H.* mark here in 1738. 1738 *quam Deus illis iureiurando promisisset,
   ipsumque Deum ei adfuturum* (`text/orig` line 995; OCR lines 29835–29841), 1750 (lines 29278–29283) and 1573 (canvas
   153) the same. The form of the process file's kind C, *Castelliō Septuāgintā sequitur*.
   **Apply:** `Deut.31.23` la: `ipsumque Deum eī adfutūrum.` → `ipsumque Deum eī adfutūrum\f + \fr 31:23 \ft Hebraicē אֲשֶׁר־נִשְׁבַּעְתִּי לָהֶם וְאָנֹכִי אֶהְיֶה עִמָּךְ, ‘quam iīs jūrāvī, et ego tēcum erō’; Castelliō Septuāgintā sequitur.\f*.`

## C. From Castellio's 1554 annotations

7. **33:8** *quem lacessīstī apud Massam*: proposed in `deut-notes-1554.md` (item 4), decided there. The BSB's added
   "Give to Levi" (a candidate here) needs no note of its own: Castellio's *Ad Lēvim autem inquit* already names Levi.

## D. Considered and left out

- **The *G.* … *H.* mark the tool placed at 3:1** (*L. Augem, G. ad sinistram superioris Ciliciae positum*) is Judith
  2:21 (Vulgate 2:12), in 1738's Judith pages (OCR lines 71024–71038, under *IVDITHA*) and 1750's (lines 74089–74094),
  and an *L.* … *G.* mark at that; it matched Deut 3:1 only by *cum suis omnibus copiis*. Nothing in Deuteronomy.
- **A name with an old identification:** 2:23 *Cappadocēs ex Cappadociā profectī* for the Caphtorim from Caphtor (the
  NRSVue Caphtor; the BSB "Caphtor", note "That is, Crete"), with the LXX and the Vulgate. His reading everywhere (1738:
  1 Chr 1:12, Jer 47:4, Amos 9:7; only Gen 10:14 keeps *Caphthorim*), and Caphtor's place is itself uncertain. Names are
  left out (Num §E: *Sinæ* for Zin); a note here would be due in three more books.
- **Near the bar, left out:** 7:10 *sine dubiō* (his deliberate "without fail" for "without delay", defended in 1554:
  `deut-notes-1554.md` item 1, recommended there to be left out); 29:26 *neque cum iīs ūllam rem habuissent* for "whom he
  had not allotted to them" (God lost as subject; a paraphrase); 28:68 *sine ūllō assertōre* for "no buyer".
- **Kind A where the sense doesn't change (both Bibles leave the Hebrew):** 11:30 (the oak or oaks of Moreh; Castellio's
  *querquētum*), 29:10, 31:1 (the narrative frame: "finished speaking" for "went and spoke"), 33:2 ("us" for "them"),
  33:8 ("Give to Levi", above), 28:22 ("drought" for "the sword", one plague in a list).
- **Only one of the NRSVue and the BSB leaves the Hebrew:** 1:7, 2:21, 2:37, 3:12, 4:48 (Sirion), 9:16, 9:24, 11:13,
  11:14–15, 13:6, 15:2, 21:23 (the BSB's "on a tree", from the LXX and Gal 3:13; the NRSVue with the Hebrew), 30:16,
  32:10, 32:13, 32:15, 32:19, 32:31, 32:35, 33:12, 33:16, 33:17, 33:27.
- **Castellio already goes the modern Bibles' way, or the BSB only reports a version:** 32:44 (*Jōsuā* for Hoshea),
  34:6, 9:19, 27:26, 32:21, 32:36, and the BSB's notes on New Testament citations (4:24, 5:16–21, 6:4–5, 6:13, 6:16, 8:3).
- **Disputed:** 15:18 *bis tam diū* (the NRSVue and the BSB differ on מִשְׁנֶה), 23:18 *admissūræ canis pretium* (the NRSVue
  keeps "dog", the BSB a male prostitute; `deut-notes-1554.md` item 3), 18:1, 18:8, 7:20, 29:19, and the Song and the
  Blessing where the NRSVue calls the Hebrew uncertain or emends (32:5, 32:26, 32:42, 33:2, 33:3, 33:6, 33:7, 33:21,
  33:25, 33:27, 33:28).
- **Old readings of a rare word or institution:** 21:4 *vallem vāstam incultam* (the KJV's "rough valley"), 23:17
  *meretrīx … scortātor*, 1:1 *maris rubrī* for Suph.
- **Names translated or paraphrased, vocabulary:** 3:9, 3:14, 9:22 *Busta cupiditātis*, 10:6, 32:14–15, 33:5 and 33:26
  (Jeshurun as *probī*), 7:5 *lūcōs*, 8:4, 8:9, 8:15, 11:24, 20:6, 21:13 *mēnstruā diē*, 28:27, 28:42, 33:17, 33:8
  *integritās et clāritās*, 34:5 *ante ōs Jōvæ*; the *senātōrēs*, *cūria* and *pontifex*.
- **Words moved across verses or condensed:** 1:35–36, 1:46, 2:20–21, 4:45–48, 5:5, 9:25, 10:1, 10:8, 11:2, 12:26–27,
  13:12–14, 16:16–17, 22:15–17, 22:18–19, 24:3–4, 25:8–9, 26:10–11, 29:28, 31:29.
- **Numbers:** every numeral matches the Hebrew (1:2–3, 2:14, 3:4, 3:11, 4:41, 5:9–10, the forty days and years, 10:22,
  14:28, 15, 16's festivals, 19's cities, 22:19, 22:29, 23:2–8, 24:5, 25:3, 31:2, 31:10, 32:30, 34:7–8). The tool's hits
  are numbers carried across verses (4:47–48, 14:22–25, 22:18–19), distributives and number words (1:11, 1:15, 13:9,
  14:6, 19:3, 21:19, 28:56 *secundās*), vocabulary (33:2, 33:17 *legiōnēs*), or a number the tool missed (10:3, 17:6).
- **The Decalogue** (5:6–21) matches Deuteronomy's Hebrew, the wife first in 5:21.
- **Misreadings of 1738:** none. All three readers checked every word with f or s against its other reading (the Num
  34:3 *falsī* kind) and the words found once only; 3:17 *salsum* was corrected in stage 2.
