# 1Pet 1–5 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 1Pet 1-5` → `text/orig/draft/1PE.usfm` (now `text/orig/1PE.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1Pet.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/1PE.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1528 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 13 | read in the OCR, a spelling the approved rules normalize |
| variant | 24 | read in the OCR, a printer's spelling no rule covers |
| ę | 2 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 16 | read in the OCR with a nasal bar (m or n put back) |
| misread | 5 | the settled word misread by the OCR; spelling as settled |
| lexicon | 58 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| guess | 7 | OCR unreadable; the settled word in the printer's conventions |
| none | 11 | no OCR word; the settled word in the printer's conventions |
| all | 1664 | |

## Spellings the approved rules normalize (13)

*cāritās* → *charitas*; *cāritātem* → *charitatem*; *cāritātis* → *charitatis*; *dextram* → *dexteram*; *exspectāret* → *expectaret*; *inobœdientēs* → *inobedientes*; *obœdiant* → *obediant*; *obœdiendō* → *obediendo*; *obœdientēs* → *obedientes* ×2; *obœdīvit* → *obediuit*; *quīcumque* → *quicunque*; *temptātiōnibus* → *tentationibus*

## Printer's spellings no rule covers (24)

*cohērēdēs* → *cohæredes*; *cælum* → *cœlum*; *cælō* → *cœlo*; *cārissimī* → *charissimi* ×2; *cōmessātiōnibus* → *commessationibus*; *exsistet* → *existet* ×2; *exstitit* → *extitit*; *exstruerētur* → *extrueretur*; *exsultātis* → *exultatis*; *exsultētis* → *exultetis*; *fēminæ* → *fœminæ*; *litterīs* → *literis*; *nūntiāta* → *nunciata*; *nūntiātus* → *nunciatus*; *pretiī* → *precij*; *pretiōsior* → *preciosior*; *pretiōsō* → *precioso*; *quamquam* → *quanquam*; *silvānum* → *syluanum*; *submittite* → *summittite*; *sæcula* → *secula*; *tamquam* → *tanquam*

## Not read in the OCR (23)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 1Pet.1.1 | sparsim | sparsim | sparsiın |
| 1Pet.1.4 | repositam | repositam | repositain |
| 1Pet.1.9 | reportātūrī | reportaturi | — |
| 1Pet.1.11 | scrūtantēs | scrutantes | — |
| 1Pet.1.14 | ignōrantiæ | ignorantiæ | ignoran tiæ |
| 1Pet.2.1 | simulātiōnibus | simulationibus | finulationibus |
| 1Pet.2.16 | prætextum | prætextum | prætextuin |
| 1Pet.2.17 | frāternitātem | fraternitatem | fraternitatein |
| 1Pet.2.17 | verēminī | veremini | — |
| 1Pet.2.20 | cædī | cædi | — |
| 1Pet.3.2 | conjūnctam | coniunctam | coniunctain |
| 1Pet.3.3 | palliōrum | palliorum | pallioruin |
| 1Pet.3.8 | ūnanimēs | vnanimes | vnaniines |
| 1Pet.3.9 | contrāriō | contrario | — |
| 1Pet.3.12 | maleficōs | maleficos | ma |
| 1Pet.3.20 | cōnservātæ | conseruatæ | — |
| 1Pet.4.2 | vīvat | viuat | vidat |
| 1Pet.4.3 | pōtātiōnibus | potationibus | — |
| 1Pet.4.10 | beneficiōrum | beneficiorum | — |
| 1Pet.4.11 | subministrat | subministrat | — |
| 1Pet.4.17 | initium | initium | — |
| 1Pet.5.1 | repræsentandæ | repræsentandæ | repræ sentandæ |
| 1Pet.5.4 | flaccēscentem | flaccescentem | — |

## Punctuation not from the OCR (7)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.2 *dicit.*; 1.11 *scrutantes,*; 1.25 *nunciatum.*; 3.12 *maleficos.*; 4.8 *habete:*; 4.11 *sæcula:*; 5.7 *sitis.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
