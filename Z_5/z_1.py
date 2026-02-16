for n in range(100, 200):
    s = str(n)
    x = int(s[0]) + int(s[1])
    y = int(s[1]) + int(s[2])
    rez = str(x) + str(y)
    print(n, rez)