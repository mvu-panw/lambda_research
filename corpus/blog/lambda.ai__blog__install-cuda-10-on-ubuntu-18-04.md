# Install CUDA 10 on Ubuntu 18.04

Source: https://lambda.ai/blog/install-cuda-10-on-ubuntu-18-04

Skip to main content

# Install CUDA 10 on Ubuntu 18.04

 February 10, 2019

 (Updated on November 23, 2023)

 • 1 min read

You were probably thinking that this was going to be a long post. You're in luck. All you need to do is to install Ubuntu 18.04 and then Lambda Stack. Here's the code for that:

LAMBDA_REPO=$(mktemp) && \
wget -O${LAMBDA_REPO} https://lambdalabs.com/static/misc/lambda-stack-repo.deb && \
sudo dpkg -i ${LAMBDA_REPO} && rm -f ${LAMBDA_REPO} && \
sudo apt-get update && sudo apt-get install -y lambda-stack-cuda

That's literally all you need to do. Now go grab yourself a can of Monster and get back to work.

This is all you need for Titan RTX and 2080 Ti (Turing) GPU support. This will install the NVIDIA Driver and CUDA 10 (at the time of writing). Simple enough.

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
