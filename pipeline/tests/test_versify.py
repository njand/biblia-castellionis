"""Renumbering to the KJV: only markers move, built from the Genesis 6–7 and 14 cases."""

import unittest

from pipeline import gold, latex, versify

BOOK = """\\id GEN
\\c 1
\\p
\\v 1 Tū vērō cibāria comportātō.

\\c 2
\\p
\\v 1 Hæc omnia cum fēcisset Nōa, Jōva eum allocūtus est.
\\v 2 Ex omnibus septēna assūmitō.
\\v 3 quæ vallis bitūminis abundābat.
\\v 4 Ibi pulsīs rēgulīs, reliquī fūgērunt.
\\v 5 Obālem, Sabam, Ophīren, et Jobābum.
"""


def edit(op, at, anchor=""):
    return {"op": op, "at": at, "anchor": anchor, "status": "proposed", "note": ""}


class Apply(unittest.TestCase):
    def setUp(self):
        self.after, self.changes = versify.apply_edits(BOOK, "Gen", [
            edit("chapter", "Gen.2.1", "Jōva eum"), edit("merge", "Gen.2.4"), edit("split", "Gen.2.5", "Ophīren")])

    def test_markers_move_words_stay(self):
        self.assertEqual(versify.words(BOOK), versify.words(self.after))
        self.assertIn("\\v 2 Hæc omnia cum fēcisset Nōa,\n\n\\c 2\n\\nb\n\\v 1 Jōva eum allocūtus est.", self.after)
        self.assertIn("\\v 3 quæ vallis bitūminis abundābat.\nIbi pulsīs rēgulīs", self.after)
        self.assertIn("\\v 4 Obālem, Sabam,\n\\v 5 Ophīren, et Jobābum.", self.after)
        self.assertEqual(versify.verse_counts(self.after, "Gen"), {1: 2, 2: 5})

    def test_changes_listed(self):
        self.assertEqual(self.changes, [
            ("Gen.2.1", "Gen.1.2", "renumbered"), ("Gen.2.1 (part)", "Gen.2.1", "chapter"),
            ("Gen.2.4", "Gen.2.3", "merged"), ("Gen.2.5", "Gen.2.4", "renumbered"),
            ("Gen.2.5 (part)", "Gen.2.5", "split")])

    def test_full_stop_keeps_a_paragraph(self):
        after, _ = versify.apply_edits("\\c 1\n\\p\n\\v 1 Fīnis.\n\n\\c 2\n\\p\n\\v 1 Jōva discessit. Angelī vēnērunt.\n",
                                       "Gen", [edit("chapter", "Gen.2.1", "Angelī")])
        self.assertIn("\\v 2 Jōva discessit.\n\n\\c 2\n\\p\n\\v 1 Angelī vēnērunt.", after)

    def test_anchor_must_be_found_once(self):
        with self.assertRaisesRegex(ValueError, "not found exactly once"):
            versify.apply_edits(BOOK, "Gen", [edit("split", "Gen.2.2", "nusquam")])

    def test_renumbered_book_still_converts(self):
        self.assertIn("Jōva eum allocūtus est.", latex.to_latex(self.after))
        rows = {vid: text for vid, text, *_ in gold.rows(self.after, "Gen")}
        self.assertEqual(rows["Gen.1.2"], "Hæc omnia cum fēcisset Nōa,")
        self.assertEqual(rows["Gen.2.3"], "quæ vallis bitūminis abundābat. Ibi pulsīs rēgulīs, reliquī fūgērunt.")


if __name__ == "__main__":
    unittest.main()


class Opens(unittest.TestCase):
    """Castellio's Exod 5:25 is the KJV's 6:1: the chapter break moves back before it."""
    USFM = "\\id EXO\n\\c 5\n\\p\n\\v 1 Postea adeunt.\n\\p\n\\v 2 Cui Jova, inquit.\n\n\\c 6\n\\p\n\\v 1 Ego sum.\n"

    def test_break_moves_back(self):
        after, changes = versify.apply_edits(self.USFM, "Exod", [edit("opens", "Exod.5.2")])
        self.assertEqual(versify.words(self.USFM), versify.words(after))
        self.assertIn("\\v 1 Postea adeunt.\n\n\\c 6\n\\p\n\\v 1 Cui Jova, inquit.", after)
        self.assertEqual(versify.verse_counts(after, "Exod"), {5: 1, 6: 2})
        self.assertIn(("Exod.5.2", "Exod.6.1", "renumbered"), changes)


class OpensAtAnchor(unittest.TestCase):
    """Castellio's 1 Cor 10:33 ends with the KJV's 11:1 (*Imitatores mei estote …*): the break moves back into it."""
    USFM = ("\\id 1CO\n\\c 10\n\\p\n\\v 1 Prīmus.\n\\v 2 Omnibus placeō. Imitātōrēs meī estōte.\n\n"
            "\\c 11\n\\p\n\\v 1 Laudō vōs.\n\\v 2 Volō.\n")

    def test_words_open_the_next_chapter(self):
        after, changes = versify.apply_edits(self.USFM, "1Cor", [edit("opens", "1Cor.10.2", "Imitātōrēs")])
        self.assertEqual(versify.words(self.USFM), versify.words(after))
        self.assertIn("\\v 2 Omnibus placeō.\n\n\\c 11\n\\p\n\\v 1 Imitātōrēs meī estōte.\n\\p\n\\v 2 Laudō vōs.", after)
        self.assertEqual(versify.verse_counts(after, "1Cor"), {10: 2, 11: 3})
        self.assertIn(("1Cor.10.2 (part)", "1Cor.11.1", "chapter"), changes)
        self.assertIn(("1Cor.11.1", "1Cor.11.2", "renumbered"), changes)
