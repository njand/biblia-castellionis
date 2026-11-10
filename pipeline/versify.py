"""Renumbering a USFM book to the KJV versification: only verse and chapter markers move, never a word.

The edits are listed in data/versification/<osis>.edits.tsv (`op  at  anchor  status  note`), one per moved
boundary, with `at` the verse id in the book's current numbering:

  split    a new verse starts inside `at`, at the words `anchor` (a verse number the anchor starts with, left
           in the text by the LaTeX conversion, is dropped)
  merge    the verse marker of `at` is removed: its text joins the verse before
  chapter  the chapter break before `at` moves to the words `anchor` inside it; the words before the anchor end
           the previous chapter as its last verse (\\p follows the new \\c after a full stop, \\nb mid-sentence)
  opens    the chapter break after `at` moves back to before it: `at` and the verses after it in its chapter
           open the next chapter (Castellio's Exod 5:25 is the KJV's 6:1); `anchor` is empty. With an `anchor`
           (`at` the chapter's last verse), the break moves back to those words inside it: they open the next
           chapter as its verse 1 (Castellio's 1 Cor 10:33 ends with the KJV's 11:1, *Imitatores mei estote*)
  absent   `at` is a KJV verse the text has no verse for (its sense folded into a neighbour, as Castellio's Gen
           41:56 holds the KJV's 41:57): nothing moves, and the chapter is checked against the KJV's count less one

All later verses of the chapter are renumbered in order. `apply` refuses unless every edit is `approved`, and
checks that the words are unchanged and that every chapter has the KJV's number of verses."""

import re

from pipeline import parallel, paths, tsv

EDITS = paths.DATA / "versification"
MARKER = re.compile(r"(\\c \d+|\\v \d+ ?)")


def edits_path(osis, draft=False):
    """data/versification/<osis>.edits.tsv, or <osis>.draft.edits.tsv for the drafted chapters (text/draft/)."""
    return EDITS / f"{osis}{'.draft' if draft else ''}.edits.tsv"


def load_edits(osis, draft=False):
    path = edits_path(osis, draft)
    return tsv.read(path) if path.exists() else []


def items(usfm, osis):
    """[(kind, value)]: ("c", chapter), ("v", old verse id), ("text", …), in order."""
    out, chapter = [], 0
    for piece in MARKER.split(usfm):
        if piece.startswith("\\c "):
            chapter = int(piece.split()[1])
            out.append(("c", chapter))
        elif piece.startswith("\\v "):
            out.append(("v", f"{osis}.{chapter}.{int(piece.split()[1])}"))
        elif piece:
            out.append(("text", piece))
    return out


def _find(seq, kind, value):
    for index, item in enumerate(seq):
        if item == (kind, value):
            return index
    raise ValueError(f"no {kind} {value} in the book")


def _split_at(seq, start, anchor, where):
    """Index of the text item after `start` holding `anchor`, and the offset of the anchor in it."""
    for index in range(start + 1, len(seq)):
        kind, value = seq[index]
        if kind in ("v", "c"):
            break
        if kind == "text" and value.count(anchor) == 1:
            return index, value.index(anchor)
    raise ValueError(f"{where}: anchor {anchor!r} not found exactly once in the verse")


