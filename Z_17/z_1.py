a = [int(x) for x in open('17.txt')]
rez = []
max_2 = max(x for x in a if len(str(x)) == 2)

for i in range(len(a) - 1):
    x1 = a[i]
    x2 = a[i + 1]
    if (len(str(abs(x1))) == 2 or len(str(abs(x2))) == 2) and int(x1) + int(x2) <= max_2:
        rez.append([x1, x2])
print(len(rez), max(sum(c) for c in rez))
