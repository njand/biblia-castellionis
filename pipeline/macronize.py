"""Stage 4: macrons, from the lexicon (`python -m pipeline latin macron`): W = Wiktionary and M = Macronizer give
the candidate forms; Gaffiot's headword decides the stem and hidden quantities wherever it marks them; W/M
decide endings. A form with more than one candidate left is a homograph, decided by `prefer` (settled forms,
or the WordPress witness in context) or left to review.

Also here: consonantal j/v (after e-liber's `orthography.jv`), the vowel before j left unmarked (*ejus*), and
the ligatures æ/œ, written only where the chosen macrons show a diphthong (not *āēr*, *Isrāēl*).

Lookups are cached in sources/cache/lexicon.json (git-ignored): Gaffiot's headwords are used, never stored in
data/."""

import json
import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import latin, paths

CACHE = paths.SOURCES / "cache" / "lexicon.json"
VOWELS = "aeiouy"
LONG = dict(zip("aeiouyAEIOUY", "āēīōūȳĀĒĪŌŪȲ"))
SHORT_FINAL = {"mihi", "tibi", "sibi", "ubi", "ibi"}          # brief: final -i short in these
UNCERTAIN = "̆̈"                                   # a breve after a macron, a diaeresis
LINE = re.compile(r"^(\S+)\s+\[([MW]+)\]\s+←\s+(.*)$")


def nfc(text):
    return unicodedata.normalize("NFC", text)


def plain(word):
    """Without any marks (macrons, breves, diaeresis), lower case."""
    return nfc("".join(c for c in unicodedata.normalize("NFD", word) if unicodedata.category(c) != "Mn")).lower()


def key(word):
    """The lexicon's key: no marks, lower case, j → i, v → u, æ/œ → ae/oe."""
    return plain(word).replace("æ", "ae").replace("œ", "oe").replace("j", "i").replace("v", "u")


def quantities(word):
    """[(vowel index in the plain word, 'L' long / 'S' short / '?' uncertain / '' unmarked)] for each vowel."""
    out, index = [], 0
    for char in unicodedata.normalize("NFD", nfc(word)):
        if unicodedata.category(char) == "Mn":
            if out and out[-1][0] == index - 1:
                mark = {"̄": "L", "̆": "S"}.get(char, "")
                if char == "̆" and out[-1][1] == "L":
                    mark = "?"
                if mark:
                    out[-1] = (out[-1][0], mark)
            continue
        if char.lower() in VOWELS:
            out.append((index, ""))
        index += 1
    return out


def long_vowels(word):
    """Indices (in the plain word) of the vowels marked long."""
    return {i for i, mark in quantities(word) if mark == "L"}


def mark(word, longs):
    """The plain letters of `word` (case kept) with a macron on each index in `longs` and none elsewhere."""
    letters = nfc("".join(c for c in unicodedata.normalize("NFD", nfc(word)) if unicodedata.category(c) != "Mn"))
    return "".join(LONG[c] if i in longs and c in LONG else c for i, c in enumerate(letters))


@dataclass
class Candidate:
    form: str
    sources: str
    lemmas: list = field(default_factory=list)


@dataclass
class Entry:
    candidates: list = field(default_factory=list)
    gaffiot: list = field(default_factory=list)       # headwords with Gaffiot's marks


def parse(block):
    entry = Entry()
    for line in block.splitlines():
        match = LINE.match(line)
        if match:
            form, sources, rest = match.groups()
            lemmas = [nfc(name) for name in re.findall(r"([^\s,(]+) \(", rest)]
            entry.candidates.append(Candidate(nfc(form), sources, lemmas))
        elif line.strip().startswith("G Gaffiot:"):
            for head in line.split(":", 1)[1].split(" · "):
                head = re.sub(r"\[.*?\]|\(.*?\)", "", head).strip()
                parts = [nfc(p.strip()) for p in head.split(",") if p.strip() and p.strip() != "…"]
                if parts:
                    entry.gaffiot.append(parts)          # headword, then principal parts (vĕnĭō, vēnī, …)
    return entry


