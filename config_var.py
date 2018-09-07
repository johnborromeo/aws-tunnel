from pprint import pprint
import re


file1 = open('pan_configlet.txt').read()
# pprint(file1)
# print(type(file1))

# x = (input('Enter Tunnel ID: '))
# print(x)
# y = (input('Enter use-case name: '))

tunnel_list = []
m = re.search('pre-shared-key key (.+)', file1)
pprint(m.group(1))

# tunnel1:
#   tunnel_id: x
#   tunnel_ip: 169.254.0.0/30
#   peer_ip: 1.1.1.1
#   tunnel_key: Testk3y1234!
#   peer_as: 65123
#   peer_zone: usecase1
#
# tunnel2:
#   tunnel_id: 20
#   tunnel_ip: 169.254.1.0/30
#   peer_ip: 1.2.1.1
#   tunnel_key: Testk3y1234!
#   peer_as: 65234
#   peer_zone: usecase1

# m = re.search('pre-shared-key key(?P<tunnel_key>.+)', file1)
# pprint(m.group('tunnel_list'))

m = re.search('pre-shared-key key (?P<tunnel_key>.+)', file1)
pprint(m.group('tunnel_key'))