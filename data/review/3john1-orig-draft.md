# 3John 1 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 3John 1` → `text/orig/draft/3JN.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/3John.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/3JN.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 167 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 2 | read in the OCR, a spelling the approved rules normalize |
| variant | 3 | read in the OCR, a printer's spelling no rule covers |
| nasal | 5 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 7 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 12 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 196 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **1.1** *cārissimō* → *charissimo*: 1573 canvas 928, read on the page: printed chariſsimo (and Caio) (read by Claude, 2026-11-13)
- **1.2** *ante* → *ante*: 1573 canvas 928, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.3** *cum* → *cùm*: 1573 canvas 928, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **1.4** *quam* → *quàm*: 1573 canvas 928, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *vērō* → *verò*: 1573 canvas 928, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *male* → *malè*: 1573 canvas 928, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **1.12** *vērum* → *verum*: 1573 canvas 928, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.3** *testātī* → *testati*: 1573 canvas 928, read on the page (guess word) (Claude, 2026-11-15)
- **1.1** *Senior* → *SENIOR*: 1573 canvas 928, read on the page (none word: opening word in capitals after the drop-cap S: "SENIOR Caio charissimo,") (Claude, 2026-11-15)
- **1.5** *fidēliter* → *fideliter*: 1573 canvas 928, read on the page (none word: preceded by the note letter a) (Claude, 2026-11-15)
- **1.10** *prohibeat* → *prohibeat*: 1573 canvas 928, read on the page (none word: hyphenated prohi-beat) (Claude, 2026-11-15)
- **1.1** *Gāiō* → *Caio|*: 1573, read on the page: Caio (unread-words pass, decision 58) (Claude, 2026-11-15)

## Spellings the approved rules normalize (2)

*cāritātem* → *charitatem*; *quidquid* → *quicquid*

## Printer's spellings no rule covers (3)

*cārissime* → *charissime* ×3

## Punctuation not from the OCR (1)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.8 *adiutores.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
