# Acts: light notes, brackets and corrections

Built 2026-11-17 by the process in `nt-notes-process.md`, with the test and wording of `nt-notes-form.md` (decisions
1–3): "the modern editions" means SBLGNT and NA28, against the TR.

**Sources read:**
- `acts-notes-candidates.md` (`python -m pipeline notes Acts`): 342 apparatus units in 289 verses, 178 TR-alone readings.
- The whole of Acts, read verse by verse against the TR, SBLGNT, BSB, WEB, the Vulgate and 1573 as printed
  (`text/orig/ACT.usfm`) by four readers (chapters 1–7, 8–14, 15–21, 22–28). Each finding was checked here against the
  files and the SBLGNT apparatus (NA28 with SBLGNT in every A and C item).
- The NRSVue (Bible Gateway, read 2026-11-17), text and footnotes, for every verse below: in each it reads with the
  modern text against Castellio, and none of its footnotes gives his sense as an alternative ("Or …").
- For Castellio's own readings, the OCR of 1556 and the later printings (27:1).

Nothing from the NRSVue is copied here beyond a word or two. The NET notes were not read for Acts.

## A. Notes where the Greek text differs (the modern editions against the TR)

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

1. **3:20** *prænūntiātum*: TR προκεκηρυγμένον, "preached before"; SBLGNT (and RP) προκεχειρισμένον, "appointed" (NRSVue "the Messiah appointed for you"). The TR alone, so not in the apparatus.
   **Apply:** `Acts.3.20` la: `cum prænūntiātum vōbīs` → `cum prænūntiātum\f + \fr 3:20 \ft Cōdicēs antīquiōrēs habent προκεχειρισμένον, ‘dēstinātum’.\f* vōbīs`
2. **4:25** *Quī tuī Dāvīdis ōre sīc dīxistī*: the modern editions add τοῦ πατρὸς ἡμῶν and διὰ πνεύματος ἁγίου (NRSVue "who said by the Holy Spirit through our ancestor David").
   **Apply:** `Acts.4.25` la: `ōre sīc dīxistī:` → `ōre sīc dīxistī\f + \fr 4:25 \ft Cōdicēs antīquiōrēs addunt τοῦ πατρὸς ἡμῶν et διὰ πνεύματος ἁγίου, ‘patris nostrī’ et ‘per Spīritum Sānctum’.\f*:`
3. **6:8** *fideī*: TR πίστεως, "faith"; the modern editions χάριτος, "grace" (NRSVue "full of grace and power").
   **Apply:** `Acts.6.8` la: `vērō fideī potentiæque` → `vērō fideī\f + \fr 6:8 \ft Cōdicēs antīquiōrēs habent χάριτος, ‘grātiæ’.\f* potentiæque`
4. **7:16** *ā fīliīs Emōris, Sichemī fīliī*: TR Ἐμμὸρ τοῦ Συχέμ, which Castellio (with the Vulgate) takes as "Hamor, son of Shechem"; the modern editions Ἑμμὼρ ἐν Συχέμ, "the sons of Hamor in Shechem" (NRSVue). Gen 33:19 makes Hamor Shechem's father.
   **Apply:** `Acts.7.16` la: `Emōris, Sichemī fīliī, ēmerat.` → `Emōris, Sichemī fīliī\f + \fr 7:16 \ft Cōdicēs antīquiōrēs habent Ἑμμὼρ ἐν Συχέμ, ‘Emōris in Sichemā’.\f*, ēmerat.`
5. **9:20** *Chrīstum prædicābat*: TR τὸν Χριστόν; the modern editions τὸν Ἰησοῦν (NRSVue "he began to proclaim Jesus"), as at Matt 23:8.
   **Apply:** `Acts.9.20` la: `collēgiīs Chrīstum prædicābat` → `collēgiīs Chrīstum\f + \fr 9:20 \ft Cōdicēs antīquiōrēs habent τὸν Ἰησοῦν, ‘Jēsum’.\f* prædicābat`
