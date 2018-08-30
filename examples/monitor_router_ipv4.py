#!/usr/bin/env python3

'''
List all active IPv4 routing table entries

Method
  https://<DEVICE_IP>/api/v2/monitor/router/ipv4

CLI
    FG # get router info routing-table all

    Routing table for VRF=0
    Codes: K - kernel, C - connected, S - static, R - RIP, B - BGP
           O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2
           i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
           * - candidate default

    S*      0.0.0.0/0 [10/0] via 192.168.0.254, port1
    C       1.1.1.0/24 is directly connected, port2
    S       10.0.0.0/8 [10/0] via 192.168.0.254, port1
    C       192.168.0.0/24 is directly connected, port1


Response
    {
      "http_method":"GET",
      "results":[
        {
          "ip_version":4,
          "type":"static",
          "ip_mask":"0.0.0.0\/0",
          "distance":10,
          "metric":0,
          "gateway":"192.168.0.254",
          "interface":"port1"
        },
        {
          "ip_version":4,
          "type":"connect",
          "ip_mask":"1.1.1.0\/24",
          "distance":0,
          "metric":0,
          "gateway":"0.0.0.0",
          "interface":"port2"
        },
        {
          "ip_version":4,
          "type":"static",
          "ip_mask":"10.0.0.0\/8",
          "distance":10,
          "metric":0,
          "gateway":"192.168.0.254",
          "interface":"port1"
        },
        {
          "ip_version":4,
          "type":"connect",
          "ip_mask":"192.168.0.0\/24",
          "distance":0,
          "metric":0,
          "gateway":"0.0.0.0",
          "interface":"port1"
        }
      ],
      "vdom":"root",
      "path":"router",
      "name":"ipv4",
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

out = fgt.monitor('router', 'ipv4')

pprint(out)

fgt.logout()
