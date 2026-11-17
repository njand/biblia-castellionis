# -īnus vs -ĭnus: Gaffiot's quantities and the fixes

Scope: `text/draft/NUM.preview.usfm` and the settled `text/*.usfm` (Gen, Exod, Lev, NT; not FRT). Words found by a
Python scan (`scratchpad/num35/inus/scan.py`, macrons stripped, soft hyphens removed), every word ending
-in-/-īn- + a case ending; nouns and verbs that merely end in -in- (*dominus, asinus, terminus, facinus, sinus,
pāgina, doctrīna, rēgīna, gallīna, concubīna, piscīna, rapīna, latrīna, farīna, patina, sarcina, trutina, lāmina,
catīnus, pulvīnus, pistrīnum*, the -minī verb forms, -tūdine, -mine …) set aside. Quantities from
`python -m pipeline latin macron` (G = Gaffiot 2016 headword; only the quantity is cited), else Lewis & Short.

## 1. Gaffiot's exceptions to -īnus (adjectives in these books)

| Word in text | Gaffiot headword quantity | Class | Marked now |
|---|---|---|---|
| cedrinus | cĕdrĭnus | material, Greek κέδρινος | short (all 30) ✓ |
| byssinus | byssĭnus | material, Greek βύσσινος | short ✓ |
| coccinus | coccĭnus | material, Greek κόκκινος | short ✓ |
| hyacinthinus | hyăcinthĭnus | material/colour, Greek ὑακίνθινος | short ✓ |
| onychinus | ŏnychĭnus | material, Greek ὀνύχινος | short ✓ |
| terebinthinus | tĕrĕbinthĭnus | material, Greek τερεβίνθινος | short ✓ |
| thyinus (Rev 18:12) | thyĭnus (L&S thȳĭnus) | material, Greek θύϊνος | short ✓ |
| murrinus (*murrinum*) | under murrhĭnus / myrrhĭnus (no entry *murrinus*; L&S murrĭnus) | material, Greek μύρρινος | short ✓ |
| crastinus | crastĭnus | time adjective in -tĭnus (Latin) | short ✓ (*crāstinum*) |
| pristinus | prīstĭnus (Gaffiot also lists a variant pristīnus) | time adjective in -tĭnus | short ✓ (*prīstinam, prīstinum*) |
| geminus | gĕmĭnus | not the suffix (root *gemin-*) | short ✓ |
| (protinus, adverb) | prōtĭnus | adverb, not an adjective | short ✓ |
| (fāginus, not in these books) | fāgĭnus | material, Greek φήγινος | — |

So the exceptions are (a) material adjectives borrowed from Greek -ινος, and (b) the Latin time adjectives
crastĭnus, prīstĭnus (the -tĭnus type; contrast vespertīnus, mātūtīnus, both long in Gaffiot). Not every
material adjective is short: Gaffiot has **sapphīrīnus**, **cĭlĭcīnus**, **cămēlīnus** long.

## 2. Adjectives Gaffiot marks -īnus (all already marked long here)

| Lemma | Gaffiot | Class |
|---|---|---|
| adulterīnus | ădultĕrīnus | other (Latin) |
| aquilīnus | ăquĭlīnus | animal |
| arietīnus | ărĭĕtīnus | animal |
| bovīnus | bŏvīnus | animal |
| camēlīnus | cămēlīnus | animal |
| caprīnus | caprīnus | animal |
| cilicīnus | cĭlĭcīnus | material (goat-hair) |
| dīvīnus | dīvīnus | other |
| ferīnus | fĕrīnus | animal |
| genuīnus | gĕnŭīnus | other |
| intestīnus | intestīnus | other |
| leōnīnus | lĕōnīnus | animal |
| lībertīnus | lībertīnus | other |
| marīnus | mărīnus | place |
| mātūtīnus | mātūtīnus | time |
| morticīnus | mortĭcīnus | other |
| ovīnus | ŏvīnus | animal |
| Palæstīnus | Pălæstīnus | gentile/place |
| peregrīnus | pĕrĕgrīnus | place |
| resupīnus | rĕsŭpīnus | other |
| sapphīrīnus | sapphīrīnus | material (long, against the Greek-material pattern) |
| ursīnus | ursīnus | animal |
| vespertīnus | vespertīnus | time |
| vīcīnus | vīcīnus | place |
| vīperīnus | vīpĕrīnus | animal |
| bīnī, trīnī, quīnī | bīnī, trīnī, quīnī | distributives (long; not the -īnus suffix) |

Not in Gaffiot, marked long, class gentile/place (→ -īnus): *Alexandrīnus* (W, M: Alexandrīnus; no Gaffiot or
L&S line returned), *Adramyttīnus* (Acts 27:2; no source; Greek Ἀδραμυττηνός has η), *Ephesīnus* (no source),
*Isaacīnus* (no source), *Trānsjordānīnus* (no source). All already long.