6. **9:31** *ecclēsiæ*: TR αἱ ἐκκλησίαι, plural; the modern editions ἡ ἐκκλησία, "the church throughout Judea, Galilee, and Samaria" (NRSVue): one church.
   **Apply:** `Acts.9.31` la: `Igitur ecclēsiæ per` → `Igitur ecclēsiæ\f + \fr 9:31 \ft Cōdicēs antīquiōrēs habent ἡ ἐκκλησία, ‘ecclēsia’, singulāriter.\f* per`
7. **13:20** *Posteā annīs circiter quadringentīs quīnquāgintā, dedit præsidēs*: in the TR the 450 years are the time of the judges; in the modern editions they close vv. 17–19 (Egypt, the wilderness, the conquest) and the judges come after (NRSVue "for about four hundred fifty years. After that he gave them judges"). The candidates file had filed it as word order.
   **Apply:** `Acts.13.20` la: `quīnquāgintā, dedit præsidēs` → `quīnquāgintā\f + \fr 13:20 \ft Cōdicēs antīquiōrēs habent ὡς ἔτεσι τετρακοσίοις καὶ πεντήκοντα. καὶ μετὰ ταῦτα ἔδωκεν κριτάς, ‘annīs circiter quadringentīs quīnquāgintā. Et posteā dedit jūdicēs’.\f*, dedit præsidēs`
8. **16:7** *Spīritus*: the modern editions add Ἰησοῦ, "the Spirit of Jesus" (NRSVue).
   **Apply:** `Acts.16.7` la: `sīvit eōs Spīritus.` → `sīvit eōs Spīritus\f + \fr 16:7 \ft Cōdicēs antīquiōrēs addunt Ἰησοῦ, ‘Jēsū’.\f*.`
9. **18:5** *dīvīnō īnstīnctū afflātus*: TR συνείχετο τῷ πνεύματι, "pressed in spirit"; the modern editions τῷ λόγῳ (NRSVue "occupied with proclaiming the word").
   **Apply:** `Acts.18.5` la: `īnstīnctū afflātus, Chrīstum` → `īnstīnctū afflātus\f + \fr 18:5 \ft Cōdicēs antīquiōrēs habent συνείχετο τῷ λόγῳ, ‘verbō prædicandō īnstābat’.\f*, Chrīstum`
10. **18:7** *Jūstī*: the modern editions Τιτίου Ἰούστου (NRSVue "Titius Justus").
    **Apply:** `Acts.18.7` la: `nōmine Jūstī, hominis` → `nōmine Jūstī\f + \fr 18:7 \ft Cōdicēs antīquiōrēs habent Τιτίου Ἰούστου, ‘Titiī Jūstī’.\f*, hominis`
11. **20:4** *Sōpater Berrhœēnsis*: the modern editions Σώπατρος Πύρρου, "Sopater son of Pyrrhus" (NRSVue). The same verse has a bracket (item 31).
    **Apply:** `Acts.20.4` la: `Sōpater Berrhœēnsis,` → `Sōpater\f + \fr 20:4 \ft Cōdicēs antīquiōrēs addunt Πύρρου, ‘Pyrrhī fīlius’.\f* Berrhœēnsis,`
12. **25:6** *nōn plūs decem diēs*: TR ἡμέρας πλείους ἢ δέκα, "more than ten days"; the modern editions οὐ πλείους ὀκτὼ ἢ δέκα (NRSVue "not more than eight or ten days"). Castellio already has *nōn*, with the Vulgate, but not "eight".
    **Apply:** `Acts.25.6` la: `nōn plūs decem diēs ēgit` → `nōn plūs decem diēs\f + \fr 25:6 \ft Cōdicēs antīquiōrēs habent οὐ πλείους ὀκτὼ ἢ δέκα, ‘nōn plūs octō aut decem’.\f* ēgit`
