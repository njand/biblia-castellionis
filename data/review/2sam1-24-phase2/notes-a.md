# 2 Samuel 1–12: light notes (Old Testament search), reader A

Built 2026-11-21 in phase 2 of decision 85 (PLAN.md §4), beside `propose`, by the process in `ot-notes-process.md`
(decisions 1A–4A), as 1 Samuel's (`1sam-notes-a.md`, settled 2026-11-20), with the bar as it now stands (Nathan,
2026-11-19: no note for a departure without plot or theological significance; `num-notes.md` §F: a construal the
context sets right is left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and
Castellio keeps it; kinds B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and
the Hebrew agreeing, and nobody calls the passage uncertain. Chapters 13–24 are reader B's. Castellio's 1554
annotations on these chapters and the 1554 text's margins, read on the page in this pass, are in `notes-1554-a.md`.
Names in note text as settled in `names.md` (none of its forms is needed by the notes proposed here).

**Sources read:**
- `2sam-notes-candidates.md` (`python -m pipeline notes 2Sam`), its entries for chapters 1–12: 12 BSB *against MT*
  (1:21, 2:29, 5:25, 6:4, 7:16, 7:23, 8:3, 8:4, 8:12, 8:13, 9:11, 10:18, 12:14, 12:16), 4 *with MT* (6:2, 6:7, 8:8), 3
  *other* (3:3, 6:5, 8:18), 4 numbers (8:2, 8:13, 9:13, 12:6), and Castellio's marks at 1:19, 8:7, 8:8. Also 1:26's and
  8:13's *L. … H.*, which the tool does not list (`2sam1-24-transcription.md`).
- The NRSVue (Bible Gateway, read 2026-11-21) for chapters 1–12 with all its footnotes (not stored). The NET was not
  read. The verses below read in the preview (`text/draft/2SA.preview.usfm`) against the BSB, with the WLC, the
  Vulgate and Brenton's LXX (`sources/parallel/`); the verse readers' reports `r1.md`–`r4.md` for what they flagged
  (1:19, 1:26, 8:7–8, 8:13, 12:31).
- 1738's 15 footnotes and 4 asterisks in these chapters, from phase 1 (`data/witnesses/read-1738/2Sam1-24.tsv`,
  `2sam1-24-transcription-readers.md`).
- The printings: 1738 as printed (`text/orig/2SA.usfm`), the 1750 raw OCR (`sources/archive/1750/text.txt`), **1554**
  (canvases 171–177 and 826) on page images read here (`notes-1554-a.md`), **1573** through the MDZ search API only.

The yield is 5 notes proposed in 12 chapters (0.42 a chapter): Castellio's gap at 5:8, which he marked himself (1554's
dagger, 1738's asterisk, his annotation), and four of his *G.* / *L.* … *H.* passages that no modern Bible prints
(1:19, 1:26, 8:7, 8:8), whose marks the edition no longer prints. No kind A passes. Four more near the bar are
recommended left out (8:13, 12:14, 12:31, 7:23).

## A. Modern Bibles follow the versions (kind A)

None proposed. The places where both the NRSVue and the BSB leave the Hebrew are 7:16 ("before me"), 7:23 (item 9),
8:3 (Euphrates: Castellio has it too), 8:12 and 8:13 (Edom for Aram: item 6), 9:11 ("David's table") and 12:14 (item
7); see §C and §F.

## B. Castellio's text departs from the Hebrew, or marks a gap in it (kind C)

**Decision:** accept (Nathan, 2026-11-21: "Approve all")

