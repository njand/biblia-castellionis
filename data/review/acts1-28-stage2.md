# Acts 1–28, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-09 (decision 30's standing rule), on the New Testament route of John 5–21
(`data/review/john5-21-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 832–856). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's Acts as
  **`text/draft/ACT.usfm`** (BSB paragraphs).
- **Wikisource's Acts is Castellio's early wording** (with 1715, 1747, 1750 and 1760), which he revised in 1556 and
  again in 1573; 1758, 1681 and your 1726–27 text (`TXT/2 - Post-Corrected`, now a witness in `collate`) print the
  1573 text. So stage 2 here is mostly the revision, not typos: *synagoga* → *collegium* (23 places), *templum* →
  *fanum*, *homine natum* → *filium hominis*, *lavari* → *baptizari*, *baptismo lavit* → *baptismate baptizavit*,
  *fortunare* → *felicitare*, *fidem habere* → *credere*, and many smaller words.
- **Versification** (decision 5): 1573 prints every verse number. At 14 places Wikisource (the 1760 line) starts a
  verse a few words away from the number 1573 prints, where 1573 agrees with the KJV (2:7–8, 4:27–28, 4:34–35,
  9:33–34, 10:30–31, 11:6–7, 11:29–30, 14:14–15, 16:6–7, 17:6–7, 18:21–22, 27:27–28, 28:30–31), and it runs 16:38–39
  together; the boundaries now follow 1573. Three more follow the KJV where 1573 does not: 19:41 (*His ille
  dicendis …*, inside 1573's 19:40), and 24:2–3 and 24:21–22 (1573 has 28 verses in chapter 24, the KJV 27).
  31 edits in `data/versification/Acts.draft.edits.tsv`, applied: 1,007 verses, every chapter at the KJV count.
- **Collation** (`python -m pipeline collate Acts 1-28`; `data/calibration/Acts1-28-collation.tsv`): 1573 base;
  1556, 1758, 1681, 1715, 1747, 1750 and your 1726 as witnesses. Read on the page image: the 151 places where 1573
  and another printing agree against Wikisource, the 47 where two others do, and 30 of the 883 places where only
  1573's OCR differs (those where 1573's word is a real Latin word and the place is not a margin note), plus 26
  misspellings no lexicon knows and the verse starts and ends (collation does not see a word added or lost at a
  verse's edge: 9:2, 14:8, 16:13, 17:2 *Et*, 18:11–12). The crops are in `sources/mdz-1573/crops/` (`Acts.*`).
  Most of the 883 are 1573's OCR (*lesus*, *cos* for *eos*, nasal bars) or its margin notes run into the line
  (*Petri oratio*, *Christianorum omnia communia*, *Stephanus lapidatur*, *Herodis mors*, *Aratus*).
- **In all, 225 corrections**: 77 Wikisource slips (section 1), 124 readings of Castellio's revised text
  (section 2), 4 word divisions (section 3), 8 found on a second pass (section 2a) 8 while reading the verses (section 2b) and 4 found by the readers of 23–28 (section 2c). **Applied to the draft** (decision 30's standing rule). Spellings
  (*adsto/asto*, *auctor/autor*, *ancora/anchora*, *sepulcrum/sepulchrum*) are left to stage 3's rules.

## 1. Wikisource slips: 1573 and the other printings agree against it (77)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

1. **Acts 1:5** *Sapiritu* → *Spiritu*. 1573 *spiritu*; 1758, 1750, your 1726.
   **Apply:** `Acts.1.5` la: `Sapiritu` → `Spiritu`
2. **Acts 1:12** *Hiserosolyma* → *Hierosolyma*. 1573 *Hierosolyma*; 1556, 1758, your 1726.
   **Apply:** `Acts.1.12` la: `Hiserosolyma` → `Hierosolyma`
3. **Acts 1:15** *discipilorum* → *discipulorum*. 1573 *discipu-|lorum*; 1556, 1758, 1715, 1750, your 1726.
   **Apply:** `Acts.1.15` la: `discipilorum` → `discipulorum`
4. **Acts 1:21** *viroum* → *virorum*. 1573 *virorum*; 1556, 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.1.21` la: `viroum` → `virorum`
5. **Acts 1:23** *statuerunt, Josephus, nomine* → *statuerunt, Josephum nomine*. 1573 *Iosephum nomine*; 1556, 1758, 1750, your 1726.
   **Apply:** `Acts.1.23` la: `statuerunt, Josephus, nomine` → `statuerunt, Josephum nomine`
6. **Acts 2:10** *Pamphiliae* → *Pamphyliae*. 1573 *Pamphyliæ*; 1758.
   **Apply:** `Acts.2.10` la: `Pamphiliae` → `Pamphyliae`
7. **Acts 2:10** *Libiae* → *Libyae*. 1573 *Libyæ*; 1758, your 1726.
   **Apply:** `Acts.2.10` la: `Libiae` → `Libyae`
8. **Acts 2:30** *eesse* → *esse*. 1573 *esse*; 1715, your 1726.
   **Apply:** `Acts.2.30` la: `eesse` → `esse`
9. **Acts 2:37** *aloquuntur* → *alloquuntur*. 1573 *alloquuntur*; 1758, your 1726.
   **Apply:** `Acts.2.37` la: `aloquuntur` → `alloquuntur`
10. **Acts 3:11** *Iraque* → *Itaque*. 1573 *Itaque*; 1758, 1715, 1750, your 1726.
   **Apply:** `Acts.3.11` la: `Iraque` → `Itaque`
11. **Acts 5:17** *Itque* → *Itaque*. 1573 *Itaque*; 1758, your 1726.
   **Apply:** `Acts.5.17` la: `Itque` → `Itaque`
12. **Acts 5:32** *impetivit* → *impertivit*. 1573 *impertiuit*; 1556, 1758, your 1726.
   **Apply:** `Acts.5.32` la: `impetivit` → `impertivit`
13. **Acts 6:3** *discipite* → *dispicite*. 1573 *dispicite*; 1758, 1750, your 1726.
   **Apply:** `Acts.6.3` la: `discipite` → `dispicite`
14. **Acts 7:4** *Tum ille Chaldaeorum* → *Tum ille ex Chaldaeorum*. 1573 *Tum ille ex Chaldæorum terra*; 1758, 1715, 1747, 1750, your 1726.
   **Apply:** `Acts.7.4` la: `Tum ille Chaldaeorum` → `Tum ille ex Chaldaeorum`
15. **Acts 7:10** *tangam* → *tantam*. 1573 *tãtam*; 1758, 1715, 1747, your 1726.
   **Apply:** `Acts.7.10` la: `tangam` → `tantam`
16. **Acts 7:16** *Sichemis filii* → *Sichemi filii*. 1573 *Siche-|mi filij*; 1556, 1758, your 1726.
   **Apply:** `Acts.7.16` la: `Sichemis filii` → `Sichemi filii`
17. **Acts 7:31** *Ac eo visendum* → *Ac eo ad visendum*. 1573 *eo ad visendum*; 1556, 1758, 1750, your 1726.
   **Apply:** `Acts.7.31` la: `Ac eo visendum` → `Ac eo ad visendum`
18. **Acts 7:43** *ad orandum* → *ad adorandum*. 1573 *ad adorandum*; 1758, 1747, your 1726.
   **Apply:** `Acts.7.43` la: `ad orandum` → `ad adorandum`
19. **Acts 8:9** *magiam* → *magicam*. 1573 *magicam*; 1758, 1681, 1747, 1750, your 1726.
   **Apply:** `Acts.8.9` la: `magiam` → `magicam`
20. **Acts 8:11** *obtupefecerat* → *obstupefecerat*. 1573 OCR *obstupefecerat* (the word is on the line after the crop); 1556, your 1726.
   **Apply:** `Acts.8.11` la: `obtupefecerat` → `obstupefecerat`
21. **Acts 8:27** *eunuchs* → *eunuchus*. 1573 *eunuchus*; 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.8.27` la: `eunuchs` → `eunuchus`
22. **Acts 9:7** *comiter* → *comites*. 1573 *comites*; 1556, 1758, 1715, 1747, your 1726.
   **Apply:** `Acts.9.7` la: `comiter` → `comites`
23. **Acts 9:26** *disciuplos* → *discipulos*. 1573 *discipulos*; 1758, 1747, your 1726.
   **Apply:** `Acts.9.26` la: `disciuplos` → `discipulos`
24. **Acts 9:28** *observari* → *obversari*. 1573 *obuersari*; 1758, 1750, your 1726.
   **Apply:** `Acts.9.28` la: `observari` → `obversari`
25. **Acts 10:18** *diverssaretur* → *diversaretur*. 1573 *diuersaretur*; 1758, your 1726.
   **Apply:** `Acts.10.18` la: `diverssaretur` → `diversaretur`
26. **Acts 10:19** *homines et quaerunt* → *homines te quaerunt*. 1573 *homines te quærunt*; 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.10.19` la: `homines et quaerunt` → `homines te quaerunt`
27. **Acts 10:30** *vir quida stetit* → *vir quidam stetit*. 1573 *vir quidam stetit*; 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.10.30` la: `vir quida stetit` → `vir quidam stetit`
28. **Acts 10:35** *justititam* → *justitiam*. 1573 *iu-|stitiam*; 1758, 1747, your 1726.
   **Apply:** `Acts.10.35` la: `justititam` → `justitiam`
29. **Acts 10:36** *missit* → *misit*. 1573 *misit*; 1556, 1758, your 1726.
   **Apply:** `Acts.10.36` la: `missit` → `misit`
30. **Acts 11:18** *adquiverunt* → *adquieverunt*. 1573 *acquieuerunt* (ad-/ac- is the rules' business); Wikisource drops the e.
   **Apply:** `Acts.11.18` la: `adquiverunt` → `adquieverunt`
31. **Acts 11:22** *hierosolymatana* → *Hierosolymitana*. 1573 *Hierosolymitana*; 1758, 1747, 1750.
   **Apply:** `Acts.11.22` la: `hierosolymatana` → `Hierosolymitana`
32. **Acts 12:10** *simulae ac* → *simulac*. 1573 *simulac*; 1556, 1758, 1750.
   **Apply:** `Acts.12.10` la: `simulae ac` → `simulac`
33. **Acts 12:13** *vestribuli* → *vestibuli*. 1573 *vestibuli*; 1556, 1758, 1715, 1750.
   **Apply:** `Acts.12.13` la: `vestribuli` → `vestibuli`
34. **Acts 12:20** *cubilario* → *cubiculario*. 1573 *cubicu-|lario*; 1556, 1758.
   **Apply:** `Acts.12.20` la: `cubilario` → `cubiculario`
35. **Acts 13:19** *Canaea* → *Chananaea*. 1573 *Chananæa* (canvas 843, page image); 1758, 1750, your 1726.
   **Apply:** `Acts.13.19` la: `Canaea` → `Chananaea`
36. **Acts 13:25** *cuju* → *cujus*. 1573 *cuius*; 1556, 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.13.25` la: `cuju` → `cujus`
37. **Acts 13:36** *obdormivit, ad suos* → *obdormivit, et ad suos*. 1573 *obdormiuit, & ad suos*; 1758, 1715, 1750.
   **Apply:** `Acts.13.36` la: `obdormivit, ad suos` → `obdormivit, et ad suos`
38. **Acts 15:4** *apostlis* → *apostolis*. 1573 *apostolis*; 1556, 1758.
   **Apply:** `Acts.15.4` la: `apostlis` → `apostolis`
39. **Acts 15:22** *Tun visum* → *Tum visum*. 1573 *Tum*; 1758.
   **Apply:** `Acts.15.22` la: `Tun visum` → `Tum visum`
40. **Acts 15:23** *externarium* → *externarum*. 1573 *externarum*; 1556, 1758, 1747.
   **Apply:** `Acts.15.23` la: `externarium` → `externarum`
41. **Acts 15:29** *Abstinendunm* → *Abstinendum*. 1573 *abstinendum*; 1758, 1681, 1715.
   **Apply:** `Acts.15.29` la: `Abstinendunm` → `Abstinendum`
42. **Acts 16:22** *corum vestimentis* → *eorum vestimentis*. 1573 *eorum*; 1556, 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.16.22` la: `corum vestimentis` → `eorum vestimentis`
43. **Acts 17:4** *nonullis* → *nonnullis*. 1573 *nonnullis*; 1556.
   **Apply:** `Acts.17.4` la: `nonullis` → `nonnullis`
44. **Acts 17:10** *Berrhoeam dimiserunt pervenerunt, in Judaeorum se synagogam receperunt* → *Berrhoeam dimiserunt. Quo postquam illi pervenerunt, in Judaeorum se collegium receperunt*. 1573 *dimiserunt. Quò postquam illi peruenerunt, in Iudæorum se collegium receperunt* (canvas 846, fresh crop); 1758, 1747, 1750 *Quo postquam illi*; 1758 *collegium*. Wikisource lost four words and has the early *synagogam*.
   **Apply:** `Acts.17.10` la: `Berrhoeam dimiserunt pervenerunt, in Judaeorum se synagogam receperunt` → `Berrhoeam dimiserunt. Quo postquam illi pervenerunt, in Judaeorum se collegium receperunt`
45. **Acts 17:23** *in qua scriptum* → *in qua inscriptum*. 1573 *inscriptum*; 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.17.23` la: `in qua scriptum` → `in qua inscriptum`
46. **Acts 17:25** *quum ipse omnia denique* → *quum ipse omnibus vitam, flatum, omnia denique*. 1573 *cùm ipse omnibus vitam, flatum, omnia denique conferat*; 1747, 1750, your 1726: Wikisource dropped three words.
   **Apply:** `Acts.17.25` la: `quum ipse omnia denique` → `quum ipse omnibus vitam, flatum, omnia denique`
47. **Acts 17:28** *et moveamus* → *et moveamur*. 1573 *moueamur*; 1556, 1681, 1747, 1750, your 1726.
   **Apply:** `Acts.17.28` la: `et moveamus` → `et moveamur`
48. **Acts 17:29** *auro atque argento* → *auro aut argento*. 1573 *auro, aut argento, aut lapidi*; 1556, 1758, 1747, your 1726.
   **Apply:** `Acts.17.29` la: `auro atque argento` → `auro aut argento`
49. **Acts 18:3** *tentorium opifices* → *tentoriorum opifices*. 1573 *tentorio-|rum*; 1556, 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.18.3` la: `tentorium opifices` → `tentoriorum opifices`
50. **Acts 18:18** *transactis illis adhuc* → *transactis illic adhuc*. 1573 *illic*; 1556, 1758, 1747, 1750.
   **Apply:** `Acts.18.18` la: `transactis illis adhuc` → `transactis illic adhuc`
51. **Acts 18:22** *conscendit, ad degressus* → *conscendit, ac degressus*. 1573 *ac*; 1747, 1750.
   **Apply:** `Acts.18.22` la: `conscendit, ad degressus` → `conscendit, ac degressus`
52. **Acts 19:16** *illis effugerent* → *illis effugerint*. 1573 *effugerint*; 1758, your 1726.
   **Apply:** `Acts.19.16` la: `illis effugerent` → `illis effugerint`
53. **Acts 19:25** *hujumodi* → *hujusmodi*. 1573 *huiusmodi*; 1556, 1758.
   **Apply:** `Acts.19.25` la: `hujumodi` → `hujusmodi`
54. **Acts 19:29** *Aristarcho Macedonis* → *Aristarcho Macedonibus*. 1573 *Ma-|cedonibus*; 1758, 1747, 1750.
   **Apply:** `Acts.19.29` la: `Aristarcho Macedonis` → `Aristarcho Macedonibus`
55. **Acts 20:10** *multuari* → *tumultuari*. 1573 *tumultuari*; 1556, 1758, 1715, 1750.
   **Apply:** `Acts.20.10` la: `multuari` → `tumultuari`
56. **Acts 20:22** *mihi sic eventurum* → *mihi sit eventurum*. 1573 *sit*; 1556, 1758.
   **Apply:** `Acts.20.22` la: `mihi sic eventurum` → `mihi sit eventurum`
57. **Acts 20:32** *Deo et sermonis* → *Deo et sermoni*. 1573 *sermoni*; 1758, 1750.
   **Apply:** `Acts.20.32` la: `Deo et sermonis` → `Deo et sermoni`
58. **Acts 21:6** *consultavimus* → *consalutavimus*. 1573 *consalutauimus*; 1758, 1681, your 1726.
   **Apply:** `Acts.21.6` la: `consultavimus` → `consalutavimus`
59. **Acts 21:25** *immmolata* → *immolata*. 1573 *immolata*; 1758, 1750.
   **Apply:** `Acts.21.25` la: `immmolata` → `immolata`
60. **Acts 21:26** *unoquque* → *unoquoque*. 1573 *vnoquoq;*; 1758, 1715, 1750.
   **Apply:** `Acts.21.26` la: `unoquque` → `unoquoque`
61. **Acts 22:20** *consentirent* → *consentirem*. 1573 *consentirem*; 1758, 1747, 1750.
   **Apply:** `Acts.22.20` la: `consentirent` → `consentirem`
62. **Acts 23:8** *resurrecitonem* → *resurrectionem*. 1573 *resurrectionem*; 1758.
   **Apply:** `Acts.23.8` la: `resurrecitonem` → `resurrectionem`
63. **Acts 23:21** *intermissent* → *interemissent*. 1573 *interemis-|sent*; 1715, 1750.
   **Apply:** `Acts.23.21` la: `intermissent` → `interemissent`
64. **Acts 23:35** *jussit adversari* → *jussit adservari*. 1573 *iussit as-|seruari* (canvas 851, page image).
   **Apply:** `Acts.23.35` la: `jussit adversari` → `jussit adservari`
65. **Acts 24:2** *fruimus* → *fruimur*. 1573 *fruimur*; 1758, 1681, 1747, 1750.
   **Apply:** `Acts.24.2` la: `fruimus` → `fruimur`
66. **Acts 24:4** *Sed ne diutius, obtundam* → *Sed ne te diutius obtundam*. 1573 *Sed ne te diutius obtundam*; 1715, 1747.
   **Apply:** `Acts.24.4` la: `Sed ne diutius, obtundam` → `Sed ne te diutius obtundam`
67. **Acts 24:27** *accepi successorem* → *accepit successorem*. 1573 *accepit*; 1758, 1747, 1750.
   **Apply:** `Acts.24.27` la: `accepi successorem` → `accepit successorem`
68. **Acts 25:5** *in hoc nomine* → *in hoc homine*. 1573 *in hoc homine*; 1556, 1758, 1715, 1747, 1750.
   **Apply:** `Acts.25.5` la: `in hoc nomine` → `in hoc homine`
69. **Acts 25:8** *pecasse* → *peccasse*. 1573 *peccasse*; 1556, 1758, your 1726.
   **Apply:** `Acts.25.8` la: `pecasse` → `peccasse`
70. **Acts 25:25** *statui mittere* → *mittere statui*. 1573 *ad Augustum prouocasset, mittere statui:* (canvas 852, page image).
   **Apply:** `Acts.25.25` la: `statui mittere` → `mittere statui`
71. **Acts 27:23** *nac nocte* → *hac nocte*. 1573 *hac*; 1747.
   **Apply:** `Acts.27.23` la: `nac nocte` → `hac nocte`
72. **Acts 27:39** *animadverterbant* → *animadvertebant*. 1573 *animaduertebant*; 1758, 1747.
   **Apply:** `Acts.27.39` la: `animadverterbant` → `animadvertebant`
73. **Acts 27:43** *cneturio* → *centurio*. 1573 *cẽturio*; 1715, 1747, 1750, your 1726.
   **Apply:** `Acts.27.43` la: `cneturio` → `centurio`
74. **Acts 28:25** *vatme* → *vatem*. 1573 *vatem*; 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.28.25` la: `vatme` → `vatem`
75. **Acts 28:26** *adispicetis* → *adspicietis*. 1573 *aspicietis*; 1556, 1758, 1747, your 1726.
   **Apply:** `Acts.28.26` la: `adispicetis` → `adspicietis`
76. **Acts 28:30** *inconducto* → *in conducto*. 1573 *in condu-|cto*; 1758, your 1726.
   **Apply:** `Acts.28.30` la: `inconducto` → `in conducto`
77. **Acts 28:31** *liberatte* → *libertate*. 1573 *libertate*; 1758, your 1726.
   **Apply:** `Acts.28.31` la: `liberatte` → `libertate`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (124)

Wikisource reads with 1715, 1747 and 1750 (after the `|`), the early wording; 1573 with 1758 and usually your 1726
text. Where 1556 is not named it was not read (its OCR finds about half the words), or it reads with 1573.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

78. **Acts 1:8** *tota Judaea et Samaria* → *tota Judaea ac Samaria*. 1573 *ac*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.1.8` la: `tota Judaea et Samaria` → `tota Judaea ac Samaria`
79. **Acts 1:11** *dixerunt, viri galilaei,* → *dixerunt, galilaei,*. 1573 *qui ita dixerunt: Galilæi, quid statis*; 1758, your 1726 | 1556, 1715, 1747, 1750 *viri*.
   **Apply:** `Acts.1.11` la: `dixerunt, viri galilaei,` → `dixerunt, galilaei,`
80. **Acts 1:16** *illud scriptura mandatum* → *illud litteris mandatum*. 1573 *illud literis mandatum fieri*; 1758, your 1726 | 1750.
   **Apply:** `Acts.1.16` la: `illud scriptura mandatum` → `illud litteris mandatum`
81. **Acts 1:22** *Joannis baptismo* → *Joannis baptismate*. 1573 *Iohannis baptismate*; 1758, your 1726 | 1750.
   **Apply:** `Acts.1.22` la: `Joannis baptismo` → `Joannis baptismate`
82. **Acts 2:7** *et inter sese dictitabant: Nonne omnes illi,* → *et sic inter sese dictitabant: Nonne omnes hi,*. 1573 *& sic inter sese dictitabant: Nonne oẽs hi*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.2.7` la: `et inter sese dictitabant: Nonne omnes illi,` → `et sic inter sese dictitabant: Nonne omnes hi,`
83. **Acts 2:10** *secundum Cyrenem* → *secundum Cyrenen*. 1573 *secundũ Cyrenen*; 1758, your 1726 | 1556, 1715, 1747.
   **Apply:** `Acts.2.10` la: `secundum Cyrenem` → `secundum Cyrenen`
84. **Acts 2:34** *sede ad meam dexteram* → *sede ad dexteram meam*. 1573 OCR *sede ad dex[teram]*; 1758, your 1726 *dexteram meam*.
   **Apply:** `Acts.2.34` la: `sede ad meam dexteram` → `sede ad dexteram meam`
85. **Acts 2:35** *scabellum pedum tuorum* → *scabellum tuorum pedum*. 1573 *scabellũ tuorũ pedũ*; 1758, your 1726.
   **Apply:** `Acts.2.35` la: `scabellum pedum tuorum` → `scabellum tuorum pedum`
86. **Acts 2:38** *et baptizetur unusquisque vestrum in* → *et baptizamini cuncti in*. 1573 *& baptizamini cuncti in Iesu Christi nomine*; 1758, your 1726 | 1750.
   **Apply:** `Acts.2.38` la: `et baptizetur unusquisque vestrum in` → `et baptizamini cuncti in`
87. **Acts 2:38** *adsequemini* → *adsequimini*. 1573 *assequimini*; 1758, your 1726 | 1750.
   **Apply:** `Acts.2.38` la: `adsequemini` → `adsequimini`
88. **Acts 2:41** *ejus sermone avide admisso, baptizati sunt,* → *ejus oratione avide admissa, sunt baptizati,*. 1573 *eius oratione auide admissa, sunt baptizati*; 1758, your 1726 | 1715, 1750.
   **Apply:** `Acts.2.41` la: `ejus sermone avide admisso, baptizati sunt,` → `ejus oratione avide admissa, sunt baptizati,`
89. **Acts 2:45** *copias et facultates* → *copias ac facultates*. 1573 *ac*; 1758, your 1726 | 1715, 1750.
   **Apply:** `Acts.2.45` la: `copias et facultates` → `copias ac facultates`
90. **Acts 2:46** *in templo* → *in fano*. 1573 *in fano*; 1758, your 1726 | 1715, 1750.
   **Apply:** `Acts.2.46` la: `in templo` → `in fano`
91. **Acts 3:4** *intuitus dicit:* → *intuitus dixit:*. 1573 *di-|xit*; 1758, your 1726 | 1750.
   **Apply:** `Acts.3.4` la: `intuitus dicit:` → `intuitus dixit:`
92. **Acts 3:15** *excitavit ex mortuis* → *excitavit a mortuis*. 1573 *à mortuis*; 1758, your 1726 | 1750.
   **Apply:** `Acts.3.15` la: `excitavit ex mortuis` → `excitavit a mortuis`
93. **Acts 3:25** *fortunandas* → *felicitandas*. 1573 *felicitandas*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.3.25` la: `fortunandas` → `felicitandas`
94. **Acts 3:26** *fortunet* → *felicitet*. 1573 *felicitet*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.3.26` la: `fortunet` → `felicitet`
95. **Acts 4:1** *templi antistites* → *fani antistes*. 1573 *& fani antistes* (singular, clear); 1758, your 1726 | 1715, 1747.
   **Apply:** `Acts.4.1` la: `templi antistites` → `fani antistes`
96. **Acts 4:30** *sancti filii Jesu* → *sancti pueri Jesu*. 1573 *tui sancti pueri Iesu* (canvas 835, page image); 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.4.30` la: `sancti filii Jesu` → `sancti pueri Jesu`
97. **Acts 4:32** *qui crediderunt* → *qui crediderant*. 1573 *crediderãt*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.4.32` la: `qui crediderunt` → `qui crediderant`
98. **Acts 5:20** *in templo* → *in fano*. 1573 *fano*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.5.20` la: `in templo` → `in fano`
99. **Acts 5:21** *in templum* → *in fanum*. 1573 *fanum*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.5.21` la: `in templum` → `in fanum`
100. **Acts 5:31** *ad conciliandam* → *ad conciliandum*. 1573 *ad conciliandum … correctionem* (gerund); 1758, 1750, your 1726.
   **Apply:** `Acts.5.31` la: `ad conciliandam` → `ad conciliandum`
101. **Acts 6:5** *Placuit hic sermo* → *Placuit haec oratio*. 1573 *hæc oratio*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.6.5` la: `Placuit hic sermo` → `Placuit haec oratio`
102. **Acts 7:2** *nostro Abramo* → *nostro Abrahamo*. 1573 *Abrahamo*; 1758, 1715, your 1726 | 1750.
   **Apply:** `Acts.7.2` la: `nostro Abramo` → `nostro Abrahamo`
103. **Acts 7:11** *Aegyptum et Chananaeam orta fame ac angustia* → *Aegyptum ac Chananaeam orta fame atque angustia*. 1573 *Ægyptum ac Chananæam orta fame atq; angustia*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.7.11` la: `Aegyptum et Chananaeam orta fame ac angustia` → `Aegyptum ac Chananaeam orta fame atque angustia`
104. **Acts 7:32** *Abrami Deus* → *Abrahami Deus*. 1573 *Abrahami*; 1556, 1715, 1747, 1750, your 1726.
   **Apply:** `Acts.7.32` la: `Abrami Deus` → `Abrahami Deus`
105. **Acts 7:45** *introduxerunt, quum* → *introduxerunt tum, quum*. 1573 *introduxerunt tum, cùm fines occuparunt*; 1758, 1747, your 1726 | 1750.
   **Apply:** `Acts.7.45` la: `introduxerunt, quum` → `introduxerunt tum, quum`
106. **Acts 7:46** *Jacobaeorum* → *Jacobeorum*. 1573 *Iacobeorum* (plain e); 1758, your 1726.
   **Apply:** `Acts.7.46` la: `Jacobaeorum` → `Jacobeorum`
107. **Acts 7:49** *domum aedificabis?* → *domum aedificabitis?*. 1573 *ædificabitis*; 1758, 1747, 1750, your 1726.
   **Apply:** `Acts.7.49` la: `domum aedificabis?` → `domum aedificabitis?`
108. **Acts 7:56** *et homine natum* → *et filium hominis*. 1573 *filium hominis*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.7.56` la: `et homine natum` → `et filium hominis`
109. **Acts 8:2** *persecuti* → *prosecuti*. 1573 *prosecuti* | 1750.
   **Apply:** `Acts.8.2` la: `persecuti` → `prosecuti`
110. **Acts 8:5** *digressus* → *degressus*. 1573 *de-|gressus*; 1758, 1750.
   **Apply:** `Acts.8.5` la: `digressus` → `degressus`
111. **Acts 8:14** *Petrum et Joannem* → *Petrum ac Joannem*. 1573 *Petrum ac Iohannem*; 1556, 1758, your 1726 | 1681, 1747, 1750.
   **Apply:** `Acts.8.14` la: `Petrum et Joannem` → `Petrum ac Joannem`
112. **Acts 8:36** *quid me lavari* → *quid me baptizari*. 1573 *baptizari*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.8.36` la: `quid me lavari` → `quid me baptizari`
113. **Acts 9:1** *adgressus est pontificem* → *adgressus pontificem*. 1573 *aggressus pontificem* (no *est*); 1758, your 1726.
   **Apply:** `Acts.9.1` la: `adgressus est pontificem` → `adgressus pontificem`
114. **Acts 9:2** *Et petiit ab eo* → *petiit ab eo*. 1573 *petijt ab eo* (no *Et*: 9:1–2 one sentence); 1758, 1681, your 1726.
   **Apply:** `Acts.9.2` la: `Et petiit ab eo` → `petiit ab eo`
115. **Acts 9:2** *ad synagogas* → *ad collegia*. 1573 *ad collegia*; 1758, 1681, your 1726 | 1747, 1750.
   **Apply:** `Acts.9.2` la: `ad synagogas` → `ad collegia`
116. **Acts 9:20** *in synagogis* → *in collegiis*. 1573 *in collegijs*; 1758, your 1726 | 1715, 1750.
   **Apply:** `Acts.9.20` la: `in synagogis` → `in collegiis`
117. **Acts 9:24** *dies ac noctes* → *dies et noctes*. 1573 *dies & noctes*; 1556, 1758, your 1726 | 1681, 1715, 1747, 1750.
   **Apply:** `Acts.9.24` la: `dies ac noctes` → `dies et noctes`
118. **Acts 9:34** *sanet te* → *sanat te*. 1573 *sanat*; 1556, 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.9.34` la: `sanet te` → `sanat te`
119. **Acts 9:41** *Et ille eam porrecta manu adlevavit* → *Et ille porrecta manu, eam adlevavit*. 1573 *Et ille porrecta manu, eam alleuauit*; 1758, your 1726.
   **Apply:** `Acts.9.41` la: `Et ille eam porrecta manu adlevavit` → `Et ille porrecta manu, eam adlevavit`
120. **Acts 10:8** *Joppem* → *Joppen*. 1573 *Ioppen*; 1758, 1715, your 1726 (Greek accusative, as 10:5 *Joppen*).
   **Apply:** `Acts.10.8` la: `Joppem` → `Joppen`
121. **Acts 10:12** *et serpentes, aereae* → *et serpentes, et aereae*. 1573 *& serpentes, & aëreæ volucres*; 1750, your 1726.
   **Apply:** `Acts.10.12` la: `et serpentes, aereae` → `et serpentes, et aereae`
122. **Acts 10:17** *sciscitari* → *sciscitati*. 1573 *sciscitati*; 1758, 1715, your 1726 | 1750.
   **Apply:** `Acts.10.17` la: `sciscitari` → `sciscitati`
123. **Acts 10:19** *At Petro* → *Ac Petro*. 1573 *Ac Petro*; 1758, 1715, your 1726 | 1750.
   **Apply:** `Acts.10.19` la: `At Petro` → `Ac Petro`
124. **Acts 10:34** *Tum Petrus* → *Tunc Petrus*. 1573 *Tunc*; 1758, your 1726 | 1556, 1681, 1715, 1747, 1750.
   **Apply:** `Acts.10.34` la: `Tum Petrus` → `Tunc Petrus`
125. **Acts 10:37** *a Joanne baptismum* → *a Joanne baptisma*. 1573 *baptisma:*; 1758, your 1726 | 1715.
   **Apply:** `Acts.10.37` la: `a Joanne baptismum` → `a Joanne baptisma`
126. **Acts 10:38** *sacro Spiritu* → *sancto Spiritu*. 1573 *sancto spiritu*; 1758, your 1726 | 1556, 1715, 1747, 1750.
   **Apply:** `Acts.10.38` la: `sacro Spiritu` → `sancto Spiritu`
127. **Acts 10:47** *adepti sunt?* → *adepti sint?*. 1573 *adepti sint?*; your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.10.47` la: `adepti sunt?` → `adepti sint?`
128. **Acts 11:9** *tu ne pollue* → *ne tu pollue*. 1573 *ne tu pollue*; 1758, 1681, your 1726 | 1715, 1750.
   **Apply:** `Acts.11.9` la: `tu ne pollue` → `ne tu pollue`
129. **Acts 11:16** *baptizasse aqua* → *baptizavisse aqua*. 1573 *baptizauisse*; 1758 | 1750 (the base edition's form, as John 9:7 *lōtum*).
   **Apply:** `Acts.11.16` la: `baptizasse aqua` → `baptizavisse aqua`
130. **Acts 12:11** *nunc vero scio* → *nunc vere scio*. 1573 *Nunc verè scio*; 1758, 1715, 1747 | 1750.
   **Apply:** `Acts.12.11` la: `nunc vero scio` → `nunc vere scio`
131. **Acts 12:15** *insanire dixere* → *insanire dicere*. 1573 *dicere* (clear; a historic infinitive, as 2:6 *vulgo convenire*, 17:6 *trahere*); 1747 | 1750.
   **Apply:** `Acts.12.15` la: `insanire dixere` → `insanire dicere`
132. **Acts 13:2** *operantibus et jejunantibus* → *operantibus ac jejunantibus*. 1573 *ac*; 1758 | 1750.
   **Apply:** `Acts.13.2` la: `operantibus et jejunantibus` → `operantibus ac jejunantibus`
133. **Acts 13:5** *in Judaeorum synagogis* → *in Judaeorum collegiis*. 1573 *collegijs*; 1758 | 1715, 1750.
   **Apply:** `Acts.13.5` la: `in Judaeorum synagogis` → `in Judaeorum collegiis`
134. **Acts 13:11** *manu duceret* → *manu ducerent*. 1573 *ducerent*; 1758 | 1556, 1715, 1747, 1750.
   **Apply:** `Acts.13.11` la: `manu duceret` → `manu ducerent`
135. **Acts 13:14** *et in synagogam sabbati* → *et collegium sabbati*. 1573 *& collegium Sabbati die ingressi* (no *in*); 1758 | 1747, 1750.
   **Apply:** `Acts.13.14` la: `et in synagogam sabbati` → `et collegium sabbati`
136. **Acts 13:15** *synagogae magistri* → *collegii magistri*. 1573 *collegij*; 1758 | 1747, 1750.
   **Apply:** `Acts.13.15` la: `synagogae magistri` → `collegii magistri`
137. **Acts 13:16** *usus est: Israelitae* → *usus est: Viri Israelitae*. 1573 *Viri Israelitæ*; 1758 | 1747, 1750.
   **Apply:** `Acts.13.16` la: `usus est: Israelitae` → `usus est: Viri Israelitae`
138. **Acts 13:21** *tribu benjaminia* → *tribu Benjaminia*. 1573 *Bẽiaminia* (capital); 1758, your 1726.
   **Apply:** `Acts.13.21` la: `tribu benjaminia` → `tribu Benjaminia`
139. **Acts 13:29** *eum ex patibulo* → *eum patibulo*. 1573 *eum patibulo detractum*; 1556, 1758, your 1726 | 1747.
   **Apply:** `Acts.13.29` la: `eum ex patibulo` → `eum patibulo`
140. **Acts 13:42** *ex Judaeorum synagoga* → *ex Judaeorum collegio*. 1573 *collegio*; your 1726 | 1747, 1750.
   **Apply:** `Acts.13.42` la: `ex Judaeorum synagoga` → `ex Judaeorum collegio`
141. **Acts 13:50** *religiosis ac honestis* → *religiosis honestisque*. 1573 *religiosis honestisque fœminis*; 1758, your 1726 | 1750.
   **Apply:** `Acts.13.50` la: `religiosis ac honestis` → `religiosis honestisque`
142. **Acts 14:1** *in Judaeorum synagogam* → *in Judaeorum collegium*. 1573 *collegium*.
   **Apply:** `Acts.14.1` la: `in Judaeorum synagogam` → `in Judaeorum collegium`
143. **Acts 14:7** *Et illic evangelium docent:* → *Illic dum evangelium docent,*. 1573 *Illic dum Euangelium docent,*, running on into 14:8; your 1726 *dum* | 1747, 1750.
   **Apply:** `Acts.14.7` la: `Et illic evangelium docent:` → `Illic dum evangelium docent,`
144. **Acts 14:8** *Et homo quidam* → *homo quidam*. 1573 *homo quidam* (no *Et*); 1758, your 1726.
   **Apply:** `Acts.14.8` la: `Et homo quidam` → `homo quidam`
145. **Acts 14:15** *ad Deum vos immortalem convertatis* → *ad Deum illum viventem vos convertatis*. 1573 *ad Deum illum viuentem vos conuertatis*; 1758 | 1556, 1747, 1750 *immortalem*.
   **Apply:** `Acts.14.15` la: `ad Deum vos immortalem convertatis` → `ad Deum illum viventem vos convertatis`
146. **Acts 15:4** *quae secum Deus fecisset* → *quae Deus secum fecisset*. 1573 *& quæ Deus secum fecisset*; 1556, 1758.
   **Apply:** `Acts.15.4` la: `quae secum Deus fecisset` → `quae Deus secum fecisset`
147. **Acts 15:11** *per Domini nostri Jesu* → *per Domini Jesu*. 1573 *per Domini Iesu Christi gratiam*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.15.11` la: `per Domini nostri Jesu` → `per Domini Jesu`
148. **Acts 15:14** *Narravit Simon* → *Narravit Simeon*. 1573 *Simeon*; 1758, 1747, your 1726 | 1750.
   **Apply:** `Acts.15.14` la: `Narravit Simon` → `Narravit Simeon`
149. **Acts 15:21** *per synagogas* → *per collegia*. 1573 *collegia*; 1556, 1758 | 1747, 1750.
   **Apply:** `Acts.15.21` la: `per synagogas` → `per collegia`
150. **Acts 15:29** *recte facietis.* → *recte facietis. Valete.*. 1573 ends the letter *rectè facietis. Valete.*.
   **Apply:** `Acts.15.29` la: `recte facietis.` → `recte facietis. Valete.`
151. **Acts 15:38** *profectus esset* → *profectus fuisset*. 1573 *fuisset*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.15.38` la: `profectus esset` → `profectus fuisset`
152. **Acts 16:12** *colonia. Eramus autem in ea urbe dies* → *colonia. In ea urbe nos dies*. 1573 *In ea vrbe nos dies aliquot agentes*; 1556, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.16.12` la: `colonia. Eramus autem in ea urbe dies` → `colonia. In ea urbe nos dies`
153. **Acts 16:13** *Et die sabbato* → *die sabbato*. 1573 *die Sabbato* (no *Et*); 1758.
   **Apply:** `Acts.16.13` la: `Et die sabbato` → `die sabbato`
154. **Acts 16:15** *judicaremus* → *judicaveramus*. 1573 *iudicaueramus*; 1758 | 1747, 1750.
   **Apply:** `Acts.16.15` la: `judicaremus` → `judicaveramus`
155. **Acts 16:30** *dixit: Domine,* → *dixit: Domini,*. 1573 *Domini* (plural vocative, 'Sirs'); 1758, 1747.
   **Apply:** `Acts.16.30` la: `dixit: Domine,` → `dixit: Domini,`
156. **Acts 16:31** *fidem habe Domino Jesu* → *crede in Dominum Jesum*. 1573 *Crede in Dominum Iesum*; 1758 | 1556, 1747 *fidem habe*.
   **Apply:** `Acts.16.31` la: `fidem habe Domino Jesu` → `crede in Dominum Jesum`
157. **Acts 16:38** *et illi timuerunt* → *et illi territi*. 1573 *territi*; your 1726 | 1747, 1750.
   **Apply:** `Acts.16.38` la: `et illi timuerunt` → `et illi territi`
158. **Acts 16:39** *juveruntque eos* → *iverunt eos*. 1573 *iuerunt eos oratum*; 1758, your 1726 | 1747, 1750 *Iueruntque*.
   **Apply:** `Acts.16.39` la: `juveruntque eos` → `iverunt eos`
159. **Acts 17:1** *ubi erat Judaeorum synagoga* → *ubi cum esset Judaeorum collegium*. 1573 *vbi cùm esset Iudæorum collegium*, the sentence running on into 17:2.
   **Apply:** `Acts.17.1` la: `ubi erat Judaeorum synagoga` → `ubi cum esset Judaeorum collegium`
160. **Acts 17:2** *Et Paulus more* → *Paulus more*. 1573 *Paulus more suo* (no *Et*); 1758.
   **Apply:** `Acts.17.2` la: `Et Paulus more` → `Paulus more`
161. **Acts 17:3** *utque is esset* → *utque esset*. 1573 *vtq; esset Christus Iesus*; 1758 | 1715, 1747, 1750.
   **Apply:** `Acts.17.3` la: `utque is esset` → `utque esset`
162. **Acts 17:13** *Berrhoeae explicatum* → *Berrhoeae explicatam*. 1573 *explicatam* (with *doctrinam*); 1758 | 1750.
   **Apply:** `Acts.17.13` la: `Berrhoeae explicatum` → `Berrhoeae explicatam`
163. **Acts 17:17** *in synagoga* → *in collegio*. 1573 *collegio*; 1758 | 1747.
   **Apply:** `Acts.17.17` la: `in synagoga` → `in collegio`
164. **Acts 18:4** *in synagoga* → *in collegio*. 1573 *collegio*; 1758, your 1726 | 1747.
   **Apply:** `Acts.18.4` la: `in synagoga` → `in collegio`
165. **Acts 18:11** *Egit autem illic annum unum, et sex menses, divinam disciplinam eos docens.* → *Postquam autem illic annum unum et sex menses egit, divinam disciplinam eos docens,*. 1573 *Postquam autem illic annum vnum & sex menses egit, diuinam disciplinam eos docens,* (canvases 846–847, page image); 1758.
   **Apply:** `Acts.18.11` la: `Egit autem illic annum unum, et sex menses, divinam disciplinam eos docens.` → `Postquam autem illic annum unum et sex menses egit, divinam disciplinam eos docens,`
166. **Acts 18:12** *Tum Judaei* → *Judaei*. 1573 *Iudæi, Gallione …* (no *Tum*: 18:11–12 one sentence; page image); 1758 | 1747.
   **Apply:** `Acts.18.12` la: `Tum Judaei` → `Judaei`
167. **Acts 18:12** *produxerunt* → *perduxerunt*. 1573 *perduxerunt* (page image); 1758 | 1747, 1750.
   **Apply:** `Acts.18.12` la: `produxerunt` → `perduxerunt`
168. **Acts 18:26** *in synagoga* → *in collegio*. 1573 *collegio*; 1758 | 1715, 1747, 1750.
   **Apply:** `Acts.18.26` la: `in synagoga` → `in collegio`
169. **Acts 19:3** *Joannis baptismo* → *Joannis baptismate*. 1573 *baptis-|mate*; 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.19.3` la: `Joannis baptismo` → `Joannis baptismate`
170. **Acts 19:4** *baptismo lavit, vulgo monens, ut venienti post se fidem haberent, hoc est, Christo Jesu.* → *baptismate baptizavit, vulgo monens, ut in venientem post se crederent, hoc est, in Christum Jesum.*. 1573 *baptismate baptizauit, … vt in venientem post se crederent, hoc est in Christum Iesum*; 1758, your 1726 | 1556 (*venienti*), 1715, 1747, 1750.
   **Apply:** `Acts.19.4` la: `baptismo lavit, vulgo monens, ut venienti post se fidem haberent, hoc est, Christo Jesu.` → `baptismate baptizavit, vulgo monens, ut in venientem post se crederent, hoc est, in Christum Jesum.`
171. **Acts 19:8** *in synagogam* → *in collegium*. 1573 *collegium*; 1758, your 1726.
   **Apply:** `Acts.19.8` la: `in synagogam` → `in collegium`
172. **Acts 19:16** *nudi ac vulnerati* → *nudi et vulnerati*. 1573 *nudi & vulnerati*; 1758, your 1726 | 1750.
   **Apply:** `Acts.19.16` la: `nudi ac vulnerati` → `nudi et vulnerati`
173. **Acts 20:21** *Domino Jesu nostro* → *Domino nostro Jesu*. 1573 *& Domino nostro Iesu* (fresh crop, canvas 848); 1758 | 1556, 1681, 1750.
   **Apply:** `Acts.20.21` la: `Domino Jesu nostro` → `Domino nostro Jesu`
174. **Acts 21:2** *in Phoenicem* → *in Phoenicen*. 1573 *Phœnicen* (Greek accusative, as *Cyrenen*, *Joppen*).
   **Apply:** `Acts.21.2` la: `in Phoenicem` → `in Phoenicen`
175. **Acts 21:32** *viso tribuno ac militibus* → *viso tribuno et militibus*. 1573 *&*; 1758, 1681 | 1715, 1747, 1750.
   **Apply:** `Acts.21.32` la: `viso tribuno ac militibus` → `viso tribuno et militibus`
176. **Acts 22:19** *per synagogas* → *per collegia*. 1573 *per collegia*; 1758 | 1715, 1750.
   **Apply:** `Acts.22.19` la: `per synagogas` → `per collegia`
177. **Acts 22:26** *quid sis acturus* → *quid agas*. 1573 *quid agas*; 1758 | 1715, 1747, 1750.
   **Apply:** `Acts.22.26` la: `quid sis acturus` → `quid agas`
178. **Acts 23:13** *fecerant* → *fecerunt*. 1573 *fecerunt*; 1556, 1758, your 1726 | 1747, 1750.
   **Apply:** `Acts.23.13` la: `fecerant` → `fecerunt`
179. **Acts 23:15** *ut de eo cognituros* → *tamquam de eo cognituros*. 1573 *tanquam*; 1758, your 1726 | 1715, 1747.
   **Apply:** `Acts.23.15` la: `ut de eo cognituros` → `tamquam de eo cognituros`
180. **Acts 23:18** *abducerem* → *adducerem*. 1573 *adducerem*; 1715, 1747 | 1750.
   **Apply:** `Acts.23.18` la: `abducerem` → `adducerem`
181. **Acts 23:19** *ac in secretum* → *inque secretum*. 1573 *inque secretum ducto*; 1758, your 1726 | 1715, 1750.
   **Apply:** `Acts.23.19` la: `ac in secretum` → `inque secretum`
182. **Acts 23:31** *adsumptum noctu* → *adsumptum Paulum noctu*. 1573 *assumptum Paulum*; 1758, 1715, 1747 | 1750.
   **Apply:** `Acts.23.31` la: `adsumptum noctu` → `adsumptum Paulum noctu`
183. **Acts 24:4** *pro tua aequitate* → *pro aequitate tua*. 1573 *pro æquitate tua*.
   **Apply:** `Acts.24.4` la: `pro tua aequitate` → `pro aequitate tua`
184. **Acts 24:12** *in synagogis* → *in collegiis*. 1573 *collegijs*; 1758, 1681, your 1726 | 1747.
   **Apply:** `Acts.24.12` la: `in synagogis` → `in collegiis`
185. **Acts 24:17** *et ferta obmoverem* → *et munera libarem*. 1573 *& munera libarem* (canvas 851, page image); 1758, your 1726 | 1715, 1750.
   **Apply:** `Acts.24.17` la: `et ferta obmoverem` → `et munera libarem`
186. **Acts 24:20** *dum adsto* → *dum starem*. 1573 *dum starem*; 1758, 1681 | 1750.
   **Apply:** `Acts.24.20` la: `dum adsto` → `dum starem`
187. **Acts 24:23** *Paulus, remissius* → *Paulus, et remissius*. 1573 *Paulus, & remissius*; 1758, 1715, 1750.
   **Apply:** `Acts.24.23` la: `Paulus, remissius` → `Paulus, et remissius`
188. **Acts 24:23** *aut audire* → *aut adire*. 1573 *adire*; 1556, 1715, 1747 | 1750.
   **Apply:** `Acts.24.23` la: `aut audire` → `aut adire`
189. **Acts 25:6** *apud eos supra decem* → *apud eos non plus decem*. 1573 *non plus*; 1758, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.25.6` la: `apud eos supra decem` → `apud eos non plus decem`
190. **Acts 25:10** *ut tute pulchre* → *ut tu pulchre*. 1573 *vt tu*; 1758, 1681, your 1726 | 1715, 1747, 1750.
   **Apply:** `Acts.25.10` la: `ut tute pulchre` → `ut tu pulchre`
191. **Acts 25:19** *quaestiones quaedam* → *quaestiones quasdam*. 1573 *quasdã*; 1747, 1750.
   **Apply:** `Acts.25.19` la: `quaestiones quaedam` → `quaestiones quasdam`
192. **Acts 26:11** *per omnes synagogas* → *per omnia collegia*. 1573 *per omnia collegia* (canvas 852, page image); 1556, 1758 | 1747, 1750.
   **Apply:** `Acts.26.11` la: `per omnes synagogas` → `per omnia collegia`
193. **Acts 26:12** *cum potestate mihi a pontificibus praemissa* → *cum potestate et procuratione a pontificibus accepta*. 1573 *cum potestate & procuratione à Pontificibus accepta* (canvas 852, page image); 1758 | 1750; 1556 OCR *permissa*.
   **Apply:** `Acts.26.12` la: `cum potestate mihi a pontificibus praemissa` → `cum potestate et procuratione a pontificibus accepta`
194. **Acts 27:1** *alii quidam vincti, centurioni* → *alii quidam vincti duo, centurioni*. 1573 *vincti duo*.
   **Apply:** `Acts.27.1` la: `alii quidam vincti, centurioni` → `alii quidam vincti duo, centurioni`
195. **Acts 27:24** *oportet: ac scito* → *oportet: at scito*. 1573 *at*; 1758 | 1681, 1747, 1750.
   **Apply:** `Acts.27.24` la: `oportet: ac scito` → `oportet: at scito`
196. **Acts 27:27** *quod sibi ad aliquam terram accedere videbantur* → *quod se alicui terrae propinquare suspicabantur*. 1573 *alicui terræ propinquare suspicabantur* (*se* before it at the crop's edge; OCR *se*) | 1750.
   **Apply:** `Acts.27.27` la: `quod sibi ad aliquam terram accedere videbantur` → `quod se alicui terrae propinquare suspicabantur`
197. **Acts 28:4** *inter sese* → *inter se*. 1573 *inter se*; 1758, 1715, 1747, your 1726 | 1750.
   **Apply:** `Acts.28.4` la: `inter sese` → `inter se`
198. **Acts 28:7** *Erant autem iis* → *Erant iis*. 1573 *Erant ijs in locis*; 1758, 1681 | 1556, 1715, 1747, 1750.
   **Apply:** `Acts.28.7` la: `Erant autem iis` → `Erant iis`
199. **Acts 28:17** *in manus Romanorum* → *in Romanorum manus*. 1573 *in Romanorum manus*; 1758, 1750.
   **Apply:** `Acts.28.17` la: `in manus Romanorum` → `in Romanorum manus`
200. **Acts 28:23** *complures* → *plures*. 1573 *plures*; 1758 | 1681, 1747.
   **Apply:** `Acts.28.23` la: `complures` → `plures`
201. **Acts 28:27** *animus illius populi* → *animus istius populi*. 1573 *istius*; 1758, your 1726 | 1750.
   **Apply:** `Acts.28.27` la: `animus illius populi` → `animus istius populi`

## 3. Word division (4)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

202. **Acts 5:36** *quot, quot ei* → *quotquot ei*. 1573 *quotquot*; 1556, 1758, 1747, 1750, your 1726; your settled *quotquot* 7×.
   **Apply:** `Acts.5.36` la: `quot, quot ei` → `quotquot ei`
203. **Acts 6:3** *Quo circa* → *Quocirca*. 1573 *Quocirca*; 1758, your 1726 (Gaffiot *quōcircā*).
   **Apply:** `Acts.6.3` la: `Quo circa` → `Quocirca`
204. **Acts 9:43** *aliquammultos* → *aliquam multos*. 1573 *aliquàm multos*; 1758, 1747, 1750, your 1726 (as 18:18 *aliquam multis*).
   **Apply:** `Acts.9.43` la: `aliquammultos` → `aliquam multos`
205. **Acts 26:3** *vel inprimis* → *vel in primis*. 1573 *in primis*; 1556, 1758, 1715, 1747, as your settled *in prīmīs*.
   **Apply:** `Acts.26.3` la: `vel inprimis` → `vel in primis`

## 2a. Found after the first pass: the same, where the collation had sorted the place as a spelling or noise (8)

Six *synagoga* places the collation did not list (1573, 1758 and your 1726 have *collegium*), and two name slips.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

206. **Acts 6:9** *ex ea synagoga, quae Libertinorum* → *ex eo collegio, quod Libertinorum*. 1573 *ex eo collegio, quod Libertinorum appellatur* (canvas 837, page image); 1758, your 1726.
   **Apply:** `Acts.6.9` la: `ex ea synagoga, quae Libertinorum` → `ex eo collegio, quod Libertinorum`
207. **Acts 7:2** *antequam Charae habitasset* → *antequam Charrae habitasset*. 1573 *Charræ*; 1750, your 1726 (as 7:4 *Charrae*).
   **Apply:** `Acts.7.2` la: `antequam Charae habitasset` → `antequam Charrae habitasset`
208. **Acts 13:13** *Pamphiliae* → *Pamphyliae*. 1573 *Pamphyliæ*; 1758, 1747 (as 2:10, 15:38).
   **Apply:** `Acts.13.13` la: `Pamphiliae` → `Pamphyliae`
209. **Acts 13:43** *Ac dimissa synagoga* → *Ac dimisso collegio*. 1573 *Ac dimisso collegio* (canvas 843, page image); 1758, your 1726.
   **Apply:** `Acts.13.43` la: `Ac dimissa synagoga` → `Ac dimisso collegio`
210. **Acts 18:7** *contiguae synagogae* → *contiguae collegio*. 1573 *contiguæ collegio* (canvas 846, page image); 1758.
   **Apply:** `Acts.18.7` la: `contiguae synagogae` → `contiguae collegio`
211. **Acts 18:8** *synagogae magister* → *collegii magister*. 1573 *collegij magister* (canvas 846, page image); 1758.
   **Apply:** `Acts.18.8` la: `synagogae magister` → `collegii magister`
212. **Acts 18:17** *synagogae magistrum* → *collegii magistrum*. 1573 *collegij magistrum* (canvas 847, page image); 1758.
   **Apply:** `Acts.18.17` la: `synagogae magistrum` → `collegii magistrum`
213. **Acts 18:19** *in synagogam ingressus* → *in collegium ingressus*. 1573 *in col-|legium ingressus* (canvas 847, page image); 1758.
   **Apply:** `Acts.18.19` la: `in synagogam ingressus` → `in collegium ingressus`

## 2b. Found while reading the verses (8)

Slips the collation cannot see: a u for v (the j/v rule leaves *aluo*, *soluimus* alone), long s against f, and two the readers noticed.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09)

214. **Acts 2:16** *a Joële vate* → *a Joele vate*. 1573 *à Ioele*; 1758, your 1726. Wikisource's diaeresis made the approved *oe* → *œ* rule write *Jœle*; *Jōēle* (Ἰωήλ) is decided in stage 3.
   **Apply:** `Acts.2.16` la: `a Joële vate` → `a Joele vate`
215. **Acts 3:2** *ab aluo matris* → *ab alvo matris*. 1573 *ab aluo* (= *alvo*: u for v; canvas 834, page image); 1758, your 1726 *alvo*.
   **Apply:** `Acts.3.2` la: `ab aluo matris` → `ab alvo matris`
216. **Acts 3:2** *ad sani portam* → *ad fani portam*. 1573 *ad fani portam* (canvas 834, page image); 1758, your 1726. The collation sets f and long s alike, so this was found in reading (the temple gate, as *fanum* in 3:1).
   **Apply:** `Acts.3.2` la: `ad sani portam` → `ad fani portam`
217. **Acts 10:1** *Caesaraeae* → *Caesareae*. 1573 *Cæsareæ*; 1758, your 1726 (as 8:40 *Caesaream*).
   **Apply:** `Acts.10.1` la: `Caesaraeae` → `Caesareae`
218. **Acts 15:2** *ob eam questionem* → *ob eam quaestionem*. the spelling of 22:24 *quaestionem* and of 1573 at 22:29 (1573 not read here).
   **Apply:** `Acts.15.2` la: `ob eam questionem` → `ob eam quaestionem`
219. **Acts 16:11** *Ergo soluimus* → *Ergo solvimus*. 1573 *soluimus* (= *solvimus*, u for v); 1758, your 1726 *solvimus*.
   **Apply:** `Acts.16.11` la: `Ergo soluimus` → `Ergo solvimus`
220. **Acts 21:33** *quidue* → *quidve*. 1573 *quidue* (= *quidve*, u for v); 1758 *quidve*.
   **Apply:** `Acts.21.33` la: `quidue` → `quidve`
221. **Acts 22:29** *de eo questionem* → *de eo quaestionem*. 1573 *quæstionem*; 1758.
   **Apply:** `Acts.22.29` la: `de eo questionem` → `de eo quaestionem`

## 2c. Found by the readers in Acts 23–28 (4)

Three where 1573 differs and the other printings' OCR reads with it but not letter for letter, so the collation did not count them as agreeing (a later sweep for that pattern found no others), and one name.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09)

222. **Acts 24:1** *contra Paulum comparaverunt* → *contra Paulum comparuerunt*. 1573 *compa-|erunt* (canvas 851, page image: a syllable dropped at the line break); 1758, 1681 *comparuerunt* ('appeared against Paul').
   **Apply:** `Acts.24.1` la: `contra Paulum comparaverunt` → `contra Paulum comparuerunt`
223. **Acts 27:2** *navi adramitina* → *navi Adramyttina*. 1573 *Adramyttina*; 1556, 1758 (Ἀδραμυττηνῷ).
   **Apply:** `Acts.27.2` la: `navi adramitina` → `navi Adramyttina`
224. **Acts 27:13** *adsecutos, Assum praetervecti Cretam* → *adsecutos, solverunt, et propius Cretam*. 1573 *assecutos, soluerunt, & propius Cretam præterferebantur* (canvas 853, page image); 1758, 1681 | 1750 and Wikisource the early wording.
   **Apply:** `Acts.27.13` la: `adsecutos, Assum praetervecti Cretam` → `adsecutos, solverunt, et propius Cretam`
225. **Acts 27:14** *in eam verticosus ventus* → *in eam procellosus ventus*. 1573 *proc-|ellosus* (OCR *procellosus*; the page image is cut after *proc*, canvas 853); 1758, 1681.
   **Apply:** `Acts.27.14` la: `in eam verticosus ventus` → `in eam procellosus ventus`

## 4. Checked and kept

- **13:19** *dedit eis possidendam*: 1573 prints *dedi eis* (canvas 843, read twice on the page image), but Paul is
  telling of God in the third person (*Deus … ēlēgit … tulit … dedit*), and 1758, 1747 and your 1726 have *dedit*: a
  misprint in 1573, not followed.
- **19:29, 20:4** *Gāius*: 1573 prints *Caio*, *Caius* (with 1758, 1681, 1715). The same name; *Gaius* is the classical
  spelling (Gaffiot *Gāius*, decision 18). Kept.
- **22:15** *audieris* (1573 *audiveris*): the short perfect, decision 19.
- **4:14, 4:32, 5:3, 5:40, 7:12, 7:59, 8:16, 8:18, 9:5, 10:22, 10:26, 11:12, 11:22, 12:23, 14:14, 16:3, 18:2, 19:11,
  20:36, 22:23, 22:25, 23:8, 25:12, 27:34**: 1573's OCR (*lesus*, *ed* for *eò*, *hono*) or a margin note; the page
  reads as the draft.
- **2:10** 1573 ends verse 9 at *Phrygiæ* and starts 10 at *& Pamphyliæ*; the KJV has Phrygia in verse 10, as
  Wikisource. Kept as the KJV (decision 5).
- **17:4** *nec non*: 1573 prints *necnon*, but your settled chapters write *nec nōn* (14 times). Kept.
- **28:31** *Et dē Dominō* after a comma: a capital inside the verse, left to the layout (stage 5).

## 5. Recorded variants: 1556 against 1573

Where 1556 (with the early-line printings) reads otherwise than 1573, now the text. Recorded, not applied (decision
24). 1556 is cited from its OCR (e-rara 10281656), not the page image.

| Place | 1573 (= the text now) | 1556 | Also |
|---|---|---|---|
| Acts 1:11 | *dīxērunt: Galilæī* | *virī Galilæī* | 1715, 1747, 1750 |
| Acts 2:10 | *Cyrēnēn* | *Cyrenem* | 1715, 1747 |
| Acts 10:34 | *Tunc Petrus* | *Tum* | 1681, 1715, 1747, 1750 |
| Acts 10:38 | *sānctō Spīritū* | *sacro* | 1715, 1747, 1750 |
| Acts 13:11 | *quī sē manū dūcerent* | *duceret* | 1715, 1747, 1750 |
| Acts 14:15 | *ad Deum illum vīventem* | *ad Deum … immortalem* | 1747, 1750 |
| Acts 16:31 | *Crēde in Dominum Jēsum* | *fidem habe Domino Iesu* | 1747 |
| Acts 19:4 | *in venientem* | *venienti* | 1715, 1747, 1750 |
| Acts 20:21 | *Dominō nostrō Jēsū* | *Domino Iesu nostro* | 1681, 1750 |
| Acts 26:12 | *ā Pontificibus acceptā* | *permissa* | (1750 *praemissa*) |
| Acts 28:7 | *Erant iīs in locīs* | *Erant autem* | 1715, 1747, 1750 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-09)
