# 1Tim 1–6 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 1Tim 1-6` → `text/orig/draft/1TI.usfm` (now `text/orig/1TI.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1Tim.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/1TI.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1441 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 13 | read in the OCR, a spelling the approved rules normalize |
| variant | 16 | read in the OCR, a printer's spelling no rule covers |
| ę | 6 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 16 | read in the OCR with a nasal bar (m or n put back) |
| misread | 5 | the settled word misread by the OCR; spelling as settled |
| lexicon | 50 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 4 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 6 | OCR unreadable; the settled word in the printer's conventions |
| none | 16 | no OCR word; the settled word in the printer's conventions |
| all | 1573 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **6.19** *præclārum* → *præclarum*: 1573 canvas 912, read on the page: ę (read by Claude, 2026-11-13)
- **6.13** *præclārā* → *præclara*: 1573 canvas 912, read on the page: ę; line break præ-clara (read by Claude, 2026-11-13)
- **5.13** *ōtiōsæ* → *ociosæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (13)

*cāritās* → *charitas*; *cāritāte* → *charitate* ×3; *cāritātem* → *charitatem*; *intellegit* → *intelligit*; *intellegunt* → *intelligunt*; *intellegēns* → *intelligens*; *iīs* → *eis* ×2; *neglegere* → *negligere*; *obœdientiā* → *obedientia*; *temptātiōnem* → *tentationem*

## Printer's spellings no rule covers (16)

*auctōritātem* → *authoritatem*; *cārī* → *chari*; *cūriōsæ* → *curiose*; *dēnūntiā* → *denuncia*; *dēnūntiātō* → *denunciato*; *dēnūntiēs* → *denuncies*; *exsequāre* → *exequare*; *exsereret* → *exereret*; *fēminās* → *fœminas* ×2; *litteræ* → *literæ*; *pretium* → *precium*; *sæcula* → *secula*; *sæculōrum* → *seculorum*; *sōbriæ* → *sobrie*; *vindicāre* → *vendicare*

## Not read in the OCR (27)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 1Tim.1.4 | īnstrūctiōnem | instructionem | — |
| 1Tim.1.6 | vānitātem | vanitatem | — |
| 1Tim.1.9 | jūstīs | iustis | biustis |
| 1Tim.1.9 | irreligiōsīs | irreligiosis | — |
| 1Tim.1.10 | contrārium | contrarium | — |
| 1Tim.1.13 | misertum | misertum | misertuin |
| 1Tim.1.19 | repulsā | repulsa | sa |
| 1Tim.2.2 | tranquillam | tranquillam | tranquillain |
| 1Tim.2.9 | verēcundiā | verecundia | — |
| 1Tim.2.13 | fōrmātus | formatus | forinatus |
| 1Tim.3.2 | modestus | modestus | nodestus |
| 1Tim.3.13 | collocandā | collocanda | — |
| 1Tim.3.16 | cōnspectus | conspectus | — |
| 1Tim.4.14 | dōtem | dotem | dotein |
| 1Tim.5.1 | Seniōrem | Seniorem | — |
| 1Tim.5.4 | parentibusque | parentibusque | parentibus |
| 1Tim.5.6 | vīvēns | viuens | viuensa |
| 1Tim.5.8 | domesticōrum | domesticorum | — |
| 1Tim.5.8 | īnfīdente | infidente | — |
| 1Tim.5.10 | subvēnit | subuenit | sabuenit |
| 1Tim.5.11 | nūbere | nubere | — |
| 1Tim.5.18 | obtūrātō | obturato | — |
| 1Tim.5.21 | lēctōrum | lectorum | lectoruin |
| 1Tim.6.6 | contentum | contentum | — |
| 1Tim.6.10 | avāritia | auaritia | — |
| 1Tim.6.14 | irreprehēnsibilis | irreprehensibilis | — |
| 1Tim.6.19 | congerentēs | congerentes | — |

## Punctuation not from the OCR (6)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.4 *instructionem.*; 1.10 *est,*; 3.13 *libertatem.*; 5.11 *volunt:*; 6.6 *esse.*; 6.10 *auaritia:*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
