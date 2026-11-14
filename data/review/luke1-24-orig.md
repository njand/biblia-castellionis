# Luke 1–24 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Luke 1-24` → `text/orig/draft/LUK.usfm` (now `text/orig/LUK.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Luke.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/LUK.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 15581 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 168 | read in the OCR, a spelling the approved rules normalize |
| variant | 158 | read in the OCR, a printer's spelling no rule covers |
| ę | 22 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 187 | read in the OCR with a nasal bar (m or n put back) |
| misread | 29 | the settled word misread by the OCR; spelling as settled |
| lexicon | 1045 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 22 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 61 | OCR unreadable; the settled word in the printer's conventions |
| none | 148 | no OCR word; the settled word in the printer's conventions |
| all | 17421 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **1.52** *foliīs* → *solijs*: 1573 canvas 789, read on the page: long s, not f (de solijs) (read by Claude, 2026-11-13)
- **2.25** *exspectāns* → *expectans*: 1573 canvas 791, read on the page (read by Claude, 2026-11-13)
- ✱ **3.7** *summōvit* → *summonuit*: 1573 canvas 792, read on the page (twice): a misprint for summouit, printed as is (read by Claude, 2026-11-13)
- **3.37** *Henōchī* → *Enochi*: 1573 canvas 792, read on the page (read by Claude, 2026-11-13)
- **4.2** *temptātus* → *tentatus*: 1573 canvas 792, read on the page: printed tẽtatus (read by Claude, 2026-11-13)
- ⚑ **5.39** *pōtō* → *potato*: 1573 canvas 794, read on the page (read by Claude, 2026-11-13)
- **7.19** *exspectēmus* → *expectemus*: 1573 canvas 795, read on the page (read by Claude, 2026-11-13)
- ⚑ **9.60** *adnūntiātum* → *annunciatum*: 1573 canvas 798, read on the page (read by Claude, 2026-11-13)
- **12.36** *exspectantibus* → *expectantibus*: 1573 canvas 801, read on the page: line break: expe-ctantibus (read by Claude, 2026-11-13)
- ⚑ **13.18** *assimulem* → *assimilem*: 1573 canvas 802, read on the page (read by Claude, 2026-11-13)
- ⚑ **15.20** *īnsiluit* → *insilijt*: 1573 canvas 804, read on the page (read by Claude, 2026-11-13)
- **18.21** *exsecūtus* → *executus*: 1573 canvas 806, read on the page (read by Claude, 2026-11-13)
- **21.32** *præteritūram* → *præterituram*: 1573 canvas 809, read on the page: ę (read by Claude, 2026-11-13)
- **3.16** *Jōhannēs* → *Iohannes*: 1573 canvas 792, read on the page (read by Claude, 2026-11-13)
- **7.44** *lacrimīs* → *lacrimis*: 1573 canvas 796, read on the page (read by Claude, 2026-11-13)
- **8.1** *nūntiāns* → *nuncians*: 1573 canvas 796, read on the page: printed nunciás (the mark a nasal bar) (read by Claude, 2026-11-13)
- ⚑ **18.1** *iīs* → *eis*: 1573 canvas 806, read on the page (read by Claude, 2026-11-13)
- ⚑ **19.33** *iīs* → *eis*: 1573 canvas 807, read on the page (read by Claude, 2026-11-13)
- ⚑ **22.58** *iīs* → *eis*: 1573 canvas 810, read on the page (read by Claude, 2026-11-13)
- ⚑ **23.34** *iīs* → *eis*: 1573 canvas 811, read on the page (read by Claude, 2026-11-13)
- ⚑ **24.36** *iīs* → *eis*: 1573 canvas 812, read on the page (read by Claude, 2026-11-13)
- ⚑ **24.45** *iīs* → *eis*: 1573 canvas 813, read on the page (read by Claude, 2026-11-13)
- **24.9** *reversæ* → *reuersæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (168)

