def f(n):
    if n < 3:
        return 1
    if n % 2 == 0:
        return f(n // 2) + 1
    if n % 2 != 0:
        return f(n - 3) + f(n - 1)


print(f(100))