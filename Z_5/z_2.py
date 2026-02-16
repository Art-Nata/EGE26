for n in range(10, 100):
    s = str(n)
    x = int(s[0]) + int(s[1])
    y = int(s[0]) * int(s[1])
    rez = str(x) + str(y) if x <= y else str(y) + str(x)
    if rez == '710':
        print(n)
