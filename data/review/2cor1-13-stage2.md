# 2 Corinthians 1–13, stages 1–2: Wikisource against the 1573 base

Proposed 2026-11-10 (decision 30's standing rule), on the route of 1 Corinthians (`data/review/1cor1-16-stage2.md`).

- **Base**: the 1573 Basel edition (decision 24; MDZ bsb10141277, canvases 879–887). 1556 is the reference: where it
  reads otherwise, its reading is recorded as a variant (section 5). Stage 1 drafted Wikisource's 2 Corinthians as
  **`text/draft/2CO.usfm`** (BSB paragraphs). You have no earlier work on 2 Corinthians; `TXT/1 - OCR` (the
  1726–27 printing, Google Books OCR, uncorrected) is the witness `1726`, read as an OCR.
- **Wikisource's 2 Corinthians is the early wording**, as its Romans and 1 Corinthians, with slips of its own:
  *caecas* for *torpentes* (3:13), *res* for *creatura* (5:17), *sontem* for *peccatum* (5:21), *persona* for *caro*
  (7:5), *favor* for *gratia* (12:9, 13:14). 1556 already has every one of these revisions where its OCR can be read;
  1573's own change against 1556 is 10:12 *ausimus* (1556 *audemus*).
- **Chapter 13 is not short of a verse.** Wikisource has 13 verses in chapter 13, and so does 1573 (canvas 887): both
  print the KJV's 13:13 (*Salutant vos sancti omnes*) inside their 12, after *Salutate inter vos osculo sancto*, and
  their 13 is the KJV's 13:14 (the blessing). No words are missing; the KJV's 13:13 is made by a versification split.
- **Versification** (decision 5): 2 edits in `data/versification/2Cor.draft.edits.tsv`, applied (256 verses, every
  chapter at the KJV count):
  - **7:15–16**: 1573 prints 16 before *Gaudeo, posse me omnibus in rebus vobis confidere* (canvas 883), as the KJV;
    Wikisource runs it into 15. Split.
  - **13:12–14**: split at *Salutant vos sancti* (above); 13 becomes the KJV's 14.
  - 1573 numbers chapter 1 otherwise: its 21 holds the KJV's 1:21–22 (*Ac qui nos vobiscum confirmat … nostris animis
    indidit*), so its 22–23 are the KJV's 23–24 (canvas 880). Wikisource follows the KJV; kept.
- **Collation** (`python -m pipeline collate 2Cor 1-13`; `data/calibration/2Cor1-13-collation.tsv`, 438 places after
  the renumbering), with the edge and f/s checks. Read on the page image (crops in `sources/mdz-1573/crops/2Cor.*`,
  52): the 40 readings where 1573 and another printing agree against Wikisource and the 7 where two others do; the
  places where only 1573's OCR differs and its words are Latin (5:21 *peccatum*, 8:1 *ecclesias*, 8:7 and 8:11 word
  order, 12:6 *equidem*, 11:28 *destinent* …); the edge places (3:10 *conseratur* for *conferatur*; 6:2, 8:3, 10:3,
  11:27 are 1573 line ends its OCR lost). The rest of the 219 base-only readings are 1573's OCR (*oinnis*, *cófolatio*,
  *Chritto*), running heads (*II PAVLI EPISTOLA*) and margin notes run into the text. Each place was also read against
  1556 (its e-rara OCR, `sources/erara-1556/`) and the archive.org printings (1758, 1681, 1715, 1747, 1750).
