"""Castellio's text as printed (PLAN.md §7a item 2, HUMAN.md decision 57): the base edition's words in its own
spelling, beside the reading edition.

The words are the settled chapter's (stage 2 has already brought them to the base edition, 1573 for the NT); their
spelling, capitals and punctuation are the base edition's, read from its OCR. Each settled word is paired with the
OCR word the aligner puts against it (`align.align_chapter`) and takes one of these forms (its `kind`):

  ocr      the OCR word, which is the settled word under the folds (case, macrons, æ/ae, i/j, u/v), once each f the
           OCR read for a long s is put back to s where the settled word has s
  rule     the OCR word, which differs from the settled word as the approved spelling rules change it
           (data/rules/orthography.tsv): the printed spelling the reading edition normalized (eis, quicquid)
  variant  the OCR word, which differs by a spelling the printer uses and no rule covers (VARIANTS: cœlum, millia,
           nunciatum, iuerunt, literis)
  ę        a variant whose e stands against the settled æ: 1573's ę, which the OCR reads as e, printed æ
  nasal    the OCR word with the m or n of a nasal bar put back (animá, Cúque, mote: the OCR reads the bar as an
           accent, or loses it)
  misread  the OCR word is the settled word misread in this face (autein, cos): the settled word, printed
  lexicon  not read here: the spelling 1573 gives the same settled word where it was read, across the NT
  doubt    not read here, and the base edition spells the word more than one way, or by habit otherwise than the
           settled text (PRINTER_HABITS): to be read on the page, since the text follows the page, not a majority
  read     read on the page image (data/decisions/<osis>.orig.tsv), where the OCR could not decide
  guess    the OCR word is something else: the settled word in the printer's conventions (`printerize`)
  none     no OCR word: the same

Unpaired settled words are first matched against the OCR words left unpaired between their neighbours (a word
printed in another spelling: conditio, exequendum). In the stems where the OCR reads both æ and œ (cœl-, pœn-,
fœd-), the print has œ (`ligature_stems`).

Nothing is normalized (decision 58): the text follows the page, inconsistencies and misprints included; a decision
row records a word read on the page, or the print's word division (printed "+" joins a settled word to the one
before: plus quam → plusquam).

Expanded as decided (decision 57): & → et, q; → -que, the nasal bar (ã → am/an), long s → s (`align.clean`); ę → æ.
Kept as printed: u/v and i/j, the printed spellings, the word divisions where read (septies ne). Accents (verò,
quòd, à, hîc) are dropped unless ACCENTS is set: the OCR reads them unevenly, and decision 57 does not settle them.

Punctuation is the OCR's after a word that was read, up to the next word or number (a marginal reference read into
the line, Zach.13.7, is not the text's); after a word not read, the OCR's just before the next word read, else the
settled text's (`punct` says which). A stop before a lower-case word where the settled text has none is dropped
(`stray_stops`). Capitals are the OCR's; for a word not read, the settled text's.

The base edition is the testament's (`base_witness`): 1573 for the New Testament, 1738 for the Old. Paragraphs:
1573 begins every verse on a line of its own, so each verse is a paragraph (the printer's own, decision 57); 1738
runs its verses on and indents its paragraphs, not read yet (`usfm`). Verse ids are the KJV's, as in text/."""

import collections
import difflib
import itertools
import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import align, books, gold, latex, macronize, mdz, normalize, paths, rules, tsv

ACCENTS = False
PUNCT = set(",.;:?!()")
ACCENT_MARKS = {"̀", "́", "̂"}          # grave, acute, circumflex as printed (verò, hîc)


@dataclass
class Word:
    vid: str
    base: str            # the settled word
    ocr: str | None      # the OCR word paired with it (cleaned), "" for the later words of a joined run
    form: str            # the printed form chosen
    kind: str            # see the module's docstring
    after: str = ""      # punctuation printed after it
    settled_after: str = ""   # the settled text's punctuation after it (for a word not read in the OCR)
    tied: bool = False   # its æ made œ by `fix_ligatures` (the OCR read œ as æ)
    punct: str = "ocr"   # where `after` comes from: ocr; settled (not read in the OCR); stray (stray_stops)


@dataclass
class Chapter:
    number: int
    words: list = field(default_factory=list)
    extra: list = field(default_factory=list)        # [(verse id, OCR words between two paired words, not taken)]
    marked: dict = field(default_factory=dict)       # {verse id: [words 1573 sets between L. and G.]}
    canvas: dict = field(default_factory=dict)       # {verse id: canvas}


def strip_accents(word):
    decomposed = unicodedata.normalize("NFD", word)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if c not in ACCENT_MARKS))


def tidy(ocr):
    """The OCR word with ę → æ, and its accents dropped unless ACCENTS."""
    ocr = ocr.replace("ę", "æ").replace("Ę", "Æ").replace("ı", "i")
    return strip_accents(ocr) if ACCENTS else rules.unmacron(ocr)


