# Exodus 31–40: how to build the base text without Wikisource (proposal)

Proposed 2026-11-14. Wikisource has no Exodus 31–40, so stage 1 has no transcription to start from (PLAN.md §7,
M4; the same holds for M6: Numbers, Deuteronomy, Chronicles, Psalms, the Prophets). **Waiting for your answer before
anything is drafted.**

**Decision:** accepted, with the check on Exodus 21–23 only, summaries left out and not recorded (Nathan, 2026-11-14; decisions 67, 68)

## The witnesses

| Witness | What it is | Measured (`data/calibration/witnesses.md`) |
|---|---|---|
| **1738** (the base, decision 1) | ABBYY OCR with word boxes (`sources/archive/1738/hocr.html`); Exodus 31–40 is leaves 145–156 | Genesis: 89.8% of words found, 89.3% read right (f/s-blind 88.5%) |
| 1750 | Tesseract OCR, noisy (`sources/archive/1750/text.txt`) | 93.7% found, 93.5% read right |
| 1726–27 (`TXT/1 - OCR`) | Google Books OCR; its two columns are interleaved line by line, so whole lines alternate between verses | 43.6% found, 97.0% read right |
| your 1726 text (`TXT/3 - Edited`) | stops at Exodus 20 | — |

## A test on Exodus 21–30, where there is an answer key

A prototype (not in the pipeline) took 1738's OCR from 21:1 to 30:38 as the backbone, aligned 1750 and 1726 to it
word by word, and kept a word where it, or a repair of it (long s, *rn* for *m*, *x* for *æ*, *cl* for *ct*), or the
other witnesses' reading, is a known Latin form (the settled text's, 1738's printed forms from stage 2b, the
`latin macron` lexicon). Against the stage-2 draft of 21–30 (Wikisource corrected on the page images):
**84% of the 4,785 words came out the same word.** Most of the rest are 1738's chapter summaries, headings,
footnotes and footnote letters read into the text (the OCR has 5,240 tokens for 4,785 words), OCR words no repair
reaches (*taberionacidi*), and 1750/1726 failing to align where 1738 is weakest. With the summaries, headings and
footnotes left out by position (as the indent reader already does), I would expect 88–92%, which still leaves some
400–600 words in ten chapters wrong.

## Proposed route

1. **Stage 1, a draft from 1738 itself** (`pipeline draft Exod 31-40 --from-ocr`, new): 1738's hOCR, leaves 145–156,
   column by column, without running heads, catchwords, the italic chapter summaries (left out, decision 50),
   footnotes, and marginal notes; 1738's verse numbers from the margins as verse markers; each word voted with 1750
   and 1726 as above, and the word's leaf and line kept.
2. **Stage 2 by reading every column on the page images**: I read each of the ~22 columns (as crops of 12–15 lines,
   with the draft beside them) and correct every word that differs, recording each correction with its leaf in
   `data/review/exod31-40-stage2.md`, as for 1–30. Unlike Wikisource chapters, every word is then read on the page,
   not only the disputed ones. Where the page is unclear (a broken letter, a bleed-through), 1750 decides, and the
   item says so.
3. **Stage 2b comes almost free**: the draft is already 1738's spelling, so its printed text (`text/orig/draft/`) is
   the read text itself, with its paragraphs from the indents. Every word is read, so no *doubt* or *prone*
   words should remain.
4. **For stages 3–5 the draft needs Wikisource's conventions first**: u/v and i/j modernized (normalize's j/v rules),
   *&*, *q;* expanded, ligatures as *ae/oe*. Then `versify` to the KJV, `propose`, and readers as for 21–30.
5. **First, a check on Exodus 21–30**: build steps 1–2 there too and compare with the Wikisource route's result. That
   measures how many words the page reading misses before it is trusted for books with no Wikisource text (M6).

Effort: steps 1 and 4 are code (a day's work with tests); step 2 is about 22 columns of reading plus the check on
21–30 (about 25 more).

## Questions for you

1. Go ahead with this route, and the check on 21–30 first?
2. Keep the italic chapter summaries out of the draft (decision 50 leaves them out of the reading edition; the
   printed text's open question 2 asks whether it should keep them)?