- **The f/s sweep** (asked for after 1 Corinthians): every *f* word in the draft whose *s*-form is also Latin
  (*fit/sit*, *fuit/suit*, *fore/sore*, *forte/sorte*, *ferat/serat* …, 40 words) was read in its verse: all are *f*
  (1:6 *id fit* twice, read on the image). The reverse sweep (every *s* word whose *f*-form is Latin: *sit/fit*,
  *sumus/fumus*, *sive/five*, *semen/femen* …) found 3:10 *conseratur* (also an edge place) and **4:4 *insidentium*
  for *infidentium*** (Castellio's *infidens*, ἀπίστων, as 6:14–15), which the collation could not see: 1573's OCR
  reads the word right, but *insidentium* is Latin too and its f/s check compares only where 1573's OCR has the f.
- **In all, 45 corrections**: 24 Wikisource slips (section 1), 16 readings of Castellio's revised text (section 2),
  1 s-for-f slip found by the sweep (section 2a), 2 slips in verses 1573's OCR had not aligned (section 2b, found
  during stages 3–5), 2 word divisions (section 3). **Applied to the draft** (decision 30's
  standing rule). Spellings (*caussa*, *adfligo*, *quacumque*, *charitas*, *exsugo*, *paullulum*) are left to stage 3
  (decision 37's rules); one rule added (section 6). Three places where 1573 reads against 1556 and the sense are kept
  as Wikisource and 1556 have them, for your eye (section 4).

## 1. Wikisource slips: 1573 and the other printings agree against it (24)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; every item read on the 1573 page image)

1. **2 Corinthians 1:13** *recogniscitis* → *recognoscitis*. 1573 *aut etiam recognoſcitis* (canvas 880); 1556, 1758, 1681, 1750.
   **Apply:** `2Cor.1.13` la: `etiam recogniscitis` → `etiam recognoscitis`
2. **2 Corinthians 1:13** *recogniscetis* → *recognoscetis*. 1573 *ad extremum recognoſcetis* (canvas 880); 1556, 1681, 1747, 1750.
   **Apply:** `2Cor.1.13` la: `extremum recogniscetis` → `extremum recognoscetis`
3. **2 Corinthians 1:16** *Et istae in Macedoniam* → *Et istac in Macedoniam*. 1573 *& iſtac in Macedoniam* (canvas 880; the adverb, "by your way"); 1556, 1758.
   **Apply:** `2Cor.1.16` la: `Et istae in` → `Et istac in`
4. **2 Corinthians 3:5** *sed uqod idonei* → *sed quod idonei*. 1573 *quod* (canvas 881); 1747, 1750, 1715.
   **Apply:** `2Cor.3.5` la: `sed uqod idonei` → `sed quod idonei`
5. **2 Corinthians 3:10** *splendore conseratur* → *splendore conferatur*. 1573 *ſi cum ſuperante ſplendore con-feratur* (canvas 881, f across the line break); 1758, 1750.
   **Apply:** `2Cor.3.10` la: `splendore conseratur` → `splendore conferatur`
6. **2 Corinthians 5:11** *hominibus persuademur* → *hominibus persuademus*. 1573 *vtut hominibus perſuademus* (canvas 882); 1556, 1758, 1681, 1750.
   **Apply:** `2Cor.5.11` la: `hominibus persuademur` → `hominibus persuademus`
7. **2 Corinthians 6:2** *te accepto tmepore* → *te accepto tempore*. 1573 *Te accepto tempore* (canvas 882); 1715, 1747, 1750.
   **Apply:** `2Cor.6.2` la: `accepto tmepore` → `accepto tempore`
8. **2 Corinthians 6:10** *multos locupletemur* → *multos locupletemus*. 1573 *cùm multos locupletemus* (canvas 882; we make many rich); 1556, 1747, 1750.
   **Apply:** `2Cor.6.10` la: `multos locupletemur` → `multos locupletemus`
9. **2 Corinthians 7:4** *de vobis gloriatio* → *de vobis est gloriatio*. 1573 *multa mihi de vobis eſt gloriatio* (canvas 883); 1556, 1758, 1681.
   **Apply:** `2Cor.7.4` la: `de vobis gloriatio` → `de vobis est gloriatio`
10. **2 Corinthians 7:10** *At mundamus dolor* → *At mundanus dolor*. 1573 *At mundanus dolor* (canvas 883); 1556, 1758, 1750.
   **Apply:** `2Cor.7.10` la: `At mundamus dolor` → `At mundanus dolor`
11. **2 Corinthians 9:5** *fratres horatri* → *fratres hortari*. 1573 *hortari* (canvas 884); 1758, 1750.
   **Apply:** `2Cor.9.5` la: `fratres horatri` → `fratres hortari`
12. **2 Corinthians 9:9** *ejus liberalitatis manet* → *ejus liberalitas manet*. 1573 *eius liberalitas manet æterna* (canvas 884; the subject); 1556, 1758, 1681, 1715.
   **Apply:** `2Cor.9.9` la: `ejus liberalitatis manet` → `ejus liberalitas manet`
13. **2 Corinthians 10:4** *sed divini potentia* → *sed divinipotentia*. 1573 *ſed diuinipotentia* (canvas 884, one word): the neuter plural of *dīvīnipotēns*, with *arma … nōn carnālia sunt* (δυνατὰ τῷ θεῷ); 1758, 1747.
   **Apply:** `2Cor.10.4` la: `sed divini potentia` → `sed divinipotentia`
14. **2 Corinthians 10:13** *quem Deus nobis tribuit* → *quem Deus nobis eum tribuit*. 1573 *quem Deus nobis eum tribuit* (canvas 885; its OCR *cum*); 1556, 1758, 1681, 1715, 1747, 1750.
   **Apply:** `2Cor.10.13` la: `Deus nobis tribuit` → `Deus nobis eum tribuit`
15. **2 Corinthians 11:2** *divina obrectatione* → *divina obtrectatione*. 1573 *diuina obtrectatione* (canvas 885); 1758, 1750.
   **Apply:** `2Cor.11.2` la: `divina obrectatione` → `divina obtrectatione`
16. **2 Corinthians 11:4** *Quod si venerit* → *Quod si veniret*. 1573 *Quòd ſi veniret qui aliũ Ieſum prædicaret* (canvas 885; imperfect, as *prædicāret … acciperētis*); 1556, 1758.
   **Apply:** `2Cor.11.4` la: `Quod si venerit` → `Quod si veniret`
17. **2 Corinthians 11:10** *hac gloratione* → *hac gloriatione*. 1573 *gloriatione* (canvas 885); 1556, 1758, 1715, 1747, 1750.
   **Apply:** `2Cor.11.10` la: `hac gloratione` → `hac gloriatione`
18. **2 Corinthians 11:15** *sic transifigurantur* → *sic transfigurantur*. 1573 *ſic transfigurantur* (canvas 885); 1556, 1747, 1750.
   **Apply:** `2Cor.11.15` la: `sic transifigurantur` → `sic transfigurantur`
19. **2 Corinthians 11:19** *fertis, ipse prudentes* → *fertis, ipsi prudentes*. 1573 *ipſi prudentes* (canvas 886; with *vōs*); 1556, 1715, 1747, 1750.
   **Apply:** `2Cor.11.19` la: `ipse prudentes` → `ipsi prudentes`
20. **2 Corinthians 12:7** *ob patefactionem praestantiam* → *ob patefactionum praestantiam*. 1573 *ob patefactionum præſtantiam* (canvas 886); 1556, 1758, 1750.
   **Apply:** `2Cor.12.7` la: `ob patefactionem praestantiam` → `ob patefactionum praestantiam`
21. **2 Corinthians 12:7** *ne nimis offerar* → *ne nimis efferar*. 1573 *ne nimis efferar* (canvas 886), as *efferam* earlier in the verse; 1556, 1758, 1750.
   **Apply:** `2Cor.12.7` la: `ne nimis offerar` → `ne nimis efferar`
22. **2 Corinthians 12:20** *sussurri* → *susurri*. 1573 *ſuſurri* (canvas 887); 1750.
   **Apply:** `2Cor.12.20` la: `sussurri` → `susurri`
23. **2 Corinthians 12:21** *adfligat met Deus* → *adfligat me Deus*. 1573 *affligat me Deus* (canvas 887); 1556, 1750.
   **Apply:** `2Cor.12.21` la: `adfligat met Deus` → `adfligat me Deus`
24. **2 Corinthians 13:2** *nunc absens seribo* → *nunc absens scribo*. 1573 *nunc abſens ſcribo* (canvas 887); 1556, 1715, 1750.
   **Apply:** `2Cor.13.2` la: `absens seribo` → `absens scribo`

## 2. Castellio's revised wording: 1573 against Wikisource's early line (16)

Where Wikisource reads with the early-line printings (1715, 1747, 1750), or 1573 differs in order or form. 1556 has
the revised reading too wherever its OCR can be read, except 10:12 (section 5).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; every item read on the 1573 page image)

