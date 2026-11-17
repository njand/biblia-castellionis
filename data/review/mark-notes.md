# Mark: light notes and brackets (the pilot)

Built 2026-11-16 by the process in `nt-notes-process.md` (decided the same day). Sources read:
`mark-notes-candidates.md` (`python -m pipeline notes Mark`: 272 apparatus units in 227 verses); the whole of Mark
read verse by verse against the TR, SBLGNT, BSB and WEB (four readers, chapters 1–4, 5–8, 9–12, 13–16, each finding
checked here against the files); the NET Bible's notes (netbible.org) for every verse below; the NRSVue (Bible
Gateway) for every verse below. Nothing from the NET or the NRSVue is copied here beyond a word or two.

Three kinds of change, following the decisions already made:

- **Notes** (`\f`), in Latin, in the form of the six already in the text: where the Greek now read says something
  else, or where Castellio's Latin says what no Greek says.
- **Brackets** `[…]` (decision 53, `brackets-and-notes.md` §1, the front matter's notae: *Verba quæ ēditiōnēs Græcæ
  hodiernæ omittunt*): words his Greek had and the modern critical text does not. Until now only whole verses were
  bracketed; these are phrases.
- **One correction**: a misprint of 1573's, as printed in `text/orig/` (which keeps it, decision 58).

In every case below the NRSVue reads with the modern text against Castellio, and the NET's note (where it has one)
does not call the point open.

## A. Notes where the Greek text differs (four editions with SBLGNT against RP)

**Decision:** accept (Nathan, 2026-11-16: "Accept all")

1. **1:2** *in vātibus*: the TR has ἐν τοῖς προφήταις; SBLGNT, WH, Treg, NA28 ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ. NET (tc):
   "in the prophets" is the reading of most later manuscripts; "in Isaiah the prophet" is early and widespread.
   NRSVue: "in the prophet Isaiah". The edition spells *Ēsāiās*.
   **Apply:** `Mark.1.2` la: `in vātibus:` → `in vātibus\f + \fr 1:2 \ft Græcē hodiē legitur ἐν τῷ Ἠσαΐᾳ τῷ προφήτῃ, ‘in Ēsāiā vāte’.\f*:`
2. **3:29** *suppliciō sempiternō*: TR αἰωνίου κρίσεως, "eternal judgment" (his *supplicium*); the four editions
   αἰωνίου ἁμαρτήματος, "eternal sin". NRSVue "guilty of an eternal sin"; NET has no text note here (its note is on
   the sense).
   **Apply:** `Mark.3.29` la: `suppliciō sempiternō.”` → `suppliciō sempiternō\f + \fr 3:29 \ft Græcē hodiē legitur αἰωνίου ἁμαρτήματος, ‘æternī peccātī’.\f*.”`
3. **5:1** *Gadarēnōrum*: TR Γαδαρηνῶν; the four editions Γερασηνῶν. NET (sn, tc): Gerasenes here, Gadarenes in
   Matt 8:28, a complicated tradition. NRSVue "Gerasenes" (with its own note). Wiktionary *Gerasēnus*.
   **Apply:** `Mark.5.1` la: `Gadarēnōrum,` → `Gadarēnōrum\f + \fr 5:1 \ft Græcē hodiē legitur Γερασηνῶν, ‘Gerasēnōrum’.\f*,`

## B. Notes where Castellio's Latin says what the Greek does not

**Decision:** accept (Nathan, 2026-11-16: "Accept all")

4. **1:10** *quī Jōhannēs … vīdit*: the Greek (TR and SBLGNT) has ἀναβαίνων … εἶδεν with no subject; the subject is
   Jesus, who has just been baptized (BSB "Jesus", NRSVue "he", NET: "the subject (Jesus) specified"). Castellio
   makes John the one who comes out of the water and sees the Spirit (as in John 1:32–34). 1573: *qui Iohannes simul
   ac ex aqua egressus est, vidit*.
   **Apply:** `Mark.1.10` la: `quī Jōhannēs simul` → `quī Jōhannēs\f + \fr 1:10 \ft Græcē εἶδεν sine nōmine; Castelliō Jōhannem intellegit, doctī nostræ ætātis Jēsum, quī ex aquā ascendit.\f* simul`
