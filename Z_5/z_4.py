for n in range(100000, 1000000):
    s = str(n)
    arr = [int(x) for x in s]
    if len(set(arr)) == 6:
        k = (arr[1] + arr[3] + arr[5]) ** 2
        l = sum([x ** 2 for x in arr if x in[2, 3, 5, 7]])
        r = abs(k - l)
        if r == 407:
            print(n, arr)
