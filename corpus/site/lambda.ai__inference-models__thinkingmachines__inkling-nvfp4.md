# thinkingmachines/Inkling-NVFP4

Source: https://lambda.ai/inference-models/thinkingmachines/inkling-nvfp4

Skip to main content

# How to deploy Inkling on Lambda

## TL;DR: token throughput

Measured on NVIDIA HGX B200, CUDA 13.0. 8192 in / 2048 out tokens, 32 concurrent requests, 512 prompts, served at TP=8 on the official NVFP4 checkpoint.

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 2,510.64 tok/s
 | 78.46 tok/s
 | 12,553.21 tok/s
 | 2,023.21 ms
 | 11.76 ms

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | NVIDIA HGX B200
 | 2,419.29 tok/s
 | 75.60 tok/s
 | 12,096.44 tok/s
 | 1,106.80 ms
 | 12.69 ms

### Benchmark command

(8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests — the workload recorded for the auto-benchmark run.)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document-analysis workflows.

Benchmark configuration:

vllm bench serve \
 --backend openai-chat \
 --model thinkingmachines/Inkling-NVFP4 \
 --served-model-name inkling \
 --dataset-name random \
 --random-input-len 8192 \
 --random-output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32 \
 --endpoint /v1/chat/completions

See Benchmarking Inkling below for the full results.

## Background

Inkling is the first openly released foundation model from Thinking Machines Lab. It is a sparse mixture-of-experts decoder that is natively multimodal, mapping text and images along with video and audio into a single shared representation processed by the same trunk, with no separate vision or speech encoders bolted on. The stack is 66 decoder blocks holding roughly 975 billion total parameters, of which about 41 billion are active per token. Weights ship under a modified Apache-2.0 license in two numeric builds (a BF16 base and an NVFP4 four-bit build tuned for Blackwell), and the usable context window runs past a million tokens (~1,048,576).

Because this is the lab's debut open release, there is no in-house predecessor to compare against, so the novelty lives in the architecture. The feed-forward path uses 256 small experts with 6 routed per token plus 2 always-on shared experts, steered by a sigmoid router with a learned per-expert bias (penalty-free load balancing) rather than an auxiliary loss. Attention interleaves 55 short-window blocks (512-token span) with 11 full-view blocks in roughly a 5:1 ratio and, unusually, gives the cheap windowed blocks more key/value memory than the full-view ones, keeping the long-context memory bill lean. A length-tied temperature keeps attention sharp out to the million-token ceiling, an eight-deep multi-token-prediction stack both densifies the training signal and enables self-drafting (speculative) decode, and a continuous thinking-effort control lets callers dial the reasoning budget (headline scores are reported at effort 0.99).

On the leaderboard snapshot embedded in its model card, Inkling reads as a top-tier open model: near-perfect on competition math (~97%), high-80s on graduate-level science, and high-70s on practical software-fixing tasks, trading blows with the strongest open contenders while trailing the best closed systems on the very hardest reasoning and raw-knowledge tests. Instruction-following and safety-refusal rates are standouts.

## Model specifications

### Overview

- Name: Inkling

- Author: Thinking Machines Lab

- Architecture: Sparse Mixture-of-Experts (MoE), natively multimodal, decoder-only

- License: Modified Apache-2.0

### Specifications

- Total parameters: ~975B (~41B active per token)

- Experts: 256 routed experts, top-6 per token, plus 2 shared experts (first blocks dense)

- Decoder blocks: 66

- Attention: 64 query heads; 55 windowed blocks plus 11 full-view blocks, ~5:1

- Multi-token prediction: 8-deep look-ahead stack for self-drafting decode

- Context window: 1,048,576 tokens (~1.05M)

- Modalities: Text, images, video, and audio through encoder-free early fusion

## Hardware requirements

For the benchmarked Inkling NVFP4 deployment, use 1× NVIDIA HGX B200 with tensor parallelism (TP=8). The tested vLLM deployment supports 32,768 tokens; Inkling advertises a context window of approximately 1.05M tokens.

### Checkpoint options

- NVFP4: thinkingmachines/Inkling-NVFP4 — benchmarked in this card on the hardware above.

- BF16: thinkingmachines/Inkling — available upstream, but this card does not document a Lambda hardware configuration or benchmark for the BF16 checkpoint.

