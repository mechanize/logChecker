
def compare(**param) -> bool:
    is_identical = True
    f1 = open(param.get('monpoly'), 'r')
    f2 = open(param.get('stream'), 'r')
    for i, j in zip(f1.readlines(), f2.readlines()):
        is_identical &= is_equal(monpoly=parse_line('monpoly', i),
                                 stream=parse_line('stream', j))
    return is_identical


def parse_line(tool: str, line: str) -> (str, [str]):
    # returns (timestamp, [output variables])
    return {
        'monpoly': (line.split(".")[0][1:], line.split(":")[-1].strip()[1:-1].split(",")),
        'stream': (line.split(":")[0][1:-1], line.split(":")[-1].strip().split(", "))
    }.get(tool)


def is_equal(**param) -> bool:
    if len(set([e[0] for e in param.values()])) != 1:  # same timestamp?
        return False
    if len(set([len(e[1]) for e in param.values()])) != 1:  # same number of output variables?
        return False
    if len(set([e for l in param.values() for e in l[1]])) != len(set(param.values()[0][1])):  # same output variables?
        return False
    return True
