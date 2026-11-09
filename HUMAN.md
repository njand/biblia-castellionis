# For Nathan

## Now

- **2026-11-07 (overnight): the Matthew 14–28 pilot is through stages 2–5 and waits for your review.** Start
  with `data/review/MORNING.md`: what was built, the order to review in, the measured rates for decision 6, and
  what could not be verified. Five review files (`settled-fixes.md`, `matt14-28-stage2.md`, `-spelling.md`,
  `-macrons.md`, `-structure.md`) and a preview of the result (`text/draft/MAT.preview.usfm`). New tools:
  `python -m pipeline review check|apply` (applies accepted Apply lines), `versify --draft`, 1573 as an aligned
  witness (`ocr-1573`, L. … G. passages kept and flagged), and the stage modules `collate`, `normalize`,
  `macrons`, `structure`, and `draft`/`collate` commands. Mark 6–16 is through stage 2 only
  (`mark6-16-stage2.md`, on a new Wikisource-based `text/draft/MRK.usfm`); Acts was collated against 1573 as a
  report (`data/calibration/acts1573.md`). Nothing committed.
- **2026-11-05: all nine plan decisions taken** (below); `brief.md`, `PLAN.md` and `CLAUDE.md` updated to match.
  Decision 9 makes USFM the master copy: LaTeX becomes a generated print output and Overleaf editing ends.
- **M0 (groundwork) is done** (commit 3badc59). `python -m pipeline` fetches every witness and keeps the chapter
  ledger.
- **M1 (calibration) is in progress** in its own session. Step 1 (migration) is done and accepted, not yet committed:
  the 62 finished chapters (2,244 verses) are migrated to `text/GEN|MAT|MRK|LUK|JHN.usfm`, and Matthew 14–28
  to `text/draft/MAT.usfm`. Converting the USFM back to LaTeX matches your LaTeX token for token, except for
  two print changes you accepted (decision 10). The per-verse gold set is in `data/gold/`. **From now on, edit the
  USFM, not the LaTeX.** Step 2 (spelling rules) is drafted and awaits your review: `data/rules/REVIEW.md`.
  Genesis is renumbered to the KJV (decision 14): 774 verses, every chapter at the KJV count. Step 3 is done:
  the seven OCR witnesses are aligned to verse ids and scored (`data/calibration/witnesses.md`). The best is
  1758, which has 98% of your words and reads 96.6% of them the same. 1681 is weakest (75.7%). TXT/1 (1726–27)
  reads well (97.0%) but holds only 44% of the text. WordPress turns out to be Wikisource with macrons, so it is
  not an independent witness. Step 4 is done: the harness (`data/calibration/harness.md`) runs normalize and
  macronize from Wikisource and meets both targets when each chapter learns from the other chapters:
  99.76% words, 99.56% spelling, 99.26% vowels. It uses your *proposed* spelling rules: approving them is still
  your call. Step 5 is done (`data/calibration/scans.md`). Comparing the 1760 scan with Castellio's own 1551, 1554
  and 1556 editions led to decision 15: the New Testament base is **1556**, his last revision. In the Gospels,
  Wikisource and 1758 already follow it closely. In Acts–Revelation, Wikisource prints Castellio's *early* wording,
  with 1750 and 1760 (e.g. *favor*, *humanitas*, *synagoga*, *lavit*), which he revised in 1556 (*gratia*, *caro*,
  *collegium*, *baptizavit*). Stage 2 will propose roughly 80–100 such changes there (`data/calibration/nt1556.tsv`).
  The editions and their history are written up in `docs/editions.md`. Then the posthumous 1573 Basel edition
  (Perna, “from his last revision”) was found and collated: it revises 1556 further, and decision 24 makes it the
  NT base in 1556's place (`data/calibration/nt1573.tsv`).
  **M1 is complete and waits for your review**; the Matthew 14–28 pilot starts after that.

## Decisions waiting

- **Genesis 28–50 is settled** (2026-11-08; decision 32): approved by you "for now", in `text/GEN.usfm` (Genesis now
  1,532 verses; every chapter at the KJV count but 41, where 41:57 is absent in every printing), gold rebuilt, draft
  removed. Record: `data/review/gen28-50-stages3-5.md`, `-stage2.md`, `-ch28.md` … `-ch50.md`,
  `settled-fixes-gen.md`, `data/decisions/Gen.*.tsv`. **Everything you transcribed earlier is now settled**: next is
  new transcription, while your in-depth review (decision 30) can begin. One call for the whole edition: *Rachel*
  (your Matt 2:18) vs *Rāchēl-* in the other cases.
