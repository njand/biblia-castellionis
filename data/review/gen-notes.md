# Genesis: light notes (Old Testament search)

Built 2026-11-18 by the process in `ot-notes-process.md` (decisions 1A–4A accepted the same day): kind A when the
NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio keeps it; kinds B and C where his
reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew agreeing, and nobody calls
the passage uncertain. Formulas as in `notes-audit.md` §A.

**Sources read:**
- `gen-notes-candidates.md` (`python -m pipeline notes Gen`): 27 BSB version notes, 41 numbers, 9 short verses.
- The NRSVue (Bible Gateway, read 2026-11-18) for all 50 chapters, with every footnote, by four readers (1–12, 13–25,
  26–37, 38–50), each reading the Latin verse by verse against the WLC, the BSB, the KJV and the Vulgate. Each find
  was checked here against the files.
- The printings: the 1738 and 1750 OCR (aligned to Gen 27; beyond it, their raw text in `sources/archive/`), the
  1726 OCR (`TXT/1`), and page images where shown: 1738 leaf 69 (10:12), leaf 94 (32:29), and 1573 canvas 53 (44:2).
- Castellio's own marks: 1738 prints *G.* (*G.L.*) … *H.* around readings he took from the Greek (1750 *Gr. lect.*
  … *Hebr.*; `docs/editions.md`). A search of both OCRs for Genesis finds five: 4:8, 11:12–13, 21:9, 32:29, 44:6.
  4:8 and 21:9 go the way modern Bibles go (no note); 11:12–13 and 32:29 are items 3 and 5; 44:6 is left out (§C).

## A. Modern Bibles follow the versions (kind A)

**Decision:** accept (Nathan, 2026-11-18: "Apply them")

