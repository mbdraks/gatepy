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

from fortiosapi import FortiOSAPI
from pprint import pprint

fgt = FortiOSAPI()

device = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
}

fgt.login(**device)

out = fgt.monitor('system', 'status')

pprint(out)