# MiniMaxAI/MiniMax-M2.5

Source: https://lambda.ai/inference-models/minimaxai/minimax-m2.5

Skip to main content

# How to deploy MiniMax M2.5 on Lambda

## TL;DR: token throughput (SGLang)

 | Hardware configuration
 | Generation throughput (tok/s)
 | Total throughput (tok/s)
 | TTFT (ms)
 | ITL (ms)
 | Prompts
 | Tokens in
 | Tokens out
 | Parallel requests

 | 2× NVIDIA B200 GPU
 | 896
 | 8,062
 | 3,091
 | 36
 | 512
 | 4,194,304
 | 524,288
 | 32

 | 4× NVIDIA H100 GPU
 | 849
 | 7,644
 | 13,131
 | 27
 | 512
 | 4,194,304
 | 524,288
 | 32

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model MiniMaxAI/MiniMax-M2.5 \
 --served-model-name minimax-m25 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking MiniMax-M2.5 for the full command.

## Background

MiniMax-M2.5 is a 229B parameter Mixture-of-Experts (MoE) language model with only 10B parameters active per token. Positioned as "the world's first production-level model designed natively for agent scenarios," M2.5 uses 256 experts with 8 activated per token, enabling efficient inference while maintaining frontier-level capabilities.

MiniMax trained using MiniMax's novel Forge framework, an agent-native RL (reinforcement learning) training system that achieves 40x training speedup through prefix-tree merging and windowed FIFO scheduling. M2.5 introduces task completion time optimization, a reward shaping approach that balances intelligence with speed, resulting in 37% faster task completion than its predecessor M2.1.

On benchmarks, M2.5 achieves 80.2% on SWE-Bench Verified (up from M2.1's 74.0%), matching Claude Opus 4.6's speed while costing 10-20x less. The model also demonstrates strong cross-scaffold generalization, performing consistently across different agent frameworks, including Claude Code (80.2%), Droid (79.7%), and OpenCode (76.1%).

## Model specifications

### Overview

- Name: MiniMax-M2.5

- Author: MiniMaxAI

- Architecture: MoE

- License: MiniMax-Open (Modified MIT)

### Specifications

- Total parameters: 229B (10B active per token)

- Context window: 192k tokens

- Languages: English, Spanish, French, German, Italian, Portuguese, Russian, Arabic, Hindi, Korean, Chinese, Japanese, Indonesian, Vietnamese, and Bengali

## Hardware Requirements

- Minimal deployment:

- 2× NVIDIA B200 (--tp-size 2)

- 4× NVIDIA H100 (--tp-size 4)

## Deployment and benchmarking

### Deploying MiniMax-M2.5

MiniMax-M2.5 requires 2× NVIDIA B200 or 4× NVIDIA H100 GPUs to load the model.

- Launch an instance with 2× NVIDIA B200 or 4× NVIDIA H100 from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the SGLang server:

# Use --tp-size 2 for 2× B200, --tp-size 4 for 4× H100
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
 --model-path MiniMaxAI/MiniMax-M2.5 \
 --served-model-name minimax-m25 \
 --tp-size 2 \ # Or 4 for H100
 --tool-call-parser minimax-m2 \
 --reasoning-parser minimax-append-think \
 --trust-remote-code \
 --mem-fraction-static 0.85

This launches an SGLang server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see MiniMax-M2.5 listed in the response.

### Benchmarking MiniMax-M2.5

You can benchmark MiniMax-M2.5 using vllm bench serve. The benchmark results in this article use an 8192 input/1024 output token workload.

Here's a minimal example to run against your server:

vllm bench serve \
 --backend openai-chat \
 --model MiniMaxAI/MiniMax-M2.5 \
 --served-model-name minimax-m25 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

Token throughput (2× NVIDIA B200 GPUs):

 | Metric
 | Tokens per second

 | Output generation
 | 896

 | Total (input & output)
 | 8,062

Latency details (2× NVIDIA B200 GPUs):

 | Metric
 | Mean (ms)
 | P99 (ms)

 | Time to first token
 | 3,091
 | 7,552

 | Time per output token
 | 33
 | 35

 | Inter-token latency
 | 36
 | 58

## Next steps

To get started with MiniMax-M2.5, follow the directions above to deploy on Lambda's infrastructure accelerated by NVIDIA. View additional resources about the model below:

- Download the MiniMax-M2.5 weights on Hugging Face.

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
