# Exodus 1–20, stages 1–2: Wikisource against 1738, 1750 and your 1726–27 text

Proposed 2026-11-08 (decision 30's standing rule), on the Old Testament route of Genesis 28–50
(`data/review/gen28-50-stage2.md`).

- **Base**: the 1738 Leipzig edition (decision 1), which Wikisource transcribes. Stage 1 drafted Wikisource's
  Exodus 1–20 as **`text/draft/EXO.usfm`** (BSB paragraphs).
- **Wikisource has every chapter**, but in 5, 6, 12 and 19 it runs the verses together with their numbers inline,
  and where it skips a printed number (5:3, 6:2, 6:11) or writes `2."Hic` without a space (12:2) the parser stopped
  splitting, so most of those chapters sat in one or two rows. `pipeline/wikisource.py` now splits at a number up to
  two past the one expected (the gap is flagged) and at a number followed by a dot and no space. Re-parsed from the
  cached page (same revision, 225845): Exodus 773 → 885 rows; Joshua 555 → 651 (the same fault); no other book
  changes.
- **Versification** (decision 5): Castellio's numbering in Exodus 5–7 is not the KJV's. 18 edits in
  `data/versification/Exod.draft.edits.tsv`, applied; every chapter now has the KJV count (545 verses):
  - **Printed numbers Wikisource drops**, restored where your 1726 text has them: 5:3, 6:2, 6:11, 10:7 (Wikisource
    prints “8.” twice), 18:27, 19:9, 20:20.
  - **Merges**: 5:16–17 (KJV 5:16), 6:2–3 (KJV 6:3), 6:25–26 (KJV 6:25 ends *the heads of the fathers of the
    Levites*, Castellio's 6:26; his 6:27 *Ii, quibus mandatum … cum suis copiis* is KJV 6:26), 7:1–2 (KJV 7:1), with
    a split at 7:3 *Atque ego Pharaonis animum* (KJV 7:3).
  - **Chapter breaks**: Castellio's 5:25 (*Cui Jova, Jam videbis*) is KJV 6:1, so the break moves back before it
    (a new `opens` edit in `pipeline/versify.py`); the opening of his 7:1, up to *obtemperaturum,*, is KJV 6:28–30
    (split twice); the opening clauses of his 8:1 (*Praeteritis septem diebus post ictum a Jova flumen,*) and 13:1
    (*Atque illo ipso die … eduxit Jova,*) are KJV 7:25 and 12:51, mid-sentence (`\nb`), as Gen 6:22 and 7:24.
- **Collation** (`python -m pipeline collate Exod 1-20`, `data/calibration/Exod1-20-collation.tsv`): 1738 base;
  1750 and your `TXT/3 - Edited` text as witnesses. Wikisource's Exodus is rougher than its Genesis: 68 “correct
  reading” places, 25 “others”, 22 divisions. Every one was read in 1738's hOCR line (leaf given), and on the page
  image where that was not clear. The 978 places where only 1738's OCR differs were filtered for real words and
  read: none is real (the four candidates are below).
- **In all, 120 corrections**: 78 slips (section 1), 16 name forms (2), Castellio’s marks twice (3), 13 misspellings
  (4), and 11 found by the stage 3–5 readings (5: e.g. 6:3, where Wikisource took the arm of 1738's drop-cap *E*
  for a word, and 10:10 *satis perspicua est vestra malitia*).
- **Ligatures**: Wikisource writes *æ/œ* in 16 lines of chapter 3 and a few others (*Ægypto, Chananæorum,
  æternitatem, ranæ*), *ae/oe* everywhere else. The macronizer cannot mark a word written with a ligature, so these
  were set to *ae/oe* in the draft (spelling only; the ligatures come back with the macrons, decision 16).
- **Kept after checking**:
  - 18:12 *cumque eo Aharon* (1738's OCR *eumque*; the page image, `sources/archive/crops/exod-18-12.jpg`, reads
    *cumque*).
  - 2:2 *et elegantem esse videret*: 1738's OCR puts *progeniem* here, but the page image (`exod-2-2.jpg`) shows it
    is a footnote, *c) progeniem*, offering a word for *familias* at 1:21 (*pietatem ᶜ familias*). 1738 prints such
    alternative renderings as footnotes (`docs/editions.md`); the text keeps *familias*.
  - Spellings the approved rules or the lexicon decide (1738 *adfluentem, adloquens, arcesseret, exstitit, vmquam,
    sepulcra, dextram, quemdam, monimenta*), and the forms decisions 19 and 26 settle (7:9 *adierunt* for 1738
    *adiuerunt*; 7:23 *repetivit* for *repetiit*).
  - Word division that changes nothing: 4:11 *annon* (1738 *an non*), 8:21 *Quodsi*, 12:4 *pater familias*.
- **Your 1726 text shares Wikisource's slips** at 4:10 *traditate* and elsewhere, so here too only 1738 decides.

**Applied to the draft** under decision 30's standing rule.

## 1. Wikisource slips (78)

1738 and at least one other printing (or 1738's page line alone, read in its hOCR) against Wikisource. Leaves are 1738's hOCR pages (the archive.org image is one lower).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

1. **Exod 2:5** *pedisse quis* → *pedissequis* (her maids). 1738 *pedisſequis* (leaf 115); your 1726.
    **Apply:** `Exod.2.5` la: `pedisse quis` → `pedissequis`
2. **Exod 2:7** *vellet ne* → *velletne*. 1738 and 1750 *velletne* (leaf 115).
    **Apply:** `Exod.2.7` la: `vellet ne` → `velletne`
3. **Exod 2:12** *Aegyptum occidit* → *Aegyptium* (he killed the Egyptian). 1738 *Aegyptium oc-|cidit* (leaf 115); your 1726.
    **Apply:** `Exod.2.12` la: `videret, Aegyptum occidit` → `videret, Aegyptium occidit`
4. **Exod 2:19** *defensasm* → *defensas*. 1738 *defenſas* (leaf 116); 1750, your 1726.
    **Apply:** `Exod.2.19` la: `esse defensasm` → `esse defensas`
5. **Exod 3:5** *Ne huc appropinques* → *appropinqua* (imperative). 1738 *Ne huc adpropinqua* (leaf 116); 1750, your 1726.
    **Apply:** `Exod.3.5` la: `Ne huc appropinques` → `Ne huc appropinqua`
6. **Exod 3:12** *colatis* → *coletis*. 1738 *coletis* (leaf 116); your 1726.
    **Apply:** `Exod.3.12` la: `in monte colatis` → `in monte coletis`
7. **Exod 3:13** *dicero* → *dixero*. 1738 *dixero* (leaf 116); 1750, your 1726.
    **Apply:** `Exod.3.13` la: `Israelitas, dicero` → `Israelitas, dixero`
8. **Exod 3:21** *disceditis* → *discedetis*. 1738 *dum diſcedetis* (leaf 117); 1750, your 1726.
    **Apply:** `Exod.3.21` la: `dum disceditis` → `dum discedetis`
9. **Exod 3:22** *muliere* → *mulieres*. 1738 *vt mulieres a ſuis vicinis* (leaf 117); your 1726.
    **Apply:** `Exod.3.22` la: `ut muliere; a` → `ut mulieres a`
10. **Exod 4:7** *Iterumque Deus, jussu* → *Iterumque Dei jussu* (at God's bidding). 1738, 1750 and your 1726 *Dei* (OCR).
    **Apply:** `Exod.4.7` la: `Iterumque Deus, jussu` → `Iterumque Dei jussu`
11. **Exod 4:17** *quo portenta facias* → *qua* (the rod). 1738 and your 1726 *qua* (OCR).
    **Apply:** `Exod.4.17` la: `manu feres, quo portenta` → `manu feres, qua portenta`
12. **Exod 5:8** *otiosus* → *otiosos*. 1738 *otioſos* (leaf 118); 1750, your 1726.
    **Apply:** `Exod.5.8` la: `esse enim otiosus` → `esse enim otiosos`
13. **Exod 5:16** *illus* → *illius*. 1750 and your 1726 *illius* (OCR).
    **Apply:** `Exod.5.16` la: `ita illus servos` → `ita illius servos`
14. **Exod 5:19** *quotidiane* → *quotidiano*. 1738 *opere quotidiano* (leaf 119); 1750, your 1726.
    **Apply:** `Exod.5.19` la: `opere quotidiane` → `opere quotidiano`
15. **Exod 5:23** *nomina* → *nomine*. 1738 *tuo nomine conueni* (leaf 119); 1750, your 1726.
    **Apply:** `Exod.5.23` la: `tuo nomina conveni` → `tuo nomine conveni`
16. **Exod 6:6** *Qua propter* → *Quapropter*. 1738, 1750 and your 1726 *Quapropter* (OCR).
    **Apply:** `Exod.6.6` la: `Qua propter haec` → `Quapropter haec`
17. **Exod 6:8** *Isacco* → *Isaaco*. 1738 *Iſaaco* (leaf 119); 1750, your 1726.
    **Apply:** `Exod.6.8` la: `Abrahamo, Isacco et` → `Abrahamo, Isaaco et`
18. **Exod 6:11** *demitteret* → *dimitteret*. 1738 *a ſuis finibus dimitteret* (leaf 119); 1750, your 1726.
    **Apply:** `Exod.6.11` la: `finibus demitteret` → `finibus dimitteret`
19. **Exod 6:15** *Sohar* → *Sochar*. 1738 and 1750 *Sochar* (leaf 119); your settled Gen 46:10 *Sōcharem*.
    **Apply:** `Exod.6.15` la: `Jachin, Sohar, et` → `Jachin, Sochar, et`
20. **Exod 6:16** *Gersonam* → *Gersonem*. 1738 and 1750 *Gerſonem* (leaf 119); your settled Gen 46:11 *Gērsōnem*.
    **Apply:** `Exod.6.16` la: `auctores, Gersonam,` → `auctores, Gersonem,`
21. **Exod 6:17** *Simeam* → *Simeim*. 1738 *Lebnim et Simeim* (leaf 119); your 1726.
    **Apply:** `Exod.6.17` la: `Lebnim et Simeam,` → `Lebnim et Simeim,`
22. **Exod 6:21** *fuerunt* → *fuere*. 1738, 1750 and your 1726 *fuere* (OCR).
    **Apply:** `Exod.6.21` la: `filii fuerunt Cora` → `filii fuere Cora`
23. **Exod 6:23** *Elisabam* → *Elisebam*. 1738 *Eliſebam* (leaf 120); 1750, your 1726.
    **Apply:** `Exod.6.23` la: `habuit Elisabam,` → `habuit Elisebam,`
24. **Exod 6:23** *Nahasoni, sororem* → *Nahasonis sororem*. 1738 *Na-|haſonis ſororem* (leaf 120); 1750, your 1726.
    **Apply:** `Exod.6.23` la: `filiam, Nahasoni, sororem` → `filiam, Nahasonis sororem`
25. **Exod 6:23** *Abiu* → *Abium*. 1738 *Abium* (leaf 120); your 1726.
    **Apply:** `Exod.6.23` la: `Nadabum, Abiu,` → `Nadabum, Abium,`
26. **Exod 6:25** *suscepit* → *sustulit*. 1738 and your 1726 *ſuſtulit*, 1750 *ſuſ tulit* (OCR).
    **Apply:** `Exod.6.25` la: `habebat, suscepit Phineem` → `habebat, sustulit Phineem`
27. **Exod 6:30** *linguae* → *lingua*. 1738 *qui lingua hæſitaret* (leaf 120); 1750, your 1726.
    **Apply:** `Exod.6.30` la: `qui linguae haesitaret` → `qui lingua haesitaret`
28. **Exod 7:8** *ut, poposcisset* → *ut, si poposcisset* (a word missing). 1738 *vt, ſi popoſciſſet* (leaf 120); your 1726.
    **Apply:** `Exod.7.8` la: `ut, poposcisset` → `ut, si poposcisset`
29. **Exod 7:15** *Convenio* → *Convenito* (imperative). 1738 *conueni-|to eum mane* (leaf 120).
    **Apply:** `Exod.7.15` la: `Convenio eum` → `Convenito eum`
30. **Exod 7:17** *nec sic quidem* → *ne sic quidem*. 1738 *Quod ſi ne ſic quidem* (leaf 120); 1750, your 1726.
    **Apply:** `Exod.7.17` la: `Quod si nec sic` → `Quod si ne sic`
31. **Exod 8:9** *tempus quando* → *tempus, inquit, quando* (a word missing). 1738 *tempus, inquit, quando* (leaf 121); 1750, your 1726.
    **Apply:** `Exod.8.9` la: `tempus quando` → `tempus, inquit, quando`
32. **Exod 8:11** *aflectis* → *adseclis* (attendants). 1738 *et adſeclis et populo* (leaf 121).
    **Apply:** `Exod.8.11` la: `et aflectis et` → `et adseclis et`
33. **Exod 8:12** *Ita Moses et Aharone et Pharone digressis* → *Ita Mose et Aharone a Pharaone digressis* (ablative absolute). 1738 *Ita Moſe et Aharone a Pharaone digreſſis* (leaf 121); your 1726.
    **Apply:** `Exod.8.12` la: `Ita Moses et Aharone et Pharone digressis` → `Ita Mose et Aharone a Pharaone digressis`
34. **Exod 8:12** *Pharoni* → *Pharaoni*. 1738 *Pharaoni* (leaf 121); your 1726.
    **Apply:** `Exod.8.12` la: `ille Pharoni immiserat` → `ille Pharaoni immiserat`
35. **Exod 8:13** *dosmesticatim* → *domesticatim*. 1738 *domeſticatim* (leaf 121); 1750, your 1726.
    **Apply:** `Exod.8.13` la: `illae dosmesticatim` → `illae domesticatim`
36. **Exod 8:27** *in solitudine* → *in solitudinem*. 1738 *in ſolitudinem progreſſos* (leaf 122); your 1726.
    **Apply:** `Exod.8.27` la: `iter in solitudine progressos` → `iter in solitudinem progressos`
37. **Exod 9:8** *plenis vasis* → *plenis volis* (handfuls; KJV “handfuls of ashes”). 1738 *plenis vo-|lis* (leaf 122); your 1726.
    **Apply:** `Exod.9.8` la: `plenis vasis` → `plenis volis`
38. **Exod 9:14** *omnes impetus* → *omnes meos impetus* (a word missing). 1738 *omnes meos impetus* (leaf 122); 1750, your 1726.
    **Apply:** `Exod.9.14` la: `omnes impetus` → `omnes meos impetus`
39. **Exod 9:30** *Et si* → *Etsi* (although). 1738 and your 1726 *Etſi* (OCR).
    **Apply:** `Exod.9.30` la: `Et si satis` → `Etsi satis`
40. **Exod 10:5** *relictum* → *reliquum*. 1738 *a grandine reliquum fa-|ctum* (leaf 123); your 1726.
    **Apply:** `Exod.10.5` la: `grandine relictum factum` → `grandine reliquum factum`
41. **Exod 10:12** *per Aegyptiam* → *per Aegyptum*. 1738, 1750 and your 1726 *Aegyptum* (OCR).
    **Apply:** `Exod.10.12` la: `per Aegyptiam` → `per Aegyptum`
42. **Exod 10:24** *cultum Jovae* → *cultum Jovam* (the supine with its object). 1738 *ite cultum Iouam* (leaf 124); 1750, your 1726.
    **Apply:** `Exod.10.24` la: `Ite cultum Jovae` → `Ite cultum Jovam`
43. **Exod 11:2** *vir a vicino* → *vir vicino* (Wikisource adds *a*). 1738 *et vir vicino, et fe-|mina a vicina* (leaf 124); 1750, your 1726.
    **Apply:** `Exod.11.2` la: `et vir a vicino` → `et vir vicino`
44. **Exod 11:7** *quantum* → *quantam* (with *differentiam*). 1738 *quantam Ioua differenti-|am* (leaf 125); 1750.
    **Apply:** `Exod.11.7` la: `quantum Jova differentiam` → `quantam Jova differentiam`
45. **Exod 12:7** *conspersentur* → *conspergentur*. 1738 *con-|ſpergentur* (leaf 125); your 1726.
    **Apply:** `Exod.12.7` la: `sanguine conspersentur` → `sanguine conspergentur`
46. **Exod 12:10** *igni cremabitis* → *igne*. 1738 and 1750 *igne cremabitis* (leaf 125).
    **Apply:** `Exod.12.10` la: `reliqui fuerit, igni` → `reliqui fuerit, igne`
47. **Exod 12:14** *dici* → *diei*. 1750 and your 1726 *diei* (OCR).
    **Apply:** `Exod.12.14` la: `illius dici` → `illius diei`
48. **Exod 12:21** *immolemus* → *immoletis*. 1738 *quibus immoletis paſcha* (leaf 126); your 1726.
    **Apply:** `Exod.12.21` la: `quibus immolemus` → `quibus immoletis`
49. **Exod 12:27** *bestrasque* → *vestrasque*. 1738 *veſtraſque* (leaf 126); 1750, your 1726.
    **Apply:** `Exod.12.27` la: `bestrasque` → `vestrasque`
50. **Exod 12:32** *postulastis* → *postulatis*. 1738 *vt poſtu-|latis* (leaf 126); 1750.
    **Apply:** `Exod.12.32` la: `ut postulastis` → `ut postulatis`
51. **Exod 12:48** a clause missing: *et tum demum ad id aditum haberent*. 1738 *haberent, et tum de-|mum ad id aditum haberent* (leaf 127); 1750, your 1726.
    **Apply:** `Exod.12.48` la: `circumcisos haberent, eademque` → `circumcisos haberent, et tum demum ad id aditum haberent, eademque`
52. **Exod 14:2** *Ballsephonis* → *Baalsephonis*. 1738 *Baalſephonis* (leaf 128); your 1726.
    **Apply:** `Exod.14.2` la: `regione Ballsephonis` → `regione Baalsephonis`
53. **Exod 14:7** *vehementer* → *veherentur*. 1738 *quibus omnibus veherentur duces* (leaf 128); 1750, your 1726.
    **Apply:** `Exod.14.7` la: `omnibus vehementer duces` → `omnibus veherentur duces`
54. **Exod 14:12** *An non* → *Annon* (as 4:11 *annon*). 1738 and 1750 *Annon* (OCR).
    **Apply:** `Exod.14.12` la: `An non hoc` → `Annon hoc`
55. **Exod 14:23** *omnes in medium in mare* → *omnes medium in mare* (Wikisource adds *in*). 1738 *o-|mnes medium in mare* (leaf 128); your 1726.
    **Apply:** `Exod.14.23` la: `omnes in medium in mare` → `omnes medium in mare`
56. **Exod 14:30** *Jova praesidio* → *Jovae praesidio*. 1738 *Iouæ præſidio* (leaf 129); 1750, your 1726.
    **Apply:** `Exod.14.30` la: `Israelitae, Jova praesidio` → `Israelitae, Jovae praesidio`
57. **Exod 15:26** *servirent* → *servarent*. 1738 *omnia ſeruarent* (leaf 130); 1750, your 1726.
    **Apply:** `Exod.15.26` la: `omnia servirent` → `omnia servarent`
58. **Exod 16:4** *se … pluvium* → *sese … pluturum* (that he would rain bread). 1738 *ſeſe illis panem pluturum* (leaf 130); 1750, your 1726.
    **Apply:** `Exod.16.4` la: `denuntiavit, se illis panem pluvium` → `denuntiavit, sese illis panem pluturum`
59. **Exod 16:9** *audivit* → *audiverit*. 1738 *querimonias audiuerit* (leaf 130); 1750, your 1726.
    **Apply:** `Exod.16.9` la: `querimonias audivit` → `querimonias audiverit`
60. **Exod 16:12** *renuntia … sub vespere* → *renuntiato … sub vesperum*. 1738 *re-|nuntiato eis, ſub veſperum* (leaf 130); 1750, your 1726.
    **Apply:** `Exod.16.12` la: `Israelitarum: renuntia eis, sub vespere` → `Israelitarum: renuntiato eis, sub vesperum`
61. **Exod 16:15** *inter se* → *inter sese*. 1738 *inter ſeſe dicere* (leaf 130); 1750, your 1726.
    **Apply:** `Exod.16.15` la: `inter se dicere` → `inter sese dicere`
62. **Exod 16:35** *quadriginta* → *quadraginta*. 1738 *per quadraginta annos* (leaf 131); your 1726.
    **Apply:** `Exod.16.35` la: `per quadriginta` → `per quadraginta`
63. **Exod 17:4** *quin me lapider* → *quin lapider* (Wikisource adds *me*). 1738 *parum abeſt, quin lapider* (leaf 131); your 1726.
    **Apply:** `Exod.17.4` la: `quin me lapider` → `quin lapider`
64. **Exod 17:9** *se* → *sese*. 1738 *poſtridie ſeſe in iugo* (leaf 132); your 1726.
    **Apply:** `Exod.17.9` la: `postridie se in` → `postridie sese in`
65. **Exod 17:12** *supposerunt* → *supposuerunt*. 1738 *ſuppoſuerunt* (leaf 132); 1750, your 1726.
    **Apply:** `Exod.17.12` la: `ei supposerunt` → `ei supposuerunt`
66. **Exod 17:14** *se enim* → *sese enim*. 1738 *ſeſe enim Amalechi* (leaf 132); 1750, your 1726.
    **Apply:** `Exod.17.14` la: `inculcaret: se enim` → `inculcaret: sese enim`
67. **Exod 18:1** *qui in Israelitas* → *qui Israelitas* (Wikisource adds *in*). 1738 *qui Iſraelitas ex Aegypto eduxiſſet* (leaf 132); 1750, your 1726.
    **Apply:** `Exod.18.1` la: `qui in Israelitas` → `qui Israelitas`
68. **Exod 18:9** *quo eos eripuisset* → *quod*. 1738 *quod eos eripuiſſet* (leaf 132); 1750, your 1726.
    **Apply:** `Exod.18.9` la: `Jethro, quo eos` → `Jethro, quod eos`
69. **Exod 18:10** *Gratias ago* → *Grates ago*. 1738 *grates ago* (leaf 132); 1750, your 1726.
    **Apply:** `Exod.18.10` la: `Gratias ago` → `Grates ago`
70. **Exod 18:14** *ira dixit* → *ita dixit*. 1738, 1750 and your 1726 *ita* (OCR).
    **Apply:** `Exod.18.14` la: `socer ejus ira dixit` → `socer ejus ita dixit`
71. **Exod 19:5** *ne eos habiturum* → *me eos habiturum*. 1738, 1750 and your 1726 *me* (OCR).
    **Apply:** `Exod.19.5` la: `conservabunt, ne eos` → `conservabunt, me eos`
72. **Exod 19:10** *vestimente* → *vestimenta*. 1738 *veſtimen-|ta perluant* (leaf 133); your 1726.
    **Apply:** `Exod.19.10` la: `sua vestimente perluant` → `sua vestimenta perluant`
73. **Exod 19:21** *videndi* → *visendi*. 1738, 1750 and your 1726 *viſendi* (OCR).
    **Apply:** `Exod.19.21` la: `Jovam videndi gratia` → `Jovam visendi gratia`
74. **Exod 19:23** *ut tu nobis* → *ut nobis tu* (word order). 1738 *vt nobis tu præcepiſti* (leaf 134); 1750.
    **Apply:** `Exod.19.23` la: `quod, ut tu nobis praecepisti` → `quod, ut nobis tu praecepisti`
75. **Exod 20:5** *aeve* → *neve*. 1738 *neue ea venerator, ne-|ue colito* (leaf 134); 1750, your 1726.
    **Apply:** `Exod.20.5` la: `venerator aeve colito` → `venerator, neve colito`
76. **Exod 20:15** *Ne furato* → *Ne furator* (the deponent's imperative). 1738 *Ne furator* (leaf 134); your 1726.
    **Apply:** `Exod.20.15` la: `Ne furato.` → `Ne furator.`
77. **Exod 20:18** *perterritus* → *perterriti*. 1738, 1750 and your 1726 *perterriti* (OCR).
    **Apply:** `Exod.20.18` la: `fumo, perterritus abscedere` → `fumo, perterriti abscedere`
78. **Exod 20:20** *Ne timueritis … tendandos* → *Ne metuite … tentandos*. 1738 *ne metuite, inquit: nam ad vos ten-|tandos* (leaf 134); 1750, your 1726.
    **Apply:** `Exod.20.20` la: `Ne timueritis," inquit, "nam ad vos tendandos` → `Ne metuite," inquit, "nam ad vos tentandos`

## 2. Names as 1738 prints them (16)

Wikisource writes *Aaron*, *Mosen* and *Moyses* in places; 1738 has *Aharon* (39 times in its OCR of Exodus 1–20, never *Aaron*), *Mosem* (23, never *Mosen*) and *Moses*, as your settled text and the rest of Wikisource's Exodus.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

79. **Exod 6:25** *Aaron* → *Aharon*.
    **Apply:** `Exod.6.25` la: `ex quibus Aaron et` → `ex quibus Aharon et`
80. **Exod 7:6** *Aaron* → *Moses*.
    **Apply:** `Exod.7.6` la: `Moses et Aaron Jovae` → `Moses et Aharon Jovae`
81. **Exod 7:9** *Aaron* → *Aharon*.
    **Apply:** `Exod.7.9` la: `projecit Aaron ante` → `projecit Aharon ante`
82. **Exod 7:12** *Aaronis* → *Aharonis*.
    **Apply:** `Exod.7.12` la: `virgas Aaronis virga` → `virgas Aharonis virga`
83. **Exod 7:19** *Aaroni* → *Aharoni*.
    **Apply:** `Exod.7.19` la: `vero Aaroni praecipito` → `vero Aharoni praecipito`
84. **Exod 7:20** *Aaron* → *Moses*.
    **Apply:** `Exod.7.20` la: `Moses et Aaron fecissent` → `Moses et Aharon fecissent`
85. **Exod 9:8** *Aaroni* → *Aharoni*.
    **Apply:** `Exod.9.8` la: `Mosi et Aaroni jussit` → `Mosi et Aharoni jussit`
86. **Exod 10:8** *Aarone* → *Aharone*.
    **Apply:** `Exod.10.8` la: `Mose et Aarone revocatis` → `Mose et Aharone revocatis`
87. **Exod 11:10** *Aarone* → *Aharone*.
    **Apply:** `Exod.11.10` la: `ab Aarone editis` → `ab Aharone editis`
88. **Exod 7:14** *Mosen* → *Mosem*.
    **Apply:** `Exod.7.14` la: `Jova Mosen alloquitur` → `Jova Mosem alloquitur`
89. **Exod 9:11** *Mosen* → *Mosem*.
    **Apply:** `Exod.9.11` la: `ante Mosen possent` → `ante Mosem possent`
90. **Exod 9:35** *Mosen* → *Mosem*.
    **Apply:** `Exod.9.35` la: `per Mosen praedixerat` → `per Mosem praedixerat`
91. **Exod 16:2** *Mosen* → *Mosem*.
    **Apply:** `Exod.16.2` la: `in Mosen et` → `in Mosem et`
92. **Exod 19:9** *Moysen* → *Mosem*.
    **Apply:** `Exod.19.9` la: `per Moysen relato` → `per Mosem relato`
93. **Exod 19:23** *Moyses* → *Moses*.
    **Apply:** `Exod.19.23` la: `Cui Moyses,` → `Cui Moses,`
94. **Exod 19:25** *Moyses* → *Moses*.
    **Apply:** `Exod.19.25` la: `Igitur Moyses ad` → `Igitur Moses ad`

## 3. Castellio's *G.* … *H.* marks (2)

Words Castellio took from the Greek (and Latin) “until the return to the Hebrew” (*Ad lectores admonitio*; `docs/editions.md`). As at Gen 44:6 and your settled Matt 19:4, the words stay and the marks go.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

95. **Exod 2:22** *G.L.* before *Item alterum, quem Eliezerem nominavit* (the second son, named here in the Septuagint and Vulgate; the Hebrew names Eliezer only at 18:4). 1738 prints the mark (OCR *G\*, leaf 116); Wikisource keeps it, your 1726 omits it. 1738 prints no *H.* after it in this verse.
    **Apply:** `Exod.2.22` la: `extranea. G.L. Item` → `extranea. Item`
96. **Exod 6:20** *G. L. et Mariam eorum sororem, H.* (“and Miriam their sister”, Septuagint and Vulgate). 1738 prints *G.L.* … *H.* (OCR, leaves 119–120).
    **Apply:** `Exod.6.20` la: `Mosem G. L. et Mariam eorum sororem, H. vixitque` → `Mosem et Mariam eorum sororem, vixitque`

## 4. Misspellings found among the unknown words (13)


Words no lexicon knows (`latin macron-check` on the draft), which the collation's spelling-blind comparison had folded away, and one stray full stop; checked in 1738's OCR line where the search reached it. Kept after checking: 12:37 *a Ramese* and 16:1 *in Sinem solitudinem* (1738 prints both), 12:39 *depsititios* (1738 *depſititios*), 3:13 *quærent* (a word the lexicon misses only for its ligature).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

97. **Exod 3:9** *ab Ægyptis* → *ab Aegyptiis*. 1738 *ab Aegyptiis vrgen-|tur* (leaf 116).
    **Apply:** `Exod.3.9` la: `ab Ægyptis urgentur` → `ab Aegyptiis urgentur`
98. **Exod 4:10** *traditate* → *tarditate* (slowness of tongue). 1738 *lin-|guae tarditate* (leaf 117, OCR); your 1726 shares Wikisource's slip.
    **Apply:** `Exod.4.10` la: `linguae traditate laboro` → `linguae tarditate laboro`
99. **Exod 5:9** *intendererent* → *intenderent*. your 1726 *intenderent*; 1738 not reached by the OCR search.
    **Apply:** `Exod.5.9` la: `vanitatem intendererent` → `vanitatem intenderent`
100. **Exod 6:6** *afferturum* → *asserturum* (long s read as f). 1738 *exemplis aſſerturum* (leaf 119); your 1726.
    **Apply:** `Exod.6.6` la: `exemplis afferturum` → `exemplis asserturum`
101. **Exod 9:5** *postrerum* → *posterum*. 1738 *conſtitui poſterum diem* (leaf 122).
    **Apply:** `Exod.9.5` la: `constitui postrerum diem` → `constitui posterum diem`
102. **Exod 12:33** *emitere* → *emittere*. 1738 *e-|mittere properantes* (leaf 126).
    **Apply:** `Exod.12.33` la: `finibus emitere` → `finibus emittere`
103. **Exod 12:49** *Eadam* → *Eadem*. your 1726 *Eadem lex*.
    **Apply:** `Exod.12.49` la: `Eadam lex` → `Eadem lex`
104. **Exod 12:49** *argentium* → *agentium* (sojourning among them). 1738 *inter eos agentium* (leaf 127); your 1726.
    **Apply:** `Exod.12.49` la: `inter eos argentium` → `inter eos agentium`
105. **Exod 13:5** *Amorraeaam* → *Amorraeam*. your 1726 *Amorraeam*.
    **Apply:** `Exod.13.5` la: `Hettaeam, Amorraeaam, Hevaeam` → `Hettaeam, Amorraeam, Hevaeam`
106. **Exod 14:12** *nos to monebamus* → *te*. 1738 *de quo nos te monebamus* (leaf 128).
    **Apply:** `Exod.14.12` la: `de quo nos to monebamus` → `de quo nos te monebamus`
107. **Exod 14:25** *Istaelitis* → *Israelitis*. 1738 *pro Iſraelitis* (leaf 129).
    **Apply:** `Exod.14.25` la: `pro Istaelitis` → `pro Israelitis`
108. **Exod 16:12** *et mane. Satiandos* → *et mane satiandos* (one sentence: “and in the morning be filled”). 1738 *et mane ſatiandos eſſe pane* (leaf 130).
    **Apply:** `Exod.16.12` la: `et mane. Satiandos` → `et mane satiandos`
109. **Exod 16:22** *retuliissent* → *retulissent*. 1738 *retulis-|ſent* (leaf 131).
    **Apply:** `Exod.16.22` la: `ad Mosem retuliissent` → `ad Mosem retulissent`
## 5. Found by the readings of stages 3–5 (11)

Suspected by the four layout and macron readers and checked in 1738's hOCR line (leaf given), on the page image for 6:3. Kept after checking: 15:19 *ingressus* (1738 *ingreſſus*), 12:5 *annulus*, 16:4 *pluturum*, 16:14 *in solo*, 20:21 *accessit* (no *Moses*), 16:31 *album*. Left to the spelling rules: 5:11 *undecunque* (1738 *vndecumque*), 12:25–26 *ceremonia* and 13:10 *cerimoniam* (1738 *cærimonia*), 18:13 *astaret* (1738 *adſtaret*). Not settled: 6:3 *nomen meum Jova non declaravi*, where a reader saw 1738's OCR as *Iouam*; the page image could not be cropped there, so the draft's *Jova* stays.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

110. **Exod 3:17** *ex Aegyptiis miseris* → *miseriis* (out of the Egyptian miseries). 1738 *ex aegyptiis mi-|ſeriis* (leaf 117).
    **Apply:** `Exod.3.17` la: `Aegyptiis miseris` → `Aegyptiis miseriis`
111. **Exod 3:19** *permitturum* → *permissurum*. 1738 *non permiſſu-|rum Aegypti regem* (leaf 117).
    **Apply:** `Exod.3.19` la: `non permitturum` → `non permissurum`
112. **Exod 5:10** *palea suppeditationem* → *paleae*. 1738 *eis paleae ſuppe-|ditationem* (leaf 118).
    **Apply:** `Exod.5.10` la: `eis palea suppeditationem` → `eis paleae suppeditationem`
113. **Exod 6:3** *a qui Abrahamo* → *qui Abrahamo*: the *a* is the arm of 1738's drop-cap *E* (of *Ego*, 6:2), which Wikisource took into the text. 1738 page image, leaf 119 (`sources/archive/crops/exod-6-3.jpg`), with the margin numbers 1 and 2 of Castellio's 6:1–2.
    **Apply:** `Exod.6.3` la: `a qui Abrahamo` → `qui Abrahamo`
114. **Exod 9:20** *ex Pharaonis Jovam minas* → *ex Pharaoniis Jovae minas* (those of Pharaoh's people who feared the LORD's threats). 1738 *ſi qui ex Pharaoniis Iouae minas timu-|erunt* (leaf 123).
    **Apply:** `Exod.9.20` la: `ex Pharaonis Jovam minas` → `ex Pharaoniis Jovae minas`
115. **Exod 10:10** *Jam jam latis perspicua malitia* → *Jam jam satis perspicua est vestra malitia* (two words missing). 1738 *Iam iam ſatis perſpicua eſt veſtra malitia* (leaf 124).
    **Apply:** `Exod.10.10` la: `Jam jam latis perspicua malitia` → `Jam jam satis perspicua est vestra malitia`
116. **Exod 12:23** *ad cedendos* → *ad caedendos* (to smite). 1738 *ad cædendos transibit* (leaf 126).
    **Apply:** `Exod.12.23` la: `ad cedendos` → `ad caedendos`
117. **Exod 12:43** *tradidit Jovae* → *tradidit Jova* (the LORD gave Moses and Aaron this rule). 1738 *Mosi et Aharo-|ni tradidit Ioua; ne quis* (leaf 126).
    **Apply:** `Exod.12.43` la: `tradidit Jovae` → `tradidit Jova`
118. **Exod 14:20** *inter Aegyptiis et Israelitica castra* → *Aegyptia*. 1738 *inter ægyptia et iſraelitica caſtra* (leaf 128).
    **Apply:** `Exod.14.20` la: `inter Aegyptiis et` → `inter Aegyptia et`
119. **Exod 14:31** *illustra* → *illustre* (with *factum*). 1738 *et tam illuſtre Iouæ contra illos factum* (leaf 129).
    **Apply:** `Exod.14.31` la: `illustra` → `illustre`
120. **Exod 18:14** *Eo re animadversa* → *Ea re*. 1738 *ea re animaduerſa ſocer eius ita dixit* (leaf 132).
    **Apply:** `Exod.18.14` la: `Eo re animadversa` → `Ea re animadversa`
