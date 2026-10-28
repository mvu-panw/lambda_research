# NVIDIA H100 Tensor Core GPU - Deep Learning Performance Analysis

Source: https://lambda.ai/blog/nvidia-h100-gpu-deep-learning-performance-analysis

Skip to main content

# NVIDIA H100 Tensor Core GPU - Deep Learning Performance Analysis

 October 5, 2022

 (Updated on November 23, 2023)

 • 11 min read

We have seen groundbreaking progress in machine learning over the last couple of years. At the same time, massive usage of GPU infrastructure has become key to success, particularly for work involving large language models and image models.

Because of this, we have seen lots of excitement around the new NVIDIA H100 Tensor Core GPU — the company’s next-generation flagship GPU for artificial intelligence and HPC. This blog provides an overview of the performance and scalability of the NVIDIA H100 GPU and sheds some light on the whys and whens for upgrading your ML infrastructure with this upcoming big release from NVIDIA.

## TL;DR

Compared to NVIDIA’s previous-generation flagship A100 SXM GPU, the H100 SXM:

- Delivers 3x throughput on Tensor Core, including FP32, and FP64 data types with next-generation Tensor Cores, increased number of streaming multiprocessors, and higher clock frequency.

- Delivers 6x throughput compared to the A100 GPU  by compounding its hardware improvement with the added FP8 data type and the new Transformer Engine. Transformer Engine dramatically accelerates AI calculations for transformer based models such as large language models.

- Updated NVIDIA NVLink and NVIDIA NVSwitch technology provide 3x increase in all-reduce throughput across eight GPUs within a single node, and a 4.5x increase for 256 GPUs across 32 nodes. This is particularly useful for model parallelization and large-scale distributed training.

- For real-world deep learning applications, the speedup varies by workload. Language models usually benefit more (~4x) than vision-based models (~2x), and specific large language models that need model parallelization can achieve up to 30x speedup in inference.

Overall, H100 offers an all-around upgrade for all deep learning applications and is optimized for the largest models, specifically transformer based, whether for large language, vision, or life sciences, that involve structured sparsity (transformers in natural language processing, vision, and drug design) and large-scale distributed workloads.

## Performance

The NVIDIA H100 GPU is based on the new NVIDIA Hopper GPU architecture. Compared to its predecessor, the A100, H100 offers multiple key performance improvements:

- Fourth-generation Tensor Cores: Powered by the new Tensor Cores, each streaming multiprocessor (SM) of the H100 doubles the computational throughput of the A100 SM clock for clock on equivalent data types, including: Tensor Core data types such as TF32, FP32, and FP64.

- More SMs: H100 is available in two form factors — SXM5 and PCIe5. H100 SXM5 features 132 SMs, and H100 PCIe has 114 SMs. These translate to a 22% and a 5.5% SM count increase over the A100 GPU’s 108 SMs.

- Increased clock frequencies: H100 SXM5 operates at a GPU boost clock speed of 1830 MHz, and H100 PCIe at 1620 MHz. These translate to a 30% and a 15% increase over the A100 GPU’s 1410 MHz.

- FP8 and Transformer Engine: The new FP8 data type, only available on H100, quadruples the computational rates clock for clock per SM of FP16 on A100. With the help of Transformer Engine, which is part of the NVIDIA Hopper architecture, the program can intelligently manage and dynamically choose between FP8 and 16-bit calculations, reducing memory usage and increasing performance while maintaining accuracy for transformer models.

Aggregating the first three improvements on the above list (Tensor Core, SM count, clock frequencies), we can expect the relative GEMMs (General Matrix Multiplications) performance of H100 over A100 on Tensor Core, FP32, and FP64 data types to be 3x for H100 SXM5 and 2.5x for H100 PCIe. Since GEMMs are a fundamental building block in neural networks, such an improvement will benefit most deep learning tasks, regardless of the models you work with.

When compounding the improvement with FP8 and Transformer Engine, we can expect the relative GEMMs performance of H100 FP8 over A100 FP16 to be 6x for H100 SXM5 and 5x for H100 PCIe — a very significant improvement for training and running inference with transformer models. In MLPerf Inference v2.1, an industry-standard measure of inference performance, the NVIDIA H100 and Transformer Engine delivered up to 4.5x more performance than the A100.

## Scalability

So far, we have discussed the performance of a single H100 GPU, and now it is time to turn our attention to its scalability. The H100 introduces some cool features for better scaling:

- Fourth-generation NVIDIA NVLink: NVLink directly interconnects two GPUs with higher bandwidth, so their communication does not have to go through PCIe lanes. H100 has 18 fourth-generation NVLink interconnects, providing 900 GB/sec total bandwidth, which is 1.5x over the A100 GPU’s 600 GB/sec total bandwidth and 7x over the bandwidth of PCIe Gen5.

