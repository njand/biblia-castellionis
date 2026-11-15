# 2Pet 1–3 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 2Pet 1-3` → `text/orig/draft/2PE.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Pet.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/2PE.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 895 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 15 | read in the OCR, a spelling the approved rules normalize |
| variant | 18 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 7 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 35 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 43 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 1014 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **2.12** *iīs* → *eis*: 1573 canvas 923, read on the page (read by Claude, 2026-11-13)
- **1.9** *vērō* → *verò*: 1573 canvas 923, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *largē* → *largè*: 1573 canvas 923, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **1.15** *post* → *post*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.17** *ā* → *à*: 1573 canvas 923, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *cum* → *quum*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *cum* → *cum*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *eō* → *eo*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *Hic* → *Hic*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *quō* → *quo*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.19** *quod* → *quod*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.19** *quod* → *quod*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *Cum* → *cùm*: 1573 canvas 923, read on the page: grave on u (printed lower-case cùm) (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *contrā* → *contra*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.19** *quō* → *quo*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.22** *quod* → *quod*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.22** *vērō* → *vero*: 1573 canvas 923, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.4** *quō* → *quo*: 1573 canvas 924, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.10** *quā* → *qua*: 1573 canvas 924, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.12** *quam* → *quam*: 1573 canvas 924, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.14** *cum* → *cum*: 1573 canvas 924, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.15** *quā* → *qua*: 1573 canvas 924, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.1** *sectās* → *sectas*: 1573 canvas 923, read on the page (guess word: hyphenated se-ctas) (Claude, 2026-11-15)
- ⚑ **2.10** *dignitātibus* → *dignitatib.*: 1573 canvas 923, read on the page (guess word: abbreviated: prints "dignitatib." (the point is the abbreviation mark, not punctuation)) (Claude, 2026-11-15)
- **2.15** *Balaamī* → *Balaami|*: 1573 canvas 923, read on the page (guess word: no comma printed after it: "Balaami Bosoris filij") (Claude, 2026-11-15)
- **3.16** *indoctī* → *indocti*: 1573 canvas 924, read on the page (guess word: hyphenated indo-cti) (Claude, 2026-11-15)
- **2.14** *īnfirmās* → *infirmas*: 1573 canvas 923, read on the page (misread word) (Claude, 2026-11-15)
- **2.22** *vomitum* → *vomitum*: 1573 canvas 923, read on the page (misread word) (Claude, 2026-11-15)
- **1.5** *acquīrentēs* → *acquirentes*: 1573 canvas 923, read on the page (prone word: only "rentes in fide vestra" visible at the top of the page; the first part is on the previous page/column, not seen) (Claude, 2026-11-15)
- **1.4** *corruptēlam* → *corruptelam*: 1573 canvas 922, read on the page (none word: read on page 922 ("mundanam cupiditatis corruptelam ef-fugiatis."); the crop missed it) (Claude, 2026-11-15)
- **1.4** *effugiātis* → *effugiatis*: 1573 canvas 922, read on the page (none word: hyphenated ef-fugiatis (page 922)) (Claude, 2026-11-15)
- **1.12** *commonefacere* → *commonefacere*: 1573 canvas 923, read on the page (none word: hyphenated com-monefacere) (Claude, 2026-11-15)
- **1.12** *fīxōs* → *fixos*: 1573 canvas 923, read on the page (none word) (Claude, 2026-11-15)
- **1.16** *dēclārāvimus* → *declarauimus*: 1573 canvas 922, read on the page (none word: hyphenated declara-uimus; read on page 923 (the crop showed 1.1)) (Claude, 2026-11-15)
- **1.17** *magnificā* → *magnifica*: 1573 canvas 923, read on the page (none word: hyphenated magnifi-ca) (Claude, 2026-11-15)
- **2.8** *cruciābat* → *cruciabat*: 1573 canvas 923, read on the page (none word: hyphenated crucia-bat (page 923)) (Claude, 2026-11-15)
- **2.10** *horrent* → *horrent|:*: 1573 canvas 923, read on the page (none word: 1573 prints a colon after it) (Claude, 2026-11-15)
- **2.11** *ferant* → *ferant*: 1573 canvas 923, read on the page (none word: hyphenated fe-rant) (Claude, 2026-11-15)
- **2.15** *convictus* → *conuictus*: 1573 canvas 923, read on the page (none word) (Claude, 2026-11-15)
- **2.21** *recessisse* → *recessisse*: 1573 canvas 923, read on the page (none word) (Claude, 2026-11-15)
- **2.22** *cænī* → *cœni*: 1573 canvas 923, read on the page (none word: printed with œ: "ad cœni") (Claude, 2026-11-15)
- **2.22** *volūtābrum* → *volutabrum*: 1573 canvas 923, read on the page (none word) (Claude, 2026-11-15)
- **3.12** *elementa* → *elementa*: 1573 canvas 924, read on the page (none word: hyphenated elemen-ta) (Claude, 2026-11-15)

## Spellings the approved rules normalize (15)

*condiciō* → *conditio*; *cotīdiānīs* → *quotidianis*; *cāritātem* → *charitatem*; *epistulīs* → *epistolis*; *erum* → *herum*; *exspectandīs* → *expectandis*; *exspectāmus* → *expectamus*; *gomorræque* → *gomorrhæque*; *intellegātis* → *intelligatis*; *iīs* → *eis* ×3; *iīsque* → *eisque*; *neglegam* → *negligam*; *quemquam* → *quenquam*

## Printer's spellings no rule covers (18)

*cælī* → *cœli* ×2; *cælō* → *cœlo*; *cārissimus* → *charissimus* ×2; *cārissimī* → *charissimi* ×4; *cētera* → *cætera*; *litterās* → *literas*; *numquam* → *nunquam*; *quamdiū* → *quandiu*; *quamquam* → *quanquam*; *umquam* → *vnquam*; *vērumtamen* → *veruntamen*; *ōtiātur* → *ociatur*; *ōtiōsōs* → *ociosos*

## Punctuation not from the OCR (7)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.2 *cognitione:*; 1.9 *peccatorum.*; 1.12 *fixos.*; 1.21 *diuini.*; 2.15 *est.*; 2.21 *recessisse:*; 2.22 *volutabrum.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
