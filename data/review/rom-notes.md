# Romans: light notes and brackets

Built 2026-11-17 by the process in `nt-notes-process.md`, with the test and wording of `nt-notes-form.md` (decisions
1–3): "the modern editions" means SBLGNT and NA28, against the TR.

**Sources read:**
- `rom-notes-candidates.md` (`python -m pipeline notes Rom`): 51 apparatus units in 48 verses, 44 TR-alone readings.
- The whole of Romans, read verse by verse against the TR, SBLGNT, BSB, WEB, the Vulgate and 1573 as printed
  (`text/orig/ROM.usfm`) by two readers (chapters 1–8 and 9–16), with the SBLGNT apparatus for every unit. Each
  finding was checked here against the files.
- The NRSVue (Bible Gateway, read 2026-11-17), text and footnotes, for every verse below: in each it reads with the
  modern text against Castellio, and none of its footnotes gives his sense as an alternative ("Or …"), except where
  an item says so.
- For Castellio's own readings, the OCR of the later printings (12:11, 14:7, 8:35). 1556's OCR doesn't give these
  verses legibly.

Nothing from the NRSVue is copied here beyond a word or two. The existing bracket (16:24) and the doxology (16:25–27,
where NA28 prints it too) need nothing. No word of the edited text differs from 1573 in more than spelling.

## A. Notes where the Greek text differs (the modern editions against the TR)

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

1. **4:19** *nōn cōnsīderāvit suum corpus*: TR οὐ κατενόησε, "he did not consider his body"; the modern editions κατενόησεν without οὐ (NRSVue "He did not weaken in faith when he considered his own body"). The sense turns round: Abraham looked at the facts and still believed. The candidates file listed only ἤδη here.
   **Apply:** `Rom.4.19` la: `nōn cōnsīderāvit suum` → `nōn cōnsīderāvit\f + \fr 4:19 \ft Cōdicēs antīquiōrēs habent κατενόησεν sine οὐ, ‘cōnsīderāvit’.\f* suum`
2. **8:2** *līberāvit mē*: TR με; the modern editions σε, "set you free" (NRSVue, whose footnote gives "me or us" as other readings). A change of person, as at Luke 9:50.
   **Apply:** `Rom.8.2` la: `līberāvit mē ā` → `līberāvit mē\f + \fr 8:2 \ft Cōdicēs antīquiōrēs habent σε, ‘tē’.\f* ā`
3. **10:17** *ex dīvīnā ōrātiōne*: TR διὰ ῥήματος Θεοῦ; the modern editions ῥήματος Χριστοῦ (NRSVue "the word of Christ", footnote "other ancient authorities read *of God*").
   **Apply:** `Rom.10.17` la: `ex dīvīnā ōrātiōne.` → `ex dīvīnā ōrātiōne\f + \fr 10:17 \ft Cōdicēs antīquiōrēs habent ῥήματος Χριστοῦ, ‘Chrīstī ōrātiōne’.\f*.`
4. **14:10** *ad Chrīstī tribūnal*: TR τῷ βήματι τοῦ Χριστοῦ; the modern editions τοῦ θεοῦ (NRSVue "the judgment seat of God", footnote "of Christ").
   **Apply:** `Rom.14.10` la: `ad Chrīstī tribūnal adfutūrī` → `ad Chrīstī tribūnal\f + \fr 14:10 \ft Cōdicēs antīquiōrēs habent τῷ βήματι τοῦ θεοῦ, ‘ad Deī tribūnal’.\f* adfutūrī`
5. **15:29** *cum plēnā chrīstiānī euangeliī ūbertāte*: TR ἐν πληρώματι εὐλογίας τοῦ εὐαγγελίου τοῦ Χριστοῦ; the modern editions εὐλογίας Χριστοῦ, without the gospel (NRSVue "in the fullness of the blessing of Christ", footnote "add *of the gospel*"). Castellio leaves εὐλογίας untranslated, so a bracket on *euangeliī* would leave little; a note gives the Greek.
   **Apply:** `Rom.15.29` la: `euangeliī ūbertāte.` → `euangeliī ūbertāte\f + \fr 15:29 \ft Græcē ἐν πληρώματι εὐλογίας τοῦ εὐαγγελίου τοῦ Χριστοῦ; cōdicēs antīquiōrēs ἐν πληρώματι εὐλογίας Χριστοῦ, ‘in plēnitūdine benedictiōnis Chrīstī’.\f*.`
6. **16:5** *Achāiæ*: TR τῆς Ἀχαΐας; the modern editions τῆς Ἀσίας (NRSVue "the first convert in Asia"; the Vulgate *Asiæ*).
   **Apply:** `Rom.16.5` la: `est Achāiæ prīmitiæ` → `est Achāiæ\f + \fr 16:5 \ft Cōdicēs antīquiōrēs habent τῆς Ἀσίας, ‘Asiæ’.\f* prīmitiæ`

