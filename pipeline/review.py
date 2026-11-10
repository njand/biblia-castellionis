"""Applying accepted proposals: the **Apply:** lines of data/review/*.md.

A review file groups proposals under `##` headings; each proposal is a numbered item (`12. …`) with one or more
lines of the form

  **Apply:** `Matt.14.3` la: `old text` → `new text`

(also `**Apply** (only if …): …`, which is applied only when its decision accepts it). Each replacement is
scoped to its verse in the USFM master (`text/<USFM>.usfm`, or `text/draft/<USFM>.usfm` for a drafted
chapter) and must match exactly once there. Whitespace in `old` matches any whitespace (a line break included),
and in `new` a space before a paragraph or poetry marker (`\\p`, `\\q1`, …) becomes a line break, so layout
changes can be written on one line.

A verse's span starts at the paragraph and poetry markers just before its `\\v` and ends where the next
verse's span starts (verse 0: from after `\\c` to verse 1), so `\\v 13 Eō` → `\\p \\v 13 Eō` adds a paragraph.

Decisions: a `**Decision:**` line at the start of a line is the group's (the `##` section's); an indented one,
inside an item, is that item's and wins. A decision applies the item when it starts with *accept*:
`accept`, `accept all`, `accept 1, 3–5` (only those), `accept all except 4, 7` (all but those). Anything else
(`keep`, `reject`, an empty line) leaves the item out. An item given by number on the command line is applied
whatever its decision says.

Items are applied in file order, each to the text as the earlier ones left it (so files compose), all or
nothing: if any selected replacement fails to match exactly once, nothing is written. A replacement whose
`old` is gone and whose `new` is already there once counts as already applied and is skipped."""

import re
from dataclasses import dataclass, field

from pipeline import books, gold, latex, tsv

APPLY = re.compile(r"\*\*Apply(?::\*\*|\*\*\s*\([^)]*\):)\s*`([^`]+)`\s*(\w+):\s*`(.*?)`\s*→\s*`(.*?)`(?:\s+\(.*\))?\s*$")
DECISION = re.compile(r"^(\s*)(?:\d+\.\s+)?\*\*Decision:\*\*\s*(.*)$")
ITEM = re.compile(r"^(\d+)\.\s")
HEADING = re.compile(r"^#{2,}\s")
LAYOUT = r"\\(?:p|m|b|nb|q\d?|pi\d?|li\d?|cls)\b"      # markers that start a line in the USFM


@dataclass
class Replacement:
    vid: str
    column: str
    old: str
    new: str
    line: int                       # line number in the review file


@dataclass
class Item:
    number: int | None
    group: str
    replacements: list = field(default_factory=list)
    decision: str = ""              # the item's own decision, if any
    group_decision: str = ""

    @property
    def label(self):
        return f"{self.group[:40]} #{self.number}" if self.number is not None else self.group[:40]


def parse(text):
    """[Item] in file order. Apply lines outside a numbered item form an item of their own."""
    items, group, group_decision, current = [], "", "", None
    for n, line in enumerate(text.splitlines(), 1):
        if HEADING.match(line):
            group, group_decision, current = line.lstrip("#").strip(), "", None
            continue
        if m := ITEM.match(line):
            current = Item(int(m.group(1)), group, group_decision=group_decision)
            items.append(current)
        if m := DECISION.match(line):
            indented = bool(m.group(1)) or bool(ITEM.match(line))
            if indented and current is not None:
                current.decision = m.group(2).strip()
            else:
                group_decision = m.group(2).strip()
                current = None
                for item in items:                     # a group decision after its items still covers them
                    if item.group == group and not item.group_decision:
                        item.group_decision = group_decision
            continue
        if m := APPLY.search(line):
            if current is None:
                current = Item(None, group, group_decision=group_decision)
                items.append(current)
            current.replacements.append(Replacement(m.group(1), m.group(2), m.group(3), m.group(4), n))
    return [item for item in items if item.replacements]


def _numbers(spec):
    """'1, 3–5, 9' → {1, 3, 4, 5, 9}."""
    out = set()
    for a, b in re.findall(r"(\d+)\s*(?:[–-]\s*(\d+))?", spec):
        out.update(range(int(a), int(b or a) + 1))
    return out


def accepted(item):
    """Does the item's decision (its own, else its group's) accept it?"""
    decision = (item.decision or item.group_decision).strip().lower()
    if not decision.startswith("accept"):
        return False
    rest = re.sub(r"\([^)]*\)", "", decision[len("accept"):])     # (Nathan, 2026-11-07)
    if m := re.search(r"\b(?:except|but)\b(.*)", rest):
        return item.number not in _numbers(m.group(1))
    listed = _numbers(rest)
    return not listed or item.number in listed


