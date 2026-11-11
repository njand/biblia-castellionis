"""Stage 7: the USFM model and every published format (website, EPUB, print LaTeX, TXT/TSV/JSON)."""

import json
import pathlib
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile

from pipeline import books, epub, gold, latex, pdf, publish, site

MATT = books.BY_OSIS["Matt"]
SAMPLE = """\\id MAT Biblia Sacra ex Sebastiani Castellionis interpretatione
\\usfm 3.0
\\ide UTF-8
\\h Matthæus
\\toc1 Ēvangelium Auctōre Matthæō
\\toc2 Matthæus
\\mt1 Ēvangelium Auctōre // Matthæō

\\c 1
\\cd Generis Chrīstī ēnumerātiō.
\\p
\\v 1 Ēnumerātiō generis Jēsū,
prōgnātī Dāvīde:
\\q1 \\v 2 Abrahāmus genuit Isaācum.
\\q2 Isaācus Jācōbum.
\\m
\\v 3 Jōsē\u00adphus vērō dīcentem: “\\qt Ex Ægyptō ēvocāvī.\\qt*”
\\v 4 “Numquam nē lēgistis? \\q1 \\qt “‘Per os īnfantium\\qt*
\\b
\\q2 \\qt laudem condis.’”\\qt*

\\c 2
\\nb
\\v 1 Hīc ȳ.
"""


def sample():
    return publish.parse(SAMPLE, MATT)


class Model(unittest.TestCase):
    def test_structure(self):
        book = sample()
        self.assertEqual((book.short, book.long, book.title), ("Matthæus", "Ēvangelium Auctōre Matthæō",
                                                               ["Ēvangelium Auctōre", "Matthæō"]))
        first, second = book.chapters
        self.assertEqual(first.summary, "Generis Chrīstī ēnumerātiō.")
        self.assertEqual([b.kind for b in first.blocks], ["p", "q1", "q2", "m", "q1", "b", "q2"])
        self.assertEqual([b.kind for b in second.blocks], ["nb"])

    def test_verses(self):
        rows = {vid: text for vid, _, _, text in publish.verses(sample())}
        self.assertEqual(rows["Matt.1.0"], "Generis Chrīstī ēnumerātiō.")
        self.assertEqual(rows["Matt.1.1"], "Ēnumerātiō generis Jēsū, prōgnātī Dāvīde:")
        self.assertEqual(rows["Matt.1.2"], "Abrahāmus genuit Isaācum. Isaācus Jācōbum.")
        self.assertEqual(rows["Matt.1.3"], "Jōsēphus vērō dīcentem: “Ex Ægyptō ēvocāvī.”")   # no soft hyphen
        self.assertEqual(rows["Matt.1.4"], "“Numquam nē lēgistis? “‘Per os īnfantium laudem condis.’”")

    def test_rejects_what_the_edition_does_not_use(self):
        for bad, message in ((SAMPLE.replace("\\m\n", "\\s1 Heading\n"), "s1"),
                             (SAMPLE.replace("\\v 3 ", "\\v 5 "), "verse 3 was expected"),
                             (SAMPLE.replace("ēvocāvī.\\qt*", "ēvocāvī."), "twice in a row"),
                             (SAMPLE.replace("\\c 2", "\\c 3"), "chapter 2 was expected")):
            with self.subTest(message=message), self.assertRaisesRegex(publish.UsfmError, message):
                publish.parse(bad, MATT)

    def test_subscription(self):
        """\\cls: a letter's subscription, set apart after the last verse and outside its text."""
        usfm = SAMPLE.rstrip("\n") + "\n\\cls Scrīpta est Corinthī.\n"
        book = publish.parse(usfm, MATT)
        self.assertEqual(book.chapters[1].closing, "Scrīpta est Corinthī.")
        rows = {vid: text for vid, _, _, text in publish.verses(book)}
        self.assertEqual(rows["Matt.2.1"], "Hīc ȳ.")
        self.assertEqual(gold.rows(usfm, "Matt")[-1][1], "Hīc ȳ.")
        self.assertTrue(publish.reading_text(book).rstrip().endswith("Hīc ȳ.\n\nScrīpta est Corinthī."))
        markup = site.chapter_html(book.chapters[1], str, "c")
        self.assertTrue(markup.endswith('<p class="cls">Scrīpta est Corinthī.</p>'))
        self.assertIn("\\Versus Hīc ȳ.\n\n\\Subscriptio{Scrīpta est Corinthī.}", latex.to_latex(usfm))
        with self.assertRaisesRegex(publish.UsfmError, "after the chapter's"):
            publish.parse(usfm + "\\p\n\\v 2 Plūs.\n", MATT)

    def test_strip_macrons(self):
        self.assertEqual(publish.strip_macrons("Ēvangelium Jēsū ȳ æ œ “‘’”"), "Evangelium Jesu y æ œ “‘’”")

    def test_settled_books_match_the_gold(self):
        """Every verse of every settled book reads exactly as data/gold has it (the gold set comes from the same
        USFM by another parser, parallel.parse_usfm)."""
        for book in publish.load():
            expected = {vid: row["text"] for vid, row in gold.load(book.info.osis).items()}
            if not expected:
                continue
            with self.subTest(book=book.info.osis):
                self.assertEqual({vid: text for vid, _, _, text in publish.verses(book)}, expected)

    def test_collection(self):
        gospels = [publish.Book(books.BY_OSIS[o], o, o, [o]) for o in ("Matt", "Mark", "Luke", "John")]
        self.assertEqual(publish.collection(gospels), ("Ēvangelia", "castellio-evangelia"))
        self.assertEqual(publish.collection(gospels[:2])[1], "castellio")


