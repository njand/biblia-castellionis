# Exodus 21–23 built from 1738 itself: a check of the route for books with no Wikisource text

Made 2026-11-14 (decision 68; `data/review/exod31-40-plan.md`, step 5, on chapters 21–23 only, as Nathan chose).
The same chapters, built two ways, compared word by word:

- **The Wikisource route**: Wikisource's text corrected against 1738 where the collation and readers found
  differences (stage 2, `data/review/exod21-30-stage2.md`); the answer key here is that stage-2 draft as it stood
  before it was settled (unmacronized).
- **The 1738 route** (`pipeline/ocrdraft.py`): 1738's own OCR (hOCR, leaves 134–138), running heads, chapter
  summaries, catchwords and margin numbers taken off, each word repaired and voted with 1750 and 1726
  (`data/witnesses/read-1738/Exod21-23.voted.tsv`); then **every line read on the page image**, each line's crop
  under its text (`ocrdraft.reading_sheets`, 22 sheets), corrected in `Exod21-23.tsv` (183 lines changed; every
  change in `Exod21-23.corrections.tsv`), the verse starts set where Castellio's margin numbers stand.

Compared on the words alone (u/v, i/j, æ/ae and case folded; punctuation aside).

## The numbers

| | words the same as the key (1,442) | verse starts found / agreeing |
|---|---:|---:|
| 1738's OCR voted with 1750 and 1726 | 1,294 (89.7%) | 75 of 100 found, by margin numbers (1738's and 1750's), most then misplaced by a missing number before them |
| after reading every line on the page | **1,429 (99.1%)** | **100 of 100**, all agreeing |

The reading changed 136 of the 1,442 words and placed every verse.

## The 13 differences left, each looked at on the page

**1738's spelling against Wikisource's (11)**: the words are the same; Wikisource writes them otherwise, and the
approved rules or stages 3–5 would settle the spelling as for any chapter: 21:2 *ebræum* (Wikisource *hebraeum*),
21:6 *adplicato* (*applicato*), 21:8 *adfecit* (*affecit*), 21:22 *multa* (*mulcta*), 22:9 *caussa* (*causa*),
22:28 *exsecrator* (*execrator*), 23:15 *adparento* (*apparento*), 23:22 *exsecutus* (*executus*), 23:29
*exsistant* (*existant*), 23:30 *paullatim* (*paulatim*), *fetifices* (*foetifices*). Each is 1738's form on the
page (leaves 135–138).

**Readings (2): both are slips in the Wikisource text that stage 2 did not catch, and are now in the settled
text:**
- **21:6** *aurem* ***subula*** *perforato*, "pierce the ear with an awl" (KJV "an aul"): 1738 *ſubula* (leaf 135,
  read on the page), 1573 *ſubula* (MDZ bsb10141277, image 72, seen), 1750 OCR *fübula* (= *ſubula*); Wikisource
  *fibula* "pin", and the 1726 OCR *fibula*. The settled Exod 21:6 reads *fībulā*.
- **22:9** *quæ* ***cuia*** *dicatur*, "which is said to be whose" (*cuius, -a, -um*): 1738 *cuia* (leaf 136, read
  on the page), 1573 *cuia* (image 72, seen), 1750 OCR *cuia*; Wikisource *cujus*. The settled Exod 22:9 reads
  *cujus*.

These two want proposals against the settled text (not made here: this check does not touch `text/`).

## Misses of the page reading

Two words the reading passed over were found by this comparison and corrected: 21:3 *tor* (OCR *tot*, at a
line's start) and 23:22 *iussero* (OCR *iusfero*). So the page reading missed **2 of 1,442 words (about 1 in
700)**, the same count as the Wikisource route's stage 2 missed here (21:6, 22:9) the other way. For books with no
Wikisource text, that is the expected rate after one reading: perhaps 5–10 words in a book the size of Exodus
31–40, worth a second reading of the lines where the OCR was weakest.

## Verdict

**The route is sound**: after one reading of every line, the 1738 route agrees with the Wikisource route on every
word but 1738's own spellings and two slips of Wikisource's, and on every verse start. Exodus 31–40 is built this
way (`data/review/exod31-40-stage2.md`).

What the code does not do yet, done by hand in the reading: a catchword *CAPVT* at a page's foot and the footnotes
under the columns (*h) scilicet …*) were read into the text twice and marked `%` (left out); both are now caught
by `ocrdraft.classify`. Footnote letters in the text (ʰ, ⁱ, *) are left out, as decision 50 leaves out the notes.
