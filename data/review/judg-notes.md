# Judges: light notes (Old Testament search)

Built 2026-11-19 by the process in `ot-notes-process.md` (decisions 1A–4A), as Deuteronomy's (`deut-notes.md`), with
the bar as the Numbers pass left it (`num-notes.md` §F: a construal the context sets right is left out). Nathan: "Start
the notes for Judges, the same way". Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and
Castellio keeps it; kinds B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and
the Hebrew agreeing, and nobody calls the passage uncertain. Castellio's 1554 annotations on Judges, read on the page in
this pass, are in `judg-notes-1554.md`, with one note proposed there (18:2), which the search below found too.

**Sources read:**
- `judg-notes-candidates.md` (`python -m pipeline notes Judg`): 14 BSB version notes, 23 numbers, 3 short verses, and
  three *G.* … *H.* places: 16:13–14 (§C) and one that is not Judges' (9:48, Judith 2:21's *L.* … *G.*, as Deut 3:1).
- The NRSVue (Bible Gateway, read 2026-11-19) for all 21 chapters with its footnotes, one chapter per fetch, by three
  readers (1–7, 8–14, 15–21), each reading the Latin verse by verse against the WLC, the BSB with its footnotes and the
  KJV, with the Vulgate and Brenton's LXX where a verse looked odd; the NET for 14:15, 15 and 18. Their notes:
  `judg-notes-readers.md`. Each item below was checked here against the files.
- The printings: 1738 as printed (`text/orig/JDG.usfm`) and its raw OCR, the 1750 raw OCR (`sources/archive/`), and
  1573 through the MDZ search API (OCR snippets, canvases 171–184; no 1573 page image read). Every reading noted stands
  in all three: Castellio's own text, so noted, not corrected.

The yield is 4 notes proposed in 21 chapters (0.19 a chapter), one more near the bar (item 5), and 1 from the 1554
annotations (18:2).

## A. Modern Bibles follow the versions (kind A)

**Decision:** accept (Nathan, 2026-11-19: "Apply these notes as recommended, and fix the Deuteronomy 33:8 note to read *temptāvistī*.")

1. **14:15** *diē septimō petīvērunt ā Samsōnis uxōre*: Hebrew בַּיּוֹם הַשְּׁבִיעִי, "on the seventh day" (the KJV, the
   Vulgate *dies septimus*). The NRSVue "On the fourth day" (note "Gk Syr: Heb *seventh*"), the BSB "So on the fourth
   day" (note "LXX and Syriac; Hebrew seventh"), the NET "fourth" too, so not disputed. The timeline changes: in
   Castellio the Philistines threaten the bride on the seventh day, in both modern Bibles on the fourth, after three days
   of failure (14:14). 1738 *die septimo petierunt* (`text/orig` line 521), 1750 (OCR line 35803), 1573 (canvas 180) the
   same. Castellio knew the other reading: his 1554 margin at 14:15 reconciles the Greek's fourth day with the Hebrew's
   seventh (`judg-notes-1554.md`).
   **Apply:** `Judg.14.15` la: `diē septimō petīvērunt` → `diē septimō\f + \fr 14:15 \ft Versiōnēs antīquæ habent ‘diē quārtō’.\f* petīvērunt`

## B. Castellio's reading or text departs from the Hebrew (kinds B and C)

**Decision:** accept items 2–4 as recommended; item 5 left out as recommended (Nathan, 2026-11-19: "Apply these notes as recommended, and fix the Deuteronomy 33:8 note to read *temptāvistī*.")

2. **4:5** *habitāns sub palmā Dēboræ, inter Hormam et Bēthēl*: Hebrew בֵּין הָרָמָה וּבֵין בֵּית־אֵל, "between Ramah and
   Bethel" (the NRSVue, the BSB, neither with a note; the KJV; the Vulgate *inter Rama et Bethel*). Hormah (חָרְמָה) is
   another town, in the Negeb far to the south, which Castellio himself names at 1:17; Deborah's palm stood in the hill
   country of Ephraim, by Ramah. Elsewhere he gives Ramah as *Rāma* (19:13 *Gabaæ aut Rāmæ*), so this is a place
   changed, not a name spelled his way. 1738 *inter Hormam et Bethel* (`text/orig` line 136), 1750 (OCR line 33950),
   1573 (canvas 173) the same.
   **Apply:** `Judg.4.5` la: `inter Hormam et Bēthēl,` → `inter Hormam\f + \fr 4:5 \ft Hebraicē הָרָמָה, ‘Rāma’.\f* et Bēthēl,`
