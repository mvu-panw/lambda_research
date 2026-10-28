# Orchestrating AI workloads with dstack - Lambda Docs

Source: https://docs.lambda.ai/education/scheduling-and-orchestration/orchestrating-workloads-with-dstack/

Skip to content

# Orchestrating AI workloads with dstack#

## Introduction#

dstack is an open-source
alternative to Kubernetes and Slurm, built for orchestrating containerized AI
and ML workloads. It simplifies the development, training, and deployment of AI
models.

With dstack, you use YAML configuration files to define how your applications
run. These files specify which
Lambda On-Demand Cloud
resources to use and how to start your workloads. You can run one-off jobs,
set up full-featured remote development environments that open in VS Code, or
deploy persistent services that expose APIs for your models.

In this tutorial, you'll learn how to:

- Run a
 Task
 that evaluates an LLM's ability to solve multiplication problems.

- Set up a remote
 development environment
 for use with VS Code.

- Launch a
 Service
 that serves an LLM via an OpenAI-compatible API endpoint.

- Create an
 SSH Fleet
 on a
 Lambda 1-Click Cluster.

## Prerequisites#

All of the instructions in this tutorial should be followed on your local
machine, not on an on-demand instance.

Before you begin, make sure the following tools are installed:

- python3

- python3-pip

- git

- curl

- jq

On Ubuntu, you can install these packages by running:

sudo apt update && sudo apt install -y python3 python3-pip git curl jq

You also need a
Lambda Cloud API key.

## Install and start the dstack server#

Before you can use dstack to run Tasks, Services, or development environments,
you need to install and start the local dstack server:

- 

Install dstack:

pip install -U "dstack[lambda]"

- 

Create a directory for the dstack server and navigate to it:

mkdir -p -m 700 ~/.dstack/server && cd ~/.dstack/server

- 

Create a
 server configuration
 file named config.yml with the following contents. Replace <API-KEY> with
 your Cloud API key:

projects:
 - name: main
 backends:
 - type: lambda
 creds:
 type: api_key
 api_key: <API-KEY>

- 

Start the dstack server:

dstack server

You should see output similar to:

[15:36:35] INFO Applying ~/.dstack/server/config.yml...
[15:36:36] INFO dstack._internal.server.services.plugins:77 Found not enabled builtin plugin rest_plugin. Plugin will not be loaded.
 INFO Configured the main project in ~/.dstack/config.yml
 INFO The admin token is <ADMIN-TOKEN>
 INFO The dstack server 0.19.15 is running at http://127.0.0.1:3000

Note

You can safely ignore any warnings about plugins that are not enabled.

## Initialize a dstack repo for the tutorial examples#

To run the examples in this tutorial, you'll need to
initialize a dstack repo
in a separate directory:

- 

In a new terminal window or tab (so the dstack server can keep running),
 create a directory for the examples and navigate to it:

mkdir ~/lambda-dstack-examples && cd ~/lambda-dstack-examples

- 

Initialize the directory as a dstack repo:

dstack init

When the repo initializes successfully, the message OK appears in your terminal output.

## Submit a dstack Task that tests a language model's multiplication skills#

In this example, you submit a Task that tests a language model's ability to
solve multiplication problems. The Task:

- Provisions an on-demand instance.

- Downloads the
 vLLM Docker image
 and launches a container.

- Downloads the
 eval_multiplication.py
 Python script.

- Runs the script to evaluate the
 Qwen/Qwen2.5-0.5B-Instruct
 model.

- 

In the lambda-dstack-examples directory you created earlier, create a file
 named eval-multiplication-task.dstack.yml containing the following:

type: task
name: eval-multiplication
image: vllm/vllm-openai:v0.9.1
commands:
 - curl -L "$SCRIPT_URL" -o eval_multiplication.py
 - python3 eval_multiplication.py "$MODEL_ID" --stdout
env:
 - MODEL_ID=Qwen/Qwen2.5-0.5B-Instruct
 - SCRIPT_URL=https://docs.lambda.ai/assets/code/eval_multiplication.py
resources:
 gpu:
 count: 1
