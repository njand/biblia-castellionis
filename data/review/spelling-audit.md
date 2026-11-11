# Spellings the rules missed: an audit of the settled chapters

Done 2026-11-11 after *quum* (decision 41), at Nathan's question whether other normalizations were overlooked when
the pipeline drafted the new chapters. Method: every word of the settled text (`text/*.usfm`) counted in the
chapters from the earlier manual work (Matt 1–13, Mark 1–5, Luke 1–13, John 1–4, Gen 1–27) and in the chapters the
pipeline drafted (the rest), then (1) a list of early modern spellings checked against both and Gaffiot 2016
(`python -m pipeline latin macron`), and (2) every approved word rule in `data/rules/orthography.tsv` tried on the
other forms of its word.

## Why they were missed

The approved spelling rules are almost all **word** rules: they change the exact forms they were learned from
(*sobole* → *subole*, *sobolis* → *subolis*, *mulctabimini* → *multabimini*), so a form not seen before
(*sobolem*, *mulctārī*) passes untouched. And a spelling that never differed between Wikisource and the settled
text of the time (*quum*, *quotīdiē*) never became a rule at all. Fixed for the drafts to come: the pipeline now
takes **stem** rules (`scope` `stem`: a word beginning with `old` takes `new` in its place; a word rule wins, the
longest stem wins; `normalize.WordRules`). The stem rules below are added to `orthography.tsv` as `proposed`; each
becomes `approved` with its group's decision.

Not proposed, after checking: *sōlātiō* (Gaffiot headword), *existimō*
(another verb than *exsistō*), *exsiliēns* (*exsiliō*, leap), *sumptus*, *percontor*, *opportūnus*, *hæreō*
(Gaffiot's spellings), *Paullō* (Acts 13:7, the proconsul Sergius Paulus: a name, left for you), *herī* (yesterday,
Gen 31:29, 31:42, Acts 7:28), *Hēr* (Luke 3:28) and *Obēd* (Luke 3:32), names. The *-īv-* perfects left in
*petīvissem* (Gen 24:45), *quæsīvissēs* (Gen 44:19), *audīverītis* (Luke 7:22), *audīverīmus* (Luke 22:71),
*petīveris* (John 11:22), *quæsīvisse* (John 21:17), *audīverim* (Acts 22:7) and *præteriisset* (Acts 27:9) are
decision 19's (form by form), not listed here; say if you want them proposed.

## The evidence, and how the groups were resolved

Nathan, 2026-11-11: resolve the groups "based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden
Age spelling)". The counts are `python -m pipeline latin attest` (the Latin Library, Erasmus, the colloquia: the
spelling of the editions there, not of the manuscripts). Its era labels proved unreliable (Gregory IX's decretals
count as "golden"), so the authors decide: hits in Cicero first, then the other Golden Age and early Silver
authors (Caesar, Sallust, Livy, Varro; Seneca, Quintilian, Tacitus), and Plautus and Terence where the word is
theirs. Every group follows Gaffiot and the classical authors; one is a judgment against Cicero's editions
(*quidquam*, below).

