# 1 Kings: one form per person, place and people (names reader, 2026-11-22)

Every capitalized word of `text/draft/1KI.preview.usfm` (built from the draft and the merged readers' rows in
`data/decisions/1Kgs.forms.tsv`), and every lower-case adjective of a people or place, was grouped by its unmarked key
and checked against the settled text (`data/gold/`, every settled book through 2 Samuel), then Gaffiot (`pipeline latin
macron`), the Greek (Brenton) and the Hebrew (WLC), in 2 Samuel's order (`2sam1-24-phase2/names.md`): settled form,
Gaffiot, the Greek's η/ω, the Hebrew vowel (qamets, tsere, holem, shureq, hireq-yod long; decision 52). Gentile
adjectives take the founder's marks and the suffix's quantity (-ānus, -īnus, -ēnsis, -īta, -æus, -iānus). Nominatives
of Greek first-declension names in *-as* take *-ās*, as the settled *Ūrīās, Ēlīās, Ābīās, Achiās, Jōsīās, Ozīās*
(the exceptions are call 2). Where Castellio's vowel differs from the Hebrew (*Abdias* for עֹבַדְיָהוּ, *Ambri* for
עָמְרִי, *Nephath-* for נָפַת), the Hebrew is not used for that vowel. The WLC numbers 4:21–34 as 5:1–14; those verses
were read there.

