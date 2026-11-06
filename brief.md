# Editorial brief

The rules every stage of the pipeline follows. Nathan approves each change to this file. The decisions behind
them are dated in `HUMAN.md` § Decided.

## Text

- **Base edition**: the editions Wikisource transcribes, 1760 for the New Testament and 1738 (Leipzig) for the Old
  (decided 2026-11-05). Where another printing (1681, 1715, 1726–27, 1747, 1750, 1758) shows a genuinely
  different reading, it is recorded as a variant, not adopted. Scans of other editions still serve to correct
  OCR and transcription errors. Books Wikisource lacks follow 1738 for the OT; the 1750 Bible fills any
  gaps.
- **Finished chapters**: they were transcribed from 1726–27. Where their wording differs from the base
  edition, the pipeline proposes the change for review and never applies it on its own.
- **Versification**: the KJV's, everywhere (`data/versification/kjv.tsv`). Where an edition numbers verses
  differently (e.g. Genesis 2, 3, 4, 6, 7, 10, 18), the text is renumbered to the KJV and the mapping recorded.
  Psalm titles stay unnumbered above verse 1.
- **Later-edition vocabulary**: the ecclesiastical terms of the later editions are kept (*baptīzō*, *angelus*), as
  the README says.
- No marginal notes or commentary.
- **Chapter summaries** (the editions' *argumenta*) are printed as a small italic heading under each chapter
  number, normalized and macronized like the text. They are stored as verse 0 (`Matt.14.0`).
- **Apocrypha**: in scope, but after the 66 books (milestone M7). Placement is decided then.

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

## Macrons

- Every long vowel, including hidden quantities; not vowels long only by position.
- Gaffiot decides stems and hidden quantities; Wiktionary/Macronizer decide endings. When the sources disagree,
  flag it.
- Final -i short in *mihi, tibi, sibi, ubi, ibi*.
- Homographs (*venit/vēnit*, *-a/-ā*, *hic/hīc*) are decided per verse from the syntax, with the Greek/Hebrew tense
  or case as evidence.

## Layout

- Paragraphs with superscript verse numbers (`\Versus`); a blank line starts a paragraph.
- Poetry, including quoted Scripture set as verse, in `\begin{verse}\begin{patverse*}`, with
  `\indentpattern{…}` for indents; lines end `\\`.
- Quotations of earlier Scripture in italics (`\emph{…}`).
- **Quotation marks**: “…” (LaTeX ``…'') for direct speech; ‘…’ only for quotes within direct speech.
  **Reported discourse is not marked**: indirect statements, questions and commands stand as plain Latin
  (decided 2026-11-05). About 33 reported passages in the finished chapters are still in ‘…’ (John 17,
  Luke 10, Mark 6); the pipeline proposes removing them.
- Punctuation may be modernized for clarity.
