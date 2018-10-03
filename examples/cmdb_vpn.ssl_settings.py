#!/usr/bin/env python3

'''
Configure SSL VPN.


Method
    https://<DEVICE_IP>/api/v2/cmdb/vpn.ssl/settings


CLI
    FG # sh vpn ssl settings
    config vpn ssl settings
        set servercert "self-sign"
        set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
        set source-interface "port1"
        set source-address "all"
        set default-portal "full-access"
    end


Response
    {
      "http_method": "GET",
      "revision": "15.0.0.9539865665020678008.1535658219",
      "results": {
        "reqclientcert": "disable",
        "tlsv1-0": "disable",
        "tlsv1-1": "enable",
        "tlsv1-2": "enable",
        "banned-cipher": "",
        "ssl-insert-empty-fragment": "enable",
        "https-redirect": "disable",
        "x-content-type-options": "enable",
        "ssl-client-renegotiation": "disable",
        "force-two-factor-auth": "disable",
        "unsafe-legacy-renegotiation": "disable",
        "servercert": "self-sign",
        "algorithm": "high",
        "idle-timeout": 300,
        "auth-timeout": 28800,
        "login-attempt-limit": 2,
        "login-block-time": 60,
        "login-timeout": 30,
        "dtls-hello-timeout": 10,
        "tunnel-ip-pools": [
          {
            "q_origin_key": "SSLVPN_TUNNEL_ADDR1",
            "name": "SSLVPN_TUNNEL_ADDR1"
          }
        ],
        "tunnel-ipv6-pools": [],
        "dns-suffix": "",
        "dns-server1": "0.0.0.0",
        "dns-server2": "0.0.0.0",
        "wins-server1": "0.0.0.0",
        "wins-server2": "0.0.0.0",
        "ipv6-dns-server1": "::",
        "ipv6-dns-server2": "::",
        "ipv6-wins-server1": "::",
        "ipv6-wins-server2": "::",
        "url-obscuration": "disable",
        "http-compression": "disable",
        "http-only-cookie": "enable",
        "deflate-compression-level": 6,
        "deflate-min-data-size": 300,
        "port": 10443,
        "port-precedence": "enable",
        "auto-tunnel-static-route": "enable",
        "header-x-forwarded-for": "add",
        "source-interface": [
          {
            "q_origin_key": "port1",
            "name": "port1"
          }
        ],
        "source-address": [
          {
            "q_origin_key": "all",
            "name": "all"
          }
        ],
        "source-address-negate": "disable",
        "source-address6": [],
        "source-address6-negate": "disable",
        "default-portal": "full-access",
        "authentication-rule": [],
        "dtls-tunnel": "enable",
        "check-referer": "disable",
        "http-request-header-timeout": 20,
        "http-request-body-timeout": 30
      },
      "vdom": "root",
      "path": "vpn.ssl",
      "name": "settings",
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

out = FG.get('vpn.ssl', 'settings')

pprint(out)

FG.logout()
