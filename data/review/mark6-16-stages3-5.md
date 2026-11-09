# Mark 6–16, stages 3–5: one proposal per verse

> **Done 2026-11-08** (decisions 28–29): every item accepted and applied, Mark 6–16 settled in `text/MRK.usfm`,
> `text/draft/MRK.usfm` and the preview removed. The review log at the end lists what changed on the way. Nothing
> committed. Kept as the record of the review.

Proposed 2026-11-07.

The draft (Wikisource, stage-2 corrections applied, BSB paragraphs) had no macrons and no quotation marks, so
nearly every word changes. Instead of one Apply line per change, **each verse is one item**, its Apply line
replacing the whole verse. The items are in eleven files, one per chapter:
`data/review/mark6-16-ch06.md` … `mark6-16-ch16.md` (486 items). Item numbers are verse numbers, so a
chapter's Decision line can name the verses you reject: `**Decision:** accept all except 14, 22`.

Each item shows the proposed verse with every stage applied:

- **Spelling**: the approved rules of `data/rules/orthography.tsv` (word and phrase rules, j/v; æ/œ follow the
  macrons). Listed under each verse, not flagged.
- **Macrons**: the harness's variant C (W/M with Gaffiot for stems, your settled forms, WordPress 2019 in
  context), except 22 words I decided by reading the verse (`data/decisions/Mark.forms.tsv`, each with its reason).
- **Layout**: quotation marks (decisions 4 and 25), `\qt` for quoted Scripture, poetry, paragraph moves, capitals
  for God (decision 20) and the punctuation a quotation needs. These are my readings, written over the draft's
  own words in `data/decisions/Mark.layout.tsv` (237 lines; the code refuses a line whose words differ from the
  draft's). Items with such a line are tagged `layout`.
- **Lower case** at the start of a verse that continues a sentence (Mark 4:2 *multa*, Matt 15:6 *nihil*).

## Applying

```
python -m pipeline review check data/review/mark6-16-ch*.md                          # 486 ok
python -m pipeline review apply data/review/mark6-16-ch06.md --write                 # after its Decision line
```

Rebuild the files and the preview (after editing a decisions file): `python -m pipeline propose Mark 6-16`
(`--rates` also measures the table below). Each verse is independent: rejecting one leaves it as in the draft,
for you to edit by hand.

## Decision 6: what goes unflagged

**Approved spelling rules, lexicon-only macrons, and homographs that WordPress 2019 chose and your settled
forms mark the same way go unflagged; everything else is flagged**, and the Gaffiot stem step always. The
homograph tier was added on 2026-11-08 (you agreed): measured, it is as safe as the lexicon's own marking (0.28%
against 0.26%).

## Flagged, by kind (7,281 words)

| Kind | Words | Shown as |
|---|---:|---|
| homograph, WordPress chose, settled silent or other | 267 | bold, with evidence |
| your settled forms overrule the lexicon | 75 | bold |
| lower case at a verse start | 45 | bold |
| case changed in a layout line (capitals for God, sentence starts) | 43 | bold |
| punctuation changed (each change shown in context) | 38 verses | flag line |
| unknown to the lexicon: WordPress's marks | 28 | bold |
| decided by reading the verse | 24 | bold, with the reason and what the pipeline had |
| lexicon's one marking, WordPress marks it otherwise | 18 | bold |
| Gaffiot changed the W/M stem | 11 | bold |
| **flagged words, all kinds** | **511** (+ 38 punctuation flags) | |
| unflagged: the lexicon's one marking | 5,488 | |
| unflagged: homographs WordPress and your settled forms agree on | 1,370 | |

379 of the 486 verses have a flag or a layout line (225 have a layout line); 107 have nothing flagged.

