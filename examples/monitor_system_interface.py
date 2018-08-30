#!/usr/bin/env python3

'''
Retrieve statistics for all system interfaces.

At FOS 6.0.2 this was not reporting all interfaces, alternatively 
use monitor/system/available-interfaces

Method
    https://<DEVICE_IP>/api/v2/monitor/system/interface


CLI
    NA


Response
    {
      "http_method": "GET",
      "revision": "1535638688.393018",
      "results": {
        "wan1": {
          "id": "wan1",
          "name": "wan1",
          "alias": "",
          "mac": "00:00:00:00:00:00",
          "ip": "189.120.3.56",
          "mask": 22,
          "link": true,
          "speed": 1000,
          "duplex": 1,
          "tx_packets": 26191632,
          "rx_packets": 39051742,
          "tx_bytes": 16913986143,
          "rx_bytes": 42061215535,
          "tx_errors": 0,
          "rx_errors": 0
        },
        ...
        
        "nyarlathotep": {
          "id": "nyarlathotep",
          "name": "nyarlathotep",
          "alias": "",
          "mac": "00:00:00:00:00:00",
          "ip": "192.168.10.1",
          "mask": 24,
          "link": true,
          "speed": 0,
          "duplex": 0,
          "tx_packets": 7326324,
          "rx_packets": 6027,
          "tx_bytes": 4140970457,
          "rx_bytes": 259836,
          "tx_errors": 0,
          "rx_errors": 0
        },
        "mesh": {
          "id": "mesh",
          "name": "mesh",
          "alias": "",
          "mac": "00:00:00:00:00:00",
          "ip": "0.0.0.0",
          "mask": 0,
          "link": true,
          "speed": 0,
          "duplex": 0,
          "tx_packets": 0,
          "rx_packets": 0,
          "tx_bytes": 0,
          "rx_bytes": 0,
          "tx_errors": 0,
          "rx_errors": 0
        }
      },
      "vdom": "root",
      "path": "system",
      "name": "interface",
      "status": "success",
      "serial": "FG81EP4Q17002868",
      "version": "v6.0.2",
      "build": 163
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

out = FG.monitor('system', 'interface')

pprint(out)

FG.logout()
