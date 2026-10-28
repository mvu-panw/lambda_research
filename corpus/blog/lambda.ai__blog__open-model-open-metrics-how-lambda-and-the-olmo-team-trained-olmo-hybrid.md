# Open model, open metrics: How Lambda and the Olmo team trained Olmo Hybrid

Source: https://lambda.ai/blog/open-model-open-metrics-how-lambda-and-the-olmo-team-trained-olmo-hybrid

Skip to main content

# Open model, open metrics: How Lambda and the Olmo team trained Olmo Hybrid

 March 5, 2026

 (Updated on March 14, 2026)

 • 14 min read

Open-source models are now one of the main engines of progress in AI. When strong models like Nemotron, Llama 3.1, and Qwen3-Next are released openly, the community can reproduce results, improve training recipes, and build new products on top of them faster than any single lab could alone.

However, building next-generation models isn’t just about designing new model architectures or datasets; it’s also an infrastructure engineering challenge. Lambda makes that kind of progress practical by providing the compute and infrastructure that lets teams train, fine-tune, and serve models reliably at scale.

The Olmo Hybrid training effort is one example demonstrating Lambda’s reliable support for long-running, large-scale model training. We present concrete evidence: a training run spanning pre- and mid-training, documented failures with demonstrated recovery behavior, and a fully open-sourced language model. 

You can replicate the training process we used using this training stack and see for yourself how reliable Lambda’s Superintelligence Cloud can be for your own training tasks.

Here’s how the model and the training system behind it were built.

## Open-source model training on Lambda

AI teams training large foundation models on hundreds of NVIDIA GPUs know that success lives in the details—the right architecture, the right data mix, and an infrastructure solid enough to see it through. Months of preparation go into every run: curating data, designing model architecture, and stress-testing the stack before a single token is processed. The teams that get it right understand that at this scale, infrastructure isn't a backdrop; it's part of the research.

Lambda and the Allen Institute for Artificial Intelligence (Ai2) tackled both sides of that challenge head-on, training Olmo Hybrid 7B on 512 NVIDIA Blackwell GPUs across 3 trillion tokens, and publishing the full results openly: the code, the training logs, and the model weights.

Compared to its predecessor, Olmo 3 7B, Olmo Hybrid delivers consistent benchmark gains across domains, a result that came from both an architectural change and a deliberate infrastructure decision. The Olmo team migrated their training workload from its internal environment with NVIDIA HGX H100 systems to 64 NVIDIA HGX B200 systems hosted on Lambda infrastructure. They finished training the model on 3 trillion tokens using a fully open stack and their data in 7 days.

The results:

- Medical Question Answering multiple choice (MedQA MC) (+7.1) (Olmo Hybrid: 48.7% vs Olmo 3: 41.6%). The +7.1 gain indicates significantly stronger domain reasoning and improved ability to handle specialized STEM content.

- MBPP (+6.7) (Olmo Hybrid: 50.3% vs Olmo 3: 43.6%) Mostly Basic Python Programming. The +6.7 improvement reflects stronger algorithmic reasoning, structured problem solving, and executable code synthesis.

- MMLU STEM (+4.5) (Olmo Hybrid: 70.8% vs Olmo 3: 66.3%) Massive Multitask Language Understanding—STEM subset. Covers subjects such as mathematics, physics, computer science, and engineering. The +4.5 gain shows improved structured reasoning and technical subject mastery across diverse scientific domains.

- MMLU Humanities (+4.7) (Olmo Hybrid: 73.9% vs Olmo 3: 69.2%) MMLU—Humanities subset.

- Evaluates knowledge and reasoning in areas like history, philosophy, and law. The +4.7 increase demonstrates broader reasoning improvements beyond purely technical domains.

Lambda’s NVIDIA HGX B200 cluster, combined with Olmos’ training stack, demonstrated strong reliability shown through transparent, real-world metrics. Specifically, we achieved:

- Active training time of 97%, excluding development work during the troubleshooting phase, 99% active training time.

- Median recovery time under 4 minutes.

- Improved model performance over Olmo 3 7B.

We’re honored to partner with the Olmo Team for this phase of Olmo Hybrid’s development, and excited to dive into what this collaboration means for teams training large models at scale.

## Model and training configuration on Lambda

Olmo Hybrid overview from the report:

### Architecture 

