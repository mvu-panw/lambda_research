# How SPREEAI cut storage costs by more than 30x and doubled model FLOPs utilization with Lambda

Source: https://lambda.ai/customer-stories/spreeai

Skip to main content

# How SPREEAI cut storage costs by more than 30x and doubled model FLOPs utilization with Lambda

Contact sales

Storage cost reduction
30x
reduction

Model FLOPs utilization (MFU)
43% 
(~20% to 43%)

Queue starvation reduction
74%
relative drop

Per-try-on inference time
< 10s
from 23 seconds

## SPREEAI and Lambda

## Executive summary

SPREEAI is building an AI commerce platform: the infrastructure that lets brands show customers what they’re buying before they buy it. The first capability to reach the market is photorealistic virtual try-on. A shopper uploads one photo and sees a garment from a brand's catalog rendered on their own body in under ten seconds. The same foundation extends across the commerce chain, from procurement through catalog production.

Building it takes a training pipeline more demanding than a text-based LLM. By early 2026, SPREEAI's pace of model development and experimentation had outpaced the infrastructure originally built to support it, which is a familiar position for any AI company moving quickly.

Working with Lambda's Machine Learning (ML) engineering team, SPREEAI rebuilt that pipeline over a single quarter.

Customer
 
SPREEAI

Website

 spreeai.com

Vertical
 
E-commerce

Products
 
1-Click Cluster

## Online shopping has a fitting room problem

Every year, online shoppers send back roughly $47 billion worth of clothing because it didn't fit.

Walk into a store, and you can feel the fabric, see how a garment drapes, and ask for personalized assistance. Shop online, and you’re guessing. Static poses, inconsistent size charts, and models who look nothing like you.

So shoppers solve it the only way they can. They order multiple sizes and keep one.
Return rates on online apparel run between 20% and 30%, the highest of any e-commerce category, and sizing and fit drive almost 70% of them (Coresight Research and Alvanon, 2025). In a $1.8 trillion online apparel market (Grand View Research, 2025), that’s the most expensive unsolved problem.

SPREEAI, an AI commerce platform built for luxury and high-street fashion brands, closes this gap. 

Outfit Builder, SPREEAI’s first product, turns a browser tab into a personal fitting room. You upload one photo and, in under ten seconds, see yourself wearing the garment, photorealistic and built from your own picture, not a generic avatar or a stock model. It does full outfits too, a top and a bottom together, the way you'd actually wear them.

Published industry benchmarks for well-executed virtual try-on report conversion lifts of 20% to 40% and return-rate reductions of 25% to 40% (those are category figures across the sector, not SPREEAI customer results).

Four people of different body types and skin tones wearing garments rendered by SPREEAI's virtual try-on in everyday settings.

## What it actually takes

When most people imagine virtual try-on, they picture Photoshop. A garment cut out and layered over a photo.

Commercial-grade try-on is a different discipline. SPREEAI's unified diffusion model has to solve four interdependent problems at once.

### Understand the human subject

Before generating a pixel, the model has to read how a person stands, since posture and balance decide where the fabric falls. And the input is unpredictable. A brand shoots its catalog in one controlled studio pose. A shopper sends whatever photo they have. The model has to place the garment right every time, and keep the person looking like themselves.

### Encode the garment

Fabric behaves. It stretches, drapes, stiffens, catches the light differently by weight and weave. The model learns how a structured blazer holds its shape, and how a soft knit gives and clings instead.

### Transfer the pose and style

The garment was photographed on one body in one pose. The model has to re-render it onto the shopper's stance, re-draping it to fit how they're standing.

### Preserve the scene

The model changes only what needs to change. If something hides part of the garment, it reconstructs what's behind it. If something belongs in front, like a handbag strap over the shoulder, it stays. The original lighting and setting carry through, so the result looks like the shopper's own photo.

“The human eye will pick up very quickly the uncanniness of it. They'll say, 'The logo looks distorted' or 'It's supposed to be an N. Why does it have a carrot on top?'”Mrinal Shukla, Head of Engineering @ SPREEAI

Four-stage diagram showing how SPREEAI's model reads the body, encodes the garment, transfers pose and style onto a different stance, and rebuilds only the region that changes.

Fidelity at that level takes work at every stage: high-resolution training, targeted upscaling, and extra headroom where fine detail is most at risk. Prints, patterns, and typography have to survive generation intact, and every output clears a set of quantitative quality gates before it reaches a shopper.

Solving all four together meant consolidating a multi-module architecture into one unified model. That speeds up development and simplifies validation, but demands the full memory footprint of a top-end NVIDIA H100 GPU. Around it sits a wider stack: vision-language models grade output quality at scale, flagging distortion and drift, while large language models automate configuration and orchestration across the training workflow.

## When the research outgrew the infrastructure

SPREEAI's training cycles are unusually data-heavy. Every run generates large volumes of intermediate output: synthetic imagery, snapshots used to benchmark regressions, and staged artifacts for each phase of the pipeline. Each cycle compounds the last, because every snapshot becomes the next run's baseline.

That pattern scales directly with research velocity, and SPREEAI's was climbing fast through 2025. The storage layer had been sized for an earlier stage of the company. By late in the year, storage costs were climbing faster than the research, and the pipeline needed rebuilding around it.

