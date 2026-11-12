# What remains before the New Testament is ready for publication

Drawn up 2026-11-12 (Claude), after v2.0, at Nathan's request. Done items stay listed, struck through, so the list
records how the edition was finished.

## Decisions waiting on you (2026-11-12, see the conversation's report)

- [x] ~~Write *se ipsum*, *tē ipsum*, *mē ipsum* as two words (10 places), with word rules for future drafts.~~ (decision 51)
- [x] ~~*epistula* for *epistola* (24 places in the text, plus 42 title lines), with a stem rule.~~ (decision 51)
- [x] ~~Compounds of *eō* with *-iērunt*/*-iit*: 2 John 7 *introiērunt*, Exod 16:27 *exiērunt*, Acts 15:41 *obiit*,
  plus a rule.~~ (decision 51)
- [ ] Book titles: one capitalization convention, and one structure for every book.
- [ ] Book titles: a smaller line (`\mt2`) for the descriptive part. This needs build support in the site, EPUB and
  PDF.
- [ ] Brackets around passages not in the earliest manuscripts: the policy, the list, and the form (see below).
- [ ] Notes: whether to have them, their scope, and their form. The builds print no notes now (`latex.py` drops
  footnotes, and the USFM has none).

## The text

- [ ] **Your in-depth review** (decision 30) of everything approved "for now": Matthew 14 – Revelation 22. Each
  batch's record lists its "Calls worth a look" and the uncertain items.
- [ ] **Doubtful passages**: each of these is in the text as Castellio printed it, following the Greek of his day.
  Decide whether to bracket each one, and add a one-line note on brackets in the front matter.
  - Matt 6:13b (the doxology), 17:21, 18:11, 23:14
  - Mark 7:16, 9:44, 9:46, 11:26, 15:28, 16:9–20
  - Luke 17:36, 22:43–44, 23:17, 23:34a
  - John 5:3b–4, 7:53–8:11
  - Acts 8:37, 15:34, 24:6b–8a, 28:29
  - Rom 16:24
  - 1 John 5:7–8 (already in Castellio's parentheses)
- [ ] **Light notes on translation**, if wanted. Candidates so far:
  - Matt 19:24, Mark 10:25 and Luke 18:25 *rudentem* ("rope"). Castellio follows the reading κάμιλος, where the
    Greek text now read has κάμηλος, "camel".
  - The readings kept against the Greek because 1573 and 1556 agree: Jude 6 *Deī*, 1 John 4:4 *nōbīs*, 1 Pet 5:8
    *noster*.
  - Rev 3:1, the verse Wikisource lacks.

  A full list needs a reading of the text against modern critical scholarship; each note to be one line.
- [ ] **Rom 16:20 and 16:24 *favor***: the only *favor* left in the NT, where 1573 elsewhere revised it to *gratia*.
  Check both on 1573's page.
- [ ] **A sweep for other spellings like *seipsum***: joined words (*idipsum*, *nihilominus*) and other variant
  spellings the rules haven't met, using the corpus's classical tier as decisions 19 and 42 did.
- [ ] **Words no lexicon knows**: run `latin macron-check` over the whole NT and review what's left (each batch
  decided its own; the whole text has never been checked at once).

## Front matter and apparatus

- [ ] An introduction: Castellio, his Bible, the editions (`docs/editions.md`), and what this edition does (the
  brief's rules in prose). The README holds a start.
- [ ] A short note on the text: 1573 as base, 1556 as reference, Wikisource as the working text, KJV versification,
  and what the brackets and notes mean.
- [ ] Book titles settled (above), and the contents page checked.
- [x] ~~Wikisource manifest covers every NT book~~ (checked 2026-11-12).
- [x] ~~The Vulgate's verse map checked for the whole NT~~ (2026-11-11).

## Production

- [ ] Read the v2.0 PDF as a proof: title pages, running heads, poetry, quotation marks across columns, the `\cls`
  subscriptions. There is no TeX install here; the release builds the PDF.
- [ ] Look over the EPUBs on a reader (epubcheck already passes in the release workflow).
- [ ] Let `v*` tags deploy to the `github-pages` environment (Settings → Environments), or drop the tag trigger from
  `pages.yml`. Without one or the other, every tag's Pages run fails.
- [ ] The redirect from the WordPress site (yours; decision 50).
