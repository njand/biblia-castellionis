# 1 Samuel: one form per person, place and people (Claude, 2026-11-20)

Every capitalized word of `text/draft/1SA.preview.usfm` (and its draft `1SA.usfm`), and every lower-case adjective of
a people or place (*isrāēlīticus, palæstīnus, bethsamiticus, odollamus, engadinus, suphius, nobanus, bethelensis,
elianus, azotius*), was grouped by its unmarked key, read in its verse for its case, matched to the Hebrew (WLC) and
the Greek (Brenton, `sources/parallel/lxx/1Sam.tsv`), and decided as Ruth and Judges were (`ruth1-4-names.md`,
`judg1-21-names.md`): the settled form first (decision 46, `data/gold/`: Genesis–Ruth and the NT), then Gaffiot
(`pipeline latin macron`; of 1 Samuel's names it marks only *Săūl, Sămŭēl, Jŏnăthās, Dāvīd, Carmēlus, Pălæstīnus,
Azōtus, Dagōn, Găbăōn, Joēl, Hebrōn, Sŏphēnē, Phăran, Mōăb, Ĭdūmæa, Ăpollō* and gives *Abner, Nabal, Geth, Thabor,
Rachel, Astaroth, Baal* unmarked), then the Greek's η/ω, then another dictionary (Wiktionary *Saūl, Samūēl, Iābēs,
Gelbōe, Galgala*; *Goliath* bare), then the Hebrew vowel (qamets, tsere, holem, shureq, hireq-yod long; decision 52).
Gentile adjectives: the founder's marks and the suffix's quantity (-īnus, -ānus, -iānus, -ius short i, -ēnsis, -īta,
-æus). Case endings read in each verse.

**Counted**: 80 rows below, about 190 persons, places and peoples (a place and its people, or a founder and his
adjective, share a row); 16 rows kept wholly as the preview has them, the rest changed in some form.
**Outputs** (scratch folder `…/scratchpad/1sam2/`; built by `names/build.py`): `names.spelling.tsv` (16 spelling
changes, each `old` checked by script to occur exactly once in its verse of `text/draft/1SA.usfm`, as a word and as a
string) and `names.forms.tsv` (568 forms rows, only where the decided form differs from the preview; five `#` rows,
all *Jōvā*: 2:20 #2, 6:19 #2, 13:13 #1, 17:37 #2, 20:13 #2, where one verse has *Jōva* nominative and *Jōvā*
ablative). **Check**: `check.py names/empty.layout.tsv names.forms.tsv`: 568 rows, 14 errors, every one a row for a
respelled word that takes effect once its spelling row is applied (1:1 *Ephrātæus*; 6:9, 6:12 *Bēthsemem*; 6:12
*Bēthsemis*; 6:13, 6:14, 6:15, 6:18 *Bēthsemītæ*; 6:19 *Bēthsemītārum, bēthsemīticum*; 22:1 *adullāmam*; 23:29
*Ēngaddīnōrum*; 24:1 *ēngaddīnō*; 31:12 *Bēthsānis*). The two *Abjathari → Abiathari* rows (23:9, 30:7) pass already
(the key folds j).

The printed text (`text/orig/1SA.usfm`) keeps 1738's spellings whatever is decided here: *Bethsam-, Ephrathæus,
Engadinorum, engadino, odollamam, Bethsanæ, Abjathari, Saulis*.

## Hard calls (for Nathan)

1. **King Saul: *Saūlus, Saūlī, Saūlō, Saūlum, Saūle*** and his men ***Saūlīnī, -īs, -ōrum*** (about 250 rows, the
   largest change): the preview left the king's name unmarked (*Saulus*), as Paul's *Saulus* (Acts 7–13, Greek
   Σαῦλος, a diphthong). The king is the settled Acts 13:21 ***Saūlem*** (Σαούλ, שָׁאוּל: two syllables), and Gaffiot
   *Săūl, ūlis* and Wiktionary *Saūl* agree. Castellio Latinizes him as *Saulus* (second declension), so the ū stands
   in every case. The settled *Saulō, Saulum, Saulīna* of Gen 36:38, 46:10, Num 26:13 are other men (Shaul), and are not
   changed. If the king's name should be left unmarked like Paul's, drop every *Saūl-* row.
