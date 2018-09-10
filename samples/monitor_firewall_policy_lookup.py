#!/usr/bin/env python3

'''Performs a policy lookup'''

import os
from pprint import pprint
import gatepy

FG_HOST = os.environ['FG_HOST']
FG_USER = os.environ['FG_USER']
FG_PASS = os.environ['FG_PASS']

DEVICE = {
    'host': FG_HOST,
    'username': FG_USER,
    'password': FG_PASS,
}

lookup_parameters = {
    'srcintf': 'port2',
    'sourceip': '1.1.1.1',
    'protocol': '6',
    'dest': '10.0.0.10',
    'destport': 80,
}

def main():
    device = gatepy.FortinetFortiGate()
    device.login(**DEVICE)
    out = device.get_monitor_firewall_policy_lookup(**lookup_parameters)
    device.logout()
    pprint(out)


if __name__ == '__main__':
    main()
