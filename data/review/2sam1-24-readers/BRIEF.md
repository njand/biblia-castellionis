# 2 Samuel, phase 1: reading 1738's lines on the page (brief for each reader)

Repo: `C:\Users\nathanjamesanderson\Documents\biblia-castellionis` (read `data/witnesses/read-1738/README.md`, and
`data/review/1sam1-31-transcription-readers.md` Reader 01 as a model of the notes wanted). You are one of 14 readers.
**Read only; do not edit any repo file.** Write only your two output files (below). Do not run `pipeline lines`.

## What you have

- `data/witnesses/read-1738/2Sam1-24.voted.tsv`: 1738's OCR of 2 Samuel, one row per printed line
  (`leaf column line text`), each word repaired and voted with 1750 and 1726 (no Wikisource for this book, so the
  vote is rougher than 1 Samuel's: ~1,400 words no witness could vote). **Row numbers are file lines** (the header is
  row 1). `#N` marks a verse start: the vote's verse numbers are a running count and are **usually wrong**; place
  every one again from 1738's margin. `\c N` rows are chapter starts (the chapter heading and italic summary are
  already taken off): copy them unchanged.
- `data/witnesses/read-1738/2Sam1-24.doubts.tsv`: places where 1750 and 1726 agree against the vote; look first.
- Reading sheets: `sources/archive/crops/sheets/lines/2Sam1-24.voted-NNN.jpg` (14 rows each, every line's crop under
  its voted text, labelled with its row). Your sheet numbers are given in your prompt.
- Whole pages: `sources/archive/crops/1738-page-0LLL.jpg` (LLL = leaf; 1680×2742 px; two columns, margin verse
  numbers outside each column, footnotes at the column's foot). Use them for margins, indents, footnotes, and
  anything the line crops cut. Zoom with ffmpeg into your own scratch folder, e.g.
  `ffmpeg -y -loglevel error -i PAGE.jpg -vf "crop=W:H:X:Y,scale=iw*3:-1" OUT.png`, then Read the PNG.
- Other witnesses (for wording doubts only; never the base): 1750 OCR `sources/archive/1750/text.txt` (noisy;
  grep it), 1726 OCR `TXT/1 - OCR/Vetus Fœdus/regum liber 2.txt`. English: `sources/parallel/bsb/2Sam.tsv`,
  Vulgate `sources/parallel/vulgate/2Sam.tsv` (if present) for the omission check.

## The rule (decisions 57, 58, 85): read the page once and take everything from it

Write each line **exactly as 1738 prints it**: spelling, u/v and i/j, æ and œ, capitals, punctuation, misprints,
word division, hyphen at line end (`ter-`). Only these are normalized: **s for ſ**; **& → et**; **q; → que**;
spaces before punctuation are dropped (`peruenit,` not `peruenit ,`). Never correct Castellio or his printer, never
take a word from 1750 or 1726 because it is "better": a misprint stays (note it). A drop capital is written with its
word as printed (`MORTVO` if the rest is capitals; `EXsultat` style if not). Where two words are set tight, write
the space; where a comma has no space after it, keep as printed (`euehit,tenuesque`) and note it.

- **Verse starts**: `#N` before the word where 1738's margin number and the sense put the verse's start (the margin
  number stands beside the line; within the line, the start is usually after a stop and a wider space). Where the
  gutter cuts a number, place it by the visible fragment, the sequence and the sense. A misprinted margin numeral:
  write the right number by sequence and note it. Chapter verse numbers restart at 1.
- **Footnotes**: each lettered note at a column's foot is its own row: `% c) text as printed.` placed right after the
  last text row of that column (new line number from 900 up on that leaf: 900, 901 …). Take the note's letter (and
  its parenthesis) **out of** the text row, and say in your notes which word it hangs on.
- **Castellio's marks** *G.*, *L.*, *H.* (italic capitals in the text) are **kept** in the text row as printed.
- **Asterisks** in the text with no footnote: take out, list with the word they stand by.
- **Catchwords and signatures** at a column's foot, if the vote has them as a row: make the row `% word` (as 1 Sam's
  `% T 3 Pa-`). Running heads, the book title (*REGVM LIBER II.*), *CAPVT* headings and the italic chapter summaries
  are not text: remove such rows (say which). A text line the OCR lost: add it with line number 900+ (say where).
- **Indents** (paragraphs): check each column's left edge; list every indented line (and drop capitals).

## Output (two files in `C:\Users\NATHAN~1\AppData\Local\Temp\claude\c92004cc0b41e5d1\3c436567-a4d0-44c9-afdd-54317e74a3b4\scratchpad\2sam\`)

1. `reader-NN.tsv`, tab-separated, header `row	leaf	column	line	text`, one row per line of your range **in page
   order** (column 0 then column 1 of each leaf; footnote rows after their column's text): `row` = the voted file's
   row number, or `+` for an added row. Every row of your range appears unless removed. Copy `\c N` rows unchanged.
   UTF-8, no BOM. Check it: same rows as your range less removed, plus added; no stray tabs.
2. `reader-NN.md`, notes in the shape of 1 Samuel's Reader 01: leaves and what is on them; verse numbers per chapter
   (where each verse begins, which numbers were cut or misprinted, which placed by sense within a line); letters
   lost in the gutter; misprints and odd forms kept as printed; paragraph indents (row numbers); footnotes (letter,
   text, the word it hangs on); G./L./H. marks and asterisks; lost/added/removed rows; **wording doubts** (where
   1738 and 1750 differ in more than spelling, or 1738 looks misprinted against the sense; quote both); an
   **omission check** (each verse against the BSB: a clause the page has and your reading lost — or, if the page
   itself lacks what the Hebrew has, say so); uncertain readings and how you settled them (zoom); a summary count
   (rows written, changed from the vote, removed, added).

Be thorough and exact: the read lines become the approved printed text. Zoom on every doubtful letter and stop
(comma vs. full stop, colon vs. semicolon, e/c, u/n, f/ſ (long s), rn/m, ii/ü). Your final message: a few lines
(rows written/changed, anything uncertain you want Claude to check on the page).
