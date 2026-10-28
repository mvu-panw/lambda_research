# What happens when Claude Code gets an experiment tracker

Source: https://lambda.ai/blog/what-happens-when-claude-code-gets-an-experiment-tracker

Skip to main content

# What happens when Claude Code gets an experiment tracker

 June 25, 2026

 • 6 min read

At CVPR 2026, Lambda ran a live demo for two and a half days: Claude Code teaching Google's Gemma 4 to play a Tetris-like game. Claude Code started with a Gemma 4 model that couldn't play at all. It pressed “down” and lost in seconds. By the end of the demo, the same agent had iterated through hundreds of experiments, trying various board representations, image inputs, prompts, inference settings, and vLLM launch parameters. Slowly but surely, Claude taught Gemma 4 how to play.

No human tuned the parameters. No human chose the prompts. Claude Code ran the experiments, tracked what worked, and built on its own results.

It ran on GPUs that would’ve have been underutilized otherwise: 468 experiments for zero added compute cost.

The tool that made this possible is the_lab.api.

## Agents can experiment, but they can't remember

Agents can write code. Agents can run experiments. What agents can't do is keep track of what they've tried.

A researcher using Weights & Biases opens a dashboard, compares runs, and sees which hyperparameters improved loss. The UI is built for human eyes. An agent has no eyes. It needs an API.

Without structured experiment tracking, an agentic loop does one of two things: it re-runs experiments it already ran, or it loses the thread of what worked and why. At scale, this turns into sprawl. Hundreds of branches. No leaderboard. No memory.

## the_lab.api: experiment tracking as an API

The Lab is a set of API endpoints that provide agents with what Weights & Biases provides humans.

Core capabilities:

- Experiments: start, queue, or cancel experiments, inspect the logs, check which knobs were tuned, which parameters changed, which git branch holds the code

- Leaderboard: to orient, agents query which experiments performed best, in ranked order, so they can search through the backlog

- Ideas as branches: each "idea" is a pinned version of the code (a git branch); within that branch, the agent can run multiple experiments with different configs

- History: the agent never loses context; it can always see what it tried, what scored, and what direction to explore next

- Message board: although not part of the demo, multiple agents can be launched in the_lab.api to collaborate on the same project; a message board helps them to communicate progress between each other

In the demo, the whole campaign ran through this API: about 810 calls, no dashboard, and no human reading charts. 82 leaderboard queries that informed 91 new ideas (each a fresh branch), 486 experiment launches, and 73 ideas concluded and built upon. That loop, query the leaderboard, branch an idea, run experiments, conclude, repeat, is the research process, expressed as API calls instead of clicks.

## 468 experiments, autonomous by default

The task: teach a Gemma 4 model to play Tetris using only experimentation (no fine-tuning, only inference).

What Claude Code controlled:

- Inference parameters (how vLLM launched Gemma 4)

- Prompting strategy and prompt optimization

- Sampling parameters (token budget, KV cache precision)

- Whether to use Gemma 4's reasoning mode (on/off)

- Whether to use Gemma 4's multimodal image capabilities

- Draft model settings (a smaller model used as a speculative decoding model to speed up inference)

What Claude Code could not touch was just as important.

The game engine, the client, and the scoring harness were locked read-only, enforced by a list of blocked files, a git pre-commit hook, and a bcrypt-protected disable password that the agent can't override through the API. The fastest way for a capable agent to "maximize the score" is not to improve Gemma at all. It can delete Gemma and write a few lines of code that solve the puzzle directly, and Claude tends to discover exactly that within a few ideas. The sandbox keeps the core game logic read-only, so the only levers left are the ones that actually exercise the Gemma model's reasoning. Without it, you measure the orchestrator's cleverness; with it, you measure the model.

Claude began with a model sweep: compared five Gemma 4 variants (12B, 26B-A4B, E2B, E4B, and the 31B AWQ build) and committed to the 31B model, then optimized everything around it. Each experiment took roughly 30 minutes. Over two and a half days, Claude Code iterated through 468 experiments across 90 distinct ideas. The leaderboard tracked every run. Claude Code queried the leaderboard, identified what worked, and built on it.

One detail shows why this needs infrastructure at all. Early on, the same configuration scored 7 on one run and 3 on the next, identical settings and different luck (GPU math isn't perfectly deterministic at this scale). Without a leaderboard to compare repeated runs, the agent would have chased that 7 as if it were progress. Tracking is what lets it tell a real improvement from a lucky one: it learned to repeat each idea several times and compare medians rather than celebrate a single lucky score. An agentic loop without that memory wastes compute and, worse, draws the wrong conclusions.

The progression ran from a score of 0, losing in seconds, to clearing lines across the full 30-minute game and peaking at a score of 16. No human intervention.

## Spare GPUs, zero marginal cost

The demo ran on a Lambda Slurm cluster with 16x NVIDIA H100 GPUs, using a preemptible queue capped at 8 parallel jobs and GPU hours that would’ve otherwise been idle. If a team member launched a higher-priority job, the experiment was canceled and requeued for later.

The only real bill was the orchestration itself. Driving the entire search, 4.4M tokens of reasoning across ~810 API calls, cost roughly $1,200 in Claude API usage. Over the ~2.5-day run, that works out to about $20 per hour of agent-driven research (around $2.70 per experiment). That’s the whole economic profile of the demo: roughly $20/hour of model reasoning, on top of GPU time that would otherwise wait for compute jobs.

That rate isn’t fixed. It scales with two choices:

- The model. We ran the most expensive option, Claude Opus 4.8, on its highest reasoning setting (since we wanted to see progress during the conference weekend).

- The experiment length. The agent only costs money while it’s reasoning, not while it waits for a game to finish. Waiting is free. Our games were short (30 minutes), so the agent cycled through many of them and reasoned often. Running 300-minute experiments instead would cost roughly a tenth per hour: fewer, longer runs, with the agent simply idling in between.

The infrastructure pattern was agentic experimentation that increased utilization by filling idle capacity. The compute cost was zero marginal GPU hours.

For Lambda Cloud users, this points to a future in which idle GPU time on reserved instances automatically runs background experimentation loops. The project is open source (MIT license, with its code hosted on GitHub). Any team with a Slurm cluster or cloud instances can set it up.

## What’s next

Agentic AI is moving from "write code and deploy" to "hypothesize, experiment, evaluate, and iterate." That loop doesn’t need just GPUs. It needs infrastructure, tracking, reproducibility, and memory.

The Lab is the first step toward that infrastructure. It’s open-source, built at Lambda, and tested in the wild at CVPR. Try it on GitHub. For the full demo story, the dead ends, the breakthroughs, and the one-line change that doubled the score, see the companion write-up on LinkedIn.

## AUTHORED BY

 David Hartmann

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
