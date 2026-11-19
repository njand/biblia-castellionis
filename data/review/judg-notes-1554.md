# Judges: footnotes from Castellio's 1554 annotations (1)

Proposed 2026-11-19 (Nathan: "Start the notes for Judges, the same way"), following the method of `deut-notes-1554.md` (and `gen-exod-notes-1554.md`, `lev-notes-1554.md`,
`num-notes-1554.md`). Every annotation on Judges in the 1554 Basel edition was read on the page and sorted as (a) a
deliberate departure from the Hebrew as read today, (b) a word no dictionary has that Castellio explains, (c)
commentary or a defence of Latin a reader can follow (no note), or (d) a place where the annotation shows the settled
text (1738) differs from what he meant. Decisions 53 and 56; brief.md, "brief Latin footnotes"; the bar of
`ot-notes-process.md` §2–3. The note goes right after its word. The Hebrew is the WLC's (`sources/parallel/wlc/Judg.tsv`)
without the cantillation marks.

**Where the annotations are** (MDZ bsb10196330; images `https://api.digitale-sammlungen.de/iiif/image/v2/bsb10196330_00824/…`,
read 2026-11-19). *IN LIB. IVDICVM* (so headed) begins a third of the way down the right column of canvas 824
(column 344), after the *EX CAP. XX.* note on Joshua (*Donec causam in concilio dixerit*), and runs to the foot of that
column. It goes on at the top of the left column of canvas 825 (column 345) and ends about 45% of the way down it,
where *IN RVTHAM* begins (one note, on Ruth 3:15). That gives twelve annotations under the heads *EX CAP. V., VIII., XI.,
XII., XIIII. (two), XV. (two), XVII. (no lemma), XVIII. (two)*. Every head matches its verse. Crops read: `c824-full.jpg`,
`c825-full.jpg`, `c824-JR1.jpg` … `c824-JR6.jpg`, `c825-JL1.jpg` … `c825-JL4.jpg`, and zooms on the Hebrew and Greek
(`z824-j5h1.jpg`, `z824-j5h2.jpg`, `z824-j8.jpg`, `z824-j8h1.jpg` … `z824-j8h3.jpg`, `z824-j14.jpg`, `z824-j14b.jpg`,
`z824-j15.jpg`, `z825-j15.jpg`), all in `sources/mdz-1554/`. No reader's handwriting is on these columns. On canvas 825,
under Kings, a hand has written *Adde* in the margin; it is not Castellio's and is not used.

**The 1554 text's own margins.** The 1554 Judges (canvases 137–150, columns 249–276) also prints **lettered marginal
notes** beside the text, set apart from the summary side-heads and cross-references. Every one of 1738's lettered
footnotes is among them (§ "1738's footnotes" below). Pages read: `t137.jpg` … `t150.jpg` (full page, 1200 px wide),
with zooms `m137-1_8.jpg`, `m137-1_8b.jpg`, `m138-2_9.jpg`, `m142-9_9.jpg`/`n142-9_9.jpg`, `n140-5_22.jpg`,
`n143-10_12.jpg`, `n146-14a.jpg`, `n148-18_30.jpg`, `n149-19_28.jpg`, `n149-20_16.jpg`, `n150-20_42.jpg`. Where no zoom
is named, the margin was read on the 1200-px page; I could read it there, but not letter by letter at full size.

**Quotations** follow the page: u/v and i/j as printed, a tilde for a nasal (*urbiũ*), *s* for ſ, *ß* written *ss*. Hebrew
is given as printed, unpointed. Where a letter of the printed Hebrew is unclear (ד or ר, ב or כ), that is said.
**Modern renderings**: the NRSVue on Bible Gateway (Judges 5, 8, 15 and 18 read 2026-11-19, with their footnotes; not
stored); the NET on Bible Gateway for 15:16; the BSB from `sources/parallel/bsb/Judg.tsv`.

