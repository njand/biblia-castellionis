# 1 Corinthians 1–16, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-10 (decision 30's standing rule), on the route of Romans (`data/review/rom1-16-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 867–880). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's 1 Corinthians as
  **`text/draft/1CO.usfm`** (BSB paragraphs). You have no earlier work on 1 Corinthians; `TXT/1 - OCR` (the
  1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's 1 Corinthians is mostly the early wording**, as its Romans and Acts, with many slips of its own:
  *in re christiana* for *in Christo* (3:1, 4:10), *corporis* for *carnis* (5:5), *humanitas* for *caro* (10:18),
  *sacrum* for *sanctum* (3:17), *cinaedi* for *paedicones* (6:10), *nomen* for *locum* (14:16). 1556, where its OCR
  can be read, already has some of these revisions (4:10 *in Christo*, 10:18 *carnem*, 6:10 *pedicones*, 14:16
  *locum*) but not others (3:1 *in re Christiana*, 3:17 *sacrum*, 5:5 *corporis*, 7:5 *& deinde*): those date from 1573.
- **Chapter 3 is not short of a verse.** Wikisource has 22 verses in chapter 3, and so does 1573: both print the KJV's
  3:23 (*vos autem Christi, et Christus Dei*) inside their 3:22, and no words are missing. The KJV's 3:23 is made by a
  versification split (below), not supplied from 1573.
- **Versification** (decision 5): 7 edits in `data/versification/1Cor.draft.edits.tsv`, applied (437 verses, every
  chapter at the KJV count). 1573 prints every verse number and agrees with Wikisource everywhere but 3:21–22 and 13:5;
  where both differ from the KJV the text follows the KJV:
  - **3:21–23**: 1573 prints 22 before *& Paulus, & Apollos*, with *omnia enim vestra sunt* closing 21 (the KJV's
    3:21–22); Wikisource starts 22 at *Omnia enim*. Neither has a 23: the KJV's 3:23 *vos autem Christi* is split off.
  - **4:10–12**: 1573 and Wikisource number the old way: *Ad hoc tempus et esurimus … agitamur* (the KJV's 4:11) sits
    in 4:10, and 4:11 *Et laboramus* + 4:12 *Conviciis appetiti* make the KJV's 4:12.
  - **10:33 / 11:1**: 1573 and Wikisource end chapter 10 with *Imitatores mei estote, quemadmodum ego quoque sum
    Christi* (the KJV's 11:1) and number chapter 11 one behind the KJV to its end, where they print the KJV's 11:34 as
    two verses (33 *Quod si quis esurit*, 34 *Reliqua cum venero componam*). The chapter break moves back before
    *Imitatores* (`opens` with an anchor, added to `pipeline/versify.py` with a test), and 11:33–34 are joined.
  - **13:4–5**: 1573 prints 5 before *charitas non aemulatur* (the KJV's 13:4b); Wikisource follows the KJV, kept.
- **Collation** (`python -m pipeline collate 1Cor 1-16`; `data/calibration/1Cor1-16-collation.tsv`, after the
  renumbering), with Romans' edge and f/s checks. Read on the page image: the 74 readings where 1573 and another
  printing agree against Wikisource and the 16 where two others do; every place where only 1573's OCR differs and its
  words are Latin; the f/s places (all but one are 1573's OCR reading ſ as f: *fi*, *fit* for *sit*, *fumus*; the one
  is 15:38 *feminum* for *seminum*); and the edge places (margin notes and note letters run into the text: 1:25 *e*,
  4:3 *a*, 9:5 *a* are note letters; 2:2 *nihil aliud scire* and 4:12 *infestati* are margin glosses). The crops are in
  `sources/mdz-1573/crops/` (`1Cor.*`). Also swept: the words no lexicon knows (15:42–44 *refurget(ur)*, Wikisource's
  f for long s, which 1573's OCR shares; 14:7 *emmitentia*; the rest are Castellio's words, *infidens*, *portentificus*,
  *viviscit*, or names) and the u-for-v slips the j/v rule leaves alone (none: every *u* left before a vowel is a
  vowel, as *mortuus*, *spiritualis*, *janua*).
- **In all, 97 corrections**: 58 Wikisource slips (section 1), 29 readings of Castellio's revised text (section 2),
  3 long-s slips found on a second pass (section 2a), 7 word divisions (section 3). **Applied to the draft** (decision 30's standing rule). Spellings (*caussa/causa*,
  *adloquor/alloquor*, *adsequor*, *quum*, *charitas*, *exsto/exto*, *-unque*) are left to stage 3, as in Romans; five
  *-mt-* forms that Wikisource writes against Gaffiot, 1573 and your settled text get new spelling rules (section 6).

## 1. Wikisource slips: 1573 and the other printings agree against it (58)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; every item read on the 1573 page image unless marked OCR)

1. **1 Corinthians 1:16** *Stephani familiam* → *Stephanae familiam*. 1573 *Stephanæ familiam* (canvas 867); 1758, 1747; Wikisource's own 16:15 and 16:17 have *Stephanae* (Stephanas, -ae).
   **Apply:** `1Cor.1.16` la: `Stephani familiam` → `Stephanae familiam`
2. **1 Corinthians 1:27** *Sed mundi stultitiam Deus* → *Sed mundi stultissima Deus*. 1573 *sed mundi stultissima Deus elegit* (canvas 867), as *infirmissima* after it and Castellio's own annotation (*Mundi stultissima elegit Deus*, canvas 868); 1556, 1758, 1726.
   **Apply:** `1Cor.1.27` la: `Sed mundi stultitiam Deus` → `Sed mundi stultissima Deus`
3. **1 Corinthians 1:28** *contentissimaque* → *contemptissimaque*. 1573 *contemptissimaq;* (canvas 868); 1556.
   **Apply:** `1Cor.1.28` la: `contentissimaque` → `contemptissimaque`
4. **1 Corinthians 2:6** *apud perdectos* → *apud perfectos*. 1573 *apud perfectos* (canvas 868); 1750.
   **Apply:** `1Cor.2.6` la: `apud perdectos` → `apud perfectos`
5. **1 Corinthians 3:11** *qui est Jesu Christus* → *qui est Jesus Christus*. 1573 *qui est Iesus Christus* (canvas 869); 1758, 1747, 1726.
   **Apply:** `1Cor.3.11` la: `qui est Jesu Christus` → `qui est Jesus Christus`
6. **1 Corinthians 3:17** *templum corrumpit,* → *templum corrumpet,*. 1573 *Si quis Dei templum corrumpet, corrumpet hunc Deus* (canvas 869); 1556 (OCR), 1758, 1726.
   **Apply:** `1Cor.3.17` la: `templum corrumpit,` → `templum corrumpet,`
7. **1 Corinthians 4:8** *sine nobis resignatis* → *sine nobis regnatis*. 1573 *sine nobis regnatis* (canvas 869); 1758, 1747, 1750.
   **Apply:** `1Cor.4.8` la: `sine nobis resignatis` → `sine nobis regnatis`
8. **1 Corinthians 4:9** *spectaculum sumus* → *spectaculum simus*. 1573 *spectaculum simus* (canvas 869; a relative clause of characteristic, *qui … simus*); 1556 (OCR), 1758.
   **Apply:** `1Cor.4.9` la: `spectaculum sumus` → `spectaculum simus`
9. **1 Corinthians 5:1** *uxorem quidem patris* → *uxorem quidam patris*. 1573 *vt vxorẽ quidã patris habeat* (canvas 870); 1758, 1715, 1747, 1750, 1726.
   **Apply:** `1Cor.5.1` la: `uxorem quidem patris` → `uxorem quidam patris`
10. **1 Corinthians 5:6** *vestra gloratio* → *vestra gloriatio*. 1573 *vestra gloriatio* (canvas 870); 1556 (OCR).
   **Apply:** `1Cor.5.6` la: `vestra gloratio` → `vestra gloriatio`
11. **1 Corinthians 5:8** *malititaeque* → *malitiaeque*. 1573 *malitiæq;* (canvas 870); 1747, 1750.
   **Apply:** `1Cor.5.8` la: `malititaeque` → `malitiaeque`
12. **1 Corinthians 5:11** *nominetur, impudicus, aut* → *nominetur, impudicus est, aut*. 1573 *impudicus est, aut auarus* (canvas 870); 1758, 1715, 1747.
   **Apply:** `1Cor.5.11` la: `nominetur, impudicus, aut` → `nominetur, impudicus est, aut`
13. **1 Corinthians 6:4** *despicati sunt* → *despicatui sunt*. 1573 *despicatui sunt* (canvas 870); 1556, 1758, 1715, 1750, 1726.
   **Apply:** `1Cor.6.4` la: `despicati sunt` → `despicatui sunt`
14. **1 Corinthians 7:9** *contrahunt matrimonium* → *contrahant matrimonium*. 1573 *contrahant matrimonium* (canvas 871); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `1Cor.7.9` la: `contrahunt matrimonium` → `contrahant matrimonium`
15. **1 Corinthians 7:25** *Domini elementia* → *Domini clementia*. 1573 *clementia* (canvas 871); 1556, 1715.
   **Apply:** `1Cor.7.25` la: `Domini elementia` → `Domini clementia`
16. **1 Corinthians 7:27** *Devinctus es uxore* → *Devinctus ex uxore*. 1573 *Deuinctus ex vxore … solutus ex vxore* (canvas 871); 1758.
   **Apply:** `1Cor.7.27` la: `Devinctus es uxore` → `Devinctus ex uxore`
17. **1 Corinthians 7:27** *solutus es uxore* → *solutus ex uxore*. As the item before: 1573 and 1758 *ex* both times.
   **Apply:** `1Cor.7.27` la: `solutus es uxore` → `solutus ex uxore`
18. **1 Corinthians 7:28** *vobis pareo* → *vobis parco*. 1573 *& ego vobis parco* (canvas 871); 1556, 1715, 1750.
   **Apply:** `1Cor.7.28` la: `vobis pareo` → `vobis parco`
19. **1 Corinthians 7:35** *non uti injiciam* → *non uti laqueum vobis injiciam*. 1573 *non vti laqueum vobis inijciam* (canvas 871); 1556 (OCR), 1758, 1750: Wikisource dropped *laqueum vobis*.
   **Apply:** `1Cor.7.35` la: `non uti injiciam` → `non uti laqueum vobis injiciam`
20. **1 Corinthians 7:36** *ea victa sit* → *ea vieta sit*. 1573 *vt ea vieta sit* (canvas 871: past her prime); 1556, 1750.
   **Apply:** `1Cor.7.36` la: `ea victa sit` → `ea vieta sit`
21. **1 Corinthians 8:1** *sacrificata astris* → *sacrificata deastris*. 1573 *sacrificata deastris* (canvas 872), Castellio's word throughout (8:4, 8:7, 8:10); 1758.
   **Apply:** `1Cor.8.1` la: `sacrificata astris` → `sacrificata deastris`
22. **1 Corinthians 8:1** *Cognitio instat* → *Cognitio inflat*. 1573 *Cognitio inflat* (canvas 872); 1747, 1750.
   **Apply:** `1Cor.8.1` la: `Cognitio instat` → `Cognitio inflat`
23. **1 Corinthians 8:3** *si quis Deus amat, in Deo* → *si quis Deum amat, is Deo*. 1573 *At si quis Deum amat, is Deo notus est* (canvas 872); 1758, 1715, 1747 (*Deum*, *is*).
   **Apply:** `1Cor.8.3` la: `si quis Deus amat, in Deo` → `si quis Deum amat, is Deo`
24. **1 Corinthians 8:5** *et qui Dei, et qui domini* → *et qui dii, et qui domini*. 1573 *& qui dij & qui domini* (canvas 872); 1556 (OCR).
   **Apply:** `1Cor.8.5` la: `et qui Dei, et qui domini` → `et qui dii, et qui domini`
25. **1 Corinthians 9:7** *quis vincam pangit* → *quis vineam pangit*. 1573 *quis vineam pangit* (canvas 872); 1715, 1726.
   **Apply:** `1Cor.9.7` la: `quis vincam pangit` → `quis vineam pangit`
26. **1 Corinthians 9:7** *quin ovalis lacte* → *quin ovilis lacte*. 1573 *quin ouilis lacte* (canvas 872); 1715, 1726.
   **Apply:** `1Cor.9.7` la: `quin ovalis lacte` → `quin ovilis lacte`
27. **1 Corinthians 9:11** *divina serminavimus, magnum vestro est* → *divina seminavimus, magnum vero est*. 1573 *diuina seminauimus, magnum verò est* (canvas 872); 1758, 1715, 1726 (*seminavimus*), 1715, 1726 (*vero*).
   **Apply:** `1Cor.9.11` la: `divina serminavimus, magnum vestro est` → `divina seminavimus, magnum vero est`
28. **1 Corinthians 9:24** *unus certamini pretium* → *unus certaminis pretium*. 1573 *certaminis precium* (canvas 873); 1556, 1747, 1750.
   **Apply:** `1Cor.9.24` la: `unus certamini pretium` → `unus certaminis pretium`
29. **1 Corinthians 9:25** *coronam: ad nos* → *coronam: at nos*. 1573 *coronam: at nos, immortalem* (canvas 873); 1758, 1715.
   **Apply:** `1Cor.9.25` la: `coronam: ad nos` → `coronam: at nos`
30. **1 Corinthians 10:17** *multi sumus ejus panis participes* → *multi sumus: omnes enim sumus ejusdem panis participes*. 1573 *vnum corpus multi sumus: omnes enim sumus eiusdem panis participes* (canvas 873); 1556 (OCR), 1758, 1747, 1750, 1726: Wikisource dropped a line.
   **Apply:** `1Cor.10.17` la: `multi sumus ejus panis participes` → `multi sumus: omnes enim sumus ejusdem panis participes`
31. **1 Corinthians 10:22** *Irritandus nobis* → *Irritandusne nobis*. 1573 *Irritandúsne nobis Dominus est?* (canvas 873); 1556, 1758, 1750.
   **Apply:** `1Cor.10.22` la: `Irritandus nobis` → `Irritandusne nobis`
32. **1 Corinthians 10:28** *propter conscientiam. Nam Dominus et terra* → *propterque conscientiam. Nam Domini et terra*. 1573 *propterq; conscientiam. Nam Domini & terra est* (canvas 873), as 10:26; 1758, 1747, 1750 (*propterque*), 1556, 1758, 1715, 1747, 1750 (*Domini*).
   **Apply:** `1Cor.10.28` la: `propter conscientiam. Nam Dominus et terra` → `propterque conscientiam. Nam Domini et terra`
33. **1 Corinthians 10:33** *omnia omnibus, non meae* → *omnia omnibus indulgeo, non meae*. 1573 *omnia omnibus indulgeo non meæ* (canvas 873); 1556, 1758, 1750: Wikisource lacks the verb.
   **Apply:** `1Cor.10.33` la: `omnia omnibus, non meae` → `omnia omnibus indulgeo, non meae`
34. **1 Corinthians 11:9** *propter mulierum creatus* → *propter mulierem creatus*. 1573 *propter mulierem creatus* (canvas 874); 1758, 1715, 1747, 1750.
   **Apply:** `1Cor.11.9` la: `propter mulierum creatus` → `propter mulierem creatus`
35. **1 Corinthians 11:10** *postestatis judicium* → *potestatis indicium*. 1573 *in capite potestatis indicium* (canvas 874: a sign of authority); 1715, 1747, 1750.
   **Apply:** `1Cor.11.10` la: `postestatis judicium` → `potestatis indicium`
36. **1 Corinthians 11:22** *Numnam domus non* → *Numnam domos non*. 1573 *Númnam domos non habetis* (canvas 874); 1758, 1715, 1747.
   **Apply:** `1Cor.11.22` la: `Numnam domus non` → `Numnam domos non`
37. **1 Corinthians 12:10** *alii Spiritum dijudicationes* → *alii spirituum dijudicationes*. 1573 *alij spirituum dijudicationes* (canvas 875); 1758, 1681, 1750, 1726.
   **Apply:** `1Cor.12.10` la: `alii Spiritum dijudicationes` → `alii spirituum dijudicationes`
38. **1 Corinthians 12:12** *multa quum sint, sic etiam* → *multa quum sint, unum corpus est: sic etiam*. 1573 *multa cùm sint, vnum corpus est: sic etiam Christus* (canvas 875); 1556 (OCR), 1758, 1747, 1726.
   **Apply:** `1Cor.12.12` la: `multa quum sint, sic etiam` → `multa quum sint, unum corpus est: sic etiam`
39. **1 Corinthians 12:16** *non sit oculus, se oculus, se corporis* → *non sit oculus, se corporis*. 1573 *quia non sit oculus, se corporis esse neget* (canvas 875, page image and OCR); 1556, 1750: Wikisource repeats *se oculus*.
   **Apply:** `1Cor.12.16` la: `non sit oculus, se oculus, se corporis` → `non sit oculus, se corporis`
40. **1 Corinthians 12:25** *dissidium, una condolescerent cuncta membra: sive in honore esset unum membrum, omnia membra congratularentur.* → *dissidium, sed eadem membra alia aliorum curam gererent:*. 1573 *ne esset in corpore dissidium, sed eadem membra alia aliorum curam gererent:* (canvas 875); 1758: Wikisource replaced the clause with the second half of 12:26.
   **Apply:** `1Cor.12.25` la: `dissidium, una condolescerent cuncta membra: sive in honore esset unum membrum, omnia membra congratularentur.` → `dissidium, sed eadem membra alia aliorum curam gererent:`
41. **1 Corinthians 12:26** *sive doloret unum* → *sive doleret unum*. 1573 *ac siue doleret vnum membrum* (canvas 875); 1747, 1750, 1726.
   **Apply:** `1Cor.12.26` la: `sive doloret unum` → `sive doleret unum`
42. **1 Corinthians 14:7** *vocem emmitentia, ut tibis,* → *vocem emittentia, ut tibia,*. 1573 *vocem emittentia, vt tibia, vt cithara* (canvas 876); 1556, 1758, 1715 (*tibia*).
   **Apply:** `1Cor.14.7` la: `vocem emmitentia, ut tibis,` → `vocem emittentia, ut tibia,`
43. **1 Corinthians 14:9** *verba faciatis, quid dicatur?* → *verba faciatis, quomodo intelligetur, quid dicatur?*. 1573 *verba faciatis, quomodo intelligetur quid dicatur?* (canvas 876); 1750, 1715, 1726: Wikisource dropped *quomodo intelligetur*.
   **Apply:** `1Cor.14.9` la: `verba faciatis, quid dicatur?` → `verba faciatis, quomodo intelligetur, quid dicatur?`
44. **1 Corinthians 14:27** *aut summum tres* → *aut ad summum tres*. 1573 *aut ad summum tres* (canvas 876); 1556, 1715, 1750, 1726.
   **Apply:** `1Cor.14.27` la: `aut summum tres` → `aut ad summum tres`
45. **1 Corinthians 15:1** *quod accepitis* → *quod accepistis*. 1573 *quod accepistis* (canvas 877); 1556, 1758, 1715, 1747, 1750, 1726.
   **Apply:** `1Cor.15.1` la: `quod accepitis` → `quod accepistis`
46. **1 Corinthians 15:2** *qua ratione docuerim* → *qua ratione vos docuerim*. 1573 *qua ratione vos docuerim* (canvas 877); 1556, 1758, 1747, 1750, 1726.
   **Apply:** `1Cor.15.2` la: `qua ratione docuerim` → `qua ratione vos docuerim`
47. **1 Corinthians 15:7** *apostolibus omnibus* → *apostolis omnibus*. 1573 *Apostolis omnibus* (canvas 877); 1556, 1758, 1715, 1747, 1726.
   **Apply:** `1Cor.15.7` la: `apostolibus omnibus` → `apostolis omnibus`
48. **1 Corinthians 15:9** *Ecclesiam injectatus sim* → *Ecclesiam insectatus sim*. 1573 *qui diuinam Ecclesiam insectatus sim* (canvas 877; long s, read on an enlarged crop: *insector*, to persecute); the OCRs read *infectatus*.
   **Apply:** `1Cor.15.9` la: `Ecclesiam injectatus sim` → `Ecclesiam insectatus sim`
49. **1 Corinthians 15:12** *apud vox mortuorum surrectionem* → *apud vos mortuorum resurrectionem*. 1573 *apud vos mortuorum resurrectionem fore negent* (canvas 877); 1758, 1681, 1747, 1750 (*vos*), 1758, 1750 (*resurrectionem*).
   **Apply:** `1Cor.15.12` la: `apud vox mortuorum surrectionem` → `apud vos mortuorum resurrectionem`
50. **1 Corinthians 15:34** *Ignorant enim nonnullis* → *Ignorant enim nonnulli*. 1573 *Ignorant enim nonnulli Deum* (canvas 878); 1758, 1715, 1747, 1750.
   **Apply:** `1Cor.15.34` la: `Ignorant enim nonnullis` → `Ignorant enim nonnulli`
51. **1 Corinthians 15:38** *cuique feminum corpus* → *cuique seminum corpus*. 1573 *suumq; cuique seminum corpus* (canvas 878); found by the f/s check.
   **Apply:** `1Cor.15.38` la: `cuique feminum corpus` → `cuique seminum corpus`
52. **1 Corinthians 15:39** *Non omnia caro* → *Non omnis caro*. 1573 *Non omnis caro eadem caro est* (canvas 878); 1758, 1747, 1750, 1726.
   **Apply:** `1Cor.15.39` la: `Non omnia caro` → `Non omnis caro`
53. **1 Corinthians 15:42** *refurgetur cum immortalitate* → *resurgetur cum immortalitate*. 1573 *resurgetur* (canvas 878, long s on the page image); Wikisource transcribed ſ as f in 15:42–44 (*refurget*, a word no lexicon knows); 1573's OCR reads it the same way.
   **Apply:** `1Cor.15.42` la: `refurgetur cum immortalitate` → `resurgetur cum immortalitate`
54. **1 Corinthians 15:43** *probro, refurgetur cum gloria* → *probro, resurgetur cum gloria*. As 15:42: 1573 *resurgetur cum gloria* (canvas 878).
   **Apply:** `1Cor.15.43` la: `probro, refurgetur cum gloria` → `probro, resurgetur cum gloria`
55. **1 Corinthians 15:43** *infirmitate, refurgetur cum potentia* → *infirmitate, resurgetur cum potentia*. As 15:42: 1573 *resurgetur cum potentia* (canvas 878).
   **Apply:** `1Cor.15.43` la: `infirmitate, refurgetur cum potentia` → `infirmitate, resurgetur cum potentia`
56. **1 Corinthians 15:44** *refurget corpus spirituale* → *resurget corpus spirituale*. As 15:42: 1573 *resurget corpus spirituale* (canvas 878).
   **Apply:** `1Cor.15.44` la: `refurget corpus spirituale` → `resurget corpus spirituale`
57. **1 Corinthians 15:58** *carissimi, praestat vos* → *carissimi, praestate vos*. 1573 *præstate vos constantes* (canvas 878); 1758, 1726.
   **Apply:** `1Cor.15.58` la: `carissimi, praestat vos` → `carissimi, praestate vos`
58. **1 Corinthians 16:15** *Achaiae primitas* → *Achaiae primitias*. 1573 *Achaiæ primitias* (canvas 879); 1758.
   **Apply:** `1Cor.16.15` la: `Achaiae primitas` → `Achaiae primitias`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (29)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 alone differs in order or form.
Section 5 lists the places where 1556 has the early reading.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; every item read on the 1573 page image unless marked OCR)

1. **1 Corinthians 1:17** *ne Christi crux* → *ne crux*. 1573 *eruditione, ne crux inanis fiat* (canvas 867); 1556, 1758, 1681. Wikisource's *Christi* (with 1747, 1750) is the early line's, as the Greek ὁ σταυρὸς τοῦ Χριστοῦ.
   **Apply:** `1Cor.1.17` la: `ne Christi crux` → `ne crux`
2. **1 Corinthians 3:1** *ut in re christiana infantes* → *ut in Christo infantes*. 1573 *vt in Christo infantes* (canvas 869); 1758. *In re christiana* is the early line (Wikisource, 1747, 1750) and **1556** (OCR *ut in re Christiana infantes*): a 1573 change.
   **Apply:** `1Cor.3.1` la: `ut in re christiana infantes` → `ut in Christo infantes`
3. **1 Corinthians 3:17** *Dei sacrum est* → *Dei sanctum est*. 1573 *templum enim Dei sanctum est* (canvas 869); 1758, 1726. **1556** has *sacrum* (OCR), with Wikisource and 1750: *sacer → sanctus*, as Rom 11:16 and 12:1, here a 1573 change.
   **Apply:** `1Cor.3.17` la: `Dei sacrum est` → `Dei sanctum est`
4. **1 Corinthians 3:21** *in hominibus:* → *apud homines:*. 1573 *Itaque nemo glorietur apud homines* (canvas 869); 1556, 1758, 1681. Wikisource's *in hominibus* with 1715, 1747, 1750.
   **Apply:** `1Cor.3.21` la: `in hominibus:` → `apud homines:`
5. **1 Corinthians 4:10** *vos in re christiana prudentes* → *vos in Christo prudentes*. 1573 *vos in Christo prudentes* (canvas 869); 1556 (OCR *uos in Christo prudétes*), 1758. The early line (Wikisource, 1750) *in re christiana*.
   **Apply:** `1Cor.4.10` la: `vos in re christiana prudentes` → `vos in Christo prudentes`
6. **1 Corinthians 4:12** *infestati patimur* → *insectati patimur*. 1573 *insectati, patimur* (canvas 869; long s, enlarged crop), with *infestati* as a margin gloss: Wikisource prints the gloss's word.
   **Apply:** `1Cor.4.12` la: `infestati patimur` → `insectati patimur`
7. **1 Corinthians 5:5** *ad perniciem corporis* → *ad perniciem carnis*. 1573 *ad perniciem carnis* (canvas 870), σαρκός; 1758, 1726. The early line *corporis* (Wikisource, 1750) and **1556** (OCR *ad perníciẽ cor-*): a 1573 change.
   **Apply:** `1Cor.5.5` la: `ad perniciem corporis` → `ad perniciem carnis`
8. **1 Corinthians 5:11** *cum hujusmodi homine* → *cum ejusmodi homine*. 1573 *cum eiusmodi homine* (canvas 870); 1556, 1758. Wikisource *hujusmodi* with 1681, 1715, 1747, 1750.
   **Apply:** `1Cor.5.11` la: `cum hujusmodi homine` → `cum ejusmodi homine`
9. **1 Corinthians 6:7** *injuriam patiamini?* → *injuriam patimini?*. 1573 *Cur non potius iniuriam patimini? cur non potius fraudamini?* (canvas 870); 1758, 1726. Wikisource's subjunctive with 1715, 1747, 1750.
   **Apply:** `1Cor.6.7` la: `injuriam patiamini?` → `injuriam patimini?`
10. **1 Corinthians 6:10** *nec cinaedi* → *nec paedicones*. 1573 *nec pædicones* (canvas 870); 1556 (OCR *pedícones*), 1726 (*prædicones*). Wikisource's *cinaedi* with 1747, 1750.
   **Apply:** `1Cor.6.10` la: `nec cinaedi` → `nec paedicones`
11. **1 Corinthians 6:18** *intra corpus suum peccat* → *intra suum corpus peccat*. 1573 *is intra suum corpus peccat* (canvas 870); 1556, 1758, 1681, 1726 (word order).
   **Apply:** `1Cor.6.18` la: `intra corpus suum peccat` → `intra suum corpus peccat`
12. **1 Corinthians 7:5** *vacetis: et deinde congrediamini* → *vacetis: deinde congrediamini*. 1573 *vacetis: deinde congrediamini* (canvas 871); 1758, 1726. Wikisource *et deinde* with 1747, 1750 and **1556** (OCR *uacetis & deinde*): a 1573 change.
   **Apply:** `1Cor.7.5` la: `vacetis: et deinde congrediamini` → `vacetis: deinde congrediamini`
13. **1 Corinthians 7:8** *bonum esse, ut sic maneant* → *bonum eis esse, si sic maneant*. 1573 *bonum eis esse, si sic maneant, vt ego* (canvas 871); 1556, 1758, 1726 (*eis*), 1747, 1750, 1726 (*si*).
   **Apply:** `1Cor.7.8` la: `bonum esse, ut sic maneant` → `bonum eis esse, si sic maneant`
14. **1 Corinthians 7:13** *qui tamen cum ea libenter habitet* → *qui tamen libenter cum ea habitet*. 1573 *qui tamen libenter cum ea habitet* (canvas 871); 1556, 1758, 1726 (word order).
   **Apply:** `1Cor.7.13` la: `qui tamen cum ea libenter habitet` → `qui tamen libenter cum ea habitet`
15. **1 Corinthians 7:37** *sed liber, sed sui juris* → *sed liber et sui juris*. 1573 *sed liber & sui iuris est* (canvas 871); 1758, 1750.
   **Apply:** `1Cor.7.37` la: `sed liber, sed sui juris` → `sed liber et sui juris`
16. **1 Corinthians 7:40** *mihi Dei habere spiritum* → *mihi habere Dei spiritum*. 1573 *Videor autem ego quoque mihi habere Dei spiritum* (canvas 871); word order.
   **Apply:** `1Cor.7.40` la: `mihi Dei habere spiritum` → `mihi habere Dei spiritum`
17. **1 Corinthians 8:10** *in deastrorum mensa accumbentem* → *in deastrorum mensam accumbentem*. 1573 *in deastrorum mensam accumbentem* (canvas 872). **1556** has *mensa* (OCR), with Wikisource, 1747, 1750: recorded as its variant.
   **Apply:** `1Cor.8.10` la: `in deastrorum mensa accumbentem` → `in deastrorum mensam accumbentem`
18. **1 Corinthians 9:21** *exleges lucrifacerem* → *exleges lucrificarem*. 1573 *quò exleges lucrificarem* (canvas 873), and 1556 the same (OCR), though both have *lucrifacerem* twice in 9:20 and in 9:22. Wikisource *lucrifacerem* with 1758, 1715, 1747, 1750. Castellio's form in both his texts; *lucrifico* is late Latin (a call for your eye).
   **Apply:** `1Cor.9.21` la: `exleges lucrifacerem` → `exleges lucrificarem`
19. **1 Corinthians 9:27** *subigoque corpus meum, neforte,* → *subigoque meum corpus, ne forte,*. 1573 *subigoq; meum corpus, ne forte* (canvas 873); 1758, 1726 (*ne forte*). Word order, and two words as your settled *nē forte* (5×).
   **Apply:** `1Cor.9.27` la: `subigoque corpus meum, neforte,` → `subigoque meum corpus, ne forte,`
20. **1 Corinthians 10:15** *quod dico ego* → *quod ego dico*. 1573 *iudicate vos, quod ego dico* (canvas 873); 1556, 1758, 1681, 1726.
   **Apply:** `1Cor.10.15` la: `quod dico ego` → `quod ego dico`
21. **1 Corinthians 10:18** *quod ad humanitatem attinet* → *quod ad carnem attinet*. 1573 *quod ad carnem attinet* (canvas 873); 1556 (OCR), 1758, 1726: *humanitas → caro*, as Rom 9:3, 9:5.
   **Apply:** `1Cor.10.18` la: `quod ad humanitatem attinet` → `quod ad carnem attinet`
22. **1 Corinthians 10:29** *libertas damnaretur ab* → *libertas damnetur ab*. 1573 *Cur enim mea libertas damnetur* (canvas 873); 1556, 1758. Wikisource's *damnaretur* with 1715, 1747.
   **Apply:** `1Cor.10.29` la: `libertas damnaretur ab` → `libertas damnetur ab`
23. **1 Corinthians 11:19** *ut probi fiant inter vos* → *ut fiant probi inter vos*. 1573 *vt fiant probi inter vos manifesti* (canvas 874); 1758 (word order).
   **Apply:** `1Cor.11.19` la: `ut probi fiant inter vos` → `ut fiant probi inter vos`
24. **1 Corinthians 12:11** *omnia effecit unus* → *omnia efficit unus*. 1573 *Atq; hæc omnia efficit vnus* (canvas 875), present as 12:6 *qui omnia efficit*; 1681. Wikisource's perfect with 1750.
   **Apply:** `1Cor.12.11` la: `omnia effecit unus` → `omnia efficit unus`
25. **1 Corinthians 14:15** *in animo orabo* → *Ita animo orabo*. 1573 *Quid ergo est? Ita animo orabo, vt significanter orem: ita animo cantabo* (canvas 876); 1556, 1758, 1681, 1715.
   **Apply:** `1Cor.14.15` la: `in animo orabo` → `Ita animo orabo`
26. **1 Corinthians 14:16** *illitterati nomen tenet* → *illitterati locum tenet*. 1573 *is qui illiterati locum tenet* (canvas 876), ὁ ἀναπληρῶν τὸν τόπον; 1556 (OCR *illiterati locum tenet*). Wikisource's *nomen* with 1747, 1715.
   **Apply:** `1Cor.14.16` la: `illitterati nomen tenet` → `illitterati locum tenet`
27. **1 Corinthians 15:4** *tertio die resurrexit ut* → *tertio die resurrexisse, ut*. 1573 *& tertio die resurrexisse, vt in literis habetur* (canvas 877), infinitive as *sepultum esse* (15:3–5 depend on *tradidi*); 1556, 1758, 1750, 1726.
   **Apply:** `1Cor.15.4` la: `tertio die resurrexit ut` → `tertio die resurrexisse, ut`
28. **1 Corinthians 15:54** *Absorpta est mors victoriose* → *Absorpta mors est victoriose*. 1573 *Absorpta mors est victoriosè* (canvas 878); word order.
   **Apply:** `1Cor.15.54` la: `Absorpta est mors victoriose` → `Absorpta mors est victoriose`
29. **1 Corinthians 16:3** *quos per epistolas* → *quos vos per epistolas*. 1573 *quos vos per epistolas probaueritis* (canvas 878); 1758, 1726.
   **Apply:** `1Cor.16.3` la: `quos per epistolas` → `quos vos per epistolas`

## 2a. Found on a second pass (3)

Long s that Wikisource transcribed as f, in words that are Latin either way, where 1573's OCR makes the same mistake
(so the f/s check, which compares the two, saw them agree). Reader 5 of stages 3–5 noticed 15:19 and 15:28; a sweep of
every *f* word in the draft then found 3:3 and nothing else (the other *fit* at 7:14 and 15:12 are *fit*).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; every item read on the 1573 page image)

1. **1 Corinthians 3:3** *quum fit inter vos* → *quum sit inter vos*. 1573 *Etenim cùm ſit inter vos æmulatio* (canvas 869, long s; the subjunctive with causal *cum*).
   **Apply:** `1Cor.3.3` la: `quum fit inter vos` → `quum sit inter vos`
2. **1 Corinthians 15:19** *fumus omnium* → *sumus omnium*. 1573 *ſumus omnium hominum miserrimi* (canvas 877, long s).
   **Apply:** `1Cor.15.19` la: `fumus omnium` → `sumus omnium`
3. **1 Corinthians 15:28** *ut fit Deus* → *ut sit Deus*. 1573 *vt ſit Deus omnia in omnibus* (canvas 878, long s; ἵνα ᾖ).
   **Apply:** `1Cor.15.28` la: `ut fit Deus` → `ut sit Deus`

## 3. Word division (7)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; every item read on the 1573 page image unless marked OCR)

1. **1 Corinthians 3:18** *Nemo seipsum fallat* → *Nemo se ipsum fallat*. 1573 *Nemo se ipsum fallat* (canvas 869); 1758; your settled *sē ipsum* (15×, never joined).
   **Apply:** `1Cor.3.18` la: `Nemo seipsum fallat` → `Nemo se ipsum fallat`
2. **1 Corinthians 11:18** *et non nihil credo* → *et nonnihil credo*. 1573 *& nonnihil credo* (canvas 874); 1556, 1758; Gaffiot's headword *nōnnihil*.
   **Apply:** `1Cor.11.18` la: `et non nihil credo` → `et nonnihil credo`
3. **1 Corinthians 11:28** *exploret homo seipsum* → *exploret homo se ipsum*. Your settled *sē ipsum* (15×), as 3:18; 1573 joins it here (*seipsum*, OCR).
   **Apply:** `1Cor.11.28` la: `exploret homo seipsum` → `exploret homo se ipsum`
4. **1 Corinthians 12:24** *Enim vero Deus* → *Enimvero Deus*. 1573 *Enimuerò Deus* (canvas 875); 1758, 1726; your settled *enimvērō* (4×) and Wikisource's own 9:25.
   **Apply:** `1Cor.12.24` la: `Enim vero Deus` → `Enimvero Deus`
5. **1 Corinthians 14:36** *A vobis ne divinus* → *A vobisne divinus*. 1573 *A vobisne* (canvas 876; the enclitic); 1556, 1758, 1715, 1747, 1726.
   **Apply:** `1Cor.14.36` la: `A vobis ne divinus` → `A vobisne divinus`
6. **1 Corinthians 15:10** *ut plusquam eorum* → *ut plus quam eorum*. 1573 *plus quàm* (OCR), with 1758, 1715, 1747, 1750; your settled *plūs quam* (4×).
   **Apply:** `1Cor.15.10` la: `ut plusquam eorum` → `ut plus quam eorum`
7. **1 Corinthians 15:15** *si quidem mortui* → *siquidem mortui*. 1573 *siquidem* (OCR), with 1747, 1726; your settled *sīquidem* (16×) for ‘since’.
   **Apply:** `1Cor.15.15` la: `si quidem mortui` → `siquidem mortui`

## 4. Checked and kept

- **3:22–23** (*vos autem Christi, et Christus Dei*): in Wikisource and 1573 alike; no words were missing (see the
  versification note above).
- **1:2** *nec non*: 1573 *necnon*; your settled *nec nōn* (20×, never joined). Kept apart.
- **1:14** *Gaium*: 1573 *Caium*, kept as Acts 19:29 and Rom 16:23 (Gaffiot *Gāius*).
- **1:25** *e*, **4:3** *a*, **9:5** *a*, **6:20** *e*, **14:36** *c*: note letters, not text. **2:2** *nihil aliud
  scire* (beside *nihil scire*) and **4:12** *infestati* (beside *insectati*) are 1573's margin glosses.
- **4:5** *ac tum*: 1573 and 1758 print *actum* close; your settled *ac tum* (6×) for ‘and then’. Kept.
- **9:2** *siquidem* (1573 *si quidem*) and **9:12** *ne quid* (1573 *nequid*): your settled forms (*sīquidem* 16×, *nē
  quid* 7×). Kept.
- **5:13** *vestrum*, **9:27** *rejectaneus*, **10:4** *petra Christus erat*, **10:7** *ad ludendum*, **12:5** *Dominus*,
  **13:13** *caritas*, **6:19** *neque vos esse vestros*: 1573 prints them (its OCR lost or misplaced them).
- **15:27** *sub ejus pedes*: 1573 *sub ei⁹* (the -us abbreviation), read by its OCR as *ei*. Kept.
- **14:35** *interroganto*: 1573 *interrogãto* (the bar is *n*). Kept.
- **12:6** *effectionum*, **12:28** *sanationum*, **13:12** *ambages, at*: 1573's OCR misreads (*effectioni*, *sanatiorum*,
  *amba gestat*). Kept.
- **15:6** *obdormierunt*: 1573 *obdormiuerunt* (canvas 877), as Wikisource's own 11:30 *obdormiverunt*. A spelling
  (decision 19's third plural, by verb): left to stage 3, a question in the stages 3–5 summary.
- **15:36** *viviscit*: 1573 *viuiscit* (Gaffiot *vīvīscō*). Kept.
- **16:24** the subscription *Ad Corinthios prima scripta est Philippis, missa per Stephanam, et Fortunatum, et
  Achaicum, et Timotheum.*: 1573 sets it in italics under the verse (canvas 879), as Romans 16:27; Wikisource runs it
  into 16:24. Kept in the verse, as in Romans (the question for the whole edition stands).
- **4:17** *caussam*, *carus* (1573 *causam*, *charus*), **16:6** *hiemabo* (1573 *hyemabo*), **7:21** *quamquam*:
  spellings, left to stage 3.
- **13:4–5**: 1573's verse 5 begins at *charitas non aemulatur*; the KJV's (and Wikisource's) at *Non se gerit
  turpiter*. Kept as the KJV.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573, now the text. Recorded, not applied (decision 24). 1556 is cited from its OCR
(e-rara 10281656), not the page image.

| Place | 1573 (= the text now) | 1556 | Also |
|---|---|---|---|
| 1 Cor 3:1 | *ut in Chrīstō infantēs* | *ut in re Christiana infantes* | Wikisource, 1747, 1750 |
| 1 Cor 3:17 | *templum enim Deī sānctum est* | *Dei sacrum est* | Wikisource, 1750 |
| 1 Cor 5:5 | *ad perniciem carnis* | *ad perniciem corporis* | Wikisource, 1750 |
| 1 Cor 7:5 | *vacētis: deinde congrediāminī* | *uacetis & deinde* | Wikisource, 1747, 1750 |
| 1 Cor 8:10 | *in deastrōrum mēnsam accumbentem* | *in deastrorum mensa* | Wikisource, 1747, 1750 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-10)

## 6. Spelling rules added

Wikisource writes *-mt-* in five words where Gaffiot, 1573 and your settled text (*sūmptum* 7×, *ēmptum*, *dirēmpt-*,
*redēmpt-*; only Rom 7:4 *perēmtī* has *-mt-*) write *-mpt-*: rules added to `data/rules/orthography.tsv`, approved
under decision 30 (*emti → empti* 7:23, *emtos → emptos* 6:20, *diremta → dirempta* 7:11, *sumtum → sumptum* 11:23,
*sumtus → sumptus* 9:18). 1573 prints *emptos* (6:20) and *dirempta* (7:11).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10)
