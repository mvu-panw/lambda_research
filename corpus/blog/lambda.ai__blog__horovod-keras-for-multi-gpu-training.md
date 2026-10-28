# Setting up Horovod + Keras for Multi-GPU training

Source: https://lambda.ai/blog/horovod-keras-for-multi-gpu-training

Skip to main content

# Setting up Horovod + Keras for Multi-GPU training

 August 28, 2019

 (Updated on August 3, 2023)

 • 5 min read

This blog will walk you through the steps of setting up a Horovod + Keras environment for multi-GPU training.

## Prerequisite

- Hardware: A machine with at least two GPUs

- Basic Software: Ubuntu (18.04 or 16.04), Nvidia Driver (418.43), CUDA (10.0) and CUDNN (7.5.0). All of these can be easily installed using Lambda Stack for free.

## Installation

There are several of things to be installed on top of the necessary software stack: NCCL2, Open MPI (optional), and Horovod. Getting the installation right can be a bit tedious for first time users, which motivated us to write this step-by-step guide to help people get it right.

You can find the one-stop installation script for all the steps after the download of the NCCL2 library.

### NCCL2

The NVIDIA Collective Communications Library (NCCL) implements multi-GPU and multi-node collective communication primitives that are optimized for NVIDIA GPUs. Think it as a library used by Horovod to improve the performance of all-gather, reduce, broadcast, etc. across GPUs devices.

You need an NVIDIA Developer Program account to download the library. The registeration is free at this link. Once login, download the library with the version that suits your CUDA environment. In our case, it is the NCCL v2.4.8, for CUDA 10.0, July 31, 2019, O/S agnostic local installer.

To install the library, one needs to copy the files to specific locations and add their path to LD_LIBRARY_PATH:

tar -vxf ~/Downloads/nccl_2.4.8-1+cuda10.0_x86_64.txz -C ~/Downloads/
sudo cp ~/Downloads/nccl_2.4.8-1+cuda10.0_x86_64/lib/libnccl* /usr/lib/x86_64-linux-gnu/
sudo cp ~/Downloads/nccl_2.4.8-1+cuda10.0_x86_64/include/nccl.h /usr/include/
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/x86_64-linux-gnu' >> ~/.bashrc
source ~/.bashrc

### Open MPI (Optional)

This is not a must-do. However, Horovod has a "Open MPI-based wrapper", and it is very convenient to use them together. It is a bit like the relationship between Keras and TensorFlow – you don't have to use TensorFlow, because Keras also supports Theano and CNTK. Nonetheless, in practice most Keras users do install TensorFlow as the backend.

In the meantime, Open MPI can be used in conjunction with NCCL: It is easy to use MPI for CPU-to-CPU communication and NCCL for GPU-to-GPU communication. We won't go into too much details here. A more in-depth discussion about the relationship between NCCL and MPI can be found here.

Before we install Open MPI, there is a catch: By default, Ubuntu comes with an outdated version mpirun and no mpicxx (the C++ compiler for Open MPI). This default setup is insufficient to work with Horovod, and can potentially cause a problem for your later installation. Hence the first thing you should do is removing these pre-installed files:

sudo mv /usr/bin/mpirun /usr/bin/bk_mpirun
sudo mv /usr/bin/mpirun.openmpi /usr/bin/bk_mpirun.openmpi

Then we can install Open MPI with following steps:

wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.1.tar.gz -P ~/Downloads
tar -xvf ~/Downloads/openmpi-4.0.1.tar.gz -C ~/Downloads
cd ~/Downloads/openmpi-4.0.1
./configure --prefix=$HOME/openmpi
make -j 8 all
make install

echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/openmpi/lib' >> ~/.bashrc
echo 'export PATH=$PATH:~/openmpi/bin' >> ~/.bashrc
source ~/.bashrc

### Horovod

Finally, we install Horovod, Keras, and TensorFlow-GPU in a Python3 virtual environment. g++-4.8 is also needed for Horovod to work with the pip installed TensorFlow.

cd

# Install g++-4.8 (for running horovod with TensorFlow)
sudo apt install g++-4.8

# Create a Python3.6 virtual environment
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv -p /usr/bin/python3.6 venv-horovod-keras
. venv-horovod-keras/bin/activate

# Install keras and TensorFlow GPU backend
pip install tensorflow-gpu==1.13.2 keras

HOROVOD_NCCL_HOME=/usr/lib/x86_64-linux-gnu HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITHOUT_PYTORCH=1 HOROVOD_WITHOUT_MXNET=1 pip install --no-cache-dir horovod

## Multi-GPU Training

To test the environment, we run the keras MNIST training example from the Horovod official Repo.

git clone https://github.com/horovod/horovod.git
cd horovod/examples
. venv-horovod-keras/bin/activate

There are actually two ways to run a Horovod job: using the horovodrun wrapper, or using the mpirun API. Below are the examples of running a training script with two GPUs on the same machine:

horovodrun -np 2 -H localhost:2 --mpi python keras_mnist.py

mpirun -np 2 \
 -H localhost:2 \
 -bind-to none -map-by slot \
 -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH \
 -mca pml ob1 -mca btl ^openib \
 python keras_mnist.py

These two commands do basically the same thing, whereas the mpirun method allows more configurations. For example, the NCCL_DEBUG=INFO option allows the display of NCCL devices information for the job.

## Summary

This tutorial demonstrated how to setup a working environment for multi-GPU training with Horovod and Keras. You can find the one-stop installation script for all the steps after the download of the NCCL2 library.

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
