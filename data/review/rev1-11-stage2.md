# Revelation 1–11, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of Jude (`data/review/jude1-stage2.md`) and 1 John
(`data/review/1john1-5-stage2.md`). Chapters 12–22 are read separately.

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277). In 1573 Revelation follows Hebrews: the title,
  Castellio's annotation on the author, Athanasius's argument, the summary and 1:1–1:6 on canvas 937, 1:6–2:29 on 938
  (an annotation after chapter 1), 3:1–5:3 on 939 (an annotation after chapter 3), 5:3–7:8 on 940 (an annotation on
  5:11), 7:8–9:17 on 941 (annotations after chapter 8), 9:17–11:19 on 942, chapter 12 from 943. 1556 is the
  reference: where it reads otherwise, its reading is recorded as a variant (section 5); its e-rara OCR has
  Revelation 1–11 on pages 10282454–58 (1:1–2:20, 2:21–5:4 with the columns interleaved, 5:4–7:15, 7:15–10:7,
  10:8–11:19) and reaches nearly every verse, poorly at 1:1–3, 1:11, 10:1 and 10:4. Stage 1 drafted Wikisource's
  Revelation as **`text/draft/REV.usfm`** (BSB paragraphs). You have no earlier work on Revelation; `TXT/1 - OCR`
  (the 1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Revelation 1–11 is the early wording**, with the early-line printings 1715, 1747 and 1750: 1:4
  *favorem* (1556 and 1573 *gratiam*), 1:13 *similem homine nati* (*hominis filio*), 2:9 *et pauperiem*, 3:15 *quod
  neque*, 8:10–11 *quae … delapsa est: (Est autem …) et conversa est*; with slips of its own (*imperitum*, *ocula*,
  *tenant*, *esset*, *aeque*, *dicit*, *vinenti*, *adnimadverti*, *inveceret*, *comissum*, *Quin*, *his*,
  *conservaque*, *scorpionum*, *snut*, *regnibusque*, *revenentibus*) and two omissions (3:1 whole, 7:5's tribe of
  Gad) and a lost clause (5:11 *et decies centena millia*). **1573 departs from 1556** at 2:7 (*arbore vitae*, 1556
  *vitali*), 2:10 (*coronam vitae*, 1556 *vitae coronam*), 2:13 (*etiam iis temporibus, quibus Antipas*, 1556
  *meisque temporibus Antipas*) and 11:19 (*arca foederis in ejus templo*, 1556 *foederis ejus*): the text follows
  1573, 1556 is recorded (section 5). 1758 follows 1573 wherever its OCR reaches these places, 1681 and 1726 at
  most of them.
- **Rev 3:1 was missing in Wikisource** (its chapter 3 began at verse 2). It was inserted into the draft from 1573
  before renumbering (section 1, item 1).
- **Versification** (decision 5): the draft is at the KJV counts (chapters 1–11: 20, 29, 22, 11, 14, 17, 17, 13, 21,
  11, 19 verses). 1573 prints every verse number and agrees with the draft but in chapter 10: 1573 (canvas 942) and
  Wikisource number 10 verses, the KJV's 10:2 inside their 10:1. `data/versification/Rev.draft.edits.tsv` split their
  10:1 at *Habebat autem* (applied 2026-11-12), so the draft's 10:1–2 are 1573's 10:1 and its 10:3–11 are 1573's 2–10; two boundaries inside the
  chapter still differ from 1573 and the KJV (section 4). No other verse boundary differs in chapters 1–11.
- **Collation** (`python -m pipeline collate Rev 1-22`; `data/calibration/Rev1-22-collation.tsv`, chapters 1–11: 411
  places: 82 *correct*, 21 *others-1573-agrees*, 14 *others*, 292 *base-only* (178 reading, 57 division, 39 f/s, 10
  spelling, 8 edge), 2 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/Rev.1.*`–`Rev.11.*`, 60): every reading where 1573 and another printing agree against
  Wikisource, the *others* places (8:8 *conuersaque*, 8:10 *qua*, 8:11 *Est*, 10:1 *de cœlo*, 10:11 *regibusque*,
  11:18 *reuerentibus*), the base-only places whose 1573 words are Latin (1:4 *gratiam*, 1:13 *hominis filio*, 2:10
  *coronam vitæ*, 2:18 *cuius*, 3:10 *euentura*, 4:8 *habebat … erat*, 8:10 *qua … delapſa*, 11:18 *iudicetur*,
  11:19 *fœderis in eius*), the edges (1:3 *inſtat*, 9:19 *quibus nocerent* at the head of canvas 942, 10:3 *voces*,
  10:5 *videram*: printed, lost by the OCR) and the uncovered verses. The rest of the base-only readings are 1573's
  OCR (*quain*, *ſerinonem*, *Tuim*, *autein*, *inorte*, *meuin*, *euomain*, *carinen*, *eoruin*, *cos* for *eos*,
  *cum* for *eum*), nasal bars it lost (*Omnipotés*, *vétus*, *librű*, *habebát*), word breaks at line ends (*me
  dio*, *eccle ſijs*, *ha beas*, *vl la*, *duode cim*, *cru ciatus*), words run together (*patrifuo*, *adoriarte*,
  *Nouitua*, *Nelæditote*, *Eratautem*, *Aceadem*), note letters, margin notes, running heads (*APOCALYPSIS*) and
  references run into the text (section 4a). Each place was also read against 1556 (its e-rara OCR,
  `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 937–942), not only the collation's places: it
  found 6:4 *comissum* and 7:5's missing tribe (section 1), which the collation did not list.
- **The uncovered verses** (4:3, 8:1) were read whole on the image: 4:3 *qui ſedens, aſpectu ſimilis erat iaſpidi
  gemmæ, & ſardio. Solium circundabat iris, aſpectu ſmaragdum referens:* (crop `Rev.4.3-smaragdum`) and 8:1 *Vt
  autem ſeptimum aperuit ſigillum, extitit in cœlo ſilentium ferè dimidiam horam:* (`Rev.8.1-extitit`). Both agree
  with the draft but in spelling (*circundabat*, *aſpectu*, *extitit*).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fui/sui* 1:18, *fidus/sidus*
  2:13, 3:14, *fumus/sumus* 9:2, 9:17, *fontes/sontes* 7:17, 8:10, *fur* 3:3, *ferisque* 6:8, *feretisque* 2:10,
  *finis* 1:8, *fuit*, *fuerit*) was read in its verse: all are *f* by sense. Every *s* word whose *f*-form is Latin
  (*sinis/finis* 2:20, *sit/fit* 10:6, 11:13, *sis* 2:9, 3:15, *si*, *sui/fui* 8:12, *solium/folium*, *sine/fine*
  4:8, *secundus*): all are *s* by sense, and the places where 1573's OCR has the *f* and the *f*-form could be
  construed were read on the image: 10:6 *non ſit* (enlarged, `Rev.10.5-sit-zoom`: the nub on the left only, no
  crossbar) is long s. But **5:5** *ejusque septem sigilla referet* (Wikisource) is 1573's *reſeret* (section 2a).
