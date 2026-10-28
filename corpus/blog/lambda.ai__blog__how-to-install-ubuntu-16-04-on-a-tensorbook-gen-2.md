# How to install Ubuntu 16.04/18.04 and Lambda Stack on a Tensorbook (Gen 2)

Source: https://lambda.ai/blog/how-to-install-ubuntu-16-04-on-a-tensorbook-gen-2

Skip to main content

# How to install Ubuntu 16.04/18.04 and Lambda Stack on a Tensorbook (Gen 2)

 November 6, 2018

 (Updated on August 3, 2023)

 • 1 min read

Many deep learning teams have software that depends on Ubuntu 16.04 (and not 18.04). However, the installation process for 16.04 has some quirks with the TensorBook. This tutorial walks you through the entire process of installing 16.04 from scratch with Lambda Stack.

- Download a version of the Ubuntu 16.04 ISO that is 16.04.5 or greater.
https://releases.ubuntu.com/16.04/

- Burn the ISO onto a USB drive. For a tutorial on this see here:
https://deeptalk.lambdalabs.com/t/create-usb-for-installing-ubuntu-18-04/482

- Insert the USB drive into the TensorBook and boot off of it by pressing [Del] during your boot sequence.

- Select Install Ubuntu in the GRUB menu and hit [e].

- Add the following text to the end of the linux line acpi_os_name=Linux acpi_osi= acpi_backlight=vendor modprobe.blacklist=nouveau. Hit [F10] to boot.

- Perform a normal installation of Ubuntu 16.04.5.

- Install Lambda Stack with this command:

LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && sudo apt-get install -y lambda-stack-cuda

That's it! You should now have a working TensorBook installed with Ubuntu 16.04.5 and Lambda Stack.

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
