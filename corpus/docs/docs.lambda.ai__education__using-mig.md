# Using Multi-Instance GPU (MIG) - Lambda Docs

Source: https://docs.lambda.ai/education/using-mig/

Skip to content

# Using Multi-Instance GPU (MIG)#

See our video tutorial on using Multi-Instance GPU (MIG).

NVIDIA Multi-Instance GPU,
or MIG, allows you to partition your GPUs into isolated instances. MIG enables
you to run simultaneous workloads on a single GPU. For example, you can run
inference on multiple models at the same time.

Tip

See NVIDIA's MIG User Guide to learn more about MIG.

In this tutorial, you'll learn how to:

- Enable MIG on a 1x GH200 on-demand instance.

- Partition the GH200 GPU into two instances.

- Run a vLLM Docker container on each instance, with each container serving a
 different model.

- Interact with the two different models.

## Prerequisites#

For this tutorial, you'll need a:

- 1x GH200 on-demand instance. You can launch the 1x GH200 on-demand instance
 from the console or using the Cloud API. See
 Creating and managing instances > Launching instances.

- Hugging Face User Access Token.

## Enable MIG on your on-demand instance#

- 

SSH into your 1x GH200 on-demand instance.

- 

Enable MIG:

sudo nvidia-smi -mig 1

You'll see:

Enabled MIG Mode for GPU 00000000:DD:00.0
All done.

## Partition the GH200 GPU into two instances#

- 

Partition the GH200 GPU into two instances (MIG devices):

sudo nvidia-smi mig -cgi 9,9 -C

You'll see:

Successfully created GPU instance ID 2 on GPU 0 using profile MIG 3g.48gb (ID 9)
Successfully created compute instance ID 0 on GPU 0 GPU instance ID 2 using profile MIG 3g.48gb (ID 2)
Successfully created GPU instance ID 1 on GPU 0 using profile MIG 3g.48gb (ID 9)
Successfully created compute instance ID 0 on GPU 0 GPU instance ID 1 using profile MIG 3g.48gb (ID 2)

- 

Verify that the GH200 GPU's 96 GB of VRAM has been partitioned into two
 instances (MIG devices):

nvidia-smi

The output should show two devices, each with 48 GB of VRAM:

Fri Dec 6 06:46:18 2024
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.127.05 Driver Version: 550.127.05 CUDA Version: 12.4 |
|-----------------------------------------+------------------------+----------------------+
| GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC |
| Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. |
| | | MIG M. |
|=========================================+========================+======================|
| 0 NVIDIA GH200 480GB On | 00000000:DD:00.0 Off | On |
| N/A 31C P0 86W / 700W | 76MiB / 97871MiB | N/A Default |
| | | Enabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| MIG devices: |
+------------------+----------------------------------+-----------+-----------------------+
| GPU GI CI MIG | Memory-Usage | Vol| Shared |
| ID ID Dev | BAR1-Usage | SM Unc| CE ENC DEC OFA JPG |
| | | ECC| |
|==================+==================================+===========+=======================|
| 0 1 0 0 | 38MiB / 47616MiB | 60 0 | 3 0 3 0 3 |
| | 0MiB / 0MiB | | |
+------------------+----------------------------------+-----------+-----------------------+
| 0 2 0 1 | 38MiB / 47616MiB | 60 0 | 3 0 3 0 3 |
| | 0MiB / 0MiB | | |
+------------------+----------------------------------+-----------+-----------------------+

+-----------------------------------------------------------------------------------------+
| Processes: |
| GPU GI CI PID Type Process name GPU Memory |
| ID ID Usage |
|=========================================================================================|
| No running processes found |
+-----------------------------------------------------------------------------------------+

## Run a vLLM Docker container on each instance#

- 

Pull the
 drikster80/vllm-gh200-openai
 Docker image:

sudo docker pull drikster80/vllm-gh200-openai

Note

The drikster80/vllm-gh200-openai Docker image is identical to the
official vllm/vllm-openai
image, except support for GH200 has been added.

- 

Start a tmux session:

tmux

- 

