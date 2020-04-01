#######################################################################################
#   
#   Author      :   Mark Monterosso - Mark.Monterosso@NetApp.com
#   Date        :   21 Mar 20
#   
#   Description :   The purpose of this code is to facilitate cloning of virtual
#                   machines in VM Workstation
#   
#   Dependencies:   VM Workstation 15.x 
#                   REST listener configured
#                   Pip intalled
#                       - Ensure all imported modules have been installed
#                   
#######################################################################################

#######################################################################################
#
#   MODULES
#
#######################################################################################
import requests 
import json 
import sys 
import argparse

#######################################################################################
#
#   CLASSES
#
#######################################################################################
class VirtualMachine:
    #------
    # Initialization Method 
    #------
    def __init__(self, rest_uri, parent_vm, username, password):
        self.name = parent_vm
        self.id = ""
        self.username = username
        self.__password = password
        self.rest_uri = rest_uri
        self.__vm_mgmt_uri = rest_uri + "/api/vms"
 
        __response = requests.get(self.rest_uri, 
                                  auth=(self.username, self.__password))
        
        print("REST URI: " + rest_uri)
        if __response.status_code == 200:
            print("VMWare Workstation REST connection was successful...")
        else:
            print("VMWare Workstation connection failed, exiting!")
            sys.exit()
        
        __response = requests.get(self.__vm_mgmt_uri, 
                                  auth=(self.username, self.__password))
        
        print("\nREST URI: " + self.__vm_mgmt_uri)
        if __response.status_code == 200:
            print("Acquisition of virtual machine list successful...")

            # Load JSON object and parse for virtual machine match
            json_response = json.loads(__response.text)
            print("\nLocating virtual machine: " + parent_vm)
            for vm_path in json_response:
                vm_name = vm_path['path'].rsplit('\\',1)[1].rsplit('.',1)[0]
                if vm_name == parent_vm:
                    print("Virtual machine found: " + vm_name)
                    print("Virtual machine id: " + vm_path['id'])
                    self.id = vm_path['id']
                    break
            if self.id == "":
                print("Could not find virtual machine " + parent_vm + ", exiting!")
                sys.exit()
        else:
            print("Could not acquire virtual machine listing, exiting!")
            sys.exit()

    #------
    # External Method - Gets power status of a virtual machine
    #------
    def get_power_status(self):
        rest_power_uri = self.__vm_mgmt_uri + "/" + self.id + "/power"

        response = requests.get(rest_power_uri,
                                auth=(self.username,self.__password))

        if response.status_code == 200:
            vm_state = json.loads(response.text)['power_state']
        else:
            print("Could not get virtual machine power state, exiting!")
            sys.exit()    
        
        return(vm_state)
       
    #------
    # Exposed Method - Creates a clone of a parent virtual machine
    #------        
    def clone(self, clone_name):
        print("Creating clone: " + clone_name + " from: " + self.name)
       
        payload = { 
                    "name"      : clone_name,
                    "parentId"  : self.id
                  }

        response = requests.post(self.__vm_mgmt_uri,
                                 auth=(self.username,self.__password), 
                                 data=json.dumps(payload),
                                 headers={"Content-Type" : "application/vnd.vmware.vmw.rest-v1+json"})

        if response.status_code == 201:
            print("Clone " + clone_name + " was created successfully...")
            self.name = clone_name
            self.id = json.loads(response.text)['id']

            # INFO: MAM 21 Mar 20
            #   We should probably add in some properties of the newly created virtual machine
            #    {
            #        "id": "KKC00JG94D646DE9NTGHQMA8T2ODRE85",
            #         "cpu": {
            #             "processors": 4
            #         },
            #         "memory": 2048
            #     }

        else:
            print("Clone " + clone_name + " failed to create, exiting!")
            print("Status Code: " + str(response.status_code))
            print("Details    : \n" + response.text)

    #------
    # Exposed Method - Power on the virtual machine
    #------            
    def start(self):
        rest_power_state_change_uri = self.__vm_mgmt_uri + "/" + self.id + "/power"
   
        print("Assessing virtual machine: " + self.name + "'s power state...")  
        vm_state = self.get_power_status()

        if vm_state == "poweredOn":
            print("Virtual machine: " + self.name + " is currently powered on, no change.")
            return

        elif vm_state == "paused":
            print("Virtual machine: " + self.name + " is paused, starting virtual machine...")
            new_state = "unpause"

        elif vm_state == "suspended":
            print("Virtual machine: " + self.name + " is suspended, starting virtual machine...")
            new_state = "on"

        elif vm_state == "poweredOff":
            print("Virtual machine: " + self.name + " is not powered on, starting virtual machine...")
            new_state = "on"
            
        response = requests.put(rest_power_state_change_uri,
                                auth=(self.username,self.__password), 
                                data=new_state,
                                headers={"Content-Type" : "application/vnd.vmware.vmw.rest-v1+json"})
        
        if response.status_code == 200:
            print("Virtual machine: " + self.name + " is powered on.")
        else:
            print("Virtual machine: " + self.name + " could not be powered on, exiting!")

    #------
    # Exposed Method - Power off the virtual machine
    #------    
    def stop(self):
        rest_power_state_change_uri = self.__vm_mgmt_uri + "/" + self.id + "/power"

        print("Assessing virtual machine: " + self.name + "'s power state...")  
        vm_state = self.get_power_status()

        if vm_state == "poweredOn":
            print("Virtual machine: " + self.name + " is powered on, stopping virtual machine...")
            new_state = "off"

        elif vm_state == "paused":
            print("Virtual machine: " + self.name + " is currently paused. The virtual machine must be started before it can be turned off; no change.")
            return
        elif vm_state == "suspended":
            print("Virtual machine: " + self.name + " is currently suspended. The virtual machine must be started before it can be turned off; no change.")
            return
        elif vm_state == "poweredOff":
            print("Virtual machine: " + self.name + " is currently powered off. The virtual machine must be started before it can be turned off; no change.")
            return

        response = requests.put(rest_power_state_change_uri,
                                auth=(self.username,self.__password), 
                                data=new_state,
                                headers={"Content-Type" : "application/vnd.vmware.vmw.rest-v1+json"})

        if response.status_code == 200:
            print("Virtual machine: " + self.name + " is powered off.")
        else:
            print("Virtual machine: " + self.name + " could not be powered off, exiting!")

    #------
    # Exposed Method - Delete the virtual machine
    #------    
    def delete(self):
        rest_delete_vm_uri = self.__vm_mgmt_uri + "/" + self.id
        
        print("Removing virtual machine: " + self.name + "...") 

        response = requests.delete(rest_delete_vm_uri,
                                   auth=(self.username,self.__password), 
                                   headers={"Content-Type" : "application/vnd.vmware.vmw.rest-v1+json"})

        if response.status_code == 204:
            print("Virtual machine: " + self.name + " successfully removed.")
        else:
            print("Could not remove virtual machine: " + self.name + ", exiting!")