def key(word):
    """The comparison form: no marks, lower case, æ/œ as ae/oe, j → i, v → u."""
    return rules.fold(strip_accents(word))


_RULES = None


def spelling_rules():
    global _RULES
    if _RULES is None:
        _RULES = normalize.word_rules()[0]
    return _RULES


def normalized(word):
    """The word as the approved word and stem rules spell it (lower case, no marks), applied until it settles."""
    w = rules.unligature(macronize.plain(strip_accents(word)))
    table = spelling_rules()
    for _ in range(3):
        hit = table.get(w)
        if not hit or rules.unligature(hit[0]) == w:
            break
        w = rules.unligature(macronize.plain(hit[0]))
    return w


def long_s(ocr, base):
    """Candidates for the OCR word with some of its f put back to s (the OCR reads long s as f), fewest first."""
    spots = [i for i, c in enumerate(ocr) if c in "fF"]
    if not spots or "s" not in key(base):
        return [ocr]
    out = []
    for n in range(len(spots) + 1):
        for chosen in itertools.combinations(spots, n):
            chars = list(ocr)
            for i in chosen:
                chars[i] = "s" if chars[i] == "f" else "S"
            out.append("".join(chars))
    return out[:64]


def printerize(base):
    """The settled word in the printer's conventions: no macrons, i for j, v at a word's start and u inside it
    (1573 vt, vxorem, reuixisset; Vnde)."""
    w = rules.unmacron(base).replace("j", "i").replace("J", "I")
    chars = []
    for i, c in enumerate(w):
        if c in "uv":
            chars.append("v" if i == 0 else "u")
        elif c == "U":
            chars.append("V")
        else:
            chars.append(c)
    return "".join(chars)


def recase(form, ocr, base):
    """The printed case: the OCR's, which is reliable; an all-capital OCR word (IESV) stays so."""
    if not ocr:
        return form
    if len(ocr) > 2 and ocr.isupper() and similar(ocr, base) >= 0.75:
        return form.upper()
    if ocr[0].isupper() or (ocr[0] in "lf" and base[:1] in "IJ"):   # the OCR reads a capital I as l or f (ludæi)
        return form[0].upper() + form[1:]
    return form[0].lower() + form[1:]


def letters(word):
    """Lower case, no marks, i for j, u for v; æ and œ kept as one letter each (so positions match the print)."""
    w = strip_accents(rules.unmacron(word)).lower().replace("ı", "i")
    return w.replace("j", "i").replace("v", "u")


# Spellings the printer and the reading edition both use, beyond the approved rules, on folded letters (u for v, i
# for j) after doubled letters are made single (literis, Barrabam, numis): 1573 cœlum, fœminas, millia, nunciatum,
# ocium, charissimus, extirpabitur, dignoscere, quæcunque, audiuerit, iuerunt, exijstis (the unsyncopated forms);
# accersitum, authore, circundatus, aliquandiu, alioquin, dexteram, misertus, summittite, inmutabiles, conburent,
# arcta, tentauit, decumas, diuersorium, myrrha, Caius, assimilem, vendicare, nequicquam, assequutum, increbescente,
# tetrarcha. A word's initial h comes and goes (olus, heri, Agar).
VARIANTS = [("intelig", "inteleg"), ("monim", "monum"), ("acers", "arces"), ("auct", "aut"), ("circun", "circum"),
            ("ndiu", "mdiu"), ("alioquin", "alioqui"), ("dexter", "dextr"), ("miserit", "misert"), ("subm", "sum"),
            ("inm", "im"), ("inp", "imp"), ("nb", "mb"), ("arct", "art"), ("tempt", "tent"), ("decum", "decim"),
            ("diuers", "deuers"), ("myrh", "mur"), ("cai", "gai"), ("assimil", "assimul"), ("uend", "uind"),
            ("cq", "dq"), ("equut", "ecut"), ("increbr", "increb"), ("tetrarches", "tetrarche"),
            ("tetrarcha", "tetrarche"), ("pellice", "pellici"),
            ("æ", "e"), ("œ", "e"), ("ch", "c"), ("ti", "ci"), ("xs", "x"), ("gn", "n"),
            ("nq", "mq"), ("nc", "mc"), ("nt", "mt"), ("iuis", "is"), ("iue", "ie"), ("iui", "ii"), ("ii", "i"),
            ("ph", "p"), ("th", "t"), ("y", "i")]
# The VARIANTS that join different forms of a word, not spellings of one form: listed with ⚑ in the review file,
# since the reading edition may want to follow the base edition there (misertus for miseritus, dexteram for dextram).
FORM_VARIANTS = ("miserit", "dexter", "alioquin", "tetrarch", "increbr", "assimil", "pellice", "decum")


