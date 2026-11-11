# Titus 1–3, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of 2 Corinthians (`data/review/2cor1-13-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvas 915 holds the whole letter, its title and
  Athanasius's argument at the foot of 914). 1556 is the reference: where it reads otherwise, its reading is recorded
  as a variant (section 5); its e-rara OCR runs Titus and Philemon together across two columns (pages 10282437–38),
  so it reaches only some places (hardly 1:3–4, not 3:1–2). Stage 1 drafted Wikisource's Titus as
  **`text/draft/TIT.usfm`** (BSB paragraphs). You have no earlier work on Titus; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Titus is the early wording**, as its Galatians and Colossians: *favor* for *gratia* (3:15),
  *Haereticum* for *Sectarium* (3:10), *et* for *ac* (2:4), *omnes* without *homines* (3:2), *omnem rem bonam* for
  *omne bonum opus* (1:16), with slips of its own (*cogitionem*, *decent docrinam*, *postestatibus*,
  *Exspectatntes*). 1556 has the revised reading wherever its OCR can be read, except 1:16, where it reads *omnem rem
  bonam* with Wikisource: *omne bonum opus* is 1573's (section 5). 1573 keeps *humanitas* (3:4), *beneficentia*
  (2:11), *beneficio* (3:7) and *Certa res est* (3:8); so does the text.
- **Versification** (decision 5): the draft is at the KJV counts (47 verses), no edits file. 1573 prints every verse
  number and agrees with the draft's numbering everywhere but **3:5–6**: 1573 prints 6 before *quo nos large
  perfudit*, so *renovationisque Spiritus Sancti* closes 5, as the KJV's 3:5 (*and renewing of the Holy Ghost*); the
  draft starts 6 with it. Moved back to 5 (section 2c).
