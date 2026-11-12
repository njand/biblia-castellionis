# The print PDF: design review and proposals (2026-11-11)

Inspected: `castellio.pdf` as published on Pages (v1.0+ 2026-11-11; 271 pages, A5; Genesis, Exodus, Gospels, Acts,
Romans, 1–2 Corinthians), rendered page by page. Page numbers below are **PDF pages** (printed folio in brackets).
The source is `pipeline/templates/preamble.tex`, `title.tex` and `pipeline/pdf.py` (`ADDITIONS`, `document`,
`colophon`). Nothing has been changed; each item is a proposal for Nathan.

The goal is the look of a reputable Bible press (Cambridge, Crossway's reader's editions, Schuyler, the Deutsche
Bibelgesellschaft's Latin editions): a quiet, even page; every line on one grid; furniture that helps you find a
place; no visible accidents.

---

## A. Defects (wrong now, whatever the design)

**Fixed 2026-11-11** in `preamble.tex` and `pdf.py`, checked on a local Tectonic build of every book in `text/`
(297 pages): contents, bookmarks and running heads all agree with the pages; Genesis and every testament divider
open recto; each book is set in `multicols` (two columns had been switched on only by accident, through memoir's
`\book`, so single-book PDFs came out in one column) and ends balanced; the text block is a whole number of lines
(40), so columns fill without stretching; poems carry no space above or below and wrap ragged without hyphens; a
chapter's first paragraph never leaves fewer than three lines at a column foot (the cost: 9 columns in 297 pages
end up to three lines short); the Wikisource list moved to a last page, "Fontes". Overfull lines in the full
build: 1.

1. **Contents and bookmarks point to the wrong page.** The contents give Exodus 54, it starts on [55]; Mark 109,
   it starts on [110]; the PDF bookmark "Matthæus" opens Exodus 16 (PDF 73; Matthew is PDF 80). `\Liber` calls
   `\addcontentsline` *before* `\clearforchapter`, so the entry and its anchor land on the previous page whenever a
   page break follows. Fix: clear first, then `\phantomsection\addcontentsline…`.
2. **Running heads name the wrong chapter.** They print `\libernameshort\ \thecaputcount` at shipout, i.e. the
   counter's value when the page is cut, not what is on the page: PDF 7 holds Genesis 1:31–2:25 and is headed
   "Genesis 3"; PDF 58, the last page of Genesis, is headed **"Exodus 0"**; PDF 72 holds Exodus 18:5–19:9 and says
   "Exodus 19". Fix with marks (see B4).
3. **Genesis opens on a verso.** `openany` plus the contents ending on [1] put Genesis on PDF 6, a left-hand page,
   with a blank PDF 4 before the testament divider. Testament dividers and Genesis/Matthew should open recto;
   other books may run on (B6).
