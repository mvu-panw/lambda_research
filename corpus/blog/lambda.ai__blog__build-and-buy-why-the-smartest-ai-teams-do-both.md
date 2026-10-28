# Build and buy: why the smartest AI teams do both

Source: https://lambda.ai/blog/build-and-buy-why-the-smartest-ai-teams-do-both

Skip to main content

# Build and buy: why the smartest AI teams do both

 August 24, 2026

 (Updated on October 22, 2026)

 • 5 min read

Not every workload needs a frontier model. The teams that want to keep costs predictable run open-weight models on compute they own, and save the frontier for the 10% that truly needs it.

Early this year, everyone was tokenmaxxing. Teams turned on frontier APIs across the company and let everyone build. Then the bills arrived, and the cost-to-value ratio of the tokens didn't line up. By mid-2026, finance leaders were staring at AI spend they couldn't forecast and couldn't cap, and the answer of the moment was token budgeting: a fixed dollar ceiling per person, per month.

Budgeting caps the wrong variable. You can fix how many dollars you spend, but not how much intelligence those dollars buy. Prices move, models change under you, and the rate you onboard at isn't the rate you keep. Cap the dollars, and your budget shrinks the moment a new frontier model releases. Cap the tokens, and you're rationing the capability you adopted AI for in the first place.

The real problem is allocation: sending every workload to the most expensive, least predictable tier, whether it belongs there or not.

## It's not "build or buy." It's "build and buy."

The old question was build versus buy. For an enterprise, both extremes fall short on their own.

Build alone means building from the ground up: you deploy the infrastructure yourself and build your own intelligence on top of it. In practice, this involves standing up AI hardware in a general-purpose data center that was never designed for it. The gear is CAPEX-heavy, and that's the easy part.

The most performant hardware needs water cooling. Power runs past 130kW per rack, on a path to a megawatt, well beyond what most enterprise facilities supply. A 3-trillion-parameter model like Kimi runs about $350,000 in hardware before cooling and electricity. And all of that comes before an ML engineer starts the first workflow: months of infrastructure work before you generate a single token. Not all compute is created equal, and compute is not a commodity.

On the other hand, buying alone is the other extreme: rent every token from a closed API, and your cost, your model, and your roadmap all move on another company's schedule.

There's a happier route in the middle. Specialized clouds are the fastest, most cost-efficient way to access top-of-the-line compute: deploy open-weight models, or train your own, on capacity you reserve. That path was once seen as research-only, with immature models and a wide gap to the proprietary frontier. That gap is gone. Neither extreme wins on its own. The smartest teams run both.

## The 90/10 line

Open-weight models are now in the multi-trillion-parameter range and genuinely frontier. For most of what a company does, they're good enough. A useful rule from the field: for 90% of people and 90% of tasks, open weights will do the job. The frontier still matters, and converting all of your employees to an in-house product takes time, maintenance, and resources.

Our outlook on this switch is as follows:

- 

Keep frontier models and their harnesses for specific applications and workflows, as they have passed through security audits, many teams are deeply integrated with their MCPs and workflows, and it will lead to the smallest amount of growing pains migrating to a new in-house solution.

- 

If applicable, run tests and evaluations to see whether self-hosted models behave properly in your existing tools and harnesses, to judge how much frontier models need to handle tasks like email updating, workflow editing, and other small tasks typical knowledge workers and engineers use models for.

When deciding what models to use and what tasks they need to achieve, we use this outlook:

- Frontier, closed: the bleeding edge, for the top 10% of the work. This includes problems like long-horizon tasks (auto-research), where they should always be state-of-the-art; orchestration of large-scale applications; and the harness-specific reasons we mentioned a moment ago.

- Open-weight workhorse, such as GLM 5.2: the bulk of real, everyday production.

- Small and efficient, such as DeepSeek v4 Flash: fast, cheap, and already running in frontier labs every day.

One frontier research lab, Noumena, runs their entire lab on a single NVIDIA GB300 NVL72, two open-weight models, and a custom harness, at roughly 5 billion tokens a month. Most companies don't need the top tier for every team and every workload. They need the discipline to put each workload where it belongs.

## The economics that finally match a CFO's efficiency bar

CFOs have spent two years hearing that AI is worth whatever it costs. This is the version where the numbers finally meet the standard you hold every other line item to. The discount matters. Predictability matters more. Reserved compute at a fixed dollar-per-GPU-per-hour is a known number for the term. An API bill moves with usage, and with price changes you don't control.

Make it concrete. Take a team running a capable open model on a Lambda 1-Click Cluster for a fixed term, priced at public rates, and compare it, like-for-like, against renting the same workload from a closed API. Then split the work 90/10 instead of sending all of it to the frontier.

Left: Each point represents a concurrency level; moving right means faster output per user, while moving up means greater throughput per GPU. Labels such as C64 indicate 64 concurrent requests.

Right: Estimated infrastructure cost per 400-output-token request at each concurrency level. Lower is cheaper; the dashed line shows the comparable official GLM-5.2 API-price proxy.

## The upside of owning the model

Two advantages compound once the deployment is yours.

First, no one can pull the rug. When the model you depend on is a closed API, a provider or a regulator can restrict it, and the feature you built on it stalls. It's happened. Open weights you host stay available on your terms, and to every employee, wherever they sit and whatever their passport says.

Second, you can make the model yours. Fine-tune it on your own data, and the advantage accumulates inside your walls. Give two companies the same open model and five years, and the one that learned to train on its own data pulls ahead. Privacy comes from the architecture: the compute is yours, and nothing leaves for an outside party to see.

None of this is a knock on frontier models. They're exceptional, and for frontier work they're the answer. The point is simpler: for most of your workloads, you have a more predictable option you actually control.

## Choose both

Ask the allocation question out loud. Which work truly needs the frontier, and which of your proven, in-production workloads could run on open weights, on compute you control? Put your top talent on the frontier. Move the 90% to a cluster you own. That's build and buy, and it's the most defensible cost equation in AI right now.

You don't have to work out the split alone. Lambda brings both halves: the compute and the ML engineers to help you size it and get started.

To request a sizing conversation, talk to our team.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
