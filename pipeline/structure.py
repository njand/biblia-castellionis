"""Stage 5 on a USFM text: paragraphs, poetry and quotation marks compared with the BSB (PLAN.md §4, stage 5).

The BSB (sources/parallel/bsb/<osis>.tsv) gives, per verse, the layout markers before it (`marks`: p, m, q1, q2,
b, headings) and the markers inside it (`layout`). The same is read from a USFM text (gold.rows). Compared:

  paragraphs  verses that open a paragraph (\\p) in one and not the other
  poetry      verses set as poetry lines (\\q1/\\q2) in one and not the other
  quotes      per verse, unbalanced “…” or ‘…’, and ‘…’ passages that may be reported speech (decisions 4, 25:
              an infinitive (-re, -isse, -ī) or a subjunctive inside, or a conjunction ut/nē/quod/quid/cūr/an
              opening it): candidates for a reader, not decisions

`calibrate()` measures how often the BSB's paragraph starts agree with your settled chapters."""

import re

from pipeline import books, gold, paths, tsv

POETRY = re.compile(r"\bq\d?\b")


def bsb_rows(osis):
    path = paths.SOURCES / "parallel" / "bsb" / f"{osis}.tsv"
    return {r["id"]: r for r in tsv.read(path)} if path.exists() else {}


def starts(marks):
    """Does a verse open a paragraph? (`marks` as in gold/BSB rows: \\p, or a heading before it.)"""
    parts = marks.split()
    return "p" in parts or any(p.startswith("s1:") for p in parts) and "q1" not in parts


def poetic(row):
    return bool(POETRY.search(row.get("marks", ""))) or "\\q" in row.get("layout", "")


def layout_of(usfm, osis):
    """{verse id: {"marks", "layout", "text"}} of a USFM text."""
    return {vid: {"text": text, "marks": marks, "layout": layout} for vid, text, marks, layout in gold.rows(usfm, osis)}


def compare(rows, osis, chapters=None):
    """{"paragraph": (yours only, BSB only, both), "poetry": (...)} as lists of verse ids."""
    bsb = bsb_rows(osis)
    out = {"paragraph": ([], [], []), "poetry": ([], [], [])}
    for vid, row in rows.items():
        if chapters and tsv.parse_id(vid)[1] not in chapters or tsv.parse_id(vid)[2] == 0 or vid not in bsb:
            continue
        for kind, test in (("paragraph", lambda r: starts(r["marks"])), ("poetry", poetic)):
            mine, theirs = test(row), test(bsb[vid])
            if mine and theirs:
                out[kind][2].append(vid)
            elif mine:
                out[kind][0].append(vid)
            elif theirs:
                out[kind][1].append(vid)
    return out


def calibrate():
    """{osis: (your paragraph starts, BSB's, both)} over the settled books."""
    result = {}
    for book in books.BOOKS:
        rows = gold.load(book.osis)
        if not rows:
            continue
        c = compare(rows, book.osis)["paragraph"]
        result[book.osis] = (len(c[0]) + len(c[2]), len(c[1]) + len(c[2]), len(c[2]))
    return result


REPORTED = re.compile(r"(?:^|[\s(])(ut|nē|quod|quid|cūr|an|sē|sēsē|eum|eam|eōs|esse)\b|\w(?:re|isse|ārī|ērī|īrī)\b")


def quotes(rows):
    """[(verse id, problem, text)]: marks out of balance (a “ inside an open “, a ” or ’ with nothing open, a
    chapter ending inside a quotation; a speech may run over verses), and every ‘…’ passage, flagged where it may
    be reported speech."""
    out, chapter, double, single = [], None, 0, 0
    for vid, row in rows.items():
        c = tsv.parse_id(vid)[1]
        if c != chapter:
            if chapter is not None and (double or single):
                out.append((last, "chapter ends inside a quotation", ""))
            chapter, double, single = c, 0, 0
        # A speech running over paragraphs reopens “ at each new one without closing the last (as in English); a
        # new paragraph that does not reopen it means the last paragraph's speech was never closed.
        if double and starts(row["marks"]) and not row["text"].lstrip().startswith("“"):
            out.append((last, "speech not closed before the next paragraph", rows[last]["text"]))
            double, single = 0, 0
        last = vid
        reopened = double == 1 and starts(row["marks"]) and row["text"].lstrip().startswith("“")
        text, triple = row["text"], 0
        for n, ch in enumerate(text):
            if ch == "“":
                if reopened and n == len(text) - len(text.lstrip()):
                    continue
                if single:
                    triple += 1                              # a quotation inside ‘…’ (Matt 22:44)
                    continue
                if double and text[n + 1:n + 2] == "‘":
                    continue                                 # “‘ reopens a speech where a quoted block begins (Matt 4:6)
                if double:
                    out.append((vid, "“ inside an open “", text))
                    continue                                 # counted once: resynchronized
                double += 1
            elif ch == "”" and triple:
                triple -= 1
            elif ch == "”":
                double -= 1
                if double < 0:
                    out.append((vid, "” with no “ open", row["text"]))
                    double = 0
            elif ch == "‘":
                single += 1
            elif ch == "’" and single:
                single -= 1
        for m in re.finditer(r"‘([^’]*)’", row["text"]):
            flag = "‘…’ may be reported speech" if REPORTED.search(m.group(1)) else "‘…’"
            out.append((vid, flag, m.group(1)))
    if chapter is not None and (double or single):
        out.append((last, "chapter ends inside a quotation", ""))
    return out