**Settled text.** Every lemma of the twelve annotations matches the settled text (`text/JDG.usfm`), with spelling
differences only (8:16 *eis*, settled *iīs*; 14:20 *affinitatis*, settled *affīnitātis*; 18:2 *abiectissimos*). The
1554 text beside each of 1738's footnotes also matches the settled text, with one exception: **2:9** 1554 has
*Thamnatare in mõte Ephraimitico* (canvas 138, column 251), where 1738 and the settled text have *Themnathare*. That is a
name form changed after 1554, and only that. (Wikisource's *Thamnatare*, corrected to 1738 in stage 2 item 15, is
1554's form.) No (d) item.

## 1. Judg 18:2 *suōrum mīlitum abjectissimōs*

The Hebrew אֲנָשִׁים בְּנֵי־חַיִל is "men of valour" (NRSVue "five valiant men", no footnote; BSB "men of valor"). Castellio
(canvas 825, column 345, *EX CAP. XVIII.*): *Suorum militum abiectissimos.) בני חיל non fortes semper, sed milites
dicuntur, ut patet ex multis locis in Numeris, & secundo Regum 17. Abiectissimi autem mittebantur, ut facilius
fallerent.* He took בני חיל as plain "soldiers", not "brave men", and then supplied "the most worthless" from his own
reasoning: men of no account would be less likely to be suspected. The settled text has *Mīsērunt igitur Daniī suæ
gentis hominēs quīnque, suōrum mīlitum abjectissimōs*, as 1554 does (canvas 147, column 270, *suorum militum
abiectissimos*).

So the sense is reversed. The Hebrew and both modern versions send the tribe's best men, and Castellio sends its
worst. The NRSVue and the BSB agree with each other and with the Hebrew's words, and neither calls the Hebrew
uncertain. Kind B (or C: the superlative has nothing in the Hebrew behind it).

> *Hebraicē אֲנָשִׁים בְּנֵי־חַיִל, ‘virōs fortēs’; ‘abjectissimōs’ Castelliō addit.*

("Hebrew 'valiant men'; Castellio adds 'the most worthless'.") Words checked with `pipeline latin macron` (virōs,
fortēs, mīlitēs, intellegit; *abjectissimōs* as the settled text has it). Shorter, if preferred: *Hebraicē אֲנָשִׁים
בְּנֵי־חַיִל, ‘virōs fortēs’.* Fuller, giving his reading: *Hebraicē אֲנָשִׁים בְּנֵי־חַיִל, ‘virōs fortēs’; Castelliō
‘mīlitēs’ intellegit, et abjectissimōs missōs, ut facilius fallerent.* (The notes no longer give his reasons,
`notes-audit.md`.)

**Recommendation (Claude):** accept, in the shorter wording (the Apply line), which keeps to the fixed formula (*Hebraicē* Hebrew, ‘Latin’) as Deut 10:3, 26:5 do; the reader's *‘abjectissimōs’ Castelliō addit* is the alternative. Reversing the spies from the tribe's best to its
worst is as large a change as Deut 33:8, which was accepted. The two versions agree with the Hebrew, and the NRSVue
gives no footnote.

**Decision:** accept, in the shorter wording (Nathan, 2026-11-19: "Apply these notes as recommended, and fix the Deuteronomy 33:8 note to read *temptāvistī*.")
**Apply:** `Judg.18.2` la: `suōrum mīlitum abjectissimōs,` → `suōrum mīlitum abjectissimōs\f + \fr 18:2 \ft Hebraicē אֲנָשִׁים בְּנֵי־חַיִל, ‘virōs fortēs’.\f*,`

## Not proposed

**Judg 5:14** *In valle posterior fuistī, ō Benjamīta*. The Hebrew is שָׁרְשָׁם בַּעֲמָלֵק אַחֲרֶיךָ בִנְיָמִין, "their root in
Amalek; after you, Benjamin". Castellio (canvas 824, column 344, *EX CAP. V.*): *In ualle posterior fuisti,
Beniamita.) בעמלק legitur, hoc est in Amalechitis: sed sententia constare non potest. Videtur בעמיק legisse Græcus
interpres, qui uertit ἐν κοιλάδι: quæ lectio sententiæ conuenit. nam paulo pòst dicitur in uallem missus esse Baracus,
in qua pugnatum est. Est igitur hæc huius loci sententia: in hoc prælio non adfuere Beniamitæ, sed eorum populares
Ephraimitæ, & Manassenses, ex Machire Manassis filio orti, digni qui deinceps imperent: item Zabulonij literarum
proceres, & Issachariani duce Baraco.* (The Hebrew is as printed, the second word with a yod, *בעמיק*; read on
`z824-j5h2.jpg`.) He follows the Greek's "in the valley", as the NRSVue does ("From Ephraim they set out into the
valley, following you, Benjamin", notes "Cn: Heb From Ephraim their root" and "Gk: Heb in Amalek"). The BSB keeps the
Hebrew ("with their roots in Amalek; Benjamin came with your people after you"). Castellio reads Benjamin as absent,
where both versions have Benjamin taking part. But the NRSVue emends the line twice and the two versions disagree, so
the passage is disputed: no note.