3. **15:19** *fissō māxillæ dente molārī*: Hebrew וַיִּבְקַע אֱלֹהִים אֶת־הַמַּכְתֵּשׁ אֲשֶׁר־בַּלֶּחִי, "God split the hollow place that
   is at Lehi" (the NRSVue, the BSB, neither with a note; the NET "the basin at Lehi", not disputed; Brenton's LXX and
   the KJV keep the hollow). Castellio follows the Vulgate (*molarem dentem in maxilla asini*): the water springs from a
   tooth of the jawbone Samson has thrown away, not from a hollow at the place Lehi, which his own verse names at its end
   (*quī fōns in Māxillā est*). A Vulgate reading of a plain Hebrew word, as Deut 26:5. 1738 (line 551), 1750 (OCR
   lines 35959–35960), 1573 (canvas 181) the same.
   **Apply:** `Judg.15.19` la: `fissō māxillæ dente molārī,` → `fissō māxillæ dente molārī\f + \fr 15:19 \ft Hebraicē הַמַּכְתֵּשׁ אֲשֶׁר־בַּלֶּחִי, ‘cavum quod est in Māxillā’.\f*,`
4. **18:2** *suōrum mīlitum abjectissimōs*: proposed in `judg-notes-1554.md` (item 1), where Castellio's annotation shows
   the reading is deliberate; found independently by the reader of 15–21. No Apply line here.
5. **10:4** *in totidem equīs equitantēs* (and 12:14 *in septuāgintā equīs equitantēs*), **near the bar**: Hebrew
   עַל־שְׁלֹשִׁים עֲיָרִים (12:14 עֲיָרִם), "on thirty (seventy) young donkeys" (the NRSVue, the BSB, neither with a note; the
   KJV "ass colts"; the Vulgate *pullos asinarum*). Castellio makes the judges' sons ride horses in both places, while he
   keeps asses elsewhere (5:10 *nitidās equitātis asinās*). Deliberate, it seems, as a mark of rank a classical reader
   would take; but the sense (a judge with many sons of standing) stands, and the horses may be counted with his
   classical vocabulary. **Recommendation (Claude): leave out**, by `num-notes.md` §F; if noted, one note covers both
   verses, as Exod 25:5. 1738 (lines 392, 471), 1750 (OCR 35130–31, 35508), 1573 (canvases 178, 179) the same.
   **Apply (only if accepted against the recommendation):** `Judg.10.4` la: `in totidem equīs equitantēs,` → `in totidem equīs\f + \fr 10:4 \ft Hebraicē hīc et 12:14 עֲיָרִים, ‘pullī asinōrum’.\f* equitantēs,`

## C. Castellio's *G.* … *H.* mark at 16:13–14 (recommended left out)

6. 1738 and 1750 print *G.* before *et clauo parieti adfixeris* (16:13) and *H.* after *nec eius vires cognitæ sunt*
   (the end of 16:14; the tool placed it at 16:15): a passage Castellio took from the Greek. **The NRSVue and the BSB both
   add nearly all of it from the Greek** too (the NRSVue "Compare Gk: Heb lacks …"; the BSB "See LXX and Vulgate; Hebrew
   does not include …"). Beyond them Castellio has only the wall (*clāvō parietī affīxeris*, as Brenton's LXX εἰς τὸν
   τοῖχον, where the modern Bibles fasten the pin in the loom) and the closing *nec ejus vīrēs cognitæ sunt* (not in
   Brenton; his source unidentified; it repeats 16:9). Castellio goes the modern Bibles' way here, as at Gen 4:8 and
   21:9, and Gen 44:6, a marked reading the NRSVue also adds, was left out (`gen-notes.md` §C); unlike Exod 2:22, 6:20 and
   Num 10:6, nothing marked is missing from the modern Bibles' story. **Recommendation (Claude): leave out.** Left out (Nathan, 2026-11-19, as recommended).
   **Apply (only if accepted against the recommendation):** `Judg.16.14` la: `nec ejus vīrēs cognitæ sunt.` → `nec ejus vīrēs cognitæ sunt\f + \fr 16:14 \ft Ā ‘et clāvō parietī affīxeris’ (16:13) ad ‘cognitæ sunt’ Castelliō ex Græcō vertit.\f*.`

