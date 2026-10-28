# Install TensorFlow & PyTorch for the RTX 3090, 3080, 3070

Source: https://lambda.ai/blog/install-tensorflow-and-pytorch-on-rtx-30-series

Skip to main content

# Install TensorFlow & PyTorch for the RTX 3090, 3080, 3070

 August 10, 2021

 (Updated on July 6, 2023)

 • 2 min read

This post shows you how to install TensorFlow & PyTorch (and all dependencies) in under 2 minutes using Lambda Stack, a freely available Ubuntu 20.04 APT package created by Lambda (we design deep learning workstations & servers and run a public GPU Cloud) 

### What will be installed 

- TensorFlow v2.5.0 
 
- PyTorch v1.9.0 
 
- CUDA v11.1 
 
- cuDNN v8.2.1 
 
- Dependencies and other frameworks like Caffe and Theano 

### System requirements 

- An NVIDIA GPU. Supported GPUs include RTX 3090, RTX 3080 Ti, RTX 3080, RTX 3070 Ti, RTX 3070, RTX 3060 Ti, RTX 3060, RTX 3050 Ti, RTX 3050, RTX A6000, RTX A5000, RTX A4000, RTX 8000, RTX 6000, RTX 5000, RTX 4000, RTX 2080 Ti, RTX 2080 SUPER, RTX 2080, RTX 2070 SUPER, RTX 2070, RTX 2060. 
 
- Ubuntu 20.04 LTS (Focal Fossa) 

### Install Lambda Stack for a desktop 

LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && sudo apt-get install -y lambda-stack-cuda

Reboot your machine. 

### Install Lambda Stack for a server 

LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && \
sudo apt-get --yes upgrade && \
sudo apt-get install --yes --no-install-recommends lambda-server && \
sudo apt-get install --yes --no-install-recommends nvidia-headless-470 && \
sudo apt-get install --yes --no-install-recommends lambda-stack-cuda

Reboot your machine. 

### Start using TensorFlow/PyTorch 

$ python
>>> import tensorflow
>>> tensorflow.__version__
'2.5.0'
>>> import torch
>>> torch.__version__
'1.8.1'

### Manage your TensorFlow/PyTorch installation 

If a new version of PyTorch, TensorFlow, CUDA, cuDNN is released, simply run: 

sudo apt-get update && sudo apt-get dist-upgrade

Reboot your machine. 

### Interested in a GPU workstation, server, or cloud instance? 

- Call us at +1 (866) 711-2025. 
 
- Email us at sales@lambdalabs.com. 
 
- Browse our GPU workstations, GPU servers, or GPU cloud instances. 

## AUTHORED BY

 Michael Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
