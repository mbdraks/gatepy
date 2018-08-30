#!/usr/bin/env python3

'''
List traffic statistics for IPv4 policies.

Method
    https://<DEVICE_IP>/api/v2/monitor/firewall/policy

    # PolicyID 0 means 'Implicit Deny' rule

CLI
FG # diag firewall iprope show 00100004 13
idx=13 pkts/bytes=553936822/569261079433 asic_pkts/asic_bytes=373877794/400601238192 nturbo_pkts/nturbo_bytes=236116365/236482516860 flag=0x0 hit count:12467662
    first:2018-03-21 18:40:50 last:2018-08-29 18:21:06
 established session count:1347
    first est:2018-03-21 18:40:50 last est:2018-08-29 18:21:05


Response FGVM
    {
      "http_method":"GET",
      "results":[
        {
          "policyid":0,
          "active_sessions":0,
          "bytes":0,
          "packets":0
        },
        {
          "policyid":1,
          "uuid":"bfa5cd8e-aba3-51e8-567b-302f11df04b7",
          "active_sessions":0,
          "bytes":0,
          "packets":0
        },
        {
          "policyid":66,
          "uuid":"88c14218-abbb-51e8-4fb5-4edfbd13d043",
          "active_sessions":0,
          "bytes":0,
          "packets":0
        },
        {
          "policyid":3,
          "uuid":"e8047652-abbe-51e8-0273-ef4a243c29c5",
          "active_sessions":0,
          "bytes":0,
          "packets":0
        }
      ],
      "vdom":"root",
      "path":"firewall",
      "name":"policy",
      "status":"success",
      "serial":"FGVM020000000000",
      "version":"v6.0.0",
      "build":76
    }


Response FG-81E
    {
      "http_method":"GET",
      "results":[
        {
          "policyid":0,
          "active_sessions":0,
          "bytes":536085,
          "packets":8397,
          "software_bytes":536085,
          "software_packets":8397,
          "asic_bytes":0,
          "asic_packets":0,
          "nturbo_bytes":0,
          "nturbo_packets":0,
          "last_used":1535478216,
          "first_used":1521670953,
          "hit_count":10770
        },
        {
          "policyid":1,
          "uuid":"bdd7cf24-f7fe-51e7-de6c-f42e21b200d1",
          "active_sessions":0,
          "bytes":0,
          "packets":0,
          "software_bytes":0,
          "software_packets":0,
          "asic_bytes":0,
          "asic_packets":0,
          "nturbo_bytes":0,
          "nturbo_packets":0
        },
        {
          "policyid":13,
          "uuid":"d61723ce-2c41-51e8-214e-3ca194c65c79",
          "active_sessions":2056,
          "bytes":569238562854,
          "packets":553910965,
          "software_bytes":168657862523,
          "software_packets":180048782,
          "asic_bytes":164098194283,
          "asic_packets":137745885,
          "nturbo_bytes":236482506048,
          "nturbo_packets":236116298,
          "last_used":1535577206,
          "first_used":1521668450,
          "hit_count":12463107,
          "session_last_used":1535577206,
          "session_first_used":1521668450,
          "session_count":2043
        }
      ],
      "vdom":"root",
      "path":"firewall",
      "name":"policy",
      "status":"success",
      "serial":"FG81EP0000000000",
      "version":"v6.0.2",
      "build":163
    }
'''

from fortiosapi import FortiOSAPI
from pprint import pprint
import time

fgt = FortiOSAPI()

device = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
}

fgt.login(**device)

out = fgt.monitor('firewall', 'policy')

for policy in out['results']:
    policyid = str(policy['policyid'])
    if 'last_used' not in policy:
        print('Policy ID {:10} {:^38}'.format(policyid, '** Never Used **'))
    else:
        policy_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(policy['last_used']))
        print('Policy ID {:10} Last Used on: {} GMT'.format(policyid, policy_time))

fgt.logout()
