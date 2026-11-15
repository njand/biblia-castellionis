# *ānulus*, *hujusmodī*, and four spellings Gaffiot heads otherwise

Proposed 2026-11-15, from Nathan's questions of that day (*annulus* in Exodus 30, *hujusmodi* one word or two) and the
side notes of `exod31-40-stages3-5.md`. Corpus counts from `python -m pipeline latin attest --count` (T1–T2 are the
Golden Age tiers); Gaffiot's headwords from `latin macron`. **Your decision**, section by section. Nothing applied.

On acceptance I also add the spelling rules named in each section to `data/rules/orthography.tsv`, re-key the
Exodus 31–40 forms rows, and re-run `propose Exod 31-40`, so the draft in review matches.

## 1. *ānulus*, the ring: one n, long a

- **Gaffiot 2016** heads the word ***ānŭlus***; *annŭlus* is only a cross-reference to it. Wiktionary gives
  *ānnulus* as an "alternative form of *ānulus*". The a is long by nature (*ānus*, "ring").
- **Corpus**: *anul-* 515 hits, 42 in T1 (Cicero 35, Plautus 25, Suetonius 15); *annul-* 105 hits, **none in T1**
  (Martinus Duncanus, Gregory IX, William of Tyre, Erasmus). Form by form: *anulum* 138 / *annulum* 38, *anulos* 57 /
  *annulos* 4, *anulo* 66 / *annulo* 21.
- **Castellio**: 1573 prints ***anulum*** (Luke 15:22) and ***anulos*** (Jas 2:2) with one n
  (`text/orig/LUK.usfm`, `JAS.usfm`, read on the page). 1738, the OT base, prints *annulus* throughout.
- **The settled text is split**: Luke 15:22 *ānulum* (your 2019 text), but Jas 2:2, Genesis and Exodus *annul-*
  with the a unmarked. Those *annul-* forms were readers' calls, made because the printing had double n; the
  spelling itself was never decided.

Proposed: ***ānul-*** in all 17 places. Exod 12:5 *mās, annulus* ("a yearling", from *annus*) is a different word,
Castellio's, and stays. Rule for future drafts: `annul → anul`, stem, approved; a yearling in a later book gets a
forms row.

1. **Apply:** `Gen.38.18` la: `“Annulum tuum` → `“Ānulum tuum`
2. **Apply:** `Gen.38.25` la: `jam dūcerētur, annulum` → `jam dūcerētur, ānulum`
3. **Apply:** `Gen.41.42` la: `manū annulum` → `manū ānulum`
4. **Apply:** `Exod.25.12` la: `quattuor annulōs` → `quattuor ānulōs`
5. **Apply:** `Exod.25.14` la: `per annulōs illōs` → `per ānulōs illōs`
6. **Apply:** `Exod.25.15` la: `in annulīs arcæ` → `in ānulīs arcæ`
7. **Apply:** `Exod.25.26` la: `quattuor annulōs` → `quattuor ānulōs`
8. **Apply:** `Exod.26.24` la: `ūnō annulō` → `ūnō ānulō`
9. **Apply:** `Exod.26.29` la: `eōrumque annulōs` → `eōrumque ānulōs`
10. **Apply:** `Exod.27.4` la: `æreōs annulōs` → `æreōs ānulōs`
11. **Apply:** `Exod.27.7` la: `per annulōs immittēs` → `per ānulōs immittēs`
12. **Apply:** `Exod.28.23` la: `duōs annulōs aureōs` → `duōs ānulōs aureōs`
13. **Apply:** `Exod.28.26` la: `duōs annulōs aureōs` → `duōs ānulōs aureōs`
14. **Apply:** `Exod.28.28` la: `suīs annulīs ad annulōs` → `suīs ānulīs ad ānulōs`
15. **Apply:** `Exod.30.4` la: `bīnōs annulōs aureōs` → `bīnōs ānulōs aureōs`
16. **Apply:** `Exod.30.4` la: `quōs annulōs vectēs` → `quōs ānulōs vectēs`
17. **Apply:** `Jas.2.2` la: `gestāns annulōs` → `gestāns ānulōs`

**Decision:** accept (Nathan, 2026-11-15: "Accept all of the other proposals I didn't comment on")

## 2. *hujusmodī*, *ejusmodī*, *cujusmodī*: one word

- **Gaffiot 2016** heads them as one word: *hŭjusmŏdī*, *ĕjusmŏdī*. Lewis & Short also writes *hūjusmŏdi*,
  *ējusmŏdi* as one word (the second sends you to *modus*).
