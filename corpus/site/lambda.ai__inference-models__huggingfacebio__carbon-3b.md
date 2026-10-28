# HuggingFaceBio/Carbon-3B

Source: https://lambda.ai/inference-models/huggingfacebio/carbon-3b

Skip to main content

# How to deploy Carbon on Lambda

## TL;DR: nucleotide throughput

Both Carbon-500M and Carbon-3B run on a single NVIDIA A10 GPU, served with SGLang or vLLM. Because Carbon tokenizes DNA as non-overlapping 6-mers, each token carries roughly 6 base pairs, so the token rates below correspond to roughly 6× as many base pairs per second.

### Carbon-500M

 | Backend
 | Output gen (tok/s)
 | Total (tok/s)
 | TTFT mean / p99 (ms)
 | ITL mean / p99 (ms)

 | SGLang
 | 1,241.5
 | 1,665.2
 | 638 / 1,172
 | 25.7 / 39.5

 | vLLM
 | 1,320.4
 | 1,771.1
 | 817 / 2,074
 | 24.1 / 35.9

1× NVIDIA A10 GPU, workload 2048 input / 6000 output tokens, 32 concurrent requests.

### Carbon-3B

 | Backend
 | Output gen (tok/s)
 | Total (tok/s)
 | TTFT mean / p99 (ms)
 | ITL mean / p99 (ms)

 | SGLang
 | 459.4
 | 574.2
 | 1,544 / 2,941
 | 23.6 / 28.8

 | vLLM
 | 437.9
 | 547.4
 | 1,131 / 3,082
 | 24.9 / 30.7

1× NVIDIA A10 GPU, workload 2048 input / 8192 output tokens, 12 concurrent requests.

### Benchmark command

The two sizes were benchmarked at different workloads (Carbon-500M at 6000 output tokens / 32 concurrent; Carbon-3B at 8192 output tokens / 12 concurrent), reflecting the longer generations and tighter memory budget of the larger model. Re-run the Carbon-3B benchmark:

vllm bench serve \
 --model HuggingFaceBio/Carbon-3B \
 --served-model-name Carbon-3B \
 --endpoint /v1/completions \
 --random-input-len 2048 --random-output-len 8192 \
 --num-prompts 256 --max-concurrency 12

("Tokens" here are 6-mer DNA tokens. Multiply by ~6 for base pairs per second.)

## Background

Carbon is a DNA language model: a Llama-style LLM whose vocabulary is a genetic sequence instead of English. It comes from HuggingFaceBio (Hugging Face, Zhongguancun Academy, and TIGEM / University of Naples "Federico II"). The family ships in three sizes, two of which are covered by this card: Carbon-500M and Carbon-3B (the flagship), with a larger Carbon-8B in the family. Because Carbon-3B ships as a stock LlamaForCausalLM, both covered sizes run in vLLM and SGLang with no custom serving code and fit on a single NVIDIA A10 GPU.

Carbon's value comes down to one tradeoff: resolution versus reach. Reading DNA one base at a time gives maximum precision but runs slow and expensive; grouping bases into chunks goes far faster but blurs the single-base detail that clinical variant tasks depend on. Carbon takes the fast path, tokenizing DNA as non-overlapping 6-mers (six bases per token). It then recovers the lost precision with a training objective called Factorized Nucleotide Supervision (FNS). FNS factorizes each 6-mer prediction into six per-position softmaxes over {A, C, G, T}, so the model generates at single-nucleotide granularity and exposes per-base likelihoods for variant scoring.

Underneath, Carbon-3B runs as a standard 30-layer Llama decoder (hidden size 3072, FFN 8448, 32 attention heads with 4 KV groups, SwiGLU, RMSNorm). Its tokenizer mixes two schemes: fixed 6-mer tokens for DNA plus the full Qwen3 BPE vocabulary for English, roughly 156k entries in all, which is why DNA must be wrapped in <dna>…</dna> and kept to uppercase ACGT. Native context runs to 32,768 tokens (≈ 197 kbp) and extends to 65,536 (≈ 393 kbp) with a YaRN factor=4. Pretraining used 1T 6-mer tokens (≈ 6T base pairs) on a staged Cross-Entropy then FNS objective, with the data mix shifted toward mRNA and prokaryotic sequences late in training.

