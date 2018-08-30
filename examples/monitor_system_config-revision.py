#!/usr/bin/env python3

'''
Returns a list of system configuration revisions.


Method
    https://<DEVICE_IP>/api/v2/monitor/system/config-revision


CLI
    FG # exec revision list config 
    Last Firmware Version: V0.0.0-build000-REL0

    ID TIME                   ADMIN                 FIRMWARE VERSION        COMMENT
     1 2018-08-30 06:28:35    daemon_admin          V6.0.0-build131-REL0    Automatic backup (upgrade)
     2 2018-08-30 06:45:52    daemon_admin          V6.0.0-build076-REL0    Automatic backup (upgrade)


Response
    {
      "http_method": "GET",
      "results": {
        "revisions": [
          {
            "id": 1,
            "time": 1535635715,
            "version_id": "1",
            "admin": "daemon_admin",
            "comment": "Automatic backup (upgrade)"
          },
          {
            "id": 2,
            "time": 1535636752,
            "version_id": "2",
            "admin": "daemon_admin",
            "comment": "Automatic backup (upgrade)"
          }
        ],
        "categories": {
          "1": {
            "major_version": 6,
            "minor_version": 0,
            "patch_number": 0,
            "build_number": 131,
            "release_number": 0
          },
          "2": {
            "major_version": 6,
            "minor_version": 0,
            "patch_number": 0,
            "build_number": 76,
            "release_number": 0
          }
        },
        "current_config_unsaved": true
      },
      "vdom": "root",
      "path": "system",
      "name": "config-revision",
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

out = FG.monitor('system', 'config-revision')

pprint(out)

FG.logout()
