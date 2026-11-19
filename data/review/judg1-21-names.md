# Judges: one form per person, place and people (Claude, 2026-11-19)

Every capitalized word of `text/draft/JDG.preview.usfm` (and its draft `JDG.usfm`), and every lower-case or capitalized
adjective of a people or place, was grouped by its unmarked key, read in its verse for its case, matched to the Hebrew
(WLC) and the Greek (Brenton, `sources/parallel/lxx/Judg.tsv`), and decided as Deuteronomy was
(`data/review/deut1-34-names.md`): the settled form first (decision 46, `data/gold/`, Genesis–Deuteronomy and the NT),
then Gaffiot (`pipeline latin macron`; it knows only *Accō, Astaroth, Baal, Dagōn, Dalila, Dēbŏra, Ephrāta, Garizim,
Gĕdĕōn, Jahel, Joās, Jŏnăthās, Lĭbănus, Măgeddō, Pharathōn, Samsōn, Sichem, Sīdōnĭus, Thabor, Thamna, Thēbē,
Zăbŭlōn*), then the Greek's η/ω/ει, then another dictionary (Wiktionary bare = short: *Cison, Micha, Iābēs*), then the
Hebrew vowel (qamets, tsere, holem, shureq, hireq-yod long; decision 52). Gentile adjectives: the founder's marks and the
suffix's quantity (-īnus, -iānus, -ius short i, -ēnsis, -īta, -æus). Case endings read in each verse.

**Counted**: 129 rows below, about 230 persons, places and peoples (related names, a place and its people, or a
founder and his adjective, share a row); 25 rows kept wholly as the preview has them, the rest changed in some form.
**Outputs** (scratch folder; built by `names/build.py`): `names.spelling.tsv` (19 spelling changes, each `old` checked by script to occur
exactly once in its verse of `text/draft/JDG.usfm`) and `names.forms.tsv` (337 forms rows, only where the decided form
differs from the preview, one `#2` row: 13:19 the second *Manoa*, ablative). Built by `names/build.py`.
**Check**: `python check.py names` (`rnames.forms.tsv`): 337 rows, 17 errors, every one a row for a respelled word that
takes effect once its spelling row is applied (1:4 *Pherezæōs*; 1:10 *Sēsæum, Achīmanem, Thalmæum*; 1:12, 1:13, 1:15
×2, 1:20, 3:9 *Caleb-*; 1:27 *Mageddōnēnsēs*; 1:36 *Amorræōrum*; 5:19 *Thanachum*; 11:13, 11:22 *Jabbōc*; 11:20
*Jāsam*; 11:24 *Chamōssus*). 18:11 *Cariathjarīmum* and 21:19 *Jōvæ* pass already (same key).

## Hard calls (for Nathan)

1. **Caleb: *Calebus, Calebī, Calebō*** (1:12, 1:13, 1:15 ×2, 1:20, 3:9; 1738 *Chalebus*, which stage 2 restored on the
   page against Wikisource's *Calebus*). The same man as the settled *Calebus, Calebō* of Numbers and Deuteronomy (C,
   unmarked: Numbers' call 2). Seven spelling rows; drop them to keep 1738's *Chaleb-* in the reading edition (the
   printed text keeps it either way). Wiktionary *Caleb* bare, Greek Χάλεβ: no marks either way.
2. **Sheshai, Ahiman, Talmai: *Sēsæum, Achīmanem, Thalmæum*** (1:10; 1738 *Sesaim, Ahimanem, Tholmaim*): the same three
   sons of Anak at Hebron as the settled Num 13:22 *Achīman, Sēsæus et Thalmæus* (שֵׁשַׁי, אֲחִימַן, תַּלְמַי in both).
   Castellio's Judges forms are Greek-like (Σεσσί, Ἀχιμάν, Θολμί); the rule (one form) decides, as Numbers' call 1. Drop
   the three rows to keep his; then mark *Sēsaim* (tsere), *Ahīmanem*, *Tholmaim*.
3. **The Kenites: *Cenæus, Cenæī, Cenæīs, Cenis*** with C unmarked, as the settled *Cenæus* (Num 24:22) and *Cenæōs*
   (Gen 15:19, Num 24:21), though the Hebrew קֵינִי has tsere-yod (the settled form beats it). The preview had *Cēnæī*
   (4:17, 5:24) and, at 1:16, ***Cēnīs*** from *cēna*: that word is the Kenite's genitive (*Cenis … soceri Mosis filii*,
   "the sons of the Kenite, Moses' father-in-law"), so *Cenis*.
