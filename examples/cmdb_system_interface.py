#!/usr/bin/env python3

'''
Configure interfaces.

Method
    https://<DEVICE_IP>/api/v2/cmdb/system/interface?filter=name==port1


CLI
    FG # sh sys int port1
    config system interface
        edit "port1"
            set vdom "root"
            set ip 192.168.0.1 255.255.255.0
            set allowaccess ping https ssh http fgfm
            set type physical
            set snmp-index 1
        next
    end


Response
    {
      "http_method": "GET",
      "revision": "23.0.50.9539865665020678008.1535505187",
      "results": [
        {
          "q_origin_key": "port1",
          "name": "port1",
          "vdom": "root",
          "vrf": 0,
          "cli-conn-status": 0,
          "fortilink": "disable",
          "mode": "static",
          "distance": 5,
          "priority": 0,
          "dhcp-relay-service": "disable",
          "dhcp-relay-ip": "",
          "dhcp-relay-type": "regular",
          "dhcp-relay-agent-option": "enable",
          "management-ip": "0.0.0.0 0.0.0.0",
          "ip": "192.168.0.1 255.255.255.0",
          "allowaccess": "ping https ssh http fgfm",
          "gwdetect": "disable",
          "ping-serv-status": 0,
          "detectserver": "",
          "detectprotocol": "ping",
          "ha-priority": 1,
          "fail-detect": "disable",
          "fail-detect-option": "link-down",
          "fail-alert-method": "link-down",
          "fail-action-on-extender": "soft-restart",
          "fail-alert-interfaces": [],
          "dhcp-client-identifier": "",
          "dhcp-renew-time": 0,
          "ipunnumbered": "0.0.0.0",
          "username": "",
          "pppoe-unnumbered-negotiate": "enable",
          "password": "",
          "idle-timeout": 0,
          "detected-peer-mtu": 0,
          "disc-retry-timeout": 1,
          "padt-retry-timeout": 1,
          "service-name": "",
          "ac-name": "",
          "lcp-echo-interval": 5,
          "lcp-max-echo-fails": 3,
          "defaultgw": "enable",
          "dns-server-override": "enable",
          "auth-type": "auto",
          "pptp-client": "disable",
          "pptp-user": "",
          "pptp-password": "",
          "pptp-server-ip": "0.0.0.0",
          "pptp-auth-type": "auto",
          "pptp-timeout": 0,
          "arpforward": "enable",
          "ndiscforward": "enable",
          "broadcast-forward": "disable",
          "bfd": "global",
          "bfd-desired-min-tx": 250,
          "bfd-detect-mult": 3,
          "bfd-required-min-rx": 250,
          "l2forward": "disable",
          "icmp-redirect": "enable",
          "vlanforward": "disable",
          "stpforward": "disable",
          "stpforward-mode": "rpl-all-ext-id",
          "ips-sniffer-mode": "disable",
          "ident-accept": "disable",
          "ipmac": "disable",
          "subst": "disable",
          "macaddr": "00:50:56:01:68:fc",
          "substitute-dst-mac": "00:00:00:00:00:00",
          "speed": "auto",
          "status": "up",
          "netbios-forward": "disable",
          "wins-ip": "0.0.0.0",
          "type": "physical",
          "dedicated-to": "none",
          "trust-ip-1": "0.0.0.0 0.0.0.0",
          "trust-ip-2": "0.0.0.0 0.0.0.0",
          "trust-ip-3": "0.0.0.0 0.0.0.0",
          "trust-ip6-1": "::/0",
          "trust-ip6-2": "::/0",
          "trust-ip6-3": "::/0",
          "mtu-override": "disable",
          "mtu": 1500,
          "wccp": "disable",
          "netflow-sampler": "disable",
          "sflow-sampler": "disable",
          "drop-overlapped-fragment": "disable",
          "drop-fragment": "disable",
          "scan-botnet-connections": "disable",
          "src-check": "enable",
          "sample-rate": 2000,
          "polling-interval": 20,
          "sample-direction": "both",
          "explicit-web-proxy": "disable",
          "explicit-ftp-proxy": "disable",
          "proxy-captive-portal": "disable",
          "tcp-mss": 0,
          "inbandwidth": 0,
          "outbandwidth": 0,
          "egress-shaping-profile": "",
          "disconnect-threshold": 0,
          "spillover-threshold": 0,
          "ingress-spillover-threshold": 0,
          "weight": 0,
          "interface": "",
          "external": "disable",
          "vlanid": 0,
          "forward-domain": 0,
          "remote-ip": "0.0.0.0 0.0.0.0",
          "member": [],
          "lacp-mode": "active",
          "lacp-ha-slave": "enable",
          "lacp-speed": "slow",
          "min-links": 1,
          "min-links-down": "operational",
          "algorithm": "L4",
          "link-up-delay": 50,
          "priority-override": "enable",
          "aggregate": "",
          "redundant-interface": "",
          "managed-device": [],
          "devindex": 3,
          "vindex": 0,
          "switch": "",
          "description": "",
          "alias": "",
          "security-mode": "none",
          "captive-portal": 0,
          "security-mac-auth-bypass": "disable",
          "security-external-web": "",
          "security-external-logout": "",
          "replacemsg-override-group": "",
          "security-redirect-url": "",
          "security-exempt-list": "",
          "security-groups": [],
          "device-identification": "disable",
          "device-user-identification": "enable",
          "device-identification-active-scan": "disable",
          "device-access-list": "",
          "lldp-transmission": "vdom",
          "fortiheartbeat": "disable",
          "broadcast-forticlient-discovery": "disable",
          "endpoint-compliance": "disable",
          "estimated-upstream-bandwidth": 0,
          "estimated-downstream-bandwidth": 0,
          "vrrp-virtual-mac": "disable",
          "vrrp": [],
          "role": "undefined",
          "snmp-index": 1,
          "secondary-IP": "disable",
          "secondaryip": [],
          "preserve-session-route": "disable",
          "auto-auth-extension-device": "disable",
          "ap-discover": "enable",
          "fortilink-stacking": "enable",
          "fortilink-split-interface": "disable",
          "internal": 0,
          "fortilink-backup-link": 0,
          "switch-controller-access-vlan": "disable",
          "switch-controller-igmp-snooping": "disable",
          "switch-controller-dhcp-snooping": "disable",
          "switch-controller-dhcp-snooping-verify-mac": "disable",
          "switch-controller-dhcp-snooping-option82": "disable",
          "switch-controller-arp-inspection": "disable",
          "switch-controller-learning-limit": 0,
          "color": 0,
          "tagging": [],
          "ipv6": {
            "ip6-mode": "static",
            "nd-mode": "basic",
            "nd-cert": "",
            "nd-security-level": 0,
            "nd-timestamp-delta": 300,
            "nd-timestamp-fuzz": 1,
            "nd-cga-modifier": "0065636473612D776974682D73686132",
            "ip6-dns-server-override": "enable",
            "ip6-address": "::/0",
            "ip6-extra-addr": [],
            "ip6-allowaccess": "",
            "ip6-send-adv": "disable",
            "ip6-manage-flag": "disable",
            "ip6-other-flag": "disable",
            "ip6-max-interval": 600,
            "ip6-min-interval": 198,
            "ip6-link-mtu": 0,
            "ip6-reachable-time": 0,
            "ip6-retrans-time": 0,
            "ip6-default-life": 1800,
            "ip6-hop-limit": 0,
            "autoconf": "disable",
            "ip6-upstream-interface": "",
            "ip6-subnet": "::/0",
            "ip6-prefix-list": [],
            "ip6-delegated-prefix-list": [],
            "dhcp6-relay-service": "disable",
            "dhcp6-relay-type": "regular",
            "dhcp6-relay-ip": "",
            "dhcp6-client-options": "",
            "dhcp6-prefix-delegation": "disable",
            "dhcp6-information-request": "disable",
            "dhcp6-prefix-hint": "::/0",
            "dhcp6-prefix-hint-plt": 604800,
            "dhcp6-prefix-hint-vlt": 2592000,
            "vrrp-virtual-mac6": "disable",
            "vrip6_link_local": "::",
            "vrrp6": []
          }
        }
      ],
      "vdom": "root",
      "path": "system",
      "name": "interface",
      "status": "success",
      "http_status": 200,
      "serial": "FGVM020000000000",
      "version": "v6.0.0",
      "build": 76
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


interface_name = 'port1'
filter = 'filter=name==' + interface_name

out = FG.get('system', 'interface', parameters=filter)

pprint(out)

FG.logout()
