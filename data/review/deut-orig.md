# Deuteronomy as printed in 1738: approved for now

Approved 2026-11-18 (Nathan: "Yes, go ahead", to approving it for now as Numbers' was), decision 58's layer:
`text/orig/DEU.usfm`, never rewritten by code after this, like `text/`. Built by `python -m pipeline
orig Deut 1-34 --read-lines` (`orig.from_read_lines`) from the lines read on 1738's pages, on the settled
versification (`data/versification/Deut1-34.draft.edits.tsv`); rebuilt 2026-11-18 and identical to the draft committed
with Deuteronomy (731ac2a) but for the header (*Deuteronomium*, added as the other books have it, 7056330).
`data/orig/Deut.pages.tsv` gives each verse's leaf.

**What has been read on the page.** Every word and mark: stage 2 read all 3,658 printed lines of leaves 227–264 and 267
on the page images, and the one line the OCR had lost (32:43 *cabitur.*; `data/review/deut1-34-stage2.md`); the words
follow the page (s for ſ, æ/œ, u/v and i/j as printed). In stages 3–5 four long s that stage 2 had read as f were seen
again on the page and set right in the read lines: 11:10 *conserebatis*, 28:30 and 28:39 *conseretis*, 33:29
*conseruate*; every other *f*-word was then compared with the settled text and read in context. So no word was taken
from the OCR unread, and Deuteronomy, like Numbers, needs no `data/decisions/Deut.orig.tsv`.

**Checked against the settled text**: the same 958 verses (14:16–17 one verse numbered 16-17), none empty; the word
counts agree in every verse but five, each the edited text's own: 32:30 *fieri ne posset* (joined *fierine* there),
and the approved word divisions *tam diū* (11:21, 15:18), *crucī fīxum* (21:23), *male dīxerit* (27:16), which 1738
prints as one word.

**Kept as printed** (decision 58), each corrected only in the edited text (`deut1-34-stage2.md`): the misprints 4:14
*possessinem*, 8:2 *haberitis*, 9:6 *iustititiam*, 16:11 *collocandc*, 18:18 *cis* (for *eis*), 22:16 *calumnietnr*,
23:7 *abhorrerote*, 23:18 *mrcedem*; 32:30 *fieri ne posset*; Castellio's 23:4 *Phegoris* (Beor); the names 1738
spells otherwise than the settled books (*Emes*, *Iabboqui*, *Cenneretho*, *Pheresæos*, *Iaquanensium*, *Ebræus*,
*Phasge* …); 3:25 *suo veniam*, 27:1 *præcipit*, 29:18 *absynthium*, 25:3 *Quadragesies*, 25:7 *glossem*; *solemnitate*
(31:10). The book's first word *ORATIO* in capitals (the print's convention for a book's opening, as Numbers' *ANNO*;
`orig.opening_word`); a chapter's drop-capital word as a normal capitalized word (decisions 75–76).

**Not yet checked on the page, for your in-depth review**: the paragraphs (1738's indents as the read lines carry
them, not compared break by break with the page as Genesis and Exodus 1–30 were); accents (dropped, as in all the OT
printed texts so far).

**Decision:** accept for now (Nathan, 2026-11-18: "Yes, go ahead")