1. **5:8** *eōque diē prōnūntiāvit Dāvīd, quisquis Jebūsæōs vīcisset, et ad canālem pertigisset, claudōsque et cæcōs
   Dāvīdī invīsōs, ex quō nātum est dictum illud*: the sentence has no main clause: what David promised the man who
   took the citadel is not said. Hebrew כָּל־מַכֵּה יְבֻסִי וְיִגַּע בַּצִּנּוֹר וְאֶת־הַפִּסְחִים וְאֶת־הַעִוְרִים שנאו נֶפֶשׁ דָּוִד, "whoever
   strikes the Jebusite and reaches the shaft, and the lame and the blind, hated of David's soul": as elliptical as
   Castellio's Latin (the KJV supplies "he shall be chief and captain" in italics, from 1 Chr 11:6). The NRSVue and the
   BSB make it a command ("let him get up the water shaft to attack the lame and the blind", "must use the water shaft
   to reach …"); the NRSVue's one note is on "hate", Q ms Syr Tg against the MT, where Castellio's *Dāvīdī invīsōs*
   reads with it. **Castellio called the place broken**: his 1554 annotation (canvas 826, column 347,
   `notes-1554-a.md` §1) begins *Hũc locum mutilũ eſſe patet, tum quòd ſententia curta eſt, tum quòd in Paralipomenis
   capite undecimo, adiectum eſt quod hic deſideratur*, and goes on to read the reward as *imperatorem fore … eum, qui
   primus Iebuſæos ſuperauiſſet*; his 1554 text marks the break with a dagger (*Dauidi inuiſos † ex quo*, canvas 173,
   column 322, zoom `z173-5_8.jpg`), and 1738 with an asterisk (*inuisos, \* ex quo*, `text/orig/2SA.usfm` line 150
   without it; reader 03). The edition prints neither.
   **Why it passes the bar**: the same case as 1 Sam 13:1 (accepted 2026-11-20): Castellio translated the broken Hebrew
   as it stands and marked the break for his reader; without the mark the edition's sentence simply breaks off, and the
   reader cannot tell a gap in the Hebrew from a slip of the printer. What David promised is the hinge of the capture of
   Zion (in Chronicles Joab wins the command by it). **Near the bar** in that a reader with a modern Bible is not misled
   about the Hebrew's words, only left without Castellio's sign; the note gives no Chronicles reading, only the fact
   Castellio states. 1750 (OCR) not checked here.
   The form of 1 Sam 13:1's *numerī excidērunt*. Words checked with `pipeline latin macron-check` (*Hebraicē* as the
   settled notes have it).
   **Recommendation (Claude): accept.**
   **Apply:** `2Sam.5.8` la: `Dāvīdī invīsōs, ex quō` → `Dāvīdī invīsōs\f + \fr 5:8 \ft Hīc sententia Hebraicē curta est: quid victōrī prōmissum sit, nōn dīcitur.\f*, ex quō`

