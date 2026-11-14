# 2John 1 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 2John 1` → `text/orig/draft/2JN.usfm` (now `text/orig/2JN.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2John.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/2JN.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 197 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 1 | read in the OCR, a spelling the approved rules normalize |
| variant | 2 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 1 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 7 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| none | 2 | no OCR word; the settled word in the printer's conventions |
| all | 211 | |

## Spellings the approved rules normalize (1)

*cāritāte* → *charitate*

## Printer's spellings no rule covers (2)

*audīstis* → *audiuistis*; *introiērunt* → *introiuerunt*

## Not read in the OCR (2)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 2John.1.1 | Senior | Senior | — |
| 2John.1.6 | præceptiōne | præceptione | — |

## Punctuation not from the OCR (1)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.4 *Patre.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
