# Ephesians 1–6, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of 2 Corinthians (`data/review/2cor1-13-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 894–897). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's Ephesians as
  **`text/draft/EPH.usfm`** (BSB paragraphs). You have no earlier work on Ephesians; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Ephesians is the early wording**, as its Romans and Corinthians, with slips of its own:
  *fortunavit* for *felicitavit* (1:3), *exsurge* for *et surge* (5:14), *unum corpus* for *una caro* (5:31),
  *corpus* for *carnem* (6:5), *favor* for *gratia* (6:24), and a clause lost at 2:2 (*ut est hujus mundi vita*).
  1556 already has these revisions where its OCR can be read; 1573's own changes against 1556 are 2:21 *sanctum*
  (1556 *sacrum*), 4:18 *duritiem* (1556 *torporem*, as `data/calibration/scans.md` noted) and 4:21 *Si modo*
  (1556 *Siquidem*), in section 5.
- **Versification** (decision 5): the draft is at the KJV counts (155 verses), no edits file. 1573 prints every verse
  number and agrees with the draft's numbering everywhere but **5:18–19**: 1573 prints 19 before *colloquentes*,
  so *sed spiritu pleni este* closes 18, as the KJV's 5:18 (*but be filled with the Spirit*); the draft starts 19
  with it. Moved back to 18 (section 2c). At **1:22–23** 1573 has *dedit caput* after the parenthesis, inside its
  23 (*quae ejus corpus est) dedit caput complementum*); with 1573's word order (section 2) the KJV's boundary falls
  at the parenthesis, as 1573's own.
