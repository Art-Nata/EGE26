from itertools import *


n = '1458 2568 3567 417 51238 62378 7346 81256'
p = 'ACDF BDHC CABHF DABEH EDGH FACG GFE HDBCE'
p = {t[0]: set(t[1:]) for t in p.split()}

for k in permutations('ABCDEFGH'):
    s = n
    for x, y in zip('12345678', k):
        s = s.replace(x, y)

    s = {x[0]: set(x[1:]) for x in s.split()}
#    if s['A'] == {'B'}:
#        print(s)
    if s == p:
        print('1 2 3 4 5 6 7 8')
        print(k)