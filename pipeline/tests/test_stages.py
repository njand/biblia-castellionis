"""Stages 2–5 on a draft: collation places, spelling proposals, quotation checks, verse numbers left in text."""

import unittest

from pipeline import collate, normalize, structure, versify


class Collate(unittest.TestCase):
    def test_a_word_more_less_and_different(self):
        rows = {"1573": "vos non esse me visuros deinceps", "1758": "vos non eſſe me viſuros deinceps",
                "ws": "vōs esse mē vīsūrōs deinceps"}
        places = collate.compare("Matt.23.39", "vōs esse mē vīsūrōs deinceps", rows)
        self.assertEqual(len(places), 1)
        place = places[0]
        self.assertEqual((place.start, place.end, place.text), (1, 1, ""))
        reading, who = place.against()
        self.assertEqual(sorted(who), ["1573", "1758"])
        self.assertEqual(place.support, ["ws"])
        self.assertEqual(collate.classify(place), "correct")

    def test_spelling_is_not_a_reading(self):
        place = collate.compare("Matt.16.8", "Id quod intellegēns Jēsūs", {"1573": "Id quod intelligens Iesus",
                                                                          "1758": "Id quod intelligens Jesus"})[0]
        self.assertEqual(collate.sort_kind(place), "spelling")
        place = collate.compare("Matt.14.12", "nūntiātum iērunt", {"1573": "nunciatum iuerunt",
                                                                  "1758": "nunciatum iverunt"})[0]
        self.assertEqual(collate.sort_kind(place), "form")


    def test_f_against_long_s(self):
        # Acts 3:2: Wikisource sani, 1573 fani; the f/s-blind fold read them alike. TXT/1 writes every ſ as f, so
        # it is no evidence either way.
        rows = {"1573": "ad fani portam", "ws": "ad sani portam", "1758": "ad fani portam"}
        places = collate.compare("Acts.3.2", "ad sani portam", rows, fs_distinct=("1573", "ws"))
        self.assertEqual([(p.start, p.end, p.text) for p in places], [(1, 2, "sani")])
        reading, who = places[0].against()
        self.assertEqual(list(who), ["1573"])
        self.assertEqual(places[0].support, ["ws"])
        self.assertEqual(collate.sort_kind(places[0]), "f/s")
        self.assertEqual(collate.compare("Acts.3.2", "ad sani portam", {"1573": "ad ſani portam"}), [])

    def test_words_added_or_lost_at_a_verse_edge(self):
        # Acts 9:1–2: Wikisource opens verse 2 with Et, which 1573 and 1758 lack; 1758's row is cut where its words
        # stop matching, so the verse-by-verse comparison sees nothing.
        a = ("Acts.9.1", "Saulus adiit pontificem")
        b = ("Acts.9.2", "Et petiit ab eo litteras")
        for witness in ("1573", "1758"):
            self.assertEqual(collate.compare("Acts.9.2", b[1], {witness: "petiit ab eo litteras"}), [])
        windows = {"1573": ("Saulus adiit pontificem", "", "petiit ab eo litteras"),
                   "1758": ("Saulus adiit pontificem", "", "petiit ab eo litteras"),
                   "ws": (a[1], "", b[1])}
        places = collate.edges(a, b, windows)
        self.assertEqual([(p.vid, p.start, p.end, p.text) for p in places], [("Acts.9.2", 0, 1, "Et")])
        self.assertEqual(sorted(places[0].against()[1]), ["1573", "1758"])
        self.assertEqual(places[0].support, ["ws"])
        self.assertEqual(collate.classify(places[0]), "correct")
        # A word the witnesses print between the two rows (the text lacks it), and one lost at a verse's end.
        windows = {"1573": ("Saulus adiit pontificem", "Tum", "Et petiit ab eo litteras"),
                   "1758": ("Saulus adiit pontificem", "Tum", "Et petiit ab eo litteras")}
        places = collate.edges(a, b, windows)
        self.assertEqual([(p.vid, p.start, p.end, p.text, p.against()[0]) for p in places],
                         [("Acts.9.2", 0, 0, "", "tum")])
        windows = {"1573": ("Saulus adiit", "", "Et petiit ab eo litteras")}
        self.assertEqual([(p.vid, p.start, p.end, p.text) for p in collate.edges(a, b, windows)],
                         [("Acts.9.1", 2, 3, "pontificem")])
        # A boundary moved (the word in the other verse's row) is not a difference.
        windows = {"1573": ("Saulus adiit pontificem Et", "", "petiit ab eo litteras")}
        self.assertEqual(collate.edges(a, b, windows), [])
        # At a chapter's end a lost word counts; its opening (a decorated initial, a heading) is not compared.
        self.assertEqual([(p.vid, p.text) for p in collate.edges(b, None, {"1573": ("Et petiit ab eo", "", None)})],
                         [("Acts.9.2", "litteras")])
        self.assertEqual(collate.edges(None, b, {"1573": (None, "", "petiit ab eo litteras")}), [])


