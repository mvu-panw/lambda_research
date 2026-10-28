# nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4

Source: https://lambda.ai/inference-models/nvidia/nvidia-nemotron-3-super-120b-a12b-nvfp4

Skip to main content

# How to deploy NVIDIA Nemotron-3-Super-120B-A12B NVFP4 on Lambda

## Performance

NVIDIA Nemotron-3-Super-120B-A12B NVFP4

2× NVIDIA B200 GPUs or 2× NVIDIA H100 GPUs · vLLM TP2

4,937 output tok/s peak measured system throughput on B200 (at C128)

262 tok/s/user at interactive latency on B200

C32 — Pareto-optimal balanceC8 — Pareto-optimal balance

### Benchmark summary

 | Hardware
 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | 2× B200
 | C1
 | 208.3
 | 261.5
 | 131 / 161
 | 4.7 / 4.7

 | 2× B200
 | C16
 | 1,786.1
 | 136.3
 | 954 / 1,459
 | 8.0 / 10.0

 | 2× B200
 | C64
 | 3,745.0
 | 65.8
 | 1,175 / 6,000
 | 15.9 / 16.9

 | 2× B200
 | C256
 | 2,248.5
 | 9.8
 | 992 / 25,034
 | 109.4 / 110.6

 | 2× H100
 | C1
 | 154.5
 | 186.3
 | 415 / 421
 | 6.1 / 6.1

 | 2× H100
 | C16
 | 834.2
 | 64.6
 | 3,358 / 4,584
 | 16.0 / 18.8

 | 2× H100
 | C64
 | 1,412.9
 | 29.4
 | 2,983 / 22,751
 | 42.4 / 44.8

 | 2× H100
 | C256
 | 1,493.0
 | 7.4
 | 3,795 / 95,675
 | 165.0 / 166.6

Methodology

Measured on 2× NVIDIA B200 GPUs and 2× NVIDIA H100 GPUs with vLLM, tensor parallel size 2 (TP2), using the official nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 checkpoint. The workload used approximately 8,192 input tokens and 1,024 output tokens per request, 512 prompts per concurrency point, concurrency swept from 1 to 256 (labels C1–C256). Per-GPU throughput is system throughput divided by 2. NVIDIA's comparative-benchmark contract documented no B200- or H100-specific server-argument overrides for this model.

Observed anomaly, reported as measured, not smoothed: on both GPUs, system throughput and TTFT/ITL both regress at C256 relative to C128 (e.g. B200 drops from 4,937 to 2,248 output tok/s and p50 TTFT drops from 1,186 ms to 992 ms, while p99 TTFT and ITL both spike sharply). AIPerf recorded no cancelled requests or errors for this point (512/512 requests completed on both hardware lanes), so this is not a data-collection failure — it is consistent with KV-cache/memory pressure and request preemption at very high concurrency on a 120B-parameter model running at TP2, which gives it a smaller per-GPU KV-cache budget than the TP1 Nano/Lightning cards in this batch. Treat C128, not C256, as this model's highest validated throughput point on this hardware configuration.

## Background

NVIDIA Nemotron-3-Super-120B-A12B is a member of the NVIDIA Nemotron 3 family, described by NVIDIA as a "LatentMoE" architecture combining Mamba-2, Mixture-of-Experts, and attention layers in a hybrid stack with Multi-Token Prediction (MTP). It is NVIDIA's first Nemotron 3 model trained natively at NVFP4 precision. Per NVIDIA's published model card it totals 120 billion parameters with 12 billion active per token, supports a context window of up to 1 million tokens, and NVIDIA states it runs on a minimum of 1× NVIDIA B200 GPU or 1× NVIDIA DGX Spark — though the comparative benchmark run backing the chart above used 2 GPUs (tensor-parallel size 2), not the vendor-stated single-GPU minimum. Selected NVIDIA-reported scores include MMLU-Pro 83.33, GPQA (no tools) 79.42, and RULER-500 @ 512k context 96.23; these are vendor-reported figures, not independently reproduced here.

## Model specifications

### Overview

- Name: NVIDIA Nemotron-3-Super-120B-A12B (NVFP4)

- Author: NVIDIA

- Architecture: LatentMoE — hybrid Mamba-2 + Mixture-of-Experts + Attention with Multi-Token Prediction; exact layer/expert counts pending confirmation

- License: pending confirmation (not stated on the fetched model-card excerpt)

### Specifications

- Total parameters: 120B total (12B active per token)

- Context window: up to 1,048,576 (1M) tokens

- Precision: Native NVFP4 (NVIDIA's first Nemotron 3 model trained at this precision) — official nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 checkpoint; KV cache FP8, Mamba cache float16

## Hardware requirements

- Minimal deployment per NVIDIA: 1× NVIDIA Blackwell GPU (B200) or 1× NVIDIA DGX Spark.

- As benchmarked here: 2× NVIDIA B200 GPUs or 2× NVIDIA H100 GPUs at tensor-parallel size 2 — this is the configuration the chart and table above measure; it is not necessarily the minimum viable footprint.

## Deployment and benchmarking

### Deploying NVIDIA Nemotron-3-Super-120B-A12B (NVFP4)

Exact launch flags pending full recipe disclosure. The command below reflects the confirmed configuration (vLLM, tensor-parallel 2, FP8 KV cache, float16 Mamba cache) from the comparative-benchmark contract; the full flag set used in the underlying run was not captured in this data handoff.

docker run -d --gpus '"device=0,1"' -p 8000:8000 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:v0.20.0 \
 --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 \
 --served-model-name nvidia/nemotron-3-super \
 --tensor-parallel-size 2 \
 --kv-cache-dtype fp8 \
 --trust-remote-code

### Verify the server

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see nvidia/nemotron-3-super listed in the response.

### Benchmarking

Results are in the benchmark summary table above. Both GPU lanes were driven with AIPerf at approximately 8,192 input / 1,024 output tokens, 512 requests per concurrency point, swept across nine concurrency levels (1–256). See the methodology note above regarding the C256 throughput regression.

## Next steps

### Upstream

- Download NVIDIA Nemotron-3-Super-120B-A12B NVFP4 on Hugging Face

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
