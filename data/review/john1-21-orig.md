# John 1–21 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig John 1-21` → `text/orig/draft/JHN.usfm` (now `text/orig/JHN.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/John.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/JHN.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 12458 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 89 | read in the OCR, a spelling the approved rules normalize |
| variant | 122 | read in the OCR, a printer's spelling no rule covers |
| ę | 17 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 178 | read in the OCR with a nasal bar (m or n put back) |
| misread | 13 | the settled word misread by the OCR; spelling as settled |
| lexicon | 810 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 15 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 39 | OCR unreadable; the settled word in the printer's conventions |
| none | 66 | no OCR word; the settled word in the printer's conventions |
| all | 13807 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **4.10** *intellegerēs* → *intelligeres*: 1573 canvas 816, read on the page: line break: intellige-res (read by Claude, 2026-11-13)
- **5.3** *exspectantium* → *expectantium*: 1573 canvas 817, read on the page: line break: expe-ctantium (read by Claude, 2026-11-13)
- ✱ **5.9** *ambulābat* → *ambulabar*: 1573 canvas 817, read on the page: a misprint, printed as is (read by Claude, 2026-11-13)
- **14.31** *intellegendum* → *intelligendum*: 1573 canvas 827, read on the page: printed intelligendũ (read by Claude, 2026-11-13)
- **20.9** *intellegēbant* → *intelligebant*: 1573 canvas 830, read on the page: printed intelligebãt (read by Claude, 2026-11-13)
- **1.24** *Pharisæīs* → *Pharisæis*: 1573 canvas 814, read on the page: ę (read by Claude, 2026-11-13)
- ⚑ **6.31** *iīs* → *eis*: 1573 canvas 819, read on the page (read by Claude, 2026-11-13)
- ⚑ **6.43** *iīs* → *eis*: 1573 canvas 819, read on the page (read by Claude, 2026-11-13)
- **7.39** *Sānctus* → *sanctus*: 1573 canvas 820, read on the page: lower case; san-ctus (read by Claude, 2026-11-13)
- **10.39** *exiit* → *exijt*: 1573 canvas 823, read on the page (read by Claude, 2026-11-13)
- ⚑ **12.23** *iīs* → *eis*: 1573 canvas 825, read on the page (read by Claude, 2026-11-13)
- ⚑ **17.26** *iīs* → *eis*: 1573 canvas 828, read on the page (read by Claude, 2026-11-13)
- **2.23** *Paschæ* → *Paschæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)
- **13.1** *Paschæ* → *Paschæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (89)

*cāritāte* → *charitate*; *dextram* → *dexteram* ×2; *intellegerent* → *intelligerent*; *intellegimus* → *intelligimus*; *intellegāmus* → *intelligamus*; *intellegēns* → *intelligens*; *intellegētis* → *intelligetis* ×2; *iīs* → *eis* ×57; *iīsque* → *eisque* ×4; *quattuor* → *quatuor* ×3; *quemquam* → *quenquam* ×3; *quidquam* → *quicquam* ×2; *quidquid* → *quicquid* ×7; *quīcumque* → *quicunque* ×3; *temptandī* → *tentandi*

## Printer's spellings no rule covers (122)

