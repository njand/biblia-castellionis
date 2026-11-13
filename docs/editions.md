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

### Acts in 1573 against the early wording (stage 2, 2026-11-09)

Every place where Wikisource's Acts (the early line, with 1715, 1747, 1750) differs from 1573 was read on the 1573
page image (`data/review/acts1-28-stage2.md`, 225 corrections). 1758, 1681 and your 1726–27 text print the 1573
wording throughout; 1556, where its OCR reaches, mostly does too, but keeps the early reading at about a dozen places
(1:11 *viri Galilæi*, 10:34 *Tum*, 10:38 *sacro spiritu*, 14:15 *ad Deum immortalem*, 16:31 *fidem habe Domino
Iesu*, 19:4 *venienti*, 20:21 *Domino Iesu nostro*, 28:7 *Erant autem*), so those changes date from 1573. What the
revision does in Acts:
- **The received church words**: *synagoga* → *collegium* (all 23 places), *templum* → *fanum*, *lavari* →
  *baptizari*, *baptismo lavit* → *baptismate baptizavit* (19:4; *baptismus* → *baptisma* at 1:22, 10:37, 19:3),
  *homine natum* → *filium hominis* (7:56), *filius* → *puer* for Jesus as God's servant (4:30, as 3:13), *fidem
  habere* → *credere* (16:31, 19:4), *fortunare* → *felicitare* (3:25–26), *sacer* → *sanctus* (10:38).
- **Wording and syntax**: *hic sermo* → *hæc oratio* (6:5), *scriptura* → *literis* (1:16), *ferta obmoverem* → *munera
  libarem* (24:17), *sibi ad aliquam terram accedere videbantur* → *se alicui terræ propinquare suspicabantur*
  (27:27), *Assum prætervecti* → *soluerunt, & propius* (27:13), *verticosus* → *procellosus* (27:14), *cum potestate mihi a pontificibus præmissa* → *cum potestate & procuratione à Pontificibus accepta*
  (26:12), *supra* → *non plus* (25:6), *adsto* → *starem* (24:20), *sis acturus* → *agas* (22:26), *et* ↔ *ac*
  throughout; sentences joined across verses (9:1–2, 14:7–8, 16:12–13, 17:1–2, 18:11–12), and the letter of 15:23–29
  closed with *Valete*.
- **Verse numbers**: 1573 numbers Acts as the KJV does at 14 places where the 1760 line (Wikisource) starts a verse a
  few words earlier or later (2:8, 4:28, 4:35, 9:34, 10:31, 11:7, 11:30, 14:15, 16:7, 16:39, 17:7, 18:22, 27:28,
  28:31); it differs from the KJV at 19:40–41 (one verse) and in chapter 24 (28 verses).
- **1573's own misprints**, not followed: 13:19 *dedi eis* (for *dedit*). Its 12:15 *dicere* (a historic infinitive,
  with 1747) is followed.

### Romans in 1573 against the early wording (stage 2, 2026-11-09)

Wikisource's Romans is the early line too (with 1715, 1747, 1750); 1758 prints the 1573 text, and 1556, where its OCR
reaches, already has nearly all of the revision (`data/review/rom1-16-stage2.md`, 93 corrections, read on the 1573
page images). What differs from the early wording:
- **σάρξ, ἁμαρτία, ἅγιος, καρδία**: *humanitas* / *humana natura* → *caro* where the sense is descent (9:3, 9:5, 9:8:
  *quod ad carnem attinet*, *non carnis filii*), but *humana natura* stays at 4:1 and 6:19 in 1573 too; *vitiositas* →
  *peccatum* (7:17, 7:20, 7:23); *sacer* → *sanctus* (11:16 twice, 12:1); *animus* → *cor* (2:29 *quæ cordis est*);
  *scripturæ* → *literæ* (15:4). *Favor* stays (16:20, 16:24).
