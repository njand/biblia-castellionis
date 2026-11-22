# 1 Kings 12–22: light notes (Old Testament search), reader B

Built 2026-11-22 in phase 2 of decision 85 (PLAN.md §4), beside `propose`, by the process in `ot-notes-process.md`
(decisions 1A–4A), as 2 Samuel's (`../2sam1-24-phase2/notes-a.md`, `notes-b.md`, settled 2026-11-21) and reader A's
chapters 1–11 (`notes-a.md`), with the bar as it now stands (Nathan, 2026-11-19: no note for a departure without plot or
theological significance, a name, place or number included; 2026-11-21: a name that changes who did or suffered what, or
makes the book contradict itself, with the modern Bibles agreeing against Castellio, does get one; `num-notes.md` §F: a
construal the context sets right is left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient
version and Castellio keeps it; kinds B and C where his reading or his text departs from the Hebrew against the NRSVue,
the BSB and the Hebrew agreeing, and nobody calls the passage uncertain. Castellio's 1554 annotations on these chapters
and the 1554 text's margins, read on the page in this pass, are in `notes-1554-b.md`. Names in note text as the preview
has them (*Roboāmum*, `text/draft/1KI.preview.usfm` 12:6, 14:30).

**Sources read:**
- `../1kgs-notes-candidates.md` (`python -m pipeline notes 1Kgs`), its entries for chapters 12–22: Castellio's marks at
  14:25, 15:8 and 18:22 (14:25 is a false placement: the 1738 OCR line *butarii. G. donee Pharao Aegypti rex* is Joshua
  16:10's Greek addition, `text/orig/JOS.usfm` line 479, already a settled note; 15:8's *L. G. (>* is OCR noise: reader 11
  read the page, `../1kgs1-22-transcription-readers.md`, and found marks only at 15:6, and 1554 has none there, canvas 198,
  column 371); BSB *against MT* 13:11, 13:12, 14:31, 15:1, 21:21; *with MT* 12:18, 12:30, 15:6, 21:23; numbers 12:32,
  12:33, 15:1, 15:33, 16:21, 16:24, 16:29, 18:32, 18:33, 19:7, 22:48, 22:51. Also 15:6's *L. … H.*, which the tool files
  under the BSB, and the BSB's own notes for 12–22 read in `sources/parallel/bsb/files/12-1KIengbsb.usfm`.
- The NRSVue (Bible Gateway, read 2026-11-22) for chapters 12–22 with its footnotes (not stored; three fetches, 12–14,
  15–17, 18–19 and 20–22). The NET was not read.
- The verses below in the preview (`text/draft/1KI.preview.usfm`) and the printed text (`text/orig/1KI.usfm`) against
  the BSB, the WLC, the Clementine Vulgate, Brenton's LXX and the KJV (`sources/parallel/`); the verse readers' reports
  `r5.md` (ch. 12), `r6.md`–`r9.md` (r6 left 15:6 for the notes; none flagged anything else for them).
- 1738's 11 footnotes and 4 asterisks in these chapters, from phase 1 (`data/witnesses/read-1738/1Kgs1-22.tsv`,
  `../1kgs1-22-transcription-readers.md`, readers 08, 11–15).
- The printings: 1738 as printed (`text/orig/1KI.usfm`), the 1750 raw OCR (`sources/archive/1750/text.txt`), **1554**
  (canvases 195–204, 833) on page images read here (`notes-1554-b.md`), **1573** through the MDZ search API only.

The yield is **1 note proposed in 11 chapters** (0.09 a chapter): 22:30, where Castellio follows the Greek and has
Jehoshaphat put on Ahab's clothes, which changes the ruse of the battle; he says so in his 1554 annotation, which the
edition does not print (1738 marks its place with an asterisk). No kind A passes. Three more are near the bar and
recommended left out (15:6, 18:22, 15:13). **15:6 also raises a question of text** for the edition summary: 1554 reads
*Roboamum*, as the Hebrew; *L. Abiamum H.* is in 1573 and 1738 (§C item 2).

## A. Modern Bibles follow the versions (kind A)

None proposed. The places where both the NRSVue and the BSB leave the Hebrew are 12:28 ("to the people", the Hebrew
"to them": Castellio *hominēsque monuit*, with them), 13:12 ("showed", the Hebrew "had seen": Castellio *Cumque illī
viam ostendissent*, with them), 19:3 ("he was afraid", the Hebrew "he saw": Castellio *Quibus ille minīs territus*, with
them, by his own annotation, `notes-1554-b.md` §1) and 12:30 (Bethel and Dan: the NRSVue with the Greek, the BSB a
"likely reading"; Castellio *alterīus vīsendī grātiā Danem usque*, "to see the other as far as Dan", which implies the
first at Bethel, 12:29). Castellio already reads with them at each. Everywhere else one of the two keeps the Hebrew (§F).

## B. Castellio's text departs from the Hebrew (kind C)

**Decision:** accept (Nathan, 2026-11-22: "Approve all as recommended")

1. **22:30** *monuit Isrāēlītārum rēx Jōsāphātum, ut prœlium commissūrus, habitum mūtāret, ipsīusque Achābī vestītum
   indueret. Ipse vicissim rēx Isrāēlītārum mūtātō habitū prœlium iniit*: Ahab tells Jehoshaphat to change his dress
   and put on **Ahab's own** clothes. The Hebrew: הִתְחַפֵּשׂ וָבֹא בַמִּלְחָמָה וְאַתָּה לְבַשׁ בְּגָדֶיךָ, "I will disguise myself and
   go into battle, but you put on your robes"; the NRSVue ("but you wear your robes", no footnote), the BSB ("but you
   wear your royal robes", no note), the KJV and the Clementine Vulgate (*et induere vestibus tuis*) the same. Brenton's
   LXX: *καὶ σὺ ἔνδυσαι τὸν ἱματισμόν μου*, "and you put on my clothing". Castellio's 1554 annotation (canvas 833,
   column 361, zoom `z833-1k21-22.jpg`) says it is deliberate: the Hebrew, as he reads it, tells Jehoshaphat both to
   change his dress and to wear his own, *Sed hæc pugnātia sunt*; he would need no telling to wear what he was not going
   to change; and the charioteers, who sought Ahab, would never have gone for Jehoshaphat *nisi ueste decepti*: *Has ob
   causas hoc in loco secutus sum Græcũ exemplar, ubi ita legitur: καὶ σὺ ἔνδυσαι τὸν ἱματισμόν μου*.
   **Why it passes the bar**: it changes what Ahab does in the story: in Castellio he dresses his ally as himself, a
   decoy, so that the Syrian charioteers (22:31–32) take Jehoshaphat for the king of Israel because of Ahab's clothes; in
   the Hebrew and the modern Bibles Jehoshaphat goes in his own royal robes while Ahab alone is disguised. A reader
   comparing a modern Bible meets "your robes" and nothing to say why the Latin differs. Castellio flagged it only in his
   annotation (no *G.* mark in the text: 1554 canvas 203, column 382, *monuit Iſraelitarũ rex Ioſaphatũ, ut prœliũ cõ-|
   miſſurus, habitũ mutaret, ipſiusq; Achabi ue-|ſtitũ indueret*), and the edition prints no annotations; 1738 marks
   the place with an asterisk (`notes-1554-b.md` §2). 1573 (canvas 247, search API, the text; canvas 248, the annotation
   printed in the book), 1738 and 1750 (OCR lines 50812–50813, *ipfiusque Achabi veftitum in-|duceret*) the same; his
   own 2 Chronicles 18:29 reads the same way (1750 OCR lines 62127–62128, *et ipfius regis Achabi vefti-|tum
   induerét*). The case of 2 Sam 14:30 (accepted: a Greek reading that changes what happens), and of reader A's 2:28.
   The note's form is A's 2:28 and the settled Deut 31:23 (*Hebraicē … ‘…’; Castelliō Septuāgintā sequitur*), without
   *ut Vulgāta* (the Vulgate keeps the Hebrew). Words checked with `pipeline latin macron-check` (*tū vērō indue vestēs
   tuās*; *Hebraicē* as the settled notes have it).
   **Recommendation (Claude): accept.**
   **Apply:** `1Kgs.22.30` la: `ipsīusque Achābī vestītum indueret.` → `ipsīusque Achābī vestītum indueret\f + \fr 22:30 \ft Hebraicē וְאַתָּה לְבַשׁ בְּגָדֶיךָ, ‘tū vērō indue vestēs tuās’; Castelliō Septuāgintā sequitur.\f*.`

