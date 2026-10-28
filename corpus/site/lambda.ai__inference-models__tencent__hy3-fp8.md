# tencent/Hy3-FP8

Source: https://lambda.ai/inference-models/tencent/hy3-fp8

Skip to main content

# How to deploy Hy3 on Lambda

## TL;DR: token throughput (vLLM)

 | Hardware configuration
 | Requests/s
 | Generation throughput (tok/s)
 | Total throughput (tok/s)
 | TTFT (ms)
 | ITL (ms)
 | Prompts
 | Tokens in
 | Tokens out
 | Parallel requests

 | 4× NVIDIA B200 GPUs
 | 0.86
 | 1,756.55
 | 8,782.76
 | 1,607.07
 | 17.44
 | 512
 | 4,194,304
 | 1,048,576
 | 32

The benchmark uses an 8192-input / 2048-output token workload (a 4:1 input-to-output ratio) with a concurrency of 32 over 512 prompts.

Benchmark configuration:

vllm bench serve \
 --backend openai \
 --model tencent/Hy3-FP8 \
 --served-model-name hy3_fp8 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/completions

## Background

Hy3 is Tencent's newest large language model. 295 billion total parameters spread across a mixture-of-experts network, only about 21 billion active per token, plus a 3.8-billion-parameter side network that predicts several future tokens in parallel. The Transformer stack is unchanged from April's Hy3 Preview: 192 experts, one shared expert, a sigmoid router, grouped-query attention, and rotary position embeddings stretching out to 256k positions, all of it exactly as before.

Tencent retrained the non-embedded weights using a larger, higher-quality post-training dataset. Tencent's own evals show hallucinations fell from 12.5% to 5.4% and multi-turn dialogue errors fell from 17.4% to 7.9%. The model can be served on a single 8-GPU node. Apache-2.0 license, both BF16 and official FP8 checkpoints available. Hy3's reasoning and coding scores meet or exceed those of open-weight flagship models two to five times its size, with tool-calling results landing in a comparable range.

## Model specifications

### Overview

- Name: Hy3

- Author: Tencent (Hy Team)

- Architecture: Mixture-of-Experts (MoE) transformer

- License: Apache-2.0

### Specifications

- Total parameters: 295B (21B active per token; 3.8B MTP layer)

- Experts: 192 routed experts, top-8 activated

- Layers: 80 (plus 1 MTP layer)

- Attention: 64 heads (GQA, 8 KV heads, head dim 128)

- Hidden size: 4096; Intermediate size: 13312

- Context window: 256K tokens

- Vocabulary size: 120,832

- Precision: FP8 — official Hy3-FP8 quantization (BF16 weights also published)

## Deployment and benchmarking

### Deploying Hy3-FP8

Hy3-FP8 is served with vLLM using tensor-parallel size 4 on an NVIDIA HGX B200 system.

- Launch an instance with an NVIDIA HGX B200 system from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the vLLM server:

docker run -d \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -e HUGGING_FACE_HUB_TOKEN=$HF_TOKEN \
 -e VLLM_FLASHINFER_ALLREDUCE_BACKEND=trtllm \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:hy3 \
 --model tencent/Hy3-FP8 \
 --served-model-name hy3_fp8 \
 --tensor-parallel-size 4 \
 --host 0.0.0.0 \
 --port 8000 \
 --max-model-len auto \
 --enable-auto-tool-choice \
 --tool-call-parser hy_v3 \
 --reasoning-parser hy_v3 \
 --trust-remote-code \
 --gpu-memory-utilization 0.9 \
 --kv-cache-dtype fp8_e4m3 \
 --block-size 64

This launches a vLLM server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

### Benchmarking Hy3-FP8

Benchmark Hy3-FP8 with vllm bench serve using the 8192 input / 2048 output workload shown above.

Token throughput (NVIDIA HGX B200 system, TP=4):

 | Metric
 | Value

 | Requests per second
 | 0.86 req/s

 | Output generation
 | 1,756.55 tok/s

 | Total (input & output)
 | 8,782.76 tok/s

Latency details (NVIDIA HGX B200, TP=4):

 | Metric
 | Mean (ms)
 | P99 (ms)

 | Time to first token
 | 1,607.07
 | 6,395.97

 | Time per output token
 | 17.44
 | 18.31

 | Inter-token latency
 | 17.44
 | 229.20

## Next steps

### Upstream

- Download Hy3-FP8 on Hugging Face (BF16 base: tencent/Hy3)

- Read the vLLM recipe for Hy3-FP8

- Hy3 on GitHub

### Downstream

Use as a noumena code backend

Use your self-hosted Hy3 as the backend to noumena's code framework rather than their hosted models for local development. Replace <NODE_IP> with the IP of the node where the server is running.

git clone https://github.com/noumena-network/code.git
cd code
bun install
bun run build

OPENAI_API_KEY="dummy" \
OPENAI_BASE_URL="http://<NODE_IP>:8000/v1" \
OPENAI_MODEL="hy3_fp8" \
./.tmp/packages/ncode-0.1.0-linux-x64/ncode \
 --print \
 --model hy3_fp8 \
 --max-turns 1 \
 "Reply exactly: ok"

Use as a Claude Code backend

Use your self-hosted Hy3 instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="hy3_fp8"
export ANTHROPIC_DEFAULT_SONNET_MODEL="hy3_fp8"
export ANTHROPIC_DEFAULT_OPUS_MODEL="hy3_fp8"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="hy3_fp8"

export ANTHROPIC_SMALL_FAST_MODEL="hy3_fp8"
export ANTHROPIC_FAST_MODEL="hy3_fp8"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
