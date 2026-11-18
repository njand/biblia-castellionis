# Deuteronomy: one form per person, place and people (Claude, 2026-11-18)

Every capitalized word of `text/draft/DEU.usfm` and its preview (`DEU.preview.usfm`), and every lower-case adjective of a
people or place, grouped by its unmarked stem, matched to the Hebrew (WLC) and the Greek (Brenton), and decided as
Numbers was (`num1-36-names.md`): the settled form first (decision 46, `data/gold/`), then Gaffiot (or an analog it
gives), the Greek's η/ω/ει, another dictionary (Wiktionary bare = short), the Hebrew vowel (decision 52). Clan and
gentile adjectives carry the founder's marks and the suffix's quantity: -īnus (Nathan), -iānus, -ius (short i), -ēnsis,
-īta, -ēus (as the settled *Jācōbēus*). Endings (case) read in each verse.

**Counted**: 119 rows below, about 135 persons, places and peoples (a founder and his clan adjective, or a place and its people, share a row); 52 rows kept as proposed, the rest changed.
**Outputs**: `names.spelling.tsv` (15 spelling changes, each `old` checked to occur once in its verse) and
`names.forms.tsv` (122 forms rows; the 15 rows for respelled words take effect once the spelling rows are applied).
Tested with the readers' check (`r9.forms.tsv`, all chapters, no error from these rows; the three *cis-/trans-*
rows were left out of the test, since before the respelling *cisiordaninam* and *cisjordānīnam* share a lexicon key
but not a spelling, and the check would refuse them).

## Hard calls (for Nathan)

1. **Kadesh-barnea: *Cadēsbarnēa*** (1:2, 1:19, 2:14, 9:23), Deuteronomy's own spelling, four times. The settled text
   spells the place both ways: *Gadēsbarnēā/-am* (Num 32:8, 34:4, flagged and kept in Numbers) and Kadesh alone
   *Cadēs, Cade, Cadem* (Num 33:36; Deut 1:46, 32:51 here). With G, Deuteronomy would have *Cadem* (1:46) and
   *Gadesbarnea* (1:2) for one place. My choice: C here, and Num 32:8, 34:4 to follow in a review item of their own
   (Hebrew קָדֵשׁ, qof). If the settled G is to win, four spelling rows (*Cadesbarnea* → *Gadesbarnea*) replace the forms.
2. **Emim → *Emenses*** (2:10, 2:11; 1738 *Emes*): the same people (הָאֵמִים; Gen 14:5 הָאֵימִים) as the settled Gen 14:5
   *Emēnsēs* (E unmarked there). As Numbers' *Ardes → Aredus*. If Castellio's *Emes* should stand, drop the two rows and
   mark *Ēmēs* (Hebrew tsere) or *Emēs* (the settled E).
3. ***Hebræus*, *Hebræa*** (15:12; 1738 *Ebraeus, Ebraea*): the settled text has both, *Hebr-* in Exod 1–2, 21:2 (the
   same law), Gen 10:21, 14:13 and the NT (about 25), *Ebr-* in Gen 39:14, 17, 40:15, 41:12, 43:32 (5). Hebraeus is the
   majority and the dictionaries' spelling (Wiktionary *hebraeus*). The five Genesis *Ebr-* should follow (not changed here).
4. ***Jaacānēnsium*** (10:6; 1738 *Jaquanensium*): Jaakan (יַעֲקָן) as in the settled Num 33:31 *Benējaacāne*. Castellio
   writes ק as *qu* elsewhere (*Enaquinus*, *Jabboquus*); the rule (one form) decides. Drop the row to keep *Jaquān-*.
5. ***Seboimōrum*** (29:23; 1738 *Sebojum*, genitive plural): Zeboiim as the settled Gen 14:2 *Seboimōrum* (same Hebrew
   צְבֹיִם, the same case). The respelling adds a syllable (Castellio's Deuteronomy declines *Seboi-*); the precedent is
   Numbers' *Phua → Phuva*, *Ardes → Aredus*.
6. ***Beōris*** for Balaam's father (23:4; 1738 ***Phegoris***, and 1726 the same, so Castellio's own): Beor (בְּעוֹר,
   LXX Βεώρ) is not Peor (פְּעוֹר, *Phegor*); the settled Num 22:5, 31:8 have *Balaamum … Beōris fīlium*. A correction of
   Castellio's confusion in the edited text, the printed text keeping *Phegoris* (as 25:1 *Sittīmō* in Numbers).
   Drop the row if *Phegoris* should stand.
