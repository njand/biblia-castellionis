"""Merge the readers' rows into data/witnesses/read-1738/2Sam1-24.tsv and .corrections.tsv; check coverage."""
import csv, sys
from pathlib import Path

ROOT = Path(r"C:\Users\nathanjamesanderson\Documents\biblia-castellionis")
HERE = Path(__file__).parent
voted = (ROOT / "data/witnesses/read-1738/2Sam1-24.voted.tsv").read_text(encoding="utf-8").splitlines()
vrows = {n: line.split("\t") for n, line in enumerate(voted, 1) if n > 1}

out, corr, seen, problems = [], [], set(), []
last = 1
for k in range(1, 15):
    p = HERE / f"reader-{k:02d}.tsv"
    if not p.exists():
        problems.append(f"missing {p.name}")
        continue
    lines = p.read_text(encoding="utf-8-sig").splitlines()
    for i, line in enumerate(lines[1:], 2):
        if not line.strip():
            continue
        f = line.split("\t")
        if len(f) != 5:
            problems.append(f"{p.name}:{i}: {len(f)} fields: {line[:60]}")
            continue
        row, leaf, col, ln, text = f
        out.append((leaf, col, ln, text))
        if row == "+":
            corr.append((f"{last}+", "", text))
        else:
            n = int(row)
            if n in seen:
                problems.append(f"{p.name}: row {n} twice")
            seen.add(n)
            last = n
            v = vrows[n]
            if (v[0], v[1], v[2]) != (leaf, col, ln) and not text.startswith("%"):
                problems.append(f"{p.name}: row {n} place {v[:3]} -> {(leaf, col, ln)}")
            if v[3] != text:
                corr.append((str(n), v[3], text))
for n in sorted(set(vrows) - seen):
    corr.append((f"{n}-", vrows[n][3], ""))
    print("removed", n, vrows[n][3])
places = [(a, b, c) for a, b, c, _ in out]
dup = {p for p in places if places.count(p) > 1}
if dup:
    problems.append(f"duplicate places {sorted(dup)[:10]}")
print("\n".join(problems) or "no problems")
print(len(out), "rows;", sum(1 for c in corr if c[0].isdigit()), "changed;",
      sum(1 for c in corr if c[0].endswith("+")), "added;", sum(1 for c in corr if c[0].endswith("-")), "removed")
if "--write" in sys.argv and not problems:
    d = ROOT / "data/witnesses/read-1738"
    (d / "2Sam1-24.tsv").write_text("leaf\tcolumn\tline\ttext\n" + "".join("\t".join(r) + "\n" for r in out),
                                     encoding="utf-8", newline="\n")
    (d / "2Sam1-24.corrections.tsv").write_text("row\tvoted\tread\n" + "".join("\t".join(c) + "\n" for c in sorted(corr, key=lambda c: int(c[0].rstrip("+-")))),
                                                 encoding="utf-8", newline="\n")
    print("written")
