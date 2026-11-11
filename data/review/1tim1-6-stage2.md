# 1 Timothy 1–6, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of Galatians (`data/review/gal1-6-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 909–912: 1:1–2:15 on 909, 3:1–4:16 on
  910, 5:1–6:3 on 911, 6:4–6:21 on 912). 1556 is the reference: where it reads otherwise, its reading is recorded as
  a variant (section 5). Stage 1 drafted Wikisource's 1 Timothy as **`text/draft/1TI.usfm`** (BSB paragraphs). You
  have no earlier work on 1 Timothy; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the
  witness `1726`, read as an OCR.
- **Wikisource's 1 Timothy is the early wording**, as its Galatians and Colossians: *favorem* for *gratiam* (1:2),
  *favor* for *gratia* (6:21), *cinaedis* for *paediconibus* (1:10), *rem bonam* for *bonum munus* (3:1), *loquentes,
  quae non debeant* for *loquentes illicita* (5:13), each with the early-line printings 1715, 1747, 1750, and slips
  of its own (*inadspectablil*, *fidelix*, *suus*, *praescentis*, *questu*, *potes*, *suppedtat*, *Absit*). 1556 has
  the revised readings where its OCR can be read, but four are 1573's own changes against 1556: 1:5 *Enimvero* (1556
  *Atqui*), 2:4 *veritatis* (1556 *veri*), 3:16 *apparuit in carne* (1556 *extitit in corpore*) and 4:2 *inustam*
  (1556 *iniustam*), section 5. 1750 shares several of Wikisource's slips (1:3 *te Macedoniam*, 5:10 *subvenit*
  without *si*).
- **Versification** (decision 5): the draft is at the KJV counts (113 verses), no edits file. 1573 prints every
  verse number and agrees with the draft but in two places:
  - **1:3–4**: 1573 prints 4 before *neue fabulas attendant* (canvas 909, on the image), as the KJV's 1:4 (*Neither
    give heed to fables and endless genealogies*); the draft ends 3 with it. Moved to 4 (section 2c).
  - **6:16–17**: 1573 prints 17 before *Amen* (canvas 912, *æternum. / 17 Amen. Iis qui in hac vita*), and the
    1726 printing too; the KJV's 6:16 ends *power everlasting. Amen.*, as the draft. Kept; nothing to move.
- **Collation** (`python -m pipeline collate 1Tim 1-6`; `data/calibration/1Tim1-6-collation.tsv`, 186 places: 33
  correct, 7 others-1573-agrees, 8 others, 136 base-only (87 reading, 22 division, 18 f/s, 5 edge, 4 spelling), 2
  uncovered), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/1Tim.*`, 39):
  every reading where 1573 and another printing agree against Wikisource, the *others* places, the base-only places
  whose 1573 words are Latin (1:3 *in*, 1:19 *bonamque*, 3:1 *bonum munus*, 5:4 *parentibus*, 5:8 *et*, 6:6
  *forte*), and the edge places (1:4 *fi-de instructionem*, 1:10 *contrarium est* and 3:13 *collocanda libertatem*
  at the head of the next column, 5:11 *nubere volunt*, 6:6 *contentum esse*: all printed, lost by the OCR). The rest
  of the base-only readings are 1573's OCR (*tantuın*, *Vous*, *hono*, *forinatus*), word breaks at line ends, note
  letters and margin notes run into the text (section 4). Each place was also read against 1556 (its e-rara OCR,
  `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 909–912), not only the collation's places:
  nothing further beyond the spacing slips of section 3.