- **Other words**: *praevidit* → *prænovit* (8:29), *lenitudo* → *lentitudo* (2:4; 1556 and 1758 *lenitudinem*),
  *praeputium* → *præputiatus* (2:26, the man, not the foreskin: Castellio's note explains the masculine *ejus*),
  *mancipatus* → *emancipatus* (7:14; 1556 and 1758 *mancipatus*, but 1556 itself has *Deoque emancipati* at 6:22),
  *Amen* → *Etiam* (9:5, as he writes it at 1:25 and 11:36), and word order (1:2 *per vates suos*, 6:11 *per Iesum
  Christum*, 9:7, 9:9, 9:11 *ratum esset* moved to the end of its clause, 11:2 *suum populum*, 16:6 *nostra causa*).
  The changes at 1:2, 2:4, 6:11, 7:14 and 16:6 are not in 1556: they date from 1573.
- **Verse numbers**: 1573 numbers chapters 3 and 8 the old way, one verse short of the KJV (no break at KJV 3:23
  *nam omnes peccaverunt* or 8:21 *fore, ut ipsa*); elsewhere it agrees with the KJV where Wikisource (the 1760 line)
  does not (3:4, 3:6, 3:28, 11:18, 12:17, 15:9–11, 15:33), except at 9:12, which it starts before *sed ex vocante*.
- **The subscription** after 16:27 (*Scripta est Corinthi, missa per Phœbam, Cenchreensis ecclesiæ ministram.*) is set
  in italics under the last verse, apart from the text; Wikisource runs it into the verse.
- **1573's margins** carry glosses as well as references (1:11 *Scilicet* beside *hoc est*; 3:6 *si esset iniustus*),
  which its OCR runs into the text.

### 1 Corinthians in 1573 against 1556 and Wikisource (stage 2, 2026-11-10)

Every place where Wikisource's 1 Corinthians differs from 1573 was read on the 1573 page image (canvases 867–880;
`data/review/1cor1-16-stage2.md`, 97 corrections, 3 of them long-s slips found on a second pass). As in Romans and Acts, Wikisource prints the early wording, with
1715, 1747 and 1750; 1758 and 1726–27 print the 1573 text. Wikisource also has many slips of its own (12:25 replaced by
half of 12:26, 10:17 a line dropped, 15:42–44 *refurget* for *resurget*: long s transcribed as f).
- **The revision**: *in re christiana* → *in Christo* (3:1, 4:10), *corporis* → *carnis* (5:5, σαρκός), *humanitas* →
  *caro* (10:18 *quod ad carnem attinet*, as Rom 9:3, 9:5), *sacrum* → *sanctum* (3:17, as Rom 11:16), *cinaedi* →
  *paedicones* (6:10), *nomen* → *locum* (14:16, τὸν τόπον), *in hominibus* → *apud homines* (3:21), *infestati* →
  *insectati* (4:12, with *infestati* kept as a margin gloss), and word order (6:18 *suum corpus*, 7:13, 7:40, 9:27,
  10:15, 11:19, 15:54 *Absorpta mors est victoriose*).
- **1556 is part-way**: where its OCR can be read it already has 4:10 *in Christo*, 10:18 *carnem*, 6:10 *pedicones*, 14:16
  *illiterati locum*, 3:21 *apud homines*, but still the early 3:1 *ut in re Christiana infantes*, 3:17 *Dei sacrum est*,
  5:5 *ad perniciem corporis*, 7:5 *uacetis & deinde*, 8:10 *in deastrorum mensa*: those are 1573 changes (or 1573
  completing a revision 1556 began, since 1556 has 4:10 revised but not 3:1). Both 1556 and 1573 have *lucrificarem*
  at 9:21 beside *lucrifacerem* in 9:20 and 9:22.
- **Verse numbers**: 1573 numbers as Wikisource (the 1760 line) except at 3:21–22, where it prints 22 before *& Paulus*
  (the KJV's 3:22); neither has the KJV's 3:23, which both print inside 3:22. Both number 4:10–12 the old way (the KJV's
  4:11 *Ad hoc tempus* inside 4:10), end chapter 10 with the KJV's 11:1 *Imitatores mei estote*, and so number chapter
  11 one behind the KJV, printing the KJV's 11:34 as two verses. 1573 alone starts 13:5 at *charitas non aemulatur*.
- **The subscription** after 16:24 (*Ad Corinthios prima scripta est Philippis, missa per Stephanam, & Fortunatum, &
  Achaicum, & Timotheum.*) is set in italics apart, as after Romans; Wikisource runs it into the verse.

### 2 Corinthians in 1573 against 1556 and Wikisource (stage 2, 2026-11-10)

Every place where Wikisource's 2 Corinthians differs from 1573 was read on the 1573 page image (canvases 879–887;
`data/review/2cor1-13-stage2.md`, 45 corrections). 1573 heads it *Pauli Apostoli Epistola secunda ad Corinthios* (1
Corinthians: *Epistola prima*), with an argument *in Epistolam posteriorem ad Corinthios*. As in 1 Corinthians,
Wikisource prints the early wording with 1715, 1747 and 1750; 1758, 1681 and 1726–27 print the 1573 text.
- **The revision**: *caecas* → *torpentes* (3:13), *res* → *creatura* (5:17, καινὴ κτίσις), *sontem* → *peccatum* (5:21,
  ἁμαρτίαν), *persona* → *caro* (7:5, ἡ σάρξ), *meus favor* → *mea gratia* (12:9) and *favor* → *gratia* (13:14),
  *hujusmodi* → *ejusmodi* (9:12), *in ecclesiis* → *in ecclesias* (8:1), *quidem* → *equidem* (12:6), and word order
  (1:14 *vestra sumus*, 8:7 *omnibus in rebus*, 8:11 *est voluntatis*). **1556 already has all of these** where its OCR
  can be read (all but 9:12 and 13:14, which it garbles or lacks): unlike 1 Corinthians, 2 Corinthians was revised in full by 1556. The one 1573 change found is 10:12
  *Nec enim ausimus* (1556 *audemus*); 13:4 *per Dei in nos potentiam* (Wikisource and 1750 *in vos*, the Greek's
  εἰς ὑμᾶς) is 1573's, with 1758 and 1681, where 1556's OCR lacks the clause.