**Judg 8:16** *Socōthēnsēs senātōrēs iīs contrīvit*. The Hebrew וַיֹּדַע בָּהֶם is "and he taught (them) with them".
Castellio (canvas 824, column 344, *EX CAP. VIII.*; the lemma's initial *S* is a large blackletter capital): *Senatores
eis contriuit.) In Hebræo legitur וידע, nullo sensu, aut certè coacto. Paulo antè positum erat ודשתי, & comminuam.
Itaq; cum hic repetantur cætera eadem uerba, puto legendum esse וידש.* (The Hebrew is read on `z824-j8h1.jpg` …
`z824-j8h3.jpg`. The second letter of each word could be ד or ר at this size; the WLC's וַיֹּדַע and 8:7 וְדַשְׁתִּי fit.)
He emends from 8:7's "trample", as the NRSVue does ("he trampled the people of Succoth", note "Compare Gk: Heb *he
taught*"). The BSB keeps the Hebrew's sense ("he disciplined the men of Succoth"). The modern versions differ and the
NRSVue itself departs from the Hebrew: no note.

**Judg 15:16** *Māxillā asinī, asinī asināriī*. The Hebrew חֲמוֹר חֲמֹרָתָיִם is read today as "heaps upon heaps" (NRSVue,
no footnote; BSB "I have piled them into heaps"). Castellio (canvas 824, column 344–canvas 825, column 345, margin
*Asinus asinarius.*): *Maxilla asini, asini asinarij.) חמור חמרתים asinus asinarius eo modo dicitur, quo caprum
caprinum, & bouem bouinum dici annotauimus: & quomodo Iudic. 5. רחם רחמתים puella puellaris, id est puella dicitur.
estq; elegans repetitio, præsertim in sententijs. Neq; hic magistros Iudæos sequi placet, qui חמור aceruum
interpretantur. Nam ita & imperfecta foret, & minus elegans sententia. neque ijsdem uocalibus scribitur id uerbum, cum
aceruum significat, nisi hoc in loco, si illis credimus. Sed ambiguus cum sit, in testimonium adduci non potest: nec
propria interpretatio, coactæ locum relinquit.* (The Hebrew is as I read it on `z825-j15.jpg`; the ח's look like ה at
this size.) He knew the "heap" reading and rejected it. But the NET's note calls the line's meaning uncertain (*The
precise meaning of the second half of the line … is uncertain*), offering "a heap, two heaps", "I have made donkeys of
them" (cf. NIV), "thoroughly skinned" and "stormed". That makes it disputed: no note.

**Judg 5:30** (settled 5:29) *puellam puellārem in singula capita*. The annotation on 15:16 shows that this phrase
renders רַחַם רַחֲמָתַיִם ("a girl or two", NRSVue "A woman or two", BSB "a girl or two") as a doubled noun, "a girlish
girl, that is, a girl". So a reader gets one girl a head where the modern versions have one or two. The point is a
small one, the line is the mother's imagined speech, and the sense (captive women shared out) is kept: no note.
Draft, if wanted: *Hebraicē רַחַם רַחֲמָתַיִם, ‘puellam aut duās’; Castelliō ‘puellam puellārem’ vertit.* (Aside: the
settled text's 5:29 holds the opening of the KJV's 5:30, *Nīmīrum prædam nactī dīvidunt … puellam puellārem in
singula capita*, a clause off. It is as Castellio divides it, so it is not a question for this file.)

**Judg 15:8** *gravī ingentīque clāde in quōdam tractū*. The Hebrew שׁוֹק עַל־יָרֵךְ is "leg upon thigh" (NRSVue "hip and
thigh with a massive defeat"; BSB "ruthlessly with a great slaughter"). Castellio (canvas 824, column 344, *EX CAP.
XV.*): *Ad uerbũ sic legitur: Percußit eos coxã supra femur. Ego cũ hinc nullam aptã possem elicere sententiã, Iosephũ
secutus sum, qui uertit, πολλοὺς ἐν τῷ πεδίῳ τῶν παλαιστινῶν ἀποκτείνας, cum multos in campo Palæstinorum
occidisset. Nam ירך non solum femur, sed etiam regionem declarat.* (The Greek is as I read it, printed with
ligatures; not checked against a Josephus edition.) The idiom means a great slaughter, which his *gravī ingentīque
clāde* keeps, as the BSB's "ruthlessly with a great slaughter" does. The *in quōdam tractū* he adds from Josephus is
small: no note.

**Judg 14:20** *illīus ipsīus affīnitātis conciliātor*. The Hebrew לְמֵרֵעֵהוּ אֲשֶׁר רֵעָה לוֹ is "to his companion who had
been his friend" (BSB "one of the men who had accompanied him"). Castellio (canvas 824, column 344, *EX CAP. XIIII.*):
*Secutus sum Iosephum, qui uertit νυμφοστόλον: & ueterem, qui pronubum: & Græcum, qui νυμφαγωγόν.* (The first word is
printed νυμφοςόλον with the στ ligature.) The best man, the sense the versions he names give: no note.

