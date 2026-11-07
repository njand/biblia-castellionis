# The settled chapters against 1573

Proposed 2026-11-07. Your settled New Testament chapters (Matthew 1–13, Mark 1–5, Luke 1–13, John 1–4; Matthew 14–28
had its own stage 2) collated word by word against 1573, the NT base (decision 24), and the other printings
(`python -m pipeline collate BOOK CH-CH --base settled`; `data/calibration/<book><chapters>-collation.tsv`). Every
place below was **read on the 1573 page image** (MDZ bsb10141277, canvas given; crops in `sources/mdz-1573/crops/`).
1556 is cited where its OCR could be aligned there. At most of these places your text agrees with Wikisource, so
decision 23 (your text against Wikisource) could not see them; this is the same blind spot as Luke's *jūris perītus*.
New words carry macrons from `latin macron` (W/M, Gaffiot).

Each **Apply** line is an exact replacement inside that verse of `text/*.usfm`, checked to match once. Answer each
group's **Decision:** with *accept*, *accept all except N, M*, or *accept N, M*; then
`python -m pipeline review apply data/review/settled-1573.md --write`.

## 1. Words missing or wrong: 1573 and the other printings agree against your text (22)

Slips in Wikisource that your text inherited: a word dropped or misprinted, a case or person that does not construe.

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 1:23** *lātūra est, ēditūra* → *lātūra est, et ēditūra*. **1573** (canvas 749, page image): *& editura*.
   Printings: 1573, 1758, 1715, 1750; your text: Wikisource.
   **Apply:** `Matt.1.23` la: `lātūra est, ēditūra` → `lātūra est, et ēditūra`
2. **Matt 2:13** *inquit, “assūmptō* → *inquit, “et assūmptō*. **1573** (canvas 750, page image): *inquit, & aſſumpto*.
   Printings: 1573, 1758, 1715, 1747; your text: Wikisource.
   **Apply:** `Matt.2.13` la: `inquit, “assūm­ptō` → `inquit, “et assūm­ptō` (the soft hyphen kept)
3. **Matt 9:16** *atque it dēterior* → *atque ita dēterior*. **1573** (canvas 757, page image): *atque ita deterior* (top of the next page).
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Matt.9.16` la: `atque it dēterior` → `atque ita dēterior`
4. **Matt 10:34** *conciliātum pācem in terrīs, sed bellum* → *conciliātum pācem, sed bellum*. **1573** (canvas 758, page image): *non veni conciliatum pacem, ſed bellum*: the second *in terris* is not there.
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Matt.10.34` la: `conciliātum pācem in terrīs, sed bellum` → `conciliātum pācem, sed bellum`
5. **Matt 12:48** *eī, quid id sibi* → *eī, quī id sibi*. **1573** (canvas 760, page image): *At ille ei, qui id ſibi dixerat*: “to him who had said it”.
   Printings: 1573, 1758; your text: Wikisource.
   **Apply:** `Matt.12.48` la: `eī, quid id sibi` → `eī, quī id sibi`
6. **Matt 13:10** *Tum cum hīs* → *Tum eum hīs*. **1573** (canvas 761, page image): *Tum eum his verbis conuenerunt*: “they came to him”.
   Printings: 1573, 1556, 1758, 1715, 1747, 1750; your text: Wikisource.
   **Apply:** `Matt.13.10` la: `Tum cum hīs` → `Tum eum hīs`
7. **Mark 2:19** *habent mēcum spōnsum* → *habent sēcum spōnsum*. **1573** (canvas 776, page image): *Quandiu habent ſecum ſponſum*: “with them”, as the Vulgate *habent secum sponsum*.
   Printings: 1573, 1758; your text: Wikisource.
   **Apply:** `Mark.2.19` la: `habent mēcum spōnsum` → `habent sēcum spōnsum`
8. **Mark 5:14** *videndum quod accidisset* → *videndum quid accidisset*. **1573** (canvas 778, page image): *ad videndum quid accidiſſet*: an indirect question.
   Printings: 1573, 1715, 1747; your text: Wikisource.
   **Apply:** `Mark.5.14` la: `videndum quod accidisset` → `videndum quid accidisset`
