# 2 Kings 1–8: aligner 1's report (2026-11-22)

Rows in `data/versification/2Kgs.draft.edits.tsv` (created with its header; rows 2–74), all `approved`, in book
order, notes in 1 Kings' style.

## Edits by op (73)

| op | count |
|---|---|
| split | 35 (two `+split` follow-ons: 2:17, 6:3) |
| merge | 38 |
| chapter | 0 |
| opens | 0 |
| absent | 0 |
| range | 0 |

Per chapter: ch. 1 – 4 (1:4/5, 1:11/12); ch. 2 – 16 (2:2/3, 2:3/4, 2:4/5, 2:13/14, 2:16–18, 2:19–21); ch. 3 – 7
(3:4–8, 3:25–28: 1738's 28 verses to the KJV's 27); ch. 4 – 18 (4:6/7, 4:12/13, 4:18/19, 4:25/26, 4:30/31,
4:32–36); ch. 5 – 6 (5:5/6, 5:12/13, 5:24/25); ch. 6 – 15 (6:2–7, 6:13/14, 6:18–20, 6:32/33: 1738's 34 to the KJV's
33); ch. 7 – 2 (7:15/16); ch. 8 – 5 (8:6/7: 1738's 30 to the KJV's 29; 8:16/17, 8:25/26).

## Tests

`python -m pipeline versify 2Kgs --draft --to <copy>` on scratch copies of `text/draft/2KI.usfm` and
`text/orig/draft/2KI.usfm`: both "73 edits, 73 boundaries moved, 25 verses renumbered", same words; the only
problems are 2Kgs 11 (20 vs 21), 15 (37 vs 38), 20 (20 vs 21) and 21 (25 vs 26), outside this range. Chapters 1–8
now have the KJV's counts (18, 25, 27, 44, 27, 33, 20, 29), and the two copies have the same number of words in
every verse of 1–8. I then read 1–8 of the renumbered draft against the KJV verse by verse.

## Judgment calls

- **The three surplus verses** (readers 02–04, checked against the text): 3:26 *Quam quum funditoribus
  circumsessam …* is KJV 25b and merges into 25 (with 3:27/28 then moved at *cepit filium*); 6:33 *sciendum vobis
  est …* is Elisha's speech of KJV 32b and merges into 32; 8:7 *ut mulieri omnia sua restitueret …* is KJV 6b and
  merges into 6.
- **Printer's starts moved to the KJV's**: 2:4 (margin at *Quibus ille, et ego scio … tacete*, KJV 3b; moved back to
  3, 4 split at *Tum Elias*) and 4:26 (margin at *eamque interrogaret*; split at *ut advenienti*), as Claude's
  settlements say. 2:2 stays at the printer's *ut ibi maneret*: KJV 2's 'And Elijah said unto Elisha' is
  *Elisaeum, qui simul aderat, hortabatur*, whose object is also KJV 1's 'with Elisha', so there is no clean place
  earlier.
- **Lead-in clauses moved back to the verse they report** (as 1 Sam 17:40, 1 Kgs 3:23): 1:5 *His ad nuntios ab Elia
  perlatis,* (KJV 4 'And Elijah departed'), 2:3 *Deinde illis ad Bethel digressis,*, 2:5 *Deinde postquam
  Hierichuntem pervenerunt,*, 2:14 *Atque ubi ad Jordanis ripam constitit:*, 2:20 *Quo adlato,*, 3:28 *Sed postquam
  non potuit,*, 4:7 *Ita cohibito oleo,*, 4:13 *eaque vocata atque adstante,*, 4:34 *Hoc incubitu pueri corpore
  tepefacto,*, 5:13 *Quum ita conversus, discederet succensens:*, 6:3 *Atque illo permittente:*, 6:14 *Atque ubi ei
  nuntiatum est, illum esse Dothane;*, 6:19 *Quod postquam ille ad Elisaei postulatum fecit:*, 7:16 *Quod postquam
  regi reversi nuntiarunt:*.
- **Splits inside a sentence where the KJV verse's words stand clear**: 2:17 at *tandem eorum* (the *Ille quum
  mittendos negaret,* clause is KJV 16b) and at the main verb's clause *ad eum Hierichunte manentem reverterunt*
  (KJV 18); 2:19 at *jussit adferri*; 3:4 at *mortuo Achabo* (KJV 5; its subject *Mesa Moabitarum rex* stays in 4);
  3:7 at *quaesivitque*; 4:18 at the main verb *coepit apud eumdem*; 4:32–33 at *ostio se cum illo* and *inscendit
  puerum* (the participle *precatusque Jovam,* is KJV 33b); 5:5 at the second main verb *et Israelitarum regi
  litteras attulit*; 5:24 at *in domini sui conspectum venit*; 6:3 at *cumque eis profectus est*; 6:4 at *accidit,
  ut unius*; 6:6 at *illi jussit*; 8:17 and 8:26 at *annos tum natus* (the age of KJV 17 and 26).
- **Speech introductions at a verse's end left where Castellio puts them**: 1:5 *ita respondent:* (KJV 6 'And they
  said'), 2:11 *cernente Elisaeo, et ita clamante:* (KJV 12 'And Elisha saw it, and he cried'), 3:15 *a Jova
  agitatus sic fatur:*, 4:15 *vocatamque et pro foribus adstantem sic adloquitur:* (KJV 15b with 16's 'And he
  said'), 6:30 *atque ita dicere:*.
- **Sentence left as Castellio divides**: 8:28–29, KJV 28's last clause 'and the Syrians wounded Joram' is
  *vulneratus a Syris Joramus* inside the *quum* clause that opens 1738's 30 (KJV 29); it stays there.
- **Readers' doubts**: 5:20 (*coepit Gihezis*) and 7:19 (*respondit triumuir*), placed by sense a line above the
  numeral, are the KJV's starts; nothing moves there. 3:21/22 and 7:17/18 keep Castellio's division (the KJV
  boundary falls between subject and verb, or between two parts of one *quum* clause).
- No `absent`, no `opens`, no `chapter`: every KJV verse of 1–8 has Latin of its own.