*abīsse* → *abijsse*; *arcessit* → *accersit*; *arcessītum* → *accersitum*; *arcessītōs* → *accersitos*; *auctōre* → *autore*; *audierint* → *audiuerint*; *audierit* → *audiuerit* ×2; *audiērunt* → *audiuerunt* ×2; *audīsse* → *audiuisse*; *audīssent* → *audiuissent*; *audīstis* → *audiuistis* ×2; *audīstī* → *audiuisti*; *barabbam* → *barrabam*; *barabbās* → *barrabas*; *bracchium* → *brachium*; *cælō* → *cœlo* ×11; *cēna* → *cœna*; *cēnā* → *cœna*; *cēpit* → *cæpit*; *cēpērunt* → *cæperunt* ×2; *exiit* → *exiuit*; *exsequar* → *exequar*; *exsequitur* → *exequitur*; *exsequī* → *exequi*; *exstat* → *extat*; *exstitisse* → *extitisse* ×2; *exstitit* → *extitit* ×2; *exsultāre* → *exultare*; *exsuscitem* → *exuscitem* ×2; *exīsse* → *exijsse*; *fēcit* → *fetit*; *fēmina* → *fœmina*; *fēminæ* → *fœminæ*; *fēminā* → *fœmina*; *fētet* → *fœtet*; *galilææ* → *galileæ*; *hicine* → *hiccine*; *hiems* → *hyems*; *ierant* → *iuerant* ×2; *ierō* → *iuero*; *iit* → *iuit* ×4; *intellegitis* → *intelligitis*; *iērunt* → *iuerunt*; *iī* → *iui*; *jōhannem* → *iohanem*; *jōvæ* → *ioue*; *lacrimāvit* → *lachrymauit*; *litteræ* → *literæ*; *litterās* → *literas* ×3; *litterīs* → *literis*; *lētālis* → *lethalis*; *lētō* → *letho* ×2; *lītore* → *littore*; *monumentum* → *monimentum* ×8; *monumentīs* → *monimentis*; *monumentō* → *monimento* ×2; *murræ* → *myrrhæ*; *nummulāriōs* → *numularios*; *numquam* → *nunquam* ×6; *numquid* → *nunquid* ×2; *nūntiārunt* → *nunciarunt*; *nūntiātum* → *nunciatum* ×2; *permānsūrum* → *permanssurum*; *petīstis* → *petijstis*; *petīvit* → *petijt*; *pretiōsī* → *preciosi*; *prænūntiābit* → *prænunciabit*; *quamquam* → *quanquam*; *quæcumque* → *quæcunque* ×5; *quōcumque* → *quocunque*; *quōscumque* → *quoscunque*; *sīcine* → *siccine*; *umquam* → *vnquam* ×5; *ænōne* → *enone*; *ōcius* → *ocyus*

## e against the settled æ, printed æ (3)

*jūdæī* → *iudæi* ×2; *jūdæōs* → *iudæos*

