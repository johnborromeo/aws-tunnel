Automation Script for AWS Tunnel build

Pre-requisites
The following python modules would need to be installed for this script:
yaml
Template from jinja2
ConnectHandler from netmiko
Python 3.x installed
Pre-filled var_pan.yml file (This will come from the AWS configlet)
Steps - Tunnel Creation
Download/Perform a git pull on this repo
Update the var_pan.yml file with the information from AWS configlet:
tunnel1:
  tunnel_id: 10 (Tunnel interface number)
  tunnel_ip: 169.254.0.0/30 (Preconfigured Tunnel IP from configlet)
  peer_ip: 1.1.1.1 (Public IP of AWS Peer)
  tunnel_key: Testk3y1234! (Tunnel key from configlet)
  peer_as: 65123 (AWS Side Autonomous System Number)
  peer_zone: usecase1 (Name of use-case or project)

Run scripts 'asa_update.py' and 'tunn_create.py' (IP's saved on this script is relevant to the lab)

Steps - Tunnel Destroy
Using the same var_pan.yml template run the 'tunnel_decom.py'
