# MLPerf Inference v6.1: pioneering agent, VLM benchmarks

Source: https://lambda.ai/blog/mlperf-inference-v6.1

Skip to main content

# MLPerf Inference v6.1: pioneering agent, VLM benchmarks

 September 16, 2026

 (Updated on October 22, 2026)

 • 14 min read

First agentic workload on datacenter hardware in MLPerf, and the first model over a trillion parameters. Plus 8.85% more throughput on identical hardware since v6.0.

Scaling large-scale inference comes down to sustained performance under real workloads. Latency, throughput, and model-level bottlenecks are the main key performance indicators for whether your production deployments are keeping up. Lambda's MLPerf Inference v6.1 results show exactly where each gap closed, and by how much.

In this inference round, our closed division results show several advances in performing inference: on the hardware side, our 4 NVIDIA Blackwell Ultra GPUs system delivers the leading Offline throughput on GPT-OSS 120B among all 4 Blackwell Ultra GPUs submissions; on the software side, that same system posts an 8.85% (Server) and 8.79% (Offline) throughput improvement over v6.0 on identical hardware, a direct reflection of the impact of stack optimizations since last round. In the open division, the memory headroom of our NVIDIA HGX B200 system allowed us to replace the Qwen3.6-27B backbone of the agentic inference workload with Kimi K2.6, deploying a model with over a trillion parameters and, to our knowledge, marking the first agentic inference workload run on datacenter hardware in MLPerf.

## The results at a glance

 | 

Model

 | 

System

 | 

Division

 | 

Scenario

 | 

Result

 | 

Notes

 | 

GPT-OSS 120B

 | 

4 NVIDIA Blackwell Ultra GPUs

 | 

Closed

 | 

Server + Offline

 | 

58,195 / 65,511 tokens/s

 | 

Leading Offline result among 4 NVIDIA Blackwell Ultra GPUs submissions, besting second place by 2.38%; 8.85% (Server) and 8.79% (Offline) improvement over v6.0

 | 

Qwen3 VL

 | 

NVIDIA HGX B200

 | 

Closed

 | 

Server + Offline

 | 

69.41 / 101.56 queries/s

 | 

Only 8× B200 + Qwen3 VL submission; Offline is 28.5% faster than the fastest v6.0 submission (79.04 q/s), Server is 2.29% faster (vs. 67.86 q/s)

 | 

Qwen3 VL

 | 

4 NVIDIA Blackwell Ultra GPUs

 | 

Closed

 | 

Server + Offline

 | 

64.624 / 71.122 queries/s

 | 

Server is second of four 4 Blackwell Ultra GPUs submissions, within thousandths of a query/s of the lead; Offline within 2.9% of the leading result

 | 

Kimi K2.6

 | 

NVIDIA HGX B200

 | 

Open

 | 

SingleStream (Edge Agentic)

 | 

86.83% BFCL v4 accuracy; 1,007/1,007 replay turns completed

 | 

First deployment of model w/ >1 trillion parameters on MLPerf; first agentic workload on datacenter hardware

Round-over-round deltas computed as (v6.1 result ÷ v6.0 result − 1) × 100 on identical hardware and benchmark conditions.

## Highlight 1: first benchmarking of VLMs on Lambda

Vision-language inference makes its debut in our submission lineup this round, and we submitted Qwen3-VL-235B-A22B-Instruct on both the NVIDIA HGX B200 and 4 NVIDIA Blackwell Ultra GPU systems.

On NVIDIA HGX B200, ours is the only Qwen3-VL-235B-A22B-Instruct submission on this configuration. The Offline result of 101.56 queries/s is 28.5% faster than the fastest submission from the previous round (79.04 q/s), and the Server result of 69.41 queries/s edges out the prior round's best (67.86 q/s) by 2.29%. Round over round, on comparable hardware, that gap is the software stack at work, as well as additional fine-tuning of hyperparameters by Lambda’s ML experts to find the most optimal configuration for inference on this model.

On 4 NVIDIA Blackwell Ultra GPUs, the field is tighter. Our Server result of 64.624 queries/s ranks second of four submissions, in a field where the entire spread from first (64.63 q/s) to fourth (64.608 q/s) is a few hundredths of a query per second. Our Offline result of 71.122 queries/s sits within 2.9% of the leading result (73.186 q/s).

