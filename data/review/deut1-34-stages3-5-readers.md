# Deuteronomy 1–34, stages 3–5: the readers' and proofreaders' notes

Eight readers (1–3, 4–6, 7–10, 11–14, 15–20, 21–26, 27–30, 31–34) and four proofreaders (1–8, 9–17, 18–27, 28–34), 2026-11-18, under the briefs summarized in `deut1-34-stages3-5.md`; their rows are in `data/decisions/Deut.layout.tsv` and `Deut.forms.tsv`. The names reader's table is `deut1-34-names.md`. Kept as written (internal notes); where a call was changed after them, `deut1-34-stages3-5.md` says so.

## Reader 1: Deuteronomy 1–3

**Rows**: 23 layout (`r1.layout.tsv`), 46 forms (`r1.forms.tsv`). `check.py 1 1-3 --all` runs with no ERROR (112 verses).

### Quotation structure

- 1:1–5 the narrator; 1:5 ends *hujusmodī verbīs:*, and Moses' discourse (1:6–3:29) stays unquoted, as the voice of
  the book (BSB). A new paragraph at 1:6 where the discourse begins.
- Almost everything Moses reports is in **reported speech** in Castellio and stays unmarked: God at Horeb (1:6–8),
  Moses' own words to the people (1:9–13, 1:20–21, 1:29–31), the people (1:14, 1:22, 1:27–28, 1:41), the spies (1:25),
  the charge to the judges (1:16–17), God's oath (1:34–36), God's warnings (1:42; 2:2–7; 2:9, with the note 2:10–12
  in acc. and inf.; 2:13; 2:31; 3:2), the message to Sihon (2:26–29), the commands of 3:18–22, Moses' prayer (3:24–25,
  *ut … daret*) and God's refusal (3:26–28). 1:12 and 1:17 lose a capital after a colon (reported, going on).
- **Direct, quoted** (three places, all God's words, no inner level):
  - 1:38–40, after *negāvit mē eō esse ventūrum:* (1:37): “Jōsua,” inquit, “Nūnis fīlius, … versus.” (decision 65).
  - 2:18–19, after *allocūtus est mē Jōva.*: “Trānsitūrus es,” inquit, “hodiē … possidendam.”
  - 2:24–25, God's words resuming after the note on the giants (2:20–23, indicative, outside the quotation as the
    BSB): “Agite proficīsciminī … percellantur.”
- The BSB's parentheses (2:10–12, 2:20–23, 3:11, 3:13b) are not added: 2:10–12 is acc. and inf. inside the reported
  command; 2:20–23 is set off by closing the quotation and a paragraph.

### Paragraphs

Added `p` at 1:6 (discourse begins), 1:37 (the second sentence, a new speech), 2:2, 2:8, 2:14, 2:20 (the 487-word
paragraph 1:41–2:23 split, decision 52, each where BSB and WEB break and a sentence begins), 2:26, 2:31 (the 275-word
paragraph from 2:24 split), 3:18 (the command to the eastern tribes; BSB and WEB break). The draft's others kept.

### Poetry

None in 1–3 (the BSB sets none).

### Capitals

*Amorræō* 3:2, *Hesebōnium* 3:6, *Cisiordaninam* 3:8, *Transiordaninam* 3:25 (adjectives of peoples and places, as
the settled *Trānsjordānīnā*, Matt 4:25, Mark 3:8). **The last two rows carry the draft's i**: if the names reader's
respelling (*cisjordaninam*, *transjordaninam*) lands in the draft first, these two layout texts need the j too.
3:24 *deus* lower case: *nūllus … neque in cælō, neque in terrā deus* is any god (decision 20).

### Forms (the main kinds)

- Ablative *Jōvā* (proposal had *Jōva*): 1:10, 1:21, 2:12, 2:29, 2:30, 2:36, 3:20#1 (settled *ā Jōvā* 59 to 1).
- Other ablatives the proposal left short: 1:24 *explōrātā*, 1:32 / 1:42 / 3:26 *eā*, 2:5 / 2:9 / 2:19 / 3:24 *terrā*,
  2:7 *vāstā illā*, *nūllā*, 2:10 *potentiā*, 2:12 / 2:22 *dēlētīs*, 2:20 *eāque*, 2:28 *pecūniā*, 3:2 *incolā*.
- 1:7 *merīdiāna* (acc. pl. among *loca*, the proposal had the ablative).
- Perfect subjunctive *-erīmus/-erītis* (the settled rule): 1:31 *vīderītis*, 2:7 *indiguerītis*, 2:33 *occīderīmus*,
  2:34 *cēperīmus*, *interfēcerīmus*, 3:4 *expugnāverīmus*.
- *concīdō* / *occīdō* / *excīdō* (cut down, kill) not *-cidō* (fall): 1:44 *concīdit*, 3:3 *occīdimus*, 3:6 *excīdimus*.
- 1:46 *moræ* (delay, Gaffiot *mŏra*), not *mōræ*. 2:1 *circumīvimus*. 2:24 *trānsīte*. 2:27 *rēctā* (adverb).
  2:30 *ēvēnit*. 1:16 *jūstē*. 3:29 *domūs* (gen. after *ē regiōne*). 3:26 *nōn modo* (settled 4 to 1).
- *īnfēst-* (Gaffiot, settled 21 to 1): 2:4, 2:9, 2:19.
- 1:11 *mīllecuplō*: in no dictionary; *mīlle* + *-cuplus* as Gaffiot's *centuplus*.

### Suspected errors in the words

