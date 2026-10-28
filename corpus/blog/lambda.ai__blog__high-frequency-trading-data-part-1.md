# In high-frequency trading data, noise isn't the problem. Assumptions are.

Source: https://lambda.ai/blog/high-frequency-trading-data-part-1

Skip to main content

# In high-frequency trading data, noise isn't the problem. Assumptions are.

 July 24, 2026

 • 5 min read

Lambda recently teamed with Hudson River Trading (HRT), one of the most respected quantitative trading firms in the world, to power their trading research and development on Lambda Cloud. It's a deal that reflects something we've been seeing more broadly: access to compute is a necessary condition for frontier quantitative research, but it's not sufficient. The firms doing the most ambitious work are running into a separate, harder problem in how they prepare and understand their data.

Part one of a two-part series on data preprocessing for high-frequency trading.

In the weeks since this partnership began, we’ve had the opportunity to speak with engineers and researchers at leading high-frequency trading (HFT) firms. The conversations were different in tone and focus, but one theme surfaced consistently: the data preprocessing problem.

## The problem nobody talks about publicly

High-frequency trading operates on a different plane of data complexity than almost any other machine learning (ML) domain. Raw market microstructure data (limit order book updates, trade executions, cancellations) arrives asynchronously, at nanosecond granularity, with irregular inter-event timing, heavy noise, and non-stationary statistical properties that shift across intraday regimes. It is, in a word, hostile.

The challenge isn't just cleaning the data. It's that no single normalization or preprocessing strategy works well across all market conditions. A calm pre-open session and a liquidity crunch mid-afternoon look like entirely different data-generating processes. Preprocessing pipelines that work on historical data often degrade on live data in ways that are hard to debug and harder to fix systematically.

Every firm we spoke with described a version of this: their preprocessing pipeline is either too rigid (overfitted to historical regimes) or too manual: requiring constant engineer intervention as market conditions change. Neither is sustainable at the scale and speed HFT demands.

## A different way to think about it

What struck us about these conversations is that this is fundamentally a representation learning problem dressed up as an engineering problem. The question isn't just “how do we clean the data,” it's “how do we build a system that understands the data well enough to preprocess it adaptively?”

That reframing opens up a more interesting space for solutions, and it turns out that the research community has begun to reach the same conclusion. Wu et al. (2021) at JPMorgan AI Research were among the first to make this explicit, arguing that the success of deep learning limit order book (LOB) models is highly dependent on the quality and robustness of the input data representation, and that existing literature had been focused almost entirely on architecture choices while ignoring the assumptions those architectures make about their inputs.¹

More recently, Zhong et al. (2025) conducted the first systematic comparative study of LOB representation learning, finding that existing approaches tightly couple representation learning with downstream prediction tasks end-to-end, limiting their reusability and generalization across market conditions.² The implication is clear: the field has been learning representations for tasks rather than learning representations of the market itself.

The most structurally similar work in our direction is SimLOB (2024), which proposes learning vector-valued representations of the full limit order book using a Transformer-based autoencoder.³ Rather than collapsing the LOB to a mid-price scalar, losing most microstructure information in the process, SimLOB learns a latent vector that preserves the nonlinear autocorrelation in the temporal axis and the precedence relationships between successive price levels.

It is a compelling demonstration that generative representation learning can capture LOB structure in ways hand-engineered features can’t. What it does not do is use that learned structure to adapt the system's response to new, unseen market conditions. That is the gap we are working in.

## What we're exploring

Rather than learning representations in service of a fixed downstream task, we are investigating a simple but underexplored idea: use a Bayesian framework to learn the structure of the market directly from historical order book data, and let that learned structure drive how the system preprocesses and adapts to incoming data, including across conditions it was never explicitly trained on.

The model builds a probabilistic picture of what normal looks like across different market regimes, encoding prior beliefs about market behavior that are continuously tested against incoming data. The degree to which new observations challenge those prior beliefs becomes a meaningful signal in its own right.

Quantified using a formal measure of statistical divergence, that signal distinguishes between data that is merely noisy and data that is genuinely novel; this is exactly the distinction that brittle preprocessing pipelines fail to make, and one that no fixed normalization scheme can produce, because the boundary between routine and novel shifts as market conditions shift. Getting a system to track that boundary automatically is the problem we are working on.

The challenges are real: financial data carries high irreducible noise that can confound information-theoretic signals if not handled carefully, and learned representations need to remain stable enough to be operationally reliable. But the convergence of LOB representation learning research and adjacent machine learning research, and the consistency of the problem we heard described across firms, pointed clearly toward a direction worth pursuing. In Part 2, we share what we found.

## Why this matters for Lambda

The Hudson River Trading partnership is about GPU infrastructure. But conversations like these (the same problem surfacing independently at high-frequency trading companies) suggest that the next frontier for quantitative firms isn't compute capacity alone. It's building systems that understand their data well enough not to need a human in the loop every time the market changes.

This matters for a practical reason that often goes undiscussed: preprocessing inefficiency is a GPU cost problem as much as an engineering one. When data arrives poorly normalized, inconsistently structured, or misaligned across regimes, models train longer, converge less reliably, and require more frequent retraining cycles as market conditions drift. At data-center GPU scale, that inefficiency is expensive. Adaptive preprocessing, systems that get the representation right before the data ever reaches the model, directly reduces the compute burden of the training loop.

Cleaner inputs → fewer wasted iterations → faster convergence → more efficient use of the infrastructure you're paying for.

As Machine Learning Engineers at Lambda, we work directly in this territory. A significant part of what we do is helping quantitative teams optimize how their workloads run on our infrastructure. In our experience, upstream data quality has an outsized effect on how efficiently downstream training uses the hardware. The firms that arrive with well-structured, regime-aware data representations get substantially more out of the same hardware than those still fighting their preprocessing stack mid-training run.

What makes Lambda's position distinctive here is the combination of infrastructure depth and applied ML fluency that sits behind every customer engagement. Most GPU cloud providers can provision compute. Fewer have field engineers who work at the intersection of large-scale distributed training, ML research, and the domain-specific data challenges of the industries they serve. At Lambda, the same team helping you provision your GPU cluster is also the team that can sit down with your ML engineers and work through why your preprocessing pipeline is costing you three extra hours of training time per run. That proximity between the infrastructure and research layers is not something you get from a hyperscaler.

For quantitative firms in particular, that matters. The problems described in this post are not pure infrastructure problems, and they’re not pure research problems. They live at the boundary between the two. Lambda is one of the few GPU infrastructure providers with the technical depth on both sides of that boundary to engage with them seriously, and the HRT partnership is an example of what that kind of engagement can look like in practice.

Next in this two-part series: what we built, what the results showed, and what adaptive risk management could look like for firms ready to move on it.

Recognize the pain? Talk to our team.

## References

¹ Wu Y, Mahfouz M, Magazzeni D, Veloso M. Towards robust representations of limit order books for deep learning models. arXiv. 2021. arXiv:2110.05479. Updated December 2022.

² Zhong M, Lin Y, Yang P. Representation learning of limit order book: a comprehensive study and benchmarking. arXiv. 2025. arXiv:2505.02139.

³ Li Z, Liu W, Bian J, et al. SimLOB: learning representations of limited order book for financial market simulation. arXiv. 2024. arXiv:2406.19396.

## AUTHORED BY

 Jessica Nicholson

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
