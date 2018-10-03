#!/usr/bin/env python3

'''
Configure local users.

Method
    https://<DEVICE_IP>/api/v2/cmdb/user/local


CLI
    FG # sh user local
    config user local
        edit "user1"
            set type password
            set passwd-time 2018-08-31 06:19:37
            set passwd ENC xxx
        next
    end


Response
    {
      "http_method": "GET",
      "revision": "3.0.0.9539865665020678008.1535658219",
      "results": [
        {
          "q_origin_key": "user1",
          "name": "user1",
          "id": 2164260865,
          "status": "enable",
          "type": "password",
          "passwd": "ENC XXXX",
          "ldap-server": "",
          "radius-server": "",
          "tacacs+-server": "",
          "two-factor": "disable",
          "fortitoken": "",
          "email-to": "",
          "sms-server": "fortiguard",
          "sms-custom-server": "",
          "sms-phone": "",
          "passwd-policy": "",
          "passwd-time": "2018-08-31 06:11:22",
          "authtimeout": 0,
          "workstation": "",
          "auth-concurrent-override": "disable",
          "auth-concurrent-value": 0,
          "ppk-secret": "",
          "ppk-identity": ""
        }
      ],
      "vdom": "root",
      "path": "user",
      "name": "local",
      "status": "success",
      "http_status": 200,
      "serial": "FGVM020000119895",
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

out = FG.get('user', 'local')

pprint(out)

FG.logout()
