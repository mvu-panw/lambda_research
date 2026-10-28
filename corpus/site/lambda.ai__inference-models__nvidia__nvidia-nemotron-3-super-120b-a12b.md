# nvidia/NVIDIA-Nemotron-3-Super-120B-A12B

Source: https://lambda.ai/inference-models/nvidia/nvidia-nemotron-3-super-120b-a12b

Skip to main content

# How to deploy Nemotron 3 Super on Lambda

## TL;DR: token throughput

### vLLM

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 2× NVIDIA B200 GPUs (NVFP4)
 | 2,057 tok/s
 | 4,040ms
 | 12ms

 | 1× NVIDIA B200 GPU (NVFP4)
 | 1,517 tok/s
 | 4,455ms
 | 16ms

 | 2× NVIDIA B200 GPUs (FP8)
 | 1,847 tok/s
 | 3,948ms
 | 13ms

 | 2× NVIDIA H100 GPUs (FP8)
 | 1,116 tok/s
 | 4,557ms
 | 24ms

 | 4× NVIDIA A100 GPUs (BF16)
 | 553 tok/s
 | 6,694ms
 | 51ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 \
 --served-model-name nemotron-super \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 1024 \
 --num-prompts 512 --max-concurrency 32

(8192 in/1024 out tokens, 32 parallel requests)

## Background

Nemotron 3 Super is a 120B parameter Mixture-of-Experts (MoE) language model from NVIDIA, with only 12.7 billion parameters active per token. It is the first model to employ LatentMoE, a novel MoE variant that projects tokens into a lower-dimensional latent space before expert routing, enabling 512 experts with top-22 routing at the inference cost of a much smaller model. The 88-layer hybrid architecture interleaves Mamba-2 blocks for linear-time sequence processing, LatentMoE FFN blocks, and sparse global attention anchors with shared-weight Multi-Token Prediction (MTP) heads for native speculative decoding.

The model was pre-trained in NVFP4 precision across 25 trillion tokens and is the first model trained at 4-bit floating point at this scale. Post-training introduces PivotRL (assistant-turn-level RL for agentic tasks), a two-stage SFT loss for long-context preservation, and multi-environment RL across 21 environments spanning math, code, tool use, and software engineering.

Nemotron 3 Super achieves competitive accuracy with GPT-OSS-120B and Qwen3.5-122B-A10B, including TerminalBench 2.0, HLE, and long context benchmarks, while delivering 2.2× and 7.5× higher inference throughput respectively. The model supports up to 1 million tokens of context and configurable reasoning modes (full, low-effort, and off).

## Model specifications

### Overview

- Name: Nemotron 3 Super

- Author: NVIDIA

- Architecture: NemotronH (Hybrid Mamba-2 + LatentMoE + Attention with MTP)

- License: NVIDIA Nemotron Open Model License

### Specifications

- Total parameters: 120.6B (12.7B active per token)

- Context window: 262,144 tokens (extendable to 1,000,000)

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA B200 GPU with NVFP4 variant (--tensor-parallel-size 1)

- 2× NVIDIA B200 GPUs or 2× NVIDIA H100 GPUs with FP8 variant (--tensor-parallel-size 2)

- 4× NVIDIA A100 GPUs with BF16 variant (--tensor-parallel-size 4)

## Deployment and benchmarking

### Deploying Nemotron 3 Super

Nemotron 3 Super requires 1× NVIDIA B200 GPU (NVFP4), 2× NVIDIA B200 GPUs / 2× NVIDIA H100 GPUs (FP8), or 4× NVIDIA A100 GPUs (BF16) to load the model. Choose the variant that matches your hardware:

 | Hardware
 | Variant
 | HF Model Path
 | TP Size

 | 2× NVIDIA B200 GPUs
 | NVFP4
 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
 | 2

 | 1× NVIDIA B200 GPU
 | NVFP4
 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4
 | 1

 | 2× NVIDIA B200 GPUs
 | FP8
 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8
 | 2

 | 2× NVIDIA H100 GPUs
 | FP8
 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8
 | 2

 | 4× NVIDIA A100 GPUs
 | BF16
 | nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16
 | 4

- Launch an instance with at least 1× B200 (for NVFP4), 2× B200 / 2× H100 (for FP8), or 4× A100 (for BF16) from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

#### vLLM

# NVFP4 on 1× B200 (TP=1)
# For FP8: use -FP8 model and --tensor-parallel-size 2
# For BF16: use -BF16 model and --tensor-parallel-size 4
docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:latest \
 --host 0.0.0.0 \
 --port 8000 \
 --model nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4 \
 --served-model-name nemotron-super \
 --trust-remote-code

This launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see nemotron-super listed in the response.

### Benchmarking results: Nemotron 3 Super

#### vLLM

Token throughput:

 | Metric
 | 2× B200 (NVFP4)
 | 1× B200 (NVFP4)
 | 2× B200 (FP8)
 | 2× H100 (FP8)
 | 4× A100 (BF16)

 | Output gen (tok/s)
 | 2,057
 | 1,517
 | 1,847
 | 1,116
 | 553

 | Total (tok/s)
 | 18,515
 | 13,650
 | 16,625
 | 10,040
 | 4,974

Latency (Mean in ms):

 | Metric
 | 2× B200 (NVFP4)
 | 1× B200 (NVFP4)
 | 2× B200 (FP8)
 | 2× H100 (FP8)
 | 4× A100 (BF16)

 | TTFT
 | 4,040
 | 4,455
 | 3,948
 | 4,557
 | 6,694

 | ITL
 | 12
 | 16
 | 13
 | 24
 | 51

## Next steps

### Upstream

- Download Nemotron 3 Super BF16 on Hugging Face

- Download Nemotron 3 Super FP8 on Hugging Face

- Download Nemotron 3 Super NVFP4 on Hugging Face

- Nemotron 3 Super Technical Report

### Downstream

Verify tool-use with tau-bench

Confirm the model handles function-calling correctly before using it in production with openbench:

VLLM_API_KEY=dummy \
OPENAI_API_KEY=dummy \
OPENAI_BASE_URL=http://localhost:8002/v1 \
uv run \
 --with openbench[tau_bench] \
 --with "tau2 @ git+https://github.com/sierra-research/tau2-bench.git" \
 bench eval --alpha tau_bench_retail \
 --model vllm/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4-vLLM \
 --model-base-url http://localhost:8002/v1 \
 -T user_model=openai/NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4-vLLM \
 --limit 10

Use as a Claude Code backend

Use your self-hosted model instead of Anthropic's API for local development:

export ANTHROPIC_BASE_URL=http://localhost:8000
claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
