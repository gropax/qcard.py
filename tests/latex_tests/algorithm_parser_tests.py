from nose.tools import *
from io import StringIO
from qcard.latex import AlgorithmParser
from qcard.latex.algorithm_parser import ALGORITHM_RE
import sys

string = r"""

\begin{algorithm}
  \KwIn{Grammar}
  \KwOut{Left-factorized Grammar}

  \ForEach{nonterm $A$}{
    \ForEach{prefix $\alpha$ common to at least 2 rules}{
      replace $A \rightarrow \alpha \beta_1 |...| \alpha \beta_m | \gamma_1 |...| \gamma_n, \quad \gamma_k \neq \alpha \delta_k$ \\
      with $A \rightarrow \alpha A' | \gamma_1 |...| \gamma_n$ \\
      $\ \ \ \ \ \ A' \rightarrow \beta_1 |...| \beta_m$ \;
    }
  }

  \caption{Left factorization algorithm}
\end{algorithm}

"""

class TestAlgorithmParser:
    def setup(self):
        stream = enumerate(StringIO(string))
        self.parser = AlgorithmParser(stream)

    def test_algorithm_re(self):
        s = "  \caption{My cool algorithm} \n"
        m = ALGORITHM_RE.match(s)
        assert_is_not_none(m)
        assert_equal('My cool algorithm', m.group('caption'))

    def test_parse(self):
        qst, ans = self.parser.parse()
        assert_equal('Left factorization algorithm', qst)
        assert_equal(string.strip() + "\n", ans)

    def test_block_open(self):
        s = "  \\begin{algorithm}  \n"
        assert_true(self.parser.block_open(s))
        s = "  \\begin{cprob}  \n"
        assert_false(self.parser.block_open(s))

    def test_block_close(self):
        qst, ans = self.parser.parse()
        s = "  \\end{algorithm} "
        assert_true(self.parser.block_close(s))
        s = "  \\end{bougle} "
        assert_false(self.parser.block_close(s))
