from itertools import *


count = 0

for s in permutations('ТОНЯ', 3):
    s = ''.join(s)
    s = s.replace('Я', 'О')
    if 'ОО' not in s:
        count += 1
print(count)