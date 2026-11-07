# Matthew 14–28, stage 5: structure (quotation marks, quoted Scripture, poetry, paragraphs)

Proposed 2026-11-07 (overnight run), on the text **after stages 2–4** (`matt14-28-stage2.md`,
`-spelling.md`, `-macrons.md` applied in full). The **Apply** lines compose in that order and were checked to
match once on that text. Within this file they compose in order too: group 1 before group 4, for instance, at
15:9 and 22:44.

What was compared (`pipeline/structure.py`): your draft's paragraphs and poetry against the BSB's
(`sources/parallel/bsb/Matt.tsv`), its quotation marks against decisions 4 and 25, and its layout against your
settled chapters' conventions. Calibration on settled Matthew 1–13: you open a paragraph at 75 of the BSB's 76
paragraph starts (and at 81 more places of your own), and you set as poetry 48 of the BSB's 49 poetry verses,
plus 13 short quotations of your own.

The draft differs from those conventions in one big way: **it has no `\qt` (italic quoted Scripture) and no
poetry lines at all** (settled Matthew 1–13 has 67 `\qt` and 61 poetry verses). The LaTeX it was converted from
evidently had no `\emph{}` or verse blocks yet. Groups 3–4 supply them in your settled style: short quotations
inline (`\qt ‘…’\qt*`, as Matt 4:7, 9:13), longer and poetic ones as `\q1`/`\q2` lines with each line in `\qt`,
the BSB's line breaks put at the matching Latin clause, and an open speech's “ repeated where the block begins
(*“‘Angelīs*, Matt 4:6). Where prose continues the same paragraph after a block, `\m` is added.

## 1. Quotation marks out of balance (4)

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 15:9** The speech that began at 15:3 is never closed before the new paragraph at 15:10.
   **Apply:** `Matt.15.9` la: `doctrīnam docentēs.’` → `doctrīnam docentēs.’”`
2. **Matt 20:28** The same: the speech of 20:25–28 is not closed before 20:29.
   **Apply:** `Matt.20.28` la: `līberātiōnem impendat.` → `līberātiōnem impendat.”`
3. **Matt 22:44** Inside Jesus' question, the psalm is in ‘…’ and the Lord's words inside it in “…”, so they
   close “ then ’: *tuōrum”’?* (your draft has *’”*, which closes the speech early; 22:45 then closes it again).
   **Apply:** `Matt.22.44` la: `pedum tuōrum’”?` → `pedum tuōrum”’?`
4. **Matt 23:30** Words quoted inside Jesus' speech take ‘…’ (decision 4), not “…”.
   **Apply:** `Matt.23.30` la: `dīcitisque: “Sī majōrum` → `dīcitisque: ‘Sī majōrum`
   **Apply:** `Matt.23.30` la: `in vātum sanguine sociī.”` → `in vātum sanguine sociī.’`

Matt 19:30 and 24:51 end a chapter inside a speech that continues in the next (20:1, 25:1 reopen it with “):
that is your convention, nothing to change.

## 2. Reported speech in ‘…’ (decisions 4 and 25) (3)

All 41 passages in ‘…’ were read. These three are reported (accusative and infinitive) and lose their marks;
the other 38 are direct words or Scripture and keep them.

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 21:3** *dīcētis: ‘Dominum iīs egēre,’*: “you shall say that the Lord needs them”.
   **Apply:** `Matt.21.3` la: `‘Dominum iīs egēre,’` → `Dominum iīs egēre,`
2. **Matt 23:16** *quī dīcitis, ‘Sī quis per templum jūret, nihil esse … eum tenērī.’*
   **Apply:** `Matt.23.16` la: `‘Sī quis per templum jūret,` → `Sī quis per templum jūret,`
   **Apply:** `Matt.23.16` la: `eum tenērī.’` → `eum tenērī.`
3. **Matt 23:18** *Item, ‘Sī quis per āram jūrāverit, id nihil esse … eum tenērī.’* (still governed by
   *dīcitis*, 23:16).
   **Apply:** `Matt.23.18` la: `‘Sī quis per āram` → `Sī quis per āram`
   **Apply:** `Matt.23.18` la: `eum tenērī.’` → `eum tenērī.`

## 3. Quoted Scripture in italics, inline (11)

Short quotations, set inline as your Matt 4:7, 5:21, 9:13. Sources from the BSB's cross-references.

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 15:4** Exod 20:12; 21:17.
   **Apply:** `Matt.15.4` la: `‘Honōrā patrem atque mātrem,’` → `\qt ‘Honōrā patrem atque mātrem,’\qt*`
   **Apply:** `Matt.15.4` la: `‘Quī patrī mātrīve male dīxerit, morte plēctātur.’` → `\qt ‘Quī patrī mātrīve male dīxerit, morte plēctātur.’\qt*`
