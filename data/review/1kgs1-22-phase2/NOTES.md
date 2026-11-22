# 1 Kings: brief for the two notes readers (phase 2)

*2026-11-22.* Reader A takes chapters 1–11, reader B 12–22 (the KJV's numbering, which the draft and preview use;
1738's chapter breaks sit at 3:1, 13:1 and 15:1 differently, `BRIEF.md`). Each writes two files here, exactly as
2 Samuel's readers did:

- `notes-a.md` / `notes-b.md`: the light notes proposed, in the form of `../2sam1-24-phase2/notes-a.md` (read it first,
  whole: its header, *Sources read*, sections A, B, C … F, each item's evidence, **Why it passes the bar**, the proposed
  note's Latin, its **Apply** line, and the items recommended left out). Leave every **Decision:** line blank.
- `notes-1554-a.md` / `notes-1554-b.md`: Castellio's 1554 annotations on your chapters and the 1554 text's margins, read
  on the page images, in the form of `../2sam1-24-phase2/notes-1554-a.md` (where they are, canvases, crops, the
  annotations sorted (a)–(d), the asterisk table).

**Process and bar:** `../ot-notes-process.md` (decisions 1A–4A) and the bar as it stands (Nathan, 2026-11-19: no note
for a departure without plot or theological significance, a name, place or number included; `../num-notes.md` §F: a
construal the context sets right is left out). Look at how 1–2 Samuel's notes were decided (`../1sam-notes-*.md`,
`../2sam-notes.md` or the `notes-*.md` here, whichever holds the Decisions) to see what Nathan accepted.

**Inputs:**
- `../1kgs-notes-candidates.md` (`python -m pipeline notes 1Kgs`): your chapters' entries.
- The preview `text/draft/1KI.preview.usfm` (the edition's text as it now stands; the draft fixes are in
  `../1kgs1-22-draft-fixes.md`, which already removed Castellio's marks from the text, keeping the words), the printed
  text `text/orig/1KI.usfm`, the read lines `data/witnesses/read-1738/1Kgs1-22.tsv` (1738's footnotes are its `%` rows),
  and `../1kgs1-22-transcription.md` (§ Footnotes and Castellio's marks; § Wording doubts).
- Parallel texts in `sources/parallel/` (WLC, BSB, KJV, Vulgate, LXX), and the NRSVue's footnotes on Bible Gateway (read
  them, don't store them).
- The verse readers' reports `r1.md`–`r9.md` here, and the names reader's `names.md` (use its forms in note text).
- 1554 (MDZ bsb10196330): the text of 1 Kings follows 2 Samuel (which ends a little after canvas 177); the annotations
  *IN III. LIB. REGVM* (or as headed) follow 2 Samuel's on canvas 826 and after. Cached pages are in `sources/mdz-1554/`;
  fetch more with PowerShell `Invoke-WebRequest` (Git Bash curl fails TLS to MDZ). 1573 (bsb10141277) through its
  search API only.

**Known candidates** (check each; propose only what passes):
- The marked passages: 1:8 *L. et Cerethæi et Phelethæi H.*; 2:12 *G. natus annos duodecim, H.*; 2:28 *G. L. Solomonem
  H.* (Hebrew: Absalom); 11:5 *L. et Chamosum Moabitarum H.*; 15:6 *L. Abiamum H.* with 1738's footnote *f) H.
  Roboamum.*; 18:22 *G. L. lucanique vates quadringenti. H.*
- 10:27 *auri* where the Hebrew has silver (1750 the same).
- 1738's 15 footnotes (glosses mostly; 4:13 *Gaulonim vocat Iosephus*) and the asterisks with no footnote (5:9; 6:2,
  6:4, 6:5, 6:23, 6:31; ch. 7; 10:11; 15:13; 19:3; 21:24; 22:30), against the 1554 annotations.

**Rules:** cite only evidence you saw (a page, a file, a tool's output; say when a tool returns nothing). Never copy
Gaffiot's text; macrons in proposed Latin checked with `python -m pipeline latin macron-check`. Don't edit any file but
your own two. Report at the end in a few lines: notes proposed (verse, kind), left out near the bar, and anything the
edition summary must ask Nathan.
