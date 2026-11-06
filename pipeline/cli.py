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

BOOK is an OSIS code (Matt) or this repo's slug (matthaeus). Downloads are cached; --refresh re-downloads."""

import argparse
import datetime
import sys

from pipeline import archive, books, latin, ledger, parallel, paths, tsv, wikisource, wordpress


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
