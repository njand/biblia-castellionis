"""Stage 3 on a USFM text: the approved spelling rules (data/rules/orthography.tsv) proposed word by word.

`propose(usfm, osis)` lists every word the approved rules would change, as replacements scoped to a verse with
enough context to match once (the Apply lines of a review file):

  word      a word rule (old → new; case kept, macrons carried over where the letters stay)
  phrase    a phrase rule (word division: mē cum → mēcum)
  ligature  ae/oe → æ/œ where neither vowel is marked (decision 16)
  jv        consonantal i/u → j/v (decision 17; macronize.jv, with its exceptions)

Decisions that need a reading of the verse (capitals for God, decision 20) are listed by `divine_candidates`
for a reader to decide; nothing here decides them."""

import difflib
import re
from dataclasses import dataclass

from pipeline import macronize, review, rules, tsv

WORD = re.compile(r"[^\W\d_]+")
DIVINE = re.compile(r"^(pater|patr|fīli|fili|spīrit|spirit|servātōr|servator|suprēm|suprem|sānct|sanct|domin)", re.I)


@dataclass
class Proposal:
    vid: str
    old: str
    new: str
    kind: str
    note: str


def settled_forms():
    """{plain key: the marked form} for every word of the settled chapters written one way only."""
    from pipeline import books, gold
    seen = {}
    for book in books.BOOKS:
        for row in gold.load(book.osis).values():
            for word in WORD.findall(row["text"]):
                k = rules.unligature(macronize.plain(word))
                seen.setdefault(k, set()).add(word.lower())
    return {k: next(iter(v)) for k, v in seen.items() if len(v) == 1}


def carry(old, new, known=None):
    """`new` with the capital of `old` and its macrons: the settled chapters' marking of `new` where they have
    one, else `old`'s macrons where the letters agree; æ/œ for diphthongs."""
    k = rules.unligature(macronize.plain(new).replace(" ", ""))
    if known and k in known and " " not in new:
        marked = known[k]
    else:
        plain_old = rules.unligature(macronize.plain(old)).replace(" ", "")
        plain_new = rules.unligature(macronize.plain(new))
        squeezed = plain_new.replace(" ", "")
        longs = macronize.long_vowels(rules.unligature(old).replace(" ", ""))
        out = set()
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, plain_old, squeezed, autojunk=False).get_opcodes():
            if tag == "equal":
                out |= {j1 + (i - i1) for i in longs if i1 <= i < i2}
        # A carried ī now before a vowel (audīverit → audierit) is short: vōcālis ante vōcālem.
        out = {i for i in out if not (squeezed[i] == "i" and i + 1 < len(squeezed) and squeezed[i + 1] in "aeiou")}
        marked = macronize.ligatures(macronize.mark(squeezed, out))
        for at in [i for i, c in enumerate(plain_new) if c == " "]:   # the spaces of a phrase rule, put back
            marked = marked[:at] + " " + marked[at:]
    return marked[:1].upper() + marked[1:] if old[:1].isupper() else marked


def verses(usfm, osis):
    """[(verse id, (start, end), text of the span)] in order (spans as review.verse_span gives them)."""
    out = []
    chapters = list(re.finditer(r"^\\c (\d+)", usfm, re.M))
    for n, c in enumerate(chapters):
        end = chapters[n + 1].start() if n + 1 < len(chapters) else len(usfm)
        for v in re.finditer(r"\\v (\d+)", usfm[c.end():end]):
            vid = tsv.verse_id(osis, int(c.group(1)), int(v.group(1)))
            span = review.verse_span(usfm, vid)
            if span:
                out.append((vid, span, usfm[span[0]:span[1]]))
    return out


def anchored(span_text, start, end, new_text):
    """(old, new) for replacing span_text[start:end] by new_text, widened a word at a time (left, then right)
    until `old` occurs once in the verse."""
    left, right, turn = start, end, 0
    while span_text.count(span_text[left:right]) > 1 and (left > 0 or right < len(span_text)):
        if turn % 2 == 0 and (before := re.search(r"\S+\s*$", span_text[:left])):
            left = before.start()
        elif turn % 2 == 1 and (after := re.match(r"\s*\S+", span_text[right:])):
            right += after.end()
        turn += 1
    return span_text[left:right], span_text[left:start] + new_text + span_text[end:right]