The 22 decided forms (`Mark.forms.tsv`): 8 homographs WordPress had chosen wrongly (*compārent → comparent*,
*lēctōrum → lectōrum* (couches), *Interne → Internē*, *prōfectum → profectum*, *terrā → terra*, *effugit →
effūgit*, *cōnspuēre → cōnspuere*, *magna vōce → magnā*); 4 Gaffiot stem errors (*Crucīfīge* ×2,
*crucīfīxērunt* ×2); 4 where the lexicon's one form was wrong (*Probe* as a name → *Probē*, *Abbā → Abba*,
*dēest → deest*, *Galīlæus → Galilæus* by your settled *Galil-*); 2 homographs nothing chose (*prīncipia*,
*hōra*); 3 unknown or WordPress-only words (*spiculātōrem*, Gaffiot; *Hērōdias*, Gaffiot *-ăs*;
*trānsjordānīnum*); *Hierichūnte* (W *Hierichûs*, your Luke 10:30).

## Measured error rates (settled chapters, `propose --rates`)

Macrons: each settled chapter marked from the others' settled forms (variant D), from your own spelling, and
compared with your marks. Spelling: the approved rules run on Wikisource's text of the settled chapters and
compared with your spelling (the j/v guard learns from the other books only).

| Kind | Measured on | Wrong | Flagged here? |
|---|---:|---:|---|
| **lexicon's one marking** (WordPress agreeing or silent) | 32,516 words | **0.26%** (84) | **no** |
| **homograph, WordPress and settled agree** | 7,456 | **0.28%** (21) | **no** |
| homograph, WordPress chose, settled not agreeing | 2,194 | 9.2% | yes |
| your settled forms overrule the lexicon | 664 | 4.8% | yes |
| WordPress alone (unknown to the lexicon) | 462 | 22.5% | yes |
| lexicon's one marking, WordPress otherwise | 228 | 38.2% | yes |
| homograph nothing chose | 77 | 28.6% | yes |
| Gaffiot changed the stem | 53 | 28.3% | yes |
| unknown | 32 | 53.1% | yes |
| **æ/œ from the macrons** | 1,716 words with æ/œ | **0.76%** (13: *Nōēma*, *coercendās*, *Abimælem* …) | **no** |
| **approved word rules** | 120 changes | **0%** | **no** |
| **j/v** | 14 changes | **1 wrong** (*iōta*, Greek) | **no** |
| lower case after , ; or a word | 387 | 9.3% | yes |
| lower case after a colon | 225 | 36.4% | not applied |

Caveats. The word rules were learned from these same chapters, so 0% is in-sample (Matthew 14–28, settled
after the rules, was reviewed with them). Phrase rules (word division) are not measured: a verse whose word
count changes is skipped. The quotation marks and layout cannot be measured this way: there is no automatic
answer key for direct versus reported speech, so every verse with them is tagged and the uncertain calls carry a
note. Expected unflagged errors in Mark 6–16 from these rates: about 14 lexicon-only macrons (0.26% of 5,487), 4
agreeing homographs (0.28% of 1,371) and one or two æ/œ. I read the flagged words, not the unflagged ones.

Two code fixes came out of the measuring: `macronize.ligatures` wrote no æ after a long vowel (*Marīae*, *Nōae*:
ligature errors 2.04% → 0.76%) and none in capitals (*JŪDAEŌRUM*).

## Layout calls worth a look

- **Reported speech left unmarked** (decision 4) where the BSB has quotation marks: 6:4, 14–16, 18, 24, 31;
  8:15–16, 23, 26; 9:11, 16, 26, 31; 11:3, 23; 13:6, 21; 14:2, 58 (inner), 69, 71–72; 15:35. Eleven indirect
  questions lose their ? (decision 25: 6:24, 9:21, 28, 33, 10:2, 11:3, 5, 12:28, 14:14, 15:2, 44).
- **Quoted Scripture** (`\qt`), following your Matthew parallels: 7:6–7 and 12:10–11, 12:36, 13:24–25, 14:27 as
  poetry; 7:10, 8:18, 10:6, 10:7–8, 10:19, 11:9, 11:17, 12:26, 12:29–31, 15:28 inline (8:18 and 10:6 by your choice,
  2026-11-08; your Matt 19:4 leaves Gen 1:27 unmarked). Not marked: 14:62 (as your Matt 26:64), 15:34 (as Matt
  27:46). Marked though the BSB has only one of them: 9:44, 46, 48 (Isa 66:24).