9. **Mark 5:31** *tē turbā premī* → *tē ā turbā premī*. **1573** (canvas 778, page image): *Vides te à turba premi*.
   Printings: 1573, 1758, 1715; your text: Wikisource.
   **Apply:** `Mark.5.31` la: `tē turbā premī` → `tē ā turbā premī`
10. **Luke 1:76** *Et puer Suprēmī* → *Et tū puer Suprēmī*. **1573** (canvas 790, page image): *Et tu puer Supremi*.
   Printings: 1573, 1556, 1758, 1715, 1747, 1750 (every printing); your text: Wikisource.
   **Apply:** `Luke.1.76` la: `Et puer Suprēmī` → `Et tū puer Suprēmī`
11. **Luke 2:28** *ipse cum suīs* → *ipse eum suīs*. **1573** (canvas 791, page image): *ipſe eum ſuis vlnis excepit*: “took him in his arms”.
   Printings: 1573, 1758, 1747, 1750; your text: Wikisource.
   **Apply:** `Luke.2.28` la: `ipse cum suīs` → `ipse eum suīs`
12. **Luke 4:1** *reversus est Jordāne* → *reversus est ā Jordāne*. **1573** (canvas 792, page image): *reuerſus eſt à Iordane*.
   Printings: 1573, 1750; your text: Wikisource.
   **Apply:** `Luke.4.1` la: `reversus est Jordāne` → `reversus est ā Jordāne`
13. **Luke 4:27** *pūrgātus et,* → *pūrgātus est,*. **1573** (canvas 793, page image): *purgatus eſt*.
   Printings: 1573, 1758, 1747; your text: Wikisource.
   **Apply:** `Luke.4.27` la: `pūrgātus et,` → `pūrgātus est,`
14. **Luke 6:12** *et per nox ōrāvit* → *et pernox ōrāvit*. **1573** (canvas 794, page image): *& pernox orauit*: *pernox*, “all night” (Gaffiot *pernox, octis*).
   Printings: 1573, 1758, 1715, 1747, 1750, 1681 (every printing); your text: Wikisource.
   **Apply:** `Luke.6.12` la: `et per nox ōrāvit` → `et pernox ōrāvit`
15. **Luke 7:11** *ut proficīsceret in* → *ut proficīscerētur in*. **1573** (canvas 795, page image): *vt proficiſceretur*: the verb is deponent.
   Printings: 1573, 1556, 1758, 1750; your text: Wikisource.
   **Apply:** `Luke.7.11` la: `ut proficīsceret in` → `ut proficīscerētur in`
16. **Luke 8:25** *ut eī obœdient?* → *ut eī obœdiant?*. **1573** (canvas 797, page image): *vt ei obediant*: subjunctive after *ut*.
   Printings: 1573, 1758, 1681; your text: Wikisource.
   **Apply:** `Luke.8.25` la: `ut eī obœdient?` → `ut eī obœdiant?`
17. **Luke 8:52** *esse, sē dormīre.* → *esse, sed dormīre.*. **1573** (canvas 797, page image): *non enim mortuam eſſe, ſed dormire*.
   Printings: 1573, 1758, 1747, 1750; your text: Wikisource.
   **Apply:** `Luke.8.52` la: `esse, sē dormīre.` → `esse, sed dormīre.`
18. **Luke 9:21** *vērō eī interminātus* → *vērō iīs interminātus*. **1573** (canvas 798, page image): *Ille verò eis interminatus eſt, præcepitq; ne cui id dicerent*: the plural, as *dīcerent*.
   Printings: 1573, 1750; your text: Wikisource.
   **Apply:** `Luke.9.21` la: `vērō eī interminātus` → `vērō iīs interminātus`
19. **Luke 11:17** *super domus cadit* → *super domum cadit*. **1573** (canvas 800, page image): *& domus ſuper domum cadit*.
   Printings: 1573, 1758, 1715, 1750; your text: Wikisource.
   **Apply:** `Luke.11.17` la: `super domus cadit` → `super domum cadit`
20. **Luke 13:4** *duodēvīgintī, quod dēlāpsa* → *duodēvīgintī, quōs dēlāpsa*. **1573** (canvas 802, page image): *illos duodeuiginti, quos delapſa turris … interfecit*.
   Printings: 1573; your text: Wikisource.
   **Apply:** `Luke.13.4` la: `duodēvīgintī, quod dēlāpsa` → `duodēvīgintī, quōs dēlāpsa`
