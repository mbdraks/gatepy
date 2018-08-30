#!/usr/bin/env python3

'''
Configure IPv4 policies

Method
  https://<DEVICE_IP>/api/v2/cmdb/firewall/policy?action=schema
  https://<DEVICE_IP>/api/v2/cmdb/firewall/policy


CLI
    FG # sh firewall policy 
    config firewall policy
        edit 1
            set name "to Internet"
            set uuid bfa5cd8e-aba3-51e8-567b-302f11df04b7
            set srcintf "port1"
            set dstintf "port2"
            set srcaddr "all"
            set dstaddr "all"
            set action accept
            set schedule "always"
            set service "ALL"
            set logtraffic all
            set nat enable
        next
    end


Response
    {
      "http_method": "GET",
      "revision": "20.0.0.9539865665020678008.1535505187",
      "results": [
        {
          "q_origin_key": 1,
          "policyid": 1,
          "name": "to Internet",
          "uuid": "bfa5cd8e-aba3-51e8-567b-302f11df04b7",
          "srcintf": [
            {
              "q_origin_key": "port1",
              "name": "port1"
            }
          ],
          "dstintf": [
            {
              "q_origin_key": "port2",
              "name": "port2"
            }
          ],
          "srcaddr": [
            {
              "q_origin_key": "all",
              "name": "all"
            }
          ],
          "dstaddr": [
            {
              "q_origin_key": "all",
              "name": "all"
            }
          ],
          "internet-service": "disable",
          "internet-service-id": [],
          "internet-service-custom": [],
          "internet-service-src": "disable",
          "internet-service-src-id": [],
          "internet-service-src-custom": [],
          "rtp-nat": "disable",
          "rtp-addr": [],
          "learning-mode": "disable",
          "action": "accept",
          "send-deny-packet": "disable",
          "firewall-session-dirty": "check-all",
          "status": "enable",
          "schedule": "always",
          "schedule-timeout": "disable",
          "service": [
            {
              "q_origin_key": "ALL",
              "name": "ALL"
            }
          ],
          "dscp-match": "disable",
          "dscp-negate": "disable",
          "dscp-value": "000000",
          "tcp-session-without-syn": "disable",
          "utm-status": "disable",
          "profile-type": "single",
          "profile-group": "",
          "av-profile": "",
          "webfilter-profile": "",
          "dnsfilter-profile": "",
          "spamfilter-profile": "",
          "dlp-sensor": "",
          "ips-sensor": "",
          "application-list": "",
          "voip-profile": "",
          "icap-profile": "",
          "waf-profile": "",
          "ssh-filter-profile": "",
          "profile-protocol-options": "",
          "ssl-ssh-profile": "",
          "logtraffic": "all",
          "logtraffic-start": "disable",
          "capture-packet": "disable",
          "wanopt": "disable",
          "wanopt-detection": "active",
          "wanopt-passive-opt": "default",
          "wanopt-profile": "",
          "wanopt-peer": "",
          "webcache": "disable",
          "webcache-https": "disable",
          "traffic-shaper": "",
          "traffic-shaper-reverse": "",
          "per-ip-shaper": "",
          "application": [],
          "app-category": [],
          "url-category": [],
          "app-group": [],
          "nat": "enable",
          "permit-any-host": "disable",
          "permit-stun-host": "disable",
          "fixedport": "disable",
          "ippool": "disable",
          "poolname": [],
          "session-ttl": 0,
          "vlan-cos-fwd": 255,
          "vlan-cos-rev": 255,
          "inbound": "disable",
          "outbound": "enable",
          "natinbound": "disable",
          "natoutbound": "disable",
          "wccp": "disable",
          "ntlm": "disable",
          "ntlm-guest": "disable",
          "ntlm-enabled-browsers": [],
          "fsso": "enable",
          "wsso": "enable",
          "rsso": "disable",
          "fsso-agent-for-ntlm": "",
          "groups": [],
          "users": [],
          "devices": [],
          "auth-path": "disable",
          "disclaimer": "disable",
          "vpntunnel": "",
          "natip": "0.0.0.0 0.0.0.0",
          "match-vip": "disable",
          "diffserv-forward": "disable",
          "diffserv-reverse": "disable",
          "diffservcode-forward": "000000",
          "diffservcode-rev": "000000",
          "tcp-mss-sender": 0,
          "tcp-mss-receiver": 0,
          "comments": "",
          "label": "",
          "global-label": "",
          "auth-cert": "",
          "auth-redirect-addr": "",
          "redirect-url": "",
          "identity-based-route": "",
          "block-notification": "disable",
          "custom-log-fields": [],
          "replacemsg-override-group": "",
          "srcaddr-negate": "disable",
          "dstaddr-negate": "disable",
          "service-negate": "disable",
          "internet-service-negate": "disable",
          "internet-service-src-negate": "disable",
          "timeout-send-rst": "disable",
          "captive-portal-exempt": "disable",
          "ssl-mirror": "disable",
          "ssl-mirror-intf": [],
          "scan-botnet-connections": "disable",
          "dsri": "disable",
          "radius-mac-auth-bypass": "disable",
          "delay-tcp-npu-session": "disable",
          "vlan-filter": ""
        }
      ],
      "vdom": "root",
      "path": "firewall",
      "name": "policy",
      "status": "success",
      "http_status": 200,
      "serial": "FGVM020000000000",
      "version": "v6.0.0",
      "build": 76
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

out = fgt.get('firewall', 'policy')

pprint(out)

fgt.logout()