2. **Matt 19:5** Gen 2:24.
   **Apply:** `Matt.19.5` la: `‘Proptereā relinquet vir patrem atque mātrem, et adhærēbit uxōrī suæ, fīetque ex duōbus ūna carō.’` → `\qt ‘Proptereā relinquet vir patrem atque mātrem, et adhærēbit uxōrī suæ, fīetque ex duōbus ūna carō.’\qt*`
3. **Matt 19:18–19** Exod 20:13–16, 12; Lev 19:18 (as your 5:21 *‘Nē occīditō*).
   **Apply:** `Matt.19.18` la: `“Nē occīditō. Nē adulterātō. Nē fūrātor. Falsum testimōnium nē dīcitō.` → `“\qt Nē occīditō. Nē adulterātō. Nē fūrātor. Falsum testimōnium nē dīcitō.\qt*`
   **Apply:** `Matt.19.19` la: `Honōrā patrem atque mātrem, et alterum ut tē ipsum dīligitō.”` → `\qt Honōrā patrem atque mātrem, et alterum ut tē ipsum dīligitō.\qt*”`
4. **Matt 21:9** Ps 118:26 (the acclamations *Hōsanna* stay roman; the BSB sets the three cries as poetry
   lines: say so if you want that too).
   **Apply:** `Matt.21.9` la: `bene sit eī quī venit in nōmine Dominī,` → `\qt bene sit eī quī venit in nōmine Dominī,\qt*`
5. **Matt 21:13** Isa 56:7; Jer 7:11 (the speech reopens with “, as your 4:7).
   **Apply:** `Matt.21.13` la: `“‘Domus mea domus supplicātiōnis vocābitur,’` → `\qt “‘Domus mea domus supplicātiōnis vocābitur,’\qt*`
   **Apply:** `Matt.21.13` la: `‘spēluncam latrōnum.’”` → `\qt ‘spēluncam latrōnum.’”\qt*`
6. **Matt 22:32** Exod 3:6.
   **Apply:** `Matt.22.32` la: `‘Ego sum Deus Abrāhāmī, Deus Isaacī, et Deus Jācōbī.’` → `\qt ‘Ego sum Deus Abrāhāmī, Deus Isaacī, et Deus Jācōbī.’\qt*`
7. **Matt 22:37** Deut 6:5.
   **Apply:** `Matt.22.37` la: `“‘Dominum Deum tuum tōtō corde, tōtō animō, tōtā mente amātō.’` → `\qt “‘Dominum Deum tuum tōtō corde, tōtō animō, tōtā mente amātō.’\qt*`
8. **Matt 22:39** Lev 19:18.
   **Apply:** `Matt.22.39` la: `‘Alterum ut tē ipsum amātō.’` → `\qt ‘Alterum ut tē ipsum amātō.’\qt*`
9. **Matt 23:39** Ps 118:26.
   **Apply:** `Matt.23.39` la: `‘Bene sit venientī in nōmine Dominī.’”` → `\qt ‘Bene sit venientī in nōmine Dominī.’”\qt*`
