# 1 Kings 1–22, phase 2: the edition and its notes

*2026-11-22. Decision 85's phase 2 (PLAN.md §4), on Nathan's "Start Phase 2", after the printed text was approved for
now (`1kgs1-22-transcription.md`). Gate 2: the book settled with its notes → `text/1KI.usfm`.*

**Decision:** approve all as recommended (Nathan, 2026-11-22: "Approve all as recommended"). Settled for now with the
three notes of point 2; 3:7 *necdum* restored (draft fixes §6), 15:6 *Ābīamum* kept; the title of point 5; points 3, 6,
7 and 9 as proposed. Point 8's questions carry no recommendation and stay open (`HUMAN.md`), the text left as the
preview has it. Done 2026-11-22: `text/1KI.usfm` from the 816 items (all `ok`), the notes applied, gold rebuilt, the
ledger settled, the draft and preview removed; the printed text titled and rebuilt from the read lines (matching word
for word), its draft removed.

## For you (9 points)

1. **Approve 1 Kings for now and settle it, with its notes?** The preview is `text/draft/1KI.preview.usfm`; the 816
   items in `1kgs1-22-ch01.md` … `-ch22.md` all check `ok`, and the notes' three Apply lines check `ok` against the
   preview.
2. **Three notes recommended** (`1kgs1-22-phase2/notes-a.md` items 1–2, `notes-b.md` item 1; Apply lines ready), all
   Castellio's own readings from the Greek, in 1554's text:
   - **2:12** *nātus annōs duodecim* (his *G. … H.*): Solomon's age at his accession, which the Hebrew never gives. With
     11:42 (forty years' reign) and 14:21 (Rehoboam forty-one at his accession) it makes Solomon a father at about
     eleven: the book contradicts itself where the Hebrew does not (your rule of 2026-11-21). Note: *‘nātus annōs
     duodecim’ Castelliō ex Græcō addit; Hebraicē nōn est.* Brenton's LXX lacks the words; reader A did not find his
     Greek source.
   - **2:28** *nōn ad Solomōnem* (his *G. L. … H.*), where the Hebrew, the NRSVue and the BSB have Absalom: it changes
     what is said of Joab. Note: *Hebraicē … ‘ad Absālōmum’; Castelliō Septuāgintā sequitur, ut Vulgāta.*
   - **22:30** *ipsīusque Achābī vestītum indueret*: Jehoshaphat told to wear Ahab's clothes, from the Greek, where the
     Hebrew has "your robes"; it changes the ruse of the battle. His 1554 annotation defends it (canvas 833: the Hebrew's
     order is pointless, and the charioteers took Jehoshaphat for Ahab); 1738 marks the place with an asterisk.

   **Left out** (each reasoned there, Apply lines ready if you want them): **10:27** *aurī* for the Hebrew's silver, the
   closest: Castellio's own (1554, 1573, 1738), a material, not a person, though his 2 Chr 9:27 has *argentī*, so his
   Bible disagrees with itself across books; **11:5** Chemosh added to Solomon's gods (11:7 names him in the Hebrew
   anyway); **1:8** the Cherethites and Pelethites added to a list; **15:6** (point 4); **18:22** *lūcānīque vātēs
   quadringentī* (the Hebrew has the 400 at 18:19); **15:13** *Pāna* (his word for an obscure noun, defended in his
   annotation); 9:8 and 6:8 (kind A by the letter, a construal and a building detail).
3. **1738's 15 footnotes not printed**, as in the books before. Most are Castellio's 1554 margins; 15:4 *posteritatem*
   keeps 1554's text word where 1738's text has *lucernam*; 15:10 *auia* is 1573's, not 1554's. **The nineteen asterisks
   with no footnote each mark one of Castellio's 1554 annotations on 1 Kings** (fifteen in 1–11, four in 12–22). Facts in
   `docs/editions.md`, "1 Kings in 1554 and 1573".