def lookup(forms):
    """{key: Entry} for words (any spelling), cached; looks up the forms not yet cached, 40 at a time."""
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    wanted = sorted({key(f) for f in forms} - set(cache))
    for start in range(0, len(wanted), 40):
        batch = wanted[start:start + 40]
        code, out = latin.run(["macron", *batch], capture=True)
        blocks = [b for b in re.split(r"\n\s*\n", out.strip()) if b.strip()]
        if code != 0 or len(blocks) != len(batch):
            blocks = [latin.run(["macron", form], capture=True)[1] for form in batch]
        cache.update(zip(batch, blocks))
        if start % 400 == 0:
            CACHE.parent.mkdir(parents=True, exist_ok=True)
            CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    return {k: parse(cache[k]) for k in {key(f) for f in forms}}


# ---------------------------------------------------------------- choosing

def gaffiot_stem(candidate, heads):
    """{plain index: 'L'/'S'} that Gaffiot marks in this candidate's stem: from the headword and principal parts
    of the candidate's lemma (or of every entry, if none is its lemma), each counting only the stem it shares
    with the word, before its own last vowel group. Where the parts disagree (vĕniō, vēnī) Gaffiot is silent."""
    word = key(candidate.form)
    # Wiktionary lists a form as its own lemma (esse ← esse); that would match ēsse, 'to eat', for esse, 'to be'.
    lemmas = {key(lemma) for lemma in candidate.lemmas} - {word} or {word}
    entries = [parts for parts in heads if key(parts[0]) in lemmas] or (heads if len(heads) == 1 else [])
    # Only the part(s) that match the word best vote: the headword or a principal part, which may follow the
    # headword's prefix (impōnō, pŏsŭī: im|posuisset). A part matching fewer than 3 letters is an ending.
    scored = []
    for parts in entries:
        head_key = key(parts[0])
        for number, part in enumerate(parts):
            part_key = key(part)
            # An abbreviated ending (ēre, ĕdis, ōnis) has no stem to share: never aligned inside the word.
            offsets = [0] + [k for k in range(1, 5) if number and plain(part)[:1] not in VOWELS + "æœ"
                             and word[:k] == head_key[:k]]
            for offset in offsets:
                shared = 0
                while shared < min(len(word) - offset, len(part_key)) and word[offset + shared] == part_key[shared]:
                    shared += 1
                if shared >= 3:
                    scored.append((offset + shared, offset, shared, part))
    if not scored:
        return {}
    best = max(total for total, *_ in scored)
    word_groups = [m.start() for m in re.finditer(r"[aeiouy]+", word)]
    ending = word_groups[-1] if word_groups else len(word)    # Gaffiot never decides the word's last syllable
    votes, heard = {}, {}
    for total, offset, shared, part in scored:
        part = part.replace("æ", "ae").replace("Æ", "Ae").replace("œ", "oe").replace("Œ", "Oe")
        part_key = key(part)
        groups = [(m.start(), m.end()) for m in re.finditer(r"[aeiouy]+", part_key)]
        for i, m in quantities(part):
            if m not in ("L", "S") or offset + i >= ending:
                continue
            after = next((start for start, _ in groups if start > i), None)
            if after is None or groups[-1][0] <= i:
                continue                                  # the part's own last syllable: its ending
            # A vowel's quantity holds only in the same syllable: the consonants after it must be the word's too
            # (stāre is no evidence for stantēs, intellĕgō none for intellēxit). Every part sharing that much is
            # heard; only the best-matching parts, sharing the next vowel as well, vote.
            consonants_end = next(end for start, end in groups if start <= i < end)
            if after <= shared:
                heard.setdefault(offset + i, set()).add(m)
            if total == best and after < shared and consonants_end <= shared:
                votes.setdefault(offset + i, set()).add(m)
    # Where a part sharing the syllable disagrees (vĭdĕō, vīdī: vīderant), Gaffiot is silent.
    return {i: marks.pop() for i, marks in votes.items() if len(marks) == 1 and heard[i] == marks}


