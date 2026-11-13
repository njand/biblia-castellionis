# The open questions now that the New Testament is complete, with the evidence and a recommendation

Surveyed 2026-11-12 (Claude). This covers every question still open in `HUMAN.md`. That means the two left by
Revelation (`data/review/rev-stages3-5.md`), the one judgment decision 42 left to you, and the follow-ups and actions
that have waited since November 5–11. Each comes with the evidence actually seen. Section A changes the settled text and
carries **Apply** lines (checked with `python -m pipeline review check`); the others decide work or wording. Nothing
here is applied until you fill in its Decision line.

A search for empty Decision lines in `data/review/*.md` found none. The names left "for the names list" in
decisions 16–20 (*Bennammi*, *Hierichūntem*, *Henōchī/Enōchī*, *Abius*) were settled by decision 22. Genesis on the site
was settled once the Pages workflow began building every book.

## A. *agnus* of Christ in John 1:29 and 1:36

Revelation writes *Agnus* with a capital wherever it means Christ, 26 lines in all (*Agnus*, *Agnum*, *Agnī*, *Agnō*).
The only settled places outside Revelation where the Lamb is Christ are John 1:29 *Ecce agnus Deī, quī mundī peccātum
tollit* and 1:36 *Ecce agnus Deī*, and both are lower case.

- **Evidence**:
  - Decision 20 chose NRSV style: titles of God and Christ capitalized (*Fīlius Hominis*, *Servātor*, *Sānctus Deī*).
    The NRSV and the BSB both print "the Lamb of God" in John 1:29 and 1:36, and "the Lamb" in Revelation.
  - 1573 and 1758 print *agnus Dei* in lower case in John. But 1573 also prints *filius hominis*, *pater* and *spiritus*
    in lower case, which decision 20 already overrides. 1573 does capitalize *Agnus* in the summary of Revelation 5 (*Agnus ille Dei*, as the Revelation 1–11 reader reported).
  - The other lower-case lambs stay lower: Acts 8:32 is Isaiah's simile (*utque agnus ante suum tōnsōrem*), Luke 10:3
    the disciples (*agnōs inter lupōs*), and John 21:15 Peter's flock (*Pāsce agnōs meōs*).
- **Options**:
  1. **Capitalize John 1:29 and 1:36** (*Ecce Agnus Deī*). This is two changes, and the edition then writes the title
     one way throughout.
  2. Keep John lower case and lower Revelation's 26 lines to match. This goes against decision 20 and the NRSV.
  3. Leave them split, reading John as a description and Revelation as a name. This is defensible, but the NRSV does
     not draw that line.
- **Recommendation: option 1.**

**Apply:** `John.1.29` la: `Ecce agnus Deī` → `Ecce Agnus Deī`
**Apply:** `John.1.36` la: `Ecce agnus Deī` → `Ecce Agnus Deī`

**Decision:** accept option 1: capitalize John 1:29 and 1:36 (Nathan, 2026-11-12; decision 50)

## B. Crediting 1573 for Rev 3:1

Wikisource has no Rev 3:1 (its chapter 3 starts at verse 2), so the verse was entered from 1573 (canvas 939).

- **Evidence**:
  - `README.md` already names 1573 as the New Testament's base edition (decision 37) and says that "where the editions
    genuinely differ, the reading of the base edition … is printed". Every stage-2 correction (1,273 Apply lines across the
    stage-2 files) is also 1573's wording rather than Wikisource's. Rev 3:1 is the largest of these but the same in
    kind.
  - The verse is printed in 1556, 1758, 1681, 1747 and 1715 as well; it is a gap in Wikisource only.
  - The record already exists: `data/review/rev1-11-stage2.md` and `docs/editions.md`. 1573 is a 16th-century print,
    so no licence is involved.
- **Options**:
  1. **No special credit**; the README's base-edition statement covers it.
  2. Add one sentence to the README: "Wikisource's Revelation lacks 3:1, which is supplied from 1573."
  3. Add a footnote to the verse in every format.
- **Recommendation: option 2.** It costs one line, tells a Wikisource editor where the edition and Wikisource part, and
  invites them to fill the gap. Option 3 puts editorial apparatus into a reader's edition that otherwise has none.

**Decision:** option 1: no special credit; the README's base-edition statement covers Rev 3:1 (Nathan, 2026-11-12; decision 50)

## C. *quidquam* or *quicquam* (decision 42's one judgment against Cicero's editions)

The settled text has *quidquam* 32 times and *quidquid* 49 times, by the brief's approved *quidquid*. Decision 42 asked
whether both should turn to *c*.

- **Evidence**:
  - The corpus, in `data/review/spelling-audit.md`: *quidquam* 396 (Cicero 65) against ***quicquam* 2,197 (Cicero 376,
    Livy 201)**. *quicquid* 172 in Cicero's editions against fewer than 74 for *quidquid*. Quintilian has 89 to 74;
    Seneca (320) and the Digest (198) print *quidquid*.
  - Gaffiot 2016 heads the *d* forms (*quisquam*, neuter *quidquam*).
  - Castellio's own printings: 1573 *quicquam* 2, *quicquid* 5 (Gospel OCR), against 1738 *quidquam* 1, *quidquid* 2.
    Wikisource mixes them: *quidquam* 43 and *quidquid* 74 against 8 each with *c*.
- **Options**:
  1. **Keep *quidquam*/*quidquid***. This follows Gaffiot, the orthography the edition is named for, and the brief.
  2. Turn both to *c* (about 80 places), following Cicero's editions and 1573. That would be the one place where the
     edition follows the corpus against Gaffiot.
- **Recommendation: option 1.** The edition's rule is "Gaffiot 2016 orthography". Every other judgment in decision 42
  agreed with Gaffiot, and Gaffiot's *d* is also the etymological spelling (*quid* + *quam*).

**Decision:** option 1: keep *quidquam*/*quidquid* with Gaffiot (Nathan, 2026-11-12; decision 50)

