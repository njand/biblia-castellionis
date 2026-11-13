# Brackets for later passages, and light notes (proposal)

Proposed 2026-11-12 (Claude), from the New Testament checklist (`data/review/nt-publication-checklist.md`). Nothing is
applied until the Decision lines are filled in. Both changes touch every format, so each needs a small change to the
builds as well as to the text.

## 1. Brackets around passages not in the earliest manuscripts

Castellio translated the Greek printed in his day (Erasmus and Stephanus), and every passage below is in the settled
text, as in 1573. A modern critical text, the SBL Greek New Testament (SBLGNT, read from `sources/parallel/sblgnt`),
treats them as follows:

| Passage | SBLGNT | BSB |
|---|---|---|
| Mark 16:9–20 | in double brackets ⟦…⟧ | in the text |
| John 7:53–8:11 | in double brackets ⟦…⟧ | in the text |
| Matt 17:21, 18:11, 23:14; Mark 7:16, 9:44, 9:46, 11:26, 15:28; Luke 17:36, 23:17; John 5:4; Acts 8:37, 15:34, 24:7 (with the end of 24:6 and the start of 24:8), 28:29 | not in the text | not in the text (verse number only) |
| Rom 16:24 | in the text (with its variant mark) | not in the text |
| Matt 6:13b, the doxology *quoniam tuum est rēgnum …* | not in the text | not in the text |
| 1 John 5:7b–8a, *in cælō … in terrā* | not in the text | not in the text |
| Luke 22:43–44, 23:34a | in the text, with variant marks | in the text |

**Options**:

1. **Bracket, following the modern convention** (NA28, SBLGNT, ESV, NRSV):
   - Double brackets ⟦…⟧ around the two long passages, Mark 16:9–20 and John 7:53–8:11.
   - Single brackets […] around the verses and phrases the critical texts leave out: the third row, Rom 16:24, Matt
     6:13b, and inside 1 John 5:7–8, where Castellio's own parentheses would become brackets.
   - Luke 22:43–44 and 23:34a stay unmarked, as in SBLGNT and the BSB.
   - One sentence in the front matter explains the brackets.
2. Bracket only the two long passages.
3. No brackets; a front-matter note lists the passages instead.

**Recommendation: option 1.** Castellio's text stays whole, which a reader's edition of Castellio should keep. A reader
who knows a modern Bible sees at a glance what it lacks, and the marks are the ones modern editions already use. It
costs no apparatus: the brackets are characters in the USFM, so every build prints them as they are. Applying them
means one Apply line per passage start and end, about 40.

**Decision:** accept option 1: ⟦…⟧ around Mark 16:9–20 and John 7:53–8:11, […] around the passages the critical texts leave out (Nathan, 2026-11-12)

## 2. Light notes on translation

The edition has no notes now. The USFM has no `\f`, and `latex.py` drops footnotes. Candidates found so far:

- **Matt 19:24, Mark 10:25, Luke 18:25 *rudentem*** ("rope"; Castellio reads κάμηλος as a ship's cable, his annotation,
  1573 canvas 766; *not* the variant κάμιλος, as first written here). The Greek text now read
  has κάμηλος, "camel"; the Vulgate has *camelum*.
- **Jude 6 *ad magnī Deī jūdicium***: the Greek has μεγάλης ἡμέρας, "of the great day". 1573 and 1556 both print
  *Dei*, which may be Castellio's choice or a slip they share.
- **1 John 4:4 *quī in nōbīs***: the Greek has ἐν ὑμῖν, "in you". 1573 and 1556 agree.
- **1 Pet 5:8 *adversārius noster***: the Greek has ὑμῶν, "your".
- **Rev 3:1**, a verse Wikisource lacks, here from 1573 (decision 50 left this to the README; a note is the other place
  for it).

A full list needs one reading of the text against the modern critical text and the commentaries, for places where
Castellio's Latin says what the Greek now read does not. That reading suits your in-depth review, book by book.

**Options for the form**:

1. **Notes at the back** (*Notæ*), one line each, keyed by verse: "Matt 19:24 *rudentem*, 'rope': Castellio follows the reading
   κάμιλον; the Greek text now read has κάμηλον, 'camel'." The site gets a notes page with a link from each noted verse. The reading text stays clean.
