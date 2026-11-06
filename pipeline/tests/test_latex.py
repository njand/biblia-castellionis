"""LaTeX → USFM → LaTeX, built from the forms met in the finished chapters."""

import unittest

from pipeline import books, gold, latex, parallel

MATT = books.BY_OSIS["Matt"]
BOOK = r"""\Liber[Ēvangelium Auctōre\\Matthæō]{Matthæus}

\Caput
\Versus Ēnumerātiō generis Jēsū, % a comment
prōgnātī Dāvīde:

\indentpattern{01}
\begin{verse}
\begin{patverse*}
\Versus Abrahāmus genuit Isaācum.\\
Isaācus Jācōbum.\\
\Versus Jūdās Phārem.
\end{patverse*}
\end{verse}

\Versus Jōsē\-phus vērō: ``Nē metue.'' Euphrātem—\Versus vidēlicet Cenæōs.
\Versus Ita dīcentem: \emph{``{}`Virgō ventrem lātūra est,'{}''} quod est ``Nōbīscum Deus.''
\Versus Is est dē quō scrīptum est:
\indentpattern{0}
\begin{verse}
\begin{patverse*}
\emph{``Vōx clāmantis,\\
\Versus parāte viam,\\
\medskip
rēctās facite sēmitās.''}
\end{patverse*}
\end{verse}
\Versus Ipse autem Jōhannēs.

% \Caput
% \Versus Per id tempus audiēns Hērōdēs,
% \Versus dīxit suīs.
"""


class Migration(unittest.TestCase):
    def setUp(self):
        self.live, self.draft, self.counts = latex.to_usfm(BOOK, MATT)

    def test_header_and_markers(self):
        self.assertEqual(self.live.split("\n\\c 1\n")[1].splitlines(), [
            "\\p",
            "\\v 1 Ēnumerātiō generis Jēsū, prōgnātī Dāvīde:",
            "\\q1 \\v 2 Abrahāmus genuit Isaācum.",
            "\\q2 Isaācus Jācōbum.",
            "\\q1 \\v 3 Jūdās Phārem.",
            "\\p",
            "\\v 4 Jōsē\u00adphus vērō: “Nē metue.” Euphrātem—",
            "\\v 5 vidēlicet Cenæōs.",
            "\\v 6 Ita dīcentem: \\qt “‘Virgō ventrem lātūra est,’”\\qt* quod est “Nōbīscum Deus.”",
            "\\v 7 Is est dē quō scrīptum est:",
            "\\q1 \\qt “Vōx clāmantis,\\qt*",
            "\\q1 \\v 8 \\qt parāte viam,\\qt*",
            "\\b",
            "\\q1 \\qt rēctās facite sēmitās.”\\qt*",
            "\\m",
            "\\v 9 Ipse autem Jōhannēs."])
        self.assertIn("\\mt1 Ēvangelium Auctōre // Matthæō", self.live)
        self.assertEqual(self.counts, {1: 9, 2: 2})

    def test_draft_chapter_kept_apart(self):
        self.assertNotIn("Hērōdēs", self.live)
        self.assertIn("\\c 2\n\\p\n\\v 1 Per id tempus audiēns Hērōdēs,\n\\v 2 dīxit suīs.", self.draft)

    def test_round_trip(self):
        diffs, _ = latex.compare(latex.live_latex(BOOK), latex.to_latex(self.live))
        # The two changes: a space before a mid-line verse number (USFM always has one), and \medskip becomes a
        # stanza break (a blank line), which closes the \emph{…} around it and reopens it after.
        self.assertEqual([(old, new) for old, new, _ in diffs],
                         [([], [" "]), (["\\\\", "\\medskip"], ["}", "¶", "\\emph", "{"])])
        diffs, _ = latex.compare(latex.draft_latex(BOOK), latex.to_latex(self.draft))
        self.assertEqual(diffs, [])

    def test_emph_rejoined_across_lines(self):
        regenerated = latex.to_latex(self.live)
        self.assertIn("\\emph{``{}`Virgō ventrem lātūra est,'{}''}", regenerated)
        self.assertIn("\\emph{``Vōx clāmantis,\\\\\n\\Versus parāte viam,}\n\n\\emph{rēctās", regenerated)

    def test_comments_listed(self):
        self.assertEqual(latex.comments(BOOK), [(4, "% a comment")])

    def test_unknown_command_refused(self):
        with self.assertRaisesRegex(latex.LatexError, "unknown command"):
            latex.to_usfm("\\Liber{X}\n\\Caput\n\\Versus Ecce \\textbf{hoc}.\n", MATT)


class Gold(unittest.TestCase):
    def test_rows(self):
        rows = {vid: (text, marks, layout) for vid, text, marks, layout in gold.rows(latex.to_usfm(BOOK, MATT)[0], "Matt")}
        self.assertEqual(rows["Matt.1.2"], ("Abrahāmus genuit Isaācum. Isaācus Jācōbum.", "q1",
                                            "Abrahāmus genuit Isaācum. \\q2 Isaācus Jācōbum."))
        self.assertEqual(rows["Matt.1.4"][0], "Jōsēphus vērō: “Nē metue.” Euphrātem—")      # soft hyphen gone
        self.assertEqual(rows["Matt.1.6"][0], "Ita dīcentem: “‘Virgō ventrem lātūra est,’” quod est “Nōbīscum Deus.”")
        self.assertEqual(rows["Matt.1.6"][2], "Ita dīcentem: \\qt “‘Virgō ventrem lātūra est,’”\\qt* quod est “Nōbīscum Deus.”")
        self.assertEqual(rows["Matt.1.9"][1], "m")


class StripInline(unittest.TestCase):
    def test_space_after_closing_marker_is_text(self):
        self.assertEqual(parallel.strip_inline("\\wj Follow me,\\wj* he said"), "Follow me, he said")
        self.assertEqual(parallel.strip_inline("\\qt Vōx,\\qt* inquit", keep=("qt",)), "\\qt Vōx,\\qt* inquit")


if __name__ == "__main__":
    unittest.main()