def with_gaffiot(candidate, heads):
    """The candidate's long vowels with Gaffiot's stem marks applied (Gaffiot first for stems and hidden
    quantities), and how many marks Gaffiot changed."""
    longs = {i for i, m in quantities(candidate.form) if m == "L"}
    uncertain = {i for i, m in quantities(candidate.form) if m == "?"}
    changed = 0
    for i, m in gaffiot_stem(candidate, heads).items():
        if m == "L" and i not in longs:
            longs.add(i)
            changed += i not in uncertain
        elif m == "S" and i in longs:
            longs.discard(i)
            changed += i not in uncertain
    for i in uncertain - set(gaffiot_stem(candidate, heads)):
        longs.discard(i)                                  # quantity uncertain and Gaffiot silent: unmarked
    return frozenset(longs), changed


@dataclass
class Choice:
    longs: frozenset = frozenset()
    how: str = ""          # lexicon, gaffiot, homograph, default, witness, unknown
    options: tuple = ()    # the distinct markings left when it was a homograph


def choose(word, entry, prefer=None):
    """The long vowels for `word` (its plain letters), from the lexicon entry; `prefer(options)` picks one of
    several markings (frozensets of indices) or returns None."""
    candidates = entry.candidates
    if word[:1].isupper() and any(c.form[:1].isupper() for c in candidates):
        candidates = [c for c in candidates if c.form[:1].isupper()]
    if len(plain(word)) and candidates:
        candidates = [c for c in candidates if len(key(c.form)) == len(key(word))] or candidates
    # A diaeresis (W's Israël) only notes the hiatus another candidate marks with macrons (Isrāēl); taken
    # alone, it would lose its mark and let ae become æ (Isræl).
    candidates = [c for c in candidates if "̈" not in unicodedata.normalize("NFD", c.form)] or candidates
    if not candidates:
        return Choice(how="unknown")
    options = {}
    for candidate in candidates:
        longs, _ = with_gaffiot(candidate, entry.gaffiot)
        options.setdefault(longs, candidate)
    as_given = {frozenset(i for i, m in quantities(c.form) if m == "L") for c in candidates}
    if len(options) == 1:
        longs = next(iter(options))
        return Choice(longs, "lexicon" if longs in as_given else "gaffiot")
    picked = prefer(tuple(options)) if prefer else None
    if picked is not None:
        return Choice(picked, "chosen", tuple(options))
    with_w = [longs for longs, c in options.items() if "W" in c.sources]
    return Choice((with_w or list(options))[0], "homograph", tuple(options))


def finish(word, longs):
    """The word marked: input letters kept (j, v and case from the text), final -i short in mihi/tibi/…,
    the vowel before j unmarked, æ/œ for diphthongs."""
    letters = plain(word)
    if letters in SHORT_FINAL:
        longs = set(longs) - {len(letters) - 1}
    longs = {i for i in longs if not (i + 1 < len(letters) and letters[i + 1] == "j")}
    if m := LONG_BEFORE_J.match(letters):              # ē|jiciō, trā|jēcit: long by nature (50 of 50 settled)
        longs.add(m.end(1) - 1)
    marked = mark(word, longs)
    return ligatures(marked)


def ligatures(word):
    """ae → æ, oe → œ where neither vowel is marked (a diphthong), in a word already macronized (a long vowel
    before it does not matter: Marīæ, Nōæ)."""
    out = re.sub(r"([Aa])e(?![̄̈])|AE(?![̄̈])", lambda m: "Æ" if m.group()[0] == "A" else "æ", nfc(word))
    out = re.sub(r"([Oo])e(?![̄̈])|OE(?![̄̈])", lambda m: "Œ" if m.group()[0] == "O" else "œ", out)
    return out


