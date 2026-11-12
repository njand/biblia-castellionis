# Hebrews 1–7, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of 1 Timothy (`data/review/1tim1-6-stage2.md`).
Chapters 8–13 are in `data/review/heb8-13-stage2.md`.

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277). In 1573 Hebrews follows Jude: Athanasius's
  argument and 1:1–1:11 on canvas 929, 1:12–4:6 on 930, 4:6–6:10 on 931, 6:10–7:28 on 932. 1556 is the reference:
  where it reads otherwise, its reading is recorded as a variant (section 5); its e-rara OCR (pages 10282448–50)
  reaches nearly every verse of chapters 1–7, poorly in places (3:11, 3:15, 7:12–21). Stage 1 drafted Wikisource's
  Hebrews as **`text/draft/HEB.usfm`** (BSB paragraphs). You have no earlier work on Hebrews; `TXT/1 - OCR` (the
  1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Hebrews 1–7 is the early wording**, with the early-line printings 1715, 1747 and 1750: 2:16 *Non
  enim angelis, sed Abrahae posteris opitulatur* (1556 and 1573 *Non enim angelos, sed Abrahami semen assumpsit*),
  3:6 *retinemus*, 4:12 *et penetrans*, 6:2 *baptismatum*, 6:14 *fortunabo et*, 7:11 *Aaronis*, 7:27 *sicut*; with
  slips of its own (*mea requietem*, *facti simus*, *statuir*, *Jodua*, *res e obscura*, *munera victimas*,
  *Tnato*, *pitulatur*). **1573 departs from 1556 more often here than in the earlier letters**: 1:13 *ad dexteram
  meam*, 2:18 *dum tentaretur, potest, qui tentantur subvenire*, 3:8, 3:15 and 4:7 *indurare corda vestra* (1556
  *mentes obfirmare vestras*), 4:10 *in eius requietem* (1556 *in Dei*), 5:6 *in aeternum* (*in perpetuum*), 5:7
  *pro sua religione* (*pietate*), 7:2 *rex interpretatur* (*regem sonat*): the text follows 1573, 1556 is recorded
  (section 5). Several of the new readings are the Clementine Vulgate's words (`sources/parallel/vulgate`: *obdurare
  corda vestra*, *qui tentantur*, *in aeternum*, *qui interpretatur rex justitiae*), but 1573 sets none of them
  between *L.* and *G.* (read on the image at each place). 1758, 1681 and 1726 follow 1573 at these places.
- **Versification** (decision 5): the draft is at the KJV counts (129 verses in chapters 1–7). 1573 prints every
  verse number and agrees with the draft but at the end of chapter 7: 1573 (canvas 932) and Wikisource number *Hoc
  enim semel fecit, dum seipsum libavit* as 7:28 and *Lex enim homines …* as 7:29; the KJV's 7:27 ends *for this he
  did once, when he offered up himself*. Already joined to 7:27 by `data/versification/Heb.draft.edits.tsv` (applied
  2026-11-12), so the draft's 7:28 is 1573's 29. Nothing to move (section 2c).
