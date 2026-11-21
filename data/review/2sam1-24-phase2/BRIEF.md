# 2 Samuel 1–24, phase 2: the readers' brief (2026-11-21)

Phase 2 of decision 85 (PLAN.md §4) for 2 Samuel, done exactly as 1 Samuel was. **Model everything on 1 Samuel**:
read first `CLAUDE.md`, `brief.md`, `data/review/1sam1-31-edition.md`, `data/review/1sam1-31-stages3-5-readers.md`, and
look at `data/decisions/1Sam.layout.tsv` and `data/decisions/1Sam.forms.tsv` for the row format and the kind of calls
made (and `data/review/1sam-notes-a.md`, `1sam-notes-1554-a.md` if you are a notes reader).

Inputs for 2 Samuel:
- `text/draft/2SA.usfm` (the draft, KJV numbering), `text/draft/2SA.preview.usfm` (propose's preview),
  `data/review/2sam1-24-chNN.md` (propose's flags, one item per verse);
- `text/orig/2SA.usfm` (1738's printed text, approved: never edit it) with `data/orig/2Sam.pages.tsv` (leaf per verse);
- `data/review/2sam1-24-transcription.md` (footnotes, 11 asterisks, Castellio's G./L./H. marks, wording doubts);
- parallels in `sources/parallel/<key>/2Sam.tsv` (kjv, bsb with its layout column, wlc, lxx, vulgate …);
- `python -m pipeline latin macron WORD` for macrons (Gaffiot: use its answers, never copy its text).

**Rules**: cite only evidence you actually saw; never edit `text/`, `text/orig/`, `text/draft/`, the shared
`data/decisions/*.tsv` or any other reader's file. Other readers are working **at the same time** on other chapters:
write ONLY to your own files in `data/review/2sam1-24-phase2/` named with your id (e.g. `r3-layout.tsv`,
`r3-forms.tsv`, `r3.md`), in exactly the columns of `1Sam.layout.tsv` (`id marks text note`) and `1Sam.forms.tsv`
(`id form note`), notes ending `(reader rN, 2026-11-21)`. Claude merges them. Write your rows as you go so nothing is
lost if you are stopped. Finish with `rN.md`: a short report in 1 Samuel's readers'-notes style (quoted speech,
paragraphs, poetry, capitals, forms, doubts) and the count of rows.

**Verse readers**: every verse of your chapters, beside the KJV, the BSB (layout), the Hebrew and the printed text:
quotation marks (“…” and ‘…’ inside), paragraphs (1738's indents and the BSB's, 1 Samuel's measure), poetry (David's
lament 1:19–27, the song of ch. 22, the last words 23:1–7: as 1 Samuel's Hannah's song, q1/q2 on the BSB's lines),
capitals and punctuation, and every flagged form's macrons decided in context. Check that your layout rows' `text`
matches the draft's words exactly (`python -m pipeline propose 2Sam A-B` only after Claude merges; do not run it
yourself — it overwrites shared files). Words that look like printer's slips: list them in your report with the
printed form, don't change the words.
