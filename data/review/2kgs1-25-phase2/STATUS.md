# 2 Kings phase 2: where it stands

Begun 2026-11-23 on Nathan's "Start phase 2", after the printed text was approved for now
(`../2kgs1-25-transcription.md`).

Done:
- `../2kgs1-25-draft-fixes.md` §1–2 (six slips and one accent, Castellio's mark at 5:26) applied to
  `text/draft/2KI.usfm`.
- `python -m pipeline propose 2Kgs 1-25` → `../2kgs1-25-ch01.md` … `-ch25.md` and `text/draft/2KI.preview.usfm`
  (before any reader's calls).
- `python -m pipeline notes 2Kgs` → `../2kgs-notes-candidates.md` (48 entries).
- Briefs: `BRIEF.md` (verse readers, names reader), `NOTES.md` (notes readers), `PROOF.md` (proofreaders); `merge.py`.

Readers, one at a time (the quota checked before each):

| id | chapters | state |
|---|---|---|
| r1 | 1–3 | done: 43 layout, 73 forms; three draft fixes (§3); asks: *adscend-*, *adferrī/adlātō/adfutūrum/adfluēbat* unassimilated (spelling rules); names *Elisæus*, *Jorāmus*, *Mēsa* for the names reader |
| r2 | 4–5 | done: 24 layout, 104 forms; no draft errors; asks: ¶ at 4:32 (or 4:25), ¶ inside 5:19 at *Cumque ille*, *Baalsālisā*, *Syrō* (Luke 4:27), *adpōneret/adfuit/adferrī/adfundī/adfuerim* unassimilated |
| r3 | 6–8 | done: 60 layout, 80 forms; draft fix *triumvir* ×3 (§3); asks: *væniitque*/*vænīrent* (*vēneō*) rule?, *cōnsūmtīs*/*sūmtīs* and *adfectūrus* rule gaps; ¶ 6:13 (or 6:15); names *Dothane*, *Amris* (1 Kgs *Ambri-*) |
| r4 | 9–10 | done: 53 layout, 40 forms; draft fix *Jonadabo* (§3); 9:16 *dēcubābat* kept (Gaffiot *dēcubō*); asks: ¶ at 9:22 (no KJV ¶ or indent), *fūgit* perfect 9:10, 9:27; rule gaps *sumta-*, *comsit*, *limphatus*?, *ad-*; names *Namsis* vs 1 Kgs 19:16 *Nansis*, *Gure*, *Jeblaam* |
| r5 | 11–14 | done: 16 layout, 47 forms; draft fix *introiverit* (§3); 12:1 `\nb` made `\p` (as 1 Kgs 3:1); asks: ¶ 12:4 (or 12:6), *Suriam* capitalized (gate of Sur), 12:5 *diœcēsī*; rule gap *sumsisset*; names *Hematha*/*Hemātham*, *Bersabā* vs Gen 28:10 |
| r6 | 15–17 | done: 14 layout, 75 forms; draft fix *Sepharvaim-* ×5 (§3); 16:1 made a paragraph; no quoted speech; asks: 17:5 ¶ taken out, ¶ at 17:7, 17:19, 17:34; names *Āzariæ*, *Ōsēa*, *Ozīæ*, *Gādis*, *Ezechīās* (decide once); 15:29 *Iōnem* kept (1 Kgs 15:20) |
| r7 | 18–19 | done: 42 layout, 61 forms; 19:5 *Ezechiani* = *Ezechīānī* (subject): draft fix §1.4 withdrawn and the draft restored (2026-11-23; `--items 4` also applied §3.4 *triumvir* early, harmless); *Ezechīās* for the book (Matt 1:9 *Ezecīās*); poetry 19:21b–34 on the BSB's lines; asks: ¶ 18:26 (or 18:28), poetry 19:21–34 or 21–28, 19:20 colon; rule gap *arctum*; *Jōa* nominative |
| r8 | 20–22 | done: 27 layout, 59 forms; no draft errors; 21:1, 22:1 made paragraphs; 20:20 ¶ out, 21:16 in, 21:19 → 21:18; asks: 21:18 ¶ (or 21:16–26 one), Huldah's nesting (or the BSB's), stops 22:15, 22:18; *adspernatus* (*aspernor*), *latumiis*, *promtuarium*; names *Berodacus Baladam*, *Ēsajās* vs NT *Ēsāiās* |
| r9 | 23–25 | done: 23 layout, 58 forms; draft fix *Pharvarim* (§3); no quoted speech; ¶ inside 23:30 at *Ejus in locum*; ¶ 23:4 out, 23:10 in, 23:21 → 23:20b, 23:28 → 23:29, 24:18 → 24:14, 25:22 → 25:21b; asks: reform split 23:10 (or 23:12, 23:15), 24:14; 24:15–16 keep 1738; names *Maachati*, *Jōhannēs* by rule |
| names | 1–25 | done: 138 rows (28 over the readers'); draft fixes §4 (*Ambris*, *Bethsemem*, *Chamosso*) applied; for Nathan: 1 Kgs 19:16 *Nansis* → *Namsis* by hand?, *Ezechīās* against Gaffiot, *Baladam*/*Baladan*, Hebrew-only marks, *Nethophatita*, *Reblatham* |
| notes A | 1–12 | done: one note proposed, 3:27 (*Hāc tantā atrōcitāte permōtī*: Hebrew "great wrath upon Israel"; near the bar); left out: 5:26 *ut emās*, 6:33 Josephus addition, 8:16, 8:21, 9:27, 10:30, 1738's footnotes; 1554: five annotations on 2 Kings (canvas 833), the asterisks 3:7, 4:37, 6:25, 6:33 match; *decubabat* and the 5:26 mark printed in 1554 and 1573; 8:16 revised in 1573; `docs/editions.md` § 2 Kings in 1554 and 1573 begun |
| notes B | 13–25 | done: no notes; left out near the bar 23:29 *adversus* (Apply ready), 25:19 *Sōphrem*, 16:6 *Syrōrum*, 20:4; all numerals match; 1554: the 20:13 annotation (*Paral.*, perhaps Isa 39:2) matches 1738's asterisk; 1738's five footnotes are 1554's margins; 19:13 *urbis* and 24:15–16 as 1738 in 1554 and 1573; *Baladam*, *Reblatham*, *Netophatita* printed so in 1554 and 1573 |
| p1 | 1–6 | done: 1 layout (¶ inside 1:4 at *Hīs ad nūntiōs*; 1:1–12 was 264 words), 1 forms (4:10 *dīversētur*); words all rules or fixes; rule gaps: nine *ad-* words (*adscendisses/-isti*, *adferri*, *adlato*, *adfluebat*, *adfundi*, *adponeret*, *adsiduo*); for Nathan: Matt 21:17 *diversātus* by hand?, *Scisne* unmarked, 6:22 *cēperis* |
| p2 | 7–12 | done: 0 layout, 2 forms (8:8, 12:18 *Hazælī* dative; 13:3 the same for p3); rule gaps *-mt-* (*consumtis*, *sumtis*, *sumtaque*, *adsumtisque*), *adfecturus*, *adferte*, *adlata*, *comsit*; for Nathan: *væniit*/*vænīrent* → *vēn-*?, *limphātus*/*lymphātus*, 11:1 colon kept |
| p3 | 13–18 | done: 1 layout (¶ at 18:36 *Ad hæc dicta*; 18:26–37 was 270 words), 6 forms (13:3 *Hazælī*, 13:7 *perditīs*, 14:16 *vītā*, 15:16 *pervāstāvit*, 18:25 *pervāstandum*, 18:2 *fīliā*); rule gaps *adpositum*, *adloquatur*, *sumsisset*, *adstrinxerat* (Nathan: *astringō* vs *adstō* rejected); for Nathan: *īnfest-*/*īnfēst-* across the Bible, 17:4 *Suam* |
| p4 | 19–25 | |

Merged 2026-11-23 (after r1–r9 and the names reader): draft fixes §1–4 applied to `text/draft/2KI.usfm`; `merge.py
--write` → `data/decisions/2Kgs.layout.tsv` (302) and `2Kgs.forms.tsv` (706); `propose 2Kgs 1-25` rebuilt the review
items and the preview (165 “, 17 ‘, balanced; 91 words unknown to every source, for the proofreaders).

Merged again 2026-11-23 after p1–p4: 26 spelling rows added to `data/rules/orthography.tsv` in approved families (18 *ad-*, six *-mpt-/-mps-*, *sæptam*, *sæptum*); `merge.py --write` → 304 layout and 721 forms rows; `propose` rebuilt the items and preview (719 items `ok`; the note at 3:27 `ok` against the preview). Tests pass (218).

Done: `../2kgs1-25-edition.md` written for Nathan.

Settled 2026-11-23 on Nathan's answers (`../2kgs1-25-edition.md` Decision): `final-forms.tsv` (41 rows: *Ezechiās* ×36, *Scīsne*, *vēniitque*, *vēnīrent*, *lymphātus*, *lautumiīs*, *adstrīnxerat*) and `final-layout.tsv` (11:1) merged last; the names reader's 25:23 *Nethōphātīta* row dropped. 305 layout and 754 forms rows.
