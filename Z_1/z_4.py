from itertools import *

def f(u, w, x, y):
    return (not((y <= w) == x)) and u


for i1, i2, i3 in product([0, 1], repeat=3):
    table = [(0, 1, 0, i1), (0, 1, 1, 1), (1, 0, 1, i2), (1, i3, 1, 1)]
    for p in permutations('uwxy'):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 1, 1]:
            if len(table) == len(set(table)):
                print(*p)
