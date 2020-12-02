#######################################################################################
#   
#   Author      :   Mark Monterosso
#   Date        :   23 Mar 20
#   
#   Description :   Custom Python module for ansible to perform gather VM data
#                   from VM Workstation / Fusion 
#                   
#   Dependencies:  VM Workstation 15 / Fusion 11
#                  
#######################################################################################
from __future__ import absolute_import, division, print_function
__metaclass__ = type

#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: vm_get_facts

short_description: Present information about a VM

version_added: "2.9"

description:
    - "Use VMWorkstation 15+ or Fusion 11+ REST interface to gather information and present that data to the user"

options:
    vm_name:
        description:
            - This is the message to send to the test module
        required: true
    rest_uri:
        description:
            - URL and Port to VMWorkstation / Fusion REST endpoint
        required: true
    rest_username:
        description:
            - Username used to authenticate to REST endpoint
        required: true
    rest_password:
        description:
            - Password used to authenticate to REST endpoint
        required: true

author:
    - Mark Monterosso 
'''

EXAMPLES = '''
- name:                     Get VM Facts
  vm_get_facts:
    vm_name:                myvm
    rest_uri:               "https://vmworkstation-host:8697"
    rest_username:          "{{ rest_username }}"
    rest_password:          "{{ rest_password }}"
  register:                 vm_facts
'''

RETURN = '''
'''

import re
import requests 
import json 
import sys 
import argparse
import traceback
import time

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native

class VirtualMachine(object):
    def __init__(self):

        self.module_args = dict(
                                    vm_name         =dict(type='str', required=True),
                                    rest_uri        =dict(type='str', required=True),
                                    rest_username   =dict(type='str', required=True),
                                    rest_password   =dict(type='str', required=True, no_log=True)
                               )

        self.module = AnsibleModule(
            argument_spec=         self.module_args,
            supports_check_mode=   True
        )
        
        # Testing connection response during object instansiation
        self.connection_response = requests.get(self.module.params['rest_uri'], auth=(self.module.params['rest_username'], self.module.params['rest_password']), verify=False)
        
        if self.connection_response.status_code != 200:
            self.module.fail_json(msg='Could not establish REST connection')
    
    def build_facts(self):
        # Get VM management information
        vm_mgmt_uri = self.module.params['rest_uri'] + '/api/vms'
        vm_mgmt_response = requests.get(vm_mgmt_uri, auth=(self.module.params['rest_username'], self.module.params['rest_password']), verify=False)
        
        dict_vm_data = {}
        
        # Find VM and get name and ID
        if vm_mgmt_response.status_code == 200:           
           json_vm_mgmt_response = json.loads(vm_mgmt_response.text)
           for vm_path in json_vm_mgmt_response:
               # --------
               # FIXED: MAM 16 Apr 20
               # 
               # Removed: vm_name = vm_path['path'].rsplit('\\',1)[1].rsplit('.',1)[0]
               # To support different slashes for Fusion output
               #
               # Added the following 3 lines
               # -------- 
               vm_path_split = re.split(r'/|\\',vm_path['path'])
               vm_path_split = vm_path_split[len(vm_path_split)-1]
               vm_name = vm_path_split.split('.')[0]

               if vm_name.lower() == self.module.params['vm_name'].lower():
                   dict_vm_data['name'] = vm_name
                   dict_vm_data['id'] = vm_path['id']
                   break
           if not bool(dict_vm_data):
               self.module.fail_json(msg='FAILED: Could not locate VM')
        else:
            self.module.fail_json(msg='FAILED: Could not locate VM')

        # Find VM power state
        vm_power_uri = self.module.params['rest_uri'] + '/api/vms/' + dict_vm_data['id'] + '/power'
        vm_power_response = requests.get(vm_power_uri, auth=(self.module.params['rest_username'], self.module.params['rest_password']), verify=False)

        if vm_power_response.status_code == 200:           
          dict_vm_data['power_state'] = json.loads(vm_power_response.text)['power_state']
        else:
            self.module.fail_json(msg='FAILED: Could get power state of the VM') 
        
        self.module.exit_json(
            result = { 'vm' : dict_vm_data  }  
        )

def main():
    vm = VirtualMachine()
    vm.build_facts()

main()