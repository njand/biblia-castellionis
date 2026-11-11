# 2 Corinthians 1–13: stages 1–5, one proposal per verse

Proposed 2026-11-10; **approved by Nathan "for now" the same day and settled in `text/2CO.usfm`** (decision 38). Same tools and format as 1 Corinthians
(`data/review/1cor1-16-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier
work on 2 Corinthians; `TXT/1 - OCR` (the 1726–27 printing, uncorrected Google Books OCR) served as a witness, read
as an OCR.

## Where it stands

- **Stage 1**: `text/draft/2CO.usfm`, Wikisource's 2 Corinthians with the BSB's paragraphs: 257 verses, every chapter
  at the KJV count after 2 versification edits (`data/versification/2Cor.draft.edits.tsv`, applied). **Chapter 13
  lacks no words**: Wikisource and 1573 both have 13 verses there and both print the KJV's 13:13 (*Salutant vos sancti
  omnes*) inside their 12, so it is a split, as at 1 Cor 3:22–23; their 13 is the KJV's 14. The other edit: 7:15–16,
  where 1573 prints 16 before *Gaudeo, posse me* as the KJV and Wikisource runs it on. 1573 numbers chapter 1 with 23
  verses (its 21 = the KJV's 1:21–22); the KJV's numbering is kept.
- **Stage 2**: `data/review/2cor1-13-stage2.md`, **45 corrections** against the 1573 base, **read on the 1573 page
  images** (crops in `sources/mdz-1573/crops/2Cor.*`): 24 Wikisource slips (13:2 *seribo*, 3:10 *conseratur*, 7:10
  *mundamus*, 10:13 *eum* dropped, 10:4 *divinipotentia* split in two), 16 readings of the revised text (3:13
  *torpentes*, 5:17 *creatura*, 5:21 *peccatum*, 7:5 *caro*, 12:9 *mea gratia*, 13:14 *gratia*, 10:12 *ausimus*),
  1 s-for-f slip found by the sweep you asked for (4:4 *insidentium* → *infidentium*), 2 slips at 2:13 (*habuit*,
  *profectus, sum*) in verses 1573's OCR had not aligned (found during stages 3–5, see below), 2 word divisions.
  **Applied to the draft** (decision 30's standing rule). 1556 has nearly all the revisions already; the one 1573
  change found is 10:12 *ausimus* (1556 *audemus*), recorded as a variant. Spelling rules added: *arrhabonem*, and 15
  words under decision 37's principles (*adfligo → affligo* and the other *ad-* forms, *intelligunt*, *pertentate →
  pertemptate*, *paullo*, *paullulum* (as your *paulum* rule; settled *paulō* 9 : 1), *Sylvanum → Silvanum*).
- **Stages 3–5**: `data/review/2cor1-13-ch01.md` … `-ch13.md`, **257 items, all checking `ok`**; waiting for your
  approval. Preview: **`text/draft/2CO.preview.usfm`**, identical byte for byte to what `review apply --all` writes on
  a copy of the draft. Quotation marks balance in every verse and across verses (`structure.quotes`: nothing open or
  unclosed; no ‘…’ in the book). The subscription stands apart as `\cls` after 13:14 (decision 37). Ledger: chapters
  1–13 at **in-review**.

## What changed in the tools

- **`verses.lower_start`**: a verse continuing the sentence before starts in lower case unless its first word may name
  God; the check covered *Pater, Fīlius, Spīritus, Dominus …* but not *Deus*, so 9:13 *Deum collaudantēs* (after a
  comma) came out *deum* even with a layout line keeping the capital. Forms of *Deus* are now kept (a pagan *deus* at a
  verse start can still be lowered by its layout line). Test added (`pipeline/tests/test_verses.py`). Tests: 107 pass.
- **Not yet in code, worth adding to `collate`**: a list of verses where the base witness has no aligned text. Here
  1573's OCR reads the page's columns out of order at 2:9–13 (canvas 880), so the collation saw no 1573 text for those
  five verses and missed 2:13's two slips; 3:9, 4:18, 5:21, 6:1 and 8:24 were aligned only in part. All ten were then
  read by hand against 1573's page text and image.

## How the verses were made

- **Layout and macrons**: five readers (1–3, 4–6, 7–9, 10–11, 12–13) under one brief adapted from 1 Corinthians, each
  file checked by a script (layout words against the draft; every form against a word of its proposed verse; every word
  flagged homograph, unknown, Gaffiot's stem or your settled forms decided). Their calls are in
  `data/decisions/2Cor.layout.tsv` (45 lines) and `2Cor.forms.tsv` (254 rows, each with its reason). The
  settled-agreeing tier (646 words) was swept by the readers for **-a/-ā** and the other endings (rows where wrong: 1:1
  *tōtā*, 1:4 *nostrā*, *eā*, 1:6 and 1:11 *vestrā*, 1:8 *quantā*, 1:12 *dīvīnā* … *grātiā*, 2:4 *multā*, 3:2
  *Epistola*, 3:6 *littera*, 4:1 *dīvīnā*, 6:4 *multā*, 7:8 *epistola*, 8:22 *cōnfīdentia*, 9:14 *vōta*, 11:28
  *cūra*, 12:12 *summā patientiā*, 13:3 *petitis* (not *petītīs*), 13:2 *prædīcō* beside *prædīxī*, 6:11 *Ōs* (mouth),
  11:20 *ōs*), then by me with two sweeps over the preview: every form your settled books never write for a word they
  write at least 3 times (one: 11:28 *cūra*, the nominative, where the settled text has only *cūrā*), and every
  unmarked *-a* after an ablative preposition (none).
- **I then made the readers' calls agree with each other and with your settled books**: reader 2 had lowered nine verse
  starts after a colon (4:2 *quīn*, 4:9, 4:10, 5:15, 5:18, 5:19, 6:4, 6:10, and 4:4 *quōrum*); your settled text keeps
  the capital after a colon (1 Cor 41 : 1, Rom 54 : 1), so they keep it here. *Sānctī Spīritūs* (13:14) and *Spīritū
  Sānctō* (6:6) both capital, as every *Sānctus Spīritus* in the settled books. Five paragraph breaks dropped to come
  to 1 Corinthians' rate (below). *Spīritūs arrabōnem* capital at both 1:22 and 5:5.
- **Names new to the edition**: *Silvānum* (1:19; Gaffiot *Silvānus*), *Bēliale* (6:15; Gaffiot *Bēlĭal*), *Titus*
  unmarked (Gaffiot *Tĭtus*); unmarked where nothing tells the length: *Aretæ* (11:32). As settled: *Tīmotheus*,
  *Achāia*, *Macedonia*, *Jūdæa*, *Trōas*, *Mōsēs/Mōsis*, *Isrāēlītæ*, *Hebræī*, *Abrāhāmī*, *Satanās/Satanā/Satanæ*,
  *Damascī*, *Ēvam* (as Genesis), *Paradīsum* (as Luke 23:43), *Philippīs*, *Lūcam*.

## Flagged (960 words)

| Kind | Words |
|---|---:|
| homograph, your settled forms agreeing (no WordPress for 2 Corinthians) | 646 |
| decided by reading the verse | 261 |
| capital changed by a layout line (*Patre*, *Fīlius*, *Spīritus*, *Deum*, …) | 26 |
| lower case at a verse start | 25 |
| punctuation changed (verses) | 2 |
| **unflagged**: the lexicon's one marking | 3,367 |

31 verses have their quotation marks, poetry, capitals or markers changed by a layout line; 8 have nothing flagged.
The rates were not re-measured for this run.

## Calls worth a look

- **Scripture** in `\qt` with “…”. **Poetry** where the BSB sets it: 6:2 (Isa 49:8, after *Dīcit enim:*, prose again
  inside the verse with `\m` for *Adest nunc …*), 6:16–18 (Lev 26:12, Isa 52:11, 2 Sam 7:14: **one quotation over
  three verses**, as Castellio joins the sayings with *Quāpropter* and *Vōbīsque* and no new formula, like Rom 9:25–26;
  *inquit Dominus* and *inquit Dominus omnipotēns* outside the marks; the BSB closes and reopens it), 8:15 (Exod
  16:18), 9:9 (Ps 112:9; Castellio's *Quum dispergat … manet* in the indicative, so quoted, not reported). **Prose**
  `\qt`: 4:13 (Ps 116:10 *Crēdidī, ideōque locūtus sum*, after *ut fert scrīptum illud:*), 10:17 (Jer 9:24, as your 1
  Cor 1:31; *vērō* inside, as *enim* at 1 Cor 2:16). **13:1** (Deut 19:15, *Ex duōrum triumve testium ōre …*) is in
  `\qt` without a formula, as the BSB quotes it: the least certain (your Matt 18:16 has the same words unmarked inside
  an *ut* clause). **Left unmarked**: 4:6 (Gen 1:3, *lūcem … lūcēre jussit*, accusative and infinitive), 3:16 (Exod
  34:34) and 5:17 (Isa 43) as allusions, 9:6–7 (the proverb; Prov 22:8 LXX), 11:3 (the serpent and Eve).
- **Direct speech** in “…”: 10:10 the critics' words, *quod “epistolæ quidem (inquit) gravēs fortēsque sunt …”*, with
  *(inquit)* inside as your Exod 11:8 and 14:4; 12:9 the Lord's answer after *sīc dīxit:*, ending after *perficitur*
  as the BSB (*Itaque* is Paul's). **1:17–20, Paul's yes and no**: the words are marked as words named, in lower case,
  *“etiam, etiam”: et “nōn, nōn”?*, *“etiam,” et “nōn.”*, … and 1:20 *“ita”* (Castellio's word for the BSB's
  "Amen"), commas and full stops inside as your 1 Cor 14:16 *“Āmēn,”*. The Latin uses them as nouns (subjects of *sit*,
  *fuit*); unmarked is the alternative. **Unmarked**: 5:20 *reconciliāminī Deō* (Paul's own plea), 12:19 *vōbīs
  excūsāre nōs* (accusative and infinitive), the fool's speech 11:16–29 (Paul's own boasting).
- **Capitals** (decision 20): *Patre* 1:2, *Pater* 1:3 (twice: *Deus et Pater Dominī nostrī*, *misericordiæ Pater*),
  11:31; *Fīlius* 1:19; *Deum* 9:13 (above). *Spīritus* capital: 1:22, 3:3, 3:6 *at Spīritus vīvificat*, 3:8, 3:17
  (both: *Dominus autem Spīritus est … Dominī Spīritus*, the NRSV), 3:18, 5:5, 6:6 *in Spīritū Sānctō*, 13:14. Lower
  case: 3:6 *nōn litteræ, sed spīritūs* (NRSV "not of letter but of spirit"), 4:13 *eōdem fīdūciæ spīritū*, 11:4
  *alium spīritum*, 12:18 *eōdem animō*, **4:4 *hujus sæculī deus*** (Satan; 1573's margin glosses it *diabolus*),
  6:18 *Vōbīsque pater erō* (a predicate, NRSV "your father"), 12:2 *hominem chrīstiānum* (adjective, as your Rom
  15:29 *chrīstiānī*) beside 11:3 *in Chrīstiānīs* (noun, as 1 Cor and Acts).
- **Paragraphs**: of the BSB's 62 ordinary (`b m`) breaks where the draft had none, 15 taken (24%; 1 Corinthians 22%):
  1:8, 2:5, 2:14, 4:16, 5:20, 6:11, 7:2, 8:18, 9:6, 10:7, 11:7, 11:12, 12:14, 12:19, 13:5, each with its reason in
  the layout file. The readers had taken 20; I dropped the five that continue the argument before them (1:15, 3:12
  *Habentēs igitur*, 5:16 *Itaque*, 9:3, 11:30). `m` after poetry: 6:2 (inside the verse), 9:10.
- **Words no source marks**, decided from the Latin: *dīvīnipotentia* (10:4; Gaffiot's *dīvīnus* and *potēns*, on
  *omnipotēns*), *ūndēquadrāgēnīs* (11:24; *ūndēquadrāgintā*, *quadrāgēnī*), *inaspectābilis*, *īnfīdente*,
  *suscitātōrī*, *mœrōre*, *commendātītiīs* (Gaffiot *commendātīcius*), *patefactiōnēs/-um* and *rejectāne-* (as your
  settled forms), *erōque*, *legendaque*. Left unmarked: *penitissimaque* (as your *penitissimum*), *meipsum* (as your
  *seipsum*, *teipsum*).
- **Uncertain, for your eye**: 6:6 *in Spīritū Sānctō* capital (the NRSV reads "holiness of spirit"); 8:14
  *abundantiā vestrā* (ablative, with the impersonal *subvenīrī*); 8:16 *quī īdem* (masculine); 10:12 *ausīmus* (the
  old perfect subjunctive, Whitaker; Rom 15:18 *ausim*); 1:8 *pressī fuerīmus* (perfect subjunctive long, as your
  *-erīmus*; Acts 15:24 *mandāverimus* short); 11:28 *cūra* nominative; 13:1 in `\qt`; 1:17–20 in “…”.
- **From stage 2, for your eye**: 8:6 *ut nōs Titum hortātī sumus* (1573 and 1556 both print the indicative;
  Wikisource *simus*); 13:4 *per Deī in nōs potentiam* (1573, 1758, 1681; Wikisource and the Greek *in vōs*); and three
  places kept against 1573 with 1556: 5:10 *quisque* (1573 and 1556 *quique*), 11:28 *distinent* (1573 *destinent*),
  12:7 *tundat* (1573 *tondat*).
- **Punctuation**: 11:7 *docuī?* takes 1573's question mark (Wikisource a full stop); 13:14 *omnibus. Āmēn.* as 1573
  (Wikisource a colon).
- **Kept as printed**: 2:13 *valē
  dictō* (1573 *valedicto* in one word; your Acts *valē dict-*), 3:18 *eamdem* (your settled *eamdem* 2 : *eandem* 1),
  13:5 *annōn* (1573 *An non*; your settled both).
- **Title lines** (added when settled, as for 1 Corinthians): `\h`/`\toc2` *Ad Corinthiōs II*, `\toc1` and `\mt1`
  *Paulī Apostolī Epistola posterior ad Corinthiōs*, on the pattern of your *Epistola prior*. 1573 heads it *Epistola
  secunda* (1 Corinthians *prima*), but its argument says *in Epistolam posteriorem*.
- **Your settled text**: the readers found no marks in it that look wrong, so there is no `settled-fixes-2cor.md`.

## Questions for the whole edition

- ***quandōquidem***: your settled text writes *quandō-* (18×, 1 Corinthians included) and 2 Cor 5:4, 11:18, 13:3
  follow it; Gaffiot has *quandŏquĭdem* (short o, by iambic shortening). Keep, or follow Gaffiot everywhere?
- **Words named, not spoken** (1:17–20 *etiam*, *nōn*, *ita*): in “…” as here and 1 Cor 14:16 *“Āmēn”*, or unmarked?
- **A collation check for verses the base witness does not cover** (above): add it to `collate`?