Launch a vLLM container serving the
 Nous Research's Hermes 3
 model:

sudo docker run \
 --gpus '"device=0:0"' \
 --ipc=host \
 -p 8000:8000 \
 drikster80/vllm-gh200-openai --model NousResearch/Hermes-3-Llama-3.1-8B --disable-log-requests

Note

Note the docker run option --gpus '"device=0:0"'. This option
specifies that the container should be launched using GPU 0, MIG
device 0.

Note also the docker run option -p 8000:8000. This option specifies
that the container should serve the NousResearch/Hermes-3-Llama-3.1-8B
model on port 8000.

The model is being served once you see:

INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

- 

Press Ctrl + B, then press % to create a new vertical pane in
 the tmux window. Then, launch a vLLM container serving the
 Meta Llama 3.1 8B Instruct
 model by running the command below.

Replace <HF-TOKEN> with your Hugging Face User Access Token.

sudo docker run \
 --gpus '"device=0:1"' \
 --ipc=host \
 -p 8001:8000 \
 -e "HUGGING_FACE_HUB_TOKEN=<HF-TOKEN>" \
 drikster80/vllm-gh200-openai --model meta-llama/Meta-Llama-3.1-8B-Instruct --disable-log-requests

Note

Note the differences between this docker run command and the previous
docker run command. This docker run command has the option --gpus
'"device=0:1"', specifying that this container should be launched using
GPU 0, MIG device 1.

This docker run command also has the option -p 8001:8000, specifying
that this container should serve the
meta-llama/Meta-Llama-3.1-8B-Instruct model on port 8001.

Again, the model is being served once you see:

INFO: Started server process [1]
INFO: Waiting for application startup.
INFO: Application startup complete.
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)

## Interact with the two different models#

- 

Press Ctrl + B, then press C to open a new tmux window.

- 

Install jq:

sudo apt -y install jq

- 

Submit an example prompt to the NousResearch/Hermes-3-Llama-3.1-8B model:

curl http://localhost:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
 "prompt": "What is the origin of the universe?",
 "model": "NousResearch/Hermes-3-Llama-3.1-8B",
 "temperature": 0.0,
 "max_tokens": 1000,
 "min_tokens": 1000
 }' | jq .

You'll see output similar to:

{
 "id": "cmpl-791ae8f8c7344f7398559bf02147c173",
 "object": "text_completion",
 "created": 1733513045,
 "model": "NousResearch/Hermes-3-Llama-3.1-8B",
 "choices": [
 {
 "index": 0,
 "text": " How did it all begin? These are questions that have puzzled scientists and philosophers for centuries. […]",
 "logprobs": null,
 "finish_reason": "length",
 "stop_reason": null,
 "prompt_logprobs": null
 }
 ],
 "usage": {
 "prompt_tokens": 9,
 "total_tokens": 1009,
 "completion_tokens": 1000,
 "prompt_tokens_details": null
 }
}

- 

Submit an example prompt to the meta-llama/Meta-Llama-3.1-8B-Instruct
 model:

curl http://localhost:8001/v1/completions \
 -H "Content-Type: application/json" \
 -d '{
 "prompt": "What is the origin of the universe?",
 "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
 "temperature": 0.0,
 "max_tokens": 1000,
 "min_tokens": 1000
 }' | jq .

You'll see output similar to:

{
 "id": "cmpl-aa3f506d63b04b188ebf9b33f3b8290f",
 "object": "text_completion",
 "created": 1733513198,
 "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
 "choices": [
 {
 "index": 0,
 "text": " The origin of the universe is a topic of ongoing research and debate in the fields of cosmology and astrophysics. […]",
 "logprobs": null,
 "finish_reason": "length",
 "stop_reason": null,
 "prompt_logprobs": null
 }
 ],
 "usage": {
 "prompt_tokens": 9,
 "total_tokens": 1009,
 "completion_tokens": 1000,
 "prompt_tokens_details": null
 }
}

## Next steps#

- Check out the
 Lambda Inference API
 for serverless access to LLMs.

- Learn how to serve LLMs on a Kubernetes cluster using KubeAI.

 Back to top