2. **13:17 *in fines Saulis*** is the land of Shual (שׁוּעָל; KJV *Shual*, Vulgate *Sual*; Greek Σωγάλ), not the king.
   1738 and Wikisource both print *Saulis*: Castellio's form, perhaps his own confusion with the king's name. I kept
   the spelling and **unmarked it** (*Saulis*, against the preview's *Saūlis*): no vowel of *Sa-ul* can be matched to
   *Shu-al*. The Deuteronomy precedent (*Phegoris → Beōris*, Deut call 6) would allow correcting it: one spelling row
   *Saulis → Sualis*, marked ***Sūālis*** (shureq, qamets), with 1738's *Saulis* kept in the printed text. Say if you want it.
3. **Beth-shemesh: *Bēthsemem, Bēthsemis, Bēthsemītæ, Bēthsemītārum, bēthsemīticum*** (6:9–19; 1738 *Bethsam-*,
   Gaffiot *Bethsamēs*, as the Vulgate): the same town (בֵּית שֶׁמֶשׁ) as the settled Josh 15:10, 21:16 *Bēthsemem*,
   19:38 *Bēthsemes* (and Judg 1:33 *Bēthsemēnsēs*). Nine spelling rows (a → e), as Judges' *Calebus* (one form, the
   settled one). Drop them to keep Castellio's *Bethsam-* (then *Bēthsamem, Bēthsamis, Bēthsamītæ*).
4. **Adullam: *adullāmam*** (22:1, *in adullamam speluncam*; 1738 *odollamam*, the Greek Ὀδολλάμ): the settled Josh
   15:35 *Adullām*, 12:15 *Adullāmī* (עֲדֻלָּם, the same town). One spelling row. Drop it to keep *odollamam* (then
   unmarked: no settled or Hebrew vowel matches the o).
5. **Engedi: *Ēngaddīnōrum*** (23:29), ***ēngaddīnō*** (24:1; 1738 *Engadinorum, engadino*): settled Josh 15:62
   *Ēngaddī*. Two spelling rows (d → dd). Drop them to keep the single d (*Ēngadīnōrum, ēngadīnō*).
6. **The Ephraimite Elkanah: *Ephrātæus*** (1:1; 1738 *Ephrathæus*): אֶפְרָתִי, the word the settled Judg 12:5 and this
   book's own 17:12 print *Ephrātæī*. One spelling row (th → t), as Ruth's *Ephrattæi → Ephrātæī*.
7. **Beth-shan: *Bēthsānis*** at 31:12 (1738 *Bethsanæ*, a first-declension genitive) to agree with 31:10 *Bethsanis*
   and the settled third-declension *Bēthsāne, Bēthsānem* (Josh 17:11, 16, Judg 1:27). One spelling row; drop it to keep
   *Bēthsānæ*.
8. **Abiathar: *Abiāthārī*** (23:9, 30:7; 1738 *Abjathari*, beside its own *Abiathar, Abiathare* at 22:20, 23:6, 30:7):
   the settled Mark 2:26 *Abiāthāre* (the same man) has the vowel i. Two spelling rows (j → i), harmless to the check.
9. **Achish: *Achis, Achim, Achī*** (8, 5 and 3 times): one name in three cases, not three spellings. Castellio
   declines אָכִישׁ as Ruth's *Noemis*: nominative *-is* and accusative *-im* unmarked, dative and ablative *-ī* long
   (21:12 *ab Achī*, 29:2 *cum Achī*, 29:4 *Achī ita dīcunt*). The Hebrew hireq-yod would make the stem vowel long
   throughout (*Achīs, Achīm*); I followed Ruth's call 1 instead. Hophni is declined the same way (*Hophnis*; 2:34,
   4:11 *Hophnī*), and so is Eli (hard call 10).
10. **Eli: *Ēlis, Ēlim, Ēlī*** (24 times): the preview had *Ēlis* but left *Elim, Eli, Elique* unmarked. Ē by the tsere
    of עֵלִי and the Greek Ἡλί (η), as the settled Luke 3:23 *Ēlis* (Heli, the same Greek name); declined as hard call 9.
    1:9 and 3:2 (ablative absolute) and 2:12, 3:12, 3:15 (dative) are *Ēlī*; 4:14 *Ēlīque*. His house's adjective 3:14
    ***ēliānæ*** (*culpam ēliānæ posteritātis*, -ānus): not the settled *Ēliānō* (Luke 1:17), which is Elijah's.
    Elihu (1:1 *Ēlīī*, אֱלִיהוּא, Greek Ἠλιού) is another name: η and hireq-yod.
