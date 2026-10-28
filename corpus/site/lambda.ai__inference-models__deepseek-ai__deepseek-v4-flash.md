# deepseek-ai/DeepSeek-V4-Flash

Source: https://lambda.ai/inference-models/deepseek-ai/deepseek-v4-flash

Skip to main content

# How to deploy DeepSeek-V4-Flash on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200 (native FP4+FP8 build)
 | 1,222 tok/s
 | 38 tok/s
 | 11,000 tok/s
 | 1,701 ms
 | 66 ms

 | NVIDIA HGX H100 (FP8-quantized build)
 | 1,262 tok/s
 | 39 tok/s
 | 11,361 tok/s
 | 2,463 ms
 | 60 ms

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200 (native FP4+FP8 build)
 | 1,469 tok/s
 | 46 tok/s
 | 13,217 tok/s
 | 1,452 ms
 | 20 ms

### Benchmark command

(8192 in / 1024 out tokens, 32 parallel requests, 512 prompts. SGLang runs use EAGLE speculative decoding.)

The benchmark uses an 8:1 input-to-output token ratio (8192 in / 1024 out per request) to simulate long-context coding and document-analysis workflows.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model deepseek-ai/DeepSeek-V4-Flash \
 --served-model-name deepseek \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 1024 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking DeepSeek-V4-Flash for the full results.

## Background

DeepSeek-V4-Flash is a 284 billion parameter sparse Mixture-of-Experts (MoE) language model from DeepSeek-AI, with only 13 billion parameters active per forward pass. It is the smaller sibling of DeepSeek-V4-Pro (1.6T / 49B active) and ships with the same native 1 million token context window and the same three reasoning effort modes (Non-think, Think High, Think Max).

DeepSeek-V4-Flash inherits the V4 architecture stack:

- Hybrid attention. Compressed Sparse Attention (CSA) plus Heavily Compressed Attention (HCA), dramatically reducing single-token inference FLOPs and KV-cache memory at long context.

- Manifold-Constrained Hyper-Connections (mHC). Refined residual connections for stable signal propagation in deep MoE stacks.

- Muon optimizer. Used during pre-training on 32T tokens for faster convergence and stability.

- FP4 + FP8 mixed precision. MoE expert parameters are FP4 while non-expert parameters are FP8, roughly halving the on-disk and in-VRAM footprint compared to a pure FP8 release.

In Think Max mode, DeepSeek-V4-Flash reaches reasoning quality comparable to DeepSeek-V4-Pro on benchmarks like LiveCodeBench (91.6 Pass@1), HMMT 2026 Feb (94.8 Pass@1), and MMLU-Pro (86.2 EM), at a fraction of the deployment footprint. The Pro model retains an edge on raw knowledge tasks (Simple-QA, Chinese-SimpleQA) and the most complex agentic workflows.

## Model specifications

### Overview

- Name: DeepSeek-V4-Flash

- Author: DeepSeek-AI

- Architecture: MoE with hybrid CSA + HCA attention

- License: MIT

### Specifications

- Total parameters: 284B (13B active per forward pass)

- Context window: 1M tokens (native)

- Precision: FP4 (MoE experts) + FP8 (other parameters), mixed

- Reasoning modes: Non-think, Think High, Think Max

## Hardware requirements

DeepSeek-V4-Flash ships in two builds:

- Native FP4+FP8 mixed (deepseek-ai/DeepSeek-V4-Flash, ~146 GB on disk) requires NVIDIA B200 GPUs for FP4 expert weights.

- FP8-only quantized (sgl-project/DeepSeek-V4-Flash-FP8, ~284 GB on disk), quantized release for NVIDIA H100 GPUs.

## Deployment and benchmarking

### Deploying DeepSeek-V4-Flash

DeepSeek-V4-Flash can be served with vLLM or SGLang on Blackwell, or with SGLang on Hopper using the FP8-quantized build.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image — NVIDIA HGX B200 (8× NVIDIA B200 GPUs) for the native build, or NVIDIA HGX H100 (8× NVIDIA H100 GPUs) for the FP8 build.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using one of the backends below.

 SGLang
 vLLM

NVIDIA HGX B200 (native FP4+FP8 build):
docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:deepseek-v4-blackwell \
 python3 -m sglang.launch_server \
 --model-path deepseek-ai/DeepSeek-V4-Flash \
 --served-model-name deepseek \
 --tp 4 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --mem-fraction-static 0.9 \
 --moe-runner-backend flashinfer_mxfp4 \
 --speculative-algo EAGLE \
 --speculative-num-steps 3 \
 --speculative-eagle-topk 1 \
 --speculative-num-draft-tokens 4 \
 --chunked-prefill-size 4096 \
 --disable-flashinfer-autotune

