# 2 Peter 1–3, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of James and 1 Peter (`data/review/jas1-5-stage2.md`,
`data/review/1pet1-5-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 922–924: the title and Athanasius's
  argument on 922 after 1 Peter, 1:1–5 at its foot, 1:5–2:22 on 923, 3:1–18 on 924). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5); its e-rara OCR has 2 Peter on pages 10282443–44,
  in interleaved columns, and reaches nearly every verse (hardly 1:1–4 and 2:1–6). Stage 1 drafted Wikisource's 2
  Peter as **`text/draft/2PE.usfm`** (BSB paragraphs). You have no earlier work on 2 Peter; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's 2 Peter is the early wording**, as its 1 Peter: *Favorem* (1:2), *in vestris animis* (1:19), *Asina
  muta … locuta* (2:16), *nocte* (3:10), *Ut et in* (3:16), and the voice's words of 1:17–18 in 17, each with
  early-line printings (1715, 1747, 1750), and slips of its own (*expitationis*, *dEo*, *autme*, *quia*, *Balsami*,
  *condito*, *excitatis*). 1556 has the revised reading wherever its OCR can be read (1:2, 1:17–18, 2:16, 3:10), except
  1:19, where it reads *in vestris animis* with Wikisource: *in cordibus vestris* is 1573's (section 5).
- **Versification** (decision 5): the draft is at the KJV counts (61 verses), no edits file. 1573 prints every verse
  number and agrees with the draft's numbering throughout. At **1:17–18** 1573 (and 1556, 1758) prints the voice's
  words *Hic est meus charissimus filius, in quo me oblecto* after *in sacro monte*, at the end of 18; the Greek and the
  KJV have them in 17, and so has Wikisource. The text follows 1573 (section 2c).
- **Collation** (`python -m pipeline collate 2Pet 1-3`; `data/calibration/2Pet1-3-collation.tsv`, 123 places: 20
  *correct*, 4 *others-1573-agrees*, 5 *others*, 93 *base-only* (65 reading, 16 division, 5 edge, 4 spelling, 3 f/s), 1
  *uncovered*), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/2Pet.*`, 18):
  every reading where 1573 and another printing agree against Wikisource, the *others* places that touch the text
  (2:15 *Balaami*, 2:16 *locutum*), every base-only reading whose 1573 words are Latin (1:19 *cordibus*, 2:16
  *Iumentum mutum*, 3:10 *noctu*, 3:16 *vt in*), the edge places (1:11 *In*, the verse number; 1:18 *quo me oblecto*,
  section 2c; 1:21 *homines diuini*, printed; 2:10 *horrent*, 2:21 *retro recessisse*, 2:22 *cœni volutabrum*: all
  printed) and the lines the OCR lost (1:2 *stri cognitione*, 1:9 *catorum*, 1:12 *tate fixos*, 2:15 *minis conuictus
  est*, 2:20 *re deterior*: all printed as the draft). The rest of the base-only readings are 1573's OCR (*setas*,
  *vindicemás*, *tenebraruin*, *infirinas*, *vomituin*, *olin*, *vêturos*, *expetantes*), word breaks at line ends
  (*patien tiam*, *na turaliter*, *tem poribus*, *dissol uentur*), words run together (*perea*, *omnistudio*,
  *Hęcenim*, *perauaritiam*, *Atisti*, *lotafus*), note letters and margin notes run into the text (section 4) and the
  chapter summaries. Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org
  printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 922–924), not only the collation's places: it
  found the transposition of 1:17–18 whole (the collation saw only its edge) and nothing further.