- **The two verses 1573's OCR covers poorly** (4:2, 5:13; `uncovered`) were read whole on the image: 4:2 *per
  ſimulationem hominum falſiloquorum, inu-ſtam habentium conſcientiam* (section 2) and 5:13 *Adde qđ ocioſæ diſcũt
  peruagari domos: nec ſolũ ocioſę, verũetiam nugaces, & curioſę, loquẽtes illicita* (section 2). Section 2b is empty.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *fidens*,
  *fili*, *finis*, *fore*, *fuerit*, *fuge*, *fuit*, *futurae*, *faciens*, *falso*, *feminas*, *profecto*,
  *confessione*, 21 words) was read in its verse: all are *f*. Every *s* word whose *f*-form is Latin (*si/fi*,
  *sit/fit*, *sine/fine*, *sontes/fontes*, *sorte/forte*, *simus/fimus*, *servi*, *serves*, *sanis/fanis*, *soli*,
  *suam*, *saecula*, *secundum*, *sumatur*, 16 words): all are *s* by sense, and the places where 1573's OCR has the
  *f* and the *f*-form would make sense were read on the image: 3:6 *Ne ſit nouitius*, 3:15 *quomodo ſit*, 4:8 *Cùm
  ſit enim*, 1:15 *ſontes*, 6:6 *ſua ſorte* are all long s. None found.
