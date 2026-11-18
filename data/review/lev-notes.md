# Leviticus: light notes (Old Testament search)

Built 2026-11-18 by the process in `ot-notes-process.md` (decisions 1A–4A), as `gen-notes.md` and `exod-notes.md` were:
kind A when the NRSVue and the BSB both leave the Hebrew for an ancient version and Castellio keeps it; kinds B and C
where his reading or his text departs from the Hebrew against the NRSVue, the BSB and the Hebrew agreeing, and nobody
calls the passage uncertain. Formulas as in `notes-audit.md` §A and the Genesis and Exodus notes.

**Sources read:**
- `lev-notes-candidates.md` (`python -m pipeline notes Lev`): 1 BSB version note, 31 numbers, 3 short verses; no
  *G.* … *H.* marks.
- The NRSVue (Bible Gateway, read 2026-11-18) for all 27 chapters with its footnotes, by two readers (1–13, 14–27),
  each reading the Latin verse by verse against the WLC, the BSB with its footnotes (`sources/parallel/bsb/files/`)
  and the KJV, with the Vulgate and Brenton's LXX where a verse looked odd. Each item below was checked here against
  the files. The NET notes could not be loaded (netbible.org again served the wrong passage); no item below rests on
  a dispute.
- The printings: 1738 as printed (`text/orig/LEV.usfm`) and its raw OCR (`sources/archive/1738/text.txt`), the 1750
  raw OCR (`sources/archive/1750/text.txt`), and for items 2 and 3 the 1573 OCR through the MDZ search (canvases 105
  and 108; no 1573 page image read). 1551 not looked at.
- Castellio's 1554 annotations (`lev-notes-1554.md`): nothing on any item below.

The yield is 3 notes in 27 chapters (0.1 a chapter), with the 4 notes already there.

## A. Modern Bibles follow the versions (kind A)

None. The BSB's one note against the Hebrew, 14:31 (the LXX and Syriac drop the Hebrew's repeated "such as he can
afford"; the NRSVue goes the same way), changes nothing: Castellio keeps the repetition (*prout feret ejus facultās,
utrumcumque cōnsequī potuerit*) and the sense is the same.

## B. Castellio's reading or text departs from the Hebrew (kinds B and C)

Each stands in 1738 and 1750 (items 2 and 3 in 1573 too): Castellio's own text, so noted, not corrected.

**Decision:** accept (Nathan, 2026-11-18: "Apply all")

1. **11:21** *quæ suprā pedēs crūra nōn habent ad saliendum humī*: the Hebrew is written אֲשֶׁר־לא כְרָעַיִם, "which
   not legs", and read (the Qere) אֲשֶׁר־לוֹ כְרָעַיִם, "which have legs above their feet, to leap with on the ground".
   Castellio translates the written "not", which turns the law round: the winged creepers one may eat would be those
   *without* leaping legs, and the next verse (11:22) lists the locusts and grasshoppers, which leap. The NRSVue ("that
   have jointed legs above their feet", no note) and the BSB ("having jointed legs above their feet for hopping", no
   note) read the Qere; so do the KJV, the Vulgate (*habet longiora retro crura, per quæ salit*) and the LXX (ἃ ἔχει
   σκέλη). 1738 *crura non habent ad saliendum humi* (`text/orig` line 339; OCR lines 17210–17211), 1750 the same
   (lines 15624–15625). Unlike Exod 21:8's Ketiv (left out: the BSB gives it as an alternative), no modern Bible or
   ancient version reads "not" here, and Castellio's own 11:22 contradicts it.
   **Apply:** `Lev.11.21` la: `crūra nōn habent ad saliendum` → `crūra nōn habent\f + \fr 11:21 \ft Hebraicē אֲשֶׁר־לוֹ כְרָעַיִם, ‘quæ crūra habent’; Castelliō לא, ‘nōn’, legit, ut scrīptum est.\f* ad saliendum`