- **1573's misprints?** Three readings of 1573 go against 1556 and the sense, and 1758 (and at 11:28 1681) repeats
  them, as it follows 1573: 5:10 *ferat quique* (1556 also *quique*), 11:28 *quae me quotidiana destinent* (1556
  *distinent*), 12:7 *qui me tondat* (1556 *tundat*, κολαφίζῃ). The text keeps *quisque*, *distinent*, *tundat*.
- **Verse numbers**: 1573 numbers chapter 1 with 23 verses (its 21 holds the KJV's 1:21–22), chapter 7 with 16 (as
  the KJV; Wikisource 15) and chapter 13 with 13: like Wikisource it prints the KJV's 13:13 *Salutant vos sancti omnes*
  inside its 12, so the blessing is its 13 (the KJV's 14).
- **The subscription** after the blessing (*Ad Corinthios secunda scripta est Philippis Macedoniae, missa per Titum &
  Lucam.*) is set in italics apart, as after Romans and 1 Corinthians; Wikisource runs it into the verse.

### Galatians–Colossians in 1573 against 1556 and Wikisource (stage 2, 2026-11-11)

Every place where Wikisource differs from 1573 was read on the 1573 page image (canvases 889–904;
`data/review/gal1-6-stage2.md`, `eph1-6-`, `phil1-4-`, `col1-4-stage2.md`, 164 corrections). As in Romans and
Corinthians, Wikisource prints the early wording (*favor*, *fiducia*, *res*, *corpus*), with 1715, 1747 and 1750 often;
1758, 1681 and 1726–27 follow 1573.
- **The revision**, already in 1556 where its OCR can be read: *favor → gratia*, *fiducia → fides* (Gal 2–3, 10×),
  *nova natura → nova creatura* (Gal 6:15), *corpus → caro* (Eph 6:5, Col 3:22), *fortunavit → felicitavit* (Eph 1:3),
  *ambire → aemulari* (Gal 4:17–18), *dedit → dedidit* (Gal 1:4, Eph 5:2, 5:25).
- **1573's own changes against 1556** (recorded as variants; the text follows 1573): Gal 3:19 *sequestrum* (1556
  *sequestrem*), 4:14 *angelum* (*nuncium*), 4:17 *nos* (*uos*), 5:2 *circumcidemini* (*circumcidamini*) and *nihil
  vobis* (*uobis nihil*), 5:6 *operans* (*agens*), 5:12 *excidantur* (*excindantur*); Eph 2:21 *sanctum* (*sacrum*),
  4:18 *duritiem* (*torporem*), 4:21 *Si modo* (*Siquidem*); Phil 4:15 *et acceptorum* added to the text (1556 has it
  in margin note b), 4:19 *quibus* (*quicquid*); Col 2:12 *collocatam* (*collatam*).
- **Kept against 1573 with 1556**: Col 2:5 *at animo quidem* (1573 *ac*, against *quamvis*).
- **Verse numbers**: 1573 prints Gal 5:22–23 as one verse (canvas 892) and ends Colossians 3 with the KJV's 4:1
  (canvas 903), as Wikisource does. Its Col 4:8 margin gives Castellio's alternative *aliàs nostrarum rerum statum
  cognoscatis*.
- **Subscriptions** set in italics apart after each epistle, as after Romans and Corinthians.

### 1 Thessalonians–Philemon in 1573 against 1556 and Wikisource (stage 2, 2026-11-11)

Every place where Wikisource differs from 1573 was read on the 1573 page image (canvases 904–916;
`data/review/1thess1-5-stage2.md`, `2thess1-3-`, `1tim1-6-`, `2tim1-4-`, `titus1-3-`, `phlm1-stage2.md`, 111
corrections). Wikisource again prints the early wording (*favor* in every greeting and blessing, *Haereticum*, *in
corpore*), often with 1715, 1747 and 1750; 1758, 1681 and 1726–27 follow 1573.
- **1573's own changes against 1556** (recorded as variants; the text follows 1573): 1 Thess 3:11 *paterque* (1556
  *pater*), 4:8 *nos* (*uos*), 4:14 *in Christo obdormiverint* (*per Christum obdormiverunt*), 4:16 *cum … cum …
  cumque* (*in praeconio, in … voce, in[que]*), 5:2 *esse venturam* (*venturam esse*); 2 Thess 1:6 *sicut* (*ut*), 2:13
  *fidemque veritatis* (*verique fidem*); 1 Tim 1:5 *Enimvero* (*Atqui*), 2:4 *ad veritatis* (*ad veri*), **3:16
  *apparuit in carne*** (1556 *Deus extitit in corpore*; Wikisource, 1715, 1747, 1750 *apparuit in corpore*), 4:2
  *inustam* (*iniustam*); 2 Tim 3:10 *assequutus* (*affectatus*); Titus 1:16 *ad omne bonum opus* (*ad omnem rem
  bonam*). 1556 is cited from its OCR.
