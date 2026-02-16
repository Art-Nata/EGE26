def cc(x):
    alpa = '0123456789ab'
    s = ''
    while x > 0:
        s = alpa[x % 12]  + s
        x = x // 12
    return s

mass = []
alpa = '0123456789ab'
for n in range(0, 1000):
    d = cc(n)
    if n % 4 == 0:
        r = '2' + d + '64'
    else:
        r = d + alpa[max([int(x, 12) for x in d])]
    r_d = int(r, 12)
#    print(n, r_d)
    if r_d > 1799:
        mass.append(r_d)
print(mass)
