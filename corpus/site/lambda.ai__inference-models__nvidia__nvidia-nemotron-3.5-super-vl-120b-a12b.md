# nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B

Source: https://lambda.ai/inference-models/nvidia/nvidia-nemotron-3.5-super-vl-120b-a12b

Skip to main content

# How to deploy NVIDIA Nemotron 3.5 Super VL on Lambda

## Performance

NVIDIA Nemotron 3.5 Super VL

NVFP4 · 1× NVIDIA Blackwell GPU · SGLang · TP1 — 1,860 output tok/s peak measured system throughput (at C16), 587 tok/s/user single-stream

BF16 · 2× NVIDIA Blackwell GPUs · SGLang · TP2 — 1,669 output tok/s peak measured system throughput (at C16), 530 tok/s/user single-stream

Both paths run multi-token-prediction speculative decoding.

On the same 8,192-input / 1,024-output workload, the NVFP4 path on a single NVIDIA Blackwell GPU out-throughputs the BF16 path on two B200 GPUs, roughly 2.2× the per-GPU throughput, because NVIDIA Blackwell runs FP4 natively.

The following graph demonstrates the speedup by hardware, focusing on a normalized result using tok/s/GPU

C1 — Highest tok/s/userC8 — Pareto-optimal balance

Measured on NVIDIA Blackwell GPUs with SGLang (lmsysorg/sglang:dev-cu13), using NVIDIA's AIPerf harness (nvcr.io/nvidia/ai-dynamo/aiperf) with the following configuration:

- 8,192 input / 1,024 output tokens per request

- Thinking disabled

- Concurrency swept from 1 to 256 (labels C1–C256). 

- Multi-token prediction with EAGLE speculative decoding (5 steps, 6 draft tokens) with the same checkpoint as the draft model, matching NVIDIA's Nemotron 3.5 Super VL cookbook.

Per that cookbook, decode NVIDIA CUDA™ graphs are captured only up to batch size 16 (--cuda-graph-max-bs-decode 16): system throughput therefore peaks at concurrency 16 and regresses beyond it, as requests queue and speculative-decode acceptance gains erode past the graph-captured batch. The useful operating range for this workload is C1–C16; the C32–C256 rows are included for completeness. 

Supplimental graphs showing also time-to-first-token and inter-token latency results from AIPerf can be found here

### Benchmark summary

NVFP4 — 1× NVIDIA Blackwell GPU, SGLang TP1

 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | C1
 | 485.5
 | 587.2
 | 294 / 302
 | 1.74 / 2.59

 | C8
 | 1,447.7
 | 201.2
 | 308 / 2,277
 | 5.02 / 7.71

 | C16
 | 1,860.3
 | 128.3
 | 319 / 3,561
 | 7.97 / 12.09

 | C64
 | 983.6
 | 27.0
 | 22,019 / 48,809
 | 37.70 / 54.82

 | C256
 | 952.6
 | 26.6
 | 136,620 / 236,758
 | 38.07 / 57.64

BF16 — 2× NVIDIA Blackwell GPUs, SGLang TP2

 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | C1
 | 455.4
 | 530.3
 | 239 / 253
 | 1.90 / 2.76

 | C8
 | 1,265.9
 | 173.3
 | 270 / 2,038
 | 5.81 / 8.84

 | C16
 | 1,669.1
 | 113.5
 | 290 / 3,265
 | 9.03 / 13.61

 | C64
 | 1,138.8
 | 44.7
 | 30,301 / 46,230
 | 22.48 / 33.10

 | C256
 | 1,123.3
 | 44.0
 | 150,318 / 213,638
 | 22.91 / 33.56

## Background

NVIDIA Nemotron 3.5 Super VL is an open multimodal model for agents that can see, reason, and act across specialized workflows. It’s the successor to the Nemotron 3 Super line, and the first of that tier to naturally integrate vision into the model. Nemotron 3.5 Super VL serves as a high-accuracy multimodal execution model, alongside Nemotron 3.5 Lightning for high-volume text execution and Nemotron 3 Ultra for the hardest text-only reasoning. Its 120B@12B-active MoE architecture combines text, image, document, GUI, video understanding with agentic reasoning and tool use.

A Hybrid Mamba architecture and MTP help Super VL generate output faster. NVFP4 KV cache quantization reduces KV cache HBM footprint, creating headroom for more concurrent long-context sessions. Vision comes in through NVIDIA's C-RADIOv4 encoder. Organizations can post-train Nemotron 3.5 Super VL with NVIDIA NeMo open libraries using their data, tools, policies, workflows. NVIDIA also reports C-RADIOv4 gains over C-RADIOv3-H: ImageNet zero-shot 82.65 to 83.09, ADE20k segmentation mIoU 52.75 to 55.20.

Read below for how to deploy Nemotron 3.5 Super VL on Lambda compute

## Model specifications

### Overview

- Name: NVIDIA Nemotron 3.5 Super VL (120B-A12B)

- Author: NVIDIA

- Hugging Face: nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B

