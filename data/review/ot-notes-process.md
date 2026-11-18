# Light notes in the Old Testament: a systematic search

Proposed 2026-11-18 (Claude), from `notes-audit.md` §G: the Old Testament has 15 notes in 153 chapters, all from places
where Castellio's 1554 annotations comment, and nothing has searched it as `pipeline notes` searched the New. This file
proposes how. The candidates tool is built and has been run on Genesis–Numbers (§4). No note is proposed here; the
reading waits on the decisions in §7.

## 1. Why the New Testament's test doesn't carry over

In the New Testament the main question was textual: Castellio translated the Greek of his day (the TR, from late
manuscripts), the modern editions (SBLGNT, NA28) print an older text, and a note marks where the difference changes
the sense (*Cōdicēs antīquiōrēs habent …*). In the Old Testament Castellio translated the Masoretic text, which is
still the text every modern Bible translates. There is no "older Hebrew" to set against his. The differences come from
three other places:

- **Modern Bibles leave the Hebrew** for an ancient version (the Septuagint, the Samaritan Pentateuch, the Syriac, the
  Vulgate, the Dead Sea Scrolls) or for a conjecture, where the Hebrew looks damaged. The NRSVue marks these "Gk: Heb
  …", "Sam: MT …", "Cn". Castellio usually keeps the Hebrew. Sometimes he goes the same way as the modern Bibles: at
  Gen 4:8 his *rūs sēdūxit* already has the versions' "let us go out to the field", and at 21:9 his *Isaacō fīliō
  suō* their "her son Isaac". Neither needs a note.
- **Castellio reads the Hebrew otherwise** than scholars now do: the existing notes at Gen 6:2 (*hominēs
  præstantēs*), Exod 25:5 (cedar for acacia) and Lev 13:48.
- **Castellio's text says something the Hebrew doesn't**: a number, a name, a clause left out, or a version followed
  where modern Bibles keep the Hebrew. Two found in the pilot (§4): Gen 8:14 *diē septimō decimō*, where the Hebrew
  has the 27th day; and Gen 11:12–13, where Castellio gives Arphaxad a son Cainan, the Septuagint's reading (Luke 3:36
  follows it). His own 10:24 follows the Hebrew without Cainan. Both readings stand in 1738 and in 1750.

## 2. What deserves a note

The NT's light test, unchanged: a note only where a reader comparing a modern Bible would be **misled about what the
Hebrew says**, or about what modern Bibles print. Three kinds, matching §1:

