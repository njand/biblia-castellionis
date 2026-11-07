# Wording: your text against Wikisource

Proposed 2026-11-06 (decision 1: wording where your 1726–27 text and Wikisource differ is proposed, never changed
automatically). The 41 places are from `data/calibration/wikisource.tsv` (*wording*); Matt 4:18 (the stray *s*)
was settled in `spelling-fixes.md`. At each place the OCR witnesses were read in their aligned verse
(`data/witnesses/ocr-*`), and for the New Testament the 1556 OCR (`sources/erara-1556/`) was searched; it reads
poorly, so 1556 is cited only where the passage was found. Bases: OT 1738; NT 1556 when this was written
(decision 15), now 1573 (decision 24). Every NT place was then re-read in 1573 (2026-11-06; MDZ bsb10141277, hOCR
in `sources/mdz-1573/`, canvas numbers given; Luke 11:7 on the page image): the **1573:** notes. "All
printings" means every witness in which the passage could be read. WordPress is Wikisource with macrons, so it
is not cited.

Each **Apply** line is an exact replacement inside that verse of `text/<BOOK>.usfm`, checked to match once.

## A. Change your text: the printings agree against it (5)

**Decision:** accept (Nathan, 2026-11-06)  
**Applied:** 2026-11-06, to `text/*.usfm`

1. **Gen 7:14** *tum ālātum* → *tum ālitum* (of the birds, from *āles*). 1738, 1750 and Wikisource: *alitum*.
   **Apply:** `Gen.7.14` la: `tum ālātum,` → `tum ālitum,`
2. **Mark 2:7** *Quis fit, ut* → *Qui fit, ut* (“how is it that”). 1747, 1758, Wikisource: *Qui fit*; 1556 not
   found. Your *Quis* is probably carried over from the next sentence (*Quis potest ignōscere*).
   **1573:** *Qui fit, vt hic ita loquatur impiè?* (canvas 776): as applied.
   **Apply:** `Mark.2.7` la: `“Quis fit, ut` → `“Qui fit, ut`
3. **Mark 4:19** *cupiditātēsque sermōnem* → *cupiditātēs, quæ sermōnem*. 1556 (*cupiditates, quæ ser-*), 1715,
   1747, 1750, 1758, Wikisource: all *cupiditates, quae*.
   **1573:** *cupiditates, quæ sermo-* (canvas 777): as applied.
   **Apply:** `Mark.4.19` la: `cupiditātēsque sermōnem` → `cupiditātēs, quæ sermōnem`
4. **Mark 5:7** *“Quod tibi mēcum* → *“Quid tibi mēcum*. 1681, 1715, 1726, 1747, 1750, 1758, Wikisource: all
   *Quid*; 1556 not found.
   **1573:** *Quid tibi mecum* (canvas 778): as applied.
   **Apply:** `Mark.5.7` la: `“Quod tibi` → `“Quid tibi`
5. **Luke 5:39** *pōtō vetere* → *pōtātō vetere* (“having drunk the old”). 1750, 1758, Wikisource: *potato*.
   **1573:** *potato vetere* (canvas 794). Reverted to *pōtō* afterwards: see item 8.
   **Decision:** reverted by item 8 (Nathan, 2026-11-06); this item-level line keeps `review apply` from re-applying it
   **Apply:** `Luke.5.39` la: `quisquam pōtō vetere` → `quisquam pōtātō vetere`

## B. Your call (2)

6. **Gen 11:25** *centum ūndēvīgintī*: 1738 (the OT base) and 1750 read *novemdecim*, as Wikisource. But
   *novemdecim* is barely Latin: one hit in the corpus (Sigebert, medieval), against *ūndēvīgintī* in Cicero,
   Livy and Augustus. Keep your *ūndēvīgintī* under decision 18 (1st-century-BC usage), or restore 1738?
   **Decision:** keep *ūndēvīgintī* (Nathan, 2026-11-06); not applied
   **Apply** (only if you restore 1738): `Gen.11.25` la: `centum ūndēvīgintī` → `centum novemdecim`
