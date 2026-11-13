# What remains before the New Testament is ready for publication

Drawn up 2026-11-12 (Claude), after v2.0, at Nathan's request. Done items stay listed, struck through, so the list
records how the edition was finished.

## Decisions

- [x] ~~**Brackets**~~: ⟦…⟧ and […] as NA28 and SBLGNT, applied (decision 52; `brackets-and-notes.md` §3).
- [x] ~~**Notes**~~: brief Latin footnotes in the text, in every build; six applied (decision 53; §4).
- [x] ~~**Long paragraphs split**~~: 64 breaks applied (decision 52; `long-paragraphs.md`).
- [x] ~~***eundem*, *quendam***~~: 39 applied, with rules (decision 52; `nd-forms.md`).
- [x] ~~**Macrons marked two ways**~~: slips, *crucī fīgō* apart, the names, *Nāzareth* applied (decision 52;
  `nt-macron-consistency.md`).
- [x] ~~Genesis 1–27 against 1738~~ (decision 52; 11:25 and 13:8 kept).
- [x] ~~Write *se ipsum*, *tē ipsum*, *mē ipsum* as two words~~ (decision 51)
- [x] ~~*epistula* for *epistola*~~ (decision 51)
- [x] ~~Compounds of *eō* with *-iērunt*/*-iit*~~ (decision 51)
- [x] ~~Book titles: title case, and a smaller `\mt2` line for the descriptive part~~ (2026-11-12, Nathan's
  instruction; supported in the site, EPUB, PDF and text builds)

## The text

- [ ] **Your in-depth review** (decision 30) of everything approved "for now": Matthew 14 – Revelation 22. Each
  batch's record lists its "Calls worth a look" and the uncertain items.
- [ ] **More notes on translation** (six so far). They need a reading of the text against the modern
  critical text, and suit your in-depth review, book by book.
- [x] ~~Rom 16:20 and 16:24 *favor*~~: 1573 prints *fauor* at both (canvas 866). The text is right.
- [x] ~~A sweep for joined and variant spellings like *seipsum*~~ (2026-11-12). The corpus's classical tier was
  checked against Gaffiot:
  - The *eumdem* type: applied (decision 52).
  - *quemadmodum*, *quamobrem*, *hujusmodi*, *ejusmodi* stay as they are. Gaffiot heads each as one word, although
    Cicero's modern editions print them apart.
  - *quamdiū*, *circumdō* and *septemdecim* are right as they are.
  - Gaffiot also lists *seipsum*, so decision 51 rests on the corpus alone, where the evidence is unanimous.
- [x] ~~Macron check over the whole NT~~ (2026-11-12). The findings are in `nt-macron-consistency.md`.

## Front matter and apparatus

- [ ] An introduction: Castellio, his Bible, the editions (`docs/editions.md`), and what this edition does (the
  brief's rules in prose). The README holds a start.
- [ ] A short note on the text: 1573 as base, 1556 as reference, Wikisource as the working text, KJV versification,
  and what the brackets and notes mean.
- [ ] The contents page checked with the new titles (needs the PDF).
- [x] ~~Wikisource manifest covers every NT book~~ (checked 2026-11-12).
- [x] ~~The Vulgate's verse map checked for the whole NT~~ (2026-11-11).

## Production

- [ ] Read the PDF as a proof: title pages (now in two sizes), the footnotes (does the Greek in LGR compile?), running heads, poetry, quotation marks across
  columns, the `\cls` subscriptions. There is no TeX install here; the release and Pages workflows build the PDF.
- [ ] Look over the EPUBs on a reader (epubcheck already passes in the release workflow).
- [ ] Let `v*` tags deploy to the `github-pages` environment (Settings → Environments), or drop the tag trigger from
  `pages.yml`. Without one or the other, every tag's Pages run fails.
- [ ] The redirect from the WordPress site (yours; decision 50).
