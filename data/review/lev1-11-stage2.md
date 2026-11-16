# Leviticus 1–11, stages 1–2: Wikisource against 1738 and 1750

Proposed 2026-11-15 (decision 30's standing rule), on the Old Testament route of Exodus 21–30
(`data/review/exod21-30-stage2.md`).

- **Base**: the 1738 Leipzig edition (decision 1). Stage 1 drafted Wikisource's Leviticus 1–11 (all Wikisource has
  of the book) as **`text/draft/LEV.usfm`** (BSB paragraphs, 299 verses). 1738 is read from its hOCR (Leviticus 1–11
  is leaves 156–167), so every reading below names its leaf (the hOCR page; the archive.org image is one lower).
  Chapters 12–27 go the Exodus 31–40 route (decision 68): `data/witnesses/read-1738/Lev12-27.voted.tsv`, leaves
  167–187, waits to be read on the page.
- **Versification**: every chapter has the KJV's count (17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47); Wikisource
  keeps 1738's numbers, which here are the KJV's (6:1 *Item Mosem Jova sic adlocutus est*, as the KJV's 6:1). No
  edits. Verse boundaries are checked again in stages 3–5 with the KJV beside each verse.
- **Collation** (`python -m pipeline collate Lev 1-11`, `data/calibration/Lev1-11-collation.tsv`): 1738 base, 1750
  witness (your 1726–27 text stops at Exodus 20). 16 "correct" places (1750 with 1738 against Wikisource): 5 are
  1738's *sumsit* (stage 3 and the printed text), the rest read on the page (below). The 480 places where only 1738's
  OCR differs were sifted for real Latin words (`pipeline latin macron`, the settled text's forms) where 1750 does
  not side with Wikisource: 29, all OCR noise but 4:11 and 8:31 (below). The 84 divisions and 47 edges with 1750
  silent were looked over: 2:9 (below). **The 20 verses 1738's OCR covers under 60%** (3:12, 3:13, 3:15, 3:16, 4:1,
  4:2, 4:18, 4:30, 5:19, 6:10, 6:26, 7:1, 7:38, 8:10, 8:20, 8:26, 9:1, 11:14, 11:25, 11:29) were read whole on the
  page images: one differs (8:10).
- **Kept after checking**: 4:27 *ita uti sese* (OCR *vtifefe*; leaf 159 *vti ſeſe*), 6:17 *sive delictum sive noxa*
  (leaf 161), 8:15 *sanguinem sumpsit, et eo* (leaf 163 *ſanguinem ſumſit, | et eo*), 9:13 *iisdem*, 11:29
  *mustolam* (leaf 166 *muſt*-|*lam*, the fifth letter broken; 1750 *mustolam*: Gaffiot's *mustela* is stage 3's
  question). Punctuation that differs is stage 5's.
- **Printed spellings seen** (for stage 2b, `data/decisions/Lev.orig.tsv` when the printed text is built): 3:15
  *exemtam* (leaf 158), 8:10 *ſumto* (163), 8:15 and 8:26 *ſumſit* (163), 11:14 *miluum* (166), 11:29 *muſt*-|*lam*.

**Applied to the draft** under decision 30's standing rule.

## 1. Wikisource slips and readings 1738 has otherwise (10)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-15)

1. **Lev 2:9** *et inara adoleat* → *et in ara*. 1738 *et in ara adoleat* (leaf 157).
    **Apply:** `Lev.2.9` la: `et inara adoleat` → `et in ara adoleat`
2. **Lev 3:2** *in introitu ocularis tabernaculi* → *oracularis*, as everywhere else in the book. 1738 *intro-|itu
   oracularis tabernaculi* (leaf 157); 1750 the same.
    **Apply:** `Lev.3.2` la: `introitu ocularis tabernaculi` → `introitu oracularis tabernaculi`
3. **Lev 4:11** *interaneis at que fimo* → *atque*. 1738 *at-|que fimo* (leaf 158), divided at the line's end.
    **Apply:** `Lev.4.11` la: `interaneis at que fimo` → `interaneis atque fimo`
4. **Lev 6:19** *quo die unguetur* → *ungentur* (Aaron and his sons, the day they are anointed). 1738 *quo die
   vngentur* (leaf 161); 1750 the same.
    **Apply:** `Lev.6.20` la: `quo die unguetur` → `quo die ungentur` (6:19 before the versification below)
5. **Lev 8:2** *cum ejus filiis vestibus et oleo* → *vestibusque*. 1738 *cum eius filiis veſtibusque et | oleo*
   (leaf 162); 1750 the same.
    **Apply:** `Lev.8.2` la: `filiis vestibus et oleo` → `filiis vestibusque et oleo`
6. **Lev 8:10** *quae in eo tabernaculo continebatur* → *continebantur* (*omnia, quae*). 1738 *continebantur*
   (leaf 163).
    **Apply:** `Lev.8.10` la: `tabernaculo continebatur` → `tabernaculo continebantur`
7. **Lev 8:31** *et inibi eam comedire* → *comedite*. 1738 *eam comedite* (leaf 163).
    **Apply:** `Lev.8.31` la: `eam comedire` → `eam comedite`
8. **Lev 10:15** *Atmum receptitium* → *Armum*. 1738 *Ar-|mum receptitium* (leaf 165); 1750 the same.
    **Apply:** `Lev.10.15` la: `Atmum receptitium` → `Armum receptitium`
9. **Lev 10:16** *Elazaro et Ithamaro* → *Eleazaro*, as 10:6 and 10:12 (*Eleazarum*). 1738 *Eleazaro* (leaf 165);
   1750 the same.
    **Apply:** `Lev.10.16` la: `Elazaro et Ithamaro` → `Eleazaro et Ithamaro`
10. **Lev 11:9** *eis vescivobis licebit* → *vesci vobis*. 1738 *eis veſci vobis licebit* (leaf 166).
    **Apply:** `Lev.11.9` la: `eis vescivobis licebit` → `eis vesci vobis licebit`

## 2. Found in stages 3–5: Wikisource slips, and 1738's misprint (7)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-15)

The readers of stages 3–5 (`data/review/lev1-27-stages3-5.md`) found these; each read on 1738's page since (crops
of the leaf named) and checked in 1750's OCR (`sources/archive/1750/text.txt`).

