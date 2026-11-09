# Test harness: normalize and macronize, scored against your finished chapters

From the Wikisource text alone (`python -m pipeline harness`). Nothing is scored on what it taught: A–C learn the spelling rules and your settled forms from the *other books*; D learns them from every *other chapter* (the realistic case for Matthew 14–28 and the rest of a book already begun). The spelling rules used are all those in `data/rules/REVIEW.md`, approved or not: this measures what they would do. Targets (PLAN §6): ≥ 99.5% words, ≥ 99% vowels.

| Variant | Words | Spelling | Vowels (macrons) | Words fully marked right |
|---|---:|---:|---:|---:|
| A: lexicon (Gaffiot/W/M) | 99.47% | 99.72% | 95.50% | 89.94% |
| B: + your settled forms | 99.47% | 99.72% | 97.96% | 95.47% |
| C: + WordPress in context | 99.47% | 99.70% | 99.25% | 98.25% |
| D: C, forms from other chapters | 99.51% | 99.77% | 99.49% | 98.83% |
| W: WordPress 2019 alone | 99.47% | 99.68% | 99.15% | 98.17% |

**Words**: of all gold words, the same word, spelling aside (what is left: Wikisource slips, which stage 2 corrects, and wording where 1760/1738 differ from your 1726–27, which decision 1 makes proposals). **Spelling**: of those, spelt as in your text (æ/œ, j/v, respellings, word division; capitals aside). **Vowels** and **fully marked**: of the correctly spelt words, each vowel long or not as in your text.

## By book (variant D)

| Book | Words | Spelling | Vowels |
|---|---:|---:|---:|
| Gen | 99.58% | 99.62% | 98.82% |
| Matt | 99.58% | 99.81% | 99.78% |
| Mark | 99.36% | 100.00% | 99.70% |
| Luke | 99.41% | 99.81% | 99.69% |
| John | 99.31% | 99.79% | 99.86% |

## Commonest errors, variant A (lexicon (Gaffiot/W/M))

Macron errors read *missing ā* (gold long, output not) or *extra ā*, then where (ending = last vowel; hidden = before two consonants; stem), then how the output was decided (lexicon, gaffiot = Gaffiot changed a W/M mark, homograph = W/M disagree and nothing chose, chosen = WordPress chose, settled = your forms, unknown = no source knows the word).

