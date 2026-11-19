# Joshua: spelling rules for forms the approved rules do not list, researched

Proposed 2026-11-19 (Claude), as Deuteronomy's (`deut1-34-rules-research.md`; Nathan, 2026-11-16: "Before applying it
to new forms, be sure to research them (Gaffiot and classical corpus)"). **Six rejected** (Nathan, 2026-11-19: "I disagree with adquiro → acquiro, adsequor → assequor, adsigno → assigno,
adsto → asto, adsurgo → assurgo based on corpus evidence"): nos. 9, 12–16, struck below; those verbs now keep *ad-*
throughout the edition (`ad-unassimilated.md`). **The other 14 approved** (Nathan, 2026-11-19: "Yes, add the 14"): in `data/rules/orthography.tsv` as approved
(status `approved` in `josh1-24-rules.tsv`), the preview rebuilt; none of the 14 forms is in the settled text.

Found by scanning the preview for words of the approved families (*ad-* assimilated, decision 37; *septentriō*;
*-mps-*) that kept the old spelling, and checking the settled text's usage (`data/gold/`: *aggressus* 32, *allocūtus* 68,
*appellāvit* 19, *ascendit* 25, *assignāvit* 4, *astāns* 9, *assurgō* forms 5; *septentriōnēs* 4, no *septemtr-*;
*sumpsimus*). Tools: `python -m pipeline latin macron` (Gaffiot's headword as the tool reports it, for the old form or,
where it knows only that, the new), `latin attest --count` (Latin Library; old : new exact-form hits). **Not changed**:
the compounds of *sum* (*adfuerat, adfutūrum, adfutūrus, adfuī*: decision 37, as the settled *adfuit* ×7), *mīllia*
(the settled text 81 : 8 *mīlia*), *dumtaxat* (Gaffiot; the settled 9 : 2), *exs-* (*exstat, exstitit*: the settled
text's).

| # | old → new | where | Gaffiot | corpus old : new | why |
|---|---|---|---|---|---|
| 1 | adgesserunt → aggesserunt | 7:26 | adgĕrō [freq 12] | 1 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 2 | adgreditur → aggreditur | 11:7 | adgrĕdĭor, gressus sum, grĕdī [freq 8] | 86 : 103 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 3 | adgredi → aggredi | 8:3 | adgrĕdĭor, gressus sum, grĕdī [freq 8] | 102 : 81 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 4 | adligabis → alligabis | 2:18 | adlĭgō, āvī, ātum, āre [freq 9] | 0 : 2 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 5 | adlocuto → allocuto | 6:8 | adlŏcūtus, a, um | 0 : 0 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 6 | adpellite → appellite | 24:23 | appellō [freq 6] · appellō [freq 10] | 0 : 1 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 7 | adpellabuntur → appellabuntur | 21:9 | appellō [freq 6] · appellō [freq 10] | 0 : 6 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 8 | adpellata → appellata | 15:13 | appellō [freq 6]  | 1 : 264 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 9 | ~~adquisito → acquisito~~ rejected | 17:18 | acquīrō [freq 10] | 12 : 8 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 10 | adscenderent → ascenderent | 17:15 | ascendō [freq 9] | 0 : 17 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 11 | adscenditur → ascenditur | 11:17, 12:7 | ascendō [freq 9] | 0 : 13 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 12 | ~~adsecuturos → assecuturos~~ rejected | 2:5 | adsĕquor [freq 8] | 2 : 3 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 13 | ~~adsignarunt → assignarunt~~ rejected | 20:8 | adsignō [freq 10] | 3 : 7 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 14 | ~~adsignavi → assignavi~~ rejected | 24:4 | adsignō [freq 10] | 3 : 3 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 15 | ~~adstantibus → astantibus~~ rejected | 3:17, 24:1 | — | 23 : 30 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 16 | ~~adsurrexit → assurrexit~~ rejected | 3:16 | adsurgō [freq 10] | 7 : 6 | decision 37 (ad- assimilated; Gaffiot heads the ad- form: Nathan's "Accept 1-8" no. 1 for Numbers, decision 37 as written) |
| 17 | septemtrionem → septentrionem | 24:30 | septentrĭō [freq 11] | 7 : 126 | septentriō as Gaffiot heads it (the approved septemtrione → septentrione and its other forms) |
| 18 | septemtrionibus → septentrionibus | 8:13, 17:9, 19:14 | septentrĭō [freq 11] | 3 : 14 | septentriō as Gaffiot heads it (the approved septemtrione → septentrione and its other forms) |
| 19 | septemtrionales → septentrionales | 11:2, 17:10 | septentrĭōnālis, e [freq 16] | 0 : 30 | septentriō as Gaffiot heads it (the approved septemtrione → septentrione and its other forms) |
| 20 | sumsimus → sumpsimus | 9:12 | sūmō, sūmpsī, sūmptum, ĕre [freq 7] | 0 : 29 | Gaffiot heads -mps-/-mpt- (sūmō, sūmpsī, sūmptum), as the approved sumsit → sumpsit |