- **1573's misprints kept out**: 1 Thess 2:8 *ſic vos* (1556 and every other printing *sic nos*, as *fuerimus* and
  *vobis* require); 4:1 *igiturs, fratre*.
- **Verse numbers**: 1573 has no 1 Thess 3:11 (its 10 runs on into *Ipse Deus paterque*, so its 11–12 are the KJV's
  12–13); it numbers *Amen* as 1 Tim 6:17. It begins 1 Tim 1:4 at *neve fabulas*, Titus 3:6 at *quo nos*, and prints 1
  Thess 5:16, 17, 18 as the KJV, where Wikisource sets those words a verse off; the text follows the KJV.
- **Castellio's L. … G. marks** at 2 Tim 3:4 (*L. caeci et G. voluptatis*), in 1573 and 1556; 1758, 1715 and 1750 drop
  them. As at Matt 19:4, the marks go and the words stay.
- **Subscriptions** set in italics apart after each letter, as after the earlier epistles.

### Hebrews and James in 1573 against 1556 and Wikisource (stage 2, 2026-11-12)

Every place where Wikisource differs from 1573 was read on the 1573 page image (`data/review/heb1-7-stage2.md`,
`heb8-13-stage2.md`, `jas1-5-stage2.md`; 79 corrections). **In 1573 Hebrews stands after Jude** (canvases 929–937, the
last of the letters); James follows Philemon (canvases 916–919). Wikisource again prints the early wording, often with
1715, 1747 and 1750; 1758, 1681 and 1726–27 follow 1573.
- **1573's own changes against 1556** (recorded as variants; the text follows 1573; 1556 from its OCR): Heb 1:13 *ad
  dexteram meam* (*ad meam dexteram*), 2:18 *dum tentaretur, potest, qui tentantur subvenire* (*periclitando, potest
  periclitantibus*), 3:8, 3:15, 4:7 *indurare corda vestra* (*mentes obfirmare vestras*), 4:10 *in ejus requietem* (*in
  Dei requiete*), 5:6 *in aeternum* (*in perpetuum*), 5:7 *pro sua religione* (*pietate*), 7:2 *rex interpretatur*
  (*regem sonat*), 7:25 *adeunt* (*adeant*); *sanctuarium* for *sacrarium* at 9:1, 9:8, 9:12, 9:24 (twice), 9:25, 10:19,
  13:11, and 9:3 *quod sanctissimum sanctuarium appellatur, aureum habens thuribulum* (*quod sacrarium sanctius
  appellatur, auream habens aram suffitoriam*); 11:3 *ex non extantibus* (*ex ijs quae non extabant*, which 1573's own
  annotation still quotes); 11:23 *quod … veriti non fuerunt* (*qui … veriti non sint*); 12:1 *onere, ambitiosoque*
  (*fastu, tenacique*). Jas 1:4 *perfectum opus* (*perfectam actionem*), 2:13 *pietatem … pietas* (*misericordiam …
  misericordia*), 2:22 *adjuverit* (*adiuuaret*), 3:17 *pietate* (*misericordia*). Several of the Hebrews changes match
  the Clementine Vulgate (*obdurare corda vestra*, *qui tentantur*, *in aeternum*, *interpretatur rex justitiae*), yet
  1573 prints no *L.* … *G.* marks there: whether Castellio or Perna's editor made them cannot be told from the print.
- **1573's misprints kept out**: Heb 7:5 no *ducentes* (*qui à Leui genus ſacerdotium ineunt*, canvas 932; the clause
  needs it; 1556 and the early line have it, 1758 and 1726–27 follow 1573 without it); 11:4 *mortuis adhuc loquitur*
  (1556 and every other printing *mortuus*).
