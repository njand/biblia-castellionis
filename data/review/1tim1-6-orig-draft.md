# 1Tim 1–6 as printed (1573): the draft for review

Built 2026-11-15 by `python -m pipeline orig 1Tim 1-6` → `text/orig/draft/1TI.usfm`. The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/1Tim.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-15: "Approve them"); moved to `text/orig/1TI.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 1404 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 13 | read in the OCR, a spelling the approved rules normalize |
| variant | 16 | read in the OCR, a printer's spelling no rule covers |
| ę | 6 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 16 | read in the OCR with a nasal bar (m or n put back) |
| lexicon | 42 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 76 | read on the page image (data/decisions/<osis>.orig.tsv) |
| all | 1573 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **6.19** *præclārum* → *præclarum*: 1573 canvas 912, read on the page: ę (read by Claude, 2026-11-13)
- **6.13** *præclārā* → *præclara*: 1573 canvas 912, read on the page: ę; line break præ-clara (read by Claude, 2026-11-13)
- **5.13** *ōtiōsæ* → *ociosæ*: 1573, read on the page: æ or ę, the OCR's e notwithstanding (read by Claude, 2026-11-13)
- **1.4** *quam* → *quàm*: 1573 canvas 909, read on the page: grave on a (accents, decision 67) (Claude, 2026-11-14)
- **1.11** *quod* → *quod*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.12** *tantum* → *tantum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.14** *Vērum* → *verùm*: 1573 canvas 909, read on the page: grave on u (accents, decision 67) (Claude, 2026-11-14)
- **1.14** *cum* → *cum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.16** *ideō* → *ideo*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.19** *quā* → *qua*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.1** *prīmum* → *primum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.2** *cum* → *cum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.6** *quam* → *quam*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.9** *cum* → *cum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.11** *cum* → *cum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **2.15** *cum* → *cum*: 1573 canvas 909, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.3** *ā* → *à*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.4** *cum* → *cum*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.5** *quō* → *quo*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **3.13** *rēctē* → *rectè*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.3** *cum* → *cum*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.3** *vērum* → *verum*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *quod* → *quod*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.4** *cum* → *cum*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.5** *quod* → *quod*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.6** *quam* → *quam*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.10** *ideō* → *ideo*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **4.14** *quā* → *qua*: 1573 canvas 910, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.2** *cum* → *cum*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.8** *qua* → *qua*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.12** *Eō* → *eo*: 1573 canvas 911, read on the page: lower-case e; no accent (accents, decision 67) (Claude, 2026-11-14)
- **5.13** *quod* → *quod*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.13** *sōlum* → *solum*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.13** *vērum* → *verum*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.19** *Contrā* → *Contra*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.20** *quō* → *quo*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **5.25** *latēre* → *làtêre*: 1573 canvas 911, read on the page: circumflex on the second e, and a faint grave-like stroke over the a (accents, decision 67) (Claude, 2026-11-14)
- **6.1** *male* → *malè*: 1573 canvas 911, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **6.2** *ideō* → *ideo*: 1573 canvas 911, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.5** *Ā* → *A*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.7** *Cum* → *Cum*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.7** *profectō* → *profectò*: 1573 canvas 912, read on the page: split profe- / ctò; grave on o (accents, decision 67) (Claude, 2026-11-14)
- **6.12** *quam* → *quam*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.13** *vērum* → *verum*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.17** *largē* → *largè*: 1573 canvas 912, read on the page: grave on e (accents, decision 67) (Claude, 2026-11-14)
- **6.18** *rēctē* → *recte*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.20** *Ō* → *O*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **6.21** *Quam* → *quam*: 1573 canvas 912, read on the page (accents, decision 67) (Claude, 2026-11-14)
- **1.9** *jūstīs* → *iustis*: 1573 canvas 909, read on the page (guess word: a note letter b stands before it) (Claude, 2026-11-15)
- **1.19** *repulsā* → *repulsa*: 1573 canvas 909, read on the page (guess word: hyphenated repul-sa) (Claude, 2026-11-15)
- **3.2** *modestus* → *modestus*: 1573 canvas 910, read on the page (guess word) (Claude, 2026-11-15)
- **5.4** *parentibusque* → *parentibusque*: 1573 canvas 911, read on the page (guess word: hyphenated paren-tibusq;) (Claude, 2026-11-15)
- **5.6** *vīvēns* → *viuens*: 1573 canvas 911, read on the page (guess word: a note letter a follows it) (Claude, 2026-11-15)
- **5.10** *subvēnit* → *subuenit*: 1573 canvas 911, read on the page (guess word) (Claude, 2026-11-15)
- **1.13** *misertum* → *misertum*: 1573 canvas 909, read on the page (misread word) (Claude, 2026-11-15)
- **2.2** *tranquillam* → *tranquillam*: 1573 canvas 909, read on the page (misread word) (Claude, 2026-11-15)
- **2.13** *fōrmātus* → *formatus*: 1573 canvas 909, read on the page (misread word) (Claude, 2026-11-15)
- **4.14** *dōtem* → *dotem*: 1573 canvas 910, read on the page (misread word) (Claude, 2026-11-15)
- **5.21** *lēctōrum* → *lectorum*: 1573 canvas 911, read on the page (misread word: hyphenated lecto-rum) (Claude, 2026-11-15)
- **1.4** *īnstrūctiōnem* → *instructionem*: 1573 canvas 909, read on the page (none word) (Claude, 2026-11-15)
- **1.6** *vānitātem* → *vanitatem*: 1573 canvas 909, read on the page (none word: hyphenated va-nitatem (line end cut off in the crop)) (Claude, 2026-11-15)
- **1.9** *irreligiōsīs* → *irreligiosis*: 1573 canvas 909, read on the page (none word: hyphenated irreli-giosis (line end cut off in the crop)) (Claude, 2026-11-15)
- **1.10** *contrārium* → *contrarium*: 1573 canvas 909, read on the page (none word: read on page 909, top of the second column ("contrarium est,"); the crop showed the annotations) (Claude, 2026-11-15)
- **2.9** *verēcundiā* → *verecundia*: 1573 canvas 909, read on the page (none word: divided verecun / dia across lines (no hyphen visible)) (Claude, 2026-11-15)
- **3.13** *collocandā* → *collocanda*: 1573 canvas 909, read on the page (none word: hyphenated collo-canda (page 910; the crop showed 1.14)) (Claude, 2026-11-15)
- **3.16** *cōnspectus* → *conspectus*: 1573 canvas 910, read on the page (none word: hyphenated con-spectus) (Claude, 2026-11-15)
- **5.1** *Seniōrem* → *SEniorem*: 1573 canvas 911, read on the page (none word: chapter opening: drop-cap S followed by capital E ("SEniorem")) (Claude, 2026-11-15)
- **5.8** *domesticōrum* → *domesticorum|,*: 1573 canvas 911, read on the page (none word: 1573 prints a comma after it) (Claude, 2026-11-15)
- **5.8** *īnfīdente* → *infidente*: 1573 canvas 911, read on the page (none word: hyphenated infiden-te) (Claude, 2026-11-15)
- **5.11** *nūbere* → *nubere*: 1573 canvas 911, read on the page (none word: hyphenated nu-bere) (Claude, 2026-11-15)
- **5.18** *obtūrātō* → *obthurato*: 1573 canvas 911, read on the page (none word: printed with th: "os ne obthu- / rato :" (page 911; the h is small at page resolution but visible)) (Claude, 2026-11-15)
- **6.6** *contentum* → *contentum*: 1573 canvas 912, read on the page (none word: hyphenated con-tentum) (Claude, 2026-11-15)
- **6.10** *avāritia* → *auaritia*: 1573 canvas 912, read on the page (none word) (Claude, 2026-11-15)
- **6.14** *irreprehēnsibilis* → *irreprehensibilis*: 1573 canvas 912, read on the page (none word: hyphenated irrepre-hensibilis; nasal bar: printed "hẽsibilis") (Claude, 2026-11-15)
- **6.19** *congerentēs* → *congerentes*: 1573 canvas 912, read on the page (none word: hyphenated conge-rentes (page 912)) (Claude, 2026-11-15)

## Spellings the approved rules normalize (13)

*cāritās* → *charitas*; *cāritāte* → *charitate* ×3; *cāritātem* → *charitatem*; *intellegit* → *intelligit*; *intellegunt* → *intelligunt*; *intellegēns* → *intelligens*; *iīs* → *eis* ×2; *neglegere* → *negligere*; *obœdientiā* → *obedientia*; *temptātiōnem* → *tentationem*

## Printer's spellings no rule covers (16)

*auctōritātem* → *authoritatem*; *cārī* → *chari*; *cūriōsæ* → *curiose*; *dēnūntiā* → *denuncia*; *dēnūntiātō* → *denunciato*; *dēnūntiēs* → *denuncies*; *exsequāre* → *exequare*; *exsereret* → *exereret*; *fēminās* → *fœminas* ×2; *litteræ* → *literæ*; *pretium* → *precium*; *sæcula* → *secula*; *sæculōrum* → *seculorum*; *sōbriæ* → *sobrie*; *vindicāre* → *vendicare*

## Punctuation not from the OCR (6)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.4 *instructionem.*; 1.10 *est,*; 3.13 *libertatem.*; 5.11 *volunt:*; 6.6 *esse.*; 6.10 *auaritia:*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary: left out of the printed text, as of the reading edition (decisions 50, 67).
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
