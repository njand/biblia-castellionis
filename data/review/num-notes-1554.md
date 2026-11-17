# Numbers: a footnote from Castellio's 1554 annotations (1)

Proposed 2026-11-16, by the method used for Genesis, Exodus and Leviticus (`data/review/gen-exod-notes-1554.md`,
`lev-notes-1554.md`, `lev23-24-note.md`): every annotation on Numbers in the 1554 Basel edition was read on the page
and sorted into (a) deliberate departures from the Hebrew as read today, (b) words no dictionary has that Castellio
explains himself, (c) commentary or defences of Latin a reader can follow (no note), and (d) places where the
annotation shows the settled text (1738) differs from what he meant. Decisions 53 and 56; brief.md, "brief Latin
footnotes". The note sits right after its word; the Hebrew is the WLC's (`sources/parallel/wlc`) without the
cantillation marks.

**Where the annotations are** (MDZ bsb10196330; images `https://api.digitale-sammlungen.de/iiif/image/v2/bsb10196330_00821/…`,
read 2026-11-16): *In Numeros* fills canvas 821 alone, from the middle of the left column (column 337, after the end
of the Leviticus 23:40 note) to the lower right column (column 338), where *In Deuteronomium* begins. Fifteen
annotations (the 21:29 one runs on to 21:30), under the heads *EX CAP. XIII., XXI., XXII., XXIII., XXIIII., XXVII.,
XXX., XXXIIII.*; the full list, in the page's order, is at the end. Crops read: `c821-L1.jpg` … `c821-L4.jpg`,
`c821-ar.jpg`, `c821-R1.jpg` … `c821-R4.jpg` in this folder.

**Quotations** follow the page: u/v and i/j as printed, the tilde for a nasal (*magnũ*), *s* for ſ, *ß* written
*ss*. **Modern renderings** were surveyed on Bible Gateway's all-translations page for each verse and in the JPS
translations on Sefaria (revised JPS 2023, Contemporary Torah 2006, NJPS 1985, JPS 1917), 2026-11-16.

The settled text (1738) still has Castellio's reading at the one place proposed. No (d) corrections: every lemma
matches the settled text (the lemma of 34:6, *Ad occidentalem terminum habebitis mare*, has an *Ad* that the 1554
text itself lacks: MDZ search, canvas 102, *Occidentalem terminum habebitis mare, & ipsum terminum*; so does 1738).

## 1. Num 21:24 *Nam Ār terminus est Ammonītārum*

The Hebrew כִּי עַז גְּבוּל בְּנֵי עַמּוֹן is "for the border of the children of Ammon was strong" (KJV; Vulgate *quia forti
præsidio tenebantur termini Ammonitarum*; Septuagint ὅτι Ἰαζὴρ ὅρια υἱῶν Ἀμμάν ἐστι, "for Jazer is the border").
Castellio (canvas 821, column 337, *EX CAP. XXI.*): *Nam Ar terminus est Ammonitarum.) In Hebræo עז legitur, sed
mendose, ut ego conijcio, tum quia hic legitur in Græco ἰαζὴρ, quod exit in r: tum quia Deuter. 2. idem locus Ar
uocatur, inter Moabitas & Ammonitas positus, his uerbis: Transiturus es hodie Moabitarum terminum, uidelicet Ar.* So
he emends עַז to ער, the town Ar (Deut 2:18), on two grounds: the Greek name ends in *r*, and Deuteronomy calls Ar a
border. 1554's text has the same reading (*Nam Ar terminus*, in the lemma; the settled text *Nam Ār terminus est
Ammonītārum*).

Modern renderings (Bible Gateway, 2026-11-16): most have "strong / fortified / strongly defended" (NRSVue "for the
boundary of the Ammonites was strong", ESV, NIV "because their border was fortified", NET, NKJV, CSB, CEB, NLT, LEB,
WEB…); some follow the Septuagint with "Jazer" (RSV "for Jazer was the boundary of the Ammonites", NABRE, NASB,
NASB1995, LSB). The JPS (NJPS 1985, Contemporary Torah, revised JPS 2023) read עַז as a place name: "for Az marked the
boundary of the Ammonites", noting "Septuagint 'Jazer,' cf. v. 32. Others 'for the boundary of the Ammonites was
strong.'" No version surveyed has Ar. Castellio's reading is his own conjecture against the Hebrew, the Greek (which
he cites for its final *r*) and every modern reading; the reader comparing a modern Bible sees a different town, or a
town where the Hebrew has an adjective.

> *Hebraicē כִּי עַז גְּבוּל בְּנֵי עַמּוֹן, ‘nam validus erat fīnis Ammonītārum’, ut plērīque hodiē intellegunt (aliī cum Græcīs ‘Jazēr’ legunt); Castelliō, quia Græcum nōmen in r exit et Ār alibī terminus dīcitur, עָר, ‘Ār’, legit.*

