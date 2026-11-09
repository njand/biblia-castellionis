"""python -m pipeline <command>

  fetch wikisource [BOOK…]      Wikisource transcription → data/witnesses/wikisource/<osis>.tsv
  fetch wordpress [BOOK…]       2019 WordPress edition → data/witnesses/wordpress/<osis>.tsv
  fetch archive [KEY…] [--hocr] archive.org OCR of each edition → sources/archive/<key>/
  fetch parallel [KEY…]         KJV, BSB, WEB, Vulgate (+ SBLGNT, OSHB) → sources/parallel/; KJV versification
  fetch all                     all of the above (without hOCR)
  ledger refresh                rebuild data/status.tsv from the repo and the witnesses
  ledger set CHAPTER… --stage S [--note TEXT]
  status [BOOK…]                one line per book (stages, witness coverage); --chapters for one line per chapter
  latin CMD …                   read-only fur-fulminis lookups (macron, macron-check --text, ls, attest, …)
  migrate [BOOK…]               LaTeX → text/<USFM>.usfm (+ text/draft/ for commented-out chapters), written only
                                where no USFM exists yet; then USFM → LaTeX compared with the LaTeX (the round trip)
  gold [BOOK…]                  text/*.usfm → data/gold/<osis>.tsv, one row per verse (the harness's answer key)
  harness [BOOK…]               stages 3–4 on the settled chapters from Wikisource, scored against the gold
                                (leave-one-book-out) → data/calibration/harness.md
  align [WITNESS…] [--books B…] align the OCR witnesses (ocr-1681 … ocr-1758, ocr-1726 = TXT/1) to the settled
                                chapters → data/witnesses/<witness>/<osis>.tsv; data/calibration/witnesses.md
  versify BOOK [--apply]        renumber the USFM master to the KJV from data/versification/<osis>.edits.tsv
                                (--draft: text/draft/ from <osis>.draft.edits.tsv; --to FILE: a working copy):
                                preview and write <osis>.REVIEW.md; --apply (all edits approved) rewrites text/ and gold
  review check FILE…            check every Apply line of data/review/*.md (in order, on a copy): matches once?
  review apply FILE… [--write]  apply the accepted items (or --items N…, or --all) to text/ (or text/draft/, or
                                --to a working copy); a dry run unless --write; rebuilds data/gold
  draft BOOK CH-CH              stage 1: Wikisource's chapters → text/draft/<USFM>.usfm (BSB paragraphs; never overwrites)
  collate BOOK CH-CH [--base B] stage 2: every witness against the draft (or settled, wikisource, a USFM file), verse by
                                verse → data/calibration/<osis><CH-CH>-collation.tsv (places, sorted by kind)
  propose BOOK CH-CH [--rates]  stages 3–5 on an unmarked draft, one review item per verse (data/decisions/ for the
                                calls made by reading) → data/review/<osis>F-L-chNN.md and text/draft/<USFM>.preview.usfm
  rules [BOOK…]                 learn spelling rules, Wikisource vs the gold → data/rules/orthography.tsv (proposed),
                                data/rules/REVIEW.md, data/calibration/wikisource.tsv

BOOK is an OSIS code (Matt) or this repo's slug (matthaeus). Downloads are cached; --refresh re-downloads."""

import argparse
import collections
import datetime
import pathlib
import re
import sys

from pipeline import (align, archive, books, collate, gold, harness, latex, latin, ledger, mdz, parallel, paths, review,
                      rules, tsv, verses, versify, wikisource, wordpress)


def fetch_wikisource(names, refresh):
    manifest = []
    for book in books.select(names):
        result = wikisource.fetch(book, refresh)
        if result is None:
            continue
        rows, revid = result
        verses = sum(1 for vid, _, _ in rows if not vid.endswith(".0"))
        flagged = sum(1 for _, _, flags in rows if wikisource.needs_review(flags))
        print(f"wikisource {book.osis:7} {verses:5} verses, {flagged} flagged")
        manifest.append((book.osis, wikisource.page_url(book), revid, verses, flagged))
    _merge_manifest(paths.WITNESSES / "wikisource" / "MANIFEST.tsv", manifest,
                    ("book", "url", "revid", "verses", "flagged", "fetched"))


