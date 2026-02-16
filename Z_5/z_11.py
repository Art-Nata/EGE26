n = 232
d = f'{n:x}'
print(d)
d1 = ''
for a in d:
    if a in 'abcdef':
        d1 = d1 + a
        print(d1)
print(int(d1, 16))