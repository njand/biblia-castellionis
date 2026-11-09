"""LaTeX ↔ USFM: migrating the finished chapters, and regenerating the print LaTeX from the USFM master.

The LaTeX in LaTeX/biblia/**/<slug>.tex is only ever read here. `to_usfm` converts a book file; `to_latex`
writes the book back in the same markup; `compare` shows the round trip loses nothing that prints.

  \\Liber[long]{short}             \\id, \\h short, \\toc1 long, \\toc2 short, \\mt1 long (\\\\ → //)
  \\Caput, \\Versus                 \\c N, \\v N (numbered as the LaTeX counts them)
  blank line                       \\p; prose that resumes after poetry without one → \\m
  verse + patverse* + \\indentpattern{…}   \\q1/\\q2/\\q3 lines (indent digit + 1); \\medskip → \\b
  \\emph{…}                         \\qt …\\qt* (closed and reopened at each line and verse)
  ``…'' `…'  \\-                    “…” ‘…’, soft hyphen (U+00AD)

Not carried over (none of it prints): comments, including the commented \\summary{} headings and \\footnote{}s
of Genesis (`comments` lists them), and whether a blank line stood before a poem. A chapter whose \\Caput is
commented out is a draft: it is converted from its commented lines into a separate draft file."""

import difflib
import re

from pipeline import paths

TEXT = paths.ROOT / "text"
DRAFT = TEXT / "draft"
SOFT_HYPHEN = "\u00ad"
TO_UNICODE = [("``", "“"), ("''", "”"), ("`", "‘"), ("'", "’"), ("\\-", SOFT_HYPHEN)]
FROM_UNICODE = [(char, latex) for latex, char in TO_UNICODE]
POETRY_ENVS = ("verse", "patverse*")
TOKEN = re.compile(r"""
    (?P<blank>\n[ \t]*\n\s*)
  | (?P<cmd>\\(?:Versus|Caput|medskip)\b[ \t]*)
  | (?P<indent>\\indentpattern\{(?P<pattern>\d*)\})
  | (?P<env>\\(?:begin|end)\{(?P<name>[^}]*)\})
  | (?P<newline>\\\\)
  | (?P<empty>\{\})
  | (?P<emph>\\emph\{)
  | (?P<close>\})
  | (?P<text>(?:[^\\{}\n]|\\-|\n(?![ \t]*\n))+)
  | (?P<bad>\\[A-Za-z]+|\\.|\{)
""", re.VERBOSE)


class LatexError(ValueError):
    pass


def latex_path(book):
    return paths.LATEX / f"{book.testament} foedus" / f"{book.slug}.tex"


def usfm_path(book, draft=False):
    return (DRAFT if draft else TEXT) / f"{book.usfm}.usfm"


def strip_comments(source):
    """Drop unescaped `%…`; drop lines that held only a comment, so they never count as blank lines."""
    out = []
    for line in source.splitlines():
        code = re.sub(r"(?<!\\)%.*", "", line)
        if code.strip() or not line.strip():
            out.append(code.rstrip())
    return "\n".join(out)


def comments(source):
    """[(line number, comment)] for comments outside draft chapters: what the USFM does not keep."""
    found, draft = [], False
    for number, line in enumerate(source.splitlines(), 1):
        if re.match(r"\s*%\s*\\Caput\b", line):
            draft = True
        elif re.match(r"\s*\\Caput\b", line):
            draft = False
        match = re.search(r"(?<!\\)%.*", line)
        if match and not draft:
            found.append((number, match.group(0)))
    return found


def split_book(source):
    """(long title, short title, [(chapter number, LaTeX body, is_draft)]). A draft's lines are uncommented."""
    head = re.match(r"\s*\\Liber(?:\[(?P<long>[^\]]*)\])?\{(?P<short>[^}]*)\}", source)
    if not head:
        raise LatexError("no \\Liber[…]{…} at the top of the file")
    pieces = re.split(r"^([ \t]*%?[ \t]*\\Caput\b.*)$", source[head.end():], flags=re.MULTILINE)
    if strip_comments(pieces[0]).strip():
        raise LatexError(f"text before the first \\Caput: {pieces[0].strip()[:60]!r}")
    chapters = []
    for number, (caput, body) in enumerate(zip(pieces[1::2], pieces[2::2]), 1):
        draft = caput.lstrip().startswith("%")
        rest = caput.split("\\Caput", 1)[1]
        if draft:
            body = "\n".join(re.sub(r"^\s*%[ ]?", "", line) for line in body.splitlines())
        chapters.append((number, strip_comments(rest + "\n" + body), draft))
    return head.group("long") or head.group("short"), head.group("short"), chapters