## B. Notes where Castellio's Latin says what the Greek does not

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

7. **8:35** *ab amōre Deī*: the Greek (TR and SBLGNT) ἀπὸ τῆς ἀγάπης τοῦ Χριστοῦ, "from the love of Christ" (NRSVue; the Vulgate *caritate Christi*). 1573 prints *ab amore Dei*, and 1750 the same; perhaps drawn from 8:39. Written as the slip notes are (1 John 4:4).
   **Apply:** `Rom.8.35` la: `ab amōre Deī?` → `ab amōre Deī\f + \fr 8:35 \ft Græcē τῆς ἀγάπης τοῦ Χριστοῦ, ‘ab amōre Chrīstī’; Castelliōnis ēditiōnēs ‘Deī’.\f*?`
8. **12:11** *temporī servientēs*: the Greek (TR and SBLGNT, NA28 too) τῷ κυρίῳ δουλεύοντες, "serve the Lord" (NRSVue, no footnote; the Vulgate *Domino servientes*). Castellio follows the reading καιρῷ, "the time", of a few manuscripts, as at Matt 13:35. *tempori seruientes* in 1573 (its index quotes "tempori seruire oportet Rom.12.11"), 1747 and 1750.
   **Apply:** `Rom.12.11` la: `temporī servientēs,` → `temporī servientēs\f + \fr 12:11 \ft Græcē τῷ κυρίῳ δουλεύοντες, ‘Dominō servientēs’.\f*,`
9. **14:7** *Nūllus enim vestrum*: the Greek (TR and SBLGNT) οὐδεὶς γὰρ ἡμῶν, "none of us" (NRSVue "we do not live to ourselves"), and 14:8 goes on in the first person. 1573 prints *vestrûm*, as do 1715, 1726, 1747 and 1758: Castellio's own slip.
   **Apply:** `Rom.14.7` la: `Nūllus enim vestrum sibi` → `Nūllus enim vestrum\f + \fr 14:7 \ft Græcē οὐδεὶς γὰρ ἡμῶν, ‘nūllus enim nostrum’; Castelliōnis ēditiōnēs ‘vestrum’.\f* sibi`

## C. Brackets: words the modern editions leave out

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

In each, the NRSVue lacks the words; where it has a footnote giving them, the item says so.

10. **1:16** *Chrīstī*: TR τὸ εὐαγγέλιον τοῦ Χριστοῦ. NRSVue "ashamed of the gospel".
    **Apply:** `Rom.1.16` la: `euangeliī Chrīstī:` → `euangeliī [Chrīstī]:`
11. **1:29** *stuprī*: TR πορνείᾳ.
    **Apply:** `Rom.1.29` la: `injūstitiæ, stuprī, perversitātis` → `injūstitiæ, [stuprī,] perversitātis`