- **Collation** (`python -m pipeline collate Eph 1-6`; `data/calibration/Eph1-6-collation.tsv`, 208 places: 35
  *correct*, 8 *others-1573-agrees*, 5 *others*, 145 *base-only* (97 reading, 29 division, 9 f/s, 6 edge, 4
  spelling), 14 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/Eph.*`, 68): every reading where 1573 and another printing agree against Wikisource, and
  every base-only reading whose 1573 words are Latin (1:3 *felicitauit*, 1:21 *in cælestibus*, 1:22–23 *dedit
  caput*, 2:21 *sanctum*, 4:18 *duriciem*, 4:21 *si modo*, 6:5 *carnem* …); the edge places (2:12 *mundo*, 1:7
  *diuite beneficentia*, 1:12 *sto collocauimus* (the next column's first line), 4:16 *in charitate*, 4:26 *iratis
  vobis*: 1573 line ends its OCR lost). The rest of the base-only readings are 1573's OCR (*oinnia*, *códiti*,
  *Deias*), note letters, margin notes and running heads run into the text (*Pet*, *Coloss*, *AD EPHESIOS*). Each
  place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758,
  1681, 1715, 1747, 1750). **2:2's lost clause was not listed by the collation** (1573 and five other printings
  have it; found by reading the verse against 1573's page text, then the image): an insertion it did not report.
- **The 14 uncovered verses** (3:9, 3:10, 4:6–10, 4:14, 5:14–17, 5:31, 6:16: 1573's OCR reads canvas 895's and 896's
  columns out of order, and 3:21 runs into 3:10) were each read in full on the page image: 3:9, 3:10, 4:6–10,
  4:14, 5:15–17 and 6:16 agree with the draft; 5:14 and 5:31 have Castellio's revised wording (section 2b).
- **The f/s sweep**, both ways: every *f* word in the draft whose *s*-form is also Latin (*fortem/sortem*, *fore/sore*,
  *fuit/suit*, *fertum/sertum*, *fero/sero*, *conferat/conserat*, *confectis/consectis* …, 25 words) and every *s*
  word whose *f*-form is Latin (*sit/fit* 8×, *sumus/fumus* 4×, *sitis*, *simus*, *sive*, *servi*, *sui*, *suam* …,
  15 words) was read in its verse. Two are slips (section 2a): **1:11 *in fortem* for *in sortem*** (1573 *ſortem*;
  the collation could not see it, 1573's OCR reading *fortem* as Wikisource), and **4:16 *modo sit* for *modo
  fit***. Read on the image: 1:18 *ſit*, 1:20 *ſui*, 2:10 *ſumus*, 3:18 *ſitis*, 5:30 *ſumus*, 5:33 *ſuam*, 6:5
  *ſerui*, 6:8 *ſiue … ſiue*, all long s; 5:2 *fertum*, 6:8 *fore*, 3:9 *fuit*, f.
- **In all, 45 corrections**: 15 Wikisource slips (section 1), 19 readings of Castellio's revised text (section 2),
  2 f/s slips found by the sweep (section 2a), 2 revised readings in verses 1573's OCR had not aligned (section 2b),
  1 verse boundary moved (section 2c, two Apply lines), 6 word divisions (section 3). **Not yet applied to the
  draft.** Spellings (*caritas*, *adsciti*, *exseruit*, *tamquam*, *quum*, *clipeo*) are left to stage 3 (decision
  37's rules); new word rules proposed (section 6, not added). Three places where 1573 reads against 1556 are taken
  from 1573 and recorded (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (15)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Ephesians 1:2** *et Dominus Jesu Christo* → *et Domino Jesu Christo*. 1573 *& Domino Ieſu Chriſto* (canvas 894); 1556, 1758, 1750.
   **Apply:** `Eph.1.2` la: `et Dominus Jesu` → `et Domino Jesu`
2. **Ephesians 1:4** *carite praediti* → *caritate praediti*. 1573 *charitate præditi* (canvas 894); 1556, 1758, 1747, 1750 (*caritate*).
   **Apply:** `Eph.1.4` la: `carite praediti` → `caritate praediti`
3. **Ephesians 1:10** *summatim comprehenda* → *summatim comprehendenda*. 1573 *comprehenden-da* (canvas 894, across the line); 1556, 1758, 1681, 1715, 1750, 1726.
   **Apply:** `Eph.1.10` la: `summatim comprehenda` → `summatim comprehendenda`
4. **Ephesians 1:20** *sui egrefii roboris* → *sui egregii roboris*. 1573 *pro ſui egregij roboris* (canvas 894); 1556, 1758, 1715, 1747, 1750.
   **Apply:** `Eph.1.20` la: `sui egrefii roboris` → `sui egregii roboris`
5. **Ephesians 2:2** *versati estis, ad principis* → *versati estis, ut est hujus mundi vita, ad principis*. 1573 *in quibus aliquãdo verſati eſtis, vt eſt huius mũdi vita, ad prĩcipis* (canvas 894; κατὰ τὸν αἰῶνα τοῦ κόσμου τούτου); 1556, 1758, 1681, 1750. No printing is without it; the collation did not list it.
   **Apply:** `Eph.2.2` la: `versati estis, ad principis` → `versati estis, ut est hujus mundi vita, ad principis`
6. **Ephesians 2:3** *versati fuimus aliquando* → *versati sumus aliquando*. 1573 *verſati ſumus aliquando* (canvas 894); 1556, 1758, 1681, 1750 (*fuimusque* follows, as all have it).
   **Apply:** `Eph.2.3` la: `versati fuimus aliquando` → `versati sumus aliquando`
7. **Ephesians 2:6** *Simulque suscitaverit. et in Christo* → *Simulque suscitaverit, et in Christo*. 1573 *ſimulq; ſuſcitauerit, & ᵃ in Chriſto* (canvas 894, a comma; the sentence runs on from 2:5); 1556, 1681, 1747, 1750.
   **Apply:** `Eph.2.6` la: `suscitaverit. et` → `suscitaverit, et`
8. **Ephesians 2:12** *ab israëlita republica* → *ab Israelitica republica*. 1573 *ab Iſraelitica republica* (canvas 894); 1556, 1758, 1681, 1715, 1747, 1750.
   **Apply:** `Eph.2.12` la: `ab israëlita republica` → `ab Israelitica republica`
9. **Ephesians 3:7** *ego factum sum minister* → *ego factus sum minister*. 1573 *cuius ego factus ſum miniſter* (canvas 895); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `Eph.3.7` la: `ego factum sum` → `ego factus sum`
10. **Ephesians 3:7** *dono divini beneficium mihi* → *dono divini beneficii, quod beneficium mihi*. 1573 *dono diuini bene-ficij, quod beneficium mihi diuinæ potentiæ vi collatum eſt* (canvas 895); 1556, 1758, 1681, 1747, 1750. Wikisource's eye skipped from one *benefici-* to the next.
   **Apply:** `Eph.3.7` la: `divini beneficium mihi` → `divini beneficii, quod beneficium mihi`
11. **Ephesians 3:20** *longeque copiosus facere* → *longeque copiosius facere*. 1573 *longè longeq; copioſius facere* (canvas 895); 1556, 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Eph.3.20` la: `copiosus facere` → `copiosius facere`
12. **Ephesians 4:16** *per quas effictur administratio* → *per quas efficitur administratio*. 1573 *per quas effici-tur adminiſtratio* (canvas 895); 1556, 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Eph.4.16` la: `quas effictur` → `quas efficitur`
13. **Ephesians 4:32** *vobis in Christum condonavit* → *vobis in Christo condonavit*. 1573 *Deus vobis in Chri-ſto condonauit* (canvas 896); 1758, 1681, 1715, 1747, 1750.
   **Apply:** `Eph.4.32` la: `in Christum condonavit` → `in Christo condonavit`
14. **Ephesians 5:23** *caput uxoris, ut Christus* → *caput uxoris est, ut Christus*. 1573 *Nam vir caput vxoris eſt, vt Chriſtus* (canvas 896); 1556, 1758, 1681, 1715, 1747, 1750.
   **Apply:** `Eph.5.23` la: `caput uxoris, ut` → `caput uxoris est, ut`
15. **Ephesians 5:27** *nulla macula et ruga* → *nulla macula aut ruga*. 1573 *nulla macula aut ruga, aut vlla tali re* (canvas 896); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Eph.5.27` la: `macula et ruga` → `macula aut ruga`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (19)

Where Wikisource reads with one or more of the early-line printings (1715, 1747, 1750), or 1573 differs in order or
form. 1556 has the revised reading too wherever its OCR can be read, except 2:21, 4:18 and 4:21 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Ephesians 1:1** *per Jesum Christum* → *per Christum Jesum*. 1573 *& fidentibus per Chriſtum Ieſum* (canvas 894); 1556 (OCR *per Chriftum lIefum*), 1758 (word order). Wikisource with 1750.
   **Apply:** `Eph.1.1` la: `per Jesum Christum` → `per Christum Jesum`
2. **Ephesians 1:3** *qui nos fortunavit* → *qui nos felicitavit*. 1573 *qui nos felicitauit omni vbertate* (canvas 894); 1556, 1758. The early line *fortunavit* (Wikisource, 1750).
   **Apply:** `Eph.1.3` la: `nos fortunavit` → `nos felicitavit`
3. **Ephesians 1:4** *sancti et inculpati* → *sancti ac inculpati*. 1573 *ſancti ac incul-pati* (canvas 894); 1556, 1758. Wikisource with 1681, 1747.
   **Apply:** `Eph.1.4` la: `sancti et inculpati` → `sancti ac inculpati`
4. **Ephesians 1:21** *dexter adsedit, caelestibus in locis, supra* → *dexter adsedit, in caelestibus, supra*. 1573 *illi dexter aſſedit, in cæleſti-bus, ſupra omnẽ principatũ* (canvas 894); 1556, 1758, 1681. The early line *caelestibus in locis* (Wikisource, 1747, 1750).
   **Apply:** `Eph.1.21` la: `adsedit, caelestibus in locis, supra` → `adsedit, in caelestibus, supra`
5. **Ephesians 1:22** *eumque dedit caput supra omnia ecclesiae* → *eumque supra omnia ecclesiae*. 1573 *eumque ſu-pra omnia Eccleſiæ, (quæ eius corpus eſt) dedit caput ᶜ complementum* (canvas 894; margin *c Christus est, per quem Deus complet ac perficit …*); 1556 (*eumq; supra omnia Ecclesiae (quae eius corpus est) dedit caput complementum*), 1758, 1681. Wikisource's order with 1715, 1750. With item 6.
   **Apply:** `Eph.1.22` la: `eumque dedit caput supra` → `eumque supra`
6. **Ephesians 1:23** *(Quae ejus corpus est) complementum* → *(Quae ejus corpus est) dedit caput complementum*. As item 5 (canvas 894).
   **Apply:** `Eph.1.23` la: `est) complementum` → `est) dedit caput complementum`
7. **Ephesians 2:21** *crescit in sacrum templum* → *crescit in sanctum templum*. 1573 *creſcit in ſanctum templum, in Domino* (canvas 895), ναὸν ἅγιον; 1758, 1681, 1726. **1556** *sacrum*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5), as 1 Cor 3:17 *sacrum → sanctum*.
   **Apply:** `Eph.2.21` la: `in sacrum templum` → `in sanctum templum`