- **Verse numbers**: 1573 numbers Heb 7:28 at *Hoc enim semel fecit* (so its 7:29 is the KJV's 7:28) and 8:14 at *Quod
  autem antiquatur*; the KJV's numbering is kept (`data/versification/Heb.draft.edits.tsv`). Jas 4:11: 1573's verse 10
  runs on to *Nolite alius alii detrahere*, and neither 1573 nor 1556 has the early line's *Fratres* there.
- **Castellio's L. … G. marks** at Jas 5:3 (*L. Pœnam G. vobis congessistis*), in 1573, 1556 and 1681; 1758, 1715,
  1747, 1750 and 1726–27 drop them. As at Matt 19:4, the marks go and the word stays.
- **Subscription** after Hebrews: *Missa ex Italia per Timotheum.* in italics under 13:25.

### 1 Peter–Jude in 1573 against 1556 and Wikisource (stage 2, 2026-11-12)

Every place where Wikisource differs from 1573 was read on the 1573 page image (`data/review/1pet1-5-stage2.md`,
`2pet1-3-stage2.md`, `1john1-5-stage2.md`, `2john1-stage2.md`, `3john1-stage2.md`, `jude1-stage2.md`; 93 corrections).
1573 prints them after James and before Hebrews: 1 Peter on canvases 920–923, 2 Peter 923–924, 1 John 925–928, 2 and
3 John and Jude 928–929. Wikisource again prints the early wording, mostly with 1715, 1747 and 1750; 1758, 1681 and
1726–27 follow 1573. **1 John was revised for 1573 more than any letter so far**: *amor* for *caritas* through 4:7–18,
*quia* for *quod*, *corporatum* (4:2–3, 2 John 7), *credere in nomen* for *nomini fidem habere* (3:23, 5:10, 5:13).
- **1573's own changes against 1556** (recorded as variants; the text follows 1573; 1556 from its OCR, whose two
  columns run together on pages 10282446–47): 1 Pet 1:20 *Provisi* (*praecogniti*), 2:2 *alienum a fraude*
  (*infraudulentum*), 2:8 *inobedientes* (*diffidentes*), 3:6 *cujus factae estis filiae, dum bene facitis* (*ex qua vos
  procreatae, recte facite*), 3:20 *Qui olim non paruerant, quum semel* (*quibus olim persuasum non fuerat, cum*), 3:21
  *stipulatio* (*testificatio*), 5:5 *modestia ornamini* (*modestiam complectemini*), 5:9 *fide* (*fiducia*); 2 Pet 1:19
  *in cordibus vestris* (*in vestris animis*), 3:16 *Ut in* (*& in*); 1 John 2:4, 2:12–13 *quia* (*quod*), 3:4 *noxa*
  (*crimen*), 3:23, 4:9 *suum filium*, 4:10, 4:20 *qui possit amare* (*quo pacto potest amare*), 5:10, 5:13 (twice).
  Doubtful from the OCR alone: 1 Pet 1:2, 4:3, 4:11, 5:10; 2 Pet 2:5. 2 John, 3 John and Jude show none.
- **Shared by 1573 and 1556, against the Greek and the early line** (kept, as the base; for Nathan's eye): 1 John 4:4
  *qui in nobis* (ὁ ἐν ὑμῖν; Wikisource *vobis*); Jude 6 *ad magni Dei judicium* (μεγάλης ἡμέρας; Wikisource and the
  other printings *diei*); 1 Pet 5:8 *adversarius noster*; 1 Pet 1:4 *invietam* (for ἀμάραντον, apparently Castellio's
  word from *viētus*).
- **1 John 5:7–8, the Comma Johanneum**: 1573 prints the heavenly witnesses in parentheses, *( in cœlo, pater, sermo,
  & spiritus sanctus: & hi tres unum sunt. 8 Item tres sunt, qui testantur in terra )*, with the margin note *Hæc ( )
  in quibusdam exemplaribus non extant*; 1556 has the same words in square brackets, its note in pieces. 1758 and
  1726–27 keep the parentheses; Wikisource, 1747 and 1750 the words without them. The edition keeps the words and the
  parentheses, the only trace of Castellio's mark once the margin notes are gone.
- **Word order across verses**: at 2 Pet 1:17–18 1573, 1556 and 1758 put the voice's words (*hic est meus carissimus
  filius, in quo me oblecto*) after *in sacro monte* at the end of 18, where the Greek and the KJV have them in 17;
  the edition follows 1573 under the KJV's numbers. 1 Pet 1:24: *Aret herba, caditque flos* in 24, as 1573 and the KJV.
- **1573's misprint kept out**: 1 Pet 4:16 *aut si ut Christianus* (1758 copies it) for *At* (εἰ δέ).
- **Verse numbers**: 1573 numbers 3 John's greetings as verse 15; joined to 14, the KJV's
  (`data/versification/3John.draft.edits.tsv`).
- **Names**: 3 John 1 *Caio* in 1573 and 1556; the edition keeps *Gāius*, as settled. *Gomorra* (1573, Jude 7), as
  the settled Genesis (decision 46).

### Revelation in 1573 against 1556 and Wikisource (stage 2, 2026-11-12)

