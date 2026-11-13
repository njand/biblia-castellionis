# Macrons marked two ways in the New Testament (proposal)

Proposed 2026-11-12 (Claude), from the checklist's macron check (`data/review/nt-publication-checklist.md`). Two
passes over the whole settled New Testament (130,998 words):

1. **`python -m pipeline latin macron-check`** found 366 words to check (120 distinct forms) and 1,404 words no
   source knows. Most of the 366 are calls already decided, such as *ūsque* (67) and *ēvangelium* (47); the rest are
   below.
2. **A consistency pass** listed every word stem marked two ways somewhere in the New Testament: 273 stems. Almost
   all are different words that share letters, such as the perfect *vēnit* and the present *venit*, *lēgēs* and
   *legō*, the perfect *-ērunt* and the future perfect *-erint*, or *lectus* "bed" and *lēctus* "chosen". What is
   left is below.

## 1. Slips: one place differs from the rest of the text (10 places, 12 Apply lines)

Each one goes against the text's own majority and Gaffiot.

**Recommendation: accept all.**

**Decision:** accept all (Nathan, 2026-11-12)

1. **Luke 7:1** *Capharnāum* → *Capharnaum*: 14 times elsewhere; Gaffiot *Căpharnaum*.
   **Apply:** `Luke.7.1` la: `Caphar­nāum` → `Caphar­naum` (the USFM has a soft hyphen after *Caphar*)
2. **Luke 3:31** *Davīdis* → *Dāvīdis*: *Dāvīd-* 28 times.
   **Apply:** `Luke.3.31` la: `Davīdis` → `Dāvīdis`
3. **Mark 3:17** *Jacōbum*, *Jacōbī* → *Jācōbum*, *Jācōbī*: *Jācōb-* 61 times, and the title *Jācōbī*.
   **Apply:** `Mark.3.17` la: `Jacōbum` → `Jācōbum`
   **Apply:** `Mark.3.17` la: `Jacōbī` → `Jācōbī`