8. **Ephesians 4:6** *qui est super omnia* → *qui est supra omnia*. 1573 *qui eſt ſupra omnia* (canvas 895); 1556, 1758. The early line *super* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Eph.4.6` la: `est super omnia` → `est supra omnia`
9. **Ephesians 4:13** *cognitionisque Dei filii* → *cognitionisque filii Dei*. 1573 *co-gnitionisq; filij Dei in virum adultum* (canvas 895); 1556, 1758, 1681, 1726 (word order). Wikisource with 1715, 1747, 1750.
   **Apply:** `Eph.4.13` la: `cognitionisque Dei filii` → `cognitionisque filii Dei`
10. **Ephesians 4:16** *ad semel exstruendum* → *ad semet exstruendum*. 1573 *ad ſemet extruẽdum in charitate* (canvas 895), εἰς οἰκοδομὴν ἑαυτοῦ; 1556, 1758, 1681, 1726. Wikisource *semel* with 1715, 1747, 1750.
   **Apply:** `Eph.4.16` la: `ad semel exstruendum` → `ad semet exstruendum`
11. **Ephesians 4:18** *animi torporem* → *animi duritiem*. 1573 *propter eorum a-nimi duriciem* (canvas 896), τὴν πώρωσιν; 1758 (*duritiem*), 1681, 1726 (*duriciem*). **1556** *torporem*, with Wikisource, 1747, 1750: a 1573 change (section 5). Written *duritiem*, Gaffiot's *dūritiēs* (1573's *-ci-* is its spelling, as its *nunciatum*, 2:17).
   **Apply:** `Eph.4.18` la: `animi torporem` → `animi duritiem`
12. **Ephesians 4:21** *Siquidem eum audivistis* → *Si modo eum audivistis*. 1573 *ſi modò eum audiuiſtis* (canvas 896), εἴ γε, as its own 3:2 *Si modo audivistis*; 1758, 1681, 1726. **1556** *siquidem*, with Wikisource, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Eph.4.21` la: `Siquidem eum` → `Si modo eum`
13. **Ephesians 5:2** *pro nobis dedit, fertum* → *pro nobis dedidit, fertum*. 1573 *& ſeipſum pro nobis dedidit, fertum hoſtiamq; Deo* (canvas 896), παρέδωκεν; 1556, 1758, 1750. Wikisource *dedit* with 1715, 1747.
   **Apply:** `Eph.5.2` la: `nobis dedit, fertum` → `nobis dedidit, fertum`
