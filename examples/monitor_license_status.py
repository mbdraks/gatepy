#!/usr/bin/env python3

'''
Get current license & registration status.

Method
  https://<DEVICE_IP>/api/v2/monitor/license/status


CLI
  NA

JSON
    {
      "http_method": "GET",
      "results": {
        "fortiguard": {
          "type": "service_or_support",
          "connected": false,
          "update_server_usa": true
        },
        "forticare": {
          "type": "service_or_support",
          "status": "pending"
        },
        "antivirus": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "1.00000",
          "entitlement": "AVDB",
          "last_update": 1517440740,
          "db_status": "db_type_extended",
          "engine": {
            "version": "6.00006",
            "last_update": 1520984340
          }
        },
        "mobile_malware": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "0.00000",
          "entitlement": "FMSS",
          "last_update": 978332400
        },
        "ips": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "6.00741",
          "entitlement": "NIDS",
          "last_update": 1448962200,
          "db_status": "db_type_normal",
          "engine": {
            "version": "4.00012",
            "last_update": 1521870900
          },
          "malicious_urls": {
            "type": "downloaded_fds_object",
            "status": "pending",
            "version": "1.00001",
            "entitlement": "NIDS",
            "last_update": 1420099260
          }
        },
        "industrial_db": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "6.00741",
          "entitlement": "ISSS",
          "last_update": 1448962200
        },
        "appctrl": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "6.00741",
          "entitlement": "FMWR",
          "last_update": 1448962200
        },
        "internet_service_db": {
          "type": "downloaded_fds_object",
          "status": "licensed",
          "version": "2.00662",
          "last_update": 1447786560
        },
        "device_os_id": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "1.00065",
          "entitlement": "FMWR",
          "last_update": 1522314180
        },
        "botnet_ip": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "1.00000",
          "entitlement": "AVDB",
          "last_update": 1338270660
        },
        "botnet_domain": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "0.00000",
          "entitlement": "AVDB",
          "last_update": 978332400
        },
        "security_rating": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "1.00005",
          "entitlement": "FGSA",
          "last_update": 1519872360
        },
        "malicious_urls": {
          "type": "downloaded_fds_object",
          "status": "pending",
          "version": "1.00001",
          "entitlement": "NIDS",
          "last_update": 1420099260
        },
        "web_filtering": {
          "type": "live_fortiguard_service",
          "status": "unavailable",
          "category_list_version": 8
        },
        "outbreak_prevention": {
          "type": "live_fortiguard_service",
          "status": "unavailable"
        },
        "antispam": {
          "type": "live_fortiguard_service",
          "status": "unavailable"
        },
        "forticlient": {
          "type": "product_integration",
          "status": "free_license",
          "can_upgrade": false,
          "used": 0,
          "max": 10
        },
        "forticloud": {
          "type": "product_integration",
          "status": "cloud_logged_out"
        },
        "vdom": {
          "type": "platform",
          "can_upgrade": true,
          "used": 1,
          "max": 1
        },
        "vm": {
          "type": "platform",
          "status": "vm_eval",
          "license_model": 1,
          "license_platform_name": "FGVMEV",
          "cpu_used": 1,
          "cpu_max": 1,
          "mem_used": 1043333120,
          "mem_max": 1073741824,
          "expires": 1537454850,
          "evaluation_mode": true
        },
        "sms": {
          "type": "other",
          "status": "pending",
          "used": 0,
          "max": 0
        }
      },
      "vdom": "root",
      "path": "license",
      "name": "status",
      "status": "success",
      "serial": "FGVMEVYEP9DLGG46",
      "version": "v6.0.0",
      "build": 76
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

out = fgt.monitor('license', 'status')

pprint(out)

fgt.logout()
