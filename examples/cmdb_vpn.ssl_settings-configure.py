#!/usr/bin/env python3

'''
Configure SSL VPN.


Method
    https://<DEVICE_IP>/api/v2/cmdb/vpn.ssl/settings


CLI
    FG # conf vpn ssl settings 
    FG (settings) # set tunnel-ip-pools SSLVPN_TUNNEL_ADDR1
    FG (settings) # set port 10443
    FG (settings) # set source-interface port1
    FG (settings) # set source-address all 
    FG (settings) # set default-portal full-access
    FG (settings) # end

    FG # sh vpn ssl settings
    config vpn ssl settings
        set servercert "self-sign"
        set tunnel-ip-pools "SSLVPN_TUNNEL_ADDR1"
        set source-interface "port1"
        set source-address "all"
        set default-portal "full-access"
    end


Response
    NA
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

vpnssl_settings = {
    'servercert':'self-sign',
    'tunnel-ip-pools':[{'name':'SSLVPN_TUNNEL_ADDR1'}],
    'source-interface':[{'name':'port1'}],
    'source-address':[{'name':'all'}],
    'port':'10443',
    'default-portal':'full-access',
}


# Config
FG.set('vpn.ssl', 'settings', data=vpnssl_settings)

# Check
out = FG.get('vpn.ssl', 'settings')

pprint(out)

FG.logout()
