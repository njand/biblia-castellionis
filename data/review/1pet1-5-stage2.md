# 1 Peter 1–5, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of James (`data/review/jas1-5-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 919–922: the title and Athanasius's
  argument at the foot of 919, 1:1–2:21 on 920, 2:22–4:14 on 921, 4:14–5:14 on 922). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5); its e-rara OCR has 1 Peter on pages 10282441–43
  and reaches most of the letter, though in two interleaved columns (it does not reach 1:1–2 whole, 3:6–8 cleanly, or
  4:16's first words). Stage 1 drafted Wikisource's 1 Peter as **`text/draft/1PE.usfm`** (BSB paragraphs). You have no
  earlier work on 1 Peter; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`,
  read as an OCR.
- **Wikisource's 1 Peter is the early wording**, as its James: *praescito* (1:2), *favorem* (1:2, 5:10), *Praecogniti*
  (1:20), *diffidentes* (2:8), *genus lectum … mirabilem* (2:9), *et peregrinos* (2:11), *faustitatem* (3:9), *animis*
  (3:19), *Quibus olim persuasum non fuerat* (3:20), *baptismus nos … qui … testificatio* (3:21), *pro nobis corpore*
  (4:1–2), *modestiam complectimini* (5:5), *vester* (5:8), each with the early-line printings 1715, 1747, 1750, and
  slips of its own (*Capadocia*, *invictam*, *et diffidentes*, *sibi Dei conscius*, *elementia*, *tempora*, *cultris*,
  *incipat*, *ad mirari*, *sylvanum*). 1556 has the revised reading at 1:2 *gratiam*, 2:9, 2:11, 3:9, 3:19, 3:21
  *baptisma vos … quod*, 4:1–2, 5:8 and 5:10; it reads with Wikisource at 1:20 *praecogniti*, 2:8 *diffidentes*, 3:20
  *quibus olim persuasum non fuerat* (without *semel*), 3:21 *testificatio* and 5:5 *modestiam complectemini*: those
  are 1573's changes (section 5), as are some readings 1556 has of its own (2:2, 3:6, 5:9).
- **Versification** (decision 5): the draft is at the KJV counts (105 verses), no edits file. 1573 prints every verse
  number and agrees with the KJV everywhere but **3:10–12**: 1573 runs *declinet malum … eamque persequatur* into 10,
  numbers *Habet enim Dominus oculos … implorationem* 11 and *Faciem autem …* 12 (canvas 921); the KJV's 3:11 is *Let
  him eschew evil*, as the draft. Kept. At **1:24–25** the draft (Wikisource) starts 25 with *Aret herba, caditque
  flos*; 1573 prints it in 24, as the KJV (*The grass withereth*): moved back (section 2c).
- **Collation** (`python -m pipeline collate 1Pet 1-5`; `data/calibration/1Pet1-5-collation.tsv`, 198 places: 41
  *correct*, 6 *others-1573-agrees*, 10 *others*, 137 *base-only* (95 reading, 27 division, 11 f/s, 3 edge, 1
  spelling), 4 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/1Pet.*`, 35): every reading where 1573 and another printing agree against Wikisource, the
  *others* places that touch the text (1:2 *secundum*, 1:4 *invietam*, 1:20 *provisi*, 4:12 *admirari*), every
  base-only reading whose 1573 words are Latin (1:2 *secundum … prouidentiam*, 1:20 *prouisi*, 2:9 *admirabilem*, 2:11
  *ac*, 3:20 *semel*, 3:21 *baptisma vos*, 4:2 *vidat* (*viuat* on the image), 4:9 *&* (the note letter *d*), 5:8
  *noster*), the edge places (1:6 *Ac in eo*, 1:11 *Scrutantes*, 1:25 *nunciatum*, 4:7 *Omnium autem*: all printed)
  and the lines the OCR lost (1:2 *cem plurimam dicit*, 3:12 *leficos*, 4:5 *iudicaturus*, 4:11 *la: Amen*, 5:7 *ræ
  sitis*: all printed as the draft). The rest of the base-only readings are 1573's OCR (*sparsiın*, *repositain*,
  *cóferédo*, *fermone*, *lapiden*, *vercimini*, *potentatibusós*, *coronaın*, *inanui*), word breaks at line ends
  (*salu tem*, *impro batum*, *ann guli*, *amen tium*, *ma leficis*), words run together (*adimmortalem*,
  *quialiquando*, *vtab*, *nobisiniuriam*, *Absitenim*, *Similiteriuniores*), note letters and margin notes run into the
  text (section 4), the running head (4:14 *I PETRI EPISTOLA*) and the chapter summaries. Each place was also read
  against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 920–922), not only the collation's places: it
  found the verse boundary at 1:24–25 (section 2c) and that 3:20's *Quibus olim persuasum non fuerat* is 1573's *qui
  olim non paruerant … semel*, which the collation had split into four places; nothing further.
