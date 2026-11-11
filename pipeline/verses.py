"""Stages 3–5 on an unmarked draft, proposed one verse at a time.

A draft made from Wikisource (`pipeline draft`) has no macrons and no quotation marks, so stages 3–5 change nearly
every word: one Apply line per change would run to thousands. Here each verse is one proposal, the whole verse
as it would be after

  layout    the verse's line in data/decisions/<osis>.layout.tsv, if any: quotation marks, \\qt, poetry markers,
            paragraph markers, capitals for God and punctuation, written over the draft's own words (the words
            must stay the same, case aside; wording is stage 2's)
  case      a verse that continues the sentence of the verse before starts in lower case (as in your settled
            chapters: Mark 4:2 *multa*, Matt 15:6 *nihil*)
  spelling  the approved rules (normalize.changes: word and phrase rules, j/v; æ/œ come with the macrons)
  macrons   harness variant C (W/M with Gaffiot for stems, your settled forms, WordPress 2019 in context), or the
            verse's line in data/decisions/<osis>.forms.tsv where one was decided by reading the verse

Each verse's Apply line replaces the whole verse (review.verse_span: its paragraph or poetry markers included),
so `python -m pipeline review check|apply` takes it as any other. Only the uncertain words are flagged, with their
evidence (decision 6): what goes unflagged is UNFLAGGED below, and `rates()` measures how often each kind is wrong
on the settled chapters."""

import collections
import difflib
import re
from dataclasses import dataclass, field

from pipeline import align, books, gold, harness, latex, macronize, normalize, paths, review, rules, structure, tsv

WORD = re.compile(r"[^\W\d_]+")
MARKER = re.compile(r"\\[a-z]+\d*\*?")
SPAN = re.compile(r"^\s*((?:\\(?:p|m|b|nb|q\d?|pi\d?)\s+)*)\\v (\d+)\s+(.*?)\s*$", re.S)
DECISIONS = paths.DATA / "decisions"

# How a word's marking was decided (harness.macronize_all's `how`, with `lexicon` split by WordPress).
KINDS = {
    "lexicon": "the lexicon's one marking (W/M), WordPress 2019 agreeing or silent",
    "wordpress": "the lexicon's one marking; WordPress 2019 marks it otherwise",
    "chosen+settled": "a homograph: WordPress 2019 chose among the lexicon's markings, your settled forms agreeing",
    "chosen": "a homograph: WordPress 2019 chose among the lexicon's markings, your settled forms silent or not agreeing",
    "settled": "your settled forms (≥ 80% of data/gold/) overrule the lexicon",
    "homograph+settled": "a homograph your settled forms decided, WordPress 2019 silent",
    "gaffiot": "Gaffiot changed the W/M stem (always flagged: the stem step is still wrong on 5 of 25 words)",
    "witness": "unknown to the lexicon: WordPress 2019's marks",
    "homograph": "a homograph that nothing chose",
    "unknown": "no source marks the word",
    "decided": "decided by reading the verse (data/decisions/<osis>.forms.tsv)",
    "capital": "a capital for God or Christ (decision 20), or another change of case",
    "case": "lower case at the start of a verse that continues a sentence",
    "punctuation": "punctuation changed (around a quotation, or modernized)",
}
UNFLAGGED = {"lexicon", "chosen+settled"}   # with the approved spelling rules (decision 6; Nathan, 2026-11-08)


@dataclass
class Flag:
    word: str
    kind: str
    note: str = ""


@dataclass
class Verse:
    vid: str
    old: str                                          # the draft's span, as review.verse_span gives it
    new: str = ""
    marks: list = field(default_factory=list)
    body: str = ""
    flags: list = field(default_factory=list)
    respelled: list = field(default_factory=list)     # [(old, new, kind)] by the approved rules: not flagged
    quotes: bool = False                              # quotation marks, \qt or poetry added (the layout file)
    note: str = ""                                    # the layout file's note (an uncertain call), if any
    kinds: collections.Counter = field(default_factory=collections.Counter)   # every word's kind


# ---------------------------------------------------------------- the decision files

