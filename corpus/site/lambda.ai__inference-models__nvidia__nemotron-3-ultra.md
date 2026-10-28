# nvidia/nemotron-3-ultra

Source: https://lambda.ai/inference-models/nvidia/nemotron-3-ultra

Skip to main content

# How to deploy Nemotron 3 Ultra on Lambda

## TL;DR: token throughput

All benchmarks use the single NVFP4 checkpoint (nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4) on a decode-heavy 8K-input / 64K-output workload at 256 concurrent requests. Per-user generation throughput is aggregate generation tok/s divided by the concurrency level — the rate each individual user sees their response stream back.

SGLang
TensorRT-LLM
vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TPOT (ms)
 | ITL (ms)

 | 4× NVIDIA Blackwell GPU
 | 2,363 tok/s
 | 9.2 tok/s/user
 | 2,659 tok/s
 | 77
 | 77

 | NVIDIA HGX H100
 | 1,930 tok/s
 | 7.5 tok/s/user
 | 2,171 tok/s
 | 46
 | 46

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TPOT (ms)
 | ITL (ms)

 | 4× NVIDIA Blackwell GPU
 | 3,404 tok/s
 | 13.3 tok/s/user
 | 3,830 tok/s
 | 14
 | 48

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TPOT (ms)
 | ITL (ms)

 | 4× NVIDIA Blackwell GPU
 | 2,305 tok/s
 | 9.0 tok/s/user
 | 2,594 tok/s
 | 57
 | —

 | NVIDIA HGX H100
 | 979 tok/s
 | 3.8 tok/s/user
 | 1,101 tok/s
 | 21
 | —

The vLLM runs did not complete cleanly at 256-way concurrency (450/512 requests completed on 4× Blackwell, 229/512 on the NVIDIA HGX H100) and its inter-token-latency counter returned inconsistent values, so vLLM figures are provisional and its ITL is omitted. SGLang and TensorRT-LLM both completed the full run.

### Benchmark command

The benchmark uses a decode-heavy 1:8 input-to-output token ratio (8,192 in / 65,536 out per request, 512 prompts, 256 concurrent requests) to stress generation throughput — the regime where Nemotron 3 Ultra's hybrid Mamba-2 architecture is designed to excel, since per-token decode cost stays constant regardless of context length. This differs from prefill-heavy coding workloads, where throughput tracks the active-parameter count instead.

At this concurrency the server stays saturated with a queue roughly two requests deep, so time-to-first-token is dominated by queue wait (tens of minutes for late-queued requests) rather than prefill latency. We therefore report steady-state per-token latency (TPOT and ITL) instead of TTFT.

Re-run the benchmark:

vllm bench serve \
 --model nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 \
 --served-model-name nemotron-3-ultra \
 --endpoint /v1/chat/completions \
 --random-input-len 8192 --random-output-len 65536 \
 --num-prompts 512 --max-concurrency 256

(8192 in / 65536 out tokens, 256 parallel requests)

## Background

Nemotron 3 Ultra ranks as the largest and most capable model NVIDIA has released, and among the most openly published frontier models available. NVIDIA ships the base, post-trained, and quantized checkpoints together with an Ultra-scale reward model, the training data, the training recipes, and the reinforcement-learning environments under the permissive OpenMDW-1.1 license. The pitch comes down to one promise: frontier-grade accuracy at a fraction of the inference cost, in a package that fits on a single GPU node.

That efficiency rests on two design choices. First, the model carries 550 billion parameters but activates only 55 billion per token, a 10% ratio, so each token pays for a sliver of its total capacity. Second, NVIDIA pre-trained the model directly in NVFP4, a 4-bit floating-point format, across 20 trillion tokens — what the technical report calls the largest-scale demonstration of stable, accurate 4-bit pre-training to date. Learning the weights in 4-bit shrinks the released NVFP4 checkpoint from roughly 1.1 TB to about 330 GB with almost no measurable quality loss, and one checkpoint runs natively on NVIDIA Blackwell GPUs (4-bit math) and as weight-only 4-bit on NVIDIA Hopper GPUs.

