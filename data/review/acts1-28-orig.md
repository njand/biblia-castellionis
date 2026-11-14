# Acts 1–28 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Acts 1-28` → `text/orig/draft/ACT.usfm` (now `text/orig/ACT.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Acts.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/ACT.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 14208 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 135 | read in the OCR, a spelling the approved rules normalize |
| variant | 158 | read in the OCR, a printer's spelling no rule covers |
| ę | 22 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 189 | read in the OCR with a nasal bar (m or n put back) |
| misread | 28 | the settled word misread by the OCR; spelling as settled |
| lexicon | 1190 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 41 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 59 | OCR unreadable; the settled word in the printer's conventions |
| none | 243 | no OCR word; the settled word in the printer's conventions |
| all | 16273 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **1.26** *Matthiam* → *Mathiam*: 1573 canvas 833, read on the page: printed Mathiã, with one t (read by Claude, 2026-11-13)
- ⚑ **2.24** *lētī* → *lethi*: 1573 canvas 833, read on the page: with h (read by Claude, 2026-11-13)
- **3.18** *prænūntiāverat* → *prænunciauerat*: 1573 canvas 835, read on the page: printed pręnuncia-uerat (read by Claude, 2026-11-13)
- **5.2** *pretiī* → *precij*: 1573 canvas 836, read on the page: with c and j (read by Claude, 2026-11-13)
- **5.9** *temptandum* → *tentandum*: 1573 canvas 836, read on the page: line break: ten-tandum (read by Claude, 2026-11-13)
- **5.23** *renūntiārunt* → *renunciarunt*: 1573 canvas 836, read on the page: printed renũciarũt (read by Claude, 2026-11-13)
- **7.52** *prænūntiārunt* → *prænunciarunt*: 1573 canvas 838, read on the page: line break: prænun-ciarunt (read by Claude, 2026-11-13)
- **8.30** *Intellegisne* → *Intelligis'ne*: 1573 canvas 839, read on the page (read by Claude, 2026-11-13)
- **11.12** *Īvērunt* → *Iuerunt*: 1573 canvas 841, read on the page: capital I (read by Claude, 2026-11-13)
- **12.23** *exspīrāvit* → *expirauit*: 1573 canvas 842, read on the page: line break: ex-pirauit (read by Claude, 2026-11-13)
- **14.27** *renūntiārunt* → *renunciarunt*: 1573 canvas 844, read on the page: line break: renun-ciarunt (read by Claude, 2026-11-13)
- **15.25** *cārissimīs* → *charissimis*: 1573 canvas 844, read on the page: with h (read by Claude, 2026-11-13)
- ✱ **16.15** *dīverterēmur* → *diuerteremus*: 1573 canvas 845, read on the page: a misprint, printed as is (read by Claude, 2026-11-13)
- **17.18** *nūntiātōrem* → *nunciatorem*: 1573 canvas 846, read on the page: line break: nun-ciatorem (read by Claude, 2026-11-13)
- **19.13** *Temptārunt* → *Tentarunt*: 1573 canvas 847, read on the page: with no p (read by Claude, 2026-11-13)
- **23.19** *nūntiandum* → *nunciandum*: 1573 canvas 851, read on the page: line break: nuncian-dum; printed with c (read by Claude, 2026-11-13)
- ⚑ **25.9** *grātificāre* → *gratificari*: 1573 canvas 852, read on the page: printed "Iudæis gratificari"; differs from proposed gratificare (read by Claude, 2026-11-13)
- **2.5** *cælō* → *cœlo*: 1573 canvas 833, read on the page: œ (read by Claude, 2026-11-13)
- **26.19** *cælestī* → *cœlesti*: 1573 canvas 853, read on the page: œ (read by Claude, 2026-11-13)
- **25.16** *præsentēs* → *præsentes*: 1573 canvas 852, read on the page: ę (read by Claude, 2026-11-13)
- **26.6** *repræsentātiōnis* → *repræsentationis*: 1573 canvas 852, read on the page: ę (read by Claude, 2026-11-13)
- ⚑ **4.1** *Iīs* → *Eis*: 1573 canvas 835, read on the page: drop cap E + Is (read by Claude, 2026-11-13)
- **4.4** *audierant* → *audiuerant*: 1573 canvas 835, read on the page: line break audiue-rant (read by Claude, 2026-11-13)
- ⚑ **4.14** *iīs* → *eis*: 1573 canvas 835, read on the page (read by Claude, 2026-11-13)
- ⚑ **4.17** *iīs* → *eis*: 1573 canvas 835, read on the page (read by Claude, 2026-11-13)
- ⚑ **5.24** *iīs* → *eis*: 1573 canvas 836, read on the page (read by Claude, 2026-11-13)
- ⚑ **5.25** *iīs* → *eis*: 1573 canvas 836, read on the page (read by Claude, 2026-11-13)
- **5.31** *dextrā* → *dextra*: 1573 canvas 836, read on the page (read by Claude, 2026-11-13)
- **11.1** *Audiērunt* → *Audiuerunt*: 1573 canvas 841, read on the page: drop cap A + Vdiuerunt (read by Claude, 2026-11-13)
- **11.15** *Sānctus* → *sanctus*: 1573 canvas 841, read on the page: lower case; san-ctus (read by Claude, 2026-11-13)
- ⚑ **13.8** *iīs* → *eis*: 1573 canvas 842, read on the page (read by Claude, 2026-11-13)
- ⚑ **14.15** *iīs* → *eis*: 1573 canvas 844, read on the page (read by Claude, 2026-11-13)
- ⚑ **15.8** *iīs* → *eis*: 1573 canvas 844, read on the page: both places (read by Claude, 2026-11-13)
- ⚑ **15.38** *iīs* → *eis*: 1573 canvas 845, read on the page (read by Claude, 2026-11-13)
- **15.38** *negōtium* → *negocium*: 1573 canvas 845, read on the page (read by Claude, 2026-11-13)
- ⚑ **16.20** *iīs* → *eis*: 1573 canvas 845, read on the page (read by Claude, 2026-11-13)
- ⚑ **19.12** *iīs* → *eis*: 1573 canvas 847, read on the page (read by Claude, 2026-11-13)
- ⚑ **21.1** *iīs* → *eis*: 1573 canvas 849, read on the page (read by Claude, 2026-11-13)
- **25.14** *negōtium* → *negotium*: 1573 canvas 852, read on the page (read by Claude, 2026-11-13)
- **28.22** *Cēterum* → *Cæterum*: 1573 canvas 854, read on the page: æ (read by Claude, 2026-11-13)
- **9.33** *Ænēam* → *Æneam*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (135)

