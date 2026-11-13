# The settled Genesis 1–13 against 1738

Proposed 2026-11-12 (decision 50, option F). Your settled Genesis 1–13 (your earlier work, never checked against its
base) collated word by word against 1738, the Old Testament base (decision 1), with 1750, the 1726–27 printing
(`TXT/1`, OCR), your corrected 1726–27 text (`TXT/3`), Wikisource and your 2019 WordPress text as the other witnesses
(`python -m pipeline collate Gen 1-27 --base settled`; `data/calibration/Gen1-27-collation.tsv`, chapters 1–13 here;
Genesis 14–27 has its own file). The model is `settled-1573.md` (decision 27).

- **The collation** (chapters 1–13): 660 places. 40 *correct* (1738 and another witness against your text), 7
  *others* (1750 or Wikisource against your text where 1738's OCR did not reach), 578 *base-only* (only 1738's OCR
  differs: 441 readings, 87 word divisions, 33 line edges, 17 spellings) and 35 *uncovered* verses (1738's OCR covers
  under 60% of the words). Almost all of it is OCR noise or spelling (æ/ae, i/j, u/v, *quum*, *ad-* assimilation,
  *sexcent-*, *quercetum*), which the approved rules decide and which is not listed.
- **Page images**: 1738's archive.org scan, cropped as for Genesis 28–50 (`pipeline/archive.py`; crops in
  `sources/archive/crops/`, `1738-gen*.jpg`; canvas = the hOCR page, as `1738-page-NNNN.jpg`). Every page of
  Genesis 1–13 (canvases 61–72) was **read whole against your text**, which covers the 35 uncovered verses and the
  places where 1738's OCR is too garbled for the collation to see. Three of the slips below (5:22, 9:15, 13:15) were
  found that way, not by the collation.
- **Results**: 8 readings where 1738 and the other printings agree against your text (sections 1–2), 5 small slips
  noticed while reading (section 3), and a list of what is kept (section 4). Where 1738's OCR alone differed, the page
  image always agreed with your text (8:11 *eum*, 7:7 *ēvītandæ*, 8:21 *dēlectātus*, 9:3 *concēdō*). As in the
  Gospels, most slips are Wikisource's, which your text inherited.

Each **Apply** line is an exact replacement inside that verse of `text/GEN.usfm`, checked to match once. Answer each
group's **Decision:** with *accept*, *accept all except N, M*, or *accept N, M*; then
`python -m pipeline review apply data/review/settled-1738-gen1-13.md --write`.

## 1. Words wrong: 1738 and the other printings agree against your text (4)

Slips in Wikisource that your text inherited: a case or person that does not construe.

**Decision:** accept (Nathan, 2026-11-12)

1. **Gen 4:8** *At Caīnum Abēlem* → *At Caīnus Abēlem*. **1738** (canvas 64, page image): *At Cainus Abelem fratrem
   ſuum ſuis verbis, (G. lect.) rus ſeduxit, (H.) ibique eum adgresſus interfecit*: Cain is the subject of
   *sēdūxit*, *interfēcit* (in 4:9 he is the object, *Tum sīc Caīnum Jōva allocūtus est*).
   Printings: 1738, 1750 *At Cainus*, 1726 *Ac Cainus*; your *Caīnum*: Wikisource, your TXT/3, WordPress.
   **Apply:** `Gen.4.8` la: `At Caīnum Abēlem` → `At Caīnus Abēlem`
2. **Gen 5:22** *post eum gentium per* → *post eum genitum per*. **1738** (canvas 65, page image): *et poſt eum
   genitum per trecentos annos*: “after he was born”, as 5:4 *Post quem genitum*, 5:13.
   Printings: 1738, 1750 *genitum*, 1726 *genicum* (OCR); your *gentium*: Wikisource, your TXT/3, WordPress.
   **Apply:** `Gen.5.22` la: `eum gentium per` → `eum genitum per`
3. **Gen 9:15** *animantium genus facta.* → *animantium genus factī.*. **1738** (canvas 69, page image): *in
   memoriam redibo fœderis inter me et vos, omneque animantium genus facti*: with *fœderis*, “the covenant made
   between me and you and every kind of living thing” (as 9:16 *fœdus … factum inter Deum et omnia*); *facta* agrees
   with nothing.
   Printings: 1738, 1750, 1726 *facti*; your *facta*: Wikisource, your TXT/3, WordPress.
   **Apply:** `Gen.9.15` la: `genus facta.` → `genus factī.`
