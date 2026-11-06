"""Aligning OCR witnesses: cleaning and word alignment, built from forms in the 1681, 1726 and 1758 OCRs."""

import unittest

from pipeline import align

BASE = [("Matt.4.18", "Ambulāns autem Jēsūs apud lacum Galilææ, cum vīdisset frātrēs duōs, Simōnem cognōmine Petrum,"),
        ("Matt.4.19", "Dīxit iīs: “Sequiminī mē, et faciam vōs hominum piscātōrēs.”"),
        ("Matt.4.20", "Illī vērō, relictīs prōtinus rētibus, eum secūtī sunt.")]


class Clean(unittest.TestCase):
    def test_long_s_hyphens_and_abbreviations(self):
        self.assertEqual(align.clean("conſi-\nderet Petrum & Andream 8c fratresq; cauſã"),
                         "consideret Petrum et Andream et fratresque causam")

    def test_fold(self):
        self.assertEqual(align.fold("Jēsūs"), "iesus")
        self.assertEqual(align.fold("quàm"), "quam")
        self.assertEqual(align.fold("Galilææ"), "galilaeae")
        self.assertEqual(align.fold("Jefus", fs=True), align.fold("Jesus", fs=True))


class Align(unittest.TestCase):
    OCR = ("CAP. IV. SECUNDUM MATTHÆUM. 23\nprædicare. 18 Ambulans autem Jefus apud lacum Galilææ, cum vidiffet "
           "fratres duos, Simonem cognomine Petrum, 19 Dixit iis: Sequimini me, & faciam vos hominum pifca-\ntores. "
           "20 Illi vero, relictis protinus retibus, eumsecuti sunt. 21 Inde progreſſus")

    def setUp(self):
        self.chapter = align.align_chapter(align.Witness(self.OCR), BASE, 4)

    def test_every_gold_word_found(self):
        s = align.score([self.chapter])
        self.assertEqual(s["found"], s["words"])
        self.assertEqual(s["fs"], s["words"])                 # Jefus, vidiffet, pifcatores agree f/s-blind
        self.assertEqual(s["exact"], s["words"] - 3)          # strictly, Jefus, vidiffet and pifcatores do not

    def test_verse_rows_and_numbers(self):
        self.assertEqual(self.chapter.verses["Matt.4.19"], "Dixit iis: Sequimini me, et faciam vos hominum pifcatores.")
        self.assertEqual(self.chapter.verses["Matt.4.20"], "Illi vero, relictis protinus retibus, eumsecuti sunt.")
        self.assertEqual(align.number_agreement([self.chapter]), (3, 3))

    def test_words_run_together(self):
        pairs = {base: witness for _, base, witness in self.chapter.matches}
        self.assertEqual((pairs["eum"], pairs["secūtī"]), ("eumsecuti", ""))

    def test_absent_chapter(self):
        chapter = align.align_chapter(align.Witness("Nihil hic de ea re scriptum est omnino."), BASE, 4)
        self.assertFalse(chapter.found)
        self.assertEqual(align.score([chapter])["found"], 0)


if __name__ == "__main__":
    unittest.main()
