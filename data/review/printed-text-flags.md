# The reading edition against the printed text: what the ⚑ readings show

Proposed 2026-11-13 (Claude), on Nathan's request ("Yes, propose fixes") after the drafts of Castellio's text as
printed (decision 57; `data/review/*-orig.md`). Those drafts read every settled word against the base edition's
OCR, and the words the OCR could not decide on the page images (`data/decisions/*.orig.tsv`). Where 1573 differs from
the settled text by more than spelling, the review files mark it ⚑. This file proposes what the reading edition should
do about them. Readings decided before are listed at the end and not proposed again.

Each **Apply** line is an exact replacement inside that verse of `text/*.usfm`, checked to match once
(`python -m pipeline review check data/review/printed-text-flags.md`). Answer each group's **Decision:** with
*accept*, *accept all except N, M*, or *accept N, M*; then
`python -m pipeline review apply data/review/printed-text-flags.md --write`. These are proposals for the reading
edition only: the printed text follows 1573 whatever is decided here (decision 58).

## 1. A long s read as f (2)

The settled text has *f* where Castellio has *ſ*, the long s. Both places go back to the OCR witnesses that write
every ſ as f (the 1726–27 Google Books OCR, and 1750 and 1747 here). Wikisource has the same slips. The sense settles
both.

**Decision:** accept (Nathan, 2026-11-13)

1. **Luke 1:52** *Dēturbat potentēs dē foliīs* ("from the leaves") → *dē soliīs* ("from the thrones"). **1573**
   (canvas 789, page image): *Deturbat potentes de ſolijs*. 1758 OCR *de soliis*; the 1750 and 1747 OCRs *foliis*
   (they write ſ as f); Wikisource *foliis*. The Greek has ἀπὸ θρόνων (SBLGNT) and the Vulgate *de sede*: thrones.
   `latin macron`: *soliīs* (Gaffiot *sŏlĭum*).
   **Apply:** `Luke.1.52` la: `dē foliīs` → `dē soliīs`
2. **Luke 6:49** *domum in terrā fīne fundāmentō* → *sine fundāmentō* ("without a foundation"). **1573** (canvas
   795, page image): *in terra ſine fundamento conſtruxit*. 1758 OCR *sine fundamento*; 1750 *fine*, 1681 *line*
   (OCR); Wikisource *fine*. The Greek has χωρὶς θεμελίου and the Vulgate *sine fundamento*.
   **Apply:** `Luke.6.49` la: `fīne fundāmentō` → `sine fundāmentō`

## 2. A reading every printing has (1)

**Decision:** accept (Nathan, 2026-11-13)

3. **Acts 25:9** *Fēstus autem volēns Jūdæīs grātificāre* → *grātificārī*. **1573** (canvas 852, page image):
   *volens Iudæis gratificari*; 1758, 1715 and 1747 (OCR) *gratificari*. Wikisource alone has *gratificare*. The verb
   is deponent (Gaffiot *grātĭfĭcor, ātus sum, ārī*; `latin macron` *grātificārī*), as Castellio prints it. The
   collation listed this place as 1573's alone, because 1556's OCR is not aligned here
   (`data/calibration/Acts1-28-collation.tsv`).
   **Apply:** `Acts.25.9` la: `Jūdæīs grātificāre` → `Jūdæīs grātificārī`

## 3. One form of *misereor*'s participle (2)

The settled text has *miseritus* 9 times (Matt 9:36, 14:14, 18:27, 18:33; Mark 1:41, 5:19, 6:34, 9:22; Luke 10:33)
and *misertus* twice (Luke 15:20, Phil 2:27). 1573 prints *misertus* wherever it was read. Both are participles of
*misereor*, and Gaffiot gives *mĭsĕrĕor, ĕrĭtus*.

- The Matthew pilot kept your *miseritus* (`data/review/matt14-28-spelling.md`). Luke 15:20 took 1573's *misertus* in
  stage 2 (`data/review/luke14-24-stage2.md` item 6, accepted). Phil 2:27 has it from the Wikisource draft, as
  1573 prints it.
- Corpus (`latin attest --count`): *misertus* 75 hits, 68 post-classical (Vulgate 18, Augustine 8); *miseritus* 6
  hits, the earlier ones Seneca the Elder, Seneca, Quintilian and Gellius. Neither is in Cicero's prose here.
- Golden Age authors (Cicero, Caesar, Sallust, Nepos, Varro, Livy, Lucretius, Catullus, Vergil, Horace, Ovid; every
  example of *miseritus*, *miserita*, *miseritum*, *misertus*, *miserta*, *misertum* in `latin attest`): neither form
  at all. Decision 18 then takes the closest evidence: *miseritus* (the Senecas, Quintilian) against the late
  *misertus*.
