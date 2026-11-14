"""The print PDF: build/pdf/<stem>.tex, generated from the USFM master, compiled with LuaLaTeX (else Tectonic or
pdfLaTeX; `engine`) when a TeX install is on the PATH (scripts/install-texlive.sh installs one).

The preamble is pipeline/templates/preamble.tex (memoir, A5, each book in two balanced columns, lettrine drop
caps, running heads giving the verses on the page, \\Liber, \\Caput, \\Versus, \\FinisLibri), with
templates/title.tex inlined so the file stands alone. After the last book comes a page listing the Wikisource
pages and revisions used (`sources`). Each book's body is `latex.to_latex`, the same conversion the migration's round trip proved lossless. Added after the preamble: the commands for a
chapter summary (\\Argumentum) and a psalm title (\\Titulus), ȳ for inputenc, and the title and colophon pages. The
front matter (text/FRT.usfm, pipeline/frontmatter.py) follows the contents, in one column with roman page numbers."""

import pathlib
import re
import shutil
import subprocess

from pipeline import frontmatter, latex, paths, publish

MAIN = paths.ROOT / "pipeline" / "templates" / "preamble.tex"
TITLE = paths.ROOT / "pipeline" / "templates" / "title.tex"

ADDITIONS = r"""
% ---- added by pipeline/pdf.py (generated; never edit this file by hand)
\usepackage{iftex}
\ifPDFTeX\else
  % LuaLaTeX (the engine used: microtype then stretches or shrinks the letters up to 2% to even the spacing) or
  % XeTeX (Tectonic): Unicode fonts; TeX Gyre Pagella is the free Palatino
  \usepackage{fontspec}
  \setmainfont{texgyrepagella}[Extension=.otf, UprightFont=*-regular, BoldFont=*-bold,
    ItalicFont=*-italic, BoldItalicFont=*-bolditalic]
  % The footnotes' Greek in GFS Didot (the Greek Font Society's, OFL), whose Latin is Palatino's kin
  \newfontfamily\GraecaFont{GFSDidot}[Extension=.otf, Scale=MatchLowercase]
  \renewcommand{\Graece}[1]{{\GraecaFont #1}}
  \usepackage{newunicodechar}        % Pagella has no precomposed ȳ: y with a macron accent
  \newunicodechar{ȳ}{\=y}
  \newunicodechar{Ȳ}{\=Y}
\fi
\ifPDFTeX
  \DeclareUnicodeCharacter{0232}{\=Y}
  \DeclareUnicodeCharacter{0233}{\=y}
\fi
% Latin hyphenation (classical patterns, which know the macron vowels): without it the A5 measure gave 186
% overfull lines in the Gospels, with it 16, and with \emergencystretch 3. babel would rename the contents to
% "Index": the preamble's own heading is put back.
\usepackage[classiclatin]{babel}
\let\CastellioContentsname\contentsname
\AtBeginDocument{\let\contentsname\CastellioContentsname}
% Fewer hyphens (2026-11-12, measured on the whole Bible with Tectonic): babel's Latin allows a break two letters
% from either end of a word (de-inde, lo-quuntur), and 40% of the column lines ended in a hyphen, up to 13 in a row.
% At least three letters on each side, a moderate cost per hyphen and a high one for two in a row: 24%, at most 7,
% the spacing a little looser (set as the document begins, after babel has set its own minimums). Under LuaLaTeX,
% whose font expansion takes up the slack, the cost per hyphen is raised from 300 to 1000: 17% of the lines end in
% a hyphen, with about a quarter of Tectonic's loose lines (engine() below; HUMAN.md has the numbers).
\setlength{\emergencystretch}{3em}
\AtBeginDocument{\lefthyphenmin=3 \righthyphenmin=3 \hyphenpenalty=1000 \exhyphenpenalty=1000
  \doublehyphendemerits=300000 }
\urlstyle{same}                     % web addresses in the text face, not typewriter type
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
    """The title page's verso: the edition, its bases, editor and licence, the credit, and a link to the list of
    Wikisource pages and revisions (decision 54: no longer printed on a last page)."""
    info = publish.credits(selected)
    wikisource = info["wikisource"]

    def link(url):
        # Each address starts a line of its own and is printed without "https://", so it is never split (a full
        # \url broke after "https:", 2026-11-12); the link itself keeps the whole address.
        return rf"\\\href{{{url}}}{{\nolinkurl{{{publish.short_url(url)}}}}}"

    return rf"""\newpage
