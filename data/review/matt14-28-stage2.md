# Matthew 14–28, stage 2: your draft against the printings

Proposed 2026-11-07 (overnight run) for the pilot (decision 6: every change reviewed). The draft (`text/draft/MAT.usfm`) was collated word by word against 1573 (the NT base, decision 24; MDZ hOCR), 1556 (the reference; e-rara OCR, which reads poorly), 1758, 1681, 1715, 1747, 1750 (archive.org OCR) and Wikisource, all aligned to the draft's verses (`pipeline/collate.py`; spelling habits set aside). Of 4,700 places where some witness differs, 4,500 are one OCR's misreading or a marginal reference run into a line, and are not listed. Every place below where 1573 and another printing agree against your text, or where 1573's OCR was unclear, was **read on the 1573 page image** (IIIF crop from the hOCR word box; canvas numbers given; crops cached in `sources/mdz-1573/crops/`). Your draft agrees with Wikisource at nearly all of them: Wikisource's Matthew follows the 1760 printing there, not 1573.

Each **Apply** line is an exact replacement inside that verse of `text/draft/MAT.usfm`, checked to match once (`python -m pipeline review check`). Verse numbers are the **KJV's, after group 1**: apply group 1 first. Answer each group's **Decision:** with *accept*, *accept all except N, M*, or *accept N, M*; then `python -m pipeline review apply data/review/matt14-28-stage2.md --write`.

Spelling and form differences from the printings (*mīlia/millia*, *iit/ivit*, *intellegō*, *-cumque*, *monumentum/monimentum*, *miseritus/misertus*) are not wording: they are in `matt14-28-spelling.md`.

## 1. Verse numbers: three lost inside quotations (3)

The LaTeX conversion left three verse numbers inside the text, where a verse begins with a quotation (*dīcēns: 8‘Hic populus*), so Matthew 15 has 38 verses and 22 has 44 (KJV 39 and 46), and every later verse in those chapters is numbered one or two short of the KJV. Wikisource numbers them as the KJV. The edits are in `data/versification/Matt.draft.edits.tsv`; each splits the verse at the quotation and drops the stray number (words unchanged, checked). Set their `status` to `approved`, then `python -m pipeline versify Matt --draft --apply` (renumbers 15:8–38 → 15:9–39, 22:32–44 → 22:33–46).

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 15:7** *… dīcēns: 8‘Hic populus mē et ōre accēdit* → verse 8 starts at *‘Hic populus* (KJV 15:8 “This people draweth nigh unto me”).
2. **Matt 22:31** *… hīs verbīs dictum est? 32‘Ego sum Deus Abrahāmī* → verse 32 starts at *‘Ego sum* (KJV 22:32 “I am the God of Abraham”).
3. **Matt 22:42** (22:43 after item 2) *… ita dīcēns: 44‘Ait Dominus Dominō meō* → verse 44 starts at *‘Ait Dominus* (KJV 22:44 “The LORD said unto my Lord”).

## 2. Change your text: 1573 and the other printings agree against it (29)

Read on the 1573 page at every place. Wikisource reads as your text unless the collation line says otherwise. The new words carry provisional macrons (from `latin macron`); stage 4 checks them.

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 16:21** *sibi eundem esse* → *sibi eundum esse*. **1573** (canvas 764, page image): *ſibi eundum eſſe Hieroſolymam*. “that he must go to Jerusalem” (ὅτι δεῖ αὐτὸν … ἀπελθεῖν): the gerundive; *eundem* (“the same”) makes no sense.
   Collation: 1573, 1758, 1747 *eundum*; as your text: Wikisource; not read: 1556, 1681, 1715, 1750.
   **Apply:** `Matt.16.21` la: `sibi eundem esse` → `sibi eundum esse`
2. **Matt 17:11** *et īnstaurātus omnia.* → *et īnstaurātūrus omnia.*. **1573** (canvas 764, page image): *& inſtauraturus omnia*. future participle, “and will restore all things” (ἀποκαταστήσει).
   Collation: 1573, 1758, 1747, 1750 *inftauraturus*; as your text: Wikisource; not read: 1556, 1681, 1715.
   **Apply:** `Matt.17.11` la: `et īnstaurātus omnia.` → `et īnstaurātūrus omnia.`