7. **Mark 5:38** *magistrī collēgī*: 1556 (*collegii*), 1758 and Wikisource read *collegii*, and your text has
   *collēgiī* seven times elsewhere. Republican prose prefers the contracted genitive (*cōnsilī* 147 : *cōnsiliī*
   89, *imperī* 132 : *imperiī* 76; *collēgī* 8 : 3, though *collēgī* is also “I collected”). Make it *collēgiī*
   like the rest (recommended), or adopt the contracted *-ī* genitive throughout? The second would be a new rule
   reaching every *-ius/-ium* noun (*fīliī* → *fīlī*), so it would come back as its own proposal.
   **Decision:** *collēgiī* (Nathan, 2026-11-06)  
   **Applied:** 2026-11-06
   **Apply** (for *collēgiī*): `Mark.5.38` la: `magistrī collēgī,` → `magistrī collēgiī,`
   **1573:** *in ædes magistri collegij* (canvas 778): as applied.

## C. Keep your text (33; Luke 12:6 moved to D, Luke 11:7–8 reopened as item 10): Wikisource's slip, or a reading no printing has

**Decision:** keep all (Nathan, 2026-11-06)

| Place | Wikisource | Yours (kept) | Evidence |
|---|---|---|---|
| Gen 2:2 | *opera* | *opere* | 1726, 1738, 1750 *opere* |
| Gen 4:11 | (none) | *apertō* | 1750 *aperto*; 1738 not readable here |
| Gen 4:14 | *extortis* | *extorris* | 1738, 1750 |
| Gen 6:5 | *hominum num vitia* | *hominum vitia* | 1726, 1738, 1750 have no *num* |
| Gen 9:1 | *Nox* | *Nōæ* | 1750 *Noae*; 1738's OCR reads *Nox* too: æ misread as x |
| Gen 9:3 | *concede* | *concēdō* | 1750 |
| Gen 19:20 | *hic a propinquum* | *hīc propinquum* | 1726, 1750 |
| Gen 20:13 | *abstraherer* | *abstraheret* | 1726, 1738, 1750 |
| Gen 22:2 | *tuum a unicum* | *tuum ūnicum* | 1750 |
| Gen 24:51 | *Jova;* | *Jōvæ* | 1726 *Jovæ*, 1750 *Iouae* |
| Gen 24:53 | *profers* | *prōfert* | 1726, 1750 |
| Gen 25:9 | *Ephroni* | *Ephrōnis* | 1726, 1750 (1738 *Ephroni 9*: the verse number may sit in the word) |
| Gen 25:11 | *Abraham* | *Abrāhāmō* | 1726, 1738, 1750 |
| Gen 25:15, 25:16 | *&* | *et* | the ampersand only |
| Matt 5:10 | *eorum et* | *eōrum est* | 1556, 1715, 1750, 1758; **1573:** *eorum est* (752) |
| Mark 1:42 | *discesserunt … leprae* | *discessit … lepra* | 1681, 1715, 1747, 1750, 1758; **1573:** *discessit ab illo lepra* (776) |
| Mark 3:25 | *dissident* | *dissīdet* | 1681, 1715, 1747, 1750, 1758; **1573:** *domus secum ipsa dissidet* (777) |
| Luke 2:11 | *qui Christus* | *quī est Chrīstus* | 1715, 1747, 1750, 1758 (1726 lacks *est*); **1573:** *qui est Christus Dominus* (791) |
| Luke 2:14 | *Gloriam supremis* | *Glōria in suprēmīs* | 1715, 1747, 1750, 1758; **1573:** *Gloria in supremis* (791) |
| Luke 2:30 | *salute* | *salūtem* | 1681, 1715, 1726, 1747, 1750, 1758; **1573:** *salutem tuam* (791) |
| Luke 3:5 | *aspera viae* | *asperæ viæ* | 1681, 1747, 1750, 1758 (1715 *aspera*); **1573:** *asperæ viæ* (792) |
| Luke 3:8 | *neu* | *nēve* | the printings have *neu*, but these are one word; *nēve* 72 : *neu* 49 in republican prose (decision 18); **1573:** *neu velitis* (792), as the printings; your *nēve* is the spelling choice |
| Luke 6:11 | *Jesus* | *Jēsū* | 1556, 1681, 1715, 1726, 1747, 1750, 1758; **1573:** *quid Iesu facerent* (794) |
| Luke 9:23 | *quid* | *quis* | 1747, 1750, 1758; **1573:** *Si quis post me* (798) |
| Luke 11:7–8 | *… et tibi dare si ille pulsare perseveraverit* | (no clause) | ~~in no printing (1681, 1715, 1750, 1758)~~ **Wrong:** the aligner dropped it. **1573** (canvas 800, page image), 1556 (OCR), 1750 and 1758 print the clause, marked *L.* … *G.*; 1715 and 1747 omit it. Back for review as item 10 |
| Luke 12:11 | *potestasque* | *potestātēsque* | 1681, 1715, 1726, 1747, 1750, 1758; **1573:** *potestatesque* (801) |
| Luke 13:32 | *illis* | *ille* | 1715, 1747, 1750, 1758; **1573:** *Quibus ille: Ite, inquit* (803) |
| John 1:36 | *Ecce conspicatus* | *et cōnspicātus* | 1681, 1715, 1726, 1747, 1750, 1758; **1573:** *& conspicatus ambulantem Iesum* (814) |
| John 3:2 | *sic allocutus* | *sīc est allocūtus* | 1681, 1715, 1747, 1750 (1758 lacks *est*); **1573:** *eum sic est allocutus* (815) |
| John 3:20 | *ne in lucem* | *nec in lūcem* | 1681, 1715, 1747, 1750, 1758; **1573:** *nec in lucem prodit* (816) |
| John 4:29 | *fortassis* | *fortasse* | the printings have *fortassis*; one word, and *fortasse* 446 : *fortassis* 0 in republican prose (decision 18); **1573:** *fortassis* (817), as the printings; your *fortasse* is the spelling choice |

