# NVIDIA NGC Tutorial: Run a PyTorch Docker Container using nvidia-container-toolkit on Ubuntu

Source: https://lambda.ai/blog/nvidia-ngc-tutorial-run-pytorch-docker-container-using-nvidia-container-toolkit-on-ubuntu

Skip to main content

# NVIDIA NGC Tutorial: Run a PyTorch Docker Container using nvidia-container-toolkit on Ubuntu

 July 19, 2021

 (Updated on July 24, 2023)

 • 2 min read

This tutorial shows you how to install Docker with GPU support on Ubuntu Linux. To get GPU passthrough to work, you'll need docker, nvidia-container-toolkit, Lambda Stack, and a docker image with a GPU accelerated library.

### 1) Install Lambda Stack

LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && sudo apt-get install -y lambda-stack-cuda
# If you've never installed the NVIDIA drivers before, you need to reboot
# sudo reboot

### 2) Install Docker & nvidia-container-toolkit

You may need to remove any old versions of docker before this step.

sudo apt-get install -y docker.io nvidia-container-toolkit

If you run into a bad launch status with the docker service, you can restart it with:

sudo systemctl daemon-reload
sudo systemctl restart docker

### 3) Pull a container from NVIDIA NGC

You can choose any container you want from https://ngc.nvidia.com/catalog.

sudo docker pull nvcr.io/nvidia/pytorch:21.06-py3

### 4) Start an interactive session with the new container

We will be passing in the data folder that exists in the local directory. Note the use of pwd

as part of the path, you need to specify absolute paths for the folder mount to work.

sudo docker run --gpus all -it --rm -v `pwd`/data:/data/ nvcr.io/nvidia/pytorch:21.06-py3

This will mount the folder located at $PWD/data into /data within the container.

### That's it

You've successfully downloaded and run a GPU accelerated Docker container from the NVIDIA NGC container registry. This tutorial applies to any GPU enabled container in any registry.

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