| Error | Count | Examples |
|---|---:|---|
| macron: missing ā · ending · homograph | 2299 | Gen.1.4 a (gold ā); Gen.1.6 aqua (gold aquā); Gen.1.7 ea (gold eā); Gen.1.14 a (gold ā) |
| macron: missing ā · stem · homograph | 920 | Gen.1.5 manē (gold māne); Gen.1.8 manē (gold māne); Gen.1.11 ederent (gold ēderent); Gen.1.13 manē (gold māne) |
| macron: missing ā · stem · unknown | 429 | Gen.2.15 Edenis (gold Ēdēnis); Gen.2.15 Edenis (gold Ēdēnis); Gen.3.1 versutissimus (gold versūtissimus); Gen.3.14 exsecrabilissima (gold exsecrābilissima) |
| word: different words | 239 | Gen.1.26 āereīs (gold āeriīs); Gen.2.2 opera (gold opere); Gen.2.4 habeat (gold habet); Gen.3.14 cicurarum (gold cicurum) |
| macron: extra ā · ending · homograph | 238 | Gen.1.5 manē (gold māne); Gen.1.8 manē (gold māne); Gen.1.13 manē (gold māne); Gen.1.19 manē (gold māne) |
| macron: extra ā · stem · homograph | 196 | Gen.4.12 cōlentī (gold colentī); Gen.4.17 condītam (gold conditam); Gen.6.14 pīce (gold pice); Gen.9.22 Pātrīs (gold Patris) |
| macron: missing ā · ending · unknown | 178 | Gen.2.11 Phison (gold Phisōn); Gen.2.13 Gehon (gold Gehōn); Gen.3.24 Cherubos (gold Cherūbōs); Gen.4.16 Edeni (gold Ēdēnī) |
| macron: extra ā · stem · lexicon | 130 | Gen.2.8 Ēum (gold eum); Gen.2.16 Ēīque (gold Eīque); Gen.4.16 Nōdā (gold Nodā); Gen.4.19 Ādā (gold Ada) |
| macron: missing ā · stem · lexicon | 121 | Gen.4.2 Abelem (gold Abēlem); Gen.4.4 Abelem (gold Abēlem); Gen.4.8 Abelem (gold Abēlem); Gen.6.8 Noæ (gold Nōæ) |
| macron: missing ā · hidden · homograph | 106 | Gen.3.3 plectāmur (gold plēctāmur); Gen.3.17 victum (gold vīctum); Gen.3.19 victum (gold vīctum); Gen.3.24 custōdiendum (gold cūstōdiendum) |
| macron: missing ā · ending · lexicon | 80 | Gen.4.2 Abel (gold Abēl); Gen.4.4 Abel (gold Abēl); Gen.4.9 Abel (gold Abēl); Gen.4.23 Si (gold Sī) |
| spelling: respelling missed | 53 | Gen.1.26 quicquid→quicquid (gold quidquid); Gen.2.8 confeverat→confeverat (gold cōnsēverat); Gen.2.10 quatuor→quatuor (gold quattuor); Gen.3.4 mulctabimini→mulctābiminī (gold multābiminī) |
| macron: extra ā · ending · lexicon | 37 | Gen.4.19 Ādā (gold Ada); Gen.4.20 Ādā (gold Ada); Gen.4.23 Ādām (gold Adam); Gen.9.18 Japhētō (gold Japhēto) |
| spelling: j/v | 31 | Gen.25.13 Nabajothua→Nabajothua (gold Nabaiothua); Matt.3.3 Esaja→Esajā (gold Ēsāiā); Matt.4.14 Esaja→Esajā (gold Ēsāiā); Matt.5.18 jota→jōta (gold iōta) |
| spelling: word division | 23 | Gen.7.11 septimōdecimō (gold septimō decimō); Gen.8.4 septimōdecimō (gold septimō decimō); Gen.8.14 septimōdecimō (gold septimō decimō); Gen.12.10 in gravēscente (gold ingravēscente) |
| macron: missing ā · hidden · unknown | 15 | Gen.3.1 Curnam (gold Cūrnam); Gen.5.29 infelicitata (gold īnfēlīcitāta); Gen.5.32 quingentenarius (gold quīngentēnārius); Gen.14.5 Zuzenses (gold Zuzēnsēs) |
| macron: extra ā · stem · gaffiot | 15 | Gen.14.18 prōtūlit (gold prōtulit); Gen.21.6 prōtūlit (gold prōtulit); Gen.22.2 Mōriam (gold Moriam); Matt.20.19 crucīfīgendum (gold crucifīgendum) |
| spelling: ligature | 14 | Gen.1.30 aerisque→ærisque (gold āerisque); Gen.4.22 Noema→Nœma (gold Nōēma); Gen.8.1 coercendas→cœrcendās (gold coercendās); Gen.16.11 Ismaelem→Ismaēlem (gold Ismælem) |
| macron: extra ā · hidden · homograph | 13 | Gen.2.16 vēsceris (gold vesceris); Gen.2.17 vēsceris (gold vesceris); Gen.3.1 vēscī (gold vescī); Gen.3.2 vēscī (gold vescī) |
| macron: extra ā · hidden · lexicon | 12 | Gen.16.8 ūndēnam (gold undenam); Gen.27.14 vēscerētur (gold vescerētur); Gen.27.31 vēscerētur (gold vescerētur); Matt.2.4 nāscitūrus (gold nascitūrus) |
| macron: missing ā · stem · gaffiot | 7 | Gen.4.22 fabricātōrem (gold fābricātōrem); Gen.15.3 herēs (gold hērēs); Gen.15.4 herēs (gold hērēs); Matt.1.10 Amōnem (gold Āmōnem) |
| macron: missing ā · hidden · lexicon | 2 | Gen.24.51 nuptūram (gold nūptūram); Matt.24.5 Christōs (gold Chrīstōs) |
| macron: extra ā · hidden · gaffiot | 1 | Gen.19.9 paulīsper (gold paulisper) |

