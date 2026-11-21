# 2 Samuel 1–24, phase 1: the transcription

*2026-11-21. Decision 85's phase 1 (PLAN.md §4), on Nathan's "Start next book transcription". Gate: the printed text
`text/orig/draft/2SA.usfm` approved → `text/orig/2SA.usfm`. The readers' own notes: `2sam1-24-transcription-readers.md`;
their rows, the readers' and aligners' briefs and the merge script: `2sam1-24-readers/`.*

**Decision:** approved for now (Nathan, 2026-11-21: "Approve for now"); `text/orig/draft/2SA.usfm` moved to `text/orig/2SA.usfm`. Phase 2 next.

## For you

1. **Approve the printed text for now?** `text/orig/draft/2SA.usfm`: every word from the lines read on the page,
   on the KJV's numbering, 693 verse ids for the KJV's 695 (15:9–11 is one, below), 12,513 words, the same as the
   draft's verse for verse (spacing after a stop apart: the printed text writes *adposito. epulatus*, as 1 Samuel's
   *euehit, tenuesque*); 62 paragraphs (each chapter's start and the indents read on the page). Castellio's *G.*, *L.*,
   *H.* marks are printed as 1738 has them; the footnotes are not.
2. **The versification** (210 edits, `data/versification/2Sam1-24.draft.edits.tsv`, applied to the draft and the
   printed text; decision 30's standing rule). Two calls you may want to see:
   - **15:9–11 as one verse** (`\v 9-11`, a `range`, as Num 7:12–83): Castellio puts the KJV's 15:11 (*comitantibus
     ducentis Hierosolymitanis … ignaris*) inside his 15:9, before the KJV's 15:10 (*Dimiserat autem Absalomus
     emissarios*); the order cannot follow the KJV's, and `absent` mid-chapter would misnumber the rest.
   - **Two chapter breaks moved**: 1738's 14:1 (*Interea quum rex Dauid …*) is the KJV's 13:39, and 1738's 20:1 opens
     with the KJV's 19:43b (*Sed quum Iudæi Israelitas verbis superarent:*).
3. Nothing else waits on you in phase 1. Phase 2 has the slips, the footnotes and asterisks, and Castellio's marks.

## How the lines were read

- **Leaves**: 1738 (archive.org `bibliasacraexseb01cast`) leaves **357–385**, found with `lines --heads`. The book
  begins on leaf 357 under 1 Samuel 31 and ends on leaf 385 above *REGVM LIBER III.* Wikisource has no 2 Samuel.