## C. Places near the bar (recommended left out)

**Decision:** reject 2, 3, 4 (as recommended, under Nathan, 2026-11-22: "Approve all as recommended"); 15:6 keeps 1738's *Ābīamum*

2. **15:6** *Intercessit autem bellum inter Ābīamum et Jeroboāmum per omnem ejus vītam*: 1738's **L. … H.** word
   *Abiamum* (taken out of the text by `../1kgs1-22-draft-fixes.md` §2 item 5), with 1738's own footnote *f) H.
   Roboamum.* The Hebrew בֵין־רְחַבְעָם וּבֵין יָרָבְעָם, "between Rehoboam and Jeroboam"; the NRSVue ("The war begun between
   Rehoboam and Jeroboam continued all the days of his life", no note), the BSB ("between the houses of Rehoboam and
   Jeroboam all the days of Abijam's life", note "Literally war between Rehoboam (most Hebrew manuscripts); some Hebrew
   manuscripts and Syriac war between Abijam"), the KJV and the Clementine Vulgate (*inter Roboam et Jeroboam*) the same;
   Brenton's LXX has no 15:6. So the *L.* source was not found (the Vulgate seen here has Rehoboam).
   **Not Castellio's 1554 text**: 1554 prints *Intercesſit autem bellũ inter Ro-|boamum & Ieroboamũ per omnem eius uitã*,
   with no marks and no margin (canvas 198, column 371, zoom `z198-15_4-6.jpg`). **1573** prints *6 InterceÅ¿sit autem
   bellum inter L. 6 [Abiamum] H.* (canvas 241, search API); 1738 and 1750 (OCR line 49417, *inter L, Abiamum H.*) the
   same. So the reading came in between 1554 and 1573 (*ex postrema recognitione*: perhaps Castellio's own last
   revision, perhaps its editor's; not settled here), and 1738 added the footnote giving the Hebrew.
   Against a note: the war of Abijam and Jeroboam is the Hebrew's own at 15:7 (*Hic Ābīamus bellum gessit cum
   Jeroboāmō*), and that of Rehoboam and Jeroboam at 14:30 (*Fuit autem inter Roboāmum et Jeroboāmum perpetuum
   bellum*), so nothing happens in Castellio that does not happen in the Hebrew; the reading only makes 15:6 say what
   15:7 says. A name, as A's 11:5 (the chapter says it anyway), not as A's 2:28 (which changes what is said of Joab).
   For it: 1738 itself printed the Hebrew's name here, and the BSB names the variant.
   **Recommendation (Claude): leave out.** But see **For the edition summary** below: the edited text could take
   1554's *Roboāmum* instead, which needs no note.
   **Apply (only if accepted against the recommendation):** `1Kgs.15.6` la: `inter Ābīamum et` → `inter Ābīamum\f + \fr 15:6 \ft Hebraicē רְחַבְעָם, ‘Roboāmum’.\f* et`

3. **18:22** *cum Baalēnsēs vātēs sint quadringentī quīnquāgintā, lūcānīque vātēs quadringentī*: Castellio's **G. L. …
   H.** words *lucanique vates quadringenti* (taken out of the text by the draft fixes), "and the prophets of the groves,
   four hundred". The Hebrew ends with Baal's 450 (וּנְבִיאֵי הַבַּעַל אַרְבַּע־מֵאוֹת וַחֲמִשִּׁים אִישׁ); the NRSVue (no note), the BSB (no
   note), the KJV and the Clementine Vulgate (*prophetæ autem Baal quadringenti et quinquaginta viri sunt*) the same.
   Brenton's LXX has them (*καὶ οἱ προφῆται τοῦ ἄλσους τετρακόσιοι*): so the Greek's; the Vulgate seen here lacks them.
   1554 (canvas 200, column 375, zoom `z200-18_22.jpg`: *cum Baalenſes uates ſint quadringen-|ti quinquaginta, G. L.
   lucaniq; uates quadrin-|genti. H.*), 1573 (canvas 244, search API: *G. L. lucaniq; vates quadringenti.H.*), 1738 and
   1750 (OCR line 49974) the same: Castellio's own. **Near the bar**, left out: the four hundred prophets of Asherah are
   the Hebrew's own at 18:19 (*et lūcānōs vātēs quadringentōs, Jezabēlis convīctōrēs*), so Elijah's count adds nothing
   the reader has not been told three verses before, and nothing in the contest turns on it (only Baal's prophets are
   named after this). As A's 11:5 (the chapter says it anyway), not as 2 Sam 14:30 (an event the Hebrew does not
   narrate). **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `1Kgs.18.22` la: `lūcānīque vātēs quadringentī.` → `lūcānīque vātēs quadringentī\f + \fr 18:22 \ft ‘lūcānīque vātēs quadringentī’ Castelliō ex Græcō addit; Hebraicē nōn est.\f*.`

