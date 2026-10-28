# MLPerf Training v5.1: Lambda’s NVIDIA GB300 NVL72 outperforms NVIDIA GB200 NVL72 by 27%

Source: https://lambda.ai/blog/lambda-mlperf-training-benchmarks-v5.1

Skip to main content

# MLPerf Training v5.1: Lambda’s NVIDIA GB300 NVL72 outperforms NVIDIA GB200 NVL72 by 27%

 November 12, 2025

 (Updated on October 22, 2026)

 • 4 min read

Training large language models (LLMs) takes massive compute power, making it critical for AI teams to understand and optimize performance across their systems. Lambda’s MLPerf training results on NVIDIA GB300 NVL72 provide a clear, reproducible baseline for benchmarking training speed and efficiency.

Since our last MLPerf v5.0 submission, both the benchmarks and the underlying model architectures have advanced.

Today, we’re announcing MLPerf v5.1 results. Version 5.1 introduces modern workloads like Meta’s Llama 3.1 8B, replacing legacy BERT models to mirror real-world generative AI training. This update brings MLPerf in line with the demands and complexity of modern enterprise models.

## Lambda’s MLPerf training results at a glance

Only three teams reported official NVIDIA GB300 NVL72 results in MLPerf Training v5.1: NVIDIA, Supermicro, and Lambda.

 | System
 | Accelerators
 | Framework
 | Llama 3.1 8B (min)
 | Llama 2-70B LoRA (min)

 | Lambda’s NVIDIA GB300 NVL72 Cluster
 | 72× GB300 279 GB
 | PyTorch NVIDIA Release 25.09
 | 14.25
 | 1.26

 | Fastest NVIDIA GB200 NVL72 Cluster in MLPerf Training v5.0
 | 72× GB200 192 GB
 | PyTorch NVIDIA Release 25.04
 | N/A
 | 1.598

 | Fastest NVIDIA 64×B200 Cluster in MLPerf Training v5.0
 | 64× B200 192 GB
 | PyTorch NVIDIA Release 25.04
 | N/A
 | 2.019

Time represents MLPerf’s standardized time-to-convergence metrics. The results can be fully reproduced using our guide.  
We’re comparing our run against the best NVIDIA GB200 NVL72 results from last round (v5.0): 1.598 min from Oracle. We’re 1.598 / 1.26 = 1.27x faster. Source: MLPerf Training benchmark suite.

Compared to the best results from the previous MLPerf Training round, our NVIDIA GB300 NVL72 Llama 2-70B run converged 1.6× faster than the top 64× NVIDIA B200 system and 1.27× faster than the best NVIDIA GB200 NVL72 submission.

## The NVIDIA GB300 NVL72 advantage

These performance gains stem from NVIDIA Blackwell Ultra architecture, a refreshed software stack, on top of Lambda’s optimized cluster design.

Specifically:

- The latest generation NVIDIA Grace Blackwell GPU, along with 288 GB of HBM3e memory, yielded a 1.12× training speedup

- Newer versions of the NVIDIA driver, NVIDIA CUDA, NVIDIA NCCL, NVIDIA cuBLAS, NVIDIA cuDNN also contributed an additional 1.13× gain

Together, these advances make NVIDIA GB300 NVL72 a leading platform for frontier-scale AI training, delivering top-tier performance with flexible orchestration through Kubernetes or Slurm, in both managed and self-managed environments.

## 

## FP4 vs FP8 on NVIDIA Blackwell

After our official submission, we evaluated FP4 efficiency using NVIDIA’s NVFP4 precision on Blackwell.

 | Model
 | FP8 time-to-target (min)
 | FP4 time-to-target (min)
 | FP4 speedup w.r.t FP8

 | Llama 3.1 8B (8xB200)
 | 86.22
 | 99.21
 | 1.13x

We observed a 13% average speedup with FP4 compared to FP8 across 10 trials. These results show that the NVIDIA Blackwell’s NVFP4 option can further shorten training time for memory bandwidth-bound LLMs, complementing the FP8 precision used in our official MLPerf Training submissions.

## What this means for your team

Enterprise AI teams evaluating GPU clouds have long had to choose: performance, cost efficiency, or control. Rarely all three.

With MLPerf v5.1, Lambda closes that gap, delivering verified NVIDIA GB300 NVL72 performance that’s production-grade and reproducible on fully accessible infrastructure.

By pairing cutting-edge hardware with a modern software stack and transparent, industry-standard benchmarking, Lambda sets a new baseline for enterprise-scale LLM training.

Experience the performance of NVIDIA GB300 NVL72 for yourself.

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
