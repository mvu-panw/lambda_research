# Lambda to integrate open-source NVIDIA Run:ai with its Managed Kubernetes Service

Source: https://lambda.ai/blog/runai-on-lambda-kubernetes-service

Skip to main content

# Lambda to integrate open-source NVIDIA Run:ai with its Managed Kubernetes Service

 October 13, 2026

 (Updated on October 22, 2026)

 • 3 min read

We welcome NVIDIA's decision to release NVIDIA Run:ai as open source, and we're working to make it a first-class option on Lambda Kubernetes Service (LKS).

NVIDIA Run:ai provides AI workload and GPU orchestration within NVIDIA DSX OS, the open, modular software portfolio of the NVIDIA DSX AI Factory Platform. Lambda, the AI cloud, has supported customer-deployed NVIDIA Run:ai on our infrastructure since 2022. 

Building on that experience, Lambda plans to make NVIDIA Run:ai available as part of the AI software library with LKS, giving teams a simpler way to deploy and operate it while gaining greater control over how they allocate and share GPU capacity. The open-source release gives Lambda the flexibility to package, validate, and maintain NVIDIA Run:ai directly as part of the LKS experience.

The planned integration of NVIDIA Run:ai with LKS is intended to help teams use shared GPU infrastructure more efficiently and reliably. NVIDIA Run:ai will schedule AI workloads and allocate GPU capacity across teams and projects, while LKS manages the underlying Kubernetes environment and monitors, isolates, and remediates unhealthy GPU nodes. When available, the integration will give teams greater control over GPU sharing while Lambda keeps the infrastructure beneath it healthy and available.

## Why fixed GPU allocation leaves capacity idle

AI development puts varied demands on GPU resources. A debugging session may use a fraction of a GPU. An evaluation may launch many independent jobs. Distributed training may require many tightly connected GPUs at once, and those needs change as a project moves from idea to experiment to production.

When small jobs reserve whole GPUs, unused capacity cannot be assigned elsewhere, leaving other researchers waiting. The same friction appears across teams, when one group's experiments queue behind another group's idle allocation. Both turn available hardware into delays between experiments.

## How NVIDIA Run:ai handles GPU sharing and scheduling

NVIDIA Run:ai extends Kubernetes with GPU-aware scheduling and resource management for shared AI infrastructure. It allows multiple workloads to share a single GPU and applies quotas, priorities, and fair-share policies across teams and projects. This helps organizations keep GPU capacity productive while giving teams predictable access to the resources they need. The result is higher GPU utilization and workload throughput on shared AI infrastructure.

Two capabilities make this possible:

- GPU fractions that let small workloads use a portion of a GPU, allowing multiple workloads to run on the same physical device.

- Scheduling policies that give teams defined allocations while allowing them to borrow unused capacity and return it when higher-priority workloads need it.

Together, these capabilities help answer two practical questions: how much GPU capacity a workload needs, and how shared infrastructure should respond as demand changes across teams.

## Keeping GPUs healthy with node auto-remediation

Sharing and preemption both rest on an assumption that the GPU underneath is healthy. On GPU compute at scale, that’s not a given. Accelerators throw XID errors, high-speed links degrade, memory rows get remapped, and networking ports drop below their expected rate. Without active monitoring and remediation policies, a scheduler can’t tell a healthy GPU from a failing one, so it keeps sending jobs to a node that drops them.

This is the part LKS owns. LKS is managed Kubernetes on Lambda GPUs, and auto-remediation ships in it today: Lambda monitors every node for those faults and surfaces each as a standard Kubernetes node condition. When one fires, the node is cordoned so nothing new schedules to it, running work is drained, and the fault is either corrected automatically or escalated straight to hardware repair. The node returns only after it revalidates. Faulty GPU isolation and remediation become a routine event rather than an incident, which lets a scheduler above it keep placing work without anyone filing a ticket.

## Bringing NVIDIA Run:ai to LKS

LKS is designed to support a library of AI software delivered as managed components that Lambda validates against its hardware and keeps current. Lambda plans to make NVIDIA Run:ai a first-class managed option in that library. The open-source release makes this possible by allowing Lambda to package, test, and maintain NVIDIA Run:ai as part of LKS rather than provide customers with integration instructions alone. Lambda is aiming for an out-of-the-box integration and will own the packaging, validation, and ongoing operations.

As a company that produces open research, Lambda values being able to inspect, adapt, and improve the tools we depend on. NVIDIA's decision to release NVIDIA Run:ai as open source extends that freedom to orchestration. That is the direction we see for AI infrastructure, and where we are taking LKS. When the integration becomes available, teams can control how GPU capacity is allocated and shared, while LKS keeps the underlying infrastructure healthy and available.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
