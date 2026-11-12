# 2 John 1, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of Philemon (`data/review/phlm1-stage2.md`) and
1 John (`data/review/1john1-5-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 927–928: the title and Athanasius's
  argument after 1 John 5 on 927, 1:1–7 on 927, 1:8–13 at the head of 928). 1556 is the reference: where it reads
  otherwise, its reading is recorded as a variant (section 5); its e-rara OCR has 2 John on pages 10282446–47, in
  pieces (1:1–3 interleaved with 1 John 5, 1:4–13 with Jude). Stage 1 drafted Wikisource's 2 John as
  **`text/draft/2JN.usfm`** (BSB paragraphs). You have no earlier work on 2 John; `TXT/1 - OCR` (the 1726–27
  printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's 2 John is the early wording**, as its 1 John and Paul's letters: *favor* for *gratia* (1:3), *in
  carne* for *corporatum* (1:7), *quod elaboravimus* for *quae* (1:8), *sicuti* for *sicut* (1:4), each with the
  early-line printings (1715, 1747, 1750). It has no slips the other printings correct. 1556 has the revised reading
  wherever its OCR can be read (*gratia*, *corporatum*, *quae*).
- **Versification** (decision 5): the draft is at the KJV count (13 verses), no edits file. 1573 prints every verse
  number (its OCR reads 1:10 *to*, 1:11 *II*) and agrees with the draft everywhere.
- **Collation** (`python -m pipeline collate 2John 1`; `data/calibration/2John1-1-collation.tsv`, 16 places: 4
  *correct*, 1 *others-1573-agrees*, 11 *base-only* (10 reading, 1 division), no *uncovered* verse), with the edge
  and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/2John.*`, 5): every reading where 1573 and
  another printing agree against Wikisource (1:3 *gratia*, 1:4 *sicut*, 1:7 *corporatum*), every base-only reading
  whose 1573 words are Latin (1:8 *aquæ*, 1:11 *ei*, 1:4 *à patre*, a line the OCR lost). The rest of the base-only
  readings are 1573's OCR (*eiusós*, *inanet*, *ChriAi*, *inulta*, *venturű*), a word break (*ade rit*), a margin
  reference run into 1:6 (*Iohan*) and the note of 1:8 (*docucuimus*). Each place was also read against 1556 (its
  e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 927–928); nothing beyond the collation's places
  differs.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*filio*, *facta*, *ferat*):
  all are *f* by sense. Every *s* word whose *f*-form is Latin (*si/fi*, *situs/fitus*, *sum*): all are *s* by sense,
  and 1573's OCR has none of them as *f* where the *f*-form could be construed. None found.
- **In all, 4 corrections**: 4 readings of Castellio's revised text (section 2). Spellings (*caritate*, *Quum*,
  *Jesu*, *ejus*) are left to stage 3; no rule is wanting (section 6). No place where 1556 reads against 1573 was
  found (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (0)

None: where 1573 and the other printings agree against Wikisource the difference is a spelling (*charitate*), left to
stage 3. No decision needed.

## 2. Castellio's revised wording: 1573 against Wikisource's early line (4)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **2 John 1:3** *Adsit vobis favor, misericordia, pax* → *gratia*. 1573 *Adſit vobis gratia, miſericordia, pax, à Deo patre,* (canvas 927, crop `2John.1.3-gratia`), χάρις; 1556 (OCR *Adſit uo-bís gratía*), 1758, 1681, 1726. The early line *favor* (Wikisource, 1715, 1747, 1750), as Phlm 1:25 and Titus 3:15.
   **Apply:** `2John.1.3` la: `Adsit vobis favor,` → `Adsit vobis gratia,`
2. **2 John 1:4** *comperi, sicuti praeceptum accepimus a patre* → *sicut*. 1573 *viuere comperi, ſicut prçceptum accepimus / à patre.* (canvas 927, `2John.1.4-sicut`; the second line the OCR lost); 1758, 1747, 1726 (1681's OCR *ucut*). The early line *sicuti* (Wikisource, 1715, 1750). 1556's OCR does not reach the word (*…ceptum accepímus d patre*).
   **Apply:** `2John.1.4` la: `comperi, sicuti praeceptum` → `comperi, sicut praeceptum`
3. **2 John 1:7** *Jesum Christum in carne venisse* → *corporatum*. 1573 *qui Ieſum Chriſtum corporatum veniſſe non / confitentur.* (canvas 927, `2John.1.7-corporatum`), as 1 John 4:2–3; 1556 (OCR *quilefum Chriftum cor poratum uenilie*), 1758. The early line *in carne* (Wikisource, 1715, 1750).
   **Apply:** `2John.1.7` la: `Jesum Christum in carne venisse` → `Jesum Christum corporatum venisse`
4. **2 John 1:8** *ne perdamus, quod elaboravimus* → *quae elaboravimus*. 1573 *Date operam ne perdamus, ᵃ quæ elaborauimus,* (canvas 928, `2John.1.8-quae`; *a* a note letter, margin *a fruſtra vos docuimus*), ἃ εἰργασάμεθα; 1556 (OCR *perdamus qua claborauimus*), 1758. The early line *quod* (Wikisource, 1715, 1747, 1750).
   **Apply:** `2John.1.8` la: `ne perdamus, quod elaboravimus` → `ne perdamus, quae elaboravimus`

## 2a. Found by the f/s sweep (0)

None (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

No verse is uncovered: 1573's OCR reaches every verse; 1:4's last words (*à patre*), lost by the OCR, were read on the
image (section 2, item 2). No decision needed.

## 3. Word division (0)

None. No decision needed.

## 4. Checked and kept

- **1:11** *participat ejus prave facta*: 1573 *participat ei⁹ prauè facta* (canvas 928, `2John.1.11-eius`; the OCR's
  *ei* lost the abbreviation mark); 1556 (OCR *efus prau£ facta*). Agrees.
- **1:4** *a patre*: printed (intro). Agrees.
- **Note letters and margin notes**, not text: 1:8 *a* (*fruſtra vos docuimus*); the reference 1:6 *Iohan.15.10*;
  Athanasius's argument and the summary before 1:1.
- **Punctuation and capitals, left to stage 3**: 1:1 *dominae, ejusque* (1573 *dominæ eiusq;*), 1:3 *pax a Deo*
  (1573 *pax, à Deo*), 1:7 *Antichristus* (1573 the same), 1:12 *atramento:* (1573 a comma).
- **Spellings, left to stage 3**: *caritate* (1573 *charitate*), *Quum* (1573 *Cùm*), *Jesu*, *ejus*, *ejusque*.

## 5. Recorded variants: 1556 against 1573

None found. 1556's OCR (e-rara 10281656, pages 10282446–47) agrees with 1573 wherever it can be read (*gratia*,
*corporatum*, *quae elaboravimus*, *ejus prave facta*); it does not reach *sicut* (1:4). No decision needed.

## 6. Spelling rules proposed

None: every spelling that differs from 1573 has an approved rule or is Gaffiot's already (*caritas*, *quum*);
*Adsit* and *aderit* are compounds of *sum* and stay. No decision needed.
