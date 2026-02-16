a = [int(x) for x in open('17_3.txt')]
rez = []
max_x = max(x for x in a if x % 100 == 42 and len(str(abs(x))) == 4)

for i in range(len(a) - 2):
    x1 = a[i]
    x2 = a[i+1]
    x3 = a[i+2]
    f1 = x1 % 100 == 42 and len(str(abs(x1))) == 4
    f2 = x2 % 100 == 42 and len(str(abs(x2))) == 4
    f3 = x3 % 100 == 42 and len(str(abs(x3))) == 4
    h1 = f1 and f2 or f1 and f3 or f2 and f3 or f1 and f2 and f3
    h2 = x1 + x2 + x3 > max_x
    if h1:
        print(x1, x2, x3, h2)
    if h1 and h2:
        rez.append([x1, x2, x3])
print(len(rez), max(sum(c) for c in rez))