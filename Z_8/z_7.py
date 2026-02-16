from itertools import *

k = 0

for n in product('0123456789abcdef', repeat=5):
    s = ''.join(n)
    if s[0] != '0':
        for x in '012345678':
            s = s.replace(x, '9')
        if s.count('9') == 1:
            k += 1
print(k)