13. **28:25** *majōrēs nostrōs*: TR ἡμῶν; the modern editions ὑμῶν, "your ancestors" (NRSVue): Paul sets himself against his hearers. A change of person, as at Luke 9:50.
    **Apply:** `Acts.28.25` la: `vātem majōrēs nostrōs,` → `vātem majōrēs nostrōs\f + \fr 28:25 \ft Cōdicēs antīquiōrēs habent ὑμῶν, ‘vestrōs’.\f*,`

## B. Notes where Castellio's Latin says what the Greek does not

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

14. **1:18** *suspēnsus crepuit medius*: the Greek (TR and SBLGNT) πρηνὴς γενόμενος ἐλάκησεν μέσος, "falling headlong, he burst open in the middle" (NRSVue). Castellio follows the Vulgate's *suspensus*, which brings the verse in line with Matt 27:5. 1573 prints *suspensus*.
    **Apply:** `Acts.1.18` la: `et suspēnsus crepuit` → `et suspēnsus\f + \fr 1:18 \ft Græcē πρηνὴς γενόμενος, ‘prōnus prōlāpsus’.\f* crepuit`
15. **4:5** *magistrātūs et scrībæ*: the Greek (TR and SBLGNT) has three groups, τοὺς ἄρχοντας καὶ τοὺς πρεσβυτέρους καὶ τοὺς γραμματεῖς, "rulers, elders, and scribes" (NRSVue; the Vulgate *seniores*). Castellio drops the elders; 1573 prints *magistratus, et scribæ*.
    **Apply:** `Acts.4.5` la: `magistrātūs et scrībæ Hierosolymam` → `magistrātūs et scrībæ\f + \fr 4:5 \ft Græcē τοὺς ἄρχοντας καὶ τοὺς πρεσβυτέρους καὶ τοὺς γραμματεῖς, ‘magistrātūs, senātōrēs et scrībæ’.\f* Hierosolymam`
16. **26:28–29** *Propemodum*: the Greek ἐν ὀλίγῳ (TR and SBLGNT), which Castellio reads as "almost", as the KJV does. The NRSVue has "so quickly" (28) and "whether quickly or not" (29), with no footnote giving "almost".
    **Apply:** `Acts.26.28` la: `“Propemodum mihi` → `“Propemodum\f + \fr 26:28 \ft Græcē ἐν ὀλίγῳ, ‘brevī’, ut et v. 29.\f* mihi`
17. **27:17** *dēmissā scaphā*: the Greek (TR and SBLGNT) χαλάσαντες τὸ σκεῦος, "lowering the gear" (NRSVue "the sea anchor"; the Vulgate *summisso vase*). The boat had just been hauled aboard in the same verse (*Quā subductā*), and Castellio has them let it down again.
    **Apply:** `Acts.27.17` la: `metuentēs, dēmissā scaphā sīc` → `metuentēs, dēmissā scaphā\f + \fr 27:17 \ft Græcē χαλάσαντες τὸ σκεῦος, ‘dēmissīs armāmentīs’.\f* sīc`

## C. Brackets: words the modern editions leave out

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

In each, the NRSVue lacks the words; where it has a footnote giving them, the item says so. Item 51 (27:1 *duo*) is a word no Greek has.

18. **1:14** *ac supplicātiōnī*: TR καὶ τῇ δεήσει.
    **Apply:** `Acts.1.14` la: `precibus, ac supplicātiōnī, cum` → `precibus[, ac supplicātiōnī], cum`
19. **2:30** *quod ad carnem pertinet, suscitātūrum esse Chrīstum, et*: TR τὸ κατὰ σάρκα ἀναστήσειν τὸν Χριστόν. NRSVue "that he would put one of his descendants on his throne".
    **Apply:** `Acts.2.30` la: `fētū, quod ad carnem pertinet, suscitātūrum esse Chrīstum, et in` → `fētū[, quod ad carnem pertinet, suscitātūrum esse Chrīstum, et] in`
