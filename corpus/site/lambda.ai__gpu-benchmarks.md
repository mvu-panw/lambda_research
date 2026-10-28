# GPU Benchmarks for Deep Learning | Lambda

Source: https://lambda.ai/gpu-benchmarks

Skip to main content

# NVIDIA GPU benchmarks

GPU training/inference speeds using PyTorch®/TensorFlow for computer vision (CV), NLP, text-to-speech (TTS), etc.
PricingTalk to our team

Loading benchmarks...

## GPU benchmark methodology

To measure the relative effectiveness of GPUs when it comes to training neural networks we’ve chosen training throughput as the measuring stick. Training throughput measures the number of samples (e.g. tokens, images, etc...) processed per second by the GPU.

Using throughput instead of Floating Point Operations per Second (FLOPS) brings GPU performance into the realm of training neural networks. Training throughput is strongly correlated with time to solution — since with high training throughput, the GPU can run a dataset more quickly through the model and teach it faster.

In order to maximize training throughput it’s important to saturate GPU resources with large batch sizes, switch to faster GPUs, or parallelize training with multiple GPUs. Additionally, it’s also important to test throughput using state of the art (SOTA) model implementations across frameworks as it can be affected by model implementation.

## PyTorch®

We are working on new benchmarks using the same software version across all GPUs. Lambda's PyTorch® benchmark code is available here.

The 2023 benchmarks used using NGC's PyTorch® 22.10 docker image with Ubuntu 20.04, PyTorch® 1.13.0a0+d0d6b1f, CUDA 11.8.0, cuDNN 8.6.0.163, NVIDIA driver 520.61.05, and our fork of NVIDIA's optimized model implementations.

The 2022 benchmarks used using NGC's PyTorch® 21.07 docker image with Ubuntu 20.04, PyTorch® 1.10.0a0+ecc3718, CUDA 11.4.0, cuDNN 8.2.2.26, NVIDIA driver 470, and NVIDIA's optimized model implementations in side of the NGC container.

PyTorch® is a registered trademark of The Linux Foundation. https://pytorch.org/

## Ready to get started?

Talk to us about powering your next breakthrough and joining the race to superintelligence.
Talk to our team
