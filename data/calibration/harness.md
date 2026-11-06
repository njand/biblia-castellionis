# Test harness: normalize and macronize, scored against your finished chapters

From the Wikisource text alone (`python -m pipeline harness`). Nothing is scored on what it taught: A–C learn the spelling rules and your settled forms from the *other books*; D learns them from every *other chapter* (the realistic case for Matthew 14–28 and the rest of a book already begun). The spelling rules used are all those in `data/rules/REVIEW.md`, approved or not: this measures what they would do. Targets (PLAN §6): ≥ 99.5% words, ≥ 99% vowels.

| Variant | Words | Spelling | Vowels (macrons) | Words fully marked right |
|---|---:|---:|---:|---:|
| A: lexicon (Gaffiot/W/M) | 99.72% | 99.55% | 95.36% | 89.54% |
| B: + your settled forms | 99.72% | 99.52% | 97.64% | 94.75% |
| C: + WordPress in context | 99.72% | 99.48% | 98.92% | 97.48% |
| D: C, forms from other chapters | 99.76% | 99.56% | 99.26% | 98.29% |
| W: WordPress 2019 alone | 99.72% | 99.48% | 98.99% | 97.78% |

**Words**: of all gold words, the same word, spelling aside (what is left: Wikisource slips, which stage 2 corrects, and wording where 1760/1738 differ from your 1726–27, which decision 1 makes proposals). **Spelling**: of those, spelt as in your text (æ/œ, j/v, respellings, word division; capitals aside). **Vowels** and **fully marked**: of the correctly spelt words, each vowel long or not as in your text.

## By book (variant D)

| Book | Words | Spelling | Vowels |
|---|---:|---:|---:|
| Gen | 99.62% | 99.27% | 98.72% |
| Matt | 99.91% | 99.69% | 99.48% |
| Mark | 99.68% | 99.93% | 99.57% |
| Luke | 99.83% | 99.67% | 99.55% |
| John | 99.84% | 99.67% | 99.73% |

## Commonest errors, variant A (lexicon (Gaffiot/W/M))

Macron errors read *missing ā* (gold long, output not) or *extra ā*, then where (ending = last vowel; hidden = before two consonants; stem), then how the output was decided (lexicon, gaffiot = Gaffiot changed a W/M mark, homograph = W/M disagree and nothing chose, chosen = WordPress chose, settled = your forms, unknown = no source knows the word).