Unresolved: **castanīnīs** (Gen 30:37; marked long). No source knows *castaninus* (not Gaffiot, L&S, W or M;
Gaffiot has castănĕus). It is a material adjective (chestnut), and by Gaffiot's pattern for tree/material
adjectives from Greek (cĕdrĭnus, tĕrĕbinthĭnus, fāgĭnus) it would be short; but no Greek καστάνινος was checked and
Latin animal/material -īnus also exists. Flag for Nathan; no fix proposed.

No word is marked long here that Gaffiot has short.

## 3. Hebrew tribal and clan adjectives (no source knows any of them)

Checked with `latin macron` (all "no source knows this form"): Gadinus, Rubeninus, Cahathinus, Galaadinus,
Amraminus, Ephraiminus, Enacinus (and the rest are the same type). Class: gentile adjectives from a person or
place name, like Gaffiot's gentile -īnus (Latīnus, Sabīnus, Tărentīnus) and like *Palæstīnus*, *Alexandrīnus*
in these books → **-īnus**. Numbers marked them short because of the settled Exod 6:14 *Rūbēninæ* (its forms
decisions cite it); that settled form is itself the one exception.

## 4. Fixes: occurrences marked short that should be -īn-

### Numbers (`text/draft/NUM.preview.usfm`; the decisions are in `data/decisions/Num.forms.tsv`) — 48

| Verse | Now | Should be |
|---|---|---|
| Num.1.5 | Rūbēninā | Rūbēnīnā |
| Num.1.14 | Gadinā | Gadīnā |
| Num.3.27 | Amrāmina | Amrāmīna |
| Num.3.27 | Cahathinæ | Cahathīnæ |
| Num.3.27 | Ozīēlina | Ozīēlīna |
| Num.3.29 | Cahathinī | Cahathīnī |
| Num.4.2 | Cahathinōrum | Cahathīnōrum |
| Num.4.4 | Cahathinōrum | Cahathīnōrum |
| Num.4.15 | Cahathinī | Cahathīnī |
| Num.4.15 | Cahathinōrum | Cahathīnōrum |
| Num.4.17 | Cahathinārum | Cahathīnārum |
| Num.4.34 | Cahathinōs | Cahathīnōs |
| Num.4.37 | Cahathinōrum | Cahathīnōrum |
| Num.7.9 | Cahathinīs | Cahathīnīs |
| Num.7.12 | Gadinōrum | Gadīnōrum |
| Num.10.20 | Gadinæ | Gadīnæ |
| Num.10.21 | Cahathinī | Cahathīnī |
| Num.13.4 | Rūbēninā | Rūbēnīnā |
| Num.13.8 | Ephrāiminā | Ephrāimīnā |
| Num.13.15 | Gadinā | Gadīnā |
| Num.13.28 | Enaquinōs | Enaquīnōs |
| Num.13.33 | Enaquinōs | Enaquīnōs |
| Num.26.12 | Namuelina | Namuelīna |
| Num.26.13 | Saulina | Saulīna |
| Num.26.24 | Jasubina | Jasubīna |
| Num.26.26 | Jalelina | Jalelīna |
| Num.26.26 | Saredina | Saredīna |
| Num.26.29 | Galaadina | Galaadīna |
| Num.26.30 | Jeserina | Jeserīna |
| Num.26.31 | Asrielina | Asrielīna |
| Num.26.38 | Achiramina | Achiramīna |
| Num.26.38 | Azbelina | Azbelīna |
| Num.26.39 | Huphamina | Huphamīna |
| Num.26.39 | Suphamina | Suphamīna |
| Num.26.42 | Suhamina | Suhamīna |
| Num.26.45 | Malcielina | Malcielīna |
| Num.26.48 | Jessielina | Jessielīna |
| Num.26.49 | Sellemina | Sellemīna |
| Num.26.57 | Cahathina | Cahathīna |
| Num.26.57 | Merarina | Merarīna |
| Num.32.1 | Gadinī | Gadīnī |
| Num.32.29 | Gadinī | Gadīnī |
| Num.32.31 | Gadinī | Gadīnī |
| Num.32.33 | Gadinīs | Gadīnīs |
| Num.32.34 | Gadinī | Gadīnī |
| Num.34.14 | Gadina | Gadīna |
| Num.34.14 | Rūbēnina | Rūbēnīna |
| Num.34.24 | Ephrāiminā | Ephrāimīnā |

(Num 26 stems other than the suffix are left as they are; only the suffix vowel changes.)

### Settled books (proposal for Nathan) — 1

| Verse | Now | Fix |
|---|---|---|
| Exod.6.14 | Rūbēninæ | Rūbēnīnæ (`text/EXO.usfm` line 175: *hinc Rūbēninæ cognātiōnēs*) |

Every other -inus adjective in Genesis, Exodus, Leviticus and the NT is already marked as Gaffiot has it.
