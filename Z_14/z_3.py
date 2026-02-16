#print(int('123', 4))
for n in range(27, 200):
    d = []
    n1 = n
    while n > 0:
        d = [n % 4] + d
        n //= 4
    if d[-3] == 1 and d[-2] == 2 and d[-1] == 3:
        print(d)
        print(n1)