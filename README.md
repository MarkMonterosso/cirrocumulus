# PROJECT: Cirrocumulus
<img src="https://github.com/MarkMonterosso/vm-deployment/blob/dev/imgs/cirrocumulus.jpeg" width=250>

## Overview
The goal of this project is to provide the automated ability to create a small private cloud-like environment.

## Motivation
A day in the life of almost anyone in I.T. requires that we provide demos, perform testing, training,
development, etc.; It quickly becomes tiresome to constantly build and tear down your infrastructure. This project is 
an attempt at aleviating some of the madness that comes with being an I.T. professional. 

## Requirements
This project assumes you have a basic understanding of VMWare, Ansible, NetApp, general infrastructure and scripting knowledge. 
To get started you must have some comination of the following installed and configured in your environment.

#### Technologies
+ VMWare
  +  <a href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMWorkstation 15.x</a> 
  +  <a href="https://www.vmware.com/go/downloadfusion">VMFusion 11</a>
+ Ansible
  + <a href="https://docs.ansible.com/">PAY FOR - Ansible Tower</a>
  + <a href="https://docs.ansible.com/">FREE - Ansible Core 2.9+</a>
  + <a href="https://github.com/ansible/awx">FREE - AWX 9.1.1+</a> 
    + This is an upstream project for Tower, a commercial derivative of AWX 
+ NetApp 
  + <a href="https://mysupport.netapp.com/site/tools/tool-eula/5e31797415040d3cce0033d3">OnTap Simulator - ONTAP 9.6+</a>
    + This can be replaced with any OnTap system
  + <a href="https://netapp-trident.readthedocs.io/en/stable-v20.01/">Trident 20.x+</a>
    + Required if you decide to use persistent storage from the OnTap system
+ Docker 
+ Kubernetes
  
## Preparation
The following sections must be already installed in your environment.
- [ ] Decide which virtualization platform are you using:
  - [ ] Purchase and install VMWorkstation 15.x+
  - [ ] Purchase and install Fusion 11+
- [ ] Decide which implementation of Ansible you are using:
  - [ ] Download and install Ansible Core
  - [ ] Download and install AWX
  - [ ] Purchase and install Ansible Tower
- [ ] Repository Usage
  - [ ] If you are using Tower or AWX it is recommended to create a project (see. <a href="https://github.com/MarkMonterosso/vm-deployment/blob/dev/TOWER_AWX.md">Setup Guide</a> ).
    - [ ] It is recommended that you clone the contents of this repository into your own to avoid unexpected behavior due to future updates.
        ```
        git clone https://github.com/MarkMonterosso/cirrocumulus.git    
        ```  
  
## Usage
TBD

## Versioning
TBD
## Contributing
TBD
## Authors
+ Mark Monterosso - NetApp Solutions Architect with focus on Automation & DevOps

## License
TBD
## Acknowledgements
TBD