14. **Ephesians 5:4** *aut facetiae, quae dedecent* → *aut facetia, quae dedecent*. 1573 *aut ſtulta oratio, aut facetia, quæ dedecent* (canvas 896), εὐτραπελία, singular as *turpitudo* and *oratio*; 1556, 1758, 1747. Wikisource *facetiae* with 1750.
   **Apply:** `Eph.5.4` la: `aut facetiae, quae` → `aut facetia, quae`
15. **Ephesians 5:19** *canentes et cantantes* → *canentes ac cantantes*. 1573 *Dominum ex animo canentes, ac cantantes* (canvas 896); 1556, 1758. Wikisource with 1715, 1747, 1750.
   **Apply:** `Eph.5.19` la: `canentes et cantantes` → `canentes ac cantantes`
16. **Ephesians 5:25** *seque pro ea dedit* → *seque pro ea dedidit*. 1573 *ſeq; pro ea dedidit* (canvas 896), as 5:2; 1681, 1750 (1556's OCR *dedi-cit*, probably the same). Wikisource *dedit* with 1715.
   **Apply:** `Eph.5.25` la: `pro ea dedit,` → `pro ea dedidit,`
17. **Ephesians 5:30** *ex ejus carne et ossibus* → *ex ejus carne atque ossibus*. 1573 *ex e-ius carne atq; oſsibus* (canvas 896); 1556, 1758, 1681, 1726. Wikisource with 1747, 1750.
   **Apply:** `Eph.5.30` la: `carne et ossibus` → `carne atque ossibus`
18. **Ephesians 6:5** *quod ad corpus attinet* → *quod ad carnem attinet*. 1573 *quod ad carnem atti-net, dominis* (canvas 897), κατὰ σάρκα; 1556, 1758, 1681. The early line *corpus* (Wikisource, 1715, 1747, 1750), as Col 3:22 (`scans.md`).
   **Apply:** `Eph.6.5` la: `ad corpus attinet` → `ad carnem attinet`
19. **Ephesians 6:24** *Adsit Dei favor immortalis* → *Adsit Dei gratia immortalis*. 1573 *Adſit Dei gratia immortalis omnibus* (canvas 897), ἡ χάρις; 1556, 1758, 1726. The early line *favor* (Wikisource, 1715, 1747, 1750), as 2 Cor 13:14.
   **Apply:** `Eph.6.24` la: `Dei favor immortalis` → `Dei gratia immortalis`

## 2a. Found by the f/s sweep (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **Ephesians 1:11** *nos in fortem adsciti* → *nos in sortem adsciti*. 1573 *in quo nos in ſortem aſciti ſu-mus* (canvas 894, long s, read on the image; its OCR *fortem*); 1758 (*sortem*); the other OCRs read ſ as f. ἐκληρώθημεν, chosen by lot; *in fortem* is no sense here.
   **Apply:** `Eph.1.11` la: `in fortem adsciti` → `in sortem adsciti`
2. **Ephesians 4:16** *actione (quae pro cujusque partis modo sit)* → *… modo fit)*. 1573 *actione (quæ pro cuiuſque partis modo fit) facit* (canvas 895; the f has its crossbar, as *facit* after it, unlike the ſ of *ſemet* on the same line); 1556's OCR *fit* (which reads ſ as f too: not evidence). κατ᾽ ἐνέργειαν ἐν μέτρῳ: the working that takes place in each part's measure. For your eye: the only place where the image alone decides.
   **Apply:** `Eph.4.16` la: `partis modo sit)` → `partis modo fit)`

