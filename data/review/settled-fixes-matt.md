# Settled Matthew: four slips found during Mark 6–16, stages 3–5

Proposed 2026-11-08 (you asked for all three on 2026-11-08). Each **Apply** line is an exact replacement in
`text/MAT.usfm`, checked to match once. Apply with
`python -m pipeline review apply data/review/settled-fixes-matt.md --write` after the Decision line; data/gold is
rebuilt.

## Fixes (4)

**Decision:** accept (Claude, delegated by Nathan, 2026-11-08: items 1–3 chosen by Nathan; item 4 added on the same evidence rule)

1. **Matt 27:37** *JŪDæŌRUM* → *JŪDÆŌRUM*: a lower-case æ inside capitals. `macronize.ligatures` handled only a
   lower-case *e* after *A*; fixed 2026-11-07.
   **Apply:** `Matt.27.37` la: `RĒX JŪDæŌRUM.` → `RĒX JŪDÆŌRUM.`
2. **Matt 20:29** *Hierichunte* → *Hierichūnte*: as your Luke 10:30 *Hierichūntem* and Wiktionary's *Hierichûs*
   (long ū; Gaffiot has only *Jĕrīchō*). The pilot's rule (*Hiericunt- → Hierichunt-*) carried over Wikisource's
   unmarked vowel.
   **Apply:** `Matt.20.29` la: `Iīs autem Hierichunte` → `Iīs autem Hierichūnte`
3. **Matt 22:44** *Sēde* → *Sedē*: the imperative of *sedeō* (Gaffiot *sĕdĕō*), as your Gen 27:19 *sedē* and the
   proposed Mark 12:36 *sedē*. *Sēde* is the ablative of *sēdēs* (correct in Matt 23:2).
   **Apply:** `Matt.22.44` la: `“Sēde ad meam dexteram,` → `“Sedē ad meam dexteram,`
4. **Matt 19:10** *connūbia* → *cōnūbia*: Gaffiot's headword *cōnūbĭum*; republican prose writes *cōnūbi-* (Latin
   Library: *conubia* 7, *conubium* 2, *conubio* 1 republican hits; *connubi-* none, all post-classical or later;
   decision 18), and your Gen 6:4 has *cōnūbiīs*. Mark 12:25 is proposed as *cōnūbia*. Added 2026-11-08.
   **Apply:** `Matt.19.10` la: `nōn expedit connūbia conjungere` → `nōn expedit cōnūbia conjungere`
