# Philemon 1, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-11 (decision 30's standing rule), on the route of 2 Corinthians (`data/review/2cor1-13-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvas 916 holds the whole letter, after its title
  and Athanasius's argument). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant
  (section 5); its e-rara OCR runs Philemon into Titus's columns (pages 10282438–39), so it reaches 1:1–6 in pieces,
  1:7–15 only in scraps (1:10 *Onefimo*, 1:14 *nihil uolui facere*) and 1:16–25. Stage 1 drafted Wikisource's Philemon as **`text/draft/PHM.usfm`** (BSB paragraphs). You
  have no earlier work on Philemon; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the
  witness `1726`, read as an OCR (it reaches 1:1–7 only, in part).
- **Wikisource's Philemon is the early wording**, as its Titus and Colossians: *favor* for *gratia* (1:25), *mei
  intimum* for *mihi intimum* (1:12), *recreati sint* for *sunt* (1:7), each with 1750 against 1573. It has no slips
  the other printings correct, but for a missing space (1:19). 1556 has *gratia* at 1:25; its OCR does not reach 1:7
  or 1:12.
- **Versification** (decision 5): the draft is at the KJV count (25 verses), no edits file. 1573 prints every verse
  number and agrees with the draft's numbering everywhere (1:11 *eo qui*, its OCR *In eo*, reads the numeral *11* as
  a word).
