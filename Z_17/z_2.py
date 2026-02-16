a = [int(x) for x in open('17_1.txt')]
rez = []
min_x = min( x for x in a if int(x) % 2025 == 0 and x > 0)

for i in range(len(a) - 3):
    x1 = a[i]
    x2 = a[i+1]
    x3 = a[i+2]
    x4 = a[i+3]
    if x1 > 0 and x4 > 0 and abs(x2 - x3) <= min_x:
        rez.append([x1, x2, x3, x4])
print(len(rez), min(sum(c) for c in rez))