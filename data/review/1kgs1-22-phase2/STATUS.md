# 1 Kings phase 2: where it stands (2026-11-22: settled for now on Nathan's "Approve all as recommended")

Done:
- `1kgs1-22-draft-fixes.md` §1–2 (slips, Castellio's marks) and §3 (nine found by the verse readers, among them two
  phase-1 misreadings) applied to `text/draft/1KI.usfm`.
- Verse readers r1–r9 (1–2, 3–5, 6–7, 8–9, 10–12, 13–15, 16–18, 19–21, 22) and the names reader: their rows merged by
  `merge.py` into `data/decisions/1Kgs.layout.tsv` (311) and `1Kgs.forms.tsv` (584, the names reader's over the
  readers'); `propose 1Kgs 1-22` rebuilt the review items and `text/draft/1KI.preview.usfm`.
- `data/review/1kgs-orig-consecratum.md`: two misreadings in the approved printed text (7:51, 22:34), accepted by
  Nathan and applied to `text/orig/1KI.usfm`.
- `1kgs1-22-draft-fixes.md` §4 (eleven names brought to one form: *Nabati*, *Ahiae*, *Hananis*, *Sarephtham*,
  *Asiongabre*, *Anathotha*, *Bethsemem*, *Chamoss-*) and §5 (six *Israelitic-*/*Solomonian-* capitalized) applied; the
  forms rows respelled to match (r1, r5, r8, names); merged and `propose` rebuilt.
- `python -m pipeline notes 1Kgs` → `../1kgs-notes-candidates.md` (67 entries); `NOTES.md` here briefs the two notes
  readers.

- Notes readers A (1–11) and B (12–22) under `NOTES.md`: `notes-a.md`, `notes-b.md` (three notes, 2:12, 2:28, 22:30),
  `notes-1554-a.md`, `-b.md`; the 1554 facts in `docs/editions.md`.
- Proofreaders p1–p4 under `PROOF.md`: 47 forms rows, 4 layout rows, merged (`merge.py` reads them over all); 32 spelling
  rows added to `data/rules/orthography.tsv` in approved families; stale forms rows respelled; `propose` rebuilt (816
  items `ok`).
- `../1kgs1-22-edition.md`: the summary for Nathan (nine points).

Next: Nathan's decisions on `../1kgs1-22-edition.md`, then its "On approval".

- Settled 2026-11-22 (`../1kgs1-22-edition.md`, Decision): 3:7 *necdum* (draft fixes §6), `text/1KI.usfm` from the 816
  items, the three notes, gold, ledger; drafts removed; the printed text titled and rebuilt from the read lines (same).
