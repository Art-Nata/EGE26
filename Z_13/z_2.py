ip_1 = '231.32.255.131'
ip_m = '255.255.240.0'
ip_s = '231.32.240.0'

s1 = '.'.join([f'{int(x):08b}' for x in ip_1.split('.')])
s2 = [f'{int(x):08b}' for x in ip_m.split('.')]
s3 = [f'{int(x):08b}' for x in ip_s.split('.')]
print(s1)
print(s2)
print(s3)