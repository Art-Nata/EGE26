count = 0
for n in range(100, 1000):

    s = str(n)
    arr = [int(x) for x in s]
    if len(set(arr)) == 3:
        a = sum(arr) - min(arr) - max(arr)
        r = str(a) + s + str(a)
        if int(r) % sum([int(x) for x in r]) == 0:
            count += 1
print(count)