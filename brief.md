# Editorial brief

The rules every stage of the pipeline follows. Nathan approves each change to this file. The decisions behind
them are dated in `HUMAN.md` § Decided.

## Text

- **Base edition**: for the New Testament, Castellio's own last revision, the 1556 Basel edition (decided
  2026-11-06); for the Old, the 1738 Leipzig edition that Wikisource transcribes (decided 2026-11-05). Wikisource
  is the working text. Where it or another printing (1551, 1554, 1681, 1715, 1726–27, 1745, 1747, 1750, 1758,
  1760) differs from the base, the base reading is proposed and the others are recorded as variants. Scans of other editions still serve to correct
  OCR and transcription errors. Books Wikisource lacks follow 1738 for the OT; the 1750 Bible fills any
  gaps.
- **Finished chapters**: they were transcribed from 1726–27. Where their wording differs from the base
  edition, the pipeline proposes the change for review and never applies it on its own.
- **Versification**: the KJV's, everywhere (`data/versification/kjv.tsv`). Where an edition numbers verses
  differently (e.g. Genesis 2, 3, 4, 6, 7, 10, 18), the text is renumbered to the KJV and the mapping recorded.
  Psalm titles stay unnumbered above verse 1.
- **Later-edition vocabulary**: the ecclesiastical terms of the later editions are kept (*baptīzō*, *angelus*), as
  the README says.
- No marginal notes or commentary, but **brief Latin footnotes** where Castellio's reading departs from the Greek
  as read today (decision 53, 2026-11-12), or in the Old Testament from the Hebrew (decision 56, 2026-11-13), with the
  same light touch: `\f + \fr 19:24 \ft …\f*`, one line, after the word it explains
  (model: Matt 19:24 *Græcē κάμηλος, ‘camēlus’; Castelliō fūnem nauticum intellegit*;
  an Old Testament note begins *Hebraicē* the same way. Fixed formulas, as the NRSVue's, defined once in the front
  matter and never varied (`data/review/nt-notes-form.md` §3, `notes-audit.md`, 2026-11-18): NT *Cōdicēs antīquiōrēs
  habent / addunt* Greek, ‘Latin’ (*habent … sine …* for a word dropped where brackets cannot stand), *Græcē* Greek
  (the TR), ‘Latin’, for Castellio's sense or a slip in his text, with no tail; OT *Hebraicē* Hebrew, ‘Latin’, with
  *Castelliō … legit* where he read other consonants, *vōx* or *locus obscūrus* where the sense is uncertain, *ut
  Vulgāta* or *Castelliō Jōsēphum sequitur* for his source, and *Castelliō fīnxit* for his coinages; no reasons, no
  modern opinions, no *hodiē*, no cross-references; other verses cited *C:V*; only the words that differ quoted;
  words written out, not abbreviated (advised 2026-11-18, since the readers are learning Latin; to revisit if an OT
  search brings many notes citing the ancient versions);
  classical idiom preferred to Church Latin in the notes: not *Scrīptūra* for the Bible, nor *hodiernī* of people).
  **Only what matters to the story or the teaching** (Nathan, 2026-11-19: "Minor notes (e.g. rare names in lists) that
  don't really have any plot or theological significance can be dropped"): no note where the departure concerns only
  a name, a place, a number, a date, a material, a plant, a coin or a furnishing detail; a note where it changes what
  happens, what a law requires, or what a passage says about God, Christ or salvation. Glosses on a word no dictionary
  has (the coinages) stay. Applied to the existing notes in `data/review/notes-minor.md`.
- **Passages not in the earliest manuscripts** stay in Castellio's text, bracketed as NA28 and SBLGNT do (decision
  52): ⟦…⟧ around Mark 16:9–20 and John 7:53–8:11, […] around the verses and phrases the critical texts leave out;
  the front matter explains them.