def load_layout(osis):
    """{verse id: (marks or None to keep the draft's, text, note)} from data/decisions/<osis>.layout.tsv."""
    path = DECISIONS / f"{osis}.layout.tsv"
    if not path.exists():
        return {}
    return {r["id"]: (None if r["marks"] == "=" else [] if r["marks"] == "-" else r["marks"].split(), r["text"],
                      r.get("note", ""))
            for r in tsv.read(path)}                      # `-`: no marker (the draft's \p removed)


def load_forms(osis):
    """{(verse id, plain word): (marked form, note)} from data/decisions/<osis>.forms.tsv. An id `Exod.18.8#2`
    decides only the second copy of the word in that verse (keyed (verse id, plain word, 2)), where the copies differ
    (*ā Jōvā* and *Jōva* in one verse)."""
    path = DECISIONS / f"{osis}.forms.tsv"
    if not path.exists():
        return {}
    out = {}
    for r in tsv.read(path):
        vid, _, nth = r["id"].partition("#")
        key = (vid, macronize.key(r["form"])) + ((int(nth),) if nth else ())
        out[key] = (r["form"], r.get("note", ""))
    return out


def words_of(text):
    return WORD.findall(MARKER.sub(" ", text))


def punctuation_of(text):
    """The text with its words and quotation marks taken out: what a layout line may change besides them."""
    text = MARKER.sub(" ", text)
    return re.sub(r"\s+", " ", re.sub(r"[“”‘’]", "", WORD.sub("", text))).strip()


PIECE = re.compile(r"[^\W\d_]+|[^\w\s“”‘’]")


def punctuation_changes(old, new):
    """The punctuation a layout line changes, each with the word before it: ['*inquit:* → *inquit,*', …]."""
    def after_each(text):
        """[(word, the punctuation up to the next word)], with a first entry for what comes before any word."""
        out = [("", "")]
        for piece in PIECE.findall(MARKER.sub(" ", text)):
            if WORD.fullmatch(piece):
                out.append((piece, ""))
            else:
                out[-1] = (out[-1][0], out[-1][1] + piece)
        return out

    out = []
    for (word, a), (_, b) in zip(after_each(old), after_each(new)):     # the words are the same (with_layout)
        if a != b:
            out.append(f"*{word}{a or ' ∅'}* → *{word}{b or ' ∅'}*")
    return out


# ---------------------------------------------------------------- one verse at a time

def split_span(text):
    """(markers before \\v, verse number, body) of a verse span."""
    m = SPAN.match(text)
    if not m:
        raise ValueError(f"not a verse span: {text[:60]!r}")
    return [x.lstrip("\\") for x in m.group(1).split()], int(m.group(2)), re.sub(r"\s*\n\s*", " ", m.group(3))


def with_layout(verse, number, decision):
    """Apply the verse's layout line; flags for case and punctuation changes. Raises if the words differ."""
    marks, text, note = decision
    old_words, new_words = words_of(verse.body), words_of(text)
    if [w.lower() for w in old_words] != [w.lower() for w in new_words]:
        raise ValueError(f"{verse.vid}: the layout line's words differ from the draft's:\n  {verse.body}\n  {text}")
    for a, b in zip(old_words, new_words):
        if a != b:
            verse.flags.append(Flag(b, "capital", f"draft *{a}*"))
    if punctuation_of(verse.body) != punctuation_of(text):
        verse.flags.append(Flag("", "punctuation", "; ".join(punctuation_changes(verse.body, text))))
    verse.quotes = bool(re.search(r"[“”‘’]|\\qt|\\q\d", text)) or marks is not None and marks != verse.marks
    if marks is not None:
        verse.marks = marks
    verse.body, verse.note = text, note


ENDS_SENTENCE = re.compile(r"[.?!][”’)\s]*$|^$")


def continues(previous_body, colon=False):
    """Does the verse after this one continue its sentence? (It ends in , ; or a word, not . ? ! or, unless
    `colon`, a colon: your settled chapters lower a capital after a colon only 61% of the time.)"""
    text = MARKER.sub(" ", previous_body).strip()
    return not ENDS_SENTENCE.search(text) and (colon or not re.search(r":[”’)\s]*$", text))


def lower_keys():
    """Lexicon keys your settled chapters write in lower case somewhere: common words, not names."""
    return {macronize.key(w) for b in books.BOOKS for row in gold.load(b.osis).values()
            for w in WORD.findall(row["text"]) if w[0].islower()}


