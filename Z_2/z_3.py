from itertools import *

def f(x, y, w, z):
    return ((w <= y) <= x) or not z

for i1, i2, i3, i4, i5, i6, i7 in product([0, 1], repeat=7):
    table = [(i1, i2, 1, i3), (i4, 0, i5, i6), (i7, 1, 0, 0)]
    for p in permutations('xywz'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
            if len(table) == len(set(table)):
                print(*p)