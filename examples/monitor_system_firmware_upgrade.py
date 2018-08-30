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

    [httpsd 181 - 1535636630     info] ap_invoke_handler[593] -- new request (handler='api_monitor_v2-handler', uri='/api/v2/monitor/system/firmware/upgrade', method='POST')
    [httpsd 181 - 1535636630     info] ap_invoke_handler[597] -- User-Agent: python-requests/2.19.1
    [httpsd 181 - 1535636630     info] ap_invoke_handler[600] -- Source: 172.30.248.57:53110 Destination: 192.168.0.1:443
    [httpsd 181 - 1535636630     info] endpoint_handle_req[594] -- received api_monitor_v2_request from '172.30.248.57'
    [httpsd 181 - 1535636630     info] aps_init_process_vdom[1163] -- initialized process vdom to 'root' (cookie='(null)')
    [httpsd 181 - 1535636630     info] api_store_parameter[227] -- add API parameter 'source': '"fortiguard"' (type=string)
    [httpsd 181 - 1535636630     info] api_store_parameter[227] -- add API parameter 'filename': '"06000000FIMG0012000000"' (type=string)
    [httpsd 181 - 1535636630     info] endpoint_process_req_vdom[444] -- new API request (action='upgrade',path='system',name='firmware',vdom='root',user='admin')
    [httpsd 181 - 1535636630     info] system_firmware_upgrade[1635] -- firmware upgrade attempt from management station for image '06000000FIMG0012000000'
    [httpsd 181 - 1535636643     info] _system_firmware_download_fds[1549] -- firmware download state: 0
    [httpsd 181 - 1535636643     info] system_firmware_upgrade[1648] -- upgrade attempt for '/tmp/fdsm.out'
    [httpsd 181 - 1535636643    error] system_firmware_upgrade[1652] -- upgrade initiated for '/tmp/fdsm.out'
    [httpsd 181 - 1535636643     info] system_firmware_upgrade[1659] -- upgrade success for '/tmp/fdsm.out'
    [httpsd 181 - 1535636643     info] ap_invoke_handler[616] -- request completed (handler='api_monitor_v2-handler' result==0)
'''

import os
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

# Obtain FIRMWARE_ID with monitor_system_firmware
FIRMWARE_ID = '06000000FIMG0012000000'  # 6.0.0
# FIRMWARE_ID = '06000000FIMG0012000001'  # 6.0.1

UPLOAD_DATA = {
    'source': 'fortiguard',
    'filename': FIRMWARE_ID,
}

UPLOAD_DATA = json.dumps(UPLOAD_DATA)

FG.upload('system', 'firmware/upgrade', data=UPLOAD_DATA)
