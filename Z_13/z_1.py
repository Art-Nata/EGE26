print(187 & 240)

x1 = f'{187:b}'
x2 = f'{240:b}'

print(x1)
print(x2)
s = ''
for i in range(len(x1)):
    if x1[i] == '1' and x2[i] == '1':
        s += '1'
    else:
        s += '0'
print(int(s, 2))