# Hebrews 8–13, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of 1 Timothy and Titus (`data/review/1tim1-6-stage2.md`,
`data/review/titus1-3-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277). In 1573 Hebrews follows Jude: 8:1–4 at the foot of
  canvas 932, 8:5–9:28 on 933, 10:1–11:10 on 934, 11:10–12:10 on 935, 12:10–13:25 on 936 (the Apocalypse opens on
  937). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant (section 5); its e-rara
  OCR has chapters 8–13 on pages 10282450–53, read for every place below. Stage 1 drafted Wikisource's Hebrews as
  **`text/draft/HEB.usfm`** (BSB paragraphs). `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is
  the witness `1726`, read as an OCR.
- **Wikisource's Hebrews 8–13 is the early wording**, as its other letters: *sacrarium* where 1573 has *sanctuarium*
  (8 places in 9:1–13:11), *substantia* for *subiectio* (11:1), *ac* for *et* (9:19), *faustitatem* for *felicitatem*
  (12:17), *favor* for *gratia* (13:25), each with the early-line printings 1715, 1747, 1750, and slips of its own
  (*tum*, *pecatum*, *Tun*, *rectte*, *sumu*, *adversario*, *Abramus*, *tnatos*, *Esauo*, *Esauus*, and the words
  dropped at 11:11, 12:26, 13:23). 1556 has the revised reading at 9:19, 11:1, 12:17 and 13:25, but five places are
  1573's own against 1556 (section 5): *sanctuarium* throughout (1556 *sacrarium*, as Wikisource), 9:3 *sanctissimum
  sanctuarium … aureum habens thuribulum* (1556 *sacrarium sanctius … auream habens aram suffitoriam*), 11:3 *ex non
  extantibus* (1556 *ex iis quae non extabant*), 11:23 *quod … veriti non fuerunt* (1556 *qui … veriti non sint*) and
  12:1 *onere, ambitiosoque* (1556 *fastu, tenacique*). Section 2 applies 1573's wording in all of them (decision 24).
- **Versification** (decision 5): the draft is at the KJV counts (174 verses in 8–13). 1573 and Wikisource number
  *Quod autem antiquatur ac senescit, id est prope interitum* as **8:14**; the KJV's 8:13 holds both sentences, so
  `data/versification/Heb.draft.edits.tsv` joined it to 8:13 (applied; 1573 canvas 933, on the image: *13 Dum nouum
  dixit, prius antiquauit. / 14 Quod autem antiquatur*). The draft's 8:13 keeps a line break between the two
  sentences (the join), for stage 3. Elsewhere 1573 prints every verse number in 8–13 (13:1 under the chapter's
  initial D, unnumbered) and agrees with the draft's numbering everywhere; 1573's OCR sets 11:5 after 11:8 (its
  column order), the page has it in place. Section 2c is empty.
