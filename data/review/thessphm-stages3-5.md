# 1 Thessalonians–Philemon: stages 1–5, one proposal per verse

Proposed 2026-11-11; **approved by Nathan "for now" the same day and settled in `text/1TH|2TH|1TI|2TI|TIT|PHM.usfm`** (decision 44). Same tools and format as Galatians–Colossians
(`data/review/galcol-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier
work on these books; `TXT/1 - OCR` (the 1726–27 printing, uncorrected) served as a witness, read as an OCR.

## Where it stands

| Book | Verses | Words | Stage 2 corrections | Layout lines | Forms decided | Items `ok` |
|---|---:|---:|---:|---:|---:|---:|
| 1 Thessalonians 1–5 | 89 | 1,354 | 20 | 12 | 72 | 89 |
| 2 Thessalonians 1–3 | 47 | 741 | 14 | 11 | 32 | 47 |
| 1 Timothy 1–6 | 113 | 1,581 | 30 | 17 | 112 | 113 |
| 2 Timothy 1–4 | 83 | 1,167 | 27 | 14 | 78 | 83 |
| Titus 1–3 | 46 | 633 | 16 | 12 | 48 | 46 |
| Philemon | 25 | 319 | 5 | 6 | 24 | 25 |
| **All** | **403** | **5,795** | **112** | **72** | **366** | **403** |

- **Stage 1**: `text/draft/1TH|2TH|1TI|2TI|TIT|PHM.usfm`, Wikisource with the BSB's paragraphs, already at the KJV's verse
  counts. Where Wikisource sets words a verse off the KJV, stage-2 Apply lines moved them: **1 Thess 5:16–18** (1573
  prints *Semper gaudete* / *continenter orate* / *in omnibus …* as three verses, as the KJV), **1 Tim 1:3–4** (*neve
  fabulas* opens 4, as 1573 and the KJV), **1 Tim 4:12–13** (*donec veniam* opens 13, as the KJV's "Till I come";
  1573 and Wikisource end 12 with it; added after the stage-3 reader found it), **Titus 3:5–6** (*renovationisque
  Spiritus Sancti* ends 5, as 1573 and the KJV). 1573 itself has no 1 Thess 3:11 (its 10 runs on) and numbers *Amen*
  as 1 Tim 6:17; the KJV's numbering is kept.
- **Stage 2**: `data/review/1thess1-5-stage2.md`, `2thess1-3-`, `1tim1-6-`, `2tim1-4-`, `titus1-3-`, `phlm1-stage2.md`,
  every correction **read on the 1573 page image** (crops in `sources/mdz-1573/crops/`, 163). Applied to the drafts
  (decision 30's standing rule). Wikisource is again the early wording: *favor → gratia* in every greeting and
  blessing, *Haereticum → Sectarium* (Titus 3:10), *in corpore → in carne* (1 Tim 3:16), *cinaedis → paediconibus*
  (1 Tim 1:10), *rem bonam → bonum munus* (1 Tim 3:1). Its slips include words lost: 1 Thess 2:9 *operando*, 3:13
  *Christi*; 2 Tim 1:7 *Deus*, 3:5 *vim*, 4:1 *regnoque*, 4:2 *importune*; Titus 1:4 *patre*, 1:16 *nefarii*; 1 Tim 5:10
  *si*. Word division: *sē ipsum* and *tē ipsum* divided (your settled 18 : 4 and 16 : 4), except Gal 5:14-style
  quotations; 2 Tim 2:15 and 1 Tim 4:7 *te ipsum*. **2 Tim 3:4**: Castellio's *L. caeci et G.* marks dropped, the words
  kept, as your Matt 19:4 (1573 and 1556 print the marks; 1758, 1715, 1750 drop them): **yours to confirm**. 1573's
  changes against 1556 are in `docs/editions.md`.
- **Stages 3–5**: `data/review/<book>-chNN.md`, 403 items, all checking `ok`. Previews **`text/draft/*.preview.usfm`**.
  Quotation marks balance in every book (`structure.quotes`: nothing open or unclosed; no ‘…’). Each subscription
  stands apart as `\cls`. Ledger: all 22 chapters **settled**.
- **Spelling rules added** (25 word rows, `orthography.tsv`): the *ad-* forms stage 2 listed (*assentatoria,
  alloquamur, affligeremur, affligentibus, afflictio, affligimini, aggregationem, affirment, afficiantur, afflictis,
  assiduam, assumptum, afferto, affecit, asseverare*) under decision 37; *temptasset*, *intellege*, *neglegere*
  (Gaffiot *neglegō*, as *intellegō*); *exstinguite* (settled 6 : 1); *sumptuoso*; *summoneo* (1573 and your
  *summonuit*); *accommodatus*; *gangraenae* (Gaffiot *gangræna*); *Silvanus* (as your 2 Cor 1:19 *Silvānum*);
  *adjutorique* (as every settled *adj-*).

## How the verses were made

- **Layout and macrons**: four readers (1–2 Thessalonians; 1 Timothy; 2 Timothy; Titus and Philemon) under the
  Galatians–Colossians brief, with the Greek (TR, SBLGNT), the BSB and the KJV beside each verse. Their calls, each with
  its reason, are in `data/decisions/{1Thess,2Thess,1Tim,2Tim,Titus,Phlm}.layout.tsv` and `.forms.tsv`. Each swept the
  endings (-a/-ā above all: about 25 ablatives in 1 Thessalonians alone); I then swept the six previews together: every
  form your settled books never write for a word they write 3 or more times (all right in their verses: *cārō*
  "dear" against your *carō* "flesh"; *positā* with *cāritāte* at 1 Tim 1:14 and 2 Tim 1:13, as the Greek's τῆς/τῇ ἐν
  Χριστῷ with ἀγάπη; *sānā*, *æternā*, *invidia*, *ūsūs*), every *-a* after an ablative preposition (three, all
  neuter accusatives: *in omnia*, *in perpetua*), and every word marked two ways across the six books (all case
  differences).
- **Perfect subjunctives** long, by your settled convention (*-erīs*, *-erīmus*, *-erītis*; the future perfect short):
  1 Thess *fuerītis*, *habuerīmus*, *converterītis*, *gesserīmus*, *trādiderīmus*, *didicerītis*; 1 Tim 5:19
  *admīserīs*, 6:7 *attulerīmus*; 2 Tim 3:14 *didicerīs*; Titus 3:5 *fēcerīmus*.
- **Paragraphs**: of the BSB's ordinary breaks the drafts lacked, 1 Thess 6 of 24 (25%), 2 Thess 3 of 10, 1 Tim 7 of 27
  (26%), 2 Tim 6 of 26 (23%), Titus 3 of 13, Philemon 2 of 8; none of the drafts' dropped.

## Calls worth a look

- **Scripture** in `\qt` with “…”: only **1 Tim 5:18** (*Ajunt enim litteræ:* Deut 25:4, as your 1 Cor 9:9, *et* the
  saying of Luke 10:7, *Dignus* capital as 1573) and **2 Tim 2:19** *“Nōvit Dominus quī sint suī”* (Num 16:5; the second
  clause, which the BSB also quotes, left unmarked: Castellio's *itaque* makes it Paul's inference). Left unmarked as
  allusions: 1 Thess 5:8; 2 Thess 1:8, 2:8; 1 Tim 2:13–14, 4:4, 5:19, 6:7; 2 Tim 4:14, 4:17.
- **Poetry, not Scripture**: **1 Tim 3:16** (*Deus apparuit in carne …*, the hymn, six lines after the BSB) and **2 Tim
  2:11–13** (the saying after *Certa rēs est:*), as Phil 2:6–11; no `\qt`.
- **Direct speech**: only **Titus 1:12**, the Cretan poet (Epimenides, as 1573's margin), in “…” after *Dīxit …
  vātēs:*, no `\qt`, as your 1 Cor 15:33 (Menander). Reported, so unmarked, where the BSB quotes: 1 Thess 5:3, 2 Thess
  2:2, 3:10, 1 Tim 4:1, the faithful sayings (1 Tim 1:15, 3:1, 4:9; 2 Tim 2:11), 2 Tim 2:18.
- **Capitals for God** (decision 20): *Pater* in every greeting; **_Servātor_ capital throughout** (Titus 1:3, 1:4,
  2:10, 2:13, 3:4, 3:6; 1 Tim 1:1, 2:3, 4:10 a predicate; 2 Tim 1:10), as 6 of your 7 settled places (Luke 1:47
  lower case: item 9 of `settled-fixes-galcol.md`). **Uncertain**: 1 Tim 3:16 *per Spīritum* (BSB "by the Spirit", NRSV
  "in spirit"); 1 Thess 1:6 *Sānctī Afflātūs* capital (the first in the edition; your settled *dīvīnō afflātū* is lower
  case); 2 Tim 4:8 *jūstus jūdex* lower case. Lower case: 2 Thess 2:4 *quidquid dīcitur deus* (as 2 Cor 4:4; 1573
  *Deus*), 2 Thess 2:8 *ōris suī spīritū* (breath), the human spirit (1 Thess 5:23, 1 Tim 4:12, 2 Tim 1:7), adjectives
  (*chrīstiānam*, *dominicæ*).
- **Greetings**: 1 Thess 1:1 *grātiam* lower case (it runs on within the verse, as 1573) against 2 Thess 1:2 *Grātiam*
  capital (its own verse, as Gal 1:3, 1 Cor 1:3): a visible difference between the two letters. 2 Tim 1:2 *fīliō
  grātiam* runs on as 1573.
- **Punctuation from 1573's page**: commas joining Greek one-sentence periods (1 Thess 1:2, 3:1; 2 Thess 1:3, 1:11, 2:1,
  2:3; Titus 1:3–4; 1 Tim 3:4, 3:15, 4:12), 1 Tim 3:5 *prōcūrābit?*, Philemon 1:5–6; before *Āmēn* each blessing keeps
  1573's own stop (colon, or **1 Thess 5:28 *grātia, Āmēn.*** with its comma, read on the image).
- **Words no source marks**, decided from the Latin: *assentātōriā* (1 Thess 2:5), *refrāctāriī*, *respōnsātōrēs*
  (Titus), *inaspectābilī* (1 Tim 1:17, as Col 1:15), **_Pācātiānæ_** (1 Tim 6:21, uncertain), **_Eunīcā_** (2 Tim
  1:5, from Gaffiot's *Eunīcus*; uncertain), **_Zēnam_** (Titus 3:13, from the Greek eta; least sourced); unmarked
  *Loide*, *Phygelus*, *Jannes*, *Jambres*, *Artemas*, *Appia*.
- **Names new to the edition**: *Hymenæus*, *Philētus*, *Onēsiphorus*, *Hermogenēs*, *Crēscēns*, *Dalmatia*, *Carpus*,
  *Eubūlus*, *Pudēns*, *Linus*, *Claudia*, *Nerō*, *Lāodicēa*, *Nīcopolis*, *Zēnas*, *Philēmōn*, and those above. As
  settled: *Silvānus*, *Tīmotheus*, *Tychicus*, *Titus*, *Mārcus*, *Lūcās*, *Dēmās*, *Prīsca*, *Aquila*, *Onēsimus*.
- **Stage 2, for your eye**: 1 Thess 2:8 *Sic nos* kept against 1573's misprint *ſic vos*; 2 Tim 3:4 (above); 1 Tim
  1:10 *paediconibus* (1573's word for the Greek ἀρσενοκοίταις); 1 Tim 5:4 *quae vidua* (1573 and 1556).

## Questions for the whole edition

- **2 Tim 4:13 *Pēnulam***: Gaffiot heads *pēnŭla* beside *pænŭla*; the corpus favours *paenula* (Cicero). A rule
  *Penulam → Paenulam* under decision 42? Not added.
- **1 Thess 1:1 / 2 Thess 1:2** greeting capitals (above): keep as printed, or one form?
- **2 Tim 3:4** L. … G. marks (above).
- **Your settled text**: Matt 12:26 *Satanām*, proposed in `data/review/settled-fixes-thessphm.md`.
- **Title lines** (added when settled, on the pattern of Corinthians): `\h`/`\toc2` *Ad Thessalonīcēnsēs I/II*, *Ad Tīmotheum I/II*,
  *Ad Titum*, *Ad Philēmonem*; `\mt1` *Paulī Apostolī Epistola prior / posterior ad …* (1573: *Epistola prima / secunda ad
  Thessalonicenses*, canvases 904, 907; *prima ad Timotheum*, 909), *Epistola ad Titum* (915), *ad Philēmonem* (916).
