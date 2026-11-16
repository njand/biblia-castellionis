# Castellio's text as printed, Genesis and Exodus 1–20 (1738): proposed for approval

Built 2026-11-14 (`python -m pipeline orig Gen 1-50`, `Exod 1-20`). The drafts are `text/orig/draft/GEN.usfm` and
`EXO.usfm`; how each word was made, word by word, is in `gen1-50-orig.md` and `exod1-20-orig.md`. This file is the
summary, the questions for the reading edition the page readings raised, and the Decision line.

**Decision:** approved for Genesis (Nathan, 2026-11-15: "Approve Genesis"; moved to `text/orig/GEN.usfm`), and for Exodus 1–40 (Nathan, 2026-11-15: "Yes, approve"; the drop capital's word set as a normal capitalized word); moved to `text/orig/EXO.usfm`.

## What changed since 2026-11-13

1. **1738 is read from its hOCR** (`archive.witness`): the same ABBYY words as `text.txt`, with each word's leaf and
   line. The drafts came out the same within a few words (Genesis: 16 fewer OCR reads of 24,239 before the fixes
   below). The printer's catchword at a page's foot is left out (it paired with Gen 44:1 *Deinde* on leaf 106).
2. **Paragraphs are 1738's own** (`archive.indents`): a line that starts 40–140 px inside its column's margin after
   a line that ends a sentence, past a verse number in the margin; drop capitals, the italic chapter summaries and
   1738's footnotes left out. **83 paragraphs inside the Genesis chapters, 44 in Exodus 1–20**, each also beginning
   a chapter. Every one was looked at on the page image (sheets of the line and the line above). Of the first 108
   found, one was a drop capital's third line (Gen 16:16; now excluded) and two were mapped one word early (Gen
   38:11/12 and 38:24, now set before the word the line begins with); two flush lines that had passed (Gen 14:24,
   30:2) went with a better margin estimate. Two full leaves were checked for indents missed (120: Exod 6:26
   found after a fix to read a number the OCR gives as letters; 126: Exod 12:17, a leaf's first line, recorded as
   a `¶` row in `data/decisions/Exod.orig.tsv`). A paragraph can begin inside a verse; then the USFM has `\p` in the
   verse's line. 1738's chapter 3 begins at the KJV's Gen 2:25 (*Ceterum*), so that is a paragraph here.
3. **Each verse's 1738 leaf** is in `data/orig/Gen.pages.tsv` and `Exod.pages.tsv` (from its words, not its OCR row's
   edges). The site's banner over the printed text now links to the leaf at the Internet Archive
   (`archive.org/details/bibliasacraexseb01cast/page/n<leaf − 1>`, as `archive.PAGE_IMAGE`; checked on Gen 44, whose
   first verse is on leaf 107, image n106).