| Error | Count | Examples |
|---|---:|---|
| macron: missing ā · ending · homograph | 1823 | Gen.1.4 a (gold ā); Gen.1.6 aqua (gold aquā); Gen.1.7 ea (gold eā); Gen.1.14 a (gold ā) |
| macron: missing ā · stem · homograph | 707 | Gen.1.5 manē (gold māne); Gen.1.8 manē (gold māne); Gen.1.11 ederent (gold ēderent); Gen.1.13 manē (gold māne) |
| macron: missing ā · stem · unknown | 383 | Gen.2.15 Edenis (gold Ēdēnis); Gen.2.15 Edenis (gold Ēdēnis); Gen.3.1 versutissimus (gold versūtissimus); Gen.3.14 exsecrabilissima (gold exsecrābilissima) |
| macron: missing ā · ending · unknown | 166 | Gen.2.11 Phison (gold Phisōn); Gen.2.13 Gehon (gold Gehōn); Gen.3.24 Cherubos (gold Cherūbōs); Gen.4.16 Edeni (gold Ēdēnī) |
| macron: missing ā · stem · lexicon | 153 | Gen.3.6 comeditque (gold comēditque); Gen.3.6 comedit (gold comēdit); Gen.3.12 comedī (gold comēdī); Gen.3.13 comedī (gold comēdī) |
| macron: extra ā · ending · homograph | 148 | Gen.1.5 manē (gold māne); Gen.1.8 manē (gold māne); Gen.1.13 manē (gold māne); Gen.1.19 manē (gold māne) |
| macron: extra ā · stem · lexicon | 140 | Gen.2.8 Ēum (gold eum); Gen.2.16 Ēīque (gold Eīque); Gen.4.1 vīrum (gold virum); Gen.4.16 Nōdā (gold Nodā) |
| macron: extra ā · stem · homograph | 112 | Gen.4.12 cōlentī (gold colentī); Gen.4.17 condītam (gold conditam); Gen.6.14 pīce (gold pice); Gen.10.4 Elīsa (gold Elisa) |
| word: different words | 105 | Gen.1.26 āereīs (gold āeriīs); Gen.2.2 opera (gold opere); Gen.2.25 conjux (gold conjūnx); Gen.3.14 cicurarum (gold cicurum) |
| macron: missing ā · hidden · homograph | 68 | Gen.3.3 plectāmur (gold plēctāmur); Gen.3.17 victum (gold vīctum); Gen.3.19 victum (gold vīctum); Gen.3.24 custōdiendum (gold cūstōdiendum) |
| macron: missing ā · ending · lexicon | 56 | Gen.4.2 Abel (gold Abēl); Gen.4.4 Abel (gold Abēl); Gen.4.9 Abel (gold Abēl); Gen.4.23 Si (gold Sī) |
| spelling: respelling missed | 55 | Gen.1.26 quicquid→quicquid (gold quidquid); Gen.2.8 confeverat→confeverat (gold cōnsēverat); Gen.2.10 quatuor→quatuor (gold quattuor); Gen.3.4 mulctabimini→mulctābiminī (gold multābiminī) |
| spelling: ligature | 54 | Gen.1.30 aerisque→ærisque (gold āerisque); Gen.2.24 adhaerebit→adhaērēbit (gold adhærēbit); Gen.4.15 poenam→pœnam (gold poenam); Gen.4.22 Noema→Nœma (gold Nōēma) |
| macron: missing ā · stem · gaffiot | 45 | Gen.3.11 comedistī (gold comēdistī); Gen.3.17 comedistī (gold comēdistī); Gen.4.22 fabricātōrem (gold fābricātōrem); Gen.8.5 Fiebant (gold Fīēbant) |
| macron: extra ā · ending · lexicon | 28 | Gen.4.19 Ādā (gold Ada); Gen.4.20 Ādā (gold Ada); Gen.4.23 Ādām (gold Adam); Gen.9.18 Japhētō (gold Japhēto) |
| macron: extra ā · hidden · lexicon | 27 | Gen.3.1 vēscī (gold vescī); Gen.3.2 vēscī (gold vescī); Gen.3.3 vēscī (gold vescī); Gen.16.8 ūndēnam (gold undenam) |
| spelling: word division | 27 | Gen.7.11 septimōdecimō (gold septimō decimō); Gen.8.4 septimōdecimō (gold septimō decimō); Gen.8.14 septimōdecimō (gold septimō decimō); Gen.12.10 in gravēscente (gold ingravēscente) |
| macron: extra ā · hidden · gaffiot | 26 | Gen.1.8 secūndus (gold secundus); Gen.1.15 lūcēntia (gold lūcentia); Gen.8.21 dēlēctātus (gold dēlectātus); Gen.19.9 paulīsper (gold paulisper) |
| macron: extra ā · stem · gaffiot | 24 | Gen.1.9 cōnflūeret (gold cōnflueret); Gen.4.15 appōsuit (gold apposuit); Gen.4.19 altērī (gold alterī); Gen.6.14 cōnstrūitō (gold cōnstruitō) |
| spelling: j/v | 18 | Gen.25.13 Nabajothua→Nabajothua (gold Nabaiothua); Matt.3.3 Esaja→Esajā (gold Ēsāiā); Matt.4.14 Esaja→Esajā (gold Ēsāiā); Matt.5.18 jota→jōta (gold iōta) |
| macron: missing ā · hidden · unknown | 13 | Gen.3.1 Curnam (gold Cūrnam); Gen.5.29 infelicitata (gold īnfēlīcitāta); Gen.5.32 quingentenarius (gold quīngentēnārius); Gen.14.5 Zuzenses (gold Zuzēnsēs) |
| macron: extra ā · hidden · homograph | 6 | Gen.2.16 vēsceris (gold vesceris); Gen.2.17 vēsceris (gold vesceris); Gen.3.18 vēsceris (gold vesceris); Gen.27.19 vēscere (gold vescere) |
| macron: missing ā · hidden · gaffiot | 1 | Gen.4.25 peremptī (gold perēmptī) |
| macron: missing ā · hidden · lexicon | 1 | Gen.24.51 nuptūram (gold nūptūram) |