def fetch_wordpress(names, refresh):
    manifest = []
    for book in books.select(names):
        rows = wordpress.fetch(book, refresh)
        if rows is None:
            continue
        verses = sum(1 for vid, _, _ in rows if not vid.endswith(".0"))
        print(f"wordpress  {book.osis:7} {verses:5} verses")
        manifest.append((book.osis, f"{wordpress.SITE}/{book.wp}/", "", verses, sum(1 for r in rows if r[2])))
    _merge_manifest(paths.WITNESSES / "wordpress" / "MANIFEST.tsv", manifest,
                    ("book", "url", "revid", "verses", "flagged", "fetched"))


def _merge_manifest(path, new_rows, header):
    """Update the rows for the books just fetched; keep the others."""
    today = datetime.date.today().isoformat()
    rows = {row["book"]: [row[h] for h in header] for row in tsv.read(path)} if path.exists() else {}
    for row in new_rows:
        rows[row[0]] = [*row, today]
    order = {book.osis: i for i, book in enumerate(books.BOOKS)}
    tsv.write(path, sorted(rows.values(), key=lambda r: order.get(r[0], 999)), header=header)


def fetch_archive(keys, hocr, refresh):
    selected = [archive.BY_KEY[key] for key in keys] if keys else archive.WITNESSES
    rows = []
    for witness in selected:
        rows.append(archive.fetch(witness, hocr=hocr, refresh=refresh))
        print(f"archive    {witness.key:7} {rows[-1][6]} pages  ({rows[-1][5]})")
    if not keys:
        archive.write_manifest(rows)


def fetch_parallel(keys, refresh):
    selected = [parallel.BY_KEY[key] for key in keys] if keys else parallel.TEXTS
    for text in selected:
        count = parallel.fetch(text, refresh)
        print(f"parallel   {text.key:7} {'%d books' % count if text.usfm else 'downloaded'}")
    if any(text.key == "kjv" for text in selected):
        rows = parallel.write_kjv_versification()
        print(f"versification: {len(rows)} chapters, {sum(r[2] for r in rows)} verses → data/versification/kjv.tsv")


def migrate(names):
    """Write the USFM master of each book that has LaTeX and no USFM yet; check every round trip."""
    for book in books.select(names):
        path = latex.latex_path(book)
        if not path.exists():
            continue
        source = path.read_text(encoding="utf-8")
        live, draft, counts = latex.to_usfm(source, book)
        targets = [(latex.usfm_path(book), live, latex.live_latex(source), "")]
        if draft:
            targets.append((latex.usfm_path(book, draft=True), draft, latex.draft_latex(source), " draft"))
        for target, usfm, original, label in targets:
            if target.exists():
                usfm, action = target.read_text(encoding="utf-8"), "kept (already the master)"
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(usfm, encoding="utf-8", newline="\n")
                action = "written"
            chapters = len(re.findall(r"^\\c ", usfm, flags=re.MULTILINE))
            diffs, size = latex.compare(original, latex.to_latex(usfm))
            print(f"{book.osis + label:11} {target.relative_to(paths.ROOT).as_posix():24} {action}; {chapters} chapters; "
                  f"round trip: {size} tokens, {len(diffs)} difference(s)")
            for old, new, context in diffs:
                print(f"    …{context[-50:]}  {' '.join(old) or '∅'}  →  {' '.join(new) or '∅'}")
        for line, comment in latex.comments(source):
            print(f"    not carried over (comment), {path.name}:{line}: {comment}")


