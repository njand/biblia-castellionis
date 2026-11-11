# 2 Thessalonians 1–3, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of Galatians (`data/review/gal1-6-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 907–908: the argument and 1:1–2:7 on 907,
  2:8–3:18 on 908). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant (section 5).
  Stage 1 drafted Wikisource's 2 Thessalonians as **`text/draft/2TH.usfm`** (BSB paragraphs). You have no earlier
  work on 2 Thessalonians; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the witness
  `1726`, read as an OCR.
- **Wikisource's 2 Thessalonians is the early wording**, as its Romans, Corinthians and Galatians: *favor* for
  *gratia* (3:18), *Ad quas* for *Ad quod* (2:14), *Deus paterque* for *Deus pater* (2:16), *et nihil agere, sed
  supervacanea agere* for *nihil agentes, sed supervacanea agentes* (3:11). 1556 already has every one of these
  revisions. 1573's own changes against 1556 are 1:6 *sicut affligentibus* (1556 *ut*) and 2:13 *fidemque veritatis*
  (1556 *verique fidem*), both with Wikisource on 1556's side (section 5). 1:2 *Gratiam* and 2:16 *pro suo favore*
  are 1573's too.
- **Versification** (decision 5): the draft is at the KJV counts (47 verses), no edits file. 1573 (canvases 907–908)
  numbers every verse as the KJV (its 3:8 number is lost in the margin references, *1. Thess. 2. 9*, but the verse
  opens its line at *vt ne victum*). Nothing to move.
