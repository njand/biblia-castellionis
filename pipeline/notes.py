"""Candidates for light notes in the New Testament (data/review/nt-notes-process.md, decided 2026-11-16).

`python -m pipeline notes BOOK` writes data/review/<book>-notes-candidates.md: the places a note might be wanted, each
with its evidence, for Claude to read (with the NET notes and the NRSVue) before proposing any note to Nathan.

Two kinds are found here:

- **text**: the SBLGNT apparatus's units where the critical editions agree (SBLGNT with WH and NA28; Tregelles either
  way, Nathan 2026-11-16 on the Mark pilot) against the Byzantine text (RP), and the TR, the Greek Castellio translated, has RP's reading. Word order, articles, another
  form of the same word and swaps of small words (conjunctions, particles, prepositions, pronouns) are left out:
  notes on the text are kept to changes of sense (decision of 2026-11-16, 2: C). Each is ranked: `clause` (three words
  or more added or left out), `name`, `number`, `word`.
- **person**: a verse whose Latin has *nōs*/*noster* where the TR has only ὑμ- (or *vōs*/*vester* where it has only
  ἡμ-), as at 1 John 4:4.

Verses already noted (`\\f`) or bracketed are left out. Nothing here is a proposal: the sense-divergences (Castellio
reading the Greek otherwise than scholars now do) need a reader, and the review file is written by hand from this."""

import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import books, gold, latex, parallel, paths, tsv

APPARATUS = paths.SOURCES / "parallel" / "sblgnt" / "files" / "SBLGNT-master" / "data" / "sblgntapp" / "text"
SBLGNT = paths.SOURCES / "parallel" / "sblgnt" / "files" / "SBLGNT-master" / "data" / "sblgnt" / "text"
CONSENSUS = {"WH", "NA28"}             # Tregelles either way (9:29, 10:24 … in Mark, Nathan 2026-11-16)
EDITION = re.compile(r"^[A-Z][A-Za-z0-9]*$")

ARTICLES = set("ο η το του της τον την τω τη οι αι τα των τοις ταις τους τας".split())
SMALL = ARTICLES | set("""και δε ουν γαρ τε αλλα αλλ ουδε μηδε ητοι η ει εαν αν οτι ως ωσπερ καθως ουτως ωσει
    τοτε ευθυς ευθεως νυν ιδου ου ουκ ουχ μη ουχι αμην δη μεν γε
    εν εις εκ εξ απο επι προς δια μετα μετ παρα περι υπο υπερ κατα συν αχρι μεχρι εως εμπροσθεν ενωπιον
    αυτος αυτου αυτω αυτον αυτοι αυτων αυτοις αυτους αυτη αυτης αυτην αυται αυτο αυτα
    μου μοι με εμου εμοι εμε σου σοι σε ημων ημιν ημας ημεις υμων υμιν υμας υμεις
    ουτος τουτο τουτου τουτω τουτον ταυτα τουτων εκεινος εκεινου εκεινω εκεινον εκεινη εκεινα τις τι""".split())
NUMBERS = ("εις", "μια", "εν", "δυο", "τρει", "τρι", "τεσσ", "τεσσαρ", "πεντ", "εξ", "επτ", "οκτω", "εννε", "δεκ",
           "δωδεκ", "εικοσ", "τριακ", "τεσσερακ", "πεντηκ", "εκατ", "διακοσ", "τριακοσ", "χιλι", "μυρι")
NUMBER_WORDS = re.compile(r"^(δυο|τρει|τρια|τρι[ωσ]|τεσσ|πεντ|επτα|οκτω|εννε|δεκα|δωδεκ|εικοσ|τριακοντ|τεσσερακ|"
                          r"πεντηκ|εκατ|διακοσ|τριακοσ|χιλι|μυρι)")
LATIN_WE = re.compile(r"\b(nōs|nōbīs|nostr\w*|noster)\b", re.I)
LATIN_YOU = re.compile(r"\b(vōs|vōbīs|vestr\w*|vester)\b", re.I)


