x = 2 ** 2048 + 32 ** 102 - 8 * 4 ** 128
d = []
while x > 0:
    d = [x % 32] + d
    x //= 32
print(d)
print(len([a for a in d if a > 9]))