- **Voted** with `python -m pipeline lines 2Sam 1-24 --leaves 357-385`: 2,743 lines; words from 1738's OCR 10,421,
  1750 371, 1726 17, unknown 1,425 (no Wikisource voter, so about twice 1 Samuel's share); 41 doubts.
- **Read** on the page by fourteen readers, two leaves each (the last three), every line on its crop and the whole
  pages for margins, indents and footnotes, doubtful places zoomed with ffmpeg. All fourteen ran at once; after
  Nathan's note on the quota (2026-11-21) the three aligners ran one after another, and the rest was done here.
- **Result**: `data/witnesses/read-1738/2Sam1-24.tsv`, 2,760 rows: 2,711 text lines, 24 chapter rows, 21 footnotes and
  4 catchwords or signatures as `%` rows. `2Sam1-24.corrections.tsv`: 2,028 changed lines, 37 added (23:1–7's 25 lines
  and footnotes the OCR lost or garbled), 20 removed (running heads, the ends of chapter summaries read as text, a
  footnote's second half). The vote's verse numbers were a running count and wrong almost everywhere; every number was
  placed again from 1738's margins. Every chapter's numbers run 1…n without a gap (checked).
- **The vote lost 23:1–7**, David's last words: the OCR lost the summary's second line and read the drop capital *S*
  as a speck apart from *Equuntur*, so the summary ran on to *cremantur.* Reader 14 added the 25 lines from the page.
  **Fix**: `ocrdraft.py`'s exception for a summary line ending in a broken word now holds only when the next line
  stands right under it (`test_summary_ends_at_a_gap`). Not re-voted (the readers' rows would move).

## Checked by Claude on the page

- **Initials**: 2:9 *Iezraelenses* and 5:15 *Iebahar*: capital I with a worn, slanted top serif. First read *l* (by the
  readers and by Claude, against *Iaphia*'s flat-topped I); corrected on Nathan's reading (2026-11-21), with 1 Samuel's
  1:20 *loua* → *Ioua* proposed in `data/review/1sam-orig-ioua.md`.
- **Letters**: 3:27 *Asaclis* (a *c*); 12:20 *adoranit* (an *n*); 19:15 *eumque* (a clear *e*; 1750 and 1726
  *cumque*); 20:8 *peruenernnt*; 12:17 *senatcres*; 11:9 *Vrjas* (a *j*); 19:26 *rcx* read *rex* (a worn *e*); 22:31
  *omnib us*, a gap in the type, read *omnibus*. Stops: 12:20 *adposito.epulatus* and 16:1 *DAuid autem. paullulum*,
  clear stops, kept.
- **Paragraphs**: `orig --read-lines` takes 1738's indents from the hOCR; against the readers' lists, two were missed
  (3:12 *At Abner*, 19:11 *Et Dauid rex*, each indented after a short line) and one was false (21:1 *Itaque
  percontatus*, the third line beside the drop capital V). Recorded in `data/decisions/2Sam.orig.tsv`.
- **Code**: `orig.from_read_lines` placed a leaf mark inside a word broken across leaves (13:34 *Absa-|lomus*, leaves
  370/371), and a versification anchor across a leaf break (19:26 *ille me a-|pud*) was not found. The mark now goes
  before the broken word, and anchors are matched with a leaf mark allowed between their words (`marked_anchor`;
  test in `test_orig.py`). Tests pass (217).

## Footnotes and Castellio's marks (inputs for phase 2's notes)

- **21 lettered footnotes**, each a `%` row with its printed text, its letter taken out of the text row; listed with
  the word each hangs on in the readers' notes. Textual ones: 2:9 *Latinus Gessuræos, Græcus Thasiri.*; 2:29 *Latinus
  Bethorone.*; 4:6 *Græce, quum quidem ædium ianitrix (quæ triticum euellebat) somno oppressa dormiret,* (ends in a
  comma); 15:7 *Iosephus 4 habet, at in Hebræo 40 sunt.*; 18:18 on Absalom's sons (*supra cap. 14.*); 24:1 *… Vid. 1.
  Par. 27.* The rest are glosses (12:25 *hoc est, Iouæ carum.*; 19:43 *decem partes, quod decem tribus erant.*).
- **Castellio's marks**, printed in the text: *G. L. … H.* 1:19, 8:8, 13:21, 14:30, 15:20; *L. … H.* 1:26 (*Sicut
  mater …*, the Vulgate's addition), 8:13, 13:37, 15:18; *G. … H.* 14:27, 17:3; 8:7–8 (*… H.*, *G. L. ex quo … L. et
  altare G. et lauacra … H.*). At 17:3 the reader wrote `#3 G. vt sponsa` (number before the mark); 1 Samuel 2:9 had
  the mark first: the order follows the margin and the sense, so both stand.
- **Eleven asterisks** with no footnote (5:8, 7:7, 7:24, 12:26, 14:13, 15:7, 18:3, 18:17, 21:6, 23:3, 23:8; and a
  raised mark at 21:6 *Darentur*, perhaps a worn one), taken out and listed. In 1 Samuel all fourteen marked
  Castellio's 1554 annotations: phase 2 checks these against *IN LIBROS REGVM*.

## Wording doubts (the printed text keeps 1738; the edition's choice is phase 2's)

- 19:15 *eumque Iordanem traducturi* (1750, 1726 *cumque*).
- 3:27 *Asaclis* (1750 *Asaelis*); 12:20 *adoranit*; 12:17
  *senatcres*; 20:8 *peruenernnt*; 16:1 *autem.*: the printer's, to be corrected in the edition.
- 12:31 *oppidis Moabitarum* where the Hebrew has the Ammonites: 1726 the same, so Castellio's text (a note, perhaps).
- 23:8: Castellio leaves out "Adino the Eznite" (an asterisk stands there); 15:7 *quatuor annis* (the footnote says
  the Hebrew has 40). Otherwise 1738 and 1750 differ only in spelling and stops (readers' notes).

## Versification

`data/versification/2Sam1-24.draft.edits.tsv`: **210 edits** (102 split, 105 merge, 2 chapter, 1 range), applied to
`text/draft/2SA.usfm` and the printed text, each with the KJV's words that place it. Made by three aligners one after
another (1–8, 9–16, 17–24), each tested on both texts; the checks pass: the same words, the KJV's verse counts. The
judgments beyond the two above:

- Clauses that open one of 1738's verses but render the end of the KJV verse before move back (2:14/15, 2:21/22,
  3:34/35, 5:20/21, 12:18/19, 13:33/34 *Absalomus autem aufugit.*, 14:28/29 and others, as 1 Sam 2:24).
- 1:26/27: *L. Sicut mater … diligebam. H.* (1738's 27) joins the KJV's 26, as 1 Sam 2:8's Greek lines.
- 6:3–4 and 13:37–38: Castellio gives the Hebrew's repeated clause once; the KJV's 6:4 is *Ahione arcam præcedente:*,
  13:38 *ibique fuit triennium.*
- Left as Castellio divides where the next verse's words do not stand clear: 2:25/26, 3:17/18, 3:26/27, 3:30/31,
  7:18/19, 7:23/24, 10:8/9, 10:17/18, 11:1/2, 11:6/7, 11:27/12:1, 13:1/2, 13:10/11, 14:5/6, 16:5/6, 18:24/25, 19:3–5,
  21:2/3, 21:15/16, 23:18/19.
- Chapter 22 (the song, set as prose in 1738): 1738 runs one ahead of the KJV from 22:24, and its 42–43 are the KJV's
  43.

## What was made

- `data/witnesses/read-1738/2Sam1-24.voted.tsv`, `.doubts.tsv`, `.tsv`, `.corrections.tsv`.
- `text/draft/2SA.usfm`: the draft in Wikisource's conventions, on the KJV's numbering, with the BSB's paragraphs (for
  phase 2).
- **`text/orig/draft/2SA.usfm`**: the printed text; each verse's leaf in `data/orig/2Sam.pages.tsv`. Its title is
  still *Regum liber 2*; phase 2 titles the book *Samuēlis Liber Posterior*, as 1 Samuel.
- `data/decisions/2Sam.orig.tsv`: the three paragraph rows.
- `docs/editions.md`: "2 Samuel in 1738".
- Code: `pipeline/ocrdraft.py` (summary at a gap), `pipeline/orig.py` (leaf marks and anchors), with tests.
- The ledger: 2 Samuel 1–24 `corrected`.

## On approval

Move `text/orig/draft/2SA.usfm` to `text/orig/2SA.usfm` (never rewritten by code after that), then phase 2:
`propose 2Sam 1-24` and the notes search side by side.
