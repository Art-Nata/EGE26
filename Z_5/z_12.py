def cc(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s


for n in range(1, 10000):
    d = cc(n)
    d1 = list(d)
    d1 = sorted(d1, reverse=True)
    d2 = ''.join(d1)
    d2 = d2 + d2[0]
    r = int(d2, 3)
    if r < 1200:
        print(d, r)