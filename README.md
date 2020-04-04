# PROJECT: Cirrocumulus
<img src="https://github.com/MarkMonterosso/vm-deployment/blob/dev/imgs/cirrocumulus.jpeg" width=250>

## Overview
The goal of this project is to provide the automated ability to create a small private cloud-like environment.
The base project will provide a quick way to spin up and down virtual machines; additional features will be available to layer-on 
to this base, and allow for quick provisioning of objects such as containers to support applications, development, testing, etc.

## Motivation
A day in the life of almost anyone in I.T. requires that we provide demos, perform testing, training,
development, etc.; It quickly becomes tiresome to constantly build and tear down your infrastructure. This project is 
an attempt at aleviating some of the madness that comes with being an I.T. professional. 

## Technologies & Requirements
As mentioned above, this project is somewhat of a, "choose your own adventure". The base requirements are bolded, everything else that is a feature
addition will be built upon that base. These features will have their own dependencies and depending on the, "adventure", you choose.

+ __Virtualization Platform__
  +  <a href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMWorkstation 15.x</a> 
  +  <a href="https://www.vmware.com/go/downloadfusion">VMFusion 11</a>
+ __Ansible__
  + <a href="https://docs.ansible.com/">PAY FOR - Ansible Tower</a>
  + <a href="https://docs.ansible.com/">FREE - Ansible Core 2.9+</a>
  + <a href="https://github.com/ansible/awx">FREE - AWX 9.1.1+</a> 
    + This is an upstream project for Tower, a commercial derivative of AWX 
+ NetApp 
  + <a href="https://mysupport.netapp.com/site/tools/tool-eula/5e31797415040d3cce0033d3">OnTap Simulator - ONTAP 9.6+</a>
    + This can be replaced with any OnTap system
  + <a href="https://netapp-trident.readthedocs.io/en/stable-v20.01/">Trident 20.x+</a>
    + Required if you decide to use persistent storage from the OnTap system
+ Containerizaton Platform
  + <a href="https://www.docker.com/">Docker 1.10+</a> 
  + <a href="https://kubernetes.io/">Kubernetes 1.14+</a>
  
## Preparation
The following sections must be already installed in your environment.
- [ ] Decide which virtualization platform are you using:
  - [ ] Purchase and install VMWorkstation 15.x+
  - [ ] Purchase and install Fusion 11+
- [ ] Enable the REST interface for VMWorkstation or Fusion
    <br>__Note:__ _Make sure you perform the setup for the HTTPS services_<br>
    <img src="https://github.com/MarkMonterosso/vm-deployment/blob/dev/imgs/vmworkstation/vmworkstation_rest.PNG" width=350>
  - [ ] <a href="https://docs.vmware.com/en/VMware-Workstation-Pro/15.0/com.vmware.ws.using.doc/GUID-C3361DF5-A4C1-432E-850C-8F60D83E5E2B.html">VM Workstation REST setup guide</a>
  - [ ] <a href="https://docs.vmware.com/en/VMware-Fusion/11/com.vmware.fusion.using.doc/GUID-63847178-3425-4D92-A043-EFBC1251C606.html">VM Fusion REST setup guide</a>
- [ ] Create your set of VM templates VM Workstation or Fusion
        <br>_Example:<br> <img src="https://github.com/MarkMonterosso/vm-deployment/blob/dev/imgs/vmworkstation/vmworkstation_templates.PNG"/>_
- [ ] Decide which implementation of Ansible you are using:
  - [ ] Download and install Ansible Core
  - [ ] Download and install AWX
  - [ ] Purchase and install Ansible Tower
- [ ] Repository Usage
 - [ ] It is recommended that you clone the contents of this repository into your own to avoid unexpected behavior due to future updates
    ```
    git clone https://github.com/MarkMonterosso/cirrocumulus.git    
    ```  
 - [ ] If you are using Tower or AWX it is recommended to create a project (<a href="https://github.com/MarkMonterosso/vm-deployment/blob/dev/TOWER_AWX.md">Setup Guide</a>)
 - [ ] If you are using Ansible core, simply clone the repository and place it somewhere logical on your Ansible host
  
## Usage
__Ansible Core__
- [ ] Modify the vars-provision-infra.yml file
  - [ ] Follow the in-file documentation
- [ ] Execute the playbook<br>
    ```
    ansible-playbook -i inventory <path>/cirrocumulus/ansible/provision-infra.yml    
    ```

__Ansible AWX or Tower__<br>
- [ ] Coming Soon

## Authors
+ Mark Monterosso - NetApp Solutions Architect with focus on Automation & DevOps