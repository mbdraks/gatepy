#!/usr/bin/env python3

''' Obtain all configured info from interface port1'''

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
    out = device.get_cmdb_system_interfaces('port1')
    pprint(out)


if __name__ == '__main__':
    main()
