"""The M1 test harness: stages 3 (normalize) and 4 (macronize) run on the settled chapters from the Wikisource
text alone, and scored against the gold (data/gold/).

Everything learned from the gold (the spelling rules, your settled forms) is learned from the other books only
and tested on the one left out, so no book is scored on what it taught. Variants:

  A  lexicon      W/M candidates, Gaffiot for stems and hidden quantities; a homograph takes the W form
  B  + settled    your settled forms (other books) decide where one marking dominates (≥ 80%)
  C  + WordPress  B, with your 2019 WordPress macrons choosing among a homograph's markings in context
  D  C, but your settled forms come from every other *chapter* (the same book included), as when a book is
     finished chapter by chapter: names and habits of the book are known; the chapter itself is not
  W  WordPress    your 2019 macrons alone (a baseline: what you decided then)

Scores, over gold words: word (the same word: case, macrons, i/j, u/v, æ aside), spelling (macrons and case
aside, æ and j/v counted), and per vowel (of correctly spelt words: long or not, as in the gold)."""

import collections
import difflib
import re
from dataclasses import dataclass, field

from pipeline import align, books, gold, macronize, paths, rules, tsv

WORD = re.compile(r"[^\W\d_]+")
VARIANTS = ("A", "B", "C", "D", "W")
NAMES = {"A": "lexicon (Gaffiot/W/M)", "B": "+ your settled forms", "C": "+ WordPress in context",
         "D": "C, forms from other chapters", "W": "WordPress 2019 alone"}


def is_long(char):
    return char in "āēīōūȳĀĒĪŌŪȲ"


# ---------------------------------------------------------------- stage 3: normalize

def word_rules(train):
    """({old: new} word rules, [(old words, new words)] phrase rules) learned from the training books."""
    return _rule_maps(rules.rule_rows(rules.learn(train)))


def _rule_maps(rows):
    words, phrases = {}, []
    for old, new, scope, status, note in rows:
        if scope == "word":
            words[rules.unligature(old)] = rules.unligature(new)
        elif scope == "phrase":
            phrases.append((tuple(rules.unligature(old).split()), tuple(rules.unligature(new).split())))
    return words, phrases


def normalize(tokens, words, phrases):
    """[(verse id, word)] → the same with phrase rules (word division), then word rules, then j/v applied."""
    out, i = [], 0
    while i < len(tokens):
        for old, new in phrases:
            span = tokens[i:i + len(old)]
            if tuple(macronize.plain(w) for _, w in span) == old:
                out.extend((tokens[i][0], _case(span[0][1], w) if k == 0 else w) for k, w in enumerate(new))
                i += len(old)
                break
        else:
            out.append(tokens[i])
            i += 1
    normalized = []
    for vid, word in out:
        word = rules.unligature(word)
        new = words.get(macronize.plain(word))
        normalized.append((vid, macronize.jv(_case(word, new) if new else word)))
    return normalized


def _case(model, word):
    return word[:1].upper() + word[1:] if model[:1].isupper() else word


# ---------------------------------------------------------------- stage 4: macronize

def marking_counts(osis_list):
    """{chapter (osis, n): {lexicon key: Counter of long-vowel sets}} over the gold of these books."""
    counts = collections.defaultdict(lambda: collections.defaultdict(collections.Counter))
    for osis in osis_list:
        for vid, row in gold.load(osis).items():
            chapter = vid.rsplit(".", 1)[0]
            for word in WORD.findall(row["text"]):
                counts[chapter][macronize.key(word)][frozenset(macronize.long_vowels(rules.unligature(word)))] += 1
    return counts


def dominant(counter):
    if not counter:
        return None
    longs, n = counter.most_common(1)[0]
    return longs if n >= 0.8 * sum(counter.values()) else None


def settled_defaults(train):
    """{lexicon key: frozenset of long vowels} for forms of the training books' gold with one dominant marking."""
    seen = collections.defaultdict(collections.Counter)
    for chapter in marking_counts(train).values():
        for k, c in chapter.items():
            seen[k].update(c)
    return {k: d for k, c in seen.items() if (d := dominant(c)) is not None}


class ChapterDefaults:
    """Settled forms from every chapter but the one a word is in (leave-one-chapter-out)."""

    def __init__(self, everything):
        self.chapters = marking_counts(everything)
        self.total = collections.defaultdict(collections.Counter)
        for chapter in self.chapters.values():
            for k, c in chapter.items():
                self.total[k].update(c)

    def get(self, vid, k):
        return dominant(self.total[k] - self.chapters[vid.rsplit(".", 1)[0]].get(k, collections.Counter()))


