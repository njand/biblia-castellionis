# Jude 1 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Jude 1` → `text/orig/draft/JUD.usfm` (now `text/orig/JUD.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Jude.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/JUD.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 372 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 6 | read in the OCR, a spelling the approved rules normalize |
| variant | 5 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 3 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 15 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 1 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 2 | OCR unreadable; the settled word in the printer's conventions |
| none | 2 | no OCR word; the settled word in the printer's conventions |
| all | 407 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **1.11** *iīs* → *eis*: 1573 canvas 929, read on the page: Væ eis (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (6)

*cāritāte* → *charitate*; *cāritātem* → *charitatem*; *cāritātibus* → *charitatibus*; *exspectantēs* → *expectantes*; *henōchus* → *enochus*; *intellegunt* → *intelligunt*

## Printer's spellings no rule covers (4)

*commemorāre* → *comemorare*; *cārissimī* → *charissimi* ×3

## Not read in the OCR (4)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Jude.1.4 | negantēs | negantes | — |
| Jude.1.7 | fīnitimæque | finitimæque | finitimæ |
| Jude.1.12 | circumāctæ | circumactæ | cir cumactæ |
| Jude.1.19 | animālēs | animales | — |

## Punctuation not from the OCR (3)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *seruus,*; 1.4 *negantes.*; 1.19 *animales,*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
