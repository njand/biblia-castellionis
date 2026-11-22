"""Merge the verse readers' rows (r1-r9) into data/decisions/1Kgs.layout.tsv and 1Kgs.forms.tsv.

The draft fixes of 1kgs1-22-draft-fixes.md §3 were applied to the draft after the readers wrote their rows, so each
fix's old words are replaced by the new in the layout rows of its verse (the readers kept the draft's words then).
Checks: one layout row per verse, every row's verse id in 1 Kings.
"""
import re, sys
from pathlib import Path

ROOT = Path(r"C:\Users\nathanjamesanderson\Documents\biblia-castellionis")
HERE = Path(__file__).parent
fixes = {}
text = (ROOT / "data/review/1kgs1-22-draft-fixes.md").read_text(encoding="utf-8")
for m in re.finditer(r"\*\*Apply:\*\* `(1Kgs\.[\d.]+)` la: `([^`]+)` → `([^`]+)`", text.split("## 3.")[1]):
    fixes.setdefault(m[1], []).append((m[2], m[3]))

layout, forms, problems, seen, used = [], [], [], {}, set()
for k in range(1, 10):
    for kind, out in (("layout", layout), ("forms", forms)):
        p = HERE / f"r{k}-{kind}.tsv"
        lines = p.read_text(encoding="utf-8-sig").splitlines()
        for line in lines[1:]:
            if not line.strip():
                continue
            f = line.split("\t")
            if kind == "layout":
                if len(f) != 4:
                    problems.append(f"{p.name}: {len(f)} fields: {line[:60]}")
                    continue
                if f[0] in seen:
                    problems.append(f"{p.name}: {f[0]} also in {seen[f[0]]}")
                seen[f[0]] = p.name
                for old, new in fixes.get(f[0], []):
                    if old in f[2]:
                        f[2] = f[2].replace(old, new)
                        used.add((f[0], old))
                    else:   # the reader may have changed a capital or stop next to the words
                        o, n = old.split(), new.split()
                        core = [(a, b) for a, b in zip(o, n) if a != b] if len(o) == len(n) else [(old, new)]
                        core += [(a[:1].upper() + a[1:], b[:1].upper() + b[1:]) for a, b in core]
                        for a, b in core:
                            if a in f[2]:
                                f[2] = f[2].replace(a, b)
                                used.add((f[0], old))
            elif len(f) != 3:
                problems.append(f"{p.name}: {len(f)} fields: {line[:60]}")
                continue
            out.append(f)
for vid, pairs in fixes.items():
    for old, _ in pairs:
        if vid in seen and (vid, old) not in used:
            problems.append(f"fix {vid} {old!r} not found in its layout row")
import unicodedata
def bare(w):   # a form without macrons, æ as ae, lower case: the word it decides
    w = unicodedata.normalize("NFD", w.replace("æ", "ae").replace("Æ", "Ae").replace("œ", "oe"))
    return "".join(c for c in w if unicodedata.category(c) != "Mn").lower()
names = HERE / "names-forms.tsv"
if names.exists():   # the names reader's rows over the verse readers'
    nrows = [l.split("\t") for l in names.read_text(encoding="utf-8-sig").splitlines()[1:] if l.strip()]
    over = {(r[0], bare(r[1])) for r in nrows}
    before = len(forms)
    forms = [r for r in forms if (r[0], bare(r[1])) not in over] + nrows
    print(len(nrows), "names rows;", before + len(nrows) - len(forms), "reader rows overridden")
for k in range(1, 5):   # the proofreaders' rows over all: a layout row by verse, a form by (verse, word)
    pl, pf = HERE / f"p{k}-layout.tsv", HERE / f"p{k}-forms.tsv"
    if pl.exists():
        rows = [l.split("\t") for l in pl.read_text(encoding="utf-8-sig").splitlines()[1:] if l.strip()]
        problems += [f"{pl.name}: {len(r)} fields: {r[0]}" for r in rows if len(r) != 4]
        ids = {r[0] for r in rows}
        layout = [r for r in layout if r[0] not in ids] + rows
        print(pl.name, len(rows), "layout rows")
    if pf.exists():
        rows = [l.split("\t") for l in pf.read_text(encoding="utf-8-sig").splitlines()[1:] if l.strip()]
        problems += [f"{pf.name}: {len(r)} fields: {r[0]}" for r in rows if len(r) != 3]
        over = {(r[0], bare(r[1])) for r in rows}
        forms = [r for r in forms if (r[0], bare(r[1])) not in over] + rows
        print(pf.name, len(rows), "forms rows")
key = lambda r: tuple(int(x) for x in r[0].split("#")[0].split(".")[1:])
layout.sort(key=key)
forms.sort(key=key)
print("\n".join(problems) or "no problems")
print(len(layout), "layout rows;", len(forms), "forms rows; fixes carried into", len(used), "rows")
if "--write" in sys.argv and not problems:
    d = ROOT / "data/decisions"
    (d / "1Kgs.layout.tsv").write_text("id\tmarks\ttext\tnote\n" + "".join("\t".join(r) + "\n" for r in layout),
                                       encoding="utf-8", newline="\n")
    (d / "1Kgs.forms.tsv").write_text("id\tform\tnote\n" + "".join("\t".join(r) + "\n" for r in forms),
                                      encoding="utf-8", newline="\n")
    print("written")
