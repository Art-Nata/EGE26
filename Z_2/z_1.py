from itertools import *

def f(x, y, w, z):
    return (x <= y) or (not(w <= z))

table = [(1, 0, 0, 1), (0, 0, 0, 1), (1, 0, 1, 1)]

for p in permutations('xyzw'):
    if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
        print(*p)