# 1 Corinthians: light notes, brackets and corrections

Built 2026-11-17 by the process in `nt-notes-process.md`, with the test and wording of `nt-notes-form.md`: "the modern
editions" means SBLGNT and NA28, against the TR.

**Sources read:**
- `1cor-notes-candidates.md` (`python -m pipeline notes 1Cor`): 108 apparatus units in 86 verses, 44 TR-alone readings.
- The whole letter, read verse by verse against the TR, SBLGNT, BSB, WEB, the Vulgate and 1573 as printed
  (`text/orig/1CO.usfm`) by two readers (chapters 1–8 and 9–16), with every line of the SBLGNT apparatus. Each finding
  was checked here against the files.
- The NRSVue (Bible Gateway, read 2026-11-17) for every verse below: it reads with the modern text against Castellio,
  and none of its footnotes gives his sense as an alternative.
- For Castellio's own readings, the OCR of the later printings (6:14, 15:31).

## A. Notes where the Greek text differs (the modern editions against the TR)

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

1. **8:7** *opīnantēs esse deastrōs*: TR τῇ συνειδήσει τοῦ εἰδώλου, "with consciousness of the idol"; the modern editions τῇ συνηθείᾳ ἕως ἄρτι τοῦ εἰδώλου (NRSVue "so accustomed to idols until now").
   **Apply:** `1Cor.8.7` la: `opīnantēs esse deastrōs, tamen` → `opīnantēs esse deastrōs\f + \fr 8:7 \ft Cōdicēs antīquiōrēs habent τῇ συνηθείᾳ ἕως ἄρτι τοῦ εἰδώλου, ‘deastrōrum cōnsuētūdine’.\f*, tamen`
2. **9:20** *lēgī subditīs, ut lēgī subditus*: the modern editions add μὴ ὢν αὐτὸς ὑπὸ νόμον (NRSVue "though I myself am not under the law"). Missed by the candidates file.
   **Apply:** `1Cor.9.20` la: `lēgī subditīs, ut lēgī subditus, quō` → `lēgī subditīs, ut lēgī subditus\f + \fr 9:20 \ft Cōdicēs antīquiōrēs addunt μὴ ὢν αὐτὸς ὑπὸ νόμον, ‘cum ipse nōn sim lēgī subditus’.\f*, quō`
3. **14:38** *ignōrātō*: TR ἀγνοείτω, "let him be ignorant"; the modern editions ἀγνοεῖται (NRSVue "is not to be recognized"): a judgment, not a permission. Missed by the candidates file.
   **Apply:** `1Cor.14.38` la: `ignōrat, ignōrātō.` → `ignōrat, ignōrātō\f + \fr 14:38 \ft Cōdicēs antīquiōrēs habent ἀγνοεῖται, ‘ignōrātur’.\f*.`
4. **15:55** *ō orce*: TR ᾍδη, "Hades"; the modern editions θάνατε both times (NRSVue "Where, O death, … Where, O death").
   **Apply:** `1Cor.15.55` la: `ō orce, victōria?”` → `ō orce, victōria?”\f + \fr 15:55 \ft Cōdicēs antīquiōrēs habent ποῦ σου, θάνατε, τὸ νῖκος; ποῦ σου, θάνατε, τὸ κέντρον, ‘Ubi tua, ō mors, victōria? Ubi tuus, ō mors, stimulus?’\f*`

## B. Notes where Castellio's Latin says what the Greek does not

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

5. **6:14** *et vōs … suscitābit*: the Greek (TR and SBLGNT) καὶ ἡμᾶς ἐξεγερεῖ, "will also raise us" (NRSVue). 1573 prints *vos*, and so does 1750: Castellio's own slip, as at Rom 14:7.
   **Apply:** `1Cor.6.14` la: `et vōs per ejus potestātem` → `et vōs\f + \fr 6:14 \ft Græcē καὶ ἡμᾶς ἐξεγερεῖ, ‘et nōs’; Castelliōnis ēditiōnēs ‘vōs’.\f* per ejus potestātem`
6. **15:31** *glōriātiōnem nostram*: the Greek (TR and SBLGNT) νὴ τὴν ὑμετέραν καύχησιν, "by my boasting of you" (NRSVue; the Vulgate *per vestram gloriam*). *gloriationem nostram* in 1573, 1747 and 1750.
   **Apply:** `1Cor.15.31` la: `glōriātiōnem nostram jūrō` → `glōriātiōnem nostram\f + \fr 15:31 \ft Græcē νὴ τὴν ὑμετέραν καύχησιν, ‘per vestram glōriātiōnem’; Castelliōnis ēditiōnēs ‘nostram’.\f* jūrō`

## C. Brackets: words the modern editions leave out

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

In each, the NRSVue lacks the words; where it has a footnote giving them, the item says so. Items 18 and 19 are words no Greek has.

7. **3:3** *et dissidia*: TR καὶ διχοστασίαι. NRSVue footnote "Other ancient authorities add *and dissensions*".
   **Apply:** `1Cor.3.3` la: `æmulātiō et līs, et dissidia, nōnne` → `æmulātiō et līs, [et dissidia,] nōnne`
8. **5:1** *nōminātur*: TR ὀνομάζεται; the modern editions lack the verb (NRSVue "not found even among gentiles").
   **Apply:** `1Cor.5.1` la: `quidem nōminātur, ut` → `quidem [nōminātur], ut`
9. **5:7** *prō nōbīs*: TR ὑπὲρ ἡμῶν, as Rom 8:26. NRSVue "our paschal lamb, Christ, has been sacrificed".
   **Apply:** `1Cor.5.7` la: `pascha nostrum prō nōbīs immolātus` → `pascha nostrum [prō nōbīs] immolātus`
