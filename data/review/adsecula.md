# *adsecula* throughout, for *assecla*

*2026-11-20.* Nathan, on the corpus evidence: "*adsecula* is the same word, but it is more classical. Standardize to
that throughout the whole Bible."

**The evidence** (`python -m pipeline latin attest`, every case form, 2026-11-20). The Latin Library by tier:

| Form | Tiers 1–3 (classical) | Tier 4 |
|---|---|---|
| *adsecul-* | 9 (Cicero 7, Livy, Juvenal) | 2 |
| *assecl-* | 3 (Nepos, Erasmus 2) | 15 (Alanus, Vives, Bacon …) |
| *adsecl-* | 0 | 1 (Ammianus) |
| *assecul-* | 0 | 2 |

Gaffiot's headword is *adsĕcŭla* (every vowel of the stem short); Lewis & Short's is *assĕcla*. Castellio's 1738
prints *adsecl-* at every place read (Exod 7:20, 10:7, Judg 3:24 and 1 Samuel's three, `data/decisions/*.orig.tsv`
and the read lines); the printed text (`text/orig/`) keeps that (decision 58).

**The rules** (`data/rules/orthography.tsv`): the approved word rows *adseclis → asseclis* (decision 37) and
*adseclarum → asseclarum*, *adseclisque → asseclisque* (1 Samuel, 2026-11-20) set to `rejected` with Nathan's words;
added, approved, the stem rules *adsecl- → adsecul-* and *assecl- → adsecul-*, which spell every form so in books to
come (Wikisource's Esther has *asseclae, asseclas* …).

**The settled text**, nine words: the endings keep their marks (*-ārum, -īs, -ās*), the stem none.

**Decision:** accept all (Nathan, 2026-11-20: "Standardize to that throughout the whole Bible")

1. **Exod 7:20** *ejusque asseclārum* → *adseculārum*.
    **Apply:** `Exod.7.20` la: `ejusque asseclārum` → `ejusque adseculārum`
2. **Exod 8:11** *et asseclīs* → *adseculīs*.
    **Apply:** `Exod.8.11` la: `et asseclīs` → `et adseculīs`
3. **Exod 8:21** *in ejus asseclās* → *adseculās*.
    **Apply:** `Exod.8.21` la: `ejus asseclās` → `ejus adseculās`
4. **Exod 9:14** *tuōs asseclās* → *adseculās*.
    **Apply:** `Exod.9.14` la: `tuōs asseclās` → `tuōs adseculās`
5. **Exod 10:7** *Pharaōnis asseclæ* → *adseculæ*.
    **Apply:** `Exod.10.7` la: `Pharaōnis asseclæ` → `Pharaōnis adseculæ`
6. **Judg 3:24** *rēgis asseclæ* → *adseculæ*.
    **Apply:** `Judg.3.24` la: `rēgis asseclæ` → `rēgis adseculæ`
7. **1 Sam 8:15** *spadōnibus asseclīsque* → *adseculīsque*.
    **Apply:** `1Sam.8.15` la: `spadōnibus asseclīsque` → `spadōnibus adseculīsque`
8. **1 Sam 22:6** *stīpātus asseclārum* → *adseculārum*.
    **Apply:** `1Sam.22.6` la: `stīpātus asseclārum` → `stīpātus adseculārum`
9. **1 Sam 22:17** *rēgiīs asseclīs* → *adseculīs*.
    **Apply:** `1Sam.22.17` la: `rēgiīs asseclīs` → `rēgiīs adseculīs`
