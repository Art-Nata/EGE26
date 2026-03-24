from itertools import *


n = "156 24678 34678 42357 514 61238 72348 82367"
p = "ADGHB BAC CBF DFEGA EDFHG FDEHC GAHED HFEGA"
p = {x[0]: set(x[1:]) for x in p.split()}
s = ''
for k in permutations('ABCDEFGH'):
    s = n
    for x, y in zip('12345678', k):
        s = s.replace(x, y)
    s = {x[0]: set(x[1:]) for x in s.split()}
    if s == p:
        print('1 2 3 4 5 6 7 8')
        print(*k)
