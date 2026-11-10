# Romans 1–16, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-09 (decision 30's standing rule), on the route of Acts (`data/review/acts1-28-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 856–866). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's Romans as
  **`text/draft/ROM.usfm`** (BSB paragraphs). You have no earlier work on Romans; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected; it holds Athanasius' argument and the first chapters) is the witness
  `1726`, read as an OCR.
- **Wikisource's Romans is Castellio's early wording**, as its Acts: *humanitas* and *humana natura* for σάρξ (9:3,
  9:5, 9:8), *vitiositas* for ἁμαρτία (7:17, 7:20, 7:23), *scripturae* (15:4), *sacer* for ἅγιος (11:16, 12:1),
  *animus* for καρδία (2:29), *praevidit* (8:29). 1556 already has the revised words where its OCR can be read; 1573
  keeps them. *Favor* (16:20, 16:24) and *humana natura* at 4:1 and 6:19 stay: 1573 prints them too.
- **Versification** (decision 5): 1573 prints every verse number, but in chapters 3 and 8 it numbers the old way,
  one verse fewer than the KJV. 17 edits in `data/versification/Rom.draft.edits.tsv`, applied (433 verses, every
  chapter at the KJV count): six boundaries move to where 1573 prints its number, which is the KJV's (3:3–4 and
  3:5–6 *Absit*, 3:27–28 *Censemus*, 11:17–18 *noli contra ramos*, 12:16–17 *nemini malum*, 15:32–33 *Deus
  pacis*); 15:9–11 is arranged as 1573 and the KJV number it (*Quare te celebrabo* inside 15:9, *Item: laudate*
  opening 15:11); and three follow the KJV where 1573 does not: 3:22–23 (*nam omnes peccaverunt*), 8:20–21 (*fore,
  ut ipsa*) and 9:11–12 (*Rebeccae, inquam*; 1573 prints 12 before *sed ex vocante*).
- **Collation** (`python -m pipeline collate Rom 1-16`; `data/calibration/Rom1-16-collation.tsv`), with the two
  blind spots Acts found now closed: words added or lost at a verse's edge are compared (`collate.edges`), and f
  against long s is a place where 1573's hOCR and Wikisource keep them apart (`collate.compare`; kept only where
  1573's word is Latin, as *fani*, *fit*). Read on the page image: the 76 readings where 1573 and another printing
  agree against Wikisource and the 13 where two others do; the places where only 1573's OCR differs and its words
  are Latin (with f read as s); the 80 f/s places (all but four are 1573's OCR reading ſ as f: *fumus*, *fiue*,
  *fi*); and the edge places (lines the OCR dropped, or margin notes run in: 1:11 *Scilicet* is a margin gloss,
  3:6 *iustus* the note *si esset iniustus*). The crops are in `sources/mdz-1573/crops/` (`Rom.*`). Also swept: the
  words no lexicon knows (13:5 *suplicii*, 15:31 *contuamces*) and the u-for-v slips the j/v rule leaves alone
  (none in Romans: every *u* it leaves before a vowel is a vowel, as *mortuus*, *tribuit*).
- **In all, 93 corrections**: 51 Wikisource slips (section 1), 30 readings of Castellio's revised
  text (section 2), 2 word divisions (section 3), 10 found on a second pass (section 2a). **Applied to
  the draft** (decision 30's standing rule). Spellings (*caussa/causa*, *adspicio/aspicio*, *adfectio*,
  *intelligo*, *millia*, *exsto/exto*, *sepulcrum/sepulchrum*) are left to stage 3's rules, as in Acts (a question
  at the end of the stages 3–5 summary).

## 1. Wikisource slips: 1573 and the other printings agree against it (51)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

1. **Romans 1:19** *patefacerit* → *patefecerit*. 1573 OCR *patefecerit*; 1556, 1758, 1747.
   **Apply:** `Rom.1.19` la: `patefacerit` → `patefecerit`
