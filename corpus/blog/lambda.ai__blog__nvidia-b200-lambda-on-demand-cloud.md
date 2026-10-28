# Introducing Next-Gen Training and Inference at Scale on Lambda Instances with NVIDIA Blackwell

Source: https://lambda.ai/blog/nvidia-b200-lambda-on-demand-cloud

Skip to main content

# Introducing Next-Gen Training and Inference at Scale on Lambda Instances with NVIDIA Blackwell

 August 12, 2025

 (Updated on November 5, 2025)

 • 4 min read

NVIDIA Blackwell GPUs are now available as 8x Lambda Instances On-Demand, featuring the powerful NVIDIA HGX™ B200 in addition to our trusted lineup.

Built for the frontier of AI development, NVIDIA Blackwell instances accelerate training and inference for trillion-parameter foundation models, while maintaining the simplicity and flexibility on-demand users expect. Whether you're training state-of-the-art LLMs or deploying custom fine-tunes in production, NVIDIA HGX™ B200 delivers massive performance gains with a familiar developer-friendly experience.

## Why NVIDIA HGX B200? 

NVIDIA Blackwell GPUs represent a major step ahead of the NVIDIA Hopper generation:

- Up to 2.25x the FP8 throughput of NVIDIA HGX H100

- 3x faster training performance for LLMs

- 15x faster inference throughput for real-time applications

With 180GB of blazing-fast HBM3e memory per GPU and new FP4 support, the NVIDIA Blackwell architecture is tailor-made for modern AI workloads. 

## Now Available On-Demand

Lambda users can instantly launch 8x NVIDIA Blackwell GPUs on-demand and pay only for what you use.

Here’s what you get out of the box:

- 8x NVIDIA Blackwell GPUs

- 1.4 TB of unified GPU memory

- 2900 GiB of system memory

- Starting at $4.99/GPU-hr

## Built for Real Work, Not Just Benchmarks

This isn’t a testbed. It’s production-ready infrastructure for enterprises training frontier-scale models and running high-throughput inference pipelines.

You’ll benefit from:

- Immediate availability on Lambda Cloud, no waitlists or commitments.

- Simplified model hosting: Host your entire model on a single node for minimal latency and maximal throughput.

- Transparent pricing and billing: Usage-based, no surprises

## NVIDIA Blackwell Architectural Innovations
There are six revolutionary technologies inside the new Blackwell architecture that enable organizations to build and run real-time inference on trillion-parameter large language models. Along with being the basis of the world’s most powerful chip, which is packed with 208 billion transistors, Blackwell includes a second-generation Transformer Engine, fifth-generation NVIDIA NVLink™ interconnect, advanced confidential computing capabilities, a dedicated decompression engine, and a RAS Engine that identifies potential faults that may occur early on to minimize downtime. 

#### Quick Code Peek: Training Llama on Lambda's B200 instances with FP16 precision

Here’s what launching a training job on Lambda’s new NVIDIA HGX B200 instances looks like in practice. A simple DeepSpeed-based launch script for training a Llama-style model on 8x Blackwell GPUs with FP16 support.

Start by spinning up 8xB200 instance, access it via CLI in JupyterLab, and follow the steps below: 

Shell

# Activate the virtual training environment
source ~/.venvs/train/bin/activate

# Clone the GitHub repository
git -C ~/transformers remote -v 

# Navigate to the Transformer repo 
cd ~/transformers

# Confirm whether the Python/DeepSpeed virtual environment is being used and that the required libraries were imported
which python; which deepspeed
python -c "import deepspeed, evaluate; print('OK', deepspeed.__version__)"

# Install HuggingFace’s Python package for model evaluation
python -m pip install -U evaluate datasets

# Ensure presence of the DeepSpeed config file
test -f /home/ubuntu/ds_config_b200_fp16.json && echo "DS config found"

# Confirm that the tiny training dataset exists
ls -lh /home/ubuntu/toy.txt

# Launch training with the virtual environment’s DeepSpeed binary
~/.venvs/train/bin/deepspeed --num_gpus=8 \
  --module examples.pytorch.language-modeling.run_clm \
  --model_name_or_path TinyLlama/TinyLlama-1.1B-Chat-v1.0 \
  --train_file /home/ubuntu/toy.txt \
  --validation_split_percentage 1 \
  --do_train \
  --fp16 \
  --per_device_train_batch_size 8 \
  --gradient_accumulation_steps 4 \
  --num_train_epochs 1 \
  --block_size 1024 \
  --output_dir /home/ubuntu/checkpoints/tinyllama-b200-fp16 \
  --deepspeed /home/ubuntu/ds_config_b200_fp16.json

# Verify that the training workload ran successfully by looking for success messages in the last 200 lines 

tail -n 200 -f /home/ubuntu/checkpoints/tinyllama-b200-fp16/runs/*/events* 2>/dev/null || true
ls -l /home/ubuntu/checkpoints/tinyllama-b200-fp16

grep -E "Running training|Saving model checkpoint|Process .* exits successfully" -n training.log 2>/dev/null || true

And here's a matching DeepSpeed config for NVIDIA HGX B200:

JSON

{
  "fp16": { "enabled": true },
  "zero_optimization": { "stage": 2 },
  "gradient_accumulation_steps": 4,
  "train_micro_batch_size_per_gpu": 8,
  "gradient_clipping": 1.0
}

This snippet shows how Lambda’s infrastructure and NVIDIA HGX B200 deliver scalable, cost-efficient LLM training. With 8x Blackwell GPUs and FP16 precision, B200 cuts epoch times by up to 2x versus H100s, powering faster pretraining and fine-tuning with zero hassle.

## How to Get Started

- Head over to Lambda On-Demand Cloud 

- Sign In to your account

- On the instances page, click on Launch Instance.

- Select Instance Type → 8xB200.

- Choose Region → Select Filesystem → Select Firewall Rulesets

- Click on Confirm and launch your instance.

No long term contracts. No paperwork. Just compute.

For teams doing serious LLM work, or looking to do more with less, NVIDIA HGX B200 On-Demand is here to unlock your next milestone.

Start training on your own terms today.

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