## 2b. Found where 1573 was not aligned (2)

`collate` listed 14 verses where 1573's OCR shows under 60% of the words (above). Read in full on the image; two have
Castellio's revised wording, which the collation could not report.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **Ephesians 5:14** *qui dormis (inquit) exsurge ex mortuis* → *qui dormis (inquit) et surge ex mortuis*. 1573 *Expergiſcere qui dormis (inquit) & / ſurge ex mortuis, & tibi Chriſtus affulgebit* (canvas 896); 1556 (OCR *& furge ex mortuis*), 1758 (*et … ex mortuis*), 1681 (*furge*). The early line *exsurge* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Eph.5.14` la: `(inquit) exsurge ex mortuis` → `(inquit) et surge ex mortuis`
2. **Ephesians 5:31** *fietque ex duobus unum corpus* → *fietque ex duobus una caro*. 1573 *adhæ-rebit vxori ſuæ, fietq; ex duobus vna caro* (canvas 896), σάρκα μίαν; 1556, 1758, 1681, 1726. The early line *unum corpus* (Wikisource, 1747, 1750), as 6:5 *corpus → carnem*.
   **Apply:** `Eph.5.31` la: `ex duobus unum corpus` → `ex duobus una caro`

## 2c. Verse boundary (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **Ephesians 5:18–19**: *sed spiritu pleni este* closes 18. 1573 *18 neue inebriamini vino, in quo ineſt luxuria: ſed / ſpiritu pleni eſte, / 19 colloquentes inter vos* (canvas 896); 1715 also prints 19 before *Colloquentes*, and the KJV's 5:18 has *but be filled with the Spirit*. Wikisource starts 19 with it (the other OCRs, aligned to the draft, cannot show where their 19 stands).
   **Apply:** `Eph.5.18` la: `inest luxuria:` → `inest luxuria: sed spiritu pleni este,`
   **Apply:** `Eph.5.19` la: `Sed spiritu pleni este, colloquentes` → `Colloquentes`

## 3. Word division (6)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **Ephesians 4:7** *proportione doni Christi* → *pro portione doni Christi*. 1573 *cium, pro portione doni Chriſti* (canvas 895, apart, read on the image); 1556 (*pro portíone*), 1681, 1726. Gaffiot's *prō portiōne* (under *portiō*); 1715, 1747, 1750 join it. For your eye.
   **Apply:** `Eph.4.7` la: `beneficium, proportione` → `beneficium, pro portione`
