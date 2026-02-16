from itertools import *
from  functools import *




#@lru_cache(maxsize=32)

count = 0
for s in product('0123456789abc', repeat=7):
    s = ''.join(s)
    if s[0] != 0 and s.count('5') >= 2:
        for n in '2468ac':
            s = s.replace(n, '0')
        for n in '3579b':
            s = s.replace(n, '1')
        if '00' not in s and '11' not in s:
            count += 1
print(count)
