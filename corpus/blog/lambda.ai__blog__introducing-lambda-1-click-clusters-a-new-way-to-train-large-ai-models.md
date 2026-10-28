# Introducing Lambda 1-Click Clusters, a new way to train large AI models

Source: https://lambda.ai/blog/introducing-lambda-1-click-clusters-a-new-way-to-train-large-ai-models

Skip to main content

# Introducing Lambda 1-Click Clusters, a new way to train large AI models

 June 3, 2024

 (Updated on August 16, 2024)

 • 5 min read

## Introducing Lambda 1-Click Clusters: 16 to 512 interconnected NVIDIA H100 Tensor Core GPUs. 

## Available on-demand. No long-term contracts required.

## Spinning up a short-term GPU cluster shouldn’t be so hard

In an ideal world, ML engineers and researchers working on large-scale training runs would have immediate access to hundreds of the latest-generation GPUs when they need them. Ease of access and use would be a given.

Reality check: 

- Until now, short-term access to GPU clusters in the cloud has only been available to the largest enterprises.

- Few ML teams need (and can afford) hundreds of top-end GPUs 24/7, for a full year or more. Instead, these teams often need a Hero Run on a cluster of tens to hundreds of GPUs for a few weeks to run an experiment, then a few weeks off to regroup and prepare for the next iteration.

Frustrating, isn’t it? We agree. And we think the time has come to break this paradigm.

## 1-Click Clusters: the time for on-demand GPU Clusters has come

Today, Lambda is introducing 1-Click Clusters: access multi-node clusters featuring 16 to 512 interconnected NVIDIA H100 Tensor Core GPUs with NVIDIA Quantum-2 InfiniBand 400 Gb/s — and with a reservation minimum of only one week. 

ML teams will no longer be forced to choose between flexibility and performance. No more choosing between wasting weeks of idle GPU time on a long-term contract or hoping an on-demand instance with many H100 GPUs will magically free up when it is needed most.

We believe that engineers’ time should be spent on core ML workflows — not infrastructure management:

- 1-Click Clusters are easy to request: reservations start right from Lambda’s On-Demand Cloud dashboard, guided by a wizard.

- Everything you need to start is pre-installed: 1-Click Clusters come with the Lambda Stack (which has over 100,000 users!); it contains all the AI frameworks engineers need to start immediately — PyTorch®, TensorFlow, NVIDIA CUDA, NVIDIA cuDNN, and NVIDIA drivers

## Lambda's ML Research team uses 1-Click Clusters

Our best test is to use 1-Click Clusters exactly like our users do: Lambda’s ML Research team is using a 4-node, 32-GPU 1-Click Cluster to fine-tune Open-Sora, a text-to-video open-source model, in order to generate brick-animated video clips. 

This project showcases the benefits of 1-Click Clusters, including their ease of use and high performance. With pre-installed software and shared storage, Lambda’s 1-Click Clusters allow engineers to focus on their core ML workflows instead of infrastructure management. The high-speed interconnected H100 GPUs in 1-Click Clusters make it an ideal platform for scaling the training of your own foundation models.

See the detailed steps and progress of Lambda’s Text2BrickAnime, iteration after iteration, on Weights & Biases. Get in touch with Lambda’s Chuan Li and his ML research team to discuss their work!

An astronaut walking on the moon, with the effects of gravity making the walk appear very bouncy

## DevOps teams will love Lambda’s 1-Click Clusters, too

Lambda focuses on infrastructure so you do not have to:

- 1-Click Clusters are from Lambda, by Lambda: we fully own the solution. We do not rely on another cloud, and Lambda’s own Datacenter Operations team handles support requests.

- Hop in and hop out: the whole point of 1-Click Clusters is to grant ML engineers and researchers access to 16-512 NVIDIA H100 Tensor Core GPUs within days, and for a minimum of only one week.

- No hidden costs: 

- Pricing is simple: $4.49 per GPU per hour.

- 3x head nodes (CPU-only) included with each cluster at no additional cost.

- Shared file system storage is $0.20 per GB per month - pay for usage only.

- No egress or ingress fees.

- Ready to geek out? 1-Click Clusters are engineered to take (an AI-sized) beating:

- Worker nodes are powered by the NVIDIA HGX H100 offering 8x NVIDIA H100 SXM GPUs interconnected with NVIDIA NVLink and NVSwitch, 208 vCPUs (104 cores), 1.9TB RAM, and 24TB local NVMe storage.

- Head node is 8 vCPUs, 34GB RAM, and 208GB local NVMe storage.

- NVIDIA Quantum-2 InfiniBand 400 Gb/s non-blocking rail-optimized compute fabric.

- 1:1 NVIDIA ConnectX-7 NIC to NVIDIA H100 GPU ratio.

- 3200 Gb/s node-to-node compute between worker nodes.

- In-band Ethernet networking providing up to 200 Gb/s.

- Two shared redundant 100Gb/s DIA (ISP) connections.

- 3 static public IP addresses per cluster, attached to head nodes with static NAT.

## Get started today!

Ready to train your mission-critical new foundation model today?
Sign in to your existing Lambda On-Demand Cloud account, or create an account and request a 1-Click Cluster! 🧙🧙‍♀️🧙‍

Need to have a conversation about 1-Click Clusters? Contact us here!

## AUTHORED BY

 Mitesh Agrawal

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
