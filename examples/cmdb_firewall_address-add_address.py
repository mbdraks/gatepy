#!/usr/bin/env python3

'''
Configure IPv4 addresses.

Method
  https://<DEVICE_IP>/api/v2/cmdb/firewall/address


CLI
    FG # sh firewall address example_host 
    config firewall address
        edit "example_host"
            set uuid 39673efe-abeb-51e8-a8da-d9052c368d9f
            set subnet 192.0.2.1 255.255.255.255
        next
    end


Response
{
  "http_method": "GET",
  "revision": "31.0.92.9539865665020678008.1535505187",
  "results": [
    {
      "q_origin_key": "example_host",
      "name": "example_host",
      "uuid": "39673efe-abeb-51e8-a8da-d9052c368d9f",
      "subnet": "192.0.2.1 255.255.255.255",
      "type": "ipmask",
      "start-ip": "192.0.2.1",
      "end-ip": "255.255.255.255",
      "fqdn": "",
      "country": "",
      "wildcard-fqdn": "",
      "cache-ttl": 0,
      "wildcard": "192.0.2.1 255.255.255.255",
      "sdn": "",
      "tenant": "",
      "organization": "",
      "epg-name": "",
      "subnet-name": "",
      "sdn-tag": "",
      "policy-group": "",
      "comment": "",
      "visibility": "enable",
      "associated-interface": "",
      "color": 0,
      "filter": "",
      "obj-id": 0,
      "list": [],
      "tagging": [],
      "allow-routing": "disable"
    }
  ],
  "vdom": "root",
  "path": "firewall",
  "name": "address",
  "status": "success",
  "http_status": 200,
  "serial": "FGVM020000000000",
  "version": "v6.0.0",
  "build": 76
}
'''

from fortiosapi import FortiOSAPI
from pprint import pprint

fgt = FortiOSAPI()

device = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
}

fgt.login(**device)


address = {
    "name": "test_net_2",
    "subnet": "198.51.100.0 255.255.255.0"
}

# Config address
fgt.set('firewall', 'address', data=address)

# Check
out = fgt.get('firewall', 'address')

# Print all address names
for address in out['results']:
  print(address['name'])

fgt.logout()
