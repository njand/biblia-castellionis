# Joshua as printed in 1738: approved for now

Approved 2026-11-19 (Nathan: "Approve it for now", to approving the printed text as Deuteronomy's was), decision 58's
layer: `text/orig/JOS.usfm`, never rewritten by code after this, like `text/`. Built by `python -m pipeline orig Josh
1-24 --read-lines` (`orig.from_read_lines`) from the lines read on 1738's pages, on the settled versification
(`data/versification/Josh1-24.draft.edits.tsv`); rebuilt 2026-11-19 and identical to the draft reviewed with Joshua.
`data/orig/Josh.pages.tsv` gives each verse's leaf.

**What has been read on the page.** Every word and mark: stage 2 read every printed line of leaves 267–292 on the
page images (2,431 lines; `data/review/josh1-24-stage2.md`, the readers' notes beside it), checked word by word against
Wikisource and 1750, every doubtful place seen on the page; the words follow the page (s for ſ, æ/œ, u/v and i/j as
printed). So no word was taken from the OCR unread, and Joshua, like Numbers and Deuteronomy, needs no
`data/decisions/Josh.orig.tsv`.

**Checked against the settled text**: the same 656 verses (4:15–17 one verse numbered 15-17), none empty; the word
counts agree in every verse but five, each explained: 1:15 *seruoMose*, *cisIordanem* and 21:2 *inChananæa* (1738's
words run together, parted in the edited text), 22:16 and 22:17 *respublica* (the edited text's *rēs pūblica*), and
16:10's *G.* and *H.* (Castellio's marks around the Septuagint's addition, kept here; the edited text's notes pass
decides them).

**Kept as printed** (decision 58), each corrected only in the edited text (`josh1-24-stage2.md`): the misprints 7:21
*auimaduertisset*, 8:10 *antem*, 13:25 *eorumqne*, 15:31 *Scsenna*, 18:1 *terrra*, 18:20 *circumseripta*, 22:3
*mandadatum*, 22:5 *toque* (for *totoque*), 12:22 *Iachananæ* (1554 and 1573 *Iachanamæ*), 15:34 *Taphna* (a turned u, in 1554 and
1573 too); 1738's readings against 1573: 7:12–13 *sacrilegium* (the edited text has 1573's *sacrilegum*), 4:14
*timuerant* (kept in both texts); the names 1738 spells otherwise than the settled books or than Joshua elsewhere
(*Setimo*, *Bosor*, *Sesaim*, *Tholmaim*, *Bethphogor*, *Esriele*, *Salphadus*, *Melcha*, *Lusæ*, *Iaser*, *Chalebo*,
*Thenaci*, *Tanacenses*, *Thannathseræ* …; the 47 of `josh1-24-stage2.md` §"Names" and items 62–65); *adlocutus* and the
other unassimilated or assimilated *ad-* forms as printed; *septemtrio*, *sumsimus*; *submœnia* (2:15), *quessitis*
(24:32). The book's first word *POSTQVAM* in capitals (the print's convention for a book's opening, as Numbers' *ANNO*,
Deuteronomy's *ORATIO*; `orig.opening_word`); a chapter's drop-capital word as a normal capitalized word (decisions
75–76). 1738's footnotes (7:1, 22:34) are not part of it.

**Not yet checked on the page, for your in-depth review**: the paragraphs (1738's indents as the read lines carry
them, the one false break inside *Israeli-|tarum* at 18:1 taken out by `orig.paragraph_starts`; not compared break by
break with the page as Genesis and Exodus 1–30 were); accents (none: 1738 prints none).

**Decision:** accept for now (Nathan, 2026-11-19: "Approve it for now")
