"""Stage 7: every published format, generated from the USFM master (text/<USFM code>.usfm) into build/.

  build/site/                 the website (GitHub Pages): a page per chapter, verse anchors (matthaeus/14.html#3),
                              a macron switch, an optional English column (pipeline/site.py)
  build/epub/<stem>.epub      EPUB 3 with macrons, and <stem>-sine-macronibus.epub without (pipeline/epub.py)
  build/pdf/<stem>.tex        print LaTeX in the legacy markup, under pipeline/templates/preamble.tex; <stem>.pdf when a
                              TeX install is found (pipeline/pdf.py)
  build/txt/<stem>.txt        reading text with and without macrons; <stem>.tsv and <stem>.json one row per verse

The USFM is parsed into a small model (Book → Chapter → Block → content) shared by every format. Only the markers
of PLAN.md §3 are accepted; anything else stops the build, so a typo in the master never reaches print. Nothing
in build/ is edited by hand: change the USFM and rebuild."""

import datetime
import json
import pathlib
import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import books, latex, paths, tsv

TEXT = paths.ROOT / "text"
BUILD = paths.ROOT / "build"
MANIFEST = paths.WITNESSES / "wikisource" / "MANIFEST.tsv"
SOFT_HYPHEN = latex.SOFT_HYPHEN
REPOSITORY = "https://github.com/njand/biblia-castellionis"
SITE = "https://njand.github.io/biblia-castellionis/"           # GitHub Pages (.github/workflows/pages.yml)


def short_url(url):
    """An address as printed: without the scheme or a closing slash ("github.com/njand/biblia-castellionis")."""
    return re.sub(r"^https?://", "", url).rstrip("/")

HEADER = {"id", "usfm", "ide", "h", "toc1", "toc2", "toc3", "mt", "mt1", "mt2", "mt3", "rem"}
PARAGRAPHS = {"p", "m", "nb", "b", "q1", "q2", "q3"}
CHARACTERS = {"qt", "qt*"}

# Collections with a name of their own; any other selection is "Biblia Sacra".
COLLECTIONS = {("Matt", "Mark", "Luke", "John"): ("Ēvangelia", "evangelia")}
SERIES = "Biblia Sacra ex Sebastiānī Castelliōnis interpretātiōne"
EDITOR = "Nathan Anderson"                     # named in every colophon (Nathan, 2026-11-10)


class UsfmError(ValueError):
    pass


@dataclass
class Block:
    kind: str                                   # p, m, nb, b (stanza break), q1–q3
    content: list = field(default_factory=list)  # ("v", n), ("text", s), ("qt", True|False),
                                                 # ("note", (reference, text)): a footnote (decision 53)


@dataclass
class Chapter:
    number: int
    summary: str = ""                           # \cd: the argumentum (verse 0)
    title: str = ""                             # \d: a psalm title (verse 0)
    closing: str = ""                           # \cls: a letter's subscription, after the last verse
    blocks: list = field(default_factory=list)


@dataclass
class Book:
    info: books.Book
    short: str                                  # \h, the running head: "Matthæus"
    long: str                                   # \toc1: "Ēvangelium Auctōre Matthæō"
    title: list                                 # [(line, minor)]: \mt1 lines (split at //) and \mt2/\mt3 lines
                                                # (minor, set smaller), in the file's order
    chapters: list = field(default_factory=list)

    @property
    def slug(self):
        return self.info.slug.replace(" ", "-")


def strip_macrons(text):
    """ā → a, ȳ → y; æ, œ, quotation marks and everything else unchanged."""
    return unicodedata.normalize("NFC", unicodedata.normalize("NFD", text).replace("\u0304", ""))


