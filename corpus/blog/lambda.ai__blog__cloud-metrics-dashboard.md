# Introducing Lambda's Cloud Metrics Dashboard: Real-Time Insights for Your GPU Workloads

Source: https://lambda.ai/blog/cloud-metrics-dashboard

Skip to main content

# Introducing Lambda's Cloud Metrics Dashboard: Real-Time Insights for Your GPU Workloads

 May 15, 2025

 (Updated on April 6, 2026)

 • 4 min read

AI doesn’t wait and neither should real-time insights into your infrastructure! 

Monitoring cloud GPU workloads shouldn’t mean manually running nvidia-smi every five minutes and hoping your instance behaves.
If that hits a little too close to home, we’ve got good news.

At Lambda, we believe real-time visibility into your GPU performance should be seamless, automatic, and insightful. That’s why we built the Lambda Cloud Metrics Dashboard, powered by our lightweight Guest Agent. It gives you visibility into your infrastructure. No custom scripts or heavyweight monitoring plugins required.

## Why It Matters

AI training is expensive, in both time and GPU hours.

Underutilized GPUs waste valuable compute and inflate costs if you are running large-scale experiments. Without a dedicated GPU metrics platform, identifying performance bottlenecks becomes significantly more difficult.

Cloud Metrics Dashboard brings clarity to your training loop. With access to hardware-level metrics, it offers several key benefits:

- Real-Time Monitoring: Stay informed about your system's performance with up-to-the-minute data.

- Proactive Issue Detection: Identify and address potential problems before they impact your workloads.

- Optimized Resource Utilization: Make data-driven decisions to maximize efficiency and performance.

## What is the Lambda Cloud Metrics Dashboard?

The Lambda Cloud Metrics Dashboard helps you understand your GPU workloads in real-time without having to set up and maintain your own monitoring infrastructure. After you’ve installed the lambda-guest-agent on your On-Demand instances or 1-Click Clusters, you’ll be able to visualize key system metrics like GPU and VRAM usage, directly from your Lambda Cloud dashboard. This feature gives you immediate insights into your system's performance, helping you make informed decisions and quickly identify potential issues. 

List of available metrics on the dashboard:

- Average GPU utilization

- Average VRAM utilization across GPUs

- CPU Utilization

- Memory utilization

- Ethernet bandwidth

- Infiniband bandwidth

## Getting Started with the Guest Agent

For individual instances, setup is intentionally simple:

- SSH into your VM. Replace <IP-ADDRESS> with your VM's actual IP address:

ssh ubuntu@<IP-ADDRESS>

- Run the following command to download and install the Guest Agent:

 curl -L https://lambdalabs-guest-agent.s3.us-west-2.amazonaws.com/scripts/install.sh | sudo bash

- Verify Installation: Check that the Guest Agent is running

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

Once installed, the Guest Agent will begin collecting metrics that show up in your Cloud dashboard within minutes. 

For more detailed instructions, refer Guest Agent documentation.

## Security and Privacy

We take your data security seriously. The Guest Agent collects system metrics without storing any personally identifiable information. All data is transmitted securely to our internal metrics infrastructure and protected by strict authorization protocols. For transparency, the Guest Agent's source code is available in our Public GitHub Repository, and we include checksums with every release artifact.

Whether you’re fine-tuning or training, Lambda's Cloud Metrics Dashboard brings the data you need, right where you need it.

### Ready to See Your Metrics in Action?

Deploy the Guest Agent in minutes and start making every GPU cycle count. Get started now!

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
