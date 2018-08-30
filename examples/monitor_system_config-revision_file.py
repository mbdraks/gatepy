#!/usr/bin/env python3

'''
Download a specific configuration revision.


Method
    https://<DEVICE_IP>/api/v2/monitor/system/config-revision/file?config_id=1


CLI
    NA


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
    'config_id': 1,
}

out = FG.download('system', 'config-revision/file', parameters=param)

with open("fg_revision.txt", "w") as f:
    f.write(out.text)

pprint(out)

FG.logout()
