# *oe* in hiatus written as *œ* in the settled text (2)

Found 2026-11-16 in Leviticus stages 3–5 (`data/review/lev1-27-stages3-5.md`). A word whose *o* and *e* belong to
different syllables (*co-erceō*, *co-eō*: Gaffiot *coercĕō*, *cŏĕō*) is not a diphthong and is written *oe*, never
*œ*. The pipeline joined them when it applied a decided form; `verses.decided_word` now keeps them apart (tested).
The settled text writes them apart elsewhere: Gen 8:1 *coercend-*, Luke 11:29 *coeunte*. Two settled words have the
slip (every *œ* followed by a vowel or *r* searched in `text/*.usfm`).

1. **1 Pet 3:10** *cœrceat* → *coerceat* (Gaffiot *coercĕō*).
   **Decision:** accept (Nathan, 2026-11-16: "Apply all of your recommendations")
   **Apply:** `1Pet.3.10` la: `cœrceat linguam` → `coerceat linguam`
2. **Acts 4:26** *cœuntque* → *coeuntque* (Gaffiot *cŏĕō*). The same slip, found in the same search; not discussed
   before.
   **Decision:** accept (Nathan, 2026-11-16: "Approve both")
   **Apply:** `Acts.4.26` la: `cœuntque optimātēs` → `coeuntque optimātēs`