_SETTLED_KEYS = []


def settled_keys():
    """Every lexicon key your settled chapters use (cached)."""
    if not _SETTLED_KEYS:
        _SETTLED_KEYS.append({macronize.key(w) for b in books.BOOKS for row in gold.load(b.osis).values()
                              for w in WORD.findall(row["text"])})
    return _SETTLED_KEYS[0]


# Deus, which normalize.DIVINE leaves out (its de- would catch dē, deinde): God, always capital in your text (2 Cor
# 9:13 *Deum collaudantēs* after a comma). A pagan *deus* at a verse start is lowered by its layout line.
GOD = re.compile(r"^(deus|deī|dei|deō|deo|deum)$", re.I)


def lower_start(body, lexicon, common):
    """The body with its first word in lower case, unless it opens a quotation, may name God (decision 20), or is
    a name: written only with a capital in your settled chapters (`common`: lower_keys()) and in the lexicon, its
    host too (Vīxit|que); None if nothing changes."""
    text = MARKER.sub(lambda m: " " * len(m.group()), body)
    m = WORD.search(text)
    if not m or not m.group()[0].isupper() or re.search(r"[“‘(]", text[:m.start()]) or normalize.DIVINE.match(m.group())             or GOD.match(m.group()):
        return None
    word = m.group()
    entry = lexicon.get(macronize.key(word), macronize.Entry())
    host, _ = macronize.split_enclitic(word, entry)
    keys = {macronize.key(word), macronize.key(host)}
    if keys & common:
        return body[:m.start()] + word[0].lower() + body[m.start() + 1:]
    if keys & settled_keys():                         # written only with a capital in your text: a name (Pīlātus)
        return None
    lexicon_lower = any(c.form[:1].islower() for k in keys for c in lexicon.get(k, macronize.Entry()).candidates)
    if not lexicon_lower:
        return None
    return body[:m.start()] + word[0].lower() + body[m.start() + 1:]


def respell(body, word_rules, known):
    """(body with the approved rules applied, [(old, new, kind)]), macrons and æ/œ taken out (stage 4 marks them)."""
    words, phrases = word_rules
    done = []
    for start, end, new, kind, note in reversed(normalize.changes(body, words, phrases, known)):
        new = rules.unligature(macronize.mark(new, set()))
        old = body[start:end]
        if new != old:
            body = body[:start] + new + body[end:]
            done.append((old, new, kind))
    return body, done[::-1]


def evidence(token, entry, counts, wp):
    parts = []
    if entry.candidates:
        parts.append("lexicon " + " · ".join(f"{macronize.ligatures(c.form)} [{c.sources}]" for c in entry.candidates[:4]))
    if entry.gaffiot:
        parts.append("Gaffiot " + " · ".join(dict.fromkeys(head[0] for head in entry.gaffiot[:3])))
    if counts:
        parts.append("settled " + ", ".join(f"{w} {n}" for w, n in counts.most_common(3)))
    if wp is not None:
        parts.append(f"WordPress {macronize.finish(token, wp)}")
    return "; ".join(parts) or "no source"


def kind_of(how, proposed, token, wp, default, options=0):
    """The flag kind of a marked word: `how`, with a lexicon word WordPress marks otherwise set apart, a homograph
    WordPress chose split by whether your settled forms' dominant marking (`default`) agrees, and a homograph
    (`options` > 1) that your settled forms decided, where WordPress was silent, set apart from the settled forms
    overruling the lexicon."""
    longs = macronize.long_vowels(rules.unligature(proposed))
    if how == "settled" and options > 1:
        return "homograph+settled"
    if how == "lexicon" and wp is not None and \
            macronize.long_vowels(rules.unligature(macronize.finish(token, wp))) != longs:
        return "wordpress"
    if how == "chosen" and default is not None and \
            macronize.long_vowels(rules.unligature(macronize.finish(token, default))) == longs:
        return "chosen+settled"
    return how


