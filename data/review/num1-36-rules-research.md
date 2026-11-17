# Numbers: the 47 proposed spelling rules, researched

Rows 600–646 of `data/rules/orthography.tsv` (status `proposed`, "Claude, 2026-11-16").
Tools: `python -m pipeline latin macron` (G = Gaffiot 2016 headword, as the tool reports it), `latin attest`
(Latin Library corpus; tiers as the tool shows them, T1 = earliest/Golden-Age core … T4 = late/post-classical),
`latin ls` (Lewis & Short). Corpus counts are exact-form hits, old : new. Where both forms have 0 hits, a
lemma-level count of other forms is given in the note. Raw output: `raw.txt` beside this file.

**A point for the whole group.** Decision 37 says *ad-* is assimilated "as in your own chapters", not as Gaffiot
heads the word. For most verbs here Gaffiot heads the assimilated form (*appellō, appāreō, apprimō, ascendō,
ascīscō, aspiciō, aspergō*), but for the *adf-* and *adg-* verbs **Gaffiot 2016 heads the *ad-* form**: *adfor,
adfectō, adferō, adficiō, adflō, adfluō, adgregō*. The edition already assimilates these (approved rows such as
*adfici → affici, adferemus → afferemus, adflatus → afflatus, adgregabor → aggregabor, adgregare → aggregare*),
so the rows below follow that precedent; but the brief's "classical spellings as Gaffiot heads them" points the
other way for these 11 rows, which Nathan may want to know (601 is the doubtful one; 602–611 apply by precedent).

