# *usque* with a short u; *eō usque* apart; *quousque*, *hūcusque*, *adusque* joined

Proposed 2026-11-18, from Nathan's spot checks of that day: "Exodus 11:8 *Eōusque*: I think we should split this
to *Eō usque*"; "*ūsque* with a long u has crept in *passim*, e.g. Exodus 20:5, 20:6 and 34:7"; "We need to consider
*quoūsque* more carefully. Should it be together or separated? I'm pretty sure the best evidence also keeps that u
short." Dictionary answers from `python -m pipeline latin macron` and `latin ls`; corpus counts from
`latin attest` (tiers as the tool gives them). **Your decision**, section by section. Nothing applied.

On acceptance I also: change the `ūsque` rows in `data/decisions/*.forms.tsv` to the new forms (they record the
old call, and `propose` would re-apply it); add *usque* and its compounds to the macron step's exceptions in
`pipeline/macronize.py`, since Gaffiot would otherwise put the long u back in every new draft (Deuteronomy's
successors); add the rule to `brief.md` (Macrons) as an exception to "Gaffiot decides hidden quantities"; rebuild
the gold. `text/orig/` is not touched: it keeps what the page prints (*eousque*, *eovsque*, *eo vsque*, *quousque*).

## 1. The u of *usque*: short

The u stands before two consonants, so the metre cannot show its quantity; only the dictionaries' judgment can.

- **Gaffiot 2016** marks it long, and consistently in every compound: *ūsquĕ*, *ădūsquĕ*, *ăbūsquĕ*, *hūcūsquĕ*,
  *quŏūsquĕ*.
- **Wiktionary** heads *usque*, *adusque*, *abusque*, *quousque* and *hūcusque* with the u bare (by the brief's names
  rule, a bare vowel there counts as short); **Macronizer** has *usque* and *quousque* with no long vowel.
- **Lewis & Short** heads *usquĕ* with the u unmarked; but L&S does not mark vowels long only by position, so its
  silence is weak evidence either way.