4. **Chemosh: *Chamōssus*** (11:24; 1738 *Chamosus*): the settled Num 21:29 *Chamōssī* (the same god, כְּמוֹשׁ, Greek
   Χαμώς). One spelling row (s → ss). Drop it to keep *Chamōsus* (ō by the Greek).
5. **Jabbok: *Jabbōc*** (11:13, 11:22; 1738 *Jaboc*, indeclinable): settled *Jabbōcum* (Num 21:24, Deut 3:16), Deut's
   call 7 the same. Two spelling rows.
6. **Jahaz: *Jāsam*** (11:20; draft *Iazam*): the same place and battle as the settled Num 21:23 *Jāsam* (Deut 2:32
   *Jāsā*; יַהְצָה). Not the settled *Jazēr* (Jazer, Num 21:32), which is another town. One spelling row.
7. **Shechem's tower: *Sichimōrum*** (9:46, 9:47, 9:49, *turris Sichimorum*): a neuter plural *Sichima, -ōrum*
   (Greek Σίκιμα) beside Judges' own *Sichemam, Sichemæ* (the settled *Sichem-*). Kept as spelled: respelling to
   *Sichemōrum* would make a form found nowhere, and *Sichemæ* would change the case. Say if you want one of them.
8. **Gilead's people, 12:4 *Galaadītīs*** ×2: the preview took the settled region *Galaadītis* (nominative, Deut 3:10),
   but here it is *Galaadīta*'s ablative and dative plural (*congregatis omnibus Galaaditis*; *qui Galaaditis
   objiciebant*), so -īs. Likewise 18:1 *Dania tribus* (nominative) and 18:12 ***Castra Dania*** (neuter plural, the
   place Mahaneh-dan), not the preview's *Daniā*; and the eight nominatives *Jephtha* (the preview's *Jephthā* follows
   the settled Heb 11:32, an ablative). 10:1 *Thōla* (nominative) the same against the settled ablative *Thōlā*.
