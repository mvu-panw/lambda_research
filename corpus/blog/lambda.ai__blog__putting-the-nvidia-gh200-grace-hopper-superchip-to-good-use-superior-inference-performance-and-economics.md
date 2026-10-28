# Putting the NVIDIA GH200 Grace Hopper Superchip to good use: superior inference performance and economics for larger models

Source: https://lambda.ai/blog/putting-the-nvidia-gh200-grace-hopper-superchip-to-good-use-superior-inference-performance-and-economics

Skip to main content

# Putting the NVIDIA GH200 Grace Hopper Superchip to good use: superior inference performance and economics for larger models

 November 22, 2024

 • 6 min read

When it comes to large language model (LLM) inference, cost and performance go hand-in-hand. Single GPU instances are practical and economical; however, models that are too large to fit into a single GPU’s memory present a challenge: either move to multi-GPU instances and take a cost impact, or use CPU Offloading and take a performance impact, as exchanges between CPU and GPU become a bottleneck.

Fear no more. For engineers deploying Llama 3.1 70B as an example, the NVIDIA GH200 stands out as an excellent alternative to the NVIDIA H100 SXM Tensor Core GPU, delivering not only better performance but also superior cost efficiency on single GPU instances.

## 
8x better cost per token!

For our study, we have chosen to compare a single instance NVIDIA GH200 (now widely available at Lambda, on-demand) to a single instance NVIDIA H100 SXM, running inference with CPU Offloading.

 |  
 | Lambda 1x H100 SXM
 | Lambda 1x GH200

 | Chipset
 | NVIDIA H100 SXM Tensor Core GPU
 | 64 Core NVIDIA GRACE CPU with NVIDIA H100 GPU

 | Interconnect
 | N/A
 | NVLink-C2C @ 900 GB/s

 | DRAM
 | 225GiB
 | 432GiB LPDDR5X

 | GPU
 | 1x H100 GPU
 | 1x H100 GPU

 | VRAM
 | 80GB
 | 96GB HBM3

 | Local Disk
 | 2.75TiB
 | 4TiB

Both instances ran Llama 70B, with no quantization, using vLLM. Our benchmark is documented here and can easily be reproduced!

Here’s a look at how a single NVIDIA GH200 instance stacks up against a single NVIDIA H100 SXM instance for Llama 3.1 70B inferencing:

 |  
 | NVIDIA H100 SXM
 | NVIDIA GH200

 | Tensor parallel
 | 1
 | 1

 | CPU offload GB
 | 75
 | 60

 | Omp Num Threads
 | 104
 | 104

 | Max Seq Len
 | 4,096
 | 4,096

 | GPU cost per Hour
 | $3.29
 | $3.19

 | Tokens per Second
 | 0.57
 | 4.33

 | Cents per Token
 | 0.16
 | 0.02

For this use case, the NVIDIA GH200 Grace Hopper Superchip delivers 7.6x better throughput. Coupled with a slightly lower hourly cost, this translates into an 8x reduction in cost per token when using the GH200.

## 
Why Does This Matter for LLM Inferencing?

Inference workloads demand a combination of speed and cost efficiency. The GH200 delivers on both fronts, making it the optimal choice for:

- Cost-Conscious Deployments: Save significantly on operational expenses by sticking to single GPU instances when models are too large to fit in memory, without compromising throughput.

- Faster Processing: Get results in less time, enabling quicker application responses or pipeline throughput.

##  

## The gotchas of a novel infrastructure

These breakthroughs tie to GH200 being based on the NVIDIA Grace architecture - an ARM-based CPU.

The NVIDIA GH200 Superchip brings together a 72-core NVIDIA Grace CPU with an NVIDIA H100 Tensor Core GPU, connected with a high-bandwidth, memory-coherent NVIDIA NVLink-C2C interconnect. It offers up to 576GB of fast-access memory and delivers up to 900GB/s of total memory bandwidth through NVLink-C2C, which is 7x higher than the typical PCIe Gen5 speeds found in x86-based systems.

Interoperability between ARM and x86 architectures can be a challenge, with some of the libraries and tools still catching up with Grace. We’re actively capturing feedback from our GH200 users; here are two gotchas that will save you research time:

pip install torch failed!
pip install torch doesn't work out of the box for GH200 as PyTorch doesn’t have an officially supported build for the ARM architecture yet. To address this, Lambda has compiled PyTorch 2.4.1 for ARM and distributes it as part of Lambda Stack. 

To access the version of PyTorch included with Lambda Stack, we recommend creating a virtual environment that uses the --system-site-packages approach, and allow the virtual environment to have access to the system-wise installed PyTorch.

If you require a later version of PyTorch (>2.4.1), you would have to compile the specific PyTorch version for ARM in order to run on GH200. 

AssertionError: Torch not compiled with CUDA enabled! 
We typically see this error when a specific PyTorch version is pinned. For example, a requirements.txt file may contain torch==2.2.0, which conflicts with the PyTorch version (2.4.1) compiled for ARM on GH200. As PyTorch is largely backwards compatible, changing torch==2.2.0 to torch>=2.2.0 can address this issue. 

We note that there are situations where a specific PyTorch version is required such as PyTorch extensions (which are version-specific). In such a case, you would have to compile the required  pytorch version for ARM in order to run on GH200. 

You can find here a step-by-step guide to deploying Llama 3.1 with vLLM on an NVIDIA GH200 instance, with CPU Offloading.

## Get started with GH200!

If you're looking to optimize your infrastructure for LLM inference workloads, especially with larger models, the GH200 is a choice that keeps your bottom line and performance goals aligned.

The NVIDIA GH200 Grace Hopper Superchip is available on-demand on Lambda’s Public Cloud, at $3.19 per hour.
Sign-up and get started with your workflows in minutes or sign-in to your existing account.

Want to apply for a volume-based discount or reserved instances? Contact our Sales team.

## AUTHORED BY

 Thomas Bordes

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