4. **John 11:43, 12:10** *Lāzāre*, *Lāzārō* → *Lāzare*, *Lāzarō*: *Lāzarus*, *Lāzarum* 13 times; Gaffiot *Lazărus*
   (the long *ā* of the first syllable is the settled text's own).
   **Apply:** `John.11.43` la: `Lāzāre` → `Lāzare`
   **Apply:** `John.12.10` la: `Lāzārō` → `Lāzarō`
5. **Matt 17:21** *jējūnium* → *jejūnium*: *jejūni-* 6 times; Gaffiot *jĕjūnium*.
   **Apply:** `Matt.17.21` la: `jējūnium` → `jejūnium`
6. **Matt 3:12** *inexstinctō* → *inexstīnctō*: *inexstīnct-* 3 times (Mark 9:43, 9:45).
   **Apply:** `Matt.3.12` la: `inexstinctō` → `inexstīnctō`
7. **John 13:33** *paulisper* → *paulīsper*: decision 42; *paulīsper* 3 times elsewhere; Gaffiot *paulīspĕr*.
   **Apply:** `John.13.33` la: `paulisper` → `paulīsper`
8. **Matt 12:5** *prōfānāre* → *profānāre*: *profān-* in Acts 24:6 and 1 Tim 6:20; Gaffiot *prŏfānō*.
   **Apply:** `Matt.12.5` la: `prōfānāre` → `profānāre`
9. **Luke 8:2** *Mariā* → *Marīā*: *Marī-* 53 times; Gaffiot *Marīa*.
   **Apply:** `Luke.8.2` la: `Mariā` → `Marīā`
10. *(withdrawn 2026-11-12: Heb 6:6 *crucīfīgant* is Gaffiot's *crŭcīfīgō*, the dative *crucī* + *fīgō*; the other 45
    *crucif-* are the ones to change, see section 2a)*
11. **Luke 4:23** *Mēdice* → *Medice*: *medic-* 6 times elsewhere; Gaffiot *mĕdĭcus*.
    **Apply:** `Luke.4.23` la: `Mēdice` → `Medice`

## 2a. *crucī fīgō*, two words, as Gaffiot and Lewis & Short advise (46 places): question for you

Gaffiot 2016 heads the verb *crŭcīfīgō ou mieux crŭcī fīgō* (read on gaffiot.fr, 2026-11-12), citing Seneca the Elder
(*Contr.* 7, 7), Valerius Maximus (6, 3, 5) and Suetonius (*Dom.* 11, 1); Lewis & Short likewise: *crucifigo … better
separated, cruci figo*. The joined word is the Christian writers' (Tertullian, Augustine, the Vulgate). The settled text
joins it 46 times (*crucifīg-* 38, *Crucifīx-* 7, Heb 6:6 *crucīfīgant*). **Recommendation: *crucī fīgō*, *crucī
fīxus* apart**, as decision 51 did for *sē ipsum*: the classical prose writers and both dictionaries agree. (Lewis &
Short marks *crucĭ*; Gaffiot's *crucī*, the dative, is the edition's authority.) Apply lines to follow your decision.

**Decision:** accept: *crucī fīgō*, *crucī fīxus* as two words, with Gaffiot's long *ī*; Apply lines in the last section (Nathan, 2026-11-12)

## 2. Names marked two ways: recommendations

The rule that decides these, in order: (1) Gaffiot's marks, where it marks (its short marks come from verse); (2) the
Greek of the New Testament, where it writes a long vowel (η → ē, ω → ō, ει → ī); (3) another dictionary that marks the
word (Wiktionary marks every long vowel of a Latin headword, so a vowel it leaves bare is a claim that it is short);
(4) the Hebrew vowel, as the edition
already reads it in *Abrāhām* (qamets), *Dāvīd* (qamets, ḥireq-yod), *Jācōb* (ḥolem): qamets in an open syllable, ṣere,
ḥolem, šureq, ḥireq-yod long; pataḥ, segol, short ḥireq, šewa short. Where none of the three speaks, no mark.

| Name | Evidence | Recommendation | Changes |
|---|---|---|---|
| Bethlehem | Greek Βηθλέεμ (η, ε, ε); Hebrew *bêṯ leḥem* (ṣere; segol, segol); Wiktionary *Bēthlehem* | ***Bēthlehem***, *Bēthlehema*, *-ā* | Matthew's 6 gain *ē*; Luke's 3 lose the last *ē* |
| Bethsaida | Greek Βηθσαϊδά (η); Hebrew *bêṯ ṣaydā* (ṣere); Gaffiot unmarked (the *e* is hidden) | ***Bēthsaida*** | 3 |
| Nazareth | Gaffiot *Nazărĕth* (both short, from verse); Greek Ναζαρέτ/-έθ (ε); the first syllable hidden before *z*: Wiktionary *Nāzareth* | ***Nāzareth***, *Nāzaretha* (by rule 3; the weakest of the table); then also *Nāzarēnus*, *Nāzaræus* (24) for one stem; or leave all unmarked | the 12 forms of the town, and the 24 of the adjectives |
| Obed | Greek Ὠβήδ (ω, η); Hebrew *ʿôḇēḏ* (ḥolem, ṣere) | ***Ōbēd*** | Matt 1:5, Luke 3:32 |
| Esrom | Greek Ἑσρώμ (ω); Hebrew *ḥeṣrôn* (segol, ḥolem) | ***Esrōm*** | Matt 1:3 (2) |
| Aminadab | Greek Ἀμιναδάβ (no long letter); Hebrew *ʿammînāḏāḇ* (pataḥ; ḥireq-yod; qamets, qamets) | ***Amīnādāb*** (by the Hebrew, as *Abrāhām*) | 3 |
| Eliacim | Greek Ἐλιακίμ (none); Hebrew *ʾelyāqîm* (segol; qamets; ḥireq-yod) | ***Eliācīm*** (by the Hebrew) | 3; neither settled form fits |
| Jairus | Wiktionary *Iaīrus* (the *a* short); Latin shortens a vowel before a vowel; Greek Ἰάϊρος (none); Hebrew *yāʾîr* (qamets) | ***Jaīrus*** | Luke 8:41 |
| Benjamin | Greek Βενιαμ(ε)ίν (ει); Hebrew *binyāmîn* (qamets, ḥireq-yod); Wiktionary *Beniāmīnus* | ***Benjāmīn-***, *Benjāmīnius* | Phil 3:5 and Genesis's 3 unmarked |
| Transjordanine | *trāns* (Gaffiot; the settled text 65 times); *Jordānēs* (Gaffiot; 16 times); the suffix *-īnus* | ***Trānsjordānīn-*** | 2 |
| Italia | Gaffiot *Ĭtălĭa*, *Ī* only in verse (for the metre); prose short | ***Italia***, unmarked | Acts 18:2 |
| narrō | Gaffiot and Wiktionary *narrō*; only the Macronizer *nārrō* (the etymology from *gnārus*, which no dictionary adopts for the hidden quantity); settled *narr-* 20 times, *nārr-* once | ***narrō*** | Heb 11:32 |

The two names decided by the Hebrew alone (*Amīnādāb*, *Eliācīm*) are the least certain: no Latin or
Greek source marks them. The others rest on Gaffiot or the Greek.

## 3. Unknown to every source

1,404 words are unknown to every source the tool reads. They are mostly names and Castellio's own coinages,
each decided in its batch and listed in that batch's record. They need no new pass.

## 4. *Nāzareth* (decided)

Lewis & Short heads *Nāzăreth*; Wiktionary *Nāzareth*; Gaffiot *Nazărĕth* (the first syllable is hidden before
*z*, so it leaves it bare). The settled text had *Nazareth-* 7 times and *Nazarēth-* 5; Luke's long *ē* goes (Gaffiot
*ĕ*, Greek ε). The adjectives *Nazarēnus* (16) and *Nazaræus* (2) were decided next (section 5): Lewis & Short
marks the first vowel of *Nāzăraeus* (the Nazirite), and gives *Nazărēnus* without it.

