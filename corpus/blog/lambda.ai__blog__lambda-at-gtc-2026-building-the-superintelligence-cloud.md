# Lambda at NVIDIA GTC 2026: building the Superintelligence Cloud

Source: https://lambda.ai/blog/lambda-at-gtc-2026-building-the-superintelligence-cloud

Skip to main content

# Lambda at NVIDIA GTC 2026: building the Superintelligence Cloud

 March 16, 2026

 • 6 min read

Lambda announces NVIDIA Vera CPUs, new Lambda Bare Metal Instances, NVIDIA Photonics, and NVIDIA STX coming to the Superintelligence Cloud.

Today, Lambda is announcing the expansion of our AI factories to include NVIDIA Vera CPUs to power the software environments behind reinforcement learning and agentic AI, new Lambda Bare Metal Instances on NVIDIA Vera Rubin NVL72 Superclusters, a production-scale NVIDIA GB300 NVL72 Supercluster with NVIDIA Quantum-X Photonics, and our role as an early NVIDIA BlueField-4 STX adopter.

## Lambda is an early NVIDIA Vera CPU launch partner

Models no longer just generate responses. They plan, call tools, run code, and interact with software environments in continuous feedback loops. Intelligence now extends beyond the model into surrounding systems, where millions of CPU-based sandbox environments execute actions and return results to GPUs.

For modern agentic workloads, evaluation latency directly affects overall system performance. When sandbox environments fall behind, accelerators must wait for results. Higher per-core CPU performance increases reinforcement learning iterations per GPU hour and improves agent responsiveness, maximizing AI factory throughput across training and inference.

NVIDIA Vera—high-density CPU capacity for AI factories:

- 88-core CPU with high single-thread performance, tuned for latency-sensitive tasks

- 

Spatial multi-threading increases agentic inference and RL sandbox density

- 

Up to 1.5 TB of LPDDR5X memory capacity and 1.2 TB/s bandwidth configurations

- 

Up to 1.8 TB/s CPU-to-GPU connectivity, reducing PCIe bottlenecks

The development of modern models involves both long training runs and millions of short evaluations. NVIDIA Vera reduces evaluation time, increases the density of sandboxes per rack, and stabilizes per-core throughput. The result is repeatable behavior when you scale experiments into production.

## Lambda is an early NVIDIA BlueField-4 STX partner

While the industry is shifting toward agentic AI, long-term memory and the processing of massive context windows are critical bottlenecks in inference. NVIDIA STX is a modular reference architecture for rack-scale AI storage, accelerating advanced inference through next-generation hardware integration and optimized KV-cache management.

Lambda is an early NVIDIA STX adopter, so the storage layer never becomes the bottleneck for frontier-scale GPU clusters:

- 

Context memory at scale: Up to 5x higher tokens per second and 5x greater power efficiency than traditional storage.

- 

Acceleration at every layer: Full cluster integration of NVIDIA Vera CPUs, Rubin GPUs, BlueField-4 DPUs, and Spectrum-X Ethernet networking for data center-scale workloads.

- 

Foundation for AI-native data platforms: High-speed data access for context memory, enterprise data, and high-performance storage use cases.

NVIDIA STX-based platforms will be available in the second half of 2026, along with our NVIDIA Vera Rubin NVL72 Superclusters.

## Lambda Bare Metal Instances on NVIDIA Vera Rubin NVL72 Superclusters

Today, Lambda is announcing Bare Metal Instances on Superclusters with NVIDIA Vera Rubin NVL72.

For teams running large-scale foundation model training and complex distributed workloads, such as disaggregated inference, direct hardware access matters. Virtualization overhead is not theoretical at this scale. It compounds. Bare metal removes that layer entirely, while Lambda's Bare Metal Instances provide cloud usability.

#### What Lambda Bare Metal Instances give you

- 

Higher performance with no hypervisor overhead

- 

Faster access to the newest compute as it becomes available

- 

Full control over the hardware stack with no shared neighbors

- 

Complete security oversight from the firmware layer up

What we built differently

- 

