# Numbers 1–36: stages 3–5, one proposal per verse

Proposed 2026-11-16 (decision 30's standing rule), as Leviticus (`data/review/lev1-27-stages3-5.md`). Nathan:
"Continue" after stages 1–2. **Waiting for your approval**: your answers of 2026-11-16 are applied (below); a few calls remain.

## Where it stands

- **Stages 1–2**: 1738's own text, every line read on the page (`data/review/num1-36-stage2.md`; Wikisource has
  only 1:1). The draft `text/draft/NUM.usfm` has the KJV's 1,288 verses in every chapter: 138 versification edits
  (`data/versification/Num1-36.draft.edits.tsv`), 7:12–83 and the census at 1:22–43, 4:38–44 as verse ranges.
- **Corrections to the draft found here** (decision 30's rule; Apply lines in the stage-2 record, §"Corrections for
  the reading edition"): 6:3 *bibito* (1738 *bibtto*), 30:16 *Atque* (*Atquæ*), 10:6 Castellio's *G. L. … H.*
  dropped (as Lev 18:17), 3:30 ***Elsaphane*** for 1738's *Elisaphane* (the same man as Exod 6:22, Lev 10:4;
  decision 46). 5:14 *adfletur* is not a misprint (*adflētur*, subjunctive of *adflō*).
- **My modernizing of 1738's spelling, fixed** (`ocrdraft.modern`, `macronize.jv`, tested): 14:7 *ivissent*, 16:11
  *coivistis* (eō's perfect, had *jv*); the Hebrew names *Jaser*, *Jasubus*, *Jasam* (a Greek-word exception had
  caught *ias-*; it is now *iasp-*, *iaspis*, and changes nothing settled); *Jacobeis* and 10:5–6 *ovatu* (Wikisource
  forms that keep i/u now go through j/v; *coierunt* kept). 21:8–9 *fore*, *adspicerent*, *serpentem*: 1738 breaks
  the line without a hyphen; joined in the read lines.
- **Stages 3–5**: `data/review/num1-36-ch01.md` … `-ch36.md`, 1,202 items (one per verse; a range is one item), all
  checking `ok` (one `already`: a verse that needs no change). Preview: **`text/draft/NUM.preview.usfm`**.
- **Stage 2b** (the printed text, `text/orig/draft/NUM.usfm`): built from the read lines in the KJV's numbering; still
  to be read on the page for approval (paragraphs, marks).

## How the verses were made

Eight readers (1–4, 5–10, 11–14, 15–18, 19–22, 23–27, 28–31, 32–36) under one brief, Leviticus's rules. Their calls
are in `data/decisions/Num.layout.tsv` and `Num.forms.tsv`; four more readers proofread all 1,288 verses (about 165
problems), and a fifth applied the proofread (40 layout and 153 forms rows changed, each noted "proofread:").

- **Quotation marks** (1738 prints none): God's speech in “…” with the narrator's frames outside; the message for the
  Israelites unmarked inside it; every *inquit* inside speech with commas, the quotation closed and reopened
  (decision 65). Speech in the narrative quoted where Castellio gives the words (Moses and Hobab 10:29–32, the
  people's complaints 11, 14, 20, 21, Miriam and Aaron 12, the spies 13:27–29, Korah 16, Balaam and Balak 22–24,
  Moses and the Reubenites and Gadites 32, the Gileadites 36); reported where he puts them in indirect speech. Inner
  ‘…’ only at 5:19–22 (the priest's oath, the woman's *Amen, amen*), 6:24–26 (the blessing Aaron is to speak), 14:18
  (Moses quoting God), 23:7 (Balak's summons in the oracle). 160 “ and 142 ”: the 18 more open marks reopen a
  speech at a new paragraph; 28:31 runs on into chapter 29.
- **Poetry** where the BSB sets it: the priestly blessing 6:24–26, the ark's words 10:35–36, the Book of the Wars
  21:15, the song of the well 21:17–18, the taunt song 21:27–30, Balaam's seven oracles (23:7–10, 18–24; 24:3–9,
  15–19, 20, 21–22, 23–24).