- **3:25 *hanc mihi suō veniam daret***: *suō* agrees with nothing (*veniam* is feminine); *suam* would be expected.
  The page has *suo* (read-1738 leaf 232, col. 0, line 6, *#26 hanc mihi suo veniam daret*), so it may be Castellio's
  own slip or a 1738 misprint. Left as printed; worth a look in another printing.
- None other found. (1:23 *placuisset; dēlēgī* and 3:1 *convertissēmus: ēgressus* are Castellio's punctuation and are
  left as they are.)

### Names noticed (for the names reader)

- *Arœre* (2:36, 3:12): the draft's *Aroere* has been given the œ ligature; Aroer is *A-ro-er* (Hebrew עֲרֹעֵר), not a
  diphthong.
- *Ogum* (1:4, 3:3) unmarked beside *Ōgus*, *Ōgī* (3:1, 3:4, 3:10, 3:13).
- *Mōabitās* (2:9) beside *Mōabītārum*, *Mōabītīs*, *Mōabītæ*; *Ammonitīs* (2:20) beside *Ammonītās*, *Ammonītārum*.
- *Enaquinis* (2:10, 2:21) unmarked beside *Enāquīnōs* (1:28, 2:11).
- *Basana* (3:4, 3:10 ×2, 3:13) unmarked beside *Bāsānam*, *Bāsānæ*; *Basanense* 3:13.
- *Galaadī* (3:12) beside *Galaādum*, *Galaādō*; *Hesebonium/-ius* unmarked beside *Hesebōnem*; *Hesebonis* (3:2).
- *Cadesbarnea* (2:14 ablative, unmarked) beside *Cadesbarneam*.
- *Esainos, Esainis, Esaini* (2:12, 2:22, 2:29) unknown; *Aris* (2:29, of Ar) a homograph left unmarked (not *ārīs*).
- *cisiordaninam* 3:8, *transiordaninam* 3:25 (i → j).

### Doubtful calls (my choice first)

1. 1:31 *vīderītis* (perfect subjunctive in reported speech, a past seeing) rather than the future perfect.
2. 2:30 *quemadmodum ēvēnit* (perfect: as it turned out) rather than the present *ēvenit*.
3. 3:13 the closing comma becomes a full stop (3:14 *Jāīr quidem … cēpit* is a new sentence); a semicolon would also do.
4. 1:6 a paragraph after the narrator's colon (*hujusmodī verbīs:*), so the discourse visibly begins.
5. 1:38 “Jōsua,” inquit, “Nūnis fīlius …: *inquit* falls between the name and its apposition; set off by decision 65
   all the same.
6. 2:10–12 and 2:20–23 left without the BSB's parentheses.

## Reader 2: Deuteronomy 4–6

**Rows**: 20 layout (`r2.layout.tsv`), 49 forms (`r2.forms.tsv`). `check.py 2 4-6 --all`: 107 verses, no ERROR.

### Quotation structure

- **4:1–40** Moses' first discourse, unquoted (the voice of the book, as the BSB). Nothing inside it is direct:
  4:6 the nations' praise is reported (*fateantur, hanc tantam gentem … esse*), 4:10 God's command reported (*ut ad sē
  populum convocārem*), 4:21 God's oath reported (*jūrāvit mē nōn esse trājectūrum*): no marks, though the BSB quotes 4:6
  and 4:10.
- **4:41–49** narrator (cities of refuge; the introduction to the law): unquoted, \p at 4:41 and 4:44 as the draft.
- **5:1** narrator, then the second discourse from *ad hunc modum: Audīte* (capital; unquoted, BSB 5:1b–26:19).
- **5:6–21** the Decalogue, God's words given directly after *Locūtus est autem in hunc modum:* (5:5): “…” opened at 5:6,
  closed at 5:21, one paragraph of prose (240 words) as the settled Exod 20:2–17; the BSB's li1 not taken.
- **5:24–27** the people's words, direct (*nōbīs, noster, audīvimus*): “Ēn … faciēmus.” *nē, inquam* (5:25) is the
  speakers' own, not a speech tag; 5:26's parentheses kept.
- **5:28–31** God's reply, direct: “Audīvī … datūrus.” The message of 5:30 is reported (*Ī renūntiātum iīs, ut … revertantur*):
  no inner ‘…’ though the BSB has ‘Return to your tents.’
- **5:32–6:25** Moses again, unquoted. 6:4 the Shema with a colon after the call (*Audīte Isrāēlītæ: Jōva …*, as the
  settled Mark 12:29). 6:20–25: the children's question is indirect (*quid sibi velint*) and the answer after *sīc
  respondētōte:* is reported throughout (accusative and infinitive: *vōs … ēductōs esse*, *Jōvam … præcēpisse*,
  *indicārī*, *vōs … habitūrōs*): unmarked, though the BSB quotes 6:20–25.

### Paragraphs

Added \p at 4:9 (4:1–14 was 328 words; BSB + WEB), 4:25 (4:15–31 was 324 words; KJV ¶ and BSB, the WEB has no break
anywhere in 4:9–40), 5:6 (the Decalogue begins; WEB \m), 5:23 (BSB), 5:28 (God's reply; BSB + WEB), 5:32 (Moses
resumes; BSB + WEB), 6:4 (the Shema; BSB + WEB; 6:1–19 was 283 words), 6:10 (BSB + WEB). Removed the draft's \p at 5:5,
which fell inside the sentence begun at 5:4 (*Vōbīscum Jōva … locūtus est, cum quidem ego …*): 5:1–5 is one paragraph.

### Poetry

None in 4–6 (the BSB sets none).

### Capitals and punctuation

*Amorræī* 4:46, 4:48; *Cisjordanini* 4:48, *Cisiordaninum* 4:49 (as the settled *Trānsjordānīnā*, Matt 4:25, Mark 3:8);
*Ægyptiæ* 6:12; 4:34 *ūllus deus* lower case (any god). Colon before *neque enim* at 5:11 (the draft has no point;
as the settled Exod 20:7).

### Forms (the main kinds)

- Ablative *-ā* where the proposal had *-a*: *in/dē/sub/cum terrā* (4:5, 14, 18 ×2, 26, 36, 40, 47; 5:8 ×2, 16, 31, 33;
  6:1, 15), *in aquā* 4:18, 5:8, *vestrā causā* 4:21, 4:34, *bonā frūge* 4:25, *vītāque … prōductā* 4:26, *grātiā* 4:36,
  *magnā vōce* 5:22, *salvā vītā* 5:26, *Hāc vestrā … ōrātiōne* 5:28, *tōtā … domō* 6:22, *rē ipsā* 6:25.
- The reverse, *-a* not *-ā*: *sua dicta* 4:10, *audīta sit* (nom.) 4:32, *audīta faciēmus/faciātis* 5:27, 6:3,
  *in sua tabernācula* 5:30, *bonaque oppida* 6:10.
- Ablative absolutes: *audītīs* 4:6, *occupātīs* 4:25. *in hōc* 4:6. Genitives *sōlis* (of *sōl*, not *sōlīs*) 4:41, 4:48,
  *domūs* 4:45.
- *hīc* adverb 5:3, 5:31; *sānctē* adverb 5:12; *modo* in *sī modo* 4:29; *solum* the soil (short o) 4:22; *opusque*
  (*opus*, short u) 5:13; *irrītāveritis* (*irrītō*, long ī) 4:25.
- Subjunctive vs future perfect: *vīderītis* 4:15 (causal *cum* inside the *nē* clause), *cūrāverītis* 6:25 (the *sī*
  clause inside the reported answer).

### Suspected errors in the words

- **4:9 *aduertite***: the u/v conversion missed it (1738 leaf 232, col. 1, line 67, *atque etiam aduertite*); in the
  draft's conventions it is *advertite* (cf. *cisiordaninum*). I left it, as the brief says; it needs a stage-2 fix or a
  spelling row before settling.
- None else found in 4–6: every verse reads as Latin and agrees in sense with the KJV/BSB.

### Names for the names reader

- *cisjordanini* 4:48 beside *cisiordaninum* 4:49 (j missed).
- *Sehonis* (Sihon, 4:46) and *Seonem* (Mount Siyon = Hermon, 4:48, Hebrew שִׂיאֹן) are different names: keep apart.
- *Baalphegorem* 4:3 ×2 and *domus Phegoris* 4:45 (Beth-peor): one Peor.
- *Basana* 4:43 (abl.) and *Basanae* 4:47: one stem. *Rubenitarum* 4:43 beside the settled Num adjectives *Rūbēnīna,
  Rubenitis*. Others: *Beser, Ramotha, Galaado, Gaulanitidem, Gadinorum, Manassensium, Hesebonem, Ogi, Aroere, Arnonis,
  Hermon, Phasga, Horebo, Massam, Abrahamo, Isaaco, Jacobo, Pharaonis*.

### Doubtful calls (my choice first)

1. **4:25 \p**: 4:15–31 runs 324 words, but the WEB never breaks in 4:9–40, so decision 52's "BSB and WEB together" is
   not met; I split where the KJV (¶) and BSB break and the subject turns to exile. Alternative: leave 4:15–31 whole.
2. **5:6 \p**: the Decalogue opens its own paragraph (240 words); the settled Exod 20 keeps its one-verse introduction in
   the same paragraph. Here the introduction belongs to the sentence of 5:4–5, and joining them would make 277 words.
3. **4:34 *ūllus deus*** lower case (BSB "any god", Hebrew אֱלֹהִים); the KJV has "God" and Brenton Θεὸς.
4. **5:25 *audīverīmus*** left as proposed (perfect subjunctive, the *sī* clause inside the *nē … moriāmur* clause);
   the future perfect *audīverimus* is possible if the clause is read as independent of the subjunctive.
5. **Capitals for *Cisjordanīnus*** (4:48–49), as Matt 4:25 and Mark 3:8; the settled Mark 10:1 has lower-case
   *trānsjordānīnum*, which looks like a slip.

## Reader 3: Deuteronomy 7–10

**Rows**: 18 layout (`r3.layout.tsv`), 40 forms (`r3.forms.tsv`). `check.py 3 7-10 --all`: 97 verses, no ERROR.

### Quotation structure
- All four chapters are Moses' discourse, unquoted (as the BSB). No speech inside chapters 7, 8 or 10 is given
  directly: 7:17 and 8:17 (what they might say in their hearts), 9:4 (the same), 9:23 (*ut proficīscerēminī*),
  10:1–2 (*mandāvit, ut … secārem; sē … scrīptūrum*), 10:11 (*ut … anteīrem*) are all reported: unmarked, though the
  BSB quotes them.
- 9:2 the saying about the Anakim, a direct question: “Quis Enaquinīs resistat?”
- 9:12–14 God to Moses on the mountain, direct: “Age, dēscende … 9:13 Videō sānē,” inquit, “populum esse cervīcōsum.
  9:14 … dēdūcam.” One speech in the Latin (the BSB closes at 9:12 and reopens at 9:13 for the Hebrew's new *said*;
  Castellio has *inquit* instead), so *inquit* is set off by commas, closed and reopened (decision 65).
- 9:26–29 Moses' prayer: “Domine Jōva, nōlī … ēdūxistī.” The nations' words inside it (9:28 *Jōvam, quoniam nōn
  posset … eōs ēdūxisse*) are reported: no ‘…’.

### Paragraphs
Over 250 words (decision 52): 7:12–26 (304) split at 7:17 (the BSB; the WEB has no break in 7:12–26); 8:1–20 (371)
at 8:11 and 8:19 (BSB and WEB both); 9:7–29 (455) at 9:15 (BSB and WEB both) and at 9:25 for the prayer (the BSB
breaks at 9:26, inside the Latin sentence *jacuī … eumque hīs verbīs supplicāvī*, so moved to its start). 10:1–11:
10:6 (the narrator's note on the journeys and the Levites; KJV, BSB, WEB all break) and 10:10 (Moses resumes; BSB and
WEB). Paragraphs now: 7:1, 7:12, 7:17, 8:1, 8:11, 8:19, 9:1, 9:7, 9:15, 9:25, 10:1, 10:6, 10:10, 10:12.

### Capitals and punctuation
*Ægyptiæ* 8:14, *Lēvīticam* 10:8 (adjectives); *Domine Jōva* 9:26 (as the settled Gen 15:2); *dominōrum Dominus*
10:17 (as the settled Rev 17:14, 19:16). Vocative commas *Audīte, Isrāēlītæ:* 9:1 and *Nunc, Isrāēlītæ, quid* 10:12
(as the settled Acts 2:22): the same call is due at 6:3, 6:4, 20:3 for whichever readers have them.

### Poetry
None in 7–10 (the BSB sets none).

### Forms (main calls)
Ablatives the proposal missed: *apertā* 7:10, *terrā* 7:13, *nātūrā* 7:24 and 9:14, *mannā … ignōtā* with *pāvit*
8:3 and 8:16, *pēnūriā*, *ūllā* 8:9, *marmoreā* 8:15, *Jōvā* 9:3 (ablative absolute; the second *Jōva* nominative),
*tuā* 9:26, *tuā magnā vī* 9:29, *factā arcā ligneā* 10:1, *arcā* 10:2 and 10:5, *eā* 10:14, *vestrā causā* 10:21.
Others: *fuerītis* 7:3 (prohibition), 10:19 (*ut quī*, as Exod 23:9); *audieritis* 7:12 (future perfect, in the new
spelling); *frūctūs* 7:13 (acc. pl.); *ūlla* 7:14; *populōsiōrēs* 7:17; *pāvit* (*pāscō*) 8:3, 8:16; *mālīs pūnicīs*
8:8; *vīctūs* (gen.) 8:9; *prēstēribus* 8:15 (Gaffiot prēstēr, ēris); *sua vitia* 9:4 (the proposal had *suā*);
*cervīcōsus/-um* 9:6, 9:13; *offenderītis* 9:7 (indirect question); *pēne* 9:8; *incīdī* 10:3 (*incīdō*, hewed);
*appāret* 10:15 (new spelling).
`check.py` does not apply the proposed spelling rules, so 7:12 *audieritis* and 10:15 *appāret* show unapplied there
(the verses still read *audīverītis*, *adparet*); they take effect once the rules *audiveritis → audieritis*,
*adparet → apparet* are applied.

### Suspected errors in the words
- **7:13 *aluorum***: 1738 prints *aluorum* (read line leaf 236, col. 1, line 94); in the draft's conventions it is
  *alvorum* (*alvus*, belly: KJV *the fruit of thy womb*). The u/v conversion missed it; the proposal has *aluōrum*.
  To respell *alvorum* in the draft (the marking *alvōrum* then follows).
- No other word looks wrong. 9:15 *revertī … dēscendere* reads as two historical infinitives (*revertor*), not a
  misprint.

### Names (for the names reader)
- *Enaquinorum*, *Enaquinis* 9:2 unmarked (unknown); one stem, *Enaquin-*, through Deut (also *Enaquinos*).
- 10:6–7 *Berothis Jaquanensium*, *Moseram*, *Gadgadam*, *Jothabatham*: Numbers 33:30–33 has *Mōsērōthīs*,
  *Benejaacāne*, *Jothabāthā* (the Hebrew differs in part: מֹסֵרָה / מֹסֵרוֹת, גֻּדְגֹּדָה / חֹר הַגִּדְגָּד;
  יָטְבָתָה is one place, and *Jothabatham* is the accusative of Num's *Jothabātha*: to be marked alike;
  *Berothis Jaquanensium* against Num's *Benejaacāne* for בְּנֵי־יַעֲקָן).
- 9:22 *Taberam* (Num 11:3 *Tabēra*), *Busta cupiditātis* (Num 33:16 capital, Num 11:34 lower case *busta*);
  9:23 *Cadesbarnea* (unknown), also *Cadesbarneam* elsewhere.

### Doubtful calls for Nathan (my choice first)
1. **8:20 *fuerītis*** (perfect subjunctive: the reason is part of what Moses testifies, *testor vōs esse peritūrōs
   … quoniam … nōn fuerītis*, indirect discourse) against *fueritis* (future perfect, if the clause is Moses' own).
2. **9:8 *pēne***: Gaffiot heads *pæne* (*pēne* a variant); the settled NT has *pæne* (Matt, Rev). Marked *pēne*
   here; a spelling rule *pene → pæne* may be wanted (the word occurs once in Deuteronomy).
3. **7:17 paragraph**: the only break in 7:12–26 is the BSB's (the WEB has none); without it the paragraph is 304
   words.
4. **8:3, 8:16 *mannā … ignōtā*** (ablative with *pāscō*, feminine): the settled NT treats *manna* as neuter (John
   6:58 *quāle manna, quō*), but Castellio's *ignota* here can only be feminine singular (or neuter plural, which
   cannot be the ablative), so feminine ablative.
5. **9:12–14 one quotation** with *inquit* at 9:13, rather than the BSB's two.

## Reader 4: Deuteronomy 11–14

**Rows**: 14 layout (`r4.layout.tsv`), 64 forms (`r4.forms.tsv`). Every verse of 11–14 read whole beside the KJV and BSB
(Hebrew where the tense or case needed it); every bold word checked; `check.py 4 11-14 --all` runs with no ERROR.

### Quotation structure
- 11:1–14:29 is Moses' discourse, unquoted (the BSB's structure).
- **One direct speech inside it: 11:14–15, God's words.** Castellio marks the change of speaker himself with
  *ego (inquit) vicissim …* (Hebrew וְנָתַתִּי, "I will give"). Set as “Ego,” inquit, “vicissim … suppetat.” (decision 65:
  parentheses become commas, quote closed and reopened). The condition in 11:13 (*meīs præceptīs … quibus ego vōs hodiē
  īnstruō*) is Moses' formula and stays unquoted; 11:16 *Cavēte* is Moses again.
- Reported, so unmarked although the BSB quotes them: 12:20 (*sī vōbīs carne vēscī libuerit*), 12:30 (*statuātis, quōmodo
  illæ … coluerint, sīc vōs quoque facere*), 13:2, 13:6 and 13:13 (*cohortētur ad deōs aliēnōs … sequendōs*, *ad cultum
  deōrum*, *ad colendum deōs*). 12:25 *inquam* is Moses' own and stays in commas.

### Paragraphs (no poetry in 11–14)
- 12:1–28 ran to ~560 words: `\p` at 12:15 and 12:20 (the BSB and WEB both break, new sentences), and at 12:8 (BSB only;
  12:1–14 was still ~280 words; *Nē facitōte, quemadmodum nōs hīc hodiē facimus* begins a new sentence and unit).
- New laws: 13:6 (the kinsman who entices; BSB and WEB), 14:3 (clean food; BSB and WEB), 14:28 (third-year tithe; BSB).
- 14:4–18 (the BSB's lists) stay prose, with `\p` at 14:9 (water creatures) and 14:11 (birds), as the settled Lev 11:9, 11:13.
  14:12 a colon before the bird list (1738 a comma), as 14:7 *hīs nē vēsciminī: camēlō*.
- 14:21 *Hædum in lacte …* (the draft's line break, the BSB's `\b \m`) left running on in the verse, as the settled Exod 23:19.

### Capitals
*Ægyptium* 11:4, *Ægyptiæ* 11:10 and 13:10 (settled Exod, Lev 24:10, Num 34:5). *rubrī maris* left lower case (settled
*mare rubrum* 6×).

### Forms (main kinds)
- Ablative -ā the proposal missed: *terrā* 11:9, 11:17 (both), 11:21, 12:1, 12:10, 12:29; *pluviā … sērōtinā* 11:14; *illā bonā*
  11:17; *grātiā* 11:18; *eāque* 11:31 (unflagged); *opācā* 12:2; *aliquā* 12:14; *cōpiā*, *capreā* 12:15; *vestrā posteritāte* 12:25;
  *congestā*, *ūniversā* 13:16; *illā* 13:17; *Nūllā … abhorrendā* 14:3; the animal and bird lists 14:5, 14:12–18 (*capreā,
  rūpicaprā, dāmā, camēlopardalī; aquilā, anatāriā; pīcā; harpā; noctuā; cicōniā*); *mundā* 14:20; *pecūniā* 14:25, 14:26;
  *familiā tuā* 14:26.
- **ā Jōvā** (proposal *ā Jōva*): 12:11, 12:21#2, 12:26, 13:5#1, 13:10, 14:25#2.
- Others: *vīctus* (food) 11:15; *fēcerītis* (prohibition) 12:4; *hīc* 12:8; *minōrisve*, *minōribusve* 12:17, 12:21; *dēlēctō*
  (dēligō) 12:18; *datīs* 12:21; *excīderit* (cut off) 12:29; *dēlētīs* (abl. abs.) 12:30; *īdem* (masc.) 13:2; *eādem*, *sinūs*,
  *æquē* 13:6; *manus* (nom. sg., not *manūs*) 13:9; *cuculō* (Gaffiot cŭcŭlus; settled Lev *cuculum*) 14:16-17; *via* (nom.)
  14:24; *petitō* (imperative, not *petītō*) 14:25.

### Suspected errors in the words
None found in 11–14. (12:1 *Deus vester patrius* and 11:2's elliptical *nōn hæc apud nātōs vestrōs* are Castellio's.)

### Names (for the names reader)
No name spelled two ways in 11–14. Names seen: Dathanem, Abiramum, Eliabi, Rubenitae (11:6); Euphrate, Libano (11:24);
Garizimo, Ebale (11:29, both `unknown`); Jordanem/Jordane, Chananaeorum, Galgala, More (11:30); Levitis/Levitas
(12, 14). *rubri maris* 11:4 left lower case, as the settled *mare rubrum*.

### Doubtful calls and pipeline points (for Nathan)
1. **14:16-17 *ībī*** (the ibis, ablative; settled Lev 11:18 *ībim*): the row is written, but `macronize.finish` strips the final
   long ī because *ibi* is in `SHORT_FINAL` (the adverb), so the check prints *ībi*. Needs an exception for this verse
   (or SHORT_FINAL to skip a decided form). My choice: *ībī*.
2. **13:12 *audieritis*** and **14:26 *īnsūmptā***: written in the proposed spelling (rules *audiveritis → audieritis*,
   *insumta → insumpta*), as the brief says; they take effect only once those rules are approved (the check still shows
   *audīverītis*, which is wrong: future perfect, short -i-; and *insumta* unmarked).
3. 11:14 quotation opening at *Ego* (not at 11:13): Castellio's *inquit* marks the turn; the Hebrew's "I" is God's from 11:14.
4. 12:8 paragraph (BSB only) chosen to keep 12:1–14 under 250 words; 12:10 would also do.

## Reader 5: Deuteronomy 15–20

**Rows**: 16 layout (`r5.layout.tsv`), 75 forms (`r5.forms.tsv`). `check.py 5 15-20 --all`: 128 verses, no ERROR; every
verse read through once as it will stand.

### Quotation structure

Moses' laws (15:1–20:20) stand unquoted, as the BSB has them, the voice of the book. Inside them:
- **18:17–20**: God's answer at Horeb, given directly (*suscitābō*, *mea verba*, *ego in eum animadvertam*), in “…”
  from *Bene dīcunt* to *moritor vātēs ille.*, as the BSB. 18:16 (*cum peterētis, nē … audīrētis*) is reported, unmarked.
- **18:21**: the people's thought in their own words (*Quō pactō intellegēmus …?*), “…” after a colon (1738 has a comma).
- **20:3–4**: the priest's address (*Audīte, Isrāēlītæ: … nōlīte*), “…”; 20:2 ends with a colon (1738 a point).
- **20:5–7** and **20:8**: the officers' words. Castellio gives them with imperatives (*repedātō*), not reported
  subjunctives, so they are direct: two quotations, as the BSB, each opening with a capital *Sī quis* after the colon.
- Reported, not marked (the BSB quotes them): 15:9 (the grudging thought, *ut … renuās*), 15:16 (the servant, *sē ā tē
  esse discessūrum*), 17:14 (*sī statueritis vōbīs creāre rēgem*), 17:16 (*cum vōs Jōva … redīre vetuerit*).

### Paragraphs

The draft's \p (the BSB's section breaks) all fall at sentence starts and stay. Added: 18:17 and 18:21 (God's speech and
Moses' return, BSB breaks); 19:11 and 19:14 (new laws, BSB breaks; 19:1–14 was 290 words); 20:5, 20:8, 20:9, 20:10,
20:16, 20:19 (BSB breaks; 20:1–20 was 350 words). No paragraph over 250 words remains.

### Poetry

None in 15–20 (the BSB sets none).

### Capitals

18:6 *israēlīticōrum* → *Isrāēlīticōrum*. God's names were already right. 20:3 a comma before the vocative *Isrāēlītæ*.

### Forms worth noting

- 15:1 *septimō quōque annō*: the ablative of *quisque* (every seventh year), not the adverb *quoque*.
- 15:19 *maria*: neuter plural of *mās, maris* (the males, Hebrew הַזָּכָר). The proposal had *marīa* from the settled
  count of the name Maria.
- 16:3, 16:8 *nōn fermentātīs*: an ablative plural, missed by the proposal (unflagged *fermentātis*). **The settled
  Exodus has the same slip four times** (Exod 12:15, 12:18, 12:20, 13:7 *fermentātis*, ablative plural with
  *vēscor/vīvō*). It is reported here for Nathan only and not changed (the settled text is never rewritten).
- 20:1, 20:19 *nōlītōte* (the proposal's *nōlitōte* is Wiktionary's alone; settled *nōlītō*, the Gen 28:1 row). **Deut
  13:3** (not mine) has the same *nōlitōte* in the preview.
- 17:8 *Sī quæ causa*: nominative (the proposal had *causā*). 19:6 *sī via longior sit*: nominative (the proposal had
  *viā*). 16:6 *sōlis* (sun), not *sōlīs*. 15:18 *gravātē*, the adverb. 19:3 *compōnitōte*. 15:5, 19:9 *sī modo …
  pārēre*.
- Jōvā after *ā/ab* (or in an ablative absolute) in 15:7, 15:15, 15:20, 16:5, 16:7, 16:20, 17:2, 17:8, 17:10, 18:6, 18:9,
  19:1, 19:3, 20:14; 15:2 *indictā Jōvānā remissiōne*. Lēvītā (ablative after *ūnā cum*) in 16:11, 16:14, as the reader's
  Lev 25:33 row. These are case calls; the names reader may want to know about them.
- Plain ablatives: *terrā*, *vestrā*, *tuā*, *familiā*, *culpā*, *vītā*, *eā*, *apertā*, *bonā*, *datā*, *sententiā*,
  *illā*, *istā*, *grātiā*, *repudiātā*, *diūtinā*, *admōtā*; 20:20 *frūctūs* (accusative plural with *edūlēs*).
- Unknowns decided: *mūtuētis*, *ēmigrātiōnis*, *ūnōquōvīs*, *aurīve*, *fīliamve*, *capramve*, *necromantis* (Greek
  νεκρόμαντις, no long vowel). *redemtum* (15:15) is left to the spelling rule (→ *redēmptum*).

### Suspected errors in the words

I found no clear misprint. One doubtful spot is 18:17 *Quum quidem Jova ita mihi respondit*: *cum* with the
indicative where the sense is "Then the LORD said to me" (KJV). It reads as Latin (*cum* inversum after a full stop),
so I left it. It could be checked on the page (read-1738 row for 18:17) if wanted.

### Names (for the names reader)

- 15:12 *Ebræus aut Ebræa*: this book's form, against *Hebræ-* if it occurs elsewhere. Check one form.
- 18:16 *Hōrēbō*, settled marking.
- 18:1 *Lēvis* (genitive of Levi).
- 20:17, the list of peoples (*Hettæōs … Jebūsæōs*), proposed with the settled markings.

### Doubtful calls for Nathan (my choice given)

1. 20:5–8, the officers' words quoted. The 3rd-person imperatives *repedātō* make them direct, so I quoted them.
2. 18:21, the people's question quoted, with 1738's comma made a colon.
3. 15:19 *maria*, the neuter plural of *mās*. It is rare, but the only form the word allows.
4. The paragraphs added to 20:8–20 make short paragraphs (20:8 and 20:9 one verse each), following the BSB.
   An alternative is to join 20:8–9.

## Reader 6: Deuteronomy 21–26

**Rows**: 17 layout (`r6.layout.tsv`), 81 forms (`r6.forms.tsv`). `check.py 6 21-26 --all` runs with no ERROR.

### Quotation structure

All of 21–26 is Moses' law discourse, unquoted (the BSB's structure). Inside it, quoted only where the Latin gives the speaker's own words:
- 21:7–8: the elders' declaration and prayer (“Neque manūs nostræ … sed ā cæde expientur.”). The quotation closes after *expientur*, because *sed* answers *nōlī … vindicāre* and so belongs to the prayer (the BSB's *And the bloodshed will be atoned for* stands outside its quotation; the Latin does not allow that).
- 25:9: the widow's words, “Sīc fit hominī, quī …”; 25:10 the name the house is to bear, “discalceātī.” (decision 39, named words).
- 26:3: the worshipper's profession to the priest (“Profiteor … nōbīs.”).
- 26:5–10: the confession before God (“Majōrēs nostrī … quam mihi Jōva dedit.”).
- 26:13–15: the declaration before God (“Sacrum domō abstulī … abundantī.”).