20. **2:41** *avidē*: TR ἀσμένως.
    **Apply:** `Acts.2.41` la: `ōrātiōne avidē admissā` → `ōrātiōne [avidē] admissā`
21. **3:22** *majōribus*: TR πρὸς τοὺς πατέρας.
    **Apply:** `Acts.3.22` la: `enim majōribus ita` → `enim [majōribus] ita`
22. **4:8** *Isrāēlītārum*: TR τοῦ Ἰσραήλ. NRSVue "Rulers of the people and elders".
    **Apply:** `Acts.4.8` la: `et Isrāēlītārum senātōrēs` → `et [Isrāēlītārum] senātōrēs`
23. **5:24** *summus sacerdōs, et*: TR ὅ τε ἱερεὺς καὶ ὁ στρατηγός; the modern editions ὅ τε στρατηγός. NRSVue "the captain of the temple and the chief priests".
    **Apply:** `Acts.5.24` la: `summus sacerdōs, et fānī` → `[summus sacerdōs, et] fānī`
24. **6:13** *impia*: TR ῥήματα βλάσφημα. NRSVue "never stops saying things against this holy place".
    **Apply:** `Acts.6.13` la: `dēsinit impia contrā` → `dēsinit [impia] contrā`
25. **7:30** *Dominī*: TR ἄγγελος Κυρίου. NRSVue "an angel appeared to him".
    **Apply:** `Acts.7.30` la: `angelus Dominī in` → `angelus [Dominī] in`
26. **7:37** *eum audiētis*: TR αὐτοῦ ἀκούσεσθε; RP lacks it too (the TR alone). NRSVue ends "as he raised me up".
    **Apply:** `Acts.7.37` la: `similem: eum audiētis.’` → `similem[: eum audiētis].’`
27. **8:18** *Sānctum*: TR τὸ πνεῦμα τὸ ἅγιον. NRSVue "the Spirit was given".
    **Apply:** `Acts.8.18` la: `Spīritum Sānctum darī` → `Spīritum [Sānctum] darī`
28. **9:5–6** *Dūrum est … calcitrāre* and Saul's question: TR σκληρόν σοι πρὸς κέντρα λακτίζειν. τρέμων τε καὶ θαμβῶν εἶπε, Κύριε, τί με θέλεις ποιῆσαι; καὶ ὁ Κύριος πρὸς αὐτόν. The TR alone (RP with the modern text): Erasmus took them from the Latin. NRSVue "I am Jesus, whom you are persecuting. But get up and enter the city". Without the brackets Jesus goes straight on: *“Surge, et in urbem ingredere …”*.
    **Apply:** `Acts.9.5` la: `persequeris. Dūrum est tibi contrā stimulōs calcitrāre.”` → `persequeris. [Dūrum est tibi contrā stimulōs calcitrāre.]”`
    **Apply:** `Acts.9.6` la: `Hīc ille tremēns ac stupefactus: “Domine, quid mē vīs facere?” inquit. Cui Dominus: “Surge` → `[Hīc ille tremēns ac stupefactus: “Domine, quid mē vīs facere?” inquit. Cui Dominus:] “Surge`
29. **10:6, 10:32** *quī tibi dīcet, quid tē facere oporteat* and *quī, ubi advēnerit, tēcum loquētur*: TR οὗτος λαλήσει σοι τί σε δεῖ ποιεῖν (10:6, the TR alone) and ὃς παραγενόμενος λαλήσει σοι (10:32). NRSVue ends both verses "by the sea(side)".
    **Apply:** `Acts.10.6` la: `quī tibi dīcet, quid tē facere oporteat` → `[quī tibi dīcet, quid tē facere oporteat]`
    **Apply:** `Acts.10.32` la: `quī, ubi advēnerit, tēcum loquētur` → `[quī, ubi advēnerit, tēcum loquētur]`
