# Critique of the front matter draft (second version, `docs/front-matter.md`)

Written 2026-11-13. The corpus counts come from `python -m pipeline latin attest` (fur-fulminis tiers: 1 = Cicero's
letters, Plautus, Terence; 2 = Petronius, Apuleius, Horace's and Pliny's letters, Seneca's letters, Erasmus; 2.5 =
Cicero's other works, Caesar, Vergil; 3 = other Latin to c. AD 150; 4 = later). A phrase missing from the corpus is
not proof of absence. The new facts below are recorded in `docs/editions.md`.

## 1. Latinity

The draft is mostly sound in grammar, but it leans on Neo-Latin and on calques of modern English and French in a
dozen places. The worst are the ones a classically trained reader stumbles on first.

### Calques and unattested collocations

| In the draft | Problem | Corpus | Proposed |
|---|---|---|---|
| *Latīnē vertit* | "translate into Latin", English shaped. *vertere* is classical, but *Latīnē vertere* is not attested as a phrase | 0; *Latīnē vertō* (lemma) only T2 Pliny once, T4 Isidore and Augustine | *in Latīnum convertit*: Cicero's own (*ē Græcō in Latīnum convertere*, T2.5), and the verb of *Dē optimō genere ōrātōrum* 14 |
| *Orthographiam ad normam … redēgimus* | "brought into conformity with the standard" | *ad normam redigere*: 1 hit, a medieval chronicler | *Orthographiam ad lexicon Fēlīcis Gaffiot accommodāvimus* (*accommodāre ad*, T1 Cicero) |
| *Textum hodiernō mōre in paragraphōs distribuimus* | *textus* "the text" is late and Neo-Latin (classical *textus* is a weave); *hodiernō mōre* is unattested, a calque of "in the modern way" | *hodiernō mōre* 0; *nostrō mōre* 12, Cicero 5 | *Capita, ut nunc fit, in paragraphōs dīvīsimus* (*ut nunc fit*: T1, Cicero) |
| *Biblia tua vernācula* | "your vernacular Bible". *vernāculus* is classical, but not of a language | *lingua vernācula*: Erasmus only (T2); *sermō vernāculus*: Vives, Cordier | *Biblia patriō sermōne scrīpta*; *patriō sermōne* is Pliny (T2), Curtius, Silius, and Bünemann's own words |
| *Germānicē recitābat* | Not classical; the corpus hits are all the name *Germānicus* | (vocative hits only) | *patriō sermōne recitābat*, as Bünemann wrote it |
| *scholæ præfectus est* | French *régent* / "head of the school" | *lūdō præesse*: 1 Neo-Latin hit | *lūdī magister factus est* (Cicero, T2.5; Martial, Erasmus) |
| *ministrī eum in suum ōrdinem nōn recēpērunt* | "did not admit him to their order" | *in ōrdinem recipere*: Digest only | *ministrī ecclēsiæ eum in collēgium suum nōn cooptāvērunt*. *cooptāre in collēgium* is the classical phrase (Quintilian, quoting Cicero; Seneca, T3) |
| *Canticum … inter librōs sacrōs habēre nōllet* | *habēre inter* is weak; *in numerō habēre* only T2 Erasmus and Quintilian | — | *inter sacrōs librōs numerāre nōllet* (*numerāre inter*: T3 Seneca, Livy, Columella) |
| *fūrtī lignōrum accūsāvit* | *fūrtī accūsāre* is attested only in law and the Decretals (T4) | 4 hits, all T4 | *fūrtum lignōrum eī obiēcit* |
| *Rhēnō auctō* | *flūmen auctum* is T3 (Seneca, Tacitus); not with a river's name | *Rhēnus auctus*: 1 medieval hit | Acceptable, flagged; or *quæ Rhēnus abundāns dētulerat* |
| *Servetus … cremātus est* | *cremāre* a living man is Silver and late (Curtius, Tertullian) | *vīvus cremāre* T2 Apuleius, T3, T4 | *vīvus combūstus est* (*vīvum combūrere*: T1 Plautus, Cicero ×4) |
| *nōmine Mārtīnī Belliī* | Ambiguous: "in the name of" | *fictō nōmine*: medieval only; *fictus … nōmen* Cicero once | *fictō Mārtīnī Belliī nōmine* (Cicero's construction) |
| *nōn nōminātō Castelliōne* | An ablative absolute of a person not named is not attested | 0 | *Beza, quamquam Castelliōnem nōn nōminābat, scrīpsit* |
| *ad fīnem ūsque sæculī duodēvīcēsimī* | *sæculum* as "century" with an ordinal is post-classical | — | *ūsque ad annum ferē 1780*: more exact too (Hanover 1780, Leipzig 1778) |
| *in ūsum studiōsæ juventūtis* | Only one corpus hit (T4); it is the Leipzig title, not our phrase | 1, T4 | Keep it, but as a quotation of the title, in quotation marks |
| *in antīquissimīs cōdicibus* | *cōdex* "manuscript" is late | — | *in antīquissimīs exemplāribus*: Cicero's word for a copy, and Castellio's own (*in quibusdam exemplaribus*) |
| *majusculīs litterīs* | Neo-Latin | Erasmus once (T2) | Acceptable, flagged |
| *sententiam potius quam Hebraismōs reddidit* | *Hebraismus* is a Neo-Latin technical word; *sententiam reddere* only T2/T3 (Apuleius, Tacitus) | 3 hits | Cicero's own wording: *nōn verbum prō verbō, sed sententiam* … or see §3 below |
| *interpūnctiōnem mūtāvimus ubi sententiæ clāriōrēs fierent* | "where the sentences would become clearer": loose, and the mood is wrong | — | *interpūnctiōnem, quō clārior esset sententia, nōnnumquam mūtāvimus* |
| *Argūmenta … nōn reddidimus* | *reddere* is "render" (translate), not "print" | — | *omīsimus* |
| *quī Latīnē discit verba ex rēbus intellegit* | Fine as Latin, but see the factual point in §2 | — | — |

### Words that are right as they stand

These are classical in the sense used, with tier-1 or tier-2.5 evidence: *victum quærere* and *tenuis victus*
(Terence, Cicero, Horace); *ferrō flammāque* and *ferrō ignīque* (Livy, Caesar, Cicero); *cavēre ab* (Cicero ×58);
*eādem operā* (Plautus; Castellio's own phrase); *magnī facere*; *ratiōnem dūcere* (Cicero, Castellio's words);
*operam dare ut*; *mortem obīre*; *morbō cōnsūmptus*; *Latīnē loquī* (Cicero ×22).

*orthographia* (Suetonius, Quintilian) and *interpūnctiō* (Cicero) are classical words. *typographus*, *macrō*,
*paragraphus* (in this sense) and *Hebraismus* are unavoidable Neo-Latin; keep them few.

### Spelling and macrons

- **collēgium**, with a long ē, as the settled text has it (*in collēgiō*, Acts 17:17). The draft wrote *collegium*
  in *Dē ejus interpretātiōne*.
- **Ecclesiastical words in the text.** The New Testament still reads *collēgium* for synagogue (it has no
  *synagōga* at all) and *fānum* beside *templum*. So "the church words that Castellio restored are what you read
  here" is too broad. It holds for *baptisma*, *baptīzāre*, *angelus* and *ecclēsia* (59 times), not for
  synagogue or temple.

### Style

- **Too many sentences of one shape**, a past-tense report followed by a quotation. The life reads as a list of
  dated events, *annō 1540 … annō 1542 … annō 1544 … annō 1553*. Cicero's letters would join them with *cum*,
  *postquam* and participles, and drop the years the reader doesn't need.
- **Several sentences say less than the sources do.**
  - *litterīs ērudītus* doesn't say which letters: Latin and Greek, and he wrote Greek verse.
  - *Inde … oppugnāvērunt* runs together three different men and occasions: Calvin's *Calumniae nebulonis* (1558),
    Beza's *Responsio* (1563), and Bodenstein's complaint before the Basel council (November 1563).
  - *corrēctor* is stated as fact, but Buisson says "probablement" (I:240).
- ***Ad hoc ipsum etiam nunc ūtilia sunt*** is vague. It means "for this very thing" without saying what.

## 2. Your points

1. **Other Latin Bibles.** This is the largest gap. The reader isn't told what Castellio was set against. What the
   sources here support:
   - the Vulgate, which his critics defended and his admirers called barbarous (Furió Ceriol's poem in the
     *Iudicia*: *fantur Biblia barbaricē*, until Castellio);
   - the word-for-word Protestant and Catholic versions of his own day: Pagnini (1528), Münster, the Zurich Bible
     (Leo Jud, 1543; Bünemann compared it), Beza's New Testament (1556), and later Tremellius–Junius. Eskhult's
     chapter sets Castellio among these (per its review).

   What sets his apart: classical vocabulary, the sense rendered rather than the Hebrew idiom, the whole Bible with
   the Apocrypha and the Josephus supplement, and his candour about what he did not understand. Pagnini's and
   Münster's dates are general knowledge, not yet seen in a source here; check them before printing.
2. **Brackets.** The text already follows one standard: ⟦…⟧ for the two long passages (Mark 16:9–20, John
   7:53–8:11), […] for every shorter one. The 1 John 5:7–8 parentheses were turned into brackets when the
   bracket proposal was applied (`data/review/brackets-and-notes.md` item 40). The draft's *Notæ* row for ( ) is
   my error and goes. The […] row can add that at 1 John 5:7–8 the brackets stand where 1573 has parentheses. 1556
   already printed square brackets there.
3. **Moses speaking Latin.** Yes. The title page of the *Moses latinus* (Basel, 1546) reads *Vidēbis, lēctor,
   Mōsem nunc dēmum et Latīnē loquentem et apertē* ("you will now at last see Moses speaking Latin, and plainly";
   Buisson II:355). Two further places to quote, both verified:
   - **Cicero**, *Dē optimō genere ōrātōrum* 14 (in the corpus): *nec convertī ut interpres, sed ut ōrātor … verbīs
     ad nostram cōnsuētūdinem aptīs … nōn verbum prō verbō necesse habuī reddere, sed genus omne verbōrum vimque
     servāvī.*
   - **Castellio, *Defensio* pp. 15–17**: the Spirit dictates the matter and leaves the words and the language free
     (*Rēs enim dictat Spīritus, verba quidem et linguam loquentī aut scrībentī līberam permittit*). So the apostles
     wrote Hebraisms from habit, and a translator need not keep them.

   In modern terms this is what Eugene Nida called **dynamic (functional) equivalence**, as against formal
   equivalence. It is also the first of Schleiermacher's two methods (1813), which moves the author toward the
   reader, what Lawrence Venuti calls **domestication**. Beza's position is the other method. That comparison is
   mine; no source read here makes it. I'd put Cicero and the Moses title in the Latin preface, and the modern
   terms in the English README, since *æquivalentia dynamica* in Latin would read as jargon.
4. **The French Bible.** It is mentioned only in a parenthesis. It deserves a sentence:
   - *La Bible nouvellement translatée* (Basel, Hervagius, March 1555), dedicated to Henri II (Mahlmann-Bauer), for
     readers without Latin;
   - written in everyday French (Mahlmann-Bauer), which Henri Estienne mocked as a beggars' language (Engammare,
     Ascona abstract);
   - unlike the Latin, never reprinted in his lifetime (Mahlmann-Bauer).
5. **How he died.** Of a long illness. Buisson (II:263) gives what was said at the time: a heart complaint or a
   wasting disease, which common opinion put down to privation and overwork; then a lingering fever with violent
   stomach pains. He seemed to recover on a milk diet, then relapsed and died within days. His friend the physician
   Theodor Zwinger wrote: *atrophiā correptus, quam assiduīs studiīs, cūrīs et vigiliīs … contrāxerat*. Zwinger
   dates the death *cal. Jan.* (1 January 1564) against everyone else's 29 December. A friend wrote that some
   thought him worn out more by grief of mind than by illness of body (Buisson II:263 n. 2). Proposed: *morbō
   diūturnō, quem studiīs, cūrīs, vigiliīs contrāxerat, cōnsūmptus*.
6. **"We know nearly all the stories."** Agreed, it assumes too much. Make it conditional: *Quī historiam sacram
   jam patriō sermōne nōvit, verba Latīna ex rēbus facilius intelleget.* Also drop "more than half a million words":
   the figure comes from the README and I haven't counted it.
7. **Sloppy or imprecise writing.** See the style list in §1. The worst are *Ad hoc ipsum*, *litterīs ērudītus*,
   *Inde … oppugnāvērunt*, the broad claim about church words, and the ( ) row.

## 3. What a Castellio scholar would say

**Inaccuracies or over-simplifications**
- **Why he left Geneva.** The draft gives only the Song of Songs. The ministers' certificate also disputed his
  reading of Christ's descent into hell (Mahlmann-Bauer; Kaegi). And on 30 May 1544 he publicly attacked the
  ministers' pride before the *congrégation*, which is what forced the break (Buisson I:211). Leaving that out makes
  him a passive victim.
- ***De haereticis* is a collection, not a treatise by one hand.** Its pieces stand under several names (Bellius,
  Georg Kleinberg, Basilius Montfort: Mahlmann-Bauer), and some attributions are disputed (Zahnd n. 30, a case for
  David Joris). That it also gathers opinions of earlier authorities (Luther, Brenz, Erasmus, the Fathers) is
  general knowledge, not yet seen in a source here. *librum ēdidit* should be *librum … collēgit et ēdidit*.
- **The quarrel with Calvin was about more than heretics:** also the translation itself, and above all
  predestination (Zahnd 375). The Romans 9 annotation against predestination was cut from the 1554 Bible by the
  Basel censors. Beza demanded that the first edition be destroyed. The note was restored only in the 17th century
  (Buisson II:56–58; Mahlmann-Bauer). It is a famous episode and the draft omits it.
- **The two textual states.** The edition now prints an Old Testament that Bünemann pulled back toward 1551, and a
  New Testament from the 1573 revision. A scholar will notice the mismatch. The preface should say so plainly, in
  one sentence, as a choice.
- **The name.** The draft says he called himself *Castalio*, then calls him *Castelliō* throughout without
  explaining. 1573 and his own books have *Castalio*; *Castellio* is the Leipzig editions' form, and it is this
  edition's title. One clause covers it.
- ***corrēctor*** is Buisson's "probably".
- **The memorial.** It is anonymous, and printed by Perna. The draft quotes it as if it were a verdict.

**Notable omissions**
- **The Apocrypha and the Josephus supplement.** Castellio translated the deuterocanonical books (*Admonitio*:
  Judith, Wisdom, Ecclesiasticus, Baruch, Maccabees, from the Greek; 4 Esdras from Latin into Latin) and set Josephus
  between the Testaments. A Castellio Bible without them is not his whole Bible. The preface should say whether they
  will come (M7).
- **His candour as a translator.** The *Admonitio* says names of plants and animals are guesses (*prō certā habērī
  nōlumus*); readers may skip his notes; when he says he does not understand a passage, he means it. The Aramaic
  chapters of Daniel and Ezra he translated from others' versions, *quoniam Syriacum sermōnem nōn didicimus*. This
  is the most attractive thing about him for a modern reader, and it gets half a sentence.
- **The dedication to Edward VI.** Why England: a refuge for the persecuted, and a boy king learning Latin. Its
  plea against persecution is the first statement of the argument of *De haereticis* (Mahlmann-Bauer: "ne iam
  damnemus alius alium"). An excerpt of it was reprinted inside *De haereticis* (Bach, Ascona abstract).
- **Montaigne** (*Essais* I.34/35), on the shame to his age that Castalio was left to starve. It is the best-known
  sentence about him, and it is about his poverty, not Servetus (Gomez-Géraud).
- **The modern picture.** Zweig's *Castellio gegen Calvin* (1936) made him a hero against tyranny; Buisson made
  him a liberal Protestant. Modern scholars (Gomez-Géraud, Zahnd) warn against both images. A preface that leans
  on Calvin and Servetus repeats them. Mention them only to set them aside, or leave the reader to the book list.
- **Verse numbers.** 1573 numbers the verses; this edition renumbers them to the KJV. Whether 1551 had numbers is
  not checked here (the README says the 1553 New Testament has none).
- **Further reading.** One short list (Buisson; Guggisberg; Gomez-Géraud's 2013 volume, which reprints the 1551
  preface and the *Defensio*) would let the preface stay short.

**Things to cut or shrink**
- Melanchthon's and Humphrey's praise. One witness is enough; Humphrey's question is the better line.
- The list of five reprint cities. "Reprinted until about 1780, at Leipzig for schoolboys" says what matters.
- The driftwood story. It is vivid, but it comes from Calvin's accusation, and the reply needs Calvin's book to
  make sense. Montaigne's sentence makes the same point with more authority.

## 4. Proposed outline for the third draft

1. **Ad lēctōrem** (short). Castellio's aim (*eādem operā pietās cum Latīnō sermōne*); the Moses title. How to
   read it: the Leipzig classroom method, put conditionally.
2. **Dē vītā** (two paragraphs). Savoy, Lyon (Latin and Greek; *Castalio*), Calvin, Geneva and the real reasons
   for the break; Basel, poverty (Montaigne), Greek; Servetus and *De haereticis* (an anthology); predestination and
   the Romans 9 note; Beza's charges, the accusation of 1563, the long illness and death. The memorial, presented as
   Perna's tribute. Works in one sentence, with the French Bible given its own.
3. **Dē interpretātiōne** (two paragraphs). Against the Vulgate and the word-for-word versions; Cicero's principle
   and Castellio's *rēs dictat Spīritus*; classical vocabulary; candour; Beza; the return to church words, and what
   remained (*collēgium*, *fānum*); reprints for schools.
4. **Ratiō hujus ēditiōnis.** The two bases, and the mismatch said plainly; the name *Castelliō*; spelling,
   macrons, layout, verses (KJV), capitals, names; what is left out (notes, *argūmenta*, Josephus, the Apocrypha
   for now); footnotes.
5. **Notæ**: ⟦ ⟧ and [ ] only, the latter noting 1 John 5:7–8.
6. **Librī legendī** (optional): three or four titles.

That is about 1,000 words, a page longer than now, with the calques in §1 replaced.

## 5. Second Latinity pass (draft 3, sentence by sentence)

Every collocation and construction in draft 3 was tested with `latin attest`, and the doubtful word senses were
looked up in Lewis & Short (`latin ls`). The changes below are now in `docs/front-matter.md`.

### Changed

| Draft 3 | Problem | Evidence | Now |
|---|---|---|---|
| *Eōdem cōnsiliō etiam nunc legī possunt* | the subject (*Biblia*) is two sentences back; "be read with the same plan" is loose | — | *Ad eandem rem etiam nunc ūtilia sunt* |
| *historiam sacram* | *historia sacra* is late (Sulpicius Severus on) | T4 only | *rēs in Bibliīs nārrātās* |
| *cēterī Latīna tacitī sequēbantur* | *sequī* "follow along in a text" is unattested | — | *cēterī eadem Latīnē tacitī legēbant* (*tacitus legere*: T2, T2.5) |
| *posteriōrēs ēditiōnēs vocant, unde hujus ēditiōnis titulus* | *ēditiō* twice in one clause; title pages print a name, they don't "call" him anything | — | *posteriōrēs typographī scrīpsērunt, unde nostrī librī titulus* |
| *tam pauper ut …* | the adjective hangs without a verb | — | *tamque pauper erat ut …* |
| *quod Castaliō ita dēcessisset* | switches the name form mid-text | — | *Castelliō* |
| *Calvīnum et Bēzam nec minus offendit quod …* | "no less" than what? The offence of *De haereticis* was only implied | — | *Quō librō Calvīnum et Bēzam graviter offendit, nec minus quod …* |
| *adnotātiōnem ejus in nōnum ad Rōmānōs caput* | compressed and ambiguous (*ad Rōmānōs* is the letter's title) | — | *adnotātiōnem quam ad caput nōnum epistulæ ad Rōmānōs scrīpserat* |
| *exsecuērunt* | *exsecāre* is to cut out surgically; nothing for a leaf taken from a book | — | *exēmērunt* (*eximere ex*: T1 ×2, T2.5) |
| *morbō diūturnō … contrāxerat* | *morbum contrahere* is T4 only; *diūturnus morbus* has one T3 hit | T4; T3 ×1 | *longō morbō cōnsūmptus, quem ex studiīs, cūrīs, vigiliīs nactus erat* (*longō morbō*: Seneca; *nactus est morbum*: Nepos, *Atticus* 21, of his last illness) |
| *diē 29 mēnsis Decembris* | a modern calendar date | — | *a. d. IV Kal. Jān.* (29 December, in the year already given) |
| *Biblia etiam Gallicē convertit* | *Gallicē* is Erasmus only | T2 only | *in sermōnem Gallicum convertit* (cf. *in Latīnum sermōnem*: Livy, Columella, Quintilian) |
| *quī Latīnē nescīrent* | *Latīnē nescīre* is Erasmus only | T2 only | *quī Latīnē nōn scīrent* (*Latīnē scīre*: Cicero, *Pro Caecina* and *Phil.* V; Terence; Livy) |
| *…, sermōne cotīdiānō, quem …* | the ablative dangles far from its verb | — | *sermōne ūsus est cotīdiānō, quem …* |
| *per duo amplius sæcula* | *duo sæcula*, "two centuries", is late | T4 only | *ducentōs amplius annōs* |
| *Gallicē Conseil …* | as above | — | *sermōne Gallicō Conseil …* |
| *Latīnē legēbātur aut vetus interpretātiō … aut novæ quædam* | unbalanced (a singular nominative paired with an elliptical plural), and *Latīnē legēbātur* reads as "was read aloud in Latin" | — | *Biblia Latīna erant aut vetera … aut ab aliīs nūper conversa; quæ omnia barbarē loquī …* |
| *in epistulā …, quam Bibliīs præposuit* | *præpōnere* (a letter before a book) is late | T4 only | *in epistulā quā Biblia Eduardō Sextō … dēdicāvit* |
| *Eādem ratiōne Cicerō* | echoes *ratiōnem dūxisse* just before, in another sense | — | *Sīc Cicerō quoque* |
| *Hebraismōs enim apostolōs …* | *enim* claims a cause that the Cicero sentence doesn't give | — | *Apostolōs autem Hebraismōs … scrīpsisse Castelliō dīcit, neque eōs ab interprete retinendōs* |
| *Opus Eduardō … dēdicāvit* | the dedication was now mentioned twice | — | *Eduardum autem amīcīs suādentibus dēlēgerat, quod …* |
| *Aliī eum valdē probāvērunt, ut Laurentius …:* | *ut* + a quotation with no verb of speaking | — | *in quibus Laurentius Humfredus Anglus: …* |
| *sæpe recūsa sunt* | *recūdere* is not in Lewis & Short; "reprint" is a coinage | — | *iterum atque iterum excūsa sunt* |
| *Posteā Buisson et Zweig* | *posteā* is vague (1892, 1936) | — | *Recentiōrēs, ut Buisson et Zweig, …* |
| *cum posteriōrēs omnēs Pernæ errōrēs prōpāgāvisse vidēret* | *posteriōrēs* lacks its noun | — | *cum Pernæ errōrēs in omnēs posteriōrēs ēditiōnēs prōpāgātōs esse vidēret* (Bünemann's own verb) |
| *quam Castelliō vīvus cūrāvit* | *cūrāre* "edit" is not classical | — | *ēdidit* |
| *fōrmæ similēs* | *fōrma* "word form" is rare and late | T3 ×3 | *quæ similēs videntur* |
| *carmina per versūs disposuimus* | *per versūs* has no classical support (one Plautus hit, in another sense) | T1 ×1 | *carmina versibus distīnximus* |
| *stant prō parenthesī ēditiōnis annī 1573* | *parenthesis* is a figure of speech (Quintilian), not a punctuation mark; the Neo-Latin *lūnula* can be avoided | Quintilian; T4 | *eādem notā ūsī sumus quā ēditiō annī 1556; ēditiō annī 1573 aliā ūtitur* |

### Kept, with their evidence

- **Classical collocations**:
  - *ex Græcō in Latīnum convertere* (Cicero); *ex rēbus intellegere* (Cicero ×3).
  - *eādem operā* (Plautus; Castellio's phrase); *sine magistrō* (Cicero ×2).
  - *litterīs Græcīs ērudītus* (Cicero ×4); *aliter sentīre* (Cicero, letters ×6); *dissentīre ab* (Cicero, Seneca).
  - *in collēgium cooptāre* (Cicero in Quintilian; Seneca); *lūdī magister* (Cicero).
  - *victum quærere* (Terence); *dēdecorī esse* (Cicero, Sallust, Livy); *cibī satis* (Cicero).
  - *vīvum combūrere* (Plautus, Cicero ×4); *dēferre ad senātum* (Cicero); *invehī in*.
  - *nostrā ætāte* (Cicero); *sermō cotīdiānus* (Cicero ×4); *perfugium esse* (Cicero ×6); *prō certō habēre*
    (Cicero ×7); *ūsūrpāre vocābula* (Cicero); *eximere ex*; *conferre cum*.
  - *verbum prō verbō* and *nōn ut interpres, sed ut ōrātor* (Cicero, *Dē optimō genere ōrātōrum* 14).
  - *ut nunc fit* (Cicero); *accommodāre ad* (Cicero); *hōc titulō* (Pliny, Quintilian, Gellius); *amplius* with
    numbers.
  - *juxtā pōnere* (T3: Sallust, Nepos, Columella).
- **Late or Neo-Latin words kept on purpose**, since a classical substitute would mislead:
  - *ēditiō* "edition" (post-Augustan: Quintilian, Pliny; L&S).
  - *excūdere* "print" (classical only as "compose", Cicero); *typographus*.
  - *adnotātiō* (Gellius); *versiculus* "verse" (classical "short line").
  - *prædēstinātiō*, *Hebraismus*, *paragraphus*, *macrō*, *lexicon*, *majusculus* (Erasmus).
  - *Vulgāta* as a name; *cēnsor* for a book censor.
  - *dēdicāre* of a book (Quintilian's *librōs … dēdicāvērunt*, T3, means "devoted"; the dedication sense is later).
- **Names**:
  - Gaffiot's forms where he has them: *Sēbastiānus*, *Fūrius*, *Hierōnymus*, *Argentorātus*, *Lugdūnum*,
    *Calvīnus*, *Genāva*, *Parīsiī*.
  - Loans marked on the penult only when the source stresses it: *Pagnīnus*, *Opōrinus* (Greek ω); *Humfredus*
    unmarked, since the English stresses the first syllable.
  - Modern surnames left undeclined (*Bünemann*, *Buisson*, *Zweig*), like *Fēlīcis Gaffiot* in the colophon.

- **Quotations stay in Castellio's and Beza's own words**, even where these are not classical (*trānslātiō*,
  *Hebraismus*, *Latīnior*, *Sacræ litteræ*). They are quotations, normalized only in spelling.

## 6. Adjusted after Nathan's note (2026-11-13)

The house rule: classical grammar, word order and idiom where they fit naturally, but no obligation to classical
vocabulary when a later term is more precise; modern dates; no clumsy circumlocutions; fewer repetitions, but not
at the cost of clarity.

- **Precise later terms restored.**
  - *historiam sacram* (for *rēs in Bibliīs nārrātās*).
  - *Gallicē vertit* (for *in sermōnem Gallicum convertit*) and *Gallicē Conseil …*.
  - *sæpe recūsa sunt* (for *iterum atque iterum excūsa sunt*).
  - *parenthesin* in the *Notæ*: *In 1Jo 5,7–8 sīc etiam ēditiō annī 1556; illa annī 1573 parenthesin habet.*
- **Modern date.** *diē 29 mēnsis Decembris* (for *a. d. IV Kal. Jān.*).
- **Kept from the second pass, because the grammar or the plain sense needed them:**
  - the balanced sentence on earlier Latin Bibles;
  - *tamque pauper erat ut*, *Quō librō … nec minus quod*;
  - *sermōne ūsus est cotīdiānō*, *in quibus Laurentius*, *Sīc Cicerō quoque*;
  - *Apostolōs autem …*, *ēdidit*, *exēmērunt*, *longō morbō … nactus erat*;
  - *Latīnē nōn scīrent*, *quæ similēs videntur*, *ducentōs amplius annōs*.
  - *carmina per versūs dīgessimus* replaces the stiff *versibus distīnximus*.
- **Repetition reduced where the Latin reads naturally without the word:**
  - *Castelliō* from 17 to 11. The life opens *Annō 1515 … nātus est* under its heading; *ipse* and *ille* stand
    where the subject is already plain, but not after Beza's quotation, where *ille* would read as Beza.
  - *ēditiō* from 14 to 10: *cum Lipsiēnsī annī 1750*, *illam secūtī sumus*, *in omnēs posteriōrēs*.
  - *sermō* from 10 to 7: *Bibliīs tuā linguā scrīptīs*.
  - *convertere* from 6 to 4: *vertit* twice.
  - Also: *Eōdem annō* no longer opens two sentences close together (the second is *Tum*), and *quoque* no longer
    falls twice in the French Bible sentence.
- **Montaigne.** *quod vir doctissimus ita dēcessisset*: Montaigne's "deux très excellents personnages en savoir"
  (Buisson I:248).
- **Years in Arabic numerals** (*annō 1515*): decided by Nathan, 2026-11-13. The remaining *ēditiō* and *Biblia*
  are the subject itself, and a synonym would only blur which printing is meant.

## 7. Nathan's critique of the third version, point by point (2026-11-13)

| Point | Answer | In the fourth version |
|---|---|---|
| Vague *rēs* (*Ad eandem rem*) | Not wrong Latin (*ad eam rem* is Ciceronian), but vague here, and the subject was two sentences away | *Nec minus hodiē Biblia ejus prōsunt iīs quī Latīnē discunt.* *rēs* remains only where it means "the matter" (Castellio's and Cicero's own quotations; *verba ex rēbus*) |
| *Latīnus* three times in sentence 2 | Agreed | *puerōs … ērudīrī*; *Latīnior* and *Latīnō* stay, since they belong to Castellio's own phrase |
| His French name | Added | *Castelliō, Gallicē Sébastien Châteillon* (Buisson I:1–2: Chatillon, Chateillon) |
| How he learned Hebrew | Unknown: Buisson says "on ne sait comment" (I:246); Renan, in a letter Buisson prints, says he knew it "très bien" (I:316) | *Hebræam linguam quō modō didicerit nescītur, sed eam bene scīvit.* |
| Who Servetus was | Added | *medicus Hispānus quī Trīnitātem negābat, … Calvīnō īnstante vīvus combustus est* |
| Book titles | Italics, sentence case (capital only on the first word and proper names), the convention of modern Latin and of Gaffiot. Title case is an English habit and would look foreign in Latin. Inflected titles keep their italics | All titles in italics |
| *nōn nisi annō 1612 ēditō*: published posthumously? Did Calvin read it? | Yes: 49 years after Castellio's death, 48 after Calvin's (1564). It circulated in manuscript (Zahnd 377 n. 33), but no source says Calvin saw it | *quem manū scrīptum quidem legēbant, sed vīvus ēdere nōn potuit (prīmum excūsus est annō 1612)* |
| *Bēza* or *Beza* | Short. No dictionary marks it, and French *Bèze* has a short open e. The draft mixed the two | *Beza* throughout |
| Who Calvin and Beza were | Added in apposition at first mention | Calvin *quī tum Genāvā expulsus ibi vīvēbat*; Beza *Calvīnī discipulum et posteā successōrem* |
| The Romans 9 note | It was Castellio's own note in his own Latin Bible (1554), against Calvin's doctrine of predestination | *in ipsīus Bibliīs annī 1554 adnotātiōnem … quā Calvīnī doctrīnam impugnābat* |
| *ex studiīs, cūrīs, vigiliīs nactus erat*: medically accurate? | It is not a diagnosis: it is his friend Zwinger's explanation (*atrophia … quam assiduis studiis, curis et vigiliis … contraxerat*); the symptoms were a slow fever and stomach pains | Attributed: *quem Theodōrus Zwingerus medicus, amīcus ejus, studiīs, cūrīs, vigiliīs contractum esse scrīpsit* |
| The memorial: *illīus*, *hujus* | *Lemannō cælō* (Lake Léman) is Geneva, *Rauracō* (the Rauraci) is Basel; *illīus* is Geneva's harshness, *hujus* Basel's charity | A gloss before the quotation: *ubi Lemannus lacus Genāvam, Rauracī Basileam significant*. The quotation is introduced as Perna's |
| Henri Estienne | The Genevan printer and scholar; he printed Beza's *Responsio* (1563) | *Henrīcus Stephanus, typographus Genāvēnsis, "jargon des gueux" appellāvit* (Buisson I:434) |
| *nisi nostrā ætāte*: reprinted? | Yes: Bayard, 2005, preface by P. Gibert and J. Roubaud (*Le Temps*; Gomez-Géraud in *Camenae* 3) | *ante annum 2005 iterum excūsa nōn sunt* |
| Too much *nōn nisi* | Agreed; none remain | — |
| *Biblia Latīna erant aut vetera …*: clunky; translations before the Vulgate? | Rewritten as a short history: the first Christians' translations from the Greek, Jerome's revision and new version, the 16th-century versions | A new opening paragraph for the section |
| Who Furió Ceriol was | A Spaniard who wrote on translating the Bible into the vernacular (the 1573 *Iudicia* cites that book) | Added in apposition |
| Mixed indirect and direct speech in the Furió sentence | Agreed, heavy. Now one indirect statement and one direct quotation, with its source named | *quās omnēs … barbarē loquī questus est, dōnec Castelliō prōdiit: "Latiō sermōne loquuntur / Biblia nunc tandem Castaliōnis ope."* |
| *scrīpsisse dīcit*: who? | Castellio (*Defensio*) | *Apostolōs autem Castelliō … dīcit* |
| *Eduardum … dēlēgerat* | Meant: chose him as dedicatee | *Eduardō autem Biblia ideō dēdicāvit, amīcīs suādentibus, quod …* |
| *ferrō, flammā, undīs*: a quotation? | Yes: *ferro & flamma & undis sævimus*, "we rage", counting himself among the persecuting Christians | Quoted exactly, with *sē nōn exceptō* |
| Beza's point unclear | His fear was that changing the church's words for elegance would cost the faith itself; the full sentence says so | *… Cicerōniānī ēvādēmus, et paulātim ipsārum quoque rērum possessiōne dēpellēmur*, introduced by *ratus sīc ipsam fidem in perīculum venīre* |
| *baptisma, baptīzāre, angelum*: parallelism | Rewritten as a list of pairs | *baptisma prō lōtiōne, angelum prō geniō, …* |
| Beza's praise; reconciled? | He praised the act (*factum ipsius laudo*) and condemned the reason; never reconciled: his *Responsio* (1563) led to the accusation, and his 1598 New Testament still attacks Castellio | *Beza factum laudāvit, causam … improbāvit; in grātiam numquam rediērunt* |
| He kept more than *collegium*; theological precision? | Yes. What returned are mostly words that carry doctrine: *baptisma*, *angelus*, *ecclesia*, *gratia*, *caro*, *filius hominis* (1556); 1573 adds *sanctus*, *peccatum*, *fides*. What stayed are names and institutions: *collēgium* for the synagogue, *Jōva*. Castellio himself gives the reason as not giving offence (*Defensio* p. 12); the doctrinal pattern is our observation, hedged with *ferē* | The list of pairs, then *collēgium … et Jōvam … retinuit* |
| The point of Humphrey's quotation | It answers Beza: if we write elegant Latin elsewhere, why should Scripture be barbarous (*Scōtī* = the scholastics)? | Now set against Beza, with his argument and a gloss on *Scōtī* |
| Why the Bible faded after 1780; why Castellio faded | No source read here says why the reprints stopped. Likely causes (not for the preface): the end of Latin as the language of the schools, and the neo-humanist turn to the ancient authors themselves. His fame changed rather than faded: known in the 18th century for the Bible and the Servetus affair (Gomez-Géraud, summarizing Sandrier), he was remade in the 19th–20th as a hero of toleration (Buisson, Zweig) | A sentence on the 18th-century reputation and the later image |
| Why scholars temper the celebration | The "apostle of toleration" is anachronistic. He asked Christians for charity, not for toleration as a right (Mahlmann-Bauer). Sixteenth-century humanism did not mean modern tolerance (Zahnd). The writings on heretics are a small part of a life spent teaching and translating (Gomez-Géraud) | The reasons are now given |
| *sequimur*: royal we? | Both are natural. Castellio mixes *ego operam dedī* and *dūximus*; Bünemann writes *ego*. For a signed preface by one editor, the singular is more candid | Changed to the first person singular; easy to reverse |
| *illam secūtī sumus*: antecedent? | Ambiguous; fixed | *ēditiōnem annī 1556 secūtus sum* |
| OT nearer the first edition, NT the last: defensible? | That sentence was wrong. The 1738 Old Testament keeps the later church words (*angelus* in Genesis 28–50, Exodus); Bünemann corrected from 1551 only the printers' errors that had crept in after 1573. Castellio's own revisions were mostly in the New Testament: his *Defensio* says the Old was already printed when he changed the words. So both Testaments give his later vocabulary | *Itaque … postrēmæ* cut; now *In utrōque Fœdere vocābula ecclēsiæ quæ Castelliō restituit leguntur* |
| *ut vōcēs rēctē prōnūntientur* | It made sense but was vague | *ut syllabārum quantitās appāreat* |
| *interpūnctiō* or *pūnctiō*? | *interpūnctiō*: Cicero's word for punctuation. *pūnctiō* is a pricking (medical) | Kept |
| Why KJV numbering | Most English Bibles, concordances and commentaries use it, so any verse can be found and compared | Said in the text |
| *sine numerō* for Psalm titles | Cut | *suprā prīmum versiculum stant* |
| One name in both Testaments: unclear | Rewritten with an example | *quī in utrōque Fœdere idem homō est, eōdem nōmine appellātur quō in Veterī, ut Nōa, nōn Nōē* |
| *Librōs quōs Hebræī nōn habent*: the Apocrypha? | Yes: the deuterocanonical books, which Castellio translated from the Greek (*Admonitio*) | Written for the final edition: *et ipsōs dedī*. Their place is still open |
| *posteā addēmus* | Written for the final edition | — |
| *Ipse lēctōrēs sīc rogāvit*: who, where? | Castellio, in the *Ad lectores admonitio* set before the Bible (1551; 1573 canvas 17) | *In Admonitiōne ad lēctōrēs, quam Bibliīs præfīxit, Castelliō sīc rogat* |
| The 1 John 5:7–8 line in the *Notæ* | Cut | — |
| A fuller case for the edition | Added to *Ad lēctōrem*: extensive reading; few long texts macronized and normalized; closer to classical Latin than the Vulgate; for whom (learners past the grammar, teachers, devotional readers, Protestant Christians, lightly). And to *Ratiō*: why paragraphs rather than a verse per line | — |
| Plagiarism | Checked. Every quotation is from a public-domain source (Castellio, Cicero, Beza, Humphrey, Furió Ceriol, the 1573 memorial, Zwinger) and is attributed. Modern scholars (Buisson, Zahnd, Gomez-Géraud, Mahlmann-Bauer) are paraphrased, never copied, and credited in the sources table. Montaigne and Estienne are short attributed quotations. The English gloss translates our own Latin. The one modern phrase earlier borrowed nearly verbatim (Gomez-Géraud's "pédagogue, traducteur et écrivain" as *magistrum, interpretem, scrīptōrem*) is gone | — |

## 8. Nathan's critique of the fourth version, point by point (2026-11-13)

| Point | Answer | In the fifth version |
|---|---|---|
| A stronger opening | Open on Castellio's own boast, the title of the *Moses latinus* | “*Vidēbis, lēctor, Mōsem nunc dēmum et Latīnē loquentem et apertē.*” *Hōc titulō … ēdidit* |
| *Cūr id fēcerit* | Grammatical, but a weak, conversational start | *Causam ipse in Dēfēnsiōne … reddit* (*causam reddere*: T2/T3) |
| *obscēnīs*: his words? hyperbole? | His words: *autores Latinos quidem, sed magna ex parte obscœnos, & moribus noxios* (*Defensio* p. 9). He means the school authors of his day (the comic poets, Ovid and the like), whose subject matter he thought harmful to boys; it is a moralist's judgement rather than hyperbole, and Woll (1728) makes the same case | Quoted, in full: “*magnā ex parte obscēnīs et mōribus noxiīs*” |
| *Multa enim legere dēbent* | Clunky | *Multā enim lēctiōne opus est, et facilius legitur quod jam nōtum est* |
| *ēditiōnem in Veterī Fœdere* | Unnatural as a phrase ("edition in the OT") | *cujus Vetus Fœdus sequor* |
| *sed eam bene scīvit* | Clunky | *probē tamen nōverat* (*probē nōvisse*: Cicero, Erasmus) |
| *ibi lūdī magister* | Ambiguous (Strasbourg or Geneva) | *Genāvæ lūdī magister factus est* |
| *librō dēfenderat, librō* | Awkward | *Calvīnus Servetī supplicium scrīptō dēfenderat; huic Castelliō respondit librō …* |
| *quem manū scrīptum quidem legēbant* | Subjectless *legēbant* is unclear | *quī diū manū scrīptus circumferēbātur nec ante annum 1612 excūsus est* |
| The parenthesis *(prīmum excūsus est annō 1612)* | Not wrong, but parentheses read as notes; folded into the sentence | — |
| The quotation not set up | It now follows *In eō scrībit:* | — |
| *ex Bezæ librō dēlātus* | It hid the accuser | *Ādamus ā Bodenstein, crīmina ex Bezæ librō sūmēns, eum apud senātum Basiliēnsem accūsāvit* (Buisson II:257) |
| The memorial gloss: heavy, and odd after Basel's censorship | Agreed on both counts: the "kind Basel" of Perna's tribute sits badly beside the Basel censors and the Basel accusation, and it needed a gloss | The memorial is cut (it remains in `docs/editions.md`) |
| *jargon des gueux*: derogatory? | Yes: "beggars' cant", mocking the plain, popular French | Paraphrased: *ut mendīcōrum sermōnem dērīsit* (one fewer quotation) |
| *ducentōs amplius annōs* | Idiomatic: *amplius* with a number and no *quam*, an accusative of time (Cicero, Livy) | Kept |
| Formatting words cited as words | Yes: italics for mention (*genium*, *lōtiōnem*, *venit*) | Done |
| Too many direct quotations? | Yes. Quoted stretches down from 19 to 11 (not counting the “ ” in the layout paragraph): the memorial, Estienne, the *Admonitio* on animals and plants, the *Syriacum sermōnem*, Cicero's *verbum prō verbō* and Humphrey's line are now paraphrased or cut | — |
| *(Scōtōs scholasticōs dīcit)*; why scholars against Ciceronians? | A bracketed gloss is fine in a scholarly note but out of place in a preface. *Scōtī* are the followers of Duns Scotus, whose scholastic Latin humanists held up as the type of barbarism; Humphrey sets the polished Latin of the humanists (*Cicerōnēs*) against it | Humphrey paraphrased: *negāns eōs quī in cēterīs librīs ēlegantiam sequerentur in sacrīs barbarē scrībere dēbēre* |
| Are the restored and kept words a full list? | No, examples. Other changes: *sanctus* for *sacer*, *peccatum* for *vitiositas*, *fides* for *fiducia* (1573), and 1573 even moved some words the other way (*fanum* for *templum*) | *ut … ; alia retinuit, ut …* |
| *Beza factum laudāvit, causam … improbāvit* | Good Latin (antithesis in asyndeton), but clearer with *quidem … sed* | *Beza quidem factum laudāvit, sed causam ab eō allātam improbāvit* |
| *Biblia ejus*: Beza? | Ambiguous after Beza | *Castelliōnis Biblia* |
| *in ūsum studiōsæ juventūtis*: the point? | The title phrase was evidence of school use, but obscure. The Leipzig editions were not rewritten for students; they added an index of Latinity with German glosses (1738) and school-method prefaces (Vockerodt, Gesner) | Said plainly: *maximē in Germāniā, ubi in scholīs puerī ex eīs Latīnē discēbant* |
| *ob Biblia* | Yes | *ob Bibliōrum interpretātiōnem* |
| *Doctī hodiē*: e.g.? | Named | *ut Marie-Christine Gomez-Géraud et Ueli Zahnd* |
| *quæ similia videntur* | *quæ* had no noun; *verba* understood | *verba fōrmā similia, ut venit et vēnit* |
| *Fōrmam lēctiōnī continuæ aptam ēlēgī …*: clunky, poorly reasoned | Rewritten with the reason: the verse division (16th century) breaks sentences, so the text is in paragraphs by the sense, with small numbers kept for reference | *Versiculōrum dīvīsiō, quæ sæculō sextō decimō in ūsum vēnit, sententiās sæpe interrumpit; itaque textum … in paragraphōs secundum sententiam dīvīsī …* |
| Versification: concordances rather than the KJV | Agreed | *Versiculōs eōdem modō numerāvī quō plēraque Biblia Anglica et concordantiæ, ut quīvīs locus facile inveniātur et cum aliīs Bibliīs cōnferātur.* (The colophon still names the KJV.) |
| Why not *apocryphī*? | It works in Latin (Jerome uses *apocrypha*; Protestant Bibles head these books *Librī apocryphī*) and is clearer | *Librōs apocryphōs, quōs Hebræī nōn habent et ille ex Græcō vertit, et ipsōs dedī.* Catholic readers call them deuterocanonical; *apocryphī* is the Protestant term Castellio's tradition used |
| *Idem ego rogō*: a strong ending? | Flat. Better to end on Castellio's own words | *Restat ut idem ā lēctōre petam quod Castelliō in Admonitiōne ad lēctōrēs petiit: “…”* |
| The *Notæ* are only for the New Testament | Right: Genesis and Exodus have no brackets, footnotes or quotation italics, and the Old Testament's own marks (Castellio's *G.*, *L.*, *H.*) are dropped | Headed *Notæ in Novō Fœdere*; nothing to add for the Old |
| *Librī legendī* run together | Markdown joined the lines into one paragraph. Now a list, one book per line, surname first; the 2005 French Bible and Plath's 2019 edition of *Contra libellum Calvini* added | — |
| Repetition | *Castelliō* in all forms down from 25 to 18 in the new draft, by *ipse*, *ille*, *eum* where no other man is in view; kept where a pronoun could mean Beza, Humphrey, Cicero or Bünemann | — |


## 9. Point by point on the fifth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| 1546: from Hebrew and Greek? | No. The *Moses latinus* is the Pentateuch, from the Hebrew only; the old clause made it sound as if the 1546 volume drew on both | *quīnque librōs Mōsis ex Hebræō conversōs ēdidit, prīmam Bibliōrum partem; opus tōtum … prōdiit* |
| *obscēnīs*: pagan authors? against Cicero and Vergil? | The words are his (*Defensio* p. 9: *magna ex parte obscœnos, & moribus noxios*). He means the school authors, above all the comedies: the preface of the *Dialogi sacri* calls Cicero too hard for children and Terence and Plautus harmful to their morals (Buisson I:160). He was not against the classics as such: he edited Homer, Xenophon and Herodotus, and his own Latin follows Cicero | *ex Plautō, Terentiō aliīsque auctōribus*, so the reader knows whom he meant |
| *verba ex rēbus intelleget* | Not natural, and *rēs* is vague again. Cicero's idiom for inferring is *conjectūrā cōnsequī* (Cic. *Fam.* 6 and 12, *Cat.* 3) | *ignōta verba ex sententiā conjectūrā cōnsequētur* |
| *Paucī tamen …* muddled | It ran three claims into one sentence. Now in order: whom the edition is for; why a story already known is easiest; why Castellio rather than the Vulgate; what this edition adds | Paragraph rebuilt |
| *multā lēctiōne* twice | Gone; the one remaining phrase is *legendō* | |
| teachers, the devout, Protestants | The three were not parallel. Protestants are now a subset of the devout, with the reason | *Ūtilis etiam erit magistrīs et iīs quī Biblia pietātis causā Latīnē legunt, Prōtestantibus præsertim, quōrum …* |
| *apud Calvīnum habitāvit*: roommates? | He was a boarder (*pensionnaire*) in Calvin's house, which took in paying students (Buisson I:103–104) | *in domō Jōhannis Calvīnī habitāvit* |
| *Genāvā* three times | Now *Genāvam*, *Genāvēnsis*, *Genāvā*, in three different constructions; *exsul Argentorātī* carries Calvin's exile | |
| The descent into hell | Geneva's catechism took *descendit ad inferos* as Christ's anguish of conscience before God's judgement on the cross. Castellio granted that the doctrine was pious but denied that the creed meant it, since the creed puts the descent after the burial (the ministers' certificate and Calvin's letter to Viret, Buisson I:198–201) | None |
| Who is Montānus? | Montaigne; *Montanus* is his Latin name but opaque to readers | *Michaēl Montānus, Gallicē Montaigne*, as for Châteillon |
| *Proximō annō ipse* | Ambiguous after Servetus | Calvin's defence now gets its own sentence, then *Castelliō vērō* |
| Calvin's book unnamed | It has a name: *Calumniae nebulonis* (January 1558, "the slanders of a scoundrel"), on providence and predestination. Both are now named | *librum Calumniæ nebulōnis*; the *Defensio* of 1562 now stands between them, since Beza's *Responsio* answers it |
| *Ādamus ā Bodenstein* | Not quite. In his Latin dedication of 1560 (Paracelsus, *De vita longa*) he writes *Adam ab Bodenstein … S. D.*, genitive *Adami*: so *Adamus ab Bodenstein*, with his own *ab* ([Theatrum Paracelsicum](https://www.theatrum-paracelsicum.com/Dedication,_1560-02-01,_Adam_von_Bodenstein_to_Duke_and_Magistrate_of_Venice)) | *Ādamus ab Bodenstein* |
| 29 December 1563 | Buisson, Mahlmann-Bauer and Gomez-Géraud all give it; only French Wikipedia hedges, without a source. It is the best date | None |
| The works after his death? | Better woven in. The list read like an appendix after the death scene. Now each work stands where it was written: the *Dialogi* at Geneva; the Latin and French Bibles at Basel; the *Defensio* in the quarrel with Beza; the *Conseil* and *De arte dubitandi* in his last years, before the death. The French Bible's fate (Estienne's jibe, no reprint before 2005) moves to the reception paragraph, set against the Latin's many reprints | Life section in five paragraphs |
| *Ipse, in epistulā* | Could be Ceriolanus | *Castelliō ipse*; the Hebraisms sentence then says *In Dēfēnsiōne autem docet* so it cannot be Cicero |
| *Aramæā* | Gaffiot heads *Ārămæī*: long first A | *Āramæā* |
| *angelum genium* vs *angelum prō geniō* | The first used *angelum* for the thing and *genium* for the word, which is correct but looks inconsistent. Now both lists cite words on both sides, in mirror order | *genium prō angelō, lōtiōnem prō baptismō …*; later *baptisma prō lōtiōne …* |
| *ex eīs* | | *ex iīs* |
| *ut Gomez-Géraud et Zahnd* | Names with *ut* read like an example list. Dropped: their books are in *Librī legendī* | *Doctī nostræ ætātis monent …* |
| *imāginem temperant* | Not attested; *imāgō* for a reputation is a stretch | *monent* with the two claims as indirect statement |
| *vertendum* alone | Means "turning" as much as "translating" | *plūrima aut scholārum causā scrīpta aut ex aliīs linguīs conversa esse* |
| *vocābula ecclēsiæ* | Neither man uses the phrase; Castellio says *Græcum vocabulum*, Beza what *Latina Ecclesia praetulit*. The usual Neo-Latin term is *vocābula ecclēsiastica* (Gaffiot heads *ecclēsiasticus*; later Latin, but more precise) | *vocābula ecclēsiastica* in both places; the earlier *quæ ecclēsia ūsūrpābat* becomes *quæ Chrīstiānī ūsūrpābant*, to keep *ecclēsia* for the word itself |
| The paragraph sentence | Clunky ablative absolute | *Versiculī … sententiās sæpe interrumpunt; itaque textum in paragraphōs dīvīsī, ut in cēterīs librīs fit, numerōsque versiculōrum parvōs relīquī, quibus locī inveniantur.* |
| *notās quibus verba ex aliīs interpretātiōnibus sūmpta sēcrēvit* | Castellio marks words he added from another version where the original lacks them: *G. lect. … H.* in the Old Testament (from the Septuagint, e.g. Gen 21:9) and *L. … G.* in the New (from the Vulgate, e.g. Jas 5:3 *Pœnam*). We drop the marks and keep the words (`docs/editions.md`) | *Omīsī etiam notās quibus verba sēcrēvit quæ, cum in Hebræō aut Græcō nōn essent, ex Græcā Veteris Fœderis aut ex Latīnā Novī interpretātiōne addiderat; verba ipsa retinuī.* |
| Broaden the *Notæ* | Done: headed *Notæ*; the two bracket rows say *In Novō Fœdere*; italics are quotations from earlier books of the Bible; footnotes mark departures from the Hebrew or Greek. The Old Testament edition now has a *Notæ* with the two rows that apply. `brief.md` (decision 53) still speaks of the Greek only | Table and variants |


## 10. Point by point on the sixth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *prīmam Bibliōrum partem; opus tōtum …* muddled | Agreed: two sentences, the second naming both originals | *… quīnque librōs Mōsis ex Hebræō conversōs ēdidit. Biblia tōta, ex Hebræō et Græcō conversa, Basileæ annō 1551 prōdiērunt.* |
| *quō modō* | Gaffiot heads *quōmodo* as one word | *quōmodo* |
| Italicize French names? | No. Italics here mark titles and words cited as words; a person's or place's name stays roman in any language (Montaigne, Châteillon, Saint-Martin-du-Fresne, Bünemann). A French title (*Conseil à la France désolée*) is italic as a title | None |
| Which book did he refute? | Calvin's defence of Servetus's execution, the *Defensio orthodoxae fidei* of 1554. The 1612 title says so: *Contra libellum Calvini in quo ostendere conatur haereticos jure gladii coercendos esse*. The previous sentence said *scrīptō*, which left *librum* without an antecedent | *Calvīnus Servetī supplicium librō dēfendit … deinde ipsum illum Calvīnī librum refūtāvit* |
| *tuitus est* | Correct but stiff, and it avoided *dēfendit* only to dodge *Dēfēnsiōne dēfendit*. The real relation is an answer to Beza | *Bezæ autem, quī interpretātiōnēs ejus … reprehenderat, Castelliō annō 1562 Dēfēnsiōne respondit; contrā quam Beza annō 1563 Respōnsiōnem ēdidit* |
| *nē cōnscientiās cōgerent* | A calque of *forcer les consciences*; *cōgere cōnscientiam* has no attestation, and a Latin reader would hesitate | *nē quem invītum ad religiōnem cōgerent* ("to force no one into a faith against his will") |
| *Sanctes* or *Xanthus*? | *Sanctes*: his own Bible of 1528 has *Sancte Pagnino* on the title page (ablative of *Sanctes*). *Xanthus* is a later variant some reference works give | None |
| *tamquam mendīcōrum dērīsit* | Elliptical: the reader has to supply *sermōnem* | *quem … irrīdēns mendīcōrum sermōnem vocāvit* |
| *plūrima aut scholārum causā scrīpta …* | Agreed, a step back: a catalogue where a judgement was wanted. Gomez-Géraud's point is that he was above all teacher and translator | *… neque tam disputātōrem dē hæreticīs quam interpretem et magistrum fuisse*, which answers *prīmum tolerantiæ dēfēnsōrem* in the sentence before |
| *omīsī. Omīsī etiam* | Anaphora is good Latin when it carries emphasis; here it only patched a long list | One sentence with *item* |
| The marks sentence | Shorter, and the reader already knows the Vulgate from *Ad lēctōrem* | *item notās quibus verba ex Septuāgintā interpretibus aut ex Vulgātā addita indicāvit; ipsa verba retinuī.* The single-Testament editions name only their own version |


## 11. Point by point on the seventh version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *historia sacra*: Bible stories or church history? | The biblical narrative. That is its sense from Sulpicius Severus's *Historia sacra* (Creation to his own day, but chiefly the Bible) through the school manuals; church history is *historia ecclēsiastica* (Eusebius in Rufinus's Latin). The context (*Vulgāta eandem historiam nārrat*) fixes it | *suā linguā* dropped: the reader may know the stories in any language, or from childhood |
| *et verbīs et locūtiōnibus* | Yes, "words and phrases", and it missed the main difference, which is syntax and order. The Vulgate mostly keeps the Hebrew and Greek idiom and word order (Jerome himself says that in Scripture "even the order of the words is a mystery", *Ep.* 57.5); Castellio recasts the sense as a Roman would write it | *sed Hebræōrum Græcōrumque locūtiōnēs et verbōrum ōrdinem plērumque servat; Castelliō sententiam Rōmānō mōre effert* |
| *sermō* overused | Five times in the first two paragraphs. Now: once in Castellio's quotation, once for Bünemann's *patriō sermōne*. Later: *Latiō sermōne* (quotation), *sermōne cotīdiānō* | *legendō prōficere*; *Rōmānō mōre*; Estienne *mendīcōrum esse dīxit* |
| *Ūtilis etiam erit*: masculine? | *ūtilis* is masculine and feminine alike; the intended subject was *ēditiō*, but after the *Accēdit quod* sentence it had none | *Haec ēditiō iīs quoque ūtilis erit …* |
| *magistrīs* out of place | Agreed: teachers are not a kind of devotional reader. They belong with Bünemann, who was one | *Eōdem modō legere licet vel magistrō cum discipulīs vel cuivīs sine magistrō …* |
| *Servetus* | Mark it *Servētus*. Spanish Servet stresses the last syllable, and English says ser-VEE-tus; unmarked, Latin would stress SER-ve-tus. Our rule for names without Greek or Hebrew (a long stressed penult, as in *Pagnīnus*) gives *Servētus* | *Servētus*, *Servētī* (three places) |
| *In eō scrībit:* heavy | The quotation now stands as the substance of the refutation, and the work is named after it | *deinde ipsum illum Calvīnī librum refūtāvit: “Hominem occīdere …” Id opus, Contrā libellum Calvīnī, …* |
| *et* overused | Yes, in the life especially. Varied where the clauses are close: *sēque*, *atque*, *annōque*, *ac*, *fidemque*. Lists of equals keep *et*; asyndeton stays in *studiīs, cūrīs, vigiliīs* and *fidēlis, Latīna, perspicua* | Five changes |
| *religiō* | To Castellio and his readers *religio* meant a faith or confession and its worship, here Catholic or Reformed; the classical sense (scruple, cult) also fits worship. *ad religiōnem cōgere* could be read as "force someone to be religious". The *Conseil*'s complaint is that each side made the other attend its worship | *nē quem religiōnem quam nōn probāret colere cōgerent* ("not to compel anyone to practise a religion he did not approve") |
| Jerome and the Vulgate | The old sentence oversimplified. The standard account (general knowledge; not from a source read this session): Jerome revised the Old Latin Gospels (c. 383) and translated most of the Old Testament from the Hebrew (c. 390–405); the Vulgate's Psalms are his earlier revision from the Greek, the rest of the New Testament was revised by someone else, and several deuterocanonical books stayed Old Latin. The whole was named the Vulgate later. Worth a check against Houghton, *The Latin New Testament* (2016), before it goes to print | *Hierōnymus Euangelia ēmendāvit et Vetus Fœdus plērumque ex Hebræō dē integrō vertit; hæc cum aliīs veteribus interpretātiōnibus posteā in ūnum corpus coaluērunt, quod Vulgāta dīcitur.* (*Euangelia* as the settled text spells it) |
| *ut Erasmus Novī Fœderis* | Yes, the genitive hung on an understood *interpretātiōnem*, which the plural *novās* made awkward | *aliī rūrsus vertērunt, ut Erasmus Novum Fœdus, Sanctes Pagnīnus Biblia tōta; quōs omnēs …* |
| Beza's *causam improbāvit* | Below | *Beza factum quidem laudāvit, causam improbāvit, quod Castelliō aliōrum tantum offēnsiōnī cessisse sē dīceret audāciamque suam excūsāret* |
| *maximē* twice | | *potissimum in Germāniā* |
| *disputātōrem dē hæreticīs* | I meant "polemicist", the opposite of the hero Buisson and Zweig made, but the Latin only says "one who argues about heretics", which is neutral and blurs the point | *neque tam in hæreticōrum causā quam in Sacrīs litterīs vertendīs et puerīs docendīs labōrāvisse* ("he laboured less in the heretics' cause than at translating Scripture and teaching children") |
| *In Veterī Fœdere … In Novō Fœdere* | *In Veteri Testamento* is Church Latin; classical prose would sooner make the edition the subject. Also: Gaffiot's ablative of *vetus* is *vetere* (*veterī* is rarer) | *Veteris Fœderis textum dedit ēditiō Lipsiēnsis annī 1738 … Novī Fœderis textum dedit Basiliēnsis annī 1573 …*; *quō in Vetere* |
| Verse numbers twice | Consolidated into the paragraph sentence | *numerōsque versiculōrum parvōs relīquī, eōsdem quōs plēraque Biblia Anglica et concordantiæ ūsūrpant, ut quīvīs locus …* |
| Sign it? | See below | Not changed until you decide |

**Beza's objection, in more detail.** In the *Defensio* (1562, p. 12) Castellio says that when some took offence at *lotio* and *genius*, he put back *baptisma*, *baptizare* and *angelus* in his last New Testament, and that he made such changes even where nothing was wrong, to show he was not stubborn. Beza's *Responsio* (1563, p. 31) answers: "I praise his act in restoring them and casting out those *genii* of his (better late than never); but that he says he did it only for some people's offence, and goes on excusing his boldness, that I do not praise." For Beza the classical words were errors of substance: *baptismus* is the Church's name for a sacrament (p. 30), and to call it *lotio*, a washing, emptied it; *collegium* for *synagoga* he thought rested on a false etymology. So he wanted a retraction, and Castellio offered a courtesy. That is the gap: Castellio treated words as clothing (*vestis*) that could change without changing the thing, Beza as part of the thing itself, which is also the point of his *Ciceroniani evademus*. The sentence now says this in one clause.

**Signature.** I'd sign it. A preface in the first person singular, giving the editor's choices and asking for corrections, is conventionally signed. The Latin prefaces of the Oxford Classical Texts, for instance, close with the editor's initials, the place and the date. Unsigned, *ego* has no referent except the title page; signed, the reader knows whom to *admonēre amīcē*. A modern form fits the house rule against ancient dates, e.g. a line flush right with your name (or initials), the place in Latin or as written, and *mēnse Novembrī 2026*, or just name and year. This reverses the earlier "no signature", so it waits for your word, including the form of the name and the place.

**Decided 2026-11-13:** signed *Nathan Anderson, mēnse Novembrī 2026*, your name as you write it, no place.


## 12. Point by point on the eighth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| Sign it | Your name as you write it, no place | *Nathan Anderson, mēnse Novembrī 2026*, in italics under the closing request; update the month at release |
| The Vulgate keeps Hebrew and Greek idiom and word order: a source? | Half of it holds. Jerome himself says that in Scripture "even the order of the words is a mystery" (*Ep.* 57.5), so word-for-word rendering was his stated principle there. But his practice is uneven: Kenyon called parts "free to the verge of paraphrase" and others literal past sense, and recent studies of his Old Testament from the Hebrew find both Hebraisms and free renderings. The New Testament outside the Gospels is a light revision of the Old Latin, which was close to the Greek. A blanket claim about word order goes beyond the evidence I've seen. That many Hebrew and Greek idioms survive is not disputed (it is also Castellio's own case in the *Defensio*) | *sed multās Hebræōrum Græcōrumque locūtiōnēs retinet* |
| *Eōdem modō legere licet …* clunky | | *Hunc mōrem imitārī possunt et magistrī et lēctōrēs sōlī, Bibliīs suā linguā scrīptīs juxtā positīs.* |
| *nē quem religiōnem quam nōn probāret colere cōgerent* wordy | Yes | *nē quem ad aliēnam religiōnem cōgerent* ("to force no one into another's religion") |
| Jerome, verified | Houghton, *The Latin New Testament* (OUP 2016), ch. 2, read online: Jerome revised only the Gospels (382–384), lightly, "only to correct errors which seemed to change the sense"; the rest of the New Testament was revised by an unknown scholar in Rome between about 393 and 410 (Rufinus the Syrian has been proposed, but his very existence is contested); Jerome's translations from the Hebrew "constitute the majority of the Old Testament in the Vulgate"; the text "was not called the Vulgate until much later". Wikipedia's "Vulgate" (citing the Stuttgart edition) adds what Houghton, writing on the New Testament, does not cover: the Vulgate Psalms are Jerome's revision from the Greek, not his version from the Hebrew; Wisdom, Ecclesiasticus, Baruch and 1–2 Maccabees are Old Latin he did not touch; Tobit and Judith he translated from Aramaic. The Latin sentence fits all of this (*Euangelia ēmendāvit*, *Vetus Fœdus plērumque ex Hebræō*, *cum aliīs veteribus interpretātiōnibus … coaluērunt*, named later) | None; sources table corrected |
| *quod Castelliō aliōrum tantum offēnsiōnī …* wordy, unclear | Yes. Beza's point in one clause: the act was right, the excuse wrong, since Castellio should have owned an error rather than a concession | *Beza factum quidem laudāvit, sed excūsātiōnem improbāvit: nōn enim aliīs cēdendum, sed errōrem fatendum fuisse* |
| *Nōa, nōn Nōē* the best example? | The best one that is settled. Noah appears in five settled New Testament books (Matthew, Luke, Hebrews, 1–2 Peter), always *Nōa*. *Hagar* (Galatians) is the other settled case, but readers know Noah. Isaiah and Elijah would be more striking, since they appear constantly in the Gospels, but their books in the Old Testament are not settled, so their forms are not fixed yet. Revisit when they are | None |


## 13. Point by point on the ninth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *locūtiōnēs* enough? Late Latin? | No. *Locūtiō* covers idiom, not vocabulary or syntax, and the larger difference is that the Vulgate is written in the Latin of its own age (Christian vocabulary, *quod*/*quia* clauses for accusative and infinitive, prepositions for plain cases), which Castellio replaces with classical usage. The Hebrew and Greek idioms come on top of that. General knowledge, uncontroversial; *cōnstrūctiō* in the grammatical sense is Priscian's, later but precise | *sed Latīnitāte ūtitur posteriōris ætātis, quæ et verbīs et cōnstrūctiōne ā Cicerōne discēdit, multāsque Hebræōrum Græcōrumque locūtiōnēs retinet; Castelliō sententiam veterum Rōmānōrum mōre effert* |
| *pietātis causā* | Natural, and right here. Classical *pietās* is dutiful devotion to gods, parents and country (Plautus, *Pseud.* 120 has *pietatis causa*); the Christian sense is Castellio's own, in the sentence quoted just above (*pietās cum Latīnō sermōne discī*), and Thomas à Kempis uses the phrase so. *religiōnis causā* is more classical but would read as "for religious reasons" | None |
| *cujus Vetus Fœdus sequor* | Yes, his edition of Castellio's Old Testament (Leipzig 1738). Said plainly now | *cujus ēditiōnem Veteris Fœderis sequor* |
| *et magistrī et lēctōrēs sōlī* | You were right that the problem was what, not how. Bünemann's example already speaks to teachers; what the reader alone needs to hear is that the method works for them. Second person, as the opening *Vidēbis, lēctor* is | *Sine magistrō idem faciēs, sī Biblia tuā linguā scrīpta juxtā posueris.* |
| Father a farmer: source? | Mahlmann-Bauer, *Verfasserlexikon* col. 3 (father Claude Chasteillon, a farmer); Buisson I:1–2 on the family; Kaegi 8 ("simple country folk"); Bruening (*Aeon* 2025) "a farmer" | None |
| *Castalio*: source? | His own account, quoted by Buisson I:26–27: at Lyon someone called him *Castalion*, the name pleased him (the Castalian spring), and he wrote it as an acrostic in his Greek poem; he later regretted the vanity. His Basel matriculation (1545) has *Sebastianus Castalio*; the 1551 Bible *interprete Sebastiano Castalione*; Ceriolanus's couplet *Castalionis ope* | None |
| Calvin's role in his leaving | The old sentence did elide it. The Council registers (Buisson I:195–215): he had already offered to resign the school in January 1544, saying his pay could not keep two assistants; after he told the ministers on 30 May that, unlike Paul, they were proud, Calvin complained to the Council the next day; on 12 June the Council found he had spoken wrongly and removed him from preaching (at Vandœuvres), and Calvin seems to have pressed for this to be permanent rather than the three months first voted. "Convinced of Calvin's enmity" (Buisson), Castellio resigned and left in July. He was not banished, though Beza's *Life of Calvin* later said so | *… Calvīnō querente ā cōntiōnibus habendīs remōtus est, et annō 1544, Calvīnum sibi inimīcum esse ratus, Genāvā discessit* |
| Begging and ditch-digging | Buisson I:248: many contemporary witnesses say he did hard manual work to feed his family, but the details differ (sawing wood, per Grotius; working the land, per Cherler; carrying water for gardeners; fishing on the Rhine), so Buisson calls it half legend. The one fixed detail is Calvin's charge that he stole firewood, which Castellio answered: he fished driftwood from the Rhine in flood, as fishermen and neighbours did. Begging: he wrote that he would rather have begged than abandon the translation, not that he begged. I found no ditches in what I read | *uxōrem līberōsque … librīs Opōrinī typographī, ut vidētur, ēmendandīs et manū etiam labōrandō aluit* |
| *deinde ipsum illum Calvīnī librum* | It meant Calvin's book, but *ipsum illum* was emphasis on a book the sentence before had barely named. Reordered: *De haereticis* first, then Calvin's book, then a plain relative | *Proximō annō Castelliō librum Dē hæreticīs … ēdidit. Eōdem annō Calvīnus Servētī supplicium librō dēfendit, quem Castelliō refūtāvit: “…”* |
| The predestination paragraph jumps back? | Slightly: it reopened 1554 after reaching 1554, then the next paragraph went back from 1563 to 1562. Now one run in order: 1554 Romans 9; 1558 Calvin; 1562 *Defensio* and *Conseil*; then a last paragraph for 1563 (*De arte dubitandi*, Beza's *Responsio*, Bodenstein, death) | Paragraphs regrouped |
| *crīmina*: which? accurate? | Castellio's answer of 24 November 1563 (Buisson II:257–262) lists five charges taken from Beza: libertine (ungodly); Pelagian (denying grace and original sin); patron of criminals and heretics, wanting magistrates out of religion; papist; "Academic" (sceptic) and Anabaptist in spirit. A second part concerned his Latin translation of Ochino's *Dialogi XXX* (1563), one of which discusses polygamy. He denied each; his books did reject Calvin's predestination, and he did plead for the magistrate to spare heretics, so "Pelagian" and "patron of heretics" were Beza's hostile readings of real positions. Too much for the front matter | None |
| A family? | Yes. He married Huguine Paquelon at Geneva; she died in January 1549 giving birth to their son Nathanael; in June 1549 he married Marie. Eight children in all (Buisson I:248 n. 2, II:269–276; Mahlmann-Bauer counts nine births), several young at his death; Basel helped the widow, and Basilius Amerbach acted as guardian. One son, Friedrich, lived 1562–1613 | *Basileæ uxōrem līberōsque, quōs octō omnīnō habuit, … aluit* |
| *lōtiōnis et geniī* then the list | Agreed | *cum quīdam novīs vocābulīs offenderentur* |
| *ea ferē vocābula quæ* | *ferē* is classical with general statements too ("as a rule", "for the most part"), not only numbers, but here it was vague | *plēraque eōrum quæ ad doctrīnam pertinent* |
| *nōn enim aliīs cēdendum …* | Grammatical (reported speech can run on without a verb of saying), but *improbāvit* is not one, so the reader has to supply it | *sed improbāvit quod Castelliō nōn errōrem fatērētur, sed aliīs sē cessisse dīceret* (*quod* + subjunctive: Beza's reason) |
| *recūsa* | Yes: *recudere* is the printers' verb of the period (*denuo recusus*, *iterum recusa* on title pages), as *excudere* is for printing | None |
| The dedication to Henri II | It adds nothing the reader needs; the point is the readers he meant it for | *Gallica, quæ annō 1555 ēdiderat ut eī quoque legerent quī Latīnē nescīrent, …* |
| Notable students? | Basilius Amerbach, the future jurist and collector, was his pupil from 1546/47 (Mahlmann-Bauer cols. 3–4); the Polish students who wrote his epitaph; Faustus Socinus edited his dialogues but was not his pupil. None belongs in the front matter | None |


## 14. Point by point on the tenth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *posteriōris ætātis … veterum Rōmānōrum mōre* | The first is fine and neutral (Du Cange's *infima Latinitas* is the old term, but pejorative). The second was vague: "the ancient Romans" includes Tertullian. The precise word has an ancient pedigree: Gellius (19.8.15) calls a model writer *classicus scrīptor*, which is where "classical" comes from | *… quæ et verbīs et cōnstrūctiōne ā classicīs scrīptōribus discēdit …; Castelliō classicōs imitātur* |
| *Sine magistrō idem faciēs …* too commanding | Yes: the future reads as an instruction. *poteris* offers it | *Idem vel sine magistrō facere poteris, Bibliīs tuā linguā scrīptīs juxtā positīs.* |
| The Geneva sentence | Every clause was doing two jobs. Now three plain steps: what he said, what Calvin and the Council did, why he left | *mox, cum eōs pūblicē superbōs esse dīxisset, Calvīnus apud senātum questus est, quī eum ā cōntiōnibus remōvit. Itaque, cum Calvīnum sibi īnfēnsum esse intellegeret, annō 1544 Genāvā discessit.* |
| Wife and eight children: reliable? | The marriages are documented: Buisson read the Geneva and Basel records (Huguine Paquelon, her death in childbirth with Nathanael, the second marriage to Marie on 20 June 1549). The number is less firm: Buisson says eight in all, citing a later biographer (I:248 n. 2); Mahlmann-Bauer counts three by Huguine and six by Marie, nine births; Bruening says eight at his death. They also differ on the year Huguine died (January 1549, Buisson; January 1550, Mahlmann-Bauer). Known by name: Susanna (born about 1544), Debora (1547–49), Nathanael (born 1549), and Friedrich (1562–1613); Basel supported the widow, with Basilius Amerbach as guardian (Buisson II:269–276) | *uxōrem et līberōs complūrēs*: no number |
| *Eōdem annō* repeated | Four times, two of them adjacent. Now twice, far apart: *sub idem tempus* for the *Conseil*; Calvin's book in the pluperfect (*dēfenderat*), which is also more accurate, since it came out a month before *De haereticis* | |
| Beza's *Respōnsiō* after *De arte dubitandi* | Agreed, it read as a reply to it. The last paragraph now runs: Beza's *Responsio* (1563), Bodenstein's accusation in November, death in December; then, as a closing note, the book he had written that year | *Annō 1563 Beza Respōnsiōnem in eum ēdidit … Castelliō tamen ante jūdicium mortuus est … Eōdem annō librum Dē arte dubitandī … scrīpserat …* |
| *plēraque eōrum quæ* | Yes: *plēraque* can stand as the noun's own adjective with *vocābula* understood from the sentence before | *plēraque quæ ad doctrīnam pertinent ad ūsitāta revocāvit* |
| The French Bible in the translation section | Agreed. It belongs in the life, where he made it: the Basel paragraph now says he finished the Latin Bible, then the French, in everyday language for those without Latin; Estienne's jibe and the 2005 reprint follow there. The reception paragraph now says *Latīna Castelliōnis Biblia* | Basel paragraph split in two (Basel and the Bibles; 1553–54 and Servetus) |


## 15. Point by point on the eleventh version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *manū labōrandō* | Not a collocation I can find (no hits for it). Jerome's *Life of Malchus* has the phrase for earning one's bread by hand, *manuum labore victum quaeritans*, and later writers use it the same way | *librīs … ēmendandīs et manuum etiam labōre aluit* |
| *Gallicē* + name | Agreed: the reader sees an adverb and then words that are not Latin. A relative clause says it outright; Montaigne simply keeps his French name, with a Latin first name and a noun in apposition, as Neo-Latin usually treats modern authors | *Castelliō, cui Gallicē nōmen erat Sébastien Châteillon, …*; *ut Michaēl dē Montaigne, scrīptor Gallicus, posteā …* |
| *prīmum annō 2005 iterum* | "First again" is clumsy. "Not reprinted until 2005", without repeating the *nec ante annum 1612* used for *Contra libellum Calvini* a few lines on | *et Gallica Biblia ūsque ad annum 2005 nōn iterum excūsa sunt* |
| What *De haereticis* argued | An anthology: passages from the Fathers and recent writers (Augustine, Jerome, Chrysostom, Luther, Brenz and Calvin himself, as Castellio lists them in *Contra libellum Calvini*; Buisson II:36) to show that heretics should not be put to death | *… librum Dē hæreticīs an sint persequendī ēdidit, in quō ex veteribus et recentiōribus doctōribus, Luthērō etiam et ipsō Calvīnō, locōs collēgit quibus hæreticōs nōn esse occīdendōs docērētur.* *Luthērus* follows Wiktionary under the names rule (decision 52), since Gaffiot has no entry |
| The ending after *De arte dubitandi* | Yes, the section should end on his death. *De arte dubitandi* now goes inside the death sentence as a relative clause, so its last words are Zwinger's: *studiīs, cūrīs, vigiliīs*. The 1981 edition drops out of the text (it stays in the sources). Beza's *Responsio* is now said to answer the *Defensio* (*Dēfēnsiōnī ejus Respōnsiōnem opposuit*), so it cannot be read as a reply to the later book. A bigger rearrangement (all the works in one place) would bring back the catalogue you objected to before | *Castelliō tamen, quī eō annō librum Dē arte dubitandī … scrīpserat, ante jūdicium mortuus est, …* |


## 16. Point by point on the twelfth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *Michaēl dē Montaigne* | Agreed. Vicipaedia's article is *Michael Montanus* (with *Michael de Montaigne* only as a redirect), and it is the Latin form older writers use | *Michaēl Montānus, scrīptor Gallicus*; the English gloss names Montaigne |
| *ūsque* | Short. The settled text writes *usque* ten times, and Wiktionary, Macronizer and Lewis & Short all have a short *u*; Gaffiot alone marks it long, so `macron-check` will keep flagging it. Same for both places | *usque* |
| *Castelliō tamen, quī eō annō …* forced | Yes: a book squeezed into a death sentence. The last paragraph now does three things in order: what he wrote in his last year, with its thesis (as *De haereticis* now has its own); the attack that overtook him (*Interim Beza … opposuerat*, pluperfect, so Beza's book is plainly earlier and plainly a reply to the *Defensio*); his death, ending on Zwinger's words | *Ultimō vītæ annō librum Dē arte dubitandī … scrīpsit, in quō docet nōn minus malī orīrī ex eō quod nōn dubitētur ubi dubitandum sit, quam ex eō quod nōn crēdātur ubi crēdendum sit. Interim Beza Dēfēnsiōnī ejus Respōnsiōnem opposuerat, … Castelliō tamen ante jūdicium mortuus est, …* (the thesis from the manuscript, fol. 81, as Buisson II:216 n. 4 quotes it) |


## 17. Point by point on the thirteenth version (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| Name Montaigne in French too | A parenthesis after the Latin name: the reader meets the form he knows without a second relative clause like Castellio's | *Michaēl Montānus, scrīptor Gallicus (Michel de Montaigne)* |
| The thesis of *De arte dubitandi* | Not needed: the title already says what the book is about, and the paragraph is now about his last year, not the book | Clause dropped: *Ultimō vītæ annō librum Dē arte dubitandī … scrīpsit. Interim Beza …* (the fol. 81 sentence stays in the sources table) |


## 18. Final review (2026-11-13)

Read through whole for flow, style, tics and accuracy. Changes:

| Kind | Found | Change |
|---|---|---|
| Spelling | *Haec* and *coepit* (twice) without their ligatures. I first passed *coepit* as having no diphthong; Gaffiot heads *cœpī*, and the settled text writes *cœpit* 38 times (corrected after your note) | *Hæc*, *cœpit* |
| Tic | *autem* opening three paragraphs running in the translation section | Dropped from *Eduardō … dēdicāvit* and *Beza, Castelliōne nōn nōminātō*; kept in *In Dēfēnsiōne autem* |
| Tic | *tamen* four times in the life | Dropped from *Castelliō ante jūdicium mortuus est* |
| Tic | *sed … sed* in Beza's objection | *sed improbāvit quod Castelliō aliīs sē cessisse dīceret, nōn errōrem fatērētur* |
| Repetition | *quod … quod* in one sentence | *id quod in tam longīs librīs rārō fit* |
| Repetition | *Calvīnum … Calvīnī … Calvīnī … Calvīnus* in the predestination sentence | *ejus discipulum*; *quā eōrum doctrīnam impugnābat* (the doctrine was Beza's too) |
| Repetition | *Gallica … Gallica Biblia* | *et ea usque ad annum 2005 …* |
| Repetition | *ēditiō* four times in the first sentence of the *Ratiō* | *in omnēs irrēpserant* |
| Flow | *Interim … opposuerat* after "in the last year of his life" read oddly | *Eōdem annō Beza … opposuit* |
| English gloss | A dangling participle in the Geneva sentence; "chiefly" twice running; *Calvin's teaching* where the Latin now says *their* | Fixed; the gloss rewrapped |

Checked and left: every date and attribution against the sources table; the quotations (*Moses latinus* title, *Defensio* pp. 9–17, the Edward VI dedication, *Contra libellum Calvini* 1612, Beza 1556 and 1563, the *Admonitio*); macrons (`macron-check`: only names, *usque* and Gaffiot-only forms flagged). No sentence of a modern source is reproduced; the modern scholars are paraphrased.


## 19. Point by point after the final review (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *cum Calvīnus Genāvam revocātus esset, … magister factus est*: Calvin the schoolmaster? | Yes, it could be read so: the only nominative in sight was *Calvīnus*. An ablative absolute takes him out of the running | *annō 1542, Calvīnō Genāvam revocātō, lūdī Genāvēnsis magister factus est* |
| *Basilea* | Gaffiot heads *Băsĭlēa*, and the Greek βασιλεία (ει, long) agrees under the names rule. *Basiliēnsis* stays: it is the usual Neo-Latin adjective (the university's own *Universitas Basiliensis*) | *Basilēæ* (twice) |
| *Opōrinus* | Yes, short. Johannes Oporinus is a Greek rendering of his German name Herbster ("autumn"): ὀπωρινός, from ὀπώρα; adjectives of season in -ινός have a short ι (ἐαρινός, χειμερινός). So *Opōrinus*, stressed o-PO-ri-nus | None |
| *ea usque ad annum 2005 nōn iterum excūsa sunt* | Understandable but not idiomatic: Latin puts the limit on the event, not on its negation. *dōnec* with the perfect says it plainly | *et ea diū neglēcta jacuērunt, dōnec annō 2005 dēnuō excūsa sunt* (*neglēcta* with Gaffiot) |
| *Dēfēnsiōne respondit* | An inflected title is normal in Latin (*in Catōne Māiōre*), but as a bare instrumental it reads as "with a defence" before the italics register. An ablative absolute makes it an act | *ēditā Dēfēnsiōne respondit* |
| *Dēfēnsiōnī ejus* italic? | Yes, a title | *Dēfēnsiōnī ejus Respōnsiōnem opposuit*, both italic |
| *ut syllabārum quantitās appāreat* | Agreed: quantity matters to metre, and this is prose. What the marks do for this reader is let them pronounce each word, put the stress where it falls, and so hear and remember the word | *ut verba rēctē prōnūntientur et accentus suō locō pōnātur, quod ad ea memoriæ mandanda multum cōnfert, utque verba fōrmā similia … distinguantur* (*accentus* is Quintilian's word for stress) |
| *Notæ* simpler | The Greek in each line already says New Testament | ⟦ ⟧ *Mc 16,9–20 et Jo 7,53–8,11, quæ antīquissima exemplāria Græca nōn habent.* [ ] *Verba quæ ēditiōnēs Græcæ hodiernæ omittunt.* |
| *Librī legendī* | Relevance: all seven are used in the text or stand behind it; no change in the selection. Order: now two groups, his works (in the order he wrote them: *De haereticis*, *Contra libellum*, the French Bible) and studies (by date). Formatting: places were half Latinized (*Parīsiīs*, *Gottingæ*) and half not (*Aldershot*); now all as on the title pages. Guggisberg's subtitle had *Tolerance*: the book says *Toleration* (library records). Titles keep their own language's capitals | List rewritten |
| Plagiarism of older sources | Checked mechanically: every run of five or more words shared with the transcriptions of the older sources (the 1573 front matter, the 1738 and 1750 prefaces, the *Defensio*, Beza, Buisson's quotations, the 1612 *Contra libellum*) is either a book title or a passage already in quotation marks: the *Moses latinus* title, *ex quā posset … discī*, Ceriolanus's couplet, the *sartōrēs* sentence, *Rēs enim dictat Spīritus …*, *multōs jūdicāsse …*, Beza's *Cicerōniānī ēvādēmus*, the *Admonitio*. The paraphrases (the Edward VI dedication, the *Admonitio* on animals and Aramaic, Humphrey, Bünemann's Minden method) are in my own words | None |


## 20. Two last points (2026-11-13)

| Your point | Answer | Change |
|---|---|---|
| *ea diū neglēcta jacuērunt* | Not idiomatic enough: *jacēre* of neglected things is Ciceronian, but the corpus has no *neglecta iacuerunt* or the like, and it added a judgement the sources don't make. *dēmum* ("not until") is the natural word | The reprint now goes with the French Bible itself, and Estienne's jibe follows: *… deinde Gallica, quæ annō dēmum 2005 rūrsus excūsa sunt. Hæc sermōne cotīdiānō vertit …; quem sermōnem Henrīcus Stephanus … mendīcōrum esse dīxit.* Also the third *Basileæ* (start of the Basel paragraph), missed in §19, is now *Basilēæ* |
| The macron sentence overshot | Yes. Correct pronunciation already includes the stress, and the memory clause was a claim the reader doesn't need | *ut verba rēctē prōnūntientur et fōrmā similia, ut venit et vēnit, distinguantur* |
