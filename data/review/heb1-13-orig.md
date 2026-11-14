# Heb 1–13 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Heb 1-13` → `text/orig/draft/HEB.usfm` (now `text/orig/HEB.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Heb.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/HEB.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 4117 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 39 | read in the OCR, a spelling the approved rules normalize |
| variant | 49 | read in the OCR, a printer's spelling no rule covers |
| ę | 5 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 47 | read in the OCR with a nasal bar (m or n put back) |
| misread | 4 | the settled word misread by the OCR; spelling as settled |
| lexicon | 191 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 7 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 22 | OCR unreadable; the settled word in the printer's conventions |
| none | 48 | no OCR word; the settled word in the printer's conventions |
| all | 4529 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **.5** *cærimōniīs* → *ceremonijs*: 1573 canvas 933, read on the page: line break: cere-monijs (read by Claude, 2026-11-13)
- **.28** *exspectantibus* → *expectantibus*: 1573 canvas 933, read on the page: line break: expectan-tibus (read by Claude, 2026-11-13)
- **1.5** *Henōchus* → *Enochus*: 1573 canvas 934, read on the page (read by Claude, 2026-11-13)
- **1.17** *temptārētur* → *tentaretur*: 1573 canvas 935, read on the page: line break: tentare-tur (read by Claude, 2026-11-13)
- **3.21** *exsequendam* → *exequendam*: 1573 canvas 936, read on the page: line break: exe-quendam (read by Claude, 2026-11-13)
- **2.26** *cælum* → *cœlum*: 1573 canvas 936, read on the page: œ (read by Claude, 2026-11-13)
- **.1** *cælīs* → *cœlis*: 1573 canvas 932, read on the page: œ (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (39)

*cotīdiē* → *quotidie* ×3; *cum* → *quum* ×2; *cærimōniārum* → *ceremoniarum* ×2; *cærimōniās* → *ceremonias*; *cærimōniīs* → *ceremonijs*; *cāritātem* → *charitatem*; *cāritātis* → *charitatis*; *decument* → *deciment*; *decumātus* → *decimatus*; *dextram* → *dexteram* ×5; *exspectābat* → *expectabat*; *exspectāns* → *expectans*; *exspectātiō* → *expectatio*; *intellegentēs* → *intelligentes*; *intellegimus* → *intelligimus*; *iīs* → *eis* ×6; *iīsque* → *eisque*; *obœdientiam* → *obedientiam*; *obœdientibus* → *obedientibus*; *obœdīvit* → *obediuit*; *pænitentiæ* → *pœnitentiæ*; *sæpe* → *sepe*; *temptantur* → *tentantur*; *temptārētur* → *tentaretur*; *temptātiōnis* → *tentationis*; *temptātī* → *tentati*

## Printer's spellings no rule covers (49)

*ancoram* → *anchoram*; *auctōrem* → *authorem*; *audierant* → *audiuerant* ×2; *circumdatus* → *circundatus*; *cohērēdibus* → *cohæredibus*; *cuicumque* → *cuicunque*; *cælestem* → *cœlestem*; *cælestis* → *cœlestis*; *decumāvit* → *decimauit*; *dēnūntiātum* → *denunciatum* ×2; *dēnūntiāvit* → *denunciauit*; *exsecrātiōnī* → *execrationi*; *exsecūtī* → *executi*; *exsequar* → *exequar* ×2; *exseruistis* → *exeruistis*; *exsistere* → *existere*; *exsistit* → *existit*; *exstantibus* → *extantibus*; *exstitit* → *extitit*; *exstrūxit* → *extruxit*; *exstīnxērunt* → *extinxerunt*; *fēminæ* → *fœminæ*; *hērēdem* → *hæredem*; *hērēdibus* → *hæredibus*; *hērēditāte* → *hæreditate*; *immūtābilēs* → *inmutabiles*; *lacrimīs* → *lachrymis*; *lītoris* → *littoris*; *numquam* → *nunquam* ×4; *oblitterandum* → *obliterandum*; *quamdiū* → *quandiu*; *quamquam* → *quanquam*; *quemcumque* → *quemcunque*; *sæculōrum* → *seculorum*; *tamquam* → *tanquam* ×4; *temptāvēre* → *tentauere*; *tūribulum* → *thuribulum*; *umquam* → *vnquam* ×2; *vindicāvit* → *vendicauit*

## e against the settled æ, printed æ (2)

*prærogātīvam* → *prærogatiuam*; *ægyptiī* → *ægyptij*

## ⚑ Other forms of the word (1)

Read in the OCR and taken by the variant rules, but a different form of the word, not only a spelling: the reading edition may want to look again at these.

7.6 *decumāvit* → *decimauit*

## Not read in the OCR (74)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Heb.1.1 | Multifāriam | Multifariam | — |
| Heb.1.3 | expressa | expressa | — |
| Heb.1.3 | substantiæ | substantiæ | — |
| Heb.1.3 | feratque | feratque | — |
| Heb.1.3 | potentī | potenti | — |
| Heb.2.6 | meminerīs | memineris | meinineris |
| Heb.2.9 | corōnātum | coronatum | — |
| Heb.3.13 | occallēscat | occallescat | — |
| Heb.3.19 | diffīdentiam | diffidentiam | — |
| Heb.4.2 | conjūnctus | coniunctus | — |
| Heb.4.8 | Jōsua | Iosua | losua |
| Heb.4.9 | sabbatismus | Sabbatismus | Sabbatisimus |
| Heb.4.14 | penetrāvit | penetrauit | — |
| Heb.4.16 | inveniāmus | inueniamus | — |
| Heb.5.2 | ālūcinantibus | alucinantibus | — |
| Heb.5.7 | exaudītus | exauditus | — |
| Heb.5.12 | elementa | elementa | — |
| Heb.6.5 | gustārunt | gustarunt | — |
| Heb.6.6 | relābuntur | relabuntur | — |
| Heb.6.6 | renoventur | renouentur | — |
| Heb.6.6 | fīgant | figant | — |
| Heb.6.6 | ēdant | edant | — |
| Heb.6.8 | affīnis | affinis | — |
| Heb.6.16 | cōnfirmandam | confirmandam | — |
| Heb.7.1 | redeuntī | redeunti | — |
| Heb.7.5 | dūcentēs | ducentes | — |
| Heb.7.7 | præstantiōre | præstantiore | præstan tiore |
| Heb.7.26 | cælīsque | cœlisque | cælisá |
| Heb.8.3 | victimāsque | victimasque | victimas |
| Heb.8.5 | monitus | monitus | — |
| Heb.8.7 | quærerētur | quæreretur | — |
| Heb.9.1 | mundānumque | mundanumque | — |
| Heb.9.6 | obeuntēs | obeuntes | ob |
| Heb.9.7 | imprūdenter | imprudenter | prudenter |
| Heb.9.13 | juvencæque | iuuencæque | iuueces |
| Heb.9.13 | pūritātem | puritatem | puri |
| Heb.9.23 | pūrgārī | purgari | — |
| Heb.10.1 | Umbram | Vmbram | — |
| Heb.10.3 | commemorātiō | commemoratio | comme |
| Heb.10.21 | præfectum | præfectum | prefectű |
| Heb.10.22 | accēdāmus | accedamus | accedainus |
| Heb.10.28 | Mōsaicam | Mosaicam | Mosaicain |
| Heb.10.28 | triumve | triumue | — |
| Heb.10.30 | rependam | rependam | — |
| Heb.11.5 | trānslātus | translatus | — |
| Heb.11.5 | trānslātus | translatus | — |
| Heb.11.5 | nusquam | nusquam | — |
| Heb.11.5 | trānslātiōnem | translationem | — |
| Heb.11.5 | placuisse | placuisse | — |
| Heb.11.13 | amplexī | amplexi | — |
| Heb.11.13 | cōnfessī | confessi | — |
| Heb.11.14 | dēclārant | declarant | — |
| Heb.11.16 | cælestem | cœlestem | coælestem |
| Heb.11.17 | ūnigenitum | vnigenitum | — |
| Heb.11.22 | memorāvit | memorauit | — |
| Heb.11.23 | occultātus | occultatus | — |
| Heb.11.23 | ēdictum | edictum | — |
| Heb.11.28 | fūsiōnem | fusionem | fusionen |
| Heb.11.30 | mœnia | mœnia | incenia |
| Heb.11.32 | narrantem | narrantem | — |
| Heb.11.32 | Samsōne | Samsone | Sampsone |
| Heb.11.33 | obtūrārunt | obturarunt | obthurarut |
| Heb.11.35 | meliōrem | meliorem | quofmeliorem |
| Heb.11.37 | calamitōsī | calamitosi | — |
| Heb.11.37 | ærumnōsī | ærumnosi | — |
| Heb.12.1 | nimbō | nimbo | nimbote |
| Heb.12.1 | testium | testium | stium |
| Heb.12.3 | pertulit | pertulit | ptulit |
| Heb.13.1 | Dūret | Duret | — |
| Heb.13.1 | frāternus | fraternus | — |
| Heb.13.4 | pūniet | puniet | — |
| Heb.13.6 | metuam | metuam | metuain |
| Heb.13.7 | ēventum | euentum | — |
| Heb.13.9 | peregrīnīsque | peregrinisque | peregrinisés |

## Punctuation not from the OCR (28)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.3 *substantiæ,*; 1.3 *sermone,*; 1.5 *erit?*; 1.13 *subsellium?*; 2.7 *tuarum.*; 3.19 *diffidentiam.*; 5.7 *exauditus,*; 6.5 *gustarunt,*; 6.6 *relabuntur,*; 6.6 *renouentur:*; 6.6 *figant,*; 6.16 *confirmandam.*; 9.6 *obeuntes:*; 9.11 *factum,*; 9.13 *puritatem:*; 10.3 *commemoratio.*; 11.3 *cernuntur.*; 11.5 *est,*; 11.5 *sit:*; 11.5 *translatus,*; 11.5 *extitit.*; 11.5 *est,*; 11.17 *tentaretur:*; 11.33 *promissa,*; 11.37 *calamitosi,*; 13.4 *Deus.*; 13.8 *sempiternum:*; 13.13 *ferentes.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
