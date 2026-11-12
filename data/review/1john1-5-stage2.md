# 1 John 1–5, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of James (`data/review/jas1-5-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 924–927: the title and Athanasius's
  argument at the foot of 924 (after 2 Pet 3), its end, the summary and 1:1–2:29 on 925, 3:1–4:19 on 926, 4:20–5:21
  on 927, then 2 John). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant
  (section 5); its e-rara OCR has 1 John on pages 10282444–46 and reaches most of the letter, with its two columns
  interleaved on 10282446 (3:23–5:21), so that 4:2–3 and 4:4 are read in pieces under 5:7–10. Stage 1 drafted
  Wikisource's 1 John as **`text/draft/1JN.usfm`** (BSB paragraphs). You have no earlier work on 1 John; `TXT/1 -
  OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's 1 John is the early wording**, as its James and Paul's letters: *in carne* for *corporatum* (4:2,
  4:3), *caritas* for *amor* (4:7, 4:12, 4:17, 4:18), *quod … quod* for *quia … quia* (2:12, 2:13, 4:10), *nomini …
  credamus* (3:23), *crimen* for *noxa* (3:4), *Qui Dei filio fidem habet* (5:10), *nomini filii Dei fidem
  habentibus … fidem adjungatis* (5:13), *cupiditates* (2:17), *scribo vobis* (2:7), *nec est in eo* (2:4), each
  with the early-line printings 1715, 1747, 1750, and slips of its own (*isse*, *Qui est mendax*, *fit*). **1556
  stands between them**: it has the revised reading at 2:17, 2:22, 4:2–3, 4:4, 4:7, 4:12, 4:17, 4:18, but
  Wikisource's at 2:4, 2:12, 2:13, 3:4, 3:23, 4:9, 4:10, 4:20, 5:10 and 5:13 (section 5): 1 John was revised further
  for 1573 than any letter so far.
- **Versification** (decision 5): the draft is at the KJV counts (105 verses), no edits file. 1573 prints every verse
  number (its OCR reads 2:10 *to*, 2:11 *It*, 3:11 and 4:11 *II*, 5:11 *u*) and agrees with the draft everywhere,
  5:7–8 included. The OCR reads 4:8–9 after 4:19, and 4:21 before 4:20, out of the page's order; on the image they
  stand in order. Nothing to move.