- **Corpus**: mixed, and in Cicero it splits by **edition, not by author**. The joined forms come from a few texts
  (Golden Age tiers): *ejusmodi* in *ad Familiares* 28, *de Inventione* 27, *ad Quintum fratrem* 15, *de Officiis* 8;
  *hujusmodi* in *de Inventione* 31, *ad Familiares* 4, *de Officiis* 3; *cujusmodi* in *ad Familiares* 9. The
  divided forms come from the others: *ejus modi* (Cicero 334) in *ad Atticum* 41, *pro Cluentio* 30, *de Oratore*
  18, the *Tusculans* 11, *de Finibus* 10 …; *hujus modi* (Cicero 33) and *cujus modi* (Cicero 35) in *ad Atticum*,
  the *Verrines*, *de Oratore*, the *Topica*. So the letters to Atticus divide where the letters to his friends
  join: the choice is the modern editor's. Roman books were not consistent in word division, so the corpus cannot
  show a preference of Cicero's own. Most modern texts of Cicero divide (*ejus modi* 334 against 84).
- **Castellio**: the printed texts (1573's New Testament, 1738's Genesis and Exodus drafts) join them 73 times
  out of 74 (*huiusmodi* 51, *eiusmodi* 16, *cuiusmodi* 5, *istiusmodi* 1). The one exception is Matt 13:36
  *huius modi verbis*.
- **The settled text** has 51 *hujusmodī*, 16 *ejusmodī*, 5 *cujusmodī*, 1 *istīusmodī*. Only Matt 13:36 has
  *hujus modī*, which follows 1573's one exception.

Proposed: one word everywhere, as Gaffiot and Castellio's usual practice have it. The printed text keeps 1573's
*huius modi* at Matt 13:36 (decision 58). Rule: `hujus modi → hujusmodi`, phrase, approved (also `ejus modi`,
`cujus modi`).

1. **Apply:** `Matt.13.36` la: `hujus modī verbīs` → `hujusmodī verbīs`

**Decision:** pending (Nathan, 2026-11-15, asked for the corpus evidence, Cicero especially: given in the section above)

## 3. Four spellings the settled Exodus shares with 31–40, against Gaffiot

All four come from 1738; the settled 21–30 took them from Wikisource, which follows 1738.

1. ***sēdecim*** for *sexdecim* (Gen 46:18, Exod 26:25; the draft 36:29). Gaffiot heads ***sēdĕcim*** (*sexdecim*
   a cross-reference). Corpus: *sedecim* in Livy 19, Tacitus 10 (6 in T1); *sexdecim* only in Columella and
   later writers (none in T1). This is decision 70's "more classical number form". Rule: `sexdecim → sedecim`,
   word.
   **Apply:** `Gen.46.18` la: `vidēlicet sexdecim` → `vidēlicet sēdecim`
   **Apply:** `Exod.26.25` la: `spīræ sexdecim` → `spīræ sēdecim`
2. ***trīcēnum*** for *trīgēnum* (Exod 26:8; the draft 36:15). Gaffiot ***trīcēnī***. No source knows *trīgēnum*,
   and the corpus has no example. Rule: `trigenum → tricenum`, word (and `trigen → tricen`, stem).
   **Apply:** `Exod.26.8` la: `longitūdinem trīgēnum` → `longitūdinem trīcēnum`
3. ***caccabōs*** for *cācabōs* (Exod 27:3; the draft 38:3). Gaffiot ***caccăbus*** (a short). Corpus: *caccab-* in
   Columella, Petronius, Apicius (T2); *cacab-* only medieval and later. Rule: `cacab → caccab`, stem.
   **Apply:** `Exod.27.3` la: `ejus cācabōs` → `ejus caccabōs`
4. ***sæpiō*** and its compounds with *æ* (Eph 2:14, Heb 12:1; the draft 39:23 *circumsēptum*). Gaffiot heads
   ***sæpĭō*** and ***circumsæpĭō*** (*sēp-* as variants), and decision 18 already gives the hedge as *sæpēs*. The
   settled text is split: Luke 14:23 *sæpta*, Matt 21:33 *sæptō* against these two. Rule: `circumsept →
   circumsaept`, stem (and `septique → saeptique`, word).
   **Apply:** `Eph.2.14` la: `sēptīque interstitium` → `sæptīque interstitium`
   **Apply:** `Heb.12.1` la: `circumsēptī nimbō` → `circumsæptī nimbō`

Left as is for now: *tēmetipsum* (Exod 32:13) and the settled *sēmetipsum* (Heb 1:3). Decision 51 splits *sē
ipsum*. *-met* is joined to its pronoun (*sēmet*, *tēmet*), and the question is only whether *ipsum* is joined too.
Corpus (2026-11-15): *temetipsum* 38 hits, none by a classical author (Thomas à Kempis 8, Augustine 4, the Vulgate 2,
Castellio 2), against *temet ipsum* 27 (the Vulgate 9, Erasmus 6, Curtius 1, Fronto 1); *semetipsum* 148 (Tertullian
49, Augustine 10, Curtius 6) against *semet ipsum* 81 (the Vulgate 18, Livy 6, the Digest 7); *memet ipsum* 16
(Cicero 2) against *memetipsum* 5 (Quintilian 1). Where classical texts have the phrase, they mostly print it apart
(Livy, Cicero); joined is mostly late and Christian. **Recommended**: apart, as decision 51 (*tēmet ipsum*, *sēmet
ipsum*), if you want it consistent.

