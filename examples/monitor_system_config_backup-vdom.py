#!/usr/bin/env python3

'''
Backup system config for a specific VDOM

Method
    https://<DEVICE_IP>/api/v2/monitor/system/config/backup?scope=vdom&vdom=vd01


CLI
    FG # conf vd
    FG (vdom) # ed vd01
    current vf=vd01:3

    FG (vd01) # sh full-configuration 
    config wireless-controller hotspot20 anqp-venue-name
    end
    ...

Response
    Object
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

param = {
    'scope': 'vdom',
    'vdom': 'vd01',
}

out = FG.download('system', 'config/backup', parameters=param)

with open("fg_backup_vdom.txt", "w") as f:
    f.write(out.text)

FG.logout()
