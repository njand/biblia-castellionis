# 2 Corinthians: light notes, brackets and a correction

Built 2026-11-17 by the process in `nt-notes-process.md`, with the test and wording of `nt-notes-form.md`: "the modern
editions" means SBLGNT and NA28, against the TR.

**Sources read:**
- `2cor-notes-candidates.md` (`python -m pipeline notes 2Cor`): 57 apparatus units in 49 verses, 38 TR-alone readings.
- The whole letter, read verse by verse against the TR, SBLGNT, BSB, WEB, the Vulgate and 1573 as printed
  (`text/orig/2CO.usfm`) by one reader, with every line of the SBLGNT apparatus. Each finding was checked here.
- The NRSVue (Bible Gateway, read 2026-11-17) for every verse below: it reads with the modern text against Castellio,
  and none of its footnotes gives his sense as an alternative, except where an item says so.
- For 13:4, the OCR of the later printings.

## A. Notes where the Greek text differs (the modern editions against the TR)

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

1. **4:14** *per Jēsum*: TR διὰ Ἰησοῦ, "through Jesus"; the modern editions σὺν Ἰησοῦ (NRSVue "will raise us with Jesus").
   **Apply:** `2Cor.4.14` la: `per Jēsum suscitet,` → `per Jēsum\f + \fr 4:14 \ft Cōdicēs antīquiōrēs habent σὺν Ἰησοῦ, ‘cum Jēsū’.\f* suscitet,`
2. **6:16** *Vōs … templum estis*: TR Ὑμεῖς … ἐστε; the modern editions ἡμεῖς … ἐσμεν (NRSVue "we are the temple of the living God", whose footnote gives "you" as another reading). A change of person, as at Rom 8:2.
   **Apply:** `2Cor.6.16` la: `Vōs enim vīventis Deī templum estis,` → `Vōs enim vīventis Deī templum estis\f + \fr 6:16 \ft Cōdicēs antīquiōrēs habent ἡμεῖς … ἐσμεν, ‘nōs … sumus’.\f*,`
3. **8:7** *istō ergā nōs amōre*: TR τῇ ἐξ ὑμῶν ἐν ἡμῖν ἀγάπῃ, "your love for us"; the modern editions τῇ ἐξ ἡμῶν ἐν ὑμῖν (NRSVue "our love for you", footnote "your love for us").
   **Apply:** `2Cor.8.7` la: `et istō ergā nōs amōre,` → `et istō ergā nōs amōre\f + \fr 8:7 \ft Cōdicēs antīquiōrēs habent τῇ ἐξ ἡμῶν ἐν ὑμῖν ἀγάπῃ, ‘nostrō ergā vōs amōre’.\f*,`
4. **11:3** *ā simplicitāte*: the modern editions add καὶ τῆς ἁγνότητος (NRSVue "a sincere and pure devotion", footnote "lack *and pure*").
   **Apply:** `2Cor.11.3` la: `ā simplicitāte, quæ` → `ā simplicitāte\f + \fr 11:3 \ft Cōdicēs antīquiōrēs addunt καὶ τῆς ἁγνότητος, ‘et castitāte’.\f*, quæ`

## B. Notes where Castellio's Latin says what the Greek does not

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

5. **6:12** *sed ergā hominem, cui estis intimī*: the Greek (TR and SBLGNT) στενοχωρεῖσθε δὲ ἐν τοῖς σπλάγχνοις ὑμῶν, "you are restricted in your own affections" (NRSVue "but only in yours"). Castellio brings in a third person the Greek does not have; 1573 the same.
   **Apply:** `2Cor.6.12` la: `sed ergā hominem, cui estis intimī.` → `sed ergā hominem, cui estis intimī\f + \fr 6:12 \ft Græcē στενοχωρεῖσθε δὲ ἐν τοῖς σπλάγχνοις ὑμῶν, ‘sed in vestrīs ipsōrum animīs estis angustī’.\f*.`
