# LLM performance up 15.4%: MLPerf v5.1 confirms NVIDIA HGX B200 on Lambda is built for enterprise inference

Source: https://lambda.ai/blog/lambda-mlperf-inference-v5.1

Skip to main content

# LLM performance up 15.4%: MLPerf v5.1 confirms NVIDIA HGX B200 on Lambda is built for enterprise inference

 September 9, 2025

 (Updated on October 22, 2026)

 • 6 min read

Inference at scale is still too slow. Large models often stall under real-world load, burning time, compute, and user trust. That’s the problem we set out to solve.

Our MLPerf Inference v5.1 results show Lambda's 1-Click Clusters powered by NVIDIA HGX B200 achieved up to 15.4% performance gains than the previous round's best results. These benchmarks highlight how our 1-Click Clusters unlock best-in-class inference performance for enterprise production workloads.

## The performance gap that matters

- We tested three models across six scenarios: Llama 2 70B, Llama 3.1 405B, and Stable Diffusion XL. Each model was benchmarked in both the Offline and Server scenarios

- Five of six submissions delivered higher performance than the prior rounds, with gains ranging from +1.6% to +15.4% 

- Every submission met MLCommons' MLPerf accuracy and compliance checks for their respective tasks

- All benchmarks were run on an 8x NVIDIA HGX B200 (180 GB VRAM per GPU), using NVIDIA TensorRT 10.11 on NVIDIA CUDA 12.9 and Ubuntu 24.04

#### Results at a glance

The table below compares our v5.1 results against v5.0’s published numbers for the same models and scenarios from the prior round.

 | 

Model

 | 

Scenario

 | 

v5.1 Result

 | 

v5.0 Best

 | 

Δ vs v5.0

 | 

llama2-70b-99

 | 

Offline

 | 

102725.00 Tokens/s

 | 

98858.00 Tokens/s

 | 

+3.9%

 | 

llama2-70b-99

 | 

Server

 | 

99993.90 Tokens/s

 | 

98443.30 Tokens/s

 | 

+1.6%

 | 

llama3.1-405b

 | 

Offline

 | 

1648.60 Tokens/s

 | 

1538.17 Tokens/s

 | 

+7.2%

 | 

llama3.1-405b

 | 

Server

 | 

1246.79 Tokens/s

 | 

1080.31 Tokens/s

 | 

+15.4%

 | 

stable-diffusion-xl

 | 

Offline

 | 

32.57 Samples/s

 | 

30.38 Samples/s

 | 

+7.2%

 | 

stable-diffusion-xl

 | 

Server

 | 

28.46 Queries/s

 | 

28.92 Queries/s

 | 

-1.6%

Percentage gains(△) are calculated as (v5.1 ÷ prior best – 1) × 100

- Llama 3.1 405B showed the largest Server-side gain (+15.4%) 

- On 8xB200, both Llama 3.1 405B and Llama 2 70B delivered 3-4x higher performance than the best 8xH200 results

- Stable Diffusion XL (SDXL) improved +7.2% in offline throughput. Server dipped -1.6% vs. the prior best but still matched the median and SDXL was 1.07x faster than the best 8xH200 results

- The latest NVIDIA silicon combined with software produced a 1.6-15.4% gains across models with NVIDIA’s updated stack: TensorRT 10.11 and CUDA 12.9 with improved FP4 support

#### System Under Test (SUT)

MLPerf benchmarks were evaluated in two key inference scenarios:

Offline: measures peak throughput at saturation, relevant for batch jobs and bulk generation.

Server: enforces strict latency caps under load, simulating real-world serving conditions. Gains here directly improve user experience for real-time applications. 

To ensure consistency, all benchmarks were run on the same system with consistent configuration:

- System: NVIDIA HGX B200 (8xB200-180GB SXM6, TensorRT)

- Host CPU: Dual Intel Xeon Platinum 8750 with 56 cores

- 

Model specifications:

- 

Llama 3.1  405B and Llama 2 70B with FP4 weights, tested on tokens per second output

- Stable Diffusion XL with UNet fp8, CLIP encoders fp32 and VAE FP32 precision, tested on samples per second in offline and queries per second in server output

## Not just new silicon: Software maturity unlocks real gains

The performance improvements weren't just about throwing newer hardware at the problem. We partnered with NVIDIA to build custom TensorRT engines for each model and tuned per-scenario runtime parameters on NVIDIA HGX B200. The main areas of focus for testing involved:

- Calibrating batch size, request count and concurrency to meet Server latency targets while maximizing throughput

- Verifying streaming tokenization and scheduler settings for LLM Server runs to prevent tail-latency spikes under high QPS

- Validating engine tactics on TensorRT 10.11 with CUDA 12.9, confirming NVIDIA NVLink bandwidth and memory configuration on NVIDIA HGX B200

- For SDXL, evaluating UNet pipeline tiling and host-device staging effects at FP8, while keeping CLIP and VAE in FP32 for accuracy and safety

## What this means for Enterprise AI 

Lambda builds supercomputers in the cloud. 

Lambda placed first or second in rankings across three MLPerf categories, standing out among a dozen top vendors. This validates our infrastructure tuning and reinforces production-readiness for enterprise workloads.

Our 1-Click Clusters scale from 16 to 1,536+ GPUs with flexible rental terms from weekly to multi-year reservations. No contracts for POCs, with clear scaling paths to production through managed Kubernetes or Slurm orchestration.

For enterprises validating AI use cases before scaling to thousands of users, these benchmarks demonstrate production-ready infrastructure. 

For startups iterating on model development, they show the compute performance available for short-term bursts without long-term commitments.

## Lambda GPU Cloud is ready. Is your stack keeping up? 

Lambda's GPU Cloud is purpose built for enterprise inference workloads. The question is whether your current infrastructure can keep up? 

Try it for yourself. 

Spin up a 1-Click Cluster with 16-1536+ NVIDIA HGX B200s, or deploy a Private Cloud with 1000-64k+ GPUs and run your own benchmarks.

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
