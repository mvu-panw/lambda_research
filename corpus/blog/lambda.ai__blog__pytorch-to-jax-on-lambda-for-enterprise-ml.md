# JAX on NVIDIA GPUs Part 1: Fundamentals and best practices

Source: https://lambda.ai/blog/pytorch-to-jax-on-lambda-for-enterprise-ml

Skip to main content

# JAX on NVIDIA GPUs Part 1: Fundamentals and best practices

 September 19, 2025

 (Updated on February 13, 2026)

 • 13 min read

JAX unlocks distinct advantages on GPUs: automatic kernel fusion via XLA, composable transformations, and hardware-agnostic code that moves between accelerators with minimal rewrites. This guide covers the practical decisions: framework selection, environment configuration, memory optimization, and scaling patterns from single-GPU experiments to multi-GPU production. By the end, you'll have a clear roadmap for implementing JAX workloads that scale efficiently across GPU infrastructure.

PyTorch vs. JAX

When to choose JAX + GPU

When to choose PyTorch + GPU

Environment configuration

Core GPU optimizations

1. XLA compilation & Kernel Fusion

2. Memory management

3. Memory-aware batch sizing

Scaling strategies

Single GPU training

Multi-GPU training

TPU-to-GPU migration

What transfers seamlessly

What requires adaptation

Migration code patterns

Multi-accelerator strategy

Example development-to-production pipeline

Performance best practices

1. Compilation strategy

2. Memory optimization strategies

3. GPU memory hierarchy awareness

Migration checklist

Conclusion

Quick reference

JAX is rapidly emerging as the framework of choice for teams that need both research flexibility and production performance. While PyTorch dominates the ML landscape with its intuitive imperative style, JAX's functional approach and XLA compilation unlock significant advantages for GPU-accelerated workloads, from automatic kernel fusion to seamless multi-accelerator scaling.

JAX on GPUs offers a compelling combination of performance and portability. This introductory guide provides the practical knowledge you need to harness JAX's full potential on GPU hardware.

We’ll walk you through the following:

- Strategic framework selection 

- GPU environment configuration

- Core optimization techniques

- Scaling strategies

- Production best practices

By the end of this guide, you'll have a clear roadmap for implementing high-performance JAX workloads that scale efficiently across modern GPU infrastructure.

## PyTorch vs. JAX

Understanding the fundamental differences between these frameworks is crucial for making informed decisions about your ML infrastructure. The following comparison highlights when each approach excels and the trade-offs you'll encounter.

 | 

Aspect

 | 

JAX + GPU

 | 

PyTorch + GPU

 | 

Hardware portability

 | 

Unified XLA backend across all accelerators

 | 

NVIDIA CUDA-centric, limited portability

 | 

Functional programming

 | 

Easier distributed computing, composable

 | 

Imperative style, complex distribution

 | 

Research velocity

 | 

Composable transformations (vmap, pmap, jit)

 | 

Larger community, more examples

 | 

Production deployment

 | 

Consistent cross-platform performance

 | 

More mature deployment ecosystem

 | 

Memory efficiency

 | 

Automatic memory optimization via XLA

 | 

Manual memory management required

 | 

Debugging

 | 

Functional approach simplifies reasoning

 | 

Dynamic graphs aid debugging

 | 

Ecosystem & libraries

 | 

Growing but smaller (Flax, Optax, Haiku)

 | 

Mature ecosystem (HuggingFace, Lightning, TorchVision)

 | 

Learning curve

 | 

Steeper, requires functional programming mindset

 | 

More intuitive for beginners, familiar imperative style

 | 

Error messages

 | 

More cryptic XLA compilation errors

 | 

Generally clearer error messages, easier stack traces

 | 

Gradient computation

 | 

Flexible grad() transformation, differentiates arbitrary functions

 | 

Automatic autograd, less composable

 | 

Data loading

 | 

Manual pipeline setup, custom solutions often needed

 | 

Rich DataLoader ecosystem with multiprocessing

 | 

Model serialization

 | 

Relies on pickle/numpy, manual state management

 | 

Native .pth format, TorchScript support

 | 

Graph type

 | 

Static compilation (can complicate control flow)

 | 

Dynamic computation graphs (easier conditional logic)

 | 

Deployment maturity

 | 

Newer options, primarily XLA compilation

 | 

TorchServe, TorchScript, ONNX export, mobile deployment

 | 

Performance profiling

 | 

XLA profiler, newer tooling ecosystem

 | 

Mature profiling tools (TensorBoard, Profiler)

### When to choose JAX + GPU

- Research requiring custom gradients/transformations (e.g., meta-learning, physics-informed neural networks)

- Multi-accelerator deployments and hardware-agnostic code (TPUs, GPUs, future accelerators)

- Teams with functional programming experience who value composable transformations

