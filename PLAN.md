# Automation plan: from scans to a finished edition

*Drafted 2026-11-05. Replaces the manual OCR → correct → edit → macronize workflow described in `TXT/README.md`.*

## 1. The short version

Most of the transcription already exists. Latin Wikisource hosts a versified transcription of Castellio's Bible covering the whole New Testament and much of the Old. Your 2019 WordPress site has macronized text for all four Gospels and Genesis 1–35. Against the chapters you have already finished, Wikisource's Gospels agree on **99.3–99.5% of words** once case, j/v and æ are set aside. Almost every remaining difference is one of your own Gaffiot respellings.

So the job is no longer *transcription*. It is **verification, normalization, macronization and formatting**, and all four can be largely automated:

1. **Take Wikisource as the base text.** Verify it word by word against several independent OCRs of different editions on archive.org. Claude resolves disagreements by looking at the page image.
2. **Normalize to Gaffiot 2016** with a rule table learned from your ~62 finished chapters, plus Gaffiot lookups for words not yet covered.
3. **Add macrons** with the fur-fulminis macron database (Wiktionary + Macronizer + Gaffiot). Your WordPress macrons count as an extra witness. Homographs are decided by Claude from the syntax, with the Greek/Hebrew and English as evidence.
4. **Format.** Paragraphs, poetry and quotations are carried over from a public-domain modern Bible (the BSB), then adjusted for Latin.
5. **Review.** You review only a short queue of low-confidence proposals per chapter, plus a random sample. Everything else is applied automatically and logged.
6. **Publish from one master.** The edition's master copy is **USFM**, one file per book. The website, EPUB, print PDF (via generated LaTeX), plain text and the ebible.org/Bible-app distribution are all built from it (§4a).

The ~62 finished chapters are a **test set**: the pipeline is run on them and scored against your hand-made results before it is trusted on new chapters.

## 2. What we have

### 2.1 Text sources for Castellio