**Decision:** accept (Nathan, 2026-11-15: "Accept all of the other proposals I didn't comment on")

## 4. The preface: *nostrī librī titulus* → *hujus librī titulus*

`text/FRT.usfm`, *Dē vītā Castelliōnis*: *Castelliōnem posteriōrēs typographī scrīpsērunt, unde nostrī librī
titulus.* Everywhere else the editor speaks in the singular (*parāvī*, *sequor*, *contulī*, *secūtus sum*,
*accommodāvī*, *dīvīsī*, *posuī*, *scrīpsī*, *omīsī*, *petam*). The only other plurals are in quotations
(Castellio's *nōs sartōrēs sumus*, *admonētō nōs*) and the general *doctī nostræ ætātis* ("scholars of our time"),
which is not the editor's *nōs*. *nostrī librī* is an editorial "we" left over from the draft
(`docs/front-matter-critique.md`, row 205). ***hujus librī*** fits the singular voice and repeats the heading
*Ratiō hujus ēditiōnis*. The book's title, *Biblia Sacra ex Sebastiani Castellionis interpretatione*, is what the
sentence points to.

Proposed (by hand on your yes; the front matter has no Apply route): `unde nostrī librī titulus` → `unde hujus librī
titulus`, in `text/FRT.usfm` and the quotation in `docs/front-matter.md`.

**Decision:** accept (Nathan, 2026-11-15: "Accept all of the other proposals I didn't comment on")

## 5. Heb 9:5 *Cherūbī*

Left over from `exod21-30-stages3-5.md`: the settled Heb 9:5 *Cherubī* has the u unmarked, against Gen 3:24
*Cherūbōs* and Exodus 25–37 *cherūb-* (Hebrew kərûḇîm, decided 2026-11-14).

1. **Apply:** `Heb.9.5` la: `splendidī Cherubī` → `splendidī Cherūbī`

**Decision:** accept (Nathan, 2026-11-15: "Accept all of the other proposals I didn't comment on")

## 6. *Ismaēl*, not *Ismæl* (found by the printed-text punctuation pass)

The settled Genesis spells the name *Ismæl-* in 13 places (*Ismæl*, *Ismæle*, *Ismælem*, *Ismælis*), with the
diphthong. Gaffiot heads it ***Ismăēl, ēlis*** (`latin macron`), as the Greek Ἰσμαήλ and the Hebrew
יִשְׁמָעֵאל have it: two syllables, *a* then *ē*. 1738 prints *Ismael* with *a* and *e* apart in every place read
(ten, on leaves 74, 75, 84, 88; divided *Isma-|el* at 16:11 and 25:17), and the settled *Ismaēlītīs*,
*Ismaēlītārum* already mark the *ē*. Proposed: *Ismaēl-* everywhere. Rule for future drafts: `Ismæl → Ismael`, stem.

1. **Apply:** `Gen.16.11` la: `Ismælem nōmine appellābis` → `Ismaēlem nōmine appellābis`
2. **Apply:** `Gen.16.15` la: `Abrāmus Ismælem` → `Abrāmus Ismaēlem`
3. **Apply:** `Gen.17.18` la: `propāgētur Ismæl` → `propāgētur Ismaēl`
4. **Apply:** `Gen.17.20` la: `Dē Ismæle` → `Dē Ismaēle`
5. **Apply:** `Gen.17.23` la: `assūmptō Ismæle` → `assūmptō Ismaēle`
6. **Apply:** `Gen.17.25` la: `Ismæl` → `Ismaēl`
7. **Apply:** `Gen.17.26` la: `fīlius Ismæl` → `fīlius Ismaēl`
8. **Apply:** `Gen.25.9` la: `et Ismæl` → `et Ismaēl`
9. **Apply:** `Gen.25.12` la: `Ismælis` → `Ismaēlis`
10. **Apply:** `Gen.25.16` la: `duodecim Ismælis` → `duodecim Ismaēlis`
11. **Apply:** `Gen.25.17` la: `Ipse Ismæl` → `Ipse Ismaēl`
12. **Apply:** `Gen.28.9` la: `ad Ismælem` → `ad Ismaēlem`
13. **Apply:** `Gen.36.3` la: `Basematham Ismælis` → `Basematham Ismaēlis`

**Decision:** accept (Nathan, 2026-11-15: "Go with Gaffiot. Ismaēl is correct.")
