import re, sys
from qcard import BlockParser, ParseError, BEGIN_RE, END_RE

ALGORITHM_RE = re.compile(r"\s*\\caption\{(?P<caption>.*)\}")

class AlgorithmParser(BlockParser):
    def parse_line(self, line):
        m = ALGORITHM_RE.match(line)
        if m:
            self.caption = m.group('caption')

    def output(self):
        if not hasattr(self, 'caption'):
            raise ParseError('line %i: algorithm must have a caption.' % self.index)

        return [self.caption, "".join(self.block)]

    def block_open(self, line):
        m = BEGIN_RE.match(line)
        return m and m.group('label') == 'algorithm'

    def block_close(self, line):
        m = END_RE.match(line)
        return m and m.group('label') == 'algorithm'
