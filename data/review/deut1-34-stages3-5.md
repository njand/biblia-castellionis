# Deuteronomy 1–34: stages 3–5, one proposal per verse

Proposed 2026-11-18 (decision 30's standing rule), as Numbers (`data/review/num1-36-stages3-5.md`). Nathan: "Yes, run
stages 3–5", "Yes, add them" (the spelling rules), then "Fix the problems you identified: "introjeris", "ībi", and the
problems in Exodus and Numbers. The go ahead and approve it for now and commit."

**Decision:** accept, and Deuteronomy 1–34 settled for now (Nathan, 2026-11-18): `text/DEU.usfm`, the 958 items applied
as accepted (identical to the preview), `data/gold/Deut.tsv` built, the ledger `settled`, the drafts removed. The calls
below stand as made; his in-depth review comes later (decision 30).

## Where it stands

- **Stages 1–2**: 1738's own text, every line read on the page (`data/review/deut1-34-stage2.md`; Wikisource has only
  1:1), versified to the KJV's 959 verses (45 edits, `data/versification/Deut1-34.draft.edits.tsv`; 14:16–17 one verse
  numbered `16-17`).
- **Corrections to the draft found here** (decision 30's rule; Apply lines in the stage-2 record, §"Corrections for the
  reading edition", all applied to `text/draft/DEU.usfm`; the printed text keeps 1738 except where stage 2 misread it):
  - 1738's misprints: 8:2 *haberetis*, 9:6 *justitiam*, 16:11 *collocando*, 18:18 *eis*, 22:16 *calumnietur*, 23:7
    *abhorretote*, 23:18 *mercedem*, 4:14 *possessionem* (1738 *posses-|si-|nem*, seen again on the page); 32:30
    *fierine* (1738 *fieri ne*: a question, the enclitic).
  - **Four long s read as f in stage 2**, each seen on its sheet beside an ſ in the same crop: 33:29 *conservate*, 11:10
    *conserebatis*, 28:30 and 28:39 *conseretis*. Set right in the read lines, the corrections file and the printed
    text (rebuilt). After the first, the draft's every *f*-word was compared with the settled text and the doubtful
    ones read in context: the others are sound.
  - The draft's j/v conversion: 4:9 *advertite*, 7:13 *alvorum*, 32:21 *perversa* (a consonantal u after a prefix:
    the draft searched for every consonant + u + vowel, no other), 23:25 *introieris* (a vowel i made j).
- **Names** (§"Names" of the stage-2 record, 15 spellings; the table `deut1-34-names.md`): one form per person, place
  and people, the settled form first (decision 46), markings by decision 52's order, 122 forms rows.
- **Stages 3–5**: `data/review/deut1-34-ch01.md` … `-ch34.md`, 958 items (one per verse; the range is one item), all
  checking `ok`. Preview: **`text/draft/DEU.preview.usfm`**. Calls in `data/decisions/Deut.layout.tsv` (263 rows) and
  `Deut.forms.tsv` (707 rows), each with its reason.
- **Stage 2b** (the printed text, `text/orig/draft/DEU.usfm`): built from the read lines in the KJV's numbering; still
  to be read on the page for approval (paragraphs, marks), as Numbers' (`num-orig.md`).

## How the verses were made

Eight readers (1–3, 4–6, 7–10, 11–14, 15–20, 21–26, 27–30, 31–34) under one brief, Numbers' rules, each verse beside
the KJV and the BSB; a names reader across the book; then four proofreaders (1–8, 9–17, 18–27, 28–34) read every verse
of the preview again (15 layout and 57 forms rows changed or added, each noted "proofread:"). Their notes:
`deut1-34-stages3-5-readers.md`. Every flag was checked in its verse; the `homograph` flags still shown (286) are words
the readers and proofreaders confirmed as proposed.

