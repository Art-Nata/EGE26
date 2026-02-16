for x in range(400, 1000):
    n = 16 ** 560 + 16 ** 120 - x
    d = []
    while n  > 0:
        d = [n % 16] + d
        n //= 16
    if d.count(0) == 442:
        print(x)
        break