Olmo Hybrid is a hybrid linear RNN–transformer model built on the Olmo 3 7B architecture. While transformers are powerful, they’ve been shown to be theoretically limited at certain sequential capabilities like state tracking, which RNNs can better express. In contrast, RNNs are limited at recall tasks relative to transformers. Thus, combining both scalable primitives within a hybrid architecture is a simple way to produce a fundamentally more expressive but similarly scalable language model.

To achieve this goal, Olmo Hybrid follows the standard transformer layout, but replaces 75% of attention layers with gated DeltaNet heads, alternating three DeltaNet layers for every one full multi-head attention layer. Each DeltaNet head uses standard queries, keys, and values, with an additional learned gate, and maintains a linear recurrent state. A Gated DeltaNet head fits seamlessly into the overall transformer architecture from Olmo 3. This hybrid design allows the model to retain full attention where needed while gaining the efficiency and expressivity of linear recurrence. Hybrid models with attention and Gated DeltaNet layers can express more than either type of model could on its own.

### Training strategy

Training uses Hybrid Sharded Data Parallelism (HSDP) to scale efficiently across large NVIDIA GPU clusters. Unlike fully sharded approaches, HSDP limits cross-node communication by sharding parameters only within nodes and replicating them across nodes, so communication overhead stays roughly constant as more nodes are added, rather than growing with cluster size. Parameters are sharded at the block level, stored in bfloat16, and reduced in FP32 for stability. The setup supports a ~4M token global batch size at 8k sequence length.

The training stack includes FlashAttention v2 for full-attention layers, cosine learning rate scheduling with warmup, and asynchronous checkpointing. Jobs are launched via SLURM using a clean, reproducible entrypoint.

### Fully open and reproducible

Most importantly, this entire training stack is fully open. The model architecture, training configuration, and launch scripts are all available on GitHub, along with the data mix definitions used for training. If you want to inspect the code, reproduce the run, or adapt it for your own cluster and hardware, you can! This transparency allows anyone to see exactly how a large-scale, long-running pretraining job is configured and executed on Lambda.

## Results

### Downstream results 

These are the downstream uplifts between Olmo 3 7B and the new Olmo Hybrid:

 | 

Aggregate benchmark

 | 

Olmo Hybrid

 | 

Olmo 3 7B 

 | 

Δ (Hybrid − Olmo 3 7B )

 | 

OlmoBaseEval Math

 | 

55.1

 | 

54.6

 | 

+0.5

 | 

OlmoBaseEval Code

 | 

32.4

 | 

30.9

 | 

+1.5

 | 

OlmoBaseEval MC STEM

 | 

70.0

 | 

66.2

 | 

+3.8

 | 

OlmoBaseEval MC Non-STEM

 | 

80.4

 | 

78.2

 | 

+2.2

 | 

OlmoBaseEval GenQA

 | 

72.9

 | 

72.5

 | 

+0.4

Aggregate downstream evaluation comparing Olmo Hybrid to Olmo 3 7B Dense. The Hybrid model improves across all benchmark categories, with the largest gains in MC STEM and Code.

 | 

Category

 | 

Benchmark

 | 

Olmo Hybrid

 | 

Olmo 3 7B 

 | 

Δ(Hybrid − Olmo 3 7B )

 | 

MC STEM

 | 

MedQA MC

 | 

48.7

 | 

41.6

 | 

+7.1

 | 

Code

 | 

MBPP

 | 

50.3

 | 

43.6

 | 

+6.7

 | 

MC STEM

 | 

MMLU STEM

 | 

70.8

 | 

66.3

 | 

+4.5

 | 

MC Non-STEM

 | 

MMLU Humanities

 | 

73.9

 | 

69.2

 | 

+4.7

 | 

MC Non-STEM

 | 

MMLU Other

 | 

71.5

 | 

66.8

 | 

+4.7

The Hybrid model delivers the largest improvements on STEM multiple-choice and code benchmarks (e.g., MedQA MC, MBPP, MMLU STEM), with consistent gains across humanities and other non-STEM categories, indicating stronger structured reasoning and algorithmic performance.

### Why does Olmo Hybrid outperform its predecessor, Olmo 3 7B, on evaluation?