## D. Reconsidered after the decision (2026-11-06)

Two places were looked at again at Nathan's request, as spelling or vocabulary choices under decision 18
(1st-century-BC prose) rather than as readings. Luke 5:39 *pōtātō* is already applied (group A, item 5), so
restoring *pōtō* is a new change.

8. **Luke 5:39 *pōtātō vetere* → back to *pōtō vetere*.** Gaffiot gives the verb as *pōtō, āvī, ātum* and has
   *pōtus, a, um* as its own headword: the short participle. In the corpus (`latin attest`), the ablative
   participle *pōtō* is classical: Cicero, *Brutus* 333, *excepisse sanguinem paterā et eō pōtō mortuum
   concidisse* (the same construction as *pōtō vetere*); Seneca twice (*venēnō pōtō*); Martial; and Varro lists
   *pōtus sum* beside *cēnātus sum* and *prānsus sum*. *pōtātō* has one hit, Neo-Latin (Laurentius Corvinus);
   *pōtātus* is post-Augustan apart from Cicero's *gustāta quam pōtāta* (Tusc.). So your *pōtō* was the classical
   form; the printings' *potato* is the later one. Recommended: restore *pōtō*.
   **Decision:** restore *pōtō* (Nathan, 2026-11-06)  
   **Applied:** 2026-11-06
   **Apply:** `Luke.5.39` la: `quisquam pōtātō vetere` → `quisquam pōtō vetere`
   **1573:** *Neq; verò quisquã potato vetere* (canvas 794), as the later printings. Nothing new: the decision
   already chose the classical *pōtō* over the printings' *potato*.
