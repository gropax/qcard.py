from nose.tools import *
from io import StringIO
from qcard.latex import TheoremParser

string = r"""

\theoremstyle{definition}
\newtheorem*{cprob}{Conditional probability}
\begin{cprob}

\( P(A \cap B) = P(B)P(A|B) = P(A)P(B|A) \)

\end{cprob}

"""

class TestTheoremParser:
    def setup(self):
        stream = enumerate(StringIO(string))
        self.parser = TheoremParser(stream)

    def test_parse(self):
        qst, ans = self.parser.parse()
        assert_equal('Conditional probability', qst)
        assert_equal(string.strip() + "\n", ans)

    def test_block_open(self):
        s = "  \\newtheorem*{cprob}{Conditional probability}  \n"
        assert_true(self.parser.block_open(s))
        s = "  \\theoremstyle{definition}  \n"
        assert_true(self.parser.block_open(s))
        s = "  \\begin{cprob}  \n"
        assert_false(self.parser.block_open(s))

    def test_block_close(self):
        qst, ans = self.parser.parse()
        s = "  \\end{cprob} "
        assert_true(self.parser.block_close(s))
        s = "  \\end{bougle} "
        assert_false(self.parser.block_close(s))
