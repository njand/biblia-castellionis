# Jācōbus and Jācōbeus: macrons out of line with the rest of the text (proposal)

Proposed 2026-11-12 (Claude), from a sweep of every form of *Jacob* in `text/*.usfm`. Nothing is applied until the
Decision lines are filled in. Item 1 is a plain correction. Items 2 and 3 are alternatives for the same question
(accept one or the other, not both).

## 1. Jācōbus in Mark

The settled text writes the name with both vowels long everywhere: *Jācōbus* 83×, *Jācōbī* 46×, *Jācōbum* 35×,
*Jācōbō* 35×, across Genesis, Exodus, the Gospels, Acts, the letters and Hebrews. Gaffiot's headword (via
`python -m pipeline latin macron Jācōbus`) is *Iācōbus, ī*, with the ā long. Mark has the only three forms with the
ā unmarked, in two verses:

1. Mark 3:18 and 5:37: *Jacōbum*, *Jacōbī* → *Jācōbum*, *Jācōbī*.

   **Apply:** `Mark.3.18` la: `et Jacōbum Alphæī fīlium` → `et Jācōbum Alphæī fīlium`
   **Apply:** `Mark.5.37` la: `et Jacōbum, et Jōhannem Jacōbī frātrem` → `et Jācōbum, et Jōhannem Jācōbī frātrem`

(*Jacobedam*, Exod 6:20, is Jochebed, a different name, left unmarked by decision in `data/decisions/Exod.forms.tsv`;
it is not touched.)

**Decision:** accept (Nathan, 2026-11-12)

## 2–3. Jācōbæus, "the Jacobeans": æ like every other people's name, or a short e?

Castellio's name for Israel's people, formed from *Jacob*, stands six times in the settled text, and not
consistently:

| Verse | Settled | Vowel |
|---|---|---|
| Gen 35:5 | *Jācōbēōs* | ē |
| Gen 49:7 | *Jācōbeōs* | e, unmarked (your settled form, as `data/decisions/Gen.forms.tsv` notes at 49:7) |
| Luke 1:33 | *Jācōbeōrum* | e, unmarked |
| Acts 7:46 | *Jācōbeōrum* | e, unmarked |
| Rom 11:26 | *Jācōbæōs* | æ (from Wikisource's *Jacobaeos*) |

No lexicon in the lookup knows the word (*Iacobaeus*, *Iacobeus*: "no source knows this form"), and the Latin Library
corpus has no *Jacobaeorum* or *Jacobaei*. The evidence is the word's kind and how Castellio's printers spelled
words of that kind:

- **It is a people's name, and every people's name in the settled text ends in -æus.** *Jūdæī*, *Hebræī*,
  *Chaldæī*, *Galilæī*, *Nāzaræī*, *Idūmæī*, and the peoples of Canaan: *Chananæī*, *Hettæī*, *Hethæī*, *Amorræī*,
  *Pherezæī*, *Hevæī*, *Jebusæī*. Several are named, like this one, after a man or a place (*Idūmæī* from Edom,
  *Jebusæī* from Jebus). The ending is the Greek -αῖος, always long (Gaffiot *Jūdæus*, *Galīlæus*, *Saddūcæus*).
- **Castellio's printers wrote e for that æ as often as not.** The 1573 hOCR (`sources/mdz-1573/`) has
  *Chanane-* 8× against *Chananæ-* once, *Amorre-* 4×, *Idume-* 2× against *Idumæ-* once, and *Jude-* 194× against
  *Judæ-* 299×. The 1556 OCR (`sources/erara-1556/`) has *Hebre-* 171× against *Hebrae-* 22×. So 1556's and 1573's
  *Iacobeorum* (Luke 1:33, canvas 789; Acts 7:46, canvas 838) and *Iacobeos* (Rom 11:26, canvas 863) are the same
  habit: they are no evidence for a short e. The settled text already turns the printers' e into æ in all the
  names above, under the approved rule `ae → æ`.
- **Later printings read it so.** At Luke 1:33, 1681 *Jacobaeorum*, 1747 *Iacobaeorum* (1726 and 1758 *Jacobeorum*);
  Wikisource *Jacobaeorum* (Isa 2:3, Acts 7:46) and *Jacobaeos* (Rom 11:26). Your 2019 text has *Iacobēōs*, long,
  at Gen 35:5.
- **The case for a short e** rests on Gaffiot's Latin adjectives made from personal names: *Hercŭlĕus*,
  *Ŭlixĕus* ("of Hercules", "of Ulysses"). Castellio's word is not such an adjective but the name of a people, used
  as a noun ("the God of the Jacobeans", "he will reign over the house of the Jacobeans"), which is the slot
  -æus fills.

**Recommendation: item 3, *Jācōbæus*, spelled with æ** as the other peoples' names are. Rom 11:26 already has it;
four places change. (Item 2, the short e, is kept for the record.)

2. Short e throughout: *Jācōbeus*. Two changes.

   **Apply:** `Gen.35.5` la: `ut Jācōbēōs nōn persequerentur` → `ut Jācōbeōs nōn persequerentur`
   **Apply:** `Rom.11.26` la: `ā sceleribus Jācōbæōs vindicet` → `ā sceleribus Jācōbeōs vindicet`

3. *Jācōbæus* throughout, with æ like *Chananæus* and *Jūdæus*. Four changes.

   **Apply:** `Gen.35.5` la: `ut Jācōbēōs nōn persequerentur` → `ut Jācōbæōs nōn persequerentur`
   **Apply:** `Gen.49.7` la: `Eōs inter Jācōbeōs distribuam` → `Eōs inter Jācōbæōs distribuam`
   **Apply:** `Luke.1.33` la: `in Jācōbeōrum domum` → `in Jācōbæōrum domum`
   **Apply:** `Acts.7.46` la: `Deō Jācōbeōrum` → `Deō Jācōbæōrum`

The Old Testament books where Wikisource has the word (Ps 14:7, Isa 2:3, 2:6, Mal 2:12, Nah 2:2) are not yet in
`text/`; whichever item is accepted becomes the rule for drafting them (with item 3, Isa 2:6 *Jacobeam domum*
becomes *Jācōbæam*).

**Decision:** accept 3: Jācōbæus, with æ (Nathan, 2026-11-12)