9. **Luke 12:6 *duōbus assāriīs* or *dupondiō*** (moved here from group C). **Castellio's own editions read
   *dipondio*.** 1554 (MDZ bsb10196330, page image 692): *Cum uæneant quinq; passerculi dipondio, tamen eorum
   nullus in obliuione est apud Deū*. 1556 (e-rara 10282355, page image; its OCR reads *dípondío*): *uæneant
   quinq; passerculi dipondio, tam[en eo]rum nullus in obliuione est apud Deum*. But the posthumous 1573 edition,
   “from his last revision” (MDZ bsb10141277, page image 801), reads *Cum væneant quinq; passerculi duobus
   assarijs*, and the later printings follow it (1681, 1715, 1726, 1747, 1750, 1758). So *duobus assariis* is
   either Castellio's own last change or his posthumous editor's; the print cannot say which. Wikisource has
   *dupondio* (1551, 1745 and 1760 not checked here). Greek ἀσσαρίων δύο. Spelling, by decision 18: Gaffiot has the headword *dŭpondĭus,
   ĭī* (with *dipondius* as a form of it); republican prose has *dupondius* (Cicero, *Prō Quīnctiō*; Varro six
   times), *dipondius* only from Seneca and Petronius on. So Castellio's word, in the classical spelling, is
   *dupondiō*. With 1556 as the base (decision 15): *dupondiō*. If 1573 becomes the base: *duōbus assāriīs*.
   **Decision:** keep *duōbus assāriīs*, the 1573 reading (Nathan, 2026-11-06; decision 24 makes 1573 the NT base).
   Nothing to apply; 1556's *dipondio* is recorded as a variant.
   **1573:** *duobus assarijs* (canvas 801, page image).
   **Apply** (only for *dupondiō*; not applied): `Luke.12.6` la: `passerculī duōbus assāriīs,` → `passerculī dupondiō,`

## E. Found in the 1573 check (2026-11-06)

10. **Luke 11:7 add *sī ille pulsāre persevērāverit*** (“if he keeps on knocking”). Moved here from group C, where
    the clause was judged to be in no printing; that was the aligner dropping it. On the 1573 page image (canvas 800,
    lines of verses 7–8): *non possum surgere, & tibi dare L. si ille pulsare perseuerauerit G. 8 mihi credite, etsi
    non surget*. 1556 (e-rara 10282354, OCR): *& ti bi dare L..(i ille pulfare perfeuerauerít Gi. míhí ctedite*.
    1758 (archive.org OCR): *tibi dare L. ſi ille pulſare perſeveraverit G. 8Mihi credite*; 1750 the same, with the
    marks. 1715 and 1747 end the verse at *tibi dare*; 1681 not found here. Wikisource has the clause without the
    marks. The marked words follow the Latin: the Clementine Vulgate has *Et si ille perseveraverit pulsans* (11:8).
    Castellio's *Ad lectores admonitio* (1573 canvas 16) explains such marks for the Old Testament: additions from
    the Greek or Latin, marked *G* or *L*, *usque ad H.* (the return to the Hebrew); here *L.* … *G.* presumably
    marks words from the Latin until the return to the Greek (`docs/editions.md`, “Words from the Latin marked”).
    **Your text elsewhere keeps such words:** Luke 10:1 *septuāgintā duōs* and 10:17 *septuāgintā duo* are marked
    the same way in 1573 (*septuaginta L. duos, G.*, canvas 799) and are in your text without the marks.
    Recommended, with 1573 as the base (decision 24) and for consistency with Luke 10: add the clause, unmarked, as
    in Luke 10. The clause belongs to the sentence that verse 8 finishes (*if he keeps knocking, believe me, …*), so
    it goes after the friend's closing quote, and verse 8's *Mihi* takes a small *m* (1573 *mihi credite*).
    Macrons: Gaffiot *pulsō, āre* and *persĕvērō, āre* (`latin macron`). Whether to print the *L.* … *G.* marks
    (or brackets) anywhere is a separate edition-wide choice; your text has none so far.
    Alternative: keep your text, without the words Castellio marks as the Latin's (as 1715 and 1747 print it).
    **Decision:** add the clause, unmarked (Nathan, 2026-11-07)  
    **Applied:** 2026-11-07, to `text/LUK.usfm`
    **Apply:** `Luke.11.7` la: `et tibi dare.’` → `et tibi dare.’ Sī ille pulsāre persevērāverit,`
    **Apply:** `Luke.11.8` la: `Mihi crēdite, etsī` → `mihi crēdite, etsī`
