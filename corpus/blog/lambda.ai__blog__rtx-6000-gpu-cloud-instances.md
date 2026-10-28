# 1, 2 & 4-GPU NVIDIA Quadro RTX 6000 Lambda GPU Cloud Instances

Source: https://lambda.ai/blog/rtx-6000-gpu-cloud-instances

Skip to main content

# 1, 2 & 4-GPU NVIDIA Quadro RTX 6000 Lambda GPU Cloud Instances

 October 29, 2020

 (Updated on August 12, 2022)

 • 4 min read

Starting today you can now spin up virtual machines with 1, 2, or 4 NVIDIA® Quadro RTX™ 6000 GPUs on Lambda's GPU cloud. We’ve built this new general purpose GPU instance type based on feedback we’ve collected from users over the past few months, and we are excited to finally bring it out of early access. With the new RTX 6000 instance types you can now expect:

- A lower price – Instances start @ $0.75 / hr to make experimenting easier
 
- More GPU VRAM – 24 GB of VRAM per card to support larger models
 
- More GPU options – The ability to choose between 1, 2, & 4 GPU configurations
 
- The latest software preinstalled – Tensorflow 2.3, PyTorch 1.6 & CUDA® 10
 
- 2x the performance per dollar – Versus a p3.8xlarge instance

## Lower Starting Price

With the new instances we’ve been able to lower the starting price of GPU compute on Lambda Cloud. Our 1-GPU instance now starts at $0.75 / hr compared to our previously lowest price Pascal based GPU instance that started at $1.50 / hr. The prices for the new instances are as follows:

- 1-GPU RTX 6000 @ $0.75 / hr
 
- 2-GPU RTX 6000 @ $1.50 / hr
 
- 4-GPU RTX 6000 @ $3.00 / hr

## Instance Specs

We heard a lot from customers about wanting more variety in choosing GPUs for their VMs as well as how much they benefited from the extremely fast NVMe storage and increased RAM on our 8-GPU V100 instances. So, with the new instances we wanted to make sure users have the best of both worlds.

1-GPU RTX 6000

- GPU: 1x RTX 6000 (24 GiB VRAM)
 
- CPU: 6 vCPUs @ 2.5 GHz
 
- RAM: 46 GiB
 
- Local NVMe Storage: 685 GiB (free space)
 
- Networking: 10 Gbps (burst)

2-GPU RTX 6000

- GPU: 2x RTX 6000 (24 GiB VRAM each)
 
- CPU: 12 vCPUs @ 2.5 GHz
 
- RAM: 92 GiB
 
- Local NVMe Storage: 1383 GiB (free space)
 
- Networking: 10 Gbps (burst)

4-GPU RTX 6000

- GPU: 4x RTX 6000 (24 GiB VRAM each)
 
- CPU: 24 vCPUs @ 2.5 GHz
 
- RAM: 184 GiB
 
- Local NVMe Storage: 2786 GiB (free space)
 
- Networking: 10 Gbps (burst)

## Up-to-date Frameworks and Drivers

The achilles heel of our now legacy 4-GPU Pascal based GPU instance was the lack of preinstalled up-to-date frameworks and drivers. While it wasn’t something we could address on the older instances, we’ve made sure our new instances come preinstalled with Tensorflow 2.3, PyTorch 1.6, Python 3.8, and CUDA 10. In addition, all machines come with a JupyterLab notebook environment and direct SSH access, so you can get started training right away.

## Price-to-Performance Comparison: Lambda Cloud 4-GPU RTX 6000 vs p3.8xlarge (4-GPU)

At Lambda we focus on providing cost effective and easy to use compute for machine learning researchers and engineers, so it was important that we do a price / performance benchmark of our 4-GPU on-demand instance against one of the most commonly available 4-GPU cloud instances, the p3.8xlarge.

To do this we first ran a comprehensive set of PyTorch model benchmarks on both our 4-GPU RTX 6000 instance and the p3.8xlarge. The benchmark covers a wide gamut of tasks including:  image classification, language models, machine translation, speech synthesis, and recommendation systems.

If we take the average of the performance difference between the two instances we see that the 4-GPU RTX 6000 instance performance is roughly 80% of what you might expect on the p3.8xlarge. However, the 4-GPU RTX 6000 instance is also roughly 40% the price of a p3.8xlarge instance ($3.00 / hr vs $12.24 / hr).

So, that means that the 4-GPU RTX 6000 GPU instance provides roughly 4x the performance per dollar of a comparable p3.8xlarge instance.

### Not a spot instance

Just like the rest of our instances the new RTX 6000 instances are not spot instances. So, even at the affordable prices, you have full on-demand access to instances without having to worry about them being terminated at an inconvenient moment.

## Getting Started

To get started with Lambda's GPU Cloud you can sign up here or, if you’re already a customer, sign in and launch a new 1, 2, or 4-GPU instance starting at $0.75 / hr.

## AUTHORED BY

 Remy Guercio

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
