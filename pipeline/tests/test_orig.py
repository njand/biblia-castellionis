"""Castellio's text as printed: each settled word against its 1573 OCR word, from forms in Matthew 14–28."""

import unittest

from pipeline import align, orig


class Choose(unittest.TestCase):
    def test_ocr_keeps_u_v_i_j_and_puts_long_s_back(self):
        self.assertEqual(orig.choose("revīxisset", "reuixiffet"), ("reuixisset", "ocr"))
        self.assertEqual(orig.choose("Jōhannem", "Iohannem"), ("Iohannem", "ocr"))
        self.assertEqual(orig.choose("ut", "vt"), ("vt", "ocr"))

    def test_accents_dropped(self):
        self.assertEqual(orig.choose("quod", "quòd"), ("quod", "ocr"))

    def test_rule_spellings_are_printed(self):
        self.assertEqual(orig.choose("quidquid", "quicquid"), ("quicquid", "rule"))
        self.assertEqual(orig.choose("iīs", "eis"), ("eis", "rule"))

    def test_que_abbreviation_misread(self):
        self.assertEqual(orig.choose("duōbusque", "duobusąs"), ("duobusque", "ocr"))
        self.assertEqual(orig.choose("Atque", "atqs")[0], "atque")

    def test_printer_variants(self):
        self.assertEqual(orig.choose("mīlia", "millia"), ("millia", "variant"))
        self.assertEqual(orig.choose("litterīs", "literis"), ("literis", "variant"))
        self.assertEqual(orig.choose("monumentō", "monimento"), ("monimento", "variant"))
        self.assertEqual(orig.choose("dēgluttītis", "deglutitis"), ("deglutitis", "variant"))
        self.assertEqual(orig.choose("nummīs", "numis"), ("numis", "variant"))

    def test_e_against_settled_ae_is_e_caudata(self):
        self.assertEqual(orig.choose("quærentēs", "querentes"), ("quærentes", "ę"))

    def test_nasal_bar(self):
        self.assertEqual(orig.choose("animam", "animá"), ("animam", "nasal"))
        self.assertEqual(orig.choose("Cumque", "Cúque"), ("Cumque", "nasal"))
        self.assertEqual(orig.choose("monte", "mote"), ("monte", "nasal"))

    def test_misread_m(self):
        self.assertEqual(orig.choose("autem", "autein"), ("autem", "misread"))

    def test_1738_ligatures_written_out_and_stray_capitals(self):
        self.assertEqual(orig.choose("cælum", "caelum"), ("cælum", "ocr"))
        self.assertEqual(orig.choose("offūsum", "ofFufum"), ("offusum", "ocr"))

    def test_more_printer_spellings(self):
        self.assertEqual(orig.choose("arcessītum", "accersitum"), ("accersitum", "variant"))
        self.assertEqual(orig.choose("audierint", "audiuerint"), ("audiuerint", "variant"))
        self.assertEqual(orig.choose("tetrarchē", "tetrarcha"), ("tetrarcha", "variant"))

    def test_no_ocr_word(self):
        self.assertEqual(orig.choose("ūxōrem", None), ("vxorem", "none"))


class FollowThePage(unittest.TestCase):
    """Decision 58: the printed text follows the page, not a majority."""

    def test_lexicon_only_where_the_print_has_one_spelling(self):
        known = orig.Lexicon()
        known["iīs"].update({"eis": 452, "ijs": 53})
        known["condiciō"].update({"conditio": 4, "condicio": 1})
        chapter = orig.Chapter(1, words=[orig.Word("Acts.1.1", "iīs", None, "iis", "none"),
                                         orig.Word("Acts.1.1", "condiciō", None, "condicio", "none")])
        orig.from_lexicon([chapter], known)
        self.assertEqual([(w.form, w.kind) for w in chapter.words], [("iis", "doubt"), ("conditio", "lexicon")])

    def test_e_caudata_only_where_the_ocr_reads_ae_in_the_stem(self):
        known = orig.Lexicon()
        known.literal_ae.update({"prae": 573, "saec": 0})
        known.e_taken.update({"prae": 33, "saec": 31})
        chapter = orig.Chapter(1, words=[orig.Word("Matt.26.32", "præcēdam", "precedam", "præcedam", "ę"),
                                         orig.Word("Eph.2.7", "sæculīs", "seculis", "sæculis", "ę")])
        orig.check_e_caudata([chapter], known)
        self.assertEqual([w.form for w in chapter.words], ["præcedam", "seculis"])

    def test_joined_words(self):
        words = [orig.Word("Matt.26.53", "plūs", None, "plusquam", "read"),
                 orig.Word("Matt.26.53", "quam", None, orig.JOINED, "read"),
                 orig.Word("Matt.26.53", "duodecim", None, "duodecim", "ocr")]
        self.assertEqual(orig.verse_text(words), "plusquam duodecim")


class Printerize(unittest.TestCase):
    def test_conventions(self):
        self.assertEqual(orig.printerize("ūxōrem"), "vxorem")
        self.assertEqual(orig.printerize("revīxisset"), "reuixisset")
        self.assertEqual(orig.printerize("Jūdæa"), "Iudæa")
        self.assertEqual(orig.printerize("Unde"), "Vnde")


class Ligatures(unittest.TestCase):
    def test_mixed_stems_take_oe(self):
        known = {"cælum": {"cælum": 24, "cœlum": 17}, "cēpit": {"cæpit": 3}, "coepit": {"cœpit": 40}}
        stems = orig.ligature_stems(known)
        chapter = orig.Chapter(1, words=[orig.Word("Matt.1.1", "cælum", "cælum", "cælum", "ocr"),
                                         orig.Word("Matt.1.1", "cēpit", "cæpit", "cæpit", "variant")])
        orig.fix_ligatures([chapter], stems)
        self.assertEqual([w.form for w in chapter.words], ["cœlum", "cæpit"])


class Build(unittest.TestCase):
    def test_punctuation_and_marginal_reference(self):
        rows = [("Matt.26.31", "Tum Jēsūs: “Vōs omnēs,” inquit iīs, “mē dēserētis hāc nocte. Scrīptum est enim: "
                               "Percutiam pāstōrem, et dispergentur ovēs gregis.")]
        witness = align.Witness("31 Tum Iefus: Vos omnes, inquit eis, me deferetis hac nocte. Scriptum eft enim: "
                                "Percutiam paftorem & 106. 16. 30 difpergentur oues gregis.", anchors=True)
        chapter = orig.build_chapter(witness, rows, 26)
        self.assertEqual(orig.verse_text(chapter.words),
                         "Tum Iesus: Vos omnes, inquit eis, me deseretis hac nocte. Scriptum est enim: "
                         "Percutiam pastorem et dispergentur oues gregis.")


if __name__ == "__main__":
    unittest.main()
