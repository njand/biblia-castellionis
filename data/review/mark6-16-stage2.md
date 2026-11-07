# Mark 6–16, stage 2: Wikisource against the printings

Proposed 2026-11-07 (overnight run). Mark 6–16 had no draft, so stage 1 made one:
**`text/draft/MRK.usfm`** is Wikisource's text for these chapters (KJV numbering, which Wikisource's Gospels
follow), with a paragraph wherever the BSB opens one (`collate.draft_usfm`). It has no macrons, no quotation
marks, no `\qt` or poetry yet, and Wikisource's spelling (*ae*, *coepit*): stages 3–5 are still to come (see
MORNING.md). It was collated word by word against 1573, 1556, 1758, 1681, 1715, 1747 and 1750, as Matthew was.
Of 3,441 places where some witness differs, 2,796 are one OCR's misreading and 463 1573's OCR alone (read where
they looked real: they were not).

Each **Apply** line is an exact replacement inside that verse of `text/draft/MRK.usfm`, checked to match once.
Where the line below says *page image*, the place was read on the 1573 image (canvas given); where it says
*OCR*, 1573's own OCR reads it clearly and the other printings named agree, so no crop was needed.

## 1. Wikisource slips: 1573 and the other printings agree against it (22)

**Decision:** accept (Nathan, 2026-11-07)

1. **Mark 6:27** *res speculatorem* → *rex spiculatorem*. 1573 *rex ſpiculatorem* (canvas 779, page image); 1758, 1715, 1747, 1750 *rex spiculatorem*.
   **Apply:** `Mark.6.27` la: `res speculatorem` → `rex spiculatorem`
2. **Mark 6:32** *Ita* → *Itaque*. 1573 *Itaque diſceſsit* (779, page image); 1758.
   **Apply:** `Mark.6.32` la: `\v 32 Ita discessit` → `\v 32 Itaque discessit`
3. **Mark 7:37** *fecisse, ut surdi* → *fecisse, et ut surdi*. 1573 *feciſſe, & vt ſurdi audirent, & vt muti* (780, page image); 1715, 1747, 1750 (1758 as Wikisource).
   **Apply:** `Mark.7.37` la: `fecisse, ut surdi` → `fecisse, et ut surdi`
4. **Mark 8:4** *sic responderunt* → *sic ei responderunt*. 1573 *ſic ei reſponderunt* (780, page image); 1758, 1750.
   **Apply:** `Mark.8.4` la: `sic responderunt` → `sic ei responderunt`
5. **Mark 8:25** *oculis manu imposuit* → *manus*. 1573 *oculis manus impoſuit* (781, page image); 1758, 1715, 1747, 1750.
   **Apply:** `Mark.8.25` la: `oculis manu imposuit` → `oculis manus imposuit`
6. **Mark 9:18** *laceret* → *lacerat*. 1573 *ita lacerat, vt ſpumet* (781, page image; 1573 numbers it 17); 1556, 1758, 1681, 1715.
   **Apply:** `Mark.9.18` la: `ita laceret` → `ita lacerat`
7. **Mark 9:50** *insultum* → *insulsum* (“if the salt have lost his saltness”). 1573 *ſi ſal inſulſum fiat* (782, page image; numbered 49); 1758, 1715, 1747, 1750.
   **Apply:** `Mark.9.50` la: `sal insultum fiat` → `sal insulsum fiat`
8. **Mark 10:24** *alloquitur: Nati* → *alloquitur: O nati*. 1573 *ſic eos alloquitur: ô nati* (783, page image); 1758 *O*.
   **Apply:** `Mark.10.24` la: `alloquitur: Nati` → `alloquitur: O nati`
9. **Mark 10:26** *si secum* → *sic secum*. 1573 *ſic ſecum ipſi cogitantes* (783, page image); 1758, 1750.
   **Apply:** `Mark.10.26` la: `stuperent, si secum` → `stuperent, sic secum`
10. **Mark 10:38** *poturus* → *potaturus*. 1573 *quod ego potaturus ſum* (783, page image); 1758, 1715, 1750.
    **Apply:** `Mark.10.38` la: `ego poturus sum` → `ego potaturus sum`
11. **Mark 10:39** *poturus* → *potaturus*. 1573 (OCR), 1758, 1715, 1747, 1750.
    **Apply:** `Mark.10.39` la: `ego poturus sum` → `ego potaturus sum`
12. **Mark 10:46** *mendicabant* → *mendicabat* (one blind man). 1573 (OCR), 1758.
    **Apply:** `Mark.10.46` la: `sedens mendicabant` → `sedens mendicabat`
13. **Mark 11:25** *agnoscite* → *ignoscite* (“forgive”). 1573 *ignoſcite* (OCR), 1747, 1758.
    **Apply:** `Mark.11.25` la: `autem agnoscite` → `autem ignoscite`
