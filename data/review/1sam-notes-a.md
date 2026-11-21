# 1 Samuel 1–15: light notes (Old Testament search), reader A

Built 2026-11-20 in phase 2 of decision 85 (PLAN.md §4), beside `propose`, by the process in `ot-notes-process.md`
(decisions 1A–4A), as Ruth's (`ruth-notes.md`), Judges' (`judg-notes.md`) and Joshua's (`josh-notes.md`), with the bar
as it now stands (Nathan, 2026-11-19: no note for a departure without plot or theological significance; `num-notes.md`
§F: a construal the context sets right is left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an
ancient version and Castellio keeps it; kinds B and C where his reading or his text departs from the Hebrew against the
NRSVue, the BSB and the Hebrew agreeing, and nobody calls the passage uncertain. Chapters 16–31 are reader B's. Castellio's
1554 annotations on these chapters and the 1554 text's margins, read on the page in this pass, are in
`1sam-notes-1554-a.md`.

**Sources read:**
- `1sam-notes-candidates.md` (`python -m pipeline notes 1Sam`), its entries for chapters 1–15: 12 BSB *against MT*
  (1:24, 1:28, 2:17, 2:20, 2:33, 3:13, 8:16, 10:27, 12:11, 13:1, 13:5, 13:20, 14:41), 10 *with MT* (1:22, 1:23, 5:6,
  6:19, 7:12, 10:1, 12:3, 12:6, 12:8, 12:15, 14:18, 14:47), 7 *other* (1:1, 10:21, 11:1, 11:8, 12:9, 13:15, 15:32), 17
  numbers, and Castellio's marks at 2:8, 5:6 (5:7 is the same mark), 11:1, 12:15 (the tool's 12:15 *G. non infestabit
  … H.* is 12:14's). Also 9:1's *L. … H.*, which the tool does not list (`1sam1-31-transcription.md`).
- The NRSVue (Bible Gateway, read 2026-11-20) for chapters 1–15 with all its footnotes (not stored). The NET was not
  read. Every verse of the preview (`text/draft/1SA.preview.usfm`) read against the BSB, with the WLC, the Vulgate and
  Brenton's LXX (`sources/parallel/`) where a verse looked odd.
- 1738's 24 footnotes and 7 asterisks in these chapters, from phase 1 (`data/witnesses/read-1738/1Sam1-31.tsv`,
  `1sam1-31-transcription-readers.md`).
- The printings: 1738 as printed (`text/orig/1SA.usfm`), the 1750 raw OCR (`sources/archive/1750/text.txt`), **1554**
  (canvases 152–161 and 825) and **1573** (canvases 190 and 195) on page images read here (`1sam-notes-1554-a.md`).

The yield is 4 notes proposed in 15 chapters (0.27 a chapter): two of Castellio's *G.* … *H.* passages that no modern
Bible prints (2:8, 5:6), the broken numbers of 13:1 (where Castellio's own annotation and 1554's daggers call the Hebrew
mutilated), and one kind A (14:41). Four more near the bar are recommended left out (12:15, 2:33, 8:16, 3:13).

## A. Modern Bibles follow the versions (kind A)

