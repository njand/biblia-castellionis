# 2 Timothy 1–4, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of Galatians (`data/review/gal1-6-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 912–914: 1:1–1:9 on 912, 1:9–3:15 on
  913, 3:15–4:22 on 914). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant
  (section 5). Stage 1 drafted Wikisource's 2 Timothy as **`text/draft/2TI.usfm`** (BSB paragraphs). You have no
  earlier work on 2 Timothy; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the witness
  `1726`, read as an OCR.
- **Wikisource's 2 Timothy is the early wording**, as its 1 Timothy: *favor* for *gratia* (4:22), *adfectatus* for
  *assequutus* (3:10), *pugnare non debeat* (2:24) and *Jesu Christo* (3:15) in the early order, with the early-line
  printings 1715, 1747, 1750; and slips of its own: words left out (1:7 *Deus*, 3:5 *vim*, 4:1 *regnoque*, 4:2
  *importune*, 4:6 the second *jam*) and misspellings (*salutatem*, *clemetia*, *docrina*, *ferarius*,
  *Onosiphori*). 1750 shares three of them (2:15 *Dei* for *Deo*, 2:17 *Hymeneus*, 4:16 *meae*). Where 1556's OCR
  can be read it has the revised readings, except 3:10, where it reads *affectatus* with Wikisource: *assequutus* is
  1573's change (section 5).
- **Versification** (decision 5): the draft is at the KJV counts (83 verses), no edits file. 1573 prints every verse
  number and agrees with the draft everywhere; no word sits in another verse than the KJV's.
