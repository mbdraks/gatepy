#!/usr/bin/env python3

'''
Backup system config

Method
    https://<DEVICE_IP>/api/v2/monitor/system/config/backup?scope=global


CLI
    FG # show full-configuration
    #config-version=FG81EP-6.0.2-FW-build0163-180725:opmode=1:vdom=0:user=admin
    #conf_file_ver=380263519573911
    #buildno=0163
    #global_vdom=1
    config system global
        set admin-concurrent enable
        set admin-console-timeout 0
        set admin-https-pki-required disable
        set admin-https-redirect enable
        set admin-https-ssl-versions tlsv1-1 tlsv1-2
        set admin-lockout-duration 60
    ....


Response
    Object
'''

from fortiosapi import FortiOSAPI

fgt = FortiOSAPI()

device = {
    'host': '10.99.236.231',
    'username': 'admin',
    'password': '',
}

fgt.login(**device)

out = fgt.download('system', 'config/backup', parameters={'scope': 'global'})

with open("fg_backup.txt", "w") as f:
    f.write(out.text)