- **Collation** (`python -m pipeline collate 1John 1-5`; `data/calibration/1John1-5-collation.tsv`, 177 places: 41
  *correct*, 10 *others-1573-agrees*, 6 *others*, 115 *base-only* (69 reading, 27 division, 9 f/s, 5 spelling, 5
  edge), 5 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/1John.*`, 39): every reading where 1573 and another printing agree against Wikisource,
  every base-only reading whose 1573 words are Latin (2:4 *nec in eo est*, 2:13 *quia*, 3:4 *noxam*, 3:12
  *fratre*, 4:10 *quia ip se se*, 4:12 *perfecto amore*, 4:17 *confidumus &*, 5:13 *credentibus … in nomen*), the
  edge places (2:10 *impingat*, 2:13 *a diabolum*, 2:28, 5:1 *ex eo natum amat*, a line the OCR lost; 5:11 *u*, the
  numeral), the parentheses of 1:2 and 5:7–8, and the uncovered verses. The rest of the base-only readings are
  1573's OCR (*autein*, *euim*, *aineimus*, *ainat*, *anamus*, *Deinque*, *nifit*, *funtis*, *quonian*,
  *fiquidein*, *cum* for *eum*), word breaks at line ends (*vl las*, *ta mem*, *co gnofcit*, *ma ior*, *pec catis*,
  *inge nio*), words run together (*Siin*, *Sinos*, *necest*, *Neamatemundum*, *Acquisquis*, *hæcest*, *Quodfinos*),
  note letters and margin notes run into the text (section 4) and the references (*Hebr*, *Apoc*, *Iob*, *Iohan*,
  *Cor*, *loan*). Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org
  printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 925–927), not only the collation's places: it
  found nothing beyond them but the clause order of 4:9 and the end of 4:20, in verses the collation could not align
  (below).
- **The five uncovered verses** were read whole on the image: 1:4 *Atq; hęc vobis ſcribim⁹, vt plena afficiamini
  lętitia* (crop `1John.1.4-scribimus`), 2:28 *Et nũc, filioli, manete in eo, vt cũ exiſtet, cõfidentiam habeamus,
  nec eũ in eius aduẽtu erubeſcamus.* (`1John.2.28-nunc`), 4:8 *Qui non amat, non nouit Deum: nam Deus amor eſt.*
  (`1John.4.8-amat`), 4:9 *In eo patuit Dei erga nos amor, quòd ſuum filium vnicum miſit Deus in mundum, vt per eum
  viuamus.* (`1John.4.9-suum`) and 4:20 *Si quis à ſe Deum amari dicit, & tamen fratrem ſuum odit, mendax eſt. Qui
  enim fratrẽ ſuum, quem vidit, non amat: Deum, quem non vidit, quî poſsit amare?* (`1John.4.20-possit`, the last
  word at the head of the next column, `1John.4.20-amare`). 4:9 (*ſuum filium*) and 4:20 (*quî poſsit*) differ from
  the draft (section 2, items 15 and 20); the others only in spelling (*afficiamini*, *existet*).
- **The Comma Johanneum (5:7–8)**, on the image (`1John.5.7-caelo`, `1John.5.8-terra`): 1573 prints *7 quoniam tres
  ſunt qui teſtantur ( in cœlo, pater, ſermo, & ſpiritus ſanctus: & hi tres vnum ſunt. 8 Item tres ſunt, qui teſtantur
  in terra ) ſpiritus, & aqua, & ſanguis, qui tres vnum ſunt.*, with the margin note *Hæc ( ) in quibuſdã exemplaribus
  non extant*: the heavenly witnesses and the start of verse 8 in parentheses, marked as missing from some copies.
  **1556** (OCR, page 10282446) has the same words and the same span between square brackets, *teſtatur[ ín coelo,
  pater, fermo,& fpirítus fanctus:& hí tres unum funt. Itém tres fünt quí teſtátur ín terra] fpiritus*, with the
  margin note in pieces (*Hec] ir … quiada es … kemplarih*, as *Hæc [ ] in quibusdam exemplaribus*). 1758 and 1726
  keep the parentheses (OCR *( in coelo … terra)*); Wikisource, 1747 and 1750 drop them. The draft follows 1573:
  its parentheses are restored (section 2, item 21); the margin note is not printed (no marginal notes), so the
  parentheses alone carry Castellio's mark. For your eye.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fuit/suit*, *fuissent*,
  *fuerit*, *fortes/sortes*, *fiet/siet*, *fit/sit*) was read in its verse: all are *f* by sense but **3:17** *ut fit
  Dei caritate praeditus*, where the sense wants *sit* (section 2a). Every *s* word whose *f*-form is Latin (*si/fi*,
  *sit/fit*, *sumus/fumus*, *simus/fimus*, *suam*): all are *s* by sense, and the places where 1573's OCR has the *f*
  and the *f*-form could be construed were read on the image: 2:27 *veraq; ſit*, 3:17 *vt ſit* (fetched again at a
  larger size, `1John.3.17-sit-zoom`: *fieri* before it has the crossbar of the fi ligature, *ſit* none), 4:6 *quis
  ſit erroris* are all long s.
- **In all, 28 corrections**: 2 Wikisource slips (section 1), 23 readings of Castellio's revised text (section 2), 1
  found by the f/s sweep (section 2a), 2 word divisions (section 3). Spellings (*quum*, *carissimi*, *caritate*,
  *umquam*, *quicumque*, *quidquid*, *letale*, *adficiamini*, *adnuntiamus*, *exsistet*, *intelligimus*, *obedit*,
  …) are left to stage 3 (decisions 37 and 42's rules); one rule proposed (section 6). Twelve places where 1556
  reads against 1573 are recorded (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **1 John 2:6** *debet, ut isse se gessit* → *ille*. 1573 *debet, vt ille ſe geſ-/ſit* (canvas 925, crop `1John.2.6-ille`); 1556 (OCR *ut ille fe geísit*), 1758, 1681, 1715, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `1John.2.6` la: `ut isse se gessit` → `ut ille se gessit`
2. **1 John 2:22** *Qui est mendax* → *Quis est mendax*. 1573 *Quis eſt mendax, niſi qui Ieſum negat eſſe Chri-/ſtum?* (canvas 925, `1John.2.22-Quis`), τίς ἐστιν ὁ ψεύστης; 1556 (OCR *Quís eff mendax*), 1758, 1715, 1747, 1750, 1726. Wikisource alone (1681's OCR lacks the opening).
   **Apply:** `1John.2.22` la: `Qui est mendax,` → `Quis est mendax,`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (23)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
Wikisource's reading at ten of these places (section 5): there 1573 is a later revision, and the draft follows it.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **1 John 1:2** *De sermone vitae loquor, quae vita patefacta est), id* → *(De sermone …*. 1573 *2 (de ſermone vitę loquor, quę / vita patefacta eſt) id, inquam* (canvas 925, `1John.1.2-sermone`): the parenthesis opens at the start of the verse; 1556 too (OCR *|( defermone uí xri … Datefattaeft)"*, page 10282444). Wikisource has only the closing bracket, as the archive.org OCRs show it (1758, 1681, 1747, 1750, 1726 *De sermone … est)*). The capital is stage 3's.
   **Apply:** `1John.1.2` la: `De sermone vitae loquor,` → `(De sermone vitae loquor,`
2. **1 John 2:4** *mendax est, nec est in eo veritas* → *nec in eo est veritas*. 1573 *mendax eſt, nec in eo eſt veritas.* (canvas 925, `1John.2.4-veritas`); 1758. **1556** *nec eſt in eo* (OCR *nec eft ín eo ueritas*), with Wikisource, 1681, 1715, 1747, 1750: a 1573 change (section 5).
   **Apply:** `1John.2.4` la: `nec est in eo veritas` → `nec in eo est veritas`
3. **1 John 2:7** *non novam praeceptionem scribo vobis* → *vobis scribo*. 1573 *non nouam præceptionem vobis ſcribo,* (canvas 925, `1John.2.7-vobis`); 1556 (OCR *praceptionem uo bis fcribo*), 1758, 1726. The early line *scribo vobis* (Wikisource, 1715, 1747, 1750).
   **Apply:** `1John.2.7` la: `praeceptionem scribo vobis, sed` → `praeceptionem vobis scribo, sed`
4. **1 John 2:12** *Scribo vobis, filioli, quod vobis ignoscuntur* → *quia*. 1573 *Scribo vobis, filioli, quia vobis ignoſcuntur* (canvas 925, `1John.2.12-quia`), as in 2:14 (*quia patrem nostis*, in every text), ὅτι; 1758, 1681. **1556** *quod* (OCR *qued*), with Wikisource, 1747, 1750 (section 5).
   **Apply:** `1John.2.12` la: `filioli, quod vobis` → `filioli, quia vobis`
5. **1 John 2:13** *Scribo vobis, patres, quod eum … juvenes, quod malum vicistis* → *quia … quia*. 1573 *Scribo vobis patres, quia eum qui à principio eſt, / nouiſtis. Scribo vobis iuuenes, quia ᵃ Malum viciſtis.* (canvas 925, `1John.2.13-quia`; *a* a note letter, margin *a diabolum*); 1758 (OCR, under 2:14: *quia eum … quia Malum*), 1681. **1556** *quod … quod* (OCR *quód eum … quód*), with Wikisource, 1747, 1750 (section 5).
   **Apply:** `1John.2.13` la: `patres, quod eum` → `patres, quia eum`
   **Apply:** `1John.2.13` la: `juvenes, quod malum` → `juvenes, quia malum`
6. **1 John 2:17** *Et mundus abit, et ejus cupiditates* → *cupiditas*. 1573 *Et mundus abit, & eius cupiditas.* (canvas 925, `1John.2.17-cupiditas`), ἡ ἐπιθυμία αὐτοῦ; 1556 (OCR *eíus cupiditas*), 1758, 1681, 1726. The early line *cupiditates* (Wikisource, 1747, 1750).
   **Apply:** `1John.2.17` la: `et ejus cupiditates.` → `et ejus cupiditas.`
7. **1 John 2:22** *nisi qui negat, Jesum esse Christum?* → *nisi qui Jesum negat esse Christum?* 1573 *niſi qui Ieſum negat eſſe Chri-/ſtum?* (canvas 925, `1John.2.22-Quis`); 1556 (OCR *quí: D lefum uegatetfe Chrftum*), 1758, 1681, 1726. The early line *qui negat Iesum esse* (Wikisource, 1715, 1747, 1750).
   **Apply:** `1John.2.22` la: `nisi qui negat, Jesum esse Christum?` → `nisi qui Jesum negat esse Christum?`
8. **1 John 2:22** *Is antichristus est, qui et patrem negat, et filium* → *qui patrem negat*. 1573 *qui patrem negat, & filium.* (canvas 925, `1John.2.22-patrem`); 1556 (OCR *quí patrem negat*), 1758, 1726. The early line *qui et patrem* (Wikisource, 1681, 1715, 1747, 1750).
   **Apply:** `1John.2.22` la: `qui et patrem negat` → `qui patrem negat`
9. **1 John 3:4** *is crimen committit, et peccatum crimen est* → *is noxam committit, et peccatum noxa est*. 1573 *ᵃ is noxam com-/mittit, & peccatum noxa eſt:* (canvas 926, `1John.3.4-noxam`; *a* a note letter, margin *a rem puniendam, ob quam aufe…*), ἀνομίαν … ἡ ἀνομία; 1758, 1681. **1556** *crimen* (OCR *& peccatum crimen. eft*), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5). For your eye.
   **Apply:** `1John.3.4` la: `is crimen committit, et peccatum crimen est` → `is noxam committit, et peccatum noxa est`
10. **1 John 3:23** *ut ejus filii Jesu Christi nomini credamus* → *ut in ejus filii Jesu Christi nomen credamus*. 1573 *vt in eius filij Ieſu / Chriſti nomen credamus* (canvas 926, `1John.3.23-nomen`), as at 5:13 (item 23); 1758, 1681, 1726. **1556** *nomini credamus* (OCR *nomíni credamus*), with Wikisource, 1747, 1750 (section 5).
    **Apply:** `1John.3.23` la: `ut ejus filii Jesu Christi nomini credamus` → `ut in ejus filii Jesu Christi nomen credamus`
11. **1 John 4:2** *Jesum Christum in carne venisse confitetur* → *corporatum venisse*. 1573 *Ieſum Chriſtum corporatum veniſſe confitetur, is* (canvas 926, `1John.4.2-corporatum`); 1556 (OCR *Chriftum corporatum uenille confitetur*), 1758, 1681, 1726. The early line *in carne* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1John.4.2` la: `Jesum Christum in carne venisse confitetur` → `Jesum Christum corporatum venisse confitetur`
12. **1 John 4:3** *Jesum Christum in carne venisse non confitetur* → *corporatum*. 1573 *Ieſum Chriſtum corpo-/ratum veniſſe non confitetur* (canvas 926, `1John.4.3-corporatum`); 1556 (OCR *corporatü ueníffenon*), 1758, 1681, 1726. The early line *in carne* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1John.4.3` la: `Jesum Christum in carne venisse non` → `Jesum Christum corporatum venisse non`
13. **1 John 4:4** *quoniam major est, qui in vobis, quam qui in mundo est* → *qui in nobis*. 1573 *quoniam ma-/ior eſt qui in nobis, quàm qui in mundo eſt.* (canvas 926, `1John.4.4-nobis`); **1556** too (OCR *quoníam maíor eft quí ín nobís, quàmquiínmun-do eft*, page 10282446), 1758, 1681, 1726. The early line *vobis* (Wikisource, 1715, 1747, 1750), as the Greek (ὁ ἐν ὑμῖν) and the Vulgate (*in vobis*). For your eye: both of Castellio's last texts read *nobis*, with the opening *Vos a Deo estis* and *eos vicistis* in the second person.
    **Apply:** `1John.4.4` la: `qui in vobis, quam` → `qui in nobis, quam`
14. **1 John 4:7** *nam caritas a Deo est* → *nam amor a Deo est*. 1573 *Nam amor / à Deo eſt* (canvas 926, `1John.4.7-amor`), as *Deus amor est* in 4:8 and 4:16 in every text; 1556 (OCR *Namamor a Deoeft*), 1758. The early line *caritas* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1John.4.7` la: `nam caritas a Deo est` → `nam amor a Deo est`
15. **1 John 4:9** *quod filium suum unicum misit Deus* → *quod suum filium unicum*. 1573 *quòd ſuum fi-/lium vnicum miſit Deus* (canvas 926, `1John.4.9-suum`; an uncovered verse); 1758. **1556** *filium suum* (OCR *quódfilí… fuum unicum*, the columns interleaved), with Wikisource, 1681, 1715, 1747, 1750 (section 5).
    **Apply:** `1John.4.9` la: `quod filium suum unicum` → `quod suum filium unicum`
16. **1 John 4:10** *non quod nos eum amaverimus, sed quod ipse nos amaverit* → *non quia nos eum, sed quia ipse nos amaverit*. 1573 *non quia nos eum, / ſed quia ip ſe nos amauerit,* (canvas 926, `1John.4.10-quia`; *ipſe* spaced, the OCR's *ſe ſe* one word); 1758. **1556** *non quód nos eum amauerimus, fed quód ipfe nos amauerít* (OCR), with Wikisource, 1715, 1747, 1750 (section 5).
    **Apply:** `1John.4.10` la: `non quod nos eum amaverimus, sed quod ipse nos amaverit` → `non quia nos eum, sed quia ipse nos amaverit`
17. **1 John 4:12** *sumusque ejus perfecta caritate praediti* → *perfecto amore*. 1573 *ſumusq; eius perfecto a-/more præditi.* (canvas 926, `1John.4.12-amore`); 1556 (OCR *fümustp eius petíectoa^ more przdítí*), 1758. The early line *perfecta caritate* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1John.4.12` la: `ejus perfecta caritate praediti` → `ejus perfecto amore praediti`
18. **1 John 4:17** *In eo perfecta caritate praediti sumus* → *perfecto amore*. 1573 *In eo perfecto amore præditi ſumus, ſi ᵃ de iudicij / die confidimus, ᵇ quod* (canvas 926, `1John.4.17-confidimus`; *a* and *b* note letters, the OCR's *&*); 1556 (OCR *In eo perfecto a… morepraedíd fumus*), 1758, 1681. The early line *perfecta caritate* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1John.4.17` la: `In eo perfecta caritate praediti sumus` → `In eo perfecto amore praediti sumus`
19. **1 John 4:18** *In caritate metus non est: quin perfecta caritas … perfecta caritate non est* → *In amore … perfectus amor … perfecto amore*. 1573 *In amore metus non eſt: quin perfectus amor fo-/ràs quatit metum, … quíque metuit, perfecto amore non eſt.* (canvas 926, `1John.4.18-amor`); 1556 (OCR *Inamoremetus non eft: quín perfe- … Clusamot forás … perfecto: … attore no eft*), 1758, 1681. The early line *caritas* (Wikisource, 1715, 1747, 1750).
    **Apply:** `1John.4.18` la: `In caritate metus` → `In amore metus`
    **Apply:** `1John.4.18` la: `quin perfecta caritas foras` → `quin perfectus amor foras`
    **Apply:** `1John.4.18` la: `perfecta caritate non est` → `perfecto amore non est`
20. **1 John 4:20** *Deum, quem non vidit, quo pacto potest amare?* → *qui possit amare?* 1573 *Deum, quem non vidit, quî poſsit / amare?* (canvas 927, `1John.4.20-possit`, `1John.4.20-amare`; an uncovered verse); 1758, 1681. **1556** *quo pacto potest amare* (OCR), with Wikisource, 1715, 1747, 1750 (section 5).
    **Apply:** `1John.4.20` la: `quo pacto potest amare?` → `qui possit amare?`
21. **1 John 5:7–8** *qui testantur in caelo, … qui testantur in terra, spiritus* → *qui testantur (in caelo, … qui testantur in terra) spiritus*. 1573's parentheses round the heavenly witnesses and *et hi tres unum sunt. Item tres sunt, qui testantur in terra* (canvas 927, `1John.5.7-caelo`, `1John.5.8-terra`; the margin *Hæc ( ) in quibuſdã exemplaribus non extant*); 1556 the same span in square brackets (OCR), 1758, 1726 (OCR *( in coelo … terra)*). Wikisource, 1747, 1750 without them. The words are all in the draft already (intro). For your eye: the marks are the only trace of Castellio's note in a text without margins.
    **Apply:** `1John.5.7` la: `qui testantur in caelo,` → `qui testantur (in caelo,`
    **Apply:** `1John.5.8` la: `qui testantur in terra,` → `qui testantur in terra)`
22. **1 John 5:10** *Qui Dei filio fidem habet* → *Qui credit in Dei filium*. 1573 *Qui credit in Dei filium, is in ſe Dei teſtimonium* (canvas 927, `1John.5.10-credit`), ὁ πιστεύων εἰς τὸν υἱὸν τοῦ θεοῦ; 1758, 1726. **1556** *Qui Dei filio fidem habet* (OCR *Qui Det filio fidem habet*), with Wikisource, 1747, 1750 (section 5).
    **Apply:** `1John.5.10` la: `Qui Dei filio fidem habet, is` → `Qui credit in Dei filium, is`
23. **1 John 5:13** *Haec vobis, nomini filii Dei fidem habentibus, … utque nomini filii Dei fidem adjungatis* → *Haec ego vobis, in nomen filii Dei credentibus, … utque in nomen filii Dei credatis*. 1573 *Hæc ego vobis, in nomen filij Dei credentibus, / ideò ſcripſi, … vtq; / in nomen filij Dei credatis.* (canvas 927, `1John.5.13-credentibus`, `1John.5.13-credatis`); 1758, 1681, 1726. **1556** *Hæc uobis, nomini filij Dei fidem habentibus … utq; nomini filij Dei fidem adiungatis* (OCR), with Wikisource, 1715, 1747, 1750 (section 5).
    **Apply:** `1John.5.13` la: `Haec vobis, nomini filii Dei fidem habentibus,` → `Haec ego vobis, in nomen filii Dei credentibus,`
    **Apply:** `1John.5.13` la: `utque nomini filii Dei fidem adjungatis.` → `utque in nomen filii Dei credatis.`

## 2a. Found by the f/s sweep (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **1 John 3:17** *qui fieri potest, ut fit Dei caritate praeditus?* → *ut sit*. 1573 *quî fieri poteſt vt ſit Dei charitate præditus.* (canvas 926, `1John.3.17-sit`, enlarged `1John.3.17-sit-zoom`: long s, no crossbar), the subjunctive after *fieri potest ut* (πῶς … μένει); 1758, 1681 (OCR *iit*), 1747, 1750 and 1556 (OCR *utfit*) read *fit/ſit* with the OCRs' f/s blindness. Wikisource *fit*.
   **Apply:** `1John.3.17` la: `ut fit Dei` → `ut sit Dei`

## 2b. Found where 1573 was not aligned (0)

The five uncovered verses (1:4, 2:28, 4:8, 4:9, 4:20) were read whole on the image (intro): 4:9 *ſuum filium* and 4:20
*quî poſsit amare* are section 2's items 15 and 20; the others differ only in spelling. No further decision needed.

## 2c. Verse boundaries (0)

1573 numbers every verse as the KJV (intro). No decision needed.

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **1 John 3:3** *is seipsum expurgat* → *se ipsum*. Your settled *sē ipsum* (66× in `data/gold/`) against *seipsum* 8×, as Jas 1:24. Not a quotation. 1573 joins it (*ſeipſum*, canvas 926).
   **Apply:** `1John.3.3` la: `is seipsum expurgat` → `is se ipsum expurgat`
2. **1 John 5:18** *ex Deo natus seipsum servat* → *se ipsum*. The same. 1573 *ſeipſum* (canvas 927).
   **Apply:** `1John.5.18` la: `natus seipsum servat` → `natus se ipsum servat`

## 4. Checked and kept

- **Uncovered verses** (1:4, 2:28, 4:8): agree with the draft but in spelling (intro).
- **3:12** *fratrem suum interemit*: 1573 *fratrẽ ſuum* (canvas 926, `1John.3.12-fratrem`; the OCR lost the bar), 1556
  (OCR *fratré*). Agrees.
- **3:18** *sed re ac veritate amemus*: 1573 *ſed re ac verita-/te amemus.* (canvas 926, `1John.3.18-veritate`; the OCR
  lost the second line). Agrees.
- **5:1** *etiam ex eo natum amat*: 1573 prints it (canvas 927, `1John.5.1-natum`; the OCR lost the line). Agrees.
- **4:1** *Carissimi, ne cuivis spiritui*: 1573's drop-capital line (*… mi, ne cuiuis ſpiritui credite*, canvas 926,
  `1John.4.1-cuivis`). Agrees.
- **4:17** *si de judicii die confidimus, quod*: 1573's OCR *sia … confidumus &* are the note letters *a* and *b*
  (on the image, `1John.4.17-confidimus`; margin *a iudicij nõ reformidamus*, *b quoniam iuſtè viuimus vt Deus …*).
  Agrees.
- **2:29** *quicumque justa faciat*: 1573 *faciat*, with 1747, 1750; 1758 and 1726 *facit*. Kept.
- **2:20** *a Sancto*: 1573 *abſancto* (*à ſancto*). The capital is stage 3's. Kept.
- **2:27** *veraque sit*, **4:6** *quis sit erroris*: *ſit* on the image (`1John.2.27-sit`, `1John.4.6-sit`). Kept.
- **Note letters and margin notes**, not text: 2:13 *a* (*diabolum*), 2:16 *B.*, 2:21 *& Chriſte* (OCR), 3:4 *a*
  (*rem puniendam, ob quam aufe…*), 3:17 *b* (*ſubuenit*), 3:22 *non later* (OCR), 4:17 *a*, *b*, 5:7 (*Hæc ( ) in
  quibuſdã exemplaribus non extant*), 5:16 *b* (OCR *bin fpiritest … fantum*), 5:18 *c* (*diabolus*); the references
  (as the OCR reads them: 1:4 *Iohan.8.12*, 1:7 *Hebr.9.28*, 1:8 *Apoc.2.5*, 2:5 *Iohan.13.35*, 3:9 *1.Iob.5.15*,
  3:23 *Iohan.13.34*, *Iohan.15.12*, *Infr.4.3*, 4:6 *Iohan.8.47*, 4:20 *Supr.2*, *Iohan.13.34*, 5:4 *Matt.11.30*,
  *1.Cor.15.57*, 5:10 *Iohan.3.16*, 5:13 *Supra 3.28*, 5:18 *1.Ioan.3.6*); Athanasius's argument and the summary run
  into 1:1 by the OCR; the chapter summaries; the running heads; 1573's annotation after chapter 2 (on 2:25, *τὴν ζωὴν
  τὴν αἰώνιον*).
- **Punctuation and capitals, left to stage 3**: 1:2 *est),* (1573 *eſt)* without the comma), 1:4 *laetitia.* (1573
  no stop), 2:4 *veritas:* (1573 a stop), 2:13 *malum*, 2:14 *malum*, 3:12 *a malo*, 5:18 *malus*, 5:19 *in malo*
  (1573 *Malum*, *Malo*, *Malus*), 2:18 *antichristum*, *antichristi* (1573 *Antichriſtum*), 3:8 *diabolus* (1573
  *Diabolus*), 3:12 *interemit?* (1573 *?*), 5:9 *admittimus.* (1573 a comma), 5:7 *Spiritus sanctus* (1573
  *ſpiritus ſanctus*).
