# Accelerate Your AI Workflow with FP4 Quantization on Lambda

Source: https://lambda.ai/blog/lambda-1cc-fp4-nvidia-hgx-b200

Skip to main content

# Accelerate Your AI Workflow with FP4 Quantization on Lambda

 July 16, 2025

 (Updated on November 5, 2025)

 • 8 min read

As AI models grow in complexity and size, the demand for efficient computation becomes paramount. FP4 (4-bit Floating Point) precision emerges as a transformative approach, balancing performance with resource optimization.

## Understanding FP4 Precision

FP4 precision represents numerical values using 4 bits: 1 bit for the sign, 2 bits for the exponent and 1 bit for the mantissa. This structure reduces the numerical representation size, thus shrinking model memory footprints and computational overhead.

With this configuration, FP4 values typically represent numbers within a dynamic range capable of encoding values between ±6.0; offering a balanced trade-off between numerical range and precision. This ultra-low-bit quantization technique accelerates data processing and significantly reduces VRAM consumption, enabling faster processing and reduced memory usage.

## Benefits of FP4 in AI Models

- Reduced Memory Footprint: Quantizing models to FP4 lowers memory footprint. For example, the Qwen3-32B model's memory requirement drops from 64GB in BF16 to 24GB when quantized to FP4, enabling easier deployment.

- Increased Throughput: Quantizing models to FP4 precision substantially boosts inference speed. For instance, the FLUX model achieved approximately a 3x increase in throughput when quantized from FP16 to FP4, significantly accelerating inference performance.

- Energy Efficiency: Lower computational demands translate to reduced energy consumption.

- Scalability: FP4 enables deployment of complex models on hardware with limited resources.

## Implementing FP4 in Practice

Adopting FP4 precision involves quantizing existing models through techniques like Post-Training Quantization (PTQ) and Quantization-Aware Training (QAT). Tools such as NVIDIA TensorRT™ facilitate this transition, ensuring models maintain high accuracy post-quantization.

#### Code Example: Quantizing GPT-2 to FP4 Using NVIDIA TensorRT on Lambda’s 1-Click Clusters

Here's a working example demonstrating how to quantize Hugging Face's GPT-2 model to FP4 precision using NVIDIA TensorRT Model Optimizer, specifically optimized for deployment on Lambda's 1-Click Clusters.

Step 1: Set up your Lambda Cluster environment:
Log into your Lambda gpu-cloud account and navigate to 1-Click Clusters. Make sure Lambda Stack is installed. TensorRT is pre-installed on Lambda's NVIDIA GPU instances.

# SSH into your Lambda 1-Click cluster
ssh user@your-lambda-instance-ip

# Activate your Python environment (optional but recommended)
python3 -m venv env
source env/bin/activate

# Install required packages
pip install transformers torch numpy

Step 2: Export GPT-2 model to ONNX (needed for TensorRT)

import torch
from transformers import GPT2Model, GPT2Tokenizer

model_name = 'gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2Model.from_pretrained(model_name)

dummy_input = tokenizer.encode("Hello world!", return_tensors="pt")

torch.onnx.export(
    model,
    dummy_input,
    "gpt2.onnx",
    input_names=['input_ids'],
    output_names=['output'],
    opset_version=13
)

Step 3: Quantize to FP4 using TensorRT (experimental and limited)

trtexec \
    --onnx=gpt2.onnx \
    --fp4 \
    --saveEngine=gpt2_fp4.engine

This would convert your ONNX model into an optimized FP4 TensorRT engine.

Step 4: Running inference on FP4 quantized TensorRT model

import tensorrt as trt
import numpy as np
import pycuda.driver as cuda
import pycuda.autoinit

TRT_LOGGER = trt.Logger(trt.Logger.WARNING)

def load_engine(engine_path):
    runtime = trt.Runtime(TRT_LOGGER)
    with open(engine_path, "rb") as f:
        return runtime.deserialize_cuda_engine(f.read())

engine = load_engine("gpt2_fp4.engine")
context = engine.create_execution_context()

# Example input
input_ids = np.array([[15496, 995]], dtype=np.int32)  # Tokens for "Hello world!"

# Allocate input/output buffers
input_buffer = cuda.mem_alloc(input_ids.nbytes)
output_size = trt.volume(engine.get_binding_shape(1)) * np.dtype(np.float32).itemsize
output_buffer = cuda.mem_alloc(output_size)

cuda.memcpy_htod(input_buffer, input_ids)

# Execute FP4 quantized inference
context.execute_v2(bindings=[int(input_buffer), int(output_buffer)])

# Retrieve results
output = np.empty(trt.volume(engine.get_binding_shape(1)), dtype=np.float32)
cuda.memcpy_dtoh(output, output_buffer)

print("Inference output:", output)

Notes and Actionable Recommendations:

