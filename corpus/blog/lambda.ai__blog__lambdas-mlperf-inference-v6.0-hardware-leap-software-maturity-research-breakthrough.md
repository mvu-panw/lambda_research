# Lambda's MLPerf Inference v6.0: hardware leap, software maturity, research breakthrough

Source: https://lambda.ai/blog/lambdas-mlperf-inference-v6.0-hardware-leap-software-maturity-research-breakthrough

Skip to main content

# Lambda's MLPerf Inference v6.0: hardware leap, software maturity, research breakthrough

 April 1, 2026

 • 10 min read

NVIDIA Blackwell Ultra GPUs delivers 29% over NVIDIA Blackwell GPUs; software stack adds 9% on identical hardware; Smart Expert Routing cuts TTFT P99 by 31%

Running frontier AI at scale comes down to sustained performance under real workloads, on state-of-the-art AI infrastructure. Latency, throughput, and model-level bottlenecks are where production deployments diverge from benchmark sheets. Lambda's MLPerf Inference v6.0 results show exactly where each gap closed, and by how much.

Lambda is the only AI-native cloud to publish official MLPerf results for both inference and training on an NVIDIA Blackwell Ultra platform.

In this inference round, our closed division results show two dimensions of progress: 

- 

On the hardware side, our NVIDIA Blackwell Ultra GPU system delivers up to 29% higher iso-GPU throughput than NVIDIA HGX B200 on GPT-OSS-120B

- 

On the software side, upgrading from NVIDIA CUDA 12.9 to CUDA 13.1 on our NVIDIA HGX B200 (8-GPU) system delivers up to a 9% throughput gain on Llama 3.1 8B, a direct measure of stack maturity over six months.

In the open division, our collaboration with Stevens Institute of Technology produced BLAZE, a runtime MoE routing optimization that reduces time-to-first-token (TTFT) P99 latency by 31% on GPT-OSS-120B, with no model retraining required3.

## The results at a glance

 | Model
 | System
 | Division
 | Scenario
 | Results
 | Notes

 | GPT-OSS 120B
 | NVIDIA GB300 (one compute tray - 4-GPU)
 | Closed
 | Server + Offline
 | 53.4k/60.2k tokens/second
 | Up to 29% improvement over 4× NVIDIA B200 GPUs1

 | Llama 3.1 8B
 | NVIDIA HGX B200 (8-GPU)
 | Closed
 | Server + Offline
 | 130.0k/160.4k tokens/second
 | Up to 9% improvement over the same hardware system in v5.12

 | GPT-OSS 120B
 | NVIDIA HGX B200 (8-GPU)
 | Open
 | Server
 | TTFT P99: 2,001 ms / Throughput: 16,167 tok/s
 | +31% TTFT reduction, +3.9% throughput vs. baseline3

Delta computed as (v6.0 result ÷ baseline – 1) × 100. GPT-OSS open-division delta is BLAZE vs. baseline (TensorRT-LLM w/ TP = 4, EP = 4) on identical hardware.

## NVIDIA Blackwell Ultra GPU is ready: 29% more throughput on GPT-OSS 120B

Our NVIDIA Blackwell Ultra submission posted 60,220 tokens/s (Offline) and 53,463 tokens/s (Server) on GPT-OSS 120B using a GB300 compute tray (4-GPU): a 1.29×1 and 1.22×4 speedup, respectively, over a NVIDIA HGX B200 (4-GPU) baseline (estimated by halving the top-performing NVIDIA HGX B200 8-GPU system in a closed-division result, as no NVIDIA B200 4-GPU submission exists). 

The delta is pure hardware: same NVIDIA TensorRT-LLM inference engine, same FP4/FP8 precision, same benchmark conditions. That's the generational lift from NVIDIA’s generation-over-generation platform performance improvements, along with the benefits of an NVIDIA Grace CPU.

