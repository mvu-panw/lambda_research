# NVIDIA Vera Rubin NVL72 GPU | Lambda

Source: https://lambda.ai/vr-200

Skip to main content

# NVIDIA Vera Rubin NVL72 on Lambda

The next compute platform for frontier AI training and inference. Deployed as a production-ready Lambda Supercluster.

Available H2 2026.
Talk to our team

## One platform for training and serving at scale

10x more inference throughput per watt. 
One-tenth the token cost. Six purpose-built chips, designed to operate as one system.

### Compute

Train frontier models with fewer GPUs. Serve inference at a fraction of the cost per token.

- 72 NVIDIA Rubin GPUs: 50 PFLOPS NVFP4 per GPU

- 36 NVIDIA Vera CPUs: 88 custom NVIDIA Olympus cores each

- 288GB HBM4 per GPU at ~22 TB/s bandwidth (~2.7x over HBM3e)

- 20.7TB HBM4 and 1,580 TB/s aggregate memory bandwidth per rack

### Networking

5x better power efficiency. Every collective stays fast from GPU to supercluster.

- NVIDIA NVLink 6 Switch: unifies all 72 GPUs in a rack into a single high-bandwidth domain, keeping collective operations local

- NVIDIA ConnectX-9 SuperNIC: GPU-direct scale-out networking with programmable RDMA for low-latency inter-rack communication

- NVIDIA BlueField-4 DPU: offloads infrastructure services and enforces zero-trust security isolation, freeing GPUs for compute

- NVIDIA Spectrum-6 Ethernet switch (co-packaged optics): scale-out switching with integrated silicon photonics

### Storage

Eliminate GPU stalls for long-context and agentic workloads.

- NVIDIA STX: 5x higher token throughput and 2x faster ingestion than traditional storage

## End-to-end network performance

Predictable collectives and fault isolation at every layer, from GPU to supercluster.

01

### Scale-up
NVLink 6 unifies all 72 GPUs in a rack. 3.6 TB/s per GPU. 260 TB/s per rack.

02

### Scale-out (InfiniBand)
NVIDIA Quantum-X800 InfiniBand with SHARP-accelerated collectives, up to 41,000 GPUs

03

### Scale-out (Ethernet)
NVIDIA Spectrum-X Ethernet (RoCE) scales to 128,000 GPUs 

## Built for agentic workloads

01

### Large-scale training

Train frontier models with fewer GPUs. Vera Rubin delivers the same MoE training throughput with one-fourth the GPUs compared to Blackwell, compressing cluster size and reducing infrastructure cost for runs at 10T+ tokens.

02

### Mixture-of-Experts (MoE)

All-to-all token routing stays within the NVLink domain, keeping expert dispatch fast and reducing step-time variance across multi-rack deployments.

03

### Long-context inference

Million-token context windows run without offloading to slower memory tiers.

04

### Agentic execution

Vera CPU handles scheduling, orchestration, and KV-cache management without competing for GPU cycles. BlueField-4 isolates infrastructure services from application workloads, maintaining deterministic performance under multi-step agent execution.

## Datasheet

Get the full NVIDIA Vera Rubin NVL72 technical specifications, performance comparisons, and networking reference architectures.
DOWNLOAD THE DATASHEET
