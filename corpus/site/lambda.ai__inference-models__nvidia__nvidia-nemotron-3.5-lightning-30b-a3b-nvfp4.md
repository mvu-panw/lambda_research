# nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

Source: https://lambda.ai/inference-models/nvidia/nvidia-nemotron-3.5-lightning-30b-a3b-nvfp4

Skip to main content

# How to deploy NVIDIA Nemotron-3.5-Lightning-30B-A3B NVFP4 on Lambda

## Performance

NVIDIA Nemotron-3.5-Lightning-30B-A3B NVFP4

1× NVIDIA B200 GPU or 1× NVIDIA H100 GPU · vLLM TP1

4,837 output tok/s maximum throughput on B200

416 tok/s/user at interactive latency on B200

C16 — Pareto-optimal balanceC4 — Pareto-optimal balance

### Benchmark summary

 | Hardware
 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | 1× B200
 | C1
 | 360.6
 | 416.2
 | 179 / 184
 | 2.6 / 2.6

 | 1× B200
 | C16
 | 2,132.2
 | 182.3
 | 1,733 / 2,437
 | 5.8 / 7.3

 | 1× B200
 | C64
 | 3,555.6
 | 66.9
 | 2,104 / 9,629
 | 15.9 / 17.4

 | 1× B200
 | C256
 | 4,836.7
 | 27.6
 | 3,478 / 38,804
 | 48.9 / 51.3

 | 1× H100
 | C1
 | 326.3
 | 351.4
 | 152 / 159
 | 2.9 / 2.9

 | 1× H100
 | C16
 | 1,438.3
 | 103.6
 | 1,231 / 2,026
 | 9.9 / 10.9

 | 1× H100
 | C64
 | 2,635.2
 | 44.4
 | 1,035 / 8,404
 | 23.2 / 24.0

 | 1× H100
 | C256
 | 4,612.2
 | 23.4
 | 1,812 / 33,594
 | 52.5 / 53.6

Methodology

Measured on 1× NVIDIA B200 GPU and 1× NVIDIA H100 GPU with vLLM, tensor parallel size 1 (TP1), using the official nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 checkpoint. The workload used approximately 8,192 input tokens and 1,024 output tokens per request, 512 prompts per concurrency point, and concurrency swept from 1 to 256 (labels C1–C256). Both lanes use one GPU, so system and per-GPU output throughput are identical. The B200 lane runs native NVFP4 execution; NVIDIA's comparative-benchmark contract applies H100-only server arguments (--moe-backend=humming, --linear-backend=humming, --mamba-ssu-algorithm=horizontal) because Hopper executes this NVFP4 checkpoint through documented W4A16 Humming fallback kernels rather than native FP4 math.

## Background

NVIDIA Nemotron-3.5-Lightning-30B-A3B is NVIDIA's latency-optimized member of the Nemotron 3.5 family. It pairs a Mixture-of-Experts feed-forward stack (128 routed experts, six active per token, plus one shared expert) with interleaved Mamba-2 state-space layers and a handful of full-attention layers. The result is 30B total parameters but only ~3B active per token, and near-linear scaling in sequence length because most layers avoid quadratic attention. Reasoning ("thinking") can be toggled on or off through the chat template, and the model ships with Multi-Token Prediction plus separate speculative-decoding drafters (DFlash, DSpark) for teams that want to push single-stream latency further. NVIDIA publishes an official NVFP4 checkpoint, so on NVIDIA Blackwell the expert weights run in native 4-bit floating point — roughly 22 GB on disk — which is what makes single-GPU deployment practical.

## Model specifications

### Overview

- Name: NVIDIA Nemotron-3.5-Lightning-30B-A3B (NVFP4)

- Author: NVIDIA

- Architecture: Hybrid Mamba-2 + Mixture-of-Experts + Attention (NemotronHForCausalLM, nemotron_h); 52 layers, 128 routed experts (top-6) + 1 shared, 8 attention layers (GQA 32 query / 2 KV heads, head dim 128), hidden size 2,688, Multi-Token Prediction

- License: OpenMDW-1.1

### Specifications

- Parameters: 30B total / ~3B active per token

- Context window: up to 1,048,576 tokens

- Precision / checkpoint: NVFP4 — MoE expert weights 4-bit FP4 (group size 16, W4A16); Mamba in/out projections and KV cache FP8

- Weights on disk: ~21.6 GB (52 safetensors shards)

## Hardware requirements

The NVFP4 checkpoint fits comfortably on a single NVIDIA Blackwell GPU (B200), tensor parallelism of 1, leaving the remaining seven GPUs of an NVIDIA HGX B200 free for other work. Native FP4 tensor cores on Blackwell run the 4-bit experts directly; the same checkpoint also runs on NVIDIA Hopper (H100) via a W4A16 fallback path, and on NVIDIA Ampere (A100) similarly.

## Deployment and benchmarking

### Deploying NVIDIA Nemotron-3.5-Lightning-30B-A3B (NVFP4)

docker run --gpus '"device=0"' -p 8000:8000 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:v0.27.1 \
 --model nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 \
 --served-model-name nemotron-3.5-lightning \
 --tensor-parallel-size 1 --max-model-len 131072 \
 --gpu-memory-utilization 0.9 --kv-cache-dtype fp8 \
 --max-num-seqs 256 --max-num-batched-tokens 16384 \
 --reasoning-parser nemotron_v3 --tool-call-parser qwen3_coder --enable-auto-tool-choice

### Deploying with SGLang

docker run --gpus '"device=0"' -p 8000:8000 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:dev-nemotron3-5-lightning \
 python3 -m sglang.launch_server \
 --model-path nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 \
 --served-model-name nemotron-3.5-lightning \
 --tp 1 --mem-fraction-static 0.85 --context-length 262144 \
 --mamba-backend flashinfer --mamba-ssm-dtype float16 \
 --enable-mamba-cache-stochastic-rounding --mamba-cache-philox-rounds 5 \
 --cuda-graph-max-bs-decode 16 \
 --reasoning-parser nemotron_3 --tool-call-parser qwen3_coder

### Verifying the server

curl http://localhost:8000/v1/models

### Benchmarking

Results are in the benchmark summary table above. Both GPU lanes were driven with AIPerf at approximately 8,192 input / 1,024 output tokens, 512 requests per concurrency point, swept across nine concurrency levels (1–256).

## Next steps

To get started, launch an NVIDIA HGX B200 instance on Lambda and run one of the commands above. Useful resources:

- Model card: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4

- BF16 reference weights: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16

- Speculative-decoding drafters: DFlash and DSpark (NVFP4) for lower single-stream latency

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