1. **2 Corinthians 1:14** *quod nos sumus vestra gloriatio* → *quod nos vestra sumus gloriatio*. 1573 *quòd nos ᵇ veſtra ſumus gloriatio* (canvas 880; margin *b Ii sumus, de quib. gloriemini vos*); 1556, 1758, 1681 (word order). Wikisource with 1750.
   **Apply:** `2Cor.1.14` la: `quod nos sumus vestra gloriatio` → `quod nos vestra sumus gloriatio`
2. **2 Corinthians 3:13** *mentes haberent caecas* → *mentes haberent torpentes*. 1573 *ſed mentes haberent torpentes* (canvas 881); 1556 (OCR *haberent torpentes*), 1758, 1726. The early line *caecas* (Wikisource, 1747, 1750).
   **Apply:** `2Cor.3.13` la: `haberent caecas` → `haberent torpentes`
3. **2 Corinthians 5:17** *is nova res est* → *is nova creatura est*. 1573 *is noua creatura eſt* (canvas 882), καινὴ κτίσις; 1556, 1758, 1726. The early line *res* (Wikisource, 1747, 1750).
   **Apply:** `2Cor.5.17` la: `is nova res est` → `is nova creatura est`
4. **2 Corinthians 5:21** *pro nobis sontem effecerit* → *pro nobis peccatum effecerit*. 1573 *pro nobis peccatum effecerit* (canvas 882), ἁμαρτίαν ἐποίησεν; 1556, 1758. The early line *sontem* (Wikisource, 1750).
   **Apply:** `2Cor.5.21` la: `pro nobis sontem effecerit` → `pro nobis peccatum effecerit`