# What the OCR confuses in this face: m as in/rn/ın, e and c, n and u, l and I.
MISREADS = [("rn", "m"), ("in", "m"), ("e", "c"), ("n", "u"), ("l", "i"), ("h", "b")]


def variant_key(word):
    w = re.sub(r"([lrtbsncpm])\1", r"\1", letters(word))
    for old, new in VARIANTS:
        w = w.replace(old, new)
    return w[1:] if w.startswith("h") else w


def restore_ae(form, base):
    """(form, changed): the OCR's e put back to æ where the settled word has æ. 1573 prints æ often as ę, which
    the OCR reads as e (Galilęa → Galilea), so an e against the settled æ is taken for ę."""
    a, b = letters(form), letters(printerize(base))
    if len(a) != len(form):
        return form, False
    chars, changed = list(form), False
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "replace" and a[i1:i2] == "e" and b[j1:j2] == "æ":
            chars[i1] = "Æ" if chars[i1].isupper() else "æ"
            changed = True
    return "".join(chars), changed


def misread_key(word):
    w = variant_key(word)
    for old, new in MISREADS:
        w = w.replace(old, new)
    return w


QUE = re.compile(r"(q[;:,]?|qs|qi|q[gi]|ą|ąs|ás|ós|os|ó|ăs|as|äs|ä|is|ig|s)$")


def nasal(base, ocr):
    """The OCR word with the m or n its nasal bar stood for put back (animá → animam, Cúque → Cumque, cóftruam →
    construam; also where the OCR lost the bar: mote → monte), when that makes the settled word; else None."""
    b, o = printerize(base), ocr
    lb = letters(b)
    lo = letters(o)
    if len(lb) != len(b) or len(lo) != len(o):
        return None
    out, ok = [], True
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, lo, lb, autojunk=False).get_opcodes():
        if tag == "equal":
            out.append(o[i1:i2])
        elif tag == "insert" and set(lb[j1:j2]) <= {"m", "n"} and j2 - j1 == 1                 and lb[j1] not in (lb[j1 - 1:j1] + lb[j2:j2 + 1]):
            # a lost nasal bar, not a doubled consonant: 1573 prints numis, which is a spelling, not nũmis
            out.append(b[j1:j2])
        else:
            ok = False
            break
    if not ok:
        return None
    form = rules.unmacron("".join(out))
    return form if variant_key(form) == variant_key(b) else None


def similar(a, b):
    return difflib.SequenceMatcher(None, letters(a), letters(b)).ratio()


def choose(base, ocr):
    """(form, kind) for one settled word and its OCR word (see the module's docstring). A capital the OCR reads
    inside a word (ofFufum, 1738 Gen 1:2) is lowered."""
    form, kind = _choose(base, ocr)
    # ABBYY (1738) writes the æ and œ ligatures out as two letters: where the settled word has the ligature there,
    # the print has it too (caelum → cælum).
    tied = re.sub("ae|Ae|AE|oe|Oe|OE", lambda m: {"ae": "æ", "Ae": "Æ", "AE": "Æ", "oe": "œ", "Oe": "Œ", "OE": "Œ"}[m.group()], form)
    if tied != form and letters(tied).replace("œ", "æ") == letters(printerize(base)).replace("œ", "æ"):
        form = tied
    if form[1:] != form[1:].lower() and not form.isupper():
        form = form[0] + form[1:].lower()
    return form, kind


def _choose(base, ocr):
    if ocr is None:
        return printerize(base), "none"
    clean = tidy(ocr)
    candidates = long_s(clean, base)
    for c in candidates:
        if key(c) == key(base):
            return c, "ocr"
    target = normalized(base)
    for c in candidates:
        if normalized(c) == target or key(rules.ligature(normalized(c))) == key(base):
            return c, "rule"
    if base.lower().endswith("que") and len(base) > 3 and (m := QUE.search(clean)) and m.start() > 0:
        form, kind = _choose(base[:-3], clean[:m.start()])
        if kind in ("ocr", "rule", "variant", "nasal", "ę"):
            return form + "que", kind
    for c in candidates:
        if variant_key(c) == variant_key(base):
            form, changed = restore_ae(c, base)
            return form, "ę" if changed else "variant"
    for c in candidates:
        if (form := nasal(base, c)) is not None:
            return form, "nasal"
    for c in candidates:
        if misread_key(c) == misread_key(base):
            return recase(printerize(base), c, base), "misread"
    form = printerize(base)
    return (recase(form, clean, base) if similar(clean, base) >= 0.6 else form), "guess"


