# The NT notes: a modern consensus test, and a shorter wording

Proposed 2026-11-17 (Claude), after Nathan's four questions on `matt-notes.md`, `luke-notes.md` and `john-notes.md`:
Westcott–Hort is out of date; are readings like Matt 20:5 slips of one printing; the wording is monotonous; and
*Græcē hodiē legitur* can read as "modern Greek". Nothing is applied. The three review files wait on the decisions
below and will be rewritten to match them.

## 1. The consensus test without the nineteenth century

Until now a reading counted as the critical text when **SBLGNT, WH and NA28** agreed against RP, with Tregelles either
way (decision of 2026-11-16). WH (1881) and Tregelles (1857–72) predate the papyri and most of the work since, so
neither belongs in a test of today's scholarship. They were there only because the SBLGNT apparatus prints them.

**Proposed test:** **SBLGNT (2010) and NA28 (2012)** against RP. The two are independent: Holmes built SBLGNT from
earlier editions without the Nestle–Aland text. Every candidate is still read against the **NRSVue (2021)**, as now.

What changes (`pipeline notes` with `CONSENSUS = {"NA28"}`, compared with the old test, Matthew–John):

- Nothing in the three files drops out, because every item already required SBLGNT and NA28.
- 28 apparatus units are added; 25 are single words or spellings and need no note. The three that matter:
  - **John 7:8** οὐκ ἀναβαίνω, "I am not going up" (NA28, SBLGNT), against οὔπω (WH, RP); Castellio *nōndum*. Left
    out before because WH read οὔπω. It now qualifies as a kind-A note.
  - **Mark 7:24** Τύρου without καὶ Σιδῶνος (NA28, SBLGNT); Castellio *Tyrī Sīdōnisque*. Brackets: *Tyrī
    [Sīdōnisque]*. Mark is settled, so this would be its own Apply line.
  - **Luke 3:33** Ἀμιναδὰβ τοῦ Ἀδμὶν τοῦ Ἀρνί (NA28, SBLGNT; WH has a third reading); Castellio *Amīnādābī fīliī,
    Arāmī fīliī*. It passes the test, but the NRSVue's footnote says the manuscripts "vary widely", so it is contested
    and left out (`luke-notes.md`).
  - Matt 6:15 (NA28 omits τὰ παραπτώματα αὐτῶν): no change of sense, no note.
- John 1:34 still fails: SBLGNT has ἐκλεκτός, NA28 υἱός.
- Luke 22:43–44 and 23:34a: unaffected. NA28 double-brackets them, and your 2026-11-12 decision to leave them
  unmarked stands.

**A third modern edition (optional):** the Tyndale House GNT (2017) is the most recent critical edition. Its text is
"all rights reserved" (Crossway), but STEPBible's tagged data (TANTT, on GitHub under CC BY-NC-ND 4.0) records for
each word which editions read it, Tyndale House included. It could be used like Gaffiot: consulted to decide, never
copied into the repo. I haven't downloaded it.

**Decision 1:** A, SBLGNT + NA28, checked against the NRSVue / B, the same plus the Tyndale House GNT from STEPBible's
data / C, other

