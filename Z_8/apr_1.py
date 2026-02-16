from itertools import *


k = 0

for n in product('МАСЛО', repeat=6):
    s = ''.join(n)
    if s.count('С') == 1:
        if s[0] not in 'АО' and s[-1] not in 'МСЛ':
            k += 1

print(k)