#######################################################################################
#
#   ANCILLARY FUNCTIONS
#
#######################################################################################
       
#######################################################################################
#
#   MAIN
#
#######################################################################################

def main():    

    # Collecting parameters
    cli_args_parser = argparse.ArgumentParser(allow_abbrev=True, description='Invoke vmware operations via REST')
    cli_args_parser.add_argument('--uri',       type=str, required=True,    help='Input the base URI: <http://<rest endpoint>:<port>')
    cli_args_parser.add_argument('--vm',        type=str, required=True,    help='Name of the VM or VM template to be manipulated')
    cli_args_parser.add_argument('--user',      type=str, required=True,    help='Username to authenticate the REST call')
    cli_args_parser.add_argument('--password',  type=str, required=True,    help='Password to authenticate the REST call')
    cli_args_parser.add_argument('--action',    type=str, required=True,    help='Possible actions are: clone, start, stop, and delete. The clone option requires the --clone_name flag.')
    cli_args_parser.add_argument('--clone_name',type=str, required=False,   help='Specify the name of the clone to be created from the --vm flag')
    args = cli_args_parser.parse_args()

    # Validating parameters        
    if args.action.lower() != 'start'   and \
       args.action.lower() != 'stop'    and \
       args.action.lower() != 'delete'  and \
       args.action.lower() != 'clone':
        print('Error: --action requires one of the following values: [start | stop | delete | clone].')
        return

    if args.action.lower() != 'clone' and (args.clone_name):
        print('Error: --clone_name can only be specified if you have selected, clone, as an action.')
        return

    if args.action.lower() == 'clone' and (args.clone_name is None):
        print('Error: --clone_name is required if you have selected, clone, as an action.')
        return

    # Create virtual machine object
    vm = VirtualMachine(args.uri,args.vm,args.user,args.password)

    # Do something useful. The lease you could do after all the pestering of your user.
    if args.action.lower()  == 'start'  : vm.start()
    if args.action.lower()  == 'stop'   : vm.stop()
    if args.action.lower()  == 'delete' : vm.delete()
    if args.action.lower()  == 'clone'  : vm.clone(args.clone_name)

#------
# Invoking Main()
#------    
main()