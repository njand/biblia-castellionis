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
quòd, à, hîc) are kept where the OCR reads them (ACCENTS, decision 67); the OCR misses about half of them, so
the words that may carry one are read on the page (data/review/accents-1573.md).

Punctuation is the OCR's after a word that was read, up to the next word or number (a marginal reference read into
the line, Zach.13.7, is not the text's); after a word not read, the OCR's just before the next word read, else the
settled text's (`punct` says which). A stop before a lower-case word where the settled text has none is dropped
(`stray_stops`). Capitals are the OCR's; for a word not read, the settled text's.

The base edition is the testament's (`base_witness`): 1573 for the New Testament, 1738 for the Old. Paragraphs:
1573 begins every verse on a line of its own, so each verse is a paragraph (the printer's own, decision 57); 1738
runs its verses on and indents its paragraphs, not read yet (`usfm`). Verse ids are the KJV's, as in text/."""

import bisect
import collections
import difflib
import itertools
import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import align, books, gold, latex, macronize, mdz, normalize, paths, rules, tsv

ACCENTS = True                          # decision 67: the printed text keeps 1573's accents
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
    token: int | None = None   # the OCR token it is paired with, or (not paired) the one after its paired neighbour


@dataclass
class Chapter:
    number: int
    words: list = field(default_factory=list)
    extra: list = field(default_factory=list)        # [(verse id, OCR words between two paired words, not taken)]
    marked: dict = field(default_factory=dict)       # {verse id: [words 1573 sets between L. and G.]}
    canvas: dict = field(default_factory=dict)       # {verse id: canvas}
    breaks: dict = field(default_factory=dict)       # {word index: (leaf, line, indent)}: the print's paragraphs (1738)


def strip_accents(word):
    decomposed = unicodedata.normalize("NFD", word)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if c not in ACCENT_MARKS))


def tidy(ocr):
    """The OCR word with ę → æ; its grave and circumflex accents kept (ACCENTS), any other mark dropped."""
    ocr = ocr.replace("ę", "æ").replace("Ę", "Æ").replace("ı", "i")
    if not ACCENTS:
        return rules.unmacron(ocr)
    # 1573's accents are the grave and the circumflex (verò, hîc); an acute is the OCR's reading of a nasal bar (nó,
    # auté), already expanded or handled by `nasal`, so it goes with any other mark.
    decomposed = unicodedata.normalize("NFD", ocr)
    return unicodedata.normalize("NFC", "".join(c for c in decomposed
                                                if unicodedata.category(c) != "Mn" or c in ("̀", "̂")))


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
    if not spots or not ("s" in key(base) or "x" in key(base)):   # x: the print's exs- (exstinguantur)
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
# for j; ae and oe as the OCR of 1738 writes æ and œ) after doubled letters are made single (literis, Barrabam, numis): 1573 cœlum, fœminas, millia, nunciatum,
# ocium, charissimus, extirpabitur, dignoscere, quæcunque, audiuerit, iuerunt, exijstis (the unsyncopated forms);
# accersitum, authore, circundatus, aliquandiu, alioquin, dexteram, misertus, summittite, inmutabiles, conburent,
# arcta, tentauit, decumas, diuersorium, myrrha, Caius, assimilem, vendicare, nequicquam, assequutum, increbescente,
# tetrarcha. A word's initial h comes and goes (olus, heri, Agar).
VARIANTS = [("intelig", "inteleg"), ("monim", "monum"), ("acers", "arces"), ("auct", "aut"), ("circun", "circum"),
            ("ndiu", "mdiu"), ("alioquin", "alioqui"), ("dexter", "dextr"), ("miserit", "misert"), ("subm", "sum"),
            ("inm", "im"), ("inp", "imp"), ("nb", "mb"), ("arct", "art"), ("tempt", "tent"), ("decum", "decim"),
            ("diuers", "deuers"), ("diuert", "deuert"),("myrh", "mur"), ("cai", "gai"), ("assimil", "assimul"), ("uend", "uind"),
            # aereus and aerius both printed aere- (1573 Matt 8:20 aereæ volucres; the edition's āeriæ by its rules)
            ("aere", "aeri"),
            ("cq", "dq"), ("equut", "ecut"), ("increbr", "increb"), ("tetrarches", "tetrarche"),
            ("tetrarcha", "tetrarche"), ("pellice", "pellici"),
            # ad- left unassimilated (1738 adfecimus, adparuisset, adligauit, adsignauit; read on the page, Gen 38:28,
            # 47:11): on folded letters, after doubled letters are made single (ff and gg stay double)
            ("adf", "aff"), ("adp", "ap"), ("adl", "al"), ("ads", "as"), ("adg", "agg"), ("adc", "ac"), ("adr", "ar"),
            # 1738 sumsit, sumta, emtus, redemtum, peremti, coemti (read on the page, Gen 4:25, 17:23)
            ("mpt", "mt"), ("mps", "ms"),
            ("ae", "e"), ("oe", "e"), ("æ", "e"), ("œ", "e"), ("ch", "c"), ("ph", "p"), ("th", "t"), ("ti", "ci"),
            ("xs", "x"), ("gn", "n"), ("nq", "mq"), ("nc", "mc"), ("nt", "mt"), ("iuis", "is"), ("iue", "ie"),
            ("iui", "ii"), ("ii", "i"), ("y", "i")]
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


