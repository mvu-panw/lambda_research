# Deploying NVIDIA Nemotron 3 Nano using vLLM - Lambda Docs

Source: https://docs.lambda.ai/education/large-language-models/deploying-nemotron-3-nano/

Skip to content

# Deploying NVIDIA Nemotron 3 Nano using vLLM#

NVIDIA Nemotron 3 Nano
uses a Mamba state layer on top of a
transformer Mixture-of-Experts (MoE) backbone. This architecture yields up to
four times the output-tokens-per-energy as Nemotron Nano 2 while still scoring at or
above the current open frontier models on SWE-Bench, GPQA Diamond, and IFBench.
This efficiency gain comes from introducing a user-supplied thinking budget
parameter that caps per-request reasoning length, allowing users to tune
latency and accuracy curves without touching the core model.

This document provides an overview of Nemotron 3 Nano, and then shows you how
to deploy and benchmark the model on Lambda Cloud.

## Model details#

### Overview#

- Name: NVIDIA-Nemotron-3-Nano-30B-A3B-BF16

- Author: NVIDIA

- Architecture: MoE

- Core capabilities: Fast reasoning, long-context understanding, robust
 coding performance, robust tool-use performance

- License: NVIDIA Open Model License Agreement

### Specifications#

- Context window: 1,000,000 tokens

- Weights-on-disk: 58GB

- Idle VRAM usage: 120GB

### Recommended Lambda VRAM configuration#

- Instances: 1x B200 (180 GB SXM6) or 1x H100 (80 GB SXM5) (minimum recommended 4096 sequence length)

- 1-Click Clusters: 16x B200 (180 GB) (max sequence length with FP8 KV cache)

## Deployment and benchmarking#

### Deploying to a single-GPU instance#

You can run NVIDIA Nemotron 3 Nano on any instance type that has enough VRAM to
comfortably support it. For example, to deploy Nemotron 3 Nano on a 1x B200 (180 GB SXM6)
instance running the Lambda Stack 22.04 image:

- In the Lambda Cloud Console, navigate to the
 Instances page and click
 Launch instance. A modal appears.

- Follow the steps in the instance launch wizard. Select the following options:

- Instance type: Select 1x B200 (180 GB SXM6).

- Base image: Select Lambda Stack 22.04.

- Security: Create a new firewall ruleset called nemotron-3-nano and
 add a rule to allow incoming traffic to port TCP/8000.

- After your instance launches, find the row for your instance, and then
 click Launch in the Cloud IDE column. JupyterLab opens in a new
 window.

- In JupyterLab's Launcher tab, under Other, click Terminal to
 open a new terminal.

- 

In your terminal, install uv, set up a Python virtual environment, and
 then begin serving Nemotron 3 Nano with vLLM.

curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm --torch-backend=auto
VLLM_SERVER_DEV_MODE=1 vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 \
 --port 8000 \
 --served-model-name nemotron-3-nano \
 --trust-remote-code \
 --enable-sleep-mode

You now have a vLLM server with an OpenAI-compatible REST API running on your
Lambda instance. To verify that the API is working:

- On the Instances page, find the row
 for your instance, and then click its IP in the IP Address column to
 copy the IP to your clipboard.

- 

In a terminal, query the instance's /v1/models endpoint. Replace
 <IP-ADDRESS> with your instance's IP address:

curl http://<IP-ADDRESS>:8000/v1/models

You should see a list of models with Nemotron 3 Nano as the sole list item.

### Deploying to a multi-GPU instance#

If you need more resources—for example, to make use of a larger context
window or to support more users—you can deploy to a multiple-GPU
instance instead. Follow the instructions for deploying to a single-GPU node,
but make the following changes:

- Choose a suitable multi-GPU instance type, such as 8x H100 (80 GB SXM5).

- Add the --tensor-parallel-size flag to your vLLM command, as shown below:

curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install vllm --torch-backend=auto
VLLM_SERVER_DEV_MODE=1 vllm serve nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 \
 --port 8000 \
 --served-model-name nemotron-3-nano \
 --trust-remote-code \
 --enable-sleep-mode \
 --tensor-parallel-size 8

### Benchmarking Nemotron 3 Nano#

You can benchmark Nemotron 3 Nano by using the vllm bench serve command. The
benchmark presented here measures across five complete spin-downs to avoid
caching, and after the GPUs have warmed up. Run the following commands from
your JupyterLab terminal or an SSH terminal connected to your instance:

wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json
vllm bench serve \
 --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 \
 --served-model-name nemotron-3-nano \
 --dataset-name sharegpt \
 --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \
 --num-prompts 10 \
 --trust-remote-code \
 --backend openai-chat \
 --endpoint /v1/chat/completions

To reset the state each time, the benchmark activates sleep mode. This feature
opens up REST endpoints for POST /sleep?level=1 and
POST /wake_up?tags=weights on your server. For example, to engage sleep
mode level 1:

curl -X POST 'http://localhost:8000/sleep?level=1'

Using sleep level 1 ensures that weights are offloaded to CPU RAM and that the
KV cache is discarded.

Token throughput on a 1x B200 (180 GB SXM6) instance:

 | 
 | Tokens per second

 | Output generation
 | 610.84 ± 45.38

 | Total (input & output)
 | 918.01 ± 68.20

Fine-grained numbers:

 | 
 | Mean (ms)
 | P99 (ms)

 | Time to first token
 | 351.40 ± 98.25
 | 254.80 ± 65.98

 | Time per output token
 | 6.37 ± 0.32
 | 8.86 ± 2.62

 | Inter-token latency
 | 5.63 ± 0.15
 | 7.6 ± 0.17

## Next steps#

- Download the Nemotron 3 Nano weights on Hugging Face.

 Back to top
