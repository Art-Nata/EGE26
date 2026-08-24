"""Ребята составляют 8-значные шестнадцатеричные числа.
Сколько существует различных чётных чисел, в записи которых
цифра 0 встречается ровно два раза?"""

from itertools import *


count_num = 0
alp = '0123456789ABCDEF'
for x in product(alp, repeat=8):
    num_not_0 = x[0] != '0'
    count_0 = x.count('0') == 2
    even = x[-1] in alp[::2]
    if num_not_0 and count_0 and even:
        print(x)
        count_num += 1
print(count_num)