def plain(text):
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn").lower()


def greek_words(text):
    return re.findall(r"[^\W\d_]+", plain(text))


@dataclass
class Unit:
    vid: str
    reading: str                    # the critical editions' (SBLGNT's) reading; "–" for none
    rp: str                         # RP's reading; "+ …" an addition, "–" none
    line: str                       # the apparatus line as printed
    kind: str = ""                  # add, omit, substitute
    rank: str = ""                  # clause, name, number, word
    loose: bool = False             # WH and NA28 with SBLGNT, but Tregelles with RP
    words: list = field(default_factory=list)


def apparatus(osis):
    """[Unit] for one book: each place where WH and NA28 stand with SBLGNT against RP. `loose` marks those where
    Tregelles sides with RP, reported apart."""
    path = APPARATUS / f"{osis}.txt"
    if not path.exists():
        return []
    units, vid = [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip().lstrip("﻿")
        ref = re.match(r"^(.+) (\d+):(\d+)$", line)
        if ref:
            vid = tsv.verse_id(osis, int(ref.group(2)), int(ref.group(3)))
            continue
        if "]" not in line or vid is None:
            continue
        unit = re.sub(r"^(\d+:\d+|\d+|•)\s*", "", line)
        left, right = unit.split("]", 1)
        eds = {w for w in left.split() if EDITION.match(w)}
        rp = next((alt.strip() for alt in right.split(";") if re.search(r"\bRP\b", alt)), None)
        if rp is None:
            continue
        if not CONSENSUS <= eds:
            continue
        loose = bool(re.search(r"\bTreg\b", rp))
        units.append(Unit(vid, " ".join(w for w in left.split() if w not in eds),
                          " ".join(w for w in rp.split() if not EDITION.match(w)), line, loose=loose))
    return units


_NAMES = None


def proper_names():
    """Plain forms the SBLGNT always capitalizes, never writes in lower case: names, not sentence or speech openings."""
    global _NAMES
    if _NAMES is None:
        upper, lower = set(), set()
        for path in SBLGNT.glob("*.txt"):
            for line in path.read_text(encoding="utf-8").splitlines():
                for word in re.findall(r"[^\W\d_]+", line.split("\t", 1)[-1]):
                    (upper if word[:1].isupper() else lower).add(plain(word))
        _NAMES = upper - lower
    return _NAMES


TRIVIAL_NAMES = {"ιησους", "ιησου", "ιησουν", "ιησοι"}     # "Jesus" supplied as subject: the Latin supplies it too


def classify(unit):
    """Set the unit's kind, rank and differing words; False when it is not a change of sense."""
    reading, rp = greek_words(unit.reading), greek_words(unit.rp.lstrip("+ "))
    if unit.rp.strip() == "–":
        unit.kind, diff = "omit", reading
    elif unit.rp.startswith("+") or unit.reading.strip() == "–":
        unit.kind, diff = "add", rp
    elif sorted(reading) == sorted(rp):
        return False                                     # word order
    else:
        unit.kind = "substitute"
        a, b = set(reading), set(rp)
        diff = sorted(a ^ b)
        if len(a - b) == 1 and len(b - a) == 1:
            x, y = next(iter(a - b)), next(iter(b - a))
            if len(x) > 3 and len(y) > 3 and x[:4] == y[:4]:
                return False                             # another form of the same word
    content = [w for w in diff if w not in SMALL]
    person = {w[:2] for w in diff if w.startswith(("ημ", "υμ"))} == {"ημ", "υμ"}
    if not content and not person:
        return False
    unit.words = content or diff
    names = [w for w in unit.words if w in proper_names() and w not in TRIVIAL_NAMES]
    if unit.kind in ("add", "omit") and len(diff) >= 3 and set(content) - TRIVIAL_NAMES:
        unit.rank = "clause"
    elif names:
        unit.rank = "name"
    elif any(NUMBER_WORDS.match(w) for w in unit.words):
        unit.rank = "number"
    elif person:
        unit.rank = "person"
    else:
        unit.rank = "word"
    return True


def tr_follows_rp(unit, tr_text):
    """Whether the TR verse has RP's reading: True, False, or None (cannot tell)."""
    tr = set(greek_words(tr_text or ""))
    if not tr:
        return None
    reading = [w for w in greek_words(unit.reading) if w not in ARTICLES]
    rp = [w for w in greek_words(unit.rp.lstrip("+ ")) if w not in ARTICLES]
    has = lambda words: bool(words) and all(w in tr for w in words)
    if unit.kind == "add":
        return has(rp)
    if unit.kind == "omit":
        return not any(w in tr for w in reading if w not in SMALL) if reading else None
    if has(rp) and not has(reading):
        return True
    if has(reading) and not has(rp):
        return False
    return None


def person_mismatches(latin, tr):
    """[(vid, what)] where the Latin's first or second person plural is not in the TR at all."""
    out = []
    for vid, text in latin.items():
        greek = greek_words(tr.get(vid, ""))
        if not greek:
            continue
        we = any(w.startswith(("ημει", "ημων", "ημιν", "ημας", "ημετερ")) for w in greek)
        you = any(w.startswith(("υμει", "υμων", "υμιν", "υμας", "υμετερ")) for w in greek)
        if LATIN_WE.search(text) and not we and you:
            out.append((vid, f"Latin *{LATIN_WE.search(text).group(0)}*; the TR has only ὑμ-"))
        if LATIN_YOU.search(text) and not you and we:
            out.append((vid, f"Latin *{LATIN_YOU.search(text).group(0)}*; the TR has only ἡμ-"))
    return out


def noted_verses(book):
    """Verse ids already carrying a note or brackets in the master."""
    path = latex.usfm_path(book)
    out = set()
    if not path.exists():
        return out
    for vid, text, *_ in gold.rows(path.read_text(encoding="utf-8"), book.osis):
        if any(mark in text for mark in "[]⟦⟧"):
            out.add(vid)
    for c, v in re.findall(r"\\f \+ \\fr (\d+):(\d+)", path.read_text(encoding="utf-8")):
        out.add(tsv.verse_id(book.osis, int(c), int(v)))
    return out


def sblgnt_text(osis):
    path = SBLGNT / f"{osis}.txt"
    out = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^.+ (\d+):(\d+)\t(.*)$", line.lstrip("﻿"))
            if m:
                out[tsv.verse_id(osis, int(m.group(1)), int(m.group(2)))] = re.sub(r"[⸀⸁⸂⸃⸄⸅]", "", m.group(3)).strip()
    return out


def candidates(osis):
    """({vid: [Unit]}, [(vid, what)] person mismatches, counts) for one New Testament book."""
    book = books.select([osis])[0]
    latin = {vid: row["text"] for vid, row in gold.load(book.osis).items()}
    tr = (parallel.aligned("tr", book.osis) or ({}, {}))[0]
    skip = noted_verses(book)
    counts = {"apparatus": 0, "not sense": 0, "TR with consensus": 0, "already noted": 0, "kept": 0}
    found = {}
    for unit in apparatus(book.osis):
        counts["apparatus"] += 1
        if not classify(unit):
            counts["not sense"] += 1
            continue
        if unit.vid in skip:
            counts["already noted"] += 1
            continue
        if tr_follows_rp(unit, tr.get(unit.vid)) is False:
            counts["TR with consensus"] += 1
            continue
        counts["kept"] += 1
        found.setdefault(unit.vid, []).append(unit)
    person = [(vid, what) for vid, what in person_mismatches(latin, tr) if vid not in skip]
    return found, person, counts


RANKS = ("clause", "name", "number", "person", "word")


def report(osis):
    """The candidates file's Markdown."""
    book = books.select([osis])[0]
    found, person, counts = candidates(book.osis)
    latin = {vid: row["text"] for vid, row in gold.load(book.osis).items()}
    orig_path = paths.ROOT / "text" / "orig" / f"{book.usfm}.usfm"
    printed = ({vid: text for vid, text, *_ in gold.rows(orig_path.read_text(encoding="utf-8"), book.osis)}
               if orig_path.exists() else {})
    texts = {key: (parallel.aligned(key, book.osis) or ({}, {}))[0] for key in ("tr", "bsb", "web", "vulgate")}
    texts["sblgnt"] = sblgnt_text(book.osis)

    def ref(vid):
        _, c, v = tsv.parse_id(vid)
        return f"{c}:{v}"

    def evidence(vid):
        rows = [("Latin", latin.get(vid, "")), ("1573", printed.get(vid, "")), ("TR", texts["tr"].get(vid, "")),
                ("SBLGNT", texts["sblgnt"].get(vid, "")), ("Vulgate", texts["vulgate"].get(vid, "")),
                ("BSB", texts["bsb"].get(vid, "")), ("WEB", texts["web"].get(vid, ""))]
        return [f"   - {name}: {text}" for name, text in rows if text]

    out = [f"# {book.osis}: candidates for light notes",
           "",
           "Built by `python -m pipeline notes " + book.osis + "` (pipeline/notes.py); the process and its decisions are in",
           "`data/review/nt-notes-process.md`. These are not proposals: each is read with the NET notes (and the NRSVue",
           "for any that survive) before a note is put to Nathan in `" + book.osis.lower() + "-notes.md`.",
           "",
           f"Apparatus units with WH and NA28 (with SBLGNT) against RP: {counts['apparatus']}; not a change of sense (order, "
           f"article, form, small words): {counts['not sense']}; the TR with the critical text: "
           f"{counts['TR with consensus']}; in a verse already noted or bracketed: {counts['already noted']}; "
           f"**kept: {counts['kept']}**, in {len(found)} verses. Pronoun person (Latin against the TR): {len(person)}.",
           ""]
    loose = {vid: [u for u in units if u.loose] for vid, units in found.items()}
    loose = {vid: units for vid, units in loose.items() if units}
    found = {vid: [u for u in units if not u.loose] for vid, units in found.items()}
    found = {vid: units for vid, units in found.items() if units}
    for rank in RANKS:
        verses = [(vid, units) for vid, units in sorted(found.items(), key=lambda x: tsv.parse_id(x[0]))
                  if min(RANKS.index(u.rank) for u in units) == RANKS.index(rank)]
        if not verses:
            continue
        out += [f"## Text: {rank} ({len(verses)} verses)", ""]
        for vid, units in verses:
            out.append(f"- **{ref(vid)}** " + "; ".join(
                f"{u.kind} ({u.rank}): critical *{u.reading}* ] RP *{u.rp}*" for u in units))
            out += evidence(vid)
        out.append("")
    if loose:
        out += [f"## Tregelles with RP ({len(loose)} verses; inside the test since 2026-11-16, listed apart)", ""]
        for vid, units in sorted(loose.items(), key=lambda x: tsv.parse_id(x[0])):
            out.append(f"- **{ref(vid)}** " + "; ".join(
                f"{u.kind} ({u.rank}): critical *{u.reading}* ] RP, Treg *{u.rp}*" for u in units))
            out += evidence(vid)
        out.append("")
    if person:
        out += [f"## Person ({len(person)} verses)", ""]
        for vid, what in person:
            out.append(f"- **{ref(vid)}** {what}")
            out += evidence(vid)
        out.append("")
    return "\n".join(out)


def write(osis):
    book = books.select([osis])[0]
    if book.testament != "novum":
        raise SystemExit("notes: the New Testament only, for now (nt-notes-process.md)")
    path = paths.DATA / "review" / f"{book.osis.lower()}-notes-candidates.md"
    path.write_text(report(book.osis), encoding="utf-8", newline="\n")
    return path
