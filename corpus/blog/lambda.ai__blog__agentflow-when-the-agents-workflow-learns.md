# AgentFlow: when the agent's workflow learns

Source: https://lambda.ai/blog/agentflow-when-the-agents-workflow-learns

Skip to main content

# AgentFlow: when the agent's workflow learns

 August 25, 2026

 (Updated on September 2, 2026)

 • 2 min read

For two years, the field has gotten very good at training models, and it still hand-wires the agents around them. Whether an agent plans, searches, calls a tool, or checks its own work before answering is decided by a developer in prompts and orchestration logic. That hand-built workflow never learns, and as tasks get longer and tools multiply, it's where agents start to break.

AgentFlow makes the workflow itself trainable. It's an ICLR 2026 oral paper (top 1.1% of submissions), co-authored by Stanford, Texas A&M, UC San Diego, and Lambda.

## The problem

Today's agent frameworks are orchestrated by hand. A developer specifies when to plan, when to retrieve, which tool to call, when to verify, and when to hand off. It holds up until the task gets long. Sparse feedback, many turns, and a growing toolset make hand-tuned orchestration brittle, and prompt-engineering your way out doesn't scale. The workflow has become the bottleneck.

## Who it's for

Researchers and developers building agents that reason, plan, and use tools over long horizons: scientific research, software engineering, enterprise automation.

## How it works

AgentFlow splits an agent into four modules that share an evolving memory: a planner, an executor, a verifier, and a generator. The planner is the piece that learns. Instead of freezing it behind a prompt, AgentFlow optimizes it on-policy, inside the live multi-turn loop, with a method the authors call Flow-GRPO (flow-based group refined policy optimization).

The hard part of training an agent over many turns is credit assignment: the only clear signal, did it get the task right, arrives at the very end. Flow-GRPO broadcasts that single end-of-task outcome back to every turn, so each planning decision is scored against whether the whole run succeeded, turning a long multi-turn problem into a series of tractable single-turn updates. The workflow improves through training, not prompt rewriting.

## The results

The headline is the size gap. With a 7B open model, AgentFlow beats much larger proprietary systems, including GPT-4o, across ten benchmarks spanning search, agentic reasoning, math, and science (gains of 14.9%, 14.0%, 14.5%, and 4.1%). Learning a better workflow, it turns out, can matter as much as scaling the model.

The sharpest result is which training method you use. Training the planner in-the-flow with Flow-GRPO added 17.2%. Doing it the conventional offline way, with supervised fine-tuning, made things 19.0% worse. Same model, opposite outcomes.

## Why it matters, and where Lambda fits

The first wave of agents was about building workflows. The next is about training them, the same shift language models already made from prompt engineering to reinforcement learning. Once the workflow can learn, agents adapt to new tasks and improve from experience instead of waiting for someone to rewrite their orchestration.

That's a compute pattern, not just a research one. Training an agent's workflow means reinforcement learning, large-scale rollouts, and repeated policy updates across many GPUs, run over and over as the agent explores. This is the layer Lambda builds: the GPU cloud where teams train, evaluate, and run agents like this at scale.

Project: agentflow.stanford.edu

Paper: arxiv.org/abs/2510.05592

Credits: Stanford University, Texas A&M University, UC San Diego, and Lambda. Authors: Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang, Yejin Choi, James Zou, and Pan Lu. ICLR 2026.

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
