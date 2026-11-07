# Quotation marks: reported speech in the settled chapters

Proposed 2026-11-06 under decision 4: “…” for direct speech, ‘…’ only for quotations within it, and reported
discourse unmarked. All 167 passages in ‘…’ in `text/*.usfm` were read. **80 are reported speech** (an accusative
and infinitive, or an indirect question or command in the subjunctive: *‘eum esse īnsānum’*, *‘quid Jēsū
facerent’*, *‘ut paulum ā terrā summovēret’*) and lose their marks here. The other 87 are direct words inside a
speech or a quotation of scripture and keep theirs, including two that mix direct and reported words (Matt 5:21
*‘Nē occīditō, quod … eum tenērī jūdiciō’*, Luke 10:11) and Matt 12:10 *‘an Sabbatīs sānāre licet?’* (indicative,
so direct). Decision 4's estimate of about 33 counted only part of them.

Each **Apply** line is an exact replacement inside that verse of `text/<BOOK>.usfm`, checked to match once. Where
a passage runs over a line or a verse, its opening and closing marks are removed by two lines.

## A. Reported statements and commands: marks removed (70)

**Decision:** accept (Nathan, 2026-11-07)  
**Applied:** 2026-11-07, to `text/*.usfm`

1. **Apply:** `Gen.24.54` la: `‘ut ad dominum remittātur.’` → `ut ad dominum remittātur.`
2. **Apply:** `Gen.24.55` la: `‘profectūrum, postquam ea cum ipsīs diēs circiter decem mānsisset.’` → `profectūrum, postquam ea cum ipsīs diēs circiter decem mānsisset.`
3. **Apply:** `Gen.24.56` la: `‘nē sē remorentur, dēbēre sē, dum ab Jōvā id sibi iter secundātur, dīmittī et ad dominum redīre.’` → `nē sē remorentur, dēbēre sē, dum ab Jōvā id sibi iter secundātur, dīmittī et ad dominum redīre.`
4. **Apply:** `Gen.24.58` la: `‘vērō, velle,’` → `vērō, velle,`
5. **Apply:** `Gen.24.65` la: `‘dominum suum esse’` → `dominum suum esse`
6. **Apply:** `Gen.26.7` la: `‘sorōrem esse,’` → `sorōrem esse,`
7. **Apply:** `Gen.26.7` la: `‘uxōrem esse’` → `uxōrem esse`
8. **Apply:** `Gen.26.11` la: `‘nē quis hominem, aut ejus conjugem tangeret, et id sub pœnā capitis.’` → `nē quis hominem, aut ejus conjugem tangeret, et id sub pœnā capitis.`
9. **Apply:** `Gen.26.16` la: `‘ab iīs discēdere, quod esset longē iīs potentior.’` → `ab iīs discēdere, quod esset longē iīs potentior.`
10. **Apply:** `Gen.26.20` la: `‘suam esse aquam,’` → `suam esse aquam,`
11. **Apply:** `Gen.26.32` la: `‘sēsē aquam invēnisse,’` → `sēsē aquam invēnisse,`
12. **Apply:** `Gen.27.6` la: `‘petere ferīnam,` → `petere ferīnam,`
   **Apply:** `Gen.27.7` la: `dare comedendum,’` → `dare comedendum,`
13. **Apply:** `Gen.27.31` la: `‘ut assurgeret et fīliī ferīnā vescerētur, ut eī bene precārētur.’` → `ut assurgeret et fīliī ferīnā vescerētur, ut eī bene precārētur.`
14. **Apply:** `Gen.27.46` la: `‘sē Hettæārum` → `sē Hettæārum`
   **Apply:** `Gen.27.46` la: `esse vellet.’` → `esse vellet.`