## Commonest errors, variant D (C, forms from other chapters)

Macron errors read *missing ā* (gold long, output not) or *extra ā*, then where (ending = last vowel; hidden = before two consonants; stem), then how the output was decided (lexicon, gaffiot = Gaffiot changed a W/M mark, homograph = W/M disagree and nothing chose, chosen = WordPress chose, settled = your forms, unknown = no source knows the word).

| Error | Count | Examples |
|---|---:|---|
| word: different words | 221 | Gen.2.2 operā (gold opere); Gen.2.4 habeat (gold habet); Gen.3.14 cicurārum (gold cicurum); Gen.4.11 ∅ (gold apertō) |
| macron: missing ā · stem · chosen | 70 | Gen.2.8 Edene (gold Ēdēne); Gen.2.8 Edene (gold Ēdēne); Gen.2.10 Edene (gold Ēdēne); Gen.2.10 Edene (gold Ēdēne) |
| macron: missing ā · ending · chosen | 60 | Gen.1.16 noctis (gold noctīs); Gen.1.21 cēte (gold cētē); Gen.1.25 dīversa (gold dīversā); Gen.2.17 ea (gold eā) |
| macron: missing ā · stem · witness | 58 | Gen.3.24 Cherubōs (gold Cherūbōs); Gen.4.16 Edenī (gold Ēdēnī); Gen.4.16 Edenī (gold Ēdēnī); Gen.4.18 Henochō (gold Henōchō) |
| macron: extra ā · stem · lexicon | 51 | Gen.4.16 Nōdā (gold Nodā); Gen.4.19 Ādā (gold Ada); Gen.4.20 Ādā (gold Ada); Gen.4.23 Ādām (gold Adam) |
| macron: extra ā · ending · chosen | 45 | Gen.3.19 vultūs (gold vultus); Gen.4.25 Abēlīs (gold Abēlis); Gen.5.29 terrā (gold terra); Gen.6.19 conjugā (gold conjuga) |
| macron: extra ā · stem · chosen | 44 | Gen.2.16 vēscēris (gold vesceris); Gen.2.17 vēscēris (gold vesceris); Gen.3.5 comēderītis (gold comēderitis); Gen.3.18 vēscēris (gold vesceris) |
| macron: extra ā · stem · witness | 38 | Gen.3.14 exsēcrābilissima (gold exsecrābilissima); Gen.4.20 Jabālem (gold Jabalem); Gen.10.2 Mesēcus (gold Mesecus); Gen.10.3 Ascānās (gold Ascanās) |
| macron: missing ā · stem · lexicon | 37 | Gen.4.2 Abelem (gold Abēlem); Gen.4.4 Abelem (gold Abēlem); Gen.4.8 Abelem (gold Abēlem); Gen.10.19 Gazam (gold Gāzam) |
| spelling: respelling missed | 32 | Gen.1.26 quicquid→quicquid (gold quidquid); Gen.2.8 confeverat→confēverat (gold cōnsēverat); Gen.3.4 mulctabimini→mulctābiminī (gold multābiminī); Gen.4.14 repererit→repererit (gold reppererit) |
| spelling: j/v | 31 | Gen.25.13 Nabajothua→Nabajothua (gold Nabaiothua); Matt.3.3 Esaja→Ēsajā (gold Ēsāiā); Matt.4.14 Esaja→Ēsajā (gold Ēsāiā); Matt.5.18 jota→jōta (gold iōta) |
| spelling: word division | 22 | Gen.12.10 in gravēscente (gold ingravēscente); Gen.18.25 Ab sit (gold Absit); Gen.23.8 mēcum (gold mē cum); Gen.24.21 nec nē (gold necne) |
| macron: missing ā · ending · lexicon | 16 | Gen.4.2 Abel (gold Abēl); Gen.4.4 Abel (gold Abēl); Gen.4.9 Abel (gold Abēl); Gen.6.13 Nōa (gold Nōā) |
| spelling: ligature | 15 | Gen.4.18 Mahujaelem→Mahujaēlem (gold Mahujælem); Gen.4.18 Mathusaelem→Mathusaēlem (gold Mathusælem); Gen.8.1 coercendas→cœrcendās (gold coercendās); Gen.10.28 Abimaelem→Abimaēlem (gold Abimælem) |
| macron: extra ā · ending · lexicon | 15 | Gen.4.19 Ādā (gold Ada); Gen.4.20 Ādā (gold Ada); Gen.4.23 Ādām (gold Adam); Gen.10.7 Chūs (gold Chus) |
| macron: missing ā · stem · settled | 13 | Gen.4.23 Lamechī (gold Lamēchī); Gen.10.31 Semō (gold Sēmō); Gen.23.9 usum (gold ūsum); Gen.23.20 usum (gold ūsum) |
| macron: extra ā · stem · settled | 12 | Gen.10.7 Dodānem (gold Dodanem); Gen.11.26 Harānem (gold Haranem); Gen.14.2 eādem (gold eadem); Gen.23.2 eādem (gold eadem) |
| macron: missing ā · ending · witness | 11 | Gen.2.11 Phison (gold Phisōn); Gen.12.4 Charra (gold Charrā); Gen.13.7 Pherezæis (gold Pherezæīs); Gen.14.6 Seīris (gold Seirīs) |
| macron: extra ā · hidden · chosen | 10 | Gen.2.9 vēscendum (gold vescendum); Gen.2.16 vēscēris (gold vesceris); Gen.2.17 vēscēris (gold vesceris); Gen.3.1 vēscī (gold vescī) |
| macron: extra ā · ending · witness | 10 | Gen.5.29 īnfēlīcitātā (gold īnfēlīcitāta); Gen.10.2 Thirās (gold Thiras); Gen.10.11 Ninivēm (gold Nīnivem); Gen.10.12 Ninivēm (gold Nīnivem) |
| macron: extra ā · stem · gaffiot | 10 | Gen.22.2 Mōriam (gold Moriam); Matt.25.9 ēmite (gold emite); Matt.27.22 crucīfīgātur (gold Crucifīgātur); Matt.27.23 Crucīfīgātur (gold Crucifīgātur) |
| macron: missing ā · stem · homograph | 8 | Gen.6.7 repentia (gold rēpentia); Gen.7.8 repentibus (gold rēpentibus); Gen.7.21 repentium (gold rēpentium); Matt.1.7 Abiam (gold Ābīam) |
| macron: extra ā · hidden · lexicon | 8 | Gen.16.8 ūndēnam (gold undenam); Gen.27.14 vēscerētur (gold vescerētur); Gen.27.31 vēscerētur (gold vescerētur); Matt.2.4 nāscitūrus (gold nascitūrus) |
| macron: missing ā · ending · homograph | 5 | Gen.9.3 prædita (gold præditā); Gen.24.20 trānsfūsa (gold trānsfūsā); Matt.1.7 Abīas (gold Ābīās); Matt.27.57 Ārīmathæa (gold Ārimāthæā) |
| macron: missing ā · stem · gaffiot | 4 | Gen.4.22 fabricātōrem (gold fābricātōrem); Matt.1.10 Amōnem (gold Āmōnem); Matt.27.7 emērunt (gold ēmērunt); Matt.27.9 emērunt (gold ēmērunt) |
