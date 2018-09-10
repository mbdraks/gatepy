#!/usr/bin/env python3

'''

Module for Fortinet FortiOS Monitor API

'''

import os
import requests
from fortiosapi import FortiOSAPI

class FortinetFortiGateMonitor(FortiOSAPI):
    """FortinetFortiGate Class

    This class will be used to extend the functions of the original 
    FortiOSAPI class

    """
    def __init__(self):
        self._https = True
        self._fortiversion = "Version is set when logged"
        self._session = requests.session()
        self._session.verify = False

    def get_monitor_firewall_policy_lookup( self, 
                                            srcintf=None, 
                                            sourceip=None, 
                                            protocol=None, 
                                            dest=None, 
                                            destport=None,
        ):
        """Performs a policy lookup by creating a dummy packet and asking the kernel which policy would be hit.

        Args:
            ipv6 (bool, optional): Perform an IPv6 lookup
            srcintf (str): Source Interface
            sourceport (int, optional): Source Port
            sourceip (str): Source IP
            protocol (str): Protocol
            dest (str): Destination IP/FQDN
            destport (int): Destination Port
            icmptype (int, optional): ICMP Type
            icmpcode (int, optional): ICMP Code


        Returns:
            Policy ID of matched policy lookup
        """
        
        param = {
            'srcintf': srcintf,
            'sourceip': sourceip,
            'protocol': protocol,
            'dest': dest,
            'destport': destport,
        }
        
        resp = self.monitor('firewall', 'policy-lookup', parameters=param)

        if resp['status'] == 'success':
            return resp['results']
        else:
            return 'nok'

    def get_monitor_firewall_policy(self, policyid=None):
        """List traffic statistics for IPv4 policies.

        Args:
            policyid (int, optional): Filter by Policy ID

        Returns:
            Traffic statistics for IPv4 policies.
        """
        
        if policyid:
            filter = 'policyid=' + str(policyid)
        else:
            filter = ''
        
        resp = self.monitor('firewall', 'policy', parameters=filter)

        if resp['status'] == 'success':
            return resp['results']
        else:
            return 'nok'


    def get_monitor_log_device_state(self):
        """Retrieve information on state of log devices.

        Returns:
            Retrieve information on state of log devices.
        """
            
        resp = self.monitor('log', 'device/state')

        if resp['status'] == 'success':
            return resp['results']
        else:
            return 'nok'


    def get_monitor_router_ipv4(self):
        """List all active IPv4 routing table entries

        Returns:
            NA
        """
            
        resp = self.monitor('router', 'ipv4')

        if resp['status'] == 'success':
            return resp['results']
        else:
            return 'nok'


    def get_monitor_system_available_interfaces(self, view_type=None):
        """Retrieve a list of all interfaces along with some meta information regarding their availability. 

        Args:
            view_type (str, optional): Include additional information for interfaces, valid options are:
            
                                         * 'poe': Includes PoE information for supported ports. 
                                         * 'ha': Includes extra meta information useful when dealing with interfaces related to HA configuration. Interfaces that are used by an HA cluster as management interfaces are also included in this view. 
                                         * 'zone': Includes extra meta information for determining zone membership eligibility.
                                         * 'vwp': Includes extra meta information for determining virtual wire pair eligibility.

        Returns:
            Retrieve a list of all interfaces along with some meta information regarding their availability.
        """

        if view_type:
            filter = 'view_type=' + view_type
        else:
            filter = ''
        
        resp = self.monitor('system', 'available-interfaces', parameters=filter)

        if resp['status'] == 'success':
            return resp['results']
        else:
            return 'nok'


    def get_monitor_system_config_backup(self, scope='global', vdom=None):
        """List all active IPv4 routing table entries

        Args:
            scope (str): global or vdom
            vdom (str, optional): vdom name

        Returns:
            None
        """
        
        param = {
            'scope': scope,
        }

        resp = self.download('system', 'config/backup', parameters=param)

        with open("fg_backup.txt", "w") as f:
            f.write(resp.text)

        if resp:
            return None
        else:
            return 'nok'


