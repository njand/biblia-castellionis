"""Candidates for light notes in the Old Testament (data/review/ot-notes-process.md, proposed 2026-11-18).

`python -m pipeline notes BOOK` (an OT book) writes data/review/<book>-notes-candidates.md: places a note might be
wanted, each with its evidence, for a reader to check against the Hebrew and the NRSVue before any note is put to
Nathan. Castellio translated the Masoretic text, much as it is printed today, so the New Testament's test (his Greek
against a modern critical edition) has no counterpart. What can be found by a script:

- **versions**: the BSB's own footnotes that name an ancient version (LXX, the Samaritan Pentateuch, the Syriac, the
  Vulgate, the Dead Sea Scrolls, the Targums). Ranked `against MT` (the BSB's text follows a version, its note gives
  the Hebrew: Gen 4:8), `with MT` (the BSB keeps the Hebrew and gives a version's reading: Gen 10:24, where Castellio
  may follow the version himself) and `other` (a version cited without a Hebrew reading: Gen 5:24).
- **numbers**: a verse whose numerals differ between the Hebrew (the OSHB's lemmas) and Castellio's Latin. One is
  left out on both sides (*ūnus*, אֶחָד, often an article), and *prīmus* with it.
- **short**: a verse whose Latin is far shorter than its Hebrew, for the book (a clause he left out, Acts 4:5's kind).

Verses already noted (`\\f`) are left out. The book's Latin is the settled text, or its draft (text/draft/) before
it is settled. Nothing here is a proposal: Castellio's readings of the Hebrew (kind B) need a reader, chapter by
chapter."""

import re
import statistics
import unicodedata
import xml.etree.ElementTree as ET

from pipeline import books, gold, latex, parallel, paths, tsv

OSHB = paths.SOURCES / "parallel" / "oshb" / "files" / "morphhb-master" / "wlc"
BSB = paths.SOURCES / "parallel" / "bsb" / "files"
WEB = paths.SOURCES / "parallel" / "web" / "files"
OSIS_NS = "{http://www.bibletechnologies.net/2003/OSIS/namespace}"

# Strong's numbers of the Hebrew numerals → value (cardinals, ordinals, multiples, the tithe and the tenth part)
HEBREW_NUMBERS = {
    "8147": 2, "7969": 3, "702": 4, "2568": 5, "8337": 6, "7651": 7, "8083": 8, "8672": 9, "6235": 10, "6240": 10,
    "6242": 20, "7970": 30, "705": 40, "2572": 50, "8346": 60, "7657": 70, "8084": 80, "8673": 90, "3967": 100,
    "505": 1000, "7233": 10000, "7239": 10000, "7240": 10000,
    "8145": 2, "7992": 3, "7243": 4, "2549": 5, "8345": 6, "7637": 7, "8066": 8, "8671": 9, "6224": 10,
    "7659": 7, "4643": 10, "6237": 10, "6241": 10,
}
DUAL = {"3967", "505"}                  # מָאתַיִם, אַלְפַּיִם: 200 and 2000 in one word