2. **Romans 1:21** *Deo gloriamque tribuerunt* → *Deo gloriam gratiamque tribuerunt*. 1573 *Deo gloriam gratiamq; tribuerunt*; 1556, 1758, 1747, 1750: Wikisource dropped *gratiam*.
   **Apply:** `Rom.1.21` la: `Deo gloriamque tribuerunt` → `Deo gloriam gratiamque tribuerunt`
3. **Romans 1:21** *caligavit eorum* → *caligavitque eorum*. 1573 *caligauitq; eorum*; 1556, 1758, 1715.
   **Apply:** `Rom.1.21` la: `caligavit eorum` → `caligavitque eorum`
4. **Romans 1:25** *transtulerunt, et res* → *transtulerint, et res*. 1573 *transtulerint*; 1556, 1758, 1715, 1726 (subjunctive, with *coluerint*).
   **Apply:** `Rom.1.25` la: `transtulerunt, et res` → `transtulerint, et res`
5. **Romans 1:32** *qui talia faciant,* → *qui talia faciunt,*. 1573 *qui talia faciunt*; 1556, 1681.
   **Apply:** `Rom.1.32` la: `qui talia faciant,` → `qui talia faciunt,`
6. **Romans 2:13** *auditores apud Deum* → *auditores erunt apud Deum*. 1573 *auditores erunt apud Deum*; 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Rom.2.13` la: `auditores apud Deum` → `auditores erunt apud Deum`
7. **Romans 2:23** *Deum decoras?* → *Deum dedecoras?*. 1573 *Deum dedecoras*; 1758, 1681, 1715, 1726.
   **Apply:** `Rom.2.23` la: `Deum decoras?` → `Deum dedecoras?`
8. **Romans 2:29** *laus ab hominibus* → *laus non ab hominibus*. 1573 *laus non ab hominibus*; 1556, 1758, 1715, 1747, 1750.
   **Apply:** `Rom.2.29` la: `laus ab hominibus` → `laus non ab hominibus`
9. **Romans 3:1** *circumcionis* → *circumcisionis*. 1573 *circumcisionis*; 1758, 1750.
   **Apply:** `Rom.3.1` la: `circumcionis` → `circumcisionis`
10. **Romans 3:5** *injustia* → *injustitia*. 1573 *iniustitia*; 1758, 1715, 1750.
   **Apply:** `Rom.3.5` la: `injustia` → `injustitia`
11. **Romans 3:12** *nequaquam sunt* → *nequamque sunt*. 1573 *nequamq; sunt* (‘and are worthless’); 1758, 1750, 1726.
   **Apply:** `Rom.3.12` la: `nequaquam sunt` → `nequamque sunt`
12. **Romans 3:13** *aspidum virtus* → *aspidum virus*. 1573 *virus*; 1747, 1726.
   **Apply:** `Rom.3.13` la: `aspidum virtus` → `aspidum virus`
13. **Romans 3:19** *lex dixit* → *lex dicit*. 1573 *lex dicit*; 1747, 1715.
   **Apply:** `Rom.3.19` la: `lex dixit` → `lex dicit`
14. **Romans 3:24** *quae sit Christo Jesu* → *quae fit in Christo Jesu*. 1573 *quæ fit in Christo Iesu* (f, not long s); 1556, 1758 *fit in*, 1747 *in*. The collation found *in*; *fit* came from the new f/s check.
   **Apply:** `Rom.3.24` la: `quae sit Christo Jesu` → `quae fit in Christo Jesu`
15. **Romans 4:11** *cicrumcisionis* → *circumcisionis*. 1573 *circumcisionis*; 1758, 1715, 1747.
   **Apply:** `Rom.4.11` la: `cicrumcisionis` → `circumcisionis`
16. **Romans 5:1** *pacem habemus eum Deo* → *pacem habemus cum Deo*. 1573 *cum Deo*; 1758, 1747, 1750, 1726.
   **Apply:** `Rom.5.1` la: `pacem habemus eum Deo` → `pacem habemus cum Deo`
17. **Romans 5:11** *reconcilitationem* → *reconciliationem*. 1573 *reconciliationem*; 1747, 1750.
   **Apply:** `Rom.5.11` la: `reconcilitationem` → `reconciliationem`
18. **Romans 5:12** *persuasit mors* → *pervasit mors*. 1573 *peruasit mors*; 1556, 1758, 1750.
   **Apply:** `Rom.5.12` la: `persuasit mors` → `pervasit mors`
19. **Romans 5:14** *reginavit* → *regnavit*. 1573 *regnauit*; 1747, 1750.
   **Apply:** `Rom.5.14` la: `reginavit` → `regnavit`
20. **Romans 5:17** *atque domum* → *atque donum*. 1573 *donum*; 1715, 1747, 1750.
   **Apply:** `Rom.5.17` la: `atque domum` → `atque donum`
21. **Romans 6:15** *non sum lege* → *non sub lege*. 1573 *non sub lege*; 1758, 1726.
   **Apply:** `Rom.6.15` la: `non sum lege` → `non sub lege`
22. **Romans 7:3** *vivente vero,* → *vivente viro,*. 1573 *viuente viro*; 1556, 1758, 1681, 1726.
   **Apply:** `Rom.7.3` la: `vivente vero,` → `vivente viro,`
23. **Romans 8:21** *quoque quoque* → *quoque*. 1573 *ipsa quoque rerum natura*; 1556, 1758, 1726: Wikisource doubles the word.
   **Apply:** `Rom.8.21` la: `quoque quoque` → `quoque`
24. **Romans 8:22** *congemiscere ac condolere* → *congemiscere atque condolere*. 1573 *atq;*; 1681, 1726.
   **Apply:** `Rom.8.22` la: `congemiscere ac condolere` → `congemiscere atque condolere`
25. **Romans 8:26** *infirmatitatibus* → *infirmitatibus*. 1573 *infirmitatibus*; 1715, 1726.
   **Apply:** `Rom.8.26` la: `infirmatitatibus` → `infirmitatibus`
26. **Romans 8:27** *indigator* → *indagator*. 1573 *indagator*; 1681, 1726.
   **Apply:** `Rom.8.27` la: `indigator` → `indagator`
27. **Romans 8:31** *quis contra nos est?* → *quis contra nos?*. 1573 *quis contra nos?*; 1758.
   **Apply:** `Rom.8.31` la: `quis contra nos est?` → `quis contra nos?`
28. **Romans 8:32** *perpercerit* → *pepercerit*. 1573 *pepercerit*; 1556, 1758, 1715, 1747, 1750.
   **Apply:** `Rom.8.32` la: `perpercerit` → `pepercerit`
29. **Romans 8:38** *neque potestates, neque potestates,* → *neque potestates,*. 1573 *neq; potestates* once; Wikisource doubles it.
   **Apply:** `Rom.8.38` la: `neque potestates, neque potestates,` → `neque potestates,`
30. **Romans 9:2** *dolore irremisso* → *dolore et irremisso*. 1573 *dolore & irremisso*; 1556, 1758.
   **Apply:** `Rom.9.2` la: `dolore irremisso` → `dolore et irremisso`
31. **Romans 9:21** *massa aliud vas* → *massa aliud facere vas*. 1573 *aliud facere vas*; 1758, 1747, 1750.
   **Apply:** `Rom.9.21` la: `massa aliud vas` → `massa aliud facere vas`
32. **Romans 10:16** *quis credidit* → *quis credit*. 1573 *quis credit orationi nostræ*; 1758, 1747.
   **Apply:** `Rom.10.16` la: `quis credidit` → `quis credit`
33. **Romans 11:4** *Verum quis ei* → *Verum quid ei*. 1573 *Verùm quid ei dicit oraculum*; 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Rom.11.4` la: `Verum quis ei` → `Verum quid ei`
34. **Romans 11:13** *ministrium* → *ministerium*. 1573 *ministerium*; 1747, 1750.
   **Apply:** `Rom.11.13` la: `ministrium` → `ministerium`