- **Collation** (`python -m pipeline collate Heb 1-13`; `data/calibration/Heb1-13-collation.tsv`, rows Heb.8–13: 277
  places: 45 *correct*, 9 *others-1573-agrees*, 14 *others*, 203 *base-only* (145 reading, 33 division, 13 f/s, 10
  edge, 2 spelling), 6 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/Heb.8.*` to `Heb.13.*`, 64): every reading where 1573 and another printing agree against
  Wikisource, the *others* places that are readings, the base-only places whose 1573 words are Latin (8:3
  *victimas*, 8:4 *obmoueat*, 9:23 *&*, 11:4 *mortuis*, 11:23 *quòd*, 12:1 *onere ambitiosoque*, 13:3 *&*), the edge
  places (9:6 *ob-/euntes*, 9:13 *puri-/tatem*, 11:3 *cernuntur*, 11:13 *confessi*, 13:4 *pu-/niet Deus*, 13:8
  *sem-/piternum*, 13:13 *de-/decus ferentes*: all printed, lost by the OCR) and 11:26 *quam* (1573 *q̃*, the OCR ran
  it into the margin note). The rest of the base-only readings are 1573's OCR (*ininimo*, *crunt*, *nodum*, *vem*,
  *nom*, *co*, *quost*, *incenia*), abbreviations (*pmissa*, *ptulit*, *eű*), word breaks at line ends, note letters and
  margin notes run into the text, and the scripture references (section 4).
- **Every verse was read whole against 1573's page text** (canvases 932–936), not only the collation's places:
  nothing further. No L. … G. marks (Castellio's Vulgate words) occur in 8–13: none in the page text, none on the crops
  read.
- **The six uncovered verses** were read whole on the image: 9:1 *Habebat autem prius testamẽtum instituta ceremoniarum,
  ᵃ mundanumq; sanctuarium.* (crop `Heb.9.1-sanctuarium`; *sanctuarium*, section 2), 10:21 *cumq; pontificẽ habeamus,
  Dei domui pręfectũ,* (`Heb.10.21-whole`), 11:5 *Fide Enochus ita translatus est, vt mortem pas-/sus non sit: & à Deo
  translatus, nusquam extitit. / Nam ante eius translationem, testatum est eum pla-[cuisse Deo:]* (`Heb.11.5-whole`),
  12:3 *Cõsiderate verò eũ, qui tãtos ꝑtulit improborum / aduersũ se insultus, ne defatigati animos despõdeatis.*
  (`Heb.12.3-tantos`; *tantos*, section 1), 12:29 *Est enim Deus noster ᵈ ignis edax.* (`Heb.12.29-ignis`; the note
  letter *d*, which the OCR ran into *dignis*, as 1556's OCR) and 13:1 *DVret fraternus amor.* (`Heb.13.1-Duret-tall`).
  Section 2b is empty.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *fidei*,
  *fidem*, *fit*, *fuit*, *foret*, *fortes*, *ferebant*, *fertum/sertum*, *feminae*, *fusionem*, *fere*, *fuerunt*,
  *fidum*, *fidamus*) was read in its verse: all are *f*, and none is *ſ* in 1573's OCR. Every *s* word whose *f*-form
  is Latin (*si/fi*, *sit/fit*, *sine/fine*, *simus/fimus*, *solii/folii*, *seminis/feminis*, *sui/fui*, *sumus*,
  *suam*): all are *s* by sense, and the 13 places where 1573's OCR has the *f* were read on the image: 8:1 and 12:2
  *ſolij*, 8:4, 11:15, 12:8, 12:25 *ſi*, 9:28, 11:6, 12:14 *ſine*, 11:11 *ſeminis*, 12:16 *ſit*, 12:28 *ſimus*, 13:21
  *ſuam* are all long s. None found.
- **In all, 34 corrections** (37 Apply lines): 15 Wikisource slips (section 1), 15 readings of Castellio's revised text
  (section 2), 4 word divisions (section 3). Spellings (*caerimonia*, *quum*, *numquam*, *caritatem*, *exs-*,
  *adficiendum*, *adloquitur*, *adsecuti*, *inadspectabilem*, *tamquam*, *quemcumque*, *tentaretur*) are left to stage 3
  (decision 37's, 41's and 42's rules); seven forms without a rule yet are proposed (section 6). Places kept against
  1573, two of them for your eye (11:4 *mortuis*, 11:32 *Sampsone*), are in section 4.

## 1. Wikisource slips: 1573 and the other printings agree against it (15)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Hebrews 8:12** *nec eorum tum peccata* → *nec eorum peccata*. 1573 *nec [eorum] / peccata & scelera deinceps recordabor* (canvas 933); 1556 (*neceorü peccata*), 1758, 1747, 1750, 1726 (οὐ μὴ μνησθῶ). Wikisource alone.
   **Apply:** `Heb.8.12` la: `nec eorum tum peccata` → `nec eorum peccata`
2. **Hebrews 9:26** *suo sacrificio pecatum* → *peccatum*. 1573 *suo sacrificio peccatum, extitit* (canvas 933); 1758, 1747, 1750, 1726.
   **Apply:** `Heb.9.26` la: `suo sacrificio pecatum,` → `suo sacrificio peccatum,`
3. **Hebrews 10:7** *Tun dixi* → *Tunc dixi*. 1573 *7 Tunc dixi : En adsum* (canvas 934); 1758, 1726 (τότε εἶπον).
   **Apply:** `Heb.10.7` la: `Tun dixi` → `Tunc dixi`
4. **Hebrews 10:24** *et rectte facta* → *et recte facta*. 1573 *& rectè fa-/cta prouocemus* (canvas 934); 1556 (*recte facta*); the collation folds the slip, so the other printings are not listed.
   **Apply:** `Heb.10.24` la: `et rectte facta` → `et recte facta`
5. **Hebrews 10:26** *adsecuti sumu, data opera* → *sumus*. 1573 *assecuti su-/mus, data opera peccamus* (canvas 934); 1556 (*affecutí fumus*), 1758, 1726 (*assequuti sumus*), 1681, 1747. The *ad-* is stage 3's (the approved *adsecuti → assecuti*).
   **Apply:** `Heb.10.26` la: `adsecuti sumu,` → `adsecuti sumus,`
6. **Hebrews 10:27** *saevitia adversario confecturi* → *adversarios*. 1573 *sæuitia aduersarios confecturi* (canvas 934); 1556 (*aduerfatios*), 1758, 1726 (τοὺς ὑπεναντίους).
   **Apply:** `Heb.10.27` la: `saevitia adversario confecturi` → `saevitia adversarios confecturi`
7. **Hebrews 11:8** *Fide vocatus Abramus* → *Abrahamus*. 1573 *8 Fide vocatus Abrahamus obediuit* (canvas 934); 1556, 1758, 1715, 1747, 1750, 1726. The draft has *Abrahamus* at 11:17; *Abramus* is the name before Gen 17:5.
   **Apply:** `Heb.11.8` la: `vocatus Abramus` → `vocatus Abrahamus`
8. **Hebrews 11:11** *praeterque tempus peperit* → *praeterque tempus aetatis peperit*. 1573 *pręterq; tempus ætatis peperit* (canvas 935); 1556 (*tempuszrtatís*), 1758, 1750, 1715, 1747 (καὶ παρὰ καιρὸν ἡλικίας). Wikisource alone drops it.
   **Apply:** `Heb.11.11` la: `praeterque tempus peperit` → `praeterque tempus aetatis peperit`
9. **Hebrews 11:20** *Jacobo et Esauo* → *Esao*. 1573 *Iaco-/bo & Esao.* (canvas 935); 1556 (*Eso*), 1758, 1750, 1715; your settled Genesis *Esaus* 27×, *Esao* 7× (dative). Wikisource with 1747.
   **Apply:** `Heb.11.20` la: `Jacobo et Esauo` → `Jacobo et Esao`
10. **Hebrews 12:3** *eum, qui tnatos pertulit* → *tantos*. 1573 *qui tãtos ꝑtulit improborum* (canvas 935; an uncovered verse, read whole); 1556, 1758, 1715, 1747, 1750, 1681, 1726.
   **Apply:** `Heb.12.3` la: `qui tnatos pertulit` → `qui tantos pertulit`
11. **Hebrews 12:11** *fructum reddit illis, qui* → *iis*. 1573 *fructum reddit ijs, qui per eam sunt* (canvas 936); 1758 (OCR *is*), 1715, 1747. Wikisource with 1750; 1556's OCR does not reach the word.
   **Apply:** `Heb.12.11` la: `reddit illis, qui` → `reddit iis, qui`
12. **Hebrews 12:16** *ut Esauus, qui* → *Esaus*. 1573 *vt Esaus, qui* (canvas 936); 1556 (*Efaus*), 1758, 1750; your settled *Esaus* (Genesis, 27×). Wikisource with 1747.
   **Apply:** `Heb.12.16` la: `ut Esauus, qui` → `ut Esaus, qui`
13. **Hebrews 12:22** *Hierosolymam caelestem, et angelorum legiones* → without *et*. 1573 *Hierosolymam cœlestem, angelorum / legiones* (canvas 936); 1556 (*codleftem, ans £elorum*), 1758. Wikisource with 1750; the Greek has καὶ μυριάσιν ἀγγέλων, so Wikisource's *et* is not senseless. For your eye.
   **Apply:** `Heb.12.22` la: `caelestem, et angelorum` → `caelestem, angelorum`
14. **Hebrews 12:26** *Qui et tum sua voce terram denuntiavit* → *terram concussit, et nunc ita denuntiavit*. 1573 *qui & tum sua voce terram concussit, & nunc ita / denunciauit* (canvas 936; οὗ ἡ φωνὴ τὴν γῆν ἐσάλευσεν τότε, νῦν δὲ ἐπήγγελται); 1556 (OCR *terram concufsít,€ nunc ítadenunAb. ciat*), 1758, 1750. Wikisource alone drops it (*terram … terram*). The *-nt-* is the draft's spelling.
   **Apply:** `Heb.12.26` la: `terram denuntiavit` → `terram concussit, et nunc ita denuntiavit`
15. **Hebrews 13:23** *cum quo, quamprimum venerit* → *cum quo, si quamprimum venerit*. 1573 *cum / quo, si quamprimùm venerit, videbo vos* (canvas 936); 1556 (*fi quamprimüm*), 1758 (ἐὰν τάχιον ἔρχηται).
   **Apply:** `Heb.13.23` la: `cum quo, quamprimum` → `cum quo, si quamprimum`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (15)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in wording. 1556 has the
revised reading at 9:19, 11:1, 12:17 and 13:25; at the others it reads with Wikisource, and 1573's wording is a 1573
change (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Hebrews 9:1** *mundanumque sacrarium* → *sanctuarium*. 1573 *ᵃ mundanumq; sanctuarium.* (canvas 933; an uncovered verse, read whole; τό τε ἅγιον κοσμικόν). **1556** *sacrarium* (OCR *facra: s*, with its margin), with Wikisource: a 1573 change (section 5), as items 3, 4, 6, 7, 8 and 14. The draft has *Sanctuarii sacrificus* at 8:2 (1573 and 1556 alike). For your eye: eight places.
   **Apply:** `Heb.9.1` la: `mundanumque sacrarium` → `mundanumque sanctuarium`
2. **Hebrews 9:3** *quod sacrarium sanctius appellatur* → *quod sanctissimum sanctuarium appellatur*. 1573 *quod / sanctissimum sanctuarium appellatur, aureum habẽs / thuribulum* (canvas 933; Ἅγια Ἁγίων); 1758. **1556** *quod sacrarium sanctius appellatur, auream habens aram suffitoriam* (OCR *facrariü fanclfus … auream habens aram fuflitoría*): Wikisource has 1556's first half and 1573's second (section 5).
   **Apply:** `Heb.9.3` la: `quod sacrarium sanctius appellatur` → `quod sanctissimum sanctuarium appellatur`
3. **Hebrews 9:8** *patefactam esse sacrarii viam* → *sanctuarii*. 1573 *esse sanctuarij viam* (canvas 933); 1758. **1556** *sacrarij*, with Wikisource, 1715, 1747, 1750 (section 5).
   **Apply:** `Heb.9.8` la: `esse sacrarii viam` → `esse sanctuarii viam`
4. **Hebrews 9:12** *ingressus est semel in sacrarium* → *sanctuarium*. 1573 *semel in san-/ctuarium* (canvas 933); 1758. **1556** *in sacrarium* (OCR *fa^ craríum*), with Wikisource, 1747, 1750 (section 5).
   **Apply:** `Heb.9.12` la: `semel in sacrarium` → `semel in sanctuarium`
5. **Hebrews 9:19** *ipsum librum ac universum populum* → *et universum*. 1573 *ipsum librum / & vniuersum populum conspersit* (canvas 933); 1556 (*ipfum librum& uniuerfum*), 1758. The early line *ac* (Wikisource, 1715, 1747, 1750), after *lana coccina ac hyssopo*.
   **Apply:** `Heb.9.19` la: `ipsum librum ac universum` → `ipsum librum et universum`
6. **Hebrews 9:24** *in manufactum sacrarium … veri sacrarii exemplar* → *sanctuarium … sanctuarii*. 1573 *in manufactum sanctuarium ingres-/sus est Iesus, quod veri sanctuarij exemplar foret* (canvas 933); 1758, 1726. **1556** *sacrarium … sacrarij*, with Wikisource, 1715, 1750 (section 5).
   **Apply:** `Heb.9.24` la: `manufactum sacrarium ingressus` → `manufactum sanctuarium ingressus`
   **Apply:** `Heb.9.24` la: `veri sacrarii exemplar` → `veri sanctuarii exemplar`
7. **Hebrews 9:25** *pontifex ingreditur sacrarium quotannis* → *sanctuarium*. 1573 *ingreditur sanctuarium quotannis* (canvas 933); 1758. **1556** *sacrarium*, with Wikisource, 1715, 1747, 1750 (section 5).
   **Apply:** `Heb.9.25` la: `ingreditur sacrarium quotannis` → `ingreditur sanctuarium quotannis`
8. **Hebrews 10:19** *quum ad sacrarium aditum* → *sanctuarium*. 1573 *cùm ad sanctuarium aditum* (canvas 934); 1758, 1726. **1556** *sacrarium*, with Wikisource, 1715, 1747, 1750 (section 5).
   **Apply:** `Heb.10.19` la: `ad sacrarium aditum` → `ad sanctuarium aditum`
9. **Hebrews 11:1** *speratorum substantia* → *subjectio*. 1573 *Est autem fides speratorum subiectio, rerum de-/monstratio* (canvas 934), with Castellio's annotation on the verse defending *subiectio* for ὑπόστασις (*Hypostasis non significat hic propriè substantiam*, canvas 935); 1556 (*fperatorü fubiectío*), 1758. The early line *substantia* (Wikisource, 1715, 1747, 1750). The *j* is the draft's.
   **Apply:** `Heb.11.1` la: `speratorum substantia,` → `speratorum subjectio,`
10. **Hebrews 11:3** *ex iis, quae non exstabant, facta sint* → *ex non exstantibus, facta sint*. 1573 *ita vt ex non extantibus, facta sint ea quæ / cernuntur* (canvas 934; εἰς τὸ μὴ ἐκ φαινομένων); 1758. **1556** *ex ijs quae non extabant*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5). 1573's own annotation still quotes the old wording as its lemma (*Ita vt ex ijs quæ non extabant*, canvas 935). The *exs-* is the draft's spelling. For your eye.
   **Apply:** `Heb.11.3` la: `ex iis, quae non exstabant, facta` → `ex non exstantibus, facta`
11. **Hebrews 11:23** *qui puerum elegantem videntes, regis edictum veriti non sint* → *quod puerum … veriti non fuerunt*. 1573 *occul-/tatus est, quòd puerum elegantem videntes, ᶜ regis e-/dictum veriti non fuerunt.* (canvas 935; margin *c regi non paruerunt*; διότι εἶδον … καὶ οὐκ ἐφοβήθησαν); *fuerunt* also 1758, 1681. **1556** *qui … ueriti non sint* (OCR *quí puerum … ftnt*), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5). For your eye.
   **Apply:** `Heb.11.23` la: `est, qui puerum` → `est, quod puerum`
   **Apply:** `Heb.11.23` la: `veriti non sint.` → `veriti non fuerunt.`
12. **Hebrews 12:1** *deposito omni fastu, tenacique peccato* → *deposito omni onere, ambitiosoque peccato*. 1573 *deposito omni onere, ᵃ ambitiosoq; pec-/cato* (canvas 935; ὄγκον … εὐπερίστατον ἁμαρτίαν; margin, by the OCR, *a mallem nos ambiente, & quasi tu dicas, circundan-…*); 1758. **1556** *omni fastu, tenacique peccato*, with Wikisource, 1747, 1750: a 1573 change (section 5). For your eye.
   **Apply:** `Heb.12.1` la: `omni fastu, tenacique peccato` → `omni onere, ambitiosoque peccato`
13. **Hebrews 12:17** *faustitatem* (twice) → *felicitatem*. 1573 *cùm postea felicitatem obtinere vel-/let … tametsi felicitatem cum lacrimis requisierit* (canvas 936; τὴν εὐλογίαν); 1556 (*felicitatem obtinere*), 1758. The early line *faustitatem* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Heb.12.17` la: `postea faustitatem obtinere` → `postea felicitatem obtinere`
   **Apply:** `Heb.12.17` la: `tametsi faustitatem cum` → `tametsi felicitatem cum`
14. **Hebrews 13:11** *sanguis in sacrarium infertur* → *sanctuarium*. 1573 *sanguis in sanctua-/rium infertur* (canvas 936); 1758. **1556** *sacrarium*, with Wikisource, 1747, 1750 (section 5).
   **Apply:** `Heb.13.11` la: `in sacrarium infertur` → `in sanctuarium infertur`
15. **Hebrews 13:25** *Adsit vobis omnibus favor* → *gratia*. 1573 *25 Adsit vobis omnibus gratia. Amen.* (canvas 936), ἡ χάρις; 1556 (*omnibusgratíat*), 1758. The early line *favor* (Wikisource, 1715, 1747), as Titus 3:15.
   **Apply:** `Heb.13.25` la: `omnibus favor:` → `omnibus gratia:`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The six uncovered verses (9:1, 10:21, 11:5, 12:3, 12:29, 13:1) were read whole on the image (intro): their only
differences from the draft, 9:1 *sanctuarium* and 12:3 *tantos*, are already sections 2 and 1. No decision needed.

## 2c. Verse boundaries (0)

None beyond the 8:13–14 join already applied by the edits file (intro). No decision needed.

## 3. Word division (4)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **Hebrews 9:7** *pro seipso, et pro populi* → *pro se ipso*. Your settled *se ipso* (9×) and *se ipsum* (28×) against *seipsum* 4× (Acts, Romans), as Titus 3:11. Not a quotation. 1573 joins it (*seipso*, canvas 933).
   **Apply:** `Heb.9.7` la: `pro seipso,` → `pro se ipso,`
2. **Hebrews 9:14** *per aeternum Spiritum seipsum libavit* → *se ipsum*. As item 1; 1573 *seipsum* (canvas 933).
   **Apply:** `Heb.9.14` la: `Spiritum seipsum libavit` → `Spiritum se ipsum libavit`
3. **Hebrews 9:25** *Neque ut saepe seipsum libaret* → *se ipsum*. As item 1; 1573 *seipsum* (canvas 933).
   **Apply:** `Heb.9.25` la: `saepe seipsum libaret` → `saepe se ipsum libaret`
4. **Hebrews 9:24** *in manufactum sanctuarium* → *in manu factum sanctuarium*. The draft divides it at 9:11 (*non manu factum*), and your settled text has *manu factum/facta* 4× (Mark 2×, Ephesians, Colossians) against *manufactis* 2× (Acts). 1573 joins both (*manufactum*, *ma-/nufactum*, canvas 933), and 1758 and 1715 at 9:11. For your eye: the alternative is to join 9:11. (After section 2's item 6.)
   **Apply:** `Heb.9.24` la: `in manufactum sanctuarium` → `in manu factum sanctuarium`

## 4. Checked and kept

- **11:4** *et per eamdem mortuus adhuc loquitur*: 1573 prints *per ean-/dem ᵃ mortuis adhuc loquitur* (canvas 934, on
  the image; margin *a cùm eius sanguis ad Deum conqueri dicitur: vide infra cap. 12*), against 1556 (*per eandem
  mortuus*), 1758, 1715, 1747, 1750 and ἀποθανὼν ἔτι λαλεῖ. Taken as a 1573 misprint; *mortuus* kept. For your eye.
- **11:32** *Gedeone, Baraco, Samsone*: 1573 *Sampsone* (canvas 935, on the image), with 1556, 1758, 1715, 1726;
  Wikisource *Samsone* with 1747, 1750. A spelling of the name (as *sumtus/sumptus*); left to stage 3, no settled
  form yet. For your eye.
- **9:23** *Necesse est ergo, caelestium exempla*: 1573's OCR *&* is the note letter *b* (canvas 933, on the image;
  margin *b rerum spiritualium*). No word missing.
- **13:3** *et calamitosorum, ut qui sitis*: 1573's OCR *& vt* is the note letter *a* (canvas 936, on the image;
  margin *a quod vobis eadẽ possunt vsu venire*); 1556's OCR has no *et* either. No word missing.
