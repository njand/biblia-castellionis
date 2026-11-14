# 2Pet 1–3 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 2Pet 1-3` → `text/orig/draft/2PE.usfm` (now `text/orig/2PE.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Pet.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/2PE.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 914 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 16 | read in the OCR, a spelling the approved rules normalize |
| variant | 18 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 8 | read in the OCR with a nasal bar (m or n put back) |
| misread | 3 | the settled word misread by the OCR; spelling as settled |
| lexicon | 35 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 1 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 3 | OCR unreadable; the settled word in the printer's conventions |
| none | 15 | no OCR word; the settled word in the printer's conventions |
| all | 1014 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **2.12** *iīs* → *eis*: 1573 canvas 923, read on the page (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (16)

*condiciō* → *conditio*; *cotīdiānīs* → *quotidianis*; *cum* → *quum*; *cāritātem* → *charitatem*; *epistulīs* → *epistolis*; *erum* → *herum*; *exspectandīs* → *expectandis*; *exspectāmus* → *expectamus*; *gomorræque* → *gomorrhæque*; *intellegātis* → *intelligatis*; *iīs* → *eis* ×3; *iīsque* → *eisque*; *neglegam* → *negligam*; *quemquam* → *quenquam*

## Printer's spellings no rule covers (18)

*cælī* → *cœli* ×2; *cælō* → *cœlo*; *cārissimus* → *charissimus* ×2; *cārissimī* → *charissimi* ×4; *cētera* → *cætera*; *litterās* → *literas*; *numquam* → *nunquam*; *quamdiū* → *quandiu*; *quamquam* → *quanquam*; *umquam* → *vnquam*; *vērumtamen* → *veruntamen*; *ōtiātur* → *ociatur*; *ōtiōsōs* → *ociosos*

## Not read in the OCR (21)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 2Pet.1.4 | corruptēlam | corruptelam | — |
| 2Pet.1.4 | effugiātis | effugiatis | — |
| 2Pet.1.5 | acquīrentēs | acquirentes | — |
| 2Pet.1.12 | commonefacere | commonefacere | — |
| 2Pet.1.12 | fīxōs | fixos | — |
| 2Pet.1.16 | dēclārāvimus | declarauimus | — |
| 2Pet.1.17 | magnificā | magnifica | — |
| 2Pet.2.1 | sectās | sectas | setas |
| 2Pet.2.8 | cruciābat | cruciabat | — |
| 2Pet.2.10 | dignitātibus | dignitatibus | dignitatib |
| 2Pet.2.10 | horrent | horrent | — |
| 2Pet.2.11 | ferant | ferant | — |
| 2Pet.2.14 | īnfirmās | infirmas | infirinas |
| 2Pet.2.15 | Balaamī | Balaami | Balaani |
| 2Pet.2.15 | convictus | conuictus | — |
| 2Pet.2.21 | recessisse | recessisse | — |
| 2Pet.2.22 | vomitum | vomitum | vomituin |
| 2Pet.2.22 | cænī | cæni | — |
| 2Pet.2.22 | volūtābrum | volutabrum | — |
| 2Pet.3.12 | elementa | elementa | — |
| 2Pet.3.16 | indoctī | indocti | indoeti |

## Punctuation not from the OCR (8)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.2 *cognitione:*; 1.9 *peccatorum.*; 1.12 *fixos.*; 1.21 *diuini.*; 2.15 *Balaami,*; 2.15 *est.*; 2.21 *recessisse:*; 2.22 *volutabrum.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
