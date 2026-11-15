# 2Thess 1–3 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 2Thess 1-3` → `text/orig/draft/2TH.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Thess.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/2TH.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 664 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 9 | read in the OCR, a spelling the approved rules normalize |
| variant | 7 | read in the OCR, a printer's spelling no rule covers |
| nasal | 5 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 19 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 35 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 739 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **1.6** *afflīgentibus* → *affligentibus*: 1573 canvas 907, read on the page: af-|fligentibus, lower case mid-sentence (read by Claude, 2026-11-13)
- **1.3** *adeō* → *adeò*: 1573 canvas 907, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.3** *vestrum* → *vestrûm*: 1573 canvas 907, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **1.4** *quā* → *qua*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.5** *Quod* → *quod*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.5** *quō* → *quo*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.7** *cum* → *cum*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *eō* → *eo*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.12** *quō* → *quò*: 1573 canvas 907, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.12** *eō* → *eo*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.1** *quod* → *quod*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.3** *modō* → *modo*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.4** *suprā* → *supra*: 1573 canvas 907, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.7** *tantum* → *tantùm*: 1573 canvas 907, read on the page: grave on u; only -tùm seen at the crop's left edge (word starts before it) (accents, decision 67) (Claude, 2026-11-14)
- **2.9** *cum* → *cum*: 1573 canvas 908, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *quō* → *quo*: 1573 canvas 908, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.12** *quō* → *quò*: 1573 canvas 908, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.13** *quod* → *quòd*: 1573 canvas 908, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.14** *quod* → *quod*: 1573 canvas 908, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.1** *Quod* → *QVod*: 1573 canvas 908, read on the page: chapter opening, drop cap Q then capital V; no accent (accents, decision 67) (Claude, 2026-11-14)
- **3.6** *quam* → *quam*: 1573 canvas 908, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.13** *vērō* → *verò*: 1573 canvas 908, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **3.17** *quod* → *quòd*: 1573 canvas 908, read on the page: grave on o (faint but visible) (accents, decision 67) (Claude, 2026-11-14)
- **2.16** *æternōque* → *æternoque*: 1573 canvas 908, read on the page (guess word: hyphenated æter-noq;) (Claude, 2026-11-15)
- **3.4** *factūrōs* → *facturos*: 1573 canvas 908, read on the page (guess word: hyphenated fa-cturos (first half beyond the crop edge)) (Claude, 2026-11-15)
- **3.7** *intemperanter* → *intemperanter*: 1573 canvas 908, read on the page (guess word) (Claude, 2026-11-15)
- **1.1** *Silvānus* → *SYLVAnus*: 1573 canvas 907, read on the page (prone word: not on crop (crop shows 2Thess.2.6); read on page 0907: book opening "PAVLVS ET SYLVA-nus, & Thimotheus", with Y (Syluanus), capitals for the first line then lower-case "nus" after the hyphen) (Claude, 2026-11-15)
- **1.8** *irrogātūrus* → *irrogaturus*: 1573 canvas 907, read on the page (none word: followed by the note letter a) (Claude, 2026-11-15)
- **1.8** *nescientibus* → *nescientibus*: 1573 canvas 907, read on the page (none word: hyphenated ne-scientibus) (Claude, 2026-11-15)
- **2.1** *Rogāmus* → *ROgamus*: 1573 canvas 906, read on the page (none word: chapter opening: drop-cap R followed by capital O ("ROgamus"), read on page 907 (the crop showed 1Thess 5.12)) (Claude, 2026-11-15)
- **2.2** *auctōrēs* → *authores*: 1573 canvas 907, read on the page (none word: printed "authores" (hyphenated au-thores: "cuius nos au- / thores esse videamur"), not "auctores") (Claude, 2026-11-15)
- **2.8** *clāritāte* → *claritate*: 1573 canvas 908, read on the page (none word: hyphenated clari-tate) (Claude, 2026-11-15)
- **2.8** *dēlēbit* → *delebit*: 1573 canvas 908, read on the page (none word) (Claude, 2026-11-15)
- **2.10** *scelerum* → *scelerum*: 1573 canvas 908, read on the page (none word) (Claude, 2026-11-15)
- **3.8** *accēperīmus* → *acceperimus*: 1573 canvas 908, read on the page (none word: hyphenated accepe-rimus (page 908)) (Claude, 2026-11-15)

## Spellings the approved rules normalize (9)

*cāritās* → *charitas*; *cāritātem* → *charitatem*; *epistulā* → *epistola* ×2; *epistulīs* → *epistolis*; *iīs* → *eis*; *obœdientibus* → *obedientibus*; *quidquid* → *quicquid*; *quīcumque* → *quicunque*

## Printer's spellings no rule covers (7)

*cælō* → *cœlo*; *dēnūntiāmus* → *denunciamus*; *exsistat* → *existat*; *exsistet* → *existet* ×2; *tamquam* → *tanquam*; *tīmotheus* → *thimotheus*

## Punctuation not from the OCR (4)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

2.8 *delebit:*; 2.17 *confirmet.*; 3.18 *gratia:*; 3.18 *Amen.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
