# zai-org/GLM-4.7-Flash

Source: https://lambda.ai/inference-models/zai-org/glm-4.7-flash

Skip to main content

# How to deploy GLM-4.7-Flash on Lambda

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

 | 1× NVIDIA Blackwell B200 GPU
 | 902.74
 | 8,124.65
 | 6,170.78
 | 30.61
 | 256
 | 2,097,152
 | 262,144
 | 32

 | 1× NVIDIA H100 GPU
 | 660.67
 | 5,946.05
 | 20,087.41
 | 27.24
 | 256
 | 2,097,152
 | 262,144
 | 32

The benchmark uses an 8:1 input-to-output token ratio (8192 in / 1024 out per request) to simulate coding workflows, where large code contexts are provided as input with shorter completions as output. This differs from chat assistant workloads, which typically have more balanced or output-heavy ratios.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model zai-org/GLM-4.7-Flash \
 --served-model-name glm-4.7-flash \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 256 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking GLM-4.7-Flash for the full command

## Background

GLM-4.7-Flash is a new Mixture-of-Experts (MoE) model just released by Z.AI. It represents a significant departure from its beloved predecessor (GLM-4.5-Air), introducing a "Lite" architecture that combines Multi-head Latent Attention (MLA) with a streamlined MoE design.

The model achieves competitive performance with Qwen3-30B-A3B while using half the active experts, enabled through:

- MLA-style KV cache compression, which reduces memory needs by up to 93%

- Auxiliary-loss-free expert routing

- Multi-token prediction for speculative decoding

- Three-tiered thinking modes (interleaved, preserved, and turn-level) optimized for agentic applications

The main development with Flash (alongside being less than 10% of the parameters of the full GLM 4.7 model) is preserved and turn-level thinking, as mentioned earlier. Preserved thinking retains reasoning blocks across conversation turns, allowing the model to reuse the established logic instead of re-deriving it, making inference on the same tools faster. Along with this is Turn-level thinking, which is per-request control over the reasoning computation within a session. This enables cost/latency trade-offs for different task complexities, such as removing reasoning during a regular chat session and immediately re-enabling it for a complex tool call.

On benchmarks, GLM-4.7-Flash scores 91.6% on AIME 25, 59.2% on SWE-bench Verified, and 79.5% on τ²-Bench—positioning it as a strong contender in the lightweight deployment and code-use category.

## Model specifications

### Overview

- Name: GLM-4.7-Flash

- Author: Z.AI (zai-org)

- Architecture: MoE

- License: MIT

### Specifications

- Context window: 200,000 tokens

- Weights-on-disk: 62.5GB

- VRAM at full context window: 265GB

## Hardware Requirements

- Minimal Deployment:

- 1x NVIDIA H100 GPU or NVIDIA B200 GPU: Use --max-model-len=auto to have the context length be set to the size of your VRAM

- At full 200k context window: 2x NVIDIA B200 GPU or 4x NVIDIA H100 GPU

## Deployment and benchmarking

### Deploying to a single-GPU instance

You can run GLM-4.7-Flash on any Lambda instance with sufficient VRAM. For this guide, we'll use a 1x B200 instance.

- 

Launch a 1x B200 (180 GB) instance from the Lambda Cloud Console using the GPU Base 24.04 image.

- 

Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- 

Create a Dockerfile with the following contents:

FROM lmsysorg/sglang:dev

# Upgrade transformers (needed for GLM-4.7-Flash support)
RUN pip install --upgrade transformers

# Fix AutoImageProcessor.register() for new transformers API
RUN python3 -c "import glob; f=glob.glob('/sgl-workspace/**/sglang/srt/configs/utils.py',recursive=True)[0]; t=open(f).read(); open(f,'w').write(t.replace('AutoImageProcessor.register(config, None, image_processor, None, exist_ok=True)','AutoImageProcessor.register(config, slow_image_processor_class=image_processor, exist_ok=True)'))"

- Build the Docker image:

docker build -t sglang-custom .

- Start the GLM-4.7-Flash server:

docker run \
 --gpus 1 \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 sglang-custom \
 python -m sglang.launch_server \
 --model-path zai-org/GLM-4.7-Flash \
 --host 0.0.0.0 \
 --port 8000 \
 --served-model-name glm-4.7-flash \
 --trust-remote-code

This launches an SGLang server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see GLM-4.7-Flash listed in the response.

### Deploying to a multi-GPU instance

For larger context windows or higher throughput, deploy to a multi-GPU instance (e.g., 2x NVIDIA B200 GPU or 4x NVIDIA H100 GPU). Follow steps 1-4 from the single-GPU instructions, then start the server with tensor parallelism:

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 sglang-custom \
 python -m sglang.launch_server \
 --model-path zai-org/GLM-4.7-Flash \
 --tp-size 4 \
 --host 0.0.0.0 \
 --port 8000 \
 --served-model-name glm-4.7-flash \
 --trust-remote-code

Adjust --tp-size to match your GPU count (e.g., 2 for 2x B200, 4 for 4x H100).

### Benchmarking GLM-4.7-Flash

You can benchmark GLM-4.7-Flash using vllm bench serve. The benchmark results in this article use an 8192 input / 1024 output token workload to simulate coding assistant patterns. Here's a minimal example to run against your server:

vllm bench serve \
 --backend openai-chat \
 --model zai-org/GLM-4.7-Flash \
 --served-model-name glm-4.7-flash \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 256 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

Token throughput (1x NVIDIA B200 GPU):

 | Metric
 | Tokens per second

 | Output generation
 | 902.74

 | Total (input & output)
 | 8,124.65

Latency details (1x NVIDIA B200 GPU):

 | Metric
 | Mean (ms)
 | P99 (ms)

 | Time to first token
 | 6,170.78
 | 11,814.82

 | Time per output token
 | 29.44
 | 34.91

 | Inter-token latency
 | 30.61
 | 25.59

## Next steps

To get started with GLM-4.7-Flash, follow the directions above to deploy on Lambda GPUs. Below are some available resources to check out more information about the model:

Download the GLM-4.7-Flash weights on Hugging Face.

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