4. **15:13** *quod ea Pāna fēcerat in lūcō: eumque Pāna exscidit*: the Hebrew מִפְלֶצֶת לָאֲשֵׁרָה, "an abominable image for
   Asherah" (the NRSVue the same, its note only "Or *Asherahs*" at 14:15 and 14:23; the BSB "a detestable Asherah
   pole"); the Clementine Vulgate *princeps in sacris Priapi … simulacrum turpissimum*. Castellio's *Pān* is deliberate:
   his 1554 annotation (canvas 833, column 361, zoom `z833-1k15.jpg`, margin *Pan.*) gives three reasons for Pan rather
   than Priapus (a woman would hardly make a Priapus; it stood in a grove, which suits Pan, Priapus being set in
   gardens; מפלצת is named from striking terror, *unde Panicus timor dicitur*). His word for an obscure Hebrew noun, and
   his *lūcus* for the asherah throughout: the same matter (Maacah's idol, cut down and burnt) in all of them. A
   construal of an uncertain word, his vocabulary; no plot or doctrine turns on which god the image is called.
   **Recommendation (Claude): leave out.**

## D. 1738's footnotes (recommended: none printed)

**Decision:** none printed (Nathan, 2026-11-22: "Approve all as recommended")

1738 prints 11 lettered footnotes in chapters 12–22 (`%` rows of `data/witnesses/read-1738/1Kgs1-22.tsv`; readers 08,
11, 12, 13, 14, 15). **Eight are Castellio's 1554 margins** (12:16, 12:18, 18:10, 18:19, 18:21, 20:34, 21:7, 22:34),
changed only in spelling and letter; **three are not in 1554** (15:4, 15:6, 15:10; `notes-1554-b.md` §3). As in Joshua,
Judges, Ruth, 1–2 Samuel and reader A's chapters, the edition prints no glosses (brief.md: "No marginal notes or
commentary"). Each, with what it glosses:

- **12:16** *c) in rege, sicut Cæsares a primo nomen habent.* (on *in Dāvīde*: David's name for the king of his line).
- **12:18** *d) scilicet ante Israelitarum discessum.* (on *Cumque mīsisset*: the timing).
- **15:4** *e) posteritatem.* (on *lucernam*, David's lamp; 1554's text reads *posteritatẽ* itself: a later revision of
  the text, the old word kept as a gloss, as A's 11:36).
- **15:6** *f) H. Roboamum.* (on *Abiamum*): the one textual footnote; §C item 2.
- **15:10** *g) auia.* (on *māter*: Maacah, Asa's grandmother, as 15:2 makes her Abijam's mother; the BSB "his
  grandmother" at 15:13, the NRSVue "his mother"). A gloss reconciling two verses; not in 1554, in 1573.
- **18:10** *h) scilicet per Deum, vt dicerent, an tu illic esses,* (on *obtestābātur*: he made them swear).
- **18:19** *i) lucorum.* (on *lūcānōs*).
- **18:21** *k) ambigua sententia nutatis?* (on *Quousque in utrumque crūs claudicātis*: the image explained).
- **20:34** *a) vbi publicanos colloces et vectigalia exigas,* (on *fora*: the bazaars).
- **21:7** *b) qui vnius vineæ comparandæ rationem non inuenias, quo pacto regnum, si esset opus, tibi parares?* (on *Ō
  tē hominem idōneum*: the irony explained).
