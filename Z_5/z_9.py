def cc(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x = x // 5
    return s


for n in range(1, 300):
    d = cc(n)
    d = d[::-1]
    d = int(d, 5)
    if d == 61:
        print(n, d)