3. **Matt 18:33** *ut ego tuī* → *ut et ego tuī*. **1573** (canvas 765, page image): *vt & ego tui miſertus eram*. “as I too”: every printing has *et*.
   Collation: 1573, 1556, 1758, 1715, 1747, 1750 *et*; as your text: Wikisource; not read: 1681.
   **Apply:** `Matt.18.33` la: `ut ego tuī` → `ut et ego tuī`
4. **Matt 19:5** *prōnūntiātum es-se:* → *prōnūntiātum esse:*. **1573** (canvas 765, page image): *atq; ita pronunciatum eſſe?*. a hyphen (U+002D) left in the word by the LaTeX conversion; every printing and Wikisource have *esse*.
   **Apply:** `Matt.19.5` la: `prōnūntiātum es-se:` → `prōnūntiātum esse:`
5. **Matt 19:24** *facilius esse camēlum per* → *facilius esse rudentem per*. **1573** (canvas 766, page image): *facilius eſſe rudentem … traijci*. Castellio's *rudentem* (“a ship's cable”, reading κάμιλος for κάμηλος) in 1573, 1750 and Wikisource; your *camēlum* is the Vulgate's. The printings' reading is restored here under decision 24; the camel is the familiar text, so this is worth a deliberate yes.
   Collation: 1573, 1750, Wikisource *rudentem*; no witness reads your text; not read: 1556, 1681, 1715, 1747.
   **Apply:** `Matt.19.24` la: `facilius esse camēlum per` → `facilius esse rudentem per`
6. **Matt 19:26** *Quod intuitus* → *Quōs intuitus*. **1573** (canvas 766, page image): *Quos intuitus Ieſus*. “looking at them” (ἐμβλέψας … αὐτοῖς).
   Collation: 1573, 1556, 1758 *Quos*; as your text: Wikisource; not read: 1681, 1715, 1747, 1750.
   **Apply:** `Matt.19.26` la: `\v 26 Quod intuitus` → `\v 26 Quōs intuitus`
7. **Matt 21:3** *egēre,’ et dīmittet eōs.* → *egēre,’ et statim dīmittet eōs.*. **1573** (canvas 767, page image): *eis egere, & ſtatim dimittet eos*. “and straightway he will send them” (εὐθὺς); 1758 and 1747 have *statim* too.
   **Apply:** `Matt.21.3` la: `egēre,’ et dīmittet eōs.` → `egēre,’ et statim dīmittet eōs.`
8. **Matt 22:17** *Dīc nōbīs* → *Dīc ergō nōbīs*. **1573** (canvas 768, page image): *Dic ergo nobis quid cenſeas*. “Tell us therefore” (εἰπὲ οὖν ἡμῖν): every printing has *ergo*.
   Collation: 1573, 1556, 1758, 1681, 1715, 1750 *ergo*; as your text: Wikisource; not read: 1747.
   **Apply:** `Matt.22.17` la: `\v 17 Dīc nōbīs` → `\v 17 Dīc ergō nōbīs`
9. **Matt 22:21** *Cæsarī, et quī Deī Deō.* → *Cæsarī, et quæ Deī Deō.*. **1573** (canvas 768, page image): *& quæ Dei Deo*. “and the things that are God's”.
   Collation: 1573, 1758, 1747 *quæ*; as your text: Wikisource; not read: 1556, 1681, 1750.
   **Apply:** `Matt.22.21` la: `Cæsarī, et quī Deī Deō.` → `Cæsarī, et quæ Deī Deō.`
10. **Matt 22:35** *eōrum, jūris perītus, tentandī* → *eōrum, lēgis perītus, tentandī*. **1573** (canvas 768, page image): *eorum, legiſperitus, tentandi gratia*. 1573 has *legisperitus* (νομικός), written *lēgis perītus* by the approved rule *legisperiti → legis periti* (as your Luke 5:17, 7:30); *jūris perītus* is Wikisource's. **Your settled Luke has *jūris perītus* five times (10:25; 11:45, 46, 52, 53) where 1573 and 1758 read *legisperitus/-tis/-ti*** (OCR rows; 11:52 seen on the page image, canvas 800): not proposed here, see MORNING.md.
   Collation: 1573, 1747 *legisperitus*; as your text: Wikisource; not read: 1556, 1758, 1681, 1715, 1750.
   **Apply:** `Matt.22.35` la: `eōrum, jūris perītus, tentandī` → `eōrum, lēgis perītus, tentandī`