\vspace*{{\fill}}
{{\footnotesize\raggedright
{tex_escape(info["about"])}

\medskip
{tex_escape(info["bases"])}

\medskip
{tex_escape(info["edited"])}

\medskip
{tex_escape(info["licence"])}
{link(info["licence_url"])}

\medskip
{tex_escape(wikisource)} {tex_escape(info["wikisource_list_lead"])}
{link(info["wikisource_list_url"])}

\medskip
{tex_escape(info["source_lead"])}
{link(info["repository"])}
\par}}
"""


def page_name(url):
    """The page's name under the work: …/Biblia_Sacra_interprete_Sebastiano_Castellione/Evangelium_auctore_Marco
    → "…/Evangelium auctore Marco"."""
    return "…/" + url.rsplit("/", 1)[-1].replace("_", " ")


def document(selected, title, version):
    """The whole .tex file."""
    parts = [preamble(), ADDITIONS, frontmatter.TEX_COMMANDS,
             "\\begin{document}\n\\frontmatter\n\n\\begin{titlingpage}\n\\titleM\n",
             "{\\centering"                       # the selection's name, unless it is the title proper again
             + ("" if title == "Biblia Sacra" else f"\\Large {tex_escape(title)}\\par\\medskip")
             + (f"{{\\small {tex_escape(version)}}}\\par" if version else "") + "}\n",
             colophon(selected), "\\end{titlingpage}\n",       # the colophon on the title page's verso
             # the contents carry no running head on any of their pages
             "\n\\pagestyle{empty}\n\\tableofcontents*\n\\clearpage\n",
             # the front matter (text/FRT.usfm), in one column, roman page numbers, before the first book
             "\\pagestyle{praefatio}\n", frontmatter.to_tex(frontmatter.load(selected)),
             "\\clearpage\n\\pagestyle{plain}\n\n\\mainmatter\n"]
    testaments = {book.info.testament for book in selected}
    if len(testaments) == 1:     # the books grouped under their testament in the contents, as the front matter is
        name = "Vetus Fœdus" if testaments == {"vetus"} else "Novum Fœdus"
        parts.append(f"\\IndexTitulus{{{name}}}\n")
    current = None
    for book in selected:
        if len(testaments) > 1 and book.info.testament != current:
            current = book.info.testament
            parts.append("\n\\book{" + ("Vetus Fœdus" if current == "vetus" else "Novum Fœdus") + "}\n")
        usfm = latex.usfm_path(book.info).read_text(encoding="utf-8")
        parts.append(f"\n% ---- {book.info.osis}: generated from text/{book.info.usfm}.usfm\n")
        parts.append(latex.to_latex(usfm))
        parts.append("\\FinisLibri\n")                  # closes the book's columns (preamble.tex)
    parts.append("\n\\end{document}\n")
    return "".join(parts)


def tex_errors(log_path, output, limit=40):
    """The lines that say why TeX stopped, for the build's own output (CI keeps no log file): each `! …` error with
    the two lines after it, and Tectonic's `error:` lines; else the output's last lines."""
    text = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
    lines = (text or output).splitlines()
    picked = []
    for index, line in enumerate(lines):
        if line.startswith("!") or line.lower().startswith("error:"):
            picked += lines[index:index + 3]
    picked += [line for line in output.splitlines() if line.lower().startswith("error")]
    picked = picked or (text or output).splitlines()[-limit:]
    return "\n".join("    " + line for line in picked[:limit])


def engine(name):
    """The commands that compile <name>.tex, by the first engine on the PATH: LuaLaTeX (twice, for the contents
    and running heads), whose font expansion (microtype) evens the narrow columns' spacing; else Tectonic (XeTeX:
    protrusion only); else pdfLaTeX, with the preamble's own Palatino and TeX Greek fonts. Measured 2026-11-12 on
    the whole Bible (HUMAN.md): Tectonic, 23.9% of the column lines ending in a hyphen, 962 underfull, 4 overfull;
    LuaLaTeX with the same settings 21.4%, 157, 0; with the hyphen penalty raised to 1000, 17.3%, 215, 0."""
    lualatex, tectonic = shutil.which("lualatex"), shutil.which("tectonic")
    latexmk, pdflatex = shutil.which("latexmk"), shutil.which("pdflatex")
    flags = ["-interaction=nonstopmode", "-halt-on-error"]
    if lualatex:
        return [[lualatex, *flags, name]] * 2
    if tectonic:        # a single-file TeX engine (XeTeX); fetches the packages it needs on first use
        return [[tectonic, "--keep-logs", "--keep-intermediates", name]]
    if latexmk:
        return [[latexmk, "-pdf", *flags, name]]
    if pdflatex:
        return [[pdflatex, *flags, name]] * 2
    return []


def write(selected, folder, stem, title, version, compile_pdf=True):
    """Write <stem>.tex; compile it if TeX is installed. Returns [paths and messages]."""
    folder.mkdir(parents=True, exist_ok=True)
    tex = folder / f"{stem}.tex"
    tex.write_text(document(selected, title, version), encoding="utf-8", newline="\n")
    made = [tex]
    if not compile_pdf:
        return made
    commands = engine(tex.name)
    if not commands:
        return made + ["no TeX install found (lualatex, tectonic or pdflatex): the LaTeX is written, the PDF is not"]
    # Run again until the contents settle (at most four runs): the first run's contents are empty, so its page is
    # shorter, and the front matter's roman page numbers would stay one short (found 2026-11-13: "ii" for "iii").
    toc, previous, runs = folder / f"{stem}.toc", None, 0
    while commands:
        command = commands[0] if runs < len(commands) else commands[-1]
        result = subprocess.run(command, cwd=folder, capture_output=True, text=True, encoding="utf-8",
                                errors="replace")
        runs += 1
        if result.returncode:
            return made + [f"TeX failed (exit {result.returncode}); see {folder / (stem + '.log')}\n"
                           + tex_errors(folder / f"{stem}.log", result.stdout + result.stderr)]
        current = toc.read_text(encoding="utf-8", errors="replace") if toc.exists() else None
        if (runs >= len(commands) and current == previous) or runs >= 4 or len(commands) == 1 and runs == 1:
            break
        previous = current
    made.append(folder / f"{stem}.pdf")
    log = (folder / f"{stem}.log").read_text(encoding="utf-8", errors="replace")
    overfull = len(re.findall(r"^Overfull \\hbox", log, re.MULTILINE))
    underfull = len(re.findall(r"^Underfull \\hbox", log, re.MULTILINE))
    missing = len(re.findall(r"Missing character", log))
    made.append(f"{overfull} overfull lines, {underfull} underfull, {missing} missing characters (from {stem}.log; "
                f"{pathlib.Path(commands[0][0]).stem})")
    return made
