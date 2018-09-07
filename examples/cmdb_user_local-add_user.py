#!/usr/bin/env python3

'''
Configure local users.

Method
    https://<DEVICE_IP>/api/v2/cmdb/user/local


CLI
    FG # config user local
    FG (local) # ed user1
    FG (user1) # set type password 
    FG (user1) # set passwd user1pwd
    FG (user1) # end

    FG # sh user local user1
    config user local
        edit "user1"
            set type password
            set passwd-time 2018-08-31 06:19:37
            set passwd ENC xxx
        next
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

user_config = {
    'name': 'user1',
    'type': 'password',
    "passwd": 'user1pwd',
}

# Config
FG.set('user', 'local', data=user_config)

# Check
filter = 'filter=name==' + user_config['name']
out = FG.get('user', 'local', parameters=filter)

pprint(out)

FG.logout()