("Hebrew 'for the border of the Ammonites was strong', as most now understand it (others read 'Jazer' with the
Greek); Castellio, because the Greek name ends in *r* and Ar is elsewhere called a border, reads *ʿar*, 'Ar'.")

Words checked with `pipeline latin macron` (validus, plērīque, dīcitur, alibī, exit, nōmen; *Græcum* and *Græcī* Gaffiot
only; *fīnis*, *Ammonītārum* and *Jazēr* (21:32) as the settled text has them). *Fīnis* for the Hebrew גְּבוּל, as the
settled text uses *fīnēs* for borders; Castellio's own *terminus* is the word the note is about, so it is kept for him.
Shorter, if preferred: *Hebraicē כִּי עַז, ‘nam validus erat’ (Græcī ‘Jazēr’); Castelliō, mendum ratus, עָר, ‘Ār’, legit.*

**Decision:** accept, the shorter wording (Nathan, 2026-11-16: "Shorter wording")
**Apply:** `Num.21.24` la: `Nam Ār terminus est` → `Nam Ār\f + \fr 21:24 \ft Hebraicē כִּי עַז, ‘nam validus erat’ (Græcī ‘Jazēr’); Castelliō, mendum ratus, עָר, ‘Ār’, legit.\f* terminus est`

## 1a. Num 21:24, the note shortened

**Decision:** accept (Nathan, 2026-11-16: "I think we can drop *(Græcī ‘Jazēr’)*.")
**Apply:** `Num.21.24` la: `‘nam validus erat’ (Græcī ‘Jazēr’); Castelliō` → `‘nam validus erat’; Castelliō`

## 1b. Num 21:24, *mendum subesse ratus*

*Mendum ratus* has no precedent in the corpus (The Latin Library, `latin attest`), and *reor* wants an accusative and
infinitive. *Mendum subesse*, "a fault lies in the text", is Erasmus's phrase for a corrupt reading (*Adagia* I.vi.1,
I.viii.58: *suboleat mendum subesse exemplaribus*); *mendum* for a scribal error is Cicero's and Gellius's (I.7).

**Decision:** accept (Nathan, 2026-11-16: "Use *mendum subesse ratus*")
**Apply:** `Num.21.24` la: `Castelliō, mendum ratus,` → `Castelliō, mendum subesse ratus,`

## Not proposed

**Num 13:23–24** *ad fluvium Escōlem*, looked at closely. נַחַל אֶשְׁכֹּל is "the valley of Eshcol" (Vulgate *Torrentem
botri*, Septuagint φάραγξ βότρυος, "ravine"). Castellio (canvas 821, column 337, *EX CAP. XIII.*): *Ad fluuium
Escolem.) נחל non semper torrentem fluuium, sed sæpe perennem significat. Itaque hoc nomine utitur alibi Moses, cũ de
Arnone loquitur, quem Ioseph. ποταμὸν, id est fluuiũ uocat, Antiquit. 4. cap. 4. & 1. Machab. 5. idem χείμαρρος &
ποταμὸς uocatur.* Modern versions: nearly all "Valley of Eshcol" (NIV, ESV, NASB, NKJV, NET, CSB…), "Wadi Eshcol"
(NRSV(ue), NABRE, OJB), "brook of Eshcol" (KJV, YLT). His *fluvius* is argued, but it is a word for a place-name's
first element, and English versions themselves vary between valley, wadi and brook (a wadi carries water in season):
by the NT test, a rendering that keeps the sense. No note, unless Nathan wants one; draft:
*Hebraicē נַחַל אֶשְׁכֹּל, ‘vallis Escōl’; Castelliō, quod נַחַל sæpe perennem fluvium significat, ‘fluvium’ vertit.*