**Decision:** accept (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

1. **14:41** *Deus Isrāēlītārum age sevērē*: Hebrew אֱלֹהֵי יִשְׂרָאֵל הָבָה תָמִים, "God of Israel, give *tāmîm*" (the KJV "Give a
   perfect lot"). The NRSVue follows the Greek and the Old Latin: "O LORD God of Israel, why have you not answered your
   servant today? If this guilt is in me or in my son Jonathan, O LORD God of Israel, give Urim; but if this guilt is in
   your people Israel, give Thummim" (note "Gk OL: Heb *Saul said to the LORD, the God of Israel*"); the BSB the same
   ("respond with Urim … respond with Thummim"; note "LXX and Vulgate; MT contains only the short quotation, 'Give a
   perfect (lot).'"). The Vulgate has it (*da indicium … da ostensionem … da sanctitatem*), and Brenton's LXX (*δὸς
   δήλους … δὸς δὴ ὁσιότητα*). Castellio keeps the Hebrew's short text, and reads תָמִים as an adverb ("deal sternly").
   **Why it passes the bar**: what Saul does changes. In both modern Bibles he puts the question to God by the Urim and
   Thummim, the oracle the priest carries (14:3, 14:18–19, 14:36–37: God has not answered), and the lot falls by it on
   Jonathan; in Castellio he only prays God to act severely. The sacred lot is the hinge of the chapter, and a reader of
   a modern Bible meets the Urim and Thummim here. Kind A, as Judg 14:15.
   Castellio's own names for the Urim and Thummim are *Clāritās* and *Integritās* (Exod 28:30 *CLĀRITĀS ET INTEGRITĀS*;
   Deut 33:8 *Tua integritās et clāritās*, `text/EXO.usfm`, `text/DEU.usfm`), so the note uses them. 1554 (canvas 160,
   column 296, *Deus Iſraelitarum age ſeuerè*), 1738 (`text/orig/1SA.usfm` line 415, *Deus Israelitarum age seuere*) and
   1750 (OCR line 39581, *age feuere*) the same.
   Words checked with `pipeline latin macron-check` (no flag but the proper names); *Jonathāne* as the preview has it.
   **Recommendation (Claude): accept.**
   **Apply:** `1Sam.14.41` la: `age sevērē.” Ac` → `age sevērē\f + \fr 14:41 \ft Versiōnēs antīquæ habent ‘Deus Isrāēlītārum, cūr servō tuō hodiē nōn respondistī? Sī in mē aut in Jonathāne fīliō meō hæc culpa est, dā Clāritātem; sīn in populō tuō, dā Integritātem’.\f*.” Ac`

## B. Castellio's reading or text departs from the Hebrew (kinds B and C)

**Decision:** accept 2, 3, 4; item 5 (12:15) left out (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

2. **2:8** *Quī et precantibus vōta concēdit … et jūs æquumque facit in terrīs*: Castellio's **G. … H.** passage in
   Hannah's song (1738's verses 9–11, merged into the KJV's 2:8 in versification, `1sam1-31-transcription.md`): a reading
   he took from the Greek, which neither the Hebrew nor any modern Bible has. Brenton's LXX 2:9–10 (*διδοὺς εὐχὴν τῷ
   εὐχομένῳ· καὶ εὐλόγησεν ἔτη δικαίου … μὴ καυχάσθω ὁ φρόνιμος ἐν τῇ φρονήσει αὐτοῦ … ποιεῖν κρίμα καὶ δικαιοσύνην ἐν μέσῳ
   τῆς γῆς*) is his source, word for word: "who grants the vow of him who vows, and blesses the years of the just; for
   man is not strong by might. The Lord will weaken his adversary, the Lord is holy. Let not the wise man boast in his
   wisdom …" (the last from Jer 9:23–24). The NRSVue and the BSB print the Hebrew 2:8–10 with none of it (the NRSVue's
   only notes at 2:8–10 are 2:10 *Most High*, "Cn"); the Vulgate neither. Castellio then gives the Hebrew's own 2:8b–10
   as well (*Nam Jōvæ sunt terræ cardinēs … quandoquidem homō vīribus nōn valet. Jōvæ frangentur adversāriī …*), so two
   lines of the Greek block (*Neque enim homō vīribus valet. Dominus īnfirmōs reddit adversāriōs suōs*) are doublets of
   the Hebrew's 2:9b–10a; the rest (the vows granted, the years of the just, the sentence from Jeremiah) has nothing
   behind it in the Hebrew. The edition no longer prints the marks (`1sam1-31-draft-fixes.md` §2), so without a note
   the reader cannot tell this passage from the Hebrew's.
   **Why it passes the bar**: a passage of the song with its own teaching (God hears the vow; the wise, the strong and
   the rich are not to boast, but to know the Lord), which a reader of any modern Bible will not find. The same case as
   Exod 2:22, Exod 6:20 and Josh 16:10 (`gen-notes.md` §C; `judg-notes.md` §C, where Judg 16:13–14 was left out only
   because the modern Bibles add it too). Kind C.
   Castellio's: 1554 prints the marks in the text (canvas 153, columns 281–282, *mittat. G. Qui & pre-|cantibus uota
   cõcedit* … *facit in terris.H.Nã Iouę*); 1738 (`text/orig/1SA.usfm` line 55) and 1750 (OCR lines 37724–37730,
   *mittat. G. Qui / et precantibus vota concedit*) the same.
   The form of Josh 16:10. **Recommendation (Claude): accept.**
   **Apply:** `1Sam.2.8` la: `jūs æquumque facit in terrīs.` → `jūs æquumque facit in terrīs\f + \fr 2:8 \ft ‘Quī et precantibus … in terrīs’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*.`

