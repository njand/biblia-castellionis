"""Functions to convert LaTeX files to TXT and HTML (for the EPUB)."""

import os
import re


BOOK_COMMAND = r"\Liber"
CHAPTER_COMMAND = r"\Caput"
VERSE_COMMAND = r"\Versus"
INDENT_COMMAND = r"\indentpattern{"
BEGIN_COMMAND = r"\begin"
END_COMMAND = r"\end"
SKIP_COMMAND = r"\medskip"


def read_latex(filepath):
    with open(filepath, "r", encoding="utf-8") as reader:
        return reader.read()


def int2roman(num):
    """Convert an integer to a roman numeral string. Adapted from: https://www.geeksforgeeks.org/python-program-to-convert-integer-to-roman/"""
    c = ["", "C", "CC"]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
  
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    return hundreds + tens + ones


def preprocess_txt_line(line):
    """Preprocess a LaTeX line to prepare it for the txt file"""
    if line.isspace():
        return line

    line = line.lstrip()
    line = re.sub(r"\\\\\n", "\n", line)
    line = re.sub(r"\\\\", " ", line)
    line = re.sub(r"\\-", "", line)
    line = re.sub(r"``", "“", line)
    line = re.sub(r"''", "”", line)
    line = re.sub(r"`", "‘", line)
    line = re.sub(r"'", "’", line)
    line = re.sub(r"\\thinspace*", "", line)
    line = re.sub(r"\{\}", "", line)
    line = re.sub(r"\\emph{", "", line)
    line = re.sub(r"}", "", line)
    line = re.sub(r"%.*", "", line)
    return line


def preprocess_html_line(line):
    """Preprocess a LaTeX line to prepare it for the html file"""
    if line.isspace():
        return line

    line = line.lstrip()
    line = re.sub(r"\\\\\n", "\n", line)
    line = re.sub(r"\\\\", " ", line)
    line = re.sub(r"\\-", "", line)
    line = re.sub(r"``", "“", line)
    line = re.sub(r"''", "”", line)
    line = re.sub(r"`", "‘", line)
    line = re.sub(r"'", "’", line)
    line = re.sub(r"\\thinspace*", "", line)
    line = re.sub(r"\{\}", "", line)
    line = re.sub(r"%.*", "", line)
    return line


def to_txt(tex_doc):
    txt_lines = []
    chapter = 0
    verse = 0
    indentpattern = []
    
    for line in tex_doc.splitlines(keepends=True):
        line = preprocess_txt_line(line)
        if line.startswith(BOOK_COMMAND):
            chapter = 0
            verse = 0
            book = re.search(r"\[(.*)\]", line)
            output_line = f"LIBER: {book.group(1)}\n"
        elif line.startswith(CHAPTER_COMMAND):
            chapter += 1
            verse = 0
            output_line = "CAPUT " + int2roman(chapter) + line[len(CHAPTER_COMMAND):]
        elif line.startswith(VERSE_COMMAND):
            verse += 1
            output_line = f"{verse}." + line[len(VERSE_COMMAND):]
        elif line.startswith(SKIP_COMMAND):
            txt_lines.append("\n")
            continue
        elif line.startswith(INDENT_COMMAND):
            indentpattern = []
            for char in line[len(INDENT_COMMAND):]:
                try:
                    indentpattern.append(int(char))
                except ValueError:
                    break
            continue
        elif line.startswith(END_COMMAND):
            indentpattern = []
            continue
        elif line.startswith("%") or line.startswith(BEGIN_COMMAND):
            continue
        else:
            output_line = line

        if len(indentpattern):
            x = indentpattern.pop(0)
            output_line = "\t"*(x+1) + output_line
            indentpattern.append(x)

        txt_lines.append(output_line)
    return txt_lines


def insert_quote(matchobj):
    if matchobj.group(8) is None:
        ret = matchobj.group(1) + matchobj.group(2) + " quote"
        for i in range(3,10):
            if i in [5, 7]:
                continue
            if matchobj.group(i) is not None:
                ret += matchobj.group(i)
    else:
        ret = ""
        for i in range(1,5):
            if matchobj.group(i) is not None:
                ret += matchobj.group(i)
        ret += "<span class=\"quote\">"
        ret += matchobj.group(6)
        if matchobj.group(7) is not None:
            ret += "</span>"
        for i in range(8,10):
            if matchobj.group(i) is not None:
                ret += matchobj.group(i)
    return ret


