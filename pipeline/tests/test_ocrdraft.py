"""A base text from 1738's own OCR (decision 68): the page's lines, the read lines joined into verses, and the
draft in Wikisource's conventions."""

import unittest

from pipeline import ocrdraft


def word(text, x0, y0, n, width=None):
    width = width or 22 * len(text)
    return (text, (x0, y0, x0 + width, y0 + 36), n)


class Classify(unittest.TestCase):
    def test_title_across_the_columns_splits_the_page(self):
        # 1738 leaf 156: Exodus ends in both columns above LEVITICVS., and Leviticus begins below it; the right
        # column's top is read before the left column's foot
        size = (1680, 2742)
        words = [word("Exodi", 160, 300, 1), word("verba", 400, 300, 1), word("sinistra", 600, 300, 1),
                 word("Exodi", 900, 300, 2), word("verba", 1100, 300, 2), word("dextra", 1300, 300, 2),
                 word("LEVITICVS.", 344, 1688, 3, width=1096),
                 word("Leuitici", 160, 2000, 4), word("verba", 400, 2000, 4), word("prima", 600, 2000, 4),
                 word("Leuitici", 900, 2000, 5), word("verba", 1100, 2000, 5), word("altera", 1300, 2000, 5)]
        lines = ocrdraft.classify(words, size)
        body = [l.text for l in lines if l.kind == "body"]
        self.assertEqual(body, ["Exodi verba sinistra", "Exodi verba dextra", "Leuitici verba prima",
                                "Leuitici verba altera"])
        self.assertEqual([l.text for l in lines if l.kind == "title"], ["LEVITICVS."])


class Verses(unittest.TestCase):
    LINES = [(155, 0, 1, "\\c 40"),
             (155, 0, 2, "#1 Tum Ioua Mosen ad hunc mo-"),
             (155, 0, 3, "dum adlocutus est : #2 Primo die"),
             (155, 0, 4, "%catchword mensis"),
             (156, 0, 5, "mensis primi tabernaculum erigito.")]

    def test_hyphens_joined_catchwords_left_out(self):
        verses, leaf = ocrdraft.verses_of(self.LINES)
        self.assertEqual(verses[(40, 1)], "Tum Ioua Mosen ad hunc modum adlocutus est :")
        self.assertEqual(verses[(40, 2)], "Primo die mensis primi tabernaculum erigito.")
        self.assertEqual(leaf[(40, 2)], 155)


class Modern(unittest.TestCase):
    FORMS = {"iouae": "jovae", "eiusque": "ejusque"}

    def test_forms_then_rules(self):
        self.assertEqual(ocrdraft.modern("Iouæ", self.FORMS), "Jovae")
        self.assertEqual(ocrdraft.modern("eiusque", self.FORMS), "ejusque")
        self.assertEqual(ocrdraft.modern("vt", {}), "ut")
        self.assertEqual(ocrdraft.modern("uersus", {}), "versus")
        self.assertEqual(ocrdraft.modern("obuelauit", {}), "obvelavit")
        self.assertEqual(ocrdraft.modern("conseruanto", {}), "conservanto")
        self.assertEqual(ocrdraft.modern("perpetuos", {}), "perpetuos")
        self.assertEqual(ocrdraft.modern("malumue", {}), "malumve")
        self.assertEqual(ocrdraft.modern("redimitorue", {}), "redimitorve")
        self.assertEqual(ocrdraft.modern("tenue", {}), "tenue")
        self.assertEqual(ocrdraft.modern("parueritis", {}), "parueritis")      # pāreō, Lev 26:15
        self.assertEqual(ocrdraft.modern("paruum", {}), "parvum")
        self.assertEqual(ocrdraft.modern("iuuatote", {}), "juvatote")          # Lev 25:35
        self.assertEqual(ocrdraft.modern("animaduertitor", {}), "animadvertitor")   # Lev 19:20
        self.assertEqual(ocrdraft.modern("coierit", {}), "coierit")            # Lev 20:12
        self.assertEqual(ocrdraft.modern("subiugiis", {}), "subjugiis")        # Lev 26:13
        self.assertEqual(ocrdraft.modern("iuissent", {}), "ivissent")          # Num 14:7, eō's perfect
        self.assertEqual(ocrdraft.modern("coiuistis", {}), "coivistis")        # Num 16:11
        self.assertEqual(ocrdraft.modern("iuuenis", {}), "juvenis")
        self.assertEqual(ocrdraft.modern("iure", {}), "jure")
        self.assertEqual(ocrdraft.modern("Iaser", {}), "Jaser")                # Num 32:1, Hebrew, not Greek ias-
        self.assertEqual(ocrdraft.modern("ouatu", {"ouatu": "ouatu"}), "ovatu")             # Num 10:5
        self.assertEqual(ocrdraft.modern("coierunt", {"coierunt": "coierunt"}), "coierunt") # Num 16:3
        self.assertEqual(ocrdraft.modern("Iacobeis", {"iacobeis": "Iacobeis"}), "Jacobeis")   # not Malachi's I
        self.assertEqual(ocrdraft.modern("eius", {}), "ejus")
        self.assertEqual(ocrdraft.modern("sæuies", {}), "saevies")

    def test_capitals_kept(self):
        self.assertEqual(ocrdraft.modern("TARDVS", {}), "TARDUS")
        self.assertEqual(ocrdraft.modern("IOVAE", self.FORMS), "JOVAE")

    def test_text_spacing_and_abbreviations(self):
        self.assertEqual(ocrdraft.modern_text("imposuit , sicut ei Ioua ( hoc ) xit,bases atq; & aræ", self.FORMS),
                         "imposuit, sicut ei Jova (hoc) xit, bases atque et arae")

    def test_drop_capital(self):
        self.assertEqual(ocrdraft.drop_capital("INterea populus"), "Interea populus")
        self.assertEqual(ocrdraft.drop_capital("EX hyacintho"), "Ex hyacintho")
        self.assertEqual(ocrdraft.drop_capital("Igitur"), "Igitur")


