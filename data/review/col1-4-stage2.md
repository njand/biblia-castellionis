# Colossians 1–4, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of 2 Corinthians (`data/review/2cor1-13-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 901–904). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's Colossians as
  **`text/draft/COL.usfm`** (BSB paragraphs). You have no earlier work on Colossians; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Colossians is the early wording**, as its Romans and Corinthians, with slips of its own: *favorem*
  for *gratiam* (1:2), *favor* for *gratia* (4:18), *rerum natura* for *creatura* (1:23), *corpus* for *carnem* (3:22),
  *habendae Christo fidei* for *vestrae in Christum fidei* (2:5), *edocti*, *baptismo* (2:7, 2:12). 1556 already has
  every one of these revisions where its OCR can be read. Wikisource also leaves out words every printing has: 1:16
  *tum inadspectabilia*, 3:16 *habitet* and *Deique laudationibus*, 3:4 *cum*.
- **Versification** (decision 5): 1 edit in `data/versification/Col.draft.edits.tsv`, applied (95 verses, every
  chapter at the KJV count). 1573 (canvas 903) and Wikisource both end chapter 3 with *Domini, ex justo aequoque cum
  servis agite* as 3:26 and open chapter 4 at *Supplicationi incumbite*; it is now 4:1, and each verse of chapter 4
  moved up one (1573's 4:1–17 are the KJV's 4:2–18). No words are missing.