## D. Considered and left out (the readers' full lists: `judg-notes-readers.md`)

- **The tool's candidates**: 1:14, 1:18, 6:14 (Castellio keeps the Hebrew with both Bibles); 9:29 (both leave the
  Hebrew, but only the narrative frame changes, as Deut 31:1); 10:12 *Maōniīs* (the Hebrew; 1738's footnote *Græcus et
  Latinus legerunt Chananæis*, Castellio's own 1554 margin, gives a reading his text does not follow); 12:7 (only the
  NRSVue follows the Greek); every numeral matches the Hebrew (carried across verse boundaries at 3:8–11, 4:14–15,
  7:21–22; 20:15 and 21:10 the Hebrew against the Vulgate); the short verses 3:12, 3:15 are words moved.
- **Near the bar, left out**: 1:29 *sed tribūtum pendentēs*, a clause the Hebrew lacks and Brenton's LXX has (καὶ
  ἐγένετο εἰς φόρον), Castellio's own (1573 canvas 171): small, and agreeing with Josh 16:10; 20:33 *Gabaānīs prātīs*,
  the one other kind-A place (both Bibles "west of Gibeah/Geba"), where only the ambush's position changes, as Deut
  11:30.
- **Construals the context or his own usage sets right**: 3:7 *Astarōthō* for the Asherahs (the Vulgate's; vocabulary of
  one cult); 3:15 *Jemīnis nepōtem* (Jemini is Benjamin to him, 19:16); 8:13 *sub ortum sōlis* (an old reading of a
  place name, as Deut 1:1); 8:18; 9:9, 9:13; 14:19–20.
- **Flagged in stages 3–5** (`judg1-21-stages3-5.md` point 4): 4:13 *Cisōnem cēpit* (1573 *cepit*; a loose verb, the
  sense kept); 5:29 *puellam puellārem* (a literal play on רַחַם רַחֲמָתַיִם; Castellio's 1554 annotation on 15:16 shows the
  doubled noun means one girl); 15:18 *mihi tuō* (his idiom, at least seven times in 1750); **20:23 *Quum enim Jōvam
  audīssent*** (1573 *audiuiſſent*, canvas 184: his own; the sense stands, and his *enim* does what the NRSVue's
  transposition of 22–23 does). Below the bar.
- **Only one of the two Bibles leaves the Hebrew** (Castellio with the Hebrew each time): 1:16, 1:27, 1:31, 2:3, 5:13,
  5:14, 5:28, 7:3, 7:5, 8:16, 9:31, 9:44, 10:11, 11:37, 12:2, 12:4, 13:19, 13:23, 14:3, 16:19, 19:2, 19:18, 19:30.
- **Disputed or uncertain Hebrew** (the NRSVue "Meaning of Heb uncertain", or the NET): 3:22–23, 5:2–16 (several),
  6:25–26, 9:6, 15:16, 18:7, 20:10, 20:42.
- **1738's footnotes** (all Castellio's 1554 margins, `judg-notes-1554.md`): none marks a departure the text needs
  noted; 18:30 *Mōsis nepōs* already agrees with the NRSVue and the BSB.

## E. A spelling in an accepted note (decision 37)

**Decision:** accept (Nathan, 2026-11-19: "Apply these notes as recommended, and fix the Deuteronomy 33:8 note to read *temptāvistī*.")

7. **Deut 33:8**: the note reads *quem tentāvistī in Massā*; the approved spelling is *temptō* (decision 37, brief.md:
   *temptō*, not *tentō*), as the settled text writes it everywhere else. Noticed while comparing the notes' wording.
   **Apply:** `Deut.33.8` la: `quem tentāvistī in Massā` → `quem temptāvistī in Massā`
