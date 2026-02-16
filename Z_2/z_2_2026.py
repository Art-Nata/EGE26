from itertools import *


def f(x, y, w, z):
    return (x or y) and (not(y == z)) and (not w)


for i1, i2, i3, i4 in product([0, 1], repeat=4):
    table = [(1, i2, 1, i4), (0, 1, i3, 0), (i1, 1, 1, 0)]
    for p in permutations("xywz"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            if len(table) == len(set(table)):
                print(*p)