- **Collation** (`python -m pipeline collate Col 1-4`; `data/calibration/Col1-4-collation.tsv`, 145 places after the
  renumbering: 31 correct, 2 others-1573-agrees, 4 others, 104 base-only, 4 uncovered), with the edge and f/s checks.
  Read on the page image (crops in `sources/mdz-1573/crops/Col.*`, 53): every reading where 1573 and another printing
  agree against Wikisource, the 4 where others do, the base-only places whose 1573 words are Latin (1:8 *quidem*, 1:19
  *omnem* without *rerum*, 2:2 *tam*, 2:5 *ac*, 3:17 *Patris*, 3:22 *carnem*, 4:4 *vtid*), and the edge places (2:3
  *re-conditæ*, 2:17 *Christus*, 3:8 *ex ore vestro*, 3:20 *Domino gratum est*, 4:2 *actione vigilantes* are 1573 line
  ends its OCR lost; 1:12 *b*, 4:8 *a* are note letters). The rest of the base-only readings are 1573's OCR (*Aginus*,
  *oinnibus*, *Nunclator*), word breaks at line ends (*na turæ*, *docen tes*), margin notes and references run into the
  text (*a Christianam & spiritualem*, *1. Pet. 2.*). Each place was also read against 1556 (its e-rara OCR,
  `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **The uncovered verses** (1573's OCR under 60% of the words): 1:8 (*qui idem nobis vestram ᵃ in spiritu charitatem
  exposuit*, its OCR *quidem*), 1:12 (*Agimusq; patri gratias, qui nos idoneos reddidit ad participandam sanctorum
  sortem ᵇ in luce*, the line read into the other column), 3:14 (*Sed super hæc omnia ᵇ charitatem, quæ perfectionis
  vinculum est*, at the head of the right column) and 4:2 (*Supplicationi incumbite, in ea cum gratiarum actione
  vigilantes*, under the chapter's initial and summary) were read on the page image: they agree with the draft but for
  4:2's *imcumbite* (section 1).
- **The f/s sweep**, both ways: every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *fore/sore*,
  *perfecti/persecti*, *facit/sacit*, *fuerit/suerit*, *fidus/sidus*, *filii/silii* …, 17 words) was read in its
  verse: all are *f*. Every *s* word whose *f*-form is Latin (*si/fi*, *sit/fit*, *sitis*, *sui/fui*, *soli*, *solia*,
  *sortem*, *servi(s)*, *desinimus/definimus*, 10 words): all are *s*, and the nine places where 1573's OCR has the
  *f* (1:11 *sitis*, 1:16 *solia*, 1:18 *sit*, 2:8 *sit*, 2:20 *si*, 3:10 *sui*, 3:13 *si*, 4:1 *servis*, 4:11 *soli*)
  read *ſ* on the image (1:16 *ſolia*, thrones, θρόνοι). None found.
- **In all, 32 corrections**: 20 Wikisource slips (section 1), 11 readings of Castellio's revised text (section 2),
  1 word division (section 3). Spellings (*caritas*, *carissimus*, *carus*, *quicumque*, *tamquam*, *quum*, *adsidens*,
  *adfixum*) are left to stage 3 (decision 37's rules); five ad- words without a rule yet are proposed (section 6).
  Two places where 1573 reads against 1556 are recorded (section 5); one of them (2:5 *ac*) is kept as Wikisource and
  1556 have it, for your eye (section 4).

## 1. Wikisource slips: 1573 and the other printings agree against it (20)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Colossians 1:16** *tum adspectabilia, et solia* → *tum adspectabilia, tum inadspectabilia, et solia*. 1573 *tum aſpectabilia, tum inaſpectabilia. & ſolia* (canvas 901); 1556, 1681, 1750 (*tum inadſpectabilia*), 1758 (its OCR *tum aspectabilia* twice). Spelled as Wikisource's own 1:15 *inadspectabilis*; the ad- is stage 3's (section 6).
   **Apply:** `Col.1.16` la: `tum adspectabilia, et solia` → `tum adspectabilia, tum inadspectabilia, et solia`
2. **Colossians 2:2** *Tum et confirmentur* → *Tum ut confirmentur*. 1573 *tum vt confirmentur eorum animi* (canvas 902); 1556, 1758, 1681, 1715, 1750.
   **Apply:** `Col.2.2` la: `Tum et confirmentur` → `Tum ut confirmentur`
3. **Colossians 2:9** *tota divinitate plenitudo* → *tota divinitatis plenitudo*. 1573 *in quo tota diuinitatis plenitudo* (canvas 902); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Col.2.9` la: `tota divinitate plenitudo` → `tota divinitatis plenitudo`
4. **Colossians 2:12** *ex moruis* → *ex mortuis*. 1573 *qui eum ex mortuis ſuſcitauit* (canvas 902); 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Col.2.12` la: `ex moruis` → `ex mortuis`
5. **Colossians 2:19** *copulisque compactu regitur* → *copulisque compactum regitur*. 1573 *copulisq; compactum regitur* (canvas 902; with *corpus*); 1556, 1758, 1750.
   **Apply:** `Col.2.19` la: `copulisque compactu regitur` → `copulisque compactum regitur`
6. **Colossians 2:22** *is usus est, et usu pereant* → *is usus est, ut usu pereant*. 1573 *is vſus eſt, vt vſu pereant* (canvas 902; Castellio's annotation: *Quorum omnium … is usus est, ut usu pereant: sic enim verto*); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Col.2.22` la: `est, et usu pereant` → `est, ut usu pereant`
7. **Colossians 3:4** *vita vestra patefier* → *vita vestra patefiet*. 1573 *Cùm Chriſtus vita veſtra patefiet* (canvas 903); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Col.3.4` la: `vestra patefier` → `vestra patefiet`
8. **Colossians 3:4** *una eo patefietis* → *una cum eo patefietis*. 1573 *vnà cum eo patefietis glorioſi* (canvas 903); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Col.3.4` la: `una eo patefietis` → `una cum eo patefietis`
9. **Colossians 3:5** *quae deastorum* → *quae deastrorum*. 1573 *quæ deaſtrorum cultus eſt* (canvas 903); 1758, 1750.
   **Apply:** `Col.3.5` la: `quae deastorum` → `quae deastrorum`
10. **Colossians 3:10** *Induti novum* → *Indutique novum*. 1573 *indutiq; nouum* (canvas 903; joined to 3:9 *exuti*); 1556, 1758, 1747.
   **Apply:** `Col.3.10` la: `Induti novum` → `Indutique novum`
11. **Colossians 3:12** *benignitatem. modestiam* → *benignitatem, modestiam*. 1573 *benignitatem, modeſtiam* (canvas 903; a list); 1556, 1758, 1750.
   **Apply:** `Col.3.12` la: `benignitatem. modestiam` → `benignitatem, modestiam`
12. **Colossians 3:13** *de aliquo expstulet* → *de aliquo expostulet*. 1573 *expoſtulet* (canvas 903); 1556, 1758, 1681, 1715, 1747, 1750.
   **Apply:** `Col.3.13` la: `aliquo expstulet` → `aliquo expostulet`
13. **Colossians 3:16** *in vobis summa cum sapientia* → *in vobis habitet, summa cum sapientia*. 1573 *Chriſti ſermo largè in vobis habitet, ſumma cum ſapientia* (canvas 903); 1556, 1758, 1681, 1747, 1750 (ἐνοικείτω).
   **Apply:** `Col.3.16` la: `in vobis summa cum` → `in vobis habitet, summa cum`
14. **Colossians 3:16** *carminibus, et divinis cantionibus* → *carminibus, Deique laudationibus, et divinis cantionibus*. 1573 *carminibus Deiq; laudationibus & diuinis cantionibus* (canvas 903; ψαλμοῖς, ὕμνοις, ᾠδαῖς); 1556, 1758, 1681, 1747, 1750 (the last two with Wikisource's commas).
   **Apply:** `Col.3.16` la: `carminibus, et divinis` → `carminibus, Deique laudationibus, et divinis`
15. **Colossians 4:2** *Supplicationi imcumbite* → *Supplicationi incumbite*. 1573 *Supplicationi incumbite* (canvas 903, the chapter's first line beside the initial); 1758.
   **Apply:** `Col.4.2` la: `Supplicationi imcumbite` → `Supplicationi incumbite`
16. **Colossians 4:9** *est: hihi vos* → *est: ii vos*. 1573 *qui veſtras eſt. Ii vos de omnibus* (canvas 904); 1556, 1758, 1681 (*ii*); 1747, 1750 *hi*. Wikisource's *hihi* is a doubled *hi*; the text follows 1573. The stop before it is left to stage 3.
   **Apply:** `Col.4.9` la: `est: hihi vos` → `est: ii vos`
17. **Colossians 4:13** *testor masgno* → *testor magno*. 1573 *teſtor magno veſtri* (canvas 904); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Col.4.13` la: `testor masgno` → `testor magno`
18. **Colossians 4:13** *ac Hierpolitanorum* → *ac Hierapolitanorum*. 1573 *ac Hierapolitanorum ſtudio* (canvas 904; Ἱεραπόλει); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Col.4.13` la: `ac Hierpolitanorum` → `ac Hierapolitanorum`
19. **Colossians 4:15** *ejus domum ecclesiam* → *ejus domus ecclesiam*. 1573 *& eius domus eccleſiam* (canvas 904; τὴν κατ᾽ οἶκον αὐτῆς ἐκκλησίαν, the church of her house); 1556, 1758, 1747, 1750.
   **Apply:** `Col.4.15` la: `ejus domum ecclesiam` → `ejus domus ecclesiam`
20. **Colossians 4:18** *manu Pauli Mementote* → *manu Pauli. Mementote*. 1573 *Salutatio mea manu Pauli. Memẽtote* (canvas 904); 1556, 1758, 1681, 1715, 1747.
   **Apply:** `Col.4.18` la: `manu Pauli Mementote` → `manu Pauli. Mementote`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (11)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Colossians 1:2** *in Christo, favorem et pacem* → *in Christo, gratiam et pacem*. 1573 *in Chriſto gratiã & pacem* (canvas 901; its OCR *gratia*), χάρις; 1758, 1681, 1726. The early line *favorem* (Wikisource, 1747, 1750), as Romans' *favor → gratia*; 1556's OCR did not align here.
   **Apply:** `Col.1.2` la: `Christo, favorem et pacem` → `Christo, gratiam et pacem`
2. **Colossians 1:19** *omnem rerum universitatem* → *omnem universitatem*. 1573 *patri omnem vniuerſitatem inhabitare* (canvas 901; its OCR *omnein*), πᾶν τὸ πλήρωμα; 1556, 1758. The early line *omnem rerum* (Wikisource, 1747, 1750).
   **Apply:** `Col.1.19` la: `omnem rerum universitatem` → `omnem universitatem`
3. **Colossians 1:23** *in omni rerum natura subjecta caelo* → *in omni creatura subjecta caelo*. 1573 *quod in omni creatura ſubiecta cœlo* (canvas 901), ἐν πάσῃ κτίσει; 1758, 1681, 1726. The early line *rerum natura* (Wikisource, 1747, 1750; 1715 *natura*), as 2 Cor 5:17 *res → creatura*; 1556's OCR loses the words. 1:15 *totius rerum naturae primogenitus* stands in 1573 and is kept.
   **Apply:** `Col.1.23` la: `in omni rerum natura subjecta` → `in omni creatura subjecta`
4. **Colossians 2:2** *tam divite, quam plena* → *tam divite, tam plena*. 1573 *tum vt tam diuite, tam plena abundent peritia* (canvas 902); 1556, 1758, 1681, 1715. Wikisource *quam* with 1750.
   **Apply:** `Col.2.2` la: `tam divite, quam plena` → `tam divite, tam plena`
5. **Colossians 2:5** *et habendae Christo fidei firmitatem* → *et vestrae in Christum fidei firmitatem*. 1573 *& veſtræ in Chriſtum fidei firmitatem* (canvas 902), τὸ στερέωμα τῆς εἰς Χριστὸν πίστεως ὑμῶν; 1681, 1726. The early line *habendae Christo* (Wikisource, 1715, 1747, 1750); the OCRs of 1556 and 1758 lose the line.
   **Apply:** `Col.2.5` la: `et habendae Christo fidei` → `et vestrae in Christum fidei`
6. **Colossians 2:7** *ut edocti estis* → *ut docti estis*. 1573 *in fide(vt docti eſtis)* (canvas 902); 1556, 1758, 1726. The early line *edocti* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Col.2.7` la: `ut edocti estis` → `ut docti estis`
7. **Colossians 2:10** *in eo perfecti estis* → *in eo estis perfecti*. 1573 *& vos in eo eſtis perfecti* (canvas 902); 1556, 1758, 1681, 1726 (word order). Wikisource with 1715, 1750.
   **Apply:** `Col.2.10` la: `in eo perfecti estis` → `in eo estis perfecti`
8. **Colossians 2:12** *sepulti in baptismo* → *sepulti in baptismate*. 1573 *ſepulti in baptiſmate* (canvas 902); 1556, 1758, 1681, 1726. The early line *baptismo* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Col.2.12` la: `in baptismo:` → `in baptismate:`
9. **Colossians 3:22** *quod ad corpus attinet* → *quod ad carnem attinet*. 1573 *quod ad car-nem attinet* (canvas 903), κατὰ σάρκα; 1556, 1758. The early line *corpus* (Wikisource, 1747, 1750), as 2 Cor 7:5 *persona → caro*.
   **Apply:** `Col.3.22` la: `quod ad corpus attinet` → `quod ad carnem attinet`
10. **Colossians 4:4** *Ut ita patefaciam* → *Ut id ita patefaciam*. 1573 *vt id ita patefaciam* (canvas 903; its OCR *vtid*), αὐτό; 1556, 1758, 1681. Wikisource with 1750.
   **Apply:** `Col.4.4` la: `Ut ita patefaciam` → `Ut id ita patefaciam`
11. **Colossians 4:18** *Adsit vobis Dei favor* → *Adsit vobis Dei gratia*. 1573 *Adſit vobis Dei gratia: Amen* (canvas 904), ἡ χάρις; 1556, 1758, 1681. The early line *favor* (Wikisource, 1715, 1747).
   **Apply:** `Col.4.18` la: `Dei favor:` → `Dei gratia:`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse and on the image where 1573's OCR has the
*f* (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The four uncovered verses (1:8, 1:12, 3:14, 4:2) were read on the page image (intro): none differs from the draft
beyond 4:2's *imcumbite*, already section 1's item 15. No decision needed.

## 3. Word division (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **Colossians 2:7** *in fide(ut* → *in fide (ut*. A space before the parenthesis, as everywhere else in the draft; 1573 sets it tight (*fide(vt*, canvas 902), 1556 and the others with a space. The OCR tokens join the two words otherwise.
   **Apply:** `Col.2.7` la: `fide(ut` → `fide (ut`

## 4. Checked and kept

- **2:5** *Quamvis enim corpore absim, at animo quidem apud vos sum*: 1573 *ac animo* (canvas 902, read on the image:
  *ac*), with 1758, 1681 and 1726, which follow 1573; **1556** *at animo* (OCR *atanimo*), with 1715, 1747, 1750. *at*
  is the particle that answers *quamvis*; *ac* there makes no sense. Kept with 1556, as the sense (section 5). For your
  eye.
- **2:12** *per collocatam in Dei vi fiduciam*: 1573 *collocatam* (canvas 902) with Wikisource, 1681, 1750; **1556**
  *collatam* with 1758, 1715, 1726. Kept as 1573 (section 5).
- **1:5** *Propter ea, quae*: 1573 *propter ea, quæ* (canvas 901, apart on the image; its OCR *propterea*). Kept.
- **1:8** *Qui idem nobis*: 1573 *qui idem* (canvas 901; its OCR *quidem*). Kept.
- **3:17** *Deo patrique*: 1573 *Deo Patriq;* (canvas 903; its OCR *Patris*). Kept.
- **3:25** *Qui vero injuriam facit*: 1573 *iniuriã* (canvas 903; its OCR *iniuria*). Kept.
- **3:14** *Sed super haec omnia caritatem*: 1573's OCR runs a note letter in as *&*; the image has *omnia ᵇ charitatem*
  (margin *b scilicet induite*). Kept.
- **Note letters and margin notes**, not text: 1:8 *a* (*Christianam & spiritualem*), 1:12 *b*, 2:13 *a*, 3:5 *a*
  (*quod avari pecuniam colunt, ut Deum*), 3:14 *b*, 3:15 *c*, *d* (*beneficiorum memores*), 3:18 *e*, 3:21 *f* (*ne
  estote nimis in eos morosi*), 4:8 *a*; the glosses run into the text at 1:13 and 2:14–15. **4:8**'s margin is a
  variant reading of Castellio's own: *aliàs nostrarum rerum statum cognoscatis* (canvas 904; the Greek variant ἵνα
  γνῶτε τὰ περὶ ἡμῶν), not taken into the text.
- **4:18** the subscription (*Scripta est Romae, missa per Tychicum et Onesimum*): 1573 sets it in italics under the
  verse (canvas 904). Set apart as `\cls` at stage 3 (decision 37).
- **Punctuation and capitals, left to stage 3**: 3:5 *cultus est.* (1573 a comma, the sentence running on into 3:6
  *propter quae*), 4:9 the stop before *ii*, 4:16 *laodicensem* (1573 *Lao-dicenſem*, its OCR; the crop shows only
  the second line).
- **Spellings, left to stage 3** (decision 37's rules, and section 6): *caritas*, *carissimus*, *carus*, *caroque*
  (1573 *charitas*, *charissimus*, *charus*, *charoque*), *quicumque*, *tamquam* (1573 *quicunque*, *tanquam*), *quum*,
  *Quumque* (1573 *cum*, *Cumque*; decision 41), *quidquid* (1573 *quicquid*), *adsidens*, *adsiduis*, *adfixum*,
  *adfectum*, *adspectabilia*, *inadspectabilis* (1573 *ass-*, *aff-*, *asp-*), *saeculorum* (1573 *seculorum*),
  *nuntiamus* (1573 *nunciamus*), *hereditatem* (1573 *hæreditatem*), *Romae* (1573 *Romæ*).

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Col 2:5 | *at animo quidem* (1556) | *ac animo* | = | 1758, 1681, 1726 with 1573; 1715, 1747, 1750 with 1556 |
| Col 2:12 | *per collocatam* | = | *per collatam* | 1758, 1715, 1726 with 1556; 1681, 1750 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Colossians has five ad- words that decision 37's principle (ad- assimilated, compounds of *sum*, *adnuntio* and names
excepted) covers but `data/rules/orthography.tsv` has no row for yet. Proposed, not written to the file:

| old | new | scope | 1573 | note |
|---|---|---|---|---|
| adspectabilia | aspectabilia | word | *aſpectabilia* (1:16) | as the approved *adspectum → aspectum* |
| inadspectabilia | inaspectabilia | word | *inaſpectabilia* (1:16) | as the approved *inadspectabilis → inaspectabilis* |
| adfixum | affixum | word | *affixum* (2:14) | as the approved *adfixa → affixa* |
| adfectum | affectum | word | *affe-ctum* (3:12) | as the approved *adfectus → affectus* |
| adsiduis | assiduis | word | *aſ-ſiduis* (4:12) | as the approved *adsidui → assidui* |

Your settled text spells the word both ways: Rom 1:20 *inadspectābilia*, 2 Cor 4:4 *inaspectābilis*. The rule would
not touch Romans (settled), so the difference stands until you choose; for your eye. A stem row *inadspect →
inaspect* (proposed, `data/review/spelling-audit.md` A) now in `orthography.tsv` would cover the second row.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11); the five rows are for `data/rules/orthography.tsv`, not yet written there