5. **12:29** *Deus vester*: Greek (TR and SBLGNT) ὁ θεὸς ἡμῶν, "our God", as Deut 6:4. 1573 *vester*; the Vulgate
   *tuus*, so Castellio may follow the address to Israel, not slip. BSB, WEB, NRSVue "our God". 1556 not seen (its
   cached pages do not reach Mark 12).
   **Apply:** `Mark.12.29` la: `Deus vester,` → `Deus vester\f + \fr 12:29 \ft Græcē ὁ θεὸς ἡμῶν, ‘Deus noster’.\f*,`
6. **12:42** *duōs terunciōs … teruncius īdem quod quadrāns*: Greek (TR and SBLGNT) λεπτὰ δύο, ὅ ἐστι κοδράντης:
   the two coins together make a quadrans. Castellio makes each coin a quadrans, so she gives two. NRSVue "two small
   copper coins, which are worth a penny" (one coin of that value). 1573 as the text.
   **Apply:** `Mark.12.42` la: `quod quadrāns.` → `quod quadrāns\f + \fr 12:42 \ft Græcē λεπτὰ δύο, ὅ ἐστι κοδράντης: duo nummī simul quadrantem efficiunt.\f*.`
7. **15:16** *extrā ātrium*: Greek (TR and SBLGNT) ἔσω τῆς αὐλῆς, "inside the courtyard"; the Vulgate *in atrium*;
   NRSVue "led him into the courtyard of the palace". Castellio's *extrā* reverses it. 1573 *eo extra atrium*,
   Wikisource the same; whether he meant it or it is a slip, the 1556 pages at hand do not show.
   **Apply:** `Mark.15.16` la: `extrā ātrium,` → `extrā ātrium\f + \fr 15:16 \ft Græcē ἔσω τῆς αὐλῆς, ‘intrā ātrium’.\f*,`

## C. Brackets: words the critical text leaves out (four editions with SBLGNT against RP)

**Decision:** accept (Nathan, 2026-11-16: "Accept all")

8. **2:17** *ad frūgem*: TR adds εἰς μετάνοιαν, "to repentance" (from Luke 5:32); the four editions omit it.
   NRSVue omits it.
   **Apply:** `Mark.2.17` la: `sontēs ad frūgem.”` → `sontēs [ad frūgem].”`
9. **6:11** the sentence on Sodom and Gomorrah: TR adds ἀμὴν λέγω ὑμῖν, ἀνεκτότερον ἔσται … (from Matt 10:15); the
   four editions omit it; NRSVue ends the verse with "as a testimony against them".
   **Apply:** `Mark.6.11` la: `testimōniō. Hoc vōbīs` → `testimōniō. [Hoc vōbīs`
   **Apply:** `Mark.6.11` la: `cum illā cīvitāte.”` → `cum illā cīvitāte.]”`
10. **10:21** *crucem ferēns*: TR adds ἄρας τὸν σταυρόν; the four editions omit it; NRSVue "then come, follow me".
   **Apply:** `Mark.10.21` la: `mē, crucem ferēns, secūtum` → `mē, [crucem ferēns,] secūtum`
11. **13:14** *ā Daniēle vāte prædictum*: TR adds τὸ ῥηθὲν ὑπὸ Δανιὴλ τοῦ προφήτου (from Matt 24:15); the four
   editions omit it.
   **Apply:** `Mark.13.14` la: `nefās ā Daniēle vāte prædictum, stāre` → `nefās [ā Daniēle vāte prædictum,] stāre`

## D. Brackets outside the four-edition test (WH, NA28 and SBLGNT against RP, Tregelles with RP)