- **Paragraphs**: the BSB's, moved to the sentence start where they fell inside one; added where a new speech begins
  or the narrator takes over (KJV 'And the LORD spake unto Moses'), and in long stretches where the BSB and WEB break.
- **Capitals** for adjectives of peoples and places (*Isrāēlīticus*, *Lēvīticus*, *Mōabīticus*, *Chananæus* …), as
  the settled Exodus and Leviticus have them (about 40 places).
- **A spelling exception**, the first of its kind: 25:12 *dīc, mē cum eō pācis inīre fœdus* is *mē* + *cum eō*, not
  the approved *mēcum*. `data/rules/exceptions.tsv` (`id old note`) now lists verses where an approved rule must
  not apply (`normalize.exceptions`, used by `propose` and `verses.respell`; tested).

## Names: one form per person in the book

Settled forms first (decision 46), then what most of Numbers had: *Nahasōn*, *Issāchar-*, *Āsēr-*, *Benjāmīn-*,
*Zabulōn-* (the OT's, not the NT's *Zabūlōnia*), *Nephthāl-*, *Gadin-* and *Cahathin-* (suffix unmarked, like the
settled *Rūbēninæ*), *Calēb-*, *Hōsēa*, *Phīnees*, *Bāsan-*, *Abār-*, *Pharan-*; *Sinæ* for Zin, *Sīnæ* for Sin and
Sinai; chapter 26's clans by the settled Genesis 46 (*Jāmīne*, *Jāchīne*, *Thōlā*, *Ōnan*, *Hāmūl*, *Gērsōne* …).
Names no source marks: Gaffiot first, then the Greek's long letters, then the Hebrew vowel.

## Your answers of 2026-11-16, applied

Nathan: "Apply rules that have already been approved to forms we have already seen. Before applying it to new forms,
be sure to research them (Gaffiot and classical corpus). In general, keep the 'original' version identical to the
prints, including errors. But correct clear errors in the edited edition … Decide 1 form for each person … I think
-īnus should be the standard … Double check the various printed editions for 'ceperat' vs 'coeperat' … match the clan
adjectives to their founders."

1. **The 47 spelling rules, researched and approved**, and one more found missing (*Beniaminea* → *Benjaminea*,
   13:9, 34:21): each new form looked up in Gaffiot (`latin macron`), Lewis & Short and the corpus (`latin attest`);
   46 apply outright (Gaffiot heads the new spelling: *appāreō, appellō, apprimō, ascendō, aspiciō, aspergō,
   ascīscō, sūmpsī, cōnsūmptrīx* (L&S), *contempsī, redēmptus, septentriō, causa*). **A tension in decision 37**:
   Gaffiot 2016 heads *adfectō, adferō, adficiō, adflō, adfluō, adgregō, adfor* with ad-; they are assimilated here
   because decision 37 assimilates and earlier approved rows already do it for these verbs (*afficī, afferēmus,
   afflātus, aggregābor*), the corpus mostly agreeing (*afficere* 65 : 30, *afflātus* 45 : 15). The weakest is 12:8
   *affābor* (*adfātus* 34 : *affātus* 27 in the corpus). The research, per form: `data/review/num1-36-rules-research.md`.
2. **Clear errors corrected in the edited text, the printed text keeping 1738** (`num1-36-stage2.md` items 5–6):
   16:47 ***clādēs cœperat*** (1554 *cœpe-|rat*, canvas 91; 1726 *coeperat*; 1738 and 1750 *ceperat*), 28:7
   ***tēmētum Jōvæ lībētur*** (1554 *Iouæ*, canvas 98; 1738 and 1750 *Ioua*). Checked in 1554 and kept, as
   Castellio's own: 35:14 *quārum* (canvas 102) and 36:8 *ex quācumque … tribuum* (canvas 103).