11. **Samuel: *Samuēl-*** throughout: the preview had *Samūēl-* in 9 places (1:20, 3:21, 7:13, 8:19, 9:14, 12:18,
    16:8, 16:10, 28:20) beside *Samuēl* elsewhere. The settled *Samuēl, Samuēle, Samuēlem* (Num 34:20,
    Acts 3:24, 13:20, Heb 11:32) and Gaffiot *Sămŭēl* have the u short; Wiktionary's *Samūēl* is not followed.
12. **Jabesh: *Jābem, Jābe, Jābemque, Jābēnsēs, Jābēnsium*** (11:1, 31:12–13; 1738 *Iabem, Iabe*, beside the settled
    Judg 21:9 *Jābis*): one third-declension name (*Jābis/Jābes, -is*) in its cases, not respelled; marked as the
    settled *Jābis, Jābēnsēs* and Wiktionary *Iābēs*.
13. **Hebrew-only marks** (no settled, Gaffiot or Greek evidence): *Nābāl* (Gaffiot's *Nabal* unmarked; its entry may be
    the Mauretanian river, Wiktionary's is), *Nāhās/Nāhā*, *Mīchol*, *Mēroba*, *Rāmātha*, *Abīnādāb-*, *Achīmelech-*,
    *Achīnōama*, *Abīgail*, *Malchīsūam*, *Jerōhāmī*, *Machmās/-ānte/-āntis* (the ā kept before -nt-, as the settled
    *Sīlūnte*), *Ōselem* (20:19, qamets written o), *Telāīm*, and the 30:27–30 towns (*Rāmōthānīs, Sephamōthānīs,
    Estamōānīs, Rāchālēnsibus, Hormānīsque, Bōrasānēnsibus, Athācānīs*). They follow Ruth's *Elīmelechus* and Judges'
    call 12; if Hebrew-only marks on these should be dropped, these are the rows.
14. **Kept unmarked against the Hebrew**: *Goliathus, Goliathī* (Wiktionary *Goliath* bare; גָּלְיָת would give
    *Goliāth-*), *Anna* (settled Luke 2:36), *Phenenna* (Greek Φεννάνα, no long vowel), *Samma, Sammam* (settled Gen
    36:13, 17), *Gabatham* (11:4, Gibeah of Saul; settled *Gabaatha* unmarked), *Selsam* (10:2), *Sene* (14:4, segol),
    *Jessuim* (14:49, Ishvi; the accusative's *-im* short as hard call 9), *Sarethi* (9:1: a name the Hebrew lacks;
    perhaps from the Greek Ἰαρέδ), *saaræam* (17:52, Shaaraim; no long vowel), *Ophram* (settled *Ophra*), *Agagum, -us*
    (settled *Agagum*).
15. **"In colle Hachīlā"** (23:19, 26:1, 26:3): read as an ablative in apposition to *colle* (hireq-yod ī); if
    Castellio meant an indeclinable genitive (*in colle Hachīla*), the three rows become *Hachīla*.

## Noticed, not names

- **Capitals of lower-case adjectives, for the layout merge**: 1738 prints *isrāēlītic-* (2:28, 2:29, 9:16, 10:20,
  15:17, 15:26, 17:45, 18:6), *palæstīn-* (6:12, 6:18, 17:46, 27:7, 27:11, 29:3, 29:4, 29:7, 29:9), *benjāmīnēnsī*
  (10:20), *ægyptius* (30:11), *azotii* (5:5), *bethsamiticum* (6:19), *elianæ* (3:14), *bethelensem* (13:2), *suphios*
  (9:5), *odollamam* (22:1), *nobanos* (22:11), *engadino* (24:1), *saaræam* (17:52) lower case; the settled text
  capitalizes *Isrāēlītic-*, *Palæstīn-*, *Benjāmīnēnsī*. The marks here are right either way; no forms row changes case.
- **17:1 *in finibus Daniorum*** for Ephes-dammim (אֶפֶס דַּמִּים): Castellio's reading (1738 and the draft), as if
  "the Danites"; *Daniōrum* kept as the settled form (Josh 19:48). For the reader of chapter 17 or the notes.
- **9:1** names a *Sarethi* between *Bechorati* and *Aphiæ* that the Hebrew (בֶּן־בְּכוֹרַת בֶּן־אֲפִיחַ) does not
  have; the Greek has Ἰαρέδ in that genealogy. Left as printed; for the notes.
- *Apollinem* (28:8) and *Phœbō* (28:7, 28:7) for the spirit of divination: Castellio's classical words, kept (Gaffiot
  *Ăpollō, -ĭnis*, *Phœbus*). *Rūpēs* (23:28) is the Latin word. *Cherūbīs* (4:4) is the common noun (settled).
