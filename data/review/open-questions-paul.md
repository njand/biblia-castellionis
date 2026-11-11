# The open questions from Galatians–Philemon, with the evidence and a recommendation

Surveyed 2026-11-11 (Claude). Every question left open by `data/review/galcol-stages3-5.md`,
`data/review/thessphm-stages3-5.md` and their two fixes files, each with the evidence actually seen and a
recommendation. Sections A and B change the settled text and carry **Apply** lines (checked with `python -m pipeline
review check`); section C recommends keeping what the settled text has, so it changes nothing; section D is tools.
Nothing here is applied until you fill in its Decision line.

## A. The slips already proposed (`settled-fixes-galcol.md`, `settled-fixes-thessphm.md`): accept all

**Recommendation: accept all 11.** Each is a marking the grammar of its own verse rules out, and in each the settled
text's own majority, Gaffiot and the Greek agree on the fix:

- **1 Cor 7:21, 7:22, 7:37, 9:1, 9:19 *liber* → *līber*** (free, ἐλεύθερος; *liber* is "book", rightly at Luke 4:17).
- **Matt 13:46 *compāret* → *comparet*** (buy, ἠγόρασεν; *compāret* is "appear").
- **Luke 7:5 *idemque* → *īdemque*** (the centurion, masculine).
- **Acts 21:8 *Evangelistæ* → *Ēvangelistæ*** (as *ēvangelium*, Eph 4:11 *ēvangelistās*).
- **Luke 1:47 *servātōre* → *Servātōre***: the only lower-case one of 17 settled places (16 capital: Luke 2:11, John 4:42,
  Acts 5:31, 13:23, Eph 5:23, Phil 3:20, 1 Tim 1:1, 2:3, 4:10, 2 Tim 1:10, Titus 1:3, 1:4, 2:10, 2:13, 3:4, 3:6); decision
  20 names *Servātor*. The Magnificat's poetry is no reason to differ: the Father is *Deō*, capital, in the same line.
- **Rom 10:6 *dīxeris* → *dīxerīs***: every other settled perfect subjunctive is *-erīs* (*jūrāverīs*, *cēlāverīs*,
  *intrāverīs*, *crēdiderīs*, *amāverīs*, *dēstināverīs*, Col 2:21 *tetigerīs*, 1 Tim 5:19 *admīserīs*, 2 Tim 3:14
  *didicerīs*).
- **Matt 12:26 *Satanām* → *Satanam***: the other three accusatives are *Satanam* (Mark 3:23, Luke 10:18, Rom 16:20);
  no source marks the a long.

Their Apply lines are in those two files; accepting them there applies them.

## B. Changes recommended to the settled text

### B1. *Abrāhām-* and *Isaac-* in your Gospels, as everywhere else

