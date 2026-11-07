# Overnight run, 2026-11-07: what is waiting for you

> **Done the same day** (decision 26): every file below was decided and applied, Matthew 14–28 is settled in
> `text/MAT.usfm`, and `text/draft/MAT.usfm` and `MAT.preview.usfm` are gone. Kept as the record of the run. The
> Gaffiot stem step was fixed afterwards: 5 of 25 wrong (was 46 of 69).

Nothing is committed and nothing settled was written. `text/*.usfm` and `text/draft/MAT.usfm` are unchanged. One
review file was touched: `wording.md` item 5 gained a `Decision:` line (see "Built", point 1). Every proposal is in a review file with exact **Apply** lines, all checked to
match once. The four Matthew files compose in order on a working copy, and the result is
**`text/draft/MAT.preview.usfm`**: Matthew 14–28 as it would be if you accepted everything. Tests: 78 pass
(`python -m unittest discover -s pipeline/tests -t .`).

## Recommended order

1. **`settled-fixes.md`** (10 items, 5 minutes). Three findings in your settled chapters, below under
   "Surprises". Apply with `python -m pipeline review apply data/review/settled-fixes.md --write`.
2. **`matt14-28-stage2.md`** (wording, 29 changes + 3 verse-number splits). Do **group 1 first**: set the three
   rows of `data/versification/Matt.draft.edits.tsv` to `approved`, then
   `python -m pipeline versify Matt --draft --apply`. Every Apply line uses KJV verse numbers, so it matches
   only after that. Then fill in the Decision lines and run `review apply … --write`.
3. **`matt14-28-spelling.md`** (42), then **`-macrons.md`** (18 lines), then **`-structure.md`** (41 lines),
   each applied after the one before. Read `MAT.preview.usfm` alongside: it shows the result.