## Not read in the OCR (118)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| John.1.7 | testārētur | testaretur | — |
| John.1.8 | testārētur | testaretur | — |
| John.1.9 | collūstrat | collustrat | — |
| John.1.14 | ūnigenæ | vnigenæ | vnige næ |
| John.1.22 | respōnsum | responsum | responsuin |
| John.1.22 | dēmus | demus | deinus |
| John.1.32 | columbam | columbam | coluinbain |
| John.1.33 | baptīzat | baptizat | baptizar |
| John.2.15 | bovēs | boues | bones |
| John.2.16 | vēnditōribus | venditoribus | vēditoribº |
| John.2.20 | excitābis | excitabis | Mar |
| John.3.2 | doctōrem | doctorem | doctorein |
| John.3.11 | testificāmur | testificamur | teltificamur |
| John.3.16 | ūnicum | vnicum | vnicuin |
| John.3.18 | damnābitur | damnabitur | daınnabitur |
| John.4.4 | Samarīam | Samariam | Sainariain |
| John.4.8 | cibōs | cibos | — |
| John.4.8 | emerent | emerent | — |
| John.4.10 | peterēs | peteres | — |
| John.4.11 | haustrum | haustrum | — |
| John.4.11 | puteus | puteus | — |
| John.4.11 | profundus | profundus | — |
| John.4.12 | parente | parente | — |
| John.4.12 | aquātiōne | aquatione | — |
| John.4.12 | pecora | pecora | — |
| John.4.14 | dederō | dedero | — |
| John.4.14 | biberit | biberit | — |
| John.4.14 | sitiet | sitiet | — |
| John.4.14 | dederō | dedero | — |
| John.4.14 | scatūriēns | scaturiens | — |
| John.4.25 | Messīam | Messiam | — |
| John.4.28 | hominēsque | hominesque | hominesó |
| John.4.29 | fortasse | fortasse | fortafsis |
| John.4.36 | gaudeat | gaudeat | — |
| John.4.36 | messor | messor | gau |
| John.4.38 | metendum | metendum | metéduin |
| John.4.41 | multōque | multoque | multog |
| John.4.52 | scīscitantī | sciscitanti | seiscitati |
| John.5.3 | ægrōtantium | ægrotantium | ægrotanitium |
| John.5.4 | dēscendēbat | descendebat | defceridebat |
| John.5.4 | dēscendēbat | descendebat | defceridebat |
| John.5.6 | dēcubuisse | decubuisse | cubuisse |
| John.5.12 | ambulāret | ambularet | ainbularet |
| John.5.20 | mōnstrābit | monstrabit | inonstrabit |
| John.6.2 | ægrōtantibus | ægrotantibus | — |
| John.6.10 | grāminis | graminis | graininis |
| John.6.39 | dēperdam | deperdam | deperdain |
| John.6.50 | vēscātur | vescatur | — |
| John.6.61 | mussāre | mussare | — |
| John.7.2 | umbrāculōrum | vmbraculorum | vinbraculorum |
| John.7.23 | succēnsētis | succensetis | fuccentetis |
| John.7.26 | contrādīcitur | contradicitur | — |
| John.7.48 | proceribus | proceribus | proteribus |
| John.8.3 | cōnstitūtā | constituta | — |
| John.8.6 | humum | humum | — |
| John.8.6 | exarāre | exarare | — |
| John.8.13 | testāris | testaris | — |
| John.8.14 | vēnerim | venerim | — |
| John.8.37 | prōgeniem | progeniem | pgeniem |
| John.8.49 | probrō | probro | pbro |
| John.9.1 | nātīvitāte | natiuitate | — |
| John.9.32 | aperuisse | aperuisse | — |
| John.10.21 | Hæ | Hæ | Hæres |
| John.10.22 | Instaurālia | Instauralia | — |
| John.11.1 | Bēthaniā | Bethania | Bethaua |
| John.11.7 | Petāmus | Petamus | Petam |
| John.11.11 | expergēfaciendum | expergefaciendum | — |
| John.11.17 | agentem | agentem | agentein |
| John.11.42 | circumstantem | circumstantem | circuinstantem |
| John.12.3 | eōsdemque | eosdemque | eofdeinque |
| John.12.7 | sepultūræ | sepulturæ | — |
| John.12.7 | reservāvit | reseruauit | — |
| John.12.40 | frūgemque | frugemque | — |
| John.12.42 | prīvārentur | priuarentur | priuarentura |
| John.13.2 | cēnā | Cena | Etcœna |
| John.13.12 | fēcerim | fecerim | feceriin |
| John.13.18 | ēlēgerim | elegerim | — |
| John.13.21 | prōdat | prodat | — |
| John.13.36 | abīs | abis | — |
| John.13.38 | cantātūrum | cantaturum | — |
| John.14.3 | assūmam | assumam | alsumam |
| John.15.5 | palmitēs | palmites | palimites |
| John.15.7 | concēdētur | concedetur | con |
| John.15.16 | dēstināvī | destinaui | — |
| John.15.16 | dūret | duret | — |
| John.15.25 | Ōdērunt | Oderunt | Odcrunt |
| John.16.1 | dēficiātis | deficiatis | — |
| John.16.11 | jūdicātus | iudicatus | — |
| John.16.14 | sūmet | sumet | — |
| John.16.15 | sūmptūrum | sumpturum | suinpturuin |
| John.16.17 | aspectūrōs | aspecturos | — |
| John.16.19 | aspectūrōs | aspecturos | — |
| John.17.12 | custōdīvī | custodiui | custodiPfal |
| John.17.24 | amāverīs | amaueris | — |
| John.18.28 | intrārunt | intrarunt | — |
| John.18.29 | affertis | affertis | — |
| John.18.39 | condōnem | condonem | — |
| John.19.6 | fīgite | figite | — |
| John.19.13 | Lapidipavium | Lapidipauium | Lapidipautuin |
| John.19.15 | fīgam | figam | — |
| John.19.24 | dīvidendam | diuidendam | — |
| John.19.29 | affīxam | affixam | — |
| John.19.29 | admōvērunt | admouerunt | — |
| John.19.29 | ōrī | ori | — |
| John.19.37 | compūnxerint | compunxerint | — |
| John.20.15 | auferam | auferam | — |
| John.20.17 | ascēnsūrum | ascensurum | — |
| John.20.26 | mediōque | medioque | medios |
| John.20.27 | laterī | lateri | — |
| John.20.30 | mīranda | miranda | — |
| John.20.31 | adipīscāminī | adipiscamini | — |
| John.21.1 | Tyberiadis | Tyberiadis | — |
| John.21.2 | aliīque | aliique | aliją |
| John.21.6 | Jacite | Iacite | lacite |
| John.21.14 | suscitātus | suscitatus | — |
| John.21.17 | quæsīvisse | quæsiuisse | quessuisse |
| John.21.20 | pectorī | pectori | — |
| John.21.25 | scrībendōs | scribendos | — |

