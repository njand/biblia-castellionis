"""Merge the readers' rows into data/witnesses/read-1738/2Kgs1-25.tsv and .corrections.tsv; check coverage.

Eleven readers, three leaves each (BRIEF.md, STATUS.md). Run without --write to check, with --write to write.
"""
import sys
from pathlib import Path

ROOT = Path(r"C:\Users\nathanjamesanderson\Documents\biblia-castellionis")
HERE = Path(__file__).parent
voted = (ROOT / "data/witnesses/read-1738/2Kgs1-25.voted.tsv").read_text(encoding="utf-8").splitlines()
vrows = {n: line.split("\t") for n, line in enumerate(voted, 1) if n > 1}
MOVED = set()   # rows a reader moved to another column (fill in if the check reports any as right)
# Claude's corrections after reading the readers' doubtful places on the page (2kgs1-25-transcription-readers.md):
# row -> (reader's text, text as corrected)
FIXES = {
    253: ("hos tres reges conuocauerit Ioua,", "hos tres reges conuocàuerit Ioua,"),   # grave printed over the a, 431/1/98
    2292: ("Hæc postquam Ezechiam Esaiæ re-", "Hæc postquam Ezechiani Esaiæ re-"),   # printed so (misprint), 452/1/32
    3082: ("lia, quos Babyloniæ habebat, muta-", "lia, quos Babyloniæ habebat, #29 muta-"),  # 25:29: numeral's line
    3083: ("tis eius carceris vestimentis, #29 eum-", "tis eius carceris vestimentis, eum-"),    # begins mid-word
}

out, corr, seen, problems = [], [], set(), []
last = 1
for k in range(1, 12):
    p = HERE / f"reader-{k:02d}.tsv"
    if not p.exists():
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
        if row != "+" and int(row) in FIXES:
            was, now = FIXES.pop(int(row))
            if text != was:
                problems.append(f"fix {row}: reader has {text!r}")
            text = now
        out.append((leaf, col, ln, text))
        if row == "+":
            corr.append((f"{last}+", "", text))
        else:
            n = int(row)
            if n in seen:
                problems.append(f"{p.name}: row {n} twice")
            if n < last:
                problems.append(f"{p.name}: row {n} after {last}")
            seen.add(n)
            last = n
            v = vrows[n]
            if (v[0], v[1], v[2]) != (leaf, col, ln) and not text.startswith("%") and n not in MOVED:
                problems.append(f"{p.name}: row {n} place {v[:3]} -> {(leaf, col, ln)}")
            if v[3] != text:
                corr.append((str(n), v[3], text))
if FIXES:
    problems.append(f"fixes not used: {sorted(FIXES)}")
removed = sorted(set(vrows) - seen)
for n in removed:
    corr.append((f"{n}-", vrows[n][3], ""))
print("removed rows:", ", ".join(map(str, removed)))
places = [(a, b, c) for a, b, c, _ in out]
dup = {p for p in places if places.count(p) > 1}
if dup:
    problems.append(f"duplicate places {sorted(dup)[:10]}")
chapters = [t for *_, t in out if t.startswith("\\c ")]
print("chapters:", " ".join(c[3:] for c in chapters))
print("\n".join(problems) or "no problems")
print(len(out), "rows;", sum(1 for c in corr if c[0].isdigit()), "changed;",
      sum(1 for c in corr if c[0].endswith("+")), "added;", len(removed), "removed")
if "--write" in sys.argv and not problems:
    d = ROOT / "data/witnesses/read-1738"
    (d / "2Kgs1-25.tsv").write_text("leaf\tcolumn\tline\ttext\n" + "".join("\t".join(r) + "\n" for r in out),
                                     encoding="utf-8", newline="\n")
    (d / "2Kgs1-25.corrections.tsv").write_text(
        "row\tvoted\tread\n" + "".join("\t".join(c) + "\n" for c in sorted(corr, key=lambda c: int(c[0].rstrip("+-")))),
        encoding="utf-8", newline="\n")
    print("written")
