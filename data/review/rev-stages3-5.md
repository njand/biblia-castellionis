# Revelation: stages 1–5, one proposal per verse

Proposed 2026-11-12; **approved by Nathan "for now" the same day and settled in `text/REV.usfm`** (decision 49),
the title line and the calls below as proposed. Same tools and format as 1 Peter–Jude
(`data/review/petjud-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier work
on Revelation; `TXT/1 - OCR` (the 1726–27 printing, uncorrected) served as a witness, read as an OCR. With this book
the New Testament is complete.

## Where it stands

| Chapters | Verses | Stage 2 corrections | Layout lines | Forms decided | Items `ok` |
|---|---:|---:|---:|---:|---:|
| 1–11 | 194 | 36 (40 Apply lines), and 3:1 inserted | 74 | 116 | 194 |
| 12–22 | 210 | 38 (41 Apply lines) | 112 | 106 | 210 |
| **All** | **404** (7,846 words) | **74**, and 3:1 | **186** | **222** | **404** |

- **Stage 1**: `text/draft/REV.usfm`, Wikisource with the BSB's paragraphs. Two repairs before renumbering:
  - **Rev 3:1 was missing from Wikisource** (its chapter 3 began at verse 2). It was inserted from 1573 (canvas 939,
    crops `Rev.3.1-Sardensis`, `Rev.3.1-viventis`, read by me): *Item angelo Sardensis ecclesiae scribito: Haec dicit
    qui septem Dei spiritus, et septem stellas habet: Novi tua facta, qui quum viventis nomen habeas, mortuus es.*
    1556, 1758, 1681, 1747 and 1715 have the same words.
  - **Chapter 10 had a verse too few**: 1573 (canvas 942) and Wikisource put the KJV's 10:2 inside their 10:1. It is
    split off at *Habebat autem* (`data/versification/Rev.draft.edits.tsv`), so 1573's 2–10 are the KJV's 3–11.
- **Stage 2**: `data/review/rev1-11-stage2.md` and `rev12-22-stage2.md`; every correction **read on the 1573 page
  image** (crops in `sources/mdz-1573/crops/Rev.*`, about 130). The doubtful ones were looked at again by me: 7:5,
  8:10–11, 11:19, 12:14, 19:15 and 21:9. Applied to the draft under decision 30's standing rule (81 Apply lines). In
  1573, Revelation follows Hebrews on canvases 937–948.
  - **Wikisource is the early wording again**, with 1715, 1747 and 1750. Examples: 1:4 *favorem → gratiam*; 1:13 and
    14:14 *homine nati → hominis filio / filio hominis*; 3:15 *quod → qui*; 16:1 *Dei saevitiae → saevitiae Dei*;
    16:5 *augustus → sanctus*; 19:8 *mandatum est, ut … induatur → datum est … vestiri*; 20:4 *animos … Ii → animas
    … eae*; 20:6 *quia → quin*; 21:8 and 22:15 *divicolas → deastricolas*; 21:25 *ibi → illic*; 22:7 *pareat → paret*;
    22:11 *nocere pergat … → nocentior fiat … sanctior fiat*.
  - **Wikisource's slips and losses**:
    - 7:5 lost the tribe of Gad (*Ex Gaddi duodecim millia*).
    - 5:11 lost *et decies centena millia*.
    - 21:21 lost *unionibus singulae*.
    - 5:5 *referet → reseret* (f/s).
    - 14:4 *seminis → feminis* (f/s).
    - 16:10 *morderent → manderent*.
    - Others: *comissum*, *captibus*, *corrurerunt*, *oranta*, and more.
  - **8:10–11**: 1573 reads *qua … delapsa: (est autem stellae nomen Absinthium) conversa est*, an ablative absolute.
    1556, 1758, 1681 and 1726 agree. Wikisource has *quae … delapsa est … et conversa*.
  - **Verse boundaries**: in 10:2–3, 10:5–6, 19:6–7 and 21:10–11 the words are moved to where 1573 and the KJV agree.
    In 17:9–10, 20:9–10, 21:20–21 and 22:3–4, 1573 numbers against the KJV, and the KJV's numbers are kept
    (decision 5).
  - **1573's changes against 1556** are recorded in section 5 of each file and in `docs/editions.md`. There are ten:
    2:7, 2:10, 2:13, 5:10 (?), 11:19, 16:5, 19:8, 20:4, 21:9 and 21:24.
- **Stages 3–5**: `data/review/rev1-22-ch01.md` … `ch22.md`; 404 items, all checking. Preview
  **`text/draft/REV.preview.usfm`**. Ledger: all 22 chapters **settled**.
  - Quotation marks: 101 “ and 3 ‘ (14:13, 18:7, 19:9), no `\qt`.
  - Poetry: 166 `\q1`/`\q2` lines, with prose resumed by `\m` 10 times.
  - 1:20 and 2:29 end inside a quotation on purpose: Christ's speech runs from 1:17 to 3:22. Each letter reopens “ at
    its paragraph, and 17:14–15 do the same.
- **Spelling rules added** (31 word rows in `orthography.tsv`, under decisions 17, 37, 42 and 46):
  - *ad-* assimilated: *astabunt*, *aspexissemque*, *ascende*, *aspiciens*, *allocuta*, *affirmat*, *afficite*,
    *afficiar*, *ascensura*, and others.
  - Gaffiot's spellings: *belua*, *beluae*, *beluam*, *sardonyx*, *chalcedon*.
  - u/v: *alvo*, *uvas*.
  - Names and other words: *Gadi* (your *Gadus*), *Johanni*, *temptentur*.

## How the verses were made

Two readers took stage 2 and then stages 3–5, one for chapters 1–11 and one for 12–22. Each verse was read beside the
Greek (TR, SBLGNT), the BSB, the KJV, the Vulgate and 1573's page. Their calls, each with its reason, are in
`data/decisions/Rev.layout.tsv` and `Rev.forms.tsv`. I then read the whole preview. One thing changed after that
reading: 16:18 *sonitūs* is a plural subject beside *tonitrua … fulgura*, as in 11:19.

## Calls worth a look

- **Christ's speech, 1:17–3:22**, is one quotation, as in the BSB. The dictated letters (*Hæc dīcit …*) are not
  quoted separately, and the *Quī habet aurem* refrains stay inside it.
- **Hymns as poetry where the BSB sets them as verse**: 4:8, 4:11, 5:9–10, 5:12–13, 7:10, 7:15–17, 11:15, 11:17–18,
  12:10–12, 15:3–4, 16:5–7, 18:2–8, 18:10, 18:14, 18:16, 18:19–20, 18:21–24, 19:1–8 and 21:3–4.
  - Kept as prose: the tribe list 7:5–8, and the allusions, left unmarked (1:7, 2:27, 7:16–17, 13:10, 14:8, 18:2,
    21:4).
  - **Uncertain**:
    - 18:14 is quoted although no verb of speaking introduces it.
    - 18:20 is poetry without quotation marks, as in the BSB.
    - Christ's interjections at 16:15 and 22:7 are quoted with no speaker named.
    - The voice's speech closes at 18:8, although 1573's colon runs on.
- **Capitals for God** (decision 20):
  - Capital: *Agnus* throughout when it means Christ (lower in 13:11 *agnī similia*, a comparison). *Pater* and *Deī
    Fīlius*. *Spīritus* in every *quid Spīritus dīcat ecclēsiīs* and at 14:13 and 22:17. *Āmēn* at 3:14 as a name.
    *Hominis Fīliō* at 1:13 and 14:14, as your *Fīlius Hominis* (**uncertain**: the phrase is Daniel's; 1573 has lower
    case). *Sermō Deī* at 19:13, as your John 1:1. *Fidēlis et Vērus* at 19:11 (**uncertain**). *dominōrum Dominus, et
    rēgum Rēx* at 17:14 and 19:16.
  - Lower case: *diabolus* and *Satanās* as written; *orcus*, except *Orcus* at 6:8, personified beside *Mors*. *leō …
    Dāvīdica stirps* at 5:5 is **uncertain**.
  - **Against your settled text**: John 1:29 and 1:36 have *agnus Deī* in lower case.
- ***α et ω*** (1:8, 1:11, 21:6, 22:13) is kept in Greek letters, as 1573 prints it, with *prīncipium et fīnis* in
  lower case.
- **Inscriptions** in “…”: 17:5 (with *Mystērium* inside the name, **uncertain**) and 19:16.
- **Punctuation from 1573's page**: 2:26 *potestātem,*; 13:3 *bēstia,*; 15:2 *citharās,*; 16:15 *fūr.*; 17:4
  *margarītīs,*; 22:5 (no comma after *lucerna*); a full stop for the draft's colon at 18:8 and 22:20.
- **Macrons decided from the sentence**:
  - About 40 ablatives in *-ā*.
  - Imperatives *præstā*, *cōnfirmā*, *servā*.
  - Perfect subjunctives in *-erīs*.
  - *Hīc* for "then".
  - *spīritūs* in the plural.
  - Perfects *vēnit*.
  - 9:20 *ærea*.
  - **Uncertain**: *clānxit*, *clānxisset* and *clānxerit*, and *pūnxit* (by analogy with *plānxī*); 1:19 *vīderis*.
- **Names new to the edition**:
  - *Ephesīnæ*, *Smyrnæōrum*, *Pergamēnsis*, *Thyatīrēnsis*, *Sardēnsis*, *Philadelphiēnsis* (**uncertain**),
    *Lāodicēnsis*.
  - *Nīcolāītārum*, *Antipās*, *Abbadōn*, *Apollyōn*, *Armageddōn*.
  - *Gōgum* and *Magōgum* (**uncertain**), *Michāēl*, *chalcolibanō*.
  - *Aseris* (stem unmarked, as your *Aserem*, *Aseriānā*) and *Gadī* (your *Gadus*).
  - Left unmarked until the Old Testament is settled: *Balacum* and *Jezabelem*, and *Issacharis*, since your text has
    both *Issāchar* and *Issachārem*. The gems of 21:19–20 follow the lexicon, since Exodus 28 is not settled.

## Questions for you

- **Title lines**, to add when settled. 1573 heads the book *APOCALYPSIS IOHANNIS THEOLOGI, HOC EST, PATEFACTIO*. The
  proposal:
  - `\mt1` *Apocalypsis Jōhannis Theologī // hoc est, Patefactiō*.
  - `\h` and `\toc2` *Apocalypsis*.
- ***Agnus*** capital in Revelation, against your *agnus Deī* in John 1:29 and 1:36. Should John be made to match?
- ***α et ω*** in Greek letters, or *Alpha et Ōmega*?
- **Rev 3:1** entered from 1573 because Wikisource lacks it. Is the Wikisource credit enough, or should the README
  name 1573 as the source of this verse?
- **Your settled text**: nothing found wrong in this run.