21. **John 1:40** *quī cum audītō* → *quī eum audītō*. **1573** (canvas 814, page image): *qui eum audito Iohanne ſecuti fuerant*: “who had followed him”.
   Printings: 1573, 1556, 1758, 1750; your text: Wikisource.
   **Apply:** `John.1.40` la: `quī cum audītō` → `quī eum audītō`
22. **John 1:47** *Vīdit ejus venientem* → *Vīdit Jēsūs venientem*. **1573** (canvas 814, page image): *Vidit Ieſus venientem ad ſe Nathanaelem*.
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `John.1.47` la: `Vīdit ejus venientem` → `Vīdit Jēsūs venientem`

## 2. Different readings: 1573 and the other printings agree against your text (21)

Both readings construe; 1573 (the base) and the printings that follow it read otherwise. Most are Wikisource's.

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 4:16** *in terræ noctis* → *in tētræ noctis*. **1573** (canvas 751, page image): *in tetræ noctis regione*: “in the region of dark night” (Gaffiot *tēter*); Vulgate *in regione umbræ mortis*.
   Printings: 1573, 1758, 1681; your text: Wikisource.
   **Apply:** `Matt.4.16` la: `in terræ noctis` → `in tētræ noctis`
2. **Matt 6:4** *quī occultē videt* → *quī occulta videt*. **1573** (canvas 753, page image): *qui occulta videt*: “who sees what is hidden”.
   Printings: 1573, 1556, 1758, 1747, 1750; your text: Wikisource.
   **Apply:** `Matt.6.4` la: `quī occultē videt` → `quī occulta videt`
3. **Matt 6:6** *quī occultē videt* → *quī occulta videt*. **1573** (canvas 754, page image): *qui occulta videt*.
   Printings: 1573, 1758, 1747, 1750; your text: Wikisource.
   **Apply:** `Matt.6.6` la: `quī occultē videt` → `quī occulta videt`
4. **Matt 6:18** *quī occultē cernit* → *quī occulta cernit*. **1573** (canvas 754, page image): *qui occulta cernit*.
   Printings: 1573, 1556, 1758, 1681, 1747, 1750 (every printing); your text: Wikisource.
   **Apply:** `Matt.6.18` la: `quī occultē cernit` → `quī occulta cernit`
5. **Matt 7:8** *pulsantī aperiētur* → *pulsantī aperītur*. **1573** (canvas 755, page image): *& pulſanti aperitur*: the present, as *obtinet*, *invenit*.
   Printings: 1573, 1758, 1681, 1715, 1747; your text: Wikisource.
   **Apply:** `Matt.7.8` la: `pulsantī aperiētur` → `pulsantī aperītur`