12. **1:31** *perfidiōsī*: TR ἀσπόνδους. Castellio's five words match the TR's five in order, *perfidiōsī* in the fourth place, ἀσπόνδους (the Vulgate's *absque fœdere*). NRSVue "foolish, faithless, heartless, ruthless".
    **Apply:** `Rom.1.31` la: `inhūmānī, perfidiōsī, immisericordēs` → `inhūmānī, [perfidiōsī,] immisericordēs`
13. **6:11** *Dominum nostrum*: TR ἐν Χριστῷ Ἰησοῦ τῷ Κυρίῳ ἡμῶν. NRSVue "in Christ Jesus".
    **Apply:** `Rom.6.11` la: `Chrīstum Dominum nostrum.` → `Chrīstum [Dominum nostrum].`
14. **8:1** *nōn carnis, sed Spīritūs arbitriō pārent*: TR μὴ κατὰ σάρκα περιπατοῦσιν, ἀλλὰ κατὰ πνεῦμα (the words stand in 8:4 in all texts). NRSVue ends "in Christ Jesus".
    **Apply:** `Rom.8.1` la: `Jēsū, nōn carnis, sed Spīritūs arbitriō pārent.` → `Jēsū[, nōn carnis, sed Spīritūs arbitriō pārent].`
15. **8:26** *prō nōbīs*: TR ὑπὲρ ἡμῶν. NRSVue footnote "Other ancient authorities add *for us*". The candidates file had filtered it with the pronouns.
    **Apply:** `Rom.8.26` la: `Spīritus prō nōbīs supplicat` → `Spīritus [prō nōbīs] supplicat`
16. **9:28** *idque cum jūstitiā, rem, inquam, sevēram*: TR ἐν δικαιοσύνῃ· ὅτι λόγον συντετμημένον. NRSVue footnote gives the longer reading.
    The verse is set as two lines of verse, so the bracket opens on one and closes on the next.
    **Apply:** `Rom.9.28` la: `semel, idque cum jūstitiā,\qt*` → `semel[, idque cum jūstitiā,\qt*`
    **Apply:** `Rom.9.28` la: `\qt rem, inquam, sevēram faciet` → `\qt rem, inquam, sevēram] faciet`
17. **10:15** *nūntiantium pācem*: TR τῶν εὐαγγελιζομένων εἰρήνην. NRSVue "the feet of those who bring good news".
    **Apply:** `Rom.10.15` la: `pedēs nūntiantium pācem, nūntiantium bona` → `pedēs [nūntiantium pācem,] nūntiantium bona`
18. **11:6** *Sīn per opera, nōn jam est grātia: aliōquin opus nōn jam esset opus*: TR Εἰ δὲ ἐξ ἔργων, οὐκέτι ἐστὶ χάρις· ἐπεὶ τὸ ἔργον οὐκέτι ἐστὶν ἔργον. NRSVue footnote gives it.
    **Apply:** `Rom.11.6` la: `esset grātia. Sīn per opera, nōn jam est grātia: aliōquin opus nōn jam esset opus.` → `esset grātia. [Sīn per opera, nōn jam est grātia: aliōquin opus nōn jam esset opus.]`
19. **13:9** *nē falsum testātor*: TR οὐ ψευδομαρτυρήσεις; RP lacks it too (the TR alone). NRSVue lists four commandments, without false witness.
    **Apply:** `Rom.13.9` la: `nē falsum testātor, nē concupīscitō` → `[nē falsum testātor,] nē concupīscitō`
20. **14:6** *item quī diērum ratiōnem nōn habet, Dominō nōn habet*: TR καὶ ὁ μὴ φρονῶν τὴν ἡμέραν, Κυρίῳ οὐ φρονεῖ. NRSVue "Those who observe the day, observe it for the Lord. Also those who eat …".
    **Apply:** `Rom.14.6` la: `Dominō habet: item quī diērum ratiōnem nōn habet, Dominō nōn habet. Quī` → `Dominō habet[: item quī diērum ratiōnem nōn habet, Dominō nōn habet]. Quī`
21. **15:24** *adībō vōs*: TR ἐλεύσομαι πρὸς ὑμᾶς. In the modern text the sentence breaks off (NRSVue "when I go to Spain. For I do hope to see you").
    **Apply:** `Rom.15.24` la: `proficīscar, adībō vōs. Spērō` → `proficīscar, [adībō vōs.] Spērō`

## Considered and left out

**From the apparatus and the TR-alone list:**
- 2:17 *Ēn* (TR Ἴδε; the modern editions Εἰ δέ): the same point, put as a condition.
- 13:11, 15:7, 16:6: a change of person only.
- 14:4 *Deus* (the modern editions ὁ κύριος); 14:9 *resurrēxit ac*; 9:31 *jūstitiæ*; 15:15 *frātrēs*; 16:18 *Jēsū*: a word that changes nothing a reader needs.
- 4:19 *jam*, 5:1 ἔχομεν/ἔχωμεν, 8:11, 11:21, 14:12, 14:21, 15:19, 15:23, 16:7 (Junia), 16:20: SBLGNT and NA28 disagree, or NA28 keeps the TR's word.
- 7:6: Castellio's *eī mortuī* already agrees with the modern text.

**From the reading of each chapter:**
- 5:14 *in eōs, quī nōn peccāverant, rēgnāvit mors propter similitūdinem dēlictī Ādamī*: Castellio attaches ἐπὶ τῷ ὁμοιώματι to "reigned", so that the people "had not sinned" at all. The NRSVue reads "over those who did not sin in the likeness of Adam". It is a construal of an old theological crux rather than a different text, so it is left out.
- 15:18 *quam nihil nōn … effēcerit per mē Chrīstus*: a free turn of the double negative (NRSVue "I will not … speak of anything except what Christ has accomplished through me"); the praise of Christ's work is the same.
- 14:1 *nūllā cum animī dubitātiōne*: the Greek is ambiguous.
- 9:5: the punctuation (Christ as God) is contested among modern editors.
- 6:17, 7:21, 11:26, 11:33: older or ambiguous construals that the Greek allows.
- 2:4 *ad sānitātem*, 2:13 *īnsontēs*, 2:22 *deastrōs*, 1:25 *etiam* for ἀμήν: his vocabulary.
- 12:18 *potest(quantum*, a missing space, and 15:27 *Nam sī, extrāneī*, a comma 1573 doesn't print: layout, for the next spot check.
