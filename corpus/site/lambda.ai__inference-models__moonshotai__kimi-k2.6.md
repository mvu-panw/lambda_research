# moonshotai/Kimi-K2.6

Source: https://lambda.ai/inference-models/moonshotai/kimi-k2.6

Skip to main content

# How to deploy Kimi K2.6 on Lambda

## TL;DR: token throughput

### vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 1408 tok/s
 | 44 tok/s
 | 7046 tok/s
 | 2264 ms
 | 44.5 ms

(8192 in / 2048 out tokens, 32 parallel requests, 512 prompts)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document analysis workflows, in which large contexts are provided as input with substantial completions as output.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model moonshotai/Kimi-K2.6 \
 --served-model-name kimi-k2.6 \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking Kimi K2.6 for the full results.

## Background

Kimi K2.6 is a 1.04T-parameter sparse Mixture-of-Experts (MoE) vision-language model from Moonshot AI. It supports a native 256k-token context window and ships with two reasoning modes (Thinking, default; Instant).

K2.6 is yet another post-training and capability-scaling change on top of Kimi K2.

In Thinking mode, Kimi K2.6 leads open-weights agentic benchmarks (Toolathlon: 50.0, MCPMark: 55.9, Terminal-Bench 2.0: 66.7, SWE-Bench Verified: 80.2) and ranks #1 of 77 open-weights models on Artificial Analysis Intelligence Index, behind only Claude Opus 4.6, GPT-5.4, and Gemini 3.1 Pro.

## Model specifications

### Overview

- Name: Kimi K2.6

- Author: Moonshot AI

- Architecture: MoE with MLA attention + MoonViT-3D vision encoder

- License: Modified MIT

### Specifications

- Total parameters: 1.04T (32B active per forward pass)

- Context window: 256K tokens (262,144) via YaRN

- Precision: INT4 (MoE experts, native QAT) + BF16 (other parameters), mixed

- Reasoning modes: Thinking (default), Instant

- Vision: MoonViT-3D (~400M parameters), image and video

## Hardware requirements

- Minimal deployment:

- NVIDIA HGX B200 node

## Deployment and benchmarking

### Deploying Kimi K2.6

Kimi K2.6 fits on a single 8× NVIDIA B200 node and is tuned here for a user coding harness with EAGLE-3 speculative decoding.

- Launch an instance with an NVIDIA HGX B200 from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the vLLM server:

docker run -d --gpus all \
 --ipc=host \
 -p 8001:8001 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 -e VLLM_USE_V1=1 \
 --entrypoint bash \
 vllm/vllm-openai:cu130-nightly \
 -c "pip install -q 'transformers==4.57.6' && exec python3 -m vllm.entrypoints.openai.api_server \
 --model moonshotai/Kimi-K2.6 \
 --served-model-name kimi-k2.6 \
 --host 0.0.0.0 \
 --port 8001 \
 --tensor-parallel-size 8 \
 --mm-encoder-tp-mode data \
 --compilation_config.pass_config.fuse_allreduce_rms true \
 --tool-call-parser kimi_k2 \
 --reasoning-parser kimi_k2 \
 --enable-auto-tool-choice \
 --trust-remote-code \
 --kv-cache-dtype fp8 \
 --no-enable-prefix-caching \
 --speculative-config '{\"method\":\"eagle3\",\"model\":\"lightseekorg/kimi-k2.6-eagle3\",\"num_speculative_tokens\":3}'"

This launches a vLLM server with an OpenAI-compatible API on port 8001. Notable flags:

- --tensor-parallel-size 8 shards the model across all 8 B200 GPUs on the node.

- --speculative-config enables EAGLE-3 speculative decoding with the lightseekorg/kimi-k2.6-eagle3 draft model and 3 speculative tokens per step. This is the largest single win on real-text output (+60-90% generation throughput).

- --kv-cache-dtype fp8 stores the KV cache in FP8 (+7% throughput) and frees up cache headroom for the 256K context window.

- --no-enable-prefix-caching disables prefix-cache hashing (+9% on coding prompts, where hits are rare and the per-token hash overhead dominates).

- --tool-call-parser kimi_k2 and --reasoning-parser kimi_k2 enable Kimi's OpenAI-compatible tool-call format and the model's Thinking-mode output format. Both are required because K2.6 enables Thinking mode by default.

- --mm-encoder-tp-mode data runs the MoonViT-3D vision encoder under data parallelism rather than tensor parallelism, which is the recommended topology for the vision tower.

- --compilation_config.pass_config.fuse_allreduce_rms true fuses the post-attention all-reduce with the following RMSNorm.

- Verify the server is running:

curl -X GET http://localhost:8001/v1/models \
 -H "Content-Type: application/json"

You should see kimi-k2.6 listed in the response.

### Benchmarking Kimi-K2.6

Benchmarks were collected with vllm bench serve using an 8192-input / 2048-output token workload across 512 prompts at 32 concurrent requests.

#### vLLM

Token throughput (NVIDIA HGX B200):

 | Metric
 | Tokens per second

 | Output generation
 | 1408

 | Total (input & output)
 | 7046

Latency (Mean / P99 in ms) (NVIDIA HGX B200):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 2264.48 ms
 | 32176.03 ms

 | Time per output token
 | 21.14 ms
 | 40.22 ms

 | Inter-token latency
 | 44.50 ms
 | 373.2 ms

## Next steps

### Upstream

- Download Kimi K2.6 on Hugging Face

- Kimi K2 Technical Report (arXiv:2507.20534)

- Kimi K2.5 Technical Report (arXiv:2602.02276)

### Downstream

Use as a Claude Code backend

Use your self-hosted Kimi K2.6 instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the vLLM server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8001"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="kimi-k2.6"
export ANTHROPIC_DEFAULT_SONNET_MODEL="kimi-k2.6"
export ANTHROPIC_DEFAULT_OPUS_MODEL="kimi-k2.6"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="kimi-k2.6"

export ANTHROPIC_SMALL_FAST_MODEL="kimi-k2.6"
export ANTHROPIC_FAST_MODEL="kimi-k2.6"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