Your test (1: A) needs Tregelles too; at these five he sides with RP. They are among the best known variants in
Mark: NA28, SBLGNT and WH omit them, the NET calls each a later addition (9:29 "a motivated reading", 10:24 "natural
scribal expansions", 14:24 "almost surely influenced by … Luke 22:20", 7:8 "floating texts"), and the NRSVue omits
each and footnotes it. **Recommendation: accept**; the test would then read "WH and NA28 with SBLGNT, Tregelles
either way" for the rest of the NT.

**Decision:** accept (Nathan, 2026-11-16: "Accept all")

12. **7:8** *urceōrum, pōculōrumque lōtiōnēs …*: TR adds βαπτισμοὺς ξεστῶν καὶ ποτηρίων … ποιεῖτε.
   **Apply:** `Mark.7.8` la: `īnstitūtum, urceōrum` → `īnstitūtum[, urceōrum`
   **Apply:** `Mark.7.8` la: `multa facitis.”` → `multa facitis].”`
13. **9:29** *et jejūniīs*: TR καὶ νηστείᾳ.
   **Apply:** `Mark.9.29` la: `precibus et jejūniīs.”` → `precibus [et jejūniīs].”`
14. **9:49** *et omne sacrificium sale saliendum est*: TR καὶ πᾶσα θυσία ἁλὶ ἁλισθήσεται.
   **Apply:** `Mark.9.49` la: `saliendī, et omne sacrificium sale saliendum est.` → `saliendī[, et omne sacrificium sale saliendum est].`
15. **10:24** *frētōs pecūniīs*: TR τοὺς πεποιθότας ἐπὶ χρήμασιν.
   **Apply:** `Mark.10.24` la: `est, frētōs pecūniīs in` → `est, [frētōs pecūniīs] in`
16. **14:24** *novī*: TR τῆς καινῆς διαθήκης.
   **Apply:** `Mark.14.24` la: `meus novī fœderis` → `meus [novī] fœderis`

## E. A misprint corrected

**Decision:** accept (Nathan, 2026-11-16: "Accept all")

17. **5:3** *vincere* ("conquer") for *vincīre* ("bind"), Greek δῆσαι, "to bind". 1573 and the 1726 OCR print
   *vincere*; the 1681 and 1758 OCRs *vincire*; Wikisource *vincere*. The next verse speaks of chains and fetters
   (*catēnīs … vīnctō*). Gaffiot *vincĭō, vīnxī, vīnctum, īre*. `text/orig/MRK.usfm` keeps *vincere*, as printed.
   **Apply:** `Mark.5.3` la: `poterat vincere quisquam` → `poterat vincīre quisquam`

## Considered and left out

From the apparatus (the four editions against RP, the TR with RP), not a change a reader needs told:
- Clauses: 3:5 *tam sāna … quam erat altera* (adds only "healthy as the other"); 5:12 *dæmonēs omnēs*; 6:33 *ad eum
  convēnērunt*; 11:10 *in nōmine Dominī*; 13:18 *vestra fuga*; 14:19 the second "Is it I?"; 14:27 *mē … hāc nocte*.
  Each repeats or fills in what the verse already says. (Tregelles with RP, also left out: 3:16, 8:26, 12:30, 12:33,
  13:15.)
- Names: 1:24 *Heu*; 2:16, 2:18 (scribes *of* the Pharisees, or *and*); 5:9 and 5:15 *Legiō* (spelling); 10:47
  *Nāzarēnum*; 15:47 *Jōsis* (form of the name).
- Numbers: 9:31 and 10:34, "on the third day" for "after three days": the same event, and Matthew and Luke have
  "the third day".
- Single words (207): tense, compound for simple verb, "Jesus" supplied as subject, and the like.

From the reading of each chapter:
- 1:34 *sē scīre eum esse Chrīstum*: he takes ὅτι as "that", not "because" (NRSVue, BSB), and *Chrīstum* is a
  variant his TR lacks (NET tc lists it in B L W Θ and others). His construal is possible; a note would need both
  points.
- 3:34 *discipulīs* for "those sitting around him": a harmonization with Matt 12:49, no change of sense worth a note.
- 7:3 *sæpe*: the Vulgate's *crebro*; πυγμῇ is itself disputed, so the modern sense is not settled.
- 7:11 Corban: Castellio has the son promise that his offering will benefit the parent, the Vulgate's construal; the
  sense of the passage (the parent goes without) still stands.
- 9:12 a statement for the question "how is it written…?": the KJV and the Vulgate read it so too; the sense is
  close.
- 9:18 *tābēscat* (KJV "pineth away") for "becomes rigid"; 12:33 *omnī studiō* for "all understanding"; 11:4
  *in biviō* (the Vulgate's); 10:32 one group afraid for two; 6:20 *observābat*; 6:33 *aggressī* for "arrived before
  them"; 14:3 *spīcātæ nardī* (the Vulgate's): a word's shade, not a different statement.
- 13:30 *hoc sæculum*, 14:27 *dēserētis*, 14:41 a command for a question, 14:65 *Dīvīnā*: possible renderings.