LATIN_NUMBERS = {
    "duo": {2}, "duae": {2}, "duos": {2}, "duas": {2}, "duorum": {2}, "duarum": {2}, "duobus": {2}, "duabus": {2},
    "ambo": {2}, "ambae": {2}, "ambos": {2}, "ambas": {2}, "amborum": {2}, "ambarum": {2}, "ambobus": {2},
    "ambabus": {2}, "tres": {3}, "tria": {3}, "trium": {3}, "tribus": {3}, "quattuor": {4}, "quinque": {5},
    "sex": {6}, "septem": {7}, "octo": {8}, "novem": {9}, "decem": {10}, "undecim": {10}, "duodecim": {2, 10},
    "tredecim": {3, 10}, "quattuordecim": {4, 10}, "quindecim": {5, 10}, "sedecim": {6, 10}, "septendecim": {7, 10},
    "duodeviginti": {8, 10}, "undeviginti": {9, 10}, "viginti": {20}, "triginta": {30}, "quadraginta": {40},
    "quinquaginta": {50}, "sexaginta": {60}, "septuaginta": {70}, "octoginta": {80}, "nonaginta": {90},
    "centum": {100}, "mille": {1000}, "bis": {2}, "ter": {3}, "quater": {4}, "quinquies": {5}, "sexies": {6},
    "septies": {7}, "octies": {8}, "novies": {9}, "decies": {10}, "centies": {100}, "millies": {1000},
}
LATIN_STEMS = [                         # (stem, endings, values): hundreds, thousands, ordinals, distributives
    ("ducent", "i ae a os as orum arum is", {2, 100}), ("trecent", "i ae a os as orum arum is", {3, 100}),
    ("quadringent", "i ae a os as orum arum is", {4, 100}), ("quingent", "i ae a os as orum arum is", {5, 100}),
    ("sescent", "i ae a os as orum arum is", {6, 100}), ("sexcent", "i ae a os as orum arum is", {6, 100}),
    ("septingent", "i ae a os as orum arum is", {7, 100}), ("octingent", "i ae a os as orum arum is", {8, 100}),
    ("nongent", "i ae a os as orum arum is", {9, 100}),
    ("mil", "ia ium ibus", {1000}), ("mill", "ia ium ibus", {1000}),
]
ORDINAL = "us a um o am i ae os as is orum arum"
DISTRIBUTIVE = "i ae a os as is orum arum um"
LATIN_STEMS += [(stem, ORDINAL, values) for stem, values in (
    ("secund", {2}), ("terti", {3}), ("quart", {4}), ("quint", {5}), ("sext", {6}), ("septim", {7}),
    ("octav", {8}), ("non", {9}), ("decim", {10}), ("vicesim", {20}), ("tricesim", {30}), ("quadragesim", {40}),
    ("quinquagesim", {50}), ("sexagesim", {60}), ("septuagesim", {70}), ("octogesim", {80}), ("nonagesim", {90}),
    ("centesim", {100}), ("ducentesim", {2, 100}), ("trecentesim", {3, 100}), ("millesim", {1000}),
    ("quinquagenari", {50}), ("sexagenari", {60}), ("septuagenari", {70}), ("octogenari", {80}),
    ("nonagenari", {90}), ("centenari", {100}), ("millenari", {1000}), ("undecim", {10}),
    ("duodecim", {2, 10}))]
HUNDREDS = {"ducent": 2, "trecent": 3, "quadringent": 4, "quingent": 5, "sescent": 6, "sexcent": 6, "septingent": 7,
            "octingent": 8, "nongent": 9}
LATIN_STEMS += [(stem + suffix, ORDINAL, {n, 100}) for stem, n in HUNDREDS.items() for suffix in ("esim", "enari")]
MULTIPLES = {"dupl": {2}, "tripl": {3}, "quadrupl": {4}, "quintupl": {5}, "septupl": {7}, "septuagecupl": {70},
             "centupl": {100}}
TENS = {"viginti": 20, "triginta": 30, "quadraginta": 40, "quinquaginta": 50, "sexaginta": 60, "septuaginta": 70,
        "octoginta": 80, "nonaginta": 90}
for tens, value in TENS.items():        # *duodēquadrāgintā* 38 = 8 and 30, as the Hebrew counts it
    LATIN_NUMBERS["duode" + tens] = {8, value - 10}
    LATIN_NUMBERS["unde" + tens] = {9, value - 10}
LATIN_NUMBERS.update({"septemdecim": {7, 10}, "octodecim": {8, 10}, "novemdecim": {9, 10}})
LATIN_STEMS += [(stem, DISTRIBUTIVE, values) for stem, values in (
    ("bin", {2}), ("tern", {3}), ("trin", {3}), ("quatern", {4}), ("septen", {7}), ("octon", {8}),
    ("noven", {9}), ("den", {10}), ("vicen", {20}), ("tricen", {30}), ("quadragen", {40}), ("quinquagen", {50}),
    ("sexagen", {60}), ("centen", {100}), ("ducen", {2, 100}), ("trecen", {3, 100}), ("quingen", {5, 100}),
    ("quinden", {5, 10}), ("duoden", {2, 10}), ("sen", {6}), ("tricenari", {30}), ("vicenari", {20}),
    ("quadragenari", {40}))]
LATIN_STEMS += [("decum", "a ae am as is", {10})]       # the tithe, as Castellio spells it
LATIN_FORMS = dict(LATIN_NUMBERS)
for stem, endings, values in LATIN_STEMS:
    for ending in endings.split():
        LATIN_FORMS.setdefault(stem + ending, values)