3. **5:6** *et ipsōrum fīnēs ēnātīs mūribus īnfestandō, ex quō ingentī clāde perturbāta cīvitās est*: two **G. L. … H.**
   passages ("Greek and Latin"), the mice that overran the land of Ashdod and the deadly panic in the city. Hebrew
   וַיַּךְ אֹתָם בעפלים אֶת־אַשְׁדּוֹד וְאֶת־גְּבוּלֶיהָ, "and he struck them with tumours, Ashdod and its territory", and no more. The
   Vulgate adds *Et ebullierunt villæ et agri in medio regionis illius, et nati sunt mures et facta est confusio mortis
   magnæ in civitate*, Brenton's LXX *καὶ μέσον τῆς χώρας αὐτῆς ἀνεφύησαν μύες· καὶ ἐγένετο σύγχυσις θανάτου μεγάλη ἐν τῇ
   πόλει*. The NRSVue prints the Hebrew with no note; the BSB too (note "Hebrew; LXX and Vulgate include *And rats
   appeared in their land, and death and destruction were throughout the city*"). Castellio follows the two versions.
   **Why it passes the bar**: it changes what the plague is. In the Hebrew and in both modern Bibles the LORD strikes
   Ashdod with tumours, and the mice first appear at 6:4–5, in the diviners' answer; in Castellio a plague of mice has
   already ravaged the land, so the golden mice of 6:4–5 answer something he has narrated. A reader comparing a modern
   Bible meets no mice at 5:6. Kind C, the case of 2:8 above. **Near the bar** in being half a sentence; recommended for
   the same reason as 2:8: the marks are gone from the edition.
   Castellio's: 1554 (canvas 155, column 285, *& ipſo-|rum fines G.L. enatis muribus H. infeſtando, G. L. ex quo
   ingenti clade perturbata ciuitas eſt H.*), 1738 (line 147), 1750 (OCR line 38232, *G. L. enatis muribus H.
   infeftan-*) the same. 1554 prints a further *H.* before 5:6 (*tranſcẽdunt. H. Tum Ioua*) with no *G.* before it in 5:1–5;
   1738 does not print it (`1sam-notes-1554-a.md`).
   **Recommendation (Claude): accept.**
   **Apply:** `1Sam.5.6` la: `perturbāta cīvitās est.` → `perturbāta cīvitās est\f + \fr 5:6 \ft ‘ēnātīs mūribus’ et ‘ex quō … cīvitās est’ Castelliō ex Græcō addit, ut Vulgāta; Hebraicē nōn est.\f*.`