10. **Matt 27:35** Ps 22:18 (the narrator's quotation, in “…” as your Matt 2:6, 2:15).
    **Apply:** `Matt.27.35` la: `“Mea inter sēsē vestīmenta partītī, super veste meā sortem jēcērunt.”` → `\qt “Mea inter sēsē vestīmenta partītī, super veste meā sortem jēcērunt.”\qt*`
11. **Matt 27:46** Ps 22:1: *not* proposed (Jesus' own cry, as the NRSV and your Mark have no italics for
    it); listed so the choice is visible.

## 4. Quoted Scripture as poetry (7 passages)

The BSB sets these as poetry; your settled chapters set every such passage so (48 of 49 in Matthew 1–13). The
whole verse text is rewritten only to insert line markers and `\qt`: the words and punctuation are unchanged
(checked: same words before and after).

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 15:8–9** Isa 29:13.
   **Apply:** `Matt.15.8` la: `\v 8 ‘Hic populus mē et ōre accēdit, et labiīs honōrat, sed eōrum animus procul abest ā mē.` → `\q1 \v 8 \qt “‘Hic populus mē et ōre accēdit, et labiīs honōrat,\qt* \q2 \qt sed eōrum animus procul abest ā mē.\qt*`
   **Apply:** `Matt.15.9` la: `\v 9 Frūstrā autem mē venerantur, hūmānōrum præceptōrum doctrīnam docentēs.’”` → `\q1 \v 9 \qt Frūstrā autem mē venerantur,\qt* \q2 \qt hūmānōrum præceptōrum doctrīnam docentēs.’”\qt*`
2. **Matt 21:5** Zech 9:9 (Isa 62:11); then `\m` for 21:6.
   **Apply:** `Matt.21.5` la: `\v 5 “Dīcite puellæ Sīōnī: ‘Ecce rēx tuus tibi venit mānsuētus, īnsidēns asinæ, et asellō jūmentī pullō.’”` → `\q1 \v 5 \qt “Dīcite puellæ Sīōnī:\qt* \q2 \qt ‘Ecce rēx tuus tibi venit mānsuētus,\qt* \q1 \qt īnsidēns asinæ,\qt* \q2 \qt et asellō jūmentī pullō.’”\qt*`
   **Apply:** `Matt.21.6` la: `\v 6 Igitur profectī` → `\m \v 6 Igitur profectī`
3. **Matt 21:16** Ps 8:2.
   **Apply:** `Matt.21.16` la: `‘Per os īnfantium ac lactentium laudem condis.’”` → `\q1 \qt “‘Per os īnfantium ac lactentium\qt* \q2 \qt laudem condis.’”\qt*`
4. **Matt 21:42** Ps 118:22–23; then `\m` for 21:43 (the speech goes on).
   **Apply:** `Matt.21.42` la: `‘Quem lapidem improbāverant strūctōrēs, is adhibitus est ad caput angulī, id quod ā Dominō profectum est, et nōbīs mīrum vidētur.’` → `\q1 \qt “‘Quem lapidem improbāverant strūctōrēs,\qt* \q2 \qt is adhibitus est ad caput angulī,\qt* \q1 \qt id quod ā Dominō profectum est,\qt* \q2 \qt et nōbīs mīrum vidētur.’\qt*`
   **Apply:** `Matt.21.43` la: `\v 43 Quamobrem` → `\m \v 43 Quamobrem`
5. **Matt 22:44** Ps 110:1 (after group 1, item 3); then `\m` for 22:45.
   **Apply:** `Matt.22.44` la: `\v 44 ‘Ait Dominus Dominō meō: “Sēde ad meam dexteram, dōnec tuōs hostēs effēcerō scabellum pedum tuōrum”’?` → `\q1 \v 44 \qt “‘Ait Dominus Dominō meō:\qt* \q2 \qt “Sēde ad meam dexteram,\qt* \q1 \qt dōnec tuōs hostēs effēcerō\qt* \q2 \qt scabellum pedum tuōrum”’?\qt*`
   **Apply:** `Matt.22.45` la: `\v 45 Quod sī` → `\m \v 45 Quod sī`
6. **Matt 24:29** Isa 13:10; 34:4; then `\m` for 24:30.
   **Apply:** `Matt.24.29` la: `‘Sōl obscūrābitur, neque lūna suum splendōrem ēmittet, et stēllæ dē cælō cadent, cælīque potestātēs concutientur.’` → `\q1 \qt “‘Sōl obscūrābitur,\qt* \q2 \qt neque lūna suum splendōrem ēmittet,\qt* \q1 \qt et stēllæ dē cælō cadent,\qt* \q2 \qt cælīque potestātēs concutientur.’\qt*`
   **Apply:** `Matt.24.30` la: `\v 30 Ac tum` → `\m \v 30 Ac tum`
7. **Matt 26:31** Zech 13:7; then `\m` for 26:32.
   **Apply:** `Matt.26.31` la: `‘Percutiam pāstōrem et dispergentur ovēs gregis.’` → `\q1 \qt “‘Percutiam pāstōrem\qt* \q2 \qt et dispergentur ovēs gregis.’\qt*`
   **Apply:** `Matt.26.32` la: `\v 32 Sed postquam` → `\m \v 32 Sed postquam`
8. **Matt 27:9–10** Zech 11:12–13 (Jer 32:6–9), the narrator's quotation in “…”.
   **Apply:** `Matt.27.9` la: `“Itaque sūmpsērunt trīgintā argenteōs, pretium æstimātī, quem licitātī ēmērunt ab Isrāēlītīs,` → `\q1 \qt “Itaque sūmpsērunt trīgintā argenteōs,\qt* \q2 \qt pretium æstimātī, quem licitātī ēmērunt ab Isrāēlītīs,\qt*`
   **Apply:** `Matt.27.10` la: `\v 10 eōsque impendērunt in agrum figulī, quemadmodum mihi præcēpit Dominus.”` → `\q1 \v 10 \qt eōsque impendērunt in agrum figulī,\qt* \q2 \qt quemadmodum mihi præcēpit Dominus.”\qt*`

## 5. Paragraphs (3, your call)

The draft opens a paragraph at 73 of the BSB's 76 paragraph starts in these chapters, and at 21 more of its
own (your habit: settled Matthew has twice the BSB's paragraphs). The BSB has three the draft lacks. Add them,
as your settled chapters would suggest (75 of 76), or keep the draft's?

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 17:19** the disciples ask privately why they could not cast it out (BSB new paragraph).
   **Apply:** `Matt.17.19` la: `\v 19 Tum aggressī` → `\p \v 19 Tum aggressī`
2. **Matt 18:19** “Again I tell you …” (BSB new paragraph; the speech continues, so it reopens with “).
   **Apply:** `Matt.18.19` la: `\v 19 Item certō scītōte` → `\p \v 19 “Item certō scītōte`
3. **Matt 24:26** “So if they say to you …” (BSB new paragraph; the speech continues, so it reopens with “).
   **Apply:** `Matt.24.26` la: `\v 26 Sī igitur` → `\p \v 26 “Sī igitur`
