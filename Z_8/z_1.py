from itertools import *

count = 0
k = 0
for s in product(sorted('ДСР'), repeat=3):
    s = ''.join(s)
    k+= 1
    print(s)
    if s[0] == 'С':
        count += 1
print(count)


