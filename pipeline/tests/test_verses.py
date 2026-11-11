"""Stages 3–5 one verse at a time: layout lines, the lower-case rule, flag kinds, and items that review.apply takes."""

import unittest

from pipeline import macronize, review, verses


class Layout(unittest.TestCase):
    def verse(self, body, marks=()):
        return verses.Verse("Mark.7.28", body, marks=list(marks), body=body)

    def test_split_span(self):
        self.assertEqual(verses.split_span("\\p\n\\v 9 Probe, inquit iis:\n"), (["p"], 9, "Probe, inquit iis:"))
        self.assertEqual(verses.split_span("\\q1 \\v 8 \\qt Hic\\qt*\n\\q2 \\qt sed\\qt*")[:2], (["q1"], 8))

    def test_layout_line_keeps_the_words(self):
        v = self.verse("Et illa: Etsi ita est, Domine, (inquit ei respondens) tamen catelli comedunt.")
        verses.with_layout(v, 28, (None, "Et illa: “Etsi ita est, Domine,” inquit ei respondens, “tamen catelli comedunt.”", ""))
        self.assertTrue(v.quotes)
        self.assertEqual([f.kind for f in v.flags], ["punctuation"])
        self.assertIn("*respondens)* → *respondens,*", v.flags[0].note)
        with self.assertRaises(ValueError):
            verses.with_layout(self.verse("Et illa: Etsi ita est"), 28, (None, "Et illa: “Etsi sic est”", ""))

    def test_layout_dash_removes_the_marker(self):
        import tempfile, pathlib
        from unittest import mock
        with tempfile.TemporaryDirectory() as folder:
            path = pathlib.Path(folder) / "Acts.layout.tsv"
            path.write_text("id\tmarks\ttext\tnote\nActs.9.20\t-\tac statim\t\nActs.9.21\tp m\tx\t\nActs.9.22\t=\ty\t\n",
                            encoding="utf-8")
            with mock.patch.object(verses, "DECISIONS", pathlib.Path(folder)):
                found = verses.load_layout("Acts")
        self.assertEqual([found[v][0] for v in ("Acts.9.20", "Acts.9.21", "Acts.9.22")], [[], ["p", "m"], None])

    def test_capitals_are_flagged(self):
        v = self.verse("Deinde cernetur filius hominis veniens,")
        verses.with_layout(v, 26, (["m"], "Deinde cernetur Filius Hominis veniens,", ""))
        self.assertEqual([(f.word, f.kind) for f in v.flags], [("Filius", "capital"), ("Hominis", "capital")])
        self.assertEqual(v.marks, ["m"])


class Case(unittest.TestCase):
    LEXICON = {"utpote": macronize.Entry([macronize.Candidate("utpote", "MW")]),
               "petrus": macronize.Entry([macronize.Candidate("Petrus", "MW")])}

    def test_continues(self):
        self.assertTrue(verses.continues("multos aegrotos sanavit,"))
        self.assertTrue(verses.continues("… surge, arcessit te,”"))
        self.assertFalse(verses.continues("eum sequimini:"))                  # a colon: kept (61% in your text)
        self.assertTrue(verses.continues("eum sequimini:", colon=True))
        self.assertFalse(verses.continues("miracula?”"))

    def test_lower_start(self):
        self.assertEqual(verses.lower_start("Utpote cum non", self.LEXICON, {"utpote"}), "utpote cum non")
        pilatus = {"pilatus": macronize.Entry([macronize.Candidate("pīlātus", "W")])}         # 'armed with javelins'
        self.assertIsNone(verses.lower_start("Pilatus eum", pilatus, set()))               # your text: a name
        self.assertIsNone(verses.lower_start("Petrus dixit", self.LEXICON, set()))        # a name
        self.assertIsNone(verses.lower_start("“Utpote cum", self.LEXICON, set()))          # a quotation opens
        self.assertIsNone(verses.lower_start("Filius quidem", self.LEXICON, {"filius"}))   # may name Christ
        self.assertIsNone(verses.lower_start("Deum collaudantes", self.LEXICON, {"deum"}))  # God (2 Cor 9:13)


class Kinds(unittest.TestCase):
    def test_wordpress_and_settled_split_the_kinds(self):
        self.assertEqual(verses.kind_of("lexicon", "vēnit", "venit", None, None), "lexicon")
        self.assertEqual(verses.kind_of("lexicon", "Jācōbī", "Jacobi", frozenset({3}), None), "wordpress")
        self.assertEqual(verses.kind_of("chosen", "vēnit", "venit", frozenset({1}), frozenset({1})), "chosen+settled")
        self.assertEqual(verses.kind_of("chosen", "vēnit", "venit", frozenset({1}), frozenset()), "chosen")

    def test_ligatures_after_a_long_vowel_and_in_capitals(self):
        self.assertEqual(macronize.ligatures("Marīae"), "Marīæ")
        self.assertEqual(macronize.ligatures("JŪDAEŌRUM"), "JŪDÆŌRUM")
        self.assertEqual(macronize.ligatures("āer"), "āer")


class Items(unittest.TestCase):
    def test_an_item_applies_as_any_review_line(self):
        usfm = "\\c 6\n\\p\n\\v 1 Illinc deinde profectus, venit in suam patriam.\n\\v 2 Atque ubi advenit sabbatum,\n"
        v = verses.Verse("Mark.6.1", "\\p\n\\v 1 Illinc deinde profectus, venit in suam patriam.", marks=["p"],
                         body="Illinc deinde profectus, **vēnit** in suam patriam.")
        v.body = "Illinc deinde profectus, vēnit in suam patriam."
        v.new = "\\p \\v 1 " + v.body
        v.flags = [verses.Flag("vēnit", "chosen", "lexicon venit [MW] · vēnit [MW]")]
        text = "## Mark 6\n\n**Decision:** accept all except 2\n\n" + verses.item(v) + "\n"
        items = review.parse(text)
        self.assertEqual([i.number for i in items], [1])
        self.assertTrue(review.accepted(items[0]))
        outcomes, texts = review.apply(items, {"x": usfm}, "x")
        self.assertEqual([o.status for o in outcomes], ["ok"])
        self.assertIn("\\p\n\\v 1 Illinc deinde profectus, vēnit in suam patriam.\n\\v 2", texts["x"])


if __name__ == "__main__":
    unittest.main()
