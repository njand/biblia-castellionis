# 1 Peter–Jude: stages 1–5, one proposal per verse

Proposed 2026-11-12; **approved by Nathan "for now" the same day and settled in
`text/1PE|2PE|1JN|2JN|3JN|JUD.usfm`** (decision 48), the title lines and the calls below as proposed. Same tools and format as Hebrews and James
(`data/review/hebjas-stages3-5.md`; `data/review/mark6-16-stages3-5.md` explains the format). You have no earlier
work on these books; `TXT/1 - OCR` (the 1726–27 printing, uncorrected) served as a witness, read as an OCR.

## Where it stands

| Book | Verses | Words | Stage 2 corrections | Layout lines | Forms decided | Items `ok` |
|---|---:|---:|---:|---:|---:|---:|
| 1 Peter 1–5 | 105 | 1,664 | 29 | 33 | 41 | 105 |
| 2 Peter 1–3 | 61 | 1,014 | 13 | 14 | 36 | 61 |
| 1 John 1–5 | 105 | 1,854 | 28 | 39 | 13 | 105 |
| 2 John | 13 | 211 | 4 | 5 | 3 | 13 |
| 3 John | 14 | 196 | 1 | 1 | 3 | 14 |
| Jude | 25 | 407 | 11 | 10 | 15 | 25 |
| **All** | **323** | **5,346** | **86** | **102** | **111** | **323** |

- **Stage 1**: `text/draft/1PE|2PE|1JN|2JN|3JN|JUD.usfm`, Wikisource with the BSB's paragraphs. **3 John had a verse
  too many**: 1573 (canvas 928) and Wikisource number the greetings *Salutant te amici. Saluta amicos nominatim* as
  verse 15; joined to 14, where the KJV has them (`data/versification/3John.draft.edits.tsv`). The others needed none.
