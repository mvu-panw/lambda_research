# NVIDIA's Vera Rubin NVL72 coming to Lambda's Superintelligence Cloud

Source: https://lambda.ai/blog/nvidias-vera-rubin-nvl72-coming-to-lambdas-superintelligence-cloud

Skip to main content

# NVIDIA's Vera Rubin NVL72 coming to Lambda's Superintelligence Cloud

 January 9, 2026

 • 3 min read

At Lambda, we build supercomputers that enable AI teams to deliver next-generation, frontier models. Today, we’re announcing the next evolution of our infrastructure: the NVIDIA Vera Rubin platform, which will serve as the core building block for Lambda Superclusters. 

The Vera Rubin NVL72 rack operates as a single, massive GPU and, when networked into a Supercluster, unlocks scale and efficiency previously out of reach. This enables teams to map models, validate performance, and run at production scale.

Why this matters

Engineers designing and training the next-generation reasoning and agentic models need two critical resources: performance and efficiency. The NVIDIA Vera Rubin architecture delivers both. Vera Rubin NVL72 is a single unified rack with a 72-GPU NVIDIA NVLink domain. It reduces cross-die communication overhead, expands the scale-up memory pool, enables model-parallel training and inference to behave more like single-node runs, and delivers up to 10x higher token throughput per watt and costs one-tenth as much per million tokens as NVIDIA Blackwell. 

What teams can do:

- Train and iterate on 10T+ parameter models and production-scale Mixture of Experts (MoE) with significantly lower communication overhead, shortening the time to convergence.

- Serve real-time, high-throughput inference and long-context reasoning with rack-local HBM4 and high intra-rack bandwidth, which keep KV caches and model state on ultra-fast memory.

- Run reinforcement learning (RL) actor-learner loops and HPC collectives with predictable, low latency on racks that behave like one NVLink domain, simplifying mapping, scheduling, and synchronization.

The building block: NVIDIA Vera Rubin NVL72

Vera Rubin NVL72 is a full-stack, rack-scale AI supercomputer purpose-built for massive-scale AI.

Core hardware:

- GPUs: 72 NVIDIA Rubin GPUs within a single NVLink domain 

- CPUs: 36 NVIDIA Vera CPUs integrated into Vera Rubin Superchips

- DPUs: 18 NVIDIA BlueField-4 DPUs that enable secure, software-defined infrastructure

- Scale-up: NVIDIA NVLink 6 Switch trays that create a high-bandwidth scale-up fabric 

- Scale-out: NVIDIA Spectrum-X Ethernet or NVIDIA Quantum-X800 InfiniBand scaling to 100,000+ GPUs 

Key technical specifications:

- Memory: Up to 20.7 TBHBM4 per rack with bandwidth targets up to 22 TB/s per GPU

- Fabric: NVIDIA NVLink 6 providing 3.6 TB/s GPU-to-GPU connectivity within the rack, backed by NVIDIA NVLink Switch scale-up fabric

- Networking: External connectivity and DPU offload via NVIDIA BlueField-4 800G DPUs and NVIDIA ConnectX-9 1600G SuperNICs for inter-rack scale-out

- Cooling: 100% direct-to-chip (D2C) liquid-cooled compute and switch trays

Lambda Supercluster

Lambda builds Superclusters — single-tenant, high-density platforms engineered to run mission-critical AI at scale. NVIDIA Vera Rubin NVL72 further enhances Supercluster value: 

- Intra-rack scale-up: The Vera Rubin NVL72 NVLink 6 design creates a domain where all 72 GPUs access memory at near-local speeds, reducing communication overhead for model-parallel training and inference and making MoE routing far cheaper in latency and bandwidth.

- Inter-rack scale-out: Using ConnectX-9 1600G SuperNICs and BlueField-4 800G DPU fabrics, we bind thousands of Vera Rubin NVL72 racks into a non-blocking fabric that delivers linear scaling for very large foundation models.

- Operational abstractions: Lambda’s control plane treats Vera Rubin NVL72 racks as unified building blocks. Engineers can provision multi-rack Superclusters with the same simplicity as a single instance and run them with reservation workflows and our managed orchestration.

Facilities and cooling

These high-density racks require purpose-built data centers with full liquid cooling and robust power delivery. Lambda’s Supercluster facilities are engineered to support sustained high-power operation, featuring redundant plumbing and comprehensive monitoring of power and thermal performance. We provide 24/7 co-engineering and operations support to keep workloads running at peak efficiency.

Availability and access

We’re working closely with NVIDIA to deploy the Rubin Platform in Lambda Superclusters. Production availability is planned for the second half of 2026. 

Request priority access: Talk to our team

## AUTHORED BY

 Khushboo Goel

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