4. **Two readings that differ from Castellio's lifetime edition**, both seen by Claude on 1554's page (crops
   `sources/mdz-1554/z188-3_7.jpg`, `z198-15_4-6.jpg`). As 1 Sam 20:30's *improbæ* (`1sam1-31-draft-fixes.md` §3), the
   printed text keeps 1738 either way:
   - **3:7** 1554 *qui necdum per ætatem res administrare scio*; 1738 and 1750 *nec tum*, which reads awkwardly ("nor
     then") where the Hebrew is "I do not know". Perhaps a later printer's slip (1573 not found by the search).
     **Recommended: restore *necdum*** as a draft fix. **Accept?**
   - **15:6** 1554 *inter Roboamum & Ieroboamum*, unmarked (the Hebrew's Rehoboam); 1573 (search) and 1738 *inter L.
     Abiamum H.*, 1738 with the footnote *H. Roboamum*. The marks are Castellio's own way of flagging a reading from the
     Latin, and 1573 is *ex postrema recognitione*, so **recommended: keep 1738's *Ābīamum*** (no note: 15:7 tells the
     same war). Reader B has an Apply line ready for *Roboāmum* if you want 1554's.
5. **The title** (`text/draft/1KI.usfm` and `text/orig/1KI.usfm` still have 1738's *Regum liber 3*): by hand, as
   1–2 Samuel's (`1sam-title-2026-11-21.md`) and the Nova Vulgata's *Regum I* (`pipeline/books.py`): `\h Rēgum I`,
   `\toc1 Rēgum Liber Prior`, `\toc2 Rēgum I`, `\mt1 Rēgum`, `\mt2 Liber Prior`; the printed text the same unmarked.
   **Accept?**
6. **Names** (`1kgs1-22-phase2/names.md`; the printed text keeps 1738's forms). Hard calls:
   - **The nominative in *-as***: the settled *Adōnias* and *Banajas* (2 Samuel) keep their short *-as*, one form per
     person; the unsettled *Abdiās, Ahiās, Ochoziās* take the majority's *-ās* (*Ūrīās, Ēlīās, Achiās* …). Say if you
     want *-ās* throughout (2 Samuel's would then need your hand edit).
   - **Marks on the Hebrew alone** (*Nābōth-*, 18 rows, and about thirty more: `names.md` call 4), as 2 Samuel's call;
     drop those rows if Hebrew-only marks are not wanted.
   - ***Jezabēl-*** from the settled Rev 2:20 *Jezabēlem*, though the Hebrew and Greek have a short vowel; ***Āzariās***
     (4:2, 4:5) as Gaffiot; 19:16 ***Nansis*** (Nimshi) kept as printed, perhaps 1738's slip for *Namsis*; 22:42
     ***Salis*** a name (Shilhi), not *salis*.
   - **To one form** (draft fixes §4): *Nabatī* (1738 twice *Nabathi*), *Ahiæ* 21:22, *Hanānis* 16:1 (1738 *Ananis*;
     16:7 *Hananis*), *Sarephtham*, *Asiōngābre* (Deut 2:8), *Anāthōtha* 2:26 (Josh 21:18; the accusative of goal, so
     the names reader's call 1 no longer arises), *Bēthsemem* (1 Sam 6:9), *Chamōss-* (Num 21:29, Judg 11:24).
7. **Layout calls**:
   - **Verse**: only Solomon's saying at the dedication, 8:12–13, on the BSB's lines (as 2 Sam 3:33–34's dirge). Say if
     two verses are too short for verse.
   - Quoted speech: 166 “ and 15 ‘, balanced. `propose`'s 13 flags were each checked: 8:15 and 8:21 are a paragraph
     inside Solomon's speech (a false alarm); the ‘…’ at 20:3, 20:13, 22:11, 22:17 and the rest are inner quotations.
     Reported speech unmarked although the BSB quotes it; *X: words, inquit* with the colon made a comma.
   - **Question marks for 1738's full stops** at 22:18 and 22:20 (questions by their first word, and in the BSB; reader
     r9). 22:16 keeps its stop. 12:6 *respondendum?* and 12:9 *aliquid?* keep 1738's question marks on indirect
     questions. Say if you prefer Castellio's stops throughout.
   - **Paragraphs** at Castellio's sentence starts: 1738's indents, the BSB's breaks, splits near 250 words (22:19 added
     by proofreader p4, 22:13–28 having run to 289 words). The moved chapter breaks (3:1, 13:1, 15:1) open with `\p` at
     the KJV's chapter start.
   - **Capitals**: *Isrāēlītic-*, *Solomōniān-* (draft fixes §5), *Dāvīdic-*, *Mōsaic-*, *Jūdaic-*, as the settled text.
8. **Spelling**: 32 rows added to the approved rules under the standing rule, all in families already approved
   (decision 37's *ad-*, 24 words: *affēcerat, affīnitātem, aggrediātur, allātōque, alliciat, annuerit, appāreō,
   appellāte, apportābat, apposititiī, arripientēs, ascendisset, ascītīsque, assectātōrēs, aspexisset* …; *-mps-/-mpt-*
   *īnsūmptīs, sūmpsistī*; *umerī*; *decimō quīntō*, *decimā quīntā* apart; *sē ipsōs*; *male dīxisse*; and the phrase
   *ab īmō*, kept from *imo → immo* as the approved *in īmō*). Your *adsto*, *adsurgo*, *adsequor* and the compounds of
   *sum* left as printed. **Questions, none applied**:
   - ***adsistat*** (19:11): the approved *adsistentes → assistentes* (Exodus, Acts *assistit*, *assistentēs*), but the
     settled Numbers prints *adsistant* (1:4) and *adsistat* (23:3). Assimilate here and in Numbers, or keep *ad-*?
   - ***assectātōrēs*** 1:2 (applied, as the settled *assectārī*): proofreader p1 asks whether *adsector* should stay
     *ad-* like your *adsequor*.
   - ***adstruēbat*** (*astruō*, not *adstō*): assimilate?
   - ***comminctōrem*** or *commīnctōrem* (14:10, 21:21; proofreader p4's question), left as the preview has it.
   - ***Adarezerō***, ***cæcūtientis***: proofreader p3's marks, against the settled 2 Sam *Adarezero* (4×, unmarked) and
     2 Pet 1:9 *cæcutiēns*. Say if the settled books should follow.
9. **1738's slips corrected in the draft** (`1kgs1-22-draft-fixes.md` §1, each seen on the page in phase 1): 3:1
   *intera*, 6:8 *lanuas*, 6:27 *in templa*, 11:33 *Mclcomum*, 11:38 *tib*, 17:1 *adparco*, 20:14 *promitit*, 22:52
   *Iou mque*; and two the verse readers found: 3:2 *Qui bus*, 6:38 *at que* (lines divided without a hyphen), 14:10
   *ſimus* (*fimus*, dung). **Left as 1738 prints them**: 18:17 *est tune* (no stop), 19:16 *Nansis*, 10:27 *aurī*. Two
   phase-1 misreadings (7:51, 22:34) were corrected in the printed text on your "Accept both"
   (`1kgs-orig-consecratum.md`).

## Where it stands

- **The draft** (`text/draft/1KI.usfm`): built in phase 1 from the read lines; `1kgs1-22-draft-fixes.md` §1 eight
  slips, §2 Castellio's marks dropped in six verses with their words kept, §3 nine found by the verse readers (among
  them u/v and i/j the draft's step left, and the two misreadings), §4 eleven names, §5 six capitals, each with
  its Apply line (46, all applied).
- **Stages 3–5** (`python -m pipeline propose 1Kgs 1-22`): 816 items. Calls in `data/decisions/1Kgs.layout.tsv` (312
  rows) and `1Kgs.forms.tsv` (628 rows), each with its reason, merged by `1kgs1-22-phase2/merge.py` (verse readers, the
  names reader over them, the proofreaders over all).
- **Tests** pass (218).

## How it was made

Nine verse readers (1–2, 3–5, 6–7, 8–9, 10–12, 13–15, 16–18, 19–21, 22) under one brief (`1kgs1-22-phase2/BRIEF.md`),
each verse beside the KJV, the BSB (with its layout), the Hebrew and the printed text; a names reader across the book,
making the readers' names agree; two notes readers (1–11, 12–22; `NOTES.md`: the candidates of `pipeline notes 1Kgs`,
the NRSVue, the LXX, the Vulgate, 1738's footnotes and asterisks, and Castellio's 1554 text and annotations read on the
page: `notes-1554-a.md`, `-b.md`); then four proofreaders (1–5, 6–9, 10–15, 16–22; `PROOF.md`) who compared the preview
with 1738 word by word and read every verse again: 47 forms rows, four layout rows, and the spelling gaps of point 8.
All one at a time, with the quota checked before each. Their files: `1kgs1-22-phase2/`.

## On approval

`python -m pipeline review apply data/review/1kgs1-22-ch*.md --write` into a new `text/1KI.usfm` (the preview's header
and verses), the title by hand (point 5), then the notes accepted (`1kgs1-22-phase2/notes-a.md`, `notes-b.md`);
`python -m pipeline gold 1Kgs`; the ledger to `settled`; `text/draft/1KI.usfm` and its preview removed. Then the
printed text's title by hand, and the printed text rebuilt from the read lines to check its words, as 2 Samuel's was.