Reported, unmarked although the BSB quotes them: 21:20 (*sīc loquuntor: hunc fīlium suum … esse*), 22:14 (*dīxeritque, sē … nōn invēnisse*), 22:16–17 (the father: *sēsē fīliam suam … dedisse … negāns, sē …*), 25:7 (*dēmōnstrātō, lēvirum suum nōlle …*), 25:8–9 (*negāverit, sē velle*). 26:17–18 are reported (acc. + inf.), as in the BSB.

### Paragraphs

The draft's breaks (the BSB's section starts) kept. Added where the BSB and WEB both break: 22:5 (22:1–12 ran to 197 words, from strayed animals to the mixed laws), 22:22 (22:13–30 was 285 words), 24:14 (24:6–22 was 278 words) and 26:12 (26:1–15 was 317 words, so the third-year tithe starts a new paragraph). 23:22 now ends with a full stop and 23:23 starts *Prōmissum* with a capital (a new command). 26:18 has its comma moved after the parenthesis *(ut vōbīs prōmīsit),*. 22:18 *Isrāēlīticæ* is capitalized.

### Poetry

None (the BSB sets no `q1` in 21–26).

### Forms: kinds of fix

- **Ablatives -ā** the proposal missed: *terrā* (21:1, 23:7, 23:20, 25:15, 25:19, 26:2), *eā* (21:4, 21:13, 22:13, 22:14 ×2, 22:17, 24:1, 25:5, 26:1), *injūstā*, *mēnstruā diē*, *āmissā … repertā rē*, *lōrīcā*, *lānā*, *habitā*, *expānsā*, *puellā*, *fēminā* (22:22#1), *vītā*, *aquā*, *tuā* (23:23, 26:4, 26:15), *leprā*, *vestrā*, *ūllā misericordiā*, *nātūrā*, *datā*, *inditīs*, *nostrā* ×2 *animadversāque … miseriā*, *mæstitiā*, *sacrā*, *Lēvītā* (26:11, case ending only), *dēfatīgātīs*.
- **Jōvā in the ablative** (proposed *Jōva*): 21:10 (*Deō vestrō Jōvā trādente*), 24:18 and 26:2#1 (*ā Jōvā*), 26:5 (*cōram Jōvā*). The proposal seems to leave every ablative *Jōva* unmarked, so the other readers' chapters probably have the same slip.
- **Wrong homographs**: 22:3 *Īdēm* → *idem* (neuter); 21:15 *utrāque* → *utraque* (nominative); 21:16 *suā* → *sua* (*bona sua*); 25:13 *Dīversā* → *Dīversa*; 22:6 *ova/ovis* → *ōva/ōvīs* (eggs); 22:12 *teges* → *tegēs* (future); 23:11 and 24:13 *solīs* → *sōlis*; 23:20 *vadīs* → *vādis*; 23:23 *vovēris* → *vōveris*; 24:15 *occīdat* → *occidat* (the sun sets); 26:15 *sedē* → *sēde*, *fave* → *favē*; 26:19 *condītās* → *conditās* (made, not seasoned); 26:10 *hic* → *hīc* (here); 25:16 *inīque* → *inīquē*; 22:21 *domus* → *domūs* (genitive); 22:21–22 *cōnstūprārit* → *cōnstuprārit* (Gaffiot cōnstŭprō); 21:17 *virium* → *vīrium*; 21:4 *vexerit* → *vēxerit*; 22:4 *præteritō* → *præterītō* (imperative of *prætereō*).
- **-erīs / -eris** (the settled rule: perfect subjunctive *-erīs*, future perfect *-eris*): 23:15 *nē dederīs*, 23:22 *fuerīs* (after causal *cum*), 23:24 *intrāveris* (future perfect, not *intrāverīs*). 24:22 *meminerīs* left as proposed.
- **Unknowns**: *incōnsitam*, *immōrigerum*, *heluōnem*, *superiōremve*, *pignorārentur*, *mūtuābis* ×2, *Quadrāgēsiēs*. Left as proposed: *bovemve*, *pignorantor*, *glossem*.

### Suspected errors in the words

- **23:25 *introjeris***: 1738 prints *introieris* (read-1738 leaf 252, col. 1, lines 73–74, *in-|troieris*). The i is a vowel (*intrō-ieris*, perfect *introiī*; the settled *introiērunt*), so the draft's j is a conversion slip. It should be *introieris*. That is a spelling change in the draft, outside my rows; it still stands as *introjeris* in the preview.
- **25:3 *Quadragesies*** (leaf 253, col. 1, line 74): Castellio's form, not classical (*quadrāgiēs*). It is printed so: kept, and marked by analogy (*Quadrāgēsiēs*). Doubtful.
- **25:7 *glossem*** (leaf 253, col. 1, line 89, beside *glos*): the classical accusative is *glōrem* (Gaffiot glōs, glōris). Castellio seems to decline *glōs, glossis*. It is printed so: kept unmarked.
- **22:27 *reperit***: the sense is past (KJV *he found her*). It is either the perfect written with one p (*repperit*) or a historic present. Left unmarked, as the settled Gen 37:15 *reperit*.

### Names (for the names reader)

- 23:17 ***Isrælitidum***: the proposal has *Isrælitidum* (æ for the a–e of *Isrāēl*), which is wrong. It should be *Isrāēlītidum* or similar, marked as *Isrāēlīt-*.
- 23:4 *Pethore* is unknown. 23:3 *Ammonita* (homograph, *-a/-ā*): it is nominative. 23:7 *Idumæo* is unknown.
- 26:5 *Syrīs*: Castellio has *majōrēs nostrī, Syrīs eōs opprimentibus* (our forefathers, the Syrians oppressing them) for the Hebrew אֲרַמִּי אֹבֵד אָבִי, a reading that may merit a light footnote (decision 56).

### Doubtful calls for Nathan (my choice given)

1. 21:8: the quotation closes after *sed ā cæde expientur* (part of the prayer), not before it as in the BSB.
2. 25:10: *dīcātur “discalceātī.”* is in quotation marks as a name (decision 39). It could also stay unmarked.
3. 26:10 *hīc* (adverb, “here I bring”) rather than *hic ego*.
4. 23:22–23: a full stop after *in vitiō* and a capital *Prōmissum*. 1738 has a comma; the punctuation is modernized.
5. 25:3 *Quadrāgēsiēs*: the marks are by analogy only.

## Reader 7: Deuteronomy 27–30

**Rows**: 54 layout (`r7.layout.tsv`), 70 forms (`r7.forms.tsv`). `check.py 7 27-30 --all` ran with no ERROR, 143 verses.

### Quotation structure

- **27:1–8**: the narrator (*Tum Mōsēs … in hunc modum:*), then Moses' charge about the stones and the altar in “…”, from *Cōnservātōte* to 27:8 (BSB).
- **27:9–10**: the narrator, then Moses and the priests in “…” (*Attende et audī, Isrāēlīta … exsequitor.*). Comma added before the vocative.
- **27:11–26**: the narrator (27:11), then Moses' command in “…” from 27:12 (*Hī … stantō*). The Levites' curses inside it are in ‘…’, and so is the people's spoken *Āmēn*, with a capital (decision 39; the settled Num 5:22 *‘Amen, amen.’*). Each curse is its own paragraph and reopens Moses' speech with “‘ (as ESV). The colon or semicolon after each curse becomes a full stop with *Et* capitalized, following Castellio's own 27:15. The speech closes at 27:26 with ’”.
- **28**: Moses' discourse, unquoted as the voice of the book, like 5–26. **Doubtful, see below.** Castellio reports 28:67 (*māne vesperam … optētis*) and 28:68 (*quam viam nē … repeterētis*), so neither is marked.
- **29:1** is the narrator's heading and now has its own `p` (the draft's `\nb` ran it on from 28:68). **29:2** has the narrator's frame, then Moses' third discourse, unquoted from *vōs vīdistis*, with a lower-case start as the preview has 5:1.
- **29:19**: the man's thoughts are reported. **29:22–28**: the nations' question is indirect (*cūr … fēcerit*, *quisnam sit*), so it has no marks, and its two question marks are dropped (decision 25). The answer (29:25–28: *quoniam … dēfēcerint*, *Jōvam … importāsse*) is reported and unmarked.
- **30:12–13**: the people's words are given directly (future indicative, *nōbīs*, *audiāmus*), so “Quis …?” is quoted with a capital. The BSB has ‘…’ there, but the discourse around it is unquoted here, so these are first-level marks.

