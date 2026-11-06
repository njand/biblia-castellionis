"""Learning the spelling rules: the Wikisource witness against the gold text (macrons removed), word by word.

Each settled book is aligned as a whole (so a verse that moved across a chapter boundary still lines up), on
folded words: lower case, no macrons, æ/œ → ae/oe, j → i, v → u. Every aligned pair is then sorted:

  same        identical once macrons are removed
  ligature    Wikisource ae/oe → gold æ/œ (the brief's rule)
  ligature-kept   gold keeps ae/oe where the ligature rule would write æ/œ (aër-type words, or inconsistency)
  ligature-added  gold writes æ/œ where Wikisource has neither ae nor oe (rare)
  case        only capitals differ (divine names, or a sentence boundary moved by modern punctuation)
  j/v         only consonantal i/j or u/v differ
  respelling  one word for one word, same ending, both forms known to the lexicon: a rule candidate
  ws-error    the Wikisource form is unknown to every lexicon: a transcription slip for collation to catch
  wording     a different word or words: an edition difference (1726–27 vs 1760/1738), proposed for review
  split/join  the same letters, divided differently (me cum → mecum)

Lexicon lookups go through `python -m pipeline latin macron` and are cached in sources/cache/ (git-ignored):
Gaffiot is used to decide, and nothing of its text is written to data/."""

import collections
import difflib
import json
import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import books, gold, latin, paths, tsv

RULES = paths.DATA / "rules"
CALIBRATION = paths.DATA / "calibration"
CACHE = paths.SOURCES / "cache" / "macron.json"
WORD = re.compile(r"[^\W\d_]+")
RULE_HEADER = ("old", "new", "scope", "status", "note")


def unmacron(word):
    decomposed = unicodedata.normalize("NFD", word)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if unicodedata.category(c) != "Mn"))


def fold(word):
    word = unmacron(word).lower().replace("æ", "ae").replace("œ", "oe")
    return word.replace("j", "i").replace("v", "u")


def ligature(word):
    """ae/oe → æ/œ everywhere (the brief's rule, before its exceptions)."""
    for old, new in (("AE", "Æ"), ("Ae", "Æ"), ("ae", "æ"), ("OE", "Œ"), ("Oe", "Œ"), ("oe", "œ")):
        word = word.replace(old, new)
    return word


def unligature(word):
    return word.replace("æ", "ae").replace("Æ", "Ae").replace("œ", "oe").replace("Œ", "Oe")


@dataclass
class Pair:
    kind: str
    old: str            # Wikisource (as transcribed)
    new: str            # gold, macrons removed
    where: str          # gold verse id (or the nearest one, for an omission)
    raw: str = ""       # the gold word as printed (with macrons)


# ---------------------------------------------------------------- lexicon lookups

def lookup(forms):
    """{form: {"known": bool, "lemmas": [folded], "gaffiot": [headwords, folded]}} for lower-case forms, cached."""
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    missing = sorted({f for f in forms if "lemmas" not in cache.get(f, {})})
    for start in range(0, len(missing), 40):
        batch = missing[start:start + 40]
        code, out = latin.run(["macron", *batch], capture=True)
        blocks = [b for b in re.split(r"\n\s*\n", out.strip()) if b.strip()]
        if code != 0 or len(blocks) != len(batch):
            blocks = [latin.run(["macron", form], capture=True)[1] for form in batch]
        for form, block in zip(batch, blocks):
            gaffiot = re.search(r"^\s*G Gaffiot: (.*)$", block, re.MULTILINE)
            heads = [fold(re.split(r"[,\[]", head)[0].strip()) for head in gaffiot.group(1).split(" · ")] if gaffiot else []
            known = "no source knows this form" not in block
            lemmas = {fold(name) for line in re.findall(r"← (.*)$", block, re.MULTILINE)
                      for name in re.findall(r"([^\s,(]+) \(", line)}
            heads = [h for h in heads if h and h != "…"]
            cache[form] = {"known": known, "lemmas": sorted(lemmas | set(heads)), "gaffiot": heads}
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0, sort_keys=True), encoding="utf-8")
    return cache


