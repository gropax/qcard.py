from nose.tools import *
from unittest.mock import MagicMock, call
from io import StringIO
from qcard import BlockParser

string = r"""

block1-line1
line2
line3

block2
...

"""

class TestBlockParser:
    def setup(self):
        stream = enumerate(StringIO(string))
        self.parser = BlockParser(stream)

    def test_parse(self):
        self.parser.output = MagicMock()
        self.parser.parse_line = MagicMock()

        self.parser.parse()

        calls = [call('block1-line1\n'), call('line2\n'), call('line3\n')]
        self.parser.parse_line.assert_has_calls(calls)

        self.parser.output.assert_called()

    def test_index(self):
        self.parser.parse()
        assert_equal(2, self.parser.index)

    def test_block(self):
        self.parser.parse()
        block = ["block1-line1\n", "line2\n", "line3\n", "\n"]
        assert_equal(block, self.parser.block)
