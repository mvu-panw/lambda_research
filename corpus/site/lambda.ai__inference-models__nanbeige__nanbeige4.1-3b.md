# Nanbeige/Nanbeige4.1-3B

Source: https://lambda.ai/inference-models/nanbeige/nanbeige4.1-3b

Skip to main content

# How to deploy Nanbeige4.1-3B on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 1× NVIDIA B200 GPU
 | 4,547 tok/s
 | 766ms
 | 6ms

 | 1× NVIDIA H100 GPU
 | 2,381 tok/s
 | 1,619ms
 | 12ms

 | 1× NVIDIA A100 GPU
 | 1,174 tok/s
 | 3,830ms
 | 29ms

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 1× NVIDIA B200 GPU
 | 4,806 tok/s
 | 526ms
 | 6ms

 | 1× NVIDIA H100 GPU
 | 2,472 tok/s
 | 822ms
 | 12ms

 | 1× NVIDIA A100 GPU
 | 1,050 tok/s
 | 1,480ms
 | 29ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --model Nanbeige/Nanbeige4.1-3B \
 --served-model-name nanbeige4.1-3b \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 1024 \
 --num-prompts 512 --max-concurrency 32

(8192 in / 1024 out tokens, 32 parallel requests)

## Background

Nanbeige4.1-3B is a 3-billion-parameter code model designed for deep-search agentic workflows, where models must reason through 500+ tool-calling rounds to solve complex problems. Despite its small size, it achieves 76.9 on LiveCodeBench-V6 and 30.5 on SWE-Bench Verified, competitive with models 10x larger, while being efficient enough to run on a single GPU.

The model's strong performance relative to its size comes from targeted training innovations:

- Complexity-aware code rewards: Reinforcement learning rewards scale with problem difficulty, preventing the model from gaming easy tasks.

- Deep-search curriculum: Training on multi-step reasoning chains with hundreds of tool calls, not just single-turn completions.

- Extended context: 262k token context window enables processing entire repositories without chunking.

Nanbeige4.1-3B is positioned as the first small model optimized for deep-search scenarios, making it ideal for edge deployment or cost-sensitive production workloads requiring agentic capabilities. Test it thoroughly on your own benchmarks, as this is one particular model that gets branded a "benchmax" (trained to optimize specific benchmarks).

## Model specifications

### Overview

- Name: Nanbeige4.1-3B

- Author: Nanbeige LLM Lab

- Architecture: Dense Transformer

- License: Apache-2.0

### Specifications

- Total parameters: 3B

- Context window: 262k tokens

- Languages: English, Chinese

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA B200 GPU

- 1× NVIDIA H100 GPU

## Deployment and benchmarking

### Deploying Nanbeige4.1-3B

Nanbeige4.1-3B can run on a single NVIDIA B200 GPU or a single NVIDIA H100 GPU.

- Launch an instance with 1× NVIDIA B200 GPU or 1× NVIDIA H100 GPU from the Lambda Cloud Console using the GPU Base 24.04 image.

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
 --model-path Nanbeige/Nanbeige4.1-3B \
 --served-model-name nanbeige4.1-3b \
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
 --model Nanbeige/Nanbeige4.1-3B \
 --served-model-name nanbeige4.1-3b \
 --trust-remote-code

This launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see nanbeige4.1-3b listed in the response.

### Benchmarking results: Nanbeige4.1-3B

 SGLang
 vLLM

Token throughput:

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | Output gen (tok/s)
 | 4,547
 | 2,381
 | 1,174

 | Total (tok/s)
 | 40,926
 | 21,430
 | 10,571

Latency (Mean / P99 in ms):

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | TTFT
 | 766 / 2,214
 | 1,619 / 3,555
 | 3,830 / 9,784

 | TPOT
 | 6 / 7
 | 12 / 13
 | 23 / 27

 | ITL
 | 6 / 19
 | 12 / 23
 | 24 / 52

Token throughput:

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | Output gen (tok/s)
 | 4,806
 | 2,472
 | 1,049

 | Total (tok/s)
 | 43,256
 | 22,249
 | 9,444

Latency (Mean / P99 in ms):

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | TTFT
 | 526 / 1,928
 | 822 / 3,463
 | 1,480 / 10,546

 | TPOT
 | 6 / 7
 | 12 / 13
 | 29 / 30

 | ITL
 | 6 / 58
 | 12 / 113
 | 29 / 130

## Next steps

- Download Nanbeige4.1-3B on Hugging Face

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
