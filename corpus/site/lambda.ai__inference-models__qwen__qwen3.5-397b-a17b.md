# Qwen/Qwen3.5-397B-A17B

Source: https://lambda.ai/inference-models/qwen/qwen3.5-397b-a17b

Skip to main content

# How to deploy Qwen3.5-397B-A17B on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 8× B200
 | 1,269 tok/s
 | 1,943ms
 | 23ms

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 8× B200
 | 1,268 tok/s
 | 5,024ms
 | 20ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --backend openai-chat \
 --model Qwen/Qwen3.5-397B-A17B \
 --served-model-name qwen \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

(8192 in/1024 out tokens, 32 parallel requests)

## Background

Qwen3.5-397B-A17B is a 397 billion parameter multimodal vision-language model from Alibaba's Qwen team, featuring a hybrid Gated DeltaNet and Mixture-of-Experts (MoE) architecture. With only 17 billion parameters active per forward pass, 23% fewer than the prior 235B version despite having 69% more total parameters, it achieves comparable or better performance at lower inference cost.

The model's improved performance is due to several key factors:

- Gated Delta Networks (GDN): A hybrid attention architecture alternating between linear attention (Gated DeltaNet) and full attention layers in a 3:1 ratio, reducing KV-cache memory by approximately 4×

- Scaling the MoE further: 512 experts (4× more than Qwen3's 128) with 10+1 active experts per token

- Multi-token prediction: Enables speculative decoding for 2-3× inference speedup

- Unified vision-language: Early fusion training on trillions of multimodal tokens

Qwen3.5 extends context to 256k tokens natively, making it well-suited for agentic workflows, long-context applications, and code analysis.

## Model specifications

### Overview

- Name: Qwen3.5-397B-A17B

- Author: Alibaba Cloud

- Architecture: MoE

- License: Apache-2.0

### Specifications

- Total parameters: 397B (17B active per forward pass)

- Context window: 256k tokens

- Languages: 201 languages and dialects

## Hardware requirements

- Minimal deployment:

- NVIDIA HGX B200 (1.5 TB)

## Deployment and benchmarking

### Deploying Qwen3.5-397B-A17B

Qwen3.5 requires NVIDIA HGX B200 to load the full 397B parameter model.

- Launch an instance with NVIDIA HGX B200 from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

 SGLang
 vLLM

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:latest \
 python -m sglang.launch_server \
 --host 0.0.0.0 \
 --port 8000 \
 --model-path Qwen/Qwen3.5-397B-A17B \
 --served-model-name qwen \
 --tool-call-parser qwen3_coder \
 --reasoning-parser qwen3 \
 --mamba-ssm-dtype float32 \
 --tp-size 8 \
 --trust-remote-code \
 --mem-fraction-static 0.85

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:latest \
 --host 0.0.0.0 \
 --port 8000 \
 --model Qwen/Qwen3.5-397B-A17B \
 --served-model-name qwen \
 --tensor-parallel-size 8 \
 --trust-remote-code

This launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see Qwen listed in the response.

### Benchmarking results: Qwen3.5-397B-A17B

 SGLang
 vLLM

Token throughput:

 | Metric
 | 8× B200

 | Output gen (tok/s)
 | 1,269

 | Total (tok/s)
 | 11,425

Latency (Mean / P99 in ms):

 | Metric
 | 8× B200

 | TTFT
 | 1,943 / 5,029

 | TPOT
 | 23 / 25

 | ITL
 | 23 / 35

Token throughput:

 | Metric
 | 8× B200

 | Output gen (tok/s)
 | 1,268

 | Total (tok/s)
 | 11,416

Latency (Mean / P99 in ms):

 | Metric
 | 8× B200

 | TTFT
 | 5,024 / 67,955

 | TPOT
 | 20 / 21

 | ITL
 | 20 / 166

## Next steps

### Upstream

- Download Qwen3.5-397B-A17B on Hugging Face

### Downstream

Verify tool-use with tau-bench

Confirm the model handles function-calling correctly before using it in production with openbench:

uv run --with openbench[tau_bench] bench eval tau_bench_retail \
 --model openai/qwen \
 -M base_url=http://localhost:8000/v1 \
 --limit 10

Use as a Claude Code backend

Use your self-hosted model instead of Anthropic's API for local development:

export ANTHROPIC_BASE_URL=http://localhost:8000
claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