**Num 21:30** *Atquī lūx eōrum Hesebōn periit*. The Hebrew וַנִּירָם אָבַד חֶשְׁבּוֹן is obscure (all three JPS
translations: "Meaning of verse uncertain"). Castellio's *lūx eōrum* takes נִירָם as "their lamp" (ניר); his annotation
does not argue the reading, it only explains the metaphor: *Atqui lux eorum Hesebon: poeticè dictum est, pro capite
regni, & urbe fortissima.* Modern versions split: a verb, "we have shot at them / overthrown them" (KJV, ESV, NIV, NET,
NASB, JPS), "their posterity" with the Septuagint (RSV, NRSV(ue), GNT), "their dominion / empire / kingdom" from the
same noun (NABRE, Geneva, Rashi's "sovereignty"; Vulgate *Jugum ipsorum*). A passage modern scholarship calls
uncertain, where his noun stands near the "dominion" reading: no note.

**Num 22:32** *istud iter susceptum est contrā meam sententiam*: Castellio follows Josephus (*Ita interpretatur
Iosephus*, quoting him in Greek, printed with ligatures; as I read it, τὴν ὁδὸν παρὰ γνώμην τοῦ θεοῦ γενομένην, "the
journey made against God's will", not checked against a Josephus edition). כִּי־יָרַט הַדֶּרֶךְ
לְנֶגְדִּי is "because your way is perverse before me" (NRSVue, ESV, KJV) or "reckless" (NIV, NASB); but NABRE has
"because this rash journey of yours is against my will", GNT "you should not be making this journey", LSB "your way
was contrary to me". His reading matches modern ones (as Exod 17:16 was dropped). No note.

## All annotations, sorted

(a) = proposed above as a departure; (c) = commentary or defence of Latin, no note; (c*) = looked at closely and not
proposed, above. All on canvas 821.

| Verse | Lemma (as printed) | Summary | Kind |
|---|---|---|---|
| 13:23 | *Ad fluuium Escolem* | נחל often a perennial river, not a torrent; Josephus calls the Arnon ποταμός | c* |
| 21:24 | *Nam Ar terminus est Ammonitarum* | עז emended to ער (Ar), with the Greek ἰαζὴρ and Deut 2 | **a** (1) |
| 21:14–15 | *Ad flumina Arnonis* | the plural for one river, as Virgil *flumina Thermodontis*, Ps 74 | c |
| 21:29–30 | *Perijsti Chamosi gens, cuius & mares fusi* | change of person, as Gen 49; *dedit filios* singular for plural and passive; *lux eorum Hesebon* poetic for the capital | c (21:30 c*) |
| 22:22 | *Quo eius itinere irato Deo* | God wanted Balaam to bless; Balaam meant to curse | c |
| 22:30 | *Nunquid tale sum tibi facere solita* | the ass's reasoning | c |
| 22:32 | *Istud iter susceptum est contra meam sententiam* | follows Josephus | c* |
| 23:9 | *En populum seorsum habitaturum* | the most excellent people, set apart and singular | c |
| 23:10 | *Quis Iacobeorum pulueris* | an innumerable multitude | c |
| 24:4 | *Qui ab Omnipotente præsignificata uidit* | מחזה: of men a vision, of God a foretelling (as ברך) | c |
| 24:7 | *Cuius de situla* | offspring that grows like trees in wet ground; Agag a title like Pharaoh | c |
| 24:24 | *Cum classis ex Cittimorum finibus* | who the Kittim are: Josephus (Cyprus, Citium), Isa 23, 1 Macc 1 and 8; Greeks or Macedonians | c |
| 27:19 | *Eiq; in eorum oculis præcipito* | i.e. give him precepts and teach him; Cicero, *De officiis* 1 | c |
| 30:5 | *Omnia eius uota irrita sunto* | if a father may annul a daughter's vow, he may annul a betrothal made without him | c |
| 34:6 | *Ad occidentalem terminum habebitis mare* | "the great sea" made "the sea", as Josh 1 | c |

## 1738's own footnotes in Numbers

1738 prints lettered glosses at the foot of the page, the letters running a–o (no j) and starting again at a new
gathering (signatures I, K, L). Read on the page images (archive.org `bibliasacraexseb01cast`, `page/n<N>.jpg`;
archive leaf n = the read file's leaf − 1), 2026-11-16: 25 in Numbers, against 11 `%footnote` rows in
`data/witnesses/read-1738/Num1-36.tsv`, which misses the ones the OCR ran into other lines or dropped (6:21, 7:85,
8:2, 14:21–22, 15:30, 18:19, 19:9, 22:5, 22:7, 24:4 *l*, *m*, 27:3, and the one it records as *a) non statim* is
*o)*). The verse is where the footnote letter stands in the text, seen on the page, except where marked "by sense"
(the letter not looked for). Crops: `fn-<n>.jpg` (page foot, three leaves stacked) and `q<n>-<0–3>.jpg` (page
quarters) in this folder. (Leaf n186's *b) in pastorum custodia est* belongs to Lev 27:32, *quidquid ᵇ sub pedum
mittitur*.)

| Leaf (n) | Verse | Letter and text (as printed) | Word it glosses (1738) | Source |
|---|---|---|---|---|
| 189 | 3:38 | *a) vt Israelitarum omnium vice sacra procurarent.* | *ad procurationem Israelitarum* | none seen |
| 189 | 3:38 | *b) non eius generis.* | *qui alienus* | none seen |
| 192 | 6:21 | *c) hæc omnino libare cogetur. Si quid præterea libare sua sponte pro sua facultate volet, licebit.* | *præter ea, quæ feret eius facultas* | none seen |
| 193 | 7:85 | *d) centenos tricentenos siclos pendentes.* | *centenariæ tricenariæ* | none seen |
| 194 | 8:2 (by sense) | *e) rostra (in quibus ellychnia sunt) haberent antrorsum spectantia.* | *vt versus candelabri conspectum lucerent* | none seen |
| 198 | 11:25 | *f) ad verbum: ita vaticinabantur, vt nihil adderent: hoc est, vt id vnum continenter agerent.* | *tum, sine intermissione vaticinabantur* | none seen (gives the Hebrew לֹא יָסָפוּ literally) |
| 198 | 12:4 | *g) scil. ex castris: nam extra castra erat tabernaculum.* | *exirent* | none seen |
| 200 | 14:21 | *h) officiam* [sic, for *efficiam*]*, vt vbique terrarum prædicer.* | *Iouæ gloria* | none seen |
| 200 | 14:22 | *i) gloriosa facta.* | *gloriam meam* | none seen |
| 202 | 15:30 | *k) crimen alioquin capitale commiserit.* | *volens fecerit* | none seen |
| 205 | 18:9 | *a) sacrificio, quod igne fit.* | *ex igne sacrosancta* | none seen (cf. his Exodus annotation on 29:18, אשה as *res diuina*, a different point) |
| 206 | 18:19 | *b) incorruptum inuiolatumque.* | *fœdus salitum* | none seen |
| 206 | 19:9 | *c) huius vaccæ cinerem ad faciendum aquam lustralem, vt paullo post docetur.* | *Hoc seruabit* | none seen |
| 208 | 20:12 | *d) in eo peccatum est, quod dixerunt, eliciamus, quod Dei erat; sibi tribuentes. Vide Deut. I. 37.* | *quoniam vos mihi non credidistis* | **Castellio's 1554 annotation on Deut 33:8** (canvas 823, column 341, crop `c823-deut33-8.jpg`): *Deo fidem nõ habuerunt, cum aquam ex petra elicuerũt. cum enim deberent eius rei gloriam Deo tribuere, in eo peccarunt, quòd dixerunt: Attendite rebelles, an uobis aquam ex hac petra eliciamus.* |
| 210 | 22:5 | *e) Euphratem.* | *apud flumen* | none seen |
| 210 | 22:7 | *f) quos scilicet ipsi Madianitæ mittebant, ad Balaamo persuadendum, vt Balaco gratificarentur.* | *Madianitarumque* | none seen |
| 212 | 23:10 | *g) innumerabilitatis.* | *pulueris* | **Castellio's 1554 annotation on 23:10**: *Quis Iacobeorum pulueris? id est, innumerabilis multitudinis.* |
| 212 | 23:21 | *h) fortitudine militari.* | *clangore comitante regio* | none seen |
| 212 | 23:23 | *i) Non sunt, quæ de Israelitis dico, vana, qualia sunt hariolorum; sed vera, et suo tempore comprobanda.* | *Neque vero* | none seen |
| 212 | 24:3 | *k) scil. quum angelum ante asinam non vidit.* | *clausis oculis* | none seen |
| 212 | 24:4 | *l) quum asina succubuit.* | *lapso* | none seen |
| 212 | 24:4 | *m) quum vidit angelum.* | *patefacti sunt oculi* | none seen |
| 216 | 27:3 | *n) scil. inter eos, qui illis XL annis perierunt.* | *sed ob suum peccatum mortuum esse* | none seen |
| 219 | 30:15 (by sense) | *o) non statim sed quum iam in silentio comprobasset.* | *postea* | none seen |
| 223 | 33:3 (by sense) | *a) cum magnis copiis.* | *ingenti manu* | none seen |

**What they are**: short explanatory glosses on Castellio's Latin (a paraphrase, the literal Hebrew, a place named,
the event alluded to), in the manner of the Genesis ones (*Ganges*, *Nilus*) and Exod 1:21 *progeniem* recorded in
`docs/editions.md`. Two come from Castellio's own 1554 annotations, condensed: 23:10 from his note on that verse, and
20:12 from his note on Deut 33:8 (with a cross-reference to Deut 1:37). The other 23 match nothing in his annotations
on Numbers (or the Deuteronomy passage); their source was not found. 1750's OCR (`sources/archive/1750/text.txt`) has
none of *innumerabilitatis*, *fortitudine militari*, *capitale commiserit*, *quod igne fit*, so 1750 seems not to
print them (not checked on its pages). None departs from the Hebrew or explains a word no dictionary has, so none is
proposed. (1738 also prints asterisks in the text at 23:9 *neque inter ceteras gentes*, 23:10 *quis vel quartæ* and
24:4 *cui lapso*; what they mark was not looked into.)