- **Collation** (`python -m pipeline collate Phlm 1`; `data/calibration/Phlm1-1-collation.tsv`, 33 places: 7
  *correct*, 1 *others-1573-agrees*, 25 *base-only* (12 reading, 4 division, 4 f/s, 4 spelling, 1 edge), no
  *uncovered* verse), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/Phlm.*`,
  10): every base-only reading whose 1573 words are Latin (1:7 *ſunt*, 1:12 *mihi*, 1:25 *gratia*), the f/s places
  and the edge (1:11 *In*, the numeral). The *correct* places are spellings (*charo*, *charitate*, *afficimur*), a line
  break (1:18 *im-putato*) and 1573's argument line run into 1:1; the rest of the base-only readings are 1573's OCR (*nottro*, *quantuin*,
  *vinetus*, *ineis*, *queın*, *ineum*) and word breaks (*Archip po*, *perte*, *tibialiquando*, *plusetiam*,
  *collegamei*, *ve stris*). Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and the
  archive.org printings (1758, 1681, 1715, 1747, 1750).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *filio*,
  *faciens*, *fore/sore*, *fuit/suit*) was read in its verse: all are *f*. Every *s* word whose *f*-form is Latin
  (*si/fi*, *sis/fis*, *sit/fit*, *socium/focium*): all are *s*, and the four places where 1573's OCR has the *f* (1:6
  *quantum ſit in vobis boni*, 1:17 *Quare ſi me ſocium*, 1:18 *Quòd ſi quid*) read *ſ* on the image; 1:6 was fetched
  again at a larger size (crop `Phlm.1.6-sit-zoom`): *fiat* before it has the crossbar of the fi ligature, *ſit* none.
  None found.
- **In all, 5 corrections**: 3 readings of Castellio's revised text (section 2), 2 word divisions (section 3).
  Spellings (*caro*, *carissimae*, *carissimum*, *caritate*, *adficimur*, *intelligatur*, *quum*, *auctoritatem*,
  *obedientia*) are left to stage 3 (decision 37's and 42's rules); no rule is wanting (section 6). No place where
  1573 reads against 1556 was found (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (0)

None: where 1573 and the other printings agree against Wikisource the difference is a spelling (*charo*,
*charitate*, *afficimur*), left to stage 3. No decision needed.

## 2. Castellio's revised wording: 1573 against Wikisource's early line (3)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11; every item read on the 1573 page image)

1. **Philemon 1:7** *per te, frater, recreati sint* → *recreati sunt*. 1573 *quòd ſanctorum animi per te, frater, / recreati ſunt.* (canvas 916, the u clear on the image; the indicative of the fact, ὅτι … ἀναπέπαυται); 1681 (OCR *funt*). The early line *sint* (Wikisource, 1750; 1715's OCR *finr*). 1758's OCR loses the word; 1556's does not reach the verse.
   **Apply:** `Phlm.1.7` la: `recreati sint.` → `recreati sunt.`
2. **Philemon 1:12** *hoc est, mei intimum recipe* → *hoc est, mihi intimum*. 1573 *Tu verò eum, hoc eſt, mihi intimum, recipe:* (canvas 916; τὰ ἐμὰ σπλάγχνα, *intimus* with the dative, my close friend); 1758, 1681, 1715. The early line *mei* (Wikisource, 1750). 1556's OCR does not reach the verse.
   **Apply:** `Phlm.1.12` la: `hoc est, mei intimum` → `hoc est, mihi intimum`
3. **Philemon 1:25** *Domini nostri Jesu Christi favor adsit* → *gratia*. 1573 *Domini noſtri Ieſu Chriſti gratia adſit animis ve-ſtris: Amen.* (canvas 916), ἡ χάρις; 1556 (*gratia adíit*, OCR), 1758, 1681. The early line *favor* (Wikisource, 1747, 1750), as Titus 3:15 and Gal 6:18.
   **Apply:** `Phlm.1.25` la: `Christi favor adsit` → `Christi gratia adsit`

## 2a. Found by the f/s sweep (0)

None: every *f* and *s* word whose other form is Latin was read in its verse, and on the image where 1573's OCR has
the *f* (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

No verse is uncovered: 1573's OCR reaches every verse. Each verse was also read whole against 1573's page text
(canvas 916); nothing beyond the collation's places differs. No decision needed.

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-11)

1. **Philemon 1:19** *scripsi mea manu,ego dissolvam* → *mea manu, ego dissolvam*. A space after the comma, as everywhere else in the draft; 1573 *ſcripſi mea manu, ego diſſoluam* (canvas 916), 1758, 1681, 1715, 1747, 1750. The OCR tokens join the two words otherwise.
   **Apply:** `Phlm.1.19` la: `mea manu,ego dissolvam` → `mea manu, ego dissolvam`
2. **Philemon 1:19** *quod tu mihi etiam teipsum debes* → *te ipsum*. Your settled *tē ipsum* / *tē ipsō* (16×: Matthew, Mark, Luke, John, Acts) against *teipsum* 4× (Romans 3×, and Gal 5:14 in the quotation kept joined), as the *sē ipsum* division of Galatians and Ephesians, and Titus 2:7. Not a quotation. 1573 joins it across the line (*tei-/pſum*, canvas 916). For your eye.
   **Apply:** `Phlm.1.19` la: `etiam teipsum debes` → `etiam te ipsum debes`

## 4. Checked and kept

- **1:6** *quantum sit in vobis boni*: 1573 *ſit* on the enlarged image (its OCR *fit*); the indirect question after
  *intelligatur*. Kept.
- **1:11** *Eo, qui tibi aliquando fuit inutilis*: 1573 *11 eo qui tibi aliquando fuit inutilis* (canvas 916, on the
  image); its OCR read the numeral as *In*. Agrees.
- **1:17** *accipe eum ut me*, **1:18** *id mihi imputato*: 1573 *accipe eum, vt me*, *id mihi im-/putato* (on the
  image), with 1758, 1681, 1750 (1715 and 1747 *accipe ut me* and *tu mihi*). Kept.
- **1:9** *talis ego, hoc est, Paulus senex*, **1:15** *Fortassis*, **1:16** *carnis et dominicae religionis nomine*:
  1573 prints them (*Fortaſsis*, *Dominicæ*). Agrees.
- **1:25** the subscription (*Missa est Roma, per Onesimum servum*): 1573 sets it in italics under the verse (canvas
  916, *Miſſa eſt Roma, per Oneſimum ſeruum*; the crop shows only the tops of the letters). Set apart as `\cls` at
  stage 3 (decision 37).
- **Punctuation and capitals, left to stage 3**: 1:1 *Paulus,* and *Philemoni,* (1573 without the commas), 1:5
  *omnes* and 1:6 *boni* (the draft without stops; 1573 *omnes,* and *boni.*), 1:9 *vinctus:* (1573 a full stop),
  1:12 *intimum recipe* (1573 *intimum, recipe*), 1:17 *eum ut* (1573 *eum, vt*), 1:21 *sciens,* and 1:22 *fore,*
  (1573 without the commas), 1:23 *Epaphras,* (1573 without), 1:16 *dominicae* (1573 *Dominicæ*).
- **Spellings, left to stage 3** (decision 37's and 42's rules): *caro*, *carissimae*, *carissimum*, *caritate*,
  *caritatem* (1573 *charo*, *charifsime*, *chariſsimum*, *charitate*), *adficimur* (1573 *afficimur*), *intelligatur*,
  *quum* (1573 *cùm*), *auctoritatem* (1573 *authoritatem*), *obedientia*, *adiutorique* (1573 *adiutoriq;*),
  *laesit* (1573 *lęſit*), *Onesimo*, *evangelii*, *injussu*.

## 5. Recorded variants: 1556 against 1573

None found. 1556's OCR (e-rara 10281656) agrees with 1573 wherever it can be read (1:1–6 in pieces, 1:16–25: *te
plus etiam*, *gratia adsit*, *Missa est Roma, per Onesimum*); of 1:7–15 it has only scraps, so 1:7 *sunt* and 1:12
*mihi* could not be checked against it. No decision needed.

## 6. Spelling rules proposed

None: every spelling that differs from 1573 has an approved rule (*adficimur* → *afficimur*, *intelligatur* →
*intellegatur*, *obedientia*, *quum*, the *charit-* stem) or is Gaffiot's already. *Adsit* is a compound of *sum* and
stays. No decision needed.
