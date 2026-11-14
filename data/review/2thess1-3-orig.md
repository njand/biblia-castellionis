# 2Thess 1–3 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 2Thess 1-3` → `text/orig/draft/2TH.usfm` (now `text/orig/2TH.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Thess.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/2TH.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 684 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 9 | read in the OCR, a spelling the approved rules normalize |
| variant | 6 | read in the OCR, a printer's spelling no rule covers |
| nasal | 5 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 22 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 1 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 3 | OCR unreadable; the settled word in the printer's conventions |
| none | 9 | no OCR word; the settled word in the printer's conventions |
| all | 739 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **s.1.6** *afflīgentibus* → *affligentibus*: 1573 canvas 907, read on the page: af-|fligentibus, lower case mid-sentence (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (9)

*cāritās* → *charitas*; *cāritātem* → *charitatem*; *epistulā* → *epistola* ×2; *epistulīs* → *epistolis*; *iīs* → *eis*; *obœdientibus* → *obedientibus*; *quidquid* → *quicquid*; *quīcumque* → *quicunque*

## Printer's spellings no rule covers (6)

*cælō* → *cœlo*; *dēnūntiāmus* → *denunciamus*; *exsistat* → *existat*; *exsistet* → *existet* ×2; *tamquam* → *tanquam*

## Not read in the OCR (12)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 2Thess.1.1 | Silvānus | Siluanus | — |
| 2Thess.1.8 | irrogātūrus | irrogaturus | — |
| 2Thess.1.8 | nescientibus | nescientibus | — |
| 2Thess.2.1 | Rogāmus | Rogamus | — |
| 2Thess.2.2 | auctōrēs | auctores | — |
| 2Thess.2.8 | clāritāte | claritate | — |
| 2Thess.2.8 | dēlēbit | delebit | — |
| 2Thess.2.10 | scelerum | scelerum | — |
| 2Thess.2.16 | æternōque | æternoque | æter noque |
| 2Thess.3.4 | factūrōs | facturos | faAuros |
| 2Thess.3.7 | intemperanter | intemperanter | inteinperanter |
| 2Thess.3.8 | accēperīmus | acceperimus | — |

## Punctuation not from the OCR (4)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

2.8 *delebit:*; 2.17 *confirmet.*; 3.18 *gratia:*; 3.18 *Amen.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
