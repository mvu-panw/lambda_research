# How to serve Kimi-K2-Instruct on Lambda with vLLM

Source: https://lambda.ai/blog/how-to-serve-kimi-k2-instruct-on-lambda-with-vllm

Skip to main content

# How to serve Kimi-K2-Instruct on Lambda with vLLM

 December 22, 2025

 (Updated on January 17, 2026)

 • 4 min read

When your model doesn’t fit on a single GPU, you suddenly need to target multiple GPUs on a single machine, configure a serving stack that actually uses all that hardware, and know whether your setup is efficient enough for production.

One such case is Kimi K2 by Moonshot AI. It’s a one-trillion-parameter Mixture-of-Experts (MoE) regression language model capable of very strong coding, writing, and reasoning tasks. Due to its large memory requirements, running it at home is exceedingly difficult and impractical for the average user, as it requires more than a terabyte. Instead of waiting for local hardware to catch up, you can run it today on an 8× NVIDIA Blackwell GPU instance on Lambda using vLLM.

In this post, you’ll learn how to deploy Kimi-K2-Instruct on Lambda using vLLM for efficient multi‑GPU inference in four steps:

- Spin up an 8× NVIDIA Blackwell GPU instance on Lambda

- Start a vLLM deployment server with a single setup block

- Run a reproducible benchmark against that server

- Share the exact model and image references so you can reproduce this setup

1. Model snapshot (on Hugging Face)

- Model name: Kimi-K2-Instruct

- Author: moonshotai

- Primary capabilities: High-capacity MoE LLM optimized for fast reasoning, long-context understanding, and robust coding and tool-use performance.

- License: MIT ⚖️

2. Stats that matter

- Context window: 128K

- Weights-on-disk: 959GB

- Idle vRAM usage: 1,347GB

- Recommended Lambda VRAM configuration:

- 8x Blackwell GPUs (on-demand or 1-Click-Cluster)

- 16x NVIDIA H100 GPUs (1-Click-Cluster)

3. Get it running (one copy-paste block)

Device information:

- 8xOn-Demand B200's

- Base image: Lambda Stack 22.04

pip install vllm
VLLM_SERVER_DEV_MODE=1 vllm serve moonshotai/Kimi-K2-Instruct \
 --port 8000 \
 --served-model-name kimi-k2 \
 --trust-remote-code \
 --tensor-parallel-size 8 \
 --enable-auto-tool-choice \
 --tool-call-parser kimi_k2 \
 --enable-sleep-mode

This will now expose a vLLM server from your node that you can access and send requests to. Most importantly, this is how we can benchmark our server to measure and gather critical information like time-to-first-token, throughput, and more.

4. Benchmark capsule

For benchmarking, we’ll utilize the vllm bench serve command and measure across five complete spin-downs to avoid caching — after the GPUs have warmed up.

wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json

vllm bench serve \
 --backend vllm \
 --model moonshotai/Kimi-K2-Instruct \
 --served-model-name kimi-k2 \
 --dataset-name sharegpt \
 --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
 --num-prompts 10 \
 --trust-remote-code \
 --backend openai-chat \
 --endpoint /v1/chat/completions

To "reset" the state each time, we activate sleep mode, which opens up endpoints to /sleep?level=1 and /wake_up?tags=weights as POST endpoints on your server. E.g., curl -X POST 'http://localhost:8000/sleep?level=1'. Level 1 will ensure that weights are offloaded to CPU RAM and the KV cache is discarded.

Token throughput:

 |  
 | Tokens per second

 | Output generation
 | 219.644 ± 0.497

 | Total (Input & Output)
 | 332.358 ± 0.810

Fine-grained numbers:

 |  
 | Mean (ms)
 | P99 (ms)

 | Time to First Token
 | 148.986 ± 6.619
 | 173.242 ± 14.551

 | Time per Output Token
 | 17.576 ± 0.070
 | 19.712 ± 0.139

 | Inter-token Latency
 | 16.294 ± 0.059
 | 20.140 ± 0.218

## Conclusion

You now have everything you need to deploy Kimi-K2-Instruct on a single Lambda 8× HGX B200 instance with vLLM. This same pattern applies to other large open models that no longer fit on a single GPU: get the right Lambda instance, run the vLLM server, then run a benchmark you can trust.

If you have questions or want to share your benchmark results, reach out to Zach at zach.mueller@lambda.ai.

## References

- Weights: https://huggingface.co/moonshotai/Kimi-K2-Instruct

- Docker image: GPU Base 24.04 on the Lambda platform

## AUTHORED BY

 Zach Mueller

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
