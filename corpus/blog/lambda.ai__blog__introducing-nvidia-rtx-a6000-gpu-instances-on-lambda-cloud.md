# Introducing NVIDIA RTX™ A6000 GPU Instances on Lambda Cloud

Source: https://lambda.ai/blog/introducing-nvidia-rtx-a6000-gpu-instances-on-lambda-cloud

Skip to main content

# Introducing NVIDIA RTX™ A6000 GPU Instances on Lambda Cloud

 April 23, 2021

 (Updated on July 24, 2023)

 • 2 min read

Update: 1-GPU NVIDIA RTX A6000 instances, starting at $1.00 / hr, are now available

Launch your 1x RTX A6000 instance

We are excited to announce that Lambda GPU Cloud is the first public cloud to offer instances with 1x, 2x, and 4x NVIDIA RTX A6000 GPUs! What’s new:

- First cloud NVIDIA RTX A6000s, providing great price to performance value

- ~2x average performance improvement over our previous 1x, 2x & 4x NVIDIA RTX 6000 instances

- 48 GiB of VRAM per GPU for higher memory workloads and larger batch sizes

- NVLink support between pairs of GPUs for faster GPU-to-GPU communication

- Up to 200 Gbps of inter-node bandwidth for faster multi-node training

## Specs & pricing

Our new 1, 2, and 4 GPU instances are powered by AMD EPYC™ 7502 CPUs and paired with high speed NVMe offering up to 6x the performance of standard SATA3 SSDs. These VMs have been designed and built to be great for general purpose, high memory, and multi-node workloads.

1-GPU NVIDIA RTX A6000 @ $1.00 / hr

- GPU: 1x NVIDIA RTX A6000 (48 GiB VRAM )

- CPU: 14 vCPUs @ 2.5 GHz

- RAM: 100 GiB

- Temporary Storage: 200 TiB NVMe

- Node-to-node Bandwidth: Up to 50 Gbps

- Internet Bandwidth: Up to 10 Gbps

2-GPU NVIDIA RTX A6000 @ $2.00 / hr

- GPU: 2x NVIDIA RTX A6000 + NVLink (48 GiB VRAM each)

- CPU: 28 vCPUs @ 2.5 GHz

- RAM: 200 GiB

- Temporary Storage: 1 TiB NVMe

- Node-to-node Bandwidth: Up to 200 Gbps

- Internet Bandwidth: Up to 10 Gbps

4-GPU NVIDIA RTX A6000 @ $4.00 / hr

- GPU: 4x NVIDIA RTX A6000 + NVLink (48 GiB VRAM each)

- CPU: 56 vCPUs @ 2.5 GHz

- RAM: 400 GiB

- Temporary Storage: 1 TiB NVMe

- Node-to-node Bandwidth: Up to 200 Gbps

- Internet Bandwidth: Up to 10 Gbps

## Performance & benchmarks

With each new generation of GPU instances we aim to provide an even better value than the previous generation. Our NVIDIA RTX A6000 instances are no exception, and we’ve been able to provide on-demand price to performance numbers that beat p3.8xlarge instances by an average of 150% and even our existing already affordable NVIDIA RTX 6000 instances by an average of 10%.

To calculate the performance figures we trained a handful of different models using PyTorch with FP32 precision and averaged out the numbers across the comparable 4 GPU instance types.

### Savings without yearly contract lock-in

Our new NVIDIA RTX A6000 instances not only provide more performance per dollar than on-demand p3.8xlarge instances, but they still provide an average of 60% more performance per dollar spent vs 1 year reserved instance. Even when the entire year is being paid upfront!

## AUTHORED BY

 Remy Guercio

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
