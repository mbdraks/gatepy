#!/usr/bin/env python3

'''gatepy module

    FortinetFortiGate class will be used to extend the functions of the original 
    FortiOSAPI class
    '''

import os
import requests
from cmdb import FortinetFortiGateCMDB
from monitor import FortinetFortiGateMonitor

class FortinetFortiGate(FortinetFortiGateCMDB, FortinetFortiGateMonitor):
    
    def __init__(self):
        self._https = True
        self._fortiversion = "Version is set when logged"
        self._session = requests.session()
        self._session.verify = False