- **Castellio's L. … G. marks**: none in chapters 1–11 (1573's OCR shows none, and none is on the image at any place
  read).
- **In all, 36 corrections**: 22 Wikisource slips (section 1, besides 3:1, already inserted), 8 readings of
  Castellio's revised text (section 2), 1 found by the f/s sweep (section 2a), 3 word divisions (section 3), 2 verse
  boundaries (section 4). Spellings (*quum*, *caritatem*, *carum*, *adflatus*, *adspiciens*, *adscende*,
  *exsequuntur*, *exstitit*, *quaecumque*, *tamquam*, *quemdam*, *leto*, *turibulum*, *obfuscata*, *circumdabat*,
  *multabo*, *terrae motus*, …) are left to stage 3 (decisions 37 and 42's rules); one rule proposed (section 6).
  Five places where 1556 reads against 1573 are recorded (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (22, and 3:1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Revelation 3:1** (already in the draft; no Apply line). Wikisource has no 3:1: its chapter 3 began at verse 2.
   The verse was inserted into the draft from 1573 before renumbering, in Wikisource's spelling: *Item angelo
   sardensis ecclesiae scribito: haec dicit qui septem Dei spiritus, et septem stellas habet: Novi tua facta, qui quum
   viventis nomen habeas, mortuus es.* 1573 *Item angelo Sardenſis eccleſiæ ſcribito: Hæc dicit qui ſeptem Dei
   ſpiritus, & ſeptem ſtellas habet: Noui tua facta, qui quum viuentis nomen habeas, mortuus es.* (canvas 939, crops
   `Rev.3.1-Sardensis`, `Rev.3.1-viventis`). The other printings have the verse with the same words: 1556 (OCR, in pieces: *Item
   agelo Sarden(is ecclefiz fcribito zHzc … dicit quí feptem Dei fpiritus& feptem fle … las habet: Nouituafacta,qui
   cum uiuentís no^ … men habeas,mortuus es*), 1758 (*qui quum viventis nomen habeas*), 1681, 1747 (*qui cum viuentis*),
   1715 (in pieces). Checked: it agrees with every printing read, but *quum*/*cum* (spelling).
2. **Revelation 1:6** *ei gloria et imperitum in perpetua saecula* → *imperium*. 1573 *gloria & imperium in perpetua
   ſecula: Amen.* (canvas 938, crop `Rev.1.6-imperium`); 1556 (OCR *ei gloria& imperium*), 1758, 1750, 1726.
   Wikisource alone.
   **Apply:** `Rev.1.6` la: `ei gloria et imperitum in` → `ei gloria et imperium in`
3. **Revelation 1:7** *eumque cernet omnis ocula* → *oculus*. 1573 *eumq; cernet omnis / oculus,* (canvas 938,
   `Rev.1.7-oculus`); 1556 (OCR *cernet omnís oculus*), 1758, 1715, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `Rev.1.7` la: `cernet omnis ocula,` → `cernet omnis oculus,`
4. **Revelation 2:15** *qui Nicolaitarum doctrinam tenant* → *teneant*. 1573 *qui Nicolaitarum doctrinam / teneant,
   id quod ego odi.* (canvas 938, `Rev.2.15-teneant`), as *qui Balaami doctrinam teneant* in 2:14; 1556 (OCR
   *doctrínam teneant*), 1758, 1750. Wikisource alone.
   **Apply:** `Rev.2.15` la: `doctrinam tenant,` → `doctrinam teneant,`
5. **Revelation 2:27** *ut ego a patre meo accepi* → *ut et ego*. 1573 *vt & ego à patre ᵇ meo accepi:* (canvas
   938, `Rev.2.27-ego`; *b* a note letter), ὡς κἀγὼ εἴληφα; 1556 (OCR *ut€ ego à … patre meo*, its *&* read as
   *€*), 1758, 1747, 1750. Wikisource alone.
   **Apply:** `Rev.2.27` la: `ut ego a patre meo` → `ut et ego a patre meo`
6. **Revelation 3:15** *Utinam aut frigidus esset, aut fervidus* → *esses*. 1573 *Vtinam aut frigidus eſſes, aut
   feruidus.* (canvas 939, `Rev.3.15-qui`), as *sis* before it; 1556 (OCR *efles*), 1758, 1747, 1750, 1726.
   Wikisource alone.
   **Apply:** `Rev.3.15` la: `aut frigidus esset,` → `aut frigidus esses,`
7. **Revelation 3:16** *quia tepidus es, aeque frigidus, neque fervidus* → *neque frigidus*. 1573 *quia tepidus es,
   neq; frigidus, neq; ferui-/dus* (canvas 939, `Rev.3.16-neque`), οὔτε … οὔτε; 1556 (OCR *necp frígtdus*), 1758,
   1747, 1726. Wikisource alone.
   **Apply:** `Rev.3.16` la: `es, aeque frigidus` → `es, neque frigidus`
8. **Revelation 3:17** *te divitem ditatumque esse dicit* → *dicis*. 1573 *ditatumq; eſſe dicis, nec vl-/la re
   indigere* (canvas 939, `Rev.3.17-dicis`), λέγεις; 1556 (OCR *dítatütp effe dícís*), 1758, 1747, 1726. Wikisource
   alone.
   **Apply:** `Rev.3.17` la: `esse dicit, nec` → `esse dicis, nec`
9. **Revelation 4:8** *qui fuit, qui est, et qui venturus sit* → *venturus est*. 1573 *qui fuit, qui eſt, & qui
   venturus eſt.* (canvas 939, `Rev.4.8-venturus`), as 1:4 and 1:8 (*qui venturus est*) in every text; 1556 (OCR
   *quí fuit, … qui eft,& qui uéturus eft*), 1758, 1750, 1726. Wikisource alone.
   **Apply:** `Rev.4.8` la: `qui venturus sit.` → `qui venturus est.`
10. **Revelation 4:9** *sedenti in solio, vinenti in perennia saecula* → *viventi*. 1573 *ſedenti in ſolio, viuenti /
    in perennia ſecula:* (canvas 939, `Rev.4.9-viventi`); 1556 (OCR *utuentí*), 1758, 1747, 1726. Wikisource alone.
    **Apply:** `Rev.4.9` la: `in solio, vinenti in` → `in solio, viventi in`
11. **Revelation 5:6** *Tum ego adspiciens, adnimadverti* → *animadverti*. 1573 *Tum ego aſpiciens, animaduerti in
    medio ſolij* (canvas 940, `Rev.5.6-animadverti`); 1556 (OCR *anímaduerti*), 1758. Wikisource alone. (*adspiciens*
    is stage 3's.)
    **Apply:** `Rev.5.6` la: `adspiciens, adnimadverti in` → `adspiciens, animadverti in`
12. **Revelation 5:11** *in millies centena millia, qui magna voce* → *in millies centena millia, et decies centena
    millia, qui*. 1573 *quorum numerus erat diſtributus in [millies centena] / millia, & decies centena millia, / 12
    qui magna voce dicebant* (canvas 940, `Rev.5.11-decies`); 1556 (OCR *in millíes centena mülía,& decíes centena
    millía,qui*), 1758, 1750. Castellio's own annotation on the verse (canvas 940) explains the two numbers: the
    praisers *distributos in classes, quarum aliae constarent singulae ex millies centenis millibus, aliae ex decies
    centenis millibus* (μυριάδες μυριάδων καὶ χιλιάδες χιλιάδων). Wikisource alone (1715's and 1747's OCRs not read
    here).
    **Apply:** `Rev.5.11` la: `in millies centena millia, qui` → `in millies centena millia, et decies centena millia, qui`
13. **Revelation 6:2** *isque prodiit vincens, et ut inveceret* → *vinceret*. 1573 *pro-/dijt vincens, & vt vinceret.*
    (canvas 940, `Rev.6.2-vinceret`); 1556 (OCR *winceret*), 1758, 1747, 1750. Wikisource alone.
    **Apply:** `Rev.6.2` la: `et ut inveceret.` → `et ut vinceret.`
14. **Revelation 6:4** *quem insidenti comissum est* → *commissum*. 1573 *quem inſidenti / commiſſum eſt vt ex terris
    auferret pacem* (canvas 940, `Rev.6.4-commissum`), as 7:2 *commissum erat* in the draft; 1556 (OCR *comilfum*),
    1715, 1726. Wikisource alone. Found reading the verse whole (not a collation place).
    **Apply:** `Rev.6.4` la: `insidenti comissum est` → `insidenti commissum est`
15. **Revelation 6:10** *Quin ingenti voce sic clamabant* → *Qui ingenti voce*. 1573 *10 qui ingenti voce ſic
    clamabát:* (canvas 940, `Rev.6.10-qui`), the souls of 6:9; 1556 (OCR *quiingentiuoce*), 1758, 1715, 1750, 1726.
    Wikisource alone. The capital is stage 3's.
    **Apply:** `Rev.6.10` la: `Quin ingenti voce` → `Qui ingenti voce`
16. **Revelation 7:5** *Ex Rubenis duodecim millia.* → *… Ex Gaddi duodecim millia.* Wikisource lacks the tribe of
    Gad, so its 7:5–8 name eleven tribes. 1573 *Ex Rubenis, duodecim millia. Ex Gaddi, duodecim / millia.* (canvas
    940, `Rev.7.5-Gaddi`), ἐκ φυλῆς Γὰδ δώδεκα χιλιάδες, KJV *Of the tribe of Gad*; 1556 (OCR *Ex Gadi,dubdecim
    rmillia*), 1758, 1681 (*Gaddi*), 1747 (*Gadi*). Wikisource alone. Inserted without the commas, as the draft writes
    the other tribes; the name's form is section 6's. Found reading the verse whole (the collation listed only the
    margin's *rm*).
    **Apply:** `Rev.7.5` la: `Ex Rubenis duodecim millia.` → `Ex Rubenis duodecim millia. Ex Gaddi duodecim millia.`
17. **Revelation 7:11** *senatoresque et quatuor animalia solium circumstantes* → *solium senatoresque et quatuor
    animalia circumstantes*. 1573 *Omnes autem angeli, ſolium ſenatoresq; & qua-/tuor animalia circumſtantes,* (canvas
    941, `Rev.7.11-solium`); 1556 (OCR *folium fé natóresip& quatuor anímalía círcumflantes*), 1758, 1681, 1747.
    Wikisource alone.
    **Apply:** `Rev.7.11` la: `senatoresque et quatuor animalia solium circumstantes` → `solium senatoresque et quatuor animalia circumstantes`
18. **Revelation 7:13** *his stolis albis amicti quinam sunt* → *hi stolis*. 1573 *ſic me affatus eſt: Hi / ſtolis
    albis amicti quinam ſunt,* (canvas 941, `Rev.7.13-Hi`), οὗτοι; 1556 (OCR *Hi ftofís*), 1758, 1681, 1747.
    Wikisource alone. The capital is stage 3's.
    **Apply:** `Rev.7.13` la: `adfatus est: his stolis` → `adfatus est: hi stolis`
19. **Revelation 8:8** *conservaque est pars tertia maris in sanguinem* → *conversaque*. 1573 *con-/uerſaq; eſt pars
    tertia maris in ſanguinem:* (canvas 941, `Rev.8.8-conversa`), as *conversa est* in 8:11; 1556 (OCR *conueríatp*),
    1758, 1715, 1747, 1750, 1726. Wikisource alone.
    **Apply:** `Rev.8.8` la: `conservaque est pars` → `conversaque est pars`
20. **Revelation 9:10** *Caudas habebant scorpionum similes* → *scorpiorum*. 1573 *Caudas habebant ſcorpiorum
    ſimiles* (canvas 941, `Rev.9.10-scorpiorum`), as *scorpii* in 9:3 and 9:5; 1556 (OCR *fcorpiorum*), 1758, 1681,
    1715, 1747, 1750, 1726. Wikisource alone.
    **Apply:** `Rev.9.10` la: `habebant scorpionum similes` → `habebant scorpiorum similes`
21. **Revelation 9:20** *qui his calamitatibus occisi non snut* → *sunt*. 1573 *occiſi / non ſunt,* (canvas 942,
    `Rev.9.20-sunt`); 1556, 1758, 1747. Wikisource alone.
    **Apply:** `Rev.9.20` la: `occisi non snut,` → `occisi non sunt,`
22. **Revelation 10:11** *et linguis, regnibusque multis* → *regibusque*. 1573 *& linguis, regi-/buſq; multis.*
    (canvas 942, `Rev.10.11-regibus`; its verse 10), βασιλεῦσι; 1556 (OCR *regibüsque*), 1715, 1747, 1750. Wikisource
    alone.
    **Apply:** `Rev.10.11` la: `linguis, regnibusque multis` → `linguis, regibusque multis`
23. **Revelation 11:18** *tuumque nomen revenentibus* → *reverentibus*. 1573 *tuumq; nomen reuerentibus, tum paruis*
    (canvas 942, `Rev.11.18-reverentibus`); 1556 (OCR *réuerentibus*), 1758, 1747, 1750, 1726. Wikisource alone.
    **Apply:** `Rev.11.18` la: `nomen revenentibus,` → `nomen reverentibus,`

## 2. Castellio's wording: 1573 against Wikisource's early line (8)

Where Wikisource reads with the early-line printings (1715, 1747, 1750). 1556 has Wikisource's reading at two of
these places (section 5): there 1573 is a later revision, and the draft follows it.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Revelation 1:4** *Joannes septem asianis ecclesiis favorem et pacem* → *gratiam et pacem*. 1573 *Iohannes ſeptem
   Aſianis eccleſijs gratiam & pa-/cem* (canvas 937, `Rev.1.4-gratiam`), χάρις; 1556 (OCR *A fianis eccleliis gratíam
   et pacem*), 1758, 1681, 1726. The early line *favorem* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Rev.1.4` la: `ecclesiis favorem et pacem` → `ecclesiis gratiam et pacem`
2. **Revelation 1:13** *similem homine nati* → *similem hominis filio*. 1573 *& in medio ſeptem candelabrorum ſimilem
   ho-/minis filio indutum veſte talari* (canvas 938, `Rev.1.13-similem`, `Rev.1.13-filio`), ὅμοιον υἱῷ ἀνθρώπου;
   1556 (OCR *fimilem. homínís filio índutum*), 1758, 1726. The early line *homine nati* (Wikisource, 1715, 1747,
   1750). The draft's comma is stage 3's.
   **Apply:** `Rev.1.13` la: `similem homine nati,` → `similem hominis filio,`
3. **Revelation 2:7** *victori dabo vesci arbore vitali* → *arbore vitae*. 1573 *Victori dabo veſci arbore vitæ, quæ
   in medio eſt* (canvas 938, `Rev.2.7-vitae`), τοῦ ξύλου τῆς ζωῆς; 1758, 1681, 1726. **1556** *vitali* (OCR
   *uíralí*), with Wikisource, 1715, 1750: a 1573 change (section 5).
   **Apply:** `Rev.2.7` la: `arbore vitali,` → `arbore vitae,`
4. **Revelation 2:9** *Novi tua facta et calamitatem et pauperiem* → *ac pauperiem*. 1573 *Noui tua facta &
   calamitatem ac pauperiem (cùm* (canvas 938, `Rev.2.9-ac`); 1556 (OCR *cla€ calamitatem ac pauperíem*), 1758,
   1681, 1726. The early line *et pauperiem* (Wikisource, 1715, 1747, 1750).
   **Apply:** `Rev.2.9` la: `calamitatem et pauperiem` → `calamitatem ac pauperiem`
5. **Revelation 2:10** *et tibi dabo vitae coronam* → *coronam vitae*. 1573 *& tibi dabo coronam / vitæ.* (canvas
   938, `Rev.2.10-coronam`), τὸν στέφανον τῆς ζωῆς; 1758, 1681, 1726. **1556** *uítae coronam* (OCR), with
   Wikisource, 1747: a 1573 change (section 5).
   **Apply:** `Rev.2.10` la: `dabo vitae coronam.` → `dabo coronam vitae.`
6. **Revelation 3:15** *Novi tua facta, quod neque frigidus sis* → *qui neque*. 1573 *Noui tua facta, qui neque
   frigidus ſis, neq; ferui-/dus.* (canvas 939, `Rev.3.15-qui`), as 3:1 *Novi tua facta, qui quum viventis nomen
   habeas*; 1758, 1726. The early line *quod* (Wikisource, 1715, 1747, 1750); 1556's OCR has *q* (not read).
   **Apply:** `Rev.3.15` la: `facta, quod neque` → `facta, qui neque`
7. **Revelation 8:10–11** *facis in morem ardens, quae in tertiam fluviorum partem, et in aquarum fontes delapsa est:
   (Est autem stellae nomen Absinthium) et conversa est tertia pars* → *ardens, qua in tertiam … fontes delapsa: (Est
   autem …) conversa est*. 1573 *ſtella, facis in morem ardẽs, qua in tertiam fluuiorum / partem, & in aquarum fontes
   delapſa: / 11 ( eſt autem ſtellæ nomen Abſinthium ) conuerſa / eſt tertia pars in Abſinthium* (canvas 941,
   `Rev.8.10-qua`, `Rev.8.11-conversa`): an ablative absolute, *qua … delapsa*, the star having fallen, the third
   part was turned to wormwood; 1556 (OCR *qua in tertíam fluuiorü partem,& ín aquarum fons tes delap(a( eftautem
   fiellz nomen Abfinthtum) conuería eft*), 1758, 1681, 1726 the same. The early line *quae … delapsa est … et
   conversa est* (Wikisource, 1715, 1747, 1750). For your eye: the three changes stand or fall together.
   **Apply:** `Rev.8.10` la: `ardens, quae in tertiam` → `ardens, qua in tertiam`
   **Apply:** `Rev.8.10` la: `fontes delapsa est:` → `fontes delapsa:`
   **Apply:** `Rev.8.11` la: `Absinthium) et conversa` → `Absinthium) conversa`
8. **Revelation 11:19** *visa est arca foederis ejus in ejus templo* → *arca foederis in ejus templo*. 1573 *viſa
   eſt arca fœ-/deris in eius templo, extiteruntq;* (canvas 942, `Rev.11.19-ejus`); 1758 (OCR *arca foederis in _*),
   1681, 1726. **1556** *foederis eius in eius templo* (OCR *arca foederis e¡us ín efus templo*), with Wikisource,
   1747, 1750, the Greek (τῆς διαθήκης αὐτοῦ) and the Vulgate: a 1573 change (section 5). For your eye: 1573 may
   have dropped one *eius* of two to avoid the repetition, or by a slip.
   **Apply:** `Rev.11.19` la: `arca foederis ejus in ejus templo` → `arca foederis in ejus templo`

## 2a. Found by the f/s sweep (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **Revelation 5:5** *qui librum aperiat, ejusque septem sigilla referet* → *reseret*. 1573 *eiuſq; ſeptem ſigilla
   reſeret.* (canvas 940, `Rev.5.5-reseret`, enlarged `Rev.5.5-reseret-zoom`: the *ſ* has the nub on the left only,
   as the *ſ* of *ſeptem* and *ſigilla* beside it), *reserare*, to unseal (λῦσαι τὰς ἑπτὰ σφραγῖδας), as *resignet*
   in 5:2 and *resolvas* in 5:9; **1758** *reſeret* (its OCR keeps the long s); 1556 (OCR *refereo*), 1681, 1747, 1750
   read *ref-* with the OCRs' f/s blindness. Wikisource *referet*.
   **Apply:** `Rev.5.5` la: `sigilla referet.` → `sigilla reseret.`

## 2b. Found where 1573 was not aligned (0)

The two uncovered verses (4:3, 8:1) were read whole on the image (intro): they differ from the draft only in spelling.
No decision needed.

## 3. Word division (3)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **Revelation 2:3** *propter meum nomen laboras inde fessus* → *indefessus*. One word, unwearied (οὐ κέκμηκας);
   1573 *laboras indefeſſus.* (canvas 938), 1556 (OCR *indetellus*), 1758, 1715, 1747, 1750.
   **Apply:** `Rev.2.3` la: `laboras inde fessus.` → `laboras indefessus.`
2. **Revelation 6:15** *tum liberi, seipsos in specus* → *se ipsos*. Your settled *sē ipsōs* (10× in `data/gold/`) and
   no *seipsos*, as Jude 1:12 and 1:19 (`data/review/jude1-stage2.md`). Not a quotation. 1573 joins it (*ſeipſos*,
   canvas 940).
   **Apply:** `Rev.6.15` la: `liberi, seipsos in` → `liberi, se ipsos in`
3. **Revelation 6:16** *et abira agni* → *ab ira*. A missing space; 1573 *& ab ira agni,* (canvas 940,
   `Rev.6.16-ab`), 1758, 1715, 1750, 1726.
   **Apply:** `Rev.6.16` la: `et abira agni` → `et ab ira agni`

## 4. Verse boundaries (2)

1573 (canvas 942) and Wikisource number chapter 10 in 10 verses, the KJV in 11. The split at *Habebat autem*
(`data/versification/Rev.draft.edits.tsv`, applied) gave the KJV's numbering; two boundaries inside the chapter still
follow Wikisource where 1573 and the KJV agree against it. The numbering stays the KJV's; the words go where 1573
prints them. Capitals are stage 3's.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **Revelation 10:2–3**: *sinistrum in terra* closes 10:2. 1573 *poſuitq; pedem ſuum dextrum in mari, ſini-/ſtrum in
   terra, / 2 & magna voce clamauit, quomodo rugit leo.* (canvas 942, crops `Rev.10.1-libellum`, `Rev.10.2-magna`):
   its verse 2 (the draft's 10:3) begins at *& magna voce*; the KJV 10:2 *and he set his right foot upon the sea, and
   his left foot on the earth*, 10:3 *And cried with a loud voice*; 1556 (OCR, in pieces: *pofuit& pedem fuum de- … xtrum ín marí,finiflrum
   ín terra,& magna uo- … ceclamauit*, no verse numbers). Wikisource begins its verse with *Sinistrum in
   terra*.
   **Apply:** `Rev.10.2` la: `pedem suum dextrum in mari,` → `pedem suum dextrum in mari, sinistrum in terra,`
   **Apply:** `Rev.10.3` la: `Sinistrum in terra, et magna voce` → `Et magna voce`
2. **Revelation 10:5–6**: *sublata in caelum sua manu* closes 10:5. 1573 *4 Tum angelus, quem in mari & in terra
   ſtantem vi-/deram, ſublata in cœlum ſua manu, / 5 iurauit per viuentem in perpetua ſecula* (canvas 942,
   `Rev.10.4-sublata`): its verse 5 (the draft's 10:6) begins at *iurauit*; the KJV 10:5 *lifted up his hand to
   heaven*, 10:6 *And sware by him that liveth*. Wikisource begins its verse with *Sublata in caelum sua manu*.
   **Apply:** `Rev.10.5` la: `stantem videram,` → `stantem videram, sublata in caelum sua manu,`
   **Apply:** `Rev.10.6` la: `Sublata in caelum sua manu, juravit per` → `Juravit per`

## 4a. Checked and kept

- **Uncovered verses** (4:3, 8:1): agree with the draft but in spelling (intro).
- **1:8 and 1:11** *Ego sum α et ω*: 1573 prints the Greek letters both times (*Ego ſum α & ω*, canvas 938,
  `Rev.1.8-alpha`, `Rev.1.11-primus`); the collation's *et et* and missing *α* at 1:11 are its OCR. Agrees.
- **1:3** *nam tempus instat*: 1573 *nam tempus / inſtat.* (canvas 937, `Rev.1.3-instat`; the OCR lost the line).
  Agrees.
- **2:18** *cujusque pedes*: 1573 *cuiuſq; pedes* (canvas 938, `Rev.2.18-cuius`; the OCR lost the *q;*), 1556 (OCR
  *cuíustp*). Agrees.
- **3:10** *eventuram*, **4:8** *habebant … erant*, **11:18** *judicentur*: 1573 *euenturã*, *habebãt*, *erãt*,
  *iudicẽtur* (canvas 939, `Rev.3.10-eventuram`, `Rev.4.8-habebant`; canvas 942, `Rev.11.18-judicentur`), the OCR
  without the bars. Agree.
- **3:14** *testis fidus atque verus*: 1573 *ver⁹* (canvas 939, `Rev.3.14-verus`), the OCR's *ver*. Agrees.
- **9:19** *capita habentes, quibus nocerent*: 1573 carries *quibus nocerent.* to the head of canvas 942
  (`Rev.9.19-habentes`, `Rev.9.19-habentes+next`). Agrees.
- **10:1** *de caelo descendentem*: 1573 *validum, de cœlo / deſcendentem* (canvas 942, `Rev.10.1-descendentem`; the
  OCR lost *de cœlo* beside the drop capital). Agrees.
- **10:3** *suas voces*: 1573 *fuas / voces.* (`Rev.10.2-magna`). **10:5** *stantem videram*: 1573 *ſtantem vi-/deram*
  (`Rev.10.4-sublata`). Agree.
- **6:10** *o Domine*: 1573 *ô Domine* (`Rev.6.10-qui`); the OCR's *6*. Agrees.
- **10:6** *ut tempus deinceps non sit*: long s (intro). Kept.
- **2:20** *Jezabelem*: 1573 *Ie-/ſabelem* (canvas 938, `Rev.2.20-Iesabelem`), 1556 (OCR *Tefabelem*), 1758
  *Iesabelem*; the 1738 Old Testament's archive.org OCR has *Iezabel*, *Iezabelem*, *Iezabelis*, *Iezabeli*.
  Under decision 46 (one form per person, the Old Testament's), Wikisource's *Jezabelem* is kept.
- **9:19** *siquidem* (1573 *ſi quidem*), **9:4** *ullamve* (1573, 1556 *vllam ve*), **4:4**, **5:8** *viginti
  quatuor* (1573 *vigintiquatuor*), **7:4** *quadraginta quatuor*: spacing; kept.
- **Note letters and margin notes**, not text (the margins as the OCR reads them): 1:1 *a* (*apatefactio*), 1:16 *o*
  (*ſplender*), 1:20 (*cid quod*, *stelle obice*), 2:26 *a*, 2:27 *b*, 3:2 *a* (*a inftirutus*), 3:3 *b* (*benqua
  accepifti do- … rinam*), 3:4 *c* (*c homines*), 3:10 *d* (*d quo ad. … uerfa patien*), 3:14 *c*, 3:15 *e* (*e hoc
  eft fi-dus atq; ve-*), 8:13 *à*, 9:11 *a* (*a perditor*), 11:8 *a* (*dum eft, que … allegoria vo-*); the side heads
  (*Ad Perga-menfem*, *Ad Sarden-*, *Ad Laodi-cenſem*, *Quatuor graffatores*, *Sextum*, *Angeliclan*, *Secundus*,
  *Tertius*, *Quartus*, *Sextus ange- … lus clangit*, *Iohannes li-bellum de-*, *Septimus an-gelus clagit*); the
  references (1:6 *colof.1.108*, *Hebr.9.14*, 1:7 *Lach.12.10*, 1:17 *Ela.44.4*, *& 41.11*, 1:19 *Efa.22.19*, 2:14
  *Num.24.14*, 2:23 *Jer.11.17*, *20.10*, *1.Reg.16.7*, 3:3 *3.Theff.5.2*, 3:19 *Prou.3.18*, 4:8 *Efa.6*, 4:11
  *infr.5.18*, 5:11 *Daniel.7*, *1.Petr.2.9*, 6:10 *Infra 19*, 6:15 *Efa.2.19*, *0/0.10.18*, 7:9 *4.Efd.2.20*, 7:16
  *Efa.49.10*, 7:17 *Efa.25.44*, *Infra 21.40*, 9:6 *Ejase 2.19*, *Ofee 2.18*, 9:7 *Sapien.6.9*, 10:8 *Ezech.3.9*,
  *4.Efd.14.10*); the running heads (*APOCALYPSIS*), the chapter summaries, Athanasius's argument, and the
  annotations after chapters 1, 3, 5 (on 5:11, section 1, item 12) and 8.
- **Punctuation and capitals, left to stage 3**: 1:1 *Joanni,* (1573 *Iohanni,* then *2 qui*), 1:10 *Divinitus*
  (1573 *diuinitus*), 1:16 *sol* (1573 *Sol*), 1:17 *ne metue* (1573 *Ne metue*), 1:18 *orci* (1573 *Orci*), 2:2
  *nec sunt, quos* (1573 *nec ſunt: quos*), 2:10 *diabolus* (1573 *Diabolus*), 2:12 *ancipitem acutum* (1573
  *ancipitem, acutum*), 2:22 *destiterint.* (1573 a colon), 3:7 *aperit:* (1573 a stop)
  4:1 *dixit;* (1573 a colon), 4:3 *Qui sedens adspectu* (1573 *qui ſedens, aſpectu*), 6:8
  *orcus* (1573 *Orcus*), 6:16 *agni:* (1573 a comma), 9:1 *tartari*, 9:2 *tartareum* (1573 *Tartari*,
  *Tartareum*), 11:11 *spectabant.* (1573 a colon), 11:17 *adeptus regnum* (1573 *adeptus, regnum*), and the capitals
  of the draft's verse openings.
- **Spellings, left to stage 3** (decisions 37 and 42's rules, and section 6): *quum*, *Quum* (1573 *cùm*, *quum*),
  *caritatem*, *carum* (1573 *charit-*, *charum*), *adflatus*, *adlocuta*, *adspectus*, *adspiciens*, *adspicio*,
  *adspiciente*, *adspicient*, *adstantem*, *adsto*, *adstiterant*, *adscende*, *adscendentem*, *Adscenditque*,
  *adscendet*, *adscendite*, *adscenderunt*, *adgrediar*, *adgressus*, *adgressa*, *adferre*, *adflictionem*,
  *adflaret*, *adloquens*, *adfatus* (1573 *aff-*, *all-*, *aſp-*, *aſt-*, *aſc-*, *agg-*), *exsequuntur*, *exstitit*,
  *exstiterunt*, *exstiteruntque* (1573 *exeq-*, *ext-*), *quaecumque*, *tamquam*, *Quamquam*, *quamquam*, *quemdam*,
  *quamdam* (1573 *quæcunque*, *tanquam*, *quendam*, *quandam*), *leto* (1573 *letho*), *terrae motus* (1573
  *terremotus*, *terræmotus*), *turibulum* (1573 *thuribulum*), *obfuscata* (1573 *offuſcata*), *circumdabat* (1573
  *circundabat*), *multabo* (1573 *mulctabo*), *nuntiavit*, *pronuntiantem* (1573 *nunc-*), *lacrimam*, *Joannes*,
  *Joanni*, *Jesu*, *Judaeos*, *Israëlitis*, *cetera* (1573 *cætera*), *caelo*, *coenabo*, *intelligant*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282454–58), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Rev 2:7 | *arbore vitae* | = | *arbore uitali* (OCR *uíralí*) | Wikisource, 1715, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| Rev 2:10 | *dabo coronam vitae* | = | *dabo uitae coronam* | Wikisource, 1747 with 1556; 1758, 1681, 1726 with 1573 |
| Rev 2:13 | *nec meam fidem negasti, etiam iis temporibus, quibus Antipas* | *etiam ijs temporibus, quibus Antipas* | *nec meam fidem negaſti: meisque temporibus Antipas* (OCR *nega^ il: meístp temporibus Antipas*) | 1747 with 1556; Wikisource, 1758, 1750 with 1573 |
| Rev 5:10 | *regnaturos in terra* | = | *regnaturos in terris* (OCR *regnatutos in terris*; one reading) | Wikisource, 1758, 1750 with 1573 |
| Rev 11:19 | *arca foederis in ejus templo* | = | *arca foederis eius in eius templo* (OCR *foederis e¡us ín efus templo*) | Wikisource, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12; 5:10 recorded
from one OCR reading)

## 6. Spelling rules proposed

Decision 46 writes one form per person, the Old Testament's; the form section 1, item 16 brings in has no row in
`data/rules/orthography.tsv` yet. Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| Gaddi | Gadi | word | 7:5 | 1556 *Gadi* (OCR), 1747 *Gadi*; your settled *Gadus*, *Gadum* (Genesis), no *Gadd-*. 1573, 1758, 1681 *Gaddi* |

**Decision:** accept (Claude, 2026-11-12, under decision 46; to be added to `data/rules/orthography.tsv` when this file
is applied)
