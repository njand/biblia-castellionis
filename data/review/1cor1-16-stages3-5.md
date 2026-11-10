# 1 Corinthians 1–16: stages 1–5, one proposal per verse

Proposed 2026-11-10; **approved by Nathan "for now" the same day and settled in `text/1CO.usfm`** (decision 36). Same tools and format as Romans
(`data/review/rom1-16-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier work
on 1 Corinthians; `TXT/1 - OCR` (the 1726–27 printing, uncorrected Google Books OCR) served as a witness, read as an OCR.

## Where it stands

- **Stage 1**: `text/draft/1CO.usfm`, Wikisource's 1 Corinthians with the BSB's paragraphs: 437 verses, every chapter
  at the KJV count after 7 versification edits (`data/versification/1Cor.draft.edits.tsv`, applied). **Chapter 3 lacks
  no words**: Wikisource and 1573 both have 22 verses there and both print the KJV's 3:23 (*vos autem Christi, et
  Christus Dei*) inside their 3:22, so it is a split, not a verse supplied from 1573. The other edits: 3:21–22 to where
  1573 prints 22 (*& Paulus*); 4:10–12 (both number the old way); 10:33 / 11:1 (both end chapter 10 with *Imitatores
  mei estote* and run chapter 11 one behind the KJV, printing the KJV's 11:34 as two verses). 1573 alone starts 13:5 at
  *charitas non aemulatur*; the KJV's division is kept.
- **Stage 2**: `data/review/1cor1-16-stage2.md`, **97 corrections** against the base, the 1573 Basel edition, **read on
  the 1573 page images** (crops in `sources/mdz-1573/crops/1Cor.*`; four from 1573's OCR, marked so): 58 Wikisource
  slips (12:25 replaced by half of 12:26; 10:17 a line dropped; 1:27 *stultitiam* for *stultissima*; 15:42–44
  *refurget* for *resurget*), 29 readings of the revised text (3:1, 4:10 *in Christo*; 5:5 *carnis*; 10:18 *carnem*;
  3:17 *sanctum*; 6:10 *paedicones*; 14:16 *locum*; 9:21 *lucrificarem*), 3 long-s slips found on a second pass (3:3
  *sit*, 15:19 *sumus*, 15:28 *sit*: 1573's OCR shares Wikisource's f, so the f/s check could not see them), 7 word
  divisions. **Applied to the draft** (decision 30's standing rule). 1556's differing readings are recorded as variants
  (3:1, 3:17, 5:5, 7:5, 8:10: changes made in 1573). Five spelling rules added (*emti, emtos, diremta, sumtum, sumtus* →
  *-mpt-*).
- **Stages 3–5**: `data/review/1cor1-16-ch01.md` … `-ch16.md`, **437 items, all checking `ok`**; waiting for your
  approval. Preview: **`text/draft/1CO.preview.usfm`**, identical byte for byte to what `review apply --all` writes on a
  copy of the draft. Quotation marks balance in every verse and across verses (`structure.quotes`: nothing open or
  unclosed, no chapter ending inside a quotation; no ‘…’ in the book). Ledger: chapters 1–16 at **in-review**.

## What changed in the tools

- **`versify.py`**: `opens` takes an anchor. The chapter break after the last verse moves back to those words inside it,
  which become verse 1 of the next chapter (1 Cor 10:33 → 11:1 *Imitatores mei estote*). Test added
  (`pipeline/tests/test_versify.py`, `OpensAtAnchor`). Tests: 106 pass.
- **f/s blind spot** (not yet in code): where 1573's OCR reads ſ as f in the same word as Wikisource, the collation sees
  agreement (3:3, 15:19, 15:28, 15:42–44). A sweep of every *f* word in the draft found them. Worth adding to
  `collate` as a check of Wikisource's *f* words whose s-form is also Latin (*fit/sit*, *fumus/sumus*), read on the image.

## How the verses were made

- **Layout and macrons**: five readers (1–4, 5–8, 9–11, 12–14, 15–16) under one brief adapted from Romans, each file
  checked by a script (layout words against the draft; every form against a word in its verse; every flagged word
  decided; quotation marks balanced). Their calls are in `data/decisions/1Cor.layout.tsv` (77 lines) and
  `1Cor.forms.tsv` (410 rows, each with its reason). Every word the pipeline flagged as a homograph nothing chose,
  unknown, Gaffiot's stem or your settled forms has a row. The settled-agreeing tier (1,134 words) was swept for
  **-a/-ā** and the other endings by the readers (rows where wrong: 2:3 *multā*, 3:22 *præsentia*, 6:16 *ūna carō*, 8:12
  *peccātis* (the verb), 8:13 *ēsus*, 12:15 *manus*, 14:8 *tuba*, 14:34 *disciplīna*, *pārēre*, 14:19 *mālō*, 15:42
  *Tālis*, 16:11 *bonā cum pāce*, 11:29 *comedit* (present, beside *bibit*)), then by me over the 119 *-a* words left: none
  wrong (*ūnā* adverb, *quā nocte*, *peregrīnā linguā*, *colloquia mala* …).
- **I then made the readers' choices agree across the book and with Romans and Acts**: *vēsc-* throughout (8:10
  *vēscendum*, as the other eleven forms and Romans 14; reader 2 had left it unmarked); 15:1 *ēvangelium* and 15:9
  *ecclēsiam* lower case (Wikisource's capitals; your settled text never capitalizes them mid-sentence); *Ādamus/Ādamum*
  as Romans' *Ādamō* (15:22, 15:45); *Sōsthenēs* (Acts *Sōsthenem*), *Crīspum* (Acts *Crīspus*), *Gāium*, *Apollōs*
  (Acts) with *Apollō* for the other cases (Ἀπολλῶ), *Cēphās*, *Achāiæ*, *Ephesī*, *Macedoniam*, *Tīmotheus*,
  *Prīscilla*, *Aquila*, *Isrāēlītās*, *Mōsis*, *Satanās/Satanæ*, *baptīz-* (all agree); 14:21 *inquit Dominus* after the
  quotation, outside it, as your Rom 12:19 (Rom 14:11 has *(inquit Dominus)* inside, a parenthesis in the line).
- **Names new to the edition**: *Achāicus* (Gaffiot), *Fortūnātus*, *Asiānæ*, *Galatiæ* (Gaffiot *Gălătĭa*);
  unmarked where nothing tells the length: *Stephanæ*, *Stephanam*, *Chloæ*.

## Flagged (1,636 words)

| Kind | Words |
|---|---:|
| homograph, your settled forms agreeing (no WordPress for 1 Corinthians) | 1,134 |
| decided by reading the verse | 439 |
| capital changed by a layout line (*Patre*, *Fīliī*, *Spīritus*, …) | 39 |
| lower case at a verse start | 20 |
| punctuation changed (verses) | 4 |
| **unflagged**: the lexicon's one marking | 4,798 |

56 verses have their quotation marks, poetry or markers changed by a layout line; 27 have nothing flagged. The rates
were not re-measured for this run.

## Calls worth a look

- **Scripture** in `\qt` with “…” (Paul's own letter is not in quotation marks). **Poetry** where the BSB sets it: 1:19
  (Isa 29:14), 2:9 (Isa 64:4, four lines), 14:21 (Isa 28:11–12), 15:32 (Isa 22:13), 15:55 (Hos 13:14, its own
  quotation: *illō scrīptō* introduces 15:54 only; Castellio's order, sting then victory, differs from the BSB's but
  breaks at the same place). **Prose** `\qt`: 1:31, 2:16 (no formula; *enim* inside, as Rom 2:24), 3:19, 6:16 (Gen 2:24,
  split round *inquit ille*), 9:9, 10:7, 10:26 and its repeat in 10:28 (Ps 24:1; the BSB lacks the repeat), 15:27, 15:54.
  **5:13** *auferte malōs dē mediō vestrum* (Deut 17:7) is in `\qt` without a formula, as the BSB: the least certain.
  **Left unmarked** because this Latin reports them (accusative and infinitive, decision 25): 3:20 (Ps 94:11), 15:45
  (Gen 2:7), 12:3, 14:25. **15:33** (Menander) in “…” without `\qt` (not Scripture).
- **Direct speech** in “…”: the slogans 1:12 and 3:4 (*Ego* capital), 6:12–13 (*Quidvīs mihi licet*; *Et dapēs ventrī …*,
  with *et hunc et illās abolēbit Deus* as Paul's answer), 10:23, 10:28 *“Hoc deastrīs immolātum est,”*, 12:21, 14:16
  *“Āmēn,”* (its full stop made a question mark), 15:35 the objector, the Lord's words at the Supper 11:24–25 (*Sūmite*).
  **Unmarked** where the Latin is reported: 7:1 *bonum esset hominī …* (Paul's judgment, subjunctive), 8:1 and 8:4
  (*scīmus, omnēs nōs … habēre*, *scīmus, nūllum esse …*), 9:10, 10:19, 15:12 (*quī fit ut quīdam … negent*).
- **Capitals** (decision 20): *Patre* 1:3, *Fīliī* 1:9, *Pater ille* 8:6; *Spīritus* capital 2:10–14 (*Deī Spīritus* 2:11
  against the draft's reversed capitals), 6:19, 7:40 *Deī Spīritum*, 12:4–13, 14:12 *dōnōrum Spīritūs* (the NRSV
  "spiritual gifts": the uncertain one). Lower case: 2:11 *hominis spīritus*, 2:12 *mundī spīritum*, 5:3–5, 6:17 *ūnus
  spīritus* (NRSV), 7:34, 12:10 *spīrituum*, 14:14 *spīritus meus*, 14:32 *vātum spīritūs*, 15:45 *spīritus vīvificus*
  (NRSV), 12:3 *dīvīnō adflātū* (as Acts), 2:14 *dīvīnī*, 15:58 *in rē dominicā*, 11:20 *dominicam* (adjectives).
- **Chapter 13** is prose in the BSB, so no poetry: its paragraphs at 13:4, 13:8, 13:11, 13:13 (more than Romans took
  from the BSB's `b m` breaks). **Paragraphs** also added or moved at 4:6, 4:18, 6:12, 7:8, 7:10, 7:12, 7:36, 7:39, 8:4,
  9:15, 10:6, 11:17 (moved from 11:18: *Hoc autem admonēns* opens the Supper section), 11:23, 11:27, 11:33, 14:20, 15:29,
  15:51, 16:12, 16:15, 16:21; `m` after poetry (1:20, 2:10, 14:22, 15:33, 15:56).
- **Words no source marks**, decided from the Latin: *īnfīdēns, īnfīdentēs, īnfīdentibus, īnfīdentium* (as your settled
  *īnfīdentiam*), *īnfermentātus* (Gaffiot), *præpūtiētur*, *perpetrātōrem*, *sacrificāta*, *portentificī*, *lucrificārem*,
  *laudātōrium*, *Irrītandusne*, *rādīve*, *Sōlīne*, *Ergōne*, *inhonestiōra*, *coītis*. Left unmarked: *contemptissimaque*,
  *abditissima*, *maranatha*.
- **Uncertain, for your eye**: 3:8 *idem sunt* (neuter, ἕν; masculine *īdem* possible); 2:8 *crucifīxissent* (your
  settled *crucifīx-*, Gaffiot *crucī-*); 4:12 *fausta* (object of *precāmur*); 14:7 *tībia … cithara* nominative, then
  *tībiā aut citharā* ablative; 15:36–37 *seris* (*sĕrō*, sow); 16:12 *Apollō*; 15:55 *orce* lower case (your *orcō* 3×,
  *orcum*; Matthew's *Orcī* once); 9:21 *lucrificārem* (1573 and 1556, beside *lucrifacerem* in 9:20, 22; *lucrifico* is
  late Latin); 7:34 *nupta*, 7:38 *nuptum* unmarked (Gaffiot *nŭptum*).
- **Kept as printed**: 7:8 *Cælibibus* (1573 *Cœlibibus*, as the draft), 12:2 *ac abdūcerēminī* (1573 *ac*), 11:34
  *Reliqua, quum vēnerō compōnam*, 9:2 ending in a question.
- **Your settled text**: the readers found no marks in it that look wrong, so there is no `settled-fixes-1cor.md`.

## Questions for the whole edition (kept as found here)

- **16:24, the subscription** (*Ad Corinthios prima scripta est Philippis, missa per Stephanam, et Fortunatum, et
  Achaicum, et Timotheum.*): 1573 sets it in italics apart, as after Romans; here it stays in the verse as Rom 16:27.
  `\cls`, in the verse, or dropped? (the same question as Romans).
- **vesc-**: *vēsc-* here and in Romans (Gaffiot *vēscor*), unmarked in Exodus and parts of your settled text: one rule
  for the edition?
- **The perfect of *obdormiō***: 11:30 *obdormīvērunt* and 15:6 *obdormiērunt* (Wikisource has both; 1573 *-iverunt* at
  15:6). Decision 19 sets the third plural by verb, with no evidence for this verb: which?
- **Adam**: *Ādamus* (Gaffiot, Romans, 1 Corinthians) against *Ādāmus* (your Genesis and Luke).
- **Early-line spellings** kept here as in Romans and Acts: *caussa*, *adloquor*, *adsequor*, *adficio*, *adfecto*,
  *intellig-*, *exsp-*, *quum* (your settled *quum* stands). The Romans question stands for all three books.
- **Paragraphs from the BSB's `b m` breaks** (chapter 13, 14:20): take them, or only its section headings, as Romans?
