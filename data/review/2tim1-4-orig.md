# 2Tim 1–4 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 2Tim 1-4` → `text/orig/draft/2TI.usfm` (now `text/orig/2TI.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Tim.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/2TI.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1026 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 7 | read in the OCR, a spelling the approved rules normalize |
| variant | 9 | read in the OCR, a printer's spelling no rule covers |
| nasal | 10 | read in the OCR with a nasal bar (m or n put back) |
| misread | 3 | the settled word misread by the OCR; spelling as settled |
| lexicon | 80 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 1 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 3 | OCR unreadable; the settled word in the printer's conventions |
| none | 15 | no OCR word; the settled word in the printer's conventions |
| all | 1154 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **4.21** *hiemem* → *hyemem*: 1573 canvas 914, read on the page: printed hyemem (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (7)

*cāritāte* → *charitate*; *cāritātis* → *charitatis*; *erō* → *hero*; *intellege* → *intellige*; *iīs* → *eis* ×2; *pænulam* → *penulam*

## Printer's spellings no rule covers (8)

*assecūtus* → *assequutus*; *audīstī* → *audiuisti* ×2; *cæleste* → *cœleste*; *cārō* → *charo*; *litterās* → *literas*; *quæsierit* → *quæsiuerit*; *tamquam* → *tanquam*

## Not read in the OCR (21)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 2Tim.1.1 | prōmissiōnem | promissionem | promifsio |
| 2Tim.1.6 | impositiōnem | impositionem | impositionein |
| 2Tim.1.10 | repræsentātum | repræsentatum | — |
| 2Tim.1.13 | positā | posita | — |
| 2Tim.2.7 | industriam | industriam | induAriam |
| 2Tim.2.14 | commemorātō | commemorato | commeinorato |
| 2Tim.3.6 | īnsinuant | insinuant | — |
| 2Tim.3.6 | captīvāsque | captiuasque | — |
| 2Tim.3.6 | reddunt | reddunt | — |
| 2Tim.3.6 | mulierculās | mulierculas | — |
| 2Tim.3.6 | coopertæ | coopertæ | — |
| 2Tim.3.6 | āctæ | actæ | — |
| 2Tim.3.7 | discunt | discunt | — |
| 2Tim.3.7 | pervenīre | peruenire | — |
| 2Tim.3.8 | Jannes | Iannes | — |
| 2Tim.3.8 | Jambres | Iambres | — |
| 2Tim.3.8 | restitērunt | restiterunt | — |
| 2Tim.3.15 | ērudīre | erudire | — |
| 2Tim.4.6 | jamjam | iamiam | iainiam |
| 2Tim.4.10 | Dalmatiam | Dalmatiam | — |
| 2Tim.4.20 | Trophimum | Trophimum | Trophinum |

## Punctuation not from the OCR (18)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *promissionem,*; 1.13 *posita.*; 2.11 *viuemus.*; 2.13 *manet,*; 2.13 *potest.*; 3.6 *sunt,*; 3.6 *insinuant,*; 3.6 *mulierculas,*; 3.6 *coopertæ,*; 3.6 *actæ,*; 3.7 *discunt,*; 3.7 *possunt.*; 3.10 *charitatem,*; 4.2 *doctrina.*; 4.18 *sæcula:*; 4.18 *Amen.*; 4.21 *Cura,*; 4.21 *omnes.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
