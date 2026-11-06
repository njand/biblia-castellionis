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
  versify BOOK [--apply]        renumber the USFM master to the KJV from data/versification/<osis>.edits.tsv:
                                preview and write <osis>.REVIEW.md; --apply (all edits approved) rewrites text/ and gold
  rules [BOOK…]                 learn spelling rules, Wikisource vs the gold → data/rules/orthography.tsv (proposed),
                                data/rules/REVIEW.md, data/calibration/wikisource.tsv

BOOK is an OSIS code (Matt) or this repo's slug (matthaeus). Downloads are cached; --refresh re-downloads."""

import argparse
import collections
import datetime
import re
import sys

from pipeline import (align, archive, books, gold, harness, latex, latin, ledger, parallel, paths, rules, tsv, versify, wikisource,
                      wordpress)


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
                witnesses = [loaded.setdefault(f, align.Witness(f.read_text(encoding="utf-8"))) for f in files]
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
                        flag = "missing" if not found[vid] else "partial" if found[vid] < 0.8 * total[vid] else ""
                        rows.append((vid, chapter.verses.get(vid, ""), flag))
                tsv.write(paths.WITNESSES / key / f"{book.osis}.tsv", rows, header=("id", "text", "flags"))
    path = align.write_report(summary, paths)
    print(f"→ {path.relative_to(paths.ROOT).as_posix()}")


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
    elif args.command == "versify":
        book = books.select([args.name])[0]
        path, edits = latex.usfm_path(book), versify.load_edits(book.osis)
        if not edits:
            parser.error(f"no data/versification/{book.osis}.edits.tsv")
        if any(e["status"] == "applied" for e in edits):
            raise SystemExit(f"{book.osis}: these edits are already applied (their ids are in the old numbering); "
                             "list new edits in a fresh file")
        before = path.read_text(encoding="utf-8")
        after, changes = versify.apply_edits(before, book.osis, edits)
        problems = versify.check(before, after, book.osis)
        moved = sum(1 for _, _, how in changes if how != "renumbered")
        print(f"{book.osis}: {len(edits)} edits, {moved} boundaries moved, {len(changes) - moved} verses renumbered; "
              + ("checks passed (same words, KJV verse counts)" if not problems else "PROBLEMS: " + "; ".join(problems)))
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
            tsv.write(versify.EDITS / f"{book.osis}.edits.tsv",
                      [(e["op"], e["at"], e["anchor"], "applied", e["note"]) for e in edits],
                      header=("op", "at", "anchor", "status", "note"))
            gold.build([book.osis])
            ledger.refresh()
            print(f"→ {path.relative_to(paths.ROOT).as_posix()} renumbered; data/gold/{book.osis}.tsv rebuilt")
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