7. **Jabbok *Jabbōc-***, **Chinnereth *Cenereth-***, **Pisgah *Phasgæ*** (34:1 *Phasge*), **Perizzites *Pherezæōs*** (7:1
   *Pheresaeos*): one spelling, the settled form (Num 21:24 *Jabbōcum*, Gen 32:22 *Jabbocī*; Num 34:11 *Cenerethī*,
   though the Hebrew כִּנֶּרֶת doubles the n as 1738's *Cenneretho*; Num 21:20 *Phasgæ*; Gen 15:20 *Pherezæōs*).
8. ***cisjordānīn-*** with *cis* short (Gaffiot cĭs, L&S and Wiktionary *cis*); the settled text has the preposition
   *cīs* 7 times (and the preview proposes *cīs* in Deut 1:1, 1:5 and elsewhere): a slip in the settled marking, to be
   reviewed separately (not a name; left to the readers here).
9. ***Seiris*** (2:4, 2:8, 2:22, 2:29) with the genitive's short -is (*fratrum … Seiris incolarum*, the inhabitants of
   Seir); the preview had *Seirīs* from the settled Gen 14:6 *montānīs Seirīs* and 36:21 *Seirīs fīliī*, both genitives
   too, so both settled ī are slips (not changed here).
10. ***Sodomitānīs*** (32:32): the settled Gen 19:4 *Sodomitānī* (the OT's), against Matt 10:15 *Sodomītānōrum*; no
    dictionary has the word. Gen 18:20 *Sodomitārum* is unmarked as well; Greek Σοδομῖται would give *-īt-*.
11. **Mount Sion *Sēōnem*** (4:48, שִׂיאֹן, LXX Σηών) is not Sihon (סִיחוֹן, *Sēhōn*): spelling kept, marked by the Greek.
    **Moserah *Mōsēram*** (10:6, מוֹסֵרָה) and **Gudgodah *Gadgādam*** (10:7, הַגֻּדְגֹּדָה) are different Hebrew forms from
    Num 33's *Mōsērōthīs* and *Hōrgadgādō*: spellings kept, marked alike.

## Settled forms that disagree (not changed: settled text is never rewritten)

- With Gaffiot: *Ēsāō, Ēsāī* (Gaffiot *Esāū*, E unmarked); *Ammonīt-* (Gaffiot *Ammōnītēs*; as in Numbers' notes);
  *Zabulōn-* (Gaffiot *Zăbŭlōn*, agreeing); *Nabōnem* (Gaffiot *Nebō*, agreeing on ō).
- With each other: *Galaādum, Galaādō* (Num 32, 4 + 3) against *Galaadī* (3) and *Galaadīna*; *Jabbocī* (Gen 32:22)
  against *Jabbōcum* (Num 21:24); *Choriōs* (Gen 14:6) against *Hōriō, Hōriōrum, Hōrium* (Gen 36:20–22) for the
  Horites; *Sodomitānī* (Gen 19:4) against *Sodomītānōrum* (Matt 10:15); *Ebr-* (Gen, 5) against *Hebr-*;
  Naphtali's adjective *Nephthāliānā* and *Nephthāliēnsis* (Num) against *Nephthālēnsibus* (Matt 4:13, followed here as
  Deuteronomy's own *Nephthalenses*); *Seirīs* (genitive, Gen 14:6, 36:21; see 9); *cīs* (see 8).

## Noticed, not names

- **15:19 *marīa*** in the preview: *pecore maria* is *mās, maris*, neuter plural *maria* (males); the pipeline took the
  settled name *Marīa*. For the reader of chapter 15.
- Two readers' layout rows stop the check: r2 `Deut.4.9` (*aduertite* for the draft's *advertite*) and r8 `Deut.32.30`
  (*fieri ne* for the draft's *fierine*).

## Decisions

| Person / place / people | Hebrew · Greek | In Deuteronomy (preview) | Decided | Reason |
|---|---|---|---|---|
| Moses | מֹשֶׁה · Μωυσῆς | *Mōsēs, Mōsem(que), Mōsī, Mōsis* | kept | settled |
| Aaron | אַהֲרֹן | *Aharōn, Aharōne* 9.20, 10.6, 32.50 | kept | settled |
| Eleazar | אֶלְעָזָר | *Eleāzarus* 10.6 | kept | settled (Numbers' call 2) |
| Abraham, Isaac, Jacob | | *Abrāhāmō/-ī, Isaacō/-ī, Jācōbō/-ī/-us* | kept | settled |
| Jacob's people (*Jācōbēus*) | | *Jacobei* 32.9; *Jācōbēōrum* 33.4; *Jācōbēōs* 33.10 | *Jācōbēī* | settled *Jācōbēus* |
| Esau | עֵשָׂו · Ἡσαῦ | *Ēsāō* 2.4, 2.5, 2.8 | kept | settled (Gaffiot *Esāū*: see above) |
| Esau's people | בְּנֵי עֵשָׂו | *Esainos* 2.12; *Esainis* 2.22; *Esaini* 2.29 | *Ēsāīnōs, Ēsāīnīs, Ēsāīnī* | founder settled *Ēsā-*; -īnus |
| Lot | לוֹט | *Lōtī* 2.9, 2.19 | kept | settled |
| Joshua son of Nun | | *Jōsua, Jōsuæ, Jōsuam; Nūnis* | kept | settled |
| Caleb son of Jephunneh | | *Calebō, Jephonis* 1.36 | kept | settled (unmarked, Numbers' call 4) |
| Dathan, Abiram, Eliab | | *Dāthānem, Abīrāmum, Elīābī* 11.6 | kept | settled |
| Balaam | בִּלְעָם | *Balaamum* 23.4, *Balaamō* 23.5 | kept | settled (unmarked) |
| Beor, Balaam's father | בְּעוֹר · Βεώρ | *Phegōris* 23.4 | *Beōris* (spelling change) | settled Num 22:5, 31:8 (hard call 6) |
| Og | עוֹג · Ὤγ | *Ogum* 1.4, 3.3, 29.7; *Ogo* 31.4; *Ōgī* 3.4…; *Ōgus* 3.1 | *Ōgum, Ōgō* | settled *Ōgus, Ōgī* |
| Sihon | סִיחוֹן · Σηών | *Sēhōn, -ōnem, -ōne, -ōnī, -ōnis* | kept | settled |
| Jair son of Manasseh | יָאִיר | *Jāīr, Jāīrī* 3.14 | kept | settled |
| Machir | מָכִיר | *Māchīrī* 3.15 | kept | settled |
| Pharaoh | פַּרְעֹה | *Pharaōnem(que), Pharaōnis* | kept | settled |
| Pharaoh's (adjective) | | *Pharaoniosque* 29.2, 34.11 | *Pharaōniōsque* | settled Exod 7:9 *Pharaōniōs* |
| Miriam | מִרְיָם | *Marīam* 24.9 | kept | settled |
| Joseph | יוֹסֵף | *Jōsēphō, Jōsēphī* 33.13, 16 | kept | settled |
| Josephites | | *Josephei* 27.12 | *Jōsēphēī* | founder settled *Jōsēphus*; -ēus as *Jācōbēus* |
| Reuben; Reubenites | רְאוּבֵן | *Rūbēn* 33.6; *Rūbēnītæ, -īs*; *Rubenitarum* 4.43 | *Rūbēnītārum* | settled *Rūbēnīt-* |
| Simeonites | שִׁמְעוֹן | *Simeonii* 27.12 | *Simeōniī* | founder settled *Simeōn*; -ius |
| Levi; Levites | לֵוִי | *Lēvī, Lēvim, Lēvis; Lēvīt-; lēvīticam* | kept | settled |
| Judah; Judaeans; Judaea | יְהוּדָה | *Jūdā, Jūdæ, Jūdæī* 27.12, *Jūdæamque* 34.2 | kept | settled |
| Issachar; Issacharites | יִשָּׂשכָר | *Issāchar* 33.18; *Issachariani* 27.12 | *Issāchariānī* | founder settled *Issāchar*; -iānus |
| Zebulun; Zebulunites | זְבוּלֻן | *Zabulōn(e)* 33.18; *Zabulonii* 27.13 | *Zabulōniī* | settled Matt 4:13 *Zabulōniīs* |
| Dan; Danites | דָּן | *Dan* 33.22, *Danem* 34.1; *Dāne* 33.22; *Danii* 27.13 | *Dane, Daniī* | settled *Dan, Danem* (stem unmarked) |
| Naphtali; Naphtalites | נַפְתָּלִי · Νεφθαλί | *Nephthālis* 33.23; *Nephthali* 33.23; *Nephthalenses* 27.13; *nephthalensem* 34.2 | *Nephthālī, Nephthālēnsēs, Nephthālēnsem* | settled *Nephthālis*; Gaffiot *Nephthalī*; settled Matt 4:13 *Nephthālēnsibus* |
| Gad; Gadites | גָּד | *Gadō, Gadum* 33.20; *Gadīn-*; *Gadinisque* 3.12 | *Gadīnīsque* | settled *Gadīnīs*; -īnus |
| Asher; Asherites | אָשֵׁר | *Āsēr* 33.24; *Asere* 33.24; *Aseriani* 27.13 | *Āsēre, Āsēriānī* | settled *Āsēr*, *Āsēriān-* |
| Benjamin; Benjamites | בִּנְיָמִן | *Benjāmīne* 33.12; *Benjamītæ* 27.12 | kept | settled (Numbers' call 2) |
| Ephraim; Ephraimite | אֶפְרַיִם | *Ephrāimī* 33.17; *ephraiminam* 34.2 | *Ephrāimīnam* | settled *Ephrāimīnā*; -īnus |
| Manasseh; Manassite | מְנַשֶּׁה | *Manassis* 33.17; *Manassēns-*; *manassensem* 34.2 | *Manassēnsem* | settled *Manassēnsis* |
| Jova's (adjective) | | *Jovana* 15.2 (ablative) | *Jōvānā* | settled *Jōvānī, Jōvānum, Jōvānæ* |
| Paran | פָּארָן · Φαράν | *Pharanem* 1.1; *Pharane* 33.2 | kept | settled (Gaffiot *Phăran*, Numbers' call 2) |
| Tophel | תֹּפֶל · Τοφόλ | *Thophel* 1.1 | *Thōphel* | Hebrew holem |
| Laban (place) | לָבָן | *Lābānem* 1.1 | kept | settled *Lābān* (the same Hebrew) |
| Hazeroth | חֲצֵרֹת | *Haserothaque* 1.1 | *Hasērōthaque* | settled Num 11:35 *Hasērōtha* (accusative) |
| Di-zahab | דִּי זָהָב | *Dizahabum* 1.1 | *Dīzāhābum* | Hebrew hireq-yod, qamets, qamets |
| Horeb | חֹרֵב | *Hōrēbō* ×9 | kept | settled |
| Seir | שֵׂעִיר · Σηείρ | *Seirem* 1.2, 2.1, 2.5; *Seire* 1.44, 2.12, 33.2; *Seirīs* 2.4, 2.8, 2.22, 2.29 | *Seiris* (genitive) | settled *Seir, Seire*; -is short (hard call 9) |
| Kadesh-barnea | קָדֵשׁ בַּרְנֵעַ | *Cadesbarneam* 1.2, 1.19; *Cadesbarnea* 2.14, 9.23 | *Cadēsbarnēam, Cadēsbarnēā* | settled *Cadēs*; Hebrew tsere (hard call 1) |
| Kadesh | קָדֵשׁ | *Cadem* 1.46; *Cade* 32.51 | kept | settled |
| Zin | צִן | *Sinis* 32.51 | kept | settled (*Sin-* for Zin) |
| Heshbon | חֶשְׁבּוֹן · Ἐσεβών | *Hesebōnem* 1.4, 4.46; *Hesebonis* 3.2, 29.7 | *Hesebōnis* | settled *Hesebōn* |
| Heshbonite (adjective) | | *Hesebonium* 2.24, 2.26, 3.6; *Hesebonius* 2.30 | *Hesebōnium, Hesebōnius* | founder settled; -ius |
| Ashtaroth | עַשְׁתָּרֹת · Ἀσταρώθ | *Astarothis* 1.4 | *Astarōthīs* | settled Gen 14:5 *Astarōtha*; ablative plural |
| Edrei | אֶדְרֶעִי | *Edreī* 1.4, 3.1; *Edreim* 3.10 | *Edreīm* | settled Num 21:33 *Edreī*; accusative -īm |
| Bashan | בָּשָׁן | *Bāsānæ, Bāsānam*; *Basana* 3.4, 3.10 ×2, 3.13, 4.43, 33.22 | *Bāsāna* (3.10 nom.), *Bāsānā* (abl.) | settled *Bāsān-* |
| of Bashan | | *Basanense* 3.13 | *Bāsānēnse* | settled stem; -ēnsis |
| Bashan-havoth-jair | חַוֺּת יָאִיר · Θαυώθ | *Basanhavotha* 3.14 | *Bāsānhavōtha* | settled *Bāsān*; Hebrew holem, Greek ω |
| Argob | אַרְגֹּב · Ἀργόβ | *Argobiae* 3.4, 3.14; *Argobiam* 3.13 | *Argōbiæ, Argōbiam* | Hebrew holem |
| Hermon | חֶרְמוֹן · Ἀερμών | *Hermonem* 3.8; *Hermon* 4.49 | *Hermōnem, Hermōn* | Greek ω |
| Sirion | שִׂרְיֹן · Σανιώρ | *Sarionem* 3.9 | *Sariōnem* | Greek ω, Hebrew holem |
| Senir | שְׂנִיר · Σανίρ | *Sanir* 3.9 | *Sanīr* | Hebrew hireq-yod |
| Mount Sion (Hermon) | שִׂיאֹן · Σηών | *Seonem* 4.48 | *Sēōnem* | Greek η, ω (not Sihon) |
| Salecah | סַלְכָה · Ἑλχᾶ | *Salcham* 3.10 | kept | Hebrew patah; -am the Latin ending |
| Rabbah | רַבַּת | *Rabbathæ* 3.11 | kept | Hebrew patah, patah |
| Geshur | גְּשׁוּרִי | *Gessuris* 3.14 | *Gessūris* | Hebrew shureq |
| Maacath | מַעֲכָתִי | *Maachatis* 3.14 | *Maachātis* | Hebrew qamets |
| Chinnereth | כִּנֶּרֶת | *Cenneretho* 3.17 | *Cenerethō* (spelling change) | settled Num 34:11 *Cenerethī* |
| Pisgah | פִּסְגָּה · Φασγά | *Phasga* 3.17, 4.49; *Phasgæ* 3.27; *Phasge* 34.1 | *Phasga* (nom.), *Phasgæ* (spelling change) | settled *Phasgæ* |
| Peor; Baal-peor; Beth-peor | פְּעוֹר · Φογώρ | *Phegōris* 3.29, 4.46; *Baalphegorem* 4.3; *Bethphegor* 34.6 | *Baalphegōrem, Bēthphegōr* | settled *Baalphegōre*, *Phegōr-*; *Bēth-* as *Bēthnemram* |
| Arnon | אַרְנֹן | *Arnōn-* | kept | settled |
| Aroer | עֲרֹעֵר · Ἀροήρ | *Arœre* 2.36, 3.12, 4.48 | *Arōēre* | settled Num 32:34 *Arōēr* (hiatus, not œ) |
| Ar | עָר | *Ār* 2.9, 2.18; *Aris* 2.29 | *Āris* | settled *Ār* |
| Gilead; the Gilead region | גִּלְעָד | *Galaādum, Galaādō, Galaadī*; *Galaaditis* 3.10, 3.13; *Galaadītidem* 34.1 | *Galaadītis* | settled (see disagreements) |
| Jabbok | יַבֹּק | *Jabboqui* 2.37; *Jabboquum* 3.16 | *Jabbōcī, Jabbōcum* (spelling changes) | settled Num 21:24 *Jabbōcum* |
| Zered | זֶרֶד | *Zaredum* 2.13, 2.14 | kept | settled |
| Jahaz | יַהְצָה | *Jasa* 2.32 | *Jāsā* | settled Num 21:23 *Jāsam* (ablative here) |
| Kedemoth | קְדֵמוֹת · Κεδαμώθ | *Cedemothis* 2.26 | *Cedēmōthis* | Greek ω, Hebrew tsere (genitive) |
| Elath | אֵילַת | *Elatho* 2.8 | *Ēlathō* | Hebrew tsere-yod |
| Ezion-geber | | *Asiōngābre* 2.8 | kept | settled |
| Hazerim | חֲצֵרִים · Ἀσηδώθ | *Hazeris* 2.23 | *Hazērīs* | Greek η, Hebrew tsere; ablative plural |
| Gaza | עַזָּה | *Gāzam* 2.23 | kept | settled |
| Caphtor | כַּפְתּוֹר | *Cappadociā* 2.23 | kept | settled (Castellio's Cappadocia) |
| Bezer | בֶּצֶר | *Beser* 4.43 | kept | Hebrew segol, segol |
| Ramoth (Gilead) | רָאמֹת · Ῥαμώθ | *Ramotha* 4.43 | *Rāmōtha* | Greek ω, Hebrew qamets, holem |
| Golan | גּוֹלָן · Γαυλών | *Gaulanitidem* 4.43 | *Gaulānītidem* | -ītis as *Galaadītidem*; Hebrew qamets |
| Beeroth (Bene-jaakan) | בְּאֵרֹת · Βηρώθ | *Berothis* 10.6 | *Bērōthīs* | Greek η, ω |
| Jaakanites | יַעֲקָן | *Jaquanensium* 10.6 | *Jaacānēnsium* (spelling change) | settled Num 33:31 *Benējaacāne* (hard call 4) |
| Moserah | מוֹסֵרָה | *Moseram* 10.6 | *Mōsēram* | Hebrew holem, tsere |
| Gudgodah | הַגֻּדְגֹּדָה · Γαδγάδ | *Gadgadam* 10.7 | *Gadgādam* | Hebrew holem; as settled *Hōrgadgādō* |
| Jotbathah | יָטְבָתָה | *Jothabatham* 10.7 | *Jothabātham* | settled Num 33:33 *Jothabāthā* |
| Taberah | תַּבְעֵרָה | *Taberam* 9.22 | *Tabēram* | settled Num 11:3 *Tabēra* |
| Massah | מַסָּה | *Massam* 6.16, 9.22, 33.8 | kept | settled Exod 17:7 *Massam* |
| Kibroth-hattaavah | | *Busta* 9.22 | kept | Latin (as Numbers) |
| Gerizim | גְּרִזִים · Γαριζίν | *Garizimo* 11.29, 27.12 | *Garizīmō* | Gaffiot *Garizim* unmarked; Hebrew hireq-yod |
| Ebal | עֵיבָל · Γαιβάλ | *Ebale* 11.29, 27.4, 27.13 | *Ēbāle* | settled Gen 36:23 *Ēbālem* (same Hebrew) |
| Gilgal | הַגִּלְגָּל | *Galgala* 11.30 | kept | Wiktionary *Galgala* bare |
| Moreh | מֹרֶה | *Mōre* 11.30 | kept | Hebrew holem (as proposed) |
| Jordan; cis-/transjordanine | יַרְדֵּן | *Jordān-*; *cisiordaninam* 3.8, *cisjordanini* 4.48, *cisiordaninum* 4.49, *transiordaninam* 3.25 | *cisjordānīnam, -īnī, -īnum; trānsjordānīnam* (j spelling changes) | settled *Jordān-*, Matt 4:25 *Trānsjordānīnā*; Gaffiot cĭs |
| Lebanon | לְבָנוֹן | *Libanum* 1.7, 3.25; *Libanō* 11.24 | kept | Gaffiot *Lĭbănus* |
| Euphrates | | *Euphrātem, Euphrāte* | kept | settled |
| Canaan | | *Chananæam* | kept | settled |
| Jericho | | *Hierichūntis* | kept | settled |
| Nebo | נְבוֹ | *Nabōnem* | kept | settled |
| Abarim | | *Abārium* 32.49 | kept | settled |
| Hor | | *Hōre* 32.50 | kept | settled |
| Sinai | | *Sīnā* 33.2 | kept | settled |
| Zoar | | *Sigōrim* 34.3 | kept | settled |
| Egypt; Egyptians | | *Ægypt-, ægypti-* | kept | settled |
| Mesopotamia; Pethor | | *Mesopotamiæ*; *Pethore* 23.4 | *Pethōre* | settled Num 22:5 *Pethōram* |
| Sodom, Gomorrah, Admah | | *Sodomæ, Gomorræ, Admæ* 29.23 | kept | settled |
| Zeboiim | צְבֹיִם | *Sebojum* 29.23 | *Seboimōrum* (spelling change) | settled Gen 14:2 (hard call 5) |
| of Sodom, of Gomorrah | | *sodomitanis, gomorranis* 32.32 | *Sodomitānīs, Gomorrānīs* | settled Gen 19:4, Matt 10:15 (hard call 10) |
| Israelites; Israelite women; Israelitish | | *Isrāēl-, Isrāēlīt-, isrāēlītic-*; *Isrælitidum* 23.17 | *Isrāēlītidum* | Gaffiot *Isrāēlītis, -ĭdis* |
| Hebrews | עִבְרִי | *Ebraeus, Ebraea* 15.12 | *Hebræus, Hebræa* (spelling changes) | settled Exod 21:2 (hard call 3) |
| Amorites | הָאֱמֹרִי | *Amorræ-*; *amorræo* 3.2 | *Amorræō* | settled *Amorræ-* (ablative) |
| Canaanites, Hittites, Hivites, Jebusites, Girgashites | | *Chananæōs, Hettæōs, Hevæōs, Jebūsæōs, Gergesæōs* 7.1, 20.17 | kept | settled |
| Perizzites | הַפְּרִזִּי | *Pheresæos* 7.1; *Pherezæōs* 20.17 | *Pherezæōs* (spelling change) | settled |
| Moabites; Moabite | | *Mōabīt-*; *Mōabitās* 2.9; *moabiticis* 34.1, *moabitica* 34.6, *mōabīticō* 34.8 | *Mōabītās, Mōabīticīs, Mōabīticā* | settled *Mōabīt-, Mōabītic-* |
| Ammonites | עַמּוֹנִי | *Ammonīt-*; *Ammonitīs* 2.20; *Ammonita* 23.3 | *Ammonītīs, Ammonīta* | settled *Ammonīt-* |
| Amalekites | | *Amālēchīta, -ārum* 25.17, 19 | kept | settled |
| Edomite | אֲדֹמִי | *Idumæo* 23.7 | *Idūmæō* | settled *Idūmæus* |
| Emim | הָאֵמִים · Ὀμμίν | *Emēs* 2.10, 2.11 | *Emēnsēs* (spelling changes) | settled Gen 14:5 (hard call 2) |
| Anakim (adjective) | עֲנָקִים | *Enāquīnōs* 1.28, 2.11; *Enaquinis* 2.10, 2.21, 9.2; *Enaquinorum* 9.2 | *Enāquīnīs, Enāquīnōrum* | settled *Enāquīnōs* |
| Horites | הַחֹרִי | *Horios* 2.12, 2.22 | *Hōriōs* | settled Gen 36:20–22 *Hōri-* |
| Zamzummim | זַמְזֻמִּים · Ζοχομμίν | *Zamzumes* 2.20 | *Zamzumēs* | Hebrew patah, qibbuts; nom. pl. -ēs |
| Avvim | עַוִּים | *Aviōs* 2.23 | kept | Hebrew patah; -ius |
| Caphtorim | כַּפְתֹּרִים | *Cappadocēs* 2.23 | kept | Gaffiot *Cappădox, -ŏcis* |
| Sidonians | צִידֹנִים | *Sīdoniī* 3.9 | *Sīdōniī* | settled *Sīdōnius* (Gaffiot *Sīdōnĭus*) |
| Arameans | אֲרַמִּי | *Syrīs* 26.5 | kept | Gaffiot *Sўrī* |
