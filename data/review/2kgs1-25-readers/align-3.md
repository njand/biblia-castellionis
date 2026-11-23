# 2 Kings 18–25: aligner 3's report (2026-11-22)

Rows in `data/versification/2Kgs.draft.edits.tsv` appended after aligners 1 and 2 (rows 151–208; rows 2–150 kept
unchanged), all `approved`, in book order, notes in 1 Kings' style. Where a split and a merge share an id, the split
comes first.

## Edits by op (58)

| op | count |
|---|---|
| split | 26 (one follow-on: `2Kgs.19.5+split`) |
| merge | 28 |
| chapter | 4 (21:1, 22:1, 23:1, 25:1) |
| opens | 0 |
| absent | 0 |
| range | 0 |

Per chapter: ch. 18 – 6 (18:1–2, 18:14–15, 18:32–33); ch. 19 – 8 (19:4–6, 19:15–16, 19:22–23); ch. 20/21 – 7 (the
chapter break at 21:1, 21:1–2, 21:3–8, 21:18–19); ch. 22 – 7 (the chapter break at 22:1, 22:1–2, 22:5–6, 22:8–9,
22:18–19); ch. 23 – 14 (the chapter break at 23:1, 23:19–21, 23:30–37); ch. 24 – 8 (24:1–3, 24:12–13, 24:15–16); ch. 25
– 8 (the chapter break at 25:1, 25:3–4, 25:16–17, 25:21–22).

## Tests

`python -m pipeline versify 2Kgs --draft --to <copy>` on scratch copies of `text/draft/2KI.usfm` and
`text/orig/draft/2KI.usfm`: both "207 edits, 207 boundaries moved, 61 verses renumbered; checks passed (same words,
KJV verse counts)": the whole book now has the KJV's counts, with no problems. Chapters 18–25 have 37, 37, 21, 26, 20,
37, 20, 30, and the two copies have the same number of words in every verse of 18–25. I then read 18–25 of the
renumbered draft against the KJV verse by verse. (`--draft` relays the BSB's paragraphs, so a new `\c` shows `\p`
even where the break falls mid-sentence; paragraphs are phase 2's.)

## Judgment calls

- **The two chapter breaks the readers found** (reader 09, checked against the text):
  - 20/21: `chapter 2Kgs.21.1` at *annos tum natus duodecim*. *Postquam ad majorum suorum manes migravit Ezechias,
    regnum pro eo obtinuit Manasses ejus filius,* (KJV 20:21) keeps its own marker and ends ch. 20 as its 21st, as
    aligner 2's 12:1; `merge 2Kgs.21.2` then joins *Regnavit annos quinquaginta quinque …* to KJV 21:1.
  - 21/22: `chapter 2Kgs.22.1` at *anno aetatis suae octavo*. *Amone in suo sepulcro … sepulto, regnum pro eo iniit
    Josias ejus filius,* (KJV 21:26) ends ch. 21 as its 26th; `merge 2Kgs.22.2` joins *Regnavit Hierosolymis annos unum
    et triginta …* to KJV 22:1.
- **Two more chapter breaks moved for lead-in clauses** (not in the readers' list; as 1 Kgs 3:1, `chapter` with a
  `merge` of the marker left behind, so the chapter keeps its count):
  - 22/23: *Haec res postquam relata regi est:* is KJV 22:20's end 'And they brought the king word again'; it joins
    22:20, and 23:1 begins at the main verb *curavit ad se convocandos*.
  - 24/25: *Quum hic Sedecias contra regem Babyloniae rebellasset,* is KJV 24:20's end 'that Zedekiah rebelled against
    the king of Babylon'; it joins 24:20, and 25:1 begins at the date *anno ejus regni nono* (KJV 'in the ninth year of
    his reign'). Both breaks now fall mid-sentence (`\nb` once paragraphs are set).
- **The readers' places, verified**: 19:3–6 (KJV 4b *quae quum … exstant* back to 4; KJV 5 *Haec postquam … retulerunt:*
  and 6 *Esajas illis respondit* split apart); 19:16 (split at *praebe Jova*); 19:23 (split at *per nuntios tuos*);
  21:1–8 (1738's 4 and 5 each hold two KJV verses, split at *aras in aede* and *filium suum per ignem*; 1738's 7–8 are
  KJV 8); 22:1–6 (6 holds KJV 5–6, split at *fabris, structoribus*); 23:31–37; 24:1–4; 24:12–16; 25:16–17 (split at
  *duodeviginti eubitus*, so printed); 25:21–22. Reader 08 has ch. 18 dividing as the KJV; the verse-by-verse
  reading found three places that differ, 18:1–2, 18:14–15 and 18:32–33.
- **Lead-in clauses moved back to the verse they report** (as 1 Sam 17:40 and aligners 1–2): 18:15 *Quumque ille ei
  trecenta … imperasset:*, 22:9 *Eum ubi legit Saphan,*, 22:19 *Quod ad ea pertinet, quae audivisti:*, 23:1 (above),
  23:21 *Deinde Hierosolymam reversus,*, 23:31 *Ejus in locum Joachazus … factus est,*, 24:2 *cui quum Joacimus …
  rebellionem fecisset:*, 24:13 *quo capto, Babyloniae rex anno sui regni octavo* (its subject stays with the ablative
  absolute, as 11:19's *Pontifex*), 25:1 (above), 25:22 *Abductis autem ex sua patria Judaeis,*.
- **Splits inside a sentence where the KJV verse's words stand clear**: 18:1 and 21:18 at *annum tum agens* (as 15:1);
  18:33 at *Num reliquarum*; 23:20 at *omnesque sacellanos*; 23:33 at *eumque Pharao Necho*; 23:34 at *Eliacimumque*;
  23:37 at *Is in Jovam fuit impius*; 24:3 at *quae res Judaeis*; 24:15 at the list item *omnibusque militibus numero
  septem millium* (KJV 16's seven thousand and thousand craftsmen; the closing *abductis* stays in 16); 25:3 at the
  main verb *refracta urbs est* (KJV 4 'And the city was broken up').
- **Speech introductions at a verse's end left where Castellio puts them**: 18:18 *Rabsaces apud eos hujusmodi verba
  facit:* (KJV 19 'And Rab-shakeh said'), 19:2 *qui ei ita dicerent: sic dicit Ezechias:* (KJV 3, reader 08), 19:9
  *sic dicetis Ezechiae Judaeae regi:* (KJV 10), 19:14 *apud eum precatur in hunc modum:* (KJV 15), 20:8 *ita dixit
  Esajas:* (KJV 9).
- **Sentences left as Castellio divides**: 22:3–4, KJV 4's 'Go up to Hilkiah the high priest' is *misit ad Helciam
  pontificem maximum* inside KJV 3's main clause, so KJV 4 begins at *ut summam faceret*; 24:3–4, KJV 3's 'to remove
  them out of his sight, for the sins of Manasseh' is the *ut* clause that opens 4, whose one verb *tolleret* also
  governs KJV 4's *fusumque ab eo sanguinem innocentem*, so 3 is only *quae res Judaeis Jovae jussu accidit,*; 24:10–11,
  KJV 10's 'and the city was besieged' is the first half of the two-part *quum* clause of 11 (as aligner 1's 7:17/18);
  25:5–6, KJV 6's 'So they took the king' is *ceperunt*, the main verb closing 5 after its subject and participles.
- **25:29** at *mutatis* (Claude's settlement) is the KJV's start; nothing moves there.
- No `absent`, no `opens`: every KJV verse of 18–25 has Latin of its own.