**Decision:** accept (Nathan, 2026-11-12: "update to Nāzareth, which is also what L&S gives")

1. **Acts 10:38** *Nazarethā* → *Nāzarethā*
   **Apply:** `Acts.10.38` la: `Nazarethā` → `Nāzarethā`
2. **John 1:45** *Nazarethā* → *Nāzarethā*
   **Apply:** `John.1.45` la: `Nazarethā` → `Nāzarethā`
3. **John 1:46** *Nazarethā* → *Nāzarethā*
   **Apply:** `John.1.46` la: `Nazarethā` → `Nāzarethā`
4. **Luke 1:26** *Nazarētham* → *Nāzaretham*
   **Apply:** `Luke.1.26` la: `Nazarētham` → `Nāzaretham`
5. **Luke 2:39** *Nazarētham* → *Nāzaretham*
   **Apply:** `Luke.2.39` la: `Nazarētham` → `Nāzaretham`
6. **Luke 2:4** *Nazarētha* → *Nāzaretha*
   **Apply:** `Luke.2.4` la: `Nazarētha` → `Nāzaretha`
7. **Luke 2:51** *Nazarētham* → *Nāzaretham*
   **Apply:** `Luke.2.51` la: `Nazarētham` → `Nāzaretham`
8. **Luke 4:16** *Nazaretham* → *Nāzaretham*
   **Apply:** `Luke.4.16` la: `Nazaretham` → `Nāzaretham`
9. **Mark 1:9** *Nazarēthā* → *Nāzarethā*
   **Apply:** `Mark.1.9` la: `Nazarēthā` → `Nāzarethā`
10. **Matt 2:23** *Nazaretha* → *Nāzaretha*
   **Apply:** `Matt.2.23` la: `Nazaretha` → `Nāzaretha`
11. **Matt 21:11** *Nazarethā* → *Nāzarethā*
   **Apply:** `Matt.21.11` la: `Nazarethā` → `Nāzarethā`
12. **Matt 4:13** *Nazarethā* → *Nāzarethā*
   **Apply:** `Matt.4.13` la: `Nazarethā` → `Nāzarethā`

## 5. *Nāzarēnus*, *Nāzaræus* (decided)

The adjectives take the town's first vowel, one stem for the name and its derivatives (Lewis & Short marks
*Nāzăraeus*; its *Nazărēnus* leaves the first syllable bare).

**Decision:** accept (Nathan, 2026-11-12: "Yes, match them")

1. **Acts 2:22** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `Acts.2.22` la: `Nazarēnum` → `Nāzarēnum`
2. **Acts 22:8** *Nazarēnus* → *Nāzarēnus*
   **Apply:** `Acts.22.8` la: `Nazarēnus` → `Nāzarēnus`
