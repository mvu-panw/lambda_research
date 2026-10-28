# How to deploy ML jobs on Lambda Cloud with SkyPilot

Source: https://lambda.ai/blog/how-to-deploy-ml-jobs-on-lambda-cloud-with-skypilot

Skip to main content

# How to deploy ML jobs on Lambda Cloud with SkyPilot

 January 20, 2026

 (Updated on October 22, 2026)

 • 3 min read

TL;DR: SkyPilot is an open-source orchestration tool that automates ML job deployment on Lambda Cloud. This tutorial covers installation, configuration, and running an example job that evaluates DeepSeek-R1-Distill-Qwen-7B on multiplication tasks with automatic instance termination when the job completes.

Without proper orchestration, deploying ML jobs often forces ML engineers to spend valuable time on system administration tasks, such as installing and upgrading software. Poorly managed cloud resources can also lead to unnecessary and costly charges when left running idle.

SkyPilot, an open-source orchestration tool designed to simplify ML job deployment and management on cloud infrastructure (including Lambda Cloud), provides a solution to these common problems.

In this post, you’ll learn how to install SkyPilot, configure it for Lambda, then use it to automatically launch an instance, submit an ML job, and safely terminate the instance after the job’s completion. Our example evaluates the DeepSeek-R1-Distill-Qwen-7B LLM’s ability to solve multiplication problems.

## Prerequisites

To try SkyPilot on Lambda Cloud, you’ll need to:

- Create a Lambda Cloud account

- Generate a Cloud API key

- Install uv on your computer

## Installing and configuring SkyPilot

Use uv to install SkyPilot on your computer. For other ways to install SkyPilot, see SkyPilot’s installation documentation.

First, create a dedicated directory and virtual environment for SkyPilot:

mkdir -p skypilot && cd skypilot
uv venv --python 3.12
source .venv/bin/activate
uv pip install "skypilot[lambda]"

Once SkyPilot is installed, configure it for Lambda Cloud:

mkdir -p ~/.lambda_cloud
chmod 700 ~/.lambda_cloud

echo "api_key = <LAMBDA-API-KEY>" > ~/.lambda_cloud/lambda_keys

chmod 600 ~/.lambda_cloud/lambda_keys

Replace <LAMBDA-API-KEY> with your actual Cloud API key.

## Submitting a job

Define your ML job by creating a YAML file named eval_multiplication.yaml:

resources:
 accelerators: {40GB+}
 autostop:
 idle_minutes: 10
 down: true

envs:
 SCRIPT_URL: "<https://docs.lambda.ai/assets/code/eval_multiplication.py>"
 MODEL_ID: "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

setup: |
 echo "Downloading evaluation script..."
 curl -L "$SCRIPT_URL" -o eval_multiplication.py

run: |
 echo "Running evaluation with uv..."
 uv run --with vllm --with huggingface-hub python eval_multiplication.py "$MODEL_ID" --stdout

This configuration defines a job that:

- Launches an on-demand instance with 40 GB or more of VRAM

- Automatically terminates the instance if it remains idle for more than 10 minutes

- Downloads and runs a Python script to perform the LLM evaluation

To learn more about defining jobs, see the SkyPilot YAML documentation.

Use the sky launch command to run the job:

sky launch eval_multiplication.yaml

You’ll see a summary of the available resources, similar to the following:

Considered resources (1 node):
-----------------------------------------------------------------------------------------
 INFRA INSTANCE vCPUs Mem(GB) GPUS COST ($) CHOSEN
-----------------------------------------------------------------------------------------
 Lambda (us-east-1) gpu_1x_a6000 14 100 A6000:1 0.80 ✔
 Lambda (us-east-1) gpu_1x_a100_sxm4 30 200 A100:1 1.29
 Lambda (us-east-1) gpu_1x_gh200 64 432 GH200:1 1.49
 Lambda (us-east-1) gpu_1x_h100_pcie 26 200 H100:1 2.49
 Lambda (us-east-1) gpu_1x_b200_sxm6 26 360 B200:1 5.29
-----------------------------------------------------------------------------------------
Launching a new cluster 'sky-ea49-lambda'. Proceed? [Y/n]:

Launch a new cluster (instance) to begin the job. Once it’s complete, you’ll see the evaluation results:

Processed prompts: 100%|██████████| 1000/1000 [00:43<00:00, 23.01it/s, est. speed input: 388.32 toks/s, output: 6669.35 toks/s] 6662.85 toks/s]
(task, pid=3997) Model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B accuracy: 0.9020
✓ Job finished (status: SUCCEEDED).

After 10 minutes, the instance will automatically terminate. You can use the Lambda Cloud console to confirm that the instance has terminated.

## Next steps

SkyPilot simplifies deploying and managing ML workloads on Lambda Cloud, so you can spend less time on infrastructure and more time on model development and evaluation.

Not sure which orchestration solution is best for your organization?

Talk to our team.

## AUTHORED BY

 Cody Brownstein

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
