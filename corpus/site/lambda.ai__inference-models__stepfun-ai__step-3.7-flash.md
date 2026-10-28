# stepfun-ai/Step-3.7-Flash

Source: https://lambda.ai/inference-models/stepfun-ai/step-3.7-flash

Skip to main content

# How to deploy Step 3.7 Flash on Lambda

## TL;DR: token throughput

vLLM with MTP speculative decoding, workload 8192 in / 2048 out tokens at 32 concurrent requests.

 | Hardware
 | Output gen
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | 4× NVIDIA B200 GPUs
 | 1,597 tok/s
 | ~53 tok/s
 | 7,982 tok/s
 | 2,183 ms
 | 52.7 ms

 | 8× NVIDIA H100 GPUs
 | 1,245 tok/s
 | ~42 tok/s
 | 6,224 tok/s
 | 2,995 ms
 | 67.2 ms

 | 8× NVIDIA A100 GPUs
 | 474 tok/s
 | ~17 tok/s
 | 2,370 tok/s
 | 13,646 ms
 | 167.5 ms

### Benchmark command

(8192 in / 2048 out tokens, 32 parallel requests, 512 prompts.)

vllm bench serve \
 --backend openai-chat \
 --model stepfun-ai/Step-3.7-Flash \
 --served-model-name step3p7-flash \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking Step 3.7 Flash for the full results.

## Background

Step 3.7 Flash is StepFun AI's 198-billion-parameter vision-language model, released open-weight under Apache 2.0. The sparse Mixture-of-Experts design activates only about 11 billion parameters per token, reads both text and images, handles a 256K-token context, and lets you set reasoning effort to low, medium, or high.

The language model carries over from Step 3.5 Flash almost unchanged, including the Multi-Token Prediction heads that vLLM uses for speculative decoding and that account for much of the throughput below. The real change in 3.7 is vision. StepFun added a 1.8-billion-parameter Perception Encoder that takes images directly and trained the model to work with them interactively, so it can crop or zoom into a region and mark it up from a short Python snippet before answering.

On StepFun's own benchmarks, the model is strongest at agentic and tool-use work and at image-grounded questions, scoring 67.1 on ClawEval 1.1 and 79.2 on SimpleVQA-Search (both first in their tests), 95.3 on V*, and 56.3 on SWE-Bench Pro. These are the vendor's numbers, so treat them as a starting point until third parties reproduce them.

## Model specifications

### Overview

- Name: Step 3.7 Flash

- Author: StepFun AI

- Architecture: Sparse MoE vision-language model (step3p7; language backbone step3p5)

- License: Apache 2.0

### Specifications

- Total parameters: 198B, 196B language backbone + 1.8B Perception Encoder vision tower (~11B active per token)

- Experts: 288 routed + 1 shared, top-8, sigmoid router

- Layers / hidden size: 45 / 4096

- Attention: S3F1 hybrid — 3× sliding-window (W=512) + 1× full GQA-8

- Context window: 256K

- Modality: image-text-to-text (vision-language)

- Reasoning modes: low / medium / high

## Hardware requirements

- Minimal deployment:

- 4× NVIDIA B200 GPUs (--tp-size 4)

- 8× NVIDIA H100 GPUs (--tp-size 8)

- 8× NVIDIA A100 GPUs (--tp-size 8)

## Deployment and benchmarking

### Deploying Step 3.7 Flash

Serve Step 3.7 Flash with vLLM, matching the tensor-parallel size to the number of GPUs (4 for B200, 8 for H100 or A100).

- Launch a 4× NVIDIA B200 GPUs, 8× NVIDIA H100 GPUs, or 8× NVIDIA A100 GPUs instance from the Lambda Cloud Console on the GPU Base 24.04 image.

- Connect over SSH or the JupyterLab terminal (see Connecting to an instance).

- Start the server:

#### vLLM

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -e HF_HOME=/root/.cache/huggingface \
 -e VLLM_USE_DEEP_GEMM=0 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:stepfun37 \
 --model stepfun-ai/Step-3.7-Flash \
 --served-model-name step3p7-flash \
 --tensor-parallel-size 4 \
 --host 0.0.0.0 --port 8000 \
 --max-model-len auto \
 --trust-remote-code \
 --gpu-memory-utilization 0.9 \
 --enable-expert-parallel \
 --disable-cascade-attn \
 --reasoning-parser step3p5 \
 --enable-auto-tool-choice \
 --tool-call-parser step3p5 \
 --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}'

A few flags are specific to this model:

- --speculative-config '{"method": "mtp", "num_speculative_tokens": 3}' turns on its built-in Multi-Token Prediction heads for speculative decoding, which is most of where the throughput above comes from.

- --reasoning-parser step3p5 and --tool-call-parser step3p5 (with --enable-auto-tool-choice) handle the model's reasoning output and OpenAI-style tool calls.

- --disable-cascade-attn is required for the S3F1 hybrid attention, and --enable-expert-parallel spreads the 288 experts across the GPUs.

#### Verify the server

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see step3p7-flash listed in the response.

### Benchmarking Step 3.7 Flash

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests, vLLM with MTP speculative decoding.

H100 and A100 figures were captured from a live vLLM server running in eager mode (CUDA graphs disabled). Throughput with CUDA graphs enabled is expected to be higher.

Token throughput:

 | Metric
 | 4× NVIDIA B200 GPUs
 | 8× NVIDIA H100 GPUs
 | 8× NVIDIA A100 GPUs

 | Output generation (tok/s)
 | 1,597
 | 1,245
 | 474

 | Total, input & output (tok/s)
 | 7,982
 | 6,224
 | 2,370

 | Per-user generation (tok/s)
 | ~53
 | ~42
 | ~17

Latency (Mean / P99 in ms):

 | Metric
 | 4× NVIDIA B200 GPUs
 | 8× NVIDIA H100 GPUs
 | 8× NVIDIA A100 GPUs

 | Time to first token
 | 2,183 / 25,629
 | 2,995 / 35,018
 | 13,646 / 99,982

 | Time per output token
 | 18.8 / 26.6
 | 24.0 / 33.9
 | 60.1 / 84.2

 | Inter-token latency
 | 52.7 / 182.3
 | 67.2 / 250.3
 | 167.5 / 215.7

## Next steps

### Upstream

- Download Step 3.7 Flash on Hugging Face

- Step 3.7 Flash announcement blog

- Step 3.5 Flash technical report (shared backbone, arXiv:2602.10604)

### Downstream

Use as a Claude Code backend

Use your self-hosted Step 3.7 Flash instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node running the vLLM server:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="step3p7-flash"
export ANTHROPIC_DEFAULT_SONNET_MODEL="step3p7-flash"
export ANTHROPIC_DEFAULT_OPUS_MODEL="step3p7-flash"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="step3p7-flash"

export DISABLE_TELEMETRY=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
