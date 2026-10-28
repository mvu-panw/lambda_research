# NVIDIA GH200 Grace Hopper Superchips Now on Lambda and Available On-Demand

Source: https://lambda.ai/blog/announcing-gh200

Skip to main content

# NVIDIA GH200 Grace Hopper Superchips Now on Lambda and Available On-Demand

 November 14, 2024

 • 5 min read

We're excited to announce the launch of the NVIDIA GH200 Grace Hopper Superchip on Lambda On-Demand. Now, with just a few clicks in your Lambda Cloud account, you can access one of the most powerful and efficient accelerated computing platforms available in the cloud today. 

The NVIDIA GH200 Superchip brings together a 72-core NVIDIA Grace CPU with an NVIDIA H100 Tensor Core GPU, connected with a high-bandwidth, memory-coherent NVIDIA NVLink-C2C interconnect. It offers up to 576GB of fast-access memory and delivers up to 900GB/s of total memory bandwidth through NVLink-C2C, which is 7x higher than the typical PCIe Gen5 speeds found in x86-based systems.

The result? Up to 2x faster time-to-first-token (TTFT) with models like Llama3 70B[1].

 | 

 | 

Lambda Bare Metal

 | 

Lambda On-Demand GH200 Superchip

 | 

Chipset:

 | 

72-core NVIDIA Grace CPU with NVIDIA H100 GPU

 | 

64 Core NVIDIA GRACE CPU with NVIDIA H100 GPU

 | 

Interconnect

 | 

NVLink-C2C @ 900 GB/s

 | 

NVLink-C2C @ 900 GB/s

 | 

DRAM

 | 

480GiB LPDDR5X

 | 

432GiB LPDDR5X

 | 

GPU

 | 

1x H100 GPU

 | 

1x H100 GPU

 | 

VRAM

 | 

96GB HBM3

 | 

96GB HBM3

 | 

Local Disk

 | 

2 x 7.68TB E1.S

 | 

4TiB

## Precision Meets Speed

The NVIDIA GH200 Superchip allows for seamless, zero-copy data transfers between CPU and GPU memory, avoiding the bottlenecks typically associated with PCIe connections. For applications where low latency and high throughput are essential, such as multiturn LLM inference, the GH200 Superchip’s unified memory architecture efficiently supports larger context windows and reduces processing times for token generation.

In early testing, Abacus.ai recorded nearly a 2x improvement in latency over using NVIDIA H100 Tensor Core GPUs when running large-context inputs with a fine-tuned Llama 2 70B model, using only 4 NVIDIA GH200 nodes on Lambda. Leonardo.ai achieved over 3x throughput improvements over using NVIDIA A100 Tensor Core GPUs by porting an existing image captioning pipeline to Lambda’s NVIDIA GH200 Superchip cluster—demonstrating the impact of optimized performance on high-demand applications.

Ready to see the power of NVIDIA GH200 Grace Hopper Superchip firsthand? Follow our step-by-step PyTorch®-based benchmark on a GH200 Superchip guide in our docs and compare it across different cloud setups. Get set up, run your benchmarks, and easily analyze results to optimize your deep learning projects.

## Designed for Science at Scale

For scientific HPC workloads, the NVIDIA GH200 Superchip offers an optimal solution for simulation-intensive applications in fields like material science (e.g., ABINIT), fluid dynamics (e.g., OpenFOAM), and molecular dynamics (e.g., GROMACS). By integrating both CPU and GPU, the GH200 Superchip delivers the computational power needed to tackle complex, large-scale scientific challenges under budget.

## Scale Your AI and HPC Workloads with Lambda

As AI and HPC demands grow, so does the need for scalable compute resources. The NVIDIA GH200 Grace Hopper Superchip on Lambda On-Demand Cloud provides a high-performance, cost-effective solution for AI/ML and HPC teams. Whether you’re overcoming memory constraints or bandwidth limits, the GH200 Superchip is ready to power your next big project.

For those working on distributed training, Lambda is also offering 10x GH200 demo clusters with up to 720 Grace CPUs and 960GB of H100 GPU memory (6TB with memory coherency). To learn more about getting access to these clusters, schedule time with one of our engineers.

Get started with the GH200 Superchip on Lambda today to see firsthand how it can transform your AI and HPC workloads.

[1] NVIDIA Blog: NVIDIA GH200 Superchip Accelerates Inference by 2x in Multiturn Interactions with Llama Models [link]

## AUTHORED BY

 Nick Harvey

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
