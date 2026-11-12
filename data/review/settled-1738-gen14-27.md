# The settled Genesis 14–27 against 1738

Proposed 2026-11-12. Your settled Genesis 14–27 (`text/GEN.usfm`, the earlier manual work, never checked against its
base) collated word by word against 1738 Leipzig, the Old Testament base (decision 1), with 1750, your 1726–27 text
(`TXT/3 - Edited`) and Wikisource as witnesses (`python -m pipeline collate Gen 1-27 --base settled`;
`data/calibration/Gen1-27-collation.tsv`, chapters 14–27 only; Genesis 1–13 is reviewed separately). The model is
`settled-1573.md` (the settled Gospels against 1573) and `gen28-50-stage2.md` (how the OT witnesses are used).

**What was compared** (chapters 14–27): 54 places where 1738 and another witness agree against your text (`correct`),
6 where two or more others do (`others`), 980 where only 1738's OCR differs (`base-only`: 780 reading, 113 word
division, 56 verse edge, 31 spelling), and 71 verses its OCR covers under 60% (`uncovered`). Spelling (æ/ae, i/j, u/v,
*quum/cum*, *caussa*, ad- assimilation, capitals, punctuation) and the forms the approved rules decide are not findings.

**What was read**: every `correct` and `others` place; the `base-only` readings filtered for real words (those far from
your word after allowing for the OCR's usual confusions, those where 1750 says nothing, and every exchange of short
words such as *eum/cum*, *tum/cum*, *ea/a*), the rest being OCR noise; and the 71 uncovered verses whole, against
1738, 1750 and Wikisource word by word, with your 1726 text and its uncorrected OCR (`TXT/1`) where needed. Eleven
places were read on 1738's page image (archive.org `bibliasacraexseb01cast`, leaf given as in gen28-50-stage2.md;
crops `sources/archive/crops/settled1738-g*.jpg`).

**Result: 3 corrections** (section 1), all Wikisource slips your text inherited. Your 1726 text (`TXT/3`) has all three
too, so it is no independent witness for them; the 1726 *OCR* (`TXT/1`), 1750 and 1738 agree. Everything else checked is
listed in sections 2–3.

Each **Apply** line is an exact replacement inside that verse of `text/GEN.usfm`, checked to match once. Answer the
**Decision:** with *accept*, *accept all except N*, or *accept N, M*; then
`python -m pipeline review apply data/review/settled-1738-gen14-27.md --write`.

## 1. Words missing or wrong: 1738 and the other printings agree against your text (3)

**Decision:**

1. **Gen 17:12** *quam es tuō ortī* → *quam ex tuō ortī* (“of any other race than from yours”; *es* does not
   construe). **1738** (leaf 75, page image): *ex alio quocumque genere quam ex tuo orti* (OCR *ei*).
   Printings: 1738, 1750 *ex*; your text: Wikisource and your 1726 text *es*.
   **Apply:** `Gen.17.12` la: `quam es tuō` → `quam ex tuō`
2. **Gen 25:13** *Nabaiothua* → *Nabaiothus*. **1738** (leaf 84, page image): *Primigenius Nabaiothus, Cedar*.
   Printings: 1738, 1750 *Nabaiothus*, 1726 OCR *Nabaiochus*; your text: Wikisource and your 1726 text *Nabaiothua*.
   Your 28:9 has the genitive *Nabaiothī*, as from *Nabaiothus*.
   **Apply:** `Gen.25.13` la: `Nabaiothua` → `Nabaiothus`
3. **Gen 27:33** *bene precātus—sānē fortūnātus erit* → *bene precātus, et sānē fortūnātus erit* (“and he shall indeed
   be blessed”; KJV *yea, and he shall be blessed*). **1738** (leaf 87, page image): *eique ſum bene precatus, & ſane
   fortunatus erit*. Printings: 1738, 1750 *et*, 1726 OCR *&*; your text: Wikisource and your 1726 text (no *et*).
   With *et* the dash your text put in its place gives way to a comma.
   **Apply:** `Gen.27.33` la: `precātus—sānē` → `precātus, et sānē`

