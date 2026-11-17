# John: light notes, brackets and corrections

Built 2026-11-17 by the process in `nt-notes-process.md`, as for Mark, Matthew and Luke.

**Sources read:**
- `john-notes-candidates.md` (`python -m pipeline notes John`), with its new section for the TR alone.
- The whole of John, read verse by verse against the TR, SBLGNT, BSB and WEB by three readers (chapters 1–7, 8–14 and 15–21). Each of their findings was checked here against the files.
- The NRSVue (Bible Gateway), text and footnotes, for every verse below.
- The NET Bible's note for 4:36.
- 1573's page images for 6:49, 9:22, 18:28 and 19:38, and its OCR for 4:36.

Rewritten the same day to the test and wording of `nt-notes-form.md`: "the modern editions" means SBLGNT and NA28, and the notes use its formulas. In every item the NRSVue reads with the modern text against Castellio. The woman taken in adultery (7:53–8:11) and 5:3b–4 are already bracketed.

## A. Notes where the Greek text differs

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

1. **1:18** *ūnigena Fīlius*: TR ὁ μονογενὴς υἱός; the modern editions μονογενὴς θεός. NRSVue "the only Son, himself God", with a footnote giving the TR's reading.
   **Apply:** `John.1.18` la: `ūnigena Fīlius, quī` → `ūnigena Fīlius\f + \fr 1:18 \ft Cōdicēs antīquiōrēs habent μονογενὴς θεός, ‘ūnigena Deus’.\f*, quī`
2. **1:28** *Bēthabaræ*: TR ἐν Βηθαβαρᾷ; SBLGNT ἐν Βηθανίᾳ (NRSVue "in Bethany across the Jordan").
   - RP also reads Bethany, so the apparatus has no unit here.
   - The candidates file missed it twice: it had no TR-alone section, and it took the two names for forms of one word. Both are fixed.
   **Apply:** `John.1.28` la: `Hæc Bēthabaræ facta` → `Hæc Bēthabaræ\f + \fr 1:28 \ft Cōdicēs antīquiōrēs habent ἐν Βηθανίᾳ, ‘in Bēthaniā’.\f* facta`
3. **1:42** *Simōn Jōnæ fīlius*: TR Ἰωνᾶ; the modern editions Ἰωάννου, "Simon son of John" (NRSVue). At 21:15–17 the Latin already has *Jōhannide*.
   **Apply:** `John.1.42` la: `Simōn Jōnæ fīlius.` → `Simōn Jōnæ fīlius\f + \fr 1:42 \ft Cōdicēs antīquiōrēs habent Ἰωάννου, ‘Jōhannis’, ut et 21:15–17.\f*.`