def parse(usfm, info):
    """The Book model of one USFM file. Raises UsfmError on any marker outside PLAN.md §3, on text outside a
    paragraph, on verses out of order and on an unclosed \\qt."""
    header, chapters, chapter, verse = {}, [], None, 0
    titles = []                         # [(line, minor)] of \mt, \mt1, \mt2, \mt3

    def fail(message, line_no):
        raise UsfmError(f"{info.usfm}.usfm line {line_no}: {message}")

    for line_no, line in enumerate(usfm.splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        match = re.match(r"\\([a-z]+\d*)(?:\s+(.*)|$)", stripped)
        marker, rest = (match.group(1), (match.group(2) or "").strip()) if match else (None, stripped)
        if marker in HEADER:
            header[marker] = rest
            if marker in ("mt", "mt1", "mt2", "mt3"):
                titles.extend((part.strip(), marker in ("mt2", "mt3")) for part in rest.split("//"))
            continue
        if marker == "c":
            number = int(rest)
            if number != len(chapters) + 1:
                fail(f"\\c {number} where chapter {len(chapters) + 1} was expected", line_no)
            chapter, verse = Chapter(number), 0
            chapters.append(chapter)
            continue
        if chapter is None:
            fail(f"{stripped[:40]!r} before the first \\c", line_no)
        if chapter.closing:
            fail(f"{stripped[:40]!r} after the chapter's \\cls", line_no)
        if marker == "cls":                             # a letter's subscription: the chapter's last line
            if not chapter.blocks or not rest:
                fail("\\cls before the chapter's text, or empty", line_no)
            chapter.closing = rest
            continue
        if marker in ("cd", "d"):
            if chapter.blocks:
                fail(f"\\{marker} after the chapter's text began", line_no)
            setattr(chapter, "summary" if marker == "cd" else "title", rest)
            continue
        if marker not in PARAGRAPHS and chapter.blocks and chapter.blocks[-1].content:
            stripped = " " + stripped                   # a line break inside a paragraph is a space
        for kind, value in latex._inline(stripped):
            if kind == "char" and value in PARAGRAPHS:  # at the start of a line or inside one ("…? \q1 \qt …")
                chapter.blocks.append(Block(value))
                continue
            if not chapter.blocks:
                fail(f"text outside a paragraph: {stripped[:40]!r}", line_no)
            block = chapter.blocks[-1]
            if kind == "v":
                verse += 1
                if value != verse:
                    fail(f"\\v {value} where verse {verse} was expected", line_no)
                block.content.append(("v", value))
            elif kind == "char":
                if value not in CHARACTERS:
                    fail(f"marker \\{value} is not one this edition uses (PLAN.md §3)", line_no)
                block.content.append(("qt", value == "qt"))
            elif kind == "note":
                block.content.append(("note", value))
            elif block.content or value.strip():
                block.content.append(("text", value))
    if not chapters:
        raise UsfmError(f"{info.usfm}.usfm has no chapters")
    for chapter in chapters:
        _check_qt(chapter, info)
    short = header.get("h") or header.get("toc2") or info.osis
    long = header.get("toc1") or short
    title = titles or [(part.strip(), False) for part in long.split("//")]
    return Book(info, short, long, title, chapters)


def _check_qt(chapter, info):
    open_ = False
    for block in chapter.blocks:
        for kind, value in block.content:
            if kind == "qt":
                if value == open_:
                    raise UsfmError(f"{info.osis}.{chapter.number}: \\qt{'' if value else '*'} twice in a row")
                open_ = value
    if open_:
        raise UsfmError(f"{info.osis}.{chapter.number}: \\qt not closed")


def load(names=()):
    """[Book] for every selected book that has a USFM master, in canon order."""
    out = []
    for info in books.select(names):
        path = latex.usfm_path(info)
        if path.exists():
            out.append(parse(path.read_text(encoding="utf-8"), info))
    if not out:
        raise SystemExit("no USFM master in text/ for the books asked for")
    return out


def verse_segments(chapter):
    """{verse: [(text, italic, line_break_before)]} for one chapter; the pieces join with "" (a piece that opens a
    new paragraph or line of a verse begins with a space). Verse 0 is the summary (or psalm title)."""
    out, verse, italic = {}, 0, False
    if chapter.title or chapter.summary:
        out[0] = [(chapter.title or chapter.summary, False, False)]
    for block in chapter.blocks:
        new_line = True
        for kind, value in block.content:
            if kind == "v":
                verse, new_line = value, False
                out.setdefault(verse, [])
            elif kind == "qt":
                italic = value
            elif kind == "note":                        # not part of the verse's text
                continue
            elif verse:
                out[verse].append((" " + value if new_line else value, italic,
                                   new_line and block.kind.startswith("q")))
                new_line = False
    return out


def plain(text):
    """Reading text without markup: soft hyphens dropped, spaces collapsed."""
    return re.sub(r"\s+", " ", text.replace(SOFT_HYPHEN, "")).strip()


def verses(book):
    """[(id, chapter, verse, text)] for a book, as the gold set has them (verse 0 where a chapter has one)."""
    rows = []
    for chapter in book.chapters:
        for number, segments in verse_segments(chapter).items():
            text = plain("".join(text for text, _, _ in segments))
            rows.append((tsv.verse_id(book.info.osis, chapter.number, number), chapter.number, number, text))
    return rows


def collection(selected):
    """(title, file stem) for a selection of Books."""
    key = tuple(book.info.osis for book in selected)
    if key in COLLECTIONS:
        title, stem = COLLECTIONS[key]
        return title, f"castellio-{stem}"
    if len(selected) == 1:
        return selected[0].long, f"castellio-{selected[0].slug}"
    return "Biblia Sacra", "castellio"


def credits(selected, macrons=True):
    """What every format prints in its colophon: licence, sources, the Wikisource pages and revisions used.
    `macrons=False`: for the editions without macrons, whose long vowels are not marked."""
    manifest = {row["book"]: row for row in tsv.read(MANIFEST)} if MANIFEST.exists() else {}
    pages = []
    for book in selected:
        row = manifest.get(book.info.osis)
        if row:
            pages.append((book.short, row["url"], row["revid"],
                          f"https://la.wikisource.org/w/index.php?oldid={row['revid']}", row["fetched"]))
    # All in Latin, as is everything in the books (Nathan, 2026-11-12): the PDF, EPUBs and text files.
    testaments = {book.info.testament for book in selected}
    bases = []
    if "novum" in testaments:
        bases.append("Novum Fœdus ēditiōnem sequitur Basileæ ā Pernā annō 1573 excūsam, “ex postrēmā recognitiōne”, "
                     "cum ultimā quam vīvus Castelliō ēdidit (Basileæ, 1556) collātam")
    if "vetus" in testaments:
        bases.append("Vetus Fœdus ēditiōnem " + ("" if bases else "sequitur ") + "Lipsiæ annō 1738 excūsam")
    # The Wikisource pages and revisions are listed on the site's colophon, a short address that prints on one line
    # (the MANIFEST.tsv address on GitHub did not).
    list_url = f"{SITE}colophon.html"
    list_lead = "Vicifontis pāginæ unde textus sūmptus est, cum numerō cujusque recēnsiōnis, hīc ēnumerantur:"
    source_lead = "Fontēs hujus ēditiōnis et tabulæ hīc reperiuntur; errōrēs, sī quōs dēprehenderis, hīc indicā:"
    return {
        "series": SERIES,
        "title": "Dē hāc ēditiōne",                # the colophon's heading (EPUB)
        # Fēlīcis Gaffiot: the surname undeclined beside a Latin first name (no attested *Gaffiotiānus*); ōrātiō rēcta
        # inter “ ” posita: the marks shown, not named (a no-break space between them, so they never part at a line's
        # end); versiculī: Bible verses, as distinct from versūs, lines of verse.
        "about": ("Sebastiānī Castelliōnis Biblia Latīna, Basileæ prīmum excūsa annō 1551, in ūsum legentium ēdita: "
                  "orthographia ad normam lexicī Fēlīcis Gaffiot (ēditiōnis annī 2016) redācta, "
                  # macron, -ī (n.): the Greek μακρόν as a loan word (Nathan, 2026-11-12)
                  + ("vōcālēs longæ omnēs macrō notātæ" if macrons else "vōcālēs longæ nūllō macrō notātæ")
                  + ", textus hodiernō mōre in paragraphōs distribūtus, carmina per versūs disposita, ōrātiō rēcta "
                  "inter “\u00a0” posita, versiculī ut in versiōne Anglicā quam Jācōbus rēx fierī jussit numerātī."),
        "bases": "; ".join(bases) + "." if bases else "",
        "editor": EDITOR,
        "edited": f"Ēdidit {EDITOR}.",
        "licence": ("Hæc ēditiō licentiā CC BY-SA 4.0 permittitur: eam dīvulgāre et mūtāre licet, dum auctōrēs "
                    "nōminentur et quidquid ex eā mūtātum fuerit eādem licentiā dīvulgētur. Textus ipse, sæculīs "
                    "XVI–XVIII excūsus, pūblicī jūris est."),
        "licence_url": "https://creativecommons.org/licenses/by-sa/4.0/",
        # The credit (2026-11-12, decision 54): Genesis 1–35 and the Gospels began as the editor's 2019 transcription,
        # which Latin Wikisource's pages of 2021 follow (their slips are his: docs/editions.md); the other books draw
        # on Wikisource (Vicifons, its Latin name), used under CC BY-SA 4.0. The page-by-page list is linked, not
        # printed, except on the site's colophon.
        # Genesis: the title declined as a Latin noun, genitive = nominative (the Vulgate's notes: in Genesi, super
        # Genesin); the Wikisource work's title quoted as it is, without macrons.
        "wikisource": ("Genesis capita 1–35 et Ēvangelia ipse ēditor annō 2019 trānscrīpsit. Cēterī librī sūmptī "
                       "sunt ex trānscrīptiōne quam Vicifontis sociī ab annō 2021 fēcērunt (Biblia Sacra interprete "
                       "Sebastiano Castellione), quæ eādem licentiā dīvulgātur et in Genesī atque Ēvangeliīs "
                       "ēditōris textum sequitur. Lēctiōnēs omnēs cum ēditiōnibus suprā nōminātīs collātæ sunt."),
        "wikisource_name": "Vicifontis",            # linked to wikisource_url on the site
        "wikisource_url": "https://la.wikisource.org/wiki/Biblia_Sacra_interprete_Sebastiano_Castellione",
        "wikisource_list_lead": list_lead,
        "wikisource_list": f"{list_lead} {list_url}",
        "wikisource_list_url": list_url,
        "pages": pages,
        "repository": REPOSITORY,
        "source_lead": source_lead,
        "source_note": f"{source_lead} {REPOSITORY}",
    }


# ---------------------------------------------------------------- plain text and data

# The citation abbreviations: the Nova Vulgata's (as the Vatican's Latin documents cite: "1Cor 10,17"), with j
# where this edition writes it (Jo, not Io), and Regum I–IV for Samuel and Kings, as Castellio names them.
CITATION = {
    "Gen": "Gn", "Exod": "Ex", "Lev": "Lv", "Num": "Nm", "Deut": "Dt", "Josh": "Jos", "Judg": "Jdc", "Ruth": "Rt",
    "1Sam": "1Reg", "2Sam": "2Reg", "1Kgs": "3Reg", "2Kgs": "4Reg", "1Chr": "1Par", "2Chr": "2Par", "Ezra": "Esd",
    "Neh": "Neh", "Esth": "Est", "Job": "Job", "Ps": "Ps", "Prov": "Prv", "Eccl": "Eccle", "Song": "Ct", "Isa": "Is",
    "Jer": "Jer", "Lam": "Lam", "Ezek": "Ez", "Dan": "Dn", "Hos": "Os", "Joel": "Joel", "Amos": "Am", "Obad": "Abd",
    "Jonah": "Jon", "Mic": "Mi", "Nah": "Na", "Hab": "Hab", "Zeph": "So", "Hag": "Agg", "Zech": "Zac", "Mal": "Mal",
    "Tob": "Tob", "Jdt": "Jdt", "Wis": "Sap", "Sir": "Sir", "Bar": "Bar", "1Macc": "1Mac", "2Macc": "2Mac",
    "Matt": "Mt", "Mark": "Mc", "Luke": "Lc", "John": "Jo", "Acts": "Act", "Rom": "Rom", "1Cor": "1Cor",
    "2Cor": "2Cor", "Gal": "Gal", "Eph": "Eph", "Phil": "Phil", "Col": "Col", "1Thess": "1Thess",
    "2Thess": "2Thess", "1Tim": "1Tim", "2Tim": "2Tim", "Titus": "Tit", "Phlm": "Philm", "Heb": "Hebr",
    "Jas": "Jac", "1Pet": "1Petr", "2Pet": "2Petr", "1John": "1Jo", "2John": "2Jo", "3John": "3Jo", "Jude": "Jud",
    "Rev": "Ap",
}


def cite(osis, chapter, first=None, last=None):
    """A reference in the Latin form: 'Mt 5', 'Mt 5,3', '2Cor 2,5–7' (number first, a comma before the verse)."""
    out = f"{CITATION.get(osis, osis)} {chapter}"
    if first not in (None, "", 0):
        out += f",{first}" + (f"–{last}" if last not in (None, "", 0, first) else "")
    return out


SUPERSCRIPT = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
SUPERSCRIPT_LETTERS = "ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ"


def note_letter(index, superscript=False):
    """A footnote's letter within its chapter: a, b, c … (superscript in the reading text: ᵃ, ᵇ …)."""
    letter = "abcdefghijklmnop"[index % 16]
    return SUPERSCRIPT_LETTERS[index % 16] if superscript else letter


def reading_text(book):
    """The book as plain reading text: paragraphs separated by blank lines, poetry lines indented, verse numbers
    as superscript digits, each chapter under "Caput <n>"."""
    out = [" ".join(line for line, _ in book.title).upper(), ""]
    for chapter in book.chapters:
        out.append(f"Caput {chapter.number}")
        out.append("")
        if chapter.title or chapter.summary:
            out += [chapter.title or chapter.summary, ""]
        lines, previous, notes = [], "", []
        for block in chapter.blocks:
            if block.kind == "b":                       # a stanza break
                lines.append("")
            else:
                poetry = block.kind.startswith("q")
                if lines and lines[-1] and not (poetry and previous.startswith("q")):
                    lines.append("")                    # a blank line between paragraphs, not between poetry lines
                pieces = []
                for kind, value in block.content:
                    if kind == "v":
                        pieces.append(str(value).translate(SUPERSCRIPT) if value > 1 else "")
                    elif kind == "text":
                        pieces.append(value)
                    elif kind == "note":                # a superscript letter here, the note at the chapter's end
                        notes.append(value)
                        pieces.append(note_letter(len(notes) - 1, superscript=True))
                text = plain("".join(pieces))
                lines.append("    " * int(block.kind[1]) + text if poetry else text)
            previous = block.kind
        if chapter.closing:
            lines += ["", chapter.closing]
        if notes:
            lines += [""] + [f"{note_letter(i)} {reference} {text}".replace("  ", " ")
                             for i, (reference, text) in enumerate(notes)]
        out += lines + [""]
    return "\n".join(out).rstrip() + "\n"


def write_text(selected, folder, stem, title):
    folder.mkdir(parents=True, exist_ok=True)
    info = credits(selected)
    head = "\n".join([SERIES.upper(), title, ""]) + "\n"
    body = "\n".join(reading_text(book) for book in selected)

    def tail(macrons):
        info = credits(selected, macrons)
        return "\n".join(["", "—" * 3, "", info["about"], info["bases"], info["edited"], "", info["licence"],
                          info["licence_url"], "", info["wikisource"], info["wikisource_list"], "",
                          info["source_note"], ""])

    full = head + body + tail(True)
    (folder / f"{stem}.txt").write_text(full, encoding="utf-8", newline="\n")
    (folder / f"{stem}-sine-macronibus.txt").write_text(strip_macrons(head + body + tail(False)), encoding="utf-8",
                                                        newline="\n")
    rows = [(vid, book.info.osis, c, v, text, strip_macrons(text))
            for book in selected for vid, c, v, text in verses(book)]
    tsv.write(folder / f"{stem}.tsv", rows, header=("id", "book", "chapter", "verse", "text", "sine_macronibus"))
    data = {"title": title, "series": SERIES, "licence": "CC BY-SA 4.0", "licence_url": info["licence_url"],
            "repository": REPOSITORY,
            "books": [{"osis": book.info.osis, "usfm": book.info.usfm, "title": book.long, "short": book.short,
                       "verses": [{"id": vid, "chapter": c, "verse": v, "text": text}
                                  for vid, c, v, text in verses(book)]} for book in selected]}
    (folder / f"{stem}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8",
                                         newline="\n")
    return [folder / f"{stem}{suffix}" for suffix in (".txt", "-sine-macronibus.txt", ".tsv", ".json")]


# ---------------------------------------------------------------- everything

def build(names=(), out=None, references=None, sources=None, version="", formats=("site", "epub", "pdf", "txt"),
          compile_pdf=True):
    """Generate the selected formats into build/ (or `out`). Returns {format: [paths or messages]}."""
    from pipeline import site
    out = out or BUILD
    selected = load(names)
    title, stem = collection(selected)
    stamp = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    made = {}
    for part in parts(selected, title, stem):
        for kind, items in build_downloads(part, out, formats, version, stamp, compile_pdf).items():
            made.setdefault(kind, []).extend(items)
    if "site" in formats:
        # the other formats built with it are offered on the site (build/site/downloads/)
        files = [item for kind in ("epub", "pdf", "txt") for item in made.get(kind, [])
                 if isinstance(item, pathlib.Path) and item.suffix in (".epub", ".pdf", ".txt", ".tsv", ".json")
                 and item.exists()]
        made["site"] = site.write(selected, out / "site", title, version,
                                   tuple(site.BY_REF) if references is None else references, sources, files,
                                   [(label, part_stem) for label, _, part_stem, _ in parts(selected, title, stem)])
    return made


TESTAMENTS = {"vetus": ("Old Testament", "Vetus Fœdus", "castellio-vetus-foedus"),
              "novum": ("New Testament", "Novum Fœdus", "castellio-novum-foedus")}


def parts(selected, title, stem):
    """The downloads built: [(label, title, stem, books)]: the selection itself, and when it holds books of both
    testaments, each testament on its own as well (Nathan, 2026-11-12)."""
    testaments = [key for key in TESTAMENTS if any(book.info.testament == key for book in selected)]
    if len(testaments) < 2:
        return [(None, title, stem, selected)]
    return [("Whole Bible", title, stem, selected)] + [
        (label, part_title, part_stem, [book for book in selected if book.info.testament == key])
        for key in testaments for label, part_title, part_stem in [TESTAMENTS[key]]]


def build_downloads(part, out, formats, version, stamp, compile_pdf):
    """The EPUBs, PDF and text files of one part: {format: [paths or messages]}."""
    from pipeline import epub, pdf
    _, title, stem, books = part
    made = {}
    if "txt" in formats:
        made["txt"] = write_text(books, out / "txt", stem, title)
    if "epub" in formats:
        made["epub"] = [epub.write(books, out / "epub" / f"{stem}.epub", title, version, stamp, macrons=True),
                        epub.write(books, out / "epub" / f"{stem}-sine-macronibus.epub", title, version, stamp,
                                   macrons=False)]
    if "pdf" in formats:
        made["pdf"] = pdf.write(books, out / "pdf", stem, title, version, compile_pdf)
    return made
