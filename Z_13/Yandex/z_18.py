"""Сеть задана IP-адресом 192.168.63.0 и маской сети 255.255.255.128.
Сколько в этой сети IP-адресов, для которых количество нулей в
двоичной записи IP-адреса не кратно 5?
В ответе укажите только число."""

from ipaddress import *


net = ip_network('192.168.63.0/255.255.255.128', 0)
count = 0
for ip in net:
    str_bin = ''.join(f'{int(x):08b}' for x in str(ip).split('.'))
    if str_bin.count('0') % 5 != 0:
        count += 1

print(count)