for word in ("tribus",                                  # tribes as often as three (MAY_COUNT)
             "senis", "seni", "sena",                   # *senex*, *senis*; *Sēna*
             "secundum", "secundus", "secundo",         # "according to"; *Deō secundō*, *secundus aderō*: favour
             "nonae"):                                  # *nōnæ*, a date
    LATIN_FORMS.pop(word, None)
SECOND = {"secundus", "secundo"}                        # second only after a number (latin_numbers)
MAY_COUNT = {"alter": {2}, "par": {2}, "uterque": {2}, "utrumque": {2}, "utraque": {2}, "biduum": {2},
             "bienni": {2}, "tridu": {3}, "trienni": {3}, "septenni": {7}, "septennari": {7}, "tribus": {3}}

VERSIONS = re.compile(r"\b(LXX|SP|Samaritan|Syriac|Vulgate|DSS|Dead Sea Scrolls|Targums?|Aramaic Targum)\b")
SHORT_RATIO = 0.5                       # Latin/Hebrew words below half the book's median ratio
SHORT_MIN = 8                           # and at least this many Hebrew words
WINDOW_RATIO = 0.75                     # and the verse with its neighbours below three quarters of it


def plain(text):
    text = text.lower().replace("æ", "ae").replace("œ", "oe").replace("j", "i")
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def latin_numbers(text):
    """The values of the numerals in a Latin verse (a set; one and first left out)."""
    out, previous = set(), set()
    for figure in re.findall(r"\d+", text):        # Numbers' census in figures: *mīlitēs 46500*
        out |= figure_values(int(figure))
    for word in re.findall(r"[a-z]+", plain(text)):
        values = LATIN_FORMS.get(word, set()) | next((v for s, v in MULTIPLES.items() if word.startswith(s)), set())
        if word in SECOND and previous:             # *sexāgēsimō secundō*: second after a number
            values = {2}
        out |= values
        previous = values
    return out


def figure_values(n):
    """A number in figures as the Hebrew words for it count (46500: six and forty thousand and five hundred →
    {6, 40, 1000, 5, 100}); one, and the two of 200 and 2000, as `hebrew_numbers` counts them."""
    if n >= 1000:
        thousands = n // 1000
        return figure_values(thousands) | ({2} if thousands == 2 else set()) | {1000} | figure_values(n % 1000)
    out = set()
    hundreds, rest = divmod(n, 100)
    if hundreds:
        out |= {100} | ({hundreds} if hundreds > 1 else set())
    tens, units = divmod(rest, 10)
    if tens == 1:
        out.add(10)
    elif tens:
        out.add(tens * 10)
    if units > 1:
        out.add(units)
    return out


def latin_may_count(text):
    """Values a Latin verse may express without a numeral (*alter* for the second, *paria*, *trīduum*), and whether
    it has *totidem*, "as many": a Hebrew number missing from the Latin is then no candidate."""
    words = re.findall(r"[a-z]+", plain(text))
    out = set()
    for word in words:
        out |= next((v for s, v in MAY_COUNT.items() if word.startswith(s)), set())
    return out, "totidem" in words


def hebrew(osis):
    """{kjv id: [(lemma, morph)]} for one book, from the OSHB (numbered as the WLC, moved to the KJV's numbering by
    data/versification/wlc.map.tsv); None when the book is not at hand or its numbering is unchecked."""
    path = OSHB / f"{osis}.xml"
    if not path.exists():
        return None
    rows = []
    for verse in ET.parse(path).iter(f"{OSIS_NS}verse"):
        words = [(w.get("lemma", ""), w.get("morph", "")) for w in verse.iter(f"{OSIS_NS}w")]
        rows.append((verse.get("osisID"), words))
    found = parallel.realign("wlc", osis, rows, join=lambda a, b: a + b)
    return found[0] if found else None


