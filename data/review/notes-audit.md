# Every footnote, audited: length, need, consistency and Latin

Proposed 2026-11-18 (Claude); accepted and applied the same day, at Nathan's request ("a complete audit of every footnote … turning this from a fun side
project into a legitimate professional edition", and "be on the lookout for awkward or unnatural Latin phrasing").
Each Apply line below has been checked to match its verse exactly once.

## What was read

All 169 notes in `text/*.usfm`: 15 in the Old Testament (Genesis 5, Exodus 5, Leviticus 4, Numbers 1) and 154 in the
New. By opening: 113 *Cōdicēs antīquiōrēs …*, 41 *Græcē …*, 13 *Hebraicē …*, and 2 on Castellio's coined words. Each
was read in its verse (the words before the caller), its Latin checked with `latin macron-check` (no macron errors
in the notes as they stand; the words it doesn't know are Castellio's coinages and æ spellings), and its form
compared with the formulas decided on 2026-11-17 (`nt-notes-form.md` §3).

**How professional Bibles do it.** The NRSVue and ESV have a few fixed formulas, defined once in the preface, and
never vary them. A note quotes only the words that differ, gives their sense, and stops. They don't give reasons,
say who holds a view, or add cross-references (those go in a separate apparatus, if there is one). The Old Testament
formulas match the New: "Heb" (what the Hebrew says), "Meaning of Heb uncertain", "Cn" (a correction of the
consonants), and a source tag such as "Gk", "Vg" or "Syr" when a version supports a reading. Critical editions in
Latin (the Stuttgart Vulgate, the Oxford texts) are terser still. The test for every note below is the same: is it one
of the formulas, does it quote only what differs, and is every word needed?

## The verdict in brief

- **The 113 *Cōdicēs antīquiōrēs* notes are in good shape**: uniform, short (median under 100 characters), and in the
  NRSVue's manner. Eight need small fixes (items 18–26).
