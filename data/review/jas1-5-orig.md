# Jas 1–5 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig Jas 1-5` → `text/orig/draft/JAS.usfm` (now `text/orig/JAS.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/Jas.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/JAS.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1456 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 14 | read in the OCR, a spelling the approved rules normalize |
| variant | 21 | read in the OCR, a printer's spelling no rule covers |
| ę | 3 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 19 | read in the OCR with a nasal bar (m or n put back) |
| misread | 3 | the settled word misread by the OCR; spelling as settled |
| lexicon | 62 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 1 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 4 | OCR unreadable; the settled word in the printer's conventions |
| none | 11 | no OCR word; the settled word in the printer's conventions |
| all | 1594 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- ⚑ **.5** *lascīvīstis* → *lasciuijstis*: 1573 canvas 919, read on the page (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (14)

*cotīdiānōque* → *quotidianoque*; *exspectat* → *expectat*; *intellegat* → *intelligat*; *intellegentēs* → *intelligentes*; *intellegere* → *intelligere*; *intellegēns* → *intelligens*; *iīs* → *eis*; *quemquam* → *quenquam*; *quidquam* → *quicquam*; *temptat* → *tentat*; *temptārī* → *tentari*; *temptātur* → *tentatur* ×3

## Printer's spellings no rule covers (21)

*annulōs* → *anulos*; *audīstis* → *audiuistis*; *cārissimī* → *charissimi* ×2; *effrēnātum* → *effrænatum*; *exsecrāmur* → *execramur*; *exsecūtor* → *executor*; *exsequitur* → *exequitur*; *exstat* → *extat*; *frēnat* → *frænat*; *frēnāre* → *frænare*; *frēnōs* → *frænos*; *fēminæ* → *fœminæ*; *hērēdēsque* → *hæredesque*; *litterīs* → *literis* ×2; *nūntiīs* → *nuncijs*; *quōcumque* → *quocunque*; *submittite* → *sumittite*; *tamquam* → *tanquam*; *umquam* → *vnquam*

## Not read in the OCR (18)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| Jas.1.3 | explōrātiōne | exploratione | — |
| Jas.1.17 | umbra | vmbra | avmbra |
| Jas.2.12 | loquiminī | loquimini | — |
| Jas.2.15 | alimentō | alimento | — |
| Jas.2.16 | calefierīque | calefierique | caleficrique |
| Jas.3.6 | scelerum | scelerum | scelerumb |
| Jas.3.6 | contāmināns | contaminans | — |
| Jas.3.6 | gehennā | gehenna | — |
| Jas.3.7 | ferārum | ferarum | feraruin |
| Jas.3.15 | proficīscātur | proficiscatur | — |
| Jas.3.16 | incōnstantia | inconstantia | — |
| Jas.4.7 | fugiet | fugiet | — |
| Jas.4.10 | ēvehet | euehet | euchet |
| Jas.4.11 | condemnātor | condemnator | — |
| Jas.5.4 | mercēnāriōrum | mercenariorum | inercenariorum |
| Jas.5.5 | indulsistis | indulsistis | — |
| Jas.5.9 | damnēminī | damnemini | dannemini |
| Jas.5.15 | allevābit | alleuabit | — |

## Punctuation not from the OCR (7)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.23 *est,*; 1.27 *mundo.*; 2.14 *fides?*; 2.24 *fide.*; 3.16 *inconstantia,*; 4.7 *fugiet:*; 4.11 *condemnator.*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. Found here: 5.3 *Pœnam*.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
