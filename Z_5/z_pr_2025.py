def to3(x):
    s = ''
    while x > 0:
         s = str(x % 3) + s
         x //= 3
    return s


for n in range(1, 100):
    r = to3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += to3(3 * (n % 3))
    if int(r, 3) <= 150:
        print(n, r, int(r, 3))