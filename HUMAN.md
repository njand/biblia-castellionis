# For Nathan

## Now

- **One form of a name in both Testaments** (2026-11-11; decision 46, on your revisit of *Hagar*/*Agar*): Gal
  4:24–25 *Hagar* (as Genesis; Paul's Greek Ἁγάρ, the BSB, WEB, NRSV, ESV, NIV), Matt 24:37–38 *Nōæ*, *Nōa* (as
  Genesis and Luke); gold rebuilt for Gal and Matt; the rule is in `brief.md` for the books to come (*Elias*, *Esaias*
  when they come up). Record: `data/review/names-one-form.md`. This reverses section C's first point of
  `open-questions-paul.md`. Nothing committed.
- **The open questions from Galatians–Philemon are decided and applied** (2026-11-11; decision 45): you accepted
  every recommendation of `data/review/open-questions-paul.md`. Applied to the settled text: the 11 slips of
  `settled-fixes-galcol.md` and `settled-fixes-thessphm.md`, *Abrāhām-*/*Isaac-* in Matthew 1–13 and Luke 1–13 (18
  places), Phil 4:2 *Euodiam*, 2 Tim 4:13 *Pænulam* (and its rule); gold rebuilt for Matt, Luke, Acts, Rom, 1 Cor,
  Phil, 2 Tim. Kept as settled, with the evidence there: *Hagar*/*Agar* (1573 prints both), the greetings,
  *Servātor*, the Spirit's capitals, the verse and quotation calls. Tools: `versify --draft` relays the BSB's
  paragraphs on the new numbering, `mdz.fetch_crop` also saves the head of the next column, `propose` prints the
  quotation-mark check (with tests). Nothing committed.
- **1–2 Thessalonians, 1–2 Timothy, Titus and Philemon are settled** (2026-11-11; decision 44): approved by you "for
  now", in `text/1TH.usfm` (89 verses), `2TH` (47), `1TI` (113), `2TI` (83), `TIT` (46), `PHM` (25), every chapter at
  the KJV count; gold rebuilt, drafts and previews removed (`text/draft/` is gone). **Paul's letters are complete.**
  Record: `data/review/thessphm-stages3-5.md` (start here), the six `-stage2.md` files, `-chNN.md`, `data/decisions/`;
  the 1573/1556 differences in `docs/editions.md`. Calls of mine to check: the title lines (`\mt1` *Paulī Apostolī
  Epistola prior / posterior ad Thessalonīcēnsēs*, *… ad Tīmotheum*, as your *Epistola prior ad Corinthiōs*, where
  1573 heads them *Epistola prima / secunda*; *Epistola ad Titum*, *ad Philēmonem*); 2 Tim 3:4 (Castellio's L. … G.
  marks dropped, the words kept, as Matt 19:4). Not yet in a release or on the site.
- **Galatians, Ephesians, Philippians and Colossians are settled** (2026-11-11; decision 43): approved by you "for
  now", in `text/GAL.usfm` (149 verses), `EPH.usfm` (155), `PHP.usfm` (104), `COL.usfm` (95), every chapter at the
  KJV count; gold rebuilt (`data/gold/{Gal,Eph,Phil,Col}.tsv`), drafts and previews removed (`text/draft/` is empty
  and gone; a draft can be rebuilt with `pipeline draft`, `versify --draft --apply` and the stage-2 Apply lines).
  Record: `data/review/galcol-stages3-5.md` (start here), the four `-stage2.md` files, `-chNN.md`,
  `data/decisions/{Gal,Eph,Phil,Col}.*.tsv`, `data/versification/{Gal,Col}.draft.edits.tsv`; the 1573/1556
  differences in `docs/editions.md`. Calls of mine to check: the title lines (`\mt1` *Paulī Apostolī Epistola ad
  Galatās / Ephesiōs / Philippēnsēs / Colossēnsēs*, as 1573 heads them *Pauli Apostoli Epistola ad …*). **Still
  waiting on your Decision line**: `data/review/settled-fixes-galcol.md` (10 slips in the settled text, e.g. 1 Cor
  *līber* ×5, Matt 13:46 *comparet*; and two questions, *Abrahām-*/*Isaāc-* in your Gospels and *Hagar*/*Agar*). Not
  yet in a release or on the site; the Vulgate is not offered beside these books until its map is checked for them.
- **2026-11-08: the publishing builds for v1.0 *Evangelia* exist (M2), not yet released.**
  `python -m pipeline build Matt Mark Luke John --version v1.0` writes into `build/` (git-ignored): the website
  (`build/site/`), two EPUBs (with and without macrons; both pass epubcheck 5.4.0 with no errors or warnings), the
  print LaTeX (`build/pdf/castellio-evangelia.tex`: the preamble and `title.tex` in `pipeline/templates/`, body by
  `latex.to_latex`), and TXT with and without macrons, TSV and JSON (`build/txt/`). With no books named it builds
  everything in `text/`. Every verse of the five settled books comes out exactly as `data/gold` has it. **To look at:**
  - **The PDF** (`build/pdf/castellio-evangelia.pdf`, 128 A5 pages) compiles with Tectonic 0.17.0 (a one-file
    XeTeX; `build` uses `latexmk`, then `pdflatex`, then `tectonic`, whichever is on the PATH): 0 missing
    characters, 3 overfull lines (1–7 pt; Luke). For it the generated LaTeX adds, after your preamble: Latin
    hyphenation (`babel` classiclatin; without it 186 lines were overfull) and `\emergencystretch`; under XeTeX only,
    TeX Gyre Pagella (the free Palatino) and ȳ built as y + macron (Pagella lacks it). The colophon is on the title
    page's verso. Under pdfLaTeX your own fonts stay, but that route is untested here (no TeX Live/MiKTeX). As in the
    old LaTeX, the running head names the chapter at the foot of the page. The Tectonic used here sat in a temporary
    folder: install it (or TeX Live) to rebuild the PDF.
  - **The site:** `python -m http.server 8765 --directory build/site`, then `localhost:8765/matthaeus/21.html#16`.
    It has a macron switch (ā / a), a light/dark switch (Auto → Light → Dark) and a menu of texts to show beside
    the Latin verse by verse: KJV (1769), BSB, WEB, the Hebrew (WLC) or Greek (Textus Receptus) by testament,
    Septuagint (Brenton's Greek), Vulgate (Clementine), all public domain from eBible.org, moved to the KJV's
    numbering by `data/versification/<key>.map.tsv` (2026-11-11; `--parallel kjv,bsb,…|none`; `--sources
    ../sources` from a worktree). Since 2026-11-11 also: one font on every device (Gentium Book and Ezra SIL,
    subset into `pipeline/fonts/`), text-size buttons (A− A+), a book/chapter jump menu, a search page (words,
    "a phrase", or a reference such as *Mt 5:3-12*; `search.json`), verse selection (click a verse number;
    shift-click or "To verse…" for a range; the address takes `#3-7`, with a Copy link button) and a print
    layout. It shows only the books built, so the v1.0 site has no Genesis: do you want Genesis on the site from the start (it was on WordPress)?
  - **Wording for you to settle:** the colophon (English; `publish.credits`) names no editor; it says the NT follows
    1573 with 1556 as the reference (decision 24), as `README.md` now does too (2026-11-10). The release title is
    *Ēvangelia* and the files are `castellio-evangelia*`; TXT chapters are headed "Matthæus 14".
  - **Two fixes in `latex.py`:** a paragraph marker in the middle of a line (`… lēgistis? \q1 \qt …`, Matt 21:16)
    now starts a new block (it used to stop `to_latex`), and `\cd` (a chapter summary) / `\d` (a psalm title) print as
    `\Argumentum{…}` / `\Titulus{…}` above the drop cap. None of the Gospels has a `\cd` yet.
  - **Waiting on your go-ahead:** tagging the GitHub release and turning on Pages (no Pages workflow exists yet), and
    pointing the WordPress site at it.

- **2026-11-07 (overnight): the Matthew 14–28 pilot is through stages 2–5 and waits for your review.** Start
  with `data/review/MORNING.md`: what was built, the order to review in, the measured rates for decision 6, and
  what could not be verified. Five review files (`settled-fixes.md`, `matt14-28-stage2.md`, `-spelling.md`,
  `-macrons.md`, `-structure.md`) and a preview of the result (`text/draft/MAT.preview.usfm`). New tools:
  `python -m pipeline review check|apply` (applies accepted Apply lines), `versify --draft`, 1573 as an aligned
  witness (`ocr-1573`, L. … G. passages kept and flagged), and the stage modules `collate`, `normalize`,
  `macrons`, `structure`, and `draft`/`collate` commands. Mark 6–16 is through stage 2 only
  (`mark6-16-stage2.md`, on a new Wikisource-based `text/draft/MRK.usfm`); Acts was collated against 1573 as a
  report (`data/calibration/acts1573.md`). Nothing committed.
- **2026-11-05: all nine plan decisions taken** (below); `brief.md`, `PLAN.md` and `CLAUDE.md` updated to match.
  Decision 9 makes USFM the master copy: LaTeX becomes a generated print output and Overleaf editing ends.
- **M0 (groundwork) is done** (commit 3badc59). `python -m pipeline` fetches every witness and keeps the chapter
  ledger.
- **M1 (calibration) is in progress** in its own session. Step 1 (migration) is done and accepted, not yet committed:
  the 62 finished chapters (2,244 verses) are migrated to `text/GEN|MAT|MRK|LUK|JHN.usfm`, and Matthew 14–28
  to `text/draft/MAT.usfm`. Converting the USFM back to LaTeX matches your LaTeX token for token, except for
  two print changes you accepted (decision 10). The per-verse gold set is in `data/gold/`. **From now on, edit the
  USFM, not the LaTeX.** Step 2 (spelling rules) is drafted and awaits your review: `data/rules/REVIEW.md`.
  Genesis is renumbered to the KJV (decision 14): 774 verses, every chapter at the KJV count. Step 3 is done:
  the seven OCR witnesses are aligned to verse ids and scored (`data/calibration/witnesses.md`). The best is
  1758, which has 98% of your words and reads 96.6% of them the same. 1681 is weakest (75.7%). TXT/1 (1726–27)
  reads well (97.0%) but holds only 44% of the text. WordPress turns out to be Wikisource with macrons, so it is
  not an independent witness. Step 4 is done: the harness (`data/calibration/harness.md`) runs normalize and
  macronize from Wikisource and meets both targets when each chapter learns from the other chapters:
  99.76% words, 99.56% spelling, 99.26% vowels. It uses your *proposed* spelling rules: approving them is still
  your call. Step 5 is done (`data/calibration/scans.md`). Comparing the 1760 scan with Castellio's own 1551, 1554
  and 1556 editions led to decision 15: the New Testament base is **1556**, his last revision. In the Gospels,
  Wikisource and 1758 already follow it closely. In Acts–Revelation, Wikisource prints Castellio's *early* wording,
  with 1750 and 1760 (e.g. *favor*, *humanitas*, *synagoga*, *lavit*), which he revised in 1556 (*gratia*, *caro*,
  *collegium*, *baptizavit*). Stage 2 will propose roughly 80–100 such changes there (`data/calibration/nt1556.tsv`).
  The editions and their history are written up in `docs/editions.md`. Then the posthumous 1573 Basel edition
  (Perna, “from his last revision”) was found and collated: it revises 1556 further, and decision 24 makes it the
  NT base in 1556's place (`data/calibration/nt1573.tsv`).
  **M1 is complete and waits for your review**; the Matthew 14–28 pilot starts after that.

## Decisions waiting

- **Downloads on the site** (2026-11-11): the home page lists the EPUBs, PDF, plain text and data, rebuilt with
  every push (the Pages workflow now installs Tectonic and builds every format), and every page's footer links
  there. An untagged build is labelled with the last tag and the date ("v1.0+ (2026-11-11)"), since v1.0's
  release predates decisions 40–42. The release workflow fetches all the parallel texts for its copy of the site.
  The Vulgate's numbering is checked for the whole New Testament (Rev 12:18 → 13:1 the one shift).
- **Legacy files removed** (2026-11-11; decision 13 carried out): `LaTeX/biblia/` (the pre-migration Genesis and
  Gospels, out of date since decisions 40–42), `HTML/`, `EPUB/`, `TXT/4 - Macronized` and
  `scripts/latex_converter.py`, all in git history; `pipeline migrate` retired. `LaTeX/main.tex` and `title.tex`
  moved to `pipeline/templates/` (the PDF's preamble and title page). `TXT/1–3` stay: `align` and `collate` read
  them as witnesses (`TXT/3` is your 1726–27 Old Testament).
- **Spellings resolved** (2026-11-11; decision 42): the 108 places of `data/review/spelling-audit.md` applied, by
  Gaffiot 2016 and the corpus, Cicero and the Golden Age first (the evidence table is in the file): *cōntiō*,
  *condiciō*, *subolēs*, *multō*, *pænit-*, *erus*, *paulō*, *umquam*, *cāritās*, *sepulcrum*, *exspect-*,
  *undecumque*, *mæstus*, *vīcēsimus*, *sescentī*, *inaspectābilis*, *cotīdiē*, *cærimōnia*, *quotiēns*, *obœdiō*,
  *adulēscēns*. One judgment against Cicero's editions: *quidquam* kept with the brief's *quidquid* (the corpus's
  Cicero prints *quicquam*, *quicquid*); say if both should turn to *c*. Gold rebuilt; the 24 stem and word rules
  approved, so drafts in progress (Galatians–Colossians) take them at `pipeline propose`. Not yet on the site.
- ***cum* applied** (2026-11-11; decision 41): *quum*/*quumque* → *cum*/*cumque* in the 243 settled places (Gen
  28–50 47, Exod 57, Acts 70, Rom 27, 1 Cor 26, 2 Cor 16), by the Apply lines of `data/review/quum.md`; gold
  rebuilt; the rules `quum → cum`, `quumque → cumque` approved, so new drafts are normalized. Not yet in a release
  or on the site (both follow the next push to `main` or tag).
- ***quandoquidem* applied** (2026-11-11; decision 40): the o unmarked in the 21 settled places (Matt 3, Mark 1,
  Luke 5, John 4, Acts 1, Rom 1, 1 Cor 3, 2 Cor 3), by the Apply lines of `data/review/quandoquidem.md`; gold
  rebuilt, so new drafts take *quandoquidem* from the settled forms. Not yet in a release or on the site (both
  follow the next push to `main` or tag).
- **v1.0 released, and the website on GitHub Pages** (2026-11-10; decision 39): the colophon of every format now says
  *Edited by Nathan Anderson* (and the EPUB names you as editor in its metadata); `.github/workflows/pages.yml` builds
  the site on every push to `main` and on each release; `.github/workflows/release.yml` builds every format when a tag
  `v*` is pushed (EPUBs checked by epubcheck, PDF compiled by Tectonic) and publishes the release with `RELEASE.md` as
  its notes. Still waiting on you: pointing the WordPress site at `https://njand.github.io/biblia-castellionis/`.
- **2 Corinthians 1–13 is settled** (2026-11-10; decision 38): approved by you "for now", in `text/2CO.usfm` (257
  verses, the KJV count; the subscription as `\cls`), gold rebuilt (`data/gold/2Cor.tsv`), draft and preview removed.
  Record: `data/review/2cor1-13-stages3-5.md`, `-stage2.md`, `-ch01.md` … `-ch13.md`, `data/decisions/2Cor.*.tsv`,
  `data/versification/2Cor.draft.edits.tsv`, `data/calibration/2Cor1-13-collation.tsv`. One call of mine to check: the
  title lines (`\h`/`\toc2` *Ad Corinthiōs II*, `\mt1` *Paulī Apostolī Epistola posterior ad Corinthiōs*; 1573
  *Epistola secunda*, its argument *posteriorem*).
- **The open questions for the whole edition are decided and applied** (2026-11-10; decision 37): you approved every
  recommendation in my walkthrough. 462 changes to the settled text (`data/review/edition-fixes.md`, one item per word,
  each group with its evidence), `data/gold/` rebuilt for all nine books, 176 spelling rules added to
  `orthography.tsv` for future drafts, the two subscriptions set apart as `\cls` (now supported by every build), and
  `README.md` now names 1573 as the NT base. Romans now has paragraphs at 23 of the BSB's ordinary breaks, to match 1 Corinthians
  (`data/review/rom-paragraphs.md`, accepted by you and applied; 79 passed over, with reasons). The colophon, release and Pages
  questions are decided (decision 39).
- **1 Corinthians 1–16 is settled** (2026-11-10; decision 36): approved by you "for now", in `text/1CO.usfm` (437
  verses, the KJV count), gold rebuilt (`data/gold/1Cor.tsv`), draft and preview removed (`text/draft/` is now empty and
  gone). Record: `data/review/1cor1-16-stages3-5.md`, `-stage2.md`, `-ch01.md` … `-ch16.md`, `data/decisions/1Cor.*.tsv`,
  `data/versification/1Cor.draft.edits.tsv`. One call of mine to check: the title lines (`\h`/`\toc2` *Ad Corinthiōs I*,
  `\mt1` *Paulī Apostolī Epistola prior ad Corinthiōs*, on the pattern of Romans). Nothing committed.
- **Romans 1–16 is settled** (2026-11-09; decision 33): approved by you "for now", in `text/ROM.usfm` (433 verses, the
  KJV count), gold rebuilt (`data/gold/Rom.tsv`), draft removed. Record: `data/review/rom1-16-stages3-5.md`,
  `-stage2.md`, `-ch01.md` … `-ch16.md`, `data/decisions/Rom.*.tsv`, `data/versification/Rom.draft.edits.tsv`. Open for
  your review: the 16:27 subscription (in the verse, or set apart as `\cls`), and the early-line spellings Romans and Acts
  both keep (*caussa*, *adsp-*, *intellig-*). Nothing committed.
- **Acts 1–28 is settled** (2026-11-09; decision 34): approved by you "for now", in `text/ACT.usfm` (1,007 verses, the
  KJV count), gold rebuilt (`data/gold/Acts.tsv`), draft removed (it is in git). Record:
  `data/review/acts1-28-stages3-5.md`, `-stage2.md`, `-ch01.md` … `-ch28.md`, `data/decisions/Acts.*.tsv`,
  `data/versification/Acts.draft.edits.tsv`.
- **Exodus 1–20 is settled** (2026-11-09; decision 35): approved by you "for now", in `text/EXO.usfm` (545 verses, every
  chapter at the KJV count), gold rebuilt (`data/gold/Exod.tsv`), draft removed (it is in git). Record:
  `data/review/exod1-20-stages3-5.md`, `-stage2.md`, `-ch01.md` … `-ch20.md`, `data/decisions/Exod.*.tsv`,
  `data/versification/Exod.draft.edits.tsv`.
- **Applied 2026-11-09** (your decision): the nine markings the Acts and Exodus readers found wrong in your settled
  text, `data/review/settled-fixes-acts.md` (Gen 6:16 *contignātiōne*, Gen 37:4 *amīcē*, Luke 2:13 *repente*, Matt 4:24
  *Syriam*) and `settled-fixes-exod.md` (Gen 8:5 *mēnsis*, Gen 13:9 and Luke 21:23 *regiō*, Gen 22:14 *ā Jōvā*, Gen 24:8
  *religiōne*); `data/gold/` rebuilt for Genesis, Luke and Matthew.
- **The questions for the whole edition** at the end of each summary (1 Corinthians, Acts, Exodus, Romans, and
  Genesis's *Rachel*) are decided: decision 37.
- **Genesis 28–50 is settled** (2026-11-08; decision 32): approved by you "for now", in `text/GEN.usfm` (Genesis now
  1,532 verses; every chapter at the KJV count but 41, where 41:57 is absent in every printing), gold rebuilt, draft
  removed. Record: `data/review/gen28-50-stages3-5.md`, `-stage2.md`, `-ch28.md` … `-ch50.md`,
  `settled-fixes-gen.md`, `data/decisions/Gen.*.tsv`. Of your earlier work, **Exodus 1–20** (`TXT/3`) and **Acts 1–16** (`TXT/2`)
  are still to go through the pipeline; your in-depth review (decision 30) can begin alongside. One call for the whole edition: *Rachel*
  (your Matt 2:18) vs *Rāchēl-* in the other cases.
- **John 5–21 is settled** (2026-11-08; decision 31): approved by you "for now", in `text/JHN.usfm` (879 verses, the
  KJV count), gold rebuilt, draft removed. **All four Gospels are now settled** (Matthew 1,071, Mark 678, Luke 1,151,
  John 879 verses). Record: `data/review/john5-21-stages3-5.md`, `-stage2.md`, `-ch05.md` … `-ch21.md`,
  `data/decisions/John.*.tsv`. Genesis 28–50 followed (decision 32).
- **Luke 14–24 is settled** (2026-11-08; decision 30): approved by you "for now", in `text/LUK.usfm` (1,151 verses,
  the KJV count), gold rebuilt, draft removed. Record: `data/review/luke14-24-stages3-5.md`, `-stage2.md`,
  `-ch14.md` … `-ch24.md`, `data/decisions/Luke.*.tsv`. **Your in-depth review of everything settled since
  2026-11-07 comes later** (decision 30), while new transcription goes on.
- **Mark 6–16 is settled** (2026-11-08; decisions 28–29): every verse read; Mark 6 accepted by you, 7–16 by me
  under your delegation, with each fix recorded in the review log of `data/review/mark6-16-stages3-5.md`. The
  chapters are in `text/MRK.usfm` (678 verses, the KJV count), `data/gold/Mark.tsv` rebuilt, `text/draft/MRK.usfm`
  removed (the pre-stage-3 draft is in git; `data/review/mark6-16-ch*.md` reproduce every change). Also applied:
  `settled-fixes-matt.md` (Matt 27:37 *JŪDÆŌRUM*, 20:29 *Hierichūnte*, 22:44 *Sedē*, 19:10 *cōnūbia*). **For your
  read-through**: the calls I made without you are listed in that review log (4 spelling rules added to
  `orthography.tsv`, 2 code fixes, 2 forms); everything is uncommitted.
- **Applied 2026-11-07** (all review proposals accepted except the open items below): `settled-fixes.md` (10, to
  `text/LUK.usfm`, `GEN.usfm`, `JHN.usfm`; gold rebuilt); Matthew's 3 verse-number splits; `matt14-28-stage2.md`
  (29), `-spelling.md` (40), `-macrons.md` (12 items), `-structure.md` (25 items) to `text/draft/MAT.usfm`;
  `mark6-16-stage2.md` (24) to `text/draft/MRK.usfm` (Mark 6–16 now *corrected*). Matt 19:4 kept unmarked; the 4
  1556 variants recorded. Then *Rabbi* by Gaffiot's standard (Matt 23:7, 23:8, 26:25, 26:49) and the 3 BSB
  paragraphs (Matt 17:19, 18:19, 24:26).
- **Matthew 14–28 is settled** (2026-11-07; decision 26): every review item decided and applied, the chapters
  moved into `text/MAT.usfm` (chapters 1–13 untouched; 1,071 verses, the KJV count) and `data/gold/Matt.tsv`
  rebuilt; `text/draft/MAT.usfm` and `MAT.preview.usfm` removed (the draft is in git history).
- **Decision 6's threshold**: the Gaffiot stem step is fixed (2026-11-07: same-syllable rule, abbreviated endings
  not aligned, silent where the principal parts disagree); it is now wrong on 5 of 25 words (was 46 of 69).
  Lexicon-only macrons: 0.65% of words wrong; all: 1.63% (was 1.79%).
- **`data/review/settled-1573.md` applied** (2026-11-07, decision 27; all 46 accepted, `data/gold/` rebuilt): the settled NT chapters (Matthew 1–13, Mark 1–5, Luke 1–13,
  John 1–4) collated against 1573, every place read on the page image. 46 items: 22 words missing or wrong (Wikisource
  slips your text inherited: Luke 4:27 *pūrgātus et*, 6:12 *per nox*, 7:11 *proficīsceret*, 13:4 *quod* …), 21 different
  readings (Matt 6:4, 6, 18 *occulta*, 13:32 *holerum*, Luke 9:12 *dēversentur* …), **John 2:18 revised between 1556 and
  1573** (*Ēde nōbīs aliquod prōdigium …*), 2 forms (*tonitruī*, *sēminece*). Kept and listed: *tetrarchēs*,
  *assimulem*, *circumsedēret*, *abstergēmus*.
- **Possible follow-ups** (not started): chapter summaries (decision 3) are in neither draft nor settled USFM;
  the same collation for settled Genesis against the 1738 OCR (the OT base).
- **The spelling rules are decided** (2026-11-06, decisions 16–20; `data/rules/REVIEW.md` has the evidence).
  `orthography.tsv`: 114 rules approved, 12 rejected; three left for the names list (*Bennammi*, *Hierichūntem*,
  with *Henōchī/Enōchī* and *Abius*).
- **The fixes they imply are applied** (2026-11-06; `data/review/spelling-fixes.md`, all accepted): 128
  replacements in `text/*.usfm` (36 œ, 7 spellings, 27 perfects, 7 word divisions, 23 single fixes and Egypt
  capitals, 28 capitals for God); `data/gold/` rebuilt. The legacy LaTeX now differs from the USFM in these too.
- **Committed** (2026-11-07, 7083d31): the names, wording, 1573 and quotation-mark work. Next: the Matthew 14–28
  pilot's stage 2 (collation against 1573) and a review/apply tool.

## Decided

| # | Date | Decision |
|---|---|---|
| 1 | 2026-11-05 | **Base edition: the editions Wikisource follows** (1760 NT, 1738 OT; the NT part is replaced by decision 15). Other printings' differing readings are recorded as variants. Wording in the finished chapters (from 1726–27) that differs is proposed for review, never changed automatically. |
| 2 | 2026-11-05 | **Apocrypha: in scope, after the 66 books** (M7). Placement decided then. |
| 3 | 2026-11-05 | **Chapter summaries: included** as small italic headings under each chapter number, normalized and macronized like the text. |
| 4 | 2026-11-05 | **Quotation marks: “…” for direct speech, ‘…’ only for quotes within it; reported discourse unmarked.** About 33 reported passages in the finished chapters lose their ‘…’ (proposed for review). |
| 5 | 2026-11-05 | **Versification: KJV everywhere**, mappings recorded; Psalm titles unnumbered above verse 1. |
| 6 | 2026-11-05 | **Review: strict pilot, then relax.** Every change is reviewed during Matthew 14–28. The auto-apply policy (sources agree on audible macrons, two-scan corrections, approved spelling rules, with a 1-in-10 full read) starts once the measured error rate is acceptable. |
| 7 | 2026-11-05 | **License: CC BY-SA 4.0**, crediting Wikisource and the scan libraries. |
| 8 | 2026-11-05 | **Latin databases used in place** from `../fur-fulminis/data` (`LATIN_REF_HOME` to move them). |
| 9 | 2026-11-05 | **USFM is the master copy** (`text/<book>.usfm`). The website, EPUBs, print PDF (generated LaTeX in your current layout), TXT and an ebible.org submission are all built from it (PLAN.md §4a). Overleaf editing ends; the old LaTeX/HTML/EPUB/TXT folders retire once the migration is verified (removal is your call). |
| 10 | 2026-11-05 | **Migration accepted.** `text/*.usfm` is the master copy for the 62 finished chapters, with two print changes: the Benedictus's `\medskip` (Luke 1:75) becomes an ordinary stanza break, and Gen 15:18 gains a space before verse 19. |
| 11 | 2026-11-05 | **Genesis's commented-out notes dropped** (three draft headings, two footnotes); the printed chapter summaries cover the same ground. They remain in git history. |
| 12 | 2026-11-05 | **Genesis renumbered to the KJV in one batch**: chapters 3, 4, 6, 7, 10, 11, 14, 18, 23, 24, only verse numbers moving, approved once from a combined report of every moved boundary. |
| 13 | 2026-11-05 | **Old outputs retire when the M2 builds replace them.** `LaTeX/biblia/`, `HTML/`, `EPUB/`, `TXT/3–4` and `scripts/latex_converter.py` stay (frozen, legacy) until the new website/EPUB/PDF exist; `LaTeX/main.tex` and `title.tex` then move to the PDF template rather than going. |
| 14 | 2026-11-05 | **Genesis renumbering approved and applied** as proposed in `data/versification/Gen.REVIEW.md`: 11 moved boundaries, including chapter breaks mid-sentence at 6:22/7:1 and 7:24/8:1 (`\nb`), and the Septuagint's Caīnān (old 11:14–15) joined to 11:13. Words unchanged; every chapter at the KJV count. The legacy LaTeX now differs from the USFM only in these markers. |
| 15 | 2026-11-06 | **New Testament base: Castellio's 1556 edition** (Basel, Oporinus; e-rara 10281656), his last revision in his lifetime. Wikisource stays the working text. Where printings differ, the 1556 reading is proposed for review. The early wording (1551/1554 *homine natus*, *collegium*), Bünemann 1745, 1760 and the other printings are recorded as variants. 1758 serves as the page image where 1556 can't be cropped. Evidence: `data/calibration/scans.md` (Wikisource/1758 agrees with 1556 at 10 of 14 test places in the Gospels, 1760 at 4). The OT base (1738) is unchanged. *The NT base is replaced by decision 24 (1573).* |
| 16 | 2026-11-06 | **Ligatures: æ and œ for every diphthong**, as Gaffiot (*fœdus, cœpī, pœna, prœlium*); separate syllables stay apart (*Isrāēlīta, coēmptī, āer*). The ae → æ and oe → œ rules are approved. The 36 oe spellings in Genesis and Matthew 11–12 will be proposed as fixes to the USFM (REVIEW.md §5). |
| 17 | 2026-11-06 | **j wherever it is pronounced** (consonantal i → j, u → v), so always in compounds of *jaciō*: *abjiciō, ējicere, prōjiciō, dējicit, subjiciō*, not Gaffiot's *abiciō*. Your *eicere* (Mark 3:22) becomes a proposed fix to *ējicere*. *ŏbex, ŏbicis* keeps i, as Gaffiot's headword. |
| 18 | 2026-11-06 | **Spelling variants follow 1st-century-BC prose, Cicero above all**, by corpus counts (`pipeline latin attest --count`); where the counts are near even or too thin, the spelling most consistent with the other choices. First results: *iīs, umerus, harēna, sēscentī, erus, reppererit* (REVIEW.md §3). Where the corpus may reflect outdated editions, Gaffiot's headword wins (*quidquid*); where there is no 1st-century-BC evidence, the closest evidence or analogy (*pellicius*). |
| 19 | 2026-11-06 | **-īv- perfects follow republican prose form by form.** A form's own counts decide when clear (≥3 hits and 2:1); otherwise the pooled counts for its ending; where the form's thin evidence leans against the pool, it keeps its spelling. Result: 3rd sing. *-īvit* (128:11), *-īvimus*; short forms everywhere else (*audierat, audierit, audīsse, audīstis, petīsse*); the 3rd plural by verb (*audiērunt* 19:1, *petīvērunt* 20:7, *quæsīvērunt* 4:1). Compounds of *eō* and verbs without an -īvī perfect (*dēsinō, feriō, insiliō, dēsiliō*) are left out. 51 rules in `orthography.tsv`; 27 words of the settled chapters to be proposed (e.g. *petiit* → *petīvit* 5×, *audīvistis* → *audīstis* 5×). |
| 20 | 2026-11-06 | **Capitals for God: NRSV style.** *Pater, Fīlius, Spīritus Sānctus, Servātor, Suprēmus, Sānctus Deī* capitalized when they refer to God or Christ; *Fīlius Hominis*; adjectives (*Pater vester cælestis*) and pronouns lower case. Castellio's 1556 capitalizes only *Deus*, *Supremus* and *Sanctus Dei*, so this is a modern editorial choice (`docs/editions.md`). Decided per verse; about 15 fixes to the settled chapters to be proposed. |
| 21 | 2026-11-06 | **Enoch is *Henōchus* in both Testaments**: Hebrew חֲנוֹךְ has ḥet, Greek Ἑνὼχ the rough breathing, and the Vulgate writes *Henoch* in both. Castellio's NT *Enochus* (1556) is not followed. Luke 3:37 *Ēnōchī* → *Henōchī* and Gen 25:4 *Henochum* → *Henōchum* applied (`data/review/names.md`). |
| 22 | 2026-11-06 | **Names: Jericho, Benammi, Abius.** *Hierichūs, -ūntis* as in 1556 (rule *Hiericunt- → Hierichunt-* for Wikisource's Gospels); Gen 19:38 *Bennammi* → *Benammi* (1738, 1750, Wikisource; Hebrew *ben-ʿammî*), applied; *Abius* (Abihu) kept from the j rule (`JV_KEEP`). |
| 23 | 2026-11-06 | **Wording against Wikisource** (`data/review/wording.md`, 41 places): six changes applied where the printings agree against your text (Gen 7:14 *ālitum*, Mark 2:7 *Qui fit*, Mark 4:19 *cupiditātēs, quæ*, Mark 5:7 *Quid*, Mark 5:38 *collēgiī*; Luke 5:39 *pōtātō* was applied, then reverted to your *pōtō*, the classical participle: Cicero, *Brutus* 333 *eō pōtō*); Gen 11:25 keeps *ūndēvīgintī* over 1738's *novemdecim* (decision 18); the other 34 keep your text (Wikisource slips, or readings no printing has, such as the clause after Luke 11:7). *The Luke 11:7 clause turned out to be in 1556 and 1573 (marked L. … G.); added 2026-11-07 (item 10): `… tibi dare.’ Sī ille pulsāre persevērāverit,` with verse 8 starting* mihi. |
| 24 | 2026-11-06 | **New Testament base: the 1573 Basel edition** (Petrus Perna, *ex postrema recognitione*; MDZ bsb10141277; USTC 616558, VD16 B 2638), replacing 1556 in decision 15. It is the 1556 text revised further (some 30–60 word changes, e.g. Mark 6:6 *infidentiam*, John 14:30 *mundi*, 1 Tim 3:16 *carne*), and it is the text of your finished chapters, 1681, 1758 and Wikisource's Gospels. Its OCR finds 89–98% of the words, it numbers the verses, and its IIIF images can be cropped from the hOCR word boxes. Wikisource stays the working text; where it differs from 1573 (as in its early-line Acts–Revelation), the 1573 reading is proposed for review. 1556 stays the reference: its readings where 1573 differs are recorded as variants, like the early wording (1551/1554), Bünemann 1745, 1760 and the later printings. Luke 12:6 keeps *duōbus assāriīs* (1573). Evidence: `data/calibration/scans.md`, `nt1573.tsv`. |
| 25 | 2026-11-07 | **Quotation marks in the settled chapters** (`data/review/quotes.md`, all accepted): of the 167 passages in ‘…’, 80 are reported speech and lose their marks (70 statements and commands; 10 indirect questions, which also lose their question mark), two slips are fixed (Luke 12:18 “‘Hoc agam,’; Gen 24:47 ‘Bathūēlis), and the other 87 keep their marks. 87 replacements applied to `text/*.usfm`; `data/gold/` rebuilt. |
| 26 | 2026-11-07 | **Matthew 14–28 approved; perfect forms of *eō*, *-āstis*, *Rabbi*.** Every proposal in `data/review/matt14-28-*.md`, `settled-fixes.md` and `mark6-16-stage2.md` accepted except as follows. The perfect of *eō* and its compounds follows republican prose (Latin Library, `latin attest --count`): *-iī* (27:0 against *-īvī* in the compounds), *-iit*, *-iērunt*, and contracted *-īstī/-īstis/-īsse/-īssent* (no *-iistī/-iisse/-iissent* at all), so Matt 25:25 keeps *iī* (1573 *iui*) and Mark 14:48 keeps *existis* (1573 *exijstis*), as Matt 11:8–9 *exīstis*. First-conjugation *-āvistis/-āstis* is near even in Cicero (9:12), so the edition's consistency decides: *-āstis* (Matt 25:36 *vīsitāstis*, = 1573). *Rabbi* unmarked, Gaffiot's form. The 3 BSB paragraphs added (Matt 17:19, 18:19, 24:26). Evidence in `matt14-28-spelling.md` group 6. |
| 27 | 2026-11-07 | **The settled NT chapters follow 1573 where it and the printings agree against them** (`data/review/settled-1573.md`, all 46 accepted, every place read on the 1573 page image): 22 Wikisource slips (Luke 4:27 *est*, 6:12 *pernox*, 7:11 *proficīscerētur* …), 21 readings (Matt 6:4, 6, 18 *occulta*, 13:32 *holerum*, Luke 9:12 *dēversentur* …), 2 forms (*tonitruī*, *sēminece*), and John 2:18 in Castellio's 1573 revision (*Ēde nōbīs aliquod prōdigium …*; 1556 recorded as a variant). Kept: *tetrarchēs* (Gaffiot, Cicero), *assimulem*, *circumsedēret*, *abstergēmus*. |
| 28 | 2026-11-08 | **Mark 6–16, stages 3–5: the per-verse review's open questions** (`data/review/mark6-16-stages3-5.md`). Decision 6's unflagged tier adds homographs that WordPress 2019 chose and your settled forms mark alike (0.28% wrong, as lexicon-only macrons' 0.26%). The 22 macrons decided in context are accepted as a batch; the three BSB paragraphs moved off mid-sentence (12:12 *Igitur*, 12:37 *Cumque*, 14:26) are accepted; 7:11 (only the man's words in ‘…’), 7:19 (*expūrgāns omnēs cibōs* inside the speech), 8:28 (the accusative answer as speech) and 11:31 (the deliberation ends before *Sīn*) stay as proposed. Quoted Scripture: Isa 66:24 in `\qt` at 9:44, 46 and 48; the commandments at 10:19 in `\qt` with ‘…’; Gen 1:27 at 10:6 and the allusion at 8:18 also in `\qt` with ‘…’ (unlike your Matt 19:4). The three Matthew slips are to be proposed as fixes. Each chapter's verses still wait on its Decision line. |
| 29 | 2026-11-08 | **Mark 6–16 settled under delegation.** After accepting Mark 6 you asked me to go through the rest "very carefully, examining the evidence for each point", apply my recommendations and record each change; you will read the whole text later and can override then. Every verse of Mark 7–16 was read with its evidence and accepted; fixes made on the way: spelling rules *quenquam → quemquam*, *sepe → saepe* (the hedge), *Genezarethanum → Gennezarethanum*, *Bethpage → Bethphage*; the long prefix before *j* in compounds of *jaciō* (*ējicere*, *trājēcit*, as your text 50 of 50); a verse-start capital kept for names your text never lowers (*Pīlātus*); 10:1 *convenit*, 15:34 *sabachtanī*; Matt 19:10 *cōnūbia* (corpus and Gaffiot), with your three Matthew fixes. |
| 30 | 2026-11-08 | **Luke 14–24 approved for now; review later.** Stages 1–5 as for Mark (17 stage-2 slips read on the 1573 images; 491 verses, 29 macrons decided in context, 252 layout lines) settled in `text/LUK.usfm`. Standing rule: the chapters you transcribed earlier are taken through the pipeline, every flag and verse checked by me with its evidence, and settled on your approval; your in-depth review of the whole comes after they are all done, while new transcription goes on. Everything stays reviewable (`data/review/`, `data/decisions/`). |
| 31 | 2026-11-08 | **John 5–21 approved for now; the Gospels are complete.** Stages 1–5 as for Luke (21 stage-2 corrections read on the 1573 images, 3 of them the base edition's forms *lōtum*, *tonitru*, *lōtus*; 28 macrons decided in context; 392 layout lines) settled in `text/JHN.usfm`. A discourse running over a chapter break is left open, as your Matt 5:48 → 6:1 (John 9:41, 14:31, 15:27). Your in-depth review follows decision 30. |
| 32 | 2026-11-08 | **Genesis 28–50 approved for now.** The first Old Testament run: Wikisource collated against 1738 (the base), 1750 and your 1726 text; 61 stage-2 corrections, mostly read on the 1738 page images; 41:57 recorded as absent (every printing ends chapter 41 at 41:56); Castellio's *G.* … *H.* marks at 44:6 dropped, the words kept (as Matt 19:4); 791 macrons decided in context and 221 layout lines; your Gen 25:33 *Jūrā*; three spelling rules (*adjutus*, *abjudicabitur*, *quattuordecim*). Settled in `text/GEN.usfm`. Open for your review: *Rachel* vs *Rāchēl-*. Your in-depth review follows decision 30. |
| 33 | 2026-11-09 | **Romans 1–16 approved for now.** Stages 1–5 as for Acts (93 stage-2 corrections against 1573 read on the page images, most of them Castellio's revision of Wikisource's early wording: *humanitas → caro*, *vitiositas → peccatum*, *sacer → sanctus*, 9:5 *Etiam*, 7:14 *emancipatus*; 17 versification edits to the KJV; 92 layout lines, 440 forms decided in context) settled in `text/ROM.usfm`. With it: the collation's edge and f/s checks and the j rule for *major* (with tests). Your in-depth review follows decision 30. |
| 34 | 2026-11-09 | **Acts 1–28 approved for now.** Stages 1–5 (225 stage-2 corrections against 1573 read on the page images, most of them Castellio's revision of Wikisource's early wording: *synagoga → collegium* 23×, *templum → fanum*, *baptismo lavit → baptismate baptizavit*; 31 versification edits; 391 layout lines, 1,111 forms) settled in `text/ACT.usfm`. The fixes to the settled text it proposed (`settled-fixes-acts.md`) are not part of this approval. Your in-depth review follows decision 30. |
| 35 | 2026-11-09 | **Exodus 1–20 approved for now.** Stages 1–5 (120 stage-2 corrections against 1738; 18 versification edits, Castellio's numbering in 5–7 to the KJV's; the Song of the Sea as poetry; 120 layout lines, 692 forms) settled in `text/EXO.usfm`. The fixes to the settled text it proposed (`settled-fixes-exod.md`) are not part of this approval. Your in-depth review follows decision 30. |
| 36 | 2026-11-10 | **1 Corinthians 1–16 approved for now.** Stages 1–5 (97 stage-2 corrections against 1573 read on the page images, 3 of them long-s slips found by a sweep of the draft's *f* words; 7 versification edits, the KJV's 3:23 split from 3:22 and 11:1 moved back to 10:33's *Imitatores mei estote*; 77 layout lines, 410 forms) settled in `text/1CO.usfm`. Its questions for the whole edition stay open (summary, end). Your in-depth review follows decision 30. |
| 37 | 2026-11-10 | **The open questions for the whole edition, as recommended** (`data/review/edition-fixes.md`, 462 changes, applied). Spelling: *causa* (Cicero 1,974 : *caussa* 3), *intelleg-* (157 : 35), *exsp-* kept, *temptō* (198 : 61; not *tentōrium*, nor John 20:23 *tenta*), *Jōhannēs* in Acts as in the Gospels; *ad-* assimilated as in your own chapters (*allocūtus* 54 : 0, *ascendō* 30 : 0), except compounds of *sum* (*adsunt*, *adsit*, *adfuit*), *adnūntiō* and the names. Macrons by Gaffiot: *vēsc-*, *īnfēst-*, *custōs*, *lōcusta*, *narrō*, *Ādamus*; *Rāchēl* as its other cases (16 nominatives, not the one counted earlier); *obdormiērunt* (third plural by verb, decision 19); Romans *Quīn etiam*, *perēmptī*, *īnsitīciī*. Hebrew names marked only where Gaffiot or a Latin source gives the length. Kept as settled: Acts 28:26's three levels of quotation marks, *Saūlem*. Layout: a letter's subscription set apart as `\cls` (Rom 16:27, 1 Cor 16:24, and the letters to come); the BSB's ordinary paragraph breaks taken where the Latin allows, as in 1 Corinthians; Romans given 23 to match (`rom-paragraphs.md`, accepted). README: the NT base is 1573. |
| 38 | 2026-11-10 | **2 Corinthians 1–13 approved for now.** Stages 1–5 (45 stage-2 corrections against 1573 read on the page images, 1 found by the f/s sweep: 4:4 *infidentium*; 2 at 2:13 in verses 1573's OCR had not aligned; 2 versification edits, 13:13 split from 13:12 and 7:16 from 7:15; 45 layout lines, 254 forms; the subscription as `\cls`) settled in `text/2CO.usfm`. With it: `verses.lower_start` keeps *Deus* capital at a verse start (with a test). Your in-depth review follows decision 30. |
| 39 | 2026-11-10 | **Named words in quotation marks; the collation's coverage check; the editor named; v1.0 and Pages.** Words named rather than spoken take quotation marks, as modern editions do (2 Cor 1:17–20 *“etiam”*, *“nōn”*, *“ita”*; already so in your Matt 5:37 and 1 Cor 14:16). `collate` now lists the verses the base witness covers under 60% (kind `uncovered`), to be read by hand. Every colophon says *Edited by Nathan Anderson*. The release is tagged v1.0 and the website is published with GitHub Pages (workflows in `.github/workflows/`). |
| 40 | 2026-11-11 | ***quandoquidem*, the o unmarked.** The attested classical quantity is short (every dactylic line: Lucretius, Catullus, Vergil, Ovid, Manilius, Juvenal); the long ō is the etymological *quandō* + *quidem*. As Gaffiot 2016. Applied to the 21 settled places (`data/review/quandoquidem.md`). *sīquidem* stays as Gaffiot heads it. |
| 41 | 2026-11-11 | ***cum*, not *quum*.** The conjunction as Gaffiot 2016 heads it, as Matt–John and Gen 1–27 already wrote it; *quumque* → *cumque*. Applied to the 243 places the Wikisource drafts kept *quum* (`data/review/quum.md`); rule approved in `orthography.tsv`. |
| 42 | 2026-11-11 | **Spelling by Gaffiot and the corpus, Cicero and the Golden Age first.** The 108 places the rules missed (`data/review/spelling-audit.md`): *cōntiō, condiciō, subolēs, multō, pænit-, erus, paulō, umquam, cāritās, sepulcrum, exspect-, undecumque, mæstus, vīcēsimus, sescentī, cotīdiē, cærimōnia, quotiēns, obœdiō, adulēscēns*; *quidquam* with the brief's *quidquid*. Word rules reach only the forms they were learned from, so the pipeline takes stem rules now; 24 approved. |
| 43 | 2026-11-11 | **Galatians, Ephesians, Philippians, Colossians approved for now.** Stages 1–5 (164 stage-2 corrections against 1573 read on the page images, most of them Castellio's revision of Wikisource's early wording: *favor → gratia*, *fiducia → fides*; clauses Wikisource lost at Gal 2:16, Eph 2:2, Col 1:16, 3:16, Phil 3:12; two versification edits, Gal 5:23 split at *lenitas* and Col 3:26 → 4:1; 115 layout lines, 448 forms; the hymn of Phil 2:6–11 as verse; the subscriptions as `\cls`) settled in `text/GAL|EPH|PHP|COL.usfm`. With it: 21 spelling rules under decision 37, and fixes to `align` (a superscript digit) and `collate` (a clause each OCR misspells differently), with tests. Your in-depth review follows decision 30. |
| 44 | 2026-11-11 | **1–2 Thessalonians, 1–2 Timothy, Titus, Philemon approved for now.** Stages 1–5 (112 stage-2 corrections against 1573 read on the page images, most of them Castellio's revision of Wikisource's early wording: *favor → gratia*, 1 Tim 3:16 *in carne*, Titus 3:10 *Sectarium*; words moved to the KJV's verse boundaries at 1 Thess 5:16–18, 1 Tim 1:3–4 and 4:12–13, Titus 3:5–6; 72 layout lines, 366 forms; 1 Tim 3:16 and 2 Tim 2:11–13 as verse; *Servātor* capital throughout; the subscriptions as `\cls`; 2 Tim 3:4's L. … G. marks dropped as Matt 19:4) settled in `text/1TH|2TH|1TI|2TI|TIT|PHM.usfm`. With it: 25 spelling rules (decision 37's *ad-*, *tempt-*, *intelleg-*; *neglegō*, *exstinguō*, *Silvānus*, *adjūtor*). Paul's letters are complete. Your in-depth review follows decision 30. |
| 45 | 2026-11-11 | **The open questions from Galatians–Philemon, as recommended** (`data/review/open-questions-paul.md`, all accepted, applied): the 11 settled-text slips (1 Cor *līber* ×5, Matt 13:46 *comparet*, Luke 7:5 *īdemque*, Acts 21:8 *Ēvangelistæ*, Luke 1:47 *Servātōre*, Rom 10:6 *dīxerīs*, Matt 12:26 *Satanam*); *Abrāhām-* and *Isaac-* throughout (your Gospels' 13 + 5 brought to the majority, 159 : 13 and 85 : 5); *Euodia* (1573, Gaffiot, as every *Eu-* name); *pænula* (Gaffiot, decision 42). Kept: *Hagar* in Genesis and *Agar* in Galatians, as 1573 prints them; *Grātiam* capital only where the greeting opens its verse; *Servātor* capital everywhere; the Spirit capital where set against flesh or acting; L. … G. marks dropped (2 Tim 3:4, as Matt 19:4); *Epistola prior / posterior*. Tools: paragraphs relaid after versification, crops of carried-over lines, the quotation check in `propose`. |
| 46 | 2026-11-11 | **One form per person in both Testaments, the Old Testament's.** Modern translations use one form (BSB, WEB, NRSV, ESV, NIV *Hagar* in Galatians; only the KJV keeps the Greek forms); Paul's Greek has Ἁγάρ; decision 37 already spelled names one way across books. Applied: Gal 4:24–25 *Agar* → *Hagar*, Matt 24:37–38 *Nōē* → *Nōæ*, *Nōa* (`data/review/names-one-form.md`); `brief.md` (Proper names) has the rule. Replaces decision 45's *Hagar*/*Agar* point. |

## How to run

```
python -m pipeline fetch all        # once; downloads are cached in sources/ (≈260 MB)
python -m pipeline status
python -m pipeline status Matt --chapters
```