- **12:29** *ignis edax*: 1573's *dignis* is the note letter *d* before *ignis* (canvas 936, on the image); 1556's OCR
  reads it the same way.
- **8:3** *munera victimasque libandas*: 1573 *victimasq;* (canvas 932, on the image; its OCR *victimas :*). Agrees.
- **8:4** *munera obmoveant*: 1573 *obmoueãt* (canvas 932, the bar for *n*). Agrees.
- **9:13** *juvencaeque cinis … corporis puritatem*: 1573 *iuuẽcæq; … puri-/tatem* (canvas 933, on the image). Agrees.
- **9:11** *non manu factum*: 1573 *ma-/nufactum*; kept divided (section 3, item 4).
- **10:34** *penes vos ipsos*: 1573 *vosipsos* (canvas 934); kept divided, as your settled *vos ipsos* (8×).
- **Edge places, printed in 1573** (on the image): 9:6 *ob-/euntes*, 11:3 *cernuntur* (a line of its own), 11:13
  *confessi* (a line of its own), 13:4 *pu-/niet Deus*, 13:8 *sem-/piternum*, 13:13 *de-/decus ferentes* (at the head
  of the next column), 11:26 *quam* (1573 *q̃*, run by the OCR into the margin note *d pro Christo patiendum*). Kept.
