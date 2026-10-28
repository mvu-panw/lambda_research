# Getting started - Lambda Docs

Source: https://docs.lambda.ai/hardware/workstations/getting-started/

Skip to content

Notice

Lambda sunset its consumer hardware business in Summer 2025. This
documentation is no longer maintained and is provided for reference only.

# Getting started#

See our video on Lambda's line of Vector desktops and workstations.

See our quick start video guide.

## What are the buttons and ports at the front and top of my Vector One?#

Your Vector One's power button is located at the front-top.

The first button at the top, closest to the front, switches between the
various RGB modes. The second button at the top changes the color.

The first port at the top, closest to the front, is used to connect USB-C 3.1
devices. The following 2 ports are used to connect USB-A 3.0 devices.

The jack at the top is used to connect a headset/microphone.

## How do I fix Wi-Fi issues with my Vector One?#

There are
known issues in Ubuntu with the Wi-Fi adapter
installed in Vector Ones. In some cases, the Wi-Fi adapter isn't detected at
all. In other cases, the Wi-Fi adapter is detected but exhibits slow
performance. These issues are fixed in updated firmware for the Wi-Fi adapter.

In order to download and install the updated firmware, you need to connect
your Vector One to the Internet.

If your Wi-Fi adapter isn't detected at all, try booting using a previous
kernel version. Your Wi-Fi adapter might be detected and you can download the
updated firmware.

Note

You can also connect your Vector One to the Internet using Ethernet
(recommended), a USB Wi-Fi adapter, or by tethering your iPhone or Android
phone.

Once your Vector One is connected to the Internet, open a terminal and run:

sudo apt update && sudo apt upgrade -y

Then, reboot your Vector One.

## Where can I download recovery images for my workstation?#

Workstation recovery images can be downloaded from our Lambda Stack and
recovery images docs page.

## Can I dual boot Ubuntu and Windows 11?#

You can't dual boot Ubuntu and Windows 11. You can have either Ubuntu or Windows
installed, but not both at the same time on your workstation.

Windows 11 requires Secure Boot and TPM 2.0 to be enabled,
which can prevent Ubuntu from booting or detecting your workstation's GPUs.

## How do I set the fan speeds for my workstation?#

See our video guide on adjusting fan curves on your Vector.

You can set baseline fan speeds for your workstation using ipmitool. Once
baseline fan speeds are set, you can fine-tune the fan speeds in the web-based
IPMI interface.

Note

These instructions are only for workstations using an ASUS Pro WS WRX80E-SAGE
SE WIFI motherboard.

Before proceeding with these instructions, run sudo dmidecode -t 2 | grep Name
to confirm your workstation uses the above motherboard. You should see:
Product Name: Pro WS WRX80E-SAGE SE.

First, install ipmitool by running:

sudo apt -y update && sudo apt -y install ipmitool

Then, set the baseline fan speeds by running:

sudo ipmitool raw 0x30 0x0E 0x04 0x00 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64 && \
sudo ipmitool raw 0x30 0x0E 0x04 0x01 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64 && \
sudo ipmitool raw 0x30 0x0E 0x04 0x02 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64 && \
sudo ipmitool raw 0x30 0x0E 0x04 0x03 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64 && \
sudo ipmitool raw 0x30 0x0E 0x04 0x04 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64 && \
sudo ipmitool raw 0x30 0x0E 0x04 0x05 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64 && \
sudo ipmitool raw 0x30 0x0E 0x04 0x06 0x32 0x23 0x49 0x46 0x5a 0x64 0x61 0x64 0x61 0x64

Tip

See the ASUS ASMB9-iKVM Fan Customized Mode User
Guide
to learn how to customize fan speeds in the web-based IPMI interface.

Note that Lambda workstations are high-performance systems and generate
plenty of heat. For this reason, it's not recommended to use the guide's
power efficiency fan policy.

## What are the power requirements for my workstation's PSU?#

Warning

Lambda workstations are high-performance systems and use a large amount of
power. For this reason, Lambda workstations can't reliably be used with
uninterruptible power supplies (UPSs, or battery backups).

If you use a UPS with your workstation, you might experience system
instability and trouble booting.

The power requirements for Lambda workstation power supply units (PSUs) are as
follows:

Note

The manufacturer and model of your workstation’s PSU appears on the label
on the PSU.

 | Manufacturer
 | Model
 | Wattage
 | Voltage (AC)
 | Current (A)
 | Frequency (Hz)
 | Inlet/Outlet

 | Super Flower
 | SF-1300F14MG V1.0
 | 1300
 | 100-240
 | 15
 | 60/50
 | C14/C13

 | Super Flower
 | SF-1600F14HT
 | 1600
 | 115-240
 | 17-10
 | 60/50
 | C20/C19

 | Super Flower
 | SF-2000F14HP
 | 2000
 | 200-240
 | 15
 | 50
 | C20/C19

## How do I upgrade my Samsung 980 PRO NVMe SSD's firmware?#

Follow these instructions to upgrade your Samsung 980 PRO NVMe SSD's firmware.

Warning

Samsung 980 PRO NVMe SSDs with the older 3B2QGXA7 firmware are known to
fail.

To know if your SSD is using the 3B2QGXA7 firmware, install the
smartmontools package by running sudo apt -y install smartmontools.
Then, run sudo smartctl -a /dev/nvme0.

If your SSD is using the 3B2QGXA7 firmware, it's recommended that you
upgrade the firmware as soon as possible.

First, download the latest firmware ISO from Samsung's website by running:

wget https://semiconductor.samsung.com/resources/software-resources/Samsung_SSD_980_PRO_5B2QGXA7.iso

Next, run sudo -s to open a shell with root (administrator) privileges.

Finally, run:

mkdir /mnt/iso && mount -o loop Samsung_SSD_980_PRO_5B2QGXA7.iso /mnt/iso && \
mkdir fwupdate && cd fwupdate && \
gzip -dc /mnt/iso/initrd | cpio -idv --no-absolute-filenames && \
cd root/fumagician && ./fumagician

The above command mounts the firmware upgrade ISO, extracts the firmware
upgrade, and launches the upgrade.

After the firmware upgrade completes, restart your computer.

Run sudo smartctl -a /dev/nvme0 to confirm your SSD is using the new
firmware.

 Back to top
