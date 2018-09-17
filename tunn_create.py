import yaml
from jinja2 import Template
from netmiko import ConnectHandler
from pprint import pprint

un = input('Enter your TACACS username: ', )
pw = input('Enter your TACACS password: ', )


#Research on getpass for pw handling... 'from getpass import getpass'
pan = {
    'device_type' : 'paloalto_panos',
    'ip':   '10.11.77.152',
    'username': 'admin',
    'password': 'Sfdc1853!',
    'verbose': True
}


########Verification###########
# read_build = open('build.j2').read().splitlines()
# pprint(read_build)
# print(type(read_build))
########Verification###########


########Open and Merge Jinja-yaml###########
with open('build.j2') as file_:
    read_build = Template(file_.read())
with open('/Users/jborromeo/Desktop/aws_tunnel/var_pan.yaml') as file_:
    values = yaml.load(file_.read())
########Open and Merge Jinja-yaml###########


output = ("{}".format(read_build.render(values))).splitlines()
pprint(output)
print(type(output))


net_connect = ConnectHandler(**pan)
net_connect.send_config_set(output)
net_connect.disconnect()

########################ASA UPDATE###########################

asa = {
    'device_type': 'cisco_asa',
    'ip': '10.1.238.81',
    'username': un,
    'password': pw,
    'secret': pw,
    'port': 22,
    'verbose': True
}

with open('asa-jinja.j2') as file_:
    read_build = Template(file_.read())
with open('/Users/jborromeo/Desktop/aws_tunnel/var_pan.yaml') as file_:
    values = yaml.load(file_.read())

output = ("{}".format(read_build.render(values))).splitlines()
pprint(output)
print(type(output))

net_connect = ConnectHandler(**asa)
net_connect.send_config_set(output)
net_connect.disconnect()