def propose(osis, chapters, usfm=None):
    """[Verse] for these chapters of the draft (text/draft/<USFM>.usfm), each with its whole proposed span."""
    book = books.select([osis])[0]
    usfm = latex.usfm_path(book, draft=True).read_text(encoding="utf-8") if usfm is None else usfm
    layout, forms = load_layout(osis), load_forms(osis)
    known = normalize.settled_forms()
    word_rules = normalize.word_rules()
    verses = []
    for vid, span, text in normalize.verses(usfm, osis):
        if tsv.parse_id(vid)[1] not in chapters:
            continue
        verse = Verse(vid, text.strip())
        verse.marks, number, verse.body = split_span(text)
        if vid in layout:
            with_layout(verse, number, layout[vid])
        verses.append(verse)
    unknown = set(layout) - {v.vid for v in verses}
    if any(tsv.parse_id(vid)[1] in chapters for vid in unknown):
        raise ValueError(f"layout lines for verses not in the draft: {sorted(unknown)}")

    # Spelling first (the words the lexicon is asked about are the respelled ones).
    for verse in verses:
        verse.body, verse.respelled = respell(verse.body, word_rules, known)
    tokens, where = [], []
    for n, verse in enumerate(verses):
        blank = MARKER.sub(lambda m: " " * len(m.group()), verse.body)
        for m in WORD.finditer(blank):
            tokens.append((verse.vid, m.group()))
            where.append((n, m.start(), m.end()))
    lexicon = macronize.lookup([w for _, w in tokens])
    lexicon.update(macronize.lookup([macronize.split_enclitic(w, lexicon[macronize.key(w)])[0] for _, w in tokens]))

    # Case: a verse continuing the sentence before starts in lower case (unless its layout line set the case).
    common = lower_keys()
    for n, verse in enumerate(verses[1:], 1):
        before = verses[n - 1]
        if tsv.parse_id(before.vid)[1] == tsv.parse_id(verse.vid)[1] and continues(before.body) and \
                not any(f.kind == "capital" for f in verse.flags):
            lowered = lower_start(verse.body, lexicon, common)
            if lowered is not None:
                first = WORD.search(MARKER.sub(" ", lowered)).group()
                verse.body = lowered
                ending = " ".join(MARKER.sub(" ", before.body).split()[-3:])
                verse.flags.append(Flag(first, "case", f"{before.vid.split('.', 1)[1].replace('.', ':')} ends “…{ending}”"))
                index = next(i for i, (k, _, _) in enumerate(where) if k == n)
                tokens[index] = (verse.vid, first)

    everything = [b.osis for b in books.BOOKS if gold.load(b.osis)]
    defaults = harness.settled_defaults(everything)
    witness = harness.wordpress_marks(osis, tokens)
    output = harness.macronize_all(tokens, lexicon, "C", defaults, witness)
    counts = settled_counts()
    marked = [list() for _ in verses]                 # [(start, end, word)] per verse
    copies = collections.Counter()                    # (verse id, plain word): copies seen so far
    for index, ((vid, token), out) in enumerate(zip(tokens, output)):
        n, start, end = where[index]
        verse = verses[n]
        k = macronize.key(token)
        entry = lexicon.get(k, macronize.Entry())
        wp = witness.get(index)
        word, kind = out.word, kind_of(out.how, out.word, token, wp, defaults.get(k), out.options)
        note = evidence(token, entry, counts.get(k), wp)
        copies[(vid, k)] += 1
        decided = (vid, k, copies[(vid, k)]) if (vid, k, copies[(vid, k)]) in forms else (vid, k)
        if decided in forms:
            form, why = forms[decided]
            if macronize.plain(rules.unligature(form)) != macronize.plain(rules.unligature(token)).replace("æ", "ae"):
                raise ValueError(f"{vid}: decided form {form} does not spell {token}")
            word = macronize.finish(token, macronize.long_vowels(rules.unligature(form)))
            note = f"{why} (pipeline: {out.word}, {out.how}; {note})"
            kind = "decided"
        verse.kinds[kind] += 1
        if kind not in UNFLAGGED:
            verse.flags.append(Flag(word, kind, note))
        marked[n].append((start, end, word))
    for verse, words in zip(verses, marked):
        body = verse.body
        for start, end, word in reversed(words):
            body = body[:start] + word + body[end:]
        verse.body = body
        verse.new = " ".join([f"\\{m}" for m in verse.marks] + [f"\\v {tsv.parse_id(verse.vid)[2]}", body])
        # Flags for case and capitals carry the draft's word: show the marked one.
        plain = {macronize.key(w): w for _, _, w in words}
        for f in verse.flags:
            if f.kind in ("capital", "case"):
                f.word = plain.get(macronize.key(f.word), f.word)
    return verses


