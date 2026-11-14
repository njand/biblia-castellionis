# 1Thess 1–5 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 1Thess 1-5` → `text/orig/draft/1TH.usfm` (now `text/orig/1TH.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1Thess.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/1TH.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1255 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 13 | read in the OCR, a spelling the approved rules normalize |
| variant | 13 | read in the OCR, a printer's spelling no rule covers |
| nasal | 4 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 49 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 4 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 5 | OCR unreadable; the settled word in the printer's conventions |
| none | 5 | no OCR word; the settled word in the printer's conventions |
| all | 1348 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **s.1.1** *Silvānus* → *Syluanus*: 1573 canvas 904, read on the page: opening words set in capitals: PAVLVS ET SYLVA-nus; y, not i (read by Claude, 2026-11-13)
- **s.2.11** *ūnumquemque* → *vnumquenque*: 1573 canvas 905, read on the page: vnumquenq;, with n before q (read by Claude, 2026-11-13)
- **s.2.19** *quænam* → *quæ'nam*: 1573 canvas 905, read on the page (read by Claude, 2026-11-13)
- ⚑ **s.5.3** *iīs* → *eis*: 1573 canvas 906, read on the page (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (13)

*cāritāte* → *charitate*; *cāritātem* → *charitatem*; *cāritātisque* → *charitatisque* ×2; *epistula* → *epistola*; *exspectārētis* → *expectaretis*; *exstinguite* → *extinguite*; *iīs* → *eis* ×2; *quidquam* → *quicquam* ×2; *temptāsset* → *tentasset*; *temptātor* → *tentator*

## Printer's spellings no rule covers (13)

*audīstis* → *audiuistis*; *cælō* → *cœlo*; *cārissimī* → *charissimi*; *cārōsque* → *charosque*; *cēterī* → *cæteri* ×2; *dumtaxat* → *duntaxat*; *negōtiō* → *negocio*; *nūntiāsset* → *nunciasset*; *obdormierint* → *obdormiuerint* ×2; *tamquam* → *tanquam*; *umquam* → *vnquam*

## Not read in the OCR (10)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 1Thess.1.3 | recolentēs | recolentes | — |
| 1Thess.1.9 | vērōque | veroque | verog |
| 1Thess.2.3 | obscēnitātis | obscenitatis | — |
| 1Thess.4.9 | didicerītis | didiceritis | — |
| 1Thess.4.11 | quiēscere | quiescere | acquiefcere |
| 1Thess.4.11 | præcēpimus | præcepimus | præ cepimus |
| 1Thess.4.13 | obdormīvērunt | obdormiuerunt | — |
| 1Thess.5.2 | ventūram | venturam | feventuram |
| 1Thess.5.3 | īnstābit | instabit | stabit |
| 1Thess.5.13 | pācātōs | pacatos | — |

## Punctuation not from the OCR (6)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.10 *defendit.*; 4.1 *igitur,*; 4.1 *Iesum,*; 4.1 *vt,*; 4.18 *sermonibus.*; 5.13 *pacatos.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
