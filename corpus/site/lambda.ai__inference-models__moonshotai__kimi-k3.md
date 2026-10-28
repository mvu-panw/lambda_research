# moonshotai/Kimi-K3

Source: https://lambda.ai/inference-models/moonshotai/kimi-k3

Skip to main content

# How to deploy Kimi K3 on Lambda

## TL;DR: token throughput

Measured on 2x NVIDIA HGX B200 connected through Infiniband, CUDA 13.0. 8192 in / 2048 out tokens, 32 concurrent requests, 512 prompts, served at TP=8 within each node plus PP=2 spanning the pair on the official MXFP4 checkpoint.

### vLLM

 | Hardware
 | Gen. throughput
 | Per-user gen.
 | Total throughput
 | TTFT (mean)
 | ITL (mean)

 | 2× NVIDIA HGX B200
 | 298.33 tok/s
 | 9.32 tok/s
 | 1,491.65 tok/s
 | 9,425.53 ms
 | 102.61 ms

### Benchmark command

(8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests, the workload recorded for the benchmark run.)

The benchmark uses a 4:1 input-to-output token ratio (8192 in / 2048 out per request) to simulate long-context coding and document-analysis workflows.

Benchmark configuration:

vllm bench serve \
 --backend openai \
 --base-url http://kimi-k3:8000 \
 --endpoint /v1/completions \
 --model kimi-k3 \
 --tokenizer /models/Kimi-K3 \
 --trust-remote-code \
 --dataset-name random \
 --input-len 8192 \
 --output-len 2048 \
 --num-prompts 512 \
 --max-concurrency 32

See Benchmarking Kimi K3 below for the full results.

## Background

Moonshot AI bills Kimi K3, its flagship open-weight release, as the first openly released model in the "3-trillion-parameter class." Model is ~2.8 trillion total parameters at ~104 billion activated per token, and it pairs a native vision encoder with a 1-million-token context window. Its predecessor, Kimi K2, ran a conventional dense-attention MoE. K3 rebuilds that backbone around linear-cost attention and extreme MoE sparsity.

A 3:1 hybrid drives the attention stack: Kimi Delta Attention (KDA), a linear-attention layer with a recurrent gated memory, plus Gated Multi-head Latent Attention (MLA), which keeps million-token context affordable. The feed-forward path runs a Stable LatentMoE of 896 routed experts (16 active per token plus 2 shared) in a compressed latent width, steered by auxiliary-loss-free Quantile Balancing. Weights ship in a native MXFP4 build with MXFP8 activations, trained with quantization-aware training, and a from-scratch MoonViT-V2 vision encoder makes the model multimodal. Moonshot reports roughly 2.5× better scaling efficiency over Kimi K2.

## Model specifications

### Overview

- Name: Kimi K3

- Author: Moonshot AI

- Architecture: Sparse Mixture-of-Experts (MoE), multimodal, hybrid attention, decoder-only

- License: Kimi K3 License (custom, MIT-style with a Model-as-a-Service clause)

### Specifications

- Total parameters: ~2.8T (~104B active per token)

- Experts: 896 routed experts, top-16 per token, plus 2 shared experts

- Decoder blocks: 93 (1 dense)

- Attention: 96 heads; 69 KDA (linear) plus 24 Gated MLA (global) blocks, ~3:1

- Quantization: MXFP4 weights / MXFP8 activations (quantization-aware training)

- Context window: 1,048,576 tokens (~1.05M)

- Modalities: Text and images/video via MoonViT-V2 (served text-only in this deployment)

## Hardware requirements

For the benchmarked Kimi K3 MXFP4 deployment, the ~1.56 TB checkpoint (96 shards) must be served as a single replica across all 16 GPUs in one compute cluster (for low latency). Kimi K3 advertises a context window of approximately 1.05M tokens.

### Checkpoint options

- MXFP4: moonshotai/Kimi-K3, benchmarked in this card on the hardware above (native MXFP4 weights / MXFP8 activations).

## Deployment and benchmarking

### Deploying Kimi K3

This multi-node Kubernetes deployment serves Kimi K3's ~1.56 TB MXFP4 checkpoint as one replica across all 16 GPUs.TP=8 within each node and PP=2 bridging the two (native vLLM multi-node, without Ray or LWS). 

Prerequisites

- Two GPU nodes in one cluster with fast node-to-node RDMA (InfiniBand or RoCE).

- NVIDIA GPU Operator and Network Operator installed (GPU node labels + an RDMA device plugin).

- A ReadWriteMany storage class with ~1.9 TB free for the checkpoint.