2. **24:6** *Jōvæ in ārā pūrā appōnitō*: Hebrew עַל הַשֻּׁלְחָן הַטָּהֹר, "on the pure table" (the NRSVue "the table of pure
   gold", note "Heb *pure table*"; the BSB the same, no note; the KJV "the pure table"; the Vulgate *super mensam
   purissimam*). The bread of the Presence lies on the table, which Castellio calls *mēnsa* everywhere else (Exod
   25:23, 25:30, 26:35, 30:27, 37:10, 39:36, 40:4, 40:22; Num 4:7). 1738 *in ara pura adponito* (`text/orig` line 853;
   OCR lines 19251–19252), 1750 *in ara pura apponito* (lines 17787–17788), 1573 *in ara pura apponi-* (canvas 105, OCR).
   The same kind as Exod 28:24 and 36:18.
   **Apply:** `Lev.24.6` la: `in ārā pūrā appōnitō:` → `in ārā pūrā\f + \fr 24:6 \ft Hebraicē עַל הַשֻּׁלְחָן הַטָּהֹר, ‘in mēnsā pūrā’.\f* appōnitō:`
3. **27:28** *sīve prædātōrius ager sit*: Hebrew וּמִשְּׂדֵה אֲחֻזָּתוֹ, "or of the field of his possession", his inherited
   land (the NRSVue "or inherited landholding", the BSB "or his inherited land", neither with a note; the KJV "the field
   of his possession"; the Vulgate *sive ager*; the LXX ἀπὸ ἀγροῦ κατασχέσεως αὐτοῦ). *Prædātōrius* makes it land taken as
   booty; Castellio seems to have read אֲחֻזָּה from אחז, "seize", though in the same chapter he gives the word as
   *possessiō* (27:16 *fundō suæ possessiōnis*, 27:24 *terræ possessiō*). 1738 *prædatorius ager* (`text/orig` line
   1025; OCR line 19914), 1750 (line 18469) and 1573 (canvas 108, OCR) the same. **Near the bar:** a real change of sense,
   but one adjective in a list. Leave it out if the bar is held strictly.
   **Apply:** `Lev.27.28` la: `prædātōrius ager sit,` → `prædātōrius ager\f + \fr 27:28 \ft Hebraicē שְׂדֵה אֲחֻזָּתוֹ, ‘ager possessiōnis suæ’.\f* sit,`

## C. The existing notes

All four stay:
- **13:48** (*in stāmine aut subtēmine*, kind B): Castellio's "outer and inner side", defended in 1554, against every
  version's threads or fabrics. The NRSVue's "uncertain" notes in that passage fall at 13:55, not 13:48.
- **21:4** (his emended Hebrew, with the Vulgate; kind C): the NRSVue and the BSB both "relatives by marriage", no note;
  the note's own *locus obscūrus* covers the dispute.
- **23:24** *monētum* (a coinage note).
- **23:40** *perseæ*: passes on precedent rather than the test (the NRSVue calls the phrase uncertain, and it is a
  plant), like Exod 30:24 *Īris*: the note gives Castellio's source, Josephus, not a reading of the Hebrew.

## D. Considered and left out

- **פָּרַע as *tondēre*** (10:6 *Capita vestra nē tondēte*, 13:45 *capite tōnsō*, 21:10 *caput nē tondētō*): the Hebrew is
  to let the hair hang loose (the NRSVue "dishevel", the BSB "let hang loose"; the KJV "uncover", the Vulgate
  *nudare*, *discooperire*). In these three verses the gesture is mourning, and cutting the hair was a mourning sign
  too (21:5 forbids it to priests), so the sense of the law stands. The same rendering at Num 5:18, outside mourning, is
  proposed in `num-notes.md` (item 2).
- **Near the bar:** 5:15 *argentī siclīs duōbus*: the Hebrew כֶּסֶף־שְׁקָלִים has no number (the NRSVue, the BSB, the KJV,
  the LXX); "two" is the Vulgate's (*duobus siclis*), the traditional reading of the plural. A version followed, but
  an old reading that changes little. 1738 and 1750 the same.
- **Only one of the NRSVue and the BSB leaves the Hebrew:** 9:19 (the NRSVue's kidneys from the Greek; Castellio with
  the Hebrew), 10:17 ("God" for "he"), 15:3 (the NRSVue adds a clause from Qumran, the LXX and the SP), 18:17, 26:12
  (the NRSVue drops "I will walk among you" with Qumran; Castellio keeps it).
- **The NRSVue calls the Hebrew uncertain:** 6:21; 13:2, 13:10, 13:19, 13:28, 13:43, 13:55; 11:18–19 (birds).
- **Old or disputed readings:** 6:18 and 6:27 *ut ea nōn nisi cōnsecrātī attingant* ("must be holy" for "becomes
  holy"; the KJV allows it), 1:16 *cum ipsīs plūmīs* (the KJV's and the Vulgate's feathers), 19:20 *verberibus* (with
  the KJV and the Vulgate; the NRSVue "inquiry", the BSB "punishment"), 26:40 *Ita fīet, ut … cōnfiteantur* (the
  waw-consecutive read as a statement).
- **Rare animals, birds, conditions and plants (no note by rule):** 11:5, 11:13–19, 11:22, 11:27 *palmipeda*, 11:29–30,
  21:20, 22:22, 17:7 *satyrīs*, 26:30 *simulācra*.
- **Vocabulary and paraphrase:** *lactēs* and *ōmentum* in 3–9, 8:8 *CLĀRITĀS ET INTEGRITĀS*, 7:35 *ūnctiō*, 8:7, 9:22
  *manū* (the Ketiv, trivial), 13:52 (the list of fabrics condensed), 15:32–33 (the summary leaves out one case),
  17:14 *capite plectendus*, 18:14, 21:2–3, 22:25, 25:45, 26:22.
- **Numbers:** every numeral matches the Hebrew (12:4–5's 33 and 66 days, 23's dates, 25's years, 27:3–7's valuations,
  27:16, 27:25). The tool's hits are *ambōs rēnēs* moved into the verse before (3:3–4, 3:9–10, 3:14–15, 4:8–9),
  *quadrupēs* (11:20–42), *iterum* and *septem alterōs* for שֵׁנִית (13:6–58), *bis septem* (12:5), *duōbusque
  arietibus* (8:2), the split verses of §E (15:28–30), and dates carried across verses (16:29, 23:26–27, 25:9, 26:8,
  27:3). 5:15 is above.
- **Short verses:** 3:5 (its words in 3:4), 13:52, 18:2 (the formula in 18:1).

## E. Found in passing: two places off the KJV's verse numbers (not a note)

The edition follows the KJV's numbering, but the settled text keeps 1738's at two places, which
`data/versification/Lev12-27.draft.edits.tsv` didn't touch (checked here against `sources/parallel/kjv/Lev.tsv`):

- **15:26–30:** Latin 26 is the KJV's 26a (the bed), Latin 27 its 26b (what she sits on), Latin 28–29 its 27–28, and
  Latin 30 its 29–30 (the birds brought, and the priest's offering).
- **19:26–28:** Latin 26 is the KJV's 26a (blood), Latin 27 its 26b (divination), Latin 28 its 27–28.

Each needs a merge and a split in `text/LEV.usfm` and `text/orig/LEV.usfm`, with `data/orig/Lev.pages.tsv`, the gold and
the `data/decisions/Lev.*.tsv` rows that name those verses.

**Decision:** fix them (Nathan, 2026-11-18: "Fix the versification"). Done the same day with the versification tool,
which moves only markers and checks the words and the KJV's verse counts: `data/versification/Lev.edits.tsv` (merge
15:27, split 15:30 at *quōrum ūnum sacerdōs*, merge 19:27, split 19:28 at *nēve corpora vestra*; now `applied`; report
in `Lev.REVIEW.md`), applied to `text/LEV.usfm` (`versify Lev --apply`, gold rebuilt) and to `text/orig/LEV.usfm`
(`--to`, the same edits, its spelling in each anchor). The `Lev.forms.tsv` rows for 15:28–29 and *columbā* (15:30)
and the `Lev.layout.tsv` row for 15:28 move to their new verses; `data/orig/Lev.pages.tsv` needs no change (every
verse concerned is on leaf 172 or 176).

A scan of Genesis–Deuteronomy for the same pattern (a verse much longer than the KJV's beside one much shorter) found
four more, each one of Castellio's sentences crossing the KJV's boundary where 1738's own number stands, not text
shifted a verse: Exod 40:34–35 (the reason clause *ut propter eum splendōrem* in 34), Lev 21:18–19 (the lame in 19),
Deut 22:18–19 (the fine *et centum argenteīs* in 18). Lev 15:32–33 was split deliberately in stage 2. Left as they are;
each could move its boundary to the KJV's words if you want the finer match.