- **The four uncovered verses** (1573's OCR 46–50% of the words) were read whole on the image: 1:4 *ad immortalem,
  impollutam, & inuietam hæredi-tatem, vobis in cœlis repositam,* (crop `1Pet.1.4-inuietam`), 1:6 *Ac in eo sanè
  exultatis, paululum modò (ᵃ si est opus) varijs tentationibus vexati,* (`1Pet.1.6-exultatis`), 1:9 *reportaturi ᵇ
  fidei vestrę finẽ, salutem animorum.* (`1Pet.1.9-reportaturi`) and 4:8 *ac ante omnia mutuam charitatem intentam
  ha-bete: nam charitas multa peccata ᶜ tegit,* (`1Pet.4.8-charitatem`). Only 1:4 differs from the draft but in spelling
  (*invietam*, section 1).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *fides*,
  *fidei*, *fidem*, *fit*, *ferat/serat*, *feratis*, *fiet*, *fuerat/suerat*, *confidet/considet*, *confiditis*,
  *diffidentes*, *fur*) was read in its verse: all are *f* by sense and on the page. Every *s* word whose *f*-form is
  Latin (*si/fi*, *sit/fit*, *sitis*, *sine/fine*, *satis/fatis*): all are *s* by sense, and the places where 1573's OCR
  has the *f* and the *f*-form could be construed were read on the image: 1:21 *vt ſit veſtra fides*
  (`1Pet.1.21-sit`), 2:19 *ſibi ſit Dei conſcius* and 2:20 *ſi peccantes* (`1Pet.2.19-sit`), 4:9 *ſine murmuribus*
  (`1Pet.4.9-et`) are all long s. None found.
