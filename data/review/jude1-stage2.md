# Jude 1, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-12 (decision 30's standing rule), on the route of Philemon (`data/review/phlm1-stage2.md`) and
1 John (`data/review/1john1-5-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 928–929: the title and summary after 3 John,
  1:1–8 on 928, 1:8–25 on 929, then Hebrews). 1556 is the reference: where it reads otherwise, its reading is
  recorded as a variant (section 5); its e-rara OCR has Jude on pages 10282447–48, interleaved with 3 John's column
  on the first (1:1–17 in pieces, 1:4 and 1:15 garbled) and clear on the second (1:18–25). Stage 1 drafted
  Wikisource's Jude as **`text/draft/JUD.usfm`** (BSB paragraphs). You have no earlier work on Jude; `TXT/1 - OCR`
  (the 1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's Jude is the early wording** at 1:4 (*et Deum, qui solus herus est* for *et solum herum Deum*, with
  1715, 1747, 1750), with slips of its own the other printings correct (*et in Jesu Christo*, a lost *impii*, *de
  illis*, *convinciat*, *coninquinatam*, two missing spaces). 1573 reads *magni Dei judicium* at 1:6, with 1556 and
  1758, where Wikisource and the other printings have *diei* (section 2, item 2).
- **Versification** (decision 5): the draft is at the KJV count (25 verses), no edits file. 1573 prints every verse
  number (its OCR reads 1:10 *so*, 1:11 *In*, 1:15 *rs*) and agrees with the draft everywhere.
- **Collation** (`python -m pipeline collate Jude 1`; `data/calibration/Jude1-1-collation.tsv`, 44 places: 13
  *correct*, 3 *others-1573-agrees*, 2 *others*, 26 *base-only* (19 reading, 3 division, 3 f/s, 1 spelling), no
  *uncovered* verse), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/Jude.*`,
  10): every reading where 1573 and another printing agree against Wikisource (1:1 *in*, 1:4 *impij*, *ſolum herum
  Deum*, 1:10 *ijs*, 1:15 *conuincat*, 1:23 *coinquinatam*), every base-only reading whose 1573 words are Latin (1:6
  *Dei*, 1:7 *finitimæ*), and 1:4's last word (*negantes*, carried to the next column, which the OCR lost). The
  *correct* places are otherwise spellings (*charitatem*, *Charissimi*, *afflatu*). The rest of the base-only
  readings are 1573's OCR (*angelosás*, *seruados*, *scribédo*, *Væeis*), word breaks (*corpo ris*, *cir cumactæ*,
  *Do mini*, *se cula*), the running head of 929 (1:8 *AD HEBRAEOS*), note letters (1:8 *d*, 1:19 *c*) and the
  references (*Pet*, *Pfal*, *Tim*). Each place was also read against 1556 (its e-rara OCR, `sources/erara-1556/`) and
  the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **Every verse was read whole against 1573's page text** (canvases 928–929); nothing beyond the collation's places
  differs.
- **The f/s sweep**, both ways. Every *f* word in the draft whose *s*-form is also Latin (*fide/side*, *frater*,
  *ferre*, *Feri/seri*, *fluctus*): all are *f* by sense (1:13 *feri fluctus maris*, wild waves). Every *s* word whose
  *f*-form is Latin (*sontes/fontes*, *suam*, *suas*, *Soli/foli*, *sub*): all are *s* by sense; 1573's OCR has
  *ſontes* (1:15), and its *fuam*, *fuas*, *foli* cannot be construed. None found.
- **In all, 11 corrections**: 5 Wikisource slips (section 1), 2 readings of Castellio's text (section 2), 4 word
  divisions (section 3). Spellings (*carissimi*, *caritatem*, *quum*, *adflatu*, *expectantes*, *Iesu*, *Gomorrha*)
  are left to stage 3; one rule proposed (section 6). No place where 1556 reads against 1573 was found (section 5).

## 1. Wikisource slips: 1573 and the other printings agree against it (5)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Jude 1:1** *sanctificatis in Deo patre, et in Jesu Christo reservatis* → *et Jesu Christo reservatis*. 1573 *ſanctificatis in Deo / Patre, & Ieſu Chriſto reſeruatis,* (canvas 928, crop `Jude.1.1-reservatis`), καὶ Ἰησοῦ Χριστῷ τετηρημένοις; 1681, 1715, 1747, 1750. Wikisource alone (1556's OCR does not show the clause).
   **Apply:** `Jude.1.1` la: `et in Jesu Christo reservatis` → `et Jesu Christo reservatis`
