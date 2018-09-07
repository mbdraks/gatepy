#!/usr/bin/env python3

'''
Upgrade firmware image on this device using uploaded file.

Method
    https://<DEVICE_IP>/api/v2/monitor/system/firmware/upgrade/


CLI
    NA


Debug
    FG # diag debug ena
    FG # d de app httpsd -1

    [httpsd 179 - 1536284801     info] ap_invoke_handler[593] -- new request (handler='api_monitor_v2-handler', uri='/api/v2/monitor/system/firmware/upgrade', method='POST')
    [httpsd 179 - 1536284801     info] ap_invoke_handler[597] -- User-Agent: python-requests/2.19.1
    [httpsd 179 - 1536284801     info] ap_invoke_handler[600] -- Source: 192.168.0.120:62279 Destination: 192.168.0.30:443
    [httpsd 179 - 1536284801     info] endpoint_handle_req[616] -- received api_monitor_v2_request from '192.168.0.120'
    [httpsd 179 - 1536284801     info] aps_init_process_vdom[1195] -- initialized process vdom to 'root' (cookie='(null)')
    [httpsd 179 - 1536284825     info] api_store_parameter[227] -- add API parameter 'source': '"upload"' (type=string)
    [httpsd 179 - 1536284825     info] api_store_parameter[227] -- add API parameter 'scope': '"global"' (type=string)
    [httpsd 179 - 1536284825     info] api_store_parameter[227] -- add API parameter 'file': '"FGT_VM64-v6-build0163-FORTINET.out"' (type=string)
    [httpsd 179 - 1536284825     info] api_store_parameter[227] -- add API parameter 'source': '"upload"' (type=string)
    [httpsd 179 - 1536284825     info] api_store_parameter[227] -- add API parameter 'scope': '"global"' (type=string)
    [httpsd 179 - 1536284825     info] api_store_parameter[227] -- add API parameter 'file': '"FGT_VM64-v6-build0163-FORTINET.out"' (type=string)
    [httpsd 179 - 1536284825     info] endpoint_process_req_vdom[457] -- new API request (action='upgrade',path='system',name='firmware',vdom='root',user='admin')
    [httpsd 179 - 1536284825     info] system_firmware_upgrade[1662] -- upgrade attempt for '/tmp/upfile'
    [httpsd 179 - 1536284825    error] system_firmware_upgrade[1666] -- upgrade initiated for '/tmp/upfile'
    [httpsd 179 - 1536284826     info] system_firmware_upgrade[1673] -- upgrade success for '/tmp/upfile'
    [httpsd 179 - 1536284826     info] ap_invoke_handler[616] -- request completed (handler='api_monitor_v2-handler' result==0)
    [httpsd 140 - 1536284829    error] log_error_core[439] -- [Fri Sep  7 01:47:09 2018] [notice] caught SIGTERM, shutting down
'''

import os
import base64
import json
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

filename = 'FGT_VM64-v6-build0163-FORTINET.out'
f = open(filename, 'rb')
firmware_file = {'file': (filename, f, 'text/plain')}

data = {
    'source': 'upload',
    'scope': 'global',
}

FG.upload('system', 'firmware/upgrade', data=data, files=firmware_file)

# Will reboot automatically after POST