**Output**: `names-forms.tsv`, **106 rows**, only where the decided form differs from the preview. Each note says what
it replaces (`replaces the preview's …`) or which merged row it overrides (`overrides rN's …`: four, r1's 2:26
*Anāthōtā* and three others). Built by a script in the scratch folder (`…/scratchpad/nm/mk.py`); every row's form,
unmarked, spells a word of its verse in `text/draft/1KI.usfm` (checked by script; six write *æ* where the draft has
*ae*, as the readers' rows do). No spelling rows: the rows fit the draft's present spellings. No other file written.

The printed text (`text/orig/1KI.usfm`) keeps 1738's spellings whatever is decided here.

## Spellings that differ (reported, not changed; for the draft fixes)

Each is 1738's own spelling (checked in `text/orig/1KI.usfm`). If a fix is applied, the forms row for that verse
must be respelled to match.

| Where | Printed | Elsewhere | Recommendation |
|---|---|---|---|
| 11:26, 21:22 | *Nabathi* (2×) | *Nabati* 7× (12:2 … 16:31, 22:52) | ***Nabati*** everywhere (נְבָט, Ναβάτ; the majority). Forms: *Nabāthī → Nabātī* |
| 21:22 | *Achiæ* (Baasha's father) | *Ahiæ* 15:27, 15:33 (the same man); *Ahi-* for the Shilonite 11:29–15:29 | ***Ahiæ*** (the book's form of Ahijah; *Achiās* 4:3 is another man, as the settled 1 Sam 14:3) |
| 16:1 / 16:7 | *Ananis* / *Hananis* (Hanani, the same man, six verses apart) | | one form; ***Hananis*** (חֲנָנִי, as the book's *Hazæl, Hiel, Hemanem* keep ח as *H*). Forms *Anānis / Hanānis* |
| 17:10 / 17:8 | *Sarephtam* / *Sarephtham* | settled *Sarephtham* (Luke 4:26) | ***Sarephtham*** |
| 22:48 / 9:26 | *Asiongaber* / *Asiongabre* | settled *Asiōngābre* (Deut 2:8) | ***Asiongabre*** (as settled); or leave 22:48 as Castellio's indeclinable. Form *Asiōngāber/-ābre* |
| 2:26 | *Anathota* | settled *Anāthōtha* (Josh 21:18), *Anāthōthēnsis* (2 Sam 23:27) | ***Anathotha*** (form then *Anāthōtha*; see call 1) |
| 4:9 | *Bethsamem* | settled *Bēthsemem* (1 Sam 6:9, 6:12), *Bēthsemes* (Josh 19:38) | ***Bethsemem*** (form then *Bēthsemem*) |
| 11:5, 11:7, 11:33 | *Chamosum, Chamoso* | settled *Chamōssus, Chamōssī* (Judg 11:24, Num 21:29) | ***Chamossum, Chamosso*** (marks unchanged); low priority |

Left as Castellio's, not recommended: *Sochot* 7:46 (settled *Sochōtha*, an indeclinable beside it), *Baalatham* 9:18
(settled *Balaāth*, Josh 19:44, another transliteration of בַּעֲלָת), *Elotha* 9:26 (Eloth; the settled *Ēlathō* is
Elath, the Hebrew's own variant), *Astorethum* (Ashtoreth, singular; the settled *Astarōth-* is the plural),
*Bethsaba* (1:15 …) beside the settled *Bethsabam* (the same).

## Hard calls (for Nathan)

1. **2:26 *Anāthōta*** (accusative neuter plural, short *-a*), overriding r1's ablative *Anāthōtā*. The settled
   *Anāthōtha* is neuter plural (Josh 21:18, *Anāthōtha et Almōnem*, both accusative), so *ut Anathota in prædium suum
   sē cōnferret* reads as the accusative of goal ("to Anathoth, to his estate"). r1 read it as the ablative of place;
   that needs a feminine singular *Anathota, -æ*, which nothing settled has. Drop my row to keep r1's.
2. **The nominative in *-as***: the settled *Adōnias* (2 Sam 3:4), *Banajas* (2 Sam 20:23, 3×) and *Saphatias* have a
   short *-as*; every other settled one (*Ūrīās, Ēlīās, Ābīās, Achiās, Jōsīās, Ozīās, Zacharīās, Ananīās, Ēsāiās*)
   has *-ās*. 1 Kings keeps each settled person's form (*Adōnias* 8×, *Banajas* 8×: one form per person) and gives the
   unsettled *Abdiās, Ahiās, Ochoziās* the majority's *-ās*. If Nathan wants *-ās* throughout, the settled 2 Sam 3:4,
   20:23 etc. need his hand edit, and the 1 Kings *Adōnias, Banajas* rows follow.
3. **Gaffiot against the Hebrew or a settled cousin**: *Āzariās* 4:2, 4:5 (Gaffiot *Āzarĭās*: the Ā against the
   hatef-patah of עֲזַרְיָהוּ, and the short i against the preview's lexicon *Āzarīās*; Gaffiot outranks both).
   *Sunamītis, Sunamītidem* (r1's, Gaffiot *Sunamītis, ĭdis*, the u unmarked) left as they are, though the settled town
   is *Sūnaman* (1 Sam 28:4, shureq): a gentile adjective normally takes its town's marks.
4. **Marked on the Hebrew alone** (no settled form, Gaffiot or Greek long vowel to confirm): *Nābōth-* (18 rows, the
   largest group; the readers left it unmarked), *Chābūl, Būl, Ēthānīm, Ēthānem, Hēmānem, Calchōlem, Māchōlis, Ezrāītam*
   (*-īta* suffix), *Achīsār, Achīnādābus, Adōnīrāmus, Elīhōrephus, Sīsæ, Zābūdus, Addōnis, Phārūæ, Tāphatham, Mācam,
   Ālōtha, Arubōtha, Bēthānānem, Carīthum, Hīēl, Segūbum, Gīnethī, Azūbam, Hanānis/Anānis, Jēhūs/Jēhum/Jēhū*. Several
   have the Greek's ω/η/ου too (*Addōnis* Σαδδώ, *Arubōtha* Ἀραβώθ, *Hīēl* Ἀχιήλ, *Segūbum* Σεγούβ, *Azūbam* Ἀζουβά,
   *Zābūdus* Ζαβούθ). If Nathan drops Hebrew-only marks (2 Samuel's call 11), these rows go.
5. **Kept unmarked against the Hebrew, because the settled form is unmarked**: *Asa, Asæ, Asam* (אָסָא; settled *Asa*,
   *Asam*, Matt 1:7–8), *Bethsaba(m)* (settled 2 Sam 11:3), *Semeis/Semeim* (settled 2 Sam; *Semeim* the accusative as
   the settled *Achim*), *Elisæus, Elisæum* (settled *Elisæō*, Luke 4:27, though אֱלִישָׁע has hireq-yod), *Boaz* 7:21
   (the pillar; the man is the settled unmarked *Boozus*), *Thersa-* (settled Josh 12:24), *Zambris*, *Maspha-*,
   *Sesacus*. And *Hazæl-* (חֲזָאֵל) kept with its ligature, as the settled *Jezræl*.
6. **Jezabel**: the readers' *Jezabēl-* (r7, r8) from the settled *Jezabēlem* (Rev 2:20) stands, though the Hebrew
   אִיזֶבֶל and the Greek Ἰεζάβελ both have a short vowel there. One form for the woman across the Bible; Revelation's
   would need Nathan's hand edit to change.
7. **19:16 *Nansis*** (Nimshi, נִמְשִׁי; Greek Ναμεσσί): kept as printed (perhaps 1738's slip for *Namsis*). Not
   checked against 2 Kings 9: no 2 Kings witness is in the repo yet. Unmarked (hireq short, nominative-genitive *-is*).
8. **22:42 *Salis*** is Shilhi (שִׁלְחִי, Greek Σαλαΐ), *Azubam, Salis fīliam*: a name (capital), not *salis* "of salt";
   unmarked (genitive *-is* short).

## Names the verse readers left

| Name | Hebrew · Greek | Preview | Decided |
|---|---|---|---|
| Bathsheba | בַּת־שֶׁבַע · Βηρσαβεέ | *Bethsaba, Bethsabam* | kept (settled *Bethsabam*; call 5) |
| Shimei | שִׁמְעִי · Σεμεΐ | *Semeis, Semeī, Semeim* 2:8, 2:41 | kept (settled 2 Sam; *Semeim* as *Achim*) |
| Rei | רֵעִי · Ῥησί | *Reīs* 1:8 | ***Rēis*** (η, tsere; nominative *-is* short) |
| Anathoth | עֲנָתֹת | *Anāthōtā* 2:26 (r1) | ***Anāthōta*** (call 1; spelling row recommended) |
| Ethanim, Bul, Ziv | הָאֵתָנִים; בּוּל; זִו | *Ethanim, Bul, Zif* | ***Ēthānīm, Būl***; *Zif* kept (hireq) |
| Cabul | כָּבוּל | *Chabul* | ***Chābūl*** |
| Megiddo; Millo | מְגִדּוֹ; הַמִּלּוֹא | *Mageddonem*; *Mellonem* 9:15, 9:24 | ***Mageddōnem*** (settled *Mageddōn-*); ***Mellōnem*** (settled *Mellōne*, 11:27) |
| Baalath; Tadmor | בַּעֲלָת | *Baalatham*; *Palmīram* | ***Baalātham*** (settled *Balaāth*, Josh 19:44); *Palmīram* kept (W, M *Palmȳra*) |
| Eloth; Ezion-geber; Ophir | אֵלוֹת; אוֹפִיר | *Elotha*; *Asiōngābre* 9:26, *Asiongaber* 22:48; *Ophir* 9:28, *Ophīre* 10:11, *Ophire* 22:48 | ***Ēlōtha*** (settled *Ēlathō*); ***Asiōngāber***; ***Ophīr, Ophīre*** (settled *Ophīren*) |
| Imlah | יִמְלָה · Ἰεμβλαά | *Jemlæ* 22:8, 22:9 | kept (hireq; the qamets is the ending) |
| Chenaanah | כְּנַעֲנָה | *Chanaanæ* 22:11, 22:24 | ***Chanaānæ*** (settled *Chanaān*) |
| Joash | יוֹאָשׁ · Ἰωάς | *Joam* 22:26 | ***Jōam*** (accusative of the settled *Jōās*) |
| Ahaziah | אֲחַזְיָהוּ · Ὀχοζίας | *Ochozias* ×3 | ***Ochoziās*** (call 2) |
| Azubah; Shilhi | עֲזוּבָה; שִׁלְחִי | *Azubam*; *Salis* | ***Azūbam***; *Salis* kept (call 8) |
| Nebat | נְבָט · Ναβάτ | *Nabāthī* ×2, *Nabātī* ×7 | kept (spelling: *Nabati*) |
| Jezebel | אִיזֶבֶל | *Jezabēl-* (r7, r8) | kept (call 6) |
| Abijam; Abijah | אֲבִיָּם; אֲבִיָּה | *Ābīam-*; *Abiā* 14:1 | *Ābīam-* kept (settled *Ābīam*); ***Ābīā*** (settled *Ābīās*, 1 Sam 8:2) |
| Nimshi | נִמְשִׁי | *Nansis* 19:16 | kept (call 7) |

## The rest

| Person / place / people | Preview | Settled | Decided |
|---|---|---|---|
| David, Solomon, Jova, Israel, Judah | *Dāvīd-, Dāvīdic-, Solomō-, Jōv-, Isrāēl-, Isrāēlīt-, Jūdæ-* | the same | kept; *solomonianis* 9:27 → ***solomōniānīs*** |
| Adonijah, Haggith, Abishag the Shunammite | *Adōnia-, Hagīthæ, Abīsag-, Sunamīt-* (r1) | *Adōnias, Hagīthæ* | kept (calls 2, 3) |
| Joab, Abner, Amasa, Zeruiah, Jether, Ner | *Jōāb-, Abnēr-, Amās-, Sarviæ, Jethris, Nēris* | the same | kept |
| Zadok, Abiathar, Nathan, Benaiah, Jehoiada | *Sadōc-, Abiāthār-, Nāthan-, Banaj-, Jojādæ* | the same | ***Sadōce*** 1:34 (vocative) |
| Cherethites, Pelethites; Gihon; En-rogel, Zoheleth | *Cerēthæ-, Phelethæ-; Gehōnem; Ēnrōgēl, Zōheleth* | *Cerēthæī, Ēnrōgēl* | kept |
| Shimei, Gera, Bahurim, Benjamite; Achish, Maacah, Gath | *Semei-, Gēræ, Bahūrīmō, Jemīniēnsem; Achim, Maachæ, Geth-* | the same | kept |
| Barzillai, Gileadite; Mahanaim; Jordan; Kidron; Hebron; Eli, Shiloh | *Berzellæi, Galaadīt-; Mahanaim; Jordān-; Cedrōnem; Hebrōne; Ēlis, Sīlūnt-* | the same | kept |
| Solomon's officers (4:2–6) | *Āzarīās, Sadōcī, Elihorephus, Achiās, Sisæ, Jōsāphātus, Achīlūdī, Nāthanis, Zabudus, Achisar, Adoniramus, Abdæ* | *Achiās, Achīlūdī, Jōsāphātus* | ***Āzariās*** (call 3), ***Elīhōrephus, Sīsæ, Zābūdus, Achīsār, Adōnīrāmus*** (also 5:14); *Abdæ* kept |
| The twelve prefects (4:8–19) | *Benhur, Bendecer, Macam, Salebīm, Bethsamem, Elonemque, Bethananem, Benhesedus, Arubotha, Sōchō, Hephra, Benabinadabus, Nephathdoram, Taphatham, Baana, Achīlūdī, Thanachum, Mageddonem, Bethsan-, Sarthanam, Jezræle, Meholam, Jecmaam, Bengeber, Rāmōtha, Jāīris, Argōbiæ, Bāsānā, Achinadabus, Addonis, Achīmaas, Nephthālēnsēs, Basematham, Chūsæī, Aserienses, Alotha, Pharuæ, Issacharienses, Semeis, Elæ, Gaber, Ūris, Sēhōnis, Ōgī* | *Salebīm, Sōchō, Baana, Thanachum, Bāsān-, Argōbiæ, Jāīris, Ūris, Sēhōnis, Ōgī, Chūsæī, Basematham, Achīmaas; Hūr, Abīnādāb-, Dōris, Hēpher, Ēlōn, Bēthsemem, Bēthsān-, Sārthānis, Ābēlmehōlæ, Mageddōn-, Āsēr-, Issāchariānus, Ēla* | ***Benhūr, Mācam, Bēthsamem, Ēlōnemque, Bēthānānem, Arubōtha, Hēphra, Benabīnādābus, Nephathdōram, Tāphatham, Mageddōnem, Bēthsānam, Bēthsānā, Sārthānam, Mehōlam, Achīnādābus, Addōnis, Āsēriēnsēs, Ālōtha, Phārūæ, Issāchariēnsēs, Ēlæ***; *Bendecer, Benhesedus, Jecmaam, Bengeber, Gaber* kept (segol, patah, qamets-hatuf) |
| The wise men (4:31) | *Ethanem Ezraitam, Hemanem, Calcholem, Dardam, Macholis* | | ***Ēthānem, Ezrāītam, Hēmānem, Calchōlem, Māchōlis***; *Dardam* kept |
| Hiram, Tyre, Sidon; Lebanon | *Hīrām-, Hīrāmicā, Tyr-, Sīdōni-; Liban-* | *Hīrāmus, Tyrō, Sīdōni-, Liban-* | kept |
| The temple's pillars and months | *Jāchīn, Boaz; Zif, Bul, Ethanim* | *Jāchīn* (Exod 6:15) | ***Būl, Ēthānīm***; *Boaz, Zif* kept |
| Huram's work; Succoth, Zarethan | *Tyriō, Nephthālēnsem; Sochot, Sarthan* 7:46 | *Sochōtha, Sārthānis* | ***Sochōt, Sārthān*** |
| Pharaoh, Egypt, Gezer, Hazor, Beth-horon, Canaanites, the five peoples (9:20) | *Pharaō-, Ægypt-, Gazer, Hāsōr, Bēthōrōnem, Chananæīs, Amorræ-, Hettæ-, Pherezæīs, Hevæīs, Jebūsæīs* | the same | kept |
| Sheba, Arabia; Cilician fleet | *Sabæ, Arabiæ, Arabas; Cilica, Cilicas* | *Sabam* (Gen 10:7) | kept (Gaffiot *Cĭlix*; *Arabs* short) |
| Solomon's wives and gods | *Moabītidas, Ammonītidas, Idūmæās, Sīdōniās, Hettæās; Astōrethum, Melcōmum, Chamōs-, Molochō* | *Mōabītidas, Molochō* | kept (spelling *Chamoss-* noted) |
| Hadad, Edom, Tahpenes, Genubath; Rezon, Eliada, Hadadezer, Zobah, Damascus | *Adad-, Idūmæ-, Taphn-, Genubathum; Razōn-, Eliādæ, Adarezero, Sophēn-, Damasc-* | *Idūmæ-, Adarezero, Sophēnæ, Damascī* | ***Idūmæum*** 11:14 |
| Jeroboam, Nebat, Zeredah, Ephrathite; Ahijah the Shilonite; Shishak | *Jeroboām-, Nabāt(h)ī, Sarēda, Ephrātæus; Ahi-, Sīlōni-; Sesac-* | *Ephrātæus, Sesacus* | ***Ahiās*** (call 2); spelling *Nabati* |
| Rehoboam, Naamah, Shemaiah; Shechem, Penuel, Bethel, Dan | *Roboām-, Naama, Semejæ; Sichemam, Phanuēl, Bēthēl-, Bēthēlēnsis, Dane(m)* | *Roboām-, Naama, Sichemam, Phanuēl, Bēthēl, Dane* | kept |
| Abijah, Abijam, Asa, Maacah, Pan, Abishalom | *Abiā, Ābīam-, Asa-, Maacha-, Pāna, Absālōmī* | *Ābīās, Ābīam, Asa(m), Maacha, Absālōmī* | ***Ābīā*** |
| Ben-hadad, Tabrimmon, Hezion; Ijon, Abel-beth-maacah, Chinneroth; Ramah, Geba, Mizpah | *Benadad-, Tabremmōnis, Heziōnis; Iōnem, Ābēlmaacham, Cenerōtha, Nephthālēnsium; Rām-, Gabāam, Masphamque* | *Ābēlmaacham, Gabāam, Maspham* | kept |
| Nadab, Baasha, Ahijah, Issachar, Gibbethon; Jehu son of Hanani | *Nādāb-, Nadabi, Baasa-, Baasān-, Ahiæ/Achiæ, Issāchariānus, Gabathōn-; Jehum, Ananis, Hananis* | *Nādāb-* | ***Nādābī*** 15:31, ***Jēhum, Anānis, Hanānis***; spellings noted |
| Elah, Zimri, Arza, Tirzah; Omri, Tibni, Ginath; Shemer, Samaria | *Ēla, Ēlæ, Zambri-, Arsæ, Thers-; Ambri-, Ambriānī, Thebni-, Thebniānōs, Ginethi; Semere, Samarī-* | *Ēla, Zambris, Thersa* | ***Thebnī*** 16:22, ***Gīnethī*** |
| Ahab, Ethbaal, Jezebel, Baal; Hiel, Abiram, Segub, Joshua, Nun | *Achāb-, Achābicīs, Ethbaalis, Jezabēl-, Baal-, Baalēns-; Hiel, Abīrāmum, Segubum, Jōsuam, Nūnis* | *Baal-, Abīrāmum, Jōsuam, Nūnis* | ***Hīēl, Segūbum*** |
| Elijah the Tishbite, Gilead; Cherith; Zarephath; Obadiah; Carmel; Kishon; Jezreel; Horeb | *Ēlī-, Thesbita, Galaadītidis; Carithum; Sarepht(h)am; Abdias; Carmēl-; Cisōnem; Jezræl; Hōrēb-* | *Ēlīās, Galaadīt-, Sarephtham, Carmēl-, Cisōnem, Jezræl, Hōrēb-* | ***Thesbīta, Thesbītā*** (overrides 21:28's row), ***Carīthum, Abdiās*** |
| Hazael, Jehu son of Nimshi, Elisha son of Shaphat, Abel-meholah | *Hazæl-, Jehu(s/m), Nansis, Elisæ-, Saphati, Abelmeholanum* | *Elisæō, Sāphātus, Ābēlmehōlæ* | ***Jēhūs, Jēhū, Jēhum, Sāphātī, Ābēlmehōlānum*** |
| Ben-hadad's war; Aphek | *Syr-, Aphēc* | *Syr-, Aphēc* | kept |
| Naboth the Jezreelite | *Naboth-* (18), *Jezrælēns-* | *Jezrælēns-* | ***Nābōth-*** (call 4) |
| Micaiah, Imlah, Zedekiah, Chenaanah, Amon, Joash; Ramoth-gilead | *Michæ-, Jemlæ, Sedecīās, Chanaanæ, Āmōnem, Joam; Rāmōth-, Galaadītārum* | *Āmōnem, Rāmōtha* | ***Chanaānæ, Jōam*** |
| Jehoshaphat, Azubah, Shilhi, Ahaziah, Joram; Ezion-geber, Ophir | *Jōsāphāt-, Azubam, Salis, Ochozias, Jorāmus; Asiongaber, Ophire* | *Jōsāphāt-, Jorāmus, Asiōngābre, Ophīren* | ***Azūbam, Ochoziās, Asiōngāber, Ophīre*** |

## Noticed, not changed

- **Lower-case name adjectives** the layout rows should capitalize, as 2 Samuel's: *isrāēlīticārum* 8:1, 8:16,
  *isrāēlīticī* 8:36, 8:52, *isrāēlīticō* 9:5, *solomōniānīs* 9:27 (lower case in the preview; whether a layout row
  covers them was not checked).
- *Achiæ* 21:22 beside *Ahiæ* 15:27, 15:33 for Baasha's father, and *Ananis/Hananis*: see the spelling table.
- 15:6 *inter Abiamum et Jeroboamum* (the Hebrew has Rehoboam): left for the notes, as the readers did.

## Report

- **Rows**: 106 in `names-forms.tsv` (*Nābōth-* 18 with its cases, *Jēhu* 6, *Abdiās* 4, *Ochoziās* 3, the rest one
  or two each); 4 override merged rows (2:26 r1, 4:12, 14:1, 21:28), the other 102 replace preview forms.
- **For Nathan**: calls 1 (Anathoth's case), 2 (*-as* against *-ās*), 4 (Hebrew-only marks), 6 (Jezabel's ē).
- **Spellings to unify** (draft fixes, not done here): *Nabathi → Nabati*, 21:22 *Achiæ → Ahiæ*, *Ananis/Hananis*,
  17:10 *Sarephtam → Sarephtham*, 22:48 *Asiongaber*, 2:26 *Anathota → Anathotha*, 4:9 *Bethsamem → Bethsemem*,
  *Chamosum/Chamoso → Chamoss-*.