def apply_edits(usfm, osis, edits):
    """The renumbered USFM, and [(old id, new id, how)] for every verse whose number or extent changes."""
    seq = items(usfm, osis)
    for edit in edits:
        op, at, anchor = edit["op"], edit["at"], edit["anchor"]
        if op == "absent":
            continue
        v = _find(seq, "v", at)
        if op == "merge":
            seq[v] = ("merged", at)
        elif op == "split":
            t, offset = _split_at(seq, v, anchor, at)
            text = seq[t][1]
            rest = re.sub(r"^\d+\.?\s*", "", text[offset:])   # a verse number left in the text (draft: 8‘Hic, 8. Tum)
            seq[t:t + 1] = [("text", text[:offset].rstrip() + "\n"), ("v", f"{at}+split"), ("text", rest)]
        elif op == "chapter":
            c = max(i for i in range(v) if seq[i][0] == "c")
            chapter = seq[c][1]
            seq[c] = ("text", "")
            if c and seq[c - 1][0] == "text":                       # drop the blank line that stood before \c
                seq[c - 1] = ("text", seq[c - 1][1].rstrip("\n") + "\n")
            t, offset = _split_at(seq, v, anchor, at)
            text = seq[t][1]
            before = text[:offset].rstrip()
            paragraph = "\\p" if before.endswith((".", "?", "!", "”", "’")) else "\\nb"
            seq[t:t + 1] = [("text", before + "\n\n"), ("c", chapter), ("text", f"\n{paragraph}\n"),
                            ("v", f"{at}+chapter"), ("text", text[offset:])]
        elif op == "opens" and anchor:
            n = next(i for i in range(v + 1, len(seq)) if seq[i][0] == "c")
            chapter = seq[n][1]
            del seq[n]
            if seq[n - 1][0] == "text":                             # the blank line that stood before \c
                seq[n - 1] = ("text", seq[n - 1][1].rstrip("\n") + "\n")
            t, offset = _split_at(seq, v, anchor, at)
            text = seq[t][1]
            before = text[:offset].rstrip()
            paragraph = "\\p" if before.endswith((".", "?", "!", "”", "’")) else "\\nb"
            seq[t:t + 1] = [("text", before + "\n\n"), ("c", chapter), ("text", f"\n{paragraph}\n"),
                            ("v", f"{at}+opens"), ("text", text[offset:])]
            if t + 5 < len(seq) and seq[t + 5][0] == "text":       # the next chapter's own \p stays, mid-chapter now
                seq[t + 5] = ("text", seq[t + 5][1].lstrip("\n"))
        elif op == "opens":
            n = next(i for i in range(v + 1, len(seq)) if seq[i][0] == "c")
            chapter = seq[n][1]
            del seq[n]
            before = seq[v - 1][1] if v and seq[v - 1][0] == "text" else None
            if before is not None:                                  # a \p that opened `at` now follows the \c
                seq[v - 1] = ("text", re.sub(r"\\p\n$", "", before).rstrip("\n") + "\n\n")
            seq[v:v] = [("c", chapter), ("text", "\n\\p\n")]
        else:
            raise ValueError(f"unknown edit {op!r}")
    out, changes, chapter, verse, last_new = [], [], 0, 0, None
    for kind, value in seq:
        if kind == "c":
            chapter, verse = value, 0
            out.append(f"\\c {chapter}")
        elif kind == "v":
            verse += 1
            new = f"{osis}.{chapter}.{verse}"
            old = value.split("+")[0]
            how = "split" if value.endswith("+split") else "chapter" if value.endswith(("+chapter", "+opens")) else ""
            if how:
                changes.append((f"{old} (part)", new, how))
            elif old != new:
                changes.append((old, new, "renumbered"))
            last_new = new
            out.append(f"\\v {verse} ")
        elif kind == "merged":
            changes.append((value, last_new, "merged"))
        else:
            out.append(value)
    return re.sub(r"\n{3,}", "\n\n", "".join(out)), changes


def words(usfm):
    return re.findall(r"[^\W\d_]+", re.sub(r"\\[a-z]+\d*\*?", " ", usfm))


def verse_counts(usfm, osis):
    counts, chapter = {}, 0
    for kind, value in items(usfm, osis):
        if kind == "c":
            chapter = value
        elif kind == "v":
            counts[chapter] = counts.get(chapter, 0) + 1
    return counts


