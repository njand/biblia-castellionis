# 2 Kings: one form per person, place and people (names reader, 2026-11-23)

Every capitalized word of `text/draft/2KI.preview.usfm` (the draft with the nine readers' rows merged in
`data/decisions/2Kgs.forms.tsv`) that is not also a common word was grouped by its unmarked key and checked against the
settled text (`data/gold/`, every settled book through 1 Kings and the NT), then Gaffiot (`pipeline latin macron`), the
Greek (Brenton) and the Hebrew (WLC), in 1 Kings' order (`1kgs1-22-phase2/names.md`): settled form, Gaffiot, the
Greek's η/ω, the Hebrew vowel (qamets, tsere, holem, shureq, hireq-yod long; decision 52). Gentile adjectives take the
founder's marks and the suffix's quantity. Nominatives of names in *-as* take *-ās* (1 Kings call 2, accepted). No
lower-case name adjectives are left in the preview (the readers' layout rows capitalized them).

**Output**: `names-forms.tsv`, **138 rows**, only where the decided form differs from the preview. Each note says what it
replaces (`replaces the preview's …`) or which merged row it overrides (`overrides the merged …`: 28, nearly all the
readers' ending-only rows, now with the stem marked; two change the readers' form: r6's *Gādis* → *Gadis*). Built by a
script in the scratch folder (`…/scratchpad/nm/mk.py`); every row's form, unmarked, spells a word of its verse in
`text/draft/2KI.usfm` (checked by script), except the five rows that assume the draft fixes below (8:26 *Ambris*, 14:11
and 14:13 *Bēthsemem*, 23:13 *Chamōssō*, 25:23 *Nethōphātīta*): **apply the fixes before merging these rows.** Once
23:13 is fixed, r9's merged row `2Kgs.23.13 Chamosō` no longer matches a word and can be dropped. No other file written.

The printed text (`text/orig/2KI.usfm`) keeps 1738's spellings whatever is decided here.

## Proposed draft fixes (names brought to one form)

Each is 1738's own spelling (checked in `text/orig/2KI.usfm`).

1. **8:26** *Amris* → *Ambris*: Athaliah's grandfather Omri, the settled *Ambris, Ambrim, Ambrī* (1 Kgs 16:16–28;
   Greek Ἀμβρί, here and there; Castellio's *b* is the Greek's). The book's only Omri.
    **Apply:** `2Kgs.8.26` la: `Athaliam, Amris Israelitarum` → `Athaliam, Ambris Israelitarum`
2. **14:11, 14:13** *Bethsamem* → *Bethsemem*: Beth-shemesh, the settled *Bēthsemem* (1 Sam 6:9 …, and 1 Kgs 4:9 after its
   draft fix §4.7, the same 1738 *Bethsamem*).
    **Apply:** `2Kgs.14.11` la: `apud Bethsamem, quae` → `apud Bethsemem, quae`
    **Apply:** `2Kgs.14.13` la: `cepit apud Bethsamem Joas` → `cepit apud Bethsemem Joas`
3. **23:13** *Chamoso* → *Chamosso*: Chemosh, the settled *Chamōssō* (1 Kgs 11:7 after its draft fix §4.8), *Chamōssī*
   (Num 21:29), *Chamōssus* (Judg 11:24).
    **Apply:** `2Kgs.23.13` la: `et Chamoso Moabitarum` → `et Chamosso Moabitarum`
4. **25:23** *Netophatita* → *Nethophatita*: the Netophathite, the settled *Nethōphātēnsis* (2 Sam 23:28, 23:29), Greek
   Νετωφαθίτης. Castellio's suffix (*-īta* here, *-ēnsis* there) kept; only the stem's *th* made one. Low priority.
    **Apply:** `2Kgs.25.23` la: `Thanehumethi Netophatita, et` → `Thanehumethi Nethophatita, et`
5. **25:6, 25:20** *Reblatham* → *Reblam*: Riblah, one form within the book (23:33 *apud Reblam*) and with the settled
   *Reblam* (Num 34:11). *Reblatham* is Castellio's transliteration of רִבְלָתָה, the name with the Hebrew's "toward"
   ending, not another form of the name (as *Dōthain*/*Dothane* are). Low priority; no forms row needed (unmarked,
   hireq).
    **Apply:** `2Kgs.25.6` la: `et Reblatham ad` → `et Reblam ad`
    **Apply:** `2Kgs.25.20` la: `Nabuzardan Reblatham ad` → `Nabuzardan Reblam ad`

Not proposed (left as Castellio's): *Dothane* 6:13 beside the settled *Dōthain* (Gen 37:17: the Hebrew there is
דֹּתַיְנָה, here דֹתָן); *Elatham* 14:22, 16:6 beside the settled *ab Ēlathō* (Deut 2:8; a declension, not a spelling);
*Jectheel* 14:7 beside the settled *Jecthēl* (Josh 15:38; another place of the same Hebrew name); *Thecuæ* 22:14
(Tikvah, תִּקְוָה, a man) beside the settled *Thecuā* (Tekoa, another name); *Joachin* (Jehoiachin) beside Matthew's
*Jechoniās*, and *Ezechīās* beside Matthew's *Ezecīās* (1573's spelling: see call 5).

## The readers' questions

| Name | Hebrew · Greek | Decided | Why |
|---|---|---|---|
| *Elisæus* | אֱלִישָׁע | kept unmarked | the settled *Elisæus, -um* (1 Kgs 19:16–21), *Elisæō* (Luke 4:27): one form for the man (1 Kings call 5) |
| *Jorāmus, Jorām-* | יְהוֹרָם | kept (the readers' *Jorām-*) | the settled *Jorāmus* (1 Kgs 22:50, Matt 1:8: the same king of Judah), *Jorāmum* (2 Sam 8:10); W's *Iōrāmus* not taken against them |
| *Mēsa* 3:4 | מֵישַׁע | kept (r1) | tsere-yod; nominative, short *-a*. The settled *Mesā* (Gen 10:30) is another name (מֵשָׁא) |
| *Gihezis, -im, -ī* | גֵּחֲזִי · Γιεζί | kept unmarked | Castellio's *Gi-* is not the tsere (the Hebrew not used for that vowel); the rest hatef-patah, and *-is/-ī* as the settled *Semeis, Semeī* |
| *Sūnam*; *Sunamīt-* | שׁוּנֵם | kept (r2) | *Sūnam* as the settled *Sūnaman* (1 Sam 28:4); *Sunamītem, -ī* as the settled *Sunamītis, -idem* (1 Kgs; Gaffiot *Sunamītis*), the town's ū not carried over (1 Kings call 3) |
| *Baalsālisā* 4:42 | בַּעַל שָׁלִשָׁה | kept (r2) | qamets; *Baal* unmarked as settled; ablative after *ā* |
| *Syrō* 5:20 | אֲרַמִּי | kept unmarked (r2) | the same man is *Naaman Syrus* (Luke 4:27), and every settled *Syr-* in Samuel and Kings is unmarked; only Gen 31:20, 31:24 *Sȳrō, Sȳrum* (Laban) follow Gaffiot (call 4) |
| *Abana*, *Pharphar* 5:12 | Kethiv אבנה (unpointed in the WLC), פַּרְפַּר | kept unmarked | no vowel to read in the Kethiv; patah in *Pharphar* |
| *Dothane* 6:13 | דֹתָן | ***Dōthāne*** | holem, qamets; the spelling kept (above) |
| *Amris* 8:26 | עָמְרִי · Ἀμβρί | ***Ambris*** | draft fix 1 |
| *Namsis* 9:2, 9:14, 9:20 | נִמְשִׁי · Ναμεσσί | kept unmarked | 1738 prints *Namsis* three times here, as the Hebrew (m) and the Greek; the settled 1 Kgs 19:16 *Nansis* is the odd one (call 1) |
| *Gure*; *Jeblaam* 9:27 | גּוּר; יִבְלְעָם | ***Gūre***; ***Jeblaām*** | shureq; the settled *Jeblaāmam* (Josh 17:11) |
| *Jonadab-*, *Rechab-* 10:15, 10:23 | יְהוֹנָדָב; רֵכָב | *Jōnādābum, -us* kept, ***Jōnādābō*** 10:23; ***Rēchābī*** ×2 | the settled *Jōnādābus* (2 Sam 13, another man, the same Latin name); the settled *Rēchābus* (2 Sam 4:2–9, the same Hebrew name) |
| *Joachazus* (10:35, 13:1 …, 23:30) | יְהוֹאָחָז | ***Jōāchazus, -ī, -ō, -um*** (15 rows) | *Jōā-* as the settled *Jōācimus* (Matt 1:11) and *Jōās*; *-chaz-* unmarked as the settled *Achazus* (Matt 1:9). The preview had the endings unmarked too |
| *Jojāda* | יְהוֹיָדָע | kept (r5) | the settled *Jojādæ* (1 Kgs 1:8 …); nominative short *-a* |
| *Messæ* 11:6 | מַסָּח | kept unmarked (r5) | patah; Castellio's genitive |
| *Joadane* 14:2 | Kethiv יהועדין (unpointed), Qere יְהוֹעַדָּן | ***Jōadane*** | *Jō-* only, as *Jōsaba* below; the rest unpointed in the Kethiv |
| *Jectheel* 14:7 | יָקְתְאֵל | ***Jectheēl*** | tsere, as the settled *Jecthēl* (Josh 15:38); spelling kept |
| *Bethsamem* 14:11, 14:13 | בֵּית שֶׁמֶשׁ | ***Bēthsemem*** | draft fix 2 |
| *Elatham* 14:22 | אֵילַת | ***Ēlatham*** | as 16:6 (r6) and the settled *Ēlathō* |
| *Hematha* / *Hemātham* | חֲמָת | ***Hemāth-*** throughout (6 rows: *Hemāthā* 14:25, 17:24; *Hemāthēnsēs* 17:30, 18:34; *Hemāthēnsī* 23:33; *Hemāthēnsium* 25:21) | the settled *Hemātham* (Josh 13:5 …), *Hemāthæ* (1 Kgs 8:65); the preview marked two and not the rest |
| *Bersabā* 12:1 | בְּאֵר שָׁבַע | kept | the settled *ā Bersabā* (Gen 28:10), the ablative; the other settled *Bersaba* are nominatives or indeclinable |
| *Āzariās, Āzariæ* | עֲזַרְיָה | kept; ***Āzariam*** 14:21 | Gaffiot *Āzarĭās*, the settled 1 Kgs 4:2 (1 Kings call 3) |
| *Ōsēa* | הוֹשֵׁעַ | kept (r6) | the settled *Ōsēā* (Rom 9:25) for the stem; Castellio's nominative *Ōsēa*, short |
| *Ozīæ* | עֻזִּיָּהוּ | kept (r6) | the settled *Ozīās, Ozīam* (Matt 1:8–9), the same king |
| *Gādis* 15:14, 15:17 | גָּדִי | ***Gadis*** (overrides r6) | the settled *Gadus* (2 Sam 24:11, גָּד), *Gadīnī*, unmarked; r6's *ā* came only from the preview's W *Gādēs* (Cadiz) |
| *Ezechīās* | חִזְקִיָּהוּ · Ἐζεκίας | **confirmed** (r7) | the same king is the settled *Ezecīās, Ezecīam* (Matt 1:9–10); W *Ezechīās*; Gaffiot *Ezĕchĭās* has a short *i* (call 2) |
| *Ezechiani* 19:5 | | ***Ezechīānī*** | r7's reading (Hezekiah's men, subject); the *-iānus* adjective as the settled *Ambriānī*; r7's row never reached the preview, so it is given here |
| *Jōa* 18:18, 18:26, 18:37 | יוֹאָח | kept (r7) | nominative, first declension, as *Ōsēa*; *Jō-* as *Jōās* |
| *Berodacus Baladam, Baladanis* 20:12 | בְּרֹאדַךְ בַּלְאֲדָן בֶּן־בַּלְאֲדָן · Μαρωδὰχ Βαλαδὰν | ***Berōdacus***, *Baladam* kept, ***Baladānis*** | holem and the Greek ω; *Baladam* is the second part of the king's name, nominative (Castellio, as the Vulgate *Berodach Baladan, filius Baladan*): call 3 |
| *Ēsajās* | יְשַׁעְיָהוּ | **kept as the preview** | the OT's *j* between vowels (the draft's spelling) leaves no *ā* to mark, as the settled *Banajas* (בְּנָיָהוּ) and *Sarajam* (2 Sam 8:17, שְׂרָיָה), whose qamets before the *j* is unmarked; the NT's *Ēsāiās* (Gaffiot *Esāĭās*) has a vowel *i* after the *ā*. *Ē-* as the NT |
| Huldah's group 22:12–14 | חִלְקִיָּהוּ, אֲחִיקָם, שָׁפָן, עַכְבּוֹר, מִיכָיָה, עֲשָׂיָה, חֻלְדָּה, שַׁלֻּם, תִּקְוָה, חַרְחַס | ***Helciās*** (22:8, 22:14, 23:24), ***Ahīchāmus, -ō, -ī***, ***Sāphān, -em, -ī, -is***, ***Achobōr, -ī*** (settled *Achobōris*, Gen 36:38); *Michajæ, Asajas, Holdam, Sellumī, Thecuæ, Haramī* kept | *-ās* (1 Kings call 2); hireq-yod and qamets; *Sāphān* as the settled *Sāphātus* (שָׁפָט); the rest have no long vowel to mark |
| *Haphsibā* 21:1, *Ididā* 22:1 | חֶפְצִי־בָהּ; יְדִידָה | ***Haphsībā***, ***Idīdā*** | hireq-yod; ablatives with *mātre* (r8) |
| *Āmōn-* | אָמוֹן | kept (r8) | the settled *Āmōn, Āmōnem* (Matt 1:10, the same king) |
| *Maachati* 25:23 | הַמַּעֲכָתִי | ***Maachātī*** | a genitive (Castellio makes it the father's name, as *Jōhannēs Careæ*, *Sarajas Thanehumethī* in the same verse), not indeclinable; the stem of the settled *Maachātis*, *Maachāthēnsis* |
| *Jōhannēs* 25:23 | יוֹחָנָן · Ἰωνά | **kept** | the approved word rule *joannes → johannes* (decision 37, names one way) covers the Latin name whoever bears it; Castellio gives Johanan the Gospels' name, and the Hebrew has the ח the *h* stands for |
| *Jēremīæ* 23:31, 24:18 | יִרְמְיָהוּ | kept (r9) | the settled *Jēremīā, -am* (Matt 2:17, 16:14); Gaffiot *Jērĕmīās* |
| *Pharvarim* 23:11 | פַּרְוָרִים | ***Pharvārīm*** | qamets, hireq-yod; a place for Castellio |
| *Sepharvaim-* | סְפַרְוַיִם | kept unmarked | patah; no long vowel |

## Hard calls (for Nathan)

1. **1 Kgs 19:16 *Nansis*** (settled) against 2 Kings' *Namsis* ×3, the same man (Nimshi, נִמְשִׁי; Greek Ναμεσσί). 1738
   prints both (1 Kings' OCR read *Nanfisi*, read on the page as *Nansis*; `data/witnesses/read-1738/1Kgs1-22.tsv`
   line 3308); *Nansis* looks like 1738's slip. Recommended: your hand edit of `text/1KI.usfm` 19:16 *Nansis* → *Namsis*
   (the printed text keeps *Nansis*). 2 Kings is left as printed either way.
2. ***Ezechīās*** with a long *ī* (r7, confirmed): one form with the settled Matt 1:9–10 *Ezecīās*, against Gaffiot's
   *Ezĕchĭās*. The same choice as the book's other *-iās* names with a settled form (*Ozīās, Sedecīās, Zacharīās, Ūrīās*);
   1 Kings' *Āzariās* followed Gaffiot only because no settled form of that name exists. If you prefer Gaffiot here,
   the readers' *Ezechīās* rows (r6, r7, r8) and Matthew's would need changing together.
3. **20:12 *Berodacus Baladam, Baladanis fīlius***: 1738 prints *Baladam* (the read lines, leaf 454), the only
   witness in the repo. The Hebrew, the Greek and the Vulgate have *Baladan* in both places, and Castellio's genitive
   *Baladanis* presupposes the stem *Baladan-*, so *Baladam* may be the printer's *m* for *n*. Kept as printed;
   if you want it corrected: **Apply:** `2Kgs.20.12` la: `Berodacus Baladam, Baladanis` → `Berodacus Baladan, Baladanis`
   (not applied; then a forms row *Baladān* would follow).
4. **Marked on the Hebrew alone** (no settled form, Gaffiot or Greek long vowel; as 1 Kings call 4, accepted): *Dōthāne,
   Gūre, Jōsaba, Jōzābārō, Jōzābādō, Sōmēris, Mattānemque, Jōadane, Jerūsa, Phūl, Razīn-, Cūthā, Cūthæī, Nērgalem, Asīmam,
   Soccōbenōthum, Arphād-, Hēnæ, Hēnēnsēs, Thartācum, Tartānem, Āsāphī, Tharācam, Nisrōchī, Ēsaraddōn, Haphsībā,
   Hārūsī, Idīdā, Mesullāmī, Ahīchām-, Sāphān-, Pharvārīm, Tōphet, Hamūtal-, Nabūzardān, Sōphrem, Evīlmerōdachus,
   Jōāchin-*. Several have the Greek's ω/η too (*Manahēmus* Μαναήμ, *Hābōre* Ἀβώρ, *Gōzānem* Γωζάν, *Rabsācēs* Ῥαψάκης,
   *Berōdacus* Μαρωδάχ, *Achobōr* Ἀχοβώρ). If Hebrew-only marks are dropped, these rows go.
5. **The NT's spellings of the same kings**: Matthew 1 (1573) has *Ezecīās* (no *h*) and *Jechoniās*; 2 Kings (1738) has
   *Ezechīās* (36 times with its cases) and *Joachin* (Castellio's other name for Jehoiachin). Not unified: the books follow different
   printed bases, and *Ezechias* is the usual Latin. Say if you want one spelling of Hezekiah across the Bible.
6. **Gen 31:20, 31:24 *Sȳrō, Sȳrum*** (Gaffiot) against every other settled *Syr-* (Luke 4:27 *Syrus*, Samuel, 1 Kings)
   unmarked. 2 Kings follows the majority (r2's *Syrō* 5:20). The Genesis pair would need your hand edit for one form.

## The rest (checked, kept)

| Person / place / people | Preview | Settled |
|---|---|---|
| Ahab, Jezebel, Jehu, Nimshi, Jehoshaphat, Ahaziah | *Achāb-, Achābicæ, Jezabēl-, Jēhūs/-um/-ū, Jōsāphāt-, Ochoziās, -æ, -ā, Ochozia* (voc.) | *Achāb-, Jezabēl-, Jēhūs, Jēhum, Jōsāphāt-, Ochoziās* |
| Elijah the Tishbite, Baal-zebub, Ekron | *Ēlī-, Ēliānum, Thesbīt-, Beelzebūb-, Accarōnēns-* | *Ēlīās, Ēliānō* (Luke 1:17), *Thesbīta, Accarōnēnsis* |
| Moab, Edom, Israel, Judah, Samaria, Syria, Damascus | *Mōabīt-, Idūmæ-, Isrāēl-, Isrāēlīt-, Jūdæ-, Jūdaicē, Samarī-, Samarītān-, Syr-, Syriacē, Damasc-, Damascēn-* | the same |
| Jericho, Gilgal, Bethel, Carmel, Jordan, Jezreel, Megiddo | *Hierichūnt-, Galgal-, Bēthēl-, Bēthēlēns-, Carmēlum, Jordān-, Jezræl-, Jezrælēns-, Mageddōn-* | the same |
| Naaman, Rimmon, Elisha's servants; Ben-hadad, Hazael | *Naaman-, Remmōnis, Benadad-, Hazæl-* | *Naaman* (Luke 4:27), *Remmōnis, Benadad-, Hazælem* |
| Jehu's line, Joash, Jehoash, Amaziah, Jeroboam, Nebat | *Jōās, Jōæ, Jōam, Jōā, Amasī-, Jeroboām-, Nabātī* | *Jōās, Jōam, Jeroboām-, Nabātī* |
| Uzziah's and the last kings of Israel | *Zacharīās, Sellum-, Jābis, Manahēm- (new), Phaca-, Phacehia-, Romeliæ, Ōsēa-, Ēlæ* | *Zacharīās, Jābis, Ēlæ* |
| Tiglath-pileser's conquests (15:29) | *Iōnem, Ābēlmaacham, Jānōam, Cadem, Hāsōr, Galaadītidem, Galilæam, Nephthālēnsem* | the same |
| Ahaz, Jotham, Rezin, Uriah, Kir | *Achaz-, Jōtham-, Razīn- (new), Ūrī-, Cirenem* | *Achazus, Jōthamus, Ūrīās*; *Cirenem* unmarked (Castellio's Kir, קִיר, read as Cyrene?) |
| Assyria, Babylon, the Medes, Ethiopia | *Assyri-, Babylōn-, Babylōni-, Mēdicæ, Æthiopiæ, Armeniam, Nīnivem* | *Assyriam* (Gen 25:16; Gaffiot *Assȳria* not taken against it), *Babylōne, Nīnivem* |
| Hezekiah's officials and Assyria's | *Eliācīmus, Sobna, Jōa, Āsāphī (new), Tartānem (new), Rabsarim, Rabsācēs (new), Senacherib-, Salmanasar, Theglathphalasar* | *Eliācīmus* (Matt 1:13); Gaffiot *Sennăchĕrib* (unmarked) |
| Isaiah, Amoz | *Ēsaj-, Āmōsī* | *Āmōsī* (Luke 3:25) |
| Manasseh, Amon, Josiah; Uzza's garden | *Manass-, Āmōn-, Jōsī-, Ozæ* | the same |
| Josiah's reform | *Astarōthō, Molochō, Melcōmō, Chamōssō, Hennōmī, Cedrōn-, Sīdōniōrum, Ammonītārum, Gabā, Bersabam, Jōsuæ* | the same |
| The last kings, Nebuchadnezzar, the exile | *Jōācim-, Jōāchin- (new), Mattaniam, Sedecī-, Nabūchodonosor, -ōris, Nechō, Nechōnī, Pharaō-, Euphrātem, Chaldæ-* | *Jōācimus, Sedecīās, Pharaō-*; W *Nabūchodonosor, -ōris*, *Nechōs* |
| Gedaliah's officers (25:23) | *Godoli-, Ismaēl, Nathaniæ, Jōhannēs, Cārēæ (new), Sarajas, Thanehumethī, Nethōphātīta (new), Jazaniās, Maachātī (new), Maspham, Elīsāmæ (new)* | *Ismaēl, Maspham, Sarajam, Elīsāma* |

## Noticed, not changed

- **Unmarked, no long vowel to mark**: *Athalia* (Gaffiot *Athalia*), *Josaba*'s *-saba*, *Sebia, Semaæ, Sillam, Romeliæ,
  Phaca, Phacehia, Jecholiā, Thapsam, Thapsēnsēsque, Argobus*'s *-bus, Arie, Halæ, Avā, Avæ, Avanī, Nebahazum,
  Adramelech-, Anamelech-, Sarasar, Resepham, Edenēnsēs* (עֶדֶן, not the garden's עֵדֶן), *Thelassariānōs, Nehostan,
  Nehostā, Asaliæ, Adajæ, Basechatēnsī, Messalemethan, Jotebanam, Phadajæ, Zebudā* (Kethiv זבידה unpointed),
  *Elnāthanis*' second *a*, *Nathanmelechī, Badacarī, Harasetham, Lebna* (settled), *Mattaniam, Sophoniam, Sarajas,
  Thanehumethī*.
- *Ēlatham* (Elath, accusative of *Ēlatha*) beside the settled ablative *Ēlathō* (Deut 2:8): Castellio declines the
  town two ways; no form unified.
- *Cirenem* 16:9 (Kir, קִירָה): Castellio's spelling suggests he read Cyrene; left unmarked, not taken to Gaffiot's
  *Cȳrēnē*.

## Report

- **Rows**: 138 in `names-forms.tsv` (*Jōāchaz-* 15, *Hemāth-* 6, *Sāphān-* 7, *Rabsāc-* 7, *Manahēm-* 6, *Jōāchin-* 7,
  the rest one to four each); 28 override merged rows (two change the reader's form: r6's *Gādis* ×2), 110 replace
  preview forms. Five rows assume the draft fixes.
- **Draft fixes proposed**: *Amris → Ambris* (8:26), *Bethsamem → Bethsemem* (14:11, 14:13), *Chamoso → Chamosso*
  (23:13), *Netophatita → Nethophatita* (25:23), *Reblatham → Reblam* (25:6, 25:20).
- **For Nathan**: calls 1 (*Nansis* in the settled 1 Kings), 2 (*Ezechīās*' ī), 3 (*Baladam*), 4 (Hebrew-only marks),
  5 (Matthew's *Ezecīās*), 6 (Genesis's *Sȳr-*).
