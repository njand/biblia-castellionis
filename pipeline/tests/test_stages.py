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