4. **Gen 13:15** *quamcumque tuī terram* → *quamcumque tū terram*. **1738** (canvas 72, page image): *Nam quamcumque
   tu* with the verse number *15* in the margin after it; 1738's OCR reads *tui $*, which is Wikisource's *tui*.
   Printings: 1738, 1750, 1726 *tu*; your *tuī*: Wikisource, your TXT/3, WordPress.
   **Apply:** `Gen.13.15` la: `quamcumque tuī terram` → `quamcumque tū terram`

## 2. Different readings: 1738 and 1750 agree against your text (4)

Both readings construe; 1738 (the base) and 1750 read otherwise. At 6:21 the 1726 printing has your reading; at
11:25 the reading is your own TXT/3 correction (Wikisource and your WordPress text have the printings' word).

**Decision:** accept 5, 6 (Nathan, 2026-11-12; the other two keep your *ūndēvīgintī* and *discidium*)

5. **Gen 4:3** *dē terrā frūgibus* → *dē terræ frūgibus*. **1738** (canvas 64, page image): *libauisſet Cainus de
   terræ frugibus*: “of the fruits of the earth” (1738's OCR lost this column, so the collation could not see it).
   Printings: 1738, 1750 *terrae*, 1726 *terræ*; your *terrā*: Wikisource, your TXT/3, WordPress.
   **Apply:** `Gen.4.3` la: `dē terrā frūgibus` → `dē terræ frūgibus`
6. **Gen 6:21** *quæ sunt edendō* → *quæ sint edendō*. **1738** (canvas 66, page image): *cibaria, quæ ſint
   edendo*: the subjunctive, “such food as is fit for eating”.
   Printings: 1738, 1750 *fint* (= *sint*); your *sunt*: 1726 (*funt*, OCR), Wikisource, your TXT/3.
   **Apply:** `Gen.6.21` la: `quæ sunt edendō` → `quæ sint edendō`
7. **Gen 11:25** *centum ūndēvīgintī* → *centum novemdecim*. **1738** (canvas 71, page image): *vixitque poſtea annos
   centum nouemdecim*. The same number (119; Vulgate *centum decem et novem*); Gaffiot *nŏvemdĕcim* (no long vowel).
   Printings: 1738, 1750 *nouemdecim*, Wikisource and WordPress *novemdecim* (1726's OCR is garbled here); your
   *ūndēvīgintī*: your TXT/3 only (its 11:27).
   **Apply:** `Gen.11.25` la: `centum ūndēvīgintī,` → `centum novemdecim,`
8. **Gen 13:8** *esse discidium inter* → *esse dissidium inter*. **1738** (canvas 72, page image): *eſſe diſſidium
   inter me et te*. Gaffiot heads them apart: *dissĭdĭum* “dissension” (*dissideō*), *discĭdĭum* “separation”
   (*discindō*); the strife between the herdsmen is the first. Your settled text writes *dissidium* everywhere else
   (7×: John 7:43, 1 Corinthians, 1 Timothy).
   Printings: 1738, 1750 *diffidium* (= *dissidium*), 1726 *dillidium* (OCR, the long s read as l); your
   *discidium*: Wikisource, your TXT/3, WordPress.
   **Apply:** `Gen.13.8` la: `esse discidium inter` → `esse dissidium inter`

## 3. Noticed while reading the pages: macrons and capitals (5)

Not readings, but slips in the settled text seen on the way.

**Decision:** accept (Nathan, 2026-11-12)

9. **Gen 9:10** *ex arca ēgressīs* → *ex arcā ēgressīs*: the ablative after *ex*, as *dē arcā* (8:15) and *ex arcā*
   (9:18).
   **Apply:** `Gen.9.10` la: `ex arca ēgressīs` → `ex arcā ēgressīs`
10. **Gen 9:18** *Chamō et Japhēto* → *Chamō et Japhētō*: ablative, with *Semō, Chamō* (`latin macron`: *Iaphētō*,
    dative/ablative).
    **Apply:** `Gen.9.18` la: `Chamō et Japhēto` → `Chamō et Japhētō`
11. **Gen 10:2** *Japhēto:* → *Japhētō:*: dative (“to Japheth were born”), as 10:3 *Gomerī*, 10:4 *Javanī*.
    **Apply:** `Gen.10.2` la: `Japhēto:` → `Japhētō:`
12. **Gen 9:29** *Complētīsque* → *complētīsque*: the sentence runs on from 9:28 (*quīnquāgintā,*).
    **Apply:** `Gen.9.29` la: `Complētīsque nōngentīs` → `complētīsque nōngentīs`
13. **Gen 11:2** *Cum illī* → *cum illī*: the sentence runs on from 11:1 (*ūterētur,*; 1738 *vteretur, quum illi*).
    **Apply:** `Gen.11.2` la: `Cum illī ab oriente` → `cum illī ab oriente`

## 4. Kept and listed

No place was found where 1738 alone differs and 1750 and 1726 support your text: every such place in the OCR was a
misreading, as the page images show. Kept, where the printings agree against your text:

- **Gen 3:14 *cicurum*** (1738 *cicurarum*, canvas 63, page image; 1750, 1726, Wikisource, WordPress the same; your
  TXT/3 *cicurum*). *Cicur* is third declension (Gaffiot *cĭcŭr, ŭris*), genitive plural *cicurum*; no lexicon here
  knows *cicurarum*. Kept, as *abstergēmus* at Luke 10:11 (`settled-1573.md` §5). Say if you want the printings' form.
- **Gen 9:3 *adhibētōte*** (1738 *adhibitote*, canvas 68, page image; 1750, 1726 *adhibicote* (OCR) the same;
  Wikisource and your TXT/3 *adhibetote*). *Adhibeō* is second conjugation; no lexicon knows *adhibitote*. Kept.
- **Gen 1:26, 1:28, 2:19, 9:2 *āeriīs, āeriās*** (1738 *aereis, aereas*, canvases 62, 63, 68; 1750, 1726, Wikisource
  the same; your TXT/3 *aeriis*). The same word (Gaffiot gives *āĕreus* beside *āĕrius*); your text writes *āerius*
  throughout (Matt 6:26, Acts 10:12, Eph 2:2). Kept.
- **Castellio's marks** at **4:8** (1738 *(G. lect.) rus seduxit, (H.)*, canvas 64; 1750 *(Gr. lect.) … (Hebr.)*;
  1726 *G. L, … H,*) and **11:12–13** (*genuit G. Cainanem … genuit H. Salam*, canvas 70; 1750 and 1726 the same):
  the Greek's “let us go into the field” and Cainan. Your text keeps the words and drops the marks, as at Gen 44:6 and
  in the New Testament.
- **1738's lettered footnotes** (canvases 62–71: 2:11–13, 2:20, 4:5, 4:10, 7:14, 9:4, 9:26, 10:5, 12:5), short
  glosses and alternatives at the foot of the page (2:11–13 name the rivers *Ganges*, *Nilus*; 7:14 *et minorum et
  maiorum*; 12:5 *servitio et pecore*). Not text; Wikisource and your text omit them. 1738's OCR runs some of them
  into the verses (7:19, 10:19).
- **Chapter divisions**: 1738 begins chapter 3 at the KJV's 2:25 (*Ceterum quum essent*), chapter 7 at 6:22 (*Hæc
  omnia Dei mandata*) and chapter 8 at 7:24 (*Postquam autem viguerunt*); your text has the KJV's numbering
  (decision 5).
- **Names**: your *Mahujæl*, *Mathusæl* (4:18) write a diphthong where 1750 prints a diaeresis (*Mahuiaël*,
  *Mathufaël*; Hebrew Mehujael, Methusael, the a and e apart), as your *Nōēma* (4:22) and Acts 2:16 *Jōēle* do.
  10:31 has *Sēmō* where the rest of your Genesis writes *Semus, Semō, Semī*. Spellings, for your eye; no Apply line.
- **Forms decided by rules**: 7:10 *præterīssent* (1738 *præteriisſent*; decision 26), 1:14 *existerent* (1738
  *exſisterent*), 6:17 *extinguantur*, 13:18 *querquētum*, *sescent-*, *vīcēsimō*, *subole*: spellings, not readings.