GPT-OSS 120B debuts in MLPerf Inference v6.0 as a new reasoning MoE model. It runs at 5.1B active parameters per token. NVIDIA Blackwell Ultra has 279GB of HBM3e per chip: the entire model fits comfortably in a single GPU's memory without the need for tensor- or expert-parallelism. Additionally, the following TensorRT-LLM features drove further performance gains:

 | Optimization
 | What it does

 | Piecewise CUDA graphs
 | Captures 39 graph variants covering prefill + decode phases for different token shapes.

 | Gen-only CUDA graphs
 | Captures 14 decode-only graphs for steady-state generation for different batch sizes.

 | MoE AutoTuner
 | Selects optimal GEMM tactics per expert

 | KV cache sizing (dry run)
 | Dry-runs a forward pass to size the KV cache precisely to available HBM; in-memory

 | PyTorch C Extension JIT Compilation
 | Caching the JIT-compiled C++ extension so compilation has a one-time cost.

System under test — one compute tray with NVIDIA Blackwell Ultra GPUs (4-GPU):

- 

NVIDIA GB300 compute tray (4-GPU) with 279GB HBM3e per GPU

- 

NVIDIA TensorRT-LLM, FP4 weights, FP8 KV cache

- 

GPT-OSS 120B (Server + Offline)

## Llama 3.1 8B: 9% more throughput from software alone

Lambda's NVIDIA HGX B200 (8-GPU) system posted 130,008 tokens/s (Server), 160,403 tokens/s (Offline), and 128,750 tokens/s (Interactive) in a closed-division submission on Llama 3.1 8B2. It was developed in collaboration with Yide Ran (PhD student, Stevens Institute of Technology) and Prof. Zhaozhuo Xu (Stevens Institute of Technology / Workato).

Llama 3.1 8B was introduced in the previous MLPerf Inference round, v5.1, replacing GPT-J with a 128K-token context window and a harder CNN/DailyMail summarization task. The more telling signal is the round-over-round delta: our NVIDIA HGX B200 (8-GPU) system shows up to 9% throughput improvement over the best v5.1 submissions on identical hardware2. 

The difference is pure software: the prior round's top results ran TRT-LLM 1.0 on CUDA 12.8–12.9; we ran TRT-LLM 1.2 on CUDA 13.1. That's six months of stack maturity translating directly into tokens per second.

System under test — NVIDIA Blackwell:

- 

NVIDIA HGX B200 (8-GPU), NVIDIA TensorRT LLM 1.2, CUDA 13.1, TP=1, EP=1

- 

FP4 weights, FP8 KV cache

- 

Dual Intel Xeon Platinum 8570 (56 cores)|

## BLAZE: 31% less latency, no model retraining

Lambda's first open-division submission paired our NVIDIA HGX B200 (8-GPU) system with BLAZE. This work was also developed in collaboration with Yide Ran (PhD student, Stevens Institute of Technology) and Prof. Zhaozhuo Xu (Stevens Institute of Technology / Workato).

BLAZE is a runtime MoE routing optimization that steers ambiguous tokens away from overloaded experts by adding a small, dynamically adjusted bias to routing scores. No model retraining required.

BLAZE is a simple drop-in NVIDIA TensorRT-LLM module agnostic to any EPLB techniques already employed. It adds only 0.1% overhead per decode step, but by steering traffic away from overloaded experts, it cuts time-to-first-token (TTFT) P99 from 2,903 ms to 2,001 ms (−31%) and lifts throughput by 3.9%, all the while maintaining full MLPerf accuracy compliance.

The table below shows some of the performance metrics. See the paper for full technical details.

 | Metric
 | Baseline3
 | BLAZE
 | Δ

 | Throughput (tokens/s)
 | 15,560
 | 16,167
 | +3.9%

 | TTFT P99 (ms)
 | 2,903
 | 2,001
 | −31.0%

 | TPOT P99 (ms)
 | 9.58
 | 10.28
 | +7.3% (well within 80 ms limit)