- **In all, 29 corrections**: 9 Wikisource slips (section 1), 18 readings of Castellio's revised text (section 2), 1
  verse boundary (section 2c), 1 word division (section 3). Spellings (*quum*, *carissimi*, *caritatem*, *tamquam*,
  *Quamquam*, *quicumque*, *numquam*, *paullulum*, *paullum*, *exsultatis*, *exsistet*, *exstitit*, *exspectaret*,
  *exstrueretur*, *eamdem*, *adfecti*, *obediant*, *submittite*, *vocauit*, …) are left to stage 3 (decisions 37 and
  42's rules); five rules proposed (section 6). Twelve places where 1556 reads against 1573 are recorded (section 5),
  four of them from a doubtful OCR. One reading of 1573 is kept out as a probable misprint (4:16 *aut*, section 4).

## 1. Wikisource slips: 1573 and the other printings agree against it (9)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **1 Peter 1:1** *Galatia, Capadocia, Asia* → *Cappadocia*. 1573 *Ponto, Galatia, Cappadocia, Aſia / & Bithynia,* (canvas 920, crop `1Pet.1.1-Cappadocia`), Καππαδοκίας; 1556 (OCR *Cappadocia*), 1758, 1681, 1750, 1726; your settled *Cappadociæ* (Acts 2:9). Wikisource alone.
   **Apply:** `1Pet.1.1` la: `Galatia, Capadocia, Asia` → `Galatia, Cappadocia, Asia`
2. **1 Peter 1:4** *et invictam hereditatem* → *et invietam hereditatem*. 1573 *impollutam, & inuietam hæredi-/tatem* (canvas 920, crop `1Pet.1.4-inuietam`: an *e*, not a *c*); 1556 (OCR *ínutetam*), 1758 (*invietam*), 1747, 1750 (*inuietam*), 1726 (*invietam*): every printing. Castellio's word for ἀμάραντον, *unfading*: *in-* and *viētus*, withered (Gaffiot *vĭētus*, of *vieō*); `python -m pipeline latin macron invietam` finds no source for the compound itself. Wikisource made it the common *invictam*. For your eye.
   **Apply:** `1Pet.1.4` la: `et invictam hereditatem` → `et invietam hereditatem`
3. **1 Peter 2:8** *offendunt, et diffidentes* → *offendunt, ei diffidentes*. 1573 *offendunt, ei inobedientes, ad / quod erant destinati.* (canvas 920, crop `1Pet.2.8-inobedientes`), *disobedient to it* (the word), τῷ λόγῳ ἀπειθοῦντες; 1556 (OCR *eí difiidentes*), 1758, 1750 (*ei diffidentes*). 1715, 1747 *et* with Wikisource. The participle is section 2's.
   **Apply:** `1Pet.2.8` la: `offendunt, et diffidentes,` → `offendunt, ei diffidentes,`
4. **1 Peter 2:19** *quoniam sibi Dei conscius* → *quoniam sibi sit Dei conscius*. 1573 *quoniam / ᵇ ſibi ſit Dei conſcius, dolores fert* (canvas 920, crop `1Pet.2.19-sit`); 1556 (OCR *fit Dei conífcíus*), 1758, 1681, 1715, 1747, 1726. 1750 lacks it with Wikisource.
   **Apply:** `1Pet.2.19` la: `quoniam sibi Dei conscius` → `quoniam sibi sit Dei conscius`
5. **1 Peter 3:20** *Dei elementia* → *Dei clementia*. 1573 *Dei clementia, temporibus Noæ* (canvas 921, crop `1Pet.3.20-paruerant`), ἡ τοῦ Θεοῦ μακροθυμία; 1556 (OCR *Dei cleme-tía*), 1758, 1681, 1715, 1747, 1750. Wikisource alone.
   **Apply:** `1Pet.3.20` la: `Dei elementia,` → `Dei clementia,`
6. **1 Peter 4:3** *praeterito vitae tempora extraneis* → *tempore*. 1573 *præterito vitæ tempore ex-/traneis* (canvas 921, crop `1Pet.4.3-tempore`), the ablative; 1556 (OCR *prateríto uíte tempore*), 1758, 1747, 1750. Wikisource alone.
   **Apply:** `1Pet.4.3` la: `praeterito vitae tempora extraneis` → `praeterito vitae tempore extraneis`
7. **1 Peter 4:3** *deastrorum cultris* → *culturis*. 1573 *& nefarijs deaſtrorum culturis.* (canvas 921, crop `1Pet.4.3-culturis`); 1556 (OCR *culurís*), 1758, 1750. Wikisource alone.
   **Apply:** `1Pet.4.3` la: `deastrorum cultris.` → `deastrorum culturis.`
8. **1 Peter 4:17** *a divina domo incipat* → *incipiat*. 1573 *diuina ʰ domo incipiat.* (canvas 922, crop `1Pet.4.17-incipiat`; margin *h familia gente*); 1556 (OCR *íncipíat*), 1758, 1681, 1715, 1747, 1750. Wikisource alone.
   **Apply:** `1Pet.4.17` la: `domo incipat.` → `domo incipiat.`
9. **1 Peter 5:12** *Per sylvanum* → *Per Sylvanum*. 1573 *Per Syluanum vobis, fidum* (canvas 922); 1556 (*Per Syluanum*), 1758, 1681, 1750 (1747 *Siluanum*); Silas's name (Σιλουανοῦ). The approved rule *Sylvanum → Silvanum* (2 Cor 1:19) reaches it but keeps Wikisource's lower case (`normalize.propose()` gives *silvānum*); with the capital, stage 3 makes it *Silvānum*, as your settled 2 Cor 1:19.
   **Apply:** `1Pet.5.12` la: `Per sylvanum,` → `Per Sylvanum,`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (18)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too where its OCR can be read, except 1:20, 2:8, 3:20, 3:21 *stipulatio* and 5:5 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **1 Peter 1:2** *Dei patris praescito electis* → *Secundum Dei patris providentiam electis*. 1573 *2 ſecũdùm Dei patris prouiden-/tiam electis* (canvas 920, crop `1Pet.1.2-secundum`), κατὰ πρόγνωσιν; 1758 (its *secundum* closes the line above, the collation's edge place), 1681 (*Dei Patris providentiam*), 1726 (*secundum … providentiam*). The early line *Dei patris praescito* (Wikisource, 1747, 1750). **1556** reads otherwise (OCR *…trís preícitum fecun-dum electis*, perhaps *praescitum secundum*; section 5). The capital follows the draft's verse openings. For your eye.
   **Apply:** `1Pet.1.2` la: `Dei patris praescito electis` → `Secundum Dei patris providentiam electis`
2. **1 Peter 1:2** *favorem et pacem plurimam dicit* → *gratiam et pacem*. 1573 *ne conſpergantur, gratiam & pa-/cem plurimam dicit.* (canvas 920, crops `1Pet.1.2-gratiam`, `1Pet.1.2-plurimam`: the second line is outside the OCR); 1556 (OCR *gratíam*), 1758, 1681, 1726. The early line *favorem* (Wikisource, 1747, 1750), as Titus 3:15.
   **Apply:** `1Pet.1.2` la: `conspergantur, favorem et pacem` → `conspergantur, gratiam et pacem`
3. **1 Peter 1:20** *Praecogniti ante orbem conditum* → *Provisi*. 1573 *20 prouiſi ante orbem conditum* (canvas 920, crop `1Pet.1.20-prouisi`); 1758, 1726. **1556** *praecogniti* (OCR), with Wikisource, 1747, 1750: a 1573 change (section 5).
   **Apply:** `1Pet.1.20` la: `Praecogniti ante orbem` → `Provisi ante orbem`
4. **1 Peter 2:8** *ei diffidentes* → *ei inobedientes* (after section 1's item 3). 1573 *ei inobedientes* (canvas 920, crop `1Pet.2.8-inobedientes`), ἀπειθοῦντες; 1758, 1726 (*inobedientes*). **1556** *ei diffidentes* (OCR), with 1750 and the early line: a 1573 change (section 5).
   **Apply:** `1Pet.2.8` la: `ei diffidentes,` → `ei inobedientes,`
5. **1 Peter 2:9** *At vos genus lectum estis* → *lectum genus*. 1573 *9 At vos lectum genus eſtis* (canvas 920, crop `1Pet.2.9-lectum`); 1556 (OCR *lectü genus*), 1758, 1681, 1726. The early line *genus lectum* (Wikisource, 1715, 1747, 1750).
   **Apply:** `1Pet.2.9` la: `At vos genus lectum estis` → `At vos lectum genus estis`
6. **1 Peter 2:9** *in suam lucem mirabilem* → *admirabilem*. 1573 *in ſuã lucem admirabilẽ vocauit:* (canvas 920, crop `1Pet.2.9-lectum`); 1556 (OCR *lücem admirabilem*), 1758, 1681, 1726. The early line *mirabilem* (Wikisource, 1715, 1747, 1750).
   **Apply:** `1Pet.2.9` la: `lucem mirabilem vocauit` → `lucem admirabilem vocauit`
7. **1 Peter 2:11** *ut inquilinos et peregrinos* → *ac peregrinos*. 1573 *cohortor vt inquilinos ac peregrinos:* (canvas 920, crop `1Pet.2.11-ac`); 1556 (OCR *inquilinosac*), 1758. The early line *et* (Wikisource, 1715, 1747, 1750).
   **Apply:** `1Pet.2.11` la: `inquilinos et peregrinos` → `inquilinos ac peregrinos`
8. **1 Peter 3:9** *ut faustitatem obtineatis* → *felicitatem*. 1573 *vt felicitatem obtineatis.* (canvas 921, crop `1Pet.3.9-felicitatem`); 1556 (OCR *felícicitate obtíneatís*), 1758. The early line *faustitatem* (Wikisource, 1715, 1747, 1750).
   **Apply:** `1Pet.3.9` la: `ut faustitatem obtineatis` → `ut felicitatem obtineatis`
9. **1 Peter 3:19** *In quo etiam animis* → *spiritibus*. 1573 *in quo etiam ſpiritibus, qui erant in carcere* (canvas 921, crop `1Pet.3.19-spiritibus`), τοῖς … πνεύμασι; 1556 (OCR *fpírítibus*), 1758, 1681. The early line *animis* (Wikisource, 1715, 1750).
   **Apply:** `1Pet.3.19` la: `etiam animis, qui` → `etiam spiritibus, qui`
10. **1 Peter 3:20** *Quibus olim persuasum non fuerat, quum exspectaret* → *Qui olim non paruerant, quum semel exspectaret*. 1573 *20 qui olim non paruerant, cùm ſemel expectaret* (canvas 921, crop `1Pet.3.20-paruerant`), ἀπειθήσασί ποτε, ὅτε ἅπαξ ἐξεδέχετο; 1758, 1681. **1556** *quibus olim persuasum non fuerat, cum expectaret* (OCR), with Wikisource, 1715, 1747, 1750: both the verb and *semel* are 1573's (section 5). *quum* and *exsp-* are the draft's spelling, left to stage 3.
    **Apply:** `1Pet.3.20` la: `Quibus olim persuasum non fuerat, quum exspectaret` → `Qui olim non paruerant, quum semel exspectaret`
11. **1 Peter 3:21** *baptismus nos servat, qui non est* → *baptisma vos servat, quod non est*. 1573 *nunc quoque baptiſma vos ſer-/uat, quod non eſt* (canvas 921, crop `1Pet.3.21-baptisma`); 1556 (OCR *ba-ptí(ima uos feruat, quod nó eft*), 1758, 1681. The early line *baptismus nos … qui* (Wikisource, 1747, 1750). For your eye: *vos* against the TR (ἡμᾶς), as both of Castellio's last texts print it.
    **Apply:** `1Pet.3.21` la: `baptismus nos servat, qui non est` → `baptisma vos servat, quod non est`
12. **1 Peter 3:21** *conscientiae testificatio ad Deum* → *stipulatio*. 1573 *bonæ conſcientiæ ſtipulatio ad Deum* (canvas 921, crop `1Pet.3.21-baptisma`), ἐπερώτημα; 1758, 1681. **1556** *testificatio* (OCR), with Wikisource, 1747, 1750: a 1573 change (section 5).
    **Apply:** `1Pet.3.21` la: `conscientiae testificatio ad` → `conscientiae stipulatio ad`
13. **1 Peter 4:1** *Christo pro nobis corpore supplicium passo* → *pro vobis carne*. 1573 *Gitur Chriſto pro vobis carne ſupplicium paſſo* (canvas 921, crop `1Pet.4.1-carne`); 1556 (OCR *pro uobís carne*), 1758, 1726. The early line *pro nobis corpore* (Wikisource, 1747, 1750); 1681 *pro nobis carne*. *vobis* against the Greek (ὑπὲρ ἡμῶν), as both of Castellio's last texts print it.
    **Apply:** `1Pet.4.1` la: `pro nobis corpore supplicium passo` → `pro vobis carne supplicium passo`
14. **1 Peter 4:1** *qui corpore supplicium tulit* → *qui carne*. 1573 *ſiquidem qui / carne ſupplicium tulit* (canvas 921, crop `1Pet.4.1-carne`), ἐν σαρκί; 1556 (OCR *quí carne fupplícíum tulít*), 1758, 1681, 1726. The early line *corpore* (Wikisource, 1747, 1750).
    **Apply:** `1Pet.4.1` la: `qui corpore supplicium tulit` → `qui carne supplicium tulit`
15. **1 Peter 4:2** *reliquum in corpore tempus* → *in carne*. 1573 *reliquum in carne tempus viuat.* (canvas 921, crop `1Pet.4.3-tempore`, its first line; the OCR's *vidat* is *viuat*); 1556 (OCR *ín carne tempus*), 1758, 1681, 1726. The early line *corpore* (Wikisource, 1747, 1750).
    **Apply:** `1Pet.4.2` la: `reliquum in corpore tempus` → `reliquum in carne tempus`
16. **1 Peter 5:5** *obsequendo, modestiam complectimini* → *modestia ornamini*. 1573 *obſequendo modeſtia ornamini: nam Deus &* (canvas 922, crop `1Pet.5.5-modestia`), τὴν ταπεινοφροσύνην ἐγκομβώσασθε; 1758, 1681. **1556** *modestiam complectemini* (OCR), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5).
    **Apply:** `1Pet.5.5` la: `obsequendo, modestiam complectimini:` → `obsequendo, modestia ornamini:`
17. **1 Peter 5:8** *nam adversarius vester diabolus* → *noster*. 1573 *nam aduerſarius noſter Dia-/bolus* (canvas 922, crop `1Pet.5.8-noster`, and the head of the next column, `1Pet.5.7-curae+next`); 1556 (OCR *aduerfarías nofter Diabolus*), 1758, 1681. The early line *vester* (Wikisource, 1715, 1747, 1750), as the Greek (ὁ ἀντίδικος ὑμῶν) and the Vulgate. For your eye: Castellio's two last texts both read *noster*.
    **Apply:** `1Pet.5.8` la: `adversarius vester diabolus` → `adversarius noster diabolus`
18. **1 Peter 5:10** *Deus vero omnis favoris* → *gratiae*. 1573 *Deus verò omnis gratiæ, qui nos ad æternam* (canvas 922, crop `1Pet.5.10-gratiae`), πάσης χάριτος; 1556 (OCR *gratíz*), 1758, 1681. The early line *favoris* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1Pet.5.10` la: `omnis favoris,` → `omnis gratiae,`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The four uncovered verses (1:4, 1:6, 1:9, 4:8) were read whole on the image (intro): only 1:4 *invietam* differs
(section 1, item 2). The lines the OCR lost (1:2, 3:12, 4:5, 4:11, 5:7) are printed as the draft has them. No decision
needed.

## 2c. Verse boundaries (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **1 Peter 1:24–25**: *Aret herba, caditque flos:* closes 24. 1573 *velut herbæ flos. Aret / herba, caditq; flos: / 25 at Domini dictũ manet* (canvas 920, crop `1Pet.1.24-Aret`), with 1556 (OCR, no numbers to show it), and 1715, 1747 and 1726 print *25* before *At Domini*; the KJV's 1:24 ends *and the flower thereof falleth away* (Ἐξηράνθη ὁ χόρτος, καὶ τὸ ἄνθος αὐτοῦ ἐξέπεσε). Wikisource starts 25 with it. The capital of *At* follows the draft's verse openings.
   **Apply:** `1Pet.1.24` la: `velut herbae flos.` → `velut herbae flos. Aret herba, caditque flos:`
   **Apply:** `1Pet.1.25` la: `Aret herba, caditque flos: at Domini` → `At Domini`

## 3. Word division (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **1 Peter 4:12** *quasi novum aliquid vobis usu veniat, ad mirari* → *admirari*. 1573 *vobis vſuueniat, admirari:* (canvas 921, crop `1Pet.4.12-admirari`); 1556 (OCR *admíratí*), 1681, 1715, 1750 *admirari*; Wikisource alone divides it (μὴ ξενίζεσθε; your settled *admīrārī*).
   **Apply:** `1Pet.4.12` la: `veniat, ad mirari:` → `veniat, admirari:`

## 4. Checked and kept

- **4:16** *At si ut Christianus, ne pudeat eum*: 1573 prints *16 aut ſi vt Chriſtianus* (canvas 922, crop
  `1Pet.4.16-aut`, on the image), and 1758 (*Aut si*), which follows 1573's text; 1715, 1747, 1750 and Wikisource *At*
  (εἰ δὲ ὡς Χριστιανός, *but if as a Christian*). 1556's OCR loses the words at its page turn. *aut* (*or if*) does not
  fit the apodosis *ne pudeat eum* after the list of 4:15; kept as a probable 1573 misprint of *at*. For your eye.
- **3:10–12**: 1573's numbering (intro); the KJV's kept.
- **4:9** *Este alii in alios hospitales sine murmuribus*: 1573's OCR *&* is the note letter *d* (canvas 921, crop
  `1Pet.4.9-et`, on the image: *hoſpitales, ᵈ ſine murmuribus*), as 1556 (OCR *d fine*). Nothing added.
- **1:2** *pacem plurimam dicit*, **3:12** *in maleficos*, **4:5** *judicaturus*, **4:11** *saecula: Amen*, **5:7**
  *curae sitis*: lines the OCR lost, printed (crops `1Pet.1.2-plurimam`, `1Pet.3.12-maleficos`,
  `1Pet.4.5-iudicaturus`, `1Pet.4.11-secula`, `1Pet.5.7-curae`). Kept.
- **3:6** *dum bene facitis*: 1573 *benefacitis* (canvas 921, crop `1Pet.3.6-benefacitis`), 1758; kept apart, as the
  rejected rule *bene facitis → benefacitis* and your settled *bene facitis*.
- **2:9** *vocauit*: Wikisource's *u*; stage 3's *jv* rule makes it *vocāvit*. Left to stage 3.
- **1:11** *quodnam* (1573 *quod'nam*), **1:21** *per eum* (OCR *percum*), **5:12** *esse* (OCR *es se*): spacing or
  OCR; kept.
- **2:19** *Hoc enim gratiam emeretur*: 1573 *emeretur* (canvas 920, crop `1Pet.2.19-sit`), with every printing. Kept.
- **5:6** *ut vos tempore curationis evehat*: 1573 prints it in parentheses, *( vt vos ᵃ tempore curationis euehat )*
  (canvas 922, crop `1Pet.5.7-curae`; *a* a note letter), as 1556. Punctuation, left to stage 3.
- **Note letters and margin notes**, not text: 1:6 *a*, 1:9 *b* (*id quo spectat & tendit fides*), 2:19 *b*, 4:1 *a*,
  4:6 *b* (*cum non intelligo, ideo que ad verbum transtuli*), 4:8 *c*, 4:9 *d*, 4:10 (*vide finem epistolae Iacobi*),
  4:12 *g* (*quod re-* …), 4:13 (*… gratis & festamini*), 4:17 *h* (*familia gente*), 5:6 *a*, 2:14 (*geret*), 2:20
  (*torem ele*); the references (from the page text, the OCR's slips set right: 1:15 *Luce1.75*, 1:17 *Leuit.15.4*, *Roman.2.11*, 1:24
  *Esa.40.6*, *Eccl.14.18*, 2:6 *Psal.117.12*, *Matt.21.42*, 2:17 *Rom.12.10*, 2:18 *Col.3.22*, 2:22 *1.Iohan.3.5*,
  3:5 *Gen.18.10*, 3:15 *Mat.13.16*, *Esa.8.11*, 3:18 *Hebr.9.18*, *Rom.5.8*, 3:20 *Gen.7.2*, *Mat.24.38*,
  *Luc.17.26*, 4:7 *Prou.10.12*, *Rom.12.13*, 4:8 *Hebr.13.2*); the chapter summaries; the running head (4:14); and
  1573's annotation after chapter 3 (on 3:7, *ποικίλης χάριτος καὶ ζωῆς*).
- **Punctuation and capitals, left to stage 3**: 1:16 *sancti estote* (1573 *Sancti*), 2:24 *vivamus cujus* (1573 a
  colon), 3:6 *Dominum eum appellans* (1573 *dominum*), 3:15 *colite, ac* (1573 a stop), 3:16 *in christianitate*
  (1573 *Christianitate*), 4:15 *appetens:* (1573 a stop), 4:17 *evangelio* (1573 *Euangelio*), 5:5 *obsequendo,*
  (1573 no comma), 5:6 the parentheses.
- **Spellings, left to stage 3** (decisions 37 and 42's rules, and section 6): *quum*, *Quum* (1573 *cùm*),
  *carissimi*, *caritatem*, *caritas*, *caritatis* (1573 *charissimi*, *charitatem*), *tamquam*, *Quamquam*,
  *quicumque*, *numquam* (1573 *tanquam*, *quanquam*, *quicunque*, *nunquam*), *paullulum*, *paullum* (1573 *paululum*,
  *paulum*), *exsultatis*, *exsultetis* (1573 *exultatis*), *exsistet* (1573 *existet*), *exstitit*, *exstrueretur*
  (1573 *extitit*, *extrueretur*), *exspectaret* (1573 *expectaret*), *eamdem* (1573 *eandem*; your settled *eamdem* 6 :
  *eandem* 1), *adferendum*, *adquisitus*, *adfecti*, *adfabiles*, *adficiatur* (1573 *afferendum*, *acquisitus*,
  *affecti*, *affabiles*, *afficiatur*; section 6), *tentationibus* (section 6), *obediant*, *obedientes*, *obedivit*,
  *obediendo*, *feminae* (1573 *fœminæ*), *caelis*, *caelo*, *caelum* (1573 *cœl-*), *hereditatem*, *coheredes* (1573
  *hæred-*), *litteris* (1573 *literis*), *nuntiata*, *nuntiatum*, *nuntiatus* (1573 *nunciat-*), *pretiosior*,
  *pretioso*, *pretii* (1573 *precio-*, *precij*), *comessationibus* (1573 *commessationibus*; your settled
  *cōmessātiōnibus*), *submittite* (1573 *summittite*; your settled text has both, as James 4:10), *sylvanum* (section 1),
  *Noae*, *Sione*, *Jesu*, *ejus*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282441–43), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 1 Pet 1:2 | *Secundum Dei patris providentiam electis* | = | OCR *…trís preícitum fecun-dum electis* (perhaps *Dei patris praescitum secundum electis*; doubtful) | Wikisource, 1747, 1750 *Dei patris praescito electis*; 1758, 1681, 1726 with 1573 |
| 1 Pet 1:20 | *Provisi ante orbem conditum* | = | *praecogniti ante orbem conditum* | Wikisource, 1747, 1750 with 1556; 1758, 1726 with 1573 |
| 1 Pet 2:2 | *rationale et alienum a fraude lac* | = | *rationale & infraudulentum lac* | Wikisource and the other printings with 1573 |
| 1 Pet 2:8 | *ei inobedientes* | = | *ei diffidentes* | 1750 with 1556 (Wikisource, 1715, 1747 *et diffidentes*); 1758, 1726 with 1573 |
| 1 Pet 3:6 | *cujus factae estis filiae, dum bene facitis, et nullo pavore terremini* | = | *ex qua vos procreatae, recte facite, & nullo pavore terremini* (OCR *exquauosprocreatz, … rectéfacite*) | Wikisource and the other printings with 1573 |
| 1 Pet 3:20 | *Qui olim non paruerant, quum semel exspectaret* | = | *quibus olim persuasum non fuerat, cum expectaret* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 Pet 3:21 | *bonae conscientiae stipulatio* | = | *bonae conscientiae testificatio* | Wikisource, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 Pet 4:3 | *Satis est enim nobis* | = | OCR *Satís eft ením uobis* (doubtful) | 1747 *vobis*; Wikisource, 1758, 1750 with 1573 |
| 1 Pet 4:11 | *si quis subministrat* | = | OCR *fi quíst fubmíniftret* (*subministret*; doubtful) | every other printing with 1573 |
| 1 Pet 5:5 | *obsequendo modestia ornamini* | = | *obsequendo modestiam complectemini* (OCR) | Wikisource, 1715, 1747, 1750 *modestiam complectimini*; 1758, 1681 with 1573 |
| 1 Pet 5:9 | *Cui resistite fide firmi* | = | *Cui resistite fiducia firmi* | Wikisource and the other printings with 1573 |
| 1 Pet 5:10 | *qui nos ad aeternam suam gloriam* | = | OCR *quí uos ad zeternam* (*vos*; doubtful) | every other printing with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12; 1:2, 4:3,
4:11 and 5:10 recorded as doubtful, the OCR alone)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) and writes *tempto*, word by word;
these 1 Peter forms have no row in `data/rules/orthography.tsv` yet (checked with `normalize.propose()` on the
draft). Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| tentationibus | temptationibus | word | 1:6 | decision 37 (*tempto*); as the approved *tentationem → temptationem*, *tentatione → temptatione*; your settled *temptātiō-* 13× |
| adferendum | afferendum | word | 1:13 | 1573 *afferendum* (canvas 920); 1556 (OCR *afíerendum*), 1758, 1747, 1726; your settled *afferre*, *afferte*; as the approved *adferto → afferto* |
| adquisitus | acquisitus | word | 2:9 | 1573 *acquiſitus* (canvas 920, crop `1Pet.2.9-lectum`); 1556 (OCR *acquífitus*), 1758, 1681, 1715, 1747, 1726; as the approved *adquiescis → acquiescis* |
| adfabiles | affabiles | word | 3:8 | 1573 *affabiles* (canvas 921); 1556 (OCR *affabiles*), 1758; Gaffiot *affābilis* |
| adficiatur | afficiatur | word | 4:15 | 1573 *afficia-tur* (canvas 922); 1556, 1758, 1681, 1715; as the approved *adficiantur → afficiantur*; your settled *afficī-* |

(*adhibitus*, *adventu*, *adversatur*, *adversa*, *adversarius*, *advenerit* do not assimilate; *adfecti* has its
approved rule.)

**Decision:** accept (Claude, 2026-11-12, under decisions 37, 42 and 46; added to `data/rules/orthography.tsv`)