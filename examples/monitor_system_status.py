#!/usr/bin/env python3

'''
Retrieve basic system status.

Method
    https://<DEVICE_IP>/api/v2/monitor/system/status

CLI
    NA

JSON
    {
    "http_method":"GET",
    "results":{
    },
    "vdom":"root",
    "path":"system",
    "name":"status",
    "status":"success",
    "serial":"FGVM020000000000",
    "version":"v6.0.0",
    "build":76
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

out = FG.monitor('system', 'status')

pprint(out)

FG.logout()
