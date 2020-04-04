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
+ Required: <a href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMWorkstation 15.x</a> or <a href="https://www.vmware.com/go/downloadfusion">VMFusion 11</a>
+ Required: Ansible 2.9+
  + <a href="https://docs.ansible.com/">Ansible Tower (Paid)</a>
  + <a href="https://docs.ansible.com/">Ansible Core (Free)</a>
  + <a href="https://github.com/ansible/awx">AWX (Free)</a> - This is an upstream project for Tower, a commercial derivative of AWX 
+ Optional: NetApp
  + <a href="https://mysupport.netapp.com/site/tools/tool-eula/5e31797415040d3cce0033d3">NetApp OnTap Simulator</a>
  + <a href="https://netapp-trident.readthedocs.io/en/stable-v20.01/">Trident</a>
  
## Configuration

+ Download or clone this repository
    ```
    git clone https://github.com/MarkMonterosso/cirrocumulus.git    
    ```
+ Configuring for:
  + <a href="https://github.com/MarkMonterosso/vm-deployment/blob/dev/TOWER_AWX.md">AWX or Tower</a>
  + <a href="https://github.com/MarkMonterosso/vm-deployment/blob/dev/ANSIBLE.md">Ansible Core</a>
## Usage

## Versioning

## Contributing

## Authors
+ Mark Monterosso - NetApp Solutions Architect with focus on Automation & DevOps

## License

## Acknowledgements
