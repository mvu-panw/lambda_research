# From structures to dynamics: scaling AI for molecular dynamics in drug discovery

Source: https://lambda.ai/blog/eginterpolator-molecular-dynamics-drug-discovery

Skip to main content

# From structures to dynamics: scaling AI for molecular dynamics in drug discovery

 September 21, 2026

 • 4 min read

## Why molecular dynamics matters for drug discovery

Molecular dynamics (MD) is an important tool in modern drug discovery. While structure prediction and molecular docking can show how a potential drug might fit into a protein, they provide only a snapshot. Molecules are constantly moving. MD simulations allow researchers to see how a drug and its target behave over time: whether the interaction remains stable, how the protein changes shape, and how the molecular system evolves.

The challenge is speed.

MD simulations calculate how atoms interact and move step by step, often over millions of simulation steps. Running these simulations at the scale needed for drug discovery can require substantial computing resources and time, limiting how many drug candidates researchers can study in depth.

## AI for molecular dynamics: an opportunity with a data bottleneck

This has created growing interest in using AI to accelerate molecular dynamics. Instead of calculating every step entirely through traditional simulation, AI models can learn patterns of molecular behavior and help generate or predict how molecular systems evolve.

But this introduces another problem: AI needs training data.

To train an AI model to understand molecular dynamics, researchers typically need large collections of MD trajectories. Yet these trajectories are exactly what is expensive to generate in the first place. Compared with the enormous amount of available static molecular structure data, high-quality molecular dynamics data remain relatively scarce.

This creates a fundamental bottleneck. We want AI to reduce the cost of MD, but training AI for MD can itself depend on large amounts of expensive MD data.

In collaboration with Stanford University, our work, EGInterpolator, explores a way around this bottleneck and introduces a framework for training AI models for molecular dynamics at scale.

The idea is simple. Before teaching AI how molecules move, first teach it what realistic molecules look like. This work was accepted as a main conference paper at ICLR 2026.

## The solution: learn structure first, then dynamics

Large molecular conformer datasets provide abundant examples of three-dimensional molecular structures. From these data, AI models can learn the fundamental geometry of molecules, such as bond lengths, bond angles, molecular conformations, and other structural patterns.

Molecular dynamics adds a more difficult dimension: time. Instead of generating a single realistic structure, a model must learn how that structure evolves over time. Each individual frame must be physically plausible, while the full sequence must also represent realistic molecular motion.

Training directly on MD trajectories therefore asks a model to learn two difficult problems at once:

- 

What does a realistic molecule look like?

- 

How does it move over time?

The challenge is that these two data types are not equally available. Static molecular structures are abundant, while high-quality MD trajectories are much more expensive to generate and therefore relatively scarce. This leads to a key insight: much of the knowledge needed to model molecular dynamics, particularly molecular geometry, can be learned before the model ever sees an MD trajectory.

Our model EGInterpolator builds on this idea: learn molecular structures first, then learn how those structures evolve. It consists of two stages:

- Structure pretraining: We first pretrain a diffusion-based generative model on large-scale molecular conformer data. This stage teaches the model the distribution of realistic three-dimensional molecular geometries, providing a strong structural prior.

- Dynamic fine-tuning: We then train a trajectory interpolator on MD data to learn how molecular structures connect over time. Because the model already understands molecular geometry, the scarce and expensive MD data can focus on what they uniquely provide: dynamics.

Conceptually, that two-stage process maps like this:

Structure pretraining → Dynamic fine-tuning → Molecular trajectory generation

Rather than learning molecular dynamics entirely from expensive trajectory data, this approach transfers knowledge from abundant static structures to molecular motion, providing a more data-efficient and scalable path toward AI-driven molecular dynamics.

## The results

EGInterpolator can generate molecular trajectories that more closely resemble reference molecular dynamics simulations.

On the DRUGS forward-simulation benchmark, EGInterpolator outperformed GeoTDM, a previous generative molecular dynamics method, across multiple measures of molecular geometry and motion. The difference from reference MD simulations decreased from 0.640 to 0.173 for bond angles, 0.643 to 0.142 for bond lengths, and 0.498 to 0.377 for torsional motion in terms of mean Jensen–Shannon Divergence (JSD): approximately 73%, 78%, and 24% lower, respectively.

Importantly, our ablation experiments show that structure pretraining itself plays a major role. On the DRUGS benchmark, removing structure pretraining increased the difference from reference MD distributions from 0.173 to 0.332 for bond angles, from 0.142 to 0.386 for bond lengths, and from 0.377 to 0.455 for torsional motion, measured by mean JSD. This provides direct evidence for our central idea: learning realistic molecular structures first helps AI learn how drug-like molecules move.

Beyond small molecules, we further extended the approach to more complex molecular systems, including tetrapeptides and protein monomers.

The takeaway is simple: by first learning from abundant molecular structure data, AI can learn molecular dynamics more effectively while reducing its dependence on scarce and expensive MD trajectory data. For drug discovery, this points toward more scalable AI tools for studying how potential drug molecules behave over time.

## Where Lambda fits

Molecular dynamics has traditionally been a compute-intensive scientific simulation workload. As AI learns molecular structures, energies, forces, and even trajectories, more of molecular simulation is becoming a GPU-native AI workload.

This research exemplifies that shift. Instead of relying only on traditional simulation to generate every molecular trajectory, we train generative AI models to learn from existing molecular structures and MD data and generate realistic molecular motion. Training and evaluating these models requires the same capabilities that power modern AI: high-performance GPUs, scalable training infrastructure, and fast experimentation.

We trained and evaluated the models in this work on Lambda GPU infrastructure, using NVIDIA GPUs across multi-GPU experiments. Lambda provided the compute environment needed to develop, train, and test the models across molecules, drug-like compounds, peptides, and proteins.

For drug discovery teams, the opportunity goes beyond a single model. A modern computational pipeline can involve protein structure prediction, molecular generation, virtual screening, docking, and molecular dynamics, all increasingly accelerated by GPUs and AI.

Lambda provides the GPU infrastructure to support these compute-intensive workloads, enabling researchers to run AI workflows spanning target understanding, molecular modeling, and candidate evaluation on a common computing platform.

Paper: arxiv.org/abs/2604.03911v1
Credits: Stanford University, Lambda.
Authors: Aniketh Iyengar, Jiaqi Han, Pengwei Sun, Mingjian Jiang, Jianwen Xie, Stefano Ermon. ICLR 2026.

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