30. **10:12** *feræque*: TR καὶ τὰ θηρία. NRSVue "four-footed creatures and reptiles and birds".
    **Apply:** `Acts.10.12` la: `terrestrēs, feræque, et` → `terrestrēs, [feræque,] et`
31. **20:4** *ūsque in Asiam*: TR ἄχρι τῆς Ἀσίας. NRSVue footnote "Other ancient authorities add *as far as Asia*".
    **Apply:** `Acts.20.4` la: `eum ūsque in Asiam Sōpater` → `eum [ūsque in Asiam] Sōpater`
32. **10:21** *ā Cornēliō ad sē missōs*: TR τοὺς ἀπεσταλμένους ἀπὸ τοῦ Κορνηλίου πρὸς αὐτόν (the TR alone). NRSVue "Peter went down to the men".
    **Apply:** `Acts.10.21` la: `hominēs, ā Cornēliō ad sē missōs, dēgressus` → `hominēs, [ā Cornēliō ad sē missōs,] dēgressus`
33. **10:30** *jejūnus eram, et*: TR ἤμην νηστεύων, καὶ … προσευχόμενος; the modern editions ἤμην … προσευχόμενος, with no fasting (NRSVue "I was praying in my house").
    **Apply:** `Acts.10.30` la: `hōram jejūnus eram, et hōrā` → `hōram [jejūnus eram, et] hōrā`
34. **13:42** *ex Jūdæōrum collēgiō* and *extrāneī*: TR ἐκ τῆς συναγωγῆς τῶν Ἰουδαίων, παρεκάλουν τὰ ἔθνη; the modern editions have neither the synagogue nor the gentiles asking (NRSVue "the people urged them").
    **Apply:** `Acts.13.42` la: `eōs ex Jūdæōrum collēgiō exeuntēs, ōrābant extrāneī, ut` → `eōs [ex Jūdæōrum collēgiō] exeuntēs, ōrābant [extrāneī], ut`
35. **15:18** *Deō omnia ejus opera*: TR Γνωστὰ ἀπ᾿ αἰῶνός ἐστι τῷ Θεῷ πάντα τὰ ἔργα αὐτοῦ; the modern editions γνωστὰ ἀπ᾿ αἰῶνος, the end of the Amos quotation ("who has been making these things known from long ago"). NRSVue footnote gives the TR's reading. The quotation mark after 15:17 stays where it is.
    **Apply:** `Acts.15.18` la: `æternitāte Deō omnia ejus opera.` → `æternitāte [Deō omnia ejus opera].`
36. **15:23** *et* in *seniōrēs, et frātrēs*: TR οἱ πρεσβύτεροι καὶ οἱ ἀδελφοί; the modern editions οἱ πρεσβύτεροι ἀδελφοί, the elders being the brothers (NRSVue "The brothers, both the apostles and the elders"). The candidates file missed it (καὶ οἱ taken for small words).
    **Apply:** `Acts.15.23` la: `seniōrēs, et frātrēs,` → `seniōrēs, [et] frātrēs,`
37. **15:24** *dīcendō, circumcīdendōs esse, lēgīque pārendum*: TR λέγοντες περιτέμνεσθαι καὶ τηρεῖν τὸν νόμον. NRSVue footnote gives it.
    **Apply:** `Acts.15.24` la: `animōs, dīcendō, circumcīdendōs esse, lēgīque pārendum, cum` → `animōs, [dīcendō, circumcīdendōs esse, lēgīque pārendum,] cum`
38. **17:5** *quibus persuāsum nōn erat*: TR οἱ ἀπειθοῦντες Ἰουδαῖοι. NRSVue "But the Jews became jealous".
    **Apply:** `Acts.17.5` la: `Jūdæī, quibus persuāsum nōn erat, per` → `Jūdæī, [quibus persuāsum nōn erat,] per`
39. **17:26** *sanguine*: TR ἐξ ἑνὸς αἵματος. NRSVue "From one ancestor", footnote "other ancient authorities read *From one blood*".
    **Apply:** `Acts.17.26` la: `ūnīus sanguine ūniversum` → `ūnīus [sanguine] ūniversum`