- Third-generation NVIDIA NVSwitch: While an NVLink connects a pair of GPUs, NVSwitch connects multiple NVLinks and ensures GPU communication runs at the max speed within a single node and between nodes. H100 uses the new third-generation NVSwitch, which provides 64 ports of fourth-generation NVLink interconnects to accelerate GPU communication within the node; second-level NVSwitch interconnects outside a node enable a large NVLink domain (up to 32 nodes or 256 GPUs) with address space isolation and protection and deliver 57.6 TB/sec of all-to-all bandwidth.

On the operation side, there is a significant difference between the two H100 form factors. The max thermal design power (TDP) is 350W for H100 PCIe, close to the 300W TDP of its predecessor, the A100 80GB PCIe. However, H100 SXM5 supports up to a700W TDP. Nonetheless, H100 cards are also more “power effective” than A100 GPUs, with a 4x and nearly 3x increase in FP8 FLOPS/W over the A100 80GB PCIe and SXM4 predecessors, respectively.

 |  
 | 

A100 80GB PCIe

 | 

A100 80 GB SXM4

 | 

H100 80GB PCIe

 | 

H100  80GB SXM5

 | 

FP8/FP16 TFLOPS*

 | 

624

 | 

624

 | 

3,026

 | 

3,958

 | 

Watts

 | 

300

 | 

400

 | 

350

 | 

700

 | 

FP8/FP16 TFLOPS/W

 | 

2.1

 | 

1.56

 | 

8.6

 | 

5.7

* A100 does not support FP8 data type. Comparisons are to FP16, the nearest precision supported on A100.

## Quality of Life

Apart from the raw performance and scalability upgrade, H100 also makes resources management and utilization more efficient:

- Second-generation Multi-Instance GPU (MIG): MIG is a technology that improves GPU utilization for a team while providing access to more users. Although the max number of independent instances per GPU is the same for H100 and its predecessor — both are seven — the H100 GPU’s second-generation MIG technology supports secure tenants, enables dedicated NVDEC and NVJPG units on each instance, and offers approximately 3x more compute capacity and nearly 2x more memory bandwidth per GPU instance compared to the A100. This helps IT operations teams.

- Asynchronous execution: Asynchronous execution allows threads to complete at different rates, as opposed to having them wait for data and pause. H100 provides new features that improve asynchronous execution, in particular, leveraging the new Tensor Memory Accelerator (TMA) unit to hide data movement with computation.

- FP8 support from major deep learning frameworks: Although it is left to see how useful the FP8 data type can be for deep learning tasks, PyTorch has already started some cutting-edge experiments with it.

## Best Use Cases

Having seen all these new features and improvements over performance and scalability, let us talk about what deep learning use cases benefit the most from an upgrade to the H100.

- Big models with high structured sparsity: Although NVIDIA estimates 5-6x improvement of H100 over A100 depending on the H100 form factor, its real-world benchmarks indicate that the gain varies from case to case: the speedup of training on H100 compared to A100 is a little over 2x for Mask R-CNN (a vision model), close to 3x for recommendation models, a little under 4x for language models such as GPT-3 16B and GPT-175B, and well above 4x for mixture of experts models. This is in line with what we have observed from the Ampere GPUs: Tensor Core’s performance is optimized for big models with high structured sparsity, with large language models being the favorite examples. Classical CNN-based models (e.g., vision tasks) tend to benefit less from the system upgrade. However, as transformers are getting increasingly more popular outside of NLP, we expect applications such as computer vision and drug discovery will also start to enjoy features such as FP8 and Transformer Engine.

- Large-scale distributed data parallelization: The H100 GPU’s new NVLink and NVSwitch technologies provide 4.5x all-reduce throughput while measured against a 32-node, 256-GPU setup. Such improvement will significantly benefit large-scale distributed training, where inter-node GPU to GPU communication has always been the bottleneck. This applies not only to language models but also text2image models or hyper-scale training of classical CNN models.

- Model parallelization: Another high-value case for H100 is that many of today’s largest and most challenging models no longer fit a single GPU, hence requiring model parallelism across multiple GPUs or GPU nodes. The H100 GPU’s new NVSwitch system can bring in another giant performance leap. For example, running inference with Megatron Turing NLG model on an H100 system resulted in a 30x speedup compared to a reference A100 system with the same number of GPUs.

- Model quantization: Getting the trained model to work well with INT8 precision has been the holy grail for many in-production applications. Despite numerous existing tools and practices, model quantization is not always a smooth journey because the INT8 model often has a drop in accuracy. The new FP8 data type offers a new route that addresses the problem from the math mode perspective, reducing or even eliminating the effort of additional quantization steps needed for specific deep learning models.

Interested in learning more? Stay up to date on availability, features and capabilities and other useful information about the NVIDIA H100 with Lambda.

## AUTHORED BY

 Chuan Li

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
