# Galatians 1–6, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of 2 Corinthians (`data/review/2cor1-13-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 889–892: 1:1–2:19 on 889, 2:20–3:29 on
  890, 4:1–5:3 on 891, 5:3–6:18 on 892). 1556 is the reference: where it reads otherwise, its reading is recorded as
  a variant (section 5). Stage 1 drafted Wikisource's Galatians as **`text/draft/GAL.usfm`** (BSB paragraphs). You
  have no earlier work on Galatians; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the
  witness `1726`, read as an OCR.
- **Wikisource's Galatians is the early wording**, as its Romans and Corinthians, with slips of its own: *fiducia*
  for *fides* (2:16, 2:20, 3:22–25), *recte se … gerere* for *recto pede incedere* (2:14, ὀρθοποδοῦσιν), *ambire*
  for *aemulari* (4:17–18), *natura* for *creatura* (6:15, καινὴ κτίσις, as 2 Cor 5:17), *favor* for *gratia* (6:18).
  1556 already has every one of these revisions where its OCR can be read. 1573's own changes against 1556 are 5:2
  *circumcidemini* and *nihil vobis*, 5:6 *operans* (1556 *agens*), 5:12 *excidantur* (1556 *excindantur*) and 3:19
  *sequestrum* (1556 *sequestrem*); at 4:14 (*angelum*) and 4:17 (*excludere nos*) 1573 reads with Wikisource
  against 1556 (section 5).
- **Versification** (decision 5): 1 edit in `data/versification/Gal.draft.edits.tsv`, applied (149 verses, every
  chapter at the KJV count):
  - **5:22–23**: 1573 (canvas 892) and Wikisource print the KJV's 5:22–23 as one verse (*At spiritus fructus …
    lenitas, continentia. Contra talia non est lex.*), so their 23–25 are the KJV's 24–26. Split at *lenitas*, where
    the KJV's 23 (*Meekness, temperance*) begins. Elsewhere 1573 numbers every verse as the KJV.
- **Collation** (`python -m pipeline collate Gal 1-6`; `data/calibration/Gal1-6-collation.tsv`, 277 places after the
  renumbering: 59 correct, 9 others-1573-agrees, 8 others, 196 base-only, 5 uncovered), with the edge and f/s
  checks. Read on the page image (crops in `sources/mdz-1573/crops/Gal.*`, 71): the readings where 1573 and another
  printing agree against Wikisource; the places where only 1573's OCR differs and its words are Latin (1:21
  *Ciliciaeque*, 3:10 *libro*, 3:15 *sancitum*, 3:19 *sequestrum*, 5:12 *excidantur*, 6:15 *creatura*, 6:16 *gerent*,
  2:6 *videtur*, 4:3 *et* …); the edge places (3:17 *rescindat*, 4:31 *liberae*, 5:1 *teneri*, 4:14 *acceperitis*,
  4:16 *dicendo*: line ends or turn-overs 1573's OCR lost, all printed). The rest of the base-only readings are 1573's
  OCR (*ludaisino*, *Deuin*, *essein*, *quisqs*), note letters and margin notes run into the text (section 4). Each
  place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758, 1681,
  1715, 1747, 1750).
- **The five verses 1573's OCR covers poorly** (1:22, 2:18, 3:13, 5:12, 6:11; `uncovered`) were read whole on the
  image: 1:22 (*Erã aũt ignotus facie Chriſtianis Iudęæ eccleſijs*), 3:13 and 6:11 agree with the draft; 2:18 has
  *praebeo* (section 1, already a collation place) and 5:12 *excidantur* (section 2). Nothing further: section 2b is
  empty.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fit/sit*, *fuit/suit*,
  *fore/sore*, *forte/sorte*, *fuerit/suerit*, *fuisse/suisse*, *feret/seret*, *foret*) was read in its verse: all are
  *f* (4:9 *qui fit*, read on the image with the fi ligature). The reverse sweep (every *s* word whose *f*-form is
  Latin: *sit/fit*, *sumus/fumus*, *simus/fimus*, *sontes/fontes*, *sontem*, *semen/femen*, *semini*, *seminibus*,
  *sui/fui*) found **4:29 *ita sit etiam nunc*** and **5:11 *qui sit, ut tamen infester*** for 1573's *fit* (section
  2a): the collation listed both as f/s places but could not tell them from the OCR's usual f for ſ; on the image both
  are the fi ligature, as 4:9 *quî fit vt*, while 6:3 *nihil ſit* and 6:14 *ne ſit* are long s. 2:15, 2:17
  *sontes*, 3:16 *seminibus*, 3:25 *sumus*, 5:26 *simus* are ſ on the image or certain by sense.
