min1 = float('inf')
r = []
for n in range(1, 100):
    n_bin = bin(n)[2:]
    if n % 2 == 0:
        result = '1' + n_bin + '0'
    else:
        result = '11' + n_bin + '11'
    result_int = int(result, 2)
    if result_int > 255:
 #       min = result
 #       print(result)
        print(n, result, result_int)
        r.append(result_int)
print(min(r))
