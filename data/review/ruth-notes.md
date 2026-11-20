# Ruth: light notes (Old Testament search)

Built 2026-11-19 in phase 2 of decision 85 (PLAN.md §4), beside `propose`, by the process in `ot-notes-process.md`
(decisions 1A–4A), as Judges' (`judg-notes.md`) and Joshua's (`josh-notes.md`), with the bar as it now stands (Nathan,
2026-11-19: no note for a departure without plot or theological significance; `num-notes.md` §F: a construal the
context sets right is left out). Kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and
Castellio keeps it; kinds B and C where his reading or his text departs from the Hebrew against the NRSVue, the BSB and
the Hebrew agreeing, and nobody calls the passage uncertain. Castellio's 1554 annotation on Ruth (one, on 3:16) and the
1554 text's margins, read on the page in this pass, are in `ruth-notes-1554.md`.

**Sources read:**
- `ruth-notes-candidates.md` (`python -m pipeline notes Ruth`): 3 BSB version notes (4:4, 4:20 against MT; 3:15 with
  MT), 1 number (1:1), 1 short verse (1:7), no *G.* … *H.* marks.
- The NRSVue (Bible Gateway, read 2026-11-19) for all four chapters with their footnotes (not stored); the NET for 3:15
  and 2:1. Every verse of the preview (`text/draft/RUT.preview.usfm`) read against the WLC, the BSB with its notes and
  the KJV, with the Vulgate where a verse looked odd.
- 1738's four footnotes and the asterisk at 3:16, from phase 1 (`ruth1-4-transcription.md`), with leaf 318's image
  (`sources/archive/crops/1738-page-0318.jpg`) seen for 1:8 and 1:10.
- The printings: 1738 as printed (`text/orig/RUT.usfm`), the 1750 raw OCR (`sources/archive/1750/text.txt`), **1554**
  (canvases 150–152 and 825) and **1573** (canvases 186–187) on page images read here (`ruth-notes-1554.md`).

The yield is 1 note proposed in 4 chapters (0.25 a chapter), from the 1554 annotation, which the candidates tool found
too (3:15); one more place near the bar recommended left out (2:1).

## A. Modern Bibles follow the versions (kind A)

None. The two places where the BSB leaves the Hebrew (4:4 "if you", 4:20 *Salmon*; the NRSVue at both) are places
where Castellio already reads as they do (§C).

## B. Castellio's reading or text departs from the Hebrew (kinds B and C)

**Decision:** accept item 1; item 2 left out, as recommended (Nathan, 2026-11-19: "Yes, settle it", on "Settle Ruth for now, with the 3:16 note?")

1. **3:16** *Illa in oppidum ad socrum vēnit*: Hebrew 3:15 ends וַיָּבֹא הָעִיר, "and **he** went into the city" (Boaz),
   and 3:16 goes on וַתָּבוֹא אֶל־חֲמוֹתָהּ, "and she came to her mother-in-law". The NRSVue has "he" here
   (no footnote), the BSB "Then he went into the city" (note: "Most Hebrew manuscripts; many Hebrew manuscripts,
   Vulgate, and Syriac she went"), the NET "he went" (note: the MT masculine; many medieval manuscripts, with the Syriac
   and the Vulgate, the feminine; the KJV follows the feminine). So the three agree on the Hebrew, and the NET treats
   the feminine as a variant, not the passage as uncertain. Castellio reads "she", with the Vulgate (*Quæ portans
   ingressa est civitatem*), and joins it to 3:16. **Deliberate**: his 1554 annotation (canvas 825, column 345) says
   *Venit in Hebræo maſculinum eſt: ſed mendum eſſe conijcio, tum ex ſenſu, tum ex uetere uerſione*
   (`ruth-notes-1554.md` §1); 1573 prints the same annotation, shortened, after chapter 3 (canvas 187). The reading
   stands in 1554 (canvas 152, column 279, *Illa in op-|pidum ad ſocrum uenit*), 1573 (canvas 187, its verse 16), 1738
   (`text/orig/RUT.usfm` line 89, *Illa in oppidum ad socrum venit:*, with an asterisk after *venit:*) and 1750 (OCR
   line 37361, *Illa in* [*oppidum*] *ad focrum venit*). Kind C (a version followed where modern Bibles keep the Hebrew).

   **Why it passes the bar**: who moves changes what happens next. In the Hebrew, Boaz leaves the threshing floor for
   the town at once, which is what Naomi counts on at 3:18 (*homō numquam hodiē, nisi rē perfectā, conquiēscet*) and
   where 4:1 finds him, at the gate; in Castellio only Ruth goes, and Boaz's prompt start on the redemption drops out
   of the story. A reader with a modern Bible meets "he went into the city" and finds *Illa* here. It is also the one
   departure Castellio himself defended. Near the bar only in being a single clause.

   The form of Gen 49:6 (*Hebraicē* Hebrew, ‘Latin’; *Castelliō* … *legit, ut Vulgāta*), with the other verse cited
   *C:V* as the brief asks. Words checked with `pipeline latin macron` (Hebraicē, ille, oppidum, vēnit perfect, legit
   present, Vulgāta).
   **Recommendation (Claude): accept.**
   **Apply:** `Ruth.3.16` la: `Illa in oppidum` → `Illa in oppidum\f + \fr 3:16 \ft Hebraicē 3:15 וַיָּבֹא הָעִיר, ‘ille in oppidum vēnit’; Castelliō וַתָּבֹא, ‘illa’, legit, ut Vulgāta.\f*`