40. **18:17** *Græcī*: TR πάντες οἱ Ἕλληνες; the modern editions πάντες (NRSVue "all of them", footnote "all the Greeks"). Who beat Sosthenes changes.
    **Apply:** `Acts.18.17` la: `Græcī vērō omnēs` → `[Græcī] vērō omnēs`
41. **18:21** *Mihi omnīnō Hierosolymæ agendum est proximum fēstum: sed*: TR Δεῖ με πάντως τὴν ἑορτὴν τὴν ἐρχομένην ποιῆσαι εἰς Ἱεροσόλυμα· πάλιν δέ. NRSVue footnote gives it.
    **Apply:** `Acts.18.21` la: `“Mihi omnīnō Hierosolymæ agendum est proximum fēstum: sed ad` → `“[Mihi omnīnō Hierosolymæ agendum est proximum fēstum: sed] ad`
42. **19:4** *Chrīstum*: TR εἰς τὸν Χριστὸν Ἰησοῦν; the modern editions εἰς τὸν Ἰησοῦν (NRSVue "that is, in Jesus").
    **Apply:** `Acts.19.4` la: `in Chrīstum Jēsum` → `in [Chrīstum] Jēsum`
43. **20:15** *et Trōgylliī morātī*: TR καὶ μείναντες ἐν Τρωγυλλίῳ. NRSVue footnote gives it.
    **Apply:** `Acts.20.15` la: `appulimus: et Trōgylliī morātī, posterō` → `appulimus: [et Trōgylliī morātī,] posterō`
44. **20:24** *cum lætitiā*: TR μετὰ χαρᾶς. NRSVue "if only I may finish my course".
    **Apply:** `Acts.20.24` la: `cursum meum cum lætitiā, et` → `cursum meum [cum lætitiā], et`
45. **21:22** *oportet, ut conveniat multitūdō*: TR Πάντως δεῖ πλῆθος συνελθεῖν· ἀκούσονται γάρ; the modern editions πάντως ἀκούσονται (NRSVue "They will certainly hear"). *Omnīnō* stays, since πάντως does.
    **Apply:** `Acts.21.22` la: `Omnīnō oportet, ut conveniat multitūdō: audient` → `Omnīnō [oportet, ut conveniat multitūdō:] audient`
46. **21:25** *nihil tāle servandum iīs esse, nisi*: TR μηδὲν τοιοῦτον τηρεῖν αὐτούς, εἰ μή. NRSVue "with our judgment that they should abstain".
    **Apply:** `Acts.21.25` la: `dēcrēvimus, nihil tāle servandum iīs esse, nisi ut` → `dēcrēvimus, [nihil tāle servandum iīs esse, nisi] ut`
47. **22:9** *et territī sunt*: TR καὶ ἔμφοβοι ἐγένοντο.
    **Apply:** `Acts.22.9` la: `illī quidem, et territī sunt: sed` → `illī quidem[, et territī sunt]: sed`
48. **22:20** *in ejus necem*: TR τῇ ἀναιρέσει αὐτοῦ. NRSVue "approving".
    **Apply:** `Acts.22.20` la: `et in ejus necem cōnsentīrem` → `et [in ejus necem] cōnsentīrem`
49. **22:30** *vinculīs*: TR ἀπὸ τῶν δεσμῶν. NRSVue "he released him".
    **Apply:** `Acts.22.30` la: `solvit eum vinculīs:` → `solvit eum [vinculīs]:`
50. **23:9** *nē pugnēmus cum Deō*: TR μὴ θεομαχῶμεν. NRSVue ends at "spoken to him?".
    **Apply:** `Acts.23.9` la: `allocūtus, nē pugnēmus cum Deō.”` → `allocūtus[, nē pugnēmus cum Deō].”`
