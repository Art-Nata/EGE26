from ipaddress import *


net = ip_network('191.128.66.83/255.192.0.0', 0)
ip_comp = ip_address('191.45.234.89')
#for ip in net.hosts():
#    print(ip)
#print(net.num_addresses)
#print(net.netmask)
print(max(net.hosts()))
