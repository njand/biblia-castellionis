# Editorial brief

The rules every stage of the pipeline follows. Nathan approves each change to this file. Items marked
*(pending)* wait on a decision in `HUMAN.md`.

## Text

- **Base edition** *(pending, decision 1)*: the README names the 1726–27 edition as primary, with earlier
  editions consulted for unclear scans. Wikisource follows 1760 (NT) and 1738 (OT).
- **Versification**: the KJV's, everywhere (`data/versification/kjv.tsv`). Where an edition numbers verses
  differently (e.g. Genesis 2, 3, 4, 6, 7, 10, 18), the text is renumbered to the KJV and the mapping recorded.
- **Later-edition vocabulary**: the ecclesiastical terms of the later editions are kept (*baptīzō*, *angelus*), as
  the README says.
- No marginal notes or commentary. **Chapter summaries** *(pending, decision 3)*.

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
- **Quotation marks** *(pending, decision 4)*: the finished text uses “…” (LaTeX ``…'') for direct speech and ‘…’
  for reported discourse and quotes within quotes; the README says reported discourse is in single quotes.
- Punctuation may be modernized for clarity.
