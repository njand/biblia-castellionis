# Judges 1–21, stages 1–2: Wikisource against 1738's pages

Proposed 2026-11-19 (decision 30's standing rule), on the Old Testament route of Leviticus 1–11
(`data/review/lev1-11-stage2.md`). Nathan: "Joshua transcription is already running on another workstation. Start
the next book. Run through all stages before you request my feedback."

- **Base**: the 1738 Leipzig edition (decision 1). Stage 1 drafted Wikisource's Judges, all 21 chapters
  (`python -m pipeline draft Judg 1-21`), as **`text/draft/JDG.usfm`** (BSB paragraphs, 618 verses in 1738's own
  numbers). Judges is 1738's leaves 292–318 (the hOCR's numbers; the archive.org image is one lower).
- **Wikisource's Judges is not a close transcript of 1738.** Besides its typing slips it drops clauses (14:13, 14:15),
  words (11:1 *Erat*, 13:22 *nam*, 13:23 *umquam*, 18:6 *iter illud*, 9:15 *ignis*, 9:38 *manus*), doubles words
  (9:23, 15:9), puts the chapter summary's words for 2:1's opening, respells names (*Philistini* for 1738's
  *Palaestini* throughout chapter 16, *-enes* for *-enses* in 1:27–31, *Jabisenses*, *Silonem*), and in a few places
  agrees with 1750 against 1738 (1:12 *Calebus*, 1:35 *quam*, 4:11 *Hobani*, 6:11 *Jovae*). So instead of reading
  only the collation's places, **every verse was read on 1738's pages**: six readers, each about 100 verses
  (leaves 292–296, 297–300, 301–304, 305–308, 309–312, 313–318), every leaf cut into four bands at the image's full
  resolution and doubtful words enlarged; 1750's OCR (`sources/archive/1750/text.txt`) checked at every larger
  difference. Claude read again on the page 2:1, 2:15, 6:11, 14:13 and 15:1 (all as the readers had them).
