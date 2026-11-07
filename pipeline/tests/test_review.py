"""Applying review files: parsing Apply and Decision lines, verse spans in the USFM, composing replacements."""

import pathlib
import tempfile
import unittest

from pipeline import review

USFM = """\\id MAT
\\c 14
\\p
\\v 1 Per id tempus audiēns Hērōdēs,
\\v 2 dīxit suīs, eum esse Jōhannem.
\\p
\\v 3 Cēperat enim Jōhannem Hērōdēs, et vīnctum
dederat in cūstōdiam.
\\q1 \\v 4 quod Hērōdī dīxisset Jōhannēs,
\\q2 eī nōn licēre.
\\c 15
\\p
\\v 1 Tum accēdunt ad Jēsūm, et dīxit Hērōdēs.
"""

REVIEW = """# Test

## A. Group accepted (2)

**Decision:** accept (Nathan, 2026-11-07)

1. **Apply:** `Matt.14.1` la: `audiēns` → `audiēns autem`
2. **Apply:** `Matt.14.3` la: `vīnctum dederat` → `vīnctum trādiderat` (across a line break)

## B. Accept some (3)

**Decision:** accept 1, 3

1. **Apply:** `Matt.14.2` la: `suīs` → `suīs discipulīs`
2. **Apply:** `Matt.14.2` la: `esse` → `fore`
3. **Apply:** `Matt.15.1` la: `Hērōdēs` → `Hērōdēs rēx`

## C. Item decisions

**Decision:** accept all except 2

1. Two lines, one item.
   **Apply:** `Matt.14.4` la: `\\q1 \\v 4 quod` → `\\p \\v 4 quod`
   **Apply:** `Matt.14.4` la: `\\q2 eī` → `eī`
2. **Apply:** `Matt.14.3` la: `Cēperat` → `Ceperat`
3. Kept by its own line.
   **Decision:** keep
   **Apply:** `Matt.14.3` la: `enim` → `autem`
"""


class Parse(unittest.TestCase):
    def setUp(self):
        self.items = review.parse(REVIEW)

    def test_items_and_lines(self):
        self.assertEqual([(i.group[:1], i.number, len(i.replacements)) for i in self.items],
                         [("A", 1, 1), ("A", 2, 1), ("B", 1, 1), ("B", 2, 1), ("B", 3, 1), ("C", 1, 2), ("C", 2, 1),
                          ("C", 3, 1)])
        r = self.items[1].replacements[0]
        self.assertEqual((r.vid, r.column, r.old, r.new), ("Matt.14.3", "la", "vīnctum dederat", "vīnctum trādiderat"))

    def test_decisions(self):
        self.assertEqual([review.accepted(i) for i in self.items], [True, True, True, False, True, True, False, False])

    def test_select_by_number_or_all(self):
        self.assertEqual(len(review.select(self.items, everything=True)), 8)
        self.assertEqual([i.number for i in review.select(self.items, numbers=[2])], [2, 2, 2])

    def test_apply_line_with_condition(self):
        items = review.parse("**Decision:** keep yours\n**Apply** (only if you restore it): `Gen.1.1` la: `a` → `b`\n")
        self.assertEqual(len(items), 1)
        self.assertFalse(review.accepted(items[0]))


class Apply(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.path = pathlib.Path(folder.name) / "MAT.usfm"
        self.path.write_text(USFM, encoding="utf-8")

    def run_items(self, items, texts=None):
        outcomes, texts = review.apply(items, texts, to=self.path)
        return [o.status for o in outcomes], texts[self.path]

    def test_verse_span_takes_the_markers_before_it(self):
        start, end = review.verse_span(USFM, "Matt.14.3")
        self.assertTrue(USFM[start:end].startswith("\\p\n\\v 3 "))
        self.assertTrue(USFM[start:end].endswith("cūstōdiam.\n"))
        start, end = review.verse_span(USFM, "Matt.14.4")
        self.assertTrue(USFM[start:end].startswith("\\q1 \\v 4"))
        self.assertTrue(USFM[start:end].endswith("licēre.\n"))

    def test_accepted_items_compose(self):
        statuses, text = self.run_items(review.select(review.parse(REVIEW)))
        self.assertEqual(statuses, ["ok"] * 6)
        self.assertIn("\\v 1 Per id tempus audiēns autem Hērōdēs,", text)
        self.assertIn("et vīnctum trādiderat in cūstōdiam.", text)
        self.assertIn("\\v 2 dīxit suīs discipulīs, eum esse", text)
        self.assertIn("\\p\n\\v 4 quod Hērōdī dīxisset Jōhannēs,\neī nōn licēre.\n\\c 15", text)
        self.assertIn("et dīxit Hērōdēs rēx.", text)
        self.assertIn("\\v 3 Cēperat enim", text)                  # items C2 and C3 not accepted

    def test_scoped_to_the_verse(self):
        # Hērōdēs is in 14.1, 14.3 and 15.1; inside 15.1 it is unique.
        items = review.parse("**Decision:** accept\n1. **Apply:** `Matt.14.1` la: `Hērōdēs` → `Herodes`\n")
        self.assertEqual(self.run_items(items)[0], ["ok"])

    def test_ambiguous_and_missing(self):
        items = review.parse("**Decision:** accept\n1. **Apply:** `Matt.14.3` la: `Jōhannem` → `x`\n"
                             "2. **Apply:** `Matt.14.3` la: `nusquam` → `y`\n")
        self.assertEqual(self.run_items(items)[0], ["ok", "missing"])
        items = review.parse("**Decision:** accept\n1. **Apply:** `Matt.14.4` la: `ō` → `o`\n")
        self.assertEqual(self.run_items(items)[0], ["ambiguous"])

    def test_already_applied(self):
        items = review.select(review.parse(REVIEW))
        _, text = self.run_items(items)
        self.path.write_text(text, encoding="utf-8")
        statuses, again = self.run_items(items)
        self.assertEqual(statuses, ["already"] * 6)
        self.assertEqual(again, text)

    def test_paragraph_added_before_a_verse(self):
        items = review.parse("**Decision:** accept\n1. **Apply:** `Matt.14.2` la: `\\v 2 dīxit` → `\\p \\v 2 dīxit`\n")
        statuses, text = self.run_items(items)
        self.assertEqual(statuses, ["ok"])
        self.assertIn("Hērōdēs,\n\\p\n\\v 2 dīxit", text)
        self.assertEqual(self.run_items(items, {self.path: text})[0], ["already"])


class Layout(unittest.TestCase):
    def test_markers_start_lines(self):
        self.assertEqual(review._layout("iērunt. \\p \\v 13 Eō"), "iērunt.\n\\p\n\\v 13 Eō")
        self.assertEqual(review._layout("dīxit: \\q1 \\v 2 Abrahāmus \\q2 Isaācus"),
                         "dīxit:\n\\q1 \\v 2 Abrahāmus\n\\q2 Isaācus")
        self.assertEqual(review._layout("Isaācum. \\v 3 Jūdās"), "Isaācum.\n\\v 3 Jūdās")


if __name__ == "__main__":
    unittest.main()
