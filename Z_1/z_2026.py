from itertools import *


n = "1258 217 356 468 5138 6347 726 8145"
p = "ACGD BCH CABG DAH EFG FEH GACE HBDF"
p = {x[0]: set(x[1:]) for x in p.split()}

for k in permutations("ABCDEFGH"):
    s = n
    for x,y in zip("12345678", k):
        s = s.replace(x, y)
    s = {x[0]: set(x[1:]) for x in s.split()}
    if s == p:
        print('1 2 3 4 5 6 7 8')
        print(*k)