# Castellio's accents in the printed text: what restoring them takes

Measured 2026-11-14, after you decided the printed text keeps Castellio's accents (decision 67). **Waiting for
your choice of route** before anything changes in `text/orig/`.

## What the prints have

- **1738** (the Old Testament base) prints **no accents**. Seen on its leaves 76 and 132: *quod*, *quam*, *e*,
  *vna*, *a* all plain, where 1573 would accent them. The Old Testament printed text is unaffected.
- **1573** (the New Testament base) accents adverbs and particles with a grave (*verò*, *quòd*, *cùm*, *quàm*,
  *à*, *è*, *eò*, *quò*, *vnà*, *rectè*, *malè*, *Latinè*), a few with a circumflex (*hîc*), and leaves the same
  letters plain where they are another word (*quod* the relative, *cum* the preposition, *vna* the adjective:
  *vna caro*, *vna hora*). An acute in the OCR is nearly always the nasal bar (*nó*, *auté*), handled already.

## How well the OCR reads them

The 1573 OCR (`sources/mdz-1573/`, NT canvases 747–960) has **4,040 accented tokens** in 514 word types; 127 types
are read with an accent three times or more, and **7,226 tokens of those types are read plain**.

A random sample of 20 of the plain ones, among adverbs that 1573 usually accents (*vero, adeo, recte, vere,
latine, male, certo, forte, una*), seen on the page images: **10 have the accent in the print** (*verò* ×5,
*Latinè*, *vnà*, *malè*, *fortè*, *certò*), 10 are rightly plain (*vna* the adjective ×6, *certo* the adjective
×2, *VNA* in capitals, *recte* at Titus 3:8). So **where the OCR reads a plain word, half the time the print has an
accent**: its plain readings cannot be trusted, and an accent cannot be put back from the OCR alone.

Of the 7,226, some are OCR noise (*qui* ×2,048, *te* ×350: a stray mark read as an accent a few times); the
real candidates are about **4,500–5,000** tokens: *cum* 910, *quod* 875, *eo* 424, *quo* 332, *quam* 268,
*a* 252, *hic* 184, *contra* 96, *paulo* 77, *e* 68, *ante* 66, *ideo* 58, *vero* 55, *modo* 52, *verum* 45 …

## The routes

1. **Read every candidate on the page** (about 400 contact sheets of 12, like the Old Testament reading). The
   only route that follows the page exactly (decision 58). The OCR's accented readings (4,040) are taken as they
   are: a sample of them should be checked too (an accent is rarely invented, but the noise above shows it can be).
   Then a new draft of all 27 books goes to `text/orig/draft/` with a review file per book, for your approval
   (the approved `text/orig/` is never rewritten by code).
2. **By 1573's own habit, word by word, then a sample**: where the sheets show 1573 always accents a word in one
   use (*verò* the adverb, *à* the preposition), put the accent on every token of that use; read only the words
   whose accent depends on their use (*quod/quòd*, *cum/cùm*, *quam/quàm*, *eo/eò*, *quo/quò*, *ante/antè*,
   *vna/vnà*: about 3,000). Faster, but the uses are decided by grammar, not the page: a printer's slip (an
   accent left off) would be "corrected", against decision 58.
3. **Keep only the accents the OCR read** (4,040): no reading, but about one accent in three would be missing,
   and the text would look as if 1573 were inconsistent where it is not. Not recommended.

**Recommended: route 1.** It is the standard the New Testament's spelling was held to. It is reading time, not
your time, and can run after the Old Testament reading now in progress.

**Decision:** route 1, read every candidate on the page (Nathan, 2026-11-14: "Yes, read them all")
