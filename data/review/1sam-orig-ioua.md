# 1 Samuel 1:20 in the printed text: *Ioua*, not *loua*

*2026-11-21.* Nathan, on 2 Samuel's transcription: "I'm pretty sure you are misreading a capital I for all of these"
(2 Sam 2:9 *lezraelenses*, 5:15 *lebahar*, 1 Sam 1:20 *loua*).

The initial of 1738's *a loua exorasset* (leaf 322, right column, line 85) has a slanted top serif, which reader 01
took for an *l* while noting it "may be a worn capital I". The same shape stands at 2 Sam 2:9 and 5:15. All three are
names, and none makes sense with *l*. They are best read as the capital I in worn type, not as misprints. The edition
already reads the word as *Jōvā* (`data/decisions/1Sam.forms.tsv`), so only the printed text changes.
The read line in `data/witnesses/read-1738/1Sam1-31.tsv` is corrected with it (row 77), and 2 Samuel's are read
*Iezraelenses*, *Iebahar*.

1. **1 Sam 1:20** *a loua* → *a Ioua* (`text/orig/1SA.usfm`).
    **Apply:** `1Sam.1.20` la: `a loua exorasset` → `a Ioua exorasset`
    **Decision:** accepted (Nathan, 2026-11-21: "Yes")

Applied with `python -m pipeline review apply data/review/1sam-orig-ioua.md --items 1 --to text/orig/1SA.usfm --write`
once accepted.
