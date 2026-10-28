# Orchestration with dstack

Source: https://lambda.ai/dstack

Skip to main content

# Container orchestration for AI teams with dstack

Managing AI workloads with Kubernetes and Slurm can introduce unnecessary complexity. dstack is an open-source container orchestration platform designed to simplify AI development, natively integrated with Lambda’s Instances, 1-Click-Clusters™, and Superclusters.
Read the docs

## Dev environments

Before submitting a training job or deploying a model, the AI team may often want to interactively experiment with code. dstack simplifies this process with dev environments.

It automatically provisions compute, fetches your code, sets up the IDE, and lets you to access it through your desktop IDE.

You can set a maximum inactivity duration to automatically stop unused dev environments, helping AI teams control costs.
Read the docs

## Tasks

Tasks allow the AI team to efficiently and conveniently schedule any kind of jobs either on single nodes or on large clusters.

Tasks may be used to train very complex large models from scratch or to fine-tune them.

dstack automatically provisions compute, uploads the contents of the repo (including your local uncommitted changes) and runs the commands over a single or multiple hosts–while letting you use any open-source frameworks, including PyTorch, HuggingFace, and more.

## Services

Services make it very easy to deploy models as scalable and secure endpoints.

You can use any serving framework of your choice and set up an auto-scaling policy that adjusts the number of replicas dynamically based on demand.

dstack’s control plane includes a playground that can be used with any running model.
Read the docs

## Fleets

Fleets are groups of instances that can be interconnected clusters or standalone hosts.

With dstack, you can provision compute in Lambda’s Instances, or access Lambda’s 1-Click-Clusters and Superclusters.

Fleets enable cost-effective reuse of compute by the AI team for running dev environments, tasks, and services.
Talk to our team

## Leverage open-source

dstack seamlessly integrates with PyTorch, HuggingFace libraries (TGI, Accelerate, PEFT, TRL, etc.), Axolotl, vLLM, NVIDIA Enterprise AI, and more.

If your script works over SSH or locally, you can also run it with dstack—whether you’re involved in development, training, fine-tuning, or deploying models.

You’re also free to use your own Docker image or rely on dstack’s default Docker image when applicable. 
Read the docs

## Ready to build?

Managing AI workloads with Kubernetes and Slurm can introduce unnecessary complexity. dstack is an open-source container orchestration platform designed to simplify AI development. dstack is natively integrated with Lambda.
Read the docs
