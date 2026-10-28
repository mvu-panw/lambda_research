# Open Jarvis: making local LLMs work as agents

Source: https://lambda.ai/blog/open-jarvis-local-llm-agents

Skip to main content

# Open Jarvis: making local LLMs work as agents

 September 30, 2026

 • 8 min read

Running an open-weight model is only half the job. The other half is the harness: what tells the model what to do, which tools it can use, and how to learn from its mistakes.

Open Jarvis started with a question: what stands in the way of personal AI running locally today? The open-weight releases keep coming, so why aren't they letting people own their own intelligence?

Drop an open-weight model into a stack tuned for a cloud model, and performance falls off. That's the problem Open Jarvis solves.

The paper shows it plainly. Swap the frontier cloud model in an agent system for a 9B open-weight model, and performance drops. On PinchBench, which measures how well an LLM performs as the brain of OpenClaw agents, accuracy fell from 96.0% with Claude Opus 4.6 to 62.3% with Qwen3.5-9B. Retarget the spec around the local model with Open Jarvis, and it recovers to 88.4%, closing 77% of the gap by tuning the harness alone — before any further spec-search optimization on top.

The performance drop is due to the harness being optimized for a different model. That harness/model system is what transforms a language model into an agent that can schedule meetings, write and run code, search the web, manage files, and remember context across sessions. Without it, local models cannot reach their full potential.

## What Open Jarvis actually does

Open Jarvis is built around a spec that is unique to a model and the machine the model runs on. The spec contains five independently configurable primitives, each of which can be retargeted around any choice of model. Given a chosen Intelligence and Engine, LLM-guided spec search uses a frontier cloud model to diagnose failures in the deployed spec and propose edits across all four editable primitives: Intelligence, Engine, Agent, and Tools & Memory, accepting only changes that improve performance without causing regressions elsewhere.

- Intelligence. Which model runs, at what quantization, with what generation settings — for example, swapping from a 9B to a 35B model.

- Engine. The inference runtime (Ollama, vLLM, llama.cpp) and its hardware settings. A Mac Mini and an NVIDIA workstation can fit into this logic; only this layer changes.

- Agent Logic. The reasoning loop, system prompts, few-shot examples, and tool-calling strategy. This is where local models need the most retuning; cloud prompts often assume capabilities that smaller models don't have.

- Tools & Memory. What the agent can do: web search, code execution, calendar and email access, file I/O, and persistent memory across sessions. On research and tool-calling tasks, Tool edits account for the largest share of accepted improvements in spec optimization.

- Learning. How the system improves over time through LoRA fine-tuning, prompt optimization, or automated spec search guided by a frontier teacher model.

## Why separation of concerns is the key insight

A lot of agent harnesses are built around a specific model. When the full framework is made editable, the same agent framework can work across a lightweight model and a 100B+ model running on a big cluster. Only the Intelligence and Engine fields differ, and the other primitives are optimized according to those.

The Open Jarvis experiment shows this: by exposing all five primitives as separate configuration fields — four of them (Intelligence, Engine, Agent, Tools & Memory) jointly optimized by spec search, with Learning operating separately — local models match cloud accuracy on the majority of personal AI benchmarks at roughly 800× lower per-query cost and 4× lower latency on local, personal-device hardware. The best single local model, Qwen3.5-122B, lands within 3.2 percentage points of Claude Opus 4.6 on average across eight benchmarks.

Set up OpenJarvis here. 

## What this means if you're building on Lambda

Lambda GPU instances, powered by NVIDIA, give you the compute. A well-designed harness is what makes it do reliable agentic work. Three practical takeaways:

- You can use this framework to rework your agent system.

- You can use a frontier model to improve your harness, not for every query. One-time spec search using a cloud teacher costs roughly $15, far cheaper than routing every request to the cloud over any meaningful deployment horizon.

- Treat the harness as changeable. The harness is a configuration — your model choice, runtime settings, prompts, tool definitions, and memory backend — and you can iterate on it like any other config.

The open-weight model ecosystem is closing the gap with frontier cloud models faster than expected. For most teams, the model isn't the bottleneck anymore — the harness is.

To make that concrete, here's what harness-level optimization looks like running on Lambda's own infrastructure.

## What this looks like on an NVIDIA HGX B200 instance on Lambda

- On a single NVIDIA HGX B200 node, Kimi K2.6 can serve 32 users concurrently, delivering about 1,286 output tokens/s total or ~40 tokens/s per user.

- That works out to 121.7M tok/day on one NVIDIA HGX B200 system.

We also evaluated Kimi K2.6 against Claude Fable 5.1 on PinchBench using the native OpenHands harness using the Open Jarvis evals CLI. (Claude Opus 4.5 scores the PinchBench outputs as the judge model; Claude Opus 4.6 is the separate frontier baseline referenced earlier in this piece — two different roles, not a version mismatch.)

Agentic evals use tools that slow down pure inference because of code execution, search, etc. On this benchmark, Fable 5.1 achieved a higher mean score on the 75 shared scored tasks: 0.8216 versus Kimi's 0.7301.

For the 75 task cost comparison, charging Kimi's 2.90 hours of summed agent time at the full node rate gives an inference-cost estimate of $155.19, or $2.07 per task, compared with Claude's API $235.48, or $3.14 per task — approximately 34% lower cost.

Cost breakdown:

 |  
 | 

Mean score

 | 

Agent time

 | 

Cost

 | 

Per task

 | 

Fable 5.1

 | 

0.8216

 | 

3.30 h

 | 

$235.48 (API)

 | 

$3.14

 | 

Kimi K2.6

 | 

0.7301

 | 

2.90 h

 | 

$155.19 (GPU)

 | 

$2.07

For workloads where Kimi's quality meets the application's requirements, self-hosting offers a practical combination of lower estimated inference cost, competitive task latency, and control over the model and serving stack.

We ran evals with:

# ~/.openjarvis/config.toml — max_turns defaults to 10 in the code; set to 60 for this benchmark run
[agent]
default_agent = "native_react"
max_turns = 60

python -m openjarvis.evals.cli run \
 -b pinchbench --backend jarvis-agent -m kimi-k2.6 \
 --base-url "http:/node-001:8000" \
 --agent native_openhands \
 --tools "think,file_read,file_write,web_search,shell_exec,code_interpreter,image_generate,calculator,http_request,pdf_extract" \
 -n 147 -w 1 --seed 42 --max-tokens 16000 \
 --judge-model claude-opus-4-5 --judge-engine cloud \
 -o results/pinchbench_kimi-k2.6-think.jsonl

## Setup instructions

If you're a researcher or developer, you should get involved! We encourage you to build on top of OpenJarvis. We welcome PRs that expand the ecosystem.

The fastest way to get started:

git clone https://github.com/open-jarvis/OpenJarvis.git && \
cd OpenJarvis && \
uv sync --extra server && \
source .venv/bin/activate && \
jarvis init && jarvis doctor && \
jarvis ask "What is the capital of France?" 

## AUTHORED BY

 Caia Costello

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