- **John 5–21 is settled** (2026-11-08; decision 31): approved by you "for now", in `text/JHN.usfm` (879 verses, the
  KJV count), gold rebuilt, draft removed. **All four Gospels are now settled** (Matthew 1,071, Mark 678, Luke 1,151,
  John 879 verses). Record: `data/review/john5-21-stages3-5.md`, `-stage2.md`, `-ch05.md` … `-ch21.md`,
  `data/decisions/John.*.tsv`. Genesis 28–50 followed (decision 32).
- **Luke 14–24 is settled** (2026-11-08; decision 30): approved by you "for now", in `text/LUK.usfm` (1,151 verses,
  the KJV count), gold rebuilt, draft removed. Record: `data/review/luke14-24-stages3-5.md`, `-stage2.md`,
  `-ch14.md` … `-ch24.md`, `data/decisions/Luke.*.tsv`. **Your in-depth review of everything settled since
  2026-11-07 comes later** (decision 30), while new transcription goes on.
- **Mark 6–16 is settled** (2026-11-08; decisions 28–29): every verse read; Mark 6 accepted by you, 7–16 by me
  under your delegation, with each fix recorded in the review log of `data/review/mark6-16-stages3-5.md`. The
  chapters are in `text/MRK.usfm` (678 verses, the KJV count), `data/gold/Mark.tsv` rebuilt, `text/draft/MRK.usfm`
  removed (the pre-stage-3 draft is in git; `data/review/mark6-16-ch*.md` reproduce every change). Also applied:
  `settled-fixes-matt.md` (Matt 27:37 *JŪDÆŌRUM*, 20:29 *Hierichūnte*, 22:44 *Sedē*, 19:10 *cōnūbia*). **For your
  read-through**: the calls I made without you are listed in that review log (4 spelling rules added to
  `orthography.tsv`, 2 code fixes, 2 forms); everything is uncommitted.
- **Applied 2026-11-07** (all review proposals accepted except the open items below): `settled-fixes.md` (10, to
  `text/LUK.usfm`, `GEN.usfm`, `JHN.usfm`; gold rebuilt); Matthew's 3 verse-number splits; `matt14-28-stage2.md`
  (29), `-spelling.md` (40), `-macrons.md` (12 items), `-structure.md` (25 items) to `text/draft/MAT.usfm`;
  `mark6-16-stage2.md` (24) to `text/draft/MRK.usfm` (Mark 6–16 now *corrected*). Matt 19:4 kept unmarked; the 4
  1556 variants recorded. Then *Rabbi* by Gaffiot's standard (Matt 23:7, 23:8, 26:25, 26:49) and the 3 BSB
  paragraphs (Matt 17:19, 18:19, 24:26).
- **Matthew 14–28 is settled** (2026-11-07; decision 26): every review item decided and applied, the chapters
  moved into `text/MAT.usfm` (chapters 1–13 untouched; 1,071 verses, the KJV count) and `data/gold/Matt.tsv`
  rebuilt; `text/draft/MAT.usfm` and `MAT.preview.usfm` removed (the draft is in git history).
- **Decision 6's threshold**: the Gaffiot stem step is fixed (2026-11-07: same-syllable rule, abbreviated endings
  not aligned, silent where the principal parts disagree); it is now wrong on 5 of 25 words (was 46 of 69).
  Lexicon-only macrons: 0.65% of words wrong; all: 1.63% (was 1.79%).
- **`data/review/settled-1573.md` applied** (2026-11-07, decision 27; all 46 accepted, `data/gold/` rebuilt): the settled NT chapters (Matthew 1–13, Mark 1–5, Luke 1–13,
  John 1–4) collated against 1573, every place read on the page image. 46 items: 22 words missing or wrong (Wikisource
  slips your text inherited: Luke 4:27 *pūrgātus et*, 6:12 *per nox*, 7:11 *proficīsceret*, 13:4 *quod* …), 21 different
  readings (Matt 6:4, 6, 18 *occulta*, 13:32 *holerum*, Luke 9:12 *dēversentur* …), **John 2:18 revised between 1556 and
  1573** (*Ēde nōbīs aliquod prōdigium …*), 2 forms (*tonitruī*, *sēminece*). Kept and listed: *tetrarchēs*,
  *assimulem*, *circumsedēret*, *abstergēmus*.
