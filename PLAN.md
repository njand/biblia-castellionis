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

The ~62 finished chapters are a **test set**: the pipeline is run on them and scored against your hand-made results before it is trusted on new chapters.

## 2. What we have

### 2.1 Text sources for Castellio

| Source | Coverage | State | Role |
|---|---|---|---|
| This repo, LaTeX | Gen 1–27, Mt 1–13 (+ 14–28 drafted), Mk 1–5, Lk 1–13, Jn 1–4 | Finished: Gaffiot orthography, macrons, paragraphs, quotes, poetry | **Gold standard** and test set; never rewritten |
| This repo, TXT | Gen 28–35 macronized; Gen 36–50, Ex 1–20 edited; Acts corrected (partly) | In progress | Inputs for those chapters |
| This repo, `TXT/1 - OCR` | Gen–2 Kings + Ruth; all of the NT | Raw Google Books OCR of 1726–27 (the finished chapters' source) | One more OCR witness |
| [WordPress site](https://bibliasacracastellionis.wordpress.com/) | Mt 1–28, Mk 1–16, Lk 1–24, Jn 1–21, Gen 1–35 (Gen 34 has no macrons) | Macronized, one verse per line, old spelling (*ae*, *coepit*), no quotation marks | **Macron witness** (your earlier decisions) |
| [la.wikisource: *Biblia Sacra interprete Sebastiano Castellione*](https://la.wikisource.org/wiki/Biblia_Sacra_interprete_Sebastiano_Castellione) | All 27 NT books; nearly complete Genesis, Judges, Ruth, 1 Kings, Job, Esther, Judith, Tobit, Wisdom, Song, minor prophets; partial Exodus (461/1213 verses), Leviticus, Joshua; stubs for Numbers, Deuteronomy, Chronicles, Psalms, Isaiah, Jeremiah | Clean, versified, with chapter summaries; marked "25%" (not proofread). NT from the 1760 edition, OT from 1738 | **Base text** wherever it exists |
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

**Not yet available anywhere:** automatic OCR correction; respelling from 16th-century to Gaffiot orthography; writing æ/œ; LaTeX output. Section 4 covers these.

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
- **The LaTeX stays the published master.** The pipeline writes a chapter's LaTeX once, when the chapter is approved. After that the chapter is `settled`, and the pipeline only *checks* it and never rewrites it, so you can keep editing in Overleaf. The current converter then produces TXT/HTML/EPUB as it does now.
- **A chapter ledger** (`data/status.tsv`, as in fur-fulminis) records each chapter's stage: `pending → fetched → aligned → corrected → normalized → macronized → structured → in-review → approved → settled`.

The old `TXT/1–4` stage folders become outputs only. `TXT/3` and `TXT/4` stay as generated reading copies; `TXT/1` and `TXT/2` are replaced by `data/`.

## 4. The pipeline

Each stage is a Python command (`python -m pipeline <stage> <book> [chapters]`, standard library plus `rapidfuzz` for alignment). Where a stage needs judgment, it pairs with a Claude skill. The unit of work is a chapter.

### Stage 0: Fetch (fully automatic)
- **Wikisource:** wikitext per book through the MediaWiki API → verse TSV. Chapter summaries are kept as verse 0.
- **WordPress:** chapter pages → verse TSV, saved as the macron witness.
- **archive.org:** `_djvu.txt`, `_hocr.html` and `_page_numbers.json` for each item. Page images are downloaded only when a dispute needs them, cropped to the word box from hOCR.
- **Google Books 1726–27:** the existing `TXT/1 - OCR` files, plus a fetch for books not yet downloaded.
- **Parallel texts:** KJV, BSB and WEB (USFM), Clementine Vulgate, SBLGNT and OSHB, cached in `sources/parallel/`.
- Everything is cached under `sources/` (git-ignored, with a manifest of URLs and checksums) so runs can be repeated.

### Stage 1: Align (automatic, with flags)
- Wikisource is versified, so it is the backbone.
- Each OCR witness is cleaned (ſ→s, broken words rejoined, running heads and catchwords removed, `&`→*et*, `q;`→*que*, the *ã* abbreviation expanded). Its verse numbers serve as anchors, and it is aligned to the base word by word using folded forms (lower case, i/j, u/v, æ→ae, *f*≈*s*).
- **Versification check:** each chapter's verse count is compared with the KJV. Merged or split verses (as found in Genesis 3, 11 and 24) are listed for a decision, recorded once in the mapping file.
- **Omission check:** Claude compares each verse with the BSB and Vulgate and flags any verse missing a clause the others have. This catches lines an OCR or the Wikisource transcriber skipped.

### Stage 2: Correct by collation (mostly automatic; Claude reads the image when witnesses disagree)
For each word of the base text:
- **All folded witnesses agree** → accept.
- **The witnesses differ only in spelling** → stage 3 handles it.
- **Two or more independent witnesses agree against the base** → a correction is proposed. Once the pilot has measured the error rate (§8, decision 6), it is applied automatically when the word is in the lexicon.
- **The witnesses split, or the reading is unknown to Lewis & Short / `macron`** → **Claude adjudicates** with:
  - the word cropped from two page images (hOCR coordinates),
  - the verse in context,
  - the Vulgate and Greek/Hebrew for sense,
  - `lrl attest` for usage.

  The result is a proposal with a confidence level.
- **A genuine difference between editions** (not an OCR error) → recorded as a variant. The base edition's reading stands (1760 NT, 1738 OT; §8, decision 1), and every variant is listed for review.

Expected load: Wikisource's Gospels differ from your finished text on ~0.5–0.7% of words, and much of that is normalization. Genesis runs ~4% (more OCR noise from 1738). That works out to roughly **5–25 real decisions per chapter**, nearly all of them resolved automatically.

### Stage 3: Normalize to Gaffiot 2016 (mostly automatic)
- **Learn the rules from your finished chapters.** Compare Wikisource with your LaTeX (macrons removed) for all ~62 finished chapters and list every respelling you made: *tentato→temptato*, *concionaretur→contionaretur*, *humeris→umeris*, *conditione→condicione*, *quicquid→quidquid*, *quatuor→quattuor*, *eis→iis*, *trigesimo→tricesimo*, *ejicere→eicere*, splitting and joining (*me cum→mecum*, *septimodecimo→septimo decimo*), capitals (*pater→Pater* for God), and so on.
  - These become `data/rules/orthography.tsv` (`old	new	scope	note`), the fur-fulminis format. The policy behind them goes into `brief.md` § Orthography.
- **Generalize with Gaffiot.** Every word not covered by a rule is looked up in `lrl macron`. If Gaffiot's headword or principal parts spell it differently (*cœlum*→*cælum*, *accerso*→*arcesso*), the change becomes a proposal. Once you approve it, it is added to the table and applies throughout the Bible ("decide once").
- **Consonantal j/v** follows e-liber's `orthography.jv` rules. **æ/œ ligatures** are written for diphthongs, with the diaeresis-style exceptions you use (*aër*, *poëta*) kept in a short exceptions list. This rewrite is new code; e-liber does the opposite.
- **Punctuation and capitals:** capitals for divine names (*Pater*, *Spīritus Sānctus*) and modern punctuation habits, taken from the same comparison with your finished text and applied by rule where they are mechanical.

### Stage 4: Macronize (mostly automatic; Claude decides homographs)
- Run e-liber's Orthographer logic, adapted to this repo's paths, so that **Gaffiot decides stems and hidden quantities** and W/M decide endings. Where they disagree, it is flagged, as in fur-fulminis.
- **Extra witnesses:**
  - **Your WordPress macrons** for the Gospels and Genesis 1–35: where the pipeline's choice differs from them, it is flagged.
  - **Your finished chapters:** every form you settled becomes a book-wide default.
- **Homographs** (*venit/vēnit*, *legit/lēgit*, *-a* nominative/ablative, *hic/hīc*, *populī/pōpulī*…) are decided by Claude from the syntax. The **Greek tense or case** of the parallel verse is the strongest evidence (aorist → *vēnit*), and the BSB English the next. Decisions go into `decisions.yaml` `forms:` per verse.
- **Checks:** `lrl macron-check --text` on the result, then `lrl macron-triage`. **A1** (audible, sources agree) is applied automatically; **A2/B/G** go to the review queue; **C** (names) is decided once in a names list for the whole Bible (*Jēsūs*, *Ābrahāmus*, *Capharnaum*).

### Stage 5: Structure (automatic transfer, with Claude adjusting)
- **Paragraphs:** BSB paragraph breaks (`\p`) are mapped onto verse IDs, then compared with your finished chapters to calibrate. You split paragraphs somewhat differently, so the pipeline learns where you merge or split.
- **Poetry:** BSB `\q1`/`\q2` lines and indents become `\begin{verse}` with your `\indentpattern{…}`. Line breaks *inside* a Latin verse are placed by Claude at the matching clause.
- **Quotations:** BSB/WEB quotation spans tell us *who speaks where*. Claude then places “…” around direct speech and ‘…’ around quotes within it, respecting *inquit* insertions. Reported discourse is left unmarked (§8, decision 4).
- **Italic Old Testament quotations** (your `\emph{}`) come from the BSB cross-reference and quotation markup plus the Vulgate.
- The output is the chapter's LaTeX, in the same form as your current files.

### Stage 6: Review (where your time goes)
- **Critic pass:** a separate Claude agent reads the finished chapter against the BSB and Vulgate. It never sees the earlier stages' reasoning (fur-fulminis' `critic`). It flags omissions, sense errors, OCR leftovers, odd macrons and quotation mismatches, each with an exact `old → new`.
- **Queue:** all open items for the chapter go into `data/review/<osis>.<chapter>.md` in insula-thesauraria's proposals format, **lowest confidence first**:
  - each item shows current text → proposed text, the category, the evidence (the witnesses, a link to the page image, the Gaffiot/L&S result), a confidence level with its reason, and an empty `Decision:` line;
  - each has an exact `Apply:` replacement, checked to match exactly once.
- **Auto-applied changes** are listed at the bottom of the same file ("applied without review"), so they can be audited at any time.
- **Sampling:** one chapter in ten (chosen at random) is also read in full by you, to measure the error rate of what the pipeline applied automatically. If the rate goes up, the auto-apply thresholds go down.
- `/approve` applies the decisions, writes the chapter's LaTeX, marks it `settled`, updates the ledger and `HUMAN.md`, and leaves the commit to you.

### Stage 7: Build and check (fully automatic)
- The existing converter → TXT/HTML/EPUB; LaTeX → PDF (latexmk locally, or Overleaf).
- **Checks** (`python -m pipeline check`):
  - verse counts against the KJV map;
  - `macron-check` over the whole text;
  - a list of unknown words;
  - balanced quotation marks per verse;
  - epubcheck (from `../e-liber/.tools`);
  - no settled chapter changed except through an approved decision.
- A tagged GitHub release (PDF + EPUB) at each milestone.

## 5. Claude skills and agents for this repo

Following fur-fulminis's layout (`.claude/skills/<name>/SKILL.md`, plus `CLAUDE.md`, `brief.md` and `HUMAN.md` at the root):

| Skill / agent | Does |
|---|---|
| `/prepare-chapter <BOOK.CH>` | Runs stages 0–5 for one chapter (or a range) and writes the review file |
| `adjudicator` agent | Stage 2 disagreements: reads the page-image crops and witnesses, returns a reading, confidence and evidence |
| `homographs` agent | Stage 4: decides homographs per verse from the Latin syntax plus Greek/Hebrew/English |
| `critic` agent | Stage 6 independent read; never sees the drafting reasoning |
| `/review-chapter` | Presents the queue, records your decisions, answers questions with evidence |
| `/approve <BOOK.CH>` | Applies decisions, writes the LaTeX, marks the chapter settled, updates the ledger |
| `/distill` | Every ~10 chapters, proposes new rules for `orthography.tsv`, the names list and `brief.md` from what you accepted or rejected |
| `/status` | Ledger summary and what to do next |

Chapters are independent, so a book can be prepared **in parallel** (one agent per chapter) and reviewed one after another. Run time and token cost grow with the number of chapters, so run large batches when you choose to.

## 6. Proving it before trusting it

Before any new chapter is produced:

1. **Test harness.** Run stages 1–5 on the finished chapters (Gen 1–27, Mt 1–13, Mk 1–5, Lk 1–13, Jn 1–4), starting from Wikisource and the witnesses alone. Compare the output with your LaTeX and measure:
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
| M1 | Calibrate | Rules learned from the finished chapters; test harness passing | §6 |
| M2 | **Four Gospels** | Mt 14–28, Mk 6–16, Lk 14–24, Jn 5–21 (59 chapters) | Richest witnesses (Wikisource, WordPress, 5 OCRs); release v1.0 "Evangelia" |
| M3 | Acts & epistles & Revelation | 201 chapters | Wikisource is complete; 4–5 OCR witnesses; release "Novum Fœdus" |
| M4 | Genesis 28–50, Exodus | Existing TXT work + Wikisource | Release "Pentateuchus I" |
| M5 | OT books on Wikisource | Leviticus, Judges, Ruth, Kings, Job, Esther, minor prophets, … | Fewer witnesses (1738 base, 1726–27, 1750) |
| M6 | OT books *not* on Wikisource | Numbers, Deuteronomy, Chronicles, Psalms, Isaiah, Jeremiah, Ezekiel, Daniel, … | **No base text:** start from three OCRs voting (1738, 1726–27, 1750), with Claude reading the 1738 page images. Slower; benefits most from the rules settled by then |
| M7 | Apocrypha (in scope; decision 2) | Judith, Tobit, Wisdom, Sirach, Maccabees | Wikisource has some |

## 8. Decisions (taken 2026-11-05)

1. **Base edition:** the editions Wikisource follows (1760 NT, 1738 OT). Other printings' differing readings are recorded as variants. Wording in the finished chapters (from 1726–27) that differs is proposed for review, never changed automatically.
2. **Apocrypha:** in scope, after the 66 books (M7); placement decided then.
3. **Chapter summaries:** included, as small italic headings under each chapter number, normalized and macronized like the text.
4. **Quotation marks:** “…” for direct speech, ‘…’ only for quotes within it; reported discourse unmarked. About 33 reported passages in the finished chapters lose their ‘…’ (proposed for review).
5. **Versification:** KJV everywhere, with mappings recorded; Psalm titles unnumbered above verse 1.
6. **Review:** every change reviewed during the Matthew 14–28 pilot; the auto-apply policy (A1 macrons, two-witness corrections, approved spelling rules, 1-in-10 full read) starts once the measured error rate is acceptable.
7. **License:** CC BY-SA 4.0, crediting Wikisource and the scan libraries.
8. **Data location:** the fur-fulminis databases are used in place (`LATIN_REF_HOME` to move them).

## 9. Risks

- **Wikisource quality is unmeasured outside the books we checked.** It is labelled 25% proofread. The OCR collation exists to catch its errors, and the test harness measures how many get through.
- **The base New Testament (1760) is scanned only on Google Books** ([FsdIAAAAcAAJ](https://www.google.com/books/edition/Novum_Jesu_Christi_testamentum_ex_Sebast/FsdIAAAAcAAJ)), not archive.org, so it has no hOCR word boxes. M1 checks whether its page images can be fetched for stage 2. If not, the closest archive.org NT (1758) stands in when Claude compares a reading against the page.
- **Differences between editions** can look like OCR errors. They are recorded as variants, never silently "corrected".
- **Noisy OCR** (1747, 1750) adds noise as well as votes. Weight witnesses by measured accuracy, not equally.
- **Homographs and hidden quantities** are where macron errors concentrate. The Greek-tense evidence and your WordPress decisions help, but the A2/B queue will still be the longest part of the review for a while.
- **Book-wide rules can over-apply** (a respelling that is right in one sense and wrong in another). Rules carry a scope (lemma or context), and `/distill` proposes them; it never adds them silently.
- **The Gaffiot license** limits redistribution, so the published edition must not contain Gaffiot text.

## 10. First steps

1. ~~Settle the decisions in §8.~~ Done 2026-11-05.
2. ~~M0: scaffold `pipeline/`, write the Wikisource/WordPress/archive.org fetchers, and connect to `lrl`.~~ Done (3badc59).
3. M1: learn the respelling and macron rules from the finished chapters and build the test harness.
4. Pilot on Matthew 14–28.
