from nose.tools import *
from qcard import AnkiCard


class TestAnkiCard:
    def test_format_field_with_quotes(self):
        s = AnkiCard.format_field('str "with" quotes')
        assert_equal(s, 'str &quot;with&quot; quotes')

    def test_format_field_with_tabs(self):
        s = AnkiCard.format_field("str\twith\ttabs")
        assert_equal(s, "\"str\twith\ttabs\"")

    def test_format_field_with_newlines(self):
        s = AnkiCard.format_field("str\nwith\nnewlines")
        assert_equal(s, "\"str\nwith\nnewlines\"")

    def test_format_field_with_latex_option(self):
        s = AnkiCard.format_field("\\superlatex{tag}", format='latex')
        assert_equal(s, "[latex]\\superlatex{tag}[/latex]")

    def test_generate(self):
        c = AnkiCard(["Question?", "\\supertex{tag}\t\"bougle\"\n\\bigle{}"])
        s = c.generate(format='latex')
        expected = "[latex]Question?[/latex]\t\"[latex]\\supertex{tag}\t&quot;bougle&quot;\n\\bigle{}[/latex]\""
        assert_equal(s, expected)
