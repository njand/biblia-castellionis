# Joshua: one form per person, place and people (Claude, 2026-11-19)

Two names readers (N1: chapters 1–14; N2: 15–24, matched to N1's shared names), under one brief: every capitalized
word of `text/draft/JOS.usfm` and its preview, and every adjective of a people or place, grouped by stem, matched to
the Hebrew (WLC) and the Greek (Brenton), and decided as Deuteronomy's and Numbers' (`deut1-34-names.md`,
`num1-36-names.md`): the settled form first (decision 46, `data/gold/`), then Gaffiot (or an analog it gives), the
Greek's η/ω/ει, another dictionary (Wiktionary bare = short), the Hebrew vowel (decision 52); clan and gentile
adjectives with the founder's marks and the suffix's quantity (-īnus, decision 77; -iānus, -ius, -ēnsis, -īta, -æus,
-ēus).

**Outputs**: 677 forms rows (N1 207, N2 470) in `data/decisions/Josh.forms.tsv`; **47 spelling changes** applied to the
draft as Apply lines in `josh1-24-stage2.md` §"Names" (N1 13, N2 33, and 12:17 *Thaphuae → Taphuae*, Tappuah, set by
Claude when the halves were matched). After them no name in Joshua is flagged `unknown`.

**Matched between the halves by Claude**: Tappuah one spelling (*Taphua*, T not Th; 12:17 respelled). **Left as
Castellio spells them**, hard calls for Nathan: Jokneam (12:22 *Jachanānæ*; 19:11, 21:34 *Jeconām*, N2 having made 21:34
*Jecanam* one with 19:11) and Taanach (12:21 *Thenacī*, 17:11 *Tanacēnsēs*, 21:25 *Thanach*): one spelling would need
case forms Castellio never prints.

---

# Joshua 1–14: one form per person, place and people (reader N1, Claude, 2026-11-19)

Every capitalized word of the proposal for Joshua 1–14 (the current `text/draft/JOS.usfm`, re-versified after the preview:
10:34–43 moved by one verse) and every adjective of a people or place, matched to the Hebrew (WLC) and Greek (Brenton),
decided as Numbers and Deuteronomy were: the settled form first (`data/gold/`), then Gaffiot (an unmarked headword
decides nothing), the Greek's η/ω/ει, another dictionary (Wiktionary bare = short), the Hebrew vowel; endings by case.

**Outputs**: `n1.forms.tsv` (207 rows) and `n1.spelling.tsv` (13 rows, each `old` checked to occur once in its verse).
`python check.py n1 1-12` and `n1 13-14`: no ERROR. The 13 forms rows for respelled words (*Sittīmō* 2:1, 3:1;
*Semerōnis* 11:1; *Salcham* 12:5, 13:11; *maachātæōs* 12:5, *maachātæōsque* 13:11, *Maachātæīsque* 13:13; *Cedis* 12:22;
*Accarōnis* 13:3; *Jāsa*, *Cedēmōtha* 13:18; *Bēthphegōr* 13:20) take effect once the spelling rows are applied; tested
by applying the spelling rows to a copy of the draft in memory (all 13 verses then proposed as intended, no `unknown`
left), with the shared layout rows of 12:5, 13:3 and 13:11 left out: **those three layout rows carry the old spellings
(*Salecham*, *Maachathaeos*, *Acharonis*) and must be respelled with them.**
The shared `data/decisions/Josh.forms.tsv` already had the case calls for *Jōvā/Jōsuā* (1:11 … 14:12), *Zarānā* 7:17 and
*Mōsaicæ* 8:31; this file adds only *Jōsuā* 11:13 (*ā Jōsuā combustum*) and 14:1 (*dīvīsōribus … et Jōsuā*).

## Hard calls

1. **Shittim *Sittīmō*** (2:1, 3:1; 1738 *Setimo*, the Vulgate's *Setim*): the settled Num 25:1 *Sittīmō*, 33:49
   *Sittīmōrum* (the same Hebrew הַשִּׁטִּים). Alternative: keep *Setimo*, marked *Setīmō* (hireq-yod).
2. **Ekron *Accarōnis*** (13:3; 1738 *Acharonis*): Joshua's own *Accaron* (15:11, 15:45, 15:46, 19:43) and
   *accaronensis* in the same verse. Alternative: keep *Acharōnis*.
3. **Kedesh *Cedis*** (12:22; 1738 *Cadis*): קֶדֶשׁ is Joshua's *Cedes* (15:23, 19:37, 21:32; *Cedesam* 20:7); *Cadis*
   reads as Kadesh (קָדֵשׁ, the settled *Cadēs*), another place. The genitive *Cedis* is not printed anywhere (a declined
   form of Joshua's own spelling). Alternative: keep *Cadis*, unmarked (Hebrew segol, segol).
4. **Maacathites *maachātæōs*** (12:5, 13:11, 13:13; 1738 *maachathaeos*): the settled Deut 3:14 *Maachātis* (t).
   Alternative: keep *th*, marked *maachāthæōs* (Hebrew qamets).
5. **Kedemoth *Cedēmōtha*** (13:18; 1738 *Cedemothia*): Joshua's own 21:37 *Cedemotha* and the settled *Cedēmōthis*
   (Deut 2:26); the extra *i* read as a slip. Alternative: keep *Cedēmōthia*.
6. **Beth-peor *Bēthphegōr*** (13:20; 1738 *Bethphogor*, as the Greek Βαιθφογώρ): the settled Deut 34:6 *Bēthphegōr*
   (and *Phegōr-*, *Baalphegōre*), the same Hebrew בֵּית פְּעוֹר. Alternative: keep *Bēthphogōr*.
7. **Shimron *Semerōnis*** (11:1; 1738 *Someronis*): Joshua's own 19:15 *Semeron* (the same town) and 12:20
   *Semeromeronis*. Alternative: keep *Somerōnis*.
8. **Lachish *Lāchīs*** (10:3, 10:5, 10:23, 12:11 genitive; *Lāchīm* 10:31, *Lāchī* 10:33–35): the name's own *-īs*
   (Hebrew hireq-yod, Greek Λαχείς 10:33; 15:39 has nominative *Lachis*), the accusative *-īm* as the settled *Edreīm*,
   *Carmīm*. Alternative: genitive *Lāchis*, short, as the settled *Charmis* (genitive of Charmi), which *Zabdis* (7:1,
   7:18) does follow, since there the *-s* is only the Latin ending.
9. **Jarmuth *Jerīmōth-*** (10:3, 10:5, 10:23; *jerīmōthius* 12:11): Greek 10:3 Ἱερειμούθ ει (12:11 has Ἱεριμούθ; the
   Hebrew יַרְמוּת has no vowel for that i). Alternative: *Jerimōth-*.
10. **Lidebir *Dabiris*** (13:26, unmarked): לִדְבִר, hireq without yod, a place in Gilead, not Debir (דְּבִיר, *Dabīr-*,
    10:3–12:13); Castellio spells both *Dabir*. Alternative: *Dabīris* as Debir.
11. **Goshen in Judah *Gōsene, Gōsenem*** (10:41, 11:16; 15:51 *Gosen*): kept with one *s*; the settled *Gōssen-* is
    Goshen in Egypt, another place with the same Hebrew (גֹּשֶׁן). Alternative: respell *Gossen-* as one name.
12. **Rabbah *Rabbam*** (13:25, unmarked): kept; the settled Deut 3:11 *Rabbathæ* renders the construct רַבַּת, Joshua the
    absolute רַבָּה (Numbers' rule: where the Hebrew differs, the book keeps its form).
13. **Avvim *hevæēnsis*** (13:3): Castellio's word follows the Greek Εὐαίῳ (the Hivites), against the settled Deut 2:23
    *Aviōs* for the Avvim; kept as his rendering, marked on the settled *Hevæ-*.
14. **Small marks**: *Sārthānis* (3:16, צָרְתָן: the first qamets read as gadol; *Sarthānis* if hatuf); *Jachanānæ*
    (12:22, יָקְנֳעָם: the first qamets hatuf, short); *gāzēa* (13:3, Castellio's *-ea*, -ēus as the settled *Jācōbēus*);
    *Hajēnsēs* (men of Ai) without a mark on the *a* before consonantal *j*, as the pipeline writes *majōribus*, though
    the settled *Hāim* has ā.

## Settled forms that disagree (not changed)

- **Gen 13:18 *in Hebrōnē***: an ablative with long -e; Joshua 11:21 *ex Hebrōne* is marked short.
- **Cenezæus** (14:6, 14:14) follows the settled Gen 15:19 *Cenezæōs*; the settled Num 32:12 *Cenezeō* spells it otherwise.
- **13:30 *Bāsāna*** (nominative, the first copy) and **13:4 *Chananæa*** (nominative, *omnis terra Chananæa*), **14:4
  *Ephrāimīna*** (nominative with *tribus*): the pipeline had the settled ablatives.

## Decisions

| Person / place / people | Hebrew · Greek | In Joshua 1–14 (draft) | Decided | Source |
|---|---|---|---|---|
| Joshua; the LORD | | *Jōsua, Jōva* | *Jōsuā* 11:13, 14:1 (others in the shared file) | ablative by case |
| Rahab | רָחָב · Ῥαάβ | *Rachabae* 2.1, 2.3; *Rachaba* 6.17; *Rachabam* 6.23, 6.25 | *Rāchabæ, Rāchabā, Rāchabam* | settled *Rāchaba* (Heb 11:31) |
| Shittim | הַשִּׁטִּים · Σαττίν | *Setimo* 2.1, 3.1 | *Sittīmō* (spelling) | settled Num 25:1 (call 1) |
| beyond Jordan | | *transjordaninos* 2.10, 9.10 | *trānsjordānīnōs* | settled Mark 10:1 |
| Adam (city) | אָדָם | *Adama* 3.16 | *Ādāmā* | Hebrew qamets, qamets |
| Zarethan | צָרְתָן | *Sarthanis* 3.16 | *Sārthānis* | Hebrew qamets, qamets (call 14) |
| Gadites | | *Gadinique* 4.12 | *Gadīnīque* | settled *Gadīnī* |
| of Jericho | | *hierichuntio* 5.10, 10.28 | *hierichūntiō* | settled *Hierichūnt-* |
| Gilgal | הַגִּלְגָּל | *Galgala, Galgalis*; *galgalensia* 9.6 | *galgalēnsia* | Wiktionary *Galgala* bare; -ēnsis |
| Achan | עָכָן · Ἄχαρ | *Achan* 7.1, 7.18, 7.20; *Achanem* 7.19, 7.24 | *Āchān, Āchānem* | Gaffiot unmarked; Hebrew qamets, qamets |
| Zabdi | זַבְדִּי · Ζαμβρί | *Zabdis* 7.1, 7.18; *Zabdi* 7.18 | *Zabdis, Zabdī* | as settled *Charmis*; Hebrew hireq-yod |
| Zerahite | הַזַּרְחִי | *zarana* 7.17 | *Zarānā* (shared file) | settled *Zarāna* |
| Achor | עָכוֹר · Ἀχώρ | *Achoris* 7.24, 7.26 | *Āchōris* | Greek ω, Hebrew qamets |
| Ai; men of Ai | הָעַי · Γαί | *Haim*; *Hai* 7.2, 8.2, 8.16, 9.3, 10.2; *Hais* 8.1, 8.9, 8.14, 8.23, 12.9; *Hajens-* 7.3–8.29 | *Hāī, Hāis, Hajēnsēs …* | settled *Hāim* (Gen 12:8) |
| Beth-aven | בֵּית אָוֶן | *Bethaven* 7.2 | *Bēthāven* | *Bēth-* settled; Hebrew qamets |
| Shebarim | הַשְּׁבָרִים | *Sabarim* 7.5 | *Sabārīm* | Hebrew qamets, hireq-yod |
| Mosaic | | *mosaicae* 8.31 | *Mōsaicæ* (shared file) | settled *Mōsaicō* |
| Ebal | עֵיבָל | *Ebali* 8.33 | *Ēbālī* | settled *Ēbāle* (dative) |
| Jebusites, Perizzites, Hivites | | *Jebusaei, Pheresaei* 9.1; *Hevaeis* 9.7 | *Jebūsæī, Pherezæī, Hevæīs* | settled |
| Gibeon; Gibeonites | גִּבְעוֹן · Γαβαών | *Gabaon, Gabaonem*; *Gabaonit-* 9.3–11.18 | *Gabaōnem, Gabaōnītæ/-ās/-ārum* | Gaffiot *Găbăōn*; -īta |
| Chephirah | הַכְּפִירָה · Κεφιρά | *Caphira* 9.17 | *Caphīra* | Hebrew hireq-yod |
| Beeroth | בְּאֵרוֹת · Βηρώτ | *Berotha* 9.17 | *Bērōtha* | Greek η, ω (settled *Bērōthīs*) |
| Kiriath-jearim | קִרְיַת יְעָרִים | *Cariathjarimum* 9.17 | *Cariathjārīmum* | settled *Cariath-*; Hebrew |
| Adoni-zedek | אֲדֹנִי־צֶדֶק · Ἀδωνιβεζέκ | *Adonisedecus* 10.1 | *Adōnīsedecus* | Greek ω; Hebrew |
| Hoham, Piram, Japhia, Horam | הוֹהָם, פִּרְאָם, יָפִיעַ, הֹרָם | *Hoamum, Pharamum, Japhiam* 10.3; *Horamum* 10.33 | *Hōāmum, Pharāmum, Jāphīam, Hōrāmum* | Hebrew |
| Jarmuth | יַרְמוּת · Ἱερειμούθ | *Jerimothi* 10.3, 10.5, 10.23; *jerimothius* 12.11 | *Jerīmōthī, jerīmōthius* | Greek ει; Hebrew shureq (call 9) |
| Lachish | לָכִישׁ · Λαχείς | *Lachis, Lachim, Lachi* | *Lāchīs, Lāchīm, Lāchī* | Greek ει; Hebrew (call 8) |
| Debir | דְּבִיר · Δαβείν | *Dabirem, Dabir, Dabiri, Dabire, Dabiris* 10.3–12.13 | *Dabīr-* | Greek ει, Hebrew hireq-yod |
| Lidebir | לִדְבִר | *Dabiris* 13.26 | *Dabiris* | Hebrew hireq (call 10) |
| Eglon | עֶגְלוֹן | *Eglon-* 10.3–12.12 | *Eglōn-* | Hebrew holem |
| Azekah; Makkedah | עֲזֵקָה · Ἀζηκά; מַקֵּדָה · Μακηδά | *Azecam* 10.10–11; *Maced-* 10.10–12.16 | *Azēcam; Macēdam, Macēdā, Macēdæ* | Greek η |
| Beth-horon | בֵּית־חוֹרֹן · Ὠρωνείν | *Bethoronis* 10.10, 10.11 | *Bēthōrōnis* | Greek ω |
| Aijalon | אַיָּלוֹן · Αἰλών | *Ajalonem* 10.12 | *Ajālōnem* | Greek ω; Hebrew qamets |
| Libnah | לִבְנָה | *Lebnae* 10.29–12.15 | *Lebnæ* | settled *Lebnā* (unmarked stem) |
| Gezer; Geder | גֶּזֶר; גֶּדֶר | *Gazeris* 10.33, 12.12; *Gaderis* 12.13 | unmarked | Hebrew segol |
| Goshen (Judah) | גֹּשֶׁן | *Gosene* 10.41; *Gosenem* 11.16 | *Gōsene, Gōsenem* | Hebrew holem (call 11) |
| Jabin | יָבִין | *Jabin* 11.1 | *Jābīn* | Hebrew |
| Hazor | חָצוֹר · Ἀσώρ | *Hasoris* 11.1, 12.19; *Hasor* 11.10, 11.13 | *Hāsōr-* | Greek ω, Hebrew qamets |
| Madon | מָדוֹן · Μαρῶν | *Madonis* 11.1, 12.19 | *Mādōnis* | Greek ω, Hebrew qamets |
| Shimron; Shimron-meron | שִׁמְרוֹן · Συμοών | *Someronis* 11.1; *Semeromeronis* 12.20 | *Semerōnis* (spelling), *Semerōmerōnis* | Greek ω (call 7) |
| Achshaph | אַכְשָׁף | *Axaphi* 11.2, 12.20 | *Axāphī* | Hebrew qamets |
| Dor | דּוֹר · Δώρ | *Doris* 12.23; *dorio* 11.2, 12.23 | kept | Greek ω |
| Mizpah, Mizpeh | מִצְפָּה | *Masphae* 11.3, 11.8; *Maspham* 13.26 | unmarked | settled *Maspha* (Gen 31:49) |
| Merom | מֵרוֹם · Μαρών | *meromias* 11.5, 11.7 | *mērōmiās* | Greek ω, Hebrew tsere |
| Baal-gad | בַּעַל גָּד | *Baalgadum* 11.17; *Baalgado* 12.7, 13.5 | unmarked, *Baalgadō* | settled *Dībōngadō*, *Baalphegōre* |
| Hebron | | *Hebrone* 11.21 | *Hebrōne* | settled stem; ablative |
| Anab | עֲנָב · Ἀναβώθ | *Anabo* 11.21 | *Anābō* | Hebrew qamets |
| Anakim | | *Enaquini* 11.22 | *Enāquīnī* | settled |
| Gaza; of Gaza | עַזָּה | *Gazae* 11.22; *gazea* 13.3 | *Gāzæ, gāzēa* | settled *Gāzam* |
| Gath; of Gath | גַּת | *Gethae* 11.22; *gethensis* 13.3 | *Gethæ, gethēnsis* | Gaffiot *Geth* unmarked; Hebrew patah |
| of Ashdod, Ashkelon, Ekron | | *azotensis, ascalonensis, accaronensis* 13.3 | *azōtēnsis, ascalōnēnsis, accarōnēnsis* | Gaffiot *Azōtus*; Wiktionary *Ascalōn, Accarōnīta* |
| Ekron | עֶקְרוֹן · Ἀκκαρών | *Acharonis* 13.3 | *Accarōnis* (spelling) | Joshua's *Accaron* (call 2) |
| Avvim | הָעַוִּים · Εὐαῖος | *hevaeensis* 13.3 | *hevæēnsis* | settled *Hevæ-* (call 13) |
| Chinnereth | | *Cenerethum* 12.3 | unmarked | settled *Cenerethī* |
| Beth-jeshimoth | | *Bethiesimotha* 12.3, 13.20 | *Bēthiesimōtha* | settled Num 33:49 |
| Salecah | סַלְכָה | *Salecham* 12.5, 13.11 | *Salcham* (spelling) | settled Deut 3:10 |
| Geshurites | הַגְּשׁוּרִי | *gessuraeos* 12.5, 13.11; *Gessuraea* 13.2; *Gessuraeis* 13.13 | *Gessūr-* | settled *Gessūris* |
| Maacathites | הַמַּעֲכָתִי | *maachathaeos* 12.5 …; *Maachathaeisque* 13.13 | *maachātæ-* (spelling) | settled *Maachātis* (call 4) |
| Heshbonite | | *hesebonii* 12.5, 13.27 | *hesebōniī* | settled *Hesebōnius* |
| Arad, Hormah | | *Aradi, Hormae* 12.14 | *Aradī, Hormæ* | settled *Aradus, Hormam* |
| Adullam | עֲדֻלָּם · Ὀδολλάμ | *Adullami* 12.15 | *Adullāmī* | Hebrew qamets |
| Tappuah | תַּפּוּחַ | *Thaphuae* 12.17 | *Thaphūæ* | Hebrew shureq |
| Aphek | אֲפֵק | *Apheci* 12.18; *Aphece* 13.4 | *Aphēcī, Aphēce* | Hebrew tsere |
| Lasharon | לַשָּׁרוֹן | *Lasaronis* 12.18 | *Lasārōnis* | Hebrew qamets, holem |
| Taanach | תַּעְנַךְ | *Thenaci* 12.21 | *Thenacī* | Hebrew patah, patah |
| Megiddo | | *Mageddonis* 12.21 | *Mageddōnis* | Gaffiot *Măgeddō* |
| Kedesh | קֶדֶשׁ | *Cadis* 12.22 | *Cedis* (spelling) | Joshua's *Cedes* (call 3) |
| Jokneam | יָקְנֳעָם | *Jachananae* 12.22 | *Jachanānæ* | Hebrew (call 14) |
| Tirzah | תִּרְצָה | *Thersae* 12.24 | unmarked | settled *Thersa* |
| Shihor | שִׁיחוֹר | *Sihore* 13.2 | *Sīhōre* | Hebrew |
| Canaanite; Sidonian; Giblite | | *chananaea, sidonius* 13.4; *giblaea* 13.5 | *Chananæa, Sīdōnius, giblæa* | case; settled *Sīdōnius*; Hebrew hireq |
| Medeba | מֵידְבָא · Μαιδαβάν | *Medabae* 13.9; *medabanus* 13.16 | *Mēdabæ, mēdabānus* | Gaffiot unmarked; Hebrew tsere-yod |
| Dibon | | *Dibon* 13.17 | *Dībōn* | settled *Dībōnem* |
| Bamoth-baal; Beth-baal-meon | בָמוֹת בַּעַל; בֵית בַּעַל מְעוֹן | *Bamothbaal, Bethbaal, Meon* 13.17 | *Bāmōthbaal, Bēthbaal, Meōn* | settled *Bāmōtha, Baalmeōnem* |
| Jahaz | יַהְצָה | *Jassa* 13.18 | *Jāsa* (spelling) | settled *Jāsam*; Joshua 21:36 *Jasa* |
| Kedemoth | קְדֵמֹת | *Cedemothia* 13.18 | *Cedēmōtha* (spelling) | settled *Cedēmōthis* (call 5) |
| Mephaath | מֵפָעַת | *Mephaatha* 13.18 | *Mēphāatha* | Hebrew tsere, qamets |
| Kiriathaim; Sibmah; Zereth-shahar | | *Cariathaimum, Sabama, Sarathasar* 13.19 | *Cariāthaimum*, unmarked, unmarked | settled *Cariāthaim, Sabamam*; Hebrew |
| Beth-peor | בֵּית פְּעוֹר · Βαιθφογώρ | *Bethphogor* 13.20 | *Bēthphegōr* (spelling) | settled (call 6) |
| of Gilead | | *galaaditica* 13.25; *Galaaditidis* 13.31 | *Galaadītica, Galaadītidis* | settled |
| Rabbah | רַבָּה | *Rabbam* 13.25 | unmarked | (call 12) |
| Betonim | בְּטֹנִים | *Betonim* 13.26 | *Betōnīm* | Hebrew holem, hireq-yod |
| Mahanaim | | *Mahanaimo* 13.26, 13.30 | *Mahanaimō* | settled *Mahanaim* (unmarked) |
| Beth-haram; Beth-nimrah | בֵית הָרָם | *Betharama, Bethnemra* 13.27 | *Bēthārāma, Bēthnemra* | Hebrew; settled *Bēthnemram* |
| Zaphon | צָפוֹן | *Saphon* 13.27 | *Sāphōn* | Gaffiot *Sāphōn* |
| Bashan | | *Basana* 13.30 (first) | *Bāsāna* (nominative) | settled stem |
| Jair | | *Jairis* 13.30 | *Jāīris* | settled *Jāīr* |
| Ephraimite | | *ephraimina* 14.4 | *Ephrāimīna* (nominative) | settled stem |
| Kenizzite | | *Cenezaeus* 14.6; *Cenezaeo* 14.14 | unmarked | settled Gen 15:19 |
| Kiriath-arba; Arba | אַרְבַּע | *Cariatharba, Arba* 14.15 | unmarked, *Arbā* (ablative) | settled *Cariatharbæ* |

Kept as proposed (settled or already right): *Mōsēs, Nūnis, Jordān-, Isrāēlīt-, Hierichūnt-/Hierichō, Hettæ-, Amorræ-,
Chananæ-, Hevæ-, Jebūsæ-, Pherezæ-, Gergesæ-, Sēhōn-, Ōg-, Bāsān-, Astarōth-, Edreī(m), Hesebōn-, Arnōn-, Arōēr-,
Galaadītid-, Jabbōcum, Phasga/-æ, Hermōn-, Libanus, Seir, Sīdōn-, Euphrātem, Ægypt-, Bēthēl-, Garizīmō, Ēbāle, Charmis,
Zaræ, Jūdæ, Hierosolymæ, Hebrōn-, Gāzam, Cadēsbarnēā, Jobābum, Cenerethī, Azōtī, Carmēlō, Gojōrum, Hēphris, Palæstīnī,
Madiānītārum, Evīm, Recemum, Sūrem, Hūrem, Rebam, Balaamum, Beōris, Jazēr, Rāmōtha, Sochōtha, Māchīris, Manass-,
Rūbēnīt-, Gadīn-, Lēvīt-, Jōsēphēī, Eleāzarō, Calebus/-um/-ō, Jephonis, Enāquīn-, Mōabīticō, Cisjordānīnī, Babylōnicam.*

## Shared names (for N2)

- **Ekron**: *Accarōn-* (15:11 *Accaronis*, 15:45, 15:46, 19:43), Greek Ἀκκαρών ω, Hebrew holem.
- **Achor** *Āchōr-* (15:7); **Achan** *Āchān* (22:20); **Gibeon** *Gabaōn-* (18:25, 21:17).
- **Debir** *Dabīr-* (15:7, 15:15, 15:49, 21:15; Hebrew דְּבִר/דְּבִיר, Greek ει); Lidebir (13:26) left short.
- **Lachish** *Lāchīs* (15:39), **Eglon** *Eglōn* (15:39), **Azekah** *Azēca* (15:35), **Jarmuth** *Jerīmōth* (15:35, and 21:29,
  Jarmuth of Issachar, the same Hebrew), **Adullam** *Adullām* (15:35), **Libnah** *Lebn-* unmarked (15:42, 21:14).
- **Beth-horon** *Bēthōrōn-* (16:3, 16:5, 18:13, 18:14, 21:22); **Aijalon** *Ajālōn-* (19:42, 21:24); **Japhia** *Jāphīa*
  (19:12, the town, the same Hebrew יָפִיעַ).
- **Hazor** *Hāsōr* (15:23, 15:25, 19:36; *Hasorhadatta* 15:25); **Shimron** *Semerōn* (19:15); **Achshaph** *Axāph*
  (19:25); **Mizpeh** *Masph-* unmarked (15:38, 18:26); **Goshen** *Gōsen* (15:51); **Anab** *Anāb* (15:50).
- **Aphek/Aphekah** *Aphēc-* (15:53, 19:30); **Shihor(-libnath)** *Sīhōr* (19:26); **Gezer** *Gazer* unmarked (16:3, 21:22;
  *Gazerenses* 16:10); **Gath-hepher, Gath-rimmon** *Geth-* unmarked (19:13, 19:45, 21:24–25); **Ashdod** *Azōt-* (15:46–47).
- **Kedesh**: Joshua's *Cedes* (15:23, 19:37, 21:32; *Cedesam* 20:7); my 12:22 *Cedis* (call 3).
- **Jahaz** *Jāsa* (21:36); **Kedemoth** *Cedēmōtha* (21:37); **Mephaath** *Mēphāath* (21:37, Hebrew tsere, qamets);
  **Mahanaim** unmarked (21:38). **Jazer**: the settled *Jazēr*; 21:39 *Jaser* would be a spelling change.
- **Kiriath-jearim** *Cariathjārīm-* (15:9, 15:60 *Cariathiarim*, 18:14, 18:15); **Kiriath-arba** *Cariatharb-* unmarked
  (15:13, 15:54, 20:7, 21:11).
- **Tappuah**: my 12:17 *Thaphūæ* against 16:8 *Taphua*, 17:8 *Taphuae* (and 15:34 *Taphna*?): spelled two ways if the
  same town; I kept *Th*, for N2 to match.
- **Taanach**: Joshua spells it three ways (12:21 *Thenaci*, 17:11 *Tanacenses*, 21:25 *Thanach*): one spelling wants a
  decision; all unmarked (patah, patah).
- **Adamah** (19:36 *Adama*, אֲדָמָה) is not Adam of 3:16 (*Ādāmā*, אָדָם): same Latin spelling, different marks.
- **Carmel** *Carmēl-* (Gaffiot; 15:55, 19:26); **Dor** *Dōr-* (17:11 *Dorios*); **Tirzah** 17:3 is the settled person
  *Thersa*.

## Odd in the words

- 10:41 *omnīque terrā Gosene*: the shared rows make *terrā* ablative, as the sentence wants.
- 13:26 Greek Δαιβών for Lidebir; 12:21 the Greek has Κάδης where the Hebrew has Taanach (Brenton's order differs).
- *sumsimus* (9:12, `unknown`, not a name): left to the stage readers.

---

# Joshua 15–24: one form per person, place and people (names reader N2, Claude, 2026-11-19)

Every capitalized name and people's adjective of the proposal for Joshua 15–24 (`check.py n2 15-24`, on the draft as it stood at 04:38, with the readers' shared `data/decisions/Josh.*.tsv`) was matched to its Hebrew (WLC), Greek (Brenton) and the Vulgate, and decided as Numbers and Deuteronomy were: the settled form first (`data/gold/`), then Gaffiot (an unmarked Gaffiot headword does not stop the search, as Deuteronomy's *Garizīmō*), the Greek's η/ω/ει, another dictionary (Wiktionary bare = short), the Hebrew vowel (decision 52); adjectives take the founder's or place's marks and the suffix's quantity (-īnus, -iānus, -ius, -ēnsis, -īta, -ēus). Endings by the Latin case in each verse; a final -a of a Hebrew -āh name is the Latin nominative (short), as in Numbers.

**Outputs** (all in `s35/`): `n2.forms.tsv`, 437 rows, every one checked (`python check.py n2 15-24`: 307 verses, no ERROR); `n2.spelling.tsv`, 33 spelling changes, each `old` checked to occur once in its verse of the draft; and 33 more forms rows for the respelled words (below, and in `n2-work/n2.forms.full.tsv` with the 437), which the check cannot test before the respelling. They were tested by `s35/n2-work/n2full.py` (`python $S/s35/n2-work/n2full.py $S`, from the repo: the spelling rows applied to an in-memory copy of the draft and to the shared layout lines, all 470 rows as forms): 307 verses, no ERROR, and **no name left flagged `unknown`** in 15–24; the names still flagged are only `settled` / `homograph+settled` forms the proposal already has right. About 330 persons, places and peoples (table below).

Capitals: the layout readers' rows now give *Cedes* (15:23, 19:37), *Aman* (15:26), *Ammam* (19:30), *Adama* (19:36), *Damna* (21:35) and the peoples' adjectives (*Jūdaicæ*, *Hierichūntiō*, *Mōsaicæ*, *Phegōrium*, *Trānsjordānīnōrum* …) their capitals; nothing is left for them from the names.

## Hard calls (for Nathan)

1. **One person, the settled spelling** (Castellio spelled these men and women differently in Joshua): 15:14 *Sesaim*, *Tholmaim* → ***Sēsæum***, ***Thalmæum*** (Num 13:22 *Sēsæus*, *Thalmæus*, with *Achīman*: Joshua's indeclinable accusatives become the settled declension); 17:2 *Esriele* → ***Asrīēle*** (Num 26:31); 17:3 *Salphadus* → ***Salphaādus***, *Melcha* → ***Melca*** (Num 26:33, 27:1; Numbers' call 8); 21:12 *Chalebo* → ***Calebō***; 24:32 *Josephaeis* → ***Jōsēphēīs*** (Deut 27:12 *Jōsēphēī*, as 18:11 *Josepheos*). Alternative: Castellio's Joshua spellings stand (drop the rows; then *Sēsaim*, *Tholmaim* unmarked but for the Hebrew tsere, *Esrīēle*, *Salphadus*, *Melcha*, *Chalebō*, *Jōsēphæīs*).
2. **One place, the settled spelling**: 15:4 *Asemonem* → ***Asmōnem*** (Num 34:4); 15:30 *Harma* → ***Horma*** (Num 14:45 *Hormam*; Joshua's own 19:4 *Horma*); 18:13 *Lusae* → ***Lūzæ*** (Gen 48:3; Joshua's 16:2 *Lūzam*); 21:39 *Jaser* → ***Jazēr*** (Num 21:32, 32:3, 32:35; N1's 13:25 *Jazer*); **20:8, 21:36 *Bosor* → *Beser*** (Deut 4:43 *Beser*, the same list of the cities of refuge). *Bosor* is the Vulgate's and the Greek's form, so this one changes Castellio's most; drop the two rows to keep it (then *Bosor*, unmarked: Hebrew segol).
3. **One spelling within Joshua** (my choice first; the other spelling is the alternative): *Adommim* (18:17; 15:7 *Adumim*: the Hebrew's doubled m, the Vulgate's both times); *Hasersual* (19:3; 15:28 *Hazersual*: s for tsade as *Hasergadda*, *Hasersusa*); *Asem* (19:3; 15:29 *Ezem*: the Vulgate has *Esem*/*Asem*, the Hebrew עָצֶם pausal in both); *Ain* (19:7, 21:16; 15:32 *Aen*); ***Saraa*** (19:41; 15:33 *Sarea*: a toss-up, the Vulgate has *Sarea* and *Sara*); *Asan* (19:7; 15:42 *Assan*); *Jattir* (21:14; 15:48 *Jatthir*: tt for the dagesh); *Cariathjarim* (15:60 *Cariathiarim*: the j); *Atarothadar* (18:13; 16:5 *Atarothaddar*: as 15:3 *Adar* and the settled *Hazaradār*); *Machmetam* (16:6; 17:7 *Machmatam*); *Helcath* (21:31; 19:25 *Halcath*: Hebrew segol); *Jephthahelis* (19:14; 19:27 *Jephthaelis*); *Gebbethon* (19:44; 21:23 *Gabathonem*); ***Jeconam*** (19:11; 21:34 *Jecanam*: a toss-up, and N1's 12:22 has *Jachananae*); *Thamnathsara* (19:50; 24:30 *Thannathserae*, the same Hebrew תִּמְנַת־סֶרַח); and with N1's chapters, where theirs is the majority or the Hebrew's: 15:41 *Macceda* → *Maceda* (10:10–29, 12:16, seven times), 17:11 *Magedonenses* → *Mageddonenses* (12:21 *Mageddonis*; dagesh), 18:26 *Caphara* → *Caphira* (9:17; hireq-yod), 18:25 *Beerota* → *Berotha* (9:17; N1's *Bērōtha*, Greek Βηρώτ η, ω, the settled *Bērōthīs*).
4. **15:34 *Taphna* → *Taphua***: read as a turned u (Tappuah, תַּפּוּחַ; the Vulgate here *Taphua*, and 15:53 *Bethtaphua*, 16:8 *Taphua*). The page reads *Taphna* (stage 2, and Wikisource): if it is Castellio's own form, drop the row and mark *Taphna* unmarked.
5. **Shiloh *Sīlūnt-*** (18:1, 8, 9; 19:51; 21:2; 22:9, 12; 16:6 *Tanathsīlūntem*): Castellio declines it as *Hierichūs, -ūntis*; the Greek Σηλώ gives η and ω (decision 52's order puts it before the Hebrew שִׁלֹה hireq, holem). Alternative by the Hebrew: *Silūntem*.
6. **Kedesh *Cedēs*** (15:23, 19:37, 21:32; *Cedēsam* 20:7) by the Greek Κάδης η (15:23, 20:7, 21:32; 19:37 has Κάδες); the Hebrew קֶדֶשׁ has segol, segol. Alternative: *Cedes* unmarked. N1's 12:22 *Cadis* is the same Kedesh (Naphtali): one spelling, *Cedes* (4 to 1), is for the two halves to match.
7. **Ramah *Rāma*** (18:25, Benjamin; and *Rāmam* 19:29, *Harāma* 19:36, other Ramahs), Hebrew qamets: the settled Matt 2:18 *Ramam* (Jeremiah's Ramah, this town) is unmarked, but the OT's form governs (decision 46), so Matt 2:18 should follow (*Rāmam*; not changed here). Alternative: *Rama* unmarked, as Matthew.
8. **18:28 *Cariathaim*** unmarked: it renders קִרְיַת (Kirjath, the Vulgate's *Cariath*), not Kiriathaim (קִרְיָתַיִם, the settled Num 32:37 *Cariāthaim*, and N1's 13:19 *Cariathaimum*); the proposal took the settled *Cariāthaim*. Alternative: keep *Cariāthaim* (one Latin word, one marking).
9. **Gaza *Gāza*** (15:47) as the settled Gen 10:19, Deut 2:23 *Gāzam*, against Gaffiot *Găza*: the settled form first; if Gaffiot should win, those two settled words change.
10. **Achan *Āchān*** (22:20; N1's 7:1–24): Gaffiot has *Achan* unmarked, which (as Deuteronomy's *Garizim*) does not stop the search; Hebrew עָכָן qamets, qamets. Alternative: *Achan* unmarked by Gaffiot. **Achor *Āchōris*** (15:7; N1's 7:24, 26) likewise (Hebrew qamets, holem; Greek ω).
11. **Castellio's vowel against the Hebrew's**: where his letter differs from the Hebrew vowel, the Hebrew's quantity is marked on his letter: *Bēthphēlet* (פָּלֶט qamets), *Cheselēthābōris* (כִּסְלֹת holem), *Jeconām*, *Sārōhen* (shureq), *Jōta* (Juttah, shureq), *Hūcūca*, *Nahalōl* (qamets), *Bālōth* (בְּעָלוֹת: the qamets of ʿā). *Allōne* (19:33) keeps the preview's ō: Castellio's *Allon* is the older text's אַלּוֹן (KJV *Allon*), not the WLC's אֵלוֹן.
12. **Kept as printed** (not respelled): *Engannin* (15:34, a town of Judah) beside *Engannim* (19:21, 21:29, Issachar): two towns, and Castellio writes -in and -im freely (*Selin* for Shilhim, *Selebim* for Shaalabbin); *Jabneel* (15:11, Judah) and *Jabnel* (19:33, Naphtali): two towns; *Ensemen* (18:17, accusative) beside *Ensemis* (15:7): perhaps a misprint for *Ensemem*, but not an extra or missing letter, so left (*Ēnsemen*); *Iiim* (15:29, עִיִּים, the Vulgate *Jim*) as printed, *Iiīm*; *Cedesam* (20:7) beside *Cedes*; *Thamnatha* (19:43) beside the settled *Thamnam*; *Gaulon* (the city, Γαυλών) beside the settled *Gaulānītidem* (Deut 4:43, the region); *Hedrei* (19:37, Edrei in Naphtali) beside the settled *Edreī* (Edrei of Bashan); *Hemath* (19:35, Hammath חַמַּת, unmarked) is not Hamath (the settled *Hemātham*); *Ebron* (19:28, עֶבְרֹן) is not Hebron; *Duma* (15:52) is marked *Dūma* by the Hebrew shureq, though the settled Gen 25:14 *Duma* (Ishmael's son) is unmarked; *Sarāim* (15:36, Sharaim) loses the ā the proposal took from the settled *Sarāim* (Sarai).

## Forms rows for the respelled words

These 33 rows belong in the forms file once `n2.spelling.tsv` is applied (tested as above):

```
Josh.15.4	Asmōnem	Azmon, settled Num 34:4 *Asmōnem* (after the spelling change) (Claude, 2026-11-19)
Josh.15.7	Adommīm	Adummim, Hebrew אֲדֻמִּים: hireq-yod; spelled as 18:17 *Adommim* (after the spelling change) (Claude, 2026-11-19)
Josh.15.14	Sēsæum	Sheshai, settled Num 13:22 *Sēsæus*, accusative (after the spelling change) (Claude, 2026-11-19)
Josh.15.14	Thalmæum	Talmai, settled Num 13:22 *Thalmæus*, accusative (after the spelling change) (Claude, 2026-11-19)
Josh.15.28	Hasersūāl	Hazar-shual: as 19:3 *Hasersūāl* (after the spelling change) (Claude, 2026-11-19)
Josh.15.29	Āsem	Azem: as 19:3 *Āsem* (after the spelling change) (Claude, 2026-11-19)
Josh.15.30	Horma	Hormah, settled Num 14:45 *Hormam* (after the spelling change) (Claude, 2026-11-19)
Josh.15.32	Ain	Ain: as 19:7, 21:16 *Ain* (after the spelling change); settled Num 34:11 *Ainis* (unmarked) (Claude, 2026-11-19)
Josh.15.33	Sāraa	Zorah: as 19:41 *Sāraa* (after the spelling change) (Claude, 2026-11-19)
Josh.15.34	Taphūa	Tappuah: 1738's *Taphna* is a turned u (Vulgate *Taphua*), after the spelling change; Hebrew תַּפּוּחַ: patah, shureq (Claude, 2026-11-19)
Josh.15.41	Macēda	Makkedah, Hebrew מַקֵּדָה: patah, tsere; nominative -a (after the spelling change, as 10:10–29, 12:16 *Maceda*) (Claude, 2026-11-19)
Josh.15.42	Āsān	Ashan: as 19:7 *Āsān* (after the spelling change) (Claude, 2026-11-19)
Josh.15.48	Jattīr	Jattir: as 21:14 *Jattir* (after the spelling change); Hebrew וְיַתִּיר: patah, hireq-yod (Claude, 2026-11-19)
Josh.15.60	Cariathjārīm	Kirjath-jearim: as 15:9 *Cariathjārīmum* (after the spelling change, j as 15:9, 18:14, 18:15) (Claude, 2026-11-19)
Josh.16.5	Atarōthadār	Ataroth-addar: as 18:13 *Atarōthadār* (after the spelling change) (Claude, 2026-11-19)
Josh.17.2	Asrīēle	Asriel, settled Num 26:31 *Asrīēl* (after the spelling change) (Claude, 2026-11-19)
Josh.17.3	Salphaādus	Zelophehad, settled Num 26:33 *Salphaādus* (after the spelling change) (Claude, 2026-11-19)
Josh.17.3	Melca	Milcah, settled Num 26:33, 27:1 *Melca* (after the spelling change) (Claude, 2026-11-19)
Josh.17.7	Machmetam	Michmethah: as 16:6 *Machmetam* (after the spelling change) (Claude, 2026-11-19)
Josh.17.11	Mageddōnēnsēs	the men of Megiddo, Hebrew מְגִדּוֹ: shewa, hireq, holem; -ēnsis (after the spelling change, dd as 12:21 *Mageddonis*) (Claude, 2026-11-19)
Josh.18.13	Lūzæ	Luz, settled Gen 48:3 *Lūzæ* (after the spelling change) (Claude, 2026-11-19)
Josh.18.25	Bērōtha	Beeroth: as N1's 9:17 *Bērōtha* (Greek Βηρώτ η, ω; the settled *Bērōthīs*) (after the spelling change) (Claude, 2026-11-19)
Josh.18.26	Caphīra	Chephirah, Hebrew הַכְּפִירָה: shewa, hireq-yod (after the spelling change, as 9:17 *Caphira*) (Claude, 2026-11-19)
Josh.19.25	Helcath	Helkath: as 21:31 *Helcath* (after the spelling change) (Claude, 2026-11-19)
Josh.19.27	Jephthahēlis	Jiphthah-el: as 19:14 *Jephthahēlis* (after the spelling change) (Claude, 2026-11-19)
Josh.20.8	Beser	Bezer, settled Deut 4:43 *Beser* (after the spelling change) (Claude, 2026-11-19)
Josh.21.12	Calebō	Caleb, settled Num 14:30 *Calebō* (after the spelling change) (Claude, 2026-11-19)
Josh.21.23	Gebbethōnem	Gibbethon: as 19:44 *Gebbethōn* (after the spelling change) (Claude, 2026-11-19)
Josh.21.34	Jeconām	Jokneam: as 19:11 *Jeconām* (after the spelling change) (Claude, 2026-11-19)
Josh.21.36	Beser	Bezer, settled Deut 4:43 *Beser* (after the spelling change) (Claude, 2026-11-19)
Josh.21.39	Jazēr	Jazer, settled Num 21:32, 32:35 *Jazēr* (after the spelling change) (Claude, 2026-11-19)
Josh.24.30	Thamnathsaræ	Timnath-serah: as 19:50 *Thamnathsaram* (after the spelling change) (Claude, 2026-11-19)
Josh.24.32	Jōsēphēīs	Josephites, settled Deut 27:12 *Jōsēphēī* (after the spelling change) (Claude, 2026-11-19)
```

## Shared names (with N1, Joshua 1–14)

N1's notes (`n1-names.md`) were read; their marks agree with mine for Achor, Achan, Gibeon, Lachish, Eglon, Azekah, Adullam, Libnah, Beth-horon, Aijalon, Japhia, Hazor, Shimron, Achshaph, Mizpeh, Goshen, Anab, Aphek, Shihor, Gezer, Gath-, Ashdod, Kirjath-jearim, Kirjath-arba, Jahaz, Kedemoth, Mephaath, Mahanaim, Carmel, Dor. Settled, nothing to match: Jericho *Hierichūs, -ūntis* (and *Hierichūntiō, -iās, -iōs* here), Gilgal *Galgala*, Jerusalem *Hierosolym-*, the Jebusites *Jebūsæ-* (*Jebūsis*, *Jebūsī* here), Hebron *Hebrōn*, Kirjath-arba *Cariatharba*, Anak *Enāqu-*, Caleb *Calebus*, Jephunneh *Jephonis*, Kenaz *Cenez-*, Seir, Bashan *Bāsān-*, Gilead *Galaad-*, Heshbon *Hesebōn*, Mahanaim, Ramoth *Rāmōtha*, Chinnereth *Cenereth-*, Rekem *Recem-*, Bethel, Luz *Lūz-*, Sidon *Sīdōn-*, Edrei *Edreī* (Bashan), the tribes and their adjectives, Joshua *Jōsua*, Eleazar *Eleāzarus*, Phinehas *Phīnees*.

My forms, for N1's chapters to match:

| Name | Mine (15–24) | N1's chapters (draft) | Note |
|---|---|---|---|
| Achor | *Āchōris* 15:7 | *Achoris* 7:24, 26 | Hebrew qamets, holem (hard call 10) |
| Achan | *Āchān* 22:20 | *Achan* 7:1, 18, 20; *Achanem* 7:19, 24 | hard call 10 |
| Debir | *Dabīr*, *Dabīris* (15:7, 15:15, 15:49, 21:15) | *Dabīr-* 10:3–12:13 (N1) | matched to N1's: Greek 10:3 Δαβείν ει (the king), Hebrew דְּבִיר; the town's own Hebrew דְּבִר and Greek Δαβίρ would leave it short |
| Arba | *Arbā* (abl.) 15:13, 21:11 | *Arba* 14:15 | stem unmarked |
| Kirjath-jearim | *Cariathjārīm-* | *Cariathjarimum* 9:17 | qamets, hireq-yod |
| Hazor | *Hāsōr* | *Hasor*, *Hasoris* 11:1–13, 12:19 | qamets, holem; Greek ω |
| Hormah | *Horma* (settled *Hormam*) | *Hormae* 12:14 | settled |
| Jarmuth | *Jerīmōth* 15:35, 21:29 | *Jerīmōthī* 10:3, 5, 23; 12:11 (N1) | matched to N1's: Greek 10:3 Ἱερειμούθ ει; shureq |
| Adullam | *Adullām* | *Adullami* 12:15 | qamets |
| Azekah | *Azēca* | *Azecam* 10:10, 11 | tsere |
| Lachish | *Lāchīs* | *Lachis* 10:3 ff | qamets, hireq-yod |
| Eglon | *Eglōn* | *Eglonis* etc. 10:3–37 | holem |
| Makkedah | *Macēda* (respelled from *Macceda*) | *Macēd-* 10:10–12:16 (N1) | tsere; Greek Μακηδά η |
| Libnah | *Lebna*, *Lebnam* (settled *Lebnā*, stem unmarked) | *Lebna*, *Lebnae* 10:29–39 | settled |
| Gaza | *Gāza* (settled *Gāzam*) | *Gazam* 10:41, *Gazae* 11:22 | hard call 9 |
| Anab | *Anāb* | *Anabo* 11:21 | qamets |
| Goshen | *Gōsen* | *Gosene* 10:41, *Gosenem* 11:16 | holem |
| Aphek | *Aphēc*, *Aphēca* | *Apheci* 12:18, *Aphece* 13:4 | tsere |
| Carmel | *Carmēl*, *Carmēlum* (Gaffiot) | *Carmelo* 12:22 | Gaffiot *Carmēlus* |
| Gibeon | *Gabaōn*, *Gabaōnem* (Gaffiot *Găbăōn*) | *Gabaon*, *Gabaonem*, *Gabaonitae* … 9–11 | Gaffiot |
| Beth-horon | *Bēthōrōn-* | *Bethoronis* 10:10, 11 | holem, holem; Greek ω |
| Gezer | *Gazer* (unmarked), *Gazerēnsēs* | *Gazeris* 10:33, 12:12 | segol, segol |
| Beth-aven | *Bēthāvenis* 18:12 | *Bethaven* 7:2 | qamets |
| Beeroth | *Bērōtha* 18:25 (respelled from *Beerota*) | *Bērōtha* 9:17 (N1) | matched to N1's |
| Chephirah | *Caphīra* (respelled from *Caphara*) | *Caphira* 9:17 | hireq-yod |
| Achshaph | *Axāph* 19:25 | *Axaphi* 11:1, 12:20 | qamets |
| Shimron | *Semerōn* 19:15 | 11:1; *Semeromeronis* 12:20 (Shimron-meron) | holem |
| Aijalon | *Ajālōn*, *Ajālōnem* | *Ajalonem* 10:12 | qamets, holem |
| Ekron | *Accarōn-* (4 times) | *Accaronis* 13:3 (N1 respells *Acharonis*) | matched |
| Kedesh (Naphtali) | *Cedēs*, *Cedēsam* | *Cedis* 12:22 (N1 respells *Cadis*) | spelling matched; my ē by the Greek Κάδης (hard call 6); N1's genitive *Cedis* agrees |
| Jokneam | *Jeconām* (19:11; 21:34 respelled) | ***Jachanānæ*** 12:22 (N1) | **two spellings left**: one to choose (both mark the final ā) |
| Megiddo | *Mageddōnēnsēs* (respelled) | *Mageddonis* 12:21 | dd as N1's |
| Dor | *Dōriōs*, *Ēndōriōs* 17:11 | *Doris* 12:23 | holem |
| Taanach | *Thanach* 21:25, *Tanacēnsēs* 17:11 (unmarked: patah, patah) | ***Thenacī*** 12:21 (N1) | **three spellings left** (Th/T, a/e, ch/c), as N1 notes too: one to choose |
| Tappuah | *Taphūa*, *Taphūæ*, *Bēthtaphūa*, *Ēntaphūæ* | ***Thaphūæ*** 12:17 (N1) | **two spellings left** (Th/T): several towns of the name, mine as printed; the marks agree |
| Kedemoth | *Cedēmōtha* 21:37 (settled Deut 2:26 *Cedēmōthis*) | *Cedemotha* 13:18 (N1 respells *Cedemothia*) | matched |
| Mephaath | *Mēphāath* 21:37 | *Mephaatha* 13:18 | tsere-yod, qamets |
| Jazer | *Jazēr* (respelled from *Jaser*) | *Jazer* 13:25 | settled; N1 agrees |
| Shihor | *Sīhōr* 19:26 (Shihor-libnath) | *Sihore* 13:3 (Egypt's) | the same Hebrew שִׁיחוֹר |
| Hamath / Hammath | *Hemath* 19:35 (Hammath, unmarked) | *Hematham* 13:5 (Hamath, settled) | two places |
| Kiriathaim | (18:28 *Cariathaim* is Kirjath: hard call 8) | *Cariathaimum* 13:19 | settled *Cariāthaim* for 13:19 |

## Odd things in the words

- 18:18 *Bethaglae* stands where the KJV's 18:19 has Beth-hoglah (the verse division, not the name).
- 24:11 has no Hivites (Castellio's list): nothing to do for the names.
- 22:20 *Annon* is Latin (*an nōn*), not a name.
- The shared `Josh.forms.tsv` (other readers) already marks *Jōsuā* (17:14) and *Jōvāna* (22:16, 17: "the stem is the names readers'"): *Jōvān-* is the settled *Jōvānā*'s stem (1), so *Jōvāna* stands.

## Decisions

| Person / place / people | In the preview (verses) | Hebrew | Greek | Decided | Source |
|---|---|---|---|---|---|
| Zin | *Sinem* 15.1,15.2 | — | — | *Sinem* | Zin, settled Num 20:1 *Sinem* |
| Addar | *Adar* 15.3 | אַדָּרָה | — | *Adār* | Addar, Hebrew אַדָּרָה: patah, qamets; as the settled Num 34:4 *Hazaradār* |
| Karka | *Carcaam* 15.3 | הַקַּרְקָעָה | — | *Carcāam* | Karka, Hebrew הַקַּרְקָעָה: patah, qamets; -am the accusative |
| Azmon | *Asemonem* 15.4 | — | — | *Asmōnem* | Azmon, settled Num 34:4 *Asmōnem* (after the spelling change) |
| Beth-hoglah | *Bethaglam* 15.6; *Bethagla* 18.21; *Bethaglæ* 18.18 | בֵּית חָגְלָה | — | *Bēthaglam*, *Bēthagla*, *Bēthaglæ* | Beth-hoglah, Hebrew בֵּית חָגְלָה: tsere-yod, qamets hatuf (short); *Bēth-* as the settled *Bēthēl* / Beth-hoglah: as 15:6 *Bēthaglam* |
| Beth-arabah | *Betharabam* 15.6; *Betharaba* 15.61,18.22 | בֵּית הָעֲרָבָה | — | *Bētharābam*, *Bētharāba* | Beth-arabah, Hebrew בֵּית הָעֲרָבָה: tsere-yod, hataf patah, qamets / Beth-arabah: as 15:6 *Bētharābam*; nominative -a |
| Bohan | *Bohenis* 15.6,18.17 | בֹּהַן | — | *Bōhenis* | Bohan, Hebrew בֹּהַן: holem, patah |
| Debir | *Dabir* 15.7,15.49,21.15; *Dabiris* 15.15 | דְּבִיר | Δαβείν | *Dabīr*, *Dabīris* | Debir: one Latin word with N1's *Dabīr-* (10:3 the king Debir, Hebrew דְּבִיר, Greek Δαβείν ει; the town 10:38–12:13); here Hebrew דְּבִר, Greek Δαβίρ / Debir: as *Dabīr* (N1's *Dabīr-*); genitive -is |
| Achor | *Achōris* 15.7 | עָכוֹר | Ἀχώρ | *Āchōris* | Achor, Hebrew עָכוֹר: qamets, holem; Greek Ἀχώρ ω |
| Gilgal | *Galgala* 15.7 | — | — | *Galgala* | Gilgal, settled Deut 11:30 *Galgala* |
| Adummim | *Adumim* 15.7; *Adommim* 18.17 | אֲדֻמִּים | — | *Adommīm* | Adummim, Hebrew אֲדֻמִּים: hireq-yod; spelled as 18:17 *Adommim* (after the spelling change) / Adummim, Hebrew אֲדֻמִּים: hataf patah, qibbuts (short), hireq-yod |
| En-shemesh | *Ensemis* 15.7; *Ensemen* 18.17 | עֵין שֶׁמֶשׁ | — | *Ēnsemis*, *Ēnsemen* | En-shemesh, Hebrew עֵין שֶׁמֶשׁ: tsere-yod, segol / En-shemesh: as 15:7 *Ēnsemis* (the ending as printed) |
| En-rogel | *Enrogel* 15.7,18.16 | עֵין רֹגֵל | — | *Ēnrōgēl* | En-rogel, Hebrew עֵין רֹגֵל: tsere-yod, holem, tsere |
| Hinnom | *Hennomi* 15.8,18.16 | הִנֹּם | — | *Hennōmī* | Hinnom, Hebrew הִנֹּם: hireq, holem; genitive -ī |
| Jebus | *Jebusis* 15.8,18.16 | — | — | *Jebūsis* | Jebus (the Jebusite), settled Gen 10:16 *Jebūsem*; genitive -is |
| Jebusi | *Jebusi* 18.28 | הַיְבוּסִי | — | *Jebūsī* | Jebusi, settled stem *Jebūs-* (Gen 10:16); Hebrew הַיְבוּסִי: shureq, hireq-yod |
| Jebusites | *Jebusæi* 15.63 | — | — | *Jebūsæī* | Jebusites, settled *Jebūsæōs* (Deut 7:1) |
| Jerusalem | *Hierosolyma* 15.8,18.28 | — | — | *Hierosolyma* | Jerusalem, nominative (*quæ eadem Hierosolyma est*; *aliās Hierosolyma*), settled Gal 4:26 *Hierosolyma* |
| Nephtoah | *Nephtoæ* 15.9,18.15 | נֶפְתּוֹחַ | Ναφθώ | *Nephtōæ* | Nephtoah, Hebrew נֶפְתּוֹחַ: segol, holem; Greek Ναφθώ ω; genitive -æ |
| Baalah | *Baalam* 15.9; *Baala* 15.10; *Baala* 15.29; *Baalæ* 15.11 | בַּעֲלָה | — | *Baalam*, *Baalā*, *Baala*, *Baalæ* | Baalah, Hebrew בַּעֲלָה: patah, hataf patah (short); -am the accusative / Baalah: ablative after *Ā* (*Ā Baala curvātur*); stem as 15:9 *Baalam* / Baalah, Hebrew בַּעֲלָה: patah, hataf patah; nominative in the list / Baalah: as 15:9 *Baalam*; genitive -æ |
| Kirjath-jearim | *Cariathjarimum* 15.9,18.14; *Cariathjarimi* 18.15; *Cariathiarim* 15.60 | קִרְיַת יְעָרִים | — | *Cariathjārīmum*, *Cariathjārīmī*, *Cariathjārīm* | Kirjath-jearim, Hebrew קִרְיַת יְעָרִים: hireq, patah, shewa, qamets, hireq-yod; *Cariath-* unmarked as the settled *Cariatharbæ* / Kirjath-jearim: as 15:9 *Cariathjārīmum*; genitive -ī / Kirjath-jearim: as 15:9 *Cariathjārīmum* (after the spelling change, j as 15:9, 18:14, 18:15) |
| Mount Jearim | *Jarimi* 15.10 | יְעָרִים | — | *Jārīmī* | Mount Jearim, Hebrew יְעָרִים: qamets, hireq-yod; genitive -ī |
| Mount Seir | *Seir* 15.10,24.4 | — | — | *Seir* | Mount Seir, settled *Seir* (Num 24:18) |
| Chesalon | *Cesalon* 15.10 | כְסָלוֹן | — | *Cesālōn* | Chesalon, Hebrew כְסָלוֹן: shewa, qamets, holem |
| Beth-shemesh | *Bethsemem* 15.10,19.22,21.16; *Bethsemes* 19.38 | בֵּית שֶׁמֶשׁ | — | *Bēthsemem*, *Bēthsemes* | Beth-shemesh, Hebrew בֵּית שֶׁמֶשׁ: tsere-yod, segol / Beth-shemesh: as *Bēthsemem* |
| Ir-shemesh | *Irsemes* 19.41 | עִיר שֶׁמֶשׁ | — | *Īrsemes* | Ir-shemesh, Hebrew עִיר שֶׁמֶשׁ: hireq-yod, segol |
| Ekron | *Accaronis* 15.11; *Accaron* 15.45,19.43; *Accārōne* 15.46 | עֶקְרוֹן | Ἀκκαρών | *Accarōnis*, *Accarōn*, *Accarōne* | Ekron, Hebrew עֶקְרוֹן: segol, holem; Greek Ἀκκαρών ω / Ekron: as 15:11 *Accarōnis* / Ekron: as 15:11 *Accarōnis* (Hebrew segol: the preview's ā has no source) |
| Shicron | *Sechronem* 15.11 | שִׁכְּרוֹנָה | — | *Sechrōnem* | Shicron, Hebrew שִׁכְּרוֹנָה: hireq, holem |
| Jabneel | *Jabneel* 15.11; *Jabnel* 19.33 | יַבְנְאֵל | — | *Jabneēl*, *Jabnēl* | Jabneel (Judah), Hebrew יַבְנְאֵל: patah, shewa, tsere / Jabneel (Naphtali), Hebrew יַבְנְאֵל: patah, tsere |
| Anak | *Enaqui* 15.13,15.14,21.11 | — | — | *Enāquī* | Anak, settled Num 13:22 *Enāquō*; genitive -ī |
| Sheshai | *Sesaim* 15.14 | — | — | *Sēsæum* | Sheshai, settled Num 13:22 *Sēsæus*, accusative (after the spelling change) |
| Ahiman | *Achimanem* 15.14 | — | — | *Achīmanem* | Ahiman, settled Num 13:22 *Achīman* |
| Talmai | *Tholmaim* 15.14 | — | — | *Thalmæum* | Talmai, settled Num 13:22 *Thalmæus*, accusative (after the spelling change) |
| Kirjath-sepher | *Cariathsepher* 15.15,15.16 | קִרְיַת־סֵפֶר | — | *Cariathsēpher* | Kirjath-sepher, Hebrew קִרְיַת־סֵפֶר: hireq, patah, tsere, segol |
| Achsah | *Axam* 15.16,15.17 | עַכְסָה | — | *Axam* | Achsah, Hebrew עַכְסָה: patah, shewa; -am the accusative |
| Othniel | *Othoniel* 15.17 | עָתְנִיאֵל | Γοθονιήλ | *Othonīēl* | Othniel, Hebrew עָתְנִיאֵל: qamets hatuf (short), hireq-yod, tsere; Greek Γοθονιήλ η |
| Kenaz | *Cenezi* 15.17 | קְנַז | — | *Cenezī* | Kenaz, Hebrew קְנַז: shewa, patah; genitive -ī (settled *Cenezeō*, Num 32:12, unmarked stem) |
| Caleb | *Calebi* 15.17; *Chalebo* 21.12 | — | — | *Calebī*, *Calebō* | Caleb, settled *Calebus* (unmarked, Num 13:6); genitive -ī / Caleb, settled Num 14:30 *Calebō* (after the spelling change) |
| Kirjath-arba | *Cariatharba* 15.13,15.54; *Cariatharbam* 20.7,21.11 | — | — | *Cariatharba*, *Cariatharbam* | Kirjath-arba, settled Gen 23:2 *Cariatharbæ* |
| Arba | *Arba* 15.13,21.11 | אַרְבַּע | — | *Arbā* | Arba, Hebrew אַרְבַּע: patah, patah; ablative after *ab* (Gaffiot *Arba, æ*, unmarked) |
| Kirjath-sannah | *Cariathsenna* 15.49 | קִרְיַת־סַנָּה | — | *Cariathsenna* | Kirjath-sannah, Hebrew קִרְיַת־סַנָּה: hireq, patah, patah |
| Kabzeel | *Cabseel* 15.21 | קַבְצְאֵל | — | *Cabseēl* | Kabzeel, Hebrew קַבְצְאֵל: patah, shewa, tsere |
| Eder | *Eder* 15.21 | עֵדֶר | — | *Ēder* | Eder, Hebrew עֵדֶר: tsere, segol |
| Jagur | *Jagur* 15.21 | יָגוּר | — | *Jāgūr* | Jagur, Hebrew יָגוּר: qamets, shureq |
| Kinah | *Cina* 15.22 | קִינָה | — | *Cīna* | Kinah, Hebrew קִינָה: hireq-yod; nominative -a |
| Dimonah | *Dimona* 15.22 | דִּימוֹנָה | — | *Dīmōna* | Dimonah, Hebrew דִּימוֹנָה: hireq-yod, holem; nominative -a |
| Adadah | *Adada* 15.22 | עַדְעָדָה | — | *Adāda* | Adadah, Hebrew עַדְעָדָה: patah, qamets; nominative -a |
| Kedesh | *cēdēs* 15.23,19.37 | קֶדֶשׁ | Κάδης | *Cedēs* | Kedesh (capital: the layout row), Hebrew קֶדֶשׁ segol; Greek Κάδης η (15:23, 20:7, 21:32), decision 52's order |
| Kedesh in Galilee | *Cēdēs* 21.32; *Cedesam* 20.7 | קֶדֶשׁ | Κάδης | *Cedēs*, *Cedēsam* | Kedesh in Galilee: Greek Κάδης η; Hebrew קֶדֶשׁ segol (first syllable short) / Kedesh in Galilee: as 21:32 *Cedēs* (Greek Κάδης η) |
| Hazor | *Hasor* 15.23,15.25,19.36 | חָצוֹר | Ἀσώρ | *Hāsōr* | Hazor, Hebrew חָצוֹר: qamets, holem; Greek Ἀσώρ ω |
| Hazor-hadattah | *Hasorhadatta* 15.25 | חָצוֹר חֲדַתָּה | — | *Hāsōrhadatta* | Hazor-hadattah, Hebrew חָצוֹר חֲדַתָּה: qamets, holem, hataf patah, patah |
| En-hazor | *Enhasor* 19.37 | עֵין חָצוֹר | — | *Ēnhāsōr* | En-hazor, Hebrew עֵין חָצוֹר: tsere-yod, qamets, holem |
| Ithnan | *Jethnan* 15.23 | יִתְנָן | — | *Jethnān* | Ithnan, Hebrew יִתְנָן: hireq, qamets |
| Ziph | *Ziph* 15.24,15.55 | זִיף | — | *Zīph* | Ziph, Hebrew זִיף: hireq-yod |
| Telem | *Tēlem* 15.24 | טֶלֶם | — | *Telem* | Telem, Hebrew טֶלֶם: segol, segol (the preview's ē had no source for the name) |
| Bealoth | *Baloth* 15.24 | בְּעָלוֹת | — | *Bālōth* | Bealoth, Hebrew בְּעָלוֹת: qamets, holem |
| Kerioth-hezron | *Cariothesron* 15.25 | קְרִיּוֹת חֶצְרוֹן | — | *Cariōthesrōn* | Kerioth-hezron, Hebrew קְרִיּוֹת חֶצְרוֹן: shewa, hireq, holem, segol, holem |
| Amam | *amān* 15.26 | אֲמָם | — | *Amān* | Amam (capital: the layout row), Hebrew אֲמָם: hataf patah, qamets |
| Shema | *Sama* 15.26 | שְׁמַע | — | *Sama* | Shema, Hebrew שְׁמַע: shewa, patah |
| Moladah | *Molada* 15.26,19.2 | מוֹלָדָה | — | *Mōlāda* | Moladah, Hebrew מוֹלָדָה: holem, qamets; nominative -a |
| Hazar-gaddah | *Hasergadda* 15.27 | חֲצַר גַּדָּה | — | *Hasergadda* | Hazar-gaddah, Hebrew חֲצַר גַּדָּה: hataf patah, patah, patah |
| Heshmon | *Hassemon* 15.27 | חֶשְׁמוֹן | — | *Hassemōn* | Heshmon, Hebrew חֶשְׁמוֹן: segol, holem |
| Beth-palet | *Bethphelet* 15.27 | בֵּית פָּלֶט | — | *Bēthphēlet* | Beth-palet, Hebrew בֵּית פָּלֶט: tsere-yod, qamets, segol |
| Hazar-shual | *Hazersual* 15.28; *Hasersual* 19.3 | חֲצַר שׁוּעָל | — | *Hasersūāl* | Hazar-shual: as 19:3 *Hasersūāl* (after the spelling change) / Hazar-shual, Hebrew חֲצַר שׁוּעָל: hataf patah, patah, shureq, qamets |
| Beer-sheba | *Bersaba* 15.28,19.2 | — | — | *Bersaba* | Beer-sheba, settled Gen 21:31 *Bersaba* |
| Bizjothjah | *Baziothia* 15.28 | בִּזְיוֹתְיָה | — | *Baziōthia* | Bizjothjah, Hebrew בִּזְיוֹתְיָה: hireq, holem; nominative -a |
| Iim | *Iiim* 15.29 | עִיִּים | — | *Iiīm* | Iim, Hebrew עִיִּים: hireq, hireq-yod (spelled as 1738 prints it) |
| Azem | *Ezem* 15.29; *Asem* 19.3 | עָצֶם | — | *Āsem* | Azem: as 19:3 *Āsem* (after the spelling change) / Azem, Hebrew (pausal) עָצֶם: qamets, segol |
| Eltolad | *Eltolad* 15.30,19.4 | אֶלְתּוֹלַד | — | *Eltōlad* | Eltolad, Hebrew אֶלְתּוֹלַד: segol, holem, patah |
| Chesil | *Chesil* 15.30 | כְּסִיל | — | *Chesīl* | Chesil, Hebrew כְּסִיל: shewa, hireq-yod |
| Hormah | *Harma* 15.30; *Horma* 19.4 | חָרְמָה | — | *Horma* | Hormah, settled Num 14:45 *Hormam* (after the spelling change) / Hormah, settled Num 14:45 *Hormam* (unmarked; Hebrew חָרְמָה qamets hatuf) |
| Ziklag | *Siceleg* 15.31,19.5 | צִקְלַג | — | *Siceleg* | Ziklag, Hebrew צִקְלַג: hireq, patah |
| Madmannah | *Medemena* 15.31 | מַדְמַנָּה | — | *Medemena* | Madmannah, Hebrew מַדְמַנָּה: patah, patah |
| Sansannah | *Sesenna* 15.31 | סַנְסַנָּה | — | *Sesenna* | Sansannah, Hebrew סַנְסַנָּה: patah, patah |
| Lebaoth | *Lebaoth* 15.32 | לְבָאוֹת | — | *Lebāōth* | Lebaoth, Hebrew לְבָאוֹת: shewa, qamets, holem |
| Beth-lebaoth | *Bethlebaoth* 19.6 | — | — | *Bēthlebāōth* | Beth-lebaoth: as 15:32 *Lebāōth* |
| Shilhim | *Selin* 15.32 | שִׁלְחִים | — | *Selīn* | Shilhim, Hebrew שִׁלְחִים: hireq, hireq-yod |
| Ain | *Æn* 15.32; *Ain* 19.7,21.16 | עַיִן | — | *Ain* | Ain: as 19:7, 21:16 *Ain* (after the spelling change); settled Num 34:11 *Ainis* (unmarked) / Ain, Hebrew עַיִן: patah, hireq; settled Num 34:11 *Ainis* (unmarked) |
| Rimmon | *Remmon* 15.32,19.7; *Remmonem* 19.13 | רִמּוֹן | — | *Remmōn*, *Remmōnem* | Rimmon, Hebrew רִמּוֹן: hireq, holem / Rimmon (Zebulun): as *Remmōn* |
| Eshtaol | *Estaol* 15.33,19.41 | אֶשְׁתָּאוֹל | — | *Estāōl* | Eshtaol, Hebrew אֶשְׁתָּאוֹל: segol, qamets, holem |
| Zorah | *Sarea* 15.33; *Saraa* 19.41 | צָרְעָה | — | *Sāraa* | Zorah: as 19:41 *Sāraa* (after the spelling change) / Zorah, Hebrew צָרְעָה: qamets; nominative -a |
| Ashnah | *Asena* 15.33; *Esna* 15.43 | אַשְׁנָה | — | *Asena*, *Esna* | Ashnah, Hebrew אַשְׁנָה: patah, shewa; Gaffiot *Asena* (unmarked) / Ashnah, Hebrew אַשְׁנָה: patah, shewa; nominative -a |
| Zanoah | *Zanoa* 15.34,15.56 | זָנוֹחַ | — | *Zānōa* | Zanoah, Hebrew זָנוֹחַ: qamets, holem |
| En-gannim | *Engannin* 15.34; *Engannim* 19.21,21.29 | עֵין גַּנִּים | — | *Ēngannīn*, *Ēngannīm* | En-gannim (Judah), Hebrew עֵין גַּנִּים: tsere-yod, patah, hireq-yod / En-gannim (Issachar), Hebrew עֵין גַּנִּים: tsere-yod, patah, hireq-yod |
| Tappuah | *Taphna* 15.34; *Taphua* 16.8; *Taphuæ* 17.8 | תַּפּוּחַ | — | *Taphūa*, *Taphūā*, *Taphūæ* | Tappuah: 1738's *Taphna* is a turned u (Vulgate *Taphua*), after the spelling change; Hebrew תַּפּוּחַ: patah, shureq / Tappuah, Hebrew תַּפּוּחַ: patah, shureq; ablative after *Ā* / Tappuah: as 16:8 *Taphūā* |
| En-tappuah | *Entaphuæ* 17.7 | עֵין תַּפּוּחַ | — | *Ēntaphūæ* | En-tappuah, Hebrew עֵין תַּפּוּחַ: tsere-yod, patah, shureq |
| Beth-tappuah | *Bethtaphua* 15.53 | בֵּית־תַּפּוּחַ | — | *Bēthtaphūa* | Beth-tappuah, Hebrew בֵּית־תַּפּוּחַ: tsere-yod, patah, shureq |
| Enam | *Ename* 15.34 | הָעֵינָם | — | *Ēnāme* | Enam, Hebrew הָעֵינָם: tsere-yod, qamets |
| Jarmuth | *Jerimoth* 15.35,21.29 | יַרְמוּת | — | *Jerīmōth* | Jarmuth, Greek 10:3 Ἱερειμούθ ει (N1's *Jerīmōth-*), Hebrew יַרְמוּת shureq |
| Adullam | *Adullam* 15.35 | עֲדֻלָּם | — | *Adullām* | Adullam, Hebrew עֲדֻלָּם: hataf patah, qibbuts, qamets; as the settled Gen 38:1 *Adulāmītam* |
| Socoh | *Socho* 15.35,15.48 | שׂוֹכֹה | — | *Sōchō* | Socoh, Hebrew שׂוֹכֹה: holem, holem |
| Azekah | *Azeca* 15.35 | עֲזֵקָה | — | *Azēca* | Azekah, Hebrew עֲזֵקָה: hataf patah, tsere; nominative -a |
| Sharaim | *Sarāim* 15.36 | שַׁעֲרַיִם | — | *Saraim* | Sharaim, Hebrew שַׁעֲרַיִם: patah, hataf patah, patah, hireq (the preview's ā is the settled *Sarāim*, Sarai, another name) |
| Adithaim | *Adithaim* 15.36 | עֲדִיתַיִם | — | *Adīthaim* | Adithaim, Hebrew עֲדִיתַיִם: hataf patah, hireq-yod, patah, hireq |
| Gederah | *Gedera* 15.36 | הַגְּדֵרָה | — | *Gedēra* | Gederah, Hebrew הַגְּדֵרָה: shewa, tsere; nominative -a |
| Gederothaim | *Gederothaim* 15.36 | גְּדֵרֹתַיִם | — | *Gedērōthaim* | Gederothaim, Hebrew גְּדֵרֹתַיִם: shewa, tsere, holem, patah, hireq |
| Gederoth | *Gederoth* 15.41 | גְּדֵרוֹת | — | *Gedērōth* | Gederoth, Hebrew גְּדֵרוֹת: shewa, tsere, holem |
| Zenan | *Sanan* 15.37 | צְנָן | — | *Sanān* | Zenan, Hebrew צְנָן: shewa, qamets |
| Hadashah | *Hadassa* 15.37 | חֲדָשָׁה | — | *Hadāssa* | Hadashah, Hebrew חֲדָשָׁה: hataf patah, qamets; nominative -a |
| Migdal-gad | *Magdalgad* 15.37 | מִגְדַּל־גָּד | — | *Magdalgād* | Migdal-gad, Hebrew מִגְדַּל־גָּד: hireq, patah, qamets |
| Dilean | *Delean* 15.38 | דִּלְעָן | — | *Deleān* | Dilean, Hebrew דִּלְעָן: hireq, qamets |
| Joktheel | *Jecthel* 15.38 | יָקְתְאֵל | — | *Jecthēl* | Joktheel, Hebrew יָקְתְאֵל: qamets hatuf, shewa, tsere |
| Lachish | *Lachis* 15.39 | לָכִישׁ | — | *Lāchīs* | Lachish, Hebrew לָכִישׁ: qamets, hireq-yod |
| Bozkath | *Baschat* 15.39 | בָּצְקַת | — | *Baschat* | Bozkath, Hebrew בָּצְקַת: qamets hatuf, patah |
| Eglon | *Eglon* 15.39 | עֶגְלוֹן | — | *Eglōn* | Eglon, Hebrew עֶגְלוֹן: segol, holem |
| Cabbon | *Chabbon* 15.40 | כַּבּוֹן | — | *Chabbōn* | Cabbon, Hebrew כַּבּוֹן: patah, holem |
| Lahmam | *Leheman* 15.40 | לַחְמָס | — | *Lehemān* | Lahmam, Hebrew לַחְמָס: patah, qamets |
| Kithlish | *Cethlis* 15.40 | כִּתְלִישׁ | — | *Cethlīs* | Kithlish, Hebrew כִּתְלִישׁ: hireq, hireq-yod |
| Beth-dagon | *Bethdagon* 15.41; *Bethdagonem* 19.27 | בֵּית־דָּגוֹן | — | *Bēthdāgōn*, *Bēthdāgōnem* | Beth-dagon, Hebrew בֵּית־דָּגוֹן: tsere-yod, qamets, holem / Beth-dagon (Asher): as 15:41 *Bēthdāgōn* |
| Naamah | *Naama* 15.41 | נַעֲמָה | — | *Naama* | Naamah, Hebrew נַעֲמָה: patah, hataf patah; nominative -a |
| Makkedah | *Macceda* 15.41 | מַקֵּדָה | — | *Macēda* | Makkedah, Hebrew מַקֵּדָה: patah, tsere; nominative -a (after the spelling change, as 10:10–29, 12:16 *Maceda*) |
| Libnah | *Lebnā* 15.42; *Lebnam* 21.14 | — | — | *Lebna*, *Lebnam* | Libnah, settled Num 33:20 *Lebnā* (stem unmarked); nominative in the list / Libnah, settled Num 33:20 *Lebnā* (stem unmarked); accusative |
| Ether | *Ether* 15.42; *Athar* 19.7 | עֶתֶר | — | *Ether*, *Athar* | Ether, Hebrew עֶתֶר: segol, segol / Ether (Simeon), Hebrew עֶתֶר: segol, segol |
| Ashan | *Assan* 15.42; *Asan* 19.7 | עָשָׁן | — | *Āsān* | Ashan: as 19:7 *Āsān* (after the spelling change) / Ashan, Hebrew עָשָׁן: qamets, qamets |
| Nezib | *Nezib* 15.43 | נְצִיב | — | *Nezīb* | Nezib, Hebrew נְצִיב: shewa, hireq-yod |
| Keilah | *Ceila* 15.44 | קְעִילָה | — | *Ceīla* | Keilah, Hebrew קְעִילָה: shewa, hireq-yod; nominative -a |
| Achzib | *Axib* 15.44; *Axibæ* 19.29 | אַכְזִיב | — | *Axīb*, *Axībæ* | Achzib, Hebrew אַכְזִיב: patah, hireq-yod / Achzib (Asher), Hebrew אַכְזִיבָה: patah, hireq-yod; genitive -æ |
| Mareshah | *Maresa* 15.44 | מָרֵאשָׁה | — | *Mārēsa* | Mareshah, Hebrew מָרֵאשָׁה: qamets, tsere; nominative -a |
| Gaza | *Gaza* 15.47 | — | — | *Gāza* | Gaza, settled Gen 10:19, Deut 2:23 *Gāzam* (Gaffiot *Găza*: the settled form first) |
| Shamir | *Samir* 15.48 | שָׁמִיר | — | *Sāmīr* | Shamir, Hebrew שָׁמִיר: qamets, hireq-yod |
| Jattir | *Jatthir* 15.48; *Jattir* 21.14 | וְיַתִּיר | — | *Jattīr* | Jattir: as 21:14 *Jattir* (after the spelling change); Hebrew וְיַתִּיר: patah, hireq-yod / Jattir, Hebrew יַתִּיר (15:48; יַתִּר here, defective): patah, hireq-yod |
| Dannah | *Danna* 15.49 | דַּנָּה | — | *Danna* | Dannah, Hebrew דַּנָּה: patah |
| Anab | *Anab* 15.50 | עֲנָב | — | *Anāb* | Anab, Hebrew עֲנָב: hataf patah, qamets |
| Eshtemoh | *Estemo* 15.50 | אֶשְׁתְּמֹה | — | *Estemō* | Eshtemoh, Hebrew אֶשְׁתְּמֹה: segol, shewa, holem |
| Eshtemoa | *Estemoam* 21.14 | אֶשְׁתְּמֹעַ | — | *Estemōam* | Eshtemoa, Hebrew אֶשְׁתְּמֹעַ: segol, shewa, holem; -am the accusative |
| Anim | *Anim* 15.50 | עָנִים | — | *Ānīm* | Anim, Hebrew עָנִים: qamets, hireq-yod |
| Goshen | *Gosen* 15.51 | גֹּשֶׁן | — | *Gōsen* | Goshen, Hebrew גֹּשֶׁן: holem, segol |
| Holon | *Holon* 15.51; *Holonem* 21.15 | חֹלֹן | — | *Hōlōn*, *Hōlōnem* | Holon, Hebrew חֹלֹן: holem, holem / Holon: as 15:51 *Hōlōn* |
| Giloh | *Gilo* 15.51 | גִּלֹה | — | *Gilō* | Giloh, Hebrew גִּלֹה: hireq, holem |
| Arab | *Arab* 15.52 | אֲרַב | — | *Arab* | Arab, Hebrew אֲרַב: hataf patah, patah |
| Dumah | *Duma* 15.52 | דּוּמָה | — | *Dūma* | Dumah, Hebrew דּוּמָה (WLC רוּמָה): shureq; the settled Gen 25:14 *Duma* is Ishmael's son, another name-bearer |
| Eshean | *Esaan* 15.52 | אֶשְׁעָן | — | *Esaān* | Eshean, Hebrew אֶשְׁעָן: segol, qamets |
| Janum | *Jānum* 15.53 | יָנוּם | — | *Jānūm* | Janum, Hebrew (qere) יָנוּם: qamets, shureq |
| Aphekah | *Apheca* 15.53 | אֲפֵקָה | — | *Aphēca* | Aphekah, Hebrew אֲפֵקָה: hataf patah, tsere; nominative -a |
| Aphek | *Aphec* 19.30 | אֲפֵק | — | *Aphēc* | Aphek, Hebrew אֲפֵק: hataf patah, tsere |
| Humtah | *Humta* 15.54 | חֻמְטָה | — | *Humta* | Humtah, Hebrew חֻמְטָה: qibbuts |
| Zior | *Sior* 15.54 | צִיעֹר | — | *Sīōr* | Zior, Hebrew צִיעֹר: hireq-yod, holem |
| Maon | *Maon* 15.55 | מָעוֹן | — | *Māōn* | Maon, Hebrew מָעוֹן: qamets, holem |
| Carmel | *Carmel* 15.55 | — | — | *Carmēl* | Carmel (Judah), Gaffiot *Carmēl* |
| Jezreel | *Jezræl* 15.56,19.18; *Jezrælis* 17.16 | יִזְרְעֶאל | — | *Jezræl*, *Jezrælis* | Jezreel, Hebrew יִזְרְעֶאל: hireq (short); the æ as printed / Jezreel: as 15:56 *Jezræl* |
| Jokdeam | *Jucadam* 15.56 | יָקְדְעָם | — | *Jucadām* | Jokdeam, Hebrew יָקְדְעָם: qamets hatuf, shewa, qamets |
| Kain | *Cain* 15.57 | הַקַּיִן | — | *Cain* | Kain, Hebrew הַקַּיִן: patah, hireq; Gaffiot *Cain* (unmarked) |
| Gibeah | *Gabaa* 15.57 | גִּבְעָה | — | *Gabāa* | Gibeah, Hebrew גִּבְעָה: hireq, qamets; nominative -a |
| Gibeath | *Gabaatha* 18.28 | גִּבְעַת | — | *Gabaatha* | Gibeath, Hebrew גִּבְעַת: hireq, patah |
| Timnah | *Thamna* 15.57 | — | — | *Thamna* | Timnah, settled Gen 36:40 *Thamna* |
| Timnathah | *Thamnatha* 19.43 | תִּמְנָתָה | — | *Thamnātha* | Timnathah, Hebrew תִּמְנָתָה: hireq, qamets (settled *Thamnam*, Gen 38:12, stem unmarked) |
| Timnath-serah | *Thamnathsaram* 19.50; *Thannathseræ* 24.30 | תִּמְנַת־סֶרַח | — | *Thamnathsaram*, *Thamnathsaræ* | Timnath-serah, Hebrew תִּמְנַת־סֶרַח: hireq, patah, segol, patah / Timnath-serah: as 19:50 *Thamnathsaram* (after the spelling change) |
| Halhul | *Halhul* 15.58 | חַלְחוּל | — | *Halhūl* | Halhul, Hebrew חַלְחוּל: patah, shureq |
| Beth-zur | *Bethsur* 15.58 | בֵּית־צוּר | — | *Bēthsūr* | Beth-zur, Hebrew בֵּית־צוּר: tsere-yod, shureq |
| Gedor | *Gedor* 15.58 | גְדוֹר | — | *Gedōr* | Gedor, Hebrew גְדוֹר: shewa, holem |
| Maarath | *Mareth* 15.59 | מַעֲרָת | — | *Marēth* | Maarath, Hebrew מַעֲרָת: patah, hataf patah, qamets |
| Beth-anoth | *Bethanoth* 15.59 | בֵּית־עֲנוֹת | — | *Bēthanōth* | Beth-anoth, Hebrew בֵּית־עֲנוֹת: tsere-yod, hataf patah, holem |
| Beth-anath | *Bethanath* 19.38 | בֵּית־עֲנָת | — | *Bēthanāth* | Beth-anath, Hebrew בֵּית־עֲנָת: tsere-yod, hataf patah, qamets |
| Eltekon | *Eltecon* 15.59 | אֶלְתְּקֹן | — | *Eltecōn* | Eltekon, Hebrew אֶלְתְּקֹן: segol, shewa, holem |
| Eltekeh | *Eltece* 19.44,21.23 | אֶלְתְּקֵה | — | *Eltecē* | Eltekeh, Hebrew אֶלְתְּקֵה: segol, shewa, tsere |
| Kirjath-baal | *Cariathbaal* 15.60,18.14 | קִרְיַת־בַּעַל | — | *Cariathbaal* | Kirjath-baal, Hebrew קִרְיַת־בַּעַל: hireq, patah, patah, patah; *Cariath-* as the settled *Cariatharbæ* |
| Rabbah | *Rabba* 15.60 | הָרַבָּה | — | *Rabba* | Rabbah, Hebrew הָרַבָּה: patah |
| Middin | *Meddin* 15.61 | מִדִּין | — | *Meddīn* | Middin, Hebrew מִדִּין: hireq, hireq-yod |
| Secacah | *Sachacha* 15.61 | סְכָכָה | — | *Sachācha* | Secacah, Hebrew סְכָכָה: shewa, qamets; nominative -a |
| Nibshan | *Nebsan* 15.62 | נִבְשָׁן | — | *Nebsān* | Nibshan, Hebrew נִבְשָׁן: hireq, qamets |
| En-gedi | *Engaddi* 15.62 | עֵין גֶּדִי | — | *Ēngaddī* | En-gedi, Hebrew עֵין גֶּדִי: tsere-yod, segol, hireq-yod |
| the sons of Joseph | *Josephidis* 16.1; *Josephidæ* 17.14 | — | — | *Jōsēphidīs*, *Jōsēphidæ* | the sons of Joseph, settled *Jōsēph-*; -idēs as the settled *Abrāhāmidēs*; dative plural -īs (*Josephidis … sors obtigit*) / the sons of Joseph: as 16:1 *Jōsēphidīs* |
| Josephites | *Josepheos* 18.11; *Josephæis* 24.32 | — | — | *Jōsēphēōs*, *Jōsēphēīs* | Josephites, settled Deut 27:12 *Jōsēphēī* / Josephites, settled Deut 27:12 *Jōsēphēī* (after the spelling change) |
| of Jericho | *Hierichuntio* 16.1; *Hierichuntias* 16.1 | — | — | *Hierichūntiō*, *Hierichūntiās* | of Jericho (adjective): settled *Hierichūnt-*; -ius |
| men of Jericho | *Hierichuntios* 24.11 | — | — | *Hierichūntiōs* | men of Jericho: settled *Hierichūnt-*; -ius |
| Luz | *Lūsæ* 18.13 | — | — | *Lūzæ* | Luz, settled Gen 48:3 *Lūzæ* (after the spelling change) |
| Archi | *Arciatarothorum* 16.2 | הָאַרְכִּי | — | *Arciatārōthōrum* | Archi (הָאַרְכִּי: patah, hireq) at Ataroth (עֲטָרוֹת: hataf patah, qamets, holem); genitive plural |
| Ataroth-addar | *Atarothaddar* 16.5; *Atarothadar* 18.13 | עַטְרוֹת אַדָּר | — | *Atarōthadār* | Ataroth-addar: as 18:13 *Atarōthadār* (after the spelling change) / Ataroth-addar, Hebrew עַטְרוֹת אַדָּר: patah, holem, patah, qamets; *-adār* as the settled Num 34:4 *Hazaradār* |
| Ataroth | *Atharotha* 16.7 | עֲטָרוֹתָה | — | *Athārōtha* | Ataroth (Ephraim), Hebrew עֲטָרוֹתָה: hataf patah, qamets, holem |
| Japhletite | *Jephleti* 16.3 | הַיַּפְלֵטִי | — | *Jephlētī* | Japhletite, Hebrew הַיַּפְלֵטִי: patah, tsere, hireq-yod |
| Beth-horon | *Bethoronis* 16.3; *Bethoronem* 16.5,21.22; *Bethoroni* 18.13,18.14 | בֵּית־חוֹרֹן | Βαιθωρών | *Bēthōrōnis*, *Bēthōrōnem*, *Bēthōrōnī* | Beth-horon, Hebrew בֵּית־חוֹרֹן: tsere-yod, holem, holem; Greek Βαιθωρών ω / Beth-horon: as 16:3 *Bēthōrōnis* / Beth-horon: as 16:3 *Bēthōrōnis*; dative -ī |
| Gezer | *Gazer* 16.3,21.22 | גֶּזֶר | — | *Gazer* | Gezer, Hebrew גֶּזֶר: segol, segol |
| the men of Gezer | *Gazerenses* 16.10; *Gazerensesque* 16.10 | — | — | *Gazerēnsēs*, *Gazerēnsēsque* | the men of Gezer: Gezer (Hebrew segol, segol); -ēnsis / the men of Gezer: as *Gazerēnsēs* |
| Manassites | *Manassenses* 16.4,17.10,17.11,17.12,17.17 | — | — | *Manassēnsēs* | Manassites, settled *Manassēns-* (Num 1:10) |
| Manassite | *Manassensibus* 17.9 | — | — | *Manassēnsibus* | Manassite (adjective), settled *Manassēns-* |
| Michmethah | *Machmetam* 16.6; *Machmatam* 17.7 | הַמִּכְמְתָת | — | *Machmetam* | Michmethah, Hebrew הַמִּכְמְתָת: hireq, shewa; -am the accusative / Michmethah: as 16:6 *Machmetam* (after the spelling change) |
| Taanath-shiloh | *Tanathsiluntem* 16.6 | תַּאֲנַת | — | *Tanathsīlūntem* | Taanath-shiloh: Hebrew תַּאֲנַת patah; *Sīlūnt-* as Shiloh (18:1) |
| Shiloh | *Silunte* 22.9; *Siluntem* 18.1,18.8,18.9,19.51,21.2,22.12 | — | Σηλώ | *Sīlūnte*, *Sīlūntem* | Shiloh, Greek Σηλώ η, ω (decision 52's order); declined as *Hierichūs, -ūntis* |
| Janohah | *Janoam* 16.6; *Janoa* 16.7 | יָנוֹחָה | — | *Jānōam*, *Jānōā* | Janohah, Hebrew יָנוֹחָה: qamets, holem; -am the accusative / Janohah: as 16:6 *Jānōam*; ablative after *Ā* |
| Naarath | *Naaratham* 16.7 | נַעֲרָתָה | — | *Naarātham* | Naarath, Hebrew נַעֲרָתָה: patah, hataf patah, qamets |
| Kanah | *Canam* 16.8,17.9; *Canā* 19.28 | קָנָה | — | *Cānam*, *Cāna* | Kanah (the brook), Hebrew קָנָה: qamets; -am the accusative / Kanah (Asher), Hebrew קָנָה: qamets; nominative in the list |
| Bashan | *Basanamque* 17.1 | — | — | *Bāsānamque* | Bashan, settled Num 21:33 *Bāsānam* |
| Gilead | *Galaaditide* 20.8,21.38,22.32 | — | — | *Galaadītide* | Gilead, settled Num 32:40 *Galaadītidem*; ablative |
| Abiezer | *Abiezere* 17.2 | אֲבִיעֶזֶר | — | *Abīezere* | Abiezer, Hebrew אֲבִיעֶזֶר: hataf patah, hireq-yod, segol, segol |
| Helek | *Heleco* 17.2 | — | — | *Hēlecō* | Helek, settled Num 26:30 *Hēlecus* |
| Asriel | *Esriele* 17.2 | — | — | *Asrīēle* | Asriel, settled Num 26:31 *Asrīēl* (after the spelling change) |
| Shechem son of Gilead | *Sechemo* 17.2 | — | — | *Sechemō* | Shechem son of Gilead, settled Num 26:31 *Sechemus* |
| Hepher | *Hephre* 17.2 | — | — | *Hēphre* | Hepher, settled Num 26:33 *Hēphris* |
| Zelophehad | *Salphadus* 17.3 | — | — | *Salphaādus* | Zelophehad, settled Num 26:33 *Salphaādus* (after the spelling change) |
| Milcah | *Melcha* 17.3 | — | — | *Melca* | Milcah, settled Num 26:33, 27:1 *Melca* (after the spelling change) |
| Asherites | *Aserianis* 17.10,17.11,19.34 | — | — | *Āsēriānīs* | Asherites, settled *Āsēriān-* (Num 1:13) |
| Issacharites | *Issacharianis* 17.10,17.11,19.17 | — | — | *Issāchariānīs* | Issacharites, settled *Issāchariān-* (Num 1:8) |
| Beth-shean | *Bethsanem* 17.11; *Bethsane* 17.16 | בֵּית־שְׁאָן | — | *Bēthsānem*, *Bēthsāne* | Beth-shean, Hebrew בֵּית־שְׁאָן: tsere-yod, qamets / Beth-shean: as 17:11 *Bēthsānem* |
| Ibleam | *Jeblaamam* 17.11 | יִבְלְעָם | — | *Jeblaāmam* | Ibleam, Hebrew יִבְלְעָם: hireq, shewa, qamets; -am the accusative |
| the men of Endor | *Endorios* 17.11 | עֵין־דֹּר | — | *Ēndōriōs* | the men of Endor, Hebrew עֵין־דֹּר: tsere-yod, holem; -ius (as *Dōriōs*) |
| the men of Taanach | *Tanacenses* 17.11 | תַּעְנַךְ | — | *Tanacēnsēs* | the men of Taanach, Hebrew תַּעְנַךְ: patah, patah; -ēnsis |
| the men of Megiddo | *Magedonenses* 17.11 | מְגִדּוֹ | — | *Mageddōnēnsēs* | the men of Megiddo, Hebrew מְגִדּוֹ: shewa, hireq, holem; -ēnsis (after the spelling change, dd as 12:21 *Mageddonis*) |
| Taanach | *Thanach* 21.25 | תַּעְנַךְ | — | *Thanach* | Taanach, Hebrew תַּעְנַךְ: patah, patah |
| Beth-aven | *Bethavenis* 18.12 | בֵּית אָוֶן | — | *Bēthāvenis* | Beth-aven, Hebrew בֵּית אָוֶן: tsere-yod, qamets, segol |
| Geliloth | *Gelilotha* 18.17 | גְּלִילוֹת | — | *Gelīlōtha* | Geliloth, Hebrew גְּלִילוֹת: shewa, hireq-yod, holem |
| Keziz | *Cāsīs* 18.21 | קְצִיץ | — | *Casīs* | Keziz (Emek-keziz), Hebrew קְצִיץ: shewa, hireq-yod (the preview's first ā is the lexicon's *cāsus*) |
| Zemaraim | *Samaraim* 18.22 | צְמָרַיִם | — | *Samāraim* | Zemaraim, Hebrew צְמָרַיִם: shewa, qamets, patah, hireq |
| Avim | *Avim* 18.23 | הָעַוִּים | — | *Avīm* | Avim, Hebrew הָעַוִּים: patah, hireq-yod |
| Parah | *Parā* 18.23 | הַפָּרָה | — | *Pāra* | Parah, Hebrew הַפָּרָה: qamets; nominative in the list |
| Ophrah | *Ophra* 18.23 | עָפְרָה | — | *Ophra* | Ophrah, Hebrew עָפְרָה: qamets hatuf |
| Chephar-haammonai | *Cepharammonai* 18.24 | כְּפַר הָעַמֹּנִי | — | *Cepharammōnai* | Chephar-haammonai, Hebrew כְּפַר הָעַמֹּנִי: shewa, patah, patah, holem |
| Ophni | *Ophni* 18.24 | הָעָפְנִי | — | *Ophnī* | Ophni, Hebrew הָעָפְנִי: qamets hatuf, hireq-yod |
| Geba | *Gaba* 18.24; *Gabam* 21.17 | גֶּבַע | — | *Gaba*, *Gabam* | Geba, Hebrew גֶּבַע: segol, patah; nominative / Geba: as 18:24 *Gaba* |
| Gibeon | *Gabaōn* 18.25; *Gabaonem* 21.17 | — | — | *Gabaōn*, *Gabaōnem* | Gibeon, Gaffiot *Găbăōn* |
| Ramah | *Rama* 18.25; *Ramam* 19.29; *Harama* 19.36 | הָרָמָה | — | *Rāma*, *Rāmam*, *Harāma* | Ramah (Benjamin), Hebrew הָרָמָה: qamets; nominative -a (the settled Matt 2:18 *Ramam*, unmarked: see notes) / Ramah (Asher), Hebrew הָרָמָה: qamets; -am the accusative / Ramah (Naphtali), Hebrew הָרָמָה: qamets; nominative -a |
| Beeroth | *Beerota* 18.25 | — | Βηρώτ | *Bērōtha* | Beeroth: as N1's 9:17 *Bērōtha* (Greek Βηρώτ η, ω; the settled *Bērōthīs*) (after the spelling change) |
| Chephirah | *Caphara* 18.26 | הַכְּפִירָה | — | *Caphīra* | Chephirah, Hebrew הַכְּפִירָה: shewa, hireq-yod (after the spelling change, as 9:17 *Caphira*) |
| Mozah | *Mosa* 18.26 | הַמֹּצָה | — | *Mōsa* | Mozah, Hebrew הַמֹּצָה: holem (Gaffiot's *Mŏsa* is the Meuse) |
| Rekem | *Recem* 18.27 | רֶקֶם | — | *Recem* | Rekem, Hebrew רֶקֶם: segol, segol; settled Num 31:8 *Recemum* (unmarked) |
| Irpeel | *Jarephel* 18.27 | יִרְפְּאֵל | — | *Jarephēl* | Irpeel, Hebrew יִרְפְּאֵל: hireq, shewa, tsere |
| Taralah | *Tharela* 18.27 | תַּרְאֲלָה | — | *Tharela* | Taralah, Hebrew תַּרְאֲלָה: patah, hataf patah |
| Zelah | *Selā* 18.28 | צֵלַע | — | *Sēla* | Zelah, Hebrew צֵלַע: tsere, patah; nominative in the list |
| Eleph | *Eleph* 18.28 | הָאֶלֶף | — | *Eleph* | Eleph, Hebrew הָאֶלֶף: segol, segol |
| Kirjath | *Cariāthaim* 18.28 | קִרְיַת | — | *Cariathaim* | Kirjath, Hebrew קִרְיַת: hireq, patah (not Kiriathaim, the settled *Cariāthaim* of Num 32:37: see notes) |
| Sheba | *Saba* 19.2 | שֶׁבַע | — | *Saba* | Sheba, Hebrew שֶׁבַע: segol, patah (Gaffiot's *Săba* is Saba of Arabia) |
| Balah | *Bālā* 19.3 | בָּלָה | — | *Bāla* | Balah, Hebrew בָּלָה: qamets; nominative in the list |
| Bethul | *Bethul* 19.4 | בְּתוּל | — | *Bethūl* | Bethul, Hebrew בְּתוּל: shewa, shureq |
| Beth-marcaboth | *Bethmarcaboth* 19.5 | בֵּית־הַמַּרְכָּבוֹת | — | *Bēthmarcābōth* | Beth-marcaboth, Hebrew בֵּית־הַמַּרְכָּבוֹת: tsere-yod, patah, qamets, holem |
| Hazar-susah | *Hasersusa* 19.5 | חֲצַר סוּסָה | — | *Hasersūsa* | Hazar-susah, Hebrew חֲצַר סוּסָה: hataf patah, patah, shureq |
| Sharuhen | *Sarohen* 19.6 | שָׁרוּחֶן | — | *Sārōhen* | Sharuhen, Hebrew שָׁרוּחֶן: qamets, shureq, segol |
| Baalath-beer | *Baalath* 19.8 | בַּעֲלַת | — | *Baalath* | Baalath-beer, Hebrew בַּעֲלַת: patah, hataf patah, patah |
| Beer | *Beerramath* 19.8 | בְּאֵר רָאמַת | — | *Beērrāmath* | Beer, Ramath (Baalath-beer, Ramath of the south), Hebrew בְּאֵר רָאמַת: shewa, tsere, qamets, patah |
| Baalath | *Balaath* 19.44 | בַּעֲלָת | — | *Balaāth* | Baalath (Dan), Hebrew בַּעֲלָת: patah, hataf patah, qamets |
| Zebulun | *Zabulōnis* 21.7,21.34 | — | — | *Zabulōnis* | Zebulun, settled Num 1:30 *Zabulōnis* |
| Zebulunites | *Zabulonios* 19.27 | — | — | *Zabulōniōs* | Zebulunites, settled *Zabulōni-* (Num 7:12) |
| Sarid | *Sarid* 19.10; *Saride* 19.12 | שָׂרִיד | — | *Sārīd*, *Sārīde* | Sarid, Hebrew שָׂרִיד: qamets, hireq-yod / Sarid: as 19:10 *Sārīd* |
| Maralah | *Marealam* 19.11 | מַרְעֲלָה | — | *Marealam* | Maralah, Hebrew מַרְעֲלָה: patah, hataf patah; -am the accusative |
| Dabbasheth | *Debaseth* 19.11 | דַּבָּשֶׁת | — | *Debāseth* | Dabbasheth, Hebrew דַּבָּשֶׁת: patah, qamets, segol |
| Jokneam | *Jeconam* 19.11; *Jecanam* 21.34 | יָקְנְעָם | — | *Jeconām* | Jokneam, Hebrew יָקְנְעָם: qamets hatuf, shewa, qamets / Jokneam: as 19:11 *Jeconām* (after the spelling change) |
| Chisloth-tabor | *Cheselethaboris* 19.12 | כִּסְלֹת תָּבֹר | — | *Cheselēthābōris* | Chisloth-tabor, Hebrew כִּסְלֹת תָּבֹר: hireq, holem, qamets, holem (*Cheseleth* + *Thaboris*, one th) |
| Daberath | *Dabereth* 19.12,21.28 | הַדָּבְרַת | — | *Dābereth* | Daberath, Hebrew הַדָּבְרַת: qamets, patah |
| Japhia | *Japhiam* 19.12 | יָפִיעַ | — | *Jāphīam* | Japhia, Hebrew יָפִיעַ: qamets, hireq-yod; -am the accusative |
| Gath-hepher | *Gethepher* 19.13 | גִּתָּה חֵפֶר | — | *Gethēpher* | Gath-hepher, Hebrew גִּתָּה חֵפֶר: tsere, segol |
| Ittah | *Ittam* 19.13 | עִתָּה | — | *Ittam* | Ittah (Ittah-kazin), Hebrew עִתָּה: hireq; -am the accusative |
| Kazin | *Casin* 19.13 | קָצִין | — | *Cāsīn* | Kazin (Ittah-kazin), Hebrew קָצִין: qamets, hireq-yod |
| Methoar | *Methoar* 19.13 | הַמְּתֹאָר | — | *Methōār* | Methoar, Hebrew הַמְּתֹאָר: holem, qamets |
| Neah | *Neam* 19.13 | הַנֵּעָה | — | *Nēam* | Neah, Hebrew הַנֵּעָה: tsere; -am the accusative |
| Hannathon | *Nathonem* 19.14 | חַנָּתֹן | — | *Nathōnem* | Hannathon, Hebrew חַנָּתֹן: patah, holem |
| Jiphthah-el | *Jephthahelis* 19.14; *Jephthælis* 19.27 | יִפְתַּח־אֵל | — | *Jephthahēlis* | Jiphthah-el, Hebrew יִפְתַּח־אֵל: hireq, patah, tsere / Jiphthah-el: as 19:14 *Jephthahēlis* (after the spelling change) |
| Kattath | *Cateth* 19.15 | קַטָּת | — | *Catēth* | Kattath, Hebrew קַטָּת: patah, qamets |
| Nahalal | *Nahalol* 19.15,21.35 | נַהֲלָל | — | *Nahalōl* | Nahalal, Hebrew נַהֲלָל: patah, hataf patah, qamets |
| Shimron | *Semeron* 19.15 | שִׁמְרוֹן | — | *Semerōn* | Shimron, Hebrew שִׁמְרוֹן: hireq, holem |
| Idalah | *Idala* 19.15 | יִדְאֲלָה | — | *Idala* | Idalah, Hebrew יִדְאֲלָה: hireq, hataf patah |
| Bethlehem | *Bēthlehēma* 19.15 | בֵּית לֶחֶם | — | *Bēthlehema* | Bethlehem (Zebulun), Hebrew בֵּית לֶחֶם: tsere-yod, segol, segol; as the settled Luke 2:4 *Bēthlehema* |
| Chesulloth | *Casaloth* 19.18 | הַכְּסוּלֹת | — | *Casālōth* | Chesulloth, Hebrew הַכְּסוּלֹת: shewa, shureq, holem |
| Shunem | *Sunem* 19.18 | שׁוּנֵם | — | *Sūnēm* | Shunem, Hebrew שׁוּנֵם: shureq, tsere |
| Hapharaim | *Hapharaim* 19.19 | חֲפָרַיִם | — | *Haphāraim* | Hapharaim, Hebrew חֲפָרַיִם: hataf patah, qamets, patah, hireq |
| Shion | *Seon* 19.19 | שִׁיאֹן | — | *Sēōn* | Shion, Hebrew שִׁיאֹן: hireq-yod, holem |
| Anaharath | *Anaharath* 19.19 | אֲנָחֲרַת | — | *Anāharath* | Anaharath, Hebrew אֲנָחֲרַת: hataf patah, qamets, hataf patah, patah |
| Rabbith | *Rabbith* 19.20 | הָרַבִּית | — | *Rabbīth* | Rabbith, Hebrew הָרַבִּית: patah, hireq-yod |
| Kishion | *Cesion* 19.20,21.28 | קִשְׁיוֹן | — | *Cesiōn* | Kishion, Hebrew קִשְׁיוֹן: hireq, holem |
| Abez | *Abes* 19.20 | אָבֶץ | — | *Ābes* | Abez, Hebrew אָבֶץ: qamets, segol |
| Remeth | *Rameth* 19.21 | רֶמֶת | — | *Rameth* | Remeth, Hebrew רֶמֶת: segol, segol |
| En-haddah | *Enhadda* 19.21 | עֵין חַדָּה | — | *Ēnhadda* | En-haddah, Hebrew עֵין חַדָּה: tsere-yod, patah |
| Beth-pazzez | *Bethpheses* 19.21 | בֵּית פַּצֵּץ | — | *Bēthphesēs* | Beth-pazzez, Hebrew בֵּית פַּצֵּץ: tsere-yod, patah, tsere |
| Tabor | *Tabor* 19.22 | תָּבוֹר | — | *Tābōr* | Tabor, Hebrew תָּבוֹר: qamets, holem |
| Aznoth-tabor | *Azanothabor* 19.34 | אַזְנוֹת תָּבוֹר | — | *Azanōthābōr* | Aznoth-tabor, Hebrew אַזְנוֹת תָּבוֹר: patah, holem, qamets, holem |
| Shahazimah | *Sehesimam* 19.22 | שַׁחֲצִימָה | — | *Sehesīmam* | Shahazimah, Hebrew (qere) שַׁחֲצִימָה: patah, hataf patah, hireq-yod; -am the accusative |
| Helkath | *Halcath* 19.25; *Helcath* 21.31 | חֶלְקַת | — | *Helcath* | Helkath: as 21:31 *Helcath* (after the spelling change) / Helkath, Hebrew חֶלְקַת: segol, patah |
| Beten | *Beten* 19.25 | בֶטֶן | — | *Beten* | Beten, Hebrew בֶטֶן: segol, segol |
| Achshaph | *Axaph* 19.25 | אַכְשָׁף | — | *Axāph* | Achshaph, Hebrew אַכְשָׁף: patah, qamets |
| Alammelech | *Elmelech* 19.26 | אַלַמֶּלֶךְ | — | *Elmelech* | Alammelech, Hebrew אַלַמֶּלֶךְ: patah, patah, segol |
| Amad | *Amaad* 19.26 | עַמְעָד | — | *Amaād* | Amad, Hebrew עַמְעָד: patah, qamets |
| Misheal | *Messal* 19.26,21.30 | מִשְׁאָל | — | *Messāl* | Misheal, Hebrew מִשְׁאָל: hireq, qamets |
| Shihor | *Sihor* 19.26 | שִׁיחוֹר | — | *Sīhōr* | Shihor (Shihor-libnath), Hebrew שִׁיחוֹר: hireq-yod, holem |
| Libnath | *Labanath* 19.26 | לִבְנָת | — | *Labanāth* | Libnath (Shihor-libnath), Hebrew לִבְנָת: hireq, qamets |
| Beth-emek | *Bethemec* 19.27 | בֵּית הָעֵמֶק | — | *Bēthēmec* | Beth-emek, Hebrew בֵּית הָעֵמֶק: tsere-yod, tsere, segol |
| Neiel | *Nehiel* 19.27 | נְעִיאֵל | — | *Nehīēl* | Neiel, Hebrew נְעִיאֵל: shewa, hireq-yod, tsere |
| Cabul | *Cabul* 19.27 | כָּבוּל | — | *Cābūl* | Cabul, Hebrew כָּבוּל: qamets, shureq |
| Hebron | *Ebron* 19.28 | עֶבְרֹן | — | *Ebrōn* | Hebron (Asher), Hebrew עֶבְרֹן: segol, holem |
| Hosah | *Hosam* 19.29 | חֹסָה | — | *Hōsam* | Hosah, Hebrew חֹסָה: holem; -am the accusative |
| Ummah | *ammam* 19.30 | עֻמָה | — | *Ammam* | Ummah (capital: the layout row), Hebrew עֻמָה: qibbuts; -am the accusative |
| Heleph | *Heleph* 19.33 | חֵלֶף | — | *Hēleph* | Heleph, Hebrew חֵלֶף: tsere, segol |
| Zaanannim | *Saanannim* 19.33 | צַעֲנַנִּים | — | *Saanannīm* | Zaanannim, Hebrew צַעֲנַנִּים: patah, hataf patah, patah, hireq-yod |
| Adami | *Ādamī* 19.33 | אֲדָמִי | — | *Adāmī* | Adami (Adami-nekeb), Hebrew אֲדָמִי: hataf patah, qamets, hireq-yod (the preview's Ā is Gaffiot's *Ādamus*, Adam) |
| Nekeb | *Neceb* 19.33 | הַנֶּקֶב | — | *Neceb* | Nekeb (Adami-nekeb), Hebrew הַנֶּקֶב: segol, segol |
| Lakum | *Lecum* 19.33 | לַקּוּם | — | *Lecūm* | Lakum, Hebrew לַקּוּם: patah, shureq |
| Hukkok | *Hucuca* 19.34 | חוּקֹקָה | — | *Hūcūca* | Hukkok, Hebrew חוּקֹקָה: shureq, holem; nominative -a |
| Ziddim | *Sedim* 19.35 | הַצִּדִּים | — | *Sedīm* | Ziddim, Hebrew הַצִּדִּים: hireq, hireq-yod |
| Hammath | *Hemath* 19.35 | חַמַּת | — | *Hemath* | Hammath (Naphtali), Hebrew חַמַּת: patah, patah (not Hamath, the settled *Hemātham*) |
| Rakkath | *Reccath* 19.35 | רַקַּת | — | *Reccath* | Rakkath, Hebrew רַקַּת: patah, patah |
| Chinnereth | *Cenereth* 19.35 | — | — | *Cenereth* | Chinnereth, settled Num 34:11 *Cenerethī* |
| Adamah | *adamā* 19.36 | אֲדָמָה | — | *Adāma* | Adamah (capital: the layout row), Hebrew אֲדָמָה: hataf patah, qamets; nominative in the list |
| Edrei | *Hedrei* 19.37 | אֶדְרֶעִי | — | *Hedreī* | Edrei (Naphtali), Hebrew אֶדְרֶעִי: segol, segol, hireq-yod (settled *Edreī*, Num 21:33, is Edrei of Bashan) |
| Iron | *Jereon* 19.38 | יִרְאוֹן | — | *Jereōn* | Iron, Hebrew יִרְאוֹן: hireq, holem |
| Migdal-el | *Magdæl* 19.38 | מִגְדַּל־אֵל | — | *Magdæl* | Migdal-el, Hebrew מִגְדַּל־אֵל (the æ as printed) |
| Horem | *Hōrem* 19.38 | חֳרֵם | — | *Horēm* | Horem, Hebrew חֳרֵם: hataf qamets (short), tsere |
| Naphtalites | *Nephthalensium* 19.39 | — | — | *Nephthālēnsium* | Naphtalites, settled *Nephthālēns-* (Deut 27:13) |
| Naphtalite | *Nephthalensi* 20.7 | — | — | *Nephthālēnsī* | Naphtalite (adjective), settled *Nephthālēns-* |
| Shaalabbin | *Selebim* 19.42 | שַׁעֲלַבִּין | — | *Selebīm* | Shaalabbin, Hebrew שַׁעֲלַבִּין: patah, hataf patah, patah, hireq-yod |
| Aijalon | *Ajalon* 19.42; *Ajalonem* 21.24 | אַיָּלוֹן | — | *Ajālōn*, *Ajālōnem* | Aijalon, Hebrew אַיָּלוֹן: patah, qamets, holem / Aijalon: as 19:42 *Ajālōn* |
| Jethlah | *Jethalo* 19.42 | יִתְלָה | — | *Jethalō* | Jethlah, Hebrew יִתְלָה: hireq, qamets |
| Elon | *Elon* 19.43 | אֵילוֹן | — | *Ēlōn* | Elon, Hebrew אֵילוֹן: tsere-yod, holem |
| Gibbethon | *Gebbethon* 19.44; *Gabathonem* 21.23 | גִּבְּתוֹן | — | *Gebbethōn*, *Gebbethōnem* | Gibbethon, Hebrew גִּבְּתוֹן: hireq, shewa, holem / Gibbethon: as 19:44 *Gebbethōn* (after the spelling change) |
| Jehud | *Jehud* 19.45 | יְהֻד | — | *Jehud* | Jehud, Hebrew יְהֻד: shewa, qibbuts |
| Bene-berak | *Banebarac* 19.45 | בְּנֵי־בְרַק | — | *Banēbarac* | Bene-berak, Hebrew בְּנֵי־בְרַק: shewa, tsere-yod, shewa, patah |
| Gath-rimmon | *Gethremmon* 19.45; *Gethremmonem* 21.24,21.25 | גַּת־רִמּוֹן | — | *Gethremmōn*, *Gethremmōnem* | Gath-rimmon, Hebrew גַּת־רִמּוֹן: patah, hireq, holem / Gath-rimmon: as 19:45 *Gethremmōn* |
| Me-jarkon | *Mejercon* 19.46 | מֵי הַיַּרְקוֹן | — | *Mējercōn* | Me-jarkon, Hebrew מֵי הַיַּרְקוֹן: tsere-yod, patah, holem |
| Rakkon | *Raccon* 19.46 | הָרַקּוֹן | — | *Raccōn* | Rakkon, Hebrew הָרַקּוֹן: patah, holem |
| Leshem | *Lesemam* 19.47 | לֶשֶׁם | — | *Lesemam* | Leshem, Hebrew לֶשֶׁם: segol, segol; -am the accusative |
| Bezer | *Bosor* 20.8,21.36 | — | — | *Beser* | Bezer, settled Deut 4:43 *Beser* (after the spelling change) |
| Reubenites | *Rubenenses* 18.7; *Rubenitas* 22.11,22.25 | — | — | *Rūbēnēnsēs*, *Rūbēnītās* | Reubenites, settled *Rūbēnēns-* (Num 2:16) / Reubenites, settled *Rūbēnīt-* (Num 16:1) |
| Reubenite | *Rubenensi* 20.8 | — | — | *Rūbēnēnsī* | Reubenite (adjective), settled *Rūbēnēns-* |
| Gadite | *Gadina* 20.8 | — | — | *Gadīnā* | Gadite (adjective), settled *Gadīn-*; ablative with *tribū* |
| Golan | *Gaulonem* 20.8; *Gaulon* 21.27 | גּוֹלָן | Γαυλών | *Gaulōnem*, *Gaulōn* | Golan, Hebrew גּוֹלָן: holem, qamets; Greek Γαυλών ω / Golan: as 20:8 *Gaulōnem* |
| Anathoth | *Anathotha* 21.18 | עֲנָתוֹת | — | *Anāthōtha* | Anathoth, Hebrew עֲנָתוֹת: hataf patah, qamets, holem |
| Kibzaim | *Cibsaim* 21.22 | קִבְצַיִם | — | *Cibsaim* | Kibzaim, Hebrew קִבְצַיִם: hireq, patah, hireq |
| Beeshterah | *Beestera* 21.27 | בְּעֶשְׁתְּרָה | — | *Beestera* | Beeshterah, Hebrew בְּעֶשְׁתְּרָה: shewa, segol, shewa |
| Abdon | *Abdon* 21.30 | עַבְדּוֹן | — | *Abdōn* | Abdon, Hebrew עַבְדּוֹן: patah, holem |
| Hammoth-dor | *Hammothor* 21.32 | חַמֹּת דֹּאר | — | *Hammōthōr* | Hammoth-dor, Hebrew חַמֹּת דֹּאר: patah, holem, holem |
| Kartan | *Carthan* 21.32 | קַרְתָּן | — | *Carthān* | Kartan, Hebrew קַרְתָּן: patah, qamets |
| Kartah | *Cartha* 21.34 | קַרְתָּה | — | *Cartha* | Kartah, Hebrew קַרְתָּה: patah |
| Dimnah | *damna* 21.35 | דִּמְנָה | — | *Damna* | Dimnah (capital: the layout row), Hebrew דִּמְנָה: hireq |
| Kedemoth | *Cedemotha* 21.37 | — | — | *Cedēmōtha* | Kedemoth, settled Deut 2:26 *Cedēmōthis* |
| Mephaath | *Mephaath* 21.37 | מֵיפָעַת | — | *Mēphāath* | Mephaath, Hebrew מֵיפָעַת: tsere-yod, qamets, patah |
| Jazer | *Jaser* 21.39 | — | — | *Jazēr* | Jazer, settled Num 21:32, 32:35 *Jazēr* (after the spelling change) |
| Gadites | *Gadinos* 22.11,22.25 | — | — | *Gadīnōs* | Gadites, settled *Gadīn-* (Num 32:1) |
| of Peor | *Phegorium* 22.17 | — | — | *Phegōrium* | of Peor (adjective), settled *Phegōr-* (Num 23:28); -ius |
| Achan | *Achan* 22.20 | עָכָן | Ἄχαρ | *Āchān* | Achan, Hebrew עָכָן: qamets, qamets (Gaffiot *Achan* unmarked; Greek Ἄχαρ no long letter) |
| Ed | *Ed* 22.34 | עֵד | — | *Ēd* | Ed, Hebrew עֵד: tsere |
| Terah | *Thara* 24.2 | — | — | *Thara* | Terah, settled Gen 11:26 *Thara* |
| Nahor | *Nachorisque* 24.2 | — | — | *Nachōrisque* | Nahor, settled Luke 3:34 *Nachōris* |
| beyond Jordan | *Transjordaninorum* 24.8 | — | — | *Trānsjordānīnōrum* | beyond Jordan (adjective), settled Deut 3:25 *Trānsjordānīnam* |
| Gaash | *Gaassi* 24.30 | גָּעַשׁ | — | *Gāassī* | Gaash, Hebrew גָּעַשׁ: qamets, patah; genitive -ī |
| Shechem | *Sichemæ* 24.25,24.32 | — | — | *Sichemæ* | Shechem, settled *Sichem-* (Gen 12:6 *Sichemam*); locative |
| Phinehas | *Phineis* 24.33 | — | — | *Phīneis* | Phinehas, settled *Phīnees*; genitive -is |
| Joshua | *Jōsua* 20.1; *Jōsua* 17.15,17.17,18.2,18.8,18.10,19.51,20.1,22.1,22.7,23.1,24.1,24.19,24.22,24.25,24.29 | — | — | *Jōsuā*, *Jōsua* | Joshua, settled *Jōsua*; ablative with *cum* / Joshua, settled *Jōsua*; nominative |
| Jahazah | *Jāsā* 21.36 | — | — | *Jāsa* | Jahazah, settled Num 21:23 *Jāsam*, Deut 2:32 *Jāsā*; nominative in the list (*Beser, Jāsa*) |

---

## Evidence re-checked for "For you" points 3 and 4 (Claude, 2026-11-19)

Nathan, 2026-11-19: "Explain the evidence for your recommendations for 3 and 4, point by point. Consider consistency
within the edited work, the original Hebrew transliterations (and Greek for support), taking careful note of long
vowels in the original language(s)." Every Hebrew form below is the WLC's in the verse (`sources/parallel/wlc/`, read
with its meteg), the Greek Brenton's in the same verse, the settled forms from `data/gold/`; 1554 (MDZ bsb10196330)
and 1573 (bsb10141277) from their OCR search, page images seen where marked. Long in the Hebrew: qamets gadol, tsere,
holem, hireq-yod, shureq; short: patah, segol, qibbuts, qamets hatuf (a closed unaccented syllable, no meteg); none:
shewa.

**Applied** (Nathan, 2026-11-19: "Apply all seven"; decision 82): the seven revisions (12:22 *Jeconām*, *Saraa*,
*Cedes*, *Thamnathser-*, *Thanach*/*Thanachēnsēs*, *Jerimōth-*, *Gaza* with the settled *Gāzam*): spelling items 58
(revised), 62–65 in `josh1-24-stage2.md`, 20 forms rows, two layout rows, `gaza-short.md`. *Cālēbus* by the Hebrew
applied too (Nathan: "Yes, Cālēbus"; decision 83; `caleb-long.md`).

### 3a. The settled spelling over 1738's (same person or place)

| Verse | 1738 → edited | Hebrew | Greek | Settled / other printings | Verdict |
|---|---|---|---|---|---|
| 20:8, 21:36 | *Bosor → Beser* | בֶּצֶר segol, segol (short) | Βοσόρ | Deut 4:43 *Beser*, the same list of refuge cities | holds; *Bosor* is the Greek's and Vulgate's |
| 15:14 | *Sesaim → Sēsæum* | שֵׁשַׁי tsere, patah | Σουσί | Num 13:22 *Sēsæus* (the same three sons of Anak) | holds |
| 15:14 | *Tholmaim → Thalmæum* | תַּלְמַי patah, patah | Θολαμί | Num 13:22 *Thalmæus* | holds; 1738's *o* is the Greek's |
| 2:1, 3:1 | *Setimo → Sittīmō* | הַשִּׁטִּים hireq + doubled ṭ, hireq-yod | Σαττίν | Num 25:1 *Sittīmō*, 33:49 *Sittīmōrum* | holds; *tt* the dagesh, *ī* the hireq-yod |
| 13:20 | *Bethphogor → Bēthphegōr* | בֵּית פְּעוֹר tsere-yod; shewa, holem | Βαιθφογώρ | Deut 34:6 *Bēthphegōr*, *Phegōr-* 9 times | holds; 1738's *o* is the Greek's |
| 17:2 | *Esriele → Asrīēle* | אַשְׂרִיאֵל patah, hireq-yod, tsere | (not in the list) | Num 26:31 *Asrīēl*, *Asrīēlīna* | holds; *E* has no Hebrew ground |
| 17:3 | *Salphadus → Salphaādus* | צְלָפְחָד shewa, qamets, qamets | Σαλπαάδ | Num 26:33 *Salphaādus*, *Salphaādī* 6 times | holds |
| 17:3 | *Melcha → Melca* | מִלְכָּה hireq, kaph with dagesh, qamets | Μελχά | Num 26:33, 27:1, 36:11 *Melca* | holds; *ch* is the Greek's χ |
| 18:13 | *Lusæ → Lūzæ* | לוּזָה shureq | Λουζά | Gen 48:3 *Lūzæ*, Gen 35:6 and Josh 16:2 *Lūzam* | holds (settled slip: Gen 28:19 *Luza* lacks its ū) |
| 21:39 | *Jaser → Jazēr* | יַעְזֵר patah, tsere | Ἰαζήρ | Num 21:32, 32:3, 32:35 *Jazēr*; Josh 13:25 *Jazer* | holds |
| 24:32 | *Josephæis → Jōsēphēīs* | יוֹסֵף holem, tsere | Ἰωσήφ | Deut 27:12 *Jōsēphēī*; Josh 18:11 *Josepheos* (1738) | holds |
| 21:12 | *Chalebo → Calebō* | כָּלֵב qamets, tsere (both long) | Χάλεβ | *Calebus/-ō/-um* 10 times (Num, Deut), short; 1738's own 15:13, 15:18 *Calebo* | spelling holds; **the marks are against the Hebrew** (below) |
| 15:4 | *Asemonem → Asmōnem* | עַצְמוֹנָה patah, silent shewa, holem | Σελμωνά | Num 34:4 *Asmōnem*, 34:5 *Asmōne* | holds |
| 15:30 | *Harma → Horma* | חָרְמָה qamets hatuf (no meteg) | Ἑρμά | *Hormam* 3 times; Josh 19:4 *Horma*, 12:14 *Hormæ* | holds; o short |
| 12:5, 13:11 | *Salecham → Salcham* | סַלְכָה patah, silent shewa | Σεκχαί | Deut 3:10 *Salcham* | holds |
| 12:5, 13:11, 13:13 | *maachathæ- → maachātæ-* | הַמַּעֲכָתִי patah, hateph patah, qamets, hireq-yod | Μαχατί | Deut 3:14 *Maachātis* | holds by the settled form (the Hebrew's soft ת would allow *th*) |
| 13:18 | *Cedemothia → Cedēmōtha* | קְדֵמֹת shewa, tsere, holem | Βακεδμώθ | Deut 2:26 *Cedēmōthis*; Josh 21:37 *Cedemotha* | holds; the *i* has no Hebrew ground |
| 13:18 | *Jassa → Jāsa* | יַהְצָה patah here; יָהְצָה qamets (pausal) Num 21:23, Deut 2:32 | Ἰασσά (Deut 2:32) | Num 21:23 *Jāsam*, Deut 2:32 *Jāsā*; Josh 21:36 *Jasa* | holds; no dagesh in ṣ, so one s; the ā has the Hebrew's pausal qamets |
| 13:3 | *Acharonis → Accarōnis* | עֶקְרוֹן segol, holem | Ἀκκαρών | Joshua's *Accaron* 4 times (1573 the same), *accaronensis* in this verse | holds |
| 11:1 | *Someronis → Semerōnis* | שִׁמְרוֹן hireq, silent shewa, holem | Συμοών | Joshua's 19:15 *Semeron*, 12:20 *Semeromeronis* | holds |
| 12:22 | *Cadis → Cedis* | קֶדֶשׁ segol, segol | (Brenton's list differs) | *Cadis* in 1554, 1573 and 1738 alike; Castellio's *Cedes* 15:23, 19:37, 21:32, *Cedesam* 20:7 | holds as one spelling for one place (*Cadis* looks like Kadesh, קָדֵשׁ, the settled *Cadēs*); but Castellio printed it in every edition |

**Kedesh's mark, revised**: 15:23, 19:37, 21:32 *Cedēs* and 20:7 *Cedēsam* took ē from the Greek Κάδης (decision 52's
order). The Hebrew has two short segols in all five places, and the Greek itself has Κάδες at 19:37. By the Hebrew:
*Cedes, Cedesam*, unmarked, as *Cedis*.

**Caleb's marks**: the Hebrew has two long vowels (qamets, tsere); the settled *Calebus* is short by Wiktionary's bare
*Caleb* and the Greek's lack of a long letter (Numbers' forms rows: "the preview had *Calēbus*"). By the Hebrew:
*Cālēbus*, in the settled Numbers and Deuteronomy as well as Joshua.

### 3b. One spelling within Joshua

| Verses | Chosen (alternative) | Hebrew | Evidence | Verdict |
|---|---|---|---|---|
| 15:7, 18:17 | *Adommīm* (*Adumim*) | אֲדֻמִּים hateph patah, qibbuts + doubled m, hireq-yod | 1738 18:17, the Vulgate both times | holds: mm the dagesh, ī the hireq-yod |
| 15:28, 19:3 | *Hasersūāl* (*Hazersual*) | חֲצַר שׁוּעָל hateph patah, patah; shureq, qamets | s for ṣ as Castellio's *Hasor*, *Hasergadda* | holds |
| 15:29, 19:3 | *Āsem* (*Ezem*) | וָעָצֶם qamets, segol in both verses | Greek Ἀσόμ (15:29) | holds: *A* and ā from the qamets |
| 15:32, 19:7, 21:16 | *Ain* (*Aen*) | עַיִן patah, hireq | Num 34:11 *Ainis* | holds |
| 15:33, 19:41 | *Saraa* (*Sarea*) | צָרְעָה qamets **hatuf** (no meteg; KJV *Zorah*), qamets | Castellio's *Saraa* at 19:41 (1554, 1573, 1738) and Judges 13:2, 16:31, 18:2, 18:11 (1554 or 1573, OCR); *Sarea* at 15:33 only (1554, 1573, 1738) | spelling holds; **mark revised**: *Sāraa* → *Saraa*, short, as *Horma* (the same hatuf) |
| 15:42, 19:7 | *Āsān* (*Assan*) | עָשָׁן qamets, qamets; no dagesh in ש | Greek Ἀσάν | holds: one s |
| 15:48, 21:14 | *Jattīr* (*Jatthir*) | יַתִּיר / יַתִּר patah, doubled t, hireq(-yod) | | holds: the dagesh gives tt, not tth |
| 15:60 | *Cariathjārīm* (*Cariathiarim*) | יְעָרִים shewa, qamets, hireq-yod | 15:9, 18:14, 18:15 | holds |
| 16:5, 18:13 | *Atarōthadār* (*Atarothaddar*) | אַדָּר patah, **doubled d**, qamets | 1573 and 1738: 16:5 *Atarothaddar*, 18:13 *Atarothadar*; 15:3 *Adar* (אַדָּרָה); the settled Num 34:4 *Hazaradār* (חֲצַר־אַדָּר, the same dagesh) | holds by the settled form and 3 of 4; the Hebrew alone gives dd |
| 16:6, 17:7 | *Machmetam* (*Machmatam*) | מִכְמְתָת hireq, shewa, qamets | | holds: *e* for the shewa |
| 19:25, 21:31 | *Helcath* (*Halcath*) | חֶלְקַת segol, patah | Greek Χελκάτ (21:31) | holds |
| 19:14, 19:27 | *Jephthahēlis* (*Jephthaelis*) | יִפְתַּח־אֵל hireq, patah, ḥ; tsere | | holds |
| 19:44, 21:23 | *Gebbethōn* (*Gabathonem*) | גִּבְּתוֹן hireq + doubled b, shewa, holem | 1573 19:44 *Gebbethon* | holds |
| 19:11, 21:34 | *Jeconām* (*Jecanam*) | יָקְנְעָם qamets hatuf, shewa, shewa, qamets | Castellio's own two: 1573 19:11 *Ieconam*, 21:34 *Iecanam* (both seen) | holds: *o* is the Hebrew's, ā its last qamets |
| 19:50, 24:30 | *Thamnathsar-* (*Thannathser-*) | תִּמְנַת־סֶרַח hireq, patah; **segol**, patah | 19:50 *Thamnathsaram* (1554, 1738); 24:30 *Thānathserę* (1573, seen: the tilde stands for m or n), *Thannathseræ* (1738), *Thamnathserae* (Wikisource); Greek Θαμνασαράχ | **revised**: the Hebrew's segol is 24:30's *e*, its mem 19:50's *m*: *Thamnathser-* in both (19:50 *Thamnathseram*, 24:30 *Thamnathseræ*) |
| 15:41 | *Macēda* (*Macceda*) | מַקֵּדָה patah, **doubled k**, tsere | Castellio's *Maced-* 7 times (10:10–12:16), *Macceda* 15:41 (1573 the same); Greek Μακηδά | holds by Castellio's majority; the Hebrew alone gives cc; ē sure (tsere, η) |
| 17:11 | *Mageddōnēnsēs* (*Magedonenses*) | מְגִדּוֹ shewa, hireq + doubled d, holem | 12:21 *Mageddonis*; 1573 17:11 *Magedonenses* | holds |
| 18:26 | *Caphīra* (*Caphara*) | הַכְּפִירָה shewa, hireq-yod | 9:17 *Caphira*; Greek Κεφιρά | holds |
| 18:25 | *Bērōtha* (*Beerota*) | בְּאֵרוֹת shewa, tsere, holem | 9:17 *Berotha*; Greek Βηρωθ, Βεηρωθά; Deut 10:6 *Bērōthīs* | holds |

### 3c. Left as Castellio spells them, reconsidered

- **Jokneam, 12:22**: 1738's *Iacha-|nanæ* is a misprint. 1573 prints *Iachanamæ* (canvas 164, seen), 1554
  *lachanamæ* (OCR), Wikisource *Jachanama*: Hebrew עָם, m. Correct it to *Jachanāmæ* in the edited text (the
  printed text keeps 1738's). Castellio's three spellings (*Jachanama*, *Jeconam*, *Jecanam*) are then all in his
  own printings. For one spelling: *Jeconām*, indeclinable at 12:22 (*rēx Jeconām*); otherwise *Jachanāmæ*.
- **Taanach**: תַּעְנַךְ patah, silent shewa, patah, final soft k (*ch*). Castellio's *Thenaci* (12:21), *Tanacenses*
  (17:11) and *Thanach* (21:25) are in 1554, 1573 and 1738 alike. The marks don't depend on the choice (all
  short). *Thanach* is the closest to the Hebrew (a–a, *ch*). The reason given for leaving three spellings ("forms he
  never prints") is weaker than it looked: *Cedis* at 12:22 is already such a form. For one spelling: *Thanach*,
  indeclinable at 12:21 (*rēx Thanach*, as the Vulgate), 17:11 *Thanachēnsēs*.

### 4. 15:34 *Taphna*

- **For *Taphna***: 1554 (canvas 132, seen), Castellio's own revision (*totum opus recognovit ipse*), 1573 (canvas
  165, seen), 1738 (leaf 282, seen) and 1750 all print it with an n, and so does Wikisource. 1551 not checked.
- **For *Taphūa***: the Hebrew is תַּפּוּחַ, the same as every other Tappuah (patah, doubled p, **shureq**, furtive
  patah): *Taphna* has no letter for the long ū. Castellio spells all the others *Taph(u)a*: 12:17, 16:8, 17:8 (twice),
  15:53 *Bethtaphua*, 17:7 *Entaphua*; the Vulgate here *Taphua*. n for u is the commonest turned letter. The
  Septuagint's list here differs (Τανώ) and decides nothing.
- **Weighed**: the "different town" reason in the stage-2 record does not explain the n, since Castellio spells
  Judah's Beth-tappuah (15:53) *Bethtaphua*. But an n that survived Castellio's own 1554 revision and every later
  printing is his text as printed, not a slip that a printing corrects. Recommendation unchanged: *Taphna*, unmarked
  (patah). *Taphūa* is the alternative if the Hebrew should decide.
- **Reconsidered** (Nathan, 2026-11-19: "Are you sure it holds up?"): it does not. The printings are one line of
  descent (1750 follows 1738 line for line; 1738 and 1573 follow the earlier text), so their agreement shows only that
  the letter was never corrected, not that Castellio meant it. No source seen has an n, and Castellio spells the same
  Hebrew name with u in all six other places. The print's form is kept where it belongs, in the printed text (decision
  58); the edited text corrects misprints and gives one form per name (decisions 46, 81), as with 12:22's n for m.
  **Revised recommendation: *Taphūa*** in the edited text (restoring stage-2 item 36), *Taphna* in the printed text.
  **Applied** (Nathan, 2026-11-19: "Yes, Taphūa"): item 36 restored, the forms row *Taphūa*, the preview rebuilt.
  1551 not checked (Google Books answered the automated search with a captcha).

### Found by the same check, outside points 3 and 4

- **Jarmuth *Jerīmōth-*** (10:3, 10:5, 10:23, 12:11 *jerīmōthius*, 15:35, 21:29): the ī comes only from the Greek
  Ἱερειμούθ at 10:3; the Greek has Ἱεριμούθ at 12:11 and Ἰερμούθ at 15:35, and the Hebrew יַרְמוּת patah, silent shewa,
  shureq has no vowel there. By the Hebrew: *Jerimōth-*.
- **Gaza *Gāza*** (11:22 *Gāzæ*, 13:3 *gāzēa*, 15:47 *Gāza*): Gaffiot *Găza*, the Hebrew עַזָּה patah, the Greek Γάζα
  all short; the settled *Gāzam* (Gen 10:19, Deut 2:23, Acts 8:26) is against all three. By the Hebrew and Gaffiot:
  *Gaza*, and the three settled words with it.
- **Shiloh *Sīlūnt-*** holds: the Hebrew is written שִׁלֹה here, but שִׁילוֹ with the yod (long ī) in Judg 21:21 (twice)
  and Jer 7:12, and the Greek has Σηλώ; the holem is Castellio's *ū*.
- **Zarethan *Sārthānis*** (3:16) holds: צָֽרְתָ֔ן has a meteg on its first qamets (gadol), unlike Zorah's.
