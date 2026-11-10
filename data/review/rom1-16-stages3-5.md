# Romans 1–16: stages 1–5, one proposal per verse

Proposed 2026-11-09; **approved by Nathan "for now" the same day and settled in `text/ROM.usfm`** (decision 33). Same tools and format as Acts (`data/review/acts1-28-stages3-5.md`;
`data/review/mark6-16-stages3-5.md` explains the format). You have no earlier work on Romans; `TXT/1 - OCR` (the
1726–27 printing, uncorrected Google Books OCR) served as a witness, read as an OCR.

## Where it stands

- **Stage 1**: `text/draft/ROM.usfm`, Wikisource's Romans with the BSB's paragraphs: 433 verses, every chapter at the
  KJV count. 17 versification edits (`data/versification/Rom.draft.edits.tsv`, applied): six boundaries move to where
  1573 prints its verse number (the KJV's), 15:9–11 follows 1573 and the KJV, and three follow the KJV where 1573 does
  not (3:22–23, 8:20–21, 9:11–12: 1573 numbers chapters 3 and 8 the old way, one verse short).
- **Stage 2**: `data/review/rom1-16-stage2.md`, **93 corrections** against the base, the 1573 Basel edition, **read on
  the 1573 page images** (crops in `sources/mdz-1573/crops/Rom.*`; a few from its OCR, marked so). Wikisource's Romans
  is Castellio's *early* wording: 51 Wikisource slips (section 1: *injustia*, *domum* for *donum*, *pareat* for
  *parcat*, *solo* for *volo*, 8:21 and 8:38 doubled words), 30 readings of the revised text (section 2: *humanitas* /
  *humana natura* → *caro* at 9:3, 9:5, 9:8; *vitiositas* → *peccatum* 7:17, 7:20, 7:23; *sacer* → *sanctus* 11:16;
  *animus* → *cor* 2:29; *scripturae* → *litterae* 15:4; *praevidit* → *praenovit* 8:29; 9:5 *Amen* → *Etiam*; 7:14
  *emancipatus*), 2 word divisions (3) and 10 found on a second pass (2a: three *fit* for *sit*, 11:17 *quidam*, 12:1
  *sanctam*, 13:5 *supplicii*, 15:31 *contumaces: utque*, two names). **Applied to the draft** (decision 30's standing
  rule). 1556's differing readings are recorded as variants (section 5 there: 1:2, 2:4, 6:11, 7:14, 16:6).
- **Stages 3–5**: `data/review/rom1-16-ch01.md` … `-ch16.md`, **433 items, all checking `ok`**; waiting for your
  approval. Preview: **`text/draft/ROM.preview.usfm`**. Quotation marks balance (`structure.quotes`: nothing open or
  unclosed, no chapter ending inside a quotation; its only notes are the two ‘…’ questions inside the Deuteronomy
  quotation at 10:6–7, which are right).

## What changed in the tools

- **`collate.py`**: the two blind spots Acts found are closed, with tests (`pipeline/tests/test_stages.py`).
  - **Words added or lost at a verse's edge** (`collate.edges`): the last words of each verse and the first of the next
    are compared with each witness's words there, including what it prints between its two rows; only differences that
    touch the boundary are kept. A chapter's opening is not compared (the printings' decorated initials, which the OCRs
    misread: a remaining blind spot for a word lost there). Run on Acts, it finds 9:2, 14:7, 14:8 and 16:13 *Et*, 15:29
    *Valete*, 25:25 and 28:31; in Romans it found nothing the other checks missed (1:11 *Scilicet* turned out to be a
    margin gloss).
  - **f against long s** (`collate.compare`): where 1573's hOCR and Wikisource keep them apart, a word read alike but
    for f/s is a place, kept only where the witness's word is Latin (`collate.sift`, 1,172 places in Acts down to 69,
    *sani/fani* among them). In Romans it found three *fit* for *sit* (3:24, 4:16, 10:10).
  - The 1726 witness is your `TXT/2` text where it has the book, otherwise the `TXT/1` OCR.
- **`normalize.py`**: the pattern that keeps the vowel *i* in Greek names (*Ēsāiās*, *Achāia*) also caught *maior* (9:12),
  which kept its *i*; *major*, *pejor*, *plēbējus*, *ējaculor* now take *j*. Test added. No other draft or settled text
  had such a word.
