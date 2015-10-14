from nose.tools import *
from io import StringIO
from qcard.latex import THEOREM_RE, read_theorem


class TestLatex:
    def test_theorem_regex_title_group(self):
        m = THEOREM_RE.match("\\newtheorem*{bayes}{Bayes' theorem}")
        assert_equal(m.group('title'), "Bayes' theorem")

    def test_read_theorem(self):
        s = "first\n\\newtheorem*{bayes}{Bayes' theorem}\nsecond\nthird\n"
        inp = StringIO(s)
        qst, ans = read_theorem(inp)
        assert_equal(qst, "Bayes' theorem")
        assert_equal(ans, s)