| Kind | Example | Form (the audit's formulas, `notes-audit.md` §A) |
|---|---|---|
| **A. Modern Bibles follow a version** against the Hebrew, Castellio keeps the Hebrew, and the sense changes | Gen 47:21: Castellio *populum … in oppida trānstulit* with the Hebrew; the BSB, with the Samaritan, the LXX and the Vulgate, "reduced the people to servitude" | *Versiōnēs antīquæ habent / addunt* ‘Latin’ (decision 1) |
| **B. His reading** of the Hebrew differs from today's consensus | Gen 6:2 בְנֵי־הָאֱלֹהִים | *Hebraicē* Hebrew, ‘Latin’. |
| **C. His text** departs from the Hebrew: a number, a name, a clause, a version followed | Gen 8:14 the 17th day; Gen 11:13 Cainan | *Hebraicē* Hebrew, ‘Latin’, with *Castelliō … legit* or *Castelliō Septuāgintā sequitur* where he follows another text |

Never a note for (as in the NT, and these besides):

- His classical vocabulary in place of the Hebrew institutions: *centuriōnēs* and *tribūnī* for the captains of
  hundreds and thousands, *decumæ*, *Jōva*. The front matter explains it once.
- A paraphrase that keeps the sense. At Gen 14:8 he names the five kings of 14:2 as *quīnque rēgulī* instead of
  listing them again.
- Words moved into the next verse, as at Gen 2:22 and 11:27.
- Names spelled his way, measures and coins (except a word no dictionary has: the audit's coinages).
- A version's reading the modern Bibles don't follow, unless Castellio follows it (kind C).
- The meaning of a rare animal, plant or stone. Castellio himself said his names for these were guesses (front
  matter, *Dē ejus interpretātiōne*), and modern Bibles disagree among themselves.

## 3. The consensus, defined so it can be checked

The NT test was two independent editions (SBLGNT and NA28) agreeing. No critical apparatus of the Hebrew can be read
here (the BHS and BHQ apparatus are copyrighted and not online), so the test uses **translations that mark their
departures from the Hebrew**:

- **Kind A:** the **NRSVue and the BSB** both leave the Hebrew for the same reading. The two come from different
  traditions (the NRSVue mainline and ecumenical, emending often; the BSB evangelical, emending rarely), so where both
  leave the Hebrew the case is strong. The BSB's notes say so in the files we have. The NRSVue is read online for each
  chapter and never stored (as for the NT).
- **Kinds B and C:** the NRSVue, the BSB and the Hebrew itself agree against Castellio, and the NRSVue doesn't call
  the Hebrew uncertain. A disputed passage gets no note, as in the NT (Col 2:18).
- For *why* Castellio chose a reading, his 1554 annotations, as the existing notes did (`gen-exod-notes-1554.md`,
  `lev-notes-1554.md`, `num-notes-1554.md`). They are cited in the review file, not the note.

**The NET Bible's notes** are free to read online and say, verse by verse, where scholars disagree. They are the
check for "disputed".

## 4. The candidates tool, and the pilot

`python -m pipeline notes BOOK` now takes Old Testament books (`pipeline/otnotes.py`; the NT's tests are unchanged).
It writes `data/review/<book>-notes-candidates.md` with three sections, each verse given with the Latin, 1738's text,
the WLC, the Vulgate, the LXX (where its numbering is checked: Genesis and Exodus so far), the BSB and the KJV:

- **Versions:** the BSB's own footnotes that name an ancient version, ranked *against MT* (the BSB's text follows the
  version: candidates for kind A), *with MT* (the BSB keeps the Hebrew but gives the version: Castellio may follow the
  version, kind C) and *other*. The WEB's few such notes besides.
- **Numbers:** verses whose numerals differ between the Hebrew (the OSHB's lemmas: cardinals, ordinals, the dual of
  200 and 2000, tithes) and the Latin (cardinals, ordinals, *ducentēsimus*, *quīngentēnārius*, distributives,
  *septuplus*, *duodēquadrāgintā*, and the figures of Numbers' census). One and first are left out on both sides,
  since אֶחָד is often an article; *alter*, *paria*, *trīduum* and *totidem* may stand for a number.
- **Short:** verses whose Latin is less than half as long as the Hebrew for the book, and still short with their
  neighbours (so words merely moved to the next verse don't count).
- **Castellio's marks** (added 2026-11-18, `gen-notes.md` §F): his *G.* (*G.L.*, 1750 *Gr. lect.*) … *H.* around a
  reading taken from the Greek, found in the raw OCR of 1738 and 1750 and placed in the verse sharing most word pairs
  with the lines around it. Genesis 5 (all those found by hand), Exodus 3 (2:22, 6:20, 28:33–34), Leviticus none,
  Numbers 1 (10:6, the third and fourth blasts). The edition doesn't print the marks, so a marked reading that modern
  Bibles don't print is a kind-C candidate.

The pilot, Genesis–Numbers (all settled):

| Book | Chapters | Versions (against / with MT / other) | Numbers | Short |
|---|---|---|---|---|
| Genesis | 50 | 27 (8 / 11 / 8) | 41 | 9 |
| Exodus | 40 | 11 (2 / 2 / 7) | 60 | 17 |
| Leviticus | 27 | 1 (1 / 0 / 0) | 31 | 3 |
| Numbers | 36 | 14 (6 / 3 / 5) | 39 | 6 |

Most of the numbers are nothing: a number on one side only (*bīnī*, *paria*, a week), or Castellio's roundings in the
tabernacle chapters (*totidemque ad partem occidentālem*). Reading them takes a few minutes a chapter. Their value is
in finds like Gen 8:14, which no reader comparing sense would stop at. The BSB's *against MT* notes are few, which is
why the NRSVue has to be read for every chapter (decision 3). Most of the Short verses are Castellio's paraphrase.

## 5. The process, per book

1. **`python -m pipeline notes BOOK`** writes the candidates (done for Genesis–Numbers).
2. **A reader per chapter range** reads every candidate, and reads each chapter once against the Hebrew, the BSB and
   the NRSVue's notes for kinds A and B, with the NET notes where a reading may be disputed and Castellio's 1554
   annotations where they exist. Each reading of Castellio's is checked in 1738 and another printing (as the NT's odd
   readings were, `nt-notes-form.md` §2), so a printer's slip is corrected and not noted.
3. **`data/review/<book>-notes.md`** for Nathan: one item per proposed note, with its evidence, its Latin wording and
   an Apply line placing the `\f` at the word; then what was considered and left out, one line each with the reason.
   The existing 1554-based notes are checked against the same test, and an item is proposed where one fails it.
4. Nathan accepts or rejects per item; `pipeline review apply` writes the accepted ones.

**When:** Genesis–Numbers now, as the NT was done once its books were settled. From Deuteronomy on, the pass runs as
each book is settled, so the notes go in with it.

**Expected yield:** the NT gave 0.4–0.8 notes a chapter. The OT should give fewer, since kind A rarely applies:
perhaps 0.2–0.4 a chapter, or 30–60 for the four books. More than one note in two chapters means the bar is too low.

## 6. What changes elsewhere if the decisions are accepted

- **Front matter** (`text/FRT.usfm`, *Notæ*), for kind A only: a gloss for *versiōnēs antīquæ*, drafted for checking
  with `latin macron-check` when the first such note is accepted: *Versiōnēs antīquæ dīcuntur Græca Septuāgintā
  interpretum, Samaritāna, Syra, Vulgāta, quās interpretēs nostræ ætātis ibi sequuntur, ubi textus Hebræus
  corruptus vidētur.* The row's *ubi Castelliōnis ēditiōnēs ā textū Hebræō … discēdunt* would need *aut ubi
  versiōnēs antīquæ ab eō* or similar.
- **Brief:** the kind-A formula added to the note formulas.

## 7. Decisions for Nathan

1. **Kind A**: modern Bibles following a version where Castellio keeps the Hebrew. A, note them with *Versiōnēs
   antīquæ habent / addunt* ‘Latin’, under the consensus of decision 2 (recommended: the NT notes the same kind of
   fact, and a reader with the NRSVue at hand meets it) / B, leave them out, keeping the OT notes to Castellio's
   own departures (the front matter stays as it is)
2. **The consensus**: A, the NRSVue and the BSB agreeing (recommended) / B, the NRSVue alone / C, add the NET
3. **The NRSVue**: A, read for every chapter (recommended: the BSB marks too few departures to find kind A alone) /
   B, only for the candidates
4. **First book**: A, Genesis (recommended: the richest candidates, including both pilot finds) / B, Numbers (the
   numbers) / C, all four at once, by several readers, as Acts–Revelation were

**Decision:** accept 1A, 2A, 3A, 4A (Nathan, 2026-11-18: "Yes, as recommended"). Genesis first:
`data/review/gen-notes.md`.
