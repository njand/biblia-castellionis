# Romans 3:10–11: the stanza break

Your spot check (2026-11-16): a blank line stands between 3:10 and 3:11. It is a mistake. The BSB's stanza break
(`\b`) is at 3:10, before the quotation begins ("As it is written: \b \q1 There is no one righteous"); the layout
decision for 3:11 (`data/decisions/Rom.layout.tsv`, "Ps 14:2 continued (BSB lines and stanza break)") carried it one
verse late, into the middle of the quotation. The settled text opens a poem after a prose line without a blank line
(Heb 5:6, 7:17), so none is wanted before 3:10's quotation either.

Every other `\b` in the settled text was checked against the BSB's in the same way: Luke 6:23's is the only other
with no BSB break at its verse (the BSB breaks at 6:22; Luke was settled from your 2019 text). It is left alone.

1. Take out the blank line before 3:11.
   **Apply:** `Rom.3.11` la: `\b \q1 \v 11 \qt Nōn est` → `\q1 \v 11 \qt Nōn est`

**Decision:** accept (Nathan, 2026-11-16: "Accept recommendations")