- **Collation** (`python -m pipeline collate 2Thess 1-3`; `data/calibration/2Thess1-3-collation.tsv`, 78 places: 19
  *correct*, 8 *others-1573-agrees*, 4 *others*, 47 *base-only* (30 reading, 6 division, 6 spelling, 3 edge, 2
  f/s), no *uncovered* verse), with the edge and f/s checks. Read on the page image (crops in
  `sources/mdz-1573/crops/2Thess.*`, 18): every reading where 1573 and another printing agree against Wikisource,
  the 4 where others do, the base-only places whose 1573 words are Latin (1:6 *sicut*, 2:13 *fidemque veritatis*,
  1:11 *in quẽ*), and the edge places (2:8 *claritate delebit*, 2:17 *confirmet*, 1:12 *beneficentia*, 3:18 *gratia:
  Amen. Scripta Athenis*: line ends and the last line of the book, which 1573's OCR lost; all printed). The rest of
  the base-only readings are 1573's OCR (*aded*, *inysterium*, *cuinque*, *Domin*), word breaks at line ends (*per
  ficiatque*, *credide rint*), margin notes run into the text (*Dei contemptoribus*, *omnes fidentes & veri
  Christiani*, *Mar. 24. 25*). Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`, page
  10282433) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Whole verses read against 1573's page text** (`mdz.page_text`, canvases 907–908), verse by verse: nothing beyond
  the collation's places.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide*, *fides*,
  *fidentibus*, *fore*, *fuerit*, *fuerint*, *fuerimus*, *falsorum*, *defectio*) was read in its verse: all are *f*.
  Every *s* word whose *f*-form is Latin (*si*, *simus*, *sui*, *confidimus*): all are *s*, and the two places where
  1573's OCR has the *f* (3:7 *simus*, 3:14 *si*) read *ſ* on the image. None found.
- **In all, 14 corrections**: 8 Wikisource slips (section 1), 6 readings of Castellio's revised text (section 2).
  Applied to the draft under decision 30's standing rule once accepted. Spellings are left to stage 3 (decision 37's
  rules); four ad- forms without a rule are proposed (section 6).

## 1. Wikisource slips: 1573 and the other printings agree against it (8)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **2 Thessalonians 1:5** *ut justo Deo judicio* → *justo Dei judicio*. 1573 *vt iuſto Dei iudicio diuinũ regnum* (canvas 907); 1556, 1758, 1681, 1747, 1750, 1726.
   **Apply:** `2Thess.1.5` la: `justo Deo judicio` → `justo Dei judicio`
2. **2 Thessalonians 1:8** *supplicium interrogaturus* → *supplicium irrogaturus*. 1573 *ſupplicium irrogaturus ᵃ ne-ſcientibus Deum* (canvas 907; margin *a Dei contemptoribus*); 1556, 1758, 1681, 1747, 1750.
   **Apply:** `2Thess.1.8` la: `supplicium interrogaturus` → `supplicium irrogaturus`
3. **2 Thessalonians 1:10** *in danctis suis* → *in sanctis suis*. 1573 *in illa die in ſanctis ſuis illuſtre-tur* (canvas 907); 1556, 1747, 1750, 1726.
   **Apply:** `2Thess.1.10` la: `in danctis suis` → `in sanctis suis`
4. **2 Thessalonians 1:11** *in quem vocati esti* → *vocati estis*. 1573 *eo in quẽ vocati eſtis, ſtatu* (canvas 907); 1556, 1758, 1681, 1715, 1747, 1726.
   **Apply:** `2Thess.1.11` la: `vocati esti, statu` → `vocati estis, statu`
5. **2 Thessalonians 2:2** *de sententia demoveamini* → *dimoveamini*. 1573 *ne citò de ſententia dimoueamini* (canvas 907); 1556 (*dímoueaminí*), 1758, 1681, 1715, 1747, 1750, 1726. Every printing has *dimoveo*.
   **Apply:** `2Thess.2.2` la: `de sententia demoveamini` → `de sententia dimoveamini`
6. **2 Thessalonians 2:8** *ille sclerosus* → *ille scelerosus*. 1573 *tum demum exiſtet ille ſceleroſus* (canvas 908), as 2:9 *scelerosi*; 1556, 1758, 1681, 1747, 1750.
   **Apply:** `2Thess.2.8` la: `ille sclerosus` → `ille scelerosus`
7. **2 Thessalonians 2:16** *aeternoqye solatio* → *aeternoque solatio*. 1573 *æter-noq; ſolatio* (canvas 908); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `2Thess.2.16` la: `aeternoqye solatio` → `aeternoque solatio`
8. **2 Thessalonians 3:11** *quosdam qpud vos* → *quosdam apud vos*. 1573 *quoſdã apud vos* (canvas 908); 1556, 1758, 1681, 1715, 1747, 1750, 1726.
   **Apply:** `2Thess.3.11` la: `quosdam qpud vos` → `quosdam apud vos`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (6)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in form. 1556 has the
revised reading too wherever its OCR can be read, except 1:6 and 2:13 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **2 Thessalonians 1:6** *ut a Deo reddatur, ut adfligentibus vos adflictio* → *sicut adfligentibus*. 1573 *vt à Deo reddatur, ſicut af-fligentibus vos afflictio* (canvas 907, on the image), answering 1:7 *Sic vobis*; 1758, 1726. **1556** *ut*, with Wikisource, 1747, 1750: a 1573 change (section 5). For your eye. The spelling *aff-* is stage 3's (section 6).
   **Apply:** `2Thess.1.6` la: `reddatur, ut adfligentibus` → `reddatur, sicut adfligentibus`
2. **2 Thessalonians 2:13** *per Spiritus sanctimoniam, verique fidem* → *fidemque veritatis*. 1573 *per ſpiritus ſanctimo-niam, fidemq; veritatis* (canvas 908, on the image), πίστει ἀληθείας. **1556** *verique fidem* (OCR *ueríq fidem*), with Wikisource, 1715, 1747, 1750: a 1573 change (section 5); the OCRs of 1758, 1681 and 1726 lose the words. For your eye.
   **Apply:** `2Thess.2.13` la: `sanctimoniam, verique fidem.` → `sanctimoniam, fidemque veritatis.`
3. **2 Thessalonians 2:14** *Ad quas vos vocavit* → *Ad quod vos vocavit*. 1573 *ad quod vos vocauit per Euangelium* (canvas 908), εἰς ὃ; 1556, 1758, 1681. The early line *quas* (Wikisource, 1715, 1747, 1750).
   **Apply:** `2Thess.2.14` la: `Ad quas vos` → `Ad quod vos`
4. **2 Thessalonians 2:16** *et Deus paterque noster* → *et Deus pater noster*. 1573 *& Deus pater noſter, qui nos* (canvas 908, on the image); 1556, 1758, 1681, 1726. The early line *paterque* (Wikisource, 1715, 1747, 1750).
   **Apply:** `2Thess.2.16` la: `Deus paterque noster, qui` → `Deus pater noster, qui`
5. **2 Thessalonians 3:11** *immodeste vivere, et nihil agere, sed supervacanea agere* → *immodeste vivere, nihil agentes, sed supervacanea agentes*. 1573 *immodeſtè vi-uere, nihil agentes, ſed ſuperuacanea agentes* (canvas 908, on the image), μηδὲν ἐργαζομένους ἀλλὰ περιεργαζομένους; 1556, 1758, 1726 (1681's OCR stops at *nihil*). The early line *et nihil agere … agere* (Wikisource, 1715, 1747, 1750).
   **Apply:** `2Thess.3.11` la: `vivere, et nihil agere, sed supervacanea agere.` → `vivere, nihil agentes, sed supervacanea agentes.`
6. **2 Thessalonians 3:18** *Jesu Christi favor: Amen.* → *gratia: Amen.* 1573 *Adſit vobis omnibus Domini noſtri Ieſu Chriſti gratia: Amen.* (canvas 908, the book's last line, read on the image), ἡ χάρις; 1556, 1758, 1681, 1726. The early line *favor* (Wikisource, 1715, 1747, 1750), as 1 Thessalonians 5:28.
   **Apply:** `2Thess.3.18` la: `Christi favor: Amen.` → `Christi gratia: Amen.`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the *f* (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

No verse is uncovered. The places 1573's OCR lost at line ends and at the foot of the book (2:8, 2:17, 1:12, 3:18)
were read on the image (crops `2Thess.2.8-claritate`, `2Thess.2.17-confirmet`, `2Thess.1.12-beneficentia`,
`2Thess.3.18-gratia`): they agree with the draft but for 3:18's *gratia* (section 2). No decision needed.

## 3. Word division (0)

None proposed (see section 4 for 1:4 *nos ipsi* and 2:5 *Annon*).

## 4. Checked and kept

- **1:4** *Ut nos ipsi de vobis gloriemur*: 1573 *noſipſi* (canvas 907), with 1758, 1726; your settled *nōs ipsōs*
  (10×), never joined. Kept apart.
- **2:5** *Annon meministis*: 1573 *An non* (canvas 907), with 1556 and 1758; 1750 *Annon*. Your settled text has
  both (*an nōn* 14×, *annōn* 8×). Kept as the draft; for your eye (one spelling for the edition).
- **1:12** *pro Dei nostri et Domini Jesu Christi beneficentia*: 1573 *pro* (canvas 907), with 1556, 1681, 1715,
  1747; 1758, 1726 *per*. Kept.
- **2:16** *pro suo favore adamavit*: 1573 *fauore* (canvas 908), with 1556 and every printing; not the early
  *favor* of 3:18. Kept.
- **1:11** *eo, in quem vocati estis*: 1573 *in quẽ* (canvas 907, the bar; its OCR *que*), 1556 *qué*. Kept.
- **3:14** *non obtemperat*: 1573 *nó* (the bar; its OCR *no*). Kept.
- **Note letters and margin notes**, not text: 1:8 *a* (*Dei contemptoribus*), 2:6 *a* (before *exsistat*); the glosses
  at 3:2 (*omnes fidentes, & veri Christiani*); the references (*Mar. 24. 25*, *1. Tim. 4*, *1. Thess. 2. 9*, *Gal.
  6. 9*); and 1573's annotations after chapters 1 (on 1:9) and 2 (on 2:9).
- **3:18** the subscription (*Scripta Athenis*): 1573 sets it in italics under the verse (canvas 908). Set apart as
  `\cls` at stage 3 (decision 37).
- **1:1** *Silvanus*, *Timotheus*: 1573 *SYLVAnus*, *Thimotheus* (canvas 907). Left to stage 3 (1 Thessalonians 1:1
  has *Sylvanus*); for your eye.
- **Punctuation, left to stage 3**: 2:8 *sclerosus:* (1573's colon), 2:13 *veritatis,* (1573 runs on into 14).
- **Spellings, left to stage 3** (decision 37's rules, and section 6): *exsistet*, *exsistat* (1573 *exiſtet*,
  *exiſtat*), *quidquid* (1573 *quicquid*), *tamquam*, *quicumque* (1573 *tanquam*, *quicunque*), *caritas*,
  *caritatem* (1573 *charitas*, *charitatem*), *auctores* (1573 *authores*), *caussa* (1573 *cauſa*; the approved
  *caussa* → *causa*), *Denuntiamus* (1573 *Denunciamus*), *quum* (1573 *cum*; decision 41), *obedientibus* (the
  approved stem *obedi-* → *oboedi-*), *caelo* (1573 *cœlo*).

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656, page 10282433), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 2 Thess 1:6 | *sicut adfligentibus* | = | *ut affligentibus* | Wikisource, 1747, 1750 with 1556; 1758, 1726 with 1573 |
| 2 Thess 2:13 | *sanctimoniam, fidemque veritatis* | = | *sanctimonium, verique fidem* | Wikisource, 1715, 1747, 1750 with 1556 |

(1556's *sanctimonium* at 2:13 is as its OCR reads, *(anciímonium*; not checked on its page image.)

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted); these forms have no row in
`data/rules/orthography.tsv` yet (checked with `normalize.word_rules()`). Proposed, not added to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| *adfligentibus* | *affligentibus* | word | 1:6 | 1573 *af-fligentibus* (canvas 907); 1556, 1758, 1726; as the approved *adflixit* → *afflixit* |
| *adflictio* | *afflictio* | word | 1:6 | 1573 *afflictio* (canvas 907); 1556, 1758, 1747; as the approved *adflictionem* → *afflictionem* |
| *adfligimini* | *affligimini* | word | 1:7 | 1573 *affligimini* (canvas 907); 1556, 1681, 1747; your settled *afflīgimur* |
| *adgregationem* | *aggregationem* | word | 2:1 | 1573 *aggregationem* (canvas 907); 1556, 1681, 1715, 1747, 1726; as the approved *adgregare* → *aggregare*; your settled *aggregātus* |

**Decision:** propose (Claude, 2026-11-11; for your approval)