1. **47:21** *populum … in oppida trānstulit*: Hebrew הֶעֱבִיר אֹתוֹ לֶעָרִים, "he removed them to the cities". The NRSVue
   ("made slaves of them"; note "Sam Gk Compare Vg: MT …") and the BSB ("reduced the people to servitude"; note "SP,
   LXX, Vulgate; Hebrew …") both leave the Hebrew; resettlement against enslavement. *in oppida transtulit* in 1738
   and 1750. The first kind-A note: item 8 adds the front-matter gloss.
   **Apply:** `Gen.47.21` la: `in oppida trānstulit.` → `in oppida trānstulit\f + \fr 47:21 \ft Versiōnēs antīquæ habent ‘populum in servitūtem redēgit’.\f*.`

## B. Castellio's text departs from the Hebrew (kinds B and C)

**Decision:** accept (Nathan, 2026-11-18: "Apply them")

2. **8:14** *diē septimō decimō*: Hebrew בְּשִׁבְעָה וְעֶשְׂרִים יוֹם, the 27th day (NRSVue, BSB, KJV; the Vulgate and the
   LXX also 27). Castellio's 17th repeats the date of 7:11, perhaps on purpose (the flood lasting exactly a year),
   but the text then says what the Hebrew doesn't. 1738 *septimodecimo* (OCR *fepti* … *modecimo*), 1750
   *septimodecimo*: not a slip of one printing.
   **Apply:** `Gen.8.14` la: `diē septimō decimō siccātā` → `diē septimō decimō\f + \fr 8:14 \ft Hebraicē בְּשִׁבְעָה וְעֶשְׂרִים יוֹם, ‘diē septimō et vīcēsimō’.\f* siccātā`
3. **11:12–13** *genuit Caīnānem*: the Hebrew has Arphaxad beget Shelah at 35 and live 403 years after (NRSVue, BSB,
   KJV, Vulgate); no Cainan, as in Castellio's own 10:24 (*Arphaxadus: Salam*). Castellio adds Cainan from the
   Septuagint (Luke 3:36 has him too), marking him *G.* … *H.* in 1738 and 1750, and mixes the years: Arphaxad at 35
   (the Hebrew; the LXX 135) begets Cainan and lives 330 years (Brenton's LXX 400; Cainan's 330 in the LXX); Cainan at
   130 (the LXX) begets Sala and lives 403 years (the Hebrew's figure for Arphaxad). The note names the Hebrew's son
   and years; the reader sees the rest.
   **Apply:** `Gen.11.12` la: `genuit Caīnānem,` → `genuit Caīnānem\f + \fr 11:12 \ft Hebraicē וַיּוֹלֶד אֶת־שָׁלַח, ‘genuit Salam’, et 11:13 post eum vīxit annōs quadringentōs trēs; Caīnānem Castelliō ex Septuāgintā addit.\f*,`
4. **29:27–28, 30** *Perageret proximum septennārium … complētīsque alterīs septem annīs*: Castellio has Jacob serve
   the second seven years before Rachel is given. The Hebrew מַלֵּא שְׁבֻעַ זֹאת is the wedding week: Rachel is given
   after it (29:28), and the seven years are served afterwards (29:30). The NRSVue ("Complete the week of this one"),
   the BSB, the KJV, the Vulgate (*hebdomada transacta*) and the LXX all read the week; the NRSVue has no note.
   Josephus reads it as Castellio does (*Ant.* 1.302, read in Whiston's translation by a reader). 1738 (`text/orig`) and
   1750 the same in all three verses. One note, at the first.
   **Apply:** `Gen.29.27` la: `Perageret proximum septennārium, sē` → `Perageret proximum septennārium\f + \fr 29:27 \ft Hebraicē מַלֵּא שְׁבֻעַ זֹאת, ‘implē hebdomadem hujus’; Castelliō septem annōs intellegit, ut Jōsēphus.\f*, sē`
5. **32:29** *quippe quod esset mīrābile*: the Hebrew has only לָמָּה זֶּה תִּשְׁאַל לִשְׁמִי, "why do you ask my name?"
   (NRSVue, BSB, KJV, Vulgate, all without a note). 1738 prints *vetans, G.L. quippe quod esset mirabile, H. eum*
   (leaf 94, read on the page), 1750 *G. L* … *H.*: Castellio's mark for a Greek reading. Brenton's LXX (`sources/parallel/lxx`)
   doesn't have the clause, so his Greek source isn't identified; the note says only what his mark says.
   **Apply:** `Gen.32.29` la: `quippe quod esset mīrābile, eum` → `quippe quod esset mīrābile\f + \fr 32:29 \ft Hebraicē לָמָּה זֶּה תִּשְׁאַל לִשְׁמִי, ‘quid quæris nōmen meum?’; ‘quippe quod esset mīrābile’ Castelliō ex Græcō addit.\f*, eum`
6. **44:2** *scyphum suum aureum*: Hebrew גְּבִיעַ הַכֶּסֶף, the silver cup (NRSVue, BSB, KJV, Vulgate *argenteum*), as
   Castellio's own 44:6 *scyphum argenteum*. 1573 prints *ſcyphum ſuum aureum* (canvas 53, read on the page), and so do
   1726 and 1738; 1750 corrects it to *argenteum*. In the text since its first posthumous printing, so noted, not
   corrected (as Rom 14:7 and 1 Cor 6:14 were). The other way, if you prefer: correct to *argenteum* with 1750.
   **Apply:** `Gen.44.2` la: `scyphum suum aureum.` → `scyphum suum aureum\f + \fr 44:2 \ft Hebraicē גְּבִיעַ הַכֶּסֶף, ‘scyphum argenteum’.\f*.`

## C. Considered and left out

- **The existing notes all pass and stay:** 4:23 (*Sī quem … interficerem* for the perfect הָרַגְתִּי), 6:2, 33:19
  (the NRSVue's own note gives "qesitah"), 49:6 (the NRSVue and BSB "hamstrung oxen", not called uncertain). 49:10 is
  disputed (the NRSVue gives alternatives), which by §3 would get no new note; its *vōx obscūra* tells the reader just
  that, against *Sospitātor*, so it stays.
- **Castellio already goes the versions' way:** 4:8, 4:15 (*Immō vērō*, "Not so!"), 21:9, 24:62, 25:22 (the Syriac),
  41:22, 41:56, 49:4, 49:26.
- **Only one of the NRSVue and the BSB leaves the Hebrew** (no consensus): 1:26, 2:2 (*sixth*), 9:7, 14:22, 19:17,
  22:13 (*one ram*; the BSB keeps *behind*, with Castellio's *pōne*), 27:5, 31:49, 31:53, 36:2, 38:5, 41:48, 44:4/44:6
  (the NRSVue adds "Why have you stolen my silver cup?" with the Greek, as Castellio does at 44:6 under *G.* … *H.*;
  the BSB keeps the Hebrew), 46:13, 50:16, 50:18.
- **Kind A on a name only:** 10:4 *Dodanimus* (the NRSVue and BSB Rodanim with the Samaritan and LXX): a single letter
  (ד/ר), the same people; no change of sense worth a note.
- **Called uncertain by the NRSVue** (no note): 6:3, 6:14, 15:2, 16:13, 24:63, 25:18, 27:40, 29:17, 31:42, 36:24,
  37:3, 41:43, 49:22.
- **Disputed readings of Castellio's, near the bar:**
  - 33:18 *ad Solymam … urbem Sichemī* for שָׁלֵם, a town Shalem (with the LXX, the Vulgate and the KJV), where the NRSVue
    and BSB have "safely". An old and living reading; the NET note couldn't be loaded to confirm it is disputed.
  - 10:11 *ortus Assur Nīnivem condidit* (Asshur as subject; the NRSVue and BSB "he went into Assyria"): the NET note
    allows both.
  - 38:14, 21 Enaim read as a common noun (*in prōpatulō*, with the KJV); the story is unchanged.
  - 14:18 *Solymæ rēx* for Salem: his name for it, as at Heb 7:1–2.
  - 18:19 *Nam sciō* ("I know him", with the KJV and Vulgate; the NRSVue notes "Heb known").
- **Paraphrase, names, vocabulary:** 14:8–9 (*quīnque rēgulī*), 18:20 (Gomorrah left out of *Sodomitārum flāgitiīs*;
  the outcry against the cities is kept, and 19:24 names both), Machpelah as *caverna duplex* (the name's meaning,
  with the LXX and the Vulgate), 24:60, 41:44, 47:2, 47:31 (*pluteum*, with the Hebrew and modern Bibles), 48:22.
- **Numbers:** every numeral the readers checked matches the Hebrew except 8:14 and 11:13. The others the tool listed
  are counts on one side only (*bis*, *totidem*, *alter*, *duplex*, a week).
- **Short verses:** paraphrase or words carried into the next verse (14:8–9, 17:25, 25:7, 25:13, 31:21, 36:14, 41:46, 44:4).

## D. A correction to the settled text (found by the reading, not a note)

**Decision:** accept (Nathan, 2026-11-18: "Apply them")

7. **10:12** *Refem*: 1738 prints *Reſem* with long s (leaf 69, read on the page: the stroke has the nub on the left
   only, no crossbar), for רֶסֶן, Resen (Vulgate *Resen*); the 1726 OCR, which tells s from f, reads *Resem*. The 1738
   and 1750 OCRs and Wikisource read long s as f, and the slip passed from them into the settled text and the printed
   text. The same correction by hand in `text/orig/GEN.usfm` (line 305: `et Refem inter` → `et Resem inter`) and a row
   in `data/decisions/Gen.orig.tsv`.
   **Apply:** `Gen.10.12` la: `et Refem inter` → `et Resem inter`

## E. Front matter, with item 1

**Decision:** accept (Nathan, 2026-11-18: "Apply them")

8. If item 1 is accepted, the gloss for *versiōnēs antīquæ* (ot-notes-process.md §6), added to the Old Testament part of
   the notes row in `text/FRT.usfm` (line 30), after *Paucæ etiam vōcēs explicantur quās ipse fīnxit aut Hebræās
   retinuit.* and inside the same `\zvt`, by hand (it has no verse id), with `docs/front-matter.md` and the OT test in
   `pipeline/tests/test_frontmatter.py`:
   *Versiōnēs antīquās, Græcam Septuāgintā interpretum, Syram, Vulgātam, Samarītānōrum Pentateuchum, tum adnotō, cum
   eās interpretēs nostræ ætātis sequuntur, ubi textus Hebræus corruptus vidētur.* (`latin macron-check`: no word to
   check; *Samarītānōrum* as the dictionaries mark it.)

## F. For the next books

- 1750 marks *G. L. et Mariam eorum sororem H.* at **Exod 6:20** (Miriam, from the Greek): a candidate for the Exodus
  pass. Searching each book's OCR for Castellio's *G.* … *H.* marks is worth making part of the candidates tool.