5. **2 Corinthians 7:5** *haberet nostra persona* → *haberet nostra caro*. 1573 *nec vllam quietem haberet noſtra caro* (canvas 883), ἡ σὰρξ ἡμῶν; 1556, 1758, 1681, 1726. The early line *persona* (Wikisource, 1750), as *humanitas → caro* in Romans.
   **Apply:** `2Cor.7.5` la: `haberet nostra persona` → `haberet nostra caro`
6. **2 Corinthians 8:1** *Certiores vos facimus* → *Certiores autem vos facimus*. 1573 *Certiores autem vos facimus* (canvas 883, the chapter's first line beside the initial). Every other OCR loses the verse's first words under its initial, so 1573's image is the only evidence; δέ.
   **Apply:** `2Cor.8.1` la: `Certiores vos facimus` → `Certiores autem vos facimus`
7. **2 Corinthians 8:1** *in ecclesiis Macedoniae* → *in ecclesias Macedoniae*. 1573 *in eccleſias Macedoniæ collato* (canvas 883; conferred upon); 1556, 1758, 1681. The early line *ecclesiis* (Wikisource, 1715, 1747, 1750).
   **Apply:** `2Cor.8.1` la: `in ecclesiis Macedoniae` → `in ecclesias Macedoniae`
8. **2 Corinthians 8:6** *Titum hortati simus* → *Titum hortati sumus*. 1573 *vt nos Titum hortati ſumus* (canvas 883); **1556** (OCR *hortatí fumus*), 1750. Wikisource's subjunctive with 1715, 1747. The indicative after a consecutive *ut* is odd Latin, but both of Castellio's last editions print it: for your eye (stages 3–5 summary).
   **Apply:** `2Cor.8.6` la: `hortati simus` → `hortati sumus`
9. **2 Corinthians 8:7** *in rebus omnibus excellitis* → *omnibus in rebus excellitis*. 1573 *quemadmodum omnibus in rebus excellitis* (canvas 883); 1556, 1758 (word order). Wikisource with 1750.
   **Apply:** `2Cor.8.7` la: `in rebus omnibus excellitis` → `omnibus in rebus excellitis`
10. **2 Corinthians 8:11** *voluntatis est alacritas* → *est voluntatis alacritas*. 1573 *vt quomodo eſt voluntatis alacritas* (canvas 884); 1556, 1758, 1681 (word order). Wikisource with 1750.
   **Apply:** `2Cor.8.11` la: `voluntatis est alacritas` → `est voluntatis alacritas`
11. **2 Corinthians 9:12** *officium hujusmodi est* → *officium ejusmodi est*. 1573 *officium eiuſmodi eſt* (canvas 884); 1758, 1681. Wikisource *hujusmodi* with 1750, as 1 Cor 5:11.
   **Apply:** `2Cor.9.12` la: `officium hujusmodi est` → `officium ejusmodi est`
12. **2 Corinthians 10:12** *Nec enim audemus* → *Nec enim ausimus*. 1573 *ᶜ Nec enim auſimus comparare* (canvas 885; margin *Indigni sumus illi, cum quibus nos comparemus*); 1758, 1681. **1556** *audemus*, with Wikisource and 1750: a 1573 change (section 5).
   **Apply:** `2Cor.10.12` la: `Nec enim audemus` → `Nec enim ausimus`
13. **2 Corinthians 12:6** *non essem quidem amens* → *non essem equidem amens*. 1573 *nõ eſſem equidem amẽs* (canvas 886); 1556, 1758, 1681. Wikisource *quidem* with 1747, 1750.
   **Apply:** `2Cor.12.6` la: `essem quidem amens` → `essem equidem amens`
14. **2 Corinthians 12:9** *Satis est tibi meus favor* → *Satis est tibi mea gratia*. 1573 *Satis eſt tibi mea gratia, nam mea fortitudo* (canvas 886), ἡ χάρις μου; 1556, 1758, 1681. The early line *meus favor* (Wikisource, 1747, 1750), as Romans' *favor → gratia*.
   **Apply:** `2Cor.12.9` la: `tibi meus favor` → `tibi mea gratia`
15. **2 Corinthians 13:4** *per Dei in vos potentiam* → *per Dei in nos potentiam*. 1573 *per Dei in nos potentiam* (canvas 887); 1758, 1681. Wikisource *in vos* with 1750, as the Greek εἰς ὑμᾶς; 1556's OCR lacks the clause. For your eye (stages 3–5 summary).
   **Apply:** `2Cor.13.4` la: `per Dei in vos potentiam` → `per Dei in nos potentiam`
16. **2 Corinthians 13:14** *Domini Jesu Christi favor* → *Domini Jesu Christi gratia*. 1573 *Domini Ieſu Chriſti gratia* (canvas 887), ἡ χάρις; 1681. The early line *favor* (Wikisource, 1747, 1750).
   **Apply:** `2Cor.13.14` la: `Christi favor,` → `Christi gratia,`

## 2a. Found by the f/s sweep (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; read on the 1573 page image)

1. **2 Corinthians 4:4** *videlicet insidentium mentes* → *videlicet infidentium mentes*. 1573 *quorum videlicet infidentium* (canvas 881, f); 1556, 1681, 1715, 1747, 1750. Castellio's *infidens* (unbeliever, ἀπίστων), as Wikisource's own 6:14 *infidentium*, 6:15 *infidente*.
   **Apply:** `2Cor.4.4` la: `videlicet insidentium` → `videlicet infidentium`

## 2b. Found where 1573 was not aligned (2)

The collation found no 1573 text for 2:9–13 (its OCR reads the page's two columns out of order there) and only part of
3:9, 4:18, 5:21, 6:1 and 8:24. Reader 1 of stages 3–5 noticed 2:13; those eight verses were then read by hand against
1573's page text and image: 2:9–12, 3:9, 4:18, 5:21 (beyond section 2's item), 6:1 and 8:24 agree with the draft.
`collate` now lists such verses itself (kind `uncovered`, the base witness showing under 60% of a verse's words;
added 2026-11-10 at your request): here 2:9–13, 3:9, 3:12, 3:16, 4:1, 4:5, 8:3, 11:13. The six not read before were
read then: 3:12 and 8:3 run on to the next line (*perspi-cuitate vtimur*, *vi-res vltro*), and 3:16, 4:1, 4:5, 11:13
are there in full, words run together (*detrahiturvelamen*); none differs from the draft.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10; read on the 1573 page image)

