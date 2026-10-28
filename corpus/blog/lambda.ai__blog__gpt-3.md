# GPT-3 A Hitchhiker's Guide

Source: https://lambda.ai/blog/gpt-3

Skip to main content

# GPT-3 A Hitchhiker's Guide

 July 20, 2020

 (Updated on April 4, 2023)

 • 10 min read

The goal of this post is to guide your thinking on GPT-3. This post will:

- Give you a glance into how the A.I. research community is thinking about GPT-3.

- Provide short summaries of the best technical write-ups on GPT-3.

- Provide a list of the best video explanations of GPT-3.

- Show some cool demos by people with early beta access to the GPT-3 API.

If you think something should be added, email m@lambdalabs.com.

## What researchers are saying about GPT-3

"For me, the big story about #gpt3 is not that it is smart - it is dumb as a pile of rocks - but that piles of rocks can do many things we thought you needed to be smart for. Fake intelligence may be dominant over real intelligence in many domains."
– Anders Sandberg, Senior Research Fellow at Oxford University, read tweet

"The GPT-3 hype is way too much. It’s impressive (thanks for the nice compliments!) but it still has serious weaknesses and sometimes makes very silly mistakes. AI is going to change the world, but GPT-3 is just a very early glimpse. We have a lot still to figure out. "
– Sam Altman, CEO of OpenAI, read tweet

"I've stayed away from Twitter waiting for the GPT-3 mist to fade.
Good news: More and more people are excited than ever about the possibilities of language modeling Love letter
Bad news: There's a rush of hot takes that forget the progression of the field and make tea leaves of science."
– Stephen Merity, Former Senior Researcher at SalesForce, read tweet

"The transformer architecture of GPT upper bounds its ability at memorization. It cannot learn many algorithms due to the functional form of its forward pass, and spends a fixed compute per token - i.e. it can't "think for a while". Progress here critical, likely but non-trivial."
– Andrej Karpathy, Senior Director of A.I. at Tesla, read tweet

"I used to say that AI research seemed to have an odd blind spot towards automation of programming work, and I suspected a subconscious self-preservation bias. The recent, almost accidental, discovery that GPT-3 can sort of write code does generate a slight shiver."
– John Carmack, Consulting CTO of Oculus VR, read tweet

"GPT-3 often performs like a clever student who hasn't done their reading trying to bullshit their way through an exam. Some well-known facts, some half-truths, and some straight lies, strung together in what first looks like a smooth narrative."
– Julian Togelius, Associate Professor researching A.I. at NYU, read tweet

"Hackers are fascinated by GPT-3. To everyone else it seems a toy. Pattern seem familiar to anyone?"
– Paul Graham, Founder of YCombinator, read tweet

"Our exciting future of security vulnerabilities involving GPT-3 like models in web apps..."
– Chris Olah, Member of Technical Staff at OpenAI, read full tweet

"Got my invite to the @OpenAI GPT-3 API from @gdb. I actually think it deserves more hype than it’s getting, but not necessarily for the magical reasons Twitter touts. Why? My quick thoughts and impressions: (1/11)"
– Shreya Shankar, ML researcher at Viaduct AI, read full tweet.

## The best GPT-3 technical write-ups

OpenAI's GPT-3 Language Model: A Technical Overview
June 3, 2020 by Chuan Li - Chief Science Officer at Lambda
Link | Reddit (408 points, 207 comments)

An overview of the original paper covering its training cost and research implications.

- GPT-3 shows that language model performance scales as a power-law of model size, dataset size, and the amount of computation.

- GPT-3 demonstrates that a language model trained on enough data can solve NLP tasks that it has never encountered. That is, GPT-3 studies the model as a general solution for many downstream jobs without fine-tuning.

- The cost of AI is increasing exponentially. Training GPT-3 would cost over $4.6M using a Tesla V100 cloud instance.

- The size of state-of-the-art (SOTA) language models is growing by at least a factor of 10 every year. This outpaces the growth of GPU memory. For NLP, the days of "embarrassingly parallel" are coming to the end; model parallelization will become indispensable.

- Although there is a clear performance gain from increasing the model capacity, it is not clear what is really going on under the hood. Especially, it remains a question of whether the model has learned to do reasoning, or simply memorizes training examples in a more intelligent way.

GPT-3
July 18, 2020, by Gwern Branwen
Link | Hacker News (291 points, 200 comments)

A well-cited overview of the original GPT-3 paper with a punchline on what it tells us about the scaling hypothesis:

- GPT-3 is interesting because:

- It exhibits meta-learning.

- Its performance continues to scale with the # of parameters (with no end in sight).

- It has these two amazing properties, despite:

- Using an obsolete (2018) small, shallow, uniform architecture.

- Being trained on low-quality internet data (e.g. code, HTML, movie scripts, tweets).

- Sampling data in a "dumb" way.

- Being trained on a data set small enough to fit on your MacBook Pro.

- Does GPT-3 beat SOTA on every task? No!

