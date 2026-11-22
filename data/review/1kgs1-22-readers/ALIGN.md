# 1 Kings, phase 1: moving 1738's verses to the KJV's numbering (brief for each aligner)

Repo: `C:\Users\nathanjamesanderson\Documents\biblia-castellionis`. Aligners run one after another, each on a
range of chapters, adding to one edits file. Read first: `pipeline/versify.py`'s docstring (the ops: `split`,
`merge`, `chapter`, `opens`, `range`, `absent`), and `data/versification/2Sam1-24.draft.edits.tsv` (2 Samuel's
210 edits, done the same way: copy the style of their notes exactly).

## What you have

- `text/draft/1KI.usfm`: the draft, in **1738's own numbering** (its margin numbers), modern spelling (*Jovam*,
  *ejus*). Do not edit it.
- `text/orig/draft/1KI.usfm`: the printed text, same numbering, 1738's spelling (*Iouam*, *eius*; misprints kept, e.g. 22:50 *Iou mque*). Do not edit it.
- KJV `sources/parallel/kjv/1Kgs.tsv`, BSB `sources/parallel/bsb/1Kgs.tsv`, Hebrew `sources/parallel/wlc/1Kgs.tsv`,
  Vulgate `sources/parallel/vulgate/1Kgs.tsv`; KJV verse counts `data/versification/kjv.tsv`.
- The readers' notes (`data/review/1kgs1-22-transcription-readers.md`, by reader; Claude's settlements at its head) say where 1738 divides differently.

## The task

Make every chapter of your range carry the KJV's verses, by moving only verse markers (never a word):
**split** where a KJV verse begins inside one of 1738's verses (anchor: the first words of the KJV verse, as
`draft form|printed form` whenever the two spellings differ, each unique within that verse); **merge** where
1738 begins a verse the KJV does not; `opens`/`chapter` for chapter breaks; `absent` only where a KJV verse has no
Latin at all (its sense folded into a neighbour). Where one Latin sentence runs across two KJV verses, split where
the second's words begin if they stand clear; otherwise leave Castellio's division and say so. Lead-in clauses
stay with the verse before (as 1 Sam 17:40). `at` is always the verse id in **1738's numbering** (the draft as it
stands); a split's follow-on uses `+split` as in 1 Samuel's file.

Each row: `op	at	anchor	approved	note`, the note quoting the KJV words that place it and the Latin
(*italic*), ending `(Claude, 2026-11-22, decision 30's standing rule)`. Status is `approved` (decision 30).

**Append** your rows, in book order, to `data/versification/1Kgs.draft.edits.tsv` (create it with the header
`op	at	anchor	status	note` if it does not exist; keep the rows already there from earlier aligners). Test:

    python -m pipeline versify 1Kgs --draft --to <your scratch copy of text/draft/1KI.usfm>
    python -m pipeline versify 1Kgs --draft --to <your scratch copy of text/orig/draft/1KI.usfm>

(copy each file to your scratch folder first; `--to` rewrites the copy). Both must report the same words; the KJV
verse-count problems must be gone for every chapter in your range (later chapters will still fail: ignore them).
Then read your range in the renumbered copy against the KJV verse by verse: every verse's Latin must say what its
KJV verse says. Do not run `--apply`; do not edit any other repo file.

Final message: the number of edits by op, the chapters that now match, and the judgment calls (sentence split
across verses left as Castellio divides, any `absent`, any `opens`).

## 1 Kings: what the readers found (verify, don't trust)

1738 has 54 verses in ch. 1 (KJV 53: its 53/54 = KJV 53a/53b), 52 in ch. 7 (KJV 51), 28 in ch. 21 (KJV 29), 54 in
ch. 22 (KJV 53: from 44 it follows the Hebrew, one ahead). Equal counts hide different divisions in at least
chs. 2, 4 (9–15 one ahead), 6 (26–37 one ahead), 7, 8 (1–19), 11, 12, 14, 15, 18, 20, 21, 22. 18:18 now opens at
*Cui ille* and 22:5 at *Sed tibi censeo* (settled at the merge).