The settled text writes *Abrāhām-* 159 times (89 in your own Genesis 1–27, 70 in the pipeline's books) and *Abrahām-* 13
times, all in your Matthew 1–13 and Luke 1–13; *Isaac-* 85 times (51 your own) and *Isaāc-* 5 times, all in the same
chapters. Wiktionary, the only source that marks them, has *Abrāhāmus* (and a variant *Ābrahām*) and *Isaā̆cus* (the
second a either way); WordPress 2019, your earlier macrons, writes *Isaacum*, *Isaacus*, *Isaacī*, *Isaacō* unmarked.
Nothing in the verses calls for a different form. **Recommendation: make the 13 + 5 agree with the majority.**

**Decision:** accept all (Nathan, 2026-11-11: "Apply all as recommended")

1. **Matt 1:1** **Apply:** `Matt.1.1` la: `prōgnātī Abrahāmō` → `prōgnātī Abrāhāmō`
2. **Matt 1:2** **Apply:** `Matt.1.2` la: `Abrahāmus genuit Isaācum.` → `Abrāhāmus genuit Isaacum.`
   **Apply:** `Matt.1.2` la: `Isaācus Jācōbum` → `Isaacus Jācōbum`
3. **Matt 1:17** **Apply:** `Matt.1.17` la: `ab Abrahāmō ad` → `ab Abrāhāmō ad`
4. **Matt 3:9** **Apply:** `Matt.3.9` la: `habēmus Abrahāmum.` → `habēmus Abrāhāmum.`
5. **Matt 3:9** **Apply:** `Matt.3.9` la: `nātōs Abrahāmō.` → `nātōs Abrāhāmō.`
6. **Matt 8:11** **Apply:** `Matt.8.11` la: `cum Abrahāmō, Isaācō et` → `cum Abrāhāmō, Isaacō et`
7. **Luke 1:55** **Apply:** `Luke.1.55` la: `Abrahāmō, et ejus` → `Abrāhāmō, et ejus`
8. **Luke 1:73** **Apply:** `Luke.1.73` la: `Abrahāmō patrī nostrō` → `Abrāhāmō patrī nostrō`
9. **Luke 3:8** **Apply:** `Luke.3.8` la: `habēmus Abrahāmum.` → `habēmus Abrāhāmum.`
10. **Luke 3:8** **Apply:** `Luke.3.8` la: `lapidibus Abrahāmō` → `lapidibus Abrāhāmō`
11. **Luke 3:34** **Apply:** `Luke.3.34` la: `Isaācī fīliī, Abrahāmī` → `Isaacī fīliī, Abrāhāmī`
12. **Luke 13:16** **Apply:** `Luke.13.16` la: `sit Abrahāmō` → `sit Abrāhāmō`
13. **Luke 13:28** **Apply:** `Luke.13.28` la: `dum Abrahāmum, Isaācum,` → `dum Abrāhāmum, Isaacum,`

### B2. Phil 4:2 *Evodiam* → *Euodiam*

1573 prints *Euodiam* (canvas 900, its OCR; Εὐοδίαν); the draft's *v* comes from the pipeline's u/v rule, not from Castellio. Gaffiot heads
*Ĕuŏdĭa* (u a vowel, nothing long), and every other Greek *eu-* name in the settled text keeps *Eu-*: *Eutychus* (Acts
20:9), *Eubūlus* (2 Tim 4:21), *Eunīcā* (2 Tim 1:5), *Euphrātēs* (Gen 2:14). **Recommendation: accept.**

**Decision:** accept all (Nathan, 2026-11-11: "Apply all as recommended")

1. **Phil 4:2** **Apply:** `Phil.4.2` la: `Evodiam exhortor` → `Euodiam exhortor`

### B3. 2 Tim 4:13 *Pēnulam* → *Pænulam*

Gaffiot heads the word *pænŭla* (`pipeline latin macron paenulam`: G *pænŭla*; *penulam*: no source knows the form); the
corpus favours *paenula* (24 hits, Cicero 2, against *penula* 5, the reader's count). Decision 42 spells by Gaffiot and
the corpus. 1573 prints *Penulam* (canvas 914, its OCR), the later e for æ. **Recommendation: accept** (and
the word rule `penulam → paenulam`, approved, for future drafts).

**Decision:** accept all (Nathan, 2026-11-11: "Apply all as recommended")

1. **2 Tim 4:13** **Apply:** `2Tim.4.13` la: `Pēnulam quam` → `Pænulam quam`

## C. Keep as settled (no change)

**Decision:** accept all (Nathan, 2026-11-11: "Apply all as recommended")

- **Hagar (Genesis) and Agar (Gal 4:24–25): keep each as printed.** *Reversed the same day by decision 46: one form,
  *Hagar*, in both (`data/review/names-one-form.md`).* Castellio spells her both ways himself: the 1573
  edition prints *Hagar* in Genesis (canvases 33 and 37, the MDZ search) and *Agar* in Galatians (canvas 891), the
  Hebrew form in the Old Testament and the Greek-Latin one in the New. Gaffiot heads *Agar*; no source knows *Hagar*.
  Making them one would correct Castellio, not the transcription.
- **The greetings' capital: keep.** One rule runs through all thirteen letters: *Grātiam* is capital where the greeting
  opens its own verse (1 Cor 1:3, 2 Cor 1:2, Gal 1:3, Eph 1:2, Phil 1:2, 2 Thess 1:2, Phlm 1:3) and lower case where it
  continues the address (Rom 1:7, Col 1:2, 1 Thess 1:1, 1 Tim 1:2, 2 Tim 1:2, Titus 1:4). 1 and 2 Thessalonians differ
  because their verse division differs, not their practice.
- ***Servātor* capital throughout** (16 places): decision 20; with item A's Luke 1:47 it is every place.
- **2 Tim 3:4, Castellio's L. … G. marks dropped, the words kept**: as your Matt 19:4 and Gen 44:6 (decision 32); 1573
  and 1556 print them, 1758, 1715 and 1750 drop them. The marks are Castellio's apparatus, not text.
- **Title lines *Epistola prior / posterior*** for 1–2 Thessalonians and 1–2 Timothy, as your 1–2 Corinthians, though
  1573 heads them *prima / secunda*: its arguments say *posterior*, and the edition is one style across the letters.
- **Capitals for the Spirit, as settled**:
  - Phil 3:3 *Spīritū Deum colimus*, set against *nōn carne frētī* in the same verse, as Rom 2:29 *Spīritū, nōn
    litterīs*, Rom 8:4 *nōn carnī … sed Spīrituī* and Gal 5:16–25: Castellio's spirit-against-flesh is the Spirit. John
    4:23–24 *in spīritū et vēritāte* is another idiom (no contrast with flesh) and stays lower case.
  - Eph 1:17 *auctōre Spīritū*: Castellio makes the Spirit the giver, a person.
  - 1 Tim 3:16 *per Spīritum commendātus est*: *per* makes it agent, against *in carne*.
  - 1 Thess 1:6 *Sānctī Afflātūs*: Castellio's *afflātus* here renders πνεύματος ἁγίου, the Holy Spirit by name
    (decision 20's *Spīritus Sānctus*). The four lower-case *dīvīnō afflātū* (Matt 22:43, Acts 20:22, 1 Cor 12:3, Eph
    2:22) are an adjective and a manner ("by divine inspiration").
- **Lower case, as settled**: 2 Tim 4:8 *jūstus jūdex* (a description in apposition; decision 20 lists no *Jūdex*); 2
  Thess 2:4 *quidquid dīcitur deus* and Phil 3:19 *prō deō habent* (false gods, as 2 Cor 4:4).
- **Layout, as settled**:
  - Phil 2:6–11, 1 Tim 3:16 and 2 Tim 2:11–13 as verse (the BSB; your Rom 11:33–36), no `\qt` (they are not earlier
    Scripture).
  - Gal 2:14 Paul's words to Peter closing at 2:14 (the BSB); 2:15 *Nōs nātūrā Jūdæī* reads as Paul to the Galatians.
  - Gal 3:6, 3:11, 3:12 in `\qt` without a formula: each keeps the Scripture's own words in the indicative (3:6 the
    same words as your Rom 4:3; 3:11 Hab 2:4 as Rom 1:17; 3:12 *per ea vīvet*), like Rom 9:7 and 10:18. Rom 10:5 is
    reported (*hominem … vīctūrum esse*), so its being unmarked is no inconsistency.
  - Eph 5:14 in `\qt`: Paul introduces it with his Scripture formula (Διὸ λέγει, as at 4:8), Castellio with *inquit*.
  - Eph 4:26 unmarked: Castellio recasts Ps 4:4 as *Ita īrāsciminī, ut nē peccētis*, no formula.
  - 2 Tim 2:19, the second clause unmarked: *itaque recēdat* makes it Paul's inference.
  - Col 2:21 in “…” without `\qt`: the teachers' precepts, not Scripture.
  - Eph 4:9 *“ascendit,”* in marks only, a word named (decision 39), not a quotation set in italics.
  - Phil 3:11 *perveniam.*: the full stop closes 3:8–11, as the Greek, BSB and KJV, so that 3:12 opens a paragraph.
- **Stage-2 readings, as settled** (each read on the 1573 image): the base edition's word where it makes sense (Gal 3:19
  *sequestrum*, 5:2 *circumcidemini*, Eph 4:16 *fit*, 6:12 *mundipotentes* as his 2 Cor 10:4 *dīvīnipotentia*, Phil 1:18
  *quoquomodo*, 1 Tim 1:10 *paediconibus*, 5:4 *quae*); 1556 where 1573 makes none (Col 2:5 *at* after *quamvis*; 1
  Thess 2:8 *nos* with *fuerimus* and *vobis*). **Phil 3:17** without *fratres*: 1573, 1556 and 1758 all omit it, so it
  is Castellio's text; the Greek's ἀδελφοί is no reason to add it (the edition does not correct his translation).
  **Eph 4:7 *pro portione*** as 1573, 1556, 1681 and 1726 print it.
