# Thomson Reuters

Source: https://lambda.com/customer-stories/thomson-reuters

Skip to main content

# How Thomson Reuters made sovereign AI achievable with Lambda

Contact Sales

TRAINING
4x
faster

EVALUATION ITERATIONS
10x
faster

TRAINING COSTS
$40M
total

## Thomson Reuters and Lambda

## Executive Summary

Thomson Reuters, in partnership with Imperial College London, post-trained an open model on its own data and got most of the benefits of pre-training from scratch, with Lambda as its compute and engineering partner.

Thomson Reuters does high-stakes professional work across legal, tax, and news. Its research team recently released Thomson-1.0, its own foundation model, and Lambda provided the compute behind it. The team's thesis: frontier model development isn't limited to heavily funded labs. Mid-size institutions can do it too.

For most institutions, sovereign AI has looked like a choice between two extremes. Pre-train a model from scratch, a billion-dollar effort, or settle for narrow fine-tuning on a model someone else controls.

Thomson Reuters set out to find the middle ground, where they could get a high-performance model at reasonable cost. Working with researchers at Imperial College London, the team took an open-source model that was already pre-trained and post-trained it further on their own data.

Customer
 
Thomson Reuters

Website

 thomsonreuters.com

Vertical
 
Professional Services

Products
 
1-Click Cluster

 “What we've tried to do is get you 90% of the way to the benefits of pre-training from scratch.”

 Jonathan Richard Schwarz, Head of AI Research @ Thomson Reuters

## Owning what “good” looks like

For the team, sovereignty means control over the data, the model, the infrastructure, and the standard the model gets measured against.

That put evaluation at the center of the project. It also made compute efficiency a hard requirement, because finding the right recipe meant running many experiments, and every one of them had to fit the budget. Post-training on domain data can erase a model's general capabilities, so the team had to balance domain adaptation against forgetting, using model merging, replay data, and a carefully tuned data mixture. That meant running experiments at scale, and fast.

“Even though you might own the data, the model, and the infrastructure, if you outsource defining what good looks like to somebody else, you've then outsourced your AI strategy.”Nabeel Seedat, Lead Research Scientist & Research Lead LLM Post-Training Evals @ Thomson Reuters

## Lambda as a compute and engineering partner

Lambda engineers worked directly with the Thomson Reuters team from the start of the engagement, including moving the project's compute to Lambda partway through. For the researchers running experiments, the move happened under the hood.

“The Lambda team felt effectively like a sort of extension of our engineering team.”Jonathan Richard Schwarz, Head of AI Research @ Thomson Reuters

“There was a lot of certainty about availability and pricing, which is not something that we had really seen with other providers.”Jonathan Richard Schwarz, Head of AI Research @ Thomson Reuters

## Per-Category score improvements of Thomson-1.0-Small

View data table
Per-Category score improvements of Thomson-1.0-Small
 | Benchmark | Thomson-1.0-Small | Qwen3.6-35B | Snowdon-1.1-Small
 | Math | 0.869 | 0.881 | 0.875
 | Instruction following | 0.863 | 0.851 | 0.855
 | General agentic | 0.862 | 0.808 | 0.817
 | Writing | 0.813 | 0.799 | 0.797
 | Tax | 0.829 | 0.775 | 0.767
 | Safety / values | 0.782 | 0.724 | 0.758
 | Long context | 0.746 | 0.745 | 0.745
 | Legal | 0.755 | 0.729 | 0.727
 | Multilingualism | 0.724 | 0.737 | 0.715
 | Journalism | 0.743 | 0.723 | 0.678
 | Reasoning | 0.616 | 0.615 | 0.615
 | Factuality | 0.612 | 0.595 | 0.590
 | Coding | 0.372 | 0.397 | 0.358
Source: Thomson-1.0 Technical Report

## Nearly 10x faster evaluation iterations

Running evaluations on Lambda, the team iterated nearly 10x faster than before. Insights from each round of evaluation made it into the next version of the model much sooner.

The final training run cost $150,000. The full effort, including all post-training work, came to about $40 million, a fraction of what pre-training from scratch costs.

“We were almost sort of shocked by our own kind of efficiency.”Jonathan Richard Schwarz, Head of AI Research @ Thomson Reuters

## Expert human preferences: Thomson-1.0-Large vs. external models

Share of comparisons (%)

View data table
Expert human preferences: Thomson-1.0-Large vs. external models
 | Evaluation set | Compared with | Thomson-1.0-Large wins | Tie | Opponent wins
 | Combined | vs GPT 5.5 | 62% | 9% | 29%
 | Combined | vs Opus 4.8 | 58% | 12% | 30%
 | Combined | vs GPT 5.6 Terra | 57% | 11% | 32%
 | Combined | vs Sonnet 5 | 53% | 17% | 30%
 | Combined | vs GPT 5.6 Sol | 54% | 13% | 33%
 | Legal | vs GPT 5.5 | 63% | 8% | 29%
 | Legal | vs Opus 4.8 | 63% | 11% | 26%
 | Legal | vs GPT 5.6 Terra | 64% | 8% | 28%
 | Legal | vs Sonnet 5 | 54% | 16% | 30%
 | Legal | vs GPT 5.6 Sol | 57% | 10% | 33%
 | General | vs GPT 5.5 | 59% | 14% | 27%
 | General | vs Opus 4.8 | 46% | 17% | 37%
 | General | vs GPT 5.6 Terra | 43% | 17% | 40%
 | General | vs Sonnet 5 | 50% | 19% | 31%
 | General | vs GPT 5.6 Sol | 47% | 19% | 34%
Source: Thomson-1.0 Technical Report

## Compute for the next generation of researchers

Lambda was founded by machine learning engineers, and supporting research has been part of the company from the start. As part of this project, Lambda donated $300,000 in compute to Imperial College London, so students and academics could work on large models that are usually out of reach in academia.

## What comes next

The team has published its blueprint in the technical report. That opens the door for other institutions to experiment with open models, try the recipe on their own use cases, and improve on it, building an ecosystem together instead of waiting on a few big labs.

Read the technical report: Thomson-1.0 Technical Report

Read more about Lambda’s GPU clusters for your workloads.

“People used to think that you were either a big lab or you were a customer of a big lab, and not many institutions could achieve sovereignty. I think we've proved them wrong.”Jonathan Richard Schwarz, Head of AI Research @ Thomson Reuters
