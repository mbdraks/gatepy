#!/usr/bin/env python3

'''
Configure global attributes.


Method
    https://<DEVICE_IP>/api/v2/cmdb/system/global


CLI
    FG # sh sys gl
    config system global
        set alias "FG"
        set hostname "FG"
        set timezone 04
    end


Response
    NA
'''

import os
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


global_config = {
    'hostname': 'FG_new',
    'timezone': "18",
    'gui-theme': 'melongene'
}

# Config
FG.set('system', 'global', data=global_config)

# Check
out = FG.get('system', 'global')

get_hostname = out['results']['hostname']
get_timezone = out['results']['timezone']
get_gui_theme = out['results']['gui-theme']

print()
print('{:13}{}'.format('Hostname:', get_hostname))
print('{:13}{}'.format('Time Zone:', get_timezone))
print('{:13}{}'.format('GUI Theme:', get_gui_theme))
print()

FG.logout()
