# Introducing NVIDIA SHARP on Lambda 1CC: Next-Gen Performance for Distributed AI Workloads

Source: https://lambda.ai/blog/nvidia-sharp-on-lambda-1cc

Skip to main content

# Introducing NVIDIA SHARP on Lambda 1CC: Next-Gen Performance for Distributed AI Workloads

 July 29, 2025

 (Updated on November 5, 2025)

 • 5 min read

Lambda’s 1-Click Clusters(1CC) provide AI teams with streamlined access to scalable, multi-node GPU clusters, cutting through the complexity of distributed infrastructure. Now, we're pushing the envelope further by integrating NVIDIA's Scalable Hierarchical Aggregation and Reduction Protocol (SHARP) into our multi-tenant 1CC environments. This technology reduces communication latency and improves bandwidth efficiency, directly accelerating training speed of distributed AI workloads.

## What is NVIDIA SHARP? Why Should You Care?

SHARP is NVIDIA’s breakthrough technology that offloads collective communication operations like allReduce, from CPUs and GPUs directly onto the NVIDIA Quantum InfiniBand network. Why does that matter? Because collective operations are often the hidden bottleneck in distributed training of large AI models. SHARP slashes this bottleneck by reducing redundant data movement and cutting latency significantly.

## How NVIDIA SHARP boosts your AI workloads

Distributed training demands efficient synchronization across GPUs for common collective operations such as allReduce and aggregate gradients from multiple systems. Traditionally, these operations route data through CPUs/GPUs multiple times, creating latency and network congestion.

NVIDIA SHARP improves performance by:

- Offloading collective operations to the NVIDIA Quantum InfiniBand network hardware: The network switches perform aggregation and reduction directly, bypassing CPUs and GPUs for these tasks.

- Eliminating redundant data copies: Redundant Data no longer bounces back and forth between endpoints unnecessarily.

- Maximizing bandwidth utilization: NVIDIA SHARP doubles your allReduce bandwidth(GB/s) compared to setups without SHARP.

- Supporting massive scale: Works seamlessly on clusters with hundreds of GPUs (think 128+ NVIDIA H100 or Blackwell GPUs).

The result? Faster gradient synchronization. Reduced training iteration time. A leaner communication stack that frees up CPU and GPU cycles for actual compute.

## Real-world performance: NVIDIA SHARP in action

Check out our internal benchmark results showing allReduce bandwidth at a 128MB message size across GPU clusters of varying sizes 16, 32, 64, 128, 256 and 1536 GPUs:

AllReduce Bandwidth (GB/s) at 128MB Message Size Across Cluster Sizes, demonstrating the performance advantage of NVIDIA SHARP-enabled clusters (purple bars) over non-SHARP setups (light purple bars)

From our tests, NVIDIA SHARP-enabled clusters significantly outperform non-SHARP clusters at every scale tested, with bandwidth improvements over 50% from 16-1536 GPUs.

Key specs:

- The 128MB message size represents a typical payload in distributed AI training.

- Bandwidth improvements scale with cluster size: approximately 50% for 16 GPUs, 49% for 32 GPUs, and 56% for 64 GPUs respectively.

- For larger clusters, bandwidth gains reach around 63% for 128 GPUs, 45% for 256 GPUs, and 54% for 1536 GPUs respectively.

- Non-SHARP configurations lag behind, limiting synchronization speed and overall training efficiency.

This data confirms the observation: NVIDIA SHARP dramatically boosts collective communication bandwidth, accelerating training on large-scale multi-GPU clusters.

### Quick code peek: leveraging NVIDIA SHARP in distributed PyTorch training

Let’s dive into a Python example that shows how NVIDIA SHARP integrates seamlessly with PyTorch’s distributed training via NCCL, the GPU communication library optimized for NVIDIA hardware.

import torch
import torch.distributed as dist
import os

def setup_distributed():
    dist.init_process_group(
        backend='nccl',  # NCCL supports SHARP-aware communication
        init_method='env://',
        world_size=int(os.environ['WORLD_SIZE']),
        rank=int(os.environ['RANK'])
    )

def train_step(tensor):
    # Perform an allReduce operation optimized by SHARP if enabled in the network
    dist.all_reduce(tensor, op=dist.ReduceOp.SUM)
    tensor /= dist.get_world_size()
    return tensor

if __name__ == "__main__":
    setup_distributed()
    local_tensor = torch.ones(10).cuda() * (dist.get_rank() + 1)
    
    # Synchronize gradients using SHARP-accelerated allReduce
    reduced_tensor = train_step(local_tensor)

    print(f"Rank {dist.get_rank()} reduced tensor: {reduced_tensor}")

- 

The setup_distributed() function initializes the distributed environment using NCCL as the backend, which supports SHARP-aware communication when the underlying infrastructure is configured properly.

- 

The train_step() function performs an all_reduce operation, a key collective communication pattern that aggregates data (like gradients) across all GPUs. When SHARP is enabled on the network, this operation is offloaded and accelerated by the NVIDIA Quantum InfiniBand fabric.

- 

In the main block, a simple tensor is created per GPU (differentiated by rank), and the all_reduce synchronizes these tensors efficiently across the cluster.

Notes and Actionable Recommendations: To take advantage of SHARP, you need the NVIDIA Quantum InfiniBand network configured correctly and the NVIDIA SHARP plugin installed on your cluster nodes. To fully leverage NVIDIA SHARP, application-level modifications are necessary. This involves integrating SHARP-aware collective operations into your codebase, such as utilizing the NVIDIA SHARP plugin with NCCL or MPI libraries.

## Benefits of SHARP

SHARP shines brightest for customers running large-scale, multi-GPU distributed training jobs who can adapt their applications to take advantage of SHARP-enabled communication libraries. If you’re pushing boundaries with:

- Training transformer models (like BERT, GPT) at scale

- HPC workloads requiring low-latency collective operations

- Clusters sized 128 GPUs and above

… then SHARP is your new secret weapon.

## SHARP on Lambda 1CC: Available now, No extra cost

When you spin up 1-Click Clusters in supported regions, NVIDIA SHARP is ready to go. No additional charges. Just install the SHARP plugin and modify your application-level code to unlock performance gains. NVIDIA benchmarks show:

- +17% faster BERT training with NVIDIA SHARP

- Up to 8x reduction in collective communication latency with NVIDIA SHARP

- Measured +63% in allReduce bandwidth improvement on Lambda’s 128x NVIDIA HGX B200 clusters

#### How to get started

- Request NVIDIA SHARP enablement on your 1-Click Cluster.

- Install the NVIDIA SHARP plugin included in updated base images.

- Modify your distributed training code to leverage SHARP-aware communication calls. Our ML team is standing by to help.

## Why choose Lambda for NVIDIA SHARP-enabled clusters?

We don’t just offer infrastructure, we bring deep expertise in optimizing multi-GPU workloads to help maximize your performance. Our multi-tenant 1-click clusters combine the latest NVIDIA hardware, NVIDIA Quantum InfiniBand networking and NVIDIA SHARP acceleration, all tuned for peak performance. This means you get scalable AI infrastructure that punches above its weight.

Need help optimizing your workloads for NVIDIA SHARP? Our team is here to guide you from installation to performance tuning, ensuring you unlock every ounce of potential.

Access High Performance Computing at your fingertips. 

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
