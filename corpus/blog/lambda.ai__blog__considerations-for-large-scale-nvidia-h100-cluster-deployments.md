# Considerations for Large-Scale NVIDIA H100 Cluster Deployments

Source: https://lambda.ai/blog/considerations-for-large-scale-nvidia-h100-cluster-deployments

Skip to main content

# Considerations for Large-Scale NVIDIA H100 Cluster Deployments

 July 13, 2023

 (Updated on November 22, 2023)

 • 4 min read

## Introduction

Pretraining LLM and Generative AI models from scratch typically consumes at least 248 GPUs. Building the infrastructure to support hundreds or thousands of GPUs requires unique design, hosting, and support considerations. As you work with trusted providers, like Lambda, to deploy a solution to meet your needs, these are some of the questions you should ask and be ready to answer.

## Questions For The ML Team

A few pieces of information are important for your team to gather as you consider building or partnering to build a GPU cluster for your training needs. Each of these can have a significant impact on the cost and design of the solution.

### GPU Selection and Quantity

- Do you intend to train various sizes of models, or are all the models consistent sizes?

- Will the cluster be used to train a single model, or multiple models concurrently? If multiple, does the system need to prioritize any?

- If multi-user, does the system need to prioritize training jobs?

- Do any of the models benefit from distributed training? (Most LLMs do)

### Data

- What is the largest size of the shared data needed for all active training jobs?

- Can the data be distributed to each GPU or does it need to be read concurrently from a single mount point?

- What is the total amount of data needed for training?

- Do you need systems dedicated to data preprocessing as part of the solution?

### Consumption

- Does my team expect to have a long idle time between training jobs or will the cluster be fully consumed through its life?

- For single model development, what is the expectation for the number of months needed to complete training the model?

- Does the training environment need to be closely integrated to the production inferencing solution?

### Tooling

- Does my company require a certain OS type and version?

- Does my company require specific libraries or tools to be installed for security or management?

- What tools does the team use for data access and engineering, model management, model tracking, and deployment?

## Questions For The Provider(s)

Once you understand the use cases mentioned above, you are ready to engage with a provider to help you build your solution. There are three primary models for large-scale deployments, each with their own financial considerations:

- On-premises: You have data centers with sufficient space, power and cooling supporting 44kW/rack, and expertise to handle these large solutions and benefit from owning the gear and having it adjacent to other technologies.

- Hosted: You don’t have data centers that can handle the requirements, but still benefit from owning the solution.

- Cloud: You prefer to rent the solution from a provider with domain expertise that maintains the solution.

For each of these, you should understand your selected provider’s capabilities in designing, delivering, and optionally supporting the solution for you. The following questions may help you in the selection process:

- How many GPUs have you deployed?

Companies that haven’t deployed thousands of GPUs likely don’t have the design or support experience you need.

- What is the size of your typical and largest connected cluster?

LLM and Generative models typically consume at least 248 GPUs. Many consume over 2000. Specific architectures are needed to scale beyond 248 GPUs.

- What technology do you use to maximize the throughput of the GPU fabric?

The H100 benefits from having a non-blocking, SHARPv3 enabled, NDR fabric to share model weights with other GPUs. The performance over other fabric choices, like RoCE or partially-non-blocking can be as much as 40% which slows your time to market.

- What technology do you use to ensure that the GPUs aren’t waiting for data?

When data must be concurrently read by many GPUs, the latency, IOPS, protocols, and line-rate of the connection must be carefully architected to prevent bottlenecks.

- What support options do you provide to ensure the health and up-time of the solution?

These large-scale clusters degrade quickly when even a single GPU is unavailable. Ensuring your provider can quickly assess and correct problems will protect your investment.

- What is the strength of your supply chain to ensure I get my solution as fast as possible?

The biggest challenge with standing up large-scale clusters is supply chain lead-times and management. A good provider meets daily with their suppliers to accelerate delivery and repair times.

### Infrastructure Solutions

Lambda is one of only a few providers 100% dedicated to Machine Learning infrastructure solutions. We can help you navigate your own discovery and then provide fully engineered, optimized, and tested solutions to specifically address your needs. Lambda has deployed tens of thousands of GPUs for AI startups, hyperscalers, and Fortune 500 companies. We’d love to show you our answers to your questions and watch your pulse quicken as you consider all you can accomplish when partnering with us.

## AUTHORED BY

 David Hall

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
