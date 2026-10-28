# Closing the loop: agentic evaluation for image editing foundation models

Source: https://lambda.ai/blog/edival-agent-agentic-evaluation-image-editing

Skip to main content

# Closing the loop: agentic evaluation for image editing foundation models

 September 17, 2026

 • 5 min read

## Why evaluating image editing models is both critical and challenging

Instruction-based image editing is becoming a core capability of multimodal foundation models. Users can increasingly edit images simply by describing what they want: “remove the person in the background,” “make the car red,” or “move the chair next to the table.”

For teams building these models, however, generating better images is only half the challenge. They also need to know whether the model is actually getting better.

Foundation-model development is an iterative process:

Train → Evaluate → Identify failures → Improve → Train again

Evaluation closes this loop. Researchers need it to compare checkpoints, validate new training strategies, detect regressions, and decide what to improve next.

For image editing, evaluation is particularly challenging. A successful edit must make exactly the requested change, preserve everything that should remain unchanged, and maintain high visual quality. In multi-turn editing, the model must also preserve previous changes as new instructions arrive.

Human evaluators can identify these failures, but manually inspecting thousands of outputs across models, checkpoints, images, and editing turns is slow and expensive. Existing automated metrics also struggle to capture all these requirements with a single score.

This raises a natural question:

Can we use AI agents to automate the evaluation of image editing foundation models?

## EdiVal-Agent: automating evaluation with agentic AI

In collaboration with The University of Texas at Austin, UCLA, and Microsoft, Lambda researchers developed EdiVal-Agent, a framework that turns image-editing foundation model evaluation into an agentic AI workflow. This work has been accepted as a conference paper at ICLR 2026.

Rather than asking a single model to judge an entire edited image, EdiVal-Agent decomposes evaluation into smaller, verifiable tasks. It first identifies semantically meaningful objects in the image and interprets the editing instruction at the object level, determining what should change and what should remain unchanged. Across multiple editing turns, it maintains an evolving object pool that tracks these changes over time.

The framework then coordinates specialized AI models and visual tools to verify different aspects of the edit. For example, given the instruction “change the blue car to red,” EdiVal-Agent can determine whether the correct car is still present, verify that its color changed as requested, check that unrelated objects and the background were preserved, and assess whether the final image remains visually convincing.

This evaluation is organized around three complementary dimensions:

- Instruction Following (EdiVal-IF): Did the model perform the requested edit? EdiVal-Agent combines vision-language reasoning, open-vocabulary object detection, and verification rules to inspect specific objects, attributes, and changes.

- Content Consistency (EdiVal-CC): Did content that should remain unchanged stay consistent? Using its evolving object pool, the framework tracks objects across editing turns and compares semantic features to detect unintended changes.

- Visual Quality (EdiVal-VQ): Does the edited image remain visually convincing? Human-preference models assess perceptual quality and visual artifacts independently of whether the requested edit was completed.

Together, these components form an agentic evaluation pipeline:

Understand the instruction → Decompose into object-level requirements → Track state across turns → Apply specialized tools → Verify each requirement → Aggregate the evaluation

This is what distinguishes EdiVal-Agent from a single AI judge or a collection of image metrics. It decomposes the problem, maintains state across interactions, coordinates specialized AI tools, and integrates their outputs to provide a fine-grained assessment of how an image editing foundation model succeeds—or fails.

## Results

The key question is whether agentic evaluation actually reflects human judgment.

For the most agentic component of the framework, EdiVal-IF, we evaluate whether its judgments align with human assessment. EdiVal-IF achieved 81.3% agreement with human judgments, outperforming a VLM-only evaluator at 75.2% and a thresholded CLIP-based metric at 68.9%.

This improvement demonstrates the value of combining AI reasoning with specialized visual tools. A vision-language model can understand the semantic intent of an instruction, while object detectors and other visual models can more precisely verify whether specific editing requirements were satisfied.

We then use EdiVal-Agent to benchmark leading image editing foundation models across different editing tasks and multi-turn interactions.

The evaluation reveals an important challenge: strong single-turn performance does not necessarily translate into strong multi-turn performance. As editing instructions accumulate, models need to follow each new request while preserving previous edits and unrelated content. Errors can therefore compound over time.

For developers, this fine-grained evaluation provides more than a leaderboard. It helps reveal whether improvements or regressions come from instruction following, content preservation, or visual quality.

## Closing the foundation-model development loop

EdiVal-Agent can therefore serve as more than a benchmark. Agentic evaluation can become part of the image-editing foundation model development process itself. When a new checkpoint is produced, the model can automatically generate edits across an evaluation set. EdiVal-Agent can inspect those outputs, measure different dimensions of performance, and identify specific failure modes. 

Those results can then inform the next training iteration. For example, a new checkpoint might improve its ability to follow editing instructions while becoming worse at preserving unrelated objects. Another might perform well on individual edits but degrade rapidly across longer editing sequences.

Automated, fine-grained evaluation makes these tradeoffs easier to identify and can shorten the feedback loop between building a new model and understanding how it behaves.

## Where Lambda fits

EdiVal-Agent is part of Lambda's broader work in Agentic AI — developing AI systems that can reason about complex tasks, coordinate specialized models and tools, and execute multi-step workflows.

Most discussions of agentic AI focus on agents performing tasks for users. EdiVal-Agent explores another important direction: Using AI agents to evaluate other AI models.

Foundation-model evaluation is naturally suited to an agentic approach. A capable evaluator needs to understand the task, decompose it into requirements, maintain state across multiple interactions, select appropriate tools, inspect the results, and produce actionable feedback.

EdiVal-Agent therefore extends Lambda's Agentic AI work into the foundation-model development loop. Agents are not only an application built on top of foundation models; they can also become part of the infrastructure used to benchmark, validate, and improve those models.

This direction becomes increasingly important as foundation models become more multimodal, interactive, and capable of long-horizon behavior. Their outputs become harder to evaluate with a single metric, or even a single AI judge. Evaluation itself increasingly requires reasoning, memory, decomposition, and tool use.

Combined with Lambda's GPU infrastructure, agentic evaluation can also be scaled across models, checkpoints, images, editing turns, and evaluators, making continuous evaluation practical during model development.

EdiVal-Agent points toward a broader direction for Lambda's Agentic AI research: AI agents that not only perform complex tasks, but also help developers understand, evaluate, and improve other AI systems.

As foundation models become more capable, the systems used to evaluate them will need to become more capable as well. Agentic AI provides a path to close the loop between training, evaluation, and improvement, helping developers understand not only whether a new model is better, but where it improved and why.

Paper: arxiv.org/pdf/2509.13399
Credits: The University of Texas at Austin, UCLA, Microsoft, and Lambda.
Authors: Tianyu Chen, Yasi Zhang, Zhi Zhang, Peiyu Yu, Shu Wang, Zhendong Wang, Kevin Lin, Xiaofei Wang, Zhengyuan Yang, Linjie Li, Chung-Ching Lin, Jianwen Xie, Oscar Leong, Lijuan Wang, Ying Nian Wu, Mingyuan Zhou. ICLR 2026.

## AUTHORED BY

 Jianwen Xie

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
