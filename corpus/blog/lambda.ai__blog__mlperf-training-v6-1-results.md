# Lambda delivers faster AI training for language and image models

Source: https://lambda.com/blog/mlperf-training-v6-1-results

Skip to main content

# Lambda delivers faster AI training for language and image models

 November 16, 2026

 • 7 min read

New MLPerf Training v6.1 results show 2.86× faster language-model training on newer NVIDIA accelerated computing and 1.50× faster image-model training with updated software.

MLPerf is the gold standard for benchmarking AI systems and performance. Over its almost nine-year history, more than 100 vendors have contributed to MLPerf, with 25 participating in the latest training round, MLPerf Training v6.1. An MLPerf Training result measures how long a system takes to train a model to a predefined quality target. This result is then peer-reviewed before being publicly released. Through this methodology, MLPerf has become the trusted benchmark suite for AI workloads since its inception in 2018.

In this round of MLPerf Training, Lambda achieved measurable improvements on two workloads on 64 NVIDIA Blackwell Ultra GPUs in a single NVIDIA GB300 NVL72 system. We finished mixture-of-experts (GPT-OSS-20B) training in 19.697 minutes. This represents a 2.86× improvement over the same workload on 64 NVIDIA H100 GPUs last round (Cisco). We also trained the text-to-image model Flux.1 in 26.36 minutes in an unofficial reproduction, a 1.50× speedup over the fastest result on the same hardware six months ago, driven mainly by software stack improvements. 

## Lambda's MLPerf Training v6.1 results

Below are our results on 64 NVIDIA Blackwell Ultra GPUs for two models: GPT-OSS-20B (official MLPerf result) and Flux.1 (unofficial reproduction).

 | 

Model

 | 

System

 | 

Time to train

 | 

Status

 | 

Notes

 | 

GPT-OSS-20B

 | 

NVIDIA GB300 NVL72 (64 NVIDIA Blackwell Ultra GPUs)

 | 

19.697 min

 | 

Official

 | 

Large-scale MoE training run.

 | 

Flux.1

 | 

NVIDIA GB300 NVL72 (64 NVIDIA Blackwell Ultra GPUs)

 | 

26.36 min

 | 

Unofficial

 | 

Our first multimodal training workload. Logs and code are publicly available.

Time to solution measured in minutes to convergence. 

## GPT-OSS-20B: a strong case for upgrading to NVIDIA GB300 NVL72

GPT-OSS-20B was one of MLPerf’s first mixture-of-experts training benchmarks, introduced in MLPerf Training v6.0. It matters because MoE is one of the most widely used architectures behind LLM-based applications today. Unlike dense LLMs, MoE models activate only a subset of their total parameters per token, drastically reducing the time spent on the forward pass and, therefore, total training and inference costs. That makes this GPT-OSS-20B benchmark a useful reference workload for teams building reasoning and agentic applications on MoE architectures.

Our results showed that 64 NVIDIA Blackwell Ultra GPUs trained the model 2.86× faster than 64 NVIDIA H100 GPUs in the last round (Cisco), and 1.37× faster than 64 NVIDIA Blackwell GPUs (8 NVIDIA HGX™ B200 systems) in the last round (CoreWeave). That's a strong reason for teams considering an upgrade.

For teams weighing an upgrade, the speedup translates into three practical benefits:

- Faster R&D iteration: the same experiment finishes sooner, so teams can run more experiments per week.

- Faster time to market: shorter training cycles mean models ship sooner.

- Lower cost per run: reaching the quality target in less time means fewer billed GPU-hours.

## Flux.1: our first step into multimodal training benchmarks

Training v6.1 is also the first time Lambda has run a multimodal workload through the MLPerf harness. Flux.1, introduced in Training v5.1, followed Stable Diffusion, MLPerf’s first text-to-image training benchmark. This matters because image generation models are a growing share of what teams train, and they sit close to physical AI: diffusion-based image models are increasingly used to generate synthetic data and simulated environments for robotics, autonomous vehicles, and other systems that perceive and act in the real world. They also stress a system differently than language models do. We wanted to show that the same infrastructure we benchmark for LLMs and MoE models performs well on them too.

We trained Flux.1 on 64 NVIDIA Blackwell Ultra GPUs and converged in 26.36 minutes, a 1.50× speedup over the fastest result for this workload on the same hardware last round. Notably, the improvement is mainly attributable to software stack improvements, as our first reproduction of the workload on the same hardware system using NVIDIA CUDA™ Version 13.4.1, CUDA Driver 580.174.04, and PyTorch NVIDIA Release 26.08 shows a 1.27× speedup. Our second reproduction used an optimized configuration, including a learning rate of 0.00025, a global batch size of 1024, and 1600 warmup steps, and gained another 1.18× speedup. This shows that an updated software stack and an optimized workload configuration can bring compounding gains.

Our unofficial reproduction was produced after the MLPerf submission deadline. This allowed us to compare 64 NVIDIA Blackwell Ultra GPUs with AMD’s 64 Instinct MI355X GPUs on the same workload. Our unofficial result was 1.12× faster than AMD’s official result, with code and configuration available in this public repo. 

## What this means for your team

Lambda’s results illustrate two ways to improve training performance: newer hardware can shorten training time, and software improvements can deliver further gains on existing hardware. The GPT-OSS-20B result provides a reference for teams evaluating a move from NVIDIA H100 to NVIDIA GB300 NVL72. The unofficial Flux.1 reproduction shows the additional impact of an updated software stack and tuned training configuration.

For your team, the next step is to establish how those gains translate to your own workload, budget, and delivery schedule.

## Before committing to training capacity

For teams choosing capacity, and the leaders approving that investment, four questions can help turn benchmark performance into a practical decision:

- How closely does the benchmark match our workload? Compare the model, quality target, and GPU count. Use the result as a starting point, then test a representative workload of your own.

- What drives the improvement? Ask which gains come from newer hardware, updated software, or changes to the training configuration. Confirm that the tested configuration is available for your team to use.

- What will it cost to reach our target? Evaluate elapsed training time alongside the price and total capacity you must reserve. A faster run on more expensive hardware does not automatically mean a lower bill.

- Can we verify the result before making a larger commitment? Ask for code, configurations, and run instructions, distinguish reviewed results from unofficial reproductions, and agree on a small evaluation with clear success criteria.

The goal is to choose capacity based on the time and cost required to reach your model-quality target, supported by evidence your technical team can validate.

To explore capacity for your workload, Lambda offers 1-Click Clusters for multi-GPU training and Superclusters for larger, dedicated deployments. Discuss your model, target scale, and evaluation requirements with our team to identify an appropriate configuration.

Explore Lambda GPU Cloud
Learn about 1-Click Clusters
Learn about Superclusters

System details
Official GPT-OSS-20B submission on 16 nodes, 64 NVIDIA Blackwell Ultra GPUs in a single NVIDIA GB300 NVL72 system, and PyTorch NVIDIA Release 26.08.

All results are subject to final MLCommons review and publication.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