### Poetry

- **28:3–6 and 28:16–19**: `q1` with a `\q2` at the BSB's line breaks. 28:4 and 28:18 have two lines each, following Castellio's two parts (the fruits of womb, soil and cattle, then *tum armentōrum, tum gregum … fētūra*). 28:5 and 28:17 have one line each. Prose resumes with `p` at 28:7 and 28:20.
- **29:5–6**: the BSB sets these as `q1`, and the brief says to follow it, so each has two lines. Prose resumes with `p` at 29:7. **Doubtful, see below.**

### Paragraphs

The draft has only 28:1 and 28:15 in chapter 28: the BSB's `b m` breaks were not passed on. Where the Latin sentence ends at a BSB break, I added one:

- **Chapter 28**: 28:7, 20, 27, 30, 35, 38, 45, 49, 54, 56, 58, 63, 66. No paragraph exceeds about 125 words.
- **No break at 28:53**: it continues 52's *ita premet, ut …*.
- **Chapter 27**: 27:9, plus the curses (27:15–26).
- **Chapter 29**: 29:1, 2, 7, 10, 16, 25, 29. The break at 29:25 splits 29:16–28, which is 285 words (decision 52). The BSB's breaks at 29:18 and 29:22 fall inside Castellio's sentences.
- **Chapter 30**: 30:7, 15, 19.
- **Capitals**: *Isrāēlīticō* (27:1), *Ægyptiīs* (28:27), *Ægyptiās* (28:60).