*adulēscēns* → *adolescens*; *condiciō* → *conditio*; *condiciōnem* → *conditionem*; *cotīdiē* → *quotidie* ×5; *cum* → *quum*; *decumātis* → *decimatis*; *dextram* → *dexteram* ×3; *dextrā* → *dextera*; *erus* → *herus* ×4; *erō* → *hero*; *exspectābant* → *expectabant* ×2; *exspectābat* → *expectabat*; *exspectātiōne* → *expectatione*; *exspectēmus* → *expectemus*; *immō* → *imo*; *intellegant* → *intelligant*; *intellegātis* → *intelligatis*; *intellegēns* → *intelligens* ×2; *iīs* → *eis* ×102; *iīsque* → *eisque* ×10; *miseritus* → *misertus* ×2; *obœdiant* → *obediant*; *obœdīret* → *obediret*; *pæniteat* → *pœniteat*; *quattuor* → *quatuor*; *quemquam* → *quenquam* ×2; *quidquam* → *quicquam* ×2; *quidquid* → *quicquid* ×3; *quotiēns* → *quoties*; *quīcumque* → *quicunque* ×3; *sepulcra* → *sepulchra*; *sæculī* → *seculi*; *temptātiōne* → *tentatione*; *temptātiōnem* → *tentationem* ×3; *temptātō* → *tentato*; *umerīs* → *humeris*; *āeriæ* → *aereæ* ×2

## Printer's spellings no rule covers (158)

*abligūrīvit* → *abligurijt*; *aliquamdiū* → *aliquandiu*; *aliōquī* → *alioquin* ×2; *arcessit* → *accersit*; *arcessī* → *accersi*; *arcessītīs* → *accersitis*; *auctōritās* → *autoritas*; *auctōritāte* → *autoritate*; *audierant* → *audiuerant*; *audiērunt* → *audiuerunt*; *audīsse* → *audiuisse*; *audīsset* → *audiuisset*; *barabbam* → *barrabam*; *bracchiō* → *brachio*; *circumdatam* → *circundatam*; *coiit* → *coiuit*; *committendum* → *commitendum*; *cuicumque* → *cuicunque*; *cælum* → *cœlum* ×5; *cælīque* → *cœlique*; *cælō* → *cœlo* ×8; *cælōne* → *cœlone*; *cārissimum* → *charissimum*; *cārissimus* → *charissimus* ×2; *cēnam* → *cœnam* ×2; *cēnamve* → *cœnamue*; *cēnæ* → *cœnæ*; *cēnāculum* → *cœnaculum*; *cēnīs* → *cœnis*; *cēterum* → *cæterum* ×4; *cēterīs* → *cæteris* ×2; *cœperit* → *ceperit*; *diciōnis* → *ditionis*; *dēversātum* → *diuersatum*; *dēversōrium* → *diuersorium* ×2; *dēversōriō* → *diuersorio*; *erī* → *heri* ×2; *exiit* → *exiuit*; *exsequitur* → *exequitur*; *exsisteret* → *existeret*; *exstirpārētur* → *extirparetur*; *exstitisse* → *extitisse*; *exstitit* → *extitit* ×5; *exstitērunt* → *extiterunt*; *exstruitis* → *extruitis* ×2; *exsultatque* → *exultatque*; *exsultāte* → *exultate*; *exsultāvit* → *exultauit* ×3; *fēmina* → *fœmina* ×2; *fēminam* → *fœminam* ×2; *fēminæ* → *fœminæ* ×3; *fēminīs* → *fœminis*; *fētus* → *fœtus*; *hocine* → *hoccine*; *holus* → *olus*; *hædum* → *hœdum*; *hērēditās* → *hæreditas*; *hērēditātem* → *hæreditatem*; *hērēs* → *hæres*; *ieris* → *iueris*; *iit* → *iuit*; *impedīstis* → *impediuistis*; *incrēbrēscente* → *increbescente*; *inexspectātō* → *inexpectato*; *inexstīnctō* → *inextincto*; *intellegenda* → *intelligenda*; *jācōbæōrum* → *iacobeorum*; *jōhannem* → *iohanem* ×2; *jōhannēs* → *iohanes*; *litterīs* → *literis*; *mattathīæ* → *mathathiæ*; *monumenta* → *monimenta*; *monumentum* → *monimentum* ×3; *monumentō* → *monimento*; *mīlia* → *millia*; *negōtia* → *negocia*; *negōtiandō* → *negociando*; *negōtium* → *negocium*; *nescierit* → *nesciuerit*; *numquam* → *nunquam*; *nūntianda* → *nuncianda*; *nūntium* → *nuncium*; *nūntiāre* → *nunciare*; *nūntiārem* → *nunciarem*; *nūntiārunt* → *nunciarunt* ×3; *nūntiātum* → *nunciatum*; *nūntiātur* → *nunciatur*; *nūntiīs* → *nuncijs*; *nūntiō* → *nuncio*; *nūntiōs* → *nuncios*; *petīvit* → *petijt*; *pretiō* → *precio*; *prœlium* → *prælium*; *quamcumque* → *quamcunque*; *quamdiū* → *quandiu*; *quamquam* → *quanquam*; *quæsīssent* → *quæsiuissent*; *quōcumque* → *quocunque*; *renūntiārunt* → *renunciarunt*; *renūntiātum* → *renunciatum*; *repperit* → *reperit*; *sincērus* → *syncerus*; *sollicitī* → *soliciti* ×2; *spatiō* → *spacio*; *sæcula* → *secula*; *sæculō* → *seculo*; *sīc* → *ssic*; *tamquam* → *tanquam* ×3; *temptāvit* → *tentauit*; *tetrarchē* → *tetrarcha* ×3; *tetrarchēs* → *tetrarcha* ×2; *tætrum* → *tetrum*; *umquam* → *vnquam* ×2; *vēneant* → *væneant*; *īsset* → *iuisset*