51. **27:1** *duo*: no Greek has a number (TR and SBLGNT τινας ἑτέρους δεσμώτας, NRSVue "some other prisoners"). 1556 prints *alij quidam uincti duo* (OCR, e-rara 10282399) and 1573 *vincti duo*; 1747 and 1750 drop it. So it is Castellio's own word, bracketed as Matt 8:13.
    **Apply:** `Acts.27.1` la: `vīnctī duo, centuriōnī` → `vīnctī [duo], centuriōnī`
52. **23:11** *Paule*: TR Θάρσει Παῦλε. NRSVue "Keep up your courage!".
    **Apply:** `Acts.23.11` la: `animō es, Paule:` → `animō es[, Paule]:`
53. **23:12** *quīdam*: TR τινες τῶν Ἰουδαίων; the modern editions οἱ Ἰουδαῖοι (NRSVue "the Jews joined in a conspiracy").
    **Apply:** `Acts.23.12` la: `Jūdæī quīdam, et` → `Jūdæī [quīdam], et`
54. **23:15** *crās*: TR ὅπως αὔριον (23:20 has it in all texts).
    **Apply:** `Acts.23.15` la: `ut crās eum` → `ut [crās] eum`
55. **23:30** *Valē*: TR Ἔρρωσο. NRSVue footnote "Other ancient authorities add *Farewell*".
    **Apply:** `Acts.23.30` la: `præcēpī. Valē.”` → `præcēpī. [Valē.]”`
56. **24:15** *mortuōrum*: TR ἀνάστασιν … νεκρῶν. NRSVue footnote "of the dead".
    **Apply:** `Acts.24.15` la: `fore mortuōrum, tum` → `fore [mortuōrum], tum`
57. **24:26** *ut eum solveret*: TR ὅπως λύσῃ αὐτόν.
    **Apply:** `Acts.24.26` la: `spērābat, ut eum solveret.` → `spērābat[, ut eum solveret].`
58. **25:16** *ad necem*: TR εἰς ἀπώλειαν. NRSVue "to hand over anyone".
    **Apply:** `Acts.25.16` la: `ūllum ad necem condōnāre` → `ūllum [ad necem] condōnāre`
59. **26:30** *Hæc eō locūtō*: TR Καὶ ταῦτα εἰπόντος αὐτοῦ. NRSVue "Then the king got up".
    **Apply:** `Acts.26.30` la: `Hæc eō locūtō, surrēxit` → `[Hæc eō locūtō,] surrēxit`
60. **28:16** *centuriō vīnctōs præfectō castrōrum trādidit*: TR ὁ ἑκατόνταρχος παρέδωκε τοὺς δεσμίους τῷ στρατοπεδάρχῃ. NRSVue "When we came into Rome, Paul was allowed to live by himself".
    **Apply:** `Acts.28.16` la: `vēnimus, centuriō vīnctōs præfectō castrōrum trādidit. Paulō` → `vēnimus, [centuriō vīnctōs præfectō castrōrum trādidit.] Paulō`

## D. Corrections to the edited text

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

`text/orig/ACT.usfm` (1573, every word read on the page) has the right reading in each; only `text/` changes.

61. **16:15** *dīverterēmur* → *dīverterēmus*: 1573 prints *diuerteremus* ("that we should stay at her house"); Wikisource has *diverteremur*, which the settled text took.
    **Apply:** `Acts.16.15` la: `suās ædēs dīverterēmur:` → `suās ædēs dīverterēmus:`
62. **9:39** a comma: *postquam advēnit in cœnāculum, subdūxērunt* → *postquam advēnit, in cœnāculum subdūxērunt*, as 1573 (*postquam aduenit, in cœnaculum subduxerunt*) and the Greek (ὃν παραγενόμενον ἀνήγαγον εἰς τὸ ὑπερῷον, "when he arrived, they took him to the room upstairs"). As it stands, Peter arrives in the upper room and is then led up.
    **Apply:** `Acts.9.39` la: `postquam advēnit in cœnāculum, subdūxērunt` → `postquam advēnit, in cœnāculum subdūxērunt`
