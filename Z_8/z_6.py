from itertools import *

count = 0

for s in set(permutations('БИТКОИН')):
    print(s)
    count += 1
print(count)