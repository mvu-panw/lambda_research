# Creating highly efficient agents: 450M tool-calling tokens distilled for post-training from top open-source models

Source: https://lambda.ai/blog/creating-highly-efficient-agents-450m-tool-calling-tokens-distilled-for-post-training-from-top-open-source-models

Skip to main content

# Creating highly efficient agents: 450M tool-calling tokens distilled for post-training from top open-source models

 April 30, 2026

 • 7 min read

## Harnesses

If you've used Claude Code or Codex, you've used a harness. A harness is the infrastructure layer that wraps an AI coding agent and decides how it operates, what it can touch, and how you measure whether it worked. It's how most engineers interact with frontier models today.

The category is moving fast. OpenClaw crossed 340,000 GitHub stars in six months, making it one of the fastest-growing repositories on the platform. Hermes Agent is on a similar trajectory.

A general-purpose harness can wire your agent into the tools you already use: iMessage, Discord, and others. The interesting part for engineers running their own stack: many of these harnesses can pair with open models that are small enough to run on a single GPU at home and hold up under real workloads.

## Hermes Agent

Hermes Agent is a new entrant into the scene, promising greater freedom in what agents can be, a more robust and secure software codebase, and greater appeal to the open-source community since it's led by Nous Research, a well-known open-source AI lab. Yet even the best harness is only as good as the model steering it, and today's top open-weight performers are simply too large to run unquantized.

We built a 450M-token distillation pipeline covering tool calls, conversation threads, and multi-step reasoning, drawn from three frontier, permissively licensed, open-weight models. The goal is to compress frontier-grade skills into a footprint small enough to run unquantized on lightweight compute, in the cloud or on the laptops and computers running in your home. By open-sourcing the entire corpus, we're giving the community access to the tokens to train small, specialized models that can perform as well as the giants at a fraction of the cost.

## Model selection

When we were deciding which models to use to create our synthetic tokens, we considered a few factors:

- 

Position on the PinchBench Leaderboard. This is regarded as one of the first places to check which models perform best for OpenClaw- and similar harnesses.

- 

The feasibility of someone at home running the model. The aim of this project is to take large models that users typically wouldn't be able to run on their home compute or on a single GPU, and make the data available. This means examining models that exceed 300 billion parameters, since spinning up these models costs tens of thousands.

- 

Interesting model behaviors. Different large models have distinct capabilities, which can make distillation particularly interesting. We'll discuss this in more detail shortly.

### PinchBench

PinchBench is a benchmark that examines how a model performs under the OpenClaw harness. It measures a variety of tool use, such as file navigation, data analysis, and the ability to recall prior information.

At the time of writing, the top-performing open-weight models include:

- 

Arcee's Trinity-Large-Thinking

- 

Qwen's 3.5 27B

- 

NVIDIA Nemotron 3 Super

For our distillations, we chose to include Trinity-Large-Thinking, which was released earlier this month.

### Interesting model behaviors

Aside from picking strong models, another factor in selection was choosing models that exhibit interesting behaviors. From the list of recently released models with special characteristics, we chose Kimi's K2.5. This model supports parallel tool calling, allowing it to use two or more separate "tools" at once. This allows the model to be both token and turn-efficient. If a user asks it to “create a new FastAPI route, add its unit tests, and bump the patch version in pyproject.toml," it can spin up:

- 

A write_file tool call for the route

- 

A write_file tool that’s already creating the unit tests

- 

A bump_version tool to do the incremental versioning

All this just from one model query.

## The final models

We focused on three models because of their strong coding and tool-calling abilities, the community's interest, and how often these models are used:

- 

Arcee's Trinity-Large-Thinking

- 

Kimi K2.5

- 

GLM-5.1

## The data

As for the data itself, it represents "turns" in a conversation directly from the Hermes Agent harness. We came up with a few assumptions, since this was purely an initial test and proof-of-concept:

- 

We assume that all data the harness generates is sound and correct, given that the harness itself is running through the conversation chain.

- 

The initial conversation prompts are varied, but could be prone to failure. Strong cleaning will likely be needed after the fact to take the dataset from “good” to “great.”

- 

There are, on average, 20 turns per sample, with each turn using 10-15 different tools.

