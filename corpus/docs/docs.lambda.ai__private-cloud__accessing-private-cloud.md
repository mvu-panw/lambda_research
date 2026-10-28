# Accessing your Lambda Private Cloud cluster - Lambda Docs

Source: https://docs.lambda.ai/private-cloud/accessing-private-cloud/

Skip to content

# Accessing your Lambda Private Cloud cluster#

## Introduction#

Lambda Private Cloud
clusters use Fortinet FortiGate firewall appliances
to enable secure VPN access. To access your Private Cloud cluster through the
firewall, you must first install and configure FortiClient VPN (FortiClient).

## Download and install FortiClient#

Download and install the appropriate FortiClient package for your computer:

- Download for Windows

- Download for MacOS

- Download for Ubuntu (and other .deb-based distributions)

- Download for Red Hat (and other .rpm-based distributions)

FortiClient for other devices, including ARM64 systems, can be downloaded from
Fortinet's
product downloads
page.

## Configure the VPN connection#

Next, you'll configure FortiClient using the credentials provided in your
1Password vault, which looks like:

- 

Open FortiClient.

- 

Click Configure VPN.

- 

In the New VPN Connection window, enter the following settings:

- VPN: Select SSL-VPN.

- Connection Name: Enter a descriptive name for the VPN connection.

- (Optional) Description: Enter a description for the VPN connection.

- Remote Gateway: Enter the VPN URL from your 1Password vault. Omit the
 port number.

- Select the Customize port checkbox and enter the VPN URL port number.

- Clear the Enable Single Sign On (SSO) for VPN Tunnel checkbox.

- Client Certificate: Select None.

- Authentication: Select Prompt on login.

- Clear the Enable Dual-stack IPv4/IPv6 address checkbox.

Your configuration should look like this:

- 

Click Save.

- 

In the main window, select the VPN connection you just created from the
 dropdown menu:

- 

Enter the Username and Password provided in your 1Password vault.

- 

Click Connect.

You're asked to confirm that you want to connect to the VPN:

- 

Verify that the certificate fingerprint matches the fingerprint shown in your
 1Password vault. Then, click Accept.

You're connected to your Private Cloud cluster when FortiClient shows the VPN
connection is active:

## Next steps#

- Learn about Lambda Private Cloud clusters.

- Learn about Lambda 1-Click Clusters.

 Back to top