This improvement aligns closely with the greater expressive power of hybrid models relative to transformers. The hybrid architecture pushes the expressivity–parallelism frontier by expanding expressivity through the combination of attention and recurrence, two architectural primitives with complementary strengths, thereby increasing the set of naturalistic subtasks the model can represent. Through empirical scaling studies and theoretical analysis, the Olmo Hybrid report argues that this expressive power translates to better pretraining scaling. Relatedly, Olmo Hybrid shows consistent gains on standard benchmarks, long-context extrapolation, and inference efficiency, suggesting hybrid models outperform pure transformers both in theory and in practice.

### Reliability breakdown

Another focus for this effort was to measure and demonstrate infrastructure reliability during a reasonably long-running model pretraining run. Unlike stress tests or short benchmarks, this job represents a realistic workload: sustained utilization of 64 NVIDIA HGX B200 systems (512 NVIDIA Blackwell GPUs total) over a pretraining run within a short fixed time budget, a little over a week total time on the cluster.

Reliability summary:

- 

Total elapsed time pretraining: 6.19 days (Dec 25 - Dec 31)

- 

Mid-training + Long Context dev and running (Jan 1 - 5)

- 

Median recovery time: 3 minutes 42 seconds

- 

Mean recovery time: 38 minutes 54 seconds (skewed by one long outage)

- 

Ratio of train time: 97%, or 99% excluding dev work during the first failure 

## How we achieved this level of reliability

Reliability was built into the training workflow. On start and restart, the system relied on automated NVIDIA GPU health checks that evaluated indicators such as temperature and idle state, allowing the job to fail fast when unsafe conditions occurred, rather than hanging or corrupting training. When an NVIDIA GPU or node failed these checks, it was automatically quarantined and added to a persistent exclusion list until maintenance was completed, so it wouldn’t be reused on restart. The job didn’t continue with fewer GPUs; instead, it was terminated and restarted on a new allocation that excluded the failed hardware.

Spare NVIDIA GPUs ensured sufficient capacity to restart without reducing job scale. Robust checkpointing and restart logic ensured that training could resume cleanly from the most recent checkpoint with minimal lost work. All of this logic lives directly in the training repository, making the approach transparent, reproducible, and easy for others to adopt.

### Health script explanation 

This script is a pre-flight health check that runs on every node before training starts in a Lambda/SLURM environment. Its entire purpose is to catch bad hardware states early and fail fast.

First, it checks NVIDIA GPU temperatures using nvidia-smi. Idle GPUs should typically be cooler, so unusually high starting temperatures can indicate throttling, stuck workloads, or cooling issues. The script enforces conservative warn and fail thresholds (configurable via environment variables) and immediately aborts the job if any GPUs are already too hot.

Second, it verifies that the GPUs are truly idle. It checks both memory usage and running compute processes, ensuring no leftover jobs or zombie processes are occupying the GPU memory.

These health-check scripts are fully public and available in the training repository, so you can use, adapt, or extend them for your own large-scale training jobs. You don’t need special Lambda-internal tooling to benefit from this approach, as the same checks can be dropped into other SLURM-based workflows to dramatically improve reliability and debugging capabilities.

### Why these metrics matter

The strongest evidence of reliability is the outcome itself: within a one-week time window, we completed the pretraining run of the Olmo Hybrid model. This outcome reflects the combined effect of expert engineering, automated recovery, and Lambda’s infrastructure operating as intended under real production conditions.

For AI teams, the takeaway is not that failures never occur, but that they’re observable, manageable, and recoverable. That operational reality is what enables teams to run large, long-duration training jobs with confidence on Lambda.

## Conclusion

This project highlights why AI teams choose Lambda to support large-scale, long-duration foundation model training with measurable reliability.

The Olmo Team successfully pretrained a 7B-parameter model on 64 NVIDIA HGX B200 systems using a fully open stack, while Lambda continuously collected real-world reliability and recovery metrics throughout the run. The resulting model delivers consistent improvements over Olmo 3 7B, reflecting both a sound architectural direction and a stable, well-operated training environment.

More importantly for AI teams, this collaboration demonstrates what it’s like to train large models on Lambda in practice:

- Failures are detected, handled, and recovered quickly and automatically.

- Open-source and research-driven teams can train at scale on a fully open stack.

- Multi-trillion-token training jobs can run with confidence on production infrastructure.

Instead of simply stating that these workloads are possible, Lambda can now point to a model that was trained, released, and validated in the open. For teams building modern foundation models, this is the kind of real-world experience that makes Lambda a trusted production platform.

## Timeline

The model required additional post-training and was subject to availability constraints. It was released on March 5th.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
