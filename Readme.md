# **Automation Script for AWS Tunnel build**
**Pre-requisites**
1. The following python modules would need to be installed for this script:
   - yaml
   - Template from jinja2
   - ConnectHandler from netmiko
2. Python 3.x installed
3. Pre-filled var_pan.yml file (This will come from the AWS configlet)

**Steps - Tunnel Creation**
1. Download/Perform a git pull on this repo
2. Update the var_pan.yml file with the information from AWS configlet:

- tunnel1:
  - tunnel_id     : 10 (Tunnel interface number)
  - tunnel_ip     : 169.254.0.0/30 (Preconfigured Tunnel IP from configlet)
  - peer_ip       : 1.1.1.1 (Public IP of AWS Peer)
  - tunnel_key    : Testk3y1234! (Tunnel key from configlet)
  - peer_as       : 65123 (AWS Side Autonomous System Number)
  - peer_zone     : usecase1 (Name of use-case or project)

3. Run scripts 'tunn_create.py' (IP's saved on this script is relevant to the lab)

**Steps - Tunnel Destroy**
1. Make sure the accurate var_pan.yml file is saved on your variable file location. If you wish to rename the file in the case of multiple files, the var file on the .py script needs to be updated as well.
2. Run the 'tunnel_decom.py' script using the variable file on step one.

## In-progress enhancements
1. Merge ASA and PAN script in one  file. (DONE)
2. Password handling improvement. (DONE)
3. Configlet automatic file parsing for var template. (In-Progress....)
4. M&A Tunnel builds script
## NOTE: username/password would need to be updated before running the script - creadentials have been ommitted since this git resource is public.