2. **2:1** *hominem mīlitārem*, **near the bar**: Hebrew אִישׁ גִּבּוֹר חַיִל, "a man of substance / of standing" (the NRSVue
   "a prominent rich man", no footnote; the BSB "a prominent man of noble character"; the NET "a wealthy, prominent
   man", its note giving "mighty in substance"; the KJV "a mighty man of wealth"; the Vulgate *homo potens, et magnarum
   opum*). Castellio makes Boaz a soldier. It is his own reading of חַיִל, which his 1554 annotation on Judg 18:2 states
   (*בני חיל non fortes semper, sed milites dicuntur*, `judg-notes-1554.md`), and it loses the match between Boaz here
   and Ruth's אֵשֶׁת חַיִל at 3:11 (*mulierem virtūte præditam*). But nothing in the story turns on it: Boaz's standing,
   his fields and his kinship stand, and his wealth is plain from 2:3–17. A construal of one word, below the bar as
   Judg 10:4 (the judges' sons on horses) was. 1554 (canvas 151, column 277, *hominem militarem*), 1573 (canvas 186),
   1738 (`text/orig/RUT.usfm`) and 1750 (OCR line 37144) the same.
   **Recommendation (Claude): leave out.**
   **Apply (only if accepted against the recommendation):** `Ruth.2.1` la: `hominem mīlitārem,` → `hominem mīlitārem\f + \fr 2:1 \ft Hebraicē אִישׁ גִּבּוֹר חַיִל, ‘vir potēns opibus’.\f*,`

## C. 1738's footnotes (recommended: none printed)

1738 prints four footnotes and an asterisk in Ruth (`ruth1-4-transcription.md`). Three are Castellio's 1554 margins;
the fourth is first found in 1573 (`ruth-notes-1554.md`, "The 1554 text's own margins"):

3. **1:8** *m) me, propter vestros maritos.* Not 1554's (which has *a ueſtros maritos, dũ uiuerent.* at the same word,
   canvas 150, column 276); 1573's (canvas 186, *a me, ꝓpter veſtros maritos.*), whoever wrote it. A gloss on the
   sense of *tum ergā mortuōs tum ergā mē*, which the verse says plainly.
4. **1:10** *n) hoc est, ituras cum ea reuertente. Nec enim reuertebantur ipsæ in Iudæam, quum in Iudæa numquam
   fuissent.* Castellio's (1554 *b*, canvas 151, column 277). It explains his *esse reversūrās* ("return" of women who
   had never been in Judah), which is the Hebrew's own word (נָשׁוּב, "we will return", the NRSVue and the BSB "return").
   No departure.
5. **1:13** *a) Inuita a vobis diuellor, sed cogit Ioua, qui me vestris maritis priuauerit.* Castellio's (1554 *c*,
   canvas 151, column 277). A paraphrase of *Equidem valdē vestrā causā doleō; sed mē Jōvæ manūs urget*. No departure.
