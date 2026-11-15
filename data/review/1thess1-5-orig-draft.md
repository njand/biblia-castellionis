# 1Thess 1–5 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 1Thess 1-5` → `text/orig/draft/1TH.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1Thess.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/1TH.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1223 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 13 | read in the OCR, a spelling the approved rules normalize |
| variant | 13 | read in the OCR, a printer's spelling no rule covers |
| nasal | 4 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 45 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 50 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 1348 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **1.1** *Silvānus* → *Syluanus*: 1573 canvas 904, read on the page: opening words set in capitals: PAVLVS ET SYLVA-nus; y, not i (read by Claude, 2026-11-13)
- **2.11** *ūnumquemque* → *vnumquenque*: 1573 canvas 905, read on the page: vnumquenq;, with n before q (read by Claude, 2026-11-13)
- **2.19** *quænam* → *quæ'nam*: 1573 canvas 905, read on the page (read by Claude, 2026-11-13)
- **5.3** *iīs* → *eis*: 1573 canvas 906, read on the page (read by Claude, 2026-11-13)
- **1.5** *cum* → *cum*: 1573 canvas 904, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *cum* → *cum*: 1573 canvas 904, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *cum* → *cum*: 1573 canvas 904, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.8** *vērum* → *verùm*: 1573 canvas 904, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **1.10** *ā* → *à*: 1573 canvas 905, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **2.2** *multō* → *multo*: 1573 canvas 905, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.2** *cum* → *cum*: 1573 canvas 905, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.9** *vestrum* → *vestrûm*: 1573 canvas 905, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *quam* → *quàm*: 1573 canvas 905, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *piē* → *piè*: 1573 canvas 905, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *quam* → *quàm*: 1573 canvas 905, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *jūstē* → *iustè*: 1573 canvas 905, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **2.13** *quod* → *quòd*: 1573 canvas 905, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **2.14** *quod* → *quod*: 1573 canvas 905, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.1** *cum* → *cùm*: 1573 canvas 905, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **3.6** *Vērum* → *Verùm*: 1573 canvas 905, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **3.9** *quam* → *quam*: 1573 canvas 905, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.13** *cum* → *cum*: 1573 canvas 905, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.1** *Quod* → *QVod*: 1573 canvas 905, read on the page: chapter opening, drop cap Q then capital V; no accent (accents, decision 67) (Claude, 2026-11-14)
- **4.1** *eō* → *eo*: 1573 canvas 905, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *vestrum* → *vestrûm*: 1573 canvas 906, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.5** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.9** *Quod* → *Quod*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.14** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.14** *eō* → *eo*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *prīmum* → *primùm*: 1573 canvas 906, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **4.17** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.17** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.2** *præclārē* → *præclarè*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.3** *Cum* → *Cùm*: 1573 canvas 906, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **5.10** *cum* → *cum*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.10** *eō* → *eo*: 1573 canvas 906, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.18** *ea* → *ea*: 1573 canvas 906, read on the page: nam ª ea est, the superscript note letter not the word's (Claude, 2026-11-14)
- **1.9** *vērōque* → *veroque|*: 1573 canvas 905, read on the page (guess word: printed veroq; (the ; is the -que sign); no punctuation after it ("veroq; Deo seruiretis,")) (Claude, 2026-11-15)
- **4.11** *quiēscere* → *quiescere*: 1573 canvas 906, read on the page (guess word: "ac quiescere,") (Claude, 2026-11-15)
- **4.11** *præcēpimus* → *præcepimus*: 1573 canvas 906, read on the page (guess word: hyphenated præ-cepimus) (Claude, 2026-11-15)
- **5.2** *ventūram* → *venturam*: 1573 canvas 906, read on the page (guess word) (Claude, 2026-11-15)
- **5.3** *īnstābit* → *instabit*: 1573 canvas 906, read on the page (guess word: hyphenated in-stabit (first half beyond the crop edge)) (Claude, 2026-11-15)
- **1.3** *recolentēs* → *recolentes*: 1573 canvas 904, read on the page (none word: hyphenated recole[n]-tes; the line end is cut off in the crop, so whether the n is written out or a nasal bar is not seen) (Claude, 2026-11-15)
- **2.3** *obscēnitātis* → *obscœnitatis*: 1573 canvas 905, read on the page (none word: printed with œ: "...scœnitatis," (hyphenated ob-scœnitatis; the ob- at the line end cut off in the crop)) (Claude, 2026-11-15)
- **4.9** *didicerītis* → *didiceritis|:*: 1573 canvas 906, read on the page (none word: 1573 prints a colon after it) (Claude, 2026-11-15)
- **4.13** *obdormīvērunt* → *obdormiuerunt*: 1573 canvas 906, read on the page (none word: hyphenated ob-dormiuerunt) (Claude, 2026-11-15)
- **5.13** *pācātōs* → *pacatos*: 1573 canvas 906, read on the page (none word: read on page 906) (Claude, 2026-11-15)

## Spellings the approved rules normalize (13)

*cāritāte* → *charitate*; *cāritātem* → *charitatem*; *cāritātisque* → *charitatisque* ×2; *epistula* → *epistola*; *exspectārētis* → *expectaretis*; *exstinguite* → *extinguite*; *iīs* → *eis* ×2; *quidquam* → *quicquam* ×2; *temptāsset* → *tentasset*; *temptātor* → *tentator*

## Printer's spellings no rule covers (13)

*audīstis* → *audiuistis*; *cælō* → *cœlo*; *cārissimī* → *charissimi*; *cārōsque* → *charosque*; *cēterī* → *cæteri* ×2; *dumtaxat* → *duntaxat*; *negōtiō* → *negocio*; *nūntiāsset* → *nunciasset*; *obdormierint* → *obdormiuerint* ×2; *tamquam* → *tanquam*; *umquam* → *vnquam*

## Punctuation not from the OCR (6)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.10 *defendit.*; 4.1 *igitur,*; 4.1 *Iesum,*; 4.1 *vt,*; 4.18 *sermonibus.*; 5.13 *pacatos.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
