from itertools import *

k = 0

for n in product('01234567', repeat=7):
    s = ''.join(n)
    if s[0] != '0':
        if all(s.count(x) == 1 for x in s):
            for x in '246':
                s = s.replace(x, '0')
            for x in '357':
                s = s.replace(x, '1')
            if '11' not in s and '00' not in s:
                k += 1
print(k)