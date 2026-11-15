# Exodus 21–30, stages 1–2: Wikisource against 1738, 1750 and your 1726–27 text

Proposed 2026-11-14 (decision 30's standing rule), on the Old Testament route of Exodus 1–20
(`data/review/exod1-20-stage2.md`).

- **Base**: the 1738 Leipzig edition (decision 1). Stage 1 drafted Wikisource's Exodus 21–30 as
  **`text/draft/EXO.usfm`** (BSB paragraphs); 1738 is read from its hOCR, so every reading below names its leaf
  (the hOCR page; the archive.org image is one lower).
- **Versification** (decision 5): 1738's own verse numbers, which Wikisource keeps, are not the KJV's in chapters
  25, 26, 27, 28 and 30. 14 edits in `data/versification/Exod21-30.draft.edits.tsv` (the 18 for chapters 1–20 are kept
  as `Exod1-20.draft.edits.tsv`), applied; every chapter now has the KJV count (343 verses):
  - 25:11: Wikisource prints “10.” twice; the second is the KJV's 25:11 (*Eam puro auro*).
  - 26:25 (*His octo asseribus suberunt* + *argenteae spirae sexdecim, singulis binae*, 1738's 25–26) merged;
    1738's 26:27 (*cedrina repagula quina, ad duo tabernaculi latera: totidemque ad partem occidentalem*) split at
    *totidemque*, so the bars for the two sides are the KJV's 26:26 and those for the west its 26:27. (1738's
    26:20–21 also cut the KJV's 26:19–21 otherwise, *Videlicet singulas duas pro numero cardinum* being the end of
    KJV 26:19; the count agrees, so they are left.)
  - 27:17–21: Castellio cuts the court's last verses finer; his 17–18, 20–21, 22–23 and 24–26 are the KJV's 17, 19,
    20 and 21 (five merges).
  - 28:43: his 28:44 (*Atque hunc ritum … sempiternum tenento*) is the end of the KJV's 28:43.
  - 30: the KJV's 30:17 and 30:22 (*And the LORD spake unto Moses, saying*) are only an *inquit* inside his 30:18
    and *(inquit Jova Mosi)* inside his 30:23, so those verses are split where the KJV's next verse begins (*scapo
    aereo*, *myrrhae ingenuae*), as 1738 itself splits a sentence at 14:1–2; his 30:17, 30:22 and 30:37 end the
    KJV's 30:16, 30:21 and 30:36 (merged). 1738's numbers checked on leaf 145.
- **Collation** (`python -m pipeline collate Exod 21-30`, `data/calibration/Exod21-30-collation.tsv`): 1738 base;
  1750 and your `TXT/3 - Edited` text as witnesses. 38 “correct” places (another printing with 1738 against
  Wikisource): 26 are line-end divisions and OCR noise, 5 spellings for stage 3 (*caussa, paullatim, adferant,
  monimentum, adferto*), 7 readings (below). The 544 places where only 1738's OCR differs were filtered for real
  Latin words (`pipeline latin macron`): 97, of which 14 were read on the page and 6 differ (below). **The 41 verses
  1738's OCR covers under 60%** were read whole on the page images, each between the words paired around it: 9
  differ (below).
- **Kept after checking**: 23:1 *ut sis testis* (OCR *is*), 23:22 *quae jussero* (OCR *quas*), 24:5 *Israelitis*,
  26:29 *quae*, 28:26 *interius* (OCR *interim*), 29:46 *Haec ego Jova Deus eorum* (1738 leaf 144); punctuation
  that differs (21:3 *uxor cum eo*) is stage 5's.

**Applied to the draft** under decision 30's standing rule.

## 1. Wikisource slips and readings 1738 has otherwise (17)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-14)