class _Writer:
    """Builds the USFM lines of one chapter from the LaTeX tokens."""

    def __init__(self, where):
        self.where = where
        self.lines = []
        self.pending = "p"            # paragraph marker waiting for content
        self.poetry = False
        self.pattern, self.line_no = [], 0
        self.emph = False             # inside \emph{…}
        self.qt_open = False          # a \qt is open on the current USFM line
        self.verse = 0

    def fail(self, message):
        raise LatexError(f"{self.where}: {message}")

    def materialize(self):
        if self.pending is not None:
            self.lines.append(f"\\{self.pending} ")
            self.pending = None

    def next_poetry_line(self):
        level = self.pattern[self.line_no % len(self.pattern)] + 1 if self.pattern else 1
        self.line_no += 1
        self.pending = f"q{level}"

    def close_qt(self):
        if self.qt_open:
            self.lines[-1] = self.lines[-1].rstrip() + "\\qt*"
            self.qt_open = False

    def add(self, text):
        if not text.strip():
            if self.pending is None and self.lines:
                self.lines[-1] += text
            return
        if self.verse == 0:
            self.fail(f"text before the first \\Versus: {text[:40]!r}")
        self.materialize()
        if self.emph and not self.qt_open:
            self.lines[-1] += "\\qt "
            self.qt_open = True
            text = text.lstrip()
        self.lines[-1] += text

    def verse_mark(self):
        self.verse += 1
        self.close_qt()
        mark = f"\\v {self.verse} "
        if self.pending is not None:
            self.materialize()
            if self.lines[-1].startswith("\\q"):
                self.lines[-1] += mark             # "\q1 \v 2 …": a poetry line that opens with a verse
            else:
                self.lines.append(mark)            # prose: each verse on a line of its own
        elif self.lines and self.lines[-1].startswith("\\q"):
            self.lines[-1] = self.lines[-1].rstrip() + " " + mark
        else:
            self.lines.append(mark)

    def token(self, kind, match):
        value = match.group(0)
        if kind == "empty":
            return                                 # `{}` only keeps two quote marks apart: '{}''
        if kind == "blank":
            if self.poetry:                        # a stanza break; the indent pattern runs on across it
                self.close_qt()
                self.lines.append("\\b")
                if self.pending is None:
                    self.next_poetry_line()
            elif self.pending in (None, "m"):
                self.pending = "p"
        elif kind == "cmd":
            command = value.strip()
            if command == "\\Versus":
                self.verse_mark()
            elif command == "\\medskip":
                if not self.poetry:
                    self.fail("\\medskip outside poetry")
                self.lines.append("\\b")
            else:
                self.fail("\\Caput inside a chapter")
        elif kind == "indent":
            self.pattern = [int(d) for d in match.group("pattern")]
        elif kind == "env":
            name, begin = match.group("name"), value.startswith("\\begin")
            if name not in POETRY_ENVS:
                self.fail(f"unknown environment {name!r}")
            if name == "verse":
                self.close_qt()
                if begin:
                    self.poetry, self.line_no = True, 0
                    self.next_poetry_line()
                else:
                    self.poetry, self.pattern = False, []
                    self.pending = "m"
        elif kind == "newline":
            if not self.poetry:
                self.fail("\\\\ outside poetry")
            self.close_qt()
            self.next_poetry_line()
        elif kind == "emph":
            if self.emph:
                self.fail("nested \\emph")
            self.emph = True
        elif kind == "close":
            if not self.emph:
                self.fail("unbalanced }")
            self.close_qt()
            self.emph = False
        elif kind == "text":
            text = re.sub(r"\s+", " ", value)
            for latex, char in TO_UNICODE:
                text = text.replace(latex, char)
            self.add(text)
        else:
            self.fail(f"unknown command {value!r}")

    def finish(self):
        if self.poetry or self.emph:
            self.fail("chapter ends inside poetry or \\emph")
        return [re.sub(r"\s+", " ", line).strip() for line in self.lines]


def chapter_usfm(body, where):
    """(USFM lines without the \\c line, number of verses) for one chapter's LaTeX body."""
    writer = _Writer(where)
    for match in TOKEN.finditer(body):
        kind = match.lastgroup
        kind = {"pattern": "indent", "name": "env"}.get(kind, kind)
        writer.token(kind, match)
    return writer.finish(), writer.verse


def to_usfm(source, book):
    """(USFM of the live chapters, USFM of the draft chapters or None, {chapter: verses})."""
    long, short, chapters = split_book(source)
    header = [f"\\id {book.usfm} Biblia Sacra ex Sebastiani Castellionis interpretatione", "\\usfm 3.0",
              "\\ide UTF-8", f"\\h {short}", f"\\toc1 {long.replace(chr(92) * 2, ' ')}", f"\\toc2 {short}",
              f"\\mt1 {long.replace(chr(92) * 2, ' // ')}"]
    live, draft, counts = list(header), list(header), {}
    for number, body, is_draft in chapters:
        lines, verses = chapter_usfm(body, f"{book.osis}.{number}")
        counts[number] = verses
        (draft if is_draft else live).extend(["", f"\\c {number}", *lines])
    has_draft = any(is_draft for _, _, is_draft in chapters)
    return "\n".join(live) + "\n", ("\n".join(draft) + "\n") if has_draft else None, counts


