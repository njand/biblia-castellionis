# For Nathan

## Now

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
  The editions and their history are written up in `docs/editions.md`.
  **M1 is complete and waits for your review**; the Matthew 14–28 pilot starts after that.

## Decisions waiting

- **The spelling rules are decided** (2026-11-06, decisions 16–20; `data/rules/REVIEW.md` has the evidence).
  `orthography.tsv`: 114 rules approved, 12 rejected; three left for the names list (*Bennammi*, *Hierichūntem*,
  with *Henōchī/Enōchī* and *Abius*).
- **The fixes they imply are applied** (2026-11-06; `data/review/spelling-fixes.md`, all accepted): 128
  replacements in `text/*.usfm` (36 œ, 7 spellings, 27 perfects, 7 word divisions, 23 single fixes and Egypt
  capitals, 28 capitals for God); `data/gold/` rebuilt. The legacy LaTeX now differs from the USFM in these too.
- **Commit M1** when you're ready: everything since 7516351 is uncommitted.

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
| 15 | 2026-11-06 | **New Testament base: Castellio's 1556 edition** (Basel, Oporinus; e-rara 10281656), his last revision in his lifetime. Wikisource stays the working text. Where printings differ, the 1556 reading is proposed for review. The early wording (1551/1554 *homine natus*, *collegium*), Bünemann 1745, 1760 and the other printings are recorded as variants. 1758 serves as the page image where 1556 can't be cropped. Evidence: `data/calibration/scans.md` (Wikisource/1758 agrees with 1556 at 10 of 14 test places in the Gospels, 1760 at 4). The OT base (1738) is unchanged. |
| 16 | 2026-11-06 | **Ligatures: æ and œ for every diphthong**, as Gaffiot (*fœdus, cœpī, pœna, prœlium*); separate syllables stay apart (*Isrāēlīta, coēmptī, āer*). The ae → æ and oe → œ rules are approved. The 36 oe spellings in Genesis and Matthew 11–12 will be proposed as fixes to the USFM (REVIEW.md §5). |
| 17 | 2026-11-06 | **j wherever it is pronounced** (consonantal i → j, u → v), so always in compounds of *jaciō*: *abjiciō, ējicere, prōjiciō, dējicit, subjiciō*, not Gaffiot's *abiciō*. Your *eicere* (Mark 3:22) becomes a proposed fix to *ējicere*. *ŏbex, ŏbicis* keeps i, as Gaffiot's headword. |
| 18 | 2026-11-06 | **Spelling variants follow 1st-century-BC prose, Cicero above all**, by corpus counts (`pipeline latin attest --count`); where the counts are near even or too thin, the spelling most consistent with the other choices. First results: *iīs, umerus, harēna, sēscentī, erus, reppererit* (REVIEW.md §3). Where the corpus may reflect outdated editions, Gaffiot's headword wins (*quidquid*); where there is no 1st-century-BC evidence, the closest evidence or analogy (*pellicius*). |
| 19 | 2026-11-06 | **-īv- perfects follow republican prose form by form.** A form's own counts decide when clear (≥3 hits and 2:1); otherwise the pooled counts for its ending; where the form's thin evidence leans against the pool, it keeps its spelling. Result: 3rd sing. *-īvit* (128:11), *-īvimus*; short forms everywhere else (*audierat, audierit, audīsse, audīstis, petīsse*); the 3rd plural by verb (*audiērunt* 19:1, *petīvērunt* 20:7, *quæsīvērunt* 4:1). Compounds of *eō* and verbs without an -īvī perfect (*dēsinō, feriō, insiliō, dēsiliō*) are left out. 51 rules in `orthography.tsv`; 27 words of the settled chapters to be proposed (e.g. *petiit* → *petīvit* 5×, *audīvistis* → *audīstis* 5×). |
| 20 | 2026-11-06 | **Capitals for God: NRSV style.** *Pater, Fīlius, Spīritus Sānctus, Servātor, Suprēmus, Sānctus Deī* capitalized when they refer to God or Christ; *Fīlius Hominis*; adjectives (*Pater vester cælestis*) and pronouns lower case. Castellio's 1556 capitalizes only *Deus*, *Supremus* and *Sanctus Dei*, so this is a modern editorial choice (`docs/editions.md`). Decided per verse; about 15 fixes to the settled chapters to be proposed. |

## How to run

```
python -m pipeline fetch all        # once; downloads are cached in sources/ (≈260 MB)
python -m pipeline status
python -m pipeline status Matt --chapters
```
