# Exodus 31–40, stages 1–2: 1738 read on the page, line by line (no Wikisource text)

Proposed 2026-11-14 (decision 68; plan `data/review/exod31-40-plan.md`; decision 30's standing rule), on the route
checked on Exodus 21–23 (`data/review/exod21-23-ocrcheck.md`). **Stages 3–5 (`python -m pipeline propose Exod
31-40`) come next and were not run.**

- **Base**: the 1738 Leipzig edition (decision 1), leaves 145–156 of its hOCR (archive.org bibliasacraexseb01cast;
  the archive.org image is one lower). Wikisource has no Exodus 31–40, so there is no transcription to correct:
  the text is 1738's own.
- **Stage 1** (`pipeline/ocrdraft.py`, `make_lines`): 1738's OCR line by line, without running heads, chapter
  headings, the italic chapter summaries (decision 67), catchwords, signature marks and footnotes; the margin
  numbers taken off the lines; each word repaired and voted with 1750 and the 1726 OCR (`TXT/1 - OCR`) →
  `data/witnesses/read-1738/Exod31-40.voted.tsv`.
- **Stage 2**: **every line read on the page images** (`ocrdraft.reading_sheets`: each line's crop under its text),
  words and punctuation as 1738 prints them (s for ſ, æ/œ, u/v and i/j as printed) →
  `data/witnesses/read-1738/Exod31-40.tsv`, every changed line in `Exod31-40.corrections.tsv`. Verse starts set
  where Castellio's margin numbers stand, with the KJV beside them.
- **The draft** (`python -m pipeline draft Exod 31-40 --from-ocr`, new): `text/draft/EXO.usfm`, the read lines
  joined into verses (hyphens joined) in Wikisource's conventions (u/v and i/j modernized by Wikisource's and the
  settled text's spellings of the same word, else by rule; æ/œ as ae/oe; spaces before punctuation, which are the
  OCR's, dropped), the BSB's paragraphs, the header of `text/EXO.usfm`. Exodus 1–30 (`text/EXO.usfm`) untouched.

## The numbers

| | |
|---|---:|
| printed lines read (leaves 145–156) | 1,053 |
| lines changed by the reading | 655 |
| words in the text | 4,715 |
| words changed by the reading (u/v, i/j, æ and case aside) | about 617 (13%) |
| verse starts (1738's numbering) | 329 |
| of them where stage 1 put them | 157 |
| set or moved by the reading | 172 |

Stage 1 found 180 verse starts by margin numbers (1738's and 1750's), 23 of them in the wrong place; the rest were
set by reading the margins on the images. Every chapter has its verses in order, 1 to the last, none missing:
31 (18), 32 (37), 33 (23), 34 (35), 35 (37), 36 (38), 37 (29), 38 (31), 39 (43), 40 (38).

**Chapter 40 after line 34 of leaf 156 (40:29–38)**, read in this pass: the leaf sets Exodus's last lines in both
columns above the title LEVITICVS. and Leviticus 1 below it; `ocrdraft.classify` now reads the columns above a
title across the page before those below it (the Leviticus heading had been sorted into the middle of Exodus 40).
22 of its 30 lines changed by the reading (40:31 *manus*, OCR *mantis*; 40:35 *eo penetrare non posset*, OCR one
word; 40:36 *quandocumque*; verse starts 30–38 by the margin numbers).

## A second look: slips of the first reading (6)

Words the lexicon did not know, and *f* words that are also words with *s*, were looked at again on the images:
six were slips of the first reading, now corrected in `Exod31-40.tsv` and its corrections file.

1. **34:6** leaf 148, line 107: *VA, IOVA DEVS MISERICORS* (the read line had *IOVA, IOVA*, the voted line's
   doubling of the *IO-|VA* broken over the line before). The draft reads *JOVA, JOVA DEUS*, not three.
2. **32:22** leaf 147, line 20: *quam sit peruersus* (read *fit*).
3. **32:19** leaf 147, line 8: *saltationesque* (read *faltationesque*).
4. **33:10** leaf 148, line 24: *adsur-|gebat* (read *adfur-*).
5. **35:13** leaf 150, line 57: *adposititio* (read *adpostitio*).
6. **39:41** leaf 155, line 58: *nistrandum* (read *niftrandum*).

Exodus 21–23 measured the first reading's misses at about 1 in 700 words; these six in 4,715 are about the same,
but they were found only by these two sweeps (unknown words, f/s), so others of a kind the sweeps cannot see (a
wrong known word) may remain. A second reading was done (next section).

## The second reading (2026-11-14, Nathan: "Yes, do the second reading of 31–40")

Two readers compared every read line (1,053, rows 3–1064 of `Exod31-40.tsv`) with its printed line, letter by letter,
on sheets of 14 lines (`ocrdraft.reading_sheets`): **14 lines changed**, applied to `Exod31-40.tsv` and logged at the
end of `Exod31-40.corrections.tsv`; the draft rebuilt (`draft Exod 31-40 --from-ocr`) and versified again.

- **Words (3)**, all as printed (decision 58): 1738's misprints **33:1** (1738's numbering) *lactc* (leaf 147; no crossbar on the last
  letter, against the *e* of *et*, *melle*: the reader less sure, worth your look) and **33:8** *tabernaeulum* (leaf
  148), and **39:4** (row 851) *quæ*, printed with the ligature (read *quae*). The reading edition's *lacte*,
  *tabernaculum* are for stage 3.
- **Verse numbers in chapter 32 (11 rows + 5 found by 1750)**: 1738's margin numbers on leaf 147 run one higher
  than the first reading's from *Hic Iosua* (18) to *in porta* (27), and there is no number at *Quumque ad eum*
  (the first reading's 27). The extra verse is on leaf 146's right column, whose margin numbers the gutter cuts off;
  **1750, which reprints 1738 line for line, numbers 13 at *Comprime istius iracundiæ*** (its OCR,
  `sources/archive/1750/text.txt` line 12871, then 14 *Memento*, 15 *Tum Ioua*, 16 *At Moses*, 17 *Opus*, 18 *Hic
  Iosua*). Set so: 1738's 32:13 is *Comprime … remitte*, its 14–27 one higher than read before.
- Seen and left: footnote letters in the text (left out, as decision 50), specks that might be accents (1738 prints
  none), the margin numbers of sheets 53–54 cut off at the crop's edge (checked by sense).

## Readings where 1738 differs from another printing (1)

- **36:25** *totitemque et eodem modo ad alterum latus* (KJV 36:25 “And for the other side … he made twenty
  boards”): 1738 prints ***totitemque*** (leaf 152, line 11, seen on the image), a misprint for *totidemque*; 1750
  reads *totidemque* (its OCR, `sources/archive/1750/text.txt` line 13588: *dines: totidemque et eodem/mo-*). The
  read lines and the draft keep 1738's misprint (decision 58 for the printed text); the reading edition's
  *totidemque* is for stage 3 to propose.

The collation (`python -m pipeline collate Exod 31-40`, `data/calibration/Exod31-40-collation.tsv`; 1738 base, 1750;
your `TXT/3 - Edited` text stops at Exodus 20, and Wikisource has nothing) found no other place where 1738's OCR and
1750 agree against the draft: its 9 “correct” places are words the OCRs break over a line (*pu rum*, *tuni cis*)
and OCR noise (38:15 *indu et is*). The 1726 OCR was used only in the voting; its interleaved columns were not
collated.

## Versification (decision 5)

1738's numbers are not the KJV's in chapters 32 and 35 (37 verses each, KJV 35). 6 edits in
`data/versification/Exod31-40.draft.edits.tsv` (redone after the second reading), applied (`versify` on the draft; the checks passed: same words,
every chapter at the KJV count, 325 verses). The 14 edits for 21–30 are kept as `Exod21-30.draft.edits.tsv` (as
those for 1–20 are `Exod1-20.draft.edits.tsv`).

- **32:12–13** (after the second reading): 1738's 32:13 *Comprime istius iracundiae saevitiam, et poenam populo tuo
  remitte* ends the KJV's 32:12 (“Turn from thy fierce wrath, and repent of this evil”); merged.
- **32:26–27**: 1738's 32:27 (*in porta castrorum adstitit … Quumque ad eum convenissent omnes Levitae, sic
  loquitur:*) is the KJV's 32:26 and the start of its 32:27 (“And he said unto them”); split at *sic loquitur*, and
  1738's 32:28 (*jubet Jova Deus Israelitarum …*) joined to it as the KJV's 32:27.
- **32:34**: the KJV's 32:34 (“Therefore now go … nevertheless in the day when I visit I will visit their sin upon
  them”) is 1738's 32:35–36 (*Quare perge … angelo.* + *Quum meae ultionis dies venerit … vindicabo.*); merged. 1738's
  32:37 is the KJV's 32:35.
- **35:35**: the KJV's 35:35 (“Them hath he filled with wisdom of heart, to work all manner of work …”) is 1738's
  35:35–37 (*et eos singulari animi peritia ornavisset:* + *cujus ope fabrilia …* + *hyacinthumque … perficerent
  industria.*); two merges.

1738's margin numbers seen on the images: 32:18–28, 35, 36 and 37 (leaf 147) and 35:34–37 (leaf 151); 32:13 by
1750 (above).

**Left as 1738 numbers them, the count agreeing (as 26:20–21 in 21–30)**, seen on the images:

- **35:4–5**: the KJV's 35:5 begins inside 1738's 35:4 (*Hoc insuper iubet Ioua … honorarium conficiatis* is
  “Take ye from among you an offering unto the LORD”); 1738's 35:5 is only *videlicet aurum, argentum, aes*.
- **36:25–34** (leaf 152, every margin number seen): Castellio cuts the boards and bars otherwise. His 25 (*totidemque
  … in parte aquilonari*) is the KJV's 25–26, his 26 (*sex asseres … et duos in angularibus*) its 27–28, his 27 its
  29, his 28–29 (*Ita octo asseres erant, et eorum spirae … binae*) its 30, his 30–31 (*utrique lateri quina,
  totidemque parti occidentali*) its 31–32, his 32 its 33, his 33–34 its 34. The KJV's 25/26 and 27/28 have no
  boundary in his words to split at.
- **38:13–18** (leaf 153, every margin number seen): his 13 (*in orientali parte quinquaginta cubitorum vela in
  utroque portae atrii latere … totidem basibus*) is the KJV's 13–15, his 14 its 16, his 15–16 its 17, his 17–18
  its 18.

**Question:** keep 36:25–34 and 38:13–18 as Castellio numbers them (the counts agree), or move them toward the
KJV's (38:13 split at *in utroque portae*, 38:16 and 38:18 merged, the KJV's 38:15 recorded `absent`; 36 has no
split point for the KJV's 26 and 28)?

## Notes for stages 3–5

- **34:6–7** is printed in capitals (*IOVA, IOVA DEVS MISERICORS … PERSEQVITVR*, leaves 148–149); the draft keeps
  the capitals (*JOVA, JOVA DEUS MISERICORS*), as Wikisource keeps *SANCTUS* or *JESUS*. How the edition sets them
  is stage 5's.
- **40:33**: 1738 indents *Postquam negotium Moses confecit* (leaf 156, column 1, line 47), a paragraph inside the
  verse; Castellio's 34 begins at *nubes* in the same sentence.
- 1738's spellings the approved rules or stage 3 will settle, as in 21–30: *adpellans, adscendat, adsurgebat,
  exspectabant, caussa, quatuor, septemtrionali, solerti, Israelitae* and the like are 1738's forms, kept.
- Wikisource's u/v convention was reached for words neither Wikisource nor the settled text has by rule (initial
  and intervocalic u, u after a prefix or in *serv-*, *solv-* …); stage 3 checks every word anyway.

## Stage 2b (the printed text)

`python -m pipeline orig Exod 31-40` was **not run**: `orig.build` aligns 1738's OCR to settled chapters
(`text/EXO.usfm`), and 31–40 are not settled. Here the read lines **are** the printed text (every word read on the
image, as printed), so stage 2b needs no OCR alignment, only: the read lines joined into verses as printed
(`ocrdraft.verses_of`, hyphens joined, s for ſ), moved to the KJV's numbering by the same 6 edits (the split at
*sic loquitur* included), with 1738's paragraphs from its indents (not read yet, as for Genesis and Exodus 1–20), and
written to `text/orig/draft/EXO.usfm` beside 1–30 (`orig.merge_usfm`). That needs a small function (an `orig`
route from read lines, or `ocrdraft` writing the orig USFM); not written here, since `pipeline/orig.py` is being
edited in another session.