4. **189 rows read on 1738's leaves** in `data/decisions/Gen.orig.tsv` (142) and `Exod.orig.tsv` (47; one of them the
   Exod 12:17 paragraph), with
   `pipeline orig BOOK CH --sheets` (contact sheets of the words' lines, `orig.sheets`, `archive.sheet`):
   - **The 273 doubtful words**: 184 were *Tum*, made doubtful by two chapter openings set in capitals (*TVm*);
     words set in capitals no longer count as a spelling (`lexicon`). The other **78 are *cum*/*cumque***, which
     1738 prints as *cum* (the preposition) and *quum*/*quumque* (the conjunction), every one read: 51 *quum*/*quumque*, 27
     *cum*/*cumque*. A row can name the occurrence in the verse (`cum#2`), since a verse may have both.
   - **92 spelling-prone words** (the settled spelling is one an approved word or stem rule writes for another): 1738
     prints *adpellauit* (×16), *adscendebat*, *adligauit*, *adsignauit*, *adfigeris*, *adstare*, *adspice*,
     *herus* (×4), *intelligam*, *paullum*, *paullisper*, *peremti*, *emtitiorum*, *connubiis*, *pœnituit*,
     *mœstos*, *sobolem*, *adolescens*, *conditionem*, *concionem*, *quoties*, *eamdem*, *audiuerant*,
     *præteriissent*, *seruiuissent*, *querceto* …; 18 as the settled spelling (*exspectauit*, *cærimoniam*,
     *multitudo*). Stem rules are now included (`spelling_prone`).
   - **Near misses**: guesses where the OCR word is itself a Latin word (`pipeline latin macron`), about 30 read;
     most were the settled word (*adamabat*, *alteræ*, *facultates*). The differences are below.
   - **The ad- prefix, -mt-, æ written out, Ebræ-**: 1738 leaves *ad-* unassimilated (*adfecimus*, *adparuisset*),
     prints *sumsit*, *sumta*, *emtus*, *redemtum* without p, writes *Ebræorum* without H, and its OCR writes æ as
     *ae*. These are now printer's variants (`VARIANTS`), so the OCR's own form is taken (95 + 67 words).
5. **A sample of the words still not read in the OCR**, to measure the rest: 36 chosen at random (`random.seed
   (20261114)`), 31 found on the page: 29 as drafted, 2 not (*depsita* for *depstā*, Gen 18:6; *conditionem*, Gen
   42:20, which led to the stem rules above). So roughly 1 in 15 of these words may differ from the page.

## What is left

- **Every word not read in the OCR is now read on 1738's leaves** (decision 68; 2026-11-14), and Exodus 21–30's
  printed text with them (settled since): 3,022 words in all, on contact sheets of each word's line (`orig.sheets`)
  and then of thirteen lines for the 563 whose first crop missed them, by six readers and me, each row in
  `data/decisions/Gen.orig.tsv` (1,971 *read*) and `Exod.orig.tsv` (1,113). **About 150 differ from the draft**:
  1738's unassimilated *ad-* (*adfluentiam*, *adpendit*, *adplicabis*), *-mt-* without p (*contemsit*, *sumtis*),
  *exs-*, *nec ne* as two words, capitals (the chapters' opening words in capitals, *PRINCIPIO*, *COmmissum*), and
  1738's misprints (Gen 37:7 *venerebantur*, 43:30 *miersatione*, Exod 2:19 *Aegytio*, 4:1 *adparauisse*, 23:30
  *fctifices*), kept as printed (decision 58). Eleven are **different words** from the settled text, and 1554 and
  1573 agree with 1738 in each: proposed for the reading edition in `data/review/ot-readings-1554-1573.md`.
  The last two, read 2026-11-15: Exod 12:4 *ac-|commodata.* (the line break falls inside the word, no hyphen
  printed; leaf 125) and 26:24 *coapta-|bis.* (leaf 140).
- The review files are now `gen1-50-orig.md` and `exod1-30-orig.md` (the latter replaces `exod1-20-orig.md` and
  `exod21-30-orig.md`).
- **The punctuation pass (2026-11-15; decision 58)**: every mark the draft took from the settled text was read on
  1738's leaves: the 539 places listed in the review files, the 47 where a stop before a lower-case word had been
  dropped (*stray*), and a random sample of 148 of the 2,812 words whose (empty) mark was assumed, by five readers on
  contact sheets of each word's lines and then, for the 60 whose crops missed the line, by one reader on the whole
  leaves; the last six by me. Each mark is now a `|` on the word's row in `data/decisions/Gen.orig.tsv` and
  `Exod.orig.tsv`. **The page differs from the draft in 45 places**: 41 of the listed ones (mostly a colon where the
  settled text has a comma or full stop: *coleret: et*, Gen 3:23; *Ioua: quid*, 4:6; *peperit:* 4:1) and 4 of the
  *stray* ones (Gen 8:19 *volucrum;*, 22:2, 24:47 *filia?*, 26:8). **The random sample had none** (148 of 148 as
  drafted; at most about 2% of the unchecked 2,664 can differ), so those are left as they are. The lists of
  punctuation not from the OCR are now empty.
- **Found on the way, all fixed in the draft and read on the page**:
  - **1738 prints the capital Æ as two letters** (*in Aegypto*, leaf 114), where 1573 prints *Æ* (*Ægypti*, canvas
    837): 205 words (*Ægypt-* → *Aegypt-*) corrected by `orig.untie_capitals` (Old Testament only; tested).
  - **The OCR reads the œ of cœp-, cœn- as ce** (*cceperunt*), which the lexicon had learned: 10 words, now *cœperunt*,
    *cœnam* (`orig.cc_for_oe`); and lower-case *ae* the lexicon took from the OCR (*aetatis* 16, *quaerenti*,
    *præterea* …), tied as 1738 prints them (`orig.retie`).
  - **Word forms** the readers saw printed otherwise: Gen 24:45 *eram* (the lexicon had *heram*, "mistress"), 27:36
    *næ*, 18:31 *næ*, 31:31 *eriperes*, Exod 9:4 *ægyptium*, 10:5 *consumturæ*, *Ismael* in all ten places read (not
    *Ismæl*: also wrong in the settled text, proposed in `spellings-2026-11-15.md` §6), 1738's misprints Exod 3:7
    *Aegyto* and 28:19 *e* for *et* (kept, decision 58), words run together (*verbafacit*, Gen 24:34;
    *successitHusamus*, 36:34), and 21 next words in lower case after a colon (*coleret: et*).
  - Three readings stayed uncertain after two readers (Gen 18:28 *ille)*, 42:32 *iam*, 47:30 *tu*): each takes the
    reading both gave, with a note on its row.
