# Qwen/Qwen3.5-122B-A10B

Source: https://lambda.ai/inference-models/qwen/qwen3.5-122b-a10b

Skip to main content

# How to deploy Qwen3.5-122B-A10B on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 4× B200
 | 2,197 tok/s
 | 1,156ms
 | 13ms

 | 8× H100
 | 1,585 tok/s
 | 2,613ms
 | 18ms

 | 8× A100
 | 930 tok/s
 | 4,602ms
 | 30ms

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 4× B200
 | 1,817 tok/s
 | 4,904ms
 | 13ms

 | 8× H100
 | 1,843 tok/s
 | 1,060ms
 | 16ms

 | 8× A100
 | 744 tok/s
 | 7,612ms
 | 35ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --model Qwen/Qwen3.5-122B-A10B \
 --served-model-name qwen35-122b \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 1024 \
 --num-prompts 512 --max-concurrency 32

(8192 in/1024 out tokens, 32 parallel requests)

## Background

Qwen3.5-122B-A10B is part of the Qwen3.5 model family, released alongside the flagship Qwen3.5-397B-A17B. The family includes a range of MoE and dense models to suit different deployment constraints:

- MoE models: 397B-A17B, 122B-A10B, 35B-A3B (the "A" indicates active parameters per forward pass)

- Dense model: 27B (standard transformer, no routing overhead)

- Base variants: Available with -Base suffix for fine-tuning

With 122 billion total parameters and only 10 billion active per token, Qwen3.5-122B-A10B offers a middle ground between the flagship 397B and smaller models. It uses the same hybrid Gated DeltaNet + MoE architecture, combining linear attention layers with full attention in a 3:1 ratio for efficient long-context processing.

The model supports 256k tokens natively and shares the same training innovations as its larger sibling: multi-token prediction for speculative decoding, 512 experts with sparse activation, and unified vision-language capabilities.

## Model specifications

### Overview

- Name: Qwen3.5-122B-A10B

- Author: Alibaba Cloud

- Architecture: MoE + Gated DeltaNet

- License: Apache-2.0

### Specifications

- Total parameters: 122B (10B active per forward pass)

- Context window: 256k tokens

- Languages: 201 languages and dialects

## Hardware requirements

- Minimal deployment:

- 4× NVIDIA B200 GPU (--tp-size 4)

- 8× NVIDIA H100 GPU (--tp-size 8)

- 8× NVIDIA A100 GPU (--tp-size 8)

## Deployment and benchmarking

### Deploying Qwen3.5-122B-A10B

Qwen3.5-122B-A10B requires 4× NVIDIA B200 GPU, 8× NVIDIA H100 GPU, or 8× NVIDIA A100 GPU to load the model.

- Launch an instance with 4× B200, 8× H100, or 8× A100 from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

 SGLang
 vLLM

# Use --tp-size 4 for 4× B200, --tp-size 8 for 8× H100 or 8× A100
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
 --model-path Qwen/Qwen3.5-122B-A10B \
 --served-model-name qwen35-122b \
 --tool-call-parser qwen3_coder \
 --reasoning-parser qwen3 \
 --tp-size 8 \
 --trust-remote-code \
 --mem-fraction-static 0.85

# Use --tensor-parallel-size 4 for 4× B200, --tensor-parallel-size 8 for 8× H100 or 8× A100
docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:latest \
 --host 0.0.0.0 \
 --port 8000 \
 --model Qwen/Qwen3.5-122B-A10B \
 --served-model-name qwen35-122b \
 --enable-auto-tool-choice \
 --tool-call-parser qwen3_coder \
 --tensor-parallel-size 8 \
 --trust-remote-code

This launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see qwen35-122b listed in the response.

### Benchmarking results: Qwen3.5-122B-A10B

 SGLang
 vLLM

Token throughput:

 | Metric
 | 4× B200
 | 8× H100
 | 8× A100

 | Output gen (tok/s)
 | 2,197
 | 1,585
 | 930

 | Total (tok/s)
 | 19,770
 | 14,262
 | 8,372

Latency (Mean / P99 in ms):

 | Metric
 | 4× B200
 | 8× H100
 | 8× A100

 | TTFT
 | 1,156 / 3,226
 | 2,613 / 5,533
 | 4,602 / 9,964

 | TPOT
 | 13 / 14
 | 18 / 20
 | 30 / 34

 | ITL
 | 13 / 15
 | 18 / 37
 | 30 / 93

Token throughput:

 | Metric
 | 4× B200
 | 8× H100
 | 8× A100

 | Output gen (tok/s)
 | 1,817
 | 1,843
 | 744

 | Total (tok/s)
 | 16,355
 | 16,589
 | 6,700

Latency (Mean / P99 in ms):

 | Metric
 | 4× B200
 | 8× H100
 | 8× A100

 | TTFT
 | 4,904 / 68,885
 | 1,060 / 5,328
 | 7,612 / 105,377

 | TPOT
 | 13 / 13
 | 16 / 17
 | 36 / 41

 | ITL
 | 13 / 102
 | 16 / 135
 | 35 / 181

## Next steps

### Upstream

- Download Qwen3.5-122B-A10B on Hugging Face

- Qwen3.5 model collection

### Downstream

Verify tool-use with tau-bench

Confirm the model handles function-calling correctly before using it in production with openbench:

uv run --with openbench[tau_bench] bench eval tau_bench_retail \
 --model openai/qwen35-122b \
 -M base_url=http://localhost:8000/v1 \
 --limit 10

Use as a Claude Code backend

Use your self-hosted model instead of Anthropic's API for local development:

export ANTHROPIC_BASE_URL=http://localhost:8000
claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
