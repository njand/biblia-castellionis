"""Parser tests, built from the forms met in the real pages."""

import unittest

from pipeline import parallel, wikisource, wordpress


def texts(rows):
    return {vid: text for vid, text, _ in rows}


def flags(rows):
    return {vid: flag for vid, _, flag in rows if flag}


class Roman(unittest.TestCase):
    def test_numerals(self):
        self.assertEqual([wikisource.roman(n) for n in ["I", "IV", "IX", "XL", "XLIX", "CL", "12"]],
                         [1, 4, 9, 40, 49, 150, 12])

    def test_u_for_v(self):
        self.assertEqual(wikisource.roman("UI"), 6)       # "CAPUT UI." in the Song of Songs


class Wikisource(unittest.TestCase):
    def test_chapter_summary_and_verses(self):
        page = "{{titulus2\n|Scriptor=Sebastianus Castellio}}\n\n==Caput VI==\n\n''In patria propheta.''\n\n" \
               "1. Illinc deinde profectus, venit in suam patriam,\n2. Atque ubi advenit sabbatum,\n"
        self.assertEqual(texts(wikisource.parse(page, "Mark")), {
            "Mark.6.0": "In patria propheta.",
            "Mark.6.1": "Illinc deinde profectus, venit in suam patriam,",
            "Mark.6.2": "Atque ubi advenit sabbatum,"})

    def test_no_space_after_number_and_heading_with_period(self):
        rows = wikisource.parse("==CAPUT I.==\n1.Beatus homo,\n2.Sed Jovae lege delectatur.", "Ps")
        self.assertEqual(texts(rows), {"Ps.1.1": "Beatus homo,", "Ps.1.2": "Sed Jovae lege delectatur."})

    def test_paragraph_with_inline_verses(self):
        rows = wikisource.parse("==Caput IV==\n1. Respondit Moses. 2. Et Jova, “Quid habes?” 3. “Abjice eam.”", "Exod")
        self.assertEqual(texts(rows), {"Exod.4.1": "Respondit Moses.", "Exod.4.2": "Et Jova, “Quid habes?”",
                                       "Exod.4.3": "“Abjice eam.”"})
        self.assertEqual(flags(rows), {"Exod.4.2": "split", "Exod.4.3": "split"})

    def test_inline_number_must_be_next_verse(self):
        rows = wikisource.parse("==Caput I==\n1. Erant homines 3000. 2. Sed ille.", "Acts")
        self.assertEqual(texts(rows), {"Acts.1.1": "Erant homines 3000.", "Acts.1.2": "Sed ille."})

    def test_line_without_number_is_joined_and_flagged(self):
        rows = wikisource.parse("==Caput I==\n1. Ibi eo ad puteum sedente,\nvenerunt pastores.\n2. Tum ille.", "Exod")
        self.assertEqual(texts(rows)["Exod.1.1"], "Ibi eo ad puteum sedente, venerunt pastores.")
        self.assertEqual(flags(rows), {"Exod.1.1": "joined"})

    def test_gap(self):
        self.assertEqual(flags(wikisource.parse("==Caput I==\n1. A.\n3. C.", "Job")), {"Job.1.3": "gap"})

    def test_one_chapter_book_without_heading_or_periods(self):
        page = "A B D I A S\n1 Sic dicit Dóminus Iova ad Edom. 2 Quum ego te géntium mínimum effécerim,"
        self.assertEqual(texts(wikisource.parse(page, "Obad")), {
            "Obad.1.1": "Sic dicit Dóminus Iova ad Edom.", "Obad.1.2": "Quum ego te géntium mínimum effécerim,"})

    def test_book_argumentum_and_finis(self):
        page = "==Argumentum in Esteram==\nHaec historia.\n==Caput I==\n1. Assuerus regnavit.\n==Esterae Finis==\nnihil"
        self.assertEqual(texts(wikisource.parse(page, "Esth")), {"Esth.0.0": "Haec historia.",
                                                                 "Esth.1.1": "Assuerus regnavit."})

    def test_markup_is_stripped(self):
        self.assertEqual(wikisource.clean("''Sic'' [[Jova|Jovam]] dixit<ref>nota</ref>&nbsp;ita"), "Sic Jovam dixit ita")

    def test_needs_review(self):
        self.assertFalse(wikisource.needs_review("split"))
        self.assertTrue(wikisource.needs_review("joined,split"))


class WordPress(unittest.TestCase):
    PAGE = ('<div class="entry-content">'
            '<p class="wp-block-paragraph">35. Sed veniet tempus, atque eō tempore jejūnābunt.</p>'
            '<p class="wp-block-paragraph">36 Dīcēbat item iīs hanc collātiōnem:</p>'
            '<p class="wp-block-paragraph">37. Neque quisquam condit vīnum. 38 Sed vīnum novum.</p>'
            '<div class="sharedaddy">1. not a verse</div>')

    def test_verses_with_and_without_periods(self):
        rows = wordpress.parse_chapter(self.PAGE, "Luke", 5)
        self.assertEqual(texts(rows), {"Luke.5.35": "Sed veniet tempus, atque eō tempore jejūnābunt.",
                                       "Luke.5.36": "Dīcēbat item iīs hanc collātiōnem:",
                                       "Luke.5.37": "Neque quisquam condit vīnum.",
                                       "Luke.5.38": "Sed vīnum novum."})

    def test_chapter_links(self):
        index = f'<a href="{wordpress.SITE}/lucas-2/">2</a><a href="{wordpress.SITE}/lucas-1/">1</a>'
        self.assertEqual(wordpress.chapter_numbers(index, "lucas"), [1, 2])


class Usfm(unittest.TestCase):
    SOURCE = "\\id PSA\n\\c 1\n\\s1 The Two Paths\n\\q1\n\\v 1 Blessed is the man\n\\q2 who does not walk" \
             "\\f + \\fr 1:1 \\ft note\\f*,\n\\q1 \\v 2 But his \\w delight|strong=\"H2656\"\\w* is in the law.\n" \
             "\\c 2\n\\p \\v 1 Why do the nations rage?"

    def test_verses_marks_and_layout(self):
        code, rows = parallel.parse_usfm(self.SOURCE)
        self.assertEqual(code, "PSA")
        self.assertEqual(rows[0], (1, 1, "Blessed is the man who does not walk,", "s1:The Two Paths q1",
                                   "Blessed is the man \\q2 who does not walk,"))
        self.assertEqual(rows[1][:4], (1, 2, "But his delight is in the law.", "q1"))
        self.assertEqual(rows[2][:4], (2, 1, "Why do the nations rage?", "p"))


if __name__ == "__main__":
    unittest.main()