def select(items, numbers=(), everything=False):
    """The items to apply: all (everything=True), those given by number, or those accepted."""
    if everything:
        return list(items)
    if numbers:
        return [item for item in items if item.number in set(numbers)]
    return [item for item in items if accepted(item)]


# ---------------------------------------------------------------- the USFM side

def target(vid, draft=None):
    """The USFM file holding this verse's chapter: text/<USFM>.usfm, else text/draft/<USFM>.usfm."""
    osis, chapter, _ = tsv.parse_id(vid)
    book = books.select([osis])[0]
    for path in (latex.usfm_path(book), latex.usfm_path(book, draft=True)):
        if path.exists() and re.search(rf"^\\c {chapter}\s*$", path.read_text(encoding="utf-8"), re.M):
            return path
    raise LookupError(f"{vid}: chapter not found in text/ or text/draft/")


def verse_span(usfm, vid):
    """(start, end) of the verse in the USFM text (see the module docstring), or None."""
    _, chapter, verse = tsv.parse_id(vid)
    c = re.search(rf"^\\c {chapter}\s*$", usfm, re.M)
    if not c:
        return None
    nxt = re.search(r"^\\c \d+", usfm[c.end():], re.M)
    chapter_end = c.end() + nxt.start() if nxt else len(usfm)

    def start_of(v):
        m = re.search(rf"\\v {v}(?=\s)", usfm[c.end():chapter_end])
        if not m:
            return None
        at = c.end() + m.start()
        while True:                                   # back over the markers that open the verse's line
            back = re.search(rf"(?:{LAYOUT})\s*$", usfm[c.end():at])
            if not back:
                return at
            at = c.end() + back.start()

    start = c.end() + 1 if verse == 0 else start_of(verse)
    if start is None:
        return None
    later = [s for v in range(verse + 1, verse + 4) if (s := start_of(v)) is not None]
    return start, (later[0] if later else chapter_end)


def _pattern(old):
    return re.compile(r"\s+".join(re.escape(piece) for piece in old.split()))


def _layout(new):
    """Spaces before line-starting markers become line breaks (`… \\p \\v 13` → `…\\n\\p\\n\\v 13`)."""
    new = re.sub(rf"(?<=\S) +(?={LAYOUT})", "\n", new)
    new = re.sub(r"(\\q\d?|\S)( +)(?=\\v )", lambda m: m.group(0) if m.group(1).startswith("\\q") else m.group(1) + "\n",
                 new)
    return re.sub(r"(\\(?:p|m|b|nb))\b\s*\n?", r"\1\n", new)


@dataclass
class Outcome:
    replacement: Replacement
    item: Item
    path: object
    status: str                     # ok, already, missing, ambiguous, no-verse
    count: int = 0


def apply(items, texts=None, to=None):
    """Apply the items' replacements in order. texts: {path: text} to start from (read on demand), updated in
    place. to: a single file to apply everything to (a working copy) instead of the masters.
    Returns ([Outcome], texts)."""
    texts = {} if texts is None else texts
    outcomes = []
    for item in items:
        for r in item.replacements:
            path = to if to is not None else target(r.vid)
            if path not in texts:
                texts[path] = path.read_text(encoding="utf-8")
            usfm = texts[path]
            span = verse_span(usfm, r.vid)
            if span is None or r.column != "la":
                outcomes.append(Outcome(r, item, path, "no-verse"))
                continue
            start, end = span
            hits = list(_pattern(r.old).finditer(usfm, start, end))
            if _pattern(r.old).search(r.new) and len(list(_pattern(r.new).finditer(usfm, start, end))) == 1:
                outcomes.append(Outcome(r, item, path, "already", len(hits)))   # new contains old: done once
                continue
            if len(hits) == 1:
                m = hits[0]
                texts[path] = usfm[:m.start()] + _layout(r.new) + usfm[m.end():]
                outcomes.append(Outcome(r, item, path, "ok", 1))
                continue
            done = len(list(_pattern(r.new).finditer(usfm, start, end))) if r.new.strip() else 0
            status = "already" if not hits and done == 1 and r.old not in r.new else \
                "missing" if not hits else "ambiguous"
            outcomes.append(Outcome(r, item, path, status, len(hits)))
    return outcomes, texts


def write(texts):
    """Write the changed files and rebuild the gold of the settled books among them."""
    rebuilt = []
    for path, text in texts.items():
        path.write_text(text, encoding="utf-8", newline="\n")
        if path.parent == latex.usfm_path(books.BOOKS[0]).parent:
            osis = next(b.osis for b in books.BOOKS if b.usfm == path.stem)
            gold.build([osis])
            rebuilt.append(osis)
    return rebuilt
