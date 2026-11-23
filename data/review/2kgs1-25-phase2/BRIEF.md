# 2 Kings 1–25, phase 2: the readers' brief (2026-11-23)

Phase 2 of decision 85 (PLAN.md §4) for 2 Kings, done exactly as 1 Kings was. **Model everything on 1 Kings**: read
first `CLAUDE.md`, `brief.md`, `data/review/1kgs1-22-edition.md` (with Nathan's Decision at its head),
`data/review/1kgs1-22-phase2/r1.md` (a verse reader's report) and `names.md`, and look at `data/decisions/1Kgs.layout.tsv`
and `data/decisions/1Kgs.forms.tsv` for the row format and the kind of calls made. The settled `text/1KI.usfm` shows
how they came out; use its forms for the names and words 2 Kings shares with it (and with `text/1SA.usfm`, `2SA.usfm`).

Inputs for 2 Kings:
- `text/draft/2KI.usfm` (the draft, KJV numbering; 1738's slips and Castellio's mark already taken out,
  `data/review/2kgs1-25-draft-fixes.md`), `text/draft/2KI.preview.usfm` (propose's preview),
  `data/review/2kgs1-25-chNN.md` (propose's flags, one item per verse);
- `text/orig/2KI.usfm` (1738's printed text, approved: never edit it) with `data/orig/2Kgs.pages.tsv` (leaf per verse);
- `data/review/2kgs1-25-transcription.md` (10 footnotes, the asterisks, Castellio's mark, wording doubts);
- parallels in `sources/parallel/<key>/2Kgs.tsv` (kjv, bsb with its layout column, wlc, lxx, vulgate …);
- `python -m pipeline latin macron WORD` for macrons (Gaffiot: use its answers, never copy its text).

**Rules**: cite only evidence you actually saw; never edit `text/`, `text/orig/`, `text/draft/`, the shared
`data/decisions/*.tsv` or any other reader's file. Other readers work on other chapters (one after another):
write ONLY to your own files in `data/review/2kgs1-25-phase2/` named with your id (e.g. `r3-layout.tsv`,
`r3-forms.tsv`, `r3.md`), in exactly the columns of `1Kgs.layout.tsv` (`id marks text note`) and `1Kgs.forms.tsv`
(`id form note`), notes ending `(reader rN, 2026-11-23)`. Claude merges them. Write your rows as you go so nothing is
lost if you are stopped. Finish with `rN.md`: a short report in 1 Kings' readers' style (quoted speech, paragraphs,
poetry, capitals, forms, doubts) and the count of rows.

**Verse readers**: every verse of your chapters, beside the KJV, the BSB (layout), the Hebrew and the printed text:
quotation marks (“…” and ‘…’ inside), paragraphs (1738's indents and the BSB's, 1 Kings' measure), poetry (only where
the BSB's layout column sets it, q1/q2 on the BSB's lines), capitals and punctuation, and every flagged form's macrons
decided in context. Check that your layout rows' `text` matches the draft's words exactly (`python -m pipeline propose
2Kgs A-B` only after Claude merges; do not run it yourself — it overwrites shared files). Words that look like
printer's slips: list them in your report with the printed form, don't change the words.

2 Kings specifics:
- **Six chapter breaks moved by the versification** fall mid-sentence: 12:1 *videlicet anno septimo*, 16:1 *Judaeae
  regnum obtinuit*, 21:1 *annos tum natus*, 22:1 *anno aetatis suae octavo* (the draft opens each with `\nb`), 23:1
  *curavit ad se* and 25:1 *anno ejus regni nono* (`\p`). Decide the layout there (1 Kings' 3:1, 13:1, 15:1 and 2 Samuel's
  14:1, 20:1 are the model).
- **Lower-case names and adjectives** as 1738 prints them (*iezraelensi*, *israeliticis*, *assyrii*, *bethelensem*,
  *accaronensis*): capitalize as 1 Kings did (its draft fixes §5 and the settled text).
- **Slips taken out** (draft fixes §1): 1:1 *Moabitae*, 13:14 *equites*, 13:15 *praecepit*, 19:5 *Ezechiam*, 25:17
  *cubitus*, 8:1 *indici*. **Left**: 9:16 *decubabat* (no source knows it; report what you think).