63. **15:32** commas: *quī et ipsī vātēs, erant,* → *quī, et ipsī vātēs, erant,*, as 1573 (*qui, et ipsi vates, erant,*). As it stands, a comma splits *vātēs erant*.
    **Apply:** `Acts.15.32` la: `Sīlās, quī et ipsī vātēs, erant,` → `Sīlās, quī, et ipsī vātēs, erant,`
64. **22:22** a comma: *Ad hæc ūsque, verba* → *Ad hæc ūsque verba*, as 1573 (*Ad hæc vsque verba*): "up to these words".
    **Apply:** `Acts.22.22` la: `Ad hæc ūsque, verba` → `Ad hæc ūsque verba`
65. **19:9** a capital: *cujusdam tyrannī lūdō* → *cujusdam Tyrannī lūdō*. The Greek ἐν τῇ σχολῇ Τυράννου τινός names a man, Tyrannus (NRSVue "the lecture hall of Tyrannus", footnote "of a certain Tyrannus"); in lower case the Latin reads "a certain tyrant's school". 1573 prints *tyranni*, but capitals are the edition's call (`data/decisions/*.layout.tsv`), and 1573 is not consistent with names.
    **Apply:** `Acts.19.9` la: `cujusdam tyrannī lūdō` → `cujusdam Tyrannī lūdō`

## Considered and left out

**From the apparatus and the TR-alone list:**
- 3:25 and 14:17, 13:26, 16:17, 19:37, 27:19, 28:1: a change of person only, where the sense hardly changes.
- 4:27 *in hāc urbe* (the modern editions add ἐν τῇ πόλει ταύτῃ); 4:24 *Deus es*; 6:3 *Sānctō*; 2:7 *omnēs*, *inter sēsē*; 2:23; 5:23 *forīs*; 7:37 *Dominus … vester*; 9:29 *Jēsū*; 10:11 *ligātum*; 10:48 *Dominī*; 11:28 *Cæsare*; 13:45 *reclāmantēs ac*; 15:11 *Chrīstī*; 19:10 *Jēsū*; 20:25 *dīvīnum*; 20:32 *frātrēs*; 18:20 *apud sē*; 23:30 *Jūdæōrum*; 24:22 *Hīs audītīs*; 24:23 *aut adīre*; 26:7 *Agrippa*: a word that changes nothing a reader needs.
- 4:36 *Jōsēs* (the modern editions Ἰωσήφ), 7:43 *Remphanis*, 27:16 *Claudam* (Cauda): forms of the same name.
- 9:25 "his disciples", 15:33, 17:23 (neuter ὅ), 20:7–8 "we", 23:6 "son of Pharisees", 26:28 ποιῆσαι, 28:13: shades.
- 3:6, 7:38, 7:46, 11:21-type splits: SBLGNT and NA28 disagree, so they fail the test.

**From the reading of each chapter:**
- 3:13 *Fīlium* for παῖδα (he has *puerum* at 3:26 and 4:27): παῖς bears both, and the Vulgate has *filium*.
- 7:20 *Deō fuit acceptus* for ἀστεῖος τῷ θεῷ: an older reading of the idiom.
- 18:22 the church greeted at Caesarea: the Greek does not name Jerusalem.
- 27:22 *nūllīus nostrum* for ἐξ ὑμῶν: Paul is on board; the sense hardly changes.
- 9:38 the two men left unnamed; 12:25 *Paulus* for Σαῦλος: no change a reader needs.
- 7:51 *Dūrī cervīce*: 1573 prints *ceruici*; the edited text's ablative is right, and `text/orig` keeps the print.
- 11:25 *Tharsum* (1573 *Tarsum*), 13:7 *Paullō*, 15:3 *Phœnīcem*, and the short perfects (*audierant*, 18:8; 19:10; 21:24): spelling, for the orthography review rather than here.