Under the hood sits a 108-layer hybrid architecture. Mamba-2 state-space layers keep decode cost constant regardless of context length, LatentMoE feed-forward blocks route 512 experts in a compressed latent space to afford more capacity per FLOP, and a handful of sparse attention layers act as long-range anchors. Shared-weight Multi-Token Prediction (MTP) heads provide built-in speculative decoding. The design reuses the architectural template introduced in Nemotron 3 Super (March 2026), scaled roughly 4.6×. The genuinely new work lands in post-training: Multi-teacher On-Policy Distillation (MOPD), in which more than ten domain-specialized teacher models supply dense, token-level feedback on the student's own rollouts, followed by an MTP Boosting stage that sharpens the speculative-decoding head and lifts decode throughput up to 2.89×.

On accuracy, the model holds its own against open frontier peers such as GLM-5.1, Kimi-K2.6, and DeepSeek-V4. It scores a top-3-human-level 570/600 on IOI 2025 competitive programming, 71.9 on SWE-Bench Verified, and 94.7 on RULER at 1 million tokens of context, while delivering reported decode-heavy throughput of roughly 5.9×, 4.8×, and 1.6× over GLM-5.1, Kimi-K2.6, and Qwen-3.5 respectively. Nemotron 3 Ultra supports up to 1 million tokens of context, with reasoning effort configurable to full, medium, or off.

## Model specifications

### Overview

- Name: Nemotron 3 Ultra
- Author: NVIDIA
- Architecture: NemotronH (Hybrid Mamba-2 + LatentMoE + Attention with MTP)
- License: OpenMDW-1.1 (commercial use permitted)

### Specifications

- Total parameters: 550B (55B active per token)
- Context window: 262,144 tokens (extendable to 1,000,000)
- Precision: NVFP4 (native 4-bit on Blackwell, weight-only 4-bit on Hopper)

### Recommended Lambda VRAM configuration

The single NVFP4 checkpoint (~330 GB) serves both Blackwell and Hopper deployments:

- Minimal deployment:
- 4× NVIDIA Blackwell GPU (--tp 4) — native NVFP4 (W4A4)
- NVIDIA HGX H100 (--tp 8) — weight-only NVFP4 (W4A16)

## Deployment and benchmarking

### Deploying Nemotron 3 Ultra

Nemotron 3 Ultra requires, at minimum, 4× NVIDIA Blackwell GPUs or an NVIDIA HGX H100 to load the NVFP4 checkpoint.

- Launch an instance with 4× Blackwell or an NVIDIA HGX H100 from the Lambda Cloud Console using the GPU Base 24.04 image.
- Connect to your instance via SSH or JupyterLab terminal. See Connecting to an instance for detailed instructions.
- Start the inference server using SGLang, TensorRT-LLM, or vLLM. The commands below are the exact launch configurations used to produce the benchmark numbers in this article. The SGLang images (sglang-n3u:patched3 on Blackwell, sglang-n3u-hopper:patched2 on Hopper) are NVIDIA pre-release patched builds used for benchmarking; substitute your own SGLang image if these are not available to you.

SGLang
TensorRT-LLM
vLLM

4× Blackwell
HGX H100

docker run -d \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -e HF_TOKEN=$HF_TOKEN \
 -e SGLANG_LOG_LEVEL=DEBUG \
 -e SAFETENSORS_FAST_GPU=1 \
 -e NVIDIA_TF32_OVERRIDE=1 \
 -e SGLANG_DISABLE_DEEP_GEMM=1 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 sglang-n3u:patched3 \
 python3 -m sglang.launch_server \
 --model-path nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 \
 --served-model-name nemotron-3-ultra \
 --tp 4 \
 --host 0.0.0.0 \
 --port 8000 \
 --tool-call-parser qwen3_coder \
 --reasoning-parser nemotron_3 \
 --trust-remote-code \
 --mem-fraction-static 0.85 \
 --disable-radix-cache \
 --context-length 262144 \
 --chunked-prefill-size 32768 \
 --disable-piecewise-cuda-graph \
 --kv-cache-dtype fp8_e4m3 \
 --max-running-requests 256

docker run -d \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -e HF_TOKEN=$HF_TOKEN \
 -e SGLANG_LOG_LEVEL=DEBUG \
 -e SAFETENSORS_FAST_GPU=1 \
 -e NVIDIA_TF32_OVERRIDE=1 \
 -e SGLANG_DISABLE_DEEP_GEMM=1 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 sglang-n3u-hopper:patched2 \
 python3 -m sglang.launch_server \
 --model-path nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 \
 --served-model-name nemotron-3-ultra \
 --tp 8 \
 --host 0.0.0.0 \
 --port 8000 \
 --tool-call-parser qwen3_coder \
 --reasoning-parser nemotron_3 \
 --trust-remote-code \
 --mem-fraction-static 0.85 \
 --context-length 262144 \
 --disable-piecewise-cuda-graph \
 --max-running-requests 256