- **Jova's ablatives**: 34 *Jōva* after *ā, ab, cōram*, in ablatives absolute (*favente, dante, auctōre, adjuvante,
  relictō Jōvā*), *secundō Jōvā* (16:18, 17:37) and *in Jōvā Deō suō* (30:6) are *Jōvā*; *cum Jōva Deus vester … esset*
  (12:12), *hodiē ā tē Jōva … abrumpit* (15:28), *āvertat hoc ā mē Jōva* (24:6) and 24:19 are nominatives and kept.
  The adjective is the settled *Jōvān-*: 11:7 *Jōvānō pavōre*, 18:17 *Jōvānaque bella*, 20:14 *Jōvānā pietāte*, 22:21
  *Jōvānīs sacerdōtibus*, 25:28 *bella Jōvāna*.

## Settled forms that disagree (not changed: settled text is never rewritten)

- *Jezræl* (Josh 15:56, 19:18; *Jezrælis* Josh 17:16) against *Jezraelis* (Judg 6:33, Judges' hiatus call). 1 Samuel's
  Jezreel (Ahinoam's town in Judah, Josh 15:56's) follows Joshua: *Jezræl, Jezrælānam, Jezrælānā, Jezrælēnsis*.
- *Saulus* (Acts, Paul) and *Saūlem* (Acts 13:21, the king) are rightly different (hard call 1).
- *Ābīās* (Matt 1:7, king Abijah) is followed for Samuel's son (8:2, the same Hebrew אֲבִיָּה), though the yod is
  doubled (short i); *Achiās* (Ahijah, 14:3, 14:18) has no settled form and follows the Hebrew.

## Decisions

| Person / place / people | Hebrew · Greek | In 1 Samuel (preview) | Decided | Reason |
|---|---|---|---|---|
| Jova | יְהוָה | *Jōva* ×124, *Jōvæ, Jōvam*; *Jovana, Jovanaque, Jovanis, Jovano*, *Jōvānī* | *Jōvā* ×34 (ablatives); *Jōvān-* | settled *ā Jōvā*, *Jōvān-* (noticed) |
| Saul (the king); his men | שָׁאוּל · Σαούλ | *Saulus, -ī, -ō, -um*, *Saule* 19.4, *Saūlis* 13.17; *Saulini, -is, -orum* | *Saūl-* ×250; *Saūlīnī, -īs, -ōrum* | settled Acts 13:21, Gaffiot *Săūl* (hard call 1) |
| Shual | שׁוּעָל · Σωγάλ | *Saūlis* 13.17 | *Saulis* | not the king (hard call 2) |
| Samuel | שְׁמוּאֵל · Σαμουήλ | *Samuēl-*; *Samūēlemque, Samūēlī, Samūēlis* | *Samuēl-* throughout | settled, Gaffiot (hard call 11) |
| David | | *Dāvīd-* | kept | settled |
| Jesse; son of Jesse | יִשַׁי · Ἰεσσαί | *Īsæus, -ī, -ō, -um*; *Isæida* 22.13, *Isæidæ* 20.30, *Isæides* 20.31 | *Īsæidā, Īsæidæ, Īsæidēs* | settled *Īsæ-*; as *Dāvīdidēs* |
| Kish | קִישׁ · Κίς | *Cis* ×6 | *Cīs* | settled Acts 13:21 |
| Jonathan; his men | יוֹנָתָן | *Jonathān, -āne*; *Jonathanem, -i, -is*; *Jonathanensiumque* 14.21 | *Jonathān-* throughout | settled Judg 18:30 |
| Eli; of Eli | עֵלִי · Ἡλί | *Ēlis*; *Eli, Elim, Elimque, Elique*; *elianæ* 3.14 | *Ēlis, Ēlim(que), Ēlī(que), ēliānæ* | settled Luke 3:23 (hard call 10) |
| Elkanah; Jeroham; Elihu; Tohu; Zuph | אֶלְקָנָה; יְרֹחָם; אֱלִיהוּא; תֹּחוּ; צוּף | *Elcāna, Elcanæ*; *Jerohami, Ēliī, Thohi, Suphi* 1.1; *suphios* 9.5 | *Elcānæ, Elcānā* 1.21; *Jerōhāmī, Ēlīī, Thōhī, Sūphī, sūphiōs* | settled Exod 6:24; Greek η; Hebrew |
| Ramathaim-zophim; Ramah | הָרָמָתַיִם צוֹפִים; הָרָמָה | *Ramatha* 1.1, *Ramatham* ×10, *Sophōrum*; *Rāmæ, Ramam* | *Rāmāthā* 1.1, *Rāmātham, Sōphōrum, Rāmam* | Hebrew qamets, holem; settled *Rāmam* |
| Ephrathite (Ephraimite); Ephraimites | אֶפְרָתִי | *Ephrathæus* 1.1; *Ephrātæī* 17.12; *Ephrāimītārum* | *Ephrātæus* (spelling) | settled Judg 12:5 (hard call 6) |
| Hannah; Peninnah | חַנָּה; פְּנִנָּה · Φεννάνα | *Anna, -æ, -am*; *Phenenna, -æ, -am* | kept | settled *Anna*; no long vowel |
| Shiloh | שִׁלֹה | *Sīlūnte, Sīlūntem* | kept | settled |
| Hophni; Phinehas | חָפְנִי; פִּינְחָס | *Hophnis*; *Hophni* 2.34, 4.11; *Phīnees, -ee, -eis* | *Hophnī* | as *Noemī* (hard call 9); settled *Phīnees* |
| Ichabod; Ahitub; Ahijah | אִי־כָבוֹד; אֲחִטוּב · Ἀχιτώβ; אֲחִיָּה | *Ichabodi, -um*; *Achitobi* ×5; *Achias, Achiæ* | *Ichabōdī, -um, Achitōbī, Achiās* | Hebrew holem; Greek ω |
| Dagon | דָּגוֹן | *Dagonem, Dagonis* | *Dagōnem, Dagōnis* | settled *Dagōnī*, Gaffiot |
| Ashdod; Ashdodites | אַשְׁדּוֹד | *Azōtō, Azōtum*; *Azotii, azotii, Azotios* | *Azōtiī, Azōtiōs* | settled *Azōtus*, Gaffiot |
| Gath; Gittite | גַּת · Γέθ | *Getha* 6.17, 17.4; *Gethæ, Getham*; *Gethanus* 17.23 | *Gethā* 6.17, 17.4; *Gethānus* | settled *Gethæ*; -ānus |
| Ekron; Ekronites | עֶקְרוֹן | *Accarōn-*; *Accarōnītæ* | kept | settled |
| Gaza; Ashkelon | | *Gaza* 6.17; *Ascalōne* | *Gazā* (ablative) | settled *Gaza* |
| Beth-shemesh; its people | בֵּית שֶׁמֶשׁ | *Bethsamem, Bethsamis, Bethsamitæ, -arum, bethsamiticum* | *Bēthsem-* (spelling) | settled Josh (hard call 3) |
| Joshua (of Beth-shemesh) | | *Jōsuæ* | kept | settled |
| Kiriath-jearim; Abinadab; Eleazar | קִרְיַת יְעָרִים; אֲבִינָדָב | *Cariathjarimenses, Cariathjārīmī*; *Abinadabi* 7.1; *Eleāzarum* | *Cariathjārīmēnsēs, Abīnādābī* | settled; Hebrew hireq-yod |
| Mizpah; Beth-car; Shen | הַמִּצְפָּה; בֵּית כָּר; הַשֵּׁן | *Maspha* 7.11, *Maspham*; *Bethcar, Sen* | *Masphā* 7.11, *Bēthcār, Sēn* | settled; Hebrew qamets, tsere |
| Amorites | | *Amorræōs* | kept | settled |
| Bethel; Gilgal | | *Bēthēl*; *Bethelensibus* 30.27, *bethelensem* 13.2; *Galgala, Galgalīs* | *Bēthēlēnsibus, bēthēlēnsem* | settled; -ēnsis |
| Joel; Abijah; Beersheba; Dan | יוֹאֵל; אֲבִיָּה | *Jœl* 8.2; *Ābīās*; *Bersabæ, -am*; *Dane* | *Jōēl* | settled Acts 2:16 *Jōēle* |
| Abiel, Zeror, Becorath, Aphiah; (Sarethi) | אֲבִיאֵל; צְרוֹר; בְּכוֹרַת; אֲפִיחַ | *Abielis* 9.1, 14.51; *Seroris, Bechorati, Sarethi, Aphiæ* 9.1 | *Abīēlis, Serōris, Bechōratī, Aphīæ*; *Sarethi* kept | Greek η; Hebrew (noticed) |
| Benjamites; Benjaminite; Jemini | יְמִינִי | *Benjamīt-*; *benjāmīnēnsī*; *Jeminiensis, -es, -iumque*; *Jeminim* 9.21 | *Jemīniēns-*, *Jemīnim* | settled *Jemīnis*, *Benjāmīnēnsī* |
| Shalisha, Shaalim | שָׁלִשָׁה; שַׁעֲלִים | *Salisa* 9.4; *Salimorum* 9.4 | *Sālisā, Salīmōrum* | Hebrew; ablative |
| Rachel; Zelzah; Tabor | רָחֵל; צֶלְצַח | *Rāchēlis*; *Selsam*; *Thaboris* 10.3 | *Thabōris* | settled *Thabōre*; *Selsam* kept |
| Gibeah; Geba; Gibeah of Saul | גִּבְעָה; גִּבְעַת שָׁאוּל | *Gabāæ, Gabāam*; *Gabatham* 11.4 | kept | settled *Gabāa*; *Gabatham* no long vowel |
| Nahash; Ammonites | נָחָשׁ · Νάας | *Nahas* 11.1; *Naha* 12.12; *Ammonīt-* | *Nāhās, Nāhā* | Hebrew (hard call 13) |
| Jabesh (Gilead); its people | יָבֵישׁ | *Jabem, Jabe, Jabemque*; *Jābēnsēs, -ibus*; *Jabensium* 11.5 | *Jābem, Jābe, Jābemque, Jābēnsium* | settled Judg 21 (hard call 12) |
| Gileadites | | *Galaadītæ, -ārum*; *Galaaditarumque* 13.7; *Galaaditis* 11.9 | *Galaadītārumque, Galaadītīs* | settled; dative plural |
| Bezek; Judaeans | | *Bezec*; *Jūdæ-* | kept | settled |
| Moses, Aaron, Jacob, Pharaoh, Egypt | | *Mōsem, Aharōnemque, Jācōbus, Pharaō(nem), Ægypt-* | kept | settled |
| Sisera, Hazor, Moabites, Jerubbaal, Bedan, Jephthah | בְּדָן | *Sīsaræ, Hāsōris, Mōabīt-, Jerobaalem, Jephtham*; *Bedanem* 12.11 | *Bedānem* | settled; Hebrew qamets |
| Baals, Ashtaroth | | *Baales*; *Astarōthum*; *Astarothumque* 12.10, *Astarothi* 31.10 | *Astarōthumque, Astarōthī* | settled |
| Michmash; Bethaven; Beth-horon | מִכְמָשׂ | *Machmas* ×5, *Machmante, -is*; *Bēthāven(is)*; *Bēthōrōnem* | *Machmās, Machmānte, Machmāntis* | Hebrew qamets (hard call 13) |
| Hebrews; Philistines | | *Hebræ-*; *Palæstīn-*, *palæstīn-* | kept | settled |
| Gad (land; prophet); Gadites; Gilead | | *Gadīnōrum, Gadō* | kept | settled |
| Ophrah; Zeboim valley | עָפְרָה; צְבֹעִים | *Ophram*; *Sebojorum* 13.18 | *Sebōjōrum* | settled *Ophra*; holem (not *Seboimōrum*) |
| Migron; Bozez; Seneh | מִגְרוֹן; בּוֹצֵץ; סֶנֶּה | *Magronem* 14.2; *Boses, Sene* 14.4 | *Magrōnem, Bōsēs*; *Sene* kept | Hebrew holem, tsere; segol |
| Aijalon | | *Ajālōnem* | kept | settled |
| Ishvi, Malchishua, Merab, Michal | יִשְׁוִי; מַלְכִּי־שׁוּעַ; מֵרַב; מִיכַל | *Jessuim*; *Malchisuam* 14.49, 31.2; *Meroba, -am*; *Michol, -e, -em* | *Malchīsūam, Mēroba, Mērobam, Mīchol, Mīchole, Mīcholem*; *Jessuim* kept | Hebrew (hard calls 13, 14) |
| Ahinoam; Ahimaaz | אֲחִינֹעַם; אֲחִימַעַץ | *Achinoama* 14.50, 27.3, 30.5; *Achinoamam* 25.43; *Achimaæ* 14.50 | *Achīnōama, Achīnōamā* 27.3, *Achīnōamam, Achīmaæ* | Hebrew (as Judges' *Abīnōamī*) |
| Abner; Ner | אַבְנֵר · Ἀβεννήρ; נֵר · Νήρ | *Abner, -e, -em, -is*; *Ner*; *Nerīs* ×3 | *Abnēr, -ēre, -ērem, -ēris; Nēr, Nēris* | Greek η; genitive -is short |
| Edom; Zobah | צוֹבָה | *Idūmæ-*; *Sophenæ* 14.47 | *Sophēnæ* | settled; Gaffiot *Sŏphēnē* |
| Amalekites; Agag | | *Amālēchīt-*; *Agago* 15.8, 15.9, *Agagum, -us* | *Agagō* | settled *Agagum*; ablative/dative |
| Telaim; Havilah; Shur | טְלָאִים | *Telaim* 15.4; *Hevila* 15.7; *Sur* | *Telāīm, Hevilā* | Hebrew; settled *Hevilam, Sur* |
| Kenites | | *Cenæī, Cenæōs*; *Cenæorum(que)* 27.10, 30.29 | *Cenæōrum(que)* | settled |
| Carmel; Carmelite | | *Carmēlō, -um*; *Carmelitæ* 27.3, 30.5 | *Carmēlītæ* | settled, Gaffiot *Carmēlus* |
| Bethlehem; Bethlehemites | | *Bēthlehēma* 17.12, *Bēthlehemam*, *Bethlehemamque* 16.4; *Bethlehemitæ, -am* | *Bēthlehemā* 17.12, *Bēthlehemamque, Bēthlehemītæ, -am* | settled |
| Eliab; Abinadab; Shammah | אֱלִיאָב; אֲבִינָדָב; שַׁמָּה | *Eliabum* 16.6, *Elīābus*; *Abinadabum, -us*; *Samma(m)* | *Elīābum, Abīnādābum, Abīnādābus* | settled *Elīāb-*; Hebrew; settled *Samma* |
| Socoh; Azekah; (Ephes-dammim) | שׂוֹכֹה | *Sochonem* 17.1 ×2; *Azēcam*; *Daniōrum* | *Sōchōnem* | settled *Sōchō* (noticed) |
| Goliath | גָּלְיָת · Γολιάθ | *Goliathus, -ī* | kept | Wiktionary bare (hard call 14) |
| Shaaraim; Jerusalem | שַׁעֲרַיִם | *saaræam* 17.52; *Hierosolymam* | kept | no long vowel; settled |
| Adriel the Meholathite | עַדְרִיאֵל הַמְּחֹלָתִי | *Adrieli, Molathitæ* 18.19 | *Adrīēlī, Mōlāthītæ* | Hebrew |
| Naioth; Secu; Ezel | נָיוֹת; שֶׂכוּ; הָאָזֶל | *Najothi, -o, -um*; *Sechu* 19.22; *Oselem* 20.19 | *Nājōthī, -ō, -um, Sechū, Ōselem* | Hebrew |
| Nob; Ahimelech; Doeg; Edomite | נֹב; אֲחִימֶלֶךְ; דּוֹאֵג · Δωήκ | *Nōbam, Nobamque*; *nobanos* 22.11; *Achimelech-*; *Dœgus*; *Idūmæus* | *Nōbamque, nōbānōs, Achīmelech-, Dōēgus* | Hebrew; Greek ω, η |
| Achish; Maoch | אָכִישׁ; מָעוֹךְ | *Achis, Achim, Achi*; *Maochi* 27.2 | *Achī* ×3, *Māōchī* | hard call 9; Hebrew |
| Adullam | עֲדֻלָּם | *odollamam* 22.1 | *adullāmam* (spelling) | settled Josh (hard call 4) |
| Mizpeh of Moab; Hareth; Gad the prophet | חָרֶת | *Maspham* 22.3; *Haretham* 22.5; *Gadō* | *Hāretham* | Hebrew qamets |
| Abiathar | אֶבְיָתָר | *Abiāthār, -āre*; *Abjathari* 23.9, 30.7 | *Abiāthārī* (spelling) | settled Mark 2:26 (hard call 8) |
| Keilah; its people | קְעִילָה | *Ceīla* 23.13 ×2; *Ceilam(que)*; *Ceilani, Ceilanosque* | *Ceīlā* 23.13, *Ceīlam(que), Ceīlānī, Ceīlānōsque* | settled Josh 15:44 |
| Ziph; Ziphites | זִיף | *Ziphi, Ziphim*; *Ziphæi* | *Zīphī, Zīphim, Zīphæī* | settled *Zīph* |
| Hachilah; Jeshimon | חֲכִילָה | *Hachila* ×3; *Jesimonis*, *Jesīmōnem* | *Hachīlā, Jesīmōnis* | Hebrew (hard call 15); settled |
| Maon; Engedi | | *Maone* ×4; *Engadinorum* 23.29, *engadino* 24.1 | *Māōne*; *Ēngaddīn-* (spelling) | settled *Māōn, Ēngaddī* (hard call 5) |
| Paran; Nabal; Abigail; Caleb | נָבָל; אֲבִיגַיִל | *Pharanem*; *Nabal, -em, -i, -is*; *Abigail, -e, -em, -i*; *Cālēbō* | *Nābāl-, Abīgail-* | Hebrew (hard call 13); settled *Cālēbō* |
| Jezreel; Jezreelitess | יִזְרְעֶאל | *Jezræl*; *Jezrælanam* 25.43, *Jezrælana* 27.3, *Jezrælensis* 30.5 | *Jezrælānam, Jezrælānā, Jezrælēnsis* | settled Josh 15:56 (noticed) |
| Palti son of Laish of Gallim | פַּלְטִי; גַּלִּים | *Phalti, Lais, Gallimensi* 25.44 | *Phaltī, Gallīmēnsī*; *Lais* kept | dative; settled *Lais*; Hebrew |
| Abishai, Zeruiah, Joab; Hittite | אֲבִישַׁי; צְרוּיָה; יוֹאָב | *Abisæus, Abisæo, Sarviæ, Joabi, Hettæō* 26.6 | *Abīsæus, Abīsæō, Jōābī*; *Sarviæ* kept | Hebrew; Greek ω; settled |
| Ziklag; Geshurites, Gezrites | | *Siceleg*; *Gessūræōs, Gerzæos* 27.8 | *Gerzæōs* | settled |
| Jerahmeelites | יְרַחְמְאֵלִי · Ἱερεμεήλ | *Jerameelitarum* 27.10, *Jerameelensium* 30.29 | *Jerameēlītārum, Jerameēlēnsium* | tsere, Greek η |
| Shunem; Gilboa; Endor | שׁוּנֵם | *Sunaman* 28.4; *Gelbōe*; *Endore* 28.7 | *Sūnaman, Ēndōre* | Hebrew; settled *Ēndōriōs* |
| Apollo, Phoebus | | *Apollinem, Phœbō* | kept | Gaffiot (noticed) |
| Aphek | | *Aphēc* | kept | settled |
| Besor; Cherethites; Calebites; Egyptian | הַבְּשׂוֹר; כְּרֵתִי | *Besorem*; *Cerethenses, Calebitidis* 30.14; *Ægyptius, ægyptius* | *Besōrem, Cerēthēnsēs, Cālēbītidis* | Hebrew; settled *Cālēb-* |
| The towns of 30:27–31 | | *Ramothanis, Jetherianis, Arœrensibus, Sephamothanis, Estamoanis, Rachalensibus, Hormanisque, Borasanensibus, Athacanis, Hebronensibus* | *Rāmōthānīs, Jetheriānīs, Arōērēnsibus, Sephamōthānīs, Estamōānīs, Rāchālēnsibus, Hormānīsque, Bōrasānēnsibus, Athācānīs, Hebrōnēnsibus* | settled *Rāmōtha, Arōēr, Horma, Hebrōn*; Hebrew (hard call 13) |
| Beth-shan | בֵּית שָׁן | *Bethsanis* 31.10, *Bethsanæ* 31.12 | *Bēthsānis* (spelling 31.12) | settled *Bēthsāne(m)* (hard call 7) |
