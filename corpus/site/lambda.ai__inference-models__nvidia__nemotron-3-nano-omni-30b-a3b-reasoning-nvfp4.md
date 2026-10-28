# nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4

Source: https://lambda.ai/inference-models/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning-nvfp4

Skip to main content

# How to deploy NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning NVFP4 on Lambda

## Performance

NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning NVFP4

1× NVIDIA B200 GPU or 1× NVIDIA H100 GPU · vLLM TP1

12,479 output tok/s maximum throughput on B200

762 tok/s/user at interactive latency on B200

C32 — Pareto-optimal balanceC16 — Pareto-optimal balance

### Benchmark summary

 | Hardware
 | Concurrency
 | Output tok/s
 | TPS/user
 | TTFT p50/p99 (ms)
 | ITL p50/p99 (ms)

 | 1× B200
 | C1
 | 450.4
 | 761.6
 | 85 / 105
 | 2.1 / 2.1

 | 1× B200
 | C16
 | 3,727.1
 | 382.0
 | 406 / 757
 | 3.8 / 5.5

 | 1× B200
 | C64
 | 8,008.1
 | 186.6
 | 870 / 2,583
 | 7.0 / 8.0

 | 1× B200
 | C256
 | 12,478.5
 | 78.9
 | 5,283 / 10,544
 | 15.1 / 19.5

 | 1× H100
 | C1
 | 316.6
 | 428.8
 | 190 / 194
 | 3.0 / 3.0

 | 1× H100
 | C16
 | 1,767.7
 | 170.1
 | 1,702 / 2,636
 | 7.2 / 9.6

 | 1× H100
 | C64
 | 3,039.1
 | 60.7
 | 1,919 / 9,872
 | 18.8 / 20.7

 | 1× H100
 | C256
 | 3,993.1
 | 23.5
 | 2,631 / 40,937
 | 57.3 / 62.9

Methodology

Measured on 1× NVIDIA B200 GPU and 1× NVIDIA H100 GPU with vLLM, tensor parallel size 1 (TP1), using the official nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 checkpoint (text-generation path; vision/audio encoders were not exercised by this text-only synthetic workload). The workload used approximately 8,192 input tokens and 1,024 output tokens per request, 512 prompts per concurrency point, and concurrency swept from 1 to 256 (labels C1–C256). Both lanes use one GPU, so system and per-GPU output throughput are identical. NVIDIA's comparative-benchmark contract applied no documented B200- or H100-specific server-argument overrides for this model — the same launch flags were used on both GPUs — but NVIDIA Hopper lacks native FP4 tensor cores, so the H100 lane necessarily executes the NVFP4 checkpoint through a dequantization fallback path rather than native 4-bit math.

## Background

NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning is a natively multimodal member of the Nemotron-3-Nano family, combining a Mamba2-Transformer hybrid Mixture-of-Experts (MoE) language backbone with two purpose-built encoders: CRADIO v4-H for vision and Parakeet (parakeet-tdt-0.6b-v2) for audio. It accepts video, audio, image, and text input and produces text output only. The "Reasoning" variant is post-trained for extended chain-of-thought.

Per NVIDIA's model card, the backbone totals approximately 31 billion parameters with roughly 3 billion active per token, and the model supports a context window of up to 256,000 tokens. NVIDIA publishes three quantization variants — BF16 (62 GB), FP8 (33 GB), and NVFP4 (~21 GB) — and reports that the quantized variants stay within roughly one point of the BF16 baseline across tested benchmarks. This card covers the official NVFP4 checkpoint.

## Model specifications

### Overview

- Name: NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning (NVFP4)

- Author: NVIDIA

- Architecture: Mamba2-Transformer hybrid Mixture-of-Experts, with a CRADIO v4-H vision encoder and a Parakeet audio encoder

- License: NVIDIA Open Model License Agreement

### Specifications

- Total parameters: 31B total (3B active per token)

- Context window: up to 256,000 tokens

- Modality: Natively multimodal — video, audio, image, and text input; text-only output

- Precision: Native NVFP4 — official nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 checkpoint, ~21 GB on disk

## Hardware requirements

- Minimal deployment:

- 1× NVIDIA Blackwell GPU (e.g. 1× NVIDIA B200 GPU) for the NVFP4 checkpoint. The same checkpoint also runs on 1× NVIDIA H100 GPU via a non-native FP4 execution path (Hopper has no native FP4 tensor cores).

## Deployment and benchmarking

### Deploying NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning (NVFP4)

NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning (NVFP4) was benchmarked on a single NVIDIA Blackwell or NVIDIA Hopper GPU with vLLM, tensor-parallel size 1, text-only chat completions (--language-model-only-style path; the vision/audio encoders were not exercised).

- Launch an instance with 1× NVIDIA B200 GPU (or 1× NVIDIA H100 GPU) from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server:

docker run --gpus all -p 8000:8000 --ipc=host \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:v0.20.0 \
 --model nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4 \
 --served-model-name nvidia/nemotron-3-nano-omni \
 --tensor-parallel-size 1 \
 --max-model-len 16384 \
 --gpu-memory-utilization 0.90 \
 --trust-remote-code

### Verify the server

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see nvidia/nemotron-3-nano-omni listed in the response.

### Benchmarking

Results are in the benchmark summary table above. Both GPU lanes were driven with AIPerf (NVIDIA Dynamo AIPerf 0.12.0) at approximately 8,192 input / 1,024 output tokens, 512 requests per concurrency point, swept across nine concurrency levels (1–256).

## Next steps

### Upstream

- Download NVIDIA Nemotron-3-Nano-Omni-30B-A3B-Reasoning NVFP4 on Hugging Face

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
