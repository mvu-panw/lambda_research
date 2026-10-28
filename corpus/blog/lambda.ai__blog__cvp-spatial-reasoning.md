# Building multimodal models for spatial reasoning

Source: https://lambda.ai/blog/cvp-spatial-reasoning

Skip to main content

# Building multimodal models for spatial reasoning

 September 24, 2026

 • 5 min read

## What is spatial reasoning?

AI is moving beyond the digital world. The next generation of AI systems needs to understand and interact with physical environments, from robots to autonomous systems navigating complex spaces.

This shift toward physical AI creates a fundamental challenge: AI models need more than language intelligence and visual recognition. They need to reason about the physical world.

Spatial reasoning is the ability to understand an environment's 3D structure: where objects are, how they relate to one another, and which objects matter for a particular task.

If you ask a robot to find the object next to the table and in front of the curtain, recognizing them won’t be enough. It must understand their spatial relationships, identify which objects matter for the instruction, and reason about their positions in the environment.

## Why is spatial reasoning challenging?

Despite rapid progress in large language models (LLMs) and vision-language models (VLMs), reasoning about 3D environments remains challenging.

Conventional LLMs can understand spatial concepts expressed in language, such as left of or behind, but they don't directly observe physical geometry. VLMs add visual perception, but they build their representations from 2D images tied to individual viewpoints. The same object can appear at different positions, scales, and orientations across camera views. The model has to connect these observations into a consistent understanding of the underlying 3D scene.

Even when 3D information is available, having spatial information isn't the same as reasoning effectively with it. A complex scene may contain many objects, while a particular question involves only a few. The model must therefore solve two problems at once: identify what matters for the current task and understand how the broader environment is organized.

These challenges point to two complementary capabilities for effective 3D spatial reasoning: local, task-dependent focus and global spatial awareness.

In their paper, CVP: Central-Peripheral Vision-Inspired Multimodal Model for Spatial Reasoning, accepted to WACV 2026, researchers from UC San Diego and Lambda explore an approach inspired by how humans naturally combine these capabilities.

CVP introduces a target-affinity token to focus the model on task-relevant objects and an allocentric grid to provide a structured representation of the broader 3D environment: focus on what matters, stay aware of everything else.

## Learning from central and peripheral vision

Human vision combines central vision, which provides detailed information about what we focus on, with peripheral vision, which maintains broader awareness of our surroundings. CVP translates this principle into two complementary mechanisms for multimodal models.

### 1. Central vision: what should I focus on?

A 3D environment may contain many objects, but only a few matter for a particular question. CVP introduces a target-affinity token that learns to identify these task-relevant objects.

During training, the model projects multi-view visual features into a shared 3D coordinate system and aggregates them into object-level representations. A contrastive objective encourages the target-affinity representation to align with relevant objects and move away from irrelevant ones.

In effect, the model learns to answer: "Given my current task, what should I pay attention to?"

### 2. Peripheral vision: how is the environment organized?

Knowing what to focus on is only part of the problem. The model also needs to understand the broader scene. CVP introduces an allocentric grid, a compact bird's-eye-view representation of the environment. Unlike an egocentric representation tied to a particular camera, the allocentric grid represents objects from a world-centered perspective.

By converting the grid into a concise textual representation, CVP makes high-level spatial structure explicitly available to the language model, rather than requiring it to reconstruct the scene entirely from raw visual and geometric features.

The default 6 x 6 grid performs strongly. Increasing its resolution provides no additional benefit. This suggests effective spatial reasoning depends on more than raw spatial detail: the right abstraction matters just as much.

Together, the two mechanisms address complementary questions:

- Target-affinity token: what matters?

- Allocentric grid: how is the environment organized?

Combined with multi-view visual tokens and 3D positional information, they enable the model to reason with both local focus and global spatial awareness.

The following figure illustrates the CVP architecture.

CVP builds on LLaVA-Video-7B and the multi-view representation of Video-3D-LLM and is jointly trained across five datasets covering question answering, visual grounding, and dense captioning.

## Results

The team evaluates CVP on five 3D vision-language benchmarks spanning question answering, visual grounding, and dense captioning: ScanQA, SQA3D, ScanRefer, Multi3DRefer, and Scan2Cap.

Across all five benchmarks, CVP consistently outperforms the Video-3D-LLM baseline:

- 

For 3D question answering, CVP improves CIDEr from 102.1 to 107.1 on ScanQA and exact-match accuracy from 58.6 to 62.3 on SQA3D.

- 

For visual grounding, it improves Acc@0.25 from 58.1 to 62.0 on ScanRefer and F1@0.25 from 58.0 to 60.2 on Multi3DRefer.

- 

For dense captioning, CVP increases CIDEr from 83.8 to 90.5 on Scan2Cap.

These results show consistent gains across spatial reasoning tasks, from answering questions about 3D scenes to locating and describing objects. 

The following figure presents several qualitative results.

Ablation experiments further show that the two components contribute to different aspects of spatial reasoning. The target-affinity token provides larger benefits for visual grounding, where identifying the task-relevant object is critical. The allocentric grid is particularly important for question answering and dense captioning, which require a broader understanding of the scene.

The results reinforce the intuition behind CVP: central vision helps determine what matters, while peripheral vision provides the broader spatial context. More broadly, CVP suggests that how information about the physical world is represented can matter as much as how much information is provided.

## Building spatial reasoning models on Lambda

Training multimodal models for 3D spatial reasoning brings together visual information, multiple camera views, camera geometry, 3D coordinates, and language within a single pipeline. Processing these modalities together increases both compute and memory demands and makes rapid experimentation with new architectures essential.

For CVP, researchers fine-tuned a 7B-parameter multimodal model across five 3D vision-language datasets using 8 NVIDIA A100 Tensor Core GPUs, with Lambda providing the compute.

As AI expands from text and 2D images to video, 3D environments, robotics, and physical AI, researchers need infrastructure that can support these compute-intensive multimodal workloads. Lambda provides scalable GPU infrastructure for training and fine-tuning multimodal foundation models and exploring new architectures at scale, helping researchers move AI from recognizing what is in the world toward reasoning about how that world is organized.

Paper: https://arxiv.org/pdf/2512.08135
Credits: UC San Diego, Lambda
Authors: Zeyuan Chen, Xiang Zhang, Haiyang Xu, Jianwen Xie, and Zhuowen Tu. WACV 2026.

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
