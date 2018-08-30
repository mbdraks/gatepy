#!/usr/bin/env python3

'''
Configure AntiVirus profiles

Method
  https://<DEVICE_IP>/api/v2/cmdb/antivirus/profile
  https://<DEVICE_IP>/api/v2/cmdb/antivirus/profile?filter=name==default


CLI
  FG # sh antivirus profile default
  config antivirus profile
      edit "default"
          set comment "Scan files and block viruses."
          config http
              set options scan
          end
          config ftp
              set options scan
          end
          config imap
              set options scan
              set executables virus
          end
          config pop3
              set options scan
              set executables virus
          end
          config smtp
              set options scan
              set executables virus
          end
      next
  end


Response
  {
    "http_method":"GET",
    "revision":"1.0.3.9539865665020678008.1535505187",
    "results":[
      {
        "q_origin_key":"default",
        "name":"default",
        "comment":"Scan files and block viruses.",
        "replacemsg-group":"",
        "inspection-mode":"flow-based",
        "ftgd-analytics":"disable",
        "analytics-max-upload":10,
        "analytics-wl-filetype":0,
        "analytics-bl-filetype":0,
        "analytics-db":"disable",
        "mobile-malware-db":"enable",
        "http":{
          "options":"scan",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "outbreak-prevention":"disabled",
          "content-disarm":"disable"
        },
        "ftp":{
          "options":"scan",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "outbreak-prevention":"disabled"
        },
        "imap":{
          "options":"scan",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "executables":"virus",
          "outbreak-prevention":"disabled",
          "content-disarm":"disable"
        },
        "pop3":{
          "options":"scan",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "executables":"virus",
          "outbreak-prevention":"disabled",
          "content-disarm":"disable"
        },
        "smtp":{
          "options":"scan",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "executables":"virus",
          "outbreak-prevention":"disabled",
          "content-disarm":"disable"
        },
        "mapi":{
          "options":"",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "executables":"default",
          "outbreak-prevention":"disabled"
        },
        "nntp":{
          "options":"",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "outbreak-prevention":"disabled"
        },
        "smb":{
          "options":"",
          "archive-block":"",
          "archive-log":"",
          "emulator":"enable",
          "outbreak-prevention":"disabled"
        },
        "nac-quar":{
          "infected":"none",
          "expiry":"5m",
          "log":"disable"
        },
        "content-disarm":{
          "original-file-destination":"discard",
          "office-macro":"enable",
          "office-hylink":"enable",
          "office-linked":"enable",
          "office-embed":"enable",
          "pdf-javacode":"enable",
          "pdf-embedfile":"enable",
          "pdf-hyperlink":"enable",
          "pdf-act-gotor":"enable",
          "pdf-act-launch":"enable",
          "pdf-act-sound":"enable",
          "pdf-act-movie":"enable",
          "pdf-act-java":"enable",
          "pdf-act-form":"enable",
          "cover-page":"enable",
          "detect-only":"disable"
        },
        "av-virus-log":"enable",
        "av-block-log":"enable",
        "extended-log":"disable",
        "scan-mode":"full"
      }
    ],
    "vdom":"root",
    "path":"antivirus",
    "name":"profile",
    "status":"success",
    "http_status":200,
    "serial":"FGVM020000000000",
    "version":"v6.0.0",
    "build":76
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

profile_name = 'default'
filter = 'filter=name==' + profile_name

out = fgt.get('antivirus', 'profile', parameters=filter)

pprint(out)


fgt.logout()

