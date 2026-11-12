# Revelation 12–22, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of Jude (`data/review/jude1-stage2.md`) and 1 John
(`data/review/1john1-5-stage2.md`). Revelation 1–11 is reviewed apart; this file touches only 12–22.

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 942–948: chapter 12's heading and summary at
  the foot of 942, 12:1–14:4 on 943, 14:4–16:18 on 944, 16:18–18:16 on 945, 18:17–20:6 on 946, 20:6–22:3 on 947,
  22:4–21 on 948). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant (section 5);
  its e-rara OCR has these chapters on pages 10282458–63, the columns interleaved on 10282458 (12:1–13:1) and in
  places on 10282459–63. Stage 1 drafted Wikisource's Revelation as **`text/draft/REV.usfm`** (BSB paragraphs), at
  the KJV count in every chapter (12–22: 210 verses). You have no earlier work on Revelation; `TXT/1 - OCR` (the
  1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **The book's end** (canvas 948, crop `Rev.22.21-end`): after 22:21 1573 prints *NOVI TESTAMENTI / FINIS.*, then a
  closing note to the reader in italics, *Habes, Lector, quæ nos in præſentia potuimus. Quòd ſi quid bene dictum eſt,
  Deo tribui laus debet, omnium bonorum datori: ſin quid erratum eſt, ignoſce nobis, vt ipſe tibi velles ignoſci.
  Deinceps, ſi voluerit Deus vt plura & meliora diſcamus, plura & meliora dabimus, volente DEO.*, then *ERRATA SIC
  CORRIGITO* (corrections to the Old Testament: Psalms, Wisdom, Ecclesiasticus, Isaiah, and page-and-line numbers).
  Canvases 949–950 are blank; 951 begins *INDEX COPIOSVS RERVM ET VERBORVM CONTENTORVM IN VETERI TESTAMENTO*. 1556's
  OCR ends Revelation with its title line garbled (*N O y … TAM BNuT I … RF N i*, page 10282463, as *Novi Testamenti
  finis*) and goes on to Castellio's annotations (10282464); the *Habes, Lector* note was not found in its OCR (pages
  10282460–79 searched for *Lector*).
- **Wikisource's Revelation 12–22 is the early wording**, with the early-line printings 1715, 1747, 1750: *pugnarunt,
  et victi* (12:8), *homine nati* (14:14), *phialas Dei saevitiae* (16:1), *augustus* (16:5), *mandatum est, ut …
  induatur* (19:8), *animos … Ii* (20:4), *quia* (20:6), *dies ac noctes* (12:10, 20:10), *divicolas*, *divicolae*
  (21:8, 22:15), *ibi* (21:25), *pareat* (22:7), *nocere pergat … sanctus esse pergat* (22:11), *facto* (22:12),
  *favor* (22:21), and slips of its own (*captibus*, *delecti*, *corrurerunt*, *instaque*, *oranta*, *Praetera*,
  *quid*, a lost *ad*, *seminis* for *feminis*, *messaque terrae*, *morderent*, a clause lost at 21:21). **1556 stands
  with 1573** almost everywhere it can be read, but has the early reading at 16:5, 19:8, 20:4, 21:9 and 21:24
  (section 5): those are 1573 changes.
- **Versification** (decision 5): no edits file for 12–22. 1573 prints every verse number. It agrees with the KJV and
  against the draft at **19:6–7** (*regnum enim adeptus est Dominus Deus omnipotens* closes 6) and **21:10–11**
  (*divina gloria praeditam* opens 11): the words are moved (section 2c). It numbers against the KJV at 17:9–10, 20:9–10,
  21:20–21 and 22:3–4; there the KJV's numbers are kept (section 4).
