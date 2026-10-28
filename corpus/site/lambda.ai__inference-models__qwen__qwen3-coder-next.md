# Qwen/Qwen3-Coder-Next

Source: https://lambda.ai/inference-models/qwen/qwen3-coder-next

Skip to main content

# How to deploy Qwen3-Coder-Next on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 2× NVIDIA B200 GPUs
 | 1,877 tok/s
 | 1,330ms
 | 16ms

 | 4× NVIDIA H100 GPUs
 | 1,810 tok/s
 | 1,960ms
 | 16ms

 | 4× NVIDIA A100 GPUs
 | 1,069 tok/s
 | 3,969ms
 | 26ms

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 2× NVIDIA B200 GPUs
 | 1,721 tok/s
 | 4,602ms
 | 14ms

 | 4× NVIDIA H100 GPUs
 | 2,180 tok/s
 | 933ms
 | 14ms

 | 4× NVIDIA A100 GPUs
 | 851 tok/s
 | 6,997ms
 | 31ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --model Qwen/Qwen3-Coder-Next \
 --served-model-name qwen3-coder-next \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 1024 \
 --num-prompts 512 --max-concurrency 32

(8192 in/1024 out tokens, 32 parallel requests)

## Background

Qwen3-Coder-Next is an 80-billion-parameter Mixture of Experts (MoE) code model from Alibaba's Qwen team, activating only 3 billion parameters per forward pass. It combines the hybrid Gated DeltaNet architecture from Qwen-Next with specialized code training, achieving 70.6% on SWE-Bench Verified, the highest reported score for an open-weight model (at the time of this model's release). The model was trained on 800k agentic coding tasks using reinforcement learning with execution-based rewards.

The model's strong agentic performance comes from several key design choices:

- Hybrid architecture: Alternating Gated DeltaNet (linear attention) and full attention layers in a 3:1 ratio, reducing KV-cache memory while maintaining reasoning quality

- Agentic RL training: 800K tasks requiring multi-step tool use, file editing, and test execution

- Multi-token prediction: Trained to predict multiple tokens simultaneously, enabling speculative decoding for faster inference

Qwen3-Coder-Next supports 256k tokens natively, making it well-suited for repository-scale code understanding and long-running agentic workflows.

## Model specifications

### Overview

- Name: Qwen3-Coder-Next

- Author: Alibaba Cloud

- Architecture: MoE + Gated DeltaNet

- License: Apache-2.0

### Specifications

- Total parameters: 80B (3B active per forward pass)

- Context window: 256k tokens

## Hardware requirements

- Minimal deployment:

- 2× NVIDIA B200 GPUs (--tp-size 2)

- 4× NVIDIA H100 GPUs (--tp-size 4)

- 4× NVIDIA A100 GPUs (--tp-size 4)

## Deployment and benchmarking

### Deploying Qwen3-Coder-Next

Qwen3-Coder-Next requires 2× NVIDIA B200 GPUs, 4× NVIDIA H100 GPUs, or 4× NVIDIA A100 GPUs.

- Launch an instance with 2× NVIDIA B200 GPUs, 4× NVIDIA H100 GPUs, or 4× NVIDIA A100 from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

 SGLang
 vLLM

# Use --tp-size 2 for 2× B200, --tp-size 4 for 4× H100 or 4× A100
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
 --model-path Qwen/Qwen3-Coder-Next \
 --served-model-name qwen3-coder-next \
 --tool-call-parser qwen3_coder \
 --tp-size 4 \
 --trust-remote-code \
 --mem-fraction-static 0.85

# Use --tensor-parallel-size 2 for 2× B200, --tensor-parallel-size 4 for 4× H100 or 4× A100
docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:latest \
 --host 0.0.0.0 \
 --port 8000 \
 --model Qwen/Qwen3-Coder-Next \
 --served-model-name qwen3-coder-next \
 --enable-auto-tool-choice \
 --tool-call-parser qwen3_coder \
 --tensor-parallel-size 4 \
 --trust-remote-code

This launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see qwen3-coder-next listed in the response.

### Benchmarking results: Qwen3-Coder-Next

 SGLang
 vLLM

Token throughput:

 | Metric
 | 2× B200
 | 4× H100
 | 4× A100

 | Output gen (tok/s)
 | 1,876
 | 1,810
 | 1,069

 | Total (tok/s)
 | 16,890
 | 16,289
 | 9,622

Latency (Mean / P99 in ms):

 | Metric
 | 2× B200
 | 4× H100
 | 4× A100

 | TTFT
 | 1,330 / 3,644
 | 1,960 / 4,489
 | 3,969 / 8,901

 | TPOT
 | 16 / 17
 | 16 / 18
 | 26 / 30

 | ITL
 | 16 / 28
 | 16 / 31
 | 26 / 46

Token throughput:

 | Metric
 | 2× B200
 | 4× H100
 | 4× A100

 | Output gen (tok/s)
 | 1,721
 | 2,180
 | 851

 | Total (tok/s)
 | 15,492
 | 19,617
 | 7,659

Latency (Mean / P99 in ms):

 | Metric
 | 2× B200
 | 4× H100
 | 4× A100

 | TTFT
 | 4,601 / 65,289
 | 933 / 4,268
 | 6,997 / 96,435

 | TPOT
 | 14 / 14
 | 14 / 15
 | 31 / 33

 | ITL
 | 14 / 109
 | 14 / 117
 | 31 / 141

## Next steps

### Upstream

- Download Qwen3-Coder-Next on Hugging Face

### Downstream

Verify tool-use with tau-bench

Confirm the model handles function-calling correctly before using it in production with openbench:

uv run --with openbench[tau_bench] bench eval tau_bench_retail \
 --model openai/qwen3-coder-next \
 -M base_url=http://localhost:8000/v1 \
 --limit 10

Use as a Claude Code backend

Use your self-hosted model instead of Anthropic's API for local development:

export ANTHROPIC_BASE_URL=http://localhost:8000
claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
