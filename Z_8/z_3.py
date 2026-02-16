from itertools import product

k = 0
for s in product(sorted('УНИВЕРСТ'), repeat=6):
    s = ''.join(s)
    k += 1
    s1 = s.replace('И', 'У').replace('Е', 'У')
    if s[0] in 'НВРСТ' and 'УУУ' in s1:
        print(k, s)