- **Collation** (`python -m pipeline collate Rev 1-22`; `data/calibration/Rev1-22-collation.tsv`, chapters 12–22 only:
  398 places: 78 *correct*, 18 *others-1573-agrees*, 18 *others*, 272 *base-only* (182 reading, 48 division, 27 f/s,
  6 spelling, 9 edge), 12 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/Rev.12.*` to `Rev.22.*`, 66): every reading where 1573 and another printing agree against
  Wikisource, every base-only reading whose 1573 words are Latin (12:5 *estad*, 14:8 *ſuo*, 14:10 *fuum*, 14:12
  *Iefus*, 14:14 *corona*, 16:19 *lænæ*, 18:12 *contecta*, 18:21 *facietur*, 19:8 *vestiri*, 19:11 *iustes*, 19:15
  *quas*, 20:12 *apertis … est*, 21:21 *vnionibus singulæ*, 22:12 *merito*), the edge places (13:11 *ut draco*, 15:5
  *in caelo*, 17:3 *cornua*, 20:2 *annos*, 20:7 *carcere*, 20:10 *perennitatem*, 21:4 *abierint*, 22:13 *ultimus*:
  lines or words the OCR lost, all printed) and the uncovered verses (below). The *correct* places are otherwise
  spellings (*extitit*, *ascendentem*, *afflatu*, *belua*, *sardonyx*, *chalcedon*, *thus*, *lachrymam*, …). The rest
  of the base-only readings are 1573's OCR (*draconen*, *nari bestian*, *aureın*, *euin*, *carnen*, *milha*,
  *fuimus*, *nihi*, *Iinmitte*, *netendi*, *margaritatum*, *marinore*, *geminisque*, *diadeinata*, *duuium*,
  *laspide*), word breaks at line ends (*Dra co*, *cor nua*, *ceci dit*, *Do mine*, *iumen ta*, *glo ria*, *tor
  cular*, *gen tium*), words run together (*mulieramicta*, *funtalæ*, *Hiceſtacumen*, *Eiusautem*, *Sedignauos*,
  *igniardet*, *eruntcanes*, *sumataquam*, *admonſtrandum*), the f/s confusions (*folium*, *fuam*, *ferui*, *fi*),
  note letters, margin notes run into the text (12:14 *Dan*, 16:2 *Primus angelus*, 19:10 *Non vult adorari se*, 20:2
  *mille annos*, 20:9 *a tanto militum numero …*) and the references (*Hier*, *Supr*, *Ezech*, *Phil*, *Gal*, *Efa*).
  Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758,
  1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 942–948), not only the collation's places: it
  found 14:4 *feminis* (below), the two verse boundaries, 12:10 *et noctes* (an uncovered verse) and 21:21's lost
  clause; nothing further.
- **The twelve uncovered verses** were read whole on the image: 12:4 (crop `Rev.12.4-cauda`), 12:10–12
  (`Rev.12.10-12`), 14:2 (`Rev.14.2-audivi`, `Rev.14.2-citharoedorum`), 15:1 (`Rev.15.1-mirabile`), 16:16–18
  (`Rev.16.10-manderent`, `Rev.16.16-18`, `Rev.16.18-terraemotus`), 17:13 (`Rev.17.13-eundem`), 21:1
  (`Rev.21.1-novum`), 22:11 (`Rev.22.11-12`). 12:10 (*dies & noctes*), 12:11 (*oppetierint*) and 22:11 (*nocentior
  fiat … ſanctior fiat*) differ from the draft (sections 1 and 2); the others only in spelling (*Ii eundem*,
  *extiteruntq;*, *terræmotus*, *extiterit*).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fumus/sumus*, *fano/sano*,
  *fuit/suit*, *fugit/sugit*, *falsus/salsus*, *fidentes/sidentes*, *fontes/sontes*, *futura/sutura*, *ferens*,
  *finis*, *folia*) was read in its verse: all are *f* by sense. Every *s* word whose *f*-form is Latin (*si*, *sitis*,
  *solium/folium*, *suam*, *sui*, *servi*, *sors/fors*, *sortem/fortem*, *sumat*, *secunda*, *sellas*, *insulae*,
  *seminis*): all are *s* by sense but **14:4** *qui cum seminis non sunt polluti*, where 1573 prints *fœminis*
  (section 2a); 12:17 *reliquis ejus seminis* is *ſeminis* in 1573 and right. 1573's OCR *folium*, *fuam*, *ferui*,
  *fi*, *fortem* are long s on the page.
- **In all, 38 corrections**: 13 Wikisource slips (section 1), 21 readings of Castellio's revised text (section 2), 1
  found by the f/s sweep (section 2a), 2 verse boundaries (section 2c), 1 word division (section 3). Spellings
  (*quum*, *quemdam*, *eumdem*, *adflatu*, *adloquens*, *adstabunt*, *exstitit*, *bellua*, *sardonix*, *calcedon*,
  *tus*, *lacrimam*, *paullulum*, *aluo*, *vuas*, …) are left to stage 3; rules proposed for the forms without a row
  (section 6). Five places where 1556 reads against 1573 are recorded (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (13)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Revelation 12:3** *et in captibus diademata* → *capitibus*. 1573 *& in capitibus diademata ſeptem,* (canvas 943, crop `Rev.12.3-capitibus`); 1556 (OCR *ín capitibus*), 1758, 1681, 1715, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `Rev.12.3` la: `et in captibus diademata` → `et in capitibus diademata`
2. **Revelation 12:5** *qui ejus filius raptus est Deum* → *raptus est ad Deum*. 1573 *qui eius filius raptus eſt ad / Deum, eiusq; ſolium.* (canvas 943, `Rev.12.5-ad`; the OCR's *estad*), ἡρπάσθη … πρὸς τὸν θεὸν; 1556 (OCR *raptus eft ad Deum*), 1758, 1681, 1715, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `Rev.12.5` la: `filius raptus est Deum` → `filius raptus est ad Deum`
3. **Revelation 12:9** *ejusque angeli delecti sunt* → *dejecti*. 1573 *angeli deiecti ſunt.* (canvas 943, `Rev.12.9-dejecti`), as *dejectus est* twice before it; 1556 (OCR *deíecii*), 1758, 1681, 1747, 1750. Wikisource alone.
   **Apply:** `Rev.12.9` la: `ejusque angeli delecti sunt` → `ejusque angeli dejecti sunt`
4. **Revelation 12:11** *ut mortem oppetierunt* → *oppetierint*. 1573 *vt / mortem oppetierint.* (canvas 943, `Rev.12.10-12`; an uncovered verse), the subjunctive after *usque adeo … ut*; 1556 (OCR *oppetíe^ríat*), 1758, 1750, 1726. Wikisource alone.
   **Apply:** `Rev.12.11` la: `ut mortem oppetierunt.` → `ut mortem oppetierint.`
5. **Revelation 14:16** *falcem suam in terram, messaque terrae est* → *messaque terra est*. 1573 *terram, meſſaq; terra eſt.* (canvas 944, `Rev.14.16-terra`), ἐθερίσθη ἡ γῆ; 1556 (OCR *meffatp terra eft*), 1758, 1681, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `Rev.14.16` la: `messaque terrae est.` → `messaque terra est.`
6. **Revelation 16:7** *vera instaque sunt tua judicia* → *justaque*. 1573 *vera iuſtaq; ſunt tua iudicia.* (canvas 944, `Rev.16.7-justaque`); 1556 (OCR *íuftagp*), 1758, 1750. Wikisource alone.
   **Apply:** `Rev.16.7` la: `vera instaque sunt` → `vera justaque sunt`
7. **Revelation 16:10** *ut ipsi suas prae dolore linguas morderent* → *manderent*. 1573 *ipſi ſuas præ dolore linguas manderent,* (canvas 944, `Rev.16.10-manderent`), ἐμασῶντο; 1556 (OCR *máderent*), 1758, 1681, 1715, 1747, 1750. Wikisource alone.
   **Apply:** `Rev.16.10` la: `linguas morderent,` → `linguas manderent,`
8. **Revelation 16:19** *gentium urbes corrurerunt* → *corruerunt*. 1573 *gen-/tium vrbes corruerunt:* (canvas 945, `Rev.16.19-corruerunt`); 1556 (OCR *cortuerunt*), 1758, 1715, 1747, 1750. Wikisource alone.
   **Apply:** `Rev.16.19` la: `urbes corrurerunt:` → `urbes corruerunt:`
9. **Revelation 17:14** *Ii eum agno bellum gerent* → *cum agno*. 1573 *Ii cum agno bellum gerent,* (canvas 945, `Rev.17.14-cum`); 1556 (OCR *lí cum agno*), 1758, 1681, 1750. Wikisource alone.
   **Apply:** `Rev.17.14` la: `Ii eum agno` → `Ii cum agno`
10. **Revelation 19:17** *Praetera vidi alium angelum* → *Praeterea*. 1573 *Præterea vidi alium angelum* (canvas 946, `Rev.19.17-Praeterea`); 1556 (OCR *Pratere ea*), 1758, 1681. Wikisource alone.
    **Apply:** `Rev.19.17` la: `Praetera vidi` → `Praeterea vidi`
11. **Revelation 21:3** *tabernaculum, quid apud eos habitabit* → *qui*. 1573 *tabernaculum, qui apud eos ha-/bitabit,* (canvas 947, `Rev.21.3-5`); 1556 (OCR *quiapud eos*), 1758, 1715, 1747, 1750, 1726. Wikisource alone.
    **Apply:** `Rev.21.3` la: `tabernaculum, quid apud eos` → `tabernaculum, qui apud eos`
12. **Revelation 21:19** *fundamenta omnibus oranta gemmis* → *ornata*. 1573 *fundamenta omnibus ornata gem-/mis.* (canvas 947, `Rev.21.19-ornata`); 1556 (OCR *ornatagemmís*), 1758, 1747, 1750, 1726. Wikisource alone.
    **Apply:** `Rev.21.19` la: `omnibus oranta gemmis` → `omnibus ornata gemmis`
13. **Revelation 21:21** *duodecim erant uniones, ex singulis constantes* → *ex singulis unionibus singulae constantes*. 1573 *duodecim erant vniones, ex ſingulis vnionibus ſin-/gulæ conſtantes.* (canvas 947, `Rev.21.20-21`), ἀνὰ εἷς ἕκαστος τῶν πυλώνων ἦν ἐξ ἑνὸς μαργαρίτου; 1556 (OCR *ex lingulís unionibus fingu" Iz conflantes*), 1758, 1747, 1750. Wikisource alone: it lost *unionibus singulae*, leaving the sentence without sense.
    **Apply:** `Rev.21.21` la: `ex singulis constantes.` → `ex singulis unionibus singulae constantes.`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (21)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
Wikisource's reading at five of these places (section 5): there 1573 is a later revision, and the draft follows it.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Revelation 12:8** *Et draco ejusque angeli pugnarunt, et victi sunt* → *pugnantes victi sunt*. 1573 *& draco eiusq; angeli pugnantes victi ſunt,* (canvas 943, `Rev.12.8-pugnantes`); 1556 (OCR *pugnátes uícti*), 1758, 1726. The early line *pugnarunt, et victi* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Rev.12.8` la: `angeli pugnarunt, et victi sunt` → `angeli pugnantes victi sunt`
2. **Revelation 12:10** *apud Deum nostrum dies ac noctes accusabat* → *dies et noctes*. 1573 *apud Deum no-/ſtrum dies & noctes accuſabat.* (canvas 943, `Rev.12.10-12`; an uncovered verse); 1556 (OCR *dies& no.tés*), 1758. The early line *dies ac noctes* (Wikisource, 1715, 1750). As 20:10 (item 11).
   **Apply:** `Rev.12.10` la: `dies ac noctes accusabat` → `dies et noctes accusabat`
3. **Revelation 12:14** *ut solitudinem in locum suum avolaret* → *ut in solitudinem*. 1573 *vt in ſolitudinem in locum ſuum auolaret,* (canvas 943, `Rev.12.14-in`), εἰς τὴν ἔρημον εἰς τὸν τόπον αὐτῆς; 1758, 1681, 1726. Wikisource and 1750 without *in* (1556's OCR *ut fa folítudinem* unclear; 1715 and 1747 not reached).
   **Apply:** `Rev.12.14` la: `ut solitudinem in locum` → `ut in solitudinem in locum`
4. **Revelation 14:14** *nubi insidentem quemdam homine nati similem* → *filio hominis similem*. 1573 *quendam filio hominis ſimilem,* (canvas 944, `Rev.14.14-filio`; *filio hominis* in italics), ὅμοιον υἱῷ ἀνθρώπου; 1556 (OCR *quendam filio homínis*), 1758, 1726. The early line *homine nati* (Wikisource, 1747, 1750). *quemdam/quendam* is stage 3's.
   **Apply:** `Rev.14.14` la: `quemdam homine nati similem` → `quemdam filio hominis similem`
5. **Revelation 16:1** *effundite phialas Dei saevitiae in terram* → *phialas saevitiae Dei*. 1573 *Ite, effundite phialas ſæuitiæ / Dei in terram.* (canvas 944, `Rev.16.1-saevitiae`); 1556 (OCR *phíalss … uitize Dei in terrà*), 1758. The early order *Dei saevitiae* (Wikisource, 1681, 1715, 1747, 1750).
   **Apply:** `Rev.16.1` la: `phialas Dei saevitiae in terram` → `phialas saevitiae Dei in terram`
6. **Revelation 16:5** *quique augustus es* → *quique sanctus es*. 1573 *qui es, quiq; fuiſti, quiq; ſanctus es,* (canvas 944, `Rev.16.5-sanctus`), ὁ ὅσιος; 1758, 1681, 1726. **1556** *auguſtus* (OCR *quidp auguftus es*), with Wikisource, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Rev.16.5` la: `quique augustus es` → `quique sanctus es`
7. **Revelation 19:8** *Eique mandatum est, ut byssino puro splendidoque induatur* → *Eique datum est byssino puro splendidoque vestiri*. 1573 *eiq; datum eſt byſsino puro ſplendidoq; veſtiri.* (canvas 946, `Rev.19.8-datum`); 1758, 1726. 1681, 1750 *datum est, ut … induatur*; **1556** *mandatum eſt ut … induatur* (OCR *mádatum eflutbyfsino puro fplendídoG induatur*), with Wikisource, 1715, 1747: a 1573 change (section 5).
   **Apply:** `Rev.19.8` la: `Eique mandatum est, ut byssino puro splendidoque induatur.` → `Eique datum est byssino puro splendidoque vestiri.`
8. **Revelation 19:15** *quo gentes feriat, quos ipse ferreo baculo reget* → *quas*. 1573 *quo gentes fe-/riat, quas ipſe ferreo baculo reget:* (canvas 946, `Rev.19.15-quas`), agreeing with *gentes*; 1556 (OCR *genresferíat quas*), 1758, 1681. Wikisource and 1750 *quos*.
   **Apply:** `Rev.19.15` la: `quo gentes feriat, quos ipse` → `quo gentes feriat, quas ipse`
9. **Revelation 20:4** *vidi animos decollatorum … Ii revixerunt* → *animas … Eae revixerunt*. 1573 *itemq; vidi animas decollatorum … manum accepe-/runt, eæ reuixerunt,* (canvas 946, `Rev.20.4-animas`), τὰς ψυχὰς … καὶ ἔζησαν; 1758, 1726 (OCR *animas … ee*), 1681 (*animas*). **1556** *animos … Ii* (OCR *uídíantmos … lireuixerunt*), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5). The full stop and the capital are the draft's; stage 3's.
   **Apply:** `Rev.20.4` la: `vidi animos decollatorum` → `vidi animas decollatorum`
   **Apply:** `Rev.20.4` la: `acceperunt. Ii revixerunt` → `acceperunt. Eae revixerunt`
10. **Revelation 20:6** *potestatem non habet, quia erunt Dei et Christi sacerdotes* → *quin*. 1573 *poteſtatem non / habet, quin erunt Dei & Chriſti ſacerdotes,* (canvas 947, `Rev.20.6-quin`), ἀλλ᾽ ἔσονται; 1556 (OCR *quín erunt*), 1758, 1726. The early line *quia* (Wikisource, 1681, 1747, 1750).
    **Apply:** `Rev.20.6` la: `non habet, quia erunt` → `non habet, quin erunt`
11. **Revelation 20:10** *cruciabunturque dies ac noctes* → *dies et noctes*. 1573 *cruciabuntúrque dies & noctes in omnem per-/ennitatem.* (canvas 947, `Rev.20.7-10`, `Rev.20.10-perennitatem+next`); 1556 (OCR *díes& noctes*), 1758, 1681. The early line *ac* (Wikisource, 1747, 1750). As 12:10 (item 2).
    **Apply:** `Rev.20.10` la: `dies ac noctes in omnem` → `dies et noctes in omnem`
12. **Revelation 20:12** *et alius liber apertus, qui est vitae liber* → *liber apertus est, qui*. 1573 *& alius liber a-/pertus eſt, qui eſt vitæ liber,* (canvas 947, `Rev.20.12-est`); 1556 (OCR *aliusliber apertus efl.qui eft*), 1758, 1681, 1726. The early line without *est* (Wikisource, 1715, 1747, 1750).
    **Apply:** `Rev.20.12` la: `alius liber apertus, qui est` → `alius liber apertus est, qui est`
13. **Revelation 21:8** *et veneficos, et divicolas* → *deastricolas*. 1573 *& veneficos, & deaſtricolas, & o-/mnes mendaces,* (canvas 947, `Rev.21.8-deastricolas`), εἰδωλολάτραις; 1556 (OCR *deaflricolas*), 1758, 1681, 1726. The early line *divicolas* (Wikisource, 1747, 1750). As 22:15 (item 20).
    **Apply:** `Rev.21.8` la: `veneficos, et divicolas,` → `veneficos, et deastricolas,`
14. **Revelation 21:9** *septem postremarum cladium plenas* → *cladum*. 1573 *ſeptem poſtremarum cla-/dum plenas,* (canvas 947, `Rev.21.9-cladum`); 1758, 1681, 1726. **1556** *cladium* (OCR *poltremarum cladium plenas*), with Wikisource, 1715, 1747, 1750 (section 5). Both are genitive plurals of *clādēs* (Gaffiot; the lexicon knows *clādum* from Morpheus only). For your eye: a form, not a word; if you would rather keep *cladium*, reject this item alone.
    **Apply:** `Rev.21.9` la: `postremarum cladium plenas` → `postremarum cladum plenas`
15. **Revelation 21:24** *conferent terrarum reges suam gloriam ac honorem* → *gloriam suam*. 1573 *conferent terrarum reges glo-/riam ſuam ac honorem:* (canvas 947, `Rev.21.24-gloriam`); 1758, 1726. **1556** *ſuam gloriam* (OCR *uam gloríam*), with Wikisource, 1747, 1750 (section 5).
    **Apply:** `Rev.21.24` la: `reges suam gloriam ac honorem` → `reges gloriam suam ac honorem`
16. **Revelation 21:25** *nam nox quidem ibi nulla erit* → *illic*. 1573 *( nam nox / quidem illic nulla erit )* (canvas 947, `Rev.21.25-illic`); 1556 (OCR *quidem illícnulla erít*), 1758, 1726. The early line *ibi* (Wikisource, 1747, 1750).
    **Apply:** `Rev.21.25` la: `nox quidem ibi nulla` → `nox quidem illic nulla`
17. **Revelation 22:7** *felix, qui verbis pareat oraculi* → *paret*. 1573 *Felix qui verbis paret / oraculi huius libri.* (canvas 948, `Rev.22.7-paret`), ὁ τηρῶν; 1556 (OCR *uerbísparet*), 1758, 1681. The early line *pareat* (Wikisource, 1747, 1750).
    **Apply:** `Rev.22.7` la: `qui verbis pareat oraculi` → `qui verbis paret oraculi`
18. **Revelation 22:11** *Qui nocet, nocere pergat: et qui sordet, sordere pergat: et justus, justus esse pergat: et sanctus, sanctus esse pergat* → *nocentior fiat … sordidior fiat … justior fiat … sanctior fiat*. 1573 *Qui nocet, nocentior fiat: & qui ſordet, ſordidior / fiat: & iuſtus iuſtior fiat: & ſanctus ſanctior fiat.* (canvas 948, `Rev.22.11-12`; an uncovered verse), ἀδικησάτω ἔτι … ῥυπαρευθήτω ἔτι … ἁγιασθήτω ἔτι; 1556 (OCR *nocentior fat:& quílordet, fordidíor fiat?&iuftus iuflior fíat:& fanctus fanctior fiat*), 1758, 1726 (OCR *fordiaior fiate*). The early line *nocere pergat …* (Wikisource, 1747, 1750). 1573 has no comma after *iustus*, *sanctus*.
    **Apply:** `Rev.22.11` la: `nocere pergat: et qui sordet, sordere pergat: et justus, justus esse pergat: et sanctus, sanctus esse pergat.` → `nocentior fiat: et qui sordet, sordidior fiat: et justus justior fiat: et sanctus sanctior fiat.`
19. **Revelation 22:12** *ut pro suo quemque facto remunerer* → *merito*. 1573 *vt pro ſuo quemque merito re-/munerer.* (canvas 948, `Rev.22.11-12`); 1556 (OCR *utpro fuo queind) meríto remue rnerer*), 1758, 1681 (OCR *rito remuncrer*), 1726. The early line *facto* (Wikisource, 1747, 1750).
    **Apply:** `Rev.22.12` la: `quemque facto remunerer` → `quemque merito remunerer`
20. **Revelation 22:15** *et homicidae, et divicolae* → *deastricolae*. 1573 *& homicidæ, & deaſtricolæ, & quiſquis* (canvas 948, `Rev.22.13-15`); 1556 (OCR *deaftrícolze*), 1758, 1681, 1726. The early line *divicolae* (Wikisource, 1715, 1747, 1750).
    **Apply:** `Rev.22.15` la: `homicidae, et divicolae, et` → `homicidae, et deastricolae, et`
21. **Revelation 22:21** *Domini nostri Jesu Christi favor adsit* → *gratia*. 1573 *Domini noſtri Ieſu Chriſti gratia adſit vobis o-/mnibus: Amen.* (canvas 948, `Rev.22.21-end`); 1556 (OCR *Chrifti gratia adfit*), 1758, 1726. The early line *favor* (Wikisource, 1715, 1747, 1750).
    **Apply:** `Rev.22.21` la: `Christi favor adsit` → `Christi gratia adsit`

## 2a. Found by the f/s sweep (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **Revelation 14:4** *Hi sunt, qui cum seminis non sunt polluti* → *cum feminis*. 1573 *Hi ſunt qui cum fœminis non ſunt polluti:* (canvas 943, `Rev.14.2-audivi`, its last line), μετὰ γυναικῶν; 1556 (OCR *cum femínis*), 1758 (*foeminis*), 1715, 1747, 1750. Wikisource alone, a long s for an f. *fœminis* → *feminis* (Gaffiot *fēmina*) is stage 3's.
   **Apply:** `Rev.14.4` la: `qui cum seminis non` → `qui cum feminis non`

## 2b. Found where 1573 was not aligned (0)

The twelve uncovered verses were read whole on the image (intro): 12:10 *dies & noctes*, 12:11 *oppetierint* and 22:11
*nocentior fiat …* are section 2's item 2, section 1's item 4 and section 2's item 18; the others differ only in
spelling. No further decision needed.

## 2c. Verse boundaries (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **Revelation 19:6–7**: *Regnum enim adeptus est Dominus Deus omnipotens* closes 6. 1573 *qui dicebant: Halleluia, regnum e-/nim adeptus eſt Dominus Deus omnipotens. / 7 Gaudeamus & exultemus,* (canvas 946, crop `Rev.19.6-7`); 1681, 1715, 1726 number 7 at *Gaudeamus* too (OCR); the KJV (*saying, Alleluia: for the Lord God omnipotent reigneth. 7 Let us be glad*) and the Greek (ὅτι ἐβασίλευσεν in 6) agree. Wikisource and 1750 begin 7 at *Regnum*. The capital *Regnum* and the stop after *Halleluja* are left to stage 3.
   **Apply:** `Rev.19.6` la: `qui dicebant: Halleluja.` → `qui dicebant: Halleluja. Regnum enim adeptus est Dominus Deus omnipotens.`
   **Apply:** `Rev.19.7` la: `Regnum enim adeptus est Dominus Deus omnipotens. Gaudeamus` → `Gaudeamus`
2. **Revelation 21:10–11**: *divina gloria praeditam* opens 11. 1573 *de cœlo à Deo deſcen-/dentem, / 11 diuina gloria pręditam. Eius luminare ſimile erat* (canvas 947, `Rev.21.10-11`); 1758, 1681, 1715, 1747 number 11 at *Divina* too (OCR); the KJV (*descending out of heaven from God, 11 Having the glory of God*) and the Greek (ἔχουσαν τὴν δόξαν in 11) agree. Wikisource and 1750 keep it in 10. The capital is stage 3's.
   **Apply:** `Rev.21.10` la: `descendentem, divina gloria praeditam.` → `descendentem,`
   **Apply:** `Rev.21.11` la: `Ejus luminare simile` → `divina gloria praeditam. Ejus luminare simile`

## 3. Word division (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **Revelation 17:8** *Bellua, quamvidisti, fuit* → *quam vidisti*. A missing space; 1573 *Belua, quam vidiſti, fuit,* (canvas 945), 1556 (OCR *Belua, quam uidifti*), 1758, 1747, 1750, 1726.
   **Apply:** `Rev.17.8` la: `Bellua, quamvidisti, fuit` → `Bellua, quam vidisti, fuit`

## 4. Checked and kept

- **Verse numbers kept at the KJV's** where 1573 numbers otherwise (decision 5; the KJV disagrees with 1573, so nothing
  moves): **17:9–10** 1573 ends 9 with *ſe-/ptemq; reges ſunt,* and begins *10 quorũ quinq; ceciderunt* (canvas 945,
  `Rev.17.9-septemque`; 1681, 1726 the same, OCR *10 Quorum*, *16 Quorum*), the KJV *10 And there are seven kings*; **20:9–10** 1573 begins
  *10 Sed eos delapſus à Deo ignis de cœlo, confecit:* (canvas 947, `Rev.20.7-10`), the KJV ends 9 with *and fire came
  down from God out of heaven, and devoured them*; **21:20–21** 1573 begins *21 duodecimum amethyſtus.* (canvas 947,
  `Rev.21.20-21`), the KJV ends 20 with *the twelfth, an amethyst*; **22:3–4** 1573 ends 3 with *& eius faciem /
  videbunt,* and begins *4 & eius nomen geſtabunt* (canvases 947–948, `Rev.22.3-4`, `Rev.22.4-nomen`), the KJV *4 And
  they shall see his face*. For your eye, if you would rather follow 1573's numbering here.
- **18:21** *tali impetu jacietur Babylon*: 1573 *Tali im-/petu ſacietur Babylon* (canvas 946, `Rev.18.21-jacietur`,
  enlarged `Rev.18.21-jacietur-zoom`: a long s, no crossbar), not a Latin word: a misprint for *iacietur*, which 1556
  (OCR *iae…cíct*), 1758, 1681, 1715, 1747, 1750, 1726 and Wikisource read (βληθήσεται). Kept.
- **Words the OCR misread, right on the page**: 12:5 *ad* (*eſtad*, section 1), 13:16 *Atque eo adigebat* (*Atque eò
  adigebat*, `Rev.13.16-eo`), 14:8 *saevo* (*ſæuo*, `Rev.14.8-saevo`), 14:10 *saevum* (*ſæuum*, `Rev.14.10-saevum`),
  14:12 *Jesuque* (*Ieſuq;*, `Rev.14.12-Jesuque`), 14:14 *coronam* (*coronã*, `Rev.14.14-filio`), 16:19 *saevae*
  (*ſæuæ*, `Rev.16.19-saevae`), 18:12 *confecta* (*confecta*, `Rev.18.12-confecta`), 19:11 *justeque* (*iuſteq;*,
  `Rev.19.11-justeque`), 20:12 *apertique* (*apertiq;*), 21:6 and 22:13 *α et ω* (Greek letters in 1573, `Rev.21.6-alpha`,
  `Rev.22.13-15`; the OCR's *a & a*). Agree.
- **Lines and words the OCR lost, printed**: 13:11 *ut draco* (`Rev.13.11-draco`), 14:2 *audivi citharoedorum*
  (`Rev.14.2-citharoedorum`), 15:5 *in caelo* (`Rev.15.5-caelo`), 17:3 *cornua* (`Rev.17.3-cornua`), 20:2 *annos*
  (`Rev.20.2-annos`), 20:7 *carcere*, 20:10 *perennitatem* (`Rev.20.7-10`, `Rev.20.10-perennitatem+next`), 21:3 *apud
  eos Deus eorum*, 21:4 *abierint* (`Rev.21.3-5`), 22:12 *remunerer*, 22:13 *ultimus* (`Rev.22.11-12`,
  `Rev.22.13-15`). Agree.
- **16:18** *terrae motus* (twice): 1573 *terræmotus*, one word (`Rev.16.18-terraemotus`); your settled *terræ
  mōtus*, *terræ mōtū*, *terræ mōtūs*. Kept. **17:14** *nec non*: 1573 *necnō*, 1556, 1758, 1681 *necnon*; spacing,
  kept. **12:17** *reliquis ejus seminis*: 1573 *ſeminis*, right (the f/s sweep).
- **Note letters and margin notes**, not text: 16:16 *a* (*mons eximius*), 18:13 *a … ſcilicet*, 20:9 *a* (*a tanto
  militum numero, vt terram omnem occuparent*), 21:4 *a* (*ſuperior rerum ſtatus*); the summaries in the margin
  (16:2 *Primus angelus ſuam phialam effundit*, 16:3 *Secundus*, 16:10 *Quintus*, 16:12 *Sextus*, 16:17 *Septimus*,
  17:8 *Meretricis interpretatio*, 19:10 *Non vult adorari ſe*, 20:2 *Satanas mille annos vinctus*, 20:8 *Gog &
  Magog*, 21:1 *Nouum cœlum*, 21:10 *Sancta Hieroſolyma*, 14:1 *Agnus ſtans in Sione*, 14:16 *Metitur terræ ſeges*);
  the references (as the OCR reads them: 12:14 *Dan.7.20*, 14:18 *loel . 3.23*, *Mar.13.39*, 16:15 *Suprà 3.3*,
  *Mat.24-44*, *Luce 12.39*, 17:14 *Infr.19.10*, 18:2 *Hier . 15. 2*, *Supr.14.8*, 18:10 *Hier.st.t.*, 19:4
  *Sup.9.14*, 19:12 *Apoc.1.2*, 19:14 *Efa . 36.1*, 19:15 *P / al.2 . 15*, 19:17 *Supr.17.14*, 20:8 *Exech.38.14*,
  20:12 *Supr.3*, *Infr.21.22*, *Phil.4.3*, 21:2–3 *Efa . 66.17*, *2.Pet.3.13*, *Ezech . 43-4*, 21:23 *f / 2.66.19*,
  21:26–27 *Efa.66.198*, *Phil.4.3*, *Supr.3.5*, 22:9 *Supr.19.10*, *Alt . 10.26*, 22:13–15 *Efa.41.6*, *Supr . 1. 8*,
  *1.Cor.6.7*, *Gal.5.10*); the chapter summaries;
  the running heads (*APOCALYPSIS*); the closing note and errata (intro).
- **Punctuation and capitals, left to stage 3**: 13:14 *ostentis, quae ei in bestiae conspectu facere datum erat,*
  (1573 in parentheses), 19:2 *meretricem, quae terram impudicitia sua corrumpebat,* (1573 in parentheses), 16:15 *ut
  fur Felix* (1573 *vt fur. Felix*), 19:6 *Halleluja.* (1573 *Halleluia, regnum*), 12:10 *in caelo* (1573 *In cœlo*),
  21:5 *vera fidaque* (1573 *vera, fidaq;*), 22:6 *dicta;* (1573 *dicta:*), 18:12 *lignum, thyinum* (1573 no comma),
  12:4 *Cujus* and the other verse openings the draft capitalizes after a comma (1573 *cuius*, *vt*, *& …*), 21:3
  *erunt:* (1573 a comma), 16:17 *ex solio dicens* (1573 *ex ſolio, dicens*).
- **Spellings, left to stage 3** (decisions 37 and 42's rules, and section 6): *quum* (1573 *cùm*, *cum*),
  *quemdam*, *eumdem* (1573 *quendam*, *eundem*), *adscendentem*, *adscensura*, *adflatu*, *adfecti*, *adlocutus*,
  *adloquens*, *adficiamini*, *Adficite*, *adfecit*, *adficiar*, *adstabunt*, *adstiterunt*, *adstantes*, *adspexi*,
  *adspexissemque* (1573 *a-*, *af-*, *al-*), *exstitit*, *exstinctum*, *exstiterunt*, *exstabit*, *exsequantur*,
  *exsecrabiles*, *exsultemus* (1573 *ext-*, *exe-*, *exul-*), *bellua*, *belluae*, *belluam* (1573 *belua*),
  *paullulum* (1573 *paululum*), *quicumque*, *quocumque* (1573 *-cunque*), *submergeret* (1573 *ſummergeret*),
  *taetro* (1573 *tetro*), *tus* (1573, 1556, 1758 *thus*; Gaffiot heads *tūs*), *lacrimam* (1573 *lachrymam*),
  *sardonix* (1573 *ſardonyx*), *calcedon* (1573 *chalcedon*), *aluo* (12:2), *vuas* (14:19), *Michaël*,
  *israëliticarum*, *aërem*, *Joannes* (1573 *Iohannes*), *Halleluja*, *quatuor*, *sexcenti*, *obedirent*, *Jesu*,
  *caelo* (1573 *cœlo*).

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282458–63), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Revelation 16:5 | *quique sanctus es* | = | *quiq; auguſtus es* (OCR *quidp auguftus es*) | Wikisource, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| Revelation 19:8 | *Eique datum est byssino puro splendidoque vestiri* | = | *eiq; mandatum eſt ut byſsino puro ſplendidoq; induatur* (OCR *mádatum eflutbyfsino puro fplendídoG induatur*) | Wikisource, 1715, 1747 with 1556; 1681, 1750 *datum est, ut … induatur*; 1758, 1726 with 1573 |
| Revelation 20:4 | *vidi animas … eae revixerunt* | = | *animos … Ii reuixerunt* (OCR *uídíantmos … lireuixerunt*) | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1726 (1681 *animas*) with 1573 |
| Revelation 21:9 | *postremarum cladum* | = | *poſtremarum cladium* (OCR *poltremarum cladium*) | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| Revelation 21:24 | *gloriam suam ac honorem* | = | *ſuam gloriam ac honorem* (OCR *uam gloríam achonorem*) | Wikisource, 1747, 1750 with 1556; 1758, 1726 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12)

## 6. Spelling rules proposed

These forms have no row in `data/rules/orthography.tsv` (checked with `normalize.propose()` on the draft). Proposed,
not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| bellua | belua | word | 17:8, 17:12, 17:16, 19:20, 20:10 | 1573 *belua* (canvases 945–947), 1556, 1758; Gaffiot *bēlŭa* (`latin macron`: *bellua* known only as a variant) |
| belluae | beluae | word | 17:3, 17:7, 17:13, 17:17 | as *bellua*; 1573 *beluæ* |
| belluam | beluam | word | 17:8, 19:19 | as *bellua*; 1573 *beluam* |
| sardonix | sardonyx | word | 21:20 | 1573 *ſardonyx* (`Rev.21.20-21`), 1556 (OCR *fardonyx*), 1758; Gaffiot *sardŏnyx* |
| calcedon | chalcedon | word | 21:19 | 1573 *chalcedon* (`Rev.21.19-ornata`), 1556 (OCR *chalcedon*), 1758, 1726; `latin macron calcedon`: no source knows it |
| adstabunt | astabunt | word | 18:15 | decision 37, as the approved *adstabat → astabat*, *adstabo → astabo*; 1573 *aſtabunt* (canvas 945) |
| adspexissemque | aspexissemque | word | 22:8 | decision 37, as the approved *adspexerunt → aspexerunt* (the phrase row *et adspexi* reaches only *adspexi*); 1573 *aſpexiſſemq;* (canvas 948) |
| aluo | alvo | word | 12:2 | u/v (decision 17's j/v orthography); 1573 *aluo* (canvas 943); your settled *alv-* |
| vuas | uvas | word | 14:19 | u/v, as *aluo*; 1573 *vuas* (canvas 944), 14:18 *uvas* in the draft itself; your settled *ūv-* |

(*tus* stays: Gaffiot heads *tūs* and lists *thūs* as the other form; *lacrimam*, *paullulum*, *quemdam*, *eumdem*,
*exst-* are covered by existing rows or decisions.)

**Decision:** accept (Claude, 2026-11-12, under decisions 17, 37, 42 and 46; to be added to `data/rules/orthography.tsv` when you apply this file)
