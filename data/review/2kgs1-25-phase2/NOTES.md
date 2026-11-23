# 2 Kings: brief for the two notes readers (phase 2)

*2026-11-23.* Reader A takes chapters 1–12, reader B 13–25 (the KJV's numbering, which the draft and preview use;
1738's chapter breaks sit at 12:1, 16:1, 21:1, 22:1, 23:1 and 25:1 differently, `BRIEF.md`). Each writes two files
here, exactly as 1 Kings' readers did:

- `notes-a.md` / `notes-b.md`: the light notes proposed, in the form of `../1kgs1-22-phase2/notes-a.md` (read it first,
  whole: its header, *Sources read*, its sections, each item's evidence, **Why it passes the bar**, the proposed
  note's Latin, its **Apply** line, and the items recommended left out). Leave every **Decision:** line blank.
- `notes-1554-a.md` / `notes-1554-b.md`: Castellio's 1554 annotations on your chapters and the 1554 text's margins, read
  on the page images, in the form of `../1kgs1-22-phase2/notes-1554-a.md` (where they are, canvases, crops, the
  annotations sorted, the asterisk table).

**Process and bar:** `../ot-notes-process.md` (decisions 1A–4A) and the bar as it stands (Nathan, 2026-11-19: no note
for a departure without plot or theological significance, a name, place or number included; `../num-notes.md` §F: a
construal the context sets right is left out; 2026-11-21: a note where the book would contradict itself and the Hebrew
does not). See what Nathan accepted for 1 Kings (`../1kgs1-22-edition.md` point 2 and its Decision: three notes, and
what was left out).

**Inputs:**
- `../2kgs-notes-candidates.md` (`python -m pipeline notes 2Kgs`): your chapters' entries (32 numerals against the
  Hebrew, 15 BSB version notes, Castellio's one mark).
- The preview `text/draft/2KI.preview.usfm`, the draft fixes `../2kgs1-25-draft-fixes.md`, the printed text
  `text/orig/2KI.usfm`, the read lines `data/witnesses/read-1738/2Kgs1-25.tsv` (1738's footnotes are its `%` rows), and
  `../2kgs1-25-transcription.md` (§ Footnotes and Castellio's marks; § Wording doubts).
- Parallel texts in `sources/parallel/` (WLC, BSB, KJV, Vulgate, LXX), and the NRSVue's footnotes on Bible Gateway (read
  them, don't store them).
- The verse readers' reports `r1.md`–`r9.md` here, and the names reader's `names.md` if written (use its forms).
- 1554 (MDZ bsb10196330): the text of 2 Kings follows 1 Kings (whose 15:4–6 is on canvas 198); the annotations on
  2 Kings (headed *IN IIII. LIB. REGVM* or as headed) follow 1 Kings' (22:30 on canvas 833). Cached pages are in
  `sources/mdz-1554/`; fetch more with PowerShell `Invoke-WebRequest` (Git Bash curl fails TLS to MDZ). 1573
  (bsb10141277) through its search API only. `docs/editions.md` § "1 Kings in 1554 and 1573" says what was found.

**Known candidates** (check each; propose only what passes):
- 5:26 *G. L. ut emas H.* (dropped from the draft, its words kept).
- 9:16 *decubabat* (1738 and 1750; no lexicon knows it): what does 1554 print?
- 19:13 *rex urbis Sepharvaimi* (1750 *civitatis*), 24:15–16 *fabrisque … omnibus denique* (1750 *fabris …
  omnibusque*): 1554's reading, for the record (the edition keeps 1738 unless 1554 shows a slip).
- The 32 numerals and 15 version notes of the candidates.
- 1738's 10 footnotes (glosses) and its asterisks with no footnote (1738's numbering: 3:7, 4:37, 6:25, 6:33, 20:13),
  against the 1554 annotations.

**Rules:** cite only evidence you saw (a page, a file, a tool's output; say when a tool returns nothing). Never copy
Gaffiot's text; macrons in proposed Latin checked with `python -m pipeline latin macron-check`. Don't edit any file but
your own two, except that facts about the 1554 and 1573 editions go into `docs/editions.md` (a section "2 Kings in
1554 and 1573", evidence cited, the unverified marked). Report at the end in a few lines: notes proposed (verse, kind),
left out near the bar, and anything the edition summary must ask Nathan.
