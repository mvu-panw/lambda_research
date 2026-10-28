# deepseek-ai/DeepSeek-V4.1-Flash

Source: https://lambda.ai/inference-models/deepseek-ai/deepseek-v4.1-flash

Skip to main content

# How to deploy DeepSeek-V4.1-Flash on Lambda

## Performance

DeepSeek-V4.1-Flash

4× NVIDIA B200 GPUs · vLLM TP4

4,859 output tok/s maximum throughput

411 tok/s/user at interactive latency

C8 — Pareto-optimal balance

### Benchmark summary

 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | C1
 | 374.8
 | 410.8
 | 178 / 184
 | 2.5 / 3.2

 | C16
 | 2,314.7
 | 156.1
 | 203 / 1,940
 | 6.6 / 9.1

 | C64
 | 3,713.9
 | 66.8
 | 359 / 9,083
 | 15.9 / 23.8

 | C256
 | 4,858.7
 | 29.6
 | 2,314 / 40,375
 | 41.4 / 69.3

Methodology

Measured on 4× NVIDIA B200 GPUs (a half NVIDIA HGX B200 system) with vLLM, tensor parallel size 4 (TP4), using the official deepseek-ai/DeepSeek-V4.1-Flash checkpoint running language-model-only (text path; the model's image understanding was not exercised by this text-only synthetic workload) with its DSpark speculative-decoding module enabled (5 speculative tokens, probabilistic draft sampling, block rejection sampling, adaptive verification). The workload used approximately 8,192 input tokens and 1,024 output tokens per request, 512 prompts per concurrency point, concurrency swept from 1 to 256 (labels C1–C256). This card reports NVIDIA B200 results only — DeepSeek-V4.1-Flash was not benchmarked on NVIDIA H100 for this card, and no H100 performance is implied.

## Background

DeepSeek-V4.1-Flash is DeepSeek-AI's successor to the DeepSeek-V4-Flash line, and architecturally distinct from the earlier DeepSeek-V4-Flash-0731 checkpoint already on file — its specifications below are sourced from DeepSeek's own model card, not inferred from that sibling. DeepSeek describes it as a "Causal Encoder-Decoder (CED)" design: a 40-layer Transformer organized as a 20-layer causal encoder followed by a 20-layer decoder, totaling approximately 552 billion backbone parameters, of which only about 8 billion are active per token during prefill and about 16 billion during decode. Its Mixture-of-Experts layers route to 1 shared expert plus 384 routed experts, activating 6 routed experts per token. The model also incorporates a 196-billion-parameter "Engram memory" that is sparsely accessed via token-based lookup rather than densely computed.

DeepSeek reports the model uses Compressed Sparse Attention 2 (CSA2) with FP4 main KV caching (E2M1 format, one E4M3 scale per 16 channels), bringing the global KV-cache footprint to approximately 890 bytes per token — about one-quarter of DeepSeek-V4-Flash's. It supports a context window of up to 1 million tokens, a continuously controllable reasoning-effort dial (1–100), and multimodal (image and text) input, and ships under the MIT license. DeepSeek's own reported scores include DeepSWE v1.1 at 74.2%, Terminal-Bench 2.1 at 90.6%, GPQA Diamond at 90.9%, and HumanEval Pass@1 at 79.4% — vendor-reported figures, not independently reproduced here.

## Model specifications

### Overview

- Name: DeepSeek-V4.1-Flash

- Author: DeepSeek-AI

- Architecture: Causal Encoder-Decoder (CED) — 40-layer Transformer (20-layer causal encoder + 20-layer decoder) with Compressed Sparse Attention 2 (CSA2) and a sparsely-accessed Engram memory

- License: MIT

### Specifications

- Total parameters: 552B backbone (8B active per token at prefill, ~16B active at decode); plus a 196B-parameter sparsely-accessed Engram memory

- Experts: 1 shared expert + 384 routed experts per MoE layer, 6 routed experts activated per token

- Context window: up to 1,048,576 (1M) tokens

- Modality: Multimodal — image and text input

- Precision: FP4 main KV cache (E2M1, one E4M3 scale per 16 channels); ~890 bytes/token KV-cache footprint — official deepseek-ai/DeepSeek-V4.1-Flash checkpoint

## Hardware requirements

- Minimal deployment (as benchmarked):

- 4× NVIDIA B200 GPUs (a half NVIDIA HGX B200 system) — served at TP=4. This card does not report an H100 configuration.

## Deployment and benchmarking

### Deploying DeepSeek-V4.1-Flash

DeepSeek-V4.1-Flash is served on 4× NVIDIA B200 GPUs with tensor-parallel size 4.

- Launch an instance with 4× NVIDIA B200 GPUs (or a full NVIDIA HGX B200 system) from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

docker run -d --gpus '"device=0,1,2,3"' -p 18080:18080 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:deepseekv41-flash-0909 \
 --model deepseek-ai/DeepSeek-V4.1-Flash \
 --served-model-name deepseek-ai/DeepSeek-V4.1-Flash \
 --host 0.0.0.0 --port 18080 \
 --tensor-parallel-size 4 \
 --tokenizer-mode deepseek_v41 \
 --language-model-only \
 --max-model-len 16384 \
 --max-num-seqs 256 \
 --gpu-memory-utilization 0.90 \
 --speculative-config '{"method":"dspark","num_speculative_tokens":5,"draft_sample_method":"probabilistic","rejection_sample_method":"block","enable_adaptive_verification":true}'

### Verify the server

curl -X GET http://localhost:18080/v1/models \
 -H "Content-Type: application/json"

You should see deepseek-ai/DeepSeek-V4.1-Flash listed in the response.

### Benchmarking

Results are in the benchmark summary table above, measured with AIPerf at approximately 8,192 input / 1,024 output tokens, 512 requests per concurrency point, swept across nine concurrency levels (1–256), B200 only.

## Next steps

### Upstream

- Download DeepSeek-V4.1-Flash on Hugging Face

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