## ⚑ Other forms of the word (8)

Read in the OCR and taken by the variant rules, but a different form of the word, not only a spelling: the reading edition may want to look again at these.

3.1 *tetrarchē* → *tetrarcha*; 3.19 *tetrarchēs* → *tetrarcha*; 5.15 *Incrēbrēscente* → *Increbescente*; 5.36 *aliōquī* → *alioquin*; 5.37 *aliōquī* → *alioquin*; 9.7 *tetrarchēs* → *tetrarcha*

## Not read in the OCR (238)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Luke.1.3 | cōnsectātus | consectatus | — |
| Luke.1.10 | ōrante | orante | — |
| Luke.1.13 | exaudītæ | exauditæ | — |
| Luke.1.17 | prūdentiam | prudentiam | prudentiain |
| Luke.1.17 | Dominōque | Dominoque | — |
| Luke.1.27 | virginem | virginem | — |
| Luke.1.27 | dēspōnsam | desponsam | — |
| Luke.1.28 | fortūnātissima | fortunatissima | — |
| Luke.1.31 | paritūramque | parituramque | arituramque |
| Luke.1.35 | inumbrābit | inumbrabit | imumbrabit |
| Luke.1.39 | montāna | montana | — |
| Luke.1.62 | appellārī | appellari | pellari |
| Luke.1.71 | vindicēmur | vindicemur | vindicemut |
| Luke.1.73 | prōmīserit | promiserit | piniserit |
| Luke.2.1 | Augustō | Augusto | — |
| Luke.2.1 | Cæsare | Cæsare | — |
| Luke.2.1 | cēnsērētur | censeretur | — |
| Luke.2.2 | prætōre | prætore | — |
| Luke.2.2 | Syriæ | Syriæ | — |
| Luke.2.5 | prægnante | prægnante | — |
| Luke.2.6 | pariendum | pariendum | — |
| Luke.2.21 | nuncupātum | nuncupatum | — |
| Luke.2.21 | conciperētur | conciperetur | — |
| Luke.2.22 | Complētīs | Completis | — |
| Luke.2.22 | pūrificātiōnis | purificationis | — |
| Luke.2.22 | sisterent | sisterent | — |
| Luke.2.23 | vulvam | vuluam | — |
| Luke.2.24 | cōnferrent | conferrent | — |
| Luke.2.24 | turturum | turturum | — |
| Luke.2.24 | pīpiōnēs | pipiones | — |
| Luke.2.25 | Simeōn | Simeon | — |
| Luke.2.26 | sēnsūrum | sensurum | — |
| Luke.2.27 | intulērunt | intulerunt | — |
| Luke.2.28 | excēpit | excepit | — |
| Luke.2.29 | dīmittis | dimittis | — |
| Luke.2.29 | prōmissiōnem | promissionem | — |
| Luke.2.29 | placidē | placide | — |
| Luke.2.31 | expositam | expositam | — |
| Luke.2.31 | parāstī | parasti | — |
| Luke.2.32 | patefaciendum | patefaciendum | — |
| Luke.2.40 | cōnfirmābātur | confirmabatur | — |
| Luke.2.40 | sapientiāque | sapientiaque | — |
| Luke.2.46 | invēnerint | inuenerint | — |
| Luke.2.51 | vēnitque | venitque | venitý |
| Luke.3.16 | baptīzābit | baptizabit | — |
| Luke.3.17 | arcamque | arcamque | areamqu |
| Luke.3.25 | Essis | Essis | Eslis |
| Luke.3.28 | Cosamī | Cosami | Cosani |
| Luke.3.31 | Nāthanī | Nathani | Nathami |
| Luke.3.35 | Sarūchī | Saruchi | — |
| Luke.3.35 | Ragāvī | Ragaui | — |
| Luke.3.35 | Phalecī | Phaleci | — |
| Luke.3.35 | Hebris | Hebris | — |
| Luke.3.35 | Salæ | Salæ | — |
| Luke.3.36 | Caīnānis | Cainanis | — |
| Luke.3.36 | Arphaxātī | Arphaxati | — |
| Luke.3.36 | Sēmī | Semi | — |
| Luke.3.36 | Lamechī | Lamechi | — |
| Luke.3.37 | Mathusalæ | Mathusalæ | — |
| Luke.3.37 | Jarēthī | Iarethi | — |
| Luke.3.37 | Maleleēlis | Maleleelis | — |
| Luke.3.37 | Caīnānis | Cainanis | — |
| Luke.3.38 | Ēnōsī | Enosi | — |
| Luke.3.38 | Sēthī | Sethi | — |
| Luke.3.38 | Ādamī | Adami | — |
| Luke.4.5 | mōmentō | momento | — |
| Luke.4.16 | legendum | legendum | — |
| Luke.4.33 | dæmoniī | dæmonii | — |
| Luke.4.38 | gravī | graui | — |
| Luke.4.39 | febrem | febrem | tebrem |
| Luke.4.39 | febris | febris | — |
| Luke.5.6 | conclūsērunt | concluserunt | — |
| Luke.5.14 | pūrgātiōnem | purgationem | purgationein |
| Luke.5.17 | passim | passim | passiin |
| Luke.5.18 | prōpōnere | proponere | pro |
| Luke.5.29 | celebre | celebre | celebrem |
| Luke.5.33 | crēbrō | crebro | — |
| Luke.5.36 | novæ | nouæ | noua |
| Luke.6.8 | stā | sta | ita |
| Luke.6.12 | ōrandum | orandum | — |
| Luke.6.13 | nōmināvit | nominauit | — |
| Luke.6.22 | sēparābunt | separabunt | — |
| Luke.6.30 | auferente | auferente | — |
| Luke.6.30 | repete | repete | — |
| Luke.6.37 | damnābiminī | damnabimini | damnabiinini |
| Luke.6.38 | remētiētur | remetietur | — |
| Luke.6.42 | extraham | extraham | — |
| Luke.6.48 | altē | alte | tè |
| Luke.7.2 | jamjam | iamiam | iamiain |
| Luke.7.14 | restitissent | restitissent | rettitiffent |
| Luke.7.15 | loquīque | loquique | loquis |
| Luke.7.17 | fīnitimamque | finitimamque | finitimamqa |
| Luke.7.24 | agitātam | agitatam | agitatain |
| Luke.7.27 | præmissūrus | præmissurus | furus |
| Luke.7.49 | convīvæ | conuiuæ | — |
| Luke.8.1 | pāgātim | pagatim | pagatiin |
| Luke.8.7 | spīnæ | spinæ | fpina |
| Luke.8.9 | quænam | quænam | — |
| Luke.8.13 | perīculōrum | periculorum | periculoruin |
| Luke.8.16 | lectōve | lectoue | lettoue |
| Luke.8.16 | ingredientēs | ingredientes | — |
| Luke.8.18 | ēripiētur | eripietur | cripietur |
| Luke.8.29 | Jusserat | Iusserat | lusserat |
| Luke.8.35 | mentīs | mentis | inentis |
| Luke.8.41 | Jaīrus | Iairus | lairus |
| Luke.9.12 | dēversentur | deuersentur | — |
| Luke.9.13 | pōpulum | populum | populuın |
| Luke.9.16 | appōnendōs | apponendos | dos |
| Luke.9.38 | ūnicus | vnicus | — |
| Luke.9.42 | convellit | conuellit | couulsit |
| Luke.9.47 | prehēnsō | prehenso | — |
| Luke.9.62 | admōtā | admota | adnota |
| Luke.10.11 | abstergēmus | abstergemus | abstergimus |
| Luke.10.13 | redīssent | redissent | — |
| Luke.10.21 | patefēcerīs | patefeceris | — |
| Luke.10.30 | dēspoliārunt | despoliarunt | difpoliarunt |
| Luke.10.35 | solūtūrum | soluturum | soluturuin |
| Luke.10.40 | sōlam | solam | folain |
| Luke.11.3 | alimentārium | alimentarium | alimétariuın |
| Luke.11.4 | remittimus | remittimus | reinittimus |
| Luke.11.21 | armātus | armatus | arinatus |
| Luke.11.28 | cōnservant | conseruant | — |
| Luke.11.39 | exteriōrem | exteriorem | — |
| Luke.11.48 | testāminī | testamini | — |
| Luke.11.49 | persequentur | persequentur | petsequentur |
| Luke.11.50 | sūmātur | sumatur | fuinatur |
| Luke.11.52 | abstulistis | abstulistis | — |
| Luke.11.54 | crīminārentur | criminarentur | — |
| Luke.12.2 | dētegendum | detegendum | — |
| Luke.12.9 | abnegābitur | abnegabitur | — |
| Luke.12.11 | potestātēsque | potestatesque | — |
| Luke.12.18 | cōnstruam | construam | construain |
| Luke.12.18 | congeram | congeram | congerain |
| Luke.12.19 | Anima | Anima | Aniina |
| Luke.12.24 | Contemplāminī | Contemplamini | — |
| Luke.12.26 | sollicitāminī | sollicitamini | — |
| Luke.12.27 | labōrent | laborent | — |
| Luke.12.31 | addentur | addentur | ad |
| Luke.12.42 | prūdēns | prudens | — |
| Luke.12.45 | famulās | famulas | — |
| Luke.12.46 | dissecābit | dissecabit | — |
| Luke.12.49 | incēnsus | incensus | fus |
| Luke.12.50 | absolvātur | absoluatur | — |
| Luke.12.53 | nurus | nurus | Expresen |
| Luke.12.54 | exorientem | exorientem | — |
| Luke.13.4 | Hierosolymītānōrum | Hierosolymitanorum | Hierofolymitanoruin |
| Luke.13.11 | dēbilitātis | debilitatis | — |
| Luke.13.20 | assimulem | assimulem | — |
| Luke.13.21 | farīnæ | farinæ | — |
| Luke.13.24 | angustam | angustam | — |
| Luke.13.24 | cōnābuntur | conabuntur | — |
| Luke.13.25 | cœperitis | cœperitis | cœperi tis |
| Luke.13.33 | ambulandum | ambulandum | ambulanduin |
| Luke.13.34 | congregāre | congregare | — |
| Luke.14.8 | accubāre | accubare | — |
| Luke.14.10 | ascende | ascende | astende |
| Luke.14.34 | condiētur | condietur | — |
| Luke.15.1 | Frequentābant | Frequentabant | — |
| Luke.15.2 | improbōs | improbos | eumimprobos |
| Luke.15.4 | perditam | perditam | perditain |
| Luke.15.8 | drachmam | drachmam | drachinam |
| Luke.15.9 | drachmam | drachmam | drachman |
| Luke.15.17 | mercēnāriī | mercenarii | inercenarij |
| Luke.15.22 | stolam | stolam | stolain |
| Luke.15.25 | propinquāsset | propinquasset | propinquaflet |
| Luke.15.30 | mactāstī | mactasti | mactati |
| Luke.16.2 | redde | redde | — |
| Luke.16.2 | dispēnsātiōnis | dispensationis | — |
| Luke.16.2 | licēbit | licebit | — |
| Luke.16.3 | dispēnsātor | dispensator | — |
| Luke.16.3 | dispēnsātiōnem | dispensationem | — |
| Luke.16.3 | auferat | auferat | — |
| Luke.16.3 | Fodere | Fodere | — |
| Luke.16.15 | abōminandum | abominandum | — |
| Luke.16.21 | lingēbant | lingebant | — |
| Luke.17.2 | asināriā | asinaria | — |
| Luke.17.7 | accubitum | accubitum | atcubitum |
| Luke.17.8 | cēnem | cenem | cœne |
| Luke.17.8 | accīnctusque | accinctusque | actinctusque |
| Luke.18.1 | ōrandum | orandum | dum |
| Luke.18.2 | reverēbātur | reuerebatur | reue |
| Luke.18.4 | metuō | metuo | inetuo |
| Luke.18.12 | Jejūnō | Ieiuno | leiuno |
| Luke.18.20 | honōrātō | honorato | — |
| Luke.18.21 | ineunte | ineunte | — |
| Luke.18.22 | deest | deest | — |
| Luke.18.22 | vēnde | vende | — |
| Luke.18.22 | dispertīre | dispertire | — |
| Luke.18.23 | trīstis | tristis | — |
| Luke.18.23 | prædīves | prædiues | — |
| Luke.18.24 | trīstem | tristem | — |
| Luke.18.24 | pecūniās | pecunias | — |
| Luke.18.24 | intrābunt | intrabunt | — |
| Luke.19.2 | Zachæus | Zachæus | — |
| Luke.19.2 | vocābātur | vocabatur | — |
| Luke.19.3 | parvus | paruus | par |
| Luke.19.12 | invāderet | inuaderet | — |
| Luke.19.27 | rēgnāre | regnare | — |
| Luke.19.29 | Bēthphagem | Bethphagem | Betphagen |
| Luke.19.44 | nōverīs | noueris | — |
| Luke.20.9 | ēlocātā | elocata | — |
| Luke.20.10 | verberātum | verberatum | — |
| Luke.20.16 | ēlocābit | elocabit | — |
| Luke.20.26 | respōnsiōnem | responsionem | responsionein |
| Luke.20.26 | tacuērunt | tacuerunt | ta |
| Luke.20.45 | audiente | audiente | — |
| Luke.20.45 | cūnctō | cuncto | — |
| Luke.20.46 | accubitiōnēs | accubitiones | accubationes |
| Luke.21.12 | trādēminī | trademini | tradenini |
| Luke.21.12 | perdūcēminī | perducemini | perduce |
| Luke.21.26 | orbī | orbi | — |
| Luke.21.30 | cernentēs | cernentes | tes |
| Luke.22.6 | pollicitus | pollicitus | — |
| Luke.22.7 | immolandum | immolandum | — |
| Luke.22.13 | parārunt | pararunt | — |
| Luke.22.15 | pollūcendī | pollucendi | — |
| Luke.22.35 | dīmīsī | dimisi | dinisi |
| Luke.22.36 | emat | emat | einat |
| Luke.22.43 | cōnfirmāret | confirmaret | — |
| Luke.22.44 | dēlābentibus | delabentibus | — |
| Luke.22.50 | Percussitque | percussitque | percussités |
| Luke.22.53 | injēcistis | iniecistis | iniectstis |
| Luke.22.63 | verberantēs | verberantes | — |
| Luke.23.7 | Hērōdem | Herodem | Herodeın |
| Luke.23.12 | Factīsque | factisque | factics |
| Luke.23.29 | sterilēs | steriles | — |
| Luke.23.29 | lactāverint | lactauerint | la |
| Luke.23.32 | Dūcēbantur | Ducebantur | Apoc |
| Luke.23.33 | Calvāria | Caluaria | — |
| Luke.23.34 | nesciunt | nesciunt | — |
| Luke.23.38 | Hebraicīs | Hebraicis | — |
| Luke.23.49 | aspicientēs | aspicientes | — |
| Luke.23.52 | postulāvit | postulauit | postu |
| Luke.24.17 | sermōnēs | sermones | serinones |
| Luke.24.19 | Quænam | Quænam | — |
| Luke.24.24 | dīxerant | dixerant | — |
| Luke.24.32 | ārdēbat | ardebat | — |
| Luke.24.41 | mīrārentur | mirarentur | — |