## All annotations, sorted

(a) = proposed above; (c) = commentary or a defence of Latin, no note; (c*) = looked at closely and not proposed (see
above).

| Verse | Canvas, column | Lemma (as printed) | Summary | Kind |
|---|---|---|---|---|
| 5:14 | 824, 344 | *In ualle posterior fuisti, Beniamita* | בעמלק makes no sense; the Greek read בעמיק, ἐν κοιλάδι; Benjamin was not at the battle, but Ephraim, Manasseh (Machir), Zebulun and Issachar were | c* |
| 8:16 | 824, 344 | *Senatores eis contriuit* | וידע makes no sense; read וידש from 8:7 ודשתי | c* |
| 11:35 | 824, 344 | *Ea es quæ me perturbes* | Hebrew "you are among my troublers", i.e. you trouble me; see the note on Ps 54 | c |
| 12:7 | 824, 344 | *Sepultus est in oppidis Galaaditicis* | the plural because the town is not named (Gen 19 *Lotus urbiũ incola*; Cicero *Ego eram in his locis*) | c |
| 14:5 | 824, 344 | *Occurrit leoni* | כפיר אריות is rendered "lion", as שעיר העצים [so printed, for העזים] "goat"; a little later it is simply "lion" | c |
| 14:20 | 824, 344 | *Illius ipsius affinitatis conciliator fuerat* | follows Josephus νυμφοστόλον, the old Latin *pronubum*, the Greek νυμφαγωγόν | c* |
| 15:8 | 824, 344 | *Graui ingentiq; clade in quodam tractu* | literally "smote them leg over thigh"; follows Josephus "in the plain of the Philistines"; ירך also "region" | c* |
| 15:16 | 824, 344–825, 345 | *Maxilla asini, asini asinarij* | doubled noun like *caprum caprinum*, *bouem bouinum*, Judg 5 רחם רחמתים *puella puellaris*; rejects the rabbis' "heap" | c* |
| (17–21) | 825, 345 | (no lemma; *EX CAP. XVII.*) | what follows to the end of the book happened before the judges: Danites seeking land (18), Jonathan grandson of Moses and Phinehas (20) could not have lived so long; 19 says the Israelites did not live in Jerusalem, 1 that they took it; Josephus tells chapter 19 earlier | c |
| 18:2 | 825, 345 | *Suorum militum abiectissimos* | בני חיל not always "brave", but "soldiers" (Numbers, 2 Kgs 17); the most worthless were sent, to deceive the more easily | **a** (1) |
| 18:28 (and 18:7) | 825, 345 | *Quod procul à Sidonijs aberant* | so they were the Sidonians' clients or allies, too far away to be defended by them | c |

(The 14:5 Hebrew: the first letter of *כפיר* could be read as ב, and the last word is printed with צ, *העצים*, where
"goats" is העזים; read on `z824-j14b.jpg`.)

## 1738's footnotes, against 1554

The nine footnotes listed in `docs/editions.md` (§ "Judges in 1738, 1750 and Wikisource") are all **lettered marginal
notes of the 1554 edition** itself. None of them is among the annotations at the end of the volume. So they are
Castellio's (1554), not Bünemann's (1734). The verse numbers below are the KJV's; 1738's numbers, where they differ,
follow in brackets.