- GPT-3 was extremely expensive to train (~$5M). There is concern that scaling beyond GPT-3 (i.e. increasing # of parameters) will become increasingly economically infeasible.

- We can expect better performance in the future from models that simply have more parameters.

- Evidence is mounting for the scaling hypothesis: once we find a scalable architecture, "which like the brain can be applied fairly uniformly," we can train "ever larger NNs and ever more sophisticated behavior will emerge as the easiest way to optimize for all the tasks & data."

- “Give it the compute, give it the data, and it will do amazing things. This stuff is like—it’s like alchemy!” - Ilya Sutskever

- He references the oft-cited essay, The Bitter Lesson

Tempering Expectations for GPT-3 and OpenAI’s API
July 18, 2020, by Max Woolf - Data Scientist at BuzzFeed, Ex- Apple
Link | Hacker News (256 points, 181 comments) | Reddit (31 comments, 23 points)

A hacker's introduction to GPT-3 with a curl-based examples of OpenAI's invite-only beta API:

- GPT-3, like other text-generating model, works as follows: you give it a chunk of text and it predicts the next chunk of text. The model then uses its own output to extend the length of its prediction. This process continues until reaching a threshold length or a stop token.

- From an end-user perspective, GPT-3 improves upon GPT-2 in two major ways:

- It allows generation of text twice the length of GPT-2 (~10 average paragraphs of English text).

- It provides better predictions than GPT-2 due to few-shot learning and having more parameters.

- The public internet was GPT-3's training ground, though it still doesn't know about COVID-19! It's likely seen code, movie scripts, tweets, blog posts, and more.

- The API works as follows: you send it an HTTP request with a text prompt (string) and it responds with text generated by GPT-3. The author released a python wrapper around the API on GitHub.

- Caveats:

- The API is slow. This is expected: the model has 175 billion parameters; it's too big to fit on a GPU (the largest GPU in the world has 48 GB of VRAM). There is currently no information about the infrastructure running GPT-3.

- The demos you're seeing around the internet are highly biased. The vast majority of output is of significantly lower quality.

- The author trained GPT-3 on his tweets; he estimates that only 30-40% were usable. This implies a 60-70% failure rate.

- If it takes three tries to generate a usable React component, it's probably more practical to just write the code yourself.

- Everyone is using the same model, so there's no competitive advantage.

- With the wrong prompt, you might get racist or sexist output.

- There is still no information on API pricing/cost.

Why GPT-3 Matters
Link | Hacker News (198 points, 142 comments)

- GPT-3 is massive (175 billion parameters); it’s an order of magnitude larger than Microsoft’s already massive 17B parameter Turing-NLG.

- With FP16, simply loading GPT-3 would use 300 GB of VRAM.

- Even without tuning, GPT-3 is competitive with SOTA on many benchmarks.

- GPT-3's performance scales with the number of parameters; it gives no indication of plateauing. This implies larger models will perform even better.

- GPT-3 is essentially a massive version of GPT-2.

- About GPT-3's training data

- It is a weighted mix of Common Crawl, WebText2 (a larger version of the original), two book corpora, and English Wikipedia.

- Some components (e.g. Wikipedia), were completely sampled 3+ times during training, while others like the Common Crawl, weren't even completely sampled. The authors claim that this is to help raise the overall quality of the corpus by prioritizing known-good datasets.

- Altogether, the filtered/cleaned dataset is 500 billion tokens, or 700GB.

- Due to a bug, some data overlapped between the training and test sets. The paper analyzes of the impact of this leakage.

- GPT-3 performance benchmarks:

- GPT-3 was testing in zero-shot, one-shot, and few-shot settings.

- Unlike its predecessors, GPT-3 can infer a task from one or a few example: this is a massive step towards generalization.

- GPT-3 can be “tuned” by providing instructions in plain English, whereas its precessors require task-specific tuning.

- Increasing model size improves performance across almost all tasks; in contrast, fine-tuning limits performance gains to one task and risks catastrophic forgetting and overfitting.

- On most tasks, GPT-3 performances significantly worse than fine-tuned SOTA, but for some tasks (i.e PhysicalQA, LAMBADA, Penn Tree Bank) it performs better.

- Ethical concerns

- People can't distinguish GPT-3 generated news stories from real ones.

- The paper notes language models will eventually become advanced enough for large scale misinformation campaigns.

GPT-3: A Disappointing Paper?
Link | Hacker News (142 points, 80 comments)

- GPT-3 is just a bigger GPT-2. Its underlying architecture is very similar. It's a generalization of the “just make the transformers bigger” approach that has become popular since GPT-2.

- One perspective on the GPT-2 paper is “amazing things happen if you just make a transformer bigger.” GPT-3 makes the same point with bigger numbers.

- GPT-2 was (arguably) a fundamental advance because it revealed the power of huge transformers. GPT-3 adds no knowledge in this area; it is far from a fundamental advance.

How GPT-3 Works
July 27, 2020
Link | Hacker News (175 points, 58 comments)

A visual introduction to GPT-3.

GPT-3: Language Models are Few-Shot Learners 
May 29, 2020
Link | Hacker News (431 points, 291 comments) | Reddit (271 points, 113 comments)

The original GPT-3 paper from OpenAI.

## Other interesting reads

- GPT-3 and Scaling Trends | Link | Hacker News (62 points, 18 comments)

- GPT-3 Creative Fiction | Link | Hacker News (234 points, 97 comments)

## The best videos on GPT-3

* GPT-3: Language Models are Few-Shot Learners (Paper Explained)
Watch video

OpenAI GPT-3: Language Models are Few-Shot Learners
Watch video | Reddit (40 points, 7 comments)
Machine Learning Street Talk

GPT 3 Demo and Explanation - An AI revolution from OpenAI
Watch video

GPT3: An Even Bigger Language Model
Watch video

## Cool GPT-3 demos

- Search engine: learn more

- The biggest thing since Bitcoin: learn more

- Building websites from English descriptions: learn more

- A natural language commandline shell: learn more

- Taking a Turing Test: learn more

- Medical diagnosis: learn more

- Resume writing: learn more

- Presentation writing: learn more

- Excel spreadsheet function: learn more

- On the existence of god: learn more

- On the meaning of life: learn more

- Doing an interview screen: learn more

- Generating tweets: learn more

- AI Dungeon: Dragon Model Upgrade: learn more

- Pretending to be stupider than it actually is? learn more

## AUTHORED BY

 Michael Balaban

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