| Source | Coverage | State | Role |
|---|---|---|---|
| This repo, LaTeX | Gen 1–27, Mt 1–13 (+ 14–28 drafted), Mk 1–5, Lk 1–13, Jn 1–4 | Finished: Gaffiot orthography, macrons, paragraphs, quotes, poetry | **Gold standard** and test set; never rewritten |
| This repo, TXT | Gen 28–35 macronized; Gen 36–50, Ex 1–20 edited; Acts corrected (partly) | In progress | Inputs for those chapters |
| This repo, `TXT/1 - OCR` | Gen–2 Kings + Ruth; all of the NT | Raw Google Books OCR of 1726–27 (the finished chapters' source) | One more OCR witness |
| [WordPress site](https://bibliasacracastellionis.wordpress.com/) | Mt 1–28, Mk 1–16, Lk 1–24, Jn 1–21, Gen 1–35 (Gen 34 has no macrons) | Macronized, one verse per line, old spelling (*ae*, *coepit*), no quotation marks | **Macron witness** (your earlier decisions) |
| [la.wikisource: *Biblia Sacra interprete Sebastiano Castellione*](https://la.wikisource.org/wiki/Biblia_Sacra_interprete_Sebastiano_Castellione) | All 27 NT books; nearly complete Genesis, Judges, Ruth, 1 Kings, Job, Esther, Judith, Tobit, Wisdom, Song, minor prophets; partial Exodus (461/1213 verses), Leviticus, Joshua; stubs for Numbers, Deuteronomy, Chronicles, Psalms, Isaiah, Jeremiah | Clean, versified, with chapter summaries; marked "25%" (not proofread). NT cites 1760 (its Gospels follow the 1573/1758 line, its Acts–Revelation the early line), OT from 1738 | **Working text** wherever it exists; NT base edition 1573 (decision 24) |
| archive.org scans (images + OCR + word coordinates) | See below | Varying OCR quality | **Independent witnesses**, and page images for checking |

archive.org editions, all with `_djvu.txt` OCR, `_hocr.html` word boxes and `_jp2.zip` page images:

| Identifier | Edition | Scope | OCR |
|---|---|---|---|
| `bibliasacraexseb01cast` | Leipzig 1738, vol. 1 | OT (Wikisource's OT source) | ABBYY 8, moderate (*f*/*s* confusions) |
| `biblia-sacra-ex-sebastiani-castellionis-interpretatione-eivsqve-postrema-1750` | 1750 Bible (+ 1715 NT in the same item) | Whole Bible | Tesseract, noisy |
| `ned-kbn-all-00001225-001` | 1681 NT (KB Netherlands) | NT | ABBYY 9, moderate |
| `novvm-testamentvm-latinvm-…-1747` | 1747 NT (+ 1750 Bible duplicate) | NT | Tesseract, noisy |
| `bim_eighteenth-century_novum-testamentum-ex-seb_1758_1`, `_2` | 1758 NT, 2 vols | NT | Tesseract with ſ, **good** |
| Google Books 1726–27 (vols 1–4), 1697, 1553 NT | Your current sources | Whole Bible / NT | Already in `TXT/1 - OCR` for part |

A New Testament verse will typically have **5–6 independent readings**, and an Old Testament verse 3–4. That is enough to outvote individual OCR errors and to spot genuine differences between editions.

### 2.2 Parallel Bibles (public domain or openly licensed)

| Text | Use |
|---|---|
| **KJV** | Versification target (as the WordPress site promised); verse counts per chapter |
| **Berean Standard Bible** (public domain since 2023; USFM from ebible.org) | Paragraph breaks, poetry lines and indents (`\q1`/`\q2`), quotation boundaries, section structure |
| **World English Bible** (public domain) | Second opinion on quotation boundaries and paragraphing |
| **Vulgata Clementina** (on la.wikisource) | Proper-name forms; Latin sense check when a word is in doubt |
| **SBLGNT** (CC BY 4.0) / **OSHB/WLC** (open) | Greek tense and mood to tell homographs apart (*venit*/*vēnit*, *legit*/*lēgit*); checking that no clause was dropped |

### 2.3 Tools in the sibling projects

| Tool | Where | What it gives us | Gap |
|---|---|---|---|
| `lrl macron`, `macron-check --text`, `macron-triage`, `ls`, `attest` | `../fur-fulminis/tools/lrl` (databases in `fur-fulminis/data/`, about 900 MB, git-ignored) | Macron lookup from three sources (W, M, **G = Gaffiot 2016**); triage into auto-fix (A1), hidden quantity (A2), your call (B), names (C), Gaffiot differs (G); Lewis & Short; corpus attestation | Checks and triages macrons but **does not insert them** |
| `tools/latin.py` | `../e-liber` | A read-only bridge to `lrl` from another repo (set `LATIN_REF_HOME`); copy this pattern | — |
| `eliber orthography` (`orthography.jv`, `choose`, contractions, enclitics) | `../e-liber/src/eliber/orthography.py` | Inserts macrons when a form has exactly one known answer; consonantal j/v by rule; lists homographs and unknown words for Claude to decide in a `forms:` YAML (book-wide or per verse); a `settled:` list protects reviewed blocks | Hard-coded to e-liber's paths; prefers Wiktionary over Gaffiot on hidden quantities (we want **Gaffiot first**); folds æ/œ to ae/oe (we want ligatures) |
| epubcheck + portable JRE | `../e-liber/.tools/` | EPUB validation | — |
| `it extract`, proposals format, `review-by-confidence` | `../insula-thesauraria` | One structured master file (TSV, stable IDs); proposals with **exact `Apply:` lines checked to match once**; queue sorted by confidence; "decide once, apply book-wide" recorded spellings | No auto-apply tier (every item is reviewed) |
| `late-screen`, `syntax-screen` | `../insula-thesauraria/tools/cicero.py` | Flags non-classical vocabulary and syntax | Probably little needed: Castellio already writes classical Latin |
| Workflow pattern: `CLAUDE.md` / `brief.md` / `HUMAN.md`, chunk ledger, independent **critic** agent, `/distill` | `../fur-fulminis/.claude/` | The skeleton for our own skills | The skills themselves are translation-specific |

**Not yet available anywhere:** automatic OCR correction; respelling from 16th-century to Gaffiot orthography; writing æ/œ; USFM output and the publishing builds. Sections 4 and 4a cover these.

**Licensing.** Gaffiot 2016 is CC BY-NC-ND. Using it to *decide* vowel quantities and spellings is fine, but no Gaffiot text should be committed or published. Wikisource transcriptions are CC BY-SA 4.0. The underlying 18th-century text is public domain, but credit Wikisource in the README and decide on a license for this edition (§8).

## 3. Data model

Code lives in `pipeline/` (a Python package, `python -m pipeline`); data lives in `data/` (committed) and `sources/` (raw downloads, git-ignored). One master file per book, one row per verse, with a column for each stage, following insula-thesauraria's TSV:

```
data/text/<osis>.tsv
id         base                    witnesses   corrected   normalized   macronized   structure   status
Matt.14.3  Ceperat enim Joannem…   ws,26,58…   …           …            …            p           settled|auto|review
```

- **IDs** are OSIS (`Matt.14.3`), numbered by the **KJV** (`data/versification/kjv.tsv`). Where an edition numbers verses differently, a mapping file records it. Verse 0 holds a chapter's summary or a psalm title.
- **Witnesses** are stored separately (`data/witnesses/<source>/<osis>.tsv`, built in M0), with the same IDs.
- **Decisions** live in reviewable YAML (`data/decisions/<osis>.yaml`): per-verse homograph choices, variant readings chosen, structure overrides. Rebuilds never overwrite them (e-liber's rule).
- **USFM is the master copy** (decided 2026-11-05; §8, decision 9): one file per book, `text/<USFM code>.usfm` (e.g. `text/MAT.usfm`). The pipeline writes a chapter's USFM once, when the chapter is approved. After that the chapter is `settled`, and the pipeline only *checks* it and never rewrites it. You can still edit it by hand: it is plain text and diffs cleanly. Every published format is generated from it (§4a), so LaTeX is no longer edited, and Overleaf is no longer part of the workflow.
- **A chapter ledger** (`data/status.tsv`, as in fur-fulminis) records each chapter's stage: `pending → fetched → aligned → corrected → normalized → macronized → structured → in-review → approved → settled`.

USFM markers used by this edition:

| Element | USFM | Was (LaTeX) |
|---|---|---|
| Book title and running head | `\id`, `\h`, `\toc1–3`, `\mt1` (e.g. *Ēvangelium Auctōre* / *Matthæō*) | `\Liber[…]{…}` |
| Chapter, verse | `\c 14`, `\v 3` | `\Caput`, `\Versus` |
| Chapter summary (*argumentum*) | `\cd …` | (commented `\summary{}`) |
| Paragraph | `\p` (`\m` to continue after poetry) | blank line |
| Poetry lines and indents | `\q1`, `\q2`, `\q3` | `verse`/`patverse*` with `\indentpattern{…}` |
| Psalm title | `\d …` | — |
| A letter's subscription (after its last verse; decision 37) | `\cls …` | `\Subscriptio{…}` |
| Quoted Scripture (italic) | `\qt …\qt*` | `\emph{…}` |
| Quotation marks, macrons, æ/œ | plain UTF-8 (“…”, ‘…’, ā, æ) | ``…'', `…' |

**Migration (M1):** the settled LaTeX chapters (Gen 1–27, Matt 1–13, Mark 1–5, Luke 1–13, John 1–4) are converted to USFM, and the commented-out Matthew 14–28 is kept as a draft. Converting back to LaTeX and comparing proves the conversion lossless. `LaTeX/`, `HTML/`, `EPUB/`, `TXT/` and `scripts/latex_converter.py` are then retired: kept in git history, with removal your call once the new builds are verified. `TXT/1` and `TXT/2` are already superseded by `data/`.

## 4. The pipeline

*Reorganized 2026-11-19 (HUMAN.md decision 85) into three phases per book, each page read once. The earlier
numbering (stages 0–7, with 2b) is kept in brackets, since the review files and the ledger use it.*

The unit of work is a **book** (or a run of chapters), and each phase ends in one place for Nathan to look. Where a
phase needs judgment, Claude's readers make the calls with their evidence and the phase's summary lists them.

| Phase | Was | What it makes | Gate |
|---|---|---|---|
| **1. Transcribe** | stages 0–2, 2b | The base edition's text as printed, every line read on the page, with its verse starts, paragraphs, footnotes, Castellio's marks and leaves; versified to the KJV | **The printed text approved** → `text/orig/` |
| **2. Edit and annotate** | stages 3–5, 6, the notes round | The reading edition from the approved printed text (spelling, macrons, layout, names) and the light notes, together | **The book settled**, its notes applied in the same step → `text/` |
| **3. Build and check** | stage 7 | Every published format, and the checks | none (automatic) |

**Why this order** (the review of 2026-11-19): the Old Testament books were being read on 1738's pages two or three
times. Judges' every verse was read against Wikisource in stage 2 (170 corrections); its printed text then read the
2,640 words the OCR missed again in stage 2b; the printed text was rebuilt from the settled words after settlement;
and 1738's footnotes, seen in stage 2, were collected again for the notes. Numbers and Deuteronomy, drafted from
1738's read lines (decision 68), read each line once and built both texts from it. That route is now the route for
every Old Testament book still to do, Wikisource or not.

**Scope.** Phases 1–3 apply to the Old Testament books still to do and the Apocrypha (base 1738 for the Old
Testament; the Apocrypha's base to be decided with M7). The New Testament is finished; its route (Wikisource as the
working text, collated against 1573, which numbers its verses and has good OCR) is the one its review files record (e.g.
`data/review/mark6-16-stage2.md`) and is not repeated here. Joshua, begun on the other workstation before this,
was read line by line the same way (decision 68's route).

### Phase 1: Transcribe (the page read once)

**Fetch** (fully automatic, as before): Wikisource, archive.org (`_djvu.txt`, `_hocr.html`, page images on demand),
the 1726–27 OCR (`TXT/1 - OCR`), the parallel texts; cached under `sources/` (`python -m pipeline fetch all`).

**The voted lines.** `python -m pipeline lines BOOK CH --leaves A-B` (`ocrdraft.make_lines`; `lines --heads` lists
each leaf's running head and chapter headings, to find a book's leaves) turns 1738's hOCR into one row per printed
line (`leaf column line text`) in `data/witnesses/read-1738/<osis><chapters>.voted.tsv`: running heads, chapter
summaries (decision 67), signatures and catchwords taken off, margin numbers kept as verse starts (`#N`, 1750's
margins where 1738's are cut), each word repaired (long s read as f, rn for m …), and where no repair is a known
word, the word of 1750, Wikisource or 1726 at the same place (each aligned word by word, in that order).
- **Wikisource is one voter**, where it has the book, its word put in 1738's letters. It is never the base: in Judges
  it dropped clauses, respelled names and in places followed 1750 (`judg1-21-stage2.md`). Tried on Judges
  (2026-11-19, scored against the approved `text/orig/JDG.usfm`): the voted lines matched 82.2% of the printed words
  with it, 80.6% without; the words no witness could vote fell from 927 to 720.
- **Doubts**, `<osis><chapters>.doubts.tsv`: the places where two or more of the others agree on a word and the vote
  has another, for the readers to look at first. 1738 is never outvoted (1750 and Wikisource share readings 1738
  lacks: Judg 4:11 *Hobani* for 1738's *Hobabi*). In Judges, 217 doubts; at 132 of them the others had the printed
  word (OCR misreadings that are real words: *ilium*, *nee*, *habere*).
- `lines --sheets` draws the reading sheets (`ocrdraft.reading_sheets`) into `sources/archive/crops/sheets/lines/`.

**The reading.** Every line is read on the page image (`ocrdraft.reading_sheets`: each line's crop under its voted
text, several readers by leaf range, doubtful words enlarged). The read file, `<osis><chapters>.tsv`, holds the
words exactly as 1738 prints them (decision 58: spelling, u/v and i/j, æ and œ, capitals, punctuation, misprints,
word division; s for ſ, & and q; written out), the drop capital with its word, verse starts where the margin number
and the sense put them. `.corrections.tsv` records every row the reading changed. In the same pass the readers record:
- **paragraphs**: the indented lines. `orig --read-lines` takes 1738's indents from the hOCR (`archive.indents`); a
  reader marks one it misses, or one it finds that is not an indent, as a `¶` / `¶-` row in
  `data/decisions/<osis>.orig.tsv`. (Numbers and Deuteronomy were approved before their paragraphs were checked.)
- **footnotes and marks**: 1738's footnotes (as `%` rows, with the word they hang on) and Castellio's *L.* … *H.* and
  *G.* … *H.* marks, listed in the phase's summary as inputs for phase 2's notes, so the pages are not read again
  for them;
- **wording doubts**: a place where 1738 and 1750 differ in more than spelling, or where 1738 looks misprinted
  against the sense, is listed with both readings (the printed text keeps 1738; the edition's choice is phase 2's).
- **Omission check**: each verse against the BSB and the Vulgate for a clause the page has and the reading lost.

**Versify.** `python -m pipeline draft BOOK CH --from-ocr` makes `text/draft/<USFM>.usfm` from the read lines, and
`versify --draft` moves it to the KJV's numbering (`<osis>.draft.edits.tsv`; verse ranges where 1738 joins verses).

**The printed text.** `python -m pipeline orig BOOK CH --read-lines` builds `text/orig/draft/<USFM>.usfm` from the
same read lines (each verse's leaf in `data/orig/<osis>.pages.tsv`) and `data/review/<osis>-orig.md`.

**Gate 1.** One summary for Nathan, `data/review/<osis><chapters>-transcription.md`: how the lines were read (leaves,
readers, corrections), the wording doubts, the footnotes and marks found, the versification edits. On approval the
printed text moves to `text/orig/<USFM>.usfm`, never rewritten by code after that (decision 61). If phase 2 finds a
misreading, it is a proposal against `text/orig/` (applied with `review apply --to`), the read lines corrected with
it, and the draft rebuilt: the two texts never drift apart.

### Phase 2: Edit and annotate

The draft from the read lines is the edition's starting point. `python -m pipeline propose BOOK CH` (stages 3–5)
makes one review item per verse (`data/review/<osis><chapters>-chNN.md`) and the preview
`text/draft/<USFM>.preview.usfm`:

- **Normalize to Gaffiot 2016**: `data/rules/orthography.tsv` (approved rows only) and Gaffiot's headwords for words
  the rules don't cover, each new respelling a proposal; Cicero and the Golden Age first where spellings vary
  (decisions 18, 42); j wherever pronounced, æ and œ for every diphthong (decisions 16, 17).
- **Macronize**: Gaffiot decides stems and hidden quantities, Wiktionary and Macronizer the endings; homographs are
  decided in context from the syntax, the Hebrew (or Greek) and the English, into `data/decisions/<osis>.forms.tsv`.
- **Structure**: the BSB's paragraphs and poetry mapped onto the verses and adjusted to the Latin; quotation marks
  (“…” for speech, ‘…’ within it, reported speech unmarked; decisions 4, 25, 65); `\qt` for quoted Scripture; calls in
  `data/decisions/<osis>.layout.tsv`.
- **Names**: a names reader brings each name to the settled form or decides it once (`<osis><chapters>-names.md`).

**The notes, in parallel** (`ot-notes-process.md` §5): they depend only on the words, so they run beside the edit,
not after settlement. `python -m pipeline notes BOOK` writes the candidates; readers go through each chapter with the
Hebrew, the BSB, the NRSVue (read online, never stored) and the NET notes; phase 1's 1738 footnotes and Castellio's
marks, and his 1554 annotations on the book (read on the page), are among the candidates. Proposals go into
`data/review/<book>-notes.md` with Apply lines against the preview.

**Proofread**: independent readers who never saw the drafting reasoning (the critic) read the preview against the
BSB and the Vulgate for omissions, sense errors, odd macrons and quotation mismatches; their finds become items.

**Edition-wide slips** found on the way (a settled book with a form the new book decides otherwise, a rule that
over-applies) go into the running `data/review/edition-fixes-<date>.md`, not into the book's files.

**Gate 2.** One summary for Nathan, `data/review/<osis><chapters>-edition.md`: the points for him (names, layout calls
against the BSB, words that may be Castellio's slips, rules proposed), the notes proposed and those left out, the
proofreaders' finds. Under decision 30 ("approved for now"), Claude checks every flag with its evidence before
asking. On approval: `review apply` writes the items and the accepted notes, the chapters move into
`text/<USFM>.usfm`, `pipeline gold` rebuilds the answer key, the ledger goes to `settled`, the drafts are removed.

### Phase 3: Build and check (fully automatic)
- `python -m pipeline build` generates every output from `text/*.usfm` and `text/orig/*.usfm` (§4a) into `build/`.
- **Checks**: the USFM uses only the markers in §3 and every `\v` is in order; verse counts against the KJV map;
  `macron-check` over the whole text; unknown words; balanced quotation marks per verse; epubcheck; the PDF without
  overfull lines or missing glyphs; no settled chapter changed except through an approved decision; the tests
  (`python -m unittest discover -s pipeline/tests -t .`).

### The ledger

`data/status.tsv` keeps its stages. Phase 1 takes a chapter from `pending` to `corrected` (fetched, aligned, read,
versified); phase 2 from `normalized` through `in-review` to `settled`.

## 4a. Publishing

One master (`text/*.usfm`), several outputs, all generated:

| Output | How | For |
|---|---|---|
| **Website** | Static HTML from the USFM, published with GitHub Pages; replaces the WordPress site (which then points to it) | Reading online: a page per chapter, linkable verses (`…/matthaeus/14#3`), a button to show or hide macrons, and an optional public-domain English column (BSB or KJV) beside the Latin, already aligned by verse id |
| **EPUB** | Generated from the USFM (two editions: with and without macrons), checked with epubcheck; markup kept Kindle-friendly, following e-liber | E-readers; Kindle via Send-to-Kindle or KDP |
| **Print PDF** | USFM → generated LaTeX using your current memoir layout (A5, drop-cap chapter numbers, running heads, verse numbers), built with `latexmk`. Never edited by hand. SIL's **PTXprint**, which typesets USFM directly, is the fallback if the LaTeX route becomes a burden | Print-on-demand (Lulu, KDP paperback) and download |
| **Plain text and data** | TXT (with and without macrons) and per-verse TSV/JSON | Readers, researchers, other tools |
| **ebible.org** | Submit the USFM (CC BY-SA 4.0 qualifies) once the New Testament is complete | ebible.org generates its own HTML, EPUB and PDF and the formats Bible apps use (e.g. SWORD modules for AndBible and Xiphos), where readers can show this text beside other translations |

**Releases:** a tagged GitHub release at each milestone carries the PDF, both EPUBs and the TXT/TSV files, and redeploys the website. The first is v1.0 *Evangelia* (end of M2). The ebible.org submission follows *Novum Fœdus* (end of M3).

## 5. Claude skills and agents for this repo

Following fur-fulminis's layout (`.claude/skills/<name>/SKILL.md`, plus `CLAUDE.md`, `brief.md` and `HUMAN.md` at the root). *Not built as of 2026-11-19: the work has run from `CLAUDE.md`, the review files and Nathan's requests. If they are built, they follow §4's phases: one skill per phase (`/transcribe BOOK`, `/edit BOOK`, `/release`), the readers and the critic as agents.*

| Skill / agent | Does |
|---|---|
| `/prepare-chapter <BOOK.CH>` | Runs stages 0–5 for one chapter (or a range) and writes the review file |
| `adjudicator` agent | Stage 2 disagreements: reads the page-image crops and witnesses, returns a reading, confidence and evidence |
| `homographs` agent | Stage 4: decides homographs per verse from the Latin syntax plus Greek/Hebrew/English |
| `critic` agent | Stage 6 independent read; never sees the drafting reasoning |
| `/review-chapter` | Presents the queue, records your decisions, answers questions with evidence |
| `/approve <BOOK.CH>` | Applies decisions, writes the chapter's USFM, marks it settled, updates the ledger |
| `/release` | Builds every output (§4a), runs the checks, drafts the release notes; tagging and publishing wait for your go-ahead |
| `/distill` | Every ~10 chapters, proposes new rules for `orthography.tsv`, the names list and `brief.md` from what you accepted or rejected |
| `/status` | Ledger summary and what to do next |

Chapters are independent, so a book can be prepared **in parallel** (one agent per chapter) and reviewed one after another. Run time and token cost grow with the number of chapters, so run large batches when you choose to.

## 6. Proving it before trusting it

Before any new chapter is produced:

1. **Test harness.** Run stages 1–5 on the finished chapters (Gen 1–27, Mt 1–13, Mk 1–5, Lk 1–13, Jn 1–4), starting from Wikisource and the witnesses alone. Compare the output with the gold USFM converted from your LaTeX and measure:
   - word accuracy;
   - spelling accuracy;
   - macron accuracy (per vowel);
   - paragraph and quotation agreement.
2. **Tune** the rules and thresholds until the output matches your hand at ≥99.5% of words and ≥99% of vowels. The disagreements that remain should be ones you would want to see anyway.
3. **Matthew 14–28 as the pilot.** It is drafted but unchecked, and it has WordPress and Wikisource witnesses. Run the full pipeline on it and review every change (§8, decision 6), then compare with your draft. Auto-apply starts only after this.

## 7. Milestones

| # | Milestone | Content | Notes |
|---|---|---|---|
| M0 | Groundwork — **built 2026-11-05** | `pipeline/` package, fetchers, bridge to `lrl`, ledger, `CLAUDE.md`/`brief.md`/`HUMAN.md` | Uses `../fur-fulminis/data` in place (`LATIN_REF_HOME` to move it). Wikisource: 58 books, 15,997 verses; the Gospels match KJV numbering exactly; Genesis numbers verses differently in 2, 3, 4, 6, 7, 10, 18 |
| M1 | Calibrate | **Migrate the finished LaTeX to USFM** (shown lossless); rules learned from the finished chapters; test harness passing | §3, §6 |
| M2 | **Four Gospels** | Mt 14–28, Mk 6–16, Lk 14–24, Jn 5–21 (59 chapters); the publishing builds (website, EPUB, PDF, TXT; §4a) | Richest witnesses (Wikisource, WordPress, 5 OCRs); release v1.0 "Evangelia"; the website replaces WordPress |
| M3 | Acts & epistles & Revelation | 201 chapters | Wikisource is complete; 4–5 OCR witnesses; release "Novum Fœdus"; submit to ebible.org |
| M4 | Genesis 28–50, Exodus | Existing TXT work + Wikisource | Release "Pentateuchus I" |
| M5 | OT books on Wikisource | Leviticus, Judges, Ruth, Kings, Job, Esther, minor prophets, … | Fewer witnesses (1738 base, 1726–27, 1750). From 2026-11-19 (decision 85) read line by line on 1738's pages like M6, Wikisource one voter among the OCRs (§4, phase 1) |
| M6 | OT books *not* on Wikisource | Numbers, Deuteronomy, Chronicles, Psalms, Isaiah, Jeremiah, Ezekiel, Daniel, … | **No base text:** start from three OCRs voting (1738, 1726–27, 1750), with Claude reading the 1738 page images (decision 68; Numbers and Deuteronomy so). The same route as M5 since decision 85 |
| M7 | Apocrypha (in scope; decision 2) | Judith, Tobit, Wisdom, Sirach, Maccabees | Wikisource has some |

### 7a. Further work (added 2026-11-11, not scheduled)

Ideas Nathan has raised. None is started; each needs a decision on scope before work begins.

1. **Notes from modern scholarship: a very light touch** (Nathan, 2026-11-11). Done the way modern reader's Bibles
   do it, never changing Castellio's text: a passage absent from the earliest manuscripts is set in brackets with
   one short footnote (in Latin, e.g. *Hīc versus in antīquissimīs cōdicibus deest*); a rendering that rests on a
   reading now rejected gets one line giving the accepted sense (Matt 19:24 *rudentem*, “a ship's cable”, from
   κάμιλος for κάμηλος: a note that the Greek reads “camel”; the text keeps *rudentem*, as the base edition prints
   it, `data/review/matt14-28-stage2.md` item 5). No discussion, sigla, manuscript names or alternative
   translations in the notes; only the few places a reader would otherwise be misled (likely a few dozen in the
   whole Bible: the longer ending of Mark, John 7:53–8:11, the *Comma Johanneum* and similar, if his text has
   them). The evidence for each (e.g. NA28/UBS5, SBLGNT's apparatus, which is already a parallel source; BHS for
   the OT) goes in a review file, not in the edition. To decide: the wording of the standard notes; USFM `\f`
   footnotes (foot of the page in print, a marker on the site, left out of the plain text); and the README's
   statement that the edition has no notes.
2. **Castellio's text as printed, beside the reading edition.** Not kept today. What exists: the witnesses
   (`data/witnesses/`; Wikisource, which in Acts–Revelation prints his *early* wording, and noisy OCRs), the
   stage-2 corrections (`data/calibration/*-collation.tsv`, `data/review/*-stage2.md`), and the drafts in git
   history (a draft is deleted once settled). No file holds the corrected base text in its own spelling, and the
   chapters from the earlier manual work (Genesis 1–27, the Gospels' opening chapters) never had one. Proposed: a
   second layer, `text/orig/<USFM code>.usfm` (or a per-verse TSV), holding the base edition's words and spelling
   (1573 NT, 1738 OT) after stage 2 and before stages 3–5, with no macrons, Gaffiot spelling, modern punctuation or
   quotation marks, published as its own outputs (TXT, EPUB, and a switch on the site). **Spelling: Castellio's own,
   with abbreviations expanded** (Nathan, 2026-11-11): *&* → *et*, *q;* → *-que*, *ã* → *am*/*an*, long s → s; the
   printed spellings (*cœlum*, *caussa*, *quum*) kept; *u/v* and *i/j* as printed; no variants (1556's readings
   stay out of it); the printer's own paragraphs (Nathan, 2026-11-13, HUMAN.md decision 57). **Begun 2026-11-13**,
   now stage 2b of the pipeline (§4): `python -m pipeline orig` (`pipeline/orig.py`) builds it from the settled
   chapters, taking each word's spelling, capitals and punctuation from the base edition's OCR. Drafted the same
   day for every settled chapter: the whole New Testament from 1573 (about 99% of words read in the OCR or in
   1573's spelling of the same word elsewhere; the rest from the settled text, listed), and Genesis and Exodus 1–20
   from 1738 (about 93%; 1738's OCR is noisier). The early Gospel chapters (Matthew 1–13, Mark 1–5, Luke 1–13,
   John 1–4) were brought to 1573 by decision 27, so they are built the same way. Still to do: 1738's paragraphs (its
   indents, from the hOCR); the outputs (TXT, EPUB). **The New Testament approved 2026-11-13** (decision 61):
   `text/orig/<book>.usfm`, shown on the site by the *Edited text | As printed, 1573* choice (item 3).
3. **On the site, a switch between Castellio's spelling and the reading edition, replacing the macron switch**
   (Nathan, 2026-11-11). Builds on item 2: the reader toggles each chapter between the normalized text (Gaffiot
   spelling, macrons, modern layout and punctuation) and Castellio's text as printed (item 2's layer), the choice
   remembered as the macron switch's is today. The ā / a switch goes; the macron-free text stays in the downloads
   (the *sine macronibus* TXT and EPUB). Since the two texts differ in punctuation and layout, not only spelling,
   the switch swaps whole verses (the page carrying both, each verse id'd as now), not words; the verse anchors and
   the parallel view work in either. The printed text keeps its own paragraphs; the PDF stays the reading edition
   only (decision 57). **Built 2026-11-13**: a chapter page carries the printed chapter in two inert `<template>`s
   (the reading view's content with the same verse ids, and each verse's Latin for the parallel view). **Redesigned
   the same day** (Nathan asked for a better design than the first *ā / 1573* button): a pair of radio buttons under
   the chapter's title, *Edited text | As printed, 1573* (*1738* in the Old Testament), both always in view, the
   choice remembered (`spelling` in local storage); over the printed text a banner, *Castellio's text as printed,
   Basel 1573 · see the page · back to the edited text*, whose page link opens the 1573 page image at MDZ (each
   verse's canvas in `data/orig/<osis>.pages.tsv`, from `pipeline orig --pages`; 1738 has none yet); and the printed
   text in the Parallel menu (*Castellio 1573 (as printed)*), beside the edited text verse by verse. The ā / a button is gone. The
   site offers the printed text from `text/orig/` (approved); `build --printed-drafts` also takes `text/orig/draft/`,
   for a preview, so the drafts do not reach the published site before they are approved.
4. **Rewrite the README.** Make it more useful to a reader and better written: what the edition is and for whom,
   where to read or download it (the site, the releases), what was changed from the printed editions and why
   (spelling, macrons, layout; drawing on `docs/editions.md`), what is finished, how to cite it and how to report
   errors, with the project's history and the pipeline moved lower or into their own documents.
5. **More front matter, starting with the standalone New Testament** (Nathan, 2026-11-12). Today the PDF and EPUB
   open with only the title page, its colophon on the verso, and the list of books. To add, first in the *Novum
   Fœdus* edition: a short preface for the reader (what Castellio's translation is, and what this edition changes:
   spelling, macrons, layout, the light notes; from `docs/editions.md`), a note on the base texts (1573, with 1556 as
   reference), and possibly a page of abbreviations and conventions (brackets, footnote letters). To decide: the
   language (Latin, English, or both), and which pieces the whole Bible and the other partial editions share.

## 8. Decisions (taken 2026-11-05)

1. **Base edition:** the editions Wikisource follows (1760 NT, 1738 OT). *The NT part was replaced on 2026-11-06 (HUMAN.md decision 15): the NT base was Castellio's 1556 edition, with Wikisource as the working text. Later the same day (decision 24) it moved to the posthumous 1573 Basel edition (Perna, “from his last revision”; MDZ bsb10141277), the 1556 text revised further; 1556 stays the reference, its differing readings recorded as variants.* Other printings' differing readings are recorded as variants. Wording in the finished chapters (from 1726–27) that differs is proposed for review, never changed automatically.
2. **Apocrypha:** in scope, after the 66 books (M7); placement decided then. *Decided 2026-11-13 (HUMAN.md decision 55): a section of their own between the Testaments, in Castellio's order.*
3. **Chapter summaries:** included, as small italic headings under each chapter number, normalized and macronized like the text. *Reversed 2026-11-12 (decision 50): left out.*
4. **Quotation marks:** “…” for direct speech, ‘…’ only for quotes within it; reported discourse unmarked. About 33 reported passages in the finished chapters lose their ‘…’ (proposed for review).
5. **Versification:** KJV everywhere, with mappings recorded; Psalm titles unnumbered above verse 1.
6. **Review:** every change reviewed during the Matthew 14–28 pilot; the auto-apply policy (A1 macrons, two-witness corrections, approved spelling rules, 1-in-10 full read) starts once the measured error rate is acceptable.
7. **License:** CC BY-SA 4.0, crediting Wikisource and the scan libraries.
8. **Data location:** the fur-fulminis databases are used in place (`LATIN_REF_HOME` to move them).
9. **Master format:** USFM, one file per book in `text/`; every published format is generated from it (§4a). LaTeX becomes a generated print output, and editing in Overleaf ends.

## 9. Risks

- **Wikisource quality is unmeasured outside the books we checked.** It is labelled 25% proofread. The OCR collation exists to catch its errors, and the test harness measures how many get through.
- **The base New Testament (1573) is at MDZ** ([bsb10141277](https://www.digitale-sammlungen.de/en/view/bsb10141277?page=1)). Its hOCR finds 89–98% of the words and gives word boxes for cropping its IIIF page images, and it numbers the verses; but its 16th-century print (long s, *q;*, *ã*) still needs folding, and whether its changes from 1556 are Castellio's own or his posthumous editor's cannot be told from the print (`docs/editions.md`). The reference edition, 1556 on e-rara ([10281656](https://www.e-rara.ch/bau_1/content/titleinfo/10281656)), reads poorly (27–69% of words found). The 1758 archive.org scan, also with word boxes, is the second image (`data/calibration/scans.md`).
- **Differences between editions** can look like OCR errors. They are recorded as variants, never silently "corrected".
- **Noisy OCR** (1747, 1750) adds noise as well as votes. Weight witnesses by measured accuracy, not equally.
- **Homographs and hidden quantities** are where macron errors concentrate. The Greek-tense evidence and your WordPress decisions help, but the A2/B queue will still be the longest part of the review for a while.
- **Book-wide rules can over-apply** (a respelling that is right in one sense and wrong in another). Rules carry a scope (lemma or context), and `/distill` proposes them; it never adds them silently.
- **The Gaffiot license** limits redistribution, so the published edition must not contain Gaffiot text.
- **The USFM migration could lose layout detail** (unusual `\indentpattern`s, italics spanning poetry lines). The round trip (USFM → LaTeX compared with the original) catches it before the old files are retired.
- **The generated PDF must keep your current design.** The LaTeX generator reuses `LaTeX/main.tex`'s preamble unchanged (now `pipeline/templates/preamble.tex`); PTXprint is the fallback, not the plan.

## 10. First steps

1. ~~Settle the decisions in §8.~~ Done 2026-11-05.
2. ~~M0: scaffold `pipeline/`, write the Wikisource/WordPress/archive.org fetchers, and connect to `lrl`.~~ Done (3badc59).
3. M1 (in progress): migrate the finished chapters to USFM, learn the respelling and macron rules from them, and build the test harness.
4. Pilot on Matthew 14–28.
5. M2: the publishing builds (§4a) and release v1.0 *Evangelia*.