## Punctuation not from the OCR (172)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *rerum,*; 1.5 *Elisabeta.*; 1.10 *orante.*; 1.18 *natu?*; 1.28 *fortunatissima.*; 1.30 *Deum,*; 1.34 *angelo,*; 1.46 *Dominum,*; 1.69 *Dauidis,(*; 2.1 *Cæsare,*; 2.1 *orbis,*; 2.6 *tempore,*; 2.10 *allocutus:*; 2.17 *fuisset.*; 2.21 *Iesus,*; 2.21 *angelo,*; 2.21 *conciperetur.*; 2.22 *diebus,*; 2.22 *Hierosolymam,*; 2.22 *sisterent(*; 2.23 *est,*; 2.23 *marem,*; 2.23 *aperuisset,*; 2.23 *dicendum),*; 2.24 *conferrent,*; 2.24 *est:*; 2.24 *turturum,*; 2.24 *pipiones.*; 2.25 *Simeon,*; 2.25 *erat,*; 2.25 *religiosus,*; 2.25 *consolationem,*; 2.25 *præditus.*; 2.26 *dictum,*; 2.26 *sensurum,*; 2.26 *vidisset.*; 2.27 *fanum,*; 2.27 *Iesum,*; 2.27 *facerent,*; 2.28 *excepit,*; 2.28 *verbis:*; 2.29 *me,*; 2.29 *Domine,*; 2.29 *placide.*; 2.30 *tuam,*; 2.31 *parasti:*; 2.32 *patefaciendum,*; 2.32 *gloriam.*; 2.40 *confirmabatur,*; 2.48 *fecisti?*; 3.16 *allocutus:*; 3.16 *baptizabit.*; 3.35 *filij,*; 3.35 *filij,*; 3.35 *filij,*; 3.35 *filij,*; 3.35 *filij,*; 3.36 *filij,*; 3.36 *filij,*; 3.36 *filij,*; 3.36 *filij,*; 3.36 *filij,*; 3.37 *filij,*; 3.37 *filij,*; 3.37 *filij,*; 3.37 *filij,*; 3.37 *filij,*; 3.38 *filij,*; 3.38 *filij,*; 3.38 *filij.*; 4.28 *surrexerunt,*; 5.10 *socij.*; 5.18 *proponere.*; 5.20 *fiduciam,*; 5.27 *ei:*; 5.27 *me.*; 6.3 *inquit,*; 6.30 *repete.*; 6.45 *os.*; 7.19 *est,*; 7.20 *est,*; 7.48 *ei.*; 7.50 *salua.*; 8.11 *sermo.*; 8.27 *monimentis.*; 9.1 *morbos,*; 9.17 *duodecim.*; 9.55 *inquit,*; 11.2 *terra.*; 11.17 *cadit.*; 11.28 *ille:*; 11.28 *Imo,*; 11.28 *inquit,*; 11.32 *præstantior.*; 11.54 *criminarentur.*; 12.2 *detegendum,*; 12.2 *occultum,*; 12.21 *est.*; 12.23 *indumentum.*; 12.31 *addentur.*; 12.53 *nurus.*; 13.20 *assimulem?*; 13.24 *portam.*; 14.10 *Amice,*; 14.34 *condietur?*; 16.2 *eum,*; 16.2 *est:*; 16.2 *est,*; 16.2 *te?*; 16.2 *rationem:*; 16.2 *esse.*; 16.3 *cogitare:*; 16.3 *agam?*; 16.3 *auferat?*; 16.6 *quinquaginta.*; 16.15 *abominandum.*; 17.8 *cenem,*; 18.2 *reuerebatur.*; 18.9 *exemplum:*; 18.20 *dicito:*; 18.20 *honorato.*; 18.21 *ille:*; 18.21 *omnia,*; 18.21 *inquit,*; 18.21 *ætate.*; 18.22 *auditis,*; 18.22 *ei:*; 18.22 *deest:*; 18.22 *vende,*; 18.22 *pauperibus,*; 18.22 *thesaurum:*; 18.22 *ades,*; 18.22 *sequere.*; 18.23 *ille,*; 18.23 *auditis,*; 18.23 *factus:*; 18.23 *esset.*; 18.24 *Iesus,*; 18.24 *dixit:*; 18.24 *difficulter,*; 18.24 *habent,*; 18.24 *intrabunt?*; 18.25 *traijci,*; 18.25 *regnum.*; 18.26 *auditores:*; 18.26 *possit?*; 18.26 *inquiunt.*; 18.27 *ille:*; 18.27 *nequeunt,*; 18.39 *mei.*; 19.3 *paruus,*; 19.17 *potestatem.*; 19.28 *ascendens.*; 19.44 *noueris.*; 20.6 *vatem.*; 20.11 *inanem.*; 20.16 *Absit.*; 20.26 *tacuerunt.*; 20.40 *interrogare.*; 20.43 *subsellium.*; 21.12 *perducemini:*; 22.20 *effundendus.*; 22.32 *tuos.*; 22.35 *inquiunt.*; 22.71 *est,*; 23.17 *festum.*; 23.29 *lactauerint.*; 23.34 *eis:*; 23.39 *nos.*; 23.50 *iustus,*; 23.52 *postulauit.*; 24.5 *mortuos?*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. Found here: 10.1 *duos*; 10.17 *duo*; 11.7 *fi ille pul fare perfeuerauerit*; 14.12 *nec*.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