def clean_txt(lines):
    """Remove extraneous linebreaks."""
    cleaned = []
    new_line_count = 0
    for i, line in enumerate(lines):
        if len(line.strip()) == 0:
            new_line_count += 1
            if new_line_count > 2:
                continue
        else:
            new_line_count = 0
        cleaned.append(line)
    return cleaned
    
    
def clean_html(html):
    """Remove extraneous tags and linebreaks. Correctly format italicized text."""
    cleaned = []
    italics = False
    for i, line in enumerate(html.splitlines(keepends=True)):
        if line.strip() == "</p>" and cleaned[-1].strip() == "<p>":
            cleaned = cleaned[:-1]
            continue
        if line.isspace() and cleaned[-1].isspace():
            continue

        if re.search(r"\\emph{", line):
            line, n = re.subn(r"(\s*<p class=\"poem-line)([^>]*)(\">)(<sup>.*</sup>)?(\\emph\{)?([^\}]+)?(\})?(.+)?(</p>)", insert_quote, line)
            
            if n == 0:
                line = re.sub(r"\\emph{", "<span class=\"quote\">", line)
                if re.search("}", line):
                    line = re.sub("}", "</span>", line)
                else:
                    italics = True
            elif not re.search("}", line):
                italics = True
                if not re.search("</p>\n$", line):
                    line = line.rstrip() + "</span>" + '\n'
        elif italics:
            line, n = re.subn(r"(\s*<p class=\"poem-line)([^>]*)(\">)(<sup>.*</sup>)?(\\emph\{)?([^\}]+)?(\})?(.+)?(</p>)", insert_quote, line)
            
            if n == 0:
                if line.strip() == "</div>":
                    italics = False
                else:
                    line = "<span class=\"quote\">" + line
                    line, n = re.subn("}", "</span>", line)
                
                    if n > 0:
                        italics = False
                    else:
                        line = line.rstrip() + "</span>" + '\n'

        cleaned.append(line)
    return cleaned


def to_html(tex_doc, filepath=None):
    html_lines = ["<?xml version='1.0' encoding='utf-8'?>\n",
                    "<html xmlns=\"http://www.w3.org/1999/xhtml\">\n",
                    "<head>\n",
                    "\t<title>Biblia Sacra</title>\n",
                    "\t<link type=\"text/css\" rel=\"stylesheet\" href=\"../../styles/0.css\"/>\n",
                    "</head>\n",
                    "\n",
                    "<body>\n"
                    ]
    chapter = 0
    verse = 0
    paragraph_flag = False
    poetry_flag = False
    indentpattern = []
    
    chapter_count = 0
    if filepath is not None:
        for line in tex_doc.splitlines():
            if line.startswith(CHAPTER_COMMAND):
                chapter_count += 1
                
    for raw_line in tex_doc.splitlines(keepends=True):
        line = preprocess_html_line(raw_line)
        if line.startswith(BOOK_COMMAND):
            chapter = 0
            verse = 0
            # Split two-line titles (e.g. "Ēvangelium Auctōre\\Lūcā") into a subtitle and title
            book = re.search(r"\[(.*)\]", raw_line).group(1).split("\\\\")

            output_line = "\t<br/>\n"
            if len(book) > 1:
                output_line += f"\t<h3>{' '.join(book[:-1]).upper()}</h3>\n"
            output_line += f"\t<h1>{book[-1].upper()}</h1>\n\t<br/>\n"
            if chapter_count > 0:
                output_line += "\t<div class=\"chapter-toc\">\n"
                for i in range(1, chapter_count+1):
                    output_line += f"\t\t<a href=\"{filepath}#caput{i}\">{i}</a>\n"
                output_line += "\t</div>\n"

        elif line.startswith(CHAPTER_COMMAND):
            chapter += 1
            verse = 0
            
            output_line = ""
            if chapter > 1:
                if paragraph_flag:
                    output_line += "\t</p>\n"
                output_line += "\t</div>\n\n"
            output_line += f"\t<div id=\"caput{chapter}\" class=\"chapter\">\n\t<span class=\"padded-dropcap\">{chapter}</span>\n"
        elif line.startswith(VERSE_COMMAND):
            verse += 1
            if verse == 1:
                output_line = "\t<p>\n\t\t"
                paragraph_flag = True
            else:
                output_line = f"\t\t<sup>{verse}</sup>"
            output_line += line[len(VERSE_COMMAND):].lstrip()
        elif line.isspace():
            if paragraph_flag:
                output_line = "\t</p>\n\n\t<p>\n"
            else:
                output_line = "\t<br/>\n"
        elif line.startswith(SKIP_COMMAND):
            output_line = "\n\t<br/>\n\n"
        elif line.startswith(INDENT_COMMAND):
            indentpattern = []
            for char in line[len(INDENT_COMMAND):]:
                try:
                    indentpattern.append(int(char))
                except ValueError:
                    break
            continue
        elif line.startswith(BEGIN_COMMAND):
            if poetry_flag:
                continue
            else:
                if paragraph_flag:
                    output_line = "\t</p>\n"
                else:
                    output_line = ""
                output_line += "\n\t<div class=\"poem\">\n"
                
                poetry_flag = True
                paragraph_flag = False
        elif line.startswith(END_COMMAND):
            if poetry_flag:
                indentpattern = []
                output_line = "\t</div>\n\t<p>\n"

                poetry_flag = False
                paragraph_flag = True
            else:
                continue
        elif line.startswith("%"):
            continue
        else:
            output_line = line
        
        if poetry_flag and len(indentpattern) and not line.startswith(BEGIN_COMMAND) and not line.startswith(SKIP_COMMAND):
            x = indentpattern.pop(0)
            indentpattern.append(x)
            
            prefix = "\t\t<p class=\"poem-line"
            if x > 0:
                prefix += f" poem-indent-{x}"
            prefix += "\">"
            suffix = "</p>\n"
            output_line = prefix + output_line.strip() + suffix
            
        html_lines.append(output_line)
    if paragraph_flag:
        html_lines.append("\t</p>\n")
    html_lines.append("\t</div>\n")
    html_lines.append("</body>\n")
    html_lines.append("</html>\n")
    
    html = "".join(html_lines)
    return clean_html(html)