- The open questions at the end of each review file (accents, summaries, Castellio's G. … H. marks, capitals of
  unread words) are as for the New Testament.

## For the reading edition

Readings that differ from the settled text by more than spelling. Four are already decided (decision 52, kept against
1738): Gen 3:14 *cicurum* (1738 *cicurarum*), 9:3 *adhibētōte* (*adhibitote*), 13:8 *discidium* (*dissidium*),
25:14 *Masma* (*Masina*). The new ones:

1. **Gen 18:6** *eā depstā pānēs depstīnōs* → 1738 (leaf 76) *ea depsita panes depsititios* (corrected
   2026-11-14: first cited here as *depstitios*; the page, read again, has *depſititios*). 1554 (MDZ bsb10196330,
   image 87) and 1573 (image 34) print the same, by their OCR: Castellio's own word is *depsititius*, made on his
   participle *depsitus* (*depsita*), with *ti* for *ci*. The classical forms are *depstus* (Gaffiot *depsō,
   depstum*) and *depstīcius* "kneaded" (Gaffiot *depstīcĭus*; Cato 74 *panem depsticium*), and Castellio writes
   *depsticium* himself in the *Dialogi sacri* (1551). *depstīnus* is in no lexicon here (Wikisource *depstinos*,
   the settled text's source). Recommended: *depstīciōs*, the classical form of his word, as the settled text
   already has *depstā* for his *depsita*.
   **Apply:** `Gen.18.6` la: `pānēs depstīnōs cōnficiat` → `pānēs depstīciōs cōnficiat`
2. **Gen 43:29** *dē quō mihi locūtīs fuistis?* → 1738 (leaf 106) *locuti fuistis*, and your 1726 text (TXT/3)
   *locuti*; Wikisource *locutis*. A slip in Wikisource that the settled text took. Recommended.
   **Apply:** `Gen.43.29` la: `mihi locūtīs fuistis` → `mihi locūtī fuistis`
3. **Exod 18:5** *Cum hīs ad Mōsem pervēnit* → 1738 (leaf 132) *Cumque his ad Mosem peruenit*; Wikisource and 1726
   (TXT/1 OCR *cum his*, TXT/3 *Cum his*) *Cum*; not found in 1750's OCR. **Checked in the earlier prints
   (2026-11-14, your request):** Castellio's own 1554 (MDZ bsb10196330, image 51) and 1573 (bsb10141277, image 70)
   both print *Cum his ad Mosem peruenit*, seen on the page images. *Cumque* is 1738's alone (a later printing's
   addition); the settled *Cum* stands. The printed text keeps 1738's *Cumque*. No Apply line.
4. **Exod 20:24** *Sed mihi cæspitum altāre fīat* → 1738 (leaf 134) *cæspitium*; the 1726 OCR (TXT/1) *caspicium*
   (æ read as a, t as c); your 1726 edited text (TXT/3) *caespititium*; Wikisource *caespitum*. **Checked in the
   earlier prints (2026-11-14, your request):** 1554 (image 52) *cespitium*, 1573 (image 71) *cæſpitium*, seen on
   the page images. Every printing from Castellio's own revision on has the word, so it is not a misprint (the
   haplography first suggested here is ruled out): it is Castellio's adjective *cæspitius* "of turf", from *cæspes*
   as his *appositītius*, *exceptītius* from participles, not in the lexicons (Gaffiot and Lewis & Short have only
   the post-classical *cæspiticius*). Wikisource's *cæspitum* is its slip. Marked as *cæspes, cæspitis*: no long
   vowel. Accepted on this evidence (Nathan asked for the prints to decide).
   **Apply:** `Exod.20.24` la: `mihi cæspitum altāre` → `mihi cæspitium altāre`
5. **Exod 6:22** *Sethris* → 1738 (leaf 120) *Setheris*; Wikisource, 1726 *Sethris*. Hebrew *Sithri*. Kept
   (recommended): two printings, closer to the Hebrew. No Apply line.
6. **Exod 15:6** *decus tibi fortissimē peperistī* → 1738 (leaf 129) *fortissimi*; Wikisource, 1726 *fortissime*.
   Kept (recommended): the vocative with *ō Jova*. No Apply line.
7. **Exod 12:11** 1738 prints *tententes* for *tenentes* (leaf 125): a misprint, kept in the printed text only.

**Decision:** accept 1, 2, 4 (Nathan, 2026-11-14: his recommendations, with 3 and 4 decided by the earlier prints; 5, 6 kept)