*adulēscentem* → *adolescentem* ×3; *adulēscentis* → *adolescentis*; *adulēscentēs* → *adolescentes*; *auctor* → *autor*; *cotīdiānō* → *quotidiano*; *cotīdiē* → *quotidie* ×8; *cum* → *quum*; *cōntiōne* → *concione* ×2; *cōntiōnem* → *concionem*; *dextram* → *dexteram* ×2; *dextrā* → *dextera* ×2; *epistulam* → *epistolam*; *epistulā* → *epistola*; *epistulās* → *epistolas* ×2; *exspectant* → *expectant* ×2; *exspectantibus* → *expectantibus*; *exspectantēs* → *expectantes*; *exspectārent* → *expectarent*; *exspectātiōne* → *expectatione*; *intellegant* → *intelligant*; *intellegantque* → *intelligantque*; *intellegere* → *intelligere* ×2; *intellegeret* → *intelligeret*; *intellegēbat* → *intelligebat*; *intellegēns* → *intelligens* ×2; *intellegētis* → *intelligetis*; *iīs* → *eis* ×67; *iīsque* → *eisque* ×5; *obœdiēbat* → *obediebat*; *obœdiētis* → *obedietis*; *paullō* → *paulo*; *petīvērunt* → *petierunt*; *quattuor* → *quatuor* ×6; *quidquam* → *quicquam* ×3; *quīcumque* → *quicunque* ×4; *sepulcrētō* → *sepulchreto*; *subolī* → *soboli*; *āeriæ* → *aereæ*; *āeriās* → *aereas*

## Printer's spellings no rule covers (158)