6. **Matt 12:42** *ad audiendam Solomōnis* → *ad audiendum Solomōnis*. **1573** (canvas 760, page image): *ad audiendum Solomonis ſapientiam*: the gerund with an object.
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Matt.12.42` la: `ad audiendam Solomōnis` → `ad audiendum Solomōnis`
7. **Matt 13:12** *Quī autem habet* → *Quī enim habet*. **1573** (canvas 761, page image): *Qui enim habet*.
   Printings: 1573, 1758, 1715, 1747, 1750; your text: Wikisource.
   **Apply:** `Matt.13.12` la: `Quī autem habet` → `Quī enim habet`
8. **Matt 13:32** *est holus maximum* → *est holerum maximum*. **1573** (canvas 761, page image): *eſt olerum maximum*: “the greatest of herbs” (Vulgate *majus est omnibus oleribus*); *h* as your *holus* (Gaffiot *hŏlus*).
   Printings: 1573, 1758, 1747, 1750; your text: Wikisource.
   **Apply:** `Matt.13.32` la: `est holus maximum` → `est holerum maximum`
9. **Mark 4:21** *Nōn ut in candēlābrō* → *Nōnne ut in candēlābrō*. **1573** (canvas 777, page image): *Nonne vt in candelabro ponatur?*.
   Printings: 1573, 1758, 1715, 1747; your text: Wikisource.
   **Apply:** `Mark.4.21` la: `Nōn ut in candēlābrō` → `Nōnne ut in candēlābrō`
10. **Luke 5:24** *Atquī ut* → *Atque ut*. **1573** (canvas 794, page image): *Atq; vt intelligatis*.
   Printings: 1573, 1556; your *Atquī*: 1758, 1750, Wikisource.
   **Apply:** `Luke.5.24` la: `Atquī ut` → `Atque ut`
11. **Luke 6:32** *amātōrēs amant.* → *amātōrēs ament.*. **1573** (canvas 795, page image): *cùm etiam improbi ſuos amatores ament*: subjunctive after *cum*, as 6:33 *faciant*.
   Printings: 1573, 1758; your text: Wikisource.
   **Apply:** `Luke.6.32` la: `amātōrēs amant.` → `amātōrēs ament.`
12. **Luke 8:1** *pāgātim prædīcēns* → *pāgātim prædicāns*. **1573** (canvas 796, page image): *pagatim prædicans*: “proclaiming” (*prædicō, -āre*), not “foretelling”.
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Luke.8.1` la: `pāgātim prædīcēns` → `pāgātim prædicāns`
13. **Luke 9:10** *facessit seorsum* → *sēcessit seorsum*. **1573** (canvas 797, page image): *ſeceſsit ſeorſum*: “withdrew apart” (the OCR reads the long *ſ* as *f*).
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Luke.9.10` la: `facessit seorsum` → `sēcessit seorsum`
14. **Luke 9:12** *profectī dīvertantur* → *profectī dēversentur*. **1573** (canvas 798, page image): *profecti di|uerſentur*: “lodge” (the Vulgate has *divertant*, as Wikisource's *dīvertantur*), *dēversor* as your *dēversōrium* (Luke 2:7, 9:52, 10:34).
   Printings: 1573, 1758, 1715; your text: Wikisource.
   **Apply:** `Luke.9.12` la: `profectī dīvertantur` → `profectī dēversentur`
15. **Luke 9:39** *ille spūmāns agentem* → *ille spūmās agentem*. **1573** (canvas 798, page image): *eumq; ille ſpumas agentem lacerat*: “foaming” (*spūmās agere*).
   Printings: 1573, 1758, 1747, 1750; your text: Wikisource.
   **Apply:** `Luke.9.39` la: `ille spūmāns agentem` → `ille spūmās agentem`
16. **Luke 10:7** *iīs suppetant* → *iīs suppetent*. **1573** (canvas 799, page image): *comedentes & bibentes quę eis ſuppetent*: the future.
   Printings: 1573, 1758, 1715, 1750; your text: Wikisource.
   **Apply:** `Luke.10.7` la: `iīs suppetant` → `iīs suppetent`
17. **Luke 11:24** *spīritus exit ex* → *spīritus exiit ex*. **1573** (canvas 800, page image): *Dum impurus ſpiritus exijt ex aliquo homine*: the perfect.
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Luke.11.24` la: `spīritus exit ex` → `spīritus exiit ex`
18. **Luke 13:15** *Ac Dominus* → *At Dominus*. **1573** (canvas 802, page image): *At Dominus ſic ad eum contrà locutus eſt*.
   Printings: 1573, 1758, 1750; your text: Wikisource.
   **Apply:** `Luke.13.15` la: `Ac Dominus` → `At Dominus`
19. **John 3:15** *fidem habet, nōn* → *fidem habeat, nōn*. **1573** (canvas 816, page image): *vt quiſquis ei fidem habeat*; your *habet*: 1758, 1750, Wikisource.
   Printings: 1573, 1747; your text: Wikisource.
   **Apply:** `John.3.15` la: `fidem habet, nōn` → `fidem habeat, nōn`
20. **John 3:29** *Spōnsī item amīcus* → *Spōnsī autem amīcus*. **1573** (canvas 816, page image): *Sponſi autem amicus*.
   Printings: 1573, 1758, 1715, 1747; your text: Wikisource.
   **Apply:** `John.3.29` la: `Spōnsī item amīcus` → `Spōnsī autem amīcus`
21. **John 4:9** *Ac mulier* → *At mulier*. **1573** (canvas 816, page image): *At mulier Samaritana*.
   Printings: 1573, 1556, 1758; your text: Wikisource.
   **Apply:** `John.4.9` la: `Ac mulier` → `At mulier`

## 3. Castellio's revision between 1556 and 1573 (1)