- Projects where training and research workflows benefit from JAX's functional paradigm

### When to choose PyTorch + GPU

- Rapid prototyping and experimentation

- Large team with varying ML experience levels

- Production systems requiring mature deployment tools

- Projects needing an extensive pre-trained model ecosystem

- Time-sensitive projects requiring extensive community support

## Environment configuration

Essential setup (must configure BEFORE importing JAX):

import os

# Prevent memory pre-allocation for flexible memory management
os.environ['XLA_PYTHON_CLIENT_PREALLOCATE'] = 'false'
os.environ['XLA_PYTHON_CLIENT_MEM_FRACTION'] = '0.8'  # Use 80% of GPU memory
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Specify GPU device
os.environ['XLA_FLAGS'] = '--xla_gpu_enable_triton_gemm=false'  # Stability

import jax
import jax.numpy as jnp

## Core GPU optimizations

JAX's true power on GPUs comes from leveraging XLA's automatic optimizations and implementing strategic memory management. These core techniques form the foundation for achieving peak performance across all your GPU workloads.

### 1. XLA compilation & Kernel Fusion

JAX automatically compiles to optimized NVIDIA CUDA kernels and fuses operations:

@jax.jit  # Compiles to efficient GPU kernels
def optimized_operations(x):
    # These operations get fused into a single GPU kernel
    x = jax.nn.relu(x)
    x = x * 2.0
    x = jnp.sum(x, axis=-1)
    return x  # Single kernel launch instead of three

### 2. Memory management

# Monitor GPU memory
device = jax.devices("gpu")[0]
memory_stats = device.memory_stats()
print(f"Available memory: {memory_stats}")

# Clean up when needed
jax.clear_backends()     # Clear GPU memory
import gc; gc.collect()  # Python garbage collection

### 3. Memory-aware batch sizing

def get_optimal_batch_size(device_type, available_memory_gb):
    """Adjust batch size based on device constraints"""
    if device_type == "gpu":
        # GPUs typically need smaller batches due to memory constraints
        base_size = min(32, int(available_memory_gb * 2))
    else:  # TPU
        base_size = 128  # TPUs excel with large batches
    return base_size

def adaptive_batch_size(device, model_params_size_mb):
    """Dynamically calculate optimal batch size based on available GPU memory"""
    memory_stats = device.memory_stats()
    available_memory_mb = memory_stats.get('bytes_limit', 0) / (1024**2)
    
    # Reserve 20% buffer and account for model parameters + gradients (2x model size)
    usable_memory = (available_memory_mb * 0.8) - (model_params_size_mb * 2)
    
    # Estimate memory per sample
    memory_per_sample = model_params_size_mb * 0.1  # Adjust based on sequence length
    
    optimal_batch_size = int(usable_memory / memory_per_sample)
    return max(1, min(optimal_batch_size, 64))  # Cap between 1 and 64

# Usage example
device = jax.devices("gpu")[0]
model_size_mb = 42 * 4  # 42M parameters * 4 bytes per float32
batch_size = adaptive_batch_size(device, model_size_mb)
print(f"Optimal batch size: {batch_size}")

## Scaling strategies

Moving from single-GPU experiments to multi-GPU production requires adapting your approach to both training patterns and resource allocation. Here's how to scale your JAX implementations effectively across different hardware configurations.

### Single GPU training

@jax.jit
def single_gpu_train_step(state, batch):
    def loss_fn(params):
        return compute_loss(params, state.apply_fn, batch)
    
    loss, grads = jax.value_and_grad(loss_fn)(state.params)
    new_state = state.apply_gradients(grads=grads)
    return new_state, loss

### Multi-GPU training

from functools import partial
from jax import pmap

@partial(pmap, axis_name='devices')
def multi_gpu_train_step(state, batch):
    def loss_fn(params):
        return compute_loss(params, state.apply_fn, batch)
    
    loss, grads = jax.value_and_grad(loss_fn)(state.params)
    # NCCL handles efficient gradient averaging across GPUs
    grads = jax.lax.pmean(grads, axis_name='devices')
    new_state = state.apply_gradients(grads=grads)
    return new_state, loss

## TPU-to-GPU migration

### What transfers seamlessly

- Model architectures and layer definitions

- Training loops and optimization logic

- Data preprocessing pipelines

- Evaluation and metrics computation

- JAX's core transformations (jit, grad, vmap, pmap)

### What requires adaptation

 | 

Component

 | 

Considerations

 | 

Notes

 | 

Parallelism Strategy

 | 

TPU: pmap over TPU cores

GPU: pmap over GPUs or multi-node distribution

 | 

Both use same JAX APIs, different topology

 | 

Communication Backend

 | 

TPU: High-speed interconnect

GPU: NCCL/NVLink

 | 

