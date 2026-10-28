# More Options for AI Developers: New On-Demand 1x, 2x and 4x NVIDIA H100 SXM Tensor Core GPU Instances in Lambda’s Cloud

Source: https://lambda.ai/blog/creating-more-options-for-ai-developers-new-1x-2x-and-4x-sxm

Skip to main content

# More Options for AI Developers: New On-Demand 1x, 2x and 4x NVIDIA H100 SXM Tensor Core GPU Instances in Lambda’s Cloud

 October 7, 2024

 • 7 min read

## Opening up options: higher-end GPUs in smaller chunks

We're excited to announce the launch of new 1x, 2x, and 4x NVIDIA H100 SXM Tensor Core GPU instances in our Public Cloud. These instances bring new options for AI Developers seeking to leverage the performance of SXM GPUs, and provision the right-sized GPU acceleration for their workloads.

## 49% to 51% performance gains

The new 1x, 2x and 4x instances are based on NVIDIA H100 SXM Tensor Core GPUs, which offer 67.5% faster memory bandwidth and up to 2 times higher power draw over the PCIe version.

 | Feature
 | NVIDIA H100 PCIe Tensor Core GPU
 | NVIDIA H100 SXM Tensor Core GPU

 | Form Factor
 | PCIe Gen 5
 | SXM5

 | Memory Bandwidth
 | 2 TB/s
 | 3.35 TB/s

 | L2 Cache
 | 50 MB
 | 50 MB

 | Transistors
 | 80 billion
 | 80 billion

 | GPU Memory
 | 80 GB
 | 80 GB

 | Memory interface
 | 5120-bit HBM2e
 | 5120-bit HBM3

 | Interconnect
 | NVLink: 600 GB/s
PCIe Gen5 128 GB/s
 | NVLink: 900 GB/s
PCIe Gen5 128 GB/s

 | Maximum Thermal Design Power (TDP)
 | 300-350W
 | Up to 700W

Looking at a geomean of results from pytorch-train-throughput-fp16 and pytorch-train-throughput-TF32, we observe a 49% to 51% performance premium for the NVIDIA H100 SXM Tensor Core GPU, over the PCIe version.

Geomean is calculated on ssd, bert_base_squad, bert_large_squad, gnmt, resnet50, tacotron2 and waveglow scores. You can view individual benchmarks at https://lambdalabs.com/gpu-benchmarks. 

Note that Ethernet is used for the 2x and 4x instances. If you are looking for NVIDIA Quantum-2 InfiniBand networking, then 1-Click Clusters are the way to go.

## More affordable options

The introduction of the new 1x, 2x and 4x NVIDIA H100 SXM Tensor Core GPU instances creates a solid set of options for AI Developers, to find the right compute at the right price for their workloads.

 | Instance
 | Availability
 | On-Demand $ / GPU / Hr

 | 1x NVIDIA H100 PCIe Tensor Core
 | Existing
 | $2.49

 | 1x NVIDIA H100 SXM Tensor Core
 | New
Up to 51% faster than PCIe!
 | $3.29

 | 2x NVIDIA H100 SXM Tensor Core
 | New
 | $3.19

 | 4x NVIDIA H100 SXM Tensor Core
 | New
 | $3.09

 | 8x NVIDIA H100 SXM Tensor Core
 | Existing
 | $2.99

##  

## Get started & win 6 months of free compute!

The new instances arrive right on time to support your bid for Lambda’s Golden Ticket: a chance for you and your team to win full-time access, for six months, to a 96GB VRAM NVIDIA GPU instance – absolutely free!

Jump in fast - the Golden Ticket is only in October! Learn more.

The new instances are available immediately and on-demand, in Lambda’s Public Cloud. Sign-up and get started with your workflows in minutes or sign-in to your existing account.

Planning to use 64+ GPUs (monthly average) and want to apply for a volume-based discount? 
Contact our Sales team.

## AUTHORED BY

 Mitesh Agrawal

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