def align_witnesses(keys, names):
    """Align each OCR witness to the settled chapters (gold), write its verse rows, and measure it."""
    sources = [align.BY_SOURCE[k] for k in keys] if keys else align.SOURCES
    reference = [("wikisource", "Wikisource (1760 NT, 1738 OT)"), ("wordpress", "WordPress 2019 (your macrons)")]
    loaded, summary = {}, []
    settled = [b for b in books.select(names) if gold.load(b.osis)]
    for source in [*sources, *reference]:
        key, label = (source.key, source.label) if isinstance(source, align.Source) else source
        for book in settled:
            base = [(vid, row["text"]) for vid, row in gold.load(book.osis).items()]
            if isinstance(source, align.Source):
                files = align.texts(source, book, paths)
                witnesses = [loaded[f] if f in loaded else loaded.setdefault(
                    f, mdz.witness() if f == "mdz-1573" else align.Witness(f.read_text(encoding="utf-8"))) for f in files]
            else:
                path = paths.WITNESSES / key / f"{book.osis}.tsv"
                witnesses = [align.Witness("\n".join(r["text"] for r in tsv.read(path)))] if path.exists() else []
            if not witnesses:
                continue
            chapters = align.align_book(witnesses, base)
            s = align.score(chapters)
            if s["found"] < s["words"] * 0.05:
                continue                                   # the book is not in this witness
            seen, agree = align.number_agreement(chapters)
            summary.append((key, label, book.osis, s, seen, agree, align.disagreements(chapters)))
            print(f"{key:11} {book.osis:5} found {s['found'] / s['words']:6.1%}  agree {s['exact'] / max(1, s['found']):6.2%}"
                  f"  f/s-blind {s['fs'] / max(1, s['found']):6.2%}  verse numbers {agree}/{seen}")
            if isinstance(source, align.Source):
                rows = []
                for chapter in chapters:
                    found = collections.Counter(vid for vid, _, w in chapter.matches if w is not None)
                    total = collections.Counter(vid for vid, _, _ in chapter.matches)
                    for vid in total:
                        rows.append((vid, chapter.verses.get(vid, ""), align.row_flags(chapter, vid, found[vid], total[vid])))
                tsv.write(paths.WITNESSES / key / f"{book.osis}.tsv", rows, header=("id", "text", "flags"))
    path = align.write_report(summary, paths)
    print(f"→ {path.relative_to(paths.ROOT).as_posix()}")


