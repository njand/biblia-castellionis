# Galatians, Ephesians, Philippians, Colossians: stages 1–5, one proposal per verse

Proposed 2026-11-11; **approved by Nathan "for now" the same day and settled in `text/GAL|EPH|PHP|COL.usfm`** (decision 43). Same tools and format as 2 Corinthians
(`data/review/2cor1-13-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier
work on these books; `TXT/1 - OCR` (the 1726–27 printing, uncorrected) served as a witness, read as an OCR.

## Where it stands

| Book | Verses | Words | Stage 2 corrections | Layout lines | Forms decided | Items `ok` |
|---|---:|---:|---:|---:|---:|---:|
| Galatians 1–6 | 149 | 2,126 | 58 | 30 | 97 | 148 + 1 unchanged (6:5) |
| Ephesians 1–6 | 155 | 2,129 | 45 | 38 | 140 | 155 |
| Philippians 1–4 | 104 | 1,543 | 29 | 25 | 109 | 104 |
| Colossians 1–4 | 95 | 1,409 | 32 | 22 | 102 | 95 |
| **All** | **503** | **7,207** | **164** | **115** | **448** | **503** |

- **Stage 1**: `text/draft/GAL|EPH|PHP|COL.usfm`, Wikisource with the BSB's paragraphs, every chapter at the KJV count
  after two versification edits: **Gal 5:22–23** (1573 canvas 892 and Wikisource print them as one verse; split at
  *lenitas*, where the KJV's 5:23 *Meekness, temperance* begins; `data/versification/Gal.draft.edits.tsv`) and
  **Col 3:26 → 4:1** (both print *Domini, ex justo aequoque cum servis agite* as the last verse of chapter 3, canvas
  903; `Col.draft.edits.tsv`). Ephesians and Philippians needed none; Eph 5:18–19's boundary (*sed spiritu pleni este*
  in 18, as 1573, 1715 and the KJV) was moved by stage-2 Apply lines.
- **Stage 2**: `data/review/gal1-6-stage2.md`, `eph1-6-`, `phil1-4-`, `col1-4-stage2.md`, every correction **read on the
  1573 page image** (crops in `sources/mdz-1573/crops/{Gal,Eph,Phil,Col}.*`, 232). Applied to the drafts (decision
  30's standing rule). Wikisource's four books are the early wording, as its Romans and Corinthians: *favor → gratia*
  (every greeting and blessing), *fiducia → fides* (Gal 2:16–3:25, 10×), *res/natura → creatura* (Gal 6:15, Col 1:23),
  *corpus → caro* (Eph 6:5, Col 3:22), *fortunavit → felicitavit* (Eph 1:3), *torporem → duritiem* (Eph 4:18), *ambire
  → aemulari* (Gal 4:17–18), *dedit → dedidit* (Gal 1:4, Eph 5:2, 5:25). Wikisource slips include whole clauses lost:
  Gal 2:16 *ut justi fieremus Christi fide*, Eph 2:2 *ut est hujus mundi vita*, Col 1:16 *tum inadspectabilia*, Col 3:16
  *Deique laudationibus*, Phil 3:12 *aut jam perfectus*. f/s sweeps both ways: Gal 4:29 and 5:11 *fit*, Eph 1:11
  *sortem*, Eph 4:16 *fit*. Word division: *sē ipsum* divided where Wikisource joins it (Gal 1:4, 6:4; Eph 4:19, 5:2,
  5:28, 5:33; Phil 2:7), as your settled 18 : 4; Gal 5:14 *teipsum* kept as your Rom 13:9 (the same quotation).
- **Stages 3–5**: `data/review/<book>-chNN.md`, 503 items, all checking `ok`. Previews **`text/draft/*.preview.usfm`**.
  Quotation marks balance in every verse and across verses (`structure.quotes`: nothing open or unclosed; no ‘…’ in
  any of the four). Each subscription stands apart as `\cls` after the last verse (decision 37). Ledger: all 20
  chapters **settled**.

## What changed in the tools

- **`align`**: an OCR's superscript digit (², ½) before a verse was taken for a verse number and stopped the Colossians
  collation (`int('²')`); only ASCII digits count now. Test added.
- **`collate`**: a clause Wikisource lacks was dropped as noise when every OCR spells it differently (Eph 2:2: 1573
  *műdi*, 1556 and 1750 *mundi*, 1758 *mundsamt*, so no two readings were alike). Readings of three words or more that
  differ only by OCR noise now count as one (`Place.against`). Rerun on the four books, it surfaces nothing stage 2 had
  not already corrected (Gal 3:10 *libro*, Eph 2:2, Phil 2:22 *inservivit*, Col 1:16), plus a few word-splits easily
  dismissed. Test added. Tests: 113 pass.
- **Not yet in code, worth adding to `draft`**: lay the BSB's paragraphs after the versification edits, not before. In
  Colossians 4 the draft's breaks fell a verse late (4:8 and 4:16 for the BSB's 4:7 and 4:15) after 3:26 became 4:1;
  the reader moved them by layout lines. Galatians' split falls where no break is affected.
- **Spelling rules added** (21 word rows, `orthography.tsv`): the *ad-* forms the stage-2 files listed (*affectum,
  affixum, affulgebit, aggrediantur, aggressiones, ascendens, assecutum, assedit, asserendam, asseruit, assiduis,
  aspectabilia, inaspectabilia, aspicientes, assumpto*) and *affectione* under decision 37 (compounds of *sum* kept:
  *adsit*, *adsint*, *adsitis*); *intellegentiam*, *intellegite*; *exstructi*; *peremptis*; *temptemini* (Gal 6:1).
  Decision 42's stem rules, approved during the run, also reached these drafts (*obœdīte*, *condiciōne*, *quotiēns*).

## How the verses were made

- **Layout and macrons**: four readers, one per book, under one brief adapted from 2 Corinthians, each with the Greek
  (TR, SBLGNT), the BSB and the KJV beside the verse. Their calls are in `data/decisions/{Gal,Eph,Phil,Col}.layout.tsv`
  and `.forms.tsv`, each with its reason. Each swept the homograph+settled tier for -a/-ā and the other endings; I then
  swept the four previews together: every form your settled books never write for a word they write at least 3 times
  (all right in their verses: *līber* "free" against your 1 Cor *liber*, see the fixes file; *dignā*, *sitā*, *vērā*,
  *vānā* ablatives), every *-a* after an ablative preposition (two, both right: Eph 1:9 *cum perācta forent*, the
  conjunction; Phil 4:20 *in perpetua sæcula*), and every word marked two ways across the four books (all case or
  homograph differences, none a stem).
- **Paragraphs**: of the BSB's ordinary breaks the drafts lacked, Galatians took 10 of 44 (23%), Ephesians 10 of 40
  (25%), Philippians 6 of 25 (24%), Colossians 7 of 26 (27%), each with its reason. Eph 5:21's break moved to 5:22
  (*Alius aliī obœdientēs* ends the sentence begun at 5:18), as decision 28 moved breaks off mid-sentence in Mark.

## Calls worth a look

- **Scripture** in `\qt` with “…”:
  - *Poetry* where the BSB sets it: Gal 4:27 (Isa 54:1, after *Scrīptum est enim:*); Eph 4:8 (Ps 68:18, *(inquit ille)*
    inside, as Rom 14:11); Eph 5:14 (*Expergīscere …*, *(inquit)* inside; the source uncertain, Isa 60:1 or a hymn).
  - *Prose*: Gal 3:16 *“et sēminī tuō,”* (with *“et sēminibus,”* in marks only, words named, decision 39); 4:30 (Gen
    21:10); 5:14 (Lev 19:18, as Rom 13:9); Eph 5:31 (Gen 2:24, no formula, as 2 Cor 13:1); Eph 6:2–3 (the commandment,
    Paul's *quod prīmum est cum prōmissiōne præceptum* outside, reopened at 6:3 *ut*).
  - **Without a formula, built into the sentence** (as Rom 9:7, 10:18): Gal 3:6 (Gen 15:6, your Rom 4:3 words; the
    least certain), 3:11 (Hab 2:4), 3:12 (Lev 18:5; your Rom 10:5 leaves the same verse unmarked).
  - *Left unmarked*: reported quotations (Gal 3:8, 3:10, 3:13, 4:22 *Scrīptum est enim, Abrāhāmum duōs habuisse
    fīliōs*); Eph 4:26 (Ps 4:4, recast as *Ita īrāsciminī, ut nē peccētis*; the BSB quotes it); Eph 4:25, 1:22, 2:17;
    Phil 2:10 (Isa 45:23, an allusion, though Rom 14:11 quotes it) and 2:15.
- **Poetry, Paul's own**: **Phil 2:6–11, the Christ hymn, as verse** (as the BSB), no `\qt`, as your Rom 11:33–36; 2:7
  ends *ut homō,* with 1573's comma. Prose is the alternative.
- **Direct speech** in “…”: Gal 2:14 Paul to Peter (*“Sī tū Jūdæus … cōgis?”*, 1573's question mark), closing at 2:14
  as the BSB (the NRSV runs it to 2:21); Gal 4:6 *“Abba, Pater.”* (as Rom 8:15); Col 2:21 the teachers' precepts *“Nē
  tetigerīs, nēve gustāverīs, nēve attrectāverīs”* (no `\qt`). Unmarked: Gal 1:23 (accusative and infinitive), Col
  4:17 (reported).
- **Capitals for God** (decision 20): *Pater* in every greeting and blessing; Col 1:19 *Patrī* (Castellio supplies the
  Father as subject); *Fīlius* Gal 1:16, 2:20, 4:4, 4:6, Eph 4:13, Col 1:13–14; *Servātor* Eph 5:23 (a predicate) and
  Phil 3:20; *Spīritus* for the Spirit received (Gal 3:2–5, Eph 5:18 changed from the draft). **Uncertain**: Phil 3:3
  *Spīritū Deum colimus* (capital, NRSV, BSB and your Rom 2:29; the KJV and your John 4:23–24 lower case); Eph 1:17
  *auctōre Spīritū* (NRSV "a spirit of wisdom"). Lower case: Phil 3:19 *prō deō habent* (the belly, as 2 Cor 4:4; 1573
  prints *Deo*), Eph 2:22 *dīvīnō afflātū* (as 1573 and your three settled places), the human spirit (Eph 4:23, Phil
  1:27), *chrīstiān-* as adjectives (Gal 1:22, Eph 4:13, Phil 1:13, 3:18).
- **Punctuation from 1573's page**: Gal 4:4 *fuit,* and 4:6 *estis,*; Phil 3:8 *lucrer,* and 3:9 *sitam,* (without
  them 3:9 *et mihi … suppetat* hangs without its *ut*); Col 3:5 *cultus est,*, 4:9 *est. Iī*, 4:16 *Lāodicēnsem*
  capital; *frātrēs. Āmēn.* at Gal 6:18. Against 1573: **Phil 3:11 *perveniam.*** a full stop for its comma, closing
  3:8–11 so that the paragraph at 3:12 opens with *Nōn*.
- **Words no source marks**, decided from the Latin: *clāmōsitās* (Eph 4:31), *mundipotentēs* (Eph 6:12, on
  *omnipotēns*), *obversātiō* (Phil 3:20, on *conversātiō*), *sancītum* (Gal 3:15, the participle of *sanciō*;
  uncertain), *cōmessātiōnēs* (as your Rom 13:13), *Lāodicēnsēs*, *Hierāpolītānī*, *Epaphrās*, *Syntychēn*. **Least
  sourced**: Col 4:14 *Dēmās*.
- **Names new to the edition**: *Agar* (Gal 4:24–25, unmarked; your Genesis *Hagar*), *Arabia*, *Epaphrodītus*,
  *Clēmēns*, *Philippēnsēs*, *Evodia* (unmarked), *Syntychē*, *Epaphrās*, *Archippus*, *Onēsimus*, *Nympha*, *Dēmās*,
  *Scytha*, *Colossæ*. As settled: *Tīmotheus*, *Tychicus*, *Barnābās*, *Cēphās*, *Mārcus*, *Lūcās*, *Abrāhāmus*.
- **Other uncertain calls**: Gal 3:28 *idem estis* (neuter as proposed; masculine *īdem* possible); Eph 2:2 *spīritūs*
  genitive; Col 1:6 *pervēnit* (the Greek is present); Phil 1:3 *venit* (present).
- **From stage 2, for your eye**: Col 2:5 *at animo quidem* kept with 1556 (1573 *ac*, which makes no sense after
  *quamvis*); Phil 3:17 *fratres* dropped with 1573, 1556 and 1758 (the Greek has ἀδελφοί); Gal 3:19 *sequestrum*
  (1573) for 1556's *sequestrem*; Gal 5:2 *circumcidemini* (1573's future); Eph 4:16 *fit* (by the image alone), 6:12
  *mundipotentes* (one word, 1573 and 1726), 4:7 *pro portione* (two words); Phil 1:18 *quoquomodo* (one word).
- **Title lines** (added when settled, on the pattern of Romans): `\h`/`\toc2` *Ad Galatās*, *Ad Ephesiōs*, *Ad
  Philippēnsēs*, *Ad Colossēnsēs*; `\toc1`/`\mt1` *Paulī Apostolī Epistola ad …*, as 1573 heads them (*PAVLI
  APOSTOLI EPISTOLA AD …*, canvases 889, 894, 898, 901; *Philippēnsēs* and *Colossēnsēs* as the lexicon marks them).
- **Your settled text**: ten markings found wrong, proposed in `data/review/settled-fixes-galcol.md` (not applied).

## Questions for the whole edition

- ***Abrahām-* / *Isaāc-*** in your Gospels against *Abrāhām-* / *Isaac-* elsewhere; ***Hagar*** against ***Agar***
  (both in the fixes file).
- ***Euodia*** (Phil 4:2): the draft's *Evodiam* comes from the j/v rule (1573 *Euodiam*, Gaffiot *Ĕuŏdĭa*, u a vowel):
  a rule *Evodiam → Euodiam*?
- **A word named that is also Scripture** (Eph 4:9 *“ascendit,”*): quotation marks only, as here, or `\qt` too?
- **`draft` after versification** (above): lay the BSB's paragraphs on the KJV numbering?