## 2. Kept and listed

1738 differs from your text, but the reading is kept; say if you want 1738's instead.

- **Gen 25:14 *Masma*.** 1738 (leaf 84, page image) *Maſi-|na*, “Masina”; 1750 *Mafi-|na* (OCR, the same line break);
  your 1726 OCR *Mafma*, Wikisource and your 1726 text *Masma*. 1738's own 1 Chr 1:30 has *Masma* (OCR), as has 1750's;
  Vulgate *Masma*, Hebrew *Mishma*. Likely a misprint in 1738 that 1750 copied. Kept.
- **Gen 26:2 *cōnsīditō*.** 1738 (leaf 85, page image) *con-|ſideto*, with 1750 and Wikisource *consideto*; your 1726
  text *considito*. No lexicon here knows *consideto* (`latin macron`: “no source knows this form”); *cōnsīditō* is the
  future imperative of *cōnsīdō* (Gaffiot *cōnsīdō*). Kept as your emendation.
- **Gen 26:2–3, the verse boundary.** Your text begins 26:3 with *In istā commorāre* (as your 1726 text and the KJV,
  “Sojourn in this land”). 1738 (leaf 85, page image) prints the numeral 3 in the margin of the line *ſideto, in iſta
  commorare. Ego*, so the line does not say whether verse 3 begins at *In istā* or at *Ego*; Wikisource puts *in ista
  commorare* in 26:2. Kept.
- **Gen 21:9 *G.* … *H.*.** 1738 (leaf 79, page image) *pepererat G. Iſaaco filio ſuo H. illudentem*, with 1750 (OCR):
  Castellio's marks for words from the Greek (the Septuagint has μετὰ Ἰσαὰκ τοῦ υἱοῦ αὐτῆς; the Hebrew has nothing).
  Your text keeps the words and drops the marks, as the settled chapters do (Gen 44:6, Matt 19:4). Kept.

## 3. Not proposed

- **Read on the page image and found to agree with your text** (the OCR or Wikisource had something else):
  24:35 *tum ovibus* (leaf 83; 1738 OCR and 1726 OCR *cum*), 24:51 *sīcutī Jōvæ* (leaf 83 *Iouæ*; 1738 OCR and
  Wikisource *Ioua;*/*Jova;*), 25:9 *Ephrōnis* (leaf 84; 1738 OCR and Wikisource *Ephroni*), 26:34 *Beeris* (leaf 86;
  OCR *Beerij*), 19:10 *Lōtō* (leaf 77; the OCR's *to* after it, in 1738 and 1750, is the verse numeral *10*).
- **Wikisource slips your text had already corrected** (1738 and 1750 with you): 15:15 *senectuta*, 20:13
  *abstraherer*, 22:2 *a ūnicum*, 22:12 *in cum*, 22:17 *suorums*, 26:2 *in ista commorare* (moved to 26:3, above);
  24:67 Wikisource lacks *et ejus amōre … lēnīvit*, which 1738 and 1750 print.
- **Forms and spellings the approved rules or earlier decisions settle**: 14:4 *servīssent*, 24:30 *audīsset*, 14:21 and
  27:14 *petīvit* (decision 19); 19:2 *dēvertant*, 19:3 *dēverterint* (1738, 1750, Wikisource *div-*; `orthography.tsv`:
  *dēvertō* fixed per verse); 17:6, 17:20, 19:34 *subolis/subolī*, 18:1 and 14:13 *querquētō*, 24:17, 24:43 *paulum*,
  27:16 *lēvōrem*, 27:36 *Nē* (*nae*), the ad- assimilations (*alloquor, afferō, aggredior, assurgō* …), *cotīdiē*.
- **The uncovered verses** (14:2 … 27:44, 71): read whole; apart from 17:12 (above) the differences are OCR breaks,
  1738's footnotes and the next column run into the line (24:64–66, 25:30), and the spellings above.
- The other 1738-only places in chapters 14–27 are OCR noise (*x* for *æ*, *f* for *ſ*, *rn* for *m*, *Turn* for
  *Tum*, verse numerals and note letters read as words).
