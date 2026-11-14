# Rev 1–22 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Rev 1-22` → `text/orig/draft/REV.usfm` (now `text/orig/REV.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Rev.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/REV.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 7105 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 53 | read in the OCR, a spelling the approved rules normalize |
| variant | 95 | read in the OCR, a printer's spelling no rule covers |
| ę | 11 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 63 | read in the OCR with a nasal bar (m or n put back) |
| misread | 11 | the settled word misread by the OCR; spelling as settled |
| lexicon | 399 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 7 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 42 | OCR unreadable; the settled word in the printer's conventions |
| none | 61 | no OCR word; the settled word in the printer's conventions |
| all | 7847 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **.10** *temptentur* → *tententur*: 1573 canvas 939, read on the page: printed tentẽtur (read by Claude, 2026-11-13)
- **.2** *prōnūntiantem* → *pronunciantem*: 1573 canvas 939, read on the page: line break: pronun / ciantem (read by Claude, 2026-11-13)
- ✱ **8.21** *jaciētur* → *sacietur*: 1573 canvas 946, read on the page: ſacietur, a misprint for iacietur, printed as is (read by Claude, 2026-11-13)
- **1.6** *cælī* → *cœli*: 1573 canvas 942, read on the page: œ (read by Claude, 2026-11-13)
- **2.5** *sæcula* → *secula*: 1573 canvas 948, read on the page: plain e (read by Claude, 2026-11-13)
- **.18** *flammæ* → *flammæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)
- **.20** *dextrā* → *dextera*: 1573 canvas 938, read on the page: dexte-ra (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (53)

*cum* → *quum* ×4; *cāritātem* → *charitatem* ×2; *dextræ* → *dexteræ*; *dextrā* → *dextera* ×4; *gadī* → *gaddi*; *intellegant* → *intelligant*; *iīs* → *eis* ×9; *iīsque* → *eisque* ×2; *multābō* → *mulctabo*; *obœdīrent* → *obedirent*; *quattuor* → *quatuor* ×20; *quidquam* → *quicquam*; *quotiēns* → *quoties*; *quīcumque* → *quicunque* ×2; *sescenta* → *sexcenta*; *sescentī* → *sexcenti*; *temptātiōnis* → *tentationis*

## Printer's spellings no rule covers (94)

*audieram* → *audiueram* ×2; *audīssem* → *audiuissem*; *chœnix* → *chænix*; *chœnīcēs* → *chenices*; *circumdabat* → *circundabat*; *citharœdōrum* → *citharædorum* ×2; *combūrent* → *conburent*; *cælicolās* → *cœlicolas*; *cælum* → *cœlum* ×3; *cælumque* → *cœlumque*; *cælī* → *cœli*; *cælō* → *cœlo* ×25; *cārum* → *charum*; *cētera* → *cætera*; *dumtaxat* → *duntaxat*; *exsecrābilēs* → *execrabiles*; *exsequantur* → *exequantur*; *exsequuntur* → *exequuntur*; *exstiterit* → *extiterit*; *exstitit* → *extitit* ×5; *exstitērunt* → *extiterunt* ×3; *exstitēruntque* → *extiteruntque* ×2; *exstābit* → *extabit* ×2; *exstīnctum* → *extinctum*; *exsultēmus* → *exultemus*; *frēnōs* → *frænos*; *fēminīs* → *fœminis*; *fœderis* → *federis*; *hī* → *i*; *immitte* → *iinmitte*; *lacrimam* → *lachrymam*; *lētō* → *letho*; *negōtiantur* → *negociantur*; *nūntiāvit* → *nunciauit*; *pretiīs* → *precijs*; *pretiōsissimīs* → *preciosissimis*; *pretiōsissimō* → *preciosissimo*; *quamquam* → *quanquam* ×2; *repetierit* → *repetiuerit*; *submergeret* → *summergeret*; *sæcula* → *secula* ×9; *sæculōrum* → *seculorum*; *tamquam* → *tanquam* ×2; *tætrō* → *tetro* ×2; *tūribulum* → *thuribulum* ×2; *tūs* → *thus*

## Not read in the OCR (114)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Rev.1.1 | patefactiō | patefactio | apatefactio |
| Rev.1.6 | abluit | abluit | — |
| Rev.1.8 | α | α | a |
| Rev.1.8 | ω | ω | w |
| Rev.1.11 | α | α | — |
| Rev.1.11 | ω | ω | — |
| Rev.1.16 | aspectus | aspectus | — |
| Rev.2.1 | Ephesīnæ | Ephesinæ | — |
| Rev.2.5 | trānsmovēbō | transmouebo | tranfinouebo |
| Rev.2.19 | priōribus | prioribus | priorib |
| Rev.2.20 | Jezabelem | Iezabelem | Iesabelem |
| Rev.2.23 | remūnerābor | remunerabor | — |
| Rev.3.2 | cōnfirmā | confirma | — |
| Rev.3.3 | audīverīsque | audiuerisque | — |
| Rev.3.3 | vigilāveris | vigilaueris | — |
| Rev.3.10 | cōnservāstī | conseruasti | — |
| Rev.3.16 | ēvomam | euomam | euomain |
| Rev.4.3 | smaragdum | smaragdum | — |
| Rev.4.3 | referēns | referens | — |
| Rev.4.8 | armipotēns | armipotens | — |
| Rev.5.2 | Vidīque | vidique | vidić |
| Rev.5.5 | plōrā | plora | ra |
| Rev.5.9 | mactātus | mactatus | maEtatus |
| Rev.6.15 | tribūnī | tribuni | — |
| Rev.7.3 | læditōte | læditote | — |
| Rev.7.14 | stolāsque | stolasque | stolasó |
| Rev.8.1 | dīmidiam | dimidiam | dimidiaın |
| Rev.8.12 | obfuscātā | obfuscata | offuscata |
| Rev.8.13 | volantem | volantem | volanten |
| Rev.9.6 | invenient | inuenient | necinuenient |
| Rev.9.7 | lōcustārum | locustarum | locustaruin |
| Rev.9.8 | dentēs | dentes | — |
| Rev.9.9 | lōrīcæ | loricæ | lori cæ |
| Rev.9.17 | hyacinthinās | hyacinthinas | — |
| Rev.9.19 | nocērent | nocerent | — |
| Rev.10.5 | vīderam | videram | — |
| Rev.10.10 | dēglūtīvī | deglutiui | — |
| Rev.11.4 | olīvæ | oliuæ | — |
| Rev.11.9 | linguīsque | linguisque | — |
| Rev.12.1 | Vīsumque | Visumque | — |
| Rev.12.1 | amicta | amicta | — |
| Rev.12.4 | peperisset | peperisset | — |
| Rev.12.10 | accūsātor | accusator | — |
| Rev.12.10 | accūsābat | accusabat | — |
| Rev.12.11 | suīque | suique | — |
| Rev.12.11 | testimōniī | testimonii | — |
| Rev.12.11 | vīcērunt | vicerunt | — |
| Rev.12.11 | amārunt | amarunt | — |
| Rev.12.11 | oppetierint | oppetierint | — |
| Rev.12.12 | lætāminī | lætamini | — |
| Rev.12.12 | cælicolæ | cœlicolæ | — |
| Rev.12.12 | furōre | furore | — |
| Rev.12.12 | percitus | percitus | — |
| Rev.12.12 | breve | breue | — |
| Rev.12.14 | ālæ | alæ | — |
| Rev.12.14 | alenda | alenda | Dan |
| Rev.13.16 | adigēbat | adigebat | — |
| Rev.14.2 | ingentisque | ingentisque | — |
| Rev.14.7 | fontium | fontium | fontiuin |
| Rev.14.8 | sævō | sæuo | suo |
| Rev.14.10 | sævum | sæuum | fuum |
| Rev.14.10 | pōtābit | potabit | porabit |
| Rev.14.15 | metendī | metendi | netendi |
| Rev.15.1 | mīrābile | mirabile | — |
| Rev.16.11 | vulneribusque | vulneribusque | vulneribusą |
| Rev.16.16 | Congregāvit | Congregauit | — |
| Rev.16.16 | Armageddōn | Armageddon | — |
| Rev.16.18 | sonitūs | sonitus | — |
| Rev.16.18 | tantusque | tantusque | — |
| Rev.16.19 | sævæ | sæuæ | lænæ |
| Rev.17.6 | testiumque | testiumque | testiumýs |
| Rev.17.10 | Septemque | Septemque | — |
| Rev.17.13 | suāsque | suasque | suasóque |
| Rev.18.1 | præditum | præditum | — |
| Rev.18.8 | lūctus | luctus | luEtus |
| Rev.18.9 | luxuriātīque | luxuriatique | — |
| Rev.18.12 | margarītārum | margaritarum | margaritatum |
| Rev.18.12 | cōnfecta | confecta | contecta |
| Rev.18.12 | marmore | marmore | marinore |
| Rev.18.13 | rhēdārum | rhedarum | rhedaruin |
| Rev.18.14 | opīma | opima | opina |
| Rev.18.16 | gemmīsque | gemmisque | geminisque |
| Rev.18.23 | dēceptæ | deceptæ | dece ptæ |
| Rev.19.8 | splendidōque | splendidoque | splendidogs |
| Rev.19.9 | nūptiārum | nuptiarum | rum |
| Rev.19.14 | candidō | candido | — |
| Rev.19.15 | feriat | feriat | — |
| Rev.20.3 | perāctī | peracti | peraEti |
| Rev.20.8 | Magōgum | Magogum | — |
| Rev.20.12 | apertīque | apertique | apertis |
| Rev.20.12 | apertus | apertus | — |
| Rev.21.1 | novamque | nouamque | — |
| Rev.21.1 | priorque | priorque | — |
| Rev.21.1 | perierat | perierat | — |
| Rev.21.3 | habitābit | habitabit | — |
| Rev.21.4 | Abstergetque | Abstergetque | — |
| Rev.21.4 | abierint | abierint | — |
| Rev.21.5 | fīdaque | fidaque | fidań |
| Rev.21.6 | α | α | — |
| Rev.21.6 | ω | ω | a |
| Rev.21.10 | arduumque | arduumque | arduuınque |
| Rev.21.12 | altum | altum | altuin |
| Rev.21.17 | cubitīs | cubitis | — |
| Rev.21.18 | jaspide | iaspide | laspide |
| Rev.21.19 | sapphīrus | sapphirus | — |
| Rev.21.19 | smaragdus | smaragdus | fimaragdus |
| Rev.21.21 | singulæ | singulæ | fin gulæ |
| Rev.21.23 | lūceant | luceant | — |
| Rev.21.27 | quodve | quodue | — |
| Rev.22.1 | fluvium | fluuium | duuium |
| Rev.22.12 | remūnerer | remunerer | re |
| Rev.22.13 | α | α | a |
| Rev.22.13 | ω | ω | a |
| Rev.22.15 | impudīcī | impudici | — |

## Punctuation not from the OCR (53)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.3 *instat.*; 3.17 *scis,*; 3.22 *ecclesijs.*; 4.3 *referens:*; 6.1 *aspiciens,*; 6.1 *spectatum.*; 9.8 *similes:*; 9.19 *nocerent.*; 10.3 *voces:*; 11.16 *sunt,*; 12.10 *dicentem:*; 12.10 *salus,*; 12.10 *potestas,*; 12.10 *nostri,*; 12.10 *eius:*; 12.10 *accusator,*; 12.10 *accusabat.*; 12.11 *sanguine,*; 12.11 *vicerunt:*; 12.11 *amarunt,*; 12.11 *oppetierint.*; 12.12 *cœli,*; 12.12 *cœlicolæ.*; 12.12 *incolis:*; 12.12 *vos,*; 12.12 *percitus,*; 12.12 *sciens,*; 13.11 *draco.*; 13.17 *numerum.*; 14.2 *sonitum,*; 14.2 *aquarum,*; 14.2 *est:*; 14.4 *sunt,*; 15.1 *mirabile,*; 15.5 *cœlo.*; 16.16 *locum,*; 16.16 *Armageddon.*; 16.17 *effudit,*; 16.17 *fano,*; 16.17 *dicens:*; 16.17 *est.*; 16.18 *tonitrua,*; 16.18 *fulgura:*; 17.3 *cornua.*; 20.2 *annos:*; 20.7 *carcere.*; 20.10 *perennitatem.*; 21.1 *cœlum,*; 21.1 *cœlum,*; 21.1 *perierat,*; 21.3 *eorum:*; 21.4 *abierint.*; 22.13 *vltimus.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