As a result, we're able to ensure that not only is it sound data (data that serves a purpose), but it also has an innate self-verification loop (does it run) and can be traced to identify useful behaviors within the data itself.

Each model generated ~150 million tokens across 184 NVIDIA H100 GPUs over a few days. Some models finished very quickly (such as Kimi and Trinity), while others, notoriously slower models like GLM, finished over the course of days. The models were served using vLLM with an optimized configuration for the compute we had, and a load balancer to ensure all model replicas were running 24/7.

Here are a few examples from GLM 5.1 and Kimi K2.5 showing a problem (request), the model choosing which tools to use, and then trying to fulfill the request.

id: 0c699abf-bc77-454a-8197-d56a2294098acategory: Agent Tools / Memory & Contextmodel: Kimi K2.5
task:Look through past sessions for the deployment config we created for the staging environment.
human:Look through past sessions for the deployment config we created for the staging environment. I need it again.
gpt:
<think>The user wants to retrieve a previously created staging deployment config.Plan: search past sessions using relevant keywords.</think>
<tool_call>{ "name": "session_search", "arguments": {   "query": "staging deployment config" }}</tool_call>
tool_response:<tool_response>{ "tool_call_id": "functions.session_search:0", "name": "session_search", "content": {   "success": false,   "error": "Session database not available." }}</tool_response>
gpt:<think>Session search is unavailable. Retry with alternative queries or inform the user.</think>
I don’t currently have access to the session database to retrieve past conversations. Trying alternative search queries:
<tool_call>{ "name": "session_search", "arguments": {   "query": "deploy staging" }}</tool_call>
<tool_call>{ "name": "session_search", "arguments": {   "query": "environment configuration" }}</tool_call>...

id: 1b510b01-5892-4810-8663-8f457280d904category: Terminal & Coding / Terminal Tasksmodel: GLM 5.1
task:Write a Python script that reads a CSV file, cleans the data by removing duplicates and fixing formatting, and outputs the results.
human:Write a Python script that reads a CSV file, cleans the data by removing duplicates and fixing formatting, and outputs the results.
gpt:<think>The user wants a Python script that:1. Reads a CSV file2. Cleans the data (remove duplicates, fix formatting)3. Outputs the cleaned results
Plan: implement a structured script that handles common data-cleaning tasks.</think>
Here’s a Python script that reads a CSV, cleans it, and outputs the results:
<tool_call>{ "name": "write_file", "arguments": {   "path": "csv_cleaner.py",   "content": "#!/usr/bin/env python3\\n\\"\\"\\"\\nCSV Data Cleaner\\n...(7,660 bytes of Python source — full text in /tmp/glm_full.md)...\\n" }}</tool_call>
tool_response:<tool_response>{ "tool_call_id": "chatcmpl-tool-86225be549df082c", "name": "write_file", "content": {   "bytes_written": 7660,   "dirs_created": false }}</tool_response>
gpt:<think>Preparing test data to validate the script.</think>
Now creating a sample CSV file and running the script:
<tool_call>{ "name": "write_file", "arguments": {   "path": "sample_data.csv",   "content": "Name,Email,Phone,DateOfBirth,Salary\\n\\"john doe\\",\\"John.Doe@GMAIL.com\\",\\"555-123-4567\\",\\"01/15/1990\\",\\"$75,000.50\\"\\n\\"  JANE  SMITH  \\",\\"jane.smith@yahoo.com\\",\\"5559876543\\",\\"03-22-1985\\",\\"€60,000\\"\\n\\"bob johnson\\",\\"bob@gmail.com\\",\\"1-555-222-3333\\",\\"12/05/1992\\",\\"45000\\"\\n... (duplicates + messy rows for testing) ..." }}</tool_call>...

## What's next?

Right now, we're training smaller language models on this data to develop specialized models for the Hermes Agent harness. We've been working on these datasets, cleaning them and training our own models with them, and the AI community has been doing the same. You can try these out today as the backend to your own harness.

Here are some useful links to learn more about our work:

●    The Lambda Hermes Agent dataset on Hugging Face
●    An LFM fine-tune on our data by a community member
●    A Qwen3.5 9B fine-tune on our data by a community member

## AUTHORED BY

 Zach Mueller

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
