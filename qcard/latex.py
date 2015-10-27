import re
import sys

def read_block(stream, **opts):
    proc = opts.get('proc', lambda l: None)
    blk = []
    line = stream.readline()
    while line.strip():
        proc(line)
        blk.append(line)
        line = stream.readline()
    return blk

THEOREM_RE = re.compile(r"\\newtheorem\*?\{\w+\}\{(?P<title>.*)\}")

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

ALGO_RE = re.compile(r"\\caption\{(?P<caption>.*)\}")

def read_algorithm(stream):
    # @fixme Ugly
    caption = []
    def read_caption(line):
        sys.stdout.write("line: %s" % line)
        m = ALGO_RE.match(line)
        sys.stdout.write("match: %i\n" % bool(m))
        if m: caption.append(m.group('caption'))

    blk = read_block(stream, proc=read_caption)

    if not caption:
        raise Exception("Could not find algorithm's caption")

    return [caption[0], "".join(blk)]