| Spelling kept | Its rival | Corpus (hits; the classical authors) | Gaffiot 2016 |
|---|---|---|---|
| *cōntiō* | *conciō* | *contione* 446 (Cicero 109) / *concione* 47 (Cicero 8); *contionem* 271 (Cicero 55) / 31 (Cicero 4) | *cōntiō* |
| *condiciō* | *conditiō* | *condicione* 1478 (Cicero 99) / *conditione* 253 (Cicero 0); *condicionem* 662 / 151 | *condiciō* |
| *subolēs* | *sobolēs* | *suboles* 80 (Cicero 5) / 47; *subolem* 67 / 60 | *subolēs* |
| *multō* | *mulctō* | *multavit* 33 (Cicero 4) / 4; few hits otherwise | *multō* |
| *pænit-* | *pœnit-* | *paenitet* 139 (Cicero 20) / *poenitet* 60 (Cicero 0); *paenitentia* 188 (Quintilian, Seneca, Tacitus) / *poenitentia* 153 (Gregory IX 82, Melanchthon …) | *pænitet*, *pænitentia* |
| *erus* | *herus* | *erus* 117 (Plautus 102, Terence, Horace, Varro; and Castellio himself 4) / *herus* 46 (Erasmus 19, Vives …) | both; *erus* |
| *paulō*, *paulīsper*, *paululum* | *paull-* | *paulo* 2203 (Cicero 313) / *paullo* 88 (Cicero 44); *paulisper* 418 / 7; *paululum* 382 / 14 | *paulō*, *paulīsper* |
| *quidquam* | *quicquam* | *quidquam* 396 (Cicero 65) / ***quicquam* 2197 (Cicero 376, Livy 201)** | *quisquam*, neuter *quidquam* |
| *umquam* | *unquam* | *umquam* 2118 (Cicero 691) / *unquam* 975 (Cicero 0) | *umquam* |
| *cāritās* | *chāritās* | *caritate* 411 (Cicero 44) / *charitate* 93 (Cicero 0) | *cāritās* |
| *sepulcrum* | *sepulchrum* | *sepulcrum* 238 (Cicero 19) / 209 (Cicero 0); *sepulcra* 90 / 70 | *sepulcrum* |
| *exspect-* | *expect-* | *exspectare* 210 (Cicero 66) / 147 (Cicero 0); *exspectatio* 82 (Cicero 45) / 51 (Cicero 4) | *exspectō* |
| *undecumque* | *undecunque* | *undecumque* 101 (Seneca, Quintilian) / 44 (William of Tyre 16 …); likewise *quicumque* 1039 (Cicero 52) / 159, *ubicumque* 394 (Cicero 19) / 57 | *undecumque* |
| *mæstus* | *mœstus* | *maestus* 95 / 9; *maesti* 73 / 3 | *mæstus* |
| *vīcēsimus* | *vīgēsimus* | *vicesimus* 28 (Cicero 2) / 8; *vicesimo* 151 / 40 | both |
| *sescentī* | *sexcentī* | *sescenta* 44 (Cicero 15) / 27 (Cicero 0); *sescentos* 49 (Cicero 4) / 25 | *sexcentī* (the corpus decides, as the approved *sescentos*) |
| *inaspectābilis* | *inadspectābilis* | no hits either way (a Christian word) | — (decision 37's *ad-* assimilation) |
| *cotīdiē* | *quotīdiē*, *cottīdiē* | *cotidie* 738 (Cicero 145) / *quotidie* 360 (Cicero 57) / *cottidie* 139 (Cicero 7); *cotidianus* 11 / 13 / 3 | *cottīdiē* and *quotīdiē* |
| *cærimōnia* | *cæremōnia*, *cēremōnia* | *caerimonias* 65 (Cicero 11) / *caeremonias* 7 / *ceremonias* 19 (Cicero 0) | *cærimōnia* |
| *quotiēns* | *quotiēs* | *quotiens* 1376 / *quoties* 675 (neo-Latin 452); *totiens* 519 (Cicero 44) / *toties* 201 (Cicero 0) | *quotiēns* |
| *obœdiō* | *obēdiō* | *oboedire* 74 (Cicero 5, Sallust; Codex of Justinian) / *obedire* 95 (Gregory IX 27, Gregory VII, William of Tyre …); *oboedientia* 45 / 74 (all medieval) | *obœdiō* |
| *adulēscēns* | *adolēscēns* | see F | *adulēscēns* |

***quidquam*, the one judgment.** Cicero's editions here print *quicquam* (376) far more than *quidquam* (65), and
*quicquid* (172) more than *quidquid* (fewer than 74), as Quintilian does (89 to 74), while Seneca (320) and the Digest (198) print *quidquid*. Gaffiot heads the
*d* forms, and the brief chose *quidquid* (not *quicquid*), an approved rule. Since *quidquam* and *quidquid* are the
same question, *quidquam* is kept with the brief. To follow Cicero's editions instead, both would turn to *c*: say
so, and it becomes a new proposal.

## A. Spellings already decided (the brief, or approved rules for other forms of the word) — 56 places

*contiō* (brief; *concionaretur* → *contionaretur* approved), *subolēs* (brief), *multō* (brief), *condiciō* (brief;
all eight are the noun "condition, terms", none *conditiō* "seasoning"), *pænit-* (5× already, Gen, Matt, Luke),
*erus* (*herum* → *erum* approved; Luke 12:46 *erus*), *paulō*, *paulīsper*, *paululum* (Gaffiot), *quidquam* (as
*quidquid*), *umquam* (19× already), *cāritās* (21× already), *sepulcrum* (Gaffiot; 12× already), *exspectātiō*
(30× *exspect-* already), *undecumque*, *mæstus*, *vīcēsimus* (*vigesimo* → *vicesimo* approved), *inaspectābilis*
(the *ad-* assimilation of decision 37), *sescentī* (*sexcentos* → *sescentos* approved). Stem rules: *concion* →
*contion*, *sobol* → *subol*, *mulct* → *mult*, *conditio* → *condicio*, *pœnit* → *pænit*, *paull* → *paul*,
*charit* → *carit*, *sepulchr* → *sepulcr*, *expect* → *exspect*, *mœst* → *mæst*, *vigesim* → *vicesim*,
*inadspect* → *inaspect*, *sexcent* → *sescent*; word rules *herus* → *erus*, *quicquam* → *quidquam*, *unquam* →
*umquam*, *undecunque* → *undecumque*.

**Decision:** accept all (Nathan, 2026-11-11: "resolve … based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden Age spelling)"; resolved by Claude, see the evidence table)

1. *cōnciōne* → *cōntiōne*
   **Apply:** `Acts.14.27` la: `cōnciōne,` → `cōntiōne,`
2. *cōnciōne* → *cōntiōne*
   **Apply:** `Acts.19.39` la: `cōnciōne` → `cōntiōne`
3. *cōnciōnem* → *cōntiōnem*
   **Apply:** `Acts.19.41` la: `cōnciōnem` → `cōntiōnem`
4. *cōnciōnem* → *cōntiōnem*
   **Apply:** `1Cor.11.18` la: `cōnciōnem,` → `cōntiōnem,`
5. *cōnciōnem* → *cōntiōnem*
   **Apply:** `1Cor.11.22` la: `cōnciōnem` → `cōntiōnem`
6. *cōnciōnī* → *cōntiōnī*
   **Apply:** `1Cor.14.4` la: `cōnciōnī` → `cōntiōnī`
7. *cōnciōnī* → *cōntiōnī*
   **Apply:** `1Cor.14.12` la: `cōnciōnī.` → `cōntiōnī.`
8. *cōnciōne* → *cōntiōne*
   **Apply:** `1Cor.14.19` la: `cōnciōne` → `cōntiōne`
9. *cōnciōne* → *cōntiōne*
   **Apply:** `1Cor.14.28` la: `cōnciōne,` → `cōntiōne,`
10. *cōnciōnibus* → *cōntiōnibus*
   **Apply:** `1Cor.14.33` la: `cōnciōnibus.` → `cōntiōnibus.`
11. *cōnciōnibus* → *cōntiōnibus*
   **Apply:** `1Cor.14.34` la: `cōnciōnibus` → `cōntiōnibus`
12. *cōnciōne* → *cōntiōne*
   **Apply:** `1Cor.14.35` la: `cōnciōne` → `cōntiōne`
13. *sobolem* → *subolem*
   **Apply:** `Gen.32.12` la: `sobolem` → `subolem`
14. *sobolēs* → *subolēs*
   **Apply:** `Gen.36.9` la: `sobolēs` → `subolēs`
15. *mulctārī* → *multārī*
   **Apply:** `Exod.5.16` la: `mulctārī.` → `multārī.`
16. *conditiōne* → *condiciōne*
   **Apply:** `Gen.31.40` la: `conditiōne,` → `condiciōne,`
17. *conditiōne* → *condiciōne*
   **Apply:** `Gen.34.15` la: `conditiōne` → `condiciōne`
18. *conditiōnem* → *condiciōnem*
   **Apply:** `Gen.42.20` la: `conditiōnem` → `condiciōnem`
19. *conditiō* → *condiciō*
   **Apply:** `Gen.47.3` la: `conditiō,` → `condiciō,`
20. *conditiōne* → *condiciōne*
   **Apply:** `Gen.47.24` la: `conditiōne,` → `condiciōne,`
21. *conditiōne* → *condiciōne*
   **Apply:** `Exod.3.16` la: `conditiōne,` → `condiciōne,`
22. *conditiōne* → *condiciōne*
   **Apply:** `Exod.12.48` la: `conditiōne,` → `condiciōne,`
23. *conditiōne* → *condiciōne*
   **Apply:** `1Cor.7.24` la: `conditiōne` → `condiciōne`
24. *pœnitentiæ* → *pænitentiæ*
   **Apply:** `Acts.13.24` la: `pœnitentiæ` → `pænitentiæ`
25. *pœniteat* → *pæniteat*
   **Apply:** `2Cor.7.8` la: `pœniteat,` → `pæniteat,`
26. *pœnituisset* → *pænituisset*
   **Apply:** `2Cor.7.8` la: `pœnituisset.` → `pænituisset.`
27. *pœnitendam* → *pænitendam*
   **Apply:** `2Cor.7.10` la: `pœnitendam` → `pænitendam`
28. *herus* → *erus*
   **Apply:** `Gen.39.3` la: `herus,` → `erus,`
29. *herus* → *erus*
   **Apply:** `Gen.39.8` la: `herus` → `erus`
30. *herus* → *erus*
   **Apply:** `Gen.39.19` la: `herus,` → `erus,`
31. *herus* → *erus*
   **Apply:** `Gen.44.6` la: `herus` → `erus`
32. *paullisper* → *paulīsper*
   **Apply:** `Acts.5.34` la: `paullisper` → `paulīsper`
33. *paullō* → *paulō*
   **Apply:** `Acts.17.22` la: `paullō` → `paulō`
34. *paullulum* → *paululum*
   **Apply:** `Acts.27.28` la: `paullulum` → `paululum`
35. *quicquam* → *quidquam*
   **Apply:** `Exod.5.8` la: `quicquam` → `quidquam`
36. *quicquam* → *quidquam*
   **Apply:** `Exod.7.18` la: `quicquam` → `quidquam`
37. *unquam* → *umquam*
   **Apply:** `Exod.10.14` la: `unquam` → `umquam`
38. *unquam* → *umquam*
   **Apply:** `Exod.11.6` la: `unquam` → `umquam`
39. *chāritās* → *cāritās*
   **Apply:** `Matt.24.12` la: `chāritās.` → `cāritās.`
40. *chāritāte* → *cāritāte*
   **Apply:** `John.15.13` la: `chāritāte` → `cāritāte`
41. *sepulchra* → *sepulcra*
   **Apply:** `Exod.14.11` la: `sepulchra` → `sepulcra`
42. *sepulchrīs* → *sepulcrīs*
   **Apply:** `Matt.23.27` la: `sepulchrīs,` → `sepulcrīs,`
43. *sepulchra* → *sepulcra*
   **Apply:** `Matt.23.29` la: `sepulchra` → `sepulcra`
44. *sepulchrī* → *sepulcrī*
   **Apply:** `Matt.27.61` la: `sepulchrī` → `sepulcrī`
45. *sepulchrum* → *sepulcrum*
   **Apply:** `Matt.27.64` la: `sepulchrum` → `sepulcrum`
46. *sepulchrum* → *sepulcrum*
   **Apply:** `Matt.27.66` la: `sepulchrum` → `sepulcrum`
47. *sepulchrum* → *sepulcrum*
   **Apply:** `Matt.28.1` la: `sepulchrum.` → `sepulcrum.`
48. *sepulchra* → *sepulcra*
   **Apply:** `Luke.11.44` la: `sepulchra,` → `sepulcra,`
49. *expectātiōne* → *exspectātiōne*
   **Apply:** `Luke.21.26` la: `expectātiōne,` → `exspectātiōne,`
50. *undecunque* → *undecumque*
   **Apply:** `Exod.5.11` la: `undecunque` → `undecumque`
51. *mœstōs* → *mæstōs*
   **Apply:** `Gen.40.6` la: `mœstōs` → `mæstōs`
52. *mœstō* → *mæstō*
   **Apply:** `Gen.40.7` la: `mœstō.` → `mæstō.`
53. *vīgēsimī* → *vīcēsimī*
   **Apply:** `Exod.12.18` la: `vīgēsimī` → `vīcēsimī`
54. *inadspectābilia* → *inaspectābilia*
   **Apply:** `Rom.1.20` la: `inadspectābilia,` → `inaspectābilia,`
55. *sexcenta* → *sescenta*
   **Apply:** `Exod.12.37` la: `sexcenta` → `sescenta`
56. *sexcentīs* → *sescentīs*
   **Apply:** `Exod.14.7` la: `sexcentīs` → `sescentīs`

## B. *cotīdiē*, not *quotīdiē* — 13 places

The Gospels write *cotīdiē* 8× (Matt 26:55, Luke 9:23, 11:3 …), the drafted chapters *quotīdiē* 13× (Exod 5:19, Acts, Rom, 1–2 Cor).
Gaffiot 2016 has both as headwords (*cottīdiē* first, *quŏtīdĭē* beside it). Recommended: *cotīdiē*, as the Gospels.
Stem rule *quotidi* → *cotidi*.

**Decision:** accept all (Nathan, 2026-11-11: "resolve … based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden Age spelling)"; resolved by Claude, see the evidence table)

57. *quotīdiānō* → *cotīdiānō*
   **Apply:** `Exod.5.19` la: `quotīdiānō` → `cotīdiānō`
58. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.2.46` la: `quotīdiē` → `cotīdiē`
59. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.2.47` la: `quotīdiē` → `cotīdiē`
60. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.3.2` la: `quotīdiē` → `cotīdiē`
61. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.5.42` la: `quotīdiē` → `cotīdiē`
62. *quotīdiānō* → *cotīdiānō*
   **Apply:** `Acts.6.1` la: `quotīdiānō` → `cotīdiānō`
63. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.16.5` la: `quotīdiē.` → `cotīdiē.`
64. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.17.11` la: `quotīdiē` → `cotīdiē`
65. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.17.17` la: `quotīdiē,` → `cotīdiē,`
66. *quotīdiē* → *cotīdiē*
   **Apply:** `Acts.19.9` la: `quotīdiē` → `cotīdiē`
67. *quotīdiē* → *cotīdiē*
   **Apply:** `Rom.8.36` la: `quotīdiē,\qt*` → `cotīdiē,\qt*`
68. *Quotīdiē* → *Cotīdiē*
   **Apply:** `1Cor.15.31` la: `Quotīdiē` → `Cotīdiē`
69. *quotīdiāna* → *cotīdiāna*
   **Apply:** `2Cor.11.28` la: `quotīdiāna` → `cotīdiāna`

## C. *cærimōnia*, not *cēremōnia* — 3 places (Exod 12–13)

Gaffiot 2016: *cærĭmōnĭa* only. Stem rules *ceremoni*, *cerimoni*, *cæremoni* → *cærimoni*.

**Decision:** accept all (Nathan, 2026-11-11: "resolve … based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden Age spelling)"; resolved by Claude, see the evidence table)

70. *cēremōniam* → *cærimōniam*
   **Apply:** `Exod.12.25` la: `cēremōniam` → `cærimōniam`
71. *cēremōnia* → *cærimōnia*
   **Apply:** `Exod.12.26` la: `cēremōnia,` → `cærimōnia,`
72. *cērimōniam* → *cærimōniam*
   **Apply:** `Exod.13.10` la: `cērimōniam` → `cærimōniam`

## D. *quotiēns*, not *quotiēs* — 6 places

The edition writes *quotiēs* everywhere (Gen 30:41, Matt 18:21, 23:37, Luke 13:34, 1 Cor 11:25–26). Gaffiot 2016
heads only *quŏtĭēns*. Recommended: *quotiēns* (and *totiēns* when it comes). Word rule *quoties* → *quotiens*.

**Decision:** accept all (Nathan, 2026-11-11: "resolve … based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden Age spelling)"; resolved by Claude, see the evidence table)

73. *quotiēs* → *quotiēns*
   **Apply:** `Gen.30.41` la: `quotiēs` → `quotiēns`
74. *quotiēs* → *quotiēns*
   **Apply:** `Matt.18.21` la: `“quotiēs` → `“quotiēns`
75. *quotiēs* → *quotiēns*
   **Apply:** `Matt.23.37` la: `quotiēs` → `quotiēns`
76. *Quotiēs* → *Quotiēns*
   **Apply:** `Luke.13.34` la: `Quotiēs` → `Quotiēns`
77. *quotiēs* → *quotiēns*
   **Apply:** `1Cor.11.25` la: `quotiēs` → `quotiēns`
78. *Quotiēs* → *Quotiēns*
   **Apply:** `1Cor.11.26` la: `Quotiēs` → `Quotiēns`

## E. *obœdiō*, not *obēdiō* — 18 places

The edition writes *obēdiō* everywhere (Gen 41:40, Acts, Rom, 2 Cor; decision 19's rules kept *obedierit*,
*obedissent*, *obedisti*). Gaffiot 2016 heads *ŏbœdĭō*. A judgment for you: Gaffiot's spelling (the brief's rule) or
the edition's consistent one. If accepted, the three decision-19 rows become *oboedierit*, *oboedissent*,
*oboedisti*. Stem rule *obedi* → *oboedi*.

**Decision:** accept all (Nathan, 2026-11-11: "resolve … based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden Age spelling)"; resolved by Claude, see the evidence table)

79. *obēdiat* → *obœdiat*
   **Apply:** `Gen.41.40` la: `obēdiat,` → `obœdiat,`
80. *obēdiētis* → *obœdiētis*
   **Apply:** `Acts.3.22` la: `obēdiētis` → `obœdiētis`
81. *obēdierit* → *obœdierit*
   **Apply:** `Acts.3.23` la: `obēdierit,` → `obœdierit,`
82. *obēdientibus* → *obœdientibus*
   **Apply:** `Acts.5.32` la: `obēdientibus` → `obœdientibus`
83. *obēdiēbat* → *obœdiēbat*
   **Apply:** `Acts.6.7` la: `obēdiēbat.` → `obœdiēbat.`
84. *obēdiātur* → *obœdiātur*
   **Apply:** `Rom.1.5` la: `obēdiātur` → `obœdiātur`
85. *obēdientibus* → *obœdientibus*
   **Apply:** `Rom.2.8` la: `obēdientibus,` → `obœdientibus,`
86. *obēdientiā* → *obœdientiā*
   **Apply:** `Rom.5.19` la: `obēdientiā` → `obœdientiā`
87. *obēdiendō* → *obœdiendō*
   **Apply:** `Rom.6.16` la: `obēdiendō,` → `obœdiendō,`
88. *obēdiātis* → *obœdiātis*
   **Apply:** `Rom.6.16` la: `obēdiātis?` → `obœdiātis?`
89. *obēdientiæ* → *obœdientiæ*
   **Apply:** `Rom.6.16` la: `obēdientiæ` → `obœdientiæ`
90. *obēdīrent* → *obœdīrent*
   **Apply:** `Rom.15.18` la: `obēdīrent)` → `obœdīrent)`
91. *obēdientia* → *obœdientia*
   **Apply:** `Rom.16.19` la: `obēdientia` → `obœdientia`
92. *obēdiendum* → *obœdiendum*
   **Apply:** `Rom.16.26` la: `obēdiendum` → `obœdiendum`
93. *obēdientiam* → *obœdientiam*
   **Apply:** `2Cor.7.15` la: `obēdientiam,` → `obœdientiam,`
94. *obēdientiam* → *obœdientiam*
   **Apply:** `2Cor.9.13` la: `obēdientiam,` → `obœdientiam,`
95. *obēdiendum* → *obœdiendum*
   **Apply:** `2Cor.10.5` la: `obēdiendum` → `obœdiendum`
96. *obēdientia* → *obœdientia*
   **Apply:** `2Cor.10.6` la: `obēdientia.` → `obœdientia.`

## F. *adulēscēns*, not *adolēscēns* — 12 places

Added 2026-11-11 at Nathan's request. All twelve are the noun, "a young man" (Gen 34:19, Matt 19:20, 19:22, Mark
14:51 twice, 16:5, Luke 7:14, Acts 5:10, 7:58, 23:17, 23:18, 23:22); none is the participle "growing up". Gaffiot 2016
heads the noun *ădŭlēscēns* (and *ădŭlēscentia*); *ădŏlēscēns* is the participle of *adolēscō*. The corpus
(`python -m pipeline latin attest --count`): *adulescens* 622 hits (archaic 125, republican 110, classical 65,
augustan 50, silver 58) against *adolescens* 226 (republican 13, classical 3, silver 3; post-classical 124,
neo-Latin 83); likewise *adulescentem* 214 / *adolescentem* 95, *adulescentes* 156 / 106, *adulescentia* 163 / 64,
*adulescentulus* 46 / 10. *adol-* is the later and early modern spelling, as Castellio's printers wrote it. Luke 7:14
is in the chapters from the earlier manual work. Recommended: *adulēscēns*. Stem rule *adolescen* → *adulescen*
(the verb *adolēscō*, *adolēvit*, *adolēscere* stays).

**Decision:** accept all (Nathan, 2026-11-11: "resolve … based on Gaffiot and the corpus evidence (prioritizing Cicero and Golden Age spelling)"; resolved by Claude, see the evidence table)

97. *adolēscēns* → *adulēscēns*
   **Apply:** `Gen.34.19` la: `adolēscēns:` → `adulēscēns:`
98. *adolēscēns* → *adulēscēns*
   **Apply:** `Matt.19.20` la: `adolēscēns:` → `adulēscēns:`
99. *adolēscēns* → *adulēscēns*
   **Apply:** `Matt.19.22` la: `adolēscēns` → `adulēscēns`
100. *adolēscēns* → *adulēscēns*
   **Apply:** `Mark.14.51` la: `adolēscēns` → `adulēscēns`
101. *adolēscentēs* → *adulēscentēs*
   **Apply:** `Mark.14.51` la: `adolēscentēs` → `adulēscentēs`
102. *adolēscentem* → *adulēscentem*
   **Apply:** `Mark.16.5` la: `adolēscentem` → `adulēscentem`
103. *Adolēscēns* → *Adulēscēns*
   **Apply:** `Luke.7.14` la: `“Adolēscēns,` → `“Adulēscēns,`
104. *adolēscentēs* → *adulēscentēs*
   **Apply:** `Acts.5.10` la: `adolēscentēs` → `adulēscentēs`
105. *adolēscentis* → *adulēscentis*
   **Apply:** `Acts.7.58` la: `adolēscentis,` → `adulēscentis,`
106. *adolēscentem* → *adulēscentem*
   **Apply:** `Acts.23.17` la: `adolēscentem` → `adulēscentem`
107. *adolēscentem* → *adulēscentem*
   **Apply:** `Acts.23.18` la: `adolēscentem` → `adulēscentem`
108. *adolēscentem* → *adulēscentem*
   **Apply:** `Acts.23.22` la: `adolēscentem` → `adulēscentem`
