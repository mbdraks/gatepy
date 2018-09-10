#!/usr/bin/env python3

'''

Module for Fortinet FortiOS CMDB API

'''

import os
import requests
from fortiosapi import FortiOSAPI

class FortinetFortiGateCMDB(FortiOSAPI):
    """FortinetFortiGate Class

    This class will be used to extend the functions of the original 
    FortiOSAPI class

    """
    def __init__(self):
        self._https = True
        self._fortiversion = "Version is set when logged"
        self._session = requests.session()
        self._session.verify = False

    def get_cmdb_system_interfaces(self, interface_name=None):
        """Get configured interfaces. 

        Args:
            interface_name (str, optional): Filter results by interface name

        Returns:
            Configured interfaces as a list

        """
        if interface_name:
            filter = 'filter=name==' + interface_name
        else:
            filter = ''
        resp = self.get('system', 'interface', parameters=filter)
        if resp['status'] == 'success':
            if len(resp['results']) == 1:       # if filtered resp will have only one interface config
                return resp['results'][0]       # return a dict instead of a list to make interface details easier to access
            return resp['results']
        else:
            return 'nok'
