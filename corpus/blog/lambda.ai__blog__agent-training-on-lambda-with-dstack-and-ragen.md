# Partner Spotlight: Orchestrating large-scale agent training on Lambda with dstack and RAGEN

Source: https://lambda.ai/blog/agent-training-on-lambda-with-dstack-and-ragen

Skip to main content

# Partner Spotlight: Orchestrating large-scale agent training on Lambda with dstack and RAGEN

 June 5, 2025

 (Updated on November 5, 2025)

 • 7 min read

Lambda + dstack: Empowering your ML team with rock-solid infrastructure for distributed reasoning agent training

Reasoning agents are among the most sought-after LLM use cases, automating complex tasks across domains. The most powerful models remain proprietary, limiting access and research. Training these agents requires serious resources. With Lambda’s 1-Click Clusters and dstack’s orchestration, your team spends less time on setup and more on building. In this blog, we walk you through scaling multi-turn reinforcement learning training with RAGEN on Lambda’s 1CC using dstack, making open-source reasoning agents accessible at scale.

While vanilla GRPO/PPO excels at single–turn tasks, it’s observed that it struggles with multi–turn agent fine-tuning. Even after prefixing dialogues into longer inputs, yields wildly oscillating metrics (reward, reward_std, loss, KL) and fails to converge on multi-step interactions ​ as shown below.

#### Reinforcement Learning with RAGEN

RAGEN is a reinforcement learning framework for training large language models as reasoning agents in complex, multi-turn environments. Designed to improve agent reliability and performance, RAGEN tackles challenges like overfitting to local rewards and misaligned reasoning. It introduces fine-grained reward signals that help guide agents toward more consistent, goal-driven behavior.

RAGEN natively treats each state as the full tokenized history and optimizes cumulative rewards over K-turn trajectories, and its StarPO-S variant further stabilizes learning through trajectory-level filtering, KL removal, and asymmetric clipping.

RAGEN’s variance-based prompt filtering keeps training focused on informative, uncertain cases so the agent continues to explore rather than collapse into rote behavior.

Under the hood, RAGEN uses verl, flexible, efficient and production-ready RL training library, and Ray, a robust ML library for distributed training. Compared to SFT, RL requires significantly more resources. This is why being able to run training across a cluster is crucial.

While Ray is a powerful framework for distributed processing, it’s rather low-level. In this blog, we explore how Ray can be used via dstack.

#### dstack and Lambda 1CC

dstack is an open-source container orchestration built specifically for ML teams. It simplifies GPU provisioning and workload orchestration, providing a streamlined alternative to Kubernetes and Slurm.

RAGEN includes built-in simulators like Sokoban, WebShop, and FrozenLake for on-policy rollouts and multi-turn evaluation, along with a modular API for custom text environments. In our example, we train an agent with Qwen/Qwen2.5-7B-Instruct with a SimpleSokoban environment.

For training our agent, we use Lambda’s 1CC with 16x NVIDIA HGX H100 GPUs.

While dstack supports automatic GPU provisioning in Lambda’s Public Cloud, using Lambda’s 1CC or Private Cloud requires accessing these clusters through dstack’s SSH fleets.

Now, we’ll walk you through the steps of using RAGEN for fine-tuning a reasoning agent on a Lambda’s 1CC with dstack.

#### dstack SSH fleets

Creating an SSH fleet is straightforward. Inside your repo, define the following lambda-h100-fleet.dstack.yml file:

type: fleet
name: lambda-h100-fleet

ssh_config:
  user: ubuntu
  identity_file: ~/.ssh/id_rsa
  hosts:
    - lambda-cluster-node-001
    - lambda-cluster-node-002
  proxy_jump:
    hostname: 192.222.48.90
    user: ubuntu
    identity_file: ~/.ssh/id_rsa

placement: cluster

Under hosts, we list the hostnames of the GPU nodes. Under proxy_jump, we specify the hostname of the head node along with the private SSH key.

Now, go ahead and apply the fleet configuration:

$ dstack apply -f lambda-h100-fleet.dstack.yml

After you run the dstack apply command, you’ll see that dstack created the corresponding fleet that now can be used for running dev environments, tasks, and services.

