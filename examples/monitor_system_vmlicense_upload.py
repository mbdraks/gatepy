#!/usr/bin/env python3

'''
Update VM license using uploaded file. Reboots immediately if successful.

Method
    https://<DEVICE_IP>/api/v2/monitor/system/vmlicense/upload/


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

FG._https = False   # Connect using http before license is applied 
FG.login(**DEVICE)


filename = 'license.lic'
f = open(filename)

data = {
    'source': 'upload',
    'scope': 'global',
}

license_file = {'file': (filename, f, 'text/plain')}

FG.upload('system', 'vmlicense/upload', data=data, files=license_file)

# Will reboot automatically after POST