4. **`mark6-16-stage2.md`** (25): Wikisource's slips in Mark 6–16 (*res* for *rex*, *quod* for *quos*,
   *insultum* for *insulsum* …), against a new stage-1 draft, `text/draft/MRK.usfm` (Wikisource with the
   BSB's paragraphs). Stages 3–5 for Mark are not done.
5. **Reports, no decisions needed:** `data/calibration/acts1573.md` (Acts, Wikisource against 1573),
   `data/calibration/quotes-check.md` (29 quotation candidates in the settled chapters, 4 of them in
   `settled-fixes.md`), `data/calibration/witnesses.md` (1573 now scored).

A dry run is the default: `python -m pipeline review apply FILE` shows what would happen, and `--write` applies.
Items can be accepted by number (`--items 3 7`) whatever the Decision line says.

## What each review file holds

| File | Items | By kind |
|---|---:|---|
| `matt14-28-stage2.md` | 3 + 29 (+1 note, 4 variants) | **Verse numbers**: 3 lost inside quotations (15:7, 22:31, 22:42; Matthew 15 and 22 were 1–2 verses short of the KJV). **Wording**: 29, every one read on the 1573 page image (canvas given). 7 are words missing from your draft (18:33 *et*, 21:3 *statim*, 22:17 *ergō*, **23:39 *nōn***, 24:15 *vāte*, 25:22 *talenta*, 28:2 *dē*). 5 are slips (19:5 *es-se*, 24:30 *Āctum* for *Ac tum*, 24:32 *congnōscitis*, 25:11 *reliquiæ*, 25:27 *com*). 16 are different words or forms (16:21 *eundum*, 17:11 *īnstaurātūrus*, **19:24 *rudentem***, 19:26 *Quōs*, 22:21 *quæ*, 22:35 *lēgis perītus*, 26:34 *Et*, 26:54 *cōnfierent*, 26:57 *abdūxērunt*, 27:8 *Ideōque*, 27:37 *Posuerant*, 27:47 *eōrum … dīcēbant*, 27:55 *fuerant*, **28:1 *septiduī***, 28:7 *illīc*). 1 is word order (24:43). **Matt 19:4 L. … G.**: keep *hominem* unmarked, as Luke 10:1 and 11:7 (nothing to apply). **Variants**: 4 where 1556 differs from 1573 (15:13, 17:9, 18:14, 25:40). |
| `matt14-28-spelling.md` | 42 | 12 æ/œ (*coepit → cœpit*); 9 approved rules (8 *-īv-* perfects, *Hierichunte*); 1 word division (*male dīxerit*); **17 capitals for God** (16 *pater → Pater*, *fīlius → Fīlius*; 26:41 *Spīritus → spīritus*, the human spirit); 1 consistency (*Barabam*); 2 your call (25:25 *iī → īvī*, 25:36 *vīsitāvistis → vīsitāstis*); plus a table of 15 spellings kept where the printings differ, with the reason for each |
| `matt14-28-macrons.md` | 13 (18 lines) | 7 against lexicon and Gaffiot (*dēfetīscantur, frustōrum, didrachma, statērem, fūstibus, intrōgressus*); 5 against your settled forms (*Simōn, congenuclāns, congenuclantēs, Abrāhāmī, Isaacī*); 1 your call (*Rabbī/Rabbi*, 4 places); 50 pipeline errors kept as you wrote them, tabulated |
| `matt14-28-structure.md` | 28 (41 lines) | 4 quotation marks out of balance; 3 reported speech in ‘…’ (decision 4: 21:3, 23:16, 23:18); 10 inline `\qt` for quoted Scripture (the draft had **no `\qt` and no poetry at all**); 8 poetry passages in your settled style (15:8–9, 21:5, 21:16, 21:42, 22:44, 24:29, 26:31, 27:9–10), with `\m` after them; 3 paragraphs where the BSB has one and the draft does not (your call) |
| `mark6-16-stage2.md` | 25 | 22 Wikisource slips that 1573 and the other printings correct (13 read on the page image, 9 from 1573's clear OCR plus other printings); 3 more (15:46 *ad*, 16:8 *metuerent*, 14:48 *exiistis*, the last your call) |
| `settled-fixes.md` | 10 | 5 *jūris perītus → lēgis perītus* (Luke 10–11); 1 *baptizandus → baptīzandus* (Luke 12:50); 4 quotation marks the wrong way round (Luke 8:45, Gen 16:10, 21:10, John 4:17) |

## What was built

1. **`python -m pipeline review check|apply FILE… [--write] [--items N…] [--all] [--to COPY]`**
   (`pipeline/review.py`, 11 tests). It parses the Apply lines and the Decision lines (group or item; *accept*,
   *accept 1, 3–5*, *accept all except 4*) and scopes each replacement to its verse. A paragraph or poetry
   marker just before `\v` belongs to that verse, so `\v 13 Eō` → `\p \v 13 Eō` adds a paragraph. Whitespace
   matches across line breaks, and markers in `new` start their own lines. All or nothing; an item already
   applied is recognized and skipped; data/gold is rebuilt after writing. All four earlier review files check
   clean (every item reported as already applied). One fix to them: `wording.md` item 5 (*pōtātō*, reverted
   by item 8) now has its own `Decision:` line, so that `apply` cannot re-apply it.
2. **1573 as a witness** (`pipeline/mdz.py`). The hOCR is read in block order, without the narrow
   marginal-note blocks. The OCR's *lesus* is read as *Iesus*, *atq ;* as *atque*, and the nasal bar it reads
   as an acute (*horú*) as *horũ*. Crops come from the IIIF image (whole lines, via PowerShell), cached in
   `sources/mdz-1573/crops/`. `python -m pipeline align` now includes `ocr-1573`, whose rows run from one
   printed verse number to the next. Scored on your settled Gospels: **94.5% found, 86.9% exact, 94.3%
   f/s-blind, 95.4% reading; verse numbers 1348/1363**. `scripts/collate_1573.py` uses the new module.
3. **The aligner keeps L. … G. passages and flags them** (`L…G: words` in the flags column; the marks are taken
   out of the text, and OCR variants *I./J./C.* are recognized). Checked: **Luke 11:7** now keeps
   *si ille pulsare perseveraverit* in 1573, 1758 and 1750 (before, 1750 and 1758 lost it). **Luke 10:1** and
   **10:17** (*duos*, *duo*) are flagged in 1573 and 1758, and 10:17 also in 1681. A new mark turned up in your
   settled text, **Matt 8:18** *iussit L. discipulos G. traijcere* (1573 canvas 755, page image; 1758 OCR).
   Your text has it unmarked, as decided for the others. The other witnesses' scores moved by 0.1% at most.
4. **Stage 2** (`pipeline/collate.py`): every witness aligned to the draft verse by verse. Differences are
   sorted into reading, form, spelling or division, and into 1573 with others, 1573 alone, others without 1573,
   or noise. Also **`versify --draft`** (edits in `<osis>.draft.edits.tsv`) and **`versify --to COPY`** (a
   working copy). A split now drops a verse number left in the text.
5. **Stage 3** (`pipeline/normalize.py`): the approved rules word by word, with macrons from your settled form
   of the new word, and safeguards (no *j* in forms of *eō* or Greek *-ia-* names; no phrase rule across a
   comma). It also lists candidates for capitals for God.
6. **Stage 4** (`pipeline/macrons.py`): re-marks a macronized text and lists the differences with evidence.
   `rates()` measures the error rate for each way a mark was decided (below).
7. **`python -m pipeline draft BOOK CH-CH`** (stage 1: Wikisource's chapters as a draft USFM with the BSB's
   paragraphs; never overwrites) and **`python -m pipeline collate BOOK CH-CH [--base draft|settled|wikisource|FILE]`**
   (stage 2: writes `data/calibration/<osis><CH-CH>-collation.tsv`, every non-noise place sorted).
8. **Stage 5** (`pipeline/structure.py`): paragraphs and poetry against the BSB, and a quotation-mark checker
   that knows your conventions (a speech reopened at each paragraph, *“‘* where a quoted block begins, nesting
   to three levels).

Rebuild the preview at any time:

```
cp text/draft/MAT.usfm text/draft/MAT.preview.usfm
python -m pipeline versify Matt --draft --to text/draft/MAT.preview.usfm
python -m pipeline review apply data/review/matt14-28-stage2.md --all --to text/draft/MAT.preview.usfm --write
```

Then the same for `-spelling.md`, `-macrons.md` and `-structure.md`, in that order.

The four Matthew files match only in sequence, after the renumbering. Checked on its own against today's draft,
each reports "missing" lines. To check them all at once, without writing anything, run `review check` on a
renumbered copy:

```
cp text/draft/MAT.usfm /tmp/check.usfm
python -m pipeline versify Matt --draft --to /tmp/check.usfm
python -m pipeline review check data/review/matt14-28-stage2.md data/review/matt14-28-spelling.md data/review/matt14-28-macrons.md data/review/matt14-28-structure.md --to /tmp/check.usfm
```

Tonight: 130 ok.

## Measured rates (for decision 6's auto-apply threshold)

**Harness, settled chapters, from Wikisource** (`data/calibration/harness.md`; unchanged tonight): variant D
reaches 99.76% words, 99.71% spelling, **99.25% vowels**, 98.28% of words fully marked right. Both targets are
met.

**Macron error rate by how the mark was decided** (`macrons.rates()`, settled chapters, gold spelling, each
chapter marked from the other chapters' forms):

| Decided by | Words | Words wrong | Vowels wrong |
|---|---:|---:|---:|
| lexicon (one W/M form) | 25,905 | **0.71%** | 0.29% |
| WordPress chose among a homograph's forms | 7,586 | 2.85% | 1.34% |
| your settled forms (≥ 80%) | 532 | 6.4% | 2.2% |
| WordPress alone (unknown to the lexicon) | 425 | 23.8% | 7.5% |
| homograph left undecided | 80 | 31% | 11% |
| **Gaffiot changed the W/M stem** | 69 | **67%** | 19% |
| unknown | 30 | 53% | 24% |
| all | 34,627 | 1.79% | 0.78% |

**On the Matthew 14–28 draft** (which you macronized yourself): the pipeline agrees with your marks on
**99.26% of words** (67 of 9,051 differ). Of the 67, 13 are your slips (proposed), 4 are your call (*Rabbī*)
and 50 are the pipeline's errors (kept). If the pipeline's marks had been applied automatically, they would have
fixed 13 words and broken 50.

**Wording**: of the ~4,700 places where some OCR differs from the draft, 29 were real, all of them confirmed on
the page image. About 3,800 were one OCR's misreading and were not read. Of the ~680 where only 1573's OCR
differed, the few that looked like real words were read on the image: 3 proved real, because 1573's OCR had
garbled a word the other printings had right (21:3 *statim*, 24:32 *cognōscitis*, 25:27 *cum*), and the rest
were misreadings or marginal references.

**The preview, collated again** (`python -m pipeline collate Matt 14-28 --base text/draft/MAT.preview.usfm`):
only 4 places remain where 1573 and another printing agree on a different reading, and all 4 are deliberate:
*accubitiōnēs* (decision 18), *audīstis* and *quæsīsset* (decision 19), and *prūdēns* (1573's OCR *prudẽs* is
the same word abbreviated). Before tonight's files there were 30.

My reading: an auto-apply tier for **lexicon-only macrons** (0.7% of words wrong) and **approved spelling rules**
(no false proposals tonight once the safeguards were in) looks defensible with your 1-in-10 full read. **Gaffiot
stem changes must not be auto-applied** until that step is fixed: 46 of 69 were wrong, e.g. *crucifīgō →
crucīfīgō*, *stantēs → stāntēs*. That looks like a bug in `macronize.gaffiot_stem`, not a property of Gaffiot.
Wording corrections need the image read regardless.

## Surprises

- **Matthew 14–28 seems to have been drafted from Wikisource (or WordPress, which is Wikisource with
  macrons)**, since it agrees with Wikisource against every printing at most of the 29 places. So it inherits
  Wikisource's slips (1726–27 was not checked for these chapters): 23:39 loses its *nōn* (“ye shall see
  me”), 25:22 loses *talenta*, and 22:17 *ergō* and 21:3 *statim* are missing too.
- **Wikisource has *juris peritus* where every printing has *legisperitus*, and your settled Luke followed it**
  five times (decision 23 compared against Wikisource and could not see this). Proposed in `settled-fixes.md`.
  A stage-2 collation of the settled chapters against 1573 would likely find more of the same kind:
  `collate.collate(osis, chapters, "settled")` does it. Not run tonight.
- Castellio's own words come back where the draft has the Vulgate's or Wikisource's: **19:24 *rudentem***
  (the cable, not the camel) and **28:1 *septiduī*** (*septiduum*, unknown to every lexicon here).
- The draft has **no italics for quoted Scripture and no poetry**; your settled Matthew has 67 `\qt` and 61
  poetry verses.
- Your settled Luke 12:50 *baptizandus* (no macron), and 29 quotation-mark candidates in the settled chapters,
  4 of them certain.

## What I could not verify

- **1556** readings are cited from its OCR only (it reads poorly); the four recorded variants were not read on
  the e-rara images.
- **Acts** (`acts1573.md`) is OCR only: no page image was read; counts are approximate.
- Two crops were inconclusive and left alone: 28:8 *illæ* (1573 looks like *ille*) and 20:15 (whether 1573 has
  *ideo*: the line breaks before it).
- Poetry line breaks and the reported-speech calls are my readings of the Latin, to be checked.
- Macrons of the new words from stage 2 are from the lexicon; *septiduī*'s stem is unmarked (no source).
- **Mark 6–16: only stage 2 was done.** Stages 3–5 start from Wikisource's unmarked text, so stage 4 would mark
  every word (about 10,000) and stage 5 would place every quotation mark (Wikisource has none). That needs a
  review format other than one Apply line per word: perhaps one line per verse, with the uncertain words
  listed. Not attempted tonight. In `mark6-16-stage2.md`, 10 of the 25 rest on 1573's clear OCR plus other
  printings, not the page image.
- **Chapter summaries** (decision 3): neither the draft nor the settled USFM has them; 1573 prints them.