6. **1:20** *b) Noemis ab amœnitate et iucunditate: Mara ab acerbitate et mœrore dicitur.* Castellio's (1554 *d*,
   canvas 151, column 277). The meaning of the two names, the one gloss a modern reader might want: the NRSVue gives the
   same in footnotes ("That is, *pleasant*", "That is, *bitter*") and the Vulgate puts it in its text. But the edition
   prints no glosses (brief.md: "No marginal notes or commentary"; 1738's glosses in Joshua and Judges were not printed,
   `josh-notes.md` §E, `judg-notes.md` §D), and Castellio's own verse makes the point (*vocāte mē Māram: nam ingentī
   mœrōre mē affēcit*).
7. **The asterisk at 3:16** (after *venit:*, no footnote on the page): it stands where the lemma of Castellio's 1554
   annotation ends, and 1573 prints that annotation after chapter 3, so it may be a trace of it (not proved). Item 1
   covers the place.

**Recommendation (Claude):** print none of the four, as in Joshua and Judges; item 1 is the edition's note at 3:16.
If Nathan wants 1:20's gloss, it would need a form of its own (it is not a departure) and a line in the front matter;
not drafted.

## D. Considered and left out

- **The tool's candidates**: **4:4** (BSB against MT: "if you will not redeem", with Hebrew manuscripts and the
  versions; the NRSVue the same, "Heb mss Gk Syr Vg: MT *if he*"): Castellio's *sīn minus redēmptūrus es* already reads
  "you", and his 1554 annotation calls the Hebrew's יגאל a mistake for תגאל; **4:20** *Salmōnem* (both Bibles *Salmon*
  with the versions, "Gk: Heb *Salmah*"): Castellio with them, and a name; **3:15** is item 1; **1:1** the numeral: the
  Latin has *duōbusque fīliīs* for וּשְׁנֵי בָנָיו (the tool does not read *duōbus* with *-que*); **1:7** short: the Hebrew's
  "the place where she had been" and "they went on the way" folded into *illinc dīgressa … revertī contendit*, the sense
  kept.
- **Castellio with the versions as the NRSVue is**: **4:5** *habendā tibi est etiam Rūthā* ("you must also take Ruth"):
  the NRSVue follows the Old Latin and the Vulgate ("OL Vg: Heb *from the hand of Naomi and from Ruth*"); the BSB keeps
  the Hebrew's words but also has "you must also acquire the widow"; the Hebrew's written קניתי ("I acquire") against
  its read קָנִיתָה is disputed. Castellio gives the sense both Bibles give.
- **The Bibles differ or the Hebrew is uncertain**: **1:13** *Equidem valdē vestrā causā doleō* (כִּי־מַר־לִי מְאֹד מִכֶּם: the
  NRSVue "it has been far more bitter for me than for you", the BSB "it grieves me very much for your sakes", Castellio
  the BSB's and the KJV's way); **1:21** *malō afflīxerit* (עָנָה בִי: the NRSVue "dealt harshly with me", note "Or *has
  testified against*", the BSB "testified against me"; Castellio with the versions and the NRSVue); **2:7** *tam paulum
  manet domī* (the NRSVue "Compare Gk Vg: Meaning of Heb uncertain").
- **His vocabulary or a construal the context sets right**: 1:1 *præsidēs prōcūrābant* for the judges; 4:1, 4:11 *in
  cūriam*, *in cūriā* for the gate; 3:9 *gremium tuum exporrigās* (כְּנָפֶךָ, "your cloak" or "wing": the garment's fold,
  the sense kept); 3:15 *sex hordeī mēnsūrās* (the Hebrew "six" with no measure, as the BSB); 3:7 *ad fīnem mētæ* (the
  end of the heap).
- **Names**: 1:2 *Mahalon*, *Chelion* (the NRSVue glosses their meanings; not departures); 4:18 *Hezronem*.

## For `docs/editions.md`

The edition facts found in this pass are listed at the end of `ruth-notes-1554.md` (1554's text, margins and
annotation on Ruth; 1573's changed 1:8 gloss, its *ANNOTATIO.* after chapter 3, and 1:18 *contradicere* → *dissuadere*).
