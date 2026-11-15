# Exodus 31–40: stages 3–5, one proposal per verse

Proposed 2026-11-15 (decision 30's standing rule), as Exodus 21–30 (`data/review/exod21-30-stages3-5.md`).
**Waiting for your approval**, with four questions first (below).

## Where it stands

- **Stages 1–2**: `data/review/exod31-40-stage2.md`. Wikisource has no Exodus 31–40, so the draft
  (`text/draft/EXO.usfm`, 325 verses, KJV numbering) is 1738's own text, every line read on the page twice. Four
  corrections for the reading edition were added there from stages 3–5 (its last section): 33:1 *lacte*, 33:8
  *tabernāculum*, 36:25 *totidemque* (1738's misprints) and 37:9 *obtegerent* (1554, 1573 and 1726; 1738 and 1750
  *obtegeret*, which does not construe: **your call**).
- **Stages 3–5**: `data/review/exod31-40-ch31.md` … `-ch40.md`, 325 items, all checking `ok`. Preview:
  **`text/draft/EXO.preview.usfm`**.
- **Stage 2b** (the printed text, from the read lines) is not built yet: it needs the small `orig` route described at
  the end of the stage-2 file.

## How the verses were made

Four readers (31–32, 33–35, 36–38, 39–40) under one brief, as for 1–30. Their calls are in
`data/decisions/Exod.layout.tsv` (65 lines for 31–40) and `Exod.forms.tsv` (240 rows, each with its reason). Then an
independent proofread of all 325 verses by two more readers; its findings are fixed (below).

- **Quotation marks, all new** (1738 prints none): God's sanctuary speech, open since 25:2, reopens at 31:1 (a
  paragraph inside it, as the settled 26:1–30:1) and closes at 31:17; 31:13 reopens around a new *inquit*.
  Chapter 32: God's speech 32:7–10 (one speech, *Videō,” inquit, “* at 32:9), Moses' plea 32:11–13, the dialogue of
  32:17–34; reported speech left unmarked (32:12 the Egyptians, 32:13 the oath, 32:23–24, 32:27, 32:30). 33:1–3,
  33:19–23 (each new *inquit* its own speech, as the settled 6:1–2), 34:1–3, 34:6–7 (the proclamation, kept in
  1738's capitals, as the settled 28:36 *JŌVÆ SACRUM*), 34:10–26, 34:27 *(inquit, Mōsem adloquēns)* turned into
  commas, 35:1–3, 35:4–19 (reopened at the 35:10 paragraph), 40:2–15. 35:30–35 reported. 46 opening marks, all balanced.
- **Paragraphs**: the BSB's, moved to the sentence start where they fell inside one (31:12 → 31:13, 40:34 → inside
  40:33 at *Postquam*, where 1738 indents); added at 32:7, 32:17, 32:25, 32:30 (chapter 32 was one paragraph of about
  640 words), 34:29 and 40:16 (brief.md, decision 52).
- **Spelling**: 27 word rules added to `data/rules/orthography.tsv`, approved by decisions already made: 26 *ad-*
  forms of 1738 the rules did not know (*adligābant, adsurgēbant, adpellāns, adscendat, adfluentem …*; the settled
  text has none of them; *adsint*, a compound of *sum*, kept: decision 37) and *septentriōnālī* (decision 42; the
  settled 27:11). No *ad-* is left in the preview but *adsint*.
- **Names**: *Beselēl-* (Greek Βεσελεήλ, Hebrew tsere), *Ūris* (Greek Οὐρείου, Hebrew shureq), *Hūris* (the settled
  *Hūr*), *Oholīāb-* (first o short or unmarked: Hebrew qamets hatuf), *Achīsāmāchī* (Hebrew), *Nūnis*; *daniā* (the
  tribe) lower case and unmarked, as 1738 and the settled *Dan*, like *jūdaicā* beside it.

## Calls worth a look

- **Forms the proposal had wrong, fixed by the readers**: the ablatives (*ā Jōvā* 34:4, 34:24, 34:32, 36:4; *grātiā*
  with *valēre* 33:12–16, 34:9, as the settled Acts 2:47; *in commissūrā*, *aureā corōnā*, *super mēnsā*, *Sīnā* in
  *dē/in monte Sīnā*), nominatives (*pœna* 31:15, *mēnsūra*, *summa*, *āra* 40:10, *sua voluntās* 35:29), *incīde*,
  *incīdit*, *succīditōte* (*incīdō*, *succīdō*, to cut), *māla* (pomegranates, as 28:33), *paxillōs*, *annulī*, and
  *æris*, *æream* (bronze, not *āeris*: as decision 63).