4. **13:1** *Inīvit autem Saulus rēgnum, annum agēns, et rēgnāvit in Isrāēlītās annōs duōs*: Hebrew בֶּן־שָׁנָה שָׁאוּל
   בְּמָלְכוֹ וּשְׁתֵּי שָׁנִים מָלַךְ עַל־יִשְׂרָאֵל, "Saul was a year old when he began to reign, and he reigned two years over Israel."
   Castellio translates the Hebrew as it stands. But the Hebrew is broken, and every witness says so: the NRSVue "Saul
   was … years old … and he reigned … and two years" (notes "The number is lacking in the Heb text (13.1 is lacking in
   Gk mss)" and "*Two* is not the entire number; something has dropped out"); the BSB fills it, "Saul was thirty years
   old … and he reigned over Israel forty-two years" (note "A few late LXX manuscripts; MT Saul was a son of a year").
   **Castellio thought so too**: his 1554 annotation (canvas 825, column 346, `1sam-notes-1554-a.md` §1) argues that the
   Hebrew cannot mean what *annum agēns* says, that "the place is mutilated" (*locum eſſe mutilatum*), and that Saul
   reigned not two years but forty (Acts 13:21, Josephus); and his 1554 text marks the two gaps with daggers (*annũ
   agens † & regnauit in Iſraelitas annos † duos*, canvas 159, column 293), which 1573 keeps (canvas 195) and 1738 turns
   into one asterisk (after *regnum,*, `1sam1-31-transcription-readers.md`, reader 07). The edition prints neither.
   **Why it passes the bar**: as printed, the edition says Saul came to the throne in his first year of age, or (as
   *annum agēns* may be read) a year into something, and reigned two years: a reader takes the length of Israel's first
   reign from it, against Acts 13:21 and every modern Bible. Castellio meant his reader to see a gap here. Not kind A, B
   or C exactly: the note gives the Hebrew and says what everyone, Castellio included, says of it. The NRSVue calls the
   numbers lost, not the passage disputed; the BSB's figures are a guess from late Greek manuscripts and are not given.
   1738 (line 346, *Iniuit autemSaulus regnum, annum agens, et regnauit in Israelitas annos duos.*), 1750 (OCR lines
   39246–39248) the same, without the daggers.
   The form *Hebraicē* Hebrew, ‘Latin’, with the fact after it, as Gen 33:19 and 49:10. Words checked with
   `pipeline latin macron-check`.
   **Recommendation (Claude): accept.**
   **Apply:** `1Sam.13.1` la: `in Isrāēlītās annōs duōs.` → `in Isrāēlītās annōs duōs\f + \fr 13:1 \ft Hebraicē בֶּן־שָׁנָה … וּשְׁתֵּי שָׁנִים, ‘annum nātus … et duōs annōs’; numerī excidērunt.\f*.`