### Forms (the main calls)

- **Ablatives the proposal marked short**: *eāque* 27:6; *clārā* 27:14; *ūllā bēstiā* 27:21; *ūllā* 28:14; *terrā* in 28:8, 11, 21, 23, 64, 29:28, 30:16, 18; *dōnātā* 28:8; *tantā* 28:21, 53; *āmentiā* 28:28; *plantā* 28:35; *vestrā* 28:46; *cōpiā* 28:47; *pēnūriā* 28:48; *aquilā* (comparison) 28:49; *angustiā* 28:53, 57; *arctā* 28:55; *summā indigentiā* 28:57; *vītā vestrā* 28:67; *Tantāque* 28:66; *īrā* 29:20, 23; *nātūrā* 29:20; *eā* 29:23; *audītīs* (ablative absolute) 29:19; *mūtātīs* 30:8; *Jōvā* (with *ūtēminī*) 30:16.
- **Nominatives the proposal marked long**:
  - *arēna* 28:24 (*pluvia arēna sit*)
  - *ruīna* 29:23 (*quālis est ruīna Sodomæ*)
  - *prōposita* 30:1 (neuter plural, subject)
- **Other forms**:
  - *frūctūs* (plural) 28:4, 18, 51; *tribūs* (nominative plural) 29:10.
  - *complexūs* (genitive, "the wife of his bosom") 28:54, 56; *hīc* ×2 29:15.
  - *modo*, the adverb in *modo … sītis* and *sī modo*, at 28:2, 9, 13 (settled *sī modo* 10 : 1).
  - *pārēre* 28:1, 15; *cecīderit* (*caedō*, strike down) 27:24; *dīcetque* 29:22.
  - Perfect subjunctive in the indirect questions *dēgerīmus*, *trānsīverīmus* 29:16.
  - *īnfēst-* (Gaffiot; the settled text 14 : 1) in 28:21, 45, 61, 30:7 and *īnfēstātiōnēs* 29:3.
  - Adverbs *expressē* 27:8 and *beneficē* 30:9.
  - Unknown words marked: *mūtuābitis* 28:12, *dēmentiētis* 28:34, *volucriōrem* 28:49, *interfēmineō* 28:56, *tālīque* 28:67, *portentōsās* 29:3, *ūllæ* 29:23.

### Suspected errors in the words

- **27:1 *præcipit***: printed so (read line leaf 255, col. 0, l. 27: *senatu populo præcipit in*). It is a present tense in narrative, where 27:11 has *præcēpit*. It could be a historic present or a misprint for *præcepit*. I left it and marked it as the present.
- **29:18 *absynthium***: Castellio's spelling of *absinthium* (Gaffiot). It is not a misprint, but it may want a spelling rule (y → i).
- No other word looked wrong.

### Names (for the names reader)

- No name in 27–30 is spelled two ways within these chapters.
- The tribe adjectives in 27:12–13 (*Simeonii, Issachariani, Josephei, Aseriani, Zabulonii, Danii, Nephthalenses*), *Garizimo*, *Ebale*, *Hesebonis*, *Ogum*, *Sebojum* and *Pharaoniosque* (29:2) are unmarked or unknown in the proposal. They are for you.

### Doubtful calls for Nathan

