# Settled Genesis: a slip found during Genesis 28–50, stages 3–5

Proposed 2026-11-08 under decision 30's standing rule. The **Apply** line is an exact replacement in
`text/GEN.usfm`, checked to match once. Apply with
`python -m pipeline review apply data/review/settled-fixes-gen.md --write` after the Decision line; data/gold is
rebuilt.

## Fixes (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

1. **Gen 25:33** *Jūra mihi* → *Jūrā mihi*: the imperative of *jūrō* (first conjugation, long ā), as your Gen
   21:23 *jūrā mihi per Deum* and the proposed Gen 47:31 *jūrā mihi*. *Jūra* is the plural of *jūs* (rights),
   which does not fit *Jūra mihi in præsentiā, inquit*. Found by the Genesis 45–50 reading.
   **Apply:** `Gen.25.33` la: `“Jūra mihi in præsentiā,”` → `“Jūrā mihi in præsentiā,”`