- Architecture: Hybrid Nemotron-H Mamba-Transformer MoE language backbone (NemotronH_Omni_Reasoning_V3; arXiv:2504.03624) built on Mamba-2 state-space layers (arXiv:2405.21060), with a C-RADIOv4 vision encoder (arXiv:2601.17237), vision projector, and temporal video embedder; Multi-Token Prediction (arXiv:2404.19737) wired as a self-speculative EAGLE draft (arXiv:2401.15077)

- License: TBD

### Specifications

- Total parameters: 120B total (12B active per token)

- Mixture-of-experts: 512 routed experts with 22 active per token, plus 1 shared expert

- Language layers: 88 blocks: 40 Mamba-2, 40 MoE, and 8 full-attention (GQA: 32 query heads, 2 KV heads; hidden size 4,096)

- Vision encoder: C-RADIOv4, an agglomerative Vision Transformer distilled from SigLIP2, DINOv3, and SAM3 (arXiv:2601.17237); 32 layers, hidden size 1,280.

- Context window: up to 1,048,576 (1M) tokens

- Modality: Input: text, images, documents, GUIs, and video. Output: text.

## Hardware requirements

- Minimal deployment (benchmarked):

- NVFP4: 1× NVIDIA Blackwell GPU at TP1. NVIDIA Blackwell runs FP4 natively, so this is the fastest and most hardware-efficient path.

- BF16: 2× NVIDIA Blackwell GPUs at TP2.

## Deployment and benchmarking

Both deployment paths serve the same model with SGLang (lmsysorg/sglang:dev-cu13) under the single served name nemotron-3-5-super-vl, using NVIDIA's Nemotron 3.5 Super VL cookbook flag set: 

- MTP as EAGLE speculative decoding

- --cuda-graph-max-bs-decode 16 (required by the cookbook's MTP path)

- The nemotron_3 reasoning parser, and the qwen3_coder tool-call parser.

NVFP4BF16

docker run -d --name sglang-super-vl-nvfp4 --network=host \
 --gpus '"device=0"' \
 -e SAFETENSORS_FAST_GPU=1 \
 lmsysorg/sglang:dev-cu13 \
 python3 -m sglang.launch_server \
 nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 \
 --served-model-name nemotron-3-5-super-vl \
 --tp-size 1 \
 --trust-remote-code \
 --context-length 1048576 \
 --mamba-backend flashinfer \
 --mamba-ssm-dtype float16 \
 --enable-mamba-cache-stochastic-rounding \
 --mamba-cache-philox-rounds 5 \
 --mem-fraction-static 0.85 \
 --cuda-graph-max-bs-decode 16 \
 --reasoning-parser nemotron_3 \
 --tool-call-parser qwen3_coder \
 --max-running-requests 256 \
 --speculative-algorithm EAGLE \
 --speculative-num-steps 5 \
 --speculative-eagle-topk 1 \
 --speculative-num-draft-tokens 6

docker run -d --name sglang-super-vl-bf16 --network=host \
 --gpus '"device=0,1"' \
 -e SAFETENSORS_FAST_GPU=1 \
 lmsysorg/sglang:dev-cu13 \
 python3 -m sglang.launch_server \
 nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16 \
 --served-model-name nemotron-3-5-super-vl \
 --tp-size 2 \
 --trust-remote-code \
 --context-length 262144 \
 --mamba-ssm-dtype float16 \
 --mem-fraction-static 0.85 \
 --cuda-graph-max-bs-decode 16 \
 --reasoning-parser nemotron_3 \
 --tool-call-parser qwen3_coder \
 --max-running-requests 256 \
 --speculative-algorithm EAGLE \
 --speculative-num-steps 5 \
 --speculative-eagle-topk 1 \
 --speculative-num-draft-tokens 6

### Verify the server

curl -X GET http://localhost:12501/v1/models \
 -H "Content-Type: application/json"

You should see nemotron-3-5-super-vl listed in the response (use port 12500 for the BF16 path on two GPUs).

### AIPerf Benchmark and Supplimental Graphs

Throughput was measured with NVIDIA's AIPerf harness against the running server at 8,192 input / 1,024 output tokens, sweeping concurrency 1–256:

aiperf profile \
 --model nemotron-3-5-super-vl \
 --url 127.0.0.1:12501 \
 --endpoint-type chat \
 --synthetic-input-tokens-mean 8192 --synthetic-input-tokens-stddev 0 \
 --output-tokens-mean 1024 --output-tokens-stddev 0 \
 --concurrency 1,2,4,8,16,32,64,128,256 \
 --extra-inputs '{"ignore_eos":true,"min_tokens":1024,"chat_template_kwargs":{"enable_thinking":false}}' \
 --use-server-token-count

## Next steps

### Upstream

- Read the official announcement blog by NVIDIA

- Find the model on Hugging Face:

- NVFP4

- BF16

- BF16 base weights

### Downstream

Use as an OpenAI-compatible endpoint

The SGLang server exposes an OpenAI-compatible /v1/chat/completions API. Point any OpenAI SDK client at the node's address (replace <NODE_IP>) and the served model name to send multimodal (text + image) requests:

export OPENAI_BASE_URL="http://<NODE_IP>:12501/v1"
export OPENAI_API_KEY="dummy"
# model: nemotron-3-5-super-vl (port 12500 for the BF16 path)

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
