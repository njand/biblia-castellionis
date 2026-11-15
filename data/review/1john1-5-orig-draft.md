# 1John 1–5 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 1John 1-5` → `text/orig/draft/1JN.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1John.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/1JN.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1598 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 13 | read in the OCR, a spelling the approved rules normalize |
| variant | 22 | read in the OCR, a printer's spelling no rule covers |
| ę | 6 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 10 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 118 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 87 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 1854 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **1.3** *adnūntiāmus* → *anunciamus*: 1573 canvas 925, read on the page: anũcia-mus (read by Claude, 2026-11-13)
- **1.1** *Quod* → *QVOD*: 1573 canvas 925, read on the page: chapter opening in capitals; no accent (accents, decision 67) (Claude, 2026-11-14)
- **1.1** *quod* → *quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.1** *quod* → *quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.1** *quod* → *quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.3** *quod* → *Quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.3** *cum* → *cum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.5** *quod* → *quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.5** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *cum* → *cum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *vērum* → *verum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.2** *sōlum* → *solùm*: 1573 canvas 925, read on the page: faint grave on u (necsolùm) (accents, decision 67) (Claude, 2026-11-14)
- **2.3** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.4** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.5** *vērō* → *verò*: 1573 canvas 925, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.5** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.6** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.7** *quam* → *quam*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.8** *vērum* → *verum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *vērō* → *verò*: 1573 canvas 925, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *cum* → *quum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.19** *Ā* → *A*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.20** *ā* → *à*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *ideō* → *ideo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *quod* → *quòd*: 1573 canvas 925, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *vērum* → *verum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *vērum* → *verum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *quod* → *quòd*: 1573 canvas 925, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *vērō* → *vero*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.24** *Quod* → *Quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.24** *quod* → *quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.25** *quod* → *quod*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.27** *quam* → *quam*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.27** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.27** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.28** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.28** *cum* → *cum*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.29** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.1** *quantō* → *quanto*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.1** *Ideō* → *Ideo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.2** *cum* → *cùm*: 1573 canvas 926, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **3.3** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.5** *ideō* → *ideo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.5** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.6** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.8** *Ideō* → *Ideo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.9** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.10** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.11** *quam* → *quam*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.20** *Quod* → *Quod*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.22** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.24** *quō* → *quo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.3** *quod* → *quod*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.5** *ā* → *à*: 1573 canvas 926, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **4.9** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.9** *quod* → *quòd*: 1573 canvas 926, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **4.10** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.11** *mūtuō* → *mutuò*: 1573 canvas 926, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **4.13** *eō* → *eo*: 1573 canvas 925, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.15** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *quō* → *quo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.17** *eō* → *eo*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.17** *quod* → *quod*: 1573 canvas 926, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.20** *ā* → *à*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.21** *eō* → *eo*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.6** *Hic* → *Hic*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.6** *sōlum* → *solum*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.9** *quod* → *quod*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.10** *quod* → *quòd*: 1573 canvas 927, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **5.10** *quod* → *quod*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.11** *quod* → *quòd*: 1573 canvas 927, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **5.14** *quam* → *quam*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.15** *Quod* → *Quòd*: 1573 canvas 927, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **5.15** *eō* → *eo*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.15** *eō* → *eo*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.16** *quō* → *quo*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.20** *eō* → *eo*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.20** *vērum* → *verum*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.20** *vērō* → *vero*: 1573 canvas 927, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.4** *scrībimus* → *scribimus*: 1573 canvas 925, read on the page (guess word: printed with the -us abbreviation: "scribim⁹") (Claude, 2026-11-15)
- **4.12** *sumusque* → *sumusque*: 1573 canvas 926, read on the page (guess word: printed "sumusq;" (page stained, legible)) (Claude, 2026-11-15)
- **5.20** *æternaque* → *æternaque*: 1573 canvas 927, read on the page (guess word: hyphenated æ-ternaque) (Claude, 2026-11-15)
- **4.9** *patuit* → *patuit*: 1573 canvas 926, read on the page (none word) (Claude, 2026-11-15)
- **4.9** *ūnicum* → *vnicum*: 1573 canvas 926, read on the page (none word) (Claude, 2026-11-15)
- **4.20** *amārī* → *amari*: 1573 canvas 927, read on the page (none word) (Claude, 2026-11-15)
- **5.20** *ingeniō* → *ingenio*: 1573 canvas 927, read on the page (none word: hyphenated inge-nio) (Claude, 2026-11-15)

## Spellings the approved rules normalize (13)

*adulēscentēs* → *adolescentes*; *cāritāte* → *charitate* ×2; *intellegimus* → *intelligimus* ×3; *intellegāmus* → *intelligamus*; *obœdit* → *obedit*; *quidquid* → *quicquid* ×4; *quīcumque* → *quicunque*

## Printer's spellings no rule covers (22)

*audīstis* → *audiuistis* ×6; *commūnitās* → *comunitas*; *commūnitātem* → *comunitatem*; *cælō* → *cœlo*; *cārissimī* → *charissimi* ×4; *dēnūntiātiō* → *denunciatio*; *exsistet* → *existet*; *lētāle* → *lethale* ×2; *lētāliter* → *lethaliter*; *nūntium* → *nuncium*; *nūntiāmus* → *nunciamus* ×2; *umquam* → *vnquam*

## Punctuation not from the OCR (15)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.6 *facimus.*; 3.18 *amemus.*; 4.1 *Charissimi,*; 4.8 *amat,*; 4.8 *Deum:*; 4.8 *est.*; 4.9 *amor,*; 4.9 *mundum,*; 4.19 *amauit.*; 4.20 *dicit,*; 4.20 *odit,*; 4.20 *est.*; 4.20 *suum,*; 4.20 *vidit,*; 5.1 *amat.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