def jv(word):
    """Consonantal i → j and u → v, after e-liber's rules (initial i before a vowel, i between vowels, u
    between vowels or initial before a vowel; not after q/g)."""
    letters = plain(word)
    if letters in JV_KEEP:
        return word
    out = list(word)

    def vowel(i):
        if not 0 <= i < len(letters) or letters[i] not in VOWELS:
            return False
        return not (letters[i] == "u" and i > 0 and letters[i - 1] in "qg" and i + 1 < len(letters))

    for i, c in enumerate(letters):
        if c == "i" and vowel(i + 1) and (i == 0 or vowel(i - 1)) and (i + 1 >= len(letters) or letters[i + 1] != "i"):
            if i == 0 and letters.startswith(("iamb", "ion", "ias", "iap", "iacch")):
                continue                                  # Greek initial i (e-liber's list)
            out[i] = "J" if word[i].isupper() else "j"
        elif c == "i" and letters[:i] in PREFIXES and re.match(r"i(ac|ec|ic|un|ur|us|um|uv|oc)", letters[i:]):
            out[i] = "J" if word[i].isupper() else "j"    # dis|jungeret, ad|jumentum, in|juria, ob|jecit
        elif c == "i" and letters[:i] in JICIO_PREFIXES and re.match(r"i(ic|ec|ac)", letters[i:]):
            out[i] = "J" if word[i].isupper() else "j"    # pro|jiciō, re|jēcit
        elif c == "i" and letters[:i] in JICIO_PREFIXES and re.match(r"ic[ieīē]", letters[i:]) and letters not in OBEX:
            out[i] = ("J" if word[i].isupper() else "j") + word[i]  # ab|iciō → abjiciō: the j is pronounced (decision 17)
        elif c == "u" and vowel(i + 1) and (i == 0 or vowel(i - 1)) and not (i > 0 and letters[i - 1] in "qg"):
            out[i] = "V" if word[i].isupper() else "v"
    return "".join(out)


PREFIXES = {"ab", "ad", "con", "dis", "in", "ob", "sub", "per", "e", "ex"}
# Compounds of jaciō whose prefix is long by nature: ējiciō, dējiciō, prōjiciō, trājiciō.
LONG_BEFORE_J = re.compile(r"(e|de|pro|tra)j(?:ic|ec|ac)")
# Compounds of jaciō, always with j (abjiciō, ējiciō, prōjiciō), not Gaffiot's abiciō (decision 17).
JICIO_PREFIXES = {"ab", "ad", "con", "dis", "in", "ob", "sub", "e", "de", "re", "pro", "tra", "trans", "circum",
                  "inter", "super", "præ", "prae"}
# ŏbex, ŏbicis keeps i (Gaffiot's headword; objex only a variant). Obici, obicis are taken as forms of objiciō.
OBEX = {"obicem", "obice", "obices", "obicibus", "obicum"}
# Names whose i is a vowel though a rule would read a consonant: Abius (Abihu, Hebrew ʾĂḇîhû), not ab|jus.
JV_KEEP = {"abius", "abium", "abii", "abio"}
ENCLITICS = ("que", "ne", "ve")
# Words that only end like an enclitic (e-liber's list, the forms met here).
NEVER_SPLIT = {"atque", "neque", "quisque", "quaeque", "quodque", "quidque", "quoque", "ubique", "undique",
               "usque", "denique", "plerumque", "namque", "uterque", "utraque", "utrumque", "quicumque",
               "quaecumque", "quodcumque", "cumque", "itaque", "bene", "sine", "nomine", "homine", "sive", "seu",
               "neve", "cave", "pene", "paene", "superne", "mane", "sane", "plane", "fortasse", "quandoque", "unde",
               "ne", "pone", "inde", "deinde", "proinde", "abunde", "ve", "que", "utique", "quinque", "nave",
               "neque", "bove", "aliquando", "quemque", "cuique", "quique", "quaque", "unumquemque", "utroque"}


def split_enclitic(word, entry):
    """(host, enclitic) when `word` is unknown to the lexicon and ends in -que/-ne/-ve; else (word, '')."""
    if entry.candidates or key(word) in NEVER_SPLIT:
        return word, ""
    for enclitic in ENCLITICS:
        if key(word).endswith(enclitic) and len(word) > len(enclitic) + 1:
            return word[:-len(enclitic)], word[-len(enclitic):]
    return word, ""
