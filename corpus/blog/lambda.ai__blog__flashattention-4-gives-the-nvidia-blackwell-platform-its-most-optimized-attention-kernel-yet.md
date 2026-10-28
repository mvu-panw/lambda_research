# FlashAttention-4 gives the NVIDIA Blackwell platform its most optimized attention kernel yet

Source: https://lambda.ai/blog/flashattention-4-gives-the-nvidia-blackwell-platform-its-most-optimized-attention-kernel-yet

Skip to main content

# FlashAttention-4 gives the NVIDIA Blackwell platform its most optimized attention kernel yet

 April 27, 2026

 (Updated on October 22, 2026)

 • 5 min read

On March 5, 2026, the much-anticipated paper for FlashAttention-4 (FA4) was published. The code was dropped on GitHub months ago; early benchmarks circulated, and preliminary results were presented at Hot Chips in August 2025. Now we have the complete technical write-up, the full benchmark methodology, and the rigorous backward-pass results to go with it. FA4 is the best open-source attention kernel, running on the most powerful GPU hardware we have.

## Attention optimization is the backbone of every ML workload

Every transformer-based model, LLM, diffusion model, and multimodal system runs attention at its core. Attention is also the most computationally expensive part of the forward and backward pass, scaling quadratically with sequence length. Optimizing it, then, is critical to every meaningful infrastructure decision in AI: training speed, inference throughput, serving cost, and sequence lengths at scale all depend on attention.
Installation of FlashAttention-4 is as simple as running the following on your GPU:

pip install flash-attn-4

## 
Why Blackwell required a new implementation

We are fortunate to be in an age where AI advances so rapidly that software is struggling to keep up with the latest chip updates.

FA3 was built with NVIDIA Hopper GPUs in mind, reaching roughly 740 TFLOPs/s at 75% utilization. NVIDIA Blackwell architectural advancements changed the underlying execution model significantly. NVIDIA’s Tensor Core (Dense) throughput more than doubled from approximately 1 PFLOPS to 2.25 PFLOPS for FP16/BF16, and the hardware introduced new tensor core instructions (TCGEN05), a new memory space called Tensor Memory for tensor core intermediates, and a fully asynchronous MMA execution model.

The challenge this created is what the paper calls asymmetric hardware scaling. In other words, the attention mechanism software needed to adapt to take advantage of the performance capabilities available on the GPUs. 

## What FA4 does differently

FA4 introduces three techniques that together unlock Blackwell's full capability for attention workloads.

- Redesigned async pipeline: Blackwell's MMA operations are fully asynchronous, so a warp can issue a matmul and immediately move on. FA4 builds a pipeline around this using warp specialization: orchestration warps manage async loads and matmul scheduling, while compute warps handle softmax in parallel. One tile's matrix multiplications overlap with the adjacent tile's softmax, keeping both tensor cores and SFUs continuously occupied.

- Software-emulated exponentials: FA4 implements exp() via polynomial approximation on FMA units rather than routing through the SFU. This moves the exponential bottleneck onto general-purpose compute that Blackwell has in abundance.

- Conditional softmax rescaling: Online softmax normally rescales intermediate results every time the running maximum changes. FA4 skips that rescaling unless the shift is large enough to threaten numerical stability, reducing rescaling operations by roughly 10× according to Tri Dao's Hot Chips presentation.

FA4 is also implemented entirely in CuTe-DSL, a Python-embedded DSL that is part of NVIDIA's CUTLASS library. As Tri Dao put it at the time of release, installing and compiling now takes seconds instead of minutes or hours. This is a huge improvement for anyone doing iterative kernel development or running JIT workflows.

## The performance impact

All numbers are from the FA4 paper (arxiv:2603.05451) and the PyTorch blog post published March 5, 2026. Results are hardware- and configuration-specific. Be sure to validate on your own setup before making infrastructure decisions.

On NVIDIA HGX B200 in BF16:

- 

1,613 TFLOPs/s peak forward pass throughput

- 

71% hardware utilization

- 

Up to 1.3× speedup over NVIDIA cuDNN 9.13

- 

Up to 2.7× speedup over Triton

Gains are strongest at sequence lengths of 4k and above. The paper notes that NVIDIA has since incorporated several FA4 techniques into newer cuDNN releases, bridging that gap in recent versions. 

For custom attention variants via FlexAttention with an FA4 backend, benchmarked on NVIDIA GB200 NVL72:

 | 

Pattern

 | 

Forward vs. Triton

 | 

Backward vs. Triton

 | 

Dense/causal

 | 

1.6–3.2×

 | 

1.85–2.3×

 | 

ALiBi

 | 

1.2–2.1×

 | 

1.9–2.9×

 | 

Document masking

 | 

up to 2.7×

 | 

up to 3×

 | 

Sliding window

 | 

1.4–2.1×

 | 

1.8–2.2×

## 
What does this mean for you?

Teams running on NVIDIA HGX B200 or NVIDIA GB300 NVL72 now have access to the most optimized attention kernel available for that architecture, and GPU utilization is as high as it has ever been for these workloads.

- 

Training long-context models: On documents, code repositories, multi-turn conversations, and scientific literature, FA4's gains are largest exactly where attention is most expensive, at 4k tokens and above.

- Serving real-time long-context inference: Larger effective batch sizes become achievable at a given sequence length, which translates directly to increasing throughput and reducing serving costs.

- 

Building custom attention variants: FlexAttention with an FA4 backend means ALiBi, sliding window, document masking, and arbitrary score modifications can stay in Python and still perform close to a hand-optimized NVIDIA CUDA kernel on both Hopper and Blackwell.

The ROI of running attention-heavy workloads on Blackwell hardware shifts meaningfully with FA4. Higher throughput at the same hardware cost means lower per-token cost for long-context applications, and the hardware investment is being utilized close to its rated capacity.

We are at the most optimized state this stack has ever been in. FA4 on Blackwell combines the best attention kernel with the best available GPU hardware, and it is open source. The question now is who harnesses it and what they build with it.

## Run it yourself

Launch on-demand Instances in minutes: https://lambda.ai/instances
Go multi-node with 1-Click Clusters: https://lambda.ai/1-click-clusters

## References

Paper: https://arxiv.org/abs/2603.05451 
Code: http://github.com/Dao-AILab/flash-attention

## AUTHORED BY

 Lea Alcantara

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