def split_joined(ocr, bases):
    """Forms for settled words the OCR ran together (or split): the OCR's letters cut at the settled words'
    lengths, when they are the same letters; else None."""
    letters = tidy(ocr).replace(" ", "")
    fixed = next((c for c in long_s(letters, "".join(bases)) if key(c) == key("".join(bases))), None)
    if fixed is None or len(fixed) != sum(len(key(b)) for b in bases):
        # ligatures make key() longer than the printed letters; cut only when the counts agree
        return None
    out, at = [], 0
    for b in bases:
        n = len(key(b))
        out.append(fixed[at:at + n])
        at += n
    return out


def overrides(osis):
    """{(verse id, settled word): (printed form, reason)} from data/decisions/<osis>.orig.tsv: words read on the
    page images where the OCR could not decide (a reading's canvas is in its reason)."""
    path = paths.DATA / "decisions" / f"{osis}.orig.tsv"
    if not path.exists():
        return {}
    return {(r["id"], r["settled"]): (r["printed"], r["reason"]) for r in tsv.read(path)}


def build_chapter(witness, rows, number, read=None):
    """Chapter for one settled chapter ([(verse id, text)], verses 1…)."""
    found = align.align_chapter(witness, rows, number)
    out = Chapter(number, canvas=dict(found.pages), marked=dict(found.marked))
    matches = found.matches
    i = 0
    while i < len(matches):
        vid, base, ocr = matches[i]
        if i in found.joined:
            run = [i]
            while i + len(run) < len(matches) and matches[i + len(run)][2] == "" and i + len(run) in found.joined:
                run.append(i + len(run))
            parts = split_joined(ocr, [matches[k][1] for k in run])
            for n, k in enumerate(run):
                v, b, _ = matches[k]
                if parts:
                    out.words.append(Word(v, b, ocr if n == 0 else "", parts[n], "ocr"))
                else:
                    out.words.append(Word(v, b, ocr if n == 0 else "", printerize(b), "guess"))
            i += len(run)
            continue
        form, kind = choose(base, ocr)
        out.words.append(Word(vid, base, ocr, form, kind))
        i += 1
    tokens = witness.tokens
    # Settled words left unpaired: the aligner pairs by folded letters, so a word printed in another spelling
    # (conditio, exequendum, existent, herum) stays unpaired beside an unpaired OCR word. Try the OCR words between
    # the neighbours that were paired, in order.
    n = 0
    while n < len(out.words):
        if out.words[n].kind != "none":
            n += 1
            continue
        end = n
        while end < len(out.words) and out.words[end].kind == "none":
            end += 1
        before = next((found.at[m][1] for m in range(n - 1, -1, -1) if m in found.at), None)
        after = next((found.at[m][0] for m in range(end, len(out.words)) if m in found.at), None)
        if before is not None and after is not None and 0 < after - before < 40:
            free = [p for p in range(before + 1, after) if tokens[p][1]]
            at = 0
            for m in range(n, end):
                w = out.words[m]
                for k in range(at, len(free)):
                    form, kind = choose(w.base, tokens[free[k]][0])
                    if kind in READ_KINDS:
                        w.ocr, w.form, w.kind = tokens[free[k]][0], form, kind
                        found.at[m] = (free[k], free[k])
                        at = k + 1
                        break
        n = end
    for w in out.words:
        if read and (w.vid, w.base) in read:
            w.form, w.kind = read[(w.vid, w.base)][0], "read"
    # The settled text's punctuation after each word, in the aligner's word order.
    settled = []
    for _, text in rows:
        for token, is_word in align.words(text):
            if is_word:
                settled.append("")
            elif settled and token in PUNCT:
                settled[-1] += token
    for w, after in zip(out.words, settled):
        w.settled_after = after
    # Punctuation and the OCR words between two paired words. A word not read in the OCR (none, guess) takes the
    # settled text's punctuation; the OCR's next to it is noise as often as not (a marginal reference read in).
    for n, w in enumerate(out.words):
        if n not in found.at or w.kind in ("none", "guess"):
            w.after, w.punct = w.settled_after, "settled"
            # Unless the next word was read: then the OCR's punctuation just before it (past a verse number) is
            # this word's, and an OCR word just before it with no punctuation means the print has none.
            if n + 1 in found.at and out.words[n + 1].kind not in ("none", "guess"):
                marks, digits, k = [], 0, found.at[n + 1][0] - 1
                while k >= 0 and not tokens[k][1] and len(marks) < 4:
                    if tokens[k][0] in PUNCT:
                        marks.insert(0, tokens[k][0])
                    elif tokens[k][0].isdecimal():
                        digits += 1
                    k -= 1
                # A verse number may stand between (one number, at a verse's start); more numbers, or one inside a
                # verse, are a marginal reference the OCR read into the line (Zach.13.7), whose stops are not the text's.
                reference = digits > 1 or (digits and out.words[n + 1].vid == w.vid) or \
                    (k >= 0 and len(tokens[k][0]) <= 4 and tokens[k][0][:1].isupper() and digits)
                if marks and not reference:
                    plain = [p for p in marks if p not in "()"]
                    w.after, w.punct = "".join(plain[:1]) + (")" if ")" in marks else ""), "ocr"
                elif not marks and k >= 0 and k + 1 == found.at[n + 1][0] and n not in found.at:
                    w.after, w.punct = "", "ocr"
            continue
        if found.at.get(n + 1, (None,))[0] == found.at[n][0]:
            continue                                     # run together with the next word in the OCR (vtabeant)
        last = found.at[n][1]
        nxt = next((found.at[m][0] for m in range(n + 1, min(n + 4, len(out.words))) if m in found.at), None)
        stop = nxt if nxt is not None and nxt > last else last + 4
        punct, between = [], []
        numbered, mark = False, False
        for t, is_word in tokens[last + 1:stop]:
            if is_word:
                between.append(t)
            elif t[:1].isalpha():
                mark = True                              # Castellio's L. or G. mark: its point is not the text's
            elif mark and t in ".,":
                mark = False
            elif t.isdecimal():
                numbered = True                          # a verse number or a marginal reference: the word's own
            elif t in PUNCT and not between and not numbered:   # stops come before it
                punct.append(t)
        marks = [p for p in punct if p not in "()"]
        w.after = ("(" if "(" in punct else "") + "".join(marks[:1]) + (")" if ")" in punct else "")
        if ")" in punct and marks and punct.index(")") < punct.index(marks[0]):
            w.after = ")" + marks[0]
        if between and nxt is not None and n + 1 < len(out.words) and n + 1 in found.at:
            out.extra.append((w.vid, " ".join(between)))
    return out


