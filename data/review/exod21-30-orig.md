# Exod 21–30 as printed (1738): the draft for review

**Superseded 2026-11-14 by `data/review/exod1-30-orig.md`** (Exodus 1–30 rebuilt after every unread word was read on 1738's leaves).

Built 2026-11-14 by `python -m pipeline orig Exod 21-30` → `text/orig/draft/EXO.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1738 (archive.org bibliasacraexseb01cast)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). Paragraphs are 1738's own, read from the indents in its hOCR (listed below) (HUMAN.md decision 57). Regenerate after changing `data/decisions/Exod.orig.tsv`.

**Decision:** pending

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 3925 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 6 | read in the OCR, a spelling the approved rules normalize |
| variant | 25 | read in the OCR, a printer's spelling no rule covers |
| nasal | 1 | read in the OCR with a nasal bar (m or n put back) |
| misread | 68 | the settled word misread by the OCR; spelling as settled |
| lexicon | 186 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 8 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 320 | OCR unreadable; the settled word in the printer's conventions |
| none | 249 | no OCR word; the settled word in the printer's conventions |
| all | 4788 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **1.1** *cum* → *cum*: 1738 leaf 114, read on the page (Claude, 2026-11-14)
- **1.18** *Cumque* → *Quumque*: 1738 leaf 115, read on the page (Claude, 2026-11-14)
- **2.3** *cum* → *quum*: 1738 leaf 115, read on the page (Claude, 2026-11-14)
- **4.3** *Cumque* → *Quumque*: 1738 leaf 117, read on the page (Claude, 2026-11-14)
- **7.20** *cumque* → *quumque*: 1738 leaf 121, read on the page (Claude, 2026-11-14)
- **7.22** *cum* → *quum*: 1738 leaf 121, read on the page (Claude, 2026-11-14)
- **9.26** *Cum* → *quum*: 1738 leaf 123, read on the page (Claude, 2026-11-14)
- **12.23** *cum* → *quum*: 1738 leaf 126, read on the page (Claude, 2026-11-14)
- **12.25** *Cumque* → *Quumque*: 1738 leaf 126, read on the page (Claude, 2026-11-14)
- **12.27** *cum* → *quum*: 1738 leaf 126, read on the page (Claude, 2026-11-14)
- **13.5** *Cum* → *Quum*: 1738 leaf 127, read on the page (Claude, 2026-11-14)
- **2.11** *cum* → *quum*: 1738 leaf 115, read on the page (Claude, 2026-11-14)
- **13.19** *cum* → *quum*: 1738 leaf 128, read on the page (Claude, 2026-11-14)
- **14.30** *cum* → *quum*: 1738 leaf 129, read on the page (Claude, 2026-11-14)
- **15.20** *cum* → *cum*: 1738 leaf 129, read on the page (Claude, 2026-11-14)
- **16.3** *cum* → *quum*: 1738 leaf 130, read on the page (Claude, 2026-11-14)
- **16.3** *cum* → *quum*: 1738 leaf 130, read on the page (Claude, 2026-11-14)
- ⚑ **18.5** *Cum* → *Cumque*: 1738 leaf 132, read on the page: "Cumque his ad Mosem peruenit"; Wikisource and 1726 (TXT/1 OCR "cum his", TXT/3 "Cum his") have Cum; not found in 1750's OCR (Claude, 2026-11-14)
- **18.12** *cumque* → *cumque*: 1738 leaf 132, read on the page (Claude, 2026-11-14)
- **19.24** *cum* → *cum*: 1738 leaf 134, read on the page (Claude, 2026-11-14)
- **1.18** *quæsīsset* → *quæsiuisset*: 1738 leaf 115, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **2.22** *appellāvit* → *adpellauit*: 1738 leaf 116, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **5.8** *eandem* → *eamdem*: 1738 leaf 118, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **6.7** *intellegant* → *intelligant*: 1738 leaf 119, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **8.22** *intellegeret* → *intelligeret*: 1738 leaf 122, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **10.7** *alloquuntur* → *adloquuntur*: 1738 leaf 123, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **13.14** *quæsierint* → *quæsiuerint*: 1738 leaf 127, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **14.10** *appellāre* → *adpellare*: 1738 leaf 128, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **17.6** *astābō* → *adstabo*: 1738 leaf 131, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **17.9** *astātūrum* → *adstaturum*: 1738 leaf 132, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **17.15** *appellāvit* → *adpellauit*: 1738 leaf 132, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **19.4** *ascīverim* → *adsciuerim*: 1738 leaf 133, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- ⚑ **6.22** *Sethris* → *Setheris*: 1738 leaf 120, read on the page: "Elsaphan et | Setheris." (Claude, 2026-11-14)
- **8.14** *fētēret* → *fœteret*: 1738 leaf 121, read on the page: "ita, vt fœteret regio." (Claude, 2026-11-14)
- ✱ **12.11** *tenentēs* → *tententes*: 1738 leaf 125, read on the page: "bacillos manus | tententes", a misprint (Claude, 2026-11-14)
- **14.7** *sescentīs* → *sexcentis*: 1738 leaf 128, read on the page (Claude, 2026-11-14)
- ⚑ **15.6** *fortissimē* → *fortissimi*: 1738 leaf 129, read on the page: "decus | tibi fortissimi peperisti" (Claude, 2026-11-14)
- **16.20** *fētēbat* → *fœtebat*: 1738 leaf 131, read on the page (Claude, 2026-11-14)
- **16.24** *fētēbat* → *fœtebat*: 1738 leaf 131, read on the page (Claude, 2026-11-14)
- ⚑ **20.24** *cæspitum* → *cæspitium*: 1738 leaf 134, read on the page: "sed mihi cæspitium | altare fiat" (Claude, 2026-11-14)
- **13.3** *cōntiōnem* → *concionem*: 1738 leaf 127, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **12.25** *cærimōniam* → *cærimoniam*: 1738 leaf 126, read on the page: as the settled spelling (Claude, 2026-11-14)
- **12.26** *cærimōnia* → *cærimonia*: 1738 leaf 126, read on the page: as the settled spelling (Claude, 2026-11-14)
- **13.10** *cærimōniam* → *cærimoniam*: 1738 leaf 127, read on the page: as the settled spelling (Claude, 2026-11-14)
- **16.1** *multitūdō* → *multitudo*: 1738 leaf 130 (the chapter's first line, "Israe-|litarum multitudo"), read on the page: as the settled spelling (Claude, 2026-11-14)
- **16.3** *multitūdō* → *multitudo*: 1738 leaf 130, read on the page: as the settled spelling (Claude, 2026-11-14)
- **21.8** *affecit* → *adfecit*: 1738 leaf 135, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **21.30** *multa* → *multa*: 1738 leaf 135, read on the page: as the settled spelling (Claude, 2026-11-14)
- **22.6** *auctor* → *auctor*: 1738 leaf 136, read on the page: as the settled spelling (Claude, 2026-11-14)
- **24.17** *aspectu* → *adspectu*: 1738 leaf 138, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- **25.20** *aspectu* → *adspectu*: 1738 leaf 139, read on the page: a spelling the approved rules normalize (Claude, 2026-11-14)
- ⚑ **29.42** *solennis* → *solemnis*: 1738 leaf 144, read on the page: "ritus vestro generi | solemnis esto" (Claude, 2026-11-14)
- **30.34** *thus* → *tus*: 1738 leaf 145, read on the page: "et purum tus , tantumdem" (Claude, 2026-11-14)
- ⚑ **30.34** *tantundem* → *tantumdem*: 1738 leaf 145, read on the page (Claude, 2026-11-14)

## Spellings the approved rules normalize (6)

*afferto* → *adferto*; *aspectu* → *adspectu*; *causa* → *caussa*; *causam* → *caussam*; *cum* → *quum*; *paulatim* → *paullatim*

## Printer's spellings no rule covers (25)

*afferant* → *adferant*; *affigas* → *adfigas*; *alligato* → *adligato*; *alterius* → *halterius*; *apparatus* → *adparatus*; *apparento* → *adparento*; *applicato* → *adplicato* ×3; *apposititium* → *adposititium*; *apposito* → *adposito*; *aspersit* → *adspersit*; *bases* → *basses*; *execrator* → *exsecrator*; *executus* → *exsecutus*; *existant* → *exsistant*; *imposuerint* → *impossuerint*; *israelitæ* → *israelite*; *jussisset* → *iusiisset*; *monumento* → *monimento*; *monumentum* → *monimentum* ×2; *septentrionali* → *septemtrionali*; *totidem* → *tocidem*; *ultimi* → *vlcimi*

## Not read in the OCR (637)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Exod.21.2 | Hebræum | hebræum | ebrxum |
| Exod.21.3 | Si | Si | — |
| Exod.21.3 | cælebs | cælebs | — |
| Exod.21.3 | cælebs | cælebs | — |
| Exod.21.3 | manumittitor | manumittitor | — |
| Exod.21.4 | uxorem | vxorem | — |
| Exod.21.4 | qua | qua | — |
| Exod.21.4 | filios | filios | — |
| Exod.21.4 | filias | filias | — |
| Exod.21.4 | sunto | sunto | — |
| Exod.21.4 | manumittitor | manumittitor | mannmittitor |
| Exod.21.5 | amore | amore | amoie |
| Exod.21.5 | noluerit | noluerit | — |
| Exod.21.6 | eique | eique | cique |
| Exod.21.6 | valvam | valuam | valuain |
| Exod.21.6 | postem | postem | poftcm |
| Exod.21.6 | fibula | fibula | fubnla |
| Exod.21.7 | filiam | filiam | hham |
| Exod.21.7 | vendiderit | vendiderit | vendicierit |
| Exod.21.7 | manumittitor | manumittitor | — |
| Exod.21.8 | displicebit | displicebit | displuebit |
| Exod.21.8 | nec | nec | nee |
| Exod.21.8 | esto | esto | elto |
| Exod.21.9 | si | si | n |
| Exod.21.9 | filio | filio | tiiio |
| Exod.21.10 | victu | victu | — |
| Exod.21.10 | vestitu | vestitu | — |
| Exod.21.10 | congressu | congressu | gresfu |
| Exod.21.11 | manumittitor | manumittitor | — |
| Exod.21.13 | captaverit | captauerit | captauent |
| Exod.21.13 | incurrerit | incurrerit | — |
| Exod.21.13 | confugiat | Confugiat | Uconfugiat |
| Exod.21.15 | Qui | Qui | — |
| Exod.21.15 | capitale | capitale | — |
| Exod.21.15 | esto | esto | — |
| Exod.21.19 | baculo | baculo | bacuio |
| Exod.21.19 | illius | illius | iilitis |
| Exod.21.19 | cubatum | cubatum | eubatum |
| Exod.21.19 | medicationem | medicationem | — |
| Exod.21.19 | præstato | præstato | — |
| Exod.21.20 | baculo | baculo | bacuio |
| Exod.21.20 | præsens | præsens | prxfens |
| Exod.21.22 | mulcta | mulcta | — |
| Exod.21.22 | esto | esto | — |
| Exod.21.22 | arbitri | arbitri | arbkri |
| Exod.21.23 | pernicies | pernicies | pcrmcies |
| Exod.21.23 | vitam | vitam | vkam |
| Exod.21.25 | Sugillationem | Sugillationem | — |
| Exod.21.25 | vulnus | vulnus | vutnus |
| Exod.21.26 | corruperit | corruperit | comment |
| Exod.21.28 | feminam | feminam | — |
| Exod.21.28 | bos | bos | — |
| Exod.21.28 | bovis | bouis | bonis |
| Exod.21.28 | esto | esto | eito |
| Exod.21.29 | feminam | feminam | — |
| Exod.21.30 | Sin | Sin | Sinei |
| Exod.21.30 | ei | ei | — |
| Exod.21.30 | imponetur | imponetur | ponetur |
| Exod.21.30 | vitæ | vitæ | vitx |
| Exod.21.31 | Sive | Siue | Sine |
| Exod.21.31 | petiverit | petiuerit | — |
| Exod.21.31 | sive | siue | — |
| Exod.21.31 | esto | esto | cito |
| Exod.21.34 | fossae | fossae | fosfx |
| Exod.21.34 | præstato | præstato | prxftato |
| Exod.22.1 | clepserit | clepserit | — |
| Exod.22.1 | mactaveritque | mactaueritque | — |
| Exod.22.1 | boves | boues | bones |
| Exod.22.2 | homicidii | homicidii | homkidii |
| Exod.22.3 | pœna | pœna | pcena |
| Exod.22.5 | fundum | fundum | ftindum |
| Exod.22.5 | vineam | vineam | — |
| Exod.22.5 | alterius | alterius | — |
| Exod.22.7 | supellectilemve | supellectilemue | fupelledtilemue |
| Exod.22.8 | Sin | sin | in |
| Exod.22.8 | interverterit | interuerterit | — |
| Exod.22.9 | bove | boue | bone |
| Exod.22.9 | ove | oue | one |
| Exod.22.9 | condemnaverint | condemnauerint | condenmauerint |
| Exod.22.9 | alteri | alteri | — |
| Exod.22.10 | nullo | nullo | nulio |
| Exod.22.10 | fractum | fractum | fvaclum |
| Exod.22.10 | abactum | abactum | cium |
| Exod.22.11 | Jovæ | Iouæ | loux |
| Exod.22.11 | illum | illum | ilium |
| Exod.22.11 | satisfactionem | satisfactionem | fatisfaftionem |
| Exod.22.12 | præstato | præstato | prxftato |
| Exod.22.13 | præstato | præstato | prxftato |
| Exod.22.14 | fractum | fractum | fraction |
| Exod.22.14 | præstato | præstato | prxfiato |
| Exod.22.15 | præsente | præsente | prxfente |
| Exod.22.15 | conductitium | conductitium | conduclitium |
| Exod.22.15 | addictum | addictum | addittum |
| Exod.22.16 | virginem | virginem | virgiuem |
| Exod.22.17 | puellæ | puellæ | puellx |
| Exod.22.20 | Jovæ | Iouæ | louae |
| Exod.22.22 | pupillum | pupillum | pupilium |
| Exod.22.23 | quum | quum | quuni |
| Exod.22.24 | conjuges | coniuges | — |
| Exod.22.24 | viduæ | viduæ | — |
| Exod.22.24 | liberi | liberi | — |
| Exod.22.25 | mutuaveris | mutuaueris | mutuaucris |
| Exod.22.25 | praebeto | praebeto | prxbeto |
| Exod.22.27 | cuticulae | cuticulae | cuticulx |
| Exod.22.27 | amictum | amictum | ainictum |
| Exod.22.27 | recubet | recubet | rccubet |
| Exod.22.29 | dato | dato | dafo |
| Exod.22.31 | Praestatote | Praestatote | Prxftatote |
| Exod.22.31 | projicitote | proiicitote | — |
| Exod.23.1 | Auditionem | Auditionem | — |
| Exod.23.1 | coito | coito | — |
| Exod.23.1 | sis | sis | is |
| Exod.23.2 | recto | recto | reclo |
| Exod.23.2 | sententiam | sententiam | fententiain |
| Exod.23.2 | deflectito | deflectito | defleclito |
| Exod.23.4 | bovem | bouem | boueiu |
| Exod.23.4 | asinumve | asinumue | afinunuie |
| Exod.23.5 | succubuisse | succubuisse | fuccubtiisfe |
| Exod.23.6 | jus | ius | iua |
| Exod.23.7 | interficito | interficito | — |
| Exod.23.7 | absolvam | absoluam | abfoluain |
| Exod.23.8 | donum | donum | domim |
| Exod.23.8 | caecat | caecat | exeat |
| Exod.23.9 | Ægypto | Ægypto | Aegytopto |
| Exod.23.12 | asinusque | asinusque | alinusque |
| Exod.23.15 | præcepi | præcepi | prxcepi |
| Exod.23.16 | severis | seueris | — |
| Exod.23.17 | conspectum | conspectum | — |
| Exod.23.17 | Jovæ | Iouæ | louae |
| Exod.23.18 | Quum | Quum | — |
| Exod.23.18 | victimæ | victimæ | — |
| Exod.23.18 | mactando | mactando | — |
| Exod.23.18 | pernoctato | pernoctato | pernoclato |
| Exod.23.19 | Jovæ | Iouæ | louse |
| Exod.23.19 | Hædum | Hædum | Hacdum |
| Exod.23.19 | lacte | lacte | lade |
| Exod.23.20 | præmissurus | præmissurus | prarmisfurus |
| Exod.23.20 | tueatur | tueatur | tucatur |
| Exod.23.20 | præparatum | præparatum | pracparatum |
| Exod.23.22 | perduellis | perduellis | perdueilis |
| Exod.23.23 | ductabit | ductabit | — |
| Exod.23.23 | Amorræos | Amorræos | Amomros |
| Exod.23.23 | Hettæos | Hettæos | Hettacos |
| Exod.23.23 | Hevaeos | Heuaeos | — |
| Exod.23.23 | Jebusæos | Iebusæos | — |
| Exod.23.23 | quos | quos | — |
| Exod.23.25 | Jovam | Iouam | louam |
| Exod.23.28 | Hevaeos | Heuaeos | — |
| Exod.23.28 | Chananæos | Chananæos | — |
| Exod.23.29 | agrestes | agrestes | agrefies |
| Exod.23.30 | foetifices | foetifices | fctifices |
| Exod.23.31 | Palaestino | Palaestino | Palaeitino |
| Exod.23.31 | flumine | flumine | — |
| Exod.23.31 | regionis | regionis | regionls |
| Exod.23.31 | conspectu | conspectu | — |
| Exod.23.32 | fœdus | fœdus | fcedus |
| Exod.23.33 | habitanto | habitanto | habitanro |
| Exod.24.2 | accesserat | accesserat | aceesferat |
| Exod.24.3 | eique | eique | eiqne |
| Exod.24.3 | Jovæ | Iouæ | louac |
| Exod.24.3 | facturum | facturum | — |
| Exod.24.3 | se | se | — |
| Exod.24.3 | Jova | Ioua | loua |
| Exod.24.4 | Jovæ | Iouæ | — |
| Exod.24.4 | dicta | dicta | dicla |
| Exod.24.4 | perscripsit | perscripsit | perfcripiit |
| Exod.24.4 | postridie | postridie | poliridie |
| Exod.24.5 | Israelitis | Israelitis | Israelites |
| Exod.24.5 | Jovæ | Iouæ | louae |
| Exod.24.7 | Sumptumque | sumptumque | fiimtumque |
| Exod.24.7 | se | se | fefc |
| Exod.24.7 | Jovæ | Iouæ | louac |
| Exod.24.7 | facturum | facturum | — |
| Exod.24.8 | sumpsit | sumpsit | — |
| Exod.24.8 | Hic | hic | hie |
| Exod.24.8 | Jova | Ioua | loua |
| Exod.24.9 | Israelitis | Israelitis | — |
| Exod.24.9 | adscenderant | adscenderant | adfeenderant |
| Exod.24.10 | similitudo | similitudo | iiiniikudo |
| Exod.24.10 | sapphirini | sapphirini | lapphirinj |
| Exod.24.10 | coctilis | coctilis | coctiiis |
| Exod.24.10 | speciesque | speciesque | fpeeksque |
| Exod.24.10 | cæli | cæli | cadi |
| Exod.24.11 | passi | passi | — |
| Exod.24.11 | primates | primates | — |
| Exod.24.11 | visoque | visoque | — |
| Exod.24.11 | Deo | Deo | — |
| Exod.24.11 | ceperunt | ceperunt | — |
| Exod.24.12 | Jova | Ioua | loua |
| Exod.24.13 | doctrinam | doctrinam | docTxinam |
| Exod.24.13 | Jova | Ioua | — |
| Exod.24.13 | disciplinam | disciplinam | — |
| Exod.24.13 | conscriptam | conscriptam | — |
| Exod.24.14 | praestolarentur | praestolarentur | prxftolarentur |
| Exod.24.14 | haberet | haberet | haberct |
| Exod.24.15 | adsumto | adsumto | — |
| Exod.24.15 | Josua | Iosua | — |
| Exod.24.15 | adscendit | adscendit | adfeendit |
| Exod.24.16 | Jovæ | Iouæ | — |
| Exod.24.16 | insedit | insedit | infedir |
| Exod.24.16 | obductum | obductum | obduelum |
| Exod.24.16 | Jova | Ioua | loua |
| Exod.24.17 | Jovæ | Iouæ | Ioux |
| Exod.24.18 | adscendit | adscendit | adfeendit |
| Exod.24.18 | noctes | noctes | — |
| Exod.25.1 | Jova | Ioua | — |
| Exod.25.1 | sic | sic | fie |
| Exod.25.2 | Dic | dic | die |
| Exod.25.2 | conferant | conferant | conteranf |
| Exod.25.2 | ultro | vltro | vitro |
| Exod.25.2 | conferent | conferent | conferenr |
| Exod.25.3 | æs | æs | — |
| Exod.25.4 | Hyacinthum | Hyacinthum | — |
| Exod.25.5 | Pelles | Pelles | — |
| Exod.25.5 | arietinas | arietinas | — |
| Exod.25.5 | pelles | pelles | peiles |
| Exod.25.6 | lucernarium | lucernarium | lu |
| Exod.25.6 | aromata | aromata | cernarium |
| Exod.25.6 | unctorium | vnctorium | vnciorium |
| Exod.25.6 | suffimenta | suffimenta | fumVuenta |
| Exod.25.7 | Gemmas | gemmas | geramas |
| Exod.25.7 | caelaturae | caelaturae | — |
| Exod.25.7 | monile | monile | — |
| Exod.25.8 | sanctuarium | sanctuarium | — |
| Exod.25.9 | sicut | sicut | lkut |
| Exod.25.10 | arca | arca | area |
| Exod.25.10 | lignis | lignis | ignis |
| Exod.25.10 | longitudinem | longitudinem | longitudincm |
| Exod.25.10 | duorum | duorum | dnorura |
| Exod.25.10 | latitudinem | latitudinem | — |
| Exod.25.10 | sesquicubitalem | sesquicubitalem | — |
| Exod.25.10 | tantundemque | tantundemque | — |
| Exod.25.12 | quatuor | quatuor | quatnor |
| Exod.25.12 | annulos | annulos | annnlos |
| Exod.25.12 | aureos | aureos | anreos |
| Exod.25.12 | quatuor | quatuor | quatnor |
| Exod.25.12 | applicabis | applicabis | — |
| Exod.25.13 | Vectesque | Vectesque | — |
| Exod.25.13 | inaurato | inaurato | inaura |
| Exod.25.14 | annulos | annulos | annnlos |
| Exod.25.14 | arcæ | arcæ | arcs |
| Exod.25.14 | portandam | portandam | portandani |
| Exod.25.15 | annulis | annulis | — |
| Exod.25.15 | arcæ | arcæ | — |
| Exod.25.15 | haereant | haereant | — |
| Exod.25.16 | arca | arca | area |
| Exod.25.16 | tradam | tradam | — |
| Exod.25.16 | ponito | ponito | — |
| Exod.25.17 | Propitiatorium | Propitiatorium | — |
| Exod.25.17 | duorum | duorum | duoriun |
| Exod.25.18 | altero | altero | alQtero |
| Exod.25.18 | extremo | extremo | cxtremo |
| Exod.25.20 | Qui | qui | oqui |
| Exod.25.20 | expansis | expansis | expands |
| Exod.25.20 | alterius | alterius | — |
| Exod.25.21 | arcæ | arcæ | — |
| Exod.25.21 | desuper | desuper | — |
| Exod.25.21 | posito | posito | polito |
| Exod.25.21 | arca | arca | area |
| Exod.25.21 | oraculo | oraculo | oraeulo |
| Exod.25.22 | arcæ | arcæ | arcs |
| Exod.25.22 | præcipiam | præcipiam | — |
| Exod.25.23 | bicubitali | bicubitali | bknbitali |
| Exod.25.25 | applicabis | applicabis | adtfplicabis |
| Exod.25.26 | annulos | annulos | annnlos |
| Exod.25.27 | marginem | marginem | marginern |
| Exod.25.27 | vectibus | vectibus | veclibns |
| Exod.25.29 | libetur | libetur | libernr |
| Exod.25.30 | mensae | mensae | menfx |
| Exod.25.30 | panem | panem | panemgo |
| Exod.25.31 | puro | puro | — |
| Exod.25.31 | facito | facito | — |
| Exod.25.31 | crus | crus | cms |
| Exod.25.31 | scapi | scapi | feapi |
| Exod.25.33 | putaminis | putaminis | putaininisamyg |
| Exod.25.33 | amygdali | amygdali | dali |
| Exod.25.33 | totidemque | totidemque | totidemqtic |
| Exod.25.34 | concavae | concauae | concaus |
| Exod.25.34 | scutulae | scutulae | fcutulx |
| Exod.25.34 | lilia | lilia | — |
| Exod.25.35 | subter | subter | — |
| Exod.25.36 | candelabro | candelabro | candelabra |
| Exod.25.37 | accensis | accensis | aceenfis |
| Exod.25.37 | se | se | feluceat |
| Exod.25.37 | luceat | luceat | earum |
| Exod.25.38 | Earumque | Earumque | que |
| Exod.25.39 | candelabro | candelabro | — |
| Exod.26.1 | decem | decem | decern |
| Exod.26.1 | picturata | picturata | pichirata |
| Exod.26.2 | octo | octo | oclo |
| Exod.26.2 | latitudo | latitudo | iatitudo |
| Exod.26.4 | ligulas | ligulas | hya |
| Exod.26.4 | hyacinthinas | hyacinthinas | cinthinas |
| Exod.26.4 | commissurae | commissurae | commisfurx |
| Exod.26.6 | aureos | aureos | — |
| Exod.26.6 | se | se | fc |
| Exod.26.6 | connectes | connectes | conneiites |
| Exod.26.7 | velleribus | velleribus | vellcribus |
| Exod.26.7 | contegendum | contegendum | — |
| Exod.26.7 | tabernaculum | tabernaculum | — |
| Exod.26.8 | longitudinem | longitudinem | long |
| Exod.26.8 | trigenum | trigenum | mdincm |
| Exod.26.8 | cubitorum | cubitorum | trigenumcubitorum |
| Exod.26.8 | latitudinem | latitudinem | ititudinein |
| Exod.26.9 | conjunges | coniunges | — |
| Exod.26.9 | sextumque | sextumque | — |
| Exod.26.9 | tabernaculi | tabernaculi | — |
| Exod.26.9 | replicabis | replicabis | — |
| Exod.26.10 | Præterea | Præterea | — |
| Exod.26.10 | commissurae | commissurae | commisfura |
| Exod.26.11 | factos | factos | — |
| Exod.26.11 | ære | ære | sere |
| Exod.26.11 | copulabis | Copulabis | Ilcopulabis |
| Exod.26.13 | redundabunt | redundabunt | redundabtmt |
| Exod.26.14 | arietinis | arietinis | — |
| Exod.26.14 | rubro | rubro | — |
| Exod.26.14 | tinctis | tinctis | — |
| Exod.26.15 | tabernaculum | tabernaculum | — |
| Exod.26.15 | arrectarios | arrectarios | airedarios |
| Exod.26.16 | latitudine | latitudine | — |
| Exod.26.17 | mutuo | Mutuo | Igmutuo |
| Exod.26.17 | cohaerentes | cohaerentes | coharentes |
| Exod.26.18 | viginti | viginti | viginri |
| Exod.26.18 | tabernaculi | tabernaculi | taberionacidi |
| Exod.26.20 | singulas | singulas | iingulas |
| Exod.26.20 | pro | pro | pronumero |
| Exod.26.20 | numero | numero | at |
| Exod.26.21 | Totidemque | totidemque | tctidemque |
| Exod.26.21 | aquilonari | aquilonari | aaiquilonari |
| Exod.26.23 | utraque | vtraque | vtraqueangulari |
| Exod.26.23 | angulari | angulari | ta |
| Exod.26.23 | tabernaculi | tabernaculi | bernacuii |
| Exod.26.25 | octo | octo | — |
| Exod.26.25 | argenteae | argenteae | argentea |
| Exod.26.25 | spirae | spirae | fpira |
| Exod.26.25 | singulis | singulis | — |
| Exod.26.25 | binae | binae | — |
| Exod.26.26 | Præterea | Præterea | — |
| Exod.26.26 | cedrina | cedrina | cednna |
| Exod.26.28 | trajectum | traiectum | traiedhim |
| Exod.26.28 | utrumque | vtrumque | zovtrumque |
| Exod.26.29 | inaurato | inaurato | maurato |
| Exod.26.30 | erigito | erigito | — |
| Exod.26.31 | iterato | iterato | — |
| Exod.26.31 | bysso | bysso | — |
| Exod.26.31 | phrygionis | phrygionis | pnrygionis |
| Exod.26.32 | appendes | appendes | aripendes |
| Exod.26.32 | quatuor | quatuor | quatu |
| Exod.26.32 | cedrinis | cedrinis | orcedrinis |
| Exod.26.32 | columnis | columnis | column |
| Exod.26.32 | auro | auro | — |
| Exod.26.32 | opertis | opertis | auroopertis |
| Exod.26.32 | capitellis | capitellis | capneihs |
| Exod.26.32 | aureis | aureis | auieis |
| Exod.26.32 | basibus | basibus | balibus |
| Exod.26.33 | suspendito | suspendito | fuspeudito |
| Exod.26.33 | oraculi | oraculi | oracuh |
| Exod.26.33 | sanctuarium | sanctuarium | fancluarium |
| Exod.26.33 | sanctiore | sanctiore | fanchore |
| Exod.26.34 | propitiatorium | propitiatorium | — |
| Exod.26.34 | arcæ | arcæ | — |
| Exod.26.34 | oraculi | oraculi | — |
| Exod.26.35 | regione | regione | — |
| Exod.26.35 | mensae | mensae | — |
| Exod.26.35 | meridianum | meridianum | nieridianum |
| Exod.26.36 | aulaeum | aulaeum | — |
| Exod.26.37 | aulaeum | aulaeum | — |
| Exod.26.37 | quinque | quinque | — |
| Exod.26.37 | illitas | illitas | — |
| Exod.26.37 | capitellis | capitellis | — |
| Exod.26.37 | ære | ære | sere |
| Exod.27.1 | altam | altam | aJtam |
| Exod.27.2 | angulis | angulis | anguhs |
| Exod.27.2 | ære | ære | are |
| Exod.27.3 | vasa | vasa | — |
| Exod.27.3 | ære | ære | — |
| Exod.27.4 | focum | focum | tocum |
| Exod.27.4 | ære | ære | aire |
| Exod.27.4 | cancellis | cancellis | cancelhs |
| Exod.27.4 | aereos | aereos | aieos |
| Exod.27.5 | aræ | aræ | arac |
| Exod.27.5 | contracturam | contracturam | contrafturam |
| Exod.27.5 | collocato | collocato | coliocato |
| Exod.27.5 | aræ | aræ | ara |
| Exod.27.6 | Præterea | Præterea | Praterea |
| Exod.27.6 | vectes | vectes | vedtes |
| Exod.27.6 | ære | ære | — |
| Exod.27.6 | superinductos | superinductos | — |
| Exod.27.7 | haereant | haereant | hxreant |
| Exod.27.7 | aræ | aræ | arx |
| Exod.27.8 | monstratum | monstratum | raonftratum |
| Exod.27.9 | atrium | atrium | a |
| Exod.27.9 | tabernaculi | tabernaculi | riumtabernaaili |
| Exod.27.9 | unius | vnius | vnins |
| Exod.27.9 | longitudinem | longitudinem | — |
| Exod.27.10 | Columnæ | columnæ | columns |
| Exod.27.10 | aereis | aereis | xreis |
| Exod.27.10 | capitellis | capitellis | capittllis |
| Exod.27.10 | praecinctionibus | praecinctionibus | prxcinetionibus |
| Exod.27.11 | Eodemque | eodemque | eodcmque |
| Exod.27.11 | longitudinem | longitudinem | lonagitudinein |
| Exod.27.12 | latitudinem | latitudinem | latitudimm |
| Exod.27.12 | occidentali | occidentali | occidental |
| Exod.27.12 | columnæ | columnæ | — |
| Exod.27.12 | decem | decem | — |
| Exod.27.12 | totidemque | totidemque | — |
| Exod.27.13 | latitudinem | Latitudinem | Iaticudinem |
| Exod.27.15 | columnæ | columnæ | colunmx |
| Exod.27.15 | ternae | ternae | ternx |
| Exod.27.16 | aulaeum | aulaeum | aulxum |
| Exod.27.16 | hyacintho | hyacintho | — |
| Exod.27.16 | purpura | purpura | — |
| Exod.27.16 | cocco | cocco | — |
| Exod.27.16 | iterato | iterato | — |
| Exod.27.16 | bilice | bilice | ilice |
| Exod.27.16 | columnæ | columnæ | columnx |
| Exod.27.17 | columnæ | columnæ | — |
| Exod.27.17 | praecinctiones | praecinctiones | prxcinchones |
| Exod.27.17 | aereas | aereas | xreas |
| Exod.27.18 | cubitorum | cubitorum | — |
| Exod.27.18 | latitudo | latitudo | — |
| Exod.27.18 | altitudo | altitudo | altituuo |
| Exod.27.18 | aereis | aereis | xreis |
| Exod.27.19 | aedis | aedis | xdis |
| Exod.27.19 | ministerium | ministerium | minilterium |
| Exod.27.19 | aedis | aedis | — |
| Exod.27.19 | ære | ære | xre |
| Exod.27.20 | præcipito | præcipito | pracipito |
| Exod.27.20 | illucendum | illucendum | — |
| Exod.27.20 | accendendas | accendendas | — |
| Exod.27.21 | tabernaculo | tabernaculo | tabemaculo |
| Exod.27.21 | siparium | siparium | liparium |
| Exod.27.21 | Jovam | Iouam | louam |
| Exod.27.21 | posteris | posteris | pofieris |
| Exod.28.2 | Ipsique | Ipsique | — |
| Exod.28.2 | sacras | sacras | lacras |
| Exod.28.2 | vestes | vestes | vefies |
| Exod.28.3 | præditis | præditis | prrditis |
| Exod.28.4 | praetexta | praetexta | prxtexta |
| Exod.28.4 | cinctus | cinctus | cinchis |
| Exod.28.5 | byssum | byssum | bysfuoi |
| Exod.28.7 | conjunctum | coniunctum | coniunchim |
| Exod.28.10 | Videlicet | Videlicet | — |
| Exod.28.10 | ætatis | ætatis | xtatis |
| Exod.28.11 | Easque | Easque | — |
| Exod.28.11 | cælato | cælato | — |
| Exod.28.11 | caelatura | caelatura | cxlatura |
| Exod.28.12 | Eas | Eas | Ens |
| Exod.28.12 | humeris | humeris | humcris |
| Exod.28.12 | suis | suis | fiiis |
| Exod.28.12 | Jovam | Iouam | louam |
| Exod.28.13 | Circulos | Circulos | — |
| Exod.28.14 | auro | auro | aitro |
| Exod.28.15 | judiciale | iudiciale | iudiciaIe |
| Exod.28.15 | sicut | sicut | flcut |
| Exod.28.16 | Quadratum | Quadratum | — |
| Exod.28.16 | longitudine | longitudine | — |
| Exod.28.16 | latitudine | latitudine | — |
| Exod.28.16 | palmi | palmi | — |
| Exod.28.17 | completo | completo | complete |
| Exod.28.18 | secundo | secundo | infecundo |
| Exod.28.19 | ligyrius | ligyrius | — |
| Exod.28.19 | achates | achates | — |
| Exod.28.21 | numero | numero | nnmero |
| Exod.28.21 | caelentur | caelentur | caelenaatur |
| Exod.28.21 | sigillis | sigillis | — |
| Exod.28.23 | Præterea | Præterea | Pneterea |
| Exod.28.26 | annulos | annulos | anmilos |
| Exod.28.26 | interius | interius | interim |
| Exod.28.27 | commissura | commissura | coniniisfura |
| Exod.28.27 | texturam | texturam | — |
| Exod.28.28 | alligetur | alligetur | — |
| Exod.28.28 | ephodi | ephodi | — |
| Exod.28.29 | monili | monili | month |
| Exod.28.29 | pectori | pectori | — |
| Exod.28.29 | suo | suo | — |
| Exod.28.29 | applicata | applicata | — |
| Exod.28.29 | sanctuarium | sanctuarium | — |
| Exod.28.29 | intrabit | intrabit | — |
| Exod.28.29 | Jovæ | Iouæ | louse |
| Exod.28.30 | CLARITAS | CLARITAS | — |
| Exod.28.30 | INTEGRITAS | INTEGRITAS | — |
| Exod.28.30 | pectus | pectus | — |
| Exod.28.30 | quandocumque | quandocumque | — |
| Exod.28.30 | Jovæ | Iouæ | — |
| Exod.28.30 | conspectum | conspectum | — |
| Exod.28.30 | veniet | veniet | — |
| Exod.28.30 | conspectu | conspectu | confpedtu |
| Exod.28.30 | Jovæ | Iouæ | loux |
| Exod.28.33 | lacinia | lacinia | laciniamala |
| Exod.28.33 | mala | mala | puni |
| Exod.28.33 | punica | punica | ca |
| Exod.28.34 | hyacintho | hyacintho | — |
| Exod.28.35 | sive | siue | fine |
| Exod.28.35 | Jovam | Iouam | louam |
| Exod.28.39 | infulam | infulam | — |
| Exod.28.39 | byssinam | byssinam | — |
| Exod.28.39 | cincturam | cincturam | — |
| Exod.28.40 | cincturasque | cincturasque | cinclurasque |
| Exod.28.43 | pœnas | pœnas | pecnas |
| Exod.29.1 | duos | duos | duaos |
| Exod.29.2 | subactas | subactas | fubaetas |
| Exod.29.4 | adductos | adductos | — |
| Exod.29.5 | sumptis | sumptis | funitis |
| Exod.29.5 | praetextam | praetextam | prxtextam |
| Exod.29.5 | ephodi | ephodi | — |
| Exod.29.5 | amicito | amicito | — |
| Exod.29.6 | infulam | infulam | infulain |
| Exod.29.6 | infulae | infulae | — |
| Exod.29.6 | coronam | coronam | — |
| Exod.29.6 | sacram | sacram | — |
| Exod.29.7 | unctorio | vnctorio | — |
| Exod.29.8 | vestito | vestito | vertito |
| Exod.29.10 | suas | suas | fuasimi |
| Exod.29.10 | imposuerint | imposuerint | pofuerint |
| Exod.29.11 | conspectu | conspectu | — |
| Exod.29.11 | Jovæ | Iouæ | — |
| Exod.29.11 | tabernaculi | tabernaculi | — |
| Exod.29.11 | mactato | mactato | — |
| Exod.29.12 | digito | digito | — |
| Exod.29.12 | invergito | inuergito | infpergito |
| Exod.29.13 | inhaerentem | inhaerentem | inhxrentem |
| Exod.29.14 | cremato | cremato | cremajo |
| Exod.29.14 | piaculum | piaculum | — |
| Exod.29.17 | ponito | Ponito | Jponito |
| Exod.29.18 | victimæ | victimæ | — |
| Exod.29.18 | solida | solida | — |
| Exod.29.18 | crematio | crematio | — |
| Exod.29.18 | Jovæ | Iouæ | — |
| Exod.29.18 | suavi | suaui | — |
| Exod.29.18 | odore | odore | — |
| Exod.29.18 | deliniat | deliniat | — |
| Exod.29.20 | Mactato | Mactato | — |
| Exod.29.20 | auriculam | auriculam | auricidam |
| Exod.29.20 | pedumque | pedumque | pediimque |
| Exod.29.21 | oleo | oleo | — |
| Exod.29.21 | unctorio | vnctorio | — |
| Exod.29.21 | eorum | eorum | eornm |
| Exod.29.22 | adhaerentem | adhaerentem | adhxrentem |
| Exod.29.23 | Jovæ | Iouæ | loux |
| Exod.29.24 | Jovæ | Iouæ | loux |
| Exod.29.25 | victimam | victimam | viclimam |
| Exod.29.25 | Jovæ | Iouæ | loux |
| Exod.29.26 | sumito | sumito | — |
| Exod.29.26 | pectusculum | pectusculum | — |
| Exod.29.26 | Jovæ | Iouæ | loux |
| Exod.29.26 | portionem | portionem | portioncm |
| Exod.29.27 | Consacratoque | Consacratoque | — |
| Exod.29.27 | pectusculum | pectusculum | — |
| Exod.29.27 | porrectitium | porrectitium | — |
| Exod.29.27 | armum | armum | annum |
| Exod.29.27 | porrectum | porrectum | porreftum |
| Exod.29.27 | filiorum | filiorum | filionuu |
| Exod.29.28 | æterna | æterna | xterna |
| Exod.29.28 | eorum | eorum | — |
| Exod.29.28 | salute | salute | — |
| Exod.29.28 | susceptis | susceptis | — |
| Exod.29.28 | Jovæ | Iouæ | — |
| Exod.29.28 | destinabitur | destinabitur | — |
| Exod.29.29 | Vestes | Vestes | — |
| Exod.29.29 | sacrae | sacrae | — |
| Exod.29.30 | eas | eas | cas |
| Exod.29.30 | intraturus | intraturus | — |
| Exod.29.31 | initiatorium | initiatorium | — |
| Exod.29.31 | sacro | sacro | gafacro |
| Exod.29.32 | nec | nec | nee |
| Exod.29.32 | comedunto | comedunto | comcdunto |
| Exod.29.33 | manus | manus | nianus |
| Exod.29.33 | consecrandorum | consecrandorum | confeerandorum |
| Exod.29.34 | sacrum | sacrum | facnun |
| Exod.29.35 | præcipio | præcipio | pnecipio |
| Exod.29.35 | initiato | initiato | inltlato |
| Exod.29.37 | sacrosancta | sacrosancta | — |
| Exod.29.38 | procurato | procurato | procurator |
| Exod.29.40 | decimam | decimam | decimara |
| Exod.29.41 | libationem | Libationem | Iibationem |
| Exod.29.41 | divinæ | diuinæ | diuinx |
| Exod.29.42 | hic | hic | — |
| Exod.29.42 | solidi | solidi | — |
| Exod.29.42 | te | te | — |
| Exod.29.42 | affando | affando | — |
| Exod.29.45 | meque | meque | nieque |
| Exod.29.46 | illum | illum | ilium |
| Exod.29.46 | educti | educti | — |
| Exod.29.46 | eorum | eorum | — |
| Exod.30.1 | cedrinam | cedrinam | cedrinara |
| Exod.30.2 | latitudine | latitudine | — |
| Exod.30.2 | cubitali | cubitali | — |
| Exod.30.4 | affigito | affigito | adngito |
| Exod.30.4 | vectes | vectes | vecles |
| Exod.30.5 | vectes | vectes | vecles |
| Exod.30.6 | siparium | siparium | — |
| Exod.30.9 | alienum | alienum | alienump |
| Exod.30.10 | sacrosanctum | sacrosanctum | facrofanclum |
| Exod.30.12 | habebis | habebis | — |
| Exod.30.12 | censu | censu | cenfti |
| Exod.30.12 | cladis | cladis | eladis |
| Exod.30.14 | defungantur | defungantur | — |
| Exod.30.14 | qui | qui | — |
| Exod.30.14 | vigesimum | vigesimum | — |
| Exod.30.14 | ætatis | ætatis | — |
| Exod.30.15 | Jovam | Iouam | — |
| Exod.30.15 | collatione | collatione | — |
| Exod.30.16 | oracularis | oracularis | — |
| Exod.30.16 | proposito | proposito | — |
| Exod.30.16 | eo | eo | — |
| Exod.30.16 | vitæ | vitæ | vkx |
| Exod.30.17 | aereum | aereum | cereum |
| Exod.30.18 | aereo | aereo | sereo |
| Exod.30.19 | abluant | abluant | — |
| Exod.30.21 | sese | sese | — |
| Exod.30.21 | avertant | auertant | — |
| Exod.30.21 | æternum | æternum | — |
| Exod.30.22 | Præterea | Præterea | Prxterea |
| Exod.30.22 | primæ | primæ | prima |
| Exod.30.22 | notae | notae | notx |
| Exod.30.23 | ingenuae | ingenuae | ingenux |
| Exod.30.23 | siclos | siclos | fidos |
| Exod.30.23 | ducentos | ducentos | ducenlos |
| Exod.30.24 | præterea | præterea | prxterea |
| Exod.30.25 | sacrae | sacrae | — |
| Exod.30.25 | unctionis | vnctionis | — |
| Exod.30.25 | confectura | confectura | confefhira |
| Exod.30.25 | unguentaria | vnguentaria | vngueutaria |
| Exod.30.28 | victimariam | victimariam | vidiimariam |
| Exod.30.28 | labrumque | labrumque | labrvimque |
| Exod.30.29 | sacrosancta | sacrosancta | facrofancla |
| Exod.30.33 | concinnaverit | concinnauerit | concinnauerir |
| Exod.30.33 | alienum | alienum | alienwm |
| Exod.30.34 | stacten | stacten | — |
| Exod.30.34 | odoratum | odoratum | odoratutn |
| Exod.30.35 | unguentaria | vnguentaria | vngueutaria |
| Exod.30.36 | eo | eo | — |
| Exod.30.36 | sacrosanctum | sacrosanctum | facrofantfhim |
| Exod.30.37 | suffimen | suffimen | fufHmen |
| Exod.30.38 | Qui | Qui | — |
| Exod.30.38 | suaveolentiam | suaueolentiam | — |

## Punctuation not from the OCR (55)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

21.3 *venit,*; 21.10 *victu,*; 21.10 *vestitu,*; 21.34 *præstato,*; 22.1 *clepserit,*; 22.10 *fractum,*; 22.31 *proiicitote.*; 23.18 *sanguinem,*; 23.23 *Amorræos,*; 23.23 *Iebusæos,*; 23.31 *Palaestino,*; 23.31 *flumine.*; 24.3 *respondit,*; 24.10 *coctilis,*; 24.11 *primates,*; 24.11 *ceperunt.*; 24.18 *noctes.*; 25.2 *conferent.*; 25.3 *æs,*; 25.6 *lucernarium,*; 25.7 *monile:*; 25.10 *sesquicubitalem,*; 25.12 *applicabis:*; 25.15 *haereant,*; 25.16 *tradam,*; 25.16 *ponito.*; 25.21 *oraculo,*; 25.31 *facito,*; 25.31 *crus,*; 25.34 *lilia:*; 25.37 *luceat,*; 26.9 *coniunges,*; 26.9 *replicabis.*; 26.25 *binae.*; 26.32 *columnis,*; 26.32 *opertis,*; 26.37 *illitas,*; 27.10 *aereis,*; 27.12 *decem,*; 27.16 *aulaeum,*; 27.16 *hyacintho,*; 27.16 *purpura,*; 27.18 *cubitorum,*; 27.20 *illucendum,*; 28.17 *completo.*; 28.19 *ligyrius,*; 28.21 *sigillis.*; 28.27 *texturam:*; 28.28 *alligetur,*; 28.30 *habeat,*; 28.39 *byssinam,*; 29.20 *Mactato:*; 29.28 *destinabitur.*; 29.38 *procurato:*; 29.46 *eorum.*

## Paragraphs (11 inside the chapters)

1738 runs its verses on and marks a paragraph by indenting its first line. Read from the hOCR (`archive.indents`: a line starting 40–140 px inside the column's margin after a line that ends a sentence; drop capitals, summaries and 1738's footnotes left out) and set before the word that begins the line; a paragraph read on the page is a `¶` row in `data/decisions/Exod.orig.tsv`. Every chapter also begins one. Leaf = archive.org's hOCR page (its image is page n<leaf − 1>).

24.8 *Et* (leaf 138, line 43); 25.23 *Item* (leaf 139, line 38); 25.31 *Item* (leaf 139, line 57); 26.31 *Item* (leaf 140, line 61); 27.9 *Item* (leaf 141, line 10); 28.6 *Ephodum* (leaf 141, line 77); 28.15 *Facito* (leaf 142, line 6); 28.36 *Item* (leaf 142, line 71); 29.38 *Hæc* (leaf 144, line 30); 30.11 *Item* (leaf 144, line 97); 30.17 *Item* (leaf 145, line 15)

## Open questions

1. **Accents.** 1738 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1738 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's G. … H. (and L., G.L.) marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
