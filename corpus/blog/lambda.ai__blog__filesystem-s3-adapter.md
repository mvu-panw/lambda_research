# No VM? No Problem: Meet the Filesystem S3 Adapter

Source: https://lambda.ai/blog/filesystem-s3-adapter

Skip to main content

# No VM? No Problem: Meet the Filesystem S3 Adapter

 May 7, 2025

 (Updated on October 22, 2026)

 • 3 min read

Say goodbye to storage gymnastics. Say hello to S3 simplicity.

Until today, transferring data into or out of Lambda storage required provisioning a VM just to move files. That middle step added both time and cost even when you only needed storage access. Our new Filesystem S3 Adapter removes that friction, letting you use familiar S3 APIs directly with your Lambda Filesystem.

## Under the Hood: S3 Access Without the Overhead

The Filesystem S3 Adapter enables a subset of the S3 API including GetObject, PutObject, DeleteObject and list on top of our existing Lambda Filesystem storage.

We’re building a world-class ML cloud that removes the friction to training and this feature is one step closer towards that vision. Here’s why:

Lowest-Cost Inference
Lambda offers industry-leading prices for GPU compute, ideal for inference at scale. Combine that with the new Filesystem S3 Adapter to eliminate VM costs during data movement.

Drop-in OpenAI API Replacement
Use open-source models hosted on Lambda with the same APIs you’re already familiar with. Swap your endpoint, not your stack.

No MLOps Required
You don’t need to build an entire MLOps pipeline to get started. Lambda’s cloud and S3 adapter streamline the messy middle of machine learning workflows.

Access to Latest Open-Source Models
Train or fine-tune cutting-edge open-source models right from your Lambda cluster. Your data, your models, no vendor lock-in.

## Designed for ML Teams, Built for Speed

This adapter is purpose-built for AI/ML practitioners and researchers using Lambda Cloud, especially those using our 1-Click Clusters (1CC).

Top use cases include:

- Pre-loading datasets before kicking off a cluster reservation

- Egressing model checkpoints and weights after training

- Transferring data from other cloud providers using familiar tools

In short: if you’re managing data and want to skip the VM middleman, this is for you.

## Why This Matters

Until now, managing data in Lambda storage often meant spinning up a VM just to shuttle files in or out. That’s friction, and when you’re eager to start training, friction is the enemy.

With the Filesystem S3 Adapter, we’re solving this problem, removing the VM bottleneck and delivering a faster, cleaner path to compute.

#### Key benefits

- VM-free data movement: Ingest and egress datasets without spinning up compute instances, saving on unnecessary VM charges.

- Familiar tools: Use rclone, s5cmd, AWS CLI or any S3-compatible client against Lambda storage.

- Availability: Currently supported in US-East-2 (Washington DC, USA) and US-East-3 (Washington DC, USA) with more regions coming soon.

#### What it supports

- Core S3 commands: GetObject, PutObject, DeleteObject and list (ls).

- Encryption at rest & in transit: All data flows are encrypted by default (no user-managed keys required).

- Multipart uploads: Handle large files in parallel for faster transfers.

## Getting Started

- Sign in to the Lambda Cloud dashboard.

- Create or select your filesystem.

- Generate your S3 access keys.

- Connect with your S3 client (rclone, s5cmd, AWS CLI) and begin transfers.

Curious about how the Filesystem S3 Adapter works in practice? Check out our step-by-step tutorial video to see how you can streamline your data workflows without the need for a VM.

For detailed information on setup and usage check out the full documentation.

## Looking ahead 

This release focuses on your essential data-transfer needs. In the coming months, we’ll expand to deeper integrations with ML frameworks, richer metadata support and custom performance tuning.

Ready to streamline your data workflows? 

Sign up now to start using the Lambda S3 Filesystem Adapter, and get back to what really matters: training smarter models faster.

## AUTHORED BY

 Anket Sah

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