2. **1:19** *Cōnsīderā, ō Isrāēlīta, quī in tuīs fastīgiīs cæsī occubuerint*: Castellio's **G. L. … H.** line, the
   first of David's lament, which neither the Hebrew nor either modern Bible has. Hebrew הַצְּבִי יִשְׂרָאֵל עַל־בָּמוֹתֶיךָ חָלָל,
   "the glory of Israel is slain on your heights", which Castellio then gives (*Isrāēlītārum decus in tuīs peremtum est
   fastīgiīs*). Brenton's LXX 1:19 has only the Greek's version of that line, *Στήλωσον Ἰσραὴλ ὑπὲρ τῶν τεθνηκότων ἐπὶ τὰ
   ὕψη σου τραυματιῶν*; the Vulgate both, at the end of its 1:18 (*Considera, Israël, pro his qui mortui sunt, super
   excelsa tua vulnerati*) and in 1:19 (*Inclyti Israël super montes tuos interfecti sunt*). So Castellio, like the
   Vulgate, gives the line twice, once from the Greek and Latin and once from the Hebrew. The NRSVue and the BSB print the
   Hebrew only, with no note.
   **Why it passes the bar**: as 1 Sam 2:8 and 5:6 (accepted 2026-11-20): the marks are gone from the edition
   (`r1.md`: the draft fix will take them out, as 1 Samuel's), so the reader cannot tell this line from the Hebrew's, and
   it opens the best-known poem of the book, which a reader will compare with a modern Bible line by line. **Near the
   bar** in adding no new matter (it says again what the next line says). 1554 (canvas 171, column 318, *Sic autem
   dixit: G.L.Con-|ſidera, ô Iſraelita, qui in tuis faſtigijs cæſi occu-|buerint.H.*), 1738 (line 30), 1750 (OCR, the
   candidates file: *dixit; G.L. confidera o Ifralita, / qui in tuis faftigiis caefi occubuc.*) the same.
   The note's quotation follows r1's layout row (*“Cōnsīderā*, capital once the mark goes). The form of 1 Sam 5:6.
   **Recommendation (Claude): accept.**
   **Apply:** `2Sam.1.19` la: `cæsī occubuerint,` → `cæsī occubuerint\f + \fr 1:19 \ft ‘Cōnsīderā … occubuerint’ Castelliō ex Græcō addit, ut Vulgāta; Hebraicē nōn est.\f*,`

3. **1:26** *Sīcut māter ūnicum amat fīlium suum, ita ego tē dīligēbam*: Castellio's **L. … H.** couplet (1738's
   1:27, joined to the KJV's 1:26 in versification), the Vulgate's addition to David's lament for Jonathan (*Sicut
   mater unicum amat filium suum, ita ego te diligebam*, word for word). Not in the Hebrew (1:26 ends נִפְלְאַתָה אַהֲבָתְךָ
   לִי מֵאַהֲבַת נָשִׁים, "your love to me was wonderful, passing the love of women"), nor in Brenton's LXX, nor in the NRSVue or
   the BSB (no note in either).
   **Why it passes the bar**: it adds to what David says of his love for Jonathan, a passage readers weigh word by word,
   a comparison no modern Bible has; and the mark that told Castellio's reader it was the Latin's is gone. Kind C, as
   item 2. 1554 (canvas 171, column 318, *amor. L. Sicut mater unicum amat filiũ ſuum, | ita ego te diligebam. H.*), 1738
   (line 37), 1750 (OCR line 42614, *muliebris amor. — L. Sicut mater*) the same.
   **Recommendation (Claude): accept.**
   **Apply:** `2Sam.1.26` la: `ita ego tē dīligēbam.` → `ita ego tē dīligēbam\f + \fr 1:26 \ft ‘Sīcut māter … dīligēbam’ Castelliō ex Vulgātā addit; Hebraicē nōn est.\f*.`

