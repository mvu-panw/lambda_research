# How FlashAttention-2 Accelerates LLMs on NVIDIA H100 and A100 GPUs

Source: https://lambda.ai/blog/flashattention-2-lambda-cloud-h100-vs-a100

Skip to main content

# How FlashAttention-2 Accelerates LLMs on NVIDIA H100 and A100 GPUs

 August 24, 2023

 (Updated on November 22, 2023)

 • 8 min read

This blog post walks you through how to use FlashAttention-2 on Lambda Cloud and outlines NVIDIA H100 vs NVIDIA A100 benchmark results for training GPT-3-style models. For more deep learning benchmarks, demos, and examples from Lambda, check out this GitHub repository.

## Table of Contents

- Introduction

- Highlights

- NVIDIA H100 vs A100 Benchmarking

- NVIDIA H100 vs A100 Results

- Acknowledgements

## Introduction

FlashAttention, the game-changing algorithm designed to accelerate attention modules and minimize memory usage without any approximation, took the world by storm after its release in 2022. It quickly found its way into machine learning frameworks and became a staple in industry-standard benchmarks, leaving a trail of awe-inspiring results in its wake.

Now, brace yourself for the next level of innovation as FlashAttention-2 has been released! Building upon its predecessor's success, FlashAttention-2 delivers an astounding 2x speedup, achieved through improved parallelism and work partitioning. In this blog post, we'll show you how to use FlashAttention-2 on Lambda Cloud and share benchmark results for training GPT-3-style models using NVIDIA A100 and H100 Tensor Core GPUs.

## Highlights

The key findings from our analysis are:

- FlashAttention-2 achieved 3x or higher speedups over the baseline Hugging Face implementation.

- NVIDIA H100 80GB SXM5 is 2x faster than NVIDIA A100 80GB SXM4 when running FlashAttention-2 training.

More details can be found in footnote [1]

Here is a chart that shows the speedup you can get from FlashAttention-2 using different GPUs (NVIDIA A100 and NVIDIA H100):

To give you a taste of its real-world impact, FlashAttention-2 enables replicating GPT3-175B training with "just" 242,400 GPU hours (H100 80GB SXM5). On Lambda Cloud, this translates to $458,136 using the three-year reserved cluster ($1.89/H100/Hour). This reduction represents a remarkable 90% cost savings compared to our earlier blog's $4,600,000 estimation.

Without further ado, let's dive into the details of the benchmark and results.

## NVIDIA H100 vs A100 Benchmarking

The FlashAttention repo has provided a Dockerfile that contains the latest FlashAttention-2. Our fork of the repo contains configuration to train GPT-3-style models with the OpenWebText dataset.

git clone https://github.com/LambdaLabsML/flash-attention.git && \
cd flash-attention && \
docker build -t flash-attention:latest ./training

Now you can launch the data preparation script and the benchmark script from the flash-attention folder:

# Prepare openwebtext dataset

docker run --gpus all --shm-size=1024g \
-v ${PWD}:/workspace \
flash-attention:latest \
sh -c 'cd /workspace/training && export PYTHONPATH=$PWD:$PYTHONPATH && pytest -q -s tests/datamodules/test_language_modeling_hf.py -k "openwebtext"'

# Train GPT-3
# Change trainer.devices so it matches the number of GPUs on your machine

docker run --gpus all --shm-size=1024g \
-v ${PWD}:/workspace \
flash-attention:latest \
sh -c 'cd /workspace/training && export PYTHONPATH=$PWD:$PYTHONPATH && python run.py experiment=owt/gpt3-2.7B-flash trainer.devices=8'

There are multiple configurations in the experiment folder. The rest of the blog will focus on the GPT3-2.7B configuration.

## NVIDIA H100 vs A100 Results

Let's begin by comparing the training speed of the baseline implementation and the FlashAttention-2 implementation. The table below shows that the FlashAttention-2 implementation achieved 3x or higher Tokens/Sec, which is calculated as Iter/Sec x max_length x batch_size. Additionally, FlashAttention-2 optimizes memory usage, enabling an increase in affordable batch_size from 1 to 4. In our benchmark, we set headdim to 80 for the FlashAttention-2 implementation. While setting  headdim to 128 (calculated as n_embd divided by n_head) may yield slightly improved performance, the exact difference varies depending on the model.

### Table 1: FlashAttention-2 on NVIDIA A100 & NVIDIA H100 GPUs

 | Configs
 | Iter / Sec
 | Tokens / Sec
 | BS / GPU
 | Memory / GPU (GB)
 | Time to 300B Tokens GPT3-2.7B (Days)
 | Extrapolated Time to 300B Tokens GPT3-175B (Days)

 | A100 80GB SXM4 Baseline
 | 3.63
 | 3,717
 | 1
 | 73
 | 934
 | 60,544

 | A100 80GB SXM4 FA2
 | 2.6
 | 10,650
 | 4
 | 73
 | 326
 | 21,132

 | H100 80GB SXM5 Baseline
 | 6.12
 | 6,267
 | 1
 | 73
 | 555
 | 10,100

 | H100 80GB SXM5 FA2
 | 5.44
 | 22,282
 | 4
 | 73
 | 156
 | 35911

It is nice to see that H100 80GB SXM5 produces more than 2x Tokens/Sec compared to A100 80GB SXM4 (22282.24 v.s. 10649.6), and that both GPUs scaled very well from 1x to 8x GPUs (96% and 98% scaling efficiency for A100 and H100 respectively, as shown in the table below).

### Table 2: Scaling FlashAttention-2 on 8x NVIDIA A100 & 8x NVIDIA H100 GPUs

 | Configs
 | Iter / Sec
 | Tokens / Sec
 | BS / GPU
 | Memory / GPU (GB)
 | Time to 300B Tokens GPT3-2.7B (Days)
 | Extrapolated Time to 300B Tokens GPT3-175B (Days)

 | A100 80GB SXM4 FA2
 | 2.6
 | 10,650
 | 4
 | 73
 | 326
 | 21,132

 | H100 80GB SXM5 FA2
 | 5.44
 | 22,282
 | 4
 | 73
 | 156
 | 10,100

 | 8xA100 80GB SXM4 FA2
 | 2.5
 | 81,920
 | 4
 | 56
 | 42
 | 2,747

 | 8xH100 80GB SXM5 FA2
 | 5.34
 | 174,981
 | 4
 | 56
 | 20
 | 1,286

Last but not least, we estimated the time to solution (process 300 billion tokens) for the GPT3-175B model by linearly scaling the time to solution of the GPT-3 2.7B model by 65 folds (175/2.7). The result suggests that with FlashAttention-2, one can expect to reproduce GPT3-175B training in just about 10 days with 1,024 H100 80GB SXM5 GPUs. On Lambda Cloud, this translates to $458,136 using the three-year reserved cluster ($1.89/H100/Hour). This reduction represents a remarkable 90% cost savings compared to our earlier blog's estimated cost of $4,600,000.

## Acknowledgements

We thank Tri Dao (the first author of FlashAttention) for valuable feedback on our benchmark results.

1. Our systems use 8x NVIDIA A100 80GB SXM4 and 8x NVIDIA H100 80GB SXM5 GPUs, with 1800GB system RAM and over 200 vCPUs. The benchmark measures the training throughput (tokens/s) using the gpt3-2.7B model and the OpenWebText dataset. The batch size per GPU is set to 4 for the FlashAttention-2 implementation and 1 for the baseline implementation (due to less optimized memory usage). The max sequence length is set to 1024, and the training uses half-precision.

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
