"""The Latin front matter (text/FRT.usfm): Ad lēctōrem, the life, the translation, the edition's method, the signs
and the reading list, rendered for every format (PDF, EPUB, site, plain text).

The master uses the USFM introduction markers (\\is1 and \\is2 headings, \\ip paragraphs, \\ipr the signature, \\ili
the reading list, \\tr \\tc1 \\tc2 the table of signs) with \\it …\\it* for italics, and user markers (USFM's \\z…)
for what depends on the edition: \\zvt …\\zvt* is kept only when the selection holds Old Testament books, \\znt
only with the New, \\zboth with both, \\zntonly with the New alone, \\zapoc with the Apocrypha, \\zmac with macrons and
\\znomac without (the EPUB and text file sine macronibus). Any other marker stops the build, as in publish.parse."""

import html
import re
import unicodedata
from dataclasses import dataclass, field

from pipeline import latex, paths, publish

PATH = paths.ROOT / "text" / "FRT.usfm"
MARKERS = {"id", "rem", "is1", "is2", "ip", "ipr", "ili", "tr"}
CONDITION = re.compile(r"\\z(vt|nt|both|ntonly|apoc|mac|nomac) (.*?)\\z\1\*", re.S)
ITALIC = re.compile(r"\\it (.*?)\\it\*", re.S)


@dataclass
class Block:
    kind: str                                   # is1, is2, ip, ipr, ili, tr
    runs: list = field(default_factory=list)    # [(text, italic)]; for tr, [runs, runs] (the two cells)
    anchor: str = ""                            # is1: the section's id on the site and in the EPUB


def flags(selected, macrons=True):
    vetus = any(book.info.testament == "vetus" and not book.info.apocrypha for book in selected)
    novum = any(book.info.testament == "novum" for book in selected)
    return {"vt": vetus, "nt": novum, "both": vetus and novum, "ntonly": novum and not vetus,
            "apoc": any(book.info.apocrypha for book in selected), "mac": macrons, "nomac": not macrons}


def resolve(text, on):
    """Keep or drop each conditional span (innermost first, until none is left)."""
    while True:
        new = CONDITION.sub(lambda m: m.group(2) if on[m.group(1)] else "", text)
        if new == text:
            if re.search(r"\\z\w", new):
                raise publish.UsfmError("text/FRT.usfm: an edition marker is not closed or not known")
            return new
        text = new


def tidy(text):
    text = re.sub(r"\s+", " ", text)
    return re.sub(r" (?=[,.;:])", "", text).strip()


def runs(text, macrons):
    """'a \\it b\\it* c' → [('a ', False), ('b', True), (' c', False)]."""
    out, at = [], 0
    for match in ITALIC.finditer(text):
        out += [(text[at:match.start()], False), (match.group(1), True)]
        at = match.end()
    out.append((text[at:], False))
    if "\\" in "".join(piece for piece, _ in out):
        raise publish.UsfmError(f"text/FRT.usfm: unknown marker in {text[:60]!r}")
    filt = (lambda s: s) if macrons else publish.strip_macrons
    return [(filt(piece), italic) for piece, italic in out if piece]


def anchor(title):
    plain = publish.strip_macrons(title).lower().replace("æ", "ae").replace("œ", "oe")
    plain = unicodedata.normalize("NFD", plain)
    return re.sub(r"[^a-z]+", "-", "".join(c for c in plain if not unicodedata.combining(c))).strip("-")


def load(selected, macrons=True, path=PATH):
    """[Block] for this selection of books (and with or without macrons)."""
    text = resolve(path.read_text(encoding="utf-8"), flags(selected, macrons))
    blocks = []
    for line in text.split("\n"):
        if not line.strip():
            continue
        match = re.match(r"\\(\w+)\s*(.*)$", line)
        if not match or match.group(1) not in MARKERS:
            raise publish.UsfmError(f"text/FRT.usfm: not a front-matter line: {line[:60]!r}")
        kind, rest = match.groups()
        if kind in ("id", "rem"):
            continue
        if kind == "tr":
            cells = re.match(r"\\tc1 (.*?) \\tc2 (.*)$", rest)
            if not cells:
                raise publish.UsfmError(f"text/FRT.usfm: a \\tr needs \\tc1 and \\tc2: {rest[:60]!r}")
            blocks.append(Block("tr", [runs(tidy(cells.group(1)), macrons), runs(tidy(cells.group(2)), macrons)]))
            continue
        content = tidy(rest)
        if not content:
            continue
        block = Block(kind, runs(content, macrons))
        if kind == "is1":
            block.anchor = anchor(content)
        blocks.append(block)
    return blocks


