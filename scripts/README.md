# AUTOMATED VM DEPLOYMENT

## Overview
Manipulate VMware Workstation or Fusion virtual machines

## Requirements
__Microsoft Windows 10__
+ VMware Workstation 15.x
+ Python 3.7+
+ Pip

__MAC__
+ VMware Fusion 11
+ Python 3.7+
+ Pip

## Installation & Configuration
Please follow the following instructions to setup your environment correctly.

__Microsoft Windows 10__

+ Go to Microsoft Application Store
  + Search for Python 3.x and install the application
  + Make sure python3 is part in the environment path
+ Download the contents of this repository
  + Open a command prompt and navigate to the location you stored this repo's contents
  + Run the following:
    ```python
     > python3 get-pip.py    
    ```

__MAC__

## Usage
```python
vm-ops.py --rest_uri <rest endpoint>:<port> --vm <vm or template name> --user <REST user> --password <REST password> --action [clone,delete,start,stop] | --clone_name <clone>

Examples:
python vm-ops.py --uri "http://127.0.0.1:8697" --vm "test_vm" --user "developer" --pass "myP@$$123" --action "start"

python vm-ops.py --uri "http://127.0.0.1:8697" --vm "test_vm" --user "developer" --pass "myP@$$123" --action "clone" --clone_name "test_vm_clone"
```