def stray_stops(chapter):
    """A stop the OCR has before a lower-case word, where the settled text has none, is a marginal note's read
    into the line (Lunaticus., Aue Rabbi.); where the settled text has ? or !, the OCR misread that mark."""
    words = chapter.words
    for w, nxt in zip(words, words[1:]):
        if w.after == "." and w.punct == "ocr" and nxt.form[:1].islower() and nxt.vid == w.vid:
            settled = w.settled_after.replace("(", "").replace(")", "")
            if not settled:
                w.after, w.punct = "", "stray"
            elif settled[:1] in "?!":
                w.after, w.punct = settled[:1], "stray"


JOINED = "+"   # a decision row's printed form for a settled word the print joins to the one before (plus quam → plusquam)


def verse_text(words):
    out = ""
    for w in words:
        if w.form == JOINED:
            out += w.after                               # its letters are in the word before; only its marks remain
            continue
        lead = w.after.startswith("(")
        piece = w.form + ("" if lead else w.after)
        out += (" " if out else "") + piece
        if lead:
            out += " " + w.after
    out = re.sub(r"\(\s+", "(", out)
    out = re.sub(r"\s+\)", ")", out)
    return out


READ_KINDS = ("ocr", "rule", "variant", "nasal", "ę")


class Lexicon(collections.defaultdict):
    """{settled word, lower case: Counter of printed forms, lower case}, with, per settled stem (`settled_stem`),
    how often the OCR read an æ there literally (`literal_ae`) and how often an e was taken for ę (`e_taken`)."""

    def __init__(self):
        super().__init__(collections.Counter)
        self.literal_ae = collections.Counter()
        self.e_taken = collections.Counter()


def lexicon(chapters):
    """The Lexicon of the words read in the OCR."""
    out = Lexicon()
    for chapter in chapters:
        for w in chapter.words:
            if w.kind in READ_KINDS and w.form:
                out[w.base.lower()][w.form.lower()] += 1
                if w.kind != "ę" and "æ" in w.form.lower() and "æ" in w.base.lower():
                    out.literal_ae[settled_stem(w.base)] += 1
            if w.kind == "ę":
                out.e_taken[settled_stem(w.base)] += 1
    return out


def check_e_caudata(chapters, known):
    """An e the OCR read against the settled æ was taken for 1573's ę. That holds only where the print has æ in the
    word: read on the page, *præcedam*, *quę* and *Cęsari* are ę, but *seculis*, *secula* and *Noe* are a plain e
    (2026-11-13, data/decisions/*.orig.tsv). So: where the OCR never reads a literal æ in the stem anywhere in the
    Testament (*sæcul-* 0 against 31), the e stands; where it reads one less than twice as often as it was taken for
    ę, the word is read on the page (`doubt`); else æ."""
    literal = getattr(known, "literal_ae", None)
    if literal is None:
        return
    for chapter in chapters:
        for w in chapter.words:
            if w.kind != "ę":
                continue
            stem = settled_stem(w.base)
            if literal[stem] == 0:
                o = tidy(w.ocr or "")
                w.form = "".join(o[i] if c in "æÆ" and i < len(o) and o[i] in "eE" else c for i, c in enumerate(w.form))
                w.kind = "variant"
            elif literal[stem] < 2 * known.e_taken[stem]:
                w.kind = "doubt"