def settled_counts():
    """{lexicon key: Counter of marked forms (lower case)} over every settled book."""
    counts = collections.defaultdict(collections.Counter)
    for book in books.BOOKS:
        for row in gold.load(book.osis).values():
            for w in WORD.findall(row["text"]):
                counts[macronize.key(w)][w.lower()] += 1
    return counts


# ---------------------------------------------------------------- the review file

QUIET = "chosen+settled"          # flagged, but listed on one line: measured as safe as the lexicon's own marking


def display(verse):
    """The proposed verse for reading: \\qt spans in italics, flagged words in bold (but the quiet kind), markers kept."""
    flagged = {macronize.key(f.word) for f in verse.flags if f.word and f.kind != QUIET}
    text = re.sub(r"\\qt\s*(.*?)\\qt\*", lambda m: f"_{m.group(1).strip()}_", verse.body)
    text = WORD.sub(lambda m: f"**{m.group()}**" if macronize.key(m.group()) in flagged else m.group(), text)
    return " ".join([f"\\{m}" for m in verse.marks] + [text])


def one_line(text):
    return re.sub(r"\s+", " ", text).strip()


def item(verse):
    osis, chapter, number = tsv.parse_id(verse.vid)
    loud = [f for f in verse.flags if f.kind != QUIET]
    quiet = [f.word for f in verse.flags if f.kind == QUIET]
    tags = [f"⚑ {len(loud)}"] if loud else []
    if verse.quotes:
        tags.append("layout")
    lines = [f"{number}. **{osis} {chapter}:{number}**" + (" · " + " · ".join(tags) if tags else ""),
             f"   {display(verse)}"]
    if verse.note:
        lines.append(f"   - ⚑ **layout**: {verse.note}")
    seen = collections.Counter((f.word, f.kind, f.note) for f in loud)
    for (word, kind, note), n in seen.items():
        label = f"*{word}*" + (f" ×{n}" if n > 1 else "") + " " if word else ""
        lines.append(f"   - ⚑ {label}{kind}: {note}")
    if quiet:
        lines.append(f"   - homographs that WordPress 2019 and your settled forms mark alike: "
                     + ", ".join(f"*{w}*" for w in dict.fromkeys(quiet)))
    if verse.respelled:
        lines.append("   - spelling (approved rules): " + ", ".join(f"{a} → {b}" for a, b, _ in verse.respelled))
    lines.append(f"   **Apply:** `{verse.vid}` la: `{one_line(verse.old)}` → `{one_line(verse.new)}`")
    return "\n".join(lines)


def chapter_file(osis, chapter, verses, title):
    flags = collections.Counter(f.kind for v in verses for f in v.flags)
    words = sum(sum(v.kinds.values()) for v in verses)
    head = [f"# {title} {chapter}: stages 3–5, one proposal per verse", "",
            f"{len(verses)} verses, {words} words. Each item is the whole verse as proposed: spelling by the approved "
            "rules, macrons, quotation marks and layout. **Bold** words are flagged (⚑), with their evidence; the "
            "rest are the lexicon's only marking (WordPress 2019 agreeing or silent), homographs that WordPress 2019 "
            "chose and your settled forms mark alike (decision 6, 2026-11-08), or the approved spelling rules. "
            "`layout` marks a verse whose quotation marks, `\\qt` (shown in _italics_) or poetry were placed by "
            "reading it. Summary, rates and how to apply: `data/review/mark6-16-stages3-5.md`.", "",
            "Flagged: " + (", ".join(f"{n} {k}" for k, n in flags.most_common()) or "nothing") + ".", "",
            f"## {title} {chapter}", "",
            "To accept the chapter but some verses, write e.g. `accept all except 14, 22` (item numbers are verse "
            "numbers).", "", "**Decision:**", ""]
    return "\n".join(head + [item(v) for v in verses]) + "\n"


# ---------------------------------------------------------------- measured on the settled chapters