- **In all, 58 corrections**: 30 Wikisource slips (section 1), 23 readings of Castellio's revised text (section 2),
  2 s-for-f slips found by the sweep (section 2a), 3 word divisions (section 3). Applied to the draft under decision
  30's standing rule once accepted. Spellings (*adscendi*, *adsumto*, *quamquam*, *quicumque*, *quamdiu*, *quum*,
  *caussa*, *caritas*, *exsecratio*, *exsequimini*, *paullum*, *litterae*, *heres*) are left to stage 3 (decision 37's
  rules); three rules proposed (section 6). Places kept against 1573 are in section 4, for your eye.

## 1. Wikisource slips: 1573 and the other printings agree against it (30)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Galatians 1:3** *et Domino Jesu Christo* → *et Domino nostro Jesu Christo*. 1573 *& Domino noſtro Ieſu Chriſto* (canvas 889); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Gal.1.3` la: `et Domino Jesu Christo` → `et Domino nostro Jesu Christo`
2. **Galatians 1:4** *pro nobis peccatis* → *pro nostris peccatis*. 1573 *qui ſeipſum pro noſtris peccatis* (canvas 889); 1556, 1758, 1681, 1715, 1750, 1726.
   **Apply:** `Gal.1.4` la: `pro nobis peccatis` → `pro nostris peccatis`
3. **Galatians 1:13** *quam immodice infestarem* → *quam immodice divinam infestarem*. 1573 *quàm immodicè diuinam infeſtarem ac depopularer Eccleſiam* (canvas 889); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Gal.1.13` la: `immodice infestarem` → `immodice divinam infestarem`
4. **Galatians 1:15** *a matres utero* → *a matris utero*. 1573 *qui me à matris vtero* (canvas 889); 1556, 1758, 1726.
   **Apply:** `Gal.1.15` la: `a matres utero` → `a matris utero`
5. **Galatians 1:18** *viscendi Petri gratia* → *visendi Petri gratia*. 1573 *aſcen-di, viſendi Petri gratia* (canvas 889); 1556, 1758, 1715, 1747.
   **Apply:** `Gal.1.18` la: `adscendi, viscendi Petri` → `adscendi, visendi Petri`
6. **Galatians 1:21** *Syriae Ciciliaeque* → *Syriae Ciliciaeque*. 1573 *in Syriæ Ciliciæq; tractus* (canvas 889); 1556, 1715, 1726 (Κιλικίας).
   **Apply:** `Gal.1.21` la: `Syriae Ciciliaeque` → `Syriae Ciliciaeque`
7. **Galatians 2:4** *quam habueremus* → *quam haberemus*. 1573 *quã haberemus in Chri-ſto Ieſu* (canvas 889); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Gal.2.4` la: `quam habueremus` → `quam haberemus`
8. **Galatians 2:8** *idem in me quoque egit* → *idem in me quoque id egit*. 1573 *idem in me quoque id egit, vt eſſem* (canvas 889); 1556, 1758, 1715, 1747, 1750.
   **Apply:** `Gal.2.8` la: `in me quoque egit` → `in me quoque id egit`
9. **Galatians 2:9** *columnae esse videantur* → *columnae esse videbantur*. 1573 *qui columnæ eſſe vi-debantur* (canvas 889); 1556, 1758, 1750, 1726.
   **Apply:** `Gal.2.9` la: `esse videantur` → `esse videbantur`