- **22:34** *c) in incertum.* (on *simpliciter*: "at random").

None marks a departure from the Hebrew but 15:6's. **Recommendation (Claude):** print none.

## E. 1738's asterisks

1738's four asterisks in these chapters (15:13, 19:3, 21:24, 22:30, by the KJV's numbering; readers 11, 13, 14, 15)
**each stand at the place of one of Castellio's four 1554 annotations on chapters 12–22** (*EX CAP. XV.*, *XIX.*,
*XXI.*, *XXII.*, canvas 833, column 361; `notes-1554-b.md` §2): with A's fifteen, nineteen of nineteen in the book.
The edition prints no asterisks. What each annotation does:

- **15:13** defends *Pāna* against the Vulgate's Priapus: vocabulary (§C item 4).
- **19:3** reads *territus* with the Greek, the Latin and Josephus for the Hebrew's "he saw", by changing the points:
  **with the NRSVue and the BSB** ("he was afraid"). No note.
- **21:23** (the asterisk after *comēsum īrī*, at 21:24's start) reads חֵלֶק, "field", for חֵל, with the old Latin and
  2 Kgs 9 (*in agrō Jezrælēnsī*): **with the NRSVue** ("within the bounds of Jezreel"), against the BSB ("by the wall",
  its note naming the Vulgate and 2 Kgs 9:36) and the Hebrew. Not the consensus for a note (`ot-notes-process.md` §3):
  a place's description, and one modern Bible reads as he does (as 2 Sam 21:6).
- **22:30** follows the Greek for Jehoshaphat's clothes: §B item 1.

## F. Considered and left out

- **The tool's candidates**, besides the items above: **13:11** *Ad hunc veniunt ipsīus fīliī* (the BSB's plural, with
  the versions; the NRSVue "One of his sons", the Hebrew's singular, no note: and the Hebrew itself goes on in the
  plural, "they told"); **13:12** (§A); **14:31, 15:1** *Ābīamus* (Abijam/Abijah, the BSB's note on the name's form);
  **21:21** (the BSB's "This is what the LORD says", for the Hebrew's "Behold": Castellio's indirect *scītō, fore, ut
  Jōva … importet* gives the speaker); **12:18** *Adōrāmum* (the Hebrew, the BSB the same); **12:30** (§A); **21:23**
  (§E). **14:25** and **15:8** are not marks of 1 Kings (above).
