# LiquidAI/LFM2.5-8B-A1B

Source: https://lambda.ai/inference-models/liquidai/lfm2.5-8b-a1b

Skip to main content

# How to deploy LFM2.5-8B-A1B on Lambda

## TL;DR: token throughput

 SGLang
 vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | 1× NVIDIA B200 GPU
 | 6,098 tok/s
 | 206 tok/s
 | 30,489 tok/s
 | 792 ms
 | 4.9 ms

 | 1× NVIDIA H100 GPU
 | 3,714 tok/s
 | 125 tok/s
 | 18,572 tok/s
 | 1,248 ms
 | 8.0 ms

 | 1× NVIDIA A100 GPU
 | 1,950 tok/s
 | 68 tok/s
 | 9,751 tok/s
 | 3,594 ms
 | 14.7 ms

 | Hardware
 | Gen. throughput
 | Per-user gen
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | 1× NVIDIA B200 GPU
 | 7,253 tok/s
 | 238 tok/s
 | 36,267 tok/s
 | 433 ms
 | 4.5 ms

 | 1× NVIDIA H100 GPU
 | 3,787 tok/s
 | 123 tok/s
 | 18,937 tok/s
 | 568 ms
 | 8.2 ms

 | 1× NVIDIA A100 GPU
 | 1,971 tok/s
 | 64 tok/s
 | 9,853 tok/s
 | 962 ms
 | 15.7 ms

### Benchmark command

Re-run the benchmark:

vllm bench serve \
 --backend openai-chat \
 --model LiquidAI/LFM2.5-8B-A1B \
 --served-model-name lfm25_8b_a1b \
 --endpoint /v1/chat/completions \
 --dataset-name random \
 --random-input-len 8192 --random-output-len 2048 \
 --num-prompts 512 --max-concurrency 32

(8192 in / 2048 out tokens, 512 prompts, 32 parallel requests)

See Benchmarking results: LFM2.5-8B-A1B for the full results.

## Background

LFM2.5-8B-A1B is a small, fast reasoning model from Liquid AI, released with open weights and built to run on-device on phones and laptops as well as datacenter GPUs. It's a sparse Mixture-of-Experts model with 8.3 billion total parameters, only about 1.5 billion of which are active for any given token. It handles a 128k-token context and is aimed at agentic work like tool calling, structured output, instruction following, and multilingual assistance.

The architecture is what makes it quick. LFM2.5-8B-A1B keeps the LFM2 design, a 24-layer stack that's mostly gated short-convolution layers (18) with only 6 grouped-query-attention layers mixed in, plus 32 experts with top-4 routing. Because most layers use convolutions rather than full attention, the model avoids the cost that normally grows with context length, and it ranks as the fastest model in its size class. Version 2.5 leaves that design alone and instead reworks the training. It now reasons step by step before answering, was pre-trained on 38 trillion tokens (up from 12 trillion), went through reinforcement learning aimed at cutting hallucinations, and gained a larger vocabulary for better multilingual efficiency, along with a 128k context window, up from 32k.

The clearest payoff is honesty. Its non-hallucination rate on AA-Omniscience rose from 7.46 to 63.47, meaning the model now abstains on questions beyond its knowledge. It's strong on agentic and instruction-following work too, reaching 88.07 on Tau²-Telecom and 91.84 on IFEval. Liquid AI also notes the tradeoff: with modest factual recall, this is not the model for heavy programming or knowledge-heavy Q&A without retrieval.

## Model specifications

### Overview

- Name: LFM2.5-8B-A1B

- Author: Liquid AI

- Architecture: Hybrid MoE (gated short convolution + GQA attention), reasoning model

- License: LFM Open License v1.0 (custom)

### Specifications

- Total parameters: 8.3B (~1.5B active per token)

- Layers: 24 (18 convolution + 6 GQA attention); 32 experts, top-4 active

- Context window: 128K tokens (128,000)

- Vocabulary: 128,000 tokens

- Languages: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, Spanish

## Hardware requirements

LFM2.5-8B-A1B runs on a single GPU. At ~8.3B total parameters in BF16, the full weights fit in a single accelerator's memory:

- 1× NVIDIA B200 GPU (--tensor-parallel-size 1)

- 1× NVIDIA H100 GPU (--tensor-parallel-size 1)