def write_output(lines, filepath):
    with open(filepath, "w", encoding="utf-8") as writer:
        writer.writelines(lines)


def split_txt_chapters(lines):
    """Split txt lines into the header (before the first chapter) and a list of chapters."""
    header, chapters = [], []
    for line in lines:
        if line.startswith("CAPUT "):
            chapters.append([])
        (chapters[-1] if chapters else header).append(line)
    return header, chapters


def keep_extra_chapters(lines, filepath):
    """Append any chapters from the existing txt file beyond those generated from LaTeX,
    so that work not yet transferred to LaTeX is not overwritten."""
    if not os.path.exists(filepath):
        return lines
    with open(filepath, "r", encoding="utf-8") as reader:
        _, old_chapters = split_txt_chapters(reader.readlines())
    _, new_chapters = split_txt_chapters(lines)
    extra = old_chapters[len(new_chapters):]
    if not extra:
        return lines
    # Keep the same spacing between chapters as the existing file
    seam = old_chapters[len(new_chapters) - 1] if new_chapters else []
    blank_count = len(seam) - len("".join(seam).rstrip("\n").splitlines())
    lines = list(lines)
    while lines and not lines[-1].strip():
        lines.pop()
    lines.extend(["\n"] * blank_count)
    for chapter in extra:
        lines.extend(chapter)
    return lines


def strip_macrons(text):
    text = re.sub("ā", "a", text)
    text = re.sub("ē", "e", text)
    text = re.sub("ī", "i", text)
    text = re.sub("ō", "o", text)
    text = re.sub("ū", "u", text)
    text = re.sub("ȳ", "y", text)
    text = re.sub("Ā", "A", text)
    text = re.sub("Ē", "E", text)
    text = re.sub("Ī", "I", text)
    text = re.sub("Ō", "O", text)
    text = re.sub("Ū", "U", text)
    text = re.sub("Ȳ", "Y", text)
    return text


BOOKS = {
    "vetus": ["genesis"],
    "novum": ["matthaeus", "marcus", "lucas", "johannes"],
}


if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    for outer_book, books in BOOKS.items():
        testament = f"{outer_book[0].upper()}{outer_book[1:]} Fœdus"
        for book in books:
            tex_doc = read_latex(f"{root}/LaTeX/biblia/{outer_book} foedus/{book}.tex")
            macronized_lines = to_txt(tex_doc)
            macronized_lines = clean_txt(macronized_lines)
            plain_lines = [strip_macrons(line) for line in macronized_lines]

            macronized_path = f"{root}/TXT/4 - Macronized/{testament}/{book}.txt"
            write_output(keep_extra_chapters(macronized_lines, macronized_path), macronized_path)

            plain_path = f"{root}/TXT/3 - Edited/{testament}/{book}.txt"
            write_output(keep_extra_chapters(plain_lines, plain_path), plain_path)

            html_lines = to_html(tex_doc, f"{book}.html")
            write_output(html_lines, f"{root}/HTML/kx1umcn9_files/text/{outer_book}/{book}.html")