# ---------------------------------------------------------------- alignment

def words(rows, chapters):
    """[(verse id, word)] of the rows in the given chapters, in order (verse 0 left out)."""
    out = []
    for vid, text in rows:
        osis, chapter, verse = tsv.parse_id(vid)
        if verse and chapter in chapters:
            out.extend((vid, word) for word in WORD.findall(text))
    return out


def align(witness, target):
    """Pairs for two [(verse id, word)] lists; the verse ids of `target` (the gold) locate each pair."""
    a, b = [fold(w) for _, w in witness], [fold(w) for _, w in target]
    pairs = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        where = target[j1][0] if j1 < len(target) else target[-1][0]
        if tag == "equal":
            pairs.extend(_classify_equal(w, g, vid) for (_, w), (vid, g) in zip(witness[i1:i2], target[j1:j2]))
        elif tag == "replace" and i2 - i1 == j2 - j1:
            pairs.extend(Pair("replace", w, unmacron(g), vid) for (_, w), (vid, g) in zip(witness[i1:i2], target[j1:j2]))
        elif tag == "replace" and "".join(a[i1:i2]) == "".join(b[j1:j2]):
            pairs.append(Pair("split/join", " ".join(w for _, w in witness[i1:i2]),
                              " ".join(unmacron(g) for _, g in target[j1:j2]), where))
        else:
            pairs.append(Pair("wording", " ".join(w for _, w in witness[i1:i2]),
                              " ".join(unmacron(g) for _, g in target[j1:j2]), where))
    return pairs


def _classify_equal(old, raw, where):
    """Kind of a pair whose folded forms agree. The ligature rule is applied to Wikisource first, so a word both
    spell `foedus` counts as ligature-kept (the rule would have written fœdus), not as same."""
    new, expected = unmacron(raw), ligature(old)
    if expected == new:
        kind = "same" if old == new else "ligature"
    elif expected.lower() == new.lower():
        kind = "case"
    elif unligature(expected).lower() == unligature(new).lower():
        ligatures = lambda word: sum(word.lower().count(c) for c in "æœ")
        kind = "ligature-kept" if ligatures(new) < ligatures(expected) else "ligature-added"
    else:
        kind = "j/v"
    return Pair(kind, old, new, where, raw)


def hiatus(raw):
    """True if a gold word's ae/oe is two syllables, not a diphthong: a macron on either vowel (Isrāēl, hērōes,
    āër), a diaeresis, or a co- compound (coeō, coemō, coerceō) other than coepī."""
    word = raw.lower()
    if re.search(r"[āōë]e|a[ēë]|o[ēë]|[āō][ēe]", word):
        return True
    return word.startswith("coe") and not word.startswith("coep")


def _edit(old, new):
    """(changed part of old, changed part of new, prefix, suffix) after removing the common ends."""
    start = 0
    while start < min(len(old), len(new)) and old[start] == new[start]:
        start += 1
    end = 0
    while end < min(len(old), len(new)) - start and old[-1 - end] == new[-1 - end]:
        end += 1
    return old[start:len(old) - end], new[start:len(new) - end], old[:start], old[len(old) - end:]


def sort_replacements(pairs):
    """Turn each one-for-one `replace` into respelling, ws-error or wording, using the lexicon."""
    lexicon = lookup({key(p.old) for p in pairs if p.kind == "replace"} | {key(p.new) for p in pairs if p.kind == "replace"})
    for p in pairs:
        if p.kind != "replace":
            continue
        old, new = lexicon[key(p.old)], lexicon[key(p.new)]
        stem_old, stem_new = fold(p.old), fold(p.new)
        if stem_old.endswith("que") and stem_new.endswith("que"):
            stem_old, stem_new = stem_old[:-3], stem_new[:-3]
        changed_old, changed_new, _, suffix = _edit(stem_old, stem_new)
        lemmas = lambda entry: {variant_key(lemma) for lemma in entry["lemmas"]}
        one_lemma = not (old["known"] and new["known"]) or bool(lemmas(old) & lemmas(new))
        if not old["known"] and new["known"] or {changed_old, changed_new} in OCR_CONFUSIONS:
            p.kind = "ws-error"
        elif suffix and (changed_old, changed_new) in SPELLING_EDITS or                 len(suffix) >= 2 and len(changed_old) <= 3 and len(changed_new) <= 3 and one_lemma:
            p.kind = "respelling"           # a known alternation, or a small change inside one word
        else:
            p.kind = "wording"              # another word, or another form of it (et/est, dissident/dissidet)
    return lexicon


