# 1John 1–5 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 1John 1-5` → `text/orig/draft/1JN.usfm` (now `text/orig/1JN.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1John.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/1JN.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1666 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 14 | read in the OCR, a spelling the approved rules normalize |
| variant | 22 | read in the OCR, a printer's spelling no rule covers |
| ę | 6 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 12 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 126 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 1 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 3 | OCR unreadable; the settled word in the printer's conventions |
| none | 4 | no OCR word; the settled word in the printer's conventions |
| all | 1854 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **.1.3** *adnūntiāmus* → *anunciamus*: 1573 canvas 925, read on the page: anũcia-mus (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (14)

*adulēscentēs* → *adolescentes*; *cum* → *quum*; *cāritāte* → *charitate* ×2; *intellegimus* → *intelligimus* ×3; *intellegāmus* → *intelligamus*; *obœdit* → *obedit*; *quidquid* → *quicquid* ×4; *quīcumque* → *quicunque*

## Printer's spellings no rule covers (22)

*audīstis* → *audiuistis* ×6; *commūnitās* → *comunitas*; *commūnitātem* → *comunitatem*; *cælō* → *cœlo*; *cārissimī* → *charissimi* ×4; *dēnūntiātiō* → *denunciatio*; *exsistet* → *existet*; *lētāle* → *lethale* ×2; *lētāliter* → *lethaliter*; *nūntium* → *nuncium*; *nūntiāmus* → *nunciamus* ×2; *umquam* → *vnquam*

## Not read in the OCR (7)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 1John.1.4 | scrībimus | scribimus | scribim |
| 1John.4.9 | patuit | patuit | — |
| 1John.4.9 | ūnicum | vnicum | — |
| 1John.4.12 | sumusque | sumusque | funtis |
| 1John.4.20 | amārī | amari | — |
| 1John.5.20 | ingeniō | ingenio | — |
| 1John.5.20 | æternaque | æternaque | ternaque |

## Punctuation not from the OCR (15)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.6 *facimus.*; 3.18 *amemus.*; 4.1 *Charissimi,*; 4.8 *amat,*; 4.8 *Deum:*; 4.8 *est.*; 4.9 *amor,*; 4.9 *mundum,*; 4.19 *amauit.*; 4.20 *dicit,*; 4.20 *odit,*; 4.20 *est.*; 4.20 *suum,*; 4.20 *vidit,*; 5.1 *amat.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
