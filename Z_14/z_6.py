for x in range(17):
    s1 = f'5432{x}67'
    s2 = f'302{x}'
    z = int(s1, 17) + int(s2, 17)
    print(s1, int(s1, 17), s2, int(s2, 17), z)
    if z % 19 == 0:
        print(x)