def key(form):
    """The lexicon's spelling of a form: lower case, ae/oe for æ/œ."""
    return unligature(form).lower()


# Changes (folded old → new letters, the word's ending untouched) that are spellings of one word, never another
# word or form: im(m)o, as(s)um(p)tus, h-, vi(g→c)esimus, s(o→u)boles, d(i→e)versorium, n(a)e, con(n)ubium,
# conju(n)x, se(x→s)centi, quer(c→qu)etum, collegi(i).
SPELLING_EDITS = {("", "m"), ("", "p"), ("", "t"), ("", "n"), ("", "h"), ("h", ""), ("g", "c"),
                  ("o", "u"), ("i", "e"), ("e", "i"), ("a", ""), ("", "a"), ("x", "s"), ("c", "qu"), ("i", "")}

# Letters a scan or transcriber confuses (long s and f, c and e, l and i): a pair that differs only so is a
# transcription slip even when both forms are Latin words (sit/fit, cum/eum, ilia/illa).
OCR_CONFUSIONS = [{"s", "f"}, {"c", "e"}, {"i", "l"}, {"n", "u"}, {"rn", "m"}]


def gaffiot_side(form, edit_prefix, edit_new, lexicon):
    """True if a Gaffiot headword for `form` begins like the form up to and including its changed letters."""
    heads = lexicon.get(key(form), {}).get("gaffiot", [])
    stem = fold(form)[:max(4, len(edit_prefix) + len(edit_new) + 1)]
    return any(head.startswith(stem) for head in heads)


def gaffiot_verdict(old, new, lexicon):
    """Which spelling Gaffiot's headwords use: "new", "old", "both" or "no headword found"."""
    o, n, prefix, _ = _edit(fold(old), fold(new))
    sides = [name for name, form, changed in (("old", old, o), ("new", new, n)) if gaffiot_side(form, prefix, changed, lexicon)]
    return {0: "no headword found", 1: sides[0] if sides else "", 2: "both"}[len(sides)]


# ---------------------------------------------------------------- the whole comparison

@dataclass
class Learned:
    pairs: list = field(default_factory=list)
    lexicon: dict = field(default_factory=dict)
    gold_words: int = 0


def learn(names=()):
    """Align Wikisource with the gold text for every settled book; sort every difference."""
    result = Learned()
    for book in books.select(names):
        rows = gold.load(book.osis)
        path = paths.WITNESSES / "wikisource" / f"{book.osis}.tsv"
        if not rows or not path.exists():
            continue
        chapters = {tsv.parse_id(vid)[1] for vid in rows}
        target = words([(vid, row["text"]) for vid, row in rows.items()], chapters)
        witness = words([(row["id"], row["text"]) for row in tsv.read(path)], chapters)
        result.pairs.extend(align(witness, target))
        result.gold_words += len(target)
    result.lexicon = sort_replacements(result.pairs)
    return result