def printed_forms(votes):
    """The forms a lexicon entry's votes really attest: at least two votes and a tenth of them (a single *estt*
    against 1779 *est* is the OCR's), with æ and œ taken as one (the OCR confuses them; `ligature_stems`)."""
    total = sum(votes.values())
    real = [f for f, n in votes.most_common() if n >= 2 and n >= 0.1 * total]
    out = []
    for f in real:
        if f.replace("œ", "æ") not in [o.replace("œ", "æ") for o in out]:
            out.append(f)
    return out


def from_lexicon(chapters, known):
    """Words not read in the OCR (none, misread, guess) take the spelling the base edition gives the same settled word
    where it was read, when it gives only one (condiciō → conditio): kind `lexicon`. Where it prints the word more than
    one way (iīs as eis and ijs, ceterum and cæterum), the text follows the page, not the majority (Nathan,
    2026-11-13): kind `doubt`, to be read on the page image."""
    for chapter in chapters:
        for w in chapter.words:
            if w.kind not in ("none", "misread", "guess"):
                continue
            votes = known.get(w.base.lower())
            if not votes:
                continue
            forms = printed_forms(votes)
            if len(forms) > 1:
                w.kind = "doubt"
            elif forms:
                form = forms[0]
                w.form = (form[0].upper() + form[1:]) if w.form[:1].isupper() else form
                w.kind = "lexicon"


def ligature_key(form, at):
    """The letters around a printed ligature: up to two before it and two after, i/j and u/v folded (c_lu)."""
    fold = lambda t: t.lower().replace("j", "i").replace("v", "u")
    return fold(form[max(0, at - 2):at]) + "_" + fold(form[at + 1:at + 3])


def ligature_stems(known):
    """(Ligature key, settled stem) pairs whose OCR readings mix æ and œ, with œ at least three times. The OCR reads
    1573's œ as æ (cœlum, cœlestis, pœnitentiam on the page, canvases 748, 761, 775, 894), not the reverse, so where
    the readings mix, the print has œ (cœl-, fœmin-, pœn-, fœd-)."""
    votes = collections.defaultdict(collections.Counter)
    for base, forms in known.items():
        for f, n in forms.items():
            for m in re.finditer("[æœ]", f):
                votes[(ligature_key(f, m.start()), settled_stem(base))][m.group()] += n
    return {k for k, c in votes.items() if c["œ"] >= 3 and c["æ"]}


def settled_stem(base):
    """The settled word's first four letters, ligatures spelled out: the words behind one printed key stay apart
    (cēpit "took", 1573 cæpit, against cœpit "began": cepi / coep)."""
    return rules.unligature(rules.unmacron(base).lower())[:4]


def fix_ligatures(chapters, stems):
    for chapter in chapters:
        for w in chapter.words:
            for m in re.finditer("[æÆ]", w.form):
                if (ligature_key(w.form, m.start()), settled_stem(w.base)) in stems:
                    w.form = w.form[:m.start()] + ("Œ" if m.group() == "Æ" else "œ") + w.form[m.start() + 1:]
                    w.tied = True


# 1573's habits, read on the page for words its OCR missed (2026-11-13, data/decisions/*.orig.tsv): every word read
# with exs-, tempt-, nunti-, intelleg-, cariss- or hiem- in the settled text is printed ex-, tent-, nunci-, intellig-,
# chariss-, hyem- (13, 12, 10, 6, 2 and 2 words). 1738 differs (exsisteret, exstitit, Gen 1:3), so these are 1573's.
PRINTER_HABITS = {"novum": [("exs", "ex"), ("tempt", "tent"), ("nunti", "nunci"), ("intelleg", "intellig"),
                            ("cariss", "chariss"), ("hiem", "hyem")]}


def printer_habits(chapters, testament):
    """A word still not read (none, guess, misread) whose settled spelling is one the base edition spells otherwise
    by habit (PRINTER_HABITS) is marked `doubt`, to be read on the page: the habit is not applied, since the text
    follows the page (Nathan, 2026-11-13)."""
    for chapter in chapters:
        for w in chapter.words:
            if w.kind not in ("none", "guess", "misread"):
                continue
            form = w.form
            for old, new in PRINTER_HABITS.get(testament, []):
                form = form.replace(old, new).replace(old.capitalize(), new.capitalize())
            if form != w.form:
                w.kind = "doubt"


def settled_rows(osis, chapters=None):
    by_chapter = collections.defaultdict(list)
    for vid, row in gold.load(osis).items():
        _, c, v = tsv.parse_id(vid)
        if (chapters is None or c in chapters) and v > 0:
            by_chapter[c].append((vid, row["text"]))
    return by_chapter