def hebrew_numbers(words):
    """The values of the numerals in a Hebrew verse (a set; אֶחָד and רִאשׁוֹן left out, as on the Latin side)."""
    out = set()
    for lemma, morph in words:
        strong = re.sub(r"[^0-9]", "", lemma.rsplit("/", 1)[-1].split()[0]) if lemma else ""
        if strong in HEBREW_NUMBERS:
            out.add(HEBREW_NUMBERS[strong])
            last = morph.split("/")[-1] if "/" in morph else morph[1:]     # HAcbda, HC/Acbda → Acbda
            if strong in DUAL and len(last) > 3 and last[:2] == "Ac" and last[3] == "d":   # dual
                out.add(2)
    return out


def footnotes(folder, usfm, pattern):
    """{kjv id: [note]} from a translation's USFM: its footnotes that name an ancient version."""
    files = sorted(folder.glob(f"*{usfm}*.usfm"))
    if not files:
        return {}
    text = files[0].read_text(encoding="utf-8")
    book = next(b for b in books.BOOKS if b.usfm == usfm)
    out = {}
    for m in re.finditer(r"\\f \+ \\fr (\d+)[:.](\d+)\S* \\ft (.*?)\\f\*", text, re.S):
        body = " ".join(re.sub(r"\\\+?[a-z]+\d?\*? ?", "", m.group(3)).split())
        if pattern.search(body):
            out.setdefault(tsv.verse_id(book.osis, int(m.group(1)), int(m.group(2))), []).append(body)
    return out


def version_rank(note):
    """against MT, with MT or other, for a BSB note naming a version (see the module's docstring)."""
    first, _, rest = note.partition(";")
    if re.search(r"\b(MT|Hebrew)\b", first) and not VERSIONS.search(first):
        return "with MT"
    if rest and re.search(r"\b(MT|Hebrew)\b", rest) or re.search(r"\bMT\b", note):
        return "against MT"
    return "other"


def latin_text(book):
    """{vid: text}: the settled verses, then the draft's for chapters not yet settled; and where they come from."""
    out, source = {vid: row["text"] for vid, row in gold.load(book.osis).items()}, "settled"
    draft = paths.ROOT / "text" / "draft" / f"{book.usfm}.usfm"
    if draft.exists():
        for vid, text, *_ in gold.rows(draft.read_text(encoding="utf-8"), book.osis):
            out.setdefault(vid, text)
        source = "settled and draft" if out else "draft"
    return out, source


def noted_verses(book):
    out = set()
    for path in (latex.usfm_path(book), paths.ROOT / "text" / "draft" / f"{book.usfm}.usfm"):
        if path.exists():
            for c, v in re.findall(r"\\f \+ \\fr (\d+):(\d+)", path.read_text(encoding="utf-8")):
                out.add(tsv.verse_id(book.osis, int(c), int(v)))
    return out


MARK = re.compile(r"(?:^|(?<=[\s,.;:(*|!>]))(?:G\.\s?L[.,:]?|G\.L\.|G[.\\]|Gr\.\s?lect\.?)(?=[\s)]|$|[A-Za-z])")
MARK_PRINTINGS = ("1738", "1750")       # the raw OCR in sources/archive/<year>/text.txt (1738's OCR may read G. as G\)
MARK_MIN = 3                            # shared word pairs for a mark to be placed in a verse


def ocr_words(text):
    """Words for matching OCR to the text: long s read as f, u for v, letters only."""
    return re.findall(r"[a-z]{3,}", plain(text).replace("ſ", "s").replace("f", "s").replace("v", "u"))


def marks(osis, latin=None, printings=MARK_PRINTINGS):
    """{vid: [(printing, OCR lines)]}: Castellio's *G.* (*G.L.*, 1750 *Gr. lect.*) … *H.* marks around readings he
    took from the Greek, found in each printing's raw OCR and placed in the verse that shares most word pairs with
    the lines around them (the OCR is not aligned beyond Gen 27)."""
    book = books.select([osis])[0]
    if latin is None:
        latin, _ = latin_text(book)
    orig_path = paths.ROOT / "text" / "orig" / f"{book.usfm}.usfm"
    texts = dict(latin)
    if orig_path.exists():
        for vid, text, *_ in gold.rows(orig_path.read_text(encoding="utf-8"), book.osis):
            texts[vid] = texts.get(vid, "") + " " + text
    pairs = {}
    for vid, text in texts.items():
        words = ocr_words(text)
        for pair in zip(words, words[1:]):
            pairs.setdefault(pair, set()).add(vid)
    out = {}
    for printing in printings:
        path = paths.SOURCES / "archive" / printing / "text.txt"
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        for i, line in enumerate(lines):
            if not MARK.search(line):
                continue
            context = " ".join(lines[max(0, i - 1):i + 3])
            words = ocr_words(context)
            score = {}
            for pair in set(zip(words, words[1:])):
                for vid in pairs.get(pair, ()):
                    score[vid] = score.get(vid, 0) + 1
            if score:
                vid = max(score, key=lambda v: (score[v], -len(texts[v])))
                if score[vid] >= MARK_MIN:
                    out.setdefault(vid, []).append((printing, " / ".join(l.strip() for l in lines[i:i + 2])))
    return out


