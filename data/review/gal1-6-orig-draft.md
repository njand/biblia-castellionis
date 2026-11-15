# Gal 1–6 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig Gal 1-6` → `text/orig/draft/GAL.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Gal.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/GAL.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1874 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 15 | read in the OCR, a spelling the approved rules normalize |
| variant | 22 | read in the OCR, a printer's spelling no rule covers |
| ę | 2 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 23 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 92 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 98 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 2126 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **3.8** *dēnūntiāvērunt* → *denunciauerunt*: 1573 canvas 890, read on the page: denũciauerunt; c not t (read by Claude, 2026-11-13)
- **3.10** *exsecrātiōnī* → *execrationi*: 1573 canvas 890, read on the page: line break: execra-tioni; no s (read by Claude, 2026-11-13)
- **6.1** *temptēminī* → *tentemini*: 1573 canvas 892, read on the page: tẽtemini (read by Claude, 2026-11-13)
- ⚑ **2.9** *Jōhannēs* → *Ioannes*: 1573 canvas 889, read on the page: no h (read by Claude, 2026-11-13)
- **5.20** *sectæ* → *sectæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)
- **1.6** *eō* → *eo*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.7** *quod* → *quòd*: 1573 canvas 889, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **1.8** *eō* → *eo*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.8** *quod* → *quod*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *eō* → *eo*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *quod* → *quod*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.13** *quam* → *quàm*: 1573 canvas 889, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.16** *cum* → *cum*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *post* → *post*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.23** *Tantum* → *Tantùm*: 1573 canvas 889, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **1.23** *quō* → *quo*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.23** *quam* → *quam*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.1** *post* → *post*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.1** *cum* → *cum*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.2** *quod* → *quod*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.4** *quam* → *quam*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.6** *Quod* → *Quòd*: 1573 canvas 889, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *quod* → *quod*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *Cum* → *Cum*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.12** *Cum* → *Cùm*: 1573 canvas 889, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **2.12** *cum* → *cum*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.13** *cum* → *cum*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.13** *eō* → *eo*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.16** *tantum* → *tantùm*: 1573 canvas 889, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **2.17** *quod* → *quod*: 1573 canvas 889, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.20** *cum* → *cum*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.20** *adeō* → *adeò*: 1573 canvas 890, read on the page: grave on o; read on page image 0890 (me adeò amauit) (accents, decision 67) (Claude, 2026-11-14)
- **3.1** *Ō* → *O*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.6** *quod* → *quod*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.7** *ā* → *à*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.8** *eō* → *eo*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.9** *cum* → *cum*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.11** *quod* → *quòd*: 1573 canvas 890, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **3.13** *ā* → *à*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.17** *post* → *post*: 1573 canvas 890, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.21** *plānē* → *planè*: 1573 canvas 890, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **4.3** *cum* → *cum*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.5** *quō* → *quo*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.7** *quod* → *quòd*: 1573 canvas 891, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **4.13** *cum* → *cum*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.14** *quam* → *quam*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.18** *sōlum* → *solum*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.25** *cum* → *cum*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.25** *cum* → *cum*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.27** *quam* → *quàm*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.1** *quam* → *quam*: 1573 canvas 891, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.4** *cum* → *cum*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.7** *quō* → *quo*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.8** *eō* → *eo*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.12** *Ō* → *O*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.13** *modo* → *modò*: 1573 canvas 892, read on the page: grave on o; divided mo-|dò across lines; grave on the final o (page 0892) (accents, decision 67) (Claude, 2026-11-14)
- **5.15** *Quod* → *Quòd*: 1573 canvas 892, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **5.17** *contrā* → *contrà*: 1573 canvas 892, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **5.17** *quam* → *quam*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.17** *quam* → *quàm*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.23** *contrā* → *Contra*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.24** *cum* → *cum*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.1** *cum* → *cum*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.4** *quod* → *quod*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.6** *cum* → *cum*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.6** *eō* → *eo*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.6** *quō* → *quo*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.7** *quod* → *quod*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.10** *cum* → *cùm*: 1573 canvas 892, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **6.13** *ideō* → *ideo*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.16** *cum* → *cum*: 1573 canvas 892, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.9** *vidēbantur* → *videbantur*: 1573 canvas 889, read on the page (guess word: hyphenated vi-debantur (first part beyond the crop edge)) (Claude, 2026-11-15)
- **2.18** *abolēvī* → *aboleui*: 1573 canvas 889, read on the page (guess word) (Claude, 2026-11-15)
- **3.17** *quadringentōs* → *quadringentos*: 1573 canvas 890, read on the page (guess word: hyphenated quadringen-tos) (Claude, 2026-11-15)
- **4.6** *clāmet* → *clamet*: 1573 canvas 891, read on the page (guess word: a comma printed after it: "qui clamet, Abba pater.") (Claude, 2026-11-15)
- **4.9** *egēnaque* → *egenaque*: 1573 canvas 891, read on the page (guess word: printed egenaq;) (Claude, 2026-11-15)
- **5.9** *fermentī* → *fermenti*: 1573 canvas 892, read on the page (guess word) (Claude, 2026-11-15)
- **5.15** *mordētis* → *mordetis*: 1573 canvas 892, read on the page (guess word) (Claude, 2026-11-15)
- **5.20** *æmulātiōnēs* → *æmulationes*: 1573 canvas 892, read on the page (guess word: hyphenated æ-mulationes) (Claude, 2026-11-15)
- **1.13** *Jūdaismō* → *Iudaismo*: 1573 canvas 889, read on the page (misread word) (Claude, 2026-11-15)
- **5.15** *cōnsūmāminī* → *consumamini*: 1573 canvas 892, read on the page (misread word) (Claude, 2026-11-15)
- **6.16** *normam* → *normam*: 1573 canvas 892, read on the page (misread word) (Claude, 2026-11-15)
- **1.7** *pervertere* → *peruertere*: 1573 canvas 889, read on the page (none word: hyphenated at the column edge (perue[r]-tere); end of first line cut off in the crop) (Claude, 2026-11-15)
- **1.14** *Jūdaismī* → *Iudaismi*: 1573 canvas 889, read on the page (none word) (Claude, 2026-11-15)
- **1.14** *prōfectū* → *profectu*: 1573 canvas 889, read on the page (none word: hyphenated pro-fectu) (Claude, 2026-11-15)
- **1.14** *īnstitūtiōnum* → *institutionum*: 1573 canvas 889, read on the page (none word: hyphenated institutio-num) (Claude, 2026-11-15)
- **2.6** *videntur* → *videntur*: 1573 canvas 889, read on the page (none word: nasal bar: printed "vidẽtur") (Claude, 2026-11-15)
- **3.8** *jūstificātūrum* → *iustificaturum*: 1573 canvas 890, read on the page (none word: hyphenated iu-stificaturum (page 890)) (Claude, 2026-11-15)
- **3.9** *beantur* → *beantur*: 1573 canvas 890, read on the page (none word) (Claude, 2026-11-15)
- **3.17** *rescindat* → *rescindat*: 1573 canvas 890, read on the page (none word) (Claude, 2026-11-15)
- **3.23** *custōdiēbāmur* → *custodiebamur*: 1573 canvas 890, read on the page (none word: hyphenated custo-diebamur) (Claude, 2026-11-15)
- **3.25** *pædagōgō* → *pædagogo*: 1573 canvas 890, read on the page (none word: hyphenated pæda-gogo) (Claude, 2026-11-15)
- **4.3** *mundānīs* → *mundanis*: 1573 canvas 891, read on the page (none word: hyphenated munda-nis (page 891)) (Claude, 2026-11-15)
- **4.3** *ēmancipātī* → *emancipati*: 1573 canvas 891, read on the page (none word) (Claude, 2026-11-15)
- **4.16** *dīcendō* → *dicendo*: 1573 canvas 891, read on the page (none word) (Claude, 2026-11-15)
- **4.27** *paris* → *paris*: 1573 canvas 891, read on the page (none word: hyphenated pa-ris) (Claude, 2026-11-15)
- **5.1** *servitūtis* → *seruitutis*: 1573 canvas 891, read on the page (none word: hyphenated serui-tutis (page 891)) (Claude, 2026-11-15)
- **5.3** *circumcīditur* → *circumciditur*: 1573 canvas 892, read on the page (none word: hyphenated across pages circum- (891) / ciditur (892)) (Claude, 2026-11-15)

