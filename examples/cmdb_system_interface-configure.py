#!/usr/bin/env python3

'''
Configure interfaces.

Method
    https://<DEVICE_IP>/api/v2/cmdb/system/interface


CLI

FG # conf sys int
FG (interface) # ed port3
FG (port3) # set ip 192.0.2.200/24
FG (port3) # set allowaccess ping
FG (port3) # end

FG # sh sys int port3
config system interface
    edit "port3"
        set vdom "root"
        set ip 192.0.2.200 255.255.255.0
        set allowaccess ping
        set type physical
        set snmp-index 3
    next
end


Response
    NA
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

interface_name = 'port3'

interface_config = {
    'name': interface_name,
    'vdom': 'root',
    "ip": "192.0.2.200 255.255.255.0",
    "allowaccess": "ping",
}

# Config
FG.set('system', 'interface', data=interface_config)

# Check
filter = 'filter=name==' + interface_name
out = FG.get('system', 'interface', parameters=filter)

pprint(out)

FG.logout()
