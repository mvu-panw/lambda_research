# DeepSeek V4: the most expected open-source model ever released, and the quietest landing

Source: https://lambda.ai/blog/deepseek-v4-the-most-expected-open-source-model

Skip to main content

# DeepSeek V4: the most expected open-source model ever released, and the quietest landing

 May 22, 2026

 (Updated on June 4, 2026)

 • 3 min read

After 15 months of incremental updates, leaks, and rumored leaks, DeepSeek released version 4. It arrived without the fanfare R1 and R1-preview commanded in early 2025.

That quiet reception is the most interesting thing about the release. A few months ago, the same model would have dominated the cycle. Now the headlines include a mixture of open and closed models trained on multiple infrastructure providers. The infrastructure conversation has crowded out the model conversation, and DeepSeek v4 is the first major open release to land in that climate.

For teams running these models in production, that's the right context. The architecture changes in v4 are engineering wins more than capability leaps, and engineering wins is what matters when you're paying for serving. Beyond the model itself, NVIDIA and Lambda co-design infrastructure and optimize performance to further reduce the cost per token on open models like DeepSeek V4 as proven by the latest MLPerf Inference V6 results. 

## What shipped

DeepSeek released two models, both under the MIT license:

- DeepSeek V4 Pro. 1.6T parameters, deployable on a single NVIDIA HGX B200 node. The largest open-source model released to date.

- DeepSeek V4 Flash. 284B parameters. Smaller, but holds its own on most evals.

The MIT license is notable. Other China-based AI labs have been migrating to open-weight licenses. DeepSeek hasn't.

## The architecture: built for serving, not benchmarks

DeepSeek's team highlighted several architectural changes. Most are engineering optimizations rather than capability bets, and most appear to address constraints from the GPU chips DeepSeek operates on.

The headline change is a hybrid attention mechanism extending DeepSeek Sparse Attention (DSA). Two new components, Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), combine to cut single-token inference FLOPs and KV-cache memory at long context. Cost-to-serve drops over 10x versus V3.2, with roughly 10x less memory.

Source: DeepSeek-V4 Technical Report

That's the win. The catch: long-context benchmark gains are inconsistent. The team needed this work to scale toward a reliable 1M context window, and they got there on cost. The capability uplift hasn't followed yet.

### A mixed reception

DeepSeek V4 entered with decent but not standout evals against other open-weight and open-source releases. Kimi K2.6, from a younger lab, beats V4 on several coding evals and scored higher on Artificial Analysis (a popular signal measurement for model rankings).

Source: DeepSeek is back among the leading open weights models with the release of DeepSeek V4 Pro and V4 Flash, with V4 Pro second only to Kimi K2.6 on the Artificial Analysis Intelligence Index

A handful of notable practitioners are running V4 inside their evaluation harnesses with reasonable results, though most are pairing it with larger models rather than running it solo with little success.

Source: @xjdr X post

### What's next

DeepSeek's work continues to shape the frontier of open weights. A meaningful share of today's strongest open-weight models trace their architecture back to DeepSeek's research, and V4's serving optimizations give every other lab a new starting point.

The serving cost story is the one to watch. If 10x cheaper inference holds in production, the economics of running 1M-context models change, and the labs that adapt fastest, including DeepSeek itself, will define how the next generation of open-weight models looks.

For teams running V4, the cost case is real, the capability story is still developing, and the right move depends on whether your workload values context window or eval scores. Lambda is deploying both Pro and Flash, with model cards and serving guidance below.

- Model card: DeepSeek V4 Pro

- Model card: DeepSeek V4 Flash

## AUTHORED BY

 Zach Mueller

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
