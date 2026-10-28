# MiniMaxAI/MiniMax-M3

Source: https://lambda.ai/inference-models/minimaxai/minimax-m3

Skip to main content

# How to deploy MiniMax-M3 on Lambda

## TL;DR: token throughput

Measured on NVIDIA HGX B200, CUDA 12.8. 8192 in / 2048 out tokens, 32 concurrent requests.

SGLang vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 1,627.79 tok/s
 | 50.87 tok/s
 | 8,138.97 tok/s
 | 3,890.10 ms
 | 17.77 ms

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 1,619.51 tok/s
 | 50.61 tok/s
 | 8,097.56 tok/s
 | 1,440.30 ms
 | 19.06 ms

### Benchmark command

(8192 in / 2048 out tokens, 32 parallel requests, 512 prompts. Measured on NVIDIA HGX B200 with CUDA 12.8.)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document-analysis workflows.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model MiniMaxAI/MiniMax-M3 \
 --served-model-name minimax-m3 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking MiniMax-M3 below for the full results.

## Background

MiniMax-M3 is a natively multimodal Mixture-of-Experts (MoE) model that takes text, image, and video as input and returns text. It's a 428B parameter model with 23B active, and it serves a context window of one million tokens. The defining change is MiniMax Sparse Attention (MSA), a block-sparse attention scheme that lets the model reach that million-token window while cutting per-token compute to roughly one twentieth. This still delivers more than 9x faster prefill and more than 15x faster decode at 1M tokens than MiniMax M2.

MSA works by giving each attention layer a lightweight indexing stage that scores the preceding context in 128-token blocks and keeps only the sixteen most relevant ones, so every query attends to a fixed budget of about 2,048 tokens no matter how long the sequence grows. That selector is trained to imitate where full attention actually wants to look, using a KL alignment loss with a stop-gradient so it never disturbs the rest of the model, an approach that also makes it possible to convert an existing dense checkpoint into a sparse one. The first three layers stay dense, with MSA engaging from the fourth layer onward. M3 also moves well beyond the text-only M2 in two respects: it learns from mixed text, image, and video data starting at the first training step, which the team credits for deeper semantic fusion across the modalities, and it exposes an adaptive reasoning mode that lets the model itself decide when extra deliberation is worth the added latency.

The model is aimed at agentic and coding work. It reports 59.0% on SWE-Bench Pro, 66.0% on Terminal-Bench 2.1, and 70.06% on OSWorld-Verified for computer use. MiniMax positions these as frontier-adjacent results delivered at a fraction of the serving cost rather than outright state-of-the-art. It notes that several of the agentic numbers were measured on its own scaffolding and awaited independent verification at release.

## Model specifications

### Overview

- Name: MiniMax-M3

- Author: MiniMax

- Architecture: MoE (native multimodal MoE with MiniMax Sparse Attention)

- License: minimax-community (custom)

### Specifications

- Total parameters: 428B (23B active per token)

- Context window: 1,048,576 (1M) tokens

- Languages: M3 accepts text, image, and video as input and returns text.

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA HGX B200 is required.

## Deployment and benchmarking

### Deploying MiniMax-M3

MiniMax-M3 is served on a full NVIDIA HGX B200 with tensor parallelism across all 8 GPUs.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image: NVIDIA HGX B200 (8× NVIDIA B200 GPUs). These benchmarks were run with CUDA 12.8 (driver 570).

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using one of the backends below.

SGLang vLLM

CUDA version note: The lmsysorg/sglang:dev-cu13-minimax-m3 image runs the fa4 (FlashAttention-4) backend, which is stable on CUDA 12.8 (driver 570). These benchmarks were run there. On CUDA 13 (driver 580) the fa4 sm100 kernel currently faults on the first inference request; use the vLLM backend on CUDA 13 instead.

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:dev-cu13-minimax-m3 \
 python3 -m sglang.launch_server \
 --model-path MiniMaxAI/MiniMax-M3 \
 --served-model-name minimax-m3 \
 --tp 8 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --mem-fraction-static 0.65 \
 --attention-backend fa4 \
 --page-size 128 \
 --moe-runner-backend deep_gemm

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:minimax-m3 \
 --model MiniMaxAI/MiniMax-M3 \
 --served-model-name minimax-m3 \
 --tensor-parallel-size 8 \
 --trust-remote-code \
 --block-size 128 \
 --tool-call-parser minimax_m3 \
 --reasoning-parser minimax_m3 \
 --enable-auto-tool-choice

#### Verify the server

Either command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see minimax-m3 listed in the response.

### Benchmarking MiniMax-M3

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests. Measured on NVIDIA HGX B200 with CUDA 12.8.

SGLang vLLM

NVIDIA HGX B200

Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,627.79

 | Total (input & output)
 | 8,138.97

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 3,890.10
 | 6,549.91

 | Time per output token
 | 17.77
 | 19.52

 | Inter-token latency
 | 17.77
 | 17.60

NVIDIA HGX B200

Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,619.51

 | Total (input & output)
 | 8,097.56

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 1,440.30
 | 7,791.99

 | Time per output token
 | 19.06
 | 19.63

 | Inter-token latency
 | 19.06
 | 177.08

## Next steps

### Upstream

- Download MiniMax-M3 on Hugging Face

- Announcement blog

### Downstream

Use as a Claude Code backend

Use your self-hosted MiniMax-M3 instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the vLLM server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="minimax-m3"
export ANTHROPIC_DEFAULT_SONNET_MODEL="minimax-m3"
export ANTHROPIC_DEFAULT_OPUS_MODEL="minimax-m3"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax-m3"

export ANTHROPIC_SMALL_FAST_MODEL="minimax-m3"
export ANTHROPIC_FAST_MODEL="minimax-m3"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
