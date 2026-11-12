# Classical spellings: *sē ipsum*, *epistula*, the perfects of *eō*'s compounds

Proposed 2026-11-12 (Claude), at Nathan's question; **accepted by Nathan the same day** (decision 51). The evidence is
the tiered Latin Library corpus (`python -m pipeline latin attest`; T1 = the classical authors) and Gaffiot 2016, as in
decisions 19 and 42. Word rules for future drafts are in `data/rules/orthography.tsv`.

## 1. *sē ipsum*, *tē ipsum*, *mē ipsum* as two words (10)

Classical Latin writes the reflexive and *ipse* apart: *se ipsum* 473 hits (Cicero 48), *seipsum* 278, none classical
(Aquinas 138, Erasmus 26); *te ipsum* 251 (Cicero 66) / *teipsum* 67, none classical; *me ipsum* 170 (Cicero 53) /
*meipsum* 26, none classical. The joined forms came from Wikisource and 1573 (which prints *seipsum*, *teipsum*); no
rule met them. Acts 26:1 had both, *prō tē ipsō* and *seipsum dēfendit*.

**Decision:** accept (Nathan, 2026-11-12; decision 51)

1. **2Cor 11:7** *meipsum* → *mē ipsum*
   **Apply:** `2Cor.11.7` la: `meipsum` → `mē ipsum`
2. **Acts 1:3** *seipsum* → *sē ipsum*
   **Apply:** `Acts.1.3` la: `seipsum` → `sē ipsum`
3. **Acts 16:27** *seipsum* → *sē ipsum*
   **Apply:** `Acts.16.27` la: `seipsum` → `sē ipsum`
4. **Acts 26:1** *seipsum* → *sē ipsum*
   **Apply:** `Acts.26.1` la: `seipsum` → `sē ipsum`
5. **Gal 5:14** *teipsum* → *tē ipsum*
   **Apply:** `Gal.5.14` la: `teipsum` → `tē ipsum`
6. **Jas 2:8** *teipsum* → *tē ipsum*
   **Apply:** `Jas.2.8` la: `teipsum` → `tē ipsum`
7. **Rom 2:1** *teipsum* → *tē ipsum*
   **Apply:** `Rom.2.1` la: `teipsum` → `tē ipsum`
8. **Rom 2:21** *teipsum* → *tē ipsum*
   **Apply:** `Rom.2.21` la: `teipsum` → `tē ipsum`
9. **Rom 13:9** *teipsum* → *tē ipsum*
   **Apply:** `Rom.13.9` la: `teipsum` → `tē ipsum`
10. **Rom 14:22** *seipsum* → *sē ipsum*
   **Apply:** `Rom.14.22` la: `seipsum` → `sē ipsum`

## 2. *epistula* for *epistola* (24, and the 42 title lines)

*epistula* is the classical spelling: T1 142 hits (Cicero 150 in all) against *epistola* 2 (Cicero 0); *epistulam* T1
155 / *epistolam* 1; *epistulae* 54 / 0. *epistola* is later (Erasmus 267). Gaffiot 2016 knows both; decision 42 chose
the classical spelling in the same case (*cōntiō*, *condiciō*). The 42 title lines (`\toc1`, `\mt1` of Romans–Jude, 21 books) were
changed with the verses, by hand (they are not verse text).

**Decision:** accept (Nathan, 2026-11-12; decision 51)

1. **1Cor 5:9** *epistolam* → *epistulam*
   **Apply:** `1Cor.5.9` la: `epistolam` → `epistulam`
2. **1Cor 16:3** *epistolās* → *epistulās*
   **Apply:** `1Cor.16.3` la: `epistolās` → `epistulās`
3. **1Thess 5:27** *epistola* → *epistula*
   **Apply:** `1Thess.5.27` la: `epistola` → `epistula`
4. **2Cor 3:1** *epistolīs* → *epistulīs*
   **Apply:** `2Cor.3.1` la: `epistolīs` → `epistulīs`