4. **8:7** *quās posteā Sesacus Ægyptī rēx abstulit in ea expedītiōne, quam Roboāmī Solomōnis fīliī temporibus fēcit in
   Hierosolymam*: Castellio's **G. … H.** sentence, the Greek's: Brenton's LXX 8:7 *καὶ ἔλαβεν αὐτὰ Σουσακὶμ βασιλεὺς
   Αἰγύπτου, ἐν τῷ ἀναβῆναι αὐτὸν εἰς Ἱερουσαλὴμ ἐν ἡμέραις Ῥοβοὰμ υἱοῦ Σαλωμῶντος*. The Hebrew ends with David bringing the
   gold to Jerusalem (וַיְבִיאֵם יְרוּשָׁלִָם); the Vulgate, the NRSVue and the BSB the same, with no note.
   **Why it passes the bar**: a sentence of history the Hebrew of Samuel does not tell here (Shishak's plunder is 1 Kgs
   14:25–26, of Solomon's shields), and the mark is gone. The case of Josh 16:10 (*dōnec Pharaō … dedit*, accepted:
   Castellio's Greek addition of a fact told elsewhere in Kings). **Near the bar**: nothing in 2 Samuel turns on it.
   1554 (canvas 175, column 326, *intulit. G. quas poſtea Seſacus Aegypti rex ab-|ſtulit … in Hieroſoly-|mam. H.*), 1738
   (line 238), 1750 (OCR, the candidates file: *tulit, G. qu: as poftea Sefacus Aegy| pti / rex abftulit*) the same.
   **Recommendation (Claude): accept**, with item 5 (the two stand or fall together).
   **Apply:** `2Sam.8.7` la: `fēcit in Hierosolymam.` → `fēcit in Hierosolymam\f + \fr 8:7 \ft ‘quās posteā … in Hierosolymam’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*.`

5. **8:8** *ex quō fēcit Solomō rēx lacum æreum, et columnās, et altāre et lavācra, omniaque vāsa*: Castellio's **G. L.
   … L. … G. … H.** clause, the Greek's: Brenton's LXX 8:8 *ἐν αὐτῷ ἐποίησε Σαλωμὼν τὴν θάλασσαν τὴν χαλκῆν, καὶ τοὺς
   στύλους, καὶ τοὺς λουτῆρας, καὶ πάντα τὰ σκεύη* (the sea, the pillars, the lavers, all the vessels); *et altāre*, marked
   *L.*, is not in Brenton, nor in the Clementine Vulgate, which has no part of the clause (*tulit rex David æs multum
   nimis.*): its Latin source was not found. The Hebrew ends נְחֹשֶׁת הַרְבֵּה מְאֹד, "very much bronze"; the NRSVue and the BSB
   the same (the BSB's note is on Betah's name only). The fact stands in the Hebrew of 1 Chr 18:8.
   **Why it passes the bar**: as item 4. 1554 (canvas 175, column 326, *rex Da-|uid, G.L. ex quo fecit Solomo rex lacum
   æreũ, | & columnas, L. & altare G. & lauacra, omniaq; | uaſa. H.*), 1738 (line 239), 1750 (OCR, the candidates file:
   *G. L. ex quo fecit / Solomo rex lacum aereum … lumnas, L, et altare G. et*) the same.
   **Recommendation (Claude): accept**, with item 4.
   **Apply:** `2Sam.8.8` la: `omniaque vāsa.` → `omniaque vāsa\f + \fr 8:8 \ft ‘ex quō … vāsa’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*.`

## C. Places near the bar (recommended left out)

**Decision:** accept 8 (Nathan, 2026-11-21: "Add the 12:31, since it isn't an inconsequential name in a list, and all modern editions agree against him"); reject 6, 7, 9 (as recommended, under his "Approve all")

6. **8:13** *cæsīs in valle salis Syrōrum octōdecim mīllibus, et apud Gebelem ad vīgintī tria mīllia*: two things.
   (a) Kind A by the letter: the Hebrew אֲרָם, "Aram", which Castellio keeps (*Syrōrum*); the NRSVue and the BSB
   "Edomites" (notes "Gk Syr Heb mss: MT *Arameans*", "A few Hebrew manuscripts, LXX, and Syriac … most Hebrew
   manuscripts Arameans"), as 8:12 (*Syris*; the BSB's note, the NRSVue "Edom" in its text). (b) Castellio's **L. … H.**
   clause *et apud Gebelem ad vīgintī tria mīllia*, a second slaughter at "Gebel" (Brenton's LXX has *ἐν Γεβελὲμ* for
   the place of the one battle, the Vulgate neither; source not found). Both a people's name, a place and a number:
   dropped by the rule of 2026-11-19, as 1 Sam 12:11 and Judg 4:5. 1554 (canvas 175, column 326, *L. & apud Gebelem
   ad uiginti tria | millia. H.*), 1738 (line 244). **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `2Sam.8.13` la: `ad vīgintī tria mīllia.` → `ad vīgintī tria mīllia\f + \fr 8:13 \ft ‘et apud Gebelem … mīllia’ Castelliō addit; Hebraicē nōn est.\f*.`

7. **12:14** *quoniam tū istā rē Jōvæ inimīcīs maledīcendī occāsiōnem dedistī*: Hebrew נִאֵץ נִאַצְתָּ אֶת־אֹיְבֵי יְהוָה, "you
   have utterly scorned the enemies of the LORD" (the KJV "given great occasion to the enemies of the LORD to
   blaspheme"). The NRSVue "you have utterly scorned the LORD" (note "Cn: Heb *scorned the enemies of the Lord*"); the BSB
   "shown utter contempt for the word of the LORD" (note "DSS; MT you have brought utter contempt from the enemies of the
   LORD"). Both leave the Hebrew, for different readings; Castellio keeps it, as the Vulgate (*blasphemare fecisti
   inimicos Domini*) and Brenton's LXX (*παρώργισας τοὺς ἐχθροὺς Κυρίου*). But the judgement does not change: David's
   sin has dishonoured the LORD and the child will die, in all of them; Castellio's form is the traditional reading of
   the Hebrew (the KJV's). The case of 1 Sam 3:13 (*nēquiter sē gerere*, left out). **Recommendation (Claude): leave
   out.**
   **Apply (only if accepted against the recommendation):** `2Sam.12.14` la: `occāsiōnem dedistī;` → `occāsiōnem dedistī\f + \fr 12:14 \ft Hebraicē אֶת־אֹיְבֵי יְהוָה, ‘Jōvæ inimīcōs’; versiōnēs recentiōrēs ‘Jōvam ipsum contempsistī’ legunt.\f*;`

8. **12:31** *idemque fēcit omnibus oppidīs Mōabītārum*, **the closest call**: Hebrew וְכֵן יַעֲשֶׂה לְכֹל עָרֵי בְנֵי־עַמּוֹן,
   "and so he did to all the cities of the Ammonites"; the NRSVue, the BSB, the Vulgate (*universis civitatibus filiorum
   Ammon*) and Brenton's LXX (*πάσαις ταῖς πόλεσιν υἱῶν Ἀμμών*) the same. Castellio's *Mōabītārum* is his own, not a
   misprint of 1738's: 1554 (canvas 177, column 330, zoom `z177-12_31.jpg`, *idẽq; | fecit omnibus oppidis Moabitarũ*),
   1573 (canvas 215, search API, *omnibus oppidis Moabitarum*), 1726 (`2sam1-24-transcription.md`) and 1738 (line 357)
   alike; flagged by `r4.md`. A plain slip of the pen, since chapters 10–12 are the Ammonite war and Moab was dealt with
   at 8:2. Kind C, but a people's name: by the rule of 2026-11-19 (1 Sam 12:11 *Bedanem*, Judg 4:5 *Hormam*: "even when
   it is a plain misreading") it is dropped. Against that, it changes what the verse says David did, and to whom: the
   treatment of the Ammonite towns is told of Moab's, which a reader of any Bible will notice. Left to Nathan.
   **Recommendation (Claude): leave out**, by the rule; accept if Nathan takes "to whom it was done" as what happens.
   **Apply:** `2Sam.12.31` la: `omnibus oppidīs Mōabītārum,` → `omnibus oppidīs Mōabītārum\f + \fr 12:31 \ft Hebraicē עָרֵי בְנֵי־עַמּוֹן, ‘oppidīs Ammonītārum’.\f*,`

9. **7:23** *ut ejus causā tam inaudīta et terribilia facerent, quam tū tuæ terræ fēcistī in tuōrum grātiam, quōs tibi
   ex Ægyptī tum gentibus tum diīs redēmptōs* (7:23–24): Hebrew וְלַעֲשׂוֹת לָכֶם הַגְּדוּלָּה וְנֹרָאוֹת לְאַרְצֶךָ מִפְּנֵי עַמְּךָ, "and to
   do for you great and awesome things for your land, before your people, whom you redeemed for yourself from Egypt,
   nations and their gods". The NRSVue follows the Greek, "doing great and awesome things for them, by driving out
   before his people nations and their gods" (notes "Gk: Heb adds *for you*", "Gk: Heb *for your land*"); the BSB the
   same ("by driving out nations and their gods from before Your people", note "See LXX and 1 Chronicles 17:21"). So
   kind A by the letter: Castellio keeps "for your land" (and reads לָכֶם as לָהֶם, "for it", with the Vulgate, as his
   annotation says: `notes-1554-a.md` §1). But the sense stands: in all of them God has done unheard-of and terrible
   things for his people, redeeming it from Egypt, from the nations and their gods; "driving out" only names the
   manner. A prayer's construal, as 1 Sam 2:33. His *quam diī redēmptum īverint* ("which gods went to redeem", reading
   the Hebrew's אֱלֹהִים with its plural verb הָלְכוּ) is a reading of the Hebrew as it stands; the NRSVue and the BSB "God",
   and the comparison holds either way. **Recommendation (Claude): leave out.**

## D. 1738's footnotes (recommended: none printed)

**Decision:** none printed (Nathan, 2026-11-21: "Approve all")

1738 prints 15 lettered footnotes in chapters 1–12 (`%` rows of `data/witnesses/read-1738/2Sam1-24.tsv`, letters
*f*–*q* and *a*–*d*). **Twelve are Castellio's 1554 margins**, changed only in spelling; 6:23's, 8:18's and 9:9's are not
in 1554 (6:23's probably 1573's; `notes-1554-a.md` §3). As in Joshua, Judges, Ruth and 1 Samuel (`josh-notes.md` §E,
`judg-notes.md` §D, `ruth-notes.md` §C, `1sam-notes-a.md` §D), the edition prints no glosses (brief.md: "No marginal
notes or commentary"). Each, with what it glosses:

- **1:18** *f) quoniam Saulus fuerat a sagittariis vulneratus,* (why *artem sagittāriam*). **1:20** *g) vrbes.*
  (*puellæ*, the daughters). **1:21** *h) pro monte dicit montes poetice.* (*Ō montēs Gelboe*). **2:9** *i) Latinus
  Gessuræos, Græcus Thasiri.* (*Assuræōs*: the Vulgate's and the Greek's names for the Hebrew's Ashurites; the NRSVue and
  the BSB "the Ashurites", with him). **2:14** *k) hoc est, dimicarent.* (*lūderent*). **2:29** *l) Latinus Bethorone.*
  (*Bethrone*, the Hebrew's Bithron; the Vulgate's name; the NRSVue "the whole forenoon", "Meaning of Heb uncertain",
  the BSB "all morning", "See LXX": a disputed word, and a place). **3:14** *m) ducenta dederat. Sed ideo centum dicit,
  quia centum petierat Saulus.* (the hundred foreskins; 1 Sam 18:27 has two hundred). **4:6** *n) Græce, quum quidem
  ædium ianitrix (quæ triticum euellebat) somno oppressa dormiret,* (the Greek's doorkeeper; the NRSVue "Meaning of Heb
  uncertain", the BSB the Hebrew: disputed). **6:23** *o) scilicet ex Dauide. Nam ex Adriele quinque filios habuit. cap.
  21, 8.* (Michal childless). **8:18** *p) præcipui, quibus in primis vtebatur.* (*antistitēs*: what David's sons
  were; the NRSVue "priests", the BSB "priestly leaders", note "Literally priests, or possibly chief officials").
  **9:9** *q) Michæ.* (*id dominī tuī fīliō dō*, the grandson). **11:4** *a) foris mansit polluta ad vesperum, ob
  concubitum, vt iubebat lex, Leu, 15.* (Bathsheba's purification). **11:8** *b) misit ei rex de sua cœna.* (*rēgium
  ferculum*). **11:21** *c) Ierobaalis, hoc est,Gedeonis.* (*Jerobosethi*: the Hebrew's Jerubbesheth; the NRSVue
  "Jerubbaal", "Gk Syr: Heb *Jerubbesheth*"; a name). **12:25** *d) hoc est, Iouæ carum.* (*Jedidiam*; the NRSVue's own
  note "That is, *beloved of the Lord*").

