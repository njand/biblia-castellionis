# Acts 1–28: stages 1–5, one proposal per verse

Proposed 2026-11-09; **approved by Nathan "for now" on 2026-11-09 and settled** (decision 34). Same tools and format as the Gospels (`data/review/john5-21-stages3-5.md`;
`data/review/mark6-16-stages3-5.md` explains the format). Your earlier work on Acts 1–16 (`TXT/2 - Post-Corrected`,
the 1726–27 printing) served as a witness, not a base.

## Where it stands

- **Stage 1**: `text/draft/ACT.usfm`, Wikisource's Acts with the BSB's paragraphs: 1,007 verses, every chapter at the
  KJV count. 31 versification edits (`data/versification/Acts.draft.edits.tsv`, applied): at 14 places the boundary
  moves to where 1573 prints its verse number (which is the KJV's), 16:38–39 is split as 1573 numbers it, and 19:41,
  24:2–3 and 24:21–22 follow the KJV where 1573 does not.
- **Stage 2**: `data/review/acts1-28-stage2.md`, **225 corrections** against the base, the 1573 Basel edition, **read on
  the 1573 page images** (crops in `sources/mdz-1573/crops/Acts.*`; a handful from its OCR, marked so). Wikisource's
  Acts is Castellio's *early* wording, so most are his revision rather than typos: 77 Wikisource slips (section 1),
  124 readings of the revised text (section 2: *synagoga → collegium*, *templum → fanum*, *lavari → baptizari*,
  *baptismo lavit → baptismate baptizavit*, *homine natum → filium hominis*, *fortunare → felicitare*, *fidem habere
  → credere*, *ferta obmoverem → munera libarem* …), 4 word divisions (3), and 20 found later: six more *synagoga*
  places and two names (2a), eight slips found in reading (2b: 3:2 *ad fani portam*, *alvo*; 16:11 *solvimus* …) and
  four by the readers of 23–28 (2c: 27:13 *solvērunt, et propius*, 27:14 *procellōsus*, 24:1 *comparuērunt*). In all
  *synagoga* gives way to *collegium* 23 times. **Applied to the draft** (decision 30's standing rule). 1556's differing
  readings are recorded as variants (section 5 there). Kept after checking: 13:19 *dedit* (1573 misprints *dedi*),
  *Gāius* (1573 *Caius*), 17:4 *nec nōn*.
- **Stages 3–5**: `data/review/acts1-28-ch01.md` … `-ch28.md`, **1,007 items, all checking `ok`**; waiting for your
  approval. Preview: **`text/draft/ACT.preview.usfm`**. Quotation marks balance (`structure.quotes`: nothing open or
  unclosed, no chapter ending inside a quotation).
- **Your settled text**: four markings the Acts readers found wrong there (Gen 6:16 *contignātiōnē*, Gen 37:4 *amīce*,
  Luke 2:13 *repentē*, Matt 4:24 *Sȳriam*), proposed in `data/review/settled-fixes-acts.md`, **not applied**.

## What changed in the tools

- **`collate.py`**: your `TXT/2 - Post-Corrected` text (Acts) is a New Testament witness, `1726`.
- **`macronize.py`**: the j rule keeps the vowel i in the forms of *tenuis* (9:36 *tenuium*, which it had made
  *tenujum*) and in *Gāius* (three syllables, Gaffiot *Gāĭus*). Test added.
- **`verses.py`**: a layout line's `-` (no marker before the verse) was printed as a marker `\-`; it now removes the
  draft's `\p`, as CLAUDE.md describes. Test added.
- **Spelling rule added** (approved under the standing rule): *quicunque* → *quicumque* (2:21; your settled
  *quīcumque* 11×, *-cunque* 0×).

**Two blind spots of the collation**, worth knowing for the rest of the New Testament: it ignores a word added or lost
at a verse's edge (Wikisource adds *Et* at 9:2, 14:8, 16:13, 17:2, found by a separate sweep of verse starts and
ends), and it reads f and long s alike, so *sani/fani* (3:2) passes. A reader found the second; a sweep against your
hand-corrected 1726 text (Acts 1–11) found no other.

## How the verses were made

- **Layout and macrons**: seven readers (1–4, 5–7, 8–10, 11–14, 15–18, 19–22, 23–28) under one brief, each checked by
  a script (the words of every layout line against the draft; every form against its verse). Their calls are in
  `data/decisions/Acts.layout.tsv` (391 lines) and `Acts.forms.tsv` (1,111 rows, each with its reason). Every word the
  pipeline flagged as a homograph nothing chose, unknown, Gaffiot's stem or your settled forms has a row; the
  settled-agreeing tier (2,587 words) was read through for **-a/-ā** and the other case endings (*hīc/hic*, *hōc/hoc*,
  *-us/-ūs*, *vēnit/venit*) and given a row where wrong. A final sweep finds no *-a* left after *cum, ex,
  ā, ab, dē, prō, sine, præ*.
- **I then made the readers' choices agree across the book**: *Barnābās* (one form; Gaffiot *Barnāba*, the nominative
  in *-ās* as your *Jūdās*), *Saule* (unmarked as your *Saulus*), *nārr-* (your settled majority), *Syria* (Gaffiot short
  y), *Asiā*, *repente*, *Gāius*, *Eutychus* (Εὔτυχος), *Euro aquilō* (27:14), *Sabbatum* capital (as the Gospels and the
  rest of Acts), and lowered the capitals Wikisource's old verse starts left mid-sentence (11:30, 28:31; 16:7, 17:7 by
  the readers). 27:30 runs on into 27:31 with a comma, as 1573.
