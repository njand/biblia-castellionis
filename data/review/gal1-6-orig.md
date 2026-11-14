# Gal 1–6 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Gal 1-6` → `text/orig/draft/GAL.usfm` (now `text/orig/GAL.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Gal.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/GAL.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1931 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 11 | read in the OCR, a spelling the approved rules normalize |
| variant | 25 | read in the OCR, a printer's spelling no rule covers |
| ę | 2 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 24 | read in the OCR with a nasal bar (m or n put back) |
| misread | 3 | the settled word misread by the OCR; spelling as settled |
| lexicon | 100 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 5 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 9 | OCR unreadable; the settled word in the printer's conventions |
| none | 16 | no OCR word; the settled word in the printer's conventions |
| all | 2126 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **.8** *dēnūntiāvērunt* → *denunciauerunt*: 1573 canvas 890, read on the page: denũciauerunt; c not t (read by Claude, 2026-11-13)
- **.10** *exsecrātiōnī* → *execrationi*: 1573 canvas 890, read on the page: line break: execra-tioni; no s (read by Claude, 2026-11-13)
- **.1** *temptēminī* → *tentemini*: 1573 canvas 892, read on the page: tẽtemini (read by Claude, 2026-11-13)
- ⚑ **.9** *Jōhannēs* → *Ioannes*: 1573 canvas 889, read on the page: no h (read by Claude, 2026-11-13)
- **.20** *sectæ* → *sectæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (11)

*cāritās* → *charitas*; *cāritātem* → *charitatem* ×2; *iīs* → *eis*; *quattuordecim* → *quatuordecim*; *quidquam* → *quicquam* ×2; *quīcumque* → *quicunque* ×3; *temptātiōnem* → *tentationem*

## Printer's spellings no rule covers (24)

*audierant* → *audiuerant*; *audīstis* → *audiuistis*; *circumcīsiōnis* → *circuncisionis*; *circumcīsōrum* → *circuncisorum*; *circumcīsōs* → *circuncisos*; *exsecrābilem* → *execrabilem* ×2; *exsecrātiō* → *execratio*; *exsecrātiōne* → *execratione*; *exsequiminī* → *exequimini*; *fēmina* → *fœmina*; *hagar* → *agar* ×2; *hērēditās* → *hæreditas*; *hērēs* → *hæres* ×3; *litteræ* → *literæ* ×2; *litterīs* → *literis*; *quamdiū* → *quandiu*; *quamquam* → *quanquam*; *servīstis* → *seruiuistis*; *sæculō* → *seculo*

## e against the settled æ, printed æ (1)

*præpūtiī* → *præputij*

## Not read in the OCR (28)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Gal.1.7 | pervertere | peruertere | — |
| Gal.1.13 | Jūdaismō | Iudaismo | ludaisino |
| Gal.1.14 | Jūdaismī | Iudaismi | — |
| Gal.1.14 | prōfectū | profectu | — |
| Gal.1.14 | īnstitūtiōnum | institutionum | — |
| Gal.2.6 | videntur | videntur | — |
| Gal.2.9 | vidēbantur | videbantur | debantur |
| Gal.2.18 | abolēvī | aboleui | — |
| Gal.3.8 | jūstificātūrum | iustificaturum | — |
| Gal.3.9 | beantur | beantur | — |
| Gal.3.17 | quadringentōs | quadringentos | tos |
| Gal.3.17 | rescindat | rescindat | — |
| Gal.3.23 | custōdiēbāmur | custodiebamur | — |
| Gal.3.25 | pædagōgō | pædagogo | — |
| Gal.4.3 | mundānīs | mundanis | — |
| Gal.4.3 | ēmancipātī | emancipati | — |
| Gal.4.6 | clāmet | clamet | clanet |
| Gal.4.9 | egēnaque | egenaque | egenags |
| Gal.4.16 | dīcendō | dicendo | — |
| Gal.4.27 | paris | paris | — |
| Gal.5.1 | servitūtis | seruitutis | — |
| Gal.5.3 | circumcīditur | circumciditur | — |
| Gal.5.9 | fermentī | fermenti | ferimenti |
| Gal.5.15 | mordētis | mordetis | nordetis |
| Gal.5.15 | cōnsūmāminī | consumamini | consumainini |
| Gal.5.20 | æmulātiōnēs | æmulationes | mulationes |
| Gal.6.9 | dēfetīscī | defetisci | defethisci |
| Gal.6.16 | normam | normam | norinam |

## Punctuation not from the OCR (14)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.7 *volunt.*; 2.6 *attinet,*; 2.6 *aliquid,*; 2.13 *Iudæi,*; 3.7 *esse.*; 3.9 *beantur.*; 3.10 *præstiterit.*; 3.17 *rescindat.*; 3.29 *hæredes.*; 4.3 *emancipati.*; 4.16 *dicendo?*; 4.31 *liberæ.*; 5.1 *teneri.*; 6.11 *manu.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