def review_files(action, files, write, numbers, everything, to):
    """`review check` / `review apply`: see pipeline/review.py."""
    texts, outcomes = {}, []
    target = pathlib.Path(to) if to else None
    if target is not None and not target.exists():
        raise SystemExit(f"{to}: no such file (copy the master there first)")
    for name in files:
        items = review.parse(pathlib.Path(name).read_text(encoding="utf-8"))
        selected = items if action == "check" else review.select(items, numbers, everything)
        print(f"{name}: {len(items)} items, {sum(len(i.replacements) for i in items)} Apply lines; "
              f"{len(selected)} selected")
        done, texts = review.apply(selected, texts, target)
        outcomes += done
    counts = collections.Counter(o.status for o in outcomes)
    for o in outcomes:
        if o.status not in ("ok", "already"):
            r = o.replacement
            print(f"  {o.status:9} line {r.line} {o.item.label}: `{r.vid}` `{r.old}` ({o.count} matches)")
    print(", ".join(f"{n} {status}" for status, n in sorted(counts.items())) or "nothing selected")
    failed = sum(n for status, n in counts.items() if status not in ("ok", "already"))
    if action == "apply":
        if failed:
            print("not written: every selected replacement must match once (all or nothing)")
            return 1
        if not write:
            print("dry run: add --write to write " + ", ".join(sorted({p.relative_to(paths.ROOT).as_posix() if p.is_relative_to(paths.ROOT) else str(p) for p in texts})))
            return 0
        rebuilt = review.write({p: t for p, t in texts.items() if counts["ok"]})
        print("written" + (f"; data/gold rebuilt for {', '.join(rebuilt)}" if rebuilt else ""))
    return 1 if failed else 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if argv and argv[0] == "latin":
        return latin.run(argv[1:])
    parser = argparse.ArgumentParser(prog="python -m pipeline", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    fetch = sub.add_parser("fetch")
    fetch.add_argument("source", choices=["wikisource", "wordpress", "archive", "parallel", "all"])
    fetch.add_argument("names", nargs="*")
    fetch.add_argument("--hocr", action="store_true", help="archive: also download hOCR word boxes")
    fetch.add_argument("--refresh", action="store_true", help="re-download instead of using the cache")

    led = sub.add_parser("ledger")
    led.add_argument("action", choices=["refresh", "set"])
    led.add_argument("chapters", nargs="*")
    led.add_argument("--stage")
    led.add_argument("--note")

    status = sub.add_parser("status")
    status.add_argument("names", nargs="*")
    status.add_argument("--chapters", action="store_true")

    mig = sub.add_parser("migrate")
    mig.add_argument("names", nargs="*")
    gld = sub.add_parser("gold")
    gld.add_argument("names", nargs="*")
    rul = sub.add_parser("rules")
    rul.add_argument("names", nargs="*")
    har = sub.add_parser("harness")
    har.add_argument("names", nargs="*")
    aln = sub.add_parser("align")
    aln.add_argument("witnesses", nargs="*")
    aln.add_argument("--books", nargs="*", default=[])
    ver = sub.add_parser("versify")
    ver.add_argument("name")
    ver.add_argument("--apply", action="store_true", help="rewrite text/<USFM>.usfm (every edit must be approved)")
    ver.add_argument("--draft", action="store_true", help="the drafted chapters (text/draft/), from <osis>.draft.edits.tsv")
    ver.add_argument("--to", help="renumber this working copy instead (approved or not)")

    rev = sub.add_parser("review")
    rev.add_argument("action", choices=["check", "apply"])
    rev.add_argument("files", nargs="+")
    rev.add_argument("--write", action="store_true", help="apply: write the files (default: a dry run)")
    rev.add_argument("--items", nargs="*", type=int, default=[], help="apply these item numbers, whatever their decision")
    rev.add_argument("--all", action="store_true", help="apply every item (for a preview on a working copy)")
    rev.add_argument("--to", help="apply to this file (a working copy) instead of text/")

    drf = sub.add_parser("draft")
    drf.add_argument("name")
    drf.add_argument("chapters", help="e.g. 6-16")
    col = sub.add_parser("collate")
    col.add_argument("name")
    col.add_argument("chapters", help="e.g. 14-28")
    col.add_argument("--base", default="draft", help="draft (default), settled, wikisource, or a USFM file")

    prp = sub.add_parser("propose", help="stages 3–5 on an unmarked draft, one review item per verse")
    prp.add_argument("name")
    prp.add_argument("chapters", help="e.g. 6-16")
    prp.add_argument("--rates", action="store_true", help="also measure each flag kind on the settled chapters")

    sub.add_parser("latin", help="read-only Latin lookups (see `python -m pipeline latin --help`)")

    args = parser.parse_args(argv)
    if args.command == "fetch":
        if args.source in ("wikisource", "all"):
            fetch_wikisource(args.names if args.source == "wikisource" else [], args.refresh)
        if args.source in ("wordpress", "all"):
            fetch_wordpress(args.names if args.source == "wordpress" else [], args.refresh)
        if args.source in ("parallel", "all"):
            fetch_parallel(args.names if args.source == "parallel" else [], args.refresh)
        if args.source in ("archive", "all"):
            fetch_archive(args.names if args.source == "archive" else [], args.hocr, args.refresh)
        if args.source != "archive":
            ledger.refresh()
    elif args.command == "migrate":
        migrate(args.names)
        ledger.refresh()
    elif args.command == "gold":
        for osis, rows in gold.build(args.names).items():
            chapters = len({vid.rsplit(".", 1)[0] for vid, *_ in rows})
            print(f"gold {osis:6} {chapters:3} chapters, {len(rows):5} verses → data/gold/{osis}.tsv")
    elif args.command == "harness":
        totals, per_book = harness.run(args.names)
        for variant, t in totals.items():
            print(f"{variant} {harness.NAMES[variant]:26} words {t.word_ok / t.words:7.2%}  spelling "
                  f"{t.spelling_ok / max(1, t.spelled):7.2%}  vowels {t.vowels_ok / max(1, t.vowels):7.2%}")
        path = paths.DATA / "calibration" / "harness.md"
        path.write_text(harness.report(totals, per_book), encoding="utf-8", newline="\n")
        print(f"→ {path.relative_to(paths.ROOT).as_posix()}")
    elif args.command == "align":
        align_witnesses(args.witnesses, args.books)
    elif args.command in ("draft", "collate"):
        book = books.select([args.name])[0]
        first, _, last = args.chapters.partition("-")
        chapters = range(int(first), int(last or first) + 1)
        if args.command == "draft":
            target = latex.usfm_path(book, draft=True)
            if target.exists():
                raise SystemExit(f"{target.relative_to(paths.ROOT).as_posix()} exists: a draft is never overwritten")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(collate.draft_usfm(book.osis, chapters), encoding="utf-8", newline="\n")
            print(f"→ {target.relative_to(paths.ROOT).as_posix()}: Wikisource {book.osis} {args.chapters}, BSB paragraphs")
            return 0
        base = args.base if args.base in ("draft", "settled", "wikisource") else pathlib.Path(args.base)
        places, _ = collate.collate(book.osis, chapters, base)
        rows = [(p.vid, p.kind, p.sort, p.text, " | ".join(f"{','.join(who)}: {next(iter(who.values()))}"
                                                          for who in p.readings.values()), ",".join(p.support), p.context)
                for ps in places.values() for p in ps if p.kind != "noise"]
        path = paths.DATA / "calibration" / f"{book.osis}{args.chapters}-collation.tsv"
        tsv.write(path, rows, header=("id", "kind", "sort", "text", "readings", "support", "context"))
        counts = collections.Counter((r[1], r[2]) for r in rows)
        print(", ".join(f"{k} {s} {n}" for (k, s), n in sorted(counts.items())))
        print(f"→ {path.relative_to(paths.ROOT).as_posix()} (noise left out; crop with pipeline.mdz.find/fetch_crop)")
    elif args.command == "propose":
        book = books.select([args.name])[0]
        first, _, last = args.chapters.partition("-")
        found, written = verses.write(book.osis, range(int(first), int(last or first) + 1))
        kinds = collections.Counter(k for v in found for k, n in v.kinds.items() for _ in range(n))
        flags = collections.Counter(f.kind for v in found for f in v.flags)
        print(f"{len(found)} verses, {sum(kinds.values())} words; " + ", ".join(f"{k} {n}" for k, n in kinds.most_common()))
        print(f"flagged {sum(flags.values())}: " + ", ".join(f"{k} {n}" for k, n in flags.most_common()))
        print(f"verses with layout from data/decisions/: {sum(v.quotes for v in found)}; with no flag: "
              f"{sum(not v.flags and not v.quotes for v in found)}")
        for path in written:
            print(f"→ {path.relative_to(paths.ROOT).as_posix()}")
        if args.rates:
            for label, (table, examples) in (("macrons", verses.rates()), ("spelling", verses.spelling_rates()),
                                             ("case", verses.case_rates())):
                for kind, (n, wrong) in sorted(table.items(), key=lambda kv: -kv[1][0]):
                    print(f"{label:9} {kind:38} {n:6} {wrong:5} {wrong / max(1, n):7.2%}  "
                          + "; ".join(examples.get(kind, [])[:3]))
    elif args.command == "review":
        return review_files(args.action, args.files, args.write, args.items, args.all, args.to)
    elif args.command == "versify":
        book = books.select([args.name])[0]
        path, edits = latex.usfm_path(book, draft=args.draft), versify.load_edits(book.osis, args.draft)
        edits_file = versify.edits_path(book.osis, args.draft)
        if not edits:
            parser.error(f"no {edits_file.relative_to(paths.ROOT).as_posix()}")
        if any(e["status"] == "applied" for e in edits):
            raise SystemExit(f"{book.osis}: these edits are already applied (their ids are in the old numbering); "
                             "list new edits in a fresh file")
        before = (pathlib.Path(args.to) if args.to else path).read_text(encoding="utf-8")
        after, changes = versify.apply_edits(before, book.osis, edits)
        problems = versify.check(before, after, book.osis, edits)
        moved = sum(1 for _, _, how in changes if how != "renumbered")
        print(f"{book.osis}: {len(edits)} edits, {moved} boundaries moved, {len(changes) - moved} verses renumbered; "
              + ("checks passed (same words, KJV verse counts)" if not problems else "PROBLEMS: " + "; ".join(problems)))
        if args.to:                                       # a working copy: renumbered, approved or not
            pathlib.Path(args.to).write_text(after, encoding="utf-8", newline="\n")
            print(f"→ {args.to} renumbered (a working copy)")
            return 1 if problems else 0
        if not args.draft:                                # the draft's edits are reviewed in its stage-2 file
            review = versify.EDITS / f"{book.osis}.REVIEW.md"
            review.write_text(versify.report(before, book.osis, edits, gold.load(book.osis),
                                             {r["id"]: r["text"] for r in tsv.read(paths.SOURCES / "parallel" / "kjv" / f"{book.osis}.tsv")}),
                              encoding="utf-8", newline="\n")
            print(f"→ {review.relative_to(paths.ROOT).as_posix()}")
        if args.apply:
            waiting = [e["at"] for e in edits if e["status"] != "approved"]
            if waiting or problems:
                raise SystemExit(f"not applied: {'edits not approved: ' + ', '.join(waiting) if waiting else 'checks failed'}")
            path.write_text(after, encoding="utf-8", newline="\n")
            tsv.write(edits_file,
                      [(e["op"], e["at"], e["anchor"], "applied", e["note"]) for e in edits],
                      header=("op", "at", "anchor", "status", "note"))
            if not args.draft:
                gold.build([book.osis])
                ledger.refresh()
            print(f"→ {path.relative_to(paths.ROOT).as_posix()} renumbered"
                  + ("" if args.draft else f"; data/gold/{book.osis}.tsv rebuilt"))
    elif args.command == "rules":
        learned = rules.learn(args.names)
        kinds = {}
        for pair in learned.pairs:
            kinds[pair.kind] = kinds.get(pair.kind, 0) + 1
        print(f"{learned.gold_words} gold words: "
              + ", ".join(f"{kind} {n}" for kind, n in sorted(kinds.items(), key=lambda kv: -kv[1])))
        for path in (rules.write_rules(rules.rule_rows(learned)), rules.write_calibration(learned.pairs),
                     rules.write_review(rules.review(learned, args.names))):
            print(f"→ {path.relative_to(paths.ROOT).as_posix()}")
    elif args.command == "ledger":
        if args.action == "refresh":
            rows = ledger.refresh()
            print(f"data/status.tsv: {len(rows)} chapters")
        else:
            if not args.stage or not args.chapters:
                parser.error("ledger set needs CHAPTER… and --stage")
            ledger.set_stage(args.chapters, args.stage, args.note)
    elif args.command == "status":
        rows = list(ledger.load().values())
        if not rows:
            print("no ledger yet: run `python -m pipeline fetch all`")
            return 1
        selected = {book.osis for book in books.select(args.names)} if args.names else None
        if args.chapters:
            for row in rows:
                if selected is None or row["chapter"].rsplit(".", 1)[0] in selected:
                    print("  ".join(f"{row[column]}" for column in ledger.HEADER).rstrip())
        else:
            print("\n".join(ledger.summary(rows, selected)))
    return 0
