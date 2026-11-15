# 1738 read on the page, line by line

Stage 1–2 for chapters Wikisource lacks (decision 68; `pipeline/ocrdraft.py`). Per book and chapters:

- `<osis><chapters>.voted.tsv`: 1738's OCR (`archive.org bibliasacraexseb01cast` hOCR), one row per printed line
  (`leaf column line text`), running heads, chapter summaries, catchwords and margin numbers taken off; each word
  repaired and voted with 1750 and 1726; verse starts as `#N`, chapters as `\c N`. Made by `ocrdraft.make_lines`.
- `<osis><chapters>.tsv`: the same after every line was read on the page image (crops from
  `ocrdraft.reading_sheets`, each line's crop under its text): the words and punctuation as 1738 prints them (s for
  ſ, & and q; expanded, æ and œ as printed, u/v and i/j as printed), a drop capital written with its word (HAec),
  verse starts where Castellio's margin number and the sense put them.
- `<osis><chapters>.corrections.tsv`: every row changed by the reading (`row  voted  read`), the record of stage 2.

Spaces before punctuation are the OCR's and carry no meaning. Rows starting `%` (a catchword or footnote read as a
line) are not the text.

`python -m pipeline draft <book> <chapters> --from-ocr` turns `<osis><chapters>.tsv` into the draft
`text/draft/<USFM>.usfm` in Wikisource's conventions (`ocrdraft.to_usfm`), for `versify --draft` and stages 3–5.
