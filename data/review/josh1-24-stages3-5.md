# Joshua 1–24: stages 3–5, one proposal per verse

Proposed 2026-11-19 (decision 30's standing rule), as Deuteronomy (`data/review/deut1-34-stages3-5.md`). Nathan:
"Pull, then start work on Joshua", "Go all the way through stage 5 before stopping to ask for my input".
**Decision:** accept, and Joshua 1–24 settled for now (Nathan, 2026-11-19: "Approve and settle Joshua"; decision 84):
`text/JOS.usfm`, the 656 items applied as accepted (identical to the preview), `data/gold/Josh.tsv` built, the ledger
`settled`, the draft and preview removed. The calls below stand as made, with his answers to "For you"; his in-depth
review comes later (decision 30).

## Where it stands

- **Stages 1–2**: 1738 read on the page line by line (Wikisource's Joshua, not a faithful copy of 1738, served as a
  witness): `data/review/josh1-24-stage2.md`, the readers' notes beside it. Versified to the KJV's 658 verses (43
  edits, `data/versification/Josh1-24.draft.edits.tsv`; 4:15–17 one verse). The draft `text/draft/JOS.usfm`, the
  printed text `text/orig/draft/JOS.usfm`, the same 656 verse rows.
- **Corrections to the draft** (Apply lines in the stage-2 record, all applied): 1738's misprints (7:21, 8:10, 13:25,
  15:31, 18:1, 18:20, 22:3, 22:5), words run together (1:15, 21:2), 16:10's *G. … H.* marks dropped, 22:11
  *exadversum* (the draft's u/v step), 22:16–17 *res publica*, 7:12–13 *sacrilegum* from 1573 (below), and **46 name
  spellings** (one form per person and place, `josh1-24-names.md`).
- **Stages 3–5**: `data/review/josh1-24-ch01.md` … `-ch24.md`, 656 items (one per verse; 4:15–17 one item), all
  checking `ok` (15:34's one `already`). Preview: **`text/draft/JOS.preview.usfm`**. Calls in
  `data/decisions/Josh.layout.tsv` (206 rows) and `Josh.forms.tsv` (948 rows), each with its reason.
- **Stage 2b** (the printed text): every word from the lines read on the page; paragraphs from 1738's indents, not yet
  checked on the page (as Numbers' and Deuteronomy's), the one false break (18:1, inside *Israeli-|tarum*) taken out by
  a fix in `orig.paragraph_starts`.
- **Not done**: the notes pass (16:10, 1738's two footnotes; decision 56); 1554's
  annotations.

## How the verses were made

Eight readers (1–3, 4–6, 7–8, 9–10, 11–14, 15–17, 18–21, 22–24) under one brief (Deuteronomy's rules, each verse
beside the KJV, the BSB and the Hebrew where needed), two names readers (1–14, 15–24, matched by Claude), then four
proofreaders (1–6, 7–11, 12–17, 18–24) read every verse of the preview again (5 layout and 8 forms rows changed, each
noted "proofread:"). Their notes: `josh1-24-stages3-5-readers.md`; the proofreaders' finds are below. Every flag was
checked in its verse; the `homograph` flags still shown (243) are words the readers and proofreaders confirmed as
proposed.

- **Quotation marks** (1738 prints none): the narrative's direct speeches in “…” (God to Joshua 1:2–9, 3:7–8, 6:2–5,
  7:10–15, 13:1–7, 20:2–6; Joshua's speeches and orders; Rahab 2:9–13; the Gibeonites 9:9–13, 9:24–25; Caleb 14:6–12;
  Achsah 15:19; the eastern tribes and the envoys in 22; Joshua's farewell 23:2–16 and 24:2–15, reopened at each new
  paragraph; the covenant dialogue 24:16–24). Castellio's **reported speech stays unmarked**, whatever the BSB does
  (1:10–11, 1:16–18, 2:24, 4:1–5, 7:2–3, 7:20–21, 8:1–2, 9:6–8, 10:8, 11:6, 18:8, 21:2, 22:7–8 and others). *Inquit*
  set off by commas, Castellio's parentheses round it too (decision 65). A message quoted inside a speech in ‘…’
  (22:16–20, the congregation's; 24:2–13, God's words in Joshua's mouth, reopened “‘ at the 24:8 paragraph). 59
  opening marks, balanced.
- **Poetry**: 10:12b–13a only, Joshua's command to the sun and moon and its answer (two couplets, `q1`/`q2`), then the
  prose resumes (`\m`) at *Atque ita scrīptum exstat*; the Book of the Upright quoted and closed at *diēī,*.
- **Paragraphs**: the BSB's, moved to the sentence start where they fell inside one; added where a new speech, scene or
  narrator begins; paragraphs over about 250 words split where the BSB and WEB break (decision 52): 4:1–18, 6:1–27,
  7:1–15, 8:1–29, 11:1–15, 22:9–29, Joshua's speeches in 23 and 24. The land lists (13, 15–19, 21) a paragraph per
  tribe or region, not a line per town. 130 paragraphs.
- **Capitals** for adjectives of peoples and places, which 1738 often prints lower case (*Isrāēlīticus, Hierichūntius,
  Meromiās, Dōriō, Gessuræōs, Galgalēnsia, Ephrāimīticus, Jūdaicus, Lēvīticus, Trānsjordānīnus* …, about 70 places);
  *Domine* for God (7:7–8), *Dominī* (3:11, 3:13); vocatives set off by commas (10:12 *Sōl, … et lūna, …*).
- **Punctuation**: a colon before a speech where 1738 has a stop; stray stops removed (6:3–4, 8:9 *sēsē. collocant*,
  15:55 *Jōta.* in mid-list, 24:15 *incolitis, Nam*); 13:7 a full stop closing God's words (1738's comma runs them into
  the narrator's 13:8).
- **Forms**: chiefly ablatives the macronizer leaves short (*terrā, eā, suā*, ablative absolutes; **the ablative
  *Jōvā*** after *ā/ab, cōram, cum* and in ablative absolutes, and *Jōsuā*), *tribūs* (genitive and plural), the lot
  formula's nominative *ducta* with *sors/hērēditās* (not *ductā*), *lacūs*, *sōlis* (the sun), perfect subjunctives
  in indirect questions and reported conditions (*tractāverītis, fēcerīs, excitāverītis, adōrāverītis*) against future
  perfects in real conditions (*sustuleritis, cēperitis*), *modo* the adverb, words no source marks (*pēnulīs,
  præmetuentēs, mūtiente, perterrefierī, numerōsiōribus*), each with its reason.
- **Names**: `josh1-24-names.md`, every person, place and people of the book: the settled form first (decision 46), then
  decision 52's order; 677 forms rows; no name left `unknown`.

## Found and fixed on the way

- **Versification**, two whole-verse drifts the count hid, found by the readers and proofreaders and fixed at both
  ends: **10:34–43** (Castellio's 35–37 held the KJV's 36–37, his 38–40 the KJV's 38–39, his 42–43 the KJV's 41–43; 10
  edits) and **11:17–20** (his 17 held the KJV's 17–18; 4 edits). Rows re-keyed to the new numbers.
- **The proofread** (11 problems, all fixed): 2:20 *hōc* (ablative with *sacrāmentō*), 5:5 *modo*, 6:3–4 a stray stop
  in 1738 (*Septem sacerdōtibus … præferentibus.* an ablative absolute with no verb, joined to 6:3), 9:2
  *cōnspīrārunt* (Gaffiot *cōnspīrō*; the proposal had a bad Wiktionary form), 13:26 *Dabīris* (as every *Dabīr-*),
  14:12 *magnaque* (with *oppida*), 15:5 *Orientālis*, 15:55 *Jōta,*, 17:2 *Semīdā* (ablative of origin), 22:21 a
  paragraph (22:9–29 ran 462 words), 23:16 *adōrāverītis* (inside the reported statement of 23:15).
- **Two pipeline fixes, tested**: `verses.keeps_capital`, a decided form written with a capital keeps the capital of a
  verse's first word (towns in a list that look like Latin words, 15:23 *Cedes*, 15:26 *Aman*, 19:30 *Ammam*, 19:36
  *Adama*, 19:37 *Cedes*, 21:35 *Damna*, were lowered by the case rule and could not be set back);
  `structure.quotes`, a quotation within a speech reopened “‘ at a new paragraph (24:8) is not counted twice. And in
  the printed text, `orig.paragraph_starts` (no paragraph begins inside a hyphenated word).
- **15:34 *Taphna***: a names reader read it as a turned u for *Taphua*; withdrawn (below, 4).

## For you

1. ~~**The 14 spelling rows still proposed**~~ **Approved** (Nathan, 2026-11-19: "Yes, add the 14"; in `orthography.tsv`,
   the preview rebuilt: 17 words changed, the 6:8 forms row now *allocūtō*, *sūmpsimus* known; 655 ok, 1 already) (`josh1-24-rules-research.md`, rows in `josh1-24-rules.tsv`): 10 *ad-*
   forms of decision 37 (*aggreditur, aggredī, aggessērunt, alligābis, allocūtō, appellite, appellābuntur, appellāta,
   ascenderent, ascenditur*), three *septemtr- → septentr-*, *sumsimus → sumpsimus*, each looked up in Gaffiot and the
   corpus. **Six rejected** (your "I disagree with adquiro → acquiro …", 2026-11-19, decision 81): *adquīrō, adsequor,
   adsignō, adstō, adsurgō* keep *ad-* throughout the edition (`ad-unassimilated.md`), so Joshua's *adquīsītō,
   adsecūtūrōs, adsignārunt, adsignāta, adsignāvī, adstāns, adstantibus, adsurrēxit* stand. On your yes the 14 go into
   `data/rules/orthography.tsv` as approved and the preview is rebuilt (the 6:8 forms row *adlocūtō* then becomes
   *allocūtō*). *sumsimus* (9:12) is the one word left `unknown` until then.
2. **7:12–13 *sacrilegum*** (applied; **accepted**, Nathan, 2026-11-19: "Accept recommendations for 2 and 5"): 1738 and 1750 print *sacrilegium*, which leaves 7:13's *ante quem* with nothing
   to agree with; **1573** prints *sacrilegum* (the guilty man) in both verses (canvas 160, with the margin note
   *Sacrilegum puniri*), as Wikisource. The alternative: 1738's *sacrilegium* in 7:12, *sacrilegum* only where the
   grammar needs it (7:13), or 1738's in both. **4:14 *timuerant*** kept as 1738 prints it, though 1573, 1750 and
   Wikisource have *fecerant*.
3. **Names, hard calls** (`josh1-24-names.md`; each can be undone in the stage-2 record): the settled spelling for
   the same person or place over 1738's, among them **20:8, 21:36 *Beser*** (1738 *Bosor*; the settled Deut 4:43),
   **15:14 *Sēsæum, Thalmæum*** (1738 *Sesaim, Tholmaim*; Num 13:22), 2:1, 3:1 *Sittīmō* (*Setimo*), 13:20
   *Bēthphegōr* (*Bethphogor*), 17:2 *Asrīēle*, 17:3 *Salphaādus, Melca*, 18:13 *Lūzæ*, 21:39 *Jazēr*, 24:32
   *Jōsēphēīs*; one spelling within Joshua for 18 places (11:1 *Semerōnis*, 12:22 *Cedis*, 13:3 *Accarōnis*, 15:33
   *Saraa*, 15:41 *Maceda*, 24:30 *Thamnathsaræ* …). **Left as Castellio spells them**: Jokneam (12:22 *Jachanānæ*,
   19:11 and 21:34 *Jeconām*) and Taanach (12:21 *Thenacī*, 17:11 *Tanacēnsēs*, 21:25 *Thanach*), since one spelling
   would need forms he never prints.
4. **15:34 *Taphna*** (**corrected to *Taphūa***, Nathan, 2026-11-19: "Yes, Taphūa", after reconsideration: `josh1-24-names.md` §"Evidence re-checked", 4; stage-2 item 36 restored; the printed text keeps *Taphna*): 1738 and 1750 both print it (enlarged on leaf 282: an n); the Hebrew is Tappuah (תַּפּוּחַ, the
   Vulgate *Taphua*), a different town from Ephraim's *Taphua* (16:8). Kept as printed; *Taphua* is the alternative.
   **Evidence for 3 and 4, re-checked** (Nathan asked for it point by point, 2026-11-19): `josh1-24-names.md`
   §"Evidence re-checked". Revised there: 12:22 *Jachananæ* is 1738's misprint (1554, 1573 *Iachanamæ*); *Saraa* and
   *Cedes* unmarked by the Hebrew; *Thamnathser-* in both places; Taanach and Jokneam could take one spelling; outside
   3–4, *Jerimōth-*, *Gaza* (and the settled *Gāzam*), *Cālēbus*. *Taphna* stands in 1554 and 1573 too (but see 4: corrected to *Taphūa*).
   **Applied** (Nathan, 2026-11-19: "Apply all seven"; decision 82), and *Cālēbus* too (decision 83);
   the preview rebuilt (656 items: 655 ok, 1 already).
5. **Smaller calls, made as recommended** (**accepted**, Nathan, 2026-11-19): 4:15–17 a verse range (Castellio condenses three KJV verses into one
   clause); 13:7 a full stop closing God's words; 10:12–13 as verse; inner ‘…’ for the quoted messages (22:16, 24:2);
   1:16–18 the tribes' answer and 2:24 the spies' report left reported (the BSB quotes them); 2:15 *submœnia* kept
   unmarked (no dictionary has it, nor *summœnia*); 3:11, 3:13 *Dominī* with a capital; paragraphs on the BSB alone at
   2:14, 6:2, 6:22, 9:16, 10:41, 15:5, 22:32.

## Found in the settled text (not changed: a review of their own)

- Num 26:40 *ab hoc Naamania*: the ablative *hōc* (proofreader of 1–6).
- Acts 23:12 *cōnspirārunt*: *cōnspīrārunt* (Gaffiot *cōnspīrō*; proofreader of 7–11).
- Gen 13:18 *in Hebrōnē*: the ablative *Hebrōne* (names reader N1).
- Num 32:12 *Cenezeō* against Gen 15:19 *Cenezæōs* (N1 followed Genesis: *Cenezæus*).
- Matt 2:18 *Ramam*: Ramah's settled marks are now *Rāma* (Joshua 18:25; names reader N2).

## Words to look at again (kept as printed)

13:17 *Bethbaal, Meon* (one town in the Hebrew, Beth-baal-meon; 1738 prints the comma, seen), 8:15 *fūsī* (routed; the
Hebrew has them only feign defeat), 24:32 *quessitis* (Wikisource *quaesitis*), 22:31 *in quō … līberāstis*, the
part-verse divisions the proofreaders listed (13:6–7, 13:12–13, 15:2–6, 18:18–19, 22:22–23, 23:8–9, 24:6–8),
Castellio's as in Deuteronomy.