| Verse | 1738 (stage 2 readers, `judg1-21-stage2-readers.md`) | 1554 margin (canvas, column) | Lemma in 1554's text vs the settled text |
|---|---|---|---|
| 1:8 | *scilicet arce ab hostibus retenta, nam paullo post negantur inde exacti Iebusæi* (b, at *et vrbem*) | *a scilicet arce ab hosti bus retenta. nã paulo pòst negantur inde exacti Iebusæi.* (137, 250; at *& ᵃ urbẽ igni incenderũt*) | same |
| 2:9 | *Hæc in Iosua vocatur Thamnathasara* (c) | *a hæc in Iosua uocatur Thamnathasara.* (138, 251) | **1554 *Thamnatare*, settled *Themnathare*** (name form) |
| 3:15 | *læua manu pro dextra vtentem* (d) | *a læua manu pro dextera utentem.* (138, 252; at *hominẽ ᵃ scæuam*) | same; the note's *dextera* became *dextra* |
| 10:12 | *Græcus et Latinus legerunt Chananæis* (on *Maoniis*) | *a Græcus & Latinus legerunt, Chananęis* (143, 262; at *à ᵃ Maonijs*) | same |
| 14:12, 14:15, 14:17 | d, e, f (leaf 309; not transcribed by the stage 2 readers) | *a ante finitos hos septem dies, in quibus sumus.* (at *ᵃ intra septem conuiuij dies*); *b qui quartus erat à proposita quæstione, septimus autem conuiuij.* (at *ᵇ die VII petierunt*); *c per eos dies qui ex septem restabant.* (at *ᶜ per septem dies*) (146, 267) | same (14:15 *die VII*, settled *diē septimō*) |
| 18:30 | *in Hebræo est Manassis: sed in Latino Mosis, quod puto rectius* (g) | *a in Hebræo est Manassis: sed in Latino Mosis quod puto rectius.* (148, 271; at *ᵃ Mosis nepos*) | same |
| 18:30 [1738 18:31] | *hinc adparet, librum hunc scriptum esse post captiuitatem* (h) | *b hinc apparet librũ hunc scriptum esse post captiuitatem.* (148, 271; at *ᵇ usq; ad tempus captiuitatis eius gẽtis*) | same |
| 19:28 [1738 19:29] | *erat enim mortua* (i, at *Sed quum*) | *a erat enim mortua.* (149, 273; at *Sed ᵃ cum illa nõ responderet*) | same |
| 20:16 | *qui sinistris manibus pro dextris uterentur* (k) | *a qui sinistris manibus pro dexteris uterentur.* (149, 274; at *ᵃ scæuæ*) | same; *dexteris* became *dextris* |
| 20:42 [1738 20:41] | *[a] decem millibus electis, supra memoratis* (l, at *excepti ab illis*) | *a decẽ millib. electis, suprà memoratis.* (150, 275; at *excepti, ᵃ ab illis perdebantur*) | same |

The 18:30 note's first person (*quod puto rectius*) is Castellio's, as `docs/editions.md` guessed. These are the first
of 1738's notes shown to be his. The 1738 footnote readings have the small changes of a later printing (*paullo*,
*dextra*, *dextris*, *adparet*); otherwise they are the 1554 notes word for word.

**1554 marginal notes that the stage-2 readers did not record in 1738.** Whether 1738 prints them was not checked:
its lettering (1:8 b, 2:9 c, 3:15 d, then 10:12 a, 14:12 d) suggests notes the readers' list leaves out.
- 5:11 *a quas in liberandis pagis exeruit* (139, 254; at *uirtutes ᵃ paganæ*)
- 5:16 *b seruitutẽ tolerantes, ut asini sarcinas.* (139, 254; at *quid sedistis ᵇ inter sarcinas*)
- 5:22 *c scilicet fugientium.* (140, 255; at *tanta erat ᶜ rectorũ eorũ incitatio*)
- 6:3 *a Arabes interprete Iosepho.* (140, 255; at *atque ᵃ orientales*)
- 8:2 *a maior est uestra, qui belli reliquias confecistis, gloria, quàm nostra, qui belli principes fuimus.* (141,
  258; at *ᵃ Quasi uerò non sit Ephraimitarũ racematio*)
- 8:21 *b ut iuuenis est Iether, sic parũ uiribus pollet.* (142, 259; at *nam ᵇ dignę homine uires*)
- 9:9 *a scilicet oleo, quod ad sacrificia & lucernas adhibetur, & ad ungendos uates, & sacerdotes & reges.* (142,
  260; at *& dij ᵃ honorarentur*)
- 9:13 *b scilicet in libaminibus.* (142, 260; at *& ᵇ deos exhilararet*)

These are glosses on the sense, not departures from the Hebrew. One bears on a notes question: 14:15 *die VII* keeps
the Hebrew's "seventh day" (the BSB's note: LXX and Syriac "fourth"; `judg-notes-candidates.md` line 40), and the
margin's *qui quartus erat à proposita quæstione, septimus autem conuiuij* shows that Castellio knew of the "fourth"
and reconciled the two.

## For `docs/editions.md` (not written by this reader)

- Judges in 1554 (MDZ bsb10196330): the text is on canvases 137–150 (columns 249–276), with lettered marginal glosses
  (listed above). The annotations at the end of the volume are canvas 824, column 344, to canvas 825, column 345.
- 1738's nine (twelve, with 14:12–17) lettered footnotes in Judges are 1554's marginal notes. They are Castellio's, and
  1738 changes only the spelling (*paullo*, *dextra*, *dextris*, *adparet*).
- 2:9 *Thamnatare* (1554) became *Themnathare* (1738) after 1554. The printing that changed it was not checked.
