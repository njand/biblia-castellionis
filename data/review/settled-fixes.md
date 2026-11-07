# Settled chapters: three findings from the overnight run

Proposed 2026-11-07. Found while building the Matthew 14–28 pilot tools; nothing here has been applied. Each
**Apply** line is an exact replacement inside that verse of `text/<BOOK>.usfm`, checked to match once
(`python -m pipeline review check data/review/settled-fixes.md`); answer each group's **Decision:**, then
`python -m pipeline review apply data/review/settled-fixes.md --write` (rebuilds `data/gold/`).

## 1. Luke 10–11: *jūris perītus* where every printing has *legisperitus* (5)

Your Luke has *jūris perītus/-ī/-īs* five times. Every printing that could be read has *legisperitus*: 1573 (page
image: 10:25 *quidam legiſperitus*, canvas 799; 11:52 *Væ vobis legiſperitis* and 11:53 *cœperunt legiſperiti*,
canvas 800; 11:45–46 OCR), 1758, 1747 and 1715 at all three places checked in their OCR rows, 1750 and 1726–27
(*legifperitus*, 11:45) where found. **Only Wikisource has *juris peritus*.** Decision 23 compared your text with
Wikisource, so it could not see this. Written *lēgis perītus* by the approved rule (*legisperiti → legis
periti*), as your Luke 5:17 and 7:30 already have it, and as Matt 22:35 in `matt14-28-stage2.md`.

**Decision:** accept (Nathan, 2026-11-07)

1. **Apply:** `Luke.10.25` la: `quīdam jūris perītus, quī` → `quīdam lēgis perītus, quī`
2. **Apply:** `Luke.11.45` la: `quīdam jūris perītus:` → `quīdam lēgis perītus:`
3. **Apply:** `Luke.11.46` la: `vōbīs jūris perītīs,” inquit` → `vōbīs lēgis perītīs,” inquit`
4. **Apply:** `Luke.11.52` la: `vōbīs jūris perītīs, quī` → `vōbīs lēgis perītīs, quī`
5. **Apply:** `Luke.11.53` la: `cœpērunt jūris perītī et` → `cœpērunt lēgis perītī et`

## 2. Luke 12:50 *baptizandus* without its macron (1)

Your settled text writes *baptīz-* everywhere else (*baptīzō*, *baptīzābat*, *baptīzandum* … 28 times); this
one lacks the *ī*.

**Decision:** accept (Nathan, 2026-11-07)

1. **Apply:** `Luke.12.50` la: `Baptismate baptizandus sum` → `Baptismate baptīzandus sum`

## 3. Quotation marks the wrong way round (4)

From the quotation check of the settled chapters (`data/calibration/quotes-check.md`, 29 candidates; these four
are certain: a closing mark used to open a speech, or a closing mark with nothing open).

**Decision:** accept (Nathan, 2026-11-07)

1. **Luke 8:45** *Tum Jēsūs: ”Quis mē tetigit?”*
   **Apply:** `Luke.8.45` la: `Tum Jēsūs: ”Quis` → `Tum Jēsūs: “Quis`
2. **Gen 16:10** *inquit eī Jōvæ angelus, ”ut præ multitūdine*
   **Apply:** `Gen.16.10` la: `angelus, ”ut præ` → `angelus, “ut præ`
3. **Gen 21:10** *ita dīxit Abrāhāmō: ”Ējice*
   **Apply:** `Gen.21.10` la: `Abrāhāmō: ”Ējice` → `Abrāhāmō: “Ējice`
4. **John 4:17** *“Nōn habeō virum,” inquit eī respondēns mulier.” Et Jēsūs*: the narration after *inquit* is not
   in the speech.
   **Apply:** `John.4.17` la: `respondēns mulier.”` → `respondēns mulier.`