def sections(blocks):
    """[(title, anchor)] of the main headings, for the contents."""
    return [("".join(t for t, _ in block.runs), block.anchor) for block in blocks if block.kind == "is1"]


# ---------------------------------------------------------------- HTML (site and EPUB)

def html_runs(pieces):
    return "".join(f"<i>{html.escape(t, quote=False)}</i>" if italic else html.escape(t, quote=False)
                   for t, italic in pieces)


def to_html(blocks, level=2):
    out, i = [], 0
    while i < len(blocks):
        block = blocks[i]
        if block.kind == "ili" or block.kind == "tr":
            group = []
            while i < len(blocks) and blocks[i].kind == block.kind:
                group.append(blocks[i])
                i += 1
            if block.kind == "ili":
                out.append('<ul class="libri">' + "".join(f"<li>{html_runs(b.runs)}</li>" for b in group) + "</ul>")
            else:
                out.append('<table class="notae">' + "".join(
                    f'<tr><td class="signum">{html_runs(b.runs[0])}</td><td>{html_runs(b.runs[1])}</td></tr>'
                    for b in group) + "</table>")
            continue
        text = html_runs(block.runs)
        if block.kind == "is1":
            out.append(f'<h{level} id="{block.anchor}">{text}</h{level}>')
        elif block.kind == "is2":
            out.append(f"<h{level + 1}>{text}</h{level + 1}>")
        elif block.kind == "ipr":
            out.append(f'<p class="signature">{text}</p>')
        else:
            first = i == 0 or blocks[i - 1].kind not in ("ip",)
            out.append(f'<p class="first">{text}</p>' if first else f"<p>{text}</p>")
        i += 1
    return "\n".join(out)


# ---------------------------------------------------------------- LaTeX (PDF)

TEX_COMMANDS = r"""
% The front matter (pipeline/frontmatter.py): one column, page numbers only, each section in the contents.
\makepagestyle{praefatio}
\makeevenhead{praefatio}{\thepage}{}{}
\makeoddhead{praefatio}{}{}{\thepage}
\newcommand{\Praefatio}[1]{\par\bigskip\phantomsection\addcontentsline{toc}{chapter}{#1}%
  {\centering\large\scshape #1\par}\nopagebreak\medskip\noindent\ignorespaces}
\newcommand{\PraefatioMinor}[1]{\par\medskip{\centering\itshape #1\par}\nopagebreak\smallskip}
\newcommand{\SubscriptioEditoris}[1]{\par\medskip{\raggedleft\itshape #1\par}}
\newcommand{\LiberLegendus}[1]{\par{\noindent\hangindent=1.5em\hangafter=1 #1\par}}
"""


def tex_text(text):
    text = re.sub(r"([&%$#_{}])", r"\\\1", text)
    text = latex.unicode_to_latex(text.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}"))
    return text.replace("ᵃ", r"\textsuperscript{a}")


def tex_runs(pieces):
    return "".join(f"\\textit{{{tex_text(t)}}}" if italic else tex_text(t) for t, italic in pieces)


def to_tex(blocks):
    out, i = [], 0
    while i < len(blocks):
        block = blocks[i]
        if block.kind == "tr":
            rows = []
            while i < len(blocks) and blocks[i].kind == "tr":
                rows.append(f"{tex_runs(blocks[i].runs[0])} & {tex_runs(blocks[i].runs[1])} \\\\")
                i += 1
            out.append("\\par\\noindent\\begin{tabular}{@{}p{2.5em}p{\\dimexpr\\textwidth-2.5em-2\\tabcolsep\\relax}@{}}\n"
                       + "\n".join(rows) + "\n\\end{tabular}\\par")
            continue
        text = tex_runs(block.runs)
        if block.kind == "is1":
            out.append(f"\\Praefatio{{{text}}}")
        elif block.kind == "is2":
            out.append(f"\\PraefatioMinor{{{text}}}")
        elif block.kind == "ipr":
            out.append(f"\\SubscriptioEditoris{{{text}}}")
        elif block.kind == "ili":
            out.append(f"\\LiberLegendus{{{text}}}")
        else:
            out.append(text + "\n")
        i += 1
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- plain text

def to_text(blocks):
    out = []
    for block in blocks:
        if block.kind == "tr":
            out.append("".join(t for t, _ in block.runs[0]) + "  " + "".join(t for t, _ in block.runs[1]))
            continue
        text = "".join(t for t, _ in block.runs)
        if block.kind == "is1":
            out += ["", text.upper(), ""]
        elif block.kind == "is2":
            out += ["", text, ""]
        elif block.kind == "ili":
            out.append("- " + text)
        else:
            out += [text, ""]
    return "\n".join(out).strip("\n") + "\n"
