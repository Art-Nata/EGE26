from itertools import *


def f(a, b, c, d):
    return ((a == b) or not(c == d)) and (b <= (not c))


table = [(0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 0, 0)]

for p in permutations('abcd'):
    if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
        print(*p)