1. **2 Corinthians 2:13** *requietem habuit* → *requietem habui*. 1573 *nullam animi requietem habui* (canvas 880; Paul speaks, *invēnissem*, *profectus sum*); 1556, 1758, 1681, 1750.
   **Apply:** `2Cor.2.13` la: `requietem habuit` → `requietem habui`
2. **2 Corinthians 2:13** *profectus, sum in Macedoniam* → *profectus sum in Macedoniam*. 1573 *profectus ſum in Macedoniam* (canvas 880), no comma; 1758, 1750.
   **Apply:** `2Cor.2.13` la: `profectus, sum` → `profectus sum`

## 3. Word division (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10)

1. **2 Corinthians 8:5** *quin seipsos addixerunt* → *quin se ipsos addixerunt*. Your settled *sē ipsōs* (Rom), *nōs ipsōs* (2×), *vōs ipsōs* (4×), never joined; as 1 Cor 3:18 *se ipsum*. 1573 joins it (*ſeipſos*, OCR).
   **Apply:** `2Cor.8.5` la: `quin seipsos` → `quin se ipsos`
2. **2 Corinthians 10:12** *in seipsis metiri* → *in se ipsis metiri*. 1573 *ſe in ſe ipſis metiri* (canvas 885, apart); 1758; your settled *sē ipsīs*.
   **Apply:** `2Cor.10.12` la: `in seipsis` → `in se ipsis`

## 4. Checked and kept

