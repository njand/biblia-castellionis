# Castellio's text as printed, Judges (1738): proposed for approval

Built 2026-11-19 (`python -m pipeline orig Judg 1-21`). The draft is `text/orig/draft/JDG.usfm`; how each word was made,
word by word, is in `judg1-21-orig.md`. This file is the summary and the Decision line.

**Decision:** approved for now (Nathan, 2026-11-19: "Approve it"); moved to `text/orig/JDG.usfm`, never rewritten by
code. Rebuilt the same day from the settled words (Judges settled that day).

## How it was made

- The words are the edited draft's (`text/draft/JDG.usfm`, KJV numbering) in 1738's spelling and punctuation, read from
  its OCR where it read them (8,300 words), and **on the page for every other word** (decision 68): 2,596 words on 217
  contact sheets (each word's line with the lines around it), by six readers, each word with the mark printed after
  it; and 44 more by me (the OCR's misreadings the builder had accepted: *Israelite* for *Israelitæ* ×14, *ccenaculi*
  for *cœnaculi*, *coloqui*, *repeciuerunt* …; 15:1's first line, lost by the OCR; the four words of 9:12–19 that lie
  wholly in leaf 303's gutter, supplied from the sense). Each is a row in `data/decisions/Judg.orig.tsv`. The review
  file's list of words not read holds only the two chapter openings beside a drop capital (2:1 *Adscendit*, 21:1
  *Iurauerant*), set by `orig.opening_word`.
- **Paragraphs**: 1738's indents, every one checked on the page by a reader (`judg1-21-orig-paragraphs.md`): of the 63
  read from the hOCR, 59 are indents; 4 taken away (two set a word late, 1:22 and 8:13; two lines at the margin, 8:8 and
  13:8) and 25 added (`¶`, `¶-` rows). 9:34 *Igitur*, a column's first line, is uncertain (kept).
- **Names** the reading edition respells (`judg1-21-stage2.md` §6) keep 1738's forms here (decision 58): *Chalebus*,
  *Sesaim*, *Ahimanem*, *Tholmaim*, *Maggedonenses*, *Pheresæos*, *Iaboc*, *Iazam*, *Chamosus*, *Cariathiarimum*,
  *Paciiouium*.

## What the page has (kept as printed, decision 58)

- **Misprints**: 3:13 *Isra-|raelitas*, 9:43 *piuisas* (a battered d), 11:5 *Gala-|ditarum*, 19:9 *deuectus* (1750
  *devexus*), 20:23 *conferere* (1750 the same).
- **Capitals**: lower case after a colon or semicolon where the sentence goes on (*adsciuerunt*, *factisque*, *quæso*,
  *missisque*, *recensitique* …), and in adjectives of peoples (*gazerenses*, *israeliticæ*, *palæstini* 16:23,
  *dania* 18:11, *chananæo* 4:23).
- **Spellings**: *quum*, *adf-/adl-/adp-/ads-* unassimilated, *-mt-* (*sumsit*, *promtu*), *exs-*, *caussa*, *quemdam*,
  *quamdam*, *septemtrione*, *prœlium*, *sexcenti*, *simulacrum*, *sepulcro*, *dictitare*, *hædum*; 6:24 *Paciiouium*
  and 15:14 *simul ac* as printed.
- **Accents** dropped, as in every printed text so far (21:10 *eò*, the readers noted the few they saw).

## Rebuilt from the settled text (2026-11-19)

- The 2,676 rows of `data/decisions/Judg.orig.tsv` were keyed to the draft's unmarked words; each was re-keyed to the
  settled word at the same place in its verse (*Jova#1* → *Jōva#1*, with its occurrence counted again), all found.
  The OCR's written-out *ae* is now tied (*desolatæ*), and 13 more words were read on the page by me: eight where the
  OCR had written out the ligature (1:1, 8:24, 8:33, 10:15, 10:17, 11:40, 19:30, 20:7), and 3:21 *Quumque*, 13:12
  *quum*, 16:16 *quotidianis*, 12:6 *Schib-|bolet :*, 14:1 *QVum* (→ *Quum*).
- Checked: the same 618 verses as `text/JDG.usfm`, the same number of words in every verse; the only word not read is
  21:1 *Iurauerant* beside its drop capital (`orig.opening_word`).