def wordpress_marks(osis, tokens):
    """{token index: frozenset of long vowels} from the WordPress witness, aligned verse by verse."""
    path = paths.WITNESSES / "wordpress" / f"{osis}.tsv"
    if not path.exists():
        return {}
    verses = {row["id"]: WORD.findall(row["text"]) for row in tsv.read(path)}
    # A chapter WordPress never macronized (Gen 34: 0 of 522 words) is no witness: its bare words would read as
    # decisions that every vowel is short.
    marked = collections.Counter()
    total = collections.Counter()
    for vid, words in verses.items():
        chapter = vid.rsplit(".", 1)[0]
        total[chapter] += len(words)
        marked[chapter] += sum(1 for w in words if macronize.long_vowels(w))
    verses = {vid: words for vid, words in verses.items()
              if marked[vid.rsplit(".", 1)[0]] >= 0.1 * total[vid.rsplit(".", 1)[0]]}
    marks, by_verse = {}, collections.defaultdict(list)
    for index, (vid, word) in enumerate(tokens):
        by_verse[vid].append(index)
    for vid, indices in by_verse.items():
        wp = verses.get(vid, [])
        a = [macronize.key(tokens[i][1]) for i in indices]
        b = [macronize.key(w) for w in wp]
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    marks[indices[i1 + k]] = frozenset(macronize.long_vowels(rules.unligature(wp[j1 + k])))
    return marks


@dataclass
class Word:
    vid: str
    word: str
    how: str
    options: int = 0


def macronize_all(tokens, lexicon, variant, defaults, witness, by_chapter=None):
    out = []
    for index, (vid, word) in enumerate(tokens):
        k = macronize.key(word)
        default = by_chapter.get(vid, k) if variant == "D" else defaults.get(k)
        entry = lexicon.get(k, macronize.Entry())
        wp = witness.get(index)
        if variant == "W":
            longs, how = (wp, "witness") if wp is not None else (frozenset(), "unknown")
            out.append(Word(vid, macronize.finish(word, longs), how))
            continue
        host, enclitic = macronize.split_enclitic(word, entry)
        if enclitic:                                      # Fēcit|que: the host is marked, the enclitic never
            entry = lexicon.get(macronize.key(host), macronize.Entry())
            wp = frozenset(i for i in wp if i < len(host)) if wp is not None else None
        prefer = None
        if variant in ("C", "D") and wp is not None:
            prefer = lambda options, wp=wp: wp if wp in options else None
        choice = macronize.choose(host, entry, prefer)
        longs, how = choice.longs, choice.how
        if variant in ("B", "C", "D") and default is not None and how != "chosen":
            if default != longs or how in ("homograph", "unknown"):
                longs, how = default, "settled"
        if variant in ("C", "D") and how == "unknown" and wp is not None:
            longs, how = wp, "witness"
        out.append(Word(vid, macronize.finish(word, longs), how, len(choice.options)))
    return out


# ---------------------------------------------------------------- scoring

@dataclass
class Score:
    words: int = 0
    word_ok: int = 0
    spelled: int = 0
    spelling_ok: int = 0
    vowels: int = 0
    vowels_ok: int = 0
    words_marked_ok: int = 0
    errors: collections.Counter = field(default_factory=collections.Counter)
    examples: dict = field(default_factory=lambda: collections.defaultdict(list))

    def add(self, other):
        for name in ("words", "word_ok", "spelled", "spelling_ok", "vowels", "vowels_ok", "words_marked_ok"):
            setattr(self, name, getattr(self, name) + getattr(other, name))
        self.errors.update(other.errors)
        for k, v in other.examples.items():
            self.examples[k].extend(v)


def classify_spelling(out, gold_word, source):
    o, g, s = macronize.plain(out), macronize.plain(gold_word), macronize.plain(source)
    if rules.unligature(o) == rules.unligature(g):
        return "ligature"
    if o.replace("j", "i").replace("v", "u") == g.replace("j", "i").replace("v", "u"):
        return "j/v"
    if o != s and g == s:
        return "rule over-applied"
    return "respelling missed"


