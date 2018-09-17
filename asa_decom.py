import yaml
from jinja2 import Template
from netmiko import ConnectHandler
from pprint import pprint

un = input('Enter your TACACS username: ', )
pw = input('Enter your TACACS password: ', )

asa = {
    'device_type': 'cisco_asa',
    'ip': '10.1.238.81',
    'username': un,
    'password': pw,
    'secret': pw,
    'port': 22,
    'verbose': True
}

with open('asa-decom.j2') as file_:
    read_build = Template(file_.read())
with open('/Users/jborromeo/Desktop/aws_tunnel/var_pan.yaml') as file_:
    values = yaml.load(file_.read())

output = ("{}".format(read_build.render(values))).splitlines()
pprint(output)
print(type(output))

net_connect = ConnectHandler(**asa)
net_connect.send_config_set(output)
net_connect.disconnect()