2. Footnotes on the page (USFM `\f … \f*`). This is more apparatus than a reader's edition usually carries, and it
   needs footnote support in the PDF, EPUB and site.
3. No notes.

**Language of the notes**: Latin, to match the edition, or English, as the colophon and README are. **Recommendation:
English**, short. A reader who needs the note is better served by English, as the front matter already is.

**Recommendation: option 1, in English**. Start with the five above, and let your in-depth review add to the list.

**Decision:** Latin footnotes in the text (not option 1): Matt 19:24, Mark 10:25, Luke 18:25, Jude 6, 1 John 4:4, 1 Pet 5:8; not Rev 3:1 (Nathan, 2026-11-12)

### Nathan's direction so far (2026-11-12)

- **Footnotes in the text, in Latin**, kept unobtrusive: a small superscript letter in the text; in the PDF the notes
  in small type at the foot of the column; in the EPUB a pop-up note; on the site a note shown on tap or hover and
  listed at the chapter's end; in the plain text at the chapter's end. In the USFM: `\f + \fr 19:24 \ft …\f*`,
  normalized and macronized like the verses.
- **Matt 19:24, the model note** (his choice of five drafts, with *Castelliō*, and the judgment given to scholars):
  *Græcē κάμηλος; Castelliō fūnem nauticum intellegit, hodiernī Scrīptūræ interpretēs plērīque camēlum.*
  Castellio's own reasoning is in his annotation (1573, canvas 766; `docs/editions.md`): κάμηλος means both the animal
  and a ship's cable, and he takes the sense that makes the saying a hyperbole rather than an absurdity.
- Still to decide: the brackets (§1), and the list of notes beyond the first five.

## 3. The brackets (Apply lines for §1)

Placed so that the text reads on when the bracketed words are passed over: whole verses in […], with a closing ”
of a speech begun earlier left outside; John 5:3b and Acts 24:6b–8a with their punctuation inside; Castellio's
parentheses at 1 John 5:7–8 turned into brackets. A sentence in the front matter will explain them.

**Decision:** accept (Nathan, 2026-11-12, §1)

1. **Matt 6:13**, the doxology (its own poetry line)
   **Apply:** `Matt.6.13` la: `quoniam tuum est` → `[quoniam tuum est`
2. **Matt 6:13**, the doxology, end
   **Apply:** `Matt.6.13` la: `in sempiternum, āmēn.’` → `in sempiternum, āmēn.]’`
3. **Matt 17:21**, whole verse
   **Apply:** `Matt.17.21` la: `Cēterum hoc genus` → `[Cēterum hoc genus`
4. **Matt 17:21**, whole verse, end (the ” closes the speech of 17:20)
   **Apply:** `Matt.17.21` la: `jejūnium.”` → `jejūnium.]”`
5. **Matt 18:11**, whole verse
   **Apply:** `Matt.18.11` la: `Venit enim Fīlius` → `[Venit enim Fīlius`
6. **Matt 18:11**, whole verse, end
   **Apply:** `Matt.18.11` la: `servātum perdita.` → `servātum perdita.]`
7. **Matt 23:14**, whole verse
   **Apply:** `Matt.23.14` la: `Væ vōbīs scrībæ` → `[Væ vōbīs scrībæ`
8. **Matt 23:14**, whole verse, end
   **Apply:** `Matt.23.14` la: `dabitis pœnās.` → `dabitis pœnās.]`
9. **Mark 7:16**, whole verse
   **Apply:** `Mark.7.16` la: `Sī quis aurēs` → `[Sī quis aurēs`
10. **Mark 7:16**, whole verse, end
   **Apply:** `Mark.7.16` la: `audiat.”` → `audiat.]”`
11. **Mark 9:44**, whole verse
   **Apply:** `Mark.9.44` la: `‘Ubi nec` → `[‘Ubi nec`
12. **Mark 9:44**, whole verse, end
   **Apply:** `Mark.9.44` la: `exstinguitur.’` → `exstinguitur.’]`
13. **Mark 9:46**, whole verse
   **Apply:** `Mark.9.46` la: `‘Ubi nec` → `[‘Ubi nec`
14. **Mark 9:46**, whole verse, end
   **Apply:** `Mark.9.46` la: `exstinguitur.’` → `exstinguitur.’]`
