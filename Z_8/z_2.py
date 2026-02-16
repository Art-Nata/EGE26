from itertools import product

k = 0
for s in product(sorted('ВОСТРГ'), repeat=6):
    s = ''.join(s)
    k += 1
    if s > 'СГОВОР':
        s1 = s.replace('С', 'В').replace('Т', 'В').replace('Р', 'В').replace('Г', 'В')
        if 'ВВ' not in s1:
            print(k, s)