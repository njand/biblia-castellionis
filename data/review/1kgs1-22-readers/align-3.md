# 1 Kings 16–22: aligner 3's report (2026-11-22)

Rows in `data/versification/1Kgs.draft.edits.tsv`, appended after aligners 1–2's 138 (rows 140–197), all
`approved`, in book order, notes in 2 Samuel's style; the earlier rows unchanged.

## Edits by op (58)

| op | count |
|---|---|
| split | 29 (one `+split` follow-on: 22:21) |
| merge | 29 |
| chapter | 0 |
| opens | 0 |
| absent | 0 |
| range | 0 |

Per chapter (1738's numbers): ch. 16 – 4 (16:24, 30–31); ch. 17 – 6 (17:3–4, 6, 23); ch. 18 – 10 (18:3, 17, 22, 34,
46); ch. 19 – 4 (19:4, 12); ch. 20 – 14 (20:4–5, 10, 17–20, 26, 35–36, 38); ch. 21 – 13 (21:9–10, 14, 17, 19, 21, 25,
27–28); ch. 22 – 9 (22:21–22, 33, 44, 53).

## Tests

`python -m pipeline versify 1Kgs --draft --to <copy>` on scratch copies of `text/draft/1KI.usfm` and
`text/orig/draft/1KI.usfm`: both "196 edits, 196 boundaries moved, 64 verses renumbered; checks passed (same words,
KJV verse counts)". **The whole book now has the KJV's verse counts, with no problems on either text.** Chapters
16–22 have 34, 24, 46, 21, 43, 29, 53 verses, and the two copies have the same number of words in every verse of
16–22. I then read 16–22 of the renumbered draft against the KJV verse by verse.

## Judgment calls

- **Ch. 21 (28 → 29)**: 1738's 25 holds KJV 25–26 in one sentence (reader 15); split inside the relative clause at
  *eo flagitiorum venisset, ut nefandos sequeretur deos* (KJV 26 'did very abominably in following idols'), so 25
  ends *qui, instigante Jezabele conjuge,* ('whom Jezebel his wife stirred up'). 1738's 27 *Tum Jova cum Elia
  Thesbita loquitur: videsne …* splits at *videsne* (KJV 29 'Seest thou'), and 28 *Quoniam* joins it.
- **Ch. 22 (54 → 53)**: 1738 follows the Hebrew from 44 (*quamquam sacella*, KJV 43b): 44 merged into 43. The
  Hebrew's 52/53 boundary also differs from the KJV's 51/52: *Regnavit in Israelitas annos duos,* (KJV 51 'reigned
  two years over Israel') moves to 51, and 52 starts at the printed *Iou mque offendit* (anchor `Jou mque|Iou mque`,
  the unprinted *a* kept as reader 15 found it).
- **22:22 at *Quo pacto?*** (KJV 'Wherewith?'), not 1738's *Ibo*; and *Atque alio aliud dicente,* (KJV 20b 'one said
  on this manner') goes back to 20, so 21 opens at *processit quidam spiritus*.
- **18:18 at *Cui ille*** (as settled at the merge) already matches the KJV: no edit.
- **Lead-in clauses moved back to the verse before** (as 1 Sam 17:40 and aligner 2): 16:24 *quorum sex quum Thersae
  regnavisset,*; 17:6 *ibi mansit,*; 17:23 *atque ita revixit puer,*; 18:3 *Quum autem fame gravi Samariae
  laboraretur,* (reader 13); 18:17 *Et Achabus Eliae obviam progressus,*; 18:22 *Quumque nihil ei populus
  responderet:*; 18:46 *Achabus autem, conscenso curru, Jezrael ire contendit:*; 19:4 *ibique relicto famulo suo,*;
  19:12 *Ventum sequebatur terrae motus …*; 20:10 *Hanc rem postquam digressi legati Benadado retulerunt:*; 20:26 *Horum consilium secutus rex Benadadus,*;
  20:38 *Ab eoque ictus et vulneratus,*; 21:14 *Ita educitur … necatur.*; 21:21 *et quia tu … addictus es,*
  (reader 14's flag); 22:33 *Sed exclamante Josaphato,*.
- **Splits inside a sentence where the KJV verse's words stand clear**: 16:30 at *parum habuit* (KJV 31 'as if it had
  been a light thing'), leaving 30 a participial clause *Hic Achabus … supergressus,*; 17:3 at *et de eo fluvio
  bibito* (KJV 4); 20:4 at *redierunt legati* (KJV 5 'the messengers came again'; 1738's 5 at *Haec est* joins it); 18:34 at *idemque iterum* (KJV 34; reader 13: Castellio's 34 = KJV 33b–34); 20:17–20 (Castellio's
  17 = KJV 17–18, his 18 = KJV 19–20a) at *jussit, eos* and *singuli singulis occisis*, with 19 *quos deinde …* and 20
  *Benadadus … evadit* joined into KJV 20; 20:35 at *praedixit ei* (KJV 36); 21:9 at *et contra eum* (KJV 10; reader
  14's flag); 21:17 at *Achabo Israelitarum* (KJV 18 'go down to meet Ahab'), so 17 is only *Tum Elias Thesbita jussus
  a Jova,*, and 1738's 18–19 join as KJV 19 (both of Elijah's sayings).
- **Left as Castellio divides**:
  - 16:9/10: *eumque … potantem et ebrium adgressus, | vulneribus interfecit* (KJV 10 'Zimri went in'; the reader
    placed 10 at the line start); the participle is not clearly KJV 10's.
  - 16:15/16: KJV 15b 'the people were encamped against Gibbethon' is Castellio's 16 (*ad Gabathonem … castra
    habentes*), inside the temporal clause.
  - 17:8/9: *jussit ei Jova, ut Sarephtham … se conferret, ibique maneret:* is KJV 8 and 9a in indirect speech;
    left.
  - Speech introductions at a verse's end, as aligner 2: 20:2 *ei ita significavit:* (KJV 2 'Thus saith Ben-hadad'),
    20:38 *stans ad praetereuntem regem clamat in hunc modum:* (KJV 39 'as the king passed by, he cried'), 20:41 *et
    ita loquitur:*, 21:8 *scriptas in hanc sententiam:*, 22:19 *atque ita dicentem:*.
- **No `absent`, `opens`, `chapter` or `range`**: every KJV verse of 16–22 has Latin of its own, and the chapter
  breaks are the KJV's.