class Html(unittest.TestCase):
    def test_chapter_html_is_well_formed(self):
        chapter = sample().chapters[0]
        markup = site.chapter_html(chapter, lambda n: f"v{n}", "c1", verse_link=False)
        root = ET.fromstring(f"<div>{markup}</div>")              # raises if tags are unbalanced
        self.assertEqual(root.find(".//span[@class='c']").text, "1")
        self.assertEqual(root.find(".//p[@class='argumentum']").text, "Generis Chrīstī ēnumerātiō.")
        poems = root.findall("div[@class='poem']")
        self.assertEqual(len(poems), 2)
        self.assertEqual([d.get("class") for d in poems[1]], ["q1", "b", "q2"])
        # \qt reopened on the next line of the poem, after the stanza break
        self.assertEqual(poems[1][2].find("i").text, "laudem condis.’”")
        self.assertIsNone(root.find(".//*[@id='v1']").text)       # verse 1: an anchor only, under the drop cap
        self.assertEqual(root.find(".//sup[@id='v2']").text, "2")

    def test_filter_and_links(self):
        chapter = sample().chapters[0]
        markup = site.chapter_html(chapter, str, "c", publish.strip_macrons)
        self.assertIn('<a class="v" id="2" href="#2">2</a>Abrahamus', markup)
        self.assertNotIn("ā", markup)


def open_braces_at_blocks(tex):
    """[line numbers] where a paragraph break or a verse environment begins or ends inside an open {…}."""
    depth, out = 0, []
    for number, line in enumerate(tex.split("\n"), 1):
        if depth and (not line.strip() or line.startswith(("\\begin{verse}", "\\end{verse}"))):
            out.append(number)
        clean = line.replace("\\{", "").replace("\\}", "")
        depth += clean.count("{") - clean.count("}")
    return out