5. **12:15** *et vōs et vestrum rēgem Jōva īnfēstābit*, **near the bar**: Hebrew וּבַאֲבֹתֵיכֶם, "and against your fathers".
   Castellio follows the Greek (Brenton *καὶ ἐπὶ τὸν βασιλέα ὑμῶν*) and marks it **G. … H.**, and this is the one
   textual note among 1738's footnotes, Castellio's own 1554 margin: *a in Hæ-|bręo eſt,pa|tres ue-|ſtros:ſed|in Græco|
   melius,ut|mihi ui-|detur.* (canvas 158, column 292; 1738's *s) in Hebræo est, patres vestros: sed in Græco melius, vt
   mihi videtur.*). The modern Bibles divide: the NRSVue follows the Greek too, "against you and your king" (note "Gk:
   Heb *and your ancestors*"); the BSB keeps the Hebrew, "as it was against your fathers" (note "Hebrew; LXX against
   your king"); the Vulgate *super patres vestros*. So the consensus of §3 of the process fails: the NRSVue reads with
   Castellio, and a reader with the NRSVue finds what he finds. And the sense is near: the threat stands, against the
   people and their king (12:25 says it in the Hebrew too, *et vōs et rēx vester perībitis*). Below the bar, as Judg
   12:7 (only the NRSVue following the Greek) and Gen 44:6. His 12:14 mark (*G. nōn īnfēstābit vōs Jōva. H.*, the
   apodosis the Hebrew lacks; the NRSVue "it will be well", the BSB "then all will be well", both supplying it) needs
   nothing. 1554 (canvas 158, column 292, *& uos & ᵃ G. | ueſtrũ regem. H.Ioua infeſtabit*), 1738 (line 332), 1750 (OCR line
   39203) the same.
   **Recommendation (Claude): leave out.** If Nathan wants Castellio's one textual margin in the edition, this is its
   form:
   **Apply (only if accepted against the recommendation):** `1Sam.12.15` la: `et vōs et vestrum rēgem Jōva` → `et vōs et vestrum rēgem\f + \fr 12:15 \ft Hebraicē וּבַאֲבֹתֵיכֶם, ‘et in patrēs vestrōs’; ‘vestrum rēgem’ Castelliō ex Græcō vertit.\f* Jōva`

## C. Kind A places near the bar (recommended left out)

**Decision:** left out (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

6. **2:33** *ut omnēs, quī tuæ posteritātī accrēverint, ætāte virīlī moriantur*: Hebrew יָמוּתוּ אֲנָשִׁים, "shall die as men"
   (the KJV "in the flower of their age"). The NRSVue "shall die by the sword" (note "Q ms Gk: MT *die like mortals*"),
   the BSB "will die by the sword of men" (note "DSS and LXX; MT will die as mortals or will die in the prime of life").
   Both leave the Hebrew; Castellio keeps it. But the sense stands: Eli's house loses its men young (2:31–32 have said
   it, *ut nūllus sit domī tuæ senex*), and the sword only names the manner, which 22:18–19 shows. The NRSVue's other
   changes in the verse (his eyes, his heart, with one survivor in view) are the NRSVue's alone (the BSB keeps "your").
   **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Sam.2.33` la: `ætāte virīlī moriantur.` → `ætāte virīlī moriantur\f + \fr 2:33 \ft Versiōnēs antīquæ habent ‘gladiō virōrum moriantur’.\f*.`
7. **8:16** *juvenum vestrōrum lēctissimōs*: Hebrew בַּחוּרֵיכֶם הַטּוֹבִים, "your best young men". The NRSVue "the best of your
   cattle" (note "Gk: Heb *young men*"), the BSB "your best cattle" (note "LXX; Hebrew your best young men"). Kind A, but
   one item in the list of what the king will take; the young men are taken in 8:11–12 already, and nothing in the
   warning changes. Below the bar, as Deut 11:30 and Judg 20:33. **Recommendation (Claude): leave out.**
8. **3:13** *cum fīliōs suōs nēquiter sē gerere nōn ignōrāret*: Hebrew כִּי־מְקַלְלִים לָהֶם בָּנָיו, "his sons were cursing for
   themselves" (the KJV "made themselves vile"). The NRSVue "his sons were blaspheming God" (note "Gk: Heb *cursing for
   themselves*"), the BSB "his sons blasphemed God" (note "LXX; Hebrew made themselves contemptible"). Kind A by the
   letter; but Castellio's "behaved wickedly" is a general rendering of the Hebrew as it stands, and the sons' sin is
   told in full in 2:12–17 and 2:22 (*Jōvæ fertum male apud hominēs audiēbat*, their contempt for the offering). The
   judgement on Eli's house does not change. **Recommendation (Claude): leave out.**

## D. 1738's footnotes (recommended: none printed)

**Decision:** none printed, as Joshua, Judges, Ruth (Nathan, 2026-11-20: "Yes, settle it", after the phase 2 summary `1sam1-31-edition.md`; approved for now, his in-depth review comes later)

1738 prints 24 lettered footnotes in chapters 1–15 (`%` rows of `data/witnesses/read-1738/1Sam1-31.tsv`, letters *c*–*t*
and *a*–*g*). **23 are Castellio's 1554 margins**, changed only in spelling; one (4:21 *i) periit gloria.*) is first
found in 1573 (`1sam-notes-1554-a.md`, table). All are glosses on the sense except 12:15's, which is item 5. As in
Joshua, Judges and Ruth (`josh-notes.md` §E, `judg-notes.md` §D, `ruth-notes.md` §C), the edition prints no glosses
(brief.md: "No marginal notes or commentary"). Each, with what it glosses:

- **1:22** *c) ministret.* (at *ut Jōvæ appāreat*): what "appear before the LORD" means. **2:3** *d) scilicet
  hominum.* (*irritī sunt cōnātus*, whose attempts). **2:12** *e) contemtores.* (*Jōvæ ignārī*). **2:27** *f) scilicet
  Leuis.* (*tuī parentis*). **2:32** *g) Videbunt posteri tui, non sine suo dolore, pontificem non ex te natum, qui
  sacrificiis fruatur: quæ Israelitæ de collatis sibi diuinitus bonis facient.* (*spectābisque in fānō æmulum*). **2:33**
  *h) dum tui posteri seruient alii pontifici.* (*quō tibi et oculī cōnsūmantur*). **4:21** *i) periit gloria.* (the
  meaning of *Ichabodum*; the verse says it). **5:6** *k) condylomatis, quum procidit sedes,* (*pōdicis morbō*, what the
  disease is). **6:20** *l) seuerum.* (*tam augustum*). **9:6** *m) vates.* (*dīvīnus*). **9:9** *n) sciscitatum
  oraculum.* (*Deum cōnsultum*). **9:24** *o) Sciebam, te adfuturum. Ideoque coquo, vt hoc reseruaret, mandaui: me enim
  habiturum conuiuas alios.* (*quod dīcerem, mē invītāsse hominēs*). **10:1** *p) suorum Israelitarum.* (*suæ
  possessiōnis*). **10:3** *q) Dei fanum.* (*ad Deum*). **10:12** *r) non solum vates est Saulus, sed etiam vatum pater,
  hoc est summus.* (*quis eōrum pater est?*). **12:15** *s)* item 5. **12:21** *t) diuos et inanes deos.* (*ad ista
  nihilī*). **14:12** *a) docebimus vos, quid sit nos lacessere, hoc est, vos interficiemus.* (*vōs quidpiam docēbimus*).
  **14:27** *b) qui scilicet peruigilatione aut fame caligabant.* (*illūstrātī sunt ejus oculī*). **14:30** *c) quæ
  videlicet melle dulcior est, quanta victoriæ lux esset exorta nobis?*, *d) ad satietatem.*, *e) quia fame languent
  milites,* (*dē prædā*, *quantum satis*, *nōn satis magna*). **15:6** *f) erant ii Iethrone Mosis socero prognati.*
  (*Cenæōs*). **15:17** *g) Dixerat enim Saulus, se tenuissimæ conditionis esse, cap. 9, 21,* (*ut tū tibi vidēbāre*).

None marks a departure from the Hebrew; the nearest, 4:21's and 10:1's, give what the Hebrew's words mean, and the
verses say it. **Recommendation (Claude):** print none; item 5 covers 12:15's.

## E. 1738's asterisks

1738's seven asterisks in these chapters (1738's 1:3, 6:8, 6:17, 8:12, 12:17, 13:1, 14:36; `1sam1-31-transcription.md`)
**each stand at the lemma of one of Castellio's 1554 annotations on 1 Samuel**, and there is one asterisk for each of
the seven annotations on chapters 1–15, in the same order (`1sam-notes-1554-a.md` §2): 1:3 *bellipotentem \* venerandum*
↔ *Ad Iouam bellipotentem.)*; 6:8 *simulacra, \* quæ illi* ↔ *Aureaq; simulachra quæ illi,&c.)*; 6:17 (KJV 6:18)
*saxum, \* in quo* ↔ *Et ad ingens illud ſaxum.)*; 8:12 *centuriones \* creabit* ↔ *Hos tribunos, hos centuriones.)*;
12:17 *tonabit, \* atque pluet* ↔ *Tritici meſsis eſt, Iouam inuocabo, & tonabit.)*; 13:1 *regnum, \* annum agens* ↔
*Iniuit autem Saulus regnum,&c.)*; 14:36 *deprædarentur,\** ↔ *Eosq; uſque ad lucem matutinam perimerent.)*. Ruth's one
asterisk (3:16) stands at the lemma of Castellio's one annotation on Ruth in the same way. So in 1738 the asterisk is
the sign that Castellio has an annotation on the place (the annotations themselves are not on 1738's pages; whether
1738 prints them elsewhere was not checked). The edition prints no asterisks; the one annotation on these chapters that
meets the bar has item 4. (On canvas 825 the annotations on chapters 17 and 20, *Vir quidam immanis.)*, *Iam ſenex &
ætate prouecta.)*, *Deſcendes autem ad ſummum ter.)*, stand at reader B's asterisks at 17:4, 17:12 and 20:18/19.)

## F. Considered and left out

- **The tool's candidates**, besides the items above: **1:24** *tribus cum taurīs* (both Bibles "a three-year-old bull"
  with the Qumran ms, the LXX and the Syriac; Castellio the Hebrew's "three bulls", as the Vulgate): the number of
  victims at Samuel's dedication, nothing turns on it (and 1:25 *taurum*, the Hebrew's singular, stands in both); **1:28**
  (only the BSB, "they worshiped"); **2:17** (the BSB alone, "the men"/"they"); **2:20** *prout ipsa ā Jōvā
  postulāverat* (both Bibles leave the Hebrew's "for the request he asked of the LORD" for "the loan she lent", but
  Castellio does not follow the Hebrew either: a construal of an obscure clause, the blessing kept); **10:27** (the
  Qumran passage about Nahash, in the NRSVue only; the BSB keeps the Hebrew); **12:11** *Bedanem* (both Bibles "Barak",
  the NRSVue also "Samson" for Samuel; Castellio the Hebrew): a name in a list of deliverers, dropped by Nathan's rule of
  2026-11-19, as Judg 4:5's kind was; **13:5** *trīgintā mīllia curruum* (the BSB alone, 3,000; a number); **13:20**
  (both Bibles "sickles" for the Hebrew's repeated "plowshare"; tools in a list); **1:22, 1:23, 7:12, 10:1, 10:21, 12:3,
  12:6, 12:8, 12:9, 13:15** (the NRSVue alone follows the Greek or the Qumran ms; the BSB keeps the Hebrew); **5:6** is
  item 3; **6:19** (both Bibles 70 dead for the Hebrew's 50,070; Castellio the Hebrew: a number); **11:1** *post ūnum
  ferē mēnsem* (Castellio's *G. L.* mark, and both Bibles add "about a month later" with the Qumran ms and the LXX:
  Castellio goes their way, as Judg 16:13–14); **11:8** (a number; the BSB keeps the Hebrew's 30,000); **12:15** item 5;
  **14:18** *dīvīnam arcam* (both Bibles keep the Hebrew's ark; the LXX's ephod in the BSB's note only); **14:47** (both
  keep the Hebrew); **15:32** *dēlicāte … mortis acerbitātem abfore spērāns* (the NRSVue alone emends: "haltingly",
  "Surely death is bitter"; Castellio with the Hebrew and the BSB); **1:1** (Ramathaim-zophim, a name); the numbers of
  2:13, 4:2, 5:4, 6:10, 8:12, 8:15, 8:17, 10:19, 11:11, 13:2, 13:17–18, 13:21, 14:4, 14:49 (numbers on one side only:
  *tridentem*, *ambābus*, *duās*, *decimābit*, *tribūnōs*, *tripartītō*, *alter … alter*; the counts read, 4:2, 11:8,
  11:11, 13:2, 13:17–18, the Hebrew's).
- **Castellio's other marks**: **9:1** *fīliī Sarethi* (*L. … H.*, a name in Kish's genealogy that the Hebrew, the
  modern Bibles and the Vulgate lack; its source not found in Brenton): a name, dropped. **12:14** (above, item 5).
- **The Bibles differ or the Hebrew is uncertain**: **1:5** *portiōnem ūnam trīstī vultū* (אַפָּיִם; the NRSVue "double
  portion", "Syr: Meaning of Heb uncertain"); **2:25** *disceptant arbitrī* (אֱלֹהִים read as judges, as the KJV); **2:32**
  *spectābisque in fānō æmulum* (צַר מָעוֹן, the KJV "an enemy in my habitation"); **13:21** *obtūsī vomerēs* (the *pim*;
  the NRSVue "Meaning of Heb uncertain"; a price besides).
- **His vocabulary or a construal the context sets right**: 1:3, 1:11, 4:4, 15:2 *bellipotēns*, *armipotēns* for
  "LORD of hosts" (his 1554 annotation on 1:3 explains it; the front matter's matter); 8:12 *tribūnōs*, *centuriōnēs*
  (the notes never mark these, `ot-notes-process.md` §2; his annotation defends them); 6:8 *aurea simulācra* (כְּלֵי
  הַזָּהָב, "gold objects": they are the images of 6:4–5, his annotation says so); 15:29 *Isrāēlītārum triumphātor* (נֵצַח
  יִשְׂרָאֵל, "the Glory of Israel"); 15:5 *apud fluvium* (בַּנָּחַל, "in the valley"); 4:1, 5:1 *saxum auxiliī* for
  Ebenezer, as 7:12 names it; 2:12 *Jōvæ ignārī*.
- **Checked and not a departure**: **15:35** ends without the Hebrew's "and the LORD regretted that he had made Saul
  king over Israel"; Castellio moves it into 16:1 (*At Jōva, quem Saulī … rēgis creātī pænitēbat*; 1554 canvas 161,
  column 298; 1738 line 470), so nothing is lost. **14:36** *dēprædārentur* is the Hebrew's "plunder"; Castellio's 1554
  annotation on it defends *perimerent*, a word his printed text does not have (`1sam-notes-1554-a.md` §1).
