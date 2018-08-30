#!/usr/bin/env python3

'''
Retrieve information on state of log devices.


Method
    https://<DEVICE_IP>/api/v2/monitor/log/device/state


CLI
    NA


Response
    {
      "http_method": "GET",
      "results": {
        "memory": {
          "is_available": true,
          "is_enabled": false,
          "is_default": false,
          "is_ha_supported": true
        },
        "disk": {
          "is_available": true,
          "is_enabled": true,
          "is_loggable": true,
          "num_ssds_available": 1,
          "is_fortiview_supported": true,
          "disabled_by_default": false,
          "is_ha_supported": true
        },
        "fortianalyzer": {
          "is_available": true,
          "is_enabled": false
        },
        "forticloud": {
          "is_available": false,
          "is_enabled": false
        }
      },
      "vdom": "root",
      "path": "log",
      "name": "device",
      "action": "state",
      "status": "success",
      "serial": "FGVM020000000000",
      "version": "v6.0.1",
      "build": 131
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

out = FG.monitor('log', 'device/state')

pprint(out)

FG.logout()