## Deployment and benchmarking

### Deploying Inkling

The serving commands below use tensor parallelism (TP=8), matching the benchmark configuration above.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image: NVIDIA HGX B200.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using one of the backends below.

 SGLang
 vLLM

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -e SGLANG_ENABLE_UNIFIED_RADIX_TREE=1 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:inkling-cu13 \
 python3 -m sglang.launch_server \
 --model-path thinkingmachines/Inkling-NVFP4 \
 --served-model-name inkling \
 --tp 8 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --quantization modelopt_fp4 \
 --attention-backend fa4 \
 --page-size 128 \
 --fp4-gemm-backend flashinfer_trtllm \
 --moe-runner-backend flashinfer_trtllm_routed \
 --enable-torch-symm-mem \
 --mamba-radix-cache-strategy extra_buffer \
 --mem-fraction-static 0.85 \
 --swa-full-tokens-ratio 0.1 \
 --mamba-full-memory-ratio 0.1 \
 --enable-multimodal \
 --reasoning-parser inkling \
 --tool-call-parser inkling

Note: Inkling is a day-0 architecture. Use the dedicated Inkling image (vllm/vllm-openai:inkling-x86_64-cu130 on CUDA 13 hosts), disable vLLM's breakable-CUDA-graph path with VLLM_USE_BREAKABLE_CUDAGRAPH=0 (otherwise the engine dies on the first request with a cudagraph replay assertion), and cap --max-model-len (the ~1M default OOMs KV/graph capture on an 8× B200 node).

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -e VLLM_USE_V2_MODEL_RUNNER=1 \
 -e FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1 \
 -e VLLM_USE_BREAKABLE_CUDAGRAPH=0 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:inkling-x86_64-cu130 \
 --model thinkingmachines/Inkling-NVFP4 \
 --served-model-name inkling \
 --tensor-parallel-size 8 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --tokenizer-mode inkling \
 --reasoning-parser inkling \
 --tool-call-parser inkling \
 --enable-auto-tool-choice \
 --max-model-len 32768 \
 --kernel-config.enable_flashinfer_autotune=False \
 --gpu-memory-utilization 0.9

Either command launches an inference server with an OpenAI-compatible API on port 8000.

- Verify the server is running:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see inkling listed in the response.

Note: The throughput benchmark client also needs a recent Transformers build to load Inkling's tokenizer — install it with pip install git+https://github.com/huggingface/transformers.git before running vllm bench serve.

### Benchmarking Inkling

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests, on NVIDIA HGX B200 (TP=8).

 SGLang
 vLLM

NVIDIA HGX B200
Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 2,023.21 ms
 | 3,758.83 ms

 | Time per output token
 | 11.76 ms
 | 12.64 ms

 | Inter-token latency
 | 11.76 ms
 | 11.87 ms

NVIDIA HGX B200
Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 1,106.80 ms
 | 3,862.28 ms

 | Time per output token
 | 12.69 ms
 | 13.14 ms

 | Inter-token latency
 | 12.69 ms
 | 136.52 ms

## Next steps

### Upstream

- Download Inkling NVFP4 weights on Hugging Face

- Download Inkling BF16 weights on Hugging Face

- Read the Thinking Machines Lab announcement: Inkling: Our Open-Weights Model

### Downstream

Use as a noumena code backend

Use your self-hosted Inkling as the backend to noumena's code framework rather than their hosted models for local development. Replace <NODE_IP> with the IP of the node where the server is running.

git clone https://github.com/noumena-network/code.git
cd code
bun install
bun run build

OPENAI_API_KEY="dummy" \
OPENAI_BASE_URL="http://<NODE_IP>:8000/v1" \
OPENAI_MODEL="inkling" \
./.tmp/packages/ncode-0.1.0-linux-x64/ncode \
 --print \
 --model inkling \
 --max-turns 1 \
 "Reply exactly: ok"

Use as a Claude Code backend

Use your self-hosted Inkling instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="inkling"
export ANTHROPIC_DEFAULT_SONNET_MODEL="inkling"
export ANTHROPIC_DEFAULT_OPUS_MODEL="inkling"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="inkling"

export ANTHROPIC_SMALL_FAST_MODEL="inkling"
export ANTHROPIC_FAST_MODEL="inkling"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