5. **2Cor 3:2** *Epistola* → *Epistula*
   **Apply:** `2Cor.3.2` la: `Epistola` → `Epistula`
6. **2Cor 3:3** *epistolam* → *epistulam*
   **Apply:** `2Cor.3.3` la: `epistolam` → `epistulam`
7. **2Cor 7:8** *epistolam* → *epistulam*
   **Apply:** `2Cor.7.8` la: `epistolam` → `epistulam`
8. **2Cor 7:8** *epistola* → *epistula*
   **Apply:** `2Cor.7.8` la: `sī epistola illa` → `sī epistula illa`
9. **2Cor 10:9** *epistolās* → *epistulās*
   **Apply:** `2Cor.10.9` la: `epistolās` → `epistulās`
10. **2Cor 10:10** *epistolæ* → *epistulæ*
   **Apply:** `2Cor.10.10` la: `epistolæ` → `epistulæ`
11. **2Cor 10:11** *epistolās* → *epistulās*
   **Apply:** `2Cor.10.11` la: `epistolās` → `epistulās`
12. **2Pet 3:16** *epistolīs* → *epistulīs*
   **Apply:** `2Pet.3.16` la: `epistolīs` → `epistulīs`
13. **2Thess 2:2** *epistolā* → *epistulā*
   **Apply:** `2Thess.2.2` la: `epistolā` → `epistulā`
14. **2Thess 2:15** *epistolā* → *epistulā*
   **Apply:** `2Thess.2.15` la: `epistolā` → `epistulā`
15. **2Thess 3:14** *epistolam* → *epistulam*
   **Apply:** `2Thess.3.14` la: `epistolam` → `epistulam`
16. **2Thess 3:17** *epistolīs* → *epistulīs*
   **Apply:** `2Thess.3.17` la: `epistolīs` → `epistulīs`
17. **Acts 9:2** *epistolās* → *epistulās*
   **Apply:** `Acts.9.2` la: `epistolās` → `epistulās`
18. **Acts 15:30** *epistolam* → *epistulam*
   **Apply:** `Acts.15.30` la: `epistolam` → `epistulam`
19. **Acts 22:5** *epistolās* → *epistulās*
   **Apply:** `Acts.22.5` la: `epistolās` → `epistulās`
20. **Acts 23:25** *epistolam* → *epistulam*
   **Apply:** `Acts.23.25` la: `epistolam` → `epistulam`
21. **Acts 23:33** *epistolā* → *epistulā*
   **Apply:** `Acts.23.33` la: `epistolā` → `epistulā`
22. **Col 4:16** *epistola,* → *epistula,*
   **Apply:** `Col.4.16` la: `epistola,` → `epistula,`
23. **Col 4:16** *epistolam* → *epistulam*
   **Apply:** `Col.4.16` la: `epistolam` → `epistulam`
24. **Rom 16:22** *epistolam* → *epistulam*
   **Apply:** `Rom.16.22` la: `epistolam` → `epistulam`

## 3. The perfects of *eō*'s compounds in *-iērunt*, *-iit* (3)

Decision 19 settles *-īv-* perfects form by form; these three had no row and came from the drafts unchanged. The corpus:
*introierunt* 34 / *introiverunt* 0; *exierunt* 125 (Cicero 7) / *exiverunt* 0; *obiit* 430 / *obivit* 5. The text
itself has *exiērunt* 2, *exiit* 18, *obiit* 4. (*excīvērunt*, *obdormīvit*, *exaudīvit* are other verbs.)

**Decision:** accept (Nathan, 2026-11-12; decision 51)

1. **2John 1:7** *introīvērunt* → *introiērunt*
   **Apply:** `2John.1.7` la: `introīvērunt` → `introiērunt`
2. **Acts 15:41** *obīvit* → *obiit*
   **Apply:** `Acts.15.41` la: `obīvit` → `obiit`
3. **Exod 16:27** *exīvērunt* → *exiērunt*
   **Apply:** `Exod.16.27` la: `exīvērunt` → `exiērunt`