On HuggingFaceBio's zero-shot evaluations, Carbon-3B matches the much larger Evo2-7B on sequence recovery, variant-effect prediction, and perturbation discrimination while running several times faster. The card reports >150× faster generation than the Evo2 family and >100,000 base pairs/sec on a single NVIDIA H100 GPU. Against GENERator-v2-3B, its same-size sibling, Carbon-3B wins every benchmarked task.

## Model specifications

- Author: HuggingFaceBio

- Architecture: Decoder-only Llama-style Transformer (GQA, SwiGLU, RMSNorm) with Factorised Nucleotide Supervision (FNS)

- Domain: DNA / genomic foundation model (nucleotide sequence)

- Tokenization: non-overlapping 6-mer DNA (~6 bp/token); shared 155,776-entry vocabulary (4,096 DNA 6-mers + DNA/metadata tags + Qwen3 BPE)

- License: Apache 2.0

The two sizes share the same architecture, tokenizer, and DNA template, differing only in scale and native context:

 | Specification
 | Carbon-3B (flagship)
 | Carbon-500M

 | Parameters
 | 3B
 | ~500M

 | Layers
 | 30
 | 28

 | Hidden size
 | 3072
 | 1024

 | FFN size
 | 8448
 | 3072

 | Attention
 | 32 heads, 4 KV groups (GQA)
 | 16 heads (GQA)

 | Context window
 | 32,768 tokens (≈ 197 kbp); 65,536 (≈ 393 kbp) with YaRN factor=4
 | 8,192 tokens (≈ 49 kbp)

Carbon-500M is useful both as a standalone genomic model on minimal hardware and as a draft model for speculative decoding on Carbon-3B / Carbon-8B (they share a tokenizer and DNA template).

## Hardware requirements

Both Carbon sizes fit comfortably on a single NVIDIA A10 GPU (23 GB) in BF16

- Carbon-500M: 1× NVIDIA A10 GPU

- Carbon-3B: 1× NVIDIA A10 GPU

## Deployment and benchmarking

### Deploying Carbon

Both sizes can be served with SGLang or vLLM on a single NVIDIA A10 GPU. The commands below deploy the flagship Carbon-3B; to serve Carbon-500M instead, swap the model path and served name (and, for SGLang, drop --attention-backend triton and raise --mem-fraction-static to 0.9)

Note on images: The container tags below are nightly / development builds pinned to specific commits, used because Carbon support was still landing in the released backends at benchmark time. Substitute a stable release tag once one ships with Carbon support.

- Launch an instance with 1× NVIDIA A10 GPU from the Lambda Cloud Console using the GPU Base 24.04 image.

- Connect to your instance via SSH or the JupyterLab terminal. See Connecting to an instance for detailed instructions.

- Start the inference server using either SGLang or vLLM:

 SGLang
 vLLM

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 lmsysorg/sglang:nightly-dev-cu12-20260529-a8cfae0b \
 python3 -m sglang.launch_server \
 --model-path HuggingFaceBio/Carbon-3B \
 --served-model-name Carbon-3B \
 --tp 1 \
 --host 0.0.0.0 --port 8000 \
 --trust-remote-code \
 --mem-fraction-static 0.85 \
 --attention-backend triton

docker run -d --gpus all \
 --ipc=host -p 8000:8000 \
 -v ~/.cache/huggingface:/root/.cache/huggingface \
 vllm/vllm-openai:nightly-22a58640b4563f5945aa2052e9e61d425351588d \
 --model HuggingFaceBio/Carbon-3B \
 --served-model-name Carbon-3B \
 --tensor-parallel-size 1 \
 --host 0.0.0.0 --port 8000 \
 --max-model-len auto \
 --trust-remote-code \
 --gpu-memory-utilization 0.9

Notable flags:

- --trust-remote-code is required for both sizes as Carbon's base-pair-level generation/scoring lives in a custom fns modeling branch loaded from the model repo.

- --attention-backend triton (Carbon-3B SGLang) selects the Triton attention kernel, which is the reliable path for Carbon-3B on the NVIDIA A10 GPU.