3. **Acts 24:5** *Nazaræōrum* → *Nāzaræōrum*
   **Apply:** `Acts.24.5` la: `Nazaræōrum` → `Nāzaræōrum`
4. **Acts 26:9** *Nazarēnī* → *Nāzarēnī*
   **Apply:** `Acts.26.9` la: `Nazarēnī` → `Nāzarēnī`
5. **Acts 3:6** *Nazarēnī* → *Nāzarēnī*
   **Apply:** `Acts.3.6` la: `Nazarēnī` → `Nāzarēnī`
6. **Acts 4:10** *Nazarēnī* → *Nāzarēnī*
   **Apply:** `Acts.4.10` la: `Nazarēnī` → `Nāzarēnī`
7. **Acts 6:14** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `Acts.6.14` la: `Nazarēnum` → `Nāzarēnum`
8. **John 18:5** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `John.18.5` la: `Nazarēnum` → `Nāzarēnum`
9. **John 18:7** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `John.18.7` la: `Nazarēnum` → `Nāzarēnum`
10. **Luke 18:37** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `Luke.18.37` la: `Nazarēnum` → `Nāzarēnum`
11. **Luke 24:19** *Nazarēnō* → *Nāzarēnō*
   **Apply:** `Luke.24.19` la: `Nazarēnō` → `Nāzarēnō`
12. **Luke 4:34** *Nazarēne* → *Nāzarēne*
   **Apply:** `Luke.4.34` la: `Nazarēne` → `Nāzarēne`
13. **Mark 1:24** *Nazarēne* → *Nāzarēne*
   **Apply:** `Mark.1.24` la: `Nazarēne` → `Nāzarēne`
14. **Mark 10:47** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `Mark.10.47` la: `Nazarēnum` → `Nāzarēnum`
15. **Mark 14:67** *Nazarēnō* → *Nāzarēnō*
   **Apply:** `Mark.14.67` la: `Nazarēnō` → `Nāzarēnō`
16. **Mark 16:6** *Nazarēnum* → *Nāzarēnum*
   **Apply:** `Mark.16.6` la: `Nazarēnum` → `Nāzarēnum`
17. **Matt 2:23** *Nazaræum* → *Nāzaræum*
   **Apply:** `Matt.2.23` la: `Nazaræum` → `Nāzaræum`
18. **Matt 26:71** *Nazarēnō* → *Nāzarēnō*
   **Apply:** `Matt.26.71` la: `Nazarēnō` → `Nāzarēnō`

## 6. *crucī fīgō* as two words (decided; Apply lines for section 2a)

Every form of the joined verb, with Gaffiot's long *ī* of the dative *crucī*.

**Decision:** accept (Nathan, 2026-11-12)

1. **1Cor 1:13** *crucifīxus* → *crucī fīxus*
   **Apply:** `1Cor.1.13` la: `crucifīxus` → `crucī fīxus`
2. **1Cor 1:23** *crucifīxum* → *crucī fīxum*
   **Apply:** `1Cor.1.23` la: `crucifīxum` → `crucī fīxum`
3. **1Cor 2:2** *crucifīxum* → *crucī fīxum*
   **Apply:** `1Cor.2.2` la: `crucifīxum` → `crucī fīxum`
4. **1Cor 2:8** *crucifīxissent* → *crucī fīxissent*
   **Apply:** `1Cor.2.8` la: `crucifīxissent` → `crucī fīxissent`
5. **2Cor 13:4** *crucifīxus* → *crucī fīxus*
   **Apply:** `2Cor.13.4` la: `crucifīxus` → `crucī fīxus`
6. **Acts 4:10** *crucifīxistis* → *crucī fīxistis*
   **Apply:** `Acts.4.10` la: `crucifīxistis` → `crucī fīxistis`
7. **Gal 2:20** *Crucifīxus* → *Crucī fīxus*
   **Apply:** `Gal.2.20` la: `Crucifīxus` → `Crucī fīxus`
8. **Gal 3:1** *crucifīxus* → *crucī fīxus*
   **Apply:** `Gal.3.1` la: `crucifīxus` → `crucī fīxus`
9. **Gal 5:24** *crucifīxērunt* → *crucī fīxērunt*
   **Apply:** `Gal.5.24` la: `crucifīxērunt` → `crucī fīxērunt`
