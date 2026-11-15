# Eph 1–6 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig Eph 1-6` → `text/orig/draft/EPH.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Eph.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/EPH.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1772 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 19 | read in the OCR, a spelling the approved rules normalize |
| variant | 24 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 15 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 175 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 116 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 2122 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **4.12** *exstrūctiōnem* → *extructionem*: 1573 canvas 895, read on the page: no s (read by Claude, 2026-11-13)
- **4.16** *exstruendum* → *extruendum*: 1573 canvas 895, read on the page: extruẽdum; no s (read by Claude, 2026-11-13)
- **2.7** *sæculīs* → *seculis*: 1573 canvas 894, read on the page: plain e (read by Claude, 2026-11-13)
- **3.21** *sæculōrum* → *seculorum*: 1573 canvas 895, read on the page: plain e (read by Claude, 2026-11-13)
- **1.4** *eō* → *eo*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.4** *ante* → *ante*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *quā* → *qua*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.7** *quō* → *quo*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.8** *quā* → *qua*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.8** *cum* → *cum*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *quō* → *quo*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.13** *quō* → *quo*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.17** *quō* → *quo*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *eō* → *eo*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.18** *quam* → *quàm*: 1573 canvas 894, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.19** *quam* → *quàm*: 1573 canvas 894, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.20** *quam* → *quam*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.21** *suprā* → *supra*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.21** *quod* → *quod*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.21** *vērum* → *verum*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.22** *suprā* → *supra*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.5** *cum* → *cum*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.7** *quā* → *qua*: 1573 canvas 894, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.21** *quod* → *quod*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.22** *quō* → *quo*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.2** *quod* → *quod*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.5** *quod* → *quod*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.7** *quod* → *quod*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.9** *quod* → *quod*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.12** *quō* → *quo*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.15** *quō* → *quo*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.17** *quō* → *quo*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.18** *cum* → *cum*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.18** *quam* → *quàm*: 1573 canvas 895, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **3.19** *quam* → *quàm*: 1573 canvas 895, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **4.1** *quam* → *quam*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.2** *cum* → *cum*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.2** *cum* → *cum*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.2** *cum* → *cum*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.5** *ūna* → *vna*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.6** *suprā* → *supra*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.10** *suprā* → *supra*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.14** *quā* → *qua*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.15** *vērum* → *verum*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.15** *cum* → *cum*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *quō* → *quo*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.16** *modō* → *modo*: 1573 canvas 895, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.18** *quā* → *qua*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.21** *modo* → *modò*: 1573 canvas 896, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **4.21** *eō* → *eo*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.24** *cum* → *cum*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.25** *cum* → *cum*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.28** *quod* → *quod*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.29** *quā* → *qua*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.30** *quō* → *quo*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.2** *cum* → *cum*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.8** *Cum* → *Cùm*: 1573 canvas 896, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **5.18** *quō* → *quo*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.21** *cum* → *cum*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.26** *quō* → *quo*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.31** *ūna* → *vna*: 1573 canvas 896, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.33** *vestrum* → *vestrûm*: 1573 canvas 896, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **6.2** *quod* → *quod*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.2** *prīmum* → *primum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.2** *cum* → *cum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.5** *quod* → *quod*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.5** *cum* → *cum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.7** *cum* → *cum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.8** *quod* → *quod*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.9** *vestrum* → *vestrum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.10** *Cēterum* → *Cæterùm*: 1573 canvas 897, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **6.16** *quō* → *quò*: 1573 canvas 897, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **6.18** *cum* → *cum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.20** *quō* → *quo*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.20** *quam* → *quàm*: 1573 canvas 897, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **6.22** *ideō* → *ideo*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.22** *quō* → *quo*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.23** *cum* → *cum*: 1573 canvas 897, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.14** *ambōbus* → *ambobus*: 1573 canvas 894, read on the page (guess word: a note letter c stands before it) (Claude, 2026-11-15)
- **1.14** *asserendam* → *asserendam*: 1573 canvas 894, read on the page (prone word: hyphenated asseren-dam) (Claude, 2026-11-15)
- **5.14** *affulgēbit* → *affulgebit*: 1573 canvas 896, read on the page (prone word) (Claude, 2026-11-15)
- **6.11** *aggressiōnēs* → *aggressiones*: 1573 canvas 897, read on the page (prone word: hyphenated; only "siones" visible at line start, the first part is cut off on the crop) (Claude, 2026-11-15)
- **1.7** *dīvite* → *diuite*: 1573 canvas 894, read on the page (none word: hyphenated diui-te (page 894)) (Claude, 2026-11-15)
- **1.12** *collocāvimus* → *collocauimus*: 1573 canvas 894, read on the page (none word: read on page 894 (crop showed 2.6); Chri-sto collocauimus:) (Claude, 2026-11-15)
- **1.23** *complēmentum* → *complementum*: 1573 canvas 894, read on the page (none word: hyphenated complemen-tum) (Claude, 2026-11-15)
- **3.9** *commūniō* → *communio*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **3.9** *æternitāte* → *æternitate*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **3.9** *cēlātum* → *celatum*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **3.10** *dēclārētur* → *declaretur*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **3.10** *prīncipātibus* → *principatibus*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **3.10** *varia* → *varia*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **3.12** *cōnfīsiōne* → *confisione*: 1573 canvas 895, read on the page (none word: hyphenated confi-sione (page 895; crop showed the annotations)) (Claude, 2026-11-15)
- **4.10** *dēscenderat* → *descenderat|?*: 1573 canvas 895, read on the page (none word: 1573 prints a question mark after it ("terræ partes descenderat?"), not a comma) (Claude, 2026-11-15)
- **4.10** *complēret* → *compleret*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.11** *euangelistās* → *Euangelistas*: 1573 canvas 895, read on the page (none word: capital E as printed) (Claude, 2026-11-15)
- **4.12** *condendōs* → *condendos*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.13** *perveniāmus* → *perueniamus*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.13** *ūnitātem* → *vnitatem*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.13** *cognitiōnisque* → *cognitionisque*: 1573 canvas 895, read on the page (none word: hyphenated co-gnitionisque; printed with the abbreviation "-q;" (gnitionisq;)) (Claude, 2026-11-15)
- **4.13** *adultum* → *adultum*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.13** *plēnæ* → *plenæ*: 1573 canvas 895, read on the page (none word: divided across lines ple / næ (no hyphen visible at the line end)) (Claude, 2026-11-15)
- **4.13** *chrīstiānæ* → *Christianæ*: 1573 canvas 895, read on the page (none word: capital C as printed) (Claude, 2026-11-15)
- **4.14** *flūctuēmus* → *fluctuemus*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.14** *circumferāmur* → *circumferamur|,*: 1573 canvas 895, read on the page (none word: 1573 prints a comma after it) (Claude, 2026-11-15)
- **4.14** *versūtiā* → *versutia|,*: 1573 canvas 895, read on the page (none word: 1573 prints a comma after it) (Claude, 2026-11-15)
- **4.15** *adolēscāmus* → *adolescamus*: 1573 canvas 895, read on the page (none word) (Claude, 2026-11-15)
- **4.16** *efficitur* → *efficitur*: 1573 canvas 895, read on the page (none word: hyphenated effici-tur) (Claude, 2026-11-15)
- **4.25** *loquiminī* → *loquimini*: 1573 canvas 896, read on the page (none word) (Claude, 2026-11-15)
- **4.26** *īrātīs* → *iratis*: 1573 canvas 896, read on the page (none word: hyphenated ira-tis, the turnover "(tis vobis" set at the end of the line above) (Claude, 2026-11-15)
- **4.28** *egentibus* → *egentibus*: 1573 canvas 896, read on the page (none word: hyphenated egenti-bus) (Claude, 2026-11-15)
- **4.32** *condōnantēs* → *condonantes*: 1573 canvas 896, read on the page (none word: hyphenated condo-nantes; nasal bar: printed "nãtes") (Claude, 2026-11-15)
- **5.15** *sōlerter* → *solerter*: 1573 canvas 896, read on the page (none word) (Claude, 2026-11-15)
- **5.15** *gradiāminī* → *gradiamini*: 1573 canvas 896, read on the page (none word) (Claude, 2026-11-15)
- **5.15** *īnsipientēs* → *insipientes*: 1573 canvas 896, read on the page (none word: hyphenated insi-pientes (line end partly cut off in the crop)) (Claude, 2026-11-15)
- **5.17** *socordēs* → *socordes*: 1573 canvas 896, read on the page (none word) (Claude, 2026-11-15)
- **5.31** *adhærēbit* → *adhærebit*: 1573 canvas 896, read on the page (none word: hyphenated adhæ-rebit) (Claude, 2026-11-15)

