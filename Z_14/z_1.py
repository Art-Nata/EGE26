x = 5 ** 23 + 25 ** 12 - 10
d = []
while x > 0:
    d = [x % 5] + d
    x //= 5
print(d.count(4))