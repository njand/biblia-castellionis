# 2 Samuel, phase 1: moving 1738's verses to the KJV's numbering (brief for each aligner)

Repo: `C:\Users\nathanjamesanderson\Documents\biblia-castellionis`. Aligners run one after another, each on a
range of chapters, adding to one edits file. Read first: `pipeline/versify.py`'s docstring (the ops: `split`,
`merge`, `chapter`, `opens`, `range`, `absent`), and `data/versification/1Sam1-31.draft.edits.tsv` (1 Samuel's
318 edits, done the same way: copy the style of their notes exactly).

## What you have

- `text/draft/2SA.usfm`: the draft, in **1738's own numbering** (its margin numbers), modern spelling (*Jovam*,
  *ejus*). Do not edit it.
- `text/orig/draft/2SA.usfm`: the printed text, same numbering, 1738's spelling (*Iouam*, *eius*). Do not edit it.
- KJV `sources/parallel/kjv/2Sam.tsv`, BSB `sources/parallel/bsb/2Sam.tsv`, Hebrew `sources/parallel/wlc/2Sam.tsv`,
  Vulgate `sources/parallel/vulgate/2Sam.tsv`; KJV verse counts `data/versification/kjv.tsv`.
- The readers' notes `data/review/2sam1-24-readers/reader-NN.md` say where 1738 divides differently.

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
(*italic*), ending `(Claude, 2026-11-21, decision 30's standing rule)`. Status is `approved` (decision 30).

**Append** your rows, in book order, to `data/versification/2Sam.draft.edits.tsv` (create it with the header
`op	at	anchor	status	note` if it does not exist; keep the rows already there from earlier aligners). Test:

    python -m pipeline versify 2Sam --draft --to <your scratch copy of text/draft/2SA.usfm>
    python -m pipeline versify 2Sam --draft --to <your scratch copy of text/orig/draft/2SA.usfm>

(copy each file to your scratch folder first; `--to` rewrites the copy). Both must report the same words; the KJV
verse-count problems must be gone for every chapter in your range (later chapters will still fail: ignore them).
Then read your range in the renumbered copy against the KJV verse by verse: every verse's Latin must say what its
KJV verse says. Do not run `--apply`; do not edit any other repo file.

Final message: the number of edits by op, the chapters that now match, and the judgment calls (sentence split
across verses left as Castellio divides, any `absent`, any `opens`).
