import sys

sys.setrecursionlimit(10**6)


mirror = lambda x: int(str(x)[::-1])
calcnext = lambda x: abs(x - mirror(x))
append = lambda x, y: [x.append(y), y][1]
calc = lambda x, s=[]: [calc(append(s, calcnext(x)), s), s][1] if x > 0 else 0