- **Stage 2**: `data/review/1pet1-5-stage2.md`, `2pet1-3-`, `1john1-5-`, `2john1-`, `3john1-`, `jude1-stage2.md`;
  every correction **read on the 1573 page image** (crops in `sources/mdz-1573/crops/{1Pet,2Pet,1John,2John,3John,Jude}.*`,
  113), the doubtful ones looked at again by me (1 John 4:4, Jude 6, 2 Pet 1:17–18). Applied to the drafts (decision
  30's standing rule; 93 Apply lines). In 1573 these letters stand between James and Hebrews (canvases 920–929).
  - Wikisource is again the early wording: *favor → gratia* (1 Pet 1:2, 5:10; 2 Pet 1:2; 2 John 3); 1 Pet 1:20
    *praecogniti → Provisi*, 3:20 *quibus olim persuasum non fuerat → Qui olim non paruerant … semel*, 3:21
    *testificatio → stipulatio*, 4:1–2 *pro vobis carne*; **1 John most of all**: *caritas → amor* through 4:7–18,
    *quod → quia* (2:12–14), 3:4 *crimen → noxa*, 4:2–3 and 2 John 7 *corporatum*, *nomini fidem habere → in nomen
    credere* (3:23, 5:10, 5:13), 4:20 *qui possit amare*; Jude 4 *et solum herum Deum*.
  - Wikisource's slips: 1 Pet 2:19 *sit* lost, 4:3 *cultris*, 2 Pet 2:7 *quia → qui a*, 2:15 *Balsami*, 1 John 2:6
    *isse*, 2:22 *Qui → Quis*, 3:17 *fit → sit* (f/s), 3 John 5 *feliciter → fideliter*, Jude 1 *in*, 15 *convincat*.
  - Verse boundaries inside the KJV's numbers: 1 Pet 1:24 *Aret herba, caditque flos* back in 24 (1573, KJV); **2 Pet
    1:17–18**: 1573 (with 1556 and 1758) puts the voice's words *hic est meus carissimus filius, in quo me oblecto* after
    *in sacro monte*, at the end of 18; the edition follows 1573's order under the KJV's numbers.
  - **1 John 5:7–8**: 1573 prints the heavenly witnesses in parentheses, with the margin note *Hæc ( ) in quibusdam
    exemplaribus non extant*; Wikisource has the words without them. The parentheses are restored (1 John section 2).
  - Kept against the Greek, because 1573 and 1556 agree: **1 John 4:4 *qui in nobis*** (ὑμῖν), **Jude 6 *ad magni Dei
    judicium*** (ἡμέρας; Wikisource *diei*), 1 Pet 5:8 *adversarius noster*, 1 Pet 1:4 *invietam* (no lexicon knows it).
    Kept out as 1573's misprint: 1 Pet 4:16 *aut* for *At*. Kept against 1573: 3 John 1 *Gaio* (1573 *Caio*), as the
    settled *Gāius*.
  - 1573's changes against 1556 (1 Pet 12, 2 Pet 3, 1 John 12) are in section 5 of each file and in `docs/editions.md`.
- **Stages 3–5**: `data/review/1pet1-5-chNN.md` (5 files), `2pet1-3-` (3), `1john1-5-` (5), `2john1-1-ch01.md`,
  `3john1-1-ch01.md`, `jude1-1-ch01.md`; 323 items, all checking. Previews **`text/draft/*.preview.usfm`**. Quotation
  marks balance in every book (1 Peter 9 “, 28 `\qt` lines; 2 Peter 3 “; Jude 2 “; the John letters none). Ledger: all
  16 chapters **settled**.
- **Spelling rules added** (11 word rows, `orthography.tsv`, under decisions 37, 42 and 46): *temptationibus*,
  *afferendum*, *acquisitus*, *affabiles*, *afficiatur*, *acquirentes*, *afficiamini*, *neglegam*, *inoboedientes* (the
  stem rule *obedi-* reaches only words that begin with it), and *Gomorra*, *Gomorraeque* (Jude 7, 2 Pet 2:6; the
  settled Genesis, decision 46).

## How the verses were made

Two readers took stage 2 and then stages 3–5, one for 1–2 Peter and one for 1–3 John and Jude, with the Greek (TR,
SBLGNT), the BSB, the KJV, the Vulgate and 1573's page beside each verse; their calls, each with its reason, are in
`data/decisions/{1Pet,2Pet,1John,2John,3John,Jude}.layout.tsv` and `.forms.tsv`. I then read all six previews whole.
Changed after that reading: 1 Pet 1:23 *renātī* lower case (the sentence runs on from 1:22 *amāte,*; 1573 *renati*),
2 Pet 2:5 *octāvō Nōā … cōnservātō* (ablative, as your Gen 6:13 *Cum Nōā*), and 1 Pet 2:8 *inobœdientēs* (the rule
above).

## Calls worth a look

- **Scripture in 1 Peter** in `\qt` with “…”, **as poetry where the BSB sets it**: 1:24–25 (Isa 40:6–8), 2:6 (Isa
  28:16), 2:7 (Ps 118:22, then Isa 8:14 after *et*), 3:10–12 (Ps 34:12–16), 4:18 (Prov 11:31), 5:5 (Prov 3:34, as your
  Jas 4:6); 1:16 (Lev 11:44) as prose. Prose resumes with `\m`. **Uncertain**: 3:14 (Isa 8:12, adapted, *illī … vōs*,
  marked). **Left unmarked**: 2:22–24 (Isa 53:9, 53:5; the BSB quotes them, but Castellio turns them into three
  relative clauses, *Quī … Quī … Quī*, and writes *vōs estis sānātī*), 2:25, 4:8 (Prov 10:12; the BSB does not quote
  it either), 2 Pet 3:8, 3:13.
- **Other speech**: 2 Pet 1:18 the Father's voice in “…”, not `\qt` (as your Matt 17:5); 2 Pet 2:22 the proverb in “…”
  (**uncertain**: only its first half is Prov 26:11); 2 Pet 3:4 the scoffers. **Jude 9** *“Increpet tē Dominus.”* and
  **Jude 15** Enoch's prophecy (1 Enoch 1:9) in “…” but **not `\qt`**, since neither is cited from Scripture (Jude 9
  tells the Assumption of Moses; 1 Enoch is not in Castellio's Bible); Jude 15 kept as prose, though the BSB sets it as
  four lines. Both **uncertain**.
- **Capitals for God** (decision 20): *Pater* and *Fīlius* wherever they mean God and Christ (1573 prints both lower
  case; about 40 places in 1 John); *Servātor* (2 Pet 1:1, 1:11, 2:20, 3:2, 3:18; 1 John 4:14; Jude 25); *Spīritus
  Sānctus*; 1 John 2:20 *ā Sānctō*. **Uncertain**: 1 John 1:2 ***(dē Sermōne vītæ*** (capital as your John 1:1; NRSV and
  1573 lower case) and 5:7 *Sermō* (capital, beside *Pater* and *Spīritus Sānctus*); the Spirit at 1 Pet 1:2, 1:22
  (*per Spīritum*, TR only), 3:18 (*carne necātus, Spīritū in vītam revocātus*, as your 1 Tim 3:16), 4:14; 1 John 5:8;
  Jude 19 (*Spīritum nōn habentēs*). Lower case: *antichrīstus* (1 John 2:18, 2:22, 4:3; 2 John 7; 1573 capital),
  *diabolus*, Jude 20 *sacrō afflātū* (as your *dīvīnō afflātū*), 1 Pet 3:6 *dominum* (Sarah's word for Abraham), 4:19
  *conditōrī*, 2:25 *pāstōrem … cūrātōrem*.
- **Punctuation from 1573's page**: 1 Pet 2:24 *vīvāmus:*; 2 Pet 1:1 *sunt,* (the sentence runs into 1:2 *grātiam …
  dīcit*); 1 John 5:9 *admittimus,* (the draft's full stop left the *sī*-clause with no main clause).
- **Words no source marks**, decided from the Latin: 1 Pet *inviētam*, *præsignificāns*, *rependentēs*; 2 Pet
  *cæcutiēns*, *sciolās*, *tartareārum*, *inēscantēs*; Jude *cōnfīderant*, *meretrīcātæ*, *Caīniānā*, *Balaamicī*,
  *Corānāque* (adjectives of names, capital as 1573 and your *Mōsaicam*; **uncertain** stems). *regenuit* left
  unmarked.
- **Names**: new to the edition *Bīthȳnia*, *Cappadocia*, *Galatia* (ablatives), *Silvānus* (by the approved rule),
  *Babylōn*, *Balaamus* (only the ending marked until Numbers is settled), *Bosor* (unmarked), *Diotrephēs* (Gaffiot),
  *Dēmētrius*, *Michāēl* (the lexicon's). As settled: *Sara*, *Abrāhāmus*, *Nōa*/*Nōæ*/*Nōā*, *Lōtus*, *Sodoma*,
  *Gomorra*, *Mārcus*, *Gāius*, *Henōchus*, *Ādamus*, *Mōsēs*, *Caīnus*.

## Questions for you

- **Title lines** (to add when settled), as 1573 heads them (*I. PETRI EPISTOLA*, *II. PETRI EPISTOLA*, *IOHAN
  APOSTOLI EPISTOLA PRIMA / SECVNDA / TERTIA*, *IVDAE APOSTOLI EPISTOLA*): `\mt1` *Petrī Apostolī Epistola prior* /
  *posterior* (as your *Epistola prior / posterior ad Corinthiōs*), *Jōhannis Apostolī Epistola prīma / secunda /
  tertia*, *Jūdæ Apostolī Epistola*; `\h`/`\toc2` *Petrī I*, *Petrī II*, *Jōhannis I–III*, *Jūdæ*.
- **1 John 5:7–8**: the parentheses restored as the only trace of Castellio's margin note. Enough, or a footnote with
  the note (*these words are not in some copies*)?
- **Jude 6 *Deī*** and **1 John 4:4 *nōbīs***: kept with 1573 and 1556 against the Greek, or treated as slips?
- **1 Pet 2:22–24**: prose (as now) or quoted as Isa 53, as the BSB does? **Jude 9 and 15**: `\qt` or not?
- **1 John 1:2 *Sermōne*** capital, and *antichrīstus* lower case (1573 capital)?
- **Your settled text**: nothing found wrong in this run.