51,168 queries, 600,000 ms minimum duration, Server scenario, QPS = 12.

System under test — NVIDIA Blackwell (Open Division):

- 

NVIDIA HGX B200 (8-GPU), NVIDIA TensorRT-LLM, TP=4, EP=4

- 

FP4 weights, FP8 KV cache, identical hardware to closed submission

## What these results mean for your next deployment

The gap between benchmark performance and production performance is what MLPerf is designed to expose. These results show it closing: on the hardware side with NVIDIA GB300, on the software side with six months of stack maturity on NVIDIA HGX B200, and at the routing layer with BLAZE.

Three results, three decisions. If you're evaluating GB300: 29% more throughput on MoE models, the entire GPT-OSS 120B fitting in a single GPU's memory. If you're on B200 today: there's 9% more throughput in a software update, no hardware change needed. If latency is your constraint: BLAZE shows what a runtime routing change can do without retraining your model.

## Run it yourself

Evaluating, optimizing, benchmarking, or scaling an architecture?

Lambda 1-Click Clusters are production-ready NVIDIA HGX B200 or NVIDIA HGX H100 clusters, available from 16 to 2,000+ NVIDIA GPUs with weekly to multi-year reservations. They’re fully optimized for AI training, fine-tuning, and inference at scale.

Learn about 1-Click Clusters
Explore Lambda

About MLPerf Inference v6.0

MLPerf Inference v6.0 is the most expansive benchmark suite in the program's history. Five new data center benchmarks debuted: Text-to-Video generation, DLRM v3, GPT-OSS 120B, VLM (vision-language), and an updated DeepSeek-R1. The suite now spans reasoning, multimodal, video generation, and recommendation systems, alongside the LLM workloads that have dominated prior rounds.

System details: 

- 

NVIDIA GB300 submission — one compute tray of NVIDIA Blackwell Ultra (4-GPU), NVIDIA TensorRT-LLM, FP4/FP8

- 

NVIDIA B200 closed submission — NVIDIA HGX B200 (8-GPU), NVIDIA TensorRT-LLM, FP4 weights, FP8 KV cache

- 

NVIDIA HGX B200 (8-GPU) open submission — identical hardware, BLAZE routing optimization, TP=4, EP=4

1 MLPerf® v6.0 Inference Closed GPT-OSS 120B offline. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ April 1st, 2026, entry 6.0-0063. For comparison, we use MLPerf® v6.0 Inference Closed GPT-OSS 120B offline. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ April 1st, 2026, entry 6.0-0091 (RedHat). 
Both results were verified by MLCommons Association.

2 MLPerf® v6.0 Inference Closed Llama 3.1 8B offline. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ April 1st, 2026, entry 6.0-0062. For comparison, we use MLPerf® v5.1 inference Closed Llama 3.1 8B offline. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ October 22nd, 2025, entry 5.1-0062 (Lenovo). 
Both results were verified by MLCommons Association. 

3 MLPerf® v6.0 Inference Open GPT-OSS 120B. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ April 1st, 2026, entry 6.0-0110. For comparison, the baseline results use the same configuration as 6.0-0110, but without BLAZE.  
Results not verified by MLCommons Association. Details can be found in this technical report. 

4 MLPerf® v6.0 Inference Closed GPT-OSS 120B offline. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ April 1st, 2026, entry 6.0-0063. For comparison, we use MLPerf® v6.0 Inference Closed GPT-OSS 120B offline. Retrieved from https://mlcommons.org/benchmarks/inference-datacenter/ April 1st, 2026, entry 6.0-0083 (Nebius). 
Both results were verified by MLCommons Association. 

The MLPerf name and logo are registered and unregistered trademarks of MLCommons Association in the United States and other countries. All rights reserved. Unauthorized use strictly prohibited. See www.mlcommons.org for more information.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