- **Possible follow-ups** (not started): chapter summaries (decision 3) are in neither draft nor settled USFM;
  the same collation for settled Genesis against the 1738 OCR (the OT base).
- **The spelling rules are decided** (2026-11-06, decisions 16–20; `data/rules/REVIEW.md` has the evidence).
  `orthography.tsv`: 114 rules approved, 12 rejected; three left for the names list (*Bennammi*, *Hierichūntem*,
  with *Henōchī/Enōchī* and *Abius*).
- **The fixes they imply are applied** (2026-11-06; `data/review/spelling-fixes.md`, all accepted): 128
  replacements in `text/*.usfm` (36 œ, 7 spellings, 27 perfects, 7 word divisions, 23 single fixes and Egypt
  capitals, 28 capitals for God); `data/gold/` rebuilt. The legacy LaTeX now differs from the USFM in these too.
- **Committed** (2026-11-07, 7083d31): the names, wording, 1573 and quotation-mark work. Next: the Matthew 14–28
  pilot's stage 2 (collation against 1573) and a review/apply tool.

## Decided

| # | Date | Decision |
|---|---|---|
| 1 | 2026-11-05 | **Base edition: the editions Wikisource follows** (1760 NT, 1738 OT; the NT part is replaced by decision 15). Other printings' differing readings are recorded as variants. Wording in the finished chapters (from 1726–27) that differs is proposed for review, never changed automatically. |
| 2 | 2026-11-05 | **Apocrypha: in scope, after the 66 books** (M7). Placement decided then. |
| 3 | 2026-11-05 | **Chapter summaries: included** as small italic headings under each chapter number, normalized and macronized like the text. |
| 4 | 2026-11-05 | **Quotation marks: “…” for direct speech, ‘…’ only for quotes within it; reported discourse unmarked.** About 33 reported passages in the finished chapters lose their ‘…’ (proposed for review). |
| 5 | 2026-11-05 | **Versification: KJV everywhere**, mappings recorded; Psalm titles unnumbered above verse 1. |
| 6 | 2026-11-05 | **Review: strict pilot, then relax.** Every change is reviewed during Matthew 14–28. The auto-apply policy (sources agree on audible macrons, two-scan corrections, approved spelling rules, with a 1-in-10 full read) starts once the measured error rate is acceptable. |
| 7 | 2026-11-05 | **License: CC BY-SA 4.0**, crediting Wikisource and the scan libraries. |
| 8 | 2026-11-05 | **Latin databases used in place** from `../fur-fulminis/data` (`LATIN_REF_HOME` to move them). |
| 9 | 2026-11-05 | **USFM is the master copy** (`text/<book>.usfm`). The website, EPUBs, print PDF (generated LaTeX in your current layout), TXT and an ebible.org submission are all built from it (PLAN.md §4a). Overleaf editing ends; the old LaTeX/HTML/EPUB/TXT folders retire once the migration is verified (removal is your call). |
| 10 | 2026-11-05 | **Migration accepted.** `text/*.usfm` is the master copy for the 62 finished chapters, with two print changes: the Benedictus's `\medskip` (Luke 1:75) becomes an ordinary stanza break, and Gen 15:18 gains a space before verse 19. |
| 11 | 2026-11-05 | **Genesis's commented-out notes dropped** (three draft headings, two footnotes); the printed chapter summaries cover the same ground. They remain in git history. |
| 12 | 2026-11-05 | **Genesis renumbered to the KJV in one batch**: chapters 3, 4, 6, 7, 10, 11, 14, 18, 23, 24, only verse numbers moving, approved once from a combined report of every moved boundary. |
| 13 | 2026-11-05 | **Old outputs retire when the M2 builds replace them.** `LaTeX/biblia/`, `HTML/`, `EPUB/`, `TXT/3–4` and `scripts/latex_converter.py` stay (frozen, legacy) until the new website/EPUB/PDF exist; `LaTeX/main.tex` and `title.tex` then move to the PDF template rather than going. |
| 14 | 2026-11-05 | **Genesis renumbering approved and applied** as proposed in `data/versification/Gen.REVIEW.md`: 11 moved boundaries, including chapter breaks mid-sentence at 6:22/7:1 and 7:24/8:1 (`\nb`), and the Septuagint's Caīnān (old 11:14–15) joined to 11:13. Words unchanged; every chapter at the KJV count. The legacy LaTeX now differs from the USFM only in these markers. |
| 15 | 2026-11-06 | **New Testament base: Castellio's 1556 edition** (Basel, Oporinus; e-rara 10281656), his last revision in his lifetime. Wikisource stays the working text. Where printings differ, the 1556 reading is proposed for review. The early wording (1551/1554 *homine natus*, *collegium*), Bünemann 1745, 1760 and the other printings are recorded as variants. 1758 serves as the page image where 1556 can't be cropped. Evidence: `data/calibration/scans.md` (Wikisource/1758 agrees with 1556 at 10 of 14 test places in the Gospels, 1760 at 4). The OT base (1738) is unchanged. *The NT base is replaced by decision 24 (1573).* |
| 16 | 2026-11-06 | **Ligatures: æ and œ for every diphthong**, as Gaffiot (*fœdus, cœpī, pœna, prœlium*); separate syllables stay apart (*Isrāēlīta, coēmptī, āer*). The ae → æ and oe → œ rules are approved. The 36 oe spellings in Genesis and Matthew 11–12 will be proposed as fixes to the USFM (REVIEW.md §5). |
| 17 | 2026-11-06 | **j wherever it is pronounced** (consonantal i → j, u → v), so always in compounds of *jaciō*: *abjiciō, ējicere, prōjiciō, dējicit, subjiciō*, not Gaffiot's *abiciō*. Your *eicere* (Mark 3:22) becomes a proposed fix to *ējicere*. *ŏbex, ŏbicis* keeps i, as Gaffiot's headword. |
| 18 | 2026-11-06 | **Spelling variants follow 1st-century-BC prose, Cicero above all**, by corpus counts (`pipeline latin attest --count`); where the counts are near even or too thin, the spelling most consistent with the other choices. First results: *iīs, umerus, harēna, sēscentī, erus, reppererit* (REVIEW.md §3). Where the corpus may reflect outdated editions, Gaffiot's headword wins (*quidquid*); where there is no 1st-century-BC evidence, the closest evidence or analogy (*pellicius*). |
| 19 | 2026-11-06 | **-īv- perfects follow republican prose form by form.** A form's own counts decide when clear (≥3 hits and 2:1); otherwise the pooled counts for its ending; where the form's thin evidence leans against the pool, it keeps its spelling. Result: 3rd sing. *-īvit* (128:11), *-īvimus*; short forms everywhere else (*audierat, audierit, audīsse, audīstis, petīsse*); the 3rd plural by verb (*audiērunt* 19:1, *petīvērunt* 20:7, *quæsīvērunt* 4:1). Compounds of *eō* and verbs without an -īvī perfect (*dēsinō, feriō, insiliō, dēsiliō*) are left out. 51 rules in `orthography.tsv`; 27 words of the settled chapters to be proposed (e.g. *petiit* → *petīvit* 5×, *audīvistis* → *audīstis* 5×). |
| 20 | 2026-11-06 | **Capitals for God: NRSV style.** *Pater, Fīlius, Spīritus Sānctus, Servātor, Suprēmus, Sānctus Deī* capitalized when they refer to God or Christ; *Fīlius Hominis*; adjectives (*Pater vester cælestis*) and pronouns lower case. Castellio's 1556 capitalizes only *Deus*, *Supremus* and *Sanctus Dei*, so this is a modern editorial choice (`docs/editions.md`). Decided per verse; about 15 fixes to the settled chapters to be proposed. |
| 21 | 2026-11-06 | **Enoch is *Henōchus* in both Testaments**: Hebrew חֲנוֹךְ has ḥet, Greek Ἑνὼχ the rough breathing, and the Vulgate writes *Henoch* in both. Castellio's NT *Enochus* (1556) is not followed. Luke 3:37 *Ēnōchī* → *Henōchī* and Gen 25:4 *Henochum* → *Henōchum* applied (`data/review/names.md`). |
| 22 | 2026-11-06 | **Names: Jericho, Benammi, Abius.** *Hierichūs, -ūntis* as in 1556 (rule *Hiericunt- → Hierichunt-* for Wikisource's Gospels); Gen 19:38 *Bennammi* → *Benammi* (1738, 1750, Wikisource; Hebrew *ben-ʿammî*), applied; *Abius* (Abihu) kept from the j rule (`JV_KEEP`). |
| 23 | 2026-11-06 | **Wording against Wikisource** (`data/review/wording.md`, 41 places): six changes applied where the printings agree against your text (Gen 7:14 *ālitum*, Mark 2:7 *Qui fit*, Mark 4:19 *cupiditātēs, quæ*, Mark 5:7 *Quid*, Mark 5:38 *collēgiī*; Luke 5:39 *pōtātō* was applied, then reverted to your *pōtō*, the classical participle: Cicero, *Brutus* 333 *eō pōtō*); Gen 11:25 keeps *ūndēvīgintī* over 1738's *novemdecim* (decision 18); the other 34 keep your text (Wikisource slips, or readings no printing has, such as the clause after Luke 11:7). *The Luke 11:7 clause turned out to be in 1556 and 1573 (marked L. … G.); added 2026-11-07 (item 10): `… tibi dare.’ Sī ille pulsāre persevērāverit,` with verse 8 starting* mihi. |
| 24 | 2026-11-06 | **New Testament base: the 1573 Basel edition** (Petrus Perna, *ex postrema recognitione*; MDZ bsb10141277; USTC 616558, VD16 B 2638), replacing 1556 in decision 15. It is the 1556 text revised further (some 30–60 word changes, e.g. Mark 6:6 *infidentiam*, John 14:30 *mundi*, 1 Tim 3:16 *carne*), and it is the text of your finished chapters, 1681, 1758 and Wikisource's Gospels. Its OCR finds 89–98% of the words, it numbers the verses, and its IIIF images can be cropped from the hOCR word boxes. Wikisource stays the working text; where it differs from 1573 (as in its early-line Acts–Revelation), the 1573 reading is proposed for review. 1556 stays the reference: its readings where 1573 differs are recorded as variants, like the early wording (1551/1554), Bünemann 1745, 1760 and the later printings. Luke 12:6 keeps *duōbus assāriīs* (1573). Evidence: `data/calibration/scans.md`, `nt1573.tsv`. |
| 25 | 2026-11-07 | **Quotation marks in the settled chapters** (`data/review/quotes.md`, all accepted): of the 167 passages in ‘…’, 80 are reported speech and lose their marks (70 statements and commands; 10 indirect questions, which also lose their question mark), two slips are fixed (Luke 12:18 “‘Hoc agam,’; Gen 24:47 ‘Bathūēlis), and the other 87 keep their marks. 87 replacements applied to `text/*.usfm`; `data/gold/` rebuilt. |
| 26 | 2026-11-07 | **Matthew 14–28 approved; perfect forms of *eō*, *-āstis*, *Rabbi*.** Every proposal in `data/review/matt14-28-*.md`, `settled-fixes.md` and `mark6-16-stage2.md` accepted except as follows. The perfect of *eō* and its compounds follows republican prose (Latin Library, `latin attest --count`): *-iī* (27:0 against *-īvī* in the compounds), *-iit*, *-iērunt*, and contracted *-īstī/-īstis/-īsse/-īssent* (no *-iistī/-iisse/-iissent* at all), so Matt 25:25 keeps *iī* (1573 *iui*) and Mark 14:48 keeps *existis* (1573 *exijstis*), as Matt 11:8–9 *exīstis*. First-conjugation *-āvistis/-āstis* is near even in Cicero (9:12), so the edition's consistency decides: *-āstis* (Matt 25:36 *vīsitāstis*, = 1573). *Rabbi* unmarked, Gaffiot's form. The 3 BSB paragraphs added (Matt 17:19, 18:19, 24:26). Evidence in `matt14-28-spelling.md` group 6. |
| 27 | 2026-11-07 | **The settled NT chapters follow 1573 where it and the printings agree against them** (`data/review/settled-1573.md`, all 46 accepted, every place read on the 1573 page image): 22 Wikisource slips (Luke 4:27 *est*, 6:12 *pernox*, 7:11 *proficīscerētur* …), 21 readings (Matt 6:4, 6, 18 *occulta*, 13:32 *holerum*, Luke 9:12 *dēversentur* …), 2 forms (*tonitruī*, *sēminece*), and John 2:18 in Castellio's 1573 revision (*Ēde nōbīs aliquod prōdigium …*; 1556 recorded as a variant). Kept: *tetrarchēs* (Gaffiot, Cicero), *assimulem*, *circumsedēret*, *abstergēmus*. |
| 28 | 2026-11-08 | **Mark 6–16, stages 3–5: the per-verse review's open questions** (`data/review/mark6-16-stages3-5.md`). Decision 6's unflagged tier adds homographs that WordPress 2019 chose and your settled forms mark alike (0.28% wrong, as lexicon-only macrons' 0.26%). The 22 macrons decided in context are accepted as a batch; the three BSB paragraphs moved off mid-sentence (12:12 *Igitur*, 12:37 *Cumque*, 14:26) are accepted; 7:11 (only the man's words in ‘…’), 7:19 (*expūrgāns omnēs cibōs* inside the speech), 8:28 (the accusative answer as speech) and 11:31 (the deliberation ends before *Sīn*) stay as proposed. Quoted Scripture: Isa 66:24 in `\qt` at 9:44, 46 and 48; the commandments at 10:19 in `\qt` with ‘…’; Gen 1:27 at 10:6 and the allusion at 8:18 also in `\qt` with ‘…’ (unlike your Matt 19:4). The three Matthew slips are to be proposed as fixes. Each chapter's verses still wait on its Decision line. |
| 29 | 2026-11-08 | **Mark 6–16 settled under delegation.** After accepting Mark 6 you asked me to go through the rest "very carefully, examining the evidence for each point", apply my recommendations and record each change; you will read the whole text later and can override then. Every verse of Mark 7–16 was read with its evidence and accepted; fixes made on the way: spelling rules *quenquam → quemquam*, *sepe → saepe* (the hedge), *Genezarethanum → Gennezarethanum*, *Bethpage → Bethphage*; the long prefix before *j* in compounds of *jaciō* (*ējicere*, *trājēcit*, as your text 50 of 50); a verse-start capital kept for names your text never lowers (*Pīlātus*); 10:1 *convenit*, 15:34 *sabachtanī*; Matt 19:10 *cōnūbia* (corpus and Gaffiot), with your three Matthew fixes. |
| 30 | 2026-11-08 | **Luke 14–24 approved for now; review later.** Stages 1–5 as for Mark (17 stage-2 slips read on the 1573 images; 491 verses, 29 macrons decided in context, 252 layout lines) settled in `text/LUK.usfm`. Standing rule: the chapters you transcribed earlier are taken through the pipeline, every flag and verse checked by me with its evidence, and settled on your approval; your in-depth review of the whole comes after they are all done, while new transcription goes on. Everything stays reviewable (`data/review/`, `data/decisions/`). |
| 31 | 2026-11-08 | **John 5–21 approved for now; the Gospels are complete.** Stages 1–5 as for Luke (21 stage-2 corrections read on the 1573 images, 3 of them the base edition's forms *lōtum*, *tonitru*, *lōtus*; 28 macrons decided in context; 392 layout lines) settled in `text/JHN.usfm`. A discourse running over a chapter break is left open, as your Matt 5:48 → 6:1 (John 9:41, 14:31, 15:27). Your in-depth review follows decision 30. |
| 32 | 2026-11-08 | **Genesis 28–50 approved for now; your earlier transcriptions are all settled.** The first Old Testament run: Wikisource collated against 1738 (the base), 1750 and your 1726 text; 61 stage-2 corrections, mostly read on the 1738 page images; 41:57 recorded as absent (every printing ends chapter 41 at 41:56); Castellio's *G.* … *H.* marks at 44:6 dropped, the words kept (as Matt 19:4); 791 macrons decided in context and 221 layout lines; your Gen 25:33 *Jūrā*; three spelling rules (*adjutus*, *abjudicabitur*, *quattuordecim*). Settled in `text/GEN.usfm`. Open for your review: *Rachel* vs *Rāchēl-*. Your in-depth review follows decision 30. |

## How to run

```
python -m pipeline fetch all        # once; downloads are cached in sources/ (≈260 MB)
python -m pipeline status
python -m pipeline status Matt --chapters
```
