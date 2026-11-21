# 1 Samuel 1–31, phase 1: the transcription

*2026-11-20. Decision 85's phase 1 (PLAN.md §4), on Nathan's "Start transcribing the next book". Gate: the printed text
`text/orig/draft/1SA.usfm` approved → `text/orig/1SA.usfm`. The readers' own notes: `1sam1-31-transcription-readers.md`.*

**Decision:** approved for now (Nathan, 2026-11-20: "Approve for now"); moved to `text/orig/1SA.usfm`, never
rewritten by code. Phase 2 next.

## For you

1. **Approve the printed text for now?** `text/orig/draft/1SA.usfm`: every word from the lines read on the page, 809
   verses on the KJV's numbering (the KJV's 810 less 13:23, below), 15,617 words, the same count as the draft's verse
   for verse; 87 paragraphs (each chapter's start, the 55 indents read on the page, and 1738's chapter 2 opening inside
   the KJV's 2:1). Castellio's *G. … H.* and *L. … H.* marks are printed in it as 1738 has them; the footnotes are not.
2. **The versification** (318 edits, `data/versification/1Sam1-31.draft.edits.tsv`, applied to the draft and the
   printed text): one `absent` and one `opens` among them (below). The calls are each noted with the KJV words that
   place them; the main judgments are listed under "Versification".
3. Nothing else waits on you in phase 1. Phase 2 has the wording doubts, the footnotes and asterisks, and Castellio's
   marks to settle (below).

## How the lines were read

- **Leaves**: 1738 (archive.org `bibliasacraexseb01cast`) leaves **322–357**, found with `lines --heads`. The book
  begins at the head of leaf 322 (*REGVM LIBER I.*) and ends on leaf 357 above *REGVM LIBER II.*
- **Voted** with `python -m pipeline lines 1Sam 1-31 --leaves 322-357`: 3,376 lines; words from 1738's OCR 14,204,
  1750 418, Wikisource 195, 1726 1, unknown 722; 241 doubts (`1Sam1-31.doubts.tsv`). **Fixes to `pipeline/ocrdraft.py`**
  were needed first, since the vote at first lost chapter 1 and seven chapter headings:
  - the heading's numeral, whose last I the OCR reads as L or 1 (*CAPVT L* for I, *XIL*, *XI1IL*, *XVIIL*, *XXL*,
    *XXIL*), is now read in sequence (`chapter_number`: the next chapter where the misreading accounts for it; a real
    *CAPVT L.*, Genesis 50, stays 50);
  - a heading read with specks (*~~ i Ca Tp VT _ XXIII.-*, chapter 23) is found (`CHAPTER_SPECKED`);
  - a chapter summary whose last stop the OCR lost no longer swallows the text under it: it ends where the text's
    larger type begins (chapter 18, whose verses 1–4 were lost), or at the line opening with the drop capital (17, 20;
    `DROP_START`), unless it breaks a word (21);
  - the book's lines end at the next book's chapter 1 (2 Samuel 1 shares leaf 357).

  The summary fixes came after the vote, so in 1 Samuel the readers restored three chapter openings on the page (17:1–2,
  20:1, and a summary line in 19, 21 and 27 taken out); re-voting would have moved the readers' row numbers. Ruth's
  vote is unchanged by them. Tests for each (`test_ocrdraft.py`); 214 pass.
- **Read** on the page by eighteen readers, two leaves each, every line on its crop and the whole pages for margins,
  indents and footnotes, doubtful places zoomed (ffmpeg crops at 2–6×). Their rows were merged (`1Sam1-31.tsv`) and
  Claude checked the open points on the page (below).
- **Result**: `data/witnesses/read-1738/1Sam1-31.tsv`, 3,410 rows: 3,365 text lines, 36 footnotes and 9 catchwords or
  signatures as `%` rows. `1Sam1-31.corrections.tsv`: 2,458 rows, of which 2,394 changed lines, 49 added (lost text
  lines and footnotes) and 15 removed (junk, the book's title, running heads and summary lines read as text). The vote's
  verse numbers were a running count and wrong almost everywhere; every number was placed again from 1738's margins
  (where the gutter cut a tens digit, by the sequence).

## Checked by Claude on the page

- **5:8** (leaf 327, left column): the margin's 8 stands beside *dure tractaret. Itaque arcessitis*, a line that opens
  mid-clause; 1738's 5:8 begins at *Itaque* (margin and sense, the readers' rule). The read line had `#8` at the line's
  start; corrected. Likewise **23:4** (`#4` stood before *cederent*, the second half of *ac-|cederent*; now at
  *iterum*) and **20:43** (`#43` at *sunto.*; the reader's notes put it at *Tum ille discessit*, now so).
- **28:6**, the note on *claritatem*: *per Pontificem, qui hæc verba, Claritas et Integritas, gestabat in monili,* ends
  in a comma at the foot of leaf 353; the foot of leaf 354 has only the next note (*e) diuinum virum …*) and show-through
  from the verso. Printed unfinished; kept so.
- **30:5** *D uidis* (the *a* fallen out of the forme), **26:6** *cum co* (the letter is a *c*), **31:9** *nuntios*: so
  on the page; kept (decision 58).
- **12:17**: one reader kept an asterisk in the text; taken out, as the others and Ruth's were (it is listed below).
- **Paragraphs**: `orig --read-lines` takes 1738's indents from the hOCR; against the readers' lists, three were false
  (2:1 *attollitur* and 22:1 *Quod vbi*, each the line beside a drop capital; 28:11 *Et mulier*, flush with the column)
  and six were missed (2:27 *Et diuinus*, 2:31 *Scito*, 5:10 *Itaque diuinam*, 9:11 *Atque in adscensu*, 9:26
  *Quumque surrexisset*, 22:11 *Tum rex*), each seen on the page. One more: 1738's chapter 2 opens at the song
  (*EXsultat*), now inside the KJV's 2:1. Recorded as `¶` / `¶-` rows in `data/decisions/1Sam.orig.tsv`. A `¶` row
  can now name a later word of the verse (`Quumque#1`), for an indent inside a KJV verse
  (`orig.verse_paragraph_rows`; test in `test_orig.py`).