10. **Gal 6:14** *crucifīxus* → *crucī fīxus*
   **Apply:** `Gal.6.14` la: `crucifīxus` → `crucī fīxus`
11. **Heb 6:6** *crucīfīgant* → *crucī fīgant*
   **Apply:** `Heb.6.6` la: `crucīfīgant` → `crucī fīgant`
12. **John 19:6** *Crucifīge* → *Crucī fīge*
   **Apply:** `John.19.6` la: `Crucifīge` → `Crucī fīge`
13. **John 19:6** *crucifīge* → *crucī fīge*
   **Apply:** `John.19.6` la: `crucifīge` → `crucī fīge`
14. **John 19:6** *crucifīgite* → *crucī fīgite*
   **Apply:** `John.19.6` la: `crucifīgite` → `crucī fīgite`
15. **John 19:10** *crucifīgendī* → *crucī fīgendī*
   **Apply:** `John.19.10` la: `crucifīgendī` → `crucī fīgendī`
16. **John 19:15** *crucifīge* → *crucī fīge*
   **Apply:** `John.19.15` la: `crucifīge` → `crucī fīge`
17. **John 19:15** *crucifīgam* → *crucī fīgam*
   **Apply:** `John.19.15` la: `crucifīgam` → `crucī fīgam`
18. **John 19:16** *crucifīgendum* → *crucī fīgendum*
   **Apply:** `John.19.16` la: `crucifīgendum` → `crucī fīgendum`
19. **John 19:18** *crucifīxērunt* → *crucī fīxērunt*
   **Apply:** `John.19.18` la: `crucifīxērunt` → `crucī fīxērunt`
20. **John 19:32** *crucifīxī* → *crucī fīxī*
   **Apply:** `John.19.32` la: `crucifīxī` → `crucī fīxī`
21. **John 19:41** *crucifīxus* → *crucī fīxus*
   **Apply:** `John.19.41` la: `crucifīxus` → `crucī fīxus`
22. **Luke 23:21** *Crucifīge* → *Crucī fīge*
   **Apply:** `Luke.23.21` la: `Crucifīge` → `Crucī fīge`
23. **Luke 23:21** *crucifīge* → *crucī fīge*
   **Apply:** `Luke.23.21` la: `crucifīge` → `crucī fīge`
24. **Luke 23:23** *crucifīgerētur* → *crucī fīgerētur*
   **Apply:** `Luke.23.23` la: `crucifīgerētur` → `crucī fīgerētur`
25. **Luke 23:33** *crucifīxērunt* → *crucī fīxērunt*
   **Apply:** `Luke.23.33` la: `crucifīxērunt` → `crucī fīxērunt`
26. **Luke 24:7** *crucifīgī* → *crucī fīgī*
   **Apply:** `Luke.24.7` la: `crucifīgī` → `crucī fīgī`
27. **Mark 15:13** *Crucifīge* → *Crucī fīge*
   **Apply:** `Mark.15.13` la: `Crucifīge` → `Crucī fīge`
28. **Mark 15:14** *Crucifīge* → *Crucī fīge*
   **Apply:** `Mark.15.14` la: `Crucifīge` → `Crucī fīge`
29. **Mark 15:15** *crucifīgendum* → *crucī fīgendum*
   **Apply:** `Mark.15.15` la: `crucifīgendum` → `crucī fīgendum`
30. **Mark 15:20** *crucifīgendum* → *crucī fīgendum*
   **Apply:** `Mark.15.20` la: `crucifīgendum` → `crucī fīgendum`
31. **Mark 15:24** *crucifīxō* → *crucī fīxō*
   **Apply:** `Mark.15.24` la: `crucifīxō` → `crucī fīxō`
32. **Mark 15:25** *crucifīxērunt* → *crucī fīxērunt*
   **Apply:** `Mark.15.25` la: `crucifīxērunt` → `crucī fīxērunt`
33. **Mark 15:27** *crucifīxērunt* → *crucī fīxērunt*
   **Apply:** `Mark.15.27` la: `crucifīxērunt` → `crucī fīxērunt`
34. **Mark 15:32** *crucifīxī* → *crucī fīxī*
   **Apply:** `Mark.15.32` la: `crucifīxī` → `crucī fīxī`
35. **Mark 16:6** *crucifīxum* → *crucī fīxum*
   **Apply:** `Mark.16.6` la: `crucifīxum` → `crucī fīxum`