15. **Apply:** `Matt.9.3` la: `‘eum impiē loquī.’` → `eum impiē loquī.`
16. **Apply:** `Matt.9.11` la: `‘cūr cum pūblicānīs et improbīs cibum caperet eōrum magister.’` → `cūr cum pūblicānīs et improbīs cibum caperet eōrum magister.`
17. **Apply:** `Matt.9.33` la: `‘umquam tālia apud Isrāēlītās fuisse vīsa.’` → `umquam tālia apud Isrāēlītās fuisse vīsa.`
18. **Apply:** `Matt.9.34` la: `‘eum per dæmoniōrum prīncipem ējicere dæmonia.’` → `eum per dæmoniōrum prīncipem ējicere dæmonia.`
19. **Apply:** `Matt.10.7` la: `‘īnstāre cæleste rēgnum.’` → `īnstāre cæleste rēgnum.`
20. **Apply:** `Matt.11.18` la: `‘eum’` → `eum`
21. **Apply:** `Matt.11.18` la: `‘esse furiōsum.’` → `esse furiōsum.`
22. **Apply:** `Matt.11.19` la: `‘eum’` → `eum`
23. **Apply:** `Matt.11.19` la: `‘hominem esse vorācem, vīnōsum, pūblicānōrum, et improbōrum amīcum.’` → `hominem esse vorācem, vīnōsum, pūblicānōrum, et improbōrum amīcum.`
24. **Apply:** `Matt.12.24` la: `‘eum nōn nisi per Beelzebūlem dæmoniōrum prīncipem ējicere dæmonia.’` → `eum nōn nisi per Beelzebūlem dæmoniōrum prīncipem ējicere dæmonia.`
25. **Apply:** `Mark.1.15` la: `‘complētum esse tempus, et īnstāre Deī rēgnum, corrigerent sē, et ēvangeliō crēderent.’` → `complētum esse tempus, et īnstāre Deī rēgnum, corrigerent sē, et ēvangeliō crēderent.`
26. **Apply:** `Mark.1.34` la: `‘sē scīre eum esse Chrīstum.’` → `sē scīre eum esse Chrīstum.`
27. **Apply:** `Mark.1.37` la: `‘eum ab omnibus conquīrī.’` → `eum ab omnibus conquīrī.`
28. **Apply:** `Mark.2.12` la: `‘sēsē nihil umquam tāle vīdisse’` → `sēsē nihil umquam tāle vīdisse`
29. **Apply:** `Mark.3.21` la: `‘eum esse īnsānum.’` → `eum esse īnsānum.`
30. **Apply:** `Mark.3.30` la: `‘eum immundum habēre spīritum.’` → `eum immundum habēre spīritum.`
31. **Apply:** `Mark.5.9` la: `‘quod eī nōmen esset.’` → `quod eī nōmen esset.`
32. **Apply:** `Mark.5.23` la: `‘fīliolam suam in extrēmō esse perīculō; venīret, eīque manūs impōneret ut servārētur, ac revalēsceret.’` → `fīliolam suam in extrēmō esse perīculō; venīret, eīque manūs impōneret ut servārētur, ac revalēsceret.`
33. **Apply:** `Luke.1.63` la: `‘ejus nōmen esse Jōhannem,’` → `ejus nōmen esse Jōhannem,`
34. **Apply:** `Luke.2.23` la: `‘scīlicet omnem marem, quī vulvam aperuisset, Dominō sacrum esse dīcendum’` → `scīlicet omnem marem, quī vulvam aperuisset, Dominō sacrum esse dīcendum`
35. **Apply:** `Luke.4.4` la: `‘nōn sōlō pāne vīvere hominem, sed etiam eō omnī quod ex ōre Deī proficīscitur.’` → `nōn sōlō pāne vīvere hominem, sed etiam eō omnī quod ex ōre Deī proficīscitur.`
36. **Apply:** `Luke.4.21` la: `‘id scrīptum hodiē esse audientibus iīs comprobātum.’` → `id scrīptum hodiē esse audientibus iīs comprobātum.`
37. **Apply:** `Luke.4.41` la: `‘sē scīre eum esse Chrīstum.’` → `sē scīre eum esse Chrīstum.`
38. **Apply:** `Luke.4.43` la: `‘oportēre sē aliīs quoque cīvitātibus nūntiāre Deī rēgnum, ad id enim sē esse missum.’` → `oportēre sē aliīs quoque cīvitātibus nūntiāre Deī rēgnum, ad id enim sē esse missum.`
39. **Apply:** `Luke.5.3` la: `‘ut paulum ā terrā summovēret,’` → `ut paulum ā terrā summovēret,`
40. **Apply:** `Luke.5.4` la: `‘ut in altum subdūceret, utque sua rētia laxārent ad prædam.’` → `ut in altum subdūceret, utque sua rētia laxārent ad prædam.`
41. **Apply:** `Luke.5.26` la: `‘sēsē hodiē incrēdibilia vīdisse.’` → `sēsē hodiē incrēdibilia vīdisse.`
42. **Apply:** `Luke.5.39` la: `‘vetus esse melius.’` → `vetus esse melius.`
43. **Apply:** `Luke.6.11` la: `‘quid Jēsū facerent.’` → `quid Jēsū facerent.`
44. **Apply:** `Luke.7.16` la: `‘magnum apud ipsōs ortum esse vātem, Deumque suōrum cūram habēre.’` → `magnum apud ipsōs ortum esse vātem, Deumque suōrum cūram habēre.`
45. **Apply:** `Luke.7.33` la: `‘eum habēre dæmonium.’` → `eum habēre dæmonium.`
46. **Apply:** `Luke.7.34` la: `‘hominem esse edācem, vīnōsumque, et pūblicānōrum ac improbōrum amīcum.’` → `hominem esse edācem, vīnōsumque, et pūblicānōrum ac improbōrum amīcum.`
47. **Apply:** `Luke.8.52` la: `‘nōn enim mortuam esse, sē dormīre.’` → `nōn enim mortuam esse, sē dormīre.`
48. **Apply:** `Luke.9.22` la: `‘oportēre Fīlium` → `oportēre Fīlium`
   **Apply:** `Luke.9.22` la: `diē resurgere.’` → `diē resurgere.`