3. **-īnus the standard** for gentile and clan adjectives. Gaffiot's only short ones are adjectives of material from
   Greek -ινος (*cĕdrĭnus, byssĭnus, coccĭnus, hyăcinthĭnus, ŏnychĭnus, tĕrĕbinthĭnus, thyĭnus*; L&S *murrĭnus*) and
   *crastĭnus, prīstĭnus*, all already short in the text (`data/review/gentile-inus-research.md`). 48 corrected in Numbers (*Rūbēnīna, Gadīnī, Cahathīnōrum,
   Enāquīnōs* …) and Exod 6:14 ***Rūbēnīnæ*** in the settled text (`data/review/gentile-inus.md`, applied, gold
   rebuilt). Left: Gen 30:37 *castanīnīs* (Castellio's coinage; no source marks it).
4. **One form per person** (decision 46; the full table, 187 persons, places and clans: `data/review/num1-36-names.md`):
   66 spellings corrected in the draft (`num1-36-stage2.md` §"Names"): one spelling where 1738 prints a man two ways
   (*Abidan, Achira, Achiezer, Eliasaphus, Elisur, Phadasuris, Surisaddæi, Ammisaddæi, Amminadabi, Melca, Jazer,
   Calebus, Magdol, Haserothis* …, the Hebrew deciding), and Genesis 46 and Exodus 6's settled spellings for the same
   persons and clans in Numbers 3 and 26 (*Imma, Isvi, Beria, Bela, Phuva, Jacobeda* …; Castellio's own Genesis 46
   has these forms). 255 forms rows: the settled marking first, then Gaffiot/L&S, the Greek's long letters, the Hebrew
   vowel; **clan adjectives marked by their founders** with -īnus/-iānus/-ēnsis as Gaffiot's suffixes
   (*Jāsūbīna, Namūēlīna, Seredīna, Belāna, Asbēlīna, Immāna* …).

## The calls, decided (Nathan, 2026-11-16: "Accept 1-8")

1. **Decision 37 as written**: *ad-* assimilated also where Gaffiot heads the verb with *ad-* (*adficiō, adferō, adflō,
   adfluō, adgregō, adfectō, adfor*), as the approved rows already do.
2. **Gaffiot first for names (decision 52), over earlier settled markings**: *Eleāzar-* (Gaffiot *Elĕāzăr*),
   *Jebūsæ-* (*Jĕbūsæī*), *Samuēl* (*Sămŭēl*), *Pharan-* (*Phăran*), *Benjamītārum* (*Benjămītæ*, as Rom 11:1); Shelah
   *Sēla* by the Hebrew ṣere. In Numbers by 40 forms rows; in the settled books by `data/review/names-gaffiot.md` (25
   places in Gen, Exod, Lev, Matt, Acts, Heb, applied, gold rebuilt).
3. **Amalekites *Amālēchīt-*** by the founder *Amālēchus* and Wiktionary; the settled Gen 14:7, Exod 17:16 changed
   with them (`names-gaffiot.md`).
4. **Caleb, Balak, Balaam unmarked** (no source marks them; the order of decision 52 stops before the Hebrew).
5. **25:1 *Sittīmō*** for 1738's *Cittimo* (Shittim; 1554 *in Sittimo*, canvas 96; 1738's own 33:49 *Sittimorum*):
   `num1-36-stage2.md` item 67; the printed text keeps *Cittimo*.
6. ***Jācōbēus*** kept. 7. Inner ‘…’ at 5:19–22 and 6:24–26 kept. 8. Gen 30:37 *castanīnīs* kept.

9. **26:30 *Jeser*** (Iezer, אִיעֶזֶר) kept as the consonant the draft reads (Nathan, 2026-11-16: "Jeser (keep A)"): the
   Vulgate's *Jezer* and every modern Romance Bible read a consonant (Reina-Valera and NVI *Jezer*, Segond *Jézer*,
   Semeur *Yézer*, NR2006 and CEI *Iezer*, Almeida *Jezer*), and Castellio prints both men *Ieser*. Unmarked; Naphtali's
   son at 26:49 stays *Jēser* (Hebrew ṣere).

All the calls are decided.

**Decision:** accept, and Numbers 1–36 settled (Nathan, 2026-11-16: "Approve and settle")
