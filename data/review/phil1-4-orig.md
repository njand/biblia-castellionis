# Phil 1–4 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Phil 1-4` → `text/orig/draft/PHP.usfm` (now `text/orig/PHP.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Phil.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/PHP.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1433 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 8 | read in the OCR, a spelling the approved rules normalize |
| variant | 19 | read in the OCR, a printer's spelling no rule covers |
| ę | 2 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 15 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 52 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 2 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 3 | OCR unreadable; the settled word in the printer's conventions |
| none | 5 | no OCR word; the settled word in the printer's conventions |
| all | 1539 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **2.30** *negōtium* → *negotium*: 1573 canvas 899, read on the page: negotiũ (read by Claude, 2026-11-13)
- **3.1** *Cēterum* → *Cæterum*: 1573 canvas 900, read on the page: drop cap C + Æterum (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (8)

*cāritāte* → *charitate* ×2; *cāritātis* → *charitatis*; *exspectō* → *expecto*; *iīs* → *eis*; *miseritus* → *misertus*; *obœdiēns* → *obediens*; *quotiēns* → *quoties*

## Printer's spellings no rule covers (19)

*assecūtum* → *assequutum*; *audīstis* → *audiuistis*; *commiserātiō* → *comiseratio*; *commūniō* → *comunio*; *cārissimī* → *charissimi* ×2; *cārī* → *chari*; *cēterum* → *cæterum*; *cēterīsque* → *cæterisque*; *exsuperāns* → *exuperans*; *nēquidquam* → *nequicquam* ×2; *opportūnitāte* → *oportunitate*; *quamquam* → *quanquam*; *quīnimmo* → *quinimo*; *sollicitī* → *soliciti*; *sæcula* → *secula*; *tamquam* → *tanquam*; *vērumtamen* → *veruntamen*

## e against the settled æ, printed æ (1)

*ægrōtāvit* → *ægrotauit*

## Not read in the OCR (8)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Phil.1.14 | impavidī | impauidi | — |
| Phil.1.20 | ēvehātur | euehatur | — |
| Phil.2.2 | ūnanimēs | vnanimes | vnanines |
| Phil.2.17 | operātiōne | operatione | — |
| Phil.2.25 | vicārium | vicarium | vicariuin |
| Phil.3.1 | piget | piget | — |
| Phil.3.2 | concīsōs | concisos | con |
| Phil.4.8 | virtūs | virtus | — |

## Punctuation not from the OCR (7)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.7 *est,*; 1.7 *habeam,*; 1.14 *facere.*; 2.24 *veniam.*; 3.1 *scribere,*; 3.1 *piget,*; 3.2 *concisos.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