11. **Matt 23:39** *habētōte, vōs esse mē* → *habētōte, vōs nōn esse mē*. **1573** (canvas 769, page image): *vos non eſſe me viſuros deinceps*. **the negative is missing**: “ye shall not see me henceforth” (οὐ μή με ἴδητε).
   Collation: 1573, 1758, 1747, 1750 *non*; as your text: Wikisource; not read: 1556, 1681.
   **Apply:** `Matt.23.39` la: `habētōte, vōs esse mē` → `habētōte, vōs nōn esse mē`
12. **Matt 24:15** *ā Daniēle prædictum* → *ā Daniēle vāte prædictum*. **1573** (canvas 770, page image): *(quod à Daniele vate prædictum eſt)*. “Daniel the prophet” (διὰ Δανιὴλ τοῦ προφήτου).
   Collation: 1556, 1758, 1747, 1750 *uate*; 1573 *Luca vate*; as your text: Wikisource; not read: 1681, 1715.
   **Apply:** `Matt.24.15` la: `ā Daniēle prædictum` → `ā Daniēle vāte prædictum`
13. **Matt 24:30** *Āctum appārēbit* → *Ac tum appārēbit*. **1573** (canvas 770, page image): *30 ac tum apparebit in cœlo*. two words, “and then” (καὶ τότε); *Āctum* (“done”) is a misjoining.
   **Apply:** `Matt.24.30` la: `\v 30 Āctum appārēbit` → `\v 30 Ac tum appārēbit`
14. **Matt 24:32** *congnōscitis* → *cognōscitis*. **1573** (canvas 770, page image): *cognoſcitis inſtare æſtatem*. a slip in your text.
   **Apply:** `Matt.24.32` la: `congnōscitis` → `cognōscitis`
15. **Matt 24:43** *neque domum perfodī suam passūrum* → *neque domum suam perfodī passūrum*. **1573** (canvas 770, page image): *neque domum ſuam perfodi paſſurum*. word order: 1556 (*suam* before *perfodi*), 1758, 1747, 1750 as 1573; Wikisource, 1681 and 1715 as your text.
   **Apply:** `Matt.24.43` la: `neque domum perfodī suam passūrum` → `neque domum suam perfodī passūrum`
16. **Matt 25:11** *et reliquiæ virginēs* → *et reliquæ virginēs*. **1573** (canvas 771, page image): *& reliquæ virgines*. *reliquæ*, “the other (virgins)”; *reliquiæ* is “remains”.
   Collation: 1573, 1747, 1750 *reliquæ*; as your text: Wikisource; not read: 1556, 1758.
   **Apply:** `Matt.25.11` la: `et reliquiæ virginēs` → `et reliquæ virginēs`
17. **Matt 25:22** *mihi duo trādidistī* → *mihi duo talenta trādidistī*. **1573** (canvas 771, page image): *tu mihi duo talenta tradidiſti*. “thou deliveredst unto me two talents”.
   Collation: 1573, 1758, 1750 *talenta*; as your text: Wikisource; not read: 1556, 1681, 1715, 1747.
   **Apply:** `Matt.25.22` la: `mihi duo trādidistī` → `mihi duo talenta trādidistī`
18. **Matt 25:27** *meum com fænore* → *meum cum fænore*. **1573** (canvas 771, page image): *meum cum fœnore recepiſſem*. a slip in your text. (*fænore*: 1573 *fœnore*; Gaffiot heads *fēnus*: the spelling is for stage 3.)
   **Apply:** `Matt.25.27` la: `meum com fænore` → `meum cum fænore`
19. **Matt 26:34** *At Jēsūs* → *Et Jēsūs*. **1573** (canvas 772, page image): *34 Et Ieſus: Hoc tibi confirmo*.
   Collation: 1573, 1758 *Et*; as your text: 1715, Wikisource; not read: 1556, 1681, 1747, 1750.
   **Apply:** `Matt.26.34` la: `\v 34 At Jēsūs` → `\v 34 Et Jēsūs`
