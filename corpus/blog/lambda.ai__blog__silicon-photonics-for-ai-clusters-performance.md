# Silicon Photonics for AI Clusters: Performance, Scale, Reliability, and Efficiency

Source: https://lambda.ai/blog/silicon-photonics-for-ai-clusters-performance

Skip to main content

# Silicon Photonics for AI Clusters: Performance, Scale, Reliability, and Efficiency

 November 21, 2025

 • 4 min read

 Scaling AI Compute Networks

Frontier AI training and inference now operate at unprecedented scale. Training clusters have moved from thousands and tens of thousands of NVIDIA GPUs just a few years ago to 100,000+ and soon millions of contiguous, interconnected GPUs as model sizes and training data sets have continued to scale. Even inference, broadly considered a single node or a single GPU workload, has shown much higher Token/GPU throughput when served in a distributed, disaggregated manner across hundreds of GPUs. Test-time scaling via reasoning models, agentic workloads, and post-training with inference-heavy reinforcement learning have continued to ramp up the volume of cluster-based inference.

For Lambda, building GPU clusters at this scale now means designing the GPU interconnect network as a core part of the compute architecture rather than a supporting layer. Redesign of the compute interconnect network, also known as the compute fabric, East-West network, back-end network, or scale-out network, has accelerated to match the annual pace of GPU refresh cycles. Leading-edge AI clusters require denser, more efficient networks capable of connecting hundreds of thousands of GPUs while improving energy efficiency, reliability, performance, and scalability.
What Is Co-Packaged Optics (CPO)

​​Traditional network switches with pluggable optical transceivers rely on long, high-speed electrical traces. The data signal travels from the switch application-specific integrated circuit (ASIC) across the printed circuit board (PCB), through connectors, and into the separate transceiver module, where it is converted into an optical signal. Inside the transceiver, the electro-optical conversion requires a digital signal processor (DSP) or retimer for signal correction, along with a laser subsystem. Each transition, from switch ASIC to trace, connectors, module electronics, and then to fiber-optic cable, introduces signal loss. The additional active components required to compensate for these transitions and signal loss increase power consumption.

Co-packaged optics with silicon photonics simplify the data path by placing optical components such as laser transmitters, modulators, and photodetectors directly on or next to the same package as the switch ASIC. In practice, this means much shorter trace lengths, fewer connections, and removal of multiple active components, enabling better signal loss, lower latency, and reduced power consumption compared with conventional pluggable optics.
Why CPO Matters for AI Compute Networks

NVIDIA Quantum-X Photonics InfiniBand and NVIDIA Spectrum-X Photonics Ethernet switches use co-packaged optics (CPO) with integrated silicon photonics to provide the most advanced networking solution for massive-scale AI infrastructure. CPO addresses the demands and constraints of GPU clusters across multiple vectors:

- Lower power consumption: Integrating the silicon photonic optical engine directly next to the switch ASIC eliminates the need for transceivers with active components that require additional power. At launch, NVIDIA mentioned a 3.5x in power efficiency improvement over traditional pluggable networks.

- Increased reliability and uptime: Fewer discrete optical transceiver modules, one of the highest failure rate components in a cluster, mean fewer potential failure points. NVIDIA cites 10x higher resilience and 5x longer AI application runtime without interruption over traditional pluggable networks.

- Lower latency communication: Placing optical conversion next to the switch ASIC minimizes electrical trace lengths. This simplified data and electro-optical conversion path provides lower latency than traditional pluggable networks.

- Faster deployment at scale: Fewer separate components, simplified optics cabling, and fewer service points mean that large-scale clusters can be deployed, provisioned, and serviced more quickly. NVIDIA cites 1.3x faster time to operation versus traditional pluggable networks.

How Lambda Plans to Leverage It

Lambda is preparing its next-generation GPU clusters to integrate CPO networking using NVIDIA Quantum-X Photonics InfiniBand and Spectrum-X Photonics Ethernet switches. These advances in silicon-photonics switching are critical as we design massive-scale training and inference systems. For Lambda’s NVIDIA GB300 NVL72 and NVIDIA Vera Rubin NVL144 clusters, we are adopting CPO-based networks to deliver higher reliability and performance for customers while simplifying large-scale deployment operations and improving power efficiency.

Two-layer 1,152 GPU NVIDIA GB300 NVL72 Cluster with Quantum-X800 Photonics switches

By using CPO-based networking as a core element of our compute architecture, we can enable key infrastructure advantages for Lambda and our customers, including:

- High-bandwidth, low-latency, and reliable GPU interconnects as cluster sizes increase to 100k+ GPUs

- Reduced deployment complexity, fewer discrete transceiver modules, and streamlined optical cabling and service

- Improved power-and-cooling efficiency in the network layer, freeing more of the data center power budget for GPUs and improving overall cluster efficiency

As AI workloads continue to demand ever-greater scale and throughput, CPO networking will be a foundational enabler of Lambda’s mission to deliver high-performance, scalable, and efficient GPU compute infrastructure.
Ready to build on infrastructure designed for scale?

From frontier model training to distributed inference, Lambda's CPO-enabled GPU clusters are engineered to handle the most demanding AI workloads. Whether you're planning your next large training run or designing for distributed inference, we can help you architect the right solution.

Talk to our team to learn more about CPO-based clusters.

## AUTHORED BY

 Maxx Garrison

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