1. **Lev 6:12** *Ignis autem in ara inextinctus ardeto* → *inexstinctus*, as the same verse's *inexstincto*. 1738
   *inexſtinctus* (leaf 160, col. 1): a Wikisource slip.
    **Apply:** `Lev.6.12` la: `in ara inextinctus ardeto` → `in ara inexstinctus ardeto`
2. **Lev 8:25** *totosque lacies* → *lactes*, as 8:16 *totos lactes* (Gaffiot *lactes*, the small intestines;
   *lacies* is no word). **A Wikisource slip**: 1738 prints *lactes* with the ct ligature (leaf 163, col. 0, line 64;
   enlarged 6× on 2026-11-16, the arched stroke runs from the c into the t, as in *ſanctum*; read small it looks like
   *ci*, which is how Wikisource and the OCR's *laciei* took it, and how I first misread it); **1750 *totosque lactes***
   (line 15228). Corrected 2026-11-16 after Nathan's side session read the ligature.
    **Apply:** `Lev.8.25` la: `totosque lacies` → `totosque lactes`
3. **Lev 10:1** *coram Jove* → *Jova*. 1738 prints *coram Ioue* (leaf 165, col. 0, line 2), the only such form in the
   book (everywhere else *coram Ioua*); **1750 *coram Ioua*** (line 15426). 1738's misprint, corrected for the
   reading edition; the printed text keeps *Ioue*. Re-read enlarged 6× on 2026-11-16: *co-|ram Ioue* (line 4–5), the
   e's bar plain. Kept (Nathan, 2026-11-16).
    **Apply:** `Lev.10.1` la: `coram Jove ignem` → `coram Jova ignem`
4. **Lev 10:1** *illis injussu* → *illius injussu* ("without his bidding", God's). 1738 *illius in-|iuſſu* (leaf 165,
   col. 0); 1750 *illius in-* (line 15426): a Wikisource slip, missed by the collation.
    **Apply:** `Lev.10.1` la: `alienum, illis injussu` → `alienum, illius injussu`
5. **Lev 11:26** *neque visulcae sunt* → *bisulcae*. 1738 *biſulcæ* (leaf 166, col. 1, line 68): a Wikisource slip
   (the printed-text draft took *visulcae* from it too, to correct there).
    **Apply:** `Lev.11.26` la: `neque visulcae sunt` → `neque bisulcae sunt`
6. **Lev 7:6** *ut quod sacrosanctum fit* → *sit*, as 6:25 and 6:29 *quod sit sacrosanctum*. 1738 prints *ſanctum ſit.*
   (leaf 161, col. 0, line 78; enlarged 6×: the long s has only the left nub of the bar, where the f of *fiet* three
   lines up, line 75, has it through the stem); 1554 *ut quod ſacroſanctum ſit* (MDZ bsb10196330, canvas 67, read by
   the side session Nathan forked, 2026-11-16). A Wikisource slip the collation missed, as the 1738 and 1750 OCRs read
   ſ as f. Added 2026-11-16 (Claude; Nathan read the page too).
    **Apply:** `Lev.7.6` la: `ut quod sacrosanctum fit.` → `ut quod sacrosanctum sit.`
7. **Lev 11:29** *mustolam* → *mustelam*. **A Wikisource slip**: 1738's fifth letter is damaged (leaf 166, col. 0,
   line 79, *muſt?-|lam*: enlarged, only a lower curve and a speck are inked, no closed ring as an o would show; it fits
   a broken e). 1750 prints *mustolam*, most likely a misreading of the damaged type, and Wikisource follows it.
   Castellio's 1554 has *muſtelã* (MDZ bsb10196330, canvas 70, read by the side session Nathan forked) and the 1726
   OCR *mustelam*; Gaffiot has only *mustēla*. The printed text reads *mustelam* (`data/decisions/Lev.orig.tsv`).
   Nathan, 2026-11-16: "Apply all of your recommendations".
    **Apply:** `Lev.11.29` la: `habetote: mustolam,` → `habetote: mustelam,`