def rates(names=(), wordpress=True):
    """{kind: [words, words wrong]} for the macron kinds and the ligatures, over the settled books: each chapter
    marked with the settled forms of the other chapters (harness variant D), from the gold's own spelling."""
    everything = [b.osis for b in books.BOOKS if gold.load(b.osis)]
    by_chapter = harness.ChapterDefaults(everything)
    out = collections.defaultdict(lambda: [0, 0])
    examples = collections.defaultdict(list)
    for osis in [b.osis for b in books.select(names) if gold.load(b.osis)]:
        rows = gold.load(osis)
        gold_words = [(vid, w) for vid, row in rows.items() if tsv.parse_id(vid)[2] > 0 for w in WORD.findall(row["text"])]
        tokens = [(vid, rules.unligature(macronize.mark(w, set()))) for vid, w in gold_words]
        lexicon = macronize.lookup([w for _, w in tokens])
        lexicon.update(macronize.lookup([macronize.split_enclitic(w, lexicon[macronize.key(w)])[0] for _, w in tokens]))
        witness = harness.wordpress_marks(osis, tokens) if wordpress else {}
        output = harness.macronize_all(tokens, lexicon, "D", {}, witness, by_chapter)
        for index, (word, (vid, want), (_, token)) in enumerate(zip(output, gold_words, tokens)):
            kind = kind_of(word.how, word.word, token, witness.get(index), by_chapter.get(vid, macronize.key(token)),
                           word.options)
            wrong = macronize.long_vowels(rules.unligature(word.word)) != macronize.long_vowels(rules.unligature(want))
            out[kind][0] += 1
            out[kind][1] += wrong
            if wrong and len(examples[kind]) < 6:
                examples[kind].append(f"{vid} {word.word} (gold {want})")
            if any(c in "æœÆŒ" for c in want + word.word):
                lig = macronize.plain(word.word) != macronize.plain(want)
                out["ligature"][0] += 1
                out["ligature"][1] += lig
                if lig and len(examples["ligature"]) < 6:
                    examples["ligature"].append(f"{vid} {word.word} (gold {want})")
    return dict(out), dict(examples)


def spelling_rates(names=()):
    """{kind: [words changed, wrong]} for the approved rules run on Wikisource's text of the settled chapters,
    against the gold (macrons, case and æ/œ aside), plus `missed` (words left as Wikisource spells them where
    the gold respells them). The settled forms that guard j/v come from the other books only."""
    word_rules = normalize.word_rules()
    out = collections.defaultdict(lambda: [0, 0])
    examples = collections.defaultdict(list)
    spell = lambda w: rules.unligature(macronize.plain(w))
    for book in [b for b in books.select(names) if gold.load(b.osis)]:
        known = {k: v for k, v in other_forms(book.osis).items()}
        rows = gold.load(book.osis)
        for r in tsv.read(paths.WITNESSES / "wikisource" / f"{book.osis}.tsv"):
            if r["id"] not in rows or tsv.parse_id(r["id"])[2] == 0:
                continue
            new, done = respell(r["text"], word_rules, known)
            source, after, target = WORD.findall(r["text"]), WORD.findall(new), WORD.findall(rows[r["id"]]["text"])
            if len(source) != len(after):
                continue                                  # a phrase rule joined words: counted below by verse
            kinds = {}
            for old, changed, kind in done:
                kinds.setdefault(rules.unligature(macronize.plain(old)), kind)
            a, b = [align.reading(w) for w in after], [align.reading(w) for w in target]
            for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
                if tag != "equal":
                    continue
                for k in range(i2 - i1):
                    before, now, want = source[i1 + k], after[i1 + k], target[j1 + k]
                    if spell(before) != spell(now):
                        kind = kinds.get(spell(before), "word")
                        out[kind][0] += 1
                        if spell(now) != spell(want):
                            out[kind][1] += 1
                            if len(examples[kind]) < 6:
                                examples[kind].append(f"{r['id']} {before}→{now} (gold {want})")
                    elif spell(now) != spell(want):
                        out["missed"][0] += 1
                        if len(examples["missed"]) < 12:
                            examples["missed"].append(f"{r['id']} {now} (gold {want})")
    return dict(out), dict(examples)


