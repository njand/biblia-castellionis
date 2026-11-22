# 1 Kings 9–15: aligner 2's report (2026-11-22)

Rows in `data/versification/1Kgs.draft.edits.tsv`, appended after aligner 1's 88 (rows 90–139), all `approved`, in
book order, notes in 2 Samuel's style; aligner 1's rows unchanged.

## Edits by op (50)

| op | count |
|---|---|
| split | 24 (two `+split` follow-ons: 11:31, 12:12) |
| merge | 24 |
| chapter | 2 (13:2, 15:1) |
| opens | 0 |
| absent | 0 |
| range | 0 |

Per chapter (1738's numbers): ch. 9 – 2 (9:26); ch. 10 – none; ch. 11 – 10 (11:3, 25, 27, 28–29, 31); ch. 12 – 13
(12:6, 12–13, 16, 18, 22–24, 33); ch. 13 – 13 (the chapter break at 13:2, 13:13–15, 23–24, 28–30); ch. 14 – 6
(14:1–2, 11, 12–13); ch. 15 – 9 (the chapter break at 15:1, 15:7–8, 10, 29–30).

## Tests

`python -m pipeline versify 1Kgs --draft --to <copy>` on scratch copies of `text/draft/1KI.usfm` and
`text/orig/draft/1KI.usfm`: both "138 edits, 138 boundaries moved, 51 verses renumbered"; the only problems are
1Kgs 21 (28 vs 29) and 22 (54 vs 53), outside this range. Chapters 9–15 have the KJV's counts (28, 29, 43, 33, 34,
31, 34), and the two copies have the same number of words in every verse of 9–15. I then read 9–15 of the renumbered
draft against the KJV verse by verse. Chapter 10 needed nothing.

## Judgment calls

- **Two chapter breaks moved (`chapter`, mid-sentence)**:
  - 12/13: 1738's 13:1 *Quum autem ad aram … adscendisset:* is the KJV's 12:33 (reader 08); its 13:2 opens with the
    main verb *supervenit* (KJV 13:1 'there came a man of God'). The break moves to *supervenit*: `chapter 13.2`
    with the anchor at the verse's first word leaves 13.2's marker before an empty head at the end of chapter 12,
    so a `merge 13.2` removes it (the split of 13:2 at *clamavit ad aram*, KJV 13:2, comes first in the file).
    1738's 12:33 joins 32 (KJV 32 holds both feast and Bethel sacrifices).
  - 14/15: KJV 14:31 ends 'And Abijam his son reigned in his stead', the main clause *Huic in regnum successit Abiamus
    ejus filius,* that opens 1738's 15:1; the break moves to the relative clause *qui anno duodevicesimo …* (KJV
    15:1), as 15:8–9 (*Huic in regnum successit Asa filius ejus, | qui vicesimo …*) in the same chapter. A judgment
    call: chapter 15 now opens with a lower-case relative clause; leaving Castellio's break would leave 14:31 one
    clause short.
  - As aligner 1 noted for 3:1, the draft's paragraph relay sets `\p` after both new `\c` lines, though the breaks
    fall mid-sentence (the op writes `\nb`).
- **Speech introductions at a verse's end left where Castellio puts them**: 9:2 *itaque locutus est:* (KJV 3 'And
  the LORD said'), 9:12 *ita dixit:* (KJV 13), 10:5 *regem sic adloquitur:* (KJV 6), 11:10 *minatus est ei in hunc
  modum:* (KJV 11), 12:8 *et ab eis quaerit:* (KJV 9), 13:20 *et ad eum sic clamat:* (KJV 21). Where a new split
  was needed inside a verse, the KJV verse's words decide: 11:31 splits at *atque ita Jeroboamum adloquitur*
  ('And he said to Jeroboam'), 12:14 at *juvenum consilium secutus, ita dixit:*.
- **Lead-in clauses moved back to the verse before** (as 1 Sam 17:40): 9:26 *Itemque absoluto templo,* (KJV 25 'So he
  finished the house'), 11:3 *Illis amore junctus Solomo,* (KJV 2 'Solomon clave unto these in love'), 12:6 *Atque
  illis digressis,* (KJV 5 'And the people departed'), 13:15 *Quumque ille se esse respondisset:* (KJV 14 'And he
  said, I am'), 13:28 *eoque instrato,* (KJV 27 'And they saddled him'), 11:31 *Hic quum duo soli essent in agris:*
  (KJV 29 'and they two were alone in the field').
- **Splits inside a sentence where the KJV verse's words stand clear**: 11:28/29 the cause of the conspiracy
  (*cujus conspirationis caussa haec fuit: Mellonem aedificante Solomone … obstruente,* = KJV 27; *erat Jeroboamus
  vir robustus* = 28); 12:12 (KJV 12–14 in one sentence) at *respondit eis rex* and *juvenum consilium secutus*;
  12:22 at the indirect command *ut Roboamo … nuntiaret* (KJV 23 'Speak unto Rehoboam'); 13:13 at *divinumque
  subsequitur* (KJV 14 'And went after the man of God'; 1738's margin 14 is at *et eum*); 14:1 at *uxori suae
  mandat* (KJV 2), leaving its subject *Jeroboamus* in 1 with *aegrotante ejus filio Abia* (KJV 1 'Abijah … fell
  sick'); 14:11 at the result clause *ita ut Jeroboamicorum mortui* (KJV 11); 15:29 at *propter Jeroboami scelera:*
  (KJV 30 'Because of the sins of Jeroboam'; 1738's margin 30 is a line lower at *quae non solum*, reader 11).
- **No `absent`, no `opens`**: every KJV verse of 9–15 has Latin of its own. Castellio's renderings that differ
  in sense (11:5's L. … H. *Chamosum*, 13:20 God speaking to the man of God, 15:6 *L. Abiamum H.*) stay in their
  verses; they are not division questions.
