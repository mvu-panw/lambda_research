# Most AI teams treat compute as a commodity. It's not.

Source: https://lambda.ai/blog/most-ai-teams-treat-compute-as-a-commodity

Skip to main content

# Most AI teams treat compute as a commodity. It's not.

 May 4, 2026

 (Updated on July 29, 2026)

 • 4 min read

Consider two teams provisioning 8,192 GPUs for a large training run. Same model, same dataset, same budget. Team A lands on a facility purpose-built for AI with sufficient power density, carefully engineered liquid cooling, a high-performance network fabric, and field engineers who have tuned similar runs before. Team B lands on a conventional facility with lower redundancy, air cooling, commodity networking, and a support team that handles tickets.

Team A has a guaranteed uptime of 99.995% with fully redundant power and cooling. It reaches target throughput in four days. Team B loses days to interruptions, maintenance windows, and performance instability. Network bandwidth between nodes doesn’t keep up. Thermal throttling kicks in during peak utilization because the cooling wasn't designed for sustained AI workloads. The support team can restart nodes, but has never diagnosed a multi-thousand-GPU training failure.

By week three, Team B hasn't completed a single useful training run. The meter kept running the entire time.

Lambda's field engineers see versions of this story regularly. The teams that treat compute as interchangeable are the ones who lose weeks and budgets to problems that have nothing to do with the model.

Granted, not every workload needs all of that. Non-production inference or exploratory work runs fine on commodity compute. The problem is assuming all workloads are those workloads.

In Lambda's own Model FLOPS Utilization (MFU—how much compute each running GPU is actually capturing) research, the team increased the Llama-3.1-70B training run's MFU from 23.83% to 50.20%: the model and dataset didn't change. The infrastructure configuration did. At that gap, what could take months takes weeks, and the compute bill is halved.

As model size, batch size, and iteration speed requirements increase, compute quality becomes proportionally more important. When a team is training a frontier model or serving a model to a large population, compute quality determines whether the project ships or stalls. 

It also determines the unit economics of every downstream product. Compute is the production line converting electricity into revenue. The less efficient that line, the less viable the projects built on top of it.

Lambda learned this early. The company started as an AI application builder in 2012, hit the limits of available compute, and built its own infrastructure. It pioneered deep learning workstations and servers, then built one of the first GPU clouds. What we've learned: what separates high-performing compute from expensive underperformance falls into three categories.

## Where clusters sit

Once clusters are built, most fundamental characteristics can’t be changed. Data centers are classified on a tier system from 1 to 4. Each tier is a single rating that covers power, cooling, maintainability, and fault-tolerance. Tier 3 is designed for concurrent maintainability; Tier 4 adds fault tolerance so a single equipment failure or distribution-path interruption is absorbed before your workload notices.

The importance of latency depends on the workload. For large distributed model training, intra-cluster latency and collective communication behavior are bottlenecks. For serving models, location matters when responses go directly to an end user. Agentic workloads chain inference calls across providers, and high-speed on-ramps to other clouds decide the latency.

Other variables are harder to change after a cluster is built: the possibility of adding power, data sovereignty, and structural load limits, such as subfloor weight tolerance. These constrain what hardware you can deploy.

## How clusters are designed

The GPU count is merely one input. The real product is sustained accelerator time. That depends on the facility's power, cooling, network fabric, storage, orchestration, observability, and engineers who know how to tune the workload for the cluster.

Compute density is constrained by the full facility, not the power contract alone. Power capacity, cooling architecture, networking infrastructure, and structural load limits all set the ceiling. Think of it as a series of bottlenecks: a site may have 24 MW of contracted power, but floor-loading or layout constraints may prevent deploying enough high-density racks to fully utilize that capacity.

Hardware is only half the story. The access model (bare metal, bare metal instances, or virtualized), orchestration, and operational tooling decide how fast a team can ship on top of it.

The difference between a well-designed cluster and a poorly designed one isn't cost alone. It's how many experiments a team can run per week, how quickly they move from prototype to production, and whether a training run that should take four days takes four weeks instead.

## Who tunes the clusters

AI infrastructure evolves faster than the data centers built to house it. Buildings might still last decades, but the useful life of a cluster design is much shorter: GPU generations, cooling requirements, and power envelopes change every 12 to 13 months. Expertise is what bridges that gap.

The teams extracting full performance from their clusters span three layers: physical infrastructure, systems engineering, and ML workload optimization. Not all compute providers cover all three. The gap is where Team B lives: weeks lost to debugging, budgets burned on capacity that never produced results. In extreme cases, the cluster never converges on a stable training run at all.

## How Lambda builds what commodity providers can't

Lambda co-engineers AI clusters that maximize intelligence produced per watt. Our data center teams build the physical layer of AI factories on Tier 3 and 4 facilities. Our field engineers work with customers to unlock cluster performance. 

Our ML engineers and researchers have published over 20 peer-reviewed papers in the past 12 months alone. Recent work includes post-training OLMo with Ai2 and a reproducible guide to maximizing Model FLOPs Utilization (MFU).

The gap between "GPUs are provisioned" and "the model is training efficiently" is where Lambda's expertise has the most impact.

## Lambda at a glance

- Founded: 2012, by Stephen and Michael Balaban

- AI accelerators: NVIDIA HGX H100 Tensor Core GPU, B200, GB300 NVL72, VR200 NVL72

- AI factories: Tier 3 and 4 only, contiguous and distributed

- Product: Superclusters, 1-Click Clusters, on-demand Instances

- Compliance: SOC 2 Type II, ISO 27001

- Customers: 10k+ active, four hyperscalers, including Microsoft

Compute isn't a commodity. Three things decide whether your model ships in weeks or months: where the cluster sits, how it's designed, and who tunes it. The teams pulling ahead engineer all three. Lambda was built for them.

Talk to our team.

## AUTHORED BY

 Lambda

## SHARE ARTICLE

## SUBSCRIBE TO THE BLOG