class Normalize(unittest.TestCase):
    def test_carry_macrons_and_spaces(self):
        self.assertEqual(normalize.carry("maledīxerit", "male dixerit"), "male dīxerit")
        self.assertEqual(normalize.carry("quæsīvisset", "quaesisset"), "quæsīsset")
        self.assertEqual(normalize.carry("obdormīverant", "obdormierant"), "obdormierant")   # ī before a vowel
        self.assertEqual(normalize.carry("Hiericunte", "hierichunte"), "Hierichunte")

    def test_rules_on_a_text(self):
        usfm = "\\c 15\n\\p\n\\v 4 Quī patrī mātrīve maledīxerit, morte plēctātur.\n\\v 5 coepit et iērunt, mē, cum illīs.\n"
        found = {(p.vid, p.old, p.new, p.kind) for p in normalize.propose(usfm, "Matt", known={})}
        self.assertIn(("Matt.15.4", "maledīxerit", "male dīxerit", "phrase"), found)
        self.assertIn(("Matt.15.5", "coepit", "cœpit", "ligature"), found)
        self.assertFalse(any(p[3] == "jv" for p in found))                  # iērunt: a form of eō
        self.assertFalse(any("mēcum" in p[2] for p in found))               # mē, cum: a comma between

    def test_greek_i_and_latin_j(self):
        # Ēsāiās and Achāia keep the vowel i; maior (Rom 9:12) and plebeius take j.
        found = [c[2] for c in normalize.changes("Maior serviet minori, Esaias in Achaia, plebeio", {}, [], {})]
        self.assertEqual(found, ["Major", "plebejo"])


class Quotes(unittest.TestCase):
    def rows(self, *verses):
        return {vid: {"text": text, "marks": marks, "layout": text} for vid, text, marks in verses}

    def test_speech_over_paragraphs_and_blocks(self):
        rows = self.rows(("Matt.4.6", "sīc: “Sī Deī Fīlius es. Scrīptum est enim: “‘Angelīs suīs.’”", "p"),
                         ("Matt.4.7", "At Jēsūs: “Rūrsum,” inquit, “nē temptātō.", "p"),
                         ("Matt.4.8", "“Ego vērō dīcō.”", "p"))
        self.assertEqual([q for q in structure.quotes(rows) if not q[1].startswith("‘")], [])

    def test_unclosed_and_reported(self):
        rows = self.rows(("Matt.15.9", "“Frūstrā mē venerantur.", "p"),
                         ("Matt.15.10", "Deinde advocātā multitūdine: ‘eum esse īnsānum.’", "p"))
        flags = [q[1] for q in structure.quotes(rows)]
        self.assertIn("speech not closed before the next paragraph", flags)
        self.assertIn("‘…’ may be reported speech", flags)


class Versify(unittest.TestCase):
    def test_split_drops_a_number_left_in_the_text(self):
        usfm = "\\c 22\n\\p\n\\v 1 dictum est? 2‘Ego sum Deus.’\n\\v 2 Hōc audītō.\n"
        after, changes = versify.apply_edits(usfm, "Matt", [{"op": "split", "at": "Matt.22.1", "anchor": "2‘Ego"}])
        self.assertIn("\\v 1 dictum est?\n\\v 2 ‘Ego sum Deus.’\n\\v 3 Hōc audītō.", after)


if __name__ == "__main__":
    unittest.main()