One-to-one mapping between instances and physical hosts, with API parity for lifecycle operations. You get direct access to CPU, GPU, memory, and local storage while managing instances the same way you manage cloud VMs.

- 

With no hypervisor mediating device access, workloads run directly on the underlying hardware, and your processes communicate directly over sixth-generation NVIDIA NVLink for scale-up and NVIDIA Quantum-X800 InfiniBand for scale-out. All-reduce, tensor parallel, and disaggregated prefill-decode traffic run over the raw fabric.

- 

When a host degrades or fails, instance mobility moves your workload to healthy hardware without manual intervention, enabling faster recovery.

You get the performance of raw bare-metal servers, with programmatic provisioning, predictable maintenance, and observability built for production ML.

Learn more at Maxx Garrison’s session about what deployment will look like for Lambda's Bare Metal Instances with NVIDIA Vera Rubin NVL72 and NVIDIA GB300 NVL72, covering what rack-scale readiness actually requires.

## Lambda's NVIDIA GB300 NVL72 Supercluster with NVIDIA Quantum-X Photonics

At scale, the fabric is the system. You can’t bolt a high-performance network onto a rack that wasn’t engineered for it from the start.

Lambda is leading one of the largest deployments of NVIDIA Quantum-X InfiniBand Photonics co-packaged optics switches to date, in an AI factory with 10,000+ NVIDIA GB300 GPUs. CPO switches eliminate the bandwidth bottleneck between racks and change the performance-per-watt calculus at cluster scale. We announced our work on NVIDIA CPO and next-generation networking fabrics in 2025. Now it’s running in production.

#### What we engineered for

- 

Rack-first design: Power and liquid cooling are planned so racks run at sustained utilization without thermal or electrical surprises when jobs push the system hard.

- 

Photonics fabric: NVIDIA Quantum-X InfiniBand Photonics CPO switches lower power, increase bandwidth, and improve resilience. That raises cluster-level bisection bandwidth and reduces energy per unit of useful work.

- 

Validated NVIDIA GB300 NVL72 scale: Lambda hosts NVIDIA GB300 NVL72 clusters at the scale required for frontier training while preserving deterministic fabric behavior across the full job.

This Supercluster is built to run large NVIDIA GB300 NVL72 jobs repeatedly and reliably. That reduces surprises and lowers the cost per useful result.

## Bringing it together: Lambda's full-stack validation

We validate the full stack before we hand over clusters: production firmware, drivers, and orchestration are tested as a single unit. Then we follow a pilot-to-production rollout so capacity, software, and operations arrive together:

- 

Small-scale NVIDIA PODs to validate sandbox density and CPU-to-GPU connectivity before full-scale deployment

- 

Phased rollouts so software and tooling scale alongside capacity

- 

Out-of-band telemetry and DPU-based controls to monitor and manage fabric without adding noise or removing resources from AI workloads

The system runs the same jobs repeatedly with minimal manual intervention. That’s how infrastructure moves from working in a lab to running in production.

NVIDIA Vera CPU delivers predictable CPU throughput. Rack-first engineering and photonics networking make the fabric scalable. Bare Metal Instances give teams control without operational overhead. Together, they make the Superintelligence Cloud a platform teams can trust in production.

We're also participating in NVIDIA's Fleet Intelligence Early Access Program to help develop telemetry, alerting, and integrity checks that will give you earlier visibility into GPU fleet issues before they escalate into workload-affecting outages. To see how these capabilities fit into a broader AI operations strategy and how NVIDIA and Lambda are collaborating to close the gap between standing up AI infrastructure and running it confidently at scale, catch "A Playbook – Operating Cloud AI Factories at Scale" [S81847] on Monday, March 16 at 3:00 p.m. PDT.

## Engage with Lambda at NVIDIA GTC

- 

Meet with our team at booth #1507 or book an in-person session at lambda.ai/nvidia-gtc

- 

Join the session on deploying Lambda's Bare Metal Instances with NVIDIA Vera Rubin NVL72 and NVIDIA GB300 NVL72.

## AUTHORED BY

 Khushboo Goel

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
