# 1 Thessalonians 1–5, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of Galatians (`data/review/gal1-6-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 904–906: the argument and 1:1–8 on 904,
  1:8–4:1 on 905, 4:2–5:28 on 906). 1556 is the reference: where it reads otherwise, its reading is recorded as a
  variant (section 5). Stage 1 drafted Wikisource's 1 Thessalonians as **`text/draft/1TH.usfm`** (BSB paragraphs).
  You have no earlier work on 1 Thessalonians; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected)
  is the witness `1726`, read as an OCR.
- **Wikisource's 1 Thessalonians is the early wording**, as its Romans, Corinthians and Galatians: *favorem* for
  *gratiam* (1:1), *favor* for *gratia* (5:28), *ac* for *et* (3:10), *converteretis* (1:9), *obdormierunt* (4:13),
  *possidere* inside 4:4 rather than at the end of the sentence (4:5). 1556 already has every one of these revisions.
  1573's own changes against 1556 are 4:14 *in Christo obdormiverint* (1556 *per Christum obdormiverunt*) and 5:2
  *diem esse venturam* (1556 *venturam esse*); at 3:11 (*paterque*), 4:8 (*nos*) and 4:16 (*cum … cum … cumque*)
  1573 reads with Wikisource against 1556 (section 5). 3:2 *de vestra fiducia* is 1573's and 1556's too, not the
  early *fiducia* for *fides*.
