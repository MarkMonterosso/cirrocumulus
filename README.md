# PROJECT: Cirrocumulus
<img src="https://github.com/MarkMonterosso/vm-deployment/blob/master/imgs/cirrocumulus.jpeg" width=250>

## Overview
The basis of this project was formed out of a need to quickly spin up and tear down my lab for testing, training, etc. I've
decided to extend this out to add new features over time. 

The goal of this project is to provide a small private cloud-like experience that could be used for a range of purposes. This will
be somewhat of a choose your own adventure by enabling or disabling certain features through flags passed to the tool.

## Features & Status

<table>
    <tr><td><b>FEATURE</td><td><b>STATUS</td></tr>
    <tr><td>Provision VMs with VM Workstation 15.x </td><td>Working</td></tr>
    <tr><td>Provision VMs with VM Fusion 11 </td><td>Testing</td></tr>
    <tr><td>Provision ONTAP 9.x for Storage </td><td>Developing</td></tr>
    <tr><td>Create Kubernetes Cluster </td><td>Developing</td></tr>
    <tr><td>Create Pods & Containers </td><td>Future</td></tr>
    <tr><td>Provide Pod & Container Persistent Storage with NetApp Trident </td><td>Future</td></tr>
</table>

## Technologies

+ __Virtualization Platform__ (Choose one)
  +  <a href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMWorkstation Pro 15.x</a> 
  +  <a href="https://www.vmware.com/go/downloadfusion">VMFusion Pro 11</a>
+  __Operating Systems__ (At least one, your templates and VMs will be built off these)
   +  <a href="https://wiki.centos.org/Download">Centos 7</a>
      +  _Note: CentOS-7-x86_64-DVD-1908 was used in testing_
   +  <a href="http://releases.ubuntu.com/">Ubuntu 18</a>
      +  _Note: Ubuntu-18.04.4-live-server-amd64 was used in testing_
+ __Ansible__ (Choose one)
  + <a href="https://docs.ansible.com/">PAY FOR - Ansible Tower</a>
  + <a href="https://docs.ansible.com/">FREE - Ansible Core 2.9+</a>
  + <a href="https://github.com/ansible/awx">FREE - AWX 9.1.1+</a> 
    + This is an upstream project for Tower, a commercial derivative of AWX 
+ NetApp (Required if you're going to provide persistent storage to containers)
  + <a href="https://mysupport.netapp.com/site/tools/tool-eula/5e31797415040d3cce0033d3">OnTap Simulator - ONTAP 9.6+</a>
    + This can be replaced with any OnTap system
  + <a href="https://netapp-trident.readthedocs.io/en/stable-v20.01/">Trident 20.x+</a>
    + Required if you decide to use persistent storage from the OnTap system
+ Containerizaton Platform (At least one; required if you want to deploy containers)
  + <a href="https://www.docker.com/">Docker 1.10+</a> 
  + <a href="https://kubernetes.io/">Kubernetes 1.14+</a>
  
## Preparation
The following sections must be already installed in your environment.
- [ ] Decide which virtualization platform are you using:
  - [ ] Purchase and install VMWorkstation Pro 15.x+
  - [ ] Purchase and install Fusion Pro 11+
- [ ] Enable the REST interface for VMWorkstation or Fusion
    <br>__Note:__ _Make sure you perform the setup for the HTTPS services_<br>
    <img src="https://github.com/MarkMonterosso/vm-deployment/blob/master/imgs/vmworkstation/vmworkstation_rest.PNG" width=350>
  - [ ] <a href="https://docs.vmware.com/en/VMware-Workstation-Pro/15.0/com.vmware.ws.using.doc/GUID-C3361DF5-A4C1-432E-850C-8F60D83E5E2B.html">VM Workstation REST setup guide</a>
  - [ ] <a href="https://docs.vmware.com/en/VMware-Fusion/11/com.vmware.fusion.using.doc/GUID-63847178-3425-4D92-A043-EFBC1251C606.html">VM Fusion REST setup guide</a>
- [ ] Create your set of VM templates VM Workstation or Fusion (Linux Hosts Only)
        <br>_Example:<br> <img src="https://github.com/MarkMonterosso/vm-deployment/blob/master/imgs/vmworkstation/vmworkstation_templates.PNG"/>_
  - [ ] Templates mush have ssh keys setup to Ansible host
  - [ ] Templates must have only _**one**_ interface and configured as DHCP
  - [ ] Templates must be routable to your ansible installation

- [ ] Decide which implementation of Ansible you are using:
  - [ ] Download and install Ansible Core
  - [ ] Download and install AWX
  - [ ] Purchase and install Ansible Tower
- [ ] Repository Usage
  - [ ] It is recommended that you clone the contents of this repository into your own to avoid unexpected behavior due to future updates
    ```
    git clone https://github.com/MarkMonterosso/cirrocumulus.git    
    ```  
  - [ ] If you are using Tower or AWX it is recommended to create a project (<a href="https://github.com/MarkMonterosso/vm-deployment/blob/master/TOWER_AWX.md">Setup Guide</a>)
  - [ ] If you are using Ansible core, simply clone the repository and place it somewhere logical on your Ansible host
- [ ] Make sure the following packages on your ansible host
  ```
    re
    requests 
    json 
    sys 
    argparse
    traceback
    time
    netaddr
  ```
  
## Usage
__Ansible Core__
- [ ] Modify the vars-provision-infra.yml file
  - [ ] Follow the in-file documentation
- [ ] Execute the playbook<br>
    __Build the environment__
    ```
    ansible-playbook -i inventory <path>/cirrocumulus/ansible/provision-infra.yml    
    ```
    __Remove the environment__
    ```
    ansible-playbook -i inventory <path>/cirrocumulus/ansible/delete-infra.yml    
    ```
__Ansible AWX or Tower__<br>
- [ ] Coming Soon

## Author(s)
+ Mark Monterosso - NetApp Solutions Architect with focus on Automation & DevOps