# OpenResearcher: a reproducible and scalable pipeline for training deep research agents

Source: https://lambda.ai/blog/openresearcher-training-research-agents-at-scale

Skip to main content

# OpenResearcher: a reproducible and scalable pipeline for training deep research agents

 September 10, 2026

 • 4 min read

A deep research agent has to do more than answer a question. It plans, searches, opens documents, gathers evidence, reasons across sources, and keeps going across dozens or hundreds of tool calls before it lands on an answer. Training one means teaching all of that. That's where most teams hit a wall.

## The data bottleneck

Training a deep research agent is a different problem from training a chat model. The training data has to capture the whole research process: the planning, the searches, the document navigation, the evidence-gathering, the tool calls that fail and get retried. Question-and-answer pairs don't capture any of that.

Collecting that experience from humans costs a fortune and does not scale. Generating it synthetically runs into its own wall. A single research task can take hundreds of tool calls, and generating at scale means millions of search and retrieval operations. Do it on the live web, and you inherit API bills, rate limits, and search results that change under you between runs.

So the real question is not how to train a research agent. It is how to generate enough high-quality research trajectories to train one, at scale, in a way anyone can reproduce.

## The pipeline

Researchers from Texas A&M University, the University of Waterloo, UC San Diego, and Lambda built OpenResearcher to answer exactly that. The work was accepted as a main conference paper at the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026).

OpenResearcher builds a reproducible offline research environment over 15 million documents, uses GPT-OSS-120B to generate more than 97,000 long-horizon research trajectories, and distills those trajectories into a smaller NVIDIA Nemotron-3-Nano-30B-A3B model.

The pipeline breaks into three stages:

- 

Build a reproducible research environment. Start with 6,000 long-horizon research questions. Bootstrap roughly 10,000 gold documents, then fold in 15 million FineWeb documents to build the corpus. Embed it with Qwen3-Embedding-8B on 8 NVIDIA A100 Tensor Core GPUs (80GB) in about eight hours, build a FAISS index, and serve retrieval on 4 NVIDIA H100 Tensor Core GPUs (80GB). The environment gives agents three tools, search, open, and find, so they can retrieve documents, read them, and locate evidence at scale. Offline, so results hold still between runs.

- 

Generate the trajectories. Deploy GPT-OSS-120B as the teacher and connect it to the environment. It reasons, searches, opens documents, gathers evidence, and iterates toward an answer on its own. Distributed inference on 64 H100 GPUs for about two days produces more than 97,000 long-horizon trajectories, each capturing the full research process, not just the final answer. A filtering pass drops the malformed, incomplete, and low-quality ones.

- 

Distill into a smaller model. Fine-tune Nemotron-3-Nano-30B-A3B on the synthetic trajectories, with context lengths up to 256K tokens so complete research interactions survive training intact. Long-context SFT runs on 8 H100 GPUs for about eight hours. The behaviors a 120B teacher generated now live in a far smaller, cheaper agent.

## The results

OpenResearcher-30B-A3B hits 54.8% on BrowseComp-Plus. That beats GPT-4.1 (36.4%), Claude-4-Opus (36.8%), and DeepSeek-R1 (16.4%), all much larger proprietary systems. It is a 34-point jump over the base Nemotron-3-Nano-30B-A3B model (20.8%).

The more important point: the agent was trained entirely in a controlled offline environment, and it still generalizes to the live web. It scores 26.3% on BrowseComp, 64.1% on GAIA, and 65.0% on xbench-DeepSearch. Against open-source deep research systems on the same benchmarks, the gap is wide: ASearcher-QwQ-32B lands at 5.2 / 52.8 / 42.0 and WebDancer-QwQ-32B at 3.8 / 51.5 / 39.0.

No live-web trajectories in training. The search, evidence-gathering, tool use, and long-horizon reasoning transferred anyway. That is the finding: synthetic research experience, generated at scale, teaches capabilities that hold up in the wild.

## A shift in where the compute goes

OpenResearcher points to a change in how agents get built. The compute moves upstream, from training the model to generating the experience the model learns from:

Run large-scale inference to generate synthetic experience. Post-train on that experience. Get a stronger agent.

Look at the split. Teacher inference ran on 64 H100 GPUs for about two days. The student post-training took 8 H100 GPUs for about eight hours. As this scales to larger models, more tasks, and millions of trajectories, generating synthetic experience becomes a compute workload in its own right, a new and growing category of demand.

## Adoption beyond the paper

OpenResearcher's reach already extends past the model built in the project. NVIDIA adopted OpenResearcher trajectories as SFT data for NVIDIA Nemotron 3 Ultra, which shows the pipeline's synthetic experience can develop research and search capabilities in frontier foundation models. NVIDIA NeMo Data Designer also builds on the OpenResearcher approach for deep-research trajectory generation, bringing the method into scalable synthetic-data infrastructure. Post-training on one end, synthetic-data generation on the other.

## Where Lambda fits

These workloads run across the full agent-development lifecycle: large-model inference, synthetic-data generation, and long-context post-training. Each one needs GPU compute at scale, and each one runs on Lambda. OpenResearcher is what that looks like in practice: frontier research and GPU infrastructure meeting on Lambda to turn compute into new capabilities.

Paper: https://arxiv.org/abs/2603.20278

Credits: Texas A&M University, University of Waterloo, UC San Diego, Verdent AI, NetMind AI, Lambda.

Authors: Zhuofeng Li, Dongfu Jiang, Xueguang Ma, Haoxiang Zhang, Ping Nie, Yuyu Zhang, Kai Zou, Jianwen Xie, Yu Zhang, Wenhu Chen. EMNLP 2026.

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