Every place where Wikisource differs from 1573 was read on the 1573 page image (`data/review/rev1-11-stage2.md`,
`rev12-22-stage2.md`; 74 corrections). In 1573, Revelation follows Hebrews on canvases 937–948. 1556's OCR has it on
pages 10282454–63. Wikisource prints the early wording throughout, mostly with 1715, 1747 and 1750; 1758, 1681 and
1726–27 follow 1573.
- **Wikisource's gaps**: Rev 3:1 is missing whole (its chapter 3 starts at verse 2), as are 7:5's *Ex Gaddi duodecim
  millia*, 5:11's *et decies centena millia* and 21:21's *unionibus singulae*. All of these are in 1573 and in 1556's
  OCR.
- **Castellio's revisions before 1556** (1556 agrees with 1573 against the early line): 1:4 *gratiam* (*favorem*); 1:13
  and 14:14 *hominis filio* (*homine nati*); 3:15 *qui* (*quod*); 8:10–11 *qua … delapsa: … conversa est*; 16:1
  *saevitiae Dei*; 20:6 *quin* (*quia*); 21:8 and 22:15 *deastricolas* (*divicolas*); 21:25 *illic* (*ibi*); 22:7
  *paret* (*pareat*); 22:11 *nocentior fiat … sanctior fiat* (*nocere pergat … sanctus esse pergat*).
- **1573's own changes against 1556** (recorded as variants; the text follows 1573):
  - 2:7 *arbore vitae* (*vitali*)
  - 2:10 *coronam vitae* (*vitae coronam*)
  - 2:13 *etiam iis temporibus, quibus Antipas* (*meisque temporibus Antipas*)
  - 11:19 *arca foederis in ejus templo* (*foederis ejus in ejus templo*)
  - 16:5 *sanctus* (*augustus*)
  - 19:8 *datum est … vestiri* (*mandatum est, ut … induatur*)
  - 20:4 *animas … eae* (*animos … Ii*)
  - 21:9 *cladum* (*cladium*)
  - 21:24 *gloriam suam* (*suam gloriam*)
  - Doubtful from one OCR reading: 5:10 *in terra* (1556 *in terris*).
- **Verse numbers**: 1573 (with Wikisource) puts the KJV's 10:2 inside 10:1, so chapter 10 has 10 verses; the verse is
  split at *Habebat autem*. Within the KJV's numbers, 1573 sets the boundaries of 10:2–3, 10:5–6, 19:6–7 and 21:10–11
  as the KJV does, and the edition follows it. It numbers against the KJV at 17:9–10, 20:9–10, 21:20–21 and 22:3–4,
  where the KJV's numbers are kept.
- **The book's frame in 1573**:
  - The title is *APOCALYPSIS IOHANNIS THEOLOGI, HOC EST, PATEFACTIO*.
  - Castellio's annotation follows the title. He says the author is doubted, and he confesses he barely understands
    "*vix millesimam partem*" of the book.
  - Athanasius's argument comes next.
  - At the end (canvas 948): *NOVI TESTAMENTI FINIS*, then a note to the reader beginning *Habes, Lector, quæ nos in
    præsentia potuimus*, which promises more and better if God wills, then *ERRATA SIC CORRIGITO* for the Old Testament.
  - 1556's OCR ends with its own *Novi Testamenti finis*. The *Habes, Lector* note was not found in it (pages
    10282460–79 searched).

### Genesis 1–27 in 1738, 1750 and Wikisource (collation of the settled text, 2026-11-12)

Nathan's settled Genesis 1–27 (his work before the pipeline) was collated against 1738, the Old Testament base, and
every place was read on 1738's archive.org page images (`data/review/settled-1738-gen1-13.md`, `settled-1738-gen14-27.md`).
- **Wikisource's Genesis appears to come from the archive.org (ABBYY) OCR of 1738.** At 13:15 it reads *tui*, the OCR's
  *tu* run into the margin verse number 15. At 9:3 it reads *concede*, as the OCR does, where the page has *concedo*.
  Its slips passed into the settled text: 4:8 *Cainum* (1738 *Cainus*), 5:22 *gentium* (*genitum*), 9:15 *facta*
  (*facti*), 13:15 *tui* (*tu*), 17:12 *es* (*ex*), 25:13 *Nabaiothua* (*Nabaiothus*), 27:33 a lost *&*.