- **Paragraphs moved** where the BSB's fell mid-sentence: 12:13 → *Igitur* in 12:12, 12:38 → *Cumque* in 12:37,
  14:27 → 14:26.
- **Uncertain, kept as proposed** (you agreed 2026-11-08): 7:11 (*Corbān*: only the man's words in ‘…’), 7:19 (*expurgāns omnēs cibōs* inside the speech),
  8:28 (the accusative answer as speech, as your Luke 9:19), 11:31 (the deliberation ends before *Sīn*).

## Found in the settled chapters (proposed in `data/review/settled-fixes-matt.md`, 3 items, all check ok)

- **Matt 27:37** *JŪDæŌRUM*: a lower-case æ inside capitals (the ligature bug above).
- **Matt 20:29** *Hierichunte* without the macron your Luke 10:30 *Hierichūntem* has.
- **Matt 22:44** *Sēde ad meam dexteram*: the imperative of *sedeō* is *sedē* (Gaffiot *sĕdĕō*), as your Gen
  27:19 *sedē*; *sēde* is the ablative of *sēdēs* (right in Matt 23:2). Mark 12:36 is proposed as *sedē*.

## Not done

- No verse was read on a page image in this stage (wording was stage 2's); chapter summaries (decision 3) are
  still absent.
- The SBLGNT is unparsed, so no Greek was consulted; tense and case calls rest on the Latin syntax and the BSB.

## Review log, 2026-11-08

Nathan answered the open questions (decision 28) and accepted Mark 6 after reading it. He then delegated the rest:
"go through the remaining reviews very carefully, examining the evidence for each point. Apply your
recommendations (recording each change)". I read every verse of Mark 7–16 in full, with each flag's evidence, and
checked every word of Mark 6–16 against the spellings and markings of your settled chapters. Changes made, each
recorded where it lives:

- **Spelling rules added** to `data/rules/orthography.tsv` (approved, with notes): *quenquam → quemquam* (7:24,
  11:16, 12:14; your text *quemquam* 8×, *quenquam* 0×; republican prose 194:0), *sepe → saepe* (12:1, the
  hedge: Gaffiot's headword *sæpēs*), *Genezarethanum → Gennezarethanum* (6:53) and *Bethpage → Bethphage* (11:1),
  both as your settled Matthew and Luke.
- **Kept against your settled text**: 12:25 *cōnūbia* (Gaffiot *cōnūbĭum*; republican prose *cōnūbi-* 10, *connūbi-*
  0; your Gen 6:4 *cōnūbiīs*); your Matt 19:10 *connūbia* is the one proposed for change (below).
- **Code: long prefix before j** (`macronize.finish`): *ē-, dē-, prō-, trā-* in compounds of *jaciō* are long in your
  text 50 times of 50 (*ējicere*, *trājēcit*); the pipeline had stripped them with every vowel before *j* (right for
  *ejus*). Mark gains *ējicere* (11:15), *ējiciēbant*, *dējicī*, *trājicī* … The harness's vowels rose from 99.25% to
  99.49% (variant D) with this and the ligature fix.
- **Code: lower case at a verse start** now asks your settled text first: a word you write only with a capital is a
  name, though the lexicon knows a common word (*pīlātus*, armed with javelins): 15:4 keeps *Pīlātus*. Measured:
  9.3% wrong (was 10.2%).
- **Forms decided** (`data/decisions/Mark.forms.tsv`, 24 now): 10:1 *convenit* (present, with *docet*), 15:34
  *sabachtanī* (as your Matt 27:46).
- **Layout** as decision 28 (8:18 and 10:6 in `\qt` with ‘…’).
- **Matthew**: `data/review/settled-fixes-matt.md`, 4 items (Nathan's three, and Matt 19:10 *cōnūbia*), accepted.

Left as proposed after checking: the WordPress-only *Ēphāta* (7:34) and *Bēthsaidam* (6:45, 8:22; your text has
both *Bethsaida* and *Bēthsaida*): no other source marks them. The remaining flags were read and agree with their
evidence; every chapter is accepted whole.
