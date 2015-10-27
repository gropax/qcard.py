import re

BEGIN_RE = re.compile(r"\s*\\begin\{(?P<label>\w+)\}")
END_RE = re.compile(r"\s*\\end\{(?P<label>\w+)\}")

class ParseError(Exception):
    pass

class BlockParser:
    # stream is an enumerated line iterator
    def __init__(self, stream):
        self.stream = stream
        self.index = None

    def parse(self):
        self.block = []
        opened = False

        i, line = next(self.stream)  #.readline()
        while line:
            if not opened and self.block_open(line):
                opened = True
                self.index = i

            if opened:
                self.block.append(line)
                self.parse_line(line)

                if self.block_close(line):
                    break

            i, line = next(self.stream)  # .readline()

        return self.output()

    def block_open(self, line):
        return bool(line.strip())

    def block_close(self, line):
        return not bool(line.strip())

    def output(self):
        pass

    def parse_line(self, line):
        pass