- **Recommended: *miseritus* throughout** (decision 18: the earlier form, and Gaffiot's), which changes the two
  places below, and Exod 2:6 *ejusque miserta* (Pharaoh's daughter), the feminine of the same participle, to
  *miserita* (added 2026-11-13, when Nathan chose to unify).

**Decision:** accept (Nathan, 2026-11-13)

4. **Luke 15:20** *pater, misertus accurrit* → *miseritus*.
   **Apply:** `Luke.15.20` la: `pater, misertus accurrit` → `pater, miseritus accurrit`
5. **Philippians 2:27** *Deus ejus misertus est* → *miseritus*.
   **Apply:** `Phil.2.27` la: `ejus misertus est` → `ejus miseritus est`
5a. **Exodus 2:6** *ejusque miserta* → *miserita* (the feminine; `latin macron`: no long vowel).
   **Apply:** `Exod.2.6` la: `ejusque miserta, dīcit` → `ejusque miserita, dīcit`

## 4. One stem for the right hand: *dextra* or *dextera* (34)

The settled text has *dexter-* 34 times (*dexteram*, *dexterā*, *dexteræ*) and *dextr-* 22 times (*dextram*, *dextrā*,
*dextra*, *dextrās*, *dextrīs*, *dextrum*), with no rule behind the split: each follows the witness it came from. 1573
prints *dexter-* wherever it was read (Matt 5:30, 5:39, 6:3, 27:29; Mark 16:19). Gaffiot heads the adjective
*dexter, tra, trum* (*dextĕra* as a second entry).

- Corpus (`latin attest --count`): *dextra* 962 hits (classical era 339) against *dextera* 444 (83); *dextram* 321
  (classical 84) against *dexteram* 304 (classical 11). Republican-era counts are near even (*dextram* 12, *dexteram*
  11), and Cicero leans the other way: he has *dexteram* 9 times and is not among *dextram*'s first eight authors (the
  8th has 7). Caesar, Vergil and Livy write *dextr-*.
- Golden Age authors, every example in `latin attest` of the eight case forms of each stem: Cicero *dexter-* 18,
  *dextr-* 20; all Golden Age authors *dexter-* 95, *dextr-* 508 (Caesar 0 : 59, Varro 1 : 20, Livy 16 : 167, Vergil
  16 : 93, Ovid 27 : 120, Sallust 4 : 8, Nepos 0 : 4).
- **Recommended: *dextr-* throughout** (decision 18: Cicero near even, the rest of Golden Age prose and verse
  *dextr-*, and Gaffiot's headword). The lines below make that change. The masculine nominative *dexter* is the same
  either way.

**Decision:** accept (Nathan, 2026-11-13)

6. **Exod 14:29** `ad dexteram` → `ad dextram`.
   **Apply:** `Exod.14.29` la: `ad dexteram` → `ad dextram`
7. **Matt 22:44** `meam dexteram` → `meam dextram`.
   **Apply:** `Matt.22.44` la: `meam dexteram` → `meam dextram`
8. **Matt 25:33** `ad dexteram` → `ad dextram`.
   **Apply:** `Matt.25.33` la: `ad dexteram` → `ad dextram`
9. **Matt 25:34** `ejus dexteram` → `ejus dextram`.
   **Apply:** `Matt.25.34` la: `ejus dexteram` → `ejus dextram`
10. **Matt 26:64** `ad dexteram` → `ad dextram`.
   **Apply:** `Matt.26.64` la: `ad dexteram` → `ad dextram`
11. **Matt 27:38** `ad dexteram` → `ad dextram`.
   **Apply:** `Matt.27.38` la: `ad dexteram` → `ad dextram`
12. **Mark 10:37** `ad dexteram` → `ad dextram`.
   **Apply:** `Mark.10.37` la: `ad dexteram` → `ad dextram`
13. **Mark 12:36** `meam dexteram` → `meam dextram`.
   **Apply:** `Mark.12.36` la: `meam dexteram` → `meam dextram`
14. **Mark 15:27** `ad dexteram` → `ad dextram`.
   **Apply:** `Mark.15.27` la: `ad dexteram` → `ad dextram`
15. **Mark 16:5** `ad dexteram` → `ad dextram`.
   **Apply:** `Mark.16.5` la: `ad dexteram` → `ad dextram`
16. **Luke 1:11** `suffītōriæ dexteram` → `suffītōriæ dextram`.
   **Apply:** `Luke.1.11` la: `suffītōriæ dexteram` → `suffītōriæ dextram`
17. **Luke 6:6** `esset dexterā` → `esset dextrā`.
   **Apply:** `Luke.6.6` la: `esset dexterā` → `esset dextrā`
18. **Luke 20:42** `meam dexteram` → `meam dextram`.
   **Apply:** `Luke.20.42` la: `meam dexteram` → `meam dextram`
19. **Luke 22:50** `eīque dexteram` → `eīque dextram`.
   **Apply:** `Luke.22.50` la: `eīque dexteram` → `eīque dextram`
20. **Luke 22:69** `ad dexteram` → `ad dextram`.
   **Apply:** `Luke.22.69` la: `ad dexteram` → `ad dextram`
21. **Luke 23:33** `ad dexteram` → `ad dextram`.
   **Apply:** `Luke.23.33` la: `ad dexteram` → `ad dextram`
22. **John 18:10** `eīque dexteram` → `eīque dextram`.
   **Apply:** `John.18.10` la: `eīque dexteram` → `eīque dextram`
23. **John 21:6** `ad dexteram` → `ad dextram`.
   **Apply:** `John.21.6` la: `ad dexteram` → `ad dextram`
24. **Acts 2:34** `ad dexteram` → `ad dextram`.
   **Apply:** `Acts.2.34` la: `ad dexteram` → `ad dextram`
25. **Acts 7:56** `ad dexteram` → `ad dextram`.
   **Apply:** `Acts.7.56` la: `ad dexteram` → `ad dextram`
26. **Rom 8:34** `Deī dexteram` → `Deī dextram`.
   **Apply:** `Rom.8.34` la: `Deī dexteram` → `Deī dextram`
27. **Heb 1:3** `ad dexteram` → `ad dextram`.
   **Apply:** `Heb.1.3` la: `ad dexteram` → `ad dextram`
28. **Heb 1:13** `ad dexteram` → `ad dextram`.
   **Apply:** `Heb.1.13` la: `ad dexteram` → `ad dextram`
29. **Heb 8:1** `ad dexteram` → `ad dextram`.
   **Apply:** `Heb.8.1` la: `ad dexteram` → `ad dextram`
30. **Heb 10:12** `Deī dexteram` → `Deī dextram`.
   **Apply:** `Heb.10.12` la: `Deī dexteram` → `Deī dextram`
31. **Heb 12:2** `ad dexteram` → `ad dextram`.
   **Apply:** `Heb.12.2` la: `ad dexteram` → `ad dextram`
32. **1 Pet 3:22** `Deī dexteram` → `Deī dextram`.
   **Apply:** `1Pet.3.22` la: `Deī dexteram` → `Deī dextram`
33. **Rev 1:16** `manū dexterā` → `manū dextrā`.
   **Apply:** `Rev.1.16` la: `manū dexterā` → `manū dextrā`
34. **Rev 1:17** `ille dexterā` → `ille dextrā`.
   **Apply:** `Rev.1.17` la: `ille dexterā` → `ille dextrā`
35. **Rev 1:20** `meā dexterā` → `meā dextrā`.
   **Apply:** `Rev.1.20` la: `meā dexterā` → `meā dextrā`
36. **Rev 2:1** `suā dexterā` → `suā dextrā`.
   **Apply:** `Rev.2.1` la: `suā dexterā` → `suā dextrā`
37. **Rev 5:1** `soliō dexteram` → `soliō dextram`.
   **Apply:** `Rev.5.1` la: `soliō dexteram` → `soliō dextram`
38. **Rev 5:7** `dē dexterā` → `dē dextrā`.
   **Apply:** `Rev.5.7` la: `dē dexterā` → `dē dextrā`
39. **Rev 13:16** `manuī dexteræ` → `manuī dextræ`.
   **Apply:** `Rev.13.16` la: `manuī dexteræ` → `manuī dextræ`

## Decided before: not proposed again

These ⚑ readings were weighed earlier. They stay as decided unless you reopen them:

- **Luke 5:39** *pōtō vetere* (1573 *potato*): you restored *pōtō* as the classical form (`data/review/wording.md`
  item 8, 2026-11-06).
- **Mark 3:32** *circumsedēret* (1573 *circumsideret*): kept, Gaffiot *circumsĕdĕō* (`data/review/settled-1573.md`,
  decision 27).
- **2 Cor 11:28** *distinent* (1573 *destinent*, page image canvas 886): kept with 1556 and shown to you
  (`data/review/2cor1-13-stages3-5.md`).
- **Matt 24:38** *Nōa* (1573 *Noe*): one form per person, the Old Testament's (decision 46).
- **Matt 16:26** *æquiperet*, **23:6** *accubitiōnēs*, **17:14** and **27:29** *congenuclāns*, *congenuclantēs*
  (1573 *æquiparet*, *accubationes*, *congenulans*): decision 18 and your settled forms
  (`data/review/matt14-28-spelling.md`).
- **Matt 23:23** *decimātis* (1573 *decumatis*): left as drafted, with your *decumās* noted; still open there if you
  want *decumātis*.
