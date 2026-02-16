from functools import *

d = {}
#@lru_cache(None)

for n in range(1, 101):
    if n not in d:
        if n <= 42:
            d[n] = '42'
        if n > 42:
            d[n] = str((n + 1) * (n - 1) * int(d[n - 1]))


print(d[100])