def other_forms(osis):
    """normalize.settled_forms() learned from the other books only."""
    seen = {}
    for book in books.BOOKS:
        if book.osis == osis:
            continue
        for row in gold.load(book.osis).values():
            for word in WORD.findall(row["text"]):
                seen.setdefault(rules.unligature(macronize.plain(word)), set()).add(word.lower())
    return {k: next(iter(v)) for k, v in seen.items() if len(v) == 1}


def case_rates(names=()):
    """The lower-case rule on Wikisource's verse starts against the gold: {kind: [n, wrong]} (wrong: the gold's
    first word has the other case). After a colon, a verse opening a quotation in the gold is left out (the
    rule keeps its capital)."""
    out = collections.defaultdict(lambda: [0, 0])
    examples = collections.defaultdict(list)
    common = lower_keys()
    for book in [b for b in books.select(names) if gold.load(b.osis)]:
        rows = gold.load(book.osis)
        ws = {r["id"]: r["text"] for r in tsv.read(paths.WITNESSES / "wikisource" / f"{book.osis}.tsv")}
        ids = [vid for vid in rows if tsv.parse_id(vid)[2] > 1 and vid in ws and WORD.search(ws[vid])]
        firsts = [WORD.search(ws[v]).group() for v in ids]
        lexicon = macronize.lookup(firsts)
        lexicon.update(macronize.lookup([macronize.split_enclitic(w, lexicon[macronize.key(w)])[0] for w in firsts]))
        for vid in ids:
            osis, c, v = tsv.parse_id(vid)
            before = tsv.verse_id(osis, c, v - 1)
            first = WORD.search(ws[vid]).group()
            if before not in ws or not first[0].isupper() or not WORD.search(rows[vid]["text"]):
                continue
            target = rows[vid]["text"].lstrip()
            if target[:1] in "“‘" or not continues(ws[before], colon=True):
                continue                                  # a quotation opens (the layout keeps it), or a new sentence
            lowered = lower_start(ws[vid], lexicon, common) is not None
            kind = ("after a colon: " if ws[before].strip().endswith(":") else "") + ("lowered" if lowered else "kept")
            out[kind][0] += 1
            if lowered != WORD.search(target).group()[0].islower():
                out[kind][1] += 1
                if len(examples[kind]) < 8:
                    examples[kind].append(f"{vid} {first} (gold {WORD.search(target).group()})")
    return dict(out), dict(examples)


def review_paths(osis, chapters):
    """{chapter: data/review/<osis>F-L-chNN.md} for these chapters (F-L: the first and last)."""
    span = f"{osis.lower()}{min(chapters)}-{max(chapters)}"
    return {c: paths.DATA / "review" / f"{span}-ch{c:02}.md" for c in chapters}


def write(osis, chapters, preview=True):
    """Write a review file per chapter and, with `preview`, text/draft/<USFM>.preview.usfm with every verse
    applied (through review.apply, as `review apply --all --to` would). Returns ([Verse], [paths written])."""
    book = books.select([osis])[0]
    verses = propose(osis, chapters)
    title = {"Mark": "Mark"}.get(osis, osis)
    written = []
    for chapter, path in review_paths(osis, chapters).items():
        mine = [v for v in verses if tsv.parse_id(v.vid)[1] == chapter]
        if mine:
            text = chapter_file(osis, chapter, mine, title)
            if path.exists():                         # a decision already written there is kept
                old = re.search(r"^\*\*Decision:\*\*.*$", path.read_text(encoding="utf-8"), re.M)
                if old:
                    text = re.sub(r"^\*\*Decision:\*\*.*$", lambda m: old.group(), text, count=1, flags=re.M)
            path.write_text(text, encoding="utf-8", newline="\n")
            written.append(path)
    if preview:
        draft = latex.usfm_path(book, draft=True)
        target = draft.with_suffix(".preview.usfm")
        items = [i for p in written for i in review.parse(p.read_text(encoding="utf-8"))]
        outcomes, texts = review.apply(items, {target: draft.read_text(encoding="utf-8")}, target)
        failed = [o for o in outcomes if o.status not in ("ok", "already")]     # already: the verse needs no change
        if failed:
            raise ValueError(f"preview: {len(failed)} verses did not apply, e.g. {failed[0].replacement.vid} {failed[0].status}")
        target.write_text(texts[target], encoding="utf-8", newline="\n")
        written.append(target)
    return verses, written