1556 reads as your text; 1573 and every later printing have a new sentence (“Show us some sign, by which we may
know that you may do these things”; the Vulgate *Quod signum ostendis nobis, quia hæc facis?* is nearer 1556). By decision 24 the 1573 reading
is the text and 1556's is recorded as a variant. *intellegāmus*: 1573 *intelligamus*, by the approved *intellig- → intelleg-*.

**Decision:** accept (1556 recorded as a variant) (Nathan, 2026-11-07)

1. **John 2:18** *Quod nōbīs exemplum præbēs, quī ista faciās?* → *Ēde nōbīs aliquod prōdigium, quō intellegāmus ista tibi licēre.*. **1573** (canvas 815, page image): *Ede nobis aliquod prodigium, quo intelligamus iſta tibi licere.*. 1556 recorded as a variant.
   Printings: 1573, 1758, 1747, 1750, 1715; your text: 1556 (OCR *Quod … nobís exemplü praebes, quí ita facías*), Wikisource.
   **Apply:** `John.2.18` la: `“Quod nōbīs exemplum præbēs, quī ista faciās?”` → `“Ēde nōbīs aliquod prōdigium, quō intellegāmus ista tibi licēre.”`

## 4. Forms: both are Latin; 1573 and the printings agree (2)

Not wording but the form of a word. **Recommended: accept** (the base's form, where no spelling rule or corpus count
decides otherwise). *Tonitruī* is the genitive of *tonitruum* (Gaffiot heads *tonitrus, ūs*, and gives *tonitruum*
too); *sēminece* the ablative of the noun *sēminex* (the adjective's is *-ī*); the corpus has neither form in
republican prose.

**Decision:** accept (Nathan, 2026-11-07)

1. **Mark 3:17** *tonitrūs fīliī* → *tonitruī fīliī*. **1573** (canvas 777, page image): *hoc eſt tonitrui filij*.
   Printings: 1573, 1758, 1715, 1750; your *tonitrūs*: Wikisource.
   **Apply:** `Mark.3.17` la: `tonitrūs fīliī` → `tonitruī fīliī`
2. **Luke 10:30** *eō sēminecī relictō* → *eō sēminece relictō*. **1573** (canvas 799, page image): *eo ſeminece relicto*.
   Printings: 1573, 1556, 1758; your *sēminecī*: Wikisource.
   **Apply:** `Luke.10.30` la: `eō sēminecī relictō` → `eō sēminece relictō`

## 5. Not proposed

- **Luke 3:1 (3×), 3:19, 9:7 *tetrarchē(s)*:** 1573 *tetrarcha* (canvases 792, 797, page image), with 1758, 1715, 1747, 1750.
  Kept: Gaffiot heads *tetrarchēs, æ*, and the republican hits are *tetrarchēs* (Cicero 1, Caesar 1). Say if you want
  1573's Latin *tetrarcha* instead.
- **Luke 13:18 *assimulem*** (1573 *assimilem*): Gaffiot *adsĭmŭlō*; republican *assimul-* 2 : *assimil-* 0. Kept.
- **Mark 3:32 *circumsedēret*** (1573 *circumsideret*): Gaffiot *circumsĕdĕō*; all eras *circumsed-* 8 : *circumsid-* 1. Kept.
- **Luke 10:11 *abstergēmus*** (1573 *abstergimus*): the same tense; *abstergeō* (2nd conjugation, yours) against
  the 3rd-conjugation variant, which no lexicon here knows. Kept.
- **John 4:8 *ierant*** (1573 *iuerant*), **Matt 2:23 *iitque***, **13:25 *iit***, **Luke 4:35 *exiit***, **John 1:39 *iērunt***
  (1573 *-iu-*): decision 26 (republican prose: the short forms of *eō*).
- ***aliōquī*** (1573 *alioquin*, 6×) and the other spellings the approved rules decide (*intelleg-, exs-, -cumque,
  quotīdiē → cotīdiē, mīlia, monumentum, sollicitus, simul ac, sē ipsum* …): rules, not readings.
- **Luke 5:29 *celebre*** (1573 *celebrē*, perhaps *celebrem*, which does not agree with *convīvium*) and **5:36
  *novæ*** (1573 *noua* at a line end, blotted): the images do not settle them. Kept.
- About 1,300 places where only 1573's OCR differed were filtered for real words; the few that looked real
  were read on the image (above, or misreadings: Mark 4:8 *edidit;* is *ediditq;*). The rest are OCR noise.