- **Collation** (`python -m pipeline collate 2Tim 1-4`; `data/calibration/2Tim1-4-collation.tsv`, 120 places: 24
  correct, 7 others-1573-agrees, 5 others, 81 base-only (53 reading, 11 division, 9 edge, 6 f/s, 2 spelling), 3
  uncovered), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/2Tim.*`, 39):
  every reading where 1573 and another printing agree against Wikisource, the *others* places, the base-only places
  whose 1573 words are Latin (2:15 *oratione*, 3:16 *Omnes*, 4:6 *iamiam*, 4:20 *Trophinum*, 4:22 *secundu*, 4:10
  *Dalmatian*: the bar for *m*, a note letter, or the OCR), and the edge places (1:13 *Iesu posita* at the head of
  canvas 913's right column, 2:11 *viuemus*, 2:13 *nõ (poteſt*, 3:16 *ad iuſtitiæ diſciplinam*, 4:2 *doctrina*, 4:18
  *ſecula: Amen*, 4:21 *omnes*: all printed, lost by the OCR). The rest of the base-only readings are 1573's OCR
  (*padet*, *matret*, *Domitius*, *agrioscant*), word breaks at line ends, note letters and margin notes run into the
  text (section 4). Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the
  archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 912–914), not only the collation's places:
  nothing further beyond the spacing slips of section 3.
- **The three verses 1573's OCR does not align** (3:6, 3:7, 3:8; `uncovered`: the hOCR reads them after 3:11, in
  another block) were read whole on the image: *Ex his autem ſunt, qui in domos ſeſe inſinuãt, captiuaſq; reddunt
  mulierculas, quę peccatis coopertę, & varijs cupiditatibus actæ, / 7 ſemper diſcunt, & nunquam ad veri
  cognitionem peruenire poſſunt. / 8 Ac quomodo Iannes & Iambres Moſi reſtiterunt, ita hi veritati reſiſtunt:
  homines mente corrupti, circa fidem improbati.* They agree with the draft but for spellings. Section 2b is empty.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide*, *fidens*, *fidis*,
  *fili*, *filio*, *fore*, *forte*, *fuge*, *fuisse*, *fuit*, *fallent*, *fallentur*, *ferent*, *fero*, *ferarius*,
  *profectus*, *adferto*, *adfuit*, *adfectatus*, 19 words) was read in its verse: all are *f*. Every *s* word whose
  *f*-form is Latin (*si/fi*, *sit/fit*, *prosit/profit*, *deseruerunt/deferuerunt*, *sui/fui*, *sumus/fumus*,
  *semine*, *sanorum*, *satis*, *secunda*, *secundum*, *suas*, *saecula*, 13 words): all are *s* by sense, and where
  1573's OCR has the *f* and the *f*-form would make sense the image was read: 2:14 *nihil proſit* and 4:16 *me
  deſeruerunt* are long s. None found.
- **In all, 27 corrections** (27 Apply lines): 14 Wikisource slips (section 1), 5 readings of Castellio's revised
  text (section 2), Castellio's *L.* … *G.* marks at 3:4 (section 2c), 7 word divisions and spacings (section 3).
  Spellings (*caritas*, *carus*, *quum*, *caussa*, *tamquam*, *adsiduam*, *adsumtum*, *adferto*, *adfecit*,
  *submoneo*, *accomodatus*, *gangrenae*) are left to stage 3 (decision 37's rules); seven rules proposed (section
  6). Places kept against 1573 are in section 4, for your eye.

## 1. Wikisource slips: 1573 and the other printings agree against it (14)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **2 Timothy 1:7** *Non enim dedit nobis timiditatis* → *dedit nobis Deus timiditatis*. 1573 *Non enim dedit nobis Deus timiditatis ſpiritum* (canvas 912), ὁ θεός; 1556, 1758, 1750, 1726. Wikisource alone.
   **Apply:** `2Tim.1.7` la: `dedit nobis timiditatis` → `dedit nobis Deus timiditatis`
2. **2 Timothy 1:18** *in illa die Quantum item* → *in illa die. Quantum item*. 1573 *à Domino in illa die. Quantum item Epheſi* (canvas 913); 1758, 1747, 1750 (1556, 1715 a comma). A new sentence; Wikisource has no stop.
   **Apply:** `2Tim.1.18` la: `in illa die Quantum` → `in illa die. Quantum`
3. **2 Timothy 2:15** *ut teipsum Dei probes* → *Deo probes*. 1573 *vt teipſum Deo probes* (canvas 913), τῷ θεῷ; 1556 (*Deó*), 1758, 1715, 1747, 1726. 1750 *Dei* with Wikisource.
   **Apply:** `2Tim.2.15` la: `teipsum Dei probes` → `teipsum Deo probes`
4. **2 Timothy 2:17** *Hymeneus et Philetus* → *Hymenaeus*. 1573 *Hymenæus, & Philetus* (canvas 913); 1556 (*Hymenzus*), 1758, 1715, 1747, and the draft's own 1 Tim 1:20 *Hymenaeus*. 1750 *Hymeneus* with Wikisource. Gaffiot *Hўmĕnæus*.
   **Apply:** `2Tim.2.17` la: `est Hymeneus et` → `est Hymenaeus et`
5. **2 Timothy 3:5** *sed qui ejus abnegaverint* → *sed qui ejus vim abnegaverint*. 1573 *ſed qui eius vim abne-gauerint* (canvas 913), τὴν δύναμιν; 1556 (*eius uím*), 1758, 1715, 1750.
   **Apply:** `2Tim.3.5` la: `qui ejus abnegaverint` → `qui ejus vim abnegaverint`
6. **2 Timothy 3:11** *me vindicavit Deus* → *me vindicavit Dominus*. 1573 *ex quibus omnibus me vindicauit Dominus* (canvas 913), ὁ κύριος; 1556, 1758, 1715, 1747, 1750, 1726.
   **Apply:** `2Tim.3.11` la: `vindicavit Deus.` → `vindicavit Dominus.`
7. **2 Timothy 3:15** *ad salutatem* → *ad salutem*. 1573 *ad ſalutem per fidem* (canvas 914); 1758, 1747, 1750, 1726.
   **Apply:** `2Tim.3.15` la: `ad salutatem per` → `ad salutem per`
8. **2 Timothy 4:1** *qui adventu suo* → *qui adventu regnoque suo*. 1573 *qui aduentu regnoq; ſuo & viuos* (canvas 914), καὶ τὴν βασιλείαν αὐτοῦ; 1556 (*regnóque*), 1758, 1715, 1747, 1750.
   **Apply:** `2Tim.4.1` la: `adventu suo et` → `adventu regnoque suo et`
9. **2 Timothy 4:2** *insta opportune: argue* → *insta opportune, importune: argue*. 1573 *inſta opportunè, importunè:* (canvas 914), εὐκαίρως ἀκαίρως; 1758, 1715, 1747, 1750.
   **Apply:** `2Tim.4.2` la: `insta opportune:` → `insta opportune, importune:`
10. **2 Timothy 4:2** *cum clemetia, ac docrina* → *cum clementia, ac doctrina*. 1573 *ſumma cum clementia ac / doctrina.* (canvas 914); 1556 (*clementía ac*), 1758, 1715, 1747, 1750.
   **Apply:** `2Tim.4.2` la: `cum clemetia, ac docrina.` → `cum clementia, ac doctrina.`
11. **2 Timothy 4:6** *Nam ego jam immolandus* → *Nam ego jamjam immolandus*. 1573 *Nam ego iamiam immolandus ſum* (canvas 914, on the image; its OCR *iainiam*), ἤδη; 1758, 1715, 1747 (*iamiam*), 1750 (*iam iam*). Spelled as your settled *jamjam* (3×).
   **Apply:** `2Tim.4.6` la: `ego jam immolandus` → `ego jamjam immolandus`
12. **2 Timothy 4:14** *faber ferarius* → *faber ferrarius*. 1573 *Alexander faber ferrarius* (canvas 914); 1556, 1758, 1715, 1747, 1750.
   **Apply:** `2Tim.4.14` la: `faber ferarius,` → `faber ferrarius,`
13. **2 Timothy 4:16** *In prima meae causae dictione* → *In prima mea causae dictione*. 1573 *In prima mea cauſæ dictione* (canvas 914; *mea* with *dictione*); 1556, 1758, 1715, 1747, 1726. 1750 *meae* with Wikisource.
   **Apply:** `2Tim.4.16` la: `prima meae causae` → `prima mea causae`
14. **2 Timothy 4:19** *et Onosiphori familiam* → *et Onesiphori*. 1573 *& Oneſiphori fa-miliam* (canvas 914), as 1:16; 1556, 1758, 1747, 1750, 1726.
   **Apply:** `2Tim.4.19` la: `et Onosiphori familiam` → `et Onesiphori familiam`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (5)

Where Wikisource reads with the early-line printings (1715, 1747, 1750). 1556's OCR does not reach 2:24, 3:15 and
4:22; at 3:10 it reads with Wikisource (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **2 Timothy 2:24** *servus pugnare non debeat* → *servus non pugnare debeat*. 1573 *cùm Domini ſeruus non pugnare debeat* (canvas 913); 1758, 1726 (word order). Wikisource with 1747, 1750.
   **Apply:** `2Tim.2.24` la: `servus pugnare non debeat` → `servus non pugnare debeat`
2. **2 Timothy 3:10** *Tu vero adfectatus es meam doctrinam* → *Tu vero adsecutus es*. 1573 *Tu verò ᵃ aſſequutus es meam doctrinam* (canvas 913; margin *a perspexisti*), παρηκολούθησας, you have followed closely; 1758, 1726 (*assequutus*). The early line *adfectatus*, *affectatus* (Wikisource, 1715, 1747, 1750) and **1556** (OCR *affeclatus*): a 1573 change (section 5). Spelled as the draft's own 1 Tim 4:6 *adsecutus*, which the approved rule makes *assecūtus* at stage 3.
   **Apply:** `2Tim.3.10` la: `vero adfectatus es` → `vero adsecutus es`
3. **2 Timothy 3:15** *quae te possunt erudire* → *quae te possint erudire*. 1573 *quæ te poſsint e-/rudire* (canvas 913–914); 1758. Wikisource *possunt* with 1750 (1747's OCR *potfu 1 nt*).
   **Apply:** `2Tim.3.15` la: `te possunt erudire` → `te possint erudire`
4. **2 Timothy 3:15** *per fidem Jesu Christo habendam* → *per fidem Christo Jesu habendam*. 1573 *per fidem Chriſto Ieſu habendam* (canvas 914); 1758 (word order). Wikisource with 1747, 1750.
   **Apply:** `2Tim.3.15` la: `fidem Jesu Christo habendam` → `fidem Christo Jesu habendam`
5. **2 Timothy 4:22** *Adsit vobis favor* → *Adsit vobis gratia*. 1573 *Adſit / vobis gratia: Amen.* (canvas 914), ἡ χάρις; 1758. The early line *favor* (Wikisource, 1747, 1750), as 1 Tim 6:21.
   **Apply:** `2Tim.4.22` la: `vobis favor:` → `vobis gratia:`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the other letter (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The uncovered verses 3:6–8 were read whole on the image (crops `2Tim.3.6-insinuant`, `2Tim.3.8-Iannes`; intro): no
difference from the draft but spellings (*insinuãt*, *quę … coopertę*, *nunquam*, *Iannes & Iambres*). No decision
needed.

## 2c. Castellio's L. … G. marks: 3:4 (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **2 Timothy 3:4** *inflati, L. caeci et G. voluptatis* → *inflati, caeci et voluptatis*. 1573 *proditores, temerarij, inflati, L. cæci & G. volupta-tis magis quàm Dei amantes* (canvas 913, on the image; *L.* and *G.* in italics) and 1556 (*L. caeci & G.*) mark *caeci et* as taken from the Latin; 1758, 1715, 1750 print the words without the marks. Your decision on Matt 19:4 (*keep unmarked*, as Matt 8:18, Luke 10:1 and 11:7 in the settled text) keeps the marked words and drops the marks; Wikisource prints them. The marks stay on record in 1573's witness row (the aligner's `L…G` flag). For your eye.
   **Apply:** `2Tim.3.4` la: `inflati, L. caeci et G. voluptatis` → `inflati, caeci et voluptatis`

## 3. Word division and spacing (7)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **2 Timothy 1:5** *et(quomodo mihi persuasi)* → *et (quomodo*. A space before the parenthesis, as Colossians 2:7; 1573 *& (quomodo mihi perſuaſi)* (canvas 912), 1556, 1758, 1715, 1750.
   **Apply:** `2Tim.1.5` la: `et(quomodo` → `et (quomodo`
2. **2 Timothy 1:15** *me(hoc tu nosti)* → *me (hoc*. 1573 *Auerſati ſunt me (hoc tu noſti)* (canvas 913), 1556, 1758, 1715, 1747.
   **Apply:** `2Tim.1.15` la: `me(hoc` → `me (hoc`
3. **2 Timothy 2:13** *manet, seipsum negare* → *manet, se ipsum*. Your settled *sē ipsum* (18×) against *seipsum* 4×, as Galatians 1:4. 1573 joins it (*ſeipſum*, canvas 913).
   **Apply:** `2Tim.2.13` la: `manet, seipsum negare` → `manet, se ipsum negare`
4. **2 Timothy 2:15** *ut teipsum Deo probes* → *ut te ipsum*. The draft's 1 Timothy divides it (4:16, 5:22), your settled text *tē ipsum* 13×; not a quotation. 1573 joins it (*teipſum*, canvas 913). (After section 1's item 3.)
   **Apply:** `2Tim.2.15` la: `ut teipsum Deo` → `ut te ipsum Deo`
5. **2 Timothy 2:19** *ab injustitia,quisquis* → *ab injustitia, quisquis*. A missing space; 1573 *ab iniuſtitia, quiſquis* (canvas 913).
   **Apply:** `2Tim.2.19` la: `injustitia,quisquis` → `injustitia, quisquis`
6. **2 Timothy 2:21** *si quis seipsum ab his* → *si quis se ipsum*. As item 3; 1573 *ſeipſum* (canvas 913).
   **Apply:** `2Tim.2.21` la: `quis seipsum ab` → `quis se ipsum ab`
7. **2 Timothy 2:23** *quippe quae(ut scis)* → *quippe quae (ut scis)*. 1573 *quippe / quæ (vt ſcis) pugnas gignant* (canvas 913, on the image), 1758, 1750.
   **Apply:** `2Tim.2.23` la: `quae(ut` → `quae (ut`

## 4. Checked and kept

- **1:6** *Quam ob caussam submoneo te*: 1573 *ſummoneo* (canvas 912, on the image), with 1556, 1758, 1715; 1750
  *submoneo*. One verb in two spellings (Gaffiot *submŏnĕō* · *summŏnĕō*); your settled *summonuit* (2×). Left to
  stage 3 (section 6).
- **1:12** *persuasum habeo, eum posse meum depositum*: 1573's OCR *cum a meam vi-* and *ameum* are the note letter
  *a* (margin, as the OCR reads it, *a meam vi-*). Kept.
- **2:15** *recte secantem veritatis orationem*: 1573 *ſecãtem … orationẽ* (canvas 913, the bars for *n* and *m*;
  its OCR *secatem*, *oratione*), with 1556, 1758, 1715, 1747, 1750. No difference.
- **2:24** *injuriae patiens*: 1573 *patiens* (canvas 913, on the image; its OCR *patieris*). Kept.
- **3:2** *homines sui amantes*: 1573 *ſui amantes* (canvas 913, apart on the image; its OCR *suiamantes*). Kept.
- **3:16** *Omne scriptum*: 1573 *Omne ᵇ ſcriptum* (canvas 914; its OCR *Omnes*, the note letter); *ad iuſtitiæ
  diſciplinam* is printed at the head of the right column. Kept.
- **4:10** *Titus in Dalmatiam*: 1573 *Dalmatiam* (canvas 914, on the image; its OCR *Dalmatian*). Kept.
- **4:20** *Trophimum*: 1573 *Trophimum* (canvas 914, on the image; its OCR *Trophinum*). Kept.
- **Edge places, printed in 1573** (on the image): 1:13 *Ieſu poſita.* (head of canvas 913's right column), 2:11
  *viuemus*, 2:13 *negare nõ (poteſt.* (the turn-over printed above the line), 4:2 *doctrina.*, 4:18 *ſecula: Amen.*,
  4:21 *omnes.* Kept.
- **Note letters and margin notes**, not text: 1:12 *a*, 2:21 *a* (*scilicet vitiis quae dixi*), 3:10 *a*
  (*perspexisti*), 3:16 *b*, 3:17 *c*; the scripture references in the margin (1:3, 2:16, 2:19, 2:22, 2:23, 3:12, 4:8); 1573's
  annotation after chapter 3; the argument of Athanasius and the chapter summaries.
- **4:22** the subscription (*Scripta est Romae ad Timotheum secunda, quum se Paulus iterum stitisset Caesari
  Neroni*): 1573 sets it in italics under the verse (canvas 914, *Scripta eſt Romæ ad Timotheum ſecunda, / cùm ſe
  Paulus iterum ſtitiſſet / Cæſari Neroni.*; its OCR *ſecundu*), as the draft but its final stop. Set apart as `\cls`
  at stage 3 (decision 37).
- **2:6** *prius, quam*, **1:18**, **2:19** and the other punctuation (1573's colons and stops): left to stage 3.
- **Spellings, left to stage 3** (decision 37's rules, and section 6): *caro*, *caritatis*, *caritate*,
  *caritatem* (1573 *charo*, *charit-*), *caussam* (1573 *cauſam*), *quum*, *Quum* (1573 *cùm*; decision 41),
  *tamquam*, *numquam* (1573 *tanquam*, *nunquam*), *adsiduam*, *adsumtum*, *adferto*, *adfecit* (1573 *aſsiduam*,
  *aſſumptum*, *afferto*, *affecit*), *submoneo* (1573 *ſummoneo*), *accomodatus* (1573 *accommodatus*), *gangrenae*
  (1573 *gangrænæ*), *aevo* (1573 *æuo*), *litteras* (1573 *literas*), *hiemem* (1573 *hyemem*), *caeleste* (1573
  *cœleſte*), *saecula* (1573 *ſecula*), *audivisti*, *quaesiverit*, *hero*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 2 Tim 3:10 | *Tu vero adsecutus es* (1573 *assequutus*) | = | *Tu uero affectatus es* (OCR *affeclatus*) | Wikisource (*adfectatus*), 1715, 1747, 1750 with 1556; 1758, 1726 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) word by word; these 2 Timothy forms
have no row in `data/rules/orthography.tsv` yet (checked with `normalize.word_rules()`), nor do three others.
Proposed, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| adsiduam | assiduam | word | 1:3 | 1573 *aſsiduam* (canvas 912); 1758, 1715, 1726; your settled *assidu-*; as the approved *adsidui → assidui* |
| adsumtum | assumptum | word | 4:11 | 1573 *aſſumptum* (canvas 914); 1715; as the approved *adsumptum → assumptum*, *adsumto → assumpto* |
| adferto | afferto | word | 4:13 | 1573 *afferto* (canvas 914); 1758, 1747; your settled *Afferte*, *affert*; as the approved *adfers → affers* |
| adfecit | affecit | word | 4:14 | 1573 *affe-cit* (canvas 914); 1556, 1758, 1715, 1747; as the approved *adfecti → affecti* |
| submoneo | summoneo | word | 1:6 | 1573 *ſummoneo* (canvas 912); 1556, 1758, 1715; your settled *summonuit* (2×); Gaffiot gives both (*submŏnĕō*, *summŏnĕō*). For your eye |
| accomodatus | accommodatus | word | 2:24 | 1573 *accommodatus* (canvas 913); 1747, 1750; Gaffiot *accommŏdātus*; your settled *accommod-* (the draft's form is not Latin) |
| gangrenae | gangraenae | word | 2:17 | 1573 *gangrænæ* (canvas 913); 1556, 1758; Gaffiot *gangræna* (the draft's form is in no dictionary) |

**Decision:** propose (Claude, 2026-11-11; for your approval)
