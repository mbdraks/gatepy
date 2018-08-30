#!/usr/bin/env python3

'''
Restore system configuration from uploaded file or from USB.

Method
    https://<DEVICE_IP>/api/v2/monitor/system/config/restore


CLI
    NA


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


filename = 'fg_backup.txt'
f = open(filename)

data = {
    'source': 'upload',
    'scope': 'global',
}

backup_file = {'file': (filename, f, 'text/plain')}

FG.upload('system', 'config/restore', data=data, files=backup_file)

# Will reboot automatically after POST