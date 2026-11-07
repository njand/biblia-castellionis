# Matthew 14–28, stage 4: macrons

Proposed 2026-11-07 (overnight run). Your draft already has macrons, so stage 4 was run as a check: every word
of the text **after stages 2 and 3** (`matt14-28-stage2.md`, then `matt14-28-spelling.md`, applied in full) was
marked again by the pipeline (`pipeline/macrons.py`: the harness's variant C, i.e. W/M candidates with Gaffiot
for stems and hidden quantities, your settled forms where one marking holds ≥ 80% of `data/gold/`, and your 2019
WordPress macrons choosing among a homograph's markings), and compared with your marks. The **Apply** lines
compose after the spelling file and were checked to match once on that text.

**9,051 words compared; 67 differ (0.74%).** 13 are proposed below (groups 1–2, with one more, 27:29, that the
pipeline could not mark) and 4 are your call (group 3). The other 50 are the pipeline's own errors, kept as you
wrote them (group 4). Homographs: of the 5 the
pipeline could not settle (*solveritis*, *vīderitis*, *pāverīmus*, *connūbia*, *lēgis*), your marking was
read in each verse and kept. Your *-eritis* (future perfect: 18:18 *solveritis*, 24:15 *vīderitis*) matches
your settled practice: *-erītis* for the perfect subjunctive (John 4:48, Luke 7:22), *-eritis* for the
future perfect (*intrāveritis*, *fueritis*).

## 1. Against the lexicon and Gaffiot (8)

The lexicon's only form and Gaffiot's headword agree against your mark (`python -m pipeline latin macron`).

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 15:32** *dēfetiscantur* → *dēfetīscantur*: Gaffiot *dēfĕtīscor*; W *dēfetīscantur* (the inchoative's *-īsc-*).
   **Apply:** `Matt.15.32` la: `dēfetiscantur` → `dēfetīscantur`
2. **Matt 15:37** *frūstōrum* → *frustōrum*: Gaffiot *frustum, ī* (short *u*); W *frustōrum*.
   **Apply:** `Matt.15.37` la: `frūstōrum` → `frustōrum`
3. **Matt 17:24** *didrāchma* (twice) → *didrachma*: Gaffiot *didrachma, ătis*; W *didrachma* (Greek δίδραχμον, short α).
   **Apply:** `Matt.17.24` la: `quī didrāchma exigēbant` → `quī didrachma exigēbant`
   **Apply:** `Matt.17.24` la: `vester didrāchma?` → `vester didrachma?`
4. **Matt 17:27** *staterem* → *statērem*: Gaffiot *stătēr, ēris*; W *statērem* (στατήρ).
   **Apply:** `Matt.17.27` la: `staterem` → `statērem`
5. **Matt 26:47** *fustibus* → *fūstibus*: Gaffiot *fūstis, is*; W *fūstibus*.
   **Apply:** `Matt.26.47` la: `fustibus` → `fūstibus`
6. **Matt 26:55** *fustibus* → *fūstibus*: as item 5.
   **Apply:** `Matt.26.55` la: `fustibus` → `fūstibus`
7. **Matt 26:58** *introgressus* → *intrōgressus*: Gaffiot *intrōgressus, a, um*; W *intrōgressus*.
   **Apply:** `Matt.26.58` la: `introgressus` → `intrōgressus`

## 2. Against your settled chapters (7)

Forms your settled chapters write one way (counts from `data/gold/`, each verse once).

**Decision:** accept (Nathan, 2026-11-07)

1. **Matt 16:16, 17:25** *Simon* → *Simōn*: settled *Simōn* in 13 verses, *Simon* once (Matt); lexicon *Simōn* (Σίμων).
   **Apply:** `Matt.16.16` la: `Cui Simon Petrus` → `Cui Simōn Petrus`
   **Apply:** `Matt.17.25` la: `Simon?` → `Simōn?`
2. **Matt 17:14** *congenūclāns* → *congenuclāns*: settled Mark 1:40 *congenuclāns*.
   **Apply:** `Matt.17.14` la: `congenūclāns` → `congenuclāns`
3. **Matt 27:29** *congenūclāntēs* → *congenuclantēs*: as item 2, and *-antēs* is short before *nt* (long only
   before *ns*: *congenuclāns*).
   **Apply:** `Matt.27.29` la: `congenūclāntēs` → `congenuclantēs`
4. **Matt 22:32** *Abrahāmī* → *Abrāhāmī*: settled *Abrāhāmī* in 18 verses (Genesis), *Abrahāmī* once; WordPress *Abrāhāmī*.
   **Apply:** `Matt.22.32` la: `Deus Abrahāmī` → `Deus Abrāhāmī`
5. **Matt 22:32** *Isaācī* → *Isaacī*: settled *Isaacī* 4× (Genesis) against *Isaācī* once (Luke 3:34); WordPress *Isaacī*.
   **Apply:** `Matt.22.32` la: `Deus Isaācī` → `Deus Isaacī`

## 3. Your call (1 form, 4 places)

**Decision:** accept (Gaffiot: rabbi, unmarked) (Nathan, 2026-11-07)

1. **Matt 23:7, 23:8, 26:25, 26:49** *Rabbī* → *Rabbi*? Your settled text has *Rabbi* twice (John 1:38, 1:49), your
   draft *Rabbī* four times; W *rabbī* (Hebrew *rabbî*); Gaffiot heads *rabbi* without a mark. Accept for
   consistency with John, or keep *Rabbī* (and change John 1:38, 1:49 instead)?
   **Apply:** `Matt.23.7` la: `vocitārī Rabbī.` → `vocitārī Rabbi.`
   **Apply:** `Matt.23.8` la: `vocārī Rabbī;` → `vocārī Rabbi;`
   **Apply:** `Matt.26.25` la: `sum, Rabbī?”` → `sum, Rabbi?”`
   **Apply:** `Matt.26.49` la: `“Avē Rabbī,”` → `“Avē Rabbi,”`

## 4. Kept as you wrote them (50)

The pipeline's marking was wrong at these (read one by one); listed so the error rate can be judged:

| How the pipeline decided | Count | Examples (yours, kept → pipeline's) |
|---|---:|---|
| Gaffiot changed a W/M stem | 20 | *crucifīgendum → crucīfīgendum* (7 forms of *crucifīgō*), *quibuscumque → quībuscumque*, *hærentēs → haērentēs*, *stantēs → stāntēs*, *emite → ēmite*, *ēmērunt → emerunt*, *precandum → precāndum*, *cōnfringētur → cōnfringetur*, *neglēxērunt → neglexērunt* |
| lexicon (W/M only) | 14 | *sēque → seque*, *jējūnium → jejūnium*, *parēs → pārēs*, *Chrīstōs → Christōs*, *incrustātīs → incrustātis*, *legit → lēgit* (24:15 “whoso readeth”: present), *Galilæō → Galīlæō*, *Avē → Ave*, *Hōsanna → Hōsannā* (3×), *catellīs → catēllīs*, *baptīzandus/baptīzāte → baptiz-* (misled by settled Luke 12:50's slip; `settled-fixes.md`) |
| settled form (≥ 80%) | 5 | *Magdalēna → Magdalēnā* (nominative, 3×), *vīderitis → vīderītis* (future perfect, 2×: see above) |
| WordPress chose | 1 | *Jēsūs → Jēsus* (17:22; settled *Jēsūs* 137×) |
| WordPress alone | 4 | *Dāvīdidæ → Davīdidæ* (2×), *Nazarethā → Nazarēthā*, *Gethsēmanē → Gethsēmane* |
| homograph | 5 | see above |
| unknown | 1 | *septiduī* (stage 2's new word; no source knows it) |

**The Gaffiot-stem step is the weak point**: on the settled chapters it was wrong at 46 of 69 words
(`MORNING.md`). Worth a look before auto-applying anything it decides.
