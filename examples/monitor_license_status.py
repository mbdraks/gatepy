#!/usr/bin/env python3

'''
Get current license & registration status.

Method
  https://<DEVICE_IP>/api/v2/monitor/license/status


CLI
  NA

JSON
  NA

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

out = fgt.monitor('license', 'status')

pprint(out)

fgt.logout()
