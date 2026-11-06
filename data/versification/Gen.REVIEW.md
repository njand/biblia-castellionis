# Gen: renumbering to the KJV

11 moved boundaries; 45 more verses only change number. Only markers move: the words before and after are checked identical, and every chapter ends with the KJV's verse count. Edits: `data/versification/Gen.edits.tsv` (set `status` to `approved`); preview: `python -m pipeline versify Gen`.

## 1. Gen.3.23: split

> Itaque eum ex Ēdēnis pōmāriō abēgit, ut humum, unde ortus erat, coleret. ‖ Et ējectō homine, collocāvit ab orientālī parte pōmāriī Cherūbōs, et flammeum ēnsem vibrantem, ad arboris vītālis aditum cūstōdiendum.

- KJV 3:23: Therefore the LORD God sent him forth from the garden of Eden, to till the ground from whence he was taken.
- KJV 3:24: So he drove out the man; and he placed at the east of the garden of Eden Cherubims, and a flaming sword which turned every way, to keep the way of the tree of life.

*KJV 3:24 "So he drove out the man"*

## 2. Gen.4.17: split

> Suscēpit autem ex uxōre suā Henōchum, ā cujus Henōchī nōmine urbem ā sē conditam appellāvit. ‖ Huic Henōchō nātus est Iradus, quī porrō Iradus genuit Mahujælem, Mahujæl Mathusælem, Mathusæl Lamēchum.

- KJV 4:17: And Cain knew his wife; and she conceived, and bare Enoch: and he builded a city, and called the name of the city, after the name of his son, Enoch.
- KJV 4:18: And unto Enoch was born Irad: and Irad begat Mehujael: and Mehujael begat Methusael: and Methusael begat Lamech.

*KJV 4:18 "And unto Enoch was born Irad"; 4:18–25 become 4:19–26*

## 3. Gen.7.1: chapter break moves

> Hæc omnia Deī mandāta cum fēcisset Nōa, ‖ Jōva eum ita est allocūtus: “Ingredere tū, ūnā cum omnī tuā familiā, in arcam, quoniam quidem tē animadvertī esse omnium hujus sæculī in meō cōnspectū facile jūstissimum.

- KJV 6:22: Thus did Noah; according to all that God commanded him, so did he.
- KJV 7:1: And the LORD said unto Noah, Come thou and all thy house into the ark; for thee have I seen righteous before me in this generation.

*KJV 6:22 "Thus did Noah" is the opening clause of 7:1; the break falls mid-sentence (USFM nb: no new paragraph)*

## 4. Gen.8.1: chapter break moves

> Postquam autem viguērunt in terrīs aquæ centum quīnquāgintā diēs, ‖ recordātus Nōæ Deus, et omnium, quæ cum eō erant in arcā, animālium et pecorum, ventum in terrās immīsit ad coercendās aquās.

- KJV 7:24: And the waters prevailed upon the earth an hundred and fifty days.
- KJV 8:1: And God remembered Noah, and every living thing, and all the cattle that was with him in the ark: and God made a wind to pass over the earth, and the waters asswaged;

*KJV 7:24 "the waters prevailed … an hundred and fifty days" is the opening clause of 8:1; mid-sentence (USFM nb: no new paragraph)*

## 5. Gen.10.28: split

> Obālem, Abimælem, Sabam, ‖ Ophīren, Hevilam, et Jobābum. Hī omnīnō fuērunt fīliī Joctānis,

- KJV 10:28: And Obal, and Abimael, and Sheba,
- KJV 10:29: And Ophir, and Havilah, and Jobab: all these were the sons of Joktan.

*KJV 10:29 "And Ophir, and Havilah, and Jobab"; 10:29–31 become 10:30–32*

## 6. Gen.11.14: merge into the verse before

> Caīnan annō ætātis suæ centēsimō trīcēsimō genuit Salam,

Joins Gen.11.13.
- KJV 11:13: And Arphaxad lived after he begat Salah four hundred and three years, and begat sons and daughters.

*Caīnān begets Sala (Septuagint; not in the KJV): joins 11:13*

## 7. Gen.11.15: merge into the verse before

> vīxitque quadringentōs trēs annōs post, aliīs intereā līberīs prōcreandīs.

Joins Gen.11.13.
- KJV 11:13: And Arphaxad lived after he begat Salah four hundred and three years, and begat sons and daughters.

*Caīnān's remaining years (Septuagint; not in the KJV): joins 11:13; 11:16–34 become 11:14–32*

## 8. Gen.14.11: merge into the verse before

> Ibi pulsīs superātīsque Sodomæ et Gomorræ rēgulīs, reliquī fugā montēs petīvērunt.

Joins Gen.14.10.
- KJV 14:10: And the vale of Siddim was full of slimepits; and the kings of Sodom and Gomorrah fled, and fell there; and they that remained fled to the mountain.

*KJV 14:10 covers both the slime pits and the flight; 14:12–25 become 14:11–24*

## 9. Gen.19.1: chapter break moves

> Tum Jōva, factō cum Abrāhāmō loquendī fīne, discessit. Abrāhāmus eōdem, unde dīgressus erat, reversus est. ‖ Angelī autem illī duo ad Sodomam sub vesperum pervēnērunt. Eōs cōnspicātus Lōtus, quī tum in portā Sodomæ sedēbat, prōcessit iīs obviam, cumque summissō ad terram vultū salūtāvisset,

- KJV 18:33: And the LORD went his way, as soon as he had left communing with Abraham: and Abraham returned unto his place.
- KJV 19:1: And there came two angels to Sodom at even; and Lot sat in the gate of Sodom: and Lot seeing them rose up to meet them; and he bowed himself with his face toward the ground;

*KJV 18:33 "And the LORD went his way … Abraham returned" is the first two sentences of 19:1*

## 10. Gen.23.20: merge into the verse before

> Abrāhāmus Saram conjugem suam sepelīvit, in terrā Chananæā.

Joins Gen.23.19.
- KJV 23:19: And after this, Abraham buried Sarah his wife in the cave of the field of Machpelah before Mamre: the same is Hebron in the land of Canaan.

*KJV 23:19 "Abraham buried Sarah … in the land of Canaan" spans 23:19–20; 23:21 becomes 23:20*

## 11. Gen.24.68: merge into the verse before

> et ejus amōre dolōrem, quem capiēbat ex Sarā mātre, lēnīvit.

Joins Gen.24.67.
- KJV 24:67: And Isaac brought her into his mother Sarah’s tent, and took Rebekah, and she became his wife; and he loved her: and Isaac was comforted after his mother’s death.

*KJV 24:67 includes "and Isaac was comforted after his mother's death"*

## Verses that only change number

4:18–25 → 4:19–26; 10:29–31 → 10:30–32; 11:16–34 → 11:14–32; 14:12–25 → 14:11–24; 23:21 → 23:20

**Decision:** approve all eleven, or name the ones to change. Two need a choice:

- **6:22 and 7:24 open the next chapter mid-sentence** in your text (*Hæc omnia Deī mandāta cum fēcisset Nōa, ‖ Jōva eum ita est allocūtus*). Following the KJV puts the chapter break inside the sentence (USFM `\nb`: no new paragraph). Accept that, or keep the break where it is and leave KJV 6:22 and 7:24 as the opening clause of 7:1 and 8:1 (two chapters then keep one verse fewer)?
- **Caīnān (11:14–15)** is in the Septuagint and Luke 3:36, not the KJV. Join both verses to 11:13 as proposed, or another arrangement?