idle_duration: 30m

- 

Run the Task:

dstack apply -f eval-multiplication-task.dstack.yml

You should see output similar to:

 Project main
 User admin
 Configuration eval-multiplication-task.dstack.yml
 Type task
 Resources cpu=2.. mem=8GB.. disk=100GB.. gpu:1
 Spot policy on-demand
 Max price -
 Retry policy -
 Creation policy reuse-or-create
 Idle duration 30m
 Max duration -
 Reservation -

 # BACKEND RESOURCES INSTANCE TYPE PRICE
 1 lambda (us-east-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 gpu_1x_a10 $0.75 idle
 2 lambda (us-east-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 gpu_1x_a10 $0.75
 3 lambda (us-west-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 gpu_1x_a10 $0.75
 ...
 Shown 3 of 120 offers, $3.29max

Submit the run eval-multiplication? [y/n]:

- 

Submit the run. dstack provisions a new on-demand instance and then starts vLLM on the instance.

From here, you can view vLLM's output as it completes the rest of the Task.
In the example below, the Task completed successfully with an accuracy of
0.6490:

Adding requests: 100% 1000/1000 [00:00<00:00, 5296.09it/s]
Processed prompts: 100% 1000/1000 [00:12<00:00, 81.39it/s, est. speed input: 1292.21 toks/s, output: 12495.35 toks/s]
Model Qwen/Qwen2.5-0.5B-Instruct accuracy: 0.6490

## Set up a remote VS Code development environment#

In this example, you create a remote development environment that you can
access using VS Code on your computer.

- 

In the lambda-dstack-examples directory created earlier, create a file
 named vs-code-dev-environment.dstack.yml with the following contents:

type: dev-environment
name: vs-code-dev-environment
python: "3.11"
ide: vscode
resources:
 gpu:
 count: 1
idle_duration: 30m

- 

Apply the configuration:

dstack apply -f vs-code-dev-environment.dstack.yml

You should see output similar to the following:

 Project main
 User admin
 Configuration vs-code-dev-environment.dstack.yml
 Type dev-environment
 Resources cpu=2.. mem=8GB.. disk=100GB..
 Spot policy on-demand
 Max price -
 Retry policy -
 Creation policy reuse-or-create
 Idle duration 30m
 Max duration -
 Inactivity duration -
 Reservation -

 # BACKEND RESOURCES INSTANCE TYPE PRICE
 1 lambda (us-east-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 gpu_1x_a10 $0.75 idle
 2 lambda (us-east-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 gpu_1x_a10 $0.75
 3 lambda (us-west-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 gpu_1x_a10 $0.75
 ...
 Shown 3 of 290 offers, $23.92max

Submit the run vs-code-dev-environment? [y/n]:

- 

Confirm the run. dstack provisions a suitable on-demand instance.

After a few minutes, you should see output like:

vscode provisioning completed (running)
pip install ipykernel...

To open in VS Code Desktop, use link below:

 vscode://vscode-remote/ssh-remote+vscode/workflow

To connect via SSH, use: `ssh vscode`

- 

Click the link to open the development environment in VS Code on your
 desktop.

## Deploy a Service to serve the Qwen2.5 LLM#

In this example, you launch an SGLang server to serve the Qwen2.5 0.5B
Instruct model through an OpenAI-compatible API.

- 

In the lambda-dstack-examples directory you created earlier, create a file
 named sglang-service.dstack.yml with the following contents:

type: service
name: sglang-service
image: lmsysorg/sglang:latest
env:
 - MODEL_ID=Qwen/Qwen2.5-0.5B-Instruct
commands:
 - python3 -m sglang.launch_server
 --model-path $MODEL_ID
 --port 8000
 --trust-remote-code
port: 8000
model: Qwen/Qwen2.5-0.5B-Instruct
auth: false
resources:
 gpu:
 count: 1
idle_duration: 30m

- 

Deploy the Service:

dstack apply -f sglang-service.dstack.yml

- 

Confirm the run to begin provisioning the on-demand instance.

Once provisioning completes, you’ll see output similar to:

 NAME BACKEND RESOURCES PRICE STATUS SUBMITTED
 sglang-service lambda (us-east-1) cpu=30 mem=215GB disk=1504GB A10:24GB:1 $0.75 running 19:03

sglang-service provisioning completed (running)
Service is published at:
 http://127.0.0.1:3000/proxy/services/main/sglang-service/
Model Qwen/Qwen2.5-0.5B-Instruct is published at:
 http://127.0.0.1:3000/proxy/models/main/

After a few moments, you should see logs indicating the server is running:

```text { .no-copy }
[2025-06-25 19:04:01] INFO: Started server process [60]
[2025-06-25 19:04:01] INFO: Waiting for application startup.
[2025-06-25 19:04:01] INFO: Application startup complete.
[2025-06-25 19:04:01] INFO: Uvicorn running on http://127.0.0.1:3000/proxy/services/main/sglang-service/ (Press CTRL+C to quit)
[2025-06-25 19:04:02] INFO: 127.0.0.1:41778 - "GET /get_model_info HTTP/1.1" 200 OK
[2025-06-25 19:04:02] Prefill batch. #new-seq: 1, #new-token: 6, #cached-token: 0, token usage: 0.00, #running-req: 0, #queue-req: 0
[2025-06-25 19:04:04] INFO: 127.0.0.1:41792 - "POST /generate HTTP/1.1" 200 OK
[2025-06-25 19:04:04] The server is fired up and ready to roll!
```

- 

Test the Service by sending a chat request:

curl -sS http://127.0.0.1:3000/proxy/services/main/sglang-service/v1/chat/completions \
 -H 'Content-Type: application/json' \
 -d '{
 "model": "Qwen/Qwen2.5-0.5B-Instruct",
 "messages": [
 {
 "role": "user",
 "content": "Explain artificial neural networks in five sentences."
 }
 ]
 }' | jq -r '.choices[] | select(.message.role == "assistant") | .message.content'

You should see output similar to:

Artificial neural networks, also known as artificial intelligence (AI) systems, are a type of machine learning model inspired by biological neural networks. These systems consist of interconnected nodes or "neurons," known as nodes, that process and analyze data to make decisions or predictions. The nodes can be trained to recognize patterns in data, classify objects, or perform other tasks based on the input it receives. Neural networks can be used for a wide range of applications, including image and speech recognition, language translation, fraud detection, and predictive analytics. The architecture of a neural network typically includes layers of nodes that are connected to each other, with each node's output influencing the next layer's input. Artificial neural networks are increasingly being used in a variety of industries, from healthcare and finance to autonomous driving and robotics.

## Create an SSH Fleet on a 1-Click Cluster#

You can use dstack to define an SSH Fleet that runs on a Lambda 1-Click Cluster.
This is useful for orchestrating distributed workloads that require low-latency
networking.

Tip

dstack can also be used to create a
Cloud Fleet
of on-demand instances. However, this Cloud Fleet won't benefit from 1-Click
Clusters' InfiniBand (RDMA) fabric.

To create an SSH Fleet, define a configuration like the following and apply it
with the dstack apply -f command. Replace <PATH-TO-SSH-PRIVATE-KEY>,
<CLUSTER-NAME>, and <HEAD-NODE-IP> with your actual values for each
placeholder:

type: fleet
name: lambda-1cc-h100-fleet
ssh_config:
 user: ubuntu
 identity_file: <PATH-TO-SSH-PRIVATE-KEY>
 hosts:
 - <CLUSTER-NAME>-node-001
 - <CLUSTER-NAME>-node-002
 # Add more nodes as needed
 proxy_jump:
 hostname: <HEAD-NODE-IP>
 user: ubuntu
 identity_file: <PATH-TO-SSH-PRIVATE-KEY>
placement: cluster

For a real-world example of using an SSH Fleet, see
Orchestrating large-scale agent training on Lambda with dstack and RAGEN
in the Lambda Deep Learning Blog.

## Next Steps#

- Visit the
 dstack documentation
 for more configuration options.

- Learn more about Lambda's orchestration solutions.

 Back to top