- --mem-fraction-static is set slightly lower for Carbon-3B (0.85 vs 0.9) to leave headroom for the larger weights on a single A10.

#### Verify the server

Either command launches an inference server with an OpenAI-compatible API on port 8000. Verify it:

curl -X GET http://localhost:8000/v1/models \
 -H "Content-Type: application/json"

You should see Carbon-3B (or Carbon-500M) listed in the response.

### Benchmarking results: Carbon

The two sizes were benchmarked at different workloads. Carbon-500M: 2048 input / 6000 output tokens, 32 concurrent requests. Carbon-3B: 2048 input / 8192 output tokens, 12 concurrent requests. All on a single NVIDIA A10 GPU.

#### Carbon-500M

Token throughput:

 | Metric
 | SGLang
 | vLLM

 | Output gen (tok/s)
 | 1,241.5
 | 1,320.4

 | Total (tok/s)
 | 1,665.2
 | 1,771.1

Latency (Mean / P99 in ms):

 | Metric
 | SGLang
 | vLLM

 | TTFT
 | 638 / 1,172
 | 817 / 2,074

 | TPOT
 | 25.7 / 26.1
 | 24.1 / 24.2

 | ITL
 | 25.7 / 39.5
 | 24.1 / 35.9

#### Carbon-3B

Token throughput:

 | Metric
 | SGLang
 | vLLM

 | Output gen (tok/s)
 | 459.4
 | 437.9

 | Total (tok/s)
 | 574.2
 | 547.4

Latency (Mean / P99 in ms):

 | Metric
 | SGLang
 | vLLM

 | TTFT
 | 1,544 / 2,941
 | 1,131 / 3,082

 | TPOT
 | 23.6 / 24.2
 | 24.9 / 25.7

 | ITL
 | 23.6 / 28.8
 | 24.9 / 30.7

## Next steps

### Upstream

- Download Carbon-3B on Hugging Face

- Download Carbon-500M on Hugging Face

### Downstream: genomics workflows

Because Carbon exposes per-base likelihoods and operates at single-nucleotide resolution via FNS, your self-hosted endpoint can drive standard genomic foundation-model tasks:

- Sequence embeddings. Encode DNA/RNA sequences (wrapped in <dna>…</dna>, uppercase ACGT) into hidden-state representations for downstream classifiers and clustering. The generation server above does not expose /v1/embeddings — start a separate instance in pooling mode (vLLM: add --runner pooling; SGLang: add --is-embedding), then call /v1/embeddings with the same <dna>…</dna> formatting.

- Variant-effect prediction (VEP). Score a variant by comparing the model's per-base likelihoods for the reference vs. alternate sequence. Carbon's 6-mer logits factorize exactly into per-position {A, T, C, G} distributions (the FNS objective), so you can recover single-base resolution straight from a standard vLLM server: launch it with --max-logprobs 4096 to cover the DNA vocabulary, request prompt_logprobs, then marginalize each 6-mer distribution to per-base client-side. The score_sequence method on the fns branch (Carbon-*-remote) is a drop-in reference for that marginalization. Carbon-3B is competitive with Evo2-7B on BRCA2, ClinVar coding/non-coding, and TraitGym Mendelian.

- DNA generation. Generate biologically plausible sequences, with optional metadata conditioning on species type and gene-region type (e.g. <vertebrate_mammalian><protein_coding_region><dna>…). Temperature, top-p, exact base counts, and per-position masking all operate at nucleotide granularity on the model's fns branch.

- Long-context retrieval. Run Genomic needle-in-a-haystack tasks out to 393 kbp by enabling the YaRN factor=4 extension.

- Speculative decoding. Pair Carbon-500M as a draft model with Carbon-3B (or Carbon-8B) for lossless generation speedups, since they share a tokenizer and DNA template.

Tokenizer caution: Always wrap DNA in <dna>…</dna> — without the tag the input is silently routed through the English BPE vocabulary and performance collapses. Non-ACGT characters map to <oov>, and sequence lengths that are not a multiple of 6 are right-padded with A.

## Ready to get started?

Create your Lambda Cloud account and launch NVIDIA GPU instances in minutes. Looking for long-term capacity? Talk to our team.
Launch GPU instance
