# Titus 1–3 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig Titus 1-3` → `text/orig/draft/TIT.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Titus.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/TIT.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 572 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 3 | read in the OCR, a spelling the approved rules normalize |
| variant | 7 | read in the OCR, a printer's spelling no rule covers |
| ę | 2 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 7 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 21 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 18 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 630 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **3.2** *exserentēs* → *exerentes*: 1573 canvas 915, read on the page: no s after x (read by Claude, 2026-11-13)
- **1.1** *quod* → *quod*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.2** *cum* → *cum*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.2** *quam* → *quam*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.2** *ante* → *ante*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.3** *quod* → *quod*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.4** *quod* → *quod*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *quō* → *quo*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.13** *vērum* → *verum*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.14** *quō* → *quo*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.15** *cum* → *cum*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.6** *quō* → *quo*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.6** *largē* → *largè*: 1573 canvas 915, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **3.10** *post* → *post*: 1573 canvas 915, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.15** *īnfidēlibus* → *infidelibus*: 1573 canvas 915, read on the page (none word: hyphenated in-fidelibus) (Claude, 2026-11-15)
- **2.8** *adversāriī* → *aduersarij*: 1573 canvas 915, read on the page (none word: printed with ij; hyphenated ad-uersarij) (Claude, 2026-11-15)
- **2.12** *mundānīsque* → *mundanisque*: 1573 canvas 915, read on the page (none word: printed with the abbreviation "-q;" (mundanisq;)) (Claude, 2026-11-15)
- **3.10** *admonitiōnem* → *admonitionem*: 1573 canvas 915, read on the page (none word) (Claude, 2026-11-15)

## Spellings the approved rules normalize (3)

*exspectantēs* → *expectantes*; *iīs* → *eis*; *obœdientēs* → *obedientes*

## Printer's spellings no rule covers (7)

*auctōritāte* → *authoritate*; *exstitit* → *extitit* ×2; *fēminās* → *fœminas*; *hiemāre* → *hyemare*; *hērēdēs* → *hæredes*; *numquam* → *nunquam*

## Punctuation not from the OCR (1)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

3.2 *exerentes.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
