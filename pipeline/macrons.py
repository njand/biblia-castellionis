"""Stage 4 on a USFM text that already has macrons (a draft): what the pipeline would mark, word by word, against
what the text marks.

Each word is marked as the harness's variant C does (pipeline.harness): W/M candidates with Gaffiot for stems and
hidden quantities, your settled forms where one marking dominates (≥ 80% in data/gold/), and your 2019 WordPress
macrons choosing among a homograph's markings in context. Where that differs from the text, the difference is a
`Mark`: the verse, the word as written, the pipeline's word, how the pipeline decided (`how`: lexicon, gaffiot,
settled, chosen, homograph, unknown, witness), the lexicon's candidates and the settled counts as evidence.

`rates()` measures, on the settled chapters, how often each `how` is wrong (variant D, leave-one-chapter-out):
the numbers decision 6's auto-apply threshold is judged by."""

import collections
import re
from dataclasses import dataclass, field

from pipeline import books, gold, harness, macronize, rules, tsv

WORD = re.compile(r"[^\W\d_]+")


@dataclass
class Mark:
    vid: str
    written: str
    proposed: str
    how: str
    candidates: list = field(default_factory=list)     # [(form, sources)]
    settled: dict = field(default_factory=dict)        # {form: count} in the gold
    wordpress: str = ""


def tokens_of(usfm, osis):
    """[(verse id, word)] with æ/œ written ae/oe, as the lexicon and harness.macronize_all expect."""
    return [(vid, rules.unligature(w)) for vid, text, *_ in gold.rows(usfm, osis) for w in WORD.findall(text)
            if tsv.parse_id(vid)[2] > 0]


LONG_PREFIX = ("e", "de", "pro", "tra", "se", "re")      # ē|jiciō, trā|jiciō: long by nature before j


def differ(written, proposed, settled):
    """The vowel indices whose length differs, leaving out the vowel before j where the text marks it long and
    either your settled text has the form or it is a long prefix (macronize.finish leaves every vowel before j
    unmarked, as in *ejus*)."""
    mine = macronize.long_vowels(rules.unligature(written))
    theirs = macronize.long_vowels(rules.unligature(proposed))
    letters = macronize.plain(rules.unligature(written))
    out = mine ^ theirs
    return {i for i in out if not (i in mine and i + 1 < len(letters) and letters[i + 1] == "j"
                                   and (written.lower() in settled or letters[:i + 1] in LONG_PREFIX))}


def settled_counts():
    """{lexicon key: Counter of marked forms (lower case)} over every settled book."""
    counts = collections.defaultdict(collections.Counter)
    for book in books.BOOKS:
        for row in gold.load(book.osis).values():
            for w in WORD.findall(row["text"]):
                counts[macronize.key(w)][w.lower()] += 1
    return counts


def compare(usfm, osis):
    """[Mark] for every word whose pipeline marking differs from the text's, and the number of words compared."""
    tokens = tokens_of(usfm, osis)
    everything = [b.osis for b in books.BOOKS if gold.load(b.osis)]
    defaults = harness.settled_defaults(everything)
    lexicon = macronize.lookup([w for _, w in tokens])
    hosts = [macronize.split_enclitic(w, lexicon[macronize.key(w)])[0] for _, w in tokens]
    lexicon.update(macronize.lookup(hosts))
    witness = harness.wordpress_marks(osis, tokens)
    output = harness.macronize_all(tokens, lexicon, "C", defaults, witness)
    counts = settled_counts()
    marks = []
    for index, ((vid, written), out) in enumerate(zip(tokens, output)):
        settled = dict(counts.get(macronize.key(written), {}))
        if not differ(written, out.word, {w.replace("æ", "ae").replace("œ", "oe") for w in settled}):
            continue
        entry = lexicon.get(macronize.key(written), macronize.Entry())
        wp = witness.get(index)
        marks.append(Mark(vid, macronize.ligatures(written), out.word, out.how,
                          [(c.form, c.sources) for c in entry.candidates], settled,
                          macronize.finish(written, wp) if wp is not None else ""))
    return marks, len(tokens)


def rates(names=()):
    """{how: (words, words wrong, vowels, vowels wrong)} over the settled books (variant D), with the totals."""
    everything = [b.osis for b in books.BOOKS if gold.load(b.osis)]
    by_chapter = harness.ChapterDefaults(everything)
    out = collections.defaultdict(lambda: [0, 0, 0, 0])
    for osis in [b.osis for b in books.select(names) if gold.load(b.osis)]:
        rows = gold.load(osis)
        tokens = [(vid, macronize.plain(w)) for vid, row in rows.items() if tsv.parse_id(vid)[2] > 0
                  for w in WORD.findall(row["text"])]
        gold_words = [w for vid, row in rows.items() if tsv.parse_id(vid)[2] > 0 for w in WORD.findall(row["text"])]
        # The gold's own spelling, macrons removed: this measures marking alone, not spelling.
        tokens = [(vid, rules.unligature(w)) for (vid, _), w in zip(tokens, [macronize.plain(g) for g in gold_words])]
        lexicon = macronize.lookup([w for _, w in tokens])
        hosts = [macronize.split_enclitic(w, lexicon[macronize.key(w)])[0] for _, w in tokens]
        lexicon.update(macronize.lookup(hosts))
        witness = harness.wordpress_marks(osis, tokens)
        output = harness.macronize_all(tokens, lexicon, "D", {}, witness, by_chapter)
        for word, want in zip(output, gold_words):
            got_l = macronize.long_vowels(rules.unligature(word.word))
            want_l = macronize.long_vowels(rules.unligature(want))
            letters = macronize.plain(rules.unligature(want))
            vowels = [i for i, c in enumerate(letters) if c in macronize.VOWELS]
            wrong = sum(1 for i in vowels if (i in got_l) != (i in want_l))
            row = out[word.how]
            row[0] += 1
            row[1] += wrong > 0
            row[2] += len(vowels)
            row[3] += wrong
    return dict(out)