*adversus* → *aduerssus*; *aliquamdiū* → *aliquandiu* ×5; *ancorās* → *anchoras*; *ancorīs* → *anchoris*; *arcesse* → *accerse*; *arcessendam* → *accersendam*; *arcesserent* → *accerserent*; *arcesseret* → *accerseret* ×2; *arcessēns* → *accersens*; *arcessītum* → *accersitum* ×2; *arcessītus* → *accersitus*; *arcessītōs* → *accersitos*; *arcessīverītis* → *accersiueritis*; *auctor* → *author*; *auctōrem* → *authorem*; *audierant* → *audiuerant*; *audierint* → *audiuerint*; *audieris* → *audiueris*; *audiērunt* → *audiuerunt* ×4; *audīsse* → *audiuisse*; *audīstis* → *audiuistis*; *circumcīdendōs* → *circuncidendos*; *circumdatus* → *circundatus*; *circumstetērunt* → *circunsteterunt*; *commendātum* → *comendatum*; *commōvēruntque* → *comoueruntque*; *cuicumque* → *cuicunque*; *cælestium* → *cœlestium*; *cælum* → *cœlum* ×3; *cælō* → *cœlo* ×7; *cælōs* → *cœlos*; *cēterum* → *cæterum*; *cēterās* → *cæteras*; *cēterī* → *cæteri* ×3; *cēterīs* → *cæteris*; *cēterō* → *cætero*; *cēterōrum* → *cæterorum*; *cēterōs* → *cæteros*; *cœpisset* → *cepisset*; *dēnūntiat* → *denunciat*; *dēnūntiāmus* → *denunciamus*; *dēnūntiārem* → *denunciarem*; *dēnūntiārunt* → *denunciarunt*; *dēnūntiāvērunt* → *denunciauerunt*; *exscēnsū* → *excensu*; *exsiliēns* → *exiliens*; *exsilīre* → *exilire*; *exsistant* → *existant*; *exstat* → *extat*; *exstimulābātur* → *extimulabatur*; *exstitissent* → *extitissent*; *exstitit* → *extitit* ×10; *exstititque* → *extititque*; *exsultō* → *exulto*; *fēminæ* → *fœminæ*; *fēminārum* → *fœminarum* ×2; *fēminās* → *fœminas* ×3; *fēminīs* → *fœminis* ×3; *fētū* → *fætu*; *gāius* → *caius*; *gāiō* → *caio*; *hiemāverat* → *hyemauerat*; *hērēditāte* → *hæreditate*; *hīberna* → *hyberna*; *hībernāre* → *hybernare*; *illitterātōs* → *illiteratos*; *imperītōs* → *iinperitos*; *jācōbæōrum* → *iacobeorum*; *jōhannēs* → *iohanes*; *lacrimīs* → *lachrymis*; *litteræ* → *literæ*; *litterās* → *literas* ×4; *litterīs* → *literis* ×2; *lītus* → *littus* ×2; *matthiam* → *mathiam*; *monumentum* → *monimentum*; *monumentō* → *monimento*; *negōtium* → *negocium* ×2; *numquam* → *nunquam*; *numquid* → *nunquid*; *numquis* → *nunquis*; *nūntiant* → *nunciant*; *nūntiantēs* → *nunciantes*; *nūntiābat* → *nunciabat*; *nūntiāmus* → *nunciamus*; *nūntiāns* → *nuncians*; *nūntiāre* → *nunciare*; *nūntiārent* → *nunciarent*; *nūntiāret* → *nunciaret*; *nūntiārī* → *nunciari*; *nūntiātum* → *nunciatum*; *nūntiātūrum* → *nunciaturum*; *nūntiāverit* → *nunciauerit*; *nūntiāvit* → *nunciauit* ×2; *nūntiīs* → *nuncijs*; *nūntiō* → *nuncio*; *obœdierit* → *obediuerit*; *opperītur* → *operitur*; *petīvit* → *petijt*; *pretia* → *precia*; *pretiō* → *precio* ×3; *prænūntiātum* → *prænunciatum*; *prōnūntiāvit* → *pronunciauit*; *quæcumque* → *quæcunque* ×2; *renūntiārent* → *renunciarent*; *renūntiāvit* → *renunciauit*; *spatiō* → *spacio*; *succurrendum* → *succurendum*; *sæculīs* → *seculis* ×2; *sēsē* → *ssese*; *tamquam* → *tanquam*; *tharsum* → *tarsum*; *umquam* → *vnquam* ×2

## e against the settled æ, printed æ (3)

*cælum* → *cœlum*; *jūdæus* → *iudæus*; *jūdæōrum* → *iudæorum*