20. **Matt 26:54** *quō pactō cōnficerent,* → *quō pactō cōnfierent,*. **1573** (canvas 772, page image): *Sed quo pacto cófierent*. *cōnfierent* (from *cōnfīō*, *cōnfierī*: “how then would be fulfilled”, πῶς οὖν πληρωθῶσιν); *cōnficerent* (“accomplish”) wants a subject. 1758, 1747 *confierent*; 1750 *con ficerent*.
   **Apply:** `Matt.26.54` la: `quō pactō cōnficerent,` → `quō pactō cōnfierent,`
21. **Matt 26:57** *Jēsum addūxērunt ad* → *Jēsum abdūxērunt ad*. **1573** (canvas 772, page image): *comprehenſum Ieſum abduxerunt ad Caiapham*. “led him away” (ἀπήγαγον).
   Collation: 1573, 1758, 1747 *abduxerunt*; as your text: 1750, Wikisource; not read: 1556, 1681, 1715.
   **Apply:** `Matt.26.57` la: `Jēsum addūxērunt ad` → `Jēsum abdūxērunt ad`
22. **Matt 27:8** *Ideō vocātus* → *Ideōque vocātus*. **1573** (canvas 773, page image): *8 Ideoque vocatus eſt ager ille*.
   Collation: 1573, 1758, 1715, 1747 *Ideoque*; as your text: Wikisource; not read: 1556, 1681.
   **Apply:** `Matt.27.8` la: `\v 8 Ideō vocātus` → `\v 8 Ideōque vocātus`
23. **Matt 27:37** *Posuērunt autem* → *Posuerant autem*. **1573** (canvas 773, page image): *37 Poſuerant autem ſupra caput*. pluperfect, “they had set up” (ἐπέθηκαν).
   Collation: 1573, 1747 *Posuerant*; as your text: 1750, Wikisource; not read: 1556, 1758, 1681, 1715.
   **Apply:** `Matt.27.37` la: `\v 37 Posuērunt autem` → `\v 37 Posuerant autem`
24. **Matt 27:47** *quīdam hōrum,* → *quīdam eōrum,*. **1573** (canvas 774, page image): *quidam eorum, qui illic aderant, dicebant*. 1556 *eorum* too.
   Collation: 1573, 1556, 1681, 1747, 1750 *eorum*; as your text: Wikisource; not read: 1715.
   **Apply:** `Matt.27.47` la: `quīdam hōrum,` → `quīdam eōrum,`
25. **Matt 27:47** *aderant, dīcēbat eum* → *aderant, dīcēbant eum*. **1573** (canvas 774, page image): *dicebant eum vocare Eliam*. plural with *quīdam* (ἔλεγον); 1556 *dicebant* too.
   Collation: 1556, 1758, 1747, 1750 *dicebant*; as your text: Wikisource; not read: 1573, 1681, 1715.
   **Apply:** `Matt.27.47` la: `aderant, dīcēbat eum` → `aderant, dīcēbant eum`
26. **Matt 27:55** *secūtæ fuērunt, eī* → *secūtæ fuerant, eī*. **1573** (canvas 774, page image): *Galilęa ſecutæ fuerant, ei miniſtrantes*. pluperfect (ἠκολούθησαν … διακονοῦσαι: “who had followed”).
   Collation: 1573, 1758, 1747 *fuerant*; as your text: Wikisource; not read: 1556, 1681, 1715, 1750.
   **Apply:** `Matt.27.55` la: `secūtæ fuērunt, eī` → `secūtæ fuerant, eī`
27. **Matt 28:1** *nocte hebdomadis, quæ* → *nocte septiduī, quæ*. **1573** (canvas 774, page image): *EA autem nocte ſeptidui, quæ in primam à Sabbato*. Castellio's *septiduī* (“of the week”, σαββάτων) in 1573 and 1747; Wikisource has *hebdomadis*. *septiduum* is not in the lexicon (`latin macron septidui`: no source knows the form); only the genitive *-ī* is marked, the stem is left for stage 4.
   Collation: 1573, 1747 *septidui*; as your text: Wikisource; not read: 1556, 1758, 1681, 1715, 1750.
   **Apply:** `Matt.28.1` la: `nocte hebdomadis, quæ` → `nocte septiduī, quæ`