- **13:12–14** and **7:15–16**: no words missing (versification, above).
- **5:10** *ut ferat quisque*: 1573 *quique* (canvas 882), with 1556 and 1758; 1681 and 1750 *quisque*. *quique* is not
  the pronoun's nominative; kept as Wikisource, a misprint carried from 1556. For your eye.
- **11:28** *quae me quotidiana distinent* (keep me busy, ἐπίστασις): 1573 *deſtinent* (canvas 886), with 1758 and
  1681, which follow 1573; **1556** and 1750 *distinent*. Kept with 1556, as the sense. For your eye.
- **12:7** *qui me tundat* (beat, κολαφίζῃ): 1573 *tondat* (canvas 886, shear), with 1758; **1556** *tundat*. Kept
  with 1556, as the sense. For your eye.
- **13:5** *annon vos ipsos*: 1573 *An non voſipſos*; your settled *annōn* (6×) and *an nōn* (8×) both stand. Kept.
- **2:17** *sed ut ex sinceritate, sed ut ex Deo*: 1573 has a colon after *sinceritate*; punctuation, left to stage 3.
- **4:1, 4:16** *defetiscimur*: 1573 *defetiſcimur* (its OCR *defethiſcimur*). Kept.
- **8:12** *adest*, **12:18** *ingressi*, **4:2** *tractamus*, **5:4** *tabernaculo*, **7:1** *sanctimonia*, **7:2**
  *circumscripsimus*: 1573 prints them; other OCRs misread.
- **Note letters and margin notes**, not text: 1:9 *a*, 1:14 *b*, 2:3 *a*, 4:4 *a*, 5:7 *a*, 5:19 *b*, 6:2 *a*,
  10:1 *a*, 11:15 *a*, 11:23 *b*, 12:5 *a*, 12:7 *b*, 12:9 *c*, 10:12 *c*; the glosses at 1:14, 3:10 (*legis splendor
  nullus est, si cum Euangelio comparetur*), 10:12, 12:6–7.
- **13:14** the subscription (*Ad Corinthios secunda scripta est Philippis Macedoniae, missa per Titum et Lucam*): 1573
  sets it in italics under the verse (canvas 887), as after 1 Corinthians. Set apart as `\cls` at stage 3
  (decision 37).
- **Spellings, left to stage 3** (decision 37's rules, and new rules where it names a principle): *caussa* (1573
  *causa*), *adfligo*, *adficio*, *adfero*, *inadspectabilis* (1573 *afflig-*, *affic-*, *affer-*, *inaspectabilis*),
  *quacumque*, *quandocumque*, *tamquam*, *quamquam* (1573 *-cunque*, *-nquam*), *eamdem* (1573 *eandem*), *exstat*
  (1573 *extat*), *exsuxi*, *exsugam* (1573 *exuxi*, *exugam*; Gaffiot *exsūgō*), *paullo*, *paullulum* (1573
  *paullo*, *paullulum*), *caritas*, *carissimi* (1573 *charitas*, *charissimi*; your settled *cārit-* 13×),
  *lacrimis* (1573 *lachrymis*), *quum* (1573 *cum*), *Israelitae*.

## 5. Recorded variants: 1556 against 1573

Where 1556 reads otherwise than 1573. Recorded, not applied (decision 24). 1556 is cited from its OCR (e-rara
10281656), not the page image.

| Place | The text now | 1573 | 1556 | Also |
|---|---|---|---|---|
| 2 Cor 10:12 | *Nec enim ausimus* | = | *Nec enim audemus* | Wikisource, 1750 |
| 2 Cor 11:28 | *quotidiana distinent* (1556) | *destinent* | = | 1758, 1681 with 1573 |
| 2 Cor 12:7 | *qui me tundat* (1556) | *tondat* | = | 1758 with 1573 |
| 2 Cor 5:10 | *ferat quisque* (Wikisource) | *quique* | *quique* | 1758 with 1573 |

**Decision:** accept (record as variants) (Claude, under the standing rule of decision 30, 2026-11-10)

## 6. Spelling rule added

Wikisource writes *arrhabonem* (1:22, 5:5) where 1573 (canvas 880, *arrabonem*), 1556, 1758, 1715, 1747 and your
settled text (*arrabōn-*, 3×) write *arrabo*, Gaffiot's headword: rule *arrhabonem → arrabonem* added to
`data/rules/orthography.tsv`, approved under decision 30, applied at stage 3.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-10)