def base_witness(osis):
    """The base edition's OCR as an align.Witness: 1573 (MDZ hOCR) for the New Testament, 1738 (archive.org
    bibliasacraexseb01cast, ABBYY) for the Old (decisions 1 and 24)."""
    if books.select([osis])[0].testament == "novum":
        return mdz.witness()
    path = paths.SOURCES / "archive" / "1738" / "text.txt"
    if not path.exists():
        raise SystemExit(f"{path.relative_to(paths.ROOT).as_posix()} is missing: python -m pipeline fetch archive 1738")
    return align.Witness(path.read_text(encoding="utf-8"))


def build(osis, chapters, witness=None, known=None):
    """{chapter: Chapter} for these settled chapters of a book (all of them when chapters is None). known: a lexicon
    (`lexicon`), by default this book's own."""
    witness = witness or base_witness(osis)
    by_chapter = settled_rows(osis, chapters)
    read = overrides(osis)
    built = {c: build_chapter(witness, by_chapter[c], c, read) for c in sorted(by_chapter)}
    known = known if known is not None else lexicon(built.values())
    from_lexicon(built.values(), known)
    check_e_caudata(built.values(), known)
    printer_habits(built.values(), books.select([osis])[0].testament)
    fix_ligatures(built.values(), ligature_stems(known))
    for chapter in built.values():
        stray_stops(chapter)
    return built


def testament_lexicon(testament, witness):
    """The lexicon of every settled book of a testament ("novum" or "vetus"), read in its base edition's OCR."""
    chapters = []
    for book in books.BOOKS:
        if book.testament != testament or not gold.load(book.osis):
            continue
        rows = settled_rows(book.osis)
        chapters += [build_chapter(witness, rows[c], c) for c in sorted(rows)]
    return lexicon(chapters)


def usfm(book, built, header):
    """The draft USFM: the reading edition's header lines, then the verses in the base edition's paragraphs. 1573
    begins every verse on a line of its own, so in the New Testament each verse is a paragraph. 1738 runs verses on
    and indents its paragraphs (Gen 44:3, 44:13 on leaf 107): those are not read yet (PLAN.md §4, stage 2b), so an
    Old Testament chapter has one paragraph until they are."""
    per_verse = book.testament == "novum"
    lines = header[:]
    for number, chapter in built.items():
        lines += ["", f"\\c {number}"] + ([] if per_verse else ["\\p"])
        verses = collections.defaultdict(list)
        for w in chapter.words:
            verses[w.vid].append(w)
        for vid, ws in verses.items():
            lines += (["\\p"] if per_verse else []) + [f"\\v {tsv.parse_id(vid)[2]} {verse_text(ws)}"]
    return "\n".join(lines) + "\n"


def header_lines(book):
    """The reading edition's header (\\id … \\mt): every line before its first chapter, blank lines dropped."""
    lines = []
    for line in latex.usfm_path(book).read_text(encoding="utf-8").splitlines():
        if line.startswith("\\c "):
            break
        if line.strip():
            lines.append(line)
    return lines


def approved_path(book):
    """The approved printed text: like text/, never rewritten by code once it is there."""
    return paths.ROOT / "text" / "orig" / f"{book.usfm}.usfm"


def path(book):
    return paths.ROOT / "text" / "orig" / "draft" / f"{book.usfm}.usfm"


KIND_NOTES = {
    "ocr": "read in the OCR as the settled word (u/v, i/j, long s as printed)",
    "rule": "read in the OCR, a spelling the approved rules normalize",
    "variant": "read in the OCR, a printer's spelling no rule covers",
    "ę": "read in the OCR as e against the settled æ: taken for the print's ę, printed æ",
    "nasal": "read in the OCR with a nasal bar (m or n put back)",
    "misread": "the settled word misread by the OCR; spelling as settled",
    "lexicon": "not read here; spelling as the base edition prints the same word elsewhere in the Testament",
    "doubt": "not read here, and the base edition spells the word more than one way: to be read on the page",
    "read": "read on the page image (data/decisions/<osis>.orig.tsv)",
    "guess": "OCR unreadable; the settled word in the printer's conventions",
    "none": "no OCR word; the settled word in the printer's conventions",
}


