# Ruth: one form per person, place and people (Claude, 2026-11-19)

Every capitalized word of `text/draft/RUT.preview.usfm` (and its draft `RUT.usfm`), and every lower-case adjective of
a people or place (*moabiticus*), was grouped by its unmarked key, read in its verse for its case, matched to the
Hebrew (WLC) and the Greek (Brenton, `sources/parallel/lxx/Ruth.tsv`), and decided as Judges was
(`judg1-21-names.md`): the settled form first (decision 46, `data/gold/`: Genesis–Judges and the NT), then Gaffiot
(`pipeline latin macron`; of Ruth's names it gives only *Booz, Ephrāta, Nŏĕmī, Phāris, Rachel, Ruth, Thamar*), then the
Greek's η/ω/ει, then another dictionary (Wiktionary: *Līa, Rāchēl, Ramus* bare, *Isaeus*), then the Hebrew vowel
(decision 52). Case endings read in each verse.

**Counted**: 27 rows below, about 30 persons, places and peoples; 14 rows kept wholly as the preview has them, 13
changed in some form. **Outputs** (scratch folder; built by `names/build.py`): `names.spelling.tsv` (5 spelling
changes, each `old` checked by script to occur exactly once in its verse of `text/draft/RUT.usfm`, as a word and as a
string) and `names.forms.tsv` (61 forms rows, only where the decided form differs from the preview; no `#2` row
needed). **Check**: `check.py names/empty.layout.tsv names.forms.tsv`: 61 rows, 5 errors, every one a row for a
respelled word that takes effect once its spelling row is applied (1:2 *Ephrātæī*; 4:18 *Hesrōnem*; 4:19 *Hesrōn*;
4:20 *Nahasōnem, Nahasōn*).

The printed text (`text/orig/RUT.usfm`) keeps 1738's spellings whatever is decided here: *Noemis, Ephrattæi,
Hezronem, Hezron, Nahassonem, Nahasson*. 1738 prints *Hezronem* (4:18) where Wikisource has *Hezeronem*; the draft
follows 1738, and the edition goes on to the settled *Hesrōn-*.

## Hard calls (for Nathan)

1. **Naomi: *Noemis, Noemim, Noemī*** (19 times), not the preview's ***Nœmis, Nœmim, Nœmī***. The spelling rule made
   the *oe* a diphthong; Gaffiot gives the name as *Nŏĕmī*, o and e short and in hiatus (Greek Νωεμίν, Hebrew נָעֳמִי:
   three syllables), so no ligature and no mark on the first two vowels (Gaffiot before the Greek ω). As Judges'
   *Jezraelis* (hiatus, not *Jezrælis*). Castellio declines it as a Latin i-stem: nominative *-is* and accusative
   *-im* short, dative and ablative *-ī* long (Gaffiot's final ī). If you would rather carry Gaffiot's ī through the
   nominative (*Noemīs*), that is 10 rows to change; the accusative stays short before final m.
2. **Hezron: *Hesrōnem, Hesrōn*** (4:18, 4:19; 1738 *Hezronem, Hezron*): the same son of Perez as the settled Gen 46:12
   *Phārēs autem Hesrōnem … habuit* and Num 26:21 *Hesrōn, ā quō Hesrōnia* (חֶצְרוֹן in all three). Two spelling rows
   (z → s); drop them to keep 1738's *Hezrōn-* (ō by the Hebrew holem). The NT's *Esrōmus* (Matt 1:3, from the Greek
   Ἐσρώμ) is not followed: the OT's settled form is the nearer.
3. **Nahshon: *Nahasōnem, Nahasōn*** (4:20; 1738 *Nahassonem, Nahasson*): the settled Exod 6:23 *Nahasōnis*, Num 1:7,
   2:3, 10:14 *Nahasōn* (נַחְשׁוֹן). Two spelling rows (ss → s), as Judges' *Chamōssus* (one form, the settled one). The
   NT's *Naasson, Naassōnem* (Matt 1:4, Luke 3:32) follow the Greek Ναασσών and are not followed here.
4. **Ephrathites: *Ephrātæī*** (1:2; 1738 *Ephrattæi*): the settled Judg 12:5 *Ephrātæī* and the town *Ephrāta, -æ*
   (Gen 35:19, 48:7; Gaffiot *Ephrāta*; Ruth 4:11 *Ephrātæ* already). One spelling row (tt → t).
5. **Elimelech: *Elīmelechus, Elīmelechī*** (7 times): ī for the hireq-yod of אֱלִימֶלֶךְ (decision 52), no settled,
   Gaffiot or Greek evidence. Judges marked the same element so (*Abīnōamī, Abīezeriānī*), but left *Abimelech-*
   unmarked because the settled Gen 20 *Abimelechus* is; if you would rather follow that analog, drop the 7 rows.
6. **Ram: *Rāmum, Rāmus*** (4:19) kept as Castellio spells them, ā by the qamets of רָם (and Wiktionary *Ramus*), though
   the settled NT has *Arāmus, Arāmum* (Matt 1:3–4, Luke 3:33, from the Greek Ἀράμ). No OT settled form; Castellio's
   OT form is from the Hebrew, as *Hesrōn* is against *Esrōmus*. Say if the NT's form should come in (two spelling
   rows *Ramum* → *Aramum*, *Ramus* → *Aramus*).
7. ***Mōabītis*** (nominative singular, 1:22, 2:2, 2:6, 4:5): the preview had *Mōabītīs* from the settled Deut 2:11
   *ā Mōabītīs* and Judg 3:30 *potestātem Mōabītīs*, both *Mōabīta*'s ablative or dative plural. Here it is the
   feminine *Mōabītis, -idis* (Gaffiot *Mōăbītis*; settled Judg 11:18 *Mōabītidis*), "Ruth the Moabitess", short -is.
   Likewise 1:4 ***Mōabītidas*** (the preview had it unmarked).
8. **Capitals of *moabiticus*, for the layout merge** (1:1, 1:2, 1:22, 2:6, 4:3, *in agrum moabiticum*, *ex agro
   moabitico*): 1738 prints it lower case and the draft and preview follow; the settled text capitalizes *Mōabītic-*
   every time (12 in `data/gold/`: *Mōabīticō* ×10, *Mōabīticum, Mōabīticā, Mōabīticīs*). The marks are right either
   way; capitals are the layout reader's (no forms row here changes case). One form would capitalize the five.

## Noticed, not names

- **Ruth's name in the book's headers** (`\h`, `\toc1`, `\toc2`, `\mt1` *Rutha*): unmarked in both the draft and the
  preview; the edition's form is *Rūtha*. Not a verse, so no row; for the merge.
- **The settled Luke 3:32 *Ōbēdīs*** has a long genitive -īs (Matt 1:5 *Ōbēdem*, Ruth's *Ōbēd, Ōbēdem*): probably a slip
  in settled text (third-declension genitive -is). Not changed (settled text is never rewritten); Ruth has no genitive
  of Obed.
- *Māram* (1:20, "call me Mara", מָרָא) kept as the preview marks it (Hebrew qamets); *omnipotēns*, *Deus* not names.

## Settled forms that disagree (not changed: settled text is never rewritten)

- OT against NT for the same men: *Hesrōn* (Gen 46:12, Num 26:21) against *Esrōmus* (Matt 1:3, Luke 3:33);
  *Nahasōn* (Exod 6:23, Num) against *Naasson* (Matt 1:4, Luke 3:32); *Ammīnādāb-* (Exod 6:23, Num) against
  *Amīnādāb-* (Matt 1:4, Luke 3:33); *Īsæus* (Acts 13:22, Luke 3:32) against *Jessæus* (Matt 1:5–6). Ruth follows the
  OT's forms throughout (Castellio's OT spellings are from the Hebrew).

## Decisions

| Person / place / people | Hebrew · Greek | In Ruth (preview) | Decided | Reason |
|---|---|---|---|---|
| Jova | יְהוָה | *Jōva, Jōvam, Jōvæ*; *Jōva* 4.13 | *Jōvā* 4.13 | ablative absolute (*Jōvā conceptum dante*); settled *ā Jōvā* |
| Bethlehem | בֵּית לֶחֶם · Βηθλεέμ | *Bēthlehēma* 1.1, 1.2, 2.4; *Bēthlehemam* 1.19, 1.22; *Bēthlehemæ* 4.11 | *Bēthlehemā* 1.1, 1.2, 2.4 | settled *Bēthlehemā* (Judg 12:8, 17:7, 19:1, John 7:42); ablatives (*ā, ex*, *adveniēns*) |
| Judaea | | *Jūdææ, Jūdæam* | kept | settled |
| Moab (the land, adjective) | מוֹאָב · Μωάβ | *mōabīticum* 1.1, 1.2; *mōabīticō* 1.22, 2.6, 4.3 | kept (capitals: hard call 8) | settled *Mōabītic-* |
| Moabites; Moabitess | מֹאֲבִיּוֹת · Μωαβίτιδας | *Mōabītās* 1.6; *Moabitidas* 1.4; *Mōabītīs* 1.22, 2.2, 2.6, 4.5; *Mōabītidem* 4.10 | *Mōabītidas*; *Mōabītis* ×4 | settled *Mōabītidis*, Gaffiot *Mōăbītis* (hard call 7) |
| Elimelech | אֱלִימֶלֶךְ · Ἐλιμέλεχ | *Elimelechus* 1.2, 1.3; *Elimelechi* 2.1, 2.3, 4.3, 4.9 | *Elīmelechus, Elīmelechī* | Hebrew hireq-yod (hard call 5) |
| Naomi | נָעֳמִי · Νωεμίν | *Nœmis* ×10, *Nœmim* ×3, *Nœmī* ×6 | *Noemis, Noemim, Noemī* | Gaffiot *Nŏĕmī*; hiatus (hard call 1) |
| Mara | מָרָא | *Māram* 1.20 | kept | Hebrew qamets |
| Mahlon | מַחְלוֹן · Μααλών | *Mahalon* 1.2, 1.5; *Mahalonis* 4.9, 4.10 | *Mahalōn, Mahalōnis* | Greek ω, Hebrew holem |
| Chilion | כִּלְיוֹן · Χελαιών | *Chelion* 1.2, 1.5; *Chelionis* 4.9 | *Cheliōn, Cheliōnis* | Greek ω, Hebrew holem |
| Ephrathites; Ephrathah | אֶפְרָתִים; אֶפְרָתָה · Ἐφραθαῖοι | *Ephrattæi* 1.2; *Ephrātæ* 4.11 | *Ephrātæī* (spelling); *Ephrātæ* kept | settled Judg 12:5, Gen 35:19 (hard call 4) |
| Orpah | עָרְפָּה · Ὀρφά | *Orpha* 1.4, 1.14 | kept | qamets hatuf, Greek ο: short; nominatives |
| Ruth | רוּת · Ῥούθ | *Rūthā* ×9 (all nominative); *Rutham* 2.8, 4.10, 4.13 | *Rūtha, Rūtham* | settled *Rūthā* (Matt 1:5, an ablative), shureq |
| Boaz | בֹּעַז · Βοόζ | *Boozus, Boozum, Boozī*; *Boozo* 4.8 | *Boozō* 4.8 | settled *Boozus, Boozum, Boozī* (unmarked stem); dative |
| Israel; Israelites | | *Isrāēlis* 4.11; *Isrāēlītās, Isrāēlītārum* | kept | settled |
| Rachel; Leah | רָחֵל; לֵאָה | *Rāchēlis, Līæ* 4.11 | kept | settled (Gen 29–35) |
| Perez | פֶּרֶץ · Φαρές | *Phāris* 4.12, 4.18; *Phārēs* 4.18 | kept | settled (Gen 38:29, Num 26:20–21), Gaffiot *Phāris* |
| Tamar | תָּמָר | *Thāmāre* 4.12 | kept | settled Gen 38, Matt 1:3 |
| Judah | יְהוּדָה | *Jūdās* 4.12 | kept | settled Matt 1:3 |
| Obed | עוֹבֵד · Ὠβήδ | *Ōbēd* 4.17, 4.22; *Ōbēdem* 4.21 | kept | settled Matt 1:5 |
| Jesse | יִשַׁי · Ἰεσσαί | *Īsæī* 4.17; *Īsæum, Īsæus* 4.22 | kept | settled Acts 13:22, Luke 3:32 |
| David | | *Dāvīdis, Dāvīdem* | kept | settled |
| Hezron | חֶצְרוֹן · Ἐσρώμ | *Hezronem* 4.18; *Hezron* 4.19 | *Hesrōnem, Hesrōn* (spelling) | settled Gen 46:12, Num 26:21 (hard call 2) |
| Ram | רָם · Ἀράμ | *Rāmum, Rāmus* 4.19 | kept | Hebrew qamets; no OT settled form (hard call 6) |
| Amminadab | עַמִּינָדָב · Ἀμιναδάβ | *Amminadabum* 4.19; *Amminadabus* 4.20 | *Ammīnādābum, Ammīnādābus* | settled Exod 6:23, Num 1:7 *Ammīnādābī* |
| Nahshon | נַחְשׁוֹן · Ναασσών | *Nahassonem, Nahasson* 4.20 | *Nahasōnem, Nahasōn* (spelling) | settled Exod 6:23, Num 1:7 (hard call 3) |
| Salmon | שַׂלְמָה, שַׂלְמוֹן · Σαλμών | *Salmōnem* 4.20; *Salmōn* 4.21 | kept | settled Matt 1:4–5 |
