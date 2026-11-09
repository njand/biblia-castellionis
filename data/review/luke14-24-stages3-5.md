# Luke 14–24: stages 1–5, one proposal per verse

> **Settled 2026-11-08** (decision 30): you approved it "for now"; every chapter accepted and applied, Luke 14–24 in
> `text/LUK.usfm`, the draft and preview removed. Nothing committed. Kept as the record for your later review.

Proposed 2026-11-08. Read with `data/review/mark6-16-stages3-5.md`, which
explains the format; this run used the same tools, with the fixes made during the Mark review.

## Where it stands

- **Stage 1**: `text/draft/LUK.usfm`, Wikisource's Luke 14–24 with the BSB's paragraphs: 491 verses, every
  chapter at the KJV count.
- **Stage 2**: `data/review/luke14-24-stage2.md`, 17 Wikisource slips, **every one read on the 1573 page image**
  (14:3 *lēgis perītōs*, 14:28 *an*, 14:31 *sē cum*, 16:1 *dispēnsātōrem*, 16:17 *intercidere*, 17:8 *cēnem*, 19:8
  *facultātum*, 21:20 *tum*, 22:12 *vōbīs*, 22:19 *dedit*, 23:19 *cædem*, 24:41 *edūliī* …). **Applied to the draft**
  (2026-11-08, under your delegation, because stages 3–5 are written over its words); each item can still be
  reverted by hand. Recorded, not proposed: 15:20 1573 *insiliit* for *insiluit*.
- **Stages 3–5**: `data/review/luke14-24-ch14.md` … `-ch24.md`, 491 items, one per verse, all checking `ok`;
  **waiting for your Decision lines** (`accept all except 14, 22`; item numbers are verse numbers). Preview of
  everything accepted: **`text/draft/LUK.preview.usfm`**.

## How the verses were made

- **Spelling**: the approved rules (with the four added for Mark).
- **Macrons**: the pipeline, then every flagged word read in context; 29 corrected in
  `data/decisions/Luke.forms.tsv`, each with its reason (e.g. 19:3 *præ hominum turbā*, 21:27 *atque glōriā*,
  23:47 *Eā rē vīsā*, 20:14 and 23:38 *Hic est*, 23:42 *vēneris*, 22:34 *nōtum*, 24:22 *māne*, 18:42 *Cerne*
  (not the name *Cernē*), 18:7 *quirītantēs*, the Gaffiot stem bug in *crucifīgerētur*, *crucifīgī*). Every word
  was also checked against your settled spellings and markings: no spelling differs; the 9 markings that differ
  are context calls (*manē* the imperative, *ūniversā multitūdine* …).
- **Layout**: `data/decisions/Luke.layout.tsv`, 252 lines: quotation marks (decisions 4, 25), `\qt` and poetry
  after your Matthew and Mark parallels, capitals for God (decision 20). Placed in three parts by separate agents
  under one brief, then read through by me and checked by the quotation checker (no imbalance).

## Flagged (7,045 words)

| Kind | Words |
|---|---:|
| homograph, WordPress chose, your settled forms not agreeing | 297 |
| your settled forms overrule the lexicon | 50 |
| lower case at a verse start | 49 |
| case changed by a layout line (capitals for God, speech openings) | 41 |
| decided by reading the verse | 30 |
| WordPress alone (unknown to the lexicon) | 13 |
| lexicon's one marking, WordPress otherwise | 13 |
| Gaffiot changed the stem | 10 |
| punctuation changed (verses) | 23 |
| **unflagged**: lexicon's one marking 5,390; homographs WordPress and your settled forms agree on 1,242 | |

238 verses have a layout line; 97 have nothing flagged.

## Measured rates (settled chapters, now with Mark 6–16; `propose --rates`)

| Kind | Measured on | Wrong | Flagged? |
|---|---:|---:|---|
| lexicon's one marking | 38,005 words | **0.09%** | no |
| homographs, WordPress and settled agreeing | 8,958 | **0.25%** | no |
| æ/œ from the macrons | 1,978 | **0.66%** | no |
| approved word rules | 135 changes | **0%** | no |
| j/v | 14 | 1 (*iōta*) | no |
| homograph, WordPress chose, settled not agreeing | 2,337 | 8.9% | yes |
| your settled forms overrule | 774 | 4.3% | yes |
| lower case after , ; or a word | 435 | 9.2% | yes |

The lexicon rate fell from 0.26% with the prefix-before-*j* fix. Mark 6–16, now in the measure, was itself made by
this pipeline, which flatters these numbers somewhat.

## Calls worth a look

- **Reported speech left unmarked** where the BSB quotes: 14:3, 9, 17, 30; 15:2, 6, 9; 17:4, 6, 7, 10, 23; 19:9–10,
  13–15, 31; 21:8 (*et quidem tempus īnstat*, read as Jesus' own clause); 23:29; 24:7, 44.
- **Indirect questions lose their ?** (decision 25): 15:26, 18:36, 22:11, 22:64, 22:67, 24:20.
- **Quoted Scripture**: 18:20 (commandments, as Mark 10:19), 19:38 (Ps 118:26 inline, as Matt 21:9), 19:46 (as
  Mark 11:17), 20:17 (Ps 118:22 as poetry), 20:42–43 (Ps 110:1 as poetry), 22:37 (Isa 53:12), 23:30 (Hos 10:8,
  inline). Not marked: 20:37 (Castellio reports Exod 3:6 in the accusative), 21:27, 22:69, 23:46 (as your
  parallels).
- **Nesting**: the prodigal son's rehearsed words (15:18–19) are a third level, “…” inside his ‘…’ inside Jesus'
  “…”. The quotation checker reset that level at every verse and called it unbalanced; fixed
  (`structure.quotes` now carries it across verses; three old false alarms in Luke 12 went with it).
- **Capitals**: 23:38 *HIC EST JŪDÆŌRUM RĒX* as your Matt 27:37; 23:37 *rēx* lowered (a mocking title).
- 18:42 and 19:26 keep Castellio's colon after *inquit*, as your Luke 12:18.

## Not done

- Chapter summaries (decision 3) are still absent, as in every book.
- No Greek was consulted (the SBLGNT is unparsed); tense and case calls rest on the Latin and the BSB.