2. **Ephesians 6:12** *adversus mundi potentes tenebrarum* → *adversus mundipotentes tenebrarum*. 1573 *aduerſus mundipotentes tenebrarum* (canvas 897, one word, read on the image), κοσμοκράτορας; 1726. Castellio's compound, as 2 Cor 10:4 *divinipotentia* (his annotation at 1:3, canvas 894, names that coinage). 1556's OCR (*mundí potétes*), 1758, 1747, 1750 print two words. For your eye.
   **Apply:** `Eph.6.12` la: `adversus mundi potentes` → `adversus mundipotentes`
3. **Ephesians 4:19** *obducto callo seipsos addixerunt* → *… se ipsos addixerunt*. Your settled *sē ipsum* (18×, against *seipsum* 4×), as 2 Cor 8:5 *se ipsos*. 1573 joins it (*ſeipſos*).
   **Apply:** `Eph.4.19` la: `callo seipsos` → `callo se ipsos`
4. **Ephesians 5:2** *et seipsum pro nobis* → *et se ipsum pro nobis*. As item 3; 1573 *ſeipſum* (canvas 896).
   **Apply:** `Eph.5.2` la: `et seipsum pro` → `et se ipsum pro`
5. **Ephesians 5:28** *seipsum amat* → *se ipsum amat*. As item 3.
   **Apply:** `Eph.5.28` la: `amat, seipsum amat` → `amat, se ipsum amat`
6. **Ephesians 5:33** *sic amato, ut seipsum* → *… ut se ipsum*. As item 3; 1573 *ſeipſum* (canvas 896).
   **Apply:** `Eph.5.33` la: `ut seipsum.` → `ut se ipsum.`

## 4. Checked and kept

- **1:22–23** and **5:18–19**: verse boundaries (above).
- **1:21** *et potentiam, et dominatum*: 1573 *potentiã, & dominatũ* (canvas 894, nasal bars; its OCR *potentia*,
  *dominatu*). Agrees. *verum etiam*: 1573 *verumetiam*; kept apart, as 1758, 1681, 1715, 1747.
- **2:11** *manu facta*: 1573 *manufacta*; your settled *manū factum* (2×). Kept.
- **6:16** *in primis*: 1573 *inprimis*; kept, a division the spelling stage can settle with *adsumto*, *clipeo*.
- **6:24** the subscription *Ad Ephesios missa est Roma per Tychicum*: 1573 sets it in italics under the verse
  (canvas 897), *Tichicum*; kept *Tychicum*, as 6:21 (1573 *Tychicus*) and 1758, 1715, 1747, 1750. Set apart as
  `\cls` at stage 3 (decision 37).
- **The uncovered verses** 3:9, 3:10 (*Deũ*, *in cœleſtibus, per Eccleſiam, tam varia Dei ſapientia*), 4:6–10
  (*Aſcendit*, *Qui deſcẽderat*), 4:14 (*ne ſimus amplius*, OCR run together), 5:15–17 (*ᵇ ementes tempus*), 6:16:
  read on the image, agree with the draft. 3:21 (*in omnem omnium seculorum perpetuitatẽ*) likewise.
- **Line ends 1573's OCR lost**, read on the image: 1:7 *diuite beneficentia*, 1:12 *ſto collocauimus* (top of the
  next column), 2:12 *mundo*, 2:22 *diuino afflatu*, 4:10 *aſcendit, vt omnia compleret*, 4:16 *in charitate*, 4:26
  *iratis vobis*, 5:32 *Eccleſia dico*. All as the draft.
- **Note letters and margin notes**, not text: 1:5 *a* (*vt in ipsum*), 1:6, 1:7 (*Dei filium, fieremus Dei filij*),
  1:13 *b*, 1:14, 1:23 *c*, 2:6 *a* (*in eo quòd Christiani sumus*), 2:9 *b*, 3:12 *a*, 4:13, 4:15 *b* (*in Christum,
  hoc est, in Christi corpus*), 4:23 *c*, 4:24, 4:27 *d* (*ne per iram detis locum diabolo*), 5:3 *a*, 5:16 *b* (*ne
  temporis occasionem amittatis*), 6:6 *a* (*simulate*); scripture references (*Psalm.8.7*, *Coloss.3.5*,
  *1.Thess.5.8* …) and the three ANNOTATIO blocks (canvases 894–897).
