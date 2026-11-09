# Genesis 28–50: stages 1–5, one proposal per verse

> **Settled 2026-11-08** (decision 32): you approved it "for now"; every chapter accepted and applied, Genesis 28–50
> in `text/GEN.usfm`, the draft and preview removed. Nothing committed. Kept as the record for your later review.

Proposed 2026-11-08. Same tools and format as the Gospels (`data/review/mark6-16-stages3-5.md` explains the
format); the first Old Testament run.

## Where it stands

- **Stage 1**: `text/draft/GEN.usfm`, Wikisource's Genesis 28–50 with the BSB's paragraphs, renumbered to the KJV
  (six edits in `data/versification/Gen.draft.edits.tsv`; 41:57 recorded as absent: every printing ends chapter 41
  at 41:56). 757 verses.
- **Stage 2**: `data/review/gen28-50-stage2.md`, **61 corrections**, all against the base, the 1738 Leipzig
  edition: 33 from the collation (1738, 1750, your 1726–27 text), 8 misspellings no lexicon knows, and 20 found
  while reading the verses (e.g. 34:23 *Hōc pactō*, 35:8 *nūtrīx*, 41:55 *illīus*, 42:24 *ab illīs*, 43:25 *Illī*,
  50:16 *eum*). Most were read on the 1738 page image (`sources/archive/crops/`, leaf given); the rest in 1738's OCR
  with your 1726 text. **Applied to the draft** (decision 30's standing rule). Kept after checking: 33:2
  *utrāsque*, 33:19 *quessitis*, 37:35 *cumque pater dēplōrāns* (1738 prints *cumque*; 1750 and your 1726
  *eumque*).
  - **Castellio's *G.* … *H.* marks** at 44:6, printed in 1738: words from the Greek “until the return to the
    Hebrew” (his *Ad lectores admonitio*). Words kept and marks dropped, as in your settled Matt 19:4 and Luke
    11:7 (item 55; `docs/editions.md`).
  - **Your 1726 text shares Wikisource's slips** at 30:1, 32:10, 32:32, 34:23, 35:3, 35:8 and 35:23, so for
    Genesis it is not an independent witness there; 1738 decided those.
- **Stages 3–5**: `data/review/gen28-50-ch28.md` … `-ch50.md`, 758 items, all checking `ok`; **waiting for your
  approval**. Preview: **`text/draft/GEN.preview.usfm`**.
- **A slip in your settled Genesis**: 25:33 *Jūra mihi* → *Jūrā mihi* (imperative, as your 21:23),
  `data/review/settled-fixes-gen.md`, applied under the standing rule.

## What changed in the tools

- **The Old Testament route**: `collate` takes 1738 as the base for the Old Testament (1750, your `TXT/3`, and
  Wikisource as witnesses). `archive.py` finds a word in 1738's hOCR and crops its lines from archive.org's page
  image. `versify` has an `absent` edit for a KJV verse no printing has.
- **WordPress 2019 left Genesis 34 unmarked** (0 macrons in 522 words), so the “chosen” tier there had picked
  unmarked forms. `harness.wordpress_marks` now ignores a chapter where under 10% of words carry macrons. Chapter
  34's words fell back to the lexicon, your settled forms, or a flag, and the flags were decided by reading.
- **Diaeresis forms**: `macronize.choose` drops a lexicon candidate with a diaeresis (*Isrāël*) when another
  exists. It had produced *Isræl*.
- **Spelling rules added** (approved under the standing rule): *adiutus* → *adjutus*, *abiudicabitur* →
  *abjudicabitur* (consonant i is j), *quatuordecim* → *quattuordecim* (as the approved *quattuor*).

## How the verses were made

- **Layout and macrons**: four readers (28–33, 34–39, 40–44, 45–50) under one brief, each checked by a script.
  Their calls are in `data/decisions/Gen.layout.tsv` (221 lines) and `Gen.forms.tsv` (791 lines, each with its
  reason). I read their reports and changed or added these:
  - **Re-keyed after stage 2:** 13 macron rows that named Wikisource's misspellings (*pacō*, *nūtīx*,
    *propserābat* …), keyed now to the corrected words.
  - **Chapter 34**, flagged after the WordPress fix: the names (*Sichemus* with no long vowel, as 33:18; *Hemōr-*
    from Hebrew חֲמוֹר) and eight homographs (34:12 *modo*, 34:23 *omnia sua*, 34:31 *habita* …).
  - **Case endings** in the agreeing-homograph tier, which I swept for *-a/-ā*: 34:17 *puellā abductā*, 46:20 *ex
    Āsenathā … fīliā*, 47:14 *quæ … inventa est*, 49:15 *amœnitāte perfectā*. Also 35:6 *in Chananæā sitam*, 49:30
    *ēmit* (perfect), 36:40 and 36:43 *Ēsāō*, 28:20 *vescendum*, and 29:34 *alium* (not *ālium*, garlic).
