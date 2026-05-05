"""Два узла, находящиеся в одной сети, имеют IP-адреса
 121.171.5.70 и 121.171.5.107. Укажите наименьшее возможное
 количество адресов в этой сети."""


from ipaddress import *


for i in range(32):
    net = ip_network(f'121.171.5.70/{i}', 0)
    if ip_address('121.171.5.107') in net:
        print(net, net.num_addresses)