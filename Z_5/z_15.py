def to5(num):
    s = ''
    while num > 0:
        s = str(num % 5) + s
        num //= 5
    return s


for n in range(1, 200):
    r = to5(n)
    total = sum([int(digit) for digit in r])
    if total % 2 == 1:
        r = r[-1] + r[:-1]
    else:
        r += to5(int(str(n)[-1]) * 3)

    if r.count('0') > 2:
        r = int(r, 5)
        print(n)
        break