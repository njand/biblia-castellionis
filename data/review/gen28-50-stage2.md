# Genesis 28–50, stages 1–2: Wikisource against 1738, 1750 and your 1726–27 text

Proposed 2026-11-08 (decision 30's standing rule). The Old Testament route, new for this run:

- **Base**: the 1738 Leipzig edition (decision 1), which Wikisource transcribes. Stage 1 drafted Wikisource's
  Genesis 28–50 as **`text/draft/GEN.usfm`** (BSB paragraphs), as for the Gospels.
- **Versification** (decision 5): six edits in `data/versification/Gen.draft.edits.tsv`, applied: splits at 38:6
  (*Sed Er Jovæ*), 43:27 (*Illī suppliciter*) and 44:27 (*alterum*), each where your 1726 text already divides;
  merges 48:21–22 and 49:31–32 (the KJV's one verse each); and **41:57 recorded as absent**: 1738, 1750, Wikisource
  and your text all end chapter 41 at 41:56 *dīvendere*, whose *urgente per omnem terram famē* carries the KJV
  41:57's sense. Chapter 41 keeps 56 verses (a new `absent` edit, so the check knows); every other chapter is at
  the KJV count. 757 verses.
- **Collation** (`python -m pipeline collate Gen 28-50`, `data/calibration/Gen28-50-collation.tsv`): the collation
  now takes 1738 as the Old Testament base, with 1750 and **your `TXT/3 - Edited` text (the 1726–27 edition, corrected
  by hand) as witnesses**. Wikisource's Genesis is rougher than its Gospels: of the places where 1738 and another
  witness agree against it, or 1750 and your text do, 33 are real (below); the rest are OCR noise in the base, word
  division, or spellings the rules handle. The 1,322 places where only 1738's OCR differs were filtered for real
  words and read: one is real (30:2).
- **Page images**: 1738's archive.org scan. The hOCR (fetched with `fetch archive 1738 --hocr`) places each word;
  `pipeline/archive.py` now finds a word on the page and crops its lines from archive.org's page image (crops in
  `sources/archive/crops/`; leaf given). 30 items were read there. For 3 (40:19, 42:33, 48:7) the crop found
  another verse, so they rest on the printings' OCR, as marked.
- **In all, 61 corrections**: 33 from the collation (section 1), 8 misspellings no lexicon knows (2), and 20 found
  while reading the verses for layout and macrons (3–4), checked in 1738. Your 1726 text shares several of
  Wikisource's slips in chapters 30–35, so for those only 1738 counts.

## 1. Wikisource slips (33)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

1. **Gen 30:2** *fetu prohibit* → *prohibet*. 1738 *fetu prohibet* (leaf 90, page image).
   **Apply:** `Gen.30.2` la: `fetu prohibit` → `fetu prohibet`
2. **Gen 36:21** *Seitis filii* → *Seiris* (of Seir). 1738 *Seiris filii* (97, page image); your 1726.
   **Apply:** `Gen.36.21` la: `Seitis filii` → `Seiris filii`
3. **Gen 37:10** *reulisset* → *retulisset*. 1738 *retulisſet* (98, page image); 1750, your 1726.
   **Apply:** `Gen.37.10` la: `reulisset` → `retulisset`
4. **Gen 38:13** *Quae res et nuntiata* → *ut*. 1738 *Quæ res vt nuntiata* (100, page image); 1750, your 1726.
   **Apply:** `Gen.38.13` la: `Quae res et nuntiata` → `Quae res ut nuntiata`
5. **Gen 39:3** *quum animadvertere herus* → *animadverteret*. 1738 *animaduerteret herus* (101, page image); 1750,
   your 1726.
   **Apply:** `Gen.39.3` la: `quum animadvertere herus` → `quum animadverteret herus`
6. **Gen 40:19** *et palum adfigeris* → *et ad palum* (a word missing). 1750 and your 1726 *ad palum* (OCR); 1738's
   crop found 40:22 instead.
   **Apply:** `Gen.40.19` la: `et palum adfigeris` → `et ad palum adfigeris`
7. **Gen 41:21** *ahuc* → *adhuc*. 1738 *adhuc* (103, page image); 1750, your 1726.
   **Apply:** `Gen.41.21` la: `ahuc` → `adhuc`
8. **Gen 41:27** *fames videbit* → *vigebit*. 1738 *fames vigebit* (103, page image); your 1726.
   **Apply:** `Gen.41.27` la: `fames videbit` → `fames vigebit`
9. **Gen 41:47** *tot Aegyptum obiit* → *totam*. 1738 *totam Aegyptum obiit* (103, page image); 1750, your 1726.
   **Apply:** `Gen.41.47` la: `tot Aegyptum` → `totam Aegyptum`
10. **Gen 41:50** *annonae penuriat est* → *penuria*. 1738 *pe-|nuria eſt* (104, page image); 1750, your 1726.
    **Apply:** `Gen.41.50` la: `penuriat est` → `penuria est`
11. **Gen 42:16** *fratrem vestrum arcessar* → *arcessat*. 1738 *arceſ-|ſat* (104, page image); 1750 *accerſat*, your
    1726.
    **Apply:** `Gen.42.16` la: `vestrum arcessar` → `vestrum arcessat`
12. **Gen 42:33** *eos veraces, si* → *eos veraces esse, si* (a word missing). 1738, 1750 and your 1726 *eſſe* (OCR);
    the crop found 45:27.
    **Apply:** `Gen.42.33` la: `eos veraces, si` → `eos veraces esse, si`
13. **Gen 42:38** *cui si quo infortunium* → *quod*. 1738 *cui ſi quod infortunium* (105, page image); 1750, your 1726.
    **Apply:** `Gen.42.38` la: `si quo infortunium` → `si quod infortunium`
14. **Gen 43:8** *et parvulis nostis* → *nostris*. 1738 *paruulis noſtris* (105, page image); 1750, your 1726.
    **Apply:** `Gen.43.8` la: `parvulis nostis` → `parvulis nostris`
15. **Gen 43:11** *ferte, aromatat et* → *aromata*. 1738 *ferte, aro-|mata et ſtacten* (106, page image); 1750, your 1726.
    **Apply:** `Gen.43.11` la: `aromatat et` → `aromata et`
16. **Gen 44:11** *deponnut* → *deponunt*. 1738 *deponunt* (107, page image); 1750, your 1726.
    **Apply:** `Gen.44.11` la: `deponnut` → `deponunt`
17. **Gen 44:12** *in sacco Benjamini* → *Benjaminis*. 1738 *ſacco Beniaminis* (107, page image); 1750, your 1726.
    **Apply:** `Gen.44.12` la: `sacco Benjamini invenit` → `sacco Benjaminis invenit`
18. **Gen 44:24** *tua illa verba* → *tua illi verba* (we told him your words). 1738 *tua illi verba* (107, page
    image); 1750, your 1726.
    **Apply:** `Gen.44.24` la: `tua illa verba` → `tua illi verba`
19. **Gen 44:30** *Nun si veniam* → *Nunc*. 1738 *Nunc ſi* (107, page image); 1750, your 1726.
    **Apply:** `Gen.44.30` la: `Nun si veniam` → `Nunc si veniam`
20. **Gen 45:3** *fratres ejus adhuc praesentia* → *fratres ejus praesentia* (a word Wikisource adds). 1738 *at fratres
    eius præſentia conturbati* (108, page image); 1750, your 1726.
    **Apply:** `Gen.45.3` la: `ejus adhuc praesentia` → `ejus praesentia`
21. **Gen 45:9** *cui Deus dominum* → *dominium*. 1738 *cui Deus dominium in omnes* (108, page image); 1750.
    **Apply:** `Gen.45.9` la: `Deus dominum in` → `Deus dominium in`
22. **Gen 45:19** *copiam faciat, et impositus* → *copiam faciat, quibus parvuli et mulieres vehantur, et impositus*
    (a clause missing). 1738 *quibus paruuli et mulieres vehantur* (108, page image); 1750, your 1726.
    **Apply:** `Gen.45.19` la: `copiam faciat, et impositus` → `copiam faciat, quibus parvuli et mulieres vehantur, et impositus`
23. **Gen 45:27** *vehendum consciperet* → *conspiceret*. 1738 *vehendum conſpiceret* (109, page image); 1750, your 1726.
    **Apply:** `Gen.45.27` la: `consciperet` → `conspiceret`
24. **Gen 46:1** *Israrel* → *Israel*. 1738 *Iſrael* (109, page image); 1750, your 1726.
    **Apply:** `Gen.46.1` la: `Israrel` → `Israel`
25. **Gen 46:22** *Hos Jacobus filios ex Rachele* → *filios habuit ex Rachele* (a word missing). 1738 *filios habuit
    ex Rache-|le* (109, page image); 1750, your 1726.
    **Apply:** `Gen.46.22` la: `filios ex Rachele` → `filios habuit ex Rachele`
26. **Gen 47:4** *ut sibi servis liceret* → *ut sibi ejus servis* (a word missing). 1738 *vt ſibi eius ſeruis* (110,
    page image); 1750, your 1726.
    **Apply:** `Gen.47.4` la: `sibi servis liceret` → `sibi ejus servis liceret`
27. **Gen 47:18** *pecunia, sibi* → *pecunia et pecore, sibi* (words missing). 1738 *pecunia et pecore, ſibi* (110,
    page image); 1750, your 1726.
    **Apply:** `Gen.47.18` la: `eum pecunia, sibi` → `eum pecunia et pecore, sibi`
28. **Gen 47:25** *in Pharaoni potestate* → *Pharaonis*. 1738 *in Pharaonis poteſtate* (111, page image); 1750, your 1726.
    **Apply:** `Gen.47.25` la: `in Pharaoni potestate` → `in Pharaonis potestate`
29. **Gen 48:7** *ex Mesopotamis venienti* → *ex Mesopotamia*. 1750 and your 1726 *Meſopotamia* (OCR); the crop found
    46:15.
    **Apply:** `Gen.48.7` la: `ex Mesopotamis venienti` → `ex Mesopotamia venienti`
30. **Gen 48:14** *natu grandiot* → *grandior*. 1738 *natu grandior* (112, page image); 1750, your 1726.
    **Apply:** `Gen.48.14` la: `natu grandiot` → `natu grandior`
31. **Gen 48:18** *hic grandiot est* → *grandior*. 1738 *nam hic gran-|dior eſt* (112, page image); 1750, your 1726.
    **Apply:** `Gen.48.18` la: `hic grandiot est` → `hic grandior est`
32. **Gen 49:15** *amoenitate perfeca* → *perfecta*. 1738 *amœnitate perfecta* (113, page image); 1750, your 1726.
    **Apply:** `Gen.49.15` la: `amoenitate perfeca` → `amoenitate perfecta`
33. **Gen 49:28** *atque haec snut* → *sunt*. 1738 *atque hæc ſunt* (113, page image); 1750, your 1726.
    **Apply:** `Gen.49.28` la: `haec snut` → `haec sunt`

## 2. Wikisource misspellings found while marking (8)

Words no lexicon knows, found in the stage-4 list of unknown words; the collation's spelling-blind comparison had
folded them away (double letters, f for s). Evidence: your 1726 text, and 1738's OCR where it reaches the word.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

34. **Gen 36:15** *filiiorum* → *filiorum*. Your 1726 *Esai filiorum duces*.
    **Apply:** `Gen.36.15` la: `filiiorum` → `filiorum`
35. **Gen 37:7** *venerebantur* → *venerabantur*. Your 1726 *circumdantes venerabantur*.
    **Apply:** `Gen.37.7` la: `venerebantur` → `venerabantur`
36. **Gen 38:3** *filiu* → *filium*. 1738 *filium* (OCR), 1750 *filium*.
    **Apply:** `Gen.38.3` la: `congressu filiu` → `congressu filium`
37. **Gen 38:11** *dommi* → *domi*. Your 1726 *viduam domi paternæ*.
    **Apply:** `Gen.38.11` la: `viduam dommi` → `viduam domi`
38. **Gen 39:23** *propserabat* → *prosperabat*. Your 1726 *facta prosperabat*.
    **Apply:** `Gen.39.23` la: `propserabat` → `prosperabat`
39. **Gen 44:22** *ab eo deferi* → *deseri* (the long s read as f). Your 1726 *patrem ab eo deseri non posse*.
    **Apply:** `Gen.44.22` la: `ab eo deferi` → `ab eo deseri`
40. **Gen 45:1** *praresentes* → *praesentes*. 1738 *præſentes* (OCR).
    **Apply:** `Gen.45.1` la: `praresentes` → `praesentes`
41. **Gen 47:3** *quarenti* → *quaerenti*. 1738 *quærenti* (OCR).
    **Apply:** `Gen.47.3` la: `quarenti` → `quaerenti`

## 3. Found while placing the layout (3)

Suspected by the layout reading (Genesis 28–33) and checked on the 1738 page image. Your 1726 text has the same
slips (its OCR followed the same misreadings or Wikisource's), so it is no evidence here. Kept after checking:
33:2 *cum suīs utrāsque nātīs* (1738 *vtrasque*, leaf 94) and 33:19 *quessitis* (Castellio's word for the Hebrew
*qesitah*).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

42. **Gen 30:1** *invidiam in sororem permota* → *invidia* ("moved by envy"). 1738 *inuidia in ſororem permota*
    (leaf 89, page image).
    **Apply:** `Gen.30.1` la: `videret, invidiam in` → `videret, invidia in`
43. **Gen 32:10** *imparsum* → *impar sum* ("I am unworthy"). 1738 and 1750 *impar ſum* (OCR).
    **Apply:** `Gen.32.10` la: `imparsum` → `impar sum`
44. **Gen 32:32** *Ex eo sit, ut* → *Ex eo fit, ut*. 1738 *Ex eo fit* (leaf 94, page image).
    **Apply:** `Gen.32.32` la: `Ex eo sit,` → `Ex eo fit,`

## 4. Found by the layout readings of chapters 34–50 (17)

Suspected by the layout and macron readings (Genesis 34–50) and checked in 1738: on the page image where cited
(`sources/archive/crops/`), otherwise in its OCR. Your 1726 text shares the slips at 34:23, 35:3, 35:8, 35:23, so it
is no evidence there. Kept after checking: 37:35 *cumque pater deplorans* (1738 prints *cumque*, leaf 99, page
image; 1750 and your 1726 have *eumque*); 43:23 *ad se pervenisse* (1738 *ad ſe*; your 1726 *ad sese*).

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

45. **Gen 34:23** *Hoc paco* → *pacto*. 1738 *Hoc pacto* (leaf 95, page image).
    **Apply:** `Gen.34.23` la: `Hoc paco` → `Hoc pacto`
46. **Gen 35:3** *in sua itinere* → *suo*. 1738 *in ſuo itinere* (leaf 96, page image).
    **Apply:** `Gen.35.3` la: `in sua itinere` → `in suo itinere`
47. **Gen 35:8** *nutix* → *nutrix*. 1738 *Rebeccæ nutrix Debora* (leaf 96, page image).
    **Apply:** `Gen.35.8` la: `nutix` → `nutrix`
48. **Gen 35:23** *ludam* → *Judam* (I read as l). 1738 *Iudam* (leaf 97, page image).
    **Apply:** `Gen.35.23` la: `Levim, ludam` → `Levim, Judam`
49. **Gen 36:5** *in Chananea* → *Chananaea*. 1738 *in Chananæa* (leaf 97, page image); your 1726 *Chananæa*.
    **Apply:** `Gen.36.5` la: `procreavit in Chananea` → `procreavit in Chananaea`
50. **Gen 38:12** *ovium surarum* → *suarum*. 1738 *ſuarum* (OCR); your 1726 *ovium suarum*.
    **Apply:** `Gen.38.12` la: `ovium surarum` → `ovium suarum`
51. **Gen 41:55** *ilius dicto* → *illius*. 1738 *il lius* and 1750 *illius* (OCR); your 1726 *illius*.
    **Apply:** `Gen.41.55` la: `jubens, ilius` → `jubens, illius`
52. **Gen 42:24** *digressus ab illius flevit* → *ab illis*. 1738 *illis* (OCR); your 1726 *Digressus ab illis*.
    **Apply:** `Gen.42.24` la: `ab illius flevit` → `ab illis flevit`
53. **Gen 43:23** *Simonem* → *Simeonem*. 1738 *Simeonem* (OCR, leaf 106); your 1726 *Simeonem*.
    **Apply:** `Gen.43.23` la: `Tum ad eos Simonem` → `Tum ad eos Simeonem`
54. **Gen 43:25** *Ille autem munus adornant* → *Illi* (the verb is plural). 1738 *Illi au-tem* (leaf 106, page
    image); 1750 and your 1726 *Illi*.
    **Apply:** `Gen.43.25` la: `Ille autem munus` → `Illi autem munus`
55. **Gen 44:6** *G.* … *H.*: Castellio's marks for words from the Greek “until the return to the Hebrew” (his
    *Ad lectores admonitio*; `docs/editions.md`). 1738 prints *G.* (leaf 107, page image) and *H.* (OCR *if.*);
    your 1726 omits them. The settled chapters keep such words and drop the marks (Matt 19:4, Luke 11:7), so the
    marks go and *cur sibi scyphum argenteum furati sint* stays.
    **Apply:** `Gen.44.6` la: `pensarint? G. cur` → `pensarint? cur`
    **Apply:** `Gen.44.6` la: `sint? H. eum` → `sint? eum`
56. **Gen 45:25** *Jacobun* → *Jacobum*. 1738 *Iacobum* (OCR *la- cobum*, leaf 105); your 1726 *Jacobum*.
    **Apply:** `Gen.45.25` la: `Jacobun` → `Jacobum`
57. **Gen 46:13** *Tholam Phuvam* → *Tholam, Phuvam*. 1738 has a mark after *Tholam* (OCR *Thok.'r.,*); your 1726
    *Tholam, Phuuam*.
    **Apply:** `Gen.46.13` la: `Tholam Phuvam` → `Tholam, Phuvam`
58. **Gen 47:13** *languerent.* → *languerent,* (the sentence runs on into 47:14 *Coegit Josephus*). Your 1726
    *languerent,*; 1738 not read here.
    **Apply:** `Gen.47.13` la: `languerent.` → `languerent,`
59. **Gen 48:6** *in tendenda hereditate* → *tenenda*. 1738 *in tenenda hereditate* (OCR); your 1726 *tenenda*.
    **Apply:** `Gen.48.6` la: `tendenda` → `tenenda`
60. **Gen 49:20** *ciborum lautorum feras* → *ferax*. 1738 *ferax* (OCR *fcrax*); your 1726 *ferax*.
    **Apply:** `Gen.49.20` la: `lautorum feras` → `lautorum ferax`
61. **Gen 50:16** *cum certiorem faciunt* → *eum* (“they inform him”). 1738 *eum* (leaf 114, page image); your 1726
    *Eum*.
    **Apply:** `Gen.50.16` la: `cum certiorem` → `eum certiorem`
