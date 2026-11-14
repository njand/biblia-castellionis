# Col 1–4 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Col 1-4` → `text/orig/draft/COL.usfm` (now `text/orig/COL.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Col.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/COL.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1294 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 11 | read in the OCR, a spelling the approved rules normalize |
| variant | 13 | read in the OCR, a printer's spelling no rule covers |
| nasal | 10 | read in the OCR with a nasal bar (m or n put back) |
| misread | 2 | the settled word misread by the OCR; spelling as settled |
| lexicon | 59 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| guess | 1 | OCR unreadable; the settled word in the printer's conventions |
| none | 11 | no OCR word; the settled word in the printer's conventions |
| all | 1401 | |

## Spellings the approved rules normalize (11)

*cāritāte* → *charitate*; *cāritātem* → *charitatem*; *epistula* → *epistola*; *epistulam* → *epistolam*; *iīs* → *eis* ×2; *obœdīte* → *obedite* ×2; *quidquid* → *quicquid* ×2; *quīcumque* → *quicunque*

## Printer's spellings no rule covers (13)

*audīstis* → *audiuistis* ×3; *cælō* → *cœlo*; *cārissimus* → *charissimus*; *cārissimō* → *charissimo*; *cārus* → *charus*; *cārōque* → *charoque*; *hērēditātem* → *hæreditatem*; *nūntiāmus* → *nunciamus*; *sæculōrum* → *seculorum*; *tamquam* → *tanquam* ×2

## Not read in the OCR (14)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Col.1.12 | participandam | participandam | — |
| Col.1.13 | trānstulit | transtulit | — |
| Col.1.24 | lætor | lætor | — |
| Col.2.2 | connexōrum | connexorum | — |
| Col.2.3 | reconditæ | reconditæ | re |
| Col.2.5 | firmitātem | firmitatem | firinitatem |
| Col.2.8 | fallāciāque | fallaciaque | — |
| Col.2.23 | vexātiōnem | vexationem | vexationein |
| Col.3.12 | affectum | affectum | — |
| Col.3.14 | perfectiōnis | perfectionis | — |
| Col.3.14 | vinculum | vinculum | — |
| Col.4.2 | Supplicātiōnī | Supplicationi | — |
| Col.4.2 | vigilantēs | vigilantes | — |
| Col.4.5 | redimentēs | redimentes | — |

## Punctuation not from the OCR (6)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

2.17 *Christus.*; 3.8 *vestro.*; 3.14 *charitatem,*; 3.20 *est.*; 4.2 *vigilantes.*; 4.5 *redimentes.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