14. **Mark 13:8** *dolorum principis* → *principia* (“the beginnings of sorrows”). 1573 (OCR), 1758.
    **Apply:** `Mark.13.8` la: `dolorum principis` → `dolorum principia`
15. **Mark 13:11** *loquimini* → *loquemini* (future: “it is not ye that speak” in the sense “shall speak”). 1573 (OCR), 1715.
    **Apply:** `Mark.13.11` la: `qui loquimini` → `qui loquemini`
16. **Mark 13:20** *electos, quod delegit* → *quos*. 1573 *propter electos, quos delegit* (785, page image); 1556, 1758, 1715, 1747, 1750.
    **Apply:** `Mark.13.20` la: `electos, quod delegit` → `electos, quos delegit`
17. **Mark 14:13** *sequemini* → *sequimini* (imperative). 1573 (OCR), 1758, 1715, 1750.
    **Apply:** `Mark.14.13` la: `eum sequemini` → `eum sequimini`
18. **Mark 14:40** *responderunt* → *responderent* (after *ut nescirent quid*). 1573 *quid ei reſponderent* (786, page image); 1758, 1747, 1750.
    **Apply:** `Mark.14.40` la: `quid ei responderunt` → `quid ei responderent`
19. **Mark 14:41** *venit horam* → *hora*. 1573 (OCR), 1556, 1758, 1747.
    **Apply:** `Mark.14.41` la: `venit horam` → `venit hora`
20. **Mark 14:46** *manu injecerunt* → *manus*. 1573 (OCR *manus*), 1758, 1715.
    **Apply:** `Mark.14.46` la: `in eum manu injecerunt` → `in eum manus injecerunt`
21. **Mark 14:52** *Ille viro relicto* → *Ille vero relicto*. 1573 *verò* (OCR), 1556, 1758.
    **Apply:** `Mark.14.52` la: `Ille viro relicto` → `Ille vero relicto`
22. **Mark 15:35** *eorum que aderant* → *qui*. 1573 *quidam eorum qui aderant* (787, page image); 1715, 1747.
    **Apply:** `Mark.15.35` la: `eorum que aderant` → `eorum qui aderant`

## 2. A word or form missing or different, not a slip (3)

**Decision:** accept 1, 2 (item 3: keep existis, by the corpus counts) (Nathan, 2026-11-07)

1. **Mark 15:46** *et monumenti ostium* → *et ad monumenti ostium* (“to the door of the sepulchre”). 1573 *& ad monimenti oſtium* (788, page image); 1556, 1747.
   **Apply:** `Mark.15.46` la: `erat: et monumenti ostium` → `erat: et ad monumenti ostium`
2. **Mark 16:8** *utpote quae metuerunt* → *metuerent* (subjunctive after *utpote quae*). 1573 *vtpote quæ metuerent* (788, page image); 1758.
   **Apply:** `Mark.16.8` la: `quae metuerunt` → `quae metuerent`
3. **Mark 14:48** *existis* → *exiistis*. 1573 *exijſtis* (OCR), 1556, 1758, 1747, 1750. A form (*exīstis*, the contracted perfect, is
   classical too), so your call under decision 19, which leaves the compounds of *eō* out of its rules.
   **Apply:** `Mark.14.48` la: `latronem existis` → `latronem exiistis`
   Corpus (republican era): compounds of *eō* have no *-iistis/-iistī/-iisse/-iissent* at all against *-īstī* 10, *-īsse* 92, *-īssent* 9; Cicero's 2nd persons are *redīstī, adīstī, transīstī*. Your settled Matt 11:8–9 has *exīstis* where 1573 prints *exijstis*. Full table in `matt14-28-spelling.md` group 6.

## 3. Not proposed

- **Mark 8:14** *Obliti autem erant*: 1573 reads as Wikisource (781, page image); 1556, 1715 and 1747 put
  *erant* after *Obliti* (the early line).
- **Mark 8:35**: 1715 and 1750's extra word is their OCR; the 1573 page has none (781, page image).
- **Mark 11:3**, **12:15**: 1573's OCR picked up a marginal note (*a adduci*) or the line above (*Licetne
  censum*), read on the page (783, 784): nothing to change.
- **Spellings** where 1573 differs (*spiculatorem* aside): *Bethphage* (11:1), *circundedit*, *myrrhinum* (15:23),
  *monimentum*, *iuit* (16:10): stage 3's business.
- **Early-line readings** in 1715, 1747 and 1750 where 1573 agrees with Wikisource (73 places, e.g. 9:31 and
  14:21 *homine natus* for *filius hominis*): Wikisource already follows the base.
