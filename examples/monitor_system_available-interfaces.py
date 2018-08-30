#!/usr/bin/env python3

'''
Retrieve a list of all interfaces along with some meta information regarding their availability.


Method
    https://<DEVICE_IP>/api/v2/monitor/system/available-interfaces


CLI

    FG # sh sys int ?
    name    Name.
    port1   static   0.0.0.0 0.0.0.0  192.168.0.1 255.255.255.0  up   disable   physical  disable   enable   
    port2   static   0.0.0.0 0.0.0.0  1.1.1.1 255.255.255.0  up   disable   physical  disable   enable   
    port3   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port4   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port5   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port6   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port7   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port8   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port9   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    port10   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   physical  disable   enable   
    ssl.root   static   0.0.0.0 0.0.0.0  0.0.0.0 0.0.0.0  up   disable   tunnel  disable   enable   


Response
    {
      "http_method": "GET",
      "results": [
        {
          "name": "any",
          "valid_in_policy": true,
          "icon": "fa-square-o"
        },
        {
          "name": "port1",
          "vdom": "root",
          "is_system_interface": true,
          "status": "up",
          "dhcp4_client_count": 0,
          "dhcp6_client_count": 0,
          "role": "undefined",
          "ipv4_addresses": [
            {
              "ip": "192.168.0.1",
              "netmask": "255.255.255.0",
              "cidr_netmask": 24
            }
          ],
          "mac_address": "00:50:56:01:68:fc",
          "link": "up",
          "duplex": "full",
          "speed": 1000,
          "supports_device_id": true,
          "valid_in_policy": true,
          "supports_fortitelemetry": true,
          "is_used": false,
          "is_physical": true,
          "media": "rj45",
          "managed_devices": [],
          "is_ipsecable": true,
          "is_routable": true,
          "tagging": [],
          "type": "physical",
          "icon": "ftnt-interface-rj45-up"
        },
        {
          "name": "port2",
          "vdom": "root",
          "is_system_interface": true,
          "status": "up",
          "dhcp4_client_count": 0,
          "dhcp6_client_count": 0,
          "role": "undefined",
          "ipv4_addresses": [
            {
              "ip": "1.1.1.1",
              "netmask": "255.255.255.0",
              "cidr_netmask": 24
            }
          ],
          "mac_address": "00:50:56:01:68:fd",
          "link": "up",
          "duplex": "full",
          "speed": 1000,
          "supports_device_id": true,
          "valid_in_policy": true,
          "supports_fortitelemetry": true,
          "is_used": false,
          "is_physical": true,
          "media": "rj45",
          "managed_devices": [],
          "is_ipsecable": true,
          "is_routable": true,
          "tagging": [],
          "type": "physical",
          "icon": "ftnt-interface-rj45-up"
        },
        {
          "name": "ssl.root",
          "vdom": "root",
          "is_system_interface": true,
          "status": "up",
          "alias": "SSL VPN interface",
          "role": "undefined",
          "mac_address": "00:00:00:00:00:00",
          "supports_fortitelemetry": true,
          "is_used": false,
          "is_sslvpn": true,
          "managed_devices": [],
          "tagging": [],
          "type": "tunnel",
          "icon": "ftnt-vpn-tunnel-up"
        },
        {
          "name": "virtual-wan-link",
          "is_virtual_wan_link": true,
          "status": "down",
          "role": "wan",
          "type": "virtual-wan",
          "load_balance_mode": "source-ip-based",
          "members": [],
          "icon": "ftnt-virtual-wan-link-down-disabled",
          "link": "down"
        }
      ],
      "vdom": "root",
      "path": "system",
      "name": "available-interfaces",
      "status": "success",
      "serial": "FGVM020000000000",
      "version": "v6.0.1",
      "build": 131
    }
'''

import os
from pprint import pprint
from fortiosapi import FortiOSAPI

FG = FortiOSAPI()

# Source _host
FG_HOST = os.environ['FG_HOST']
FG_USER = os.environ['FG_USER']
FG_PASS = os.environ['FG_PASS']

DEVICE = {
    'host': FG_HOST,
    'username': FG_USER,
    'password': FG_PASS,
}

FG.login(**DEVICE)

out = FG.monitor('system', 'available-interfaces')

pprint(out)

FG.logout()