This submission marks Lambda's first MLPerf result for a vision-language model (VLM). Beyond the benchmark itself, we publish this result as a case study demonstrating how customers can achieve low-latency, multi-modal inference on Lambda infrastructure, a workload profile that serves as a proxy for emerging use cases such as synthetic data generation and physical AI.

### System under test: NVIDIA HGX B200

- 8× NVIDIA B200-SXM-180GB using vLLM, NVIDIA CUDA version 13.0, no parallelism

- NVFP4 weights, FP8 KV cache

- Dual Intel Xeon Platinum 8570 (56 cores)

## Highlight 2: introducing agent inference benchmarking on datacenter hardware

Lambda's open-division submission paired our NVIDIA HGX B200 system with Kimi K2.6. MLPerf Inference v6.1 is the first round to include agentic tasks, and ours is the only agentic inference submission on datacenter hardware. It’s also the first deployment in MLPerf of a model with over a trillion parameters. The benchmark was designed for a single edge accelerator; we used it to show what the same agentic harness looks like when the memory ceiling comes off.

The Edge Agentic benchmark is new in v6.1, introduced by the MLCommons Edge LLM Taskforce to measure how well and how fast agentic LLMs call tools. It pairs two workloads: the Berkeley Function Calling Leaderboard v4 (BFCL v4) as a deterministic, judge-free accuracy confirmation, and a recorded agentic-coding replay (20 trajectories) for single-stream performance. The reference implementation serves Qwen3.6-27B as a Q4_K_M GGUF quantization on a single edge accelerator.

We ran the reference workload unchanged, except we swapped the served model. With 1.44 TB of aggregate HBM across the HGX B200 system, we had the headroom to host a model roughly 40× larger, so we chose Kimi K2.6 by Moonshot AI, a mixture-of-experts model with over a trillion parameters, served in FP8 with SGLang at TP=8. Swapping the model is what places this in the open division; every other parameter is the reference configuration: temperature 0, max_new_tokens 1024, single-stream execution (target_concurrency 1), and the reference BFCL v4 category mix. Reasoning was disabled server-side, matching the reference server's `--reasoning off` setting.

On the performance side, the agentic-coding replay completed as a fully valid run: 1,007 turns issued and completed with zero failures, with an inline IoU score of 0.6158. Mean per-turn latency came in at 770.8 ms (median: 361.0 ms), with time-to-first-token averaging just 179.7 ms and remarkably consistent, with a P99 TTFT of 196.7 ms. Of the 1,007 turns, 1,003 completed via tool calls, a rate expected with an agentic workload.

 | 

Submitter

 | 

Model size (total parameters)

 | 

System

 | 

Mean latency (ms)

 | 

BFCL v4 overall accuracy

 | 

Lambda (open)

 | 

1 trillion (Kimi K2.6)

 | 

NVIDIA HGX B200

 | 

770.8

 | 

86.83%

 | 

Vendor A

 | 

27 billion (Qwen3.6-27B)

 | 

NVIDIA Jetson AGX Thor 128G

 | 

1,466.0

 | 

87.94%

 | 

Vendor B

 | 

27 billion (Qwen3.6-27B)

 | 

ProLiant DL345 Gen12, 4× RTX PRO 4500

 | 

2,616.2

 | 

86.43%

 | 

Vendor B

 | 

27 billion (Qwen3.6-27B)

 | 

ProLiant DL145 Gen11, 1× RTX PRO 4500

 | 

2,758.0

 | 

86.13%

 | 

Vendor C

 | 

27 billion (Qwen3.6-27B)

 | 

NVIDIA DGX Spark (GB10)

 | 

3,807.7

 | 

87.24%

This is not an apples-to-apples comparison, as those are closed-division submissions on edge hardware running a 27B model, and ours is an open-division submission on datacenter hardware running a model roughly 40× larger. However, the asymmetry is the point: the same agentic harness, with the memory ceiling removed, serves a frontier-scale MoE at lower latency, with accuracy squarely in the field's band and above the published reference baseline.

