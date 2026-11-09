# Luke 14–24, stage 2: Wikisource against the printings

Proposed 2026-11-08. Stage 1 made **`text/draft/LUK.usfm`**: Wikisource's text for these chapters (KJV numbering;
all 11 chapters at the KJV count, 491 verses), with a paragraph wherever the BSB opens one. It was collated word by
word against 1573, 1556, 1758, 1681, 1715, 1747 and 1750 (`python -m pipeline collate Luke 14-24`;
`data/calibration/Luke14-24-collation.tsv`). Of the places where some witness differs, the 37 where 1573 and
another printing agree against Wikisource were each judged; the 386 where only 1573's OCR differs were all
scanned, and the five that looked like real words were read on the image (three proved real: 16:17, 17:8, 22:19;
19:22 *seuerum* and 23:15 *misi* were misreadings). The rest of the 37 are spellings the rules handle (*quicunque*,
*nunquam*, *quotidie*, *charissimum*, *monimentum*), OCR noise, or forms kept by decision (14:21 *iit*, 22:66 *coiit*,
19:7 *īsset*: decision 26; 20:46 *accubitiōnēs*: decision 18).

**Every item below was read on the 1573 page image** (canvas given; crops in `sources/mdz-1573/crops/`). Each
**Apply** line is an exact replacement in `text/draft/LUK.usfm`, checked to match once.

## 1. Wikisource slips: 1573 and the other printings agree against it (17)

**Decision:** accept (Claude, delegated by Nathan, 2026-11-08: needed before stages 3–5; every item read on the image)

1. **Luke 14:3** *juris peritos* → *legis peritos*. 1573 *legiſperitos* (canvas 803); 1758, 1681. As your Luke
   10–11 fixes (*lēgis perītus*, `settled-fixes.md`).
   **Apply:** `Luke.14.3` la: `juris peritos` → `legis peritos`
2. **Luke 14:28** *en habeat* → *an habeat* ("whether he has"). 1573 *an habeat* (803); 1758, 1750.
   **Apply:** `Luke.14.28` la: `en habeat` → `an habeat`
3. **Luke 14:31** *qui secum viginti* → *qui se cum viginti* ("who attacks him with twenty thousand"). 1573 *qui ſe
   cum viginti* (803); 1758, 1750, 1681, 1715.
   **Apply:** `Luke.14.31` la: `qui secum viginti` → `qui se cum viginti`
4. **Luke 14:32** *Alioqui* → *Alioquin*. 1573 *Alioquin* (803); 1758, 1715, 1747, 1750. Your settled chapters have
   neither form.
   **Apply:** `Luke.14.32` la: `Alioqui adhuc` → `Alioquin adhuc`
5. **Luke 14:33** *valedicit* → *vale dicit*. 1573 *vale dicit* (803); 1715, 1747, 1750; as Mark 6:46 *valē dīxit*.
   **Apply:** `Luke.14.33` la: `valedicit` → `vale dicit`
6. **Luke 15:20** *miseritus* → *misertus*. 1573 *miſertus* (804); 1758, 1715. Both are classical participles of
   *misereor*; the base edition's is proposed (decision 24). **Variant recorded, not proposed:** 1573 *inſilijt*
   (*insiliit*) for *insiluit* (Gaffiot *insiluī*; decision 19 leaves *insiliō* out of the *-īv-* rule).
   **Apply:** `Luke.15.20` la: `miseritus` → `misertus`
7. **Luke 15:29** *ne umquam* → *nec umquam*. 1573 *nec vnquam* (804); 1758, 1715, 1747, 1750.
   **Apply:** `Luke.15.29` la: `ne umquam` → `nec umquam`
8. **Luke 16:17** *interdicere* → *intercidere* ("than one tittle of the law to fail"). 1573 *intercidere* (805);
   1556, 1758.
   **Apply:** `Luke.16.17` la: `interdicere` → `intercidere`
9. **Luke 16:30** *si qui a mortuis* → *si quis*. 1573 *ſi quis* (805); 1556, 1758, 1747, 1750.
   **Apply:** `Luke.16.30` la: `si qui a` → `si quis a`
10. **Luke 17:8** *Para quod ego cenam* → *cenem* (the subjunctive: "prepare what I may dine on"). 1573 *cœnē*,
    i.e. *cœnem* (805); 1556 *coene*.
    **Apply:** `Luke.17.8` la: `quod ego cenam` → `quod ego cenem`
11. **Luke 19:8** *dimidium facultatem* → *facultatum*. 1573 *facultatum* (807); 1715, 1750.
    **Apply:** `Luke.19.8` la: `facultatem` → `facultatum`
12. **Luke 21:20** *tu scitote* → *tum scitote*. 1573 *tum ſcitote* (809); 1758, 1747, 1750.
    **Apply:** `Luke.21.20` la: `tu scitote` → `tum scitote`
13. **Luke 22:12** *Atque ille cenaculum* → *Atque ille vobis cenaculum* (a word missing). 1573 *Atq; ille vobis
    cœnaculum* (810); 1758, 1681, 1750.
    **Apply:** `Luke.22.12` la: `Atque ille cenaculum` → `Atque ille vobis cenaculum`
14. **Luke 22:19** *iisque dicens* → *iisque dedit, dicens* (a word missing). 1573 *eiſque dedit, dicēs* (810); 1758,
    1747, 1750.
    **Apply:** `Luke.22.19` la: `iisque dicens` → `iisque dedit, dicens`
15. **Luke 23:19** *caedam* → *caedem*. 1573 *cædem* (811); 1758, 1747, 1750.
    **Apply:** `Luke.23.19` la: `caedam` → `caedem`
16. **Luke 24:41** *aliquid edule* → *aliquid edulii* (partitive genitive). 1573 *aliquid edulij* (812); 1556, 1758,
    1750.
    **Apply:** `Luke.24.41` la: `aliquid edule` → `aliquid edulii`
17. **Luke 16:1** *dives dispensatore habebat* → *dispensatorem* (the object of *habēbat*). 1573 *diſpenſatorē*, the
    tilde for *m* (canvas 804, page image); 1758, 1747, 1750 *dispensatorem*. 1573's OCR lost the tilde, so the
    collation counted it with Wikisource; found while placing the quotation marks. Added 2026-11-08.
    **Apply:** `Luke.16.1` la: `dives dispensatore habebat` → `dives dispensatorem habebat`
