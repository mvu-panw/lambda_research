# Lambda at NVIDIA GTC 2026: our thoughts

Source: https://lambda.ai/blog/lambda-at-nvidia-gtc2026-our-thoughts

Skip to main content

# Lambda at NVIDIA GTC 2026: our thoughts

 March 31, 2026

 • 4 min read

The industry stopped asking, ‘What's possible?’ and started asking, ‘Who can deliver?’

NVIDIA GTC 2026 drew over 30,000 attendees, and the tone had shifted. Engineers and infrastructure teams weren't there to explore what's possible. They were there to gauge what works and who can deliver it. Open models, inference workloads, and system-level constraints came up repeatedly, from Jensen Huang’s interviews to discussions on the floor. The focus was on how to run models reliably at scale.

For Lambda, that's validation of work already underway.

## What the conference confirmed about our infrastructure bets

Every announcement at NVIDIA GTC 2026 was significant in its own right, but what stood out even more was the consistency of the underlying themes. Three challenges kept surfacing across keynotes, conversations, and product announcements: how to scale compute beyond the GPU, how to move data fast enough to achieve higher GPU utilization, and how to build networks that hold up at rack and data center scale. 

Lambda was among the first AI-native clouds and an early NVIDIA Cloud Partner to announce bare-metal instances on NVIDIA Vera Rubin NVL72, with systems arriving in H2 2026. The unit of compute is no longer limited by GPUs alone; it’s the data center. Unlocking the full performance of the data center requires direct hardware access with minimal abstraction and no virtualization overhead.

As an early launch collaborator on the NVIDIA Vera CPU, we built our architecture around a principle often overlooked: CPU performance matters. From orchestration of GPU infrastructure, to executing agentic tools and managing software environments, CPU performance impacts how quickly models learn and how responsively agents act.

In networking, Lambda is among the first to deploy NVIDIA Quantum-X InfiniBand Photonics in production, on a 10,000-GPU NVIDIA GB300 NVL72 cluster. At this scale, networking is not just a bandwidth problem. It becomes a problem of power efficiency, reliability, and operability.

Finally, our participation in the NVIDIA BlueField-4 STX ecosystem places us among a select group focused on deploying and operating systems well adapted to the data challenges of real-world inference at scale. 

Taken together, these decisions reflect a focus on building systems that are production-ready for large-scale training and inference.

## Three structural shifts defining the next era of AI infrastructure

#### Inference is now the primary workload.

While clusters for training remain massive, inference is now the dominant workload. Agentic systems have shifted the bottleneck to memory bandwidth, KV cache management, and data movement. Raw FLOPs matter less than the efficiency with which data moves through the system. We prioritize balanced CPU-GPU systems and memory architectures designed for continuous, long-context workloads, not just peak training throughput.

#### The data center is the unit of scale.

The days of evaluating a GPU in isolation are over. Teams now want to understand how compute, memory, networking, power, and cooling work together. The shift to rack-scale systems that expand to data centers reflects the need for coordinated performance across the entire stack.

#### The market has moved to execution.

The key question is no longer “what is possible?” but “what works, and who can deliver?” Throughout the conference, customers moved from exploration to vendor selection and capacity planning. Evaluation cycles are shrinking, and the need for proven ability to execute and deliver next-generation hardware is greater. We’re shipping NVIDIA Vera Rubin NVL72 as bare-metal instances in H2 2026, with the system architecture required to run them effectively.

## What engineers actually asked us on the floor 

Beyond Jensen's keynote, some of the most valuable signals at NVIDIA GTC came from direct conversations. What's changed is where the requirements originate. ML and AI engineers are more prescriptive about the compute configuration required to meet their specific workloads. Co-engineering is now the critical path to success: workload expertise met by infrastructure expertise.  

We were asked about data locality: specifically, which regions could support workloads without cross-region latency penalties. Then, about long-context inference strategies, KV cache pressure at 128K+ lengths, and memory architecture under sustained load. We were also asked about capacity: what compute could be provisioned, and when.

When we demonstrated our real-time region availability maps, our 1-Click Cluster provisioning, and our transparent Model FLOPS Utilization results, we moved conversations quickly from pitch to planning. Customers pushed for proof under real workloads, not ideal benchmarks. This shift is pushing the industry from narrative-driven claims to measurable performance.

## The race to execute has begun. Here is where we are focused

NVIDIA GTC 2026 confirmed our trajectory. What differentiates teams now is co-engineering and execution: delivering production-grade systems that meet precise specifications and work at scale.

In H2 2026, we begin deploying NVIDIA Vera Rubin NVL72 as bare-metal instances. Our focus is on building balanced CPU-GPU systems with predictable, high-scale networks, designed with memory architectures that improve utilization in production. This gives customers full control over hardware and software, with no abstraction layers. 

NVIDIA GTC has evolved from a developer-centric forum into a broader forum for how AI infrastructure gets built. The engineers we spoke with at GTC weren't exploring. They were deciding. If you're in that stage too, we'd like to help.

Talk to our team.

## AUTHORED BY

 Khushboo Goel

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