- **Names** follow your settled forms (*Jēsūs*, *Chrīstus*, *Mōsēs*, *Dāvīd*, *Abrāhāmus*, *Cæsarēa*, *Hierosolyma*,
  *Jōsēs*, *Zēlōta*); new names take their lengths from Gaffiot or the Greek (*Sapphīra*, *Theudās*, *Rhodē*, *Manahēn*,
  *Sōsthenēs*, *Apollōs*, *Lȳsiās*, *Drūsilla*, *Antiochīa*, *Adramyttīnus*); where nothing tells the length the vowel
  is unmarked (*Haceldama*, *Tabitha*, *Agabus*, *Elymas*, *Derbē*, *Antipatris*, *Molochus*, *Remphan*).

## Flagged (4,115 words)

| Kind | Words |
|---|---:|
| homograph, your settled forms agreeing (no WordPress for Acts) | 2,587 |
| decided by reading the verse | 1,116 |
| capital changed by a layout line (*Spīritus Sānctus*, speech openings, *Fīlius Hominis* …) | 323 |
| lower case at a verse start | 56 |
| punctuation changed (verses) | 27 |
| your settled forms overrule the lexicon | 5 |
| homograph (7:2 *Abrāhāmō*, your settled majority) | 1 |
| **unflagged**: the lexicon's one marking | 12,560 |

296 verses have their quotation marks, poetry or markers changed by a layout line; 27 have nothing flagged. The rates
were not re-measured for this run.

## Calls worth a look

- **Speeches**: Peter 2:14–36 and 3:12–26; Stephen 7:2–53 (each paragraph reopening with “); Paul 13:16–41, 17:22–31,
  20:18–35, 22:3–21, 24:10–21, 26:2–23; the letters 15:23–29 (closing *Valēte.*) and 23:26–30 in “…”. Voices inside
  them in ‘…’ (9:4 → 22:7 and 26:14 *Saule, Saule*; 11:7–9; 27:24).
- **Scripture**: in `\qt`, with ‘…’ inside a speech (as John 6:31). Set as **poetry** where the BSB does: Joel at
  2:17–21, Ps 16 at 2:25–28, Ps 110 at 2:34–35, Ps 2 at 4:25–26, Amos at 7:42–43 and 15:16–17, Isa 66 at 7:49–50, Isa 53
  at 8:32–33, Isa 6 at 28:26–27 (its *“Audiētis …”* as a third level). Kept as **prose** `\qt`: 1:20, 3:22–23, 4:11 (woven
  into Peter's sentence), 7:7, 7:32–34, 7:37, 13:22, 13:33–35, 13:41, 13:47 (the readers kept Paul's citations in 13
  alike; Ps 2:7 and Hab 1:5 could be poetry), 23:5. Not `\qt`: 7:26–28 (Moses and the Israelite, dialogue in Stephen's
  retelling), 17:23 *‘Ignōtō Deō.’* and 17:28 (Aratus) in ‘…’.
- **Reported speech left unmarked** where the BSB quotes: e.g. 2:13, 5:23, 5:25, 7:3, 7:6, 7:35, 7:40, 8:26, 9:38,
  11:13–14, 12:14–15, 14:22, 15:1, 15:5, 16:15, 17:6–7, 17:18, 19:21, 20:35, 23:19, 25:4, 26:31, 28:6.
- **Capitals**: *Spīritus Sānctus* both words (as your *Sānctō Spīritū*), also 5:9 *Dominī Spīritum*, 6:10 and 16:7;
  *Fīlius Hominis* 7:56; *Servātor* 5:31, 13:23 (*ductōrem* lower case); *rēx* lower case in Festus' and Paul's mouths;
  *deōs/deum* lower case for the pagan gods (14:11, 19:26, 28:6) and Rephan (7:43); 10:4 *domine* lower case (Cornelius
  to the angel); 22:14 *jūstum* (Christ) lower case, as decision 20 does not list it; 3:2 *Speciōsa* (the gate's name).
- **Paragraphs moved** to the sentence start: 14:8 → 14:7, 18:12 → 18:11; 9:20's BSB paragraph dropped (the sentence
  starts inside 9:19).
- **Words no source marks**, decided from the Latin: *mānsiōnātim* 2:46, *īnficiārī* 3:13, 4:16, *obēdierit* 3:23,
  *fēlīcitandās* 3:25. *manufactīs* (7:48) left as the lexicon has it.

## Questions for the whole edition (kept as found here)

- ***Jōannēs*** in Acts (Wikisource's *Joannes*) against your *Jōhannēs* in the Gospels: no approved rule joins them.
- ***cūst-*** long u in your settled forms (followed here); Gaffiot *custōs*.
- ***Saūlem*** (the king, 13:21) as proposed, against the apostle's unmarked *Saulus*.
- ***temptō***: *tentandum* (5:9) as your settled *tentand-* 7×, though brief.md prefers *temptō*.
- **28:26** a third level of quotation marks (“…” inside ‘…’ inside “…”), the BSB's reading of Isaiah's message.
