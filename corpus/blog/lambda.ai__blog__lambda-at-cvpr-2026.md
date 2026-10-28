# Building at the speed of research: Lambda at CVPR 2026

Source: https://lambda.ai/blog/lambda-at-cvpr-2026

Skip to main content

# Building at the speed of research: Lambda at CVPR 2026

 June 9, 2026

 (Updated on October 22, 2026)

 • 6 min read

Every year, CVPR draws the researchers defining what AI can see, understand, and act on. This year in Denver, more than 9,000 attendees showed up with over 4,000 accepted papers, and one shared problem we saw underneath much of it: compute. And CVPR’s program committee saw it too. For the first time this year, they required a compute-reporting form on every submission — a sign that compute is becoming a first-class variable, not an afterthought.

Closing the gap between a strong idea and a verified solution takes compute. Lambda came to Denver as part of the community, doing the work. Two accepted papers. Two workshops. A Kodiak autonomous truck demo. And a booth where the conversations ran from model architectures to cluster configurations.

Here's what we did, and what we learned.

## The compute wall

A researcher leaves CVPR with a paper to implement, a model to scale, an idea to test before the next submission deadline. Then the work stalls: the capacity isn’t there when the deadline is.

This pattern came up at the booth over and over.

Two issues came up repeatedly. The first was getting GPUs at all, which comes down to both cost and availability. Compute budgets are limited to begin with, and scarcity makes it worse: a lab validates an idea on a small scale, then can't scale it up to achieve real impact. Because it's too expensive, because the GPUs aren't available, or both. Smaller labs feel this most, and many treat low-budget projects as a necessity rather than a choice. The second issue was operating at scale, which applied to well-resourced labs: scaling from a single node to multi-node requires system expertise in profiling, identifying bottlenecks in individual workloads, and optimizing resource utilization across an entire cluster. This adds ongoing engineering and operational costs on top of the initial hardware cost.

## Who we met

CVPR's audience splits into two groups Lambda serves directly: researchers publishing at the frontier of computer vision, embodied AI, and autonomous systems, and the engineers who take that research into production. At CVPR 2026, 57% of attendees were from R&D and 28% from education. These are the people training the models, running the experiments, and deciding which cloud they'll use for the next project life cycle.

## What we brought

Lambda's public cloud was built for this audience. On-demand GPU instances at published prices, no lock-in. 1-Click Clusters that let you quickly and cost-effectively provision multi-node workloads at scale. And Lambda's Research Grant Program, which gives researchers direct access to compute. At CVPR, we announced an expansion covering entire research groups, not just individual grants.

### Papers and workshops

- 

PixARMesh: Autoregressive Mesh-Native Single-View Scene Reconstruction. Co-authored with UC San Diego, led by Lambda intern Xiang Zhang. PixARMesh approaches 3D scene reconstruction from a single image using an autoregressive, mesh-native method. A step forward in how vision models represent 3D geometry. 

- 

Beyond Reassembly: Fractured Object Recovery with Missing Parts. Co-authored with Tsinghua, Bath, VAST, and Tencent ARC. Beyond Reassembly introduces a new task, fractured object recovery: it jointly reassembles an object's existing parts and predicts its missing ones, using a transformer that represents missing parts as tokens. The result is reconstruction from incomplete input. 

- World Models Meet Active Sensing and Closed-Loop Planning brought together researchers working at the intersection of perception, planning, and real-world deployment

- Rediscovering Intelligence: Can AI Still Learn from Humans? explored what human learning can still teach AI systems, with direct implications for training data design and model architecture

We also demoed other recent Lambda research in 3D vision, world models, and embodied AI, with collaborators from UCSD, Stanford, and JHU.

Beyond co-publishing, we released The Lab. As agents take on more of the research loop: branching hypotheses, running experiments, and iterating. They create experiment sprawl, and The Lab keeps that tracked, reproducible, and under control.

### The Kodiak demo

The most concrete proof Lambda brought to Denver was Kodiak's. Kodiak trained GigaFusionNet, the unified foundation model behind their autonomous trucks, on Lambda's NVIDIA HGX H100 GPU clusters. At the booth, Kodiak's Head of AI, Shubham Shrivastava, walked through the compute decisions, the training architecture, and how a model moves from data center to the truck.

Twenty-eight trucks. No one in the cab. The model behind them was trained on Lambda in under a week, at twice the iteration speed of their previous setup.

## What we learned

The dominant theme was physical AI: modeling and reasoning about the physical world. It’s the fastest-growing field where multimodal models, world models, and embodied AI converge.

The main change from last year is resource intensity and heterogeneity. The rise of physical AI has driven up demand for both compute and data, and has pushed workloads that combine training, rendering, physics simulation, and inference to roll out rather than training alone.

The field is scaling hard and trying to make scaling cheaper at the same time. On one hand, the work keeps getting bigger: foundation-model architectures reused across tasks and trained on more synthetic, simulation-generated data. But there's an equally real efficiency push underneath: faster inference, caching, and getting more out of the same hardware.

A similar tension runs through the data. In embodied AI, for instance, you can train on cheap, abundant synthetic data and pay later to bridge the sim-to-real gap, or learn directly from real demonstrations through imitation learning, while facing data scarcity and limited generalization.

Both workshops we ran pushed on this from different angles. World Models Meet Active Sensing claims generative world models have mastered passive generation, but real intelligence is active. For anyone putting perception into a robot or a vehicle, the closed-loop gap, not visual fidelity, is the real bottleneck. ReLearn came at it from the other side: smarter data design and human-inspired structure can sometimes substitute for brute-force scale. This is a healthy counterweight in a year when everyone's anxious about compute.

One thing we didn't expect was how many autonomous-driving companies were on the exhibition floor. The last time it looked like this was around 2019, when AV startups were leading the pack in the exhibits. Seven years on, the technology has matured, and the names have changed. This time, it was more than demos, as the work is embodied in real vehicles: sedans, trucks, even racing cars, thanks to the scaling laws of compute, data, and model quality.

For Lambda, the takeaway is that infrastructure has to keep pace with workloads that change this fast. This is why we partner with labs in academia and industry and co-publish. The best way to understand what researchers need isn't just to be their vendor, but their peer.

## What's next

A researcher leaves CVPR with an idea. They spin up an instance that afternoon. They're running experiments that same evening. A week later, they've validated the approach and scaled to a cluster for the full training run. No sales call. No waiting for capacity.

Lambda's public cloud is built for the workloads that ML researchers and engineers are running right now: on-demand GPU instances, 1-Click Clusters, and a Research Grant Program that gives labs direct access to compute.

Start building on Lambda Cloud or apply for a research grant.

## AUTHORED BY

 Chuan Li

 Ksenia Anske

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