- **The *others* and *others-1573-agrees* places**: 8:6 *promissis*, 9:9 *possent*, 10:6 *delectaris*, 10:38 *est
  acceptus*, 11:8 *profectus*, 12:13 *rectas*, 12:21 *spectaculum*, 12:22 *accessistis*, 13:24 *sanctos* are other
  printings' OCR; 9:11 *manu factum* (1758, 1715 join), 11:4 *eamdem* (*eandem*), and the spellings 9:1, 9:6, 9:21
  *caerimon-*, 9:28 *exspectantibus*, 10:29 *adfecerit*, 11:5 *exstitit*, 11:27 *tamquam*, 11:35 *adsequerentur*,
  12:17 *lacrimis*, 13:21 *exsequendam* are stage 3's. 12:3 *tnatos* is section 1. Kept.
- **Note letters and margin notes**, not text: 8:5 *a* (*eorum cultus exemplum rerum caelestium*), 9:1 *a*, 9:23 *b*,
  10:23 *a* (*a speremus firmissime felicitatem, quam nos sperare profitemur*), 11:4 *a*, 11:14 *b* (*se esse
  peregrinos*), 11:23 *c* (*regi non paruerunt*), 11:26 *d* (*pro Christo patiendum*), 11:27 *e* (*Deum*), 11:37
  (*illa liberatio*), 12:1 *a*, 12:17 *a* (*nihil ei profuisse paenitentiam*), 12:18 *b* (*tam den[…] obductum: ut
  tactu, non visu adeundus*), 12:28 *c* (*scilicet*), 12:29 *d*, 13:3 *a*, 13:7 *b* (*quales efficiantur
  eorum mores, quorum causa fit fides*), 13:8 *c* (*ut Christus […]tuo manet, ita debetis eandem do[…]petuo
  tene[…]*), as the OCR reads them; the scripture references in the margin (as the OCR reads them: 8:8 *Iere. 31. 31*, 9:5 *Num. 17. 10*,
  9:12 *Leuit. 16. 14*, 9:20 *Exod. 24. 8*, 10:16 *Ierem. 31. 31, Supra 8. 8*, 10:26 *Supra 6. 4*, 10:28 *Deut. 19. 15*,
  10:30 *Rom. 12. 19*, 13:20 *1. Pet. 5. 4*, and others); the chapter summaries before 9:1, 10:1, 11:1, 12:1, 13:1; and 1573's
  annotations after chapters 9, 11 and 13.
