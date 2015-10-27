import re
from qcard import BlockParser, ParseError, END_RE

THEOREM_RE = re.compile(r"\s*\\newtheorem\*?\{(?P<name>\w+)\}\{(?P<title>.*)\}")
TH_STYLE_RE = re.compile(r"\s*\\theoremstyle\{definition\}")

class TheoremParser(BlockParser):
    def parse_line(self, line):
        m = THEOREM_RE.match(line)
        if m:
            self.title = m.group('title')
            self.name = m.group('name')

    def output(self):
        if not hasattr(self, 'title'):
            raise ParseError('line %i: theorem must have a title.' % self.index)

        return [self.title, "".join(self.block)]

    def block_open(self, line):
        return THEOREM_RE.match(line) or TH_STYLE_RE.match(line)

    def block_close(self, line):
        m = END_RE.match(line)
        return m and m.group('label') == self.name
