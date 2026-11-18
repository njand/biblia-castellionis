# Lev: renumbering to the KJV

4 moved boundaries; 4 more verses only change number. Only markers move: the words before and after are checked identical, and every chapter ends with the KJV's verse count. Edits: `data/versification/Lev.edits.tsv` (set `status` to `approved`); preview: `python -m pipeline versify Lev`.

## 1. Lev.15.27: merge into the verse before

> Omne ūtēnsile, super quō sēderit, pollūtum estō, perinde atque in mēnsibus.

Joins Lev.15.26.
- KJV 15:26: Every bed whereon she lieth all the days of her issue shall be unto her as the bed of her separation: and whatsoever she sitteth upon shall be unclean, as the uncleanness of her separation.

*KJV 15:26 'Every bed whereon she lieth … and whatsoever she sitteth upon shall be unclean' is 1738's 15:26–27 (*Omne utensile, super quo sederit*); its 28–29 are the KJV's 27–28 (Nathan, 2026-11-18: "Fix the versification"; lev-notes.md §E)*

## 2. Lev.15.30: split

> Diē octāvō sūmitō duōs turturēs, aut duōs columbā nātōs, eōsque ad sacerdōtem affertō ad portam ōrāculāris tabernāculī, quōrum ūnum sacerdōs ad piāculum faciat, alterum solidō sacrificiō, et prō eā apud Jōvam supplicet ob ejus immundum flūxum.

- KJV 15:30: And the priest shall offer the one for a sin offering, and the other for a burnt offering; and the priest shall make an atonement for her before the LORD for the issue of her uncleanness.
- KJV 15:31: Thus shall ye separate the children of Israel from their uncleanness; that they die not in their uncleanness, when they defile my tabernacle that is among them.

*KJV 15:30 'And the priest shall offer the one for a sin offering, and the other for a burnt offering' begins at *quorum unum sacerdos ad piaculum faciat*; 1738's 15:30 holds the KJV's 29–30 (Nathan, 2026-11-18)*

## 3. Lev.19.27: merge into the verse before

> Nē auguriō nēve dīvīnātiōne ūtiminī.

Joins Lev.19.26.
- KJV 19:26: ¶ Ye shall not eat any thing with the blood: neither shall ye use enchantment, nor observe times.

*KJV 19:26 'Ye shall not eat any thing with the blood: neither shall ye use enchantment, nor observe times' is 1738's 19:26–27 (*Ne augurio neve divinatione utimini*); its 28 holds the KJV's 27–28 (Nathan, 2026-11-18)*

## 4. Lev.19.28: split

> Nē vōbīs in fūnere verticem dērāditōte, nēve barbam vellitōte, nēve corpora vestra dīlaniātōte, neu vōbīs notās inūritōte. Ego Jōva.

- KJV 19:28: Ye shall not make any cuttings in your flesh for the dead, nor print any marks upon you: I am the LORD.
- KJV 19:29: ¶ Do not prostitute thy daughter, to cause her to be a whore; lest the land fall to whoredom, and the land become full of wickedness.

*KJV 19:28 'Ye shall not make any cuttings in your flesh for the dead, nor print any marks upon you: I am the LORD' begins at *neve corpora vestra dilaniatote*; KJV 19:27 is the head and the beard (Nathan, 2026-11-18)*

## Verses that only change number

15:28–30 → 15:27–29; 19:28 → 19:27

**Decision:** approve all eleven, or name the ones to change. Two need a choice:

- **6:22 and 7:24 open the next chapter mid-sentence** in your text (*Hæc omnia Deī mandāta cum fēcisset Nōa, ‖ Jōva eum ita est allocūtus*). Following the KJV puts the chapter break inside the sentence (USFM `\nb`: no new paragraph). Accept that, or keep the break where it is and leave KJV 6:22 and 7:24 as the opening clause of 7:1 and 8:1 (two chapters then keep one verse fewer)?
- **Caīnān (11:14–15)** is in the Septuagint and Luke 3:36, not the KJV. Join both verses to 11:13 as proposed, or another arrangement?
