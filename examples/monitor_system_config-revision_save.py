#!/usr/bin/env python3

'''
Create a new config revision checkpoint.


Method
    https://<DEVICE_IP>/api/v2/monitor/system/config-revision/save


CLI
    NA


Response
    NA
'''

import os
import json
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

# out = FG.monitor('system', 'config-revision/save')

COMMENTS = {
    'comments': 'new config revision',
}

COMMENTS = json.dumps(COMMENTS)

# Using upload method because it's the easiest way to POST to
# /monitor using fortiosapi at the moment
FG.upload('system', 'config-revision/save', data=COMMENTS)


# Check
out = FG.monitor('system', 'config-revision')

pprint(out)

FG.logout()