4. **A drop cap followed by poetry breaks.** Matthew 1 (PDF 80): the cap takes two lines, the prose verse needs
   two and a half, so "-mō:" falls under the "1" by itself, then a blank line, then the genealogy. Any chapter whose
   first verse is short or opens a `verse` block risks this. Fix: if the chapter's first block is poetry or the
   first paragraph is shorter than ~3 lines, set the cap with `lines=2` and `\lettrine` inside a paragraph that is
   allowed to end early (`\par` after a `\vphantom` of the cap's depth), or drop the cap to a hanging numeral for
   such chapters.
5. **Unequal, unpredictable white space at chapter openings and around poetry.** `\Caput` adds `\linebreak` and a
   paragraph end, then lettrine; the result is 2–3 blank lines before some chapters (PDF 7, 59, 72, 77) and a full
   blank line before and after every poem (PDF 7, 8). Columns no longer share baselines (compare left and right
   columns on PDF 7). See B2.
6. **Book endings are unbalanced.** The last page of a book fills the left column and leaves the right empty
   (Genesis, PDF 58; Exodus, PDF 74). End each book with balanced columns (`multicols` or `\balance`), so the last
   page has two short columns of equal height.
7. **Small furniture slips.** "Biblia Sacra" is printed twice on the title page (the `title` argument under the
   title proper); the colophon is a wall of monospaced URLs (Latin Modern Mono is the only third font in the
   book); hyphens split poetry lines inside a narrow column ("bēs- / tiārum", "Rā- / chabā", PDF 8, 80).

---

## B. Design proposals

### B1. Page and measure: one column, wider measure (recommended)

Today: A5, 9 pt Pagella, two columns of ~36 characters, 0.5 in inner margin. Justified Latin with long macroned
words in a 36-character column gives rivers and wide word spaces (PDF 7, "Deus diē septimō suum, quod fēcerat"),
a hyphen every four or five lines, and poetry that turns over on almost every line (Genesis 3, PDF 8).

For a **reader's edition** — modern paragraphs, verse set as verse, quotation marks — the presses that do this
(ESV Reader's Bible, Bibliotheca, Schuyler's reader's editions) use a **single column**. On A5 that is a measure of
about 62–66 characters at 9.5/12.5 pt: the ideal range, almost no hyphenation, poetry on one line with real
indents. Page count rises roughly 15–25 % (the two-column page loses space to gutters, ragged poem lines and
column ends anyway), which matters only for a one-volume whole Bible; if that is the target, set the two
testaments as two volumes, or move to a 6 × 9 in trim and keep a single column.

If two columns are kept (for a compact whole Bible): go to 6 × 9 in or 15.5 × 23.5 cm, 8.75/11 pt, gutter
1.5 pc with a 0.3 pt column rule, and set poetry ragged-right without hyphenation.

### B2. One baseline grid

Every line on every page sits on the same baseline grid (it also stops show-through on thin Bible paper, where
lines on the back of the leaf print between the lines on the front). Concretely:
- chapter openings take exactly **one blank line** before the cap, nothing after; no `\linebreak`;
- poetry: no space before or after a poem by default, **half-line** stanza breaks only where two half-lines pair up,
  or a full line; never `\medskip`/`\smallskip` (they are off-grid);
- headings (book titles, `\Argumentum`, `\Titulus`, `\Subscriptio`) sized and spaced in whole multiples of the
  baseline (`\vspace{\baselineskip}`), `\raggedbottom` off, `\flushbottom` on;
- verse numbers must not change the line height: set them with `\raisebox` and zero height, not `\textsuperscript`
  (currently `\linespread{1.1}` hides the bumps by loosening every line).

### B3. Type

- **Face**: Gentium Book (already the website's face, in `pipeline/fonts/`, OFL; use the full SIL fonts for print,
  not the web subsets). It has precomposed ȳ Ȳ (Pagella lacks them; they are faked with `\=y` today), proper
  macron spacing over capitals (compare "ĒVANGELIUM", PDF 80), Greek and Hebrew from the same family/companion
  (Ezra SIL), and gives print and screen one identity. Alternatives with full macron coverage: EB Garamond,
  Brill (free for non-commercial use, check terms), Cardo.
- **Engine**: LuaLaTeX rather than XeTeX/Tectonic, so `microtype` can do font expansion as well as protrusion.
  Expansion is what lets justified narrow measures avoid rivers. (Tectonic can stay as fallback.)
- **Size**: 9.5/12.5 single column (B1); 8.75/11 if two columns.
- **Figures**: old-style figures in running text and verse numbers; lining in chapter caps.
- **Penalties**: `\widowpenalty=10000 \clubpenalty=10000`, `\brokenpenalty=10000` (no hyphen at a page/column
  end), `\hyphenpenalty` raised in poetry, `\lefthyphenmin=3 \righthyphenmin=3` for Latin.

### B4. Running heads and folios

The standard Bible head gives the **range on the page**: left page "GENESIS 1:31 – 2:25", right page the same for
its own page, set in letterspaced small capitals at 7.5 pt, with the folio at the outer edge of the head or centred
at the foot. Implement with marks: each `\Versus` sets a mark `Book Chapter:Verse`; the head prints
`\firstmark … \botmark` (memoir's `\firstmark`/`\botmark`, or `extramarks`/`titleps`). This also fixes A2. A thin
rule (0.3 pt) under the head is common; optional. Remove the vertical bar separators.

Book-opening pages: no head, folio at the foot (`\thispagestyle{chapter}` with a foot folio), as now but with the
folio printed.

### B5. Book and chapter openings

- **Book titles** span the full measure and are set in a clear hierarchy, not three lines of `\HUGE` small caps in
  one column (PDF 80, 234): a small letterspaced line for the form ("ĒVANGELIUM AUCTŌRE", "PAULĪ APOSTOLĪ
  EPISTOLA AD"), then the name in large capitals or caps-and-small-caps ("MATTHÆUS", "RŌMĀNŌS"), then one or two
  blank lines. In two columns use `\twocolumn[...]`/`multicols` with the title as its preamble.
- **Chapter numbers**: keep two-line drop numerals, but lighter: the same face, regular weight or semibold, kerned
  close to the text, `lettrine` `findent=0.3em, nindent=0pt`; first word of the chapter in small caps
  (`\lettrine{1}{Prīncipiō}` → "1 PRĪNCIPIŌ creāvit…") as Cambridge and Crossway do.
- **Rubrication (optional, two-colour print)**: chapter numerals and book titles in a dark red. It costs a second
  colour at press; the PDF can carry it with a one-line switch so a one-colour printing remains possible.
- **Verse numbers**: 6.5 pt old-style, raised ~0.35 em with zero height (B2), followed by a thin unbreakable space
  (`\,` tied to the word) so the number never ends a line alone. Optionally a mid-grey (70 % black) on screen
  editions only.

### B6. Front and back matter, in the order a press would print it

1. Half-title: BIBLIA SACRA, alone, small. (recto)
2. Blank. (verso)
3. **Title page**: BIBLIA SACRA / ex / SEBASTIĀNĪ CASTELLIŌNIS / interpretātiōne, then at the foot the edition line
   (edition and year; wording for Nathan to choose) — not the build title repeated. Spaced caps, a single rule or ornament at most.
4. **Copyright page** (verso of the title): a short paragraph each for the text and its sources, the licence, the
   edition/version and date, and "Source files and corrections: github.com/njand/biblia-castellionis", in 7.5 pt
   serif, ranged left at the foot. No URL list here.
5. Contents (Ōrdō librōrum), with the testaments and books in one tidy table with leaders or a tab, folios in
   old-style figures; no blank page after it unless needed to reach a recto.
6. A short **preface** (Praefātiō or an English note on the edition, drawn from `docs/editions.md`): what text, what
   orthography, what the marks mean. Optionally Castellio's own dedication to Edward VI (1551) as a period text.
7. Testament dividers: half-title style, recto, with the verso blank.
8. Back matter: **Fontes** — the Wikisource pages and revisions in a compact two-column list in serif type with
   shortened URLs (`la.wikisource.org/wiki/…/Genesis`, rev. 170371); the CC BY-SA credit stays complete. Optionally
   a table of book names and abbreviations.

### B7. Production

- Trim and bleed: produce a printer's version with 3 mm bleed and crop marks (memoir `\settrims`, or the `crop`
  package), and keep the plain PDF for the website.
- PDF/X-4 (or PDF/A-2b for the archived copy) via `pdfx`/`\DocumentMetadata`; all fonts embedded (they are now),
  black text as 100 % K only.
- Total pages a multiple of 16 (or 32 for Bible paper signatures), padding with blanks at the end.
- Hyperlinks: keep for the screen PDF, but no coloured boxes; the print PDF without links.

---

## Suggested order

1. A1–A3, A6–A7 (half a day: TOC/marks, recto openings, balanced endings, title and colophon tidy).
2. B2 grid + B3 penalties + B5 verse numbers (the page starts to look professional).
3. Decide B1 (one column vs two, trim size) and B3 face; then B4 heads and B5 openings, which depend on the measure.
4. B6 front/back matter, B7 production files.

A before/after prototype of a few spreads (Genesis 1–3, Matthew 1, Romans 1) would settle B1 and B3 quickly; it
needs a local TeX (Tectonic or TeX Live/MiKTeX), which this machine does not have now.