| # | old → new | Gaffiot headword | corpus old : new | verdict | note |
|---|---|---|---|---|---|
| 600 | absumsit → absumpsit | absūmō, sūmpsī, sūmptum | 2 (T1 1, T4 1) : 59 (T2 2, T3 22, T4 35) | apply | one T1 *absumsit*; the -mps- form dominates |
| 601 | adfabor → affabor (12:8) | **adfor**, fātus sum (ad- headed) | 0 : 0; lemma: *adfatus* 34 : *affatus* 27, *adfari* 14 : *affari* 5 | **doubt** | Gaffiot heads *adfor*, and the corpus favours *adf-* overall (48 : 32), though T2 favours *aff-* (5 : 1); no *affor* form in the settled text to follow |
| 602 | adfectetis → affectetis | **adfectō** (ad- headed) | 0 : 1 (T4) | apply | by decision 37 precedent; Gaffiot heads ad- |
| 603 | adferendae → afferendae | **adferō**, adtulī, adlātum (ad- headed) | 0 : 0 | apply | by the many approved *adfer- → affer-* rows; Gaffiot heads ad- |
| 604 | adficere → afficere | **adficiō** (ad- headed) | 30 (T1 1, T2.5 4, T3 6, T4 19) : 65 (T2 8, T2.5 1, T4 56) | apply | precedent *adfici → affici* etc.; Gaffiot heads ad- |
| 605 | adficiemus → afficiemus | **adficiō** | 0 : 2 (T3, T4) | apply | as 604 |
| 606 | adficientur → afficientur | **adficiō** | 1 (T4) : 2 (T2.5, T4) | apply | as 604 |
| 607 | adficis → afficis | **adficiō** | 1 (T2.5) : 2 (T1, T4) | apply | as 604 |
| 608 | adfletur → affletur (5:14) | **adflō**, āvī, ātum (ad- headed) | 0 : 0; lemma: *adflatus* 15 : *afflatus* 45 (T2 10 : 0) | apply | context *obtrectatione … adfletur* is passive of *adflō/afflō* (Wiktionary also lists a homograph from *affleō*, not the sense here); precedent *adflatus → afflatus* approved |
| 609 | adflueret → afflueret | **adfluō**, flūxī (ad- headed) | 1 (T3) : 6 (T2.5 2, T4 4) | apply | Gaffiot heads ad- |
| 610 | adgregabitur → aggregabitur | **adgregō** (ad- headed) | 0 : 0; lemma: *adgregare* 6 : *aggregare* 4, *adgregavit* 6 : *aggregavit* 6 | apply | corpus evenly split, Gaffiot heads ad-; follows approved *adgregabor/adgregare/adgregarunt → agg-* |
| 611 | adgregarentur → aggregarentur | **adgregō** | 2 (T3) : 0 | apply | as 610 |
| 612 | adparentem → apparentem | appārĕō | 0 : 10 (T2 2, T3 3, T4 5) | apply | 16:42 |
| 613 | adparentes → apparentes | appārĕō | 1 (T4) : 14 (T2 1, T3 2, T4 11) | apply | 16:9 (*appāreō* "attend, serve") |
| 614 | adpellati → appellati | appellō | 3 (T3 1, T4 2) : 162 (T1 1, T2 3, T2.5 11, T3 45, T4 102) | apply | |
| 615 | adposititiorum → apposititiorum (4:7) | none (neither spelling in Gaffiot, L&S or the macron sources) | 0 : 0 | apply | follows approved *adposititios/adposititio → appositi-* and the settled *appositītium, -ō, -ōs*. Separate question: Gaffiot and L&S head the model word *suppŏsĭtīcĭus* with -c-, and decision 37 settled Romans *īnsitīciī*; the settled *appositītius* keeps -t- |
| 616 | adpressit → appressit (22:25) | apprĭmō | 1 (T3) : 0 | apply | |
| 617 | adscenderuntque → ascenderuntque | ascendō (form unknown to the tool with -que) | 0 : 5 (T4) | apply | decision 37 named *ascendō* (30 : 0) |
| 618 | adscendissent → ascendissent | ascendō | 1 (T2.5) : 17 (T2.5 2, T3 1, T4 14) | apply | |
| 619 | adscendunt → ascendunt | ascendō | 0 : 40 | apply | |
| 620 | adscensum → ascensum | ascendō; ascēnsus | 6 (T3 4, T4 2) : 53 (T1 1, T2 1, T2.5 3, T3 7, T4 41) | apply | |
| 621 | adsciscito → asciscito (18:2) | ascīscō (L&S *a-scisco*, reached also via *adscisco*) | 0 : 0; lemma: *adsciscere* 15 : *asciscere* 11, *adscivit* 40 : *ascivit* 28 | apply | Gaffiot and L&S head *asc-*; the corpus overall leans *adsc-*, but T2 favours *asc-* (8 : 3 across the two forms) |
| 622 | adspecta → aspecta (27:13, *eaque adspecta*) | aspĭcĭō; aspectō | 1 (T3) : 7 (T1 3, T3 3, T4 1) | apply | ablative absolute, *aspectā* |
| 623 | adspecturus → aspecturus | aspĭcĭō | 0 : 0 | apply | |
| 624 | adspersus → aspersus | aspergō; aspersus | 4 (T2 1, T3 3) : 23 (T1 1, T2 5, T2.5 1, T3 5, T4 11) | apply | |
| 625 | adspicerent → aspicerent | aspĭcĭō | 1 (T3) : 12 | apply | |
| 626 | adspiciam → aspiciam | aspĭcĭō | 7 (T2 1, T3 5, T4 1) : 19 (T1 3, T2 2, T2.5 2, T3 5, T4 7) | apply | lemma *adspexit* 19 : *aspexit* 126 |
| 627 | adspiciendum → aspiciendum | aspĭcĭō | 0 : 1 (T4) | apply | |
| 628 | adspiciet → aspiciet | aspĭcĭō | 0 : 19 | apply | |
| 629 | caussaque → causaque (25:11) | (causa, decision 37) | 0 : 36 (T1 1, T2 3, T2.5 6, T3 17, T4 9) | apply | |
| 630 | consumsit → consumpsit | cōnsūmō, sūmpsī, sūmptum | 4 (T4) : 119 | apply | |
| 631 | consumto → consumpto | cōnsūmō | 4 (T4) : 44 | apply | |
| 632 | consumtricem → consumptricem (13:32) | not in Gaffiot (tool); L&S *consumptrix*, īcis, "late Lat." | 0 : 0; lemma *consumptrix* 1 (T4) : *consumtrix* 0 | apply | L&S heads -mpt-; follows *cōnsūmō, -sūmptum* |
| 633 | consumtum → consumptum | cōnsūmō | 0 : 63 | apply | |
| 634 | contemsit → contempsit | contemnō, tempsī, temptum | 8 (T3 1, T4 7) : 120 (T1 1, T2 21, …) | apply | |
| 635 | desumsi → desumpsi | dēsūmō, psī, ptum | 0 : 0 | apply | |
| 636 | desumsit → desumpsit | dēsūmō | 0 : 7 (T2 3, T3 3, T4 1) | apply | |
| 637 | desumti → desumpti | dēsūmō | 0 : 1 (T4) | apply | |
| 638 | redemtos → redemptos | rĕdĭmō, ēmī, ēmptum (Gaffiot also gives ēmtum) | 3 (T2 1, T4 2) : 12 (T2 1, T3 2, T4 9) | apply | Gaffiot heads -mpt- and lists -mt- as variant; approved *redēmptus* |
| 639 | septemtrionale → septentrionale | septentrĭōnālis | 0 : 5 (T2 3, T4 2) | apply | |
| 640 | septemtrionalem → septentrionalem | septentrĭōnālis | 9 (T3 4, T4 5) : 34 | apply | |
| 641 | septemtrionalis → septentrionalis | septentrĭōnālis | 6 (T2 1, T3 2, T4 3) : 38 | apply | |
| 642 | septemtrione → septentrione | septentrĭō | 20 (T1 2, T2 1, T3 1, T4 16) : 180 (T2 3, T3 43, T4 134) | apply | the T1 hits prefer *-mt-* (2 : 0); Gaffiot and the approved *septentrionali* decide |
| 643 | septemtriones → septentriones | septentrĭō | 15 (T1 1, …) : 46 (T1 1, T2 1, T2.5 5, …) | apply | |
| 644 | sumsit → sumpsit | sūmō, sūmpsī, sūmptum | 5 (T4) : 327 | apply | |
| 645 | sumtos → sumptos | sūmō | 0 : 9 | apply | |
| 646 | beniaminensium → benjaminensium (1:36–37) | n/a (name; no source knows either form) | 0 : 0 | apply | i/j, not *ad-*: j for consonantal i (brief) and the settled *Benjāmīn, Benjāmīnēnsis, -ī* (decision 46). Gap: the draft's **Beniaminea** (13:9, 34:21; preview *Beniāmīneā*) has no rule and would stay with i |