“We were using the storage as if it's just storage lying there, but eventually you learn that this storage is very expensive.”Mrinal Shukla

## Why the interconnect mattered

SPREEAI trains with distributed data parallelism across multi-node NVIDIA HGX H100 systems on Lambda 1-Click Clusters, so every optimizer step needs a full gradient all-reduce, and interconnect bandwidth becomes the binding constraint.

Diffusion models stress the interconnect differently than large language models (LLMs) do. Attention cost in an LLM is dominated by a KV cache that grows with sequence length, while a diffusion transformer recomputes attention across the image at every denoising step. Multiply that across a full pass and any latency in the fabric compounds through the run, surfacing as GPU idle time.

Lambda's 1-Click Clusters run on an NVIDIA Quantum-2 400 Gb/s InfiniBand non-blocking fabric in a rail-optimized topology, delivering up to 3,200 Gb/s of peer-to-peer GPUDirect RDMA between nodes. Gradient synchronization stayed off the critical path.

## More than 30x out of the storage layer

Lambda's persistent file storage carries no ingress, egress, or data transfer fees. That matters more than it sounds, because SPREEAI's pipeline isn’t a linear pass. Pose extraction feeds garment-conditioned training, checkpoints feed evaluation renders, and evaluation artifacts become the next run's regression baselines.

SPREEAI's team sat down with Lambda's ML engineers, audited the full data estate, and rebuilt the lifecycle around what they found. Zero egress let them move legacy data to lower-cost object storage, decoupling storage cost from throughput. That became a permanent workflow: orchestration now manages data shards and pulls in only what the current phase actually needs. Retention policies brought the live training footprint down by roughly an order of magnitude. With better pre-staging, storage I/O stalls disappeared.

Across a single quarter, storage costs dropped more than 30x.

“Unlike many other cloud providers, with Lambda, we don't have to pay ingress, egress, and data transfer fees when we're using it. It means that we have an uninterrupted flow of the overall training workload.”Mrinal Shukla

## Doubling model FLOPs utilization

Before the rebuild, model FLOPs utilization (MFU) sat in the low twenties even during active training windows. Workloads had been fragmented across features, some needing the HGX H100 system and some not, but all of them scheduled onto the same high-end hardware. GPUs also spent real time waiting on data that hadn't been pre-staged.

Lambda's ML engineers started with systematic workload profiling, tracing GPU idle time to three root causes: storage I/O stalls, an HGX H100 system allocated to jobs that didn't need them, and conservative numerical precision defaults.

That last one was the least obvious. Large parts of the training graph turned out to be stable at lower precision than they were running at, and right-sizing it reclaimed memory headroom and lifted per-GPU throughput.

SPREEAI then built experiment orchestration directly on Lambda's stack: H100 1-Click Clusters, Quantum-2 InfiniBand, and a persistent shared filesystem. Lambda supplied documentation, guidance, and working examples covering data pipelines and GPU observability, and SPREEAI wired Lambda's metrics APIs into their own dashboards.

MFU more than doubled, from roughly 20% to 43%. Queue starvation, meaning experiments blocked waiting on a GPU allocation, fell 74%.

“Eventually, our goal is not more GPUs, but it's to get more efficiency from our current GPUs.”Mrinal Shukla

## Serving COGS down roughly 65%

The cost to serve a try-on is the amortized cost of training plus the GPU wall-time each request consumes. SPREEAI and Lambda went after both, and the two are worth separating.

On wall-time: end-to-end profiling of the serving path cut per-try-on inference from 23 to 10 seconds by reducing denoising steps and tuning kernels. Tuning has continued since, and try-ons now return in under 10 seconds.

On cost: serving cost of goods sold (COGS) per try-on has fallen by roughly 65%. That figure isn't a restatement of the latency improvement. It combines the training efficiency gains above, the reduction in wall-time per request, and better throughput per GPU, which together let the same fleet absorb substantially higher daily volume with no added hardware and no extra reserved or spot capacity.

SPREEAI projects per-try-on time will reach three to four seconds by the end of 2026.

## What's next

SPREEAI handles static try-on today, for single garments and complete outfits. Next comes full layering, a shirt under a jacket or a dress over denim, and complete looks with accessorizing. Size-aware try-on is being built, so shoppers get a fit recommendation based on their photo instead of a static size chart.

The frontier is video.

One photo in. Every angle out.

Temporal consistency changes the problem. A model that produces a flawless single frame will still show artifacts once that frame sits in a sequence. Fixing it requires temporally consistent video diffusion, far more compute-intensive than image generation. The roadmap extends beyond a single clip to 360-degree video and custom sequences with distinct camera angles, so a shopper can check a garment from every angle, as they would in a mirror.

Try-on is just the entry point. The same platform extends across the commerce chain and into agent-to-agent ecosystems: wholesale procurement, where virtual visualization replaces physical sample shipments, and AI-generated fashion content that cuts catalog production costs while widening representation across body types, skin tones, and ethnicities.

Visit demo.spreeai.com, upload a photo, and see full outfits on yourself. Or pick from a library of virtual twins.

Read more about how SPREEAI trains their virtual try-on model on Lambda, and explore Lambda's 1-Click Clusters for your own workloads.

“Our North Star is a real-time video try-on. You walk into a store, flash a garment in front of a screen, and see it right on yourself. We want to be the ones bringing that to the world.”Mrinal Shukla