## Punctuation not from the OCR (119)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.4 *hominum,*; 1.7 *testimonium,*; 1.7 *testaretur,*; 1.7 *crederent.*; 1.8 *lux,*; 1.8 *testaretur.*; 1.9 *lux,*; 1.9 *mundum.*; 1.10 *erat,*; 1.10 *fuit,*; 1.10 *cognouit.*; 1.11 *venit,*; 1.36 *Dei.*; 2.2 *sunt.*; 2.10 *alloquitur:*; 2.16 *hinc,*; 2.20 *excitabis?*; 4.8 *emerent.*; 4.10 *respondens:*; 4.10 *intelligeres,*; 4.10 *inquit,*; 4.10 *postulat,*; 4.10 *eo,*; 4.10 *viuam.*; 4.11 *mulier:*; 4.11 *Domine,*; 4.11 *ei,*; 4.11 *habes,*; 4.11 *profundus.*; 4.11 *viuam?*; 4.12 *Iacobo,*; 4.12 *tradidit,*; 4.12 *ipse,*; 4.12 *pecora?*; 4.13 *respondit:*; 4.13 *bibit,*; 4.13 *sitit,*; 4.14 *aqua,*; 4.14 *dedero,*; 4.14 *biberit,*; 4.14 *sitiet,*; 4.14 *aqua,*; 4.14 *dedero,*; 4.14 *æternam.*; 4.25 *Messiam(*; 4.34 *absoluere.*; 4.36 *messor.*; 5.4 *descendebat,*; 5.17 *dixit:*; 5.28 *mirari:*; 6.2 *ægrotantibus.*; 6.9 *multos?*; 6.31 *comedendum.*; 6.43 *vos.*; 6.45 *venit.*; 6.49 *sunt.*; 6.71 *duodecim.*; 7.8 *completum.*; 7.13 *metu.*; 7.28 *est,*; 7.39 *sanctus,*; 7.48 *Pharisæis?*; 8.3 *constituta,*; 8.6 *exarare.*; 8.13 *testaris,*; 8.13 *ei,*; 8.27 *intelligerent,*; 8.36 *eritis.*; 9.1 *cæcum,*; 9.22 *formidabant.*; 9.27 *audiuistis:*; 9.37 *loquitur.*; 10.25 *testantur:*; 11.28 *vocaret.*; 11.37 *is,*; 11.37 *moreretur?*; 12.7 *reseruauit,*; 12.36 *subduxit.*; 12.42 *priuarentur.*; 13.21 *prodat.*; 13.36 *sequi:*; 14.22 *item?*; 14.31 *est,*; 14.31 *Patrem:*; 15.3 *habui.*; 15.4 *me.*; 15.7 *concedetur.*; 15.12 *amaui.*; 16.1 *loquor,*; 16.1 *deficiatis.*; 16.11 *est.*; 16.14 *sumet,*; 16.14 *exponat.*; 16.19 *me.*; 16.33 *mundum.*; 17.11 *venio.*; 17.12 *custodiui:*; 17.26 *eis.*; 18.27 *cecinit.*; 18.28 *intrarunt,*; 18.36 *Iesus:*; 18.36 *ministri,*; 18.37 *es?*; 18.40 *istum,*; 19.6 *figite,*; 19.25 *Magdalena.*; 19.29 *affixam,*; 19.29 *ori.*; 19.32 *fixi.*; 19.39 *centum.*; 19.42 *Iesum.*; 20.1 *monimento.*; 20.4 *monimentum,*; 20.11 *monimentum.*; 20.15 *auferam.*; 20.30 *discipulorum,*; 20.31 *adipiscamini.*; 21.14 *mortuis.*; 21.17 *me?*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. Found here: 5.4 *in piscinam*; 6.52 *suam*.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