- **Words no source marks, as settled**: *Dēmās* (Col 4:14) and *Zēnam* (Titus 3:13) from the Greek eta (Δημᾶς, Ζηνᾶν),
  the edition's rule for Greek names (*Cȳrēnēn*, *Joppēn*); *Eunīcā* (2 Tim 1:5) from Gaffiot's *Eunīcus* and νίκη's
  long ι; *Pācātiānæ* (1 Tim 6:21) from *pācātus* and *-iānus*; Gal 3:15 *sancītum*, the regular fourth-conjugation
  participle of *sanciō* beside Gaffiot's *sānctum* (no source marks *sancitum*; the least certain of these).

## D. Tools (no editorial change)

- **`pipeline draft`: lay the BSB's paragraphs after the versification edits.** In Colossians 4 the draft's breaks fell a
  verse late after 3:26 became 4:1 (the reader moved them). Recommendation: do it, with a test.
- **`mdz.fetch_crop`** cuts off a line carried over to the head of the next column (1 Tim 1:10, 2 Tim 1:13).
  Recommendation: widen the crop to the next column's first line when the word is a column's last.
- **`structure.quotes`** takes a dict of rows, and the readers each built one by hand. Recommendation: a `quotes` check in
  `propose` itself, printed with its counts.

**Decision:** accept all (Nathan, 2026-11-11: "Apply all as recommended")