- 1× NVIDIA A100 GPU (--tensor-parallel-size 1)

## Deployment and benchmarking

### Deploying LFM2.5-8B-A1B

LFM2.5-8B-A1B can be served with vLLM or SGLang on a single NVIDIA B200 GPU, NVIDIA H100 GPU, or NVIDIA A100 GPU.

- Launch a single-GPU instance (1× NVIDIA B200 GPU, NVIDIA H100 GPU, or NVIDIA A100 GPU) from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using one of the backends below.

Note: Day-one support for LFM2.5-8B-A1B ships in nightly/development builds of both backends. The image tags below are the nightly/dev builds used for these benchmarks; substitute a newer pinned tag once stable releases land.

 SGLang
 vLLM

docker run -d --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:nightly-dev-cu12-20260529-a8cfae0b \
 python3 -m sglang.launch_server \
 --model-path LiquidAI/LFM2.5-8B-A1B \
 --served-model-name lfm25_8b_a1b \
 --tp 1 \
 --host 0.0.0.0 --port 8000 \
 --tool-call-parser lfm2 \
 --trust-remote-code \
 --mem-fraction-static 0.9 \
 --disable-radix-cache

docker run -d --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:nightly-22a58640b4563f5945aa2052e9e61d425351588d \
 --model LiquidAI/LFM2.5-8B-A1B \
 --served-model-name lfm25_8b_a1b \
 --tensor-parallel-size 1 \
 --host 0.0.0.0 --port 8000 \
 --max-model-len auto \
 --enable-auto-tool-choice \
 --tool-call-parser pythonic \
 --trust-remote-code \
 --gpu-memory-utilization 0.9

Notable flags:

- --tensor-parallel-size 1 (vLLM) / --tp 1 (SGLang): the model fits on a single GPU, so no tensor parallelism is needed.

- vLLM --tool-call-parser pythonic with --enable-auto-tool-choice: enables OpenAI-compatible function calling using the model's Pythonic tool-call format.

- SGLang --tool-call-parser lfm2: the LFM2-family tool-call parser for function calling.

- SGLang --disable-radix-cache: required for correct behavior with this model on the current nightly build.

#### Verify the server

Either command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see lfm25_8b_a1b listed in the response.

### Benchmarking results: LFM2.5-8B-A1B

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests.

 SGLang
 vLLM

Token throughput:

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | Output gen (tok/s)
 | 6,098
 | 3,714
 | 1,950

 | Per-user gen (tok/s)
 | 206
 | 125
 | 68

 | Total (tok/s)
 | 30,489
 | 18,572
 | 9,751

Latency (Mean / P99 in ms):

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | TTFT
 | 792 / 2,110
 | 1,248 / 2,616
 | 3,594 / 6,495

 | TPOT
 | 4.9 / 5.1
 | 8.0 / 8.6
 | 14.7 / 16.3

 | ITL
 | 4.9 / 5.3
 | 8.0 / 8.0
 | 14.7 / 16.3

Token throughput:

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | Output gen (tok/s)
 | 7,253
 | 3,787
 | 1,971

 | Per-user gen (tok/s)
 | 238
 | 123
 | 64

 | Total (tok/s)
 | 36,267
 | 18,937
 | 9,853

Latency (Mean / P99 in ms):

 | Metric
 | 1× B200
 | 1× H100
 | 1× A100

 | TTFT
 | 433 / 2,148
 | 568 / 2,987
 | 962 / 7,433

 | TPOT
 | 4.2 / 4.5
 | 8.2 / 8.4
 | 15.7 / 16.3

 | ITL
 | 4.5 / 24.5
 | 8.2 / 59.2
 | 15.7 / 62.8

## Next steps

### Upstream

- Download LFM2.5-8B-A1B on Hugging Face

- LFM2.5-8B-A1B blog post (Liquid AI)

### Downstream

Use as a Claude Code backend

Use your self-hosted LFM2.5-8B-A1B instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node running the server:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="lfm25_8b_a1b"
export ANTHROPIC_DEFAULT_SONNET_MODEL="lfm25_8b_a1b"
export ANTHROPIC_DEFAULT_OPUS_MODEL="lfm25_8b_a1b"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="lfm25_8b_a1b"

export DISABLE_TELEMETRY=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
