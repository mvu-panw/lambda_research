# moonshotai/Kimi-K2.7-Code

Source: https://lambda.ai/inference-models/moonshotai/kimi-k2.7-code

Skip to main content

# How to deploy Kimi-K2.7-Code on Lambda

## TL;DR: token throughput

Measured on NVIDIA HGX B200, CUDA 12.8. 8192 in / 2048 out tokens, 32 concurrent requests.

### vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 1,157.35 tok/s
 | 36.17 tok/s
 | 5,786.74 tok/s
 | 3,312.87 ms
 | 26.03 ms

### Benchmark command

(8192 in / 2048 out tokens, 32 parallel requests, 512 prompts. Measured on NVIDIA HGX B200 with CUDA 12.8.)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document-analysis workflows.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model moonshotai/Kimi-K2.7-Code \
 --served-model-name kimi-k2.7-code \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking Kimi-K2.7-Code below for the full results.

## Background

Kimi-K2.7-Code is Moonshot AI's coding-focused member of the Kimi K2 family. Moonshot took the K2.6 checkpoint and specialized it for long-horizon software engineering through reinforcement learning on the read, plan, edit, run, and debug loop that real coding work demands, often stretched across hundreds of steps. They also tuned it to spend roughly 30% fewer reasoning tokens than K2.6 while holding or improving quality, which matters because output tokens dominate the cost of running a reasoning model over a long session. Thinking is always on and cannot be turned off, and the model carries its full reasoning forward across turns rather than discarding it after each one, so a number or plan it worked out earlier remains available later in the conversation.

The coding-specific tuning is evident across Moonshot's reported benchmarks, every one of which improves over K2.6. Kimi Code Bench v2 rises from 50.9 to 62.0, a 21.8% gain; Program Bench moves from 48.3 to 53.6; and MLS-Bench-Lite climbs from 26.7 to 35.1, up 31.5%.

## Model specifications

### Overview

- Name: Kimi-K2.7-Code

- Author: Moonshot AI

- Architecture: Mixture-of-Experts (DeepSeek-V3-style MoE backbone with Multi-head Latent Attention; multimodal kimi_k25 architecture with a MoonViT vision encoder)

- License: Modified MIT

### Specifications

- Total parameters: 1T total (32B active)

- Context window: 256k (262,144) tokens

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA HGX B200 (8× NVIDIA B200 GPU system) is required.

## Deployment and benchmarking

### Deploying Kimi-K2.7-Code

Kimi-K2.7-Code is served on a full NVIDIA HGX B200 with tensor parallelism across all 8 GPUs.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image — NVIDIA HGX B200. These benchmarks were run with CUDA 12.8 (driver 570).

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server.

#### vLLM

CUDA version note: Kimi-K2.7-Code has no published vendor image. These benchmarks were run with the vLLM nightly vllm/vllm-openai:nightly-e312c5cb25427e76fc3830ab14e7b6bc0963a55c on a CUDA 12.8 host; substitute the current vLLM nightly if that tag is unavailable.

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:nightly-e312c5cb25427e76fc3830ab14e7b6bc0963a55c \
 --model moonshotai/Kimi-K2.7-Code \
 --served-model-name kimi-k2.7-code \
 --tensor-parallel-size 8 \
 --trust-remote-code \
 --mm-encoder-tp-mode data \
 --tool-call-parser kimi_k2 \
 --reasoning-parser kimi_k2 \
 --enable-auto-tool-choice

#### Verify the server

This launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see kimi-k2.7-code listed in the response.

### Benchmarking Kimi-K2.7-Code

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests. Measured on NVIDIA HGX B200 with CUDA 12.8.

#### vLLM

NVIDIA HGX B200

Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,157.35

 | Total (input & output)
 | 5,786.74

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 3,312.87
 | 29,902.17

 | Time per output token
 | 26.03
 | 31.07

 | Inter-token latency
 | 26.03
 | 369.65

## Next steps

### Upstream

- Download Kimi-K2.7-Code on Hugging Face

- Read the release blog post

### Downstream

Use as a noumena code backend

Use your self-hosted Kimi-K2.7-Code as the backend to noumena's code framework rather than their hosted models for local development. Replace <NODE_IP> with the IP of the node where the server is running.

git clone https://github.com/noumena-network/code.git
cd code
bun install
bun run build

OPENAI_API_KEY="dummy" \
OPENAI_BASE_URL="http://<NODE_IP>:8000/v1" \
OPENAI_MODEL="kimi-k2.7-code" \
./.tmp/packages/ncode-0.1.0-linux-x64/ncode \
 --print \
 --model kimi-k2.7-code \
 --max-turns 1 \
 "Reply exactly: ok"

Use as a Claude Code backend

Use your self-hosted Kimi-K2.7-Code instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the vLLM server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="kimi-k2.7-code"
export ANTHROPIC_DEFAULT_SONNET_MODEL="kimi-k2.7-code"
export ANTHROPIC_DEFAULT_OPUS_MODEL="kimi-k2.7-code"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="kimi-k2.7-code"

export ANTHROPIC_SMALL_FAST_MODEL="kimi-k2.7-code"
export ANTHROPIC_FAST_MODEL="kimi-k2.7-code"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