## Not read in the OCR (330)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Acts.1.13 | Bartholomæus | Bartholomæus | Bartholemeus |
| Acts.1.18 | suspēnsus | suspensus | — |
| Acts.1.18 | medius | medius | medis |
| Acts.2.1 | quīnquāgēsimæ | quinquagesimæ | — |
| Acts.2.2 | vehementis | vehementis | — |
| Acts.2.9 | Jūdææque | Iudææque | Iu dææque |
| Acts.2.17 | perfundam | perfundam | — |
| Acts.2.17 | somniābunt | somniabunt | soinniabunt |
| Acts.2.21 | ēvādet | euadet | — |
| Acts.2.23 | alligātum | alligatum | alligatuın |
| Acts.2.38 | assequiminī | assequimini | — |
| Acts.2.39 | remōtiōrēs | remotiores | — |
| Acts.2.39 | advocāverit | aduocauerit | — |
| Acts.2.40 | plūribus | pluribus | — |
| Acts.2.40 | commonuit | commonuit | — |
| Acts.2.40 | perversō | peruerso | — |
| Acts.2.41 | avidē | auide | — |
| Acts.2.41 | admissā | admissa | — |
| Acts.2.46 | mānsiōnātim | mansionatim | — |
| Acts.3.1 | Ascendēbant | Ascendebant | — |
| Acts.3.5 | acceptūrum | accepturum | — |
| Acts.3.9 | laudantem | laudantem | — |
| Acts.3.10 | admīrātiōne | admiratione | admisatione |
| Acts.3.10 | stupōre | Stupore | Itupore |
| Acts.3.22 | cōnsanguinitāte | consanguinitate | — |
| Acts.4.10 | astāre | astare | — |
| Acts.4.17 | minēmur | minemur | mine |
| Acts.4.18 | mitterent | mitterent | initterent |
| Acts.4.21 | interminātī | interminati | interininati |
| Acts.4.23 | dīmīsī | dimisi | diinissi |
| Acts.4.25 | tumultuantur | tumultuantur | — |
| Acts.4.26 | cœuntque | cœuntque | coeutitás |
| Acts.4.31 | dīvīnumque | diuinumque | — |
| Acts.4.32 | ūnusque | vnusque | — |
| Acts.4.34 | vēnditōrum | venditorum | — |
| Acts.4.36 | Jōsēs | Ioses | — |
| Acts.4.36 | Cyprius | Cyprius | Cypris |
| Acts.5.1 | Sapphīrā | Sapphira | — |
| Acts.5.1 | conjuge | coniuge | — |
| Acts.5.1 | vēndidit | vendidit | — |
| Acts.5.2 | dētractā | detracta | — |
| Acts.5.2 | cōnsciā | conscia | — |
| Acts.5.2 | dēposuit | deposuit | — |
| Acts.5.3 | Ananīā | Anania | — |
| Acts.5.3 | implēvit | impleuit | — |
| Acts.5.3 | mentīrēris | mentireris | — |
| Acts.5.3 | prædiī | prædii | — |
| Acts.5.3 | dētraherēs | detraheres | — |
| Acts.5.4 | manēbat | manebat | — |
| Acts.5.10 | extulērunt | extulerunt | — |
| Acts.5.13 | adjungere | adiungere | — |
| Acts.5.14 | magisque | magisque | imagisque |
| Acts.5.15 | umbra | vmbra | — |
| Acts.5.16 | immundīs | immundis | iminundis |
| Acts.5.20 | ēloquiminī | eloquimini | eloquinini |
| Acts.5.23 | dīligentissimē | diligentissime | — |
| Acts.5.23 | clausum | clausum | — |
| Acts.5.23 | comperiisse | comperiisse | — |
| Acts.5.23 | astantēs | astantes | — |
| Acts.5.23 | aperuissent | aperuissent | — |
| Acts.5.24 | summus | summus | — |
| Acts.5.24 | antistes | antistes | — |
| Acts.5.24 | ambigēbant | ambigebant | — |
| Acts.5.25 | dedissent | dedissent | — |
| Acts.5.26 | antistes | antistes | — |
| Acts.5.26 | addūxit | adduxit | — |
| Acts.5.26 | lapidārentur | lapidarentur | — |
| Acts.5.27 | adductōs | adductos | — |
| Acts.5.28 | vetuimus | vetuimus | — |
| Acts.5.28 | replēvistis | repleuistis | — |
| Acts.5.28 | dērīvāre | deriuare | — |
| Acts.5.29 | Pārendum | Parendum | — |
| Acts.5.30 | suspēnsum | suspensum | — |
| Acts.5.30 | interfēcistis | interfecistis | — |
| Acts.5.31 | ductōrem | ductorem | — |
| Acts.5.31 | Servātōremque | Seruatoremque | — |
| Acts.5.31 | conciliandum | conciliandum | — |
| Acts.5.31 | peccātōrumque | peccatorumque | — |
| Acts.5.32 | hārum | harum | — |
| Acts.5.32 | Sānctusque | Sanctusque | — |
| Acts.5.34 | ēdūcī | educi | — |
| Acts.5.36 | redāctī | redacti | — |
| Acts.5.39 | obtemperārunt | obtemperarunt | — |
| Acts.5.41 | ignōminiā | ignominia | igno |
| Acts.6.2 | placet | placet | platet |
| Acts.6.5 | Tīmōnem | Timonem | Timonein |
| Acts.6.5 | Parmenam | Parmenam | Parmenaim |
| Acts.6.7 | ingēnsque | ingensque | ingensés |
| Acts.6.9 | Lībertīnōrum | Libertinorum | Libertinoruin |
| Acts.6.12 | correptumque | correptumque | correptuinque |
| Acts.7.3 | ostēnsūrus | ostensurus | ottenfurus |
| Acts.7.4 | mortuō | mortuo | nortuo |
| Acts.7.7 | exībuntque | exibuntque | — |
| Acts.7.10 | Pharaōnem | Pharaonem | Pharaonein |
| Acts.7.15 | obiisset | obiisset | — |
| Acts.7.16 | Emōris | Emoris | — |
| Acts.7.16 | Sichemī | Sichemi | — |
| Acts.7.24 | ultus | vltus | vitus |
| Acts.7.34 | gemitum | gemitum | gemituin |
| Acts.7.36 | mīraque | miraque | miras |
| Acts.7.45 | Jōsuā | Iosua | losua |
| Acts.7.46 | invenīre | inuenire | — |
| Acts.7.48 | Suprēmus | Supremus | — |
| Acts.7.51 | Dūrī | Duri | — |
| Acts.7.51 | cervīce | ceruice | — |
| Acts.7.52 | interfectōrēs | interfectores | inter |
| Acts.7.53 | servāstis | seruastis | — |
| Acts.8.1 | Samarīæque | Samariæque | Samariços |
| Acts.8.10 | summīque | summique | suiminiqs |
| Acts.8.11 | præstīgiīs | præstigiis | — |
| Acts.8.11 | obstupefēcerat | obstupefecerat | — |
| Acts.8.20 | exīstimēs | existimes | exittimes |
| Acts.8.23 | ingeniō | ingenio | — |
| Acts.8.23 | contumācī | contumaci | — |
| Acts.8.23 | amārō | amaro | — |
| Acts.8.23 | felle | felle | — |
| Acts.8.23 | præditum | præditum | — |
| Acts.8.27 | Æthiops | Æthiops | — |
| Acts.8.27 | rēgīnæ | reginæ | — |
| Acts.8.29 | currum | currum | curfum |
| Acts.8.32 | ovis | ouis | — |
| Acts.8.32 | tōnsōrem | tonsorem | — |
| Acts.9.3 | Damascō | Damasco | Danasco |
| Acts.9.3 | propinquantem | propinquantem | propinquantein |
| Acts.9.11 | Saulum | Saulum | Sauluin |
| Acts.9.18 | squāmīs | squamis | — |
| Acts.9.31 | Samarīam | Samariam | Samariain |
| Acts.9.32 | dēscenderet | descenderet | — |
| Acts.9.35 | Lyddæ | Lyddæ | Lydd |
| Acts.10.17 | vestibulō | vestibulo | — |
| Acts.10.21 | adestis | adestis | — |
| Acts.10.30 | supplicābam | supplicabam | — |
| Acts.10.33 | vēneris | veneris | — |
| Acts.11.17 | adjūnximus | adiunximus | — |
| Acts.11.21 | converteret | conuerteret | con |
| Acts.11.22 | Hierosolymītāna | Hierosolymitana | — |
| Acts.12.20 | cubiculāriō | cubiculario | — |
| Acts.12.24 | amplificābātur | amplificabatur | amplificabat |
| Acts.13.2 | sēgregārent | segregarent | — |
| Acts.13.5 | Salamīnem | Salaminem | — |
| Acts.13.8 | āvertere | auertere | — |
| Acts.13.16 | reverēminī | reueremini | — |
| Acts.13.19 | Chananæā | Chananæa | Chananæaterra |
| Acts.13.27 | damnātō | damnato | dannato |
| Acts.13.41 | obtorpēscite | obtorpescite | — |
| Acts.13.46 | convertī | conuerti | — |
| Acts.13.50 | impulsīs | impulsis | — |
| Acts.13.50 | religiōsīs | religiosis | — |
| Acts.13.50 | īnsectātiōnem | insectationem | infeetationem |
| Acts.13.52 | complēbantur | complebantur | — |
| Acts.14.1 | Īconiī | Iconii | — |
| Acts.14.13 | vestibulō | vestibulo | vettibulo |
| Acts.14.22 | miseriās | miserias | iniserias |
| Acts.14.23 | suffrāgiīs | suffragiis | — |
| Acts.15.2 | mediocre | mediocre | — |
| Acts.15.2 | ascendendum | ascendendum | — |
| Acts.15.3 | dēductī | deducti | — |
| Acts.15.3 | Phœnīcem | Phœnicem | — |
| Acts.15.3 | Samarīam | Samariam | — |
| Acts.15.3 | obībant | obibant | — |
| Acts.15.3 | conversiōnem | conuersionem | — |
| Acts.15.3 | expōnentēs | exponentes | — |
| Acts.15.3 | afficiēbant | afficiebant | — |
| Acts.15.4 | perventum | peruentum | — |
| Acts.15.5 | circumcīdendōs | circumcidendos | — |
| Acts.15.5 | indīcendumque | indicendumque | — |
| Acts.15.5 | servārent | seruarent | — |
| Acts.15.6 | dispiciendæ | dispiciendæ | — |
| Acts.15.7 | contentiōne | contentione | — |
| Acts.15.7 | ēlēgerit | elegerit | — |
| Acts.15.7 | euangelicam | euangelicam | — |
| Acts.15.8 | cognitor | cognitor | — |
| Acts.15.8 | impertītus | impertitus | — |
| Acts.15.9 | purgāsset | purgasset | — |
| Acts.15.10 | cervīcibus | ceruicibus | — |
| Acts.15.10 | jugum | iugum | — |
| Acts.15.10 | impōnendō | imponendo | — |
| Acts.15.10 | potuimus | potuimus | — |
| Acts.15.12 | Siluit | Siluit | — |
| Acts.15.12 | Paulumque | Paulumque | — |
| Acts.15.12 | narrantēs | narrantes | — |
| Acts.15.12 | dēsignāsset | designasset | — |
| Acts.15.13 | conticuērunt | conticuerunt | — |
| Acts.15.14 | Simeōn | Simeon | — |
| Acts.15.14 | cūrāverit | curauerit | — |
| Acts.15.14 | ascīscendum | asciscendum | — |
| Acts.15.17 | dēnōminātæ | denominatæ | — |
| Acts.15.23 | externārum | externarum | externaruin |
| Acts.15.24 | lēgīque | legique | legińs |
| Acts.15.31 | lēctā | lecta | — |
| Acts.15.31 | cohortātiōne | cohortatione | — |
| Acts.15.31 | gāvīsī | gauisi | — |
| Acts.15.32 | cohortātī | cohortati | — |
| Acts.15.32 | cōnfirmārunt | confirmarunt | — |
| Acts.15.33 | amīcē | amice | — |
| Acts.15.34 | Sīlæ | Silæ | — |
| Acts.15.34 | remanēre | remanere | — |
| Acts.15.35 | morātī | morati | — |
| Acts.15.35 | explicantēs | explicantes | — |
| Acts.15.36 | explānāssent | explanassent | — |
| Acts.15.36 | revīseret | reuiseret | — |
| Acts.15.37 | assūmere | assumere | — |
| Acts.15.37 | Mārcum | Marcum | — |
| Acts.15.38 | cēnsēbat | censebat | — |
| Acts.15.38 | Pamphȳliā | Pamphylia | — |
| Acts.15.38 | dēfēcisset | defecisset | — |
| Acts.15.38 | assūmendum | assumendum | — |
| Acts.15.39 | jūrgium | iurgium | — |
| Acts.15.39 | dirēmptī | dirempti | — |
| Acts.15.39 | Mārcō | Marco | — |
| Acts.15.39 | nāvigārit | nauigarit | — |
| Acts.15.40 | ēlēctō | electo | — |
| Acts.15.40 | Sīlā | Sila | — |
| Acts.15.41 | Syriamque | Syriamque | — |
| Acts.15.41 | Ciliciam | Ciliciam | — |
| Acts.16.9 | hortābātur | hortabatur | — |
| Acts.16.14 | vēnditrīx | venditrix | — |
| Acts.16.14 | Thyatīrārum | Thyatirarum | Thyatyrarum |
| Acts.16.19 | periisse | periisse | — |
| Acts.16.19 | trāxērunt | traxerunt | — |
| Acts.16.29 | tremebundus | tremebundus | — |
| Acts.16.36 | Significārunt | Significarunt | — |
| Acts.17.5 | æmulātiōnem | æmulationem | — |
| Acts.17.5 | Jāsonis | Iasonis | lafonis |
| Acts.17.5 | prōdūcere | producere | — |
| Acts.17.9 | Jāsonis | Iasonis | lafonis |
| Acts.17.9 | satisfactiōne | satisfactione | fatisfactiohe |
| Acts.17.10 | Berrhœam | Berrhœam | — |
| Acts.17.12 | Græcārum | Græcarum | — |
| Acts.17.13 | Berrhœæ | Berrhœæ | Berrææ |
| Acts.17.17 | religiōsīs | religiosis | — |
| Acts.17.18 | Stōicōrumque | Stoicorumque | — |
| Acts.17.19 | Possumusne | Possumusne | — |
| Acts.17.29 | exīstimāre | existimare | — |
| Acts.18.1 | Corinthum | Corinthum | — |
| Acts.18.8 | Crīspus | Crispus | Areopagi |
| Acts.18.8 | Corinthiōrum | Corinthiorum | — |
| Acts.18.10 | lædendī | lædendi | læden di |
| Acts.18.13 | colant | colant | — |
| Acts.18.17 | cūrante | curante | — |
| Acts.18.17 | Galliōne | Gallione | — |
| Acts.18.23 | Galaticum | Galaticum | — |
| Acts.18.25 | baptismum | baptismum | baptifina |
| Acts.18.27 | volente | volente | — |
| Acts.19.6 | vāticinābantur | vaticinabantur | — |
| Acts.19.12 | ægrōtantēs | ægrotantes | — |
| Acts.19.12 | afferrentur | afferrentur | — |
| Acts.19.12 | sūdāria | sudaria | — |
| Acts.19.12 | sēmicīnctia | semicinctia | — |
| Acts.19.12 | līberārentur | liberarentur | — |
| Acts.19.12 | immundī | immundi | — |
| Acts.19.12 | exīrent | exirent | — |
| Acts.19.13 | ambulātōribus | ambulatoribus | — |
| Acts.19.13 | obtestātōribus | obtestatoribus | — |
| Acts.19.13 | nōmināre | nominare | — |
| Acts.19.13 | Obtestāmur | Obtestamur | — |
| Acts.19.13 | prædicat | prædicat | — |
| Acts.19.14 | Scevæ | Sceuæ | — |
| Acts.19.19 | nummōrum | nummorum | — |
| Acts.19.24 | argentārius | argentarius | — |
| Acts.19.24 | argentea | argentea | — |
| Acts.19.24 | quæstum | quæstum | — |
| Acts.19.27 | cōnfūtētur | confutetur | corifutetür |
| Acts.19.35 | Jove | Ioue | loue |
| Acts.19.35 | dīlāpsī | dilapsi | delapli |
| Acts.20.4 | Berrhœēnsis | Berrhœensis | Berreenfis |
| Acts.20.11 | gustātōque | gustatoque | gustatos |
| Acts.20.17 | Mīlētō | Mileto | — |
| Acts.20.17 | arcessendōs | arcessendos | — |
| Acts.20.17 | Ephesō | Epheso | — |
| Acts.20.20 | īnstituerem | instituerem | instituerein |
| Acts.20.21 | corrēctīs | correctis | corretis |
| Acts.20.36 | supplicāvit | supplicauit | — |
| Acts.21.5 | supplicāvimus | supplicauimus | fupplicauinus |
| Acts.21.7 | Ptolemāidem | Ptolemaidem | Ptolemaiden |
| Acts.21.11 | colligātīs | colligatis | — |
| Acts.21.31 | cōnfūsam | confusam | confusain |
| Acts.21.37 | Græcē | Græce | Græcès |
| Acts.22.4 | īnsectātus | insectatus | — |
| Acts.22.5 | accēperam | acceperam | acceperain |
| Acts.22.25 | indemnātum | indemnatum | indeinnatum |
| Acts.22.25 | verberāre | verberare | — |
| Acts.23.1 | optimē | optime | optiune |
| Acts.23.4 | convīciāris | conuiciaris | — |
| Acts.23.5 | maledīcitō | maledicito | — |
| Acts.23.8 | utrumque | vtrumque | — |
| Acts.23.8 | cōnfitentur | confitentur | — |
| Acts.23.10 | abreptum | abreptum | abreptuin |
| Acts.23.23 | proficīscantur | proficiscantur | — |
| Acts.23.27 | interfectūrī | interfecturi | — |
| Acts.23.35 | asservārī | asseruari | — |
| Acts.24.1 | compāruērunt | comparuerunt | compa |
| Acts.24.2 | prōvidentiā | prouidentia | — |
| Acts.24.4 | æquitāte | æquitate | quitate |
| Acts.24.17 | allevārem | alleuarem | allenarein |
| Acts.24.22 | dēscenderit | descenderit | — |
| Acts.24.26 | sæpius | sæpius | — |
| Acts.24.27 | Portium | Portium | — |
| Acts.25.15 | poscentēs | poscentes | poIcentes |
| Acts.25.19 | quāsdam | quasdam | quaída |
| Acts.26.8 | excitārī | excitari | — |
| Acts.26.14 | Hebræō | Hebræo | — |
| Acts.26.17 | Vindicābō | vindicabo | vindicádo |
| Acts.26.22 | summōs | summos | fuimmos |
| Acts.27.5 | nāvigātō | nauigato | hauigato |
| Acts.27.9 | præteriisset | præteriisset | — |
| Acts.27.9 | monēbat | monebat | — |
| Acts.27.12 | Phœnīcēn | Phœnicen | — |
| Acts.27.16 | Claudam | Claudam | Claudain |
| Acts.27.20 | incumbente | incumbente | — |
| Acts.27.21 | dētrīmentum | detrimentum | — |
| Acts.27.21 | damnumque | damnumque | — |
| Acts.27.24 | sistī | sisti | sistř |
| Acts.27.24 | condōnāsse | condonasse | — |
| Acts.27.27 | quārta | quarta | — |
| Acts.27.28 | ulnās | vlnas | — |
| Acts.27.28 | ulnās | vlnas | vinas |
| Acts.27.29 | puppī | puppi | — |
| Acts.27.30 | ancorās | ancoras | — |
| Acts.27.31 | mānserint | manserint | — |
| Acts.27.31 | ēvādere | euadere | cuadere |
| Acts.28.1 | Ēlāpsī | Elapsi | — |
| Acts.28.1 | Melitam | Melitam | Melitain |
| Acts.28.3 | collēgisset | collegisset | — |
| Acts.28.4 | pendentem | pendentem | pendentein |
| Acts.28.18 | exāminātum | examinatum | examinatuin |
| Acts.28.26 | perspiciētis | perspicietis | — |
| Acts.28.27 | obtūsē | obtuse | — |
| Acts.28.30 | conductō | conducto | — |
| Acts.28.30 | prīvātim | priuatim | — |

