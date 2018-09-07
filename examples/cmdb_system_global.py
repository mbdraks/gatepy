#!/usr/bin/env python3

'''
Configure global attributes.


Method
    https://<DEVICE_IP>/api/v2/cmdb/system/global


CLI
    FG # sh sys gl
    config system global
        set alias "FG"
        set hostname "FG"
        set timezone 04
    end


Response
{
  "http_method": "GET",
  "revision": "6.0.0.9542928822994478097.1536278864",
  "results": {
    "language": "english",
    "gui-ipv6": "disable",
    "gui-certificates": "enable",
    "gui-custom-language": "disable",
    "gui-wireless-opensecurity": "disable",
    "gui-display-hostname": "disable",
    "gui-lines-per-page": 50,
    "admin-https-ssl-versions": "tlsv1-1 tlsv1-2",
    "admintimeout": 5,
    "admin-console-timeout": 0,
    "admin-concurrent": "enable",
    "admin-lockout-threshold": 3,
    "admin-lockout-duration": 60,
    "refresh": 0,
    "interval": 5,
    "failtime": 5,
    "daily-restart": "disable",
    "restart-time": "00:00",
    "radius-port": 1812,
    "admin-login-max": 100,
    "remoteauthtimeout": 5,
    "ldapconntimeout": 500,
    "batch-cmdb": "enable",
    "multi-factor-authentication": "optional",
    "ssl-min-proto-version": "TLSv1-2",
    "dst": "enable",
    "timezone": "04",
    "traffic-priority": "tos",
    "traffic-priority-level": "medium",
    "anti-replay": "strict",
    "send-pmtu-icmp": "enable",
    "honor-df": "enable",
    "revision-image-auto-backup": "disable",
    "revision-backup-on-logout": "disable",
    "management-vdom": "root",
    "hostname": "FG",
    "alias": "FG",
    "strong-crypto": "enable",
    "ssh-cbc-cipher": "enable",
    "ssh-hmac-md5": "enable",
    "ssh-kex-sha1": "enable",
    "ssl-static-key-ciphers": "enable",
    "snat-route-change": "disable",
    "cli-audit-log": "disable",
    "dh-params": "2048",
    "fds-statistics": "enable",
    "fds-statistics-period": 60,
    "multicast-forward": "enable",
    "mc-ttl-notchange": "disable",
    "asymroute": "disable",
    "tcp-option": "enable",
    "lldp-transmission": "disable",
    "proxy-auth-timeout": 10,
    "proxy-re-authentication-mode": "session",
    "proxy-auth-lifetime": "disable",
    "proxy-auth-lifetime-timeout": 480,
    "sys-perf-log-interval": 5,
    "check-protocol-header": "loose",
    "vip-arp-range": "restricted",
    "reset-sessionless-tcp": "disable",
    "allow-traffic-redirect": "enable",
    "strict-dirty-session-check": "enable",
    "tcp-halfclose-timer": 120,
    "tcp-halfopen-timer": 10,
    "tcp-timewait-timer": 1,
    "udp-idle-timer": 180,
    "block-session-timer": 30,
    "ip-src-port-range": "1024-25000",
    "pre-login-banner": "disable",
    "post-login-banner": "disable",
    "tftp": "enable",
    "av-failopen": "pass",
    "av-failopen-session": "disable",
    "memory-use-threshold-extreme": 95,
    "memory-use-threshold-red": 88,
    "memory-use-threshold-green": 82,
    "cpu-use-threshold": 90,
    "check-reset-range": "disable",
    "vdom-admin": "disable",
    "long-vdom-name": "disable",
    "admin-port": 80,
    "admin-sport": 443,
    "admin-https-redirect": "enable",
    "admin-ssh-password": "enable",
    "admin-restrict-local": "disable",
    "admin-ssh-port": 22,
    "admin-ssh-grace-time": 120,
    "admin-ssh-v1": "disable",
    "admin-telnet-port": 23,
    "admin-maintainer": "enable",
    "admin-server-cert": "self-sign",
    "user-server-cert": "Fortinet_Factory",
    "admin-https-pki-required": "disable",
    "wifi-certificate": "Fortinet_Wifi",
    "wifi-ca-certificate": "Fortinet_Wifi_CA",
    "auth-http-port": 1000,
    "auth-https-port": 1003,
    "auth-keepalive": "disable",
    "policy-auth-concurrent": 0,
    "auth-session-limit": "block-new",
    "auth-cert": "Fortinet_Factory",
    "clt-cert-req": "disable",
    "fortiservice-port": 8013,
    "endpoint-control-portal-port": 8009,
    "endpoint-control-fds-access": "enable",
    "tp-mc-skip-policy": "disable",
    "cfg-save": "automatic",
    "cfg-revert-timeout": 600,
    "reboot-upon-config-restore": "enable",
    "admin-scp": "disable",
    "security-rating-result-submission": "enable",
    "security-rating-run-on-schedule": "enable",
    "wireless-controller": "enable",
    "wireless-controller-port": 5246,
    "fortiextender-data-port": 25246,
    "fortiextender": "disable",
    "fortiextender-vlan-mode": "disable",
    "switch-controller": "disable",
    "switch-controller-reserved-network": "169.254.0.0 255.255.0.0",
    "proxy-worker-count": 0,
    "scanunit-count": 0,
    "proxy-kxp-hardware-acceleration": "enable",
    "proxy-cipher-hardware-acceleration": "enable",
    "fgd-alert-subscription": "",
    "ipsec-hmac-offload": "enable",
    "ipv6-accept-dad": 1,
    "ipv6-allow-anycast-probe": "disable",
    "csr-ca-attribute": "enable",
    "wimax-4g-usb": "disable",
    "cert-chain-max": 8,
    "sslvpn-max-worker-count": 0,
    "sslvpn-kxp-hardware-acceleration": "enable",
    "sslvpn-cipher-hardware-acceleration": "enable",
    "sslvpn-plugin-version-check": "enable",
    "two-factor-ftk-expiry": 60,
    "two-factor-email-expiry": 60,
    "two-factor-sms-expiry": 60,
    "two-factor-fac-expiry": 60,
    "two-factor-ftm-expiry": 72,
    "per-user-bwl": "disable",
    "virtual-server-count": 0,
    "virtual-server-hardware-acceleration": "enable",
    "wad-worker-count": 0,
    "wad-csvc-cs-count": 1,
    "wad-csvc-db-count": 0,
    "wad-source-affinity": "enable",
    "login-timestamp": "disable",
    "miglogd-children": 0,
    "special-file-23-support": "disable",
    "log-uuid": "policy-only",
    "log-ssl-connection": "disable",
    "arp-max-entry": 131072,
    "av-affinity": "0",
    "wad-affinity": "0",
    "ips-affinity": "0",
    "miglog-affinity": "0",
    "ndp-max-entry": 0,
    "br-fdb-max-entry": 8192,
    "max-route-cache-size": 0,
    "ipsec-asic-offload": "enable",
    "ipsec-soft-dec-async": "disable",
    "device-idle-timeout": 300,
    "device-identification-active-scan-delay": 90,
    "compliance-check": "enable",
    "compliance-check-time": "00:00:00",
    "gui-device-latitude": "",
    "gui-device-longitude": "",
    "private-data-encryption": "disable",
    "auto-auth-extension-device": "enable",
    "gui-theme": "green",
    "gui-date-format": "yyyy/MM/dd",
    "igmp-state-limit": 3200
  },
  "vdom": "root",
  "path": "system",
  "name": "global",
  "status": "success",
  "http_status": 200,
  "serial": "FGVM040000000000",
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



out = FG.get('system', 'global')

pprint(out)

FG.logout()
