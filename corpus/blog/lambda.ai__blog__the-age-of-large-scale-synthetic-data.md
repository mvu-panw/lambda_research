# We’re entering the age of large-scale synthetic data

Source: https://lambda.ai/blog/the-age-of-large-scale-synthetic-data

Skip to main content

# We’re entering the age of large-scale synthetic data

 June 18, 2026

 • 2 min read

To humans, the internet feels infinite, a vast, ever-expanding space of knowledge. To learning systems, it’s starting to look finite. A place where genuinely new learning signals are increasingly hard to find.

That limitation is forcing a shift: we’re entering the era of synthetic data.

What once felt speculative or an optional boost to real-world datasets is now becoming foundational. With each new result, the direction is set: models won’t just use synthetic data; they will depend on it. It may take time, but the trajectory is set. A significant portion of modern training pipelines is already synthetic. Estimates suggest OpenAI allocates 20-30% of its compute budget to generating it. Aggregate that across frontier labs, and we land on a large and growing market in compute demand.

In this shift, data and compute collapse into the same resource. What used to require human annotation is now expressed in GPU hours. The bottleneck is no longer labeling; it’s generation at scale.

Lambda is building for the synthetic data generation market. From generation pipelines to storage and infrastructure, our ML team is studying and scoping the systems required for large-scale synthetic data. Not as theory, but as practice. And we bring those learnings directly to our customers.

Our latest work makes that concrete.

## Introducing Sim2Reason

Accepted at ICML 2026, Sim2Reason asks a simple question: "Can an LLM learn to solve International Physics Olympiad problems using only synthetic data?"

Yes, it can.

The system turns physics simulators into scalable data engines. A domain-specific language procedurally generates diverse physical scenarios in MuJoCo: a ball rolling down a ramp, a pulley system in motion, a charged particle in a magnetic field. Each simulation produces complete physical traces: forces, velocities, accelerations, energy flows.

From these traces, the pipeline automatically constructs verified question–answer pairs across three modes:

- Numeric: "What's the velocity of block A at time 3s?"

- Reverse: "What must the mass of block A be for its velocity after 3s to equal 5 m/s?"

- Symbolic: "What's the velocity of block A as a function of time t?"

No human annotation. No hand-curated problems. Just simulation, then extraction, then supervision.

## What Sim2Reason achieved

Models trained purely on Sim2Reason data improved zero-shot performance on IPhO mechanics problems by 5–10 percentage points, across model sizes from 3B to 72B parameters. On JEEBench, gains reached +17.9% for 32B models. Improvements generalized across benchmarks, including OlympiadBench, PHYSICS, and even out-of-domain math-reasoning tasks such as AIME 2025 and MATH 500.

Sim2Reason surpassed DAPO-17K on physics transfer, and not by scaling data, but by aligning it. Synthetic data, when generated from the right process, produces a higher-signal distribution than generic internet corpora.

More data doesn't solve the problem. Better data does.

## What’s next

Sim2Reason is one paper. The shift it represents is already underway.

At Lambda, we’re actively studying the emerging field of large production-level synthetic data. We’re listening to our customers, learning about their needs and the tools that help them achieve their goals on our Superintelligence cloud. We help them benchmark and optimize their throughput, and we ensure their synthetic data generation experience on our cloud is second to none. Our expertise will culminate in a set of tried-and-true best practices that will help our customers go from 0 to 1 in synthetic generation.

The age of large-scale synthetic data is here. The question is no longer whether models will depend on it, but who builds the infrastructure to generate it.

To learn more, explore the project page, code, and visualizations.

## AUTHORED BY

 Amir Zadeh

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
