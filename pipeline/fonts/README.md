# The website's fonts

Copied into `build/site/fonts/` by `site.write`. Both are under the SIL Open Font License 1.1 (the licence texts
are beside them). A subset is a Modified Version under the OFL, which may not keep the Reserved Font Names, so they
are renamed.

| File | From | Kept | Renamed |
|---|---|---|---|
| `castellio-book-regular.woff2`, `-italic`, `-semibold` | Gentium Book 7.000 (SIL), `GentiumBook-Regular/Italic/SemiBold.ttf` from software.sil.org/gentium | U+0000–024F, U+0300–036F, U+0370–03FF, U+1E00–1EFF, U+1F00–1FFF, U+2000–206F and a few signs (€ ™ arrows − ◐ ☀ ☾ ﬀ–ﬆ) | Castellio Book |
| `castellio-hebrew.woff2` | Ezra SIL 2.51 (SIL), `SILEOT.ttf` | U+0020–0040, U+0590–05FF, U+FB1D–FB4F, U+25CC, U+2000–206F | Castellio Hebrew |

Made 2026-11-11 with fontTools 4.68 (`fonttools subset … --flavor=woff2 --layout-features='*'`, then the `name`
table's family, full and PostScript names changed). To remake them, repeat with the same ranges.