- **1750 follows 1738 closely**: it shares every real reading in Genesis 1–27, including 1738's slip *Masina* at 25:14
  (1738's own 1 Chr 1:30 has *Masma*), and some of the same line breaks (*Masi-na*, *for-tunatus*, *con-sideto*). It is
  not a line-for-line reprint (only about a quarter of the hyphenated words are shared). So 1750 is weak independent
  support against 1738.
- **Castellio's marks in the Old Testament**: 1738 prints *G. lect. … H.* (1750 *Gr. lect. … Hebr.*) around readings
  from the Greek, e.g. Gen 21:9 *pepererat G. Isaaco filio suo H. illudentem*, the Septuagint's μετὰ Ἰσαὰκ τοῦ υἱοῦ
  αὐτῆς; the 1573 New Testament marks *L. … G.* in the same way.
- **1738's footnotes**: lettered glosses at the foot of the page (2:11–13 name the rivers *Ganges* and *Nilus*), not
  printed in the edition.

### Castellio's annotation on *rudentem* (Matt 19:24), seen in 1573

1573 prints Castellio's *Annotatio* after Matthew 19 (canvas 766, crop `sources/mdz-1573/crops/Matt.19.24-annotatio.jpg`).
He reads κάμηλος, not a variant. He says the word means both the animal and a ship's cable (*nauticum funem … qui
rudens appellatur*), which he says survives in French *cable*. He notes that Phavorinus would spell it with an iota in
the second syllable, and says that either way it must be taken in the sense that suits the saying, *ne Christum cogamus
hic ineptissima similitudine uti*. He separates hyperbole from absurdity, comparing the beam in the eye: a twig grows
into a beam, and a thread (*per foramen acus solet filum traiici*), however much it grows, never becomes a camel, but
it does become a rope. His rendering of Mark 10:25 and Luke 18:25 follows the same reading.

### Capitals for God in 1556

Searched in the e-rara OCR of the New Testament (`sources/erara-1556/`; long s reads as *f*), 2026-11-06. 1556 capitalizes only *Deus* and *Supremus* (*Supremi filius vocabitur*, *Supremi vis*, Luke 1:32, 35) and the title *Sanctus Dei* (Mark 1:24). Everything else is lower case: *a patre meo*, *pater vester coelestis*, *pater tuus*; *Dei filius*, *filio fidem habet*, *filius hominis*; *sancto spiritu*, *spiritum sanctum*. Any capitals this edition gives *Pater*, *Fīlius* or *Spīritus Sānctus* are therefore a modern editorial choice, not Castellio's.

### Names

Castellio spells Enoch *Henochus* in the Old Testament (Wikisource) but *Enochus* in the New (1556 *Enochi*, Luke 3:37; *Enochus*, Heb 11:5). This edition writes *Henōchus* in both (HUMAN.md decision 21). For Jericho he writes *Hierichus, -untis* in the Gospels (1556 *ad Hierichuntem*, Luke 10:30), where Wikisource's Gospels have *Hiericunt-*.

### A change after 1556: Luke 12:6

Castellio wrote *passerculi dipondio* (“two-penny sparrows”, Greek ἀσσαρίων δύο) in 1554 (MDZ page image 692) and 1556 (e-rara 10282355). The posthumous 1573 edition, “from his last revision”, reads *Cum væneant quinq; passerculi duobus assarijs* (MDZ bsb10141277, page image 801), and so do the later printings examined (1681, 1715, 1726–27, 1747, 1750, 1758). Wikisource has *dupondio*. Whether the change is Castellio's own last revision or Perna's editor's cannot be told from the print; the 1573 title claims his. All seen on the page images 2026-11-06. With 1573 as the base (decision 24), this edition keeps *duōbus assāriīs*; *dipondio* is recorded as 1556's variant.

### Words from the Latin marked *L.* … *G.*

In a few places Castellio prints words that follow the Latin (Vulgate) wording, set between an italic *L.* and *G.*: 1573 Matt 19:4 *qui principio fecit L. hominem, G. eos marem & fæminam* (canvas 765), Luke 10:1 *septuaginta L. duos, G. eosque binos* (799), 10:17 *septuaginta L. duo G. cum lætitia* (799), 11:7 *& tibi dare L. si ille pulsare perseuerauerit G.* (800, page image), John 5:4 *qui primus L. in piscinam G. descendebat* (817), Jas 5:3 *L. Pœnam G. vobis congessistis* (919). The marked words match the Clementine Vulgate where checked (Luke 10:1 *septuaginta duos*, 11:8 *si ille perseveraverit pulsans*, John 5:4 *in piscinam*, Matt 19:4 *hominem*). Castellio explains the system for the Old Testament in his *Ad lectores admonitio* (1573 canvas 16, OCR): what he found in the Greek or the old Latin translation of a book extant in Hebrew, and not in the Hebrew, he inserted, marking it *G* (Greek), *L* (Latin) or *G.L.* (both), *usque ad H.*, “which signifies the return to the Hebrew”. In the New Testament the same marks evidently set off words from the Latin (*L.*) until the return to the Greek (*G.*); that reading of the NT marks is an inference from the OT rule and the Vulgate matches. 1556 has the same marks at Luke 11:7 (OCR, e-rara 10282354), and so do 1750 (Luke 11:7) and 1758 (Luke 10:1, 10:17, 11:7); 1715 and 1747 omit the Luke 11:7 clause. Wikisource prints the marked words without the marks.

