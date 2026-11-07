# The editions of Castellio's Latin Bible

Notes for the README and the front matter of a printed edition. They are kept to what has been seen: a title page, a library record, or a reading in a scan or its OCR. Where something is inferred or unknown, it says so. The evidence for each reading is in `data/calibration/scans.md`. The decisions these notes support are HUMAN.md decisions 15 and 24.

Sebastian Castellio (Sébastien Châteillon, 1515–1563) began his Latin translation in Geneva in 1542. He finished it in Basel in 1550, and Johannes Oporinus published it there in 1551 with a dedication to Edward VI of England. (These are general facts from the [Wikipedia article](https://en.wikipedia.org/wiki/Castellio_Bible); the dedication also appears in the Halle record for the 1750 edition.) His French Bible (Basel, 1555) is a separate translation and is not used here.

## Printed in Castellio's lifetime

| Year | Place, printer | What the edition says or shows | Scans |
|---|---|---|---|
| 1551 | Basel, [Jacob Parcus for] Johannes Oporinus | First edition, *Biblia … una cum eiusdem annotationibus*. In the Gospels it reads *homine natus* ("Son of man") and *collegium* (synagogue): Matthew 12 checked on the page | [Google Books BrlIAAAAcAAJ](https://books.google.com/books?id=BrlIAAAAcAAJ) (Austrian National Library); e-rara (UB Bern MUE Hospinian 44; UB Basel FG III 15) |
| 1553 | — | A *Novum Testamentum* listed in the README (no marginal notes, no verse numbers); not examined in M1 | [Google Books rFtSAAAAcAAJ](https://books.google.com/books?id=rFtSAAAAcAAJ) |
| 1554 | Basel, Oporinus | The title says *totum opus recognovit ipse*: Castellio revised the whole work himself. It adds a history supplement from Josephus (Ezra to the Maccabees, the Maccabees to Christ). There are two issues, with and without the annotation on Romans 9 (Castellio Correspondence Project). The Gospels' OCR has *homine natus* 70×, *filius hominis* 0×; *collegium* 52×, *synagoga* 0× | [MDZ bsb10196330](https://www.digitale-sammlungen.de/en/view/bsb10196330?page=1) (searchable OCR); [Google Books kpp_lc3BtOMC](https://books.google.com/books?id=kpp_lc3BtOMC) |
| **1556** | Basel, Oporinus | **The last edition from his lifetime that we found.** The Gospels' OCR has *filius hominis* 47×, *homine natus* 0×; *collegium* 53×, *synagoga* 0×. The New Testament base of this edition by decision 15, then replaced by 1573 (decision 24); **now the reference**, its readings where 1573 differs recorded as variants | [e-rara 10281656](https://www.e-rara.ch/bau_1/content/titleinfo/10281656) (UB Basel FG II 41; OCR and IIIF) |

Not yet checked: whether there were other lifetime printings (Latin NT-only issues after 1556, for example). The 1573 Perna edition (below) claims to print Castellio's last revision; it follows the 1556 text with some 30–60 later word changes.

## Printed after his death

| Year | Place, printer, editor | What the title or record says | Text line (see below) | Scans |
|---|---|---|---|---|
| 1573 | Basel, Petrus Perna | *Biblia sacra ex Sebastiani Castalionis postrema recognitione. Cum annotationibus eiusdem, et historiae supplemento …* (USTC 616558, VD16 B 2638; folio, col. 1446 + 404): "from his last revision". The source the later title pages invoke. **Numbers the verses.** **The New Testament base of this edition** (decision 24, 2026-11-06) | **the 1556 line**, revised further (some 30–60 word changes, `data/calibration/nt1573.tsv`): *filius hominis* (e.g. John 13:31 *Nunc filius hominis illustratur*), Acts 19:4 *baptismate baptizavit*, Mark 12:44 *at hæc sua penuria*, Matt 2:11 *thus, & myrrham*, all as 1556; but Luke 12:6 *duobus assarijs* where 1556 has *dipondio* | [MDZ bsb10141277](https://www.digitale-sammlungen.de/en/view/bsb10141277?page=1) (BSB 2 B.lat. 112; searchable OCR, IIIF); [ÖNB](http://data.onb.ac.at/ABO/+Z165385104) (BE.1.G.6); 41 copies listed by USTC |
| 1681 | (Netherlands; Koninklijke Bibliotheek copy) | New Testament | *filius hominis* (37×) | [archive.org](https://archive.org/details/ned-kbn-all-00001225-001) |
| 1697 | — | Old and New Testament, with commentary and Castellio's reply to Beza (README) | not checked | [Google Books wc1QkYeThIwC](https://books.google.com/books?id=wc1QkYeThIwC) |
| 1715 | — | *Novum Testamentum Latinum … ex eiusdem postrema castigatione* | *homine natus* (61×) | archive.org (in the 1750 scan) |
| 1726–27 | (4 vols.) | The source of the finished chapters (TXT/1) | *filius hominis* | Google Books [vols 1–2](https://books.google.com/books?id=1EBbAAAAQAAJ), [3–4](https://books.google.com/books?id=40BbAAAAQAAJ) |
| 1728 | Leipzig, Walther (4 vols.) | *Biblia sacra ex … interpretatione eiusque postrema recognitione* | not checked | MDZ (SuStB Augsburg Th B V 102) |
| 1738 | Leipzig | *Biblia sacra … et postrema recognitione*, vol. 1 | (OT; **the Old Testament base**, transcribed by Wikisource) | [archive.org](https://archive.org/details/bibliasacraexseb01cast) |
| 1745 | Leipzig, Caspar Heinrich Fuchs; ed. **Johann Ludolf Bünemann** | *versionem et adnotationes ex primis editionibus emendavit*: the editor **restored the translation from the first editions**. Adds notes, maps, a plan of Solomon's temple, and an index of Castellio's Latinity (*Latinitatis selectae, vulgo neglectae, merito et falso suspectae*) | early line: *homine natus*, agrees with 1554 at 12 of 15 test places | [Halle ULB](https://opendata.uni-halle.de/handle/1981185920/56262) (IIIF, public domain) |
| 1747 | — | *Novum Testamentum Latinum … ex eiusdem postrema castigatione*, with Gesner's essay *De usu huius interpretationis* | *homine natus* (68×) | [archive.org](https://archive.org/details/novvm-testamentvm-latinvm-sebastiano-castellione-interprete-ex-eivsdem-postrema-castigatione-1747) |
| 1750 | Leipzig, Bernhard Christoph Breitkopf (Sysang named in the record) | *… praecipue in usum studiosae iuventutis denuo evulgata*: **for students** | *homine natus* (81×) | [archive.org](https://archive.org/details/biblia-sacra-ex-sebastiani-castellionis-interpretatione-eivsqve-postrema-1750); [Halle ULB](https://opendata.uni-halle.de/handle/1981185920/65566) |
| 1758 | (2 vols.) | *Novum Testamentum ex Sebastiani Castalionis interpretatione* | *filius hominis* (67×) | archive.org [vol. 1](https://archive.org/details/bim_eighteenth-century_novum-testamentum-ex-seb_1758_1), [vol. 2](https://archive.org/details/bim_eighteenth-century_novum-testamentum-ex-seb_1758_2) |
| 1760 | Leipzig, Breitkopf | *Novum Iesu Christi Testamentum … postrema recognitione praecipue in usum studiosae iuventutis denuo evulgatum*: for students. **Cited by Wikisource as its NT source** | *homine natus*; follows the early line (agrees with 1554 at 9 of 15, with 1556 at 4 of 14) | [Google Books FsdIAAAAcAAJ](https://books.google.com/books?id=FsdIAAAAcAAJ) |
| (Wikisource) | — | Cites 1760 for the NT and 1738 for the OT | Gospels: the revised line (*filius hominis*), agreeing with 1556 at 10 of 14; but in Matthew 14–28 it departs from 1573 and the later printings at some 25 places, mostly words left out (23:39 *non*, 25:22 *talenta*) and a few of its own (28:1 *hebdomadis* for *septidui*), and in Luke 10–11 it alone has *juris peritus* for *legisperitus* (2026-11-07; whether these are 1760's readings was not checked). Acts–Revelation: the early line (*favor*, *humanitas*, *synagoga*, *lavit*), as in 1750/1760 | [la.wikisource](https://la.wikisource.org/wiki/Biblia_Sacra_interprete_Sebastiano_Castellione) |

## Two lines of text

The printed tradition splits on a few readings. "Son of man" is the clearest marker.

- **The early line:** *homine natus* ("born of a human"), *collegium* for synagogue, *respondet*, *haec nostis*, and so on. This is **Castellio's own early wording** (1551, 1554). Later printings that carry it:
  - 1715, 1747 and 1750;
  - Bünemann's 1745 edition, deliberately, since he restored "from the first editions";
  - the 1760 New Testament.
- **The revised line:** *filius hominis*, *hoc nostis*, *Tum Iesus ei dicit*, and so on. This is **Castellio's own 1556 revision**, revised again in the posthumous **1573** edition (*infidentiam*, *mundi*, *carne*, *duobus assariis*, …), which is what the later printings carry:
  - 1681, 1726–27 and 1758;
  - Wikisource's Gospels;
  - the finished chapters of this edition.

### What Castellio changed himself (1554 → 1556)

Seen at the Gospel test places in `scans.md`:
- *homine natus / homine natum* → *filius hominis / filium hominis* (Matt 20:28, Luke 19:10, John 13:31; 47 times in all)
- *Si hæc nostis* → *Si hoc nostis* (John 13:17)

He kept *collegium* for synagogue, *& assumpto* (Matt 2:13), *thus, & myrrham* (Matt 2:11), *laudem tribuit* (Luke 18:43) and *respondet* (John 13:26).

In Acts–Revelation (1554 OCR search; 1556 OCR collation, `data/calibration/scans.md`), he moved from classical words back toward the received terms:
- *favor* (grace, χάρις) → *gratia*, e.g. the closing blessings: *Domini nostri Iesu Christi favor* → *gratia*.
- *quod ad humanitatem attinet* → *carnem* (flesh, σάρξ: Rom 9:5, 1 Cor 1:26, 10:18).
- *faustitatem* → *felicitatem* (Heb 12:17).
- In Acts 19:4, 1556 reads *baptismate baptizavit*, where Wikisource and 1760 have *baptismo lavit*. Whether 1554 had *lavit* there is not yet checked.

Wikisource's Gospels follow the 1556 revision, but its Acts–Revelation follow the early wording (as 1750 and 1760 do).

### Capitals for God in 1556

Searched in the e-rara OCR of the New Testament (`sources/erara-1556/`; long s reads as *f*), 2026-11-06. 1556 capitalizes only *Deus* and *Supremus* (*Supremi filius vocabitur*, *Supremi vis*, Luke 1:32, 35) and the title *Sanctus Dei* (Mark 1:24). Everything else is lower case: *a patre meo*, *pater vester coelestis*, *pater tuus*; *Dei filius*, *filio fidem habet*, *filius hominis*; *sancto spiritu*, *spiritum sanctum*. Any capitals this edition gives *Pater*, *Fīlius* or *Spīritus Sānctus* are therefore a modern editorial choice, not Castellio's.

### Names

Castellio spells Enoch *Henochus* in the Old Testament (Wikisource) but *Enochus* in the New (1556 *Enochi*, Luke 3:37; *Enochus*, Heb 11:5). This edition writes *Henōchus* in both (HUMAN.md decision 21). For Jericho he writes *Hierichus, -untis* in the Gospels (1556 *ad Hierichuntem*, Luke 10:30), where Wikisource's Gospels have *Hiericunt-*.

### A change after 1556: Luke 12:6

Castellio wrote *passerculi dipondio* (“two-penny sparrows”, Greek ἀσσαρίων δύο) in 1554 (MDZ page image 692) and 1556 (e-rara 10282355). The posthumous 1573 edition, “from his last revision”, reads *Cum væneant quinq; passerculi duobus assarijs* (MDZ bsb10141277, page image 801), and so do the later printings examined (1681, 1715, 1726–27, 1747, 1750, 1758). Wikisource has *dupondio*. Whether the change is Castellio's own last revision or Perna's editor's cannot be told from the print; the 1573 title claims his. All seen on the page images 2026-11-06. With 1573 as the base (decision 24), this edition keeps *duōbus assāriīs*; *dipondio* is recorded as 1556's variant.

### Words from the Latin marked *L.* … *G.*

In a few places Castellio prints words that follow the Latin (Vulgate) wording, set between an italic *L.* and *G.*: 1573 Matt 19:4 *qui principio fecit L. hominem, G. eos marem & fæminam* (canvas 765), Luke 10:1 *septuaginta L. duos, G. eosque binos* (799), 10:17 *septuaginta L. duo G. cum lætitia* (799), 11:7 *& tibi dare L. si ille pulsare perseuerauerit G.* (800, page image), John 5:4 *qui primus L. in piscinam G. descendebat* (817), Jas 5:3 *L. Pœnam G. vobis congessistis* (919). The marked words match the Clementine Vulgate where checked (Luke 10:1 *septuaginta duos*, 11:8 *si ille perseveraverit pulsans*, John 5:4 *in piscinam*, Matt 19:4 *hominem*). Castellio explains the system for the Old Testament in his *Ad lectores admonitio* (1573 canvas 16, OCR): what he found in the Greek or the old Latin translation of a book extant in Hebrew, and not in the Hebrew, he inserted, marking it *G* (Greek), *L* (Latin) or *G.L.* (both), *usque ad H.*, “which signifies the return to the Hebrew”. In the New Testament the same marks evidently set off words from the Latin (*L.*) until the return to the Greek (*G.*); that reading of the NT marks is an inference from the OT rule and the Vulgate matches. 1556 has the same marks at Luke 11:7 (OCR, e-rara 10282354), and so do 1750 (Luke 11:7) and 1758 (Luke 10:1, 10:17, 11:7); 1715 and 1747 omit the Luke 11:7 clause. Wikisource prints the marked words without the marks.

Found by the aligner on 2026-11-07 (it now records the marks as a flag; `data/witnesses/ocr-*/`): one more place, **Matt 8:18** *iussit L. discipulos G. traijcere* (1573 canvas 755, page image; 1758 OCR). Here the marked word is **not** the Clementine Vulgate's (*jussit ire trans fretum*, `sources/parallel/vulgate`), and the Greek has no word for it either (SBLGNT ἐκέλευσεν ἀπελθεῖν εἰς τὸ πέραν): so at this place *L.* does not mark the Vulgate's wording, which weakens the inference above. Which Latin Castellio followed here is not known. Marks also seen in the OCR of 1715 (Matt 19:4 *L, hominem G.*; Luke 10:1 *L. du-os G,*), 1681 (Luke 10:17) and 1556 (Matt 19:4 *L; hominem*). The OCRs read the marks as *L./I./J.* and *G./C.*; 1747 prints none of them where its OCR was read.

### Castellio's own words, seen in 1573 (Matthew 14–28)

Read on the 1573 page images on 2026-11-07 (canvas numbers in `data/review/matt14-28-stage2.md`), where Wikisource and the draft have something else: Matt 19:24 *facilius esse rudentem per foramen acus traijci* (a ship's cable, reading κάμιλος for κάμηλος; 1750 and Wikisource agree), Matt 28:1 *Ea autem nocte septidui* (“of the week”; also 1747), Matt 22:35 *legisperitus* (νομικός), Matt 26:54 *quo pacto confierent*.

### What the 1573 edition says about itself

Read 2026-11-06 in the BSB copy (MDZ bsb10141277: OCR of canvases 1–24, 740–750 and 961–1026; canvas 8 on the page image).

- **Title pages:** the Bible *ex Sebastiani Castalionis postrema recognitione* (canvas 7); the New Testament, which has its own title page, *ex eiusdem postrema castigatione* (canvas 747). These are the only places it claims a last revision.
- **Colophons:** *Basileae, excudebat Petrus Perna, anno salutis humanae M.D.LXXIII mense Augusto* after the Old Testament and the Josephus supplement (canvas 746), and *Basileae, apud Petrum Pernam, mense Augusto M.D.LXXIII* at the end (canvas 1019).
- **A memorial to Castellio** on the back of the title page (canvas 8): *Christo Servatori. Lemano Caelo invisus, Rauraco maxime gratus, illius inclementia dira passus, huius charitate mire complexus, sub Christi tandem crucem dura duriter durans, Deo et Patri coronandus vixit*: hated under Geneva's sky, warmly loved by Basel, he suffered the one's harshness and was embraced by the other's charity.
- **Castellio's own front matter:** the dedication to Edward VI (canvases 9–15), *Ad lectores admonitio* (16–17), which ends with his promise to go on correcting the translation (*deinceps, volente Deo, dabimus operam, ut si quid erratum … cognoverimus, id … corrigamus*), and *Quae via sit recta ad intelligendas sacras Scripturas* (18–19).
- **Testimonials,** *Iudicia doctorum virorum de Bibliis Castalionis* (canvases 20–21): Andreas Hyperius, Fadrique Furió Ceriol, a letter from Melanchthon to Castellio, a letter of 1562 from the Englishman Christopher Carlile to Castellio, and Laurence Humphrey. Letters addressed to Castellio suggest that whoever compiled the edition had his papers; that is an inference, not something the book says.
- **No preface by Perna or an editor:** nothing says where the "last revision" came from, who prepared it, or what changed. The front matter, the start of the New Testament and the end of the volume were all searched.
- The BSB copy has a later owner's handwritten note on an endpaper (canvas 6), legible in the OCR only in part; it names the editions of 1551, 1554, 1556 (*ab eod[em] recognita*) and 1573, and cites Alsted.

### Where the "last revision" came from: what the sources say (searched 2026-11-06)

- **Buisson** (*Sébastien Castellion*, 1892, vol. 2, appendix pp. 307–308 and 358–360; archive.org `sebastiencastell02buisuoft`) lists the 1573 Perna Bible (*postrema recognitione*, 1446 + 404 columns) without discussing where its text came from. He notes that both 1556 and "Perna, 1572" [the 1573 Bible] print only an asterisk at Rom 9:12, where the suppressed annotation stood. His list of separate New Testaments: Oporinus 1551 and 1553, Ludwig Lucius September 1556 (with the annotations), then posthumous Cologne 1564, Basel 1567, Venice 1571 and s.l. 1573 (the last four only from Draudius), Perna's Latin–French New Testament of 1572 ("the French corrected by Minus Celsus"), and a Venice [?] 1583 New Testament *ex ejusdem postrema castigatione*.
- **USTC** lists two 1572 Latin New Testaments titled *Novum Jesu Christi testamentum interprete Sebastiano Castalione. Ex postrema eiusdem castigatione*: one per Peter Perna (no. 678361, 7 copies), one ex officina Johann Oporinus (his successors; no. 678360, 2 copies). These are the earliest uses of the "last revision" label found: the revised New Testament was in print, under Perna's and Oporinus's successors' names, a year before the 1573 Bible. No digital copy of either was found (MDZ has none; the VD16 catalogue sits behind a bot check). A bookseller's description of the 1572 Perna Latin–French New Testament (VD16 ZV 28179 or ZV 228179) says its Latin was edited by Lelio Sozzini; that is unverified, and Lelio died in 1562.
- **Perna** printed other Castellio texts from his papers: the *Dialogi IV* (1578) from manuscript transcriptions, and an undated Psalter with Proverbs, Ecclesiastes and Wisdom *ex versione et postrema castigatione* (Buisson). So "postrema castigatione" was Perna's label for Castellio texts he printed after the author's death.
- **Not found:** any statement, by Perna or a modern scholar, that Castellio left a corrected copy of the Bible, or who prepared the 1572–73 text. Likely places: Guggisberg's biography (*Sebastian Castellio 1515–1563*, 1997; English 2003), studies of Perna's press (L. Perini, *La vita e i tempi di Pietro Perna*, 2002), and the 1572 New Testaments themselves, if a scan can be found (or requested from a holding library).

## Still to find out

- **1573** (Perna, *postrema recognitione*): found 2026-11-06 at MDZ (bsb10141277) and collated with 1556 the same day (`data/calibration/scans.md`). It is 1556 revised further: some 30–60 word changes (*incredulitatem → infidentiam*, *orbis → mundi*, *corpore → carne*, *sonat → interpretatur*, *dipondio → duobus assariis*), all carried by 1681, 1726–27 and 1758. Whether Castellio made them (as the title says) or Perna's editor did is still open: the edition has no preface saying (see “What the 1573 edition says about itself”). The Castellio correspondence (e.g. the Castellio Correspondence Project) or studies of Perna's press may say whether Castellio left a corrected copy.
- **Acts–Revelation:** compared with 1556 by OCR (2026-11-06). Wikisource follows the early wording there. Acts was collated against 1573 by OCR on 2026-11-07 (`data/calibration/acts1573.md`): about 92 places where Wikisource has the early line with 1715/1747/1750 (*synagoga → collegium*, *templum → fanum*, *homine natus → filius hominis*, *lavari → baptizari*, *hic sermo → hæc oratio*) and about 62 where it stands alone. A page-image check awaits stage 2.
- **Why the Leipzig printings (1745, 1750, 1760) went back to the early wording:** Bünemann's preface (1745) should say. Not yet read.
- **Printers and editors** of 1681, 1697, 1715, 1726–27 and 1758, from their title pages.
- **Purpose statements** in the prefaces: Castellio's own (1551 dedication, 1554 and 1556 prefaces), Bünemann's (1745), and Gesner's essay (1747). Not yet read.