15. **Mark 11:26**, whole verse
   **Apply:** `Mark.11.26` la: `Quod nisi ignōscētis` → `[Quod nisi ignōscētis`
16. **Mark 11:26**, whole verse, end
   **Apply:** `Mark.11.26` la: `dēlicta vestra ignōscet.”` → `dēlicta vestra ignōscet.]”`
17. **Mark 15:28**, whole verse
   **Apply:** `Mark.15.28` la: `Ita comprobātum` → `[Ita comprobātum`
18. **Mark 15:28**, whole verse, end
   **Apply:** `Mark.15.28` la: `habitus est.”` → `habitus est.”]`
19. **Mark 16:9**, the longer ending
   **Apply:** `Mark.16.9` la: `Resurrēxit autem` → `⟦Resurrēxit autem`
20. **Mark 16:20**, the longer ending, end
   **Apply:** `Mark.16.20` la: `signīs cōnfirmante.` → `signīs cōnfirmante.⟧`
21. **Luke 17:36**, whole verse
   **Apply:** `Luke.17.36` la: `Duōrum quī rūrī` → `[Duōrum quī rūrī`
22. **Luke 17:36**, whole verse, end
   **Apply:** `Luke.17.36` la: `alter relinquētur.”` → `alter relinquētur.]”`
23. **Luke 23:17**, whole verse
   **Apply:** `Luke.23.17` la: `Habēbat autem necesse` → `[Habēbat autem necesse`
24. **Luke 23:17**, whole verse, end
   **Apply:** `Luke.23.17` la: `per fēstum.` → `per fēstum.]`
25. **John 5:3**, 5:3b
   **Apply:** `John.5.3` la: `tābidōrum, aquæ mōtiōnem exspectantium.` → `tābidōrum[, aquæ mōtiōnem exspectantium].`
26. **John 5:4**, whole verse
   **Apply:** `John.5.4` la: `Angelus enim` → `[Angelus enim`
27. **John 5:4**, whole verse, end
   **Apply:** `John.5.4` la: `morbō tenērētur.` → `morbō tenērētur.]`
28. **John 7:53**, the woman taken in adultery
   **Apply:** `John.7.53` la: `Ita in suam` → `⟦Ita in suam`
29. **John 8:11**, the woman taken in adultery, end
   **Apply:** `John.8.11` la: `peccāre nōlī.”` → `peccāre nōlī.”⟧`
30. **Acts 8:37**, whole verse
   **Apply:** `Acts.8.37` la: `Et Philippus:` → `[Et Philippus:`
31. **Acts 8:37**, whole verse, end
   **Apply:** `Acts.8.37` la: `esse Jēsum Chrīstum.”` → `esse Jēsum Chrīstum.”]`
32. **Acts 15:34**, whole verse
   **Apply:** `Acts.15.34` la: `Sīlæ autem` → `[Sīlæ autem`
33. **Acts 15:34**, whole verse, end
   **Apply:** `Acts.15.34` la: `remanēre vīsum est.` → `remanēre vīsum est.]`
34. **Acts 24:6**, 24:6b
   **Apply:** `Acts.24.6` la: `comprehendimus, et ex lēge` → `comprehendimus, [et ex lēge`
35. **Acts 24:8**, 24:8a
   **Apply:** `Acts.24.8` la: `apud tē adessent: ex quō` → `apud tē adessent:] ex quō`
36. **Acts 28:29**, whole verse
   **Apply:** `Acts.28.29` la: `Hīs ab eō dictīs` → `[Hīs ab eō dictīs`
37. **Acts 28:29**, whole verse, end
   **Apply:** `Acts.28.29` la: `inter sēsē contentiōnem.` → `inter sēsē contentiōnem.]`
38. **Rom 16:24**, whole verse
   **Apply:** `Rom.16.24` la: `Favor Dominī` → `[Favor Dominī`
39. **Rom 16:24**, whole verse, end
   **Apply:** `Rom.16.24` la: `omnibus. Āmēn.` → `omnibus. Āmēn.]`
40. **1John 5:7**, the heavenly witnesses: Castellio's parentheses become brackets
   **Apply:** `1John.5.7` la: `(in cælō` → `[in cælō`
41. **1John 5:8**, the heavenly witnesses, end
   **Apply:** `1John.5.8` la: `in terrā)` → `in terrā]`

## 4. The notes (Apply lines for §2)

