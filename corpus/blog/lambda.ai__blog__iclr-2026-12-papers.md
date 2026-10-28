# ICLR 2026: 12 papers on making AI systems reliable, efficient, and secure

Source: https://lambda.ai/blog/iclr-2026-12-papers

Skip to main content

# ICLR 2026: 12 papers on making AI systems reliable, efficient, and secure

 April 23, 2026

 (Updated on June 5, 2026)

 • 7 min read

A 7B agent that beats GPT-4o. Lossless weight compression that speeds up inference by 177%. An arena where 23 teams battled across 103,000 adversarial rounds. This year at ICLR, Lambda is presenting twelve papers and two workshops with over 20 collaborators across academia and industry. This work covers agents, LLMs, physical AI, and multimodal efficiency, addressing some recurring themes: long-horizon agentic planning under sparse rewards, alignment with safety constraints, structured world modeling, and inference-time efficiency.

## Agents that plan, socialize, and grade

Systems that plan, reason, and invoke tools over extended horizons are quickly gaining capability, but training them remains a challenge. Reward signals are often sparse and delayed, and credit assignment across long trajectories doesn't come naturally.

In-The-Flow Agentic System Optimization [1] introduces AgentFlow, a trainable agentic system where a team of agents learns to plan and use tools in the flow of a task, and Flow-GRPO (Flow-based Group Refined Policy Optimization), an efficient method to train a modular agent live inside its own loop. Rather than optimizing the whole trajectory at once, Flow-GRPO breaks it into single-turn updates and propagates a verifiable trajectory-level signal back to each step, with group-normalized advantages for stability. With this approach, a 7B AgentFlow model beats GPT-4o on search, math, and science reasoning.

Capability alone isn't enough; agents also have to hold up when other agents, users, or adversaries push back. The KAIROS benchmark [2] drops models into collaborative scenarios with unreliable peers and adversarial participants, revealing that LLMs cave under peer pressure; an RL recipe in the same paper helps smaller models resist. EdiVal-Agent [3] takes a different angle, using agents as evaluators: it grades multi-turn image editing by decomposing images into objects and scoring outputs on instruction-following, consistency, and visual quality, surfacing where today's best editors quietly break down.

## LLMs in the wild: alignment, correction, and adaptation

Indirect prompt injection can be written into the persistent-memory agent reloads every session, turning a one-time attack into a durable backdoor [13]. We collaborated with UC Berkeley’s Center for Responsible, Decentralized Intelligence (RDI) to organize the Agent Security Arena, a public competition in which 23 teams built autonomous attack and defense agents that battled head-to-head across prompt-injection scenarios. Every agent ran on the same fixed open-weight LLM, but each team had a different harness code: prompts, multi-step reasoning, and fallback logic. Over 65 evaluation rounds, the arena logged more than 103,000 battles across 31 scenarios spanning finance, healthcare, legal, and cybersecurity.

We'll be sharing findings at the ICLR 2026 Agents in the Wild workshop.

Our study also discovered that models don't need an adversary to go off track. OffTopicEval [4] shows that even with a clear role and explicit boundaries, current LLMs answer questions they shouldn't, almost every time. Once these failures are identified, the next question is how to fix them. RASLIK [5] reframes LLM unlearning as data selection: using a linearized influence kernel, it picks both the data to forget and retain, pushing the trade-off frontier past oracle sampling. Three more papers push the same agenda further: MEERKAT [6] handles correction when data can't be pooled across clients, ESPO [7] adapts principled RL to diffusion language models, and Inference-Time Rethinking [14] gives models a way to revise their reasoning before answering (to be presented at ICLR's Latent & Implicit Thinking workshop).

## From pixels to particles: structured world models

Modeling the physical world gets easier when you move from raw signal to structured representations. We explore this in two settings: how objects move in video, and how molecules evolve over time.

Latent Particle World Models [8] moves away from patch-based video representations toward object-centric latent particles that track salient entities. Most video models divide frames into a fixed grid of patches without regard for semantic content. LPWM instead discovers objects, keypoints, and masks directly from raw video with no supervision, and models their stochastic dynamics through a novel latent action module. The architecture is trained end-to-end from video alone but supports flexible conditioning on actions, language, and image goals, making it applicable to both video prediction and decision-making. On diverse real-world and synthetic multi-object datasets, LPWM achieves state-of-the-art results, and, downstream, it makes goal-conditioned imitation learning more effective because the model reasons over things rather than patches.

The same principle applies at the molecular scale. EGInterpolator [9] pretrains on abundant static conformer data and learns to stitch those structures into realistic Molecular Dynamics trajectories, sidestepping the scarcity of simulation data for drug discovery and materials design.

