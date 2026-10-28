# zai-org/GLM-5.2

Source: https://lambda.ai/inference-models/zai-org/glm-5.2

Skip to main content

# How to deploy GLM-5.2 on Lambda

## TL;DR: token throughput

Measured on NVIDIA HGX B200, CUDA 12.8. 8192 in / 2048 out tokens, 32 concurrent requests.

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 1,454.07 tok/s
 | 45.44 tok/s
 | 7,270.35 tok/s
 | 5,403.88 ms
 | 19.38 ms

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 1,264.08 tok/s
 | 39.50 tok/s
 | 6,320.40 tok/s
 | 1,913.21 ms
 | 24.38 ms

### Benchmark command

(8192 in / 2048 out tokens, 32 parallel requests, 512 prompts. Measured on NVIDIA HGX B200 with CUDA 12.8.)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document-analysis workflows.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model zai-org/GLM-5.2-FP8 \
 --served-model-name glm-5.2-fp8 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking GLM-5.2 below for the full results.

## Background

GLM-5.2 is Z.ai's flagship open-weight model for long-horizon agentic work, the third release in the GLM-5 family. It's a Mixture-of-Experts (MoE) model built on the glm_moe_dsa architecture, with roughly 753B parameters and 32B active. The major change over GLM-5.1 is architectural: GLM-5.2 ships a 1M-token context window, up from roughly 198K in its predecessors, and sustains it efficiently through a technique called IndexShare.

GLM-5 already used DeepSeek Sparse Attention to keep the core attention cheap at long context. But its per-layer indexer, the component that scores prior tokens to decide what each query attends to, still grew quadratically and ran at every layer. IndexShare exploits the observation that top-k selections change little between adjacent layers, so it computes a fresh indexer only once every four sparse layers and lets the rest reuse the nearest layer's indices. Z.ai reports this cuts per-token FLOPs by 2.9x at 1M context.

Beyond the attention work, GLM-5.2 builds its long-horizon gains on the asynchronous agent reinforcement-learning post-training introduced with GLM-5 and adds two practical refinements. Its multi-token prediction layer, which doubles as a built-in draft model for speculative decoding, was improved to raise the accepted draft length by up to 20%. The model also exposes adjustable thinking-effort levels, so a coding agent can spend more reasoning on a hard repository task and less on a trivial edit. It's released under an MIT license with no regional restrictions.

The combination shows up most clearly on agentic coding and long-horizon suites. Against GLM-5.1, GLM-5.2 moves DeepSWE from 18.0 to 46.2, Terminal-Bench 2.1 (Terminus-2) from 63.5 to 81.0, and FrontierSWE dominance from 30.5 to 74.4, while SWE-Marathon, a very long-horizon test run at 1M context, climbs from 1.0 to 13.0. Gains on more established suites are steadier, with SWE-bench Pro reaching 62.1 and AIME 2026 at 99.2. The largest jumps land squarely on the long-context, multi-round tasks that the 1M window and the agentic post-training are built to serve. This is a useful signal for teams weighing it for extended coding and tool-use workflows.

## Model specifications

### Overview

- Name: GLM-5.2

- Author: Z.ai (Zhipu AI / zai-org)

- Architecture: MoE (glm_moe_dsa)

- License: MIT

### Specifications

- Total parameters: ~753B total (~32B active)

- Context window: 1,000,000 (1M) tokens

- Languages: English and Chinese (en, zh)

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA HGX B200 (NVIDIA HGX B200 system) is required to load the 744B-parameter model. Use the FP8 quantized version (zai-org/GLM-5.2-FP8) for the fastest throughput.

## Deployment and benchmarking

### Deploying GLM-5.2

GLM-5.2 is served on a full NVIDIA HGX B200 (NVIDIA HGX B200) with tensor parallelism across all 8 GPUs.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image: NVIDIA HGX B200. These benchmarks were run with CUDA 12.8 (driver 570).

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using one of the backends below.

 SGLang
 vLLM

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:latest \
 python3 -m sglang.launch_server \
 --model-path zai-org/GLM-5.2-FP8 \
 --served-model-name glm-5.2-fp8 \
 --tp 8 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --mem-fraction-static 0.85 \
 --tool-call-parser glm47 \
 --reasoning-parser glm45

CUDA version note: On CUDA 12.x hosts (Lambda's driver-570 B200 nodes), use the vllm/vllm-openai:glm52-cu129 image, as below. It's the image these benchmarks were run with. On CUDA 13 hosts, use vllm/vllm-openai:glm52.

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:glm52-cu129 \
 --model zai-org/GLM-5.2-FP8 \
 --served-model-name glm-5.2-fp8 \
 --tensor-parallel-size 8 \
 --trust-remote-code \
 --kv-cache-dtype fp8 \
 --tool-call-parser glm47 \
 --reasoning-parser glm45

#### Verify the server

Either command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see glm-5.2-fp8 listed in the response.

### Benchmarking GLM-5.2

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests. Measured on NVIDIA HGX B200 with CUDA 12.8.

 SGLang
 vLLM

NVIDIA HGX B200
Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,454.07

 | Total (input & output)
 | 7,270.35

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 5,403.88
 | 9,479.69

 | Time per output token
 | 19.38
 | 21.67

 | Inter-token latency
 | 19.38
 | 18.27

NVIDIA HGX B200
Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,264.08

 | Total (input & output)
 | 6,320.40

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 1,913.21
 | 9,319.32

 | Time per output token
 | 24.38
 | 25.14

 | Inter-token latency
 | 24.38
 | 331.77

## Next steps

### Upstream

- Download GLM-5.2 on Hugging Face

- Read the official blog post

### Downstream

Use as a noumena code backend

Use your self-hosted GLM-5.2 as the backend to noumena's code framework rather than their hosted models for local development. Replace <NODE_IP> with the IP of the node where the server is running.

git clone https://github.com/noumena-network/code.git
cd code
bun install
bun run build

OPENAI_API_KEY="dummy" \
OPENAI_BASE_URL="http://<NODE_IP>:8000/v1" \
OPENAI_MODEL="glm-5.2-fp8" \
./.tmp/packages/ncode-0.1.0-linux-x64/ncode \
 --print \
 --model glm-5.2-fp8 \
 --max-turns 1 \
 "Reply exactly: ok"

Use as a Claude Code backend

Use your self-hosted GLM-5.2 instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="glm-5.2-fp8"
export ANTHROPIC_DEFAULT_SONNET_MODEL="glm-5.2-fp8"
export ANTHROPIC_DEFAULT_OPUS_MODEL="glm-5.2-fp8"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="glm-5.2-fp8"

export ANTHROPIC_SMALL_FAST_MODEL="glm-5.2-fp8"
export ANTHROPIC_FAST_MODEL="glm-5.2-fp8"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