- No other source available here (the OLD, de Vaan) was checked: `pipeline latin` does not reach them.
- **In this edition**: every *usque* in the settled text is *ūsque* (Gaffiot's mark, by the brief's rule that
  Gaffiot decides hidden quantities; the `forms.tsv` rows of Acts, 1–2 Corinthians and 2 Timothy cite "your settled
  *ūsque*" besides Gaffiot). The front matter already
  writes *usque* (`docs/front-matter-critique.md` argued the short u in its review).

So this is two dictionaries against one, and it overrules the brief's general rule for one word family. Your
message decides it; I record it as an exception rather than a change to the rule.

Proposed: ***usque*** in all 118 places (Gen 8, Exod 4, Lev 1, Num 10, Deut 26, Matt 15, Mark 3, Luke 10, John 1,
Acts 16, Rom 3, 1 Cor 1, 2 Cor 6, Gal 1, Phil 3, 1 Tim 1, 2 Tim 1, Heb 3, Jas 1, Rev 4). Exod 34:7 is in the
capitals of God's proclamation (*ŪSQUE* → *USQUE*). Lev 26:28, Num 24:22, Gen 25:34, Matt 12:20, Acts 7:19, 24:6
and Phil 2:7 already write *eō* apart and change here only in the u. The genitives with *-que*
(*adventūsque*, *manūsque*, *Spīritūsque*, *tellūsque*, *vīctūsque*, *interitūsque*, *magistrātūsque*,
*discessūsque*) are fourth-declension *-ūs* and are not touched.

1. **Apply:** `Gen.6.7` la: `volucrēs—ūsque adeō` → `volucrēs—usque adeō`
2. **Apply:** `Gen.8.5` la: `ūsque ad` → `usque ad`
3. **Apply:** `Gen.14.14` la: `ūsque cōnsequitur.` → `usque cōnsequitur.`
4. **Apply:** `Gen.25.18` la: `ūsque suīs` → `usque suīs`
5. **Apply:** `Gen.25.34` la: `ūsque prærogātīvam` → `usque prærogātīvam`
6. **Apply:** `Gen.32.24` la: `ūsque ad` → `usque ad`
7. **Apply:** `Gen.34.5` la: `ūsque ad` → `usque ad`
8. **Apply:** `Gen.44.8` la: `ūsque ē` → `usque ē`
9. **Apply:** `Exod.20.5` la: `ūsque quārtamque` → `usque quārtamque`
10. **Apply:** `Exod.20.6` la: `ūsque stirpem` → `usque stirpem`
11. **Apply:** `Exod.34.7` la: `ŪSQUE ÆTĀTĒS` → `USQUE ÆTĀTĒS`
12. **Apply:** `Exod.34.34` la: `ūsque ad` → `usque ad`
13. **Apply:** `Lev.26.28` la: `eō ūsque,` → `eō usque,`
14. **Apply:** `Num.4.47` la: `ūsque ad` → `usque ad`
15. **Apply:** `Num.6.5` la: `ūsque ad` → `usque ad`
16. **Apply:** `Num.9.15` la: `ūsque ad` → `usque ad`
17. **Apply:** `Num.14.45` la: `ūsque concīdērunt.` → `usque concīdērunt.`
18. **Apply:** `Num.21.24` la: `ūsque ad` → `usque ad`
19. **Apply:** `Num.21.26` la: `ūsque ēripuerat.` → `usque ēripuerat.`
20. **Apply:** `Num.21.30` la: `ūsque ad Dībōnem,` → `usque ad Dībōnem,`
21. **Apply:** `Num.21.30` la: `ūsque ad Nōphan,` → `usque ad Nōphan,`
22. **Apply:** `Num.23.7` la: `ūsque Syriā` → `usque Syriā`
23. **Apply:** `Num.24.22` la: `ūsque, ut` → `usque, ut`
24. **Apply:** `Deut.1.7` la: `ūsque ad` → `usque ad`
25. **Apply:** `Deut.1.24` la: `ūsque ad` → `usque ad`
26. **Apply:** `Deut.1.44` la: `ūsque ā` → `usque ā`
27. **Apply:** `Deut.2.23` la: `ūsque ad` → `usque ad`
28. **Apply:** `Deut.2.36` la: `ūsque nūllum` → `usque nūllum`
29. **Apply:** `Deut.3.12` la: `ūsque ab` → `usque ab`
30. **Apply:** `Deut.3.14` la: `ūsque ad` → `usque ad`
31. **Apply:** `Deut.4.11` la: `ūsque cælum` → `usque cælum`
32. **Apply:** `Deut.4.49` la: `ūsque ad` → `usque ad`
33. **Apply:** `Deut.5.9` la: `ūsque ad` → `usque ad`
34. **Apply:** `Deut.5.10` la: `ūsque stirpēs` → `usque stirpēs`
35. **Apply:** `Deut.7.9` la: `ūsque stirpēs:` → `usque stirpēs:`
36. **Apply:** `Deut.9.8` la: `ūsque adeō` → `usque adeō`
37. **Apply:** `Deut.11.24` la: `ūsque ad` → `usque ad`
38. **Apply:** `Deut.28.22` la: `ūsque persequētur.` → `usque persequētur.`
39. **Apply:** `Deut.28.24` la: `ūsque exitium` → `usque exitium`
40. **Apply:** `Deut.28.48` la: `ūsque ad` → `usque ad`
41. **Apply:** `Deut.28.49` la: `ūsque ab` → `usque ab`
42. **Apply:** `Deut.28.52` la: `ūsque adeō` → `usque adeō`
43. **Apply:** `Deut.28.61` la: `ūsque exitium` → `usque exitium`
44. **Apply:** `Deut.31.30` la: `fīnem ūsque.` → `fīnem usque.`
45. **Apply:** `Deut.32.22` la: `ūsque tartara` → `usque tartara`
46. **Apply:** `Deut.32.22` la: `ūsque fundāmenta` → `usque fundāmenta`
47. **Apply:** `Deut.34.1` la: `ūsque ad` → `usque ad`
48. **Apply:** `Deut.34.2` la: `ūsque ad` → `usque ad`
49. **Apply:** `Deut.34.3` la: `ūsque ad` → `usque ad`
50. **Apply:** `Matt.2.15` la: `ūsque ad` → `usque ad`
51. **Apply:** `Matt.11.13` la: `ūsque vāticinātī` → `usque vāticinātī`
52. **Apply:** `Matt.11.23` la: `ūsque ēlāta` → `usque ēlāta`
53. **Apply:** `Matt.11.23` la: `‘num ad cælum ūsque` → `‘num ad cælum usque`
54. **Apply:** `Matt.12.20` la: `ūsque ut` → `usque ut`
55. **Apply:** `Matt.12.42` la: `ūsque terrīs` → `usque terrīs`
56. **Apply:** `Matt.13.30` la: `ūsque ad` → `usque ad`
57. **Apply:** `Matt.22.26` la: `ūsque ad` → `usque ad`
58. **Apply:** `Matt.23.35` la: `ūsque ad` → `usque ad`
59. **Apply:** `Matt.24.38` la: `ūsque ad` → `usque ad`
60. **Apply:** `Matt.26.29` la: `ūsque ad` → `usque ad`
61. **Apply:** `Matt.26.58` la: `ūsque ad` → `usque ad`
62. **Apply:** `Matt.27.45` la: `ūsque ad` → `usque ad`
63. **Apply:** `Matt.27.64` la: `ūsque ad` → `usque ad`
64. **Apply:** `Matt.28.20` la: `ūsque ad` → `usque ad`
65. **Apply:** `Mark.14.25` la: `ūsque ad` → `usque ad`
66. **Apply:** `Mark.14.54` la: `ūsque in` → `usque in`
67. **Apply:** `Mark.15.33` la: `ūsque ad` → `usque ad`
68. **Apply:** `Luke.1.80` la: `ūsque ad` → `usque ad`
69. **Apply:** `Luke.4.29` la: `ūsque ad` → `usque ad`
70. **Apply:** `Luke.10.15` la: `ūsque ēvecta` → `usque ēvecta`
71. **Apply:** `Luke.10.15` la: `‘num ad cælum ūsque` → `‘num ad cælum usque`
72. **Apply:** `Luke.10.15` la: `ūsque dēprimēris.` → `usque dēprimēris.`
73. **Apply:** `Luke.11.51` la: `ūsque ad` → `usque ad`
74. **Apply:** `Luke.16.16` la: `ūsque ad` → `usque ad`
75. **Apply:** `Luke.17.27` la: `ūsque ad` → `usque ad`
76. **Apply:** `Luke.23.44` la: `ūsque ad` → `usque ad`
77. **Apply:** `Luke.24.50` la: `ūsque, sublātīsque` → `usque, sublātīsque`
78. **Apply:** `John.2.7` la: `ūsque replēvissent,` → `usque replēvissent,`
79. **Apply:** `Acts.1.2` la: `ūsque diem,` → `usque diem,`
80. **Apply:** `Acts.1.22` la: `ūsque ā` → `usque ā`
81. **Apply:** `Acts.3.21` la: `ūsque ad` → `usque ad`
82. **Apply:** `Acts.7.19` la: `ūsque afflīxit,` → `usque afflīxit,`
83. **Apply:** `Acts.11.5` la: `ūsque vēnit.` → `usque vēnit.`
84. **Apply:** `Acts.11.19` la: `ūsque in` → `usque in`
85. **Apply:** `Acts.13.6` la: `ūsque, nactī` → `usque, nactī`
86. **Apply:** `Acts.13.20` la: `ūsque ad` → `usque ad`
87. **Apply:** `Acts.13.47` la: `ūsque terrās` → `usque terrās`
88. **Apply:** `Acts.17.15` la: `ūsque dūxērunt:` → `usque dūxērunt:`
89. **Apply:** `Acts.20.4` la: `[ūsque in` → `[usque in`
90. **Apply:** `Acts.20.11` la: `ūsque ad` → `usque ad`
91. **Apply:** `Acts.22.22` la: `ūsque verba` → `usque verba`
92. **Apply:** `Acts.24.6` la: `ūsque, ut` → `usque, ut`
93. **Apply:** `Acts.26.22` la: `ūsque diem` → `usque diem`
94. **Apply:** `Acts.28.15` la: `ūsque ad` → `usque ad`
95. **Apply:** `Rom.5.13` la: `ūsque ad` → `usque ad`
96. **Apply:** `Rom.5.14` la: `ūsque etiam` → `usque etiam`
97. **Apply:** `Rom.15.19` la: `ūsque ad` → `usque ad`
98. **Apply:** `1Cor.16.8` la: `ūsque ad` → `usque ad`
99. **Apply:** `2Cor.1.8` la: `ūsque adeō,` → `usque adeō,`
100. **Apply:** `2Cor.3.14` la: `ūsque diem` → `usque diem`
101. **Apply:** `2Cor.3.15` la: `ūsque diem,` → `usque diem,`
102. **Apply:** `2Cor.10.13` la: `ūsque pertingāmus.` → `usque pertingāmus.`
103. **Apply:** `2Cor.10.15` la: `ūsque adeō` → `usque adeō`
104. **Apply:** `2Cor.12.2` la: `ūsque cælum.` → `usque cælum.`
105. **Apply:** `Gal.4.2` la: `ūsque ad` → `usque ad`
106. **Apply:** `Phil.1.6` la: `ūsque ad` → `usque ad`
107. **Apply:** `Phil.2.7` la: `ūsque ad` → `usque ad`
108. **Apply:** `Phil.2.8` la: `ūsque ad` → `usque ad`
109. **Apply:** `1Tim.6.14` la: `ūsque ad` → `usque ad`
110. **Apply:** `2Tim.2.9` la: `ūsque ad` → `usque ad`
111. **Apply:** `Heb.4.12` la: `ūsque ad` → `usque ad`
112. **Apply:** `Heb.9.10` la: `ūsque ad` → `usque ad`
113. **Apply:** `Heb.12.4` la: `ūsque ad` → `usque ad`
114. **Apply:** `Jas.5.7` la: `ūsque ad` → `usque ad`
115. **Apply:** `Rev.2.10` la: `ūsque, et` → `usque, et`
116. **Apply:** `Rev.12.11` la: `ūsque adeō` → `usque adeō`
117. **Apply:** `Rev.14.20` la: `ūsque ad` → `usque ad`
118. **Apply:** `Rev.18.5` la: `ūsque pertigērunt,` → `usque pertigērunt,`

**Decision:** accept (Nathan, 2026-11-18: "Accept all four")

## 2. *eō usque*: two words

- **Dictionaries**: no source in the macron database has *eōusque* or *eousque* as a form ("no source knows this
  form"), and Lewis & Short has no headword for it. Gaffiot's headwords have none either. L&S gives *usque* "with adverbs of
  place" as its own sense (Cic. *Att.* 1.14.4 *eos usque istinc*), the construction *eō usque* belongs to.
- **Corpus**: *eo usque* 164 hits (Digest 19, Bacon 11, Tacitus 11, Quintilian 6, Valerius Maximus 6, Sulpicius
  Severus 6 …); *eousque* 12 (Bacon 2, Columella 2, the Digest 2, Tertullian, William of Tyre, Erasmus, More …).
  Divided, about 14 to 1.
- **Castellio** divides and joins it: 1738 prints *eo vsque* at Gen 25:34, Lev 26:28 and Num 24:22 but *eovsque* at
  Exod 9:10 and 11:8 and *eousque* at Deut 12:31, 28:20 and 28:52; 1573 prints *eò vsque* at Acts 7:19 and 24:6,
  *eo usque* at Phil 2:7, *eousque* at Matt 12:20 (all from `text/orig/`, read on the page in stage 2b).
- **The settled text** follows neither consistently: *eō ūsque* apart in seven places (Gen 25:34, Lev 26:28, Num
  24:22, Matt 12:20, Acts 7:19, 24:6, Phil 2:7), *eōusque* joined in five. The printed text is in `text/orig/` for
  anyone who wants Castellio's division.

Proposed: ***eō usque*** apart in the five joined places, as in the other seven (their u is in section 1).

119. **Apply:** `Exod.9.10` la: `eōusque,` → `eō usque,`
120. **Apply:** `Exod.11.8` la: `“Eōusque,”` → `“Eō usque,”`
121. **Apply:** `Deut.12.31` la: `eōusque,` → `eō usque,`
122. **Apply:** `Deut.28.20` la: `eōusque` → `eō usque`
123. **Apply:** `Deut.28.52` la: `eōusque` → `eō usque`

**Decision:** accept (Nathan, 2026-11-18: "Accept all four")

## 3. *quousque*: one word, both vowels unmarked

- **Dictionaries**: all three head it as one word. Gaffiot *quŏūsquĕ*, Lewis & Short *quŏ-usquē* (as `latin ls` prints it) (sense I "until
  what time, how long", "class."), Wiktionary *quousque*; Macronizer has it too. Unlike *eō usque*, it is a word in
  every dictionary checked.
- **The o is short in both Gaffiot and L&S**: the *quō* of *quō usque* loses its length before the vowel, a shortening that
  belongs inside a word (across two words the vowel would be elided instead). So their marks treat it as one word
  (my inference from the marks, not a statement of theirs).
- **The u**: Gaffiot long, Wiktionary and Macronizer bare; the same split as section 1, so it follows section 1.
- **Corpus**: *quousque* 385 hits (Albert of Aix 67, William of Tyre 48, Seneca 19, Augustine 15, Isidore 12,
  Tertullian 11; Cicero, *ad Atticum*, 3); *quo usque* 62 (Augustine 17, Cicero 7, Quintilian 6, Apuleius 3,
  Plautus 2). *quo usque tandem* 4 (Cicero, Quintilian 2, Apuleius) against *quousque tandem* 9 (Livy, Sallust,
  Seneca the Elder, Castellio 2 …). As with *ejusmodī* (`spellings-2026-11-15.md` §2), the division in the
  classical texts is the modern editors': the corpus's Cicero joins it in *ad Atticum* and divides it elsewhere.
- **Castellio** joins it every time: *quousque* in all nine places (Exod 10:3, Num 14:11 twice, 14:27; Matt 17:17
  twice, Mark 9:19 twice, Rev 6:10; `text/orig/`).

Proposed: keep it **joined**, as the dictionaries, the corpus's majority and Castellio have it, and write
***quousque*** with no macron (Gaffiot's and L&S's short o; the short u of section 1). The settled text's
*quoūsque* (9 places) changes only in the u. If you would rather divide it, it would be *quō usque* (the o long
again as a word of its own); say so and I will redo the nine lines.

124. **Apply:** `Exod.10.3` la: `quoūsque` → `quousque`
125. **Apply:** `Num.14.11` la: `“Quoūsque` → `“Quousque`
126. **Apply:** `Num.14.11` la: `quoūsque` → `quousque`
127. **Apply:** `Num.14.27` la: `“Quoūsque` → `“Quousque`
128. **Apply:** `Matt.17.17` la: `Quoūsque vōbīscum` → `Quousque vōbīscum`
129. **Apply:** `Matt.17.17` la: `Quoūsque vōs` → `Quousque vōs`
130. **Apply:** `Mark.9.19` la: `“quoūsque` → `“quousque`
131. **Apply:** `Mark.9.19` la: `quoūsque tandem vōs` → `quousque tandem vōs`
132. **Apply:** `Rev.6.10` la: `“Quoūsque` → `“Quousque`

**Decision:** accept (Nathan, 2026-11-18: "Accept all four")

## 4. *hūcusque*, *adusque*: joined, u short

Both are headed as one word by Gaffiot (*hūcūsquĕ*, *ădūsquĕ*) and Wiktionary (*hūcusque*, *adusque*); 1573
prints *hucusque* (Luke 23:5, John 2:10), 1738 *hucusque* (Num 14:19) and *adusque* (Deut 7:20). Corpus: *hucusque*
128 against *huc usque* 53; *adusque* 42 (Apuleius 10, Ovid 5) against *ad usque* 177 (Ammianus 107, Solinus). They
stay joined as Castellio prints them; only the u changes, with section 1.

133. **Apply:** `Num.14.19` la: `hūcūsque` → `hūcusque`
134. **Apply:** `Deut.7.20` la: `adūsque` → `adusque`
135. **Apply:** `Luke.23.5` la: `hūcūsque.”` → `hūcusque.”`
136. **Apply:** `John.2.10` la: `hūcūsque` → `hūcusque`

**Decision:** accept (Nathan, 2026-11-18: "Accept all four")
