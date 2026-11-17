import unittest

from pipeline import notes


def unit(reading, rp):
    return notes.Unit("Mark.1.1", reading, rp, "")


class Classify(unittest.TestCase):
    def test_order_article_and_form_are_not_sense(self):
        self.assertFalse(notes.classify(unit("ἅπαξ ὑμᾶς", "ὑμᾶς ἅπαξ")))
        self.assertFalse(notes.classify(unit("ὁ", "–")))
        self.assertFalse(notes.classify(unit("ἐγήγερται", "ἐγήγερθη")))
        self.assertFalse(notes.classify(unit("καὶ", "δὲ")))

    def test_ranks(self):
        u = unit("αὐτοῦ", "+ ὑγιὴς ὡς ἡ ἄλλη")                   # Mark 3:5
        self.assertTrue(notes.classify(u))
        self.assertEqual((u.kind, u.rank), ("add", "clause"))
        u = unit("μετὰ τρεῖς ἡμέρας", "τῇ τρίτῃ ἡμέρᾳ")            # Mark 9:31
        self.assertTrue(notes.classify(u))
        self.assertEqual(u.rank, "number")
        u = unit("ὑμῶν", "ἡμῶν")                                  # a change of person
        self.assertTrue(notes.classify(u))
        self.assertEqual(u.rank, "person")

    @unittest.skipUnless((notes.SBLGNT / "Mark.txt").exists(), "SBLGNT not cached (sources/ is git-ignored)")
    def test_names_from_the_sblgnt(self):
        u = unit("Γερασηνῶν", "Γαδαρηνῶν")                       # Mark 5:1
        self.assertTrue(notes.classify(u))
        self.assertEqual(u.rank, "name")

    def test_jesus_supplied_is_only_a_word(self):
        u = unit("εἶδεν", "+ ὁ Ἰησοῦς")
        self.assertTrue(notes.classify(u))
        self.assertEqual(u.rank, "word")

    def test_tr_follows_rp(self):
        u = unit("αὐτοῦ", "+ ὑγιὴς ὡς ἡ ἄλλη")
        notes.classify(u)
        self.assertTrue(notes.tr_follows_rp(u, "καὶ ἀπεκατεστάθη ἡ χεὶρ αὐτοῦ ὑγιὴς ὡς ἡ ἄλλη"))
        self.assertFalse(notes.tr_follows_rp(u, "καὶ ἀπεκατεστάθη ἡ χεὶρ αὐτοῦ"))

    def test_person(self):
        found = notes.person_mismatches({"1John.4.4": "quī in nōbīs est"}, {"1John.4.4": "ὁ ἐν ὑμῖν"})
        self.assertEqual([vid for vid, _ in found], ["1John.4.4"])


if __name__ == "__main__":
    unittest.main()
