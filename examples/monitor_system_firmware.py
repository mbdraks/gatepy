#!/usr/bin/env python3

'''
Retrieve a list of firmware images available to use for upgrade on this device.

Method
  https://<DEVICE_IP>/api/v2/monitor/system/firmware


CLI
  FG # diag fdsm image-list
  Last update: 0 secs ago.

  06000000FIMG0012000002  v6.0 GA P2 b0163 (upgrade)
  06000000FIMG0012000001  v6.0 GA P1 b0131 (upgrade)
  05006000FIMG0012006005  v5.6 GA P5 b1600 (downgrade)
  05006000FIMG0012006004  v5.6 GA P4 b1575 (downgrade)
  05006000FIMG0012006003  v5.6 GA P3 b1547 (downgrade)
  05006000FIMG0012006002  v5.6 GA P2 b1486 (downgrade)


JSON
  {
    "http_method":"GET",
    "results":{
      "current":{
        "name":"FortiOS",
        "id":"current",
        "version":"v6.0.0",
        "major":6,
        "minor":0,
        "patch":0,
        "build":76,
        "branch-point":76,
        "release-type":"GA",
        "notes":"http:\/\/docs.fortinet.com\/d\/fortios-6.0.0-release-notes\/download",
        "source":"current",
        "platform-id":"FGVM64"
      },
      "available":[
        {
          "name":"FortiOS",
          "id":"06000000FIMG0012000002",
          "version":"v6.0.2",
          "major":6,
          "minor":0,
          "patch":2,
          "build":163,
          "branch-point":163,
          "release-type":"GA",
          "notes":"http:\/\/docs.fortinet.com\/d\/fortios-6.0.2-release-notes\/download",
          "source":"fortiguard"
        },
        ...,
        {
          "name":"FortiOS",
          "id":"05006000FIMG0012006002",
          "version":"v5.6.2",
          "major":5,
          "minor":6,
          "patch":2,
          "build":1486,
          "branch-point":1486,
          "release-type":"GA",
          "notes":"http:\/\/docs.fortinet.com\/d\/fortios-5.6.2-release-notes\/download",
          "source":"fortiguard"
        }
      ]
    },
    "vdom":"root",
    "path":"system",
    "name":"firmware",
    "status":"success",
    "serial":"FGVM020000000000",
    "version":"v6.0.0",
    "build":76
  }

'''

import os
from pprint import pprint
from fortiosapi import FortiOSAPI


fgt = FortiOSAPI()

# Source _host
FG_HOST = os.environ['FG_HOST']
FG_USER = os.environ['FG_USER']
FG_PASS = os.environ['FG_PASS']

DEVICE = {
    'host': FG_HOST,
    'username': FG_USER,
    'password': FG_PASS,
}

fgt.login(**DEVICE)

out = fgt.monitor('system', 'firmware')

pprint(out)

fgt.logout()
