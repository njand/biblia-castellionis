# Mark 1–16 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Mark 1-16` → `text/orig/draft/MRK.usfm` (now `text/orig/MRK.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Mark.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/MRK.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 9166 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 140 | read in the OCR, a spelling the approved rules normalize |
| variant | 104 | read in the OCR, a printer's spelling no rule covers |
| ę | 8 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 79 | read in the OCR with a nasal bar (m or n put back) |
| misread | 6 | the settled word misread by the OCR; spelling as settled |
| lexicon | 475 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 13 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 32 | OCR unreadable; the settled word in the printer's conventions |
| none | 74 | no OCR word; the settled word in the printer's conventions |
| all | 10097 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **1.6** *pelliciō* → *pelliceo*: 1573 canvas 775, read on the page (read by Claude, 2026-11-13)
- **2.25** *Numquamne* → *Nunquam ne*: 1573 canvas 776, read on the page: two words (read by Claude, 2026-11-13)
- ⚑ **3.32** *circumsedēret* → *circumsideret*: 1573 canvas 777, read on the page (read by Claude, 2026-11-13)
- **9.43** *inexstīnctum* → *inextinctum*: 1573 canvas 782, read on the page (read by Claude, 2026-11-13)
- **1.27** *quænam* → *quæ'nam*: 1573 canvas 775, read on the page (read by Claude, 2026-11-13)
- **13.27** *cælī* → *cœli*: 1573 canvas 785, read on the page: œ (read by Claude, 2026-11-13)
- **12.17** *Cæsarī* → *Cæsari*: 1573 canvas 784, read on the page: ę (read by Claude, 2026-11-13)
- ⚑ **3.33** *iīs* → *eis*: 1573 canvas 777, read on the page (read by Claude, 2026-11-13)
- ⚑ **7.36** *iīs* → *eis*: 1573 canvas 780, read on the page (read by Claude, 2026-11-13)
- ⚑ **9.2** *iīs* → *eis*: 1573 canvas 781, read on the page (read by Claude, 2026-11-13)
- ⚑ **11.12** *iīs* → *eis*: 1573 canvas 783, read on the page (read by Claude, 2026-11-13)
- ⚑ **15.9** *iīs* → *eis*: 1573 canvas 787, read on the page (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (140)

*adulēscentem* → *adolescentem*; *adulēscēns* → *adolescens*; *cotīdiē* → *quotidie*; *dextram* → *dexteram* ×5; *exspectābat* → *expectabat*; *immō* → *imo*; *intellegant* → *intelligant*; *intellegerent* → *intelligerent*; *intellegite* → *intelligite*; *intellegēns* → *intelligens*; *intellegō* → *intelligo*; *iīs* → *eis* ×84; *iīsque* → *eisque* ×10; *miseritus* → *misertus* ×3; *quattuor* → *quatuor* ×4; *quemquam* → *quenquam* ×3; *quidquam* → *quicquam* ×3; *quidquid* → *quicquid* ×6; *quīcumque* → *quicunque*; *sepulcrētīs* → *sepulchretis*; *sæpe* → *sepe* ×2; *temptandī* → *tentandi*; *temptantēs* → *tentantes*; *temptātis* → *tentatis*; *temptātiōnem* → *tentationem*; *temptātusque* → *tentatusque*; *trīcēsimō* → *trigesimo*; *āeriæ* → *aereæ* ×2

## Printer's spellings no rule covers (103)

*aliōquī* → *alioquin* ×2; *andrēam* → *andræam*; *arcessendum* → *accersendum*; *arcesserent* → *accerserent*; *arcessit* → *accersit*; *arcessī* → *accersi*; *arcessītō* → *accersito*; *audierint* → *audiuerint*; *audiērunt* → *audiuerunt*; *audīssent* → *audiuissent*; *audīsset* → *audiuisset* ×3; *audīstis* → *audiuistis*; *barabbam* → *barrabam*; *barabbās* → *barrabas*; *circumdedit* → *circundedit*; *cælestēsque* → *cœlestesque*; *cælum* → *cœlum* ×2; *cælō* → *cœlo* ×3; *cārissimum* → *charissimum*; *cārissimus* → *charissimus* ×2; *cēnāculum* → *cœnaculum*; *cēterum* → *cæterum*; *cēterīs* → *cæteris*; *cōnfestim* → *confesstim*; *exsecrātus* → *execratus*; *exsistent* → *existent*; *exstinguitur* → *extinguitur* ×3; *exstitit* → *extitit* ×3; *exstititque* → *extititque*; *exstitērunt* → *extiterunt* ×2; *exstrūctūrum* → *extructurum*; *exīstis* → *exijstis*; *fēmina* → *fœmina*; *fēminam* → *fœminam*; *fētū* → *fœtu*; *habeātis* → *habeatiss*; *hieme* → *hyeme*; *hērēditās* → *hæreditas*; *hērēs* → *hæres*; *iit* → *iuit* ×2; *impertierit* → *impertiuerit*; *impingere* → *inpingere*; *inexstīnctum* → *inextinctum*; *intellegitis* → *intelligitis* ×4; *iērunt* → *iuerunt*; *jōhannēs* → *iohanes*; *lacrimīs* → *lachrymis*; *monumentum* → *monimentum* ×2; *monumentī* → *monimenti* ×2; *monumentīs* → *monimentis* ×2; *monumentō* → *monimento* ×2; *murrinum* → *myrrhinum*; *mīlia* → *millia* ×3; *negōtium* → *negocium*; *numquam* → *nunquam* ×3; *numquid* → *nunquid*; *nūntium* → *nuncium*; *nūntiārunt* → *nunciarunt*; *nūntiātum* → *nunciatum* ×3; *nūntiātō* → *nunciato*; *nūntiīs* → *nuncijs*; *petīvit* → *petijt*; *pretiōsī* → *preciosi*; *quamdiū* → *quandiu*; *quandōcumque* → *quandocunque*; *quemcumque* → *quemcunque*; *quæcumque* → *quæcunque*; *renūntiet* → *renunciet*; *renūntiāvērunt* → *renunciauerunt*; *sabachtanī* → *sabachthani*; *silvestrī* → *syluestri*; *statimque* → *statiinque*; *tamquam* → *tanquam*; *ubicumque* → *vbicunque* ×2; *umquam* → *vnquam*; *ōtium* → *ocium*

## e against the settled æ, printed æ (1)

*lævāque* → *læuaque*

## ⚑ Other forms of the word (2)

Read in the OCR and taken by the variant rules, but a different form of the word, not only a spelling: the reading edition may want to look again at these.

2.21 *Aliōquī* → *Alioquin*; 2.22 *Aliōquī* → *alioquin*

## Not read in the OCR (112)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Mark.1.1 | Initium | Initium | — |
| Mark.1.4 | ēmendātiōnis | emendationis | — |
| Mark.1.8 | baptīzābit | baptizabit | — |
| Mark.1.10 | columbam | columbam | coluinbaım |
| Mark.1.20 | Zebedæō | Zebedæo | Zebedço |
| Mark.1.28 | Galilæa | Galilæa | — |
| Mark.1.32 | afferēbantur | afferebantur | — |
| Mark.1.40 | congenuclāns | congenuclans | congenulans |
| Mark.2.3 | portābātur | portabatur | — |
| Mark.2.4 | factōque | factoque | — |
| Mark.2.16 | pōtiōnemque | potionemque | potioneings |
| Mark.2.21 | assuit | assuit | — |
| Mark.2.23 | vellerent | vellerent | Sabbato |
| Mark.3.1 | āridam | aridam | aridaın |
| Mark.3.2 | sānāret | sanaret | — |
| Mark.3.5 | tacērent | tacerent | — |
| Mark.3.5 | īrātē | irate | — |
| Mark.3.5 | callum | callum | — |
| Mark.3.5 | Extende | Extende | — |
| Mark.3.5 | extendit | extendit | — |
| Mark.3.8 | Trānsjordānīnō | Transiordanino | — |
| Mark.3.34 | circumsedēbant | circumsedebant | — |
| Mark.4.1 | tantaque | tantaque | tantas |
| Mark.4.8 | ēdiditque | ediditque | edidit |
| Mark.4.22 | patefaciendum | patefaciendum | — |
| Mark.4.24 | mētiendum | metiendum | metiéduin |
| Mark.4.24 | addētur | addetur | addeturau |
| Mark.4.32 | umbrā | vmbra | vinbra |
| Mark.4.35 | Trājiciāmus | Traiiciamus | Traij |
| Mark.4.36 | admīsērunt | admiserunt | — |
| Mark.4.36 | nāviculæ | nauiculæ | — |
| Mark.5.22 | Jaīrus | Iairus | lairus |
| Mark.6.4 | inhonōrātum | inhonoratum | — |
| Mark.6.8 | crumēnā | crumena | — |
| Mark.6.16 | dēcollāsset | decollasset | — |
| Mark.6.21 | nātālicia | natalicia | — |
| Mark.6.27 | dēcollātum | decollatum | — |
| Mark.6.31 | requiēscerent | requiescerent | requiesterét |
| Mark.6.48 | vigiliam | vigiliam | — |
| Mark.6.53 | Gennezarethānum | Gennezarethanum | — |
| Mark.6.56 | pāgōs | pagos | — |
| Mark.6.56 | prōpōnēbant | proponebant | — |
| Mark.6.56 | fora | fora | — |
| Mark.6.56 | ægrōtantēs | ægrotantes | — |
| Mark.6.56 | rogābant | rogabant | — |
| Mark.7.6 | simulātōribus | simulatoribus | — |
| Mark.7.10 | plēctātur | plectatur | Curtaren |
| Mark.7.11 | Corbān | Corban | — |
| Mark.7.13 | rescindentēs | rescindentes | fcindentes |
| Mark.7.21 | prāvæ | prauæ | — |
| Mark.7.26 | Syrophœnissa | Syrophœnissa | — |
| Mark.7.26 | fīliā | filia | — |
| Mark.7.28 | puerōrum | puerorum | — |
| Mark.7.33 | immīsit | immisit | — |
| Mark.7.36 | præcipiēbat | præcipiebat | — |
| Mark.8.3 | dēfetīscentur | defetiscentur | — |
| Mark.8.16 | pertinēre | pertinere | — |
| Mark.8.34 | sibimet | sibimet | — |
| Mark.8.38 | adulterīnā | adulterina | — |
| Mark.9.7 | vēnitque | venitque | — |
| Mark.9.12 | contemnendum | contemnendum | — |
| Mark.9.24 | diffīdentiæ | diffidentiæ | dif |
| Mark.9.32 | ignōrābant | ignorabant | ignombant |
| Mark.9.49 | sale | sale | — |
| Mark.9.49 | saliendum | saliendum | — |
| Mark.9.50 | condiētur | condietur | — |
| Mark.10.13 | Addūcēbantur | Adducebantur | — |
| Mark.10.24 | frētōs | fretos | — |
| Mark.10.34 | interficiendum | interficiendum | — |
| Mark.10.46 | Tīmæī | Timæi | Timai |
| Mark.10.46 | Bartimæus | Bartimæus | Bartinæus |
| Mark.11.3 | dīmittet | dimittet | di |
| Mark.11.8 | sternere | sternere | — |
| Mark.11.11 | circumspectīs | circumspectis | — |
| Mark.11.12 | Bēthaniā | Bethania | — |
| Mark.11.12 | ēgressīs | egressis | — |
| Mark.11.15 | nummulāriōrum | nummulariorum | nutmulariorum |
| Mark.11.23 | dubitāverit | dubitauerit | dubitainuerit |
| Mark.11.24 | assecūtūrōs | assecuturos | afssecuturos |
| Mark.11.28 | faciendī | faciendi | — |
| Mark.12.1 | locāvit | locauit | — |
| Mark.12.15 | Pendāmus | pendamus | pendainus |
| Mark.12.15 | videam | videam | — |
| Mark.12.22 | prōgeniem | progeniem | — |
| Mark.12.25 | conjungentur | coniungentur | con |
| Mark.12.25 | cōnūbia | conubia | iungenturconnubia |
| Mark.12.28 | disceptantibus | disceptantibus | — |
| Mark.12.34 | respondisse | respondisse | refpondifsse |
| Mark.12.39 | accubandī | accubandi | maaccubandi |
| Mark.13.1 | Exeuntī | Exeunti | — |
| Mark.13.11 | præmeditārī | præmeditari | præineditari |
| Mark.13.22 | falsīque | falsique | falsins |
| Mark.13.27 | dīmissīs | dimissis | dimilsis |
| Mark.13.30 | sæculum | sæculum | hocfeculum |
| Mark.14.1 | studēbant | studebant | itudebant |
| Mark.14.3 | alabastrō | alabastro | — |
| Mark.14.4 | indignābantur | indignabantur | — |
| Mark.14.9 | pūblicābitur | publicabitur | — |
| Mark.14.12 | azȳmālium | azymalium | azyınalium |
| Mark.14.18 | prōdat | prodat | — |
| Mark.14.18 | epulātur | epulatur | — |
| Mark.15.1 | trādunt | tradunt | — |
| Mark.15.21 | Cȳrēnæum | Cyrenæum | Cyrenqum |
| Mark.15.21 | cōgunt | cogunt | — |
| Mark.15.34 | lāmā | lama | — |
| Mark.15.36 | spongiā | spongia | — |
| Mark.15.36 | arundinīque | arundinique | — |
| Mark.15.38 | fissum | fissum | — |
| Mark.15.46 | excīsum | excisum | — |
| Mark.16.8 | metuerent | metuerent | me |
| Mark.16.12 | ambulantibus | ambulantibus | aimbulantibus |
| Mark.16.17 | novīs | nouis | — |

## Punctuation not from the OCR (77)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *Christi,*; 1.1 *Filij,*; 1.8 *baptizabit.*; 2.3 *portabatur,*; 2.4 *sideratus.*; 2.15 *fuerant),*; 2.23 *vellerent.*; 3.1 *collegium,*; 3.4 *alloquens:*; 3.4 *facere,*; 3.4 *facere?*; 3.4 *seruare,*; 3.4 *interficere?*; 3.5 *tacerent,*; 3.5 *intuitus,*; 3.5 *dolens,*; 3.5 *homini:*; 3.5 *tuam.*; 3.5 *extendit,*; 3.5 *est,*; 4.16 *lætitia.*; 4.21 *lecto?*; 4.21 *ponatur?*; 4.35 *Traiiciamus.*; 4.41 *obediant?*; 5.1 *Gadarenorum,*; 5.20 *omnes.*; 5.22 *accidit,*; 5.34 *seruauit.*; 6.8 *crumena,*; 6.9 *tunicas.*; 6.27 *iuit.*; 6.32 *seorsum:*; 6.56 *pagos,*; 6.56 *ægrotantes,*; 7.10 *plectatur.*; 7.26 *filia.*; 7.28 *micis.*; 8.3 *via:*; 8.3 *venerunt.*; 8.4 *responderunt:*; 8.6 *multitudini.*; 8.9 *millia:*; 8.29 *esse?*; 9.2 *eis,*; 9.22 *misertus.*; 9.24 *diffidentiæ.*; 9.49 *est.*; 10.12 *adulterat.*; 10.27 *fieri.*; 11.3 *dimittet.*; 11.8 *sternere:*; 11.11 *Dominus,*; 11.11 *templum:*; 11.11 *circumspectis,*; 11.11 *hora,*; 11.11 *duodecim.*; 11.25 *est,*; 12.8 *eiecerunt.*; 12.10 *anguli,*; 12.24 *potentiam.*; 12.25 *cœlis.*; 12.34 *ei:*; 14.4 *indignabantur,*; 14.4 *dicebant:*; 14.18 *prodat,*; 14.18 *epulatur.*; 14.32 *eo.*; 14.45 *Magister,*; 15.1 *tradunt.*; 15.12 *dicitis?*; 15.18 *Iudæorum.*; 15.21 *crucem.*; 15.26 *Iudæorum.*; 15.36 *spongia,*; 16.8 *metuerent.*; 16.17 *nouis:*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
