# 2 Samuel 1–24, phase 2: the proofreaders' brief (2026-11-21)

As 1 Samuel's four proofreaders (`data/review/1sam1-31-stages3-5-readers.md`, "## Proofreaders"): read **every verse of
your chapters in the preview** `text/draft/2SA.preview.usfm` (built by `propose` from the draft, the approved spelling
rules, and the merged calls in `data/decisions/2Sam.layout.tsv` and `2Sam.forms.tsv`) as a reader of the finished
edition would, against the BSB (`sources/parallel/bsb/2Sam.tsv`, with its layout), the Vulgate, the Hebrew (wlc) and
1738's printed text (`text/orig/2SA.usfm`). Read `BRIEF.md` beside this file for the rules, and `CLAUDE.md`, `brief.md`.

Check:
- **Words**: compare the preview's words with 1738's word by word. Every difference must be an approved spelling rule
  (`data/rules/orthography.tsv`) or a listed draft fix (`data/review/2sam1-24-draft-fixes.md`). Report any omission,
  misreading or unexplained change.
- **Macrons**: every word's quantities in context (case, tense, *hīc*/*hic*, *vēnit*/*venit* …), with
  `python -m pipeline latin macron WORD`; names as settled in `names.md` here.
- **Layout**: quotation marks (balanced, reported speech unmarked, *X: words, inquit* with a comma), paragraphs (at
  Castellio's sentence starts, 1738's indents, split near 250 words), poetry, capitals, punctuation.

Write ONLY `data/review/2sam1-24-phase2/pN-layout.tsv`, `pN-forms.tsv` (the columns of the decision files; a layout
row replaces the merged row for its verse, so copy the merged row's text and change only what you correct; notes start
`proofread:` and end `(proofreader pN, 2026-11-21)`) and `pN.md` (a short report: what you corrected, spelling gaps that
need a rule, what you left and why). Never edit the decision files, the rules, the draft, the preview or `text/`; never
run `propose` (it rewrites shared files). Write as you go.