def report(usfm, osis, edits, gold_rows, kjv_rows):
    """The review text: each edit with your Latin (‖ where the new boundary falls) and the KJV verses it serves."""
    after, changes = apply_edits(usfm, osis, edits)
    chapter_moves = {edit["at"] for edit in edits if edit["op"] == "chapter"}
    renumbered = [(old, new) for old, new, how in changes if how == "renumbered" and old not in chapter_moves]
    lines = [f"# {osis}: renumbering to the KJV", "",
             f"{len(edits)} moved boundaries; {len(renumbered)} more verses only change number. Only markers move: "
             "the words before and after are checked identical, and every chapter ends with the KJV's verse "
             f"count. Edits: `data/versification/{osis}.edits.tsv` (set `status` to `approved`); preview: "
             f"`python -m pipeline versify {osis}`.", ""]
    for number, edit in enumerate(edits, 1):
        op, at, anchor = edit["op"], edit["at"], edit["anchor"]
        text = gold_rows[at]["text"]
        shown = text.replace(anchor, "‖ " + anchor, 1) if anchor else text
        new_ids = sorted({new for old, new, how in changes if old == at or old.startswith(at + " ")},
                         key=lambda vid: tuple(int(x) for x in vid.split(".")[1:]))
        label = {"split": "split", "merge": "merge into the verse before", "chapter": "chapter break moves",
                 "opens": "opens the next chapter", "absent": "absent"}[op]
        lines += [f"## {number}. {at}: {label}", "", f"> {shown}", ""]
        if op == "merge":
            lines.append(f"Joins {new_ids[0] if new_ids else '?'}.")
        for vid in _kjv_ids(at, op, changes):
            if vid in kjv_rows:
                lines.append(f"- KJV {vid.split('.', 1)[1].replace('.', ':')}: {kjv_rows[vid]}")
        lines += ["", f"*{edit['note']}*", ""]
    lines += ["## Verses that only change number", "", _ranges(renumbered), "",
              "**Decision:** approve all eleven, or name the ones to change. Two need a choice:", "",
              "- **6:22 and 7:24 open the next chapter mid-sentence** in your text (*Hæc omnia Deī mandāta cum "
              "fēcisset Nōa, ‖ Jōva eum ita est allocūtus*). Following the KJV puts the chapter break inside the "
              "sentence (USFM `\\nb`: no new paragraph). Accept that, or keep the break where it is and leave "
              "KJV 6:22 and 7:24 as the opening clause of 7:1 and 8:1 (two chapters then keep one verse fewer)?",
              "- **Caīnān (11:14–15)** is in the Septuagint and Luke 3:36, not the KJV. Join both verses to 11:13 "
              "as proposed, or another arrangement?", ""]
    return "\n".join(lines)


def _kjv_ids(at, op, changes):
    """The KJV verses an edit concerns: the verse itself and the new verse it creates or joins."""
    osis, chapter, verse = tsv.parse_id(at)
    if op == "split":
        return [at, f"{osis}.{chapter}.{verse + 1}"]
    if op == "merge":
        return [next(new for old, new, how in changes if old == at)]
    if op == "opens":
        return [f"{osis}.{chapter + 1}.1"]
    if op == "absent":
        return [at]
    last = parallel.kjv_counts()[(osis, chapter - 1)]          # chapter: the previous chapter's new last verse
    return [f"{osis}.{chapter - 1}.{last}", at]


def _ranges(pairs):
    """'Gen.4.18–25 → 4.19–26; …' for runs of verses shifted by the same amount."""
    runs = []
    for old, new in pairs:
        o, n = tsv.parse_id(old), tsv.parse_id(new)
        if runs and runs[-1][1] == (o[0], o[1], o[2] - 1) and runs[-1][3] == (n[0], n[1], n[2] - 1):
            runs[-1][1], runs[-1][3] = o, n
        else:
            runs.append([o, o, n, n])
    return "; ".join(f"{a[1]}:{a[2]}–{b[2]} → {c[1]}:{c[2]}–{d[2]}" if a != b else f"{a[1]}:{a[2]} → {c[1]}:{c[2]}"
                     for a, b, c, d in runs)


def check(before, after, osis, edits=()):
    """Problems with a renumbering: words changed, or a chapter whose verse count is not the KJV's (less the KJV
    verses an `absent` edit records)."""
    problems = []
    if words(before) != words(after):
        problems.append("the words changed")
    kjv = dict(parallel.kjv_counts())
    for edit in edits:
        if edit["op"] == "absent":
            kjv[(osis, int(edit["at"].split(".")[1]))] -= 1
    for chapter, count in verse_counts(after, osis).items():
        if count != kjv.get((osis, chapter)):
            problems.append(f"{osis} {chapter}: {count} verses, KJV {kjv.get((osis, chapter))}")
    return problems