## Footnotes and Castellio's marks (inputs for phase 2's notes)

- **36 lettered footnotes**, each a `%` row with its printed text, its mark taken out of the text row; listed with the
  word each hangs on in the readers' notes. Almost all glosses on the sense; one textual, on 12:15 *G. vestrum regem
  H.*: *in Hebræo est, patres vestros: sed in Græco melius, vt mihi videtur.* Whether they are Castellio's 1554 margins
  (as three of Ruth's were) is for phase 2.
- **Castellio's marks**, printed in the text (KJV verses): *G. … H.* 2:8 (*Qui et precantibus vota … facit in terris*,
  the Greek's lines in Hannah's song), 12:14, 12:15, 17:43 (twice; the second *G* has no stop), 17:49; *G. L. … H.*
  5:6 (twice), 11:1, 22:9; *L. … H.* 9:1. The draft keeps them for phase 2 (Joshua's 16:10 was settled without them).
- **Fourteen asterisks** with no footnote on their pages (1738's 1:3, 6:8, 6:17, 8:12, 12:17, 13:1, 14:36, 17:4, 17:12,
  20:18, 28:17, two in chapter 25, one in chapter 30), taken out of the text rows and listed. Ruth's one asterisk stood
  where Castellio's only 1554 annotation on Ruth falls: phase 2 should check these against his 1554 annotations on
  1 Samuel.

## Wording doubts (the printed text keeps 1738; the edition's choice is phase 2's)

KJV verses. Where 1750 agrees with 1738 against Wikisource (most of the readers' many cases), the difference is
Wikisource's and not listed here; the readers' notes list them all.

- 10:25 *populo* (1750 and Wikisource *populi*).
- 19:11 *qui eum obseruarent* (1750 and Wikisource *cum*).
- 30:23 *nos conseruauerit* (1750 and Wikisource *vos*).
- 31:9 *nuntios* (1750 and Wikisource *nuntius*).
- 26:6 *cum co*; 29:9 *dininus*; 30:5 *D uidis*; 12:20 *Iona* (turned *u*): the printer's, to be corrected in the edition.
- 19:4 *Saule patre suo*; 19:9 *hasta, quam*; 24:14 *vnum..*; and the forms the edition will normalize (*sumto*,
  *contemsit*, *depromtum*, *desumserunt*, *adpellatus*, *diremtoria*, *caussa*, *paullum*, *numquam*, lower-case
  *palæstini*, *israeliticus*, *moabiticus*).

## Versification

`data/versification/1Sam1-31.draft.edits.tsv`: **318 edits** (154 split, 162 merge, one `opens`, one `absent`),
applied to `text/draft/1SA.usfm` and the printed text (decision 30's standing rule, each with the KJV's words that place
it). Made by four aligners (1–8, 9–16, 17–24, 25–31), each tested on both texts; the checks pass: the same words, the
KJV's verse counts. Castellio recasts the narrative freely, so even the chapters with the KJV's count (1, 3–5, 8–12, 14,
16–18, 22, 25, 27, 29, 30) are cut differently in many places. The judgments:

- **1:28 / 2:1**: `opens`: *Et Anna his verbis supplicauit:* (the end of 1738's 1:28) opens the KJV's 2:1.
- **2:8**: Castellio's *G. … H.* lines from the Greek (1738's 2:9–11) have no KJV verse; merged into 2:8, where he
  placed them (as Genesis 11's Cainan).
- **13:23 `absent`**: the garrison going out to the pass of Michmash is only a relative clause inside 14:1 (*præsidium,
  quod vltra Machmas processerat*); chapter 13 keeps 22 verses (as Gen 41:57).
- One Latin sentence across two KJV verses, split where the second's first words begin: 12:6/7 (*vobiscum disputem*),
  15:18/19 (*non obediuisti*), 14:25/26, 25:18/19, 25:37/38, 28:5/6, 30:1/2; left as Castellio divides where the next
  verse's words do not stand clear: 17:14–15, 17:19–20, 18:13–16, 19:9–10, 20:12–15, 22:20–21, 24:17–18, 30:16–17.
- Lead-in clauses kept with the verse before (17:40, 17:51, 20:34, 24:7/8, as Judg 12:9); 22:12 begins at *in hunc
  modum … audi*, not at the margin's *Cui ille*.
- Three merges bring one of 1738's indents inside a KJV verse (13:7, 14:36, 16:13): kept, as printed.

## What was made

- `data/witnesses/read-1738/1Sam1-31.voted.tsv`, `.doubts.tsv`, `.tsv`, `.corrections.tsv`.
- `text/draft/1SA.usfm`: the draft in Wikisource's conventions, on the KJV's numbering, with the BSB's paragraphs (for
  phase 2).
- **`text/orig/draft/1SA.usfm`**: the printed text, 809 verses; each verse's leaf in `data/orig/1Sam.pages.tsv`.
- `data/decisions/1Sam.orig.tsv`: the ten paragraph rows.
- `docs/editions.md`: "1 Samuel in 1738".
- The ledger: 1 Samuel 1–31 `corrected`.

## On approval

Move `text/orig/draft/1SA.usfm` to `text/orig/1SA.usfm` (never rewritten by code after that), then phase 2:
`propose 1Sam 1-31` and the notes search side by side.
