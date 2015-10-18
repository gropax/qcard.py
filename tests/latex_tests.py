from nose.tools import *
from io import StringIO
from qcard.latex import THEOREM_RE, read_theorem, read_constituent_tree

ctree = "\Tree [.S [.NP [.D Le ] [.N chat ]] [.VP [.V mange ] [.NP [.D la ] [.N souris. ]]]]\n"

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

    #def test_cnode_regex(self):
    #    m = CNODE_RE.match("\\Tree [.S [.NP [.N il ]] [.VP [.V pleut ]]]")
    #    assert_equal(m.group('node'), 'S')
    #    assert_equal(m.group('children'), '[.NP [.N il ]] [.VP [.V pleut ]]')

    def test_read_constituent_tree(self):
        inp = StringIO(ctree)
        qst, ans = read_constituent_tree(inp)
        assert_equal(qst, "Le chat mange la souris.")
        assert_equal(ans, ctree)
