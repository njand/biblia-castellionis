# Matthew 14–28, stage 3: spelling

Proposed 2026-11-07 (overnight run). The text is the draft **after stage 2** (`matt14-28-stage2.md` applied in full, verse numbers the KJV's); the **Apply** lines compose in that order and were checked to match once on that text (`python -m pipeline review check` on a working copy). Groups 1–3 are the approved rules (`data/rules/orthography.tsv`, `pipeline/normalize.py`), proposed word by word; under decision 6 every one is still reviewed during the pilot. Groups 4–6 are judgments, read verse by verse; the last table lists what was left as it is.

The draft was already spelt to your settled conventions almost everywhere: the stage-2 collation found 45 places where the printings spell otherwise, and all but the ones in groups 5–6 match your settled chapters or a decision (table at the end).

## 1. æ and œ for diphthongs (decision 16) (12)

Your draft writes *oe* in these words, as Wikisource; your settled text and Gaffiot have *œ* (*cœpit*, *pœna*, *fœdus*, *fœditās*).

**Decision:** accept (Nathan, 2026-11-07)

1. **Apply:** `Matt.16.21` la: `coepit` → `cœpit`
2. **Apply:** `Matt.16.22` la: `coepit` → `cœpit`
3. **Apply:** `Matt.18.24` la: `coepisset` → `cœpisset`
4. **Apply:** `Matt.23.14` la: `poenās` → `pœnās`
5. **Apply:** `Matt.23.27` la: `foeditāte` → `fœditāte`
6. **Apply:** `Matt.23.36` la: `poenās` → `pœnās`
7. **Apply:** `Matt.24.49` la: `coeperit` → `cœperit`
8. **Apply:** `Matt.25.46` la: `poenam` → `pœnam`
9. **Apply:** `Matt.26.22` la: `coepērunt` → `cœpērunt`
10. **Apply:** `Matt.26.28` la: `foederis` → `fœderis`
11. **Apply:** `Matt.26.37` la: `coepit` → `cœpit`
12. **Apply:** `Matt.26.74` la: `coepit` → `cœpit`

## 2. Spelling rules (approved; decisions 19 and 22) (9)

Word rules from `orthography.tsv`: the *-īv-* perfects form by form (decision 19) and *Hierichūs, -ūntis* (decision 22). Macrons are taken from your settled chapters' form of the new word where it occurs there.

**Decision:** accept (Nathan, 2026-11-07)

1. **Apply:** `Matt.18.15` la: `audīverit` → `audierit` (decision 19 (-īv- perfects, form by form): 9× in our texts)
2. **Apply:** `Matt.18.16` la: `audīverit` → `audierit` (decision 19 (-īv- perfects, form by form): 9× in our texts)
3. **Apply:** `Matt.20.29` la: `Hiericunte` → `Hierichunte` (with hiericuntem (Wikisource's Gospels: Matt 20:29, Mark 10:46))
4. **Apply:** `Matt.20.30` la: `audīvērunt` → `audiērunt` (decision 19 (-īv- perfects, form by form): 18× in our texts)
5. **Apply:** `Matt.25.36` la: `vestīvistis` → `vestīstis` (decision 19 (-īv- perfects, form by form): 2× in our texts)
6. **Apply:** `Matt.26.65` la: `audīvistis` → `audīstis` (decision 19 (-īv- perfects, form by form): 33× in our texts)
7. **Apply:** `Matt.27.21` la: `quæsīvisset` → `quæsīsset` (decision 19 (-īv- perfects, form by form): 3× in our texts)
8. **Apply:** `Matt.27.52` la: `obdormīverant` → `obdormierant` (decision 19 (-īv- perfects, form by form): 2× in our texts)
9. **Apply:** `Matt.27.58` la: `petiit` → `petīvit` (decision 19 (-īv- perfects, form by form): 22× in our texts)

## 3. Word division (approved phrase rules) (1)

**Decision:** accept (Nathan, 2026-11-07)

1. **Apply:** `Matt.15.4` la: `maledīxerit` → `male dīxerit`

## 4. Capitals for God (decision 20) (17)

*Pater*, *Fīlius*, *Spīritus* capitalized where they refer to God or Christ (NRSV style), as in your settled chapters (*Pater vester cælestis*, *ā Patre*); a human father or son stays lower case (15:4–6, 19:19, 21:31, 21:37). Read verse by verse. *Fīlius Hominis* and *Deī Fīlius* are already capitalized throughout the draft; *in suprēmīs* (21:9, “in the highest”) stays lower case.

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 15:13** *meus pater cælestis* → *Pater*: “my heavenly Father”.
   **Apply:** `Matt.15.13` la: `meus pater cælestis` → `meus Pater cælestis`
2. **Matt 16:17** *pater meus quī in cælīs est* → *Pater*.
   **Apply:** `Matt.16.17` la: `sed pater meus` → `sed Pater meus`
3. **Matt 16:27** *in suī patris glōriā* → *Patris* (“in the glory of his Father”).
   **Apply:** `Matt.16.27` la: `suī patris` → `suī Patris`
4. **Matt 17:5** the voice from the cloud: *meus cārissimus fīlius* → *Fīlius*, as your Matt 3:17, Mark 1:11, Luke 3:22.
   **Apply:** `Matt.17.5` la: `cārissimus fīlius` → `cārissimus Fīlius`
5. **Matt 18:10** *faciem patris meī, quī in cælīs est* → *Patris*.
   **Apply:** `Matt.18.10` la: `faciem patris meī` → `faciem Patris meī`
6. **Matt 18:14** *voluntās … vestrī patris, quī est in cælīs* → *Patris*.
   **Apply:** `Matt.18.14` la: `vestrī patris` → `vestrī Patris`
7. **Matt 18:19** *ā patre meō, quī in cælīs est* → *Patre*.
   **Apply:** `Matt.18.19` la: `ā patre meō,` → `ā Patre meō,`
8. **Matt 18:35** *meus quoque cælestis pater* → *Pater*.
   **Apply:** `Matt.18.35` la: `cælestis pater` → `cælestis Pater`
9. **Matt 20:23** *parātum est ā patre meō* → *Patre*.
   **Apply:** `Matt.20.23` la: `ā patre meō.”` → `ā Patre meō.”`
10. **Matt 23:9** *ūnus est enim vester pater quī est in cælīs* → *Pater* (the earthly *patrem* before it stays).
   **Apply:** `Matt.23.9` la: `vester pater` → `vester Pater`
11. **Matt 24:36** *sed meus pater sōlus* → *Pater*.
   **Apply:** `Matt.24.36` la: `meus pater sōlus` → `meus Pater sōlus`
12. **Matt 25:34** *Adeste beātī patris meī* → *Patris*.
   **Apply:** `Matt.25.34` la: `beātī patris meī,` → `beātī Patris meī,`
13. **Matt 26:29** *in rēgnō patris meī* → *Patris*.
   **Apply:** `Matt.26.29` la: `rēgnō patris meī.”` → `rēgnō Patris meī.”`
14. **Matt 26:39** the prayer in Gethsemane: *Mī pater* → *Pater*.
   **Apply:** `Matt.26.39` la: `“Mī pater,` → `“Mī Pater,`
15. **Matt 26:42** *Mī pater* → *Pater*.
   **Apply:** `Matt.26.42` la: `“Mī pater,` → `“Mī Pater,`
16. **Matt 26:53** *exōrāre patrem meum* → *Patrem*.
   **Apply:** `Matt.26.53` la: `exōrāre patrem meum` → `exōrāre Patrem meum`
17. **Matt 26:41** *Spīritus quidem prōmptus est, sed carō īnfirma*: the human spirit (NRSV “the spirit indeed is willing”): lower case.
   **Apply:** `Matt.26.41` la: `Spīritus quidem` → `spīritus quidem`

## 5. Consistency within the book (1)

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 27:26** *Barabam* → *Barabbam*, as the draft's other four (27:16, 17, 20, 21) and Wikisource. (1573 and the later printings write *Barrabam*; the names list may want to settle this once.)
   **Apply:** `Matt.27.26` la: `ille Barabam` → `ille Barabbam`

## 6. Your call (2)

**Corpus evidence** (`pipeline latin attest --count`, Latin Library, republican era; Cicero in brackets; 2026-11-07).
Plain *eō* and its compounds both prefer the short perfect forms in republican prose:

| Form | Compounds of *eō* | Plain *eō* |
|---|---|---|
| 1st sing. | *-iī* 27 (23) : *-īvī* 0 (*praeteriī* 12, *rediī* 8, *adiī* 3, *abiī* 2, *periī*, *obiī*) | *īvī* 0; *iī* not countable (= the pronoun) |
| 3rd sing. | *-iit* 93 : *-īvit* 0 (*rediit* 39, *abiit* 19, *adiit* 17, *periit* 12 …) | *iit* 6 (6) : *īvit* 1 |
| 3rd pl. | *-iērunt* 20 : *-īvērunt* 0 | *iērunt* 4 : *īvērunt* 1 |
| 2nd sing. | *-iistī* 0 : *-īstī* 10 (9) (*redīstī, adīstī, transīstī, exīstī*) | *īstī* not countable (= *istī*) |
| 2nd pl. | *-iistis* 0 : *-īstis* 0 (all eras 7 : 15, *existis* left out: also *exsistis*) | *īstis* not countable (= *istis*) |
| infinitive | *-iisse* 0 : *-īsse* 92 (*perīsse* 27, *exīsse* 16, *transīsse* 16, *redīsse* 15 …) | *īsse* 10 : *iisse* 0 : *īvisse* 0 |
| plupf. subj. | *-iissent* 0 : *-īssent* 9 | *īsset* 5 : *īvisset* 0 |

The *-īv-* forms of *eō* are later: all eras, *īvit* 143 and *exīvit* 125, *transīvit* 75, *exīvī* 27, mostly post-classical.

**Corpus evidence for item 2** (republican era, 24 first-conjugation verbs; Cicero in brackets): *-āvistis* 10 (9) :
*-āstis* 14 (12), near even; Cicero uses both, even in one passage (*Philippic* VII 11 *iūdicāvistis … iūdicāstis*).
*vīsitō* has neither form in republican prose (all eras *visitastis* 10, *visitavistis* 0). By the principle of
decision 18/19 (near even → the spelling most consistent with the rest), your settled text, which has only *-āstis*
(*saltāstis, plōrāstis, labōrāstis, intrāstis*), and the base (1573 *visitastis*) decide it.

**Decision:** accept 2 (item 1: keep iī, by the corpus counts) (Nathan, 2026-11-07)

1. **Matt 25:25** *Id veritus, iī obrutum humī tuum talentum*: “I went (and hid)”. 1573 *iui* (canvas 771, page image). Your *iī* is also the pronoun “they” (36× in your settled text), so *īvī* reads more clearly. Decision 19 left *eō* and its compounds out of the *-īv-* rules, and your settled text has *iit* (2×) and *iērunt*: accept for clarity here only, or keep *iī*?
   **Apply:** `Matt.25.25` la: `Id veritus, iī` → `Id veritus, īvī`
2. **Matt 25:36** *cum æger, vīsitāvistis*: 1573, 1758, 1747, 1750 *visitastis* (1573 canvas 771, OCR). Your settled text keeps the printings' contracted *-āv-* forms (*plōrāstis*, Luke 7:32; decision 19 concerns *-īv-* only), so *vīsitāstis* would follow the base. Accept, or keep the full form?
   **Apply:** `Matt.25.36` la: `æger, vīsitāvistis;` → `æger, vīsitāstis;`

## 7. Your spelling kept where the printings differ (15 kinds)

Found by the stage-2 collation: the printings spell these otherwise, but your draft agrees with your settled chapters or with a decision, so nothing is proposed.

| Your draft | Printings | Why kept |
|---|---|---|
| *iit*, *iērunt*, *coiērunt*, *abiit* | *iuit*, *iuerunt*, *coiuerunt* | your settled *iit*, *iērunt*, *adiērunt*, *rediērunt*; decision 19 leaves *eō* out |
| *miseritus* (14:14, 18:27, 18:33) | *misertus* | your settled *miseritus* (4×) |
| *congenūclāns*, *congenūclantēs* | *congenulans* | your settled *congenuclāns* (Mark 1:40; its *u* is short there: the draft's *ū* is a stage-4 question) |
| *mīlia*, *mīlium* | *millia*, *millium* | your settled *mīlia* |
| *intellegō* | *intelligo* | approved rule (*intelligam → intellegam* …) |
| *-cumque*, *quemquam*, *quamquam* | *-cunque*, *quenquam*, *quanquam* | your settled forms |
| *exspectō*, *exsequor*, *exstinguō*, *exstirpō* | *expecto*, *exequor* … | your settled *exsp-*, *exsequ-* |
| *monumentum* | *monimentum* | your settled *monumentīs* |
| *cotīdiē*, *hieme*, *silvīs*, *cārissimus* | *quotidie*, *hyeme*, *sylvis*, *charissimus* | your settled forms; Gaffiot |
| *sē ipsum*, *tē ipsum* | *seipsum*, *teipsum* | two words, as your settled text |
| *æquiperet* (16:26) | *æquiparet* (1573, page image) | decision 18: republican *aequiperare* (Cicero, Livy, Nepos; *aequiparare* only later) |
| *accubitiōnēs* (23:6) | *accubationes* | decision 18: Cicero *accubitio* (2×); *accubatio* only Neo-Latin |
| *fænore* (25:27) | *fœnore* | decision 18: *faenore* republican 12 : *fenore* 1 |
| *decimātis* (23:23) | *decumatis* | Gaffiot heads both; your settled *decumās* (Gen 14:20, the noun) has *u*. Left as drafted; say if you want *decumātis* |
| *dextram* (27:29) | *dexteram* | your settled text has both; left as drafted |