10. **6:20** *et animīs, quæ Deī sunt*: TR καὶ ἐν τῷ πνεύματι ὑμῶν, ἅτινά ἐστι τοῦ Θεοῦ. NRSVue "glorify God in your body".
    **Apply:** `1Cor.6.20` la: `corporibus et animīs, quæ Deī sunt.` → `corporibus [et animīs, quæ Deī sunt].`
11. **7:5** *jejūniō et*: TR τῇ νηστείᾳ καί. NRSVue footnote "Other ancient authorities read *fasting and prayer*".
    **Apply:** `1Cor.7.5` la: `ut jejūniō et precibus vacētis` → `ut [jejūniō et] precibus vacētis`
12. **9:18** *Chrīstī*: TR τὸ εὐαγγέλιον τοῦ Χριστοῦ, as Rom 1:16.
    **Apply:** `1Cor.9.18` la: `in Chrīstī euangelium` → `in [Chrīstī] euangelium`
13. **10:28** *Nam “Dominī et terra est, et omnia terrestria.”*: TR Τοῦ γὰρ Κυρίου ἡ γῆ καὶ τὸ πλήρωμα αὐτῆς, repeating 10:26.
    **Apply:** `1Cor.10.28` la: `cōnscientiam. Nam \qt “Dominī et terra est, et omnia terrestria.”\qt*` → `cōnscientiam. [Nam \qt “Dominī et terra est, et omnia terrestria.”\qt*]`
14. **11:24** *Sūmite, comedite* and *frangendum*: TR Λάβετε, φάγετε and τὸ ὑπὲρ ὑμῶν κλώμενον. NRSVue "This is my body that is for you", footnote "is broken for".
    **Apply:** `1Cor.11.24` la: `dīxit: “Sūmite, comedite: hoc meum` → `dīxit: “[Sūmite, comedite:] hoc meum`
    **Apply:** `1Cor.11.24` la: `prō vōbīs frangendum. Hoc` → `prō vōbīs [frangendum]. Hoc`
15. **11:29** *indignē* and *Dominī*: TR ἀναξίως and τὸ σῶμα τοῦ Κυρίου. NRSVue "without discerning the body", footnotes "in an unworthy manner" and "the Lord's body".
    **Apply:** `1Cor.11.29` la: `quī indignē comedit` → `quī [indignē] comedit`
    **Apply:** `1Cor.11.29` la: `dē Dominī corpore` → `dē [Dominī] corpore`
16. **16:22** *Jēsum Chrīstum*: TR τὸν Κύριον Ἰησοῦν Χριστόν. NRSVue "who has no love for the Lord".
    **Apply:** `1Cor.16.22` la: `Dominum Jēsum Chrīstum nōn amat` → `Dominum [Jēsum Chrīstum] nōn amat`
17. **16:24** *Āmēn*: TR ἀμήν. NRSVue footnote "Other ancient authorities add *Amen*".
    **Apply:** `1Cor.16.24` la: `omnibus adsit. Āmēn.` → `omnibus adsit. [Āmēn.]`
18. **15:47** *cælestis*: in no Greek. The TR has ὁ Κύριος ἐξ οὐρανοῦ, the modern editions ἐξ οὐρανοῦ (NRSVue "the second man is from heaven", footnote "add *the Lord*"). Castellio leaves out ὁ Κύριος, as the modern text does, and puts the Vulgate's *cælestis* in its place.
    **Apply:** `1Cor.15.47` la: `dē cælō cælestis.` → `dē cælō [cælestis].`
19. **16:15** *et Fortūnātī*: in no Greek (TR and SBLGNT τὴν οἰκίαν Στεφανᾶ; NRSVue "the household of Stephanas"). The Vulgate adds *et Fortunati, et Achaici* from 16:17; 1573 prints *Stephanæ et Fortunati familiam*.
    **Apply:** `1Cor.16.15` la: `Stephanæ et Fortūnātī familiam` → `Stephanæ [et Fortūnātī] familiam`

## D. Corrections to the edited text

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

20. **11:22** a question mark: *in hōc nōn laudō?* → *in hōc nōn laudō.*, as 1573 (*in hoc non laudo.*) and the Greek (NRSVue "In this matter I do not commend you!"). As it stands, Paul's refusal reads as a question.
    **Apply:** `1Cor.11.22` la: `in hōc nōn laudō?` → `in hōc nōn laudō.`
21. **9:2** a question mark: *sigillum estis in Dominō?* → *sigillum estis in Dominō.* 1573 prints a colon, and the Greek is a statement, introduced by *sīquidem*.
    **Apply:** `1Cor.9.2` la: `sigillum estis in Dominō?` → `sigillum estis in Dominō.`

## Considered and left out

- 2:4 *hūmānæ* and 7:39 *lēge*; 9:1 *Chrīstum*, 16:23 *Chrīstī*, 5:4–5 *Chrīstī*, *Jēsū*: a word that changes nothing a reader needs.
- 1:14, 2:1, 5:13, 6:11, 7:15, 13:3, 14:37: SBLGNT and NA28 disagree, or NA28 keeps the TR's word.
- 1:15, 1:23, 3:4, 7:3, 7:14, 7:17, 8:2, 10:20: no change of sense, or a change of person only.
- 4:7 *Quis enim dē tē jūdicātūrus est?* for τίς γάρ σε διακρίνει: διακρίνω bears "judge" as well as "distinguish" (NRSVue "who sees anything different in you?", with "Or …" a third rendering); the Greek is open.
- 4:15 *mīlle* for μυρίους: the Latin idiom for a great number.
- 12:27 *aliquātenus*, 15:44: shades.
- 7:34: Castellio already follows the modern verse division.
- 1:13, 6:6: punctuation, for the next spot check.