36. **Matt 20:19** *crucifīgendum* → *crucī fīgendum*
   **Apply:** `Matt.20.19` la: `crucifīgendum` → `crucī fīgendum`
37. **Matt 26:2** *crucifīgendum* → *crucī fīgendum*
   **Apply:** `Matt.26.2` la: `crucifīgendum` → `crucī fīgendum`
38. **Matt 27:22** *Crucifīgātur* → *Crucī fīgātur*
   **Apply:** `Matt.27.22` la: `Crucifīgātur` → `Crucī fīgātur`
39. **Matt 27:23** *Crucifīgātur* → *Crucī fīgātur*
   **Apply:** `Matt.27.23` la: `Crucifīgātur` → `Crucī fīgātur`
40. **Matt 27:26** *crucifīgendum* → *crucī fīgendum*
   **Apply:** `Matt.27.26` la: `crucifīgendum` → `crucī fīgendum`
41. **Matt 27:35** *crucifīxō* → *crucī fīxō*
   **Apply:** `Matt.27.35` la: `crucifīxō` → `crucī fīxō`
42. **Matt 27:38** *crucifīguntur* → *crucī fīguntur*
   **Apply:** `Matt.27.38` la: `crucifīguntur` → `crucī fīguntur`
43. **Matt 27:44** *crucifīxī* → *crucī fīxī*
   **Apply:** `Matt.27.44` la: `crucifīxī` → `crucī fīxī`
44. **Matt 28:5** *crucifīxum* → *crucī fīxum*
   **Apply:** `Matt.28.5` la: `crucifīxum` → `crucī fīxum`
45. **Rev 11:8** *crucifīxus* → *crucī fīxus*
   **Apply:** `Rev.11.8` la: `crucifīxus` → `crucī fīxus`
46. **Rom 6:6** *crucifīxum* → *crucī fīxum*
   **Apply:** `Rom.6.6` la: `crucifīxum` → `crucī fīxum`

## 7. The names of section 2 (decided)

Every form in the settled text, Old Testament included (decision 46: one form of a name).

**Decision:** accept (Nathan, 2026-11-12)

1. **Gen 35:19** *Bēthlehēma* → *Bēthlehema* (Bēthlehem)
   **Apply:** `Gen.35.19` la: `Bēthlehēma` → `Bēthlehema`
2. **Gen 48:7** *Bethlehemæ* → *Bēthlehemæ* (Bēthlehem)
   **Apply:** `Gen.48.7` la: `Bethlehemæ` → `Bēthlehemæ`
3. **John 7:42** *Bēthlehēmā* → *Bēthlehemā* (Bēthlehem)
   **Apply:** `John.7.42` la: `Bēthlehēmā` → `Bēthlehemā`
4. **Luke 2:4** *Bēthlehēma* → *Bēthlehema* (Bēthlehem)
   **Apply:** `Luke.2.4` la: `Bēthlehēma` → `Bēthlehema`
5. **Luke 2:15** *Bēthlehēmam* → *Bēthlehemam* (Bēthlehem)
   **Apply:** `Luke.2.15` la: `Bēthlehēmam` → `Bēthlehemam`
6. **Matt 2:1** *Bethlehemæ* → *Bēthlehemæ* (Bēthlehem)
   **Apply:** `Matt.2.1` la: `Bethlehemæ` → `Bēthlehemæ`
7. **Matt 2:5** *Bethlehemæ* → *Bēthlehemæ* (Bēthlehem)
   **Apply:** `Matt.2.5` la: `Bethlehemæ` → `Bēthlehemæ`
8. **Matt 2:6** *Bethlehema* → *Bēthlehema* (Bēthlehem)
   **Apply:** `Matt.2.6` la: `Bethlehema` → `Bēthlehema`
9. **Matt 2:8** *Bethlehemam* → *Bēthlehemam* (Bēthlehem)
   **Apply:** `Matt.2.8` la: `Bethlehemam` → `Bēthlehemam`
10. **Matt 2:16** *Bethlehemæ* → *Bēthlehemæ* (Bēthlehem)
   **Apply:** `Matt.2.16` la: `Bethlehemæ` → `Bēthlehemæ`
