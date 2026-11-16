# Castellio's text as printed, Leviticus (1738): proposed for approval

Built 2026-11-16 (`python -m pipeline orig Lev 1-11`, `orig Lev 12-27 --read-lines`). The draft is
`text/orig/draft/LEV.usfm`; how each word of 1–11 was made, word by word, is in `lev1-11-orig.md`, and 12–27's lines
in `lev12-27-stage2.md`. This file is the summary, the questions, and the Decision line.

**Decision:** approved (Nathan, 2026-11-16: "Approve it"; his answers to the three questions above); moved to `text/orig/LEV.usfm`.

## How it was made

- **Chapters 12–27** are 1738's own lines, every one read on the page in stage 2 (`data/witnesses/read-1738/
  Lev12-27.tsv`), set as printed (`orig --read-lines`), versified by the draft's edits.
- **Chapters 1–11** are the settled words in 1738's spelling and punctuation, read from its OCR where it read them
  (4,014 words), and **on the page for every other word** (decision 68, as Genesis and Exodus): 689 places on
  contact sheets of each word's lines (`sources/archive/crops/`, `orig.sheets`' method), by six readers, each word
  with the mark printed after it; and 33 more by me (the chapter openings, the misprints, the punctuation the settled
  text had brought in). Each is a row in `data/decisions/Lev.orig.tsv` (722 rows). Nothing in 1–11 is now taken
  from the settled text or a guess: the review file's lists of words and marks not read are empty.
- **Paragraphs**: 1738's indents. All 29 inside chapters 1–11 were looked at on the page: 28 are indents; the one at
  3:5 was set a line early and is now at 3:6 *Quod si ouino* (rows `¶-`, `¶`). In 12–27 the three doubtful ones:
  12:1 *hæc Israelitis* and 13:2 *homo, cuius* are the lines beside the chapter's drop capital, not paragraphs
  (taken away by `¶-` rows; `orig.verse_paragraph_rows` now takes a row inside a verse, tested); 16:29 *Mensis
  septimi* is a true indent after *tenetote.*, kept.

## What the page changed (all kept as printed, decision 58)

- **Capitals and stops**: 1:12 *victima* and 6:28 *detergitor* lower case after a stop; 4:32 *Quod*, 11:6 *Et*
  capital; 10:4 *auferrent* lower case; 11:2 *adloquimini* lower case after the colon; 6:12 *inexstinctus* no colon,
  6:16 *tabernaculi:*, 6:25 *victima,*, 11:38 *deciderit* no comma, 7:1 *Noxæ autem hæc* and 9:1 *Vbi dies octaua*
  no comma, 4:1 *inquit:*, 7:28 *(inquit)*, 8:14 *eum, quum*, 11:35 *diruuntor:* and *habenda. (nam*; the stray
  parentheses the OCR had made at 3:2, 4:6, 6:24, 11:37 gone.
- **Spellings**: *quum* where the settled text has *cum* (8:14, 10:3, 11:4 and the rest the OCR read), *adp-*,
  *adl-* unassimilated (8:26, 9:4, 11:2), 10:4 *Elisaphanem*, 10:1 *Ioue* (1738's misprint), 1:1 *VOCAVIT* in
  capitals (as Gen 1:1 *PRINCIPIO*).

## Questions (answered by Nathan, 2026-11-16, on the enlarged crops in `lev-orig-questions.png`)

1. ~~**3:13 *idque anre oraculare***~~ **ante** ("1. ante"): the letter after *an* (leaf 158, line 31), with neither
   the stem nor the cross of a t, is a broken t. The printed text reads *ante*.
2. ~~**7:28 *(irquit)***~~ **inquit**, a badly inked n (leaf 162, line 47), as drafted.
3. ~~**Worn or stained letters**~~ **as drafted** ("All of the other 'printed text now' transcriptions are accurate"):
   1:9 *cremandæ*, 9:12 *sanguinemque*, 6:27 *consecrator*, 7:10 *habento*, 7:12 *similam*, 7:18 *salute*, 8:13
   *mandatum*, 10:6 *detis*, 11:24 and 11:25 *pollutus* (the same r-like t in both), 11:29 *mustelam*; 8:25 *ambos*,
   *dextrum* and 8:26 *panum* under the stain.
