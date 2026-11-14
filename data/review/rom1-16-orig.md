# Rom 1–16 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Rom 1-16` → `text/orig/draft/ROM.usfm` (now `text/orig/ROM.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Rom.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/ROM.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 6008 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 36 | read in the OCR, a spelling the approved rules normalize |
| variant | 67 | read in the OCR, a printer's spelling no rule covers |
| ę | 6 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 64 | read in the OCR with a nasal bar (m or n put back) |
| misread | 8 | the settled word misread by the OCR; spelling as settled |
| lexicon | 287 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 6 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 25 | OCR unreadable; the settled word in the printer's conventions |
| none | 35 | no OCR word; the settled word in the printer's conventions |
| all | 6542 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **.16** *obœdiendō* → *obediendo*: 1573 canvas 860, read on the page: line break: obedi-endo; no œ (read by Claude, 2026-11-13)
- **.37** *exsuperāmus* → *exuperamus*: 1573 canvas 861, read on the page: no s; verse numbered 36 on the page (read by Claude, 2026-11-13)
- **0.19** *annōn* → *an non*: 1573 canvas 863, read on the page: printed as two words: Sed an non nouerunt (read by Claude, 2026-11-13)
- **.7** *quæ* → *quæ*: 1573 canvas 861, read on the page: ę (read by Claude, 2026-11-13)
- ⚑ **.11** *iīs* → *eis*: 1573 canvas 858, read on the page (read by Claude, 2026-11-13)
- **5.21** *audierant* → *audiuerant*: 1573 canvas 866, read on the page: line break audiue-rant (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (36)

*cotīdiē* → *quotidie*; *cāritās* → *charitas* ×3; *cāritātem* → *charitatem*; *cāritātis* → *charitatis*; *dextram* → *dexteram*; *epistulam* → *epistolam*; *exspectāmus* → *expectamus*; *exspectātiō* → *expectatio*; *intellegent* → *intelligent*; *iīs* → *eis* ×8; *iīsque* → *eisque*; *obœdiendum* → *obediendum*; *obœdientia* → *obedientia*; *obœdientibus* → *obedientibus*; *obœdientiæ* → *obedientiæ*; *obœdientiā* → *obedientia*; *obœdiātis* → *obediatis*; *obœdiātur* → *obediatur*; *obœdīrent* → *obedirent*; *quidquam* → *quicquam*; *quidquid* → *quicquid*; *quīcumque* → *quicunque* ×5; *sepulcrum* → *sepulchrum*

## Printer's spellings no rule covers (67)

*ab* → *abb*; *animus* → *aniimus*; *auctor* → *author*; *audiērunt* → *audiuerunt*; *cohērēdēs* → *cohæredes*; *committite* → *comittite*; *cuicumque* → *cuicunque*; *cælum* → *cœlum*; *cælō* → *cœlo*; *cārissimam* → *charissimam*; *cārissimum* → *charissimum* ×3; *cārissimī* → *charissimi*; *cārī* → *chari*; *cārīs* → *charis*; *cēteræ* → *cæteræ*; *cēterārum* → *cæterarum*; *cēterās* → *cæteras* ×2; *cēterīs* → *cæteris* ×2; *exsecrātiōne* → *execratione*; *exsecūtōrēs* → *executores*; *exsequitur* → *exequitur*; *exseritur* → *exeritur* ×2; *exsistetque* → *existetque*; *exstat* → *extat* ×3; *fēminæ* → *fœminæ*; *fētibus* → *fœtibus*; *fētificārēmus* → *fœtificaremus*; *gāius* → *caius*; *hērēdem* → *hæredem*; *hērēdēs* → *hæredes* ×3; *jācōbæōs* → *iacobeos*; *litteram* → *literam*; *litteræ* → *literæ* ×4; *litterā* → *litera*; *litterārum* → *literarum*; *litterās* → *literas*; *litterīs* → *literis* ×7; *līberet* → *liberæt*; *malitiæ* → *maliciæ*; *mīllia* → *milia*; *nūntiātum* → *nunciatum*; *obscœna* → *obscena*; *permīsit* → *permissit*; *quamdiū* → *quandiu*; *quæcumque* → *quæcunque*; *submīsērunt* → *summiserunt*; *sæculō* → *seculo*; *sī* → *sii*; *īnsitīciī* → *insititij*

## Not read in the OCR (68)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Rom.1.12 | recreēmur | recreemur | crecreemur |
| Rom.1.18 | supprimentium | supprimentium | — |
| Rom.1.30 | arrogantēs | arrogantes | atrogantes |
| Rom.2.1 | condemnās | condemnas | demnas |
| Rom.2.20 | imprūdentium | imprudentium | imprudentum |
| Rom.2.25 | committās | committas | cominittas |
| Rom.3.1 | Quænam | Quænam | — |
| Rom.3.8 | damnandī | damnandi | dainnaridi |
| Rom.3.9 | antecellimus | antecellimus | antecellim |
| Rom.3.15 | fundendum | fundendum | fundenduin |
| Rom.4.9 | habitam | habitam | habitain |
| Rom.5.5 | perfūsī | perfusi | — |
| Rom.5.19 | effectī | effecti | — |
| Rom.5.19 | efficientur | efficientur | — |
| Rom.6.4 | baptismum | baptismum | — |
| Rom.6.19 | impūritātī | impuritati | — |
| Rom.7.6 | tenēbāmur | tenebamur | tenebainur |
| Rom.7.14 | spīrituālem | spiritualem | spiritualen |
| Rom.8.3 | damnāvit | damnauit | damnauite |
| Rom.8.11 | inhabitantem | inhabitantem | inhabitantein |
| Rom.8.15 | clāmāmus | clamamus | clamainus |
| Rom.8.36 | necāmur | necamur | necamut |
| Rom.9.11 | fūnctīs | functis | — |
| Rom.9.22 | potentiamque | potentiamque | — |
| Rom.10.1 | spectat | spectat | — |
| Rom.10.5 | scrībit | scribit | — |
| Rom.10.7 | ēdūcere | educere | — |
| Rom.10.10 | cōnfessiō | confessio | — |
| Rom.10.14 | præcōne | præcone | — |
| Rom.10.18 | annōn | annon | — |
| Rom.10.19 | imperītam | imperitam | imperitain |
| Rom.10.21 | contumācem | contumacem | totumacem |
| Rom.11.2 | prænōvit | prænouit | prætiouit |
| Rom.11.8 | torpentem | torpentem | — |
| Rom.11.17 | oleaster | oleaster | — |
| Rom.11.20 | timē | time | tiine |
| Rom.11.22 | lāpsōs | lapsos | — |
| Rom.11.22 | sevēritātem | seueritatem | — |
| Rom.11.25 | contigisse | contigisse | contigifle |
| Rom.11.26 | līberātor | liberator | — |
| Rom.12.16 | efferentēs | efferentes | — |
| Rom.12.20 | congerēs | congeres | — |
| Rom.12.21 | maleficium | maleficium | — |
| Rom.13.2 | resistit | resistit | refiltit |
| Rom.13.2 | restiterint | restiterint | rettiterunt |
| Rom.13.4 | malefēceris | malefeceris | — |
| Rom.13.4 | formīdā | formida | — |
| Rom.13.9 | summātim | summatim | — |
| Rom.13.9 | comprehenditur | comprehenditur | — |
| Rom.13.10 | perfūnctiō | perfunctio | perfuntio |
| Rom.13.11 | crēdidimus | credidimus | cre |
| Rom.13.13 | cōmessātiōnibus | comessationibus | — |
| Rom.14.1 | imbēcillā | imbecilla | — |
| Rom.14.11 | flectet | flectet | sectet |
| Rom.14.11 | celebrābit | celebrabit | — |
| Rom.15.8 | cōnfirmanda | confirmanda | — |
| Rom.15.10 | Lætāminī | Lætamini | Lætaminigentes |
| Rom.15.12 | Isæa | Isæa | Ilza |
| Rom.15.14 | commonefacere | commonefacere | cominonefacere |
| Rom.15.19 | Illyricum | Illyricum | — |
| Rom.15.22 | venīrem | venirem | — |
| Rom.15.23 | tenear | tenear | — |
| Rom.16.1 | Cenchreēnsis | Cenchreensis | Cenehreensis |
| Rom.16.5 | Epænetum | Epænetum | Epæne tum |
| Rom.16.12 | Tryphænam | Tryphænam | Tryphenaım |
| Rom.16.14 | Hermem | Hermem | Herinem |
| Rom.16.21 | Lūcius | Lucius | — |
| Rom.16.21 | Jāsōn | Iason | lafon |

## Punctuation not from the OCR (34)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *Paulus,*; 2.3 *damnas,*; 3.2 *diuina.*; 3.4 *est:*; 3.27 *lege?*; 3.29 *est?*; 5.8 *est.*; 5.14 *est.*; 5.19 *multi.*; 7.22 *attinet:*; 8.10 *iustitiam.*; 8.16 *liberos.*; 9.2 *affici.*; 9.7 *progenies:*; 9.25 *amatam:*; 10.1 *supplicatio,*; 10.1 *Israelitarum.*; 10.7 *educere.*; 10.10 *salutem.*; 10.12 *omnibus,*; 10.14 *præcone?*; 10.17 *oratione.*; 10.19 *Israelitæ?*; 11.25 *numerus:*; 12.20 *congeres.*; 12.21 *maleficium.*; 13.4 *malefeceris,*; 13.11 *tum,*; 13.11 *credidimus.*; 14.1 *est,*; 14.11 *celebrabit.*; 15.22 *venirem.*; 15.23 *tenear,*; 16.23 *frater.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