- **Collation** (`python -m pipeline collate Heb 1-13`; `data/calibration/Heb1-13-collation.tsv`, chapters 1–7: 189
  places: 47 correct, 11 others-1573-agrees, 3 others, 125 base-only (85 reading, 15 division, 13 f/s, 8 spelling, 4
  edge), 3 uncovered), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/Heb.1.*`–`Heb.7.*`): every reading where 1573 and another printing agree against
  Wikisource, the *others* places, the base-only places whose 1573 words are Latin (1:7 *&*, 3:6 *tenemus*, 3:8
  *indurare corda vestra*, 4:10 *eius*, 5:6 *æternum*), and the four edges (1:5 *ipſe mihi filius erit*, 1:13
  *tuorum ſubſellium* at the head of the next column, 6:16 *rem confirmandam* at the head of canvas 932's first
  column: printed, lost by the OCR; 5:7 *religione exauditus*, section 2). The rest of the base-only readings are
  1573's OCR (*eniın*, *Fuinq;*, *meinineris*, *codein*, *habenus*, *fumıni*, *fastus*), word breaks at line ends
  (*per manet*, *i pſe*, *mo dò*, *requie tem*, *mor te*), note letters and margin notes run into the text (section 4).
  Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758,
  1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 929–932), not only the collation's places, and
  1573's verse numbers checked against the draft's: nothing further beyond section 3's divisions and the 7:5 omission
  (section 4).
- **The uncovered verses** (1:5, 2:16, 6:6) were read whole on the image: 1:5 *Cui enim dixit vnquam angelorum?
  Filius meus es tu, ego hodie genui te? Et rurſum: Ego ei pater, & ipſe mihi filius erit.* and 6:6 *& tamen
  relabuntur, ij iterum vitæ correctione renouentur: qui ſibi Dei filium iterum crucifigant, & in eum exemplum
  edant.* agree with the draft but for punctuation; 2:16 *Nõ enim angelos, ſed Abrahami ſemẽ aſſumpſit:* does not
  (section 2b).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fidusque/sidus*, *fit*
  7:18, *fuit/suit*, *fuere*, *fuerunt*, *forte/sorte*, *finis/sinis*, *feratque/seratque*) was read in its verse: all
  are *f*, and 1573's OCR has none of them with *ſ*. Every *s* word whose *f*-form is Latin (*sit/fit*, *si/fi*,
  *sine/fine*, *solium/folium*, *sui/fui*, *supersit*): all are *s* by sense, and the places where 1573's OCR has the
  *f* were read on the image: 1:3 *Qui cùm ſit*, 3:14 *ſi modò*, 4:16 *ad gratiæ ſolium*, 5:2 *cùm ipſe ſit*, 6:17
  *ſui conſilij*, 7:3 *ſine patre, ſine matre, ſine maioribus*, 7:7 *ſine vlla*, 7:16 *factus ſit*, 7:20 *ſine
  iureiurando* are all long s. None found.
- **Castellio's L. … G. marks**: none in chapters 1–7 (1573's OCR shows none, and none is on the image at any place
  read).
- **In all, 26 corrections**: 7 Wikisource slips (section 1), 16 readings of Castellio's revised
  text (section 2), 1 found in an uncovered verse (section 2b), 2 word divisions (section 3). Spellings (*quum*,
  *umquam*, *tamquam*, *paullo*, *caussa*, *adlocutus*, *adfectus*, *adfici*, *audiverant*, *audiverunt*,
  *heredem*, *caritatis*, *exsistere*, *Cuicumque*) are left to stage 3 (decision 37's and 42's rules); five rules
  proposed (section 6). Places kept against 1573 are in section 4, for your eye: chiefly **7:5 *genus ducentes***,
  where 1573 lacks *ducentes*.

## 1. Wikisource slips: 1573 and the other printings agree against it (7)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Hebrews 3:11** *non esse in mea requietem* → *in meam requietem*. 1573 *iratus iuraui non eſſe in meam requietem ingreſ-ſuros* (canvas 930); 1556 (*in meamrequietem*), 1758, 1747, 1750; as 3:18 and 4:3, 4:5 *in meam requietem*.
   **Apply:** `Heb.3.11` la: `in mea requietem` → `in meam requietem`
2. **Hebrews 3:14** *Christi consortes facti simus* → *facti sumus*. 1573 *Etenim Chriſti conſortes facti ſumus, ſi mo-dò* (canvas 930), γεγόναμεν; 1556 (*fumus*), 1758, 1681, 1715, 1747, 1750. Wikisource alone.
   **Apply:** `Heb.3.14` la: `facti simus, si modo` → `facti sumus, si modo`
3. **Hebrews 4:7** *quamdam statuir David* → *statuit*. 1573 *rurſum quandam ſtatuit Dauid diem* (canvas 931); 1556 (*flatuít*), 1758, 1681, 1715, 1747, 1750. *quamdam* (1573 *quandam*) is left to stage 3.
   **Apply:** `Heb.4.7` la: `quamdam statuir David` → `quamdam statuit David`
4. **Hebrews 4:8** *Si enim eos Jodua* → *Josua*. 1573 *Si enim eos Ioſua quietos reddidiſſet* (canvas 931); 1556 (*lofua*), 1758, 1681, 1715, 1747. Your settled *Jōsua* (Exodus, Acts 7:45, Colossians).
   **Apply:** `Heb.4.8` la: `eos Jodua quietos` → `eos Josua quietos`
5. **Hebrews 4:13** *nulla res e obscura est* → *nulla res ei obscura est*. 1573 *adeoq; nulla res ei obſcura eſt* (canvas 931); 1556 (*reseí*), 1758, 1681, 1747, 1750, 1726.
   **Apply:** `Heb.4.13` la: `nulla res e obscura` → `nulla res ei obscura`
6. **Hebrews 5:1** *ut munera victimas libet* → *munera victimasque libet*. 1573 *vt / munera victimaſq; libet pro peccatis* (canvas 931), δῶρά τε καὶ θυσίας; 1556 (*uíctimastp*), 1758, 1681, 1747, 1750.
   **Apply:** `Heb.5.1` la: `munera victimas libet` → `munera victimasque libet`
7. **Hebrews 7:22** *Tnato praestantioris* → *Tanto*. 1573 *tantò præſtantioris teſtamẽti ſponſor fuit Ieſus* (canvas 932); 1556 (*tanto*), 1758, 1750.
   **Apply:** `Heb.7.22` la: `Tnato praestantioris` → `Tanto praestantioris`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (16)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too, except at 1:13, 2:18, 3:8, 3:15, 4:7, 4:10, 5:6, 5:7 and 7:2, where 1573 alone changed it
(section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Hebrews 1:13** *sede ad meam dexteram* → *sede ad dexteram meam*. 1573 *Sede ad dex-/teram meam, donec ex tuis hoſtibus* (canvas 930); 1758, 1681, 1726. **1556** *ad meam dexteram*, with Wikisource, 1715, 1747, 1750: a 1573 change of order (section 5). For your eye.
   **Apply:** `Heb.1.13` la: `sede ad meam dexteram` → `sede ad dexteram meam`
2. **Hebrews 2:18** *passus est ipse periclitando, potest periclitantibus subvenire* → *ipse dum tentaretur, potest, qui tentantur subvenire*. 1573 *Quoniam enim paſſus eſt ipſe dum tentaretur, / poteſt, qui tentantur ſubuenire.* (canvas 930), πέπονθεν αὐτὸς πειρασθείς … τοῖς πειραζομένοις; 1758. **1556** *periclitando, poteſt periclitantibus*, with Wikisource, 1747, 1750: a 1573 change (section 5). The *tent-* spelling goes to stage 3 (*tentaretur* has a rule; *tentantur*, section 6); the punctuation is 1573's.
   **Apply:** `Heb.2.18` la: `ipse periclitando, potest periclitantibus subvenire.` → `ipse dum tentaretur, potest, qui tentantur subvenire.`
3. **Hebrews 3:6** *ad extremum firmam retinemus* → *firmam tenemus*. 1573 *gloriationem ad extremum firmam tenemus.* (canvas 930), κατάσχωμεν; 1556 (*firinam te-nemus*), 1758. The early line *retinemus* (Wikisource, 1715, 1747, 1750); 3:14 *firmum tenemus* in all.
   **Apply:** `Heb.3.6` la: `firmam retinemus.` → `firmam tenemus.`
4. **Hebrews 3:8** *Nolite mentes obfirmare vestras* → *Nolite indurare corda vestra*. 1573 *8 Nolite indurare corda veſtra, vt in iurgio* (canvas 930, no *L.* … *G.*), μὴ σκληρύνητε τὰς καρδίας ὑμῶν; 1758. **1556** *nolite mentes obfirmare ueftras*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5), made at all three places (3:15, 4:7). For your eye.
   **Apply:** `Heb.3.8` la: `Nolite mentes obfirmare vestras,` → `Nolite indurare corda vestra,`
5. **Hebrews 3:15** *nolite mentes obfirmare vestras* → *nolite indurare corda vestra*. 1573 *no-/lite indurare corda veſtra, vt in iurgio.* (canvas 930); 1758, 1681. 1556 *mentes obfirmare* with Wikisource, 1715, 1747, 1750. As item 4.
   **Apply:** `Heb.3.15` la: `nolite mentes obfirmare vestras,` → `nolite indurare corda vestra,`
6. **Hebrews 4:7** the same. 1573 *nolite indurare corda veſtra.* (canvas 931); 1758. 1556 *nolite mentes obfirmare ueftras* with Wikisource, 1715, 1747, 1750. As item 4 (after section 1's item 3).
   **Apply:** `Heb.4.7` la: `nolite mentes obfirmare vestras.` → `nolite indurare corda vestra.`
7. **Hebrews 4:10** *Qui enim in Dei requietem* → *in ejus requietem*. 1573 *Qui enim in eius requietẽ ingreſſus eſt* (canvas 931, the bar for *m* on the image; its OCR *requiete*), εἰς τὴν κατάπαυσιν αὐτοῦ; 1758. **1556** *in Dei requiete* (OCR *ín Deírequíete*), with Wikisource, 1715, 1747, 1750 *Dei requietem*: a 1573 change (section 5).
   **Apply:** `Heb.4.10` la: `in Dei requietem` → `in ejus requietem`
8. **Hebrews 4:12** *gladio acutior, et penetrans* → *ac penetrans*. 1573 *acutior, ac penetrans vſque ad di-/uiſionem* (canvas 931); 1556 (*acu-tiot,ac penetrans*), 1758, 1726. The early line *et* (Wikisource, 1681, 1715, 1747, 1750).
   **Apply:** `Heb.4.12` la: `acutior, et penetrans` → `acutior, ac penetrans`
9. **Hebrews 5:6** *tu es sacerdos in perpetuum* → *in aeternum*. 1573 *Tu es ſacerdos in æter-/num ad rationem Melchiſedechi.* (canvas 931), εἰς τὸν αἰῶνα; 1758, 1681 (OCR *artcrnum*); as 7:17 and 7:21 *in aeternum* in 1573 and the draft. **1556** *in perpetuum*, with Wikisource, 1715, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Heb.5.6` la: `sacerdos in perpetuum ad` → `sacerdos in aeternum ad`
10. **Hebrews 5:7** *et pro sua pietate exauditus* → *pro sua religione exauditus*. 1573 *& pro ſua / religione exauditus,* (canvas 931; *religione* heads the right-hand column, crop `Heb.5.7-pietate+next`; its OCR lost the line), ἀπὸ τῆς εὐλαβείας; 1758, 1681 (*rcligione*). **1556** *pro fua píetate exaudítus*, with Wikisource, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Heb.5.7` la: `pro sua pietate exauditus` → `pro sua religione exauditus`
11. **Hebrews 6:2** *Doctrinae baptismatum* → *baptismorum*. 1573 *doctrinæ, baptiſmorum, impoſitionis* (canvas 931); 1556 (*baptifmorum*), 1758, 1726. The early line *baptismatum* (Wikisource, 1715, 1747). Both are Latin (*baptismus* and *baptisma*); your settled text has *baptisma*, *baptismate* (17×) and *baptismum* (2×). For your eye. The comma after *doctrinae* is left to stage 3.
   **Apply:** `Heb.6.2` la: `Doctrinae baptismatum,` → `Doctrinae baptismorum,`
12. **Hebrews 6:12** *Nec sitis ignavi* → *Ne sitis ignavi*. 1573 *12 ne ſitis ignaui, ſed eorũ imitatores* (canvas 932), the purpose clause of 6:11 (ἵνα μὴ νωθροὶ γένησθε); 1556 (*ne fitis*), 1758. The early line *nec* (Wikisource, 1750). The capital follows the draft's verse openings; stage 3 decides it.
   **Apply:** `Heb.6.12` la: `Nec sitis ignavi` → `Ne sitis ignavi`
13. **Hebrews 6:14** *ni ego te fortunabo et amplificabo* → *felicitabo atque amplificabo*. 1573 *dicens: Ni ego te felicitabo atq; amplificabo.* (canvas 932); 1556 (*felícitabo … ate amplifícabo*), 1758, 1681 (*felicitabo, et*), 1726. The early line *fortunabo et* (Wikisource, 1715, 1750), as Castellio's *faustitatem → felicitatem* (Heb 12:17, `docs/editions.md`); your settled Genesis has *fēlīcitābō*.
   **Apply:** `Heb.6.14` la: `te fortunabo et amplificabo` → `te felicitabo atque amplificabo`
14. **Hebrews 7:2** *primum justitiae regem sonat* → *justitiae rex interpretatur*. 1573 *qui Melchiſedechus primùm iuſtitiæ rex interpreta-/tur: deinde Solymæ rex* (canvas 932), ἑρμηνευόμενος βασιλεὺς δικαιοσύνης; 1758, 1681, 1726. **1556** *iuftitiz regem fonat*, with Wikisource, 1747, 1750: a 1573 change (section 5).
   **Apply:** `Heb.7.2` la: `justitiae regem sonat;` → `justitiae rex interpretatur;`
15. **Hebrews 7:11** *ac non ad Aaronis rationem* → *Aharonis*. 1573 *ac non ad Aharonis rationem?* (canvas 932); 1556 (*Aharonis*), 1758, 1726. The early line *Aaronis* (Wikisource, 1715, 1747, 1750). The draft's own 5:4 has *Aharon*, and your settled text *Aharōn* (Exodus, Luke, Acts).
   **Apply:** `Heb.7.11` la: `ad Aaronis rationem` → `ad Aharonis rationem`
16. **Hebrews 7:27** *quotidie necesse, sicut pontifices* → *sicuti pontifices*. 1573 *qui non habet quotidie neceſſe, ſicuti pontifices,* (canvas 932); 1556 (*ficuti*), 1758. The early line *sicut* (Wikisource, 1715, 1747, 1750); your settled *sīcutī* 10×.
   **Apply:** `Heb.7.27` la: `necesse, sicut pontifices` → `necesse, sicuti pontifices`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter (intro). No decision needed.

## 2b. Found where 1573 was not aligned (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **Hebrews 2:16** *Non enim angelis, sed Abrahae posteris pitulatur* → *Non enim angelos, sed Abrahami semen assumpsit*. 1573 *16 Nõ enim angelos, ſed Abrahami ſemẽ aſſumpſit:* (canvas 930; the uncovered verse, read whole), οὐ γὰρ δήπου ἀγγέλων ἐπιλαμβάνεται, ἀλλὰ σπέρματος Ἀβραὰμ ἐπιλαμβάνεται; 1556 (OCR *angelos.fed AZ brahámifemé affumipfit*), 1758. The early line *angelis, sed Abrahae posteris opitulatur* (1747; 1715, its OCR misaligned into 3:6; 1750 *angelis, sed*), which Wikisource prints with the slip *pitulatur*. *assumpsit* is spelled as your settled *assūmpt-*. 1681's and 1726's OCR do not reach the verse.
   **Apply:** `Heb.2.16` la: `Non enim angelis, sed Abrahae posteris pitulatur:` → `Non enim angelos, sed Abrahami semen assumpsit:`

## 2c. Verse boundaries (0)

None to move: 1573's 7:28–29 against the KJV's 7:27–28 is already joined by `data/versification/Heb.draft.edits.tsv`
(intro). Every other verse number in 1573 stands where the draft's does. No decision needed.

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **Hebrews 6:13** *juravit per seipsum* → *per se ipsum*. Your settled *sē ipsum* (18×) against *seipsum* 4×, as Galatians 1:4 and 1 Timothy 2:6. Not a quotation. 1573 joins it (*iurauit per ſeipſum:*, canvas 932).
   **Apply:** `Heb.6.13` la: `juravit per seipsum,` → `juravit per se ipsum,`
2. **Hebrews 7:27** *dum seipsum libavit* → *dum se ipsum libavit*. As item 1; 1573 *dum ſeipſum libauit* (canvas 932, its 7:28).
   **Apply:** `Heb.7.27` la: `dum seipsum libavit` → `dum se ipsum libavit`

## 4. Checked and kept

- **7:5** *qui a Levi genus ducentes sacerdotium ineunt*: **1573 has no *ducentes*** (*5 Et quidem qui à Leui genus
  ſacerdotium ineunt,* canvas 932, on the image), and 1758 and 1726, which follow 1573, lack it too; 1556 (*genus
  ducentes*), 1681, 1747, 1750 and Wikisource have it. Without the participle *genus* has nothing to govern it
  (*genus ducere ab*, to trace one's descent from). Kept as a 1573 omission, as 1 Thess 2:8 *ſic vos* (recorded in
  section 5). **For your eye.**
- **1:5, 6:6** (uncovered): read whole on the image (intro); no difference but punctuation.
- **Edge places, printed in 1573** (on the image): 1:5 *ipſe mihi filius erit.* (at the head of the next column,
  under the chapter summary), 1:13 *tuorum ſubſellium?* (head of canvas 930), 6:16 *rem confirmandam.* (head of canvas
  932), and 3:19 *dif-/fidentiam* (in the OCR). Kept.
- **1:7** 1573's OCR *vtitur & 1044*: the margin reference *Pſal. 91.7 & 104.4* (canvas 929, on the image), not
  text. Kept.
- **3:13** *occallescat*: 1573 *oc-/caleſcat* (canvas 930, on the image), one *l*; 1556 *occallefcat* and every other
  printing *-ll-*, Gaffiot *occallēscō*. Kept.
- **5:2** *alucinantibus*: 1573 *hallucinanti-/bus* (canvas 931, on the image), with 1556, 1758, 1681, 1747;
  Wikisource and 1750 *alucinantibus*. One word; the spelling (Gaffiot *ālūcinor*, also *hallūcinor*) is left to
  stage 3.
- **1:3** *per semetipsum*: 1573 *ſemetipſum*, as Wikisource; your settled text has no form of it but *sēmet* (Eph
  4:16). Kept joined.
- **7:25** *Deum adeunt*: 1573 *adeunt* (canvas 932, on the image), with 1758, 1681, 1750; 1556 *adeant* (section 5),
  1715, 1747. Kept.
- **Others-1573-agrees, kept**: 1:7 *de angelis*, 1:8 *o*, 2:8 *videmus* (1715, 1747 *vidimus*), 3:18 *esse*, 4:1
  *tardasse*, 4:10 *in*, *ingressus*, 6:15 *consecutus*, 7:25 *eos*.
- **Note letters and margin notes**, not text: 1:14 *a*, 4:1 *a*, 4:2 *b* (*quoniam …*), 4:14 *c* (*respondeamus
  professioni nostrae*), 4:15 *d* (*ut nos*), 4:16 *e*, 5:11 *a* (*auditores*), 6:17 *a* (*promi[…] felicitati[…]*),
  7:13 *a* (*sacerdotio fungitur*), the note beside 7:19–20 (*… sedechianum perficit hominem*); the scripture
  references in the margin (as the OCR and image read them, among others: 1:3 *Sap. 7.26, Col. 1.15*, 1:5 *Psal. 2.7,
  2. Reg. 7.14*, 1:7 *Psal. 91.7 & 104.4*, 1:8 *Psal. 45.7*, 2:8 *1. Cor. 15.27*, 3:2 *Num. 12.7*, 4:3 *Psal. 95.11*,
  4:4 *Gen. 1*, 4:8 *Supr. 3.7*, 6:6 *Infr. 10.26*, 7:5 *Num. 18.21*); Athanasius's argument and the chapter
  summaries before 1:1, 2:1, 3:1, 4:1, 5:1, 6:1 and 7:1; 1573's annotations after 4:16 and 6:20, which the OCR ran
  into 7:1 with chapter 7's summary; and 6:6, which the OCR ran into 6:1 from the next column.
- **Punctuation and capitals, left to stage 3**: 1:5 *angelorum:* (1573 *?*) and *erit?* (1573 a stop), 2:8
  *subjecta:* (1573 a comma), 3:15 *jurgio,* (1573 a stop), 4:9 *sabbatismus* (1573 *Sabbatiſmus*), 6:2 the comma
  after *doctrinae*, 7:2 *rex:* (1573 a comma), 7:11 *levitico* (1573 *Leuitico*), 2:18 (section 2).
- **Spellings, left to stage 3** (decision 37's and 42's rules, and section 6): *adlocutus* (1573 *alloquutus*),
  *heredem*, *heredibus* (1573 *hæred-*), *quum*, *Quum* (1573 *cùm*), *umquam*, *numquam*, *tamquam*, *Quamquam*,
  *quamdiu*, *quamdam*, *Cuicumque* (1573 *-n-*), *paullo* (1573 *paulò*), *caussa*, *caussam*, *auctorem* (1573
  *authorem*), *adfectus*, *adfici* (1573 *aff-*), *audiverant*, *audiverunt* (1573 *audierant*, *audierunt*),
  *denuntiatum* (1573 *denunciatum*), *circumdatus* (1573 *circundatus*), *vindicavit* (1573 *vendicauit*; your
  settled *vindic-*), *lacrimis* (1573 *lachrymis*), *caeleste*, *caelestis* (1573 *cœl-*), *caritatis* (1573
  *charitatis*), *adfinis exsecrationi* (1573 *affinis execrationi*; section 6), *exseruistis* (1573 *exeruistis*),
  *ancoram* (1573 *anchoram*; your settled *ancor-*), *exsistere*, *exsistit* (1573 *exist-*), *adstat* (1573
  *astat*; section 6), *idcirco* (1573 *iccirco*), *tentationis*, *tentavere* (section 6), *majores*, *Jesum*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282448–50), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Heb 1:13 | *sede ad dexteram meam* | = | *ad meam dexteram* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| Heb 2:7 | *Eum paullo angelis* | *paulò* | *paululo* (OCR *pau lulo*) | 1747 with 1556; Wikisource, 1758, 1750 with 1573 |
| Heb 2:18 | *dum tentaretur, potest, qui tentantur subvenire* | = | *periclitando, potest periclitantibus subvenire* | Wikisource, 1747, 1750 with 1556; 1758 with 1573 |
| Heb 3:8 | *Nolite indurare corda vestra* | = | *nolite mentes obfirmare vestras* | Wikisource, 1715, 1747, 1750 with 1556; 1758 with 1573 |
| Heb 3:15 | *nolite indurare corda vestra* | = | *nolite mentes obfirmare vestras* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| Heb 4:7 | *nolite indurare corda vestra* | = | *nolite mentes obfirmare vestras* | Wikisource, 1715, 1747, 1750 with 1556; 1758 with 1573 |
| Heb 4:10 | *in ejus requietem* | = | *in Dei requiete* (OCR) | Wikisource, 1715, 1747, 1750 *Dei requietem*; 1758 with 1573 |
| Heb 5:6 | *sacerdos in aeternum* | = | *in perpetuum* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| Heb 5:7 | *pro sua religione exauditus* | = | *pro sua pietate exauditus* | Wikisource, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| Heb 7:2 | *justitiae rex interpretatur* | = | *justitiae regem sonat* | Wikisource, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| Heb 7:5 | *genus ducentes* (1556's) | *genus* (no *ducentes*) | *genus ducentes* | Wikisource, 1681, 1747, 1750 with 1556; 1758, 1726 with 1573 (section 4) |
| Heb 7:25 | *Deum adeunt* | = | *Deum adeant* | 1715, 1747 with 1556; Wikisource, 1758, 1681, 1750 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) and writes *tempt-* word by word;
these Hebrews 1–7 forms have no row in `data/rules/orthography.tsv` yet (checked with `normalize.word_rules()`).
Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adfinis | affinis | word | 6:8 | 1573 *af-/finis* (canvas 931); 1556, 1758, 1715; Gaffiot *affīnis*; your settled *affīnitātem* (Genesis) |
| adstat | astat | word | 7:13 | 1573 *ᵃ aſtat* (canvas 932, with its note letter); 1758, 1747; your settled *astat* (John); as the approved *adstabat → astabat*, *adstare → astare* |
| tentationis | temptationis | word | 3:8 | 1573 *ten-/tationis* (canvas 930); as the approved *tentationem*, *tentatione*, *tentatio* |
| tentavere | temptavere | word | 3:9 | 1573 *tentauêre* (canvas 930); as the approved *tentavit* |
| tentantur | temptantur | word | 2:18 | 1573 *qui tentantur* (canvas 930; the word section 2's item 2 brings in); as the approved *tentaretur → temptaretur* |

(*Adhuc*, *adjectio*, *adorent*, *adipiscamur*, *adultorum* do not assimilate; *attendenda*, *attestante*,
*accedamus*, *arrogat*, *appellatus*, *accommodatam*, *accipit* are already assimilated.)

**Decision:** accept (Claude, 2026-11-12, under decisions 37 and 42; added to `data/rules/orthography.tsv`)
