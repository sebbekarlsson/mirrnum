class InfiniteLoopError(Exception):
    pass


mirror = lambda x: int(str(x)[::-1])
calcnext = lambda x: abs(x - mirror(x))
append = lambda x, y: [x.append(y), y][1]


def calc(x, s=[]):
    while x > 0:
        if s.count(x) > 2:
            raise InfiniteLoopError

        x = append(s, calcnext(x))

    return s
