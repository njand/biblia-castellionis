# The New Testament as printed (1573), with Castellio's accents: new drafts for approval

Built 2026-11-14 (decision 67, route 1: `data/review/accents-1573.md`). The approved printed text
(`text/orig/<book>.usfm`, decision 61) is never rewritten by code, so each book has a new draft beside it,
`text/orig/draft/<book>.usfm`, built with `python -m pipeline orig BOOK CH --force`, with its own review file
`data/review/<book><chapters>-orig-draft.md`. On your approval the drafts replace the approved files.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); the 27 drafts moved to `text/orig/<book>.usfm`

## What changed against the approved text

Compared word for word, all 27 books:

- **3,148 accents added**: every word of an accent-prone type (127 types) the OCR read without an accent was read on
  the page images (3,480 words, 232 contact sheets, five readers), with a 5% sample of the words the OCR read with
  one. **Every accent the OCR had read was confirmed**; 835 the OCR had missed were found (*cùm*, *quòd*, *verò*,
  *quàm*, *eò*, *vestrûm*, *hîc* …), each a row in `data/decisions/<book>.orig.tsv`. The rest come from the OCR
  itself, which keeps 1573's grave and circumflex now (`orig.tidy`); an acute in the OCR is its reading of a nasal
  bar and is not an accent. Two capitals *À* the draft had are printed plain (1 Cor 14:36, 2 Cor 11:24).
- **21 capitals and word divisions** read on the page: drop-capital openings as printed (*CVm*, *MAnè*, *POst*,
  *PRIMVM*, *QVod*), and words printed as one (*plusquam*, *Veruntamen*, *eousque*, *maledixerit*, *malefacere*;
  decision 58).
- **About 30 others, each looked at on the page:**
  - **The ; of the -q; abbreviation** left after *-que* (*reuersusque;*, *idque;* … 18 places) is gone.
  - **The approved text was wrong, the draft right** (1573 seen): Matt 12:12 *Sabbathis*, 2 Cor 1:1 and 2 Thess
    1:1 *Thimotheus*, 2 Cor 4:1, 16 *defethiscimur*, Gal 6:9 *defethisci*, Heb 11:32 *Sampsone*, 1 Cor 9:27 *ne forté
    cùm* (no comma), Luke 22:35, Rom 15:13, 1 Cor 7:29 *Cæterùm* (ę).
  - **Read on the page and set by a row**: Luke 11:28 *Imò inquit* (approved *Imo,*), Rom 3:31 *imò*, Acts 21:37
    *Græcè? inquit* (the OCR read the ? as s), Heb 13:17 *vt id cum* (a parenthesis the OCR misplaced), 1 Thess
    5:18 *nam ea est* (the OCR joined the superscript note letter: *aea*), Heb 11:29 *quoſt* (1573's misprint), Rev
    6:1 *quum*. A row can now give the marks after its word (`Græcè|?`, `id|`; `orig.READ_AFTER`).

## Seven slips of the settled text

The accent reading found seven places where 1573 (and 1556) print another word than the settled text, which the
approved printed text carries too: `data/review/nt-readings-1573-1556.md` (Luke 20:21 *hī*, John 9:27 *quid*, 14:16
*vērē*, 16:30 *profectum*, Acts 11:16 *quō*, 14:23 without *cum suffrāgiīs*, 1 Cor 1:16 *Cēterōrum*). Once decided,
the printed drafts follow.

## The words the OCR did not read: now read on the page (2026-11-15)

The OCR route had filled 1,655 words with the settled word (kinds *guess* 415, *misread* 147, *none* 1,048, *doubt*
14, *prone* 31). All were read on 1573's page images (166 contact sheets, five readers; the doubtful ones zoomed at
full resolution) and are rows in `data/decisions/<book>.orig.tsv`; the drafts were rebuilt (260 changes):

- **1,612 the draft's word**, 127 of them spelt, accented or capitalized otherwise (*Bartholemæus*, *redijssent*,
  *defethiscantur*, *obthurato*, *authores*, *vænire*, *paterfamiliâs*, *arduúmque* and *Númnam* with an acute,
  *Possumus'ne* with its mark before *-ne*, *SYLVAnus*, *ENVMERATIO*, misprints as printed: *Impertice*,
  *atrogantes*, *derurbamus*, *imumbrabit*, *celebrẽ*), and about 70 with other punctuation after them.
- **37 another word, missing or joined**: the six slips above found again, thirteen more slips proposed in
  `data/review/nt-readings-unread.md`, seven where 1573 differs and the settled word stays (listed there), and word
  divisions (*crucifixissent*, *crucifigite*, *crucifigam*, *crucifigant*, *econtrariò*, *An non*, *sibimetipsi*,
  *operæprecium*). The printed drafts have 1573's word in all of them.
- **Acts 8:23**, where 1573 prints another sentence, follows since item 9 of `nt-readings-unread.md` was accepted
  (*imminere* read on the page, the OCR's *inminere*).

**Decided 2026-11-15:** `nt-readings-1573-1556.md` accepted except item 3 (John 14:16 keeps *vērō*; the printed text
keeps 1573's *verè*), `nt-readings-unread.md` accepted whole; applied to `text/`, the gold rebuilt, the rows in
`data/decisions/<book>.orig.tsv` re-keyed to the new settled words, and the seven books' drafts rebuilt (Matt, Mark,
Luke, John, Acts, Rom, 1 Cor; the only printed change Acts 8:23). Every NT draft now has 1573's word wherever it
was read. **Recommended now:** approve the drafts.