4. **6:69** *tē esse Chrīstum vīventis Deī Fīlium*: TR ὁ Χριστὸς ὁ υἱὸς τοῦ Θεοῦ τοῦ ζῶντος; the modern editions ὁ ἅγιος τοῦ θεοῦ, "the Holy One of God" (NRSVue, with a footnote giving the TR's reading).
   **Apply:** `John.6.69` la: `vīventis Deī Fīlium.”` → `vīventis Deī Fīlium\f + \fr 6:69 \ft Cōdicēs antīquiōrēs habent ὁ ἅγιος τοῦ θεοῦ, ‘ille Deī sānctus’.\f*.”`
5. **9:4** *Mihi agenda sunt*: TR ἐμὲ δεῖ, "I must"; the modern editions ἡμᾶς δεῖ, "we must". NRSVue "We must", with footnotes giving "I" and "us".
   **Apply:** `John.9.4` la: `Mihi agenda sunt` → `Mihi\f + \fr 9:4 \ft Cōdicēs antīquiōrēs habent ἡμᾶς δεῖ, ‘nōs oportet’.\f* agenda sunt`
6. **9:35** *in Deī Fīlium*: TR τὸν υἱὸν τοῦ Θεοῦ; the modern editions τὸν υἱὸν τοῦ ἀνθρώπου. NRSVue "the Son of Man", with a footnote giving the TR's reading.
   **Apply:** `John.9.35` la: `in Deī Fīlium?”` → `in Deī Fīlium\f + \fr 9:35 \ft Cōdicēs antīquiōrēs habent τὸν υἱὸν τοῦ ἀνθρώπου, ‘in Fīlium Hominis’.\f*?”`
7. **11:50** *nōbīs*: TR ἡμῖν, "for us"; the modern editions ὑμῖν, "for you" (NRSVue). This is a change of person, as at Luke 9:50.
   **Apply:** `John.11.50` la: `condūcibilius esse nōbīs,` → `condūcibilius esse nōbīs\f + \fr 11:50 \ft Cōdicēs antīquiōrēs habent ὑμῖν, ‘vōbīs’.\f*,`
8. **12:7** *id ad meæ sepultūræ diem reservāvit*: TR τετήρηκεν, "she has kept it"; the modern editions ἵνα … τηρήσῃ, "so that she might keep it" (NRSVue).
   **Apply:** `John.12.7` la: `diem reservāvit,` → `diem reservāvit\f + \fr 12:7 \ft Cōdicēs antīquiōrēs habent ἵνα … τηρήσῃ, ‘ut … servet’.\f*,`
9. **12:47** *neque crēdiderit*: TR μὴ πιστεύσῃ, "does not believe"; the modern editions μὴ φυλάξῃ, "does not keep them" (NRSVue).
   **Apply:** `John.12.47` la: `neque crēdiderit,` → `neque crēdiderit\f + \fr 12:47 \ft Cōdicēs antīquiōrēs habent φυλάξῃ, ‘servāverit’.\f*,`
10. **7:8** *ego nōndum ad hoc fēstum ascendō*: TR οὔπω ἀναβαίνω, "I am not yet going up"; the modern editions οὐκ ἀναβαίνω, "I am not going up". NRSVue "I am not going to this festival", with a footnote "Other ancient authorities add *yet*".
    - Left out before because WH reads οὔπω; with the modern test (SBLGNT and NA28) it qualifies.
    - The note goes after *ascendō*, since *nōndum* comes first in the Latin.
    **Apply:** `John.7.8` la: `fēstum ascendō, quod` → `fēstum ascendō\f + \fr 7:8 \ft Cōdicēs antīquiōrēs habent οὐκ ἀναβαίνω, ‘nōn ascendō’.\f*, quod`

## B. Notes where Castellio's Latin says what the Greek does not

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

11. **4:36** *et sator frūgēs congerit*: Greek (TR and SBLGNT) ὁ θερίζων μισθὸν λαμβάνει καὶ συνάγει καρπόν. The reaper is the subject of both verbs: "the reaper is … receiving wages and is gathering fruit" (NRSVue).
    - Castellio gives the gathering to the sower. The Vulgate keeps the reaper (*qui metit … congregat fructum*).
    - The NET's note is on the wages only.
    - *sator fruges congerit* in 1556 (OCR *fator fruges*), 1573 (OCR *ſator fruges con-gerit*), 1715, 1747, 1750 and 1758.
    **Apply:** `John.4.36` la: `et sator frūgēs congerit` → `et sator\f + \fr 4:36 \ft Græcē ὁ θερίζων … συνάγει καρπόν, ‘messor … frūctum colligit’.\f* frūgēs congerit`
12. **18:28** *nē polluerentur*: Greek (TR and SBLGNT) goes on ἀλλ᾿ ἵνα φάγωσι τὸ Πάσχα, "and to be able to eat the Passover" (NRSVue); the Vulgate has it too.
    - Castellio leaves the clause out, and 1573 ends the verse at *ne polluerentur* (canvas 829, read on the page). 1556 does too (OCR *ne polluerentur, Itaque Pilatus*), and so does 1758.
    - Later editors filled it in: 1681, 1715, 1747 and 1750 read *ne polluerentur, sed vescerentur Pascha*. So the gap is Castellio's own, not one printing's.
    - The clause matters: it is how John dates the crucifixion against the Passover.
    **Apply:** `John.18.28` la: `nē polluerentur.` → `nē polluerentur\f + \fr 18:28 \ft Græcē sequitur ἀλλ᾿ ἵνα φάγωσι τὸ Πάσχα, ‘sed ut Pascha ēsse possent’.\f*.`
13. **19:38** *id quod permīsit Pīlātus*: Greek (TR and SBLGNT) goes on ἦλθεν οὖν καὶ ἦρε τὸ σῶμα, "so he came and removed his body" (NRSVue).
    - 1573 ends the verse at *id quod permiſit Pilatus* (canvas 830, read on the page); 1750 and 1758 go straight on to *Accessit et Nicodemus*. 1556's OCR doesn't give the verse.
    - The sense returns in 19:40 (*Hī Jēsū corpus cēpērunt*).
    **Apply:** `John.19.38` la: `permīsit Pīlātus.` → `permīsit Pīlātus\f + \fr 19:38 \ft Græcē sequitur ἦλθεν οὖν καὶ ἦρε τὸ σῶμα αὐτοῦ, ‘vēnit igitur et corpus ejus sustulit’.\f*.`

## C. Brackets: words the modern editions leave out

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

In each, the NRSVue lacks the words.

14. **1:27** *et ante mē fuit*: TR ὃς ἔμπροσθέν μου γέγονεν.
    **Apply:** `John.1.27` la: `venit, et ante mē fuit, cujus` → `venit, [et ante mē fuit,] cujus`
15. **3:13** *quī est in cælō*: TR ὁ ὢν ἐν τῷ οὐρανῷ. NRSVue footnote "who is in heaven".
    **Apply:** `John.3.13` la: `Hominis quī est in cælō.` → `Hominis [quī est in cælō].`
16. **3:15** *nōn pereat, sed*: TR μὴ ἀπόληται, ἀλλ᾿. NRSVue "may have eternal life". 3:16 has the same words in both texts.
    **Apply:** `John.3.15` la: `habeat, nōn pereat, sed vītam` → `habeat, [nōn pereat, sed] vītam`
17. **5:16** *et occīdere cōnābantur*: TR καὶ ἐζήτουν αὐτὸν ἀποκτεῖναι.
    **Apply:** `John.5.16` la: `Jūdæī, et occīdere cōnābantur, quod` → `Jūdæī, [et occīdere cōnābantur,] quod`
18. **6:11** *discipulīs: discipulī porrō*: TR τοῖς μαθηταῖς, οἱ δὲ μαθηταί. NRSVue "distributed them to those who were seated".
    **Apply:** `John.6.11` la: `distribuit discipulīs: discipulī porrō discumbentibus` → `distribuit [discipulīs: discipulī porrō] discumbentibus`
19. **6:22** *illam quam cōnscenderant ejus discipulī*: TR ἐκεῖνο εἰς ὃ ἐνέβησαν οἱ μαθηταὶ αὐτοῦ.
    **Apply:** `John.6.22` la: `ūnam illam quam cōnscenderant ejus discipulī,` → `ūnam [illam quam cōnscenderant ejus discipulī],`
20. **6:47** *in mē*: TR εἰς ἐμέ. NRSVue "whoever believes has eternal life". The candidates file had filtered the two words out as small words; the change is in what is believed.
    **Apply:** `John.6.47` la: `quī in mē crēdit` → `quī [in mē] crēdit`
21. **10:26** *quemadmodum vōbīs dīxī*: TR καθὼς εἶπον ὑμῖν.
    **Apply:** `John.10.26` la: `nōn estis, quemadmodum vōbīs dīxī.` → `nōn estis[, quemadmodum vōbīs dīxī].`
22. **11:41** *ubi situs erat mortuus*: TR οὗ ἦν ὁ τεθνηκὼς κείμενος.
    **Apply:** `John.11.41` la: `sustulērunt, ubi situs erat mortuus.` → `sustulērunt[, ubi situs erat mortuus].`
23. **16:16** *quoniam ego ad Patrem proficīscor*: TR ὅτι ἐγὼ ὑπάγω πρὸς τὸν πατέρα. In the critical text the disciples still quote the words back in 16:17.
    **Apply:** `John.16.16` la: `cernētis mē, quoniam ego ad Patrem proficīscor.”` → `cernētis mē[, quoniam ego ad Patrem proficīscor].”`

## D. Corrections to the edited text

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

Items 24 and 25 are slips that came in from Wikisource: 1573 prints the right text, and `text/orig/JHN.usfm` copied the slips too. For those, the same correction in `text/orig/JHN.usfm` would be made by hand on acceptance, as for Matthew 5:20.

24. **6:49** *mortuīs* → *mortuī*: Greek ἀπέθανον, "they died".
    - 1573 prints *tamen mortui ſunt* (canvas 819).
    - 1556, 1681, 1747 and 1758 have *mortui* (`data/calibration/nt1556.tsv` marks it "wikisource-slip"), and 6:58 has *mortuī sunt*.
    - In `text/orig/JHN.usfm`: *mortuis sunt* → *mortui sunt*.
    **Apply:** `John.6.49` la: `tamen mortuīs sunt.` → `tamen mortuī sunt.`
25. **9:22** words dropped from the verse:
    - 1573 prints *Iam enim conſpirauerant Iudæi, vt ſi quis eum Chriſtum eſſe confiteretur, is collegij communione priuaretur* (canvas 822, read on the page).
    - Wikisource, and so the settled text, lost *conſpirauerant Iudæi, vt ſi quis eum Chriſtum eſſe*, leaving *confiteretur* without a subject.
    - Greek: συνετέθειντο οἱ Ἰουδαῖοι ἵνα ἐάν τις αὐτὸν ὁμολογήσῃ Χριστόν (NRSVue "the Jews had already agreed that anyone who confessed Jesus to be the Messiah …").
    - Macrons: *cōnspīrāverant* (`pipeline latin macron`, Gaffiot *cōnspīrō*); *Jūdæī* and *Chrīstum* as elsewhere in the edition.
    - In `text/orig/JHN.usfm`: *Iam enim confiteretur,* → *Iam enim conspirauerant Iudæi, vt si quis eum Christum esse confiteretur,*.
    **Apply:** `John.9.22` la: `Jam enim cōnfitērētur,` → `Jam enim cōnspīrāverant Jūdæī, ut sī quis eum Chrīstum esse cōnfitērētur,`
26. **14:12** *eādem* → *eadem*: "will do the same things as I" (Greek τὰ ἔργα ἃ ἐγὼ ποιῶ κἀκεῖνος ποιήσει). The neuter plural object of *factūrum* is *eadem*; *eādem* is the ablative or the adverb.
    - The long ā came in with the Apply line at `data/review/john5-21-ch14.md:72`.
    - WordPress 2019 has *eadem*.
    **Apply:** `John.14.12` la: `eum esse eādem mēcum` → `eum esse eadem mēcum`

## Considered and left out

**From the apparatus and the TR-alone list:**
- 1:34 *Deī Fīlium*: SBLGNT has ὁ ἐκλεκτός (NRSVue "the Chosen One"), but NA28 reads υἱός, so it fails the consensus test.
- 7:50 *noctū*; 3:25 *Jūdæōs*; 6:71 *Iscariōtam*; 4:42 *Chrīstum*; 6:51, 6:58, 7:39, 7:46.
- 12:1 *quī mortuus fuerat*: the dead man is Lazarus either way, so nothing changes for the reader.
- 12:41 *tum cum* for "because": the NRSVue's own footnote gives "when".
- 17:12 *in mundō*; 13:2 *cēnā parātā*.
- The single-word entries.

**From the reading of each chapter.** In each, the Greek is contested, or the NRSVue gives his sense as an alternative:
- 1:3–4, 1:9, 1:15, 3:3: contested.
- 5:39 *Scrūtāminī*: contested.
- 8:25: contested.
- 12:27: contested.
- 15:27, 16:31, 18:37, 19:25: contested.
- 5:2 *oviāricam piscīnam*: the Vulgate's construal; the NRSVue footnote shows the place names vary.
- 7:35 *dispersās Græcōrum nātiōnēs*.
- 8:50 *cum ratiōne*.
- 18:38 the exclamation mark: 1573 prints it so.
- 21:7 *indūsium*.
