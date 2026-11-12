# Hebrews and James: stages 1–5, one proposal per verse

Proposed 2026-11-12; **approved by Nathan "for now" the same day and settled in `text/HEB|JAS.usfm`** (decision 47), the
title lines and the calls below as proposed. Same tools and format as 1 Thessalonians–Philemon
(`data/review/thessphm-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier
work on these books; `TXT/1 - OCR` (the 1726–27 printing, uncorrected) served as a witness, read as an OCR.

## Where it stands

| Book | Verses | Words | Stage 2 corrections | Layout lines | Forms decided | Items `ok` |
|---|---:|---:|---:|---:|---:|---:|
| Hebrews 1–13 | 303 | 4,533 | 60 | 102 | 98 | 302 + 1 unchanged (10:9) |
| James 1–5 | 108 | 1,593 | 19 | 21 | 33 | 108 |
| **All** | **411** | **6,126** | **79** | **123** | **131** | **411** |

- **Stage 1**: `text/draft/HEB.usfm`, `JAS.usfm`, Wikisource with the BSB's paragraphs. **Hebrews 7 and 8 had a verse
  too many**: 1573 itself (canvases 932–933) and Wikisource number *Hoc enim semel fecit, dum seipsum libavit* as 7:28
  and *Quod autem antiquatur ac senescit* as 8:14; both are joined to the verse before, where the KJV has them (7:27
  "for this he did once", 8:13 "Now that which decayeth"; `data/versification/Heb.draft.edits.tsv`). James needed
  none.
- **Stage 2**: `data/review/heb1-7-stage2.md`, `heb8-13-stage2.md` (Hebrews in two halves), `jas1-5-stage2.md`; every
  correction **read on the 1573 page image** (crops in `sources/mdz-1573/crops/{Heb,Jas}.*`, 144), and the doubtful
  ones checked again by me on the crops (Heb 2:16, 7:5, 9:1, 11:4; Jas 4:10–11, 5:16). Applied to the drafts (decision
  30's standing rule). **In 1573 Hebrews stands last of the letters, after Jude** (canvases 929–937), headed
  *EPISTOLA AD HEBRAEOS* with no author; James follows Philemon (916–919), *IACOBI APOSTOLI EPISTOLA*.
  - Wikisource is again the early wording: Heb 2:16 *Non enim angelis, sed Abrahae posteris pitulatur* (its own slip for *opitulatur*) → *angelos, sed
    Abrahami semen assumpsit*; *sacrarium → sanctuarium* (8 places in 9–13, a 1573 change); 3:8, 3:15, 4:7 *mentes
    obfirmare vestras → indurare corda vestra*; 12:1 *fastu, tenacique → onere, ambitiosoque*; Jas 1:4 *perfectam
    actionem → perfectum opus*, 5:16 *viri boni → justi*, 4:11 *Fratres* dropped (1573 and 1556 lack it).
  - Wikisource's slips include words lost: Heb 8:12 *tum*, 11:11 *aetatis*, 12:26 *concussit, et nunc ita*, 13:23 *si*;
    Jas 4:1 *et → ex*, 3:3 *parcant → pareant*, 2:19 *credit → credis*.
  - Word division: *sē ipsum* divided (Heb 6:13, 7:27, 9:7, 9:14, 9:25; Jas 1:24), Heb 9:24 *manu factum* (as 9:11);
    Jas 2:8 *teipsum* kept joined, the quotation of Lev 19:18 as your Gal 5:14.
  - 1573's changes against 1556 (Heb 1:13, 2:18, 3:8/3:15/4:7, 4:10, 5:6, 5:7, 7:2, 7:25, 9:1–13:11 *sanctuarium*,
    9:3, 11:3, 11:23, 12:1; Jas 1:4, 2:13, 2:22, 3:17) are in section 5 of each file and in `docs/editions.md`. Several
    of the Hebrews ones match the Vulgate, with no *L. … G.* marks.
- **Stages 3–5**: `data/review/heb1-13-chNN.md` (13 files), `jas1-5-chNN.md` (5), 411 items, all checking. Previews
  **`text/draft/HEB.preview.usfm`**, **`JAS.preview.usfm`**. Quotation marks balance in both books (`structure.quotes`:
  Hebrews 44 “, 2 ‘, 113 `\qt` lines; James 12 “, 6 `\qt`). Ledger: all 18 chapters **settled**.
- **Spelling rules added** (23 word rows, `orthography.tsv`, under decisions 37 and 42): the *ad-* forms the stage-2
  files listed (*allectus, assequi, afflictate, affligitur, allevabit; affinis, astat, aspergens, affecerit, aspiceret,
  assequerentur, assiduum*), *temptatur, temptat, temptationis, temptavere, temptantur, temptati* (decision 37),
  *gehenna* (Jas 3:6, as your 11 settled *gehenn-*), *perpaulo* (Heb 10:37; the stem rule *paull → paul* reaches only
  words that begin with it), and *intellegat, intellegentes, intellegimus* (found when Jas 1:3 and 5:20 kept *-ll-*
  beside 2:20 *intellegere*).

## How the verses were made

- **Layout and macrons**: three readers (Hebrews 1–7, Hebrews 8–13, James) under the brief of the earlier letters, with
  the Greek (TR, SBLGNT), the BSB and the KJV beside each verse. Their calls, each with its reason, are in
  `data/decisions/{Heb,Jas}.layout.tsv` and `.forms.tsv`. I then read both previews whole. Changed after that reading:
  **Heb 8:2 *sānctuāriī*** lower case (the sentence of 8:1 runs on, 1573 *in cælis, 2 ſanctuarij*; the pipeline kept the
  capital because your settled text never writes the word lower case at a verse start), **Heb 11:2 *in eā*** (the
  ablative, faith of 11:1, ἐν ταύτῃ), and the note for Heb 9:14 restored (below).
- **Endings swept**: in Hebrews about 30 *-a/-ā* corrections (1:3 *fōrma*, *factā*; 2:3 *tantā … neglēctā*; 7:7 *ūllā
  contrōversiā*; 10:26 *datā operā*; 11:29 *terrā siccā*), the fourth declension (*spīritūs*, *vocātūs*, *sēnsūs*,
  *tribūs*, *specūs*, *īnsultūs*), *hīc* (4:5, 7:8, 13:14), *lībet* "offer" (5:1, 8:3), *novī* (9:15, 12:24), *īdem*
  (13:8), *lectus* "bed" (13:4); in James about 20 (1:4 *nūllā*, 1:5 *sapientiā*, 1:6 *fīdūciā*, 2:21 *ārā*, 3:11 *aquā
  … amārā*, 2:3 *hīc* ×2, 2:8 *pārētis*, 3:12 *fīcūs*).
- **Capitals after a colon** at a verse start are kept, as in your settled letters (Romans 55 : 1, the other letters
  without exception), though 1573 prints some lower case (Jas 2:3 *& vos*, 3:10 *prodeunte*).
- **Paragraphs**: of the BSB's ordinary breaks the drafts lacked, Hebrews 1–7 took 8 (27%), Hebrews 8–13 17 of 60 (28%),
  James 7 of 26 (27%), each with its reason; none of the drafts' own dropped. After poetry, prose resumes with `\m`.

## Calls worth a look

- **Scripture in Hebrews** in `\qt` with “…”, **as poetry where the BSB sets it**: the catena 1:5–13 (Ps 2:7, 2 Sam
  7:14 with *Et rūrsum:* between, Deut 32:43, Ps 104:4, Ps 45:6–7, Ps 102:25–27, Ps 110:1), 2:6–8 (Ps 8; three lines in
  2:7, as the Latin keeps *et operibus præfēcistī*), 2:12–13, 3:7–11 and 3:15 (Ps 95), 4:3, 5:5–6, 7:17, 7:21 (the oath
  in ‘…’ inside), **8:8–12 (Jer 31:31–34)**, 10:5–7 (Ps 40, *‘Ēn adsum …’* inside), 10:16–17, 10:37–38 (Hab 2:3–4),
  12:5–6 (Prov 3:11–12), 13:5–6. **As prose**: 4:4 (Gen 2:2), 4:5, 4:7, 6:14 (Gen 22:17), 8:5 (Exod 25:40, *“Vidē,”
  inquit, “ut …”*), 9:20, 10:8, 10:30, 12:20, 12:26. A bracketed *(inquit Dominus)* stays inside the `\qt` (8:8, as Rom
  14:11, Eph 4:8); an unbracketed one stands outside (8:9, 8:10, 10:16, 10:30, as Rom 12:19). In 1:5 and 1:13 the
  question mark is the writer's and follows the closing mark (*genuī tē”?*, as Matt 22:44).
  - **Uncertain**: 4:5 *“Nōn esse … ingressūrōs”* marked though an infinitive (the words of 3:11 cited as a text).
  - **Left unmarked**: 3:10–11's inner speech (reported, as Rom 9:26), 3:18, 10:13, 10:28, 11:18, 12:21; **12:29 *Est
    enim Deus noster ignis edāx*** (Deut 4:24; the writer's own sentence with *enim* and *noster*; the BSB quotes it):
    yours to decide.
- **Scripture in James**: 2:8 (Lev 19:18), 2:11 (*“Nē adulterātō,” … “Nē occīditō.”*, as Rom 13:9), 2:23 (Gen 15:6, as
  Rom 4:3 and Gal 3:6; *et Deī amīcus est appellātus* outside), 4:6 (Prov 3:34, two lines of poetry, *(inquit ille)*
  inside, as Eph 4:8). Unmarked: 4:5 (no OT verse says it), the allusions 1:10–11, 5:4, 5:11, 5:20, and the reported
  1:13, 2:16.
- **Words named** (decision 39): Heb 4:7 *“hodiē” dīcēns*, 7:2 *“jūstitiæ rēx”*, *“pācis rēx,”* (**uncertain**; *Solymæ
  rēx* left as his title), 12:27 *“Adhūc semel,”*; Jas 5:12 *ut “etiam” sit etiam, et “nōn” nōn* (only the word named,
  not the predicate; your Matt 5:37 sets *‘etiam, etiam’, ‘nōn, nōn’* in single marks, before decision 39).
- **Direct speech** in James: 2:3 (two speeches), 2:18 the objector *“Tū fidem habēs; ego opera habeō.”* (**uncertain**:
  his words may run to the end of the verse), 4:13, 4:15.
- **Capitals for God** (decision 20): *Fīlius* throughout Hebrews (1:2, 1:5, 1:8, 3:6, 4:14, 5:5, 5:8, 6:6, 7:3, 7:28,
  10:29), *Pater* 1:5 and 12:9 *spīrituum Patrī*, *Spīritus Sānctus* (2:4, 3:7, 6:4, 9:8, 10:15), 10:29 *grātiæ
  Spīritum*; James *Patre*/*Patrem* (1:17, 1:27, 3:9). **Uncertain**: **Heb 1:8 *ō Dīve*** (ὁ θεός addressed to the Son,
  BSB and NRSV "O God"; but Castellio chose *dīvus*, 1573 prints *diue*, and no settled verse uses *dīvus* for God);
  **Heb 9:14 *per æternum Spīritum*** (BSB, NRSV, KJV capital; perhaps Christ's own spirit; 1573 lower case); **Jas 4:5
  *Spīritus*** (1573 and the KJV lower case). Lower case: Jas 4:12 *lēgislātor (atque jūdex)* (1573 *Iudex*), 5:9
  *jūdex*, 5:4 *Dominī armipotentis* (as Rom 9:29), Heb 1:3 *majestātis*, 7:1 *summī Deī*. Heb 10:28 *Mōsaicam* capital,
  as Acts 15:1.
- **Jas 5:3**, Castellio's *L. Pœnam G.*: the marks dropped, the word kept (as Matt 19:4, 2 Tim 3:4), and *cōnsūmet.* a
  full stop so that *Pœnam vōbīs congessistis* stands as its own sentence (1573: a comma, the capital inside the marks).
- **Punctuation from 1573's page**: Heb 1:9, 3:15, 6:4 (6:4–6 one sentence), 7:2 (7:1–3 one sentence), 7:15, 9:13
  *pūritātem:*; 13:25 *grātia. Āmēn.* Quotations ending on a colon in the draft end with a full stop (Heb 12:20, 13:5),
  as no settled verse closes a quotation on a colon.
- **Subscription**: Heb 13:25 *Missa ex Ītaliā per Tīmotheum.* as `\cls` (1573, in italics). James has none.
- **Words no source marks**, decided from the Latin: Heb *sēmetipsum*, *compāgumque*, *faustitāte* (Gaffiot
  *Faustĭtās*), *Cherubī*, *inumbrantēs*, *immolātōrem*, *ostentuī*, *exhortātōrium*, *obmoveant*, *prōculcāverit*;
  Jas 5:5 *lascīvīstis* (contracted, as *audīstis*). Left as proposed: *sabbatismus*.
- **Names**: new to the edition *Melchisedēchus* (as your Gen 14:18), *Solyma*, *Jephthā* (**uncertain**, stem
  unmarked), *Gedeōn*, *Barac*, *Samsōn* (1573 *Sampsone*: a name's spelling, left), *Italicī* (short I, Gaffiot
  *Ĭtalĭcus*, beside *Ītalia*), *Rāchaba* (as your Matt 1:5), *Jācōbus* as the author (as the Gospels). As settled:
  *Aharōn*, *Jōsua* (decision 46), *Abēl*, *Caīnus*, *Henōchus*, *Nōa*, *Ēsāus*, *Hierichūs*, *Ēliās* (the settled
  majority, 8 : 4 *Ēlīās*).

## Questions for you

- **Title lines** (to add when settled): Hebrews `\h`/`\toc2` *Ad Hebræōs*, `\toc1` *Epistola ad Hebræōs*, `\mt1`
  *Epistola // ad Hebræōs*: **without Paul's name, as 1573** (*EPISTOLA AD HEBRAEOS*), against the pattern of the
  thirteen letters. James `\h`/`\toc2` *Jācōbī*, `\toc1`/`\mt1` *Jācōbī Apostolī Epistola*, as 1573.
- **Book order**: 1573 puts Hebrews after Jude, as the last letter; the edition follows the KJV order (Hebrews after
  Philemon). Kept, unless you want Castellio's order.
- **Heb 7:5 *ducentes***: 1573 lacks it (with 1758 and 1726–27); kept from 1556 as a 1573 omission, since *qui à Levi
  genus sacerdotium ineunt* has no verb for *genus*. **Heb 11:4 *mortuus***: 1573 *mortuis*, kept out as a misprint.
- **Heb 12:29** (Deut 4:24): quote it or not (above).
- **Your settled text**: nothing found wrong in this run.
