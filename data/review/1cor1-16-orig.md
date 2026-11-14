# 1Cor 1–16 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 1Cor 1-16` → `text/orig/draft/1CO.usfm` (now `text/orig/1CO.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1Cor.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/1CO.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 5577 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 49 | read in the OCR, a spelling the approved rules normalize |
| variant | 61 | read in the OCR, a printer's spelling no rule covers |
| ę | 8 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 59 | read in the OCR with a nasal bar (m or n put back) |
| misread | 7 | the settled word misread by the OCR; spelling as settled |
| lexicon | 496 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 11 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 18 | OCR unreadable; the settled word in the printer's conventions |
| none | 74 | no OCR word; the settled word in the printer's conventions |
| all | 6360 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **7.39** *obdormierit* → *obdormiuerit*: 1573 canvas 871, read on the page: differs from proposed (read by Claude, 2026-11-13)
- **10.13** *temptātiōne* → *tentatione*: 1573 canvas 873, read on the page: tẽtatione (read by Claude, 2026-11-13)
- **14.7** *intellegētur* → *intelligetur*: 1573 canvas 876, read on the page: line break: intellige tur; i not e (read by Claude, 2026-11-13)
- **14.24** *illitterātus* → *illiteratus*: 1573 canvas 876, read on the page: single t (read by Claude, 2026-11-13)
- **16.6** *hiemābō* → *hyemabo*: 1573 canvas 879, read on the page: y, not i (read by Claude, 2026-11-13)
- **15.40** *cælestia* → *cœlestia*: 1573 canvas 878, read on the page: œ (read by Claude, 2026-11-13)
- **1.16** *Cēterum* → *Cæterum*: 1573 canvas 867, read on the page: ę (read by Claude, 2026-11-13)
- **6.1** *negōtium* → *negotium*: 1573 canvas 870, read on the page (read by Claude, 2026-11-13)
- **7.14** *Sānctus* → *Sanctus*: 1573 canvas 871, read on the page (read by Claude, 2026-11-13)
- **7.17** *Cēterum* → *Cæterum*: 1573 canvas 871, read on the page: æ (read by Claude, 2026-11-13)
- **7.39** *quamdiū* → *quandiu*: 1573 canvas 871, read on the page (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (49)

*condiciōne* → *conditione*; *cotīdiē* → *quotidie*; *cāritās* → *charitas* ×5; *cāritāte* → *charitate* ×5; *cōntiōne* → *concione* ×2; *cōntiōnem* → *concionem*; *cōntiōnibus* → *concionibus* ×2; *cōntiōnī* → *concioni* ×2; *epistulam* → *epistolam*; *epistulās* → *epistolas*; *exspectantēs* → *expectantes*; *exspectāte* → *expectate*; *exspectō* → *expecto*; *immō* → *imo* ×2; *intellegam* → *intelligam*; *intellegit* → *intelligit*; *intellegāmus* → *intelligamus*; *intellegātur* → *intelligatur*; *intellegētur* → *intelligetur*; *iīs* → *eis* ×4; *quidquam* → *quicquam*; *quidquid* → *quicquid* ×2; *quotiēns* → *quoties* ×2; *sæculī* → *seculi* ×4; *temptet* → *tentet*; *temptārunt* → *tentarunt*; *temptārī* → *tentari*; *temptātiō* → *tentatio*; *temptēmus* → *tentemus*

## Printer's spellings no rule covers (61)

*aliquamdiū* → *aliquandiu*; *commodō* → *comodo*; *commūnitās* → *comunitas*; *cælestis* → *cœlestis*; *cælestēs* → *cœlestes*; *cælō* → *cœlo*; *cārissimī* → *charissimi* ×2; *cārissimōs* → *charissimos*; *cārus* → *charus*; *cēterum* → *cæterum* ×2; *cēterīs* → *cæteris*; *est* → *estt*; *exsecrētur* → *execretur*; *exstat* → *extat*; *fēmina* → *fœmina* ×2; *fēminam* → *fœminam*; *fēminæ* → *fœminæ* ×2; *fēminā* → *fœmina*; *fēminīs* → *fœminis*; *gāium* → *caium*; *illitterātī* → *illiterati* ×2; *immortālitātem* → *inmortalitatem*; *litterātus* → *literatus*; *litterīs* → *literis* ×3; *numquam* → *nunquam* ×3; *numquid* → *nunquid* ×6; *nōnne* → *none*; *obdormiēre* → *obdormiuere*; *obdormiērunt* → *obdormiuerunt* ×3; *oppetīvit* → *oppetijt*; *pretium* → *precium*; *pretiō* → *precio* ×2; *quamquam* → *quanquam*; *quodcumque* → *quodcunque*; *quōcumque* → *quocunque* ×2; *rēs* → *hres*; *scīscitantēs* → *stiscitantes*; *sæcula* → *secula*; *sæculō* → *seculo*; *sæculōrum* → *seculorum*; *tamquam* → *tanquam*; *umquam* → *vnquam*; *vēsciminī* → *vestimini*

## e against the settled æ, printed æ (1)

*cælebs* → *cœlebs*

## Not read in the OCR (99)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 1Cor.1.6 | cōnfirmātum | confirmatum | — |
| 1Cor.1.13 | Dīvīsusne | Diuisusne | — |
| 1Cor.1.20 | conquīsītor | conquisitor | — |
| 1Cor.1.21 | prædicātiōnis | prædicationis | — |
| 1Cor.1.23 | stultitiam | stultitiam | stultitian |
| 1Cor.1.25 | fortius | fortius | — |
| 1Cor.2.8 | fīxissent | fixissent | Efa |
| 1Cor.2.10 | abditissima | abditissima | — |
| 1Cor.2.13 | spīrituālibus | spiritualibus | — |
| 1Cor.2.14 | exāminanda | examinanda | — |
| 1Cor.2.16 | īnstīget | instiget | — |
| 1Cor.3.12 | gemmās | gemmas | — |
| 1Cor.3.12 | ligna | ligna | — |
| 1Cor.3.12 | fœnum | fœnum | — |
| 1Cor.3.12 | stipulam | stipulam | — |
| 1Cor.4.3 | minimī | minimi | ninimi |
| 1Cor.5.3 | dēcrēvī | decreui | — |
| 1Cor.6.1 | Audet | Audet | — |
| 1Cor.6.2 | factūrōs | facturos | — |
| 1Cor.6.5 | dijūdicāre | diiudicare | di |
| 1Cor.6.10 | impudīcī | impudici | — |
| 1Cor.6.12 | mancipābor | mancipabor | inancipabor |
| 1Cor.6.15 | tollam | tollam | tollain |
| 1Cor.7.9 | ārdēre | ardere | — |
| 1Cor.7.12 | īnfīdentem | infidentem | — |
| 1Cor.7.13 | īnfīdentem | infidentem | — |
| 1Cor.7.14 | īnfīdēns | infidens | — |
| 1Cor.7.14 | īnfīdēns | infidens | — |
| 1Cor.7.15 | īnfīdēns | infidens | — |
| 1Cor.7.15 | dīvortium | diuortium | — |
| 1Cor.7.16 | servātūra | seruatura | — |
| 1Cor.7.16 | servātūrus | seruaturus | — |
| 1Cor.7.17 | largītus | largitus | — |
| 1Cor.7.17 | gerat | gerat | — |
| 1Cor.7.18 | Circumcīsus | Circumcisus | — |
| 1Cor.7.18 | præpūtiētur | præputietur | — |
| 1Cor.7.18 | circumcīdātur | circumcidatur | — |
| 1Cor.7.19 | cōnservātiō | conseruatio | — |
| 1Cor.7.21 | cūrātō | curato | — |
| 1Cor.7.29 | restat | restat | — |
| 1Cor.7.36 | nūbat | nubat | — |
| 1Cor.7.37 | cōnstāns | constans | — |
| 1Cor.7.37 | cōgitur | cogitur | — |
| 1Cor.7.37 | jūris | iuris | — |
| 1Cor.7.37 | servandam | seruandam | — |
| 1Cor.7.37 | virginem | virginem | — |
| 1Cor.7.38 | nuptum | nuptum | — |
| 1Cor.7.38 | ēlocat | elocat | — |
| 1Cor.7.38 | ēlocat | elocat | — |
| 1Cor.7.38 | rēctius | rectius | — |
| 1Cor.7.39 | obstricta | obstricta | — |
| 1Cor.7.39 | nūbere | nubere | — |
| 1Cor.7.39 | dummodo | dummodo | — |
| 1Cor.7.40 | fēlīcior | felicior | — |
| 1Cor.7.40 | Videor | Videor | — |
| 1Cor.8.8 | vēscimur | vescimur | fivefcimur |
| 1Cor.9.9 | Bovēsne | Bouesne | — |
| 1Cor.9.10 | arantem | arantem | aranten |
| 1Cor.9.10 | trītūrantem | triturantem | — |
| 1Cor.9.15 | aboleat | aboleat | ftipendium |
| 1Cor.9.16 | cōgar | cogar | cogart |
| 1Cor.9.18 | abūtendō | abutendo | — |
| 1Cor.9.26 | verberem | verberem | verberein |
| 1Cor.9.27 | subigōque | subigoque | subigogs |
| 1Cor.9.27 | rejectāneus | reiectaneus | — |
| 1Cor.10.4 | petra | petra | — |
| 1Cor.10.7 | lūdendum | ludendum | — |
| 1Cor.10.16 | frangimus | frangimus | — |
| 1Cor.11.6 | vēlātur | velatur | — |
| 1Cor.11.17 | admonēns | admonens | — |
| 1Cor.11.17 | ūtiliter | vtiliter | — |
| 1Cor.11.22 | Numnam | Numnam | Númnain |
| 1Cor.11.22 | egēnōs | egenos | — |
| 1Cor.11.23 | prōdēbātur | prodebatur | — |
| 1Cor.11.26 | vēscēminī | vescemini | vesceinini |
| 1Cor.12.6 | effectiōnum | effectionum | effectioni |
| 1Cor.13.1 | cymbalum | cymbalum | cyınbalum |
| 1Cor.13.2 | trānsmoveam | transmoueam | tranfmouean |
| 1Cor.13.7 | tolerat | tolerat | — |
| 1Cor.13.7 | spērat | sperat | — |
| 1Cor.13.7 | sustinet | sustinet | — |
| 1Cor.13.8 | cessābunt | cessabunt | — |
| 1Cor.13.11 | sentiēbam | sentiebam | — |
| 1Cor.13.12 | ambāgēs | ambages | amba |
| 1Cor.13.13 | hārum | harum | — |
| 1Cor.13.13 | maxima | maxima | inaxima |
| 1Cor.14.1 | Persequiminī | Persequimini | — |
| 1Cor.14.6 | allocūtum | allocutum | — |
| 1Cor.14.18 | teneō | teneo | tenco |
| 1Cor.14.24 | īnfīdēns | infidens | in |
| 1Cor.14.25 | adōretque | adoretque | adorérque |
| 1Cor.14.36 | vōbīsne | vobisne | — |
| 1Cor.15.9 | īnsectātus | insectatus | — |
| 1Cor.15.32 | Comedāmus | Comedamus | — |
| 1Cor.15.37 | gignendum | gignendum | gignenduin |
| 1Cor.15.54 | victōriōsē | victoriose | — |
| 1Cor.16.2 | collēctæ | collectæ | collectz |
| 1Cor.16.4 | operæ | operæ | — |
| 1Cor.16.9 | adversāriī | aduersarii | funtaduerfarij |

## Punctuation not from the OCR (116)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.6 *est)*; 1.12 *dico,*; 1.12 *est,*; 1.12 *dicit:*; 1.12 *Pauli;*; 1.12 *alius:*; 1.12 *Apollo;*; 1.12 *Cephæ;*; 1.12 *Christi.*; 1.13 *est?*; 1.13 *est?*; 1.23 *fixum,*; 2.8 *fixissent.*; 3.5 *Dominus.*; 3.12 *argentum,*; 3.12 *gemmas,*; 3.12 *ligna,*; 3.12 *fœnum,*; 5.12 *attinet?*; 5.13 *vestrum.*; 6.1 *vestrum,*; 6.5 *diiudicare?*; 6.8 *fratres.*; 6.10 *impudici,*; 6.19 *vestros,*; 7.9 *ardere.*; 7.12 *dico,*; 7.12 *Dominus:*; 7.12 *infidentem,*; 7.12 *habitet,*; 7.12 *repudiato.*; 7.13 *mulier,*; 7.13 *infidentem,*; 7.13 *habitet,*; 7.13 *repudiato.*; 7.14 *vxorem:*; 7.14 *virum.*; 7.14 *essent,*; 7.14 *sancti.*; 7.15 *facit,*; 7.15 *faciat;*; 7.15 *seruus,*; 7.15 *soror:*; 7.15 *Deus.*; 7.16 *autem,*; 7.16 *mulier,*; 7.16 *sis?*; 7.16 *scis,*; 7.16 *vir,*; 7.16 *sis?*; 7.17 *est,*; 7.17 *vocauit,*; 7.17 *gerat:*; 7.17 *præcipio.*; 7.18 *aliquis,*; 7.18 *præputietur:*; 7.18 *est,*; 7.18 *circumcidatur.*; 7.19 *est,*; 7.19 *est,*; 7.19 *conseruatio.*; 7.20 *est,*; 7.20 *maneto.*; 7.21 *es,*; 7.21 *curato:*; 7.26 *igitur,*; 7.36 *sit,*; 7.36 *est,*; 7.36 *volet,*; 7.36 *faciat,*; 7.36 *peccat,*; 7.36 *nubat.*; 7.37 *est,*; 7.37 *cogitur,*; 7.37 *est,*; 7.37 *statuit,*; 7.37 *virginem,*; 7.37 *facit.*; 7.38 *elocat,*; 7.38 *facit:*; 7.38 *elocat,*; 7.38 *facit.*; 7.39 *est,*; 7.39 *vir:*; 7.39 *eius,*; 7.39 *ei,*; 7.39 *nubere,*; 7.39 *Domino:*; 7.40 *est,*; 7.40 *manserit,*; 7.40 *sententia.*; 7.40 *Spiritum.*; 9.1 *Domino?*; 9.16 *cogar:*; 9.27 *forte,*; 9.27 *reiectaneus.*; 10.4 *erat.*; 10.7 *ludendum.*; 10.33 *seruentur.*; 11.1 *estote,*; 11.1 *Christi.*; 11.9 *mulier.*; 12.5 *Dominus.*; 13.7 *tolerat,*; 13.7 *credit,*; 13.7 *sperat,*; 13.12 *ambages:*; 13.13 *charitas.*; 14.24 *infidens,*; 15.7 *omnibus.*; 15.9 *sim.*; 15.33 *mala.*; 15.54 *victoriose.*; 16.6 *proficiscar.*; 16.24 *adsit.*; 16.24 *Amen.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