- **In all, 29 corrections** (30 Apply lines): 12 Wikisource slips (section 1), 10 readings of Castellio's revised
  text (section 2), 1 verse boundary (section 2c), 6 word divisions and spacings (section 3). Spellings
  (*caritas*, *cari*, *quum*, *adfirment*, *adficiantur*, *adflictis*, *sumtuoso*, *intellegit*, *exsereret*,
  *exsequare*, *auctoritatem*, *vindicare*, *otiosae*) are left to stage 3 (decision 37's rules); four rules
  proposed (section 6). Places kept against 1573 are in section 4, for your eye.

## 1. Wikisource slips: 1573 and the other printings agree against it (12)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **1 Timothy 1:3** *ego te Macedoniam proficiscens* → *ego te in Macedoniam*. 1573 *Quemadmodum ego te in Macedoniam profici-ſcens* (canvas 909); 1556 (*ego te ín*), 1758, 1681, 1715, 1747. 1750 drops *in* with Wikisource.
   **Apply:** `1Tim.1.3` la: `ego te Macedoniam` → `ego te in Macedoniam`
2. **1 Timothy 1:13** *Sed mei misertus est* → *Sed mei misertum est*. 1573 *Sed mei miſertum eſt, quoniam igna-rus feci* (canvas 909; impersonal, as Gaffiot's *misertum est*); 1556, 1758, 1681, 1715, 1750, 1726. Wikisource alone.
   **Apply:** `1Tim.1.13` la: `mei misertus est` → `mei misertum est`
3. **1 Timothy 1:17** *immortali, inadspectablil, soli* → *inadspectabili*. 1573 *immortali, inaſpectabili, ſoli ſa-pienti* (canvas 909); 1556 (*inafpectabili*), 1715, 1750 (*inadſpectabili*). The *ad-* is stage 3's (the approved stem *inadspect → inaspect*).
   **Apply:** `1Tim.1.17` la: `inadspectablil,` → `inadspectabili,`
4. **1 Timothy 1:19** *Fidem habens, bonam conscientiam* → *bonamque conscientiam*. 1573 *fidem habens, bonamq; conſcientiam* (canvas 909; its OCR *bonamq*); 1556 (*bonamép*), 1758, 1715, 1750.
   **Apply:** `1Tim.1.19` la: `habens, bonam conscientiam` → `habens, bonamque conscientiam`
5. **1 Timothy 2:7** *alienigenarum fidelix* → *fidelis*. 1573 *alienigenarum fidelis atq; verax* (canvas 909); 1556, 1758, 1715, 1747, 1750.
   **Apply:** `1Tim.2.7` la: `alienigenarum fidelix` → `alienigenarum fidelis`
6. **1 Timothy 3:12** *liberos domosque suus* → *suas*. 1573 *liberos do-moſq; ſuas bene regentes* (canvas 910); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `1Tim.3.12` la: `domosque suus bene` → `domosque suas bene`
7. **1 Timothy 4:8** *et praescentis et futurae* → *et praesentis*. 1573 *præſentis & futuræ vitæ* (canvas 910); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `1Tim.4.8` la: `et praescentis et` → `et praesentis et`
8. **1 Timothy 5:10** *pedes lavit, subvenit adflictis* → *pedes lavit, si subvenit adflictis*. 1573 *ſi ſanctorum pedes lauit, ſi / ſubuenit afflictis, ſi omnia* (canvas 911), the fifth of the *si* clauses; 1758, 1715, 1747, 1726. 1750 drops *si* with Wikisource; 1556's OCR is garbled here.
   **Apply:** `1Tim.5.10` la: `pedes lavit, subvenit` → `pedes lavit, si subvenit`
9. **1 Timothy 6:5** *pietatem pro questu habentium* → *pro quaestu*. 1573 *pietatem pro quæſtu haben-tium* (canvas 912); 1556, 1758, 1715, 1747, 1750, 1726. *questu* is *questus*, a complaint; *quaestus* is 6:6's own word (πορισμόν).
   **Apply:** `1Tim.6.5` la: `pro questu habentium` → `pro quaestu habentium`
10. **1 Timothy 6:16** *neque videre potes* → *neque videre potest*. 1573 *neque videre poteſt, cui honor* (canvas 912); 1556, 1758, 1681, 1747, 1750, 1726.
   **Apply:** `1Tim.6.16` la: `videre potes,` → `videre potest,`
11. **1 Timothy 6:17** *omnia large suppedtat* → *suppeditat*. 1573 *omnia largè ſuppeditat ad fruitionem* (canvas 912); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `1Tim.6.17` la: `large suppedtat` → `large suppeditat`
12. **1 Timothy 6:21** *Absit tibi* → *Adsit tibi*. 1573 *Ad-ſit tibi gratia: Amen.* (canvas 912); 1556 (OCR *A díit*), 1758, 1715, 1747, 1750, 1726. Wikisource's *Absit* says the opposite (ἡ χάρις μετὰ σοῦ).
   **Apply:** `1Tim.6.21` la: `Absit tibi favor` → `Adsit tibi favor`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (10)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in form. 1556 has the
revised reading too wherever its OCR can be read, except 1:5, 2:4, 3:16 and 4:2 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **1 Timothy 1:2** *in fide filio, favorem, misericordiam* → *gratiam*. 1573 *filio, gratiam, miſericordiam, pa-cem* (canvas 909), χάρις; 1556 (*gra tíam*), 1758. The early line *favorem* (Wikisource, 1715, 1747, 1750), as Colossians 1:2.
   **Apply:** `1Tim.1.2` la: `filio, favorem, misericordiam` → `filio, gratiam, misericordiam`
2. **1 Timothy 1:5** *Atqui praeceptionum finis* → *Enimvero praeceptionum finis*. 1573 *5 Enimuerò præceptionum finis eſt charitas* (canvas 909, on the image); 1758. **1556** *Atqui*, with Wikisource, 1747, 1750: a 1573 change (section 5). For your eye: a particle, τὸ δὲ τέλος.
   **Apply:** `1Tim.1.5` la: `Atqui praeceptionum` → `Enimvero praeceptionum`
3. **1 Timothy 1:10** *impudicis, cinaedis, plagiariis* → *impudicis, paediconibus, plagiariis*. 1573 *impudicis, pædiconibus, plagiarijs* (canvas 909), ἀρσενοκοίταις; 1556 (*padíconíbus*), 1758, 1681, 1726. The early line *cinaedis* (Wikisource, 1747, 1750). Gaffiot has *pædīcō, ōnis*.
   **Apply:** `1Tim.1.10` la: `impudicis, cinaedis,` → `impudicis, paediconibus,`
4. **1 Timothy 2:4** *et ad veri cognitionem venire* → *et ad veritatis cognitionem*. 1573 *& ad veritatis / cognitionem venire* (canvas 909), ἐπίγνωσιν ἀληθείας; 1758, 1681 (OCR *tatiscognitionem*). **1556** *ad ueri*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5).
   **Apply:** `1Tim.2.4` la: `ad veri cognitionem` → `ad veritatis cognitionem`
5. **1 Timothy 3:1** *expetit, rem bonam cupit* → *expetit, bonum munus cupit*. 1573 *ſi quis epiſcopi munus expetit, bo-/num munus cupit* (canvas 910), καλοῦ ἔργου; 1758 (OCR *bonur munus*), 1681. The early line *rem bonam* (Wikisource, 1747, 1750); 1556's OCR does not reach the verse.
   **Apply:** `1Tim.3.1` la: `expetit, rem bonam cupit` → `expetit, bonum munus cupit`
6. **1 Timothy 3:16** *Deus apparuit in corpore* → *in carne*. 1573 *Deus / apparuit in carne, per ſpiritum* (canvas 910), ἐν σαρκί; 1758, 1681, 1726. Wikisource *in corpore* with 1715, 1747, 1750; **1556** *Deus extitit in corpore* (OCR *extítít ín corpore*): a 1573 change (section 5), as Colossians 3:22 *corpus → caro*.
   **Apply:** `1Tim.3.16` la: `apparuit in corpore,` → `apparuit in carne,`
7. **1 Timothy 4:2** *injustam habentium conscientiam* → *inustam*. 1573 *inu-/ſtam habentium conſcientiam* (canvas 910; an uncovered verse, read whole on the image), κεκαυστηριασμένων, branded; 1758. **1556** *iniustam* (OCR *iníuftà*), with Wikisource and 1750 (1747's OCR garbled, *iniuinen ftam*): a 1573 change (section 5).
   **Apply:** `1Tim.4.2` la: `falsiloquorum, injustam habentium` → `falsiloquorum, inustam habentium`
8. **1 Timothy 5:4** *Quod si qua vidua* → *Quod si quae vidua*. 1573 *Quòd ſi quæ vidua liberos habet* (canvas 911); 1556 (*quz*), 1758, 1750. Wikisource *qua* with 1747. For your eye: both forms are Latin after *si*; 5:8 *si qua suorum* is *qua* in 1573 and stays, 5:16 *si quae fidens* is *quae* in both.
   **Apply:** `1Tim.5.4` la: `Quod si qua vidua` → `Quod si quae vidua`
9. **1 Timothy 5:13** *curiosae, loquentes, quae non debeant* → *curiosae, loquentes illicita*. 1573 *& curioſę, loquẽtes illicita.* (canvas 911; an uncovered verse, read whole on the image), λαλοῦσαι τὰ μὴ δέοντα; 1556 (OCR *loquentes fllíaLI*), 1726. The early line *quae non debeant* (Wikisource, 1747, 1750).
   **Apply:** `1Tim.5.13` la: `loquentes, quae non debeant.` → `loquentes illicita.`
10. **1 Timothy 6:21** *Adsit tibi favor* → *gratia*. 1573 *Ad-ſit tibi gratia: Amen* (canvas 912), ἡ χάρις; 1556, 1758, 1726. The early line *favor* (Wikisource, 1715, 1747, 1750). (After section 1's item 12.)
   **Apply:** `1Tim.6.21` la: `tibi favor:` → `tibi gratia:`
## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The two uncovered verses (4:2, 5:13) were read whole on the image (crops `1Tim.4.2-inustam`, `1Tim.5.13-illicita`):
their only differences from the draft are 4:2 *inustam* and 5:13 *illicita* (section 2), both already collation
places. No decision needed.

## 2c. Verse boundaries: 1:3–4, 4:12–13 (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **1 Timothy 1:3–4**: *neve fabulas attendant* opens 4. 1573 *denuncies ne aliam ſequantur doctrinam, / 4 neue
   fabulas attendant, & antiquitates infinitas* (canvas 909); 1681 (*4 NeVe fabulas*) and 1747 (*4. Neue fabulas*)
   print 4 there too, and the KJV's 1:4 is *Neither give heed to fables and endless genealogies* (μηδὲ προσέχειν
   μύθοις). Wikisource ends 3 with it. The capital follows the draft's verse openings; stage 3 decides it.
   **Apply:** `1Tim.1.3` la: `doctrinam, neve fabulas attendant,` → `doctrinam,`
   **Apply:** `1Tim.1.4` la: `Et antiquitates infinitas` → `Neve fabulas attendant, et antiquitates infinitas`
2. **1 Timothy 4:12–13**: *donec veniam* opens 13, as the KJV (*Till I come, give attendance to reading*; ἕως
   ἔρχομαι πρόσεχε τῇ ἀναγνώσει). 1573 (canvas 910) and Wikisource end 12 with it; the edition follows the KJV's
   verses (decision 5), as Gal 5:23. The comma before it becomes the verse's full stop, and *Donec* takes the capital
   of a verse opening its sentence. Added by Claude 2026-11-11 after the stage-3 reader found it (layout line for
   4:12 changed to match).
   **Apply:** `1Tim.4.12` la: `castitate, donec veniam.` → `castitate.`
   **Apply:** `1Tim.4.13` la: `Da operam lectioni` → `Donec veniam, da operam lectioni`

## 3. Word division and spacing (6)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **1 Timothy 1:3** *maneto Ephesi ,ut* → *maneto Ephesi, ut*. A misplaced space; 1573 *maneto Epheſi, vt* (canvas 909).
   **Apply:** `1Tim.1.3` la: `Ephesi ,ut` → `Ephesi, ut`
2. **1 Timothy 1:10** *periuris, etsi quid aliud* → *periuris, et si quid aliud*. 1573 *periuris, & ſi quid aliud* (canvas 909, on the image), καὶ εἴ τι ἕτερον, “and if there be any other thing”; 1556, 1758, 1750, 1726. Wikisource joins it with 1747, making *etsi*, “although”.
   **Apply:** `1Tim.1.10` la: `periuris, etsi quid` → `periuris, et si quid`
3. **1 Timothy 2:6** *Qui seipsum liberationis* → *Qui se ipsum*. Your settled *sē ipsum* (18×) against *seipsum* 4×, as Galatians 1:4. 1573 joins it (*ſeipſum*, canvas 909).
   **Apply:** `1Tim.2.6` la: `Qui seipsum liberationis` → `Qui se ipsum liberationis`
4. **1 Timothy 2:15** *in fide,et caritate* → *in fide, et caritate*. A missing space; 1573 *in fide, & charitate* (canvas 909).
   **Apply:** `1Tim.2.15` la: `fide,et caritate` → `fide, et caritate`
5. **1 Timothy 4:7** *ac teipsum ad pietatem* → *ac te ipsum*. The draft divides it at 4:16 and 5:22 (*te ipsum*), your settled text *tē ipsum* 13× in the Gospels; not a quotation (the exception of Rom 13:9 and Gal 5:14). 1573 joins all three (*teipſum*, canvases 910–911).
   **Apply:** `1Tim.4.7` la: `ac teipsum ad` → `ac te ipsum ad`
6. **1 Timothy 6:16** *aeternum:Amen.* → *aeternum: Amen.* A missing space; 1573 *æternum. / 17 Amen.* (canvas 912; the verse number, intro).
   **Apply:** `1Tim.6.16` la: `aeternum:Amen.` → `aeternum: Amen.`

## 4. Checked and kept

- **6:16–17**: 1573 numbers *Amen* as 17 (intro); the KJV keeps it in 16. Kept.
- **5:4** *parentibusque vicem reddere*: 1573 *paren-/tibusq; vicem reddere* (canvas 911, on the image; its OCR lost
  the *q;*), with 1556 and every printing. No difference.
- **5:8** *ea fidem abnegavit*: 1573's OCR *ea & fidem* is the note letter *b* (canvas 911, margin *b Christianã
  religionem*), as 1556 (*ea b fídem*). Kept.
- **Edge places, printed in 1573** (on the image): 1:4 *in fi-/de instructionem*, 1:10 *contrarium eſt,* (at the head
  of the right column), 3:13 *collo-/canda libertatem*, 5:11 *nu-/bere volunt*, 6:6 *con-/tentum eſſe*. Kept.
- **1:2** *Domino Jesu Christo*: 1573 *Dño* (the abbreviation). Kept.
- **5:13** *verum etiam*: 1573 *verũetiam*; kept apart, as 1758, 1681, 1747, 1750 (as Ephesians 1:21).
- **Note letters and margin notes**, not text: 1:2 *a*, 1:9 *b* (*… quod si lex lata non esset, nihilominus recte
  viverent*), 3:7 *a*, 3:9 *b* (*religionis*), 3:11 *e* (*scilicet co…*), 3:16 *d*
  (*Christianae religionis*), 4:14 *a* (*divino iussu*), 5:6, 5:8 *b* (*Christianam religionem*), 5:9 (*scilicet
  ad ministrandum …*), 5:11 *d* (*ad ministrandum ne admittito*), 5:22 *e* (*si vitiosum admiseris …*), 5:23, 6:8
  (*vestimenta*), 6:10 *b* (*Christiana religione*); the gloss *assiduam scripturae lectionem* printed beside 4:8 (it
  belongs to 4:13's *lectioni*); the scripture references in the margin (as the OCR reads them: 1:5 *Tit. 2. 14*, 1:20 *1. Cor. 5.*, 2:9
  *1. Petr. 3.*, 4:2 *2. Thes. 2.*, 5:18 *Deut. 25. 4*, 6:15 *Apoc. 17. 14*); and 1573's annotations after each
  chapter.
- **6:21** the subscription (*Scripta est Laodiceae, quae Pacatianae Phrygiae caput est*): 1573 sets it in italics
  under the verse (canvas 912, *Scripta eſt Laodiceæ, quæ Pacatianæ / Phrygiæ caput eſt.*), as the draft but its
  final stop. Set apart as `\cls` at stage 3 (decision 37).
- **Punctuation, left to stage 3**: 1:8 *utatur:* (1573 a stop), 3:5 *procurabit.* (1573 *?*), 6:21's final stop.
- **Spellings, left to stage 3** (decision 37's rules, and section 6): *caritas*, *caritate*, *caritatem*, *cari*
  (1573 *charit-*, *chari*), *quum*, *Quum* (1573 *cùm*, *Cùm*, *Cum*; decision 41), *denunties*, *denuntiato*,
  *denuntia* (1573 *denunc-*), *adfirment*, *adficiantur*, *adflictis*, *adsecutus*, *adsequantur* (1573 *aff-*,
  *aſſ-*), *inadspectabili* (1573 *inaſpectabili*), *exsereret*, *exsequare* (1573 *exereret*, *exequare*; your
  settled *exser-*, *exsequ-*), *sumtuoso* (1573 *ſumptuoſo*), *precium*/*pretium* (1573 *precium*), *auctoritatem*,
  *vindicare* (1573 *authoritatem*, *vendicare*; your settled *vindic-*), *intellegit*, *intelligens* (1573
  *intellig-*), *otiosae* (1573 *ocioſæ*), *feminas* (1573 *fœminas*), *saeculorum*, *saecula* (1573 *ſecul-*),
  *Quicumque* (1573 *Quicunq;*), *litterae* (1573 *literæ*), *obedientia*, *tentationem*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 1 Tim 1:5 | *Enimvero praeceptionum* | = | *Atqui praeceptionum* | Wikisource, 1747, 1750 with 1556; 1758 with 1573 |
| 1 Tim 2:4 | *ad veritatis cognitionem* | = | *ad veri cognitionem* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 Tim 3:16 | *Deus apparuit in carne* | = | *Deus extitit in corpore* | Wikisource, 1715, 1747, 1750 *apparuit in corpore*; 1758, 1681, 1726 with 1573 |
| 1 Tim 4:2 | *inustam habentium conscientiam* | = | *iniustam* (OCR *iníuftà*) | Wikisource, 1750 with 1556; 1758 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) word by word; these 1 Timothy forms
have no row in `data/rules/orthography.tsv` yet (checked with `normalize.word_rules()`). Proposed, not written to the
file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adfirment | affirment | word | 1:7 | 1573 *affirment* (canvas 909); 1758, 1747; your settled *affirm-*; as the approved *adfirmavit → affirmavit* |
| adficiantur | afficiantur | word | 5:17, 5:20 | 1573 *afficiantur* (canvas 911); 1758, 1747, 1556; your settled *affici-*; as the approved *adfici → affici* |
| adflictis | afflictis | word | 5:10 | 1573 *afflictis* (canvas 911); 1758, 1715, 1747, 1726; as the approved *adflictum → afflictum* |
| sumtuoso | sumptuoso | word | 2:9 | 1573 *ſumptuoſo* (canvas 909); Gaffiot *sūmptuōsus*; as the approved *sumtus → sumptus* |

**Decision:** propose (Claude, 2026-11-11; for your approval)