## Commonest errors, variant D (C, forms from other chapters)

Macron errors read *missing ā* (gold long, output not) or *extra ā*, then where (ending = last vowel; hidden = before two consonants; stem), then how the output was decided (lexicon, gaffiot = Gaffiot changed a W/M mark, homograph = W/M disagree and nothing chose, chosen = WordPress chose, settled = your forms, unknown = no source knows the word).

| Error | Count | Examples |
|---|---:|---|
| word: different words | 92 | Gen.2.2 operā (gold opere); Gen.3.14 cicurārum (gold cicurum); Gen.4.11 ∅ (gold apertō); Gen.4.14 extortīs (gold extorris) |
| macron: missing ā · stem · lexicon | 83 | Gen.3.6 comeditque (gold comēditque); Gen.3.24 ejectō (gold ējectō); Gen.4.2 Abelem (gold Abēlem); Gen.4.4 Abelem (gold Abēlem) |
| spelling: ligature | 73 | Gen.2.24 adhaerebit→adhaērēbit (gold adhærēbit); Gen.4.15 poenam→pœnam (gold poenam); Gen.4.18 Mahujaelem→Mahujaēlem (gold Mahujælem); Gen.4.18 Mathusaelem→Mathusaēlem (gold Mathusælem) |
| macron: missing ā · stem · chosen | 67 | Gen.2.8 Edene (gold Ēdēne); Gen.2.8 Edene (gold Ēdēne); Gen.2.10 Edene (gold Ēdēne); Gen.2.10 Edene (gold Ēdēne) |
| macron: missing ā · stem · witness | 60 | Gen.3.24 Cherubōs (gold Cherūbōs); Gen.4.16 Edenī (gold Ēdēnī); Gen.4.16 Edenī (gold Ēdēnī); Gen.4.17 Henochum (gold Henōchum) |
| macron: missing ā · ending · chosen | 59 | Gen.1.16 noctis (gold noctīs); Gen.1.21 cēte (gold cētē); Gen.1.25 dīversa (gold dīversā); Gen.2.17 ea (gold eā) |
| macron: extra ā · stem · lexicon | 56 | Gen.4.16 Nōdā (gold Nodā); Gen.4.19 Ādā (gold Ada); Gen.4.20 Ādā (gold Ada); Gen.4.23 Ādām (gold Adam) |
| macron: extra ā · ending · chosen | 46 | Gen.3.19 vultūs (gold vultus); Gen.4.25 Abēlīs (gold Abēlis); Gen.5.29 terrā (gold terra); Gen.6.19 conjugā (gold conjuga) |
| macron: extra ā · stem · chosen | 42 | Gen.2.16 vēscēris (gold vesceris); Gen.2.17 vēscēris (gold vesceris); Gen.3.18 vēscēris (gold vesceris); Gen.4.15 nōtam (gold notam) |
| spelling: respelling missed | 41 | Gen.1.26 quicquid→quicquid (gold quidquid); Gen.2.8 confeverat→confēverat (gold cōnsēverat); Gen.3.4 mulctabimini→mulctābiminī (gold multābiminī); Gen.4.14 repererit→repererit (gold reppererit) |
| macron: extra ā · stem · witness | 37 | Gen.3.14 exsēcrābilissima (gold exsecrābilissima); Gen.4.20 Jabālem (gold Jabalem); Gen.10.2 Mesēcus (gold Mesecus); Gen.10.3 Ascānās (gold Ascanās) |
| macron: missing ā · stem · gaffiot | 21 | Gen.3.11 comedistī (gold comēdistī); Gen.3.17 comedistī (gold comēdistī); Gen.4.22 fabricātōrem (gold fābricātōrem); Gen.12.12 viderint (gold vīderint) |
| spelling: word division | 21 | Gen.12.10 in gravēscente (gold ingravēscente); Gen.18.25 Ab sit (gold Absit); Gen.23.8 mēcum (gold mē cum); Gen.24.21 nec nē (gold necne) |
| spelling: j/v | 18 | Gen.25.13 Nabajothua→Nabajothua (gold Nabaiothua); Matt.3.3 Esaja→Ēsajā (gold Ēsāiā); Matt.4.14 Esaja→Ēsajā (gold Ēsāiā); Matt.5.18 jota→jōta (gold iōta) |
| macron: extra ā · stem · settled | 15 | Gen.10.7 Dodānem (gold Dodanem); Gen.11.26 Harānem (gold Haranem); Gen.14.2 eādem (gold eadem); Gen.23.2 eādem (gold eadem) |
| macron: extra ā · hidden · gaffiot | 14 | Gen.1.15 lūcēntia (gold lūcentia); Gen.8.21 dēlēctātus (gold dēlectātus); Gen.19.9 paulīsper (gold paulisper); Gen.24.13 stānte (gold stante) |
| macron: extra ā · hidden · lexicon | 14 | Gen.3.1 vēscī (gold vescī); Gen.3.2 vēscī (gold vescī); Gen.3.3 vēscī (gold vescī); Gen.16.8 ūndēnam (gold undenam) |
| macron: missing ā · ending · lexicon | 14 | Gen.4.2 Abel (gold Abēl); Gen.4.4 Abel (gold Abēl); Gen.4.9 Abel (gold Abēl); Gen.6.13 Nōa (gold Nōā) |
| macron: extra ā · ending · lexicon | 14 | Gen.4.19 Ādā (gold Ada); Gen.4.20 Ādā (gold Ada); Gen.4.23 Ādām (gold Adam); Gen.10.7 Chūs (gold Chus) |
| macron: missing ā · stem · settled | 13 | Gen.4.23 Lamechī (gold Lamēchī); Gen.10.31 Semō (gold Sēmō); Gen.23.9 usum (gold ūsum); Gen.23.20 usum (gold ūsum) |
| macron: extra ā · stem · gaffiot | 12 | Gen.1.9 cōnflūeret (gold cōnflueret); Gen.6.14 cōnstrūitō (gold cōnstruitō); Gen.6.15 Cōnstrūendī (gold Cōnstruendī); Gen.8.3 difflūentēs (gold diffluentēs) |
| macron: missing ā · ending · witness | 10 | Gen.2.11 Phison (gold Phisōn); Gen.12.4 Charra (gold Charrā); Gen.13.7 Pherezæis (gold Pherezæīs); Gen.14.6 Seīris (gold Seirīs) |
| macron: missing ā · stem · homograph | 10 | Gen.3.5 comederitis (gold comēderitis); Gen.6.7 repentia (gold rēpentia); Gen.7.8 repentibus (gold rēpentibus); Gen.7.21 repentium (gold rēpentium) |
| macron: extra ā · ending · witness | 9 | Gen.5.29 īnfēlīcitātā (gold īnfēlīcitāta); Gen.10.2 Thirās (gold Thiras); Gen.10.11 Ninivēm (gold Nīnivem); Gen.10.12 Ninivēm (gold Nīnivem) |
| macron: extra ā · hidden · chosen | 7 | Gen.2.9 vēscendum (gold vescendum); Gen.2.16 vēscēris (gold vesceris); Gen.2.17 vēscēris (gold vesceris); Gen.3.6 vēscendum (gold vescendum) |
