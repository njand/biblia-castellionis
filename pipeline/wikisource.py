"""Latin Wikisource's transcription of Castellio's Bible → one verse TSV per book.

The pages (https://la.wikisource.org/wiki/Biblia_Sacra_interprete_Sebastiano_Castellione) are CC BY-SA 4.0:
credit Wikisource when this text is used. The New Testament follows the 1760 edition and the Old Testament
the 1738 Leipzig edition (archive.org `bibliasacraexseb01cast`); a few books (e.g. the Song of Songs) come
from other printings and keep u for v.

Rows: `id  text  flags`. Verse 0 holds a chapter's summary (argumentum) or a psalm's title; chapter 0
verse 0 a book's argumentum. Flags note anything the parser had to guess, so stage 1 can check it:
  joined      a line without a verse number was appended to the previous verse
  split       a verse number found inside a line started a new verse (normal where a page is set in
              paragraphs, as Exodus and Joshua are; not counted as needing review)
  gap         verse numbers skip (e.g. 5 → 7)
  repeat      a verse number appears twice in a chapter (texts joined)"""

import html
import re

from pipeline import net, paths, tsv
from pipeline.books import Book

API = "https://la.wikisource.org/w/api.php"
WORK = "Biblia Sacra interprete Sebastiano Castellione"
SOURCE = "wikisource"

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
HEADING = re.compile(r"^=+\s*(caput|psalmus)\s+([IVXLCU]+|\d+)\.?\s*=+$", re.IGNORECASE)
OTHER_HEADING = re.compile(r"^=+\s*(.*?)\s*=+$")
VERSE = re.compile(r"^(\d{1,3})\.?\s*(?=\S)(.*)$")
# A verse number inside a line: "… educti. 17. Dimissum" or, in some books, "… legáto. 2 Quum". Only the next
# expected number counts, so stray numerals in the text are left alone.
INLINE_VERSE = re.compile(r"(?<=[\s.,;:!?'\"’”)])(\d{1,3})\.?\s+(?=\S)")

REVIEW_FLAGS = {"joined", "gap", "repeat"}


def needs_review(flags):
    return bool(REVIEW_FLAGS & set(flags.split(",")))


def roman(numeral):
    numeral = numeral.upper().replace("U", "V")
    if numeral.isdigit():
        return int(numeral)
    total = 0
    for i, char in enumerate(numeral):
        value = ROMAN[char]
        total += -value if i + 1 < len(numeral) and ROMAN[numeral[i + 1]] > value else value
    return total


def clean(text):
    """Strip wiki markup and normalize spaces."""
    text = re.sub(r"<ref[^>]*>.*?</ref>|<ref[^>]*/>", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    text = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("'''", "").replace("''", "")
    text = html.unescape(text).replace(" ", " ")
    return re.sub(r"\s+", " ", text).strip()


def split_inline(text, expected):
    """[(None, before), (n, text), …]: split at verse numbers inside a line, starting with `expected`."""
    pieces, last = [], 0
    for match in INLINE_VERSE.finditer(text):
        number = int(match.group(1))
        if number != expected:
            continue
        pieces += [text[last:match.start()].strip(), number]
        last = match.end()
        expected += 1
    pieces.append(text[last:].strip())
    return [(None, pieces[0])] + [(pieces[i], pieces[i + 1]) for i in range(1, len(pieces), 2)]


def parse(wikitext, osis):
    """Return [(id, text, flags)] in page order."""
    rows = []                 # [id, text, set(flags)]
    chapter = None            # None before the first chapter heading; 0 inside a book-level argumentum
    verse = None
    seen = set()
    stop = False

    def start(number, text, flags=()):
        nonlocal verse
        flags = set(flags)
        if number > (verse or 0) + 1:
            flags.add("gap")
        if (chapter, number) in seen:
            flags.add("repeat")
        seen.add((chapter, number))
        verse = number
        rows.append([tsv.verse_id(osis, chapter, number), text, flags])

    def add_text(text, flag):
        """Text with no verse number: continue the current verse, splitting at inline verse numbers."""
        pieces = split_inline(text, (verse or 0) + 1)
        first, rest = pieces[0], pieces[1:]
        if first[1]:
            if rows and verse is not None:
                rows[-1][1] = f"{rows[-1][1]} {first[1]}".strip()
                if flag:
                    rows[-1][2].add(flag)
            else:
                start(0, first[1])
        for number, piece in rest:
            start(number, piece, {"split"})

    for raw in wikitext.splitlines():
        line = raw.strip()
        if not line or stop:
            continue
        if line.startswith(("{{", "|", "}}", "__")):
            continue
        heading = HEADING.match(line)
        if heading:
            chapter, verse = roman(heading.group(2)), None
            continue
        other = OTHER_HEADING.match(line)
        if other:
            title = other.group(1).lower()
            if "finis" in title:
                stop = True
            elif "argumentum" in title:
                chapter, verse = 0, None
            continue
        line = line.lstrip(":*# ")
        if chapter is None:
            # One-chapter books (Obadiah) have no chapter heading: the text starts at verse 1.
            match = VERSE.match(clean(line))
            if not (match and match.group(1) == "1"):
                continue
            chapter = 1
        is_summary = line.startswith("''") and verse is None
        text = clean(line)
        if not text:
            continue
        match = VERSE.match(text)
        if match and not is_summary and _plausible(int(match.group(1)), verse):
            start(int(match.group(1)), "")
            add_text(match.group(2), None)
        elif verse is None:
            start(0, text)
        else:
            add_text(text, "joined")
    return [(vid, text, ",".join(sorted(flags))) for vid, text, flags in rows]


def _plausible(number, previous):
    """A leading number is a verse number if it continues the count (allowing small gaps and restarts)."""
    if previous is None:
        return number <= 5
    return previous < number <= previous + 5


def fetch(book: Book, refresh=False):
    """Download one book's wikitext (cached in sources/wikisource/) and write data/witnesses/wikisource/<osis>.tsv.
    Returns (rows, revid) or None when Wikisource has no page for the book."""
    if not book.ws:
        return None
    cache = paths.SOURCES / SOURCE / f"{book.osis}.wikitext"
    meta = cache.with_suffix(".revid")
    if refresh or not cache.exists():
        reply = net.get_json(API, action="parse", prop="wikitext|revid", format="json",
                             page=f"{WORK}/{book.ws}", formatversion="2")
        if "error" in reply:
            return None
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(reply["parse"]["wikitext"], encoding="utf-8")
        meta.write_text(str(reply["parse"]["revid"]), encoding="utf-8")
    rows = parse(cache.read_text(encoding="utf-8"), book.osis)
    tsv.write(paths.WITNESSES / SOURCE / f"{book.osis}.tsv", rows, header=("id", "text", "flags"))
    return rows, meta.read_text(encoding="utf-8").strip()


def page_url(book: Book):
    return "https://la.wikisource.org/wiki/" + f"{WORK}/{book.ws}".replace(" ", "_")
