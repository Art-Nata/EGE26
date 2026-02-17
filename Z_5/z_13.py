def cc(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s


for n in range(1, 100):
    d = cc(n)
    r = ''
    if n % 3 == 0:
        r = d + d[-2] + d[-1]
    else:
        r = d + cc(n % 3 * 5)
    if int(r, 3) > 133:
        print(n, int(r, 3))