Found by the aligner on 2026-11-07 (it now records the marks as a flag; `data/witnesses/ocr-*/`): one more place, **Matt 8:18** *iussit L. discipulos G. traijcere* (1573 canvas 755, page image; 1758 OCR). Here the marked word is **not** the Clementine Vulgate's (*jussit ire trans fretum*, `sources/parallel/vulgate`), and the Greek has no word for it either (SBLGNT ἐκέλευσεν ἀπελθεῖν εἰς τὸ πέραν): so at this place *L.* does not mark the Vulgate's wording, which weakens the inference above. Which Latin Castellio followed here is not known. Marks also seen in the OCR of 1715 (Matt 19:4 *L, hominem G.*; Luke 10:1 *L. du-os G,*), 1681 (Luke 10:17) and 1556 (Matt 19:4 *L; hominem*). The OCRs read the marks as *L./I./J.* and *G./C.*; 1747 prints none of them where its OCR was read.

**The Old Testament marks in print** (seen 2026-11-08): 1738 Gen 44:6 *cur bonum malo pensarint? G. cur sibi scyphum argenteum furati sint? H. eum esse, quo suus herus potare …* (archive.org leaf 107: *G.* on the page image, *H.* in the OCR as *if.*). The marked question matches the words the Septuagint adds at Gen 44:5 (“why have you stolen my silver cup?”); that match is from memory of the Greek, not checked against a text here. Wikisource prints the marks; the 1726–27 text (`TXT/3`) omits them and keeps the words.

In Exodus (seen 2026-11-08, 1738 OCR): 2:22 *in terra extranea. G.L. Item alterum, quem Eliezerem nominavit …* (leaf 116; the second son, named here as in the Septuagint and Vulgate, where the Hebrew names him only at 18:4; no *H.* follows in the verse), and 6:20 *Aharonem et Mosem G.L. et Mariam eorum sororem, H. vixitque Amramus …* (leaves 119–120; “and Miriam their sister”). These are the *G.L.* (“both”) of the *admonitio*. Wikisource prints them; the 1726–27 text omits them and keeps the words.

**1738 prints footnotes with alternative renderings.** Exod 1:21 *pietatem ᶜ familias* has the footnote *c) progeniem.* at the foot of the page (leaf 115, page image), offering *progeniem* for *familias*; 1738's OCR runs the note into the text of 2:2. Wikisource, 1750 and the 1726–27 text print the text without the note. Whether the notes are Castellio's own was not checked.

### Castellio's own words, seen in 1573 (Matthew 14–28)

Read on the 1573 page images on 2026-11-07 (canvas numbers in `data/review/matt14-28-stage2.md`), where Wikisource and the draft have something else: Matt 19:24 *facilius esse rudentem per foramen acus traijci* (a ship's cable, reading κάμιλος for κάμηλος; 1750 and Wikisource agree), Matt 28:1 *Ea autem nocte septidui* (“of the week”; also 1747), Matt 22:35 *legisperitus* (νομικός), Matt 26:54 *quo pacto confierent*.

In the settled chapters (read on the 1573 page images on 2026-11-07; `data/review/settled-1573.md`): **John 2:18 is revised between 1556 and 1573.** 1556 has *Quod nobis exemplum praebes, qui ista facias?* (OCR; Wikisource the same); 1573 (canvas 815) and 1758, 1747, 1750, 1715 have *Ede nobis aliquod prodigium, quo intelligamus ista tibi licere* (“show us some sign, by which we may know that you may do these things”). Also Castellio's: Matt 4:16 *in tetræ noctis regione* (“in the region of dark night”), Matt 6:4, 6, 18 *qui occulta videt/cernit*, Matt 13:32 *olerum maximum*, Luke 6:12 *pernox orauit*, Luke 9:12 *diuersentur* (“lodge”), where Wikisource has *terrae*, *occulte*, *holus*, *per nox*, *divertantur*.

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
- **Acts–Revelation:** compared with 1556 by OCR (2026-11-06). Wikisource follows the early wording there. Acts was collated against 1573 by OCR on 2026-11-07 (`data/calibration/acts1573.md`): about 92 places where Wikisource has the early line with 1715/1747/1750 (*synagoga → collegium*, *templum → fanum*, *homine natus → filius hominis*, *lavari → baptizari*, *hic sermo → hæc oratio*) and about 62 where it stands alone. Read on the page images in stage 2 (2026-11-09): see “Acts in 1573 against the early wording” above.
- **Why the Leipzig printings (1745, 1750, 1760) went back to the early wording:** Bünemann's preface (1745) should say. Not yet read.
- **Printers and editors** of 1681, 1697, 1715, 1726–27 and 1758, from their title pages.
- **Purpose statements** in the prefaces: Castellio's own (1551 dedication, 1554 and 1556 prefaces), Bünemann's (1745), and Gesner's essay (1747). Not yet read.
