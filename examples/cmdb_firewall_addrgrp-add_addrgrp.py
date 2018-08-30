#!/usr/bin/env python3

'''
Configure IPv4 address groups.

Method
  https://<DEVICE_IP>/api/v2/cmdb/firewall/addrgrp


CLI
    FG # sh firewall addrgrp
    config firewall addrgrp
        edit "add_grp_example"
            set uuid 1802a868-abee-51e8-fb7b-cde25eb10edd
            set member "example_host" "test_net_2"
        next
    end


Response
{
  "http_method": "GET",
  "revision": "5.0.94.9539865665020678008.1535505187",
  "results": [
    {
      "q_origin_key": "add_grp_example",
      "name": "add_grp_example",
      "uuid": "1802a868-abee-51e8-fb7b-cde25eb10edd",
      "member": [
        {
          "q_origin_key": "example_host",
          "name": "example_host"
        },
        {
          "q_origin_key": "test_net_2",
          "name": "test_net_2"
        }
      ],
      "comment": "",
      "visibility": "enable",
      "color": 0,
      "tagging": [],
      "allow-routing": "disable"
    }
  ],
  "vdom": "root",
  "path": "firewall",
  "name": "addrgrp",
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

out = fgt.get('firewall', 'addrgrp')



address_group = {
    "name": "test_group_1",
    "member": [
        {"name": "test_net_1"},
        {"name": "test_net_2"},
    ]
}

# Config address
fgt.set('firewall', 'addrgrp', data=address_group)

# Check
out = fgt.get('firewall', 'addrgrp')

pprint(out)

fgt.logout()
