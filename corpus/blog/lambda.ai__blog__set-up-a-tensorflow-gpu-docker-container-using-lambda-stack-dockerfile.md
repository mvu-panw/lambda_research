# Set up a GPU accelerated Docker container using Lambda Stack + Lambda Stack Dockerfiles on Ubuntu 20.04 LTS

Source: https://lambda.ai/blog/set-up-a-tensorflow-gpu-docker-container-using-lambda-stack-dockerfile

Skip to main content

# Set up a GPU accelerated Docker container using Lambda Stack + Lambda Stack Dockerfiles on Ubuntu 20.04 LTS

 February 10, 2019

 (Updated on August 12, 2022)

 • 2 min read

Or, how Lambda Stack + Lambda Stack Dockerfiles = GPU accelerated deep learning containers

 Accelerated Docker Containers with GPUs!

Ever wonder how to build a GPU docker container with TensorFlow or PyTorch in it? In this tutorial, we'll walk you through every step. We provide Dockerfiles for 20.04, 18.04, and 16.04 for the container OS. This tutorial should work for both 20.04 LTS and 18.04 LTS host systems. 

### 1) Install Lambda Stack

LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && sudo apt-get install -y lambda-stack-cuda
sudo reboot

### 2) Install Docker & nvidia-container-toolkit

You may need to remove any old versions of docker before this step.

# Next, install docker & nvidia-container-toolkit
sudo apt-get install -y docker.io nvidia-container-toolkit

### 3) Build an open source Lambda Stack Dockerfile.

# Build a docker image named lambda-stack:20.04
sudo docker build -t lambda-stack:20.04 -f Dockerfile.focal git://github.com/lambdal/lambda-stack-dockerfiles.git

You can ensure this went smoothly by running the sudo docker image list command.

sudo docker image list
REPOSITORY TAG IMAGE ID CREATED SIZE
lambda-stack 20.04 62bb1f0bfe05 About a minute ago 7.8GB

### 4) Run a test job within the container

sudo docker run --gpus 1 --rm lambda-stack:20.04 /usr/bin/python3 -c 'import torch; sz=10000; torch.mm(torch.randn(sz, sz).cuda(), torch.randn(sz, sz).cuda())'

### 5) Upload your container image to a container registry

sudo docker login
sudo docker tag lambda-stack myusername/lambda-stack:20.04
sudo docker push myusername/lambda-stack:20.04

# You can now run the above command on any new computer after installing Lambda Stack, docker.io, and the nvidia-container-runtime like this:
sudo docker run --gpus 1 --rm --interactive --tty myusername/lambda-stack:latest /usr/bin/python3 -c 'import torch; print(torch.rand(5, 5).cuda()); print("I love Lambda Stack!")'

Voilà. You're now up and running with a Lambda Stack Docker image. Furthermore, you now have a Docker image hosted on your container registry that you control.

If you have any questions about using Lambda Stack Dockerfiles, email software@lambdalabs.com.

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
