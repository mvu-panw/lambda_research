# zai-org/GLM-5.3-Flash

Source: https://lambda.ai/inference-models/zai-org/glm-5.3-flash

Skip to main content

# How to deploy GLM-5.3-Flash on Lambda

## Performance

GLM-5.3-Flash

4× NVIDIA B200 · FP8 · SGLang

2,591 output tok/s maximum throughput

140 tok/s/user at interactive latency

C16 — Best balance of throughput and interactivityC1 — Highest tok/s/user

### Benchmark summary

 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | C1
 | 135.7
 | 139.8
 | 220 / 235
 | 7.2 / 7.2

 | C16
 | 1,070.5
 | 81.3
 | 2,890 / 3,590
 | 12.3 / 14.3

 | C64
 | 2,024.2
 | 42.1
 | 8,225 / 14,524
 | 23.7 / 30.3

 | C256
 | 2,590.8
 | 21.2
 | 31,167 / 91,345
 | 47.2 / 73.0

Methodology

Measured on 4× NVIDIA B200 GPUs (NVIDIA HGX B200 system), SGLang, tensor-parallel and expert-parallel size 4 (TP4/EP4), approximately 8192 input / 1024 output tokens per request, concurrency swept from 1 to 256 (labels C1–C256). NVIDIA's standard benchmark reporting plots time-to-first-token (TTFT) or inter-token latency (ITL) against total system throughput, with each point labeled by its concurrency level — the TTFT/ITL curves above follow that convention. The primary chart instead normalizes throughput per GPU to show the buyer-facing tradeoff between per-user speed and hardware efficiency, which is why its y-axis reads "per GPU" rather than "system."

## Background

GLM-5.3-Flash is Zhipu AI's (Z.ai) first natively multimodal model in the GLM-5 family, a 320-billion-parameter Mixture-of-Experts (MoE) model that activates only 18 billion parameters per token. Its defining contribution is architectural: it's the first GLM model to combine sparse attention and linear attention in a single hybrid stack, interleaving 34 Kimi Delta Attention (KDA) linear-attention layers with 11 DeepSeek Sparse Attention (DSA) layers in a fixed 3:1 pattern. This design attacks the dominant cost of long-context serving — attention compute and the KV cache — cutting attention compute by approximately 3.01x and KV-cache size by approximately 4.44x relative to the dense-attention GLM-5.3 sibling.

Two further changes accompany the hybrid attention. GLM-5.3-Flash adopts Manifold-Constrained Hyper-Connections (mHC), a residual-stream replacement that widens the residual into parallel streams while constraining the mixing matrix to be doubly stochastic via the Sinkhorn–Knopp algorithm, stabilizing training at scale. It also runs its Multi-head Latent Attention (MLA) layers in pure No-Position-Encoding (NoPE) mode — the rotary component is zeroed out — delegating position tracking to the interleaved linear-attention layers. The model is also natively multimodal, trained jointly with a 24-layer vision tower on a 30-trillion-token corpus spanning text, code, image, and video.

On benchmarks, GLM-5.3-Flash beats predecessor GLM-5.2 across every reported test — DeepSWE v1.1 rises 46.2 to 63.4, AutomationBench 26.2 to 48.8 — while approaching Claude Opus 4.8 on coding and agentic tasks at roughly one-tenth the price ($0.15/$0.50 per million input/output tokens). It leads the independently scored GDPval-AA v2 (1773 Elo) but trails frontier models on natural-image vision such as BabyVision (53.4 vs Gemini 3.7 Flash's 70.9). Nearly all non-Artificial-Analysis scores are vendor-reported and await independent verification. Released August 26, 2026 under an MIT license.

## Model specifications

### Overview

- Name: GLM-5.3-Flash

- Author: Z.ai (Zhipu AI / zai-org)

- Architecture: MoE, hybrid linear + sparse attention (Glm5NextForConditionalGeneration)

- License: MIT

### Specifications

- Total parameters: 320B total (18B active per token)

- Experts: 288 routed, 8 active per token, plus 1 shared expert

- Attention: 34 KDA linear-attention layers interleaved with 11 DSA sparse-attention layers (3:1 ratio); DSA/MLA layers run in pure NoPE mode

- Context window: 1,048,576 (1M) tokens

- Modality: Natively multimodal — text, image, and video input

- Precision: Native FP8 (e4m3, dynamic scaling) — official zai-org/GLM-5.3-Flash checkpoint

## Hardware requirements

- Minimal deployment:

- 4× NVIDIA B200 GPUs (a half NVIDIA HGX B200 system) — served at TP=4/EP=4. Use zai-org/GLM-5.3-Flash (native FP8) for the fastest throughput.

## Deployment and benchmarking

### Deploying GLM-5.3-Flash

GLM-5.3-Flash is served on 4× NVIDIA B200 GPUs with tensor-parallel and expert-parallel size 4.

- Launch an instance from the Lambda Cloud Console using the GPU Base 24.04 image: NVIDIA HGX B200.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server.

#### SGLang

docker run -d \
 --name pareto-glm53-flash \
 --gpus '"device=0,1,2,3"' \
 --ipc=host \
 --shm-size=64g \
 -p 127.0.0.1:18080:18080 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 --entrypoint python3 \
 lmsysorg/sglang:glm-5.3-flash@sha256:aa9210e3507fef64ded0c78afc571d9412b53417c6e271721a095fbde754ad40 \
 -m sglang.launch_server \
 --model-path zai-org/GLM-5.3-Flash \
 --revision eb9eb208eb0d988989d07a6a12d0fdeb5f52574a \
 --served-model-name zai-org/GLM-5.3-Flash \
 --host 0.0.0.0 \
 --port 18080 \
 --tp-size 4 \
 --ep-size 4 \
 --context-length 16384 \
 --max-running-requests 256 \
 --dsa-prefill-backend trtllm \
 --dsa-decode-backend trtllm \
 --kv-cache-dtype fp8_e4m3 \
 --moe-runner-backend deep_gemm \
 --reasoning-parser glm45 \
 --tool-call-parser glm47

#### Verify the server

curl -X GET http://localhost:18080/v1/models \
 -H "Content-Type: application/json"

You should see zai-org/GLM-5.3-Flash listed in the response.

## Next steps

### Upstream

- Download GLM-5.3-Flash on Hugging Face

### Downstream

Use as a Claude Code backend

Use your self-hosted GLM-5.3-Flash instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:18080"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="zai-org/GLM-5.3-Flash"
export ANTHROPIC_DEFAULT_SONNET_MODEL="zai-org/GLM-5.3-Flash"
export ANTHROPIC_DEFAULT_OPUS_MODEL="zai-org/GLM-5.3-Flash"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="zai-org/GLM-5.3-Flash"

export ANTHROPIC_SMALL_FAST_MODEL="zai-org/GLM-5.3-Flash"
export ANTHROPIC_FAST_MODEL="zai-org/GLM-5.3-Flash"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