## Spellings the approved rules normalize (15)

*cāritās* → *charitas*; *cāritātem* → *charitatem* ×2; *exsecrābilem* → *execrabilem* ×2; *exsecrātiō* → *execratio*; *exsecrātiōne* → *execratione*; *iīs* → *eis*; *quattuordecim* → *quatuordecim*; *quidquam* → *quicquam* ×2; *quīcumque* → *quicunque* ×3; *temptātiōnem* → *tentationem*

## Printer's spellings no rule covers (21)

*audierant* → *audiuerant*; *audīstis* → *audiuistis*; *circumcīsiōnis* → *circuncisionis*; *circumcīsōrum* → *circuncisorum*; *circumcīsōs* → *circuncisos*; *dēfetīscī* → *defethisci*; *exsequiminī* → *exequimini*; *fēmina* → *fœmina*; *hagar* → *agar* ×2; *hērēditās* → *hæreditas*; *hērēs* → *hæres* ×3; *litteræ* → *literæ* ×2; *litterīs* → *literis*; *quamdiū* → *quandiu*; *quamquam* → *quanquam*; *servīstis* → *seruiuistis*; *sæculō* → *seculo*

## e against the settled æ, printed æ (1)

*præpūtiī* → *præputij*

## Punctuation not from the OCR (14)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.7 *volunt.*; 2.6 *attinet,*; 2.6 *aliquid,*; 2.13 *Iudæi,*; 3.7 *esse.*; 3.9 *beantur.*; 3.10 *præstiterit.*; 3.17 *rescindat.*; 3.29 *hæredes.*; 4.3 *emancipati.*; 4.16 *dicendo?*; 4.31 *liberæ.*; 5.1 *teneri.*; 6.11 *manu.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
