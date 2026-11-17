# 1 John: light notes and brackets

Built 2026-11-17 by the process in `nt-notes-process.md`, with the test and wording of `nt-notes-form.md`: "the modern
editions" means SBLGNT and NA28, against the TR.

**Sources read:** `1john-notes-candidates.md` (`python -m pipeline notes 1John`); the letter, read verse by verse
against the TR, SBLGNT, BSB, WEB, the Vulgate and 1573 as printed, with every line of the SBLGNT apparatus (one reader for 1–3 John and Jude);
the NRSVue (Bible Gateway, read 2026-11-17) for every verse below: it reads with the modern text against Castellio,
and none of its footnotes gives his sense as an alternative, except where an item says so. No word of the edited
text differs from 1573 in more than spelling.

## A. Notes where the Greek text differs (the modern editions against the TR)

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

1. **2:23** *nē Patrem quidem habet*: the modern editions add ὁ ὁμολογῶν τὸν υἱὸν καὶ τὸν πατέρα ἔχει (NRSVue "everyone who confesses the Son has the Father also"); the TR and 1573 lack it.
   **Apply:** `1John.2.23` la: `nē Patrem quidem habet.` → `nē Patrem quidem habet\f + \fr 2:23 \ft Cōdicēs antīquiōrēs addunt ὁ ὁμολογῶν τὸν υἱὸν καὶ τὸν πατέρα ἔχει, ‘quī Fīlium cōnfitētur, et Patrem habet’.\f*.`
2. **3:1** *ut Deī fīliī vocēmur*: the modern editions add καὶ ἐσμέν (NRSVue "and that is what we are").
   **Apply:** `1John.3.1` la: `ut Deī fīliī vocēmur.` → `ut Deī fīliī vocēmur\f + \fr 3:1 \ft Cōdicēs antīquiōrēs addunt καὶ ἐσμέν, ‘et sumus’.\f*.`
3. **2:20** *nōvistis omnia*: TR οἴδατε πάντα; the modern editions οἴδατε πάντες (NRSVue "all of you have knowledge", footnote "you know all things").
   **Apply:** `1John.2.20` la: `nōvistis omnia.` → `nōvistis omnia\f + \fr 2:20 \ft Cōdicēs antīquiōrēs habent οἴδατε πάντες, ‘nōstis omnēs’.\f*.`

## C. Brackets: words the modern editions leave out

**Decision:** accept (Nathan, 2026-11-17: "Apply them")

4. **4:3** *Chrīstum corporātum vēnisse*: TR Χριστὸν ἐν σαρκὶ ἐληλυθότα (NRSVue "every spirit that does not confess Jesus").
   **Apply:** `1John.4.3` la: `spīritus Jēsum Chrīstum corporātum vēnisse nōn cōnfitētur` → `spīritus Jēsum [Chrīstum corporātum vēnisse] nōn cōnfitētur`
5. **5:13** *utque in nōmen Fīliī Deī crēdātis*: TR καὶ ἵνα πιστεύητε εἰς τὸ ὄνομα τοῦ υἱοῦ τοῦ Θεοῦ (NRSVue footnote "Other ancient authorities add *and that you may believe in the name of the Son of God*"). The modern text's "you who believe in the name" Castellio already has.
   **Apply:** `1John.5.13` la: `vītam sciātis, utque in nōmen Fīliī Deī crēdātis.` → `vītam sciātis[, utque in nōmen Fīliī Deī crēdātis].`
6. **3:14** *frātrem*: TR τὸν ἀδελφόν (NRSVue "Whoever does not love abides in death").
   **Apply:** `1John.3.14` la: `Quī frātrem nōn amat` → `Quī [frātrem] nōn amat`
7. **4:19** *eum*: TR αὐτόν (NRSVue "We love because he first loved us", footnote "add *him* or *God*").
   **Apply:** `1John.4.19` la: `Nōs eum amāmus` → `Nōs [eum] amāmus`
8. **1:7** *Chrīstī*: TR Ἰησοῦ Χριστοῦ (NRSVue "the blood of Jesus his Son").
   **Apply:** `1John.1.7` la: `Jēsū Chrīstī sanguis` → `Jēsū [Chrīstī] sanguis`
9. **5:21** *Āmēn*: TR ἀμήν (NRSVue footnote "Other ancient authorities add *Amen*").
   **Apply:** `1John.5.21` la: `cavēte deastrōs: Āmēn.` → `cavēte deastrōs[: Āmēn].`

## Considered and left out

- 5:7–8: already bracketed (`brackets-and-notes.md` items 40–41, from Castellio's own parentheses in 1573); the NRSVue's footnote gives the same words.
- 5:18 ἑαυτόν: NA28 with the TR.
- 1:4 *lætitiā* (the modern editions "our joy"): a change of person only.
- 2:7 *prīncipiō* (the second): a word that changes nothing a reader needs.
- 2:13, 2:14, 3:12, 5:19 *malum*, which 1573 capitalizes for the Evil One: a matter of capitals, for the house style.
