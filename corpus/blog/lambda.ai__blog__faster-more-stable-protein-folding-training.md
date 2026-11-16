# TurboPairFormer: faster, more stable, more accurate OpenFold3 fine-tuning

Source: https://lambda.com/blog/faster-more-stable-protein-folding-training

Skip to main content

# TurboPairFormer: faster, more stable, more accurate OpenFold3 fine-tuning

 November 13, 2026

 • 5 min read

Lambda, Stevens Institute of Technology, and the OpenFold team built open-source GPU kernels that train OpenFold3 up to 1.73× faster, with more accurate and fully reproducible gradients.

Models like AlphaFold3 and OpenFold3 have changed how researchers study proteins, nucleic acids, and small molecules, and their interactions. Training and fine-tuning them is still expensive, and the cost climbs fast as molecular systems get bigger.

Much of that cost sits in one operation: triangle attention.

So researchers from Lambda, Stevens Institute of Technology, and the OpenFold team built TurboPairFormer, a high-performance implementation of triangle attention and triangle multiplication for biomolecular structure prediction models. It's open source and available on PyPI.

Three results stand out:

- Faster training: up to 1.73× faster than the original OpenFold3 Triton backend, with the lowest GPU computation time per optimizer step of eight backends tested on 16 NVIDIA H100 GPUs.

- More accurate gradients: the lowest mean query, key, and pair-bias gradient errors of eight attention implementations, plus 28–47% less error from output-residual compensation in controlled experiments.

- Reproducible runs: bitwise-identical gradients across repeated runs in all 600 fixed-input test cases.

## Why triangle attention is the bottleneck

Triangle attention helps a model reason about pairs of molecular components by routing information through a third one. That's how it captures the geometry needed to predict 3D structures.

It's also expensive. Standard attention scales quadratically with the number of tokens. Triangle attention scales cubically, so doubling the training crop size makes it about 8× more expensive.

Existing implementations, including NVIDIA® cuEquivariance™ as a part of the NVIDIA BioNeMo platform, ByteDance Protenix, and the OpenFold3 Triton backend, already speed this up. Each one still gives up something among speed, numerical precision, and reproducibility. TurboPairFormer was built to keep all three on NVIDIA Hopper™ GPUs.

## How TurboPairFormer works

TurboPairFormer pairs hardware-aware GPU optimizations with a redesigned attention computation. It uses three techniques that work together.

- 

It computes attention probabilities once in the backward pass. The backward pass, where gradients are calculated for queries, keys, values, and pair biases, is the most demanding part of triangle attention. Existing kernels often recompute attention probabilities several times, once for each gradient, adding redundant computation and overhead. TurboPairFormer recomputes each attention probability tile only once and uses that one result for all four gradients.

- 

It keeps what BF16 rounding loses, to improve accuracy. Existing kernels often mix FP32 and BF16 precision to balance speed and accuracy. Converting FP32 values to BF16 introduces rounding errors. TurboPairFormer saves that lost information. Its output-residual compensation captures the rounding residual when the forward-pass output is converted from FP32 to BF16, then uses it to make the backward-pass gradients more accurate. In controlled experiments, this cut mean gradient error by about 28–47%.

- 

It makes gradients deterministic to stabilize training. Kernels that accumulate gradients with floating-point atomic operations can return slightly different results on identical runs, because the order of operations changes from run to run. TurboPairFormer uses a fixed accumulation order, so gradients are bitwise identical every time, which supports more stable training.

## Benchmark results

We integrated TurboPairFormer into OpenFold3 and compared it with seven other backend configurations: ByteDance Protenix, NVIDIA cuEquivariance, TriFast, MegaFold, DeepSpeed-Evo, ScaleFold, and the original OpenFold3 Triton backend. Tests ran on 16 H100 GPUs across two nodes, at crop sizes of 384, 640, and 768 tokens.

TurboPairFormer had the lowest GPU computation time per optimizer step at every crop size.

## OpenFold3 training time on 16 H100 GPUs

 | GPU backend
 | Crop 384
 | Crop 640
 | Crop 768

 | TurboPairFormer
 | 5.26
 | 9.40
 | 12.58

 | ByteDance Protenix
 | 5.35
 | 9.62
 | 12.93

 | NVIDIA cuEquivariance
 | 5.60
 | 10.43
 | 14.25

 | TriFast
 | 5.39
 | 9.79
 | 13.18

 | MegaFold
 | 5.66
 | 11.42
 | 15.94

 | DeepSpeed-Evo
 | 5.78
 | 11.81
 | 16.63

 | ScaleFold
 | 5.96
 | 11.17
 | 15.71

 | OpenFold3 Triton
 | 6.37
 | 14.48
 | 21.72

GPU computation time in seconds per optimizer step. Lower is better. Measurements cover steps 21 to 200 and exclude data loading, host-to-device transfers, and EMA updates.

At crop 768, TurboPairFormer is 1.73× faster than OpenFold3 Triton, 1.13× faster than NVIDIA cuEquivariance, and 1.03× to 1.32× faster than the remaining five backends. The gap widens as crop size grows, which is where triangle attention gets most expensive. On NVIDIA H200 GPUs, TurboPairFormer trained 1.54× faster than OpenFold3 Triton at crop 768, cutting time per step from 22.53 to 14.67 seconds.

## Accuracy

We gave every kernel identical BF16 inputs and compared its gradients against a high-precision FP64 reference. TurboPairFormer had the lowest mean errors for query, key, and pair-bias gradients across the tested crop sizes and attention dimensions. Compared with NVIDIA cuEquivariance, it reduced mean gradient error by:

- 31.4–44.4% for query gradients

- 28.7–42.4% for key gradients

- 16.9–37.9% for pair-bias gradients

Value-gradient accuracy was essentially tied. That's expected: output-residual compensation improves the query, key, and pair-bias gradients and doesn't directly affect the value gradient.

## Reproducibility and stability

We also checked whether each kernel returns identical gradients for identical inputs. On a single NVIDIA H100 GPU, we ran 600 fixed-input cases five times each. We counted a case as reproducible only if all four gradients (queries, keys, values, and pair biases) matched bit for bit across all five runs. TurboPairFormer was reproducible in all 600.

Reproducible gradients help keep training stable. To test that, we resumed training from the same model checkpoint with each kernel, using identical random seeds and training examples on an NVIDIA H100 GPU. With TurboPairFormer, training loss stayed steady, with no significant fluctuations and no NaN values.

## What it means for drug discovery

Biomolecular structure prediction models support work like protein–ligand binding prediction, structure-guided drug design, and the study of disease-related protein families. Adapting them usually means fine-tuning on new experimental structures, specializing for a protein family, or repeatedly re-evaluating candidates. Every one of those runs costs compute.

Faster core operations let researchers run more experiments on the same GPUs and test more hypotheses in less time. And because TurboPairFormer targets building blocks shared across biomolecular structure prediction models, the gains carry over to a wide range of biomolecular AI applications.

## Get started

TurboPairFormer currently supports H100 and H200 GPUs.

- Install the package: pip install turbopairformer

- Set it up with the quickstart guide

- Read the paper for the full method and results

Authors: Yide Ran, Chelsea Lowman, Jan Domański, David Hartmann, Jenke Scheen, Jennifer Wei, Chuan Li, Jianwen Xie, Zhaozhuo Xu
Credits: Stevens Institute of Technology, Lambda, OpenFold Consortium at Open Molecular Software Foundation

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