- **The numbers**: 12:32, 12:33 *octāvō mēnse, diē … decimōquīntō* (the Hebrew's); 15:1 *duodēvīcēsimō* (18), 15:33
  *vīgintī quattuor*, 16:29 *duodēquadrāgēsimō … duōs et vīgintī*, 22:51 *decimō septimō … duōs*: each the Hebrew's,
  in words the tool does not count; 16:21 *in partēs duās*, 16:24 *duōbus argentī talentīs*, 18:32 *duo sata* (the
  Hebrew's two, or its dual); 18:33 *quattuor amphorās* (the Hebrew's 18:34 four jars, the versification); 19:7
  *Iterumque* ("a second time"); 22:48 (the Ketiv עשר, "made", not "ten": Castellio *Fēcit*, as the BSB). Every numeral in
  12–22 matches the Hebrew.
- **The NRSVue alone leaves the Hebrew** (Castellio with the Hebrew and the BSB): 12:31 "houses" (Castellio *ædem*, the
  Hebrew's singular), 13:29 (Gk), 17:1 "of Tishbe in Gilead" (Gk; Castellio *ex incolīs Galaadītidis*, the Hebrew's
  "of the settlers", as the BSB), 20:6 "whatever pleases them" (Castellio *tuōrum ēlegantissima quæque*, the Hebrew's
  "you"), 20:11 "Enough!" (Gk), 21:23 (§E, Castellio with it). None with the BSB's agreement.
- **The Hebrew uncertain** (the NRSVue's notes): 14:14 (Castellio *quī Jeroboāmī stirpem aliquandō ēruat*, the sense).
- **Castellio's other marks**: none; with items 2 and 3, every mark in 12–22 is accounted for (15:6's not in 1554).
- **His vocabulary, or a construal the context sets right**: 15:13 *Pāna* (§C item 4); 22:48 *nāvēs Cilicas* (his
  Cilicia for Tarshish); 14:10 and 21:21 *comminctōrem parietis* (the Hebrew's idiom kept); 12:16 *in Īsæidā*.

**For the edition summary (not a note):**
- **15:6 *Ābīamum* or *Roboāmum*.** The edited text follows 1738 (*L. Abiamum H.*, marks taken out), which agrees with
  1573; **1554 prints *Roboamum*** (canvas 198, column 371), as the Hebrew, the Vulgate, the NRSVue and the KJV. If
  Nathan takes 1554's reading (Castellio's last lifetime edition; whether 1573's change is his is not known), item 2
  falls away; **Apply (text, only if Nathan chooses 1554):** `1Kgs.15.6` la: `inter Ābīamum et` → `inter Roboāmum et`
  (the printed text, `text/orig/`, keeps 1738 either way).
- 15:4 *lucernam* (1738) where **1554 prints *posteritatem*** in the text (canvas 198, column 371), the gloss of 1738's
  footnote *e)*: the same change as A's 11:36 (*lumen* → *lucernam*), a revision after 1554; no choice proposed (the
  Hebrew נִיר, "lamp", is 1738's).
