# allenai/Olmo-Hybrid-Instruct-DPO-7B

Source: https://lambda.ai/inference-models/allenai/olmo-hybrid-instruct-dpo-7b

Skip to main content

# How to deploy OLMo Hybrid 7B on Lambda

## TL;DR: token throughput on vLLM

 | Hardware
 | Gen. throughput
 | TTFT
 | ITL

 | 1× NVIDIA B200 GPU
 | 1,765 tok/s
 | 4,424ms
 | 14ms

 | 1× NVIDIA H100 GPU
 | 1,066 tok/s
 | 4,665ms
 | 25ms

 | 1× NVIDIA A100 GPU
 | 551 tok/s
 | 7,191ms
 | 51ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --model allenai/Olmo-Hybrid-Instruct-DPO-7B \
 --served-model-name olmo-hybrid-7b \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 1024 \
 --num-prompts 512 --max-concurrency 32

(8192 in/1024 out tokens, 32 parallel requests)

## Background

OLMo Hybrid 7B is a open-weight language model from the Allen Institute for AI (Ai2) that replaces 75% of traditional attention layers with **Gated DeltaNet—**a modern linear recurrent neural network. This hybrid architecture uses a repeating 3:1 pattern: three consecutive Gated DeltaNet layers followed by one full-attention layer, achieving roughly 2x data efficiency over its predecessor OLMo 3 7B. The model matches the same MMLU accuracy with 49% fewer training tokens and delivers better long-context performance (85.0 vs. 70.9 on RULER at 64K tokens) and up to 75% improved inference throughput on long sequences.

Ai2 trained OLMo Hybrid 7B on 5.5T tokens across 512 GPUs. Pre-training began on NVIDIA H100 GPUs and migrated midway to Lambda's NVIDIA HGX B200 infrastructure, making it one of the first fully open models trained on Blackwell-generation hardware. The B200 phase processed approximately 3 trillion tokens in just 6.19 days, achieving 97% active training time with a median recovery time under 4 minutes. This migration demonstrated the production readiness of Lambda's NVIDIA B200 infrastructure for large-scale training.

The model is fully open under Apache 2.0 including all code, checkpoints, intermediate checkpoints, and training data—continuing Ai2's commitment to open science.

## Model specifications

### Overview

- Name: OLMo Hybrid 7B

- Author: Allen Institute for AI (Ai2)

- Architecture: Hybrid RNN-Transformer (Gated DeltaNet + Full Attention, 3:1 ratio)

- License: Apache-2.0

### Specifications

- Total parameters: 7B

- Context window: 65,536 tokens

- Languages: English

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA B200 GPU

- 1× NVIDIA H100 GPU

- 1× NVIDIA A100 GPU

## Deployment and benchmarking

### Deploying OLMo Hybrid 7B

OLMo Hybrid 7B fits on a single GPU.

- Launch an instance with 1× NVIDIA B200 GPU, 1× NVIDIA H100 GPU, or 1× NVIDIA A100 GPU from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

#### vLLM

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:latest \
 --host 0.0.0.0 \
 --port 8000 \
 --model allenai/Olmo-Hybrid-Instruct-DPO-7B \
 --served-model-name olmo-hybrid-7b \
 --trust-remote-code

This launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see olmo-hybrid-7b listed in the response.

### Benchmarking results: OLMo Hybrid 7B

Token throughput:

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | Output gen (tok/s)
 | 1,765
 | 1,066
 | 551

Latency (Mean in ms):

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | TTFT
 | 4,424
 | 4,665
 | 7,191

 | ITL
 | 14
 | 25
 | 51

## Next steps

### Upstream

- Download OLMo Hybrid 7B on Hugging Face

- OLMo Hybrid paper

- Lambda training blog: Open Model, Open Metrics

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
