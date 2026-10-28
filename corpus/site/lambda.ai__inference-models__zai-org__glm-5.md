# zai-org/GLM-5

Source: https://lambda.ai/inference-models/zai-org/glm-5

Skip to main content

# How to deploy GLM-5 on Lambda

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

 | NVIDIA HGX B200
 | 700
 | 6,300
 | 1,662
 | 103
 | 256
 | 4,194,304
 | 524,288
 | 32

The benchmark uses an 8:1 input-to-output token ratio (8192 in/1024 out per request) to simulate coding workflows, where large code contexts are provided as input with shorter completions as output. This differs from chat assistant workloads, which typically have more balanced or output-heavy ratios.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model zai-org/GLM-5 \
 --served-model-name glm-5-fp8 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 256 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking GLM-5 for the full command.

## Background

GLM-5 is a 744 billion parameter Mixture-of-Experts (MoE) language model developed by Z.AI, with only 40 billion parameters active per token. Building on the success of GLM-4.7 and trained on 28.5 trillion tokens, GLM-5 incorporates DeepSeek Sparse Attention (DSA) for efficient long-context processing

The model was scaled from 355B parameters (32B active) to 744B (40B active) using advanced post-training with SLIME (asynchronous RL infrastructure). It achieves best-in-class performance on reasoning benchmarks (HLE: 30.5), strong coding performance (SWE-bench Verified: 77.8%), and advanced agentic capabilities (BrowseComp: 62.0-75.9%).

GLM-5 extends context to 128K-202K tokens depending on the task, making it well-suited for complex systems engineering, long-horizon agentic tasks, and reasoning applications.

## Model specifications

### Overview

- Name: GLM-5

- Author: Z.AI (zai-org)

- Architecture: MoE with DeepSeek Sparse Attention (DSA)

- License: MIT

### Specifications

- Total parameters: 744B (40B active per token)

- Context window: 200K tokens

## Hardware Requirements

- NVIDIA HGX B200 (8x NVIDIA B200 GPU system) is required to load the full 744B parameter model. For efficient deployment, use FP8 quantized version (zai-org/GLM-5-FP8).

## Deployment and benchmarking

### Deploying GLM-5

GLM-5 requires, at minimum, 8x NVIDIA B200 GPUs to load the full 744B parameter model.

- 

Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image (denoted as "8x B200 (180 GB SXM6)".

- 

Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- 

Start the SGLang server:

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:glm5-blackwell \
 python -m sglang.launch_server \
 --model-path zai-org/GLM-5-FP8 \
 --host 0.0.0.0 \
 --port 8000 \
 --tp-size 8 \
 --tool-call-parser glm47 \
 --reasoning-parser glm45 \
 --speculative-algorithm EAGLE \
 --speculative-num-steps 3 \
 --speculative-eagle-topk 1 \
 --speculative-num-draft-tokens 4 \
 --mem-fraction-static 0.85 \
 --served-model-name glm-5-fp8

This launches a SGLang server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see GLM-5 listed in the response.

### Benchmarking GLM-5

You can benchmark GLM-5 using vllm bench serve. In this article, the benchmark results use a 8192 input/1024 output token workload to simulate coding assistant patterns.

Here's a minimal example to run against your server:

vllm bench serve \
 --backend openai-chat \
 --model zai-org/GLM-5 \
 --served-model-name glm-5-fp8 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 256 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

Token throughput (NVIDIA HGX B200):

 | Metric
 | Tokens per second

 | Output generation
 | 700

 | Total (input & output)
 | 6,300

Latency details (NVIDIA HGX B200):

 | Metric
 | Mean (ms)
 | P99 (ms)

 | Time to first token
 | 1,662
 | 21,350

 | Time per output token
 | 43
 | 58

 | Inter-token latency
 | 103
 | 730

## Next steps

To get started with GLM-5, follow the directions above. Read more about the model on Hugging Face:

Download the GLM-5 weights on Hugging Face.

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
