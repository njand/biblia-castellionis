# Philippians 1–4, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of 2 Corinthians (`data/review/2cor1-13-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 898–900). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's Philippians as
  **`text/draft/PHP.usfm`** (BSB paragraphs). You have no earlier work on Philippians; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Philippians is the early wording**, as its Romans and Corinthians, with slips of its own: *Favorem*
  for *Gratiam* (1:2), *favor* for *gratia* (4:23), *in cognitione omnique* for *in omni cognitione et* (1:9),
  *interiora* for *anteriora* (3:14), *fratres* (3:17), *ut* (3:18) and *et* (4:4, 4:9) that 1556 and 1573 do not print.
  1556 already has every one of these revisions. 1573's own change against 1556 is 4:19 *quibus* (1556 *quicquid*),
  and 1573 adds *& acceptorum* in 4:15 (section 5).
- **Versification**: the draft is at the KJV's counts (30, 30, 21, 23 verses); no edits. 1573 numbers every verse as
  the KJV (canvases 898–900).
- **Collation** (`python -m pipeline collate Phil 1-4`; `data/calibration/Phil1-4-collation.tsv`, 164 places; no
  verse uncovered). Read on the page image (crops in `sources/mdz-1573/crops/Phil.*`, 38): the 22 readings where
  1573 and another printing agree against Wikisource, the places where only 1573's OCR differs and its words are
  Latin (3:17, where 1573 has no *fratres*; 3:18 and 4:4, 4:9 without *ut*/*et*; 4:19 *quibus*), and the verses whose
  1573 row is short (1:14 *ver-ba facere*, on two lines; 2:24 *breui veniam*, whose line the OCR read as a margin
  reference; 3:1 *Ea-dem* beside the initial; 3:2 *con-cisos*): all are there in full. The rest of the base-only
  readings are 1573's OCR (*queinadinodum*, *cuin*, *vestrain*), words broken at a line end, and margin notes run
  into the text (1:18 *aduersariorum odium*, 2:15 *euangelicæ doctrinæ respondentes*, 4:8, 4:18). Each place was also
  read against 1556 (its e-rara OCR, `sources/erara-1556/`, and for 2:1–4:23 its page images, e-rara 10282428–9) and
  the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **The f/s sweep**, both ways: every *f* word in the draft whose *s*-form the lexicon knows (*fore/sore*,
  *fide/side*, *confidens/considens*, *defectum/desectum*, *profectum/prosectum*, *fuerit/suerit* …, 14 words) was read
  in its verse: all are *f* (2:8 *fuerit*, 2:19 and 2:24 *fore*, 2:22 *filius*, 2:14 *facite* seen on the crops).
  The reverse (every *s* word whose *f*-form is known: *sit/fit* 5×, *sitis/fitis*, *sive/five*, *sine/fine*,
  *sumus/fumus*, *servi/fervi*, *si/fi*, *suam*, *saecula*): all are *s*; 1573 prints the long s in each one read on
  the image (1:1 *ſerui*, 1:10 *ſitis*, 1:29, 2:7, 2:16 *ſit*, 2:14 *ſine*, 3:3 *ſumus*), where its OCR has *f*.
  No f/s slip found.
- **In all, 28 corrections**: 17 Wikisource slips (section 1), 10 readings of Castellio's revised text (section 2),
  1 word division (section 3). Spellings (*adfectione*, *exspecto*, *tamquam*, *caritas*, *nequidquam*,
  *eamdem* …) are left to stage 3 (decision 37's rules); no rule added (section 6). Two 1556 readings are recorded
  as variants (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (17)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Philippians 1:1** *Phillipis* → *Philippis*. 1573 *qui ſunt Philippis* (canvas 898); 1556, 1758, 1726.
   **Apply:** `Phil.1.1` la: `sunt Phillipis,` → `sunt Philippis,`
2. **Philippians 1:3** *venit in mente* → *venit in mentem*. 1573 *quoties veſtri venit in mentem* (canvas 898); 1556, 1758, 1747, 1750.
   **Apply:** `Phil.1.3` la: `venit in mente,` → `venit in mentem,`
3. **Philippians 2:2** *eadem caritate, unanimes* → *eadem caritate praediti, unanimes*. 1573 *eadem charitate præditi, vnanimes* (canvas 899); 1556 (*prædi-ti*, page image), 1681, 1715, 1747, 1750.
   **Apply:** `Phil.2.2` la: `eadem caritate, unanimes` → `eadem caritate praediti, unanimes`
4. **Philippians 2:7** *ut, summa servili forma* → *ut, sumpta servili forma*. 1573 *vt ſumpta ſeruili forma* (canvas 899; μορφὴν δούλου λαβών); 1556, 1715, 1747, 1750, 1726.
   **Apply:** `Phil.2.7` la: `ut, summa servili` → `ut, sumpta servili`
5. **Philippians 2:7** *figura repertus est ut homo* → *figura repertus ut homo*. 1573 *& figura re-pertus vt homo* (canvas 899), no *est*; 1556 (page image), 1715, 1750, 1726.
   **Apply:** `Phil.2.7` la: `repertus est ut homo` → `repertus ut homo`
6. **Philippians 2:8** *Sese adeo deicit* → *Sese adeo dejecit*. 1573 *ſeſe adeò deiecit* (canvas 899; the perfect, as *redēgit*, *fuerit*); 1556, 1758, 1747, 1726.
   **Apply:** `Phil.2.8` la: `adeo deicit,` → `adeo dejecit,`
7. **Philippians 2:19** *mittam vobis, et ego quoque recreer* → *ut ego quoque recreer*. 1573 *mittam vobis, vt ego quoq; recreer* (canvas 899); 1556 (page image), 1758, 1715, 1747, 1750, 1726. (The collation lists 1556 with Wikisource here: its OCR runs *utego* together.)
   **Apply:** `Phil.2.19` la: `vobis, et ego quoque` → `vobis, ut ego quoque`
8. **Philippians 2:20** *parem enimo* → *parem animo*. 1573 *ei parem animo* (canvas 899); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `Phil.2.20` la: `parem enimo,` → `parem animo,`
9. **Philippians 2:22** *mecum una inservit evangelio* → *inservivit*. 1573 *mecum vnà inſeruiuit Euangelio* (canvas 899; ἐδούλευσεν); 1556 (page image), 1758, 1747, 1750, 1726.
   **Apply:** `Phil.2.22` la: `una inservit evangelio` → `una inservivit evangelio`
10. **Philippians 2:25** *Necessarium autem putavit* → *putavi*. 1573 *Neceſſarium autem putaui* (canvas 899; Paul speaks, *ad vōs mittere*); 1556, 1758, 1681, 1715, 1750, 1726.
   **Apply:** `Phil.2.25` la: `autem putavit,` → `autem putavi,`
11. **Philippians 2:25** *commilitionemque* → *commilitonemque*. 1573 *commilitonemq;* (canvas 899), from *commīlitō* (no *commilitio*); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `Phil.2.25` la: `collegam, commilitionemque` → `collegam, commilitonemque`
12. **Philippians 3:12** *jam consectutus sim* → *jam consecutus sim*. 1573 *non quia iam conſecutus ſim* (canvas 900); 1556, 1747 (1758, 1726 *consequutus*).
   **Apply:** `Phil.3.12` la: `jam consectutus` → `jam consecutus`
13. **Philippians 3:12** *sim, sed persequor* → *sim, aut jam perfectus, sed persequor*. 1573 *conſecutus ſim, aut iam perfectus, ſed perſequor* (canvas 900; ἢ ἤδη τετελείωμαι); 1556 (page image), 1758, 1747, 1750, 1726. Wikisource drops the clause.
   **Apply:** `Phil.3.12` la: `sim, sed persequor` → `sim, aut jam perfectus, sed persequor`
14. **Philippians 3:20** *nostra quidem observatio* → *nostra quidem obversatio*. 1573 *noſtra quidem obuerſatio in cœlis* (canvas 900; πολίτευμα, "dwelling"); 1556 (page image), 1715, 1747, 1750.
   **Apply:** `Phil.3.20` la: `quidem observatio in` → `quidem obversatio in`
15. **Philippians 3:21** *sibi sibjicere* → *sibi subjicere*. 1573 *qua ipſe ſibi ſubijcere poteſt omnia* (canvas 900); 1556, 1758, 1715, 1750. Written with *j* as the draft and your settled *subjici* (3×).
   **Apply:** `Phil.3.21` la: `sibi sibjicere potest` → `sibi subjicere potest`
16. **Philippians 4:3** *quae mecum certaverunt* → *certaverint*. 1573 *quæ mecum certauerint in Euangelio* (canvas 900; the subjunctive of a characterizing relative); 1556 (page image), 1758, 1715, 1747, 1750, 1726.
   **Apply:** `Phil.4.3` la: `mecum certaverunt in` → `mecum certaverint in`
17. **Philippians 4:6** *Nihil esse solliciti* → *Nihil este solliciti*. 1573 *Nihil eſte ſoliciti* (canvas 900; the imperative, μηδὲν μεριμνᾶτε); 1556 (page image), 1758, 1715, 1747, 1726.
   **Apply:** `Phil.4.6` la: `Nihil esse solliciti` → `Nihil este solliciti`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (10)

Where Wikisource reads with the early-line printings (1715, 1747, 1750). 1556 has the revised reading in every place
but 4:19 (section 5); read on its page images for 2:1–4:23, on its OCR for 1:2 and 1:9.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Philippians 1:2** *Favorem et pacem* → *Gratiam et pacem*. 1573 *gratiã & pacem à Deo patre* (canvas 898), χάρις; 1556 (OCR *gratíam*), 1758, 1681, 1726. The early line *Favorem* (Wikisource, 1715, 1750), as Romans' *favor → gratia*.
   **Apply:** `Phil.1.2` la: `Favorem et pacem` → `Gratiam et pacem`
2. **Philippians 1:9** *in cognitione omnique perspicientia* → *in omni cognitione et perspicientia*. 1573 *excellatis, in omni cognitione & perſpicientia* (canvas 898), ἐν ἐπιγνώσει καὶ πάσῃ αἰσθήσει; 1556 (OCR *ín omnícognítíone X perfpíciétía*), 1758, 1726. Wikisource with 1747, 1750.
   **Apply:** `Phil.1.9` la: `in cognitione omnique perspicientia` → `in omni cognitione et perspicientia`
3. **Philippians 3:12** *quatenus a Jesu Christo sum* → *a Christo Jesu sum*. 1573 *quatenus à Chriſto Ieſu ſum comprehenſus* (canvas 900); 1556 (page image), 1758, 1726. Wikisource's order with 1747, 1750.
   **Apply:** `Phil.3.12` la: `a Jesu Christo sum` → `a Christo Jesu sum`
4. **Philippians 3:14** *ad interiora me intendens* → *ad anteriora me intendens*. 1573 *& ad anteriora me intendens* (canvas 900), τοῖς ἔμπροσθεν, against *quae sunt a tergo*; 1556 (page image), 1758, 1681, 1726. Wikisource *interiora* with 1750 (1715's OCR *interi-*).
   **Apply:** `Phil.3.14` la: `ad interiora me` → `ad anteriora me`
5. **Philippians 3:17** *Este mei imitatores, fratres, et eos* → *Este mei imitatores, et eos*. 1573 *Eſte mei imitatores, & eos conſiderate* (canvas 900), no *fratres*; 1556 (page image), 1758. Wikisource's *fratres* (ἀδελφοί) with 1681, 1715, 1747, 1750. Both of Castellio's last editions leave the vocative out: for your eye.
   **Apply:** `Phil.3.17` la: `imitatores, fratres, et eos` → `imitatores, et eos`
6. **Philippians 3:18** *plorans dico) ut christianae crucis hostes* → *plorans dico) christianae crucis hostes*. 1573 *& nunc plorans dico) Chriſtianæ crucis hoſtes* (canvas 900), no *ut*; 1556 (page image), 1758, 1681. Wikisource's *ut* with 1715, 1747, 1750.
   **Apply:** `Phil.3.18` la: `dico) ut christianae` → `dico) christianae`
7. **Philippians 4:4** *semper; et iterum dicam* → *semper; iterum dicam*. 1573 *Gaudete in Domino ſemper: iterum dicam, gaudete* (canvas 900); 1556 (page image), 1758, 1726. Wikisource's *et* with 1715, 1747, 1750. The punctuation is left to stage 3.
   **Apply:** `Phil.4.4` la: `semper; et iterum` → `semper; iterum`
8. **Philippians 4:9** *Quae et didicistis* → *Quae didicistis*. 1573 *quæ didiciſtis, & accepiſtis* (canvas 900); 1556 (page image), 1681, 1726. Wikisource's *et* (καί) with 1715, 1747, 1750.
   **Apply:** `Phil.4.9` la: `Quae et didicistis` → `Quae didicistis`
9. **Philippians 4:19** *pro sua opulentia, quidquid vobis opus erit* → *quibus vobis opus erit*. 1573 *pro ſua opulẽtia, quibus vobis opus erit, glorioſe cumulabit* (canvas 900; *cumulāre* with the ablative of what is heaped); 1758, 1726. **1556** *quicquid* (page image), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Phil.4.19` la: `opulentia, quidquid vobis` → `opulentia, quibus vobis`
10. **Philippians 4:23** *Domini nostri Jesu Christi favor adsit* → *gratia adsit*. 1573 *Domini noſtri Ieſu Chriſti gratia adſit vobis omnibus* (canvas 900), ἡ χάρις; 1556 (page image), 1758, 1726. The early line *favor* (Wikisource, 1715, 1750).
   **Apply:** `Phil.4.23` la: `Christi favor adsit` → `Christi gratia adsit`

## 2a. Found by the f/s sweep (0)

None: every candidate read in its verse, and on the image where 1573's OCR has the other letter, is as the draft has it.

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **Philippians 1:18** *certe quoquo modo* → *certe quoquomodo*. 1573 *certè quoquomodo, ſiue in ſpeciem* (canvas 898, one word); 1556, 1758, 1726. Gaffiot's headword is *quōquōmodo* (`pipeline latin macron quoquomodo`: G *quōquōmŏdŏ*); your settled text has neither form. Wikisource apart, with 1681, 1747.
   **Apply:** `Phil.1.18` la: `certe quoquo modo,` → `certe quoquomodo,`
2. **Philippians 2:7** *Sed seipsum eo* → *Sed se ipsum eo*. 1573 *ſeipſum* (canvas 899) and 1556 join it, as Wikisource; divided to follow your settled text (*sē ipsum* 18 : *seipsum* 4) and Galatians 1:4, 6:4 and Ephesians 4:19, 5:2, 5:28, 5:33 in this batch (added by Claude 2026-11-11, after the stage-3 read, for consistency across the four books; the layout line for 2:7 changed to match).
   **Apply:** `Phil.2.7` la: `Sed seipsum eo` → `Sed se ipsum eo`

## 4. Checked and kept

- **2:7** *Sed seipsum eo usque* (the division of *seipsum* was then made in section 3, item 2): 1573 *ſeipſum eouſq;* (canvas 899), 1556 *seipsum eousque*. Your settled text has both
  *seipsum* (4×) and *sē ipsum* (18×), both *eō ūsque* (Acts 7:19, 24:6) and *eōusque* (Exod 9:10, 11:8); Gaffiot
  knows no *eousque*. Kept as Wikisource; for stage 3.
- **1:29** *verum etiam*: 1573 and 1556 *verumetiam*; your settled *vērum etiam* (11×). Kept.
- **3:1** *neque me piget* and **4:11** *Neque propter inopiam*: as 1573 (canvas 900). 1556's OCR reads *nec* and
  *Nec*, but its page images (10282428–9) print *neq;* both times: no variant.
- **4:15** *ad rationem expensorum et acceptorum*: as 1573 (canvas 900, *expen-ſorum & acceptorum*). 1556 lacks
  *et acceptorum* (section 5).
- **1:14** *impavidi verba facere*, **2:24** *brevi veniam*, **3:1** *Eadem*, **3:2** *concisos*: 1573 prints them
  (lines its OCR broke or lost; 2:24's *1. torto. 4.* is the margin reference *1. Corint. 4*).
- **Note letters and margin notes**, not text: 1:8 *a* (*Christiana*), 1:18 (*… aduersariorum odium*), 2:15 *a*
  (*euangelicæ doctrinæ respondentes …*), 4:8 *a* (*si quid cum virtute coniunctum & laudabile est*), 4:15 *b*, 4:18
  (*res sit vobis vtilissima*), 4:19 *Rom. 12*.
- **4:23** the subscription (*Missa Roma per Epaphroditum*): 1573 sets it in italics under the verse (canvas 900), as
  1556 (page image). Set apart as `\cls` at stage 3 (decision 37).
- **Punctuation**, left to stage 3: 1:13 *in christianitate, facta*, 1:27 *dimicantes:*, 2:7 *ut, sumpta servili
  forma,* (1573 *vt ſumpta ſeruili forma,*), 3:15 *sentiamus. Quod* (1573 colon), 4:4 (1573 colon).
- **Spellings, left to stage 3** (decision 37's rules): *adfectione*, *adflictionem*, *adsecutum* (1573 *affectione*,
  *afflictionem*, *assequutum*), *exspecto*, *exsuperans* (1573 *expecto*, *exuperans*), *tamquam*, *quamquam* (1573
  *tanquam*, *quanquam*), *caritate*, *caritatis*, *cari*, *carissimi* (1573 *charit-*, *chari*, *charissimi*),
  *solliciti*, *opportunitate* (1573 *soliciti*, *oportunitate*; Gaffiot *sollicitus*, *opportūnitās*), *nequidquam*
  (1573 *nequicquam*), *quidquam* (1573 *quicquam*), *eamdem* (1573 *eandem*), *Quinimmo* (1573 *Quinimò*; Gaffiot
  *quīnimmo*), *saecula* (1573 *secula*), *ceterisque*, *Ceterum* (1573 *cæteris*, *Cæterùm*), *quum* (1573 *cùm*).

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). Both read on 1556's page image (e-rara
10282429), not only its OCR.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Phil 4:15 | *ad rationem expensorum et acceptorum* | = | *ad rationem expensorum, nisi vos solos* (margin *b*: *quod vel illi mihi expensum, vel eis ego acceptum ferre possem*) | Wikisource, 1758, 1750 with 1573 |
| Phil 4:19 | *pro sua opulentia, quibus vobis* | = | *quicquid vobis* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1726 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

None added. Every spelling difference above falls under decision 37's rules or is already Gaffiot's form in
Wikisource (*solliciti*, *opportunitate*, *Quinimmo*). For later books, a phrase rule **`quoquo modo → quoquomodo`**
(Gaffiot's headword; 1573 and 1556 join it) would save a section-3 item each time: proposed, not entered in
`data/rules/orthography.tsv`. *nequidquam* (2:16, twice; 1573 *nequicquam*) waits on the proposed *quicquam →
quidquam* rule (`data/review/spelling-audit.md` A), which it would follow.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)