A footnote follows the word it explains: `\f + \fr 19:24 \ft …\f*`. The builds print a small letter there,
and the note in small type at the foot (PDF), as a pop-up (EPUB), on hover and at the chapter's end (site), and at
the chapter's end (plain text).

### 4a. *rudentem*: the model note (decided)

**Decision:** accept (Nathan, 2026-11-12: wording chosen from five drafts)

1. **Matt 19:24**
   **Apply:** `Matt.19.24` la: `rudentem per` → `rudentem\f + \fr 19:24 \ft Græcē κάμηλος; Castelliō fūnem nauticum intellegit, hodiernī Scrīptūræ interpretēs plērīque camēlum.\f* per`
2. **Mark 10:25**
   **Apply:** `Mark.10.25` la: `rudentem per` → `rudentem\f + \fr 10:25 \ft Græcē κάμηλος; Castelliō fūnem nauticum intellegit, hodiernī Scrīptūræ interpretēs plērīque camēlum.\f* per`
3. **Luke 18:25**
   **Apply:** `Luke.18.25` la: `rudentem per` → `rudentem\f + \fr 18:25 \ft Græcē κάμηλος; Castelliō fūnem nauticum intellegit, hodiernī Scrīptūræ interpretēs plērīque camēlum.\f* per`

### 4b. *rudentem*: the note reworded (decided, applied 2026-11-12)

*Scrīptūra* for the Bible is Church Latin, and *hodiernus* is classical of things (*hodiernus diēs*) but rare of
people. Three drafts were offered: *quī hodiē sacrās litterās ēnarrant, plērīque camēlum*; *plērīque nostræ ætātis
sacrārum litterārum interpretēs camēlum* (*interpretēs* also "translators", as Castellio himself is); *doctī nostræ
ætātis plērīque camēlum*. Macrons by Gaffiot (`pipeline latin macron`: *ætātis*, *plērīque*).

**Decision:** the third, *doctī nostræ ætātis* (Nathan, 2026-11-12)

1. **Matt 19:24, Mark 10:25, Luke 18:25** (each once)
   **Apply:** `Matt.19.24` la: `hodiernī Scrīptūræ interpretēs plērīque camēlum.` → `doctī nostræ ætātis plērīque camēlum.`
   **Apply:** `Mark.10.25` la: `hodiernī Scrīptūræ interpretēs plērīque camēlum.` → `doctī nostræ ætātis plērīque camēlum.`
   **Apply:** `Luke.18.25` la: `hodiernī Scrīptūræ interpretēs plērīque camēlum.` → `doctī nostræ ætātis plērīque camēlum.`

### 4b. Jude 6, 1 John 4:4, 1 Pet 5:8 (decided)

Readings 1573 and 1556 share against the Greek, the Greek of Castellio's day (Textus Receptus) included.

**Decision:** accept, the short wording of each (Nathan, 2026-11-12)

1. **Jude.1.6** *magnī Deī*: Græcē μεγάλης ἡμέρας, ‘magnī diēī’; Castelliōnis ēditiōnēs ‘Deī’ habent.
   **Apply:** `Jude.1.6` la: `magnī Deī jūdicium` → `magnī Deī\f + \fr 1:6 \ft Græcē μεγάλης ἡμέρας, ‘magnī diēī’; Castelliōnis ēditiōnēs ‘Deī’ habent.\f* jūdicium`
2. **1John.4.4** *quī in nōbīs*: Græcē ἐν ὑμῖν, ‘in vōbīs’; Castelliōnis ēditiōnēs ‘nōbīs’ habent.
   **Apply:** `1John.4.4` la: `quī in nōbīs, quam` → `quī in nōbīs\f + \fr 4:4 \ft Græcē ἐν ὑμῖν, ‘in vōbīs’; Castelliōnis ēditiōnēs ‘nōbīs’ habent.\f*, quam`
3. **1Pet.5.8** *adversārius noster*: Græcē ὑμῶν, ‘vester’; Castelliōnis ēditiōnēs ‘noster’ habent.
   **Apply:** `1Pet.5.8` la: `adversārius noster diabolus` → `adversārius noster\f + \fr 5:8 \ft Græcē ὑμῶν, ‘vester’; Castelliōnis ēditiōnēs ‘noster’ habent.\f* diabolus`
