# Lambda Stack AI Software for Deep Learning & Machine Learning

Source: https://lambda.ai/lambda-stack-deep-learning-software

Skip to main content

# Lambda Stack: Deep Learning Software for Ubuntu

Lambda Stack is a curated set of software packages widely used in machine learning and deep learning. Each package is tested for compatibility and interoperability across all Lambda systems and architectures, including the latest NVIDIA HGX B200 and H200 SXM GPUs.

- 

- 

- 

- 

- 

## Supported packages

Installation

## Installing Lambda Stack

Lambda Stack comes preinstalled with Ubuntu on all Lambda products, including 1-Click Clusters and Instances. It can also be installed on non-Lambda servers and workstations running Ubuntu using the Lambda Stack Install Script (licensed under BSD-3-Clause):

01

### Non-interactive installations

For non-interactive installations, such as on servers, run:

wget -nv -O- https://lambda.ai/install-lambda-stack.sh | 
I_AGREE_TO_THE_CUDNN_LICENSE=1 sh -

Note: You must read and agree to the cuDNN license agreement before running the non-interactive installation command.

02

### Interactive installations

For interactive installations, such as on workstations, run:

wget -nv -O- https://lambda.ai/install-lambda-stack.sh | sh - 
sudo reboot

Note: The installation script automatically detects your system’s hardware and installs the appropriate drivers and firmware, including NVIDIA Fabric Manager for NVSwitch-based systems.

## Lambda Stack in Python virtual environments

Once Lambda Stack is installed — either preinstalled or manually — you can access its packages from within a Python virtual environment:

python3 -m venv --system-site-packages <VIRTUAL-ENVIRONMENT-NAME>

source <VIRTUAL-ENVIRONMENT-NAME>/bin/activate

## Running GPU-accelerated Docker containers

Since Lambda Stack includes the NVIDIA Container Toolkit, you can run GPU-accelerated containers immediately — no additional setup required.

Check out some of our tutorials using GPU-accelerated containers:

- Using Multi-Instance GPU (MIG)

- Serving the Llama 3.1 8B and 70B models on Lambda Cloud on-demand instances

- Running DeepSeek-R1 70B using Ollama

## Upgrading Lambda Stack

Run this command and all of your AI software, from PyTorch® to CUDA, will be updated. Like magic.

sudo apt update && sudo apt dist-upgrade

## Current package versions

 | Package | Version | License
 | python3-torch-cuda | 2.7.0+ds | License
 | python3-tensorflow-cuda | 2.19.0 | License
 | python3-keras | 3.10.0 | License
 | python3-jax-cuda | 0.6.0 | License
 | python3-triton-cuda | 3.3.0+llvm20.1.2 | License
 | nvidia-cuda-toolkit | 12.8.93~12.8.1 | License
 | libnccl2 | 2.26.2 | License
 | nvidia-container-toolkit | 1.18.1 | License

## Everyone loves Lambda Stack

Used by the F500, research labs, and the Department of Defense. Everything we ship comes pre-installed with Lambda Stack. It’s loved by thousands of Lambda customers.

## Ready to get started?

Create a cloud account to launch an instance today.
Launch GPU instance