#### NCCL tests

In order to test the cluster and its interconnect speed, you can run nccl-tests via a dstack task:

$ dstack apply -f nccl-tests.dstack.yml

See the NCCL tests example for the source code of nccl-tests.dstack.yml

#### Ray with dstack

dstack tasks allow you to run any distributed workload directly using torch run, accelerate, or other distributed frameworks. However, to use Ray with dstack, you need to launch a Ray cluster as a task before submitting Ray jobs:

type: task
name: ray-ragen-cluster

nodes: 2

env:
- WANDB_API_KEY
image: whatcanyousee/verl:ngc-cu124-vllm0.8.5-sglang0.4.6-mcore0.12.0-te2.2
commands:
  - wget -O miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  - bash miniconda.sh -b -p /workflow/miniconda
  - eval "$(/workflow/miniconda/bin/conda shell.bash hook)"
  - git clone https://github.com/RAGEN-AI/RAGEN.git
  - cd RAGEN
  - bash scripts/setup_ragen.sh
  - conda activate ragen
  - cd verl
  - pip install --no-deps -e .
  - pip install hf_transfer hf_xet
  - pip uninstall -y ray
  - pip install -U "ray[default]"
  - |
    if [ $DSTACK_NODE_RANK = 0 ]; then 
        ray start --head --port=6379;
    else
        ray start --address=$DSTACK_MASTER_NODE_IP:6379
    fi

# Expose Ray dashboard port
ports:
  - 8265

resources:
  gpu: 80GB:8
  shm_size: 128GB

# Save checkpoints on the instance
volumes:
  - /checkpoints:/checkpoints

This dstack task launches a Ray cluster with the RAGEN environment. Run this task using the same dstack apply command:

$ dstack apply -f ray-ragen-cluster.dstack.yml

When the task exposes ports, the dstack apply command automatically forwards these ports to the current machine. In our case, this makes the Ray's dashboard available locally at localhost:8265.

#### Training run

This means, we can submit Ray tasks from our local machine.

$ pip install ray
$ RAY_ADDRESS=http://localhost:8265
$ ray job submit \
  -- bash -c "\
    export PYTHONPATH=/workflow/RAGEN; \
    cd /workflow/RAGEN; \
    /workflow/miniconda/envs/ragen/bin/python train.py \
      --config-name base \
      system.CUDA_VISIBLE_DEVICES=[0,1,2,3,4,5,6,7] \
      model_path=Qwen/Qwen2.5-7B-Instruct \
      trainer.experiment_name=agent-fine-tuning-Qwen2.5-7B \
      trainer.n_gpus_per_node=8 \
      trainer.nnodes=2 \
      micro_batch_size_per_gpu=2 \
      trainer.default_local_dir=/checkpoints \
      trainer.save_freq=50 \
      actor_rollout_ref.rollout.tp_size_check=False \
      actor_rollout_ref.rollout.tensor_model_parallel_size=4"

#### GPU metrics

While the training is done, you can observe hardware metrics via dstack’s control plane:

Once the Ray cluster is not needed anymore, you can stop it via dstack stop:

$ dstack stop ray-ragen-cluster

Training recovery

Because our Ray cluster task mounts the /checkpoints folder inside the containers to the cluster instance as an instance volume, we can recover training in case of a failure or cluster restart.

After walking through how to launch a dstack SSH fleet on Lambda’s 1CC instances, provision a multi-node Ray cluster, and run distributed training with RAGEN, you can now extend the same workflow to other frameworks. If your framework doesn’t rely on Ray, you can simply skip the Ray cluster step and run distributed training directly.

To dive deeper, check out the Clusters guide. dstack provides a streamlined alternative to Kubernetes and Slurm for teams running on Lambda, with native support for training workloads, development environments, and persistent services.

#### What’s next?

With Lambda and dstack handling infrastructure complexity, your team can push the boundaries of reasoning agents without setup headaches. Scale your experiments confidently on Lambda’s powerful clusters with dstack.

- 

Sign up on Lambda to access GPU clusters tailored to your needs.

- 

Explore the RAGEN and verl framework repos.

- 

Check out dstack's repository.

## AUTHORED BY

 dstack

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
