# arcee-ai/Trinity-Large-Preview

Source: https://lambda.ai/inference-models/arcee-ai/trinity-large-preview

Skip to main content

# How to deploy Trinity Large Preview on Lambda

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
 | 1,735
 | 15,611
 | 1,850
 | 17
 | 256
 | 2,097,152
 | 262,144
 | 32

The benchmark uses an 8:1 input-to-output token ratio (8192 in / 1024 out per request) to simulate coding workflows, where large code contexts are provided as input with shorter completions as output. This differs from chat assistant workloads, which typically have more balanced or output-heavy ratios.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model arcee-ai/Trinity-Large-Preview \
 --served-model-name trinity \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 256 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking Arcee for the full command

## Background

Trinity Large Preview is a 398 billion parameter sparse Mixture-of-Experts (MoE) language model developed by Arcee AI, with only 13 billion parameters active per token—an extreme 1.56% activation ratio. This efficiency enables 2-3x faster inference throughput compared to similarly-sized models while maintaining competitive performance with models like GLM-4.5 Base.

The model was trained on 17 trillion tokens across 256 NVIDIA HGX B200 systems in partnership with Prime Intellect (infrastructure) and DatologyAI (data curation). It introduces several innovations including gated attention (NeurIPS 2025 Best Paper), interleaved local/global attention for efficient long-context processing, and novel load balancing techniques (SMEBU) that enabled zero loss spikes during training.

Trinity extends context to 512K tokens with length extrapolation observed up to 1M tokens, making it well-suited for long-context applications like code analysis and document processing.

## Model specifications

### Overview

- Name: Trinity Large Preview

- Author: Arcee AI

- Architecture: AfmoeForCausalLM (Sparse MoE Transformer)

- License: Apache-2.0

### Specifications

- Total parameters: 398B (13B active per token)

- Context window: 512K tokens (extrapolation tested to 1M)

- Languages: English, Spanish, French, German, Italian, Portuguese, Russian, Arabic, Hindi, Korean, Chinese, Japanese, Indonesian, Vietnamese, Bengali

## Hardware requirements

- Minimal Deployment:

- NVIDIA HGX B200: Required to load the full 398B parameter model (~800 GB in BF16). Note: BF16 precision requires validation - confirm VRAM calculation is accurate for this model size.

## Deployment and benchmarking

### Deploying Trinity Large Preview

Trinity Large Preview requires an NVIDIA HGX B200 to load the full 398B parameter model.

- 

Launch an instance with an NVIDIA HGX B200 from the Lambda Cloud Console using the GPU Base 24.04 image.

- 

Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- 

Create a Dockerfile with the following contents:

FROM lmsysorg/sglang:dev

# Upgrade transformers (needed for Arcee support)
RUN pip install --upgrade transformers

- Build the Docker image:

docker build -t sglang-custom .

- Start the SGLang server:

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 sglang-custom \
 python -m sglang.launch_server \
 --model-path arcee-ai/Trinity-Large-Preview \
 --tp-size 8 \
 --host 0.0.0.0 \
 --port 8000 \
 --served-model-name trinity \
 --trust-remote-code

This launches an SGLang server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see Trinity listed in the response.

### Benchmarking Trinity

You can benchmark Trinity using vllm bench serve. The benchmark results in this article use an 8192 input / 1024 output token workload to simulate coding assistant patterns. Here's a minimal example to run against your server:

vllm bench serve \
 --backend openai-chat \
 --model arcee-ai/Trinity-Large-Preview \
 --served-model-name trinity \
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
 | 1,735

 | Total (input & output)
 | 15,611

Latency details (NVIDIA HGX B200):

 | Metric
 | Mean (ms)
 | P99 (ms)

 | Time to first token
 | 1,850
 | 4,007

 | Time per output token
 | 17
 | 18

 | Inter-token latency
 | 17
 | 30

## Next steps

To get started with Arcee, follow the directions above to deploy on Lambda's infrastructure accelerated by NVIDIA. Below are some available resources to check out more information about the model:

Download the Trinity Large Preview weights on Hugging Face.

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
