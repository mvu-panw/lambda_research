# Why your Kubernetes scheduler can't handle AI workloads

Source: https://lambda.ai/blog/why-your-kubernetes-scheduler-cant-handle-ai-workloads

Skip to main content

# Why your Kubernetes scheduler can't handle AI workloads

 July 16, 2026

 • 8 min read

Imagine this scenario: You have a distributed training job with 16 worker pods, each requesting 1 GPU. 4 GPUs are currently available. The default Kubernetes scheduler (kube-scheduler) may schedule those 4 pods while the remaining 12 stay pending.

Meanwhile, those 4 GPUs are reserved by pods that cannot make progress until the full distributed job is ready. No one else on the cluster can use them. Your job isn't actually training. The other cluster users' jobs can't use those reserved GPUs either. The cluster is busy doing absolutely nothing.

This is a classic partial-scheduling deadlock. By default, kube-scheduler doesn't gang-schedule; the feature exists in alpha but ships disabled. It schedules pods one at a time, meaning it has no concept of "all pods in this job must start together, or none of them start."

The second problem is that kube-scheduler lacks multi-node fabric topology awareness. While it can track basic on-node constraints such as available CPU or memory capacity, it doesn’t account for which separate nodes share the same NVIDIA Quantum, or how high-bandwidth interconnects are routed across the cluster network. It places pods wherever capacity exists. For distributed training, this introduces severe communication latency that throttles performance at scale.

For teams running small jobs on a few GPUs, this inefficiency is tolerable. For AI/ML organizations running distributed training across dozens or hundreds of GPUs, it breaks the entire workflow.

## What's gang scheduling?

To put it simply: gang scheduling means all pods in a job start together, or none of them start.

If a job requires 16 GPUs and only 4 are available, a gang-aware scheduler queues the entire job and releases the 4 available GPUs for other work. When all 16 become available simultaneously, the job launches as a single unit.

There is no partial allocation, no idle GPUs locked by a waiting job, and no deadlock. Because this functionality is not built into standard Kubernetes, you need a scheduler extension or replacement that supports it.

## Three schedulers built for AI workloads

When moving beyond standard Kubernetes for AI workloads, three primary options dominate the ecosystem. Each serves a distinct purpose depending on your organization's bottlenecks.

### 1. Kueue

Kueue is a Kubernetes-native job-queueing and quota management layer. It sits on top of the default scheduler, controlling which jobs are admitted to the cluster and how resources are shared across teams.

- Core Strength: Multi-tenant governance. It excels at managing quotas, fair-share scheduling, resource borrowing between teams, and strict admission control. Kueue doesn’t replace kube-scheduler; it controls the queue that feeds it.

- Best For: Organizations where the primary problem is resource contention and fair sharing between multiple teams, rather than physical GPU placement.

- Limitation: Kueue provides gang admission—which natively prevents the partial-allocation deadlock mentioned above—but it does not handle pod-level scheduling or fabric topology placement. For advanced network fabric optimization, teams often pair Kueue with Volcano: Kueue for organizational admission, Volcano for fine-grained pod scheduling. 

### 2. KAI Scheduler

KAI Scheduler is an open-source, AI/ML-focused, Kubernetes-native scheduler derived from the proven scheduling technology behind NVIDIA Run:ai. It is available both as a standalone CNCF Sandbox project and as part of the NVIDIA Run:ai platform.

- Core Strength: AI-native scheduling for performance at scale. It combines gang scheduling, GPU-aware resource allocation, workload consolidation, and topology-aware placement to maximize cluster utilization and distributed workload performance, helping reduce communication latency for distributed AI workloads.

- Best For: Organizations running large NVIDIA GPU clusters where physical GPU topology and maximum utilization efficiency are the top priorities.

- Consideration: It has a proven track record as part of NVIDIA Run:ai, while its open-source community continues to grow around its highly specialized focus.

### 3. Volcano

Volcano is a CNCF project and the most mature batch scheduling system available for Kubernetes. It has been battle-tested in production for years across AI/ML, HPC, and big data workloads.

- Core Strength: Mature gang scheduling, preemption, priority queues, and deep, native integration with popular ML frameworks like PyTorch, TensorFlow, MPI, Horovod, Ray, and Apache Spark. Volcano completely replaces kube-scheduler for targeted workloads.

- Best for: Organizations already running distributed training at scale that need proven gang scheduling and broad, out-of-the-box framework support.

- Consideration: It comes with higher operational complexity and a larger configuration surface area than a queueing layer like Kueue.

## Side-by-side comparison

 | 

Dimension

 | 

Kueue

 | 

KAI Scheduler

 | 

Volcano

 | 

Primary Role

 | 

Queueing and quota layer

 | 

GPU/AI workload scheduler

 | 

Batch scheduler

 | 

Replaces kube-scheduler?

 | 

No

 | 

Yes, for GPU workloads

 | 

Yes, for targeted workloads

 | 

Gang Scheduling

 | 

Gang admission natively (pair with Volcano for pod-level control)

 | 

Built-in

 | 

Built-in, highly mature

 | 

GPU Topology Awareness

 | 

Not the focus

 | 

Strong (NVIDIA NVLink, NVIDIA Quantum InfiniBand)

 | 

Framework/task topology support; fabric-topology features emerging

 | 

Multi-Tenant Quotas

 | 

Strong

 | 

Strong, GPU-focused

 | 

Strong

 | 

Framework Integrations

 | 

Works with standard K8s controllers

 | 

AI/ML focused

 | 

PyTorch, TensorFlow, MPI, Ray, Spark, and more

 | 

Maturity

 | 

GA, growing adoption

 | 

Validated technology; newer CNCF project

 | 

Most mature CNCF project

 | 

Best Starting Point For

 | 

Multi-tenant resource governance

 | 

NVIDIA GPU cluster optimization

 | 

Distributed training at scale

## Common deployment patterns

Choosing a scheduler isn't always about picking just one; it’s about finding the combination that fits your architecture.

- Kueue + Volcano: Kueue handles macro-level admission and quota governance across teams, while Volcano handles micro-level gang scheduling and pod placement. This is a very common pattern for enterprise multi-tenant clusters running massive distributed training.

- KAI Scheduler Standalone: Ideal for dedicated, NVIDIA-centric AI clusters where maximizing hardware performance via topology and consolidation is the absolute highest priority.

- Volcano Standalone: Built for infrastructure teams that need mature gang scheduling and broad framework support without the operational overhead of managing a separate queueing layer.

## How Lambda helps

Modern AI infrastructure requires more than GPUs: it requires scheduling that understands distributed AI workloads. Evaluating which scheduler fits your specific workload, machine learning framework, and physical cluster topology can be a daunting architectural hurdle. Whether you are adding managed Kubernetes to a 1-Click Cluster, a Reserved Private Cloud, or a massive Supercluster, the right choice depends heavily on your team's specific mix of frameworks (PyTorch, TensorFlow, Ray), cluster size, multi-tenancy needs, and GPU topology.

Lambda’s solutions engineers don't prescribe a one-size-fits-all scheduler. Instead, we partner with your team to evaluate your workloads, help you choose the right scheduling architecture, and ensure it is seamlessly implemented.

Talk to our team to optimize your cluster scheduling.

## AUTHORED BY

 Cody Brownstein

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
