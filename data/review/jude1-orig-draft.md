# Jude 1 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig Jude 1` → `text/orig/draft/JUD.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Jude.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/JUD.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 360 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 6 | read in the OCR, a spelling the approved rules normalize |
| variant | 5 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 3 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 15 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 17 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 407 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **1.11** *iīs* → *eis*: 1573 canvas 929, read on the page: Væ eis (read by Claude, 2026-11-13)
- **1.3** *cum* → *cum*: 1573 canvas 928, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.4** *sōlum* → *solum*: 1573 canvas 928, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.5** *quod* → *quod*: 1573 canvas 928, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.5** *quod* → *quòd*: 1573 canvas 928, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.7** *modō* → *modo*: 1573 canvas 928, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *cum* → *cum*: 1573 canvas 929, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.15** *cum* → *cum*: 1573 canvas 929, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.15** *contrā* → *contrà*: 1573 canvas 929, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *postrēmō* → *postremo*: 1573 canvas 929, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.20** *vērō* → *verò*: 1573 canvas 929, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.24** *vērō* → *verò*: 1573 canvas 929, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.24** *cum* → *cum*: 1573 canvas 929, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.7** *fīnitimæque* → *finitimæque*: 1573 canvas 928, read on the page (guess word: printed "finitimæq;") (Claude, 2026-11-15)
- **1.12** *circumāctæ* → *circumactæ*: 1573 canvas 929, read on the page (guess word: split across lines "cir / cumactæ" with no hyphen visible) (Claude, 2026-11-15)
- **1.4** *negantēs* → *negantes*: 1573 canvas 928, read on the page (none word) (Claude, 2026-11-15)
- **1.19** *animālēs* → *animales|*: 1573 canvas 929, read on the page (none word: no comma printed after it ("c animales spiritum non habentes."); preceded by the note letter c) (Claude, 2026-11-15)

## Spellings the approved rules normalize (6)

*cāritāte* → *charitate*; *cāritātem* → *charitatem*; *cāritātibus* → *charitatibus*; *exspectantēs* → *expectantes*; *henōchus* → *enochus*; *intellegunt* → *intelligunt*

## Printer's spellings no rule covers (4)

*commemorāre* → *comemorare*; *cārissimī* → *charissimi* ×3

## Punctuation not from the OCR (2)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *seruus,*; 1.4 *negantes.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