def candidates(osis):
    """{"versions": {vid: [(rank, note)]}, "web": {vid: [note]}, "numbers": {vid: (hebrew, latin)},
    "short": {vid: (latin words, hebrew words)}, "marks": {vid: [(printing, lines)]}} and counts, for one Old
    Testament book. Marks are listed even in verses already noted."""
    book = books.select([osis])[0]
    latin, source = latin_text(book)
    skip = noted_verses(book)
    heb = hebrew(book.osis) or {}
    found = {"versions": {}, "web": {}, "numbers": {}, "short": {}}
    for vid, notes in footnotes(BSB, book.usfm, VERSIONS).items():
        if vid in latin and vid not in skip:
            found["versions"][vid] = [(version_rank(n), n) for n in notes]
    for vid, notes in footnotes(WEB, book.usfm, re.compile(VERSIONS.pattern + r"|\bHebrew (manuscripts|text)\b"))\
            .items():
        if vid in latin and vid not in skip and vid not in found["versions"]:
            found["web"][vid] = notes
    ratios = {}
    for vid, text in latin.items():
        words = heb.get(vid)
        if not words or vid in skip:
            continue
        h, l = hebrew_numbers(words), latin_numbers(text)
        may, as_many = latin_may_count(text)
        missing = set() if as_many else h - l - may
        if missing or l - h:
            found["numbers"][vid] = (h, l)
        latin_words = len(re.findall(r"[^\W\d_]+", text)) + sum(len(figure_values(int(n)))
                                                                 for n in re.findall(r"\d+", text))
        ratios[vid] = (latin_words, sum(1 for lemma, _ in words if lemma.rsplit("/", 1)[-1].strip() != "853"))   # not אֵת
    usable = [l / h for l, h in ratios.values() if h >= SHORT_MIN]
    if usable:
        median = statistics.median(usable)
        order = sorted(ratios, key=tsv.parse_id)
        for i, vid in enumerate(order):
            l, h = ratios[vid]
            # the verse with its neighbours: Castellio often carries words into the next verse (Gen 2:22, 11:27)
            window = [ratios[order[j]] for j in range(max(0, i - 1), min(len(order), i + 2))]
            wl, wh = sum(x for x, _ in window), sum(y for _, y in window)
            if h >= SHORT_MIN and l / h < SHORT_RATIO * median and wl / wh < WINDOW_RATIO * median:
                found["short"][vid] = (l, h)
    found["marks"] = marks(book.osis, latin)
    counts = {"verses": len(latin), "source": source, "hebrew": bool(heb), "noted": len(skip & set(latin))}
    return found, counts