- 

FP4 quantization support: Official support from NVIDIA for FP4 quantization is limited or experimental. Public TensorRT releases typically support INT8 and FP8 quantization.

- 

Running Environment: Lambda’s NVIDIA HGX B200 clusters are optimal for experimental FP4 workloads due to their native FP4 hardware support.

## Case Study: FLUX Model Optimization

The FLUX model exemplifies FP4's potential. By quantizing the transformer backbone to FP4, there is a 3x increase in throughput and a ~60%  reduction in VRAM usage compared to FP16, all while maintaining image quality.

 | 

System 

 | 

No. of GPUs

 | 

Quantization

 | 

Latency(ms)

 | 

Throughput 
Speedup vs H100 FP16

 | 

NVIDIA HGX H100

 | 

8

 | 

FP16

 | 

1.00x (baseline)

 | 

1.00x (baseline)

 | 

NVIDIA HGX H100

 | 

8

 | 

FP8

 | 

1.4x faster

 | 

1.46x

 | 

NVIDIA HGX B200

 | 

8

 | 

FP8

 | 

2.63x faster

 | 

2.80x

 | 

NVIDIA HGX B200

 | 

8

 | 

FP4

 | 

3.8x faster

 | 

3.17x

Performance Improvements

- NVIDIA Blackwell GPUs vs NVIDIA H100 GPUs: NVIDIA Blackwell with FP4 offers 3x more throughput than FP16 H100. NVIDIA HGX B200 shows more stability at lower precision (FP4), maintaining high performance where the NVIDIA HGX H100 significantly degrades, making it ideal for deployment scenarios where efficiency is critical.

- Scaling with Model Complexity: The performance advantage of HGX B200 FP4 over HGX H100 FP16 increases with model complexity. Complex models (Flux.1-dev) show up to 3.17x better performance on FP4.

- Quantization Efficiency: NVIDIA HGX B200 demonstrates superior performance stability across quantization levels: At FP4 precision, HGX B200 maintains high performance with Flux.1-dev.

Productivity Improvements

- Creative workflows: Generate up to 3.17x more images per second with Flux.1-dev on HGX B200.

- Batch processing: Complete large image generation jobs in nearly half the time.

Cost Efficiency

- Lower TCO: Higher throughput means fewer GPUs needed for the same workload

- Resource optimization: Blackwell’s efficiency at lower FP4 precision enables cost savings without sacrificing quality

User Experience

- Reduced wait times: Up to 68.46% lower latency for interactive applications.

Figure 1: Side-by-side comparison shows the image generation accuracy of FP4 compared to TensorRT BF16 pipelines. Src: NVIDIA Blackwell FP4 Image Gen

## Lambda's FP4 Readiness: Optimized for Precision and Performance

Lambda's 1-Click Clusters, accelerated by NVIDIA HGX B200, are engineered for native FP4 precision support, ensuring optimized performance right from deployment. For teams aiming to leverage FP4-optimized models, these clusters provide:

- On-Demand Access: Deploy multi-node clusters without long-term commitments.

- High Performance: Benefit from up to 3x faster training and 15x faster inference speeds.

- Scalability: Access clusters ranging from 16 to 1536 GPUs, interconnected via high-performance NVIDIA InfiniBand networking, ensuring optimal scalability and minimal latency tailored to your workload requirements.

- Ease of Use: Simplify deployment with pre-configured environments optimized for AI workloads.

## Conclusion

FP4 precision stands at the forefront of AI model optimization, offering a path to more efficient, scalable, and accessible AI solutions. By reducing computational demands without sacrificing performance, FP4 paves the way for broader adoption of advanced AI technologies.

DeepSeek-R1 0528 accuracy measured on NVIDIA Blackwell using TensorRT-LLM build 0.2 1rc0, TensorRT 10.10.0.31 in June 2025. Llama 3.1 405B and Llama 3.3 70B accuracy measured on NVIDIA Blackwell using TensorRT-LLM vO. 17 in January 2025. Src: NVIDIA's NVFP4 for Inference

As seen in Figure 2, NVIDIA’s NVFP4 format paired with the TensorRT Model Optimizer achieves accuracy nearly identical to FP8 even on cutting-edge models like DeepSeek-R1, DeepSeek-R1-0528, Llama 3.1 405B and Llama 3.3 70B. For example, Llama 3.1 405B hits 13,866 tokens/sec with 96.1% accuracy, while DeepSeek-R1-0528 reaches over 43,144 tokens/sec with an impressive 98.1% accuracy, surpassing FP8.

That’s how Blackwell on Lambda sets the bar - not just in tokens per second, but in trust per token.

Ready to unlock the power of FP4 in your AI workflows? Spin up your 1-Click Cluster powered by NVIDIA HGX B200 with advanced FP4 capabilities.

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