## Spellings the approved rules normalize (19)

*condiciōne* → *conditione*; *condiciōnis* → *conditionis*; *cāritāte* → *charitate* ×7; *cāritātem* → *charitatem*; *exstrūctī* → *extructi*; *intellegentiam* → *intelligentiam*; *iīs* → *eis* ×2; *obœdientēs* → *obedientes*; *obœdīte* → *obedite* ×2; *quidquid* → *quicquid*; *sæculī* → *seculi*

## Printer's spellings no rule covers (24)

*auctōre* → *authore*; *audīstis* → *audiuistis* ×2; *clipeō* → *clypeo*; *cohērēdēs* → *cohæredes*; *cælestibus* → *cœlestibus*; *cārissimum* → *charissimum*; *cārissimus* → *charissimus*; *cārī* → *chari*; *cēterum* → *cæterùm*; *cēterī* → *cæteri*; *dūritiem* → *duriciem*; *exseruit* → *exeruit*; *exstinguere* → *extinguere*; *hērēditās* → *hæreditas*; *hērēditātem* → *hæreditatem*; *hērēditātis* → *hæreditatis*; *nūntiātum* → *nunciatum*; *obscēnitātem* → *obscœnitatem*; *sæculīs* → *seculis*; *sæculō* → *seculo*; *tamquam* → *tanquam*; *umquam* → *vnquam*; *āeriæ* → *aereæ*

