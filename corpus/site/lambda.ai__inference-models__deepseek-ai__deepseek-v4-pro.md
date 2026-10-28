# deepseek-ai/DeepSeek-V4-Pro

Source: https://lambda.ai/inference-models/deepseek-ai/deepseek-v4-pro

Skip to main content

# How to deploy DeepSeek-V4-Pro on Lambda

## TL;DR: token throughput

### vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 911.92 tok/s
 | 28.50 tok/s
 | 4,561.38 tok/s
 | 1,186.15 ms
 | 55.79 ms

(8192 in / 2048 out tokens, 32 parallel requests, 512 prompts)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document-analysis workflows, in which large contexts are provided as input with substantial completions as output.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model deepseek-ai/DeepSeek-V4-Pro \
 --served-model-name deepseek \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking DeepSeek-V4-Pro for the full results.

## Background

DeepSeek-V4-Pro is a 1.6T-parameter sparse Mixture-of-Experts (MoE) language model from DeepSeek-AI. It supports a native 1M-token context window and ships with three reasoning effort modes (Non-think, Think High, Think Max).

Several architectural changes drive the model's efficiency at long context vs. DeepSeek-V3.2:

- Hybrid attention. A combination of Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA). At a 1M-token context, DeepSeek-V4-Pro uses only 27% of single-token inference FLOPs and 10% of the KV cache of DeepSeek-V3.2.

- Manifold-Constrained Hyper-Connections (mHC). A residual-connection refinement that improves signal propagation stability across the deep MoE stack.

- Muon optimizer. Used end-to-end during pre-training on 32T tokens for faster convergence and greater training stability.

- FP4 + FP8 mixed precision. DeepSeek-V4-Pro stores MoE expert parameters at FP4 while non-expert parameters use FP8, roughly halving the on-disk and in-VRAM footprint compared to a pure FP8 release.

In Think Max mode, DeepSeek-V4-Pro leads open-weight coding benchmarks (LiveCodeBench Pass@1: 93.5, Codeforces Rating: 3,206) and is competitive with frontier closed-source models such as Claude Opus 4.6, GPT-5.4, and Gemini 3.1-Pro on reasoning and agentic tasks.

## Model specifications

### Overview

- Name: DeepSeek-V4-Pro

- Author: DeepSeek-AI

- Architecture: MoE with hybrid CSA + HCA attention

- License: MIT

### Specifications

- Total parameters: 1.6T (49B active per forward pass)

- Context window: 1M tokens (native)

- Precision: FP4 (MoE experts) + FP8 (other parameters), mixed

- Reasoning modes: Non-think, Think High, Think Max

## Hardware requirements

- Minimal deployment:

- NVIDIA HGX B200 node

## Deployment and benchmarking

### Deploying DeepSeek-V4-Pro

DeepSeek-V4-Pro requires a NVIDIA HGX B200 node to load the full 1.6T-parameter model.

- Launch an instance with a NVIDIA HGX B200 from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the vLLM server:

docker run --gpus all -d \
 --privileged --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \
 vllm/vllm-openai:latest-cu129 deepseek-ai/DeepSeek-V4-Pro \
 --trust-remote-code \
 --kv-cache-dtype fp8 \
 --block-size 256 \
 --enable-expert-parallel \
 --data-parallel-size 8 \
 --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' \
 --attention_config.use_fp4_indexer_cache=True \
 --moe-backend deep_gemm_mega_moe \
 --tokenizer-mode deepseek_v4 \
 --tool-call-parser deepseek_v4 \
 --enable-auto-tool-choice \
 --reasoning-parser deepseek_v4 \
 --speculative_config '{"method":"mtp","num_speculative_tokens":2}'

This launches a vLLM server with an OpenAI-compatible API on port 8000. Notable flags:

- --data-parallel-size 8 with --enable-expert-parallel runs the model under data parallelism with expert parallelism, which is the recommended topology for V4-Pro on 8× NVIDIA B200 GPUs.

- --kv-cache-dtype fp8 and --attention_config.use_fp4_indexer_cache=True keep KV-cache memory low enough to use the 1M-token context window.

- --tokenizer-mode deepseek_v4, --tool-call-parser deepseek_v4, and --reasoning-parser deepseek_v4 enable the V4 tokenizer, OpenAI-compatible tool calls, and the model's reasoning-mode output format.

- --moe-backend deep_gemm_mega_moe selects the DeepGEMM MegaMoE expert kernel, the fastest path for V4-Pro's FP4 MoE on Blackwell.

- --speculative_config '{"method":"mtp","num_speculative_tokens":2}' enables V4-Pro's built-in Multi-Token Prediction (MTP) speculative decoding at K=2, reaching ~33% acceptance on this workload.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see deepseek-ai/DeepSeek-V4-Pro listed in the response.

### Benchmarking DeepSeek-V4-Pro

Benchmarks were collected with vllm bench serve using an 8192-input / 2048-output token workload across 512 prompts at 32 concurrent requests.

#### vLLM

Token throughput (NVIDIA HGX B200):

 | Metric
 | Tokens per second

 | Output generation
 | 911.92

 | Total (input & output)
 | 4,561.38

Latency (Mean / P99 in ms) (NVIDIA HGX B200):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 1,186.15
 | 7,121.00

 | Time per output token
 | 33.36
 | 54.29

 | Inter-token latency
 | 55.79
 | 690.12

## Next steps

### Upstream

- Download DeepSeek-V4-Pro on Hugging Face

- DeepSeek-V4 Technical Report (PDF)

### Downstream

Use as a Claude Code backend

Use your self-hosted DeepSeek-V4-Pro instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the vLLM server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="deepseek-ai/DeepSeek-V4-Pro"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-ai/DeepSeek-V4-Pro"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-ai/DeepSeek-V4-Pro"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-ai/DeepSeek-V4-Pro"

export ANTHROPIC_SMALL_FAST_MODEL="deepseek-ai/DeepSeek-V4-Pro"
export ANTHROPIC_FAST_MODEL="deepseek-ai/DeepSeek-V4-Pro"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