- **Collation** (`python -m pipeline collate Judg 1-21`, `data/calibration/Judg1-21-collation.tsv`): 1738 base, 1750
  witness (the 1726–27 text stops at Exodus 20). 102 "correct" places (1750 with 1738's OCR against Wikisource) and
  the 115 verses 1738's OCR covers under 60%: every one settled on the page by the readers. Most are 1738's spellings
  (*adgressi*, *numquam*, *exſtat*), line-end divisions and OCR noise; the real ones are among the items below.
- **Kept after checking**: 8:3 *eum* (OCR *cum*), 1:5 *Nactique*, 10:4 *Jairis*, 9:51, 9:54, the verses 20:25–30
  (word for word as the draft). Punctuation that differs is stage 5's.
- **1738's misprints, the draft keeping the sense** (the printed text keeps 1738): 20:21 *conferere* for *conferre*
  (1750 the same: a shared misprint; the draft's *conferre* stands); 9:43 *piuisas* (a battered d; 1750 *diuisas*;
  the draft's *divisas* stands).
- **Verse numbers**: every margin number the readers could see stands where the draft divides (some fall in the
  gutter: leaves 292–295, 299, 301, 303, 305, 312, 316–317); the renumbering to the KJV is §3.
- **Not in the draft, for later stages**: the chapter summaries (decision 50: not printed); 1738's footnotes, for the
  notes stage: 1:8 *scilicet arce ab hostibus retenta, nam paullo post negantur inde exacti Iebusæi*; 2:9 *Hæc in
  Iosua vocatur Thamnathasara*; 3:15 *læua manu pro dextra vtentem*; 10:12 *Græcus et Latinus legerunt Chananæis*
  (on *Maoniis*); 14:12, 14:15, 14:17 (notes d, e, f, leaf 309); 18:30 *in Hebræo est Manassis: sed in Latino Mosis,
  quod puto rectius*; 18:31 *hinc adparet, librum hunc scriptum esse post captiuitatem*; 19:29 *erat enim mortua*;
  20:16 *qui sinistris manibus pro dextris vterentur*; 20:41 *[a] decem millibus electis, supra memoratis* (first
  letters in the gutter); asterisks at 11:35, 12:8, 14:5, 14:20, 15:8, 15:16, 17:1, 18:2, 21:25 with no note on these
  leaves. Castellio's marks *L. cognatis suis H.* at 4:11 and *G.* … *H.* at 16:15–17 (the 1738 *L.*/*G.* … *H.*
  of the other books).
- **Printed spellings seen** (for stage 2b): 6:24 *Paciiouium* (one word; 1750 *Pacii ouium*), 7:1 *ſe-|ptemtrione*,
  7:12 *litorearum*, 9:28 *annon*, 9:37 *Immo*, 14:3 *arceſſeret*, 15:6 *auctorem*, 15:14 *ſimul ac*, *brachia*,
  16:13 *brachiis*, 16:12 and 19:20 *quidquam*, 18:22 *perſequuntur*, 20:46 *viginti quinque*, 21:11 *dumtaxat*, 6:21
  *conſumſit*, 6:25 *ſumto*, 11:35 *ſciſsis*, 16:23 *palæſtini*, 18:11 *dania* (lower case). The readers' notes are
  `judg1-21-stage2-readers.md`.

**Applied to the draft** under decision 30's standing rule.

## 1. Wikisource slips and readings 1738 has otherwise (156)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

1. **Judg 1:7** *Quum quidem illi dixit* → *Quum quidem ille dixit*. 1738 *quum quidem ille dixit,* (leaf 292, right); 1750 the same: Adonibezek speaks.
    **Apply:** `Judg.1.7` la: `Quum quidem illi dixit` → `Quum quidem ille dixit`
2. **Judg 1:11** *olim Cariatsepher* → *olim Cariathsepher*. 1738 *Cariath-|sepher* (leaf 293, left).
    **Apply:** `Judg.1.11` la: `olim Cariatsepher` → `olim Cariathsepher`
3. **Judg 1:12** *Ubi Calebus* → *Ubi Chalebus*. 1738 *Chale-|bus* (leaf 293, left), as the draft's own 1:13, 1:15 *Chalebi, Chalebo*; 1750 *Calebus*.
    **Apply:** `Judg.1.12` la: `Ubi Calebus` → `Ubi Chalebus`
4. **Judg 1:12** *qui Cariatsepher* → *qui Cariathsepher*. 1738 *Cari-|athsepher* (leaf 293, left).
    **Apply:** `Judg.1.12` la: `qui Cariatsepher` → `qui Cariathsepher`
5. **Judg 1:13** *itaque filius filiam Axam* → *itaque illius filiam Axam*. 1738 *itaque illius filiam Axam* (leaf 293, left); 1750 the same.
    **Apply:** `Judg.1.13` la: `itaque filius filiam Axam` → `itaque illius filiam Axam`
6. **Judg 1:15** *Chalebo quarenti* → *Chalebo quaerenti*. 1738 *quærenti* (leaf 293, left).
    **Apply:** `Judg.1.15` la: `Chalebo quarenti` → `Chalebo quaerenti`
7. **Judg 1:20** *Calebo autem* → *Chalebo autem*. 1738 *Chalebo autem* (leaf 293, left).
    **Apply:** `Judg.1.20` la: `Calebo autem` → `Chalebo autem`
8. **Judg 1:27** *occupaverunt Manassenes,* → *occupaverunt Manassenses,*. 1738 *Manasſenſes* (leaf 293, right); 1750 the same.
    **Apply:** `Judg.1.27` la: `occupaverunt Manassenes,` → `occupaverunt Manassenses,`
9. **Judg 1:29** *quoque Gazerenes* → *quoque Gazerenses*. 1738 *gazeren-|ses* (leaf 293, right); 1750 *-renses*.
    **Apply:** `Judg.1.29` la: `quoque Gazerenes` → `quoque Gazerenses`
10. **Judg 1:31** *Aseriani Acconenes,* → *Aseriani Acconenses,*. 1738 *Acconenses,* (leaf 293, right).
    **Apply:** `Judg.1.31` la: `Aseriani Acconenes,` → `Aseriani Acconenses,`
11. **Judg 1:31** *neque Ahalabenes, neque Axibenes,* → *neque Ahalabenses, neque Axibenses,*. 1738 *Ahalabenses, … Axibenses,* (leaf 293, right); 1750 the same.
    **Apply:** `Judg.1.31` la: `neque Ahalabenes, neque Axibenes,` → `neque Ahalabenses, neque Axibenses,`
12. **Judg 1:31** *neque Aphecenes,* → *neque Aphecenses,*. 1738 *Aphecenses,* (leaf 293, right).
    **Apply:** `Judg.1.31` la: `neque Aphecenes,` → `neque Aphecenses,`
13. **Judg 1:35** *Salebim: quam Josephaeis* → *Salebim: quamquam Josephaeis*. 1738 *quamquam, Ioſephæis prævalentibus* (leaf 293, right, enlarged); 1750's OCR *quamIosephaeis*.
    **Apply:** `Judg.1.35` la: `Salebim: quam Josephaeis` → `Salebim: quamquam Josephaeis`
14. **Judg 2:1** *Contra Israelitas Jovae nuntius a Galgalis* → *Adscendit autem Jovae nuntius a Galgalis*. 1738 *ADſcendit autem Iouæ nuntius a Galgalis* (leaf 294, left, the drop capital; read again by Claude); 1750 the same. Wikisource put the chapter summary's first words (*Contra Israelitas Iouæ nuntius*) for the verse's.
    **Apply:** `Judg.2.1` la: `Contra Israelitas Jovae nuntius a Galgalis` → `Adscendit autem Jovae nuntius a Galgalis`
15. **Judg 2:9** *Thamnatare in monte* → *Themnathare in monte*. 1738 *Themnathare* (leaf 294, left, enlarged; its footnote c: *Hæc in Iosua vocatur Thamnathasara*); 1750's OCR *Themnatare*.
    **Apply:** `Judg.2.9` la: `Thamnatare in monte` → `Themnathare in monte`
16. **Judg 2:15** *Jova praesides suscitarent* → *Jova praesides suscitaret*. 1738 *Ioua præſides ſuſcitaret,* (leaf 294, right; read again by Claude): Jova the subject.
    **Apply:** `Judg.2.15` la: `Jova praesides suscitarent` → `Jova praesides suscitaret`
17. **Judg 3:8** *eos Chusanrishathaimo* → *eos Chusanrasathaimo*. 1738 *Chuſanraſathaimo* (leaf 295, left, enlarged); 1750's OCR the same.
    **Apply:** `Judg.3.8` la: `eos Chusanrishathaimo` → `eos Chusanrasathaimo`
18. **Judg 3:9** *defensorem suscitato* → *defensore suscitato*. 1738 *defenſore ſuſcitato,* (leaf 295, left), the ablative absolute; 1750 the same.
    **Apply:** `Judg.3.9` la: `defensorem suscitato` → `defensore suscitato`
19. **Judg 3:10** *egressus, Chusanrishathaimum* → *egressus, Chusanrasathaimum*. 1738 *Chuſanraſathai-|mum* (leaf 295, left).
    **Apply:** `Judg.3.10` la: `egressus, Chusanrishathaimum` → `egressus, Chusanrasathaimum`
20. **Judg 4:1** *Sed Ado mortuo* → *Sed Aodo mortuo*. 1738 *Sed Aodo mortuo* (leaf 296, left).
    **Apply:** `Judg.4.1` la: `Sed Ado mortuo` → `Sed Aodo mortuo`
21. **Judg 4:6** *Haec Baracum, Abinoami filium, a Cedesa Nephthalensium arcessito, eo sic egit* → *Haec Baraco, Abinoami filio, a Cedesa Nephthalensium arcessito, cum eo sic egit*. 1738 *Hæc, Baraco, Abinoami filio, a Cedeſa Nephthalenſium arceſſito, cum eo ſic egit:* (leaf 296, left): the ablative absolute and *cum eo*; 1750 the same.
    **Apply:** `Judg.4.6` la: `Haec Baracum, Abinoami filium, a Cedesa Nephthalensium arcessito, eo sic egit` → `Haec Baraco, Abinoami filio, a Cedesa Nephthalensium arcessito, cum eo sic egit`
22. **Judg 4:7** *Sifaram* → *Sisaram*. 1738 *Siſaram* (leaf 296, left).
    **Apply:** `Judg.4.7` la: `Sifaram` → `Sisaram`
23. **Judg 4:11** *Cenaeis Hobani soceri* → *Cenaeis Hobabi soceri*. 1738 *Hobabi* (leaf 296, left, enlarged), Hobab (Num 10:29); 1750's OCR *Hobani*.
    **Apply:** `Judg.4.11` la: `Cenaeis Hobani soceri` → `Cenaeis Hobabi soceri`
24. **Judg 4:16** *ad unum Sisarae pedites.* → *ad unum omnes Sisarae copiae.*. 1738 *ad vnum omnes Siſaræ copiæ.* (leaf 296, right, enlarged); 1750 the same.
    **Apply:** `Judg.4.16` la: `ad unum Sisarae pedites.` → `ad unum omnes Sisarae copiae.`
25. **Judg 4:17** *Ipse Sisara autem pedibus* → *Ipse Sisara pedibus*. 1738 *Ipſe Siſara pedibus* (leaf 296, right, enlarged): no *autem*; 1750 the same.
    **Apply:** `Judg.4.17` la: `Ipse Sisara autem pedibus` → `Ipse Sisara pedibus`
26. **Judg 4:21** *eique tempus clavum transadigit* → *eique tempus clavo transadigit*. 1738 *eique tempus clauo transadigit* (leaf 296, right); 1750 the same.
    **Apply:** `Judg.4.21` la: `eique tempus clavum transadigit` → `eique tempus clavo transadigit`
27. **Judg 6:1** *septenno* → *septennio*. 1738 *ſeptennio* (leaf 298); 1750 the same.
    **Apply:** `Judg.6.1` la: `septenno` → `septennio`
28. **Judg 6:4** *Gagam* → *Gazam*. 1738 *Gazam* (leaf 298, left).
    **Apply:** `Judg.6.4` la: `Gagam` → `Gazam`
29. **Judg 6:11** *sub quercu Jovae Abiezeriani* → *sub quercu Joae Abiezeriani*. 1738 *ſub quercu Ioæ Abiezeriani* (leaf 298, right, enlarged; read again by Claude): the oak of Joash the Abiezrite, Gideon's father (Vulgate *Joas*); 1750's OCR *Iouae*, the line Wikisource follows.
    **Apply:** `Judg.6.11` la: `sub quercu Jovae Abiezeriani` → `sub quercu Joae Abiezeriani`
30. **Judg 6:11** *fiilio* → *filio*. 1738 *filio* (leaf 298, right).
    **Apply:** `Judg.6.11` la: `fiilio` → `filio`
31. **Judg 6:19** *egredditur* → *egreditur*. 1738 *egreditur* (leaf 299, left).
    **Apply:** `Judg.6.19` la: `egredditur` → `egreditur`
32. **Judg 6:31** *lacesivit* → *lacessivit*. 1738 *laceſſi-|uit* (leaf 299, right).
    **Apply:** `Judg.6.31` la: `lacesivit` → `lacessivit`
33. **Judg 6:34** *nuntios dimitti* → *nuntios dimittit*. 1738 *dimittit* (leaf 299, right); 1750 the same.
    **Apply:** `Judg.6.34` la: `nuntios dimitti` → `nuntios dimittit`
34. **Judg 7:2** *Madianitsa* → *Madianitas*. 1738 *Ma-|dianitas* (leaf 299, right).
    **Apply:** `Judg.7.2` la: `Madianitsa` → `Madianitas`
35. **Judg 7:2** *gloriates* → *gloriantes*. 1738 *gloriantes* (leaf 300, left).
    **Apply:** `Judg.7.2` la: `gloriates` → `gloriantes`
36. **Judg 7:5** *Atque ille homines ad aquas* → *Atque ubi ille homines ad aquas*. 1738 *Atque vbi ille homines ad aquas deduxit,* (leaf 300, left).
    **Apply:** `Judg.7.5` la: `Atque ille homines ad aquas` → `Atque ubi ille homines ad aquas`
37. **Judg 7:14** *responndens* → *respondens*. 1738 *reſpondens* (leaf 300, right).
    **Apply:** `Judg.7.14` la: `responndens` → `respondens`
38. **Judg 7:15** *vicotriam* → *victoriam*. 1738 *victoriam* (leaf 300, right); 1750 the same.
    **Apply:** `Judg.7.15` la: `vicotriam` → `victoriam`
39. **Judg 7:16** *amphrasque* → *amphorasque*. 1738 *amphorasque* (leaf 300, right); 1750 the same.
    **Apply:** `Judg.7.16` la: `amphrasque` → `amphorasque`
40. **Judg 7:19** *ille et ejuc centum* → *ille et ejus centum*. 1738 *eius* (leaf 300, right); 1750 the same.
    **Apply:** `Judg.7.19` la: `ille et ejuc centum` → `ille et ejus centum`
41. **Judg 7:19** *ad extremeum castrorum* → *ad extremum castrorum*. 1738 *extremum* (leaf 300, right); 1750 the same.
    **Apply:** `Judg.7.19` la: `ad extremeum castrorum` → `ad extremum castrorum`
42. **Judg 7:20** *clagendum* → *clangendum*. 1738 *clangendum* (leaf 300, right).
    **Apply:** `Judg.7.20` la: `clagendum` → `clangendum`
43. **Judg 7:26** *occierunt* → *occiderunt*. 1738 *occiderunt,* (leaf 301, left).
    **Apply:** `Judg.7.26` la: `occierunt` → `occiderunt`
44. **Judg 7:27** *Madianitas persecuti sunt, ad Gedeonem* → *Madianitas persecuti, ad Gedeonem*. 1738 *Madianitas perſecuti, ad Gedeo-|nem* (leaf 301, left, enlarged): no *sunt*.
    **Apply:** `Judg.7.27` la: `Madianitas persecuti sunt, ad Gedeonem` → `Madianitas persecuti, ad Gedeonem`
45. **Judg 8:4** *Joradanem* → *Jordanem*. 1738 *Iorda-|nem* (leaf 301, left).
    **Apply:** `Judg.8.4` la: `Joradanem` → `Jordanem`
46. **Judg 8:11** *scentiarum* → *scenitarum*. 1738 *ſcenita-|rum via,* (leaf 301, right); 1750 the same.
    **Apply:** `Judg.8.11` la: `scentiarum` → `scenitarum`
47. **Judg 8:15** *aggresses* → *aggressus*. 1738 *adgreſſus,* (leaf 301, right; the *ad-* is stage 3's).
    **Apply:** `Judg.8.15` la: `aggresses` → `aggressus`
48. **Judg 8:15** *militbus* → *militibus*. 1738 *militibus* (leaf 301, right); 1750 the same.
    **Apply:** `Judg.8.15` la: `militbus` → `militibus`
49. **Judg 8:24** *ut sibi despoliis inaurem* → *ut sibi de spoliis inaurem*. 1738 *de ſpoliis* (leaf 302, left), two words.
    **Apply:** `Judg.8.24` la: `ut sibi despoliis inaurem` → `ut sibi de spoliis inaurem`
50. **Judg 8:24** *hostes inaures, quod erat Ismaelitae* → *hostes inaures aureas, quod erant Ismaelitae*. 1738 *hoſtes inaures au-|reas, quod erant Iſmaelitæ.* (leaf 302, left); 1750 *erant*.
    **Apply:** `Judg.8.24` la: `hostes inaures, quod erat Ismaelitae` → `hostes inaures aureas, quod erant Ismaelitae`
51. **Judg 8:30** *suo semina* → *suo semine*. 1738 *ſuo ſemine* (leaf 302, left); 1750 the same.
    **Apply:** `Judg.8.30` la: `suo semina` → `suo semine`
52. **Judg 8:34** *per quam fuerant* → *per quem fuerant*. 1738 *(per|quem fuerant* (leaf 302, right): Jova; 1750 the same.
    **Apply:** `Judg.8.34` la: `per quam fuerant` → `per quem fuerant`
53. **Judg 8:35** *gratiamm* → *gratiam*. 1738 *gratiam* (leaf 302, right).
    **Apply:** `Judg.8.35` la: `gratiamm` → `gratiam`
54. **Judg 9:4** *ile* → *ille*. 1738 *ille* (leaf 302, right).
    **Apply:** `Judg.9.4` la: `ile` → `ille`
55. **Judg 9:9** *et homines, et arborum negotia* → *et homines, ut arborum negotia*. 1738 *et homines, vt arborum negotia capeſſeret.* (leaf 303, left); 1750 the same.
    **Apply:** `Judg.9.9` la: `et homines, et arborum negotia` → `et homines, ut arborum negotia`
56. **Judg 9:13** *Se vitis negavit* → *sed vitis negavit*. 1738 *ſed vitis ne-|gauit,* (leaf 303, left).
    **Apply:** `Judg.9.13` la: `Se vitis negavit` → `sed vitis negavit`
57. **Judg 9:15** *sin minus exiret e rhamno* → *sin minus exiret ignis a rhamno*. 1738 *ſin mi-|nus, exiret ignis a rhamno,* (leaf 303, left); 1750 the same.
    **Apply:** `Judg.9.15` la: `sin minus exiret e rhamno` → `sin minus exiret ignis a rhamno`
58. **Judg 9:23** *et Sichemitas malo spiritu, Sichemitas malo spiritu, effecit* → *et Sichemitas malo spiritu, effecit*. 1738 *et Sichemitas malo|ſpiritu, effecit* (leaf 303, right): Wikisource doubles the words.
    **Apply:** `Judg.9.23` la: `et Sichemitas malo spiritu, Sichemitas malo spiritu, effecit` → `et Sichemitas malo spiritu, effecit`
59. **Judg 9:36** *Eos Gaale conspicatus* → *Eos Gaal conspicatus*. 1738 *Eos|Gaal conſpicatus,* (leaf 304, left); 1750 the same.
    **Apply:** `Judg.9.36` la: `Eos Gaale conspicatus` → `Eos Gaal conspicatus`
60. **Judg 9:38** *et cum eis consere* → *et cum eis manus consere*. 1738 *et cum eis manus conſere.* (leaf 304, left); 1750 the same.
    **Apply:** `Judg.9.38` la: `et cum eis consere` → `et cum eis manus consere`
61. **Judg 9:39** *Tum Gaal Sichemitae educit* → *Tum Gaal Sichemitas educit*. 1738 *Tum|Gaal Sichemitas educit,* (leaf 304, left); 1750 the same.
    **Apply:** `Judg.9.39` la: `Tum Gaal Sichemitae educit` → `Tum Gaal Sichemitas educit`
62. **Judg 9:39** *ab illo victus fugit* → *ab illoque victus fugit*. 1738 *ab illoque victus fugit,* (leaf 304, left); 1750 the same.
    **Apply:** `Judg.9.39` la: `ab illo victus fugit` → `ab illoque victus fugit`
63. **Judg 9:41** *de Sichem habitatione* → *de Sichemae habitatione*. 1738 *de|Sichemæ habitatione* (leaf 304, left); 1750 the same.
    **Apply:** `Judg.9.41` la: `de Sichem habitatione` → `de Sichemae habitatione`
64. **Judg 9:48** *Selinonem* → *Selmonem*. 1738 *Sel-|monem,* (leaf 304, left, enlarged), Zalmon; 1750 the same.
    **Apply:** `Judg.9.48` la: `Selinonem` → `Selmonem`
65. **Judg 9:57** *tanta Sichemorum scelera* → *tanta Sichemitarum scelera*. 1738 *tanta Sichemitarum ſcelera* (leaf 304, right).
    **Apply:** `Judg.9.57` la: `tanta Sichemorum scelera` → `tanta Sichemitarum scelera`
66. **Judg 10:2** *Istaelitas* → *Israelitas*. 1738 *Iſraeli-|tas* (leaf 304, right).
    **Apply:** `Judg.10.2` la: `Istaelitas` → `Israelitas`
67. **Judg 10:2** *Mortuus Samiro sepultus* → *Mortuus Samire sepultus*. 1738 *Mor-|tuus Samire ſepultus eſt.* (leaf 304, right, enlarged); 1750 the same.
    **Apply:** `Judg.10.2` la: `Mortuus Samiro sepultus` → `Mortuus Samire sepultus`
68. **Judg 10:5** *Gamone* → *Camone*. 1738 *Camone* (leaf 305, left); 1750 the same.
    **Apply:** `Judg.10.5` la: `Gamone` → `Camone`
69. **Judg 10:7** *eos illo anno atrociter* → *eos anno illo atrociter*. 1738 *anno illo* (leaf 305, left); 1750 the same.
    **Apply:** `Judg.10.7` la: `eos illo anno atrociter` → `eos anno illo atrociter`
70. **Judg 10:9** *Benhamitisque* → *Benjamitisque*. 1738 *Beniamitis-|que* (leaf 305, left).
    **Apply:** `Judg.10.9` la: `Benhamitisque` → `Benjamitisque`
71. **Judg 10:10** *angustis* → *angustia*. 1738 *anguſtia* (leaf 305, left).
    **Apply:** `Judg.10.10` la: `angustis` → `angustia`
72. **Judg 10:17** *castramentis* → *castrametatis*. 1738 *caſtrametatis* (leaf 305, left).
    **Apply:** `Judg.10.17` la: `castramentis` → `castrametatis`
73. **Judg 10:18** *Coeprunt* → *Coeperunt*. 1738 *cœperunt* (leaf 305, left).
    **Apply:** `Judg.10.18` la: `Coeprunt` → `Coeperunt`
74. **Judg 11:1** *Quidam Jephtha, vir* → *Erat quidam Jephtha, vir*. 1738 *ERat quidam Iephtha* (leaf 305, right, the drop capital).
    **Apply:** `Judg.11.1` la: `Quidam Jephtha, vir` → `Erat quidam Jephtha, vir`
75. **Judg 11:1** *meretrice natus, Galaado genitus* → *meretrice natus, a Galaado genitus*. 1738 *meretrice natus, a Galaado genitus* (leaf 305, right); 1750 the same.
    **Apply:** `Judg.11.1` la: `meretrice natus, Galaado genitus` → `meretrice natus, a Galaado genitus`
76. **Judg 11:8** *omnes Galaaditis incolas* → *omnes Galaaditidis incolas*. 1738 *Galaadi-|tidis incolas* (leaf 305, right).
    **Apply:** `Judg.11.8` la: `omnes Galaaditis incolas` → `omnes Galaaditidis incolas`
77. **Judg 11:13** *Jaboq* → *Jaboc*. 1738 *Iaboc* (leaf 305, right).
    **Apply:** `Judg.11.13` la: `Jaboq` → `Jaboc`
78. **Judg 11:16** *ad Cades pervenissent* → *ad Cadem pervenissent*. 1738 *ad Cadem* (leaf 306, left), as 11:17 *in Cade*.
    **Apply:** `Judg.11.16` la: `ad Cades pervenissent` → `ad Cadem pervenissent`
79. **Judg 11:18** *nam Moabitis terminus* → *nam Moabitidis terminus*. 1738 *Moabitidis terminus* (leaf 306, left); 1750 the same.
    **Apply:** `Judg.11.18` la: `nam Moabitis terminus` → `nam Moabitidis terminus`
80. **Judg 11:22** *Jaboq* → *Jaboc*. 1738 *Iaboc* (leaf 306, left).
    **Apply:** `Judg.11.22` la: `Jaboq` → `Jaboc`
81. **Judg 11:22** *occupaverunt* → *occuparunt*. 1738 *occuparunt.* (leaf 306, left); 1750 the same.
    **Apply:** `Judg.11.22` la: `occupaverunt` → `occuparunt`
82. **Judg 11:29** *Galaaditas Manassenesque* → *Galaaditas Manassensesque*. 1738 *Manas-|ſenſesque* (leaf 306, right); 1750 the same.
    **Apply:** `Judg.11.29` la: `Galaaditas Manassenesque` → `Galaaditas Manassensesque`
83. **Judg 11:35** *sciscis* → *scissis*. 1738 *ſciſsis* (leaf 306, right).
    **Apply:** `Judg.11.35` la: `sciscis` → `scissis`
84. **Judg 12:9** *septultus* → *sepultus*. 1738 *ſe-|pultus* (leaf 307, right).
    **Apply:** `Judg.12.9` la: `septultus` → `sepultus`
85. **Judg 12:10** *mortuus: sepultus est Ajalone* → *mortuus est et sepultus Ajalone*. 1738 *mortuus eſt et ſepul-|tus Aialone* (leaf 307, right).
    **Apply:** `Judg.12.10` la: `mortuus: sepultus est Ajalone` → `mortuus est et sepultus Ajalone`
86. **Judg 12:13** *in Israelitis principatum* → *in Israelitas principatum*. 1738 *in Iſraelitas principatum* (leaf 307, right).
    **Apply:** `Judg.12.13` la: `in Israelitis principatum` → `in Israelitas principatum`
87. **Judg 13:1** *Philistaeis* → *Palaestinis*. 1738 *Palæſtinis* (leaf 307, right); 1750 the same (as the draft's 10:7, 14:3 *Palaestinis*).
    **Apply:** `Judg.13.1` la: `Philistaeis` → `Palaestinis`
88. **Judg 13:4** *sterilitas vitio* → *sterilitatis vitio*. 1738 *ſterilitatis vi-|tio* (leaf 307, right).
    **Apply:** `Judg.13.4` la: `sterilitas vitio` → `sterilitatis vitio`
89. **Judg 13:5** *Philistinorum* → *Palaestinorum*. 1738 *Palæſtino-|rum* (leaf 307, right).
    **Apply:** `Judg.13.5` la: `Philistinorum` → `Palaestinorum`
90. **Judg 13:22** *Moriemur; Deum vidimus.* → *Moriemur; nam Deum vidimus.*. 1738 *moriemur; nam | Deum vidimus.* (leaf 308); 1750 the same.
    **Apply:** `Judg.13.22` la: `Moriemur; Deum vidimus.` → `Moriemur; nam Deum vidimus.`
91. **Judg 13:23** *neque nos sic exaudivisset* → *neque nos umquam sic exaudivisset*. 1738 *neque nos | vmquam ſic exaudiuiſſet.* (leaf 308, right); 1750 the same.
    **Apply:** `Judg.13.23` la: `neque nos sic exaudivisset` → `neque nos umquam sic exaudivisset`
92. **Judg 13:25** *et Esthaol* → *et Estaol*. 1738 *Eſtaol.* (leaf 308, right).
    **Apply:** `Judg.13.25` la: `et Esthaol` → `et Estaol`
93. **Judg 14:4** *Nesciebat autem* → *Nesciebant autem*. 1738 *Neſciebant autem eius pa-|rentes* (leaf 308, right).
    **Apply:** `Judg.14.4` la: `Nesciebat autem` → `Nesciebant autem`
94. **Judg 14:13** *totidemque vestes elegantes.* → *totidemque vestes elegantes. Quumque illi conditionem accepissent, et, aenigma proponi, postularent; sic proposuit:*. 1738 *Quumque illi conditionem accepiſſent, et, ænigma proponi, poſtularent; ſic pro-|poſuit:* before the margin's 14 at *ex edace* (leaf 309, left; read again by Claude); 1750 the same. A clause Wikisource left out.
    **Apply:** `Judg.14.13` la: `totidemque vestes elegantes.` → `totidemque vestes elegantes. Quumque illi conditionem accepissent, et, aenigma proponi, postularent; sic proposuit:`
95. **Judg 14:15** *Samonis* → *Samsonis*. 1738 *Samſonis* (leaf 309, left).
    **Apply:** `Judg.14.15` la: `Samonis` → `Samsonis`
96. **Judg 14:15** *igni crematuros:* → *igni crematuros: an enim se illuc ab ipsis vocatos esse ad suum detrimentum?*. 1738 *igni crematuros: an enim ſe illuc ab ipſis vocatos eſſe ad ſuum detrimentum?* (leaf 309, left); 1750 the same. A clause Wikisource left out.
    **Apply:** `Judg.14.15` la: `igni crematuros:` → `igni crematuros: an enim se illuc ab ipsis vocatos esse ad suum detrimentum?`
97. **Judg 14:18** *oppidiani* → *oppidani*. 1738 *oppidani* (leaf 309, right).
    **Apply:** `Judg.14.18` la: `oppidiani` → `oppidani`
98. **Judg 15:1** *camprum ferens, ad eam* → *caprum ferens, et ad eam*. 1738 *caprum ferens, et ad eam* (leaf 309, right; read again by Claude).
    **Apply:** `Judg.15.1` la: `camprum ferens, ad eam` → `caprum ferens, et ad eam`
99. **Judg 15:5** *Iiisque* → *iisque*. 1738 *iiſque* (leaf 309, right).
    **Apply:** `Judg.15.5` la: `Iiisque` → `iisque`
100. **Judg 15:9** *in Judaeos faciunt, positisque castris exercitum in Judaeos faciunt, positisque castris exercitum in Judaea* → *in Judaeos faciunt, positisque castris exercitum in Judaea*. 1738 *expeditionem in Iudæos faciunt, poſitisque caſtris exercitum in Iudæa apud Maxillam explicant* (leaf 310, left): Wikisource repeats the words.
    **Apply:** `Judg.15.9` la: `in Judaeos faciunt, positisque castris exercitum in Judaeos faciunt, positisque castris exercitum in Judaea` → `in Judaeos faciunt, positisque castris exercitum in Judaea`
101. **Judg 15:10** *constrigendum* → *constringendum*. 1738 *conſtringendum* (leaf 310, left).
    **Apply:** `Judg.15.10` la: `constrigendum` → `constringendum`
102. **Judg 15:14** *instinctit* → *instinctu*. 1738 *inſtinctu* (leaf 310, left).
    **Apply:** `Judg.15.14` la: `instinctit` → `instinctu`
103. **Judg 15:18** *hanc tantum* → *hanc tantam*. 1738 *hanc tantam … victoriam* (leaf 310, left); 1750 the same.
    **Apply:** `Judg.15.18` la: `hanc tantum` → `hanc tantam`
104. **Judg 16:3** *aspectu positum* → *aspectu positi*. 1738 *adſpectu poſiti.* (leaf 310, right), agreeing with *montis*; 1750's OCR *potiti*.
    **Apply:** `Judg.16.3` la: `aspectu positum` → `aspectu positi`
105. **Judg 16:5** *Philistinorum proceres* → *Palaestinorum proceres*. 1738 *Palæſtinorum proceres* (leaf 310, right).
    **Apply:** `Judg.16.5` la: `Philistinorum proceres` → `Palaestinorum proceres`
106. **Judg 16:6** *subjugique* → *subigique*. 1738 *ſubigique* (leaf 310, right); 1750 the same.
    **Apply:** `Judg.16.6` la: `subjugique` → `subigique`
107. **Judg 16:8** *Philistini proceres* → *Palaestinae proceres*. 1738 *Palæſtinæ proceres* (leaf 310, right).
    **Apply:** `Judg.16.8` la: `Philistini proceres` → `Palaestinae proceres`
108. **Judg 16:9** *Philistini* → *Palaestini*. 1738 *Palæſtini Samſon* (leaf 311, left).
    **Apply:** `Judg.16.9` la: `Philistini` → `Palaestini`
109. **Judg 16:10** *vincula* → *vitilia*. 1738 *vitilia* (leaf 311, left); 1750 the same.
    **Apply:** `Judg.16.10` la: `vincula` → `vitilia`
110. **Judg 16:16** *Philistini* → *Palaestini*. 1738 *ingruunt tibi Palæſtini* (leaf 311, left).
    **Apply:** `Judg.16.16` la: `Philistini` → `Palaestini`
111. **Judg 16:19** *Philistinorum optimates* → *Palaestinorum optimates*. 1738 *Palæſtinorum optimates* (leaf 311, right).
    **Apply:** `Judg.16.19` la: `Philistinorum optimates` → `Palaestinorum optimates`
112. **Judg 16:20** *Philistinos* → *Palaestinos*. 1738 *Palæ-ſtinos inſtare* (leaf 311, right).
    **Apply:** `Judg.16.20` la: `Philistinos` → `Palaestinos`
113. **Judg 16:22** *Philistini* → *Palaestini*. 1738 *At Palæſtini* (leaf 311, right).
    **Apply:** `Judg.16.22` la: `Philistini` → `Palaestini`
114. **Judg 16:23** *convenerunt Philistini proceres* → *convenere Palaestini proceres*. 1738 *conuenere palæſtini proceres* (leaf 311, right; lower-case p, the printed text's).
    **Apply:** `Judg.16.23` la: `convenerunt Philistini proceres` → `convenere Palaestini proceres`
115. **Judg 16:23** *sibi a deo in manum* → *sibi a deo suo in manum*. 1738 *ſibi a deo ſuo in manum* (leaf 311, right); 1750 the same.
    **Apply:** `Judg.16.23` la: `sibi a deo in manum` → `sibi a deo suo in manum`
116. **Judg 16:25** *Itaque evocatus est Samson* → *Itaque evocatus Samson*. 1738 *Itaque euocatus Samſon* (leaf 311, right); 1750 the same.
    **Apply:** `Judg.16.25` la: `Itaque evocatus est Samson` → `Itaque evocatus Samson`
117. **Judg 16:27** *Philistinae* → *Palaestinae*. 1738 *Palæſtinæ optimates* (leaf 311, right).
    **Apply:** `Judg.16.27` la: `Philistinae` → `Palaestinae`
118. **Judg 16:28** *Philistinos* → *Palaestinos*. 1738 *Palæſtinos ſemel vlciſcor* (leaf 312, left).
    **Apply:** `Judg.16.28` la: `Philistinos` → `Palaestinos`
119. **Judg 16:30** *Philistinis* → *Palaestinis*. 1738 *cum Pa-|læſtinis* (leaf 312, left).
    **Apply:** `Judg.16.30` la: `Philistinis` → `Palaestinis`
120. **Judg 16:32** *Manoah* → *Manoae*. 1738 *Manoæ* (leaf 312, left); 1750 the same.
    **Apply:** `Judg.16.32` la: `Manoah` → `Manoae`
121. **Judg 17:7** *ex Bethlehem Judae,* → *ex Bethlehema Judaeae,*. 1738 *ex Bethlehema Iudææ* (leaf 312, left); 1750 the same.
    **Apply:** `Judg.17.7` la: `ex Bethlehem Judae,` → `ex Bethlehema Judaeae,`
122. **Judg 17:10** *sibique pastor sit* → *sibique pater sit*. 1738 *ſibique pater ſit* (leaf 312, right); 1750 the same (Vulgate *parens*).
    **Apply:** `Judg.17.10` la: `sibique pastor sit` → `sibique pater sit`
123. **Judg 18:1** *habitanum* → *habitandum*. 1738 *habitandum* (leaf 312, right).
    **Apply:** `Judg.18.1` la: `habitanum` → `habitandum`
124. **Judg 18:4** *ad fugiendum sacerdotio* → *ad fungendum sacerdotio*. 1738 *fungendum* (leaf 312, right); 1750 the same.
    **Apply:** `Judg.18.4` la: `ad fugiendum sacerdotio` → `ad fungendum sacerdotio`
125. **Judg 18:6** *Jovam eis prosperare* → *Jovam eis iter illud prosperare*. 1738 *Iouam eis iter illud proſperare.* (leaf 313, left).
    **Apply:** `Judg.18.6` la: `Jovam eis prosperare` → `Jovam eis iter illud prosperare`
126. **Judg 18:7** *nemine illi terra negotium* → *nemine illi terrae negotium*. 1738 *nemine illi terræ negotium* (leaf 313, left).
    **Apply:** `Judg.18.7` la: `nemine illi terra negotium` → `nemine illi terrae negotium`
127. **Judg 18:11** *ex gente Dan, Saraa et Esthaol* → *ex gente Dania, Saraa et Estaole*. 1738 *ex gente dania, Saraa et Eſtaole* (leaf 313, left; *dania* lower case, the printed text's).
    **Apply:** `Judg.18.11` la: `ex gente Dan, Saraa et Esthaol` → `ex gente Dania, Saraa et Estaole`
128. **Judg 18:11** *apud Cariathiarim in* → *apud Cariathiarimum in*. 1738 *apud Cariathiarimum in Iudæa:* (leaf 313, left).
    **Apply:** `Judg.18.11` la: `apud Cariathiarim in` → `apud Cariathiarimum in`
129. **Judg 18:16** *illis Danitis armatis* → *illis Daniis armatis*. 1738 *ſexcentis illis Da-|niis armatis* (leaf 313, left).
    **Apply:** `Judg.18.16` la: `illis Danitis armatis` → `illis Daniis armatis`
130. **Judg 18:19** *ac cu ipsis* → *ac cum ipsis*. 1738 *ac cum ipſis* (leaf 313, right).
    **Apply:** `Judg.18.19` la: `ac cu ipsis` → `ac cum ipsis`
131. **Judg 18:23** *clameret* → *clamaret*. 1738 *clamaret* (leaf 313, right).
    **Apply:** `Judg.18.23` la: `clameret` → `clamaret`
132. **Judg 19:4** *qui puella pater* → *qui puellae pater*. 1738 *qui puellæ pater* (leaf 314, left).
    **Apply:** `Judg.19.4` la: `qui puella pater` → `qui puellae pater`
133. **Judg 19:8** *manne* → *mane*. 1738 *mane* (leaf 314, left).
    **Apply:** `Judg.19.8` la: `manne` → `mane`
134. **Judg 19:11** *Jebusam sivi Hierosolymam* → *Jebusam, sive Hierosolymam*. 1738 *Iebuſam, ſiue Hieroſolymam* (leaf 314, right).
    **Apply:** `Judg.19.11` la: `Jebusam sivi Hierosolymam` → `Jebusam, sive Hierosolymam`
135. **Judg 19:12** *Quam apud Jebusam* → *Quum apud Jebusam*. 1738 *Quum apud Iebuſam* (leaf 314, right).
    **Apply:** `Judg.19.12` la: `Quam apud Jebusam` → `Quum apud Jebusam`
136. **Judg 19:12** *illudd* → *illud*. 1738 *illud* (leaf 314, right).
    **Apply:** `Judg.19.12` la: `illudd` → `illud`
137. **Judg 19:14** *Gabaeae aut Ramae* → *Gabaae aut Ramae*. 1738 *Gabaæ aut Ramæ* (leaf 314, right, enlarged).
    **Apply:** `Judg.19.14` la: `Gabaeae aut Ramae` → `Gabaae aut Ramae`
138. **Judg 19:17** *Gabaeae peregrinus* → *Gabaae peregrinus*. 1738 *Gabaæ peregrinus* (leaf 314, right).
    **Apply:** `Judg.19.17` la: `Gabaeae peregrinus` → `Gabaae peregrinus`
139. **Judg 19:20** *quiddem* → *quidem*. 1738 *quidem* (leaf 314, right).
    **Apply:** `Judg.19.20` la: `quiddem` → `quidem`
140. **Judg 19:23** *exhiliarantibus* → *exhilarantibus*. 1738 *exhilarantibus* (leaf 314, right).
    **Apply:** `Judg.19.23` la: `exhiliarantibus` → `exhilarantibus`
141. **Judg 19:23** *homiinem* → *hominem*. 1738 *hominem* (leaf 314, right).
    **Apply:** `Judg.19.23` la: `homiinem` → `hominem`
142. **Judg 19:28** *facienddum* → *faciendum*. 1738 *faciendum* (leaf 315, left).
    **Apply:** `Judg.19.28` la: `facienddum` → `faciendum`
143. **Judg 19:29** *respondderet* → *responderet*. 1738 *reſponderet* (leaf 315, left).
    **Apply:** `Judg.19.29` la: `respondderet` → `responderet`
144. **Judg 20:2** *quadrigenta* → *quadringenta*. 1738 *quadringenta* (leaf 315, right).
    **Apply:** `Judg.20.2` la: `quadrigenta` → `quadringenta`
145. **Judg 20:3** *quodd* → *quod*. 1738 *id quod* (leaf 315, right).
    **Apply:** `Judg.20.3` la: `quodd` → `quod`
146. **Judg 20:3** *quarentibus* → *quaerentibus*. 1738 *quærentibus* (leaf 315, right).
    **Apply:** `Judg.20.3` la: `quarentibus` → `quaerentibus`
147. **Judg 20:5** *meam concubinam stupraverunt et morte affecerunt* → *meam concubinam et stupro et morte affecerunt*. 1738 *meam concubinam et ſtupro et morte adfecerunt.* (leaf 315, right); 1750 the same (the *ad-* is stage 3's).
    **Apply:** `Judg.20.5` la: `meam concubinam stupraverunt et morte affecerunt` → `meam concubinam et stupro et morte affecerunt`
148. **Judg 20:22** *adversus quos* → *adversum quos*. 1738 *aduerſum quos* (leaf 316, left); 1750 the same.
    **Apply:** `Judg.20.22` la: `adversus quos` → `adversum quos`
149. **Judg 20:24** *Eleazati* → *Eleazari*. 1738 *Eleazari* (leaf 316, left); 1750 the same.
    **Apply:** `Judg.20.24` la: `Eleazati` → `Eleazari`
150. **Judg 20:37** *repente Gabam* → *repente Gabaam*. 1738 *repente Gabaam* (leaf 316, right).
    **Apply:** `Judg.20.37` la: `repente Gabam` → `repente Gabaam`
151. **Judg 21:5** *ad conventum ad Jovam* → *ad conventus ad Jovam*. 1738 *ad [c]onuentus ad Iouam* (leaf 317, left; the c in the gutter); 1750's OCR *conuentus*.
    **Apply:** `Judg.21.5` la: `ad conventum ad Jovam` → `ad conventus ad Jovam`
152. **Judg 21:10** *ut Jabisenses Galaaditas* → *ut Jabenses Galaaditas*. 1738 *Iabenſes Galaaditas* (leaf 317, right), as the draft's own 21:12 *Jabensibus*.
    **Apply:** `Judg.21.10` la: `ut Jabisenses Galaaditas` → `ut Jabenses Galaaditas`
153. **Judg 21:11** *funditus everterent* → *funditus evertant*. 1738 *funditus euertant* (leaf 317, right).
    **Apply:** `Judg.21.11` la: `funditus everterent` → `funditus evertant`
154. **Judg 21:12** *apud Silonem in Chanaan situm adduxerunt* → *apud Siluntem in Chananaea sita adduxerunt*. 1738 *apud Siluntem in Chananæa ſita adduxerunt* (leaf 317, right); 1750's OCR *Siluntem*.
    **Apply:** `Judg.21.12` la: `apud Silonem in Chanaan situm adduxerunt` → `apud Siluntem in Chananaea sita adduxerunt`
155. **Judg 21:13** *erant, ut cum illis* → *erant, qui cum illis*. 1738 *qui cum illis colloquerentur* (leaf 317, right); 1750 the same.
    **Apply:** `Judg.21.13` la: `erant, ut cum illis` → `erant, qui cum illis`
156. **Judg 21:14** *ex Jabisensibus* → *ex Jabensibus*. 1738 *ex Iabenſibus* (leaf 317, right).
    **Apply:** `Judg.21.14` la: `ex Jabisensibus` → `ex Jabensibus`

## 2. Wikisource respellings set back to 1738 (14)

Not readings: spellings Wikisource changed. The draft takes 1738's, so that stage 3 spells them by the approved rules and the printed text pairs them with the page.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

1. **Judg 7:1** *a septentrione* → *a septemtrione*. 1738 *ſe-|ptemtrione* (leaf 299, right).
    **Apply:** `Judg.7.1` la: `a septentrione` → `a septemtrione`
2. **Judg 7:12** *arenarum littorearum* → *arenarum litorearum*. 1738 *litorearum* (leaf 300, left).
    **Apply:** `Judg.7.12` la: `arenarum littorearum` → `arenarum litorearum`
3. **Judg 9:28** *an non Jerobaalis* → *annon Jerobaalis*. 1738 *annon* (leaf 303, right), one word.
    **Apply:** `Judg.9.28` la: `an non Jerobaalis` → `annon Jerobaalis`
4. **Judg 9:37** *Imo enimvero* → *Immo enimvero*. 1738 *Immo* (leaf 304, left).
    **Apply:** `Judg.9.37` la: `Imo enimvero` → `Immo enimvero`
5. **Judg 14:3** *accerseret* → *arcesseret*. 1738 *arceſſeret* (leaf 308, right).
    **Apply:** `Judg.14.3` la: `accerseret` → `arcesseret`
6. **Judg 15:6** *authorem* → *auctorem*. 1738 *auctorem* (leaf 309, right).
    **Apply:** `Judg.15.6` la: `authorem` → `auctorem`
7. **Judg 15:14** *simulac ad Maxillam* → *simul ac ad Maxillam*. 1738 *ſimul ac* (leaf 310, left).
    **Apply:** `Judg.15.14` la: `simulac ad Maxillam` → `simul ac ad Maxillam`
8. **Judg 15:14** *bracchia* → *brachia*. 1738 *brachia* (leaf 310, left).
    **Apply:** `Judg.15.14` la: `bracchia` → `brachia`
9. **Judg 16:12** *quicquam* → *quidquam*. 1738 *quidquam* (leaf 311, left).
    **Apply:** `Judg.16.12` la: `quicquam` → `quidquam`
10. **Judg 16:13** *bracchiis* → *brachiis*. 1738 *brachiis* (leaf 311, left).
    **Apply:** `Judg.16.13` la: `bracchiis` → `brachiis`
11. **Judg 18:22** *persecuntur* → *persequuntur*. 1738 *perſequuntur* (leaf 313, right).
    **Apply:** `Judg.18.22` la: `persecuntur` → `persequuntur`
12. **Judg 19:20** *quicquam* → *quidquam*. 1738 *quidquam* (leaf 314, right).
    **Apply:** `Judg.19.20` la: `quicquam` → `quidquam`
13. **Judg 20:46** *vigintiquinque* → *viginti quinque*. 1738 *viginti quinque* (leaf 317, left), two words.
    **Apply:** `Judg.20.46` la: `vigintiquinque` → `viginti quinque`
14. **Judg 21:11** *duntaxat* → *dumtaxat*. 1738 *dumtaxat* (leaf 317, right).
    **Apply:** `Judg.21.11` la: `duntaxat` → `dumtaxat`

## 3. Versification (decision 5)

**63 edits** in `data/versification/Judg1-21.draft.edits.tsv` (29 splits, 33 merges, one chapter break), applied
after §1–2 (`versify Judg --draft --apply`; the file was `Judg.draft.edits.tsv`): the words unchanged, every chapter
at the KJV's count (618 verses). Each KJV number now holds the Latin that renders that KJV verse, split at the Latin
words where the KJV's next verse begins; each edit's note gives the English and the Latin. Proposed by a reader with
the KJV and BSB beside every verse; four anchors re-set by Claude after the stage-2 corrections (9:39 *ab illoque*,
12:10 *mortuus est et sepultus*, 16:23 *convenere Palaestini*, 20:22 *adversum*).

- **Chapters 3, 8, 10, 11, 13, 14, 15, 17** unchanged (clause-level differences stand as Castellio divides them).
- **5:31 / 6:1**: the KJV's 5:31 ends "And the land had rest forty years", Castellio's 6:1 *Ita otium fuit annis
  quadraginta.*: the chapter break moved to *Deinde offensus ab* (as Exod 7:1).
- **2**: one behind from 12 (*atque ita offenso relictoque Jova*, the KJV's 13, split off). **7**: his 24–25 and 26–27
  are the KJV's 24 and 25. **12**: Ibzan's, Elon's and Abdon's verses cut where the KJV's are (Castellio gives each
  judge two verses, the KJV three). **16**, **19**, **21**: shifts of one; **20** (the three battles) is the hardest:
  26 edits, Castellio being up to three verses off in 17–45, no verse range needed.
- **Calls a later reader may revisit** (as proposed): 20:27–28 split inside Castellio's parenthesis at *cui tum
  ministrabat Phinees* (where the KJV divides its own); 20:34–35 *ingruentis sibi mali ignaros* (the KJV's 34) left in
  35, being a participle of 35's clause; 20:39 begins with the openings of the KJV's 40–41 (left; a range 39–41 the
  alternative); 18:28–29 left (the KJV's 28 would start inside a relative clause); 12:9, 16:17, 19:9, 20:28, 20:29,
  21:16–17 a split and a merge each, so the boundary falls exactly where the KJV's verse begins. Stages 3–5 check every
  boundary again with the KJV beside each verse.

## 4. Found in stage 2b: a word stage 2 missed (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

The printed text's readers (stage 2b) read every word 1738's OCR missed; one differs from the draft by more than
spelling (KJV numbering, after §3).

1. **Judg 20:15** *Recensiti sunt eo tempore* → *Recensitique sunt*. 1738 *exirent: recen-|ſitique ſunt eo tempore*
   (leaf 316; orig reader 6, 2026-11-19); 1750 *recen-|fitique funt* (OCR line 36707). Missed by the stage-2 reader.
   The case after the colon is stage 5's.
    **Apply:** `Judg.20.15` la: `Recensiti sunt eo tempore` → `Recensitique sunt eo tempore`

- **Kept**: 19:9 *dies jam ad vesperum devexus inclinaret*: 1738 prints *deuectus* (leaf 314, the ct ligature,
  enlarged by orig reader 5), 1750 *de-|vexus* (OCR line 36482–3), which the sense needs ("the day declining
  towards evening"; Gaffiot *dēvexus*). 1738's misprint; the printed text keeps *deuectus*. 3:13 1738 *Isra-|raelitas*
  (leaf 295), a misprint, likewise kept in the printed text only.

## 5. Found in stage 2b and stages 3–5: more Wikisource changes (KJV numbering)

The printed text, once every word was read (stage 2b), was compared word for word with the draft: these are the
places where the draft's word is Wikisource's and not 1738's. Two are readings (Wikisource's *dicitare* is no word;
*disgressi* for *digressi*), the rest spellings no approved rule covers, set back to 1738's (the classical forms
Gaffiot heads: *quamquam*, *numquam*, *exst-*, *ceter-*, *hēred-*, *simulacrum*), as §2. Found by the stages 3–5
readers too (1, 4, 5, 7).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

1. **Judg 9:28** *dicitare* → *dictitare*. 1738 *dictitare* (leaf 303, right; orig reader 3, clear on the page): Gaffiot *dictitō*, 'keep saying'; Wikisource's *dicitare* is no word.
    **Apply:** `Judg.9.28` la: `dicitare` → `dictitare`
2. **Judg 18:21** *disgressi* → *digressi*. 1738 *digreſſi* (leaf 313; orig reader 5), as the draft's own 18:7 *digressi*.
    **Apply:** `Judg.18.21` la: `disgressi` → `digressi`
3. **Judg 21:16** *perissent* → *periissent*. 1738 *periiſſent* (leaf 317; orig reader 6).
    **Apply:** `Judg.21.16` la: `perissent` → `periissent`
4. **Judg 1:30** *quanquam* → *quamquam*. 1738 *quamquam* (leaf 293).
    **Apply:** `Judg.1.30` la: `quanquam` → `quamquam`
5. **Judg 2:2** *nunquam* → *numquam*. 1738 *numquam* (leaf 294).
    **Apply:** `Judg.2.2` la: `nunquam` → `numquam`
6. **Judg 11:25** *nunquid* → *numquid*. 1738 *numquid* (leaf 306).
    **Apply:** `Judg.11.25` la: `nunquid` → `numquid`
7. **Judg 2:10** *extitit* → *exstitit*. 1738 *exſtitit* (leaf 294).
    **Apply:** `Judg.2.10` la: `extitit` → `exstitit`
8. **Judg 10:1** *extitit* → *exstitit*. 1738 *exſtitit* (leaf 304).
    **Apply:** `Judg.10.1` la: `extitit` → `exstitit`
9. **Judg 19:30** *extitisse* → *exstitisse*. 1738 *exſtitiſſe* (leaf 315).
    **Apply:** `Judg.19.30` la: `extitisse` → `exstitisse`
10. **Judg 2:17** *exequendis* → *exsequendis*. 1738 *exſequendis* (leaf 294).
    **Apply:** `Judg.2.17` la: `exequendis` → `exsequendis`
11. **Judg 6:24** *extat* → *exstat*. 1738 *exſtat* (leaf 299).
    **Apply:** `Judg.6.24` la: `extat` → `exstat`
12. **Judg 1:26** *extruxit* → *exstruxit*. 1738 *exſtruxit* (leaf 293).
    **Apply:** `Judg.1.26` la: `extruxit` → `exstruxit`
13. **Judg 6:24** *extruxit* → *exstruxit*. 1738 *exſtruxit* (leaf 299).
    **Apply:** `Judg.6.24` la: `extruxit` → `exstruxit`
14. **Judg 6:28** *extructa* → *exstructa*. 1738 *exſtructa* (leaf 299).
    **Apply:** `Judg.6.28` la: `extructa` → `exstructa`
15. **Judg 20:48** *extabant* → *exstabant*. 1738 *exſtabant* (leaf 317).
    **Apply:** `Judg.20.48` la: `extabant` → `exstabant`
16. **Judg 20:48** *caeteros* → *ceteros*. 1738 *ceteros* (leaf 317), as the draft's own 20:14 *ceteris*.
    **Apply:** `Judg.20.48` la: `caeteros` → `ceteros`
17. **Judg 16:17** *caeterorum* → *ceterorum*. 1738 *ceterorum* (leaf 311).
    **Apply:** `Judg.16.17` la: `caeterorum` → `ceterorum`
18. **Judg 21:17** *haereditas* → *hereditas*. 1738 *hereditas* (leaf 317).
    **Apply:** `Judg.21.17` la: `haereditas` → `hereditas`
19. **Judg 14:6** *hoedum* → *haedum*. 1738 *hædum* (leaf 309).
    **Apply:** `Judg.14.6` la: `hoedum` → `haedum`
20. **Judg 18:14** *simulachrum* → *simulacrum*. 1738 *ſimulacrum* (leaf 313).
    **Apply:** `Judg.18.14` la: `simulachrum` → `simulacrum`
21. **Judg 18:17** *simulachrum* → *simulacrum*. 1738 *ſimulacrum* (leaf 313).
    **Apply:** `Judg.18.17` la: `simulachrum` → `simulacrum`
22. **Judg 18:20** *simulachrumque* → *simulacrumque*. 1738 *ſimulacrumque* (leaf 313).
    **Apply:** `Judg.18.20` la: `simulachrumque` → `simulacrumque`
23. **Judg 18:30** *simulachrum* → *simulacrum*. 1738 *ſimulacrum* (leaf 313).
    **Apply:** `Judg.18.30` la: `simulachrum` → `simulacrum`
24. **Judg 18:31** *simulachrum* → *simulacrum*. 1738 *ſimulacrum* (leaf 313).
    **Apply:** `Judg.18.31` la: `simulachrum` → `simulacrum`

## 6. Names made one with the settled text, and 6:24 (decision 46)

From the names reader's table (`data/review/judg1-21-names.md`; its hard calls are in `judg1-21-stages3-5.md` § "For
you"): one form per person, place and people, the settled form first. The printed text keeps 1738's (decision 58).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-19)

1. **Judg 6:24** *Pacii ovium* → *Pacijovium*. 1738 prints one word, *Paciiouium* (leaf 299, enlarged by the stage-2 reader; 1750 *Pacii ouium*): Castellio's name for the altar, "Peace-of-Jova" for יְהוָה שָׁלוֹם, as the settled Exod 17:15 *Signijōvium* for יְהוָה נִסִּי. Wikisource's *Pacii ovium* ("of the peace of sheep") is a misdivision. Found by stages 3–5 reader 3.
    **Apply:** `Judg.6.24` la: `Pacii ovium` → `Pacijovium`
2. **Judg 1:4** *Pheresaeos* → *Pherezaeos*. settled Pherezæōs (Deut 7:1, Gen 15:20) (Claude, 2026-11-19).
    **Apply:** `Judg.1.4` la: `Pheresaeos` → `Pherezaeos`
3. **Judg 1:10** *Sesaim* → *Sesaeum*. settled Num 13:22 Sēsæus (hard call 2) (Claude, 2026-11-19).
    **Apply:** `Judg.1.10` la: `Sesaim` → `Sesaeum`
4. **Judg 1:10** *Ahimanem* → *Achimanem*. settled Num 13:22 Achīman (hard call 2) (Claude, 2026-11-19).
    **Apply:** `Judg.1.10` la: `Ahimanem` → `Achimanem`
5. **Judg 1:10** *Tholmaim* → *Thalmaeum*. settled Num 13:22 Thalmæus (hard call 2) (Claude, 2026-11-19).
    **Apply:** `Judg.1.10` la: `Tholmaim` → `Thalmaeum`
6. **Judg 1:12** *Chalebus* → *Calebus*. settled Calebus (hard call 1) (Claude, 2026-11-19).
    **Apply:** `Judg.1.12` la: `Chalebus` → `Calebus`
7. **Judg 1:13** *Chalebi* → *Calebi*. settled Calebus (hard call 1) (Claude, 2026-11-19).
    **Apply:** `Judg.1.13` la: `Chalebi` → `Calebi`
8. **Judg 1:15** *Chalebo* → *Calebo*. settled Calebō (hard call 1) (Claude, 2026-11-19).
    **Apply:** `Judg.1.15` la: `Chalebo` → `Calebo`
9. **Judg 1:15** *Chalebus* → *Calebus*. settled Calebus (hard call 1) (Claude, 2026-11-19).
    **Apply:** `Judg.1.15` la: `Chalebus` → `Calebus`
10. **Judg 1:20** *Chalebo* → *Calebo*. settled Calebō (hard call 1) (Claude, 2026-11-19).
    **Apply:** `Judg.1.20` la: `Chalebo` → `Calebo`
11. **Judg 3:9** *Chalebi* → *Calebi*. settled Calebus (hard call 1) (Claude, 2026-11-19).
    **Apply:** `Judg.3.9` la: `Chalebi` → `Calebi`
12. **Judg 1:27** *Maggedonenses* → *Mageddonenses*. one spelling with 5:19 Mageddonias, Hebrew מְגִדּוֹ (hard call 9) (Claude, 2026-11-19).
    **Apply:** `Judg.1.27` la: `Maggedonenses` → `Mageddonenses`
13. **Judg 1:36** *Amorrhaeorum* → *Amorraeorum*. settled Amorræ- (Claude, 2026-11-19).
    **Apply:** `Judg.1.36` la: `Amorrhaeorum` → `Amorraeorum`
14. **Judg 5:19** *Thanacum* → *Thanachum*. one spelling with 1:27 Thanachum (hard call 9) (Claude, 2026-11-19).
    **Apply:** `Judg.5.19` la: `Thanacum` → `Thanachum`
15. **Judg 11:13** *Jaboc* → *Jabboc*. settled Jabbōcum (hard call 5) (Claude, 2026-11-19).
    **Apply:** `Judg.11.13` la: `Jaboc` → `Jabboc`
16. **Judg 11:22** *Jaboc* → *Jabboc*. settled Jabbōcum (hard call 5) (Claude, 2026-11-19).
    **Apply:** `Judg.11.22` la: `Jaboc` → `Jabboc`
17. **Judg 11:20** *Iazam* → *Iasam*. settled Num 21:23 Jāsam (hard call 6) (Claude, 2026-11-19).
    **Apply:** `Judg.11.20` la: `Iazam` → `Iasam`
18. **Judg 11:24** *Chamosus* → *Chamossus*. settled Num 21:29 Chamōssī (hard call 4) (Claude, 2026-11-19).
    **Apply:** `Judg.11.24` la: `Chamosus` → `Chamossus`
19. **Judg 18:11** *Cariathiarimum* → *Cariathjarimum*. one spelling with 18:12 Cariathjarimum (hard call 9) (Claude, 2026-11-19).
    **Apply:** `Judg.18.11` la: `Cariathiarimum` → `Cariathjarimum`
20. **Judg 21:19** *JOvae* → *Jovae*. the draft's capital O a typing slip (Claude, 2026-11-19).
    **Apply:** `Judg.21.19` la: `JOvae` → `Jovae`