## e against the settled æ, printed æ (1)

*præparāvit* → *præparauit*

## Punctuation not from the OCR (40)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.7 *beneficentia,*; 1.12 *collocauimus:*; 2.12 *mundo.*; 3.9 *faciam,*; 3.9 *communio,*; 3.9 *Deum(*; 3.9 *condidit)*; 3.9 *celatum,*; 3.10 *potestatibus,*; 3.10 *cœlestibus,*; 3.10 *ecclesiam,*; 3.12 *aditum,*; 4.10 *ascendit,*; 4.10 *compleret.*; 4.11 *apostolos,*; 4.11 *vates,*; 4.11 *Euangelistas,*; 4.11 *dedit,*; 4.12 *ministerium,*; 4.12 *extructionem,*; 4.13 *fidei,*; 4.13 *Dei,*; 4.13 *adultum,*; 4.13 *Christianæ:*; 4.14 *pueri,*; 4.26 *vobis,*; 5.14 *mortuis,*; 5.14 *affulgebit.*; 5.15 *igitur,*; 5.15 *gradiamini,*; 5.15 *insipientes,*; 5.15 *sapientes;*; 5.16 *tempus,*; 5.16 *sunt.*; 5.17 *socordes,*; 5.17 *intelligite,*; 5.17 *voluntas:*; 5.31 *suæ,*; 5.31 *caro.*; 5.32 *dico.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