## The efficiency tax on multimodal models

Running multimodal models can be expensive. Three papers address the cost of running multimodal models from different angles: sparsity in video data, architecture efficiency for audio, and lossless compression for model weights.

Long-context video understanding has a clear bottleneck: attention cost blows up on long sequences. Existing approaches either compress tokens (irreversibly losing information) or apply static sparse patterns that don't adapt to the input. VideoNSA [11] takes a different path: a learnable, hardware-aware sparse attention mechanism built on Qwen2.5-VL that combines three complementary branches for video tokens: a compression branch that aggregates frame-level blocks into coarse representations, a selection branch that identifies the most salient tokens, and a sliding window branch for local temporal coverage. A learned gate dynamically weights these branches at each layer, while text tokens retain full dense attention. At 128K tokens, VideoNSA uses 3.6% of the attention budget and still improves accuracy over both dense and token-compression baselines on long-video understanding, temporal reasoning, and spatial benchmarks.

In addition to being selective about attention, efficiency also comes from lean architecture. TangoFlux [10] proposes a lean 515M-parameter text-to-audio model that generates 30 seconds of studio-quality sound in under 4 seconds, bootstrapping its own alignment signal through CLAP-Ranked Preference Optimization.

Building small is one strategy; compressing what's already trained is another. It turns out the exponents of trained model weights concentrate into just 2 to 3 bits of entropy out of the 4 bits FP8 allocates. That gap is compressible. ECF8 (Exponent-Concentrated FP8) [12] exploits this by encoding redundancy with Huffman coding, yielding up to 26.9% memory savings on diffusion models and throughput gains up to 177.1%, with perfectly lossless computation scaling to 671B LLM parameters.

## Get involved

The best AI labs we've worked with this year all share a quiet frustration: great research ideas routinely stall on infrastructure, scaling, and systems-level engineering. That's the gap Lambda is built to close. We bring compute infrastructure and engineering support, as well as a dedicated ML team that can contribute technically to every stage of the research, from problem formulation to experiments to publication. The results speak for themselves: twelve ICLR papers and two workshops with over 20 partners, including Stanford, CMU, UC Berkeley, UCSD, UCLA, Google, NVIDIA, and Microsoft.

We're looking for new collaborators across agents, alignment, world modeling, and efficiency. For independent researchers who need compute, the Lambda Research Grant also offers up to $5,000 in credits for Lambda's on-demand Instances. Apply for the Lambda Research Grant at lambda.ai/research.

## References

[1] In-The-Flow Agentic System Optimization for Effective Planning and Tool Use https://arxiv.org/abs/2510.05592 https://agentflow.stanford.edu/

[2] Measuring and Mitigating Rapport Bias of Large Language Models under Multi-Agent Social Interactions https://openreview.net/forum?id=gF31wuYdk7

[3] EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing https://arxiv.org/abs/2509.13399 https://tianyucodings.github.io/EdiVAL-page/

[4] OffTopicEval: When Large Language Models Enter the Wrong Chat, Almost Always! https://arxiv.org/abs/2509.26495 https://github.com/declare-lab/OffTopicEval

[5] Randomized Antipodal Search Done Right for Data Pareto Improvement of LLM Unlearning https://openreview.net/forum?id=Xn6EnJZghu

[6] Mitigating Non-IID Drift in Zeroth-Order Federated LLM Fine-Tuning with Transferable Sparsity https://arxiv.org/abs/2506.03337

[7] Principled RL for Diffusion LLMs Emerges from a Sequence-Level Perspective https://arxiv.org/abs/2512.03759 https://github.com/ML-GSAI/ESPO

[8] Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling https://arxiv.org/abs/2603.04553 https://sites.google.com/view/lpwm/home

[9] Align Your Structures: Generating Trajectories with Structure Pretraining for Molecular Dynamics https://arxiv.org/abs/2604.03911

[10] TangoFlux: Super Fast and Faithful Text to Audio Generation with Flow Matching and CLAP-Ranked Preference Optimization https://arxiv.org/abs/2412.21037 https://tangoflux.github.io/

[11] VideoNSA: Native Sparse Attention Scales Video Understanding https://arxiv.org/abs/2510.02295 https://enxinsong.com/VideoNSA-web/

[12] To Compress or Not? Pushing the Frontier of Lossless GenAI Model Weights Compression with Exponent Concentration https://arxiv.org/abs/2510.02676 https://github.com/zeyuyang8/ecf8/

[13] Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/

[14] Inference-Time Rethinking with Latent Thought Vectors for Math Reasoning
https://arxiv.org/abs/2602.06584

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