## Punctuation not from the OCR (228)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

2.15 *tertia)*; 2.34 *meam,*; 2.38 *veniam,*; 2.38 *assequimini.*; 2.39 *promissio,*; 2.39 *natos,*; 2.39 *remotiores,*; 2.39 *noster.*; 2.40 *commonuit,*; 2.40 *et,*; 2.40 *euaderent,*; 2.40 *est.*; 2.41 *admissa,*; 2.41 *baptizati,*; 2.41 *millia.*; 3.14 *Vos,*; 4.10 *sanum.*; 4.14 *astantem,*; 4.17 *faciant.*; 5.1 *autem,*; 5.1 *nomine,*; 5.1 *sua,*; 5.1 *vendidit:*; 5.2 *Et,*; 5.2 *parte,*; 5.2 *conscia,*; 5.2 *attulit,*; 5.2 *deposuit.*; 5.3 *Petrus:*; 5.3 *Anania,*; 5.3 *inquit,*; 5.3 *Satanas,*; 5.3 *mentireris,*; 5.3 *detraheres?*; 5.4 *manebat,*; 5.14 *magisque,*; 5.14 *virorum,*; 5.23 *comperiisse,*; 5.23 *renunciarunt,*; 5.23 *astantes:*; 5.23 *sed,*; 5.23 *aperuissent,*; 5.23 *neminem.*; 5.24 *auditis,*; 5.24 *sacerdos,*; 5.24 *antistes,*; 5.24 *pontifices,*; 5.24 *ambigebant,*; 5.24 *esset.*; 5.25 *quidam,*; 5.25 *nunciauit,*; 5.25 *illos,*; 5.25 *dedissent,*; 5.25 *fano,*; 5.25 *docere.*; 5.26 *ministris,*; 5.26 *adduxit,*; 5.26 *vi:*; 5.26 *enim,*; 5.26 *lapidarentur.*; 5.27 *concilio,*; 5.27 *interrogauit:*; 5.28 *docere?*; 5.28 *vestra,*; 5.28 *deriuare.*; 5.29 *responderunt:*; 5.29 *est,*; 5.29 *hominibus.*; 5.30 *suscitauit,*; 5.30 *interfecistis.*; 5.31 *extulit,*; 5.31 *correctionem,*; 5.31 *veniam.*; 5.32 *rerum,*; 5.32 *Spiritus,*; 5.34 *educi.*; 5.36 *redacti.*; 5.39 *obtemperarunt.*; 5.41 *ignominia:*; 7.7 *Deus,*; 7.16 *Emoris,*; 7.36 *quadraginta.*; 7.52 *interfectores:*; 7.53 *seruastis.*; 9.5 *ille:*; 9.33 *captum,*; 9.35 *incolæ,*; 10.17 *vestibulo,*; 10.21 *adestis?*; 10.33 *veneris.*; 11.13 *Petrum,*; 11.21 *conuerteret.*; 11.22 *Hierosolymitana,*; 11.27 *Antiochiam.*; 13.8 *auertere.*; 13.12 *Domini.*; 13.46 *conuerti.*; 13.50 *Iudæi,*; 13.52 *complebantur.*; 14.15 *eis:*; 15.2 *contentio:*; 15.2 *Barnabæ,*; 15.2 *suis,*; 15.2 *seniores,*; 15.2 *quæstionem.*; 15.3 *deducti,*; 15.3 *obibant,*; 15.3 *exponentes,*; 15.3 *fratres,*; 15.3 *lætitia.*; 15.4 *est,*; 15.4 *senioribus,*; 15.4 *et,*; 15.4 *fecisset,*; 15.4 *retulerunt.*; 15.5 *eorum,*; 15.5 *crediderant,*; 15.5 *secta,*; 15.5 *dicerent,*; 15.5 *indicendumque,*; 15.5 *seruarent.*; 15.6 *gratia,*; 15.6 *conuenerunt:*; 15.7 *exorta,*; 15.7 *Petrus,*; 15.7 *habuit:*; 15.7 *fratres,*; 15.7 *scitis,*; 15.7 *elegerit,*; 15.7 *crederent.*; 15.8 *dedit,*; 15.8 *Sanctum,*; 15.8 *nobis:*; 15.9 *fecit,*; 15.9 *purgasset.*; 15.10 *tentatis,*; 15.10 *imponendo,*; 15.10 *nostri,*; 15.10 *potuimus?*; 15.11 *credimus,*; 15.11 *illi.*; 15.12 *multitudo,*; 15.12 *narrantes,*; 15.12 *designasset.*; 15.13 *Deinde,*; 15.13 *conticuerunt,*; 15.13 *fecit:*; 15.13 *fratres,*; 15.13 *me.*; 15.14 *Simeon,*; 15.23 *fratres,*; 15.31 *lecta,*; 15.32 *Silas,*; 15.32 *vates,*; 15.32 *erant,*; 15.32 *sunt,*; 15.32 *confirmarunt.*; 15.33 *commorati,*; 15.35 *sunt,*; 15.35 *docentes,*; 15.35 *explicantes.*; 15.36 *Barnabam,*; 15.36 *vrbes,*; 15.36 *explanassent,*; 15.36 *reuiseret,*; 15.36 *haberent.*; 15.37 *assumere,*; 15.37 *Marcum.*; 15.38 *censebat,*; 15.38 *eum,*; 15.38 *defecisset,*; 15.38 *fuisset,*; 15.38 *assumendum.*; 15.39 *est,*; 15.39 *sint;*; 15.39 *Barnabas,*; 15.39 *Marco,*; 15.39 *Cyprum.*; 15.40 *Paulus,*; 15.40 *Sila,*; 15.40 *est,*; 15.40 *fratribus:*; 15.41 *obijt,*; 15.41 *ecclesias.*; 16.9 *nobis.*; 17.5 *conari:*; 17.19 *ductum,*; 17.19 *alloquuntur:*; 18.8 *autem,*; 18.13 *colant,*; 18.13 *dixerunt.*; 18.17 *Gallione.*; 19.2 *audiuimus.*; 19.6 *vaticinabantur.*; 19.12 *adeo,*; 19.12 *sudaria,*; 19.12 *semicinctia,*; 19.12 *liberarentur,*; 19.12 *exirent.*; 19.13 *obtestatoribus,*; 19.13 *Iesu,*; 19.13 *dicentes:*; 19.13 *Iesum,*; 19.13 *prædicat.*; 19.14 *septem,*; 19.24 *argentarius,*; 20.16 *venire.*; 20.36 *supplicauit.*; 20.38 *nauem.*; 21.7 *diem.*; 21.37 *Græce?*; 23.4 *conuiciaris?*; 23.5 *maledicito.*; 23.8 *resurrectionem,*; 23.8 *angelum,*; 23.8 *negant:*; 23.19 *haberet.*; 23.35 *asseruari.*; 24.1 *comparuerunt.*; 24.19 *sunt,*; 24.27 *Festum.*; 25.7 *poterant:*; 26.8 *excitari?*; 27.9 *præteriisset,*; 27.23 *sum,*; 27.32 *siuerunt.*; 28.8 *sanauit.*; 28.31 *docens.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