None marks a departure that meets the bar; the textual ones (2:9, 2:29, 4:6) report the versions at a name or at a
word the modern Bibles call uncertain. **Recommendation (Claude):** print none.

## E. 1738's asterisks

1738's four asterisks in these chapters (5:8, 7:7, 7:23 end, 12:26 end on the KJV's numbering;
`2sam1-24-transcription.md` lists 7:24 and 12:26 by where the readers found them) **each stand at the lemma of one of
Castellio's four 1554 annotations on 2 Samuel 1–12**, in the same order, one for each (`notes-1554-a.md` §2): 5:8
*inuisos, \* ex quo* ↔ *CLaudosq; & cæcos Dauidi inuiſos.)*; 7:7 *præsidum Israelitarum \* (cui meos* ↔ *Ecquod ulli
præſidum Iſraelitarum.)*; 7:23 *in tuorum gratiam, \* quos tibi* ↔ *Quam tu in terris feciſti in tuorum gratiam.)*;
12:26 *ceperat: \* et missis* ↔ *Cum regiam urbis partem cępiſſet.)*. As in 1 Samuel (fourteen of fourteen) and Ruth,
the asterisk is the sign that Castellio has an annotation on the place. The edition prints no asterisks. The one
annotation that meets the bar has item 1 (5:8); 7:7 and 12:26 are commentary on words where the modern Bibles read with
him in sense; 7:23's annotation commends a reading its own text does not carry (item 9; `notes-1554-a.md` §1).

