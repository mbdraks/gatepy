#!/usr/bin/env python3

'''
Performs a policy lookup by creating a dummy packet and asking the kernel which policy would be hit.


Method
    https://<DEVICE_IP>/api/v2/monitor/firewall/policy-lookup?srcintf=port2&sourceip=1.1.1.1&protocol=6&dest=10.0.0.10&destport=80


CLI
    NA


Response
    {
      "http_method": "GET",
      "results": {
        "destip": "10.0.0.10",
        "policy_id": 2,           # policy_id 0 here means implicit deny
        "success": true
      },
      "vdom": "root",
      "path": "firewall",
      "name": "policy-lookup",
      "status": "success",
      "serial": "FGVM040000141945",
      "version": "v6.0.2",
      "build": 163
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

# Protocol Numbers
# https://www.iana.org/assignments/protocol-numbers/protocol-numbers.txt

param = {
    'srcintf': 'port2',
    'sourceip': '1.1.1.1',
    'protocol': '6',
    'dest': '10.0.0.10',
    'destport': 80,
}

out = FG.monitor('firewall', 'policy-lookup', parameters=param)

pprint(out)

FG.logout()
