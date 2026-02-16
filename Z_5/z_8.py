for n in range(33, 100):
    s = f'{n:b}'
    if n % 2 != 0:
        s = '1' + s
        s = s[:-2]
        s = s + '10'
    else:
        s = s + '1'
        s = s[2:]
        s = '10' + s
    r = int(s, 2)
    print(r)