- **13:25** the subscription (*Missa ex Italia per Timotheum*): 1573 sets it in italics under the verse (canvas 936,
  *Missa ex Italia per Timotheum.*); the draft has it in the verse. Set apart as `\cls` at stage 3 (decision 37).
- **Punctuation and capitals, left to stage 3**: 8:8 *Futurum* (1573 a capital after the colon), 8:10 *Dominus:*
  (1573 a stop, *Indam*), 10:28 *mosaicam* (1573 *Mosaicam*), 12:9 *reverebamur?* (1573 a comma), 12:21 *dixerit:*
  (1573 a stop), 13:6 *est:*, 13:17 *gementes:* (1573 a stop), 13:25 *gratia:* (1573 a stop), and the draft's line break
  inside 8:13 (the join).
- **Spellings, left to stage 3** (decision 37's, 41's and 42's rules, and section 6): *caerimoniis*, *caerimoniarum*,
  *caerimonias* (1573 *ceremon-*; the approved stem *ceremoni → cærimoni*), *quum*, *Quumque* (1573 *cùm*, *Cumq;*),
  *numquam* (1573 *nunquam*), *caritatem* (1573 *charitatem*), *turibulum* (1573 *thuribulum*), *adspergens*,
  *adficiendum*, *adfecerit*, *adsecuti*, *adspiceret*, *adsequerentur*, *adloquitur*, *adsiduum* (1573 *as-*, *aff-*,
  *all-*), *inadspectabilem* (1573 *inaspectabilem*), *exstitit*, *exstruxit*, *exstinxerunt*, *exstabant*, *exsequar*,
  *exsequendam*, *exsecuti*, *exspectans*, *Exspectabat*, *exspectatio*, *exspectantibus* (1573 *ext-*, *exe-*,
  *expect-*), *oblitterandum* (1573 *obliterandum*), *perpaullo* (1573 *perpaulo*), *tamquam* (1573 *tanquam*),
  *quemcumque* (1573 *quemcunq;*), *eamdem* (1573 *eandem*), *hereditatem*, *coheredibus* (1573 *hære-*), *litoris*
  (1573 *littoris*), *feminae* (1573 *fœminæ*), *obturarunt* (1573 *obthurarunt*), *tentaretur*, *tentati*, *saeculorum*
  (1573 *seculorum*), *denuntiavit* (1573 *denunciauit*), *lacrimis*, *intelligimus*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282450–53), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Heb 9:1, 9:8, 9:12, 9:24 (twice), 9:25, 10:19, 13:11 | *sanctuarium*, *sanctuarii* | = | *sacrarium*, *sacrarii* | Wikisource, 1715, 1747, 1750 with 1556; 1758 (and 1726 at 9:24, 10:19) with 1573. 8:2 *sanctuarii* in both |