10. **Galatians 2:11** *quoniam reprehendus erat* → *quoniam reprehendendus erat*. 1573 *quoniam reprehendendus erat* (canvas 889; its annotation on the verse too); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `Gal.2.11` la: `quoniam reprehendus erat` → `quoniam reprehendendus erat`
11. **Galatians 2:13** *Barnabas quoque eorum simulationem* → *Barnabas quoque ad eorum simulationem*. 1573 *vt Barnabas quoq; ad eorum ſimulationem ab-duceretur* (canvas 889); 1556, 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Gal.2.13` la: `quoque eorum simulationem` → `quoque ad eorum simulationem`
12. **Galatians 2:16** *fidem adhibuimus Christo Jesu, non legis operibus* → *… Christo Jesu, ut justi fieremus Christi fide, non legis operibus*. 1573 *fidem adhibuimus Chriſto Ieſu, vt iuſti fieremus Chriſti fide, non legis operibus* (canvas 889; ἵνα δικαιωθῶμεν ἐκ πίστεως Χριστοῦ); 1556, 1758, 1726. Wikisource alone drops the clause: 1715, 1747, 1750 have it with the early *fiducia* (section 2's word).
   **Apply:** `Gal.2.16` la: `adhibuimus Christo Jesu, non legis` → `adhibuimus Christo Jesu, ut justi fieremus Christi fide, non legis`
13. **Galatians 2:17** *ergo Christus peccasti minister* → *ergo Christus peccati minister*. 1573 *ergo Chriſtus pecca-ti miniſter eſt?* (canvas 889); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `Gal.2.17` la: `Christus peccasti minister` → `Christus peccati minister`
14. **Galatians 2:18** *sontem me prabeo* → *sontem me praebeo*. 1573 *ſontem me præbeo* (canvas 889; an uncovered verse, read whole); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `Gal.2.18` la: `me prabeo` → `me praebeo`
15. **Galatians 3:2** *per legis opera spirtum* → *per legis opera spiritum*. 1573 *ſpiritum acceperitis* (canvas 890); 1556, 1747, 1726.
   **Apply:** `Gal.3.2` la: `opera spirtum acceperitis` → `opera spiritum acceperitis`
16. **Galatians 3:5** *spiritum suggesit* → *spiritum suggessit*. 1573 *ſpiritum ſuggeſsit* (canvas 890); 1556, 1758, 1681, 1747, 1726.
   **Apply:** `Gal.3.5` la: `spiritum suggesit` → `spiritum suggessit`
17. **Galatians 3:10** *omnibus in legis scriptis* → *omnibus in legis libro scriptis*. 1573 *omnibus in legis libro ſcriptis* (canvas 890; ἐν τῷ βιβλίῳ τοῦ νόμου); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Gal.3.10` la: `in legis scriptis` → `in legis libro scriptis`
18. **Galatians 3:14** *ut Spirtus promissum* → *ut Spiritus promissum*. 1573 *vt ſpiritus promiſſum adipiſcamur* (canvas 890); 1556, 1750, 1726. The capital is Wikisource's, left to stage 3.
   **Apply:** `Gal.3.14` la: `ut Spirtus promissum` → `ut Spiritus promissum`
19. **Galatians 3:15** *hominis sanctum pactum* → *hominis sancitum pactum*. 1573 *Quamuis hominis ſanci-tum pactum* (canvas 890; ratified, κεκυρωμένην); 1556, 1681, 1715, 1747, 1750, 1726. (3:17 *foedus a Deo sanctum* is *ſanctum* in 1573 and stays.)
   **Apply:** `Gal.3.15` la: `hominis sanctum pactum` → `hominis sancitum pactum`
20. **Galatians 3:17** *post annos quadrigentos* → *post annos quadringentos*. 1573 *poſt annos quadringen-tos triginta* (canvas 890); 1556, 1715, 1747, 1750.
   **Apply:** `Gal.3.17` la: `annos quadrigentos` → `annos quadringentos`
21. **Galatians 3:21** *neququam* → *nequaquam*. 1573 *Nequa-quam* (canvas 890); 1556, 1681, 1715, 1747, 1750.
   **Apply:** `Gal.3.21` la: `promissis? neququam.` → `promissis? nequaquam.`
22. **Galatians 3:21** *quae vitam conferre potest* → *quae vitam conferre posset*. 1573 *quæ vitam conferre poſ-ſet* (canvas 890; the subjunctive after *si data lex esset*); 1556, 1681, 1715, 1747, 1750.
   **Apply:** `Gal.3.21` la: `vitam conferre potest` → `vitam conferre posset`
23. **Galatians 4:20** *Vellem quidem nunc* → *Vellem equidem nunc*. 1573 *Vellem equidem nunc apud vos adeſſe* (canvas 891); 1556, 1758, 1750, 1726.
   **Apply:** `Gal.4.20` la: `Vellem quidem nunc` → `Vellem equidem nunc`
24. **Galatians 4:23** *Quorsum, ancillae filius* → *Quorum, ancillae filius*. 1573 *quorum, ancillę filius* (canvas 891; of the two sons of 4:22); 1556, 1681, 1715, 1750.
   **Apply:** `Gal.4.23` la: `Quorsum, ancillae` → `Quorum, ancillae`