11. **John 1:44** *Bethsaidā* → *Bēthsaidā* (Bēthsaida)
   **Apply:** `John.1.44` la: `Bethsaidā` → `Bēthsaidā`
12. **Luke 9:10** *Bethsaida* → *Bēthsaida* (Bēthsaida)
   **Apply:** `Luke.9.10` la: `Bethsaida` → `Bēthsaida`
13. **Matt 11:21** *Bethsaidan* → *Bēthsaidan* (Bēthsaida)
   **Apply:** `Matt.11.21` la: `Bethsaidan` → `Bēthsaidan`
14. **Luke 3:32** *Obēdīs* → *Ōbēdīs* (Ōbēd)
   **Apply:** `Luke.3.32` la: `Obēdīs` → `Ōbēdīs`
15. **Matt 1:5** *Ōbedem* → *Ōbēdem* (Ōbēd)
   **Apply:** `Matt.1.5` la: `Ōbedem` → `Ōbēdem`
16. **Matt 1:5** *Ōbed* → *Ōbēd* (Ōbēd)
   **Apply:** `Matt.1.5` la: `Ōbed ` → `Ōbēd `
17. **Matt 1:3** *Esromum* → *Esrōmum* (Esrōm)
   **Apply:** `Matt.1.3` la: `Esromum` → `Esrōmum`
18. **Matt 1:3** *Esromus* → *Esrōmus* (Esrōm)
   **Apply:** `Matt.1.3` la: `Esromus` → `Esrōmus`
19. **Luke 3:33** *Aminadābī* → *Amīnādābī* (Amīnādāb)
   **Apply:** `Luke.3.33` la: `Aminadābī` → `Amīnādābī`
20. **Matt 1:4** *Amīnadābum* → *Amīnādābum* (Amīnādāb)
   **Apply:** `Matt.1.4` la: `Amīnadābum` → `Amīnādābum`
21. **Matt 1:4** *Amīnadābus* → *Amīnādābus* (Amīnādāb)
   **Apply:** `Matt.1.4` la: `Amīnadābus` → `Amīnādābus`
22. **Luke 3:30** *Ēliacīmī* → *Eliācīmī* (Eliācīm)
   **Apply:** `Luke.3.30` la: `Ēliacīmī` → `Eliācīmī`
23. **Matt 1:13** *Elīacimum* → *Eliācīmum* (Eliācīm)
   **Apply:** `Matt.1.13` la: `Elīacimum` → `Eliācīmum`
24. **Matt 1:13** *Elīacimus* → *Eliācīmus* (Eliācīm)
   **Apply:** `Matt.1.13` la: `Elīacimus` → `Eliācīmus`
25. **Luke 8:41** *Jairus* → *Jaīrus* (Jaīrus)
   **Apply:** `Luke.8.41` la: `Jairus` → `Jaīrus`
26. **Gen 35:18** *Benjaminem* → *Benjāmīnem* (Benjāmīn)
   **Apply:** `Gen.35.18` la: `Benjaminem` → `Benjāmīnem`
27. **Gen 35:24** *Benjaminem* → *Benjāmīnem* (Benjāmīn)
   **Apply:** `Gen.35.24` la: `Benjaminem` → `Benjāmīnem`
28. **Gen 46:19** *Benjamin* → *Benjāmīn* (Benjāmīn)
   **Apply:** `Gen.46.19` la: `Benjamin` → `Benjāmīn`
29. **Phil 3:5** *Benjaminiæ* → *Benjāmīniæ* (Benjāmīn)
   **Apply:** `Phil.3.5` la: `Benjaminiæ` → `Benjāmīniæ`
30. **Mark 3:8** *Transjordānīnō* → *Trānsjordānīnō* (Trānsjordānīn)
   **Apply:** `Mark.3.8` la: `Transjordānīnō` → `Trānsjordānīnō`
31. **Matt 4:25** *Transjordanīnā* → *Trānsjordānīnā* (Trānsjordānīn)
   **Apply:** `Matt.4.25` la: `Transjordanīnā` → `Trānsjordānīnā`
32. **Acts 18:2** *Ītaliā* → *Italiā* (Italia)
   **Apply:** `Acts.18.2` la: `Ītaliā` → `Italiā`
33. **Heb 11:32** *nārrantem* → *narrantem* (narrō)
   **Apply:** `Heb.11.32` la: `nārrantem` → `narrantem`