def report(osis):
    book = books.select([osis])[0]
    found, counts = candidates(book.osis)
    latin, _ = latin_text(book)
    orig_path = paths.ROOT / "text" / "orig" / f"{book.usfm}.usfm"
    printed = ({vid: text for vid, text, *_ in gold.rows(orig_path.read_text(encoding="utf-8"), book.osis)}
               if orig_path.exists() else {})
    texts = {key: (parallel.aligned(key, book.osis) or ({}, {}))[0]
             for key in ("wlc", "vulgate", "lxx", "bsb", "kjv")}

    def ref(vid):
        _, c, v = tsv.parse_id(vid)
        return f"{c}:{v}"

    def evidence(vid):
        rows = [("Latin", latin.get(vid, "")), ("1738", printed.get(vid, "")), ("WLC", texts["wlc"].get(vid, "")),
                ("Vulgate", texts["vulgate"].get(vid, "")), ("LXX", texts["lxx"].get(vid, "")),
                ("BSB", texts["bsb"].get(vid, "")), ("KJV", texts["kjv"].get(vid, ""))]
        return [f"   - {name}: {text}" for name, text in rows if text]

    def values(s):
        return ", ".join(str(n) for n in sorted(s)) or "none"

    order = ("against MT", "with MT", "other")
    out = [f"# {book.osis}: candidates for light notes",
           "",
           f"Built by `python -m pipeline notes {book.osis}` (pipeline/otnotes.py); the process and its decisions are in",
           "`data/review/ot-notes-process.md`. These are not proposals: each is read against the Hebrew and the NRSVue",
           f"before a note is put to Nathan in `{book.osis.lower()}-notes.md`.",
           "",
           f"Latin: {counts['verses']} verses ({counts['source']}); already noted: {counts['noted']}. "
           f"BSB notes naming a version: {len(found['versions'])} verses ("
           + ", ".join(f"{k} {sum(1 for ns in found['versions'].values() if min(order.index(r) for r, _ in ns) == i)}"
                       for i, k in enumerate(order))
           + f"); WEB notes besides: {len(found['web'])}. Numerals differing from the Hebrew: "
           f"{len(found['numbers'])}. Latin far shorter than the Hebrew: {len(found['short'])}. "
           f"Castellio's G. … H. marks: {len(found['marks'])}."
           + ("" if counts["hebrew"] else " **The OSHB's Hebrew is not at hand or its numbering is unchecked: no "
                                         "numbers or lengths.**"),
           ""]
    if found["marks"]:
        out += [f"## Castellio's marks ({len(found['marks'])} verses)", "",
                "*G.* (*G.L.*, 1750 *Gr. lect.*) … *H.*: a reading he took from the Greek, found in the raw OCR of 1738 "
                "and 1750 and placed by the words around it (check the verse).", ""]
        for vid, hits in sorted(found["marks"].items(), key=lambda x: tsv.parse_id(x[0])):
            out.append(f"- **{ref(vid)}** " + " | ".join(f"{p}: {lines}" for p, lines in hits))
            out += evidence(vid)
        out.append("")
    for i, rank in enumerate(order):
        verses = [(vid, ns) for vid, ns in sorted(found["versions"].items(), key=lambda x: tsv.parse_id(x[0]))
                  if min(order.index(r) for r, _ in ns) == i]
        if verses:
            out += [f"## Versions: the BSB {rank} ({len(verses)} verses)", ""]
            for vid, ns in verses:
                out.append(f"- **{ref(vid)}** " + " | ".join(f"BSB: {n}" for _, n in ns))
                out += evidence(vid)
            out.append("")
    if found["web"]:
        out += [f"## Versions: the WEB's notes ({len(found['web'])} verses)", ""]
        for vid, ns in sorted(found["web"].items(), key=lambda x: tsv.parse_id(x[0])):
            out.append(f"- **{ref(vid)}** " + " | ".join(f"WEB: {n}" for n in ns))
            out += evidence(vid)
        out.append("")
    if found["numbers"]:
        out += [f"## Numbers ({len(found['numbers'])} verses)", "",
                "Values of the numerals (one and first left out); a word may stand for a number on one side only "
                "(*bīnī*, a week, a tithe), so most are nothing.", ""]
        for vid, (h, l) in sorted(found["numbers"].items(), key=lambda x: tsv.parse_id(x[0])):
            out.append(f"- **{ref(vid)}** Hebrew {values(h)}; Latin {values(l)}")
            out += evidence(vid)
        out.append("")
    if found["short"]:
        out += [f"## Short ({len(found['short'])} verses)", "",
                f"Latin words against Hebrew words, below {SHORT_RATIO:g} of the book's median ratio.", ""]
        for vid, (l, h) in sorted(found["short"].items(), key=lambda x: tsv.parse_id(x[0])):
            out.append(f"- **{ref(vid)}** {l} Latin words, {h} Hebrew")
            out += evidence(vid)
        out.append("")
    return "\n".join(out)


def write(osis):
    book = books.select([osis])[0]
    path = paths.DATA / "review" / f"{book.osis.lower()}-notes-candidates.md"
    path.write_text(report(book.osis), encoding="utf-8", newline="\n")
    return path