## D. Chapter summaries (decision 3: "included", but not yet in the text)

Decision 3 (2026-11-05) put Castellio's chapter summaries (the *argumenta*) in the edition, as small italic headings
under each chapter number. None of the settled books has one: `text/*.usfm` has no `\cd` line. The builds already print
`\cd` as `\Argumentum{…}` (`latex.py`, 2026-11-08).

- **Evidence**:
  - Wikisource has a summary for **every one of the 260 New Testament chapters** (verse 0 in
    `data/witnesses/wikisource/*.tsv`), 557 in all with the Old Testament books it covers.
  - 1573 prints them in italics under each *CAPVT* (seen on the page images this week, e.g. Rev 10 *Alius apparet
    angelus amictus nube, libellum apertum tenens*).
  - They would go through the same stages as the verses: Wikisource drafted, read against 1573 on the page image, then
    spelling, macrons and capitals. Each summary is one or two lines, roughly 260 lines of text in all, about the size
    of one of the recent batches.
- **Options**:
  1. **Do it now as the next batch**, the whole New Testament at once (stage 2 against 1573, then 3–5), so the next
     release has them. Genesis and Exodus 1–20 follow in the same way, against 1738.
  2. Do it book by book as the in-depth review reaches each book.
  3. Reverse decision 3 and leave them out.
- **Recommendation: option 1.** The decision stands. The text is already parsed, the pipeline handles verse 0 (the
  gold format reserves it), and they are short. Leaving them till last means touching every settled book again later.

**Decision:** option 3: decision 3 reversed; the chapter summaries are left out (Nathan, 2026-11-12; decision 50)

## E. A release with the complete New Testament

v1.0 (tag of 2026-11-10, commit 997430a) holds Genesis, Exodus 1–20, the Gospels, Acts, Romans and 1–2 Corinthians.
There have been 18 commits since, including the rest of the New Testament and decisions 40–49. The site on GitHub Pages
already shows everything (it rebuilds on every push to `main` and labels itself "v1.0+ (date)"), but the downloadable
release is still v1.0, and `RELEASE.md` describes it.

- **Options**:
  1. **Tag v2.0 now**, *Novum Testamentum* complete (with Genesis and Exodus 1–20), after updating `RELEASE.md`'s
     contents line.
  2. Wait for the chapter summaries (D) and tag once, with them in.
  3. Wait for your in-depth review.
- **Recommendation: option 2** if you accept D now; it is one batch away, and a release whose headline is "the New
  Testament" is better with the summaries every printing has. Otherwise option 1. The release notes already say the
  chapters are approved for now, so option 3 is not needed.

**Decision:** option 1: tag v2.0 now (Nathan, 2026-11-12; decision 50)

## F. Genesis 1–27 against 1738 (a follow-up from 2026-11-07)

Your settled New Testament chapters from before the pipeline (Matthew 1–13, Mark 1–5, Luke 1–13, John 1–4) were
collated against 1573 (`data/review/settled-1573.md`, decision 27). That found 46 places, 22 of them Wikisource slips
your text had inherited (e.g. Luke 6:12 *per nox*). Genesis 1–27, also your earlier work, has never been collated
against its base, 1738. Genesis 28–50 and Exodus 1–20 were, through the pipeline.

- **Options**:
  1. **Do it**, the same way: `collate` against 1738 (archive.org OCR, which has no page images to crop, so 1750 and
     your 1726–27 text are the second witnesses). The differences go into one review file with Apply lines.
  2. Leave it to your in-depth review.
- **Recommendation: option 1**, after D. If the Gospels are a guide, it will find a handful of inherited slips, and it
  is the only settled text that has had no check against its base.

**Decision:** option 1: collate Genesis 1–27 against 1738 (Nathan, 2026-11-12; decision 50)

## G. Pointing the WordPress site at the new one (an action only you can take)

Waiting since decision 39 (2026-11-10): the old WordPress site (the 2019 Gospels and Genesis) should point readers to
`https://njand.github.io/biblia-castellionis/`, by a notice, a redirect, or both. I have no access to it.

- **Recommendation**: a short notice at the top of the WordPress home page and of each book page, linking to the new
  site. A redirect would hide the 2019 text, which is the record of your earlier macron decisions; better to keep it
  readable.

**Decision:** Nathan will add a redirect from the WordPress site to the new one (Nathan, 2026-11-12; decision 50)

**Done** (2026-11-12, with Nathan in the browser): a notice at the top of the home post linking to the new site,
and the 131 chapter and index pages moved to the WordPress trash (Nathan's choice), not a redirect.

## Calls taken "for now" (no answer needed until your in-depth review)

These were proposed, approved for now, and are listed in each batch's record. They stay as they are unless your review
changes them:

- **Revelation** (decision 49): the title line; *α et ω* in Greek letters; Christ's speech 1:17–3:22 as one quotation;
  *Hominis Fīliō*, *Fidēlis et Vērus*; the uncertain quotations at 16:15, 18:14, 18:20, 22:7.
- **1 Peter–Jude** (decision 48): 1 John 5:7–8's parentheses with no note; Jude 6 *Deī* and 1 John 4:4 *nōbīs* kept
  with 1573 and 1556 against the Greek; 1 Pet 2:22–24 as prose; Jude 9 and 15 without `\qt`.
- **Hebrews and James** (decision 47): Hebrews titled without Paul's name; the KJV book order; Heb 1:8 *ō Dīve*.
- **Paul's letters** (decisions 43–44, 36, 38): the title lines (*prior/posterior* where 1573 has *prima/secunda*).
