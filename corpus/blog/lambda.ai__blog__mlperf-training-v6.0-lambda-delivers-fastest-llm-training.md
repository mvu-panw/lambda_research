# MLPerf Training v6.0: Lambda delivers fastest LLM training on NVIDIA GB300 NVL72 and fastest MoE training on NVIDIA HGX B200

Source: https://lambda.ai/blog/mlperf-training-v6.0-lambda-delivers-fastest-llm-training

Skip to main content

# MLPerf Training v6.0: Lambda delivers fastest LLM training on NVIDIA GB300 NVL72 and fastest MoE training on NVIDIA HGX B200

 June 16, 2026

 • 4 min read

Lambda’s GB300 NVL72 Llama 3.1 8B MLPerf Training v6.0 submission improved performance by 18.7% over Lambda’s previous result, achieving the fastest convergence on this round's workload on GB300 NVL72. In addition, Lambda achieved the fastest result among single-node HGX B200 submissions for GPT-OSS-20B.

Training performance depends on far more than just compute capacity. Model architecture, system design, and software optimizations all play a critical role in determining how quickly models converge. Lambda's MLPerf Training v6.0 NVIDIA GB300 NVL72 and NVIDIA HGX B200 results provide a clear, reproducible baseline for benchmarking training speed and efficiency.

Version 6.0 marks a meaningful expansion of the MLPerf Training suite. For the first time, the benchmark includes mixture-of-experts (MoE) models, notably OpenAI's GPT-OSS-20B. This reflects MLCommons' pursuit of benchmarking real-world AI training workloads; dense LLMs have dominated prior rounds, while MoE architectures are increasingly central to frontier model development.

Lambda submitted results for two systems and two models:

- NVIDIA GB300 NVL72 on Llama 3.1 8B and GPT-OSS-20B

- NVIDIA HGX B200 on Llama 3.1 8B and GPT-OSS-20B

## Lambda's MLPerf Training v6.0 results

 | Model
 | System
 | Time-to-train
 | Notes

 | Llama 3.1 8B
 | GB300 NVL72
 | 11.59 minutes
 | 18.7% faster convergence compared to the previous training round, fastest among GB300 NVL72 submissions

 | Llama 3.1 8B
 | HGX B200
 | 85.26 minutes
 | Competitive with the best HGX B200 submissions

 | GPT-OSS-20B
 | GB300 NVL72
 | 18.35 minutes
 | Large-scale MoE training run. Competitive with the best GB300 NVL72 systems

 | GPT-OSS-20B
 | HGX B200
 | 96.46 minutes
 | Fastest among HGX B200 single-node submissions

Time-to-train measured in minutes to convergence. All results subject to final MLCommons review and publication.

## Lambda's NVIDIA GB300 NVL72 leads the class

For Llama 3.1 8B, Lambda completed training in 11.59 minutes on a GB300 NVL72 system, the fastest result among all GB300 NVL72 systems submitted this round, edging the NVIDIA Theia system single-rack submission (11.75 min), HPE (11.82 min), GigaComputing (11.84 min), and Nebius (11.87 min). The same pattern holds for GPT-OSS-20B: Lambda converged in 18.35 minutes, among the fastest of the GB300 NVL72 single-rack systems.

These gains stem from NVIDIA Blackwell Ultra innovations: 279GB of HBM3e per GPU, higher memory bandwidth, and an improved interconnect, combined with Lambda's cluster design and a tuned NVIDIA NeMo software stack.

System specifications for NVIDIA GB300 NVL72:

- 18 nodes × 4 NVIDIA GB300 NVL72 (72 GPUs total)

- NVIDIA Blackwell Ultra GPUs with 279GB HBM3e memory

- PyTorch NVIDIA Release 25.09 / NeMo Framework

- Neoverse-V2 host processors

## Llama 3.1 8B: comparing across generations

Llama 3.1 8B was introduced in the previous round (MLPerf Training v5.1), so this is the first cycle in which a round-over-round comparison is meaningful for that model. The most impactful comparison for this workload is the stack optimizations between rounds using the same SUT.

Our GB300 NVL72 system converges in 11.59 minutes, compared to 14.25 minutes in Training v5.1. This represents an 18.7% improvement in training speed attributed purely to software improvements over the last round. At large scales, this can save days, weeks, or even months of time.

## GPT-OSS-20B: one of the first MoE training benchmarks

GPT-OSS-20B, along with DeepSeek-V3, is one of MLPerf's first mixture-of-experts benchmarks. MoE training introduces distinct challenges: expert load balancing, routing overhead, and communication patterns that differ from dense transformer training.

Our HGX B200 system achieved the fastest time-to-train among single-node submitters in this category, converging in 96.46 minutes. For teams looking ahead to GB300 NVL72 clusters, our GB300 NVL72 result shows what frontier-scale MoE training unlocks: converging in 18.35 minutes and delivering meaningfully higher throughput per accelerator, a strong signal for the economics of large MoE training at scale.

## What this means for your team

MLPerf Training v6.0 is the most architecturally diverse training benchmark to date. Eight teams reported official GB300 NVL72 results this round: Lambda, Nebius, CoreWeave, Oracle, Dell, GigaComputing, HPE, and NVIDIA.

For enterprise AI teams, the benchmark results are reproducible, and the stack is production-ready. Whether the workload is a dense LLM like Llama 3.1 8B or an emerging MoE architecture like GPT-OSS-20B, the hardware and software are validated against industry-standard conditions.

Lambda 1-Click Clusters are available from 16 to 2,000+ GPUs, with weekly to multi-year reservations and no contracts required for proof-of-concept work. Whether you're benchmarking a new architecture, scaling a production training run, or evaluating hardware for your next infrastructure decision, the infrastructure is ready.

Explore Lambda GPU Cloud
Learn about 1-Click Clusters

System details
GB300 NVL72 submission: NVIDIA Blackwell Ultra GPU (GB300 NVL72), PyTorch NVIDIA Release 25.09.
HGX B200 submission: NVIDIA B200-SXM-180GB, PyTorch NVIDIA Release 25.04.

All results subject to final MLCommons review and publication.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
