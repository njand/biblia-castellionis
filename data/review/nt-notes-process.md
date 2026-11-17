# Light notes where Castellio departs from the modern consensus: a process (NT first)

Proposed 2026-11-16 (Claude), after your request for a better way to propose *light* footnotes. Nothing here changes
the text; it describes how candidates would be found, filtered and put to you. The notes themselves keep the form
you chose on 2026-11-12 (`brackets-and-notes.md` §2): Latin, `\f + \fr C:V \ft …\f*`, a superscript letter in the
text.

## What we have now, and why it is not enough

- Six NT notes (Matt 19:24 and its two parallels, Jude 6, 1 John 4:4, 1 Pet 5:8) and the brackets. They were found
  by chance, during stage 2 or a spot check. Nothing has looked for the rest systematically.
- The OT notes come from Castellio's own 1554 annotations (`gen-exod-notes-1554.md`, `lev-notes-1554.md`): a good
  source for *why* he chose a reading, but it only finds the places he chose to comment on.

## What deserves a note (the "light" test)

A note only where a reader comparing a modern Bible would be **misled about what the Greek says**, in one of three
kinds:

| Kind | Example | Note form (as the existing notes) |
|---|---|---|
| **A. His Greek text** differs from the modern critical text, and the difference changes the sense | (none settled yet; the brackets already cover whole verses) | *Græcē hodiē legitur …, '…'.* |
| **B. His reading** of the Greek differs from today's consensus | Matt 19:24 κάμηλος as a ship's cable | *Græcē …; Castelliō … intellegit, hodiernī interpretēs plērīque ….* |
| **C. A slip** in his editions, or a reading of no Greek text | 1 John 4:4 *nōbīs* for ὑμῖν; Jude 6 *Deī* for ἡμέρας | *Græcē …, '…'; Castelliōnis ēditiōnēs '…' habent.* |

Never a note for: word order, articles, conjunctions (καί/δέ/οὖν), tense or mood variants that the Latin does not
show, a pronoun the sense supplies anyway, spelling of names, his classical vocabulary in place of the Church's (as
*Jōva* in the OT), which the front matter explains once, or a paraphrase that keeps the sense.

## The consensus, defined so it can be checked

The SBLGNT apparatus (cached in `sources/parallel/sblgnt/files/…/sblgntapp/`) gives, for every variant, the readings
of Westcott–Hort (WH), Tregelles (Treg), NA28, the NIV's Greek and the Byzantine text (RP). **Consensus** = SBLGNT,
WH, Treg and NA28 agree. Castellio's Greek is the TR (`sources/parallel/tr`), which nearly always sides with RP.

Pilot count (all 27 books, 2026-11-16): 4,880 apparatus units have the four critical editions together against RP.
1,301 are word order, articles or another form of the same word. That leaves 3,579 where words differ, are added
or dropped. Only **122** add or drop three words or more. Most of the rest are single words that change
nothing a reader would notice (Acts 1:6 ἠρώτων for ἐπηρώτων).

## Modern translations and commentaries (added 2026-11-16, your question)

The Greek alone shows where Castellio's *text* differs; it does not show where his *reading* differs from what scholars
now take the Greek to mean (kind B), which is the larger and harder group. For that, the modern translations and
commentaries are the evidence, used in two ways:

- **To find candidates.** Where several modern scholarly translations agree with one another on a sense and
  Castellio's Latin says something else, that is a candidate. One translation alone is not: they differ among
  themselves on many renderings, and a note should mark only what the consensus holds.
- **To judge them.** For each candidate, a commentary says whether the modern reading is settled or disputed. A
  disputed passage gets no note: Castellio's reading is then one of the live ones.

Which sources, given copyright and what can be read:

| Source | Use | Access |
|---|---|---|
| BSB, WEB (already in `sources/parallel`) | the first comparison, every verse | free, local |
| **NET Bible and its translators' notes** (about 60,000 notes on text and translation) | the main commentary: it says, verse by verse, what the Greek allows and where scholars disagree | free to read online; quotation limited, so cited, not copied |
| **NRSVue**, ESV, NIV | the consensus check, read for the candidates only | copyrighted; read online (e.g. Bible Gateway), never stored in the repo |
| Metzger, *A Textual Commentary on the Greek NT* | the reasons for kind A | copyrighted; only if you have a copy (I can't read it) |
| 19th-century commentaries (Alford, Meyer, the *Expositor's Greek Testament*) | context on older debates | public domain, on archive.org; dated, so a support, not the authority |

The review file cites each source by name and verse, with what it says in a few words of my own, never quoted at
length. Nothing from the copyrighted translations is stored.

**Recommendation**: per chapter, compare the Latin with the Greek, BSB and WEB (local, every verse), and read the NET
notes for the whole chapter. Check NRSVue (with ESV or NIV) only for the candidates that survive, since that means
reading a copyrighted site verse by verse. Count a divergence only when NRSVue, the NET and the BSB agree against
Castellio and the NET notes don't call it disputed.

## The process, per book

1. **`python -m pipeline notes BOOK`** (new; standard library), writes `data/review/<book>-notes-candidates.md`:
   - **Kind A, from the apparatus**: each consensus-vs-RP unit, filtered automatically (order, article, same word,
     conjunction, particle and pronoun swaps out), kept only where the TR has the RP reading. Each with the Latin
     verse (settled and as printed in 1573), TR, SBLGNT, the apparatus line, the Vulgate and the BSB.
   - **Kind C, checks a script can make**: pronoun person and number (ἡμεῖς/ὑμεῖς against *nōs/vōs*, as at 1 John
     4:4), numbers, and proper names, between the Latin and the TR. Each hit with 1556's reading too, so a slip
     shared by both lifetime editions is told from a 1573 misprint.
   - Already noted or bracketed verses are left out.
2. **Claude reads every candidate**, and reads each chapter once against SBLGNT for **kind B** (a sense the Greek
   does not bear today), with the Vulgate and BSB as a check on what "today's reading" is. Castellio's annotations
   (1554 OT; for the NT the notes in 1551/1573, where they exist) are quoted when they explain the choice.
3. **`data/review/<book>-notes.md`** for you: one item per proposed note, with its evidence, its Latin wording and
   an Apply line placing the `\f` at the word; then **a list of what was considered and left out**, one line each
   with the reason. You see what was dropped as well as what was kept.
4. You accept or reject per item; `pipeline review apply` writes the accepted ones, and `gold` is rebuilt as usual.

**Expected yield**: a handful per Gospel and Acts, one or two in most letters, none in many: perhaps 30–60 in the NT.
If a book gives more than one note per chapter on average, the bar is too low; the review file says so.

## Decisions for you

1. **The consensus test**: SBLGNT + WH + Treg + NA28 against RP (as above), or SBLGNT alone?
2. **Kind A beyond the brackets**: note smaller text differences (a phrase or a name), or keep the text-critical
   side to the brackets and note only kinds B and C?
3. **Translations and commentaries**: the recommendation above (NET notes for every chapter; NRSVue, NET and BSB
   agreeing as the test for kind B), or a different set? Do you have Metzger's *Textual Commentary*?
4. **Pilot book**: Mark (16 chapters, Gospel, the longer ending already bracketed) or a short letter first
   (Jude, Philemon) to settle the forms?

**Decision:** (Nathan, 2026-11-16) 1: A, the four editions against RP. 2: C, notes on the Greek text only where the sense changes (a clause, a name or number, a main word). 3: A, the Greek, BSB, WEB and the NET notes for every chapter, NRSVue for the candidates; Metzger offered (see below). 4: A, Mark first.

**Metzger** (2026-11-16): the link offered (a PDF of the 2nd edition on obinfonet.ro) looks like an unauthorized copy of
a book still in copyright (United Bible Societies, 1994), so it was not downloaded. A copy you own (print, or a PDF or
Logos edition) can be used: scans or page photos of the verses in question are enough.

**Begun 2026-11-16**: `pipeline/notes.py` (`python -m pipeline notes BOOK`) writes the candidates;
`data/review/mark-notes-candidates.md` is the first (272 apparatus units in 227 verses: 9 clauses, 9 names, 2 numbers,
207 single words; 1 pronoun mismatch). Read with the NET notes and the NRSVue: `mark-notes.md` (17 items), accepted and applied 2026-11-16. The consensus test is now WH and NA28 with SBLGNT, Tregelles either way (section D's decision).

**2026-11-17**: Matthew, Luke and John read the same way (`matt-notes.md`, 45 items; `luke-notes.md`, 47; `john-notes.md`, 25), for Nathan. The readers found strong readings the candidates file had missed (Luke 14:5, John 1:28, Matt 20:16 and 27:35), so `pipeline notes` now has a third section, **the TR alone**: TR against SBLGNT where the apparatus has no unit, because RP stands with the critical text. Movable ν and elision no longer count as differences, and two names sharing four letters are no longer taken for one word. The yield: notes 19, 16 and 12 (0.6–0.7 a chapter, under the bar set above), brackets 19, 27 and 10, besides the corrections. The reading also turned up misprints and Wikisource slips that only the page images could settle (each file's section D).

**2026-11-17, later**: your questions on WH, on printing slips and on the wording led to `nt-notes-form.md`, which proposes a test of modern editions only (SBLGNT + NA28, checked against the NRSVue), records each of Castellio's odd readings across the printings (none is one printing's misprint; Matt 20:5 *septimam* is already in 1556), and proposes fixed short formulas modelled on the NRSVue's, with *Cōdicēs antīquiōrēs* in place of *Græcē hodiē legitur*. Decided the same day (decisions 1 and 2: A; words in no Greek get brackets, not a note; *Castelliōnis ēditiōnēs*, not *omnēs*, since not every edition was seen). `pipeline notes` now tests NA28 with SBLGNT only, and the three review files are rewritten to match.