## Summary

- **46 apply, 0 don't apply, 1 doubt.**
- **Doubt: 601 *adfabor → affabor*.** Gaffiot heads *adfor*, and the corpus favours *adf-* (lemma 48 : 32),
  with only the T2 tier on the side of *aff-* (5 : 1). Only decision 37's blanket "*ad-* assimilated" supports
  the change; the settled text has no form of the verb to follow.
- **Apply, by decision 37 against Gaffiot's headword (10 rows, 602–611):** Gaffiot 2016 heads
  *adfectō, adferō, adficiō, adflō, adfluō, adgregō* with *ad-*. The approved precedents (*affici, afferemus,
  afflatus, aggregabor, aggregare*) already assimilate them, and the corpus mostly favours *aff-* (*afficere* 65 :
  30, *afflatus* 45 : 15; *adgreg-* is about even). Worth Nathan knowing that here "assimilated" and "as Gaffiot
  heads it" diverge.
- *adfletur* (5:14) is the passive of *adflō/afflō*; *affletur* is right under the rule.
- *adsciscito*: Gaffiot and L&S head *ascīscō*; the corpus leans *adsc-* overall but the T2 tier favours *asc-*. Apply.
- *apposititiorum*: no dictionary has the word in either spelling; the row follows approved sibling rows and the
  settled text. Separate open point: Gaffiot's model *suppositīcius* and the settled *īnsitīciī* use -īcius, the
  settled *appositītius* uses -ītius.
- *consumptricem*: L&S heads *consumptrix* (late Latin); Gaffiot (via the tool) has nothing. Apply.
- *Beniaminensium*: apply (i/j, decision 46). The draft's *Beniaminea* (13:9, 34:21) needs a rule of its own.
