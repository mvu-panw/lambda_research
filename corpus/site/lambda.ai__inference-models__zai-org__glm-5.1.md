# zai-org/GLM-5.1

Source: https://lambda.ai/inference-models/zai-org/glm-5.1

Skip to main content

# How to deploy GLM-5.1 on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TTFT
 | ITL

 | 1× NVIDIA HGX B200
 | 1,345 tok/s
 | 42.0 tok/s/user
 | 6,727 tok/s
 | 1,073ms
 | 59ms

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TTFT
 | ITL

 | 1× NVIDIA HGX B200
 | 1,265 tok/s
 | 39.5 tok/s/user
 | 6,327 tok/s
 | 1,317ms
 | 58ms

### Benchmark command

The benchmark uses a 4:1 input-to-output token ratio (8,192 in / 2,048 out per request, 512 prompts, 32 parallel requests) to simulate a realistic Claude Code backend workload, where large tool results, file reads, and conversation history dominate the input while the model returns a moderate response plus thinking-mode reasoning. Per-user generation throughput is aggregate generation tok/s divided by the concurrency level, or the rate each individual user sees their response streaming back.

Re-run the benchmark:

vllm bench serve \
 --model zai-org/GLM-5.1-FP8 \
 --served-model-name glm-5.1-fp8 \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 2048 \
 --num-prompts 512 --max-concurrency 32

(8192 in / 2048 out tokens, 32 parallel requests)

## Background

GLM-5.1 is an incremental update to Z.ai's GLM-5, maintaining the same architecture as GLM-5 (40B active per token, 256 routed experts with top-8 routing plus 1 shared expert, Multi-head Latent Attention combined with DeepSeek Sparse Attention, and a Multi-Token Prediction head for speculative decoding).

Compared with GLM-5, GLM-5.1 delivers significant improvements in coding, agentic tool use, reasoning, role-play, and long-horizon agentic tasks (e.g. CUDA kernel optimization):

 | Benchmark
 | GLM-5.1 (FP8)
 | GLM-5 (FP8, reference)

 | Terminal-Bench 2
 | 63.5
 | 56.2

 | AIME 25
 | 95.3
 | —

 | HLE
 | 31.0
 | 30.5

 | GPQA
 | 86.2
 | —

 | SWE-Bench Pro
 | 58.4
 | —

The biggest behavioral change vs GLM-5 is that thinking mode is enabled by default. GLM-5.1 uses the same Interleaved and Preserved Thinking patterns as GLM-5: use Interleaved Thinking for general chat, and Interleaved + Preserved Thinking for agentic workflows such as Claude Code, Roo Code, or Kilo Code. See Z.ai's thinking-mode docs for details.

The chat template also changes: GLM-5.1 supports Claude-style deferred tool loading (tools with defer_loading=True do not appear in the system prompt; they appear in tool results instead), allows empty reasoning content in assistant messages, and accepts both List[tool] and List[tool.function] for SGLang compatibility.

## Model specifications

### Overview

- Name: GLM-5.1

- Author: Z.ai (zai-org)

- Architecture: MoE with Multi-head Latent Attention (MLA) + DeepSeek Sparse Attention (DSA), Multi-Token Prediction (MTP) head

- License: MIT

### Specifications

- Total parameters: 744B (40B active per token)

- Routed experts: 256 (top-8 active per token) + 1 shared expert; first 3 layers dense

- Context window: 202,752 tokens

### Recommended Lambda VRAM configuration

- Minimal deployment:

- 1× NVIDIA HGX B200 (8× NVIDIA B200 GPU system) is required to load the 744B-parameter model. Use the FP8 quantized version (zai-org/GLM-5.1-FP8) for the fastest throughput.

## Deployment and benchmarking

### Deploying GLM-5.1

GLM-5.1 requires, at minimum, 1× NVIDIA HGX B200 to load the 744B-parameter model.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image (1x NVIDIA HGX B200 (8x NVIDIA B200 GPUs)).

- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using either SGLang or vLLM:

 SGLang
 vLLM

Important: Use SGLang 0.5.10 — not 0.5.10rc0, which has a known flashmla bug that has been fixed in the 0.5.10 release.

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:v0.5.10-cu12 \
 python -m sglang.launch_server \
 --model-path zai-org/GLM-5.1-FP8 \
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
 --served-model-name glm-5.1-fp8

Important: Upgrade transformers to v5.3.0 or later inside the vLLM container before launching. The base vLLM 0.19.0 image ships an older transformers that does not yet support GLM-5.1's chat template.

docker run \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 --entrypoint /bin/bash \
 vllm/vllm-openai:v0.19.0 \
 -c "pip install --upgrade 'transformers>=5.3.0' && \
 vllm serve zai-org/GLM-5.1-FP8 \
 --tensor-parallel-size 8 \
 --max-model-len 202752 \
 --max-num-seqs 64 \
 --trust-remote-code \
 --speculative-config.method mtp \
 --speculative-config.num_speculative_tokens 3 \
 --tool-call-parser glm47 \
 --reasoning-parser glm45 \
 --enable-auto-tool-choice \
 --served-model-name glm-5.1-fp8 \
 --port 8000 \
 --host 0.0.0.0"

#### Verify the server

Either command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see glm-5.1-fp8 listed in the response.

### Recommended inference parameters

Z.ai's recommended defaults for GLM-5.1:

 | Scenario
 | Temperature
 | Top-p
 | Max new tokens
 | Notes

 | Default (most tasks)
 | 1.0
 | 0.95
 | 131,072
 | Interleaved Thinking (default)

 | Terminal-Bench 2
 | 0.7
 | 1.0
 | 16,384
 | Preserved Thinking ON; context 202,752

 | τ²-Bench (tool use)
 | 0
 | —
 | 16,384
 | Preserved Thinking ON

For multi-turn agentic tasks (τ²-Bench, Terminal-Bench 2), enable Preserved Thinking by sending chat_template_kwargs with enable_thinking: true and clear_thinking: false. To disable thinking entirely, send chat_template_kwargs: {"enable_thinking": false}.

### Benchmarking results: GLM-5.1

 SGLang
 vLLM

Token throughput:

 | Metric
 | 1× NVIDIA HGX B200

 | Output gen (tok/s)
 | 1,345.44

 | Per-user gen (tok/s/user)
 | 42.04

 | Total (tok/s)
 | 6,727.19

Latency (Mean / P99 in ms):

 | Metric
 | 1× NVIDIA HGX B200

 | TTFT
 | 1,072.61 / 14,237.85

 | TPOT
 | 22.83 / 30.60

 | ITL
 | 58.61 / 452.50

Token throughput:

 | Metric
 | 1× NVIDIA HGX B200

 | Output gen (tok/s)
 | 1,265.45

 | Per-user gen (tok/s/user)
 | 39.55

 | Total (tok/s)
 | 6,327.24

Latency (Mean / P99 in ms):

 | Metric
 | 1× NVIDIA HGX B200

 | TTFT
 | 1,316.86 / 14,853.08

 | TPOT
 | 24.34 / 30.26

 | ITL
 | 57.79 / 530.82

## Next steps

To get started with GLM-5.1, follow the directions above. Read more about the model:

- Download GLM-5.1-FP8 on Hugging Face

- Z.ai thinking-mode documentation

- SGLang GLM-5 cookbook (same architecture, applies to GLM-5.1)

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
