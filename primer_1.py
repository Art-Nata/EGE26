
a, b = abs(int(input())), abs(int(input()))
while a != 0 and b != 0:
    if a > b:
        a, b = b, a % b
    else:
        a, b = b, b % a
print(a)