TensorRT-LLM delivers the highest throughput on Blackwell and enables the model's MTP speculative decoding. First write the extra config, then launch on 4× NVIDIA Blackwell:

mkdir -p ~/benchmark
cat > ~/benchmark/extra-llm-api-config.yml << 'YAML'
cuda_graph_config:
 enable_padding: true
 max_batch_size: 32

enable_chunked_prefill: true
max_seq_len: 77824
enable_attention_dp: true
max_num_tokens: 8192
num_postprocess_workers: 4

kv_cache_config:
 dtype: fp8
 enable_block_reuse: false
 free_gpu_memory_fraction: 0.6
 mamba_ssm_cache_dtype: float16
 mamba_ssm_philox_rounds: 5
 mamba_ssm_stochastic_rounding: true

moe_config:
 backend: CUTEDSL

speculative_config:
 decoding_type: MTP
 max_draft_len: 3
 num_nextn_predict_layers: 3
 allow_advanced_sampling: true
YAML
docker run -d \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 --ulimit memlock=-1 \
 --ulimit stack=67108864 \
 -e HF_HOME=/root/.cache/huggingface \
 -e HF_TOKEN=$HF_TOKEN \
 -e HUGGING_FACE_HUB_TOKEN=$HF_TOKEN \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 -v ~/benchmark/extra-llm-api-config.yml:/config/extra-llm-api-config.yml:ro \
 nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc17 \
 trtllm-serve nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 \
 --host 0.0.0.0 \
 --port 8000 \
 --backend pytorch \
 --served_model_name nemotron-3-ultra \
 --tp_size 4 \
 --reasoning_parser nano-v3 \
 --tool_parser qwen3_coder \
 --trust_remote_code \
 --max_batch_size 32 \
 --ep_size 4 \
 --max_num_tokens 8192 \
 --extra_llm_api_options /config/extra-llm-api-config.yml

vLLM serves the same checkpoint with MTP speculative decoding. Note that we saw elevated request failures at 256-way concurrency on this release of vLLM (v0.22.0); for production at high concurrency, prefer SGLang or TensorRT-LLM until the issue is resolved.

4× Blackwell
HGX H100

docker run -d \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -e HUGGING_FACE_HUB_TOKEN=$HF_TOKEN \
 -e VLLM_LOGGING_LEVEL=DEBUG \
 -e VLLM_WORKER_MULTIPROC_METHOD=spawn \
 -e SAFETENSORS_FAST_GPU=1 \
 -e NVIDIA_TF32_OVERRIDE=1 \
 -e VLLM_USE_DEEP_GEMM=0 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:v0.22.0 \
 --model nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 \
 --served-model-name nemotron-3-ultra \
 --tensor-parallel-size 4 \
 --host 0.0.0.0 \
 --port 8000 \
 --max-model-len 262144 \
 --enable-auto-tool-choice \
 --tool-call-parser qwen3_coder \
 --reasoning-parser nemotron_v3 \
 --trust-remote-code \
 --gpu-memory-utilization 0.9 \
 --enable-expert-parallel \
 --kv-cache-dtype fp8 \
 --max-num-seqs 256 \
 --max-num-batched-tokens 32768 \
 --enable-chunked-prefill \
 --enable-prefix-caching \
 --mamba-ssm-cache-dtype float16 \
 --mamba-backend flashinfer \
 --enable-mamba-cache-stochastic-rounding \
 --mamba-cache-philox-rounds 5 \
 --speculative-config '{"method": "nemotron_h_mtp", "num_speculative_tokens": 5}'

