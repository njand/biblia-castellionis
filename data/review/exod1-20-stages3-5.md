# Exodus 1–20: stages 1–5, one proposal per verse

Proposed 2026-11-08, **waiting for your approval**. Same tools and format as Genesis 28–50
(`data/review/gen28-50-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). The last of your earlier
Old Testament work (`TXT/3`); with Genesis it makes milestone M4.

## Where it stands

- **Stage 1**: `text/draft/EXO.usfm`, Wikisource's Exodus 1–20 with the BSB's paragraphs, renumbered to the KJV, 545
  verses, every chapter at the KJV count. Wikisource has every chapter, but had run 5, 6, 12 and 19 together with
  inline verse numbers; the parser now splits them (`pipeline/wikisource.py`). Castellio's numbering in 5–7 is not the
  KJV's: 18 edits in `data/versification/Exod.draft.edits.tsv`, including a new `opens` edit (his 5:25 is the KJV's
  6:1, so the chapter break moves back) and two mid-sentence chapter breaks (KJV 7:25 and 12:51, `\nb`). Details in
  the stage-2 file.
- **Stage 2**: `data/review/exod1-20-stage2.md`, **120 corrections** against the base, the 1738 Leipzig edition: 78
  Wikisource slips, 16 name forms (1738's *Aharon*, *Mosem*, *Moses* for Wikisource's *Aaron*, *Mosen*, *Moyses*),
  Castellio's *G.L.* … *H.* marks dropped at 2:22 and 6:20 (words kept, as Gen 44:6), 13 misspellings, and 11 found
  while reading the verses (6:3, where Wikisource took the arm of 1738's drop-cap *E* for a word *a*; 10:10 *satis
  perspicua est vestra malitia*; 9:20 *ex Pharaoniis Jovae minas*). Every one was read in 1738's hOCR line, five on
  the page image (`sources/archive/crops/exod-*.jpg`). **Applied to the draft** (decision 30's standing rule). Kept
  after checking: 18:12 *cumque* (page image), 2:2 (1738's *progeniem* is a footnote to 1:21).
- **Stages 3–5**: `data/review/exod1-20-ch01.md` … `-ch20.md`, 545 items, all checking `ok`; **waiting for your
  approval**. Preview: **`text/draft/EXO.preview.usfm`**. Quotation marks balance in the preview (`structure.quotes`:
  nothing open or unclosed; the two passages in ‘…’, 3:14 and 15:9, are quotations inside speech).
- **Your settled text**: five markings the Exodus readers found wrong there (Gen 8:5 *mēnsis*, 13:9 and Luke 21:23
  *regiō*, Gen 22:14 *ā Jōvā*, 24:8 *religiōne*), proposed in `data/review/settled-fixes-exod.md`, **not applied**.

## What changed in the tools

- **`wikisource.py`**: an inline verse number may skip one or two (flagged `gap`), and may be followed by a dot with no
  space (`2."Hic`). Re-parsed from the cached page (same revision): Exodus 773 → 885 rows, Joshua 555 → 651; no other
  book changes.
- **`versify.py`**: the `opens` edit; a split drops a leftover number with its dot (`8. Tum`). Test added.
- **`verses.py`**: a forms row may name one copy of a word (`Exod.18.8#2`) where a verse has it twice in different
  cases (*quibus Jōva modīs … ā Jōvā līberātī*; also 3:12 *hoc/hōc*, 7:16, 10:7 *Hīc/hic*, 12:39 *eā/ea*). The item
  label named every book *Mark* (Genesis's and John's files show *Mark 28:1*); it now shows the book.
- **`cli.py`**: `draft` creates `text/draft/` when it is missing.
- **Ligatures in the draft**: Wikisource writes *æ/œ* in 16 lines (chapter 3 mostly), which the macronizer cannot
  mark; set to *ae/oe* like the rest of the draft (the ligatures come back with the macrons).

## How the verses were made

- **Layout and macrons**: four readers (1–5, 6–10, 11–15, 16–20) under one brief, each checked by a script. Their
  calls are in `data/decisions/Exod.layout.tsv` (120 lines) and `Exod.forms.tsv` (692 rows, each with its reason). I
  read their reports, checked the suspected slips in 1738 (stage 2, section 5), re-keyed their rows to the corrected
  words, added the rows for words that occur twice, and fixed one line (16:8 lacked its opening mark).
- **Names** follow your settled forms (*Aharōn-*, *Jōva*, *Mōsēs*, *Pharaō*, *Sōchar*, *Gērsōn*, the Gen 46:9–11
  names). New names take their vowel lengths from the Hebrew (OSHB `wlc/Exod.xml`): *Pitōmam, Phūa, Sephōra, Jethrō,
  Hōrēbum, Lebnīm, Simeīm, Amrām-, Ozīēl-, Elīsebam, Ammīnādābī, Ēthāmō, Ahīrōtha, Magdōl, Baalsephōnis, Māra,
  Raphīdīm-, Sīnem* (Sin), *Sīnam* (Sinai). Uncertain lengths are left unmarked (*Charmis, Zechris, Sethris, Nephegus,
  Jacobedam*).

## Flagged (2,519 words)

| Kind | Words |
|---|---:|
| homograph, your settled forms agreeing (no WordPress for Exodus) | 1,611 |
| decided by reading the verse | 700 |
| lower case at a verse start | 77 |
| punctuation changed (verses) | 72 |
| your settled forms overrule the lexicon | 36 |
| case changed by a layout line | 20 |
| Gaffiot changed the stem | 3 |
| **unflagged**: the lexicon's one marking | 6,786 |

88 verses have their quotation marks, poetry or markers changed by a layout line; 14 have nothing flagged. The rates
were not re-measured for this run (Genesis: lexicon-only 0.23%).

**The settled-agreeing tier was wrong mostly in two ways**, and every word of it was read by the readers:
- ***Jōva* for the ablative *Jōvā*** (some 30 places: *ā Jōvā*, *prō Jōvā*, *jubente Jōvā*): your settled forms have
  *Jōva* 79 times as a nominative, so the tier chose it everywhere. I then read every remaining *Jōva* in the
  preview: all nominative or vocative.
- ***-a/-ā*** as in Genesis: ablatives after prepositions and in ablatives absolute (*ex eā terrā, Apertā cistā,
  sublātā virgā, tōtā nocte, magnā vī*) and, the other way, nominatives and neuter plurals (*vāsa aurea, mūtāta est,
  Eadem lēx, quæ via erat*).

## Calls worth a look

- **Poetry**: the Song of the Sea, 15:1–19, `\q1`/`\q2`, opened after *sīc cecinit:* and **closed at 15:19, not
  15:18**: in Castellio 15:18 *Rēgnet in omnem æternitātem Jōva,* runs on into the relative clause *quī in Pharaōnis
  equōs … ingressus, … perambulāverint* (1738 prints it so). The enemy's words, 15:9, in ‘…’. Miriam's refrain, 15:21,
  set like 15:1. The Decalogue, 20:2–17, one speech of God in prose, no `\qt`.
- **Reported speech left unmarked** where the BSB quotes (Castellio's accusative and infinitive or subjunctive), among
  others: Pharaoh's order 5:6–11; Moses' messages to Pharaoh in the plagues (8:1–5, 8:20–23, 9:1–5, 10:3–6); 12:43–49;
  16:4–7; 19:12–13; 20:18–19.
- **Speech boundaries**: 12:2–20 and 13:3–16 one speech each (Wikisource closed and reopened them); 9:13–19 with what
  Moses is to say in ‘…’; 14:3 opened at *ut Pharaō* (Wikisource opens at 14:4 *mē*); 16:15 *Mān hū? quid hoc?* kept
  together inside the quotation (*quid hoc* may be Castellio's gloss); 3:14 *‘Erō mittit mē ad vōs.’*
- **Indirect questions lose their ?**: 2:7, 2:13, 2:18, 2:20, 3:13 (1738 prints a ?), 10:3, 12:26, 13:14, 17:2–3.
- **Paragraphs moved** to the sentence start: 4:6 → 4:5, 10:21 → 10:20, 12:29 → 12:28.
- **Capitals**: *Domine* to God (4:10, 4:13, 5:22, 15:17); 7:1 *Pharaōnī deum efficiō* lower case (Moses as “a god”);
  *Ōrāculum* (the Testimony, 16:34) capitalized, *ōrāculum* (consulting God, 18:15) not; *Manna* as 1738.
- **Hebrew words**: *Mān hū* (16:15) and *gōmer*, *ēphī* (16:16–36) marked from the Hebrew.

## Questions for the whole edition (kept as found here)

- ***vesc-***: your settled forms have a short e (*vescendum, vescī*) where Gaffiot and the lexicon have *vēscor*; kept
  short (12:15, 18, 20, 43, 48). Likewise *īnfestus* (15:7) short where Gaffiot has *īnfēstus*.
- ***lōcusta*** marked long (10:4–19, Gaffiot and the lexicon) against your unmarked Matt 3:4 *locustæ*.
- ***nārr-*** (10:2) by your settled majority (14 *nārr-*, 4 *narr-*); Gaffiot *narrō*.
- ***Gomer*** (Gen 10:2) unmarked in your text, *gōmer* here; ***Amalechitārum*** (17:16, as Gen 14:7) unmarked against
  *Amālēchus*; *Ramesse/Ramessem*, *Sochotha*, *Sur*, *Jebusæōrum* unmarked as your Genesis, though the Hebrew has
  long vowels.
- **Spellings 1738 has otherwise**, left to the rules: *undecunque* (1738 *undecumque*), *ceremonia/cerimonia*
  (1738 *cærimonia*), *astaret* (*adstaret*), *asseclārum* (7:20) beside *adseclīs* (8:11).
- **6:3** *nōmen meum Jōva nōn dēclārāvī*: one reader saw 1738's OCR as *Iouam*; not confirmed on the page image, so
  the draft's *Jōva* stays.
