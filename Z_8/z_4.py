from itertools import product

k = 0
for s in product(sorted('АВТОБУС'), repeat=5):
    s = ''.join(s)
    k += 1
    l1 = (s.count('Б') == 1 and s.count('В') == 1 and s.count('Т') == 1 and \
          s.count('У') == 1 and s.count('С') == 1)
    if 'А' not in s and 'О' not in s and l1 and \
        s[-2] == 'С' and s[-1] == 'Б':
        print(k, s)