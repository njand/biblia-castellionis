# Deuteronomy: spelling rules for forms the approved rules do not list, researched

Proposed 2026-11-18 (Claude), as Numbers' (`num1-36-rules-research.md`; Nathan, 2026-11-16: "Before applying it to new
forms, be sure to research them (Gaffiot and classical corpus)"). **Approved and added to `data/rules/orthography.tsv`** (Nathan,
2026-11-18: "Yes, add them"; the 54 rows also in `deut1-34-rules.tsv` beside this file); the review items and the preview
rebuilt with them.

Found by scanning the draft for words that make the same change as two or more approved word rules (`ad- → as-`, `-ms- →
-mps-`, `tent- → tempt-` …) and have no rule of their own; the scan's false families (*-ert → -erit*, *sicut*) dropped by
reading them. Tools: `python -m pipeline latin macron` (G = Gaffiot 2016's headword as the tool reports it), `latin attest
--count` (Latin Library; old : new exact-form hits, with tiers). Not changed: the compounds of *sum* (*adsumus, adsunt,
adfuit, adfuerunt, adfuisset, adfuturum*; decision 37), *audivi* and *audivimus* (decision 19 keeps -īvī where the settled
text has it, 32 : 3; -īvimus), *custodivit, exaudivit* (-īvit), *colligo* (not *intellego*), *verumtamen, dumtaxat*.

**Found on the way, in the settled text** (not changed: settled chapters are never rewritten by code): `data/gold/` has
*adsignātās* and *adsignāverit* beside 11 *assign-* forms; a fix for the settled-fixes list.

| # | old → new | where | Gaffiot | corpus old : new | why |
|---|---|---|---|---|---|
| 1 | adfeceritis → affeceritis | 21:22 | adfĭciō, fēcī, fectum, ĕre | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 2 | adfectos → affectos | 8:3 | adfectus, a, um · adfectŭs, ūs | 16 (T1: 2, T2: 1, T2.5: 2, T3: 5, T4: 6) : 21 (T2.5: 2, T3: 2, T4: 17) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 3 | adfero → affero | 26:10 | adfĕrō, adtŭlī, adlātum, ferre | 30 (T1: 9, T2: 6, T2.5: 3, T3: 8, T4: 4) : 23 (T1: 5, T3: 2, T4: 16) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 4 | adficiet → afficiet | 7:15, 28:27, 28:28, 28:35 | adfĭciō, fēcī, fectum, ĕre | 5 (T1: 1, T2.5: 1, T3: 2, T4: 1) : 3 (T2: 1, T4: 2) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 5 | adfigito → affigito | 15:17 | adfīgō, fīxī, fīxum, fīgĕre | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 6 | adflato → afflato | 34:9 | adflātus, a, um · adflātŭs, ūs · adflō, āvī, ātum, āre | 1 (T3: 1) : 2 (T2: 1, T4: 1) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 7 | adfligeret → affligeret | 8:2, 8:16 | adflīgō, flīxī, flīctum, ĕre | 12 (T2.5: 1, T3: 3, T4: 8) : 6 (T2: 1, T4: 5) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 8 | adfluentiam → affluentiam | 33:19 | adflŭentĭa, æ | 0 : 10 (T3: 2, T4: 8) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 9 | adgregandus → aggregandus | 32:50 | adgrĕgō, āvī, ātum, āre | 2 (T4: 2) : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 10 | adlevato → allevato | 22:4 | adlĕvātus, a, um · adlĕvō, āvī, ātum, āre · adlēvō, āre | 2 (T1: 1, T3: 1) : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 11 | adligatote → alligatote | 6:8, 11:18 | adlĭgō, āvī, ātum, āre | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 12 | adloquuntor → alloquuntor | 25:8 | adlŏquor, lŏcūtus sum, lŏquī | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 13 | adparendum → apparendum | 10:8 | appārĕō | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 14 | adpareat → appareat | 16:16 | appārĕō | 7 (T2: 1, T3: 4, T4: 2) : 440 (T1: 12, T2: 39, T2.5: 48, T3: 67, T4: 274) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 15 | adparet → apparet | 10:15 | appārĕō · appărō | 11 (T1: 1, T2.5: 1, T3: 6, T4: 3) : 1229 (T1: 15, T2: 225, T2.5: 51, T3: 220, T4: 718) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 16 | adpellant → appellant | 3:9 | appellō · appellō | 20 (T3: 17, T4: 3) : 867 (T1: 3, T2: 213, T2.5: 95, T3: 201, T4: 355) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 17 | adpetet → appetet | 14:26 | appĕtō · appĕtō, ōnis | 3 (T3: 3) : 4 (T2.5: 2, T3: 2) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 18 | adscendent → ascendent | 28:43 | ascendō | 0 : 13 (T4: 13) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 19 | adscenderem → ascenderem | 3:27, 10:1 | ascendō | 0 : 5 (T1: 1, T2: 1, T3: 1, T4: 2) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 20 | adscenderis → ascenderis | 32:50 | ascendō | 0 : 8 (T1: 1, T2.5: 1, T3: 2, T4: 4) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 21 | adscendissem → ascendissem | 9:9 | ascendō | 0 : 1 (T2.5: 1) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 22 | adscendissetis → ascendissetis | 5:5 | ascendō | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 23 | adscensuros → ascensuros | 1:41 | — | 0 : 3 (T4: 3) | decision 37 (ad- assimilated; Gaffiot heads the assimilated form) |
| 24 | adsequatur → assequatur | 19:6 | adsĕquor | 10 (T2: 3, T2.5: 5, T4: 2) : 16 (T2: 3, T3: 1, T4: 12) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 25 | adserti → asserti | 13:5 | — | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 26 | adsertore → assertore | 28:68 | adsertŏr | 2 (T4: 2) : 6 (T4: 6) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 27 | adsignabis → assignabis | 31:7 | adsignō | 0 : 1 (T4: 1) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 28 | adsignasse → assignasse | 32:8 | adsignō | 3 (T4: 3) : 2 (T4: 2) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 29 | adstato → astato | 5:31 | adstō | 0 : 3 (T1: 3) | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 30 | caussae → causae | 21:5 | causa · caussa, etc. | 29 (T2: 5, T3: 3, T4: 21) : 1501 (T1: 44, T2: 80, T2.5: 273, T3: 302, T4: 802) | decision 37: *causa* |
| 31 | caussamque → causamque | 32:41 | — | 1 (T4: 1) : 77 (T1: 7, T2: 1, T2.5: 20, T3: 20, T4: 29) | decision 37: *causa* |
| 32 | caussas → causas | 1:17 | causa · caussa, etc. | 38 (T2: 5, T3: 1, T4: 32) : 1585 (T1: 27, T2: 124, T2.5: 171, T3: 398, T4: 865) | decision 37: *causa* |
| 33 | sumserunt → sumpserunt | 1:25 | sūmō, sūmpsī, sūmptum, ĕre | 3 (T2: 1, T4: 2) : 69 (T1: 1, T2: 3, T2.5: 2, T3: 19, T4: 44) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 34 | sumsissem → sumpsissem | 9:9 | sūmō, sūmpsī, sūmptum, ĕre | 0 : 8 (T1: 2, T2.5: 1, T3: 3, T4: 2) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 35 | sumsero → sumpsero | 32:41 | sūmō, sūmpsī, sūmptum, ĕre | 0 : 10 (T1: 3, T2: 2, T2.5: 1, T4: 4) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 36 | sumto → sumpto | 8:10, 32:43 | sūmō, sūmpsī, sūmptum, ĕre | 2 (T4: 2) : 114 (T2: 14, T2.5: 1, T3: 34, T4: 65) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 37 | absumtum → absumptum | 2:14 | absūmō, sūmpsī, sūmptum, ĕre | 1 (T4: 1) : 27 (T1: 1, T2: 1, T2.5: 1, T3: 11, T4: 13) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 38 | insumta → insumpta | 14:26 | īnsūmō, sūmpsī, sūmptum, ĕre | 0 : 2 (T2.5: 1, T3: 1) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 39 | contemtisque → contemptisque | 1:43 | — | 0 : 2 (T2: 2) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 40 | redemtum → redemptum | 15:15 | rĕdĭmō, ēmī, ēmptum (ēmtum), ĕre | 1 (T4: 1) : 30 (T2: 1, T2.5: 1, T3: 13, T4: 15) | Gaffiot heads -mps-/-mpt- (*sūmō, sūmpsī, sūmptum*; *contemnō, tempsī*; *redimō, ēmptum*), as the approved *consumsit, redemtos* rows |
| 41 | tentaret → temptaret | 8:2 | tentō | 22 (T2: 4, T4: 18) : 37 (T1: 1, T2: 2, T2.5: 2, T3: 17, T4: 15) | decision 37: *temptō* |
| 42 | tentaretque → temptaretque | 8:16 | — | 0 : 1 (T3: 1) | decision 37: *temptō* |
| 43 | tentastis → temptastis | 6:16 | tentō | 1 (T4: 1) : 3 (T3: 1, T4: 2) | decision 37: *temptō* |
| 44 | tentatote → temptatote | 6:16 | tentō | 0 : 0 | decision 37: *temptō* |
| 45 | intelligemus → intellegemus | 18:21 | intellĕgō, lēxī, lēctum, ĕre · intellĭgō | 7 (T2: 1, T3: 1, T4: 5) : 47 (T2: 1, T2.5: 4, T3: 1, T4: 41) | decision 37: *intelleg-* |
| 46 | intelligendum → intellegendum | 29:4 | intellĕgō, lēxī, lēctum, ĕre · intellĭgō | 106 (T1: 1, T2: 3, T3: 1, T4: 101) : 206 (T2: 2, T2.5: 22, T3: 7, T4: 175) | decision 37: *intelleg-* |
| 47 | humeros → umeros | 33:12 | hŭmĕrus | 64 (T2: 11, T3: 4, T4: 49) : 128 (T2: 4, T2.5: 13, T3: 80, T4: 31) | brief.md: *umerus*; approved *humeris → umeris* |
| 48 | audiveritis → audieritis | 4:36, 7:12, 13:12 | audĭō, īvī | 0 : 30 (T2: 1, T3: 3, T4: 26) | decision 19: -īv- shortened except 3rd sing. -īvit and -īvimus (approved *audiverit → audierit*) |
| 49 | audiverimus → audierimus | 5:25 | audĭō, īvī | 1 (T4: 1) : 8 (T1: 1, T3: 2, T4: 5) | decision 19: -īv- shortened except 3rd sing. -īvit and -īvimus (approved *audiverit → audierit*) |
| 50 | serviveritis → servieritis | 28:47 | servĭō, īvī | 0 : 3 (T4: 3) | decision 19: -īv- shortened except 3rd sing. -īvit and -īvimus (approved *audiverit → audierit*) |
| 51 | transiverimus → transierimus | 29:16 | trānsĕō, ĭī | 0 : 5 (T1: 1, T2: 1, T3: 2, T4: 1) | decision 26: *eō*'s compounds, -i- forms (*trānsierimus*) |
| 52 | lacessivisti → lacessisti | 33:8 | lăcessō, īvī | 0 : 1 (T2.5: 1) | decision 19 (short forms) and 26 (contracted -īstī) |
| 53 | circumivissemus → circumissemus | 2:3 | circumĕō | 0 : 0 | decision 26: *eō*'s compounds contracted (-īsse, -īssent; no -iisse), so *circumīssēmus* |
| 54 | pene → paene | 9:8 | pænĕ | 841 (T1 0, T2 31, T3 14, T4 796) : 1729 (T1 86, T2 91, T2.5 280, T3 567, T4 705) | Gaffiot's headword; the settled text has *pæne* 3 times (found by reader 3) |

**Verdict**: all 54 apply. The ad- rows where Gaffiot heads *ad-* follow decision 37 as Nathan confirmed it for Numbers
("Accept 1-8", no. 1); the corpus leans *ad-* only for *adferō* (30 : 23), *adfīgō*/*adflīgō* (12 : 6), *adlevō* (2 : 0) and
*adgregō* (2 : 0), as it did for Numbers' *adf-* verbs.