docker run -d \
 --gpus all \
 -p 8000:8000 \
 --ipc=host \
 -e HF_HOME=/root/.cache/huggingface \
 -e HUGGING_FACE_HUB_TOKEN=$HF_TOKEN \
 -e VLLM_LOGGING_LEVEL=DEBUG \
 -e VLLM_WORKER_MULTIPROC_METHOD=spawn \
 -e SAFETENSORS_FAST_GPU=1 \
 -e NVIDIA_TF32_OVERRIDE=1 \
 -e VLLM_USE_DEEP_GEMM=0 \
 -e VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:v0.22.0 \
 --model nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4 \
 --served-model-name nemotron-3-ultra \
 --tensor-parallel-size 8 \
 --host 0.0.0.0 \
 --port 8000 \
 --max-model-len 262144 \
 --enable-auto-tool-choice \
 --tool-call-parser qwen3_coder \
 --reasoning-parser nemotron_v3 \
 --trust-remote-code \
 --gpu-memory-utilization 0.9 \
 --kv-cache-dtype fp8 \
 --max-num-seqs 256 \
 --max-num-batched-tokens 32768 \
 --enable-flashinfer-autotune \
 --async-scheduling \
 --speculative_config.method mtp \
 --speculative_config.num_speculative_tokens 5 \
 --mamba-backend triton \
 --mamba-ssm-cache-dtype float32

When calling the chat completions endpoint with tools, set "chat_template_kwargs": {"enable_thinking": true, "force_nonempty_content": true} in the request body so the server parses both reasoning and tool calls correctly. To serve the full 1M-token context, set VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 (vLLM) or SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1 (SGLang) and raise --max-model-len / --context-length to 1048576.

#### Verify the server

Each command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see nemotron-3-ultra listed in the response.

### Benchmarking results: Nemotron 3 Ultra

All results use the 8,192-in / 65,536-out workload at 256 concurrent requests (512 prompts). Latency is reported as Mean / P99 in milliseconds. Time-to-first-token is excluded because the saturated queue makes it reflect wait time rather than prefill latency.

SGLang
TensorRT-LLM
vLLM

Token throughput:

 | Metric
 | 4× NVIDIA Blackwell
 | NVIDIA HGX H100

 | Output gen (tok/s)
 | 2,363.12
 | 1,930.04

 | Per-user gen (tok/s/user)
 | 9.23
 | 7.54

 | Total (tok/s)
 | 2,658.52
 | 2,171.31

Latency (Mean / P99 in ms):

 | Metric
 | 4× NVIDIA Blackwell
 | NVIDIA HGX H100

 | TPOT
 | 76.51 / 94.81
 | 45.52 / 114.52

 | ITL
 | 76.51 / 179.12
 | 45.52 / 77.84

Token throughput:

 | Metric
 | 4× NVIDIA Blackwell

 | Output gen (tok/s)
 | 3,404.40

 | Per-user gen (tok/s/user)
 | 13.30

 | Total (tok/s)
 | 3,829.95

Latency (Mean / P99 in ms):

 | Metric
 | 4× NVIDIA Blackwell

 | TPOT
 | 14.36 / 48.77

 | ITL
 | 48.41 / 133.60

Provisional — the vLLM runs completed 450/512 requests on 4× Blackwell and 229/512 on the NVIDIA HGX H100, and its ITL counter returned inconsistent values (omitted below).

Token throughput:

 | Metric
 | 4× NVIDIA Blackwell
 | NVIDIA HGX H100

 | Output gen (tok/s)
 | 2,305.31
 | 978.94

 | Per-user gen (tok/s/user)
 | 9.01
 | 3.82

 | Total (tok/s)
 | 2,593.47
 | 1,101.32

Latency (Mean / P99 in ms):

 | Metric
 | 4× NVIDIA Blackwell
 | NVIDIA HGX H100

 | TPOT
 | 57.17 / 194.74
 | 20.52 / 112.56

## Next steps

To get started with Nemotron 3 Ultra, follow the directions above to deploy on Lambda's infrastructure powered by NVIDIA. View additional resources about the model below:

### Upstream

- Download Nemotron 3 Ultra NVFP4 on Hugging Face
- Download Nemotron 3 Ultra BF16 on Hugging Face
- Nemotron 3 Ultra Technical Report

### Downstream

Use as a Claude Code backend

Use your self-hosted Nemotron 3 Ultra instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the inference server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="nemotron-3-ultra"
export ANTHROPIC_DEFAULT_SONNET_MODEL="nemotron-3-ultra"
export ANTHROPIC_DEFAULT_OPUS_MODEL="nemotron-3-ultra"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="nemotron-3-ultra"

export ANTHROPIC_SMALL_FAST_MODEL="nemotron-3-ultra"
export ANTHROPIC_FAST_MODEL="nemotron-3-ultra"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