- **Chapter summaries** (the editions' *argumenta*) are **not printed** (decision 50, 2026-11-12, reversing decision 3).
  The witnesses keep them as verse 0 (`Matt.14.0`); the builds still understand `\cd` should that change.
- **Apocrypha**: in scope, but after the 66 books (milestone M7). In the published Bible they stand in a **section of
  their own between the Testaments**, as the NRSV and most English Bibles have them, **in the order Castellio printed
  them** (decision 55, 2026-11-13). In 1573 most are interspersed in the Old Testament; taken in that sequence: Tobit,
  Judith, Wisdom, Ecclesiasticus, Baruch, the additions to Daniel, 3–4 Esdras, Maccabees (to be checked at M7).

## Orthography: Gaffiot 2016

- j for consonantal i; u/v distinguished; æ and œ written as ligatures for the diphthongs.
- Classical spellings as Gaffiot heads them (*cælum*, *arcessō*). Spellings recorded so far, seen in the
  finished chapters (M1 extracts the full list into `data/rules/orthography.tsv`):
  *temptō* (not *tentō*), *contiō* (not *conciō*), *umerus* (not *humerus*), *condiciō* (not *conditiō*),
  *quidquid* (not *quicquid*), *quattuor* (not *quatuor*), *iīs* (not *eīs*), *multō* (not *mulctō*),
  *subolēs* (not *sobolēs*), *mēcum* (not *mē cum*), *quænam* (not *quæ nam*), *septimō decimō* (two words).
  Not yet consistent: *ējiciō* (5×) against *ēiciō* (1×); M1 will list such cases for a decision.
- Capitals for the persons of God (*Pater*, *Fīlius*, *Spīritus Sānctus*).
- Proper names: as in the finished chapters (*Capharnaum*, *Jēsūs*, *Jācōbus*); a names list will be kept.
  **One form per person in both Testaments, the Old Testament's** (decided 2026-11-11, decision 46): *Hagar* in
  Galatians as in Genesis, *Nōa* in Matthew as in Genesis and Luke; where a New Testament book has the Greek or
  Vulgate form (*Agar*, *Noe*, *Elias*, *Esaias*), the Old Testament's is proposed, in its case.
- Words Gaffiot advises writing apart are written apart: *sē ipsum* (decision 51), *crucī fīgō* ("mieux"; decision
  52); *n* before *d* in *eundem*, *quendam* (decision 52).

## Macrons

- Every long vowel, including hidden quantities; not vowels long only by position.
- Gaffiot decides stems and hidden quantities; Wiktionary/Macronizer decide endings. When the sources disagree,
  flag it.
- Final -i short in *mihi, tibi, sibi, ubi, ibi*.
- *usque* with a short u, against Gaffiot's *ūsque*, with Wiktionary and Macronizer (decision 80): *usque*,
  *adusque*, *hūcusque*, *quousque* (joined, no macron); *eō usque* written apart.
- **Names** (decision 52): Gaffiot's marks first; then the Greek's long letters (η, ω, ει); then another dictionary
  that marks the word (Wiktionary's bare vowel counts as short); then the Hebrew vowel, as *Abrāhām*, *Dāvīd*.
- Homographs (*venit/vēnit*, *-a/-ā*, *hic/hīc*) are decided per verse from the syntax, with the Greek/Hebrew tense
  or case as evidence.

## Layout

Written in the USFM master (markers listed in PLAN.md §3); every output renders them the same way.

- Paragraphs (`\p`) with superscript verse numbers (`\v`). A paragraph of more than about 250 words is split
  where SBLGNT, or the BSB and WEB together, break and the Latin's sentence ends (decision 52).
- Poetry, including quoted Scripture set as verse, as indented lines (`\q1`, `\q2`, `\q3`).
- Quotations of earlier Scripture in italics (`\qt …\qt*`).
- **Quotation marks**: “…” for direct speech; ‘…’ only for quotes within direct speech.
  **Reported discourse is not marked**: indirect statements, questions and commands stand as plain Latin
  (decided 2026-11-05). About 33 reported passages in the finished chapters are still in ‘…’ (John 17,
  Luke 10, Mark 6); the pipeline proposes removing them.
- Punctuation may be modernized for clarity.