- **The uncovered verse** 1:17 (1573's OCR 58% of the words) was read whole on the image: *quippe qui à Deo patre
  honorem acceperit & gloriam, voce delata ad eum huiuſmodi ᵍ à magnifi-ca gloria.* (crops `2Pet.1.17-magnifica`,
  `2Pet.1.17-18-oblecto`; margin *g à glorioso Deo*). It differs from the draft in Wikisource's *dEo* (section 1) and
  in the voice's words, which 1573 prints in 18 (section 2c).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide*, *fidem*, *fit/sit*,
  *ferant/serant*, *falsi/salsi*, *fontes/sontes*, *fuerunt*, *fur*) was read in its verse: all are *f* by sense and on
  the page; 2:20 *fit eorum posterior conditio*, the indicative of the apodosis, is *f* on the image
  (`2Pet.2.20-fit`). Every *s* word whose *f*-form is Latin (*si/fi*, *sit/fit*, *suique*, *sumus/fumus*): all are *s*
  by sense, and 1:3 *largita ſit*, where 1573's OCR has the *f*, is long s on the image (`2Pet.1.3-sit`). None found.
- **In all, 13 corrections**: 7 Wikisource slips (section 1), 5 readings of Castellio's revised text (section 2), 1
  transposition across a verse boundary (section 2c). Spellings (*quum*, *carissimi*, *numquam*, *quamquam*,
  *quamdiu*, *umquam*, *quemquam*, *tamquam*, *otiosos*, *otiatur*, *Verumtamen*, *adsiduam*, *adspectu*,
  *exspectantes*, *intelligatis*, *quotidianis*, *eis*, *herum*, …) are left to stage 3 (decisions 37 and 42's rules);
  two rules proposed (section 6). Three places where 1556 reads against 1573 are recorded (section 5), one of them from
  a doubtful OCR.

## 1. Wikisource slips: 1573 and the other printings agree against it (7)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **2 Peter 1:9** *oblivione captus expitationis veterum* → *expiationis*. 1573 *obliuione captus expiationis veterum ſuorum pec-/catorum.* (canvas 923, crop `2Pet.1.9-expiationis`), τοῦ καθαρισμοῦ; 1556 (OCR *exptationis*), 1758, 1747, 1750. Wikisource alone.
   **Apply:** `2Pet.1.9` la: `captus expitationis veterum` → `captus expiationis veterum`
2. **2 Peter 1:17** *a dEo patre* → *a Deo patre*. 1573 *quippe qui à Deo patre honorem acceperit* (canvas 923, crop `2Pet.1.17-magnifica`); every printing. A typing slip.
   **Apply:** `2Pet.1.17` la: `a dEo patre` → `a Deo patre`
3. **2 Peter 2:1** *Fuerunt autme et falsi vates* → *autem*. 1573 *FVerunt autem & falſi vates in populo* (canvas 923, crop `2Pet.2.1-autem`); 1556 (OCR *Veruntautem*); the archive.org printings' rows, as aligned, begin after the word. Wikisource alone.
   **Apply:** `2Pet.2.1` la: `Fuerunt autme et` → `Fuerunt autem et`
4. **2 Peter 2:7** *Et justum Lotum, quia libidinosis nefariorum moribus vexabatur* → *qui a libidinosis*. 1573 *& iuſtum Lotum, qui à libidinoſis nefariorum / moribus vexabatur* (canvas 923, crop `2Pet.2.7-qui`), *who was vexed by*, καταπονούμενον ὑπὸ; 1556 (OCR *qui alibidinofis*), 1758, 1681, 1715, 1726. 1750 *qui libidinosis*. Wikisource joined the two words into *quia*.
   **Apply:** `2Pet.2.7` la: `Lotum, quia libidinosis` → `Lotum, qui a libidinosis`
5. **2 Peter 2:15** *Balsami, Bosoris filii* → *Balaami*. 1573 *errant, Balaami Boſoris filij* (canvas 923, crop `2Pet.2.15-Balaami`; the OCR's *Balaani*), τοῦ Βαλαάμ; 1556 (*Balaami*), 1758, 1715, 1750, 1726; Wikisource's own Revelation 2:14 *Balaami*. Wikisource alone. (The name's form against the Old Testament's, decision 46, waits on Numbers, which Wikisource and your text do not yet have.)
   **Apply:** `2Pet.2.15` la: `errant, Balsami, Bosoris` → `errant, Balaami, Bosoris`
6. **2 Peter 2:20** *fit eorum posterior condito priore deterior* → *conditio*. 1573 *poſterior conditio prio-/re deterior.* (canvas 923, crop `2Pet.2.20-conditio`); 1556 (OCR *condi-tio*), 1758 (*conditio*), 1747, 1750. Wikisource alone.
   **Apply:** `2Pet.2.20` la: `posterior condito priore` → `posterior conditio priore`
7. **2 Peter 3:17** *ne … abducti, excitatis ex vestra firmitate* → *excidatis*. 1573 *abducti, excidatis ex ve-/ſtra firmitate:* (canvas 924, crop `2Pet.3.17-excidatis`), ἐκπέσητε; 1556 (OCR *excidatísex*), 1758, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `2Pet.3.17` la: `abducti, excitatis ex` → `abducti, excidatis ex`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (5)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read, except 1:19 and 3:16 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **2 Peter 1:2** *Favorem et pacem plurimam dicit* → *Gratiam*. 1573 *2 gratiam & pacem plurimam / dicit, in Dei & Ieſu Domini no-/ſtri cognitione,* (canvas 922, crops `2Pet.1.2-gratiam`, `2Pet.1.2-cognitione`), χάρις; 1556 (OCR *gratíam*), 1758, 1681. The early line *favorem* (Wikisource, 1715, 1747, 1750), as 1 Pet 1:2. The capital follows the draft's verse openings.
   **Apply:** `2Pet.1.2` la: `Favorem et pacem` → `Gratiam et pacem`
2. **2 Peter 1:19** *et lucifer oriatur in vestris animis* → *in cordibus vestris*. 1573 *& lucifer oriatur in cordibus veſtris:* (canvas 923, crop `2Pet.1.17-18-oblecto`, its last line), ἐν ταῖς καρδίαις ὑμῶν; 1758 (OCR *in corbus vestris*). **1556** *in vestris animis* (OCR *íti ueftrís anímís*), with Wikisource and 1715: a 1573 change (section 5).
   **Apply:** `2Pet.1.19` la: `oriatur in vestris animis:` → `oriatur in cordibus vestris:`
3. **2 Peter 2:16** *Asina muta, humana voce locuta* → *Jumentum mutum, humana voce locutum*. 1573 *16 Iumentum mutum, humana voce locutum, in-/hibuit vatis amentiam.* (canvas 923, crop `2Pet.2.16-Iumentum`), ὑποζύγιον ἄφωνον; 1556 (OCR *Iumentummmutum, humana uocelocutum*), 1758 (*loquutum*), 1681 (*locu-*), 1726 (*loquutum*). The early line *Asina … locuta* (Wikisource, 1750). *J* as Wikisource and your settled *jūmentum* write it.
   **Apply:** `2Pet.2.16` la: `Asina muta, humana voce locuta,` → `Jumentum mutum, humana voce locutum,`
4. **2 Peter 3:10** *ut fur nocte* → *ut fur noctu*. 1573 *Veniet autem Domini dies vt fur noctu, in qua* (canvas 924, crop `2Pet.3.10-noctu`); 1556 (OCR *utfur nociu*). The early line *nocte* (Wikisource, 1747, 1750); 1758's OCR loses the word's end (*noc*).
   **Apply:** `2Pet.3.10` la: `ut fur nocte, in qua` → `ut fur noctu, in qua`
5. **2 Peter 3:16** *Ut et in omnibus epistolis* → *Ut in omnibus epistolis*. 1573 *16 vt in omnibus epiſtolis, de hiſce rebus* (canvas 924, crop `2Pet.3.16-vt`), ὡς καὶ ἐν πάσαις; 1758, 1681, 1750. 1747 *Et in*; **1556** (OCR) *scripsit, & in omnibus epistolis*, without the *ut* (section 5). Wikisource has both words. For your eye: the Greek's καί is 1556's and 1747's *et*, not 1573's.
   **Apply:** `2Pet.3.16` la: `Ut et in omnibus epistolis` → `Ut in omnibus epistolis`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter or the other form could be construed (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The uncovered verse 1:17 was read whole on the image (intro): its differences are section 1's *dEo* and section 2c.
The lines the OCR lost (1:2, 1:9, 1:12, 2:10, 2:15, 2:20, 2:21) are printed as the draft has them. No decision needed.

## 2c. Verse boundaries (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **2 Peter 1:17–18**: the voice's words close 18. 1573 *voce delata ad eum huiuſmodi ᵍ à magnifi-/ca gloria. / 18 Hanc nos vocem audiuimus de cœlo delatam, / quum vnà cum eo eſſemus in ſacro monte: Hic eſt / meus chariſsimus filius, in quo me oblecto.* (canvas 923, crop `2Pet.1.17-18-oblecto`); 1556 (OCR *… magnifica gloria, Hanc nos uocem audiuimus … ín facro monte, Hic eft meus chariſsimus filius, ín quo mé oblecto*), 1758 (the same order; 1726 also ends 17 at *magnifica gloria.*). Castellio sets the words after the mount, where the Greek (17, Οὗτός ἐστιν ὁ υἱός μου …) and the KJV have them in 17; the early line (1715, 1747, 1750, 1681) and Wikisource keep the Greek's order. The numbering stays the KJV's; the words go where 1573 prints them. *hic*'s capital is left to stage 3. For your eye.
   **Apply:** `2Pet.1.17` la: `a magnifica gloria: hic est meus carissimus filius, in quo me oblecto.` → `a magnifica gloria.`
   **Apply:** `2Pet.1.18` la: `in sacro monte.` → `in sacro monte: hic est meus carissimus filius, in quo me oblecto.`

## 3. Word division (0)

None. 1573's joined or divided words (*perea*, *omnistudio*, *Si quidem*, *multisubsequentur*) are spacing; the draft's
division is kept (section 4).

## 4. Checked and kept

- **1:17–18**: the numbering stays the KJV's (section 2c).
- **1:2** *nostri cognitione*, **1:9** *peccatorum*, **1:12** *veritate fixos*, **2:10** *horrent*, **2:15** *suique
  criminis convictus est*, **2:20** *priore deterior*, **2:21** *retro recessisse*: lines the OCR lost, printed (crops
  `2Pet.1.2-cognitione`, `2Pet.1.9-expiationis`, `2Pet.1.12-veritate`, `2Pet.2.10-horrent`, `2Pet.2.15-Balaami`,
  `2Pet.2.20-conditio`, `2Pet.2.21-recessisse`). Kept.
- **2:8** *justum animum*: 1573 *iuſtũ ᵃ animum* (canvas 923, crop `2Pet.2.7-qui`, its last line; margin *a animum
  … hoc est, ei*), the OCR's *iustu*. Kept.
- **1:13** *in hoc domicilio*: 1573's OCR *hoce* is *hoc* and the note letter *e* (margin *e corpore*). **2:12** *de
  eis*, **2:13** *de vobis in suis*: the OCR's *deceis*, *din* are note letters *c*, *d*. Kept.
- **2:19** *Siquidem* (1573 *Si quidem*), **2:2** *multi subsequentur* (1573 *multiſubſequentur*), **1:4** *per ea*
  (1573 *perea*), **1:5** *omni studio* (1573, 1556 *omniſtudio*): spacing; kept.
- **1:21** *homines divini*: printed (1573 *ho-/mines diuini*, before the chapter summary); 1758 and 1681 lose it in
  their OCR. Kept.
- **2:4** *in tartarearum tenebrarum catenas*: 1573 *tartarearũ tenebrarum* (OCR). Kept.
- **Note letters and margin notes**, not text: 1:3 *a* (*Dei*), *b* (*Christi*), 1:4 *c* (*Christum*), *d* (*pater*),
  1:13 *e* (*corpore*), 1:16 *f* (*cum sapientiæ specie fictas*), 1:17 *g* (*à glorioso Deo*), 1:19 *h* (*scil. ad
  suadendum hominibus Christum*), 2:8 *a*, 2:11 *b* (*… epist. de Mo-…*), 2:12 *c*, 2:13 *d*, 2:14 (*… purantes …
  errent ipsi*); the scripture references in the margin (at 1:18, 1:19, 2:6, 2:15, 2:17, 2:20, 2:22, 3:5, 3:8, 3:9 and
  3:12, the OCR's *Num.22.25*, *Inda*, *Pron.26.12*, *Apoc.al,1* among them); the chapter summaries; and 1573's annotations after
  chapters 2 and 3 (on 2:4, 2:14, 2:18; on 3:5–6).
- **Punctuation and capitals, left to stage 3**: 1:1 *sortiti sunt.* (1573 a comma), 1:17–18 *hic* (1573 *Hic*), 2:20
  *Domini et Servatoris* (1573 *domini & seruatoris*), 3:2 *Domini Servatorisque* (1573 *seruatorisq;*), 3:4 *ubi est*
  (1573 *Vbi*), 3:11 *quales decet esse vos in sanctis moribus … Dei?* (1573 *esse vos? in sanctis … Dei,*), 3:18
  *Servatorisque* (1573 *seruatorisq;*).
- **Spellings, left to stage 3** (decisions 37 and 42's rules, and section 6): *quum*, *Quum* (1573 *cùm*, *quum*),
  *carissimi*, *carissimus* (1573 *chariſsimi*), *caritatem* (1573 *charitatem*), *numquam*, *umquam*, *quemquam*,
  *quamquam*, *tamquam*, *quamdiu* (1573 *nunquam*, *vnquam*, *quenquam*, *quanquam*, *tanquam*, *quandiu*), *otiosos*,
  *otiatur* (1573 *ocio-*), *Verumtamen* (1573 *Veruntamen*), *adquirentes* (section 6), *adsunt* (a compound of *sum*,
  kept), *adsiduam*, *adspectu* (1573 *aſsiduam*, *aſpectu*), *exspectantes*, *exspectamus*, *exspectandis* (1573
  *exp-*), *negligam* (section 6), *intelligatis*, *quotidianis*, *litteras* (1573 *literas*), *caelo*, *caeli*,
  *caelos*, *caeni* (1573 *cœl-*, *cæl-*, *cœni*), *foeditatibus*, *cetera* (1573 *cætera*), *herum*, *eis*, *Eisque*,
  *Gomorrhaeque*, *Noa*, *Lotum*, *Jesu*, *ejus*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282443–44), not the page image; it hardly reaches 1:1–4 and 2:1–6.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 2 Pet 1:19 | *et lucifer oriatur in cordibus vestris* | = | *et lucifer oriatur in vestris animis* | Wikisource, 1715 with 1556; 1758 with 1573 |
| 2 Pet 2:5 | *impiorum generi diluvium invexerit* | = | OCR *ínuexít* (*invexit*; doubtful, the columns interleaved) | every other printing with 1573 |
| 2 Pet 3:15–16 | *vobis scripsit, Ut in omnibus epistolis* | = | *uobis scripsit, & in omnibus epistolis* (OCR *ferípfie,& ín omnibus*) | 1747 *Et in*; Wikisource *Ut et in*; 1758, 1681, 1750 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12; 2:5 recorded as
doubtful, the OCR alone)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) and decision 42 writes *neglegō*
(as the approved *negligere → neglegere*); these 2 Peter forms have no row in `data/rules/orthography.tsv` yet
(checked with `normalize.propose()` on the draft). Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adquirentes | acquirentes | word | 1:5 | 1573 *acqui-/rentes* (canvas 922–923); 1556, 1747 (*acquírentes*); as the approved *adquiescis → acquiescis*; Gaffiot *acquīrō* |
| negligam | neglegam | word | 1:12 | decision 42 (Gaffiot *neglegō*); as the approved *negligere → neglegere*; 1573 *negligam* (canvas 923, crop `2Pet.1.12-veritate`) |

(1:9 *adsunt* is a compound of *sum*, left as it is; *adventum*, *aditus* do not assimilate; *adsiduam* and
*adspectu* have their approved rules.)

**Decision:** accept (Claude, 2026-11-12, under decisions 37, 42 and 46; added to `data/rules/orthography.tsv`)