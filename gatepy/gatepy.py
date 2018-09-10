#!/usr/bin/env python3

'''Module for Fortinet FortiOS API'''

import os
import requests
from cmdb import FortinetFortiGateCMDB
from monitor import FortinetFortiGateMonitor

class FortinetFortiGate(FortinetFortiGateCMDB, FortinetFortiGateMonitor):
    """FortinetFortiGate Class

    This class will be used to extend the functions of the original 
    FortiOSAPI class

    """
    def __init__(self):
        self._https = True
        self._fortiversion = "Version is set when logged"
        self._session = requests.session()
        self._session.verify = False
