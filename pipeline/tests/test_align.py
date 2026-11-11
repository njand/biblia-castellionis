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

    def test_marked_passage_kept_and_flagged(self):
        # 1758 Luke 11:7: the clause between L. and G. is in the OCR; a base without it must not drop it.
        base = [("Luke.11.7", "Nōn possum surgere et tibi dare."),
                ("Luke.11.8", "Mihi crēdite, etsī nōn surget ad eī dandum, quia sit ejus amīcus.")]
        ocr = ("7 Non possum sur-\ngere, et tibi dare L. si ille pulsare perseveraverit G. 8Mihi credite, etsi non "
               "surget ad ei dandum, quia sit ejus amicus.")
        chapter = align.align_chapter(align.Witness(ocr), base, 11)
        self.assertEqual(chapter.verses["Luke.11.7"], "Non possum surgere, et tibi dare si ille pulsare perseveraverit")
        self.assertEqual(chapter.marked["Luke.11.7"], ["si ille pulsare perseveraverit"])
        self.assertEqual(align.row_flags(chapter, "Luke.11.7", 6, 6), "L…G: si ille pulsare perseveraverit")

    def test_marks_read_as_other_letters(self):
        # 1758 Luke 10:1 prints "septuaginta I. duos, G. eosque": the marks are no words and leave the text.
        tokens = align.words("alios septuaginta I. duos, G. eosque binos")
        self.assertEqual(align.lg_marks(tokens), {2: 6})
        self.assertEqual(align.strip_marks([t for t, _ in tokens]), ("alios septuaginta duos, eosque binos", ["duos"]))
        self.assertEqual(align.lg_marks(align.words("CAP. I. Quodam tempore")), {})

    def test_anchors_take_words_up_to_the_next_number(self):
        ocr = "3 Ceperat enim Iohannem Herodes, et vinctum dederat in custodiam, nouum verbum 4 quod Herodi dixisset"
        base = [("Matt.14.3", "Cēperat enim Jōhannem Hērōdēs, et vīnctum dederat in cūstōdiam,"),
                ("Matt.14.4", "quod Hērōdī dīxisset Jōhannēs,")]
        plain = align.align_chapter(align.Witness(ocr), base, 14)
        anchored = align.align_chapter(align.Witness(ocr, anchors=True), base, 14)
        self.assertTrue(plain.verses["Matt.14.3"].endswith("custodiam,"))
        self.assertTrue(anchored.verses["Matt.14.3"].endswith("custodiam, nouum verbum"))

    def test_superscript_digit_is_no_verse_number(self):
        # An OCR's ² or ½ before a verse is a digit to str.isdigit but no number: it must not stop the alignment
        # (the Colossians collation stopped on one, 2026-11-11).
        ocr = self.OCR.replace("19 Dixit", "19 ² Dixit")
        chapter = align.align_chapter(align.Witness(ocr), BASE, 4)
        self.assertIn("Matt.4.19", chapter.verses)

    def test_absent_chapter(self):
        chapter = align.align_chapter(align.Witness("Nihil hic de ea re scriptum est omnino."), BASE, 4)
        self.assertFalse(chapter.found)
        self.assertEqual(align.score([chapter])["found"], 0)


if __name__ == "__main__":
    unittest.main()