def l_for_i(ocr, base):
    """Whether the OCR word differs from the settled word only by i read for l or the reverse (1738 JJle, iila for
    Ille, illa): an OCR confusion, which the variants' doubled letters (ll → l, ii → i) would otherwise take for a
    spelling."""
    a, b = letters(ocr), letters(printerize(base))
    return a != b and a.replace("l", "i") == b.replace("l", "i")


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
    if tied != form and letters(tied).replace("œ", "æ").lstrip("h") ==             letters(printerize(base)).replace("œ", "æ").lstrip("h"):          # (1738 Ebræorum for Hebræōrum)
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
        if variant_key(c) == variant_key(base) and not l_for_i(c, base):
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
    page images where the OCR could not decide (a reading's canvas is in its reason). A settled word may carry its
    occurrence in the verse (cum#2); without one, the row is every occurrence's."""
    path = paths.DATA / "decisions" / f"{osis}.orig.tsv"
    if not path.exists():
        return {}
    return {(r["id"], r["settled"]): (r["printed"], r["reason"]) for r in tsv.read(path)
            if not r["printed"].startswith(PARAGRAPH)}


PARAGRAPH = "¶"   # a decision row's printed form for a paragraph read on the page: ¶ begins one before the settled word, ¶- takes one away


def paragraph_rows(osis):
    """{(verse id, settled word): (True to begin a paragraph there, False to take one away, reason)} from the rows
    of data/decisions/<osis>.orig.tsv whose printed form is ¶ or ¶-: paragraphs read on the page where the indents
    read from the hOCR miss one or take a line for one (a column's first line, its number and a footnote letter read
    as words: 1738 Exod 12:17)."""
    path = paths.DATA / "decisions" / f"{osis}.orig.tsv"
    if not path.exists():
        return {}
    return {(r["id"], r["settled"]): (r["printed"] == PARAGRAPH, r["reason"]) for r in tsv.read(path)
            if r["printed"].startswith(PARAGRAPH)}


def apply_paragraph_rows(chapter, rows):
    """Set the paragraphs read on the page (`paragraph_rows`) in a built chapter: (leaf, line, indent) is None for one."""
    for (vid, settled), (begin, _) in rows.items():
        n = next((k for k, w in enumerate(chapter.words) if w.vid == vid and w.base == settled), None)
        if n is None:
            raise SystemExit(f"orig: {vid} has no settled word {settled!r} for its paragraph row")
        if begin:
            chapter.breaks[n] = None
        else:
            chapter.breaks.pop(n, None)


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
    out.breaks = paragraph_breaks(witness, found, len(out.words))
    near = None
    for n, w in enumerate(out.words):
        if n in found.at:
            w.token = near = found.at[n][0]
        elif near is not None:
            w.token = near + 1
    # A verse's pages are its paired words' (1738: the hOCR leaf of each word), not its OCR row's, whose edges may
    # reach back into the chapter's heading and summary on the leaf before (1738 Gen 44:1, leaf 106 → 107).
    if getattr(witness, "line_at", None):
        leaves = collections.defaultdict(set)
        for n, w in enumerate(out.words):
            if n in found.at:
                leaves[w.vid].add(witness.canvas_at[min(found.at[n][0], len(witness.canvas_at) - 1)])
        out.canvas = {vid: "–".join(map(str, sorted(ls)[::max(1, len(ls) - 1)])) for vid, ls in leaves.items()}
    seen = collections.Counter()
    after_read = [None] * len(out.words)
    for k, w in enumerate(out.words):
        seen[(w.vid, w.base)] += 1
        if not read:
            continue
        # A row's settled word may name its occurrence in the verse (cum#2): 1738 prints the preposition cum and
        # the conjunction quum, which the settled text spells alike.
        hit = read.get((w.vid, f"{w.base}#{seen[(w.vid, w.base)]}")) or read.get((w.vid, w.base))
        if hit:
            form, bar, marks = hit[0].partition(READ_AFTER)
            w.form, w.kind = form, "read"
            if bar:
                after_read[k] = marks
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
    # A row read on the page may give the marks after its word too (READ_AFTER: Græcè|? where the OCR read the ? as
    # an s, id| where it misplaced a parenthesis): they replace the OCR's.
    for w, forced in zip(out.words, after_read):
        if forced is not None:
            w.after, w.punct = forced, "read"
    return out


OPENING = 15   # words a chapter's drop capital may push in (1738 Gen 48:1, leaf 111): no paragraph is read there


def paragraph_breaks(witness, found, count):
    """{settled word index: (leaf, line, indent)} where the print begins a paragraph: the word paired with the first
    word of an indented line (`archive.indents`, held by the witness as `indented`: {token index: (leaf, line,
    indent)}), or, where that OCR word was not paired, the first settled word paired on the same line, less the OCR
    words before it on the line. None within a chapter's first OPENING words (the chapter begins one anyway)."""
    indented = getattr(witness, "indented", None)
    if not indented:
        return {}
    first = {}
    for n, at in sorted(found.at.items()):
        first.setdefault(at[0], n)                       # a run the OCR joined: its first word
    last = sorted((at[1], n) for n, at in found.at.items())
    out = {}
    for token, (leaf, line, indent, start) in indented.items():
        place = (leaf, line, indent)
        k = bisect.bisect_left(last, (start, -1)) - 1
        if token in first:
            n = first[token]
        elif k >= 0 and not any(witness.tokens[t][1] for t in range(last[k][0] + 1, start)):
            n = last[k][1] + 1                           # the word after the last one paired before the line
        else:
            line = witness.line_at[token]
            later = [(t, m) for t, m in first.items() if t > token and witness.line_at[t] == line]
            if not later:
                continue
            t, m = min(later)
            n = m - sum(1 for k in range(token, t) if witness.tokens[k][1])
            if n < 0 or (n != m and n in found.at):
                continue
        if OPENING <= n < count:
            out[n] = place
    return out


def stray_stops(chapter):
    """A stop the OCR has before a lower-case word, where the settled text has none, is a marginal note's read
    into the line (Lunaticus., Aue Rabbi.); where the settled text has ? or !, the OCR misread that mark."""
    words = chapter.words
    ot = bool(words) and books.select([words[0].vid.split(".")[0]])[0].testament == "vetus"
    for w, nxt in zip(words, words[1:]):
        if w.after == "." and w.punct == "ocr" and nxt.form[:1].islower() and nxt.vid == w.vid:
            settled = w.settled_after.replace("(", "").replace(")", "")
            if not settled:
                w.after, w.punct = "", "stray"
            elif settled[:1] in "?!":
                w.after, w.punct = settled[:1], "stray"
        # 1738's superscript footnote letters (Gen 2:7 in ᵃ eius) are read as ; ? or !: dropped before a lower-case
        # word where the settled text has no stop (its commas and colons are its own, and stay).
        # (1738 only: 1573's ? and ! are its own; in 1573 only the ; left from the -q; abbreviation goes, reuersusq;)
        elif w.after in (";", "?", "!") and w.punct == "ocr" and nxt.form[:1].islower() and nxt.vid == w.vid \
                and not w.settled_after.strip("()") and (ot or (w.after == ";" and w.form.endswith("que"))):
            w.after, w.punct = "", "stray"
        # and a colon is read as ? (Exod 21:8 redhibeto: in, OCR redhibeto?): the settled text's mark (1738 only).
        elif ot and w.after == "?" and w.punct == "ocr" and nxt.form[:1].islower() and nxt.vid == w.vid \
                and w.settled_after.strip("()") in (":", ";", ","):
            w.after, w.punct = w.settled_after.strip("()"), "stray"


READ_AFTER = "|"   # in a decision row's printed form: the marks printed after the word follow it (Græcè|?, id|)
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
            if w.kind in READ_KINDS and w.form and not (w.ocr or "")[1:2].isupper():
                # (a word set in capitals, as a chapter's first after its drop capital, prints V for U: 1738 TVm)
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


def spelling_prone(chapters):
    """A word still not read (none, guess, misread) whose settled spelling is one an approved rule writes for another
    (appellāvit for adpellavit, intellegam for intelligam) is marked `prone`, to be read on the page (PLAN.md §4,
    stage 2b): the base edition may print the old spelling, and the text follows the page."""
    table = spelling_rules()
    targets = set()
    for old, hit in dict.items(table):
        if rules.unligature(macronize.plain(hit[0])) != old:
            targets.add(rules.unligature(macronize.plain(hit[0])))
    # and the stem rules' new stems (condic- for condit-: 1738 Gen 42:20 conditionem, found by the sample check)
    stems = [rules.unligature(macronize.plain(new)) for old, new, _ in getattr(table, "stems", ())
             if rules.unligature(macronize.plain(new)) != old]
    for chapter in chapters:
        for w in chapter.words:
            plain = rules.unligature(macronize.plain(w.base.lower()))
            if w.kind in ("none", "guess", "misread") and (plain in targets or any(plain.startswith(s) for s in stems)):
                w.kind = "prone"


def settled_rows(osis, chapters=None):
    """{chapter: [(verse id, text)]}: the settled chapters' words (data/gold/), and, for a chapter named in `chapters`
    that is not settled, the draft's (text/draft/<USFM>.usfm) after stage 2, so stage 2b runs as soon as stage 2 is
    done (CLAUDE.md, PLAN.md §4)."""
    by_chapter = collections.defaultdict(list)
    for vid, row in gold.load(osis).items():
        _, c, v = tsv.parse_id(vid)
        if (chapters is None or c in chapters) and v > 0:
            by_chapter[c].append((vid, row["text"]))
    if chapters is not None:
        book = books.select([osis])[0]
        draft = latex.usfm_path(book, draft=True)
        if draft.exists() and any(c not in by_chapter for c in chapters):
            for vid, text, *_ in gold.rows(draft.read_text(encoding="utf-8"), osis):
                _, c, v = tsv.parse_id(vid)
                if c in chapters and c not in gold_chapters(osis) and v > 0:
                    by_chapter[c].append((vid, tied(text)))
    return by_chapter


_TIED = None


def tied(text):
    """A draft's text (Wikisource writes ae, oe) with the ligatures the settled text writes in the same word
    (Haec → Hæc, caelebs → cælebs, but Israelitae → Israelitæ, aer kept): taken word by word from every settled book,
    since a ligature marks a diphthong, not a hiatus (decision 16). A word no settled book has keeps ae/oe."""
    global _TIED
    if _TIED is None:
        seen = collections.defaultdict(collections.Counter)
        for book in books.BOOKS:
            for row in gold.load(book.osis).values():
                for word, is_word in align.words(row["text"]):
                    if is_word and re.search("[æœÆŒ]|ae|oe", word, re.I):
                        plain = rules.unmacron(word)
                        seen[rules.unligature(plain).lower()][plain.lower()] += 1
        _TIED = {k: c.most_common(1)[0][0] for k, c in seen.items()}

    def one(m):
        word = m.group()
        form = _TIED.get(word.lower())
        if not form:
            return word
        out = form if word.islower() else form[0].upper() + form[1:] if word[0].isupper() else form
        return out if rules.unligature(out).lower() == word.lower() else word
    return re.sub(r"[^\W\d_]+", one, text)


def gold_chapters(osis):
    return {tsv.parse_id(vid)[1] for vid in gold.load(osis)}


LEAF_MARK = re.compile(r"⁅(\d+)⁆\s*")
PARAGRAPH_MARK = "¶"


def printed_from_read_lines(rows):
    """A run of 1738's read lines (data/witnesses/read-1738/, every word read on the page as printed) as the printed
    text's conventions (decision 57): & and q; written out, the space 1738 sets before a mark dropped and one set
    after it. Spelling, u/v, i/j, capitals and misprints stay as read (decision 58)."""
    text = re.sub(r"(?<=\w)q;", "que", rows.replace("&", "et"))
    text = re.sub(r"\s+([,.;:?!)])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"([,;:?!.)])(?=[^\W\d_])", r"\1 ", text)
    return re.sub(r"\s+", " ", text).strip()


def from_read_lines(book, chapters, source, edits=()):
    r"""(USFM chapters, {verse id: leaf}) of the printed text built from 1738's read lines, for chapters drafted from
    them (Exodus 31–40, where Wikisource has none: data/review/exod31-40-stage2.md, Stage 2b). No OCR alignment is
    needed, since the lines are the page: they are joined into verses (hyphens joined, `ocrdraft.verses_of`), set
    by `printed_from_read_lines`, moved to the KJV's numbering by the draft's own versification edits, and given
    1738's paragraphs from its indents (`archive.indents`, as `build_chapter` reads them). A chapter's first word
    beside its drop capital is set as the other chapters' are (INterea → Interea, `ocrdraft.drop_capital`)."""
    from pipeline import archive, ocrdraft, versify
    rows = [r for r in ocrdraft.read_lines(source)]
    keep, on = [], False
    for row in rows:
        if m := re.match(r"\\c (\d+)$", row[3].strip()):
            on = int(m.group(1)) in chapters
        if on:
            keep.append(row)
    leaves = sorted({int(r[0]) for r in keep if str(r[0]).isdigit()})
    starts = archive.indents("1738", leaves)
    marked, previous = [], None
    for leaf, column, line, text in keep:
        if text.strip().startswith(("\\c", "%")):
            marked.append((leaf, column, line, text))
            continue
        lead = f"⁅{leaf}⁆ " if leaf != previous else ""      # a mark where a leaf begins (none inside a phrase)
        previous = leaf
        para = PARAGRAPH_MARK + " " if (int(leaf), int(line)) in starts else ""
        body = text.strip()
        if m := re.match(r"(#\d+)\s*(.*)$", body):          # a verse number first: the mark goes after it
            body = f"{m.group(1)} {para}{lead}{m.group(2)}"
        else:
            body = f"{para}{lead}{body}"
        marked.append((leaf, column, line, body))
    verses, _ = ocrdraft.verses_of(marked)
    lines, chapter = [], None
    for (c, v), text in verses.items():
        if c != chapter:
            lines += [f"\\c {c}"]
            chapter = c
        if v == 1:
            text = re.sub(r"^((?:¶\s*)?(?:⁅\d+⁆\s*)*)(\S+)",
                          lambda m: m.group(1) + opening_word(m.group(2)), text)
        lines.append(f"\\v {v} {text}")
    usfm = "\n".join(lines) + "\n"
    if edits:
        usfm, _ = versify.apply_edits(usfm, book.osis, edits)
    # Each verse's whole text (a merged verse runs on over the lines after it), and its leaf: the last leaf mark
    # before its first word. Then the marks go.
    pages, leaf, chapter, verses_out = {}, None, None, []      # verses_out: [("c", n) | ("v", n, text)]
    for piece in re.split(r"(\\c \d+|\\v \d+(?:-\d+)? ?)", usfm):
        if piece.startswith("\\c "):
            chapter = int(piece.split()[1])
            verses_out.append(("c", chapter))
        elif piece.startswith("\\v "):
            verses_out.append(("v", tsv.parse_number(piece.split()[1]), ""))   # 12-83: a range (Num 7)
        elif verses_out and verses_out[-1][0] == "v":
            first = re.match(r"\s*(?:¶\s*)?⁅(\d+)⁆", piece)
            pages[f"{book.osis}.{chapter}.{verses_out[-1][1]}"] = str(int(first.group(1)) if first else leaf)
            for m in LEAF_MARK.finditer(piece):
                leaf = int(m.group(1))
            text = re.sub(r"\\[a-z]+\d*\s*", " ", LEAF_MARK.sub("", piece))     # \p from versify: not 1738's
            verses_out[-1] = ("v", verses_out[-1][1], re.sub(r"\s+", " ", text).strip())
    # Paragraphs: one at each chapter's start, and where 1738 indents (inside a verse: \p in the verse's line).
    result = []
    for item in verses_out:
        if item[0] == "c":
            result += ["", f"\\c {item[1]}", "\\p"]
            continue
        _, number, body = item
        parts = [printed_from_read_lines(p) for p in body.split(PARAGRAPH_MARK)]
        if not parts[0] and len(parts) > 1:                  # the verse begins the paragraph
            if result[-1] != "\\p":
                result.append("\\p")
            parts = parts[1:]
        result.append(f"\\v {number} {parts[0]}")
        for part in parts[1:]:
            result += ["\\p", part]
    return "\n".join(result).lstrip("\n") + "\n", pages


def verse_paragraph_rows(text, book, chapters):
    r"""The ¶ and ¶- rows (`paragraph_rows`) of these chapters set in printed USFM from read lines: a paragraph
    begun or taken away before a verse whose first settled word the row names (1738 Exod 34:7, the capitals of the
    proclamation flush with the lines around them, not indented). A row naming a later word of the verse (`Hæc#2`)
    can only take away a paragraph begun inside the verse before that word (1738 Lev 12:1, 13:2: the lines beside a
    chapter's drop capital, indented but not a paragraph)."""
    from pipeline import gold
    first = {}
    for vid, row in gold.load(book.osis).items():
        words = re.findall(r"[^\W\d_]+", re.sub(r"\\f .*?\\f\*", "", row["text"]))
        if words:
            first[vid] = words[0]
    lines = text.splitlines()
    for (vid, word), (begin, _) in paragraph_rows(book.osis).items():
        _, c, v = tsv.parse_id(vid)
        if c not in chapters:
            continue
        chapter_at = lines.index(f"\\c {c}")
        k = next(i for i in range(chapter_at, len(lines)) if lines[i].startswith(f"\\v {v} "))
        if first.get(vid) != word.split("#")[0] or word.partition("#")[2] not in ("", "1"):
            inside = word if begin is False else None
            for i in range(k + 1, len(lines) - 1):
                if lines[i].startswith(("\\v ", "\\c ")):
                    break
                if inside and lines[i] == "\\p" and same_word(lines[i + 1].split()[0] if lines[i + 1].split() else "",
                                                              inside.split("#")[0]):
                    lines[i - 1] = lines[i - 1] + " " + lines[i + 1]
                    del lines[i:i + 2]
                    break
            else:
                raise SystemExit(f"orig: the paragraph row {vid} {word!r} is neither the verse's first word "
                                 f"({first.get(vid)!r}) nor a paragraph inside it to take away")
            continue
        if begin and lines[k - 1] != "\\p":
            lines.insert(k, "\\p")
        elif not begin and lines[k - 1] == "\\p":
            del lines[k - 1]
    return "\n".join(lines) + "\n"


def same_word(printed, settled):
    """Whether a printed word (with its punctuation) is this settled word, under the folds (case, macrons, æ/ae,
    i/j, u/v)."""
    return rules.fold(re.sub(r"[^\w]", "", printed)) == rules.fold(settled)


def write_from_read_lines(book, chapters):
    """`pipeline orig BOOK CH-CH --read-lines`: the printed text of chapters drafted from 1738's read lines
    (`from_read_lines`), merged into text/orig/draft/<USFM>.usfm beside the chapters built from the OCR, their leaves
    into data/orig/<osis>.pages.tsv, and a review file. Returns the paths written."""
    span = f"{chapters.start}-{chapters.stop - 1}"
    source = paths.WITNESSES / "read-1738" / f"{book.osis}{span}.tsv"
    if not source.exists():
        raise SystemExit(f"no {source.relative_to(paths.ROOT).as_posix()}: these chapters were not drafted from read lines")
    edits_file = paths.DATA / "versification" / f"{book.osis}{span}.draft.edits.tsv"
    edits = [e for e in tsv.read(edits_file) if e.get("status", "applied") == "applied"] if edits_file.exists() else []
    text, pages = from_read_lines(book, chapters, source, edits)
    text = verse_paragraph_rows(text, book, chapters)
    target = path(book)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        text = merge_usfm(target.read_text(encoding="utf-8"), text)
    else:
        text = "\n".join(header_lines(book)) + "\n\n" + text
    target.write_text(text, encoding="utf-8", newline="\n")
    pages_file = pages_path(book)
    kept = {r["id"]: r["canvas"] for r in tsv.read(pages_file)
            if tsv.parse_id(r["id"])[1] not in chapters} if pages_file.exists() else {}
    rows = {**kept, **pages}
    tsv.write(pages_file, sorted(rows.items(), key=lambda kv: tsv.parse_id(kv[0])), header=("id", "canvas"))
    return [target, pages_file]


def merge_usfm(old, new):
    """The draft file `old` with the chapters `new` holds put in place (and new ones added in order): a draft of
    Exodus 21–30 beside the one of 1–20, each built when its stage 2 is done."""
    def split(text):
        pieces = re.split(r"(?m)^(?=\\c )", text)
        return pieces[0].rstrip() + "\n", {int(piece.split()[1]): piece.rstrip() for piece in pieces[1:]}
    head, chapters = split(old)
    chapters.update(split(new)[1])
    return head + "\n" + "\n\n".join(chapters[c] for c in sorted(chapters)) + "\n"


def base_witness(osis):
    """The base edition's OCR as an align.Witness: 1573 (MDZ hOCR) for the New Testament, 1738 (archive.org
    bibliasacraexseb01cast, ABBYY) for the Old (decisions 1 and 24)."""
    if books.select([osis])[0].testament == "novum":
        return mdz.witness()
    from pipeline import archive
    path = paths.SOURCES / "archive" / "1738" / "hocr.html"
    if not path.exists():
        raise SystemExit(f"{path.relative_to(paths.ROOT).as_posix()} is missing: python -m pipeline fetch archive 1738 --hocr")
    # Read from the hOCR (the same words as text.txt), so each word has its leaf and line: the page links and the
    # paragraphs, which 1738 marks by indenting (archive.indents).
    w = archive.witness("1738")
    lines = {place: token for token, place in w.line_start.items()}
    w.indented = {}
    for (leaf, line), (indent, word) in archive.indents("1738").items():
        if (leaf, line) not in lines:
            continue
        token = start = lines[(leaf, line)]
        first = align.words(align.clean(word))
        # The line's text starts at this word, past a verse number the OCR may have read as letters (1738 Gen 38:12 "la").
        for k in range(token, min(token + 6, len(w.tokens))):
            if first and w.tokens[k][0] == first[0][0]:
                token = k
                break
        w.indented[token] = (leaf, line, indent, start)
    return w


def build(osis, chapters, witness=None, known=None):
    """{chapter: Chapter} for these settled chapters of a book (all of them when chapters is None). known: a lexicon
    (`lexicon`), by default this book's own."""
    witness = witness or base_witness(osis)
    by_chapter = settled_rows(osis, chapters)
    read = overrides(osis)
    built = {c: build_chapter(witness, by_chapter[c], c, read) for c in sorted(by_chapter)}
    marks = paragraph_rows(osis)
    for chapter in built.values():
        apply_paragraph_rows(chapter, {k: v for k, v in marks.items() if tsv.parse_id(k[0])[1] == chapter.number})
    known = known if known is not None else lexicon(built.values())
    from_lexicon(built.values(), known)
    check_e_caudata(built.values(), known)
    printer_habits(built.values(), books.select([osis])[0].testament)
    spelling_prone(built.values())
    fix_ligatures(built.values(), ligature_stems(known))
    if books.select([osis])[0].testament == "vetus":
        untie_capitals(built.values())
        cc_for_oe(built.values())
        retie(built.values())
    for chapter in built.values():                       # both printers' drop capitals (orig-drop-capitals.md)
        if chapter.words and chapter.words[0].kind != "read":
            chapter.words[0].form = opening_word(chapter.words[0].form)
    for chapter in built.values():
        stray_stops(chapter)
    return built


def untie_capitals(chapters):
    """1738 has the æ and œ ligatures in lower case only: a capital is printed as two letters (in Aegypto, leaf 114;
    Aegytio, Exod 2:19, leaf 116), where 1573 prints Æ (Ægypti, canvas 837). `choose` ties the OCR's Ae like ae, so
    the capital is untied here; a word read on the page keeps its row's form, and a word in capitals is left alone."""
    for chapter in chapters:
        for w in chapter.words:
            if w.kind != "read" and w.form[:1] in "ÆŒ" and not w.form.isupper():
                w.form = {"Æ": "Ae", "Œ": "Oe"}[w.form[0]] + w.form[1:]


def retie(chapters):
    """1738 prints æ and œ in lower case as ligatures, and its OCR writes them out (aetatis): a form not read on the
    page that took the OCR's spelling through the lexicon is tied where the settled word has the ligature, as
    `choose` ties a word read in the OCR (ætatis, seen on leaves 87 and 120)."""
    for chapter in chapters:
        for w in chapter.words:
            if w.kind == "read" or not re.search("ae|oe", w.form):
                continue
            tied = re.sub("ae|oe", lambda m: {"ae": "æ", "oe": "œ"}[m.group()], w.form)
            if letters(tied).replace("œ", "æ").lstrip("h") == letters(printerize(w.base)).replace("œ", "æ").lstrip("h"):
                w.form = tied


def opening_word(word):
    """A chapter's first word beside its drop capital, which the print sets with a small capital or two after the
    initial (AVditionem, AD, CVm), as a normal capitalized word, with the printers' u inside a word for the small
    capital V (Auditionem, Ad, Cum; Nathan, 2026-11-15, data/review/exod31-40-orig.md). A word wholly in capitals
    beyond two letters (PRINCIPIO, PRIMVM, a book's first word) is the print's own convention and is kept."""
    if re.match(r"^[A-Z]{2,}[a-zæœàèìòùáéíóú]", word) or re.match(r"^[A-Z]v[a-z]", word) or \
            (word.isupper() and len(word) == 2):
        return word[0] + word[1:].lower().replace("v", "u")
    return word


def cc_for_oe(chapters):
    """1738's OCR reads the œ of cœp-, cœn- as ce (cceperunt, ccenam), and the lexicon learned it: where the settled
    word begins with cœ and the form with cc, the print has cœ (cœperunt, seen on leaf 98, Gen 37:18)."""
    for chapter in chapters:
        for w in chapter.words:
            if w.kind != "read" and w.form[:3].lower() == "cce" and w.base[:2].lower() in ("cœ", "cē"):   # cēna, 1738 cœna
                w.form = w.form[0] + "œ" + w.form[3:]


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
    and indents its paragraphs (Gen 44:3, 44:13 on leaf 107), read from its hOCR (`Chapter.breaks`): a paragraph
    begins at a verse or, where the print begins it inside one, in the verse's line."""
    per_verse = book.testament == "novum"
    lines = header[:]
    for number, chapter in built.items():
        lines += ["", f"\\c {number}"] + ([] if per_verse else ["\\p"])
        verses = collections.defaultdict(list)
        for n, w in enumerate(chapter.words):
            verses[w.vid].append((n, w))
        for vid, items in verses.items():
            v = tsv.parse_id(vid)[2]
            if per_verse:
                lines += ["\\p", f"\\v {v} {verse_text([w for _, w in items])}"]
                continue
            pieces, run = [], []
            for n, w in items:
                if n in chapter.breaks and run:
                    pieces.append(run)
                    run = []
                elif n in chapter.breaks:
                    lines.append("\\p")
                run.append(w)
            pieces.append(run)
            lines.append(f"\\v {v} {verse_text(pieces[0])}")
            for run in pieces[1:]:
                lines += ["\\p", verse_text(run)]
    return "\n".join(lines) + "\n"


def header_lines(book):
    """The reading edition's header (\\id … \\mt): every line before its first chapter, blank lines dropped. A book
    with no settled chapter yet (Leviticus 1–11) takes its draft's."""
    lines = []
    source = latex.usfm_path(book)
    if not source.exists():
        source = paths.ROOT / "text" / "draft" / f"{book.usfm}.usfm"
    for line in source.read_text(encoding="utf-8").splitlines():
        if line.startswith("\\c "):
            break
        if line.strip():
            lines.append(line)
    return lines


def pages_path(book):
    """data/orig/<osis>.pages.tsv: the base edition's page (canvas) of each verse, for the site's links to the page
    images (1573: MDZ canvas; 1738: the hOCR's leaf, archive.org's page image n<leaf − 1>). Metadata, not the
    text: rewritten whenever the pages are read again."""
    return paths.DATA / "orig" / f"{book.osis}.pages.tsv"


def write_pages(book, built):
    """Write the pages file for these chapters, keeping rows of the book's other chapters. Both base editions have
    them: 1573's canvases (MDZ hOCR) and 1738's leaves (archive.org hOCR)."""
    rows = {vid: canvas for c in built.values() for vid, canvas in c.canvas.items() if canvas}
    if not rows:
        return None
    target = pages_path(book)
    if target.exists():
        kept = {r["id"]: r["canvas"] for r in tsv.read(target) if tsv.parse_id(r["id"])[1] not in built}
        rows = {**kept, **rows}
    target.parent.mkdir(parents=True, exist_ok=True)
    tsv.write(target, sorted(rows.items(), key=lambda kv: tsv.parse_id(kv[0])), header=("id", "canvas"))
    return target


def load_pages(osis):
    """{verse id: canvas, e.g. "762" or "762–763"} from data/orig/<osis>.pages.tsv ({} without one)."""
    path = paths.DATA / "orig" / f"{osis}.pages.tsv"
    return {r["id"]: r["canvas"] for r in tsv.read(path)} if path.exists() else {}


def sheets(book, built, witness, kinds=("doubt", "prone"), size=12):
    """Contact sheets of the words of these kinds on the base edition's page images, for reading them (1738: the
    line of the word's paired neighbours, cut from archive.org's page; `archive.sheet`). Returns [(sheet path,
    [(label, verse id, settled word, form now, leaf, line)])]; the sheets go to sources/archive/crops/sheets/."""
    from pipeline import archive
    if not getattr(witness, "line_at", None):
        raise SystemExit("orig --sheets: only for the Old Testament (1738's hOCR); the NT is read with mdz.fetch_crop")
    items = []
    for chapter in built.values():
        words = chapter.words
        for n, w in enumerate(words):
            if w.kind not in kinds or w.token is None:
                continue
            leaf, line = witness.line_at[min(w.token, len(witness.line_at) - 1)]
            # The word's own line, found by the neighbours' words on this leaf and the next (the OCR's reading order
            # breaks beside a drop capital or a chapter's heading): anchored on the longest neighbour.
            span = [rules.unmacron(x.base) for x in words[max(0, n - 3):n + 4]]
            here = n - max(0, n - 3)
            anchor = max((k for k in range(len(span)) if k != here), key=lambda k: (len(span[k]), -abs(k - here)))
            found = archive.find("1738", span, anchor, leaves={leaf - 1, leaf, leaf + 1})
            if found is not None:
                leaf, line = found.canvas, found.line
            first, last = max(1, line - 1), line + 1
            context = " ".join(x.base for x in words[max(0, n - 2):n + 3])
            occurrence = sum(1 for x in words[:n + 1] if x.vid == w.vid and x.base == w.base)
            label = f"{len(items) + 1}. {w.vid} {w.base}#{occurrence}  [{context}]  leaf {leaf}"
            items.append((label, w.vid, f"{w.base}#{occurrence}", w.form, leaf, line,
                          archive.line_box("1738", leaf, first, last, pad=(90, 8))))
    out = []
    folder = archive.CROPS / "sheets"
    for k in range(0, len(items), size):
        chunk = items[k:k + size]
        path = folder / f"{book.osis}-{chunk[0][0].split('.')[0]}.jpg"
        archive.sheet("1738", [(i[0], i[4], i[6]) for i in chunk], path, 760)
        out.append((path, [i[:6] for i in chunk]))
    return out


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
    "prone": "not read here, and an approved rule writes the settled spelling for another: to be read on the page",
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
              "Paragraphs are 1738's own, read from the indents in its hOCR (listed below)")
    out = [f"# {name} {span} as printed ({year}): the draft for review", "",
           f"Built {today} by `python -m pipeline orig {name} {command}` → `{target}`. The words are the settled chapters' "
           f"(`text/`); their spelling, capitals and punctuation are {edition}'s, read from its OCR as "
           "`pipeline/orig.py` describes. Expanded: *&*, *q;*, the nasal bar, long s, *ę*. Kept: u/v and i/j as "
           f"printed. Dropped: the accents (*verò*, *quòd*, *à*). {layout} "
           "(HUMAN.md decision 57). Regenerate after changing `data/decisions/" + name + ".orig.tsv`.", "",
           "**Decision:** pending", "", "## How each word was made", "",
           "| Kind | Words | |", "|---|---:|---|"]
    for kind in ("ocr", "rule", "variant", "ę", "nasal", "misread", "lexicon", "read", "doubt", "prone", "guess", "none"):
        if kinds[kind]:
            out.append(f"| {kind} | {kinds[kind]} | {KIND_NOTES[kind]} |")
    out += [f"| all | {len(words)} | |", ""]
    read = overrides(name)
    if read:
        out += ["## Read on the page", "",
                "Where the OCR could not decide. Several differ from the settled text by more than spelling: "
                "the reading edition may want to look again at these (marked ⚑).", ""]
        for (vid, settled), (printed, reason) in read.items():
            settled = settled.split("#")[0]
            plain = re.sub(r"[ ']", "", printed)
            # A spelling the approved rules normalize (quum, quoties, eamdem) is not flagged: the reading edition has it.
            same = normalized(plain) == normalized(settled) or variant_key(plain) == variant_key(settled) or \
                variant_key(plain).startswith(variant_key(settled))
            if plain.lower().endswith("que") and not settled.lower().endswith("que"):
                same = False                                 # a -que the settled text lacks (1738 Exod 18:5 Cumque)
            flag = "" if printed == JOINED or "misprint" in reason or same else "⚑ "
            if "misprint" in reason:
                flag = "✱ "
            out.append(f"- {flag}**{vid[len(name) + 1:] if vid.startswith(name + '.') else vid}** *{settled}* → "
                       f"*{printed}*: {reason}")
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
    left = [w for w in words if w.kind in ("none", "guess", "misread", "doubt", "prone")]
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
    if not nt:
        breaks = [(c.words[n], place) for c in built.values() for n, place in sorted(c.breaks.items())]
        read_rows = paragraph_rows(name)
        out += [f"## Paragraphs ({len(breaks)} inside the chapters)", "",
                "1738 runs its verses on and marks a paragraph by indenting its first line. Read from the hOCR "
                "(`archive.indents`: a line starting 40–140 px inside the column's margin after a line that ends a "
                "sentence; drop capitals, summaries and 1738's footnotes left out) and set before the word that "
                "begins the line; a paragraph read on the page is a `¶` row in `data/decisions/" + name + ".orig.tsv`. "
                "Every chapter also begins one. Leaf = archive.org's hOCR page (its image is page n<leaf − 1>).", "",
                "; ".join(f"{w.vid[len(name) + 1:]} *{w.form}* (" +
                          (f"leaf {place[0]}, line {place[1]}" if place else "read on the page: " +
                           read_rows.get((w.vid, w.base), (True, ""))[1]) + ")" for w, place in breaks), ""]
    marks = "L. … G." if nt else "G. … H. (and L., G.L.)"
    found = "; ".join(f"{vid[len(name) + 1:]} *{' '.join(ws)}*" for c in built.values() for vid, ws in c.marked.items())
    out += ["## Open questions", "",
            f"1. **Accents.** {year} prints grave accents on adverbs (*verò*, *cùm*, *continuò*) and on *quòd*, *à* "
            "and *hîc*. Dropped here, since the OCR reads them unevenly. Keeping them means restoring them by rule, "
            "or reading them page by page.",
            f"2. **Chapter summaries.** {year} heads each chapter with a summary: left out of the printed text, as "
            "of the reading edition (decisions 50, 67).",
            "3. **Apostrophes and word division** follow the print where read on the page (*Is'ne*, Matt 26:25; "
            "*plusquam*, 26:53; decision 58); elsewhere the settled text's division stands until read.",
            f"4. **Castellio's {marks} marks**: the words are kept, the marks dropped, as in the reading edition. "
            + (f"Found here: {found}." if found else "None found by the aligner in these chapters."),
            "5. **Capitals of words the OCR missed** follow the settled text (Matt 26:41 *spiritus*, 1573 *Spiritus*).",
            ""]
    return "\n".join(out)