# ---------------------------------------------------------------- USFM → LaTeX

HEADER = {"id", "usfm", "ide", "h", "toc1", "toc2", "toc3", "mt", "mt1", "rem"}
PARAGRAPHS = {"p", "m", "nb", "b", "q1", "q2", "q3", "q4"}
TITLES = {"cd": "Argumentum", "d": "Titulus"}   # chapter summary (verse 0), psalm title: one line each; the commands
                                                # are defined by the generated print LaTeX (pipeline/pdf.py)


def unicode_to_latex(text):
    """Plain text → LaTeX: ’” → '{}'' as in the original, then the quotation marks and soft hyphens."""
    text = re.sub(r"(?<=[“”‘’])(?=[“”‘’])", "{}", text)
    for char, latex in FROM_UNICODE:
        text = text.replace(char, latex)
    return text


def _inline(text):
    """[(kind, value)] for a stretch of paragraph content: ("v", 3), ("char", "qt"), ("text", "…")."""
    content = []
    while text:
        # An opening marker takes one space after it; the space after a closing one (\qt*) is text.
        match = re.search(r"\\(\+?[a-z]+\d*\*)|\\(\+?[a-z]+\d*)[ ]?", text)
        if not match:
            content.append(("text", text))
            break
        if match.start():
            content.append(("text", text[:match.start()]))
        name, text = match.group(1) or match.group(2), text[match.end():]
        if name == "v":
            number, text = re.match(r"(\d+)\s*(.*)", text, re.DOTALL).groups()
            content.append(("v", int(number)))
        else:
            content.append(("char", name))
    return content


def blocks(usfm):
    """[(marker, content)]: each paragraph-level marker with the content that follows it. Header markers and
    \\c carry their line's text as content."""
    out = []
    for line in usfm.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = re.match(r"\\([a-z]+\d*)(?:\s+(.*)|$)", stripped)
        marker = match.group(1) if match else None
        if marker in HEADER or marker in TITLES or marker == "c":
            out.append((marker, (match.group(2) or "").strip()))
            continue
        if marker in PARAGRAPHS:
            out.append((marker, []))
            stripped = match.group(2) or ""
        elif not out or not isinstance(out[-1][1], list):
            raise LatexError(f"USFM text outside a paragraph: {stripped[:40]!r}")
        elif out[-1][1]:
            stripped = " " + stripped           # a line break inside a paragraph is a space
        for kind, value in _inline(stripped):
            if kind == "char" and value in PARAGRAPHS:
                out.append((value, []))         # a marker inside a line ("… lēgistis? \q1 \qt …") starts a block too
            else:
                out[-1][1].append((kind, value))
    return out


def to_latex(usfm):
    """The book's LaTeX, in the markup of LaTeX/biblia (\\Liber, \\Caput, \\Versus, verse/patverse*)."""
    parsed = blocks(usfm)
    header = {marker: content for marker, content in parsed if marker in HEADER}
    long = header.get("mt1", header.get("h", "")).replace(" // ", "\\\\")
    short = header.get("h", long)
    out = [f"\\Liber[{long}]{{{short}}}\n"]
    body = [(m, c) for m, c in parsed if m not in HEADER]
    poem, start, stanza, verse = False, True, False, 0
    closed_at = None      # where the last \emph{…} closed, while only line breaks and verse numbers follow it

    def close_poem():
        nonlocal poem
        if poem:
            out.append("\n\\end{patverse*}\n\\end{verse}")
            poem = False

    for index, (marker, content) in enumerate(body):
        if marker == "c":
            close_poem()
            out.append("\n\n\\Caput\n")
            verse, start = 0, True
            continue
        if marker in TITLES:                     # printed above the chapter's drop cap
            if out[-1] != "\n\n\\Caput\n":
                raise LatexError(f"\\{marker} must follow \\c directly")
            text = re.sub(r"\\\+?[a-z]+\d*\*?\s?", "", content)
            out[-1] = f"\n\n\\{TITLES[marker]}{{{unicode_to_latex(text)}}}\n\\Caput\n"
            continue
        if marker == "b":
            out.append("\n\n")                   # a stanza break: the line before it has no \\
            stanza, closed_at = True, None
            continue
        if marker in ("p", "m", "nb"):                # \nb: a chapter that opens mid-sentence (KJV 6:22 | 7:1)
            closed_at = None
            close_poem()
            if not start:
                out.append("\n\n" if marker == "p" else "\n")
        elif not poem:
            levels = []
            for later, _ in body[index:]:
                if later == "b":
                    continue
                if not later.startswith("q"):
                    break
                levels.append(str(int(later[1:]) - 1))
            out.append(("" if start else "\n\n") + f"\\indentpattern{{{''.join(levels)}}}\n"
                       "\\begin{verse}\n\\begin{patverse*}\n")
            poem = True
        elif not stanza:
            out.append("\\\\\n")
        start = stanza = False
        for position, (kind, value) in enumerate(content):
            if kind == "v":
                verse += 1
                if value != verse:
                    raise LatexError(f"\\v {value} where verse {verse} was expected")
                if position and not poem:
                    out[-1] = out[-1].rstrip(" ")
                    out.append("\n")
                out.append("\\Versus ")
            elif kind == "char":
                if value not in ("qt", "qt*"):
                    raise LatexError(f"no LaTeX for \\{value}")
                if value == "qt*":
                    closed_at = len(out)
                    out.append("}")
                elif closed_at is not None:
                    out[closed_at] = ""            # \qt was closed only for a line or verse: one \emph{…}
                else:
                    out.append("\\emph{")
                continue
            elif value.strip():
                out.append(unicode_to_latex(value))
            else:
                out.append(value)
                continue
            closed_at = None if kind == "text" else closed_at
    close_poem()
    return "".join(out).rstrip() + "\n"