2. **Jude 1:4** *ad hoc ipsum supplicium designati, Dei nostri* → *designati, impii, Dei nostri*. 1573 *ipſum ſupplicium deſignati, impij, Dei noſtri bene-/ficium* (canvas 928, `Jude.1.4-impii`), ἀσεβεῖς; 1758, 1681, 1715, 1747, 1750, 1726. Wikisource alone (1556's OCR garbled here).
   **Apply:** `Jude.1.4` la: `supplicium designati, Dei nostri` → `supplicium designati, impii, Dei nostri`
3. **Jude 1:10** *quae ignorant, de illis maledicunt* → *de iis*. 1573 *de ijs maledicunt* (canvas 929, `Jude.1.10-iis`), as *in iis corrupti sunt* after it; 1556 (OCR *deijs*), 1758, 1681, 1715, 1747, 1750, 1726. Wikisource alone.
   **Apply:** `Jude.1.10` la: `de illis maledicunt` → `de iis maledicunt`
4. **Jude 1:15** *omnesque eorum impios convinciat* → *convincat*. 1573 *impios conuincat omnium* (canvas 929, `Jude.1.15-convincat`); 1758, 1681, 1747, 1750 (1715's OCR *convinca*, 1556's *couinc*). Wikisource alone.
   **Apply:** `Jude.1.15` la: `impios convinciat omnium` → `impios convincat omnium`
5. **Jude 1:23** *exosi etiam carne coninquinatam vestem* → *coinquinatam*. 1573 *carne coinquinatam veſtem.* (canvas 929, `Jude.1.23-coinquinatam`); 1556 (OCR *coíriquínata*), 1758, 1750, 1726. Wikisource alone.
   **Apply:** `Jude.1.23` la: `carne coninquinatam vestem` → `carne coinquinatam vestem`

## 2. Castellio's wording: 1573 against Wikisource (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12; every item read on the 1573 page image)

1. **Jude 1:4** *in libidinem, et Deum, qui solus herus est, Dominumque nostrum Jesum Christum negantes* → *et solum herum Deum, Dominumque*. 1573 *transferentes in libidinem : & ſolum herum / Deum, Dominumq; noſtrum Ieſum Chriſtum / negantes.* (canvas 928, `Jude.1.4-impii`, `Jude.1.4-solum+next`; the last two lines at the head of the next column), τὸν μόνον δεσπότην θεὸν; 1758, 1681, 1726 (1556's OCR *& fo…* garbled, perhaps *ſolum*). The early line *Deum, qui solus herus est* (Wikisource, 1715, 1747, 1750). The colon before *&* is stage 3's.
   **Apply:** `Jude.1.4` la: `in libidinem, et Deum, qui solus herus est, Dominumque` → `in libidinem, et solum herum Deum, Dominumque`
2. **Jude 1:6** *ad magni diei judicium* → *ad magni Dei judicium*. 1573 *ad magni Dei iudi-/cium æternis vinculis* (canvas 928, `Jude.1.6-Dei`); **1556** too (OCR *ad magni Deiiudictü*, page 10282447) and 1758 (OCR *Dei judidum*). Wikisource, 1681, 1715, 1747, 1750, 1726 *diei*, as the Greek (εἰς κρίσιν μεγάλης ἡμέρας) and the Vulgate (*in iudicium magni diei*). For your eye: not 1573's own misprint, since 1556 has it too; *the judgement of the great God* may be Castellio's reading or a slip both printings share.
   **Apply:** `Jude.1.6` la: `ad magni diei judicium` → `ad magni Dei judicium`

## 2a. Found by the f/s sweep (0)

None (intro). No decision needed.

## 2b. Found where 1573 was not aligned (0)

No verse is uncovered: 1573's OCR reaches every verse; 1:4's *negantes*, which it lost, was read on the image
(section 2, item 1). No decision needed.

## 3. Word division (4)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-12)

1. **Jude 1:12** *arbores autumnales infructuosae,bis mortuae* → *infructuosae, bis*. A space after the comma; 1573 *infructuoſæ, bis mor-/tuæ* (canvas 929), 1715, 1747, 1726.
   **Apply:** `Jude.1.12` la: `infructuosae,bis mortuae` → `infructuosae, bis mortuae`
2. **Jude 1:12** *irreligiose convivantes, seipsos pascentes* → *se ipsos*. Your settled *sē ipsōs* (6× in `data/gold/`) and no *seipsos*, as *sē ipsum* in 1 John 3:3 (`data/review/1john1-5-stage2.md`). Not a quotation. 1573 joins it (*ſeipſos*, canvas 929).
   **Apply:** `Jude.1.12` la: `convivantes, seipsos pascentes` → `convivantes, se ipsos pascentes`
3. **Jude 1:15** *omniumque,quae contra eum* → *omniumque, quae*. A space after the comma; 1573 *omniumq; quæ contra eum* (canvas 929), 1747, 1750.
   **Apply:** `Jude.1.15` la: `omniumque,quae contra` → `omniumque, quae contra`
4. **Jude 1:19** *Hi sunt, qui seipsos secernunt* → *se ipsos*. As item 2. 1573 *ſeipſos* (canvas 929).
   **Apply:** `Jude.1.19` la: `qui seipsos secernunt` → `qui se ipsos secernunt`

## 4. Checked and kept

- **1:7** *finitimaeque urbes*: 1573 *finitimæq; vrbes* (canvas 928, `Jude.1.7-finitimae`; its OCR lost the *q;*), with
  1556 (OCR *finitimadq Urbes*) and every printing. Agrees.
- **1:6** *Angelosque*: 1573 *angeloſq;*; the capital follows the draft's verse openings.
- **1:20** *vos ipsos*: 1573 *voſipſos*, 1556 joined (OCR); the draft already divides it. Kept.
- **1:13** *Feri fluctus maris*: 1573 *feri fluctus* (canvas 929). Agrees.
- **Note letters and margin notes**, not text: 1:8 *d* (OCR *& ſcil. Dei*, the margin), 1:19 *c* (*terreſtres*;
  1:20's margin OCR *tate alieni*); the references (as the OCR reads them: 1:4 *2.Pet.2.14*, 1:5 *Num.14.37*, 1:7
  *Gen.19.24*, 1:11 *Num.22.21*, 1:12 *2.Pet.2.17*, 1:15 *Pſal.17.19*, 1:17 *1.Tim.4.1*, *2.Tim.3.1*, 1:18
  *2.Pet.3.3*); the summary before 1:1; the running head of 929 (*AD HEBRÆOS*).
- **Punctuation and capitals, left to stage 3**: 1:1 *Judas,* (1573 *IVDAS* without the comma), 1:3 *habui, vos* (1573
  without the comma), 1:4 *libidinem,* (1573 a colon), 1:5 *perdidit:* (1573 a stop), 1:9 *increpet* (1573
  *Increpet*), 1:11 *cainiana*, *balaamici*, *coranaque* (1573 *Cainiana*, *Balaamici*, *Coranaque*), 1:15 *sontes,
  impii* (1573 without the comma), 1:25 *Amen* (1573 without the colon).
- **Spellings, left to stage 3** (and section 6): *carissimi*, *caritatem*, *caritatibus*, *caritate* (1573
  *charit-*), *quum* (1573 *cùm*), *adflatu* (1573, 1556 *afflatu*; approved rule), *expectantes* (1573
  *expectantes*; decision 42's *exspect-*), *Iesu* (decision 17), *iacent* (1573 *iacent*), *herus* (Gaffiot
  *erus*, decision 42), *Gomorrha* (section 6), *Enochus*, *Michael*, *Mosis*.

## 5. Recorded variants: 1556 against 1573

None found. 1556's OCR (e-rara 10281656, pages 10282447–48) agrees with 1573 wherever it can be read (1:6 *magni Dei
iudicium*, 1:7 *finitimæq;*, 1:10 *de ijs*, 1:19–25); at 1:1 and 1:4 it is too garbled to compare. No decision needed.

## 6. Spelling rules proposed

The draft's *Gomorrha* has no row in `data/rules/orthography.tsv` (checked with `normalize.propose()` on the draft).
Proposed under decision 46 (one form per person, the Old Testament's) and decision 37's names, not written to the file:

| old | new | scope | Where | Evidence |
|---|---|---|---|---|
| Gomorrha | Gomorra | word | 1:7 | 1573 *Gomorra* (canvas 928, `Jude.1.7-finitimae`); 1556 (OCR *Go…morra*), 1758, 1715, 1747, 1726; your settled *Gomorra*, *Gomorram*, *Gomorræ* (Genesis, Matthew, Mark, Rom 9:29), no *Gomorrh-*. 2 Pet 2:6 may have the same form |

**Decision:** accept (Claude, 2026-11-12, under decisions 37, 42 and 46; added to `data/rules/orthography.tsv`)