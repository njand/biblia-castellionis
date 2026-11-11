"""The 1573 hOCR pages: finding where a column's text carries over (runs only where the pages are cached)."""

import unittest

from pipeline import mdz


@unittest.skipUnless((mdz.FOLDER / "0909.hocr").exists(), "1573 hOCR pages not cached (sources/ is git-ignored)")
class CarriedOver(unittest.TestCase):
    def words(self, text, line):
        return [w for w in mdz.page_words(909) if w.text.startswith(text) and w.line == line][0]

    def line_of(self, word):
        return " ".join(w.text for w in mdz.page_words(word.canvas) if w.line == word.line and w.column == word.column)

    def test_left_column_into_the_right(self):
        # 1 Tim 1:10 ends the upper left column at *ſanæ doctrinæ*; the right column goes on (its *contrarium eſt*
        # is lost by the OCR, so the first line it has is 1:11, under which the crop reaches up).
        after = mdz.carried_over(self.words("doctrin", 37))
        self.assertEqual((after.canvas, after.column), (909, 1))
        self.assertTrue(self.line_of(after).startswith("11 que"))

    def test_right_column_past_the_notes_into_the_next_zone(self):
        # 1:20 *Satanæ dedidi* ends the upper zone; chapter 2 goes on below Castellio's notes, not its centred summary.
        after = mdz.carried_over(self.words("Satan", 63))
        self.assertTrue(self.line_of(after).startswith("Xhortor"))

    def test_right_column_into_the_next_page(self):
        after = mdz.carried_over(self.words("frugal", 109))
        self.assertEqual((after.canvas, after.column), (910, 0))

    def test_a_line_inside_a_column(self):
        self.assertIsNone(mdz.carried_over(self.words("accept", 83)))


if __name__ == "__main__":
    unittest.main()
