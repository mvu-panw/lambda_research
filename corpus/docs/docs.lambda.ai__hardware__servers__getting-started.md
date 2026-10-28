# Getting started - Lambda Docs

Source: https://docs.lambda.ai/hardware/servers/getting-started/

Skip to content

Notice

Lambda sunset its consumer hardware business in Summer 2025. This
documentation is no longer maintained and is provided for reference only.

# Getting started#

## Where can I download the user manual for my server chassis?#

User manuals for Lambda server chassis can be downloaded below.

Tip

You can run sudo dmidecode -t 1 to know your server chassis. The command will output, for example:

# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 3.3.0 present.
# SMBIOS implementations newer than version 3.2.0 are not
# fully supported by this version of dmidecode.
Handle 0x0001, DMI type 1, 27 bytes
System Information
Manufacturer: Supermicro
Product Name: AS -1114CS-TNR
Version: 0123456789
Serial Number: S452392X2826686
UUID: 51605a00-c54f-11ec-8000-3cecefcdb48b
Wake-up Type: Power Switch
SKU Number: To be filled by O.E.M.
Family: To be filled by O.E.M.

Product Name is the server chassis. In this example, the server chassis is AS -1114CS-TNR.

### Supermicro#

 | Chassis
 | User manual

 | SuperServer 420GP-TNR
 | Download

 | AS -4124GO-NART
 | Download

 | AS -1124US-TNRP
 | Download

 | AS -1114CS-TNR
 | Download

 | AS -2124GQ-NART
 | Download

 | AS -4023S-TRT
 | Download

 | SuperServer 4029GP-TRT2
 | Download

 | SuperWorkstation 740GP-TNRT
 | Download

 | AS -2124US-TNRP
 | Download

 | SuperServer 420GP-TNAR
 | Download

 | SuperServer SYS-821GE-TNHR
 | Download

 | AS -8125GS-TNHR
 | Download

 | AS -4125GS-TNRT
 | Download

 | SuperServer SYS-421GE-TNRT
 | Download

### GIGABYTE#

 | Chassis
 | User manual

 | R152-Z33
 | Download

 | G292-Z43
 | Download

 | G292-Z24
 | Download

 | G292-Z22
 | Download

 | G292-Z42
 | Download

 | G292-280
 | Download

## Where do I find my server's serial number?#

See our video guide on how to find your server's serial number.

On the Supermicro server chassis, the serial number is on a service tag located at the front-bottom of the chassis.

Serial number on the service tag of a Supermicro server chassis

On GIGABYTE 2U server chassis, the serial number is on a sticker on the right side of the chassis.

On GIGABYTE 4U server chassis, the serial number is on a sticker on the left side of the chassis.

Serial number on a sticker on the left side of a GIGABYTE 4U server chassis

## Where can I find my server's IPMI (BMC) password?#

Tip

You can choose your own IPMI password for your server from within Ubuntu:

- Run sudo apt-get install ipmitool to install ipmitool, which is a program for managing IPMI functions.

- Run ipmitool user list 1 to view the user list. Confirm that ID 2 is admin or ADMIN.

- Run ipmitool user set password 2 to set a new IPMI password.

### Supermicro#

On Supermicro chassis, the IPMI password appears on one or more of the following:

- A sticker near the BMC (Baseboard Management Controller).

- A sticker near the motherboard serial number label.

- The service tag.

See Supermicro's
 BMC Unique Password Guide
for more information.

### GIGABYTE#

On GIGABYTE chassis, the IPMI password appears on one or more of the following:

- A sticker affixed to the motherboard.

- The chassis itself.

See GIGABYTE's
 BMC Unique Pre-Programmed Password Reference Guide
for more information.

## What are the power requirements for my server's PSUs?#

The power requirements for Lambda server power supply units (PSUs) are as follows:

 | Manufacturer
 | Model
 | Wattage
 | Voltage (AC)
 | Current (A)
 | Frequency (Hz)
 | Inlet/Outlet
 | Efficiency

 | Supermicro
 | PWS-2K05A-1R
 | 1000
 | 100-127
 | 12-9.5
 | 60/50
 | C14/C13
 | 80 Plus Titanium (> 96%)

 | 
 | 
 | 1800
 | 200-220
 | 10-9.5
 | 60/50
 | 
 | 

 | 
 | 
 | 1980
 | 220-230
 | 10-9.8
 | 60/50
 | 
 | 

 | 
 | 
 | 2000
 | 230-240
 | 10-9.8
 | 60/50
 | 
 | 

 | Supermicro
 | PWS-2K08A-1R
 | 1800
 | 200-220
 | 10-9.8
 | 60/50
 | C14/C13
 | 80 Plus Titanium (> 96%)

 | 
 | 
 | 1980
 | 220-230
 | 10-9.8
 | 60/50
 | 
 | 

 | 
 | 
 | 2000
 | 230-240
 | 10-9.8
 | 60/50
 | 
 | 

 | Supermicro
 | PWS-3K02G-2R
 | 2880
 | 200-207
 | 16-15.7
 | 60/50
 | C20/C19
 | 80 Plus Titanium (> 96%)

 | 
 | 
 | 3000
 | 207.1-240
 | 16-14.5
 | 60/50
 | 
 | 

 | Supermicro
 | PWS-3K06G-2R
 | 3000
 | 207.1-240
 | 16-14.5
 | 60/50
 | C20/C19
 | 

This is what C13 outlets and C14 inlets look like:

C13 outlet and C14 inlet

This is what C19 outlets and C20 inlets look like:

C19 outlet and C20 inlet

 Back to top