1. **Chapter 28 left unquoted.** The BSB (and ESV) run Moses' command of 27:11 on through 28:68, reopening “ at each paragraph. I closed it at 27:26 and left 28 as the discourse's own voice, like 5–26. The brief names the narrator's short speeches in 27 for quoting and the long discourses for leaving unquoted. The alternative is to drop the ” at 27:26 and open “ at every paragraph of chapter 28, closing at 28:68.
2. **29:2b–30:20 left unquoted**, as the brief says. Note that the BSB does quote it, from 29:2 “You have seen … to 30:20 …Jacob.”, so the brief's "where the BSB leaves it unquoted" is not true here. I followed the analogy with 5:1.
3. **29:5–6 set as poetry** because the BSB does so and the brief says to follow it. In the Hebrew this is God's first person (*I am the LORD*), but Castellio makes it Moses' prose (*eum esse Jōvam Deum vestrum*). I would rather set it as prose: removing the two `q1` rows and the `p` on 29:7 does that.
4. **27:15–26 as twelve paragraphs**, each opening “‘. The alternative is one paragraph for 27:14–26 (about 200 words), which needs no reopening marks.
5. **Future perfect kept** where *quoniam*/*quī* clauses might be perfect subjunctive: *relīqueritis* 28:20, *fueritis* 28:45 and 62, *servīveritis* 28:47, *æquāveritis* 28:62. I read them as future perfect, seen from the time of the curses. If 28:62 *quī … æquāveritis* is concessive, it would be *æquāverītis*.

## Reader 8: Deuteronomy 31–34

**Rows:** 99 layout (`r8.layout.tsv`), 105 forms (`r8.forms.tsv`). `check.py 8 31-34 --all` runs with no ERROR. One
`homograph` flag is left, at 32:50 *adscenderis*. My row there is written in the new spelling, *ascenderis* (future
perfect), as the brief says, so it takes effect only once the proposed rule *adscenderis → ascenderis* applies.

### Quotation structure
- **31** (narrative with speeches, all direct unless noted):
  - 31:2–6: Moses to Israel. God's word to him is reported (*mē nōn esse … trājectūrum*), unmarked.
  - 31:7–8: Moses' charge to Joshua.
  - 31:10–13: Moses' command to the priests and elders.
  - 31:14: God to Moses.
  - 31:16–21: God to Moses. It reopens “ at a new paragraph at 31:19. The people's later confession in 31:17 is reported (acc. + inf.), so the BSB's inner ‘…’ is not used.
  - 31:23: Moses' charge to Joshua, reported (*ut … præbēret: ductūrum enim …*), unmarked.
  - 31:26–29: Moses to the Levites.
- **32:1–43, the Song**: unquoted, as the BSB (it is the book's voice, announced by 31:30). God's words inside it are in “…”:
  - 32:20–28, after *ita fātur:*;
  - 32:34–35;
  - 32:37–42, where *inquiet* (parentheses in 1738) is set off with commas, closing and reopening the quotation (decision 65).
  - The enemies' boast (32:27) and the oath *ita semper vīvam* (32:40) get no inner marks: the first is reported, and the BSB marks neither.
- **32:44–52**: Moses' exhortation (32:46–47) and God's words to Moses (32:49–52) in “…”.
- **33**: the Blessing in “…”.
  - 33:2–6 is one quotation, opened at 33:2 with *inquit* between commas.
  - Each tribe's blessing has its own prose frame and its own quotation: Judah 7; Levi 8–11; Benjamin 12; Joseph 13–17; Zebulun and Issachar 18–19; Gad 20–21; Dan 22; Naphtali 23; Asher 24–25.
  - 33:26–29 is a new quotation, as the BSB.
  - Reported, unmarked: 33:9 (*negat sē … scīre*) and 33:27 (*eum jubēbit ēvertere*).
- **34**: God at 34:4, “Et hæc,” inquit, “terra est …”. The oath to the fathers inside it is reported.

### Paragraphs
- **31:1 `p`**: replaces the draft's `\nb`. 30:20 ends with a full stop, and the narrator takes over.
- New paragraphs added at 31:7, 15, 16, 19, 22, at 32:44, and at 34:4, 5 and 7, all at the BSB's breaks.
- BSB breaks left because they fall inside a Latin sentence: 31:10, 31:12, 32:50–51, 34:9.
- BSB breaks left because the speech is short: 31:3, 31:5, 31:28.

### Poetry
- **32:1–43**: `q1` throughout, with no `\b`, as the settled Exod 15 and Num 23–24. Castellio's clauses follow the BSB's lines; where a sentence gives fewer, the verse has fewer lines: 32:14 has four lines for the BSB's six, 32:39 has five, 32:43 has four.
- **33:2–29**:
  - 33:2 starts the poem directly (`q1`).
  - Each tribe's frame (*Hoc autem dē Jūdā inquit:*, *Item super Dāne:* …) is a prose paragraph (`p`) with the poem following inline, as the settled Num 24:20–23.
  - **33:26 is `b q1`**, the BSB's break. Without it, Asher's closing ” and the new “ would run together. It is the only `\b` in these chapters.
- **Prose resumes** at 32:44 (`p`) and 34:1 (the draft's `\p`).

### Capitals
- **Raised** (adjectives of peoples and places): *Sodomitanis*, *Gomorranis* (32:32); *Moabiticis* (34:1); *Nephthalensem*, *Ephraiminam*, *Manassensem* (34:2); *Moabitica* (34:6); *Moabitico* (34:8).
- **Lowered**:
  - *diē* in 32:48: 1738 prints *Eodem Die*.
  - *būtȳrō* in 32:14 and *nūminis* in 32:18: both continue the sentence of the verse before.
- **Left as they are**:
  - *Suprēmum* (32:8) stays capital: it is a title of God (decision 20).
  - *nūmen* stays lower case, as the settled Num 25:13. Castellio uses it for the Hebrew 'Rock' at 32:4, 15, 18, 30, 31, so there is no *Rūpēs* or *Excelsus* to capitalize.
  - *habitātōris rubī* (33:16) stays lower case: it is a description, not a title.

### Forms: the main corrections to the proposal
- **Ablatives the proposal had wrong:**
  - 32:10 *in dēsertā, inaccessā, fērālī vāstāque terrā* (Hebrew 'in a desert land');
  - 32:13 *dē rigidā caute*;
  - 32:22 *īrācundiā meā*;
  - 32:40 *ēlātā … manū*;
  - 31:15 *columnā*;
  - 31:13 *terrā*, *grātiā*;
  - 32:47 *in eā*, *terrā*;
  - 33:3 *manū tuā*;
  - 33:16 *cōpiā*;
  - 34:5 and 34:6 *terrā*;
  - 34:9 *plēnā … sapientiā*;
  - 34:12 *tantā illā*.
- **Other cases:**
  - 32:21 *per sua illa inānia*: accusative, not *suā*.
  - 33:23 *merīdiāna* and 33:25 *ferrea … claustra*: neuter plurals, not *-ā*.
  - 32:35 *diēs interitūs*: genitive.
  - 31:20 *victūsque*: genitive.
- **Wrong words or quantities:**
  - 31:7 *vādēs*, 'you will go', not *vadēs*.
  - 31:21 and 31:27 *nōvī*, 'I know'.
  - 31:27 *fuerītis* and 31:29 *offenderītis*: perfect subjunctives.
  - 31:29 *irrītandō*.
  - 32:6 *stulte*: the vocative adjective, not the adverb *stultē*.
  - 33:20 *Īdem*: the proposal's *Īdēm* is a slip.
  - 33:25 *æreaque*, as the settled *ærea*; not *āereaque*.
  - 33:11 *Prosperā*, *favē*, *ēlumbā*: imperatives.
  - 33:17 *monocerōtiīs*, as the settled Num 23:22.
  - 33:29 *cōnservāte*, *prōculcābis*.
  - 34:5 *hīc* (adverb); 34:10 *nōtō*.
- **Josua's case** (*Jōsuā*: ablative at 31:3, 31:7, 32:44; *Jōsua*: nominative at 31:15). These are case calls like the Numbers readers' (Num 26:65, 32:12), not spellings. The names reader may want to confirm them.

### Suspected errors in the words
- **32:21 *peruersa***: 1738's u was not converted to v. The coordinator says this is now fixed in the draft, and my row reads *perversa*.
- **32:30 *fieri ne posset***: 1738 prints it as two words (leaf 263, column 0, line 8). The sense is the interrogative enclitic, *fierīne posset* ('could it be that one chased a thousand …?'). That is a word-division question for Nathan, so I left it. As printed, the proposal reads *nē* ('lest'), which the sense rejects.
- **Verse boundaries** where 1738 is a clause off the KJV (31:15, 32:21, 32:33, 33:3) were kept by stage 2. Rows here follow that.

### Names seen spelled two ways (for the names reader)
- **Dan**: *Dāne* / *Dan* (33:22) and *Danem* (34:1). Different cases, but check the stems.
- **Naphtali**: *Nephthali* (33:23 frame, unknown) / *Nephthālis* (33:23 poem, settled).
- **Asher**: *Asere* (33:24, unknown) / *Āsēr* (33:24).
- **Zebulun**: *Zabulōne* (Gaffiot flag) / *Zabulōn* (33:18).
- **Gad**: *Gadō* / *Gadum* (33:20).
- **Jacob's people**: *Jacobei* (32:9, unknown, no macrons) / *Jācōbēōrum*, *Jācōbēōs* (33:4, 33:10).
- **Sinai**: *Sīnā* (33:2) / *Sinis* (32:51, Zin: a different place, the Hebrew צִן).
- **Pisgah**: *Phasge* (34:1, unknown).
- **Beth-peor**: *Bethphegor* (34:6, unknown).
- **Og**: *Ogo* (31:4, unknown).
- **Pharaoh's people**: *Pharaoniosque* (34:11, unknown), against the settled *Pharaōniōs*.

### Doubtful calls for Nathan (my choice given)
1. **Where God's speech in the Song ends**: I closed it at 32:28, not at 32:27 as the BSB. *quippe nātiō rationis expers* finishes God's sentence of 32:26–27, and 32:29–31 speak of *Jōva* in the third person and of *nūminī nostrō*.
2. **The `b q1` at 33:26**: the only stanza break in the OT so far. It is there to keep two quotations apart. The alternative is to run Asher's quotation on through 33:29.
3. **Paragraphs inside short speeches** (31:3, 31:28): BSB breaks left. **31:19**: added inside God's speech, at the BSB's break.
4. **32:7 *narrābunt:***: a colon in place of the full stop, since 32:8 is what the fathers tell, in reported speech.
5. **33:11 *ēlumbā***: no source knows Castellio's verb. I marked it after *ēlumbis* (ē long, Gaffiot and W).

## Proofreader 1: Deuteronomy 1–8

**Read**: all 265 verses of 1–8 whole, as `check.py` proposes them (readers 1–3, the names reader), beside the KJV
and the BSB (layout). `check.py 1 1-8 --all`: 265 verses, no ERROR.

**Rows**: 9 layout (`p1.layout.tsv`), 29 forms (`p1.forms.tsv`).

### Layout rows (9)

- **4 rows only respelled** (3:8 *Cisjordaninam*, 3:25 *Transjordaninam*, 4:9 *advertite*, 4:49 *Cisjordaninum*):
  the readers' rows exactly as `merge.py` already respelled them in `Deut.layout.tsv`. `check.py` reads the r* files
  unrespelled and stopped with an ERROR at 3:8 (the draft now has the j and v); these rows let it run. They change
  nothing in the merged file.
- **Vocative set off by commas** (one call through the book, as 9:1 and 10:12 and the settled Acts 2:22): 4:1 *Et nunc,
  Isrāēlītæ, audīte*; 5:1 *ad hunc modum: Audīte, Isrāēlītæ, īnstitūta* (reader 2's row kept otherwise); 6:3 *Audīte
  igitur, Isrāēlītæ, et cūrāte*; 6:4 *Audīte, Isrāēlītæ: Jōva …* (reader 2's \p and colon kept).
- **Punctuation**: 1:23 *placuisset; dēlēgī* → *placuisset, dēlēgī* (1738's semicolon between the *cum* clause and
  its main verb; as the proofread Lev 20:20). 3:1 *convertissēmus: ēgressus* left (a colon there has precedent, Num 12:10).

Quotation structure checked and kept: Moses' discourse unquoted throughout (1:6–4:40, 5:1b–8:20); direct speech
quoted at 1:38–40, 2:18–19, 2:24–25 (God), 5:6–21 (the Decalogue), 5:24–27 (the people), 5:28–31 (God); every one
balanced and closed; *inquit* with commas (1:38, 2:18). Reported speech unmarked everywhere else. The seams 3/4 and
6/7 are clean (3:29 and 6:25 end with a full stop, 4:1 and 7:1 open paragraphs). No paragraph in 1–8 is over 250
words (largest 5:6–21, 240). No poetry in 1–8.

### Forms rows (29), by kind of error

- **Ablative *Jōvā* left as *Jōva*** (6; readers 2 and 3's ranges): 4:23, 5:15, 6:21, 8:5 *ā Jōvā*; 6:25 *cōram
  Jōvā*; 7:4#1 *ā Jōvā* (the second *Jōva*, *īrātus Jōva*, nominative).
- **The preposition *cis*** (4): 1:1, 1:5 (*Cis*), 4:41, 4:45: short i (Gaffiot cĭs; W and M *cis*); the proposal had
  *cīs* from the settled count (names reader's hard call 8). These four are all of Deuteronomy's.
- **A stem** (1): 6:11 *quās nōn excīdistis* (*excīdō*, hew out, with *excīsās cisternās*), not *excidistis* (fall).
- **Still `unknown`, decided** (16): names by the names reader's table: *Seirem* 1:2, 2:1, 2:5 (unmarked, see call 3);
  *Amorræum* 1:19, 1:20, 2:24; *Salcham* 3:10; *Rabbathæ* 3:11; *Phasga* 3:17, 4:49; *Beser* 4:43; and *Aviōs* 2:23
  (a homograph with *āviōs*; the table keeps it). Others: *agrumve*, *ancillamve* 5:21 (no long vowel); *pessumdederit*
  7:1 (future perfect, Gaffiot pessumdō); *rependentem* 7:10 (Gaffiot rĕpendō, not *rēpō*). Left `unknown`: only rule
  words (1:25 *sumserunt*, 1:43 *contemtisque*).
- **Homographs confirmed as proposed** (no rows): *maritima* 1:7, *vāstam* 1:19, 8:15, *Jōsua*, *hic* 1:38, *apēs* 1:44,
  *emerētis* 2:6, *favēre* 2:7, *lacessitō* 2:19, *Ea … terra* 2:20, *illa* 3:5, *tōtaque*, *rēgnantis* 3:10, *terra*
  3:13, the neuter plurals *jūra, ea, obeunda, discenda, exsequenda, adōranda, colenda, tenenda, illāta, pacta, mōnstra,
  olīvēta, īnstitūtaque, eaque* (4–7), *ītis* 4:5, *tanta* 4:7, 4:8, 4:32, 7:18, *tōta* 4:8, *idem* 4:20, 4:49,
  *pecūliāris* 4:20, 7:6, *ipsa* 4:38, *revocāte* 4:39, *ancilla* 5:14, *expetitō* 5:21, *servāveritis* 7:12 and
  *fueritis* 8:10 (future perfects).

Every other word of 1–8 was read for its quantity in context; no other slip found (the reader rows for *-ā*
ablatives, *-erīmus/-erītis*, *sōlis*, *domūs*, *frūctūs*, *-tō* imperatives all hold).

### Suspected errors in the words

None new. Reader 1's 3:25 *suō veniam* (for *suam*) stands as a question for another printing.

### Calls for Nathan (my choice first)

1. ***cis*, short**, here (4 places), against the settled Numbers' *cīs* (6: Num 21:13, 22:1, 32:19, 32:32, 34:15,
   35:14), which want a review item of their own; the macronizer will keep proposing *cīs* from those counts until then.
2. **Vocative commas**: *Audīte, Isrāēlītæ:* (6:4) as the brief's call; the settled Mark 12:29 has *Audī Isrāēlīta:*
   without one (a slip by this rule, not changed).
3. ***Seirem* unmarked**: the proofreading brief says "as the settled *Seīr-*", but the settled text has *Seir* (3),
   *Seire* (2), *Seirīs* (2), stem unmarked, and the names reader's *Seiris* rows leave it unmarked; I followed the
   settled form. If the Greek Σηείρ / Hebrew שֵׂעִיר (hireq-yod) should mark it *Seīr-*, it is the names reader's row
   for the whole book (*Seīrem*, *Seīre*, *Seīris*).
4. **1:23 the semicolon a comma** (modern punctuation); leaving Castellio's is the alternative.

## Proofreader 2: Deuteronomy 9–17

All 226 verses of chapters 9–17 read whole in the preview (as `check.py 2 9-17 --all` gives them, with every reader's,
the names reader's and the proofreaders' rows), beside the KJV, with the BSB for layout and the Hebrew where a case
was in doubt. Every flagged word checked in context (`data/review/deut1-34-ch09…17.md`), and the unflagged ones read
too: each word ending in *-a/-ā*, each *-eritis/-erītis*, each imperative in *-tō/-tōte*, each *Jōva* after *ā*,
*ūnā cum* and in an ablative absolute. The check runs with no ERROR (it did not before: see 1 below).

### Rows written

- `p2.layout.tsv`: **1** row.
  - **10:6**: reader 3's row with *Jaacanensium*, the spelling the merge has now applied to the draft (names hard call 4).
    Unchanged otherwise. The check does not respell layout rows the way `merge.py` does, so it stopped with an ERROR
    on reader 3's *Jaquanensium*. The merged `Deut.layout.tsv` already has the new spelling, so this row only makes
    the check agree with it.
- `p2.forms.tsv`: **9** rows.
  - *Jōva* left short after *ā* (2): **9:4** *ā Jōvā* (`#2`, the first copy is the subject), **9:6** *ā Jōvā Deō vestrō*.
  - *nōlitōte* → *nōlītōte* (3): **9:4**, **13:3**, **14:1**. This follows the readers' 20:1 and 20:19 rows and 15:7 *nōlītō*.
  - Ablative *-ā* where the nominative is meant (1): **10:14** *terraque*, a subject of *sint* with *cælī*.
  - *manūs* → *manus* (1): **17:7**. *testium quidem manus … prior estō* is singular, as 13:9 *tua manus prīma sit*.
  - Rule words flagged `unknown`, written in the new spelling (2): **9:9** *sūmpsissem*, **15:15** *redēmptum*. They
    take effect once the rules apply. (14:26 *īnsūmptā* and 13:12 *audieritis* already have readers' rows.)

### Errors found, by kind

| Kind | Count |
|---|---|
| *Jōva* for *Jōvā* after *ā* | 2 |
| *nōlitōte* for *nōlītōte* | 3 |
| *-ā* for the nominative *-a* (*terrāque*) | 1 |
| *manūs* for the singular *manus* | 1 |
| Layout row out of step with the respelled draft (check ERROR) | 1 |
| `unknown` rule words given a form | 2 |

No other macron error found. These were checked and are right as proposed:
- every *ūnā cum*: 11:6, 12:7, 12:12, 12:18, 13:16, 14:26, 15:20, 16:11, 16:14;
- every *ā Jōvā* other than the two above;
- the perfect subjunctives 9:7 *offenderītis*, 10:19 *fuerītis*, 12:4 *nē fēcerītis*, against the future perfects
  (*-eritis*) in conditions and *cum* clauses;
- 12:8 *hīc*, 10:21 *Hic* (the pronoun, KJV "He is thy praise");
- 16:6 *sōlis*, 17:3 *sōlem*, 17:6 *ōre*;
- every *-tō/-tōte* imperative.

The `homograph` flags still standing are all right as proposed, each confirmed in context: 9:2 *solēre*,
9:7 *repetite*, 9:14 *ea* (nom.), 9:15 *flagrābat*, 9:21 *commolitō* (*commolō*, ground), 9:26 *corrumpere*,
10:4 *eaque*, 10:10 *morātus*, *ēvertere*, 10:21 *vestra*, *magna*, *illa*, *stupenda*, 11:1, 11:32, 12:1 *jūra*,
11:4 *profūsīs*, 11:6 *terra*, *aperta*, 11:10 *terra*, 11:11 *pōtat*, 11:18 *mea*, *eaque*, 11:24 *Euphrāte*,
12:6 and 12:11 *sēcrēveritis*, *honōrāria*, *lēcta*, *vōveritis*, 12:8 *libet*, 12:10, 12:29 and 17:14 *cōnsēderitis*,
12:18, 12:26, 15:9, 15:20 and 16:22 *ea*, 12:22 and 15:22 *caprea*, 12:23 and 13:6 *anima*, 12:25 *fueritis*,
13:6, 13:9 and 14:29 *tua*, 13:9 *prīma*, 13:10 *abdūcere*, *cōnātus*, 13:14 *dēprehenderitis*, 13:15 *oppidāna*,
*ipsaque*, 14:1 *vestra*, 14:2 *pecūliāris*, 14:7 *lepore*, 14:10 *eaque*, 14:18 *pīcō* (the woodpecker),
14:20 *volucrī*, 14:28 *tribus* (*trēs*), 15:7 *contractior*, 15:11 *dēerunt*, 15:17 *idemque* (neuter),
15:18 *conductus*, 16:4 *immolāveritis*, 16:9 *immīseris*, 16:13 *percēperis*, 17:4 *compereritis*,
17:14 *occupāveritis*, *statueritis*.

**Layout.** Quotation marks balance in 9–17 (6 “ and 6 ”). The structure was checked:
- God's words are quoted at 9:12–14, with *inquit* in commas at 9:13, and at 11:14–15, with *“Ego,” inquit, “…”*.
- Moses' prayer is quoted at 9:26–29. Within it, 9:28 is reported (*Jōvam … ēdūxisse*) and left unmarked.
- The saying at 9:2 is quoted.
- Castellio's reported forms stay unmarked: 9:23, 10:1–2, 10:11, 12:20, 12:30, 13:2, 13:6, 13:13, 15:9, 15:16,
  17:14, 17:16.

The vocatives take commas (9:1 *Audīte, Isrāēlītæ:*, 10:12 *Nunc, Isrāēlītæ, quid*), and *inquam* is set off by
commas (9:11, 12:25, 15:6). Capitals are right: *Domine Jōva* (9:26), *deōrum Deus … dominōrum Dominus* (10:17),
*Ægyptium, Ægyptiæ, Lēvīticam*, and lower case *mare rubrum*, as the settled text has it. No paragraph runs over
about 180 words, and the seams at 10/11 and 14/15 are clean.

### Suspected word errors (not changed)

- **11:10 *conferebatis***: *quam et seminibus vestris conferebatis, et pedibus vestris … irrigabatis*. Read thus on
  the page (read-1738, leaf 240 col. 1 line 98). The sense wants *conserebatis* (*cōnserō*, to sow: "which you sowed
  with your seeds", KJV "where thou sowedst thy seed"), and 16:21 has Castellio's *cōnseritō*. This could be ſ read
  as f, or a misprint in 1738. Worth a look at the page image, or at another printing if one has Deuteronomy.
- 9:15 *Tum ego revertī, et … dēscendere*: read thus (leaf 238 col. 1 line 102). Historical infinitives (*revertī*,
  *dēscendere*) make sense, so this is probably not an error, only unusual.

### Calls for Nathan (or the merge)

1. **14:16–17 *ībī***: reader 4's row (the ibis, ablative; settled Lev 11:18 *ībim*) has no effect. The preview shows
   *ībi*, because `macronize.finish` shortens the final *-i* of every word spelled *ibi* (the brief's rule for the
   adverb), and it does this after a decided form too. Fixing it needs code: exempt decided forms from
   `SHORT_FINAL`. A row cannot do it. My choice is *ībī*.
2. **10:6 layout row**: the check script does not respell rows the way `merge.py` does. Any reader's layout row in a
   verse that the names reader respelled will make `check.py` stop with an ERROR, as 10:6 did. Other proofreaders may
   meet the same thing.
3. ***nōlītōte***: the settled text has *nōlitōte* 3 times and *nōlītōte* twice. Deuteronomy now has *nōlītōte*
   throughout. The settled three should follow in a review item.
4. **9:8 *pēne***: reader 3's row is in the old spelling. Once the rule *pene* → *paene* applies, it will no longer
   match the word. *pæne* needs no row (no long vowel).

## Proofreader 3: Deuteronomy 18–27

I read all 227 verses of 18–27 in full as `check.py` proposes them, beside the KJV and the BSB (its marks and layout).
I checked every word's marking in context and every plain `homograph` and `unknown` flag. `check.py 3 18-27 --all`
runs with no ERROR. Four verses change as a result (25:7, 25:11, 27:2, 27:3).

### Rows written

- **Layout (1 row, `p3.layout.tsv`)**: 25:11 `p`. The fight law (25:11–12) is a separate law from the levirate
  law (25:5–10). The BSB (b m), WEB and KJV (¶) all break here, and the Latin sentence starts here.
- **Forms (6 rows, `p3.forms.tsv`)**:
  - *Jōvā* after *ā*: 27:2 and 27:3#1. In 27:3 only the first copy changes; the second, *Jōva Deus vester patrius*,
    is nominative.
  - Words still `unknown`: 22:4 *bovemve*, 24:6 *pignorantor*, 25:7 *glōssem*.
  - 26:19 *decoris*: a homograph nothing chose. It is the genitive of *decus* (honour), not *decōris*, and the
    row confirms the proposal.

### Errors found, by kind

- **Ablative *Jōvā* left as *Jōva* after *ā***: 2 (27:2, 27:3). Reader 7's range; their notes list *Jōvā* only at 30:16.
  Every other *ā/ab/cōram Jōvā* and every ablative absolute in 18–27 is right.
- **`unknown` words decided**: 3 (*bovemve*, *pignorantor*, *glōssem*).
- **Paragraph**: 1 (25:11).
- **None found** in these kinds: ablatives in *-ā*, neuter plurals in *-a*, *-erīs/-eris*, *hīc/hic*, *sōlis*,
  *ōs*, *domūs*, *frūctūs*, *nōlītōte*, *-tō* imperatives, quotation marks, God's capitals, the vocative commas
  (20:3 *Audīte, Isrāēlītæ:*, 21:8 *…, Jōva, nōlī*, 27:9 *audī, Isrāēlīta.*).

### Homographs confirmed in context (no row needed)

- **18–20**: 18:1 *ūniversa tribus* (nom.), 18:4 *velleris* (gen. of *vellus*), 18:6 *Lēvīta*, 18:12, 19:9, 25:16 *ista*
  (acc. pl.), 18:14 *venītis* (present), 18:18 *mea verba*, 19:3 *concessa possessiō*, 19:17 *contrōversia*, 20:18 *nefanda*,
  20:3 *remollēscere*, 20:19 *corrumpere*.
- **Future perfect *-eris/-eritis*** (main clause future or imperative): 19:1 *exēgeritis, cōnsēderitis*, 20:1 *vīderitis*,
  20:20 *subēgeritis*, 21:10 *abēgeritis*, 21:11 *animadverteris*, 21:22 *adfēceritis, ēgeritis*, 22:6 *incideris*,
  23:21 *nuncupāveris, commīseris*, 23:23 *prōnūntiāveris*, 23:25 *introjeris*, 24:19 *omīseris*, 26:1
  *occupāveritis, cōnsēderitis*, 26:2 *percēperis*, 27:12 *trājēceritis*.
- **21–24**: 21:4 *adhibita* (nom.), *vāstam*, 21:5 *concelebrent*, 21:12 *ipsa*, 21:16 *bona sua*, 22:4 *adlevātō*, 22:6 *avis*
  (gen.), 22:8 *dēciderit*, 22:23 *pactam*, 23:2–3 *decima* (nom.), 23:9 *malam* (evil), 23:12 *requīsīta*, 23:14 *vestra, pūra*,
  23:20 and 24:19 *tua* (acc. pl.), 24:1, 24:3, 24:13, 27:22–23 *suā* (abl.), 24:4 and 25:6 *illa* (nom.), 24:5 *immūnis*, 24:7
  *compertus*, 24:13 *eaque rēs*, 24:14 *populāris*.
- **25–27**: 25:3 *ferītō*, 25:10 *domus* (nom.), 25:13 and 25:15 *pondera*, 25:18 *lassīs*, 26:14 *præcepta tua, ea*,
  26:16–17 *jūra*, 26:17 *prōnūntiātis*, 26:19 *laudis*, 27:4 *eaque* (acc. pl., *saxa*), 27:10 *dēcrētaque*, 27:15–26
  *Exsecrābilis* (nom.).

### Layout across the seams 20/21 and 26/27

The quotation marks are balanced.
- **Chapter 20**: 20:3–4, 20:5–7 and 20:8 open and close within the chapter. 21:1 is a new law, unquoted.
- **26/27**: 26:19 ends Moses' unquoted discourse.
- **Chapter 27**:
  - 27:1–8 and 27:9–10 are quoted after the narrator's frames.
  - 27:12–26 is one speech that reopens “ at each curse's paragraph and closes at 26 with ’”. Inside it, the
    Levites' curses and the *Āmēn* are in ‘…’.
- **Paragraphs**: none in 18–27 runs over 250 words. The longest is 19:1–10, at 219 words.

### Suspected word errors (stage 2; not changed)

- **23:25 *introjeris***: 1738 prints *introieris*, where the i is a vowel (Reader 6's note, leaf 252 col. 1
  ll. 73–74). The draft's *j* is a conversion slip. A spelling row would fix it.
- **25:7 *glossem***: printed so (leaf 253, col. 1, l. 89). It is Castellio's own accusative of *glōs*, not a
  misprint. It is kept and marked *glōssem*.
- No others. *Quum quidem* (18:17), *reperit* (22:27), *præcipit* (27:1) and *Quadrāgēsiēs* (25:3) read as
  Castellio's own, as the readers noted.

### Names

No person is marked two ways in 18–27. *Isrāēlītidum* (23:17) is now right; Reader 6 had flagged it as
*Isrælitidum*.

### Calls for Nathan (my choice given)

1. **25:7 *glōssem***: I marked the ō long from *glōs*, reading the ss as the doubled s after a long vowel (as in
   *caussa*). If Castellio declined the word like *os, ossis*, it would be *glossem*, unmarked.
2. **25:11 paragraph added.** Other small laws in 22:5–12 and 23:15–25 also have BSB/KJV breaks but stay grouped,
   as the readers grouped them. Those paragraphs are under 170 words.
3. **26:19 *decoris*** is read as *decus*, -oris (honour), rather than *decor*, -ōris (beauty).

## Proofreader 4: Deuteronomy 28–34

I read all 240 verses of 28:1–34:12 in full, beside the KJV, and used the BSB's markers for layout. I checked every word, flagged or not, against the settled forms in `data/gold/`. I also scanned the range for words the settled text marks only one way, for words it lacks, for every unmarked *-a*, every *Jōva* and every æ/œ. `check.py 4 28-34 --all` runs with no ERROR (240 verses).

**Rows**: 4 layout rows in `p4.layout.tsv` and 15 forms rows in `p4.forms.tsv`.

### Errors found, by kind

- **Ablative *Jōvā* left as *Jōva*** (6 forms rows): 28:52 and 28:53 *ā Jōvā Deō vestrō*, 29:15 *cōram Jōvā*, 29:18 *ā Jōvā Deō nostrō*, 30:1 *ā Jōvā Deō vestrō*, 34:11 *ā Jōvā*. The settled text has *ā Jōvā* 59 times against *ā Jōva* once, and *cōram Jōvā* 19 times. Every other *Jōva* in the range is a nominative or a vocative (33:7, 33:11).
- **Perfect subjunctive, not future perfect** (2): 28:20 *quī eum relīquerītis* is a causal relative inside *eōusque ut … ēvertat*. 28:62 *quī cælī stēllās … æquāverītis* is a concessive relative with a past sense (KJV *whereas ye were*) inside *ita ut … superētis*. Reader 7 had both as doubtful calls.
- **Wrong word** (1): 28:26 *ālitibus āereīs*, the birds of the air. It comes from *āēr* (Gaffiot āĕreus), as the settled *āeriæ, āeriīs* for the birds of the air. The proposal had *æreīs* 'of bronze', taken from the settled Exodus bases. 28:23 *æreō* and 33:25 *æreaque* are bronze and correct.
- **Hidden quantity against the settled text** (2): 28:37 *dictēriīs*: Gaffiot dictērĭum, and the settled text writes *dictum, dicta* unmarked. 31:20 *vīctūsque*: the settled text has *vīctū* 10 times and *vīctuī* 6. Reader 8's note said *vīctus*, but the row had *victūsque*.
- **Hiatus written as œ** (1): 33:5 *coeuntibus* (Gaffiot cŏĕō), as the settled *coeuntque, coeunte* and Lev 18:23 *coeundum*.
- **Unknown words decided** (3): 28:14 *sinistramve*, 32:6 *Hæccine* (no long vowel in either), and 32:30 *fierīne* (*fierī* + *-ne*, joined from 1738's *fieri ne*).
- **Vocatives without commas** (3 layout rows), now set off as the book's other vocatives (9:1, 20:3, 32:43, 33:11): 32:1 *Attendite, cælī, … audī, terra, verba*; 33:7 *Exaudī, Jōva, vōcem Jūdæ*; 33:18 *Lætāre, Zabulōn, … et, Issāchar, in tabernāculīs tuīs*.
- **A reader's row behind the draft** (1 layout row): reader 8's 34:1 still read *Phasge*. The draft now has the names reader's *Phasgae*, so `check.py` stopped with an ERROR. My row is reader 8's row with the draft's word, otherwise unchanged. The merge would have respelled it anyway.

### Confirmed as they stand

- **Homographs left as proposed**: I confirmed each one in context. They are the future perfects in *sī*, *quem* and *quoniam* clauses (28:1, 25, 36, 45, 47, 62 *fueritis*, 30:4), and the nominative and accusative neuter plurals (*vestra, dīra, nefanda, aurea, aperta, nostra, exsequenda, dēscrīpta, jūra, altissima, mūnītissimaque*). The rest are *solī* (soil), *fētūra*, *tābe*, *olea*, *incognita*, *pluvia*, *familia*, *tribus* (singular, 29:18), *āversa*, *doctrīna*, *posita*, *vīta* (30:20), *mollis*, *dēlicāta*, *fīgere*, *ea*, *ītis*, *amandō*, *dedimus*, *cūrētis*, *colētisque* and *modō* (29:2 *hoc modō*, ablative).
- **Readers' case calls**: the 12 forms that differ from the settled text's single form are all correct in context: *dōnātā, arēna, aquilā, complexūs* (twice), *Tantāque, trānsīverīmus, ruīna, prōposita, stulte, merīdiāna, ferrea*.
- **Quotation marks**: balanced through 31–34, and every speech is opened and closed. The 30/31 seam is right: 30:20 ends Moses' unquoted discourse, 31:1 has the narrator, and the quotation opens at 31:2.
- **Paragraphs**: none over about 220 words (29:16–24).
- **29:5–6 are prose**. The merge drops reader 7's `q1` rows (`merge.py` DROP), so 29:2–6 is one paragraph and 29:7 keeps its `p`. I wrote no rows for this. `check.py` does not apply the DROP, so it still prints 29:5–6 as poetry.
- **Names**: each person is marked one way: *Jōsua/-æ/-am/-ā*, *Nūnis*, *Mōsēs/-em/-ī/-is*, *Āsēr/-e*, *Nephthālis/-ī*, *Dan/Dane/Danem*, *Gadō/Gadum*, *Zabulōn/-e*, *Ōgum/Ōgō*, *Bāsānæ/-ā*, *Mōabīt-*.

### Suspected errors in the words

None new. 32:30 *fierine* is already joined in the draft.

### Calls for Nathan (my choice given)

1. **28:20 *relīquerītis*, 28:62 *æquāverītis***: I made both perfect subjunctive, overriding reader 7's future perfect. Drop the two rows to keep *-eritis*.
2. **Mood attraction left alone**: 28:25 *in quem viā ūnā exieritis* and 30:4 *sī … fueritis dissipātī* sit inside *ut* clauses, and strict grammar would make them subjunctive (*-erītis*). I kept the future perfect: the indicative reading is natural there, and nothing else in the verse requires the subjunctive.
3. **31:10 *sōlemnitāte***: kept as the settled *sōlemnitāt-* (14 copies). Gaffiot has *sollemnĭtās* and Wiktionary *sollemnitās*, both with a short o, so the settled ō may be a slip. A review of its own is needed; nothing was changed here.
4. **32:40 *sīc loquor: ita semper vīvam …***: no inner marks, which agrees with reader 8 and the BSB. It is God's own oath, spoken in the present, not a quotation.
5. **32:39 *neque quemquam Deum esse præter mē***: the capital is kept, as the settled 1 Cor 8:4 *nūllumque alium esse Deum*.

