#!/usr/bin/env python3

'''
Retrieve a list of supported firmware upgrade paths.

Method
    https://<DEVICE_IP>/api/v2/monitor/system/firmware/upgrade-paths/


CLI
    NA


Response
    {
      "http_method": "GET",
      "results": [
        {
          "from": {
            "major": 6,
            "minor": 0,
            "patch": 1,
            "build": 131
          },
          "to": {
            "major": 6,
            "minor": 0,
            "patch": 2,
            "build": 163
          }
        },
        ...
        {
          "from": {
            "major": 5,
            "minor": 2,
            "patch": 12,
            "build": 760
          },
          "to": {
            "major": 5,
            "minor": 4,
            "patch": 9,
            "build": 1202
          }
        }
      ],
      "vdom": "root",
      "path": "system",
      "name": "firmware",
      "action": "upgrade-paths",
      "status": "success",
      "serial": "FGVM020000000000",
      "version": "v6.0.0",
      "build": 76
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

out = FG.monitor('system', 'firmware/upgrade-paths')

pprint(out)

FG.logout()