25. **Galatians 4:29** *genitum divinitum infestabat* → *genitum divinitus infestabat*. 1573 *diuinitùs infeſtabat* (canvas 891), as *humanitus* before it; 1758, 1681, 1715, 1747, 1750.
   **Apply:** `Gal.4.29` la: `genitum divinitum infestabat` → `genitum divinitus infestabat`
26. **Galatians 5:1** *Christus nos adservuit* → *Christus nos adseruit*. 1573 *nos aſſeruit* (canvas 891; *adserō*, set free, as Wikisource's own 3:13 *adseruit*); 1556, 1681, 1715, 1747, 1750. The spelling *asseruit* is left to stage 3 (section 6).
   **Apply:** `Gal.5.1` la: `nos adservuit` → `nos adseruit`
27. **Galatians 5:17** *et Spirtus, contra quam caro* → *et Spiritus, contra quam caro*. 1573 *& ſpiritus con-trà quàm caro* (canvas 892); 1556, 1758, 1715, 1747, 1750.
   **Apply:** `Gal.5.17` la: `et Spirtus, contra` → `et Spiritus, contra`
28. **Galatians 6:2** *Alii aliorum opera ferte* → *Alii aliorum onera ferte*. 1573 *Alij aliorum onera ferte* (canvas 892; τὰ βάρη, as *onus* in 6:5); 1556, 1758, 1715, 1750.
   **Apply:** `Gal.6.2` la: `aliorum opera ferte` → `aliorum onera ferte`
29. **Galatians 6:4** *ita demum seipso tantum* → *ita demum in seipso tantum*. 1573 *ita demum in ſeipſo tantùm* (canvas 892; εἰς ἑαυτόν, beside *non in altero*); 1556, 1758, 1681, 1715, 1750.
   **Apply:** `Gal.6.4` la: `demum seipso` → `demum in seipso`
30. **Galatians 6:13** *Nam se ipsi quidem* → *Nam ne ipsi quidem*. 1573 *Nam ne ipſi quidem, qui circumciduntur, legi pa-rent* (canvas 892; οὐδὲ … αὐτοί); 1556, 1758, 1681, 1750.
   **Apply:** `Gal.6.13` la: `Nam se ipsi quidem` → `Nam ne ipsi quidem`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (23)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read, except 3:19, 5:2, 5:6 and 5:12 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Galatians 1:4** *pro nostris peccatis dedit* → *dedidit*. 1573 *pro noſtris peccatis dedidit* (canvas 889; *dēdō*, gave himself up, as *dederet* in 2:20); 1556, 1758, 1681, 1750, 1726. Wikisource *dedit* with 1715, 1747.
   **Apply:** `Gal.1.4` la: `peccatis dedit,` → `peccatis dedidit,`
2. **Galatians 2:13** *simulationem adduceretur* → *simulationem abduceretur*. 1573 *ad eorum ſimulationem ab-duceretur* (canvas 889; was carried away, συναπήχθη); 1556, 1758, 1726 (1750's OCR *à duceretur*). Wikisource with 1715.
   **Apply:** `Gal.2.13` la: `simulationem adduceretur` → `simulationem abduceretur`
3. **Galatians 2:14** *non recte se ad evangelii veritatem gerere* → *non recto pede incedere ad evangelii veritatem*. 1573 *eos non recto pede ince-dere ad Euangelij veritatem* (canvas 889), ὀρθοποδοῦσιν; 1556, 1758, 1681, 1726. The early line *recte se … gerere* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Gal.2.14` la: `non recte se ad evangelii veritatem gerere,` → `non recto pede incedere ad evangelii veritatem,`
4. **Galatians 2:16** *sed fiducia in Jesu Christo collocanda* → *sed tantum fide in Jesu Christo collocanda*. 1573 *ſed tantum fide in Ieſu Chriſto collocãda* (canvas 889), ἐὰν μὴ διὰ πίστεως; 1556 (OCR *fed tantum … ín Iefu Chrifto collocanda*), 1758, 1726. The early line *fiducia* without *tantum* (Wikisource, 1747, 1750).
   **Apply:** `Gal.2.16` la: `sed fiducia in Jesu` → `sed tantum fide in Jesu`
5. **Galatians 2:20** *fiducia vivo filii Dei* → *fide vivo filii Dei*. 1573 *fide viuo filij Dei* (canvas 890), ἐν πίστει; 1556, 1758, 1681. The early line *fiducia* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Gal.2.20` la: `fiducia vivo filii` → `fide vivo filii`
6. **Galatians 3:15** *nemo repudiat* → *nemo tamen repudiat*. 1573 *nemo tamen repudiat, aut immutat* (canvas 890; after *Quamvis*); 1556, 1681, 1750, 1726. Wikisource with 1715, 1747.
   **Apply:** `Gal.3.15` la: `nemo repudiat` → `nemo tamen repudiat`
7. **Galatians 3:19** *lata per sequestrem* → *lata per sequestrum*. 1573 *lata per ſequeſtrum* (canvas 890, clear on the image), and its annotation on the verse again *per ſequeſtrum, Scilicet Moſem*: *sequester, -trī*, the second-declension noun Gaffiot gives beside *sequester, -tris*. **1556** *sequestre* (the bar for *m*), with Wikisource, 1715, 1750: a 1573 change (section 5). For your eye: an inflection, not a wording; 3:20 *Sequester* is either.
   **Apply:** `Gal.3.19` la: `lata per sequestrem.` → `lata per sequestrum.`
8. **Galatians 3:21** *Ergone lex contraria est* → *Ergone lex est contraria*. 1573 *Ergóne lex eſt contraria Dei promiſsis?* (canvas 890); 1556, 1681 (word order). Wikisource with 1715, 1747, 1750.
   **Apply:** `Gal.3.21` la: `lex contraria est Dei` → `lex est contraria Dei`
9. **Galatians 3:22** *per Christi Jesu fiduciam* → *per Christi Jesu fidem*. 1573 *per Chriſti Ieſu fidem daretur fidentib.* (canvas 890), ἐκ πίστεως; 1556. The early line *fiduciam* (Wikisource, 1747, 1750).
   **Apply:** `Gal.3.22` la: `Jesu fiduciam daretur` → `Jesu fidem daretur`
10. **Galatians 3:23** *Antequam autem venisset fiducia* → *venisset fides*. 1573 *Antequam autem veniſſet fides ſub lege* (canvas 890), τὴν πίστιν; 1556, 1681, 1726. The early line (Wikisource, 1747, 1750).
   **Apply:** `Gal.3.23` la: `venisset fiducia,` → `venisset fides,`
11. **Galatians 3:23** *conclusi ad fiduciam* → *conclusi ad fidem*. 1573 *concluſi ad fidem, quæ patefacienda erat* (canvas 890); 1556, 1726. The early line (Wikisource, 1747, 1750).
   **Apply:** `Gal.3.23` la: `ad fiduciam, quae` → `ad fidem, quae`
12. **Galatians 3:24** *ut fiducia justi fieremus* → *ut fide justi fieremus*. 1573 *vt fide iuſti fieremus* (canvas 890), ἐκ πίστεως; 1556, 1681, 1726. The early line (Wikisource, 1747, 1750).
   **Apply:** `Gal.3.24` la: `ut fiducia justi` → `ut fide justi`
13. **Galatians 3:25** *Postquam autem venit fiducia* → *venit fides*. 1573 *Poſtquam autem venit fides non iam ſub pæda-gogo ſumus* (canvas 890); 1556, 1681, 1726. The early line (Wikisource, 1747, 1750). (3:26 *fide Christo Jesu habenda* is *fide* in Wikisource already.)
   **Apply:** `Gal.3.25` la: `venit fiducia,` → `venit fides,`
14. **Galatians 4:17** *ut se ambiatis* → *ut se aemulemini*. 1573 *vt ſe æmulemini* (canvas 891), ἵνα αὐτοὺς ζηλοῦτε; 1556, 1758, 1726. The early line *ambiatis* (Wikisource, 1750).
   **Apply:** `Gal.4.17` la: `ut se ambiatis` → `ut se aemulemini`
15. **Galatians 4:18** *Decet autem ambire in re bona* → *Deceret autem aemulari in re bona*. 1573 *Deceret autem æmulari in re bona ſemper* (canvas 891), ζηλοῦσθαι; 1556, 1758, 1726. The early line *Decet … ambire* (Wikisource, 1747, 1750). 4:17 *Ambiunt vos* is 1573's too and stays.
   **Apply:** `Gal.4.18` la: `Decet autem ambire` → `Deceret autem aemulari`
16. **Galatians 5:2** *si circumcidamini* → *si circumcidemini*. 1573 *ſi circũcidemini* (canvas 891, the e clear on the image; future, ἐὰν περιτέμνησθε); 1758, 1681 (OCR *circumcideni*). **1556** *circumcidamini*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5). For your eye.
   **Apply:** `Gal.5.2` la: `si circumcidamini,` → `si circumcidemini,`
17. **Galatians 5:2** *Christus vobis nihil proderit* → *Christus nihil vobis proderit*. 1573 *Chri-ſtus nihil vobis proderit* (canvas 891); 1758, 1681 (word order). **1556** *uobis nihil*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Gal.5.2` la: `Christus vobis nihil proderit` → `Christus nihil vobis proderit`
18. **Galatians 5:6** *fides per caritatem agens* → *fides per caritatem operans*. 1573 *ſed fides per charitatem operans* (canvas 892), ἐνεργουμένη; 1758, 1681. **1556** *agens*, with Wikisource, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Gal.5.6` la: `caritatem agens` → `caritatem operans`
19. **Galatians 5:12** *O utinam exscindatur* → *O utinam excidantur*. 1573 *O vtinam excidantur, qui vos inquietant* (canvas 892; an uncovered verse, read whole; *excīdō*, be cut off, ἀποκόψονται); 1758. No printing has Wikisource's singular with *qui … inquietant*: **1556** *excindantur*, with 1715 and 1750, 1747 *exscindantur*. The plural is every printing's; the verb 1573's (section 5).
   **Apply:** `Gal.5.12` la: `O utinam exscindatur,` → `O utinam excidantur,`
20. **Galatians 5:16** *obtemperate Spiritui, neque carnis* → *neve carnis*. 1573 *obtẽperate ſpiritui, néue carnis cu-piditatem* (canvas 892; with the imperative); 1556 (*neue*), 1758. The early line *neque* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Gal.5.16` la: `Spiritui, neque carnis` → `Spiritui, neve carnis`
21. **Galatians 6:15** *sed nova natura* → *sed nova creatura*. 1573 *ſed noua creatura* (canvas 892), καινὴ κτίσις, as 2 Cor 5:17; 1556. The early line *natura* (Wikisource, 1715, 1750).
   **Apply:** `Gal.6.15` la: `nova natura` → `nova creatura`
22. **Galatians 6:16** *ad hanc normam se gerunt* → *se gerent*. 1573 *ad hanc normam ſe gerẽt, ijs pax* (canvas 892; future, στοιχήσουσιν, as *tribuetur*); 1556 (*gerét*), 1758, 1681. Wikisource *gerunt* with 1715, 1750.
   **Apply:** `Gal.6.16` la: `se gerunt,` → `se gerent,`
23. **Galatians 6:18** *Domini nostri Jesu Christi favor* → *gratia*. 1573 *Domini noſtri Ieſu Chriſti gratia adſit animis veſtris* (canvas 892), ἡ χάρις; 1556. The early line *favor* (Wikisource, 1715, 1747, 1750), as 2 Cor 13:14.
   **Apply:** `Gal.6.18` la: `Christi favor adsit` → `Christi gratia adsit`

## 2a. Found by the f/s sweep (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **Galatians 4:29** *ita sit etiam nunc* → *ita fit etiam nunc*. 1573 *infeſtabat: ita fit etiam nunc* (canvas 891, the fi ligature on the image; so it happens now too, οὕτως καὶ νῦν); 1556 (OCR *fit*), 1758 (OCR *fit*). The other OCRs print *fit* too, but read every ſ as f, so they cannot tell.
   **Apply:** `Gal.4.29` la: `ita sit etiam` → `ita fit etiam`
2. **Galatians 5:11** *qui sit, ut tamen infester* → *qui fit, ut tamen infester*. 1573 *prædico, quî fit vt tamen infeſter* (canvas 892, the fi ligature, as 4:9 *quî fit vt vos*: how is it that); 1556 (OCR *quifitut*), 1758.
   **Apply:** `Gal.5.11` la: `qui sit, ut tamen` → `qui fit, ut tamen`

## 2b. Found where 1573 was not aligned (0)

The five uncovered verses (1:22, 2:18, 3:13, 5:12, 6:11) were read whole on the image (crops `Gal.1.22-Eram`,
`Gal.2.18-Atqui`, `Gal.3.13-execratio`, `Gal.5.12-excidantur`, `Gal.6.11-manu`). Their only differences from the
draft are 2:18 *praebeo* (section 1) and 5:12 *excidantur* (section 2), both already collation places; 1:22, 3:13
and 6:11 agree with the draft but for spellings (*Iudęæ*, *execratio*, *asseruit*, *quãtis … literis*).

## 3. Word division (3)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **Galatians 1:4** *Qui seipsum pro nostris peccatis* → *Qui se ipsum*. Your settled *sē ipsum* (18×: Matthew, Mark, Luke, John, 1–2 Corinthians) against *seipsum* 4× (Acts 3×, Romans 1×), as 1 Cor 3:18 and 11:28. 1573 joins it (*ſeipſum*, canvas 889).
   **Apply:** `Gal.1.4` la: `Qui seipsum pro` → `Qui se ipsum pro`
2. **Galatians 2:4** *in ChristoJesu libertatem* → *in Christo Jesu libertatem*. 1573 *in Chri-ſto Ieſu libertatem* (canvas 889); 1556, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Gal.2.4` la: `in ChristoJesu libertatem` → `in Christo Jesu libertatem`
3. **Galatians 6:4** *in seipso tantum* → *in se ipso tantum*. Your settled *sē ipsō* (7×: Luke, John, Acts), never *seipso*; as item 1. 1573 joins it (*ſeipſo*, canvas 892). (After section 1's item 29.)
   **Apply:** `Gal.6.4` la: `in seipso tantum` → `in se ipso tantum`

## 4. Checked and kept

- **5:22–23**: no words missing (versification, above).
- **2:6** *qui videntur esse aliquid*: 1573's OCR *videtur*; the image has *vidẽtur*, the bar for *n* (canvas 889).
  1556 and every printing *videntur*. No difference.
- **2:20** *ut se ipsum pro me dederet*: 1573 *dederet* (canvas 890, on the image), with 1556, 1681, 1715, 1747,
  1750 (1758 *dederit*): *dēderet*, from *dēdō*, as 1:4 *dedidit*. Kept.
- **3:17** *foedus a Deo sanctum*: 1573 *ſanctum* (canvas 890), not 3:15's *sancitum*. Kept.
- **4:14** *ceu Dei angelum*: 1573 *angelum* (canvas 891), with Wikisource, 1758, 1681, 1747, 1726; **1556**
  *nuncium* (section 5). Kept as 1573.
- **4:17** *nam excludere nos volunt*: 1573 *excludere nos vo-lunt* (canvas 891, on the image), with Wikisource,
  1758, 1750, 1726; **1556** and 1747 *vos* (ἐκκλεῖσαι ὑμᾶς). Kept as 1573, the base; for your eye (section 5).
- **4:31** *sed liberae*: 1573 *ſed liberæ* (canvas 891; its OCR lost the æ), with 1747, 1750. Kept.
- **4:3** *cum pueri essemus, sub mundanis*: 1573's OCR *& ſub* is the note letter *a* (canvas 891, margin *a ſub
  lege, quæ doctrina rudimenta humana ſunt*). Kept.
- **Note letters and margin notes**, not text: 1:6 *a* and *b*, 1:10 *c*, 1:16 *d* (twice), 3:8 *b*, 3:22 *c*, 3:24
  *d*, 4:3 *a*, 4:15 *b*, 5:11 *a*, 6:2 *a*, 6:14 *b*; the glosses at 1:7 (*in religione Christiana*), 1:16
  (*hominis*), 2:9–10 (*iustificari per Christum*), 3:1 (*crucifixus esse videatur*), 3:22 (*Omnia sub peccato sunt,
  ut docent literae*), 3:24 (*Ut nobis praeesset usque ad adventum Christi*), 4:3, 4:15, 5:11 (*si circumcisione
  docerem, non infestarent me Iudaei, nec eos offenderet Euangelium*), 6:2 (*praecepto*), 6:14; and 1573's
  annotations after chapters 2, 3, 4 and 6.
- **5:14** *alterum ut teipsum diligito*: 1573 *teipſum*; your settled Romans keeps *teipsum* in the same quotation
  (Rom 13:9 *Alterum ut teipsum amātō*) and twice more, against *tē ipsum* 13× in the Gospels. Kept as Romans; for
  your eye (the edition has both).
- **6:1** *adspicientes vos ipsos*: 1573 *aſpiciẽtes voſipſos*; your settled *vōs ipsōs* (6×), never joined. Kept
  apart; the spelling to stage 3 (section 6).
- **6:9** *defetisci*: 1573 *defethiſci* (as 2 Cor 4:1). Kept.
- **6:18** the subscription (*Ad Galatas scripta est Romae*): 1573 sets it in italics under the verse (canvas 892,
  *Ad Galatas ſcripta eſt Romæ*), as after 2 Corinthians. Set apart as `\cls` at stage 3 (decision 37).
- **1:15** *pro suo favore vocavit*, **2:21** *Dei beneficium*, **5:4** *ex beneficio excidistis*: 1573 prints them
  (*fauore*, *beneficium*); not the early *favor* of 6:18. Kept.
- **3:20** *Sequester*, **4:9** *qui fit*, **4:16** *dicendo*, **3:17** *rescindat*, **5:1** *teneri*, **4:14**
  *acceperitis*: 1573 prints them (its OCR lost line ends or turn-overs). Kept.
- **Punctuation** (1573's colons, question marks at 2:14 *cogis?*, 5:11 *infester.*): left to stage 3.
- **Spellings, left to stage 3** (decision 37's rules, and the rules in section 6): *adscendi*, *Adscendi* (1573
  *aſcendi*), *adsumto* (1573 *aſſumpto*), *adseruit* (3:13, 5:1; 1573 *aſſeruit*), *adspicientes* (1573
  *aſpiciẽtes*), *quamquam*, *quicumque* (1573 *-cunque*), *quamdiu* (1573 *Quandiu*), *quum* (1573 *cum*), *caussa*
  (1573 *cauſa*), *caritas*, *caritatem* (1573 *charit-*), *exsecratio*, *exsecrabilem*, *exsecrationi* (1573
  *execr-*; your settled *exsecr-* 5×), *exsequimini* (1573 *exequimini*), *Paullum* (1573 *Paulum*), *quidquam*
  (1573 *quicquam*), *litterae* (1573 *literae*), *heres*, *hereditas* (1573 *hær-*), *femina* (1573 *fæmina*),
  *circumcisionis*, *circumcisos* (1573 *circunc-*), *quatuordecim*, *Israëlitis*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Gal 3:19 | *lata per sequestrum* | = | *per sequestrem* | Wikisource, 1715, 1750 |
| Gal 4:14 | *ceu Dei angelum* | = | *ceu Dei nuncium* | 1573 with Wikisource, 1758, 1681, 1747, 1726 |
| Gal 4:17 | *excludere nos volunt* | = | *excludere uos* | 1747 with 1556 |
| Gal 5:2 | *si circumcidemini* | = | *si circumcidamini* | Wikisource, 1715, 1747, 1750; 1758, 1681 with 1573 |
| Gal 5:2 | *Christus nihil vobis* | = | *Christus uobis nihil* | Wikisource, 1715, 1747, 1750; 1758, 1681 with 1573 |
| Gal 5:6 | *per caritatem operans* | = | *per charitatem agens* | Wikisource, 1747, 1750; 1758, 1681 with 1573 |
| Gal 5:12 | *O utinam excidantur* | = | *excindantur* | 1715, 1750 (1747 *exscindantur*); 1758 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) word by word; three Galatians forms
have no rule yet. Proposed, not added to `data/rules/orthography.tsv`:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| *adsumto* | *assumpto* | word | 2:1 | 1573 *aſſumpto* (canvas 889); 1758, 1747, 1726; your settled *assūmptō* 9×; as the approved *assumto*, *adsumpto* → *assumpto* |
| *adseruit* | *asseruit* | word | 3:13, 5:1 (after section 1's item 26) | 1573 *aſſeruit* (canvases 890, 891); 1556 (*afferuit*, *alleruit*); your settled *asserātur*, *assertūrum*; as the approved *adseratur* → *asseratur* |
| *adspicientes* | *aspicientes* | word | 6:1 | 1573 *aſpiciẽtes* (canvas 892); 1556, 1758, 1715; your settled *aspicientēs*; as the approved *adspicient* → *aspicient* |

(2:1 *adscendi* and 2:2 *Adscendi* fall under the approved *adscendi* → *ascendi*, if the rule matches the capital.)

**Decision:** propose (Claude, 2026-11-11; for your approval)
