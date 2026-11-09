# John 5–21, stage 2: Wikisource against the printings

Proposed 2026-11-08. Stage 1 made **`text/draft/JHN.usfm`**: Wikisource's John 5–21 (KJV numbering; all 17
chapters at the KJV count, 713 verses) with the BSB's paragraphs. Collated word by word against 1573, 1556, 1758,
1681, 1715, 1747 and 1750 (`python -m pipeline collate John 5-21`; `data/calibration/John5-21-collation.tsv`).

The 110 places where 1573 and another printing agree against Wikisource were each judged: most are spellings the
rules handle (*nunquam*, *intelligo*, *quicunque*, *monimentum*, *extitit*), word division (*seipso*, *Vtaudio*),
or forms kept by decision (*iit*, *iī*, *iērō*: decision 26; *abīsse*, *petīstis*: decision 19). Kept as your
settled text has them: 19:39 *murræ* (your Matt 2:11 *murram*; 1573 *myrrhæ*), 18:22 *Sīcine*. Of the 584 places
where only 1573's OCR differs, those where 1573's word is a real word the lexicon knows (about 110) were read in
context and the eight that could be readings cropped: one proved real (10:19); the others were misreadings
(5:7, 17:22 *fuimus*, 17:23, 18:12, 18:37, 20:26) or a margin note (7:50 *Nicodemus Iesum defendit*). 19:13's
*a* is a note marker.

**Every item below was read on the 1573 page image** (canvas given; crops in `sources/mdz-1573/crops/`).

## 1. Wikisource slips: 1573 and the other printings agree against it (18)

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08; every item read on the image)

1. **John 5:21** *suscitat at vivificat* → *ac*. 1573 *ſuſcitat, ac viuificat* (canvas 818); 1758, 1715, 1750.
   **Apply:** `John.5.21` la: `suscitat, at vivificat` → `suscitat, ac vivificat`
2. **John 5:39** *in ei vos* → *in eis* (the *litterās*). 1573 *in eis vos* (818); 1556, 1758, 1715, 1750.
   **Apply:** `John.5.39` la: `in ei vos` → `in eis vos`
3. **John 6:2** *quod viderant* → *viderent*. 1573 *quod viderent* (818); 1556, 1758, 1747, 1750.
   **Apply:** `John.6.2` la: `quod viderant` → `quod viderent`
4. **John 6:62** *Quid si videatis* → *videritis*. 1573 *Quid ſi videritis* (819); 1758, 1681.
   **Apply:** `John.6.62` la: `si videatis` → `si videritis`
5. **John 7:43** *discidium* → *dissidium* (disagreement; *discidium* is separation). 1573 *diſsidium* (820); 1750,
   1758 *disidium*.
   **Apply:** `John.7.43` la: `discidium` → `dissidium`
6. **John 10:19** *discidium* → *dissidium*, as 7:43. 1573 *diſsidium* (823). Here only 1573 differs; the
   other printings were not checked for this verse.
   **Apply:** `John.10.19` la: `discidium` → `dissidium`
7. **John 8:46** *cur me vos non creditis* → *mihi* (*crēdō* takes the dative). 1573 *cur mihi vos* (821); 1758,
   1681, 1747, 1750.
   **Apply:** `John.8.46` la: `cur me vos` → `cur mihi vos`
8. **John 10:37** *mihi ne credito* → *credite* (to the crowd). 1573 *mihi ne credite* (823); 1758, 1715, 1747, 1750.
   **Apply:** `John.10.37` la: `ne credito` → `ne credite`
9. **John 11:49** *sic eos verba facit* → *sic ad eos*. 1573 *ſic ad eos verba facit* (824); 1556, 1758, 1750.
   **Apply:** `John.11.49` la: `sic eos verba` → `sic ad eos verba`
10. **John 12:22** *Philippus Jesus dicunt* → *Jesu* (dative). 1573 *Philippus Ieſu dicunt* (825); 1758, 1747.
    **Apply:** `John.12.22` la: `Philippus Jesus dicunt` → `Philippus Jesu dicunt`
11. **John 14:7** *jam nunc cognoscitis* → *jam nunc eum cognoscitis* (a word missing). 1573 *iam nunc eum
    cognoſcitis* (826); 1758, 1747.
    **Apply:** `John.14.7` la: `jam nunc cognoscitis` → `jam nunc eum cognoscitis`
12. **John 14:28** *proficisci quo pater* → *quod*. 1573 *proficiſci, quòd pater* (826); 1556, 1758, 1747.
    **Apply:** `John.14.28` la: `quo pater` → `quod pater`
13. **John 15:6** *projectus arescit* → *aruit*. 1573 *proiectus aruit* (827); 1758, 1715, 1750.
    **Apply:** `John.15.6` la: `arescit` → `aruit`
14. **John 18:9** *dedisti, ego nullum* → *eorum ego nullum* (a word missing). 1573 *dediſti, eorum ego nullum
    perdidi* (828); 1758.
    **Apply:** `John.18.9` la: `ego nullum perdidi` → `eorum ego nullum perdidi`
15. **John 18:18** *erant enim frigus* → *erat*. 1573 *(erat enim frigus)* (829); 1758, 1747.
    **Apply:** `John.18.18` la: `erant enim frigus` → `erat enim frigus`
16. **John 18:21** *quid iis locutus sum* → *sim* (an indirect question). 1573 *quid eis locutus ſim* (829); 1556,
    1758, 1681.
    **Apply:** `John.18.21` la: `locutus sum` → `locutus sim`
17. **John 19:12** *non est Caesaris amicus* → *es* (to Pilate). 1573 *non es Cæſaris amicus* (829); 1758, 1747, 1750.
    **Apply:** `John.19.12` la: `non est Caesaris` → `non es Caesaris`
18. **John 21:5** *numquid pulmentarii* → *numquid edulii*. 1573 *nunquid edulij* (831); 1758, 1747; as Luke 24:41.
    **Apply:** `John.21.5` la: `numquid pulmentarii` → `numquid edulii`

## 2. Forms: the base edition's (3)

Both forms are classical; the base edition's is proposed (decision 24), as 1573's *misertus* in Luke 15:20.

**Decision:** accept (Claude, under the standing rule of decision 30, 2026-11-08)

19. **John 9:7** *ut iret lavatum* → *lotum* (supine). 1573 *vt iret lotum* (822); 1758, 1681, 1747, 1750.
    **Apply:** `John.9.7` la: `iret lavatum` → `iret lotum`
20. **John 12:29** *exstitisse tonitrus* → *tonitru*. 1573 *extitiſſe tonitru* (825); 1556, 1758, 1715, 1750.
    **Apply:** `John.12.29` la: `tonitrus` → `tonitru`
21. **John 13:10** *Qui lautus est* → *lotus*. 1573 *Qui lotus eſt* (825); 1758, 1747, 1750.
    **Apply:** `John.13.10` la: `Qui lautus` → `Qui lotus`