def rule_rows(learned):
    """Proposed rules: [(old, new, scope, status, note)], mechanical patterns first, then words and phrases."""
    pairs = learned.pairs
    counts = collections.Counter(p.kind for p in pairs)
    # What each Wikisource form became in the gold, to see whether a respelling was applied every time.
    became = collections.defaultdict(lambda: collections.defaultdict(list))
    for p in pairs:
        if " " not in p.old and " " not in p.new and p.kind not in ("wording", "ws-error"):
            became[ligature(p.old).lower()][p.new.lower()].append(p.where)
    rows = []
    kept = collections.Counter(p.new.lower() for p in pairs if p.kind == "ligature-kept")
    rows.append(("ae", "æ", "pattern", "proposed",
                 f"diphthong ae → æ: {counts['ligature']} words in the gold follow it; gold keeps ae/oe in "
                 f"{counts['ligature-kept']} ({', '.join(f'{w} {n}×' for w, n in kept.most_common(8))})"))
    rows.append(("oe", "œ", "pattern", "proposed", "diphthong oe → œ, with the same exceptions list (aër, poëta …)"))
    jv = [p for p in pairs if p.kind == "j/v"]
    rows.append(("i", "j", "pattern", "proposed",
                 f"consonantal i → j (e-liber's orthography.jv rules): {len(jv)} gold words differ from Wikisource "
                 f"only in i/j or u/v, e.g. " + ", ".join(sorted({f"{p.old}→{p.new}" for p in jv})[:6])))
    respell = collections.defaultdict(list)
    for p in pairs:
        if p.kind == "respelling":
            respell[(ligature(p.old).lower(), p.new.lower())].append(p.where)
    for (old, new), where in sorted(respell.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        note = f"{len(where)}× ({_ids(where)}); Gaffiot headword: {gaffiot_verdict(old, new, learned.lexicon)}"
        unchanged = became[old].get(old)
        if unchanged:
            note += f"; but {old} kept {len(unchanged)}× ({_ids(unchanged)}): inconsistent"
        rows.append((old, new, "word", "proposed", note))
    joins = collections.defaultdict(list)
    for p in pairs:
        if p.kind == "split/join":
            joins[(ligature(p.old).lower(), p.new.lower())].append(p.where)
    for (old, new), where in sorted(joins.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        rows.append((old, new, "phrase", "proposed", f"{len(where)}× ({_ids(where)})"))
    return rows


def _ids(where, limit=4):
    return ", ".join(where[:limit]) + (", …" if len(where) > limit else "")


def families(rows):
    """{(changed letters old → new): [(old, new)]} for word rules that share an edit: candidates to generalize."""
    found = collections.defaultdict(list)
    for old, new, scope, *_ in rows:
        if scope == "word":
            o, n, _, _ = _edit(old, new)
            found[(o, n)].append((old, new))
    return {edit: members for edit, members in found.items() if len(members) > 1}


# ---------------------------------------------------------------- inconsistencies inside the gold text

def variant_key(word):
    """A key that is equal for spellings of one word that differ only by the alternations the edition decides:
    æ/ae (and æ/e inside a word), œ/oe, i/j, u/v, ejic/eic, h-, mpt/mt/nt, lct/lt, ci/ti before a vowel,
    quidq/quicq, and tt/pp/mm/nn (quat(t)uor, rep(p)erit, im(m)o, con(n)ubium)."""
    w = unmacron(word).lower().replace("æ", "ae").replace("œ", "oe").replace("j", "i").replace("v", "u")
    w = re.sub(r"^h", "", w)
    w = w.replace("quicq", "quidq").replace("mpt", "nt").replace("mt", "nt").replace("iic", "ic").replace("lct", "lt")
    w = re.sub(r"ti(?=[aeiou])", "ci", w)
    w = re.sub(r"(tt|pp|mm|nn)", lambda m: m.group()[0], w)
    return re.sub(r"[ao]e(?!$)", "e", w)


def gold_variants(names=()):
    """[(key, {spelling: [verse ids]})] for words the gold spells more than one way (macrons and capitals aside).
    Spellings whose lemmas the lexicon keeps apart (hostium/ostium, hōra/ōra) are not counted as variants."""
    groups = collections.defaultdict(lambda: collections.defaultdict(list))
    for book in books.select(names):
        for vid, row in gold.load(book.osis).items():
            for word in WORD.findall(row["text"]):
                groups[variant_key(word)][unmacron(word).lower()].append(vid)
    candidates = {key: dict(spellings) for key, spellings in groups.items() if len(spellings) > 1}
    lexicon = lookup({unligature(s) for spellings in candidates.values() for s in spellings})
    lexicon = {s: lexicon[unligature(s)] for spellings in candidates.values() for s in spellings}

    distinct = {frozenset((row["a"], row["b"])) for row in tsv.read(RULES / "distinct.tsv")} \
        if (RULES / "distinct.tsv").exists() else set()

    def same_word(a, b):
        if frozenset((a, b)) in distinct:
            return False                                   # data/rules/distinct.tsv: decided to be different words
        if strict_key(a) == strict_key(b):
            return True                                    # ligature, i/j, mpt/nt, quicq/quidq, ti/ci: unambiguous
        lemmas_a, lemmas_b = set(lexicon[a]["lemmas"]), set(lexicon[b]["lemmas"])
        if not lexicon[a]["known"] or not lexicon[b]["known"]:
            return True                                    # one is unknown to every lexicon: perhaps a slip
        return bool(lemmas_a & lemmas_b)                   # hōra/ōra, hīs/is, cēpit/cœpit are different words

    found = []
    for key, spellings in candidates.items():
        clusters = []
        for spelling in spellings:
            home = next((c for c in clusters if any(same_word(spelling, other) for other in c)), None)
            (home.append(spelling) if home is not None else clusters.append([spelling]))
        found.extend((key, {s: spellings[s] for s in cluster}) for cluster in clusters if len(cluster) > 1)
    return sorted(found, key=lambda kv: -sum(len(v) for v in kv[1].values()))


def strict_key(word):
    """Only the alternations that never change the word: æ/ae, œ/oe, i/j, u/v, ejic/eic, mpt/nt, quicq/quidq,
    ti/ci before a vowel."""
    w = unmacron(word).lower().replace("æ", "ae").replace("œ", "oe").replace("j", "i").replace("v", "u")
    w = w.replace("quicq", "quidq").replace("mpt", "nt").replace("iic", "ic")
    return re.sub(r"ti(?=[aeiou])", "ci", w)


DIVINE = ("pater", "patr", "fili", "spirit", "sanct", "domin", "suprem", "sermo", "servator", "divin", "hominis",
          "cælest")


def divine_capitals(names=()):
    """[(word, capitalized ids, lower-case ids)] for words that can name God, where the less frequent of the two
    spellings occurs at most three times: the places to check (Pater for God, pater for a man, both correct)."""
    out = []
    for word, (upper, lower) in capital_variants(names).items():
        if word.startswith(DIVINE) and min(len(upper), len(lower)) <= 3:
            out.append((word, upper, lower))
    return sorted(out)


def lowered_names(pairs):
    """{gold form: [verse ids]} where Wikisource capitalizes a word the gold begins with a lower-case æ/œ
    (Aegyptum → ægyptum): the ae → æ conversion lost the capital."""
    found = collections.defaultdict(list)
    for p in pairs:
        if p.kind == "case" and p.old[:2] in ("Ae", "Oe", "AE", "OE") and p.new[:1] in ("æ", "œ"):
            found[p.new].append(p.where)
    return dict(found)


def capital_variants(names=()):
    """{word: (capitalized ids, lower-case ids)} for words written both ways in the middle of a sentence."""
    seen = collections.defaultdict(lambda: ([], []))
    for book in books.select(names):
        for vid, row in gold.load(book.osis).items():
            for match in WORD.finditer(row["text"]):
                before = row["text"][:match.start()].rstrip(" (")
                if not before or before[-1] in ".?!:;—“‘":
                    continue                                   # sentence, clause or speech start: capitals vary
                word = unmacron(match.group())
                seen[word.lower()][0 if word[0].isupper() else 1].append(vid)
    return {w: ids for w, ids in seen.items() if ids[0] and ids[1]}


# ---------------------------------------------------------------- files

def write_rules(rows):
    """data/rules/orthography.tsv, keeping the status (approved/rejected) of rules already there."""
    path = RULES / "orthography.tsv"
    previous = {(r["old"], r["new"], r["scope"]): r for r in tsv.read(path)} if path.exists() else {}
    merged = []
    for old, new, scope, status, note in rows:
        earlier = previous.pop((old, new, scope), None)
        merged.append((old, new, scope, earlier["status"] if earlier else status, note))
    merged.extend((r["old"], r["new"], r["scope"], r["status"], r["note"]) for r in previous.values())
    tsv.write(path, merged, header=RULE_HEADER)
    return path


def load_rules(status="approved"):
    path = RULES / "orthography.tsv"
    return [r for r in tsv.read(path) if r["status"] == status] if path.exists() else []


def write_calibration(pairs):
    """data/calibration/wikisource.tsv: every difference between Wikisource and the gold, with its kind."""
    path = CALIBRATION / "wikisource.tsv"
    rows = [(p.where, p.kind, p.old, p.new) for p in pairs if p.kind != "same"]
    tsv.write(path, rows, header=("id", "kind", "wikisource", "gold"))
    return path


KIND_MEANING = {
    "same": "identical", "ligature": "ae/oe → æ/œ",
    "case": "capitals only (mostly sentence boundaries moved by modern punctuation; divine titles)",
    "respelling": "spelling rule candidates (§3)", "ligature-kept": "ae/oe kept where the ligature rule would write æ/œ (§1)",
    "wording": "a different word: edition difference or Wikisource slip (§6; not a rule)",
    "split/join": "word division (§4)", "ws-error": "Wikisource transcription slip (§6; stage 2 corrects these)",
    "j/v": "consonantal i/j (§2)"}


def review(learned, names=()):
    """The text of data/rules/REVIEW.md: the rules and the inconsistencies, each with a Decision line."""
    pairs, rows = learned.pairs, rule_rows(learned)
    counts = collections.Counter(p.kind for p in pairs)
    total = learned.gold_words
    kept = [p for p in pairs if p.kind == "ligature-kept"]
    hiatus_words = collections.Counter(p.raw for p in kept if hiatus(p.raw))
    diphthongs = collections.Counter(p.raw for p in kept if not hiatus(p.raw))
    jv = sorted({f"*{p.old}* → *{p.new}*" for p in pairs if p.kind == "j/v"})
    lines = [
        "# Spelling rules learned from the finished chapters", "",
        f"Wikisource against the gold text (macrons removed): {total:,} gold words. Generated by "
        "`python -m pipeline rules`; the rules themselves are in `orthography.tsv`, all `proposed` until you "
        "approve them. Write your answer after each **Decision:**.", "",
        "| Kind | Words | Share | What it is |", "|---|---:|---:|---|"]
    lines += [f"| {kind} | {n:,} | {100 * n / total:.2f}% | {KIND_MEANING.get(kind, '')} |" for kind, n in counts.most_common()]
    lines += [
        "", "## 1. Ligatures", "",
        f"**ae → æ, oe → œ** for diphthongs: {counts['ligature']:,} gold words follow it. Exceptions, where your "
        "macrons show two syllables, so no ligature:", "",
        "- " + ", ".join(f"*{w}* {n}×" for w, n in hiatus_words.most_common()), "",
        "These are diphthongs (no macron on either vowel; Gaffiot writes œ), yet your text has oe:", "",
        "- " + ", ".join(f"*{w}* {n}×" for w, n in diphthongs.most_common()), "",
        "**Decision:** œ in *fœdus, pœna, prœlium, cœpī* (as Gaffiot and the brief), or keep oe in these words? ", "",
        "## 2. Consonantal i → j", "",
        f"{counts['j/v']} gold words differ from Wikisource only in i/j (its Genesis writes *iniuria, adiumentum*): "
        + ", ".join(jv) + ".", "",
        "Rule: j for consonantal i, by e-liber's `orthography.jv` rules. **Decision:** ", "",
        "## 3. Word respellings", "",
        "Wikisource → your text, how often, and which spelling Gaffiot's headwords use (`both`: it has an entry "
        "for each). The Gaffiot column compares headwords, so it says little about inflected forms (*eīs* and "
        "*iīs* both belong to *is*). *Inconsistent*: your text also keeps the old form.", "",
        "| Old | New | Seen | Gaffiot | Note |", "|---|---|---|---|---|"]
    for old, new, scope, status, note in rows:
        if scope == "word":
            seen, _, rest = note.partition("; Gaffiot headword: ")
            verdict, _, extra = rest.partition("; ")
            lines.append(f"| {old} | {new} | {seen} | {verdict} | {extra} |")
    lines += ["", "Groups that could become one rule each (approve a group to cover forms not seen yet):", ""]
    for (o, n), members in sorted(families(rows).items(), key=lambda kv: -len(kv[1])):
        lines.append(f"- **{o or '∅'} → {n or '∅'}**: " + ", ".join(f"{a}→{b}" for a, b in members))
    lines += ["", "**Decision:** (approve all, or name the rows and groups to reject) ", "",
              "## 4. Word division", "", "| Old | New | Seen |", "|---|---|---|"]
    lines += [f"| {old} | {new} | {note} |" for old, new, scope, status, note in rows if scope == "phrase"]
    lines += ["", "Both directions occur: *bene facere → benefacere*, but *maledīxerit → male dīxerit*, "
              "*jampridem → jam prīdem*, *tamdiu → tam diū*. **Decision:** ", "",
              "## 5. Inconsistencies inside your text", "",
              "The same word spelled more than one way in the finished chapters (macrons and capitals aside; "
              "pairs listed in `distinct.tsv` are different words and left out):", "",
              "| Spellings | Where |", "|---|---|"]
    for _, spellings in gold_variants(names):
        lines.append("| " + " / ".join(f"*{s}* {len(v)}×" for s, v in spellings.items()) + " | "
                     + "; ".join(f"{s}: {_ids(v, 3)}" for s, v in spellings.items()) + " |")
    slips = [p for p in pairs if p.kind == "wording" and not p.old and len(p.new) == 1 and p.new.lower() not in "aeō"]
    if slips:
        lines += ["", "**Probable slips in your text** (letters that are no word, absent from Wikisource): "
                  + "; ".join(f"{p.where} stray *{p.new}*" for p in slips) + "."]
    lowered = lowered_names(pairs)
    lines += ["", f"**Proper names lower-cased by the æ conversion** ({sum(map(len, lowered.values()))} words; "
              "Wikisource has the capital): " + "; ".join(f"*{w}* ({_ids(v, 3)})" for w, v in lowered.items()) + ".",
              "", "**Capitals for God**, where the rarer spelling may be a slip (a man's *pater* is rightly lower "
              "case; only words written both ways mid-sentence, rarer side ≤ 3):", "",
              "| Word | Capital | Lower case |", "|---|---|---|"]
    for word, upper, lower in divine_capitals(names):
        lines.append(f"| {word} | {len(upper)}× ({_ids(upper, 3)}) | {len(lower)}× ({_ids(lower, 3)}) |")
    lines += ["", "**Decision:** (which spelling for each line; the pipeline then proposes the fixes to the USFM) ",
              "", "## 6. Not spelling: for later stages", "",
              f"- **Wikisource slips** ({counts['ws-error']}): " + ", ".join(
                  f"{p.where} *{p.old}* → *{p.new}*" for p in pairs if p.kind == "ws-error") + ".",
              f"- **Wording** ({counts['wording']}): your text (1726–27) and Wikisource (1760 NT, 1738 OT) read "
              "differently. Under decision 1 these become proposals, never automatic changes: " + ", ".join(
                  f"{p.where} *{p.old or '∅'}* → *{p.new or '∅'}*" for p in pairs if p.kind == "wording") + ".", ""]
    return "\n".join(lines)


def write_review(text):
    path = RULES / "REVIEW.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return path