**Decision:** A (Nathan, 2026-11-17: "Yes, rewrite the notes files", to the question "Rewrite the three notes files with
SBLGNT + NA28 and *Cōdicēs antīquiōrēs*?")

## 2. Are Castellio's odd readings slips of one printing?

These were checked in the OCR of each printing (1556 from e-rara; 1573 from MDZ, checked on the page where shown;
1681, 1715, 1747, 1750 and 1758 from archive.org; 1726 = `TXT/1`). A dash means the OCR doesn't give the passage
legibly, not that the words are missing.

| Verse | Castellio | 1556 | 1573 | Later printings | Verdict |
|---|---|---|---|---|---|
| Matt 20:5 | *septimam* (Gk sixth) | *septimam* | *septimam* | 1681, 1747, 1750, 1758 *septimam* | His own slip since 1556 at least; never corrected. Note. |
| Matt 1:11 | adds Jōācimus | – | yes | 1681, 1715, 1747, 1758 | In every printing. Note. |
| Matt 3:16 | *vīdit Jōhannēs* | – | yes | 1681, 1715, 1726, 1747, 1750, 1758 | In every printing. Note. |
| Matt 8:13 | added sentence | – | yes | 1715, 1726, 1747, 1750, 1758 | In every printing. Note. |
| Matt 10:12 | *Salveat hæc domus* | – | yes | 1681, 1715, 1747, 1750, 1758 | In every printing. Note. |
| Matt 11:19, Luke 7:35 | *aliēna sapientia* | yes | yes | all | Castellio's reading. Note. |
| John 4:36 | *sator* | yes | yes | 1715, 1747, 1750, 1758 | In every printing. Note. |
| Luke 19:47 | *Pharisæī* | – | yes (page) | 1747, 1750, 1758 | In every printing. Note. |
| Luke 15:12 | *dīvīsit eī* | – | *ei* (page, canvas 804) | 1726, 1758 *ei*; **1681, 1715, 1747, 1750 *eis*** | Later editors corrected it to the Greek αὐτοῖς. Note as proposed, adding that later printings read *eīs*? |
| John 18:28 | omits "but to eat the Passover" | **omits** | omits | 1758 omits; **1681, 1715, 1747, 1750 add *sed vescerentur Pascha*** | Castellio's lifetime text omits it; later editors filled it in. Note. |
| John 19:38 | omits "so he came and took his body" | – | omits | 1750, 1758 omit | Note. |
| Luke 14:21 | 1573 *ficos* | ***uicos*** | *ficos* | 1715, 1747, 1750, 1758 *vicos* | 1573's misprint. Correction, as proposed. |
| Matt 10:19 | 1573 *suggereretur* | ***suggeretur*** | *suggereretur* | 1715, 1750, 1758 *suggeretur*; 1726 as 1573 | 1573's misprint. Correction, as proposed. |
| Matt 16:9 | 1573 *quod* | – | *quod* (page) | 1747, 1758 *quot* | 1573's misprint. Correction, as proposed. |
| John 9:22 | Wikisource lost a clause | – | has it (page) | 1715 *Iam enim conspiraverant Iudæi* | Wikisource's slip. Correction, as proposed. |

So none of the kind-B notes rests on one printing's misprint. Matt 20:5 is in 1556, Castellio's last lifetime edition,
and in 1573, 1681, 1747, 1750 and 1758.

Not every edition was seen, though: 1551 and 1554 aren't cached, and the OCR of 1715 and 1726 doesn't give the verse.
So the note says *Castelliōnis ēditiōnēs*, as at 1 John 4:4, not *omnēs* (Nathan, 2026-11-17: "Have you checked ALL of
them?").

## 3. The wording

**Modern Bibles.** Modern Bible footnotes repeat themselves on purpose. The NRSVue uses three formulas nearly
everywhere: "Other ancient authorities read / add / lack …", "Gk …" (what the Greek says literally) and "Or …" (another
possible rendering). The ESV does the same with "Some manuscripts …". The preface explains each formula once. A reader
learns them in a page and then reads every note at a glance; varying the wording would make the same fact look like
different facts. The NET's long notes are a study Bible's, not a reader's edition's.

So the trouble with our notes is not that they repeat; the proposal keeps them repeating. The trouble is length and
argument. They are sentences (*Castelliō … intellegit, doctī nostræ ætātis plērīque …*), and each one restates who
judges, which the front matter could say once.

**Græcē hodiē legitur.** You are right that it misleads. *Hodiē* attaches to *Græcē*, so the phrase can mean
"in Greek as spoken today". It also hides the reason, which is that the oldest manuscripts read otherwise. NRSVue's
"Other ancient authorities" names the manuscripts, not the date.

**Proposed formulas.** Each is defined once in the front matter's section on signs, and none is varied:

| Kind | Formula | NRSVue's equivalent |
|---|---|---|
| A, a different reading | *Cōdicēs antīquiōrēs habent* Greek, ‘Latin’. | Other ancient authorities read |
| A, an addition | *Cōdicēs antīquiōrēs addunt* Greek, ‘Latin’. | Other ancient authorities add |
| A, an omission | [brackets] in the text, as now | Other ancient authorities lack |
| B, Castellio's sense | *Græcē* Greek, ‘Latin’. A short clause *Castelliō … intellegit* only where his Latin would otherwise look like a mistake (κάμηλος). | Gk |
| B, a slip in his text | *Græcē* Greek, ‘Latin’; *Castelliōnis ēditiōnēs* ‘…’. | (none: modern Bibles have no slips to report) |
| B, words in no Greek | brackets, with no note (Nathan, 2026-11-17): the modern editions lack them too, so the front matter's definition of [ ] covers them | Other ancient authorities lack |

*Cōdicēs antīquiōrēs*, "the older manuscripts", says why the reading differs. Castellio translated the Greek printed in
his day, which came from late manuscripts; the editions of our time weigh the oldest. The front matter would gloss it
once (draft, to be checked with `latin macron-check` before it goes in): *Cōdicēs antīquiōrēs dīcuntur, quōs ēditiōnēs
Græcæ nostræ ætātis (Nestle–Aland, SBL) sequuntur; Castelliō Græca suī temporis vertit, ex recentiōribus cōdicibus
ducta.* An alternative is *Ēditiōnēs crīticæ habent …*, which is exact about the source but says less about the
reason.

**Examples, old and new:**

| Verse | Now | Proposed |
|---|---|---|
| Mark 1:2 | Græcē hodiē legitur ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ, ‘in Ēsāiā vāte’. | Cōdicēs antīquiōrēs habent ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ, ‘in Ēsāiā vāte’. |
| Matt 24:36 | Græcē hodiē additur οὐδὲ ὁ υἱός, ‘nē Fīlius quidem’. | Cōdicēs antīquiōrēs addunt οὐδὲ ὁ υἱός, ‘nē Fīlius quidem’. |
| Matt 19:24 | Græcē κάμηλος; Castelliō fūnem nauticum intellegit, doctī nostræ ætātis plērīque camēlum. | Græcē κάμηλος, ‘camēlus’; Castelliō fūnem nauticum intellegit. |
| Mark 1:10 | Græcē εἶδεν sine nōmine; Castelliō Jōhannem intellegit, doctī nostræ ætātis Jēsum, quī ex aquā ascendit. | Græcē εἶδεν, ‘vīdit’, sine nōmine; Castelliō Jōhannem intellegit. |
| Matt 11:19 | Græcē ἐδικαιώθη ἡ σοφία ἀπὸ τῶν τέκνων αὐτῆς (hodiē ἔργων, ‘operibus’); Castelliō ‘aliēna est’ intellegit, doctī nostræ ætātis ‘probāta est’. | Græcē ἐδικαιώθη ἡ σοφία, ‘jūstificāta est sapientia’; cōdicēs antīquiōrēs ἀπὸ τῶν ἔργων αὐτῆς, ‘ab operibus suīs’. |
| Matt 20:5 | Græcē περὶ ἕκτην, ‘circā sextam’; ēditiō annī 1573 ‘septimam’ habet. | Græcē περὶ ἕκτην, ‘circā sextam’; Castelliōnis ēditiōnēs ‘septimam’. |
| 1 John 4:4 | Græcē ἐν ὑμῖν, ‘in vōbīs’; Castelliōnis ēditiōnēs ‘nōbīs’ habent. | Græcē ἐν ὑμῖν, ‘in vōbīs’; Castelliōnis ēditiōnēs ‘nōbīs’. |
| Matt 8:13 | Verba reversusque … valentem nec in Græcō quem Castelliō vertit, nec in hodiernō leguntur. | no note: *hōrā[, reversusque … valentem]*. Matt 1:11 and 10:12 likewise. |

**The front matter.** Its list of signs (`text/FRT.usfm`, *Notæ*) would match. It now reads *[ ] Verba quæ ēditiōnēs
Græcæ hodiernæ omittunt* and, for the notes, *ā textū … Græcō, ut hodiē legitur, discēdunt*, the same *hodiē*. A draft,
to be checked with `latin macron-check` and reviewed in `docs/front-matter.md` before it goes in:
- [ ] *Verba quæ cōdicēs antīquiōrēs nōn habent.*
- ᵃ *Adnotātiōnēs īmā pāginā, ubi Castelliōnis ēditiōnēs ā textū Hebræō aut Græcō discēdunt. Cōdicēs antīquiōrēs
  dīcuntur, quōs ēditiōnēs Græcæ nostræ ætātis sequuntur; Castelliō Græca suī temporis, ex recentiōribus cōdicibus
  ducta, vertit.*

The notes already settled (Mark's 9, and Matt 19:24, Luke 18:25, Jude 6, 1 John 4:4, 1 Pet 5:8) would be rewritten
the same way, by Apply lines in a review file of their own. The OT notes are a different kind: they give Castellio's
reasons from his 1554 annotations and need sentences, so they keep their form.

**Decision 2:** A, the formulas above with *Cōdicēs antīquiōrēs* / B, the same with *Ēditiōnēs crīticæ* / C, other

**Decision:** A (Nathan, 2026-11-17, as for decision 1), with brackets and no note for words in no Greek.
`matt-notes.md`, `luke-notes.md` and `john-notes.md` were rewritten to match the same day.

**Decision 3:** rewrite the settled NT notes to match: A, yes / B, only new notes

**Decision:** A, with the front matter's list of signs (Nathan, 2026-11-17: "Yes, rewrite the settled notes and front
matter's list of signs too"). Applied the same day: `nt-notes-settled.md`.