- **u-for-v sweep**: every *u* the j/v rule leaves before a vowel in Romans is a vowel (*mortuus*, *tribuit*,
  *perpetuum*); no slip like Acts' *aluo*, *soluimus*.

## How the verses were made

- **Layout and macrons**: four readers (1–3, 4–7, 8–11, 12–16) under one brief, each file checked by a script (the
  words of every layout line against the draft; every form against its verse). Their calls are in
  `data/decisions/Rom.layout.tsv` (92 lines) and `Rom.forms.tsv` (440 rows, each with its reason). Every word the
  pipeline flagged as a homograph nothing chose, unknown, Gaffiot's stem or your settled forms has a row; the
  settled-agreeing tier (1,168 words) was read through for **-a/-ā** and the other case endings and given a row where
  wrong: the settled majority's ablative is wrong for the nominative *jūstitia* six times (1:17, 3:21, 3:22, 4:11,
  10:6, 14:17), and *angustia*, *injūstitia*, *mēnsa*, *inopia*, *subjecta*, *serva* (6:19, with *membra*) likewise. A
  final sweep finds no *-a* left after *cum, ex, ā, ab, dē, prō, sine, præ*.
- **I then made the readers' choices agree across the book**: *Ādamō*, *Ādamī* (5:14, Gaffiot *Ādamus*), *Ēlīā*
  (11:2, your *Ēlīās*), 7:25 *ego īdem* (masculine, as 10:12), 14:23 *sī comēdit* (perfect, Vulgate *mandūcāverit*;
  a reader had the present), 15:28 *Hoc*; and dropped a form row that would have respelled 9:12 (the j fix above does
  it).
- **Names** follow your settled forms (*Abrāhāmus*, *Isaacō*, *Dāvīd*, *Mōsēs*, *Sara*, *Rebeccæ*, *Ēsāum*, *Ēsāiās*,
  *Pharaōnī*, *Sodomæ*, *Gomorræ*, *Satanam*, *Gāius*) and Acts (*Tīmotheus*, *Lūcius*, *Jāsōn*, *Prīscam*, *Aquilam*,
  *Corinthī*); new names take their lengths from Gaffiot or the Greek (*Andronīcum*, *Jūniam*, *Urbānum*, *Rūfum*,
  *Hērōdiōnem*, *Tryphōsam*, *Nēreum*, *Aristobōlī*, *Benjamīticæ*, *Cenchreēnsis* as your *Tarsēnsis*); where nothing
  tells the length the vowel is unmarked (*Phœbam*, *Epænetum*, *Ampliam*, *Stachym*, *Tryphænam*, *Asyncritum*,
  *Phlegontem*, *Hermam*, *Patrobam*, *Hermem*, *Olympam*, *Erastus*, *Isæa*).

## Flagged (1,715 words)

| Kind | Words |
|---|---:|
| homograph, your settled forms agreeing (no WordPress for Romans) | 1,168 |
| decided by reading the verse | 457 |
| capital changed by a layout line (*Fīlius*, *Pater*, *Spīritus Sānctus*, …) | 53 |
| lower case at a verse start | 31 |
| punctuation changed (verses) | 3 |
| your settled forms overrule the lexicon (*nisi*, *ō*, *sī*) | 3 |
| **unflagged**: the lexicon's one marking | 4,917 |

80 verses have their quotation marks, poetry or markers changed by a layout line; 16 have nothing flagged. The rates
were not re-measured for this run.

## Calls worth a look