- **Names** follow your settled forms (*Jācōbus*, *Labān*, *Ēsāus*, *Rūbēn*, *Ephrāim* as John 11:54). New names
  take their vowel lengths from the Hebrew (OSHB, `sources/parallel/oshb/…/wlc/Gen.xml`). Where the length is
  uncertain, the vowel is left unmarked.

## Flagged (12,242 words)

| Kind | Words |
|---|---:|
| homograph, your settled forms agreeing (no WordPress for 36–50) | 1,221 |
| decided by reading the verse | 803 |
| homograph, WordPress chose, your settled forms not agreeing | 168 |
| your settled forms overrule the lexicon | 159 |
| WordPress alone | 103 |
| case changed by a layout line | 94 |
| lower case at a verse start | 52 |
| a witness's marking (names) | 44 |
| punctuation changed (verses) | 41 |
| Gaffiot changed the stem | 7 |
| **unflagged**: lexicon's one marking 9,172; homographs WordPress and your settled forms agree on 565 | |

213 verses have their quotation marks or markers changed by a layout line, and 39 have nothing flagged.

**Measured error rates, without WordPress** (as for most of this run): lexicon-only 0.23%; homographs your
settled forms agree on 1.8%. That tier is the large one here (1,221) because WordPress stops at Genesis 35.
- **Its errors are almost all *-a/-ā* agreement**: ablatives after *in*, *cum*, *ex* and in ablative absolutes.
  The readers found 7 in 40–44 and my sweep found 4 more. All 177 *-a/-ā* words in the tier were read; the other
  1,044 were read by word and passed.

## Calls worth a look

- **Poetry**:
  - 48:15–16 and 48:20, Jacob's blessings, with the formula in ‘…’;
  - 49:2–27, Jacob's last words: `\q1` throughout, one speech opened at 49:1 and closed at 49:27.
- **Reported speech left unmarked** where the BSB quotes:
  - the steward's charge, 44:4–6;
  - what Joseph's brothers report, 43:3–7 and 44:19–29 (Jacob's words inside Judah's speech);
  - Joseph's message to Jacob, 45:9–11;
  - what is to be told to Pharaoh, 46:31–34;
  - God's promise, 48:3–4.
- **Indirect questions lose their ?**: 42:7, 43:7, 44:6, 47:3.
- **Paragraphs moved** to the sentence start: 41:46's to *Ita* in 41:45; 46:7's to *Veneruntque* in 46:6.
- **Capitals**:
  - *Terror Isaacī*, 31:42, and *per Isaacī patris suī Terrōrem*, 31:53 (a name of God);
  - *Sospitator*, 49:10 (Castellio reads Shiloh as a saviour, decision 20);
  - *ab Omnipotente*, 49:25;
  - *dominum*, 47:18, lower case (the Egyptians' title for Joseph).
- **Other calls**:
  - 41:43 *“Genua flectite.”* set as direct speech, although it follows *ut … prōclāmārētur*;
  - 48:7, where the speech closes before *id est, Bethlehemæ* (as the BSB);
  - 50:19 *īdem* (masculine with *ego*);
  - 37:25 *cætum* left as printed.
- **Inconsistent in your settled text**: *Rachel* unmarked (your Matt 2:18, the only place it occurs) but *Rāchēl-* in
  the other cases (Wiktionary; Gaffiot has *Rachel* unmarked). Kept as found; worth one decision for the whole
  edition.
