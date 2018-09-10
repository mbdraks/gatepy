#!/usr/bin/env python3

'''Retrieve a list of all interfaces along with some meta info'''

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


def main():
    device = gatepy.FortinetFortiGate()
    device.login(**DEVICE)
    out = device.get_monitor_system_available_interfaces()
    pprint(out)


if __name__ == '__main__':
    main()