- **The Old Testament notes don't match the New.** They are sentences with reasons (*ratus*, *putat*, *quia*), modern
  opinions introduced with *hodiē* (the word dropped from the NT for misleading readers), and one spelling error
  (*caelitēs* for Gaffiot's *cælitēs*, Gen 6:2). Proposal: the NT's short form (decision A).
- **One fact is written two ways.** Eleven notes on a slip in Castellio's text end *Castelliōnis ēditiōnēs ‘…’*; nine
  others of the same kind (Mark 12:29 *vester*, Mark 15:16 *extrā*, 1 Pet 5:2 *Chrīstī* …) don't. Exodus 40:20 still
  has the *habent* that the NT dropped (decision B).
- **Five notes explain what the text already shows** (*Castelliō Jōhannem intellegit* after *vīdit Jōhannēs*), and
  two fall outside what the front matter says the notes are for: a cross-reference (Matt 13:35) and an
  arithmetic gloss (Mark 12:42) (decisions C and D).
- **Small inconsistencies**: three ways of citing another verse (*v. 37*, *in 5:9*, *(23:16)*), two elision marks in
  the Greek, a gloss placed after the wrong word (Rom 4:19), and a few awkward Latin phrasings (items 16–26).

---

## A. The Old Testament notes in the New Testament's form

The OT notes kept their sentences on 2026-11-17 (`nt-notes-settled.md`: "they give Castellio's reasons from his 1554
annotations and need sentences"). This reverses that. Castellio's reasons are worth having, but they are commentary,
and the front matter already says the edition leaves out his annotations. They stay in `gen-exod-notes-1554.md`,
`lev-notes-1554.md` and `num-notes-1554.md` for anyone who wants them, and could go in a separate appendix later.

The formulas, as in the NRSVue:

| Formula | Use | NRSVue |
|---|---|---|
| *Hebraicē* Hebrew, ‘Latin’. | the text renders it otherwise | Heb |
| *…; Castelliō* Hebrew, ‘Latin’, *legit.* | he read other consonants | Cn |
| *…, ut Vulgāta* / *Castelliō Jōsēphum sequitur.* | an ancient source for his reading | Vg, Gk |
| *vōx obscūra* / *locus obscūrus* | the Hebrew's sense is uncertain | Meaning of Heb uncertain |
| *Castelliō fīnxit* | a word he coined (A2) | (none) |

*Ut Vulgāta*, not *ut Hierōnymus*: the reader can check the Vulgate, and the front matter names it.

**Decision A:** accept all / accept with changes / keep the OT notes as they are: accepted (2026-11-18), recorded under A1 and A2

### A1. Readings (items 1–12)

**Decision:** accept (Nathan, 2026-11-18: "Apply the audit as recommended")

1. **Gen 4:23**: the reason (*præteritum prō conjūnctīvō positum ratus …*) goes. Castellio's conditional
   (*Sī quem … interficerem*) shows his reading against ‘nam virum occīdī’.
   **Apply:** `Gen.4.23` la: `הָרַגְתִּי, ‘nam virum occīdī’; Castelliō, præteritum prō conjūnctīvō positum ratus, Lamēchum nōn suum facinus nārrāre, sed in ūniversum loquī intellegit.` → `הָרַגְתִּי, ‘nam virum occīdī’.`
2. **Gen 6:2**: *quōs hodiē multī caelitēs intellegunt* goes (*hodiē*; the modern view is itself disputed: angels,
   kings or Sethites). It also misspells *cælitēs*. The rest is a clause with no verb (*Castelliō … ratus, hominēs
   præstantēs*). The text's *hominum potentissimī* shows his reading.
   **Apply:** `Gen.6.2` la: `‘fīliī Deī’, quōs hodiē multī caelitēs intellegunt; Castelliō, ‘fīliōs’ prō adjectīvō positōs ratus, hominēs præstantēs.` → `‘fīliī Deī’.`
3. **Gen 49:6**: *ut Hierōnymus* moves to the end as the source tag.
   **Apply:** `Gen.49.6` la: `Castelliō, ut Hierōnymus, שׁוּר, ‘mūrum’, legit.` → `Castelliō שׁוּר, ‘mūrum’, legit, ut Vulgāta.`
4. **Gen 49:10**: *quam hodiē aliī ‘cujus est’ … legunt* uses *legunt* where it means "interpret", and lists modern
   views. *Ā שלה ductam sospitālem … intellegit* has no noun for *ductam* to agree with, and *sospitālem* doesn't match
   the text's *Sospitātor*. *Id est Chrīstum* is commentary. *Vōx obscūra* is the NRSVue's "meaning uncertain".
   (שילה stays unpointed: so the WLC prints it, ketiv.)
   **Apply:** `Gen.49.10` la: `vōx obscūra, quam hodiē aliī ‘cujus est’, aliī ‘tribūtum eī’ legunt; Castelliō ā שלה ductam sospitālem, id est Chrīstum, intellegit.` → `vōx obscūra.`
5. **Exod 19:23**: the reason goes. *Populus terminārī jubētur* is also loose: the people are bounded off; they are
   not bounded.
   **Apply:** `Exod.19.23` la: `Castelliō, quia 19:12 populus terminārī jubētur, הָעָם` → `Castelliō הָעָם`
6. **Exod 25:5**: *quæ cariem numquam sentit* is commentary, and *Græcī ξύλα ἄσηπτα* says "the Greeks" (a people) for
   the Septuagint. The word recurs about 25 times in Exodus 25–38 (*cedrinus* each time), so the note says *hīc et
   passim*.
   **Apply:** `Exod.25.5` la: `Hebraicē עֲצֵי שִׁטִּים, ‘ligna acaciæ’; Castelliō cedrum intellegit, quæ cariem numquam sentit (Græcī ξύλα ἄσηπτα).` → `Hebraicē hīc et passim עֲצֵי שִׁטִּים, ‘ligna acaciæ’.`
7. **Exod 30:24**: 30 words of reasoning, with *Psalmō 45* (ablative, no *in*, no verse). The source tag is enough;
   the text's *Īris* shows the reading.
   **Apply:** `Exod.30.24` la: `‘casia’; Castelliō, quod casiam Hebraicē קְצִיעוֹת vocārī putat (Psalmō 45), Jōsēphum sequitur, quī īrim nōminat.` → `‘casia’; Castelliō Jōsēphum sequitur.`
8. **Lev 13:48**: the reason goes. *Partem exteriōrem et interiōrem vertit* ("he translated outer and inner part") is
   unclear Latin, and the text says it already.
   **Apply:** `Lev.13.48` la: `‘in stāmine aut subtēmine’; Castelliō, ratus alterum sine alterō nōn maculārī, partem exteriōrem et interiōrem vertit.` → `‘in stāmine aut subtēmine’.`
9. **Lev 21:4**: the modern view (*hodiē*) and *litterā trānspositā* go. The two Hebrew forms show the transposition.
   **Apply:** `Lev.21.4` la: `locus obscūrus, quem plērīque hodiē dē affīnibus accipiunt; Castelliō litterā trānspositā בבעל עמיו legit, ut Hierōnymus.` → `locus obscūrus; Castelliō בבעל עמיו legit, ut Vulgāta.`
10. **Lev 23:40**: as Exodus 30:24.
    **Apply:** `Lev.23.40` la: `Castelliō Jōsēphum sequitur, quī perseæ pōmum nōminat.` → `Castelliō Jōsēphum sequitur.`
11. **Num 21:24**: *mendum subesse ratus* goes. *Legit* with a different word already says he emended.
    **Apply:** `Num.21.24` la: `Castelliō, mendum subesse ratus, עָר` → `Castelliō עָר`
12. **Gen 33:19**: not a departure (Castellio keeps the word as *quessitis*), but a reader can't find *quessita* in
    a Latin dictionary, so it stays as a gloss (A2). *Cujus pretium hodiē ignōrātur* becomes the genitive of
    quality, which is shorter and drops *hodiē*.
    **Apply:** `Gen.33.19` la: `nummus cujus pretium hodiē ignōrātur; Castelliō vōcem retinet.` → `nummus incertī pretiī; Castelliō vōcem retinet.`

### A2. Castellio's coinages (items 13–14)

**Decision:** accept (Nathan, 2026-11-18: "Apply the audit as recommended")

Neither is a departure from the Hebrew, so neither fits the front matter's definition of a note. Both should stay:
the edition is meant for people learning Latin, and *Azȳmālia* and *monētum* are in no dictionary. The front matter
would say so (§F). *Ut Agōnālia, Flōrālia* can be read as "as he coined the Agonalia": *ad exemplum* + genitive is
the classical phrase and is unambiguous.

13. **Exod 23:15** (and 23:16)
    **Apply:** `Exod.23.15` la: `‘Azȳmālia’, ‘messālia’ et ‘conditālia’ (23:16) Castelliō fīnxit, ut Agōnālia, Flōrālia, Līberālia.` → `‘Azȳmālia’, et 23:16 ‘messālia’ et ‘conditālia’, Castelliō fīnxit ad exemplum Flōrālium et Līberālium.`
14. **Lev 23:24**
    **Apply:** `Lev.23.24` la: `‘Monētum’ Castelliō ā monendō fīnxit, ut Jūnō Monēta.` → `‘Monētum’ Castelliō ā monendō fīnxit, ad exemplum Jūnōnis Monētæ.`

---

## B. Slips in Castellio's text: one form (item 15)

Twenty notes record a place where every edition of Castellio seen says something the Greek or Hebrew doesn't (a
pronoun's person, *Deī* for *diēī*, *extrā* for *intrā*). Eleven end *Castelliōnis ēditiōnēs ‘…’*; nine don't
(Mark 12:29, 15:16, Luke 15:12, 19:47, John 4:36, Gal 4:17, Jas 4:2, 1 Tim 5:4, 1 Pet 5:2). The tail repeats what the
text in the line above already shows. What it really says is "this is in Castellio's editions; the editor didn't
introduce it and kept it on purpose". That is true of every note and belongs in the front matter once (§F). The
NRSVue's "Gk" notes have no tail.

**Recommendation:** drop the tail everywhere (item 15), with the front matter sentence. The alternative is to add it to
the nine that lack it. Either way the twenty would match. 1 Cor 6:14's gloss ‘et nōs’ also gets its verb, which the
other glosses have.

**Decision B:** A, drop the tail and say it once in the front matter / B, add it to the nine

**Decision:** accept, A (Nathan, 2026-11-18: "Apply the audit as recommended")

15. **Exod 40:20, Matt 20:5, Rom 8:35, 14:7, 1 Cor 6:14, 15:31, 2 Cor 13:4, 1 Thess 2:14, 1 Pet 5:8, 1 John 4:4,
    Jude 6**
    **Apply:** `Exod.40.20` la: `‘arcæ’; Castelliōnis ēditiōnēs ‘āræ’ habent.` → `‘arcæ’.`
    **Apply:** `Matt.20.5` la: `‘circā sextam’; Castelliōnis ēditiōnēs ‘septimam’.` → `‘circā sextam’.`
    **Apply:** `Rom.8.35` la: `‘ab amōre Chrīstī’; Castelliōnis ēditiōnēs ‘Deī’.` → `‘ab amōre Chrīstī’.`
    **Apply:** `Rom.14.7` la: `‘nūllus enim nostrum’; Castelliōnis ēditiōnēs ‘vestrum’.` → `‘nūllus enim nostrum’.`
    **Apply:** `1Cor.6.14` la: `ἐξεγερεῖ, ‘et nōs’; Castelliōnis ēditiōnēs ‘vōs’.` → `ἐξεγερεῖ, ‘et nōs suscitābit’.`
    **Apply:** `1Cor.15.31` la: `‘per vestram glōriātiōnem’; Castelliōnis ēditiōnēs ‘nostram’.` → `‘per vestram glōriātiōnem’.`
    **Apply:** `2Cor.13.4` la: `‘in vōs’; Castelliōnis ēditiōnēs ‘in nōs’.` → `‘in vōs’.`
    **Apply:** `1Thess.2.14` la: `‘quæ et illī’; Castelliōnis ēditiōnēs ‘nōs’.` → `‘quæ et illī’.`
    **Apply:** `1Pet.5.8` la: `‘vester’; Castelliōnis ēditiōnēs ‘noster’.` → `‘vester’.`
    **Apply:** `1John.4.4` la: `‘in vōbīs’; Castelliōnis ēditiōnēs ‘nōbīs’.` → `‘in vōbīs’.`
    **Apply:** `Jude.1.6` la: `‘magnī diēī’; Castelliōnis ēditiōnēs ‘Deī’.` → `‘magnī diēī’.`

---

## C. Clauses that restate the text (item 16)

`nt-notes-form.md` kept *Castelliō … intellegit* "only where his Latin would otherwise look like a mistake". At
Matt 3:16 and Mark 1:10 the text says *vīdit Jōhannēs* and the note says *Castelliō Jōhannem intellegit*: the same
fact twice. *Sine nōmine* already tells the reader the name is his.

Mark 1:10 also quotes εἶδεν (SBLGNT's spelling), but a *Græcē* note quotes the Greek Castellio translated, the TR,
which has εἶδε (as the Matthew note does).

**Kept:** κάμηλος (Matt 19:24, Mark 10:25, Luke 18:25). *Rudentem* against ‘camēlus’ would look like a blunder;
the clause says it is a reading. It is also the brief's model note.

**Decision C:** accept / keep the clause

**Decision:** accept (Nathan, 2026-11-18: "Apply the audit as recommended")

16. **Matt 3:16, Mark 1:10**
    **Apply:** `Matt.3.16` la: `sine nōmine; Castelliō Jōhannem intellegit.` → `sine nōmine.`
    **Apply:** `Mark.1.10` la: `Græcē εἶδεν, ‘vīdit’, sine nōmine; Castelliō Jōhannem intellegit.` → `Græcē εἶδε, ‘vīdit’, sine nōmine.`

---

## D. Single notes (items 17–26)

**Decision D:** accept all / accept items … / reject items …

**Decision:** accept all (Nathan, 2026-11-18: "Apply the audit as recommended")

17. **Mark 12:42** (reverses `nt-notes-settled.md`, which kept it as "an explanation of the coins, not a reading").
    It is a reading: Castellio writes *teruncius īdem quod quadrāns*, which makes each coin worth a quadrans, while
    the Greek makes the two together a quadrans. The note never says what the Greek says, and *duo nummī simul
    quadrantem efficiunt* is the editor explaining. As a plain *Græcē* note the reader sees the difference.
    The gloss is the Vulgate's.
    **Apply:** `Mark.12.42` la: `κοδράντης: duo nummī simul quadrantem efficiunt.` → `κοδράντης, ‘minūta duo, quod est quadrāns’.`
18. **Matt 13:35**: *verba sunt Psalmī 78:2* is a cross-reference, which no other note gives. *Sine nōmine* against
    the text's *ab Ēsāiā* already makes the point.
    **Apply:** `Matt.13.35` la: `sine nōmine; verba sunt Psalmī 78:2.` → `sine nōmine.`
19. **Matt 11:19 and Luke 7:35**: the decided example (`nt-notes-form.md` §3) quoted only ἐδικαιώθη ἡ σοφία. The
    applied notes quote the whole clause, and Luke's then differs from Matthew's only by πάντων, which isn't the
    point. Both shortened to the example.
    **Apply:** `Matt.11.19` la: `ἐδικαιώθη ἡ σοφία ἀπὸ τῶν τέκνων αὐτῆς, ‘jūstificāta est sapientia ā fīliīs suīs’;` → `ἐδικαιώθη ἡ σοφία, ‘jūstificāta est sapientia’;`
    **Apply:** `Luke.7.35` la: `ἐδικαιώθη ἡ σοφία ἀπὸ τῶν τέκνων αὐτῆς πάντων, ‘jūstificāta est sapientia ab omnibus fīliīs suīs’.` → `ἐδικαιώθη ἡ σοφία, ‘jūstificāta est sapientia’.`
20. **Rom 15:29**: two notes in one. A *Græcē* half quotes the TR without a gloss, to show Castellio's paraphrase
    *ūbertāte*, which by the rules gets no note. The other half is a *cōdicēs* note on a dropped phrase. Made one
    *cōdicēs* note in the *habent … sine* form.
    **Apply:** `Rom.15.29` la: `Græcē ἐν πληρώματι εὐλογίας τοῦ εὐαγγελίου τοῦ Χριστοῦ; cōdicēs antīquiōrēs ἐν πληρώματι εὐλογίας Χριστοῦ, ‘in plēnitūdine benedictiōnis Chrīstī’.` → `Cōdicēs antīquiōrēs habent εὐλογίας Χριστοῦ, ‘benedictiōnis Chrīstī’, sine τοῦ εὐαγγελίου.`
21. ***Habent … sine***, one order (Rom 4:19, Phlm 12, Matt 19:17). Matt 23:8 has the right order: *habent* Greek,
    ‘gloss’, *sine* Greek. Rom 4:19 puts the gloss after *sine οὐ*, so ‘cōnsīderāvit’ seems to translate οὐ.
    Philemon 12 joins two clauses with a colon. Matt 19:17 puts a Latin word after *sine* (‘bone’), uses *v. 16*,
    and leaves Διδάσκαλε without a gloss.
    **Apply:** `Rom.4.19` la: `habent κατενόησεν sine οὐ, ‘cōnsīderāvit’.` → `habent κατενόησεν, ‘cōnsīderāvit’, sine οὐ.`
    **Apply:** `Phlm.1.12` la: `nōn habent προσλαβοῦ, ‘recipe’: ὃν ἀνέπεμψά σοι αὐτόν, ‘quem tibi remīsī’.` → `habent ὃν ἀνέπεμψά σοι αὐτόν, ‘quem tibi remīsī’, sine προσλαβοῦ.`
    **Apply:** `Matt.19.17` la: `et v. 16 Διδάσκαλε sine ‘bone’.` → `et 19:16 Διδάσκαλε, ‘Magister’, sine ἀγαθέ.`
22. **Luke 6:16**: *sine ‘frātrem’* gives a Latin word after *sine* and repeats what the text shows. The Greek with its
    gloss leaves "brother" or "son" open, as the NRSVue's "Gk" does.
    **Apply:** `Luke.6.16` la: `‘Jūdam Jācōbī’, sine ‘frātrem’.` → `‘Jūdam Jācōbī’.`
23. **Cross-references in one form**, *C:V* as in `\fr` (not *v. 37*, *in 5:9*). At Rev 1:6 the note quotes λύσαντι,
    which is in 1:5, without saying so. Rev 5:10's added Greek gets its gloss like every other.
    **Apply:** `Luke.8.26` la: `ut et v. 37.` → `ut et 8:37.`
    **Apply:** `Acts.26.28` la: `ut et v. 29.` → `ut et 26:29.`
    **Apply:** `Rev.1.6` la: `habent λύσαντι, ‘solvit’, et βασιλείαν` → `habent λύσαντι (1:5), ‘solvit’, et βασιλείαν`
    **Apply:** `Rev.5.10` la: `et in 5:9 nōn habent ἡμᾶς.` → `et 5:9 nōn habent ἡμᾶς, ‘nōs’.`
24. **Acts 9:31**: *singulāriter* repeats what ‘ecclēsia’ shows (the text has *ecclēsiæ*).
    **Apply:** `Acts.9.31` la: `‘ecclēsia’, singulāriter.` → `‘ecclēsia’.`
25. **Glosses that misrender.** At 1 Cor 8:7 the variant is one word, συνηθείᾳ "habit" (for συνειδήσει,
    "conscience"). The note quotes four more words, and its gloss makes the singular εἰδώλου plural (*deastrōrum*)
    and leaves out ἕως ἄρτι. Quoting only the word that differs fixes both. At John 6:69, *ille Deī sānctus* renders
    the Greek article with *ille*, which is not Latin usage. The title is ‘Sānctus Deī’, capitalized as the edition
    capitalizes ‘Fīlius Hominis’.
    **Apply:** `1Cor.8.7` la: `τῇ συνηθείᾳ ἕως ἄρτι τοῦ εἰδώλου, ‘deastrōrum cōnsuētūdine’.` → `τῇ συνηθείᾳ, ‘cōnsuētūdine’.`
    **Apply:** `John.6.69` la: `‘ille Deī sānctus’` → `‘Sānctus Deī’`
26. **One elision mark.** John 18:28 has ᾿ (U+1FBF, the TR's breathing sign used as an apostrophe) and Luke 9:50 has ʼ
    (U+02BC). Unicode recommends the apostrophe ’ (U+2019) for Greek elision, and GFS Didot sets it correctly.
    **Apply:** `John.18.28` la: `ἀλλ᾿ ἵνα` → `ἀλλ’ ἵνα`
    **Apply:** `Luke.9.50` la: `καθʼ ὑμῶν` → `καθ’ ὑμῶν`

---

## E. Read and left as they are

- **The *Cōdicēs antīquiōrēs* notes** not named above: each quotes the differing words, glosses them, and stops.
  Long Greek is kept only where a whole clause differs (Matt 14:24, Luke 6:48, 23:15, Acts 13:20, Jude 22–23,
  Rev 13:10, 14:1).
- **The κάμηλος notes** (§C).
- **Rev 13:1** *dē dracōne*: good Latin ("said of the dragon"), and needed, since ἐστάθη has no subject in the note.
- **Matt 11:23, Luke 10:15, 1 Cor 15:55**: the Greek question mark (;) before the gloss looks like a misplaced
  semicolon but is Greek punctuation.
- **Matt 23:8** *sine ὁ Χριστός*: *sine* with an undeclined Greek quotation is normal in philological Latin, and the
  model for item 21.
- **Rev 8:7**: the only caller after punctuation (*dējectīs,*). It marks where the older manuscripts' words would
  stand, which is right for an *addunt* note.
- **Luke 16:9** ‘cum dēfēcerint opēs’: the gloss supplies the subject (mammon). That is free, but clearer than a
  bare ‘cum dēfēcerit’.
- **Rom 12:11, Jas 4:2**: Castellio follows a reading (καιρῷ) or a conjecture (φθονεῖτε) known in his day. A study
  Bible would say so. A reader's edition needs only the Greek, and `rom-notes.md` cites no manuscript evidence seen.
- **Typography.** Lettered callers that restart each chapter, the reference in bold, notes at the foot of the page
  (PDF), at the chapter's end (site) and as pop-ups (EPUB): this is the ESV's and NRSVue's practice. I considered
  italics for the Latin glosses in place of ‘…’ (the NRSVue italicizes alternative readings). But the Oxford Classical
  Texts do the opposite, italicizing the editor's words, and in a note that is all Latin the quotation marks
  separate gloss from comment more clearly at footnote size. They also survive the TXT build. No change proposed.

---

## F. The front matter and the brief (on approval of A–B)

**Front matter** (`text/FRT.usfm`, the *Notæ* table, reviewed in `docs/front-matter.md`). After *… discēdunt.* in
the ᵃ row, add (macrons checked with `latin macron-check`; the unknown words are æ spellings):

> Ubi sōla verba \zvt Hebræa\zvt*\zboth  aut \zboth*\znt Græca\znt* adnotantur, Castelliō aliter vertit, nec
> ejus verba mūtāvī.\zvt  Paucæ etiam vōcēs explicantur quās ipse fīnxit aut Hebræās retinuit.\zvt*

("Where only the Hebrew or Greek words are given, Castellio rendered them otherwise, and I have not changed his
words. A few words he coined, or kept from the Hebrew, are also explained.") The edition conditions follow the row's.

**Brief** (`brief.md`, the notes paragraph): it says an OT note begins *Hebræē*, a form no dictionary knows
(`latin macron`: Gaffiot has *Hebraicē*, which every note uses). Change to *Hebraicē*. The model (Matt 19:24) is
updated to the form now in the text, *Græcē κάμηλος, ‘camēlus’; Castelliō fūnem nauticum intellegit*, and the OT
formulas of §A are added.

**Decision F:** accept / change the wording

**Decision:** accept (Nathan, 2026-11-18: "Apply the audit as recommended")

---

## G. Beyond this audit (not proposed here)

- **The Old Testament has 15 notes in 153 chapters; the New has 154 in 260.** The OT notes come only from places
  where Castellio's 1554 annotations comment. Nothing has searched the OT systematically, as `pipeline notes` did
  the NT. A professional edition would apply the same test (the WLC against Castellio, checked against the NRSVue's
  notes) before it calls the OT annotated. This is worth a process file of its own before Deuteronomy.
- **Two styles of reference.** The notes cite *19:24*, and the front matter's *Notæ* cites *Mc 16,9–20* and
  *Jo 7,53–8,11* in the continental style. One edition should use one. The colon matches `\fr` and the site's
  links.