- **Scripture** in `\qt` with “…” (Paul's own letter is not in quotation marks; a quotation inside a quotation in ‘…’).
  Set as **poetry** where the BSB does: 3:4 (Ps 51), 3:10–18 (the catena, **one quotation** under its single
  *quemadmodum est in litteris*, where the BSB marks each source), 4:7–8 (Ps 32), 8:36, 9:25–29 (9:25–26 one quotation,
  joined by *Ac*), 9:33, 10:19–21, 11:8–10, 11:26–27, 11:34–35 (one, joined by *Aut*), 12:20, 14:11, 15:9–12, 15:21.
  Kept as **prose** `\qt`: 1:17, 2:6 and 2:24 (woven into Paul's sentence), 4:3, 4:17–18, 7:7, 9:7, 9:9, 9:12–13,
  9:15, 9:17, 10:6–8 (the forbidden questions in ‘…’, the *hoc est* glosses outside), 10:15–16, 10:18 (woven in, though
  the BSB sets poetry), 11:3–4, 12:19, 13:9 (the commandments as one quotation), 15:3. The doxology 11:33–36 is poetry
  without `\qt` (Paul's own words).
- **Direct speech** in “…”: 8:15 *“Abba, Pater”*, the objector at 9:19 and 11:19, and 9:20 *“Cūr mē sīc fēcistī?”*.
  **Left unmarked** where the BSB quotes: 3:8 (*sīc ajunt quīdam dīcere nōs*), 4:22–23, 10:5, 10:9, 10:11, 10:13,
  9:30–31; the rhetorical questions (6:1, 6:15, 7:7) and 7:24 are Paul's own voice.
- **Capitals**: *Fīlius* for the Son (1:3, 1:4, 1:9, 5:10, 8:3, 8:29, 8:32), *Pater* (1:7, 8:15, 15:6), 15:16 *per
  Sānctum … Spīritum*. Lower case, by reading: 7:6 *in novō spīritū* (spirit against letter), 8:10 *spīritus vīvus est*
  (the believer's spirit; the NRSV reads Spirit), 8:15 *spīritum servitūtis*, 14:4 *suō dominō* (the servant's master),
  1:25 *creātōrem*. Kept capital: 1:4 *Spīritum Sānctificum*, 2:29 *Spīritū*, 8:15 *Spīritum adoptiōnis*.
- **Paragraphs** moved to the sentence start (8:29 → 8:28, 8:36 → 8:35); added at 9:14, 9:19, 10:14, 11:28, 11:33;
  `m` after poetry where the sentence runs on.
- **Words no source marks**, decided from the Latin: *inadspectābilia* 1:20, *īnsitītiī* 6:5 (Gaffiot *īnsitīcius*),
  *perēmtī* 7:4, *patefactiōnem*, *congemīscere* 8:19–22, *laniōniīs* 8:36, *impāctōrium*, *illīsōriam* 9:33. Left
  unmarked: *pudefacit* 5:5, *peccantissimum* 7:13.
- **Uncertain, for your eye**: 1:17 *perpetuanda fidē* (nominative with *jūstitia*; the ablative is possible); 2:28
  *manifestō* (Gaffiot; your settled text is mixed); 5:14 *Ādamō* against your unmarked *Adam* in Genesis; 7:14
  *emancipātus* (1573 alone; stage 2); 11:12 *lāpsus* (singular, *sunt* with *dīvitiæ*); 12:8 *hilarē* (Gaffiot's
  adverb); 16:10 *Aristobōlī* (Castellio's o for ου; Gaffiot *Aristobūlus*).

## Questions for the whole edition (kept as found here)

- **16:27, the subscription** (*Scrīpta est Corinthī, missa per Phœbam, Cenchreēnsis ecclesiæ ministram.*): 1573 sets it
  in italics under the last verse, apart from the text; here it stays in 16:27 as Wikisource has it. Set it apart (USFM
  `\cls`, a letter's closing), keep it in the verse, or drop it? The other letters have the same.
- **Wikisource's early-line spellings** stay in Romans as in Acts, against your settled forms: *caussa* (Romans 11×,
  Acts 17×; your *causa* 30, *caussa* 2), *adsp-* / *adfe-* / *adfi-* / *adsec-* (your *aspiciō*, *affectiō*,
  *assequor*), *intellig-* (Romans 1, Acts 9; your *intelleg-* 43, with approved rules for single forms), *exst-* /
  *exsp-*. Rules for them would change Romans and Acts together: approve them as a set?
- ***Quinetiam*** (5:11, Wikisource one word) against *Quīn etiam* (8:23); ***perēmtī*** (7:4) against Gaffiot's and your
  *perēmpt-*; *īnsitītiī* (Gaffiot *-īcius*); *tamdiu* → *tam diū* (7:1, an approved rule); 11:26 *Jācōbæōs* (1573
  *Iacobeos*).
