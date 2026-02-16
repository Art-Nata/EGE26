def cc(x):
    s = ''
    while x > 0:
        s = str(x % 4) + s
        x = x // 4
    return s

d = cc(48)
d1 = ''
for a in d:
    if a != '0':
        d1 = d1 + a
print(int(d1, 4))