# ---------------------------------------------------------------- the round trip

NORMAL_TOKEN = re.compile(r"¶| |\\(?:begin|end|indentpattern)\{[^}]*\}|\\[A-Za-z]+\*?|\\\\|\\-|[{}]|[^\s\\{}¶]+")


def normalize(latex):
    """What prints, as a list of tokens: comments and `{}` dropped, whitespace collapsed, each \\indentpattern written
    out to one digit per line of its poem, blank lines before a poem or after \\Caput dropped, and two
    \\emph{…} that meet across a line break or a verse number joined into one (they print the same)."""
    latex = strip_comments(latex).replace("{}", "")

    def expand(match):
        digits, poem = match.group(1), match.group(2)
        lines = poem.count("\\\\") + len(re.findall(r"\n[ \t]*\n", poem)) + 1     # stanza breaks end lines too
        return "\\indentpattern{" + ((digits * lines)[:lines] if digits else "") + "}" + poem

    latex = re.sub(r"\\indentpattern\{(\d*)\}(.*?\\end\{verse\})", expand, latex, flags=re.DOTALL)
    latex = re.sub(r"\n[ \t]*\n\s*(?=\\indentpattern)", "\n", latex)
    latex = re.sub(r"(\\Caput)\s+", r"\1\n", latex)
    latex = re.sub(r"\n[ \t]*\n\s*", "¶", latex)
    # Spaces are kept as tokens, except where TeX ignores them: after a command word or \\, and before \\, a
    # paragraph end or an environment.
    tokens = NORMAL_TOKEN.findall(re.sub(r"\s+", " ", latex).strip())
    command = lambda token: token == "¶" or re.match(r"\\[A-Za-z\\]", token) is not None
    tokens = [token for i, token in enumerate(tokens)
              if token != " " or not (i and command(tokens[i - 1]) or i + 1 < len(tokens) and
                                      (tokens[i + 1] in ("\\\\", "¶") or tokens[i + 1].startswith(("\\begin", "\\end", "\\indentpattern"))))]
    out = []
    for token in tokens:
        if token == "{" and out[-1:] == ["\\emph"]:
            back = len(out) - 2
            while back >= 0 and out[back] in ("\\\\", "\\Versus", " "):
                back -= 1
            if back >= 0 and out[back] == "}":
                del out[back]
                out.pop()
                continue
        out.append(token)
    while out and out[-1] == "¶":
        out.pop()
    return out


def compare(original, regenerated):
    """[(original tokens, regenerated tokens, context)] for every place where the two differ."""
    a, b = normalize(original), normalize(regenerated)
    diffs = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            diffs.append((a[i1:i2], b[j1:j2], " ".join(a[max(0, i1 - 6):i1])))
    return diffs, len(a)


def live_latex(source):
    """The book's LaTeX with its draft chapters (commented-out \\Caput onward) removed."""
    return re.split(r"^[ \t]*%[ \t]*\\Caput\b", source, maxsplit=1, flags=re.MULTILINE)[0]


def draft_latex(source):
    """The book's draft chapters, uncommented, under the \\Liber line (to compare with the draft USFM)."""
    head = source.split("\n", 1)[0]
    _, _, chapters = split_book(source)
    return head + "\n" + "".join(f"\n\\Caput{body}\n" for _, body, draft in chapters if draft)