def classify_vowel(out, gold_word, index, how):
    letters = macronize.plain(gold_word)
    vowel_positions = [i for i, c in enumerate(letters) if c in macronize.VOWELS]
    final = index == vowel_positions[-1] if vowel_positions else False
    after = letters[index + 1:index + 3]
    hidden = len(after) == 2 and all(c not in macronize.VOWELS for c in after) and after not in (
        "br", "cr", "dr", "fr", "gr", "pr", "tr", "bl", "cl", "fl", "gl", "pl", "ch", "ph", "th", "qu")
    where = "ending" if final else "hidden" if hidden else "stem"
    missing = index in macronize.long_vowels(gold_word)
    return f"{'missing ā' if missing else 'extra ā'} · {where} · {how}"


def score(output, sources, gold_tokens):
    """Score the output words (with the source words they came from) against the gold, aligned on folds."""
    s = Score(words=len(gold_tokens))
    # Aligned on the spelling-blind reading form, so a respelling (eīs/iīs) is a spelling error, not a word error.
    a = [align.reading(w.word) for w in output]
    b = [align.reading(w) for _, w in gold_tokens]
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "replace" and "".join(a[i1:i2]) == "".join(b[j1:j2]):
            n = j2 - j1                                   # same letters, divided differently (mēcum / mē cum)
            s.word_ok += n
            s.spelled += n
            s.errors["spelling: word division"] += n
            s.examples["spelling: word division"].append(
                f"{gold_tokens[j1][0]} {' '.join(w.word for w in output[i1:i2])} (gold {' '.join(w for _, w in gold_tokens[j1:j2])})")
            continue
        if tag not in ("equal", "replace") or (tag == "replace" and i2 - i1 != j2 - j1):
            s.errors["word: different words"] += max(i2 - i1, j2 - j1)
            s.examples["word: different words"].append(
                f"{gold_tokens[min(j1, len(gold_tokens) - 1)][0]} {' '.join(w.word for w in output[i1:i2]) or '∅'} "
                f"(gold {' '.join(w for _, w in gold_tokens[j1:j2]) or '∅'})")
            continue
        for k in range(i2 - i1):
            out, source = output[i1 + k], sources[i1 + k]
            vid, gold_word = gold_tokens[j1 + k]
            if tag == "replace":
                s.errors["word: different words"] += 1
                s.examples["word: different words"].append(f"{vid} {out.word} (gold {gold_word})")
                continue
            s.word_ok += 1
            s.spelled += 1
            if macronize.plain(out.word) != macronize.plain(gold_word):
                kind = classify_spelling(out.word, gold_word, source)
                s.errors[f"spelling: {kind}"] += 1
                s.examples[f"spelling: {kind}"].append(f"{vid} {source}→{out.word} (gold {gold_word})")
                continue
            s.spelling_ok += 1
            got, want = macronize.long_vowels(rules.unligature(out.word)), macronize.long_vowels(rules.unligature(gold_word))
            letters = macronize.plain(rules.unligature(gold_word))
            vowels = [i for i, c in enumerate(letters) if c in macronize.VOWELS]
            s.vowels += len(vowels)
            wrong = [i for i in vowels if (i in got) != (i in want)]
            s.vowels_ok += len(vowels) - len(wrong)
            s.words_marked_ok += not wrong
            for i in wrong:
                kind = classify_vowel(out.word, rules.unligature(gold_word), i, out.how)
                s.errors[f"macron: {kind}"] += 1
                if len(s.examples[f"macron: {kind}"]) < 40:
                    s.examples[f"macron: {kind}"].append(f"{vid} {out.word} (gold {gold_word})")
    return s


# ---------------------------------------------------------------- the run

