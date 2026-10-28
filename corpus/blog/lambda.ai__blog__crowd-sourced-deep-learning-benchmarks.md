# Crowd Sourced Deep Learning GPU Benchmarks from the Community

Source: https://lambda.ai/blog/crowd-sourced-deep-learning-benchmarks

Skip to main content

# Crowd Sourced Deep Learning GPU Benchmarks from the Community

 October 12, 2018

 (Updated on August 3, 2023)

 • 11 min read

We open sourced the benchmarking code we use at Lambda Labs so that anybody can reproduce the benchmarks that we publish or run their own. We encourage people to email us with their results and will continue to publish those results here. You can run the code and email benchmarks@lambdalabs.com or tweet @LambdaAPI. This is the official page for all Lambda Community Benchmarks.

## How to get your results published here

- Download and run our benchmarking code: https://github.com/lambdal/lambda-tensorflow-benchmark

- Fill out this markdown table form for your system setup.

Component | Version
-----------------|------------
CPU | $(cat /proc/cpuinfo | grep 'model name' | uniq | awk -F: '{ print $2 }')
Distro | $(lsb_release -d)
Kernel Version | $(uname -r)
Kernel Arch | $(uname -m)
GPU | $(sudo lspci | grep VGA\ compat | head -n1)
Tensorflow | $(python -c 'import tensorflow;print(tensorflow.__version__)' 2> /dev/null)
NVIDIA Driver | $(head -n1 /proc/driver/nvidia/version | awk '{ print $8 }')
CUDA | $(nvcc --version | tail -n 1 | grep Cuda | awk '{ print $6 }')
cuDNN | $(cat /usr/include/cudnn.h | grep -P 'define\ CUDNN_MAJOR|define\ CUDNN_MINOR|define\ CUDNN_PATCHLEVEL' | awk '{ print $3 }' | sed ':a;N;$!ba;s/\n/./g')
Python | $(python --version 2>&1)

Copy the above and paste into template.txt. Then run the code below to output your table.

IFS=' '
cat > template.txt
CTRL-V (paste in)
CTRL-D (end file)
(for line in $(cat template.txt); do eval "echo \"$line\""; done) > specs-table.txt

- Mail the output summary.md file as well as the output system specification table above to benchmarks@lambdalabs.com.

### Crowd Sourced Results

Here are the results that have been submitted to us by third parties.

## Summary (Stanislav Brizitsky)

 | Component
 | Version

 | CPU
 | AMD Phenom(tm) II X6 1075T Processor

 | Distro
 | Ubuntu 19.04

 | Kernel Version
 | 5.0.0-31-generic

 | Kernel Arch
 | x86_64

 | GPU
 | 04:00.0 VGA compatible controller: NVIDIA Corporation TU102 GeForce RTX 2080 Ti (rev a1)

 | Tensorflow
 | 1.14.0

 | NVIDIA Driver
 | 430.50

 | CUDA
 | V10.1.105

 | cuDNN
 | 7.6.4

 | Python
 | Python 3.7.3

## Summary

 | model
 | input size
 | param mem
 | feat. mem
 | flops

 | resnet-50
 | 224 x 224
 | 98 MB
 | 103 MB
 | 4 BFLOPs

 | resnet-152
 | 224 x 224
 | 230 MB
 | 219 MB
 | 11 BFLOPs

 | inception-v3
 | 299 x 299
 | 91 MB
 | 89 MB
 | 6 BFLOPs

 | vgg-vd-19
 | 224 x 224
 | 548 MB
 | 63 MB
 | 20 BFLOPs

 | alexnet
 | 227 x 227
 | 233 MB
 | 3 MB
 | 1.5 BFLOPs

 | ssd-300
 | 300 x 300
 | 100 MB
 | 116 MB
 | 31 GFLOPS

syn-replicated-fp32-1gpus

 | Config
 | X6-GeForce_RTX_2080_Ti

 | resnet50
 | 294.45

 | resnet152
 | 107.72

 | inception3
 | 193.16

 | inception4
 | 76.11

 | vgg16
 | 176.88

 | alexnet
 | 3665.52

 | ssd300
 | 150.39

syn-parameter_server-fp32-1gpus

 | Config
 | X6-GeForce_RTX_2080_Ti

 | resnet50
 | 291.69

 | resnet152
 | 107.40

 | inception3
 | 192.78

 | inception4
 | 76.10

 | vgg16
 | 176.89

 | alexnet
 | 3673.53

 | ssd300
 | 150.30

syn-replicated-fp16-1gpus

 | Config
 | X6-GeForce_RTX_2080_Ti

 | resnet50
 | 462.98

 | resnet152
 | 172.64

 | inception3
 | 284.54

 | inception4
 | 104.68

 | vgg16
 | 261.92

 | alexnet
 | 4755.02

 | ssd300
 | 194.10

syn-parameter_server-fp16-1gpus

 | Config
 | X6-GeForce_RTX_2080_Ti

 | resnet50
 | 468.89

 | resnet152
 | 176.30

 | inception3
 | 287.66

 | inception4
 | 108.32

 | vgg16
 | 266.71

 | alexnet
 | 4856.88

 | ssd300
 | 197.04

 | Attachments area
 |  

## Summary (Antonio Marin)

RTX2080Ti benchmark

