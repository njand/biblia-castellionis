# 2 Samuel: one form per person, place and people (names reader, 2026-11-21)

Every capitalized word of `text/draft/2SA.preview.usfm`, and every lower-case adjective of a people or place, was
grouped by its unmarked key and read with the seven verse readers' forms rows laid over the preview (`r1-forms.tsv`
… `r7-forms.tsv`), so each word was judged as it will stand after the merge. Each was checked against the settled
text (`data/gold/`, rebuilt from `text/*.usfm`, now with 1 Samuel), and then against the Greek (Brenton) and the
Hebrew (WLC), in the order 1 Samuel's names reader used (`data/review/1sam1-31-names.md`): settled form, Gaffiot,
the Greek's η/ω, then the Hebrew vowel (qamets, tsere, holem, shureq, hireq-yod long; decision 52). Gentile
adjectives take the founder's marks and the suffix's quantity (-ānus, -īnus, -ēnsis, -īta, -æus, -ius).

**Outputs**: `names-forms.tsv`, **118 rows**, only where the decided form differs from a reader's row or from the
preview. Each note says which reader row it overrides (`overrides rN's …`) or which preview form it replaces. Built by
a script in the scratch folder (`…/scratchpad/n/mk.py`); no other file was written.
**Check** (`check.py` from the 1 Samuel scratch, pointed at 2SA): 118 rows, 3 errors, each a row for a word that only
exists once its spelling row (below) is applied: 3:27 *Asaēlis*, 23:13 *Adullām*, 23:34 *Achītōphelis*. Six more
rows pass the check (its key folds j and i) but **`propose` will refuse them until the spelling rows are applied**,
because a decided form must spell the draft's word letter for letter: 11:9 *Ūrīās*, 13:3, 13:5, 13:32, 13:35
*Jōnādāb-*, 5:15 *Jāphīa*. If a spelling row is rejected, drop its forms row (the reader's row, if any, then stands).

The printed text (`text/orig/2SA.usfm`) keeps 1738's spellings whatever is decided here: *Asaclis, Vrjas, Iaphia,
Ionadab-, Berzelæus, Odollam, Achithophelis*.

## Spelling rows (for `data/decisions/` or the draft; not written by me)

Each `old` occurs exactly once in its verse of `text/draft/2SA.usfm` (checked by script).

| id | old | new | why |
|---|---|---|---|
| 2Sam.3.27 | Asaclis | Asaelis | 1738's printer's slip (transcription: *Asaclis*, a *c*; 1750 *Asaelis*); Asahel, the book's *Asaēl* |
| 2Sam.5.15 | Iaphia | Japhia | the draft left 1738's consonantal *I* (as it did not elsewhere: *Jebahar* beside it); settled *Jāphīam* |
| 2Sam.11.9 | Urjas | Urias | the book's *Ūrīās* everywhere else (1738 *Vrjas* here only) |
| 2Sam.13.3 | Ionadabum | Jonadabum | consonantal *I* left by the draft (1738 *Ionadab-*; *Ioabus* became *Joabus*) |
| 2Sam.13.5 | Ionadabus | Jonadabus | the same |
| 2Sam.13.32 | Ionadabus | Jonadabus | the same |
| 2Sam.13.35 | Ionadabus | Jonadabus | the same |
| 2Sam.17.27 | Berzelaeus | Berzellaeus | one form for Barzillai (1738 *Berzellæ-* at 19:31, 33, 39, 21:8; בַּרְזִלַּי doubled l); no forms row (unmarked) |
| 2Sam.23.13 | Odollam | Adullam | the settled 1 Sam 22:1 *Adullāmam* (respelled from 1738's *odollamam*), Josh 15:35 *Adullām* |
| 2Sam.23.34 | Achithophelis | Achitophelis | one form for Ahithophel (1738 *Achitophel-* 16 times in 15–17, *Achithophelis* here only) |

## Hard calls (for Nathan)

1. **Joab: *Jōābus, Jōābī, Jōābō(que), Jōābum*** (78 rows, the largest change: 67 replace the preview's *Jōab-*, 11 override readers' *Jōabī*). The readers wrote *Jōab-* (r4, r5, r6,
   r7 even changed the preview's *Jōābī* at 12:28, 14:30, 17:25, 18:2, 18:15, 20:7, 20:11, 20:15, 23:18, 23:24, 23:37 to
   *Jōabī*, leaving the choice to the merge). The settled text has Joab once, **1 Sam 26:6 *Jōābī*** (the same man,
   decided by 1 Samuel's names reader: יוֹאָב holem, qamets; Greek Ἰωάβ ω), and the preview kept it at 2:22, 3:29, 11:22.
   Settled first: *Jōāb-* in every case. Gaffiot has *Joab* unmarked (M only). If the qamets should go, the settled
   1 Sam 26:6 would need Nathan's hand edit and every row here becomes *Jōab-*.
2. **Ahithophel: *Achītōphel-*** (r5's form, Hebrew alone: אֲחִיתֹפֶל hireq-yod, holem) and **23:34 respelled**
   *Achithophelis → Achitophelis*, *Achītōphelis* (r7 kept 1738's *th*, *Achīthōphelis*). One spelling per person, as
   1 Samuel's *Bethsanæ → Bethsanis*. Drop the spelling row to keep r7's form.
3. **Mephibosheth: *Mephībōseth-*** for Jonathan's son (r2, r3, r5, r6, r7; מְפִיבֹשֶׁת hireq-yod, holem), and **21:8
   *Mephībōsetum*** for Rizpah's son (r7): another man, whom 1738 spells without *h*. Kept as printed and marked
   alike; no spelling row (Castellio may have meant to tell the two apart). Readers agree; nothing to override.
4. **Jonadab: *Jōnādābum, Jōnādābus*** after four spelling rows (I → J). r4 wrote *Iōnadab-* (Greek ω only). The draft
   turns every other consonantal I into J; ω gives *Jō-*, the two qamets give *-nādāb-* as the settled *Abīnādāb-*. Without
   the spelling rows: *Iōnādābum, Iōnādābus*.
5. **23:38 *Īra*, 23:39 *Ūrīās***: the preview lower-cased both (*īra*, read as the noun; *uriās*) because the case
   rule lowers a verse's first word when the sentence runs on, and both open their verse in the list of heroes. r7's
   forms rows (*Īra*, *Ūrīās*) are capitalized, and `verses.keeps_capital` then leaves a verse's first word alone
   when its decided form has a capital: **r7's rows suffice**; no row of mine. (A forms row cannot change case anywhere
   else: `decided_word` keeps the draft's letters and only takes the long vowels.)
6. **Asahel at 3:27**: 1738 prints *Asaclis*, a slip for *Asaēlis* (1750 *Asaelis*); spelling row above, form
   *Asaēlis* (as r1's *Asaēl, Asaēlem*, with the *a-e* apart; the preview's *Asæl* wrong: עֲשָׂהאֵל, Ἀσαήλ).
7. **Abel-beth-maacah: *Ābēlmaacham, Ābēlmaachæ*, 20:18 *Ābēl*** (r6 *Abēl-*, citing the settled *Abēl*): that *Abēl*
   is Adam's son (הֶבֶל, segol). The town is אָבֵל, the word of the settled *Ābēlmehōlæ* (Judg 7:22).
8. **Settled forms the readers missed**: *Ammīēlis* (9:4, 9:5, 17:27; settled *Ammīēl*, Num 13:12; r3, r5 *Ammiēlis*),
   *Adrīēle* 21:8 (settled 1 Sam 18:19 *Adrīēlī*, the same man; r7 *Adriēle*), *Anāthōthēnsis* 23:27 (settled
   *Anāthōtha*; r7 *Anathōth-*), *Pharathōnēnsis* 23:30 (settled *Pharathōne, Pharathōnīta*, a unmarked; r7
   *Pharāth-*), *Bēthrohōbānōrum* 10:6 (settled *Bēthrohōbēnsium*; r3 *Beth-*), *Hemāthæ* 8:9 (settled *Hemātham*;
   preview and r3 unmarked, r3 citing *Hemath*, which is Hammath of Naphtali, Josh 19:35), *Sēlæ* 21:14 (settled
   *Sēla*, Josh 18:28, Zela), *Gabāānus* 23:29 (settled *Gabāānīs*, Judg 20:33).
9. **Within-book consistency on the Hebrew**: *Īstōbum, Īstōbus* 10:6, 10:8 (r3 *Istōb-*; the same אִישׁ as r1's
   *Īsbōseth-*); *Bahūrīm, Bahūrīmō*, 3:16 *Bathūrīm* (r1, r5, r6 *Bahurīm*: they marked the hireq-yod but not the
   shureq); *Rēchāb-* (r2 *Rēchab-*: tsere marked, qamets not); *Hānōn, Hānōnī* (r3 *Hanōn*); *Hīrāmus* 5:11 (r2
   *Hīramus*; the settled *Hīram* r2 cites is Hirah, Gen 38:1, another man); *Eliāda* 5:16 (r2 left him unmarked while
   marking his brothers). If Hebrew-only marks go (call 11), these go with them.
10. **Endings**: 23:36 *Bānis* (nominative, *Bānis Gadius*; the preview *Banīs*), 23:26 *Accis* (genitive, *Īra
    Accis fīlius*; the preview *Accīs*), 19:23 *Semei* (vocative, the king to Shimei; the preview *Semeī*), declined as
    the settled *Achis, Achī* and *Noemis, Noemī* (1 Samuel's call 9): -is and the vocative short, dative/ablative -ī.
11. **Marked on the Hebrew alone** (no settled form, Gaffiot or Greek long vowel). Readers': r1 *Īsbōseth-, Assūræōs,
    Gīæ, Bethrōne, Cheleābus, Adōnias, Hagīthæ, Abītālis, Jethraāmus, Bathurīm, Bōrsira*; r2 *Mephībōseth-, Sammūa,
    Elīphāletus, Baalpharasīmum, Ahiōne, Ōbēdedōm-* (settled *Ōbēd*), *Elīsūa, Sōbābus*; r3 *Sība, Lōdabare, Thōis/Thōī,
    Bērōthai, Sarājam, Banājam, Elīāmī, Istōb-, Sōbach-, Achīlūdī*; r4 *Jedīdiam, Thecuāna*; r5 *Achītōphel-, Chūsæ-,
    Archīt-, Gīlōne, Gīlōnium, Amāsa, Sōbis, Rōgelēnsis, Absālōmānōrum, Bahurīm*; r6 *Chūsis/-ī/-im* (the Cushite;
    the settled *Chus*, Gen 10:7, is unmarked), *Rōgelīmō, Jāīrius* (settled *Jāīr*, so not Hebrew-only); r7 *Armōnim,
    Jesbibenōbus, Gōbam, Elehānān, Hacmōnis, Dōdis, Achōis, Achōjēnsis, Elīca, Harōdius, Rībais, Abīalbōn, Achīāmus,
    Elīphelethus, Harārīta, Husāthēnsis, Nethōphātēnsis, Arbāthēnsis, Beroniēnsis, Salabōnēnsis, Arārēnsis,
    Maachāthēnsis*. Mine: *Jōnādāb-* (the ā's), *Jāphīa* (settled), *Bahūr-*, *Rēchāb-*, *Hānōn*, *Hīrāmus*, *Eliāda*,
    *Bānis*. The preview's own (from earlier settled books or the lexicon): *Absālōm-* (Greek ω too), *Abīsæ-, Thāmār*
    (settled). If Nathan drops Hebrew-only marks, these are the rows (and the readers' rows) to strip.
12. **Kept unmarked**, as the readers and preview have them: *Adarezer-* (Ἁδρααζάρ; the -ānus adjective marked),
    *Arauna, Respha, Ajæ, Baana, Oza, Ettæ-* (Ittai), *Berzellæ-, Chamaam-, Bochris, Siva, Seba* (r6: שֶׁבַע segol; the
    preview's *Sēba* came from *sēbum*), *Semeis, Semaæ, Samaæ, Saphatias, Thomais/Tholmaim, Bethsabam, Jerobosethi,
    Micham* (settled), *Maacha*, the heroes of 23:8–39 without a long vowel the readers could match.

## Noticed, not changed

- **Capitals of the lower-case name adjectives** (1738 prints them small; the settled text capitalizes *Isrāēlītic-,
  Dāvīdic-, Jūdaic-*): the readers' layout rows capitalize every one (1:12, 1:20, 2:3, 2:4, 2:13, 2:24, 3:6, 5:2, 6:2,
  6:5, 6:21, 7:8, 7:24, 10:6, 10:8, 10:16, 10:18, 12:8 ×2, 13:39, 15:2, 15:12, 16:5, 20:19, 20:26, 23:1, 23:20) **except
  15:9 *isrāēlīticās***, which has no layout row: the merge should add one (*Isrāēlīticās*).
- **Talmai** is *Thomais* at 3:3 and *Tholmaim* (accusative) at 13:37 in 1738: two spellings of one man, both kept as
  printed (the *Thomais* form may be Castellio's own from the Greek Θολμί/Θοαμαί; not checked on another printing).
  For the notes or a spelling row if Nathan wants one form.
- **The Cushite** (18:21–32, *Chusis, Chusī, Chusim*, r6) is Castellio's proper name for הַכּוּשִׁי, distinct from Hushai
  (*Chūsæus*). r6's shureq ū stands against the settled unmarked *Chus* (Gen 10:7); left to r6.
- *Gelbōem* 1:6 (r1; the preview's *Gelbœm*) and *Asaēl* (r1, r7; the preview's *Asæl*) write two vowels where the
  draft has the ligature: `decided_word` allows *æ → ae*, so these apply.
- 21:8 *Micholis* (Hebrew Michal, many manuscripts Merab), 21:18 *Nōbam* (Hebrew Gob), 21:19 *Goliathum*: Castellio's
  readings, for the notes readers (r7 noticed them).
- *Jōva* in the ablative: every *ā, cōram, ab ipsīus Deō Jōva* and ablative absolute (8:6 *tūtante*, 24:1 *īrātō
  Isrāēlītīs*) has a reader's *Jōvā* row; the remaining *Jōva* are nominatives or vocatives (checked by script on every
  occurrence).

## Decisions

| Person / place / people | Hebrew · Greek | In 2 Samuel (preview; readers' rows) | Settled | Decided |
|---|---|---|---|---|
| Jova; Jacob's people | יְהוָה | *Jōva, Jōvæ, Jōvam*; *Jōvā* (r1–r7, ablatives); *Jācōbæōrum* 23.1 | *Jōva, Jōvā*; *Jācōbæōrum* | kept (readers) |
| Saul; his house | שָׁאוּל · Σαούλ | *Saūl-*; *Saūlīnam* 3.6 (r1), *Saūlīnæ* 16.5 (r5) | 1 Sam *Saūl-, Saūlīn-* | kept |
| David; his men | | *Dāvīd-*; *Dāvīdic-* (r1, r3, r6, r7) | *Dāvīd-, Dāvīdica* | kept |
| Jonathan | יוֹנָתָן | *Jonathān-* | 1 Sam *Jonathān-* | kept |
| Joab | יוֹאָב · Ἰωάβ | *Jōab-* (r4–r7 too); *Jōābī* 2.22, 3.29, 11.22 | 1 Sam 26:6 *Jōābī* | ***Jōāb-*** (call 1) |
| Abishai; Asahel; Zeruiah | אֲבִישַׁי; עֲשָׂהאֵל · Ἀσαήλ | *Abīsæ-*; *Asæl* → *Asaēl-* (r1, r7); *Asaclis* 3.27; *Sarviæ* | *Abīsæ-, Sarviæ* | *Asaēlis* 3.27 (spelling; call 6) |
| Abner; Ner; Abner's men | אַבְנֵר · Ἀβεννήρ | *Abnēr-*; *Abnērī* (r1); *Abnēriānōrum* (r1); *Nēris* | 1 Sam *Abnēr-, Nēris* | kept |
| Ish-bosheth; Mephibosheth | אִישׁ־בֹּשֶׁת; מְפִיבֹשֶׁת | *Īsbōseth-* (r1, r2); *Mephībōseth-* (r2–r7), *Mephībōsetum* 21.8 (r7) | | kept (call 3) |
| Ish-tob | אִישׁ טוֹב | *Istōbum, Istōbus* (r3) | | ***Īstōb-*** (call 9) |
| Jerubbesheth; Abimelech; Thebez | | *Jerobosethi, Abimelechum*; *Thēbem* (r3) | *Abimelechum, Thēbēn* | kept |
| Jebusites, Hivites, Canaanites, Amorites, Hittites | | *Jebūsæ-, Hevæōrum, Chananæōrum, Amorræōrum, Hettæ-* | the same | kept |
| Uriah | אוּרִיָּה | *Ūrīās, Ūrīæ, Ūrīam* (r3, r4); *Ūrjās* 11.9; *uriās* 23.39 → *Ūrīās* (r7) | *Ūrīæ* (Matt 1:6) | *Ūrīās* 11.9 (spelling); r7's 23.39 kept (call 5) |
| Ira; Ikkesh | עִירָא; עִקֵּשׁ | *Īra* 20.26, 23.26; *īra* 23.38 → *Īra* (r7); *Accīs* 23.26 | | *Accis* (call 10) |
| Ahinoam; Abigail; Nabal; Jezreel | | *Achīnōamā* (r1); *Abīgaile*; *Nābālis*; *Jezræl, Jezrælēns-* (r1) | 1 Sam the same | kept |
| David's sons and wives (3:2–5) | | *Amnōn-* (r1, r4), *Amnōniæ* (r4); *Cheleābus, Adōnias, Hagīthæ, Saphatias, Abītālis, Jethraāmus, Eglā* (r1); *Maachæ, Thomais* | | kept (call 11) |
| Absalom; his men | אַבְשָׁלוֹם · Ἀβεσσαλώμ | *Absālōm-*; *Absālōmānōrum* (r5) | | kept |
| Tamar; Talmai; Ammihud; Geshur | | *Thāmār-*; *Thomais* 3.3, *Tholmaim* 13.37; *Ammīūdis* (r4); *Gessūr-* (r4, r5) | *Thāmār-, Ammīūdī, Gessūris* | kept (noticed) |
| David's sons born at Jerusalem (5:14–16) | | *Sammūa, Sōbābus* (r2), *Nāthan, Solomō, Jebahar, Elīsūa* (r2), *Nephegus, Iaphia, Elīsāma* (r2), *Eliada, Elīphāletus* (r2) | *Elīsāma, Nephegus, Solomō, Jāphīam* | *Jāphīa* 5.15 (spelling), *Eliāda* |
| Nathan the prophet | נָתָן | *Nāthan, Nāthanī, Nāthanem* (r2, r4), *Nāthanis* (r7) | *Nāthanī* (Luke 3:31) | kept |
| Jonadab; Shimeah | יוֹנָדָב · Ἰωναδάβ | *Ionadab-* → *Iōnadab-* (r4); *Semaæ* | *Abīnādāb-* | ***Jōnādāb-*** (spelling; call 4) |
| Ahithophel; Gilo | אֲחִיתֹפֶל | *Achītōphel-* (r5), *Achīthōphelis* 23.34 (r7); *Gīlōne, Gīlōnium* (r5), *Gīlōnēnsis* (r7) | | *Achītōphelis* 23.34 (spelling; call 2) |
| Hushai the Archite; the Cushite | חוּשַׁי; הַכּוּשִׁי | *Chūsæ-, Archīt-* (r5); *Chūsis, Chūsī, Chūsim(que)* (r6) | *Chus* (Gen 10) | kept (noticed) |
| Zadok; Abiathar; Ahimaaz; Jonathan; Ahitub; Ahimelech | | *Sadōc-* (r5, r6); *Abiāthār-*, *Abiāthāris* (r3, r5); *Achīmaa-* (r5, r6); *Achitōbī; Achīmelechum* | 1 Sam the same; *Sadōcum* (Matt) | kept |
| Ittai the Gittite; Gath; Gittites | | *Ettæ-* (r6); *Gethā, Gethæ, Getham*; *Gethān-* (r2, r5, r6); *Gethæum* 21.19 | 1 Sam *Gethā, Gethæ, Gethānus* | kept |
| Cherethites, Pelethites | | *Cerēthæ-* (r3, r5, r6), *Phelethæ-* (r3, r5, r6) | 1 Sam *Cerēthēnsēs* | kept |
| Benaiah; Jehoiada | בְּנָיָהוּ; יְהוֹיָדָע | *Banāj-* (r3, r6, r7); *Jojādæ* | | kept |
| Ziba; Machir; Ammiel; Lo-debar | צִיבָא; עַמִּיאֵל | *Sība-* (r3, r5, r6); *Māchīr-*; *Ammiēlis* (r3, r5); *Lōdabar-* (r3, r5) | *Māchīr-, Ammīēl* | ***Ammīēlis*** (call 8) |
| Shimei; Gera; Bahurim | שִׁמְעִי; בַּחוּרִים | *Semeis, Semeī*; *Gēræ*; *Bahurīm(ō)* (r5, r6), *Bathurīm* 3.16 (r1) | *Gēræ* | *Semei* 19.23; ***Bahūrīm(ō), Bathūrīm*** |
| Barzillai; Rogelim; Chimham | בַּרְזִלַּי | *Berzelæus* 17.27, *Berzellæ-*; *Rōgel-* (r5, r6); *Chamaam-* | | *Berzellæus* 17.27 (spelling) |
| Amasa; Jether; Nahash; Shobi; Rabbah | עֲמָשָׂא | *Amāsa-* (r5, r6); *Jethræ*; *Nāhæ* (r3, r5); *Sōbis* (r5); *Rabbā* (r5), *Rabbam* | 1 Sam *Nāhās*; *Rabba* | kept |
| Ammonites; Hanun | חָנוּן · Ἀννών | *Ammonīt-*; *Hanōn, Hanōnī* (r3) | *Ammonīt-* | ***Hānōn, Hānōnī*** |
| Aram: Zobah, Beth-rehob, Rehob, Maacah, Tob | | *Sophēn-* (r3), *Bethrohōbānōrum* (r3), *Rochōbī, Rohōbānī* (r3), *Maacha(m)* | *Sophēnæ, Bēthrohōbēnsium* | ***Bēthrohōbānōrum*** (call 8) |
| Hadadezer; Shobach; Helam; Toi; Joram; Hamath | הֲדַדְעֶזֶר; חֲמָת | *Adarezer-*, *Adarezeriān-* (r3); *Sōbach-* (r3); *Helamam*; *Thōis, Thōī* (r3); *Jorāmum*; *Hemathæ* | *Jorāmum, Hemātham* | ***Hemāthæ*** |
| Betah, Berothai; Edom; Syria, Damascus | | *Betha, Bērōthai* (r3); *Idūmæ-*; *Syr-*, *Damascēnōrum* (r3) | *Idūmæ-, Damascēnōrum* | kept |
| Moabites, Amalekites, Philistines, Egypt | | *Mōabīt-*, *Mōabīticōs* (r7); *Amālēchīt-*; *Palæstīn-*; *Ægypt-* | the same | kept |
| Ahio, Uzzah, Abinadab, Nacon, Obed-edom | | *Ahiōne* (r2); *Oza, Ozæ*; *Abīnādābī*; *Nachōnis* (r2); *Ōbēdedōm-* (r2) | *Abīnādābī, Ōbēd* | kept |
| Michal; Paltiel; Laish | מִיכַל | *Mīchol-*, *Mīcholis* (r7); *Phaltīēle* (r1); *Lais* | 1 Sam *Mīchol-, Lais* | kept |
| Rechab, Baanah, Rimmon, Beeroth | רֵכָב | *Rēchab-* (r2); *Baana-*; *Remmōnis*; *Bērōtha, Bērōthītæ* (r2), *Bērōthēnsis* (r7) | *Remmōnis, Bērōtha* | ***Rēchāb-*** |
| Hiram; Tyre; Sidon | חִירָם | *Hīramus* (r2); *Tyrī*; *Sīdōne* | *Tyrī, Sīdōne* | ***Hīrāmus*** |
| Bathsheba; Eliam; Jedidiah | | *Bethsabam*; *Elīāmī* (r3), *Elīāmus* (r7); *Jedīdiam* (r4) | | kept |
| Tekoa | | *Thecuā* (r4), *Thecuāna* (r4), *Thecuānus* (r7) | | kept |
| Gibeon, Gibeah; Gibeonites | | *Gabaōn-*, *Gabaōniam, -ium* (r1), *Gabaōnītīs* (r7); *Gabāā, Gabā* (r2), *Gabāam*; *Gabaanus* 23.29 | *Gabaōn-, Gabāa, Gabāānīs* | ***Gabāānus*** |
| Gilead; Jabesh; Mahanaim; Gilboa | | *Galaadīt-* (r1, r7); *Jābēnsibus*; *Mahanaim-* (r1); *Gelbōe, Gelbōem* (r1) | the same | kept |
| Hebron; Ziklag; Ashkelon | | *Hebrōn-*, *Hebrōniīs* (r1); *Siceleg(e)* (r1); *Ascalōniīs* (r1) | *Hebrōn-, Siceleg, Ascalōne* | kept |
| Rizpah, Aiah; Armoni; Adriel the Meholathite | עַדְרִיאֵל | *Respha, Ajæ*; *Armōnim* (r7); *Adriēle* (r7), *Mōlāthītæ* | 1 Sam *Adrīēlī, Mōlāthītæ* | ***Adrīēle*** (call 8) |
| Zela; Kish | צֵלַע | *Selæ*; *Cīs* | *Sēla, Cīs* | ***Sēlæ*** |
| The giants (21:16–22) | | *Jesbibenōbus, Gōbam, Elehānān, Jaarei* (r7); *Nōbam*; *Sobochæus, Saphum, Goliathum* | *Nōbam* | kept |
| Abel-beth-maacah; Sheba, Bichri | אָבֵל; שֶׁבַע | *Abēlmaach-* (r6), *Abēl* 20.18; *Seba-* (r6), *Bochris* | *Ābēlmehōlæ* | ***Ābēlmaach-, Ābēl*** (call 7) |
| David's officers (8:16–18, 20:23–26) | | *Achīlūdī* (r3, r6), *Jōsāphāt-*, *Sarājam* (r3), *Adōrāmus*, *Siva*, *Jāīrius* (r6) | *Jōsāphātum, Jāīr* | kept |
| The heroes (23:8–39) | | *Jasobaamus, Hacmōnis, Eleāzarus, Dōdis, Achōis, Agēs, Harārīta, Elehānān, Dōdōnis, Bēthlehemīta, Samma, Harōdius, Elīca, Heles, Phaltius, Accīs, Thecuānus, Abīezer, Anathōthēnsis, Mobonais, Husāthēnsis, Salmōn, Achōjēnsis, Maharais, Nethōphātēnsis, Helebus, Baanæ, Ithais, Gabaanus, Benjamīta, Banājas, Pharāthōnēnsis, Heddais, Gaa, Abīalbōn, Arbāthēnsis, Azmavethus, Beroniēnsis, Eliaba, Salabōnēnsis, Jasenis, Jonathān, Samma, Arārēnsis, Achīāmus, Sarari, Elīphelethus, Ahasbais, Maachāthēnsis, Elīāmus, Achithophelis, Gīlōnēnsis, Hesrais, Carmēlīta, Pharais, Arbius, Igaal, Nāthanis, Sophēnē, Banīs, Gadius, Selecus, Ammonīta, Naharais, Bērōthēnsis, Īra, Jethrius, Garebus, Ūrīās, Hettæus* (r7) | *Abīezere, Anāthōtha, Pharathōne, Gabāānīs, Dōdōnis, Carmēlītæ* | ***Accis, Anāthōthēnsis, Pharathōnēnsis, Gabāānus, Bānis, Achītōphelis***; the cave ***Adullām*** 23:13 |
| Araunah; Gad; Dan, Beersheba; Aroer, Jazer, Dan-jaan, Tahtim-hodshi | | *Arauna-*; *Gadus, Gadum*, *Gadīnōrum*; *Dane, Bersabam*; *Arōēre, Jazēr, Daniaan, Hasdis* | *Gadus, Dane, Bersabam, Arōēre, Jazēr* | kept |
| Jerusalem, Zion, Millo; Jordan; Kidron; Jericho; Euphrates; En-rogel | | *Hierosolym-*, *Sīōnem*, *Mellōne*; *Jordān-*; *Cedrōnem*; *Hierichūnte*; *Euphrātem*; *Ēnrōgēl* | the same | kept |
| Baal-perazim, Baal-hazor, Gezer, Geba; Valley of salt, Metheg-ammah | | *Baalpharasīmum* (r2), *Baalhasōre* (r4), *Gazer*, *Gabā* (r2); *Gebelem, Methegammam* | *Gazer, Gaba* | kept |
| Ephraimites, Josephites, Benjamites, Jeminites, Judaeans, Levites, Israelites | | *Ephrāimīt-*, *Jōsēphidārum* (r6), *Benjamīt-*, *Jemīniēnsis*, *Jūdæ-*, *Lēvītās*, *Isrāēlīt-*, *Isrāēlītides* (r1) | the same; *Jōsēphidæ* | kept (15:9 capital: noticed) |

## Report

- **Rows**: 118 in `names-forms.tsv` (Joab 78; Jonadab 4; the rest one to three each), plus ten spelling rows in the
  table above for the merge to place. Every row's note names the reader row it overrides (39 override a reader, the
  other 79 replace a preview form no reader touched).
- **Disagreements settled**: readers against the settled text (Joab, Ammiel, Adriel, Anathoth, Pirathon,
  Beth-rehob, Abel-maacah), readers against each other or their own rule (Achitophel's *th*, *Istōb-* beside
  *Īsbōseth-*, Bahurim's shureq, Rechab's and Hiram's qamets, Eliada), preview endings (*Banīs, Accīs, Semeī* 19:23),
  printer's slip (3:27 *Asaclis*) and the draft's leftover consonantal *I* (Ionadab, Iaphia) and *j* (11:9 *Urjas*).
- **Not my rows, but needed at the merge**: a layout row capitalizing 15:9 *Isrāēlīticās*; the ten spelling rows
  before the six forms rows that depend on them. 23:38–39's capitals come from r7's rows (no change needed).
- **For Nathan**: call 1 (Joab's qamets, against the readers), call 11 (whether to keep marks found only in the
  Hebrew), and the Talmai spellings (*Thomais*/*Tholmaim*), left as printed.
