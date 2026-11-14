# Eph 1–6 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Eph 1-6` → `text/orig/draft/EPH.usfm` (now `text/orig/EPH.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Eph.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/EPH.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1839 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 20 | read in the OCR, a spelling the approved rules normalize |
| variant | 24 | read in the OCR, a printer's spelling no rule covers |
| ę | 1 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 15 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 181 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 4 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 1 | OCR unreadable; the settled word in the printer's conventions |
| none | 37 | no OCR word; the settled word in the printer's conventions |
| all | 2122 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **.12** *exstrūctiōnem* → *extructionem*: 1573 canvas 895, read on the page: no s (read by Claude, 2026-11-13)
- **.16** *exstruendum* → *extruendum*: 1573 canvas 895, read on the page: extruẽdum; no s (read by Claude, 2026-11-13)
- **.7** *sæculīs* → *seculis*: 1573 canvas 894, read on the page: plain e (read by Claude, 2026-11-13)
- **.21** *sæculōrum* → *seculorum*: 1573 canvas 895, read on the page: plain e (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (20)

*condiciōne* → *conditione*; *condiciōnis* → *conditionis*; *cāritāte* → *charitate* ×7; *cāritātem* → *charitatem*; *exstrūctī* → *extructi*; *intellegentiam* → *intelligentiam*; *iīs* → *eis* ×2; *obœdientēs* → *obedientes*; *obœdīte* → *obedite* ×2; *quidquid* → *quicquid*; *sæculī* → *seculi*; *āeriæ* → *aereæ*

## Printer's spellings no rule covers (24)

*auctōre* → *authore*; *audīstis* → *audiuistis* ×2; *clipeō* → *clypeo*; *cohērēdēs* → *cohæredes*; *cælestibus* → *cœlestibus*; *cārissimum* → *charissimum*; *cārissimus* → *charissimus*; *cārī* → *chari*; *cēterum* → *cæterum* ×2; *cēterī* → *cæteri*; *dūritiem* → *duriciem*; *exseruit* → *exeruit*; *exstinguere* → *extinguere*; *hērēditās* → *hæreditas*; *hērēditātem* → *hæreditatem*; *hērēditātis* → *hæreditatis*; *nūntiātum* → *nunciatum*; *obscēnitātem* → *obscœnitatem*; *sæculīs* → *seculis*; *sæculō* → *seculo*; *tamquam* → *tanquam*; *umquam* → *vnquam*

## e against the settled æ, printed æ (1)

*præparāvit* → *præparauit*

## Not read in the OCR (38)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Eph.1.7 | dīvite | diuite | — |
| Eph.1.12 | collocāvimus | collocauimus | — |
| Eph.1.14 | asserendam | asserendam | — |
| Eph.1.23 | complēmentum | complementum | — |
| Eph.2.14 | ambōbus | ambobus | cambobus |
| Eph.3.9 | commūniō | communio | — |
| Eph.3.9 | æternitāte | æternitate | — |
| Eph.3.9 | cēlātum | celatum | — |
| Eph.3.10 | dēclārētur | declaretur | — |
| Eph.3.10 | prīncipātibus | principatibus | — |
| Eph.3.10 | varia | varia | — |
| Eph.3.12 | cōnfīsiōne | confisione | — |
| Eph.4.10 | dēscenderat | descenderat | — |
| Eph.4.10 | complēret | compleret | — |
| Eph.4.11 | euangelistās | euangelistas | — |
| Eph.4.12 | condendōs | condendos | — |
| Eph.4.13 | perveniāmus | perueniamus | — |
| Eph.4.13 | ūnitātem | vnitatem | — |
| Eph.4.13 | cognitiōnisque | cognitionisque | — |
| Eph.4.13 | adultum | adultum | — |
| Eph.4.13 | plēnæ | plenæ | — |
| Eph.4.13 | chrīstiānæ | christianæ | — |
| Eph.4.14 | flūctuēmus | fluctuemus | — |
| Eph.4.14 | circumferāmur | circumferamur | — |
| Eph.4.14 | versūtiā | versutia | — |
| Eph.4.15 | adolēscāmus | adolescamus | — |
| Eph.4.16 | efficitur | efficitur | — |
| Eph.4.25 | loquiminī | loquimini | — |
| Eph.4.26 | īrātīs | iratis | — |
| Eph.4.28 | egentibus | egentibus | — |
| Eph.4.32 | condōnantēs | condonantes | — |
| Eph.5.14 | affulgēbit | affulgebit | — |
| Eph.5.15 | sōlerter | solerter | — |
| Eph.5.15 | gradiāminī | gradiamini | — |
| Eph.5.15 | īnsipientēs | insipientes | — |
| Eph.5.17 | socordēs | socordes | — |
| Eph.5.31 | adhærēbit | adhærebit | — |
| Eph.6.11 | aggressiōnēs | aggressiones | — |

## Punctuation not from the OCR (40)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.7 *beneficentia,*; 1.12 *collocauimus:*; 2.12 *mundo.*; 3.9 *faciam,*; 3.9 *communio,*; 3.9 *Deum(*; 3.9 *condidit)*; 3.9 *celatum,*; 3.10 *potestatibus,*; 3.10 *cœlestibus,*; 3.10 *ecclesiam,*; 3.12 *aditum,*; 4.10 *ascendit,*; 4.10 *compleret.*; 4.11 *apostolos,*; 4.11 *vates,*; 4.11 *euangelistas,*; 4.11 *dedit,*; 4.12 *ministerium,*; 4.12 *extructionem,*; 4.13 *fidei,*; 4.13 *Dei,*; 4.13 *adultum,*; 4.13 *christianæ:*; 4.14 *pueri,*; 4.26 *vobis,*; 5.14 *mortuis,*; 5.14 *affulgebit.*; 5.15 *igitur,*; 5.15 *gradiamini,*; 5.15 *insipientes,*; 5.15 *sapientes;*; 5.16 *tempus,*; 5.16 *sunt.*; 5.17 *socordes,*; 5.17 *intelligite,*; 5.17 *voluntas:*; 5.31 *suæ,*; 5.31 *caro.*; 5.32 *dico.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
