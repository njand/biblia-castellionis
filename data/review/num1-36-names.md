# Numbers: one form per person, place and clan (Claude, 2026-11-16)

Every capitalized name in `text/draft/NUM.preview.usfm` was grouped by its unmarked stem, matched to its Hebrew (WLC) and
Greek (Brenton), and decided in this order: the settled form (text/*.usfm, decision 46) beats everything; then Gaffiot
(or an analog Gaffiot gives), the Greek's η/ω/ει, another dictionary (Wiktionary bare = short), the Hebrew vowel
(decision 52). Clan adjectives carry the founder's marks on the stem and the suffix's quantity: -īnus (Nathan,
confirmed), -ānus, -iānus, -ius (short i), -ēnsis, -īta/-ītēs. Endings (case) are left as the preview has them.

Outputs: `names-spelling.tsv` (66 spelling changes in the unmarked draft, each `old` checked to occur once in its verse)
and `names-forms.tsv` (255 forms rows). The 48 Numbers -īnus fixes of `inus/fixes.tsv` are all inside it (with the
founder's marks added to the stem, e.g. *Jāsūbīna*, *Enāquīnōs*); its Exod 6:14 *Rūbēninæ* → *Rūbēnīnæ* is settled text
and needs a review item of its own. *Beniamin-* is no longer a spelling row (the approved rules now respell it); the forms
rows are written for *Benjāmīnēnsium* (1:36) and *Benjāmīneā* (13:9, 34:21).

## Hard calls (for Nathan)

1. **Genesis 46 / Exodus 6 harmonization** (settled beats; same Hebrew name in both places). Castellio printed these men
   differently in Numbers 26 and Numbers 3 than in Gen 46 / Exod 6 (the 1738 page of Gen 46 confirms *Immam*, *Cunim*,
   *Phuuam*, *Simeronem*, *Iahelem*, *Iaseelem*). Following the rule, Numbers takes the settled spelling: *Haggi→Hagī*,
   *Arieli→Areēlī*, *Phua→Phuva*, *Simbron-→Simerōn-*, *Sared-→Sered-*, *Jalel-→Jahēl-*, *Bala/Balæ→Bela/Belæ*,
   *Azbel-→Asbēl-*, *Ardes→Aredus*, *Jemna→Imma*, *Jessui→Isvī*, *Bria→Berīa*, *Saram→Seram*, *Jessiel-→Jaseēl-*,
   *Guni→Cūnī*, *Sellem-→Sillēm-*, *Libnia→Lebnia*, *Semeis/Semejana→Simeis/Simejāna*, *Moolis/-ia/-iana→Moholis…*,
   *Jesaar(iana)→Isaār(iāna)*, *Jochabeda(m)→Jacobeda(m)* (Exod 6:20), with their clan adjectives. 45 of the 66 spelling
   rows; they can be dropped as a block if Castellio's Numbers spellings are to stand. Where the Hebrew itself differs
   (Nemuel/Jemuel, Zerah/Zohar, Zephon/Ziphion, Ozni/Ezbon, Arod/Arodi, Jashub/Iob, Shephupham/Muppim, Hupham/Huppim,
   Shuham/Hushim, Ahiram/Ehi) Numbers keeps its own form.
2. **Caleb unmarked** (*Calēbus* → *Calebus*, 9 rows; 34:19 *Chalebus* → *Calebus*): Wiktionary *Caleb* is bare and
   the Greek Χάλεβ has no long letter, so decision 52 stops before the Hebrew ṣere.
3. **Amalekites** *Amālēchīt-* (Wiktionary *Amālēcīta*, founder settled *Amālēchus*), against the settled Gen 14:7
   *Amalechitārum*, Exod 17:16 *Amalechitīs* (unmarked): those two settled words should follow (not changed here).
4. **Ammonites** *Ammonīt-* as the settled Gen 19:38 *Ammonītæ*; Gaffiot *Ammōnītēs* marks the o. **Benjamites**
   7:12 *Benjāmītārum* keeps the founder's *Benjāmīn*; Gaffiot *Benjămītæ* has ă. **Jebusites** stay *Jebusæus*
   (settled) though Gaffiot has *Jĕbūsæī*. **Eleazar** stays unmarked (settled) though Gaffiot has *Elĕāzăr*;
   **Balac-/Balaam-** unmarked (settled Rev 2:14, 2 Pet 2:15) though the Hebrew has qamets.
5. **Samuēl** (34:20, Shemuel): Gaffiot *Sămŭēl*; the settled prophet is *Samūēl-* (Acts 3:24, 13:20, Heb 11:32),
   which by the same rule should become *Samuēl-* (not changed here).
6. **Sēla** (26:20, *Sēlāna*): settled Genesis has both *Sēlam* (38:5, 14) and *Selā* (38:11, 26; 46:12); the Hebrew
   ṣere decides *Sēl-*, and Gen's *Selā* ×3 should follow.
7. **Pharān-** (10:12, 12:16, 13:3, 13:26): Gaffiot *Phăran*, last a by the Hebrew qamets and the settled Gen 21:21
   *Pharāne*; the settled Gen 14:6 *Pharanem* disagrees.
8. **Melca** (26:33) over *Melcha* (27:1, 36:11): Hebrew kaf with dagesh, and Castellio's settled *Melca* for the same
   name (Gen 22); the majority in Numbers is *Melcha*.
9. **Phadasur** over *Phadassur* (two and two in Numbers): Hebrew single ṣade; the Greek Φαδασσούρ doubles it.
   **Achiezer** over *Achieser* (two and two): zayin, as the settled *Eliezer*. **Surisaddæi**, **Ammisaddæi**: dd (Hebrew
   dagesh; 5 of 8).
10. **Jeser** (26:30, Iezer, אִיעֶזֶר) left as spelled, unmarked, *Jeserīna*: read as 1738's *Ieser* with a vowel I it
    would be *Īeser*, but the draft's j-rule would respell it; left for you. It is a different man from *Jēser*
    (26:49, Jezer, settled Gen 46:24 *Jēserem*).
11. Not changed, flagged: 25:1 *Cittimō* is Shittim (בַּשִּׁטִּים), which Castellio writes *Sittīm-* at 33:49 (marked
    *Cittīmō* here); *Gadēsbarnēa* (32:8, 34:4) spells Kadesh with G as one compound name; 34:15 *Hiericho* is the only
    indeclinable form (elsewhere *Hierichūs, -ūntis*), marked *Hierichō*; *Arodonia* (26:17) may be a misprint for
    *Arodia* (Hebrew הָאֲרוֹדִי); *Sabamam* (32:3, 38) unmarked, the two Hebrew spellings disagree (שְׂבָם, שִׂבְמָה);
    *Aradus* (21:1, 33:40) unmarked by Wiktionary *Aradus* (bare) over the Hebrew qamets.

## Names checked and kept as the preview has them

Settled or already right: *Mōsēs, Aharōn, Marīa, Nādābus, Abīus, Eleazarus, Īthāmārus, Phīnees, Jōsua, Hōsēa,
Nūnis, Jephonis, Cōra, Dāthān, Abīrāmus, Ōn, Phelethī, Isrāēl-, Lēvīt-, Rūbēn-, Simeōn-, Jūda-, Issāchar-, Zabulōn-,
Ephrāim-, Manass-, Dan-, Āsēr-, Nephthāl-, Gad-, Gērsōn-, Cahath-, Merār-, Amrām-, Hebrōn-, Ozīēl-, Elsāphān,
Lāēlis, Sūrīēle, Henōchus, Phallus/Phallu, Hesrōn-, Carmis, Jāmīne, Jāchīne, Zara, Saulus, Sūnī, Ērī, Arōdō, Ēr,
Ōnan, Phārēs, Hāmūl, Thōla, Ēlōne, Māchīr, Galaad-, Sechem-, Maala, Nōa, Hegla, Thersa, Bechre, Thaane-, Naaman-,
Heber, Malcīēle, Jēsere, Salōmis, Ahīūdus, Elīaddus, Caselōnis, Boccis, Joglis, Hanīēl, Ēphōdī, Elīsāphān,
Pharnacī (Gaffiot Pharnăcēs), Phaltīēl, Phadaēl, Phaltis, Gaddis, Camallis, Michaēlis, Nahbis, Vopsis, Thalmæus,
Hōbābō, Ragūēlis, Madiānīt-, Mōabīt-, Balaam-, Balac-, Sephōris, Beōris, Pethōram, Agagum, Sēthō, Idūmæ-, Seir,
Cenæ-, Assyrius, Hebrem, Zambris, Cozbis, Sūris, Sūrem, Hūrem, Recemum, Rebam, Sēhōn, Ōgus, Nāzaræus (L&S
Nāzăraeus), Chananæ-, Amorræ-, Hettæus, Jebusæus*; places *Sīna (Sinai) / Sin- (Zin) / Sīnæ (Sin), Cadēs/Cade/Cadem,
Hōr-, Hormam, Ōbōth-, Abārium, Jeabārīm-, Zaredum, Arnōn-, Ār, Phasgæ, Jesīmōnem, Hesebōn-, Chamōssī, Dībōn-, Nōphan,
Jordān-, Hierichūntium, Atārōtha, Atrōtha, Nemram, Eleālē, Nabōnem, Beōnem, Baalmeōnem, Jogbaam, Bēthnemram,
Cariāthaim, Nōba, Canatham (Gaffiot Cănătha), Ramese, Sochothis, Ēthām-, Ahīrōth-, Baalsephōnis, Mārā, Ēlim-,
Raphīdīmō, Dopheā, Ālūsō, Rethmā, Remmōnphāre, Lebnā, Rissā, Ceēlāthā, Sāphare, Harādā, Macēlōthīs, Thāhathā,
Methchā, Hasmōnā, Mōsērōthīs, Jothabāthā, Abrōnā, Asiōngābre, Salmōnā, Phūnōne, Dībōngadō, Almōndeblāthaimā,
Bēthiesimōthīs, Sittīmōrum, Asmōn-, Sedādam, Zephrōnam, Sephām-, Reblam, Ainis, Cenerethī, Gadēsbarnēa, Escol-*
(changed), *Busta* (Latin).

## Decisions
| Person / place / clan | Found in the preview (verses) | Decided | Reason |
|---|---|---|---|
| Reubenite (tribe adjective) | *Rūbēninā* 1.5,13.4; *Rūbēnina* 34.14 | *Rūbēnīna, Rūbēnīnā* | settled *Rūbēn*; -īnus long (Nathan, 2026-11-16) |
| Elizur son of Shedeur (Reuben) | *Elīsūr* 1.5,7.12; *Elīsūre* 2.10; *Elīzūr* 10.18 | *Elīsūr, Elīsūre* (spelling changes) | Hebrew אֱלִיצוּר: ḥataf segol, ḥireq-yod, shureq; spelled with s as 1:5, 2:10, 7:12 (3 of 4) and as Castellio writes ṣade in Phadasur, Surisaddai / one spelling, as 1:5, 2:10, 7:12 *Elisur* |
| Shedeur | *Sedēūris* 1.5,2.10,7.12,10.18 | *Sedēūris* | Hebrew שְׁדֵיאוּר: ṣere-yod, shureq |
| Shelumiel son of Zurishaddai (Simeon) | *Salumīēl* 1.6,7.12,10.19; *Salumīēle* 2.12 | *Salumīēl, Salumīēle* | Hebrew שְׁלֻמִיאֵל: qibbuṣ short, ḥireq-yod; Greek Σαλαμιήλ η |
| Zurishaddai | *Sūrīsadæī* 1.6,2.12; *Sūrīsaddæī* 7.12,10.19 | *Sūrīsaddæī* (spelling changes) | one spelling, -sadd- (Hebrew dagesh; as 7:12, 10:19) / Hebrew צוּרִישַׁדָּי: shureq, ḥireq-yod, dagesh in d; spelled -sadd- as 7:12, 10:19 and as *Ammisaddæi* (3 of 4) |
| Nahshon son of Amminadab (Judah) | *Nahasōn* 1.7,2.3,7.12,10.14 | *Nahasōn* | settled Exod 6:23 *Nahasōnis* |
| Amminadab | *Amīnādābī* 1.7,2.3; *Ammīnādābī* 7.12,10.14 | *Ammīnādābī* (spelling changes) | one form: settled Exod 6:23 *Ammīnādābī* (decision 46; Luke 3:33, Matt 1:4 have *Amīnādāb-*) / settled Exod 6:23 *Ammīnādābī* (the OT form, decision 46) |
| Nethanel son of Zuar (Issachar) | *Nathanaēl* 1.8,7.12,10.15; *Nathanaēle* 2.5 | *Nathanaēl, Nathanaēle* | settled John 1 *Nathanaēl*; Greek Ναθαναήλ η |
| Zuar | *Sūāris* 1.8,2.5,7.12,10.15 | *Sūāris* | Hebrew צוּעָר: shureq, qamets; Greek Σωγάρ ω |
| Eliab son of Helon (Zebulun); Eliab son of Pallu (Reuben) | *Elīābus* 1.9,7.12,10.16,26.8; *Elīābō* 2.7; *Elīābī* 16.1,16.12,26.9 | *Elīābus, Elīābī, Elīābō* | Hebrew אֱלִיאָב: ḥireq-yod, qamets |
| Helon | *Hēlōnis* 1.9,2.7,7.12,10.16 | *Hēlōnis* | Hebrew חֵלֹן: ṣere, ḥolem; Greek Χαιλών ω |
| Elishama son of Ammihud (Ephraim) | *Elīsāma* 1.10,7.12,10.22; *Elīsāmā* 2.18 | *Elīsāma, Elīsāmā* | Hebrew אֱלִישָׁמָע: ḥireq-yod, qamets (nominative -a short) |
| Ammihud (father of Elishama, Shemuel, Pedahel) | *Ammīūdī* 1.10,2.18,7.12,10.22,34.20,34.28 | *Ammīūdī* | Hebrew עַמִּיהוּד: ḥireq-yod, shureq |
| Gamaliel son of Pedahzur (Manasseh) | *Gamaliēl* 1.10,7.12,10.23; *Gamaliēle* 2.20 | *Gamaliēl, Gamaliēle* | settled Acts 5:34 *Gamaliēl*; Wiktionary *Gamaliēl* |
| Pedahzur | *Phadāsūris* 1.10,10.23; *Phadāssūris* 2.20,7.12 | *Phadāsūris* (spelling changes) | Hebrew פְּדָהצוּר: qamets, shureq, one ṣade; spelled -s- as 1:10, 10:23 / one spelling, *Phadasur* as 1:10, 10:23 (Hebrew single ṣade; the Greek Φαδασσούρ doubles it) |
| Benjamin | *Benjāmīnēnsī* 1.11; *Benjāmīnēnsis* 2.22,10.24; *Benjāmīnis* 26.38,26.41; *Beniāmīnēnsium* 1.36; *Beniāmīneā* 13.9,34.21 | *Benjāmīneā, Benjāmīnis, Benjāmīnēnsis, Benjāmīnēnsium, Benjāmīnēnsī* | settled *Benjāmīn* / one spelling, the settled *Benjāmīn* (j as everywhere else) |
| Abidan son of Gideoni (Benjamin) | *Abīdām* 1.11; *Abīdāne* 2.22; *Abīdān* 7.12,10.24 | *Abīdān, Abīdāne* (spelling changes) | one spelling, *Abidan* as 2:22, 7:12, 10:24 (Hebrew nun; *Abidam* is Abida, Gen 25:4) / Hebrew אֲבִידָן: ḥireq-yod, qamets |
| Gideoni | *Gedeōnis* 1.11,2.22,7.12,10.24 | *Gedeōnis* | Gaffiot *Gĕdĕōn* (analog); Greek Γαδεωνί ω |
| Ahiezer son of Ammishaddai (Dan) | *Achīezer* 1.12; *Achīezere* 2.25; *Achīeser* 7.12,10.25 | *Achīezer, Achīezere* (spelling changes) | Hebrew אֲחִיעֶזֶר: ḥireq-yod, segol, segol; z for zayin as the settled *Eliezer* / one spelling, *Achiezer* as 1:12, 2:25 (zayin, as the settled *Eliezer*) |
| Ammishaddai | *Ammīsaddæī* 1.12,7.12,10.25; *Ammīsadæī* 2.25 | *Ammīsaddæī* (spelling changes) | Hebrew עַמִּישַׁדָּי: ḥireq-yod, dagesh in d / one spelling, -sadd- as 1:12, 7:12, 10:25 |
| Asherite (tribe adjective) | *Āsēriānā* 1.13,34.27; *Āsēriāna* 2.27; *Āssēriānōrum* 7.12; *Āssēriānæ* 10.26; *Āssēriānā* 13.13 | *Āsēriāna, Āsēriānæ, Āsēriānā, Āsēriānōrum* (spelling changes) | settled *Āsēr*; -iānus / one spelling, the settled *Āsēr* (1:13, 2:27, 34:27 *Aseriana*) |
| Pagiel son of Ochran (Asher) | *Phegīēl* 1.13,7.12,10.26; *Phegīēle* 2.27 | *Phegīēl, Phegīēle* | Hebrew פַּגְעִיאֵל: ḥireq-yod, ṣere; Greek Φαγαιήλ η |
| Ochran | *Ochrānis* 1.13,2.27,7.12,10.26 | *Ochrānis* | Hebrew עָכְרָן: qamets ḥatuf short, qamets |
| Gadite (tribe adjective) | *Gadinā* 1.14,13.15; *Gadinōrum* 7.12; *Gadinæ* 10.20; *Gadinī* 32.1,32.29,32.31,32.34; *Gadinīs* 32.33; *Gadina* 34.14 | *Gadīna, Gadīnæ, Gadīnā, Gadīnī, Gadīnīs, Gadīnōrum* | settled *Gadus* (stem unmarked); -īnus long (Nathan) |
| Eliasaph son of Deuel (Gad); Eliasaph son of Lael (Gershon) | *Eliāsāphus* 1.14,3.24,10.20; *Eliāsāphō* 2.14 | *Eliāsāphus, Eliāsāphō* | Hebrew אֶלְיָסָף: qamets, qamets |
| Deuel | *Dūēlis* 1.14,2.14,7.12,10.20 | *Dūēlis* | Hebrew דְּעוּאֵל: shureq, ṣere; Greek Ῥαγουήλ η |
| Naphtalite (tribe adjective) | *Nepthāliānā* 1.15 | *Nephthāliānā* (spelling changes) | one spelling, as 13:14 *Nephthaliana* and the settled *Nephthālis* |
| Ahira son of Enan (Naphtali) | *Ahīra* 1.15; *Achīrā* 2.29; *Achīra* 7.12,10.27 | *Achīra, Achīrā* (spelling changes) | one spelling, *Achira* as 2:29, 7:12, 10:27 / Hebrew אֲחִירַע: ḥireq-yod; ch for ḥet as 2:29, 7:12, 10:27 and *Achiezer*, *Achiman* |
| Enan | *Ēnānis* 1.15,2.29,7.12,10.27 | *Ēnānis* | Hebrew עֵינָן: ṣere-yod, qamets |
| Reuben | *Rūbēne* 1.20; *Rūbēnis* 1.21,2.10,26.5; *Rūbēnēnsium* 2.16,7.12,26.7; *Rūbēnēnsis* 10.18 | *Rūbēne, Rūbēnis, Rūbēnēnsis, Rūbēnēnsium* | settled *Rūbēn* |
| Shimei son of Gershon | *Semeis* 3.18 | *Simeis* (spelling changes) | one spelling, the settled *Simeīm* (Exod 6:17) |
| Izhar son of Kohath | *Jesaār* 3.19 | *Isaār* (spelling changes) | one spelling, the settled *Isaār* (Exod 6:18, 21) as Num 16:1 *Isaāris* |
| Mahli son of Merari | *Moolis* 3.20 | *Moholis* (spelling changes) | one spelling, the settled *Moholīm* (Exod 6:19) |
| Shimeite | *Semejāna* 3.21 | *Simejāna* (spelling changes) | founder settled *Simeī* (Exod 6:17 *Simeīm*); -ānus; the vowel before j unmarked |
| Kohathite | *Cahathinæ* 3.27; *Cahathinī* 3.29,4.15,10.21; *Cahathinōrum* 4.2,4.4,4.15,4.37; *Cahathinārum* 4.17; *Cahathinōs* 4.34; *Cahathinīs* 7.9; *Cahathina* 26.57 | *Cahathīna, Cahathīnæ, Cahathīnārum, Cahathīnī, Cahathīnīs, Cahathīnōrum, Cahathīnōs* | founder settled *Cahathus* (unmarked); -īnus long (Nathan) |
| Amramite | *Amrāmina* 3.27 | *Amrāmīna* | founder settled *Amrām*; -īnus long (Nathan) |
| Izharite | *Jesaāriāna* 3.27 | *Isaāriāna* (spelling changes) | founder settled *Isaār* (Exod 6:18, 21; Num 16:1); -iānus |
| Uzzielite | *Ozīēlina* 3.27 | *Ozīēlīna* | founder settled *Ozīēl*; -īnus long (Nathan) |
| Mahlite | *Mooliāna* 3.33; *Moolia* 26.58 | *Moholia, Moholiāna* (spelling changes) | founder settled *Moholī* (Exod 6:19 *Moholīm*); -iānus / founder settled *Moholī* (Exod 6:19 *Moholīm*) |
| Abihail | *Abīchailis* 3.35 | *Abīchāilis* | Hebrew אֲבִיחָיִל: ḥireq-yod, qamets |
| Eliasaph son of Deuel (Gad) | *Elisāphus* 7.12 | *Eliāsāphus* (spelling changes) | one spelling, *Eliasaphus* as 1:14, 2:14, 10:20 (Hebrew אֶלְיָסָף) |
| Benjamite | *Benjāmītārum* 7.12 | *Benjāmītārum* | the founder's settled *Benjāmīn*; -īta as *Isrāēlīta* (Gaffiot *Benjămītæ* has ă: see notes) |
| Paran | *Pharane* 10.12,12.16,13.3; *Pharanem* 13.26 | *Pharāne, Pharānem* | Gaffiot *Phăran* (first a short); last a qamets (Hebrew פָּארָן), as the settled Gen 21:21 *Pharāne* |
| Taberah | *Tabera* 11.3 | *Tabēra* | Hebrew תַּבְעֵרָה: ṣere |
| Eldad | *Eldadus* 11.26; *Eldadum* 11.27 | *Eldādum, Eldādus* | Hebrew אֶלְדָּד: segol, qamets |
| Medad | *Medadus* 11.26; *Medadum* 11.27 | *Mēdādum, Mēdādus* | Hebrew מֵידָד: ṣere-yod, qamets; Greek Μωδάδ ω |
| Hazeroth | *Haserotha* 11.35; *Haserothīs* 12.1,12.16; *Hazērōthīs* 33.17 | *Hasērōtha, Hasērōthīs* (spelling changes) | Hebrew חֲצֵרוֹת: ṣere, ḥolem; Greek Ἀσηρώθ η, ω / one spelling, *Haseroth* as 11:35, 12:1, 12:16 |
| Shammua son of Zaccur | *Samua* 13.4 | *Samūa* | Hebrew שַׁמּוּעַ: shureq |
| Zaccur | *Zaccuris* 13.4 | *Zaccūris* | Hebrew זַכּוּר: shureq; Greek Ζαχούρ |
| Shaphat son of Hori | *Saphatus* 13.5 | *Sāphātus* | Hebrew שָׁפָט: qamets, qamets |
| Hori | *Horis* 13.5 | *Hōris* | Hebrew חוֹרִי: ḥolem |
| Caleb son of Jephunneh | *Calēbus* 13.6,13.30,14.6,14.38; *Calēbum* 14.24; *Calēbō* 14.30,26.65,32.12; *Chalēbus* 34.19 | *Calebum, Calebus, Calebō* (spelling changes) | Wiktionary *Caleb* (bare vowels short, decision 52; Greek Χάλεβ has no long letter) / one spelling, *Calebus* as 13:6, 14:6 … (Hebrew כָּלֵב, kaf with dagesh) |
| Igal son of Joseph | *Igal* 13.7 | *Igāl* | Hebrew יִגְאָל: ḥireq, qamets |
| Ephraimite (tribe adjective) | *Ephrāiminā* 13.8,34.24 | *Ephrāimīnā* | settled *Ephrāim*; -īnus long (Nathan) |
| Raphu | *Raphuis* 13.9 | *Rāphūis* | Hebrew רָפוּא: qamets, shureq |
| Gaddiel son of Sodi | *Gadiel* 13.10 | *Gadīēl* | Hebrew גַּדִּיאֵל: ḥireq-yod, ṣere; Greek Γουδιήλ η |
| Sodi | *Sodis* 13.10 | *Sōdis* | Hebrew סוֹדִי: ḥolem |
| Susi | *Susis* 13.11 | *Sūsis* | Hebrew סוּסִי: shureq |
| Ammiel son of Gemalli | *Ammiel* 13.12 | *Ammīēl* | Hebrew עַמִּיאֵל: ḥireq-yod, ṣere; Greek Ἀμιήλ η |
| Sethur son of Michael | *Sathur* 13.13 | *Sathūr* | Hebrew סְתוּר: shureq; Greek Σαθούρ |
| Geuel son of Machi | *Guel* 13.15 | *Gūēl* | Hebrew גְּאוּאֵל: shureq, ṣere; Greek -ιήλ η |
| Machi | *Machis* 13.15 | *Māchis* | Hebrew מָכִי: qamets |
| Rehob | *Rohob* 13.21 | *Rohōb* | Hebrew רְחֹב: ḥolem |
| Hamath | *Hematham* 13.21,34.8 | *Hemātham* | Hebrew חֲמָת: qamets |
| Ahiman | *Achiman* 13.22 | *Achīman* | Hebrew אֲחִימַן: ḥireq-yod, pataḥ |
| Sheshai | *Sesæus* 13.22 | *Sēsæus* | Hebrew שֵׁשַׁי: ṣere |
| Anak | *Enaquō* 13.22 | *Enāquō* | Hebrew עֲנָק: ḥataf pataḥ, qamets |
| Zoan | *Soanem* 13.22 | *Sōanem* | Hebrew צֹעַן: ḥolem |
| Eshcol | *Escolem* 13.23,32.9; *Escol* 13.24 | *Escōl, Escōlem* | Hebrew אֶשְׁכֹּל: ḥolem |
| Anakim (adjective) | *Enaquinōs* 13.28,13.33 | *Enāquīnōs* | founder Anak, Hebrew עֲנָק qamets; -īnus long (Nathan) |
| Amalekite | *Amalechita* 13.29,24.20; *Amalechitās* 14.25,24.20; *Amalechitam* 14.43; *Amalechitæ* 14.45 | *Amālēchīta, Amālēchītam, Amālēchītæ, Amālēchītās* | Wiktionary *Amālēcīta*; the settled founder *Amālēchus* (Exod 17); -īta (settled Gen 14:7, Exod 17:16 *Amalechit-* unmarked: see notes) |
| Mattanah | *Mattanam* 21.19; *Mattanā* 21.19 | *Mattānam, Mattānā* | Hebrew מַתָּנָה: qamets |
| Nahaliel | *Nahaliēl* 21.19; *Nahaliēle* 21.19 | *Nahalīēl, Nahalīēle* | Hebrew נַחֲלִיאֵל: ḥireq-yod, ṣere; Greek Νααλιήλ η |
| Bamoth | *Bamōtha* 21.19; *Bamōthīs* 21.20 | *Bāmōtha, Bāmōthīs* | Hebrew בָּמוֹת: qamets, ḥolem; Greek Βαμώθ ω |
| Jahaz | *Jasam* 21.23 | *Jāsam* | Hebrew יָהְצָה: qamets |
| Jabbok | *Jabbocum* 21.24 | *Jabbōcum* | Hebrew יַבֹּק: ḥolem |
| Ammonite | *Ammonitās* 21.24; *Ammonitārum* 21.24 | *Ammonītārum, Ammonītās* | settled Gen 19:38 *Ammonītæ* (Gaffiot *Ammōnītēs* marks the o: see notes) |
| Medeba | *Medebam* 21.30 | *Mēdebam* | Hebrew מֵידְבָא: ṣere-yod |
| Jazer | *Jasēr* 21.32 | *Jazēr* (spelling changes) | one spelling, *Jazer* as 32:1, 3, 35 (Hebrew zayin); Greek Ἰαζήρ η |
| Bashan | *Bāsanam* 21.33; *Bāsanæ* 21.33,32.33 | *Bāsānam, Bāsānæ* | Hebrew הַבָּשָׁן: qamets, qamets |
| Edrei | *Edrei* 21.33 | *Edreī* | Hebrew אֶדְרֶעִי: ḥireq-yod |
| Peor | *Phegoris* 23.28,25.18,31.16; *Phegorem* 25.18 | *Phegōrem, Phegōris* | Hebrew פְּעוֹר ḥolem; Greek Φογώρ ω |
| Kittim | *Cittimōrum* 24.24; *Cittimō* 25.1 | *Cittīmō, Cittīmōrum* | Hebrew כִּתִּים: ḥireq-yod |
| Baal-peor | *Baalphegore* 25.3,25.5 | *Baalphegōre* | as *Phegōr* |
| Salu | *Salu* 25.14 | *Sālū* | Hebrew סָלוּא: qamets, shureq |
| Hanochite | *Henochiōrum* 26.5 | *Henōchiōrum* | founder settled *Henōchus* (Gen 46:9, Exod 6:14) |
| Nemuel son of Simeon; Nemuel son of Eliab | *Namuel* 26.9; *Namuele* 26.12 | *Namūēl, Namūēle* | Hebrew נְמוּאֵל: shureq, ṣere; Greek Ναμουήλ η |
| Nemuelite | *Namuelina* 26.12 | *Namūēlīna* | founder Nemuel: Hebrew נְמוּאֵל shureq, ṣere; Greek Ναμουήλ η; -īnus (Nathan) |
| Jaminite | *Jaminia* 26.12 | *Jāmīnia* | founder settled *Jāmīn* (Exod 6:15) |
| Jachinite | *Jachinia* 26.12 | *Jāchīnia* | founder settled *Jāchīn* (Exod 6:15) |
| Zerahite | *Zarana* 26.13,26.20 | *Zarāna* | founder settled *Zara* (Gaffiot *Zara*); -ānus |
| Shaulite | *Saulina* 26.13 | *Saulīna* | founder settled *Saulus* (Gen 46:10, Exod 6:15); -īnus (Nathan) |
| Zephon son of Gad | *Sephone* 26.15 | *Sephōne* | Hebrew צְפוֹן ḥolem; Greek Σαφών ω (not Gen 46:16 Ziphion, צִפְיוֹן) |
| Zephonite | *Sephonia* 26.15 | *Sephōnia* | founder Zephon: Hebrew צְפוֹן ḥolem; Greek Σαφών ω |
| Haggi son of Gad | *Haggi* 26.15 | *Hagī* (spelling changes) | one form, the settled Gen 46:16 *Hagīm* (Hebrew חַגִּי in both) |
| Haggite | *Haggia* 26.15 | *Hagia* (spelling changes) | founder Haggi as settled Gen 46:16 *Hagīm*; -ius |
| Shunite | *Sunia* 26.15 | *Sūnia* | founder settled *Sūnī* (Gen 46:16 *Sūnīm*) |
| Ozni son of Gad | *Ozni* 26.16 | *Oznī* | Hebrew אָזְנִי: qamets ḥatuf, ḥireq-yod (as the settled *Sūnīm*, *Ērīm*) |
| Oznite | *Oznia* 26.16 | *Oznia* | founder Ozni; -ius |
| Erite | *Eria* 26.16 | *Ēria* | founder settled *Ērī* (Gen 46:16 *Ērīm*) |
| Arodite | *Arodonia* 26.17 | *Arōdonia* | founder *Arōdus* (Hebrew ḥolem; settled Gen 46:16 *Arōdīm*) |
| Areli son of Gad | *Arieli* 26.17 | *Areēlī* (spelling changes) | one form, the settled Gen 46:16 *Areēlīm* (Hebrew אַרְאֵלִי in both) |
| Arelite | *Arielia* 26.17 | *Areēlia* (spelling changes) | founder Areli as settled Gen 46:16 *Areēlīm* |
| Shelanite | *Selana* 26.20 | *Sēlāna* | founder *Sēla* (Hebrew שֵׁלָה ṣere; settled Gen 38:5 *Sēlam*); -ānus |
| Perezite | *Pharesia* 26.20 | *Phārēsia* | founder settled *Phārēs* |
| Hamulite | *Hamulia* 26.21 | *Hāmūlia* | founder settled *Hāmūl* (Gen 46:12) |
| Tolaite | *Tholana* 26.23 | *Thōlāna* | founder settled *Thōla* (Gen 46:13); -ānus |
| Puvah son of Issachar | *Phūā* 26.23 | *Phuva* (spelling changes) | one form, the settled Gen 46:13 *Phuvam* (Hebrew פֻּוָּה in both) |
| Punite | *Phuana* 26.23 | *Phuvāna* (spelling changes) | founder Puvah as settled Gen 46:13 *Phuvam*; -ānus |
| Jashub son of Issachar | *Jasubō* 26.24 | *Jāsūbō* | Hebrew יָשׁוּב: qamets, shureq (not Gen 46:13 Iob, יוֹב) |
| Jashubite | *Jasubina* 26.24 | *Jāsūbīna* | founder Jashub: Hebrew יָשׁוּב qamets, shureq; -īnus (Nathan) |
| Shimron son of Issachar | *Simbrone* 26.24 | *Simerōne* (spelling changes) | one form, the settled Gen 46:13 *Simerōnem* (Hebrew שִׁמְרֹן in both) |
| Shimronite | *Simbronia* 26.24 | *Simerōnia* (spelling changes) | founder Shimron as settled Gen 46:13 *Simerōnem* |
| Sered son of Zebulun | *Saredō* 26.26 | *Seredō* (spelling changes) | one form, the settled Gen 46:14 *Seredum* (Hebrew סֶרֶד in both) |
| Seredite | *Saredina* 26.26 | *Seredīna* (spelling changes) | founder Sered as settled Gen 46:14 *Seredum*; -īnus (Nathan) |
| Elonite | *Elonia* 26.26 | *Ēlōnia* | founder settled *Ēlōn* (Gen 46:14) |
| Jahleel son of Zebulun | *Jalele* 26.26 | *Jahēle* (spelling changes) | one form, the settled Gen 46:14 *Jahēlem* (Hebrew יַחְלְאֵל in both) |
| Jahleelite | *Jalelina* 26.26 | *Jahēlīna* (spelling changes) | founder Jahleel as settled Gen 46:14 *Jahēlem*; -īnus (Nathan) |
| Machirite | *Machiriana* 26.29 | *Māchīriāna* | founder settled *Māchīr*; -iānus |
| Gileadite | *Galaadina* 26.29 | *Galaadīna* | founder settled *Galaadus* (unmarked); -īnus (Nathan) |
| Iezerite | *Jeserina* 26.30 | *Jeserīna* | founder Iezer (Jeser, unmarked: see notes); -īnus (Nathan) |
| Helek son of Gilead; Helekite | *Helecus* 26.30; *Helecia* 26.30 | *Hēlecia, Hēlecus* | Hebrew חֵלֶק: ṣere, segol |
| Asriel son of Gilead | *Asriel* 26.31 | *Asrīēl* | Hebrew אַשְׂרִיאֵל: ḥireq-yod, ṣere; Greek Ἐσριήλ η |
| Asrielite | *Asrielina* 26.31 | *Asrīēlīna* | founder Asriel; -īnus (Nathan) |
| Shemida son of Gilead | *Semida* 26.32 | *Semīda* | Hebrew שְׁמִידָע: ḥireq-yod (nominative -a short) |
| Shemidaite | *Semidana* 26.32 | *Semīdāna* | founder Shemida; -ānus |
| Hepher son of Gilead | *Hepher* 26.32; *Hephris* 26.33,27.1 | *Hēpher, Hēphris* | Hebrew חֵפֶר: ṣere, segol / Hebrew חֵפֶר: ṣere |
| Hepherite | *Hepheriana* 26.32 | *Hēpheriāna* | founder Hepher; -iānus |
| Zelophehad | *Salphaadus* 26.33; *Salphaadī* 27.1,27.7,36.2,36.6,36.10,36.11 | *Salphaādus, Salphaādī* | Hebrew צְלָפְחָד: qamets ḥatuf, qamets in the last syllable |
| Shuthelah son of Ephraim | *Suthalā* 26.35; *Suthalæ* 26.36 | *Sūthalæ, Sūthalā* | Hebrew שׁוּתֶלַח: shureq; Greek Σουθαλά |
| Shuthalhite | *Suthalana* 26.35 | *Sūthalāna* | founder Shuthelah; -ānus |
| Becherite | *Becheriana* 26.35 | *Becheriāna* | founder Becher (unmarked, settled Gen 46:21 *Becherem*); -iānus |
| Eran son of Shuthelah | *Eran* 26.36 | *Ērān* | Hebrew עֵרָן: ṣere, qamets |
| Eranite | *Erania* 26.36 | *Ērānia* | founder Eran |
| Bela son of Benjamin | *Balā* 26.38; *Balæ* 26.40 | *Bela, Belæ* (spelling changes) | one form, the settled Gen 46:21 *Belam* (Hebrew בֶּלַע in both) / one form, the settled Gen 46:21 *Belam* |
| Belaite | *Balana* 26.38 | *Belāna* (spelling changes) | founder Bela as settled Gen 46:21 *Belam*; -ānus |
| Ashbel son of Benjamin | *Azbele* 26.38 | *Asbēle* (spelling changes) | one form, the settled Gen 46:21 *Asbēlem* (Hebrew אַשְׁבֵּל in both) |
| Ashbelite | *Azbelina* 26.38 | *Asbēlīna* (spelling changes) | founder Ashbel as settled Gen 46:21 *Asbēlem*; -īnus (Nathan) |
| Ahiram son of Benjamin | *Achiramō* 26.38 | *Achīrāmō* | Hebrew אֲחִירָם: ḥireq-yod, qamets |
| Ahiramite | *Achiramina* 26.38 | *Achīrāmīna* | founder Ahiram; -īnus (Nathan) |
| Shephupham son of Benjamin | *Suphamō* 26.39 | *Sūphāmō* | Hebrew שְׁפוּפָם: shureq, qamets; Greek Σωφάν ω |
| Shuphamite | *Suphamina* 26.39 | *Sūphāmīna* | founder Shephupham; -īnus (Nathan) |
| Hupham son of Benjamin | *Huphamō* 26.39 | *Hūphāmō* | Hebrew חוּפָם: shureq, qamets (not Gen 46:21 Huppim, חֻפִּים) |
| Huphamite | *Huphamina* 26.39 | *Hūphāmīna* | founder Hupham; -īnus (Nathan) |
| Ard son of Bela | *Ārdēs* 26.40 | *Aredus* (spelling changes) | one form, the settled Gen 46:21 *Aredum* (Hebrew אַרְדְּ in both) |
| Ardite | *Ardiana* 26.40 | *Arediāna* (spelling changes) | founder Ard as settled Gen 46:21 *Aredum*; -iānus |
| Shuham son of Dan | *Suhamō* 26.42,26.43 | *Sūhāmō* | Hebrew שׁוּחָם: shureq, qamets (not Gen 46:23 Hushim, חֻשִׁים) |
| Shuhamite | *Suhamina* 26.42 | *Sūhāmīna* | founder Shuham; -īnus (Nathan) |
| Imnah son of Asher | *Jemnā* 26.44 | *Imma* (spelling changes) | one form, the settled Gen 46:17 *Immam* (Hebrew יִמְנָה in both) |
| Imnite | *Jemnana* 26.44 | *Immāna* (spelling changes) | founder Imnah as settled Gen 46:17 *Immam*; -ānus |
| Ishvi son of Asher | *Jessui* 26.44 | *Isvī* (spelling changes) | one form, the settled Gen 46:17 *Isvīm* (Hebrew יִשְׁוִי in both) |
| Ishvite | *Jessujana* 26.44 | *Isviāna* (spelling changes) | founder Ishvi as settled Gen 46:17 *Isvīm*; -ānus |
| Beriah son of Asher | *Briā* 26.44; *Briæ* 26.45 | *Berīæ, Berīā* (spelling changes) | one form, the settled Gen 46:17 *Berīa*, *Berīam* (Hebrew בְּרִיעָה in both) |
| Beriite | *Briana* 26.44 | *Berīāna* (spelling changes) | founder Beriah as settled Gen 46:17 *Berīa*; -ānus |
| Heberite | *Heberiana* 26.45 | *Heberiāna* | founder settled *Heber* (Gen 46:17 *Hebrem*, unmarked); -iānus |
| Malchielite | *Malcielina* 26.45 | *Malcīēlīna* | founder settled *Malcīēl* (Gen 46:17); -īnus (Nathan) |
| Serah daughter of Asher | *Saram* 26.46 | *Seram* (spelling changes) | one form, the settled Gen 46:17 *Seram* (Hebrew שָׂרַח in both) |
| Jahzeel son of Naphtali | *Jessiele* 26.48 | *Jaseēle* (spelling changes) | one form, the settled Gen 46:24 *Jaseēlem* (Hebrew יַחְצְאֵל in both) |
| Jahzeelite | *Jessielina* 26.48 | *Jaseēlīna* (spelling changes) | founder Jahzeel as settled Gen 46:24 *Jaseēlem*; -īnus (Nathan) |
| Guni son of Naphtali | *Guni* 26.48 | *Cūnī* (spelling changes) | one form, the settled Gen 46:24 *Cūnīm* (Hebrew גּוּנִי in both) |
| Gunite | *Guniana* 26.48 | *Cūniāna* (spelling changes) | founder Guni as settled Gen 46:24 *Cūnīm*; -iānus |
| Jezerite | *Jeseriana* 26.49 | *Jēseriāna* | founder settled *Jēser* (Gen 46:24 *Jēserem*); -iānus |
| Shillem son of Naphtali | *Sellemō* 26.49 | *Sillēmō* (spelling changes) | one form, the settled Gen 46:24 *Sillēmum* (Hebrew שִׁלֵּם in both) |
| Shillemite | *Sellemina* 26.49 | *Sillēmīna* (spelling changes) | founder Shillem as settled Gen 46:24 *Sillēmum*; -īnus (Nathan) |
| Merarite | *Merarina* 26.57 | *Merārīna* | founder settled *Merāris*; -īnus long (Nathan) |
| Libnite | *Libnia* 26.58 | *Lebnia* (spelling changes) | founder settled *Lebnī* (Exod 6:17 *Lebnīm*; Num 3:18, 21 *Lebn-*) |
| Mushite | *Musia* 26.58 | *Mūsia* | founder *Mūsis* (settled Exod 6:19 *Mūsīm*) |
| Korahite | *Coreja* 26.58 | *Cōreja* | founder settled *Cōra* |
| Jochebed | *Jochabedam* 26.59; *Jochabedā* 26.59 | *Jacobedam, Jacobedā* (spelling changes) | one form, the settled Exod 6:20 *Jacobedam* (unmarked there by decision) |
| Milcah daughter of Zelophehad | *Melcha* 27.1,36.11 | *Melca* (spelling changes) | one spelling, *Melca* as 26:33 and the settled *Melca* (Gen 22, same Hebrew מִלְכָּה, kaf with dagesh) |
| Abarim | *Abārim* 27.12 | *Abārīm* | Hebrew עֲבָרִים: qamets, ḥireq-yod (as 33:44 *Jeabārīmō*) |
| Evi king of Midian | *Evim* 31.8 | *Evīm* | Hebrew אֱוִי: ḥireq-yod; Greek Εὐείν ει; accusative in -īm as the settled *Carmīm* |
| Aroer | *Aroēr* 32.34 | *Arōēr* | Hebrew עֲרֹעֵר: ḥolem, ṣere; Greek Ἀροήρ η |
| Atroth-shophan | *Sōphanem* 32.35 | *Sōphānem* | Hebrew שׁוֹפָן: ḥolem, qamets; Greek Σωφάρ ω |
| Beth-haran | *Bēthāranem* 32.36 | *Bēthārānem* | Hebrew בֵּית הָרָן: qamets, qamets |
| Jair son of Manasseh | *Jaīr* 32.41; *Jaīrī* 32.41 | *Jāīr, Jāīrī* | Hebrew יָאִיר: qamets, ḥireq-yod |
| Migdol | *Magdal* 33.7 | *Magdōl* (spelling changes) | one form, the settled Exod 14:2 *Magdōl* |
| Terah (camp) | *Tharā* 33.27 | *Thārā* | Hebrew תָּרַח: qamets (not the man Terah, תֶּרַח, settled *Thara*) |
| Bene-jaakan | *Benejaacane* 33.31 | *Benējaacāne* | Hebrew בְּנֵי יַעֲקָן: ṣere-yod; qamets |
| Hor-haggidgad | *Hōrgadgadō* 33.32 | *Hōrgadgādō* | Hebrew חֹר הַגִּדְגָּד: ḥolem; qamets |
| Hazar-addar | *Hazaradar* 34.4 | *Hazaradār* | Hebrew חֲצַר־אַדָּר: qamets in the last syllable |
| Hazar-enan | *Hazarēnanem* 34.9; *Hazarēnane* 34.10 | *Hazarēnāne, Hazarēnānem* | Hebrew חֲצַר עֵינָן: ṣere-yod, qamets |
| Jericho | *Hiericho* 34.15 | *Hierichō* | Gaffiot *Ierichō*, *Jĕrīchō* (final ō); the stem short as Gaffiot *Hĭĕrĭcūs* and the settled *Hierichūnt-* |
| Shemuel son of Ammihud | *Samūēl* 34.20 | *Samuēl* | Gaffiot *Sămŭēl* (the same name; see notes on the settled *Samūēl-*) |
| Kemuel son of Shiphtan | *Camuēl* 34.24 | *Camūēl* | Hebrew קְמוּאֵל: shureq, ṣere; Greek Καμουήλ η |
| Shiphtan | *Sephthanis* 34.24 | *Sephthānis* | Hebrew שִׁפְטָן: qamets |
| Azzan | *Azanis* 34.26 | *Azānis* | Hebrew עַזָּן: qamets |