- The pre-release image vllm/vllm-openai:kimi-k3 (min vLLM 0.27.0), and kubectl pointed at the cluster.

- Get the manifests:

git clone https://github.com/LambdaLabsML/lambda-inference-model-recipes.git
cd lambda-inference-model-recipes/moonshotai/Kimi-K3

- Adapt the defaults to your cluster (they match Lambda's fabric):

- In manifests/10-model-cache.yaml, set storageClassName to your RWX class.

- In manifests/30-vllm-serve.yaml, set the nvidia.com/gpu.product node selector, the rdma/… device-plugin resource name, and NCCL_IB_HCA (your fast IB rails).

- Apply in order; the server's init container waits for the download to verify all 96 shards before starting:

kubectl apply -f manifests/00-namespace.yaml
kubectl apply -f manifests/10-model-cache.yaml # ~1.9 TB RWX PVC
kubectl apply -f manifests/20-model-download.yaml # downloads + verifies 96 shards
kubectl apply -f manifests/30-vllm-serve.yaml # 2-pod StatefulSet + headless + API Service
kubectl -n kimi-k3 rollout status statefulset/kimi-k3 --timeout=60m

Each pod runs the vLLM server below, where rank-0 serves the OpenAI API and rank-1 runs as a --headless worker. That server is already baked into 30-vllm-serve.yaml and shown here only for reference. On plain B200 the off-NVLink recipe flags are required, or the group deadlocks on the first cross-node collective:

vllm serve /models/Kimi-K3 \
 --served-model-name kimi-k3 --trust-remote-code --language-model-only \
 --tensor-parallel-size 8 --pipeline-parallel-size 2 \
 --nnodes 2 --node-rank $RANK --master-addr $MASTER --master-port 29501 \
 --moe-backend flashinfer_trtllm --disable-custom-all-reduce \
 --kv-cache-dtype fp8 --enable-prefix-caching \
 --max-model-len 49152 --distributed-timeout-seconds 3600 \
 --host 0.0.0.0 --port 8000
# required env: VLLM_USE_V2_MODEL_RUNNER=0 VLLM_ALLREDUCE_USE_FLASHINFER=0 VLLM_ENABLE_K3_LATENT_MOE_TAIL_FUSION=0

- Verify the server (rank-0 exposes an OpenAI-compatible API on port 8000):

kubectl -n kimi-k3 port-forward svc/kimi-k3 8000:8000 &
curl -s http://localhost:8000/v1/models

You should see kimi-k3 listed in the response.

### Benchmarking Kimi K3

Workload: 8192 input / 2048 output tokens, 512 prompts, 32 concurrent requests, on 2× NVIDIA HGX B200 (TP=8, PP=2).

#### vLLM

2× NVIDIA HGX B200

Latency (Mean / P99 in ms):

 | Metric
 | Mean
 | P99

 | Time to first token
 | 9,425.53 ms
 | 79,957.65 ms

 | Time per output token
 | 102.66 ms
 | 140.70 ms

 | Inter-token latency
 | 102.61 ms
 | 1,352.76 ms

## Next steps

### Upstream

- Download Kimi K3 weights on Hugging Face

- Read the Moonshot AI Kimi K3 announcement

### Downstream

Use as a noumena code backend

Use your self-hosted Kimi K3 as the backend to noumena's code framework rather than their hosted models for local development. Replace <NODE_IP> with the IP of the node where the server is running.

git clone https://github.com/noumena-network/code.git
cd code
bun install
bun run build

OPENAI_API_KEY="dummy" \
OPENAI_BASE_URL="http://<NODE_IP>:8000/v1" \
OPENAI_MODEL="kimi-k3" \
./.tmp/packages/ncode-0.1.0-linux-x64/ncode \
 --print \
 --model kimi-k3 \
 --max-turns 1 \
 "Reply exactly: ok"

Use as a Claude Code backend

Use your self-hosted Kimi K3 instead of Anthropic's API for local development. Replace <NODE_IP> with the IP of the node where the server is running:

export ANTHROPIC_BASE_URL="http://<NODE_IP>:8000"
export ANTHROPIC_API_KEY="dummy"

export ANTHROPIC_MODEL="kimi-k3"
export ANTHROPIC_DEFAULT_SONNET_MODEL="kimi-k3"
export ANTHROPIC_DEFAULT_OPUS_MODEL="kimi-k3"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="kimi-k3"

export DISABLE_TELEMETRY=1
export ENABLE_PROMPT_CACHING_1H=1

claude

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