- **Versification** (decision 5): the draft is at the KJV counts (89 verses), no edits file. 1573 numbers every verse
  as the KJV except:
  - **3:10–13**: 1573 (canvas 905) prints no 11: *Ipse Deus paterque noster … iter secundet* runs on in its 10, so
    its 11–12 are the KJV's 12–13. The draft follows the KJV; nothing to move.
  - **5:16–18**: 1573 (canvas 906) prints *16 Semper gaudete, 17 continenter orate, 18 in omnibus Deo gratias agite:
    nam ea est Dei …*, as the KJV (16 *Rejoice evermore*, 17 *Pray without ceasing*, 18 *In every thing give
    thanks: for this is the will of God*). Wikisource and the draft have *continenter orate* in 16 and *In omnibus …
    agite* in 17. Moved (section 2c).
  - **4:4–5**: with 1573's word order (section 2, item 4), *possidere* ends the sentence inside 1573's own 5, as in
    1556; the KJV's *possess* is in 4. The boundary is 1573's, at *non (ut alienigenae*; nothing else moves.
- **Collation** (`python -m pipeline collate 1Thess 1-5`; `data/calibration/1Thess1-5-collation.tsv`, 120 places: 20
  *correct*, 7 *others-1573-agrees*, 3 *others*, 88 *base-only* (53 reading, 17 division, 8 f/s, 7 edge, 3
  spelling), 2 *uncovered*), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/1Thess.*`, 32): every reading where 1573 and another printing agree against Wikisource; the
  base-only places whose 1573 words are Latin (1:9 *conuerteritis*, 2:8 *vos*, 4:5 *possidere*, 4:13
  *obdormiuerunt*, 4:14 *resurrexisse*, 5:2 *esse venturam*, 5:15 *Videre*, 5:23 *vestra*); the edge places (1:10
  *supplicio defendit*, 3:4 *& vos scitis*, 4:9 *divinitus didiceritis*, 5:13 *pacatos*: line ends 1573's OCR lost,
  all printed). The rest of the base-only readings are 1573's OCR (*poteriria*, *Doinini*, *Domitium*, *Dominqs*),
  word breaks at line ends (*adi tum*, *col legam*), margin notes and references run into the text (*fide operemini,
  & laboretis, & spe toleretis*, *De resurrectione*, *1. Cor. 15. 51*). Each place was also read against 1556 (its
  e-rara OCR, `sources/erara-1556/`, pages 10282431–10282432) and the archive.org printings (1758, 1681, 1715, 1747,
  1750).
- **The two verses 1573's OCR covers poorly** (1:4, 5:2; `uncovered`) were read whole on the image: 1:4 (*ſciẽtes,
  fratres chariſsimi, vos eſſe diuinitùs electos*) agrees with the draft; 5:2 (*cùm ipſi præclarè ſciatis, Domini
  diem eſ-ſe venturam vt furem noctu*) has 1573's word order (section 2). Section 2b is empty.
- **Whole verses read against 1573's page text** (`mdz.page_text`, canvases 904–906), verse by verse: besides the
  collation's places this found 3:10 *sumopere* and *suplere*, Wikisource's misspellings of *summopere* and
  *supplere* (section 1), and the verse boundary at 5:16–18.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide*, *fides*,
  *fidentes*, *fidentibus*, *filium*, *fore*, *forte*, *fuit*, *fuimus*, *fuerimus*, *fueritis*, *fuisse*,
  *fuistis*, *faciatis*, *facitis*, *ferenti*) was read in its verse: all are *f*. Every *s* word whose *f*-form is
  Latin (*si*, *sit*, *sitis*, *simus*, *sumus*, *sive*, *secundet*): all are *s*, and the places where 1573's OCR
  has the *f* (3:12, 4:6, 5:5 *sumus*; 5:6, 5:8 *simus*; 5:10 *sive* twice; 5:24 *sit*) read *ſ* on the image. None
  found.
- **In all, 20 corrections**: 9 Wikisource slips (section 1), 8 readings of Castellio's revised text (section 2), 1
  verse boundary (section 2c), 2 word divisions (section 3). Applied to the draft under decision 30's standing rule
  once accepted. Spellings are left to stage 3 (decision 37's rules); five ad-, *tent-* and *ext-* forms without a
  rule are proposed (section 6). 2:8 is kept against 1573, a misprint there (section 4).

## 1. Wikisource slips: 1573 and the other printings agree against it (9)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **1 Thessalonians 2:2** *ante Phillipis* → *ante Philippis*. 1573 *quin quamuis antè Philippis (vt ſcitis)* (canvas 905); 1556, 1758, 1747, 1750 (Φιλίπποις). The space before the parenthesis is section 3's.
   **Apply:** `1Thess.2.2` la: `ante Phillipis(ut` → `ante Philippis(ut`
2. **1 Thessalonians 2:9** *noctes et dies(ne quem* → *noctes et dies operando (ne quem*. 1573 *quippe qui noctes & dies operando (ne quem veſtrûm grauaremus)* (canvas 905; ἐργαζόμενοι); 1556, 1758, 1681, 1715, 1747, 1750. Wikisource alone drops the word; the space before the parenthesis as everywhere else in the draft.
   **Apply:** `1Thess.2.9` la: `noctes et dies(ne quem` → `noctes et dies operando (ne quem`
3. **1 Thessalonians 3:5** *ne forte vos tentasse tentator* → *tentasset*. 1573 *ne fortè vos tentaſſet ten-tator* (canvas 905); 1556, 1758, 1681, 1715, 1747, 1750, 1726. The spelling *tempt-* is left to stage 3 (section 6).
   **Apply:** `1Thess.3.5` la: `vos tentasse tentator` → `vos tentasset tentator`
4. **1 Thessalonians 3:10** *dies sumopere orantes* → *dies summopere orantes*. 1573 *noctes & dies ſummopere orantes* (canvas 905); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `1Thess.3.10` la: `dies sumopere orantes` → `dies summopere orantes`
5. **1 Thessalonians 3:10** *quae vestrae fidei desunt, suplere?* → *supplere?* 1573 *quæ veſtræ fidei deſunt, ſupplere?* (canvas 905); 1556, 1758, 1726.
   **Apply:** `1Thess.3.10` la: `desunt, suplere?` → `desunt, supplere?`
6. **1 Thessalonians 3:13** *in adventum Domini nostri Jesu cum ejus sanctis* → *Domini nostri Jesu Christi cum ejus sanctis*. 1573 *in aduentum Do-mini noſtri Ieſu Chriſti cum eius ſanctis omnibus* (canvas 905); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `1Thess.3.13` la: `nostri Jesu cum ejus` → `nostri Jesu Christi cum ejus`
7. **1 Thessalonians 4:14** *Jesum mortuum esse et surrexisse* → *resurrexisse*. 1573 *Ieſum mortuum eſſe & reſur-rexiſſe* (canvas 906); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `1Thess.4.14` la: `esse et surrexisse,` → `esse et resurrexisse,`
8. **1 Thessalonians 5:8** *sobrii sumus induti* → *sobrii simus induti*. 1573 *At nos cùm diei ſimus, ſobrij ſimus, induti fidei* (canvas 906, both *ſimus* on the image; its OCR *ſiumus*; νήφωμεν, let us be sober); 1556, 1758, 1681, 1715, 1747, 1750.
   **Apply:** `1Thess.5.8` la: `sobrii sumus induti` → `sobrii simus induti`
9. **1 Thessalonians 5:12** *praesunt in Domino negotio* → *in Domini negotio*. 1573 *vobiſq; præſunt in Domini negocio* (canvas 906); 1556, 1758, 1681, 1715, 1747, 1750.
   **Apply:** `1Thess.5.12` la: `in Domino negotio` → `in Domini negotio`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (8)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read, except 4:14 and 5:2 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **1 Thessalonians 1:1** *Domini Jesu Christi, favorem et pacem* → *gratiam et pacem*. 1573 *gratiam, & pacem à Deo patre* (canvas 904), χάρις; 1556, 1758, 1681, 1726. The early line *favorem* (Wikisource, 1715), as Colossians 1:2.
   **Apply:** `1Thess.1.1` la: `Christi, favorem et pacem` → `Christi, gratiam et pacem`
2. **1 Thessalonians 1:9** *utque vos a deastris ad Deum converteretis* → *converteritis*. 1573 *vtq; vos à deaſtris ad Deum con-uerteritis* (canvas 905, on the image); 1556 (*cóuerterítís*), 1758, 1681. The perfect subjunctive, as *habuerimus* before it in the same question after *praedicant*. The early line *converteretis* (Wikisource, 1747, 1750).
   **Apply:** `1Thess.1.9` la: `ad Deum converteretis` → `ad Deum converteritis`
3. **1 Thessalonians 3:10** *Noctes ac dies* → *Noctes et dies*. 1573 *noctes & dies ſummopere* (canvas 905); 1556, 1758. The early line *ac* (Wikisource, 1747, 1750).
   **Apply:** `1Thess.3.10` la: `Noctes ac dies` → `Noctes et dies`
4. **1 Thessalonians 4:4–5** *suum vas cum sanctimonia ac honestate possidere, Non (ut alienigenae Deum ignorantes) cum cupiditatis libidine* → *… ac honestate, Non (…) cum cupiditatis libidine, possidere*. 1573 *4 ſciatq; quiſque veſtrûm ſuum vas cum ſanctimo-nia ac honeſtate, 5 non (vt alienigenæ Deum ignorantes) cum cupi-ditatis libidine, poſsidere.* (canvas 906, on the image); 1556 (*cum cupiditatis libidine, possidere:*), 1758 (its 4:4 ends at *honestate*). The early line has *possidere* after *honestate* (Wikisource, 1715, 1747, 1750). The verb now stands in 5, inside 1573's own verse 5 (intro, versification).
   **Apply:** `1Thess.4.4` la: `ac honestate possidere,` → `ac honestate,`
   **Apply:** `1Thess.4.5` la: `cupiditatis libidine:` → `cupiditatis libidine, possidere:`
5. **1 Thessalonians 4:13** *de iis, qui obdormierunt* → *obdormiverunt*. 1573 *de ijs qui ob-dormiuerunt* (canvas 906); 1556, 1758, 1681. The early line's syncopated *obdormierunt* (Wikisource, 1747, 1750); 4:14 and 4:15 have *-iverint* in every printing.
   **Apply:** `1Thess.4.13` la: `de iis, qui obdormierunt,` → `de iis, qui obdormiverunt,`
6. **1 Thessalonians 4:14** *qui per Christum obdormiverunt* → *qui in Christo obdormiverint*. 1573 *qui in Chriſto obdormi-uerint, ducet cum eo* (canvas 906, on the image); 1758, 1681. **1556** *qui per Christum obdormiverunt* (OCR *quiper Chriftum obdormígerunt*), with Wikisource, 1747, 1750 (διὰ τοῦ Ἰησοῦ): a 1573 change (section 5). For your eye.
   **Apply:** `1Thess.4.14` la: `qui per Christum obdormiverunt,` → `qui in Christo obdormiverint,`
7. **1 Thessalonians 5:2** *Domini diem venturam esse* → *Domini diem esse venturam*. 1573 *Domini diem eſ-ſe venturam vt furem noctu* (canvas 906, an uncovered verse, read whole); 1758 (word order). **1556** *diem uentur[am] esse*, with Wikisource, 1681, 1715, 1747, 1750: a 1573 change (section 5).
   **Apply:** `1Thess.5.2` la: `diem venturam esse ut` → `diem esse venturam ut`
8. **1 Thessalonians 5:28** *Jesu Christi favor: Amen.* → *gratia: Amen.* 1573 *Adſit vobis Domini noſtri Ieſu Chriſti gratia, Amen.* (canvas 906), ἡ χάρις; 1556, 1758. The early line *favor* (Wikisource, 1747, 1750), as Galatians 6:18.
   **Apply:** `1Thess.5.28` la: `Christi favor: Amen.` → `Christi gratia: Amen.`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the *f* (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The two uncovered verses (1:4, 5:2) were read whole on the image (crops `1Thess.1.4-scientes`,
`1Thess.5.2-venturam`): 1:4 agrees with the draft but for spellings (*ſciẽtes*, *chariſsimi*); 5:2's only difference
is the word order of section 2, item 7, already a collation place. No decision needed.

## 2c. Verse boundaries (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **1 Thessalonians 5:16–18**: *continenter orate* is 17, *In omnibus Deo gratias agite* begins 18. 1573 *16 Semper gaudete, / 17 continenter orate, / 18 in omnibus Deo gratias agite: nam ᵃ ea eſt Dei de vobis, qui ſitis Chriſti Ieſu, voluntas.* (canvas 906, each number at the head of its line), as the KJV's 5:17 *Pray without ceasing* and 5:18 *In every thing give thanks: for this is the will of God*. Wikisource numbers *Semper gaudete, continenter orate* as 16 and *In omnibus … agite* as 17 (the other OCRs, aligned to the draft, cannot show where their verses stand). *nam* takes a small letter inside the sentence, as 1573.
   **Apply:** `1Thess.5.16` la: `Semper gaudete, continenter orate,` → `Semper gaudete,`
   **Apply:** `1Thess.5.17` la: `In omnibus Deo gratias agite:` → `Continenter orate,`
   **Apply:** `1Thess.5.18` la: `Nam ea est Dei` → `In omnibus Deo gratias agite: nam ea est Dei`

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **1 Thessalonians 2:2** *Philippis(ut scitis)* → *Philippis (ut scitis)*. A space before the parenthesis, as 4:5 *Non (ut* and Colossians 2:7; 1573 *Philippis (vt ſcitis)* (canvas 905), 1556, 1758, 1750. (After section 1's item 1.)
   **Apply:** `1Thess.2.2` la: `Philippis(ut` → `Philippis (ut`
2. **1 Thessalonians 2:13** *sed(ut vere est)* → *sed (ut vere est)*. A space, as item 1; 1573 sets it tight here (*ſed(vt verè eſt)*, canvas 905, on the image), as Colossians 2:7.
   **Apply:** `1Thess.2.13` la: `sed(ut vere` → `sed (ut vere`

(2:9 *dies(ne* gets its space in section 1's item 2.)

## 4. Checked and kept

- **2:8** *Sic nos prae vestri cupiditate … impertituri fuerimus*: 1573 prints **ſic vos** (canvas 905, clear on the
  image), against *fuerimus*, *vobis* and the sense (we were ready to impart, ηὐδοκοῦμεν); **1556** *sic nos*, with
  1758, 1681, 1747, 1750. Kept as 1556: a 1573 misprint (section 5). For your eye.
- **4:1** *Quod superest igitur, fratres*: 1573 *Quod ſupereſt igiturs, fratre,* (canvas 905, on the image: the *s*
  set before the comma). Kept as 1556 and every printing.
- **3:2** *de vestra fiducia commonefaciendos*: 1573 *fiducia* (canvas 905), with 1556 and every printing. Kept.
- **3:11** *Ipse Deus paterque noster*: 1573 *paterq;* (canvas 905, on the image), with Wikisource, 1758, 1681, 1750,
  1726; **1556** *pater*, with 1747. Kept as 1573 (section 5).
- **4:8** *qui nos suo Sancto Spiritu donat*: 1573 *nos* (canvas 906, on the image), with 1758, 1750, 1726; **1556**
  *uos*, with 1715, 1747. Kept as 1573 (section 5). 1573's note letter *a* after *qui* is not text.
- **4:16** *cum praeconio, cum summi angeli voce, cumque divina tuba*: 1573 (canvas 906, on the image), with
  Wikisource and every archive.org printing; **1556** *in praeconio, in summi angeli voce in[que] divina tuba*
  (OCR *ín … ín … ín&p*). Kept as 1573 (section 5).
- **3:4** *et vos scitis*, **1:10** *supplicio defendit*, **4:9** *divinitus didiceritis*, **5:13** *pacatos*: 1573
  prints them (its OCR lost line ends). Kept.
- **1:5** *cum potentia*, **5:15** *Videte*, **5:23** *integrique vestri spiritus*: 1573 *poten-tia*, *Videte*,
  *veſtri* on the image (its OCR *poteriria*, *Videre*, *veſtra*). Kept.
- **3:4** *praedicebamus*: 1573 *prædiceba-mus*, with 1758, 1726; 1715, 1747 *praedicabamus*. Kept.
- **Note letters and margin notes**, not text: 1:3 *a* (*fide operemini, & laboretis, & spe toleretis*), 4:8 *a*,
  5:18 *a* (*id vos facere vult Deus qui Christiani sitis*); the margin glosses at 1:7–8 (*charitate la…*) and 4:13
  (*De resurrectione*); the references (*2. Thess. 1.3*, *Act. 20. 34*, *1. Cor. 15. 51*, *Mat. 24. 44*, *Ephes. 6.
  17*); and 1573's annotation after chapter 4 (on 4:15).
- **5:28** the subscription (*Ad Thessalonicenses prima scripta est Athenis*): 1573 sets it in italics under the
  verse (canvas 906). Set apart as `\cls` at stage 3 (decision 37).
- **1:1** *Sylvanus*: 1573 *SYLVAnus*, as 2 Thessalonians 1:1, where Wikisource writes *Silvanus*; your settled text
  has neither. Left to stage 3, for your eye (one spelling for both).
- **Punctuation and capitals, left to stage 3**: 2:19 *corona?* (1573 none), 4:5 *possidere.* (1573 a stop, 6 in
  lower case), 5:12 *Rogamus autem, vos fratres* (1573's comma).
- **Spellings, left to stage 3** (decision 37's rules, and section 6): *caritas*, *caritatisque*, *caritate*,
  *caritatem*, *cari*, *carosque*, *carissimi* (1573 *char-*), *ceteri* (1573 *cæteri*), *quidquam* (1573
  *quicquam*), *umquam*, *tamquam* (1573 *vnquam*, *tanquam*), *dumtaxat* (1573 *duntaxat*), *aliquamdiu* (1573
  *aliquãdiu*), *quum* (1573 *cum*; decision 41), *nuntiasset* (1573 *nunciaſſet*), *negotio*, *negotiis* (1573
  *negocio*, *negotijs*), *obscenitatis*, *obscenitatem* (1573 *obſcœn-*), *expectaretis* (1573 *expectaretis*),
  *Adflatus* (1573 *afflatus*), *caelis*, *caelo* (1573 *cælis*, *cœlo*).

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, pages 10282431–10282432), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 1 Thess 2:8 | *Sic nos prae vestri* (1556) | *ſic vos* | = | 1758, 1681, 1747, 1750 with 1556 |
| 1 Thess 3:11 | *Deus paterque noster* | = | *Deus pater noster* | 1747 with 1556; Wikisource, 1758, 1681, 1750, 1726 with 1573 |
| 1 Thess 4:8 | *qui nos suo Sancto Spiritu* | = | *qui uos* | 1715, 1747 with 1556; 1758, 1750, 1726 with 1573 |
| 1 Thess 4:14 | *qui in Christo obdormiverint* | = | *qui per Christum obdormiverunt* | Wikisource, 1747, 1750 with 1556; 1758, 1681 with 1573 |
| 1 Thess 4:16 | *cum praeconio, cum summi angeli voce, cumque* | = | *in praeconio, in summi angeli voce in[que]* | every other printing with 1573 |
| 1 Thess 5:2 | *Domini diem esse venturam* | = | *diem venturam esse* | Wikisource, 1681, 1715, 1747, 1750 with 1556; 1758 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted), writes *tempto* and *exst-*; these
forms have no row in `data/rules/orthography.tsv` yet (checked with `normalize.word_rules()`). Proposed, not added
to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| *adsentatoria* | *assentatoria* | word | 2:5 | 1573 *aſſentatoria* (canvas 905); 1758, 1747; as the approved *adsentiuntur* → *assentiuntur* |
| *adloquamur* | *alloquamur* | word | 2:16 | 1573 *alloqua-mur* (canvas 905); 1556, 1758, 1747, 1726; as the approved *adloquar* → *alloquar* |
| *adfligeremur* | *affligeremur* | word | 3:4 | 1573 *affligeremur* (canvas 905); 1556, 1758, 1715, 1726; as the approved *adflixit* → *afflixit*; your settled *afflīgimur* |
| *tentasset* | *temptasset* | word | 3:5 (after section 1's item 3) | 1573 *tentaſſet*; decision 37's *tempto*, as the approved *tentassent* → *temptassent* (your settled *temptāssent*) |
| *extinguite* | *exstinguite* | word | 5:19 | 1573 *extinguite* (canvas 906); Gaffiot heads *exstinguō* (`pipeline latin macron`); your settled *exstingu-* 6× against *extinguantur* 1× |

(1:6 *Adflatus* falls under the approved *adflatus* → *afflatus*, if the rule matches the capital; 3:5 *tentator* under
the approved *tentator* → *temptator*.)

**Decision:** propose (Claude, 2026-11-11; for your approval)