- **Spellings, left to stage 3** (decisions 37 and 42's rules, and section 6): *quum*, *Quum* (1573 *cùm*),
  *carissimi* (1573 *chariſsimi*), *caritate*, *caritas* (1573 *charit-*), *umquam*, *quicumque*, *quidquid* (1573
  *vnquam*, *quicunque*, *quicquid*), *adficiamini* (1573 *afficiamini*; section 6), *adnuntiamus* (1573
  *anunciamus*, 1556 *annunciamus*; *adnūntiō* kept, decision 37), *nuntium*, *nuntiamus*, *denuntiatio* (1573
  *nunc-*), *exsistet* (1573 *exiſtet*; your settled *exsistet* 4×), *letale*, *letaliter* (1573 *lethale*),
  *intelligimus*, *intelligamus* (1573 *intellig-*), *obedit*, *adolescentes*, *caelo* (1573 *cœlo*), *Jesu*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282444–46), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 1 John 2:4 | *nec in eo est veritas* | = | *nec est in eo ueritas* | Wikisource, 1681, 1715, 1747, 1750 with 1556; 1758 with 1573 |
| 1 John 2:12 | *filioli, quia vobis* | = | *filioli, quod uobis* (OCR *qued*) | Wikisource, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 John 2:13 | *patres, quia eum … juvenes, quia malum* | = | *quód eum … quód* | Wikisource, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 John 3:4 | *is noxam committit, et peccatum noxa est* | = | *… & peccatum crimen eſt* (OCR *crimen. eft*; the first clause not reached) | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 John 3:23 | *ut in ejus filii Jesu Christi nomen credamus* | = | *… nomini credamus* | Wikisource, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| 1 John 4:9 | *quod suum filium unicum* | = | *quod filium suum unicum* (OCR *quódfilí… fuum unicum*, the columns interleaved) | Wikisource, 1681, 1715, 1747, 1750 with 1556; 1758 with 1573 |
| 1 John 4:10 | *non quia nos eum, sed quia ipse nos amaverit* | = | *non quód nos eum amauerimus, ſed quód ipſe nos amauerit* | Wikisource, 1715, 1747, 1750 with 1556; 1758 with 1573 |
| 1 John 4:20 | *qui possit amare?* | = | *quo pacto poteſt amare* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 John 5:7–8 | *(in caelo … in terra)* | = | the same words and span in square brackets, *[ ín coelo … ín terra]*, the margin note in pieces | 1758, 1726 with 1573's parentheses; Wikisource, 1747, 1750 without |
| 1 John 5:10 | *Qui credit in Dei filium* | = | *Qui Dei filio fidem habet* | Wikisource, 1747, 1750 with 1556; 1758, 1726 with 1573 |
| 1 John 5:13 | *Haec ego vobis, in nomen filii Dei credentibus* | = | *Hæc uobis, nomini filij Dei fidem habentibus* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |
| 1 John 5:13 | *utque in nomen filii Dei credatis* | = | *utq; nomini filij Dei fidem adiungatis* | Wikisource, 1715, 1747, 1750 with 1556; 1758, 1681, 1726 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-12; 4:9 recorded
from an interleaved OCR)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted), word by word; this form has no row
in `data/rules/orthography.tsv` yet (checked with `normalize.propose()` on the draft). Proposed, not written to the
file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adficiamini | afficiamini | word | 1:4 | 1573 *afficiamini* (canvas 925, `1John.1.4-scribimus`); 1556 (OCR *a,\|., ficiamíni*), 1758, 1726; as the approved *adficimur → afficimur*, *adficitis → afficitis* |

(*adnuntiamus* is *adnūntiō*'s, kept; *aderit*, *Adsit* are compounds of *sum*; *adhuc*, *adventu*, *advenisse*,
*admittimus*, *adjungatis* do not assimilate.)

**Decision:** accept (Claude, 2026-11-12, under decisions 37, 42 and 46; added to `data/rules/orthography.tsv`)