**Applied to the draft** under decision 30's standing rule.

## 3. Versification (decision 5)

Reader B of stages 3–5 found Wikisource's chapter 6 dividing three verses otherwise than the KJV (the counts agree):
6 edits in `data/versification/Lev1-11.draft.edits.tsv`, applied (`versify Lev --draft --apply`; same words, the
KJV's count). The KJV's 6:7 (*illique pontifex … exorato*) was inside Wikisource's 6:6, its 6:9 was Wikisource's
6:8–9, its 6:13 (*igni semper in ara inexstincto ardente*) the end of 6:12, its 6:14 Wikisource's 6:13–14, and its
6:19 only *De libamine autem Aharonis, aut ejus filiorum, inquit,* (as Exod 30:17), 6:20 going on at *quod Jovae
libabunt*. The readers' rows were re-keyed.

## 4. Names made one with the settled text (decision 46) (1)

**Decision:** accept (Nathan, 2026-11-16: "Yes, Elsāphānem")

1. **Lev 10:4** *Elisaphanem* → *Elsaphanem*, as the settled Exod 6:22 *Elsāphān*: the same man, Uzziel's son.
   *Elsāphān* follows the Hebrew *ʾElṣāp̄ān*, *Elisaphan* the Greek Ἐλισαφάν. 1738 prints *Eliſaphanem* (leaf 165,
   col. 0, line 16, read enlarged 2026-11-16), and so do 1750 and Wikisource. The printed text keeps it
   (`data/decisions/Lev.orig.tsv`, decision 58).
    **Apply:** `Lev.10.4` la: `Misaelem et Elisaphanem,` → `Misaelem et Elsaphanem,`
