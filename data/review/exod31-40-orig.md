# Exodus 31–40 as printed (1738): the draft for review

Built 2026-11-15 by `python -m pipeline orig Exod 31-40 --read-lines` → `text/orig/draft/EXO.usfm` (beside
chapters 1–30), with each verse's leaf in `data/orig/Exod.pages.tsv` (for the site's link to the page).

**Decision:** approved (Nathan, 2026-11-15: "Yes, approve"; the drop capital's word set as a normal capitalized word); moved to `text/orig/EXO.usfm`

## How it was made

Wikisource has no Exodus 31–40, so stage 2 read 1738's lines on the page images, each line twice
(`data/review/exod31-40-stage2.md`; the lines in `data/witnesses/read-1738/Exod31-40.tsv`). Those lines **are** the
printed text: every word and mark was read on the image, as printed. So this draft needs no OCR alignment and no
further reading of words, unlike Genesis and Exodus 1–30 (`orig.from_read_lines`):

- **The lines joined into verses** (`ocrdraft.verses_of`, hyphens at a line's end joined), with the printed text's
  conventions (decision 57): *&* and *q;* written out, s for ſ, the space 1738 sets before a mark dropped.
  Everything else is as printed (decision 58): spelling, u/v and i/j, capitals (the proclamation of 34:6–7 in
  capitals), the æ and œ ligatures in lower case and *Ae* for the capital (*Aegypto*), punctuation, and 1738's
  misprints.
- **Moved to the KJV's numbering** by the draft's own six edits (`data/versification/Exod31-40.draft.edits.tsv`:
  32:12–13, 32:27–28 with the split at *sic loquitur*, 32:34, 35:35). Every one of the 325 verses has the same
  words as the settled verse (checked word by word).
- **1738's paragraphs from its indents** (`archive.indents`, as for 1–30), each looked at on the page: **18 inside
  the chapters**, besides each chapter's start: 32:7, 32:15, 32:25, 33:7, 34:4, 34:29, 35:20, 36:35, 37:6, 37:10,
  37:17, 37:25, 38:9, 38:24 (the first line of leaf 154), 39:15, 40:12, 40:17, and inside 40:33 at *Postquam*. One
  more that the indent reading found was not one: 34:7 *QVI CLEMENTIA*, flush with the capitals around it (leaf
  149), taken away by a `¶-` row in `data/decisions/Exod.orig.tsv`.

## Where the printed text differs from the reading edition

118 words, all of them 1738's spellings or misprints, no other words:

- **Spellings the approved rules normalize**: *quum* (18), *quatuor* (12), *annul-* (13), *eis* (7), the unassimilated
  *ad-* (*adligabant*, *adstitit*, *adloquitur*, *adspiraui*, *adposititios* … 41), *caussa* (3), *concione* (2),
  *septemtrionali* (2), *intellig-* (2), *sobol-* (2), *quoties*, *quemdam*, *eamdem*, *tamdiu*, *sexcenta*,
  *adolescens*, *trigenum*, *sexdecim*, *cacabos*, *circumseptum*, *temetipsum* (one word).
- **1738's misprints and readings, kept** (corrected in the reading edition): 33:1 *lactc*, 33:8 *tabernaeulum*, 36:25
  *totitemque*, 37:9 *obtegeret* (1554 and 1573 *obtegerent*). (40:20 *aræ*, every printing's, is the same in both: the reading edition keeps
  it with a note.)

## A question

**Chapter openings beside a drop capital.** 1738 prints the first word of each chapter with its second letter as a
capital too (*DEstinaui*, *INterea*). This draft sets them as the drafts of 1–30 mostly do, *Destinaui*, *Interea*
(`ocrdraft.drop_capital`). But Exodus 1–30 is not consistent: *Igitur*, *Quidam* … beside *AVditionem* (22:1), *AD*
(24:1) and *Tvm* (28:1), which came from rows read on the page. Recommended: one convention for both Testaments'
printed text, the drop capital's word as a normal capitalized word (the large initial is the page's ornament, not
spelling). Say if you would rather keep the printed small capitals (*DEstinaui*) everywhere.
