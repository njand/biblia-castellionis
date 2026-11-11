"""The print PDF: build/pdf/<stem>.tex, generated from the USFM master, compiled with latexmk (or pdflatex twice)
when a TeX install is on the PATH.

The preamble is pipeline/templates/preamble.tex (the former LaTeX/main.tex's), taken as it stands (memoir, A5,
lettrine drop caps, running heads, \\Liber, \\Caput, \\Versus), with templates/title.tex inlined so the file stands
alone. Each book's body is `latex.to_latex`, the same conversion the migration's round trip proved lossless. Added after the preamble: the commands for a
chapter summary (\\Argumentum) and a psalm title (\\Titulus), ȳ for inputenc, and the title and colophon pages."""

import re
import shutil
import subprocess

from pipeline import latex, paths, publish

MAIN = paths.ROOT / "pipeline" / "templates" / "preamble.tex"
TITLE = paths.ROOT / "pipeline" / "templates" / "title.tex"

ADDITIONS = r"""
% ---- added by pipeline/pdf.py (generated; never edit this file by hand)
\ifdefined\XeTeXrevision
  % XeTeX (Tectonic): Unicode fonts; TeX Gyre Pagella is the free Palatino
  \usepackage{fontspec}
  \setmainfont{texgyrepagella}[Extension=.otf, UprightFont=*-regular, BoldFont=*-bold,
    ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
  \usepackage{newunicodechar}        % Pagella has no precomposed ȳ: y with a macron accent
  \newunicodechar{ȳ}{\=y}
  \newunicodechar{Ȳ}{\=Y}
\else
  \DeclareUnicodeCharacter{0232}{\=Y}
  \DeclareUnicodeCharacter{0233}{\=y}
\fi
% Latin hyphenation (classical patterns, which know the macron vowels): without it the A5 measure gave 186
% overfull lines in the Gospels, with it 16, and with \emergencystretch 3. babel would rename the contents to
% "Index": the preamble's own heading is put back.
\usepackage[classiclatin]{babel}
\let\CastellioContentsname\contentsname
\AtBeginDocument{\let\contentsname\CastellioContentsname}
\setlength{\emergencystretch}{1.5em}
\newcommand{\Argumentum}[1]{\par\medskip{\small\itshape #1\par}\smallskip}
\newcommand{\Titulus}[1]{\par{\itshape #1\par}\smallskip}
\newcommand{\Subscriptio}[1]{\par\medskip{\small\itshape\noindent #1\par}}
"""


def preamble():
    """The preamble (up to any \\begin{document}), with \\input{title.tex} replaced by the file's text."""
    main = MAIN.read_text(encoding="utf-8")
    head = main.split("\\begin{document}", 1)[0]
    title = TITLE.read_text(encoding="utf-8")
    return head.replace("\\input{title.tex}", title.rstrip() + "\n")


def tex_escape(text):
    text = re.sub(r"([&%$#_{}])", r"\\\1", text)
    return latex.unicode_to_latex(text.replace("~", r"\textasciitilde{}").replace("^", r"\textasciicircum{}"))


def colophon(selected):
    info = publish.credits(selected)
    pages = "\n".join(f"\\item {tex_escape(short)}: \\url{{{url}}} (revision {revid}, fetched {fetched})"
                      for short, url, revid, _, fetched in info["pages"])
    return rf"""\newpage
\vspace*{{\fill}}
{{\footnotesize\raggedright
{tex_escape(info["about"])}

\medskip
{tex_escape(info["bases"])}

\medskip
{tex_escape(info["edited"])}

\medskip
{tex_escape(info["licence"])} \url{{{info["licence_url"]}}}

\medskip
{tex_escape(info["wikisource"])}
\begin{{itemize}}\setlength{{\itemsep}}{{0pt}}
{pages}
\end{{itemize}}

{tex_escape("Source files, data and corrections:")} \url{{{info["repository"]}}}
\par}}
"""


def document(selected, title, version):
    """The whole .tex file."""
    parts = [preamble(), ADDITIONS, "\\begin{document}\n\n\\begin{titlingpage}\n\\titleM\n",
             f"{{\\centering\\Large {tex_escape(title)}\\par"
             + (f"\\medskip{{\\small {tex_escape(version)}}}\\par" if version else "") + "}\n",
             colophon(selected), "\\end{titlingpage}\n",       # the colophon on the title page's verso
             "\n\\tableofcontents*\n\n\\mainmatter\n"]
    testaments = {book.info.testament for book in selected}
    current = None
    for book in selected:
        if len(testaments) > 1 and book.info.testament != current:
            current = book.info.testament
            parts.append("\n\\book{" + ("Vetus Fœdus" if current == "vetus" else "Novum Fœdus") + "}\n")
        usfm = latex.usfm_path(book.info).read_text(encoding="utf-8")
        parts.append(f"\n% ---- {book.info.osis}: generated from text/{book.info.usfm}.usfm\n")
        parts.append(latex.to_latex(usfm))
    parts.append("\n\\end{document}\n")
    return "".join(parts)


def write(selected, folder, stem, title, version, compile_pdf=True):
    """Write <stem>.tex; compile it if TeX is installed. Returns [paths and messages]."""
    folder.mkdir(parents=True, exist_ok=True)
    tex = folder / f"{stem}.tex"
    tex.write_text(document(selected, title, version), encoding="utf-8", newline="\n")
    made = [tex]
    if not compile_pdf:
        return made
    latexmk, pdflatex, tectonic = shutil.which("latexmk"), shutil.which("pdflatex"), shutil.which("tectonic")
    if latexmk:
        commands = [[latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error", tex.name]]
    elif pdflatex:
        commands = [[pdflatex, "-interaction=nonstopmode", "-halt-on-error", tex.name]] * 2
    elif tectonic:      # a single-file TeX engine (XeTeX); fetches the packages it needs on first use
        commands = [[tectonic, "--keep-logs", "--keep-intermediates", tex.name]]
    else:
        return made + ["no TeX install found (latexmk, pdflatex or tectonic): the LaTeX is written, the PDF is not"]
    for command in commands:
        result = subprocess.run(command, cwd=folder, capture_output=True, text=True, encoding="utf-8",
                                errors="replace")
        if result.returncode:
            return made + [f"TeX failed (exit {result.returncode}); see {folder / (stem + '.log')}"]
    made.append(folder / f"{stem}.pdf")
    log = (folder / f"{stem}.log").read_text(encoding="utf-8", errors="replace")
    overfull = len(re.findall(r"^Overfull \\hbox", log, re.MULTILINE))
    missing = len(re.findall(r"Missing character", log))
    made.append(f"{overfull} overfull lines, {missing} missing characters (from {stem}.log)")
    return made
