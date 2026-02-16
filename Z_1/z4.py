from itertools import *


n = '149 24569 3789 4128 5268 6258 7389 834567 91237'
s = 'АГДЕИ БВДЖ ВБДЖ ГАИЖ ДАЗВБ ЕАЗЖ ЖИГВБЕ ЗДЕ ИАГЖ'


s = {x[0]: set(x[1:]) for x in s.split()}


for k in permutations('АБВГДЕЖЗИ'):
    n1 = n
    for x1, y in zip('123456789', k):
        n1 = n1.replace(x1, y)
    n1 = {x[0]: set(x[1:]) for x in n1.split()}

    if n1 == s:
        print('1 2 3 4 5 6 7 8 9')
        print(*n1)
