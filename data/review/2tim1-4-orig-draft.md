# 2Tim 1–4 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 2Tim 1-4` → `text/orig/draft/2TI.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Tim.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/2TI.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 995 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 7 | read in the OCR, a spelling the approved rules normalize |
| variant | 9 | read in the OCR, a printer's spelling no rule covers |
| nasal | 10 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 78 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 55 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 1154 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **4.21** *hiemem* → *hyemem*: 1573 canvas 914, read on the page: printed hyemem (read by Claude, 2026-11-13)
- **1.6** *Quam* → *Quam*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *quā* → *qua*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *quod* → *quod*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *ante* → *ante*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *quod* → *quod*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.12** *quam* → *quam*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.13** *cum* → *cum*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.6** *quam* → *quàm*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.9** *quō* → *quo*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.10** *cum* → *cum*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.14** *modo* → *modò*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.20** *sōlum* → *solum*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.22** *cum* → *cum*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.25** *cum* → *cum*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.25** *forte* → *forte*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.25** *vērum* → *verum*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.26** *ā* → *à*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.26** *quō* → *quo*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.4** *quam* → *quàm*: 1573 canvas 913, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **3.10** *vērō* → *verò*: 1573 canvas 913, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **3.12** *piē* → *piè*: 1573 canvas 913, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **3.14** *quō* → *quo*: 1573 canvas 913, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.17** *rēctē* → *rectè*: 1573 canvas 914, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **4.2** *cum* → *cum*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.3** *cum* → *cùm*: 1573 canvas 914, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *ā* → *à*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *vērō* → *vero*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.8** *Quod* → *quod*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.8** *quam* → *quam*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.8** *sōlum* → *solùm*: 1573 canvas 914, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **4.13** *quam* → *quam*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *quod* → *quod*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.21** *ante* → *ante*: 1573 canvas 914, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.1** *prōmissiōnem* → *promissionem*: 1573 canvas 912, read on the page (guess word: hyphenated promissio-nem) (Claude, 2026-11-15)
- **2.7** *industriam* → *industriam*: 1573 canvas 913, read on the page (guess word: hyphenated indu-striam (first half beyond the crop edge)) (Claude, 2026-11-15)
- **4.20** *Trophimum* → *Trophimum*: 1573 canvas 914, read on the page (guess word) (Claude, 2026-11-15)
- **1.6** *impositiōnem* → *impositionem*: 1573 canvas 912, read on the page (misread word) (Claude, 2026-11-15)
- **2.14** *commemorātō* → *commemorato*: 1573 canvas 913, read on the page (misread word) (Claude, 2026-11-15)
- **4.6** *jamjam* → *iamiam*: 1573 canvas 914, read on the page (misread word) (Claude, 2026-11-15)
- **1.10** *repræsentātum* → *repræsentatum*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **1.13** *positā* → *posita*: 1573 canvas 913, read on the page (none word: read on page 913, top of the second column ("Iesu posita."); the crop showed 3.12-15) (Claude, 2026-11-15)
- **3.6** *īnsinuant* → *insinuant*: 1573 canvas 913, read on the page (none word: nasal bar: printed "insinuãt") (Claude, 2026-11-15)
- **3.6** *captīvāsque* → *captiuasque*: 1573 canvas 913, read on the page (none word: hyphenated ca-ptiuasque; printed with the abbreviation "-q;" (ptiuasq;)) (Claude, 2026-11-15)
- **3.6** *reddunt* → *reddunt*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.6** *mulierculās* → *mulierculas*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.6** *coopertæ* → *coopertæ*: 1573 canvas 913, read on the page (none word: printed with hooked e (coopertę)) (Claude, 2026-11-15)
- **3.6** *āctæ* → *actæ*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.7** *discunt* → *discunt*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.7** *pervenīre* → *peruenire*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.8** *Jannes* → *Iannes*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.8** *Jambres* → *Iambres*: 1573 canvas 913, read on the page (none word) (Claude, 2026-11-15)
- **3.8** *restitērunt* → *restiterunt|,*: 1573 canvas 913, read on the page (none word: 1573 prints a comma after it ("Mosi restiterunt, / ita hi veritati"), not a full stop; read on crops 4-5 and page 913) (Claude, 2026-11-15)
- **3.15** *ērudīre* → *erudire*: 1573 canvas 914, read on the page (none word: hyphenated e-rudire (the e- at the end of the line above, cut off in the crop)) (Claude, 2026-11-15)
- **4.10** *Dalmatiam* → *Dalmatiam|:*: 1573 canvas 914, read on the page (none word: 1573 prints a colon after it) (Claude, 2026-11-15)

## Spellings the approved rules normalize (7)

*cāritāte* → *charitate*; *cāritātis* → *charitatis*; *erō* → *hero*; *intellege* → *intellige*; *iīs* → *eis* ×2; *pænulam* → *penulam*

## Printer's spellings no rule covers (8)

*assecūtus* → *assequutus*; *audīstī* → *audiuisti* ×2; *cæleste* → *cœleste*; *cārō* → *charo*; *litterās* → *literas*; *quæsierit* → *quæsiuerit*; *tamquam* → *tanquam*

## Punctuation not from the OCR (17)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.13 *posita.*; 2.11 *viuemus.*; 2.13 *manet,*; 2.13 *potest.*; 3.6 *sunt,*; 3.6 *insinuant,*; 3.6 *mulierculas,*; 3.6 *coopertæ,*; 3.6 *actæ,*; 3.7 *discunt,*; 3.7 *possunt.*; 3.10 *charitatem,*; 4.2 *doctrina.*; 4.18 *sæcula:*; 4.18 *Amen.*; 4.21 *Cura,*; 4.21 *omnes.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