### System under test: HGX B200 (open division)

- 8× NVIDIA Blackwell GPU-SXM-180GB, served with SGLang

- Parallelized with TP=8 and quantized with FP8, temp=0, max_new_tokens=1024, single-stream

- Identical hardware to closed NVIDIA HGX B200 submissions

## Highlight 3: MoE throughput, hardware and software

Our 4 NVIDIA Blackwell Ultra GPUs submission posted 65,511 tokens/s (Offline) and 58,195 tokens/s (Server) on GPT-OSS 120B. The Offline result leads all 4 Blackwell Ultra GPUs submissions this round, besting second place by 2.38% and third place by 7.8%. On the Server scenario, our result lands within 3.9% of the fastest submission (60,466 tokens/s), a tight three-way field where the spread between first and third is under 4%.

Measured against a 4× Blackwell GPU baseline (estimated by halving our HGX B200 closed-division result), the 4 Blackwell Ultra GPUs deliver a 1.54× (Offline) and 1.42× (Server) speedup. The delta is pure hardware: same NVIDIA TensorRT, same NVFP4/FP8 precision, and the same task. And the 8.85%/8.79% improvement over our own v6.0 Blackwell Ultra results, on identical hardware, is due to pure software improvements in the last six months.

GPT-OSS 120B runs at 5.1B active parameters per token. On NVIDIA Blackwell Ultra GPUs, with 279 GB of HBM3e per chip, the entire model fits comfortably in a single GPU's memory without tensor or expert parallelism. Additionally, the following TensorRT features drove further performance gains:

 | 

Optimization

 | 

What it does

 | 

torch.compile

 | 

Fuses ops into Triton kernels

 | 

Piecewise NVIDIA CUDA graphs

 | 

Captures 39 graph variants covering prefill + decode phases for different token shapes

 | 

Gen-only NVIDIA CUDA graphs

 | 

Captures 14 decode-only graphs for steady-state generation for different batch sizes

 | 

MNNVL for NVIDIA GB300 NVL72

 | 

Flag that enables higher GPU power and performance, as well as larger NVLink domains, over multiple nodes within a rack

 | 

MoE AutoTuner

 | 

Selects optimal GEMM tactics per expert

 | 

KV cache sizing (dry run)

 | 

Dry-runs a forward pass to size the KV cache precisely to available HBM; in-memory

 | 

PyTorch C++ extension JIT compilation

 | 

Caches the JIT-compiled C++ extension so compilation has a one-time cost

### System under test: 4 NVIDIA Blackwell Ultra GPUs

- 4×Blackwell Ultra GPUs (279 GB HBM3e per GPU)

- NVIDIA TensorRT, MXFP4 weights, FP8 KV cache

- GPT-OSS 120B (Server + Offline)

## What this means for your AI infrastructure

MLPerf Inference v6.1 continues the suite's expansion into the workloads enterprise teams actually run: reasoning, multimodal, and now agentic inference alongside the LLM serving benchmarks that have anchored prior rounds. Lambda continues to push the frontier, submitting leading performances in several of these closed workloads and contributing a novel open submission. 

Lambda's results span the models that enterprise teams are deploying today and preparing to deploy tomorrow. On NVIDIA Blackwell Ultra GPUs, we're ready for the next generation. On NVIDIA Blackwell GPUs, we're still pushing the boundary of what the current generation can do.

Lambda 1-Click Clusters are available from 16 to 1,536+ GPUs, with weekly to multi-year reservations and no contracts required for proof-of-concept work. Whether you're benchmarking a new architecture, scaling a production deployment, or researching frontier models, the infrastructure is ready.

Explore Lambda 
Learn about Lambda 1-Click Clusters

System details
4 NVIDIA Blackwell Ultra GPUs submission: 4× NVIDIA Blackwell Ultra GPUs, NVIDIA TensorRT, NVFP4/FP8. NVIDIA HGX B200 closed submissions: 8× NVIDIA Blackwell GPUs SXM 180 GB, NVIDIA TensorRT, FP4 weights, FP8 KV cache. NVIDIA HGX B200 open submission: identical hardware, Kimi K2.6 agentic workload.

All results are subject to final MLCommons review and publication.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