1. **Exod 21:32** *sicli domino solvuntur* → *solvuntor* (the law's future imperative, as 23:17 *sistuntor*). 1738
   *soluuntor:* (leaf 135); 1750 the same.
    **Apply:** `Exod.21.32` la: `domino solvuntur` → `domino solvuntor`
2. **Exod 23:7** *Innocentem et justum ne interficito* → *Insontem*. 1738 *Insontem* (leaf 137); 1750 the same.
    **Apply:** `Exod.23.7` la: `Innocentem et justum` → `Insontem et justum`
3. **Exod 23:23** *angelus viam praebit* → *praeibit* (“will go before”). 1738 *præ-|ibit* (leaf 137).
    **Apply:** `Exod.23.23` la: `viam praebit` → `viam praeibit`
4. **Exod 24:12** *ab illo accipere tabulas* → *ab illoque accipere*. 1738 *ab illoque accipere* (leaf 138); 1750
   the same.
    **Apply:** `Exod.24.12` la: `ab illo accipere` → `ab illoque accipere`
5. **Exod 24:17** *splendor ad aspectu similis* → *splendor aspectu similis*. 1738 *adſpectu*, one word (leaf 138);
   Wikisource cut it in two.
    **Apply:** `Exod.24.17` la: `splendor ad aspectu similis` → `splendor aspectu similis`
6. **Exod 25:6** *ad suffimenta adorata* → *odorata* (sweet incense). 1738 *odora-|ta* (leaf 138).
    **Apply:** `Exod.25.6` la: `suffimenta adorata` → `suffimenta odorata`
7. **Exod 26:6** *quibus uncos lintea inter se connectes* → *quibus uncis*. 1738 *vncis* (leaf 139); 1750 the same.
    **Apply:** `Exod.26.6` la: `quibus uncos lintea` → `quibus uncis lintea`
8. **Exod 26:25** *Spirae argenteae sedecim* → *argenteae spirae sexdecim*. 1738 *argenteæ ſpiræ ſexdecim* (leaf
   140); 1750 *argenteac fpirae fexdecim* (OCR). The spelling of *sexdecim* is stage 3's.
    **Apply:** `Exod.26.25` la: `Spirae argenteae sedecim` → `argenteae spirae sexdecim`
9. **Exod 27:5** *ita collcato* → *collocato*. 1738 *collocato* (leaf 140); a typing slip.
    **Apply:** `Exod.27.5` la: `ita collcato` → `ita collocato`
10. **Exod 28:1** *qui mihi sacerdotis fungantur* → *sacerdotio* (*fungor* with the ablative). 1738 *ſacerdotio*
    (leaf 141); 1750 the same.
    **Apply:** `Exod.28.1` la: `mihi sacerdotis fungantur` → `mihi sacerdotio fungantur`
11. **Exod 28:4** *hae: Monila, ephodus* → *Monile* (the breastplate, as 28:15 *monile judiciale*). 1738 *monile*
    (leaf 141). The capital is stage 5's.
    **Apply:** `Exod.28.4` la: `Monila, ephodus` → `Monile, ephodus`
12. **Exod 28:18** *carbunculus, saphyrus et adamas* → *sapphirus*. 1738 *ſapphirus* (leaf 142).
    **Apply:** `Exod.28.18` la: `carbunculus, saphyrus` → `carbunculus, sapphirus`
13. **Exod 28:37** *vitta hyacinthina insulae infulae a fronte* → *infulae a fronte*. 1738 *infulæ a | fronte* (leaf
    142): Wikisource wrote the word twice, once with ſ read as s.
    **Apply:** `Exod.28.37` la: `hyacinthina insulae infulae` → `hyacinthina infulae`
14. **Exod 28:39** *bysso circuntexito* → *circumtexito*. 1738 *circumtexito* (leaf 142).
    **Apply:** `Exod.28.39` la: `bysso circuntexito` → `bysso circumtexito`
15. **Exod 29:4** *Deinde Aaronem* → *Aharonem*, the form of every other place. 1738 *Aharonem* (leaf 143).
    **Apply:** `Exod.29.4` la: `Deinde Aaronem` → `Deinde Aharonem`
16. **Exod 29:26** *idque Jovae porrigito* → *porricito* (*porriciō*, to offer the entrails; Gaffiot). 1738
    *porricito* (leaf 143).
    **Apply:** `Exod.29.26` la: `Jovae porrigito` → `Jovae porricito`
17. **Exod 30:24** *olei olivae hinem* → *olei olivi*. 1738 *olei oliui hinem* (leaf 145); 1750 the same.
    **Apply:** `Exod.30.24` la: `olei olivae hinem` → `olei olivi hinem`

## 2. Castellio's marks (1)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-14)

18. **Exod 28:34** *G.L. et bysso bilice H.*: 1738 prints *G. L.* … *H.* around *et bysso bilice* (leaf 142), the
    words his Greek and Latin sources add. The marks dropped, the words kept, as Exod 2:22 and 6:20.
    **Apply:** `Exod.28.34` la: `iterato, G.L. et bysso bilice H., et` → `iterato, et bysso bilice, et`

## 3. Found by the printed-text readings (stage 2b) (2)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-14)

19. **Exod 22:23** *Si premeris, quum ad me conquerentur* → *Si presseris* (“if thou afflict them”, as the law's
    perfect subjunctives around it). 1738 *Si preſſeris,* (leaf 136); 1750 *Si preferis* (OCR, a long s lost).
    **Apply:** `Exod.22.23` la: `Si premeris` → `Si presseris`
20. **Exod 29:24** *Jovae porrigito* → *porricito*, as 29:26. 1738 *Iouæ porricito:* (leaf 143).
    **Apply:** `Exod.29.24` la: `Jovae porrigito` → `Jovae porricito`

## 4. Found by the readers of stages 3–5 (13)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-14)

21. **Exod 21:25** *Sugilllationem* → *Sugillationem* (a triple l, Wikisource's typing slip). 1738 *ſugil-|lationem*
    (leaf 135).
    **Apply:** `Exod.21.25` la: `Sugilllationem` → `Sugillationem`
22. **Exod 22:5** *ēmissō pecore compaverit fundum* → *depaverit* (*dēpāscō*, “graze off”; *compāscō* has no
    perfect in Gaffiot). 1738 *emiſſo pecore, depa-|uerit* (leaf 136); your 1726 OCR (TXT/1) *com-|paverit*, as
    Wikisource: a difference between printings, the base's reading taken (decision 1); 1726 recorded as a variant.
    **Apply:** `Exod.22.5` la: `pecore compaverit` → `pecore depaverit`
23. **Exod 23:20** *in locum mē præparātum* → *in locum ā mē præparātum*. 1738 *in locum | a me præparatum* (leaf
    137): Wikisource lost the preposition.
    **Apply:** `Exod.23.20` la: `in locum me praeparatum` → `in locum a me praeparatum`
24. **Exod 23:23** *Hevaos* → *Hevaeos*, as 23:28. 1738 *Heuæos et Iebusæos* (leaf 137).
    **Apply:** `Exod.23.23` la: `Hevaos et` → `Hevaeos et`
25. **Exod 23:32** *foetus nē percutitō* → *foedus* (a covenant). 1738 *fœdus ne | percutito* (leaf 138); 1750 the
    same.
    **Apply:** `Exod.23.32` la: `foetus ne percutito` → `foedus ne percutito`
26. **Exod 25:10** a stray *10.* at the verse's end, left by the versification split of Wikisource's doubled number
    (25:11 begins *Eam puro auro*). 1738 prints *altitudinem, | Eam puro auro* (leaf 139).
    **Apply:** `Exod.25.10` la: `in altitudinem. 10.` → `in altitudinem.`
27. **Exod 25:23** *altitūdine sexquicubitālī* → *sesquicubitali*, as 25:10 and 25:17. 1738 *ſeſquicubitali* (leaf
    139).
    **Apply:** `Exod.25.23` la: `altitudine sexquicubitali` → `altitudine sesquicubitali`
28. **Exod 26:16** *lātitūdine sexquicubitālī* → *sesquicubitali*. 1738 *ſeſquicubitali* (leaf 140).
    **Apply:** `Exod.26.16` la: `latitudine sexquicubitali` → `latitudine sesquicubitali`
29. **Exod 30:33** *Quī tāle concinnāveris* → *concinnaverit* (third person, as *perfūderit*). 1738 *concinnauerit*
    (leaf 145).
    **Apply:** `Exod.30.33` la: `tale concinnaveris` → `tale concinnaverit`
30. **Exod 30:34** *sūmitō (inquit) statim, crocum* → *stacten* (στακτή, Vulgate *stacten*). 1738 *ſta-|cten* (leaf 145).
    **Apply:** `Exod.30.34` la: `(inquit) statim, crocum` → `(inquit) stacten, crocum`
31. **Exod 28:5** *et bystium adhibeant* → *byssum*. 1738 *byſſum* (leaf 141).
    **Apply:** `Exod.28.5` la: `et bystium adhibeant` → `et byssum adhibeant`
32. **Exod 28:28** *monile ā suīs annulōs ephodī* → *a suis annulis ad annulos ephodi* (Wikisource lost two words).
    1738 *a ſuis annulis ad | annulos ephodi* (leaf 142); 1750 *annulis ad*.
    **Apply:** `Exod.28.28` la: `a suis annulos ephodi` → `a suis annulis ad annulos ephodi`
33. **Exod 28:39** *et insulam byssinam* → *infulam* (the turban; ſ read for f). 1738 *infulam* (leaf 142; seen when
    the verse was read whole, section 1 item 14).
    **Apply:** `Exod.28.39` la: `et insulam byssinam` → `et infulam byssinam`