| Heb 9:3 | *quod sanctissimum sanctuarium appellatur, aureum habens turibulum* | = (*thuribulum*) | *quod sacrarium sanctius appellatur, auream habens aram suffitoriam* | Wikisource *sacrarium sanctius … aureum habens turibulum*; 1758 with 1573 |
| Heb 11:3 | *ex non exstantibus* | = (*extantibus*) | *ex iis quae non extabant* | Wikisource, 1715, 1747, 1750 with 1556; 1758 with 1573; 1573's annotation quotes 1556's wording |
| Heb 11:4 | *per eamdem mortuus* | *per eandem mortuis* | *per eandem mortuus* | the text keeps 1556's (section 4); every other printing *mortuus* |
| Heb 11:23 | *quod puerum … veriti non fuerunt* | = | *qui puerum … veriti non sint* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 *fuerunt* |
| Heb 12:1 | *deposito omni onere, ambitiosoque peccato* | = | *deposito omni fastu, tenacique peccato* | Wikisource, 1747, 1750 with 1556; 1758 with 1573 |

1556's OCR at 12:26 reads *ítadenunAb. ciat*, perhaps *denunciat* against 1573's *denunciauit*; not recorded without
the page image.

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) and writes *tempto*, word by word;
these Hebrews 8–13 forms have no row in `data/rules/orthography.tsv` yet (checked with `normalize.word_rules()`, stems
included). Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adspergens | aspergens | word | 9:13 | 1573 *aspergens* (canvas 933, on the image); 1556, 1747; as the approved *adspice → aspice* |
| adfecerit | affecerit | word | 10:29 | 1573 *affecerit* (canvas 934); 1758, 1747; your settled *affecerim*; as the approved *adfecit → affecit* |
| adspiceret | aspiceret | word | 11:27 | 1573 *aspiceret* (canvas 935); 1758, 1715, 1747; your settled *aspicere* |
| adsequerentur | assequerentur | word | 11:35 | 1573 *assequerentur* (canvas 935); 1758, 1715, 1747; as the approved *adsequantur → assequantur* |
| adsiduum | assiduum | word | 13:15 | 1573 *assiduum* (canvas 936); 1758, 1726; your settled *assiduus*, *assidui*; as the approved *adsiduus → assiduus* |
| tentati | temptati | word | 11:37 | 1573 *tentati* (canvas 935); decision 37's *tempto*; your settled *temptatis*, *temptatus* |
| perpaullo | perpaulo | word | 10:37 | 1573 *perpaulo* (canvas 934); 1758, 1715, 1747, 1726; the approved *paullo → paulo* and stem *paull → paul* reach only words that begin with it |

(10:7–8 *adsum*, 13:5 *adsunt* and 13:25 *Adsit* are compounds of *sum*, left as they are; 11:7 *admonitus* does not
assimilate.)

**Decision:** accept (Claude, 2026-11-12, under decisions 37 and 42; added to `data/rules/orthography.tsv`)
