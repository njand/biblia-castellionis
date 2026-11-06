"""Learning spelling rules: alignment and sorting, built from pairs met in the finished chapters."""

import unittest

from pipeline import rules


def words(text, vid="Gen.1.1"):
    return [(vid, word) for word in rules.WORD.findall(text)]


class Folding(unittest.TestCase):
    def test_fold(self):
        self.assertEqual(rules.fold("Jēsūs"), "iesus")
        self.assertEqual(rules.fold("cælī"), "caeli")
        self.assertEqual(rules.unmacron("tenebrīsque"), "tenebrisque")

    def test_ligature(self):
        self.assertEqual(rules.ligature("Aegypti poenae"), "Ægypti pœnæ")


class Align(unittest.TestCase):
    def kinds(self, witness, gold):
        return [(p.kind, p.old, p.new) for p in rules.align(words(witness), words(gold)) if p.kind != "same"]

    def test_mechanical_kinds(self):
        self.assertEqual(self.kinds("terrae Divinus iniuria foedus Israelitis",
                                    "terræ dīvīnus injūria foedus Isrāēlītīs"), [
            ("ligature", "terrae", "terræ"), ("case", "Divinus", "divinus"), ("j/v", "iniuria", "injuria"),
            ("ligature-kept", "foedus", "foedus"), ("ligature-kept", "Israelitis", "Israelitis")])

    def test_split_join_and_wording(self):
        self.assertEqual(self.kinds("me cum ambulat septimodecimo", "mēcum ambulat septimō decimō"), [
            ("split/join", "me cum", "mecum"), ("split/join", "septimodecimo", "septimo decimo")])
        self.assertEqual(self.kinds("in dupondio venit", "in duōbus assāriīs venit"),
                         [("wording", "dupondio", "duobus assariis")])

    def test_one_for_one_waits_for_the_lexicon(self):
        self.assertEqual(self.kinds("ne tentato Dominum", "nē temptātō Dominum"), [("replace", "tentato", "temptato")])


class Sorting(unittest.TestCase):
    def test_edit(self):
        self.assertEqual(rules._edit("tentato", "temptato"), ("n", "mp", "te", "tato"))
        self.assertEqual(rules._edit("humeris", "umeris"), ("h", "", "", "umeris"))

    def test_hiatus(self):
        for word in ("Isrāēlītīs", "hērōēs", "āerem", "coeunte", "coēmptī"):
            self.assertTrue(rules.hiatus(word), word)
        for word in ("foedus", "coepit", "poena", "proeliō"):
            self.assertFalse(rules.hiatus(word), word)

    def test_variant_keys(self):
        self.assertEqual(rules.variant_key("ējicere"), rules.variant_key("ēicere"))
        self.assertEqual(rules.variant_key("tentātō"), rules.variant_key("temptātō"))
        self.assertEqual(rules.variant_key("præsæpī"), rules.variant_key("præsēpī"))
        self.assertEqual(rules.strict_key("cœpit"), rules.strict_key("coepit"))
        self.assertNotEqual(rules.strict_key("hōra"), rules.strict_key("ōra"))

    def test_rule_rows_flag_inconsistency(self):
        learned = rules.Learned(pairs=[
            rules.Pair("respelling", "tentato", "temptato", "Matt.4.7"),
            rules.Pair("same", "tentato", "tentato", "Luke.4.12"),
            rules.Pair("split/join", "me cum", "mecum", "Matt.12.30")], gold_words=3)
        rows = {(old, new, scope): note for old, new, scope, status, note in rules.rule_rows(learned)}
        self.assertIn("but tentato kept 1× (Luke.4.12): inconsistent", rows[("tentato", "temptato", "word")])
        self.assertEqual(rows[("me cum", "mecum", "phrase")], "1× (Matt.12.30)")


if __name__ == "__main__":
    unittest.main()