May need NCCL tuning for multi-node

 | 

Memory Management

 | 

TPU: More automated memory optimization

GPU: May require manual tuning (gradient checkpointing, mixed precision)

 | 

Both support same capacity/strategies

 | 

Batch Size Tuning

 | 

Re-profile for your specific GPU memory and model size

 | 

Not hardware-limited, but optimal size may differ

### Migration code patterns

Before (TPU-optimized):

# Large batch, unified memory
x = jax.device_put(large_batch, jax.devices("tpu")[0])

After (GPU-optimized):

# Smaller batch, memory-aware
gpu_device = jax.devices("gpu")[0]
memory_stats = gpu_device.memory_stats()
optimal_batch = calculate_optimal_batch_size(memory_stats)
x = jax.device_put(optimal_batch, gpu_device)

## Multi-accelerator strategy

Modern ML teams need flexibility to move workloads between different accelerators - whether that's GPU to TPU, TPU to GPU, or adapting to new hardware as it becomes available. JAX's hardware-agnostic design enables this portability for both training and inference workloads.

Common scenarios:

- Develop on GPUs (widely available infrastructure) → Scale training on TPUs (cost-effective for large runs)

- Prototype on TPUs (via cloud providers) → Deploy on GPUs (existing production infrastructure)

- Hybrid workflows: Use whichever accelerator is available/affordable at any given time

This hybrid approach maximizes both development velocity and infrastructure efficiency, letting teams optimize for cost, availability, and performance without rewriting models.

### Example development-to-production pipeline

# Development: Fast iteration on GPU
@jax.jit
def dev_model(x):
    return jax.device_put(model(x), jax.devices("gpu")[0])

# Production: Scale training on TPU
@jax.jit  
def prod_model(x):
    return jax.device_put(model(x), jax.devices("tpu")[0])

# Transfer weights between accelerators
tpu_weights = train_on_tpu(model, data)
gpu_weights = jax.device_put(tpu_weights, jax.devices("gpu")[0])

## Performance best practices

Extracting maximum performance from JAX on GPUs requires understanding both the compilation pipeline and GPU memory hierarchy. These optimizations can dramatically improve throughput while reducing resource costs.

### 1. Compilation strategy

# Compile once, reuse many times
@jax.jit
def train_step(params, batch):
    return loss, grads

# Pre-compile outside training loop
compiled_step = jax.jit(train_step)
for batch in data_loader:
    loss, grads = compiled_step(params, batch)  # No recompilation

### 2. Memory optimization strategies

- Gradient Checkpointing: Trade compute for memory

- Model Sharding: Distribute parameters across GPUs

- Mixed Precision: Use FP16/BF16 to double effective memory

- Pipeline Parallelism: Overlap computation and communication

### 3. GPU memory hierarchy awareness

L1 Cache: ~100KB per SM     → Ultra-fast access
L2 Cache: ~40-80MB shared   → Fast access  
HBM: 24-80GB per GPU        → Main memory
NVLink: 600GB/s GPU-GPU     → Inter-GPU communication
PCIe: ~64GB/s CPU-GPU       → Host communication

## Migration checklist

- Profile existing code for memory and compute bottlenecks

- Adjust batch sizes for GPU memory constraints (typically 2-4x smaller)

- Replace accelerator-specific APIs with device-agnostic alternatives

- Implement gradient checkpointing for memory efficiency

- Test multi-GPU scaling with NCCL communication

- Benchmark performance against existing implementations

- Set up monitoring for GPU utilization and memory usage

- Update deployment scripts for GPU-specific configurations

## Quick reference

# Device management
devices = jax.devices("gpu")
device = jax.devices("gpu")[0] 

# Memory monitoring
memory_stats = device.memory_stats()

# Device placement
data_on_gpu = jax.device_put(data, device)

# Multi-device replication
replicated_data = jax.device_put_replicated(data, devices)

# Cleanup
jax.clear_backends()

## Conclusion

We've covered the essential strategies for deploying JAX on GPUs effectively, from choosing the right framework and optimizing core operations to scaling across multiple accelerators and implementing performance best practices. You now have the foundation to migrate existing workloads, optimize memory usage, and build production-ready pipelines that leverage JAX's unique strengths on NVIDIA infrastructure.

At Lambda, we’re building the GPU infrastructure that makes JAX sing. From single-GPU workstations for rapid prototyping to multi-GPU clusters for large-scale training, Lambda helps you accelerate every stage of your workflow.

Run your next JAX experiment on Lambda and experience the performance difference.

In our next post, we'll put these concepts into practice by implementing a full-scale language model training pipeline using JAX on GPUs, demonstrating how these optimizations translate into real-world performance gains at enterprise scale.

## AUTHORED BY

 Jessica Nicholson

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