49. **Apply:** `Luke.10.9` la: `‘ad eōs Deī rēgnum vēnisse’` → `ad eōs Deī rēgnum vēnisse`
50. **Apply:** `Luke.10.35` la: `‘sēsē quidquid ille īnsuper īnsūmpsisset, eī in suō reditū esse solūtūrum.’` → `sēsē quidquid ille īnsuper īnsūmpsisset, eī in suō reditū esse solūtūrum.`
51. **Apply:** `Luke.12.54` la: `‘adventāre pluviam,’` → `adventāre pluviam,`
52. **Apply:** `Luke.12.55` la: `‘æstum futūrum,’` → `æstum futūrum,`
53. **Apply:** `Luke.13.32` la: `‘mē dæmonia` → `mē dæmonia`
   **Apply:** `Luke.13.33` la: `Hierosolymam perīre.’` → `Hierosolymam perīre.`
54. **Apply:** `John.1.20` la: `‘sē nōn esse Chrīstum.’` → `sē nōn esse Chrīstum.`
55. **Apply:** `John.2.5` la: `‘quod ille iīs jussisset, facerent.’` → `quod ille iīs jussisset, facerent.`
56. **Apply:** `John.2.7` la: `‘Ea solia ut aquā replērent,’` → `Ea solia ut aquā replērent,`
57. **Apply:** `John.2.8` la: `‘nunc haurīrent, et convīviī magistrō ferrent.’` → `nunc haurīrent, et convīviī magistrō ferrent.`
58. **Apply:** `John.3.7` la: `‘vōbīs esse renāscendum.’` → `vōbīs esse renāscendum.`
59. **Apply:** `John.3.28` la: `‘nōn esse mē Chrīstum, sed eī præmissum.’` → `nōn esse mē Chrīstum, sed eī præmissum.`
60. **Apply:** `John.4.27` la: `‘quid quæreret’` → `quid quæreret`
61. **Apply:** `John.4.27` la: `‘quid cum eā loquerētur’` → `quid cum eā loquerētur`
62. **Apply:** `John.4.29` la: `‘ut hominem vīserent, quī sibi omnia facta sua dīxisset; fortasse eum esse Chrīstum.’` → `ut hominem vīserent, quī sibi omnia facta sua dīxisset; fortasse eum esse Chrīstum.`
63. **Apply:** `John.4.33` la: `‘num quis eī cibum attulisset,’` → `num quis eī cibum attulisset,`
64. **Apply:** `John.4.35` la: `‘hinc ad quattuor mēnsēs futūram esse messem.’` → `hinc ad quattuor mēnsēs futūram esse messem.`
65. **Apply:** `John.4.39` la: `‘eum sibi quidquid ipsa fēcisset dīxisse.’` → `eum sibi quidquid ipsa fēcisset dīxisse.`
66. **Apply:** `John.4.42` la: `‘nōn sē` → `nōn sē`
   **Apply:** `John.4.42` la: `esse Chrīstum.’` → `esse Chrīstum.`
