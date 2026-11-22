# 1 Kings 1–22, phase 2: the readers' brief (2026-11-22)

Phase 2 of decision 85 (PLAN.md §4) for 1 Kings, done exactly as 2 Samuel was. **Model everything on 2 Samuel**:
read first `CLAUDE.md`, `brief.md`, `data/review/2sam1-24-edition.md`, `data/review/2sam1-24-stages3-5-readers.md`, and
look at `data/decisions/2Sam.layout.tsv` and `data/decisions/2Sam.forms.tsv` for the row format and the kind of calls
made (and `data/review/2sam1-24-phase2/notes-a.md`, `notes-1554-a.md` if you are a notes reader).

Inputs for 1 Kings:
- `text/draft/1KI.usfm` (the draft, KJV numbering), `text/draft/1KI.preview.usfm` (propose's preview),
  `data/review/1kgs1-22-chNN.md` (propose's flags, one item per verse);
- `text/orig/1KI.usfm` (1738's printed text, approved: never edit it) with `data/orig/1Kgs.pages.tsv` (leaf per verse);
- `data/review/1kgs1-22-transcription.md` (15 footnotes, the asterisks, Castellio's G./L./H. marks, wording doubts);
- parallels in `sources/parallel/<key>/1Kgs.tsv` (kjv, bsb with its layout column, wlc, lxx, vulgate …);
- `python -m pipeline latin macron WORD` for macrons (Gaffiot: use its answers, never copy its text).

**Rules**: cite only evidence you actually saw; never edit `text/`, `text/orig/`, `text/draft/`, the shared
`data/decisions/*.tsv` or any other reader's file. Other readers work on other chapters (one after another):
write ONLY to your own files in `data/review/1kgs1-22-phase2/` named with your id (e.g. `r3-layout.tsv`,
`r3-forms.tsv`, `r3.md`), in exactly the columns of `2Sam.layout.tsv` (`id marks text note`) and `2Sam.forms.tsv`
(`id form note`), notes ending `(reader rN, 2026-11-22)`. Claude merges them. Write your rows as you go so nothing is
lost if you are stopped. Finish with `rN.md`: a short report in 2 Samuel's readers'-notes style (quoted speech,
paragraphs, poetry, capitals, forms, doubts) and the count of rows.

**Verse readers**: every verse of your chapters, beside the KJV, the BSB (layout), the Hebrew and the printed text:
quotation marks (“…” and ‘…’ inside), paragraphs (1738's indents and the BSB's, 2 Samuel's measure), poetry (only where the BSB's layout column sets it,
as 2 Samuel's songs, q1/q2 on the BSB's lines),
capitals and punctuation, and every flagged form's macrons decided in context. Check that your layout rows' `text`
matches the draft's words exactly (`python -m pipeline propose 1Kgs A-B` only after Claude merges; do not run it
yourself — it overwrites shared files). Words that look like printer's slips: list them in your report with the
printed form, don't change the words.

1 Kings specifics: the three chapter breaks moved by the versification (3:1 *Solomo*, 13:1 *supervenit*, 15:1 *qui
anno*) fall mid-sentence: the draft opens each with `\p`; decide the layout there (2 Samuel's 14:1 and 20:1 are the
model). Misprints 1738 prints (3:1 *intera*, 6:8 *lanuas*, 6:27 *in templa*, 11:38 *tib*, 17:1 *adparco*, 18:17 *est
tune*, 20:14 *promitit*, 22:52 *Iou mque*): check the draft has the right word; if not, report it.
