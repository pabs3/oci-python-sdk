# Usage2ADW - Oracle Cloud Infrastructure Usage and Cost Reports to Autonomous Database with APEX Reporting

## Step by Step Manual installation Guide on OCI VM and Autonomous Data Warehouse Database
usage2adw is a tool which uses the Python SDK to extract the usage reports from your tenant and load it to Oracle Autonomous Database.

Oracle Application Express (APEX) will be used for reporting.  

**DISCLAIMER – This is not an official Oracle application,  It does not supported by Oracle Support, It should NOT be used for utilization calculation purposes, and rather OCI's official 
[cost analysis](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/costanalysisoverview.htm) 
and [usage reports](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/usagereportsoverview.htm) features should be used instead.**

**Developed by Adi Zohar, 2020-2021**

## 1. Deploy VM Compute instance to run the python script
```
   OCI -> Menu -> Compute -> Instances
   Create Instance
   --> Name = UsageVM
   --> Image = Oracle Linux 7
   --> Shape = VM.Standard2.1
   --> Choose your network VCN and Subnet (any type of VCN and Subnet)
   --> Assign public IP -  Optional if on public subnet
   --> Add your public SSH key
   --> Press Create
```
![](img/Image_01.png)

![](img/Image_02.png)

![](img/Image_03.png)

```
   Copy Instance Info:
   --> Compute OCID to be used for Dynamic Group Permission
   --> Compute IP
```

## 2. Create Dynamic Group for Instance Principles

```
   OCI -> Menu -> Identity -> Dynamic Groups -> Create Dynamic Group
   --> Name = UsageDownloadGroup 
   --> Desc = Dynamic Group for the Usage Report VM
   --> Rule 1 = ANY { instance.id = 'OCID_Of_Step_1_Instance' }
```
![](img/Image_04.png)

## 3. Create Policy to allow the Dynamic Group to extract usage report and read Compartments

```
   OCI -> Menu -> Identity -> Policies
   Choose Root Compartment
   Create Policy
   --> Name = UsageDownloadPolicy
   --> Desc = Allow Dynamic Group UsageDownloadGroup to Extract Usage report script
   Statements:
   define tenancy usage-report as ocid1.tenancy.oc1..aaaaaaaaned4fkpkisbwjlr56u7cj63lf3wffbilvqknstgtvzub7vhqkggq
   endorse dynamic-group UsageDownloadGroup to read objects in tenancy usage-report
   Allow dynamic-group UsageDownloadGroup to inspect compartments in tenancy
   Allow dynamic-group UsageDownloadGroup to inspect tenancies in tenancy
   *** Please don't change the usage report tenant OCID, it is fixed.
```

![](img/Image_05.png)

## 4. Deploy Autonomous Data Warehouse Database

```
   OCI -> Menu -> Autonomous Data Warehouse
   Create Autonomous Database
   --> Compartment = Please Choose
   --> Display Name = ADWCUSG
   --> Database Name ADWCUSG
   --> Workload = Data Warehouse
   --> Deployment = Shared
   --> Always Free = Optional
   --> OCPU = 1
   --> Storage = 1
   --> Auto Scale = No
   --> Password = We1lc2om3e#4 (Please choose your own password)
   --> Choose Network Access = Allow secure Access from Everywhere (you can use VCN as well which requires NSG)
   --> Choose License Type
```

![](img/Image_06.png)

![](img/Image_07.png)

![](img/Image_08.png)

![](img/Image_09.png)

## 5. Login to Linux Machine

```
   Using the SSH key you provided, SSH to the linux machine from step #1
   ssh opc@UsageVM
```

## 6. Run Install Packages Script from Github

The script will install Python3, Git and python packages - oci, oci-cli, cx_Oracle and requests
Install Oracle Database Instance Client, Update bashrc and Clone the Python SDK
```
   # on oci github:
   bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-python-sdk/master/examples/usage_reports_to_adw/setup/setup_packages.sh)"
```

## 7. Setup Credentials

This script will ask for Database Name, Admin Password, Application Password and Extract Start Date

```
   /home/opc/usage_reports_to_adw/setup/setup_credentials.sh
```
   
## 8. Download Autonomous database Wallet

```
   # on Linux -> create folder $HOME/ADWCUSG
   mkdir $HOME/ADWCUSG

   # On OCI -> MENU -> Autonomous Data Warehouse -> ADWCUSG
   --> Service Console
   --> Administration
   --> Download Client Credential
   --> Specify the Admin Password
   --> Copy the Wallet wallet_ADWCUSG.zip to the Linux folder /home/opc with the name wallet.zip
```

![](img/Image_10.png)

## 9. Check OCI Connectivity and setup database users and apex

```
   # Execute:
   /home/opc/usage_reports_to_adw/setup/setup_usage2adw.sh
   
```

## 10. Open Autonomous Database APEX Workspace Admin

```
    OCI Console -> Autonomous Databases -> ADWCUSG -> Service Console
    Development Menu -> Oracle APEX
    Choose Workspace Login.

    Workspace = Usage
    User = Usage
    Password = Password you defined for the application


```
![](img/Image_16.png)

## 11. Login to Apex Application

```
    Press on App Builder on the Left side
    Press on the application "Usage and Cost Report"
    Execute the application
    Bookmark this page for future use

    User = Usage
    Password = Password you defined for the application

```
![](img/Image_30.png)


## 12. How to create additional End User Accounts

```
   Login to Workspace Managament 
   Top 3rd Right Menu -> Manage Users and Groups
   --> Create User
   
   Fill:
   --> Username
   --> Email
   --> Password
   --> Confirm Password
   --> Optional - Require to change passqword = No
   --> Apply Changes
```

![](img/Image_19.png)

![](img/Image_20.png)

![](img/Image_21.png)

![](img/Image_22.png)
   

## 13. How to change Autonomous Database to Private End Point

Login to OCI Console -> Menu -> Oracle Database -> Autonomous Database

Choose The Autonomous database for Usage2ADW

More Actions Menu -> Update Network Access

![](img/pe1.png)

#### Update Network Access

Choose Network Access -> Private endpoint access Only

Choose Network security group that will assigned to the Autonomous database

If you don't have Network Security Group, Go to the Virtual Cloud Network and Create one.

Make sure you allow port 1522/TCP inbound traffic.

![](img/pe2.png)

#### Update VM tnsnames to the private endpoint

Find the Private Endpoint URL:

![](img/pe3.png)

Login to the usage2adw virtual machine using ssh tool with opc user

cd ADWCUSG

Edit tnsnames.ora file and change the tnsnames *_low entry host to the private end point specify in the ADW page

## 19. How to add multiple tenants

Login to Usage2adw VM

```
   # setup oci tenant configuration
   oci setup config
   Enter a location for your config [/home/opc/.oci/config]: ( Press Enter) 
   Do you want add a profile here - Press Y
   Name of the profile - Enter the tenant name
   Complete the rest of the questions based on the user authentication

   # update run_multi_daily_usage2adw.sh
   cd /home/opc/usage_reports_to_adw/shell_scripts
   vi run_multi_daily_usage2adw.sh

   # scroll to the bottom and add lines per tenant profile, you can specify different tagspecial1 and tagspecial2 if different then the main tenant
   run_report tenant2 tagspecial1 tagspecial2
   run_report tenant3 tagspecial1 tagspecial2
```

## 20. How to upgrade the usage2adw application and APEX
```
   # on oci github:
   bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-python-sdk/master/examples/usage_reports_to_adw/setup/setup_upgrade_usage2adw.sh)"    
```


## License

Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl
or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