## F. Considered and left out

- **The tool's candidates**, besides the items above: **1:21** *ut arva eximia* (the BSB alone leaves the Hebrew's
  "fields of offerings", the NRSVue "bounteous fields", "Meaning of Heb uncertain"); **2:29** *Bethrone* (the Hebrew's
  Bithron, a place; disputed, §D); **5:25** *ā Gabā* (the BSB alone "Gibeon"; the NRSVue keeps Geba); **6:4** (the
  Hebrew's repeated clause given once; the BSB and the NRSVue drop it too); **7:16** *tibique firma domus* (both Bibles
  "before me"; Castellio's "for you" keeps the promise, a pronoun); **8:3** *ad fluvium Euphrātem* (with both Bibles);
  **8:4** *mīlle septingentōs equitēs* (the BSB alone, with the LXX, 1,000 chariots and 7,000 charioteers; a number);
  **8:12** *Syrīs* (Aram for Edom: a people's name, as item 6); **9:11** *ad mēnsam meam … inquit ille* (both Bibles
  "David's table" with the Greek; Castellio gives "my table" to the king, so the sense is theirs); **10:18**
  *quadrāgintā mīllibus equitum* (the BSB alone "foot soldiers"; a number); **12:16** (the BSB alone adds sackcloth);
  **6:2, 6:7, 8:8** (with MT: the BSB keeps the Hebrew); **3:3** *Cheleabus* (a name); **6:5** *pīneīs īnstrūmentīs* (the
  NRSVue alone "with songs", with the Qumran ms and the Greek; Castellio and the BSB the Hebrew's "wood"); **8:18**
  *antistitēs* (§D); the numbers of 8:2 (*in trēs partēs … duās morti*: the Hebrew's two lines to death and one to keep,
  the same proportion), 9:13 (*claudus utrōque pede*), 12:6 (*quadruplō*).
- **The NRSVue alone**: 1:12 "struck down" (Q ms Gk), 2:8–4:12 *Ishbaal* for Ish-bosheth (Castellio *Isbosethus*, the
  Hebrew), 3:7 and 4:1 the name supplied (Castellio supplies it too), 5:10 (Q ms Gk), 7:15 (Gk Syr Vg), 11:12 (Gk ms),
  11:21 *Jerubbaal* (§D), 12:30 *Milcom* (the BSB and Castellio *rēgis illōrum*, the Hebrew's "their king"): none with
  the BSB's agreement.
- **The Hebrew uncertain** (the NRSVue's notes): 1:21, 2:29, 3:12, 4:6, 6:7 (*ob temeritātem*, the Hebrew's שַׁל), 6:19,
  7:19.
- **His vocabulary or a construal the context sets right**: 6:2 *Jōvæ armipotentis* and the other "LORD of hosts"
  (1 Samuel's *bellipotēns*, the front matter's matter); 7:7 *præsidum* (Chronicles' "judges", his annotation; the
  modern Bibles "leaders"); 12:26–27 *rēgiam urbis partem*, *urbis partem … in quā erat aquātiō* (his annotation
  defends them); 5:8 *Dāvīdī invīsōs* (the Qere, with the NRSVue); 1:18 *artem sagittāriam … discere jussit* (the
  Hebrew's "the bow", as the KJV; the NRSVue "The Song of the Bow").
- **Castellio's other mark**: 8:13 *L. … H.* (item 6).
- **Not a departure**: 12:31's tortures (*ferrīs tribulīsque … per laterāriam fornācem trājectōs, necāvit*) follow the
  traditional reading of the Hebrew (the KJV "put them under saws … made them pass through the brickkiln"; the Vulgate
  *serravit … traduxit in typo laterum*), where the NRSVue and the BSB read forced labour ("set them to work with saws
  … sent them to the brickworks"): a construal of a disputed verse (the Hebrew's וַיָּשֶׂם בַּמְּגֵרָה is read both ways), no
  note. 1554 read *& calcaria excruciatos* here; the brick-kiln is a later revision (`notes-1554-a.md`, for
  `docs/editions.md`).
