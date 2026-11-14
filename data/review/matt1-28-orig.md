# Matt 1–28 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Matt 1-28` → `text/orig/draft/MAT.usfm` (now `text/orig/MAT.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Matt.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/MAT.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 14555 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 162 | read in the OCR, a spelling the approved rules normalize |
| variant | 191 | read in the OCR, a printer's spelling no rule covers |
| ę | 15 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 168 | read in the OCR with a nasal bar (m or n put back) |
| misread | 16 | the settled word misread by the OCR; spelling as settled |
| lexicon | 752 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 42 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 42 | OCR unreadable; the settled word in the printer's conventions |
| none | 119 | no OCR word; the settled word in the printer's conventions |
| all | 16062 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **14.14** *miseritus* → *misertus*: 1573 canvas 762, read on the page (Claude, 2026-11-13)
- **14.35** *quibuscumque* → *quibuscunque*: 1573 canvas 762, read on the page: quibuscunq; (Claude, 2026-11-13)
- **15.10** *intellegite* → *intelligite*: 1573 canvas 763, read on the page (Claude, 2026-11-13)
- ⚑ **16.26** *æquiperet* → *æquiparet*: 1573 canvas 764, read on the page (Claude, 2026-11-13)
- ⚑ **17.14** *congenuclāns* → *congenulans*: 1573 canvas 764, read on the page (Claude, 2026-11-13)
- **17.18** *exiitque* → *exijtque*: 1573 OCR exijtó (q; misread), as 1573 prints ij elsewhere (Claude, 2026-11-13)
- **18.21** *septiēsne* → *septies ne*: 1573 canvas 765, read on the page: two words, septiés ne (Claude, 2026-11-13)
- **18.27** *miseritus* → *misertus*: 1573 OCR misertus, as 14:14 on the page (Claude, 2026-11-13)
- **18.32** *arcessītum* → *accersitum*: 1573 canvas 765, read on the page (Claude, 2026-11-13)
- **18.33** *miseritus* → *misertus*: 1573 OCR mifertus, as 14:14 on the page (Claude, 2026-11-13)
- **21.12** *nummulāriōrum* → *numulariorum*: 1573 canvas 767, read on the page: one m and no bar, as numis 27:5–6 (Claude, 2026-11-13)
- **23.3** *exsequiminī* → *exequimini*: 1573 canvas 769, read on the page: exe-quimini (Claude, 2026-11-13)
- ⚑ **23.6** *accubitiōnēs* → *accubationes*: 1573 canvas 769, read on the page (Claude, 2026-11-13)
- **23.15** *adventīcium* → *aduentitium*: 1573 canvas 769, read on the page: aduenti-tium (Claude, 2026-11-13)
- **23.23** *decimātis* → *decumatis*: 1573 canvas 769, read on the page (Claude, 2026-11-13)
- **23.24** *dēgluttītis* → *deglutitis*: 1573 OCR deglutitis (Claude, 2026-11-13)
- **24.31** *nūntiōs* → *nuncios*: 1573 canvas 770, read on the page: nũcios (Claude, 2026-11-13)
- ⚑ **24.38** *Nōa* → *Noe*: 1573 canvas 770, read on the page (Claude, 2026-11-13)
- **25.41** *exsecrābilēs* → *execrabiles*: 1573 canvas 771, read on the page: execrabi-les (Claude, 2026-11-13)
- **27.29** *dextram* → *dexteram*: 1573 canvas 773, read on the page (Claude, 2026-11-13)
- ⚑ **27.29** *congenuclantēs* → *congenulantes*: 1573 canvas 773, read on the page (Claude, 2026-11-13)
- ⚑ **3.4** *pelliciō* → *pelliceo*: 1573 canvas 751, read on the page (read by Claude, 2026-11-13)
- **4.1** *temptārētur* → *tentaretur*: 1573 canvas 751, read on the page: vt tentaretur (read by Claude, 2026-11-13)
- **4.3** *temptātor* → *tentator*: 1573 canvas 751, read on the page: printed tẽtator (read by Claude, 2026-11-13)
- **26.25** *Isne* → *Is'ne*: 1573 canvas 772, read on the page (read by Claude, 2026-11-13)
- **26.62** *Nihilne* → *Nihil'ne*: 1573 canvas 772, read on the page (read by Claude, 2026-11-13)
- **26.53** *plūs* → *plusquam*: 1573 canvas 772, read on the page: plusq̃, one word (read by Claude, 2026-11-13)
- **26.53** *quam* → *+*: 1573 canvas 772: joined to plus (plusq̃) (read by Claude, 2026-11-13)
- **25.31** *nec* → *necnon*: 1573 canvas 771, read on the page: one word (read by Claude, 2026-11-13)
- **25.31** *nōn* → *+*: 1573 canvas 771: joined to nec (necnon) (read by Claude, 2026-11-13)
- **24.30** *cælō* → *cœlo*: 1573 canvas 770, read on the page: œ (read by Claude, 2026-11-13)
- **6.32** *cælestis* → *cœlestis*: 1573 canvas 754, read on the page: œ (read by Claude, 2026-11-13)
- **11.11** *cælestī* → *cœlesti*: 1573 canvas 759, read on the page: œ (read by Claude, 2026-11-13)
- **15.13** *cælestis* → *cœlestis*: 1573 canvas 763, read on the page: œ (read by Claude, 2026-11-13)
- **7.21** *cælīs* → *cœlis*: 1573 canvas 755, read on the page: œ (read by Claude, 2026-11-13)
- **6.14** *cælestis* → *cœlestis*: 1573 canvas 754, read on the page: œ (read by Claude, 2026-11-13)
- **13.31** *cæleste* → *cœleste*: 1573 canvas 761, read on the page: œ (read by Claude, 2026-11-13)
- **26.32** *præcēdam* → *præcedam*: 1573 canvas 772, read on the page: ę (read by Claude, 2026-11-13)
- **28.20** *præcēpī* → *præcepi*: 1573 canvas 774, read on the page: ę (read by Claude, 2026-11-13)
- **24.37** *Nōæ* → *Noe*: 1573 canvas 770, read on the page: plain e (read by Claude, 2026-11-13)
- **4.7** *temptātō* → *tentato*: 1573 canvas 751, read on the page: line break ten-tato (read by Claude, 2026-11-13)
- **10.14** *audierit* → *audiuerit*: 1573 canvas 757, read on the page (read by Claude, 2026-11-13)
- **20.30** *audiērunt* → *audiuerunt*: 1573 canvas 767, read on the page: line break audiue-runt (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (162)

*adulēscēns* → *adolescens*; *condiciō* → *conditio* ×2; *condiciōne* → *conditione*; *condiciōnem* → *conditionem*; *cotīdiē* → *quotidie*; *cōntiōnārētur* → *concionaretur*; *dextra* → *dextera* ×2; *dextram* → *dexteram* ×4; *erum* → *herum*; *erus* → *herus* ×3; *exspectandus* → *expectandus*; *exspectā* → *expecta*; *exspectāret* → *expectaret*; *intellegat* → *intelligat*; *intellegentēs* → *intelligentes*; *intellegit* → *intelligit*; *intellegunt* → *intelligunt*; *intellegātis* → *intelligatis*; *intellegēns* → *intelligens* ×2; *intellegētis* → *intelligetis*; *iīs* → *eis* ×91; *iīsque* → *eisque* ×5; *miseritus* → *misertus*; *obœdiant* → *obediant*; *quattuor* → *quatuor* ×3; *quattuordecim* → *quatuordecim* ×2; *quemquam* → *quenquam*; *quidquam* → *quicquam*; *quidquid* → *quicquid* ×8; *quotiēns* → *quoties* ×2; *quæsīvērunt* → *quæsierunt*; *quīcumque* → *quicunque*; *sepulcra* → *sepulchra*; *sepulcrum* → *sepulchrum* ×3; *sepulcrī* → *sepulchri*; *sepulcrīs* → *sepulchris*; *temptandī* → *tentandi* ×3; *temptātis* → *tentatis*; *temptātiōnem* → *tentationem* ×2; *trīcēsimō* → *trigesimo*; *umerīs* → *humeris*; *āeriæ* → *aereæ* ×2; *āeriās* → *aereas*

## Printer's spellings no rule covers (189)

*adīssent* → *adijssent*; *aliōquī* → *alioquin* ×2; *arta* → *arcta*; *audierit* → *audiuerit* ×2; *audīsse* → *audiuisse*; *audīsset* → *audiuisset*; *audīstis* → *audiuistis* ×6; *barabbam* → *barrabam* ×4; *circumdatīs* → *circundatis*; *coiērunt* → *coiuerunt* ×3; *cupīsse* → *cupijsse*; *cæleste* → *cœleste* ×10; *cælestis* → *cœlestis* ×4; *cælestēs* → *cœlestes*; *cælestī* → *cœlesti* ×4; *cælum* → *cœlum* ×2; *cælī* → *cœli*; *cælīque* → *cœlique*; *cælīs* → *cœlis* ×4; *cælō* → *cœlo* ×6; *cælōne* → *cœlone*; *cārissimus* → *charissimus* ×2; *cēnīs* → *cœnis*; *cēpit* → *cæpit*; *cēterum* → *cæterum* ×2; *cēterī* → *cæteri*; *cōnūbia* → *connubia*; *dumtaxat* → *duntaxat* ×2; *dīnōscere* → *dignoscere*; *ere* → *here*; *exsecūtus* → *executus*; *exsequendum* → *exequendum*; *exsequere* → *exequere*; *exsequitur* → *exequitur*; *exsequī* → *exequi*; *exsistent* → *existent*; *exsistentque* → *existentque*; *exstinguet* → *extinguet*; *exstinguuntur* → *extinguuntur*; *exstirpābitur* → *extirpabitur*; *exstitisse* → *extitisse*; *exstitit* → *extitit* ×3; *exstruitis* → *extruitis*; *exstrūxit* → *extruxit*; *exīstis* → *exijstis* ×2; *fēminam* → *fœminam*; *fēminæ* → *fœminæ*; *fēminārum* → *fœminarum*; *fēminās* → *fœminas* ×2; *hieme* → *hyeme*; *holerum* → *olerum*; *hērēditātem* → *hæreditatem*; *hērēs* → *hæres*; *hūcine* → *huccine*; *iit* → *iuit* ×7; *iitque* → *iuitque*; *inexspectātō* → *inexpectato*; *inexstīnctō* → *inextincto*; *intellegitis* → *intelligitis* ×3; *iērunt* → *iuerunt* ×4; *iī* → *iui*; *jōhannēs* → *iohanes* ×2; *litterās* → *literas*; *litterātōs* → *literatos*; *litterīs* → *literis* ×2; *lītus* → *littus* ×2; *monumenta* → *monimenta*; *monumentīs* → *monimentis* ×2; *monumentō* → *monimento* ×2; *murram* → *myrrham*; *mīlia* → *millia* ×2; *mīlium* → *millium* ×2; *nummīs* → *numis* ×2; *nummōs* → *numos*; *numquam* → *nunquam* ×2; *nūntium* → *nuncium*; *nūntiārunt* → *nunciarunt* ×2; *nūntiātum* → *nunciatum*; *obdormierant* → *obdormiuerant*; *petīvit* → *petijt* ×2; *pittacium* → *pittatium*; *pretium* → *precium* ×2; *pretiōsum* → *preciosum*; *pretiōsī* → *preciosi*; *prōnūntiātum* → *pronunciatum*; *quamcumque* → *quamcunque*; *quamquam* → *quanquam*; *quandōcumque* → *quandocunque* ×2; *quodcumque* → *quodcunque*; *quæcumque* → *quæcunque* ×3; *quæsīsset* → *quæsiuisset*; *quōscumque* → *quoscunque*; *renūntiet* → *renunciet*; *renūntiātum* → *renunciatum* ×3; *silvestre* → *syluestre*; *silvīs* → *syluis*; *sollicitāminī* → *solicitamini*; *sollicitī* → *soliciti* ×3; *sæculō* → *seculo*; *tamquam* → *tanquam* ×2; *tætra* → *tetra* ×2; *tætram* → *tetram*; *tætricī* → *tetrici*; *tætrum* → *tetrum*; *ubicumque* → *vbicunque* ×2; *umquam* → *vnquam* ×2; *vestīstis* → *vestiuistis*; *ēsurīvit* → *esurijt* ×2; *ōtiōsī* → *ociosi*; *ōtiōsōs* → *ociosos* ×2

## e against the settled æ, printed æ (1)

*jūdæōs* → *iudæos*

## ⚑ Other forms of the word (2)

Read in the OCR and taken by the variant rules, but a different form of the word, not only a spelling: the reading edition may want to look again at these.

6.1 *aliōquī* → *alioquin*; 9.17 *aliōquī* → *alioquin*

## Not read in the OCR (177)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Matt.1.1 | Ēnumerātiō | Enumeratio | — |
| Matt.1.4 | Naasson | Naasson | — |
| Matt.1.4 | Salmōnem | Salmonem | — |
| Matt.1.5 | Jessæum | Iessæum | leffæum |
| Matt.1.6 | Jessæus | Iessæus | lessqus |
| Matt.1.7 | Asam | Asam | Afaim |
| Matt.1.9 | Jōthamum | Iothamum | Ioathamum |
| Matt.1.9 | Jōthamus | Iothamus | Ioathamus |
| Matt.1.10 | Jōsīam | Iosiam | — |
| Matt.1.11 | Jechōniam | Iechoniam | lechoniam |
| Matt.1.12 | Jechōniās | Iechonias | lechonias |
| Matt.1.12 | Zorobabēlem | Zorobabelem | Zorobabelein |
| Matt.1.13 | Eliācīmus | Eliacimus | — |
| Matt.1.13 | Azōrem | Azorem | — |
| Matt.1.14 | Achimus | Achimus | Achinus |
| Matt.1.17 | exilium | exilium | — |
| Matt.1.17 | Babylōnicō | Babylonico | — |
| Matt.1.18 | dēspōnsa | desponsa | — |
| Matt.1.24 | conjugem | coniugem | — |
| Matt.2.12 | Hērōdem | Herodem | — |
| Matt.2.18 | complōrātiōque | comploratioque | — |
| Matt.3.7 | summonuit | summonuit | suminonuit |
| Matt.3.10 | admōta | admota | adınota |
| Matt.3.12 | frūmentumque | frumentumque | fruinentumque |
| Matt.3.16 | columbam | columbam | coluinbam |
| Matt.4.5 | addūcit | Adducit | Tuncadducit |
| Matt.4.9 | adōrāveris | adoraueris | — |
| Matt.4.11 | omittit | Omittit | Tuncomittit |
| Matt.4.24 | afferrentur | afferrentur | — |
| Matt.4.25 | Trānsjordānīnā | Transiordanina | — |
| Matt.5.6 | saturābuntur | saturabuntur | satu |
| Matt.5.17 | perficiam | perficiam | perfician |
| Matt.5.30 | amputā | amputa | amputado |
| Matt.5.34 | jūrandum | iurandum | — |
| Matt.5.36 | possīs | possis | — |
| Matt.5.39 | impēgerit | impegerit | — |
| Matt.6.1 | exerceātis | exerceatis | exercearis |
| Matt.6.12 | remittimus | remittimus | — |
| Matt.6.16 | abstulisse | abstulisse | — |
| Matt.6.24 | contemnet | contemnet | — |
| Matt.6.26 | metant | metant | — |
| Matt.6.26 | præstantiōrēs | præstantiores | præ |
| Matt.7.2 | remētiētur | remetietur | — |
| Matt.7.5 | exime | exime | exine |
| Matt.7.6 | versī | versi | — |
| Matt.7.6 | lacerent | lacerent | — |
| Matt.7.7 | pulsāte | pulsate | — |
| Matt.7.14 | angusta | angusta | anguita |
| Matt.7.15 | lupī | lupi | — |
| Matt.7.19 | excīditur | exciditur | — |
| Matt.7.23 | maleficī | malefici | — |
| Matt.7.24 | rūpem | rupem | rupein |
| Matt.7.27 | ruīnam | ruinam | ruinain |
| Matt.7.28 | stupēbat | stupebat | — |
| Matt.8.1 | Dēgressum | Degressum | — |
| Matt.8.6 | graviterque | grauiterque | — |
| Matt.8.13 | reversusque | reuersusque | reuerfusć |
| Matt.8.13 | valentem | valentem | valentein |
| Matt.8.16 | affectōs | affectos | — |
| Matt.9.14 | jejūnēmus | ieiunemus | — |
| Matt.9.16 | supplēmentum | supplementum | — |
| Matt.9.16 | ruptūra | ruptura | — |
| Matt.9.18 | magistrātū | magistratu | — |
| Matt.9.30 | Comminātus | Comminatus | Comininatus |
| Matt.9.36 | carentēs | carentes | — |
| Matt.10.1 | sānārent | sanarent | — |
| Matt.10.8 | suscitāte | suscitate | — |
| Matt.10.9 | crumēnīs | crumenis | — |
| Matt.10.10 | alimentō | alimento | — |
| Matt.10.14 | admīserit | admiserit | — |
| Matt.10.15 | Sodomītānōrum | Sodomitanorum | — |
| Matt.10.16 | lupōs | lupos | — |
| Matt.10.16 | columbæ | columbæ | — |
| Matt.10.17 | concilia | concilia | — |
| Matt.10.32 | agnōscam | agnoscam | agnoscain |
| Matt.11.16 | comparābō | comparabo | coinparabo |
| Matt.11.20 | redīssent | redissent | — |
| Matt.11.21 | corrēxissent | correxissent | — |
| Matt.11.29 | jugum | iugum | iuguin |
| Matt.11.30 | leve | leue | — |
| Matt.12.11 | dēcīderit | deciderit | — |
| Matt.12.12 | ovī | oui | qui |
| Matt.12.18 | dōnābō | donabo | — |
| Matt.12.23 | dictitāre | dictitare | — |
| Matt.13.5 | carērent | carerent | — |
| Matt.13.6 | āruērunt | aruerunt | a |
| Matt.13.19 | rapit | rapit | — |
| Matt.13.33 | farīnæ | farinæ | — |
| Matt.13.47 | ēverriculō | euerriculo | — |
| Matt.13.48 | replētum | repletum | repletuin |
| Matt.13.49 | Prōdībunt | Prodibunt | — |
| Matt.13.55 | Jōsēs | Ioses | — |
| Matt.14.11 | allātumque | allatumque | II |
| Matt.14.19 | jussā | iussa | — |
| Matt.14.19 | grāmina | gramina | — |
| Matt.14.24 | vexābātur | vexabatur | — |
| Matt.15.21 | Sīdoniōsque | Sidoniosque | — |
| Matt.15.32 | dēfetīscantur | defetiscantur | — |
| Matt.16.2 | Serēnum | Serenum | — |
| Matt.16.3 | temporum | temporum | teinporum |
| Matt.16.6 | Saddūcæōrumque | Sadducæorumque | Sadduczorumque |
| Matt.17.1 | arduum | arduum | arduuin |
| Matt.17.3 | colloquentēs | colloquentes | — |
| Matt.17.5 | obumbrāvit | obumbrauit | — |
| Matt.17.22 | Versantibus | Versantibus | — |
| Matt.17.24 | didrachma | didrachma | didrachina |
| Matt.18.16 | triumve | triumue | — |
| Matt.18.17 | extrāneus | extraneus | — |
| Matt.18.22 | septuāgiēs | septuagies | — |
| Matt.19.9 | repudiāverit | repudiauerit | — |
| Matt.19.9 | adulterāre | adulterare | — |
| Matt.19.18 | Quænam | Quænam | — |
| Matt.19.27 | relīquimus | reliquimus | — |
| Matt.20.18 | damnātum | damnatum | — |
| Matt.20.25 | prīncipēs | principes | — |
| Matt.21.2 | asinam | asinam | afinaım |
| Matt.21.10 | commōta | commota | coinmota |
| Matt.21.12 | sellāsque | sellasque | fellasó |
| Matt.21.16 | condis | condis | — |
| Matt.21.19 | quādam | quadam | quadain |
| Matt.21.22 | obtinēbitis | obtinebitis | obti |
| Matt.21.32 | mūtāstis | mutastis | — |
| Matt.21.33 | turrim | turrim | turrin |
| Matt.21.33 | ēlocāvit | elocauit | — |
| Matt.21.45 | exemplīs | exemplis | — |
| Matt.22.34 | Saddūcæōs | Sadducæos | — |
| Matt.23.5 | spectentur | spectentur | spectenturab |
| Matt.23.10 | rēctor | rector | — |
| Matt.23.15 | digniōrem | digniorem | digniorern |
| Matt.23.21 | incolam | incolam | — |
| Matt.23.25 | intemperantiāque | intemperantiaque | intemperantias |
| Matt.23.26 | Pharisæe | Pharisæe | Phariffe |
| Matt.23.30 | fuissēmus | fuissemus | — |
| Matt.23.31 | posterōs | posteros | — |
| Matt.23.33 | poteritisne | poteritisne | — |
| Matt.23.33 | gehennæ | gehennæ | — |
| Matt.23.34 | tollētis | tolletis | — |
| Matt.23.38 | relictum | relictum | — |
| Matt.24.2 | lapide | lapide | dem |
| Matt.24.5 | Chrīstōs | Christos | — |
| Matt.24.9 | occīdēminī | occidemini | — |
| Matt.24.29 | ēmittet | emittet | — |
| Matt.24.29 | concutientur | concutientur | — |
| Matt.24.30 | vidēbuntque | videbuntque | — |
| Matt.24.34 | ætātem | ætatem | ætatein |
| Matt.24.38 | comedēbātur | comedebatur | — |
| Matt.24.38 | mātrimōnia | matrimonia | — |
| Matt.24.47 | præpōnet | præponet | præ ponet |
| Matt.24.51 | dissecābit | dissecabit | — |
| Matt.24.51 | simulātōrum | simulatorum | — |
| Matt.24.51 | rediget | rediget | — |
| Matt.25.3 | sūmpsēre | sumpsere | — |
| Matt.25.5 | dormiēruntque | dormieruntque | — |
| Matt.25.8 | Impertīte | Impertite | Impertice |
| Matt.25.9 | emite | emite | — |
| Matt.25.21 | præficiam | præficiam | — |
| Matt.25.43 | ægrum | ægrum | — |
| Matt.25.44 | ægrum | ægrum | egru |
| Matt.26.1 | Posteāquam | Posteaquam | — |
| Matt.26.4 | interficiendō | interficiendo | — |
| Matt.26.9 | vēnīre | venire | — |
| Matt.26.16 | prōdendī | prodendi | — |
| Matt.26.17 | epulandum | epulandum | — |
| Matt.26.31 | dēserētis | deseretis | — |
| Matt.26.57 | Caiāpham | Caiapham | — |
| Matt.26.67 | impingere | impingere | — |
| Matt.26.69 | Galilæō | Galilæo | Cralilæo |
| Matt.27.25 | nostrīque | nostrique | noftrig |
| Matt.27.32 | Cȳrēnæum | Cyrenæum | — |
| Matt.27.40 | īnstaurās | instauras | — |
| Matt.27.53 | appāruērunt | apparuerunt | appa |
| Matt.27.54 | cōnfessī | confessi | confeisi |
| Matt.27.64 | dīcantque | dicantque | — |
| Matt.28.8 | cucurrērunt | cucurrerunt | — |
| Matt.28.10 | abeant | abeant | — |
| Matt.28.15 | ēdoctī | edocti | — |
| Matt.28.19 | baptīzāte | baptizate | — |

## Punctuation not from the OCR (95)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.9 *Iothamum.*; 1.10 *Iosiam.*; 1.13 *Azorem.*; 1.24 *coniugem,*; 2.1 *Hierosolymam,*; 3.2 *regnum.*; 4.6 *enim:*; 4.21 *vocauit.*; 4.22 *eum.*; 4.25 *Transiordanina.*; 5.6 *saturabuntur.*; 5.10 *regnum.*; 5.12 *vestros.*; 5.19 *cœlesti.*; 5.24 *tuum.*; 5.28 *aspicit,*; 6.16 *confirmo,*; 7.2 *remetietur.*; 7.15 *lupi.*; 7.22 *fecimus?*; 7.23 *malefici.*; 7.29 *scribæ.*; 9.1 *venit.*; 9.8 *dedisset.*; 9.15 *ieiunabunt.*; 9.16 *vestis,*; 9.16 *fieret.*; 9.36 *oues.*; 10.1 *sanarent.*; 10.13 *salus.*; 10.14 *admiserit,*; 10.23 *Hominis.*; 10.28 *perdere.*; 10.38 *dignus.*; 11.9 *vatem.*; 11.21 *correxissent.*; 11.23 *diem.*; 13.5 *carerent.*; 13.6 *aruerunt.*; 13.49 *fine.*; 13.57 *est,*; 14.12 *iuerunt.*; 14.14 *eorum.*; 14.17 *pisces.*; 15.3 *facitis?*; 16.2 *dicitis:*; 16.15 *dicitis?*; 17.3 *colloquentes.*; 17.7 *metuite.*; 18.2 *eos,*; 18.3 *regnum.*; 18.18 *fore.*; 18.21 *debeo?*; 18.22 *septies.*; 19.23 *vobis,*; 19.23 *inquit,*; 20.31 *Dauidide.*; 20.34 *oculos,*; 21.10 *Hierosolyma,*; 21.11 *Galilææ.*; 21.13 *latronum.*; 21.16 *condis.*; 21.19 *aruit.*; 21.20 *ficus?*; 21.22 *obtinebitis.*; 21.25 *erat?*; 23.1 *est:*; 23.16 *teneri.*; 23.21 *incolam.*; 23.39 *Domini.*; 24.9 *occidemini,*; 24.9 *meum.*; 24.12 *charitas.*; 24.29 *concutientur.*; 24.32 *æstatem.*; 24.51 *dissecabit,*; 24.51 *dentium.*; 25.3 *oleum;*; 25.9 *emite.*; 25.28 *decem.*; 26.4 *interficiendo.*; 26.16 *prodendi.*; 26.25 *Rabbi?*; 26.30 *Oliuarum.*; 26.57 *conuenerant.*; 26.64 *dexteram,*; 26.65 *testibus?*; 26.68 *percussit.*; 26.70 *diceret.*; 27.11 *dicis,*; 27.35 *iecerunt.*; 27.53 *apparuerunt.*; 28.5 *metuite,*; 28.8 *cucurrerunt.*; 28.20 *seculi.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. Found here: 8.18 *difcipulos*; 19.4 *hominem*.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
