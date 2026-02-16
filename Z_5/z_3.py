for n in range(1000, 10000):
    s = str(n)
    r1 = sum([int(x) for x in s if int(x) % 2 == 0]) ** 2
    max_n = max([int(x) for x in s])
    min_n = min([int(x) for x in s])
    r2 = (max_n - min_n) ** 3
    rez = str(r1) + str(r2) if r1 <= r2 else str(r2) + str(r1)
    if rez == '4343':
        print(n)