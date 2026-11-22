"""Merge the readers' rows into data/witnesses/read-1738/1Kgs1-22.tsv and .corrections.tsv; check coverage.

Readers 01-02 saved their whole ranges as reader-NN.partial.tsv; 09-10 share reader-09-10.md. Reader 01's rows from
leaves 386-387 (first shots of pp. 324-325, which archive.org leaves out of its images) are not taken: the merge keeps
02/03's reading of the same pages from leaves 390-391 and writes both side by side, word by word, to
compare-324-325.tsv, every difference to be looked at on the page (STATUS.md).
"""
import difflib, sys
from pathlib import Path

ROOT = Path(r"C:\Users\nathanjamesanderson\Documents\biblia-castellionis")
HERE = Path(__file__).parent
voted = (ROOT / "data/witnesses/read-1738/1Kgs1-22.voted.tsv").read_text(encoding="utf-8").splitlines()
vrows = {n: line.split("\t") for n, line in enumerate(voted, 1) if n > 1}
FIRST_SHOTS = {"386", "387"}   # reader 01's second reading of pp. 324-325
CLEAN_SHOTS = {"390", "391"}
MOVED = {1300}                 # reader 05: fuit. ends leaf 399 col. 1, not col. 0


def source(k):
    for name in (f"reader-{k:02d}.tsv", f"reader-{k:02d}.partial.tsv"):
        if (HERE / name).exists():
            return HERE / name
    return None


out, corr, seen, problems, first, clean = [], [], set(), [], [], []
last = 1
for k in range(1, 16):
    p = source(k)
    if p is None:
        problems.append(f"missing reader-{k:02d}")
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
        if k == 1 and leaf in FIRST_SHOTS:
            first.append(text)
            continue
        if leaf in CLEAN_SHOTS:
            clean.append(text)
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
            if (v[0], v[1], v[2]) != (leaf, col, ln) and not text.startswith("%") and n not in MOVED:
                problems.append(f"{p.name}: row {n} place {v[:3]} -> {(leaf, col, ln)}")
            if v[3] != text:
                corr.append((str(n), v[3], text))
removed = sorted(set(vrows) - seen)
for n in removed:
    corr.append((f"{n}-", vrows[n][3], ""))
runs, start = [], None
for a, b in zip([None] + removed, removed + [None]):
    if start is None:
        start = b
    elif b is None or b != a + 1:
        runs.append(f"{start}-{a}" if a != start else str(start))
        start = b
print("removed rows:", ", ".join(runs))
places = [(a, b, c) for a, b, c, _ in out]
dup = {p for p in places if places.count(p) > 1}
if dup:
    problems.append(f"duplicate places {sorted(dup)[:10]}")
print("\n".join(problems) or "no problems")
print(len(out), "rows;", sum(1 for c in corr if c[0].isdigit()), "changed;",
      sum(1 for c in corr if c[0].endswith("+")), "added;", sum(1 for c in corr if c[0].endswith("-")), "removed")


def words(texts):
    return " ".join(t for t in texts if not t.startswith(("%", "\\"))).replace("- ", "-\n").split()


a, b = words(first), words(clean)
diffs = [(" ".join(a[i1:i2]), " ".join(b[j1:j2]))
         for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes() if tag != "equal"]
print(len(a), "words (reader 01, leaves 386-387) vs", len(b), "(02/03, leaves 390-391):", len(diffs), "differences")
if "--write" in sys.argv and not problems:
    d = ROOT / "data/witnesses/read-1738"
    (d / "1Kgs1-22.tsv").write_text("leaf\tcolumn\tline\ttext\n" + "".join("\t".join(r) + "\n" for r in out),
                                     encoding="utf-8", newline="\n")
    (d / "1Kgs1-22.corrections.tsv").write_text(
        "row\tvoted\tread\n" + "".join("\t".join(c) + "\n" for c in sorted(corr, key=lambda c: int(c[0].rstrip("+-")))),
        encoding="utf-8", newline="\n")
    (HERE / "compare-324-325.tsv").write_text("reader 01 (leaves 386-387)\treaders 02/03 (leaves 390-391)\n"
                                              + "".join(f"{x}\t{y}\n" for x, y in diffs), encoding="utf-8", newline="\n")
    print("written")
