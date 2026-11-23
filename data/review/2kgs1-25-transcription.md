# 2 Kings 1–25, phase 1: the transcription

*2026-11-22. Decision 85's phase 1 (PLAN.md §4), on Nathan's "Start transcribing the next book". Gate: the printed
text `text/orig/draft/2KI.usfm` approved → `text/orig/2KI.usfm`. The readers' own notes, with Claude's settlements at
their head: `2kgs1-25-transcription-readers.md`; their rows, the readers' and aligners' briefs and reports, `STATUS.md`
and the merge script: `2kgs1-25-readers/`.*

**Decision:** approved for now (Nathan, 2026-11-23: "Approve for now"); `text/orig/draft/2KI.usfm` moved to
`text/orig/2KI.usfm`, its title set to *Regum / Liber Posterior* (1 Kings' *Regum / Liber Prior*). Phase 2 next.

## For you

1. **Approve the printed text for now?** `text/orig/draft/2KI.usfm`: every word from the lines read on the page, on
   the KJV's numbering, 719 verse ids (the KJV's 719), 13,975 words, the same as the draft's verse for verse; 41
   paragraphs (each chapter's start and the readers' 16 indents, checked, below). Castellio's one *G. L. … H.* mark
   is printed as 1738 has it; the footnotes are not.
2. **The versification** (207 edits, `data/versification/2Kgs1-25.draft.edits.tsv`: 98 split, 103 merge, 6 chapter;
   applied to the draft and the printed text; decision 30's standing rule). Made by three aligners one after another
   (1–8, 9–17, 18–25; reports `2kgs1-25-readers/align-1.md` … `align-3.md`), each tested on both texts; the checks
   pass (the same words, the KJV's verse counts). Calls you may want to see:
   - **Six chapter breaks moved**, each where 1738's chapter opens with the end of the KJV's last verse before, as
     1 Kings 2/3:
     - 11/12: *Agebat Ioas annum septimum, quum regnum iniit,* = KJV 11:21; ch. 12 opens *videlicet anno septimo*.
     - 15/16: 1738's 16:1 (*Iothamo vita defuncto … Achazus eius filius,*) = KJV 15:38; ch. 16 opens *Iudææ regnum
       obtinuit*.
     - 20/21: *Postquam … Manasses eius filius,* = KJV 20:21; ch. 21 opens *annos tum natus*.
     - 21/22: *Amone … Iosias eius filius,* = KJV 21:26; ch. 22 opens *anno ætatis suæ octavo*.
     - 22/23: *Hæc res postquam relata regi est:* = KJV 22:20's end ("And they brought the king word again"); ch. 23
       opens *curauit ad se*. Not in the readers' lists; aligner 3's call.
     - 24/25: *Quum hic Sedecias contra regem Babyloniæ rebellasset,* = KJV 24:20's end ("that Zedekiah rebelled");
       ch. 25 opens *anno eius regni nono*. Also aligner 3's call.
     Each new chapter begins mid-sentence (`\nb` in the draft); the printed text opens the chapter's paragraph where the
     KJV's chapter now begins, as 1 Kings' and 2 Samuel's do. Phase 2's layout settles the edited text's.
   - **1738's own extra verses** (3, 6, 8 have one more than the KJV) are the second halves of KJV verses, merged.
     **Ch. 17** falls four behind from 13 (five of 1738's verses each hold two of the KJV's) and catches up by 40.
   - **The printer's margins moved to the KJV's starts** where they differ: 2:4 (*Tum Elias*, not *Quibus*), 4:26
     (*vt aduenienti*, not *eamque*), 10:29 (*quamquam*, not *videlicet*), 17:29 (KJV 31 at *Auani*).
   - Left as Castellio divides, one Latin sentence across two KJV verses with no clear place for the second: 2:2,
     8:28–29, 9:33–34, 11:2–3, 12:10–11, 12:20–21, 17:40, 22:3–4, 24:3–4, 24:10–11, 25:5–6; speech introductions
     ending a verse stay there.
   - One anchor corrected while building the printed text: 11:16 *Illi,iniectis*, printed with no space after the
     comma (the row's printed form had one).
3. Nothing else waits on you in phase 1. Phase 2 has the misprints, the footnotes and asterisks, the accents, and
   Castellio's mark.

## How the lines were read

- **Leaves**: 1738 (archive.org `bibliasacraexseb01cast`) leaves **429–460** (pp. 357–388). The book begins on leaf
  429 col. 0 under *REGVM LIBER IIII.* and ends on leaf 460 col. 1 (*diu vixit.*), above a woodcut and the catchword
  *PARA-*. Wikisource has no 2 Kings; 1750 was the only other voter. No leaf was photographed twice.
- **Voted** with `python -m pipeline lines 2Kgs 1-25 --leaves 429-460`: 3,086 lines; 0 doubts (one other witness).
- **Read** on the page by eleven readers, three leaves each (two for the last), one at a time (2026-11-22). The
  three aligners ran one after another; the rest was done here.
- **Result**: `data/witnesses/read-1738/2Kgs1-25.tsv`, 3,093 rows: 25 chapter rows, 10 lettered footnotes and 32
  signatures or catchwords as `%` rows. `2Kgs1-25.corrections.tsv`: 2,306 changed lines, 38 added, 31 removed
  (running heads, the last lines of chapter summaries, a page number). The vote's verse numbers were placed again
  from 1738's margins; the vote had *CAPVT XXIII* as `\c 21` (reader 10 corrected it).

## Checked by Claude on the page

Every place a reader asked about was looked at (the line with one either side, the column's full width with its
margin numerals). Three corrections, in `merge.py`'s `FIXES`; the readers' files stay as they read:
- **19:5 *Ezechiani*** (row 2292): printed so; reader 08 had normalized it to *Ezechiam*. (Taken here for a misprint; in phase 2 reader r7
  showed it is *Ezechīānī*, "Hezekiah's men", the subject of *retulerunt*.)
- **25:29 at *muta-*** (row 3082): the margin *29* stands beside a line that opens mid-word (*-tis eius carceris*),
  so the verse begins at the sense break on the line above, as the readers did at 5:20 and 7:19.
- **3:13 *conuocàuerit*** (row 253): a grave stands over the *a*, printed; kept like 1738's other accents (the settled
  printed texts keep them, decision 67).

Kept as read: the margin placements at 2:2, 2:4, 4:26, 5:20, 7:19, 10:28–29, 13:25, 17:19, 17:29, 20:19, 21:15,
25:28; and *cecidisses* (13:19), *Et* (11:17, lost in the gutter), *aram*, *eubitus* (25:17, misprint for *cubitus*),
*indîci* (8:1, circumflex printed), *eouites* (13:14, the *q* without its tail), *cepi.,* (13:15, the *t* not
printed), *quær eret* (4:13). Details at the head of `2kgs1-25-transcription-readers.md`.

## Paragraphs (checked 2026-11-22)

`orig --read-lines` took 40 paragraphs from the hOCR's indents; the readers list 41 (the 25 chapter openings and 16
indents, every column's left edge looked at). Every difference was seen on the page:
- **Two indents the hOCR missed**: 18:13 *Anno autem Ezechiæ* (after the short line *dienter fecerant.*) and 23:30
  *Eius in locum Ioachazus* (1738's 23:31, after *sepultus est.*; KJV 23:30's last clause, so the paragraph begins
  inside the verse).
- **One false**: 17:7 *Et quia Israelitæ* starts flush beside its margin *7*.
- Recorded in `data/decisions/2Kgs.orig.tsv` (¶ and ¶-), the printed text rebuilt: 41 paragraphs, the words
  unchanged. Tests pass (218).

## Footnotes and Castellio's marks (inputs for phase 2's notes)

- **10 lettered footnotes**, each a `%` row with its printed text, its letter taken out of the text row. 1738's
  letters run on from 1 Kings and restart: *d)* 2:12 *currus* (*columen atque præsidium.*), *e)* 3:14 *adpareo*
  (*administro.*), *f)* 4:13 *iussit illi* (Elisha speaks through his servant), *g)* 4:13 *inter suos se continere*,
  *b)* 9:11 *limphatus* (*insanus.*), *a)* 18:17 *apud aquæ ductum* (*scilicet extra vrbem.*), *b)* 19:3 *iam fetu*
  (the woman in labour), *c)* 19:24 *aggeribus* (*magna.*), *d)* 19:25 *hoc olim*, *e)* 21:13 (*sic Hierosolymam
  puniam, vt etc.*). Glosses all.