class Latex(unittest.TestCase):
    def test_summary_and_marker_inside_a_line(self):
        out = latex.to_latex(SAMPLE)
        self.assertIn("\\Argumentum{Generis Chrīstī ēnumerātiō.}\n\\Caput", out)
        self.assertIn("\\Versus ``Numquam nē lēgistis? \n\n\\indentpattern{01}", out)
        self.assertIn("Jōsē\\-phus", out)

    def test_every_settled_book_converts(self):
        for book in publish.load():
            with self.subTest(book=book.info.osis):
                out = latex.to_latex(latex.usfm_path(book.info).read_text(encoding="utf-8"))
                self.assertEqual(out.count("\\begin{verse}"), out.count("\\end{verse}"))
                self.assertEqual(out.count("\\Caput"), len(book.chapters))
                self.assertEqual(open_braces_at_blocks(out), [])

    def test_quotation_before_a_poem_closes_in_its_paragraph(self):
        """1 Cor 15:54-55: a \\qt closing a prose verse and one opening the poem after it are two \\emph{…}."""
        usfm = ("\\id 1CO\n\\c 1\n\\p\n\\v 1 dīcitur: \\qt “Absorpta mors.”\\qt*\n"
                "\\q1 \\v 2 \\qt “Ubi, ō mors?\\qt*\n\\q2 \\qt Ubi victōria?”\\qt*\n\\m\n\\v 3 Est autem.\n")
        out = latex.to_latex(usfm)
        self.assertIn("\\emph{``Absorpta mors.''}", out)
        self.assertEqual(open_braces_at_blocks(out), [])

    def test_document_reuses_the_preamble(self):
        mark = publish.load(["Mark"])
        document = pdf.document(mark, "Mārcus", "v0")
        self.assertIn("\\documentclass[9pt,a5paper,twoside,openany]{memoir}", document)
        self.assertIn("\\newcommand*\\titleM", document)                 # title.tex inlined
        self.assertNotIn("\\input{", document)
        self.assertIn("revision 165335", document)                       # the Wikisource revision credited
        self.assertEqual(document.count("\\begin{document}"), 1)
        self.assertEqual(pdf.tex_escape("50% & _x_"), "50\\% \\& \\_x\\_")


class Build(unittest.TestCase):
    def test_build_mark(self):
        with tempfile.TemporaryDirectory() as folder:
            out = pathlib.Path(folder)
            made = publish.build(["Mark"], out, references=(), version="test", compile_pdf=False)
            self.assertEqual(set(made), {"site", "epub", "pdf", "txt"})
            mark = publish.load(["Mark"])[0]
            verses = publish.verses(mark)
            # TXT/TSV/JSON
            stem = "castellio-marcus"
            self.assertIn("Wikisource", (out / "txt" / f"{stem}.txt").read_text(encoding="utf-8"))
            self.assertNotIn("ā", (out / "txt" / f"{stem}-sine-macronibus.txt").read_text(encoding="utf-8"))
            self.assertEqual(len((out / "txt" / f"{stem}.tsv").read_text(encoding="utf-8").splitlines()),
                             len(verses) + 1)
            data = json.loads((out / "txt" / f"{stem}.json").read_text(encoding="utf-8"))
            self.assertEqual(len(data["books"][0]["verses"]), len(verses))
            # EPUB: mimetype first and stored; every XHTML file well-formed
            for name in (f"{stem}.epub", f"{stem}-sine-macronibus.epub"):
                with zipfile.ZipFile(out / "epub" / name) as z:
                    first = z.infolist()[0]
                    self.assertEqual((first.filename, first.compress_type), ("mimetype", zipfile.ZIP_STORED))
                    for item in z.namelist():
                        if item.endswith((".xhtml", ".opf", ".ncx", ".xml")):
                            ET.fromstring(z.read(item))
                    if "sine" in name:
                        self.assertNotIn("ā", z.read("EPUB/book1.xhtml").decode("utf-8"))
            # LaTeX, not compiled
            self.assertTrue((out / "pdf" / f"{stem}.tex").exists())
            # the site: a page per chapter, a verse anchor per verse
            pages = sorted((out / "site" / "marcus").glob("[0-9]*.html"))
            self.assertEqual(len(pages), len(mark.chapters))
            sixteen = (out / "site" / "marcus" / "16.html").read_text(encoding="utf-8")
            self.assertIn('id="20" href="#20"', sixteen)
            self.assertIn('rel="prev" href="15.html"', sixteen)
            self.assertIn("oldid=", (out / "site" / "colophon.html").read_text(encoding="utf-8"))
            # the downloads built with the site are copied and listed (no PDF: the LaTeX was not compiled)
            self.assertTrue((out / "site" / "downloads" / f"{stem}.epub").exists())
            home = (out / "site" / "index.html").read_text(encoding="utf-8")
            self.assertIn(f'href="downloads/{stem}-sine-macronibus.epub"', home)
            self.assertNotIn("<b>PDF</b>", home)
            self.assertIn("index.html#downloads", sixteen)


if __name__ == "__main__":
    unittest.main()
