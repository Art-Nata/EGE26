from itertools import *


s1 = "1256 21458 3478 4237 5126 6158 7348 82367"
s2 = "АБВГ БАВГ ВАБД ГАБДЖ ДВГЕЗ ЕЖДЗ ЖГЕЗ ЗДЕЖ"

s2 = {x[0]: set(x[1:]) for x in s2.split()}


for k in permutations("АБВГДЕЖЗ"):
    s = s1
    for a, b in zip('12345678', k):
        s = s.replace(a, b)
    s = {x[0]: set(x[1:]) for x in s.split()}
    if s2 == s:
        print("1 2 3 4 5 6 7 8")
        print(*s)