9. **Inconsistent within Judges, one spelling**: 1:27 *Maggedonenses* → *Mageddonenses* (5:19 *Mageddonias*; Hebrew
   מְגִדּוֹ doubles the d; Gaffiot *Măgeddō*); 5:19 *Thanacum* → *Thanachum* (1:27; Hebrew כ, as Castellio writes it
   elsewhere); 18:11 *Cariathiarimum* → *Cariathjarimum* (18:12; the j-rule's form). Not inconsistent, though the brief
   asked: *Estaol, Estaole, Estaolque* are already one spelling in the draft (stage 2 put 1738's *Estaol* at 13:25), and
   *Gabaa, Gabaæ, Gabaam* are the cases of one first-declension word (Gabaæ locative or genitive; 20:21, 20:25
   *Gabaā* ablative).
10. **Kept as 1738 spells them, though the settled has a near form**: *Palæstīnī* is already the settled form
    (Gen 10:14, 21:32, Exod 13:17, 15:14), so no change; *Jābēnsēs, Jābis* (Jabesh; no settled form; Wiktionary
    *Iābēs*); *Silūns, -ūntis* for Shiloh (no settled form; marked as the settled *Hierichūntis*, Greek Σηλώ ω);
    *Lebnæ* (21:19 Lebonah, לְבוֹנָה) is not the settled *Lebnā* (Libnah, Num 33:20); *Socōthēnsēs* (Succoth in Gilead,
    marked as the settled *Sochōthis*, Succoth in Egypt, spelling kept: another place); *Cenezī* (Kenaz, Caleb's
    brother) kept against the settled Edomite *Cenazus* (Gen 36:11): another man, and the settled *Cenezeō* (Num 32:12)
    has Judges' vowel; *Ēlōn* the judge marked as the settled *Ēlōne* (Gen 46:14), another man of the same Hebrew name.
11. **Settled forms followed against the Hebrew or dictionary** (not changed in settled text): *Benjamīt-* with the a
    unmarked (settled Deut 27:12, Num 7, Rom 11:1), against the founder's *Benjāmīn*; *Abimelech-, Barac-, Gaal-* left
    unmarked (settled *Abimelechus* Gen 20, *Baracō* Heb 11:32); *Lūza, Lūzamque* (1:22, 1:26) follow the settled
    *Lūzam, Lūzæ* and the Hebrew shureq, so the settled Gen 28:19 *Luza* is the slip (not changed here);
    *Bēthlehemā* (6 ablatives) follows the settled *Bēthlehema, Bēthlehemā*, not the preview's *Bēthlehēma*.
12. **Hebrew-only marks on long compounds** (no settled, Gaffiot or Greek evidence): *Ābēlmehōlæ* (7:22),
    *Chūsanrasāthaimō/-um* (3:8, 3:10: ā for the qamets of רִשְׁעָתַיִם), *Serērātham* (7:22), *Cariathsēpher* (1:11,
    1:12), *Adōnībezecum* (Greek ω, Hebrew hireq-yod), *Estāōl*, *Bēthanāthēnsēs*. They follow Deuteronomy's
    *Dīzāhābum*; if you would rather leave Hebrew-only compounds unmarked, these are the rows to drop.

## Noticed, not names

- **6:24 *Pacii ovium*** (1738 *Paciiouium*, one word; 1750 *Pacii ouium*), the altar's name: capitalized but not a name
  and hard to construe; left to the reader of chapter 6 (no forms row).
- **8:27 *Ēphōdum*** is capitalized in the preview (the common noun, lower case at 17:5, 18:14): for the reader of
  chapter 8. **21:19 *JOvae*** in the draft is a capital-O slip, given a spelling row here.
- *Māxilla, Māxillam* (15:9, 15:14, 15:19: Lehi, Castellio's Latin for it) kept as the Latin word; *Chananaica* (3:1)
  left unmarked (no source); *Pacii*, *Castra* not names.

## Settled forms that disagree (not changed: settled text is never rewritten)

- *Luza* (Gen 28:19) against *Lūzam, Lūzæ*; *Jabbocī* against *Jabbōcī* (Deut's note). *Bēthlehema* ×3 and
  *Bēthlehemā* differ only by case; *Jephthā* (Heb 11:32) is right as an ablative.

## Decisions

| Person / place / people | Hebrew · Greek | In Judges (preview) | Decided | Reason |
|---|---|---|---|---|
| Joshua | יְהוֹשֻׁעַ | *Jōsua, Jōsuæ* | kept | settled |
| Jova | | *Jōva, Jōvæ, Jōvam*; *JŌvæ* 21.19 | *Jōvæ* (spelling change JOvae) | settled |
| Moses, Aaron, Eleazar, Phinehas | | *Mōsis, Mōsem, Aharōnis, Eleāzarī, Phīnees* | kept | settled |
| Israel; Israelites; Israelitish | | *Isrāēl-, Isrāēlīt-, Isrāēlītic-* | kept | settled |
| Judah; Judaeans; Judaea; Judaic | | *Jūdæ-, Jūdaicī* | kept | settled |
| Simeonites | שִׁמְעוֹן | *Simeonios* 1.3, *Simeoniis* 1.17 | *Simeōniōs, Simeōniīs* | settled *Simeōniī* |
| Caleb | כָּלֵב · Χάλεβ | *Chalebus, -ī, -ō* 1.12–20, 3.9 | *Calebus, Calebī, Calebō* (spelling) | settled (hard call 1) |
| Achsah | עַכְסָה · Ἀσχά | *Axam* 1.12, 1.13 | kept | Hebrew patah |
| Othniel | עָתְנִיאֵל · Γοθονιήλ | *Othoniel* 1.13; *Othoniele* 3.9, 3.11 | *Othonīēl, Othonīēle* | Greek η, Hebrew hireq-yod (as settled *Nahalīēl*) |
| Kenaz | קְנַז · Κενέζ | *Cenezi* 1.13, 3.9, 3.11 | *Cenezī* | settled *Cenezeō*; genitive (hard call 10) |
| Kenites | קֵינִי · Κιναῖος | *Cēnīs* 1.16; *Cenæus, Cenæis* 4.11; *Cēnæī* 4.17 ×2, 5.24 | *Cenis, Cenæīs, Cenæī* | settled *Cenæus* (hard call 3) |
| Adoni-bezek | אֲדֹנִי־בֶזֶק · Ἀδωνιβεζέκ | *Adonibezecum* 1.5, 1.6 | *Adōnībezecum* | Greek ω, Hebrew hireq-yod |
| Bezek | בֶּזֶק | *Bezec* 1.4, 1.5 | kept | Hebrew segol |
| Jerusalem; Jebus; Jebusites | יְבוּס | *Hierosolym-*; *Jebusam* 19.10, 19.11; *Jebusæi* 1.21; *Jebūsæ-* | *Jebūsam, Jebūsæī* | settled *Jebūsem, Jebūsæus* |
| Hierosolymites | | *Hierosolymītānōs* 1.21 | kept | W, M |
| Hebron; Kiriath-arba | | *Hebrōn-*; *Cariatharba* 1.10 | kept | settled |
| Sheshai, Ahiman, Talmai | שֵׁשַׁי, אֲחִימַן, תַּלְמַי | *Sesaim, Ahimanem, Tholmaim* 1.10 | *Sēsæum, Achīmanem, Thalmæum* (spelling) | settled Num 13:22 (hard call 2) |
| Debir; Kiriath-sepher | דְּבִיר; קִרְיַת־סֵפֶר | *Dabiris* 1.11; *Cariathsepher* 1.11, 1.12 | *Dabīris, Cariathsēpher* | Hebrew hireq-yod, tsere |
| Arad | עֲרָד | *Aradī* 1.16 | kept | settled *Aradus* unmarked |
| Zephath; Hormah | צְפַת; חָרְמָה | *Sephati* 1.17; *Hormam(que)* 1.17, 4.5 | *Sephatī* | genitive; settled *Hormam* |
| Gaza; Gazites | עַזָּה | *Gāzam*; *Gazenses* 16.2 | *Gāzēnsēs* | settled *Gāzam* |
| Ashkelon | אַשְׁקְלוֹן | *Ascalōnem* | kept | W *Ascalōn* |
| Ekron | עֶקְרוֹן · Ἀκκαρών | *Accaronem* 1.18 | *Accarōnem* | Greek ω |
| Bethel; Luz | | *Bēthēl-*; *Luza* 1.22, *Luzamque* 1.26 | *Lūza, Lūzamque* | settled *Lūzam, Lūzæ* (hard call 11) |
| Joseph; Josephites | | *Jōsēphī*; *Josephæis* 1.35 | *Jōsēphæīs* | settled *Jōsēphus*; -æus |
| Hittites, Hivites, Amorites | | *Hettæ-, Hevæ-, Amorræ-*; *Amorrhæōrum* 1.36 | *Amorræōrum* (spelling) | settled |
| Canaanites; Canaan | | *Chananæi* 1.27, 1.29, 1.30; *Chananæos* 1.29, 1.33; *Chananæā*; *Chananaica* 3.1 | *Chananæī, Chananæōs*; *Chananaica* kept | settled |
| Perizzites | הַפְּרִזִּי | *Pheresæos* 1.4; *Pherezæōs* 1.5, 3.5 | *Pherezæōs* (spelling) | settled |
| Manasseh's men | | *Manassenses(que), -ibus*; *Manassēnsium* 6.15 | *Manassēnsēs(que), Manassēnsibus* | settled |
| Beth-shean, Taanach, Dor, Ibleam, Megiddo | שְׁאָן; תַּעְנַךְ; מְגִדּוֹ | *Bethsanem, Thanachum* 1.27, *Thanacum* 5.19, *Dōriōs, Jeblamenses, Maggedonenses* 1.27, *Mageddonias* 5.19 | *Bēthsānem, Thanachum* (spelling 5.19), *Mageddōnēnsēs* (spelling), *Mageddōniās*; *Jeblamenses* kept | Hebrew qamets; Gaffiot *Măgeddō* (hard call 9) |
| Ephraim; Ephraimites | | *Ephrāim-, Ephrāimīt-*; *Ephrāimītica* 12.15 | *Ephrāimīticā* (ablative) | settled |
| Ephrathite | אֶפְרָתִי · Ἐφραθίτης | *Ephratæi* 12.5 | *Ephrātæī* | settled *Ephrāta* |
| Gezer; Gezerites | גֶּזֶר | *Gazeræ* 1.29; *Gazerenses* | *Gazerēnsēs* | Hebrew segol |
| Zebulun; Zebulunites | זְבוּלֻן | *Zabulōne*; *Zabulōniī/-īs*; *Zabulonios* 6.35, *Zabulonius* 12.11, *Zabulonia* 12.12 | *Zabulōniōs, Zabulōnius, Zabulōniā* | settled |
| Kitron; Nahalol | קִטְרוֹן; נַהֲלֹל | *Cetronenses, Nahalolenses* 1.30 | *Cetrōnēnsēs, Nahalōlēnsēs* | Hebrew holem |
| Asher; Asherites | אָשֵׁר | *Āsēriānī*; *Aserianos* 6.35; *Aserianisque* 7.23 | *Āsēriānōs, Āsēriānīsque* | settled |
| Acco, Sidon, Ahlab, Achzib, Helbah, Aphik, Rehob | | *Acconenses, Sīdoniōs, Ahalabenses, Axibenses, Helbanos, Aphecenses, Rohobenses* 1.31 | *Accōnēnsēs, Sīdōniōs, Ahalābēnsēs, Axībēnsēs, Helbānōs, Aphecēnsēs, Rohōbēnsēs* | Gaffiot *Accō*; settled *Sīdōni-, Rohōb*; Hebrew qamets, hireq-yod |
| Sidonians | צִידֹנִים | *Sīdōniī/-īs*; *Sīdoniōrum* 10.6, 18.7 | *Sīdōniōrum* | settled |
| Naphtali's men | | *Nephthālēnsēs, -ibus*; *Nephthalensium* 4.6 | *Nephthālēnsium* | settled |
| Beth-shemesh, Beth-anath | שֶׁמֶשׁ; עֲנָת | *Bethsemenses* ×2, *Bethanathenses(que)* 1.33 | *Bēthsemēnsēs, Bēthanāthēnsēs(que)* | settled *Bēth-*; Hebrew |
| Danites; Dan | הַדָּנִי | *Danios* 1.34; *Daniī*; *Daniis* 13.25, 18.16, 18.22, 20.1; *Daniæ*; *Daniā* 18.1, 18.11, 18.12; *Danemque, Danis* 18.29 | *Daniōs, Daniīs*; *Dania* 18.1, 18.12 | settled *Daniī, Daniæ, Danem, Danis* (hard call 8) |
| Heres, Aijalon, Shaalbim | חֶרֶס; אַיָּלוֹן; שַׁעַלְבִים | *Harem, Ajalonem, Salebim* 1.35; *Ajalone* 12.12 | *Ajalōnem, Ajalōne, Salebīm* | Hebrew holem, hireq-yod |
| Gilgal; Bochim | הַבֹּכִים | *Galgalīs* 2.1, *Galgala* 3.18; *Bochos* 2.1, 2.5 | *Bōchōs* | settled *Galgala*; Hebrew holem |
| Egypt; Egyptians | | *Ægypt-* | kept | settled |
| Timnath-heres; Gaash | גָּעַשׁ | *Themnathare* 2.9; *Gaasi* 2.9 | *Gāasī* | Hebrew qamets |
| Baal, Baalim; Ashtaroth | בַּעַל; עַשְׁתָּרוֹת | *Baal, Baalem, Baales(que), Baalibus, Baalis, Baaliam*; *Astarothum, Astarotho* | *Astarōthum, Astarōthō* | settled *Baalis, Astarōtha* |
| Baal-berith; El-berith | בְּרִית | *Baalberithum* 8.33, *Baalberithi* 9.4, *Berithi* 9.46 | *Baalberīthum, Baalberīthī, Berīthī* | Hebrew hireq-yod |
| Baal-hermon; Hamath; Lebanon | | *Baalhermone, Hemātham, Libanī* 3.3 | *Baalhermōne* | settled *Hermōn, Hemātham*; Gaffiot *Lĭbănus* |
| Baal-tamar | תָּמָר | *Baalthamar* 20.33 | *Baalthāmār* | settled *Thāmār* |
| Cushan-rishathaim; Mesopotamia | כּוּשַׁן רִשְׁעָתַיִם | *Chusanrasathaimo/-um* 3.8, 3.10; *Mesopotamiæ* | *Chūsanrasāthaimō/-um* | Hebrew (hard call 12) |
| Eglon; Moabites | עֶגְלוֹן · Ἐγλώμ | *Eglonem, Egloni*; *Mōabīt-*; *Mōabītidis* 11.18 | *Eglōnem, Eglōnī* | Greek ω; settled; Gaffiot *Mōăbītis* |
| Ammonites, Amalekites | | *Ammonīt-, Amālēchīt-*; *Amalechitæque* 7.12 | *Amālēchītæque* | settled |
| Ehud; Gera; Benjamite | אֵהוּד · Ἀώδ; גֵּרָא · Γηρά; יְמִינִי | *Aodus, -um, -o*; *Geræ* 3.15; *Jeminis* 3.15, *Jemine* 19.16 | *Aōdus, Aōdum, Aōdō, Gēræ, Jemīnis, Jemīne* | Greek ω, η; settled *Gēram*; Hebrew hireq-yod |
| Benjamites | | *Benjamīt-*; *Benjamita* 5.14, *Benjamiticum* 21.21 | *Benjamīta, Benjamīticum* | settled (hard call 11) |
| Seirah; Jordan | | *Seiratham* 3.26; *Jordān-* | kept | settled *Seir, Jordān-* |
| Shamgar; Anath | שַׁמְגַּר; עֲנָת | *Samgar(is)*; *Anathi* 3.31, 5.6 | *Anāthī* | Hebrew qamets |
| Philistines | פְּלִשְׁתִּים | *Palæstīn-* | kept | settled Gen 10:14, Exod 13:17 (hard call 10) |
| Jabin; of Jabin | יָבִין · Ἰαβίν | *Jabini* 4.2, *Jabinii* 4.7, *Jabinem* 4.17, *Jabine* 4.23 | *Jābīnī, Jābīniī, Jābīnem, Jābīne* | Hebrew qamets, hireq-yod |
| Hazor; Harosheth of the nations | חָצוֹר · Ἀσώρ; חֲרֹשֶׁת · Ἀρισώθ | *Hasore, Hasoris*; *Harosethi/-o/-um*; *Gojōrum* | *Hāsōre, Hāsōris, Harōsethī/-ō/-um* | Greek ω, Hebrew qamets, holem; settled *Gojōrum* |
| Sisera | סִיסְרָא | *Sisara, -æ, -am*; 5.20 ablative | *Sīsara, Sīsaræ, Sīsaram, Sīsarā* | Hebrew hireq-yod |
| Deborah | דְּבוֹרָה · Δεββῶρα | *Dēbora, Dēboræ*; ablatives 4.10, 5.15 | *Dēborā* (4.10, 5.15) | Gaffiot, settled *Dēbora* |
| Lappidoth | לַפִּידוֹת · Λαφιδώθ | *Lapidothi* 4.4 | *Lapīdōthī* | Greek ω, Hebrew hireq-yod |
| Barak; Abinoam | אֲבִינֹעַם | *Barac-*; *Abinoami* 4.6, 4.12, 5.1, 5.12 | *Abīnōamī* | settled *Baracō*; Hebrew |
| Kedesh | קֶדֶשׁ · Κάδης | *Cedesa, Cedesam* | kept | Hebrew segol |
| Tabor | תָּבוֹר · Θαβώρ | *Thabore, Thaborem* | *Thabōre, Thabōrem* | Greek ω |
| Kishon | קִישׁוֹן · Κισῶν | *Cison, Cisonem* | *Cisōn, Cisōnem* | Greek ω (Wiktionary bare i) |
| Heber; Hobab; Zaanannim | חֶבֶר; חֹבָב | *Heber, Hebris*; *Hobabi* 4.11; *Sennimo* 4.11 | *Hōbābī, Sennimō* | settled *Heber, Hōbābō* |
| Jael | יָעֵל · Ἰαήλ | *Jæl, Jælis* | *Jāēl, Jāēlis* | Greek η, Hebrew qamets; hiatus |
| Seir, Edom, Sinai | | *Seire, Idūmæ-, Sīnā* | kept | settled |
| Machir; Reubenites; Issacharites | | *Māchīre, Rūbēnītæ*; *Issacharianos, -is* 5.15, *-us* 10.1 | *Issāchariānōs, -īs, -us* | settled |
| Gileadites; Gilead | | *Galaaditæ, -a, -ārum, -ās, -icī, -ide, -idis*; *Galaadītis* 12.4; *Galaādō, Galaadī*; *Galaadītidem, Galaadīticīs* | *Galaadīt-*; *Galaadītīs* 12.4 | settled (hard call 8) |
| Meroz | מֵרוֹז · Μηρώζ | *Merozam, Merozenses* 5.23 | *Mērōzam, Mērōzēnsēs* | Greek η, ω |
| Midianites | | *Madiānīt-*; *Madianiticos* 8.12 | *Madiānīticōs* | settled |
| Ophrah; Joash; Abiezrites | עָפְרָה; יוֹאָשׁ; אֲבִיעֶזֶר | *Ephram, Ephræ*; *Jōā, Jōæ, Jōās*; *Abiezeriani, -is, -orum* | *Abīezeriānī, -īs, -ōrum* | Gaffiot *Joās*; Hebrew hireq-yod |
| Gideon; Jerubbaal | | *Gedeōn-*; *Jerobaal(e/is)* | kept | Gaffiot *Gĕdĕōn*; Hebrew patah |
| Jezreel | יִזְרְעֶאל · Ἰεζραέλ | *Jezrælis* 6.33 | *Jezraelis* | no long vowel; hiatus |
| Harod; Moreh | עֵין חֲרֹד | *Enharod* 7.1; *Mōre* | *Ēnharōd* | Hebrew; settled *Mōre* |
| Purah | פֻּרָה | *Phara* 7.10, 7.11 | *Pharā* | ablatives |
| Beth-shittah, Zererah, Abel-meholah, Tabbath | | *Bethsetam, Sereratham, Abelmeholæ, Tabbathum* 7.22 | *Bēthsetam, Serērātham, Ābēlmehōlæ, Tabbāthum* | Hebrew (hard call 12) |
| Beth-barah | בֵּית בָּרָה | *Bethbaram* 7.24 ×2 | *Bēthbāram* | Hebrew qamets |
| Oreb, Zeeb | עֹרֵב · Ὠρήβ; זְאֵב · Ζήβ | *Orebum, Orebi*; *Zebum, Zebi* | *Ōrēbum, Ōrēbī, Zēbum, Zēbī* | Greek ω, η |
| Succoth (Gilead) | סֻכּוֹת · Σοκχώθ | *Socothenses, -ensem, -ensibus* | *Socōthēnsēs, -ēnsem, -ēnsibus* | settled *Sochōthis* (hard call 10) |
| Penuel | פְּנוּאֵל | *Phanuēl*; *Phanuelenses, -em, -ibus* | *Phanuēlēnsēs, -ēnsem, -ēnsibus* | settled *Phanuēl* |
| Zebah, Zalmunna | זֶבַח; צַלְמֻנָּע | *Zeba(m), Salmana(m)(que)* | kept | Hebrew segol, patah |
| Karkor; Nobah; Jogbehah | קַרְקֹר; נֹבַח | *Carcore* 8.10; *Nobæ, Jegbaæ* 8.11 | *Carcōre, Nōbæ* | Hebrew holem; settled *Nōba* |
| Jether | יֶתֶר | *Jethri* 8.20 | *Jethrī* | dative |
| Ishmaelites | | *Ismælitæ* 8.24 | *Ismaēlītæ* | settled *Ismaēlītārum* |
| Abimelech; Jotham | | *Abimelech-*; *Jothamo* 9.5, 9.7, *Jōthamus* | *Jōthamō* | settled |
| Shechem; Shechemites | שְׁכֶם | *Sichem-*; *Sichemita, -æ, -ārum, -ās, -īs*; *Sichimorum* 9.46–49 | *Sichemīt-*; *Sichimōrum* | settled *Sichem-*; -īta (hard call 7) |
| Millo (Beth-millo) | מִלּוֹא · Βηθμααλώ | *Mellonia* 9.6, *Melloniamque, Melloniaque* 9.20 | *Mellōnia, Mellōniamque, Mellōniāque* | Greek ω |
| Gerizim | | *Garizim* 9.7 | *Garizīm* | settled *Garizīmō* |
| Beer | בְּאֵרָה | *Bēram* 9.21 | kept | Hebrew tsere |
| Gaal; Ebed; Zebul; Hamor | עֶבֶד; זְבֻל | *Gaal-; Obœdī; Zebul-; Hemōris* | kept | Hebrew patah; settled *Hemōr* |
| Arumah; Zalmon; Thebez | | *Rūmæ; Selmonem; Thēbēn* | *Selmōnem* | Greek Σελμών ω; Gaffiot *Thēbē* |
| Tola; Puah; Dodo; Shamir | תּוֹלָע; פּוּאָה; שָׁמִיר | *Thōlā* 10.1; *Phuæ*; *Dōdōnis*; *Samirianus* 10.1, *Samire* 10.2 | *Thōla, Phūæ, Sāmīriānus, Sāmīre* | settled *Phūa*; Hebrew |
| Jair; Havvoth-jair; Kamon | יָאִיר; קָמוֹן | *Jāīr, Jaīre, Jairis*; *Camōne* | *Jāīre, Jāīris, Cāmōne* | settled *Jāīr*; Hebrew qamets |
| Syrians, Maonites | מָעוֹן | *Syrōrum*; *Maoniis* 10.12 | *Maōniīs* | Gaffiot; Hebrew holem |
| Mizpah | | *Maspha* 11.30, *Maspham* | *Masphā* (ablative) | settled *Maspha* |
| Jephthah | יִפְתָּח | *Jephthā* ×8, *Jephthæ, Jephtham* | *Jephtha* (nominatives) | first declension (hard call 8) |
| Tob | טוֹב · Τώβ | *Toba* 11.2, 11.5 | *Tōbā* | Greek ω; ablative |
| Arnon, Aroer, Heshbon, Sihon, Balak, Zippor, Kadesh | | *Arnōn-, Arōēr-, Hesebōn-, Sēhōn-, Balacō, Sephōris, Cadem, Cade* | kept | settled |
| Jabbok | יַבֹּק | *Jaboc* 11.13, 11.22 | *Jabbōc* (spelling) | settled (hard call 5) |
| Jahaz | יַהְצָה | *Jazam* 11.20 | *Jāsam* (spelling) | settled (hard call 6) |
| Chemosh | כְּמוֹשׁ · Χαμώς | *Chamosus* 11.24 | *Chamōssus* (spelling) | settled (hard call 4) |
| Minnith | מִנִּית | *Minnith* 11.33 | *Minnīth* | Hebrew hireq-yod |
| Shibboleth, Sibboleth | שִׁבֹּלֶת | *Schibbolet, Sibbolet* 12.6 | *Schibbōlet, Sibbōlet* | Hebrew holem |
| Ibzan; Bethlehem | אִבְצָן | *Abesan* 12.8; *Bēthlehēma* ×6, *Bēthlehemæ, -am* | *Abesān, Bēthlehemā* | Hebrew qamets; settled (hard call 11) |
| Elon | אֵילוֹן | *Elon* 12.11 | *Ēlōn* | settled *Ēlōne* |
| Abdon; Hillel; Pirathon | עַבְדּוֹן; הִלֵּל · Ἑλλήλ | *Abdon, Hellelis, Pharathonita* 12.13, *Pharathone* 12.15 | *Abdōn, Hellēlis, Pharathōnīta, Pharathōne* | Greek ω, η; Gaffiot *Pharathōn* |
| Zorah; Eshtaol | צָרְעָה; אֶשְׁתָּאֹל | *Saraa, Saraam*; *Estaol(e/que)* | *Saraā* (ablatives 13.2, 18.2, 18.11); *Estāōl, Estāōle, Estāōlque* | Hebrew qamets, holem |
| Manoah | מָנוֹחַ · Μανωέ | *Manoa, Manoæ* | *Manōa, Manōæ*; *Manōā* 13.9, 13.19 #2 | Greek ω |
| Samson | | *Samsōn-* | kept | Gaffiot |
| Timnah; Timnite | תִּמְנָתָה | *Thamnatham, Thamnathæ, Thamnathensis* | *Thamnātham, Thamnāthæ, Thamnāthēnsis* | Hebrew qamets |
| Etam | עֵיטָם · Ἠτάμ | *Etamum* 15.8, 15.11 | *Ētāmum* | Greek η |
| Lehi | לֶחִי | *Māxillam, Māxilla* | kept | Latin |
| Sorek; Delilah; Dagon | שֹׂרֵק; דְּלִילָה | *Sorec*; *Dalila(m)*; *Dagoni* | *Sōrēc, Dagōnī* | Hebrew; Gaffiot *Dalila, Dagōn* |
| Micah | מִיכָה | *Micha, Michæ, Micham* | *Michā* 17.9, 18.31 (ablatives) | Wiktionary *Micha* bare |
| Levite | | *Lēvīt-* | kept | settled |
| Laish; Laishites | לַיִשׁ | *Laim* 18.7, 18.27; *Lāis* 18.29; *Lajenses, Lajensem* | *Lais, Lajēnsēs, Lajēnsem* | Hebrew patah |
| Kiriath-jearim; Mahaneh-dan | קִרְיַת יְעָרִים | *Cariathiarimum* 18.11, *Cariathjarimum* 18.12; *Castra Daniā* 18.12 | *Cariathjarīmum* (spelling 18.11); *Dania* | Hebrew hireq-yod (hard call 9) |
| Beth-rehob | רְחֹב | *Bethrohobensium* 18.29 | *Bēthrohōbēnsium* | settled *Rohōb* |
| Gershom; Jonathan | | *Gersomi* 18.30; *Jonathān* | *Gērsōmī*; kept | settled *Gērsōmus*; Gaffiot *Jŏnăthās* (analog) |
| Shiloh; of Shiloh | שִׁלֹה · Σηλώ | *Silunte, Siluntem*; *Siluntias* 21.21 | *Silūnte, Silūntem, Silūntiās* | Greek ω (hard call 10) |
| Gibeah; Gibeathites | גִּבְעָה | *Gabaa(m), Gabaæ*; *Gabaanis* 20.33; *Gabænses* | *Gabaā* 20.21, 20.25; *Gabaānīs, Gabaēnsēs* | cases; hiatus (hard call 9) |
| Ramah | רָמָה | *Ramæ* 19.13 | *Rāmæ* | Hebrew qamets |
| Beersheba (men of) | | *Bersabanos* 20.1 | *Bersabānōs* | settled *Bersaba*; -ānus |
| Rimmon; Gidom | רִמּוֹן · Ῥεμμών; גִּדְעֹם | *Remmonis*; *Gedeomum* 20.45 | *Remmōnis, Gedeōmum* | Greek ω; Hebrew holem |
| Jabesh (Gilead); its people | יָבֵישׁ | *Jabis* 21.9; *Jabenses* 21.10; *Jabensibus* 21.12, 21.14 | *Jābis, Jābēnsēs, Jābēnsibus* | Wiktionary *Iābēs* |
| Canaan (land) | | *Chananæā* 21.12 | kept | settled |
| Lebonah | לְבוֹנָה | *Lebnæ* 21.19 | kept | no vowel to mark (hard call 10) |
