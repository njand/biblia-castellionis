# Page images for stage 2 (M1 step 5)

Checked 2026-11-06.

## The 1760 New Testament on Google Books (FsdIAAAAcAAJ)

**The page images can be fetched.**
- **Access:** the book is in full view. The viewer's JSON (`books?id=FsdIAAAAcAAJ&pg=<pid>&jscmd=click3`) lists 502 page ids (PP1–PP10 front matter, PA1–PA482, PT1–PT6). Each request returns signed image URLs for about five pages near `pg`.
- **Resolution:** the image at `zoom=3` is 575 px wide. Adding `&w=1600` to the signed URL gives a 1380 × 2500 JPEG, about 500 KB per page, which reads cleanly. Changing `zoom` to 4 or 5 gives an "image not available" placeholder.
- **Coverage:** we fetched seven pages (PP3, PP7 title page, PA1, PA150, PA200, PA330, PA482); all came back. The title page reads *Novum Iesu Christi Testamentum Latinum … denuo evulgatum*, Lipsiae, Breitkopf, CIↃ IↃCC LX: the 1760 edition.
- **Limits:**
  - Google gives no OCR text or word boxes, so word crops would need our own page coordinates.
  - The Books API returned 429 (rate-limited) without a key.
  - The page has a *Download PDF* link; it was not downloaded.

**But Wikisource's Gospels do not follow this edition.** Wikisource's index page names this scan as its New Testament source. Comparing four 1760 pages with Wikisource and the archive.org OCRs:

| Verse | 1760 (page image) | Wikisource | Others |
|---|---|---|---|
| Matt 2:17 | *quod fuerat a Ieremia vate ita dictum* | *quod a Jeremia vate ita dictum fuerat* | 1681, 1715, 1747, 1750, 1758, your text: as Wikisource |
| Matt 2:11 | *tus et myrrham* | *thus, murram* | 1681 *thus & myrrham*; your text *thūs, murram* |
| Luke 18:43 | *Deo laudem tribuit* | *Deo tribuit laudem* | 1758 as Wikisource; 1715, 1750 as 1760 |
| Luke 19:9 | *Tum Iesus ei dixit* | *ei dicit* | 1758 *dicit*; 1750 *dixit* |
| Luke 19:10 | *Venisse enim hominem natum* | *filium hominis* | 1758 as Wikisource |
| Luke 19:7 | *diuersatum iuisset* | *deversatum isset* | 1758 *diversatum ivisset* (Wikisource's own slip) |
| John 13:17 | *Si haec nostis* | *Si hoc nostis* | 1758 as Wikisource |
| John 13:26 | *Cui Iesus respondet* | *respondit* | (not found in the other OCRs) |
| John 13:31 | *nunc homine natus* | *Nunc filius hominis* | |
| 1 Cor 15:37–55 | same wording as Wikisource | (*omnia caro* and *refurgetur* are Wikisource slips) | |

The clearest marker is "Son of man". Counting in the raw OCR:

| Text | *filius hominis* | *homine natus* |
|---|---:|---:|
| 1681 | 37 | 2 |
| 1758 vol. 1 | 67 | 0 |
| Wikisource Gospels | 78 | 0 |
| Your Gospels (1726–27) | 52 | 0 |
| 1715 | 0 | 61 |
| 1747 | 0 | 68 |
| 1750 | 0 | 81 |
| 1760 (four pages read) | 0 | 2 (Luke 19:10, John 13:31) |

So there are two textual families. Wikisource's Gospels, 1758, 1681 and your 1726–27 text form one; 1715, 1747, 1750 and the 1760 scan form the other. On the one Epistle page checked, the two agree. Wikisource's Gospels must come from a "filius hominis" text, not from the scan it cites. This bears on decision 1 ("1760 NT" as the base edition).

### The split is in the Gospels only

Ten 1760 pages were read and transcribed: 2,493 words across nine books. Each was compared word by word with Wikisource. Spelling was set aside (*quum/cum*, *ad-/as-*, *intelligo*, *ocyus*, *sumsit*, *seipsum*, *sescenta*), and so were differences of word division.

| Pages | Words | Wording differs | What the differences are |
|---|---:|---:|---|
| Gospels (Matt 2, 20; Mark 12; Luke 18–19; John 13) | 1,276 | 15 readings | **Edition differences** (below), in all four Gospels |
| Acts 15, Rom 6, 1 Cor 15, Titus 1, Rev 14 | 1,217 | 7 | **All Wikisource slips** against 1760: *apostlis*, *sum* (for *sub*), *omnia* (for *omnis*), *cogitionem*, *terrae* (for *terra*), *patre* omitted (Titus 1:4); in Luke 19:8 the same kind of slip, *facultatem* |

Gospel readings where 1760 differs from Wikisource (1758, checked in its OCR where found, sides with Wikisource every time):
- Matt 2:11 *tus et myrrham* / *thus, murram*.
- Matt 2:13: 1760 adds *et*.
- Matt 2:17: word order.
- Matt 20:19 *exteris* / *externis*: 1758 and 1715 read *externis*.
- Matt 20:28 *homine natus* / *filius hominis*.
- Mark 12:37 *unde fit eius* / *unde fit ut sit ejus*: 1758 reads *ut sit*. The verse division of 12:37–38 also differs.
- Mark 12:39 *synagogis* / *collegiis*: 1758 and 1681 read *collegiis*; 1715 reads *Synagogis*.
- Mark 12:44: 1760 adds *ex*, and misprints *penuaria*.
- Luke 18:43, 19:7, 19:9, 19:10 and John 13:17, 13:26: as in the first table.

**Conclusion:**
- From Acts to Revelation, Wikisource follows 1760, as it says. It differs from 1760 only by its own slips, about 0.5% of words. There the 1760 page images are the right ones for stage 2.
- In the Gospels, Wikisource follows the *filius hominis* text (as do 1758, 1681 and your 1726–27). It differs from 1760 in about 1.2% of words. In those books 1758 is the matching page image, and 1760's readings are variants.

### Castellio's own text (1551)

The first edition (Basel, Oporinus 1551; Google Books BrlIAAAAcAAJ, full view) was checked by an in-book search and one page image (Matthew 12, second pagination p. 19).
- It reads *homine natus*: in Matt 12:8, 12:32 and 12:40 on that page, and in 10 search hits across pp. 19–95.
- It has no *filius hominis* phrase. The 10 hits for that search are scattered words in the Old Testament.
- Matt 12:9 has *in eorum collegium* (synagogue).

So neither 18th-century family is simply Castellio's 1551 text:
- 1760 keeps his *homine natus* but has *synagogis* at Mark 12:39.
- 1758, Wikisource and the 1726–27 text keep *collegiis* but have *filius hominis*.

Castellio's last revision (Basel, Perna 1573, *ex postrema recognitione*), which the later title pages invoke, has not been checked. A scan appears to be at the Elbląg library (dlibra, DjVu), not yet opened.

### The whole New Testament against 1556 (2026-11-06)

**Method** (`scripts/collate_1556.py`):
- The e-rara OCR of 1556 (pages 10282300–10282529, cached in `sources/erara-1556/`) was aligned word by word with Wikisource, book by book. So were the 1758, 1681, 1747 and 1750 OCRs.
- The 1556 OCR is poor: it finds 27–69% of Wikisource's words, and only 80–88% of those it finds read the same. Most single disagreements are therefore OCR noise.
- A difference is counted only when **another printing reads as 1556 does**:
  - *edition*: the printings split;
  - *wikisource-slip*: every printing found agrees against Wikisource.
- Spelling habits (*caussa/causa*, *adflatus/afflatus*, *quemdam/quendam*, *numquam/nunquam*, *caritas/charitas*, …) are set aside.
- All 487 remaining differences are in `data/calibration/nt1556.tsv`; per-book counts are in `nt1556-books.tsv`.

**The telling pattern** is 1556 + 1758 (the revised line) against Wikisource + 1750 (the Leipzig line):

| | Wording differences in that pattern | Examples |
|---|---:|---|
| Gospels | 3 | (Wikisource already follows the 1556 line) |
| Acts–Revelation | 79 (about 45 real wording, the rest spelling the filter missed). The OCR finds ~55% of words, so the true number is roughly double | *favor → gratia* (Eph 6:24, Phil 1:2, 1 Thess 5:28, 2 Thess 3:18, Phlm 25, Rev 22:21); *humanitatem → carnem* (Rom 9:5, 9:8, 1 Cor 10:18; Col 3:22 *corpus → carnem*); *synagogis/synagogas → collegiis/collegia* (Acts 13:5, 15:21, 26:11); *baptismo lavit → baptismate baptizavit* (Acts 19:4); *faustitatem → felicitatem* (Heb 12:17); *scripturarum → literarum* (Rom 15:4); *sermo → oratio* (Acts 6:5); *angelis → angelos* (Heb 2:16) |

**Seen on the page image:** 1556 Acts 19:4 and 19:8 (e-rara 10282393) read *Iohannes quidem corrigendae vitae baptismate baptizavit … Ille ingressus in collegium*. Wikisource has *baptismo lavit … in synagogam*.

**Castellio's 1554 text** (MDZ OCR search) has the Leipzig/Wikisource wording in the Epistles:
- *Domini nostri Iesu Christi favor*;
- *quod ad humanitatem attinet* (Rom 9:5, 1 Cor 1:26, 10:18);
- *faustitatem* (Heb 12:17).

So in Acts–Revelation, Wikisource (with 1760 and 1750) prints Castellio's **early** wording. The 1556 revision replaced it with *gratia*, *caro*, *felicitas* and so on. It is the same pattern as in the Gospels, where Wikisource happens to follow the revised line.

**For stage 2:** with 1556 as the base (decision 15), Acts–Revelation will carry a steady stream of "1556 reading" proposals: perhaps 80–100 words. The Gospels will carry few. *(Decision 24 then made 1573 the base; 1573 keeps these revised readings, so the stream of proposals in Acts–Revelation stands, now as "1573 reading" proposals.)*

### Other editions found online (checked 2026-11-06)

| Edition | Where | Notes |
|---|---|---|
| 1551 Basel, Oporinus (first edition) | Google Books BrlIAAAAcAAJ; e-rara (UB Bern, UB Basel) | *homine natus*, *collegium* (see above) |
| 1554 Basel, Oporinus, "totum opus recognovit ipse" | MDZ (BSB Res/2 B.lat. 92, searchable full text); Google Books kpp_lc3BtOMC | Castellio's own revision |
| 1556 Basel, Oporinus | e-rara (UB Basel FG II 41) | The last edition in Castellio's lifetime |
| 1573 Basel, Perna, *postrema recognitione* | **No full scan found.** Elbląg's DjVu has only 18 pages (binding and a few leaves). Not on e-rara, MDZ or archive.org; a Google search was blocked by a CAPTCHA | Held in print at Berlin, Hamburg, Wolfenbüttel and Princeton |
| 1728 Leipzig, Walther (4 vols.) | MDZ (SuStB Augsburg Th B V 102) | |
| **1745 Leipzig, Fuchs, ed. J. L. Bünemann** | Halle ULB (opendata.uni-halle.de, handle 1981185920/56262), public domain, IIIF, 1,431 images | Title: *versionem et adnotationes ex primis editionibus emendavit*. Restores Castellio's text from the early editions and adds an index of his Latinity. Matt 24:27 and 24:30 read *homine nati*. |
| 1750 Leipzig, Breitkopf | Halle ULB (handle 1981185920/65566) and archive.org (already a witness) | |

### The Gospel differences in Castellio's own text (1554) and in Bünemann (1745)

The sources for each reading:
- **1554:** MDZ's OCR (bsb10196330, page OCR via api.digitale-sammlungen.de, images 645–790).
- **Bünemann 1745:** the Halle page images, read by eye: NT pp. 4, 25, 54, 88, 116, 117.
- **1760:** the transcribed pages above.
- **Wikisource:** its text; 1758 agrees with Wikisource wherever it was checked.

| Verse | 1554 (Castellio) | Bünemann 1745 | 1760 | Wikisource / 1758 |
|---|---|---|---|---|
| Matt 2:11 | *thus, & myrrham* | *… et myrrham* | *tus et myrrham* | *thus, murram* |
| Matt 2:13 | *& assumpto* | *et adsumto* | *et assumto* | *assumpto* (no *et*) |
| Matt 2:17 | *quod à Ieremia uate ita dictum fuerat* | same | *quod fuerat a Ieremia vate ita dictum* | as 1554 |
| Matt 20:19 | *tradent externis* | *externis* | *exteris* | *externis* |
| Matt 20:28 | *homine natus* | *homine natus* | *homine natus* | *filius hominis* |
| Mark 12:37 | *unde fit ut sit eius* | *ut sit* | *unde fit eius* | *ut sit* |
| Mark 12:39 | *in collegijs* | ***in synagogis*** | *in synagogis* | *in collegiis* |
| Mark 12:44 | *at hæc … sua penuria* (no *ex*) | ***at hæc ex*** | *ex* | no *ex* |
| Luke 18:43 | *Deo laudem tribuit* | *laudem tribuit* | *laudem tribuit* | *tribuit laudem* |
| Luke 19:7 | *diuersatū iuisset* | *diu[ersatum]* | *diversatum ivisset* | *deversatum isset* (Wikisource slip; 1758 *diversatum ivisset*) |
| Luke 19:9 | *Tum Iesus ei dicit* | ***dixit*** | *dixit* | *dicit* |
| Luke 19:10 | *homine natum* | *homine na[tum]* | *hominem natum* | *filium hominis* |
| John 13:17 | *Si hæc nostis* | *Si hæc* | *haec* | *hoc* |
| John 13:26 | *Cui Iesus respondet* | *respondet* | *respondet* | *respondit* |
| John 13:31 | *Nunc homine natus* | *homine natus* | *homine natus* | *filius hominis* |

Whole-book counts in the 1554 Gospels OCR: *homine nat-* 70, *filius hominis* 0, *collegi-* 52, *synagog-* 0.

How often each text agrees with Castellio's 1554 at these 15 places:

| Text | Agrees | Where it differs |
|---|---:|---|
| Bünemann 1745 | 12 of 15 | Mark 12:39 *synagogis*, Mark 12:44 *ex*, Luke 19:9 *dixit*: all three as in 1760 |
| 1760 | 9 of 15 | The same three, plus three of its own: Matt 2:17 word order, Matt 20:19 *exteris*, Mark 12:37 *ut sit* omitted |
| Wikisource / 1758 | 6 of 15 | *filius hominis* ×3, *tribuit laudem*, *hoc*, *respondit*, *murram*, missing *et*, plus the slip *deversatum isset* |

### Castellio's last revision in his lifetime (1556) reverses the picture

1556 Basel, Oporinus, e-rara 10281656 (UB Basel FG II 41).

**Sources:**
- e-rara's OCR (`/bau_1/download/fulltext/plain/<page id>`), pages 10282300–10282419.
- Luke 19:9 and 19:10 were also read on the page image (10282360).

**Whole-Gospels counts in the OCR:** *filius hominis* 47 and *homine natus* 0; *collegi-* 53 and *synagog-* 0. Matt 12:8 reads "Sabbathi quoque dominus filius hominis", where 1551 has *homine natus*.

| Verse | 1556 | Same as |
|---|---|---|
| Matt 2:11 | *thus, & myrrham* | 1554 |
| Matt 2:13 | *& assumpto* | 1554, 1745, 1760 |
| Matt 2:17 | *quod a Ieremia uate ita dictum fuerat* | Wikisource, 1554 |
| Matt 20:19 | *tradent externis* | Wikisource, 1554 |
| Matt 20:28 | *filius hominis non uenit* | **Wikisource** |
| Mark 12:37 | *unde fit ut sit eius* | Wikisource, 1554 |
| Mark 12:39 | *in collegiis primas* | Wikisource, 1554 |
| Mark 12:44 | *at hæc sua penuria* (no *ex*) | Wikisource, 1554 |
| Luke 18:43 | *Deo laudem tribuit* | 1554, 1745, 1760 |
| Luke 19:9 | *Tum Iesus ei dicit* (image) | Wikisource, 1554 |
| Luke 19:10 | *uenisse enim filium hominis* (image) | **Wikisource** |
| John 13:17 | *Si hoc nostis* | **Wikisource** |
| John 13:26 | *Iesus respondet* | 1554, 1745, 1760 |
| John 13:31 | *Nunc filius hominis illustratur* | **Wikisource** |

Agreement with 1556 at these 14 places (Luke 19:7 is left out as a Wikisource slip):

| Text | Agrees with 1556 | Where it differs |
|---|---:|---|
| **Wikisource / 1758** | **10 of 14** | *murram*, no *et* (2:13), *tribuit laudem*, *respondit* |
| 1554 | 10 of 14 | *homine natus* ×3, *haec* |
| Bünemann 1745 | 7 of 14 | |
| 1760 | 4 of 14 | |

**Reading of the evidence:**
- *Homine natus* is Castellio's **early** wording (1551, 1554). By 1556 he had changed it to *filius hominis*, and made the other changes in the 1556 column.
- The *filius hominis* line follows his **later** text: 1681, 1726–27, 1758, Wikisource's Gospels, and your finished chapters.
- Bünemann says he corrected the text "from the first editions", so he deliberately went back to the early readings, and 1760 sides with him.
- The three readings Bünemann and 1760 share against both 1554 and 1556 (*synagogis*, *ex*, *dixit*) appear in neither of Castellio's editions checked here. Their source (1573? a Leipzig editor?) is unknown.

## The 1758 New Testament on archive.org (stand-in)

**Confirmed usable.**
- Two volumes, 276 + 358 leaves at 800 ppi.
- Each has hOCR word boxes (11.0 and 13.7 MB), `_djvu.txt` and page numbers.
- **Single pages without the 1–1.8 GB `_jp2.zip`:**
  - `archive.org/download/<id>/page/n<leaf>.jpg` gives a 4251 × 7626 JPEG (2.2 MB);
  - `…/page/n<leaf>_w1400.jpg` gives a scaled one (650 KB).

  The IIIF endpoint returned 404.
- **As a witness:**
  - It is the best-scoring OCR witness (98.2% found, 96.6% reading agreement, `witnesses.md`).
  - It is in the same textual family as Wikisource's Gospels.
  - It is the closer image for checking a Wikisource reading.
  - It has the word boxes that stage 2's crops need.

## The 1573 Basel edition (Perna, *postrema recognitione*), found 2026-11-06

- **Where:** MDZ bsb10141277 (BSB 2 B.lat. 112), full view, with searchable OCR. Found through USTC 616558, which
  also lists an ÖNB digital copy (BE.1.G.6, `data.onb.ac.at/ABO/+Z165385104`) and 41 copies in all; VD16 B 2638.
  Folio: [16] pp., 1,446 + 404 columns, [64] pp.
- **Access:** the IIIF content search `api.digitale-sammlungen.de/iiif/services/search/v1/bsb10141277?q=<word>`
  returns each hit's canvas, box and context (paged by `&page=N`); the page images are at
  `api.digitale-sammlungen.de/iiif/image/v2/bsb10141277_<00801>/<x,y,w,h>/800,/0/default.jpg`. The same works
  for 1554 (bsb10196330). From this machine the shell's `curl` fails on TLS to MDZ; the web-fetch tool and the
  browser pane work.
- **Verse numbers** are printed (e.g. Luke 12:6–7), unlike 1556: alignment will be easier.
- **Text line:** the 1556 one. As 1556: *filius hominis* throughout the Gospels (John 13:31 *Nunc filius hominis
  illustratur*, canvas 826), Acts 19:4 *corrigendæ vitæ baptismate baptizavit* (canvas 847), Mark 12:44 *at hæc
  sua penuria* (no *ex*, canvas 785), Matt 2:11 *aurum, thus, & myrrham* (canvas 750). Unlike 1556: Luke 12:6
  *duobus assarijs* for 1556's *dipondio* (canvas 801, page image).
- **Collation with 1556** (2026-11-06, `scripts/collate_1573.py`; every difference in `nt1573.tsv`, per book in
  `nt1573-books.tsv`). Both OCRs were aligned to Wikisource with the five archive.org printings. 1573's OCR finds
  89–98% of the words in each book (1556's: 27–69%), and reads 92–94% of them as Wikisource does (OCR noise
  included). Both editions were found at about 64,000 of the NT's words; they read alike at 81–86% of them, nearly
  all of the rest being OCR noise in one or the other.
- **1573 revises 1556.** Keeping only differences of three letters or more where 1758 or 1681 reads as 1573 and
  another text as 1556, about 30 word changes remain. In every one, 1556 reads with the early-line printings
  (1715, 1747, 1750) and, in Acts–Revelation, with Wikisource; 1573 reads with 1758 and often 1681. Since 1556's OCR
  covers only about half the text, the true number is perhaps twice that, plus Luke 12:6 (*dipondio* →
  *duobus assarijs*), which the filter misses. Examples:

  | Place | 1556 | 1573 (= 1758) |
  |---|---|---|
  | Matt 6:22–23 | *fuerit* | *erit* |
  | Mark 6:6 | *incredulitatem* | *infidentiam* |
  | Mark 13:5 | *infit* | *loquitur* |
  | Mark 14:21 | *vadit* | *abit* |
  | Luke 2:41 | *festo* | *festis* |
  | Luke 6:49 | *dat* | *trahit* |
  | Luke 7:16 | *se* | *ipsos* |
  | Luke 9:54 | *etiam* | *et* |
  | John 14:30 | *orbis* | *mundi* |
  | John 21:5 | *pulmentarii* | *edulii* |
  | Gal 5:6 | *agens* | *operans* |
  | Eph 4:18 | *torporem* | *duritiem* |
  | 1 Tim 1:5 | *Atqui* | *Enimvero* |
  | 1 Tim 2:4 | *veri* | *veritatis* |
  | 1 Tim 3:16 | *corpore* | *carne* |
  | Heb 5:7 | *pietate* | *religione* |
  | Heb 7:2 | *iustitiæ regem sonat* | *iustitiæ rex interpretatur* |
  | Heb 9:8 | *sacrarii* | *sanctuarii* |
  | Jas 1:4 | *actionem* | *opus* |
  | 1 Pet 3:21 | *testificatio* | *stipulatio* |
  | 1 John 3:4 | *crimen* | *noxa* |
  | Rev 16:5 | *augustus* | *sanctus* |
  | Rev 19:8 | *induatur* | *vestiri* |

  Heb 7:2 was read on the 1573 page image (canvas 932) and in the 1556 OCR (e-rara 10282450), which is clear here.
- **What follows:** 1573 is the source of the "revised line". 1681, 1726–27 (your finished chapters: *erit*,
  *festis*, *ipsos*, *et*, *duobus assariis*) and 1758 print it, and so do Wikisource's Gospels; Wikisource's
  Acts–Revelation follow the early line instead. The changes run the way Castellio's own 1556 revision did, from
  classical words toward the received ones (*carne*, *sanctuarium*, *sanctus*, *opus*), which fits the title's
  claim that this is his last revision; the print alone cannot prove whose they are.
- **Decided (2026-11-06, HUMAN.md decision 24):** 1573 is the New Testament base in place of 1556. 1556 stays
  the reference, its readings where 1573 differs recorded as variants. 1573's own hOCR word boxes and IIIF images
  serve for crops (e.g. Luke 11:7, canvas 800, region 380,960,1300,320); 1758 is the second image.