def report(book, chapters, built, target, today):
    """The review file for a draft: how each word was made, and what is left to check."""
    words = [w for c in built.values() for w in c.words]
    kinds = collections.Counter(w.kind for w in words)
    span = f"{min(built)}–{max(built)}" if len(built) > 1 else f"{min(built)}"
    command = span.replace("–", "-")
    name = book.osis
    nt = book.testament == "novum"
    edition = "1573 (MDZ bsb10141277)" if nt else "1738 (archive.org bibliasacraexseb01cast)"
    year = edition[:4]
    layout = ("One paragraph per verse, as 1573 sets them" if nt else
              "Paragraphs not yet set: 1738 runs the verses on and indents its paragraphs, which are still to be "
              "read from its hOCR (PLAN.md §4, stage 2b); each chapter is one paragraph until then")
    out = [f"# {name} {span} as printed ({year}): the draft for review", "",
           f"Built {today} by `python -m pipeline orig {name} {command}` → `{target}`. The words are the settled chapters' "
           f"(`text/`); their spelling, capitals and punctuation are {edition}'s, read from its OCR as "
           "`pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as "
           f"printed. Dropped: the accents (*verò*, *quòd*, *à*). {layout} "
           "(HUMAN.md decision 57). Regenerate after changing `data/decisions/" + name + ".orig.tsv`.", "",
           "**Decision:** pending", "", "## How each word was made", "",
           "| Kind | Words | |", "|---|---:|---|"]
    for kind in ("ocr", "rule", "variant", "ę", "nasal", "misread", "lexicon", "read", "doubt", "guess", "none"):
        if kinds[kind]:
            out.append(f"| {kind} | {kinds[kind]} | {KIND_NOTES[kind]} |")
    out += [f"| all | {len(words)} | |", ""]
    read = overrides(name)
    if read:
        out += ["## Read on the page", "",
                "Where the OCR could not decide. Several differ from the settled text by more than spelling: "
                "the reading edition may want to look again at these (marked ⚑).", ""]
        for (vid, settled), (printed, reason) in read.items():
            plain = re.sub(r"[ ']", "", printed)
            flag = "" if printed == JOINED or "misprint" in reason or \
                variant_key(plain) == variant_key(settled) or variant_key(plain).startswith(variant_key(settled)) else "⚑ "
            if "misprint" in reason:
                flag = "✱ "
            out.append(f"- {flag}**{vid[5:] if vid.startswith(name + '.') else vid}** *{settled}* → *{printed}*: {reason}")
        out.append("")
    for kind, title in (("rule", "Spellings the approved rules normalize"), ("variant", "Printer's spellings no rule covers"),
                        ("ę", "e against the settled æ, printed æ")):
        pairs = collections.Counter((w.base.lower(), w.form.lower()) for w in words
                                    if w.kind == kind and rules.unmacron(w.base).lower() != w.form.lower())
        if pairs:
            out += [f"## {title} ({sum(pairs.values())})", "",
                    "; ".join(f"*{b}* → *{f}*" + (f" ×{n}" if n > 1 else "") for (b, f), n in sorted(pairs.items())), ""]
    forms = collections.Counter((w.vid, w.base, w.form) for w in words if w.kind == "variant" and
                                any(f in letters(w.base) or f in letters(w.form) for f in FORM_VARIANTS))
    if forms:
        out += [f"## ⚑ Other forms of the word ({sum(forms.values())})", "",
                "Read in the OCR and taken by the variant rules, but a different form of the word, not only a spelling: "
                "the reading edition may want to look again at these.", "",
                "; ".join(f"{vid[len(name) + 1:]} *{b}* → *{f}*" for vid, b, f in forms), ""]
    left = [w for w in words if w.kind in ("none", "guess", "misread", "doubt")]
    if left:
        out += [f"## Not read in the OCR ({len(left)})", "",
                "Spelling as settled, in the printer's conventions (u/v, i/j); not checked on the page.", "",
                "| Verse | Settled | Printed | OCR |", "|---|---|---|---|"]
        for w in left:
            out.append(f"| {w.vid} | {w.base} | {w.form} | {w.ocr or '—'} |")
        out.append("")
    settled = [w for w in words if w.punct in ("settled", "stray") and w.after != w.settled_after or
               (w.punct == "settled" and w.after)]
    if settled:
        out += [f"## Punctuation not from the OCR ({len(settled)})", "",
                "After a word the OCR missed, the settled text's mark stands; a stop the OCR had before a lower-case "
                "word was dropped or corrected (stray). Not checked on the page.", ""]
        out.append("; ".join(f"{w.vid[len(name) + 1:]} *{w.form}{w.after}*" + (" (stray)" if w.punct == "stray" else "")
                             for w in settled))
        out.append("")
    marks = "L. … G." if nt else "G. … H. (and L., G.L.)"
    found = "; ".join(f"{vid[len(name) + 1:]} *{' '.join(ws)}*" for c in built.values() for vid, ws in c.marked.items())
    out += ["## Open questions", "",
            f"1. **Accents.** {year} prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* "
            "and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, "
            "or reading them page by page.",
            f"2. **Chapter summaries.** {year} heads each chapter with a summary. The reading edition leaves them out "
            "(decision 50); the printed text could keep them.",
            "3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; "
            "*plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.",
            f"4. **Castellio's {marks} marks**: the words are kept, the marks dropped, as in the reading edition. "
            + (f"Found here: {found}." if found else "None found by the aligner in these chapters."),
            "5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).",
            ""]
    return "\n".join(out)
