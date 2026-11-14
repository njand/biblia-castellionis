"""The front matter (text/FRT.usfm, pipeline/frontmatter.py): edition conditions, macrons, markers, rendering."""

import pathlib
import tempfile
import unittest
from types import SimpleNamespace

from pipeline import frontmatter, publish


def book(testament, apocrypha=False):
    return SimpleNamespace(info=SimpleNamespace(testament=testament, apocrypha=apocrypha))


VETUS, NOVUM, APOC = book("vetus"), book("novum"), book("vetus", apocrypha=True)


def text(selected, macrons=True):
    return frontmatter.to_text(frontmatter.load(selected, macrons))


class Conditions(unittest.TestCase):
    def test_new_testament_alone(self):
        out = text([NOVUM])
        self.assertIn("Novī Fœderis textum dedit ēditiō Basiliēnsis", out)
        self.assertNotIn("Lipsiēnsis", out)
        self.assertNotIn("cujus ēditiōnem Veteris Fœderis", out)
        self.assertIn("ex Vulgātā addita", out)
        self.assertIn("ā textū Græcō, ut", out)
        self.assertIn("⟦ ⟧", out)

    def test_old_testament_alone(self):
        out = text([VETUS])
        self.assertIn("Veteris Fœderis textum dedit ēditiō Lipsiēnsis", out)
        self.assertNotIn("Basiliēnsis annī 1573", out)
        self.assertNotIn("⟦ ⟧", out)
        self.assertIn("ā textū Hebræō, ut", out)
        self.assertNotIn("Nōa", out)

    def test_both_and_the_apocrypha(self):
        out = text([VETUS, NOVUM])
        self.assertIn("In utrōque Fœdere vocābula ecclēsiastica", out)
        self.assertIn("Novī Fœderis textum dedit Basiliēnsis", out)       # ēditiō only once, with the Old
        self.assertIn("Hebræō aut Græcō", out)
        self.assertNotIn("apocryphōs", out)                               # no Apocrypha built yet
        self.assertIn("apocryphōs", text([VETUS, APOC, NOVUM]))

    def test_without_macrons(self):
        out = text([VETUS, NOVUM], macrons=False)
        self.assertEqual(out, publish.strip_macrons(out))
        self.assertNotIn("vocales longae", out.replace("æ", "ae"))
        self.assertIn("Accedit quod hic orthographia ad hodiernam normam accommodata est, id quod", out)
        self.assertIn("Orthographiam ad lexicon Felicis Gaffiot accommodavi. Versiculi", out)


class Markers(unittest.TestCase):
    def load(self, usfm):
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "FRT.usfm"
            path.write_text(usfm, encoding="utf-8")
            return frontmatter.load([NOVUM], path=path)

    def test_unknown_marker_stops(self):
        with self.assertRaises(publish.UsfmError):
            self.load("\\id FRT\n\\p a paragraph marker of the books, not of the front matter\n")
        with self.assertRaises(publish.UsfmError):
            self.load("\\id FRT\n\\ip an \\bd unknown\\bd* character style\n")

    def test_unclosed_condition_stops(self):
        with self.assertRaises(publish.UsfmError):
            self.load("\\id FRT\n\\ip \\znt never closed\n")

    def test_italics_and_rendering(self):
        blocks = self.load("\\id FRT\n\\is1 Notæ\n\\ip a \\it b\\it* c\n\\tr \\tc1 ᵃ \\tc2 d\n")
        self.assertEqual(blocks[1].runs, [("a ", False), ("b", True), (" c", False)])
        self.assertEqual(frontmatter.sections(blocks), [("Notæ", "notae")])
        tex = frontmatter.to_tex(blocks)
        self.assertIn("\\Praefatio{Notæ}", tex)
        self.assertIn("a \\textit{b} c", tex)
        self.assertIn("\\textsuperscript{a}", tex)
        self.assertIn('<h2 id="notae">Notæ</h2>', frontmatter.to_html(blocks))


class Layout(unittest.TestCase):
    def test_sections_open_pages_but_the_reading_list(self):
        blocks = frontmatter.load([NOVUM])
        tex = frontmatter.to_tex(blocks)
        self.assertTrue(tex.startswith("\\IndexTitulus{Præfātiō}"))
        self.assertIn("\\Praefatio{Notæ}", tex)
        self.assertIn("\\PraefatioSequens{Librī legendī}", tex)
        self.assertEqual(tex.count("\\Praefatio{"), 5)
        page = frontmatter.to_html(blocks)
        self.assertIn('<h2 id="ad-lectorem">', page)                 # the first: no rule above it
        self.assertIn('<h2 id="notae" class="nova">', page)
        self.assertIn('<h2 id="libri-legendi">', page)
        self.assertIn('href="praefatio.html#notae"', frontmatter.contents_html(blocks, "praefatio.html"))


class Master(unittest.TestCase):
    def test_master_loads_for_every_edition(self):
        for selected in ([VETUS], [NOVUM], [VETUS, NOVUM]):
            for macrons in (True, False):
                blocks = frontmatter.load(selected, macrons)
                self.assertEqual([title for title, _ in frontmatter.sections(blocks)][0],
                                 "Ad lēctōrem" if macrons else "Ad lectorem")
                self.assertTrue(any(b.kind == "ipr" for b in blocks))


if __name__ == "__main__":
    unittest.main()
