"""The books of Castellio's Bible: identifiers and names used by each source.

ids follow OSIS (`Matt.14.3`); `usfm` is the code used by the USFM parallel texts. `ws` is the subpage of
la.wikisource's *Biblia Sacra interprete Sebastiano Castellione* (None where none exists yet, as of 2026-11).
`wp` is the 2019 WordPress site's slug. `slug` is the file name this repo uses in LaTeX/ and TXT/.
Castellio follows the Vulgate's naming: Regum I–IV are 1–2 Samuel and 1–2 Kings."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    osis: str
    usfm: str
    slug: str
    ws: str | None
    testament: str           # "vetus" or "novum"
    wp: str | None = None
    apocrypha: bool = False


def _ot(osis, usfm, slug, ws, wp=None):
    return Book(osis, usfm, slug, ws, "vetus", wp)


def _ap(osis, usfm, slug, ws):
    return Book(osis, usfm, slug, ws, "vetus", apocrypha=True)


def _nt(osis, usfm, slug, ws, wp=None):
    return Book(osis, usfm, slug, ws, "novum", wp)


BOOKS = [
    _ot("Gen", "GEN", "genesis", "Genesis", "genesis"),
    _ot("Exod", "EXO", "exodus", "Exodus"),
    _ot("Lev", "LEV", "leviticus", "Leviticus"),
    _ot("Num", "NUM", "numeri", "Numeri"),
    _ot("Deut", "DEU", "deuteronomium", "Deuteronomium"),
    _ot("Josh", "JOS", "josua", "Josua"),
    _ot("Judg", "JDG", "judices", "Judices"),
    _ot("Ruth", "RUT", "rutha", "Rutha"),
    _ot("1Sam", "1SA", "regum liber 1", "Regum liber I"),
    _ot("2Sam", "2SA", "regum liber 2", None),
    _ot("1Kgs", "1KI", "regum liber 3", None),
    _ot("2Kgs", "2KI", "regum liber 4", None),
    _ot("1Chr", "1CH", "paralipomenon liber 1", "Paralipomenon liber I"),
    _ot("2Chr", "2CH", "paralipomenon liber 2", None),
    _ot("Ezra", "EZR", "esdras", None),
    _ot("Neh", "NEH", "nehemias", None),
    _ot("Esth", "EST", "estera", "Estera"),
    _ot("Job", "JOB", "jobus", "Jobus"),
    _ot("Ps", "PSA", "psalterium", "Psalterium"),
    _ot("Prov", "PRO", "proverbia", None),
    _ot("Eccl", "ECC", "ecclesiastes", "Ecclesiastes"),
    _ot("Song", "SNG", "canticum canticorum", "Canticum canticorum"),
    _ot("Isa", "ISA", "esaias", "Esaias"),
    _ot("Jer", "JER", "jeremias", "Jeremias"),
    _ot("Lam", "LAM", "jeremiae lamentationes", "Jeremiae lamentationes"),
    _ot("Ezek", "EZK", "ezechiel", None),
    _ot("Dan", "DAN", "daniel", None),
    _ot("Hos", "HOS", "osea", "Osea"),
    _ot("Joel", "JOL", "joel", "Joel"),
    _ot("Amos", "AMO", "amos", None),
    _ot("Obad", "OBA", "abdias", "Abdias"),
    _ot("Jonah", "JON", "jonas", "Jonas"),
    _ot("Mic", "MIC", "michaeas", None),
    _ot("Nah", "NAM", "nahumus", "Nahumus"),
    _ot("Hab", "HAB", "habacucus", "Habacucus"),
    _ot("Zeph", "ZEP", "sophonias", "Sophonias"),
    _ot("Hag", "HAG", "haggaeus", "Haggaeus"),
    _ot("Zech", "ZEC", "zacharias", None),
    _ot("Mal", "MAL", "malachias", "Malachias"),
    _ap("Tob", "TOB", "tobias", "Tobias"),
    _ap("Jdt", "JDT", "juditha", "Juditha"),
    _ap("Wis", "WIS", "sapientia", "Sapientia"),
    _ap("Sir", "SIR", "ecclesiasticus", None),
    _ap("Bar", "BAR", "baruchus", None),
    _ap("1Macc", "1MA", "machabaeorum liber 1", None),
    _ap("2Macc", "2MA", "machabaeorum liber 2", None),
    _nt("Matt", "MAT", "matthaeus", "Evangelium auctore Matthaeo", "matthaeus"),
    _nt("Mark", "MRK", "marcus", "Evangelium auctore Marco", "marcus"),
    _nt("Luke", "LUK", "lucas", "Evangelium auctore Luca", "lucas"),
    _nt("John", "JHN", "johannes", "Evangelium auctore Joanne", "johannes"),
    _nt("Acts", "ACT", "acta", "Acta apostolorum"),
    _nt("Rom", "ROM", "ad romanos", "Pauli epistola ad Romanos"),
    _nt("1Cor", "1CO", "ad corinthios i", "Pauli epistola I ad Corinthios"),
    _nt("2Cor", "2CO", "ad corinthios ii", "Pauli epistola II ad Corinthios"),
    _nt("Gal", "GAL", "ad galatas", "Pauli epistola ad Galatas"),
    _nt("Eph", "EPH", "ad ephesios", "Pauli epistola ad Ephesios"),
    _nt("Phil", "PHP", "ad philippenses", "Pauli epistola ad Philippenses"),
    _nt("Col", "COL", "ad colossenses", "Pauli epistola ad Colossenses"),
    _nt("1Thess", "1TH", "ad thessalonicenses i", "Pauli epistola I ad Thessalonicenses"),
    _nt("2Thess", "2TH", "ad thessalonicenses ii", "Pauli epistola II ad Thessalonicenses"),
    _nt("1Tim", "1TI", "ad timotheum i", "Pauli epistola I ad Timotheum"),
    _nt("2Tim", "2TI", "ad timotheum ii", "Pauli epistola II ad Timotheum"),
    _nt("Titus", "TIT", "ad titum", "Pauli epistola ad Titum"),
    _nt("Phlm", "PHM", "ad philemonem", "Pauli epistola ad Philemonem"),
    _nt("Heb", "HEB", "ad hebraeos", "Epistola ad Hebraeos"),
    _nt("Jas", "JAS", "jacobus", "Jacobi epistola"),
    _nt("1Pet", "1PE", "petrus i", "Petri epistola I"),
    _nt("2Pet", "2PE", "petrus ii", "Petri epistola II"),
    _nt("1John", "1JN", "johannes i", "Joannis epistola I"),
    _nt("2John", "2JN", "johannes ii", "Joannis epistola II"),
    _nt("3John", "3JN", "johannes iii", "Joannis epistola III"),
    _nt("Jude", "JUD", "juda", "Judae epistola"),
    _nt("Rev", "REV", "apocalypsis", "Apocalypsis"),
]

BY_OSIS = {book.osis: book for book in BOOKS}
BY_USFM = {book.usfm: book for book in BOOKS}
BY_SLUG = {book.slug: book for book in BOOKS}


def select(names):
    """Books named by OSIS code or slug (case-insensitive); all books if `names` is empty."""
    if not names:
        return list(BOOKS)
    lookup = {key.lower(): book for book in BOOKS for key in (book.osis, book.slug)}
    try:
        return [lookup[name.lower()] for name in names]
    except KeyError as error:
        raise SystemExit(f"unknown book {error.args[0]!r}; use an OSIS code (e.g. Matt) or slug (e.g. matthaeus)")
