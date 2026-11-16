# Leviticus 1–27: stages 3–5, one proposal per verse

Proposed 2026-11-15 (decision 30's standing rule), as Exodus 31–40 (`data/review/exod31-40-stages3-5.md`). Nathan:
"Yes, run stages 3–5". **Waiting for your approval**, with the questions below first.

## Where it stands

- **Stages 1–2**: chapters 1–11 from Wikisource, corrected against 1738 (`data/review/lev1-11-stage2.md`); 12–27
  1738's own text, every line read on the page (`data/review/lev12-27-stage2.md`). The draft `text/draft/LEV.usfm`
  has 859 verses, the KJV's count in every chapter: 23 versification edits in 15–26
  (`data/versification/Lev12-27.draft.edits.tsv`) and, found by the readers, 6 in chapter 6
  (`Lev1-11.draft.edits.tsv`).
- **Corrections added to stage 2 from stages 3–5** (each read on 1738's page or traced to the code; under decision 30's
  rule, applied to the draft):
  - Wikisource slips: 6:12 *inexstinctus*, 7:6 *sit* (*fit*), 8:25 *lactes* (*lacies*; 1738's ct ligature), 10:1
    *illius injussu* (Wikisource *illis*), 11:26 *bisulcae* (*visulcae*), 11:29 *mustelam* (*mustolam*; 1738's letter
    damaged).
  - 1738's misprints, corrected for the reading edition where 1750 has the right word: 10:1 *coram Jova* (1738
    *Ioue*), 13:32 *neque* (*neqne*). The printed text keeps 1738's (decision 58).
  - 18:17 Castellio's *L. … H.* marks dropped, the words kept (as Exod 28:34).
  - Five words my modernizing of the read lines had set wrongly, now fixed in `ocrdraft.modern` with tests: 19:20
    *animadvertitor*, 20:12 *coierit*, 25:35 *juvatote*, 26:13 *subjugiis*, 26:15 *parueritis*.
- **Stages 3–5**: `data/review/lev1-27-ch01.md` … `-ch27.md`, 859 items, all checking `ok`. Preview:
  **`text/draft/LEV.preview.usfm`**.
- **Stage 2b** (the printed text, `text/orig/draft/LEV.usfm`): rebuilt on the corrected, renumbered draft; still to
  be read on the page (`data/review/lev1-11-orig.md`: about 500 words the OCR missed in 1–11; three paragraph breaks
  in 12–27 that may be a drop capital's indent).

## How the verses were made

Eight readers (1–5, 6–8, 9–12, 13–14, 15–18, 19–22, 23–25, 26–27) under one brief, as for Exodus. Their calls are in
`data/decisions/Lev.layout.tsv` (142 lines) and `Lev.forms.tsv` (801 rows, each with its reason). I checked every
layout row against the draft's words, joined the readers' speech boundaries, re-keyed chapter 6 to its new numbering,
and read the doubtful words on 1738's pages. Then four more readers proofread all 859 verses; what they found is
fixed (below).

- **Quotation marks** (1738 prints none): Leviticus is God's speech with the narrator's frames (*Item Jova cum Mose
  locutus est in hunc modum:*) outside the marks; one level only, the message for the Israelites unmarked inside
  (as Exod 20:22–26), lower case after its colon. Every *inquit* inside speech with commas, the quotation closed and
  reopened (decision 65); a verse that is only *Tum haec, inquit,* (6:19, 22:17, 22:26, 23:26, 23:33) reopens at its
  end, as Exod 30:17. Speeches left open across a chapter break where no narrator comes between (1→2, 2→3, 4→5,
  6→7, 25→26; decision 31), reopened at the next chapter's paragraph. Speeches quoted in the narrative of 8–10
  (Moses to Aaron and the people, Aaron's answer 10:19) and 24:10–23 (God's ruling). 93 opening marks, balanced.
- **Paragraphs**: the BSB's, moved to the sentence start where they fell inside one (6:7 → 6:8, 6:13 → 6:14);
  added at 6:19, 7:35, 26:27, 27:14, 27:22 (paragraphs of 250–490 words broken where the BSB and WEB break).
- **Punctuation**: a colon for 1738's full stop before a speech (1:1, 17:1, 17:2, 21:1); 25:33 *quique. a Levita*
  and 27:29 *est. ne* (1738's stray points) removed; 20:20's semicolon a comma.

## The proofread (12 problems, all fixed)

- *cōram Jōvā*, not *Jōva*, in 9:4, 10:1, 14:16, 18, 27, 29 (and 4:4–24, 6:14, 8:27 by the readers);
  2:13 *condītō* (*condiō*, to season); 4:3, 4:14 *bovillum* (as 22:19, the settled *bovillī*); 25:13 *Jūbilis*
  (genitive of the neuter *Jūbile*, short -is).
- **A pipeline bug, fixed**: a decided form that writes *oe* apart (a hiatus, 16:2 *introeat*, 18:23 *coeundum*,
  20:19 *coercendum*) was ligatured to *œ* after the decision; `verses.decided_word` now keeps it apart (tested). The
  settled 1 Pet 3:10 *cœrceat* had the same slip, now *coerceat* (`data/review/hiatus-oe.md`, 2026-11-16); Acts 4:26 *cœuntque* is proposed there.
- Layout: 25:55 no longer closes the speech (it runs on into 26); 24:15 and 17:3 *qui*, *haec* lower case after the
  colon; 19:1 a new paragraph (the draft had `\nb`); 21:1 a colon before the speech.

## Calls worth a look

- **Ablatives the proposal had wrong**, fixed by the readers, chiefly *rē dīvīnā*, *aquā lavātor/perluitō* (about
  20 places), *noxā*, *columbā nātōs/nātīs* (ablative of origin, every place alike), *cum eā*, *prō eā*, *ā Jōvā*;
  *vestīmenta sua* (not *suā*); *domūs* genitive in 14:36–55; *macula* nominative 13:19–28; *porrīgō* (scurf).
- **Coinages and rare words, marked by analogy**: *frustulātim* (1:6), *circumsperguntō*, *clībanārium*,
  *patellārium*, *sartāginārium*, *raptītiī*, *ūnīuscujusvīs*, *glabrētō* (13:55; *glabruerit* 13:41 left unmarked),
  *trullissantō*, *septemdiāle*, *permetitō*, *meretrīcātū*, *mentīginōsum*, *stātor* (27:14, 17: from *stō*).
- ***jubile-***: Castellio's neuter noun *Jūbile, Jūbilis* (unmarked e, an i-stem like *mare*) and his adjective
  *jubileus* marked *jūbilēus* (its e for Gaffiot's *æ* in *jūbilæus*). Kept as he spells them.
- **Names**: *Elisāphānem* (10:4), *Solōmītha*, *Dibris* (unmarked: no evidence), *Molochō* (o's unmarked, as Acts
  *Molochī*), *Isrāēlītide*, *Misaēlem*, *Ozīēlis*.
- 21:20 *argemam* (Gaffiot *argema, -atis*, neuter: Castellio's own accusative, kept), 19:36 *pondo justa* (kept),
  11:36 *aquae adfluentiae*, 11:35 *solia*, 11:16 *harpam*, 11:22 *attelabōrum* (L&S *attelabus*; Gaffiot
  *attelebus*): all kept as printed.

## Questions

1. ~~**The spelling rules**~~ **Approved, all 42** (Nathan, 2026-11-16: "Approve all 42"): status `approved` in
   `data/rules/orthography.tsv`, each note saying so.
   - 28 *ad-* forms of decision 37 (*afferet, aspicitō, appārēbit, assignō, alloquere, assurgitō* …);
   - 8 *-mt-* → *-mpt-* (*ēmptor, redēmptus, cōnsūmptī* …);
   - *vōsmet ipsōs*, *quārtō decimō*, *tætrum*, *satyrīs*, *cōnīventēs*, *male dīxit* (20:9).

   The readers' 12 rows on those words re-keyed to the new spellings (19:34's split into *vōsmet* and *ipsōs*). The
   preview regenerated: 52 words changed in 50 verses, every one a rule's word, all 859 items `ok`. The settled Exod
   29:21 *adspergitō*, the one *ad-* form left in the settled text outside the compounds of *sum*, is proposed
   for the same change in `data/review/exod-adspergito.md`.
2. ~~**7:6 *fit* or *sit*?**~~ **Answered by the page (2026-11-16): *sit*.** Enlarged 6×, 1738 leaf 161 (col. 0,
   line 78) prints *ſanctum ſit.*: the bar is only a left nub, where *fiet* on line 75 has it through the stem. 1554
   prints *ſacroſanctum ſit* (canvas 67, read by the side session). A Wikisource slip, now item 6 of
   `lev1-11-stage2.md` §2 and applied to the draft; the preview and `lev1-27-ch07.md` are regenerated (only 7:6
   changed, all items `ok`), and the printed-text draft, rebuilt, has *sit*.
3. ~~**10:1 *Jova*, 8:25 *lactes*: keep?**~~ **Kept** (Nathan, 2026-11-16: "Apply all of your recommendations"). The
   printed text keeps 1738's *Ioue* by a row in `data/decisions/Lev.orig.tsv` (leaf 165, line 5, re-read enlarged).
   **8:25 is not a misprint**: 1738 prints *lactes* with the ct ligature (leaf 163, line 64, enlarged 6×), which
   Wikisource and I had read as *ci*. So *lacies* was a Wikisource slip, and the printed text has *lactes*.
4. ~~**13:24, 17:15, 23:24, 11:29**~~ **Decided by 1554** (MDZ bsb10196330, read by the side session Nathan forked;
   Nathan, 2026-11-16: "Apply all of your recommendations"). Applied, the preview regenerated (only these four
   verses changed, all items `ok`):
   - **13:24 *rubicantem*** kept (Gaffiot *rŭbĭcō*; 1554 *rubican-tem*), and **13:19 *rubricans* → *rubicāns*** (1554
     *rubicãs*; 1738 prints *rubricans*, leaf 168, read enlarged here): `lev12-27-stage2.md` item 4.
   - **17:15** → *impūrusque ad vesperum estō, et ita pūrgātor.* (1554 *& ita pur-gator*; the later printings repeat
     *et aqua lauator*): item 5 there. The printed text keeps 1738's.
   - **23:24 *monētum***: Castellio's coinage from *moneō*, explained in his 1554 annotations (canvas 820). The
     forms row is changed. A footnote on the coinage was added 2026-11-16: *‘Monētum’ Castelliō ā monendō fīnxit, ut Jūnō Monēta.* (`lev23-24-note.md`).
   - **11:29 *mustolam* → *mustēlam*** (1554 *muſtelã*, the 1726 OCR *mustelam*): `lev1-11-stage2.md` §2 item 7. On
     1738's leaf 166 (line 79) the letter after *must-* is damaged, with no closed ring as an o would show. So 1750's
     *mustolam*, which Wikisource follows, is most likely a misreading. The printed text reads *mustelam* by a
     `Lev.orig.tsv` row that says so.
   - *vesperam*/*vespera* elsewhere: not normalized (Nathan, in the side session).
5. ~~**10:4 *Elisaphanem* or the settled *Elsāphān*?**~~ **Decided: *Elsāphānem*** (Nathan, 2026-11-16: "Yes,
   Elsāphānem"; decision 46), the same man as Exod 6:22. Recorded in `lev1-11-stage2.md` §4 and applied to the draft,
   with the forms row changed; the preview regenerated (only 10:4 changed, all items `ok`). 1738 prints *Eliſaphanem*
   (leaf 165, line 16, read enlarged), and the printed text keeps it by a `Lev.orig.tsv` row.

**Decision:** accept 1–5 as decided above, and Leviticus 1–27 settled (Nathan, 2026-11-16: "Approve Leviticus 1–27 and settle it")