def run(names=()):
    """{variant: Score} over the settled books, each scored with what the other books taught."""
    settled = [b.osis for b in books.select(names) if gold.load(b.osis)]
    everything = [b.osis for b in books.BOOKS if gold.load(b.osis)]
    totals = {v: Score() for v in VARIANTS}
    per_book = {}
    by_chapter = ChapterDefaults(everything)
    learned = rules.learn(everything)                     # every pair, for rules learned chapter by chapter
    for osis in settled:
        train = [o for o in everything if o != osis]
        book_rules = word_rules(train)
        defaults = settled_defaults(train)
        rows = gold.load(osis)
        chapters = sorted({tsv.parse_id(vid)[1] for vid in rows})
        source = [(r["id"], w) for r in tsv.read(paths.WITNESSES / "wikisource" / f"{osis}.tsv")
                  if tsv.parse_id(r["id"])[1] in chapters and tsv.parse_id(r["id"])[2] > 0
                  for w in WORD.findall(r["text"])]
        by_book = normalize(source, *book_rules)
        by_chapter_text = [token for c in chapters for token in normalize(
            [t for t in source if tsv.parse_id(t[0])[1] == c], *chapter_rules(learned, f"{osis}.{c}"))]
        lexicon = macronize.lookup([w for _, w in by_book + by_chapter_text])
        hosts = [macronize.split_enclitic(w, lexicon[macronize.key(w)])[0] for _, w in by_book + by_chapter_text]
        lexicon.update(macronize.lookup(hosts))
        gold_tokens = [(vid, w) for vid, row in rows.items() for w in WORD.findall(row["text"])]
        for variant in VARIANTS:
            normalized = by_chapter_text if variant == "D" else by_book
            witness = wordpress_marks(osis, normalized)
            output = macronize_all(normalized, lexicon, variant, defaults, witness, by_chapter)
            # The source word each output word came from (to tell a missed rule from an over-applied one).
            s = score(output, [w for _, w in normalized], gold_tokens)
            per_book[(osis, variant)] = s
            totals[variant].add(s)
    return totals, per_book


def chapter_rules(learned, chapter):
    """(word rules, phrase rules) learned from every settled chapter except `chapter` ("Gen.11")."""
    kept = rules.Learned(pairs=[p for p in learned.pairs if p.where.rsplit(".", 1)[0] != chapter],
                         lexicon=learned.lexicon, gold_words=learned.gold_words)
    return _rule_maps(rules.rule_rows(kept))


def report(totals, per_book):
    pct = lambda a, b: f"{100 * a / b:.2f}%" if b else "–"
    lines = ["# Test harness: normalize and macronize, scored against your finished chapters", "",
             "From the Wikisource text alone (`python -m pipeline harness`). Nothing is scored on what it taught: "
             "A–C learn the spelling rules and your settled forms from the *other books*; D learns them from every "
             "*other chapter* (the realistic case for Matthew 14–28 and the rest of a book already begun). The "
             "spelling rules used are all those in `data/rules/REVIEW.md`, approved or not: this measures what "
             "they would do. Targets (PLAN §6): ≥ 99.5% words, ≥ 99% vowels.", "",
             "| Variant | Words | Spelling | Vowels (macrons) | Words fully marked right |", "|---|---:|---:|---:|---:|"]
    for v in VARIANTS:
        t = totals[v]
        lines.append(f"| {v}: {NAMES[v]} | {pct(t.word_ok, t.words)} | {pct(t.spelling_ok, t.spelled)} | "
                     f"{pct(t.vowels_ok, t.vowels)} | {pct(t.words_marked_ok, t.spelling_ok)} |")
    lines += ["", "**Words**: of all gold words, the same word, spelling aside (what is left: Wikisource slips, which "
              "stage 2 corrects, and wording where 1760/1738 differ from your 1726–27, which decision 1 makes "
              "proposals). **Spelling**: of those, spelt as in your text (æ/œ, j/v, respellings, word division; "
              "capitals aside). **Vowels** and **fully marked**: of the correctly spelt words, each vowel long or not "
              "as in your text.", "", "## By book (variant D)", "",
              "| Book | Words | Spelling | Vowels |", "|---|---:|---:|---:|"]
    for (osis, v), s in per_book.items():
        if v == "D":
            lines.append(f"| {osis} | {pct(s.word_ok, s.words)} | {pct(s.spelling_ok, s.spelled)} | {pct(s.vowels_ok, s.vowels)} |")
    for v in ("A", "D"):
        t = totals[v]
        lines += ["", f"## Commonest errors, variant {v} ({NAMES[v]})", "",
                  "Macron errors read *missing ā* (gold long, output not) or *extra ā*, then where (ending = last "
                  "vowel; hidden = before two consonants; stem), then how the output was decided (lexicon, gaffiot "
                  "= Gaffiot changed a W/M mark, homograph = W/M disagree and nothing chose, chosen = WordPress chose, "
                  "settled = your forms, unknown = no source knows the word).", "",
                  "| Error | Count | Examples |", "|---|---:|---|"]
        for kind, n in t.errors.most_common(25):
            lines.append(f"| {kind} | {n} | {'; '.join(t.examples.get(kind, [])[:4])} |")
    return "\n".join(lines) + "\n"
