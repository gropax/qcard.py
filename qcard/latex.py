import re

THEOREM_RE = re.compile(r"\\newtheorem\*?\{\w+\}\{(?P<title>.*)\}")

def read_block(stream, **opts):
    proc = opts.get('proc', lambda l: None)
    blk = []
    line = stream.readline()
    while line.strip():
        proc(line)
        blk.append(line)
        line = stream.readline()
    return blk

def read_theorem(stream):
    # @fixme Ugly
    title = []
    def read_title(line):
        m = THEOREM_RE.match(line)
        if m: title.append(m.group('title'))

    blk = read_block(stream, proc=read_title)

    if not title:
        raise Exception("Could not find theorem's title")

    return [title[0], "".join(blk)]


def read_constituent_tree(stream):
    blk = read_block(stream)
    ans = " ".join(blk)
    qst = " ".join(re.sub(r"\\Tree|\[|\]|\.\w+", "", ans).split())
    return (qst, ans)
