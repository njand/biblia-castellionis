# 2Cor 1–13 as printed (1573): the draft for review

Built 2026-11-13 by `python -m pipeline orig 2Cor 1-13` → `text/orig/draft/2CO.usfm` (now `text/orig/2CO.usfm`). The words are the settled chapters' (`text/`); their spelling, capitals and punctuation are 1573 (MDZ bsb10141277)'s, read from its OCR as `pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as printed. Dropped: the accents (*verò*, *quòd*, *à*). One paragraph per verse, as 1573 sets them (HUMAN.md decision 57). Regenerate after changing `data/decisions/2Cor.orig.tsv`.

**Decision:** approved (Nathan, 2026-11-13: "Yes, approve NT"); moved to `text/orig/2CO.usfm`

## How each word was made

| Kind | Words | |
|---|---:|---|
| ocr | 3863 | read in the OCR as the settled word (u/v, i/j, long s as printed) |
| rule | 33 | read in the OCR, a spelling the approved rules normalize |
| variant | 24 | read in the OCR, a printer's spelling no rule covers |
| ę | 5 | read in the OCR as e against the settled æ: taken for the print's ę, printed æ |
| nasal | 34 | read in the OCR with a nasal bar (m or n put back) |
| misread | 6 | the settled word misread by the OCR; spelling as settled |
| lexicon | 229 | not read here; spelling as the base edition prints the same word elsewhere in the Testament |
| read | 3 | read on the page image (data/decisions/<osis>.orig.tsv) |
| guess | 28 | OCR unreadable; the settled word in the printer's conventions |
| none | 39 | no OCR word; the settled word in the printer's conventions |
| all | 4264 | |

## Read on the page

Where the OCR could not decide. Several differ from the settled text by more than spelling: the reading edition may want to look again at these (marked ⚑).

- **2.8** *exserātis* → *exeratis*: 1573 canvas 880, read on the page: no s (read by Claude, 2026-11-13)
- ⚑ **11.28** *distinent* → *destinent*: 1573 canvas 886, read on the page: printed deſtinent; differs from proposed (read by Claude, 2026-11-13)
- ⚑ **5.19** *iīs* → *eis*: 1573 canvas 882, read on the page (read by Claude, 2026-11-13)

## Spellings the approved rules normalize (33)

*cotīdiāna* → *quotidiana*; *cāritāte* → *charitate* ×2; *cāritātem* → *charitatem*; *cāritātis* → *charitatis*; *epistula* → *epistola* ×2; *epistulam* → *epistolam* ×2; *epistulæ* → *epistolæ*; *epistulās* → *epistolas* ×2; *epistulīs* → *epistolis*; *immō* → *imo* ×6; *intellegātis* → *intelligatis*; *iīs* → *eis* ×4; *obœdiendum* → *obediendum*; *obœdientia* → *obedientia*; *obœdientiam* → *obedientiam* ×2; *pertemptāte* → *pertentate*; *pæniteat* → *pœniteat*; *quattuordecim* → *quatuordecim*; *quidquam* → *quicquam*; *sæculī* → *seculi*

## Printer's spellings no rule covers (24)

*audīsse* → *audiuisse*; *cārissimī* → *charissimi*; *cēpī* → *cæpi*; *cētera* → *cætera*; *cēterum* → *cæterum* ×2; *cēterīs* → *cæteris*; *cēterīsque* → *cæterisque*; *cœpit* → *cepit*; *exstat* → *extat* ×2; *exsūgam* → *exugam*; *exsūxī* → *exuxi* ×2; *lacrimīs* → *lachrymis*; *littera* → *litera*; *litteræ* → *literæ*; *litterīs* → *literis*; *numquid* → *nunquid*; *quamquam* → *quanquam*; *quandōcumque* → *quandocunque*; *quācumque* → *quacunque*; *silvānum* → *syluanum*; *tamquam* → *tanquam*

## e against the settled æ, printed æ (1)

*cæleste* → *cœleste*

## Not read in the OCR (73)

Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.

| Verse | Settled | Printed | OCR |
|---|---|---|---|
| 2Cor.1.4 | cōnsōlātur | consolatur | — |
| 2Cor.1.7 | adversōrum | aduersorum | aduerforuin |
| 2Cor.1.8 | pressī | pressi | — |
| 2Cor.1.8 | dubitārēmus | dubitaremus | dubi |
| 2Cor.1.9 | cōnfīderēmus | confideremus | confidereinus |
| 2Cor.2.2 | oblectet | oblectet | oblecter |
| 2Cor.2.2 | contrīstētur | contristetur | contrifterur |
| 2Cor.2.7 | condōnētis | condonetis | condornetis |
| 2Cor.2.9 | facerem | facerem | — |
| 2Cor.2.9 | mōrigerī | morigeri | — |
| 2Cor.2.10 | condōnātis | condonatis | — |
| 2Cor.2.10 | condōnō | condono | — |
| 2Cor.2.10 | condōnāvī | condonaui | — |
| 2Cor.2.10 | condōnāvī | condonaui | — |
| 2Cor.2.10 | persōnā | persona | — |
| 2Cor.2.11 | circumveniāmur | circumueniamur | — |
| 2Cor.2.11 | cōnātūs | conatus | — |
| 2Cor.2.11 | ignōrāmus | ignoramus | — |
| 2Cor.2.12 | aperta | aperta | — |
| 2Cor.2.13 | invēnissem | inuenissem | — |
| 2Cor.2.14 | dīvulgat | diuulgat | diuulgar |
| 2Cor.3.1 | Ingredimur | Ingredimur | — |
| 2Cor.3.1 | commendāre | commendare | — |
| 2Cor.3.9 | excellit | excellit | — |
| 2Cor.3.10 | cōnferātur | conferatur | — |
| 2Cor.3.12 | perspicuitāte | perspicuitate | — |
| 2Cor.3.12 | ūtimur | vtimur | — |
| 2Cor.4.1 | dēfetīscimur | defetiscimur | defethifcimur |
| 2Cor.4.8 | æstuāmus | æstuamus | æituamus |
| 2Cor.4.9 | dējicimur | deiicimur | deijcinur |
| 2Cor.4.10 | repræsentētur | repræsentetur | — |
| 2Cor.4.16 | dēfetīscimur | defetiscimur | defethiscimur |
| 2Cor.5.1 | factam | factam | fatam |
| 2Cor.5.8 | māllēmus | mallemus | inallemus |
| 2Cor.5.16 | cognōvimus | cognouimus | — |
| 2Cor.5.19 | reconciliātiōnis | reconciliationis | dreconciliationis |
| 2Cor.5.19 | mandāverit | mandauerit | nandauerit |
| 2Cor.7.3 | damnandī | damnandi | daınnandi |
| 2Cor.7.16 | cōnfīdere | confidere | — |
| 2Cor.8.1 | Certiōrēs | Certiores | — |
| 2Cor.8.2 | penitissimaque | penitissimaque | penitissinaque |
| 2Cor.8.7 | excellitis | excellitis | — |
| 2Cor.9.7 | invītus | inuitus | innitus |
| 2Cor.9.7 | datōrem | datorem | datoren |
| 2Cor.10.3 | mīlitāmus | militamus | — |
| 2Cor.10.5 | dēturbāmus | deturbamus | derurbamus |
| 2Cor.10.10 | ōrātiōque | oratioque | — |
| 2Cor.10.10 | abjectā | abiecta | — |
| 2Cor.10.15 | normā | norma | norina |
| 2Cor.11.2 | trādendam | tradendam | — |
| 2Cor.11.4 | admīsistis | admisistis | adımisistis |
| 2Cor.11.5 | exīstimō | existimo | exiftino |
| 2Cor.11.10 | commissūrum | commissurum | comimiffurum |
| 2Cor.11.12 | adimam | adimam | adiman |
| 2Cor.11.13 | istīusmodī | istiusmodi | — |
| 2Cor.11.13 | trānsfōrmantur | transformantur | — |
| 2Cor.11.16 | dēmentem | dementem | denentein |
| 2Cor.11.16 | admittite | admittite | adımittite |
| 2Cor.11.17 | dēmentiam | dementiam | deinentiam |
| 2Cor.11.27 | nūditāte | nuditate | — |
| 2Cor.11.30 | glōriandum | gloriandum | — |
| 2Cor.12.1 | vīsiōnēs | visiones | — |
| 2Cor.12.7 | tundat | tundat | tondat |
| 2Cor.12.8 | facesseret | facesseret | facesserer |
| 2Cor.12.10 | contumēliīs | contumeliis | — |
| 2Cor.12.11 | dēbērem | deberem | — |
| 2Cor.12.11 | commendārī | commendari | cominendari |
| 2Cor.12.11 | īnferior | inferior | — |
| 2Cor.12.12 | Specimina | Specimina | — |
| 2Cor.12.12 | portentīs | portentis | — |
| 2Cor.12.15 | redamer | redamer | redainer |
| 2Cor.13.1 | testium | testium | eftium |
| 2Cor.13.5 | annōn | annon | An |

## Punctuation not from the OCR (35)

After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case word was dropped or corrected (stray). Not checked on the page.

1.1 *Paulus,*; 1.8 *dubitaremus.*; 2.8 *exeratis.*; 2.9 *scripsi,*; 2.9 *facerem,*; 2.9 *morigeri.*; 2.10 *condonatis,*; 2.10 *condono.*; 2.10 *condonaui,*; 2.10 *condonaui,*; 2.10 *Christi.*; 2.11 *Satana:*; 2.11 *ignoramus.*; 2.12 *venissem,*; 2.12 *ianua:*; 2.13 *habui,*; 2.13 *inuenissem.*; 2.13 *dicto,*; 2.17 *multi,*; 3.1 *commendare?*; 3.9 *iustitiæ.*; 3.17 *est,*; 3.17 *libertas.*; 6.2 *salutis.*; 7.9 *affecti.*; 7.16 *confidere.*; 8.3 *vltro,*; 8.6 *beneficium:*; 10.3 *militamus.*; 10.12 *intelligunt.*; 11.2 *tradendam.*; 11.13 *transformantur.*; 11.27 *nuditate:*; 12.6 *aliquid.*; 12.8 *facesseret:*

## Open questions

1. **Accents.** 1573 prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, or reading them page by page.
2. **Chapter summaries.** 1573 heads each chapter with a summary. The reading edition leaves them out (decision 50); the printed text could keep them.
3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; *plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.
4. **Castellio's L. … G. marks**: the words are kept, the marks dropped, as in the reading edition. None found by the aligner in these chapters.
5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).