def word_rules():
    words, phrases = {}, []
    for row in rules.load_rules():
        old, new = rules.unligature(row["old"]).lower(), rules.unligature(row["new"]).lower()
        if row["scope"] == "word":
            words[old] = (new, row["note"])
        elif row["scope"] == "phrase":
            phrases.append((old.split(), new, row["note"]))
    return words, phrases


# i before a vowel that stays a vowel: forms of eō and its compounds (iērunt, coiērunt, iit), and Greek names
# with ι before a vowel (Ēsāiās, Caiāphās, Gāius).
EO = re.compile(r"^(ab|ad|amb|co|ex|in|ob|per|præ|prae|prōd|prod|red|sub|trāns|trans|inter|circum|vēn|ven)?i[eē](r|b|n|ram|ndu)")
GREEK_I = re.compile(r"[aeē]i[aāoō]")
# Latin words the Greek pattern would catch, whose i is a consonant: major (Rom 9:12 *Maior*), pejor, plēbējus,
# ējaculor.
LATIN_J = re.compile(r"^(m[aā]io|pei[oō]|pl[eē]b[eē]i|[eē]iac)")


def propose(usfm, osis, known=None):
    """[Proposal] for every change the approved rules make in this USFM text. known: settled_forms()."""
    words, phrases = word_rules()
    known = settled_forms() if known is None else known
    out = []
    for vid, span, text in verses(usfm, osis):
        for start, end, change, kind, note in changes(text, words, phrases, known):
            out.append(Proposal(vid, *anchored(text, start, end, change), kind, note))
    return out


def changes(text, words, phrases, known):
    """[(start, end, new, kind, note)]: the approved rules' changes to one verse's text (markers left alone),
    by offset in `text`, in order."""
    settled_keys = set(known)
    body = re.sub(r"\\[a-z]+\d*\*?", lambda m: " " * len(m.group()), text)     # markers blanked, offsets kept
    tokens = [(m.start(), m.end(), m.group()) for m in WORD.finditer(body)]
    out = []
    k = 0
    while k < len(tokens):
        start, end, word = tokens[k]
        key = rules.unligature(macronize.plain(word))
        for old_words, new, note in phrases:
            n = len(old_words)
            if [rules.unligature(macronize.plain(t[2])) for t in tokens[k:k + n]] == old_words and                     all(not body[a[1]:b[0]].strip() for a, b in zip(tokens[k:k + n], tokens[k + 1:k + n])):
                e = tokens[k + n - 1][1]
                out.append((start, e, carry(text[start:e], new, known), "phrase", note))
                k += n
                break
        else:
            change, kind, note = None, "", ""
            if key in words:
                change, kind, note = carry(word, words[key][0], known), "word", words[key][1]
            else:
                lig = macronize.ligatures(word)
                if lig != word:
                    change, kind, note = lig, "ligature", "decision 16"
                jv = macronize.jv(change or word)
                plain = macronize.plain(word)
                if jv != (change or word) and key not in settled_keys and not EO.match(plain)                         and not (GREEK_I.search(plain) and not LATIN_J.match(plain)):
                    change, kind, note = jv, "jv", "decision 17"
            if change and change != word:
                out.append((start, end, change, kind, note))
            k += 1
    return out


def divine_candidates(usfm, osis):
    """[(verse id, word, context)] for words that may name God or Christ (decision 20), with their case as
    written, for a reader to decide."""
    out = []
    for vid, span, text in verses(usfm, osis):
        plain = re.sub(r"\\[a-z]+\d*\*?", " ", text)
        for m in WORD.finditer(plain):
            if DIVINE.match(m.group()):
                out.append((vid, m.group(), re.sub(r"\s+", " ", plain[max(0, m.start() - 60):m.end() + 50]).strip()))
    return out