35. **Romans 11:21** *quidem pareat* → *quidem parcat*. 1573 *parcat*; 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Rom.11.21` la: `quidem pareat` → `quidem parcat`
36. **Romans 11:22** *severitatem, in benignitatem* → *severitatem, in te benignitatem*. 1573 *in te benignitatem*; 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Rom.11.22` la: `severitatem, in benignitatem` → `severitatem, in te benignitatem`
37. **Romans 11:30** *Ut enim nos,* → *Ut enim vos,*. 1573 *Vt enim vos*; 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Rom.11.30` la: `Ut enim nos,` → `Ut enim vos,`
38. **Romans 11:33** *sapientiae cognitionis Dei* → *sapientiae cognitionisque Dei*. 1573 *cognitionisq;*; 1758, 1747, 1750.
   **Apply:** `Rom.11.33` la: `sapientiae cognitionis Dei` → `sapientiae cognitionisque Dei`
39. **Romans 12:6** *fidei potione* → *fidei portione*. 1573 *portione*; 1758, 1750, 1715, 1747.
   **Apply:** `Rom.12.6` la: `fidei potione` → `fidei portione`
40. **Romans 13:4** *caussa gaudium* → *caussa gladium*. 1573 *causa gladium*; 1747, 1715.
   **Apply:** `Rom.13.4` la: `caussa gaudium` → `caussa gladium`
41. **Romans 14:4** *qut cadit* → *aut cadit*. 1573 *aut*; 1758, 1715, 1750, 1726.
   **Apply:** `Rom.14.4` la: `qut cadit` → `aut cadit`
42. **Romans 14:11** *omnis lingua* → *omnisque lingua*. 1573 *omnisq; lingua*; 1758, 1750, 1726.
   **Apply:** `Rom.14.11` la: `omnis lingua` → `omnisque lingua`
43. **Romans 15:11** *Deominum* → *Dominum*. 1573 *Dominum*; 1747, 1750, 1726.
   **Apply:** `Rom.15.11` la: `Deominum` → `Dominum`
44. **Romans 15:15** *aliquando audacius* → *aliquanto audacius*. 1573 *aliquanto*; 1556, 1758, 1747, 1715, 1726.
   **Apply:** `Rom.15.15` la: `aliquando audacius` → `aliquanto audacius`
45. **Romans 15:19** *Christa evangelio* → *Christi evangelio*. 1573 *Christi*; 1758, 1747, 1750.
   **Apply:** `Rom.15.19` la: `Christa evangelio` → `Christi evangelio`
46. **Romans 15:21** *deo eo* → *de eo*. 1573 *de eo*; 1758, 1747, 1750.
   **Apply:** `Rom.15.21` la: `deo eo` → `de eo`
47. **Romans 15:24** *in itinere vos* → *in itinere visurum vos*. 1573 *in itinere visurű vos*; 1681, 1747, 1750, 1726.
   **Apply:** `Rom.15.24` la: `in itinere vos` → `in itinere visurum vos`
48. **Romans 15:24** *aliquantulum* → *aliquantum*. 1573 *aliquantum*; 1750, 1726.
   **Apply:** `Rom.15.24` la: `aliquantulum` → `aliquantum`
49. **Romans 16:17** *qosque* → *eosque*. 1573 *eosq;*; 1758, 1715, 1747, 1750.
   **Apply:** `Rom.16.17` la: `qosque` → `eosque`
50. **Romans 16:19** *Sed solo vos* → *Sed volo vos*. 1573 *Sed volo vos*; 1758, 1715, 1750.
   **Apply:** `Rom.16.19` la: `Sed solo vos` → `Sed volo vos`
51. **Romans 16:27** *Cenchreenis ecclesiae ministram* → *Cenchreensis ecclesiae ministram.*. 1573 *Cenchreensis ecclesiæ ministram.* (the subscription, in italics; see section 4); 1747, 1750, and 16:1 *Cenchreensis*.
   **Apply:** `Rom.16.27` la: `Cenchreenis ecclesiae ministram` → `Cenchreensis ecclesiae ministram.`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (30)

Wikisource reads with the printings after the `|` (1715, 1747, 1750: the early wording, and sometimes 1556); 1573 with 1758 and usually 1556. 1556 is cited from its OCR (e-rara), which finds about half the words.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

52. **Romans 1:2** *per suos vates* → *per vates suos*. 1573 *per vates suos*; 1758 | 1556 *per suos uates*, 1747, 1750.
   **Apply:** `Rom.1.2` la: `per suos vates` → `per vates suos`
53. **Romans 2:4** *ac lenitudinem* → *ac lentitudinem*. 1573 *lentitudinē* (‘slowness’); 1726, 1715, 1747 | 1556, 1758, 1750 *lenitudinem*.
   **Apply:** `Rom.2.4` la: `ac lenitudinem` → `ac lentitudinem`
54. **Romans 2:26** *Quod si praeputium legis* → *Quod si praeputiatus legis*. 1573 *Quòd si præputiatus legis instituta conseruat*; 1556, 1726 | 1750 (Castellio's note on the verse explains the masculine *ejus*).
   **Apply:** `Rom.2.26` la: `Quod si praeputium legis` → `Quod si praeputiatus legis`
55. **Romans 2:29** *quae animi est* → *quae cordis est*. 1573 *quæ cordis est*; 1556, 1758, 1726 | 1715, 1747, 1750.
   **Apply:** `Rom.2.29` la: `quae animi est` → `quae cordis est`
56. **Romans 3:21** *a lege et vatibus* → *a lege ac vatibus*. 1573 *à lege ac vatibus* (the *b* before *diuina* is a note mark, which the OCR read as *et*); 1556 *ac*.
   **Apply:** `Rom.3.21` la: `a lege et vatibus` → `a lege ac vatibus`
57. **Romans 3:22** *Non est enim discrimen* → *Non enim est discrimen*. 1573 *Non enim est discrimen*; 1758 | 1681, 1715, 1750.
   **Apply:** `Rom.3.22` la: `Non est enim discrimen` → `Non enim est discrimen`
58. **Romans 6:11** *per Christum Jesum Dominum* → *per Jesum Christum Dominum*. 1573 OCR *per Iesum Christum Dominum* (the crop found 7:25, worded alike); 1758 | 1556 *per Christum Iesum*, 1681, 1747, 1750.
   **Apply:** `Rom.6.11` la: `per Christum Jesum Dominum` → `per Jesum Christum Dominum`
59. **Romans 7:14** *peccato mancipatus* → *peccato emancipatus*. 1573 *peccato emancipatus* (canvas 860; ‘made over to sin’, as Castellio's own 6:22 *Deoque emancipati*) | 1556, 1758 *mancipatus*. 1573 alone of the printings read: a misprint is possible, but the word is his. Worth a look.
   **Apply:** `Rom.7.14` la: `peccato mancipatus` → `peccato emancipatus`
60. **Romans 7:17** *in me vitiositas* → *in me peccatum*. 1573 *habitans in me peccatum*; 1758, 1726 | 1715, 1750.
   **Apply:** `Rom.7.17` la: `in me vitiositas` → `in me peccatum`
61. **Romans 7:20** *in me vitiositas* → *in me peccatum*. 1573 OCR *habitans in me peccatum* (as 7:17, read on the page); 1758 | 1715, 1750.
   **Apply:** `Rom.7.20` la: `in me vitiositas` → `in me peccatum`
62. **Romans 7:23** *legi vitiositatis* → *legi peccati*. 1573 *legi peccati*; 1556, 1758 | 1715, 1750.
   **Apply:** `Rom.7.23` la: `legi vitiositatis` → `legi peccati`
63. **Romans 8:3** *et peccatum peccato damnavit* → *et pro peccato peccatum damnavit*. 1573 *& pro pecca-|to peccatum damnauit in carne*; 1556 *pro peccato peccatum* | 1747, 1750.
   **Apply:** `Rom.8.3` la: `et peccatum peccato damnavit` → `et pro peccato peccatum damnavit`
64. **Romans 8:29** *Quos enim praevidit* → *Quos enim praenovit*. 1573 *prænouit*; 1556, 1758, 1681 | 1715, 1747.
   **Apply:** `Rom.8.29` la: `Quos enim praevidit` → `Quos enim praenovit`
65. **Romans 9:3** *quod ad humanam naturam attinet* → *quod ad carnem attinet*. 1573 *quod ad carnem attinet*; 1556, 1758 | 1747, 1750.
   **Apply:** `Rom.9.3` la: `quod ad humanam naturam attinet` → `quod ad carnem attinet`
66. **Romans 9:5** *quod ad humanitatem attinet* → *quod ad carnem attinet*. 1573 *quod ad carnem attinet*; 1556, 1681 | 1747, 1750.
   **Apply:** `Rom.9.5` la: `quod ad humanitatem attinet` → `quod ad carnem attinet`
67. **Romans 9:5** *in sempiternum. Amen.* → *in sempiternum. Etiam.*. 1573 *collaudandus in sempiternum, Etiam.*; 1758 *Etiam* (Castellio's word for ἀμήν, as 1:25 and 11:36).
   **Apply:** `Rom.9.5` la: `in sempiternum. Amen.` → `in sempiternum. Etiam.`
68. **Romans 9:7** *ideo omnes sunt, filii* → *ideo sunt omnes filii*. 1573 *ideò sunt omnes filij*; 1556 | 1747, 1750.
   **Apply:** `Rom.9.7` la: `ideo omnes sunt, filii` → `ideo sunt omnes filii`
69. **Romans 9:8** *non humanitatis filii* → *non carnis filii*. 1573 *non carnis filij*; 1556, 1758, 1726 | 1747, 1750.
   **Apply:** `Rom.9.8` la: `non humanitatis filii` → `non carnis filii`
70. **Romans 9:9** *enim hoc est dictum* → *enim est hoc dictum*. 1573 *enim est hoc dictum*; 1556, 1726 | 1750.
   **Apply:** `Rom.9.9` la: `enim hoc est dictum` → `enim est hoc dictum`
71. **Romans 9:11** *decretum ratum esset, Non ex operibus, sed ex vocante,* → *decretum, non ex operibus, sed ex vocante ratum esset,*. 1573 *decretum, non ex operibus, 12 sed ex vocante ratum esset, Rebeccæ inquam dictum est*; 1556, 1758, 1726 | 1747. (The verse boundary is the KJV's, before *Rebeccae*: versification edits.)
   **Apply:** `Rom.9.11` la: `decretum ratum esset, Non ex operibus, sed ex vocante,` → `decretum, non ex operibus, sed ex vocante ratum esset,`
72. **Romans 10:2** *sed inscite facere* → *sed id inscite facere*. 1573 *sed id inscitè facere*; 1556, 1758, 1726 | 1715, 1747, 1750.
   **Apply:** `Rom.10.2` la: `sed inscite facere` → `sed id inscite facere`
73. **Romans 10:8** *quid agunt litterae* → *quid aiunt litterae*. 1573 *Sed quid aiunt literæ*; 1758, 1681, 1747, 1726 | 1750.
   **Apply:** `Rom.10.8` la: `quid agunt litterae` → `quid aiunt litterae`
74. **Romans 11:2** *Deus populum suum, quem* → *Deus suum populum, quem*. 1573 *Deus suum populum*; 1758, 1681, 1726 | 1715, 1747, 1750.
   **Apply:** `Rom.11.2` la: `Deus populum suum, quem` → `Deus suum populum, quem`
75. **Romans 11:16** *primitiae sacrae sunt* → *primitiae sanctae sunt*. 1573 *primitiæ sanctæ*; 1758.
   **Apply:** `Rom.11.16` la: `primitiae sacrae sunt` → `primitiae sanctae sunt`
76. **Romans 11:16** *si sacra radix* → *si sancta radix*. 1573 *si sancta radix*; 1758.
   **Apply:** `Rom.11.16` la: `si sacra radix` → `si sancta radix`
77. **Romans 11:20** *diffidentia avulsi* → *diffidentia evulsi*. 1573 *Diffidentia euulsi*; 1758, 1726 | 1715, 1747, 1750.
   **Apply:** `Rom.11.20` la: `diffidentia avulsi` → `diffidentia evulsi`
78. **Romans 11:23** *eos rursum inserere* → *eos rursus inserere*. 1573 *rursus*; 1758, 1726 | 1715, 1750.
   **Apply:** `Rom.11.23` la: `eos rursum inserere` → `eos rursus inserere`
79. **Romans 15:2** *Quisquis nostrum* → *Quisque nostrum*. 1573 *Quisque nostrûm*; 1556 OCR *Quisq;*.
   **Apply:** `Rom.15.2` la: `Quisquis nostrum` → `Quisque nostrum`
80. **Romans 15:4** *et scripturarum consolationem* → *et litterarum consolationem*. 1573 *& literarum consolationem*; 1556, 1758 | 1747, 1750.
   **Apply:** `Rom.15.4` la: `et scripturarum consolationem` → `et litterarum consolationem`
81. **Romans 16:6** *multum caussa nostra laboravit* → *multum nostra caussa laboravit*. 1573 *quæ multum nostra causa laborauit* | 1556, 1750 *caussa nostra*.
   **Apply:** `Rom.16.6` la: `multum caussa nostra laboravit` → `multum nostra caussa laboravit`

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

82. **Romans 4:12** *noniis solum* → *non iis solum*. 1573 *non ijs solùm*; 1758, 1715, 1747, 1750.
   **Apply:** `Rom.4.12` la: `noniis solum` → `non iis solum`
83. **Romans 13:4** *qui malefaciunt* → *qui male faciunt*. 1573 *qui malè faciunt*; 1556, 1758, 1747 (as your settled *male facere*).
   **Apply:** `Rom.13.4` la: `qui malefaciunt` → `qui male faciunt`

## 2a. Found on a second pass (10)

Where the collation had sorted the place as noise or a spelling, or the new checks found it: two *fit* for *sit* (f/s), a one-letter reading, the early *sacram*, two slips no lexicon knows, a capital, a stray mark, and two names brought to your settled forms.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-09; every item read on the 1573 page image unless marked OCR)

84. **Romans 4:16** *per fidem id sit,* → *per fidem id fit,*. 1573 *per fidem id fit, vt ſit gratuitum* (f, then long s); 1556 *id fit, ut sit*; 1758 *fit*. Found by the new f/s check.
   **Apply:** `Rom.4.16` la: `per fidem id sit,` → `per fidem id fit,`
85. **Romans 10:10** *et ore sit confessio* → *et ore fit confessio*. 1573 *& ore fit confessio*; 1556, 1758 *fit*. Found by the new f/s check (Vulgate *ore autem confessio fit*).
   **Apply:** `Rom.10.10` la: `et ore sit confessio` → `et ore fit confessio`
86. **Romans 11:17** *ramorum quidem avulsi* → *ramorum quidam avulsi*. 1573 *ramorum quidam auulsi* (canvas 863); 1556 *quidam*. The collation had counted *quidem/quidam* as noise (one letter, 1573 alone in its OCR).
   **Apply:** `Rom.11.17` la: `ramorum quidem avulsi` → `ramorum quidam avulsi`
87. **Romans 12:1** *viventem, sacram,* → *viventem, sanctam,*. 1573 *viuentem, sanctam, acceptam Deo* (canvas 864): the early *sacram*, as 11:16; its OCR *fanctam* hid it from the first filter.
   **Apply:** `Rom.12.1` la: `viventem, sacram,` → `viventem, sanctam,`
88. **Romans 13:5** *suplicii* → *supplicii*. 1573 *supplicij*; 1758 (the collation folds double letters).
   **Apply:** `Rom.13.5` la: `suplicii` → `supplicii`
89. **Romans 11:1** *tribus benjamiticae* → *tribus Benjamiticae*. 1573 *tribus Beniamiticæ* (capital); 1758 (as Acts 13:21 *Benjaminia*).
   **Apply:** `Rom.11.1` la: `tribus benjamiticae` → `tribus Benjamiticae`
90. **Romans 15:31** *contuamces: usque id* → *contumaces: utque id*. 1573 *cótumaces: vtq; id* (‘and that’); 1747, 1750 *utque*: Wikisource's *contuamces* (no word) and *usque*.
   **Apply:** `Rom.15.31` la: `contuamces: usque id` → `contumaces: utque id`
91. **Romans 12:16** *accommodantes,| Ne vobis placete,* → *accommodantes. Ne vobis placete,*. 1573 *accommodantes. Ne vobis placete,*: Wikisource's stray `|` (a wiki table mark) and comma.
   **Apply:** `Rom.12.16` la: `accommodantes,| Ne vobis placete,` → `accommodantes. Ne vobis placete,`
92. **Romans 9:13** *Esauum vero* → *Esaum vero*. 1573 *Esaum*; 1758, 1726: your settled *Ēsāum* (7×; Genesis *Ēsāus*).
   **Apply:** `Rom.9.13` la: `Esauum vero` → `Esaum vero`
93. **Romans 9:29** *Sodomae ac Gomorrhae* → *Sodomae ac Gomorrae*. 1573 *Gomorræ*; 1758, 1747: your settled *Gomorræ* (3×), *Gomorram* (4×).
   **Apply:** `Rom.9.29` la: `Sodomae ac Gomorrhae` → `Sodomae ac Gomorrae`

## 4. Checked and kept

- **1:32** *adsentiuntur* and **12:21** *maleficium*: 1573 prints both (*facientibus assentiuntur*, *vince
  malefi-|cium*); the OCRs lost the line's end.
- **4:1** *quod ad humanam naturam attinet* and **8:1** *qui in Christo Jesu*: 1573 prints them (its OCR dropped
  *quod* and read *quia*).
- **1:11** *Scilicet* (1573 OCR) is a margin gloss beside *hoc est*, and **3:6** *iustus* the margin note *si esset
  iniustus*: not text.
- **1:16; 4:16** (the second to fourth); **8:27; 13:4; 13:11; 15:16** *sit*: long s on the page (subjunctives). The
  other f/s places are 1573's OCR.
- **16:23** *Gāius*: 1573 *Caius*, kept as Acts 19:29 (Gaffiot *Gāius*).
- **16:27** the subscription *Scripta est Corinthi, missa per Phœbam, Cenchreensis ecclesiæ ministram.*: 1573 sets
  it in italics under the verse, as a subscription, not verse text; Wikisource runs it into 16:27. Kept in 16:27 for
  now (USFM has `\cls` for a letter's closing; a question in the stages 3–5 summary).
- **11:26** *Jacobaeos*: 1573 *Iacobeos* (e, not æ): a spelling, left to stage 3.
- **8:23** *Quin etiam*, **16:4** *verum etiam*, **6:16** *vos ipsos*, **9:3** *me ipsum*: 1573 joins them
  (*Quinetiam*, *verumetiam*, *vosipsos*, *meipsum*); your settled chapters write them apart (*vērum etiam*, *vōs
  ipsōs*, *mē ipsum*). Kept apart.
- The collation's `correct` places at a chapter's opening (*Quaenam*, *Igitur*, *Num* …) were 1573's decorated
  initials, which the OCRs miss: the edge check now leaves a chapter's opening alone.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573, now the text. Recorded, not applied (decision 24). 1556 is cited from its OCR
(e-rara 10281656), not the page image.

| Place | 1573 (= the text now) | 1556 | Also |
|---|---|---|---|
| Rom 1:2 | *per vātēs suōs* | *per suos uates* | 1747, 1750 |
| Rom 2:4 | *lentitūdinem* | *lenitudinem* | 1758, 1750 |
| Rom 6:11 | *per Jēsum Chrīstum* | *per Christum Iesum* | 1681, 1747, 1750 |
| Rom 7:14 | *peccātō ēmancipātus* | *mancipatus* | 1758 |
| Rom 16:6 | *nostrā causā* | *caussa nostra* | 1750 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-09)
