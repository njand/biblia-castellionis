# 2 Kings 9–17: aligner 2's report (2026-11-22)

Rows in `data/versification/2Kgs.draft.edits.tsv` appended after aligner 1's (rows 75–150; rows 2–74 kept
unchanged), all `approved`, in book order, notes in 1 Kings' style. Where a split and a merge share an id, the split
comes first (a merged marker can no longer be found by a later edit).

## Edits by op (76)

| op | count |
|---|---|
| split | 37 (two follow-ons: `2Kgs.11.19+split`, `2Kgs.16.2+chapter`) |
| merge | 37 |
| chapter | 2 (12:1, 16:2) |
| opens | 0 |
| absent | 0 |
| range | 0 |

Per chapter: ch. 9 – 8 (9:19–21, 9:25, 9:28); ch. 10 – 22 (10:11–13, 10:16–17, 10:20–23, 10:26, 10:28–29,
10:32–35); ch. 11 – 8 (11:5, 11:16, 11:19–20); ch. 12 – 1 (the chapter break); ch. 13 – 2 (13:16); ch. 14 – 4 (14:1–2,
14:27); ch. 15 – 6 (15:1–2, 15:22–23, 15:32–33); ch. 16 – 5 (the chapter break at 16:2, 16:2–3); ch. 17 – 20 (17:2,
17:8–9, 17:13–18, 17:21, 17:27, 17:29–30, 17:37–39).

## Tests

`python -m pipeline versify 2Kgs --draft --to <copy>` on scratch copies of `text/draft/2KI.usfm` and
`text/orig/draft/2KI.usfm`: both "149 edits, 149 boundaries moved, 48 verses renumbered", same words; the only
problems are 2Kgs 20 (20 vs 21) and 21 (25 vs 26), outside this range. Chapters 1–19 now have the KJV's counts (9–17:
37, 36, 21, 21, 25, 29, 38, 20, 41), and the two copies have the same number of words in every verse of 9–17. I then
read 9–17 of the renumbered draft against the KJV verse by verse. (`--draft` relays the BSB's paragraphs, so the `\p`
that opened 1738's 12:1 and 16:1 does not follow them into 11:21 and 15:38 in the copies; paragraphs are phase 2's.)

## Judgment calls