28. **Matt 28:2** *Dominī cælō dēgressus* → *Dominī dē cælō dēgressus*. **1573** (canvas 774, page image): *Domini de cœlo degreſſus*.
   Collation: 1573, 1750 *de*; as your text: 1758, Wikisource; not read: 1556, 1681, 1715, 1747.
   **Apply:** `Matt.28.2` la: `Dominī cælō dēgressus` → `Dominī dē cælō dēgressus`
29. **Matt 28:7** *antecēdere, illī eum* → *antecēdere, illīc eum*. **1573** (canvas 774, page image): *antecedere: illic eum viſuros eſſe*. “there shall ye see him” (ἐκεῖ αὐτὸν ὄψεσθε); 1715, 1747 *illic*.
   Collation: 1715, 1747 *illic*; as your text: Wikisource; not read: 1573, 1556, 1758, 1681, 1750.
   **Apply:** `Matt.28.7` la: `antecēdere, illī eum` → `antecēdere, illīc eum`

## 3. Matt 19:4: Castellio's L. … G. passage (1)

1573 prints *qui principio fecit L. hominem, G. eos marem & fæminam* (canvas 765, OCR; 1556 *L; hominem*; 1715 *L, hominem G.*): *hominem* is from the Latin (Vulgate *qui fecit hominem ab initio*). Your draft already has *quī prīncipiō fēcit hominem, eōs marem* with no marks, as Luke 10:1 *septuāgintā duōs* and the Luke 11:7 clause (decision 23, item 10) in the settled chapters. **Proposed: keep it so** (marked words kept, unmarked), with the marks recorded among the variants (`data/witnesses/ocr-1573/Matt.tsv` will carry the `L…G` flag once Matthew 14–28 is aligned as gold). Nothing to apply.

The aligner found one more marked word in the settled chapters: **Matt 8:18** *iussit L. discipulos G. traijcere* (1573 canvas 755, page image; 1758 too). Your text has *jussit discipulōs trājicere*, unmarked, consistent with the rest. Nothing to apply.

**Decision:** accept (keep unmarked) (Nathan, 2026-11-07)

## 4. Recorded variants: 1556 against 1573 (4)

Where 1573 reads as your text and 1556 (with the early-line printings) differs. These are recorded, not applied (decision 24). 1556 is cited from its OCR only (e-rara 10281656; not read on the image).

| Place | 1573 (= your text) | 1556 | Also |
|---|---|---|---|
| Matt 15:13 | *meus pater cælestis* | *cælestis* absent | 1715, 1747, 1750 |
| Matt 17:9 | *præcēpit iīs Jēsūs* | *iīs* absent | 1747, 1750 |
| Matt 18:14 | *Sīc voluntās nōn est* | *voluntatis* | 1715, 1747 |
| Matt 25:40 | *Quibus respondēbit rēx: ‘Certō scītōte* (canvas 771, page image) | *respondens … inquiet* | 1715, 1747, 1750 (*respondens*, *inquiet*) |

**Decision:** accept (record as variants) (Nathan, 2026-11-07)

## 5. Not proposed

- **1573 alone against your text** (681 places): read where the reading looked like a real word; every one was 1573's OCR (*eú prehendit*, *fremebãt* = *fremebant* at 20:11, *ille* for *illæ* at 28:8 is uncertain on the image and left) or a marginal reference run into the line (*Marc*, *Luc*, *Zach*).
- **1573 with your text, two or more later printings against it** (81): the early line of 1715, 1747 and 1750 (e.g. 20:15 *An ideo tuus oculus*, 27:53 *in sacram urbem*), and OCR. Your text follows the base.
- **Matt 25:25** *Id veritus iī* (1573 *iui*, page image), **20:5, 21:30** and the other *-īv-* perfects of *eō*: a form question, in `matt14-28-spelling.md`.
- **Matt 16:26** *æquiperet* (1573 *æquiparet*, page image): spelling, in `matt14-28-spelling.md`.
- **Chapter summaries** (decision 3): the draft has none (nor do the settled chapters' USFM); 1573 prints them (e.g. Matt 28, canvas 774). Not proposed here.
