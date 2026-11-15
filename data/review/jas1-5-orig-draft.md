# Jas 1–5 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig Jas 1-5` → `text/orig/draft/JAS.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Jas.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/JAS.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1429 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 16 | read in the OCR, a spelling the approved rules normalize |
| variant | 19 | read in the OCR, a printer's spelling no rule covers |
| ę | 3 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 19 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 61 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 47 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 1594 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **5.5** *lascīvīstis* → *lasciuijstis*: 1573 canvas 919, read on the page (read by Claude, 2026-11-13)
- **1.5** *vestrum* → *vestrûm*: 1573 canvas 917, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **1.6** *cum* → *cum*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *cum* → *cum*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *cum* → *cum*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.12** *quam* → *quam*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.17** *supernē* → *supernè*: 1573 canvas 917, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **2.2** *vestrum* → *vestrum*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.3** *hīc* → *hic*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.3** *hīc* → *híc*: 1573 canvas 917, read on the page: accent on the i; the stroke rises to the right like an acute, unlike the circumflex hîc elsewhere; please check (accents, decision 67) (Claude, 2026-11-14)
- **2.5** *quod* → *quod*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.7** *quō* → *quo*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.9** *contrā* → *contra*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *contrā* → *contra*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.16** *vestrum* → *vestrûm*: 1573 canvas 917, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **2.16** *cum* → *cum*: 1573 canvas 917, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.23** *quod* → *quod*: 1573 canvas 918, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.24** *sōlum* → *solum*: 1573 canvas 918, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.13** *cum* → *cum*: 1573 canvas 918, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.14** *Quod* → *Quòd*: 1573 canvas 918, read on the page: grave on o (accents, decision 67) (Claude, 2026-11-14)
- **3.14** *contrā* → *contra*: 1573 canvas 918, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.14** *vērum* → *verum*: 1573 canvas 918, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *Ō* → *O*: 1573 canvas 918, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.3** *contrā* → *contra*: 1573 canvas 919, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.7** *eō* → *eo*: 1573 canvas 919, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.13** *vestrum* → *vestrûm*: 1573 canvas 919, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **5.14** *vestrum* → *vestrûm*: 1573 canvas 919, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **5.19** *vestrum* → *vestrûm*: 1573 canvas 919, read on the page: circumflex on u (accents, decision 67) (Claude, 2026-11-14)
- **5.19** *vērō* → *vero*: 1573 canvas 919, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.17** *umbra* → *vmbra*: 1573 canvas 917, read on the page (guess word: marginal note letter a before it) (Claude, 2026-11-15)
- **3.6** *scelerum* → *scelerum*: 1573 canvas 918, read on the page (guess word: marginal note letter b after it, then "mundus.") (Claude, 2026-11-15)
- **4.10** *ēvehet* → *euehet*: 1573 canvas 918, read on the page (guess word) (Claude, 2026-11-15)
- **5.9** *damnēminī* → *damnemini*: 1573 canvas 919, read on the page (guess word) (Claude, 2026-11-15)
- **2.16** *calefierīque* → *calefierique*: 1573 canvas 917, read on the page (misread word: printed "cale-fieriq;", hyphenated) (Claude, 2026-11-15)
- **3.7** *ferārum* → *ferarum*: 1573 canvas 918, read on the page (misread word) (Claude, 2026-11-15)
- **5.4** *mercēnāriōrum* → *mercenariorum*: 1573 canvas 919, read on the page (misread word) (Claude, 2026-11-15)
- **3.6** *gehennā* → *gehenna*: 1573 canvas 918, read on the page (prone word: hyphenated; only "na inflammanda." visible at line start, the first part is cut off on the crop) (Claude, 2026-11-15)
- **5.15** *allevābit* → *alleuabit*: 1573 canvas 919, read on the page (prone word: split across lines "alleua / bit" with no hyphen visible) (Claude, 2026-11-15)
- **1.3** *explōrātiōne* → *exploratione*: 1573 canvas 917, read on the page (none word: hyphenated explo-ratione (read on page 917; the crop cut off the first half)) (Claude, 2026-11-15)
- **2.12** *loquiminī* → *loquimini*: 1573 canvas 917, read on the page (none word: printed abbreviated, "loq" with a stroke through the q's tail for "qui" + "mini" (loꝗmini); expanded here) (Claude, 2026-11-15)
- **2.15** *alimentō* → *alimento*: 1573 canvas 917, read on the page (none word: hyphenated ali-mento (page 917)) (Claude, 2026-11-15)
- **3.6** *contāmināns* → *contaminans*: 1573 canvas 918, read on the page (none word: hyphenated conta-minans (the first half at the line end cut off in the crop)) (Claude, 2026-11-15)
- **3.15** *proficīscātur* → *proficiscatur*: 1573 canvas 918, read on the page (none word: hyphenated [proficisca]-tur:; the first half at the line end is cut off in the crop) (Claude, 2026-11-15)
- **3.16** *incōnstantia* → *inconstantia*: 1573 canvas 918, read on the page (none word: hyphenated inconstan-tia) (Claude, 2026-11-15)
- **4.7** *fugiet* → *fugiet*: 1573 canvas 918, read on the page (none word) (Claude, 2026-11-15)
- **4.11** *condemnātor* → *condemnator*: 1573 canvas 918, read on the page (none word: the turnover is set at the end of the line above: "damnat. (condemnator.") (Claude, 2026-11-15)
- **5.5** *indulsistis* → *indulsistis*: 1573 canvas 919, read on the page (none word: hyphenated indulsi-stis) (Claude, 2026-11-15)

## Spellings the approved rules normalize (16)

*cotīdiānōque* → *quotidianoque*; *exsecrāmur* → *execramur*; *exsecūtor* → *executor*; *exspectat* → *expectat*; *intellegat* → *intelligat*; *intellegentēs* → *intelligentes*; *intellegere* → *intelligere*; *intellegēns* → *intelligens*; *iīs* → *eis*; *quemquam* → *quenquam*; *quidquam* → *quicquam*; *temptat* → *tentat*; *temptārī* → *tentari*; *temptātur* → *tentatur* ×3

## Printer's spellings no rule covers (19)

*annulōs* → *anulos*; *audīstis* → *audiuistis*; *cārissimī* → *charissimi* ×2; *effrēnātum* → *effrænatum*; *exsequitur* → *exequitur*; *exstat* → *extat*; *frēnat* → *frænat*; *frēnāre* → *frænare*; *frēnōs* → *frænos*; *fēminæ* → *fœminæ*; *hērēdēsque* → *hæredesque*; *litterīs* → *literis* ×2; *nūntiīs* → *nuncijs*; *quōcumque* → *quocunque*; *submittite* → *sumittite*; *tamquam* → *tanquam*; *umquam* → *vnquam*

## Punctuation not from the OCR (7)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.23 *est,*; 1.27 *mundo.*; 2.14 *fides?*; 2.24 *fide.*; 3.16 *inconstantia,*; 4.7 *fugiet:*; 4.11 *condemnator.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. Found here: 5.3 *Pœnam*.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