6. **13:4** *per Deī in nōs potentiam*: the Greek (TR and SBLGNT) ἐκ δυνάμεως Θεοῦ εἰς ὑμᾶς, "by the power of God … in dealing with you" (NRSVue). *in nos* in 1573 and 1758: Castellio's own.
   **Apply:** `2Cor.13.4` la: `per Deī in nōs potentiam.` → `per Deī in nōs potentiam\f + \fr 13:4 \ft Græcē εἰς ὑμᾶς, ‘in vōs’; Castelliōnis ēditiōnēs ‘in nōs’.\f*.`

## C. Brackets: words the modern editions leave out

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

In each, the NRSVue lacks the words. Item 10 is a word no Greek has.

7. **4:10** *Dominī*: TR τὴν νέκρωσιν τοῦ Κυρίου Ἰησοῦ (NRSVue "the death of Jesus"), as Acts 7:30.
   **Apply:** `2Cor.4.10` la: `Semper Dominī Jēsū occīsiōnem` → `Semper [Dominī] Jēsū occīsiōnem`
8. **5:17** *omnia*: TR γέγονε καινὰ τὰ πάντα (NRSVue "new things have come into being", footnote "everything has become new").
   **Apply:** `2Cor.5.17` la: `nova facta sunt omnia:` → `nova facta sunt [omnia]:`
9. **8:4** *reciperēmus*: TR δέξασθαι ἡμᾶς, the TR alone (NRSVue "begging us earnestly for the favor of partnering in this ministry"). As at Rom 15:24, the Latin is left without its verb, as the modern text is.
   **Apply:** `2Cor.8.4` la: `officium reciperēmus.` → `officium [reciperēmus].`
10. **4:4** *inaspectābilis*: in no Greek (TR and SBLGNT ὅς ἐστιν εἰκὼν τοῦ Θεοῦ; NRSVue "the image of God"); Castellio takes it from Col 1:15. 1573 prints *inaspectabilis*.
    **Apply:** `2Cor.4.4` la: `imāgō Deī inaspectābilis.` → `imāgō Deī [inaspectābilis].`
11. **13:14** *Āmēn*: TR ἀμήν (NRSVue ends 13:13 without it).
    **Apply:** `2Cor.13.14` la: `adsit omnibus. Āmēn.` → `adsit omnibus. [Āmēn.]`

## D. A correction to the edited text

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

12. **10:10** cases: *corporis præsentiā imbēcillā, ōrātiōque abjectā est* → *corporis præsentia imbēcilla, ōrātiōque abjecta est*. The clause needs nominatives (παρουσία … ἀσθενής, ὁ λόγος ἐξουθενημένος), as 1573 prints (*præsentia imbecilla, oratioque abiecta est*); the ablative macrons break the grammar.
    **Apply:** `2Cor.10.10` la: `præsentiā imbēcillā, ōrātiōque abjectā est` → `præsentia imbēcilla, ōrātiōque abjecta est`

## Considered and left out

- 1:11, 7:13, 8:19, 12:1 (Καυχᾶσθαι δεῖ): a change of person, or a shade; 9:4 *glōriātiōnis*, 12:9 *mea*, 12:11 *quī glōriātus sim*, 13:2 *scrībō*: a word that changes nothing a reader needs.
- 1:12, 4:6, 4:14 *Dominum*, 5:3: SBLGNT and NA28 disagree, or NA28 keeps the TR's word.
- 1:6–7, 8:13–14, 10:4–5, 13:12–14: verse division only.
- 1:23 *nōndum Corinthum vēnisse* for οὐκέτι: *nōndum* can carry "not yet again".
- 1:24 *fīdūciam dērogēmus*, 11:2 *obtrectō*: his paraphrase and vocabulary.
- 12:7 *tundat* (1573 *tondat*), 11:28 *distinent* (1573 *destinent*), 10:5 *dēturbāmus* (1573 *derurbamus*): the edited text already has the right word; `text/orig` keeps the print.