### Specifications

 | Component
 | Version

 | CPU
 | Intel(R) Core(TM) i9-7900X CPU @ 3.30GHz

 | Distro
 | Description: Ubuntu 16.04.6 LTS

 | Kernel Version
 | 4.15.0-52-generic

 | Kernel Arch
 | x86_64

 | GPU
 | 65:00.0 VGA compatible controller: NVIDIA Corporation GV102 (rev a1)

 | Tensorflow
 | 1.12.0

 | NVIDIA Driver
 | 418.56

 | CUDA
 | V7.5.17

 | cuDNN
 | 7.3.1

 | Python
 | Python 3.6.8 :: Anaconda, Inc.

### Benchmark results

 | model
 | input size
 | param mem
 | feat. mem
 | flops

 | resnet-50
 | 224 x 224
 | 98 MB
 | 103 MB
 | 4 BFLOPs

 | resnet-152
 | 224 x 224
 | 230 MB
 | 219 MB
 | 11 BFLOPs

 | inception-v3
 | 299 x 299
 | 91 MB
 | 89 MB
 | 6 BFLOPs

 | vgg-vd-19
 | 224 x 224
 | 548 MB
 | 63 MB
 | 20 BFLOPs

 | alexnet
 | 227 x 227
 | 233 MB
 | 3 MB
 | 1.5 BFLOPs

 | ssd-300
 | 300 x 300
 | 100 MB
 | 116 MB
 | 31 GFLOPS

syn-replicated-fp32-1gpus

 | Config
 | i9-7900X-GeForce_RTX_2080_Ti

 | resnet50
 | 318.45

 | resnet152
 | 121.54

 | inception3
 | 210.28

 | inception4
 | 88.72

 | vgg16
 | 186.87

 | alexnet
 | 3877.75

 | ssd300
 | 162.28

syn-parameter_server-fp32-1gpus

 | Config
 | i9-7900X-GeForce_RTX_2080_Ti

 | resnet50
 | 316.52

 | resnet152
 | 122.22

 | inception3
 | 211.87

 | inception4
 | 88.26

 | vgg16
 | 186.70

 | alexnet
 | 3868.16

 | ssd300
 | 162.23

syn-replicated-fp16-1gpus

 | Config
 | i9-7900X-GeForce_RTX_2080_Ti

 | resnet50
 | 448.98

 | resnet152
 | 159.09

 | inception3
 | 261.64

 | inception4
 | 96.25

 | vgg16
 | 215.97

 | alexnet
 | 4507.86

 | ssd300
 | 186.27

syn-parameter_server-fp16-1gpus

 | Config
 | i9-7900X-GeForce_RTX_2080_Ti

 | resnet50
 | 454.84

 | resnet152
 | 162.12

 | inception3
 | 259.83

 | inception4
 | 98.24

 | vgg16
 | 220.16

 | alexnet
 | 4566.05

 | ssd300
 | 187.44

## Summary - Mike Metral - 1080 Ti

 | model
 | input size
 | param mem
 | feat. mem
 | flops

 | resnet-50
 | 224 x 224
 | 98 MB
 | 103 MB
 | 4 BFLOPs

 | resnet-152
 | 224 x 224
 | 230 MB
 | 219 MB
 | 11 BFLOPs

 | inception-v3
 | 299 x 299
 | 91 MB
 | 89 MB
 | 6 BFLOPs

 | vgg-vd-19
 | 224 x 224
 | 548 MB
 | 63 MB
 | 20 BFLOPs

 | alexnet
 | 227 x 227
 | 233 MB
 | 3 MB
 | 1.5 BFLOPs

 | ssd-300
 | 300 x 300
 | 100 MB
 | 116 MB
 | 31 GFLOPS

syn-replicated-fp32-1gpus

 | Config
 | v2-GeForce_GTX_1080_Ti

 | resnet50
 | 221.33

 | resnet152
 | 84.99

 | inception3
 | 142.51

 | inception4
 | 60.11

 | vgg16
 | 142.39

 | alexnet
 | 2868.88

 | ssd300
 | 112.22

syn-parameter_server-fp32-1gpus

 | Config
 | v2-GeForce_GTX_1080_Ti

 | resnet50
 | 221.24

 | resnet152
 | 85.04

 | inception3
 | 142.39

 | inception4
 | 60.12

 | vgg16
 | 142.17

 | alexnet
 | 2870.47

 | ssd300
 | 112.14

syn-replicated-fp16-1gpus

 | Config
 | v2-GeForce_GTX_1080_Ti

 | resnet50
 | 275.24

 | resnet152
 | 99.76

 | inception3
 | 161.39

 | inception4
 | 64.63

 | vgg16
 | 153.03

 | alexnet
 | 2981.33

 | ssd300
 | 126.42

syn-parameter_server-fp16-1gpus

 | Config
 | v2-GeForce_GTX_1080_Ti

 | resnet50
 | 275.78

 | resnet152
 | 100.20

 | inception3
 | 160.48

 | inception4
 | 65.22

 | vgg16
 | 156.34

 | alexnet
 | 3022.28

 | ssd300
 | 127.33

### Hardware / Software

 | Component
 | Version

 | Distro
 | Ubuntu 18.04.1

 | Kernel
 | 4.18.5 x86_64

 | GPU / Compute Capacity
 | NVIDIA GeForce GTX 1080 TI - 6.1

 | Tensorflow
 | v1.11.0

 | NVIDIA
 | 410.57

 | CUDA
 | 10.0.130_410.48

 | cuDNN
 | 7.3.0.29

 | NCCL
 | 2.3.5

 | GCC Ubuntu
 | 6.4.0-17ubuntu1

 | Python
 | 3.6.6

 | Bazel
 | 0.16.1

## AUTHORED BY

 Stephen Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
