# Guest Agent - Lambda Docs

Source: https://docs.lambda.ai/public-cloud/guest-agent/

Skip to content

# Guest Agent#

## Introduction#

The lambda-guest-agent (Guest Agent) is a service you can install on both
Lambda Cloud on-demand instances and 1-Click Cluster (1CC) nodes. For
simplicity, this documentation refers to both types of systems as virtual
machines (VMs). The Guest Agent collects system metrics, such as GPU and VRAM
utilization, and sends them to Lambda's backend. You can then view these metrics
in the the
Lambda Cloud console.

Note

The metrics dashboard will be generally available in the Lambda Cloud console in
Q2 of 2025. To request early access, submit a support ticket.

## Install the Guest Agent#

To install the Guest Agent:

- 

SSH into your VM. Replace <IP-ADDRESS> with the actual IP address of your
 VM:

ssh ubuntu@<IP-ADDRESS>

- 

Download and install the Guest Agent:

curl -L https://lambdalabs-guest-agent.s3.us-west-2.amazonaws.com/scripts/install.sh | sudo bash

- 

Confirm that the Guest Agent is running:

sudo systemctl --no-pager status lambda-guest-agent*

You should see output similar to:

● lambda-guest-agent.service - Lambda metrics and observability agent
 Loaded: loaded (/etc/systemd/system/lambda-guest-agent.service; enabled; vendor preset: enabled)
 Active: active (running) since Mon 2024-10-28 20:58:44 UTC; 18s ago
Main PID: 68284 (telegraf)
 Tasks: 18 (limit: 271525)
 Memory: 11.5M
 CPU: 572ms
 CGroup: /system.slice/lambda-guest-agent.service
 └─68284 /usr/local/bin/lambda/guest-agent/telegraf -config /etc/lambda/guest-agent/telegraf/telegraf.conf

● lambda-guest-agent-updater.timer - Lambda metrics and observability agent updater
 Loaded: loaded (/etc/systemd/system/lambda-guest-agent-updater.timer; enabled; vendor preset: enabled)
 Active: active (waiting) since Mon 2024-10-28 20:58:44 UTC; 18s ago
Trigger: Tue 2024-11-05 10:27:09 UTC; 1 week 0 days left
Triggers: ● lambda-guest-agent-updater.service

Oct 28 20:58:44 192-222-52-58 systemd[1]: Started Lambda metrics and observability agent updater.

● lambda-guest-agent-updater.service - Lambda metrics and observability agent updater
 Loaded: loaded (/etc/systemd/system/lambda-guest-agent-updater.service; enabled; vendor preset: enabled)
 Active: active (exited) since Mon 2024-10-28 20:58:50 UTC; 12s ago
TriggeredBy: ● lambda-guest-agent-updater.timer
Process: 68290 ExecStart=/bin/bash /usr/local/bin/lambda/guest-agent/guest-agent-update.sh (code=exited, status=0/SUCCESS)
Main PID: 68290 (code=exited, status=0/SUCCESS)
 CPU: 4.845s

Your metrics should appear in the Lambda Cloud console within a few minutes.

## Updating the Guest Agent#

The Guest Agent automatically updates itself every two weeks. To disable
automatic updates, stop and disable the lambda-guest-agent-updater.timer
systemd unit:

sudo systemctl stop lambda-guest-agent-updater.timer
sudo systemctl disable lambda-guest-agent-updater.timer

## Uninstalling the Guest Agent#

To uninstall the Guest Agent, run:

sudo apt remove lambda-guest-agent

## Security#

The guest agent collects and measures attributes of your system. We store these
metrics in our internal metrics infrastructure that we gate behind strict authorization
schemes.

The source code for guest-agent is available in our public Github mirror.
We publish checksums of the release artifacts in the Releases page
that you can use to verify the integrity of the downloaded artifacts.

### Data privacy#

Lambda takes your data privacy seriously. When you install lambda-guest-agent, we forward
your metrics to our internal metrics infrastructure. Lambda does not store any
personally identifying information in our metrics backend. The only customer-specific
identifier we store is a unique ID that will only be used to allow lambda.ai
to gather your specific data once visualizations are available there. We do not store names,
email addresses, street addresses, billing information, VM hostnames, or any other
personally-identifying information on our metrics backend beyond what is
necessary to serve your data to you.

 Back to top