67. **Apply:** `John.4.51` la: `‘ejus puerum vīvere.’` → `ejus puerum vīvere.`
68. **Apply:** `John.4.52` la: `‘quā hōrā melius habuisset,’` → `quā hōrā melius habuisset,`
69. **Apply:** `John.4.52` la: `‘prīdiē hōrā septimā līberātum fuisse febre.’` → `prīdiē hōrā septimā līberātum fuisse febre.`
70. **Apply:** `John.4.53` la: `‘ejus fīlium vīvere,’` → `ejus fīlium vīvere,`

## B. Indirect questions: marks removed, and the question mark with them (10)

Unquoted, an indirect question takes no question mark in Latin (*rogāvit quidnam esset*). The final *?*
becomes a full stop where the sentence ends, and is dropped where it runs on; in Mark 1:27 the three questions
are joined by commas.

**Decision:** accept (Nathan, 2026-11-07)  
**Applied:** 2026-11-07, to `text/*.usfm`

1. **Apply:** `Gen.24.47` la: `‘cujus esset fīlia?’` → `cujus esset fīlia`
2. **Apply:** `Gen.24.58` la: `‘velitne cum homine discēdere?’` → `velitne cum homine discēdere.`
3. **Apply:** `Gen.24.65` la: `‘quisnam vir ille sit, quī per agrum adversum ipsōs tendat?’` → `quisnam vir ille sit, quī per agrum adversum ipsōs tendat.`
4. **Apply:** `Gen.26.27` la: `‘cūr ad sē accēderent, quem præ odiō ex suō cōnsortiō expulissent?’` → `cūr ad sē accēderent, quem præ odiō ex suō cōnsortiō expulissent`
5. **Apply:** `Mark.1.27` la: `‘quidnam id esset? quænam ea foret nova doctrīna? quod per potestātem etiam impūrīs spīritibus imperāret, iīque eī pārērent.’` → `quidnam id esset, quænam ea foret nova doctrīna, quod per potestātem etiam impūrīs spīritibus imperāret, iīque eī pārērent.`
6. **Apply:** `Mark.2.16` la: `‘quī fieret ut cum pūblicānīs et improbīs cibum pōtiōnemque sūmeret?’` → `quī fieret ut cum pūblicānīs et improbīs cibum pōtiōnemque sūmeret.`
7. **Apply:** `Luke.1.66` la: `‘quidnam futūrus esset ille puer?’` → `quidnam futūrus esset ille puer.`
8. **Apply:** `Luke.7.49` la: `‘quisnam is esset, quī etiam peccāta ignōsceret?’` → `quisnam is esset, quī etiam peccāta ignōsceret.`
9. **Apply:** `Luke.8.9` la: `‘quænam esset ea similitūdō?’` → `quænam esset ea similitūdō.`
10. **Apply:** `Luke.8.30` la: `‘quodnam eī nōmen esset?’` → `quodnam eī nōmen esset.`

## C. Quotation-mark slips (2)

Luke 12:18 starts a new paragraph inside Jesus' parable, so both open quotations are reopened (“‘); the ‘ for
the rich man's words is missing, though its ’ follows (*Hoc agam,’ inquit*). Gen 24:47 opens the answer with a
closing mark (*respondit: ’Bathūēlis*).

**Decision:** accept (Nathan, 2026-11-07)  
**Applied:** 2026-11-07, to `text/*.usfm`

1. **Apply:** `Luke.12.18` la: `“Hoc agam,’` → `“‘Hoc agam,’`
2. **Apply:** `Gen.24.47` la: `respondit: ’Bathūēlis` → `respondit: ‘Bathūēlis`