class ToUsfm(unittest.TestCase):
    def test_draft(self):
        lines = [(155, 0, 1, "\\c 40"), (155, 0, 2, "#1 TUm Ioua Mosen ad-"), (155, 0, 3, "locutus est. #2 Pri-"),
                 (155, 0, 4, "mo die ere-"), (155, 0, 5, "xit. #3 Arcam posuit.")]
        bsb = {"Exod.40.3": {"marks": "p"}}
        out = ocrdraft.to_usfm(lines, ["\\id EXO", "\\usfm 3.0"], {"iova": "jova"}, bsb, "Exod")
        self.assertEqual(out, "\\id EXO\n\\usfm 3.0\n\n\\c 40\n\\p\n\\v 1 Tum Jova Mosen adlocutus est.\n"
                              "\\v 2 Primo die erexit.\n\\p\n\\v 3 Arcam posuit.\n")


if __name__ == "__main__":
    unittest.main()


class Vote(unittest.TestCase):
    def voter(self):
        from pipeline import align
        known = {align.fold(w) for w in ("filius", "iouae", "chalebus", "calebus", "cum", "eum", "dixit")}
        return ocrdraft.Voter(set(), known)

    def test_own_word_first_then_others_in_order(self):
        v = self.voter()
        self.assertEqual(v.vote("dixit", ["xx", "cum"], ["1750", "Wikisource"]), "dixit")
        self.assertEqual(v.vote("qqq", [None, "Calebus", "Chalebus"], ["1750", "Wikisource", "1726"]), "Calebus")
        self.assertEqual(v.how["1738"], 1)
        self.assertEqual(v.how["Wikisource"], 1)

    def test_wikisource_word_in_the_print_letters(self):
        # the OCR's Iouæ with a misread letter: Wikisource's Jovae is taken in 1738's letters
        self.assertEqual(ocrdraft.in_print_letters("Iouæ", "Jovae"), "Iouæ")
        self.assertEqual(ocrdraft.in_print_letters("zzz", "Jovae"), "Iovae")

    def test_doubts_where_the_others_agree_against_the_vote(self):
        voted = ["Chalebus", "cum", "dixit", "filius"]
        others = [{0: "Calebus", 1: "eum", 2: "dixit", 3: "filius"},
                  {0: "Calebus", 1: "eum", 2: "dixit"}]
        self.assertEqual(ocrdraft.doubts(voted, others), [(0, "Calebus"), (1, "eum")])
        # one other alone, or the others split, is no doubt
        self.assertEqual(ocrdraft.doubts(["cum"], [{0: "eum"}]), [])
        self.assertEqual(ocrdraft.doubts(["cum"], [{0: "eum"}, {0: "tum"}]), [])
        # spelling alone (u/v, æ, long s) is no doubt
        self.assertEqual(ocrdraft.doubts(["Iouæ"], [{0: "Jovae"}, {0: "Iouae"}]), [])