- **Quotation marks: Moses' discourses unquoted** (1:6–4:40, 5:1b–26:19, 28, 29:2b–30:20), as the voice of the book, as
  the BSB has 1–26; speech he reports inside them in “…”, a quotation within that in ‘…’. Castellio gives most of it as
  **reported speech** (1:6 *admonuit nōs … jam satis nōs in eō monte mānsisse*; the people, the spies, God's oath,
  the children's question at 6:20–25): unmarked, whatever the BSB does (decisions 4, 25). Quoted where the Latin gives
  the words: God at 1:38–40, 2:18–19, 2:24–25, 5:28–31, 9:12–14, 11:14–15, 18:17–20, 31:14–21, 32:49–52, 34:4; the
  Decalogue 5:6–21 (one paragraph, as the settled Exod 20); the people 5:24–27, 18:21, 30:12–13; Moses' prayer 9:26–29;
  the priest and officers 20:3–8; the elders 21:7–8; the widow 25:9; the worshipper 26:3, 26:5–10, 26:13–15. The
  framed speeches of the narrative chapters are quoted: 27:1–8, 27:9–10, 27:12–26 (the Levites' curses and the people's
  *Āmēn* in ‘…’, one paragraph per curse, the speech reopened), 31:2–13, 31:26–29, 32:46–47. *Inquit* set off by commas,
  the quotation closed and reopened (decision 65). 69 “ and 66 ”: the extra three reopen a speech at a new paragraph
  (27 and 31:19).
- **Poetry** where the BSB sets it and the Latin is verse: 28:3–6 and 28:16–19 (the blessings and curses), the Song of
  Moses 32:1–43, the Blessing of Moses 33:2–29, Castellio's clauses on the BSB's lines. In the Song God's words are in
  “…” (32:20–28, 34–35, 37–42); in the Blessing each tribe's words (33:2–6 and 26–29 the frame). **Not** 29:5–6, which
  the BSB sets as God's first-person verse: Castellio has Moses speak of God (*ut intellegātis, eum esse Jōvam*), so
  prose (the reader's own preference; the merge drops those two rows).
- **Paragraphs**: the BSB's, moved to the sentence start where they fell inside one; added where a new speech, law or
  narrator begins; paragraphs over about 250 words split where the BSB (and WEB where it breaks) break (decision 52):
  1:41–2:23, 4:15–31, 7:12–26, 8, 9:7–29, 12:1–28, 19:1–14, 20, 22:13–30, 24:6–22, 26:1–15, 29:16–28. The BSB's lists
  (5:7–21, 14:4–18, 27:15–26) are paragraphs, not lists (the settled text has none).
- **Capitals** for adjectives of peoples and places (*Amorræus, Hesebōnius, Isrāēlīticus, Ægyptius, Mōabīticus,
  Cisjordānīnus* …; about 20 places), for God (*Domine Jōva*, *dominōrum Dominus*, *Suprēmus* in the Song); *deus*
  lower case where it is "any god" (3:24, 4:34 *ūllus deus*). **Vocatives set off by commas** throughout (*Audīte,
  Isrāēlītæ:*; *Attendite, cælī*).
- **Forms**: chiefly the ablatives the macronizer leaves short (*terrā* 48 times, *eā*, *vītā*, and **the ablative
  *Jōvā*** after *ā/ab*, *cōram*, in ablative absolutes: 50 rows, the settled text's *ā Jōvā* 59 : 1), perfect
  subjunctive *-erīs/-erītis* in prohibitions, indirect questions and relative clauses of cause against the future
  perfect, *hīc*, *sōlis*, *domūs*, *frūctūs*, *nōlītōte*, *manus* singular, *maria* (males, 15:19, not the name), and
  the words no source marks (*mūtuābitis, dēmentiētis, interfēmineō, glōssem, pignorantor, fierīne* …), each with its
  reason.

## Names: one form per person, place and people

`deut1-34-names.md` (about 135 persons, places and peoples): the settled form first (decision 46), then Gaffiot, the
Greek's long letters, another dictionary, the Hebrew vowel (decision 52); gentile adjectives in *-īnus/-iānus/-ēnsis*.
Spelled as the settled text: *Emenses* (the Emim, Gen 14:5), *Jabboc-*, *Ceneretho*, *Pherezæōs*, *Jaacanēnsium*
(Num 33:31), *Hebræus/-a* (15:12, as Exod 21:2), *Seboimōrum* (Gen 14:2), *Phasgæ*, and **23:4 *Beōris*** for 1738's
*Phegoris* (Balaam's father, Beor: בְּעוֹר, Βεώρ; Castellio's own slip, in 1726 too; the settled Num 22:5 *Beōris*). The
printed text keeps 1738's spellings.

## Spelling rules for new forms, researched and approved

`deut1-34-rules-research.md`, with the rows in `deut1-34-rules.tsv`: 54 word forms of approved families the rules did
not list (*adscendent → ascendent*, *adficiet → afficiet*, *caussas → causas*, *sumserunt → sumpserunt*, *tentaret →
temptaret*, *intelligemus → intellegemus*, *humeros → umeros*, *audiveritis → audieritis*, *pene → paene* …), each looked
up in Gaffiot and the corpus as you asked for Numbers. **Added to `data/rules/orthography.tsv` as approved** (Nathan,
2026-11-18: "Yes, add them") and the preview rebuilt: every one of the 54 words respelled, the readers' rows written in
the new spelling taking effect (*īnsūmptā*, *appāret*, *contemptīsque*, *audieritis* as future perfect). Three forms
the respelling unmarked are decided again: 5:25 *audierīmus* and 29:16 *trānsierīmus* (the readers' perfect
subjunctives), 33:8 *lacessīstī* (contracted, decision 26, as the settled *audīstī*); the 9:8 *pēne* row dropped (*pæne*
by the rule). No word is left `unknown`.

## For you

1. ~~Add the 54 spelling rows~~: done (your "Yes, add them", 2026-11-18; above).
2. ~~23:25 *introieris*~~: fixed (your "Fix the problems"): `normalize.EO` now lists *intrō-* among the *eō*
   compounds whose i stays a vowel (tested); the text reads *introieris*.
3. ~~14:16–17 *ībī*~~: fixed: `macronize.finish(…, decided=True)` lets a decided form keep the final ī that the brief's
   *ibi* rule shortens (`verses.decided_word`; tested); the text reads *ībī*.
4. **Quotation structure** (above): the BSB itself quotes 27:11–28:68 and 29:2–30:20 as speeches; I kept every long
   discourse of Moses unquoted, for one rule across the book. The alternative: chapter 28 and 29:2–30:20 in “…”,
   reopened at every paragraph.
5. **Names, hard calls** (`deut1-34-names.md`, each can be dropped): *Emenses*, *Hebræus*, *Jaacanēnsium*,
   *Seboimōrum*, 23:4 *Beōris*; *Cadēsbarnēa* kept (Deut's own, with the settled *Cadēs*), against the settled Num 32:8,
   34:4 *Gadēsbarnēa*.
6. **Smaller calls, made as recommended**: 33:26 `b q1`, a stanza break (the first in the Old Testament) so that
   Asher's closing ” and the new “ don't run together; 27:15–26 twelve paragraphs; God's speech in the Song closed at
   32:28, not the BSB's 32:27; 28:20 and 28:62 *-erītis* (relative clauses of cause and concession); 8:3, 8:16 *mannā …
   ignōtā* (Castellio's *manna* feminine; the settled John 6:58 treats it as neuter); 25:7 *glōssem* (Castellio's
   accusative of *glōs*, kept as printed); 25:10 “discalceātī.” quoted as a name (decision 39).

## Found in the settled text

**Exodus and Numbers fixed** (your "Fix … the problems in Exodus and Numbers"; `data/review/settled-fixes-deut.md`,
applied, gold rebuilt): Exod 12:15, 12:18, 12:20, 13:7 *fermentātīs*; Num *cis* six times; Num 32:8, 34:4
*Cadēsbarnēa*; Num 18:26, 33:54 *assign-*. Checked there and left: *sōlemn-* (Wiktionary and Macronizer mark
*sōlemnis*), *nōlitōte* (not in the settled text after all). As first listed: Exod 12:15, 12:18, 12:20, 13:7 *fermentātis* (ablative plural *fermentātīs*);
*nōlitōte* three times (*nōlītōte* twice, and throughout Deuteronomy); *adsignātās*, *adsignāverit* beside 11
*assign-*; *cīs* seven times in Numbers (Gaffiot *cĭs*); *Seirīs* at Gen 14:6, 36:21 (a genitive, short); Num 32:8, 34:4
*Gadēsbarnēa*; Mark 10:1 *trānsjordānīnum* in lower case; Mark 12:29 *Audī Isrāēlīta:* without the vocative's comma;
*sōlemnitāt-* 14 times (Gaffiot, Wiktionary *sollemnĭtās*, short o); and between books *Galaād-/Galaad-*,
*Jabboc-/Jabbōc-*, *Choriōs/Hōri-*, Naphtali's adjective three ways, *Ēsāō* (Gaffiot *Esāū*).

## Words to look at again (kept as printed)

3:25 *hanc mihi suo veniam daret* (*suam* expected; the page has *suo*), 27:1 *præcipit* (a historic present, or a
misprint for *præcēpit* as 27:11), 29:18 *absynthium* (Gaffiot *absinthium*: perhaps a spelling rule), 25:3
*Quadragesies* (classical *quadrāgiēs*). 26:5 *Syrīs eōs opprimentibus* departs from the Hebrew אֲרַמִּי אֹבֵד אָבִי: a
candidate for a light footnote when the notes are made (decision 56).