- ***abdūxerīs*** (33:15) as a perfect subjunctive in a prohibition; ***proficīscēris*** (34:24) future indicative;
  ***dīspescerent*** (32:24): Gaffiot has *dispēscō* and *dīspescō*; the readers could not tell which.
- **Castellio's coinages**, marked by analogy: *cherūbāta*, *cherūbātum* (36:8, 35), *fēriātiō* (31:15),
  *tabernāculāris* (40:6, all three printings), *assamenta* (35:11, 40:18, "boards"; stem unmarked: no source).
- **38:11 *idem*** read as neuter ("did the same"); *īdem* if "he likewise".

## Questions

1. **37:9 *obtegerent*** (above): applied to the draft from 1726; say if you prefer 1738's *obtegeret*. Since
   seen on Castellio's own pages (2026-11-15): **1554** *obtegerẽt* (MDZ bsb10196330, image 62) and **1573**
   *obtege-|rent* (bsb10141277, image 88). The singular is 1738's misprint (the tilde lost), carried into 1750.
2. **40:20 *vectēs āræ accommodāvit*** ("the bars on the altar"): the verse is about the ark (Hebrew הָאָרֹן, LXX
   κιβωτόν, KJV "the staves on the ark"). (*eam … propitiātōriō tēxit* does not decide it: *eam* can take up the
   *arcam* of *in arcam illātō*.) 1738 (leaf 156), 1750 (its OCR, line 14183) and 1726 (TXT/1, line 2477) print
   *aræ*, and so do **1554** *arę* (MDZ bsb10196330, image 64), **1556** *arę* (e-rara 10281727, p. 104, col. 1) and
   **1573** *aræ* (image 90), all three seen on the page (2026-11-15). So it is the reading of every lifetime revision
   Castellio made, not a later misprint (1551 not seen: Google Books refused the search). Not a misreading of the
   Hebrew, which names the ark three times in the verse (*ʾărôn*) and has nothing like *mizbēaḥ*, the altar: most
   likely a one-letter slip, *arcæ* → *aræ*, by Castellio or the first compositor, which leaves a grammatical
   sentence (so nobody stopped at it), and *vectēs … āræ* is a phrase Castellio had just used for the altar's bars
   (38:7 *vectēs … ad āræ costās*, 39:39 *āram ærātam … vectēsque*). Not changed. Correct to *arcæ*, or keep
   *āræ* with a note, as the edition does where Castellio departs from the Greek (1 John 4:4, 1 Pet 5:8, Jude 6; the
   front matter's *Notæ* promise such notes for the Hebrew too)? The note on the model of those:
   `\f + \fr 40:20 \ft Hebraicē הָאָרֹן, ‘arcæ’; Castelliōnis ēditiōnēs ‘āræ’ habent.\f*`
   **Decided** (Nathan, 2026-11-15): *āræ* kept, with the note. The drafts carry no notes, so it is applied to
   `text/EXO.usfm` when 31–40 is settled, by this line:
   **Apply** (on settling): `Exod.40.20` la: `vectēs āræ accommodāvit` → `vectēs āræ\f + \fr 40:20 \ft Hebraicē הָאָרֹן, ‘arcæ’; Castelliōnis ēditiōnēs ‘āræ’ habent.\f* accommodāvit`
   Declined (the correction to *arcæ*): `Exod.40.20` `vectes arae accommodavit` → `vectes arcae accommodavit`
3. **36:27 *in immō***: the approved word rule *imo → immo* (learned from Gen 23:13 *immō*, "no indeed") also turns
   *in imo* "at the bottom" (*īmus*, Gaffiot) into *immō*, here and in the settled 26:24 *et in immō et in summō*.
   Proposed: a phrase rule `in imo → in imo` (status `proposed`, which keeps *īmō* where *in* precedes), and the
   settled 26:24 corrected:
   **Apply** (only if accepted): `Exod.26.24` la: `et in immō et in summō` → `et in īmō et in summō`
4. **Versification** (from the stage-2 file): keep 36:25–34 and 38:13–18 as Castellio divides them (the counts agree
   with the KJV), as the draft does now?

Also for you to know: *sexdecim* (36:29), *trīgēnum* (36:15) and *cācabōs* (38:3) are not Gaffiot's spellings
(*sēdecim*, *trīcēnī*, *caccabus*), but they are the settled 26:25, 26:8 and 27:3's; *circumsēptum* (39:23) is
Gaffiot's variant of *circumsæptum*; *tēmetipsum* (32:13) is written as one word, as the settled *sēmetipsum*,
though decision 51 writes *sē ipsum* apart. Say if any should change everywhere.

**Decision:** accept 1, 2, 3, 4 (Nathan, 2026-11-15: "Accept all of the other proposals I didn't comment on"; 2, 40:20: *āræ* kept with the note, applied on settling; Exodus 31–40 settled, "Settle it")
