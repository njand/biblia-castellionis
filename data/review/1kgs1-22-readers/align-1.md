# 1 Kings 1–8: aligner 1's report (2026-11-22)

Rows in `data/versification/1Kgs.draft.edits.tsv` (created with its header; rows 2–89), all `approved`, in book
order, notes in 2 Samuel's style.

## Edits by op (88)

| op | count |
|---|---|
| split | 42 (two `+split` follow-ons: 3:23, 7:46) |
| merge | 45 |
| chapter | 1 (3:1) |
| opens | 0 |
| absent | 0 |
| range | 0 |

Per chapter: ch. 1 – 7 (1:5/6, 1:36/37, 1:46/47, 1:53/54); ch. 2 – 10 (2:2/3, 2:18/19, 2:30/31, 2:41/42, 2:44/45)
+ the chapter break at 3:1; ch. 3 – 11 (the merge of 3:1, 3:3/4, 3:19/20, 3:22–26); ch. 4 – 10 (4:1/2, 4:7–11, 4:30/31); ch. 5 – 6
(5:8–11, 5:14/15); ch. 6 – 2 (6:25/26, 6:37/38); ch. 7 – 29 (2, 13/14, 16–24, 27–29, 31–35, 39, 41–50);
ch. 8 – 12 (8:7–19, 8:38/39, 8:41–43).

## Tests

`python -m pipeline versify 1Kgs --draft --to <copy>` on scratch copies of `text/draft/1KI.usfm` and
`text/orig/draft/1KI.usfm`: both "88 edits, 88 boundaries moved, 42 verses renumbered", same words; the only
problems are 1Kgs 21 (28 vs 29) and 22 (54 vs 53), outside this range. Chapters 1–8 now have the KJV's counts
(53, 46, 28, 34, 18, 38, 51, 66), and the two copies have the same number of words in every verse of 1–8. I then
read 1–8 of the renumbered draft against the KJV verse by verse.

## Judgment calls

- **Chapter break moved (`chapter`, not `opens`)**: KJV 2:46b 'And the kingdom was established in the hand of
  Solomon' is the ablative absolute *Confirmato regno,* that opens 1738's 3:1; the break moves to *Solomo
  adfinitatem* (as Exod 8:1, Deut 2:1) and a `merge` of 3:1 joins *Confirmato regno,* to 2:46. Note: the draft's
  paragraph relay then sets `\p` after `\c 3`, though the break falls mid-sentence (the op itself writes `\nb`).
- **Speech introductions at a verse's end left where Castellio puts them** (the words belong to the next KJV verse
  but introduce the speech in their own sentence): 1:16 *respondit in hunc modum:* (KJV 17 'And she said'), 1:28
  *sic ei jurat rex.* (KJV 29 'And the king sware'), 1:32 *iisque ita imperat:* (KJV 33 'The king also said'),
  2:19 *et ita dixit:*, 3:10 *sic ei respondit.*, 3:16 *altera earum sic loquitur:*, 5:7 *et Solomoni ita
  rescripsit:* (KJV 8 'And Hiram sent to Solomon, saying'), 8:22 *ita fatur:*. Narrative clauses carrying the
  previous verse's content were moved back, as 1 Sam 17:40 (2:31 *Quod Joabi responsum postquam regi Banajas
  retulit:*, 3:23 *Ad hunc modum quum illae apud regem altercarentur:*, 5:15 *His praeerat Adoniramus.*, 7:2 *Qua ad
  finem perducta,*, 3:4 *Quumque in sacellis … solitus,*, etc.).
- **Sentences left as Castellio divides**: 1:47–48, KJV 47's last clause 'And the king bowed himself upon the bed'
  is one clause with 48's thanks (*Et rex ipse in lecto … submisse gratias egit*), so stays in 48; 6:21–22 *Idque
  et totum denique templum … auro tegebat* (KJV 21b 'and he overlaid it with gold' fused with 22); 8:12–13 split at
  *commorandi domicilium aedificavi*, leaving its subject *ego tibi Jova* in 12 before the relative clause; 8:41–42
  split at *audito tuo tam praeclaro nomine*, leaving KJV 41's 'cometh out of a far country for thy name's sake'
  (*venerint ob tuum nomen, ex finibus remotis*) inside 42, where Castellio's sentence puts it.
- **Splits inside a sentence where the KJV verse's words stand clear**: 1:5/6 at the closing ablative absolute
  *patre interea connivente*; 1:36/37 at *ut quemadmodum ipse tibi adfuit* (after *faxit Jova Deus tuus*); 3:19/20
  at the main verb *media nocte surgit*; 4:30/31 at *verum etiam omnes mortales*; 6:25/26 at *utroque in denos
  adsurgente cubitos* (Castellio's 25 = KJV 25–26); 7:13/14 at the apposition *ex matre vidua Nephthalensem*;
  7:46 (three KJV verses of one list, 43–45); 7:48 at *omissa tot vasorum* (KJV 47); 8:9 at *ut nequirent*.
- **Readers' doubts**: 1:47 (margin at *eiusque* or *dominoque*) and 4:9 (margin at *Elonemque* or *Bethsamem*)
  are moot: the KJV's boundaries fall at *dominoque* and *Bendecer*, and the words go there either way. 2:45 (margin
  at *quod scelus*, the KJV's 44b) is moved back to 44; 8:8 (*atque illic adhuc sunt*, reader 06) is the KJV's 8b.
- No `absent`, no `opens`: every KJV verse of 1–8 has Latin of its own.
