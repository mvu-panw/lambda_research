# Setting up a Mellanox InfiniBand Switch (SB7800 36-port EDR)

Source: https://lambda.ai/blog/setting-up-a-mellanox-infiniband-switch-sb7800-36-port-edr

Skip to main content

# Setting up a Mellanox InfiniBand Switch (SB7800 36-port EDR)

 October 30, 2019

 (Updated on August 3, 2023)

 • 6 min read

The desired end-state of this tutorial, a running subnet manager on your switch.

This tutorial will walk you through the steps required to set up a Mellanox SB7800 36-port switch. The subnet manager discovers and configures the devices running on the InfiniBand fabric.[1] This tutorial will show you how to set it up via the command line or via the web browser.

## Enabling the subnet manager via the command line

### Step 1. Perform an arp-scan to determine the switch's IP address

sudo arp-scan --localnet

### Step 2. SSH into the switch and enable the subnet manager

The default username and password is admin / admin. Follow the instructions below to enable the configuration terminal and then enable the subnet manger.

$ ssh admin@10.1.10.136
Mellanox Onyx Switch Management

Password (type admin for the password):

Last login: Sun Apr 28 00:00:00 1989 from 10.1.10.100

Mellanox Switch

switch-hostname > enable

switch-hostname # configure terminal

switch-hostnam (config) # ib smnode my-sm enable

Your subnet manager should now be running.

## Enabling the subnet manager via the MLNX-OS Management web browser console

### Enabling the Subnet Manager via your web browser

The subnet manager must be enabled, or the lights will remain amber and the links will not start. To enable the subnet manager via the web browser:

- Navigate to the switch's IP (e.g. https://10.1.10.136 ); it's important to use HTTPS.

- Log in with username: admin / password: admin.

- Visit the IB SM Mgmt tab in the top navigation bar.

- Click Base SM.

- Check the checkbox next to the switch name and the checkbox "SM Enabled"

- Click Apply.

### Visual walkthrough of setting up the Subnet Manager via your web browser

Log into the subnet manager web console. The password is admin/admin.

Dismiss the welcome popup.

Click over to the IB SM Mgmt page and then > Base SM page

Checkmark the switch that you would like to enable the subnet manager on and then click the"SM Enabled" checkmark. Then click Apply.

Your local subnet manager should now be running. Confirm by looking at the top right part of the screen. It should say Subnet Manager is running.

## Citations

- https://docs.mellanox.com/display/MLNXOSv381000/Subnet+Manager

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