- **Collation** (`python -m pipeline collate Titus 1-3`; `data/calibration/Titus1-3-collation.tsv`, 66 places: 16
  *correct*, 1 *others-1573-agrees*, 2 *others*, 46 *base-only* (29 reading, 11 division, 3 f/s, 2 spelling, 1 edge),
  1 *uncovered*), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/Titus.*`,
  23): every reading where 1573 and another printing agree against Wikisource, the two where others do (2:1, 2:11),
  every base-only reading whose 1573 words are Latin (1:14 *veritatem*, 1:16 *opus*, 3:2 *homines*, 3:10 *Sectarium*,
  3:13 *desit*), and the edge at 3:5–6 (*renovationisque*, section 2c). The rest of the base-only readings are 1573's
  OCR (*tpa* for the abbreviated *tempora*, *téporibus*, *neinini*, *cuctis*), word breaks at line ends (*atti net*,
  *ha bens*, *purga ret*), note letters and margin notes run into the text (1:12 *a Epimeni*, 1:13 *tis*, 2:8 *Ephes.
  5.22 Coloss. 3.22 … 2. Pet. 2. 8*, 3:10 *et vitiose se-*, 3:11 *c sua culpa*, 3:12 *perstet*) and the line of the
  chapter summary run into 2:9 (*esse studium pie et recte vivendi*). Each place was also read against 1556 (its
  e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **The uncovered verse** 2:1 (1573's OCR 43% of the words, under the chapter's initial T) was read whole on the
  image: *TV verò loquere quæ ſanã deceant doctrinam.* (crop `Titus.2.1-deceant`). It differs from the draft only in
  *deceant doctrinam*, already a collation place (section 1).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *fidi*,
  *fidentes*, *filio*, *fabulis*, *faciant*, *feminas*, *fuimus*, *futiles/sutiles*, *confidunt/considunt*) was read in
  its verse: all are *f*. Every *s* word whose *f*-form is Latin (*si/fi*, *sani/fani*, *sana*, *servi*, *desit/defit*):
  all are *s*, and the three places where 1573's OCR has the *f* (1:6 *ſi quis*, 2:2 *patientia ſani*, 3:13 *ne quid
  eis deſit*) read *ſ* on the image. None found.
- **In all, 16 corrections**: 8 Wikisource slips (section 1), 5 readings of Castellio's revised text (section 2), 1
  verse boundary (section 2c), 2 word divisions (section 3). Spellings (*caussa*, *numquam*, *quum*, *idcirco*,
  *caritate*, *exstitit*, *Exspectantes*, *exserentes*, *hiemare*, *heredes*, *obedientes*, *eis*) are left to stage 3
  (decision 37's and 42's rules); one ad- word without a rule yet is proposed (section 6). One place where 1573 reads
  against 1556 is recorded (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (8)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Titus 1:1** *et veritatis cogitionem* → *cognitionem*. 1573 *& veri-tatis cognitionem* (canvas 915); 1556 (*ueritatis cogni-*), 1758, 1681, 1747, 1750, 1726 (τῆς ἐπιγνώσεως).
   **Apply:** `Titus.1.1` la: `veritatis cogitionem` → `veritatis cognitionem`
2. **Titus 1:4** *pacem a Deo et Domino* → *pacem a Deo patre et Domino*. 1573 *pacem à Deo patre, & Domino Ieſu Chriſto* (canvas 915; ἀπὸ θεοῦ πατρὸς); 1758, 1681, 1715, 1747, 1750. 1556's OCR does not reach the verse. The comma is left to stage 3.
   **Apply:** `Titus.1.4` la: `pacem a Deo et Domino` → `pacem a Deo patre et Domino`
3. **Titus 1:14** *hominumque praeceptis, veritatis aversantium* → *veritatem aversantium*. 1573 *hominumq; præce-ptis, veritatem auerſantium* (canvas 915; ἀποστρεφομένων τὴν ἀλήθειαν, *āversor* with the accusative); 1556 (OCR *ueritate suet-fantíum*), 1758, 1715, 1747, 1750.
   **Apply:** `Titus.1.14` la: `praeceptis, veritatis aversantium` → `praeceptis, veritatem aversantium`
4. **Titus 1:16** *factis negant, et contumaces* → *factis negant, nefarii, et contumaces*. 1573 *& eũdem factis negant, / nefarij, & contumaces* (canvas 915; βδελυκτοὶ ὄντες); 1556 (*nefarij*), 1758, 1715, 1750, 1726. Wikisource alone drops it.
   **Apply:** `Titus.1.16` la: `factis negant, et contumaces` → `factis negant, nefarii, et contumaces`
5. **Titus 2:1** *quae sanam decent docrinam* → *quae sanam deceant doctrinam*. 1573 *TV verò loquere quæ ſanã deceant doctrinam.* (canvas 915; the uncovered verse, read whole; the subjunctive of the relative clause of character, ἃ πρέπει); 1556 (OCR *deceái dot-*), 1758, 1715, 1750. Two slips in Wikisource's line.
   **Apply:** `Titus.2.1` la: `sanam decent docrinam` → `sanam deceant doctrinam`
6. **Titus 2:13** *Exspectatntes speratam* → *Exspectantes speratam*. 1573 *expectantes ſperatam beatitudinem* (canvas 915); 1556 (*expe-ctantes*), 1758, 1681, 1747, 1750, 1726. The *exsp-* is Wikisource's spelling and the approved stem rule's (*expect → exspect*).
   **Apply:** `Titus.2.13` la: `Exspectatntes speratam` → `Exspectantes speratam`
7. **Titus 2:14** *ab omni sceleri vindicaret* → *ab omni scelere vindicaret*. 1573 *quo nos ab omni / ſcelere vindicaret* (canvas 915); 1758, 1681, 1747, 1750, 1726 (1556's OCR *abomniífceler*).
   **Apply:** `Titus.2.14` la: `ab omni sceleri vindicaret` → `ab omni scelere vindicaret`
8. **Titus 3:1** *magistratibus et postestatibus* → *et potestatibus*. 1573 *vt magiſtratibus & poteſta-tibus pareant* (canvas 915); 1758, 1681, 1715, 1750, 1726.
   **Apply:** `Titus.3.1` la: `et postestatibus pareant` → `et potestatibus pareant`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (5)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read, except 1:16 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Titus 1:16** *et ad omnem rem bonam inepti* → *et ad omne bonum opus inepti*. 1573 *& ad omne bonũ opus inepti* (canvas 915, the bar for *m* on the image), πρὸς πᾶν ἔργον ἀγαθὸν; 1758, 1726. **1556** *ad omnem rem bonam* (OCR *alomnemiembonáincpi*), with Wikisource, 1715, 1750: a 1573 change (section 5). For your eye.
   **Apply:** `Titus.1.16` la: `ad omnem rem bonam inepti` → `ad omne bonum opus inepti`
2. **Titus 2:4** *suorum virorum et liberorum* → *suorum virorum ac liberorum*. 1573 *ſuorum virorum ac / liberorum amantes eſſe* (canvas 915); 1556 (OCR *uíroiif ac libétorunm*), 1758, 1726. The early line *et* (Wikisource, 1681, 1715, 1747, 1750).
   **Apply:** `Titus.2.4` la: `virorum et liberorum` → `virorum ac liberorum`
3. **Titus 3:2** *summam erga omnes comitatem* → *summam erga omnes homines comitatem*. 1573 *ſummam erga omnes homines comitatem / exerentes* (canvas 915; πρὸς πάντας ἀνθρώπους); 1681 (OCR *omncshomij*), 1726. The early line without it (Wikisource, 1747, 1750); 1758's OCR breaks off after *omnes*, and 1556's OCR does not reach the verse.
   **Apply:** `Titus.3.2` la: `erga omnes comitatem` → `erga omnes homines comitatem`
4. **Titus 3:10** *Haereticum hominem* → *Sectarium hominem*. 1573 *ᵇ Sectarium hominem poſt vnam atq; alteram* (canvas 915; margin *b vitiosæ sectæ addictũ*), αἱρετικὸν; 1556 (OCR *b Secizrium*, with the same note letter), 1758, 1681. The early line *Haereticum* (Wikisource, 1747, 1750).
   **Apply:** `Titus.3.10` la: `Haereticum hominem` → `Sectarium hominem`
5. **Titus 3:15** *Adsit vobis omnibus favor* → *gratia*. 1573 *Adſit vobis omnibus gratia: Amen.* (canvas 915), ἡ χάρις; 1556 (OCR *grata*), 1758. The early line *favor* (Wikisource, 1715, 1747, 1750), as Gal 6:18 and Col 4:18.
   **Apply:** `Titus.3.15` la: `omnibus favor:` → `omnibus gratia:`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the *f* (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The uncovered verse 2:1 was read whole on the image (intro): its only difference from the draft, *deceant
doctrinam*, is already section 1's item 5. No decision needed.

## 2c. Verse boundary (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; read on the 1573 page image)

1. **Titus 3:5–6**: *renovationisque Spiritus Sancti* closes 5. 1573 *lauacro ᵃ renaſcentiæ, / renouationisq; ſpiritus ſancti, / 6 quo nos largè perfudit* (canvas 915; margin *a quo renascimur, & à spiritu sancto renovamur*); 1681 and 1726 also print 6 before *Quo*, and the KJV's 3:5 has *and renewing of the Holy Ghost* (ἀνακαινώσεως πνεύματος ἁγίου). Wikisource starts 6 with it (1750 and 1758, aligned to the draft, cannot show where their 6 stands). The capital is Wikisource's, left to stage 3.
   **Apply:** `Titus.3.5` la: `lavacro renascentiae` → `lavacro renascentiae, renovationisque Spiritus Sancti,`
   **Apply:** `Titus.3.6` la: `Renovationisque Spiritus Sancti, quo nos` → `Quo nos`

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **Titus 2:5** *castas, domimanentes, bonas* → *domi manentes*. 1573 *frugi, caſtas, domi manentes, bonas* (canvas 915, apart on the image; οἰκουργούς); 1556 (*domí manétes*), 1758, 1681, 1715, 1750, 1726.
   **Apply:** `Titus.2.5` la: `castas, domimanentes, bonas` → `castas, domi manentes, bonas`
2. **Titus 2:7** *In cunctis teipsum recte* → *te ipsum*. Your settled *tē ipsum* / *tē ipsō* (16×: Matthew, Mark, Luke, John, Acts) against *teipsum* 4× (Romans 3×, and Gal 5:14 in the quotation kept joined), as the *sē ipsum* division of Galatians and Ephesians. Not a quotation. 1573 joins it (*teipſum*, canvas 915). For your eye.
   **Apply:** `Titus.2.7` la: `In cunctis teipsum recte` → `In cunctis te ipsum recte`

## 4. Checked and kept

- **3:5–6**: no words missing (versification, above).
- **1:16** *Deum se scire profitentur*: 1573 *profitẽtur* (canvas 915, the bar for *n*; its OCR *profitetur*). Agrees.
- **3:2** *comitatem exserentes*: 1573 *exerentes* (canvas 915, on the image; its OCR lost the line), with 1681, 1726;
  Wikisource and 1750 *exserentes*. One word (Gaffiot *exserō*); the spelling to stage 3. Kept.
- **3:11** *ut ipse a se ipso damnetur*, **2:14** *Qui se ipsum*: 1573 joins them (*ſeipſo*, *ſeipſum*); the draft
  already divides them. Kept.
- **1:5** *idcirco*: 1573 *iccirco* (canvas 915), with 1681; Gaffiot *idcircō*, with 1758, 1750 and Wikisource. Kept.
- **3:4** *benignitas et humanitas*, **2:11** *divina beneficentia*, **3:7** *ejus beneficio*, **3:8** *Certa res est*:
  1573 prints them (canvas 915, 2:11 *Extitit enim diuina beneficentia* on the image). Not the early wording
  1556/1573 revised elsewhere. Kept.
- **The f/s places** 1:6 *Si quis*, 2:2 *patientia sani*, 3:13 *ne quid eis desit*: long s on the image (intro). Kept.
- **Note letters and margin notes**, not text: 1:12 *a* (*Epimenides, qui fuit ipse Cretensis*), 2:7 *a*, 3:5 *a*
  (*quo renascimur, & à spiritu sancto renovamur*), 3:10 *b* (*vitiosæ sectæ addictum*), 3:11 *c* (*sua culpa
  pereat, qui in errore perstet*); the references 1:15 *Rom. 14. 20*, 2:8 *Ephes. 5. 22, Coloss. 3. 22, 2. Pet. 2. 8*;
  the chapter summaries before 1:1, 2:1 and 3:1 (*Docet quales oporteat ministros eligere …*), whose last line the
  OCR ran into 2:9.
- **3:15** the subscription (*Scripta Nicopoli Macedoniae*): 1573 sets it in italics under the verse (canvas 915,
  *Scripta Nicopoli Macedoniæ*). Set apart as `\cls` at stage 3 (decision 37).
- **Punctuation and capitals, left to stage 3**: 1:3 *commissum est.* (1573 a comma, the sentence running on into 1:4),
  1:4 *patre,*, 1:10 *oportet.* (1573 a colon), 2:2 *frugi;* (1573 a colon), 2:12 *impietati,*, 3:1 *faciant,* (1573 a
  colon), 3:5 the comma after *renascentiae* (section 2c), 3:11 *Sciens,*, 3:12 *cura,*.
- **Spellings, left to stage 3** (decision 37's and 42's rules, and section 6): *caussa* (1573 *cauſa*), *numquam*
  (1573 *nunquam*), *coniuncta*, *quum* (1573 *Cùm*), *caritate* (1573 *chari-tate*), *feminas* (1573 *fœminas*),
  *obedientes*, *Exstitit*, *exstitit* (1573 *Extitit*, *extitit*), *Exspectantes* (1573 *expectantes*), *saeculo* (1573
  *ſeculo*), *auctoritate* (1573 *authoritate*), *adseverare* (1573 *aſſeuerare*; section 6), *heredes* (1573
  *hæredes*), *hiemare* (1573 *hyemare*), *eis*, *Judaicis*, *Jesu*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image; it does not reach 1:3–4 or 3:1–2.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| Titus 1:16 | *ad omne bonum opus inepti* | = | *ad omnem rem bonam inepti* | Wikisource, 1715, 1750 with 1556; 1758, 1726 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-11)

## 6. Spelling rules proposed

Decision 37 assimilates *ad-* (compounds of *sum*, *adnuntio* and names excepted) word by word; one Titus form has
no rule yet. Proposed, not added to `data/rules/orthography.tsv`:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| *adseverare* | *asseverare* | word | 3:8 | 1573 *aſſeuerare* (canvas 915); 1758, 1681, 1726; Gaffiot *adsĕvērō* (the lexicon has *assevērāre* too); as the approved *adseratur* → *asseratur*. Your settled text has no form of the verb |

(3:15 *Adsit* is a compound of *sum*, left as it is; *adiutor* and *adversarii* do not assimilate.)

**Decision:** propose (Claude, 2026-11-11; for your approval)