--moe-runner-backend flashinfer_mxfp4 enables the FlashInfer FP4 expert kernel (Blackwell-only). EAGLE speculative decoding is enabled for additional throughput.
NVIDIA HGX H100 (FP8-quantized build):

Important: Hopper has no FP4 hardware, so on H100 you must run the FP8-quantized release (sgl-project/DeepSeek-V4-Flash-FP8). Set SGLANG_DSV4_FP4_EXPERTS=0 so SGLang doesn't attempt the FP4 kernel.

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -e SGLANG_DSV4_FP4_EXPERTS=0 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:deepseek-v4-hopper \
 python3 -m sglang.launch_server \
 --model-path sgl-project/DeepSeek-V4-Flash-FP8 \
 --served-model-name deepseek \
 --tp 8 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --mem-fraction-static 0.85 \
 --speculative-algo EAGLE \
 --speculative-num-steps 3 \
 --speculative-eagle-topk 1 \
 --speculative-num-draft-tokens 4 \
 --chunked-prefill-size 4096 \
 --disable-flashinfer-autotune

The FP8 build is roughly 2× the size of the native FP4+FP8 build, which is why TP=8 across all 8 NVIDIA H100 GPUs in the HGX system is the minimum on Hopper.

NVIDIA HGX B200 (native FP4+FP8 build):
docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:deepseekv4-cu130 \
 --model deepseek-ai/DeepSeek-V4-Flash \
 --served-model-name deepseek \
 --tensor-parallel-size 4 \
 --enable-expert-parallel \
 --kv-cache-dtype fp8 \
 --block-size 256 \
 --max-model-len auto \
 --trust-remote-code \
 --gpu-memory-utilization 0.9 \
 --tokenizer-mode deepseek_v4 \
 --no-disable-hybrid-kv-cache-manager \
 --tool-call-parser deepseek_v4 \
 --enable-auto-tool-choice \
 --reasoning-parser deepseek_v4

Notable flags:

- --tensor-parallel-size 4 with --enable-expert-parallel shards attention/shared params 4-way and routes the 256 MoE experts across all 8 NVIDIA B200 GPUs.

- --no-disable-hybrid-kv-cache-manager keeps vLLM's hybrid KV-cache manager on, required for V4's CSA + HCA hybrid attention.

- --kv-cache-dtype fp8 keeps KV-cache memory low enough to take advantage of the 1M-token context window.

- --tokenizer-mode deepseek_v4, --tool-call-parser deepseek_v4, and --reasoning-parser deepseek_v4 enable the V4 tokenizer, OpenAI-compatible tool calls, and the model's reasoning-mode output format.

#### Verify the server

Either command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see deepseek listed in the response.

### Benchmarking DeepSeek-V4-Flash

Workload: 8192 input / 1024 output tokens, 512 prompts, 32 concurrent requests.

 SGLang
 vLLM

NVIDIA HGX B200 (native FP4+FP8 build, EAGLE speculative decoding)
Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,222

 | Total (input & output)
 | 11,000

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 1,701
 | 20,886

 | Time per output token
 | 24.2
 | 51.6

 | Inter-token latency
 | 65.5
 | 559.0

NVIDIA HGX H100 (FP8-quantized build, EAGLE speculative decoding)
Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,262

 | Total (input & output)
 | 11,361

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 2,463
 | 32,221

 | Time per output token
 | 22.7
 | 54.9

 | Inter-token latency
 | 60.3
 | 624.4

NVIDIA HGX B200 (native FP4+FP8 build)
Token throughput:

 | Metric
 | Tokens per second

 | Output generation
 | 1,469

 | Total (input & output)
 | 13,217

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 1,452
 | 10,085

 | Time per output token
 | 20.4
 | 28.5

 | Inter-token latency
 | 20.3
 | 175.9

## Next steps

### Upstream

- Download DeepSeek-V4-Flash on Hugging Face

- DeepSeek-V4 Technical Report (PDF)

### Downstream

Use as a Claude Code backend

Use your self-hosted DeepSeek-V4-Flash instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the vLLM server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="deepseek"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek"

export ANTHROPIC_SMALL_FAST_MODEL="deepseek"
export ANTHROPIC_FAST_MODEL="deepseek"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
