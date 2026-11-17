# Numbers as printed in 1738: approved for now

Approved 2026-11-17 (Nathan: "Approve the printed text for now"), decision 58's layer: `text/orig/NUM.usfm`, never
rewritten by code after this, like `text/`. Built by `python -m pipeline orig Num 1-36 --read-lines`
(`orig.from_read_lines`) from the lines read on 1738's pages, rebuilt 2026-11-17 on the settled versification and
identical to the draft committed with Numbers (bc3ce3b); the header (*Numerī*) added as the other books have it.

**What has been read on the page.** Every word and mark: stage 2 read all 3,849 printed lines of leaves 187–227 on
the page images, and the 91 lines the OCR had lost (`data/review/num1-36-stage2.md`); the words follow the page (s for
ſ, æ/œ, u/v and i/j as printed). So no word was taken from the OCR unread, unlike Genesis–Leviticus 1–11, which needed
a separate pass (`data/decisions/<osis>.orig.tsv`); Numbers needs no such file.

**Kept as printed** (decision 58), each corrected only in the edited text (`num1-36-stage2.md`): 6:3 *bibtto*, 10:6
*G. L. … H.*, 16:47 *clades ceperat*, 25:1 *in Cittimo*, 28:7 *temetum Ioua*, 30:16 *Atquæ*, 3:30 *Elisaphane*,
the names 1738 prints two ways (*Abidam*/*Abidan* …), 16:11 *coiuistis*. The book's first word *ANNO* in capitals
(the print's convention for a book's opening, as *PRINCIPIO*; `orig.opening_word`).

**Not yet checked on the page, for your in-depth review**: the paragraphs (1738's indents as the read lines carry
them, not compared break by break with the page as Genesis and Exodus 1–30 were); accents (dropped, as in all the OT
printed texts so far).

**Decision:** accept for now (Nathan, 2026-11-17: "Approve the printed text for now")