- **Punctuation, left to stage 3**: 2:5 *Christo(estis*, 2:11 *alienigenas(qui*, 3:9 *Deum(qui*, 4:16
  *omnibus(per*, *actione(quae*, 4:22 *hominem(qui*, 5:5 *avarum(qui* (no space before the parenthesis); 5:15 *sed ut
  sapientes;* (1573 a comma); 1:13 *Sancto Spiritu*, 2:22 *Divino Adflatu* (1573 lower case).
- **Spellings, left to stage 3** (decision 37's rules, and new rules in section 6): *caritas*, *carissimus*, *cari*
  (1573 *charit-*, *chariss-*, *chari*), *auctore* (1573 *authore*), *adsciti*, *adsedit*, *adserendam*, *adsumto*,
  *adgrediantur*, *adgressiones*, *adscendens*, *adscendit*, *adfulgebit*, *Adflatu* (1573 *asc-*, *ass-*, *aggr-*,
  *aff-*), *exseruit* (1573 *exeruit*), *extructi*, *exstructionem*, *exstruendum* (1573 *extru-*), *exstinguere*
  (1573 *extinguere*), *peremtis* (1573 *peremptis*), *clipeo* (1573 *clypeo*), *hereditas*, *coheredes* (1573
  *hær-*, *cohær-*), *nuntiatum* (1573 *nunciatum*), *umquam*, *tamquam*, *quamquam* (1573 *vnquam*, *tanquam*,
  *Quanquam*), *quum* (1573 *cum*), *Quidquid* (1573 *Quicquid*), *ceteri*, *Ceterum* (1573 *cæteri*, *Cæterùm*),
  *obscenitatem* (1573 *obſcœnitatem*), *intelligentiam*, *intelligite*, *Huius*, *Cuius* (j, by the approved rule).

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Eph 2:21 | *in sanctum templum* | = | *in sacrum templum* | Wikisource, 1715, 1747, 1750 |
| Eph 4:18 | *animi duritiem* | = (*duriciem*) | *animi torporem* | Wikisource, 1747, 1750 |
| Eph 4:21 | *Si modo eum audivistis* | = | *Siquidem eum audivistis* | Wikisource, 1747, 1750 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Word rules for forms in the draft that no row of `data/rules/orthography.tsv` covers yet, each the next member of a
family already approved there and in your settled text. **Proposed, not added** to `orthography.tsv`.

| old | new | scope | the approved family | 1573 (canvas) |
|---|---|---|---|---|
| adsedit | assedit | word | *adseratur → asseratur*, *adservari → asservari* | *aſſedit* (894) |
| adserendam | asserendam | word | the same | *aſſeren-dam* (894) |
| adsumto | assumpto | word | *assumto → assumpto*, *adsumpto → assumpto*; settled *assumpto* 9× | *aſſumpto* (897) |
| peremtis | peremptis | word | *peremti → perempti*; settled *perempti*, *peremptus* | *peremptis* (895) |
| adgrediantur | aggrediantur | word | *adgressus → aggressus*; settled *aggred-*, *aggress-* 55× | *aggrediantur* (895) |
| adgressiones | aggressiones | word | the same | *aggreſ-ſiones* (897) |
| adscendens | ascendens | word | *adscendit → ascendit* …; settled *ascendens* 2× | *aſcendens* (895) |
| adfulgebit | affulgebit | word | *adflatu → afflatu*, *adflatus → afflatus* | *affulgebit* (896) |
| extructi | exstructi | word | your settled *exstru-* 12× (*extruxit* 1×); the draft's own 4:12, 4:16 | *extructi* (895) |
| intelligentiam | intellegentiam | word | *intelligens → intellegens* … (22 rows) | *intelligentiam* (895) |
| intelligite | intellegite | word | the same | *intelligite* (896) |

2:22 *Adflatu* is the capitalized *adflatu*, which the approved row covers if rules match without regard to case;
else it needs a row of its own (or the lower case of section 4 first).

**Decision:** (Nathan, or Claude under decision 30: add the rows as `approved` before stage 3)
