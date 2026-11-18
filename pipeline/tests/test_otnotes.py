import unittest

from pipeline import otnotes


class LatinNumbers(unittest.TestCase):
    def test_cardinals_ordinals_and_hundreds(self):
        self.assertEqual(otnotes.latin_numbers("Ita nōngentēsimum trīcēsimum ætātis annum agēns"), {9, 100, 30})
        self.assertEqual(otnotes.latin_numbers("vīxitque posteā annōs ducentōs suprā novem"), {2, 100, 9})
        self.assertEqual(otnotes.latin_numbers("Nōa quīngentēnārius genuit Sēmum"), {5, 100})
        self.assertEqual(otnotes.latin_numbers("annōs septemdecim nātus"), {7, 10})

    def test_one_and_first_left_out(self):
        self.assertEqual(otnotes.latin_numbers("Ūnō autem et sescentēsimō annō, prīmī mēnsis diē prīmō"), {6, 100})

    def test_second_only_after_a_number(self):
        self.assertEqual(otnotes.latin_numbers("Hic puer Deō secundō crēvit"), set())
        self.assertEqual(otnotes.latin_numbers("annō suæ vītæ nōngentēsimō sexāgēsimō secundō"), {9, 100, 60, 2})
        self.assertEqual(otnotes.latin_numbers("secundum quās"), set())

    def test_distributives_multiples_and_figures(self):
        self.assertEqual(otnotes.latin_numbers("caprās et ovēs ducēnās, caprōs et arietēs vīcēnōs"), {2, 100, 20})
        self.assertEqual(otnotes.latin_numbers("septuāgēcuplī septuplī"), {70, 7})
        self.assertEqual(otnotes.latin_numbers("mīlitēs 46500."), {40, 6, 1000, 5, 100})

    def test_tribes_are_not_three(self):
        self.assertEqual(otnotes.latin_numbers("Hæ sunt omnīnō Isrāēlītārum tribus"), set())

    def test_figures_count_as_the_hebrew_does(self):
        self.assertEqual(otnotes.figure_values(603550), {6, 100, 3, 1000, 5, 50})
        self.assertEqual(otnotes.figure_values(2200), {2, 1000, 100})
        self.assertEqual(otnotes.figure_values(17), {7, 10})

    def test_may_count(self):
        self.assertEqual(otnotes.latin_may_count("Alterum flūmen Gehōn vocātur"), ({2}, False))
        self.assertEqual(otnotes.latin_may_count("totidem alteræ")[1], True)


class HebrewNumbers(unittest.TestCase):
    def test_lemmas_and_the_dual(self):
        words = [("7651", "HAcbsc"), ("c/6242", "HC/Acbpa"), ("3117", "HNcmsa")]      # seven and twenty, day
        self.assertEqual(otnotes.hebrew_numbers(words), {7, 20})
        self.assertEqual(otnotes.hebrew_numbers([("3967", "HAcbda")]), {2, 100})           # two hundred
        self.assertEqual(otnotes.hebrew_numbers([("c/3967", "HC/Acbda")]), {2, 100})
        self.assertEqual(otnotes.hebrew_numbers([("3967", "HAcbpa")]), {100})
        self.assertEqual(otnotes.hebrew_numbers([("259", "HAcmsa")]), set())               # one


class Versions(unittest.TestCase):
    def test_rank(self):
        self.assertEqual(otnotes.version_rank("SP, LXX, Syriac, and Vulgate; Hebrew Then Cain spoke to his brother"),
                         "against MT")
        self.assertEqual(otnotes.version_rank("Hebrew; LXX the child lifted up his voice and wept"), "with MT")
        self.assertEqual(otnotes.version_rank("MT; Syriac and over all the beasts of the earth"), "with MT")
        self.assertEqual(otnotes.version_rank("See LXX; MT a fifth from the land"), "against MT")
        self.assertEqual(otnotes.version_rank("LXX pleased God; also in verse 24"), "other")


class Marks(unittest.TestCase):
    def test_mark_forms(self):
        for line in ("G. L. et Mariam eorum fororem,", "vetans G. L, quippe", "rus fe- ( G. /efl.)", "dixit; G.L. confidera",
                     "fuum fuis verbis, (Gr.lect.) rus", "terra extranea. G. ltem", "terra  extranca.  G\\  Item"):
            self.assertTrue(otnotes.MARK.search(line), line)
        for line in ("Hinc et iftud probauit D.G", "GENESIS", "Gerfomus"):
            self.assertFalse(otnotes.MARK.search(line), line)

    def test_ocr_words(self):
        self.assertEqual(otnotes.ocr_words("Ifaaco fīliō ſuō"), ["isaaco", "silio", "suo"])


if __name__ == "__main__":
    unittest.main()
