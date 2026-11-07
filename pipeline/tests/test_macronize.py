"""Macronizing: parsing lexicon answers, Gaffiot for stems, homographs, j/v and ligatures. The lexicon blocks
are written for the tests in the format of `lrl macron` (no dictionary text is copied)."""

import unittest

from pipeline import harness, macronize

ANXIUS = """anxius  [W]  ← anxiē (W)
    W:comparative
ānxius  [MW]  ← anxius (M), ānxius (W)
    M:a-s---nac
  G Gaffiot: ānxĭus, a, um [freq 9]"""

VENIT = """venit  [MW]  ← venio (M), veniō (W)
    M:v3spia---
vēnit  [MW]  ← venio (M), veniō (W)
    M:v3sria---
  G Gaffiot: vĕnĭō, vēnī, ventum, īre [freq 4]"""

HIDDEN = """dixit  [M]  ← dico (M)
    M:v3sria---
  G Gaffiot: dīcō, dīxī, dictum, ĕre"""


class Marks(unittest.TestCase):
    def test_quantities_and_mark(self):
        self.assertEqual(macronize.long_vowels("vēnērunt"), {1, 3})
        self.assertEqual(macronize.mark("venerunt", {1, 3}), "vēnērunt")
        self.assertEqual(macronize.quantities("hŏmō"), [(1, "S"), (3, "L")])
        self.assertEqual(macronize.quantities("quā̆tuor")[1], (2, "?"))

    def test_key(self):
        self.assertEqual(macronize.key("Jēsūs"), "iesus")
        self.assertEqual(macronize.key("cælī"), "caeli")


class Choose(unittest.TestCase):
    def test_one_candidate_after_gaffiot(self):
        choice = macronize.choose("anxius", macronize.parse(ANXIUS))
        self.assertEqual(choice.longs, {0})                   # both readings become ānxius
        self.assertEqual(choice.how, "lexicon")

    def test_gaffiot_supplies_a_hidden_quantity(self):
        choice = macronize.choose("dixit", macronize.parse(HIDDEN))
        self.assertEqual(macronize.finish("dixit", choice.longs), "dīxit")
        self.assertEqual(choice.how, "gaffiot")

    def test_homograph_left_or_chosen(self):
        entry = macronize.parse(VENIT)
        self.assertEqual(macronize.choose("venit", entry).how, "homograph")
        picked = macronize.choose("venit", entry, prefer=lambda options: frozenset({1}) if frozenset({1}) in options else None)
        self.assertEqual((macronize.finish("venit", picked.longs), picked.how), ("vēnit", "chosen"))

    def test_unknown(self):
        self.assertEqual(macronize.choose("Mahujæl", macronize.parse("mahuiael: no source knows this form")).how, "unknown")


class Finish(unittest.TestCase):
    def test_brief_overrides(self):
        self.assertEqual(macronize.finish("mihi", {3}), "mihi")          # final -i short in mihi
        self.assertEqual(macronize.finish("ejus", {0}), "ejus")          # vowel before j unmarked

    def test_ligatures_only_for_diphthongs(self):
        self.assertEqual(macronize.finish("caeli", {4}), "cælī")
        self.assertEqual(macronize.finish("aeris", {0}), "āeris")
        self.assertEqual(macronize.finish("Israelitae", {3, 4, 6}), "Isrāēlītæ")
        self.assertEqual(macronize.finish("poena", set()), "pœna")

    def test_jv(self):
        self.assertEqual([macronize.jv(w) for w in ("eius", "iam", "Iudas", "iis", "dies", "filius", "novus", "quae")],
                         ["ejus", "jam", "Judas", "iis", "dies", "filius", "novus", "quae"])

    def test_jicio_compounds(self):
        self.assertEqual([macronize.jv(w) for w in ("abicient", "eicere", "Ēiciunt", "proiicit", "reiecit",
                                                     "periculum", "dicere", "abies", "deinde", "obicem")],
                         ["abjicient", "ejicere", "Ējiciunt", "projicit", "rejecit",
                          "periculum", "dicere", "abies", "deinde", "obicem"])

    def test_jv_keeps_names(self):
        self.assertEqual([macronize.jv(w) for w in ("Abius", "Abium", "adiumentum")],
                         ["Abius", "Abium", "adjumentum"])


class Normalize(unittest.TestCase):
    def test_rules_and_division(self):
        tokens = [("Matt.12.30", "Qui"), ("Matt.12.30", "me"), ("Matt.12.30", "cum"), ("Gen.9.23", "Humeris"),
                  ("Gen.9.23", "eius")]
        out = harness.normalize(tokens, {"humeris": "umeris"}, [(("me", "cum"), ("mecum",))])
        self.assertEqual([w for _, w in out], ["Qui", "mecum", "Umeris", "ejus"])


class Score(unittest.TestCase):
    def test_spelling_word_division_and_vowels(self):
        out = [harness.Word("Gen.1.1", w, "lexicon") for w in ("mē", "cum", "humerīs", "vēnit", "ēsse")]
        gold = [("Gen.1.1", w) for w in ("mēcum", "umerīs", "vēnit", "esse")]
        s = harness.score(out, ["me", "cum", "humeris", "venit", "esse"], gold)
        self.assertEqual((s.words, s.word_ok, s.spelled, s.spelling_ok), (4, 4, 4, 2))
        self.assertEqual(s.errors["spelling: word division"], 1)
        self.assertEqual(s.errors["spelling: respelling missed"], 1)
        self.assertEqual((s.vowels, s.vowels_ok), (4, 3))      # vēnit right; ēsse has one extra long vowel

    def test_dominant_marking(self):
        import collections
        self.assertEqual(harness.dominant(collections.Counter({frozenset({1}): 9, frozenset(): 1})), frozenset({1}))
        self.assertIsNone(harness.dominant(collections.Counter({frozenset({1}): 6, frozenset(): 4})))


if __name__ == "__main__":
    unittest.main()
