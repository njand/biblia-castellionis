# 3 John 1, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of Philemon (`data/review/phlm1-stage2.md`) and
1 John (`data/review/1john1-5-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvas 928 holds the whole letter, after 2 John and
  Athanasius's argument). 1556 is the reference: where it reads otherwise, its reading is recorded as a variant
  (section 5); its e-rara OCR has 3 John on page 10282447, interleaved with Jude's column but readable for most of
  the letter. Stage 1 drafted Wikisource's 3 John as **`text/draft/3JN.usfm`** (BSB paragraphs). You have no earlier
  work on 3 John; `TXT/1 - OCR` (the 1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as
  an OCR.
- **Wikisource's 3 John is the early wording** at one place: *feliciter agis* for *fideliter agis* (1:5), with 1747
  and 1750. It has no slips the other printings correct. 1556 has *fideliter*.
- **Versification** (decision 5): the draft is at the KJV count (14 verses). 1573 prints every verse number and
  agrees with the draft but at the end: 1573 (canvas 928, on the image, `3John.1.14-Salutant`) and Wikisource number
  *Salutant te amici. Saluta amicos nominatim* as **15**; the KJV's 14 holds the greetings (*Peace be to thee. Our
  friends salute thee. Greet the friends by name*). Already joined to 14 by `data/versification/3John.draft.edits.tsv`
  (applied 2026-11-12), so the draft's 14 is 1573's 14 and 15. Nothing to move (section 2c).
- **Collation** (`python -m pipeline collate 3John 1`; `data/calibration/3John1-1-collation.tsv`, 29 places: 3
  *correct*, 1 *others-1573-agrees*, 1 *others*, 22 *base-only* (14 reading, 4 division, 2 f/s, 1 spelling, 1 edge),
  2 *uncovered*), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/3John.*`, 6):
  the *others* place 1:5 (*fideliter*, 1758 and 1726 with 1573), the edge (1:4 *ave fidente*, the margin note of 1:5
  run into the text), 1:8's last line, which the OCR lost (*ſi-/mus adiutores*), the numbering of 1:15, and the
  uncovered verses. The *correct* places are spellings (*Charissime*, *charitatem*) and a word joined (1:11
  *benefacit*); the rest of the base-only readings are 1573's OCR (*quéadmodum*, *teitati*, *nulla*, *Naim*,
  *nihilós*, *dignű*, *bonű*, *Deu*), word breaks (*vehes menter*, *prima rius*, *char ta*, *colloque mur*,
  *Salutantteamici*) and the margin note of 1:10 (*fcil, admi*). Each place was also read against 1556 (its e-rara
  OCR, `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvas 928); nothing beyond the collation's places
  differs.
- **The two uncovered verses** were read whole on the image: 1:1 *SENIOR Caio chariſsimo, quem ego verè amo.*
  (crop `3John.1.1-Caio`) and 1:5 *Chariſsime, ᵃ fideliter agis, quicquid erga fratres & hoſpites facis,*
  (`3John.1.5-fideliter`; *a* a note letter, margin *a vt fidentẽ Chriſtianũq; decet*). 1:5 differs from the draft
  (section 2); 1:1 only in the name's spelling (section 4).
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fratres*, *facis*,
  *facies*, *feliciter*): all are *f* by sense. Every *s* word whose *f*-form is Latin (*si/fi*, *simus/fimus*,
  *sum*): all are *s* by sense; where 1573's OCR has *fi* (1:6, 1:10) the *f*-form cannot be construed. None found.
- **In all, 1 correction**: 1 reading of Castellio's revised text (section 2). Spellings (*carissimo*,
  *Carissime*, *caritatem*, *quum*, *quidquid*, *ejiciat*, *charta*) are left to stage 3; no rule is wanting
  (section 6). No place where 1556 reads against 1573 was found (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (0)

None: where 1573 and the other printings agree against Wikisource the difference is a spelling (*charissime*,
*charitatem*) or a word division (*benefacit*), left to stage 3. No decision needed.

## 2. Castellio's revised wording: 1573 against Wikisource's early line (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; read on the 1573 page image)

1. **3 John 1:5** *Carissime, feliciter agis* → *fideliter agis*. 1573 *Chariſsime, ᵃ fideliter agis, quicquid erga fratres* (canvas 928, crop `3John.1.5-fideliter`; an uncovered verse), πιστὸν ποιεῖς; 1556 (OCR *Cha-/rífsime, 2 fideliter agis*, the note letter read as *2*), 1758, 1726. The early line *feliciter*, echoing 1:2–3 (Wikisource, 1747, 1750).
   **Apply:** `3John.1.5` la: `Carissime, feliciter agis,` → `Carissime, fideliter agis,`

## 2a. Found by the f/s sweep (0)

None (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

The two uncovered verses were read whole on the image (intro): 1:5 is section 2's item; 1:1 differs only in the
name's spelling. No further decision needed.

## 2c. Verse boundaries (0)

1573's verse 15 (*Salutant te amici …*) is joined to 14 already (intro). No decision needed.

## 3. Word division (0)

None. No decision needed.

## 4. Checked and kept

- **1:1** *Senior Gaio carissimo*: 1573 *Caio* (on the image), 1556 *Caío* (OCR); Athanasius's argument in 1573
  *ad Gaium*, its summary *Gaium monet* (on the image); Wikisource, 1747, 1750 *Gaio*. Your settled text has *Gāius* (Rom 16:23,
  1 Cor 1:14, Acts 19:29, 20:4: 6×), no *Cai-*; kept, one form per person (decision 46).
- **1:8** *ut veritatis simus adjutores*: 1573 *vt veritatis ſi-/mus adiutores* (canvas 928, `3John.1.8-simus+next`,
  the second line at the head of the next column). Agrees.
- **1:14** *Salutant te amici. Saluta amicos nominatim*: 1573 *15 Salutant te amici. Saluta amicos nominatim.*
  (`3John.1.14-Salutant`); 1556 and 1681's OCRs end before *nominatim*. Joined to 14 (intro).
- **1:11** *Qui bene facit*: 1573 *Qui be-/nefacit*, 1556 *Quíbenefacit*, 1726 joined; Wikisource, 1681, 1715, 1747,
  1750 apart. Two words or one, the same sense (ὁ ἀγαθοποιῶν); kept.
- **Note letters and margin notes**, not text: 1:5 *a* (*vt fidentẽ Chriſtianũq; decet*), 1:10 (*ſcil. admi[ttere]*);
  Athanasius's argument and the summary before 1:1.
- **Punctuation and capitals, left to stage 3**: 1:3 *uti ex veritate vivas* (1573 *vti*), 1:6 *si, ut Deo dignum
  est,* (1573 *ſi vt Deo dignũ eſt*), 1:11 *a Deo est:* (1573 a comma), 1:12 *et vos, verum esse testimonium
  nostrum, scitis* (1573 without the commas).
- **Spellings, left to stage 3**: *carissimo*, *Carissime*, *caritatem* (1573 *chariſsimo*, *Chariſsime*,
  *charitatem*), *quum* (1573 *cùm*), *quidquid* (1573 *quicquid*), *ejiciat* (1573 *eijciat*; your *ējiciō* kept,
  decision 17), *charta* (Gaffiot), *ejus*, *adjutores*.

## 5. Recorded variants: 1556 against 1573

None found. 1556's OCR (e-rara 10281656, page 10282447) agrees with 1573 wherever it can be read (*Caio*,
*fideliter agis*, *simus adiutores*, *Salutant te amici*); it is interleaved with Jude's column, so a few words of
1:2–4 are read in pieces. No decision needed.

## 6. Spelling rules proposed

None: every spelling that differs from 1573 has an approved rule or is Gaffiot's already. No decision needed.
