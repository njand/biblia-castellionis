# Exodus 21–30: stages 1–5, one proposal per verse

Proposed 2026-11-14 (decision 30's standing rule), as Exodus 1–20 (`data/review/exod1-20-stages3-5.md`).
**Waiting for your approval.**

## Where it stands

- **Stage 1**: `text/draft/EXO.usfm`, Wikisource's Exodus 21–30 with the BSB's paragraphs, renumbered to the KJV (343
  verses, every chapter at the KJV count): 14 edits in `data/versification/Exod21-30.draft.edits.tsv`, explained in the
  stage-2 file.
- **Stage 2**: `data/review/exod21-30-stage2.md`, **33 corrections** against 1738, every one read on its page image
  (leaf given): 17 slips and readings found by the collation and by reading the 41 verses 1738's OCR covers poorly
  (21:32 *solvuntor*, 23:7 *Insontem*, 23:23 *praeibit*, 28:1 *sacerdotio*, 28:37 the doubled *insulae infulae* …),
  Castellio's *G. L. … H.* at 28:34 (marks dropped, words kept), 2 found by stage 2b (22:23 *presseris*, 29:24
  *porricito*), and 13 found by the readers of stages 3–5 (22:5 *depaverit*, 23:20 *a me*, 23:32 *foedus*, 28:28
  *a suis annulis ad annulos*, 30:34 *stacten* …). One is a difference between printings: 22:5, 1738 *depauerit*
  against 1726 and Wikisource *compaverit*; the base's reading is taken. **Applied to the draft.**
- **Stage 2b**: Castellio's text as printed, `text/orig/draft/EXO.usfm` chapters 21–30 and
  `data/review/exod21-30-orig.md`: 4,787 words, 82% read in the OCR, the 5 spelling-prone words and 3 near misses read
  on the page (`data/decisions/Exod.orig.tsv`), 11 paragraphs from 1738's indents (each checked on the page).
- **Stages 3–5**: `data/review/exod21-30-ch21.md` … `-ch30.md`, 343 items, all checking `ok`. Preview:
  **`text/draft/EXO.preview.usfm`**.

## How the verses were made

Four readers (21–22, 23–25, 26–28, 29–30) under one brief, as for 1–20. Their calls are in
`data/decisions/Exod.layout.tsv` (59 lines for 21–30) and `Exod.forms.tsv` (316 rows, each with its reason). I read
their reports, checked every suspected Wikisource slip on 1738's page (stage 2, section 4: all 13 confirmed), re-keyed
their rows to the corrected words, and added the paragraph reopenings.

## Calls worth a look

- **Speeches**: God's laws, 21:1–23:33, one speech; the sanctuary speech opens at 25:2 and is left open at 30:38 (it
  runs on into 31; decision 31). A paragraph inside a speech reopens it with “ (the settled 12:14). The narrator's own
  introductions inside it: 30:10 closes, 30:11 *Item hæc Mōsī dīxit Jōva,* is narrative, 30:12 reopens; 30:17 *“Item
  facitō lābrum æreum,” inquit, “*, 30:22, 30:34: the speech closed and reopened around *inquit*, Castellio's
  parentheses *(inquit Jōva Mōsī)*, *(inquit)* turned into commas, as the settled 9:13, 10:1 and 19:10. (The settled
  14:4 keeps a parenthetical *(inquit)* inside the speech instead: say which you prefer.) 30:31–33 reported, not quoted.
- **Paragraphs moved** to the sentence start: 29:10 → 29:5, 29:45 → 29:44.
- **Words Castellio coins**, marked by analogy (no source has them): *initiātōrius*, *suffītōrius*, *exceptītius*,
  *porrēctītius* (29:27; its e is long by *porrēctus*, though the same verse's *porrectum* is from *porriciō*, short:
  worth a look), *messālia*, *conditālia*, *appositītium*, *ēphōdum* (25:7, from the Hebrew; elsewhere *ephodus* all
  short as Gaffiot: the two disagree, and one form should win).
- ***hīnis*, *hīnem***: Gaffiot gives no length; marked long from the Greek εἵν and the Hebrew *hîn*.
- ***vēscēris*** (23:15) as a future, against the settled Gen 2:16–17, 3:18 *vēsceris*: one or the other.
- **22:30 and 23:11 *Idem***: the tool proposed *Īdēm* (a place name) unflagged; the readers caught both. Other such
  unflagged words may have slipped: a reason to read the preview.

## Your decisions of 2026-11-14, and a proofread

Applied to the proposal (decisions 63, 65, 66): *ēphōd-* long in all 13 places, *porrectītius* short e, *hīn-*
long, *lābrum*, *vēscēris*, *inquit* with commas. Then an independent proofread of all 343 verses found 16
problems, all fixed here (the per-verse files re-proposed, all 343 checking `ok`):
- four chapters (22, 26, 28, 30) opened with `\nb` (no new paragraph) after a chapter ending its sentence: now `\p`;
- 24:8 kept Wikisource's straight quotation marks, which also lost 24:9 its capital (*Et Mōsēs quidem*); 25:4
  *hyacinthum* lower case (the list of 25:3 runs on);