- **Castellio's mark**, printed in the text: *G. L. vt emas H.* at 5:26 (Elisha to Gehazi: the Greek and the Latin
  add "that you might buy").
- **Asterisks with no footnote**, taken out and listed in the readers' notes (1738's numbering): 3:7 (*Iosaphatum*),
  4:37, 6:25, 6:33, 20:13. As in 1 Kings, phase 2 checks them against Castellio's 1554 annotations *IN LIBROS REGVM*.

## Wording doubts (the printed text keeps 1738; the edition's choice is phase 2's)

- **19:13 *rex vrbis Sepharuaimi***: 1750 *rex ciuitatis*. **24:15–16 *fabrisque … omnibus denique***: 1750 *fabris
  … omnibusque denique*. 1738 clear on the page in both.
- Misprints kept: 1:1 *Moabi-/bitæ* (looked at: the syllable printed twice across the line end); 9:16 *decubabat* (1750 the same); 13:14 *eouites*; 13:15 *cepi.,*; 25:17
  *eubitus*. (19:5 *Ezechiani*, listed here at first, is no misprint but *Ezechīānī*, "Hezekiah's men", the subject:
  reader r7 in phase 2, `2kgs1-25-draft-fixes.md` §1.4; the printed text has it either way.) Lower-case names (*iezraelensi*, *israeliticis*, *assyrii*, *bethelensem*) as printed.
  Otherwise 1738 and 1750 differ mostly in spelling and stops (readers' notes, by row). The omission checks against
  the BSB found no clause lost in the reading; Castellio's condensing is his own.
