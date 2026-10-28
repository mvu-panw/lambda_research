# Gigawatt-Scale AI Factories: NVIDIA GB300 NVL72 System on Lambda Cloud

Source: https://lambda.ai/blog/gigawatt-scale-ai-factories-nvidia-gb300-nvl72-system-on-lambda-cloud

Skip to main content

# Gigawatt-Scale AI Factories: NVIDIA GB300 NVL72 System on Lambda Cloud

 October 22, 2025

 • 4 min read

The path to superintelligence depends on infrastructure capable of sustaining trillion-parameter models and reasoning workloads at scale. That’s why Lambda is building gigawatt-scale AI factories on NVIDIA GB300 NVL72 systems as the compute backbone for the next generation of training and inference.

Last week, the first NVIDIA GB300 NVL72 systems were stood up in Lambda’s high-density liquid-cooled datacenters. Each rack integrates 72 NVIDIA Blackwell Ultra GPUs and 36 NVIDIA Grace CPUs, featuring 37 TB of fast memory and 130 TB/s of NVIDIA NVLink Switch bandwidth, turbocharging frontier-scale research and enterprise AI deployment.

Hydrogen-powered NVIDIA GB300 NVL72 racks

## NVIDIA GB300 NVL72: What’s New

Compared to NVIDIA GB200 NVL72, NVIDIA GB300 NVL72 introduces significant architectural gains:

- +50% HBM3e capacity (20TB per rack): Supports trillion-parameter models with larger checkpoints, higher batch sizes, and extended context.

- +1.5× higher dense FP4 performance & 2× faster attention operations: increases inference efficiency and utilization for reasoning-heavy workloads.

These improvements translate directly into faster training cycles and more efficient inference at scale.

NVIDIA GB300 NVL72 before InfiniBand XDR scale-out networking

## Built for reasoning workloads

NVIDIA GB300 NVL72 is designed around the demands of large-scale inference. Reasoning workloads can require up to 100× more compute per query compared to oneshot inference workloads. NVIDIA GB300 NVL72’s expanded HBM3e memory and FP4 efficiency keep those workloads running at full speed. 

Rack-scale NVLink5 provides 1.8 TB/s of bandwidth per GPU, connecting them into a single high-speed fabric for model parallelism with NVLink Switch. For multi-rack clusters, NVIDIA Quantum-X800 InfiniBand and ConnectX-8 SuperNICs deliver 800 Gb/s per GPU, reducing communication overhead during distributed training and inference.

Direct-to-chip liquid cooling ensures these systems run at peak utilization without thermal throttling, making it possible to deploy NVIDIA GB300 NVL72 at the density required for gigawatt-scale AI factories.

NVIDIA GB300 NVL72 power shelves and out-of-band Spectrum switches

## Why it matters:

For superintelligence and enterprise AI, NVIDIA GB300 NVL72 introduces the second-generation Transformer Engine with dynamic range management and fine-grain scaling techniques that optimize inference efficiency. With 1.5× more memory and up to 50% higher FP4 performance vs. NVIDIA GB200 NVL72. NVIDIA GB300 NVL72 is purpose-built to drive the next leap in trillion-parameter models and reasoning workloads.

NVIDIA GB300 NVL72 clusters deployed by Lambda combine compute, storage, orchestration, and observability into a single system. Each rack provides 3.84 TB of NVMe cache per GPU (276 TB per NVL72), configurable parallel file storage for high-throughput data access, and optional managed orchestration with Kubernetes or Slurm. Unified observability is delivered through Prometheus and Grafana for real-time metrics and alerting.

NVIDIA GB300 NVL72 rack-scale systems

## 
Lambda: The Superintelligence Cloud

Lambda Private Cloud delivers dedicated, bare-metal NVIDIA GPU clusters with low-latency networking and high-throughput interconnects, all in physically isolated data centers. Each rack is housed in a high-density, liquid-cooled facility engineered to maximize performance and ensure efficiency at the gigawatt scale.

Here’s what sets Lambda apart:

- Data centers purpose-built for AI
Optimized compute, storage, and networking in liquid-cooled data centers for scalable, efficient performance.

- Single-tenant clusters with observability
Secure, dedicated clusters with optional real-time monitoring, metrics, and reporting for production-grade operations.

- Co-engineering excellence & embedded support
Hands-on partnership with Lambda’s engineers, infrastructure specialists, and ML experts to reduce bottlenecks and accelerate results.

## The future of AI factories starts here.

With NVIDIA GB300 NVL72, Lambda enables the world’s most ambitious superintelligence labs and enterprises to train and serve next-generation models faster, more efficiently, and at gigawatt scale.

Connect with Lambda’s AI experts on deploying NVIDIA GB300 NVL72 Clusters.

## AUTHORED BY

 Khushboo Goel

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
