# Proper names in the settled chapters

Proposed 2026-11-06 from the spelling review (`data/rules/REVIEW.md` §3, §5). Each **Apply** line is an exact
replacement inside that verse of `text/<BOOK>.usfm`, checked to match exactly once.

## 1. Enoch: *Henōchus* everywhere

Hebrew חֲנוֹךְ (OSHB, Gen 4:17, 5:18, 25:4, 46:9) begins with ḥet; Greek Ἑνὼχ (SBLGNT, Luke 3:37, Heb 11:5,
Jude 14) has the rough breathing; the Clementine Vulgate writes *Henoch* in both Testaments (*Enoch* only in
Jude). Castellio writes *Henochus* in the OT and *Enochus* in the NT (1556: *Enochi*, Luke 3:37; *Enochus*,
Heb 11:5). Gaffiot has *Henoch* and *Ēnōch*. Rules *Enoch- → Henoch-* approved in `orthography.tsv`.

**Decision:** Henōchus everywhere (Nathan, 2026-11-06; decision 21)  
**Applied:** 2026-11-06, to `text/*.usfm`

1. **Apply:** `Gen.25.4` la: `Henochum` → `Henōchum` (macrons as Gen 4:17, 5:18)
2. **Apply:** `Luke.3.37` la: `Ēnōchī` → `Henōchī`

## 2. Jericho: keep *Hierichūs*

1556 reads *ad Hierichuntem descendens* in Luke 10:30 and *Hierichuntis*, *Hierichunte* elsewhere; Wikisource's
Joshua has *Hierichunt-*, its Gospels *Hiericunt-*; Greek Ἰεριχώ has χ. Your *Hierichūntem* (Luke 10:30) stands;
the rule *Hiericunt- → Hierichunt-* would bring the coming Gospel chapters into line.

**Decision:** accept (Nathan, 2026-11-06)  
**Applied:** 2026-11-06: rule *Hiericunt- → Hierichunt-* approved in `orthography.tsv`

## 3. Benammi (Gen 19:38)

1738, 1750 and Wikisource read *Benammi*; Hebrew *ben-ʿammî* has one n. Your *Bennammi* looks like a slip.

**Decision:** accept (Nathan, 2026-11-06)  
**Applied:** 2026-11-06, to `text/GEN.usfm`

1. **Apply:** `Gen.19.38` la: `Bennammi` → `Benammi`

## 4. Abihu (*Abius*, Exodus and Leviticus; not yet in your text)

Wikisource *Abius*, *Abium* (Exod 24:9, 28:1, Lev 10:1). The i is a vowel, but the j rule reads *ab-* as a prefix
(as in *abjungō*) and would write *Abjus*. Proposed: a keep-list of names the j rule leaves alone, starting with
*Abius*; the macron is decided with Exodus.

**Decision:** accept (Nathan, 2026-11-06)  
**Applied:** 2026-11-06: *Abius* and its forms added to `JV_KEEP` in `pipeline/macronize.py`