- forms: 22:26 *accēperis* (future perfect, short -is, as every other in 21–30), 23:13 *ūsurpātō*, 24:10
  *sapphīrīnī* (Gaffiot), 25:25 *factā margine* (ablative absolute), 28:6 *Ēphōdum*, 28:28 *annulīs*, and
  *cherūb-* in all four places (25:18, 22, 26:1, 31), as the settled Gen 3:24 *Cherūbōs* (Hebrew kərûḇîm);
- spelling by decisions already made, as rule rows in `orthography.tsv`: *exsecrātor* 22:28 and *exsecūtus* 23:22
  (decision 42, Gaffiot *exsecror*, *exsequor*; the settled text is *exs-* throughout), *fētificēs* 23:30 (Gaffiot
  *fētificō*, settled *fētificārēmus*), *ascenderat* 24:2 (decision 37).

Left as they are, for you to know: 26:14 *Huic īdem tegumentō* keeps *īdem* masculine ("you likewise", the
readers' reading of the syntax); 28:24 *duās illās argenteās catēnulās*: the Hebrew has gold (as 28:14, 22), but
1738, 1750 and Wikisource all read *argenteas*, so it is Castellio's wording. One inconsistency outside these
chapters: the settled Heb 9:5 has *Cherubī* (u unmarked) against Gen 3:24 *Cherūbōs*; say if Heb 9:5 should be
*Cherūbī*.

## Questions for the whole edition

1. **Three approved spelling rules turn bronze into air.** *æreæ → aeriæ*, *æreas → aerias*, *æreis → aeriis*
   (`data/rules/orthography.tsv`, rows 7, 11, 19) were learned from the birds “of the air” (Gen 1:26, 9:2, Matt
   8:20): *volucrēs āeriæ*. They are word rules, so here they also respell *æreus* “of bronze”: 27:10 and 27:18
   *basibus æreīs* → *āeriīs*, 27:17 *basēs æreās* → *āeriās* (the proposal in `-ch27.md` has these, wrongly), and the
   readers saw the same at 27:4. **Decided 2026-11-14 (Nathan): replaced as proposed below.** The rules file is
   changed and `propose Exod 21-30` re-run: 27:10 and 27:18 now read *basibus æreīs*, 27:17 *basēs æreās*, and no
   *āeri-* is left in the preview; all 343 Apply lines check `ok`.

   **The evidence.** Wikisource spells both words *aere-*; every one of its 30 places (whole Bible, as fetched):
   - *of the air* (13), every one beside a form of *volucris*: Gen 1:26 *volucribus aereis*, 1:28 *volucresque
     aereas*, 2:19 *aereas volucres*, 9:2 *aereis volucribus*, 1 Sam 17:44, 46 *volucribus aereis*, Ps 8:9 and Matt
     6:26 *volucres aereas*, Matt 8:20, Mark 4:4, 4:32, Luke 9:58, 13:19, Acts 10:12 *aereae volucres*, Acts 11:6
     *aereas volucres*; and, not beside it, Job 28:21 *aëreis abdita volucribus*, Zeph 1:3 *aereas uolucres* (u for
     v), Eph 2:2 *aëreae potestatis* (settled *āeriæ*, by reading).
   - *of bronze* (12), never beside it: 1 Sam 17:5 (three), 17:38, Lev 6:28, Josh 6:24, Exod 27:4, 27:10, 17, 18,
     30:18 (two), Rev 9:20.

   **Proposed** (`data/rules/orthography.tsv`): the three word rules (rows 7, 11, 19) to `rejected`, with the note
   *also respells æreus, of bronze (Exod 27:10, 17, 18); replaced by phrase rules*, and seven phrase rules,
   `approved`:

   | old | new |
   |---|---|
   | volucribus æreis | volucribus aeriis |
   | æreis volucribus | aeriis volucribus |
   | volucres æreas | volucres aerias |
   | volucresque æreas | volucresque aerias |
   | æreas volucres | aerias volucres |
   | æreæ volucres | aeriæ volucres |
   | volucres æreæ | volucres aeriæ |

   Tried on all of Wikisource with the rules so changed: the 13 birds beside *volucris* come out *āeri-* as the
   settled text has them (*volucribus āeriīs*, *āeriæ volucrēs* …), and all 12 bronze places stay *ære-*. Three air
   places are missed and would be read like other homographs when their books come: Job 28:21 (words between),
   Zeph 1:3 (*uolucres*, until u/v is normalized first), Eph 2:2 (settled already). The settled text is not
   touched: its *āeri-* forms were all birds (and Eph 2:2).

   A phrase rule with a diphthong put its spaces back one letter off (*āeriævo lucrēs*); fixed in
   `pipeline/normalize.py` `carry()` (each word of an equal-length phrase is now marked on its own, and the ligatures
   are tied after the spaces), with tests.

   On your yes I change the rules file, re-run `propose` for chapter 27 (the readers' rows already say *æreīs*,
   *æreās*), and check that 27:10, 17, 18 come out *basibus æreīs*, *basēs æreās*.
2. ***lābrum*** (the basin, 30:17–28) and ***labrum*** (the lip) are different words; the readers marked the basin
   long (Gaffiot *lābrum*). The settled text has neither.

**Decision:** accept (Nathan, 2026-11-14: decision 69, settled in `text/EXO.usfm`)