- **The two chapter breaks** (readers 05 and 07, checked against the text):
  - 11/12: `chapter 2Kgs.12.1` at *videlicet anno septimo regni Jehu*. *Agebat Joas annum septimum, quum regnum
    iniit,* (KJV 11:21 'Seven years old was Jehoash when he began to reign') keeps its own marker and ends ch. 11 as
    its 21st; the break falls mid-sentence (`\nb`), as 1 Kgs 3:1.
  - 15/16: 1738's 16:1 is all of KJV 15:38, the ablative absolute *Jothamo vita defuncto … sepulto,*. `chapter
    2Kgs.16.2` at its first words *Judaeae regnum obtinuit*, with `merge 2Kgs.16.2` taking away the marker left with
    no words, moves the break from before 16:1 to before 16:2 (mid-sentence, `\nb`). KJV 15:38's last clause 'and Ahaz
    his son reigned in his stead' is that main clause, *Judaeae regnum obtinuit Achazus ejus filius*, which also
    carries KJV 16:1's 'began to reign' and goes with 16:1. The follow-on split `2Kgs.16.2+chapter` at *annos tum
    natus* then makes KJV 16:2.
- **Ch. 17** (readers 07–08, verified): 1738 falls four behind through 17:13–18, each of which holds two KJV verses
  (splits at *non obtemperaverant* / *repudiatis illius* (13–14), *filios filiasque* (15), *repudiavit Jova* (17),
  *per omnia ab illo* (18)), and catches up through verses that divide KJV verses: 21 (KJV 24b), 27 (KJV 29b), 29–30
  (KJV 30–31, split at *Avani Nebahazum*), and 37–39 (KJV 37–39). For 37–39 I split where the KJV's words stand
  clear rather than following reader 08's sketch (38 = KJV 39a): *neve deos vererentur alienos,* ends KJV 37 ('and ye
  shall not fear other gods'), *neve icti … obliviscerentur; ne deos, inquam, vererentur alienos,* is KJV 38, *sed
  tantum Jovam Deum suum vererentur,* begins KJV 39. 17:1/2 also moves *Regnavit Samariae annos novem.* back to KJV 1,
  and 17:8/9 splits at the main verb *res designaverant illicitas*.
- **Printer's starts moved to the KJV's**: 10:29 (margin at *videlicet*, Claude's settlement; split at *quamquam a
  Jeroboami*); 17:29 (margin at the line start *Hemathenses*; KJV 31 begins at *Avani*). 10:35 (no numeral at *Jehu
  vita defuncto*) is split there for KJV 35.
- **Lead-in clauses moved back to the verse they report** (as 1 Sam 17:40 and aligner 1): 9:19 *Quum speculator
  nuntiasset …*, 9:25 *Eoque in curru prostrato,*, 10:13 *Quumque illi respondissent …*, 10:17 *Illo in currum
  evecto,*, 10:22 *Qui postquam ad unum omnes … jungerentur:*, 10:23 *iisque prolatis,*, 10:26 *Deinde in oppidum
  templi Baalis profecti,*, 11:16 *Nolebat enim sacerdos …* (a closing reason, KJV 15b), 11:19 *Pontifex Jovae templo
  custodiis munito,*, 13:16 *Quumque ille arcum et sagittas cepisset:*, 14:27 *Quumque nullus esset, qui eis
  auxilium ferret:*, 16:3 *Is tantum abfuit … fecerat,* (KJV 2b).
- **Splits inside a sentence where the KJV verse's words stand clear**: 9:21 at *jussit Joramus*; 9:28 at *et a suis
  Hierosolymam* (*Ille ad Mageddonem fugit, ibique mortuus est,* is KJV 27's end); 10:11 at the main verb *Samariam ire
  contendit* and 10:12 at *nactus Ochoziae*; 10:16 at *seque comitari*; 10:21 at *curavit, ut ex*; 10:32 at *a Jordane
  ad exortum*; 11:5 at *atque ita praecipit* (*eisque regis filium ostendit,* is KJV 4's end); 11:19 at *centuriones,
  stipatores* (its subject *Pontifex* stays with the ablative absolute, as 3:4's *Mesa*) and at *universi laetati*;
  14:1, 15:32 and 16:2 at *annos tum natus*, 15:1 at *annum tum agens*, and 15:22 at *anno Azariae Judaeae regis
  quinquagesimo* (the age or the date of the next KJV verse, as 8:17); 16:3 at the second *ut* clause *ut,
  israeliticorum regum mores imitatus*.
- **Speech introductions at a verse's end left where Castellio puts them**: 9:30 *Jehu praetereunte portam, dixit:*
  (KJV 31 'And as Jehu entered in at the gate, she said').
- **Sentences left as Castellio divides**: 9:33, KJV 33's last clause 'and he trode her under foot' is *Ille, ea
  conculcata,*, the subject and ablative absolute of KJV 34's *ivit ad sumendum cibum*; 11:2–3, KJV 2's 'and they hid
  him … from Athaliah, so that he was not slain' is *eumque ex Athaliae conspectu abditum, et a morte vindicatum,*,
  participles of KJV 3's *habuit in Jovae templo occultum*; 12:10–11, KJV 10's 'and they put up in bags' is *inque
  loculos relatam,*, a participle of KJV 11's *tradebant*; 12:20–21, KJV 20 and 21a are one clause (*Hic Joas a suis
  Jozabaro … facta conjuratione, occisus est apud Mellonem domum*), so KJV 21's 'For Jozachar … smote him' stays in
  20 and 21 begins at *Eoque … sepulto* (reader 06); 17:40, KJV 40's 'but they did after their former manner' is
  *suosque pristinos mores retinentes illae gentes,*, whose subject goes on into 41.
- **Readers' doubts**: 13:16 and 13:17 (margins lost in the gutter, placed by sense) are the KJV's starts once
  *Quumque ille arcum et sagittas cepisset:* goes back to 15; 13:25 at *Joas Joachazi filius* and 17:19 at *eousque*
  are the KJV's starts; nothing moves there.
- No `absent`, no `opens`: every KJV verse of 9–17 has Latin of its own.
