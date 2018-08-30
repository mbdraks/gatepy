#!/usr/bin/env python3

'''
Configure interfaces.

Method
    https://<DEVICE_IP>/api/v2/cmdb/system/interface?action=schema


CLI
    FG # sh sys int port1
    config system interface
        edit "port1"
            set vdom "root"
            set ip 192.168.0.1 255.255.255.0
            set allowaccess ping https ssh http fgfm
            set type physical
            set snmp-index 1
        next
    end


Response
    NA
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


schema = 'action=schema'

out = fgt.get('system', 'interface', parameters=schema)

interface_table = out['results']['children']

for field, value in interface_table.items():
    if value.get('required'):
        print()
        print(field, value)

fgt.logout()
