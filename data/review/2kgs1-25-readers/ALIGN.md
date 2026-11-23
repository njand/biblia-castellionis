# 2 Kings, phase 1: moving 1738's verses to the KJV's numbering (brief for each aligner)

Repo: `C:\Users\nathanjamesanderson\Documents\biblia-castellionis`. Aligners run one after another, each on a
range of chapters, adding to one edits file. Read first: `pipeline/versify.py`'s docstring (the ops: `split`,
`merge`, `chapter`, `opens`, `range`, `absent`), and `data/versification/1Kgs1-22.draft.edits.tsv` (1 Kings'
196 edits, done the same way: copy the style of their notes exactly).

## What you have

- `text/draft/2KI.usfm`: the draft, in **1738's own numbering** (its margin numbers), modern spelling (*Jovam*,
  *ejus*). Do not edit it.
- `text/orig/draft/2KI.usfm`: the printed text, same numbering, 1738's spelling (*Iouam*, *eius*; misprints kept, e.g. *Ezechiani*, *eubitus*). Do not edit it.
- KJV `sources/parallel/kjv/2Kgs.tsv`, BSB `sources/parallel/bsb/2Kgs.tsv`, Hebrew `sources/parallel/wlc/2Kgs.tsv`,
  Vulgate `sources/parallel/vulgate/2Kgs.tsv`; KJV verse counts `data/versification/kjv.tsv`.
- The readers' notes (`data/review/2kgs1-25-transcription-readers.md`, by reader; Claude's settlements at its head) say where 1738 divides differently.

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

**Append** your rows, in book order, to `data/versification/2Kgs.draft.edits.tsv` (create it with the header
`op	at	anchor	status	note` if it does not exist; keep the rows already there from earlier aligners). Test:

    python -m pipeline versify 2Kgs --draft --to <your scratch copy of text/draft/2KI.usfm>
    python -m pipeline versify 2Kgs --draft --to <your scratch copy of text/orig/draft/2KI.usfm>

(copy each file to your scratch folder first; `--to` rewrites the copy). Both must report the same words; the KJV
verse-count problems must be gone for every chapter in your range (later chapters will still fail: ignore them).
Then read your range in the renumbered copy against the KJV verse by verse: every verse's Latin must say what its
KJV verse says. Do not run `--apply`; do not edit any other repo file.

Final message: the number of edits by op, the chapters that now match, and the judgment calls (sentence split
across verses left as Castellio divides, any `absent`, any `opens`).

## 2 Kings: what the readers found (verify, don't trust)

1738 has 28 verses in ch. 3 (KJV 27), 34 in ch. 6 (KJV 33), 30 in ch. 8 (KJV 29), 20 in ch. 11 (KJV 21: KJV 11:21 is
1738's 12:1), 37 in ch. 15 (KJV 38: KJV 15:38 is 1738's 16:1), 20 in ch. 20 (KJV 21: KJV 20:21 is in 1738's 21:1)
and 25 in ch. 21 (KJV 26: KJV 21:26 is in 1738's 22:1). Equal counts hide different divisions in at least chs. 2, 4,
9 (19–21), 10, 13, 17 (four behind from 15, caught up by 40), 19 (3–6, 16, 23), 21 (1–8), 22 (1–6), 23 (31–37), 24
(1–4, 12–16) and 25 (16–17, 21–22). Claude's settlements at the head of the readers' notes say which margin
placements were looked at (2:4, 4:26, 10:29 are the printer's starts, not the KJV's).
